---
title: "资讯雷达 2026-10-24｜Epic 周免效期复查、Steam 两项带截止、App Store 一条核到免费与 OpenShell、VoxCPM"
author: OxYGC
date: 2026-10-24 06:42:00 +0800
permalink: /posts/info-radar-2026-10-24/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Epic, Steam优惠, AppStore, AI-Agent, TTS, 币圈]
description: "2026-10-24 一轮 25 个来源的资讯雷达：Epic 两款周免的效期复查（10-29 23:00 收口）、Steam 国区两项带截止的折扣、App Store 国区一条核到下载价 0 的本体限免、OpenShell 与 VoxCPM 两个仓库、go-ethereum v1.17.10 一手发版，全部标注核实时间与截止时间。"
---

这一轮跑了 25 个来源，取回 311 条，两天窗口加跨天去重之后留下 168 条，0 个来源报错。结论先摆出来：<strong>本轮仍然没有紧急项</strong>——最近的硬截止还是 Epic 这批周免 10 月 29 日 23:00（北京时间）收口，还剩五天；没有任何一条命中「影响在用的域名、VPS 或在用 API 的免费额度」，也没有一条命中「直接影响在用资产可得性」的交易所公告。要说的一处变化是福利侧的口径：Epic 那两款昨天已经报过，今天的取数轮因为去重键是标题而没再把它们放进新增名单，所以这一篇给的是<strong>效期复查</strong>而不是新消息——06:36 重读官方端点，<code>discountPrice</code> 仍然是 0，截止时间一字未变。App Store 侧今天只有一条播报核到免费下载价。开发侧留下 OpenShell（agent 的隔离运行时）与 VoxCPM2（多语种 TTS + 声音克隆）两个仓库，币圈侧唯一一手材料充分的是 go-ethereum v1.17.10 正式发布。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:14px 16px;background:#fbfcfd;">

