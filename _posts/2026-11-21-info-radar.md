---
title: "资讯雷达 2026-11-21｜BTC 跌破 5.9 万、Epic《Mark of the Deep》限免、Steam 黑五战地双作 -95%"
author: OxYGC
date: 2026-11-21 00:20:00 +0800
permalink: /posts/info-radar-2026-11-21/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam黑五, 战地, 比特币, 黎曼猜想, GitHub趋势]
description: "2026-11-21 当天唯一一篇（午夜 00:03–00:12 取数 + 早间 06:30 全量复核）：Epic《Mark of the Deep》¥55→0 限免至 11-27 00:00（早间重查接口 endDate=2026-11-26T16:00Z，反向更正昨日误算的 08:00）；Steam 黑五 10 款全部经 appdetails 回读，战地 1 / 战地风云 5 双双 -95%；早间这一轮 25 个来源取回 305 条、新增 169 条、errors=1（appstore 首轮 URLError，单源重跑补齐 iOS 限免），补上 Kraken 充提与衍生品降级的复查（状态页 06:04 更新，仍未 resolve）、两条国区 iOS 本体免费（PDF编辑器 / 一生声迹，iTunes 按 id 核到现价 0），以及午夜档截稿后的 Tao 博客、OpenComputer、DreamCoder 三条一手材料。"
---

这一轮取数在 2026-11-21 00:03–00:12（北京时间）完成：20 个来源里 16 个取到数据、3 个被代理通道挡住、1 个（`panews`）RSS 已退化为 HTML 订阅页。`SUMMARY fetched=240 fresh=203 sources=20 errors=4`。异常集中在需要境外通道的行情接口：`bitfinex`、`binance`、`okx`、`coingecko`、`coinbase`、`kraken`、`bybit` 全部超时或被 SSL 拒绝，本轮改走 Gate.io 拿到一手价格；GitHub REST API 因共享出口 IP 触发限流（403），Trending 页面的 star 数与今日增量仍为现抓。**这是 2026-11-21 当天第一版；今天若再跑，只会在本文件内更新，不新增文件。**

结论先摆前面：**消费侧今天没有“今天到期”的硬截止，最近一个到期点是 11-24 02:00 的《我带过的最差一届》-35%；黑五主力档集中在 12-01 至 12-04，战地 1 与战地风云 5 双双 -95%，是本轮幅度最大的两张。** 免费游戏方面，Epic 本周只有《Mark of the Deep》一款 0 元，11-27 00:00 截止，接口同时给出下周《Bread and Fred》¥47→0。资讯面被两条 AI 消息占住 HN：Anthropic 数学家 Levent Alpoge 宣称与 Claude 合作给出黎曼猜想的“一般性证明”（PDF，尚未同行评审），以及 Anthropic 官方博客称 Claude 解决了黑洞物理的两个开放问题。币圈是明显的风险日：BTC 24 小时 -6.43% 跌破 6 万美元，ETH -8.1%，SOL -7.38%，恐惧贪婪指数 12（Extreme Fear），美国现货比特币 ETF 单日净流出 5.82 亿美元。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮真正会过期、或需要你自己动手的只有这几条</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:18%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-24 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《我带过的最差一届》-35%</td>
<td style="padding:9px 8px 9px 0;">¥28.00 → ¥18.20</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/5175310/">store.steampowered.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-27 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《Mark of the Deep》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-01 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《天国：拯救2》-67%</td>
<td style="padding:9px 8px 9px 0;">¥228.00 → ¥75.24</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1771300/">store.steampowered.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-02 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《对马岛之魂 导演剪辑版》-50%、《漫威蜘蛛侠 重制版》-60%</td>
<td style="padding:9px 8px 9px 0;">¥199.00 / ¥165.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2215430/">对马岛</a> · <a href="https://store.steampowered.com/app/1817070/">蜘蛛侠</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-03 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《FF7 重生》-85%、《FF7 重制版》-82%</td>
<td style="padding:9px 8px 9px 0;">¥37.20 / ¥35.64</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2909400/">FF7 重生</a> · <a href="https://store.steampowered.com/app/1462040/">重制版</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-04 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam 战地风云 5 / 战地 1 双双 -95%、《双人成行》-80%</td>
<td style="padding:9px 8px 9px 0;">¥11.40 / ¥9.90 / ¥39.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1238810/">BF5</a> · <a href="https://store.steampowered.com/app/1238840/">BF1</a> · <a href="https://store.steampowered.com/app/1426210/">双人成行</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-21 00:03–00:08 官方接口实测：Epic <code>freeGamesPromotions</code>、Steam <code>featuredcategories</code> 与逐款 <code>appdetails</code>。Steam 的 <code>discount_expiration</code> 是 epoch 时间，这里已换算成北京时间（比 UTC 多 8 小时）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（7）

