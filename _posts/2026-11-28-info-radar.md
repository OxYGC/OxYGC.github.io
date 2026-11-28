---
title: "资讯雷达 2026-11-28｜Epic《Bread and Fred》0 元进入最后一周、Steam 黑五 3A 折扣、GPT 6.2 Astra 与 Agent Skills 屠榜"
author: OxYGC
date: 2026-11-28 12:05:00 +0800
last_modified_at: 2026-11-28 12:05:00 +0800
permalink: /posts/info-radar-2026-11-28/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam黑五, 比特币, GitHub趋势, GPT-6.2, Agent Skills]
description: "2026-11-28 当天唯一一篇（午间 12:05 取数）：Epic《Bread and Fred》¥47.00 → 0 元，官方接口 endDate 回读为北京时间 12-04 00:00；同接口《Eternal Threads》-80%（¥62.00 → ¥12.40）至 12-01 23:00；《火之石》原价即 0，不按新增限免计。Steam 黑五 3A 全部经官方 featuredcategories 核价（RDR2 -75%、双人成行 -80%、赛博朋克 2077 -70%、SILENT HILL f -72%），接口不返回截止，收口以商店页为准。HN 头条 GPT 6.2 Astra 解历史谜题 368 分，其次 Convex skill 未经告知上传用户创意 250 分；GitHub Trending 被 Agent Skills 类仓库占据，Claude-BugHunter 单日 +1,608。币圈 BTC 12:05 Gate.io 快照 60,061.6（-2.14%），ETH 1,667.2（-3.50%），恐惧贪婪 10（Extreme Fear）。"
---

这一轮是 2026-11-28 当天的第一跑，取数窗口在午间 12:05 前后（北京时间）。按「一天一份」的规矩，今天只落这一个文件；后续若有增补，改这一篇而不新开。先说结论：**Epic 本周免费还是《Bread and Fred》，原价 ¥47.00 → 0 元，官方接口的 `endDate` 折算到北京时间是 12-04 00:00，已经进入最后一周**；同一次接口返回里另有一款《Eternal Threads》在打 -80%（¥62.00 → ¥12.40），截止 12-01 23:00，这是「折扣」不是「限免」，两者别混。Steam 黑五仍在进行，`featuredcategories` 的 `specials` 档给到《RDR2》-75%、《双人成行》-80%、《赛博朋克 2077》-70% 等，但该接口不返回截止时间，所以收口一律以商店页倒下计时为准。

需要如实说明本轮的取数范围：**实际取到数据的是 Epic 官方促销接口、Steam `featuredcategories`、Hacker News Firebase、GitHub Trending、Gate.io 行情、alternative.me 恐惧贪婪指数、IT之家 RSS 这几路**；CoinGecko 与 V2EX 本轮 SSL 握手失败（`SSL_ERROR_SYSCALL`），所以行情改走 Gate.io 单源、并明确标注时点。GitHub REST API 因未鉴权触发限流（`API rate limit exceeded`），趋势数据改用 GitHub Trending 页面抓取，仓库名与「今日新增 star」都可回页面核对。没有取到的源就不写数，不拿昨天的值充今天。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮会过期、或需要你自己动手的条目</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">12-04 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《Bread and Fred》0 元领取永久入库（本周免费，最后一周）</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/p/bread-and-fred-1db362">Epic 商店页</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;font-weight:700;">12-01 23:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《Eternal Threads》-80%（折扣，非限免）</td>
<td style="padding:9px 8px 9px 0;">¥62.00 → ¥12.40</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/p/eternal-threads-197169">Epic 商店页</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;font-weight:700;">商店页为准</td>
<td style="padding:9px 8px 9px 0;">Steam 黑五 3A：《RDR2》-75%、《双人成行》-80%、《赛博朋克 2077》-70%、《SILENT HILL f》-72%</td>
<td style="padding:9px 8px 9px 0;">¥69.75 / ¥39.60 / ¥89.40 / ¥83.44</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/specials">Steam 特卖页</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">需要自查</td>
<td style="padding:9px 8px 9px 0;">Convex skill 未经告知把用户创意发往远端（用过该插件的开发者）</td>
<td style="padding:9px 8px 9px 0;">—</td>
<td style="padding:9px 0 9px 0;">见下方「值得看」，以 issue 原文为准</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格均为 2026-11-28 12:05 前后实测：Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN&amp;allowCountries=CN</code>，Steam <code>featuredcategories?cc=cn&amp;l=zh</code>（分位转元）。Epic <code>endDate</code> 为 UTC，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（6）

