---
title: "资讯雷达 2026-11-23｜Epic《深渊之印》最后 4 天、Steam 黑五战地 5 -95%、BTC 回升至 6.11 万"
author: OxYGC
date: 2026-11-23 00:20:00 +0800
permalink: /posts/info-radar-2026-11-23/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam黑五, 比特币, 黎曼猜想, GitHub趋势]
description: "2026-11-23 当天唯一一篇：本轮 25 个来源取回 174 条、去重后 130 条、11 个异常。Epic《深渊之印》¥55→0 至 11-27 00:00；Steam 黑五 9 款逐一回读 appdetails，战地风云 5 -95% ¥11.40、双人成行 -80% ¥39.60、《我带过的最差一届》-35% ¥18.20 最近 11-24 02:00 收。BTC 00:22 Gate.io 快照 61,146.8（+2.06%），恐惧贪婪 11（Extreme Fear）。HN 头条仍是 Lean 社区对黎曼猜想的“形式化核验”（1,147 分），但编译通过不等于命题已证明；GitHub Trending 16 条继续被 Agent Skills 类仓库占据。失败的 11 个源集中在境外行情与交易所接口（binance / coingecko / cgmarkets / cmc / exstatus / ethblog / creleases / coindesk / v2ex / hf / appstore），行情因此改走 Gate.io 补位。"
---

这一轮取数在 2026-11-23 00:10–00:22（北京时间）完成：25 个来源里 14 个取到数据（含 1 个合法空档），11 个报错。`SUMMARY fetched=174 fresh=130 sources=25 errors=11`。异常几乎全部集中在需要境外通道的行情与交易所接口——`binance`、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`creleases`、`coindesk` 都报 `URLError`，`v2ex` 与 `hf` 也未能握手，`appstore`（iOS 限免层）单源重跑两次仍是 `URLError`。行情因此改走 Gate.io 公开 ticker 补位，技术资讯靠 HN、Lobsters、GitHub Trending、ITHome、阮一峰与 Product Hunt 支撑。**这是 2026-11-23 当天唯一一篇；今天若再跑，只会在本文件内更新，不新增文件。**

结论先摆前面：**今天没有“今天到期”的硬截止，最近一个到期点是 11-24 02:00 的《我带过的最差一届》-35%（¥18.20）。** 免费游戏方面，Epic 本周仍只有《深渊之印》（Mark of the Deep，¥55→0）一款，11-27 00:00 截止；同接口里《TerraScape》-70% 到 12-22 00:00，是这一轮唯一新核到的 Epic 折扣。Steam 黑五 9 款全部用 `appdetails?cc=cn` 逐条回读，战地风云 5（-95%，¥11.40）与双人成行（-80%，¥39.60）仍是幅度最大的两张；第 10 款《The Escapists 2 GOTY》因 `appdetails` 未返回该包体，价格未二次核实，已移出「值得」。资讯面仍是数学：Lean 社区博客《Lean verification of the Riemann Hypothesis》以 1,147 分居 HN 首位，**“形式化核验通过”不等于“黎曼猜想已被证明”**。市场侧是急跌后的第二天反弹：BTC 00:22 报 61,146.8（+2.06%），但恐惧贪婪指数从 12 再降到 **11（Extreme Fear）**。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮真正会过期、或需要你自己动手的只有这几条</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-24 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《我带过的最差一届》-35%</td>
<td style="padding:9px 8px 9px 0;">¥28.00 → ¥18.20</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/5175310/?l=schinese">store.steampowered.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-27 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《深渊之印》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-02 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《对马岛之魂 导演剪辑版》-50%、《漫威蜘蛛侠 重制版》-60%</td>
<td style="padding:9px 8px 9px 0;">¥199.00 / ¥165.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2215430/?l=schinese">对马岛</a> · <a href="https://store.steampowered.com/app/1817070/?l=schinese">蜘蛛侠</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-03 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《FF7 重生》-85%、《FF7 重制版》-82%</td>
<td style="padding:9px 8px 9px 0;">¥37.20 / ¥35.64</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2909400/?l=schinese">FF7 重生</a> · <a href="https://store.steampowered.com/app/1462040/?l=schinese">重制版</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-23 00:20–00:24 官方接口实测：Steam <code>appdetails?cc=cn&amp;l=schinese</code>、Epic <code>freeGamesPromotions</code>。Steam 的 <code>discount_expiration</code> 为 epoch，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（5）

