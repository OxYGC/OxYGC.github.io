---
title: "资讯雷达 2026-11-27｜Epic《Bread and Fred》0 元、TerraScape 折扣与黑五 VPS/域名观察"
author: OxYGC
date: 2026-11-27 00:10:00 +0800
last_modified_at: 2026-11-27 00:16:00 +0800
permalink: /posts/info-radar-2026-11-27/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, 黑五, VPS, 比特币, GitHub趋势]
description: "2026-11-27 凌晨首稿（00:05–00:16）：25 源取回 143 条、12 源成功、12 源报错、appinn 空结果。Epic《Bread and Fred》0 元至 12-04 00:00，《TerraScape》-30% 至 12-22 00:00，均已回官方接口核价。黑五 VPS/域名线索集中在 idcspy 与 LowEndBox，未回官方活动页的降为观察。币圈：The Block 与 PANews 正常，BTC 00:16 Gate.io 快照 60,614 USDT（+3.69%，24h 低 58,100.4），恐惧贪婪 11（Extreme Fear）；Okto 钱包 12-22 停运仅见 PANews 转述。v2ex、hf、appstore、steam、binance、exstatus、coingecko、cgmarkets、cmc、ethblog、creleases、coindesk 均报 URLError。"
---

这一轮取数在 2026-11-27 00:05–00:16（北京时间）完成：25 个来源里 12 个取到数据、12 个报错、1 个空结果，成功来源合计 **143 条**。失败仍集中在需要境外 HTTPS 的接口——`v2ex`、`hf`、`appstore`、`steam`、`binance`、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`creleases`、`coindesk` 全部报 `URLError`；同一时刻用 curl 走沙箱代理能取到部分站点，因此判为执行环境通道问题，不判断这些站本身下线。`panews` 本轮恢复正常（15 条），行情改用 Gate.io 公开 ticker 补位，单列标注、不计入 25 源。

先给能直接用的结论：**Epic 本周免费是《Bread and Fred》（原价 ¥47.00），0 元领取永久入库，12-04 00:00 收；同接口还有《TerraScape》-30%（¥53.00 → ¥37.10），12-22 00:00 收。** 这两条都回官方 `freeGamesPromotions` 接口核过价与 `endDate`，不是转述。黑五 VPS/域名线索今天很多，但绝大多数只到「美国主机侦探」的媒体转述，没回厂商活动页，按口径全部放进观察段。币圈一侧，BTC 在 00:16 的 Gate.io 快照为 **60,614 USDT（+3.69%，24h 区间 58,100.4–61,633.8）**，ETH 1,689.28（+2.49%），恐惧贪婪仍是 **11（Extreme Fear）**；The Block 的主线是现货 BTC ETF 可能创下最差月度、Galaxy 收回「6 月见底」判断，PANews 则记录 Okto 钱包 12-22 停运。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮会过期、或需要你自己动手的条目</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-04 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《Bread and Fred》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#6b7280;font-weight:700;">12-22 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《TerraScape》-30%（折扣，非限免）</td>
<td style="padding:9px 8px 9px 0;">¥53.00 → ¥37.10</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-27 00:15 官方接口实测：Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code>。`endDate` 为 UTC，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（2）

<details open>
<summary><strong>Epic《Bread and Fred》0 元领取永久入库，原价 ¥47.00</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥47.00 → 0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 12-04 00:00</span></summary>
<p>Epic 官方促销接口在 2026-11-27 00:15 返回：<code>title=Bread and Fred</code>、<code>originalPrice=4700</code>（分）、<code>discountPrice=0</code>、<code>endDate=2026-12-03T16:00:00Z</code>，即 **北京时间 12-04 00:00 截止**。这是「免费领取永久入库」，不是限时试玩。领取入口只有官方商店页，登录、下单、领取都由你本人完成；本站不代领、不绑卡。</p>
<p><strong>怎么读</strong>：如果你上周领过《深渊之印》，这次是同档位的接档免费游戏；Epic 每周四 00:00（北京时间）换榜，错过就不能补领。领取前确认账号区域与商店币种，避免把打折页当成 0 元页。</p>
<p><a href="https://store.epicgames.com/free-games?lang=zh-CN">官方领取页</a> · 核实于 2026-11-27 00:15（Epic 官方接口）</p>
</details>

