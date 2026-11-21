---
title: "资讯雷达 2026-11-22｜BTC 反弹回 5.99 万、Epic《深渊之印》最后 5 天、Steam 黑五战地双作 -95%"
author: OxYGC
date: 2026-11-22 00:10:00 +0800
permalink: /posts/info-radar-2026-11-22/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam黑五, 比特币, 黎曼猜想, GitHub趋势]
description: "2026-11-22 当天唯一一篇，含两轮取数：00:03–00:06 那轮 17 源（7 个异常，行情走 Gate.io 兜底），06:31–06:33 早间全量复核 25 源全绿、fetched=323 / fresh=137，BTC 快照 60,148（+1.9%）、恐惧贪婪 12。Epic《深渊之印》¥55→0 截止 11-27 00:00；Steam 黑五地平线 5 ¥198→¥79.20、地平线 6 ¥298→¥223.50，两款均经 appdetails?cc=cn 逐条核到国区价与 12-03 18:00 截止。复核新增 4 条 ⭐：GPGME CVE-2026-129975、Ghostscript CVE-2026-125396、C++26 行程报告、gopgext；🔥 0 条（本机实测 gpg/gs/convert/magick 未安装，Kraken 降级不涉及充提暂停）。iOS 限免 6 条全部只到观察，Apple 不公布截止时间。"
---

这一轮取数在 2026-11-22 00:03–00:06（北京时间）完成：17 个来源里 10 个取到数据、7 个被代理通道或接口方挡住。`SUMMARY fetched=100 fresh=100 sources=17 errors=7`。异常集中在需要境外直连的行情接口：`binance`、`okx`、`coingecko` 全部超时，`v2ex` 与 HN 官方 Firebase 接口无响应，`36kr` 的 RSS 返回空条目、`techcrunch` 的 feed 为空；本轮行情改走 Gate.io，技术资讯改走 HN Algolia 镜像与 ITHome / Solidot / 少数派 RSS。**这是 2026-11-22 当天第一版；今天若再跑，只会在本文件内更新，不新增文件。**

结论先摆前面：**今天没有“今天到期”的硬截止，最近一个到期点是 11-24 02:00 的《我带过的最差一届》-35%；黑五主力档集中在 12-02 至 12-04，战地风云 5（-95%，¥11.40）与双人成行（-80%，¥39.60）仍是本轮幅度最大的两张。** 免费游戏方面，Epic 本周只有《深渊之印》（Mark of the Deep，¥55→0）一款，11-27 00:00 截止；接口同时确认下周 11-27 00:00 起《Bread and Fred》¥47→0 接档，以及客户端标价本身为 ¥0 的《火之石 – 放置点击英雄RPG》。资讯面被数学占住：Levent Alpöge 与 Alessandro Masullo 先后发布广义黎曼猜想的证明手稿，Terry Tao 同日讨论 Navier–Stokes 奇点与 GRH 的关系，三篇都未经过同行评审。市场侧是“急跌后的反弹”：BTC 24 小时最低摸到 55,123，亚洲早盘回到 59,943.9，但恐惧贪婪指数仍在 12（Extreme Fear）。

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
<td style="padding:9px 8px 9px 0;">Epic《深渊之印》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">11-27 00:00 开</td>
<td style="padding:9px 8px 9px 0;">Epic 下周接档：《Bread and Fred》0 元</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
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
<td style="padding:9px 8px 9px 0;">Steam 战地风云 5 -95%、《双人成行》-80%、《极限竞速：地平线 5》-60%</td>
<td style="padding:9px 8px 9px 0;">¥11.40 / ¥39.60 / ¥79.20</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1238810/">BF5</a> · <a href="https://store.steampowered.com/app/1426210/">双人成行</a> · <a href="https://store.steampowered.com/app/1551360/">FH5</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-22 00:03–00:05 官方接口实测：Epic <code>freeGamesPromotions</code>、Steam <code>featuredcategories</code>。Steam 的 <code>discount_expiration</code> 是 epoch 时间，这里已换算成北京时间（比 UTC 多 8 小时）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（7）