<details open>
<summary><strong>Steam 黑五：9 款逐一回读 appdetails，战地风云 5 -95% 领跑</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥11.40 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-24 02:00 收</span></summary>
<p>Steam 官方 <code>featuredcategories</code> 本轮返回 10 条特惠，其中 9 条再用 <code>appdetails</code> 逐款复核，<code>initial / final / discount_percent</code> 三项与榜单一致。战地风云 5 以 -95%（¥228→¥11.40）居首，双人成行 -80%（¥198→¥39.60）次之；《The Escapists 2 GOTY》在 <code>appdetails</code> 未返回该包体，按“未二次核实不进值得”处理，只在这里留一句：榜单价 -90% ¥11.99、截止 12-06 02:00，需你自己回页面确认。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:12%;">折扣</th><th style="padding:6px 8px 6px 0;width:26%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1238810/?l=schinese">战地风云 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-95%</td><td style="padding:8px 8px 8px 0;">¥11.40 / ¥228.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1551360/?l=schinese">极限竞速：地平线 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥79.20 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2483190/?l=schinese">极限竞速：地平线 6</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-25%</td><td style="padding:8px 8px 8px 0;">¥223.50 / ¥298.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1817070/?l=schinese">漫威蜘蛛侠 重制版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥165.60 / ¥414.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2215430/?l=schinese">对马岛之魂 导演剪辑版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-50%</td><td style="padding:8px 8px 8px 0;">¥199.00 / ¥398.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1462040/?l=schinese">FF7 重制版 INTERGRADE</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-82%</td><td style="padding:8px 8px 8px 0;">¥35.64 / ¥198.00</td><td style="padding:8px 0;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2909400/?l=schinese">FF7 重生</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-85%</td><td style="padding:8px 8px 8px 0;">¥37.20 / ¥248.00</td><td style="padding:8px 0;">12-03 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5175310/?l=schinese">我带过的最差一届</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-35%</td><td style="padding:8px 8px 8px 0;">¥18.20 / ¥28.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">11-24 02:00</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:10px 0 0;">榜单只反映“此刻正在打折”，不代表历史最低；国区价格以 <code>cc=cn</code> 返回为准。如果只想要“幅度最大 + 时间最长”，战地风云 5 与双人成行都到 12-04 02:00，不必在今明两天决定。</p>
</details>

<details>
<summary><strong>Epic 本周《深渊之印》¥55→0 剩 4 天，《TerraScape》-70% 到 12-22</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00 收</span></summary>
<p>Epic 官方 <code>freeGamesPromotions</code> 接口（<code>locale=zh-CN&amp;country=CN</code>）本轮返回的当前 0 元档仍只有一款：《深渊之印》（Mark of the Deep），原价 ¥55.00，促销窗口 <code>2026-11-19T16:00Z</code> 至 <code>2026-11-26T16:00Z</code>，换算成北京时间就是 <strong>11-27 00:00 截止</strong>。海盗题材的银河恶魔城 + 魂系作品，领取后永久入库，不需要订阅。</p>
<p>同接口另有《TerraScape》-70%：原价 ¥53.00，现价 ¥37.10，窗口到 <code>2026-12-21T16:00Z</code>（北京时间 <strong>12-22 00:00</strong>）。本轮没有抓到下周免费档的新条目，昨天提到的《Bread and Fred》接档信息维持不变，本次不重复展开。以上时间全部以接口 <code>endDate</code> 为准，未做二次推断。</p>
</details>

<details>
<summary><strong>Lean 社区对黎曼猜想做形式化核验，HN 1,147 分，但“编译通过 ≠ 已证明”</strong> ｜ <span style="color:#c0392b;font-weight:700;">未经同行评审</span> ｜ <span style="color:#8a9099;">HN 全站第一</span></summary>
<p>HN 首页当前第一是 Lean 社区博客《Lean verification of the Riemann Hypothesis》（<a href="https://leanprover-community.github.io/blog/posts/riemann-hypothesis/">leanprover-community.github.io</a>），读数 <strong>1,147 分 / 954 评论</strong>（00:20 快照），比昨天午间记录的 897 分继续上涨。MIT 数学系页面同时上线了对应的核验文件入口。</p>
<p>需要把边界说清楚：<strong>Lean 编译通过只说明代码与所陈述的命题一致，不等于命题就是黎曼猜想，也不等于证明里没有未声明公理</strong>。这仍是手稿与形式化核验阶段，不是已通过同行评审的结论。对非数学读者，可操作的信息只有一条：未来数月若这些证明被接受，密码学与数论相关教材会被重写；在此之前，任何“黎曼猜想已被证明”的标题都应加上“待验证”。</p>
</details>