<details open>
<summary><strong>Epic《Bread and Fred》0 元领取永久入库，原价 ¥47.00，最后一周</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥47.00 → 0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 12-04 00:00</span></summary>
<p>Epic 官方促销接口在 2026-11-28 12:05 前后返回：<code>title=Bread and Fred</code>、<code>originalPrice=4700</code>（分）、<code>discountPrice=0</code>、<code>endDate=2026-12-03T16:00:00Z</code>，即 <strong>北京时间 12-04 00:00 截止</strong>。这是「免费领取、永久入库」，不是限时试玩。领取入口只有官方商店页，登录、下单、领取都由你本人完成；本站不代领、不绑卡。</p>
<p><strong>怎么读</strong>：Epic 每周四 00:00（北京时间）换榜，本周这档已经进入最后一周，错过不能补领。领取前确认账号区域与商店币种，避免把打折页当成 0 元页。</p>
<p><a href="https://store.epicgames.com/zh-CN/p/bread-and-fred-1db362">官方领取页</a> · 核实于 2026-11-28 12:05（Epic 官方接口）</p>
</details>

<details open>
<summary><strong>Epic《Eternal Threads》-80%，¥62.00 → ¥12.40</strong> ｜ <span style="color:#1a7f37;font-weight:700;">-80% 折扣</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 12-01 23:00</span></summary>
<p>同一次 Epic 接口返回里，<code>Eternal Threads</code> 的 <code>originalPrice=6200</code>、<code>discountPrice=1240</code>，即 -80% 到 <strong>¥12.40</strong>；<code>promotionalOffers[].startDate=2026-11-27T16:00:00Z</code>、<code>endDate=2026-12-01T15:00:00Z</code>，折到北京时间是 <strong>12-01 23:00 截止</strong>。这是一款时间循环解谜叙事游戏，折扣而非限免，12 元档属于「补票位」，不是历史最低的抄底价。</p>
<p><strong>怎么读</strong>：别把它和本周 0 元的《Bread and Fred》混为一谈——一个是免费入库、一个是付费折扣。买之前回商店页确认版本与 DLC，Epic 商店在不同区服的价格与文案可能微调。</p>
<p><a href="https://store.epicgames.com/zh-CN/p/eternal-threads-197169">Epic 商店页</a> · 核实于 2026-11-28 12:05（Epic 官方接口）</p>
</details>

<details open>
<summary><strong>Steam 黑五 3A 折扣：《RDR2》-75%、《双人成行》-80%、《赛博朋克 2077》-70%、《SILENT HILL f》-72%</strong> ｜ <span style="color:#1a7f37;font-weight:700;">官方 featuredcategories</span> ｜ <span style="color:#6b7280;font-weight:700;">截止以商店页为准</span></summary>
<p>Steam 官方 <code>featuredcategories?cc=cn&amp;l=zh</code> 在 12:05 前后的 <code>specials</code> 档返回（分位已换算成人民币）：<code>Red Dead Redemption 2</code> 75% → <strong>¥69.75</strong>；<code>It Takes Two</code> 80% → <strong>¥39.60</strong>；<code>Cyberpunk 2077</code> 70% → <strong>¥89.40</strong>；<code>SILENT HILL f</code> 72% → <strong>¥83.44</strong>；<code>Grand Theft Auto V Enhanced</code> 56% → <strong>¥98.56</strong>；<code>Baldur's Gate 3</code> 30% → <strong>¥187.60</strong>；<code>Split Fiction</code> 40% → <strong>¥118.80</strong>；<code>SILENT HILL 2 &amp; SILENT HILL f</code> 双包 65% → <strong>¥156.80</strong>；<code>007 First Light</code> 50% → <strong>¥149.00</strong>。</p>
<p><strong>怎么读</strong>：这是官方接口给到的当前价，但接口<strong>不返回截止时间</strong>，所以本条目只承诺「价格来自官方接口、时刻已标注」，不承诺具体收口时点，买前请回商店页看倒计时。折扣价不等于历史最低；新手最容易踩的是「增强版 / 终极版 / 含 DLC」的价差，《赛博朋克 2077》本体与《往日之影》扩展是分开计价的，别买错。</p>
<p><a href="https://store.steampowered.com/specials">Steam 特卖页</a> · 核实于 2026-11-28 12:05（Steam 官方接口）</p>
</details>

