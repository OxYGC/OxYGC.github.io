---
title: "资讯雷达 2026-11-17｜Epic《斗阵骑士》0 元、Steam 特惠换血、Trezor 物流方泄露 2.7 万单（凌晨版 + 早间 06:30 复核）"
author: OxYGC
date: 2026-11-17 00:25:00 +0800
permalink: /posts/info-radar-2026-11-17/
categories: [Info, Deals]
tags: [资讯雷达, Steam折扣, Epic限免, App Store限免, GitHub趋势, AI动态, 币圈]
description: "2026-11-17 凌晨版 + 早间 06:30–06:46 复核：Epic《斗阵骑士 Knightica》0 元领取，11-20 00:00 截止；Steam 特惠窗口换血，早间《天国：拯救2》¥228 → ¥75.24（-67%）已回 appdetails 逐款复核；GitHub Trending 仍由 Agent Skills 与 coding agent 占榜；币圈恐惧贪婪指数 10（Extreme Fear）。早间这一轮 25 个来源全绿、errors=0，凌晨因代理通道失败的 11 个源全部恢复，补齐了 iOS 国区限免（1 款本体核到下载不花钱）、Trezor 物流方 Skladon 泄露约 2.7 万笔订单、Kraken 充提部分降级与 CoinGecko/CMC 行情热搜。"
---

这一轮取数在 2026-11-17 00:10–00:25（北京时间）完成：25 个来源里 13 个取到数据、1 个本轮无货（小众软件，属正常）、11 个因代理通道限制未取到（清单见文末）。共留下 121 条条目，其中 10 条来自 Steam、1 条来自 Epic。这是当天第一版，也是当天唯一一篇；今天若再跑，只会在本文件内更新，不新增文件。

**早间 06:30:45–06:31:52 跑了第二轮，验真做到 06:46，仍然是这一篇。** 第二轮的规模与连通都和凌晨不同：`SUMMARY fetched=314 fresh=179 sources=25 errors=0`，凌晨报 URLError／超时的 11 个源（v2ex、hf、binance、exstatus、coingecko、cgmarkets、cmc、ethblog、creleases、coindesk、appstore）这一轮全部返回成功，印证了「是代理节点抖动，不是站点集体改版」。复核带来的增量是五块，凡标注「早间」的数值以 06:30–06:46 这次实测为准：

1. **iOS 国区限免**——凌晨整源失败，早间按 trackId 逐条回 iTunes 核了国区现价：7 条播报里 1 款本体限免核到下载不花钱、5 条内购型只算转述、1 条查不到上架记录。
2. **交易所与项目方一手**——Kraken 状态页仍是 minor / Partially Degraded，最新事件 KAVA Funding Delays；Trezor 官方博客一手公告：物流合作方 Skladon 被泄约 27,000 笔订单的收货信息。
3. **Steam 早间窗口**——凌晨在榜的《Overcooked! 2》《隔离区-丧尸末日生存》《Bodycam》《Euro Truck Simulator 2》这一轮已掉出返回窗口（掉出≠活动结束），新进窗口的是《天国：拯救2》-67%；其中两条已逐款回 `appdetails` 复核。
4. **行情与热搜**——凌晨没有现价快照，早间取到 CoinGecko 市值前 5、异动 5 条与两个热搜榜（仍是快照，不是信号）。
5. **GitHub Trending**——早间回 GitHub API 复核了 4 个仓库的总 star 与创建时间。

结论先摆前面：**早间这一轮最该动手的是 Trezor 那条防钓鱼提醒——物流合作方 Skladon 被泄约 2.7 万笔订单的姓名、电话、地址、邮箱，此后自称 Trezor / Skladon 的改址与补发一律按钓鱼处理；Kraken 的充提网关仍在报降级（最新事件 KAVA 充值延迟），在 Kraken 有充提的自己复查一笔。** 消费侧：Epic 免费位仍是《斗阵骑士 Knightica》0 元、11-20 00:00 换新；Steam 早间窗口里最近的一个到期点是《How They Built the Pyramids》¥22.00 → ¥15.40（-30%，11-20 18:00 收），幅度最大的是《天国：拯救2》¥228.00 → ¥75.24（-67%，11-30 18:00 收），这两条已逐款回官方 `appdetails` 复核；凌晨卡在榜首的《Overcooked! 2》-66%（¥33.32）今早 06:46 已掉出滚动窗口，按“掉出窗口≠活动结束”处理，行动卡里不再列它，要买请自己打开商店页确认。iOS 侧早间核到 1 款本体限免下载不花钱，但 Apple 不公布截止时间。资讯面今天比较集中：GitHub Trending 依旧被 Agent Skills / coding agent 相关项目占住；AI 侧有 Qwen4-Max 发布页冲上 HN 首页、AMD 完成对 World Labs 的收购并由李飞飞出任首席科学家；币圈继续处于恐惧区间，恐惧贪婪指数 10，PANews 转述过去 24 小时全网合约爆仓 2.83 亿美元（多空双爆），另有 Solana 基金会发布 Linux 内核漏洞安全提醒——这条本轮只有媒体转述，未回到官方 advisory，按“观察”处理。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮真正会过期、或需要你自己动手的只有这几条</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:18%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-20 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《斗阵骑士 Knightica》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-20 18:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《How They Built the Pyramids》-30%（早间窗口最近的一个到期点，已回 appdetails 复核）</td>
<td style="padding:9px 8px 9px 0;">¥22.00 → ¥15.40</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/5458210/">store.steampowered.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-30 18:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《天国：拯救2》-67%（早间新进窗口，本轮最大折扣，已回 appdetails 复核）</td>
<td style="padding:9px 8px 9px 0;">¥228.00 → ¥75.24</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1771300/">store.steampowered.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">今天下载（无截止）</td>
<td style="padding:9px 8px 9px 0;">App Store「我的待办」本体限免，早间回 iTunes 核到国区下载价 0 元</td>
<td style="padding:9px 8px 9px 0;">下载不花钱</td>
<td style="padding:9px 0 9px 0;"><a href="https://apps.apple.com/cn/app/id1294530516">apps.apple.com/cn</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">持续中（复查）</td>
<td style="padding:9px 8px 9px 0;">Kraken 充提仍部分降级，最新事件 KAVA Funding Delays</td>
<td style="padding:9px 8px 9px 0;">非价格项</td>
<td style="padding:9px 0 9px 0;"><a href="https://status.kraken.com/api/v2/summary.json">status.kraken.com</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">此后长期（防钓鱼）</td>
<td style="padding:9px 8px 9px 0;">Trezor 官方公告：物流方 Skladon 泄露约 27,000 笔订单信息</td>
<td style="padding:9px 8px 9px 0;">非价格项</td>
<td style="padding:9px 0 9px 0;"><a href="https://trezor.io/blog/news/data-breach-at-trezor-shipping-partner-skladon">trezor.io</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-17 00:22 与 06:33–06:46 两次官方接口实测（Steam <code>featuredcategories</code> / <code>appdetails</code>、Epic <code>freeGamesPromotions</code>、iTunes <code>lookup</code>、交易所 Statuspage）。<strong>凌晨卡里的《Overcooked! 2》-66%（11-20 01:00 收）、《隔离区-丧尸末日生存》-40%、《Bodycam》-20% 在早间 06:46 的返回里已经掉出前 10 窗口，按旧口径「掉出窗口≠活动结束」从行动卡移出，数值本身没有再核到</strong>——要买请自己打开商店页确认。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（5，另加早间复核 5 条）