<details>
<summary><strong>GitHub Trending：16 条里 Agent Skills / 编码代理仍占一半以上</strong> ｜ <span style="color:#1a7f37;font-weight:700;">16 条</span> ｜ <span style="color:#8a9099;">00:12 抓取</span></summary>
<p>GitHub Trending 日榜（00:12 抓取）前 16 条中，与 Agent / Skills / 编码代理直接相关的超过一半，前三名仍是 Claude-BugHunter、superpowers、CLI-Anything。与昨天“firecrawl 单日 +1,241”的走势一致：<strong>流量继续从“模型本身”转向“给代理用的技能与工具”</strong>。本轮脚本只取回总 star，不提供可靠的“今日新增”字段，因此下表不写日增量，只列总 star 与用途。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:36%;">仓库</th><th style="padding:7px 8px 7px 0;width:14%;">总 star</th><th style="padding:7px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/elementalsouls/Claude-BugHunter">elementalsouls/Claude-BugHunter</a></td><td style="padding:7px 8px 7px 0;">17,177</td><td style="padding:7px 0;">Claude Code 的红队 / 漏洞狩猎技能包，82 个技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td style="padding:7px 8px 7px 0;">323,946</td><td style="padding:7px 0;">Agentic skills 框架与软件开发方法论</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/HKUDS/CLI-Anything">HKUDS/CLI-Anything</a></td><td style="padding:7px 8px 7px 0;">62,567</td><td style="padding:7px 0;">把软件做成 Agent 可直接调用的 CLI</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/jingyaogong/minimind">jingyaogong/minimind</a></td><td style="padding:7px 8px 7px 0;">68,499</td><td style="padding:7px 0;">2 小时从 0 训出 64M 小模型</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/cursor/plugins">cursor/plugins</a></td><td style="padding:7px 8px 7px 0;">18,332</td><td style="padding:7px 0;">Cursor 插件规范与官方插件</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/firecrawl/firecrawl">firecrawl/firecrawl</a></td><td style="padding:7px 8px 7px 0;">206,740</td><td style="padding:7px 0;">Agent 抓取 / 搜索基础设施</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/cathrynlavery/diagram-design">cathrynlavery/diagram-design</a></td><td style="padding:7px 8px 7px 0;">70,147</td><td style="padding:7px 0;">45 种图表的 Agent 设计技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/mvanhorn/last30days-skill">mvanhorn/last30days-skill</a></td><td style="padding:7px 8px 7px 0;">72,523</td><td style="padding:7px 0;">跨 Reddit / X / YouTube 的研究技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/google-labs-code/stitch-skills">google-labs-code/stitch-skills</a></td><td style="padding:7px 8px 7px 0;">11,801</td><td style="padding:7px 0;">面向 Stitch MCP 的技能库</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/Tracer-Cloud/opensre">Tracer-Cloud/opensre</a></td><td style="padding:7px 8px 7px 0;">14,270</td><td style="padding:7px 0;">CI/CD 可靠性的开源 Agent</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://github.com/toeverything/AFFiNE">toeverything/AFFiNE</a></td><td style="padding:7px 8px 7px 0;">76,638</td><td style="padding:7px 0;">知识库 / 白板工具</td></tr>
<tr><td style="padding:7px 8px 7px 0;"><a href="https://github.com/zhouxiaoka/autoclip">zhouxiaoka/autoclip</a></td><td style="padding:7px 8px 7px 0;">13,277</td><td style="padding:7px 0;">长视频一键剪成短视频的桌面工具</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:10px 0 0;">完整 16 条见取数原文；star 数为 00:12 页面读数，不排除后续变动。新库是否值得用仍需读 README，不凭名字判断。</p>
</details>

<details>
<summary><strong>阮一峰《科技爱好者周刊》第 420 期：最分心的一年</strong> ｜ <span style="color:#6b7280;">11-20 发布</span> ｜ <span style="color:#8a9099;">周更</span></summary>
<p>阮一峰《科技爱好者周刊》第 420 期《最分心的一年》已于 11-20 发布（<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">ruanyifeng.com</a>）。本期标题本身就是一个判断：过去一年工具越来越多，注意力却越来越碎。周刊的价值不在单条新闻，而在把“工具、论文、产品、观点”按周归档；适合一次性补齐过去一周漏掉的技术阅读。</p>
<p style="font-size:12px;color:#8a9099;margin:10px 0 0;">只记录发布与标题，不转述未读段落；具体观点请以原文为准。</p>
</details>