<details>
<summary><strong>HN 头条：GPT 6.2 Astra 破解一桩历史谜题</strong> ｜ <span style="color:#6b7280;">368 分 / 232 评</span> ｜ 无截止</summary>
<p>Hacker News 当前头条是 <code>GPT 6.2 Astra Solves a Historical Mystery</code>，发在 generativehistory.substack.com，<strong>368 分、232 条评论</strong>，是今天讨论度最高的一条。它的价值不在「AI 又赢了」，而在于把模型推理用在史料交叉验证上：如果结论可复现、引文可回溯，它就是一个可讨论的方法样本；如果只是叙述流畅但证据链断，community 的评论里通常会第一时间拆穿。</p>
<p><strong>怎么读</strong>：把它当成「一条待核的结论」而不是定论。历史类结论要看三件事——原始文献是否可查、推理链是否自洽、是否有独立第三方复核。前两条文章里能给，第三条得等学术界回应。</p>
<p><a href="https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical">原文（Substack）</a> · 核实于 2026-11-28 12:05（HN Firebase）</p>
</details>

<details>
<summary><strong>Convex skill 被指未经告知把用户创意发往远端服务器</strong> ｜ <span style="color:#6b7280;">250 分 / 79 评</span> ｜ 用过该插件需自查</summary>
<p>HN 第二名是一条 GitHub issue：<code>Convex skills send the user's app idea to a remote server without telling them</code>，位于 <code>convex/convex-backend-skill</code> 仓库，<strong>250 分、79 条评论</strong>。核心指控是某个 Agent Skill 在用户不知情的情况下，把「用户的应用创意」上传到远端。这类问题的严重性不在单次调用，而在它发生在一个被当作「本地工具」使用的 skill 里——用户默认数据不出本机，实际却出站了。</p>
<p><strong>怎么读 / 自查</strong>：如果你装过这类第三方 Agent Skill，动作很具体——翻一遍 skill 的源码或 <code>SKILL.md</code> 里有没有对外 HTTP 请求、看网络请求日志里有没有意料之外的出站域名、确认厂商是否在文档里披露了数据流向。issue 原文是判断依据，不要只看转述。</p>
<p><a href="https://github.com/convex/convex-backend-skill/issues/64">issue 原文</a> · 核实于 2026-11-28 12:05（HN Firebase）</p>
</details>

<details>
<summary><strong>GitHub Trending：Agent Skills 类仓库屠榜，Claude-BugHunter 单日 +1,608</strong> ｜ <span style="color:#6b7280;">开发者动态</span> ｜ 无截止</summary>
<p>今日 GitHub Trending（daily）几乎被「Agent Skills / 插件 / 工作流」类仓库占满：<code>elementalsouls/Claude-BugHunter</code> 单日 <strong>+1,608</strong>（一套面向漏洞挖掘与红队的 Claude Code skill 包，含 85 个 skill、16 个 slash command）；<code>obra/superpowers</code> <strong>+922</strong>（agentic skills 框架与方法论）；<code>XiaoYouChR/Ghost-Downloader-3</code> <strong>+836</strong>；<code>firecrawl/firecrawl</code> <strong>+822</strong>；<code>cathrynlavery/diagram-design</code> <strong>+725</strong>；<code>zhouxiaoka/autoclip</code> <strong>+718</strong>；<code>mvanhorn/last30days-skill</code> <strong>+675</strong>；<code>HKUDS/CLI-Anything</code> <strong>+666</strong>；<code>jingyaogong/minimind</code> <strong>+660</strong>（两小时从 0 训 64M 大模型）。</p>
<p><strong>怎么读</strong>：趋势这一栏反映的是「注意力」不是「质量」。skill 类仓库尤其要看两点——维护者是否持续合并 PR、以及 skill 是否会访问外部服务（对照上一条 Convex 的教训）。红队 / 漏洞挖掘类工具请只在授权范围内使用。</p>
<p><a href="https://github.com/trending?since=daily">GitHub Trending</a> · 核实于 2026-11-28 12:05（Trending 页面抓取；API 本轮限流）</p>
</details>