<details open>
<summary><strong>Steam 折扣：窗口换血，最近《Overcooked! 2》11-20 01:00</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥15.40 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-20 01:00 收</span></summary>
<p>Steam 官方 <code>featuredcategories</code> 本轮返回 10 条特惠，金额已从“分”换算成人民币，截止时间按 <code>discount_expiration</code> 换算为北京时间。与 11-16 那轮相比，《Sifu》《Hearts of Iron IV》掉出窗口；新进的是《红色沙漠：增强版》《Dungeonbound》《How They Built the Pyramids》《我带过的最差一届》；《Overcooked! 2》《隔离区-丧尸末日生存》《Bodycam》《Euro Truck Simulator 2》《转运军团 - Slotbound》《重生2我独自逆袭》继续在榜。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏（appid）</th><th style="padding:6px 8px 6px 0;">国区价</th><th style="padding:6px 8px 6px 0;">折扣</th><th style="padding:6px 0 6px 0;width:24%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/728880/">Overcooked! 2</a>（728880）</td><td style="padding:8px 8px 8px 0;">¥98.00 → ¥33.32</td><td style="padding:8px 8px 8px 0;">-66%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-20 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1211600/">隔离区-丧尸末日生存</a>（1211600）</td><td style="padding:8px 8px 8px 0;">¥48.00 → ¥28.80</td><td style="padding:8px 8px 8px 0;">-40%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-20 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5458210/">How They Built the Pyramids</a>（5458210）</td><td style="padding:8px 8px 8px 0;">¥22.00 → ¥15.40</td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-21 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2406770/">Bodycam</a>（2406770）</td><td style="padding:8px 8px 8px 0;">¥128.00 → ¥102.40</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-21 05:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5175310/">我带过的最差一届</a>（5175310）</td><td style="padding:8px 8px 8px 0;">¥28.00 → ¥18.20</td><td style="padding:8px 8px 8px 0;">-35%</td><td style="padding:8px 0 8px 0;">11-24 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/227300/">Euro Truck Simulator 2</a>（227300）</td><td style="padding:8px 8px 8px 0;">¥92.99 → ¥23.24</td><td style="padding:8px 8px 8px 0;">-75%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-25 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/4459590/">转运军团 - Slotbound</a>（4459590）</td><td style="padding:8px 8px 8px 0;">¥42.00 → ¥37.80</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">11-27 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3816120/">重生2我独自逆袭</a>（3816120）</td><td style="padding:8px 8px 8px 0;">¥58.00 → ¥46.40</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 0 8px 0;">11-28 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3321460/">红色沙漠：增强版</a>（3321460）</td><td style="padding:8px 8px 8px 0;">¥268.00 → ¥214.40</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 0 8px 0;">11-30 16:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5200620/">Dungeonbound</a>（5200620）</td><td style="padding:8px 8px 8px 0;">¥42.00 → ¥37.80</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">12-01 02:00</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">取法：<code>store.steampowered.com/api/featuredcategories?cc=cn&amp;l=schinese</code> 的 <code>specials.items</code>，价格取 <code>original_price</code>/<code>final_price</code>（单位分），截止取 <code>discount_expiration</code> 并换算为北京时间；核实于 2026-11-17 00:22。边界：只取列表接口，未逐款回 <code>appdetails</code> 复核，付款前请以商店页为准；这个接口只返回滚动的前 10 条，掉出窗口不等于活动结束。</p>
</details>

