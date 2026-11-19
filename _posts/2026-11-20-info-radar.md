---
title: "资讯雷达 2026-11-20｜Epic《Mark of the Deep》限免、Steam 黑五前哨三款实测价、Gemini 4 Neon 发布与 Ruby 七个 RCE 漏洞"
author: OxYGC
date: 2026-11-20 00:18:00 +0800
permalink: /posts/info-radar-2026-11-20/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam折扣, Gemini 4 Neon, Ruby安全, Anthropic IPO, 币圈]
description: "2026-11-20 午夜档：25 个来源取回 165 条、去重后 147 条新，11 个来源异常。Epic 本周限免为《Mark of the Deep》¥55→0（11-27 00:00 截止）；Steam《FF7 重生》-85%、《极限国度》-90%、《天国：拯救2》-67% 均经 appdetails 回读；Gemini 4 Neon 官方发布，$3/$15 每百万 token、1M 上下文；Ruby 修 7 个含 RCE PoC 的漏洞；Anthropic IPO 官方口径 $83/股、9.8 亿股，对 IT之家「1.5 万亿美元估值」做了更正。"
---

这一轮取数在 2026-11-20 00:08–00:22（北京时间）完成：25 个来源里 14 个取到数据、11 个异常，`SUMMARY fetched=165 fresh=147 sources=25 errors=11`。异常集中在需要境外通道的源：`v2ex`、`hf`、`appstore` 与币圈的 `binance`、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`creleases`、`coindesk` 全部报 `URLError`，形态与昨晚一致，按代理节点抖动记录，不判为站点改版。今天真正会过期的是 Steam《GTA：三部曲 最终版》——榜单截止 11-20 02:00，但 `appdetails` 回读失败，价格只能算未核实；确定可执行的是 Epic 本周限免《Mark of the Deep》，以及 Steam 三款已回读价格的折扣。资讯面两条值得单独拎出来：Gemini 4 Neon 官方发布并给出明确单价；Ruby 一次修掉 7 个漏洞，官方说部分已有 RCE PoC，跑 Ruby / Rails 的生产环境应当优先升级。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮真正会过期、或需要你自己动手的只有这几条</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:25%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:19%;">价格</th><th style="padding:6px 0 6px 0;width:19%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-20 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《GTA：三部曲 最终版》-67%（价格未二次核实）</td>
<td style="padding:9px 8px 9px 0;">¥279.00 → ¥92.07</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/817628/">store.steampowered.com</a></td></tr>
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
<tr>
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-03 01:00 / 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《极限国度》-90%、《FF7 重生》-85%</td>
<td style="padding:9px 8px 9px 0;">¥16.80 / ¥37.20</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/2290180/">极限国度</a> · <a href="https://store.steampowered.com/app/2909400/">FF7 重生</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-20 00:12–00:18 官方接口实测：Epic <code>freeGamesPromotions</code>、Steam <code>featuredcategories</code> 与逐款 <code>appdetails</code>。Steam 的 <code>discount_expiration</code> 是 epoch 时间，这里已换算成北京时间（比 UTC 多 8 小时）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（7）

<details open>
<summary><strong>Epic 本周限免：Mark of the Deep</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥55.00 → 0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00 截止</span></summary>
<p>Epic 这周的免费位只放了这一款：原价 ¥55.00 的《Mark of the Deep》，0 元领取后永久入库。口碑与玩法不在这里展开，0 元入库的机会成本几乎为零。</p>
<p>截止口径来自官方接口：<code>promotionalOffers[].appliedRules[].endDate = 2026-11-26T16:00:00Z</code>，换算北京时间是 11-27 00:00。同一接口本轮只返回这一款 <code>discountPrice == 0</code> 的条目，没有第二款免费游戏，不补写、不推测下一档。</p>
<p style="font-size:12.5px;color:#6b7280;">Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 返回 <code>originalPrice = 5500</code>、<code>discountPrice = 0</code>、<code>endDate = 2026-11-26T16:00:00Z</code>；商店页对直取返回 403，本轮以官方 JSON 为准｜<a href="https://store.epicgames.com/zh-CN/free-games">Epic 免费游戏页</a> ｜ 核实于 2026-11-20 00:12</p>
</details>