<details open>
<summary><strong>Epic《TerraScape》-30%，¥53.00 → ¥37.10</strong> ｜ <span style="color:#1a7f37;font-weight:700;">-30%</span> ｜ <span style="color:#6b7280;font-weight:700;">截止 12-22 00:00</span></summary>
<p>同一接口在 00:15 返回：<code>originalPrice=5300</code>、<code>discountPrice=3710</code>、<code>endDate=2026-12-21T16:00:00Z</code>，即 **北京时间 12-22 00:00 截止**。这是折扣而不是限免，<code>discountPrice</code> 不为 0，请别把它写进「免费领取」。</p>
<p><strong>怎么读</strong>：适合已经在愿望单里的玩家；折扣幅度 30%，不是历史最低的保证。买之前回商店页看当前价与是否包含 DLC，别只看标题。</p>
<p><a href="https://store.epicgames.com/free-games?lang=zh-CN">官方商店页</a> · 核实于 2026-11-27 00:15（Epic 官方接口）</p>
</details>

## 观察（7）· 资讯与币圈那一轮、方法与来源健康度

<details>
<summary><strong>优惠与羊毛观察（7 条，均未回厂商官方活动页）</strong></summary>
<table style="width:100%;border-collapse:collapse;font-size:13.5px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:26%;">条目</th><th style="padding:7px 8px 7px 0;">价格 / 额度</th><th style="padding:7px 0;width:34%;">存疑原因</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170993.html">Spaceship 黑五</a></td><td style="padding:8px 8px 8px 0;">.com $3.60/年、.net $4.78/年、.xyz $0.75/年；EasyWP Turbo 与 Shared Essential 免费试用 30 天</td><td style="padding:8px 0;">媒体转述，未回 Spaceship 官方活动页核价；未写截止时间。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170965.html">ColoCrossing 黑五</a></td><td style="padding:8px 8px 8px 0;">美国 VPS 年付 $17.99 起；美国服务器 $20/月起</td><td style="padding:8px 0;">未核续费是否同价，未核截止时间。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/171001.html">SurferCloud 黑五</a></td><td style="padding:8px 8px 8px 0;">UHost 云服务器最高 4 折；ULightHost 轻量云最高 7 折</td><td style="padding:8px 0;">「最高折扣」未折算到具体机型最终价。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170983.html">SocialEcho 黑五</a></td><td style="padding:8px 8px 8px 0;">充 $99 送 $10、充 $399 送 $88，最高赠送 $1688</td><td style="padding:8px 0;">需先充值，收益随档位变化；未核活动截止。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/170959.html">宝塔面板免费一年 DV 证书</a></td><td style="padding:8px 8px 8px 0;">免费 1 年 DV</td><td style="padding:8px 0;">教程类线索；未核证书品牌、域名数量与续费限制。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://lowendbox.com/blog/sneak-peak-serverhosts-black-friday-vanishing-vps-offers-rise-1-a-day-starting-november-28/">ServerHost 黑五 VPS</a></td><td style="padding:8px 8px 8px 0;">11-28 起每日涨 $1 的阶梯价</td><td style="padding:8px 0;">只有玩法说明，没有具体配置与到手价。</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://www.panewslab.com/zh/articles/01a2187f-0ff8-723f-9c12-779d0b7c687e">Okto 钱包 12-22 停运</a></td><td style="padding:8px 8px 8px 0;">代币发行计划取消</td><td style="padding:8px 0;">仅 PANews 转述，未回 Okto 官方公告；若在用请自行核对并提前处理资产，别点「代提/追回」链接。</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">这一段的共同点是「有价格、但没在一手官方页核到」：按门槛只能放观察，不进「值得」。价格与名额随时变，动手前请以厂商活动页为准。</p>
</details>

