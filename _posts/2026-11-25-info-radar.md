---
title: "资讯雷达 2026-11-25｜午间复跑：BTC 下探 58,950、Steam 换榜 Hades 进、HN 头条换成 The Spray Bottle"
author: OxYGC
date: 2026-11-25 00:20:00 +0800
last_modified_at: 2026-11-25 12:06:00 +0800
permalink: /posts/info-radar-2026-11-25/
categories: [Info, Deals]
tags: [资讯雷达, Steam黑五, Epic限免, Hades, 比特币, GitHub趋势, 黄仁勋]
description: "2026-11-25 午间复跑（11:58–12:06，同日第二稿，仅更新本文件）：25 源取回 377 条、14 源成功、10 源失败（9 个 URLError + creleases 410）、PANews 返回 HTML 按异常单列。今天仍无 11-25 当天到期的硬截止，最近是 Epic《深渊之印》¥55→0 于 11-27 00:00 收；Epic 本轮未返回下一档 upcoming。Steam 黑五换榜：Hades II -30% ¥75.60、Hades -75% ¥23.00（均 12-02）、底特律 -90% ¥13.60（12-01）、双人成行 -80% ¥39.60（12-04）。BTC 12:04 Gate.io 59,274.7（-1.73%，低 58,950.1）、Binance Vision 59,281.00（-1.72%），较 00:05 的 59,671.5 再跌 0.66%，恐惧贪婪 13（Extreme Fear）；HN 头条换成 The Spray Bottle 401 分、Quad9 撤出法国 368 分，黄仁勋那条已跌出首页前 10。GitHub Trending Claude-BugHunter 21,679 star、单日 +1,826。"
---

这一轮取数在 2026-11-25 00:02–00:10（北京时间）完成：25 个来源里 14 个取到数据、10 个报错、1 个异常。`SUMMARY fetched=367 sources=25 errors=10 abnormal=1`。失败依旧集中在需要境外 HTTPS 通道的行情与交易所接口——`binance`（api 域）、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`creleases`、`coindesk` 全部报 `URLError / SSL_ERROR_SYSCALL`，`v2ex` 与 `hf` 也没能握手，`panews` 的 RSS 地址这次返回的是 Nuxt 渲染的 HTML 首页而不是 feed（0 条，按异常单列）。行情因此用 Gate.io 公开 ticker 与 Binance Vision 公共行情双源补位，技术资讯由 HN、Lobsters、GitHub Trending、IT之家、阮一峰与 Product Hunt 支撑。**这是 2026-11-25 当天第一篇；今天若再跑，只会在本文件内更新，不新增文件。**

结论先摆前面：**今天没有 11-25 当天到期的硬截止。** 最近的一个到期点是 Epic《深渊之印 / Mark of the Deep》0 元（原价 ¥55.00），**11-27 00:00 收**，按 00:10 计算还剩约 2 天。Steam 黑五当前榜里，底特律 -90%（¥13.60）、霍格沃茨之遗 -90%（¥38.40）、The Escapists 2 GOTY 订阅包 -90%（¥11.99）是幅度最大的三张，截止分别在 12-01、12-08、12-06；《双人成行》-80%（¥39.60）与《极限竞速：地平线 5》-60%（¥79.20）到 12-04。

真正占据今天技术头条的是 **Ladybird 浏览器进入 alpha**：HN 首页 2,264 分 / 549 评论，仅次黄仁勋那条；官方公告标题就是 *Ladybird is now in alpha*。黄仁勋那条继续放大——**Nvidia Reinstates Jensen Huang as CEO** 已升到 **2,719 分 / 3,578 评论**，较昨天 12:07 的 2,274 分 / 3,292 评论继续增长；Yann LeCun 批评 Dario Amodei 的推文 1,897 分 / 1,095 评论居第三。市场侧 BTC **跌破 6 万**：Gate.io 00:05 报 59,671.5（-4.54%），Binance Vision 59,669.72（-4.531%），24 小时低点已到 59,390 附近；恐惧贪婪指数仍是 **11（Extreme Fear）**。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮会过期、或需要你自己动手的条目</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-27 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《深渊之印 / Mark of the Deep》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">12-01 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《底特律：化身为人》-90%、《博德之门 3》-30%</td>
<td style="padding:9px 8px 9px 0;">¥13.60 / ¥187.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1222140/?l=schinese">底特律</a> · <a href="https://store.steampowered.com/app/1086940/?l=schinese">博德之门3</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-04 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《双人成行》-80%、《极限竞速：地平线 5》-60%</td>
<td style="padding:9px 8px 9px 0;">¥39.60 / ¥79.20</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a> · <a href="https://store.steampowered.com/app/1551360/?l=schinese">FH5</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-06 / 12-08 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Escapists 2 GOTY 订阅包 -90%；RDR2 -75%、GTA V 增强版 -56%、霍格沃茨之遗 -90%</td>
<td style="padding:9px 8px 9px 0;">¥11.99 / ¥69.75 / ¥98.56 / ¥38.40</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/sub/1066581/?l=schinese">Escapists 2</a> · <a href="https://store.steampowered.com/app/1174180/?l=schinese">RDR2</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-25 00:02–00:08 官方接口实测：Steam <code>featuredcategories?cc=cn&amp;l=schinese</code>，Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code>。Steam 的 <code>discount_expiration</code> 为 epoch，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（5）

