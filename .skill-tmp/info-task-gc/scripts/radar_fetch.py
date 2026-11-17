#!/usr/bin/env python3
"""资讯雷达取数层：把已实测可机器读取的来源归一化成 NDJSON，并做跨天去重。

用法：
  python3 radar_fetch.py --all --days 2                 # 全量取，只要近 2 天
  python3 radar_fetch.py --source epic,hn --limit 10     # 只取指定来源
  python3 radar_fetch.py --all --seen state/history.jsonl --append state/history.jsonl
  python3 radar_fetch.py --lookup 6753570922             # 按 App Store id 核国区现价
  python3 radar_fetch.py --lookup "Idle Isle"            # 按名字搜，只出候选（国区会改名）

输出一行一条 JSON：{id, cat, source, title, url, price, until, ts, extra}
末尾一行 SUMMARY；某个来源挂了只打 ERR 行，不影响其余来源。
"""
import argparse
import datetime as dt
import json
import os
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
PROXY = os.environ.get("INFO_PROXY", "http://127.0.0.1:7897")
PROXY_ONLY = os.environ.get("INFO_PROXY_ONLY") == "1"
CTX = ssl.create_default_context()


class _Follow308(urllib.request.HTTPRedirectHandler):
    """urllib 只跟 301/302/303/307；CoinDesk 的 RSS 回 308，不处理就当取数失败。"""

    def http_error_308(self, req, fp, code, msg, headers):
        # redirect_request 的白名单只有 301/302/303/307，直接透传 308 会被它抛错；
        # GET 请求下 307 与 308 语义一致，按 307 交给父类走重定向。
        return self.http_error_301(req, fp, 307, msg, headers)


def _opener(proxy_url):
    handlers = [urllib.request.HTTPSHandler(context=CTX),
                urllib.request.HTTPHandler(),
                _Follow308()]
    if proxy_url:
        handlers.append(urllib.request.ProxyHandler(
            {"http": proxy_url, "https": proxy_url}))
    else:
        handlers.append(urllib.request.ProxyHandler({}))
    return urllib.request.build_opener(*handlers)


def http_get(url, timeout=20):
    """境外站在本机无直连出口，先走 INFO_PROXY 再回落直连。

    代理偶发连接重置（同一 URL 一次 200 一次 URLError），每个通道重试一次。
    """
    last = None
    for proxy in ((PROXY,) if PROXY_ONLY else (PROXY, None)):
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                           "Accept-Language": "zh-CN,zh;q=0.9"})
                with _opener(proxy).open(req, timeout=timeout) as r:
                    return r.read(), r.status
            except (urllib.error.URLError, socket.timeout, ssl.SSLError, OSError) as e:
                last = e
                if attempt == 0:
                    time.sleep(2)
    raise last


def text_of(raw):
    return raw.decode("utf-8", "ignore")


def norm(source, cat, title, url, price=None, until=None, ts=None, extra=None,
         ident=None):
    title = re.sub(r"\s+", " ", (title or "").strip())[:220]
    key = ident or url
    slug = re.sub(r"[^a-z0-9]+", "-", key.lower())[:70]
    return {"id": "%s:%s" % (source, slug), "cat": cat, "source": source,
            "title": title, "url": url, "price": price,
            "until": until, "ts": ts, "extra": extra}


def recent(iso, days):
    if not iso or days <= 0:
        return True
    then = None
    try:
        then = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            then = parsedate_to_datetime(iso).date()
        except (TypeError, ValueError):
            return True
    return (dt.date.today() - then).days <= days


# ---------------------------------------------------------------- sources
def src_epic():
    url = ("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
           "?locale=zh-CN&country=CN&allowCountries=CN")
    raw, _ = http_get(url)
    els = json.loads(text_of(raw))["data"]["Catalog"]["searchStore"]["elements"]
    out = []
    for e in els:
        price_obj = e.get("price") or {}
        tp = price_obj.get("totalPrice") or {}
        original, discount = tp.get("originalPrice"), tp.get("discountPrice")
        fmt = (tp.get("fmtPrice") or {})
        until = None
        for lo in price_obj.get("lineOffers") or []:
            for rule in lo.get("appliedRules") or []:
                until = rule.get("endDate") or until
        if discount == 0 and original:
            kind = "本周限免（原价 %s）" % (fmt.get("originalPrice") or "")
        elif discount is not None and original and discount < original:
            kind = "打折 %s→%s" % (fmt.get("originalPrice"), fmt.get("discountPrice"))
        else:
            continue
        title = (e.get("title") or "").strip()
        out.append(norm("epic-store", "freebie", title,
                        "https://store.epicgames.com/free-games?lang=zh-CN",
                        (original or 0) / 100.0, until, until, kind,
                        ident=title))
    return out


