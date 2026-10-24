---
title: "资讯雷达 2026-10-25｜Steam 赛博朋克 2077 明晨收口、Epic 周免效期复查、App Store 一条核到免费下载与 Brotli 漏洞扩散"
author: OxYGC
date: 2026-10-25 06:38:00 +0800
permalink: /posts/info-radar-2026-10-25/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Steam优惠, Epic, AppStore, 安全漏洞, AI-Agent, 币圈]
description: "2026-10-25 一轮 25 个来源的资讯雷达：Steam 赛博朋克 2077 一档明天凌晨收口、Epic 两款周免效期复查、App Store 国区一条核到免费下载价、Brotli 漏洞扩散到多语言 HTTP 库，全部标注核实时间与截止时间。"
---

这一轮跑了 25 个来源，取回 316 条，两天窗口加跨天去重之后留下 143 条，0 个来源报错。先把话说完：<strong>本轮没有紧急项</strong>。最近的硬截止是 Steam 那批 10 月 27 日 02:00（北京时间）收口的折扣，距今约 44 小时，没命中「距截止 ≤3 小时」；没有任何一条命中「影响在用的域名、VPS 或在用 API 的免费额度」，也没有一条命中「直接影响在用资产可得性」的交易所公告。和昨天相比有两处变化。其一是 Steam 的特惠位换了一批：昨天报的《再再启程》折扣已经下掉，今天接口里绝对降价额最大的是《赛博朋克 2077》本体与《往日之影》，同一批、同一个凌晨截止。其二是这一轮被跨天去重挡掉的三个源（<code>steam</code>、<code>epic-store</code>、<code>appinn</code>）其实都有在线内容，所以本篇对 Epic 那两款周免给的是<strong>效期复查</strong>而不是新消息——06:38 重读官方端点，<code>discountPrice</code> 仍是 0，截止时间一字未动。App Store 侧今天只有一条播报核到免费下载价。开发侧最值得后端读者看一眼的是 Brotli 那条漏洞的影响面扩张，币圈侧唯一一手材料充分的是 Solana 核心客户端 Agave 发了一个 RC。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:14px 16px;background:#fbfcfd;">