<details open>
<summary><strong>Ladybird 浏览器进入 alpha：HN 2,264 分 / 549 评论，独立引擎从「可编译」走到「可用」</strong> ｜ <span style="color:#1a7f37;font-weight:700;">官方公告</span> ｜ <span style="color:#8a9099;">00:04 读数</span></summary>
<p>Ladybird 官方博客发布 <em>Ladybird is now in alpha</em>，HN 首页以 <strong>2,264 分 / 549 评论</strong>排第二，Lobsters 同日也在首页（108 分 / 48 评论）。这是一个从零编写的独立浏览器引擎项目，alpha 是官方自己给出的阶段标签，不是第三方评测结论。公告本身说明了当前支持范围与已知缺口，<strong>请以官方原文为准</strong>：<a href="https://ladybird.org/posts/alpha/">ladybird.org/posts/alpha</a>。</p>
<p><strong>怎么读</strong>：alpha 意味着可以安装体验、可以反馈 bug，但<strong>不意味着可以替代日常主力浏览器</strong>。本站没有在本地构建或跑分，因此不转载任何「性能超过某内核」的说法；讨论热度（分数与评论）是 HN 页面读数，不等于工程质量结论。</p>
</details>

<details open>
<summary><strong>黄仁勋被英伟达董事会恢复 CEO：HN 升至 2,719 分 / 3,578 评论</strong> ｜ <span style="color:#c0392b;font-weight:700;">今日头条</span> ｜ <span style="color:#1a7f37;font-weight:700;">公司与主流媒体一手</span></summary>
<p>CNBC 报道 <a href="https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html">Nvidia Reinstates Jensen Huang as CEO</a>，HN 首页 <strong>2,719 分 / 3,578 评论</strong>居首，比昨天 12:07 的 2,274 分 / 3,292 评论分别增加 445 分与 286 条评论，热度仍在扩张而非回落。HN 同日还有一条相关讨论 <a href="https://www.kadoa.com/congress/insights/trump-nvidia">《Who in Washington owns and trades Nvidia stock》</a>（231 分 / 115 评论），属于公开持仓数据的整理，不是内幕消息。</p>
<p><strong>怎么读</strong>：这是「公司人事 + 主流财经媒体」双重可核的事件；但盘中涨跌幅、市值增量属于行情读数，会随时间变化，<strong>不是收盘价，也不是投资建议</strong>。若你在关注 NVDA 或相关资产，请回公司公告与交易所行情自行判断，本站不提供买卖建议或目标价。</p>
</details>

<details open>
<summary><strong>Steam 黑五当前榜：底特律 / 霍格沃茨之遗 / Escapists 2 三张 -90%，今天没有当天到期项</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥11.99 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 12-01 02:00</span></summary>
<p>榜单由 <code>featuredcategories?cc=cn&amp;l=schinese</code> 返回 10 条，字段为 <code>final_price / original_price / discount_percent / discount_expiration</code>，全部按官方值换算，没有用媒体转述补价。IT之家 11-24 14:43 的《Steam 新一周销量榜》也提到《EA SPORTS FC 27》5 折登顶全球、《双人成行》2 折登顶国区，可作为侧证，但价格仍以官方接口为准。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:12%;">折扣</th><th style="padding:6px 8px 6px 0;width:26%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1222140/?l=schinese">底特律：化身为人</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥13.60 / ¥136.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">12-01 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/990080/?l=schinese">霍格沃茨之遗</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥38.40 / ¥384.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/sub/1066581/?l=schinese">The Escapists 2 GOTY（订阅包）</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥11.99 / ¥119.99</td><td style="padding:8px 0;">12-06 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1174180/?l=schinese">Red Dead Redemption 2</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-75%</td><td style="padding:8px 8px 8px 0;">¥69.75 / ¥279.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1551360/?l=schinese">极限竞速：地平线 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥79.20 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3240220/?l=schinese">Grand Theft Auto V 增强版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-56%</td><td style="padding:8px 8px 8px 0;">¥98.56 / ¥224.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3768760/?l=schinese">007 初露锋芒</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-50%</td><td style="padding:8px 8px 8px 0;">¥149.00 / ¥298.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2001120/?l=schinese">双影奇境</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-40%</td><td style="padding:8px 8px 8px 0;">¥118.80 / ¥198.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1086940/?l=schinese">博德之门 3</a></td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 8px 8px 0;">¥187.60 / ¥268.00</td><td style="padding:8px 0;">12-01 02:00</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">榜单价即官方接口返回值；<code>discount_expiration</code> 换算后与北京时间整点对齐，说明这是 Steam 侧的固定活动截止，不是媒体估算。《The Escapists 2 GOTY》在接口里是订阅包，直链用 <code>/sub/1066581</code>，用 <code>/app/1066581</code> 会跳转。领取与付款前仍请回商店页确认。</p>
</details>

<details open>
<summary><strong>Epic 本周限免仍是《深渊之印 / Mark of the Deep》：¥55→0，11-27 00:00 收；下一档 11-27 起接 Bread and Fred 与 Eternal Threads</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00</span></summary>
<p>Epic 的 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 返回的 <em>Mark of the Deep</em> 价格结构为 <code>originalPrice=5500</code>（¥55.00）、<code>discountPrice=0</code>，促销区间 <code>2026-11-19T16:00:00Z → 2026-11-26T16:00:00Z</code>，换算北京时间即 <strong>11-20 00:00 至 11-27 00:00</strong>。同一接口里 <em>TerraScape</em> 为 <code>originalPrice=5300</code>、<code>discountPrice=3710</code>（-70%，¥37.10），区间 <strong>11-22 00:00 至 12-22 00:00</strong>。</p>
<p><strong>下一档已经排上，但现在不能领</strong>：接口的 <code>upcomingPromotionalOffers</code> 给出 <em>Bread and Fred</em>（原价 ¥47.00）与 <em>Eternal Threads</em>（原价 ¥62.00）在 <strong>11-27 00:00–12-04 00:00</strong> 的 0 元档期，状态是 SOON。另有 <em>Luftrausers</em> 与 <em>Eternal Threads</em> 出现在 <strong>11-28 00:00–12-01 23:00</strong> 的短档期，属于另一个促销位，同样未开始。按边界只记录档期，不发布「已可领」。Epic 页面对 curl 有 403 风控，链接用官方商店，领取请在浏览器里自行完成。</p>
</details>