def src_hn():
    url = "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30"
    raw, _ = http_get(url)
    hits = json.loads(text_of(raw))["hits"]
    return [norm("hackernews", "tech-news", h.get("title"),
                 h.get("url") or "https://news.ycombinator.com/item?id=%s" % h.get("objectID"),
                 None, None, h.get("created_at"),
                 "%s 分 / %s 评" % (h.get("points"), h.get("num_comments")))
            for h in hits]


def src_lobsters():
    raw, _ = http_get("https://lobste.rs/hottest.json")
    return [norm("lobsters", "tech-news", it.get("title"),
                 it.get("url") or "https://lobste.rs%s" % it.get("path", ""),
                 None, None, it.get("created_at"),
                 "%s 赞 / %s 评" % (it.get("score"), it.get("comment_count")))
            for it in json.loads(text_of(raw))[:20]]


def src_v2ex():
    raw, _ = http_get("https://www.v2ex.com/api/topics/hot.json")
    return [norm("v2ex", "tech-news", it.get("title"), it.get("url"),
                 None, None, dt.datetime.utcfromtimestamp(
                     it.get("created", 0)).isoformat() if it.get("created") else None,
                 "%s 回" % it.get("replies"))
            for it in json.loads(text_of(raw))[:20]]


def src_hf_papers():
    raw, _ = http_get("https://huggingface.co/api/daily_papers?limit=15")
    out = []
    for it in json.loads(text_of(raw)):
        p = it.get("paper") or {}
        out.append(norm("hf-daily-papers", "ai-updates", p.get("title"),
                        "https://huggingface.co/papers/%s" % p.get("id"),
                        None, None, it.get("publishedAt"),
                        "up%s" % p.get("upvotes")))
    return out


def src_github_trending():
    raw, _ = http_get("https://github.com/trending?since=daily")
    html = text_of(raw)
    out = []
    for m in re.finditer(r'<h2 class="h3 lh-condensed">\s*<a[^>]*?href="/([^"]+)"',
                         html):
        repo = m.group(1).strip("/")
        blk = html[m.end():m.end() + 3000]
        desc = re.search(r'<p class="col-9[^"]*">\s*(.*?)\s*</p>', blk, re.S)
        star = re.search(r'href="/%s/stargazers"[^>]*>(.*?)</a>' % re.escape(repo),
                         blk, re.S)
        note = re.sub(r"<[^>]+>", "", desc.group(1)).strip() if desc else ""
        stars = re.sub(r"[^\d,]", "", re.sub(r"<[^>]+>", " ",
                                             star.group(1))).strip(",") if star else ""
        out.append(norm("github-trending", "dev-tools", repo,
                        "https://github.com/%s" % repo, None, None, None,
                        (note[:120] + (" | %s star" % stars if stars else ""))))
    return out


def parse_rss(raw, source, cat, limit=20, title_words=None):
    html = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", text_of(raw))
    root = ET.fromstring(html.encode("utf-8", "ignore"))

    def keep(title):
        return not title_words or any(w in title for w in title_words)

    out = []
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = (it.findtext("pubDate") or "").strip()
        if keep(title):
            out.append(norm(source, cat, title, link, None, None, pub))
        if len(out) >= limit:
            break
    if not out:
        for it in root.iter("{http://www.w3.org/2005/Atom}entry"):
            title = (it.findtext("{http://www.w3.org/2005/Atom}title") or "").strip()
            l = it.find("{http://www.w3.org/2005/Atom}link")
            link = l.get("href") if l is not None else ""
            if not keep(title):
                continue
            out.append(norm(source, cat, title, link, None, None,
                            it.findtext("{http://www.w3.org/2005/Atom}updated")))
            if len(out) >= limit:
                break
    return out


