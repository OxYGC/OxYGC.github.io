---
title: "资讯雷达 2026-10-23｜Epic 周免两款到 10-29、Steam 两项深折、App Store 五条本体限免与 OpenShell"
author: OxYGC
date: 2026-10-23 06:35:00 +0800
permalink: /posts/info-radar-2026-10-23/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Epic, Steam优惠, AppStore, AI-Agent, 币圈]
description: "2026-10-23 一轮 25 个来源的资讯雷达：Epic 两款周免（《斯盖尔仪式》《归家》）10-29 23:00 收口、Steam 国区两项深折、App Store 国区五条本体限免、OpenShell 与 claude-howto 两个 Agent 向仓库，以及 Ethereum 官方那条 Hoodi 推迟公告，全部标注核实时间与截止时间。"
---

这一轮跑了 25 个来源，取回 318 条，两天窗口加跨天去重之后留下 187 条新的，0 个来源报错。结论先摆出来：<strong>本轮没有紧急项</strong>——最近的硬截止是 Epic 这批周免 10 月 29 日 23:00（北京时间）收口，还剩六天；也没有任何一条命中「影响在用的域名、VPS 或在用 API 的免费额度」。福利侧是主力：Epic 官方端点实测两款 <code>discountPrice = 0</code>（《Sker Ritual》原价 ¥78、《Home》原价 ¥15），Steam 国区有 -75% 与 -90% 两项深折，App Store 国区五条「本体限免」的下载价核到 0。开发侧留下两个和 Agent 直接相关的仓库（NVIDIA/OpenShell、claude-howto），币圈侧唯一一条一手材料充分的是 Ethereum 官方博客把 Hoodi 测试网上的 Glamsterdam 分叉推迟了——它不是价格消息，是「你写的时间线要跟着改」的消息。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:14px 16px;background:#fbfcfd;">