<details>
<summary><strong>Steam《FINAL FANTASY VII REBIRTH》-85%</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥248.00 → ¥37.20</span> ｜ <span style="color:#c0392b;font-weight:700;">12-03 02:00 截止</span></summary>
<p>黑五前哨里幅度最大的一档之一。国区原价 ¥248.00，现价 ¥37.20，-85%，`appdetails` 回读的 <code>initial / final / discount_percent</code> 与榜单一致。</p>
<p>同系列的《FF7 重制版 INTERGRADE》榜单显示 -82%（¥198.00 → ¥35.64），但本轮 `appdetails` 连续超时，价格没有二次核实，已放进「观察」段，不在这里当已核实数字。</p>
<p style="font-size:12.5px;color:#6b7280;"><code>appdetails?appids=2909400&amp;cc=cn&amp;l=schinese</code> 返回 <code>initial 24800 / final 3720 / discount_percent 85</code>；截止取自 <code>featuredcategories.discount_expiration</code>（2026-12-02T18:00Z）｜<a href="https://store.steampowered.com/app/2909400/">Steam 商店页</a> ｜ 核实于 2026-11-20 00:15</p>
</details>

<details>
<summary><strong>Steam《极限国度》-90%</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥168.00 → ¥16.80</span> ｜ <span style="color:#c0392b;font-weight:700;">12-03 01:00 截止</span></summary>
<p>原价 ¥168.00，现价 ¥16.80，-90%，是本轮折扣幅度最大的一条。`appdetails` 回读的价格与榜单一致，截止时间 2026-12-02T17:00Z，换算北京时间 12-03 01:00。</p>
<p style="font-size:12.5px;color:#6b7280;"><code>appdetails?appids=2290180&amp;cc=cn&amp;l=schinese</code> 返回 <code>initial 16800 / final 1680 / discount_percent 90</code>｜<a href="https://store.steampowered.com/app/2290180/">Steam 商店页</a> ｜ 核实于 2026-11-20 00:16</p>
</details>

<details>
<summary><strong>Steam《天国：拯救2》-67%</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥228.00 → ¥75.24</span> ｜ <span style="color:#c0392b;font-weight:700;">12-01 02:00 截止</span></summary>
<p>原价 ¥228.00，现价 ¥75.24，-67%。截止 2026-11-30T18:00Z，换算北京时间 12-01 02:00。价格经 `appdetails` 回读，三项与榜单一致。</p>
<p style="font-size:12.5px;color:#6b7280;"><code>appdetails?appids=1771300&amp;cc=cn&amp;l=schinese&amp;filters=price_overview</code> 返回 <code>initial 22800 / final 7524 / discount_percent 67</code>｜<a href="https://store.steampowered.com/app/1771300/">Steam 商店页</a> ｜ 核实于 2026-11-20 00:17</p>
</details>

<details>
<summary><strong>Gemini 4 Neon 发布：$3 / $15 每百万 token，1M 上下文</strong> ｜ <span style="color:#6b7280;">官方博客 2026-11-18</span></summary>
<p>Google 官方给这代 Flash 档的定位是「frontier-level intelligence with fast end-to-end task completion」，覆盖软件工程、知识工作与科研流程。官方给出的硬数字：Artificial Analysis Intelligence Index 61 分、整体第 3（xhigh thinking level），Vals Index 第 2，Agent Arena Index 的可控性第 2；输入 $3 / 百万 token，缓存输入 $0.15 / 百万 token（95% 折扣），输出 $15 / 百万 token，上下文窗口 1M token。</p>
<p>可用渠道同步开放：Gemini API、Google AI Studio、Gemini for business、Google Antigravity（Pro / Ultra 订阅）与 Gemini app（Pro / Ultra）。这组单价对每天跑 Agent 的人是可直接代入成本模型的变化，但榜单名次只作参考，真实效果仍要用自己的任务量一遍。</p>
<p style="font-size:12.5px;color:#6b7280;">官方博客页面返回 200，正文命中 <code>$3 per million input tokens</code>、<code>$15 per million output tokens</code>、<code>1 million-token context window</code>、<code>score of 61</code>，发布日期 2026-11-18；HN 首页同条 953 分 / 732 评｜<a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">Google 官方博客</a> ｜ 核实于 2026-11-20 00:15</p>
</details>

