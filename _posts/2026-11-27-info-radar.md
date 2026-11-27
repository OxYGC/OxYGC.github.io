---
title: "资讯雷达 2026-11-27（午间复跑）｜Epic 两款 0 元、Steam 黑五 3A 折扣、NFS 9.8 漏洞待核"
author: OxYGC
date: 2026-11-27 00:10:00 +0800
last_modified_at: 2026-11-27 12:09:00 +0800
permalink: /posts/info-radar-2026-11-27/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam折扣, 黑五, NFS, 比特币, GitHub趋势]
description: "2026-11-27 当天第二跑（午间 12:00 前后）：25 源成功 14、报错/异常 11，取回 402 条。Epic《Bread and Fred》0 元（原 ¥47.00）至 12-04 00:00，同接口另有一款原价即 0 的《火之石》，《TerraScape》-30% 至 12-22 00:00，均回官方接口核价。Steam 黑五 3A 折扣经官方 featuredcategories 核对（RDR2 -75%、双人成行 -80%、底特律 -90%）。安全面：NFS2ROOT 9.8 仅见 appinn 转述、NVD 未检索到，1Password 官方博客承认后端被入侵。币圈 BTC 12:09 Gate.io 快照 61,420.8（+0.82%），恐惧贪婪 12（Extreme Fear）。"
---

这是 2026-11-27 当天第二跑（午间 12:00 前后，北京时间）。按「一天一份」规则，本次不新增第二篇，只更新本文件：凌晨首稿的结论在本轮逐条复核，新增 Steam 黑五与 NFS 漏洞两条主线。本轮 25 个来源里 **14 个取到数据、11 个报错或异常**，取回 **402 条**（其中 appstore 109 条为新上架免费榜，仅作产品发现）。与凌晨相比，`appstore`、`steam`、`appinn` 本轮经 curl 走沙箱代理拿到；`panews` 的 RSS 入口返回的是网页而非 feed，本轮无可用条目，币圈改用 The Block 单源。

先给能直接用的结论：**Epic 本周免费仍是《Bread and Fred》（原价 ¥47.00），0 元领取永久入库，12-04 00:00 收；同接口还有《TerraScape》-30%（¥53.00 → ¥37.10），12-22 00:00 收。** 这两条都回官方 `freeGamesPromotions` 接口核过价与 `endDate`，不是转述。Steam 黑五正在进行，`specials` 接口给到《RDR2》-75%、《双人成行》-80%、《底特律：化身为人》-90% 等，但该接口不返回截止时间，收口一律以商店页为准。安全面两条要分开看：NFS2ROOT 9.8 目前只有小众软件（appinn）转述、NVD 关键词检索 0 条，属「未核实」；1Password 是官方博客自述，可信度更高但仍需按官方 RCA 跟进。币圈 BTC 在 12:09 的 Gate.io 快照为 **61,420.8 USDT（+0.82%，24h 区间 59,923.9–61,862.7）**，ETH 1,728.18（+1.56%），恐惧贪婪 **12（Extreme Fear）**。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮会过期、或需要你自己动手的条目</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-04 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《Bread and Fred》0 元领取永久入库（同接口另有原价 0 的《火之石》，非新增限免）</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;font-weight:700;">12-22 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《TerraScape》-30%（折扣，非限免）</td>
<td style="padding:9px 8px 9px 0;">¥53.00 → ¥37.10</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;font-weight:700;">商店页为准</td>
<td style="padding:9px 8px 9px 0;">Steam 黑五 3A：《RDR2》-75%、《双人成行》-80%、《赛博朋克 2077》-70%、《底特律》-90%</td>
<td style="padding:9px 8px 9px 0;">¥69.75 / ¥39.60 / ¥89.40 / ¥13.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/specials">store.steampowered.com</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">未定（自查）</td>
<td style="padding:9px 8px 9px 0;">NFS2ROOT 9.8 漏洞（开 NFS 共享的 NAS 用户）</td>
<td style="padding:9px 8px 9px 0;">—</td>
<td style="padding:9px 0 9px 0;">见下方「安全观察」，以厂商 advisory 为准</td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格均为 2026-11-27 11:55–12:09 实测：Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code>，Steam <code>featuredcategories?cc=cn&amp;l=zh</code>（分位转元）。Epic `endDate` 为 UTC，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（3）