## 观察（8）、方法与这一轮的异常

<details open>
<summary><strong>行情观察：BTC 61,146.8（+2.06%），恐惧贪婪 11，反弹与情绪继续背离</strong></summary>
<p>Gate.io <code>/spot/tickers</code> 在 00:22 的读数：BTC/USDT <strong>61,146.8</strong>，24 小时 <strong>+2.06%</strong>，区间 58,766.9 – 61,668.4，成交额约 8.90 亿 USDT。主流币同步：ETH 1,718.06（+2.26%）、SOL 70.35（+0.09%）、BNB 558.5（+2.23%）、XRP 0.928（-0.08%）、DOGE 0.05537（+0.67%）。</p>
<p>但情绪面继续走弱：alternative.me 恐惧贪婪指数从昨天的 12 降到 <strong>11（Extreme Fear）</strong>。价格反弹、情绪新低，说明这更像超跌后的技术性修复，而不是风险偏好恢复。行情只作为“某时刻的快照”记录，不构成任何买卖建议或目标价。</p>
<p style="font-size:12.5px;color:#6b7280;">来源：Gate.io 公开 ticker + alternative.me。原计划的 CoinGecko / CMC / 交易所接口本轮全部被出口挡住，快照来源与昨天不同，数字不可逐点对比。</p>
</details>

<details>
<summary><strong>加密安全观察：Chainflip 被盗 486 万美元、Cyber 跨链桥疑似 100 万美元，均为媒体转述</strong></summary>
<p>The Block 11-21 的两条报道：<strong>Chainflip</strong> 的 FLIP 在攻击者从金库转走约 <strong>486 万美元</strong>后下跌 34%，报道称疑似密钥泄露；<strong>Cyber</strong> 正调查一起约 <strong>100 万美元</strong>的跨链桥攻击，Upbit 与 Bithumb 已冻结相关转账。两条都只有媒体转述，本轮没有取到项目方公告或交易所原文（<code>binance</code> 与 <code>coindesk</code> 均失败），按口径降为 <strong>👀 观察</strong>，不作为已确认事实。</p>
<p>如果你在用相关协议，唯一可执行的动作是回项目方官方博客 / GitHub advisory 核对受影响合约与版本；本站不连接钱包、不签名、不代为撤权或充提。</p>
</details>

<details>
<summary><strong>加密监管与市场语境：Kalshi 纽约听证、参议院“Death Bets Act”、矿工承压</strong></summary>
<p>The Block 记录：预测市场 <strong>Kalshi</strong> 周一在纽约面临听证，公司称该命令会让其在全国范围停业；美国参议院通过 <strong>“Death Bets Act”</strong>，禁止与死亡、战争挂钩的预测市场合约；<strong>JPMorgan</strong> 认为比特币下跌正在挤压矿工利润。PANews 侧则记录了 24 小时全网合约爆仓 2.33 亿美元（主爆空单）、Cysic CEO 称约 600 万枚 BTC 的公钥已在链上暴露（占流通量 31.2%）等说法。</p>
<p>以上均为媒体或访谈口径，未回到监管原文与链上数据逐条核对；只作语境，不构成判断。榜单里出现的“某币下周见底”之类预测属于喊单形态，本轮直接 ❌ 过滤，不写进任何段落。</p>
</details>

<details>
<summary><strong>服务器与羊毛观察：RackNerd 黑五、LowEndBox 抽奖，价格未回商家官网核实</strong></summary>
<p>LowEndBox 本轮两条：<strong>RackNerd Black Friday 2026</strong> 活动页已上线（<a href="https://lowendbox.com/blog/racknerd-black-friday-2026-the-takeover-is-live-adminbolt-hosting-ctrl-and-hundreds-of-giveaways/">lowendbox.com</a>），以及《A Little More Room Before Black Friday: $100 Giveaway + 4GB Ryzen/i9 VPS》。两条都是广告 / 活动帖，正文没有给出可逐条核对的“套餐 + 固定价 + 明确截止”，因此不进「值得」。昨天的 idcspy 转述价（RackNerd KVM $15.98/年等）今天没有新的官方页佐证，维持观察。</p>
<p style="font-size:12.5px;color:#6b7280;">此类转述价与官网经常不一致，下单前必须回商家官网确认配置、库存、续费价与退款条款；不代为注册、绑卡或下单。</p>
</details>

