---
title: "资讯雷达 2026-10-26｜Steam 赛博朋克 2077 明晨收口、Epic 周免两款复查、App Store 三条本体限免核到免费价"
author: OxYGC
date: 2026-10-26 06:40:00 +0800
permalink: /posts/info-radar-2026-10-26/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Steam优惠, Epic, AppStore, AI动态, 币圈]
description: "2026-10-26 一轮 25 个来源的资讯雷达：Steam 赛博朋克 2077 明晨收口、Epic 两款周免与两款折扣复查、App Store 国区三条本体限免逐条回 iTunes 核到免费价、开发侧四篇一手长文，全部标注核实时间与截止时间。"
---

这一轮跑了 25 个来源，取回 316 条，两天窗口加跨天去重之后留下 136 条，0 个来源报错。先把结论说完：<strong>本轮没有命中 🔥 紧急门槛的条目</strong>。最近的硬截止是 Steam 那批 10 月 27 日 02:00（北京时间）收口的折扣，距取数时刻约 20 小时，没进「距截止 ≤3 小时」那一档；没有任何一条影响在用的域名、VPS 或在用 API 的免费额度。和昨天相比有四处变化。其一是 Epic 那两款周免仍在窗口内，06:36 重读官方端点 <code>discountPrice</code> 依旧是 0、截止时间一字未动，所以本篇给的是<strong>效期复查</strong>而不是新消息。其二是 App Store 侧今天有三条本体限免逐条回 iTunes 国区核到了免费下载价（昨天只有一条）。其三是 Steam 的《赛博朋克 2077》本体与《往日之影》进入收口前一天，而且发现脚本把这个字段的时区读错了——官方给的是 UTC 秒，脚本按北京时间打印，实际截止晚 8 小时，本档已按官方值换算修正。其四是币圈这边 Coinbase 与 Kraken 两家状态页同时挂着 <code>minor</code>，昨天它也在观察段，今天仍在观察段，理由不变：雷达没有「你把资产挂在这两家」的证据，按门槛不能升紧急。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:14px 16px;background:#fbfcfd;">