<details open>
<summary><strong>行情：BTC 跌破 6 万、24 小时 -4.53%，恐惧贪婪仍是 11（Extreme Fear）</strong> ｜ <span style="color:#c0392b;font-weight:700;">-4.53%</span> ｜ <span style="color:#8a9099;">Gate.io / Binance Vision 双源</span></summary>
<p>CoinGecko、CoinGecko Markets、CoinMarketCap、Binance 主 API 与 Kraken / Coinbase 状态页本轮全部被境外通道挡住，因此行情改用两个可核的公开接口：<strong>Gate.io <code>/spot/tickers?currency_pair=BTC_USDT</code></strong> 00:05 快照 BTC <strong>59,671.5</strong>，24 小时 <strong>-4.54%</strong>，区间 <strong>62,907.1 – 59,392.8</strong>，成交额约 <strong>11.59 亿 USDT</strong>（19,103.65 BTC）；<strong>Binance Vision <code>/api/v3/ticker/24hr</code></strong> 同一时段 BTC <strong>59,669.72</strong>，24 小时 <strong>-4.531%</strong>，区间 <strong>62,906.44 – 59,390.86</strong>，成交额约 <strong>13.12 亿 USDT</strong>（21,631.67 BTC）。两个独立接口相差约 0.003%，可以作为同一时刻的交叉校验。</p>
<p>情绪侧，alternative.me 恐惧贪婪指数读数为 <strong>11（Extreme Fear）</strong>，时间戳对应 2026-11-24 08:00（北京时间），仍停在极度恐惧区间。与昨天 12:05 的 Gate.io 60,438.4（-1.49%）相比，价格<strong>回落约 1.27%</strong>，24 小时涨幅从 -1.49% 扩大到 -4.54%；The Block 同日也以《Bitcoin slips back toward $60,000 as Jensen Huang's Nvidia return rally fizzles》记录这轮回吐。<strong>行情只作时刻记录，不构成买卖建议，也不写支撑位与目标价。</strong></p>
</details>

## 观察（核不到官方截止或价格，不进「值得」）

<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:32%;">条目</th><th style="padding:7px 8px 7px 0;width:30%;">拿到的事实</th><th style="padding:7px 0;">为什么停在观察</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/google-ai-pro-black-friday-2026/">Google Gemini 黑五五折：AI Pro / Plus 年费 100 / 24 美元</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 05:53 转述</td><td style="padding:7px 0;">未回 Google 官方活动页核地区资格、续费价与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/parallels-desktop-27/">Parallels Desktop 27 黑五 249 元/年</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-23 02:52</td><td style="padding:7px 0;">未回 Parallels 官方页核截止与版本差异</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://lowendbox.com/blog/racknerd-black-friday-2026-the-takeover-is-live-adminbolt-hosting-ctrl-and-hundreds-of-giveaways/">RackNerd 2026 黑五：抽奖 + VPS 促销仍在进行</a></td><td style="padding:7px 8px 7px 0;">LowEndBox 11-22、11-24 两篇</td><td style="padding:7px 0;">官网不公布套餐截止时间，购物车倒计时不是活动截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170919.html">UltaHost 黑五：主机及 VPS 最高 70% 折扣，低至 $2.01/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 08:21</td><td style="padding:7px 0;">未回 UltaHost 官方页核机型、续费价与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170888.html">Just Hosting 黑五：VPS 全场五折，自定义配置 / 38 节点</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 05:50</td><td style="padding:7px 0;">未回商家活动页核首期与续费口径</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170870.html">荫云 YINNET 黑五：VPS 全场 5 折，低至 $3/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 05:20</td><td style="padding:7px 0;">「新购续费同享」需回官方页复核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170872.html">HostEase 黑五：Windows 主机首年 5 折，美国 VPS $26.28/年起</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 04:05</td><td style="padding:7px 0;">未核高防服务器起价与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170915.html">Post Affiliate Pro 黑五：月付前 6 个月 5 折，年付低至 $19.75/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 08:05</td><td style="padding:7px 0;">未回官网核套餐与续费价</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170861.html">NovixLink 美国 Cogent 双 ISP 住宅 IP VPS 补货</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 02:23</td><td style="padding:7px 0;">补货消息，无固定折扣截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/upload2shell-cve-2026-125396/">Upload2Shell 高危漏洞公开：CVE-2026-125396，8.5 分</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-24 03:08</td><td style="padding:7px 0;">安全公告，不是优惠；未回 NVD / 厂商公告复核影响面</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.appinn.com/windows-11-new-native-search/">Windows 11 全新系统搜索：更快、更省内存</a></td><td style="padding:7px 8px 7px 0;">Appinn 11-24 05:55</td><td style="padding:7px 0;">功能更新，非折扣；未回微软官方文档复核</td></tr>
<tr><td style="padding:7px 8px 7px 0;">App Store 新上架免费应用 101 条（Catch &amp; Shoot、斯威奇灵斯、PicMind、MirrorSync、Outa、Tinela 等）</td><td style="padding:7px 8px 7px 0;">iTunes 中国区 <code>newapplications</code> 接口 101 条</td><td style="padding:7px 0;">新上架 ≠ 限时免费；Apple 不公布限免截止，不补日期</td></tr>
</tbody></table>

## 资讯面：HN、Lobsters、IT之家、阮一峰与 Product Hunt