<details>
<summary><strong>Ruby 修 7 个漏洞：部分已有 RCE PoC，升级到 4.0.10 / 3.4.13 / 3.3.14</strong> ｜ <span style="color:#c0392b;font-weight:700;">生产环境优先处理</span></summary>
<p>Ruby 官方安全公告说，正则表达式引擎与字符串大小写转换里共发现 7 个漏洞，已知 PoC 能证明其中部分可触发远程代码执行（RCE）。修复版本是 Ruby 4.0.10、3.4.13、3.3.14；受影响范围：Ruby 3.3.13 及更早、3.4.0–3.4.12、4.0.0–4.0.9。Ruby 3.2 及更早已 EOL，不会拿到修复。</p>
<p>跑 Rails / Sidekiq / 任何常驻 Ruby 服务的，先把版本升上去再谈其他优化；升级前读一眼自家依赖对 4.0 的兼容性，升不了 4.0 的至少落到 3.4.13 或 3.3.14。CVE 编号尚未分配，公告暂以 GHSA 编号引用。</p>
<p style="font-size:12.5px;color:#6b7280;">Ruby 官方公告页返回 200，正文命中 <code>Seven vulnerabilities</code>、<code>remote code execution</code>、<code>Ruby 4.0.10, 3.4.13 and 3.3.14</code>｜<a href="https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/">Ruby 安全公告</a> ｜ 核实于 2026-11-20 00:14</p>
</details>

<details>
<summary><strong>Anthropic IPO 官方口径：$83/股、9.8 亿股，对「1.5 万亿美元估值」做了更正</strong> ｜ <span style="color:#6b7280;">官方新闻稿 2026-11-18</span></summary>
<p>Anthropic 官方新闻稿写明：Class A 普通股定价 $83.00/股，发行 980,000,000 股，其中 956,351,354 股由 Anthropic 出售、23,648,646 股由售股股东出售；预计 11-19 在 Nasdaq Global Select Market 以代码 <code>ANT</code> 开始交易，11-20 交割；承销商另有 30 天、最多 147,000,000 股的超额配售权。</p>
<p>按官方这两个数粗算，发行规模约 813 亿美元（9.8 亿股 × $83），不是 IT之家标题里的「1.5 万亿美元估值」。官方新闻稿本身没有给估值口径，所以这里只报可复算的发行规模；看到「1.5 万亿」这类数字，先回官方原文对一遍股数与单价。</p>
<p style="font-size:12.5px;color:#6b7280;">Anthropic 官方页返回 200，正文命中 <code>$83.00 per share</code>、<code>980,000,000 shares</code>、<code>symbol “ANT”</code>、<code>November 19, 2026</code>；IT之家同条标题称「上市估值达 1.5 万亿美元」，与官方股数、单价对不上｜<a href="https://www.anthropic.com/news/anthropic-prices-initial-public-offering">Anthropic 官方新闻稿</a> ｜ 核实于 2026-11-20 00:16</p>
</details>

## 观察（9）、币圈那一轮与方法