<details open>
<summary><strong>Steam 黑五：10 款特惠全部经 appdetails 回读，战地双作 -95% 领跑</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥9.90 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-24 02:00 收</span></summary>
<p>Steam 官方 <code>featuredcategories</code> 本轮返回 10 条特惠，金额已从“分”换算成人民币。10 款全部用 <code>appdetails</code> 回读过 <code>initial / final / discount_percent</code>，三项与榜单一致，没有未核实价格。首轮并发请求有 6 款超时，逐款重试后全部成功。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏（appid）</th><th style="padding:6px 8px 6px 0;">国区价</th><th style="padding:6px 8px 6px 0;">折扣</th><th style="padding:6px 0 6px 0;width:26%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">战地风云 5（1238810）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥228.00 → ¥11.40</td><td style="padding:8px 8px 8px 0;">-95%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Battlefield 1（1238840）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥198.00 → ¥9.90</td><td style="padding:8px 8px 8px 0;">-95%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">双人成行（1426210）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥198.00 → ¥39.60</td><td style="padding:8px 8px 8px 0;">-80%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">FINAL FANTASY VII REBIRTH（2909400）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥248.00 → ¥37.20</td><td style="padding:8px 8px 8px 0;">-85%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">FINAL FANTASY VII REMAKE INTERGRADE（1462040）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥198.00 → ¥35.64</td><td style="padding:8px 8px 8px 0;">-82%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">对马岛之魂 导演剪辑版（2215430）</td><td style="padding:8px 8px 8px 0;">¥398.00 → ¥199.00</td><td style="padding:8px 8px 8px 0;">-50%</td><td style="padding:8px 0 8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">漫威蜘蛛侠 重制版（1817070）</td><td style="padding:8px 8px 8px 0;">¥414.00 → ¥165.60</td><td style="padding:8px 8px 8px 0;">-60%</td><td style="padding:8px 0 8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">天国：拯救2（1771300）</td><td style="padding:8px 8px 8px 0;">¥228.00 → ¥75.24</td><td style="padding:8px 8px 8px 0;">-67%</td><td style="padding:8px 0 8px 0;">12-01 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">我带过的最差一届（5175310）</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">¥28.00 → ¥18.20</td><td style="padding:8px 8px 8px 0;">-35%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-24 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;">转运军团 - Slotbound（4459590）</td><td style="padding:8px 8px 8px 0;">¥42.00 → ¥37.80</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">11-27 02:00</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">核实于 2026-11-21 00:04–00:08，来源为 Steam 官方 <code>appdetails</code>（<code>cc=cn&amp;l=schinese</code>）。折扣页面会滚动换位，掉出榜单不等于活动结束；要买请自己打开商店页确认最终价格。国区价格可能随账号区域与支付方式变化，以结算页为准。</p>
</details>

<details>
<summary><strong>Epic 免费位：《Mark of the Deep》0 元，11-27 00:00 截止，下周《Bread and Fred》接档</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span>（原价 ¥55.00）｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00 截止</span></summary>
<p>Epic 官方 <code>freeGamesPromotions</code> 接口（<code>locale=zh-CN&amp;country=CN</code>）本轮只有一条满足「<code>discountPrice == 0</code> 且 <code>originalPrice &gt; 0</code>」：<strong>Mark of the Deep</strong>，原价 ¥55.00，领取窗口 <code>2026-11-19T16:00:00Z</code> 至 <code>2026-11-26T16:00:00Z</code>，换算北京时间是 <strong>11-20 00:00 至 11-27 00:00</strong>。领取后永久入库，不是限时试玩。</p>
<p>同一接口的 <code>upcomingPromotionalOffers</code> 给出下一档：<strong>Bread and Fred</strong>，原价 ¥47.00，<code>2026-11-26T16:00:00Z</code> 起 0 元，即北京时间 <strong>11-27 00:00 至 12-04 00:00</strong>。这是官方字段，不再是推测；但免费位仍可能临时调整，届时以商店页刷新为准。领取入口：<a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com/zh-CN/free-games</a>。核实于 2026-11-21 00:05。</p>
</details>