<p><strong>HN 首页（00:04 读数）</strong>：除黄仁勋与 Ladybird 两条外，<a href="https://twitter.com/ylecun/status/2124550037912920090">Yann LeCun：“Dario is hyping the dangers so OSS models are illegal and he stays in control”</a> 1,897 分 / 1,095 评论居第三；其后是 <a href="https://spelunkr.tv">用 Internet Archive 老视频搭的免费替代电视网</a> 1,053 分 / 178 评论、<a href="https://fzakaria.com/2026/11/23/2035-came-early">2035 came early</a> 633 分 / 239 评论、<a href="https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-signs-bill-restricting-exploitative-vehicle-subscription">纽约州禁止汽车订阅费与购后附加费</a> 609 分 / 285 评论、<a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart 成为 Microsoft Exchange 的 drop-in 替代</a> 607 分 / 312 评论、<a href="https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/">LLM agents work for their parent companies, not for you</a> 488 分 / 211 评论、<a href="https://github.com/zed-industries/gpui">GPUI 独立成仓库</a> 343 分 / 121 评论。</p>

<p><strong>Lobsters（按分数）</strong>：<a href="https://signal.org/blog/protecting-your-privacy/">Signal is Serious About Protecting Your Privacy</a> 115 分；<a href="https://ladybird.org/posts/alpha/">Ladybird is now in alpha</a> 108 分；<a href="https://yossarian.net/til/post/github-actions-accepts-invalid-yaml/">GitHub Actions accepts invalid YAML</a> 82 分；<a href="https://fzakaria.com/2026/11/23/2035-came-early">2035 came early</a> 62 分；<a href="https://sneakernet.eu/">Sneakernet</a> 37 分；<a href="https://news.uq.edu.au/2026-11-uq-researchers-send-unblockable-message-using-gravity">昆士兰大学用引力发送「不可屏蔽」消息</a> 34 分；<a href="https://www.friedgil.com/vpvnp/">What VP != VNP Means (In 3 Minutes)</a> 34 分。</p>

<p><strong>IT之家（最新条目停在 11-24 15:17 GMT，即北京 11-24 23:17）</strong>：值得记的有<a href="https://www.ithome.com/1/031/891.htm">鸿蒙系统终端设备数破亿，开发者超 1200 万</a>、<a href="https://www.ithome.com/1/031/888.htm">Steam 新一周销量榜：《EA SPORTS FC 27》5 折登顶全球、《双人成行》2 折登顶国区</a>、<a href="https://www.ithome.com/1/031/892.htm">微软 Win11 将淘汰蓝牙 MTP 功能</a>、<a href="https://www.ithome.com/1/031/883.htm">华为 Mate X8 通信能力公开，支持星闪 E2.0、eSIM、北斗卫星消息</a>、<a href="https://www.ithome.com/1/031/887.htm">拓竹发布 3D 打印机 P3C，国补到手价 6374.2 元起</a>、<a href="https://www.ithome.com/1/031/882.htm">比亚迪与英力士就收购法国汉巴赫工厂展开独家谈判</a>、<a href="https://www.ithome.com/1/031/885.htm">NASA 好奇号与毅力号在火星接连发现奇特岩石</a>。以上均为媒体转述，未逐条回官方公告，不进「值得」。</p>

<p><strong>阮一峰周刊</strong>：最新一期仍是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>（feed 更新时间 2026-11-24 14:36 北京时间），前两期是第 419 期《机房来了，写字楼走了》、第 418 期《如果科技停止在21世纪初》。周更节奏，本轮只有这 3 条。</p>

<p><strong>Product Hunt</strong>：最新 feed 里可读的有 <a href="https://www.producthunt.com/products/astrolabio">Astrolabio</a>、<a href="https://www.producthunt.com/products/claude-code">Claude Ship</a>、<a href="https://www.producthunt.com/products/viktor">Viktor Code</a>、<a href="https://www.producthunt.com/products/willow-voice">Willow iOS 2.0</a>、<a href="https://www.producthunt.com/products/kodak-slidetag">Kodak SlideTag</a>、<a href="https://www.producthunt.com/products/tday">tday.com</a>、<a href="https://www.producthunt.com/products/mystonie">Mystonie</a>、<a href="https://www.producthunt.com/products/rotara">Rotara</a>。只作产品发现，不评优劣。</p>

## 币圈与安全：ETF 资金流出与安全团队扩编

<p><strong>资金面</strong>：The Block 记录 <a href="https://www.theblock.co/news/markets/2026-11-24-bitcoin-etfs-another-570-million-net-outflows-november-total-nears-5-billion-btc-dips-below-60k-445548">现货比特币 ETF 再净流出 5.7 亿美元，11 月累计接近 50 亿美元，BTC 跌破 6 万</a>；同日 <a href="https://www.theblock.co/news/markets/2026-11-24-bitcoin-60000-jensen-huang-fizzles-445472">BTC 随黄仁勋复任行情的退潮回落至 6 万附近</a>。机构侧还有 <a href="https://www.theblock.co/news/business/2026-11-24-ethereum-treasury-firm-btcs-sells-43-8-million-eth-cut-aave-debt-ceo-says-we-do-not-take-this-lightly-445562">ETH 财库公司 BTCS 卖出 4,380 万美元 ETH 偿还 Aave 债务</a>、<a href="https://www.theblock.co/newsletters/the-daily/2026-11-24-doj-binance-hack-strategy-bitcoin-more-crypto-news-445430">美国司法部追索与 Binance 被盗案相关的 11.7 亿美元，Strategy 再买 457 BTC</a>。这些是机构持仓与资金流向新闻，不是买卖建议。</p>