<details open>
<summary><strong>观察清单：未二次核实的 Steam 价、没有截止时间的 VPS、以及两条安全线索</strong> ｜ <span style="color:#6b7280;">存疑原因逐条写明</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;"><th style="padding:6px 8px 6px 0;width:27%;">条目</th><th style="padding:6px 8px 6px 0;width:28%;">数字 / 说法</th><th style="padding:6px 0 6px 0;width:45%;">为什么只算观察</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1462040/">Steam《FF7 重制版 INTERGRADE》-82%</a></td><td style="padding:8px 8px 8px 0;">¥198.00 → ¥35.64，截止 12-03 02:00</td><td style="padding:8px 0 8px 0;">榜单 <code>featuredcategories</code> 有价，<code>appdetails</code> 连续超时，未能二次核价。要买先回商店页确认结算价。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1985810/">Steam《使命召唤：黑色行动冷战》-75%</a></td><td style="padding:8px 8px 8px 0;">¥298.00 → ¥74.50，截止 12-01 02:00</td><td style="padding:8px 0 8px 0;"><code>appdetails</code> 回读时 SSL 握手失败，只有榜单价，未二次核实。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/817628/">Steam《GTA：三部曲 最终版》-67%</a></td><td style="padding:8px 8px 8px 0;">¥279.00 → ¥92.07，截止 11-20 02:00</td><td style="padding:8px 0 8px 0;">榜单价，<code>appdetails</code> 返回 <code>success=false</code>。距截止不到 2 小时，价格未经二次核实，别把它当已核实数字。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://lowendbox.com/blog/pre-black-friday-warm-up-win-a-100-prize-and-grab-a-2gb-ryzen-i9-vps-for-only-22-99-year/">LowEndBox：2GB Ryzen/i9 VPS $22.99/年</a></td><td style="padding:8px 8px 8px 0;">2GB 内存，年付 $22.99，另带抽奖</td><td style="padding:8px 0 8px 0;">商家促销稿，文章未写活动截止时间。按「优惠必须有截止」的门槛只能进观察；低价年付先看备份与迁移成本。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://lowendbox.com/blog/the-dedirock-high-ram-vps-is-here-at-last-omg-8gb-ram-for-24-99-year/">LowEndBox：DediRock 8GB VPS $24.99/年</a></td><td style="padding:8px 8px 8px 0;">8GB 内存，年付 $24.99</td><td style="padding:8px 0 8px 0;">同样是商家促销稿，未写截止，也未回官网核带宽、续费价与退款条款。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.ithome.com/1/029/700.htm">微软官方 PyPI 包 Agent Framework 被劫持</a></td><td style="padding:8px 8px 8px 0;">IT之家称攻击者植入窃取登录凭据的恶意软件</td><td style="padding:8px 0 8px 0;">媒体转述，本轮没回微软安全公告或 PyPI 下架记录。用过该包的环境先查依赖锁文件与凭据轮换。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://social.anoxinon.de/@Codeberg/117636454915265360">Codeberg 域名从账号消失、站点不可达</a></td><td style="padding:8px 8px 8px 0;">Lobsters 212 分、当日第一；Codeberg 官方 Mastodon 发布</td><td style="padding:8px 0 8px 0;">虽有官方社媒帖，但没回 codeberg.org 状态页与注册商记录，域名问题可能仍在处置中。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.postgresql.org/about/news/postgresql-19-released-3449/">PostgreSQL 19 发布</a> · <a href="https://www.php.net/releases/8.6/en.php">PHP 8.6 发布</a></td><td style="padding:8px 8px 8px 0;">两个官方发布页均返回 200</td><td style="padding:8px 0 8px 0;">只核到「已发布」，本轮没逐条读 changelog 与破坏性变更；升级前以官方 release notes 为准。</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://www.theblock.co/news/web3/2026-11-18-ledger-new-hardware-incidents-germany-uae-443530">Ledger 硬件攻击调查扩至德国、阿联酋</a></td><td style="padding:8px 8px 8px 0;">The Block 11-18 报道新案例</td><td style="padding:8px 0 8px 0;">媒体转述，未回 Ledger 官方公告核对受影响批次与处置建议。硬件钱包用户先关注官方渠道，不点社交媒体上的「代为追回」链接。</td></tr>
</tbody></table>
</details>