def src_lowendbox():
    raw, _ = http_get("https://lowendbox.com/feed/")
    return parse_rss(raw, "lowendbox", "deal", 15)


def src_steam():
    raw, _ = http_get("https://store.steampowered.com/api/featuredcategories"
                      "?cc=cn&l=schinese", timeout=40)
    spec = (json.loads(text_of(raw)) or {}).get("specials") or {}
    out = []
    for it in spec.get("items") or []:
        pct = it.get("discount_percent") or 0
        if not pct:
            continue
        final = (it.get("final_price") or 0) / 100.0
        origin = (it.get("original_price") or 0) / 100.0
        exp = it.get("discount_expiration")
        out.append(norm("steam", "deal", it.get("name"),
                        "https://store.steampowered.com/app/%s/?l=schinese" % it.get("id"),
                        final,
                        dt.datetime.utcfromtimestamp(exp).isoformat() if exp else None,
                        None, "原价 ¥%.2f → ¥%.2f（-%s%%）" % (origin, final, pct),
                        ident=str(it.get("id"))))
    return out


def src_idcspy():
    raw, _ = http_get("https://www.idcspy.com/feed")
    return parse_rss(raw, "idcspy", "deal", 12)


def src_ruanyifeng():
    raw, _ = http_get("https://www.ruanyifeng.com/blog/atom.xml")
    return parse_rss(raw, "ruanyifeng-weekly", "tech-news", 8)


def src_ithome():
    raw, _ = http_get("https://www.ithome.com/rss/")
    return parse_rss(raw, "ithome", "tech-news", 25)


def src_producthunt():
    raw, _ = http_get("https://www.producthunt.com/feed")
    return parse_rss(raw, "producthunt", "ai-updates", 15)


# ---------------------------------------------------------------- app store
# App Store 没有官方限免接口，所以分两层：
#   发现 = 免登录的限免汇总通道（Telegram 频道公开预览、小众软件 RSS）
#   核实 = 播报正文里的 apps.apple.com id → iTunes lookup 读该区商店现价
# 认 id 不认名字：国区会把 app 改名（Idle Isle 上架名「发呆岛」），按名字 search
# 会认错另一个 app 并把它的价格安到限免条目上（实测踩过）。
# price==0 只证明「今天下载不花钱」，接口分不出本就免费和促销中；内购限免改的是
# 内购价，下载价上看不出来。Apple 不给促销截止时间（实测页面无「限时优惠」字样），
# 所以 until 一律 None，不许编一个截止日期。
IOS_CHANNEL = "TossTF"                 # t.me/s/<channel> 免登录公开预览，每天数条 iOS 限免
APPSTORE_VERIFY_MAX = 15               # 一轮最多核价多少条，超出的标「未核价」
APPSTORE_EMPTY_WORDS = ("限免", "免费", "促销", "秒送", "0元", "骨折")


def _strip_tags(html_fragment):
    txt = re.sub(r"<br\s*/?>", "\n", html_fragment)
    txt = re.sub(r"<[^>]+>", "", txt)
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " ")):
        txt = txt.replace(a, b)
    return txt


def _clean_track_url(u):
    return re.sub(r"[?&](at|uo|app|ign|ct|cc)=[^&]*", "", u or "").rstrip("?&")


def _itunes_json(url):
    raw, _ = http_get(url, timeout=25)
    return json.loads(text_of(raw)).get("results") or []


def itunes_by_id(track_id, country="cn"):
    """按 App Store id 取该地区商店的现行价。免 key、免登录。查不到返回 None。

    id 是唯一可靠的对应关系：国区会把 app 改名（Idle Isle 上架名是「发呆岛」），
    按 app 名去 search 会认错另一个同名 app 并把它的价格安到限免条目上（实测踩过）。
    """
    rs = _itunes_json("https://itunes.apple.com/lookup?id=%s&country=%s"
                      % (track_id, country))
    return rs[0] if rs else None


def itunes_search(term, country="cn", limit=6):
    """按名字搜，只用于人工抽查——国区常改名，返回结果不保证是同一个 app。"""
    q = urllib.parse.quote(term.strip()[:80])
    return _itunes_json("https://itunes.apple.com/search?media=software"
                        "&country=%s&limit=%d&term=%s" % (country, limit, q))