<p><strong>基础设施与监管</strong>：<a href="https://www.theblock.co/news/business/2026-11-24-blackrock-opens-tokenized-money-market-fund-with-100-million-in-assets-to-hong-kong-investors-445524">BlackRock 向香港投资者开放 1 亿美元规模的代币化货币市场基金</a>；<a href="https://www.theblock.co/news/business/2026-11-24-ledn-launches-us-custody-account-bitcoin-gold-stablecoins-lending-445411">Ledn 在美国推出可持有、兑换与抵押借贷的托管账户</a>；<a href="https://www.theblock.co/news/markets/2026-11-24-neuberger-berman-tokenized-hinc-fund-aave-horizon-collateral-445391">Neuberger Berman 的 HINC 基金接入 Aave 机构借贷</a>；<a href="https://www.theblock.co/news/regulation/2026-11-24-south-korea-new-crypto-bill-445494">韩国加密法案草案为本土 ICO 开路，交易所股东持股上限 20%</a>；<a href="https://www.theblock.co/news/regulation/2026-11-23-kalshi-pauses-operations-utah-dodging-ban-new-york-445456">Kalshi 暂停犹他州业务，在纽约暂避禁令</a>。</p>

<p><strong>安全</strong>：<a href="https://www.theblock.co/news/ecosystems/2026-11-24-ethereum-foundation-doubles-protocol-security-team-calls-ai-a-more-urgent-risk-than-quantum-445497">以太坊基金会将协议安全团队扩编一倍，称 AI 是比量子计算「更紧迫的风险」</a>；技术面另有 Appinn 转述的 <a href="https://www.appinn.com/upload2shell-cve-2026-125396/">Upload2Shell（CVE-2026-125396，8.5 分）</a>，称特制图片上传即可入侵服务器。涉及上传链路与私钥的操作，请回官方公告与发行版补丁自行核对，本站不代为升级或执行命令。</p>

<p><strong>PANews 本轮异常</strong>：RSS 地址 <code>panewslab.com/rss</code> 返回的是 Nuxt 渲染的 HTML 首页（重定向到 <code>/zh/rss</code>，约 106 KB、<code>text/html</code>），不是 XML feed，解析为 0 条，按「异常」单列，不计入 10 个 URLError。Coindesk、The Ethereum Blog、Crypto Releases 同样未被通道放行，因此本轮没有它们的原文。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">取数与异常</p>

<p>本轮按 <code>info-task-gc</code> 的 25 源口径分三组执行，成功 14 源、异常 1 源、报错 10 源，合计 <strong>fetched=367 / sources=25 / errors=10 / abnormal=1</strong>。</p>

<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:14%;">组</th><th style="padding:7px 8px 7px 0;width:50%;">成功</th><th style="padding:7px 0;">失败 / 异常</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">news（8）</td><td style="padding:7px 8px 7px 0;">6 源 / 183 条：hackernews 29、lobsters 25、github-trending 16、ruanyifeng 3、ithome 60、producthunt 50</td><td style="padding:7px 0;color:#c0392b;">v2ex、hf（URLError）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">deal（6）</td><td style="padding:7px 8px 7px 0;">6 源 / 163 条：epic 12、steam 10、appinn 10、lowendbox 20、idcspy 10、appstore 101</td><td style="padding:7px 0;color:#1a7f37;">全绿</td></tr>
<tr><td style="padding:7px 8px 7px 0;">crypto（11）</td><td style="padding:7px 8px 7px 0;">2 源 / 21 条：fng 1、theblock 20</td><td style="padding:7px 0;color:#c0392b;">binance、exstatus、coingecko、cgmarkets、cmc、ethblog、creleases、coindesk（URLError）；panews（返回 HTML，0 条）</td></tr>
</tbody></table>

<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">合计 <code>367 = 183 + 163 + 21</code>；取数窗口 2026-11-25 00:02–00:10（北京时间）。<code>appstore</code> 本轮返回国区新上架 101 条，是「新上架」而不是限免价格层，因此不据此判断任何 App 是否限免。行情用 Gate.io 与 Binance Vision 双源补位，两者 24 小时涨幅相差约 0.009 个百分点。本机没有挂载历史的 <code>history.jsonl</code>，因此本轮未做跨轮 <code>fresh</code> 去重，<code>fetched</code> 为成功源返回条目数之和。</p>

<p><strong>形态判断</strong>：失败的仍集中在同一类境外 HTTPS 接口（Binance 主 API、CoinGecko、CMC、Coindesk、Ethereum Blog、Crypto Releases、Kraken / Coinbase Status），报错形态为 <code>SSL_ERROR_SYSCALL</code> 或连接超时，而不是站点改版或 4xx；这与 11-20 至 11-24 多轮记录一致，按共享出口的通道限制处理，不据此判断这些站点本身不可用。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">口径与边界</p>

<p><strong>四步口径不变</strong>：取数（25 源，NDJSON 归一化）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。边界：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。今天按边界过滤了 idcspy 的推荐 / 返利类帖子，不转载带推荐码的内容。</p>

<p>另需如实记两句：<strong>本轮执行环境没有挂载 <code>info-task-gc</code> 技能文件</strong>，因此按仓库既有稿件的 25 源清单与同一口径执行，源名单、四步流程与边界均与 11-23 / 11-24 稿件一致，差异只在当天数据与失败源集合；<strong>GitHub 连接器也未以 MCP 形式挂载</strong>，仓库读写通过既有 git 凭据与 <code>origin/main</code> 远端完成。</p>

<p style="margin:28px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-25 00:02–00:10 接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，不构成任何投资建议；新闻部分请注意「媒体转述」与「公司公告 / 官方接口」的区别。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">12:05 午间增量复核（同日发布）</p>