<details>
<summary><strong>币圈：Gate.io 一手行情快照与情绪指数</strong> ｜ <span style="color:#6b7280;">仅作快照，不构成买卖建议</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;"><th style="padding:6px 8px 6px 0;">标的</th><th style="padding:6px 8px 6px 0;">最新价（USDT）</th><th style="padding:6px 8px 6px 0;">24h 涨跌</th><th style="padding:6px 8px 6px 0;">24h 高 / 低</th><th style="padding:6px 0 6px 0;">来源</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">BTC</td><td style="padding:8px 8px 8px 0;">63,108.2</td><td style="padding:8px 8px 8px 0;color:#1a7f37;">+0.50%</td><td style="padding:8px 8px 8px 0;">64,086.9 / 62,062</td><td style="padding:8px 0 8px 0;">Gate.io 现货</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">ETH</td><td style="padding:8px 8px 8px 0;">1,779.33</td><td style="padding:8px 8px 8px 0;color:#1a7f37;">+0.96%</td><td style="padding:8px 8px 8px 0;">1,817.51 / 1,733</td><td style="padding:8px 0 8px 0;">Gate.io 现货</td></tr>
<tr><td style="padding:8px 8px 8px 0;">SOL</td><td style="padding:8px 8px 8px 0;">73.73</td><td style="padding:8px 8px 8px 0;color:#1a7f37;">+0.83%</td><td style="padding:8px 8px 8px 0;">75.63 / 72.22</td><td style="padding:8px 0 8px 0;">Gate.io 现货</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;margin:12px 0 0;">恐惧贪婪指数当日快照为 <strong>10（Extreme Fear）</strong>，来源 alternative.me。币圈 11 个源里只有 <code>fng</code>、<code>theblock</code>、<code>panews</code> 通，<code>binance</code>、<code>exstatus</code>、<code>coingecko</code>、<code>cgmarkets</code>、<code>cmc</code>、<code>ethblog</code>、<code>creleases</code>、<code>coindesk</code> 全部被代理挡住，所以这一轮没有交易所公告原文、没有热搜与异动榜，只有上面三行一手价格。媒体面另有三条只作语境：Binance 获 65 亿美元冻结令、Kraken 母公司收购 Tribe Capital、Ledger 扩大硬件攻击调查——都未回交易所或项目方公告核实。<strong>行情与情绪指数一律不构成买卖建议，本轮不写支撑位与目标价。</strong></p>
</details>

<details>
<summary><strong>取数与来源健康度：25 个来源、14 个正常、11 个异常</strong> ｜ <span style="color:#6b7280;">00:08–00:22 实测</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;"><th style="padding:6px 8px 6px 0;">来源</th><th style="padding:6px 8px 6px 0;">条数</th><th style="padding:6px 0 6px 0;">状态</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">hackernews</td><td style="padding:5px 8px 5px 0;">25</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK（榜首 Gemini 4 Neon 953 分）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">ithome</td><td style="padding:5px 8px 5px 0;">25</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">lobsters</td><td style="padding:5px 8px 5px 0;">20</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">github-trending</td><td style="padding:5px 8px 5px 0;">16</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK（Agent Skills 仍占主导）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">producthunt</td><td style="padding:5px 8px 5px 0;">15</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">ruanyifeng</td><td style="padding:5px 8px 5px 0;">1</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK（周刊第 418 期）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">epic</td><td style="padding:5px 8px 5px 0;">1</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">steam</td><td style="padding:5px 8px 5px 0;">10</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK（3 条 appdetails 回读一致）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">lowendbox</td><td style="padding:5px 8px 5px 0;">2</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">idcspy</td><td style="padding:5px 8px 5px 0;">10</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">appinn</td><td style="padding:5px 8px 5px 0;">1</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;">fng / theblock / panews</td><td style="padding:5px 8px 5px 0;">1 / 10 / 10</td><td style="padding:5px 0 5px 0;color:#1a7f37;">OK</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:5px 8px 5px 0;color:#c0392b;">v2ex / hf / appstore</td><td style="padding:5px 8px 5px 0;color:#c0392b;">0</td><td style="padding:5px 0 5px 0;color:#c0392b;">ERR URLError（代理/登录态）</td></tr>
<tr><td style="padding:5px 8px 5px 0;color:#c0392b;">binance / exstatus / coingecko / cgmarkets / cmc / ethblog / creleases / coindesk</td><td style="padding:5px 8px 5px 0;color:#c0392b;">0</td><td style="padding:5px 0 5px 0;color:#c0392b;">ERR URLError（境外通道整批被挡）</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">聚合口径：<code>SUMMARY fetched=165 fresh=147 sources=25 errors=11</code>。境内源与 HN / Lobsters / GitHub Trending / Steam / Epic 正常；境外交易所与 CoinGecko / CMC 整批被挡，形态与昨晚一致，仍按代理节点抖动记录，不做站点改版判断。App Store 限免层本轮同样没取到，iOS 限免缺位。</p>
</details>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">06:30 早间全量复核（同日发布）</p>

<p style="margin:0 0 16px;">午夜那一轮境外通道整批被挡（11 个 <code>ERR URLError</code>，交易所、行情、App Store 三层全空）。06:32 这轮代理恢复，25 个源 <code>errors=0</code>、取回 317 条、去重后新增 187 条，把缺的三层补齐，另外多核到两条软件版本发布与一条羊毛。下面只写增量，午夜档已核实的内容不重复。</p>

