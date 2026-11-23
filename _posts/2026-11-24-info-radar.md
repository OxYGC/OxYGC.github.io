---
title: "资讯雷达 2026-11-24｜黄仁勋复任英伟达 CEO 点燃美股、Steam《我带过的最差一届》2 小时截止、BTC 回到 6.26 万"
author: OxYGC
date: 2026-11-24 00:15:00 +0800
permalink: /posts/info-radar-2026-11-24/
categories: [Info, Deals]
tags: [资讯雷达, 黄仁勋, 英伟达, Steam黑五, Epic限免, 比特币, GitHub趋势]
description: "2026-11-24 当天第一篇：25 个来源取回 368 条，14 源成功、10 源 URLError、Panews 返回 HTML 异常；行情改用 Gate.io 与 Binance Vision 补位。最重要的一条新闻是黄仁勋被英伟达董事会恢复 CEO 职务，HN 头条 1,494 分，IT之家记录美股开盘 NVDA 涨 32%、市值增加超 1 万亿美元。最近硬截止是 Steam《我带过的最差一届》-35% ¥18.20，11-24 02:00 收，只剩约 2 小时；Epic《深渊之印 / Mark of the Deep》¥55→0 到 11-27 00:00。Steam 黑五 10 款均回读官方榜单，战地风云 5 -95% ¥11.40、双人成行 -80% ¥39.60、FF7 重制版 -82% ¥35.64。BTC 00:00 Gate.io 62,666（+2.81%）、Binance Vision 62,690（+2.85%），恐惧贪婪 11（Extreme Fear）。GitHub Trending 仍是 Agent Skills 占前排，Claude-BugHunter 单日 +2,037 star。"
---

这一轮取数在 2026-11-24 00:00–00:05（北京时间）完成：25 个来源里 14 个取到数据、10 个报错、1 个异常。`SUMMARY fetched=368 sources=25 errors=10 abnormal=1`。异常依旧集中在需要境外 HTTPS 通道的行情与交易所接口——`binance`（api 域）、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`creleases`、`coindesk` 全部报 `URLError / SSL_ERROR_SYSCALL`，`v2ex` 与 `hf` 也没能握手，`panews` 的 RSS 地址这次返回的是 HTML 首页而不是 feed（0 条，按异常单列）。行情因此用 Gate.io 公开 ticker 与 Binance Vision 公共行情双源补位，技术资讯由 HN、Lobsters、GitHub Trending、IT之家、阮一峰与 Product Hunt 支撑。**这是 2026-11-24 当天第一篇；今天若再跑，只会在本文件内更新，不新增文件。**

结论先摆前面：**今天最近的一个硬截止就在约 2 小时后——Steam《我带过的最差一届》-35%（¥28.00 → ¥18.20）11-24 02:00 收。** 免费游戏方面，Epic 本周仍是《深渊之印》（Mark of the Deep，¥55→0）一款限免，11-27 00:00 截止；TerraScape -70%（¥53→¥37.10）到 12-22 00:00。Steam 黑五榜单 10 条全部来自官方 `featuredcategories?cc=cn&l=schinese`，其中战地风云 5（-95%，¥11.40）、双人成行（-80%，¥39.60）、FF7 重制版 INTERGRADE（-82%，¥35.64）是幅度最大的三张；《The Escapists 2 GOTY》在接口里 `type=1` 是**订阅包不是 app**，直链应指 `/sub/1066581`，这点昨天早间档已经纠正，今天榜单再次复现。