<p>这一轮在 2026-11-25 11:58–12:06（北京时间）按 <code>info-task-gc</code> 的 25 源口径复跑：<code>SUMMARY fetched=377 sources=25 success=14 errors=10 abnormal=1</code>。失败仍是同一类境外 HTTPS 接口：<code>v2ex</code>、<code>hf</code>、<code>binance</code>（api 主域）、<code>exstatus</code>、<code>coingecko</code>、<code>cgmarkets</code>、<code>cmc</code>、<code>ethblog</code>、<code>coindesk</code> 全部报 <code>URLError</code>，<code>creleases</code> 这次直接返回 <code>410</code>（源已下线）；<code>panews</code> 的 <code>/rss</code> 仍是 Nuxt 渲染的 HTML 首页（106,360 字节、<code>text/html</code>，0 条，按异常单列）。Epic 旧静态域仍连不上，改用官方 ipv4 静态域成功取到 12 条。行情继续用 Gate.io 与 Binance Vision 双源补位。<strong>今天仍只有这一篇，本次只在原文件内追加，不新增文件。</strong></p>

<p><strong>先处理旧结论：</strong>00:20 首稿「今天没有 11-25 当天到期的硬截止」依然成立。最近一个是 Epic《深渊之印 / Mark of the Deep》0 元（原价 ¥55.00），本轮接口确认促销区间仍是 <strong>11-20 00:00 → 11-27 00:00</strong>，按 12:06 计算还剩约 1 天 12 小时。下一档《Bread and Fred》（¥47）与《Eternal Threads》（¥62）在本轮 <code>upcomingPromotionalOffers</code> 里<strong>没有返回</strong>，两条都还是原价、无促销字段，因此不再沿用首稿「11-27 起接档」的表述，等接口给出档期再记。</p>

<p><strong>Steam 黑五换榜：Hades 与 Hades II 进榜，霍格沃茨之遗、The Escapists 2、极限竞速：地平线 5 退出当前十格。</strong> 10 条全部来自 <code>featuredcategories?cc=cn&amp;l=schinese</code>，<code>final_price / original_price / discount_percent / discount_expiration</code> 按官方值换算，<code>discount_expiration</code> 的 epoch 已换算为北京时间（UTC+8）。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:10%;">折扣</th><th style="padding:6px 8px 6px 0;width:24%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1222140/?l=schinese">底特律：化身为人</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥13.60 / ¥136.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">12-01 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1145360/?l=schinese">Hades</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-75%</td><td style="padding:8px 8px 8px 0;">¥23.00 / ¥92.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1145350/?l=schinese">Hades II</a></td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 8px 8px 0;">¥75.60 / ¥108.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2483190/?l=schinese">极限竞速：地平线 6</a></td><td style="padding:8px 8px 8px 0;">-25%</td><td style="padding:8px 8px 8px 0;">¥223.50 / ¥298.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2001120/?l=schinese">双影奇境</a></td><td style="padding:8px 8px 8px 0;">-40%</td><td style="padding:8px 8px 8px 0;">¥118.80 / ¥198.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1174180/?l=schinese">Red Dead Redemption 2</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-75%</td><td style="padding:8px 8px 8px 0;">¥69.75 / ¥279.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3240220/?l=schinese">Grand Theft Auto V 增强版</a></td><td style="padding:8px 8px 8px 0;">-56%</td><td style="padding:8px 8px 8px 0;">¥98.56 / ¥224.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3768760/?l=schinese">007 初露锋芒</a></td><td style="padding:8px 8px 8px 0;">-50%</td><td style="padding:8px 8px 8px 0;">¥149.00 / ¥298.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1086940/?l=schinese">博德之门 3</a></td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 8px 8px 0;">¥187.60 / ¥268.00</td><td style="padding:8px 0;">12-01 02:00</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">与 00:20 首稿相比，底特律 / RDR2 / GTA V / 双人成行 / 博德 3 / 007 / 双影奇境仍在，霍格沃茨之遗、Escapists 2、FH5 下榜，Hades 与 Hades II 新进。榜单是「当前折扣位」而不是资产清单，进榜不代表史低；截止时间只认 <code>discount_expiration</code>。</p>

<p><strong>Epic 当前档：</strong>《深渊之印 / Mark of the Deep》<code>originalPrice=5500</code>、<code>discountPrice=0</code>，区间 11-20 00:00–11-27 00:00；《TerraScape》¥53.00 → ¥37.10（-70%），区间 11-22 00:00–12-22 00:00。《火之石 – 放置点击英雄RPG》是 <code>0 → 0</code> 的长期免费本体，不按限免记。Epic 页面对 curl 有 403 风控，链接用官方商店，领取请在浏览器里自行完成。</p>

<p><strong>行情：BTC 再下探，24 小时低点跌到 58,950。</strong> Gate.io <code>/spot/tickers</code> 12:04 快照 BTC/USDT <strong>59,274.7</strong>，24 小时 <strong>-1.73%</strong>，区间 <strong>60,773.3 – 58,950.1</strong>，成交额约 <strong>9.93 亿 USDT</strong>；Binance Vision <code>/api/v3/ticker/24hr</code> 同一时段 BTC <strong>59,281.00</strong>、<strong>-1.722%</strong>、区间 <strong>60,768.56 – 58,952.48</strong>、成交额约 <strong>11.27 亿 USDT</strong>，两源相差约 0.01%。ETH <strong>1,660.77</strong>（-2.09%）、BNB <strong>542.30</strong>（-1.79%）。与 00:05 的 Gate.io 59,671.5 相比<strong>再跌约 0.66%</strong>，24 小时低点从 59,392.8 下移到 58,950.1。alternative.me 恐惧贪婪指数为 <strong>13（Extreme Fear）</strong>，时间戳 2026-11-25 08:00（北京时间），仍处极度恐惧区间。<strong>行情只作时刻记录，不构成买卖建议。</strong></p>