<details open>
<summary><strong>Epic《Bread and Fred》0 元领取永久入库，原价 ¥47.00</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥47.00 → 0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 12-04 00:00</span></summary>
<p>Epic 官方促销接口在 2026-11-27 12:00 前后再次返回：<code>title=Bread and Fred</code>、<code>originalPrice=4700</code>（分）、<code>discountPrice=0</code>、<code>endDate=2026-12-03T16:00:00Z</code>，即 **北京时间 12-04 00:00 截止**。这是「免费领取永久入库」，不是限时试玩。领取入口只有官方商店页，登录、下单、领取都由你本人完成；本站不代领、不绑卡。</p>
<p><strong>怎么读</strong>：Epic 每周四 00:00（北京时间）换榜，错过就不能补领。同一次接口返回里还有一条《火之石 – 放置点击英雄RPG》，但它的 <code>originalPrice=0</code>、<code>discountPrice=0</code>，属本来就免费或常年促销标记，<strong>不能当成「本周新增限免」</strong>，所以不单列。领取前确认账号区域与商店币种，避免把打折页当成 0 元页。</p>
<p><a href="https://store.epicgames.com/free-games?lang=zh-CN">官方领取页</a> · 核实于 2026-11-27 12:00（Epic 官方接口）</p>
</details>

<details open>
<summary><strong>Steam 黑五 3A 折扣：《RDR2》-75%、《双人成行》-80%、《底特律》-90%</strong> ｜ <span style="color:#1a7f37;font-weight:700;">官方 featuredcategories</span> ｜ <span style="color:#6b7280;font-weight:700;">截止以商店页为准</span></summary>
<p>Steam 官方 <code>featuredcategories?cc=cn&amp;l=zh</code> 在 12:00 前后的 <code>specials</code> 档返回（分位已换算成人民币）：<code>Red Dead Redemption 2</code> 折扣 75% → <strong>¥69.75</strong>；<code>Grand Theft Auto V 增强版</code> 56% → <strong>¥98.56</strong>；<code>双人成行</code> 80% → <strong>¥39.60</strong>；<code>赛博朋克 2077</code> 70% → <strong>¥89.40</strong>；<code>底特律：化身为人</code> 90% → <strong>¥13.60</strong>；<code>博德之门3</code> 30% → <strong>¥187.60</strong>；<code>双影奇境</code> 40% → <strong>¥118.80</strong>；<code>SILENT HILL 2 &amp; f 双包</code> 65% → <strong>¥156.80</strong>。</p>
<p><strong>怎么读</strong>：这是官方接口给到的当前价，但接口<strong>不返回截止时间</strong>，所以本条目只承诺「价格来自官方接口、时刻已标注」，不承诺具体收口时点，买前请回商店页看倒计时。折扣价不等于历史最低，若已在愿望单可等史低提醒；新手最容易踩的是「增强版 / 终极版 / 含 DLC」价差，下单前看清版本。</p>
<p><a href="https://store.steampowered.com/specials">Steam 特卖页</a> · 核实于 2026-11-27 12:00（Steam 官方接口）</p>
</details>

<details open>
<summary><strong>Epic《TerraScape》-30%，¥53.00 → ¥37.10</strong> ｜ <span style="color:#1a7f37;font-weight:700;">-30%</span> ｜ <span style="color:#6b7280;font-weight:700;">截止 12-22 00:00</span></summary>
<p>同一接口在 12:00 前后返回：<code>originalPrice=5300</code>、<code>discountPrice=3710</code>、<code>endDate=2026-12-21T16:00:00Z</code>，即 **北京时间 12-22 00:00 截止**。这是折扣而不是限免，<code>discountPrice</code> 不为 0，请别把它写进「免费领取」。</p>
<p><strong>怎么读</strong>：适合已经在愿望单里的玩家；折扣幅度 30%，不是历史最低的保证。买之前回商店页看当前价与是否包含 DLC，别只看标题。</p>
<p><a href="https://store.epicgames.com/free-games?lang=zh-CN">官方商店页</a> · 核实于 2026-11-27 12:00（Epic 官方接口）</p>
</details>