真正占据今天资讯头条的不是折扣，而是**黄仁勋被英伟达董事会恢复 CEO 职务**：HN 首页 1,494 分 / 1,276 评论居首，IT之家连续多条跟进，记录美股开盘 NVDA 涨 32%、市值增加超 1 万亿美元，马斯克称“错误已更正”、特朗普发文祝贺。这是可回到公司公告与主流媒体的一手事件，不是论坛转述。技术侧，OpenAI《Perplexity and Intelligence》（651 分）与智谱 GLM-5.4（635 分）仍在 HN 前排；Lobsters 最高分是 Ars Technica 的“AI 供应链 200 万枚 canary、隐私事故浮现”（138 分）。市场侧 BTC 回到 6.26 万、24 小时 +2.8%，但恐惧贪婪指数仍停在 **11（Extreme Fear）**——价格反弹与情绪修复不同步。

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
<td style="padding:9px 8px 9px 0;">Epic《深渊之印 / Mark of the Deep》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-02 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《对马岛之魂 导演剪辑版》-50%、《漫威蜘蛛侠 重制版》-60%</td>
<td style="padding:9px 8px 9px 0;">¥199.00 / ¥165.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2215430/?l=schinese">对马岛</a> · <a href="https://store.steampowered.com/app/1817070/?l=schinese">蜘蛛侠</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-03 / 12-06 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《FF7 重生》区间、《FF7 重制版》-82%；Escapists 2 GOTY 订阅包 -90%</td>
<td style="padding:9px 8px 9px 0;">¥35.64 / ¥11.99</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1462040/?l=schinese">FF7 重制版</a> · <a href="https://store.steampowered.com/sub/1066581/?l=schinese">Escapists 2</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-24 00:00–00:05 官方接口实测：Steam <code>featuredcategories?cc=cn&amp;l=schinese</code>，Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code>。Steam 的 <code>discount_expiration</code> 为 epoch，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（5）

<details open>
<summary><strong>黄仁勋被董事会恢复英伟达 CEO 职务：HN 1,494 分，NVDA 开盘涨 32%、市值增超 1 万亿美元</strong> ｜ <span style="color:#c0392b;font-weight:700;">今日头条</span> ｜ <span style="color:#1a7f37;font-weight:700;">公司与主流媒体一手</span></summary>
<p>英伟达官网新闻稿标题为 <em>NVIDIA Board Reinstates Jensen Huang as President, CEO and Board Director</em>，HN 首页以 <strong>1,494 分 / 1,276 评论</strong>居首，是今天讨论度最高的事件。IT之家在 11-23 14:22–14:41 连续跟进四条：<a href="https://www.ithome.com/1/031/218.htm">英伟达恢复黄仁勋 CEO 职务，马斯克称“错误已更正”</a>、<a href="https://www.ithome.com/1/031/217.htm">黄仁勋恢复 CEO 职务：英伟达美股开盘大涨 32%，市值增加超 1 万亿美元</a>、<a href="https://www.ithome.com/1/031/216.htm">特朗普祝贺黄仁勋重返英伟达</a>。The Block 同日 15:02 的报道也把“比特币、加密资产与科技股同涨”直接归因于这次人事恢复。</p>
<p><strong>怎么读</strong>：这是一条“公司公告 + 主流财经媒体”双重可核的事件，不是社交平台传闻；但“开盘涨 32%”“市值增 1 万亿美元”是 IT之家转述的盘中读数，不是收盘价，也不是投资建议。若你在关注 NVDA 或相关加密资产，请回<a href="https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director">英伟达官方新闻稿</a>与交易所行情自行判断，本站不提供买卖建议或目标价。</p>
</details>