def src_appinn():
    """小众软件 RSS：只留标题带限免/免费/促销字样的条目。

    它的「限免」tag 归档页实测不是按时间倒序（首条 2026-06、次条 2026-04），
    列表页也没有日期，所以不能当新帖源用；这里走带 pubDate 的主 feed。
    这两天没限免帖是常态，allow_empty 让 main() 别把它当改版报警。
    """
    raw, _ = http_get("https://www.appinn.com/feed/")
    items = parse_rss(raw, "appinn", "freebie", 12,
                      title_words=APPSTORE_EMPTY_WORDS)
    for it in items:
        it["extra"] = "小众软件转述，未回官方页核价（iOS/macOS/Windows 任一端）"
    return items


src_appinn.allow_empty = True


def src_tosstf():
    """TossTF 的 iOS 限免播报：t.me/s/ 预览页免登录，消息带 datetime 和 App Store 直链。

    核实走 id：每条播报的正文里都挂着 apps.apple.com/app/id<trackId>，
    拿这个 id 回 iTunes lookup 的国区记录读现价。读到的口径只有三种——
      price==0  → 国区现价免费（下载不花钱；但接口分不出「本就免费」和「促销中」）
      price>0   → 播报的限免已失效或已改价
      国区无此 id → 播报给的是别的区，按那个区核一次并注明
    内购限免改的是内购价，不体现在下载价上，所以这一类一律标「未核实」。
    核价额度优先给最新的条目（越新的限免越可能还在）。
    """
    raw, _ = http_get("https://t.me/s/%s" % IOS_CHANNEL)
    html = text_of(raw)
    cuts = [m.start() for m in re.finditer(r'data-post="%s/(\d+)"' % IOS_CHANNEL, html)]
    cuts.append(len(html))
    pending = []
    for i, start in enumerate(cuts[:-1]):
        chunk = html[start:cuts[i + 1]]
        m_id = re.search(r'data-post="%s/(\d+)"' % IOS_CHANNEL, chunk)
        m_time = re.search(r'<time datetime="([^"]+)"', chunk)
        m_body = re.search(
            r'<div class="tgme_widget_message_text[^"]*"[^>]*>([\s\S]*?)</div>', chunk)
        if not (m_id and m_body):
            continue
        raw_body = m_body.group(1)
        body = _strip_tags(raw_body)
        if "限免" not in body:
            continue
        lines = [l.strip() for l in body.split("\n") if l.strip()]
        name = ""
        for l in lines:
            if "//" in l:
                name = l.split("//")[0].strip()
                break
        if not name:
            for l in lines:                     # 退回首个 #CamelCase 标签（就是 app 名）
                m_tag = re.match(r"^#([A-Za-z][\w\-]{2,})", l)
                if m_tag:
                    name = m_tag.group(1)
                    break
        if not name:
            continue
        hrefs = re.findall(r'<a[^>]+href="(https?://[^"]+)"', raw_body)
        store = next((h for h in hrefs if "apps.apple.com" in h), "")
        m_tid = re.search(r"/app/id(\d+)", store)
        m_geo = re.search(r"apps\.apple\.com/([a-z]{2})/app/", store)
        pending.append({
            "name": name,
            "kind": "本体限免" if "本体限免" in body else (
                "内购限免" if "内购限免" in body else "限免"),
            "post": "https://t.me/%s/%s" % (IOS_CHANNEL, m_id.group(1)),
            "ts": m_time.group(1) if m_time else None,
            "id": m_tid.group(1) if m_tid else "",
            "store": store,
            "geo": m_geo.group(1) if m_geo else "cn",
        })

    out = []
    budget = APPSTORE_VERIFY_MAX
    for p in reversed(pending):                 # 最新的先核价
        note = [p["kind"]]
        price, url, ident = None, p["post"], None
        if "/redeem" in p["store"]:
            note.append("兑换码型限免，兑换码不转载，回原帖自取")
        elif not p["id"]:
            note.append("播报正文里没有 App Store 直链，无从核实 id")
        elif budget > 0:
            budget -= 1
            rec = None
            try:
                rec = itunes_by_id(p["id"], "cn")
                used_geo = "cn"
                if not rec and p["geo"] != "cn":
                    rec = itunes_by_id(p["id"], p["geo"])
                    used_geo = p["geo"]
            except Exception:
                rec = None                      # 核价挂掉只降级这一条，不拖垮整源
                used_geo = "cn"
            if rec:
                cur = float(rec.get("price") or 0)
                price = cur
                ident = "%s-%s" % (p["id"], (p["ts"] or "")[:10])  # 次日仍在要重报
                url = _clean_track_url(rec.get("trackViewUrl")) or p["store"]
                geo_label = "国区" if used_geo == "cn" else "%s区" % used_geo
                note.append("iTunes %s实测现价 %s" % (
                    geo_label, rec.get("formattedPrice") or "免费"))
                note.append("商店名 %s / %s" % (rec.get("trackName"),
                                                rec.get("sellerName")))
                if cur == 0:
                    note.append("下载不花钱（接口分不出本就免费与促销中）")
                else:
                    note.append("现价非 0：播报的限免已失效或已改价")
                if rec.get("minimumOsVersion"):
                    note.append("最低系统 %s" % rec["minimumOsVersion"])
            else:
                note.append("iTunes 按 id %s 查不到上架记录，价格未核实" % p["id"])
        else:
            note.append("未走 iTunes 核价（超出本轮核价上限）")
        if p["kind"] == "内购限免":
            note.append("内购解锁价不体现在下载价上，这一项只算转述")
        note.append("Apple 不公布限免截止时间")
        out.append((p, norm("appstore-ios", "freebie",
                            "%s（%s）" % (p["name"], p["kind"]), url, price,
                            None, p["ts"], "｜".join(note),
                            ident=ident or "appstore-%s-%s" % (
                                p["id"] or p["post"].rsplit("/", 1)[-1],
                                (p["ts"] or "")[:10]))))
    return [it for _, it in sorted(out, key=lambda x: x[0]["ts"] or "")]