<div style="border:1px solid #e6e8eb;border-radius:10px;padding:14px 16px;margin:0 0 24px;">
<p style="margin:0 0 10px;font-size:14px;font-weight:600;color:#1f2329;">早间增补行动清单</p>
<table>
<thead><tr><th>时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
<tbody>
<tr>
<td><strong style="color:#c0392b;">11-27 08:00 更正</strong><br>北京时间</td>
<td>Epic 周免《Mark of the Deep》截止口径</td>
<td><span style="color:#1a7f37;font-weight:600;">0 元</span><br><span style="color:#6b7280;">原价 ¥55.00</span></td>
<td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 领取页</a></td>
</tr>
<tr>
<td><strong style="color:#c0392b;">12-01 前</strong><br>VIP 上线日</td>
<td>UU远程：上线前注册可领年卡五折</td>
<td><span style="color:#6b7280;">年卡 5 折</span></td>
<td><a href="https://uuyc.163.com/">官方页公告</a></td>
</tr>
<tr>
<td><strong style="color:#c0392b;">进行中</strong><br>起于 11-20 04:06</td>
<td>Kraken：期货撤单被拒 + API 降级（午夜档缺这个源）</td>
<td><span style="color:#6b7280;">minor</span></td>
<td><a href="https://status.kraken.com/">状态页</a></td>
</tr>
<tr>
<td>合约已于 11-19 转换</td>
<td>币安 ANTUSDT「Pre-IPO 永续」转标准 TradFi 永续</td>
<td><span style="color:#6b7280;">公告口径</span></td>
<td><a href="https://www.binance.com/en/support/announcement/detail/89df0df327a3431485ba54a7c03663c3">公告原文</a></td>
</tr>
</tbody>
</table>
</div>

<details open>
<summary><strong>🔥 早间唯一新增紧急：Kraken 服务部分降级（含期货与 API）</strong> —— <span style="color:#c0392b;">状态页 identified，起于 11-20 04:06</span></summary>
<p>11-20 06:41 回读 Statuspage：<code>indicator=minor</code>、<code>description=Partially Degraded Service</code>。现行事件「Futures cancel-after-timeout requests rejected」状态 identified，创建于 2026-11-19T20:06:33Z（北京时间 11-20 04:06）。组件层面 Kraken Derivatives / Kraken API / Unified WebSocket / Digital Currency Funding 为 degraded_performance，REST / WebSocket / Kraken Prime API 挂 under_maintenance。<br>列成紧急的理由：午夜档 <code>exstatus</code> 整源失败，这个状态当时根本看不到；而它在「服务状态非 none」这一档，直接决定在 Kraken 的撤单、行情与充提入口是否可用。<strong>你要做的</strong>：登进 Kraken 确认没有在途订单依赖 WebSocket，有仓位就复核风控单是否还挂得住。同轮 Coinbase <code>indicator=none</code>（All Systems Operational）。<a href="https://status.kraken.com/">status.kraken.com</a> ｜ 核实于 2026-11-20 06:41</p>
</details>