<details open>
<summary><strong>Steam 黑五今晚进入收尾：《我带过的最差一届》2 小时后截止，另外 9 款集中在 12-02 至 12-06</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥11.40 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-24 02:00</span></summary>
<p>榜单由 <code>featuredcategories?cc=cn&amp;l=schinese</code> 返回 10 条，字段为 <code>final_price / original_price / discount_percent / discount_expiration</code>，全部按官方值换算，没有用媒体转述补价。战地风云 5 -95%（¥228→¥11.40）幅度最大，双人成行 -80%（¥198→¥39.60）次之，FF7 重制版 INTERGRADE -82%（¥198→¥35.64）第三。《The Escapists 2 GOTY》是 <code>type=1</code> 的订阅包，<strong>直链用 <code>/sub/1066581</code> 实测 200</strong>，用 <code>/app/1066581</code> 会 302，今天榜单再次复现这一点。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:12%;">折扣</th><th style="padding:6px 8px 6px 0;width:26%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5175310/?l=schinese">我带过的最差一届</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-35%</td><td style="padding:8px 8px 8px 0;">¥18.20 / ¥28.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">11-24 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1238810/?l=schinese">战地风云 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-95%</td><td style="padding:8px 8px 8px 0;">¥11.40 / ¥228.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1551360/?l=schinese">极限竞速：地平线 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥79.20 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2483190/?l=schinese">极限竞速：地平线 6</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-25%</td><td style="padding:8px 8px 8px 0;">¥223.50 / ¥298.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1462040/?l=schinese">FF7 重制版 INTERGRADE</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-82%</td><td style="padding:8px 8px 8px 0;">¥35.64 / ¥198.00</td><td style="padding:8px 0;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1817070/?l=schinese">漫威蜘蛛侠 重制版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥165.60 / ¥414.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2215430/?l=schinese">对马岛之魂 导演剪辑版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-50%</td><td style="padding:8px 8px 8px 0;">¥199.00 / ¥398.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/sub/1066581/?l=schinese">The Escapists 2 GOTY（订阅包）</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥11.99 / ¥119.99</td><td style="padding:8px 0;">12-06 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/4459590/?l=schinese">转运军团 - Slotbound</a></td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 8px 8px 0;">¥37.80 / ¥42.00</td><td style="padding:8px 0;">11-27 02:00</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">榜单价即官方接口返回值；<code>discount_expiration</code> 换算后与北京时间整点对齐，说明这是 Steam 侧的固定活动截止，不是媒体估算。领取与付款前仍请回商店页确认。</p>
</details>

<details open>
<summary><strong>Epic 本周限免仍是《深渊之印 / Mark of the Deep》：¥55→0，11-27 00:00 收；TerraScape -70% 到 12-22</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00</span></summary>
<p>Epic 的 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 返回的 <em>Mark of the Deep</em> 价格结构为 <code>originalPrice=5500</code>（¥55.00）、<code>discountPrice=0</code>，促销区间 <code>2026-11-19T16:00:00Z → 2026-11-26T16:00:00Z</code>，换算北京时间即 <strong>11-20 00:00 至 11-27 00:00</strong>，与本月初以来的口径一致。同一接口里 <em>TerraScape</em> 为 <code>originalPrice=5300</code>、<code>discountPrice=3710</code>（-70%，¥37.10），区间 <strong>11-22 00:00 至 12-22 00:00</strong>。</p>
<p><strong>两点别误读</strong>：其一，本周没有新的限免接档，《火之石 – 放置点击英雄RPG》虽然促销字段存在，但原始价与折扣价都是 <code>0</code>，它是免费游戏而不是限时赠送；其二，《Them's Fightin' Herds》《Model Builder: Complete Edition》《幽灵行者 2》等条目在本接口是原价展示，<strong>不是限免</strong>。Epic 页面对 curl 有 403 风控，链接用官方商店，领取请在浏览器里自行完成。</p>
</details>

<details open>
<summary><strong>行情：BTC 回到 6.26 万、24 小时 +2.8%，但恐惧贪婪仍是 11（Extreme Fear）</strong> ｜ <span style="color:#1a7f37;font-weight:700;">+2.81%</span> ｜ <span style="color:#c0392b;font-weight:700;">CoinGecko / CMC 不可达</span></summary>
<p>CoinGecko、CoinGecko Markets、CoinMarketCap、Kraken / Coinbase Status 本轮全部被境外通道挡住，因此行情改用两个可核的公开接口：<strong>Gate.io <code>/spot/tickers?currency_pair=BTC_USDT</code></strong> 00:00 快照 BTC <strong>62,666</strong>，24 小时 <strong>+2.81%</strong>，区间 60,383.5 – 64,593.8，成交额约 <strong>11.10 亿 USDT</strong>；<strong>Binance Vision <code>/api/v3/ticker/24hr</code></strong> 同一时段 BTC <strong>62,690.29</strong>，24 小时 <strong>+2.852%</strong>，区间 60,386.0 – 64,603.12，成交额约 <strong>16.23 亿 USDT</strong>。两个独立接口相差不到 0.04%，可以作为同一时刻的交叉校验。</p>
<p>情绪侧，alternative.me 恐惧贪婪指数读数为 <strong>11（Extreme Fear）</strong>，时间戳对应 2026-11-23 08:00（北京时间），仍是极度恐惧区间。价格从昨天的 61,146.8 抬到 62,666，涨幅约 2.5%，但情绪没有同步回到中性——<strong>这是价格反弹，不是风险偏好修复</strong>。行情只作时刻记录，不构成买卖建议，也不写支撑位与目标价。</p>
</details>