<details>
<summary><strong>资讯面：HN、Lobsters、IT之家、阮一峰、Product Hunt 与 GitHub Trending</strong></summary>
<p><strong>HN 首页（00:14 读数，Algolia <code>front_page</code>）</strong>：<a href="https://scottaaronson.blog/?p=10379">Scott Aaronson《Holy shit…: The magnitude of what’s now happening》</a> **1,806 分 / 1,646 评论**居首，属个人博客观点；<a href="https://1password.com/blog/update-on-nov-2026-security-incident">1Password 安全事件官方公告</a> **1,573 分 / 673 评论**第二；<a href="https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features">NYT 提醒摄影师别急着更新 Photoshop</a> 517 分 / 437 评论；<a href="https://github.com/lsernau/grh-lean">Anthropic 的 GRH Lean 验证短版本</a> 506 分 / 318 评论；<a href="https://twitter.com/thsottiaux/status/2125784147889393806">OpenAI 削减 GPT-6.2 用量：Astra 上限快 40%、Sol 快 25%</a> 402 分 / 223 评论；<a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">Ubuntu 安全响应偏慢</a> 364 分 / 209 评论。</p>
<p><strong>Lobsters（按分数）</strong>：<a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">Slow Ubuntu security response times</a> 87 赞；<a href="https://www.marginalia.nu/log/a_141_marginalia_update/">Marginalia Search 的更新</a> 110 赞；<a href="https://servo.org/blog/2026/11/25/october-in-servo/">Servo 十月进展</a> 59 赞；<a href="https://donsz.nl/blog/optimizing-rustcs-next-trait-solver">优化 rustc 的下一代 trait solver</a> 57 赞；<a href="https://scottaaronson.blog/?p=10379">Scott Aaronson 谈近期 AI 复杂度理论成果</a> 48 赞；<a href="https://1password.com/blog/update-on-nov-2026-security-incident">1Password 后端安全事件</a> 44 赞；<a href="https://jmmv.dev/2026/11/entering-the-geminispace.html">Entering the Geminispace</a> 28 赞。</p>
<p><strong>IT之家（最新条目到 11-26 23:24 北京时间）</strong>：值得记的有<a href="https://www.ithome.com/1/033/131.htm">瑞士发生五起 AI 智能体网络攻击，电力供水通信系统遭入侵</a>、<a href="https://www.ithome.com/1/033/130.htm">华为 HarmonyOS 五大技术品牌公开</a>、<a href="https://www.ithome.com/1/033/125.htm">腾讯用 AI 挑战药物研发，成果登 Nature</a>、<a href="https://www.ithome.com/1/033/121.htm">拓竹发布 S1 手持 3D 扫描仪，首发 11499 元起</a>、<a href="https://www.ithome.com/1/033/120.htm">ANBERNIC 公布 RG 47G1 竖版掌机</a>、<a href="https://www.ithome.com/1/033/117.htm">国际足联报告遭遇黑客入侵</a>、<a href="https://www.ithome.com/1/033/101.htm">我国首例无线侵入式汉语脑机接口临床试验成功</a>、<a href="https://www.ithome.com/1/033/098.htm">微信 iOS 8.0.80 上线 NFC 交通卡</a>。以上均为媒体转述，未逐条回官方公告，不进「值得」。</p>
<p><strong>阮一峰周刊</strong>：最新一期是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>，feed 更新时间 2026-11-26 16:56 北京时间；上一期是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-419.html">第 419 期《机房来了，写字楼走了》</a>。周更节奏，本轮只有 2 条。</p>
<p><strong>Product Hunt</strong>：本轮 15 条，可读的有 <a href="https://www.producthunt.com/products/vybe-4">Falcon by Vybe</a>、<a href="https://www.producthunt.com/products/canva">Canva MCP</a>、<a href="https://www.producthunt.com/products/3way-social">3way.Social MCP</a>、<a href="https://www.producthunt.com/products/eluna">eluna</a>、<a href="https://www.producthunt.com/products/blink-35">Blink</a>、<a href="https://www.producthunt.com/products/airbots">Airbot</a>、<a href="https://www.producthunt.com/products/koed">Koed</a>、<a href="https://www.producthunt.com/products/coderabbit">CodeRabbit Verify</a>、<a href="https://www.producthunt.com/products/magi-1">MAGI-2</a>。只作产品发现，不评优劣.</p>
<p><strong>GitHub Trending（00:14 抓取 16 条）</strong>：star 为页面读数，不是官方增量接口。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:42%;">仓库</th><th style="padding:7px 8px 7px 0;width:18%;">总 star</th><th style="padding:7px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">obra/superpowers</td><td style="padding:7px 8px 7px 0;">327,199</td><td style="padding:7px 0;">Agentic skills 框架</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">firecrawl/firecrawl</td><td style="padding:7px 8px 7px 0;">210,671</td><td style="padding:7px 0;">Agent 抓取 / 搜索基础设施</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">toeverything/AFFiNE</td><td style="padding:7px 8px 7px 0;">78,821</td><td style="padding:7px 0;">知识库与协作</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">mvanhorn/last30days-skill</td><td style="padding:7px 8px 7px 0;">75,563</td><td style="padding:7px 0;">跨 Reddit / X / YouTube 的研究技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">cathrynlavery/diagram-design</td><td style="padding:7px 8px 7px 0;">73,639</td><td style="padding:7px 0;">图表 / 版式设计资源</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">jingyaogong/minimind</td><td style="padding:7px 8px 7px 0;">71,510</td><td style="padding:7px 0;">两小时从 0 训 64M 小模型</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">HKUDS/CLI-Anything</td><td style="padding:7px 8px 7px 0;">66,169</td><td style="padding:7px 0;">把软件做成 Agent 可调用的 CLI</td></tr>
<tr><td style="padding:7px 8px 7px 0;">elementalsouls/Claude-BugHunter</td><td style="padding:7px 8px 7px 0;">24,093</td><td style="padding:7px 0;">Claude Code 漏洞狩猎技能包</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">其余进榜：cursor/plugins（19,711）、XiaoYouChR/Ghost-Downloader-3（18,919）、zhouxiaoka/autoclip（16,755）、Tracer-Cloud/opensre（15,713）、google-labs-code/stitch-skills（13,193）、openvinotoolkit/openvino（12,765）、nginx/nginx（33,475）、mjmirza/app-store-compliance（6,869）。Agent Skills 仍占前排，下载 / 剪辑 / 安全工具同榜。</p>
</details>