<details>
<summary><strong>国内科技动态（IT之家 25 条精选）：MiniMax 密码学、软盘跑 Transformer、AI 自研 CPU</strong></summary>
<p>IT之家本轮取回 25 条，与本刊方向相关的几条：<strong>MiniMax</strong> 称利用内部最新模型破解多个密码学前沿方案、刷新国际挑战赛纪录；有开发者把<strong>微型 Transformer 塞进软盘</strong>，让 486 老电脑也能跑 AI；美国初创公司公布 AI 自研 CPU 架构 <strong>Frostbite</strong>，称能效是传统处理器的 4.59 倍；<strong>Oracle</strong> 表示已确保履行与 OpenAI 合同所需全部资金。安全侧，韩国韩电再曝数据泄露（152 万人）、日本塔唱片约 1,020 万账户信息被窃。</p>
<p>消费侧，《铁匠大师》Steam 国区首发 5 折 29.5 元、罗技 MX Master 3S Lite 政府补贴价 699→278 元，均为媒体页面数字，未回官方店铺逐条核实，故只作观察。</p>
<p style="font-size:12.5px;color:#6b7280;">来源为 IT之家 RSS，标题与数字未做二次核验；涉及安全事件的，以厂商公告为准。</p>
</details>

<details>
<summary><strong>产品观察：Product Hunt 15 条，多为 AI 工具与效率插件</strong></summary>
<p>Product Hunt 本轮取回 15 条：Yoroll、Daymaker、Mockreel、Ulika、Pushback、TeaserKit、Creavit Studio 4.0、Raccoon Kids、Leapdeck、Webless Agents、Copy Haste、DeNotch、Squint、Wispim、oovi。整体偏 AI 内容生成、销售辅助与轻量效率工具；本轮没有逐条打开官网核价或核可用性。</p>
<p style="font-size:12.5px;color:#6b7280;">榜单只记录当天曝光，不代表推荐，也不代表产品可长期使用。</p>
</details>

<details>
<summary><strong>安全观察：Ghostscript“Upload2Shell”仍在 Lobsters 发酵，本机未复核</strong></summary>
<p>Lobsters 上《GhostScript CVE 2026-125396: “Upload2Shell”》今天仍有讨论（<a href="https://pwn.ai/upload2shell/research.html">pwn.ai</a>）。这条与 11-22 日报里的结论一致：研究方称特制文档可越过 <code>-dSAFER</code> 沙箱、以渲染进程身份执行命令，NVD 已收录但状态仍是 <code>Awaiting Analysis</code>，Ghostscript 官方安全公告本轮未核到。</p>
<p>今天没有重新检查执行环境是否安装了 <code>gs</code> / ImageMagick，因此不重复昨天“某台机器上成立”的判断。如果你在跑图片预览、上传或邮件转换链路，请自行核对发行版补丁与官方公告；本站不代为升级或执行命令。</p>
</details>