<details open>
<summary><strong>Epic 免费位：《斗阵骑士》0 元到 11-20 00:00，下一位《Mark of the Deep》接棒</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span>（原价 ¥47.00）｜ <span style="color:#c0392b;font-weight:700;">11-20 00:00 截止</span></summary>
<p>官方 JSON 里《斗阵骑士 Knightica》当前 <code>discountPrice=0</code>、<code>originalPrice=4700</code> 分，促销窗口 <code>2026-11-12T16:00Z</code> → <code>2026-11-19T16:00Z</code>，换算成北京时间是<strong>现在 → 11-20 00:00</strong>，领取后永久入库。同一接口返回的后续免费位：<strong>《Mark of the Deep》（原价 ¥55.00）窗口 <code>2026-11-19T16:00Z</code> → <code>2026-11-26T16:00Z</code>，即 11-20 00:00 → 11-27 00:00</strong>；《TerraScape》（原价 ¥53.00）窗口 <code>2026-11-21T16:00Z</code> → <code>2026-12-21T16:00Z</code>，即 11-22 00:00 → 12-22 00:00。其他条目本轮都是付费折扣或未开促销，不混进免费位。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;">原价</th><th style="padding:6px 0 6px 0;">窗口（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;font-weight:700;">斗阵骑士 Knightica</td><td style="padding:8px 8px 8px 0;">¥47.00</td><td style="padding:8px 0 8px 0;color:#c0392b;">现在 → 11-20 00:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.epicgames.com/zh-CN/p/mark-of-the-deep-f7dc08">Mark of the Deep</a></td><td style="padding:8px 8px 8px 0;">¥55.00</td><td style="padding:8px 0 8px 0;">11-20 00:00 → 11-27 00:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.epicgames.com/zh-CN/p/terrascape">TerraScape</a></td><td style="padding:8px 8px 8px 0;">¥53.00</td><td style="padding:8px 0 8px 0;">11-22 00:00 → 12-22 00:00</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">出处：Epic 官方 <code>freeGamesPromotions</code> 接口（<code>locale=zh-CN&amp;country=CN&amp;allowCountries=CN</code>），核实于 2026-11-17 00:22。边界：领了永久入库，后续 DLC / 内购是否另收费以商店页为准；本站不代领。未在本轮 JSON 出现的游戏（包括昨天提过的《Alien: Isolation》）不写成“下周一定送”，等接口返回再报。</p>
</details>

<details open>
<summary><strong>GitHub Trending：Agent Skills 与 coding agent 继续占榜，last30days-skill 以 67,930 star 居前</strong> ｜ <span style="color:#6b7280;">今日榜</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">仓库</th><th style="padding:6px 8px 6px 0;width:14%;">总 star</th><th style="padding:6px 0 6px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/ag-ui-protocol/ag-ui">ag-ui-protocol/ag-ui</a></td><td style="padding:8px 8px 8px 0;">18,593</td><td style="padding:8px 0 8px 0;">Agent 与前端的交互协议层</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/backnotprop/plannotator">backnotprop/plannotator</a></td><td style="padding:8px 8px 8px 0;">12,344</td><td style="padding:8px 0 8px 0;">与 Agent 协作的规划 / 标注 / 审阅工作台</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/dream-num/univer">dream-num/univer</a></td><td style="padding:8px 8px 8px 0;">27,567</td><td style="padding:8px 0 8px 0;">AI Office SDK：编辑、计算、协作与文件处理</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/mvanhorn/last30days-skill">mvanhorn/last30days-skill</a></td><td style="padding:8px 8px 8px 0;">67,930</td><td style="padding:8px 0 8px 0;">跨 Reddit / X / YouTube / HN 研究任意主题的 Agent skill</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/google-labs-code/stitch-skills">google-labs-code/stitch-skills</a></td><td style="padding:8px 8px 8px 0;">9,643</td><td style="padding:8px 0 8px 0;">配合 Stitch MCP 的 Agent Skills 库</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/NVIDIA/SkillEvaluator">NVIDIA/SkillEvaluator</a></td><td style="padding:8px 8px 8px 0;">2,391</td><td style="padding:8px 0 8px 0;">Agent skills 的分层评测与质量门禁</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/alibaba/open-code-review">alibaba/open-code-review</a></td><td style="padding:8px 8px 8px 0;">52,764</td><td style="padding:8px 0 8px 0;">混合架构代码评审：确定性流水线 + LLM Agent</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">ChromeDevTools/chrome-devtools-mcp</a></td><td style="padding:8px 8px 8px 0;">57,524</td><td style="padding:8px 0 8px 0;">面向编码 Agent 的 Chrome DevTools</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/getarcaneapp/arcane">getarcaneapp/arcane</a></td><td style="padding:8px 8px 8px 0;">8,514</td><td style="padding:8px 0 8px 0;">面向所有人的 Docker 管理面板</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://github.com/kajisho5/ffmpeg-skill">kajisho5/ffmpeg-skill</a></td><td style="padding:8px 8px 8px 0;">6,360</td><td style="padding:8px 0 8px 0;">给 coding agent 的本地视频编辑：42 个 FFmpeg 工具 + MCP</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">出处：GitHub Trending 日榜 HTML 抓取，总 star 为 2026-11-17 00:22 接口返回的数值，会随时间继续上涨。本轮脚本没有解析出“今日新增”，所以不写 +N，只给总量与用途。另：<a href="https://github.com/DeanChensj/jiangshan-map">DeanChensj/jiangshan-map</a>（江山时序，6,607 star）与 <a href="https://github.com/google-research/paper-orchestra">google-research/paper-orchestra</a>（自动写论文的多 Agent 框架，1,194 star）也在榜，前者是历史地图项目、后者偏研究工具。</p>
</details>