<details>
<summary><strong>⭐ 早间新增值得（5）</strong> —— iOS 本体免费 3 条、UU远程羊毛、PG 19 与 PHP 8.6</summary>
<p><strong>App Store 本体免费（午夜档 <code>appstore</code> 整源未取到，这轮补上）</strong>：汇总频道 11-19 播报「本体限免」，iTunes lookup 按 id 核到国区现价 0 的有三条 —— <a href="https://apps.apple.com/cn/app/id6827505184">Andarium（id 6827505184）</a>、<a href="https://apps.apple.com/cn/app/id1381194246">AiZIP - AI时代压缩包工作台（id 1381194246）</a>、<a href="https://apps.apple.com/cn/app/id6770079462">AuraRead 本地小说听书阅读器（id 6770079462）</a>。口径照旧：核到现价 0 只写「下载不花钱」，接口分不出本就免费与促销中，不等于「限免仍在」；<strong>Apple 不公布限免截止时间</strong>。<br>反例两条，说明为什么必须按 id 核：<a href="https://apps.apple.com/cn/app/id6832136677">Remind &amp; Record</a> 国区现价 ¥8.00、<a href="https://apps.apple.com/cn/app/id6821917560">AudayWatch 全天AI录音</a> 现价 ¥38.00 —— 播报的限免已失效或已改价。<br>核实于 2026-11-20 06:32（取数轮）。</p>
<p><strong>UU远程：VIP 上线前注册可领年卡五折 ｜ <span style="color:#c0392b;">截止 12-01</span></strong>。官方页公告（2026-11-19）原文：「基础远控保持『免费』」「基础远控将持续免费，且不限次、不限时、不排队、无广告」「在 2026 年 12 月 1 日 VIP 服务上线前注册成功的用户，还可领取年卡五折专属优惠」。核到的是这条免费承诺与五折条件；小众软件那篇写的「24元/月起、免费版只剩 1080P 30帧」本轮没回官方页对上档位价格，挂在下面的观察。<a href="https://uuyc.163.com/">uuyc.163.com</a> ｜ 核实于 2026-11-20 06:42。</p>
<p><strong>PostgreSQL 19 正式发布 / PHP 8.6 发布</strong>：官方新闻页 H1「PostgreSQL 19 Released!」（页面日期 2026-11-19）与 <a href="https://www.postgresql.org/about/news/postgresql-19-released-3449/">postgresql.org 公告</a>；PHP <a href="https://www.php.net/releases/8.6/en.php">8.6 release 页</a>主题「Faster, Safer, More Powerful」。两条都是主版本节点，值得排的是兼容性自查而不是新功能。<br>核实于 2026-11-20 06:43。</p>
<p><strong>币圈一手：币安把 USDⓈ 本位 ANTUSDT「Pre-IPO 永续」转为标准 TradFi 永续</strong>，公告明写 2026-11-19 生效（<a href="https://www.binance.com/en/support/announcement/detail/89df0df327a3431485ba54a7c03663c3">公告原文</a>）。若账户还持有该永续仓位或挂单，转换后合约规格与标记价口径会变。<strong>这不是买卖建议</strong>，本轮对 ANT 及任何币种不写方向与目标价。另有 6 条 Anthropic（ANTB / ANT）bStocks 公告（上币、加抵押品、Wallet 活动）属新产品与活动口径，与在用资产可得性无关，列在观察。核实于 2026-11-20 06:32。</p>
</details>

<details>
<summary><strong>👀 早间新增观察（12）与一处口径更正</strong></summary>
<p><strong>更正</strong>：午夜档写《Mark of the Deep》「11-27 00:00 截止」，官方接口 <code>endDate=2026-11-26T16:00Z</code> 换算北京时间是 <strong>11-27 08:00</strong>，以这轮回读为准。原价 ¥55.00、<code>discountPrice=0</code> 两条与午夜档一致。</p>
<table>
<thead><tr><th>条目</th><th>为什么只算观察</th></tr></thead>
<tbody>
<tr><td>《The Last of Us Part II Remastered》¥231.15（-33%，12-02 02:00 截止）</td><td>抓到的字段与站内活动一致，但本轮没单独回官方页核这一条，只作榜单转述</td></tr>
<tr><td>Epic 下一周免预告《火之石 – 放置点击英雄RPG》</td><td>官方接口给的是 upcoming 档期 11-27 08:00 ~ 12-04 08:00（北京时间），还没开始，不催领</td></tr>
<tr><td>App Store：Infinite Canvas / 物有记（内购限免）</td><td>前者按 id 查不到上架记录、后者播报正文没有直链无从取 id；内购解锁价不体现在下载价上，只算频道转述</td></tr>
<tr><td>UU远程「24元/月起、免费版只剩 1080P 30帧」</td><td>官方页只确认免费承诺与五折条件，档位价格是小众软件转述，未核实</td></tr>
<tr><td>Nginx 曝出 10 项安全漏洞（美国主机侦探转述）</td><td>只核到官方 advisories 页在线（累计 77 个唯一 CVE 编号），没逐条对上「10 项」指哪批；跑 nginx 的自己按版本过一遍。午夜档另有一条 Ruby 修 7 个含 RCE PoC 漏洞，同源口径</td></tr>
<tr><td>GitHub Trending：firecrawl / Ghost-Downloader-3 / autoclip / opensre 等 8 库</td><td>trending 无发布时间戳，只说明当天热度，未逐个读 README 判断是否解决你手上的问题</td></tr>
<tr><td>币安 Anthropic（ANTB / ANT）bStocks 系列 6 条公告</td><td>上币、加抵押品、Wallet 活动更新，与在用资产可得性无关，只列存在</td></tr>
<tr><td>行情与热度快照（截至 11-20 06:32，来源 CoinGecko / CMC / alternative.me）</td><td>BTC $62,075（-0.6%）、ETH $1,756.81（-0.3%）、BNB $580.18（+0.4%）；热搜前列 BTC / Sky / Pepe / Zcash；恐惧贪婪指数 10（Extreme Fear）。是数字不是信息，不构成任何操作建议</td></tr>
<tr><td>市值榜 24h 异动：Bitway +19.6% / Pieverse -16.0% / Pearl +8.6%</td><td>门槛是 rank ≤300 且绝对涨跌 ≥8%，纯行情，不给 ⭐</td></tr>
<tr><td>Coinbase 状态 All Systems Operational</td><td>11-20 06:41 实测 <code>indicator=none</code>，只为对照 Kraken 记录</td></tr>
<tr><td>Solana 客户端 anza-xyz/agave 发 v5.0.0-alpha.1</td><td>项目方一手发版（11-20 04:57 北京时间），alpha 版本，非运行中验证节点无需动作</td></tr>
<tr><td>LowEndBox 黑五预热「抽 $100 + 2GB Ryzen VPS $22.99/年」</td><td>抽奖软文属性，未回厂商页核价，不作值得</td></tr>
</tbody>
</table>
</details>