<details>
<summary><strong>GitHub Trending：Claude-BugHunter 单日 +1,660 继续领跑，Agent Skills 仍占前十的 5 席</strong> ｜ <span style="color:#6b7280;">2026-11-21 00:06 抓取</span></summary>
<p>本轮 <code>github.com/trending?since=daily</code> 抓到 16 个仓库，按「今日新增 star」排序。前十里 Agent Skills / coding agent 相关仍占 5 席；star 总数为页面快照，GitHub REST API 本轮因出口 IP 限流未能二次复核（403）。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">仓库</th><th style="padding:6px 8px 6px 0;">今日 +</th><th style="padding:6px 8px 6px 0;">star 总数</th><th style="padding:6px 0 6px 0;">一句话</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/elementalsouls/Claude-BugHunter">elementalsouls/Claude-BugHunter</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">+1,660</td><td style="padding:8px 8px 8px 0;">13,655</td><td style="padding:8px 0 8px 0;">漏洞挖掘与红队外网的 Claude Code skill 包</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/firecrawl/firecrawl">firecrawl/firecrawl</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">+1,226</td><td style="padding:8px 8px 8px 0;">204,946</td><td style="padding:8px 0 8px 0;">给 agent 用的网页搜索、抓取与结构化数据层</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/XiaoYouChR/Ghost-Downloader-3">XiaoYouChR/Ghost-Downloader-3</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">+1,082</td><td style="padding:8px 8px 8px 0;">13,470</td><td style="padding:8px 0 8px 0;">多协议下载器，支持浏览器接管与并发分片</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td style="padding:8px 8px 8px 0;">+888</td><td style="padding:8px 8px 8px 0;">322,635</td><td style="padding:8px 0 8px 0;">agentic skills 框架与开发方法论</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/mjmirza/app-store-compliance">mjmirza/app-store-compliance</a></td><td style="padding:8px 8px 8px 0;">+874</td><td style="padding:8px 8px 8px 0;">2,482</td><td style="padding:8px 0 8px 0;">App Store / Google Play 过审避坑手册</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/jingyaogong/minimind">jingyaogong/minimind</a></td><td style="padding:8px 8px 8px 0;">+841</td><td style="padding:8px 8px 8px 0;">67,548</td><td style="padding:8px 0 8px 0;">两小时从 0 训出 64M 小模型</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/HKUDS/CLI-Anything">HKUDS/CLI-Anything</a></td><td style="padding:8px 8px 8px 0;">+774</td><td style="padding:8px 8px 8px 0;">61,120</td><td style="padding:8px 0 8px 0;">把软件改造成 agent 可直接调用的 CLI</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://github.com/toeverything/AFFiNE">toeverything/AFFiNE</a></td><td style="padding:8px 8px 8px 0;">+686</td><td style="padding:8px 8px 8px 0;">75,581</td><td style="padding:8px 0 8px 0;">文档、白板与知识库一体的协作工具</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">抓取于 2026-11-21 00:06。榜单只说明当天的关注度，不代表质量或安全审计结论；装 skill 前先读 README 与权限要求，尤其是安全/红队类 skill。</p>
</details>

<details>
<summary><strong>开发 · AI：黎曼猜想“证明”冲上 HN 头条，OpenSSL 9.8 分漏洞同日刷屏</strong> ｜ <span style="color:#6b7280;">2026-11-21 00:07 核实</span></summary>
<p><strong>HN 首页</strong>：Anthropic 数学家 Levent Alpoge 宣称给出黎曼猜想的一般性证明（835 分 / 487 评，<a href="https://alpo.ge/remark.pdf">alpo.ge/remark.pdf</a>）；Anthropic 官方博客称 Claude 解决了黑洞物理的两个开放问题（524 分 / 252 评）；Architect Labs 称 AI 发现、设计并验证了一种新 CPU 架构 Frostbite（407 分 / 254 评）；OpenSSL 披露 <code>EVP_EncodeBlock()</code> 缓冲区溢出，CVE-2026-121481、CVSS 9.8（331 分 / 282 评）；PostgreSQL 19 正式文档上线（319 分）；FFmpeg 9.1 “Gauss” 发布（234 分）；Signal 发布隐私保护说明（173 分）。</p>
<p><strong>Lobsters</strong>：Vim Classic 8.3.1 发布（32 赞）；LWN 讨论移除 <code>binder.c</code>（24 赞）；PostgreSQL 19 发布（78 赞）；「Design for Understandability」（46 赞）；Jujutsu 入门与 jj-musubi 实时同步（20 / 9 赞）；DreamCoder 编辑器发布（10 赞）。</p>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">核实于 2026-11-21 00:07，来源为 HN Algolia 与 lobste.rs/hottest.json。黎曼猜想条目的 PDF 尚未经同行评审，这里只记录传播事实，不背书结论；OpenSSL 漏洞请以官方安全公告与发行版补丁为准。</p>
</details>

<details>
<summary><strong>IT之家 · AI 动态：Anthropic 上市次日跌 9%、内存采购价同比涨 263%、Steam Machine 售价成谜</strong> ｜ <span style="color:#6b7280;">11-20 23:37–23:48 抓取</span></summary>
<p><strong>AI 与资本</strong>：IT之家转述《科学美国人》称 Anthropic 数学家宣称与 Claude 合作攻克黎曼猜想；同日 Anthropic 上市次日股价下跌 9%，AI 板块继续承压；三星电子两位高管称 Neocloud 风险有限、AI 投资基于实际需求。</p>
<p><strong>硬件与供应链</strong>：三星电子非半导体板块内存平均采购价今年前九个月同比暴涨 263%；Valve 坦承内存成本涨幅前所未有，Steam Machine 未来售价“无法得知”，512GB 版目前尚有少量现货。</p>
<p><strong>安全与出行</strong>：伦敦交通局证实 26.5 万名 Oyster 照片卡用户敏感信息泄露；特斯拉辅助驾驶系统获意大利运行许可，已覆盖 12 个欧洲国家；奔驰成为德国首家获批点到点辅助驾驶的车企；加州禁令引发连锁反应，Waymo 暂停全美 Robotaxi 高速公路服务。</p>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">核实于 2026-11-21 00:03，来源为 IT之家 RSS（北京时间 11-20 23:37–23:48 的条目）。以上均为转述，未逐条回厂商新闻稿。</p>
</details>

