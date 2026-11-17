# 来源现状表（2026-10-15 实测）

本表的每一条都是**本机本轮实际请求过**的：状态码、条数、需要什么通道，都记实测结果，不含凭记忆写的 URL。判读原则：**没在这里出现的源＝没验证过，不要直接用**；要加就按第五节流程先实测。

## 一、网络前提

- 本机 `curl` **不走系统代理**，境外站必须显式 `-x http://127.0.0.1:7897`；`radar_fetch.py` 里已经做成「先试 `INFO_PROXY`（默认 127.0.0.1:7897），失败回落直连，每个通道重试一次」。
- 境内站（IT之家 / 阮一峰 / 美国主机侦探 / 小众软件 / iTunes lookup）实测**直连即 200**；v2ex、HuggingFace、Steam、GitHub、HN、lobsters、LowEndBox、Epic、`t.me` 直连返回 `000`，必须走代理。
- `appstore` 是唯一**跨两条通道**的源：发现层 `t.me/s/TossTF` 走代理，核实层 `itunes.apple.com/lookup` 直连即 200。所以代理节点挂掉时它会整源失效（拿不到播报），而不是「抓到但全标未核价」——看到这行的 ERR 要把代理一起查。
- 代理节点坏掉时表现为「浏览器桥与所有境外源一起挂，但境内源全绿」——按 `skill-system-gc` 的判据先做 direct vs `-x` 对照，别急着怀疑站点改版。

## 二、机器可读（已接进 `radar_fetch.py` 的 `SOURCES`）

| key | 端点 | 赛道 | 格式 | 实测条数（10-15 / 10-16） | 通道 |
| --- | --- | --- | --- | --- | --- |
| `epic` | `store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN` | 限免 | JSON | 2 条（1 条本周限免 + 1 条打折） | 代理 |
| `steam` | `store.steampowered.com/api/featuredcategories?cc=cn&l=schinese` | 优惠 | JSON | specials 10 条，过滤 `discount_percent>0` | 代理，响应偏慢（超时给到 40s） |
| `lowendbox` | `lowendbox.com/feed/` | 优惠 | RSS | 15 条 | 代理 |
| `idcspy` | `www.idcspy.com/feed`（`idcspy.com/feed` 会 301 到 www） | 优惠·域名 | RSS | 10 条 | 直连即可 |
| `hn` | `hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30` | 资讯 | JSON | 30 条 | 代理 |
| `lobsters` | `lobste.rs/hottest.json` | 资讯 | JSON | 20 条 | 代理 |
| `v2ex` | `www.v2ex.com/api/topics/hot.json` | 资讯 | JSON | 8 条 | 代理 |
| `hf` | `huggingface.co/api/daily_papers?limit=15` | AI 动态 | JSON | 15 条 | 代理 |
| `trending` | `github.com/trending?since=daily` | 开发工具 | HTML 抓取 | 12 条（含描述截断 + star 数） | 代理 |
| `ruanyifeng` | `www.ruanyifeng.com/blog/atom.xml` | 周刊·资源 | Atom | 3 条 | 直连即可 |
| `ithome` | `www.ithome.com/rss/` | 资讯·限免线索 | RSS | 25 条 | 直连即可 |
| `producthunt` | `www.producthunt.com/feed` | 产品发布 | RSS | 15 条 | 代理 |
| `binance` | `www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId={48,49,51}` | 币圈·交易所公告 | JSON | 22 条 | 代理 |
| `exstatus` | `status.coinbase.com`、`status.kraken.com` 的 `/api/v2/status.json` | 币圈·服务状态 | JSON | 1 条聚合 | 代理 |
| `cgmarkets` | `api.coingecko.com/api/v3/coins/markets?...per_page=100` | 币圈·行情 | JSON | 7 条 | 代理 |
| `coingecko` | `api.coingecko.com/api/v3/search/trending` | 币圈·热搜 | JSON | 10 条 | 代理 |
| `cmc` | `api.coinmarketcap.com/data-api/v3/topsearch/rank` | 币圈·热搜 | JSON | 6 条 | 代理 |
| `fng` | `api.alternative.me/fng/?limit=1` | 币圈·情绪 | JSON | 1 条 | 直连即可 |
| `ethblog` | `blog.ethereum.org/feed.xml` | 币圈·项目方 | RSS | 6 条 | 代理 |
| `creleases` | `api.github.com/repos/{go-ethereum,agave}/releases` | 币圈·发版 | JSON | 4 条 | 代理 |
| `coindesk` | `www.coindesk.com/arc/outboundfeeds/rss/` | 币圈·媒体 | RSS | 12 条 | 代理，**需跟 308** |
| `theblock` | `www.theblock.co/rss.xml` | 币圈·媒体 | RSS | 12 条 | 代理 |
| `panews` | `www.panewslab.com/rss.xml` | 币圈·中文媒体 | RSS | 15 条 | 代理 |
| `appstore` | `t.me/s/TossTF` 公开预览（免登录）→ 每条回 `itunes.apple.com/lookup?id=<trackId>&country=cn` 核价 | 限免·iOS | HTML 抓取 + JSON 核价 | `--days 2` 出 15 条，本体限免／内购限免／兑换码三类都有 | 预览页**必须代理**（直连 `000`），iTunes 直连即 200 |
| `appinn` | `www.appinn.com/feed/`（标题含限免/免费/促销才留） | 限免·线索 | RSS + 关键词过滤 | 1 条（多数轮 0 条，属正常，脚本给它开了 `allow_empty`） | 直连即 200 |