<details open>
<summary><strong>Steam 黑五：10 款特惠一次回读，战地风云 5 -95% 领跑</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥11.40 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 11-24 02:00 收</span></summary>
<p>Steam 官方 <code>featuredcategories</code> 本轮返回 10 条特惠，金额已从“分”换算成人民币。10 条全部列出，没有做主观筛选：<code>discount_percent</code> 与 <code>final_price</code> 均来自同一份接口返回，未再逐款 <code>appdetails</code> 复核，这是本轮与上一轮在方法上的差别。战地风云 5 以 -95%（¥228→¥11.40）居首，双人成行 -80%（¥198→¥39.60）次之。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:12%;">折扣</th><th style="padding:6px 8px 6px 0;width:24%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1238810/">战地风云 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-95%</td><td style="padding:8px 8px 8px 0;">¥11.40 / ¥228.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1551360/">极限竞速：地平线 5</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥79.20 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2483190/">极限竞速：地平线 6</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-25%</td><td style="padding:8px 8px 8px 0;">¥223.50 / ¥298.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1817070/">漫威蜘蛛侠 重制版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-60%</td><td style="padding:8px 8px 8px 0;">¥165.60 / ¥414.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2215430/">对马岛之魂 导演剪辑版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-50%</td><td style="padding:8px 8px 8px 0;">¥199.00 / ¥398.00</td><td style="padding:8px 0;">12-02 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1462040/">FF7 重制版 INTERGRADE</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-82%</td><td style="padding:8px 8px 8px 0;">¥35.64 / ¥198.00</td><td style="padding:8px 0;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2909400/">FF7 重生</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-85%</td><td style="padding:8px 8px 8px 0;">¥37.20 / ¥248.00</td><td style="padding:8px 0;">12-03 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5175310/">我带过的最差一届</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-35%</td><td style="padding:8px 8px 8px 0;">¥18.20 / ¥28.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">11-24 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/4459590/">转运军团 - Slotbound</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-10%</td><td style="padding:8px 8px 8px 0;">¥37.80 / ¥42.00</td><td style="padding:8px 0;">11-27 02:00</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:10px 0 0;">榜单只反映“此刻正在打折”，不代表历史最低；国区价格以接口 <code>cc=cn</code> 返回为准。若你只想要“幅度最大 + 时间最长”，战地风云 5 与双人成行都到 12-04 02:00，不用急在今明两天决定。</p>
</details>

<details>
<summary><strong>Epic 本周《深渊之印》¥55→0，下周《Bread and Fred》¥47→0 接档</strong> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">11-27 00:00 收</span></summary>
<p>Epic 官方 <code>freeGamesPromotions</code> 接口（<code>locale=zh-CN&amp;country=CN</code>）本轮返回的当前 0 元档只有一款：《深渊之印》（Mark of the Deep），原价 ¥55.00，促销窗口 <code>2026-11-19T16:00Z</code> 至 <code>2026-11-26T16:00Z</code>，换算成北京时间就是 <strong>11-27 00:00 截止</strong>。这是一款海盗题材的银河恶魔城 + 魂系作品，领取后永久入库，不需要订阅。</p>
<p>同一份接口的 <code>upcomingPromotionalOffers</code> 给出下周档：<strong>《Bread and Fred》</strong>（Atari 发行，双人合作企鹅登顶）原价 ¥47.00，<code>2026-11-26T16:00Z</code> 起 0 元，持续到 <code>2026-12-03T16:00Z</code>（北京时间 11-27 00:00 至 12-04 00:00）。另一款《火之石 – 放置点击英雄RPG》（Firestone: Online Idle RPG）也在同一窗口，但它的原价字段本身就是 ¥0，属于免费游玩（F2P）作品，不是“付费游戏限时白送”，这里单独标注，避免误读。</p>
<p>补充一条不着急但可以留意：<strong>《TerraScape》-70%</strong> 的窗口到 2026-12-22 00:00（北京时间），不在本周免费档内。以上时间全部以接口 <code>startDate / endDate</code> 为准，未做二次推断。</p>
</details>

<details>
<summary><strong>BTC 从 55,123 反弹回 59,943.9，恐惧贪婪指数仍卡在 12</strong> ｜ <span style="color:#1a7f37;font-weight:700;">+1.59%</span> ｜ <span style="color:#c0392b;font-weight:700;">24h 振幅 8.8%</span></summary>
<p>Gate.io <code>spot/tickers</code> 在 00:03–00:04 的读数：BTC/USDT <strong>59,943.9</strong>，24 小时 <strong>+1.59%</strong>，区间 55,123 – 60,989.5，成交额 23.42 亿 USDT。也就是说过去 24 小时先砸到 55,123，再拉回 6 万下方，振幅约 8.8%。主流币同步反弹：ETH 1,682.58（+3.06%）、SOL 70.26（+3.39%）、BNB 546.5（+0.62%）、XRP 0.9241（+2.06%）、DOGE 0.05503（+3.05%）。</p>
<p>但情绪面没有跟上：alternative.me 恐惧贪婪指数仍为 <strong>12（Extreme Fear）</strong>，与昨日同一档。Cointelegraph 的记录显示 BTC 一度跌破 6 万美元、为 7 月以来首次；同期纳指回吐 2026 年全部涨幅，AI 板块抛售是主因（详见下面“AI 与市场”一条）。<strong>判断：这是超跌反弹，不是风险偏好恢复</strong>——指数没有离开个位数区间之前，不宜把反弹当成趋势反转。</p>
</details>