<details>
<summary><strong>币圈：BTC 59,073.5（-6.43%）跌破 6 万、ETH -8.1%、SOL -7.38%，情绪指数 12</strong> ｜ <span style="color:#6b7280;">00:09 快照</span></summary>
<p>本轮 <code>bitfinex</code> / <code>binance</code> / <code>okx</code> / <code>coingecko</code> / <code>coinbase</code> / <code>kraken</code> / <code>bybit</code> 整源被挡，改走 Gate.io 公开 ticker 拿到一手价格：<strong>BTC 59,073.5 美元</strong>（24h -6.43%，日内高 63,410.5、低 58,764.5）、<strong>ETH 1,636.96</strong>（24h -8.1%，高 1,791.5、低 1,623.8）、<strong>SOL 68.26</strong>（24h -7.38%，高 74.69、低 67.77）。恐惧贪婪指数 <strong>12（Extreme Fear）</strong>，与昨日持平。</p>
<p><strong>媒体轴（只作语境）</strong>：The Block 称美国现货比特币 ETF 单日净流出 5.82 亿美元，11 月累计接近 35 亿美元；Ark 在 Anthropic 上市首日买入约 9,000 万美元股票，同时减持以太坊与 Solana 质押 ETF；MoonPay 向 OCC 申请国家信托银行牌照以扩展稳定币服务；美国参议院通过“Death Bets Act”，禁止与死亡和战争挂钩的预测市场合约；Wintermute 政策负责人呼吁加密游说圈在华盛顿“清理门户”。</p>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">行情为 2026-11-21 00:09 的 Gate.io <code>/spot/tickers</code> 快照，只记录数字，不构成任何买卖建议或目标价。媒体转述的 ETF 流向、持仓与监管进展未回官方公告或链上原始数据核对，统一放在「观察」语境。持仓相关操作请自己回交易所公告与账户记录确认。</p>
</details>

<details>
<summary><strong>黑五前哨：RackNerd KVM VPS $15.98/年、HostArmada VPS $3.28/月、Dynadot .com 转入 $10.49</strong> ｜ <span style="color:#6b7280;">全部为转述价，未回商家官网核实</span></summary>
<p><strong>idcspy</strong>：RackNerd 2026 黑五，KVM VPS 低至 <strong>$15.98/年</strong>、续费同价，美国机房现货，独立服务器 $64/月起（11-20 10:31）；HostArmada 七周年庆，虚拟主机低至 <strong>$1.91/月</strong>、VPS 低至 <strong>$3.28/月</strong>，最高 84% 优惠（11-20 14:51）；Dynadot 黑五&amp;网一，<code>.com</code> 转入低至 <strong>$10.49</strong>，<code>.org/.net/.com</code> 首年 $19.99（11-20 17:10）；另有阿里云 Token Plan＋Qoder CN 首月 34.4 元起、最高 65,000 Credits（11-20 15:01）。</p>
<p><strong>LowEndBox</strong>：Fast Moose 黑五早鸟，共享主机 <strong>$15.99/年</strong>、不限账户与流量（11-20 12:00）；2GB Ryzen VPS <strong>$22.99/年</strong> 预热活动（11-19）；DediRock 8GB RAM VPS <strong>$24.99/年</strong>（11-18）。</p>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">以上全部来自 idcspy 与 LowEndBox 的转述/广告稿，本轮没有逐条回商家官网核对配置、库存与续费价。<strong>提醒：此类转述价与官网经常不一致，下单前务必回官网确认。</strong>VPS 类只报道价格与门槛，不代为注册、绑卡或下单。</p>
</details>

## 观察（8）、方法与这一轮的异常

<details open>
<summary><strong>安全观察：OpenSSL 9.8 分、群晖 SA-26:21、Nginx CVE-2026-123007、PHP 8.6</strong></summary>
<p><strong>OpenSSL</strong>：HN 指向的 PR 显示 <code>EVP_EncodeBlock()</code> 存在缓冲区溢出，CVE-2026-121481，CVSS 9.8，属于需要优先评估的一类。</p>
<p><strong>群晖</strong>：官方 11-19 披露 OAuth API 与 NGINX HTTP/2 两项漏洞，最高 9.8 分，可远程读写文件，官方仍在紧急修复中（Synology-SA-26:21）。</p>
<p><strong>Nginx</strong>：11-18 披露多项漏洞，其中两项涉及 HTTP/2，攻击者可能无需登录远程执行代码，CVE-2026-123007，评分 8.1；1.31.8 及以下版本受影响，升级路径见官方公告。</p>
<p><strong>PHP</strong>：PHP 8.6 正式发布，同时 8.2.36、8.3.37、8.4.28、8.5.13 修复安全漏洞，网站管理员应优先安装当前分支的安全补丁。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为小众软件 RSS 与 HN 链接。安全条目只做提醒，补丁细节与受影响版本请以厂商公告为准。</p>
</details>