<details open>
<summary><strong>开发 · AI 动态：Qwen4-Max 发布页登上 HN 首页，AMD 完成收购 World Labs</strong> ｜ <span style="color:#6b7280;">2026-11-17 00:22 核实</span></summary>
<p>今天值得读的四条，全部给一手链接（HN 只作发现层，点进去是原始页面）：</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 0 6px 0;">看点</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://qwen.ai/blog?id=qwen4-max">Qwen4-Max</a></td><td style="padding:8px 0 8px 0;">官方博客发布，HN 首页当轮第一；具体参数与开放范围以页面为准，本轮未逐项摘录</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.ithome.com/1/027/969.htm">AMD 完成收购 World Labs，李飞飞出任首席科学家</a></td><td style="padding:8px 0 8px 0;">IT之家转述；AI 侧又一起大厂并购，具体交割条款未在报道中展开</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://iter.ca/post/ubo-uxss/">uBlock Origin 的通用 XSS（网站驱动的元素选择器）</a></td><td style="padding:8px 0 8px 0;">安全研究者公开细节；如果你在用的浏览器扩展版本较旧，值得对照更新记录</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-419.html">阮一峰周刊第 419 期：机房来了，写字楼走了</a></td><td style="padding:8px 0 8px 0;">每周固定读物，本期主题是数据中心与写字楼经济</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">核实于 2026-11-17 00:22。HN / IT之家 / 阮一峰都是本轮实际取到的条目；Qwen4-Max 与 uBlock 那两条只核到“页面存在且标题一致”，未做技术细节复核，按阅读线索处理。</p>
</details>

<details open>
<summary><strong>币圈：恐惧贪婪指数 10，24 小时全网爆仓 2.83 亿美元，Solana 协议升到 1.0</strong> ｜ <span style="color:#6b7280;">快照与转述</span></summary>
<p>本轮 CoinGecko 行情与热搜接口被代理通道挡住，没有 BTC / ETH 现价快照，只有情绪指数与媒体转述，按“观察级信息”呈现，不构成任何操作建议。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 0 6px 0;">内容</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">恐惧贪婪指数</td><td style="padding:8px 0 8px 0;"><strong style="color:#c0392b;">10（Extreme Fear）</strong>，alternative.me 官方接口，2026-11-17 快照</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.panewslab.com/zh/articles/01a1e4fa-be57-76fc-8371-937abc55f170">24 小时全网合约爆仓</a></td><td style="padding:8px 0 8px 0;">2.83 亿美元，多空双爆（PANews 转述，未回交易所原始数据核对）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.theblock.co/news/ecosystems/2026-11-16-solana-drops-mainnet-beta-lab">Solana 去掉 mainnet beta 标签</a></td><td style="padding:8px 0 8px 0;">采用 protocol version 1.0（TheBlock，媒体转述）</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://www.panewslab.com/zh/articles/01a1e4a4-056d-7631-912a-2902c10c5aa6">Vitalik 谈 EIP-8037</a></td><td style="padding:8px 0 8px 0;">主张提高创建账户与部署合约的 gas 成本，属于扩容与状态管理的讨论，不是操作建议</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">口径：行情、涨跌幅、情绪指数一律只作状态描述；喊单、目标价、荐币不写。快照时间 2026-11-17 00:22（北京时间），来源已在表中逐条标注。</p>
</details>

<details open>
<summary><strong>早间复核｜Steam 窗口换血：天国：拯救2 -67% 与 Pyramids -30% 已逐款回 appdetails</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥15.40 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-20 18:00 收</span></summary>
<p>06:46 这一轮 <code>featuredcategories</code> 返回 5 条国区特惠，和凌晨那 10 条不是同一批：<strong>新进的《天国：拯救2》是本轮最大折扣（-67%）</strong>，而凌晨在榜的《Overcooked! 2》《隔离区-丧尸末日生存》《Bodycam》《Euro Truck Simulator 2》《我带过的最差一届》等已掉出返回窗口。下表里前两条做了第二层核对——除汇总接口外，另用 <code>appdetails</code> 逐款回读 <code>initial / final / discount_percent</code>，三项都对上；后三条只停在汇总接口这一层，按口径留在观察。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏（appid）</th><th style="padding:6px 8px 6px 0;">国区价</th><th style="padding:6px 8px 6px 0;">折扣</th><th style="padding:6px 8px 6px 0;width:20%;">截止（北京时间）</th><th style="padding:6px 0 6px 0;width:18%;">核实层级</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1771300/">天国：拯救2</a>（1771300）</td><td style="padding:8px 8px 8px 0;">¥228.00 → ¥75.24</td><td style="padding:8px 8px 8px 0;">-67%</td><td style="padding:8px 8px 8px 0;">11-30 18:00</td><td style="padding:8px 0 8px 0;color:#1a7f37;font-weight:700;">appdetails 回读</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5458210/">How They Built the Pyramids</a>（5458210）</td><td style="padding:8px 8px 8px 0;">¥22.00 → ¥15.40</td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 0 8px 0;color:#c0392b;font-weight:700;">11-20 18:00</td><td style="padding:8px 0 8px 0;color:#1a7f37;font-weight:700;">appdetails 回读</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3321460/">红色沙漠：增强版</a>（3321460）</td><td style="padding:8px 8px 8px 0;">¥268.00 → ¥214.40</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 8px 8px 0;">11-30 18:00</td><td style="padding:8px 0 8px 0;color:#8a9099;">仅汇总接口 → 观察</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/499170/">沉星之序</a>（499170）</td><td style="padding:8px 8px 8px 0;">¥98.00 → ¥78.40</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 8px 8px 0;">11-30 18:00</td><td style="padding:8px 0 8px 0;color:#8a9099;">仅汇总接口 → 观察</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5200620/">Dungeonbound</a>（5200620）</td><td style="padding:8px 8px 8px 0;">¥42.00 → ¥37.80</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 8px 8px 0;">11-30 18:00</td><td style="padding:8px 0 8px 0;color:#8a9099;">仅汇总接口 → 观察</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">口径与凌晨一致：汇总接口只返回滚动的前 10 条，掉出窗口不等于活动结束。核实于 2026-11-17 06:46。边界：付款前以商店页为准，本站不代下单。</p>
</details>