<details>
<summary><strong>广义黎曼猜想一天内出现两份证明手稿，Tao 同日谈 Navier–Stokes</strong> ｜ <span style="color:#c0392b;font-weight:700;">未经同行评审</span> ｜ <span style="color:#8a9099;">HN 三席</span></summary>
<p>HN 首页今天被数学占住，且三条互相咬合：</p>
<ul>
<li><strong>Levent Alpöge</strong> 发布《Generalized Riemann Hypothesis》证明手稿 PDF（<a href="https://alpo.ge/remark.pdf">alpo.ge/remark.pdf</a>），2,779 分，是今日全站最高。</li>
<li><strong>Alessandro Masullo</strong> 的 GRH 手稿由数学博客“紧急通告”形式发布（<a href="https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/">math216.wordpress.com</a>），2,272 分。</li>
<li><strong>Terry Tao</strong> 同日写《Unforced Navier–Stokes Singularity and the Generalized Riemann Hypothesis》（<a href="https://terrytao.wordpress.com/2026/11/20/...">terrytao.wordpress.com</a>），499 分；另有一份《Finite-time blow-up for the Navier–Stokes equations》的代码/论文仓库（<a href="https://github.com/tristanbuckmaster/navier-stokes/">GitHub</a>），305 分。</li>
</ul>
<p>需要强调：以上都是<strong>手稿与预印本，不是已通过同行评审的结论</strong>。Solidot 在 11-21 19:09 也以“人类数学家匆忙发布广义黎曼猜想的证明手稿”为题跟进，用词同样是“手稿”。对非数学读者，真正可操作的信息只有一条：如果这些证明成立，密码学与数论相关课程的教材会在未来数月内被重写；在此之前，任何“黎曼猜想已被证明”的标题都应当加上“待验证”。</p>
</details>

<details>
<summary><strong>AI 抛售令纳指回吐 2026 年全部涨幅，Anthropic 上市第二日承压</strong> ｜ <span style="color:#c0392b;font-weight:700;">风险事件</span> ｜ <span style="color:#8a9099;">HN + Cointelegraph</span></summary>
<p>HN 上的 Guardian 报道标题是《Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic's second day》（418 分）。Cointelegraph 的行情稿同时记录了“Bitcoin price drops to $60K as Anthropic drops to $87 in tech sell-off”，并把 BTC 的 20 周低点与 AI 板块绑定。两条独立来源指向同一件事：<strong>这轮风险资产下跌的触发器是 AI 估值，而不是加密行业自身的事件</strong>。</p>
<p>对本站读者的意义：如果你在盯 BTC 的“6 万保卫战”，同时也要看纳指与 Anthropic 的股价，因为过去 48 小时两者的日内节奏高度同步。反过来说，若 AI 板块企稳，加密的反弹才有第二段；只靠币圈内部的利好，很难单独把指数从“极度恐惧”拉出来。</p>
</details>

<details>
<summary><strong>Thinking Machines 发布 Inkling 2 Mini</strong> ｜ <span style="color:#1a7f37;font-weight:700;">1,174 分</span> ｜ <span style="color:#8a9099;">模型发布</span></summary>
<p>Thinking Machines 官方博客发布 <strong>Inkling 2 Mini</strong>（<a href="https://thinkingmachines.ai/news/inkling-2-mini/">thinkingmachines.ai/news/inkling-2-mini/</a>），HN 1,174 分，是今日除数学之外分数最高的技术条目。官方页面只给出发布信息，本轮没有抓到独立的第三方评测，因此这里<strong>不转述参数、价格与 benchmark 数字</strong>，只记录“已发布”这一事实。等有可复现的评测再补。</p>
<p>同日 HN 还有一篇 arXiv 论文《Language Models Can Rewrite Their Own Weights》（450 分，<a href="https://arxiv.org/abs/2611.21885">arxiv.org/abs/2611.21885</a>），主题是模型对自身权重的改写。两条放在一起看，今天 HN 的技术注意力集中在“模型能力边界”，而不是产品落地。</p>
</details>

