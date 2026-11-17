# 币圈赛道（2026-10-15 实测）

本表同样只记**本机本轮实际请求过**的结果。判读原则和 `sources.md` 一致：没在这里出现的源＝没验证过，不要直接用；要加就按第八节流程先实测。

币圈和另外四条赛道最大的差别是**噪声与污染**：行情数字一小时就变，热搜与涨幅榜会被山寨币刷穿，治理论坛里混着骗子回帖，X 没有可用的机器读通道。所以这一档的重点不是「多抓」，而是「抓来的必须能核、核不到就压进观察」。

## 一、四条轴

| 轴 | 关注什么 | 机器可读源 | 验真靠 |
| --- | --- | --- | --- |
| 交易所动态（`crypto-exchange`） | 上币/下架、充提开关、新交易对、API 与维护变更、服务状态 | `binance`（公告三个目录）、`exstatus`（Coinbase / Kraken 状态页） | 交易所公告原文 + 合约地址核对 |
| 行情与热度（`crypto-market`） | 主流币快照、市值前 300 里的 24h 异动、热搜与趋势、市场情绪 | `cgmarkets`、`coingecko`、`cmc`、`fng` | 只认带快照时间的数字，不追第二天的价格 |
| 项目方一手（`crypto-project`） | 协议博客、核心客户端发版、EIP/升级提案 | `ethblog`、`creleases` | 项目官方仓库/博客原文 |
| 媒体转述（`crypto-news`） | 监管、机构、安全事件、中文语境 | `panews`（中文）、`coindesk`、`theblock` | 事件必须回到项目方或交易所的一手公告 |

中文转述只作**发现与措辞参考**，数字与政策以一手英文原文为准；反过来，`coindesk`/`theblock` 提到的监管细节，如果拿不到监管原文，一律标「未核实」。

## 二、机器可读（已接进 `radar_fetch.py` 的 `SOURCES`）

| key | 端点 | 轴 | 格式 | 2026-10-15 实测 | 通道 |
| --- | --- | --- | --- | --- | --- |
| `binance` | `www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId={48,49,51}&pageNo=1&pageSize=6` | 交易所 | JSON | 22 条（三个 catalog 各 6~8） | 代理 |
| `exstatus` | `status.coinbase.com/api/v2/status.json`、`status.kraken.com/api/v2/status.json` | 交易所 | JSON | 1 条聚合（当天 Coinbase operational / Kraken **minor·Partially Degraded**） | 代理 |
| `cgmarkets` | `api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&price_change_percentage=24h` | 行情 | JSON | 7 条（1 快照 + 6 异动） | 代理，约 5s |
| `coingecko` | `api.coingecko.com/api/v3/search/trending` | 行情 | JSON | 10 条 | 代理 |
| `cmc` | `api.coinmarketcap.com/data-api/v3/topsearch/rank` | 行情 | JSON | 6 条 | 代理 |
| `fng` | `api.alternative.me/fng/?limit=1` | 行情 | JSON | 1 条 | 直连即可 |
| `ethblog` | `blog.ethereum.org/feed.xml` | 项目方 | RSS | 6 条（多为周更，`--days 2` 常为 0） | 代理 |
| `creleases` | `api.github.com/repos/{ethereum/go-ethereum,anza-xyz/agave}/releases?per_page=2` | 项目方 | JSON | 4 条 | 代理 |
| `coindesk` | `www.coindesk.com/arc/outboundfeeds/rss/` | 媒体 | RSS | 12 条 | 代理，**需跟 308** |
| `theblock` | `www.theblock.co/rss.xml` | 媒体 | RSS | 12 条 | 代理 |
| `panews` | `www.panewslab.com/rss.xml` | 媒体 | RSS | 15 条 | 代理 |

`--source crypto` 一次跑完这 11 个 key（约 82 条），并入 `--all` 后总规模 **25 源 / 318 条 / 约 48 秒**（2026-10-16 实测；crypto 这一段本身仍是最初的 11 个 key，涨的是后来并入的 iOS 限免两源，多出的时间全在 `appstore` 逐条回 iTunes 核价上）。

## 三、字段取法（踩过坑的地方，改脚本前先看）