| 时点 | 条目 | 价格 | 去哪 |
| --- | --- | --- | --- |
| <span style="color:#c0392b;font-weight:700;">10-29 23:00 截止，剩约 5 天</span> | Epic 本批周免两款（《Sker Ritual》《Home》）效期复查 | <span style="color:#1a7f37;">0 元</span>（原 ¥78 / ¥15） | [Epic 免费游戏页](https://store.epicgames.com/free-games?lang=zh-CN) |
| <span style="color:#c0392b;font-weight:700;">10-30 01:00 截止，剩约 5 天</span> | Steam 国区《再再启程》 -20% | <span style="color:#1a7f37;">¥54.40</span>（原 ¥68.00） | [Steam 商店页](https://store.steampowered.com/app/4817620/?l=schinese) |
| 11-06 02:00 截止 | Steam 国区《饥荒联机版》 -50% | <span style="color:#1a7f37;">¥12.00</span>（原 ¥24.00） | [Steam 商店页](https://store.steampowered.com/app/322330/?l=schinese) |
| <span style="color:#6b7280;font-weight:700;">Apple 不公布限免截止时间</span> | App Store 国区《Yaosamo Time》本体限免 | <span style="color:#1a7f37;">下载 0 元</span> | [apps.apple.com/cn/app/id6759643546](https://apps.apple.com/cn/app/id6759643546?mt=12) |

</div>

## 值得看（9）

<details>
<summary><strong>Epic 本周限免《Sker Ritual（斯盖尔仪式）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥78.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00，剩约 5 天</span></summary>
<p>10-23 那一篇已经报道过它，本轮取数没有再把它列进新增，是因为 Epic 这一路的去重键是标题（<code>ident = title</code>）——同一款限免持续多天，只在第一次出现时报。这一条的价值不是「新消息」，而是<strong>复查</strong>：06:36 重读官方 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 端点，<code>discountPrice</code> 仍为 0，<code>appliedRules.endDate = 2026-10-29T15:00:00Z</code>，换算北京时间 23:00，与昨天完全一致。</p>
<p>僵尸题材 roguelike 卡牌，<strong>领取即永久入库</strong>，不需要赶在截止前玩完。另外注意 Epic 中文商店页有时把同一时刻渲染成次日 00:00，两处都是官方来源，按早的动手。</p>
<p>核实于 2026-10-24 06:36（Epic 官方端点） · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure（归家）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥15.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00</span></summary>
<p>与上一条同一批、同一截止时间，一并领即可，不需要分开判断窗口。本轮复查官方端点仍为 <code>discountPrice = 0</code>、<code>originalPrice = 1500</code>（单位是分）。</p>
<p>核实于 2026-10-24 06:36 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 国区《Yaosamo Time / Timezone Clock》（id 6759643546）</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>菜单栏／桌面的多时区时钟，汇总频道的播报口径是「本体限免」，回 iTunes lookup 用播报正文里那个 trackId 核到国区 <code>formattedPrice = 免费</code>、<code>price = 0.0</code>，商店返回带 <code>mt=12</code>，也就是 Mac App Store 条目，本机直接可用。最低系统 15.6，开发者署名 Yaroslav Samoylov。</p>
<p>三处口径要说清：其一，核到现价 0 只等于「今天下载不花钱」，lookup 接口分不出「本就免费」与「促销中」，所以不写「限免仍在」；其二，Apple 不公布促销结束时间，那一栏只能这么空着，编一个日期出来反而更糟；其三，国区会给应用改名，所以一律认 id 不认名字。</p>
<p>核实于 2026-10-24 06:35（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id6759643546">apps.apple.com/cn/app/id6759643546</a></p>
</details>

<details>
<summary><strong>Steam 国区《饥荒联机版》（app 322330） -50%</strong> ｜ <span style="color:#1a7f37;">¥12.00</span>（原 ¥24.00） ｜ <span style="color:#c0392b;">截止 11-06 02:00</span></summary>
<p>本轮 Steam 折扣里折扣率最高的一条，也是那种「买了会真的开」的长期合作生存类。判据来自官方 <code>featuredcategories?cc=cn&amp;l=schinese</code>：<code>original_price = 2400</code>、<code>final_price = 1200</code>（接口给的是分）、<code>discount_percent = 50</code>、<code>discount_expiration = 1793901600</code>，那是 UTC 秒，换算北京时间 11 月 6 日 02:00。</p>
<p>区域参数必须显式带 <code>cc=cn</code>：不带它会按出口 IP 返回别的货币定价，数字对不上不是改价而是区域差异。</p>
<p>核实于 2026-10-24 06:41（Steam 官方接口） · 直链 <a href="https://store.steampowered.com/app/322330/?l=schinese">store.steampowered.com/app/322330</a></p>
</details>

<details>
<summary><strong>Steam 国区《再再启程》（app 4817620） -20%</strong> ｜ <span style="color:#1a7f37;">¥54.40</span>（原 ¥68.00） ｜ <span style="color:#c0392b;">截止 10-30 01:00</span></summary>
<p>绝对金额与折扣率都一般，列进「值得」的理由只有一条：它是本轮 specials 里另一条带明确截止时刻的折扣，<code>discount_expiration = 1793293205</code> 换算北京时间 10 月 30 日 01:00，比 Epic 那批还早收口一天。要不要动取决于你玩不玩，不玩就划掉。</p>
<p>核实于 2026-10-24 06:41 · 直链 <a href="https://store.steampowered.com/app/4817620/?l=schinese">store.steampowered.com/app/4817620</a></p>
</details>

<details>
<summary><strong>NVIDIA / OpenShell：给 agent 用的「安全私有运行时」</strong> ｜ <span style="color:#6b7280;">0 元（开源）</span> ｜ 无截止，随时可读</summary>
<p>仓库自述是 <code>the safe, private runtime for autonomous AI agents</code>，定位是给成批运行的 agent 提供隔离与工具授权边界——恰好是「定时任务 + 浏览器桥 + 只读边界」这套手工搭法的产品化版本。值得读的是它怎么划沙箱、怎么表达工具授权，而不是那句宣传语。</p>
<p>与昨天那条相比的变化是活跃度：官方 API 给到 18,738 star（昨天 17,650），最近一次 push 是 2026-10-23T22:34:16Z，也就是北京时间今天 06:34，仍在高速迭代期。</p>
<p>核实于 2026-10-24 06:39（GitHub 官方 API） · 直链 <a href="https://github.com/NVIDIA/OpenShell">github.com/NVIDIA/OpenShell</a></p>
</details>

<details>
<summary><strong>OpenBMB / VoxCPM（VoxCPM2）：无 tokenizer 的多语种 TTS + 音色克隆</strong> ｜ <span style="color:#6b7280;">0 元（开源）</span> ｜ 无截止</summary>
<p>自述覆盖多语种语音生成、创意音色设计与「逼真声音克隆」，40,226 star。和做频道配音、口播素材那条线直接对口，可以先在本地拿一段自己的文案试合成，再决定要不要进工作流。</p>
<p>一句提醒：声音克隆类模型的商用与音色授权合规要自己读仓库那一章再定，雷达只报「它存在且开源」，不替你判许可。</p>
<p>核实于 2026-10-24 06:39（GitHub 官方 API：40,226 star，最近一次 push 2026-10-08） · 直链 <a href="https://github.com/OpenBMB/VoxCPM">github.com/OpenBMB/VoxCPM</a></p>
</details>

<details>
<summary><strong>《UUIDv7 doesn't have the properties you think it does》</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>拆的是 UUIDv7 的排序性与唯一性直觉误区——「带时间戳所以天然可排序所以能当游标」这一串推理里哪一步不成立。写后端基础类选题的人可以直接接：它同时挂在 Hacker News（93 分 / 78 评）与 lobsters（39 赞 / 12 评），属双通道互证而不是单点热帖。</p>
<p>核实于 2026-10-24 06:31（HN Algolia 官方接口 + lobsters 官方 RSS） · 直链 <a href="https://alexsci.com/blog/uuidv7-is-weird/">alexsci.com/blog/uuidv7-is-weird</a></p>
</details>

<details>
<summary><strong>go-ethereum v1.17.10「Soil Reducer」正式发布</strong> ｜ <span style="color:#6b7280;">0 元（项目方一手）</span> ｜ 无截止</summary>
<p>核心客户端发版，来源是项目方自己的 GitHub releases，不是媒体转述。官方 API 给 <code>published_at = 2026-10-23T12:07:39Z</code>（北京时间 10 月 23 日 20:07）、<code>prerelease = false</code>，前序版本 v1.17.9 是 10-21 发的，两天一版属于补丁节奏。</p>
<p>对写 EVM / 节点类内容的人来说，这条的意义是「引用的版本号要跟着改」；自己是否升级取决于是否真的在跑节点，雷达不给操作建议。</p>
<p>核实于 2026-10-24 06:39（GitHub 官方 releases API，仓库 51,408 star） · 直链 <a href="https://github.com/ethereum/go-ethereum/releases/tag/v1.17.10">releases/tag/v1.17.10</a></p>
</details>

## 观察（12）、币圈那一轮与方法

<details>
<summary><strong>观察 12 条（每条末尾写存疑原因）</strong></summary>
<table>
<tr><th>条目</th><th>为什么只放观察</th></tr>
<tr><td>交易所服务状态：Coinbase <code>Service Under Maintenance</code>（indicator=maintenance，updated_at 北京 10-24 01:00）、Kraken <code>Partially Degraded Service</code>（indicator=minor，updated_at 北京 10-24 06:24）</td><td>06:36 回读两家官方 Statuspage，Kraken 已是连续第三天同状态。要不要紧取决于有没有把资产挂在这两家，雷达没有这项证据，按口径既不升紧急也不做任何链上或交易所侧动作。</td></tr>
<tr><td>Initia 安全事件：The Block《Initia halts network after security incident as attacker reportedly mints tokens》＋ PANews《Initia：暂停 L1 及 Rollup 运行》《Upbit 与 Bithumb 暂停 INIT 充提并发布警示》《黑客已套现约 260 万美元》</td><td>两个独立媒体源指向同一起事件，但本轮没拿到 Initia 项目方 advisory 原文，也没核对涉事合约地址。安全事件只认项目方 advisory / 官方博客 / 交易所公告三方之一，媒体单独转述一律降观察。</td></tr>
<tr><td>印度最大交易所否认被黑（CoinDesk，链上分析者称约 1600 万美元可疑流出）</td><td>「疑似」来自链上分析者而非交易所或监管，未取到一手；与 Initia 是不同事件，不要合并读。</td></tr>
<tr><td>iOS《Magic PiP》（id 1613046504）</td><td>播报为「本体限免」，但 iTunes lookup 按 id 查不到上架记录（<code>resultCount = 0</code>），价格未核实，也不排除已下架。Apple 不公布限免截止时间。原帖 <a href="https://t.me/TossTF/3755">t.me/TossTF/3755</a> 留给需要自己核对的人。</td></tr>
<tr><td>智谱 ZCode 1024 程序员节送 5 亿 Tokens（小众软件转述）</td><td>官方域名本轮只拿到 307 跳转，未回官方活动页核到额度、领取门槛与截止时间。免费额度类一律要官方口径才进「值得」。</td></tr>
<tr><td>美国主机侦探 7 条机房／域名优惠（Gname·Namecheap·NameSilo 转入价对比、LisaHost 越南双 ISP VPS 9 折低至 79.2 元/月、RakSmart 北美精品 CN2 多 IP 上线、NovixLink 美国 NTT 住宅 IP 月付 7.99 加元起、Just Hosting 21 周年 VPS 首期 6 折、飞跨浏览器双 11 充赠、欧盟 PID 申报 11 月起实施）</td><td>全部是转述稿，未回各官方活动页核最终价与「是否续费同价」。其中欧盟 PID 申报那条如果涉及你在用的注册商，需要自己回注册商公告核对生效日期，雷达未取到官方原文。</td></tr>
<tr><td>lowendbox《Anthropic's IPO Is Coming Soon. Should You Buy?》</td><td>该源把它归在 deal 组，但内容是财经评论而非优惠，属软文形态，直接过滤，不作为优惠报道，也不构成任何投资参考。</td></tr>
<tr><td>行情与热度快照（06:31，CoinGecko / CoinMarketCap / alternative.me）：市值前 5 BTC $81,260（-0.0%）、ETH $2,393.65（+0.4%）、USDT $0.999171、BNB $740.51（+1.3%）、XRP $1.30（-0.2%）；异动 Akedo $0.0392592（+25.0%，rank 81）、Worldcoin $0.494475（-8.6%，rank 52）；CoinGecko 热搜 UHI / IRYS（+309.8%）/ PEARL / DACITY / PENGU / BTC / AAVE / AERO / DOT / AVAX；CMC 热搜 Irys / PEPE / BNB / SHIB / DOS / BIRB；恐惧贪婪指数 50（Neutral）</td><td>它们是某一刻的数字，不是可执行信息。行情、涨跌幅、热搜、情绪指数按口径一律不给「值得」，也不构成任何操作建议。</td></tr>
<tr><td>币安公告《Binance Will Support the ASML and Nokia Cash Dividend Distribution》（catalog 49 新产品与活动）</td><td>只取到标题，未回公告正文核对生效时间、标的范围与结算方式；只有真在跑币安相关 API 的人需要自己展开。</td></tr>
<tr><td>中英文加密媒体转述 38 条（CoinDesk 12 / The Block 11 / PANews 15）</td><td>本轮没有一条回到一手原文。其中《Ethereum delays Glamsterdam test…》与昨天已用 Ethereum 官方博客核到并报道过的是同一件事，今天只多了媒体口径，属旧闻延续，不重复升级。</td></tr>
<tr><td>阮一峰《科技爱好者周刊》第 416 期《编程已经面目全非》</td><td>官方 atom feed 里有这一条（时间戳 2026-10-23 17:09），但文章页直取返回 403（本机 UA 被反爬拦），未读到正文，无法判断其中哪条与你的方向相关——不据标题进「值得」。链接 <a href="https://www.ruanyifeng.com/blog/2026/10/weekly-issue-416.html">ruanyifeng.com/blog/2026/10/weekly-issue-416</a>。</td></tr>
<tr><td>GitHub Trending 其余 3 库、Product Hunt 14 条、v2ex 9 条、IT之家 25 条</td><td>trending 与 PH 无发布时间戳、不参与窗口过滤，且未逐个读 README 判断是否真在解决你关心的事（ziwei-doushu 6,831★ 紫微排盘引擎、SnailSploit/Claude-Red 8,419★ 攻击性安全 skills 集、nodejs/node）；v2ex 当天热帖多为闲聊与职业困惑，与发文选题没有直接接口。</td></tr>
</table>
</details>

<details>
<summary><strong>币圈这一轮怎么取的、来源健康度与四步口径</strong></summary>
<p><strong>取数结果</strong>：<code>SUMMARY fetched=311 fresh=168 sources=25 errors=0</code>，整轮没有任何 <code>ERR source=</code> 行，也没有 <code>INFO source=appinn empty=</code>（appinn 本轮有 1 条）。25 个 source key 全部返回成功，其中 22 个有新增，3 个本轮 0 条：<code>epic-store</code>（去重键是标题，昨天已报，效期至 10-29 23:00，本篇按「效期复查」重新核了一遍）、<code>ethblog</code>（两天窗口内无新帖，昨天那条 Glamsterdam 延期仍在媒体转述里）、<code>hf</code>（跨天去重）。这几条空都不是故障。</p>
<p><strong>来源分布（fresh）</strong>：hackernews 25、ithome 25、lobsters 15、panews 15、producthunt 14、coindesk 12、theblock 11、coingecko-trending 10、v2ex 9、idcspy 7、coinmarketcap-search 6、github-trending 5、coingecko-markets 3、steam 2、appstore-ios 2、appinn 1、binance-ann 1、exchange-status 1、crypto-release 1、fng-index 1、lowendbox 1、ruanyifeng-weekly 1。</p>
<p><strong>通道判据</strong>：境内（IT之家、美国主机侦探、v2ex、小众软件、iTunes lookup）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、Steam、GitHub API、Statuspage）同时全绿，所以代理节点这一轮工作正常。少数站点的 403／307 属于站点侧反爬，不是通道故障，已在对应条目里分别写明。</p>
<p><strong>四步口径</strong>：一、取数只用有机器可读通道且能判新旧的来源，行情类靠「id 带当天日期」避免整批被去重吃掉；二、验真——优惠、限免、免费额度三类必须回官方页或官方接口二次确认价格与截止时间，App Store 因为 Apple 不公布促销结束时间，那一栏写「不公布」而不是编一个日期，且一律认 trackId 不认名字（国区会改名，按名字搜会认错 app、把别人的免费价安到这条上）；三、分级——🔥 只给距截止 ≤3 小时或影响在用服务与在用资产可得性的，⭐ 给已核实且本周内能直接用的，👀 给未核实或门槛高的，❌ 给旧闻重推、软文与要连钱包才能领的东西；四、边界——只收集、验证、报告，不注册、不绑卡、不代领券、不下单，兑换码型福利不转载兑换码，币圈不连钱包、不签名、不导私钥、不给买卖建议与目标价，产物里不出现钱包地址、私钥、助记词与带返利参数的邀请链接。</p>
</details>