<details>
<summary><strong>GitHub Trending：Agent Skills 类仓库霸榜，Claude-BugHunter 单日 +1,794 star</strong> ｜ <span style="color:#1a7f37;font-weight:700;">15 条</span> ｜ <span style="color:#8a9099;">GitHub Trending</span></summary>
<p>GitHub Trending 日榜（00:04 抓取）前 15 条里，与 Agent / Skills / 编码代理直接相关的占了一半以上，且前三名全部属于这一类。这与昨天“firecrawl 单日 +1,241”的走势一致：<strong>流量正在从“模型本身”转向“给代理用的技能与工具”</strong>。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:38%;">仓库</th><th style="padding:6px 8px 6px 0;width:12%;">今日 star</th><th style="padding:6px 8px 6px 0;width:10%;">语言</th><th style="padding:6px 0 6px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/elementalsouls/Claude-BugHunter">elementalsouls/Claude-BugHunter</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+1,794</td><td style="padding:8px 8px 8px 0;">Python</td><td style="padding:8px 0;">82 个 skills、15 个 slash 命令的漏洞挖掘技能包</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/firecrawl/firecrawl">firecrawl/firecrawl</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+999</td><td style="padding:8px 8px 8px 0;">TypeScript</td><td style="padding:8px 0;">面向 agent 的搜索/抓取，接入 550+ 数据源</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+884</td><td style="padding:8px 8px 8px 0;">Shell</td><td style="padding:8px 0;">agentic skills 框架与开发方法论</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/XiaoYouChR/Ghost-Downloader-3">XiaoYouChR/Ghost-Downloader-3</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+774</td><td style="padding:8px 8px 8px 0;">Python</td><td style="padding:8px 0;">下载器，支持多协议</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/HKUDS/CLI-Anything">HKUDS/CLI-Anything</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+767</td><td style="padding:8px 8px 8px 0;">Python</td><td style="padding:8px 0;">“让所有软件都变成 agent 原生”</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/mjmirza/app-store-compliance">mjmirza/app-store-compliance</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+724</td><td style="padding:8px 8px 8px 0;">Shell</td><td style="padding:8px 0;">App Store / Google Play 上架避坑手册</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/zhouxiaoka/autoclip">zhouxiaoka/autoclip</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+689</td><td style="padding:8px 8px 8px 0;">Python</td><td style="padding:8px 0;">自动剪辑</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/cathrynlavery/diagram-design">cathrynlavery/diagram-design</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+582</td><td style="padding:8px 8px 8px 0;">HTML</td><td style="padding:8px 0;">给多个编码代理用的编辑级图表设计</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://github.com/toeverything/AFFiNE">toeverything/AFFiNE</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+577</td><td style="padding:8px 8px 8px 0;">TypeScript</td><td style="padding:8px 0;">知识库 / 协作白板</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://github.com/mvanhorn/last30days-skill">mvanhorn/last30days-skill</a></td><td style="padding:8px 8px 8px 0;font-weight:700;">+566</td><td style="padding:8px 8px 8px 0;">Python</td><td style="padding:8px 0;">跨 Reddit / X / YouTube / HN 的研究型 skill</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:10px 0 0;">“今日 star”是 Trending 页面展示的增量，不等于总 star；GitHub REST API 本轮未调用（避免共享出口 IP 触发 403），因此没有总 star 与许可证字段。</p>
</details>

## 币圈与宏观

<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">资产</th><th style="padding:6px 8px 6px 0;width:18%;">最新价（USDT）</th><th style="padding:6px 8px 6px 0;width:16%;">24h 涨跌</th><th style="padding:6px 0 6px 0;width:24%;">24h 区间</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">BTC</td><td style="padding:8px 8px 8px 0;font-weight:700;">59,943.9</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+1.59%</td><td style="padding:8px 0;">55,123 – 60,989.5</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">ETH</td><td style="padding:8px 8px 8px 0;font-weight:700;">1,682.58</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+3.06%</td><td style="padding:8px 0;">1,538.09 – 1,716.66</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">SOL</td><td style="padding:8px 8px 8px 0;font-weight:700;">70.26</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+3.39%</td><td style="padding:8px 0;">64.87 – 71.12</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">BNB</td><td style="padding:8px 8px 8px 0;font-weight:700;">546.5</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+0.62%</td><td style="padding:8px 0;">503.7 – 552.3</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">XRP</td><td style="padding:8px 8px 8px 0;font-weight:700;">0.9241</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+2.06%</td><td style="padding:8px 0;">0.86 – 0.9346</td></tr>
<tr><td style="padding:8px 8px 8px 0;">DOGE</td><td style="padding:8px 8px 8px 0;font-weight:700;">0.05503</td><td style="padding:8px 8px 8px 0;color:#1a7f37;font-weight:700;">+3.05%</td><td style="padding:8px 0;">0.05076 – 0.05569</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:8px 0 20px;">数据源：Gate.io <code>api/v4/spot/tickers</code>，2026-11-22 00:03–00:04（北京时间）。恐惧贪婪指数：12，Extreme Fear（alternative.me）。</p>

