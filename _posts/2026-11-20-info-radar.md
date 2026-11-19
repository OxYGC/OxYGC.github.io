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

<p style="font-size:12px;color:#9aa0a8;margin:28px 0 0;">边界声明：本站只收集、核实与报道，不代为注册、不绑卡、不领取、不下单；币圈不连钱包、不签名、不给买卖建议。价格、折扣与截止时间以官方页面结算时为准。</p>