## 观察 · 安全、优惠、资讯与币圈

<details>
<summary><strong>安全观察：NFS2ROOT 9.8（未核实）与 1Password 官方事件</strong></summary>
<p><strong>NFS2ROOT（仅转述，未核实）</strong>：<a href="https://www.appinn.com/">小众软件（appinn）</a>本轮条目称 Linux NFS 曝出 9.8 分漏洞「NFS2ROOT」，提醒开了 NFS 共享的 NAS 用户注意。这条的硬伤是<strong>只有媒体转述</strong>：截至 2026-11-27 12:08，NVD <code>keywordSearch=NFS2ROOT</code> 返回 0 条，没取到 CVE 编号与厂商 advisory。按口径只能放观察。如果你的 NAS / 服务器开着 NFS 导出，建议主动做两件事：确认 NFS 服务是否暴露在不可信网段、关注发行版与 NAS 厂商的安全公告与补丁节奏——不要靠这条转述直接下结论。</p>
<p><strong>1Password 后端安全事件（官方博客）</strong>：<a href="https://1password.com/blog/update-on-nov-2026-security-incident">1Password 官方公告</a> 自述：攻击者访问了部分后端系统，复制了<strong>部分客户的账户信息（用于登录的姓名与邮箱）</strong>；官方强调<strong>客户密码库未被访问、仍然安全</strong>，并称将在调查完成后数周内发布根因分析（RCA）。这属于「公司公告」而非转述，但细节仍以官方后续 RCA 为准；若你收到以此事为由索要主密码、验证码或诱导点链接的邮件，一律当钓鱼处理。</p>
</details>

<details>
<summary><strong>优惠与羊毛观察（黑五 VPS / 域名，均未回厂商官方活动页）</strong></summary>
<table style="width:100%;border-collapse:collapse;font-size:13.5px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:26%;">条目</th><th style="padding:7px 8px 7px 0;">价格 / 额度</th><th style="padding:7px 0;width:34%;">存疑原因</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/">AdsPower 指纹浏览器黑五</a></td><td style="padding:8px 8px 8px 0;">540 天套餐低至 4 折，赠送最高 600 AI 积分</td><td style="padding:8px 0;">媒体转述，未回官方活动页核价与截止。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/">SurferCloud 黑五</a></td><td style="padding:8px 8px 8px 0;">UHost 云服务器最高 4 折；ULightHost 轻量云最高 7 折</td><td style="padding:8px 0;">「最高折扣」未折算到具体机型最终价。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/">Spaceship 黑五</a></td><td style="padding:8px 8px 8px 0;">.com 域名低至 $3.60/年，EasyWP 主机免费试用 30 天</td><td style="padding:8px 0;">未回 Spaceship 官方活动页核价；未写截止时间。</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://www.idcspy.com/">SocialEcho 黑五</a></td><td style="padding:8px 8px 8px 0;">充 $99 送 $10、充 $399 送 $88，最高赠送 $1688</td><td style="padding:8px 0;">需先充值，收益随档位变化；未核活动截止。</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://lowendbox.com/blog/sneak-peak-serverhosts-black-friday-vanishing-vps-offers-rise-1-a-day-starting-november-28/">ServerHost 黑五 VPS</a></td><td style="padding:8px 8px 8px 0;">11-28 起每日涨 $1 的阶梯价</td><td style="padding:8px 0;">只有玩法说明，没有具体配置与到手价。</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">这段共同点是「有价格、但没在一手官方页核到」：按门槛只能放观察。另：<strong>App Store 新上架免费榜本轮取到 109 条</strong>（PicMind、MirrorSync 等），iTunes JSON 给的是「新上架免费应用」，<strong>不是限免核定</strong>，因此只作产品发现，不列「值得」。</p>
</details>