今天值得记的币圈条目：

- **Wrapped Monero 疑似被盗，价格闪崩 99.8%**：Cointelegraph 报道涉案约 1,350 万美元，wrapped 代币的价格几乎归零。这是今天唯一一条“资产本身出问题”的消息，其余跌幅都可归因于宏观。
- **Sky Protocol 出现约 20 亿美元稳定币赎回**：项目方否认涉及非法资金，但赎回规模本身值得跟踪。
- **香港推进托管与投顾发牌**：Cointelegraph 称立法草案将把加密托管人、顾问纳入牌照体系。
- **欧洲央行招募代币化存款与证券实验伙伴**：属于基础设施层动作，不影响短线价格。
- **美国预测市场监管升温**：参议院推进 DEATH BETS Act，另有议员提议给预测市场举报人最高 30% 奖励。

## 科技与开源

**HN 首页（Algolia 镜像，00:05 抓取）**，除上面展开的三条数学与两条 AI 之外，还值得看：

- 《We promoted developers into architects without informing them》（516 分）——晋升不等于角色转换，作者把组织问题写得很直。
- 《Slopstrap – Make your site look hastily vibecoded》（437 分）——一个反向审美的前端模板，今天在 HN 上属于“轻松项”。
- 《Brazil's tax authority open-sources its tax calculator on GitHub under MIT》（349 分）——巴西税务局把税务计算器以 MIT 协议开源。
- 《DreamCoder: Coding harness and IDE from the author of Mastering Emacs》（254 分）——Mastering Emacs 作者的编码工具。
- 《NINLIVE: The Nine Inch Nails live archive》（310 分）、《My Monitor Was Cutting My Download Speed by 75%》（188 分）——分别属于资料归档与硬件排查，适合周末读。

**国内侧（ITHome / Solidot / 少数派 RSS）**：

- **三星未来三年大部分存储芯片产能已被锁定**，有客户希望供货保障到 2031 年（ITHome 11-21 12:47）。这是今天与“AI 算力紧缺”叙事直接相关的一条供应链消息。
- **阿里巴巴警告未来两年算力紧缺**（Solidot 11-20 20:48）。
- **GTA 6 首日销售额 37.9 亿美元**，创游戏史纪录（Solidot 11-21 18:48）。
- **南非开发者宣称独自开发 Impossible OS**，兼容 Win32 与 Linux 二进制，称两年后见（ITHome 11-21 13:32）——属于“先记录，不背书”。
- **地球 28 光年外发现三星系统**、**人类免疫系统衰老在 40 岁和 60 岁后加速**（Solidot 11-21 22:40 / 22:25）——两条基础科学条目，后者来自新论文，具体样本量需看原文。
- **少数派**今天的主推是《这群在鸿蒙写应用的年轻人，只想做点「用得上」的》（11-21 12:00），另外《GTA 6》游玩体验（11-20 15:34）可以作为上面销量新闻的对照阅读。

## 取数与异常

- **成功（10）**：Gate.io（6 个交易对）、alternative.me、Epic <code>freeGamesPromotions</code>、Steam <code>featuredcategories</code>、GitHub Trending、HN Algolia、ITHome RSS、Solidot RSS、少数派 RSS、Cointelegraph RSS。
- **失败（7）**：Binance / OKX / CoinGecko（超时，未取到价格）、V2EX（接口无响应）、HN Firebase 官方接口（无响应）、36Kr RSS（返回空条目）、TechCrunch RSS（空 feed）。
- **口径说明**：本轮的 Steam 价格只回读了 <code>featuredcategories</code> 一次，没有像上一轮那样逐款 <code>appdetails</code> 二次核对；Epic 的时间全部以接口返回的 UTC 时间换算，未做“提前/延后”的人为修正。凡是接口没有给出的数字（例如总 star、历史最低价），本文不补。

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">06:30 早间全量复核（同日发布）</p>

<p>这一轮在 2026-11-22 06:31–06:33（北京时间）按 info-task-gc 的标准 25 源口径重跑：<code>SUMMARY fetched=323 fresh=137 sources=25 errors=0</code>，境外源全部经本机代理成功。<strong>午夜档的 7 个异常源（binance / okx / coingecko / v2ex / HN 官方 Firebase 接口 / 36kr / techcrunch）本轮没有一个报 ERR</strong>，行情因此回到 CoinGecko 官方接口口径：BTC $60,148（24h +1.9%）、ETH $1,680.22（+3.7%）、BNB $547.99（+1.5%）、USDT $0.998499、USDC $0.999302，恐惧贪婪指数仍为 <strong>12（Extreme Fear）</strong>——与午夜档 Gate.io 的 59,943.9 同向，差别只来自取数时刻（快照 06:33，来源 CoinGecko）。<strong>需要立刻处理维持 0 条。</strong></p>