币圈这 11 个源的字段取法、异动过滤门槛、分级与边界口径单独立档，见 `references/crypto.md`；本表只登记连通状态与条数。

全量一轮（25 源）2026-10-16 实测约 **48 秒**、抓到 **318 条**（`--days 2` 过滤后 241 条新），0 个 ERR。比 10-15 那轮的 31 秒多出约 17 秒，全部花在 `appstore` 的逐条 iTunes 核价上（一轮最多 15 次 lookup）。单跑币圈：`--source crypto`（组名）19:02 实测 `fetched=134 fresh=88 sources=11 errors=0`，约 20 秒。单跑优惠限免：`--source deal`（组名，6 源含 appstore/appinn）2026-10-16 实测 `fetched=56 fresh=40 sources=6 errors=0`，约 25 秒。

### 字段取法（踩过坑的地方，改脚本前先看）

- **Epic**：真值在 `data.Catalog.searchStore.elements[].price.totalPrice`，`discountPrice==0 且 originalPrice>0` 才是本周限免；截止时间在 `price.lineOffers[].appliedRules[].endDate`。**所有条目共用同一落地页 URL**，所以 `id` 必须按标题生成（`ident=title`），否则条目会互相覆盖。
- **Steam**：`original_price` / `final_price` 单位是**分**，要除 100；截止字段是 `discount_expiration`（epoch 秒）。商店页 HTML 直取是 403，只有这个 API 能用。
- **GitHub trending**：仓库链接的 `<a>` 里 `href` 不是第一个属性（前面挂着 `data-hydro-click`），正则得用 `<a[^>]*?href="/([^"]+)"`；star 数要取 `href="/<repo>/stargazers"` 那个锚到 `</a>` 的**整段**再剥标签，直接 `>.*?([\d,]+)` 会抓到 svg 里的 `height="16"`，全变成 16 star。
- **RSS**：`pubDate` 是 RFC 822（`Thu, 15 Oct 2026 07:28:11 +0000`），`--days` 靠 `email.utils.parsedate_to_datetime` 才能过滤掉旧闻；只认 ISO 会让旧活动天天重报。
- **308 重定向**：`coindesk` 的 RSS 回 `308 Permanent Redirect`，而 urllib 的 `redirect_request` 白名单只认 301/302/303/307，会把 308 当错误抛——表现为「curl -L 明明 200，脚本却 URLError」。已在 `_Follow308` 里按 307 语义转发。以后新增源报 ERR 而 `curl -sI -L` 是 200 时，先看中间状态码是不是 308。