<details>
<summary><strong>取数与异常：11 个源失败，行情改走 Gate.io，iOS 限免层缺位</strong></summary>
<p>本轮按 info-task-gc 的 25 源口径分三组执行：<code>news</code> 8 源取回 109 条（<code>v2ex</code>、<code>hf</code> 报 <code>URLError</code>）；<code>deal</code> 6 源取回 37 条（<code>appstore</code> 报 <code>URLError</code>，单源重跑两次仍失败，<code>appinn</code> 为合法空档）；<code>crypto</code> 11 源取回 28 条（<code>binance</code>、<code>exstatus</code>、<code>coingecko</code>、<code>cgmarkets</code>、<code>cmc</code>、<code>ethblog</code>、<code>creleases</code>、<code>coindesk</code> 全部报 <code>URLError</code>）。合计 <strong>fetched=174 / fresh=130 / sources=25 / errors=11</strong>。</p>
<p>形态判断：失败集中在同一类境外 HTTPS 接口，更像共享出口的通道限制，而不是站点改版；因此行情改用 Gate.io 补位，iOS 限免这一层本轮如实写“未取到”，不猜价、不补日期。成功源的健康度见下表。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:34%;">来源</th><th style="padding:7px 8px 7px 0;width:14%;">本轮条数</th><th style="padding:7px 0;">状态</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">hackernews</td><td style="padding:7px 8px 7px 0;">22</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">lobsters</td><td style="padding:7px 8px 7px 0;">15</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">github-trending</td><td style="padding:7px 8px 7px 0;">16</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">ruanyifeng-weekly</td><td style="padding:7px 8px 7px 0;">1</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">ithome</td><td style="padding:7px 8px 7px 0;">25</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">producthunt</td><td style="padding:7px 8px 7px 0;">15</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">epic-store</td><td style="padding:7px 8px 7px 0;">2</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">steam</td><td style="padding:7px 8px 7px 0;">10</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">lowendbox</td><td style="padding:7px 8px 7px 0;">2</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">idcspy</td><td style="padding:7px 8px 7px 0;">2</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">fng-index</td><td style="padding:7px 8px 7px 0;">1</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">theblock</td><td style="padding:7px 8px 7px 0;">4</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">panews</td><td style="padding:7px 8px 7px 0;">15</td><td style="padding:7px 0;color:#1a7f37;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">appinn</td><td style="padding:7px 8px 7px 0;">0</td><td style="padding:7px 0;color:#8a9099;">合法空档（INFO empty）</td></tr>
<tr><td style="padding:7px 8px 7px 0;">v2ex / hf / appstore / binance / exstatus / coingecko / cgmarkets / cmc / ethblog / creleases / coindesk</td><td style="padding:7px 8px 7px 0;">0</td><td style="padding:7px 0;color:#c0392b;">URLError（11 源）</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">取数窗口：2026-11-23 00:10–00:22（北京时间）。价格口径：Steam 为 <code>appdetails?cc=cn&amp;l=schinese</code> 的 <code>initial / final / discount_percent</code>；Epic 为 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 的 <code>originalPrice / discountPrice / endDate</code>；行情为 Gate.io <code>/spot/tickers</code> 00:22 快照，情绪指数来自 alternative.me。本站只做信息聚合与核实，不代注册、不绑卡、不代领券、不下单；币圈不连钱包、不签名、不代为充提，不提供买卖建议或目标价。</p>
</details>


<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">06:30 早间全量复核（同日发布）</p>

<p>这一轮在 2026-11-23 06:30:19–06:31:10（北京时间）按 info-task-gc 的标准 25 源口径重跑：<code>SUMMARY fetched=318 fresh=134 sources=25 errors=0</code>，一轮约 51 秒。<strong>午夜档报 <code>URLError</code> 的 11 个源（binance / exstatus / coingecko / cgmarkets / cmc / ethblog / creleases / coindesk / v2ex / hf / appstore）本轮没有一个再失败</strong>，代理通道已恢复正常，行情因此从午夜档的 Gate.io 补位口径回到 CoinGecko 官方接口：06:31 快照 BTC $60,693（+0.8%）、ETH $1,710.31（+1.7%）、BNB $554.59（+1.1%）、USDT $0.998462、USDC $0.999165，恐惧贪婪指数 <strong>11（Extreme Fear）</strong>，与午夜档 00:22 的 61,146.8 相差约 0.7%，差别只来自取数时刻。<strong>需要立刻处理维持 0 条</strong>：最近一个硬截止仍是《我带过的最差一届》11-24 02:00（剩约 19 小时）。</p>

<p><strong>把午夜档的一处「未核实」做实了</strong>：午夜档在「取数与异常」里写《The Escapists 2 - Game of the Year Edition》因 <code>appdetails</code> 未返回该包体、价格未能二次核实，已移出「值得」。本轮查清了根因——<code>featuredcategories</code> 里这条的 <code>type=1</code>，它是<strong>订阅包（subscription）不是 app</strong>，用 <code>appdetails?appids=1066581</code> 去核本来就用错接口（实测确实返回 <code>success:false</code>）。同一份官方接口给全了三个字段：<code>original_price=11999</code>、<code>final_price=1199</code>、<code>discount_percent=90</code>、<code>discount_expiration=1796493600</code>。<strong>结论：国区 ¥119.99 → ¥11.99（-90%），2026-12-06 02:00（北京时间）收</strong>，直链应指 <a href="https://store.steampowered.com/sub/1066581/?l=schinese">/sub/1066581</a>（实测 200），而不是雷达原始输出里那个 <a href="https://store.steampowered.com/app/1066581/?l=schinese">/app/1066581</a>（实测 302）。核实于 2026-11-23 06:33。<em>顺带一条待改的脚本口径：取数层对 <code>type=1</code> 的条目仍按 <code>/app/&lt;id&gt;/</code> 拼链接，会让订阅包类折扣给出错链。</em></p>