<details>
<summary><strong>资讯面：HN、Lobsters、IT之家、阮一峰、Product Hunt 与 GitHub Trending</strong></summary>
<p><strong>HN 首页（12:00 前后，Algolia <code>front_page</code>）</strong>：<a href="https://scottaaronson.blog/?p=10379">Scott Aaronson《Holy shit…: The magnitude of what’s now happening》</a> **2,007 分**居首，属个人博客观点；<a href="https://news.ycombinator.com/item?id=50655664">Tell HN: Happy Thanksgiving</a> 644 分；<a href="https://github.com/intel/intel-one-mono">Intel One Mono 字体（2023）</a> 485 分；<a href="https://janlukas.blog/posts/ai-self-hosting">AI made self-hosting fun again</a> 416 分；<a href="https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/">Nextcloud Office 桌面版</a> 410 分；<a href="https://github.com/antonpictures/youtube-punisher">YouTube Ad Punisher</a> 304 分；<a href="https://devnull.land/amd-specific-llama-cpp">AMD 专用 llama.cpp 分支</a> 304 分。以上为社区热度，不代表事实成立。</p>
<p><strong>Lobsters（按分数）</strong>：<a href="https://www.marginalia.nu/log/a_141_marginalia_update/">Marginalia Search 更新</a> 114 赞；<a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">Slow Ubuntu security response times</a> 111 赞；<a href="https://donsz.nl/blog/optimizing-rustcs-next-trait-solver">优化 rustc 下一代 trait solver</a> 61 赞；<a href="https://scottaaronson.blog/?p=10379">Scott Aaronson 谈近期复杂度理论</a> 57 赞；<a href="https://leanprover.zulipchat.com/">GRH 证明在 Lean 4 中精简到 7.6 万行</a> 51 赞；<a href="https://1password.com/blog/update-on-nov-2026-security-incident">1Password 后端安全事件</a> 46 赞；<a href="https://jmmv.dev/2026/11/entering-the-geminispace.html">Entering the Geminispace</a> 41 赞。</p>
<p><strong>IT之家（最新条目到 11-27 11:54 北京时间）</strong>：<a href="https://www.ithome.com/">纳德拉承认微软放缓应届生招聘，AI 时代年轻人的第一份工作更难拿</a>；<a href="https://www.ithome.com/">腾讯混元发布 3D 生成大模型 Hy3D 3.6</a>；<a href="https://www.ithome.com/">微软承认 Win11 原生应用开发不足，WinUI 手写组件迟到约 4 年</a>；<a href="https://www.ithome.com/">广汽丰田汉兰达 9X 官宣，携手华为、宁德时代</a>；<a href="https://www.ithome.com/">领克 900L 预售：30.98 万–36.98 万元</a>；<a href="https://www.ithome.com/">Collabora Online 内存占用最高直降 55%</a>；<a href="https://www.ithome.com/">长三角三条高铁同日开通</a>。均为媒体转述，未逐条回官方公告，不进「值得」。</p>
<p><strong>阮一峰周刊</strong>：最新一期已更新到<a href="https://www.ruanyifeng.com/blog/2026/11/">第 421 期《AI 的疯狂造富》</a>（feed 更新 2026-11-27 11:17 北京时间），上一期是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>。周更节奏，本轮 3 条。</p>
<p><strong>Product Hunt</strong>：本轮 50 条，可读的有 ExtraOrbital、Meboki、NEXUS、Flurra、Claude-Mem Cloud Sync、Kagi Mail、Transept AI、Doodle。只作产品发现，不评优劣。</p>
<p><strong>GitHub Trending（12:00 前后抓取 16 条）</strong>：star 为页面读数，不是官方增量接口。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:42%;">仓库</th><th style="padding:7px 8px 7px 0;width:18%;">总 star</th><th style="padding:7px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">obra/superpowers</td><td style="padding:7px 8px 7px 0;">327,600</td><td style="padding:7px 0;">Agentic skills 框架</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">firecrawl/firecrawl</td><td style="padding:7px 8px 7px 0;">211,068</td><td style="padding:7px 0;">Agent 抓取 / 搜索基础设施</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">toeverything/AFFiNE</td><td style="padding:7px 8px 7px 0;">79,044</td><td style="padding:7px 0;">知识库与协作</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">mvanhorn/last30days-skill</td><td style="padding:7px 8px 7px 0;">75,875</td><td style="padding:7px 0;">跨 Reddit / X / YouTube 的研究技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">cathrynlavery/diagram-design</td><td style="padding:7px 8px 7px 0;">73,973</td><td style="padding:7px 0;">图表 / 版式设计资源</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">jingyaogong/minimind</td><td style="padding:7px 8px 7px 0;">71,789</td><td style="padding:7px 0;">两小时从 0 训 64M 小模型</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">HKUDS/CLI-Anything</td><td style="padding:7px 8px 7px 0;">66,481</td><td style="padding:7px 0;">把软件做成 Agent 可调用的 CLI</td></tr>
<tr><td style="padding:7px 8px 7px 0;">elementalsouls/Claude-BugHunter</td><td style="padding:7px 8px 7px 0;">24,820</td><td style="padding:7px 0;">Claude Code 漏洞狩猎技能包</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">其余进榜：cursor/plugins（19,823）、XiaoYouChR/Ghost-Downloader-3（19,283）、zhouxiaoka/autoclip（17,081）、Tracer-Cloud/opensre（15,872）、google-labs-code/stitch-skills（13,338）、openvinotoolkit/openvino（12,841）、nginx/nginx（33,544）、mjmirza/app-store-compliance（7,101）。Agent Skills 仍占前排，下载 / 剪辑 / 安全工具同榜。</p>
</details>