### App Store 限免这一层怎么取、怎么核（2026-10-16 实测）

Apple 没有官方限免接口（`apps.apple.com/cn/rss/topfreeapplications` 实测 404，旧的那套 RSS 已经废了），所以 `appstore` 是**两层**：发现靠免登录的汇总通道，核实回 iTunes lookup 读现价。

- **发现**：`t.me/s/TossTF` 的公开预览页免登录可读（**必须走代理**，直连 `000`）。消息按 `data-post="TossTF/<id>"` 切段，播报时间在 `<time datetime="2026-10-14T05:57:22+00:00">`，正文在 `<div class="tgme_widget_message_text js-message_text">`。排版固定：标签行（`#AppName #中文名 #限免推荐 #本体限免`）→ `App名  // 中文说明` → 简介 → `🔒 解锁方法 ∶…` → `📱 系统要求 ∶…`。app 名优先取带 `//` 那行的前半段，取不到就退回首个 `#CamelCase` 标签。
- **认 id 不认名字**（这条是整个层的地基）：核价用的 `trackId` 从**播报正文里的** `apps.apple.com/<cc>/app/id<trackId>` 链接抓，不是拿名字去 search。国区会给 app 改名——`Idle Isle` 上架名「发呆岛 - 白噪音与专注计时器」、`Readify AI` →「悦读AI - Readify大模型自然语音听书阅读器」、`KoiFiles` →「双鱼文件浏览器」，按名字匹配既漏掉这些，又会认错人：实测频道报的 DuoScope 是 `6766231134`，名字 search 命中的却是 `1629252207` 那个另一个 app，把它的免费价安到了限免条目上。`itunes_search()` 只留作人工抽查，不进链路。
- **`price` 能证明什么**：`itunes.apple.com/lookup?id=…&country=cn`（免 key、免登录、直连即 200）的 `price` 是当前可下载价，且**会跟着促销走**——`6753570922` 返 0/免费；对照 `1067198688` 彩云天气Pro 返 ¥98.00。但 `price==0` 只等于「今天下载不花钱」，接口分不出本就免费与促销中，所以措辞写「下载不花钱」，**不写成「限免仍在」**。反过来 `6814196653` KoiFiles 播报「本体限免」而实测 ¥8.00 ⇒ 判「限免已失效或已改价」，这条就是不做核价会误报的形态。
- **内购限免单独降档**：内购解锁改的是 IAP 价格，下载价上完全看不出来，所以 `kind == "内购限免"` 一律附「这一项只算转述」，不许升到 ⭐值得。
- **没有截止时间**：商品页的 `application/ld+json` 只有一个 `offers.price`，页面上实测无「限时优惠」字样，Apple 不公布促销结束时间 ⇒ `until` 一律 `None`，条目里明写「Apple 不公布限免截止时间」，**不许编一个日期**。
- **兑换码型**：正文里是 `apps.apple.com/.../redeem?id=…&code=…` 的，只标「兑换码型限免，兑换码不转载，回原帖自取」——`code=` 不进产物（SKILL §一 第 3 条）。
- **核价额度最新优先**：先把全部消息解析进 `pending`，再 `reversed(pending)` 从最新一条开始花 `APPSTORE_VERIFY_MAX = 15` 次 lookup。倒序前出过岔子——额度被过期旧帖吃掉，当天真正的限免全标「未核价」。超出额度的明写「未走 iTunes 核价（超出本轮核价上限）」。
- **区回落**：国区查不到该 id、而播报链接里带区（`apps.apple.com/us/app/id…`）时按那个区再查一次，标签写成「iTunes us区实测现价 …」；都查不到就写「iTunes 按 id … 查不到上架记录，价格未核实」，不猜。
- **去重键 `ident=<trackId>-<播报日期>`**：与 Epic 的 `ident=title` 不同。限免通常持续好几天，键里带日期才能让「今天仍在」第二天重新报一次并重新核价；只带 trackId 会把后续几天全 `--seen` 掉。匹配不到 id 的退回 `appstore-<id或帖号>-<日期>`。
- **`allow_empty`**：解析函数可以挂 `src_x.allow_empty = True`，`main()` 见到空结果就打印 `INFO source=x empty=本轮无符合条件的新条目（非故障）` 而不算 ERR。`appinn` 靠它——小众软件两天没限免帖是常态，按原口径会被误判成站点改版。**但只给「业务上允许空」的源挂，别拿它当抑制报错的开关。**
- **小众软件的两个坑**：主 feed `www.appinn.com/feed/` 直连 200 且带 `pubDate`，走它；`/tag/限免/` 归档页**不按时间倒序**（实测首条 2026-06、次条 2026-04），列表页干脆没有日期，tag feed 的 URL 返回的是 HTML 壳而不是 RSS，所以不能当新帖源。

