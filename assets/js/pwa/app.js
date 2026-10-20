---
layout: compress
permalink: '/app.js'
---

if ('serviceWorker' in navigator) {
    /* 只注册，不提示、不强刷。正文时效性由 sw.js 的导航请求直连网络保证 */
    navigator.serviceWorker.register('{{ "/sw.js" | relative_url }}');
}