<details open>
<summary><strong>早间复核｜iOS 国区限免：1 款本体核到下载不花钱，5 条内购型只算转述</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
<p>凌晨 <code>appstore</code> 整源 ERR，所以那版只能写「本轮 iOS 限免未取」。早间 06:33 这一轮把汇总频道的 7 条播报逐条拿 <code>trackId</code> 回 <code>itunes.apple.com/lookup?id=&lt;trackId&gt;&amp;country=cn</code> 核了国区现价，结果分三种：</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">应用（trackId）</th><th style="padding:6px 8px 6px 0;width:14%;">播报口径</th><th style="padding:6px 8px 6px 0;width:18%;">iTunes 国区实测</th><th style="padding:6px 0 6px 0;">这一条能给什么结论</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://apps.apple.com/cn/app/id1294530516">我的待办 - 清单四象限日历提醒小组件</a>（1294530516）</td><td style="padding:8px 8px 8px 0;">本体限免</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">免费</td><td style="padding:8px 0 8px 0;">进「值得」：今天下载不花钱（开发者 Shanghai Paitui Technology，最低系统 17.0）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">选一下（6830170969）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;">免费</td><td style="padding:8px 0 8px 0;">只算转述：内购解锁价不体现在下载价上</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">MediaUtilityPro（6762476764）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;">免费</td><td style="padding:8px 0 8px 0;">只算转述，同上</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">SnipMark：截图标注与压缩（6827030851）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;">免费</td><td style="padding:8px 0 8px 0;">只算转述，同上</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">ShotPin（6825411577）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;">免费</td><td style="padding:8px 0 8px 0;">只算转述，同上</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Phomus - 整理相册，照见时光（6748335312）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;">免费</td><td style="padding:8px 0 8px 0;">只算转述，同上</td></tr>
<tr><td style="padding:8px 8px 8px 0;">Utly（6824127297）</td><td style="padding:8px 8px 8px 0;">内购限免</td><td style="padding:8px 8px 8px 0;color:#c0392b;">查不到上架记录</td><td style="padding:8px 0 8px 0;">价格未核实，只留频道原帖</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">三条口径要说在前面：<strong>① 没有截止时间</strong>——Apple 不公布促销结束时间，这一栏只能空着，绝不编日期；<strong>② <code>price==0</code> 只等于「今天下载不花钱」</strong>，接口分不出「本就免费」与「促销限免」，所以不写「限免仍在」；<strong>③ 认 id 不认名字</strong>，国区常给 app 改名，按名字匹配会认错 app、把别人的免费价安到这条上。核实于 2026-11-17 06:33。边界：下载与兑换由你自己完成；兑换码型限免不转载码本身，只留原帖。</p>
</details>

<details open>
<summary><strong>早间复核｜Trezor 官方公告：物流合作方 Skladon 泄露约 27,000 笔订单的收货信息</strong> ｜ <span style="color:#c0392b;font-weight:700;">此后自称 Trezor / Skladon 的改址与补发按钓鱼处理</span></summary>
<p>项目方博客一手原文（不是媒体转述）：泄露发生在 Trezor 的物流合作方 Skladon 一侧，涉及 <strong>2026-08-09 至 2026-11-07 之间约 27,000 笔订单</strong>，被导出的字段是姓名、电话、收货地址、邮箱；<strong>Trezor 自身系统未被入侵，硬件设备、私钥与资金不受影响</strong>。</p>
<p style="font-size:13px;"><strong>你要做的是</strong>：此后凡是自称 Trezor 或 Skladon 的短信、邮件、来电，内容涉及「修改收货地址」「重新发货」「包裹异常需要补料」，一律按钓鱼处理——官方不会通过这类渠道索要信息，更不会要助记词；任何情况下不透露助记词。要确认订单状态就自己从官网进，不要点短信与邮件里的链接。这是事件公告而不是限时活动，所以没有截止时间。</p>
<p style="font-size:13px;color:#6b7280;">出处：<a href="https://trezor.io/blog/news/data-breach-at-trezor-shipping-partner-skladon">trezor.io/blog/news/data-breach-at-trezor-shipping-partner-skladon</a>｜核实于 2026-11-17 06:44。边界：不代做任何链上操作，也不替你判断要不要重下设备。</p>
</details>

<details open>
<summary><strong>早间复核｜Kraken 服务状态整体 minor / Partially Degraded，最新事件 KAVA 充值延迟</strong> ｜ <span style="color:#c0392b;font-weight:700;">在 Kraken 有充提的自己复查一笔</span></summary>
<p>凌晨 <code>exstatus</code> 被代理通道挡住，所以那版没有服务状态这一层。早间 06:41 取到交易所自有 Statuspage（一手，非第三方监控）：Kraken <code>indicator=minor</code>、描述 <code>Partially Degraded Service</code>，最新事件 <code>Kava (KAVA) Funding Delays</code>，状态 identified，北京时间 2026-11-16 14:57；同一轮 Coinbase 是 <code>All Systems Operational</code>。状态页里另有 OSMO（11-14）、FLARE（11-11）、INIT（11-10）、Memecore 充值关闭（8-19）、USDR/EURR（5-24）等历史事件，超出最近 24 小时窗口，只作背景放观察。</p>
<p style="font-size:13px;color:#6b7280;">口径：<code>indicator</code> 不是 <code>none</code> 就提出「复查」，因为它影响的是<strong>在用资产的可得性</strong>；不用 Kraken 可以直接跳过这一条。本站不代操作充提、不碰任何链上动作，也不替你判断该不该提。</p>
<p style="font-size:13px;color:#6b7280;">出处：<a href="https://status.kraken.com/api/v2/summary.json">status.kraken.com/api/v2/summary.json</a>、<a href="https://status.coinbase.com/api/v2/status.json">status.coinbase.com/api/v2/status.json</a>｜核实于 2026-11-17 06:41。</p>
</details>