<p><strong>HN 头条换人：</strong>12:04 首页读数，<a href="https://mechanical-pencil.com/products/spray-bottle">The Spray Bottle</a> <strong>401 分 / 104 评论</strong>居首，<a href="https://prismml.com/news/bonsai-2-5-27b">Ternary Bonsai 2.5 27B</a> 372 分 / 127 评论，<a href="https://quad9.net/news/blog/quad9-service-deactivation-in-france/">Quad9 撤出法国 DNS 服务</a> 368 分 / 222 评论，<a href="https://twitter.com/raul_bs3/status/2125213756238291075">GTA 6 在 Windows 上运行</a> 317 分 / 410 评论，<a href="https://hypercritical.co/2026/11/23/jetty-pro">Jetty Pro</a> 287 分，<a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">针对 Check Point 管理服务器的在野入侵</a> 271 分，<a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">矩阵乘法指数 Θ(n^2.25) 预印本</a> 248 分，<a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 展现蛋白质设计能力</a> 203 分。<strong>首稿里 2,719 分的黄仁勋那条已跌出首页前 10</strong>，属热度回落，不代表被删除。Check Point 那条是安全厂商博客，涉及管理面暴露，<strong>只按厂商公告与自有资产自查处理</strong>，本站不代为扫描或执行命令。</p>

<p><strong>Lobsters：</strong><a href="https://ladybird.org/posts/alpha/">Ladybird is now in alpha</a> 116 分 / 65 评论；<a href="https://fzakaria.com/2026/11/23/2035-came-early">2035 came early</a> 97 分；<a href="https://s.conao3.com/blog/2026/e4f733">用 Lean 检查 Clojure core，发现 17 个未上报 bug</a> 62 分；<a href="https://hex.pm/blog/security-incident-on-hexpm">Hex.pm 安全事件</a> 47 分；其后是 <a href="https://mastodon.social/@pervognsen/117668394962974183">AVX-512 对词法解析的影响</a> 28 分、<a href="https://wheybags.com/blog/pokemon_childhood_version.html">Pokemon Childhood Version</a> 24 分、<a href="https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/">iOS 仍无 WebKit 之外浏览器</a> 19 分。</p>

<p><strong>GitHub Trending（12:04 抓取 16 条）</strong>：star 与「今日新增」均为页面读数，不是官方增量接口。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:40%;">仓库</th><th style="padding:7px 8px 7px 0;width:18%;">12:04 总 star</th><th style="padding:7px 8px 7px 0;width:16%;">今日新增</th><th style="padding:7px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">elementalsouls/Claude-BugHunter</td><td style="padding:7px 8px 7px 0;">21,679</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,826</td><td style="padding:7px 0;">Claude Code 漏洞狩猎技能包</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">XiaoYouChR/Ghost-Downloader-3</td><td style="padding:7px 8px 7px 0;">17,521</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,092</td><td style="padding:7px 0;">桌面下载器</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">HKUDS/CLI-Anything</td><td style="padding:7px 8px 7px 0;">64,963</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,074</td><td style="padding:7px 0;">把软件做成 Agent 可调用的 CLI</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">obra/superpowers</td><td style="padding:7px 8px 7px 0;">325,927</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,003</td><td style="padding:7px 0;">Agentic skills 框架</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">firecrawl/firecrawl</td><td style="padding:7px 8px 7px 0;">209,076</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+991</td><td style="padding:7px 0;">Agent 抓取 / 搜索基础设施</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">zhouxiaoka/autoclip</td><td style="padding:7px 8px 7px 0;">15,526</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+980</td><td style="padding:7px 0;">长视频一键剪短视频</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">mjmirza/app-store-compliance</td><td style="padding:7px 8px 7px 0;">5,950</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+928</td><td style="padding:7px 0;">App Store 合规检查</td></tr>
<tr><td style="padding:7px 8px 7px 0;">cathrynlavery/diagram-design</td><td style="padding:7px 8px 7px 0;">72,217</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+802</td><td style="padding:7px 0;">图表 / 版式设计资源</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">其余进榜：mvanhorn/last30days-skill（74,354，+703）、jingyaogong/minimind（70,397，+727）、toeverything/AFFiNE（78,062，+584）、google-labs-code/stitch-skills（12,724，+403）、Tracer-Cloud/opensre（15,234，+398）、cursor/plugins（19,281，+360）、openvinotoolkit/openvino（12,497，+185）、nginx/nginx（33,244，+158）。与 00:20 档比较，Claude-BugHunter 从 20,945 涨到 21,679（+734），Agent Skills 与下载 / 剪辑工具仍占前排。</p>

<p><strong>国内与产品面（媒体转述，不进「值得」）</strong>：IT之家最新条目到 11-25 11:58（北京时间），值得记的有<a href="https://www.ithome.com/1/032/017.htm">神舟二十四号与空间站完成自主快速交会对接</a>、<a href="https://www.ithome.com/1/032/015.htm">卢伟冰称 Q3 是从业以来最难的一个季度</a>、<a href="https://www.ithome.com/1/031/989.htm">OpenAI 把新金矿瞄向「防黑客」</a>、<a href="https://www.ithome.com/1/031/990.htm">《原始袭变》2027-09-29 停服、明年 3 月停售</a>、<a href="https://www.ithome.com/1/031/988.htm">《GTA6》曼迪演员回应走红</a>。阮一峰最新仍是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>。Product Hunt 最新可读的有 SparrowDesk Phone Calls、Viktor Code、Claude Ship、distribution.dev、Juncts、Mystonie、Willow iOS 2.0、tday.com。Appinn 本轮新增 <a href="https://www.appinn.com/koofr-1tb/">Koofr 终身 1TB 特价</a>，另有 Windows 11 原生搜索、Upload2Shell、WinGet MCP 等在列。</p>