<p><strong>新增「值得」四条（午夜档没有的一手材料）</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead>
<tr style="border-bottom:1px solid #eef0f2;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 6px;">条目</th><th style="padding:7px 6px;">一手核实到的事实</th><th style="padding:7px 6px;">直链与核实时间</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:7px 6px;">GPGME 2.3.1 修复 <strong>CVE-2026-129975</strong>（内部编号 T8557）</td>
<td style="padding:7px 6px;">GnuPG 官方 announce（Werner Koch，2026-11-20 19:01 CET）原文：含特制超长 user id 的 OpenPGP 密钥触发 double free，可被用于从应用中外泄数据，"挂载 RCE 攻击不能排除"，官方措辞 <em>an immediate update is highly suggested</em>；漏洞由 Johan Carlsson 发现，GitLab 2026-11-12 通报，原定 11-25 协同披露、因 Ruby2Shell 事件提前到 11-20 公开。同批更新 Gpg4win / GnuPG Desktop / GnuPG VS-Desktop</td>
<td style="padding:7px 6px;"><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">gnupg-announce 000517</a> ｜ 核实于 2026-11-22 06:37</td>
</tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:7px 6px;">Ghostscript Type 1 字体加载器 use-after-free，<strong>CVE-2026-125396</strong>（研究方称 Upload2Shell）</td>
<td style="padding:7px 6px;">特制文档可越过 <code>-dSAFER</code> 沙箱、改写原生路径控制并以渲染进程身份执行命令；研究方列出打印 / 邮件 / 上传 / 预览链路下的受影响路径，并指出命名为 <code>.png</code> / <code>.jpg</code> 的文件仍可能经图片转换进到 Ghostscript。NVD 已收录（published 2026-11-10，<code>vulnStatus: Awaiting Analysis</code>）；<strong>Ghostscript 官方安全公告本轮未核到</strong>，修复版本以发行版与上游公告为准</td>
<td style="padding:7px 6px;"><a href="https://pwn.ai/upload2shell">pwn.ai/upload2shell</a> ｜ 核实于 2026-11-22 06:38</td>
</tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:7px 6px;">C++26 技术内容"再次"完成（11 月 ISO 会议出差报告）</td>
<td style="padding:7px 6px;">3 月已完成的技术内容被重新打开后再次完成；六天会议主要用于处理第二批国际评审意见，焦点是 contracts 语言特性；下一步是把更新后的文本重新提交第二轮批准投票</td>
<td style="padding:7px 6px;"><a href="https://herbsutter.com/2026-11-21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/">herbsutter.com</a> ｜ 核实于 2026-11-22 06:37</td>
</tr>
<tr>
<td style="padding:7px 6px;">gopgext：用 Go 写 PostgreSQL 扩展</td>
<td style="padding:7px 6px;">实验性框架，扩展点覆盖 FDW、索引方法（gin / gist / spgist / brin）、聚合、选择率钩子、触发器、共享内存、subscript、tablesample，带文档与示例；生产使用前先读它的 Limitations</td>
<td style="padding:7px 6px;"><a href="https://jespino.github.io/gopgext/">jespino.github.io/gopgext</a> ｜ 核实于 2026-11-22 06:37</td>
</tr>
</tbody>
</table>

<p><strong>两条安全披露为什么没有升成紧急</strong>：2026-11-22 06:39 在本机实测 <code>gpg</code>、<code>gpgconf</code>、<code>gs</code>、<code>convert</code>、<code>magick</code> 五个命令<strong>全部未安装</strong>，"影响在用服务"这个成立条件不存在。换一台装了 GPGME 或 Ghostscript 的机器（尤其是跑图片转换与预览链路的服务器），这两条就应排在最前面。<strong>本雷达不代为升级、不代为执行任何操作。</strong></p>

<p><strong>补做午夜档自己留的缺口（Steam 逐款二次核对）</strong>：午夜档在「取数与异常」一节写明那一轮只回读了一次 <code>featuredcategories</code>、没有逐款 <code>appdetails</code> 复核。本轮对两款《极限竞速：地平线》补齐——<a href="https://store.steampowered.com/app/1551360/?l=schinese">《极限竞速：地平线 5》</a> 国区 <span style="color:#1a7f37;">¥198.00 → ¥79.20（-60%）</span>、<a href="https://store.steampowered.com/app/2483190/?l=schinese">《极限竞速：地平线 6》</a> 国区 <span style="color:#1a7f37;">¥298.00 → ¥223.50（-25%）</span>，两者 <code>discount_expiration=1796320800</code> 即 <strong>2026-12-03 18:00（北京时间）</strong>收。核实于 2026-11-22 06:36。<em>顺带记一处通道现象：不带 <code>cc=cn</code> 时官方接口按出口 IP 返回日元价（本轮代理出口在日本），本篇与午夜档的人民币价都以 <code>cc=cn</code> 为准。</em></p>