<details>
<summary><strong>币圈与安全：ETF 最差月度、Galaxy 收回底部判断、Okto 停运与算力劫持</strong></summary>
<p><strong>行情快照</strong>：2026-11-27 00:16（北京时间）Gate.io 公开 ticker，BTC/USDT 最新 <strong>60,614</strong>，24h 涨幅 <strong>+3.69%</strong>，24h 区间 <strong>58,100.4–61,633.8</strong>；ETH/USDT 最新 <strong>1,689.28</strong>，24h 涨幅 <strong>+2.49%</strong>，24h 区间 1,630.06–1,729.9。恐惧贪婪指数 <strong>11（Extreme Fear）</strong>。以上是时刻快照，只描述状态，不构成任何操作建议。</p>
<p><strong>市场与资金（The Block）</strong>：<a href="https://www.theblock.co/news/markets/2026-11-26-spot-bitcoin-etfs-worst-month-november-446814">现货 BTC ETF 可能创下史上最差月度</a>；<a href="https://www.theblock.co/news/markets/2026-11-26-galaxy-walks-back-bitcoin-bottom-call-446786">Galaxy 收回「6 月见底」判断，警告跌破 $58,525 后可能更深</a>；<a href="https://www.theblock.co/news/markets/2026-11-26-swiss-bitcoin-etf-bbit-begins-trading-europes-only-446724">欧洲唯一现货 BTC ETF 在瑞士开始交易</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-house-committee-advances-strategic-bitcoin-reserve-bill-446778">美国众议院委员会推进「战略比特币储备」法案</a>；<a href="https://www.theblock.co/news/business/2026-11-25-fidelity-chainlink-etf-nasdaq-listing-446735">Fidelity 申请现货 Chainlink ETF</a>；<a href="https://www.theblock.co/news/business/2026-11-25-layerzero-kakaopay-samsung-446770">LayerZero 把 Samsung Card、Kakao Pay、ZAN 纳入验证人</a>。</p>
<p><strong>监管与安全（The Block）</strong>：<a href="https://www.theblock.co/news/regulation/2026-11-26-switzerland-approves-57-jurisdictions-for-crypto-data-exchange-from-2028-446821">瑞士批准 57 个司法辖区从 2028 年起交换加密数据</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-warren-van-hollen-lead-push-scrap-sec-regulation-crypto-innovation-exemption-446756">Warren 与 Van Hollen 推动取消 SEC 的 crypto 创新豁免</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-justice-department-takes-aim-billions-crypto-fraud-proceeds-largest-ever-crackdown-446711">司法部针对数十亿美元加密欺诈所得展开「史上最大规模」执法</a>；<a href="https://www.theblock.co/news/ecosystems/2026-11-25-bitcoin-miners-hit-hashrate-hijacking-attack-exploiting-unencrypted-connections-446723">比特币矿工遭「算力劫持」攻击，利用未加密连接</a>。矿机管理面与凭据相关操作，请按厂商公告与自有资产自查，本站不代为扫描或执行命令。</p>
<p><strong>中文媒体（PANews）</strong>：<a href="https://www.panewslab.com/zh/articles/01a2187f-0ff8-723f-9c12-779d0b7c687e">加密钱包 Okto 将于 12-22 停运，代币发行计划取消</a>（仅有转述，未见官方公告原文，按观察处理）；<a href="https://www.panewslab.com/zh/articles/01a2187a-5616-7749-9630-ca6e73d115c3">过去 24 小时全网合约爆仓 3.68 亿美元，主爆空单</a>；<a href="https://www.panewslab.com/zh/articles/01a21861-75f4-75e2-86f8-c055ca39e8f9">CryptoQuant：以太坊与 Tron 上 USDT 供应量较 5 月高点减少 129 亿美元</a>；<a href="https://www.panewslab.com/zh/articles/01a2182c-3de0-76fa-97a2-8929f9158b62">Glassnode：机构资金集体撤退，市场进入防守周期</a>；<a href="https://www.panewslab.com/zh/articles/01a21840-812c-72cb-8d8e-73aeaa034336">西班牙赋予反洗钱机构无需法官批准即可冻结加密账户的权力</a>；<a href="https://www.panewslab.com/zh/articles/01a21807-724d-749c-b3cf-173a4c328896">某地址两天累计接收约 7,186 枚 BTC，价值约 4.35 亿美元</a>。</p>
<p><strong>口径</strong>：行情、涨跌幅、热搜、情绪指数一律只作状态描述；只有直接影响在用资产可得性的公告才可能升级。安全事件只认项目方 advisory / 官方博客 / 交易所公告；媒体转述单独出现时降为观察。不连钱包、不签名、不导私钥、不代充提，不写买卖建议与目标价。</p>
</details>