- **Binance**：公告正文接口不返回日期——`publishDate`、`releaseDate` 实测全是 `None`，日期只写在标题尾巴上，所以取 `re.search(r"20\d{2}-\d{2}-\d{2}", title)`。带 `language=zh_CN` 请求实测返回 **0 字节**，只能用英文默认口径，中文转述交给 `panews`。三个 catalog 挂一个不算整源失败（函数里已按 `if out: continue` 处理）。目录含义：48 上币与新交易对 / 49 新产品与活动 / 51 技术与 API 变更。
- **CoinGecko 两个接口形态不一致**：`coins/markets` 的 `current_price`、`price_change_percentage_24h` 是 float；`search/trending` 的 `item.data.market_cap` 是**已格式化的字符串** `'$1,626,655,750,585'`，直接 `float()` 会抛 ValueError 把整源打死——所以金额一律过 `_fmt_usd()`，它先剥非数字再转，转不动就原样返回。
- **行情快照的 id 必须带当天日期**（`ident="%s-%s" % (coin_id, TODAY)`）。榜单每天重排，用稳定 id 的话第二天整批被 `--seen` 吃掉，等于雷达瞎了。`fng`、`exstatus` 同理。
- **异动过滤**：只看市值前 300 且 24h 绝对涨跌幅 ≥ 8%（`MARKET_RANK_MAX` / `MARKET_MIN_MOVE`）。CMC 的 `cryptocurrency/listing?sortBy=percent_change_24h` 实测前 50 条是 rank 485~7400 的山寨币，榜首 +44914%，加 rank 限制后**一条不剩**；该接口的 `sortBy=rank` 参数也不生效（返回 rank 8000+ 的包装币）。所以涨幅榜改由 `cgmarkets` 出，CMC 只保留 `topsearch/rank`（其中 `rankSort` 字段是 `None`，序号用 `enumerate` 自己编）。
- **308**：`coindesk` 的 RSS 回 `308 Permanent Redirect`，而 urllib 的 `redirect_request` 白名单只有 301/302/303/307，直接把 308 当错误抛。已在 `_Follow308` 里按 307 语义转发（GET 下两者行为一致）。curl 因为带 `-L` 看着正常，这条只对 Python 侧成立。
- **恐惧贪婪指数**只作语境底数，`extra` 里已明写「不构成任何操作建议」，别把它当信号。

## 四、X：实测没有稳定的机器可读通道

这一节是为了避免以后又花时间重踩。2026-10-15 逐个试过的结果：

| 通道 | 实测 | 结论 |
| --- | --- | --- |
| `syndication.twitter.com/srv/timeline-profile/screen-name/<x>` | **429** | 限流，不可依赖 |
| `nitter.net/<x>` | **410** | 实例已下线 |
| `nitter.poast.org/<x>` | **000** | 连不上 |
| `threadreaderapp.com/user/<x>` | **404** | 要按用户预先订阅才有页 |
| `api.fxtwitter.com/<x>` | 200 但只有用户元信息 | 拿不到时间线 |

所以 **X 只能走浏览器桥**（`user-browser-use`，登录态由用户本人在窗口里维护），且不作为常规抓取项，只作**验真与补充**：交易所/项目方发公告后，官方账号往往是第一时间，需要确认「到底说没说」时打开对应主页读原文。

关注清单（**候选，首次使用前要在登录窗口逐个核对 handle 与认证标志**——仿冒号是这个圈子的常态，我不凭记忆认定任何 handle 是真的）：

- 交易所官方号：Binance / OKX / Bybit / Coinbase 各自的公告口径
- 公链与项目方：Ethereum、go-ethereum、Solana/Anza、以及当天条目涉及的那个项目
- 安全告警类：只做「有没有出事」的交叉确认，出事必须回到项目方 advisory 或交易所公告，不据推文下结论

纪律：只取正文与发布时间，**不取评论区、不截图带 cookie 的页面**；不要用 `get_network_request`；需要登录由用户本人扫码，不代填不保存。

## 五、验真口径（币圈特有）

1. **上币 / 下架 / 充提开关**：以交易所公告原文为准，条目里要写清「哪条链、哪个合约、什么时刻开充提」。同一个币在不同链上的合约地址不同——去项目官方文档或区块浏览器核地址，核不上就降级 👀观察 并写「合约地址未核」。
2. **行情数字**：必须带快照时间（`ts` 就是取数当天，报告里写「HH:MM 快照，来源 CoinGecko/CMC」）。超过两小时的数字不要写进正文，宁可写「截至取数时刻」。
3. **安全事件 / 盗币 / 漏洞**：只认项目方 GitHub security advisory、官方 blog、交易所公告这三类一手源；媒体转述只作线索。涉及用户操作建议时只写「按官方公告升级/撤销授权」，不自己发挥。
4. **空投与钓鱼**：任何要求「连接钱包领取」「先付 gas」「加 TG / 私聊客服」「帮你追回被盗资产」的内容，一律 ❌过滤，并在观察段点明它是钓鱼形态。实测证据：Lido 治理论坛的 `latest.json` 里混着「How you can recover your crypto from scammers // consult century」这种骗子回帖——**这是币圈特有的污染源，不是特例**。
5. **旧闻重推**：`--days 2` 只挡时间戳；换标题重推的监管旧闻靠人和 URL 再判一次。