<p><strong>Epic 截止时间复核（与午夜档一致，不改）</strong>：06:38 回读官方 <code>freeGamesPromotions</code>，《深渊之印 / Mark of the Deep》<code>endDate=2026-11-26T16:00:00Z</code> ⇒ 北京时间 <strong>11-27 00:00</strong> 收，原价 ¥55.00、现价 0 元。同 id 此前已报道，本轮不重推，只留复查提示。</p>

<p><strong>App Store iOS 限免（06:32 取数 + 逐条回 iTunes 按 id 核价）</strong>：6 条播报里没有一条能进「值得」——<a href="https://apps.apple.com/cn/app/castkeeper-for-podcasts/id6760909808">CastKeeper</a>、<a href="https://apps.apple.com/cn/app/id6824264781">阿默</a>、<a href="https://apps.apple.com/cn/app/id6502558762">提醒清单</a>三条核到国区下载价为 0，但都是<strong>内购限免</strong>（内购解锁价不体现在下载价上，只算转述），且核到 0 只能写"下载不花钱"、分不出本就免费与促销中；LifeCue（id 6801134535）与 Inventarioteca（id 6820461445）<strong>按 id 查不到上架记录 ⇒ 价格未核实</strong>；「浮现」是<strong>兑换码型</strong>，按边界不转载兑换码，只留<a href="https://t.me/TossTF/4002">频道原帖</a>由你自取。<strong>Apple 不公布限免截止时间</strong>，这几条都不补日期。</p>

<p><strong>交易所与链上一手复查</strong>：Kraken 状态页 06:35 读 <code>status.json</code> / <code>components.json</code> / <code>incidents/unresolved.json</code>——仍为 <code>minor</code> / Partially Degraded Service（页面更新 11-21 21:54 UTC ≈ 北京 11-22 05:54），非运营组件 8 个：User Interface、Kraken Derivatives、Digital Currency Funding，以及 Cyber (CYBER)-Optimism、MemeCore-M BNB Chain、Osmosis、Stablr EURR、Stablr USDR；未解决事件 "Cyber (CYBER) Funding Delays"（11-21 19:59 UTC 起，identified，impact minor）原文为 "Deposits may be delayed…All other funding methods are operating normally"。Coinbase 同期 <code>none</code> / All Systems Operational。<a href="https://status.kraken.com">状态页</a> ｜ 降级项里没有充提暂停，且没有在用 Kraken 的证据 ⇒ 维持观察。</p>

<p><strong>Chainflip 被盗的一手核对（本轮最实质的一次降级判断）</strong>：中英文媒体 11-21 均报"金库被抽走约 $4.86M、FLIP 跌 30~34%、协议进入全面安全模式并暂停所有操作"（<a href="https://www.theblock.co/news/defi/2026-11-21-chainflips-flip-drops-34-after-attacker-drains-4-86-million-from-vault-with-suspected-key-compromise-444804">The Block</a> ／ <a href="https://www.coindesk.com/business/2026-11-21/cross-chain-protocol-chainflip-s-flip-tanks-30-after-suspected-usd4-86-million-vault-drain">CoinDesk</a> ／ <a href="https://www.panewslab.com/zh/articles/01a1fed7-9ee1-7480-b8d3-c5b72dff8a12">PANews</a>）。06:37 回到项目方一手页 <code>chainflip.io/blog</code>：<strong>最新公告只到 11-18（Coinbase cbBTC 上线），没有任何 11-21 事件的说明</strong>；GitHub org advisory 接口返回 404，X 没有机器可读通道。按"安全事件只认项目方 advisory / 官方博客 / 交易所公告三方"的口径，这条<strong>维持观察、不升紧急</strong>；若你在用 FLIP 或该协议，只按官方公告撤销授权，不自行发挥。同类的还有 Upbit / Bithumb 冻结转账一说（仅 The Block 单家转述，未见两所一手公告）。</p>

