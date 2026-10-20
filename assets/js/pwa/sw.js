---
layout: compress
permalink: '/sw.js'
# PWA service worker
---

self.importScripts('{{ "/assets/js/data/swcache.js" | relative_url }}');

const cacheName = 'chirpy-{{ "now" | date: "%s" }}';

function verifyDomain(url) {
  for (const domain of allowedDomains) {
    const regex = RegExp(`^http(s)?:\/\/${domain}\/`);
    if (regex.test(url)) {
      return true;
    }
  }

  return false;
}

function isExcluded(url) {
  for (const item of denyUrls) {
    if (url === item) {
      return true;
    }
  }
  return false;
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(resource);
    })
  );

  /* 装好即接管，不进 waiting 状态：缓存里那份旧 app.js 就再也读不到 waiting，弹窗条件被从源头抹掉 */
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== cacheName) {
            return caches.delete(key);
          }
        })
      );
    })
  );
});

self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

self.addEventListener('fetch', (event) => {
  /* 页面导航：优先走网络，保证部署后立刻能读到新文章；断网时才回落到缓存 */
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          if (response.ok) {
            let responseToCache = response.clone();

            caches.open(cacheName).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }

          return response;
        })
        .catch(() => caches.match(event.request))
    );

    return;
  }

  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }

      return fetch(event.request).then((response) => {
        const url = event.request.url;

        if (
          event.request.method !== 'GET' ||
          !verifyDomain(url) ||
          isExcluded(url)
        ) {
          return response;
        }

        /* see: <https://developers.google.com/web/fundamentals/primers/service-workers#cache_and_return_requests> */
        let responseToCache = response.clone();

        caches.open(cacheName).then((cache) => {
          /* console.log('[sw] Caching new resource: ' + event.request.url); */
          cache.put(event.request, responseToCache);
        });

        return response;
      });
    })
  );
});