<details>
<summary><strong>取数与来源健康度：25 源，143 条，12 源报错、1 源空结果</strong></summary>
<p>本轮按 <code>info-task-gc</code> 的 25 源口径执行，成功 12 源、报错 12 源、空结果 1 源，合计 <strong>fetched=143 / sources=25 / errors=12</strong>。取数窗口 2026-11-27 00:05–00:16（北京时间）。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:16%;">来源</th><th style="padding:7px 8px 7px 0;width:12%;">条数</th><th style="padding:7px 8px 7px 0;width:14%;">状态</th><th style="padding:7px 0;">备注</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">epic</td><td style="padding:6px 8px 6px 0;">2</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">1 限免 + 1 折扣</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">hn</td><td style="padding:6px 8px 6px 0;">23</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">Algolia front_page</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">lobsters</td><td style="padding:6px 8px 6px 0;">20</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">hottest</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">github-trending</td><td style="padding:6px 8px 6px 0;">16</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">HTML 抓取</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">lowendbox</td><td style="padding:6px 8px 6px 0;">2</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">idcspy</td><td style="padding:6px 8px 6px 0;">10</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS，含多条黑五转述</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">ruanyifeng</td><td style="padding:6px 8px 6px 0;">2</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">Atom，第 419/420 期</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">ithome</td><td style="padding:6px 8px 6px 0;">25</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">producthunt</td><td style="padding:6px 8px 6px 0;">15</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">fng</td><td style="padding:6px 8px 6px 0;">1</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">恐惧贪婪 11（Extreme Fear）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">theblock</td><td style="padding:6px 8px 6px 0;">12</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">panews</td><td style="padding:6px 8px 6px 0;">15</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS，本轮恢复正常</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">v2ex</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR</td><td style="padding:6px 0;">URLError，403 类</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">hf</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR</td><td style="padding:6px 0;">URLError，403 类</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">appstore</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR</td><td style="padding:6px 0;">URLError，Telegram 预览页未通</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">steam</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR</td><td style="padding:6px 0;">URLError，商店 API 未通</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">binance / exstatus / coingecko / cgmarkets / cmc / ethblog / creleases / coindesk</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR ×8</td><td style="padding:6px 0;">均为 URLError</td></tr>
<tr><td style="padding:6px 8px 6px 0;">appinn</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#6b7280;">INFO empty</td><td style="padding:6px 0;">本轮无符合条件的限免帖（非故障）</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">12 个失败全部是境外 HTTPS 接口在本轮 Python 通道里的 <code>URLError</code>，没有 4xx / 410 类源站下线信号；同一时刻 curl 走沙箱代理可访问部分站点，因此判为执行环境通道问题。行情用 Gate.io 公开 ticker 补位（单列，不计入 25 源）。</p>
</details>

<details>
<summary><strong>方法与边界</strong></summary>
<p><strong>四步口径</strong>：取数（25 源，NDJSON 归一化）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。</p>
<p><strong>边界</strong>：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。</p>
<p><strong>执行说明</strong>：本轮按 <code>info-task-gc</code> 的 SKILL 与三份 references 执行，取数脚本为仓库内 <code>scripts/radar_fetch.py</code>；因沙箱内 Python 对部分境外站点的 TLS 握手会挂住，本轮把单通道超时收紧到 7 秒，失败源按 ERR 原样记录，未用记忆或别的站数据冒充。今天是 2026-11-27 当天第一份；同日复跑只更新本文件，不新增第二份。</p>
<p style="margin:24px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-27 00:05–00:16 接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，且本轮仅有 Gate.io 单源，不构成任何投资建议；新闻部分请注意「媒体转述」与「公司公告 / 官方接口」的区别。</p>
</details>
</content>