# ---------------------------------------------------------------- crypto
# 币圈四轴：交易所公告 / 行情榜单 / 项目方一手 / 媒体转述。
# 行情快照类必须把日期写进 id，否则跨天去重会把第二天的榜单整批吃掉。
TODAY = dt.date.today().isoformat()

BINANCE_CATALOGS = (
    (48, "上币与新交易对"),
    (49, "新产品与活动"),
    (51, "技术与 API 变更"),
)
MARKET_RANK_MAX = 300       # 异动只看市值前 300：按 24h 涨幅全局排序时榜首是 rank 485、+44914% 的山寨币，纯噪声
MARKET_MIN_MOVE = 8.0
CRYPTO_CORE_REPOS = ("ethereum/go-ethereum", "anza-xyz/agave")
EXCHANGE_STATUS_PAGES = (
    ("Coinbase", "https://status.coinbase.com/api/v2/status.json"),
    ("Kraken", "https://status.kraken.com/api/v2/status.json"),
)


def src_binance():
    out = []
    for cid, label in BINANCE_CATALOGS:
        url = ("https://www.binance.com/bapi/composite/v1/public/cms/article"
               "/catalog/list/query?catalogId=%d&pageNo=1&pageSize=6" % cid)
        try:
            raw, _ = http_get(url)
            arts = (json.loads(text_of(raw)).get("data") or {}).get("articles") or []
        except Exception:
            if out:                      # 三个 catalog 挂一个不算整源失败
                continue
            raise
        for a in arts:
            title, code = (a.get("title") or "").strip(), a.get("code")
            if not title or not code:
                continue
            m = re.search(r"20\d{2}-\d{2}-\d{2}", title)   # 日期只写在标题里，接口不返回
            out.append(norm("binance-ann", "crypto-exchange", title,
                            "https://www.binance.com/en/support/announcement/detail/%s" % code,
                            None, None, m.group(0) if m else None,
                            "币安公告 · %s（英文原文，中文转述看 panews）" % label,
                            ident=code))
    return out