## 三、需要浏览器桥（curl/WebFetch 拿不到，不进脚本）

| 源 | 用途 | 实测 | 走法 |
| --- | --- | --- | --- |
| `store.epicgames.com/zh-CN/free-games` | 核对限免封面图与领取入口原文 | WebFetch/HTML 403 | chrome-devtools MCP 或 user-browser-use 打开页面读文本 |
| `lowendtalk.com/discussions` | VPS 商家口碑、真实续费吐槽 | 403 | 浏览器桥 |
| `reddit.com/r/*/json` | 社区口碑与翻车线索 | 403 | 浏览器桥，或直接放弃这条 |
| 知乎热榜 / 微博 | 国内限免与羊毛热点 | 403 | 浏览器桥（登录态在 user-browser-use 那个 profile） |
| 腾讯云 `act/pro/promotion`、阿里云 `minisite/goods`、OpenRouter 定价页 | 国内云与 API 免费额度核实 | 200/308 但内容是 JS 渲染，直取 HTML 拿不到价格 | **验真环节**用浏览器桥打开读数字，不做常规抓取 |
| X / Twitter（交易所与项目方官方号） | 币圈一手时间线、公告首发 | 机器读全无：`syndication.twitter.com` **429**、`nitter.net` **410**、`nitter.poast.org` **000**、threadreader 用户页 **404**、`api.fxtwitter.com/<user>` 只有用户元信息 | 只能在 `user-browser-use` 里用用户自己的登录态打开主页读原文；账号清单与核对纪律见 `references/crypto.md` 第四节 |
| OKX / Bybit / Bitget / Coinbase / Upbit 的公告页 | 核对该交易所的上币、下架、充提开关原文 | 200 但 JS 渲染，直取 HTML 拿不到条目列表 | 浏览器桥打开具体公告页读数字与生效时间；OKX 的 `api/v5/system/status` 实测 200 但无维护时 `data` 就是空数组，进 `SOURCES` 会被判 empty，所以不走脚本 |
| `defillama.com` 前端 | 协议 TVL、收益率横向对照 | 站点本身可读，但 `yields.llama.fi/pools` 是 **11.5 MB** 全量 JSON | 需要时浏览器桥按需查单个协议，不进定时任务 |

浏览器桥纪律：**不要用 `get_network_request`**（会倒出整站 cookie）；需要登录由用户本人在窗口里扫码，不代填、不保存凭据。币圈页面额外一条——只读文本，**绝不代点「连接钱包 / 签名 / 领取 / 交易 / 提现」**，那已经越过 SKILL §一 第 1 条的红线。

## 四、试过但不进清单