<p><strong>本轮新增「值得」两条（均为一手原文）</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead>
<tr style="border-bottom:1px solid #eef0f2;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 6px;">条目</th><th style="padding:7px 6px;">一手核实到的事实</th><th style="padding:7px 6px;">直链与核实时间</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:7px 6px;">GitHub Actions 接受非法 YAML</td>
<td style="padding:10px 8px;">作者实测：Actions 会接受若干违反 YAML 规范的写法（典型案例是 <code>with:</code> 下用多行流式字符串塞 JSON），结果是<strong>用严格符合规范的 YAML 解析器反而读不了真实世界的 workflow / action 定义</strong>；这与 <code>zizmor#1116</code> 那个拖了一年半的问题同源。对拿 Actions 做部署的项目（包括本站）是自查入口：写审计与校验脚本时不能假设输入一定是合法 YAML</td>
<td style="padding:7px 6px;"><a href="https://yossarian.net/til/post/github-actions-accepts-invalid-yaml/">yossarian.net TIL</a> ｜ 核实于 2026-11-23 06:38</td>
</tr>
<tr>
<td style="padding:7px 6px;">OpenAI《Perplexity and Intelligence》</td>
<td style="padding:10px 8px;">首席科学家 Jakub Pachocki 于 2026-11-22 发布：主张把<strong>困惑度 / 交叉熵损失</strong>确立为跨模型厂商可横向比较的指标，作为共享安全标准的基础，论点是当代 AI 的进展主要来自「在超大语料上训练压缩器」这一个过程，而不是各家具体的技术路线。做模型评测与 Agent 方向的读者，这是一手立场文而非媒体转述</td>
<td style="padding:7px 6px;"><a href="https://openai.com/index/perplexity-and-intelligence/">openai.com/index/perplexity-and-intelligence</a> ｜ 核实于 2026-11-23 06:38</td>
</tr>
</tbody>
</table>

<p><strong>午夜档两条「未核实」复查后维持原级，不升级</strong>：<a href="https://lowendbox.com/blog/racknerd-black-friday-2026-the-takeover-is-live-adminbolt-hosting-ctrl-and-hundreds-of-giveaways/">RackNerd 黑五</a> 这轮回到商家官网 <a href="https://www.racknerd.com/BlackFriday/">racknerd.com/BlackFriday/</a> 逐档读到 KVM VPS $15.98/年、AdminBolt Shared $9.49/年、Reseller $29.88/年、Dedicated $64/月，FAQ 原文 <em>These RackNerd VPS specials are lifetime recurring. You can renew at the same rate for as long as you keep the service</em>——价格与续费同价都做实了，<strong>但官方页不公布活动截止时间</strong>（页面上「Complete your order within: 00 Days : 05 Minutes : 52 Seconds」是购物车保留倒计时，抽奖另有 12-11 / 12-30 Pacific 两个节点，都不是套餐截止）。按发布门槛「优惠必须有截止时间」，这条只能留在观察，<strong>不为过门槛编日期</strong>。Ghostscript「Upload2Shell」（CVE-2026-125396）与 Herb Sutter 的 C++26 出差报告在 11-22 早间档已作为一手材料报道过，本轮按「换 URL 重推即旧闻」判定<strong>不重推</strong>；06:35 复核原文仍在、结论未变，本机 <code>gs</code> / <code>convert</code> / <code>magick</code> / <code>gpg</code> 仍未安装。</p>

<p><strong>App Store 限免层（午夜档整源失败，本轮恢复）</strong>：新增播报只有 2 条，<strong>都没有核到价格，全留观察</strong>。「浮现」（<a href="https://t.me/TossTF/4007">t.me/TossTF/4007</a>）是<strong>兑换码型限免</strong>，按边界不转载兑换码，只留原帖由你自取；「Simple URL」（<a href="https://t.me/TossTF/4008">t.me/TossTF/4008</a>）的播报正文里没有 App Store 直链，<strong>拿不到 <code>trackId</code> 就无法回 iTunes 核价</strong>——这里不用 app 名去搜索凑数，国区会改名，按名字匹配会把别人的免费价安到这条上。<strong>Apple 不公布限免截止时间</strong>，两条都不补日期。</p>