<details open>
<summary><strong>早间复核｜GitHub Trending 回到 API：4 个仓库补上总 star 与创建时间</strong> ｜ <span style="color:#6b7280;">06:31 抓榜、06:45 回读</span></summary>
<p>凌晨那张表已经给了总 star；早间这一轮榜单只剩 6 条（滚动窗口，与 00:22 那批不同），其中 4 个回到 <code>/repos/&lt;owner&gt;/&lt;name&gt;</code> 一手接口复核，数值比凌晨同一仓库高几十到几百——差值就是这六小时的增速：</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">仓库</th><th style="padding:6px 8px 6px 0;width:14%;">06:45 实测 star</th><th style="padding:6px 8px 6px 0;width:14%;">创建</th><th style="padding:6px 0 6px 0;">为什么值得点进去</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/mvanhorn/last30days-skill">mvanhorn/last30days-skill</a></td><td style="padding:8px 8px 8px 0;">68,080（00:22 为 67,930）</td><td style="padding:8px 8px 8px 0;">—</td><td style="padding:8px 0 8px 0;">跨 Reddit / X / YouTube / HN / Polymarket 做近 30 天调研再综合成报告的 Agent skill</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/getarcaneapp/arcane">getarcaneapp/arcane</a></td><td style="padding:8px 8px 8px 0;">8,669（00:22 为 8,514）</td><td style="padding:8px 8px 8px 0;">—</td><td style="padding:8px 0 8px 0;">自托管的现代化 Docker 管理面板，手上有 VPS 的可以直接试</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/kajisho5/ffmpeg-skill">kajisho5/ffmpeg-skill</a></td><td style="padding:8px 8px 8px 0;">6,615（00:22 为 6,360）</td><td style="padding:8px 8px 8px 0;">2026-09-03</td><td style="padding:8px 0 8px 0;">给 coding agent 用的本地视频编辑器：42 个 FFmpeg 工具、工具表机器可读，另带 MCP server</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://github.com/google-research/paper-orchestra">google-research/paper-orchestra</a></td><td style="padding:8px 8px 8px 0;">1,417（00:22 为 1,194）</td><td style="padding:8px 8px 8px 0;">2026-05-01</td><td style="padding:8px 0 8px 0;">多智能体的 AI 论文自动写作框架，正好对上「写作 + Agent 自动化」这条线</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">早间窗口另外两条：<a href="https://github.com/DeanChensj/jiangshan-map">DeanChensj/jiangshan-map</a>（江山时序 · 中国历史交互地图时间轴，6,664 star）与 <a href="https://github.com/sveltejs/svelte">sveltejs/svelte</a>（88,950 star），本轮没回到 API 复核，只按抓取原文列出。核实于 2026-11-17 06:45。边界：新库先读 README 与最近提交再决定用不用。</p>
</details>

## 观察（8 + 早间 13 组）、币圈那一轮与方法

<details>
<summary><strong>观察：8 条存疑或门槛高的条目</strong> ｜ <span style="color:#6b7280;">未核实的数字不当事实写</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:34%;">条目</th><th style="padding:6px 0 6px 0;">存疑原因</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">ColoCrossing 国外 VPS 五折，1 核 1GB / 25GB SSD 月付 $1.97 起</td><td style="padding:8px 0 8px 0;">来自美国主机侦探转述，未回厂商官网核对续费同价与截止时间</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Database Mart 黑五最高 75% off，Linux VPS 低至 $1.25/月</td><td style="padding:8px 0 8px 0;">同上，转述；配置档位与“最高优惠”是否同款未核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">DMIT 洛杉矶 LAX.EB 电信方向丢包波动，符合条件可申请按比例退款</td><td style="padding:8px 0 8px 0;">转述；退款条件与申请入口以商家公告为准</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Solana 基金会发布 Linux 内核漏洞安全提醒</td><td style="padding:8px 0 8px 0;">只有 PANews 转述，未回到 Solana 官方 advisory 或公告原文，先按观察处理</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Luxor 称遭 AI 赋能攻击、客户算力被重定向，漏洞已修补</td><td style="padding:8px 0 8px 0;">TheBlock 转述，未见项目方安全公告原文</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Upbit 母公司 Dunamu Q3 净亏损 1,400 万美元，营收同比 -61%</td><td style="padding:8px 0 8px 0;">媒体转述财报数字，未见原始财报</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">DBS 与 JPMorgan 上线美新两地代币化存款即时转账</td><td style="padding:8px 0 8px 0;">媒体转述，未核银行公告；与普通用户距离较远</td></tr>
<tr><td style="padding:8px 8px 8px 0;">Product Hunt 今日 15 条新品（含 ChatGPT Wallet、Zoom Slides 等）</td><td style="padding:8px 0 8px 0;">只取到榜单标题与链接，未逐条打开核实功能与定价；iOS 限免通道本轮失败，“今天没有 iOS 限免”不能从本轮数据推出</td></tr>
</tbody></table>
</details>