<details open>
<summary><strong>GitHub Trending：Agent Skills 继续占前排，Claude-BugHunter 单日 +2,037 star，基础设施与桌面工具回榜</strong> ｜ <span style="color:#1a7f37;font-weight:700;">16 条</span> ｜ <span style="color:#8a9099;">00:04 页面读数</span></summary>
<p>今天 <code>github.com/trending?since=daily</code> 抓到 16 条，前四名仍是 Agent / Skills 类：<strong>Claude-BugHunter</strong>（19,172 star，单日 +2,037）、<strong>obra/superpowers</strong>（324,785，+838）、<strong>HKUDS/CLI-Anything</strong>（63,346，+783）、<strong>jingyaogong/minimind</strong>（69,306，+828）。之后是 <strong>firecrawl/firecrawl</strong>（207,601，+920）、<strong>cursor/plugins</strong>（18,718，+395）、<strong>cathrynlavery/diagram-design</strong>（70,778，+624）、<strong>mvanhorn/last30days-skill</strong>（73,244，+790）。</p>
<p>值得注意的是回榜的基础设施与桌面工具：<strong>nginx/nginx</strong>（33,006，+174）、<strong>openvinotoolkit/openvino</strong>（12,227，+183）、<strong>toeverything/AFFiNE</strong>（77,198，+593）、<strong>XiaoYouChR/Ghost-Downloader-3</strong>（16,054，+1,078）。这说明热度不是只往 Agent 一个方向走，但“把软件包成 Agent 可调用的技能/CLI”仍是增长最快的一类。star 数是页面读数，不是官方增量接口。</p>
</details>

## 观察（核不到官方截止或价格，不进「值得」）

<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:32%;">条目</th><th style="padding:7px 8px 7px 0;width:30%;">拿到的事实</th><th style="padding:7px 0;">为什么停在观察</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/google-ai-pro-black-friday-2026/">Google Gemini 黑五五折：AI Pro / Plus 年费 100 / 24 美元</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 05:53 转述</td><td style="padding:7px 0;">未回 Google 官方活动页核地区资格、续费价与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/parallels-desktop-27/">Parallels Desktop 27 黑五 249 元/年</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 02:52</td><td style="padding:7px 0;">未回 Parallels 官方页核截止与版本差异</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://lowendbox.com/blog/racknerd-black-friday-2026-the-takeover-is-live-adminbolt-hosti/">RackNerd 2026 黑五：KVM VPS $15.98/年起</a></td><td style="padding:7px 8px 7px 0;">LowEndBox 11-22；Appinn 11-22 同报</td><td style="padding:7px 0;">官网不公布套餐截止时间，购物车倒计时不是活动截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170845.html">FastComet 黑五：共享主机低至 $1.49/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-23 08:56</td><td style="padding:7px 0;">未回注册商活动页核首年/续费与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170829.html">Zenlayer 黑五：指定独立服务器 5 折、流量 6 折、充 $100 送 $50</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-23 08:21</td><td style="padding:7px 0;">未回 Zenlayer 官方页核适用机型与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170819.html">WPForms 黑五最高 70%：低至 $49.5/年</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-23 07:42</td><td style="padding:7px 0;">未回插件官网核套餐与续费价</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170814.html">TranslatePress 全系 30%：最低 €69.3/年</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-23 07:14</td><td style="padding:7px 0;">同上，未核官方截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170807.html">FriendHosting 黑五：VDS 首期 4 折，€1.20/月起</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-23 05:12</td><td style="padding:7px 0;">“首期”口径需回商家页确认续费价</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/superlist-start/">Superlist：微软 To Do 将关闭后的替代</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 09:33</td><td style="padding:7px 0;">产品新闻，无价格与截止，不是优惠</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/winget-mcp-server/">WinGet 开始支持 MCP：可让 AI 安装 Windows 软件</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 07:19</td><td style="padding:7px 0;">工具更新，非折扣；未回微软官方文档复核</td></tr>
<tr><td style="padding:7px 8px 7px 0;">App Store 新上架免费应用 12 条（Catch &amp; Shoot、斯威奇灵斯、PicMind、MirrorSync、Outa、Tinela、Huddle 等）</td><td style="padding:7px 8px 7px 0;">iTunes 中国区 <code>newapplications</code> 接口 101 条</td><td style="padding:7px 0;">新上架 ≠ 限时免费；Apple 不公布限免截止，不补日期</td></tr>
</tbody></table>