| 时点 | 条目 | 价格 | 去哪 |
| --- | --- | --- | --- |
| <span style="color:#c0392b;font-weight:700;">10-27 02:00 截止，剩约 20 小时</span> | Steam《赛博朋克 2077》本体 +《往日之影》 | <span style="color:#1a7f37;">各 ¥89.40</span>（原 ¥298 / ¥149） | [Steam 商店页](https://store.steampowered.com/app/1091500/?l=schinese) |
| <span style="color:#c0392b;font-weight:700;">10-29 23:00 截止，剩约 3 天</span> | Epic 本批周免两款（《Sker Ritual》《Home》）效期复查 | <span style="color:#1a7f37;">0 元</span>（原 ¥78 / ¥15） | [Epic 免费游戏页](https://store.epicgames.com/free-games?lang=zh-CN) |
| <span style="color:#6b7280;font-weight:700;">Apple 不公布限免截止时间</span> | App Store 国区三条本体限免（day.txt / iMenuBar Lite / 休息日） | <span style="color:#1a7f37;">下载 0 元</span> | [apps.apple.com/cn/app/id6805007155](https://apps.apple.com/cn/app/id6805007155) |
| <span style="color:#6b7280;font-weight:700;">无截止，需要你自己核对</span> | Coinbase / Kraken 状态页 <code>minor</code>（服务部分降级） | <span style="color:#6b7280;">—</span> | [status.coinbase.com](https://status.coinbase.com) ｜ [status.kraken.com](https://status.kraken.com) |

</div>

## 值得看（16）

<details>
<summary><strong>Steam《赛博朋克 2077》（app 1091500） -70%</strong> ｜ <span style="color:#1a7f37;">¥89.40</span>（原 ¥298.00） ｜ <span style="color:#c0392b;">截止 10-27 02:00，剩约 20 小时</span></summary>
<p>本轮绝对降价额最大、也是收口最早的一档。判据来自官方 <code>featuredcategories?cc=cn&amp;l=schinese</code> 与商品页两处读到的 <code>discount_expiration = 1793037600</code>，那是 <strong>UTC 秒</strong>，即 <code>2026-10-26T18:00:00Z</code>，换算北京时间 10 月 27 日 02:00。</p>
<p>这里有一个取数侧的坑要写出来：雷达脚本把这个字段按本地时间渲染，输出成「今天 18:00 截止」，比真实截止早了 8 小时。本档按官方值手工换算修正，脚本那处口径建议在后续版本改掉——<strong>凡是照接口原文抄时间的条目，都值得对一眼时区</strong>。</p>
<p>区域参数必须显式带 <code>cc=cn</code>：不带它会按出口 IP 返回别的货币定价，数字对不上不是改价而是区域差异。</p>
<p>核实于 2026-10-26 06:38（Steam 官方接口 + 商品页双读） · 直链 <a href="https://store.steampowered.com/app/1091500/?l=schinese">store.steampowered.com/app/1091500</a></p>
</details>

<details>
<summary><strong>Steam《赛博朋克 2077：往日之影》（app 2138330） -40%</strong> ｜ <span style="color:#1a7f37;">¥89.40</span>（原 ¥149.00） ｜ <span style="color:#c0392b;">截止 10-27 02:00</span></summary>
<p>与本体同一批、同一截止时间，要动就一次判完，不必分两次看。折扣率上它比本体浅得多（-40% 对 -70%），但折后价恰好落在同一个数字上，所以判断依据应该是「要不要连着 DLC 一起补」，而不是比谁打折狠。</p>
<p>核实于 2026-10-26 06:38（Steam 官方接口） · 直链 <a href="https://store.steampowered.com/app/2138330/?l=schinese">store.steampowered.com/app/2138330</a></p>
</details>

<details>
<summary><strong>Steam《The Walking Dead: The Telltale Definitive Series》（app 1449690） -90%</strong> ｜ <span style="color:#1a7f37;">¥16.80</span>（原 ¥168.00） ｜ <span style="color:#c0392b;">截止 11-06 02:00</span></summary>
<p>本轮折扣率最高的一条，全季合集一次到位。它不进紧急是因为窗口还有十一天，且折扣率本身不构成价值——玩不玩剧情向章节制作品，只有你自己判得出来。</p>
<p>核实于 2026-10-26 06:38（Steam 官方接口） · 直链 <a href="https://store.steampowered.com/app/1449690/?l=schinese">store.steampowered.com/app/1449690</a></p>
</details>

<details>
<summary><strong>Steam《Resident Evil 4》（app 2050650） -75%</strong> ｜ <span style="color:#1a7f37;">¥49.50</span>（原 ¥198.00） ｜ <span style="color:#c0392b;">截止 11-04 02:00</span></summary>
<p>本轮第二深的折扣率，绝对价也低到不需要犹豫太久的档位。同一轮官方接口里还有 GTA V 增强版 ¥149.00→¥74.50（-50%）与《朋友，梭哈吧》-38%，均已核实但收在观察段的合并行里，不逐条单列。</p>
<p>核实于 2026-10-26 06:38（Steam 官方接口） · 直链 <a href="https://store.steampowered.com/app/2050650/?l=schinese">store.steampowered.com/app/2050650</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Sker Ritual（斯盖尔仪式）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥78.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00，剩约 3 天</span></summary>
<p>10-23 起连续几天都在报它，本轮取数没再列进新增，是因为 Epic 这一路的去重键是标题（<code>ident = title</code>）——同一款限免持续多天，只在第一次出现时报。这一条的价值不是「新消息」，而是<strong>复查</strong>：06:36 重读官方 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 端点，<code>price.totalPrice.discountPrice</code> 仍为 0，<code>originalPrice</code> 是 7800（接口单位是分），<code>appliedRules.endDate = 2026-10-29T15:00:00Z</code>，换算北京时间 23:00，与前几日一致。</p>
<p>另外注意 Epic 中文商店页有时把同一时刻渲染成次日 00:00，两处都是官方来源，按早的动手。领取即永久入库，不需要赶在截止前玩完。</p>
<p>核实于 2026-10-26 06:36（Epic 官方端点） · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure（归家）》效期复查</strong> ｜ <span style="color:#1a7f37;">0 元</span>（原 ¥15.00） ｜ <span style="color:#c0392b;">截止 10-29 23:00</span></summary>
<p>与上一条同一批、同一截止时间，一并领即可。本轮复查官方端点仍为 <code>discountPrice = 0</code>、<code>originalPrice = 1500</code>。这一批周免里只有这两款是真正的 0 元，其余是打折，不要混在一张卡里判。</p>
<p>这里补一个上一版判断的更正过程：Epic 接口里的 <code>discountPercentage</code> 对限免条目给出的值是 0，跟「打 0% 折」撞字面，一开始据此把它读成了非限免。最后是以 <code>price.totalPrice.discountPrice</code> 这个权威字段重新判的——<strong>遇到字段语义有歧义，回到那个专门表达业务的字段，别拿折扣率反推是否免费</strong>。</p>
<p>核实于 2026-10-26 06:36 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic《纪念碑谷（Monument Valley）》 -65%</strong> ｜ <span style="color:#1a7f37;">¥11.55</span>（原 ¥33.00） ｜ <span style="color:#c0392b;">截止 11-03 00:00</span></summary>
<p>移动端移植经典，绝对价本身低，属于「不需要纠结」的那一档。它是打折不是限免，截止时间来自官方 <code>appliedRules.endDate</code>，按北京时间算到 11 月 3 日 00:00。</p>
<p>核实于 2026-10-26 06:36（Epic 官方端点） · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic《Eternal Threads》 -80%</strong> ｜ <span style="color:#1a7f37;">¥12.40</span>（原 ¥62.00） ｜ <span style="color:#c0392b;">截止 11-03 00:00</span></summary>
<p>叙事解谜，本周折扣率最深的一条。与上一条同一批、同一截止时间。同一页里的《Sorry We're Closed》¥78.00→¥54.60 折扣率浅，收进观察段的合并行不单独列卡。</p>
<p>核实于 2026-10-26 06:36 · 直链 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 国区《day.txt》（id 6805007155）本体限免</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>纯文本日记工具，汇总频道 10-24 08:11 UTC 的播报口径是「本体限免」，回 iTunes lookup 用播报正文里那个 trackId 核到国区 <code>formattedPrice = 免费</code>、<code>price = 0.0</code>，商店名与播报名一致（day.txt），开发者署名 Zbigniew Ledwon，最低系统 17.0。</p>
<p>三处口径要说清：其一，核到现价 0 只等于「今天下载不花钱」，lookup 接口分不出「本就免费」与「促销中」，所以不写「限免仍在」；其二，Apple 不公布促销结束时间，那一栏只能这么空着，编一个日期出来反而更糟；其三，国区会给应用改名，所以一律认 id 不认名字——按名字搜会认错另一个 app，把别人的免费价安到这条上。</p>
<p>核实于 2026-10-26 06:31（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id6805007155">apps.apple.com/cn/app/id6805007155</a></p>
</details>

<details>
<summary><strong>App Store 国区《iMenuBar Lite：菜单栏图标隐藏》（id 6805884598）本体限免</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>Mac 菜单栏整理小工具（<code>mt=12</code>，是 Mac 应用），汇总频道 10-25 14:03 UTC 播报「本体限免」，回 iTunes lookup 用播报正文里的 trackId 核到国区现价<strong>免费</strong>、<code>price = 0.0</code>，商店名与播报名一致，开发者署名「耀 陈」，最低系统 26.0。</p>
<p>这一条在取数时差点带着一个错误的 id 出门：转储被截断时我按记忆拼了另一个 id 上去，回原始 NDJSON 重读才确认是 6805884598。这正好是「认 id 不认名字」这条口径的反面教材——<strong>id 本身也必须从原始记录里取，不能从印象里取</strong>。</p>
<p>核实于 2026-10-26 06:31（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id6805884598">apps.apple.com/cn/app/id6805884598</a></p>
</details>

<details>
<summary><strong>App Store 国区《休息日 / Off Day》（id 6501973975）本体限免</strong> ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ Apple 不公布限免截止时间</summary>
<p>休息提醒类工具，10-25 14:03 UTC 播报「本体限免」，回 iTunes lookup 用播报正文里的 trackId 核到国区现价<strong>免费</strong>，开发者署名 ZIZICICI LIMITED，最低系统 16.0。</p>
<p>注意这条是「改名」口径的实例：播报名写的是 <em>Off Day</em>，App Store 国区商店名实际是<strong>休息日</strong>，直链 slug 也是中文。如果按名字去搜国区，很容易认错成另一个同名 app，所以核价只认 id。</p>
<p>核实于 2026-10-26 06:31（iTunes 国区 lookup） · 直链 <a href="https://apps.apple.com/cn/app/id6501973975">apps.apple.com/cn/app/id6501973975</a></p>
</details>

<details>
<summary><strong>阮一峰《科技爱好者周刊》第 416 期：编程已经面目全非</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>本期标题就是主题——AI 把写代码这件事的形态改掉了，周刊按惯例是周六晚更新，RSS 时间戳落在 10-25。对你的写作方向属于「同类选题的现成目录」，可以直接看它这一期选了哪些条目、怎么配注释，比单看某一条更有参照价值。</p>
<p>核实于 2026-10-26 06:31（周刊 RSS 时间戳） · 直链 <a href="https://www.ruanyifeng.com/blog/2026/10/weekly-issue-416.html">ruanyifeng.com/blog/2026/10/weekly-issue-416.html</a></p>
</details>

<details>
<summary><strong>danluu《We should be more ambitious with the software we build》</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>本轮讨论量最大的一篇工程观点文：Hacker News 730 分 / 671 评，10-24 21:47 UTC 上榜。danluu 的长文一贯是「拿数据和历史案例把一句话论证到底」的写法，这篇的核心主张是现在大家太满足于做小东西，论据落在软件工业史上那些「本来能做成但没做」的例子上。</p>
<p>它值得读的第二层原因是可复用：这类「观点 + 反直觉证据 + 个人经历」的结构，和纯教程类文章在选题上是互补的。</p>
<p>核实于 2026-10-26 06:31（HN Algolia 官方接口） · 直链 <a href="https://danluu.com/ambitious/">danluu.com/ambitious</a></p>
</details>

<details>
<summary><strong>Cerebras：万亿参数前沿模型的部署方式</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>厂商自己写的一手工程博客（不是媒体转述），讲万亿参数前沿模型怎么落到实际推理服务上：权重摆放、显存与互联的约束、请求调度与吞吐的取舍。本轮 Hacker News 344 分 / 127 评，10-25 01:33 UTC 上榜。</p>
<p>对后端读者的价值点在推理基础设施这一层——它给的是「一家做硬件的厂怎么描述自己推理栈的工程约束」，可以拿来和常见的 GPU 集群推理方案对照着读，看两边把瓶颈划在哪里。</p>
<p>核实于 2026-10-26 06:31（HN Algolia 官方接口 + 官方博客 URL） · 直链 <a href="https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras">cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras</a></p>
</details>

<details>
<summary><strong>Goose 编程语言（aardappel）</strong> ｜ <span style="color:#6b7280;">0 元</span> ｜ 无截止</summary>
<p>双通道互证而不是单点热帖：Hacker News 558 分 / 345 评（10-24 19:06 UTC），lobsters 同期 8 赞 / 2 评（10-25 15:10 -05:00）。作者此前做过 C++ 与工具链方向的工作，这次是一个自述极简的语言实现，读点在于他把哪些语言特性判定为「不值得为通用性付出代价」并明确删掉。</p>
<p>雷达这一轮对 trending 与热帖的入选口径没有放宽：热度只是发现入口，进「值得」要靠「读了作者自述与用途，能判断它对你手上的后端、Agent 与工具链选题有接口」。</p>
<p>核实于 2026-10-26 06:31（HN Algolia 官方接口 + lobsters 官方 RSS） · 直链 <a href="https://aardappel.github.io/goose/">aardappel.github.io/goose</a></p>
</details>

<details>
<summary><strong>anza-xyz/agave 发版 v4.4.0-rc.0</strong> ｜ <span style="color:#6b7280;">0 元（项目方一手）</span> ｜ 无截止</summary>
<p>Solana 核心客户端的发版，来源是项目方自己的 GitHub releases，不是媒体转述。官方 API 给 <code>published_at = 2026-10-24T07:27:33Z</code>（北京时间 10 月 24 日 15:27），版本形态是 <code>rc</code> 而非正式版，这点必须写清楚，不能当成可用稳定版引用。它与昨天报的是同一个 release，本轮仍在两天窗口内所以又被带到面前，这一条的作用同样是<strong>复查</strong>。</p>
<p>对写公链与客户端类内容的人来说，这条的意义是「引用的版本号要跟着改，而且要标明是 RC」；自己是否升级取决于是否真的在跑节点，雷达不给操作建议。</p>
<p>核实于 2026-10-26 06:31（GitHub 官方 releases API） · 直链 <a href="https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0">anza-xyz/agave releases/tag/v4.4.0-rc.0</a></p>
</details>

## 观察（12）、币圈那一轮与方法

<details>
<summary><strong>观察 12 条（每条末尾写存疑原因）</strong></summary>
<table>
<tr><th>条目</th><th>为什么只放观察</th></tr>
<tr><td>交易所服务状态：Coinbase 与 Kraken 两家 Statuspage <code>indicator=minor</code>（Partially Degraded Service）。Coinbase 页面时间 10-25 16:21 +08，Kraken 10-26 06:19 +08；06:46 二次回读两家 <code>api/v2/status.json</code> 仍是 minor（<a href="https://status.coinbase.com">status.coinbase.com</a> ｜ <a href="https://status.kraken.com">status.kraken.com</a>）</td><td>要不要紧取决于有没有把资产或正在走的充提挂在这两家，雷达没有这项证据。按币圈门槛，只有<strong>直接影响在用资产可得性</strong>（下架、清退、充提暂停、服务降级）才升紧急，而这一条的判断卡在「在用」两个字上，所以昨天在观察、今天也留在观察，不做任何链上或交易所侧动作。</td></tr>
<tr><td>币安杠杆「小额负债账户常规清退」：负债小于 1 USD（或等值其他资产）的账户将于 <strong>2026-10-27 00:00（UTC）= 北京时间 08:00</strong> 起被清理，公告发布于 10-21（<a href="https://www.binance.com/zh-CN/support/announcements">binance.com 公告中心</a>）</td><td>已回公告原文核对生效时间，但它只影响「在币安开过杠杆且留了零头负债」的人，雷达没有你在使用币安杠杆的证据。若你确实有敞口，请自己开账户页核对负债金额，这条不代操作、不代为平仓。</td></tr>
<tr><td>币安矿池服务关闭公告（发布 10-13，属旧闻重推）：2026-11-10 07:00 UTC 起断开 Stratum 连接，2026-11-24 07:00 UTC 起移除数据</td><td>仅影响仍在用币安矿池挖矿的人；公告本身是旧闻，日期已在两天窗口边缘。若在用请自己复查切换时间点，雷达不代为变更任何配置。</td></tr>
<tr><td>CoinDCX 确认因退役钱包损失约 1,600 万美元（The Block / CoinDesk 转述）</td><td>只见到媒体转述，未取得交易所一手公告原文，无法核对金额、涉及链与合约地址。链上资产只按代币符号认会认错，必须回到一手材料的地址栏才算核实，故降为观察。</td></tr>
<tr><td>Keystone 客户称硬件钱包厂商数据泄露（PANews 10-25 转述）</td><td>来源是「客户说法 + 媒体」，未见项目方 security advisory。安全事件按口径只认项目方 advisory / 官方博客 / 交易所公告三方之一，媒体单独出现时一律降级。</td></tr>
<tr><td>月之暗面就 Kimi K3.1 Pro 限流致歉并为订阅用户重置 25% 月度额度（PANews 中文转述）</td><td>免费额度类一律要官方口径才进「值得」。本轮只见到媒体转述，未回到月之暗面官方公告核对「25%」「月度」「适用套餐」这几个数字，价格与额度均未核实。需要用到额度的话请自己开官方订阅页核对，雷达不代领、不代注册。</td></tr>
<tr><td>币安上币与费率类公告：RWUSD 零手续费促销、HYPE 上线、PREDICTUSDT 永续合约、tick size 10-29 调整、保证金分层 10-30 调整（18 条公告里筛出）</td><td>均为新产品与规则变更，不影响既有资产的可得性，条款也未逐条回原文核对生效时间与合约地址；日期只写在标题里是这批公告的一贯形态，容易读错，所以整体留在观察。</td></tr>
<tr><td>iOS 内购限免一批：FreePlay（id 6754824912）、LiveToFrame（id 6757419019）、Artino（id 6774119167）、框语-相机水印大师（id 6755989422）、invsi</td><td>iTunes 核到的只是下载价为 0，而内购解锁价根本不体现在下载价上，这类只能算频道转述；Apple 也不公布限免截止时间。国区常改名，已按 id 对齐商店名。</td></tr>
<tr><td>iOS《OneFocus: Deep Work》内购限免</td><td>按播报正文里的 id 6790143964 在 iTunes 国区查不到上架记录，价格未核实——查不到 id 就只能写「未核实」，不能按名字换一条近似记录顶上。</td></tr>
<tr><td>iOS《Burning Parchment: Bedtime》兑换码型限免（<a href="https://t.me/TossTF/3756">t.me/TossTF/3756</a>）</td><td>兑换码不转载、不拼进任何产物、不代兑换，只留频道原帖让你自己取；本轮未走 iTunes 核价，价格未核实。Apple 不公布限免截止时间。</td></tr>
<tr><td>iOS《Bothie》限免（<a href="https://t.me/TossTF/3757">t.me/TossTF/3757</a>）</td><td>播报正文里没有 App Store 直链，拿不到 trackId 就无法核价，价格未核实；也不排除已下架。Apple 不公布限免截止时间。</td></tr>
<tr><td>行情与热度快照（06:31，CoinGecko / CoinMarketCap / alternative.me）：BTC $80,498（+0.1%）、ETH $2,344（+0.2%）；CoinGecko 热搜前列 QNT / HYPE / ENA；恐惧贪婪指数 54（Neutral）；另有本轮官方接口已核但未单列的折扣：Steam GTA V 增强版 ¥149.00→¥74.50、《朋友，梭哈吧》-38%，Epic《Sorry We're Closed》¥78.00→¥54.60</td><td>行情、涨跌幅、热搜、情绪指数是某一刻的数字而非可执行信息，按口径一律不给「值得」，也不构成任何操作依据；后三款是折扣率或适配度不足以单列一张卡片，数字已核实，列在这里是为了「会过期或要复查」这件事可追溯。</td></tr>
</table>
<p><strong>过滤（不进正文，只计数）</strong>：币圈侧的喊单、目标价、荐币与要求连钱包/签名/领空投的条目本轮没有出现值得判定的形态，Product Hunt 15 条与 IT之家 25 条多为产品通稿与硬件新品，与发文选题没有直接接口，一律不进正文；v2ex 9 条以闲聊与职业困惑为主。全轮 <code>errors=0</code>，没有一条源被静默跳过。</p>
</details>

<details>
<summary><strong>币圈这一轮怎么取的、来源健康度与四步口径</strong></summary>
<p><strong>取数结果</strong>：全量一轮 <code>SUMMARY fetched=316 fresh=136 sources=25 errors=0</code>（带 <code>--seen/--append</code> 跨天去重），整轮没有任何 <code>ERR source=</code> 行。为了把被终端截断的正文头部找回来，又按赛道分三组重取了一次（这三次<strong>不带</strong> <code>--seen/--append</code>，因此不污染去重库，数字是「两天窗内条数」，与上面那个 fresh 不是同一口径）：<code>deal fetched=57 fresh=29 sources=6 errors=0</code>、<code>crypto fetched=130 fresh=70 sources=11 errors=0</code>、<code>news fetched=127 fresh=106 sources=8 errors=0</code>，三组同样 <code>errors=0</code>。</p>
<p><strong>来源分布（分组重取，窗内条数）</strong>：hackernews 25、ithome 25、lobsters 19、binance-ann 18、panews 15、producthunt 15、appstore-ios 11、coindesk 11、github-trending 11、coingecko-trending 10、steam 9、v2ex 9、coinmarketcap-search 6、epic-store 5、theblock 4、coingecko-markets 3、lowendbox 2、idcspy 2、ruanyifeng-weekly 2、exchange-status 1、fng-index 1、crypto-release 1。两个本轮 0 条且<strong>不是故障</strong>的源：<code>appinn</code> 打印 <code>INFO source=appinn empty=</code>（业务上本来就常没货，挂了 <code>allow_empty</code>，这次是没有限免帖）、<code>ethblog</code> 在两天窗口内确实没有新文。</p>
<p><strong>一处已发现的脚本口径问题</strong>：Steam 的 <code>discount_expiration</code> 是 UTC 秒，脚本按本地时间渲染，导致所有 Steam 截止时间显示得比真实早 8 小时。本档已逐条按官方值换算修正（《赛博朋克 2077》本体与 DLC 的真实收口是北京时间 10-27 02:00），脚本那处留给后续改动，并已在本地存档的「来源健康度」里标为<strong>需注意</strong>而不是正常。</p>
<p><strong>通道判据</strong>：境内（IT之家、美国主机侦探、v2ex、小众软件、iTunes lookup）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、GitHub API、Statuspage）同时全绿。Steam 商店页直连取不到（<code>http=000</code>），走本机代理节点才拿到 200，属于「本机对境外站没有直连出口」的既有形态，不是站点改版；Coinbase 状态页第一次直连返回空、走代理后正常，同理。X 一侧本轮没有需要验真的条目，因此没有动用登录窗口。</p>
<p><strong>四步口径</strong>：一、取数只用有机器可读通道且能判新旧的来源，行情类靠「id 带当天日期」避免整批被去重吃掉；二、验真——优惠、限免、免费额度三类必须回官方页或官方接口二次确认价格与截止时间，App Store 因为 Apple 不公布促销结束时间，那一栏写「不公布」而不是编一个日期，且一律认 trackId 不认名字（国区会改名，按名字搜会认错 app、把别人的免费价安到这条上），内购限免与兑换码型只算转述；三、分级——🔥 只给距截止 ≤3 小时或影响在用服务与在用资产可得性的，⭐ 给已核实且本周内能直接用的，👀 给未核实或门槛高的，❌ 给旧闻重推、软文与要连钱包才能领的东西；四、边界——只收集、验证、报告，不注册、不绑卡、不代领券、不下单，兑换码型福利不转载兑换码，币圈不连钱包、不签名、不导私钥、不给买卖建议与目标价，产物里不出现钱包地址、私钥、助记词与带返利参数的邀请链接。</p>
</details>