<details>
<summary><strong>早间复核新增观察（13 组）</strong> ｜ <span style="color:#6b7280;">未核实的数字不当事实写，缺截止时间就不升档</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:34%;">条目</th><th style="padding:6px 0 6px 0;">存疑原因</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Steam 另外三条折扣（<a href="https://store.steampowered.com/app/3321460/">红色沙漠：增强版</a> ¥214.40、<a href="https://store.steampowered.com/app/499170/">沉星之序</a> ¥78.40、<a href="https://store.steampowered.com/app/5200620/">Dungeonbound</a> ¥37.80，截止均 11-30 18:00）</td><td style="padding:8px 0 8px 0;">只来自 <code>featuredcategories</code> 汇总接口，本轮未逐款回 <code>appdetails</code> 复核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170499.html">Database Mart 黑五促销</a>：最高 75% off、Linux VPS $1.25/月、独立服务器 $21.60/月起</td><td style="padding:8px 0 8px 0;">转述源可读，但官方页未公布活动截止时间——缺截止这一栏按口径不能进「值得」，续费价同样未核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170518.html">ColoCrossing 国外 VPS 五折</a>：1 核 1GB / 25GB SSD 月付 $1.97 起</td><td style="padding:8px 0 8px 0;">只有转述；官方站 <code>colcrossing.com</code> 与 <code>colo-crossing.com</code> 本轮经代理均返回 <code>000</code> 不可达，价格与截止都没核到</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.ithome.com/1/027/858.htm">WPS 京东 PLUS 联合会员 191 元返场</a>（单个会员 1 年 47 元）、<a href="https://www.ithome.com/1/027/966.htm">iPad mini（A20 Pro）国补后 5499 → 4499</a></td><td style="padding:8px 0 8px 0;">均需登录京东才能核最终到手价与名额；返场与国补多为限时限量，未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">App Store 内购限免 5 条 + Utly 查不到 id</td><td style="padding:8px 0 8px 0;">内购解锁不体现在下载价上，iTunes 只能证明「下载不花钱」，整类按频道转述处理；Utly 播报 id 6824127297 在 iTunes 无上架记录，价格未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.coindesk.com/tech/2026-11-16/lighter-suspends-all-withdrawals-after-usd10-4-million-crypto-exploit">Lighter 暂停全部提现</a>（涉 $10.4M exploit）</td><td style="padding:8px 0 8px 0;">仅媒体转述，<code>docs.lighter.xyz</code> 只有 security / vulnerability disclosure 页，未取到项目方一手暂停公告——按「安全事件只认一手」降为观察</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Kraken 其余历史事件（OSMO 11-14、FLARE 11-11、INIT 11-10、Memecore 充值关闭 8-19、USDR/EURR 5-24）</td><td style="padding:8px 0 8px 0;">官方状态页可读，但都超出最近 24 小时窗口，只作背景</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">币安两条公告：<a href="https://www.binance.com/en/support/announcement/detail/5f041987d1ca4252a3c59ad27eff3e28">Pay Later 下月初前 0% 利率</a>、<a href="https://www.binance.com/en/support/announcement/detail/d1bc1b9ca8ab4bb9800b205162964aea">bStocks 支持 MSFT / AMAT 现金分红</a></td><td style="padding:8px 0 8px 0;">公告接口不返回发布日期（<code>publishDate</code> / <code>releaseDate</code> 实测为 None），日期只写在标题尾巴而这两条没有——时效未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">行情与热搜快照（06:33）</td><td style="padding:8px 0 8px 0;">数字不是信息，涨跌本身不构成价值；详见下一张「币圈那一轮」的早间表格</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.cs.cmu.edu/learn/">卡内基梅隆把 CS 课程放上 YouTube</a>（HN 117 分 / 24 评）</td><td style="padding:8px 0 8px 0;">官方页可读且 200，但 YouTube 侧课程清单未逐条核对是否完整、是否持续更新</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">三条安全类一手披露：<a href="https://iter.ca/post/ubo-uxss/">uBlock Origin 通用型 XSS</a>、<a href="https://amirulcyber.com/2026-11-16/optimjack-optimizely-skimmer/">Optimizely 被植入 skimmer</a>、<a href="https://www.openwall.com/lists/oss-security/2026-11-15/2">NoisyTCP</a>（oss-security）</td><td style="padding:8px 0 8px 0;">原文都在，但修复版本、影响范围与是否影响你当前环境未确认；涉及操作时只按官方公告升级 / 撤销授权，不自己发挥</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.v2ex.com/t/1257320">v2ex「HyperAPI 中转站评论留 ID 送 $10 体验额度」</a>（66 回）</td><td style="padding:8px 0 8px 0;">第三方 API 中转站的引流活动，兑现要公开留账号 ID 且无官方背书；按边界不作推荐、不写刷额度玩法</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://lowendbox.com/blog/raptors-testing-the-fences-whos-really-commenting-on-your-reddit-posts-is-it-90-bots-guys/">LowEndBox 本轮唯一一条：Reddit 评论有多少是机器人</a></td><td style="padding:8px 0 8px 0;">是行业观察不是优惠；本轮这一源只有这一条，无价格可核</td></tr>
</tbody></table>
</details>