| 源 | 实测 | 结论 |
| --- | --- | --- |
| `keylol.com/rss.php?fid=335` | 404（论坛页 `forum6-1.html` 是 200） | 无可用 RSS；要限免线索就从 `ithome` + 浏览器桥进 keylol 论坛页 |
| `feedx.net/*` | 404 | 服务已不可用 |
| `vpsjixian.com/feed`、`zhujiceping.com/feed`、`onepointseveral.com/feed` | `000` | 连不上，不猜原因也不写进流程 |
| `rss.shab.fun/feed/` | `000` | 同上 |
| Vultr 定价页 | 403 | 需要浏览器桥；且价格类只作验真、不作发现 |
| `store.steampowered.com/api/featuredcategories` 直连 | `000`（走代理 200） | 只能配代理用 |
| CMC `cryptocurrency/listing?sortBy=percent_change_24h` | 200 但前 50 全是 rank 485~7400 的山寨币（榜首 +44914%），限 rank≤300 后一条不剩；`sortBy=rank` 参数不生效 | 涨幅榜改由 `cgmarkets` 出（详见 `references/crypto.md` 第三节） |
| Aave / Uniswap / Lido 治理论坛 `latest.json` | 200 但不按时间排序，且 Lido 结果里混着骗子回帖「recover your crypto from scammers / consult century」 | 不作常规源——币圈特有的污染源；要看治理动态走浏览器桥逐个打开 |
| Binance `?language=zh_CN` 公告参数 | 返回 **0 字节** | 只能用英文默认口径，中文转述靠 `panews` |
| Binance `bapi/apax/v1/public/product-list/simple-status` | 403 | 不用 |
| `status.bybit.com` / `status.bitget.com` / `status.okx.com` / `status.kucoin.com` / `status.mexc.com` / `status.upbit.com` / `status.gate.io` | 全部 `000`（域名不存在） | 交易所状态页只有 Coinbase、Kraken 两家是 Statuspage，已进 `exstatus` |
| KuCoin `www.kucoin.com/_api/cms/articles?category=announcement` | 200 但 `totalNum: 0, items: []`（换 `type=announcement` 直接 400） | 参数形态未知，没搞清之前不写进流程 |
| Bitget `api/support/announcement/getList` | 404（返回 HTML 壳） | 不用 |
| `apps.apple.com/cn/rss/topfreeapplications/…` | 404 | Apple 早年那套 RSS 已废，商店没有官方限免接口；iOS 限免只能「汇总通道发现 + iTunes lookup 核价」两层拼 |
| `itunes.apple.com/lookup?id=1453415739&country=cn` | 200 但 `resultCount: 0` | lookup 本身可用（免 key、直连 200），但 id 不对就是空——所以核价必须用播报正文里带出来的真实 `trackId`，不能凭名字猜 |
| `sspai.com/tag/…`、`sspai.com/api/v1/search/post/get_list` | 页面是 SPA 壳拿不到列表；搜索 API 404 | 少数派不作 iOS 限免源；`appinn` 那条关键词过滤已经够用 |
| `ithome.com/tag/限免/` | 404 | IT之家没有可用的限免 tag 页；线索仍从 `ithome` RSS 的标题里过 |
| `52pojie.cn/forum.php?mod=rss` | 返回安全验证页而非 RSS | 无机器可读通道，且 52pj 那边另有签到任务的红线，不作雷达源 |
| `reddit.com/r/AppHookup/new.json`、`old.reddit.com` | 403 | 与第三节同源结论：iOS 限免的英文社区只在浏览器桥里按需看，不进定时 |
| `freeappontheiphone.com` | DNS 解析失败 | 站点已不在，不猜原因 |
| `freeup.net` | 200 但内容是自由职业导航站，无 iOS 限免列表 | 名不符实，不用 |
| `macupdate.com/freebies` | 404 | 不用；macOS 限免线索走 `appinn` + `ithome` |
| `lemonprice.cn` | 不可达 | 境内限免聚合站候选，连不上就不写进流程 |
| GitHub 仓库搜「限免 / free app iOS」 | 搜到的一律是 README 营销库与失效脚本 | 噪声大于信号，不作发现层 |