## 资讯面：HN、Lobsters、IT之家、阮一峰与 Product Hunt

<p><strong>HN 首页（00:04 读数）</strong>：除黄仁勋那条居首外，<a href="https://openai.com/index/perplexity-and-intelligence/">OpenAI《Perplexity and Intelligence》</a> 651 分 / 423 评论、<a href="https://z.ai/blog/glm-5.4">智谱 GLM-5.4</a> 635 分 / 238 评论、<a href="https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife">《GTA 6》鸟类田野指南</a> 590 分 / 322 评论；<a href="https://github.com/AFK-surf/xnulinux">XNU Linux：在 Linux 上跑完整 OS X 图形用户态</a> 489 分，<a href="https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/">Masullo on the Riemann Hypothesis</a> 277 分，<a href="https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20">GL.iNet 安全公告 2026-11-20</a> 249 分，<a href="https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/">Yes, 17M lines of Lean is a lot</a> 199 分。</p>

<p><strong>黎曼猜想这条仍要泼冷水</strong>：HN 上的讨论是“Masullo 手稿的 Lean 形式化 / 核验进度”，<strong>形式化核验通过不等于黎曼猜想已被证明</strong>。昨天到今天，这个话题从“Lean verification”换成了 John Baez 的评论文章，热度在降，但结论没变。</p>

<p><strong>Lobsters（按分数）</strong>：<a href="https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/">研究者在 AI 供应链植入 200 万枚 canary，隐私事故浮现</a> 138 分；<a href="https://yossarian.net/til/post/github-actions-accepts-invalid-yaml/">GitHub Actions accepts invalid YAML</a> 73 分；<a href="https://dustycloud.org/blog/gliver-completes-the-guix-desktop/">Gliver completes the Guix desktop</a> 54 分；<a href="https://signal.org/blog/protecting-your-privacy/">Signal is Serious About Protecting Your Privacy</a> 53 分；<a href="https://reiver.link/atproto/falsehoods-programmers-believe/">Falsehoods Programmers Believe About ATProto</a> 39 分。</p>

<p><strong>IT之家（最新条目停在 11-23 15:32）</strong>：除黄仁勋三条外，值得记的有<a href="https://www.ithome.com/1/031/230.htm">《暗黑破坏神 5》职业、装备体系与世界观细节公开（距离发售尚有三年）</a>、<a href="https://www.ithome.com/1/031/229.htm">微信鸿蒙版 8.0.24.19 大版本邀测</a>、<a href="https://www.ithome.com/1/031/219.htm">华为星芒 OSTA O1 Pro 支持 eSIM、最多四号</a>、<a href="https://www.ithome.com/1/031/215.htm">《复仇者联盟 5：毁灭之日》新预告，12 月 16 日内地领先全球上映</a>、<a href="https://www.ithome.com/1/031/214.htm">《GTA 6》首发周末销量近 4500 万份</a>、<a href="https://www.ithome.com/1/031/213.htm">大疆 Osmo Action 6 街拍大师套装 3799 元</a>、<a href="https://www.ithome.com/1/031/212.htm">小鹏图灵世界模型 X-World 升级</a>、<a href="https://www.ithome.com/1/031/210.htm">《群星》DLC《意志之力》Steam 国区 ¥108</a>。以上均为媒体转述，未逐条回官方公告，不进「值得」。</p>