<details>
<summary><strong>早间这轮来源健康度：25 个 key 全绿</strong> ｜ <span style="color:#6b7280;">06:32 完成，约 55 秒</span></summary>
<table>
<thead><tr><th>来源</th><th>条数</th><th>状态</th></tr></thead>
<tbody>
<tr><td>hackernews / ithome</td><td>25 / 25</td><td style="color:#1a7f37;">OK</td></tr>
<tr><td>panews / lobsters / producthunt</td><td>15 / 14 / 14</td><td style="color:#1a7f37;">OK（lobsters 出 PG19、PHP8.6）</td></tr>
<tr><td>coindesk / theblock</td><td>12 / 12</td><td style="color:#1a7f37;">OK（午夜档这两个只通一个）</td></tr>
<tr><td>v2ex / coingecko-trending / github-trending</td><td>10 / 10 / 8</td><td style="color:#1a7f37;">OK（v2ex 午夜档 ERR，本轮恢复）</td></tr>
<tr><td>appstore-ios</td><td>8</td><td style="color:#1a7f37;">OK（午夜档整源缺位；3 条现价 0 进取，5 条进观察）</td></tr>
<tr><td>binance-ann / idcspy / coinmarketcap-search</td><td>7 / 6 / 6</td><td style="color:#1a7f37;">OK（境外交易所源本轮恢复）</td></tr>
<tr><td>steam / coingecko-markets / epic-store</td><td>4 / 4 / 1</td><td style="color:#1a7f37;">OK（Steam 走 <code>cc=cn</code> 核国区价）</td></tr>
<tr><td>hf-daily-papers / lowendbox / crypto-release</td><td>1 / 1 / 1 / 1</td><td style="color:#1a7f37;">OK</td></tr>
<tr><td>exchange-status / appinn / fng-index</td><td>1 / 1 / 1</td><td style="color:#1a7f37;">OK（Kraken minor、Coinbase none）</td></tr>
<tr><td>ethblog</td><td>0</td><td style="color:#1a7f37;">OK（<code>--days 2</code> 窗口内无新帖，非故障）</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">聚合口径：<code>SUMMARY fetched=317 fresh=187 sources=25 errors=0</code>，本轮没有一条 <code>ERR source=</code>。午夜档那 11 个 <code>URLError</code> 全部恢复，印证当时的判断：是代理节点抖动，不是站点改版。</p>
</details>

<p style="font-size:12px;color:#9aa0a8;margin:28px 0 0;">边界声明：本站只收集、核实与报道，不代为注册、不绑卡、不领取、不下单；币圈不连钱包、不签名、不给买卖建议。价格、折扣与截止时间以官方页面结算时为准。</p>