## 五、新增来源的流程

1. **先实测**：`curl -sI -m 15 -x http://127.0.0.1:7897 <url>`，再 `curl -s -m 20 <url> | head -c 1200` 确认是真 RSS/JSON 而不是 HTML 壳。
2. 状态码与条数写进本表（标明实测日期），403 或 JS 渲染的只进第三节。
3. 能机器读的才在 `radar_fetch.py` 加 `src_xxx()`：返回 `norm(...)` 列表，`cat` 必须选 `deal` / `freebie` / `tech-news` / `ai-updates` / `dev-tools` / `crypto-exchange` / `crypto-market` / `crypto-project` / `crypto-news` 之一，价格给「到手价」、截止时间给 ISO，去重键不稳的（同一落地页多发）用 `ident=`。行情快照类的 `ident` 必须带当天日期，否则次日整批被 `--seen` 吃掉（见 `references/crypto.md` 第三节）；**持续多天的促销类反过来**——`ident` 要带播报日期，好让「今天仍在」次日重报一次（`appstore` 用 `<trackId>-<日期>`）。
4. 注册进 `SOURCES`，跑 `python3 scripts/radar_fetch.py --source xxx --limit 3` 看样例，再跑一轮 `--all` 确认没把总时长拖爆。**一条源要发 N 次额外请求的（如逐条回 iTunes 核价），加完必须在第二节的时间段里重报 `--all` 与所属组名的实测秒数**——本轮 23→25 源就是 31 秒变 48 秒，差额全是核价。
5. 某源持续 `ERR source=x empty`（HTTP 200 但解析 0 条）＝站点改版，手工打开对照后改正则；**不要因为解析失败就删源**，也不要用别的站的数据冒充它。**只有「业务上本来就经常没货」的源才挂 `src_x.allow_empty = True`**（如 `appinn` 两天没限免帖），它会打印 `INFO source=x empty=` 而不进 errors——别拿这个开关当抑制报错的省事办法，挂了就等于放弃了改版报警。
6. **发现层不等于事实**：Telegram 频道、小众软件这类汇总通道只负责「今天有什么在限免」，价格与在否一律回官方接口（iTunes lookup）核；核不到的写明「未核实」并留在 👀，不许把转述的原价/现价当成实测数字。

## 六、赛道 → 来源映射

| 赛道 | 常规取数 | 验真靠 |
| --- | --- | --- |
| 优惠价格（服务器/域名/订阅） | `lowendbox`、`idcspy`、`steam`、`ithome` | 厂商官网活动页（浏览器桥），要确认是否续费同价 |
| 限免（游戏/应用/课程/素材） | `epic`、`appstore`（TossTF 播报 + iTunes lookup 核价）、`appinn`、`ithome` | 官方领取页原文 + 截止时间；iOS 回 `itunes.apple.com/lookup?id=<trackId>&country=cn` 认 **id** 读现价，Apple 不公布截止时间就不写时间 |
| 薅羊毛 / 免费额度 | `ithome`、`idcspy`、`v2ex`、`producthunt` 做发现 | 官方定价与额度政策页，折算成人民币或 token 数 |
| IT·开发·AI·程序员 | `hn`、`lobsters`、`v2ex`、`hf`、`trending`、`ruanyifeng`、`producthunt` | 一手源（论文/仓库/发布公告原文） |
| 币圈（交易所/行情/项目方/媒体） | `--source crypto` 组名一次跑完：`binance`、`exstatus`、`cgmarkets`、`coingecko`、`cmc`、`fng`、`ethblog`、`creleases`、`panews`、`coindesk`、`theblock` | 交易所公告原文 + 合约地址核对；X 只有浏览器桥一条路。分级与验真口径见 `references/crypto.md` 第五、六节 |