| 时点 | 条目 | 价格 | 去哪 |
| --- | --- | --- | --- |
| <span style="color:#c0392b;font-weight:700;">10-27 02:00 截止，剩约 44 小时</span> | Steam《赛博朋克 2077》本体 +《往日之影》 | <span style="color:#1a7f37;">¥89.40</span>（原 ¥298 / ¥149） | [Steam 商店页](https://store.steampowered.com/app/1091500/?l=schinese) |
| <span style="color:#c0392b;font-weight:700;">10-29 23:00 截止，剩约 4 天</span> | Epic 本批周免两款（《Sker Ritual》《Home》）效期复查 | <span style="color:#1a7f37;">0 元</span>（原 ¥78 / ¥15） | [Epic 免费游戏页](https://store.epicgames.com/free-games?lang=zh-CN) |
| 11-06 02:00 截止 | Steam《行尸走肉：Telltale 完整版》 -90% | <span style="color:#1a7f37;">¥16.80</span>（原 ¥168.00） | [Steam 商店页](https://store.steampowered.com/app/1449690/?l=schinese) |
| <span style="color:#6b7280;font-weight:700;">Apple 不公布限免截止时间</span> | App Store 国区《day.txt》本体限免 | <span style="color:#1a7f37;">下载 0 元</span> | [apps.apple.com/cn/app/id6805007155](https://apps.apple.com/cn/app/id6805007155) |

</div>

## 值得看（10）

<details>
<summary><strong>Steam《赛博朋克 2077》（app 1091500） -70%</strong> ｜ <span style="color:#1a7f37;">¥89.40</span>（原 ¥298.00） ｜ <span style="color:#c0392b;">截止 10-27 02:00，剩约 44 小时</span></summary>
<p>本轮所有已核实条目里绝对降价额最大的一档，也是收口最早的一档。判据来自官方 <code>featuredcategories?cc=cn&amp;l=schinese</code>：<code>discount_expiration</code> 是 UTC 秒，<code>2026-10-26T18:00:00Z</code> 换算北京时间 10 月 27 日 02:00。同一批里《赛博朋克 2077：往日之影》（app 2138330）是 ¥149.00 → ¥89.40（-40%），截止时间完全相同，要动就一次判完，不必分两次看。</p>
<p>区域参数必须显式带 <code>cc=cn</code>：不带它会按出口 IP 返回别的货币定价，数字对不上不是改价而是区域差异。</p>
<p>核实于 2026-10-25 06:38（Steam 官方接口） · 直链 <a href="https://store.steampowered.com/app/1091500/?l=schinese">store.steampowered.com/app/1091500</a></p>
</details>

<details>
<summary><strong>Steam《The Walking Dead: The Telltale Definitive Series》（app 1449690） -90%</strong> ｜ <span style="color:#1a7f37;">¥16.80</span>（原 ¥168.00） ｜ <span style="color:#c0392b;">截止 11-06 02:00</span></summary>
<p>本轮折扣率最高的一条，全季合集一次到位。它不进「紧急」是因为窗口还有十二天，且折扣率本身不构成价值——玩不玩剧情向章节制作品，只有你自己判得出来。</p>
<p>同一轮官方接口里还有 GTA V 增强版 ¥149.00→¥74.50（-50%）、Resident Evil 4 ¥198.00→¥49.50（-75%）、Resident Evil Requiem ¥348.00→¥243.60（-30%）、雾锁王国 -10%、《朋友，梭哈吧》-38%，均已核实但折扣率或适配度不足以单列，收在观察段的合并行里。</p>
<p>核实于 2026-10-25 06:38 · 直链 <a href="https://store.steampowered.com/app/1449690/?l=schinese">store.steampowered.com/app/1449690</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Sker Ritual（斯盖尔仪式）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥78.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00，剩约 4 天</span></summary>
<p>10-23、10-24 两篇都报道过它，本轮取数没再把它列进新增，是因为 Epic 这一路的去重键是标题（<code>ident = title</code>）——同一款限免持续多天，只在第一次出现时报。这一条的价值不是「新消息」，而是<strong>复查</strong>：06:38 重读官方 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 端点，<code>discountPrice</code> 仍为 0，<code>appliedRules.endDate = 2026-10-29T15:00:00Z</code>，换算北京时间 23:00，与前两天一致。</p>
<p>僵尸题材 roguelike 卡牌，<strong>领取即永久入库</strong>，不需要赶在截止前玩完。另外注意 Epic 中文商店页有时把同一时刻渲染成次日 00:00，两处都是官方来源，按早的动手。</p>
<p>核实于 2026-10-25 06:38（Epic 官方端点） · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure（归家）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥15.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00</span></summary>
<p>与上一条同一批、同一截止时间，一并领即可，不需要分开判断窗口。本轮复查官方端点仍为 <code>discountPrice = 0</code>、<code>originalPrice = 1500</code>（接口单位是分）。</p>
<p>同一页里 Eternal Threads ¥62.00→¥12.40、纪念碑谷 ¥33.00→¥11.55、《Sorry We're Closed》¥78.00→¥54.60 是打折而非限免，截止 11-03 00:00（北京时间），已核实但没进「值得」。</p>
<p>核实于 2026-10-25 06:38 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 国区《day.txt》（id 6805007155）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>纯文本日记工具，汇总频道 08:11 UTC 的播报口径是「本体限免」，回 iTunes lookup 用播报正文里那个 trackId 核到国区 <code>formattedPrice = 免费</code>、<code>price = 0.0</code>，商店名与播报名一致（day.txt），开发者署名 Zbigniew Ledwon，最低系统 17.0。</p>
<p>三处口径要说清：其一，核到现价 0 只等于「今天下载不花钱」，lookup 接口分不出「本就免费」与「促销中」，所以不写「限免仍在」；其二，Apple 不公布促销结束时间，那一栏只能这么空着，编一个日期出来反而更糟；其三，国区会给应用改名，所以一律认 id 不认名字——按名字搜会认错另一个 app，把别人的免费价安到这条上。</p>
<p>核实于 2026-10-25 06:36（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id6805007155">apps.apple.com/cn/app/id6805007155</a></p>
</details>

<details>
<summary><strong>《Node2Shell 演化到 HTTP2Shell：Brotli 链路影响面扩到多语言 HTTP 库》</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止，但依赖值得现在就查</summary>
<p>技术安全博客 Aikido 的一手分析（CVE-2026-111497）：原先按 Node 侧问题传播的那条利用链，作者把结论扩到了 HTTP/2 路径与所有消费 brotli 解压的运行时。对后端读者的意义很具体——不是「又有个 RCE」，而是<strong>依赖树里那个 brotli 绑定层才是排查点</strong>，Python 之外同样可能吃到。</p>
<p>热度上是双通道互证而不是单点热帖：Hacker News 256 分 / 126 评，lobsters 同期 6 赞 / 6 评，两个独立社区指向同一篇文章。要不要立刻动手取决于线上服务是否真在解压 <code>Content-Encoding: br</code>，雷达只报道它存在与影响面，不替你判风险。</p>
<p>核实于 2026-10-25 06:31（取数轮，HN Algolia 官方接口 + lobsters 官方 RSS） · 直链 <a href="https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497">aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497</a></p>
</details>

<details>
<summary><strong>《Twelve years of distributed SQLite》</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>Philip Toole 复盘把 SQLite 做成分布式存储十二年一路的取舍：为什么选嵌入式、哪些假设最终崩掉、代价付在哪。嵌入式数据库与本地优先（local-first）方向的一手长文，适合直接当选题材料读。本轮 Hacker News 352 分 / 60 评，同时挂在 lobsters（13 赞 / 1 评），属双通道互证。</p>
<p>核实于 2026-10-25 06:31（HN Algolia 官方接口 + lobsters 官方 RSS） · 直链 <a href="https://philipotoole.com/twelve-years-of-distributed-sqlite/">philipotoole.com/twelve-years-of-distributed-sqlite</a></p>
</details>

<details>
<summary><strong>Nutlope/hallmark：给 Claude Code、Cursor、Codex 用的「反 AI 味」设计 skill</strong> ｜ <span style="color:#6b7280;">0 元（开源）</span> ｜ 无截止</summary>
<p>仓库自述是 <code>Anti-AI-slop design skill for Claude Code, Cursor, and Codex</code>，GitHub trending 榜面 32,062 star。它和今天刚落地的那篇《从安装部署到入门 Claude Code：三条安装路线、模型接入、权限模式与日常命令一次讲清》是同一根线——Claude Code 的 skill 挂载方式可以直接复用，读点在于它把「设计约束」写成 skill 的具体做法，而不是那句反 slop 的口号。</p>
<p>trending 榜没有发布时间戳，也不参与时间窗过滤，所以这一条是按「读了自述与用途」入选，不是按热度入选；star 数取的是榜单显示值。</p>
<p>核实于 2026-10-25 06:31（GitHub Trending 官方页面） · 直链 <a href="https://github.com/Nutlope/hallmark">github.com/Nutlope/hallmark</a></p>
</details>

<details>
<summary><strong>aws/agent-toolkit-for-aws：云厂方自己维护的 MCP servers 与 skills 套件</strong> ｜ <span style="color:#6b7280;">0 元（开源）</span> ｜ 无截止</summary>
<p>自述 <code>Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS</code>，榜面 3,101 star。它的价值不在星数，而在「官方口径」这一格：写 Agent 工具链对比时可以拿它和社区那批 MCP server 对照，看云厂方自己怎么划工具边界与授权模型。</p>
<p>核实于 2026-10-25 06:31（GitHub Trending 官方页面） · 直链 <a href="https://github.com/aws/agent-toolkit-for-aws">github.com/aws/agent-toolkit-for-aws</a></p>
</details>

<details>
<summary><strong>anza-xyz/agave 发版 v4.4.0-rc.0</strong> ｜ <span style="color:#6b7280;">0 元（项目方一手）</span> ｜ 无截止</summary>
<p>Solana 核心客户端的发版，来源是项目方自己的 GitHub releases，不是媒体转述。官方 API 给 <code>published_at = 2026-10-24T07:27:33Z</code>（北京时间 10 月 24 日 15:27），版本形态是 <code>rc</code> 而非正式版，这点必须写清楚，不能当成可用稳定版引用。</p>
<p>对写公链与客户端类内容的人来说，这条的意义是「引用的版本号要跟着改，而且要标明是 RC」；自己是否升级取决于是否真的在跑节点，雷达不给操作建议。</p>
<p>核实于 2026-10-25 06:31（GitHub 官方 releases API） · 直链 <a href="https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0">anza-xyz/agave releases/tag/v4.4.0-rc.0</a></p>
</details>

## 观察（11）、币圈那一轮与方法

<details>
<summary><strong>观察 11 条（每条末尾写存疑原因）</strong></summary>
<table>
<tr><th>条目</th><th>为什么只放观察</th></tr>
<tr><td>交易所服务状态：Coinbase <code>All Systems Operational</code>、Kraken <code>Partially Degraded Service</code>（indicator=minor）</td><td>06:31 回读两家官方 Statuspage。要不要紧取决于有没有把资产挂在这两家，雷达没有这项证据，按口径既不升紧急也不做任何链上或交易所侧动作。</td></tr>
<tr><td>PANews《Electrum 披露已遭在野利用的高危漏洞，已有用户资金受损》（10-24 20:22 GMT）</td><td>只见到媒体转述，electrum.org 首页本轮没有对应公告，未回到项目方 advisory 一手。安全事件只认项目方 advisory / 官方博客 / 交易所公告三方之一。涉及操作时按官方口径升级或撤销授权，雷达不自行发挥。</td></tr>
<tr><td>PANews《硬件钱包 Keystone 官网遭未授权访问，用户姓名及收货地址泄露》（10-24 19:23 GMT）</td><td>同上，未见项目方一手公告，无法核对泄露范围与生效时间。</td></tr>
<tr><td>PANews《安全机构：X100 遭持续攻击，攻击者已套取约 485 万枚 USDT》（10-24 15:04 GMT）</td><td>金额来自安全机构经媒体转述，未回一手报告，也没核对涉事合约地址（链上资产只按代币符号认会认错）。</td></tr>
<tr><td>智谱 ZCode「1024 程序员节送 5 亿 Tokens」，小众软件 10-23 转述，称 10-23 23:00 生效、<strong>10-26 09:00 到期</strong>，限 GLM-5.3 与 GLM-5.3-Flash（<a href="https://www.appinn.com/zcode-1024-free-500-million-tokens/">appinn.com 原文</a>）</td><td>06:37 用浏览器读官网 <code>zcode.z.ai/cn</code>，整页文本里没有出现 1024、程序员节、Tokens、5 亿、活动等任何字样，活动入口在桌面客户端内、要登录才看得见。免费额度类一律要官方口径才进「值得」。这条的唯一时间敏感点是播报里的 10-26 09:00 到期——真要用请自己开客户端左下角活动入口核对生效与到期时间，雷达不代领、不代注册。</td></tr>
<tr><td>iOS 内购限免 4 款：FreePlay（id 6754824912）、LiveToFrame（id 6757419019）、Artino（id 6774119167）、框语-相机水印大师（id 6755989422）</td><td>iTunes 核到的只是下载价为 0，而内购解锁价根本不体现在下载价上，这类只能算转述；Apple 不公布限免截止时间。四款里三款的商店名与播报名不一致（国区会改名），已按 id 对齐。</td></tr>
<tr><td>iOS 兑换码型限免《Burning Parchment: Bedtime》（<a href="https://t.me/TossTF/3756">t.me/TossTF/3756</a>）</td><td>兑换码不转载、不代兑换，只留频道原帖让你自己取；本轮未走 iTunes 核价，价格未核实。Apple 不公布限免截止时间。</td></tr>
<tr><td>iOS《Bothie》（<a href="https://t.me/TossTF/3757">t.me/TossTF/3757</a>）</td><td>播报正文里没有 App Store 直链，无从取 trackId 核价，价格未核实；也不排除已下架。Apple 不公布限免截止时间。</td></tr>
<tr><td>行情与热度快照（06:31，CoinGecko / CoinMarketCap / alternative.me）：市值前 5 BTC $80,417（-1.0%）、ETH $2,339.87（-2.2%）、USDT $0.999089、BNB $733.69（-0.9%）、XRP $1.29（-1.0%）；异动 Akedo $0.0306864（-21.9%，rank 88）；CoinGecko 热搜 HYPE / BSC / UHI / DACITY / PEARL / BTC / PUMP / BMT / AERO / ZEC；CMC 热搜 BTC / SOL / XRP / ORDER / NEAR / JCT；恐惧贪婪指数 51（Neutral）</td><td>它们是某一刻的数字，不是可执行信息。行情、涨跌幅、热搜、情绪指数按口径一律不给「值得」，也不构成任何操作建议。媒体侧「ETH 跌破 2300」「24 小时全网合约爆仓 8.46 亿美元」「某巨鲸 ETH 多单清算价 2256/2227」同属此类，不重复列。</td></tr>
<tr><td>其余带截止折扣（本轮官方接口已核，未逐条进「值得」）：Steam GTA V 增强版 ¥149.00→¥74.50、RE4 ¥198.00→¥49.50（至 11-04 02:00）、RE Requiem ¥348.00→¥243.60、雾锁王国 -10%（至 10-30 01:00）、《朋友，梭哈吧》-38%（至 10-29 01:00）；Epic Eternal Threads ¥62.00→¥12.40、纪念碑谷 ¥33.00→¥11.55、《Sorry We're Closed》¥78.00→¥54.60（均至 11-03 00:00）（北京时间，均为打折非限免）</td><td>折扣率或与你内容方向的适配度不足以单列一张卡片，数字本身已回官方接口核实，列在这里是为了「会过期或要复查」这件事可追溯。</td></tr>
<tr><td>《Balloting has completed for C++26. Unfortunately it was Disapproved》（lobsters 13 赞 / 8 评，来源是 Robert Seacord 本人的 LinkedIn 帖）</td><td>对 C++ 选题有分量，但 LinkedIn 页面本轮无法核对账号认证状态，属「一手作者但不可验真」，按口径不给「值得」。另外两条技术动态也未入选：astral.sh《Bringing uv and ty together》（22 赞，Python 工具链，与你当前 Java/Go 方向接口弱）、Roku 开发仓库从 GitHub 迁到 GitLab（224 分，事件性新闻，无可执行动作）。</td></tr>
<tr><td>中英文加密媒体转述 26 条（PANews 15 / CoinDesk 9 / The Block 2）、Product Hunt 13 条、IT之家 25 条、v2ex 10 条</td><td>媒体侧本轮没有一条回到一手原文（监管、机构、代币化股票争议居多）；PH 与 IT之家多为产品通稿与硬件新品，v2ex 热帖多为闲聊与职业困惑，与发文选题没有直接接口。</td></tr>
</table>
<p><strong>过滤（不进正文，只计数）</strong>：v2ex「抽送 GPTPLUS 日区独享月卡成品号」属共享账号交易、「用单位电脑开代理如何逃避后台监测」属绕过风控，两者一律过滤且不写做法；lowendbox 那条被归在 deal 组的《A Graph Showing Why It's Not a Fun Time to Work in IT》是财经评论而非优惠，按软文形态处理，不构成任何投资参考。</p>
</details>

<details>
<summary><strong>币圈这一轮怎么取的、来源健康度与四步口径</strong></summary>
<p><strong>取数结果</strong>：<code>SUMMARY fetched=316 fresh=143 sources=25 errors=0</code>，整轮没有任何 <code>ERR source=</code> 行，也没有 <code>INFO source=x empty=</code>。25 个 source key 全部返回成功，其中 18 个有新增，7 个本轮 0 条新增，逐一说清：<code>epic-store</code>、<code>steam</code>、<code>appinn</code> 是<strong>有在线内容但被跨天去重挡掉</strong>（06:38 分别单独复核，Epic 5 条、Steam 9 条、appinn 1 条），这一类本篇按「效期复查」重新核了一遍而不是当无事发生；<code>binance-ann</code> 是最新一批公告日期为 10-21，超出两天窗口；<code>ethblog</code>、<code>ruanyifeng</code>、<code>hf</code> 窗口内确实没有新帖（周刊周六晚更、第 416 期已在 10-24 报过；周末无 daily papers）。这几条空都不是故障。</p>
<p><strong>来源分布（fresh）</strong>：ithome 25、hackernews 19、panews 15、lobsters 13、producthunt 13、v2ex 10、coingecko-trending 10、coindesk 9、github-trending 7、appstore-ios 7、coinmarketcap-search 6、coingecko-markets 2、theblock 2、lowendbox 1、idcspy 1、exchange-status 1、fng-index 1、crypto-release 1。</p>
<p><strong>通道判据</strong>：境内（IT之家、美国主机侦探、v2ex、小众软件、iTunes lookup）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、Steam、GitHub API、Statuspage）同时全绿，代理节点这一轮工作正常。ZCode 官网属于「200 但页面是 JS 壳」，浏览器桥渲染后仍无活动信息，这是站点侧结构问题，不是通道故障，已在对应条目里写明。X 一侧本轮没有需要验真的条目，因此没有动用登录窗口。</p>
<p><strong>四步口径</strong>：一、取数只用有机器可读通道且能判新旧的来源，行情类靠「id 带当天日期」避免整批被去重吃掉；二、验真——优惠、限免、免费额度三类必须回官方页或官方接口二次确认价格与截止时间，App Store 因为 Apple 不公布促销结束时间，那一栏写「不公布」而不是编一个日期，且一律认 trackId 不认名字（国区会改名，按名字搜会认错 app、把别人的免费价安到这条上），内购限免与兑换码型只算转述；三、分级——🔥 只给距截止 ≤3 小时或影响在用服务与在用资产可得性的，⭐ 给已核实且本周内能直接用的，👀 给未核实或门槛高的，❌ 给旧闻重推、软文与要连钱包才能领的东西；四、边界——只收集、验证、报告，不注册、不绑卡、不代领券、不下单，兑换码型福利不转载兑换码，币圈不连钱包、不签名、不导私钥、不给买卖建议与目标价，产物里不出现钱包地址、私钥、助记词与带返利参数的邀请链接。</p>
</details>