<details>
<summary><strong>币圈：JPMorgan「投降」判断、ETF 最差月度与情绪极度恐惧</strong></summary>
<p><strong>行情快照</strong>：2026-11-27 12:09（北京时间）Gate.io 公开 ticker，BTC/USDT 最新 <strong>61,420.8</strong>，24h 涨幅 <strong>+0.82%</strong>，24h 区间 <strong>59,923.9–61,862.7</strong>；ETH/USDT 最新 <strong>1,728.18</strong>，24h 涨幅 <strong>+1.56%</strong>，24h 区间 1,667.93–1,739.35。恐惧贪婪指数 <strong>12（Extreme Fear）</strong>。以上是时刻快照，只描述状态，不构成任何操作建议。</p>
<p><strong>市场与资金（The Block）</strong>：<a href="https://www.theblock.co/">JPMorgan 称 Strategy 的 NAV 倍数创新低，标志比特币「投降式」出清</a>；<a href="https://www.theblock.co/">现货 BTC ETF 可能创下史上最差月度</a>；<a href="https://www.theblock.co/">Galaxy 收回「6 月见底」判断，警告跌破 $58,525 后可能更深</a>；<a href="https://www.theblock.co/">欧洲唯一现货 BTC ETF 在瑞士开始交易</a>；<a href="https://www.theblock.co/">Fidelity 申请现货 Chainlink ETF</a>；<a href="https://www.theblock.co/">Tokenized Anthropic 持仓 3 天内翻倍</a>。</p>
<p><strong>监管与生态（The Block）</strong>：<a href="https://www.theblock.co/">美国众议院委员会推进「战略比特币储备」法案</a>；<a href="https://www.theblock.co/">瑞士批准 57 个司法辖区从 2028 年起交换加密数据</a>；<a href="https://www.theblock.co/">Warren 与 Van Hollen 推动取消 SEC 的 crypto 创新豁免</a>；<a href="https://www.theblock.co/">Zcash 团队呼吁加快淘汰旧版隐私方案，为「密码学突破」提前准备</a>；<a href="https://www.theblock.co/">LayerZero 把 Samsung Card、Kakao Pay、ZAN 纳入验证人</a>。安全与钱包相关操作请按官方公告与自有资产自查，本站不连钱包、不代执行命令。</p>
<p><strong>口径</strong>：行情、涨跌幅、热搜、情绪指数一律只作状态描述；只有直接影响在用资产可得性的公告才可能升级。安全事件只认项目方 advisory / 官方博客 / 交易所公告；媒体转述单独出现时降为观察。不连钱包、不签名、不导私钥、不代充提，不写买卖建议与目标价。</p>
</details>