<details>
<summary><strong>发布观察：PostgreSQL 19、FFmpeg 9.1、Vim Classic 8.3.1、Alfred 6</strong></summary>
<p><strong>PostgreSQL 19</strong> 正式发布，官方文档与新闻稿同日上线；Snowflake 工程博客补充了内置 <code>REPACK</code> 对表膨胀清理的改进。</p>
<p><strong>FFmpeg 9.1 “Gauss”</strong> 发布；<strong>Vim Classic 8.3.1</strong> 发布；<strong>Alfred 6</strong> 正式版带来搜索历史、剪贴板与 Alfred UI Toolkit，工作流可以自绘输入框、按钮、表格与预览，并能调用 AI 模型。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为 HN、Lobsters 与少数派/小众软件 RSS。发布说明只记录版本与主要变化，升级前请读官方 changelog。</p>
</details>

<details>
<summary><strong>AI 观察：黎曼猜想“证明”尚未评审，Anthropic 官方黑洞论文可复核</strong></summary>
<p>Alpoge 的 PDF 目前只有个人主页与 HN 讨论，未见期刊投稿或同行评审信息，数学界是否接受仍需时间。Anthropic 官方博客的“Claude 解决黑洞物理两个开放问题”属于机构自述，至少提供了可复现的实验描述。IT之家同日报道 Anthropic 上市次日股价下跌 9%，说明资本市场并未把单篇研究当成基本面拐点。</p>
<p style="font-size:12.5px;color:#6b7280;">本条为传播事实记录，不构成对研究结论的背书。</p>
</details>

<details>
<summary><strong>游戏观察：《GTA 6》评测解禁、Steam Machine 受内存成本拖累</strong></summary>
<p>少数派转载篝火营地《GTA 6》游玩体验，称其为“游戏史最高分、不负 13 年等待”；Take-Two 前 CEO 费德称《GTA 6》将是 AI 时代前夜最后的“传统”3A 大作。硬件侧，Valve 因内存成本无法给出 Steam Machine 的未来售价，AI 热潮对消费电子的传导已经从显卡扩散到整机。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为少数派 RSS 与 IT之家 RSS，评测结论只代表原作者。</p>
</details>

<details>
<summary><strong>应用观察：微软关闭 To Do、UU 远程转付费、群晖漏洞、浮屏上架</strong></summary>
<p>微软宣布 Microsoft To Do 将于明年 6 月全面停用——从收购 Wunderlist 到关停自研替代品，前后 12 年；网易 UU 远程结束免费运营，VIP 24 元/月起、SVIP 88 元/月起，免费版降至 1080P 30 帧；少数派作者自荐的「浮屏」把截图变成可记录的“岛屿”，适合轻量生活记录。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为小众软件与少数派 RSS，仅记录产品变化。</p>
</details>

<details>
<summary><strong>产品观察：Product Hunt 今日榜单与阮一峰周刊第 420 期</strong></summary>
<p>Product Hunt 本轮抓到 greatai Review、Direct by Instagram、Mailpipe、pickfit、Andromon、Veryfi Thinking Mode、Zethos、UndoGuard 等条目，整体偏 AI 工具与效率插件。阮一峰《科技爱好者周刊》第 420 期「最分心的一年」于 11-20 发布。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为 Product Hunt feed 与阮一峰 Atom。榜单只记录当天曝光，不代表推荐。</p>
</details>

<details>
<summary><strong>数据异常：7 个行情接口被挡、PANews RSS 退化、GitHub API 限流</strong></summary>
<p>本轮 <code>bitfinex</code>、<code>binance</code>、<code>okx</code>、<code>coingecko</code>、<code>coinbase</code>、<code>kraken</code>、<code>bybit</code> 全部失败，形态为超时或 SSL 握手被重置，按代理通道限制记录，不判为站点改版；<code>panews</code> 的 <code>/zh/rss</code> 已返回 HTML 订阅页而非 XML，本轮改用 The Block RSS 补位；GitHub REST API 因共享出口 IP 触发 403 限流，Trending 的 star 总数与今日增量仍来自页面现抓。</p>
<p style="font-size:12.5px;color:#6b7280;">以上异常不影响价格与免费游戏结论，因为这两类数据分别来自 Steam / Epic 官方接口并逐条回读。</p>
</details>

<details>
<summary><strong>方法与免责声明</strong></summary>
<p>本轮取数窗口为 2026-11-21 00:03–00:12（北京时间）。价格口径：Steam 为 <code>appdetails?cc=cn&amp;l=schinese</code> 的 <code>initial / final / discount_percent</code>，截止时间为 <code>featuredcategories.discount_expiration</code> 的 epoch 换算；Epic 为 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 的 <code>originalPrice / discountPrice / endDate</code>。行情为 Gate.io 公开 ticker 快照，情绪指数来自 alternative.me。</p>
<p>本站只做信息聚合与核实，不代注册、不代下单、不构成投资建议。价格、库存、活动时间都可能随时变化，执行前请回官方页面确认。</p>
</details>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">06:30 早间全量复核（同日发布）</p>

