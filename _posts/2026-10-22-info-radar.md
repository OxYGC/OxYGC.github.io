---
title: "资讯雷达 2026-10-22｜Node.js 高危安全发布、Epic 周免今晚收口、PHP 8.2.35 与 GitLab 补丁"
author: OxYGC
date: 2026-10-22 06:25:00 +0800
permalink: /posts/info-radar-2026-10-22/
categories: [Info, Deals]
tags: [资讯雷达, Node.js, 安全更新, 限免, Steam优惠, PHP, GitLab, DuckDB]
description: "2026-10-22 一轮 25 个来源的资讯雷达：Node.js 24.x 高危安全发布、Epic 本批周免今晚 23:00 截止、App Store 国区四条本体限免、Steam 国区促销与 PHP/GitLab/DuckDB 三条一手官方动态，全部标注核实时间与截止时间。"
---

这一轮跑了 25 个来源，取回 314 条，两天窗口加跨天去重之后留下 179 条新的，0 个来源报错。真正值得单独拎出来的只有一条：**Node.js 在 10 月 21 日发了安全发布，24.x 这条线的官方严重级别是 HIGH**，而本机 `node -v` 正好在读 24.15.0，所以它不是"今天的技术新闻"，是"今天该做的维护"。福利侧最紧的是 Epic 本批周免，今晚 23:00（北京时间）收口，App Store 国区那四条本体限免仍然只能保证"今天下载不花钱"。剩下的优惠与动态里，能拿到一手官方页的只有 PHP、GitLab、DuckDB 和 Steam 这四处，其余中文站转述的机房活动全部按口径压在观察段。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:14px 16px;background:#fbfcfd;">