## 观察（行情、IT之家与其余 HN）

<details>
<summary>币圈行情：BTC 60,061.6（-2.14%）、ETH 1,667.2（-3.50%）、恐惧贪婪 10</summary>
<p>Gate.io 在 12:05 前的现货快照：<strong>BTC/USDT 60,061.6</strong>，24h <code>-2.14%</code>，区间 58,800–62,225.9；<strong>ETH/USDT 1,667.2</strong>，24h <code>-3.50%</code>，区间 1,634.57–1,754.9。alternative.me 恐惧贪婪指数<strong>今天为 10（Extreme Fear）</strong>，昨天 12，继续处于极度恐惧区间。</p>
<p>这一栏按规矩只记为「数字」而非「信息」：单源 Gate.io 快照、时刻已标注，CoinGecko 本轮 SSL 失败未做交叉，所以不据此给任何买卖判断。真正的信息是「有没有影响你在用资产可得性的事件」，今天没有取到这一类官方公告。</p>
<p>来源：Gate.io / alternative.me，2026-11-28 12:05 快照</p>
</details>

<details>
<summary>IT之家当日要闻（节选）：OpenAI 实体设备、三星 One UI 9.5、Win12 无时间表</summary>
<table>
  <thead>
    <tr><th style="text-align:left;">标题</th><th style="text-align:left;">要点</th></tr>
  </thead>
  <tbody>
    <tr><td>“iPod 之父”法德尔：OpenAI 曾邀乔纳森·艾维打造实体 AI 设备</td><td>说法德尔称苹果「永远不会提供数据」，所以合作对象换成了 OpenAI；属人物访谈转述，未见 OpenAI 官方确认</td></tr>
    <tr><td>三星 One UI 9.5 Beta 曝光 36 项 AI 新功能</td><td>面向 Galaxy S27 系列，属爆料/曝光阶段，未到官方发布</td></tr>
    <tr><td>微软高管：暂无 Win12 发布时间表，首要任务是打磨 Win11</td><td>官方口径，可直接引用；短期不必等 Win12</td></tr>
    <tr><td>“GTA 6 终于来了”：微软 GitHub 力挺 PS5 转 PC 工具惹争议，官方火速删除推文</td><td>官方账号操作后删除，属公关事件；与 GTA 6 本身无直接关系</td></tr>
    <tr><td>影石 Ace Pro 3 被曝 12 月 1 日发布</td><td>1/1.1 英寸方形传感器、双 OLED 屏、2250mAh，属发布前爆料</td></tr>
  </tbody>
</table>
<p>IT之家这一栏都是「转述/爆料」为主的快讯，除微软 Win12 的官方表态外，其余未回原始信源二次核实，按观察处理。来源：IT之家 RSS，2026-11-28 11:22（UTC+8）前后更新。</p>
</details>