<p style="margin:0 0 16px;">午夜那一轮 00:03–00:12 取数，把 Steam 黑五、Epic 周免、GitHub Trending 与行情快照都核实了一遍。06:30 这一轮跑满 25 个来源，取回 305 条、去重后新增 169 条，<code>errors=1</code>——唯一异常是 <code>appstore</code>（iOS 限免层）报 <code>URLError</code>，06:35 实测发现层 <code>t.me/s/TossTF</code> 直连仍 000、走代理 200，判为当轮瞬时失败而非改版或代理整体失效，06:37 单源重跑 <code>fetched=18 fresh=18 errors=0</code>，iOS 这一层没有缺位。下面只写增量：Kraken 的降级复查、两条国区本体限免、午夜档截稿后才出现的一手技术材料，以及一处截止时间的反向更正。午夜档已核实的 Steam 与 Epic 结论不作废，本轮重抓逐条一致。</p>

<div style="border:1px solid #e6e8eb;border-radius:10px;padding:14px 16px;margin:0 0 24px;">
<p style="margin:0 0 10px;font-size:14px;font-weight:600;color:#1f2329;">早间增补行动清单</p>
<table>
<thead><tr><th>时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
<tbody>
<tr>
<td><strong style="color:#c0392b;">进行中</strong><br>状态页 06:04 更新</td>
<td>Kraken：充提与衍生品仍在降级窗口（午夜档缺这个源）</td>
<td><span style="color:#6b7280;">minor</span></td>
<td><a href="https://status.kraken.com/">状态页</a></td>
</tr>
<tr>
<td><strong style="color:#c0392b;">Apple 不公布</strong><br>限免截止时间</td>
<td>App Store 本体免费：PDF编辑器（id 6450979125）</td>
<td><span style="color:#1a7f37;font-weight:600;">0 元</span><br><span style="color:#6b7280;">下载不花钱</span></td>
<td><a href="https://apps.apple.com/cn/app/id6450979125">商店页</a></td>
</tr>
<tr>
<td><strong style="color:#c0392b;">Apple 不公布</strong><br>限免截止时间</td>
<td>App Store 本体免费：一生声迹（id 6825671043）</td>
<td><span style="color:#1a7f37;font-weight:600;">0 元</span><br><span style="color:#6b7280;">下载不花钱</span></td>
<td><a href="https://apps.apple.com/cn/app/id6825671043">商店页</a></td>
</tr>
<tr>
<td><strong style="color:#c0392b;">11-27 00:00</strong><br>北京时间（反向更正）</td>
<td>Epic《Mark of the Deep》截止口径回到午夜档的值</td>
<td><span style="color:#1a7f37;font-weight:600;">0 元</span><br><span style="color:#6b7280;">原价 ¥55.00</span></td>
<td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 领取页</a></td>
</tr>
</tbody>
</table>
</div>

<details open>
<summary><strong>🔥 早间唯一紧急：Kraken 充提与衍生品降级，11-20 报过、本轮复查仍未 resolve</strong> —— <span style="color:#c0392b;">状态页最后更新 11-21 06:04（北京时间）</span></summary>
<p>06:34 回读 Statuspage 三份原文：<code>status.json</code> 为 <code>indicator=minor</code> / <code>Partially Degraded Service</code>，页面 <code>updated_at=2026-11-20T22:04:40Z</code>（北京 11-21 06:04，即本轮取数前三十分钟）。<code>components.json</code> 里非 operational 的是 <code>User Interface</code>、<code>Kraken Derivatives</code>、<code>Digital Currency Funding</code>（充提入口）与 <code>MemeCore (M) - BNB Chain</code>、<code>Osmosis (OSMO)</code>、<code>Stablr Euro (EURR) - Ethereum</code>、<code>Stablr USD (USDR) - Ethereum</code> 七个组件，全部 <code>degraded_performance</code>。<br><code>incidents/unresolved.json</code> 现行三条：<strong>Stablr USD (USDR) 与 Stablr Euro (EURR) 的 Funding Methods Halted</strong>（identified，起于 05-24 14:19 北京，最后更新 07-01 22:03）；<strong>MemeCore (M) Deposits Disabled</strong>（monitoring，起于 08-19 16:20 北京，提现已恢复、充值仍关闭）；<strong>Osmosis (OSMO) Funding Delays</strong>（investigating，起于 11-14 19:02 北京，公告原文「Deposits and withdrawals may be delayed」）。<br>列紧急的理由照 11-20 的口径不变：它落在「服务状态非 none」这一档，直接决定在 Kraken 的充提入口与衍生品撤单是否可用；而午夜档那轮 <code>exchange-status</code> 没有进增量，这个状态当时看不到。<strong>你要做的</strong>：只有在 Kraken 有资产、跑 API 或挂着衍生品仓位才需要动作——不要在降级窗口做充提与撤单，动手前先确认状态页已 resolved；本轮没有证据表明你在用 Kraken，若确实没有，这条只是背景。同轮 Coinbase <code>indicator=none</code>（All Systems Operational）。<a href="https://status.kraken.com/">status.kraken.com</a> ｜ 核实于 2026-11-21 06:34</p>
</details>