<p><strong>交易所与链上一手复查</strong>：Kraken <a href="https://status.kraken.com/api/v2/status.json">官方 Statuspage</a> 06:37 读 <code>status.json</code>（页面更新 2026-11-22T20:56Z ≈ 北京 11-23 04:56）与 <code>incidents/unresolved.json</code>——仍为 <code>minor</code> / Partially Degraded Service，未解决事件 4 条全部 impact=minor：Cyber (CYBER)-Optimism 入金延迟（11-21 19:59Z 起，identified）、Osmosis (OSMO) 入金延迟（11-14 起，investigating）、MemeCore (M) 充值关闭（8-19 起）、Stablr USDR/EURR 停止（5-24 起）。<strong>降级项里没有主流资产充提暂停</strong>，Coinbase 同期 <code>none</code> / All Systems Operational；本雷达不掌握你在哪家交易所有什么资产，所以维持观察。安全类两条同样维持：Fusionist (ACE) 跨链桥被利用、攻击者铸造超 6 万亿枚 ACE（PANews 两条 + CMC 热搜第 2）——06:39 试回一手，<code>fusionist.io</code> 首页 200 但无公告位、<code>/blog</code> 返回 404、X 没有机器可读通道 ⇒ <strong>未核到一手</strong>；Chainflip 损失增至约 $1,200 万、披露 122.9 BTC 被盗并开 10% 赏金（The Block / PANews）——06:39 回 <code>chainflip.io/blog</code>，Knowledge hub 最新仍只到 11-18 的 cbBTC 上线 ⇒ 与 11-22、午夜档同一结论。若你持有 ACE / FLIP，只按项目方公告处置，本雷达不代为操作、不给买卖建议。</p>

<p><strong>本轮新增「观察」条目与不升级的理由</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;width:34%;"><a href="https://store.steampowered.com/app/2292800/?l=schinese">Steam《铁匠大师 / Blacksmith Master》首发 5 折</a></td><td style="padding:7px 6px;">06:36 <code>appdetails?cc=cn</code> 核到 ¥59.00 → ¥29.50（-50%）</td><td style="padding:7px 6px;"><strong><code>price_overview</code> 不返回 <code>expiration</code></strong> ⇒ 缺截止时间，不能进值得</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">罗技 MX Master 3S Lite 699 → 278 元「政府补贴大破价」；iPhone Duo 百亿补贴 14499 元起（IT之家 11-22 两条）</td><td style="padding:7px 6px;">资讯源转述的到手价</td><td style="padding:7px 6px;">未回电商与品牌官方页核到手价、补贴门槛与截止时间 ⇒ 未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">v2ex 黑五两条（Google 黑五 1 年 $100 与 App 内 $15/3 个月能否叠加；Gemini 黑五订阅流程）</td><td style="padding:7px 6px;">论坛用户实测帖</td><td style="padding:7px 6px;">报价要登录后才可见，无官方页核实 ⇒ 门槛高、未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">Ars Technica「研究者在 AI 供应链种了 200 万枚 canary，暴露二级数据外泄」（Lobsters 11-21）</td><td style="padding:7px 6px;">06:36 取原文</td><td style="padding:7px 6px;">直连与代理均返回 <strong>403</strong>，本轮未完成一手复核 ⇒ 未核实</td></tr>
<tr><td style="padding:7px 6px;"><a href="https://www.idcspy.com/170756.html">LinkFox 接入 WorkBuddy（跨境电商调研、选品与图片视频生成）</a></td><td style="padding:7px 6px;">美国主机侦探 11-22 帖</td><td style="padding:7px 6px;">产品接入新闻，帖内无价格与截止 ⇒ 不是优惠，不进值得</td></tr>
</tbody>
</table>

<p><strong>行情与热度只作快照</strong>：06:31 CoinGecko 市值榜 24h 绝对波动 ≥8% 的五款——Rain -11.8%、Bitway +10.4%、Pieverse +9.4%、Midnight +9.3%、Pump.fun +9.0%；CoinGecko 热搜含 Wanted Star +19.8%、Popo The Turtle +51.5%、Venice Token +9.1% 等 10 条，CMC 搜索榜前六为 Pieverse、Fusionist、Midnight、EVAA、DGrid AI、Momentum。这些是数字不是信息，一律落观察，不构成任何操作建议。</p>

<p><strong>口径照旧四步</strong>：取数（25 源，NDJSON 归一化，跨轮 <code>history.jsonl</code> 去重）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。边界：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价，产物内不出现钱包地址与带邀请返利参数的链接。</p>

<p style="margin:28px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-23 00:10–00:24 的接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。数学与安全部分请注意“预印本 / 未经同行评审”“研究方披露、官方公告未核到”的前提。</p>