<p><strong>阮一峰周刊</strong>：最新一期是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>（2026-11-20），前两期是第 419 期《机房来了，写字楼走了》、第 418 期《如果科技停止在21世纪初》。周更节奏，本轮只有这 3 条。</p>

<p><strong>Product Hunt</strong>：最新 feed 里可读的有 <a href="https://www.producthunt.com/products/figmamcp">FigmaMCP</a>、<a href="https://www.producthunt.com/products/omi-work">Omi Work</a>、<a href="https://www.producthunt.com/products/open-source-solana-wallet">Open Source Solana Wallet</a>、<a href="https://www.producthunt.com/products/ashwa">Ashwa</a>、<a href="https://www.producthunt.com/products/plango">Plango</a>、<a href="https://www.producthunt.com/products/strict">Strict</a>、<a href="https://www.producthunt.com/products/tesla">Tesla Self-Driving V15</a>、<a href="https://www.producthunt.com/products/naturefunding-org">naturefunding.org</a>。只作产品发现，不评优劣。</p>

## 币圈与安全：媒体面三条主线

<p><strong>与英伟达人事直接联动</strong>：The Block 11-23 15:02 报道 <a href="https://www.theblock.co/news/markets/2026-11-23-bitcoin-crypto-tech-stocks-rally-nvidia-re">Bitcoin, crypto and tech stocks rally as Nvidia reinstates Jensen Huang as CEO; NVDA jumps 30%</a>。同日的资金面还包括：<a href="https://www.theblock.co/news/business/2026-11-23-the-dots-arent-done-michael-saylor-bitcoi">Strategy 再买 457 BTC（约 3000 万美元）</a>、<a href="https://www.theblock.co/news/business/2026-11-23-bitmine-adds-7819-eth-tom-lee-makes-hard-">Bitmine 增持 7,819 ETH</a>、<a href="https://www.theblock.co/news/markets/2026-11-23-defi-development-dfdv-solana-treasury-11-c">DeFi Development 连续 11 周买 SOL，持仓 262 万枚</a>、<a href="https://www.theblock.co/news/business/2026-11-23-ark-buys-146-million-worth-anthropic-sinc">Ark 上周买入 1.46 亿美元 Anthropic 股份并减持 ETH / SOL 质押 ETF</a>。这些是机构持仓新闻，不是买卖建议。</p>

<p><strong>基础设施与监管</strong>：<a href="https://www.theblock.co/news/business/2026-11-23-okxice-launches-tokenized-securities-venu">OKXICE 上线代币化证券场所，首批确认 113 项资产</a>；<a href="https://www.theblock.co/news/business/2026-11-23-visa-launches-experimental-ai-agent-walle">Visa 为符合条件的美国用户推出实验性 AI Agent 钱包</a>；<a href="https://www.theblock.co/news/regulation/2026-11-23-south-korea-to-publish-draft-digital-as">韩国本周将发布综合加密法律框架草案</a>；<a href="https://www.theblock.co/news/deals/2026-11-23-lendingusa-cross-river-bitcoin-backed-loans-">Cross River 与 LendingUSA 推出比特币抵押贷款，最高 25 万美元</a>；<a href="https://www.theblock.co/news/business/2026-11-23-ocbc-straitsx-pilot-stablecoin-payments-4">新加坡 OCBC 与 StraitsX 试点跨境稳定币支付</a>。</p>