<p><strong>币圈媒体面</strong>：The Block 12:04 的 20 条里，值得记的是<a href="https://www.theblock.co/news/regulation/2026-11-24-utah-moves-to-drop-criminal-charges-kalshi-446090">犹他州在 Kalshi 暂停后拟撤销刑事指控</a>、<a href="https://www.theblock.co/news/regulation/2026-11-24-new-york-proposal-prediction-market-tax-446082">纽约州参议员提议对预测市场手续费征 10% 税</a>、<a href="https://www.theblock.co/news/business/2026-11-24-bitcoin-miner-cleanspark-swings-987-million-annual-loss-btc-production-declines-446061">矿企 CleanSpark 年亏 9.87 亿美元</a>、<a href="https://www.theblock.co/news/regulation/2026-11-24-sec-staff-gives-molecule-no-action-relief-scientific-research-tokens-446067">SEC 工作人员给 Molecule 科研代币无异议函</a>、<a href="https://www.theblock.co/news/business/2026-11-24-kraken-krak-early-2027-launch-us-credit-cards-bitcoin-cashback-usdc-collateral-445498">Kraken 旗下 Krak 拟 2027 年初在美发信用卡</a>、<a href="https://www.theblock.co/news/regulation/2026-11-24-rep-raskin-probes-trump-jr-s-firms-investments-polymarket-juul-suspiciously-well-timed-government-favors-446052">众议员 Raskin 质询 Trump Jr. 关联公司对 Polymarket 的投资</a>、<a href="https://www.theblock.co/newsletters/data-and-insights/2026-11-24-weve-entered-peak-fear-sky-falls-445476">「We’ve Entered Peak FEAR」与 SKY 下跌</a>。这些是媒体转述与监管进展，不构成操作建议；涉及被盗资金与私钥的条目，只按项目方与执法机构公告处置。</p>

<p><strong>观察与过滤：</strong>RackNerd 黑五仍<strong>不公布活动截止时间</strong>（LowEndBox 11-24 只发了最终 bonus code 与抽奖节点），维持观察；UltaHost、Just Hosting、荫云 YINNET、HostEase、Post Affiliate Pro 等 idcspy 黑五条目仍是转述，未回官方页核到固定价与截止，全部留观察；Appinn 的 Gemini AI Pro 五折、Parallels Desktop 27 黑五 249 元/年同样未回官方活动页，维持观察。本轮<strong>未发现带推荐 / 返利参数的链接</strong>，过滤 0 条。App Store 国区本轮返回「新上架」110 条，是新上架而非限免价格层，不据此判断任何 App 是否限免。</p>

<p><strong>源健康度（11:58–12:06）</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:14%;">组</th><th style="padding:7px 8px 7px 0;width:48%;">成功</th><th style="padding:7px 8px 7px 0;">失败 / 异常</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">news（8）</td><td style="padding:7px 8px 7px 0;">6 源 / 184 条：hn 30、lobsters 25、github-trending 16、ruanyifeng 3、ithome 60、producthunt 50</td><td style="padding:7px 0;color:#c0392b;">v2ex、hf（URLError）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">deal（6）</td><td style="padding:7px 8px 7px 0;">6 源 / 172 条：epic 12、steam 10、appinn 10、lowendbox 20、idcspy 10、appstore 110</td><td style="padding:7px 0;color:#1a7f37;">全绿</td></tr>
<tr><td style="padding:7px 8px 7px 0;">crypto（11）</td><td style="padding:7px 8px 7px 0;">2 源 / 21 条：fng 1、theblock 20</td><td style="padding:7px 0;color:#c0392b;">binance、exstatus、coingecko、cgmarkets、cmc、ethblog、coindesk（URLError）、creleases（410）；panews（HTML，0 条）</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">合计 <code>377 = 184 + 172 + 21</code>；取数窗口 2026-11-25 11:58–12:06（北京时间）。<code>appstore</code> 本轮返回国区新上架 110 条，是「新上架」而不是限免价格层。行情用 Gate.io 与 Binance Vision 双源补位，两者 24 小时涨幅相差约 0.01 个百分点。</p>

<p><strong>形态判断</strong>：失败仍集中在同一类境外 HTTPS 接口，报错形态为 <code>SSL_ERROR_SYSCALL</code> 或连接超时，而不是站点改版或 4xx；这与 11-20 至 11-25 多轮记录一致，按共享出口的通道限制处理，不据此判断这些站点本身不可用。<code>creleases</code> 返回 410 属源站下线，是唯一形态不同的失败。</p>

<p><strong>口径与边界</strong>：四步口径不变：取数（25 源，NDJSON 归一化）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。边界：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。</p>

<p>如实记两句：<strong>本轮执行环境仍未挂载 <code>info-task-gc</code> 技能文件</strong>，因此按仓库既有稿件的 25 源清单与同一口径执行，源名单、四步流程与边界均与 11-23 / 11-24 / 11-25 首稿一致；<strong>GitHub 连接器未以 MCP 形式挂载</strong>，仓库读写通过既有 git 凭据与 <code>origin/main</code> 远端完成。</p>

<p style="margin:28px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-25 00:02–00:10 与 11:58–12:06 两次接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，不构成任何投资建议；新闻部分请注意「媒体转述」与「公司公告 / 官方接口」的区别。</p>