<details>
<summary><strong>⭐ 早间新增值得（5）</strong> —— 国区 iOS 本体免费 2 条 + 午夜档截稿后的 3 条一手技术材料</summary>
<p><strong>App Store 本体免费（记法照旧：认 id 不认名字）</strong>：汇总频道 11-20 播报「本体限免」，iTunes lookup 按 id 核到国区现价 0 的有两条——<a href="https://apps.apple.com/cn/app/id6450979125">PDF编辑器 - 合并拆分与签名盖章（id 6450979125，合并/拆分/签名盖章）</a>、<a href="https://apps.apple.com/cn/app/id6825671043">一生声迹（id 6825671043）</a>。06:38 又用 <code>--lookup</code> 逐个按 id 复核了一遍，两条均为「免费 ← 现价为 0」。口径边界：<strong>核到现价 0 只等于「今天下载不花钱」，接口分不出本就免费与促销中，不等于「限免仍在」；Apple 不公布限免截止时间</strong>，这一栏不补日期。昨天已报过的 AuraRead（id 6770079462）与 AiZIP（id 1381194246）本轮重抓仍为 0，按同 id 不重推。<br>核实于 2026-11-21 06:38。</p>
<p><strong>Terence Tao：Navier–Stokes 有限时间 blow-up 与广义黎曼猜想</strong>——一手博客发布于 11-20 17:21 UTC＝北京 11-21 01:21，<strong>晚于午夜档 00:12 的截稿</strong>，是黎曼猜想这条线当天最新的原始材料，而不是媒体转述；06:43 页面 200 可达。<a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">原文</a> ｜ 核实于 2026-11-21 06:43。</p>
<p><strong>Show HN: OpenComputer（diggerhq）——Devin 的开源替代</strong>：仓库描述原文「An open-source, faster Devin alternative」，06:44 页面 200 可达，与在跑的 Agent 编码工具同赛道，值得自查架构与授权方式；本轮没有跑过它，不评价完成度。<a href="https://github.com/diggerhq/opencomputer">仓库</a> ｜ 核实于 2026-11-21 06:44。</p>
<p><strong>DreamCoder：《Mastering Emacs》作者的 coding harness / IDE</strong>：作者本人发布的一手博客，06:43 页面 200 可达，编辑器与自动化方向可直接评估。<a href="https://www.masteringemacs.org/article/announcing-dreamcoder">原文</a> ｜ 核实于 2026-11-21 06:43。</p>
<p><strong>反向更正一处：Epic《Mark of the Deep》的截止时间</strong>。本轮重查官方促销接口 <code>endDate=2026-11-26T16:00:00Z</code>，换算北京时间是 <strong>11-27 00:00</strong>，与午夜档一致。而 <a href="https://oxygc.github.io/posts/info-radar-2026-11-20/">11-20 那篇</a>的早间复核把这一条「更正」成了 08:00——那次更正本身算错了，同一段里写的 UTC 11-26 16:00 是对的，换算应得 00:00。以本行为准：<strong>11-27 00:00（北京时间）截止，原价 ¥55.00、<code>discountPrice=0</code> 两条与午夜档相同</strong>。 ｜ 核实于 2026-11-21 06:35</p>
</details>