<p><strong>安全与矿工</strong>：<a href="https://www.theblock.co/news/ecosystems/2026-11-23-pump-fun-draws-criticism-over-private-k">Pump.fun 在网页端停用外部钱包登录、改为导入私钥，引发批评</a>——涉及私钥的操作请只在官方客户端、核对域名后自行判断，本站不代为操作；<a href="https://www.theblock.co/news/ecosystems/2026-11-23-solo-bitcoin-miner-beats-odds-wins-1910">独立矿工命中区块，获约 19.1 万美元奖励</a>。</p>

<p><strong>PANews 本轮异常</strong>：RSS 地址 <code>panewslab.com/rss</code> 返回的是 Nuxt 渲染的 HTML 首页，不是 XML feed，解析为 0 条，按“异常”单列，不计入 10 个 URLError。Coindesk、The Ethereum Blog、Crypto Releases 同样未被通道放行，因此本轮没有它们的原文。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">取数与异常</p>

<p>本轮按 <code>info-task-gc</code> 的 25 源口径分三组执行，成功 14 源、异常 1 源、报错 10 源，合计 <strong>fetched=368 / sources=25 / errors=10 / abnormal=1</strong>。</p>

<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:14%;">组</th><th style="padding:7px 8px 7px 0;width:50%;">成功</th><th style="padding:7px 0;">失败 / 异常</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">news（8）</td><td style="padding:7px 8px 7px 0;">6 源 / 184 条：hackernews 30、lobsters 25、github-trending 16、ruanyifeng 3、ithome 60、producthunt 50</td><td style="padding:7px 0;color:#c0392b;">v2ex、hf（URLError）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">deal（6）</td><td style="padding:7px 8px 7px 0;">6 源 / 153 条：epic 12、steam 10、appinn 10、lowendbox 20、idcspy 10、appstore 101</td><td style="padding:7px 0;color:#1a7f37;">全绿</td></tr>
<tr><td style="padding:7px 8px 7px 0;">crypto（11）</td><td style="padding:7px 8px 7px 0;">2 源 / 21 条：fng 1、theblock 20</td><td style="padding:7px 0;color:#c0392b;">binance、exstatus、coingecko、cgmarkets、cmc、ethblog、creleases、coindesk（URLError）；panews（返回 HTML，0 条）</td></tr>
</tbody></table>

<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">取数窗口：2026-11-24 00:00–00:05（北京时间）。<code>steam</code> 首次请求超时，单源重试第 2 次成功；行情用 Gate.io 与 Binance Vision 双源补位，两者 24h 涨幅相差 0.042 个百分点。本机没有挂载历史的 <code>history.jsonl</code>，因此本轮未做跨轮 <code>fresh</code> 去重，<code>fetched</code> 为成功源返回条目数之和。</p>

<p><strong>形态判断</strong>：失败的仍集中在同一类境外 HTTPS 接口（Binance 主 API、CoinGecko、CMC、Coindesk、Ethereum Blog、Kraken / Coinbase Status），报错形态为 <code>SSL_ERROR_SYSCALL</code> 或连接超时，而不是站点改版或 4xx；这与 11-20 至 11-23 多轮记录一致，按共享出口的通道限制处理，不据此判断这些站点本身不可用。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">口径与边界</p>

<p><strong>四步口径不变</strong>：取数（25 源，NDJSON 归一化）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写“未核实”）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。边界：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。今天按边界过滤了 idcspy 的“店雷达推荐码 07W7U5 享会员 8 折”一条，原因是正文含推荐/返利参数。</p>

<p>另需如实记一句：<strong>本轮执行环境没有挂载 <code>info-task-gc</code> 技能文件</strong>，因此按仓库既有稿件的 25 源清单与同一口径执行；源名单、四步流程与边界均与 11-23 稿件保持一致，差异只在当天数据与失败源集合。</p>

<p style="margin:28px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-24 00:00–00:05 的接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，不构成任何投资建议；新闻部分请注意“媒体转述”与“公司公告 / 官方接口”的区别。</p>