<details>
<summary><strong>币圈那一轮：凌晨只通了媒体轴，早间四条轴全通</strong> ｜ <span style="color:#6b7280;">凌晨 11 个源里 2 个可用 → 早间 11 个全绿</span></summary>
<p>本轮币圈 11 个机器可读源里，只有 <code>theblock</code>（12 条）与 <code>panews</code>（15 条）取到数据，另有 <code>fng</code> 直连取到情绪指数 1 条。<code>binance</code> 公告、<code>exstatus</code>（Coinbase / Kraken 状态）、<code>cgmarkets</code> / <code>coingecko</code> / <code>cmc</code>（行情与热搜）、<code>ethblog</code> / <code>creleases</code>（项目方一手与发版）、<code>coindesk</code> 全部被代理通道挡住，返回 URLError 或被超时截断。所以今天没有交易所上币/下架、充提开关与链上安全事件的一手核对结果；<strong>没有取到不等于没有发生</strong>，涉及资产操作请自行打开交易所公告页确认。</p>
<p style="font-size:13px;color:#6b7280;"><strong>早间 06:30–06:41 这一轮这四条轴全部通了</strong>（<code>binance</code> 2 条、<code>exstatus</code> 1 条聚合、<code>cgmarkets</code> 6 条、<code>coingecko</code> 热搜 10 条、<code>cmc</code> 6 条、<code>fng</code> 1 条、<code>panews</code> 15 条、<code>coindesk</code> 12 条、<code>theblock</code> 12 条，<code>ethblog</code> / <code>creleases</code> 两天窗口内确无新条目，均非故障），所以上面那句「没有一手核对结果」只对凌晨那一轮成立。交易所一手层的结果是两张卡：Kraken 状态与 Trezor 物流方泄露，都在「值得」里。行情与热搜仍是快照：</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">指标</th><th style="padding:6px 8px 6px 0;width:30%;">06:33 快照</th><th style="padding:6px 0 6px 0;">口径</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">BTC / ETH / BNB</td><td style="padding:8px 8px 8px 0;">$65,314（+0.2%）/ $1,832.67（+0.2%）/ $593.78（-0.2%）</td><td style="padding:8px 0 8px 0;">CoinGecko 市值前 5（USDT $0.999388、USDC $0.999681）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">异动</td><td style="padding:8px 8px 8px 0;">Rain +71.8%、ICP +14.1%、JUP -8.3%、Midnight -8.1%、Bitway -31.5%</td><td style="padding:8px 0 8px 0;">只看市值前 300 且 24h 绝对涨跌 ≥ 8%</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">CoinGecko 热搜前 10</td><td style="padding:8px 8px 8px 0;">Solana、Macca the Gator、BTC、Lighter、Backpack、Pudgy Penguins、Bittensor、Ondo、Hyperliquid、Avalanche</td><td style="padding:8px 0 8px 0;">热度，不是涨跌</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">CMC 搜索榜前 6</td><td style="padding:8px 8px 8px 0;">Spacecoin、Hyperliquid、Bless、Internet Computer、Lighter、Huma Finance</td><td style="padding:8px 0 8px 0;">热度，不是涨跌</td></tr>
<tr><td style="padding:8px 8px 8px 0;">恐惧贪婪指数</td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">10（Extreme Fear）</td><td style="padding:8px 0 8px 0;">alternative.me，06:33 与凌晨同值，只作语境底数</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">快照会随时间走，超过两小时就不该当今天的数字读；不写买卖建议、目标价、钱包地址与带返利参数的邀请链接，落地链接已剥成干净 URL。</p>
</details>

<details>
<summary><strong>方法与来源健康度：凌晨 25 源里 11 个通道失败 → 早间同一批全部恢复、errors=0</strong> ｜ <span style="color:#6b7280;">含 ERR 原文</span></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">来源</th><th style="padding:6px 8px 6px 0;width:16%;">本轮条数</th><th style="padding:6px 0 6px 0;">状态 / 备注</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">hackernews / lobsters / ithome / producthunt</td><td style="padding:7px 8px 7px 0;">15 / 15 / 15 / 15</td><td style="padding:7px 0 7px 0;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">panews / theblock / trending</td><td style="padding:7px 8px 7px 0;">15 / 12 / 14</td><td style="padding:7px 0 7px 0;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">steam</td><td style="padding:7px 8px 7px 0;">10</td><td style="padding:7px 0 7px 0;color:#c0392b;">脚本通道超时，改用 curl 走同一官方接口补齐</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">idcspy / lowendbox / epic / fng / ruanyifeng</td><td style="padding:7px 8px 7px 0;">5 / 2 / 1 / 1 / 1</td><td style="padding:7px 0 7px 0;">正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">appinn</td><td style="padding:7px 8px 7px 0;">0</td><td style="padding:7px 0 7px 0;">本轮无符合条件的新条目（非故障）</td></tr>
<tr><td style="padding:7px 8px 7px 0;color:#c0392b;">v2ex / hf / binance / exstatus / coingecko / cgmarkets / cmc / ethblog / creleases / coindesk / appstore</td><td style="padding:7px 8px 7px 0;color:#c0392b;">0</td><td style="padding:7px 0 7px 0;color:#c0392b;">ERR（URLError / 超时），代理通道不可用。appstore 失败意味着本轮 iOS 限免未取，不是“没有限免”。</td></tr>
</tbody></table>
<p style="font-size:13px;color:#6b7280;">取数：<code>radar_fetch.py</code> 25 源，逐源超时隔离执行；成功 12 源，Steam 另行用 curl 补取，合计 121 条。验真：Steam / Epic / alternative.me 均回官方接口核对，IT之家与其他媒体条目按“转述”标注；第三方 VPS 优惠未回官网，全部留在观察段。发布：本地存档 <code>2026-11-17-info-radar.md</code>，GitHub Pages 本篇 <code>/posts/info-radar-2026-11-17/</code>。</p>
<p style="font-size:13px;color:#6b7280;"><strong>早间第二轮（06:30:45–06:31:52 取数，06:33–06:46 验真）</strong>：<code>SUMMARY fetched=314 fresh=179 sources=25 errors=0</code>，一轮 67 秒、<strong>无一条 ERR</strong>。上表红字那 11 个源这一轮全部返回成功（IT之家 25、HN 25、lobsters 17、PANews 15、Product Hunt 14、CoinDesk 12、The Block 12、v2ex 10、CoinGecko 热搜 10、App Store 7、GitHub Trending 6、CoinGecko 行情 6、CMC 6、Steam 5、IDCSPY 4、币安 2、LowEndBox 1、交易所状态 1、恐惧贪婪 1）；0 条的 6 个源里，Epic 是本周限免已被 <code>history.jsonl</code> 去重命中（数值改由 06:44 直接回官方接口读到，仍是 0 元 / 11-20 00:00），hf、阮一峰、appinn、ethblog、creleases 是两天窗口内确无更新，都不是取数失败。境外源整批挂、境内源全绿这个形态，两轮对照下来确认是代理节点抖动，不是站点集体改版。</p>
<p style="font-size:13px;color:#6b7280;">需要点名的一处取数偏差：本次运行里 CSDN 后台的发文统计来自创作中心列表页的 DOM，官方签名接口 <code>phoenix/console/v1/article/list</code> 的 XHR 观测没能装上，所以那几个发文数字不是接口层证据；公众号后台本轮「登录超时」，未取数、也没有代填任何凭据。这两项属于打卡与发文块，不在雷达三段里，但一并写清楚。</p>
</details>