<p><strong>新增「观察」条目与不升级的理由</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;width:34%;"><a href="https://lowendbox.com/blog/a-little-more-room-before-black-friday-100-giveaway-4gb-ryzen-i9-vps/">ServerHost 4GB Ryzen/i9 VPS</a></td><td style="padding:7px 6px;">$55 USD/年（年付），优惠码 <code>OCTRYZI94GB</code>，06:35 读到原文数字</td><td style="padding:7px 6px;"><strong>帖内未给该套餐的截止时间</strong>，按发布门槛"优惠必须有截止时间"不能进值得；厂商为 LowEndBox 广告主，未独立核服务商官网</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">同帖 $100 店铺余额抽奖</td><td style="padding:7px 6px;">最后参与日 <strong>11-25（周三）</strong>，方式是在 LowEndTalk 回帖</td><td style="padding:7px 6px;">抽奖型收益不确定 + 需要论坛账号 ⇒ 门槛高</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">v2ex 黑五两条（Enconvo"7 折 + 送 10 个终身版"、哈基米"到 26 号半价"）</td><td style="padding:7px 6px;">论坛内厂商自我推广帖与用户转述</td><td style="padding:7px 6px;">无官方定价页核实 ⇒ 软文与转述，未核实</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;"><a href="https://www.idcspy.com/170746.html">RakSmart VPS 升降级操作步骤</a></td><td style="padding:7px 6px;">美国主机侦探的使用教程</td><td style="padding:7px 6px;">不是优惠：帖内无价格与截止时间</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">链上大额转移（PANews 三条）</td><td style="padding:7px 6px;">称 Tether 向未知钱包转约 1.43 亿 USDT、向 Bitfinex 转入 1.25 亿 USDT；Kraken 转出 1214 枚 BTC</td><td style="padding:7px 6px;">无一手链上标签说明 ⇒ 不作任何方向判断</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 6px;">Kalshi 纽约周一听证</td><td style="padding:7px 6px;"><a href="https://www.theblock.co/news/regulation/2026-11-21-kalshi-faces-monday-hearing-on-new-york-order-it-says-would-shut-down-its-exchange-nationwide-444813">The Block</a> / <a href="https://www.coindesk.com/policy/2026-11-20/kalshi-races-to-get-ahead-of-new-york-order-that-could-shut-down-exchange">CoinDesk</a> 两条</td><td style="padding:7px 6px;">未取到纽约监管原文 ⇒ 未核实</td></tr>
<tr><td style="padding:7px 6px;">"比特币节点可被重复同一个 ID 五万次拖慢"（<a href="https://www.coindesk.com/markets/2026-11-21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug">CoinDesk</a>）</td><td style="padding:7px 6px;">与 GPGME 公告里"超长 ID 触发缺陷"属同类报道</td><td style="padding:7px 6px;">未核到比特币核心官方安全说明（<code>bitcoincore.org/en/security/</code> 直取 404、<code>bitcoin/bitcoin</code> 的 GH advisory 接口 404）⇒ 未核实</td></tr>
</tbody>
</table>

<p><strong>被过滤、未写进任何段落的一条</strong>：PANews 的"币安 Alpha 上线 STBL，开放 1675 枚空投领取"——要求连接钱包才能领取的形态按边界属 ❌ 过滤，不转载、不评价。本轮币圈共 50 条（新闻 26 / 行情 23 / 交易所状态 1），行情、涨跌幅、热搜与情绪指数一律落在观察：它们是数字不是信息，<strong>不构成任何操作建议，也不预测价格</strong>；产物里不出现钱包地址、私钥、助记词与带推广参数的邀请链接。</p>

<p><strong>早间这轮 25 源健康度</strong>：hackernews 17、ithome 25、lobsters 11、v2ex 10、producthunt 14、panews 15、coindesk 7、theblock 4、coingecko 趋势 10、coingecko 市值异动 6、cmc 热搜 6、fng 1、appstore-ios 6、lowendbox 1、idcspy 1、steam 2、exchange-status 1；epic / appinn / binance / 阮一峰 / GitHub Trending / 项目方一手等抓到但被 <code>--days 2</code> 或 <code>history.jsonl</code> 去重为 0 新条，<code>SUMMARY</code> 未出现任何 <code>ERR source=</code>。<strong>合计 0 异常，代理节点无故障形态。</strong></p>

<p style="font-size:12px;color:#8a9099;">早间复核补充的兑现边界同上：只收集、核实、报告，不注册、不绑卡、不代领券、不下单，币圈不连钱包、不签名、不代为充提。本地存档 <code>~/aigc/info-radar/daily/2026-11-22.md</code>（六段结构，含早间这轮的完整分级）。</p>

## 免责声明

本文只做信息聚合与交叉核对，不构成投资、购买或法律建议。所有价格、折扣与截止时间均来自 2026-11-22 00:03–00:06 的接口返回，价格随时可能变动，领取与下单前请以官方页面为准。数学手稿部分请注意“预印本 / 未经同行评审”的前提。