## 六、分级口径（币圈）

| 标记 | 币圈的门槛 | 例子 |
| --- | --- | --- |
| 🔥 紧急 | **仅限直接影响在用资产可得性**：交易所下架/清退你持有的币种、充提暂停、服务状态非 none（`exstatus` 报 degraded）、核心客户端安全版本、稳定币脱锚 | Kraken 状态 minor 且你在用 Kraken → 提；否则只是背景 |
| ⭐ 值得 | 已核到一手 + 能落到具体动作（读 EIP、升级节点、核对某个上币时间） | go-ethereum 发安全补丁版 |
| 👀 观察 | **所有行情、涨跌幅、热搜、情绪指数默认落在这里**——它们是状态描述，不是可执行信息 | BTC 24h -2.9%、Bitway -20% |
| ❌ 过滤 | 喊单、目标价、荐币、KOL 预测、「内幕消息」、要连钱包才能领的东西、治理论坛里的追回服务回帖 | 直接不写 |

行情类默认不给 ⭐，这条比另外四条赛道更严：**涨跌本身不构成价值**，写进正文只会把日报变成荐股。

## 七、边界（在 SKILL §一 之上追加，不覆盖它）

- 不给投资建议，不预测价格，不写「该买/该卖/该拿」；只描述发生了什么、官方说了什么、什么时候生效。
- **不碰任何链上操作**：不连钱包、不签名、不导入私钥/助记词、不代为 approve、不注册交易所账号、不代充提、不使用任何 API key。
- 不写搬砖、绕过风控、多号刷空投、女巫之类玩法，也不提供教程。
- 产物里不出现钱包地址、私钥、交易所 API key、邀请码/返利链接。交易所落地页常带 `?ref=`、`?from=...` 之类的推广参数，写进报告前一律剥成干净 URL。
- 涉及金额折算只写美元原值与快照时间，不替用户换算成「值多少人民币」以外的推断性表述。

## 八、新增币圈来源的流程

沿用 `sources.md` 第五节，另加两条本赛道特有的门槛：

1. 先实测：`curl -sI -m 15 -x http://127.0.0.1:7897 <url>`，再取前 1200 字节确认是真 JSON/RSS 而不是 JS 壳。
2. **必须能带时间或能判新旧**。行情类接口没有发布时间戳，就用 `TODAY` + id 带日期；两者都做不到就别进取数层，只写进第四节的浏览器桥档。
3. 注册进 `SOURCES` 后同时加进 `GROUPS["crypto"]`，否则 `--source crypto` 跑不到它。
4. 跑 `--source <新key> --limit 5` 看样例，再 `--all --days 2` 确认 0 ERR 且总时长还在 1 分钟内。

## 九、试过但不进清单

| 源 | 实测（2026-10-15） | 结论 |
| --- | --- | --- |
| `api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?sortBy=percent_change_24h` | 200 但前 50 全是 rank 485~7400 的山寨币 | 噪声不可用，异动改走 `cgmarkets` |
| 同上 `sortBy=rank` | 200 但返回 rank 8000+ 的包装币，参数不生效 | 不用 |
| Aave / Uniswap / Lido 治理论坛 `latest.json` | 200，但**不按时间排序**，且 Lido 结果里混骗子回帖 | 不作常规源；要看治理动态走浏览器桥逐个打开 |
| `yields.llama.fi/pools`（DeFiLlama） | 200，响应 **11.5 MB** | 太重，不进定时任务 |
| `www.okx.com/api/v5/system/status` | 200，`data: []`（无维护时就是空） | 空是合法值，进 `SOURCES` 会被判 `ERR empty`，只作浏览器桥验真 |
| `www.binance.com/bapi/apax/v1/public/product-list/simple-status` | **403** | 不用 |
| Bitget `api/support/announcement/getList` | 404（返回 HTML 壳） | 不用 |
| KuCoin `www.kucoin.com/_api/cms/articles?category=announcement` | 200 但 `totalNum: 0, items: []`，参数形态未知 | 待解，未搞清参数前不写进流程 |
| `status.bybit.com` / `status.bitget.com` / `status.okx.com` / `status.kucoin.com` / `status.mexc.com` / `status.upbit.com` / `status.gate.io` | 全部 **000**（域名不存在） | 只有 Coinbase、Kraken 两家是 Statuspage |
| OKX / Bybit / Upbit / Coinbase 公告页正文 | 200 但 JS 渲染，直取 HTML 拿不到条目 | 需浏览器桥，作为**验真**通道而非发现通道 |
| `cryptopanic` 之类聚合 API | 未测（要 key） | 没实测就不写进流程 |