<details>
<summary>其余 HN 与技术条目（按分数排序，未逐条深挖）</summary>
<table>
  <thead>
    <tr><th style="text-align:left;">条目</th><th style="text-align:left;">分数 / 评论</th><th style="text-align:left;">备注</th></tr>
  </thead>
  <tbody>
    <tr><td>Google DeepCrossAttention：同等质量下最快 3 倍</td><td>195 / 65</td><td>Google Research 官方博客，属工程优化类</td></tr>
    <tr><td>Hera 任务拍到 DART 撞击小行星后的首批图像</td><td>195 / 58</td><td>Ars Technica，航天观测类</td></tr>
    <tr><td>Citroën 液压悬挂系统</td><td>147 / 50</td><td>经典工程资料站，科普向</td></tr>
    <tr><td>The Balatro Timeline</td><td>140 / 30</td><td>独立游戏开发复盘</td></tr>
    <tr><td>Atari Homebrew Awards 被取消</td><td>114 / 95</td><td>社区事件，讨论集中在评审机制</td></tr>
    <tr><td>9/UX：一个受 Macintosh 启发的 9front 桌面</td><td>89 / 22</td><td>极客玩具，非生产可用</td></tr>
    <tr><td>AT&amp;T Unix PC（3B1）虚拟机</td><td>68 / 13</td><td>复古计算</td></tr>
    <tr><td>78 美元的 DIY 音箱建模踏板套件</td><td>57 / 16</td><td>硬件 DIY</td></tr>
    <tr><td>Unkernel：编译成 WebAssembly 的真实 Linux 内核</td><td>14 / 3</td><td>刚上榜，样本太小</td></tr>
  </tbody>
</table>
<p>这些条目今天不构成「需要你立刻行动」的信息，所以只做登记不展开。来源：Hacker News Firebase，2026-11-28 12:05 抓取（部分条目首轮 SSL 失败后重试成功）。</p>
</details>

<details>
<summary>关于 Epic「火之石」与「非折扣条目」的说明</summary>
<p>同一次 Epic 接口里还有《火之石 – 放置点击英雄RPG》，但它的 <code>originalPrice=0</code>、<code>discountPrice=0</code>，属<strong>本来就免费或常年促销标记，不能当成「本周新增限免」</strong>，所以不单列。另外《Them's Fightin' Herds》<code>¥60.00</code>、《Model Builder: Complete Edition》<code>¥70.00</code>、《幽灵行者 2》<code>¥169.00</code> 等条目的 <code>originalPrice == discountPrice</code>，即当前没有折扣，不写入行动清单。判据只有一个：<code>discountPrice</code> 是否低于 <code>originalPrice</code>。</p>
<p>来源：Epic 官方促销接口，2026-11-28 12:05</p>
</details>

<details>
<summary>这一轮怎么跑的：口径与来源健康度</summary>
<p>四步口径不变：<strong>取数</strong> → <strong>验真</strong>（价格与截止回官方接口二次确认；Epic 以 <code>endDate</code> 的 UTC 值换算北京时间，Steam 以商店页倒计时为准）→ <strong>分级</strong>（值得 / 观察 / 过滤，宁严勿松）→ <strong>落盘与发布</strong>（本地 Markdown + Jekyll 发 Pages）。整个链路只收集与核实，不代注册、不绑卡、不领券、不下单；币圈侧不连钱包、不签名、不给买卖建议与目标价。</p>
<p><strong>来源健康度（本轮实况）</strong>：成功 7 路——Epic 官方接口、Steam <code>featuredcategories</code>、Hacker News Firebase、GitHub Trending 页面、Gate.io、alternative.me、IT之家 RSS。异常 2 路——CoinGecko 与 V2EX 本轮 <code>SSL_ERROR_SYSCALL</code> 握手失败，行情改走 Gate.io 单源并标注时点。受限 1 路——GitHub REST API 未鉴权触发限流，趋势数据改抓页面。没有取到的源不写数、不用旧值顶替。</p>
<p><strong>与昨天相比的变化</strong>：Epic 本周免费未换档（仍是《Bread and Fred》，进入最后一周），新增《Eternal Threads》-80%；Steam 黑五阵容基本延续，<code>SILENT HILL f</code> 由昨日双包拆出单列 -72%；HN 头条从 1Password 事件换成 GPT 6.2 Astra 的历史谜题；BTC 从昨日 12:09 的 61,420.8 回落到 60,061.6，恐惧贪婪由 12 降到 10。</p>
</details>