<details>
<summary><strong>👀 早间新增观察（11）与本轮取数健康度</strong></summary>
<p><strong>阿里云 Token Plan＋Qoder CN「首月 34.4 元起 / 最高 65,000 Credits」</strong>——只有美国主机侦探（<code>idcspy</code> 11-20 15:01）一条转述。本轮回官方定价页 <a href="https://www.aliyun.com/product/qoder">aliyun.com/product/qoder</a> 实测到的是企业版 <strong>Teams ¥300.00/席位/月含 3,000 Credits</strong>、<strong>Teams 年包 ¥3,060.00/席位/年（年付 85 折）</strong>，<strong>没有核到 34.4 元首月档，也没有核到 65,000 Credits 这个额度</strong>；<code>qoder.com/pricing</code> 直取只回 35 字节（JS 壳）。未核实，要下手先自己登录官方权益页确认档位。</p>
<p><strong>币安 4 条公告（11-20）</strong>——TradFi USDⓈ 本位永续上新、SNDKUSDT「Last Price Protected」期结束、SNDKUSDT 合约规模调整提前完成、Monitoring Tag 扩展至 BANK/INIT/MITO/ONE/THE/ZIL 并移除 MORPHO/HYPE 的 Seed Tag。只取到公告目录标题，未逐条回正文核生效时间与合约地址；<strong>标签变化不等于下架或充提暂停</strong>，与在用资产可得性无关，只列存在。<a href="https://www.binance.com/en/support/announcement">公告目录</a> ｜ 核实于 2026-11-21 06:32（仅标题层）。</p>
<table>
<thead><tr><th>条目</th><th>为什么只算观察</th></tr></thead>
<tbody>
<tr><td>App Store 内购限免 5 条：大明万年历 6769966541、惠普打印机 6814182997、择光 6826511163、NuSSH 6757864341、PocketADB 6828068983</td><td>iTunes 国区下载价实测均为 0，但内购解锁价不体现在下载价上，「本体免费」证明不了「内购已限免」，只算频道转述</td></tr>
<tr><td>App Store 兑换码型限免：Luggzy</td><td>兑换码不转载，只留原帖 <a href="https://t.me/TossTF/3984">TossTF/3984</a> 自取；播报没有 App Store 直链，未走核价</td></tr>
<tr><td>App Store 查不到上架记录：FinalLook 6809647256、Axon 6450880876、App Launcher 6831404723；另「鼠标·键盘」无直链</td><td>06:38 逐个 <code>--lookup</code> 复核，国区商店均返回查无此 id ⇒ 价格未核实；最后一条连 id 都取不到</td></tr>
<tr><td>Google DeepMind 新建 <code>math-horizon</code> 仓库（北京 05:42）</td><td>06:44 确实 200 在线，但 GitHub 描述为空、本轮没读 README 判断用途，只能确认「存在」，不能替它定性</td></tr>
<tr><td>Nvidia 会计问题受 SEC 调查（北京 04:22）</td><td>HN 标题口径是 "sources say"，通讯社转述未经手，未核 SEC 原文或 Nvidia 回应</td></tr>
<tr><td>伦敦交通局遭网络攻击、26.5 万张 Oyster 卡用户数据泄露</td><td>IT之家单源转述，未回 TfL / NCSC 一手公告核影响范围与时间</td></tr>
<tr><td>Fast Moose 黑五早鸟：共享主机 $15.99/年、不限账号数与带宽</td><td>LowEndBox 促销帖带软文属性，未回商家官网核续费价与是否续费同价</td></tr>
<tr><td>Steam 黑五重抓 3 条：漫威蜘蛛侠 重制版 ¥165.60（-60%，12-02 02:00 收）、战地风云 5 ¥11.40、战地 1 ¥9.90（-95%，12-04 02:00 收）</td><td>06:32 <code>appdetails</code> 价格与截止与午夜档逐条一致，同一活动同一 URL，按「旧活动不重推」过滤，不进值得</td></tr>
<tr><td>Remind &amp; Record（6832136677）现价 ¥8.00、AudayWatch（6821917560）¥38.00</td><td>播报「本体限免」与国区实价不符，判为已失效或已改价，昨日已列同一结论</td></tr>
<tr><td>PostgreSQL 19 浏览器可运行示例教程（北京 01:08）</td><td>与午夜档报的 PG19 发布是两条内容，本轮没读全文判断质量，只在评估升级路径时作辅助材料</td></tr>
<tr><td>v2ex 生活闲聊 10 条、IT之家车企与手机口水稿 15 条</td><td>与五条赛道无关，计入统计不进正文</td></tr>
</tbody>
</table>
<p><strong>行情与热度快照（截至 11-21 06:32 取数，来源 CoinGecko / CMC / alternative.me）</strong>：BTC $59,059（-4.9%）、ETH $1,621.87（-7.7%）、BNB $539.93（-7.0%）、USDT $0.9986、USDC $0.9994；异动榜 Pearl $1.87（-18.6%，rank 79）、Zcash $738.25（-17.0%，rank 11）、Lighter $2.34（-16.4%，rank 90）；热搜 BTC / HYPE / SOL / SUI / PENGU / TRUMP；恐惧贪婪指数 12（Extreme Fear）。这些是数字不是信息，不构成任何操作建议，本段不写方向与目标价。</p>
<p><strong>本轮取数健康度</strong>：<code>SUMMARY fetched=305 fresh=169 sources=25 errors=1</code>。18 个来源取到新条目（hackernews 25、ithome 25、producthunt 15、panews 15、lobsters 14、coindesk 12、theblock 12、v2ex 10、coingecko-trending 10、coingecko-markets 7、idcspy 7、coinmarketcap-search 6、binance-ann 4、steam 3、lowendbox 1、ruanyifeng-weekly 1、exchange-status 1、fng-index 1）。唯一 <code>ERR source=appstore URLError</code> 已在 06:37 单源重跑补救（<code>fetched=18 fresh=18 errors=0</code>，核价额度 15 条用满）；<code>epic-store</code>、<code>github-trending</code>、<code>hf-daily-papers</code>、<code>ethblog</code>、<code>crypto-release</code>、<code>appinn</code> 六源本轮无新增条目，属午夜档已报或周更节奏，不是故障。<strong>境外源没有出现整批被挡的形态</strong>（coindesk / theblock / binance / CoinGecko 全绿），代理节点这一轮正常。</p>
</details>