<details>
<summary><strong>取数与来源健康度：25 源，402 条，14 源成功、11 源报错或异常</strong></summary>
<p>本轮按 <code>info-task-gc</code> 的 25 源口径执行，成功 14 源、报错/异常 11 源，合计 <strong>fetched=402 / sources=25 / errors=11</strong>。取数窗口 2026-11-27 11:55–12:09（北京时间）。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:16%;">来源</th><th style="padding:7px 8px 7px 0;width:12%;">条数</th><th style="padding:7px 8px 7px 0;width:14%;">状态</th><th style="padding:7px 0;">备注</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">epic</td><td style="padding:6px 8px 6px 0;">3</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">2 款 0 元（含 1 款原价 0）+ 1 折扣</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">hn</td><td style="padding:6px 8px 6px 0;">25</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">Algolia front_page</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">lobsters</td><td style="padding:6px 8px 6px 0;">25</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">hottest</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">github-trending</td><td style="padding:6px 8px 6px 0;">16</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">HTML 抓取</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">ithome</td><td style="padding:6px 8px 6px 0;">60</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">producthunt</td><td style="padding:6px 8px 6px 0;">50</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">lowendbox</td><td style="padding:6px 8px 6px 0;">20</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">idcspy</td><td style="padding:6px 8px 6px 0;">10</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS，含多条黑五转述</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">ruanyifeng</td><td style="padding:6px 8px 6px 0;">3</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">Atom，第 419/420/421 期</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">theblock</td><td style="padding:6px 8px 6px 0;">20</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">appinn</td><td style="padding:6px 8px 6px 0;">10</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">RSS，含 NFS 与 1Password 条目</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">appstore</td><td style="padding:6px 8px 6px 0;">109</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">iTunes JSON，新上架免费榜（非限免）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">steam</td><td style="padding:6px 8px 6px 0;">50</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">featuredcategories 10+30+10</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">fng</td><td style="padding:6px 8px 6px 0;">1</td><td style="padding:6px 8px 6px 0;color:#1a7f37;">成功</td><td style="padding:6px 0;">恐惧贪婪 12（Extreme Fear）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">panews</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">异常</td><td style="padding:6px 0;">RSS 入口返回 HTML 网页，非 feed</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">v2ex / hf / binance / coingecko / cgmarkets / cmc / ethblog / coindesk</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR ×8</td><td style="padding:6px 0;">代理下 000 / 连接被拒（curl exit 35）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:6px 8px 6px 0;">exstatus / creleases</td><td style="padding:6px 8px 6px 0;">0</td><td style="padding:6px 8px 6px 0;color:#c0392b;">ERR ×2</td><td style="padding:6px 0;">本轮未取到可用入口</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">8 个 ERR 是境外 HTTPS 接口在本轮通道里的 <code>000</code>（curl exit 35，连接被拒），没有 4xx / 410 类源站下线信号；<code>exstatus</code>、<code>creleases</code> 本轮没有稳定入口，按「未取」记录。<code>panews</code> 单列为「异常」而非「成功」，是因为该入口回的是 HTML 页面。行情用 Gate.io 公开 ticker 补位（单列，不计入 25 源）。</p>
</details>

<details>
<summary><strong>方法与边界</strong></summary>
<p><strong>四步口径</strong>：取数（25 源，归一化为标题 / 时间 / 链接 / 数值）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本篇 Pages 稿 + 仓库 <code>_posts/</code> 存档）。</p>
<p><strong>边界</strong>：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。</p>
<p><strong>执行说明</strong>：本轮用 <code>curl</code> 走沙箱代理（<code>HTTP(S)_PROXY</code>）直取各源，按上表逐源记录成功 / 报错 / 异常，没有用记忆或别站数据冒充；Epic 与 Steam 的价格均来自官方接口实测。今天是 2026-11-27，本文件是<strong>当天同一天内的第二次更新</strong>（首稿 00:10、本次 12:09），按「一天一份」规则只更新本文件，不新增第二篇。</p>
<p style="margin:24px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-27 11:55–12:09 接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，且本轮仅有 Gate.io 单源，不构成任何投资建议；新闻部分请注意「媒体转述」与「公司公告 / 官方接口」的区别。</p>
</details>