def src_exchange_status():
    """交易所服务状态：Statuspage 的 status.json 是唯一实测机器可读的「影响在用」信号。

    只两家可用（status.bybit/bitget/okx/kucoin/mexc/upbit/gate 这些域名实测不存在，
    Binance 的 simple-status 是 403），所以合成一条而不是每家一条。
    """
    parts, ok = [], 0
    for name, url in EXCHANGE_STATUS_PAGES:
        try:
            raw, _ = http_get(url)
            st = (json.loads(text_of(raw)) or {}).get("status") or {}
        except Exception:
            if ok:
                parts.append("%s 本轮未取到" % name)
                continue
            raise
        ok += 1
        parts.append("%s %s" % (name, st.get("description") or st.get("indicator") or "?"))
    return [norm("exchange-status", "crypto-exchange",
                 "交易所服务状态：%s" % ("、".join(p.split()[0] for p in parts)),
                 "https://status.coinbase.com", None, None, TODAY,
                 "｜".join(parts) + "｜非 none 即需在用资产复查",
                 ident="exchange-status-%s" % TODAY)]


def _fmt_usd(n):
    """金额压成 K/M/B/T，避免 extra 里出现 5.1e+08 这种没法进报告的写法。

    CoinGecko 两个接口的金额形态不一致：markets 给 float，trending 给
    '$1,626,655,750,585' 这种已格式化字符串，所以先剥掉非数字再转。
    """
    if isinstance(n, str):
        n = re.sub(r"[^\d.]", "", n)
    try:
        n = float(n or 0)
    except (TypeError, ValueError):
        return str(n)
    for unit, div in (("T", 1e12), ("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if n >= div:
            return "$%.2f%s" % (n / div, unit)
    return "$%.4f" % n


def src_cg_trending():
    raw, _ = http_get("https://api.coingecko.com/api/v3/search/trending")
    out = []
    for c in (json.loads(text_of(raw)).get("coins") or [])[:10]:
        it = c.get("item") or {}
        d = it.get("data") or {}
        price, ch = d.get("price"), (d.get("price_change_percentage_24h") or {}).get("usd")
        out.append(norm("coingecko-trending", "crypto-market",
                        "%s (%s)" % (it.get("name"), it.get("symbol")),
                        "https://www.coingecko.com/en/coins/%s" % (it.get("slug") or it.get("id")),
                        price, None, TODAY,
                        "CoinGecko 热搜榜 · 现价 $%s｜24h %s｜市值 %s" % (
                            ("%.6g" % price) if price else "?",
                            ("%+.1f%%" % ch) if ch is not None else "?",
                            _fmt_usd(d.get("market_cap")) if d.get("market_cap") else "?"),
                        ident="%s-%s" % (it.get("id"), TODAY)))
    return out


def src_cmc():
    # 涨幅榜不走 CMC：该接口按 percent_change_24h 排序时前 50 条是 rank 485~7400
    # 的山寨币（最高 +44914%），限制 rank<=300 后一条不剩；异动改由 src_cg_markets 出。
    raw, _ = http_get("https://api.coinmarketcap.com/data-api/v3/topsearch/rank")
    ranks = (json.loads(text_of(raw)).get("data") or {}).get("cryptoTopSearchRanks") or []
    return [norm("coinmarketcap-search", "crypto-market",
                 "CMC 热搜：%s (%s)" % (r.get("name"), r.get("symbol")),
                 "https://coinmarketcap.com/currencies/%s/" % r.get("slug"),
                 None, None, TODAY,
                 "CMC 搜索榜第 %d 位（热度，不是涨跌）" % i,
                 ident="%s-%s" % (r.get("id"), TODAY))
            for i, r in enumerate(ranks[:6], 1)]


def src_cg_markets():
    raw, _ = http_get("https://api.coingecko.com/api/v3/coins/markets"
                      "?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
                      "&price_change_percentage=24h", timeout=30)
    rows = json.loads(text_of(raw))
    majors = [r for r in rows if r.get("current_price") is not None]
    if not majors:
        return []
    snap = "｜".join("%s $%.6g (%+.1f%%)" % (
        r["symbol"].upper(), r["current_price"],
        r.get("price_change_percentage_24h") or 0) for r in majors[:5])
    out = [norm("coingecko-markets", "crypto-market",
                "市值前 5 快照（24h）", "https://www.coingecko.com/en/coins",
                majors[0]["current_price"], None, TODAY,
                snap + "｜行情快照，不构成任何操作建议",
                ident="cg-snapshot-%s" % TODAY)]
    movers = sorted(
        [r for r in majors if r.get("price_change_percentage_24h") is not None
         and abs(r["price_change_percentage_24h"]) >= MARKET_MIN_MOVE
         and (r.get("market_cap_rank") or 9999) <= MARKET_RANK_MAX],
        key=lambda r: -abs(r["price_change_percentage_24h"]))[:6]
    for r in movers:
        ch = r["price_change_percentage_24h"]
        out.append(norm("coingecko-markets", "crypto-market",
                        "%s (%s) 24h %+.1f%%" % (r["name"], r["symbol"].upper(), ch),
                        "https://www.coingecko.com/en/coins/%s" % r["id"],
                        r["current_price"], None, TODAY,
                        "市值榜 rank %s｜现价 $%.6g｜24h 额 %s" % (
                            r.get("market_cap_rank"), r["current_price"],
                            _fmt_usd(r.get("total_volume"))),
                        ident="%s-%s" % (r["id"], TODAY)))
    return out


def src_fng():
    raw, _ = http_get("https://api.alternative.me/fng/?limit=1")
    d = (json.loads(text_of(raw)).get("data") or [{}])[0]
    if not d.get("value"):
        return []
    return [norm("fng-index", "crypto-market",
                 "恐惧贪婪指数 %s（%s）" % (d.get("value"), d.get("value_classification")),
                 "https://alternative.me/crypto/fear-and-greed-index/",
                 None, None, TODAY,
                 "行情情绪底数，只用于判断语境，不构成任何操作建议",
                 ident="fng-%s" % TODAY)]


def src_ethblog():
    raw, _ = http_get("https://blog.ethereum.org/feed.xml")
    return parse_rss(raw, "ethereum-blog", "crypto-project", 6)


def src_crypto_releases():
    out = []
    for repo in CRYPTO_CORE_REPOS:
        raw, _ = http_get("https://api.github.com/repos/%s/releases?per_page=2" % repo)
        for r in json.loads(text_of(raw)):
            if r.get("draft") or not r.get("html_url"):
                continue
            out.append(norm("crypto-release", "crypto-project",
                            "%s → %s" % (repo, r.get("tag_name") or r.get("name")),
                            r.get("html_url"), None, None, r.get("published_at"),
                            "核心客户端发版（项目方一手）：%s" % (r.get("name") or "")[:90]))
    return out


def src_coindesk():
    raw, _ = http_get("https://www.coindesk.com/arc/outboundfeeds/rss/")
    return parse_rss(raw, "coindesk", "crypto-news", 12)


def src_theblock():
    raw, _ = http_get("https://www.theblock.co/rss.xml")
    return parse_rss(raw, "theblock", "crypto-news", 12)


def src_panews():
    raw, _ = http_get("https://www.panewslab.com/rss.xml")
    return parse_rss(raw, "panews", "crypto-news", 15)


SOURCES = {
    "epic": src_epic,
    "hn": src_hn,
    "lobsters": src_lobsters,
    "v2ex": src_v2ex,
    "hf": src_hf_papers,
    "trending": src_github_trending,
    "lowendbox": src_lowendbox,
    "steam": src_steam,
    "idcspy": src_idcspy,
    "ruanyifeng": src_ruanyifeng,
    "ithome": src_ithome,
    "producthunt": src_producthunt,
    "binance": src_binance,
    "exstatus": src_exchange_status,
    "coingecko": src_cg_trending,
    "cgmarkets": src_cg_markets,
    "cmc": src_cmc,
    "fng": src_fng,
    "ethblog": src_ethblog,
    "creleases": src_crypto_releases,
    "coindesk": src_coindesk,
    "theblock": src_theblock,
    "panews": src_panews,
    "appstore": src_tosstf,
    "appinn": src_appinn,
}

# --source 支持组名，省得每次手敲十个 key
GROUPS = {
    "crypto": ["binance", "exstatus", "coingecko", "cgmarkets", "cmc",
               "fng", "ethblog", "creleases", "coindesk", "theblock", "panews"],
    "deal": ["epic", "lowendbox", "idcspy", "steam", "appstore", "appinn"],
    "news": ["hn", "lobsters", "v2ex", "hf", "trending", "ruanyifeng",
             "ithome", "producthunt"],
}


def load_seen(path):
    seen = set()
    if not path or not os.path.exists(path):
        return seen
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                seen.add(json.loads(line).get("id"))
            except json.JSONDecodeError:
                pass
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="逗号分隔，如 epic,hn；缺省=全部")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--days", type=int, default=0, help="只保留近 N 天有时间戳的条目")
    ap.add_argument("--limit", type=int, default=25, help="每个来源最多几条")
    ap.add_argument("--seen", help="历史 jsonl，用于跨天去重")
    ap.add_argument("--append", help="把本次新条目追加进这个 jsonl")
    ap.add_argument("--lookup", help="核一个 app 的国区现价：给 trackId 最准，给名字只出候选")
    ap.add_argument("--country", default="cn", help="--lookup 的地区，默认 cn")
    args = ap.parse_args()

    if args.lookup:
        arg = args.lookup.strip()
        if re.fullmatch(r"\d+", arg):
            rec = itunes_by_id(arg, args.country)
            if not rec:
                print("LOOKUP id %s｜%s 区商店查不到这个 id" % (arg, args.country))
                return 1
            recs = [rec]
        else:
            recs = itunes_search(arg, args.country)
            if not recs:
                print("LOOKUP %s｜%s 区搜不到同名应用" % (arg, args.country))
                return 1
            print("LOOKUP 名字「%s」—— 国区常给 app 改名，以下只是候选，认 id 不认名字"
                  % arg)
        for rec in recs:
            cur = float(rec.get("price") or 0)
            print("  %-46s id %-12s %s%s" % (
                rec.get("trackName"), rec.get("trackId"),
                rec.get("formattedPrice"),
                "  ← 现价为 0" if cur == 0 else ""))
        if re.fullmatch(r"\d+", arg):
            print("  官方页 : %s" % _clean_track_url(recs[0].get("trackViewUrl")))
            print("  开发商 : %s｜最低系统 %s" % (
                recs[0].get("sellerName"), recs[0].get("minimumOsVersion")))
        print("  口径   : Apple 不公布限免截止时间；内购限免不体现在下载价上")
        return 0

    names = list(SOURCES) if (args.all or not args.source) else \
        [s.strip() for s in args.source.split(",") if s.strip()]
    names = [n for spec in names for n in GROUPS.get(spec, [spec])]
    seen = load_seen(args.seen)
    fresh_fp = open(args.append, "a", encoding="utf-8") if args.append else None

    total, fresh_n, errs = 0, 0, []
    for name in names:
        fn = SOURCES.get(name)
        print("BEGIN source=%s" % name, file=sys.stderr, flush=True)
        if not fn:
            errs.append("ERR source=%s hint=未知来源" % name)
            continue
        try:
            items = fn()
        except Exception as e:  # noqa: BLE001 - 单来源失败不能拖垮整轮
            code = getattr(e, "code", "")
            errs.append("ERR source=%s %s hint=%s" % (
                name, code or type(e).__name__,
                "403 类需走浏览器桥，见 references/sources.md"))
            continue
        print("DONE source=%s items=%d" % (name, len(items)), file=sys.stderr, flush=True)
        if not items:
            if getattr(fn, "allow_empty", False):
                print("INFO source=%s empty=本轮无符合条件的新条目（非故障）" % name)
            else:
                errs.append("ERR source=%s empty hint=来源改版或解析失效，手工打开核对再改脚本" % name)
            continue
        kept = 0
        for it in items:
            total += 1
            if it["id"] in seen or not recent(it.get("ts"), args.days):
                continue
            seen.add(it["id"])
            fresh_n += 1
            kept += 1
            print(json.dumps(it, ensure_ascii=False))
            if fresh_fp:
                fresh_fp.write(json.dumps(it, ensure_ascii=False) + "\n")
            if kept >= args.limit:
                break
    if fresh_fp:
        fresh_fp.close()
    for line in errs:
        print(line)
    print("SUMMARY fetched=%d fresh=%d sources=%d errors=%d" % (
        total, fresh_n, len(names), len(errs)))


if __name__ == "__main__":
    sys.exit(main())