| 时点 | 条目 | 价格 | 去哪 |
| --- | --- | --- | --- |
| <span style="color:#c0392b;font-weight:700;">10-29 23:00 截止，剩约 6 天</span> | Epic 本批周免两款（《Sker Ritual》《Home》） | <span style="color:#1a7f37;">0 元</span>（原 ¥78 / ¥15） | [Epic 免费游戏页](https://store.epicgames.com/free-games?lang=zh-CN) |
| <span style="color:#c0392b;font-weight:700;">Apple 不公布限免截止时间</span> | App Store 国区五条本体限免（含两款 macOS 应用） | <span style="color:#1a7f37;">下载 0 元</span> | [Watch Tuner Lite](https://apps.apple.com/cn/app/id968820626) |
| 11-04 02:00 截止 | Steam 国区《Resident Evil 4》 -75% | <span style="color:#1a7f37;">¥49.50</span>（原 ¥198.00） | [Steam 商店页](https://store.steampowered.com/app/2050650/?l=schinese) |
| 10-22 官方发布，跟你的时间线有关 | Ethereum 博客《Glamsterdam on Hoodi Postponed》 | <span style="color:#6b7280;">0 元（官方博客）</span> | [blog.ethereum.org](https://blog.ethereum.org/en/2026-10-22/glamsterdam-hoodi-delay) |

</div>

## 值得看（12）

<details>
<summary><strong>Epic 本周限免《Sker Ritual（斯盖尔仪式）》</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥78.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00，剩约 6 天</span></summary>
<p>僵尸题材的 roguelike 卡牌，领取即永久入库，不需要赶在截止前玩完。判据仍然只有一条：<code>discountPrice == 0</code> 才算免费，打折档不算。官方端点这次同时给了 <code>appliedRules.endDate = 2026-10-29T15:00:00Z</code>，换算北京时间 23:00——注意 Epic 中文商店页有时把同一时刻渲染成次日 00:00，两处都是官方来源，按早的动手。</p>
<p>同一批还有一处中文资讯源当天的「喜加二」转述与之互证，定性以官方端点为准。</p>
<p>核实于 2026-10-23 06:35 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure（归家）》</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥15.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00</span></summary>
<p>与上一条同一批、同一截止时间，一并领取即可，不需要分开判断窗口。</p>
<p>核实于 2026-10-23 06:35 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 国区《Watch Tuner Lite》（id 968820626）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>Apple Watch 侧的调音与乐器辅助工具，汇总频道的播报口径是「本体限免」，回 iTunes lookup 用播报正文里的 trackId 核到国区现价为免费。最低系统 15.6。</p>
<p>口径边界要说清：核到现价 0 只等于「今天下载不花钱」，lookup 接口分不出「本就免费」与「促销中」，所以这里不写「限免仍在」；Apple 也不公布促销结束时间，那一栏只能空着。国区会给应用改名，所以认 id 不认名字。</p>
<p>核实于 2026-10-23 06:32（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id968820626">apps.apple.com/cn/app/id968820626</a></p>
</details>

<details>
<summary><strong>App Store 国区《Projects Timer》（id 6785089676）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>多项目并行计时器，播报为「本体限免」，实测现价免费。最低系统 18.0。做按项目分段写作或录素材的人可以直接拿来替掉计时器 + 备忘录的组合。</p>
<p>核实于 2026-10-23 06:32 · 直链 <a href="https://apps.apple.com/cn/app/id6785089676">apps.apple.com/cn/app/id6785089676</a></p>
</details>

<details>
<summary><strong>App Store 国区《Retro Widget 3: Classic Snake》（id 1534337551）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>主屏小组件形态的贪吃蛇，播报为「本体限免」，实测现价免费。最低系统 18.0。</p>
<p>核实于 2026-10-23 06:32 · 直链 <a href="https://apps.apple.com/cn/app/id1534337551">apps.apple.com/cn/app/id1534337551</a></p>
</details>

<details>
<summary><strong>Mac App Store《Fish Image Viewer》（id 6738393886）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>桌面端看图工具（返回的商店条目带 <code>mt=12</code>，是 macOS 应用而不是 iOS 应用），播报为「本体限免」，实测现价免费。最低系统 14.0。macOS 本机直接可用，这类桌面端限免在 iOS 那一层里是稀缺的。</p>
<p>核实于 2026-10-23 06:32 · 直链 <a href="https://apps.apple.com/cn/app/id6738393886">apps.apple.com/cn/app/id6738393886</a></p>
</details>

<details>
<summary><strong>Mac App Store《Highlight my cursor》（id 6738329029）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>录屏与演示时高亮光标，同为 macOS 条目，播报为「本体限免」，实测现价免费。最低系统 15.0。对录教程视频的人是刚需小工具。</p>
<p>核实于 2026-10-23 06:32 · 直链 <a href="https://apps.apple.com/cn/app/id6738329029">apps.apple.com/cn/app/id6738329029</a></p>
</details>

<details>
<summary><strong>Steam 国区《Resident Evil 4》 -75%</strong> ｜ <span style="color:#1a7f37;">¥49.50</span>（原 ¥198.00） ｜ 截止 11-04 02:00</summary>
<p>本轮 Steam 折扣里绝对金额与折扣率同时到位的一条。判据来自 Steam 官方 <code>featuredcategories?cc=cn&amp;l=schinese</code> 接口：<code>original_price = 19800</code>、<code>final_price = 4950</code>（单位是分）、<code>discount_percent = 75</code>、<code>discount_expiration</code> 换算北京时间 11-04 02:00。</p>
<p>区域参数必须显式带 <code>cc=cn</code>：同一接口不带它时会按出口 IP 返回别的货币定价，数字对不上不是改价而是区域差异。</p>
<p>核实于 2026-10-23 06:36 · 直链 <a href="https://store.steampowered.com/app/2050650/?l=schinese">store.steampowered.com/app/2050650</a></p>
</details>

<details>
<summary><strong>Steam 国区《The Walking Dead: The Telltale Definitive Series》 -90%</strong> ｜ <span style="color:#1a7f37;">¥16.80</span>（原 ¥168.00） ｜ 截止 11-06 02:00</summary>
<p>本轮折扣率最高的一条（-90%），全套收录。同一接口给出 <code>original_price = 16800</code>、<code>final_price = 1680</code>、到期时间换算北京时间 11-06 02:00。</p>
<p>核实于 2026-10-23 06:36 · 直链 <a href="https://store.steampowered.com/search/?term=The%20Walking%20Dead%3A%20The%20Telltale%20Definitive%20Series&amp;cc=cn">Steam 国区搜索页</a></p>
</details>

<details>
<summary><strong>NVIDIA/OpenShell：面向 agent 集群的「安全私有运行时」</strong> ｜ <span style="color:#1a7f37;">0 元</span>（开源） ｜ 无截止，随时可读</summary>
<p>仓库自述是 "the safe, private runtime for autonomous AI agents"，定位是给成批跑的 agent 提供隔离与权限边界——这恰好是你现在这套「定时任务 + 浏览器桥 + 只读边界」手工搭出来的东西的工业化版本。值得看的是它怎么划沙箱边界、怎么管 agent 的工具授权，而不是它的宣传语。GitHub API 实测 17,650 star，最近一次更新 10-22（当天仍在动），当天 HN 234 分 / 125 评。</p>
<p>核实于 2026-10-23 06:39（GitHub 官方 API 回读 star 数与 updated_at） · 直链 <a href="https://github.com/NVIDIA/OpenShell">github.com/NVIDIA/OpenShell</a></p>
</details>

<details>
<summary><strong>luongnv89/claude-howto：示例驱动的 Claude Code 图文指南</strong> ｜ <span style="color:#1a7f37;">0 元</span>（开源文档） ｜ 无截止</summary>
<p>从基础概念到高级 agent 用法，按「可复制粘贴的例子」组织，43,130 star，最近一次更新 10-22。对你手上 10-25 00:15 定时那篇《从安装部署到入门 Claude Code：三条安装路线、模型接入、权限模式与日常命令一次讲清》是同一题材的交叉核对材料——尤其是权限模式那一节，可以拿它的说法对照官方文档，看有没有第三方案。GitHub API 实测数字与更新时间。</p>
<p>核实于 2026-10-23 06:39（GitHub 官方 API） · 直链 <a href="https://github.com/luongnv89/claude-howto">github.com/luongnv89/claude-howto</a></p>
</details>

<details>
<summary><strong>Ethereum 官方博客《Glamsterdam on Hoodi Postponed》</strong> ｜ <span style="color:#6b7280;">0 元（官方博客）</span> ｜ 无截止，但它会让旧的时间线作废</summary>
<p>Hoodi 测试网上的 Glamsterdam 分叉被推迟。这条的意义不在于「测试网又延期」，而在于它是<strong>一手源把已经公布过的时间线改掉了</strong>：昨天官方才发过《Glamsterdam Hoodi Testnet Announcement》（10-16），今天这条就是它的修订。任何按那批时间写的 EVM 升级内容、节点运维 checklist，都要跟着改日期。</p>
<p>定性依据：Ethereum 官方博客 <code>feed.xml</code> 里该条的 <code>pubDate = Thu, 22 Oct 2026 00:00:00 GMT</code> 与标题逐字命中。要说清一处不完美：permalink 正文本轮直取返回 404（站内路由），所以原文逐字未能通读，判据是官方 feed 里的这一条；真要引用具体新时间，得等你自己打开正文确认。</p>
<p>核实于 2026-10-23 06:36 · 直链 <a href="https://blog.ethereum.org/en/2026-10-22/glamsterdam-hoodi-delay">blog.ethereum.org/en/2026-10-22/glamsterdam-hoodi-delay</a></p>
</details>

## 观察（10）、币圈那一轮与方法

<details>
<summary><strong>观察清单：未核实、门槛高或只算转述的 10 组</strong></summary>
<table>
<thead><tr><th>条目</th><th>本轮证据</th><th>为什么只给观察</th></tr></thead>
<tbody>
<tr><td>Kraken 状态页 <code>Partially Degraded Service</code>（Coinbase 侧 All Systems Operational）</td><td>06:31 读官方 Statuspage 聚合，<strong>连续两天同一状态</strong></td><td>要不要紧取决于你是否在 Kraken 挂着资产与充提，雷达没有这项证据，所以既不升紧急也不做任何链上或交易所操作</td></tr>
<tr><td>币安公告《Updates on Tick Size for Spot Trading Pairs (2026-10-29)》</td><td>只取到标题</td><td>未按口径回公告正文核对生效交易对清单与精度数值；只有跑币安现货 API 的人需要自己展开</td></tr>
<tr><td>iOS 内购限免 4 款（Reactie 6802706711、手机测速 SpeedTest 6741730996、DualCamPro 6790040520、Storage Cleaner: SpaceFresh 6798147223）</td><td>iTunes 国区下载价确实是 0</td><td>内购解锁价不体现在下载价上，按口径只算转述，不写「限免」；Apple 也不公布促销结束时间</td></tr>
<tr><td>iOS 未核价 3 条 + iLinkbox（id 6756910810）</td><td>频道播报原文</td><td>前 3 条超出本轮 15 条核价额度、没走 iTunes lookup；iLinkbox 按 id 查不到上架记录，价格未核实</td></tr>
<tr><td>美国主机侦探转述两条机房优惠：Spaceship <code>.com</code> 首年 $3.60、<code>.net</code> $4.78（另称主机与邮箱免费试用 30 天）；HostGator 黑五早鸟 虚拟主机 $4.21/月起、VPS $2.24/月起、年付额外最高 8 折</td><td>中文站转述，ts 在 10-22</td><td>官方活动页本轮返回 403，最终价与「是否续费同价」都没核到；优惠类缺官方口径一律不进值得。这条对老域名续费没有直接影响，不构成紧急</td></tr>
<tr><td>PHP 漏洞那条线的余波：HN《Tell HN: I unknowingly broke the PHP RCE embargo》269 分 / 113 评、PANews 转述《美国纽约州金融服务局就关键 PHP 漏洞发布警报》、美国主机侦探转述《Google 提醒：PHP 补丁维护期间应返回 503，持续多日可能影响网站收录》</td><td>三个来源指向同一起事件</td><td>均未取到监管原文与 Google 原文；本站是 Jekyll 静态托管，不在 PHP 影响面。昨天那条已经用 php.net ChangeLog 核到并报道过，今天属旧闻延续，不重复升级</td></tr>
<tr><td>Garmin 改版并开放 Connect Developer API（lobsters 14 赞，来源 dcrainmaker 转述）</td><td>单一转述源</td><td>未回 Garmin 官方开发者页核对免费额度、申请门槛与速率限制，「开放」这个词的具体边界未知</td></tr>
<tr><td>行情与热度快照（06:31，CoinGecko / CoinMarketCap / alternative.me）</td><td>BTC $81,266（-3.9%）、ETH $2,382.85（-4.2%）、BNB $731.03（-2.5%）、XRP $1.31（-4.9%）、USDT $0.99894；24h 异动 ZEC $1,209.36（-10.3%）、Lighter -10.8%、Pump.fun -10.1%、Canton -10.0%、Akedo +27.1%、MemeCore +16.4%；CoinGecko 热搜 UHI / DACITY / OnlyAgent / PEARL / NEAR / BTC / PENGU / AVAX / AERO / HYPE；CMC 热搜 BTC / CASHCAT / SUI / Sleepless AI / DOGE / ZEC；恐惧贪婪指数 68（Greed）</td><td>它们是某一刻的数字，不是可执行信息；一律不给值得，也不构成任何操作建议</td></tr>
<tr><td>中英文加密媒体转述 39 条（CoinDesk 12 / The Block 12 / PANews 15）</td><td>其中《QuickSwap 将于 12 月 31 日结束 Soneium 部署界面运行，提醒用户提前撤出资产及 LP 头寸》涉及资产可得性</td><td>没有一条拿到一手原文；这类「撤出资产」只有在你确实用过 QuickSwap 的 Soneium 界面时才需要自己回项目方公告核对，雷达不代为操作</td></tr>
<tr><td>GitHub Trending 4 个库、Product Hunt 15 条、v2ex 9 条</td><td>榜单标题与 star/回复数快照</td><td>trending 与 PH 无发布时间戳、不参与窗口过滤，且未逐个读 README 判断是否真在解决关心的事；v2ex 的送码类要登录回帖才能领，门槛不透明</td></tr>
</tbody>
</table>
</details>

<details>
<summary><strong>币圈那一轮：四轴取到多少、以及为什么本轮只有 1 条值得</strong></summary>
<p>币圈跑了 11 个机器可读来源，四条轴各有落点：交易所动态（Binance 公告 1 条 + Coinbase/Kraken 状态页聚合 1 条）、行情与热度（CoinGecko 快照与异动 7 条、热搜 10 条、CMC 搜索榜 6 条、恐惧贪婪 1 条）、项目方一手（Ethereum 博客 1 条）、中英文媒体（PANews 15 / CoinDesk 12 / The Block 12）。</p>
<p>本轮币圈<strong>只有 1 条值得</strong>，就是 Ethereum 官方那条 Hoodi 推迟。理由和上一轮一样分三层：行情、热搜、情绪指数本身不构成价值，按口径全落观察；交易所公告只取到标题，没回正文核对生效时间与合约地址，链上资产只按代币符号认会认错，所以连「值得」的核实门槛都没过；唯一一手充分的，恰好是那条改了时间线的官方博客。</p>
<p>需要复查但没有升紧急的是 Kraken 的 <code>Partially Degraded Service</code>：它影响的是服务可用性而不是价格，但要不要紧取决于你有没有把资产挂在那儿——这条雷达没有证据。媒体里那条 QuickSwap 结束 Soneium 界面、提醒撤出 LP 的转述同理，只有真用过的人才需要自己回项目方公告核对，本站不代为做任何链上或交易所操作。</p>
<p>边界照旧：不连钱包、不签名、不导私钥与助记词、不代充代提、不给买卖建议与目标价；产物里不出现钱包地址、私钥、交易所 API key 与带返利参数的邀请链接；行情只作为「某时刻的快照」写，并标来源与时间。</p>
</details>

<details>
<summary><strong>这一轮的四步口径与来源健康度</strong></summary>
<p>四步：取数 → 验真 → 分级 → 存档与发布。</p>
<p>取数：25 个来源一轮约两分钟，<code>SUMMARY fetched=318 fresh=187 sources=25 errors=0</code>，整轮无 <code>ERR source=</code> 行。App Store 那一层依旧是瓶颈：播报频道只负责「今天有什么在限免」，每条还要回 iTunes lookup 用 trackId 核国区现价，一轮最多核 15 条且最新的先核，所以有 3 条被留在「未核价」。</p>
<p>验真：回官方页逐条复核共 6 处——Epic <code>freeGamesPromotions</code>（zh-CN / CN，逐条读 <code>discountPrice</code> 与 <code>appliedRules.endDate</code>）、Steam <code>featuredcategories?cc=cn</code>（读 <code>original_price</code>、<code>final_price</code>、<code>discount_expiration</code>）、iTunes lookup（五条本体限免现价 0）、GitHub API（两个仓库的 star 与 updated_at）、Ethereum 官方 <code>feed.xml</code>、Coinbase 与 Kraken 的 Statuspage。境内（IT之家、美国主机侦探、v2ex）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、GitHub）同时全绿，所以「代理节点疑似不可用」这一项今天不成立；Spaceship 与 HostGator 的官方页 403 属于站点侧的反爬，不是通道故障。</p>
<p>分级：<strong>紧急 0 条 / 值得 12 条 / 观察 10 组</strong>。本轮没有 ≤3 小时的临期项，也没有命中「在用服务受影响」，所以不占用紧急段。空源都不是故障：appinn 挂 <code>allow_empty</code>，打印 <code>INFO source=appinn empty=</code>，本轮确实没有限免帖；creleases、hf、ruanyifeng 是被两天窗口或跨天去重过滤掉，单跑可复现。</p>
<p>落点：本地存档 <code>~/aigc/info-radar/daily/2026-10-23.md</code>，本页是 GitHub Pages 那一份。边界声明：雷达只收集、验证、报告，绝不代为注册、绑卡、领券、下单；兑换码型福利不转载兑换码本身，只留原帖；币圈只读。</p>
</details>