| 时点 | 条目 | 价格 | 去哪 |
| --- | --- | --- | --- |
| <span style="color:#c0392b;font-weight:700;">无截止，风险从今天开着</span> | Node.js 24.x 安全发布（含 Brotli 解码器越界写 RCE） | 0 元（版本升级） | [nodejs.org 漏洞公告](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) |
| <span style="color:#c0392b;font-weight:700;">10-22 23:00 截止，剩约 16 小时</span> | Epic 本批周免两款（Agent A、Bad Cheese） | <span style="color:#1a7f37;">0 元</span> | [Epic 免费游戏页](https://store.epicgames.com/free-games?lang=zh-CN) |
| 11-02 截止 | Steam 国区《黎明杀机》-60% | <span style="color:#1a7f37;">¥37.50</span>（原 ¥93.75） | [Steam 商店页](https://store.steampowered.com/app/381210/?l=schinese) |
| 10-22 已发布，建议本周复查 | PHP 8.2.35 / GitLab Critical Patch / DuckDB 2.0.0 LTS | 0 元（源码或开源） | [PHP ChangeLog](https://www.php.net/ChangeLog-8.php) |

</div>

## 值得看（10）

<details>
<summary><strong>Node.js 2026-10-21 安全发布，24.x 线官方定级 HIGH</strong> ｜ <span style="color:#1a7f37;">0 元（升级）</span> ｜ <span style="color:#c0392b;">无截止，在用即需处理</span></summary>
<p>影响面是运行时本身，不是某个站点。官方页逐条列出的高危项：<code>dns.resolve</code> 会截断含 NUL 字符的名字（CVE-2026-105482）、TLS 证书主机名在全角数字写法下被绕过（CVE-2026-105483）、主机名被宽松解析成 IP 时绕过校验（CVE-2026-106069），以及 <strong>Brotli 解码器越界写，可导致远程代码执行（CVE-2026-111497）</strong>；另有 keep-alive 响应时序、非规范 IPv4 主机名证书校验、<code>crypto.randomUUID()</code> 熵缓存被写进启动快照等 medium/low 若干。受影响版本线是 26.x / 24.x / 22.x，三条线的官方级别都标 HIGH。这次发布同时更新了 c-ares、OpenSSL、SQLite、Undici 与 ca-cert 依赖，其中 ca-cert 那一条对应的正是 eMudhra 中间 CA 私钥泄露事件，跟着升级一起解决。</p>
<p>你能做的：把 Node 升到 24.x 的最新补丁版（<code>node -v</code> 先确认自己在哪条线），容器基础镜像与 CI 里的固定版本号同步改。雷达不代为改环境。<br>核实于 2026-10-22 06:35 · 直链 <a href="https://nodejs.org/en/blog/vulnerability/october-2026-security-releases">nodejs.org/en/blog/vulnerability/october-2026-security-releases</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Agent A - 伪装游戏》</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥62.00） ｜ <span style="color:#c0392b;">截止 10-22 23:00，剩约 16 小时</span></summary>
<p>潜行解谜类，领取即永久入库，不需要赶在截止前玩完。这是本批最后一次机会，接口给的是 <code>2026-10-22T15:00:00Z</code>，也就是北京时间 23:00；同一时刻中文商店页有时会渲染成次日 00:00，两处都是官方来源，按早的动手。判据是 <code>discountPercentage == 0</code> 才算免费，Epic 每周固定放两款，决定做一次就够。</p>
<p>核实于 2026-10-22 06:37（<code>--source epic --days 7</code> 单跑复验，本批两款仍在架） · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Bad Cheese》</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥40.00） ｜ <span style="color:#c0392b;">截止 10-22 23:00</span></summary>
<p>与上一条同一批、同一截止时间，一并领取即可。</p>
<p>核实于 2026-10-22 06:37 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 国区《Sharp Lynx 系统监控》（macOS，id 453164367）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>菜单栏系统监控工具，是这批里唯一的桌面端，播报口径为「本体限免」，回 iTunes 用播报正文里的 trackId 核到国区现价为免费。最低系统 14.0。</p>
<p>口径边界要说清：核到现价 0 只等于"今天下载不花钱"，lookup 接口分不出"本就免费"与"促销中"，所以这里不写"限免仍在"；Apple 也不公布促销结束时间，那一栏只能空着。国区会给应用改名，所以认 id 不认名字。</p>
<p>核实于 2026-10-22 06:20 · 直链 <a href="https://apps.apple.com/cn/app/id453164367">apps.apple.com/cn/app/id453164367</a></p>
</details>

<details>
<summary><strong>App Store 国区《卡待删 - 相册清理助手》（ReelSort，id 6785087820）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>相册重复与废片清理，播报为「本体限免」，iTunes 国区实测现价为免费。最低系统 16.0。</p>
<p>核实于 2026-10-22 06:23 · 直链 <a href="https://apps.apple.com/cn/app/id6785087820">apps.apple.com/cn/app/id6785087820</a></p>
</details>

<details>
<summary><strong>App Store 国区《FocusTodo — Minimal List》（id 6754666421）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>极简待办工具，播报为「本体限免」，实测现价免费。最低系统 16.6。</p>
<p>核实于 2026-10-22 06:22 · 直链 <a href="https://apps.apple.com/cn/app/id6754666421">apps.apple.com/cn/app/id6754666421</a></p>
</details>

<details>
<summary><strong>App Store 国区《7Player》（id 6812360078）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>本地播放器，播报为「本体限免」，实测现价免费。最低系统 17.0。</p>
<p>核实于 2026-10-22 06:21 · 直链 <a href="https://apps.apple.com/cn/app/id6812360078">apps.apple.com/cn/app/id6812360078</a></p>
</details>

<details>
<summary><strong>Steam 国区《黎明杀机 / Dead by Daylight》 -60%</strong> ｜ <span style="color:#1a7f37;">¥37.50</span>（原 ¥93.75） ｜ 11 月 2 日截止</summary>
<p>本轮唯一一条新报的 Steam 促销（其余为往期已报道的存量）。商店页促销条原文是"特别促销！11 月 2 日截止"，接口 <code>discount_expiration = 2026-11-02T18:00:00</code>，两处一致。</p>
<p>核价时有个值得记的细节：同一个 <code>appdetails</code> 接口，不带 <code>cc=cn</code> 时按出口 IP 返回的是日元定价（¥2,499 → ¥999），带 <code>cc=cn</code> 才是国区的 9375 分原价、3750 分现价、60% 折扣。这不是改价，是商店区域差异，所以区域必须显式指定。同样 -60% 这一档折扣在两种货币下都是成立的。</p>
<p>核实于 2026-10-22 06:33 · 直链 <a href="https://store.steampowered.com/app/381210/?l=schinese">store.steampowered.com/app/381210</a></p>
</details>

<details>
<summary><strong>PHP 8.2.35 已发布（10-22）</strong> ｜ <span style="color:#1a7f37;">0 元</span>（源码与发行版） ｜ 无截止，建议尽快升级</summary>
<p>这两天"PHP 零日、要大修了"的讨论在今天有了官方收口版。ChangeLog 正文标注 <code>Version 8.2.35 22 Oct 2026 — Core: Fixed GHSA-w8hw-w9fx-j79w、GHSA-6wmf-4rv5-p3rp（Avoid state corruption via bailout）</code>。同一条线在四个来源同时上榜：HN 的《PHP 8.2.35》939 分、《Today's PHP security release》576 分，lobsters 的《Upcoming Critical PHP Security Release》171 赞，LowEndBox 的《Patch Your PHP! The PHPopaclypse is Upon Us!》，以及 v2ex 的《PHP 最新零日漏洞怎么没人讨论》103 回。HN 另一条《AWS rates PHP RCE as Important so Amazon Linux 2023 patch may take 20 days》提醒的是发行版侧的补丁节奏差，跑 Amazon Linux 2023 + PHP 的话要自己盯 OS 层更新。</p>
<p>核实于 2026-10-22 06:37 · 直链 <a href="https://www.php.net/ChangeLog-8.php">www.php.net/ChangeLog-8.php</a></p>
</details>

<details>
<summary><strong>GitLab Critical Patch Release：19.5.1 / 19.4.3 / 19.3.6 / 19.2.9 / 19.1.9 / 19.0.10 / 18.11.13</strong> ｜ <span style="color:#1a7f37;">0 元</span>（版本升级） ｜ 无截止，自建实例本周复查</summary>
<p>官方一手补丁公告，页面日期 October 21, 2026，一次性覆盖七条版本线——这个跨度本身说明问题的通用性。自建 GitLab 或在用 GitLab 托管的人要对照自己那条线取对应小版本。同一帖在 HN（169 分）与 lobsters 双榜，但定性以官方页为准。</p>
<p>核实于 2026-10-22 06:37（回源 200，标题与日期逐字命中） · 直链 <a href="https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/">docs.gitlab.com 补丁公告</a></p>
</details>

<details>
<summary><strong>DuckDB 2.0.0 LTS「Cinnamon Teal」</strong> ｜ <span style="color:#1a7f37;">0 元</span>（开源） ｜ 无截止</summary>
<p>嵌入式分析库进入 LTS 周期，官方公告发布于 2026-10-21。做后端本地 OLAP、数据湖查询、或者想把一次性分析脚本从 pandas 挪到 SQL 的话，LTS 意味着可以把它写进长期依赖清单。HN 337 分 / 39 评。</p>
<p>核实于 2026-10-22 06:38（回源 200） · 直链 <a href="https://duckdb.org/2026/10/21/announcing-duckdb-200">duckdb.org 发布公告</a></p>
</details>

## 观察（14）、币圈那一轮与方法

<details>
<summary><strong>观察清单：未核实、门槛高或只算转述的 14 组</strong></summary>
<table>
<thead><tr><th>条目</th><th>本轮证据</th><th>为什么只给观察</th></tr></thead>
<tbody>
<tr><td>LiteLLM 1.107.0 在 PyPI 被投毒（凭证窃取 + 后门）</td><td>06:36 读官方 PyPI JSON：<code>1.107.0</code> 不在发布列表（只有 dev1/2/3 与 rc1/rc2），最新稳定版 1.106.2</td><td>事件本身只有两家安全厂商博客在讲（safedep.io、hexaclaw.com），未取到 LiteLLM 项目方一手公告；PyPI 现状与"该版已撤下"方向一致，但不足以定性</td></tr>
<tr><td>Kraken 状态页 <code>Partially Degraded Service</code>（Coinbase 侧 All Systems Operational）</td><td>06:24 聚合读 <code>status.kraken.com/api/v2/status.json</code></td><td>要不要紧取决于你是否在 Kraken 挂着充提，雷达没有这项证据，因此不给紧急</td></tr>
<tr><td>Binance 公告 7 条（含 Margin 小额欠款账户常规清理，标题日期 2026-10-27；USDⓈ-M tick size 更新；TradFi 永续两类更新；bStocks 抵押品与新交易对）</td><td>只取到标题</td><td>未按口径回公告正文核对生效时间与合约地址；只有在用币安杠杆/合约的人需要自己展开</td></tr>
<tr><td>go-ethereum v1.17.9「Universal Semiconductor」</td><td>06:31 读 GitHub 一手 release note（发布于 2026-10-21T15:08:46Z）</td><td>正文写的是在 Hoodi 测试网块时间戳 1793036568（10-26 17:42:48 UTC）启用 Amsterdam 分叉，加 EVM opcode 派发提速 16% 与若干掉电数据库损坏修复，推荐给 Hoodi 测试网运营者，全文无安全公告——不满足"安全补丁版"的值得门槛</td></tr>
<tr><td>Epic 另外两款（纪念碑谷 ¥33.00→¥11.55、Eternal Threads ¥62.00→¥12.40）</td><td>06:37 同一接口，档期到 <code>2026-11-02T16:00:00Z</code>（北京 11-03 00:00）</td><td>它们是打折不是限免，判据仍是 <code>discountPercentage == 0</code></td></tr>
<tr><td>iOS 四条内购限免（Chill 1622262960、奶茶日记 6760588830、Leafora 6781948787、闹钟 6748983354）</td><td>iTunes 下载价本就是 0</td><td>内购解锁价不体现在下载价上，按口径只算转述，不写"限免"</td></tr>
<tr><td>v2ex 两条开发者自办送码（Vanto 送 200 份永久版，64 回；SiteGlance 附兑换码，88 回）</td><td>榜单标题与回复数</td><td>兑换码型福利按口径不转载 <code>code=</code>，只留原帖由本人取；且要登录回帖才能领，门槛不透明</td></tr>
<tr><td>美国主机侦探 7 条机房活动（衡天云双十一 12 元/月起、恒创科技 2.2 折买 3 年送 1 年、LisaHost 9929 住宅 IP VPS 月付 61.2 元起、BlueHost AI All-Access $20/月起，另含一篇机型对比与两篇教程）</td><td>中文站转述，ts 全在 10-21</td><td>未回厂商官方活动页核价与截止时间，优惠/限免类缺官方口径一律不进值得</td></tr>
<tr><td>musl libc <code>regcomp</code> 多个整数溢出 CVE-2026-107891</td><td>lobsters 19 赞（10-21 12:40 榜）</td><td>未回 CVE 原文核对受影响版本与发行版修复状态</td></tr>
<tr><td>行情与热度快照（06:24）</td><td>BTC $84,594（+2.0%）、ETH $2,488.41（+1.2%）、BNB $749.98（+1.1%）、XRP $1.37（+2.8%）、USDT $0.999473；24h 异动 Pearl +13.0%、Lighter +12.2%、Bitway -10.5%、Ethena +8.9%、Canton +8.4%；CoinGecko 热搜 UHI / AERO / PENGU / PEARL / NEAR / BTC / LIT / AXIS / TAO / STRK；CMC 热搜 BTC / ETH / XRP / QNT / NEAR / ZEC；恐惧贪婪指数 63（Greed）</td><td>它们是某一刻的数字，不是可执行信息；一律不给值得，也不构成任何操作建议</td></tr>
<tr><td>eMudhra 中间 CA 私钥被毫秒级破解（《Eight Bits of Trust》）</td><td>HN 786 分 / 385 评，lobsters 同题双榜</td><td>一手来源仍是 10-20 的 Mozilla 处置公告；今天新增的可信证据是 Node.js 把 ca-cert 更新打包进了上面那条安全发布，跟着升级即可，不需要单独动作</td></tr>
<tr><td>中英文媒体转述 38 条（CoinDesk 12 / The Block 11 / PANews 15）</td><td>含《OpenAI 更新使用政策：模型中转平台须经审批》《特斯拉 Q3 营收 280.5 亿美元，未出售所持比特币》</td><td>没有一条拿到一手原文，政策与财报类按口径不进值得</td></tr>
<tr><td>GitHub Trending 3 个库（strelov1/freehire 2,342★、supabase/supabase、twentyhq/twenty 59,114★）</td><td>06:24 star 数快照</td><td>trending 无发布时间戳、不参与窗口过滤，且未逐个读 README 判断是否真在解决关心的事</td></tr>
<tr><td>史泰博遭入侵：劫持员工会话生成超 1.5 万张礼品卡、面值逾 500 万美元（IT之家 10-21 14:01）</td><td>中文资讯源单条</td><td>厂商通告与规则原文本轮没核到；同列表里《请立即更新：Node.js 发布最高严重级别高危安全更新》那条已用官方页核到并升为紧急</td></tr>
</tbody>
</table>
</details>

<details>
<summary><strong>币圈那一轮：四轴取到多少、以及为什么整段没有一条值得</strong></summary>
<p>这一轮币圈跑了 11 个机器可读来源：交易所公告（Binance 三个目录 + Coinbase/Kraken 状态页）、行情与热度（CoinGecko 两个接口、CMC 搜索榜、恐惧贪婪指数）、项目方一手（Ethereum 博客、go-ethereum / Agave 的 GitHub release）、中英文媒体（PANews、CoinDesk、The Block）。</p>
<p>留下的结论是：<strong>这一轮币圈 0 条值得、0 条紧急</strong>。理由分三层。第一，行情、热搜、情绪指数本身不构成价值，它们只是某一刻的数字，按口径全部落在观察；第二，交易所公告这一轮只取到标题，没回正文核对生效时间与合约地址，链上资产只按代币符号认会认错，所以连"值得"的核实门槛都没过；第三，唯一一条一手材料充分的 go-ethereum v1.17.9，读完 release note 之后判定它不是安全版本，而是测试网分叉启用 + 性能与稳定性修复，给的是 Hoodi 测试网运营者。</p>
<p>唯一一条需要复查的是 Kraken 状态页的 <code>Partially Degraded Service</code>：它影响的是服务可用性而不是价格，但要不要紧取决于你有没有把资产挂在那儿——这条雷达没有证据，所以既不升紧急，也不做任何链上与交易所操作。</p>
<p>边界照旧：不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价，产物里不出现钱包地址、私钥、助记词与带返利参数的邀请链接。</p>
</details>

<details>
<summary><strong>这一轮的四步口径与来源健康度</strong></summary>
<p>四步：取数 → 验真 → 分级 → 存档与发布。</p>
<p>取数：25 个来源，约 55 秒，<code>SUMMARY fetched=314 fresh=179 sources=25 errors=0</code>，无 <code>ERR source=</code> 行。大头时间花在 App Store 那一层——播报频道只负责"今天有什么在限免"，每条还要回 iTunes lookup 用 trackId 核国区现价，一轮最多核 15 条且最新的先核。</p>
<p>验真：官方页逐条回源共 6 处——Node.js 漏洞公告、Epic 免费游戏接口、Steam <code>appdetails</code>（带 <code>cc=cn</code>）与商店页促销条、PHP 8 ChangeLog、GitLab 补丁公告、DuckDB 发布公告；go-ethereum 读了 GitHub 一手 release note；LiteLLM 读了 PyPI 官方 JSON。境内（IT之家、美国主机侦探、v2ex）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、Hugging Face）同时全绿，所以"代理节点疑似不可用"这一项今天不成立。</p>
<p>分级：<strong>紧急 1 条 / 值得 10 条 / 观察 14 组</strong>。空源 5 个都不是故障：epic 与 ruanyifeng、hf、ethblog 是被跨天去重或两天窗口过滤掉（06:37~06:39 分别单跑 <code>--days 7</code>/<code>--days 30</code> 复验能取到内容），appinn 挂 <code>allow_empty</code>，打印 <code>INFO source=appinn empty=</code>，本轮确实没有限免帖。</p>
<p>落点：本地存档 <code>~/aigc/info-radar/daily/2026-10-22.md</code>，本页是 GitHub Pages 那一份。边界声明：雷达只收集、验证、报告，绝不代为注册、绑卡、领券、下单；兑换码型福利不转载兑换码本身；币圈只读。</p>
</details>
