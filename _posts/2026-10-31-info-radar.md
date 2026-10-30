---
title: "资讯雷达 2026-10-31｜币安提币暂停终于拿到一手公告、Go 默认 MPTCP 撞上内核 CVE、被投毒的 Claude Code 扩展"
author: OxYGC
date: 2026-10-31 06:32:00 +0800
permalink: /posts/info-radar-2026-10-31/
categories: [Info, Deals]
tags: [资讯雷达, 币安, 提币暂停, Go, CVE, Cursor, 限免, GitHub Actions]
description: "2026-10-31 一轮 25 个来源的资讯雷达：币安安全事件 Update #2 的一手原文核实到提币暂停与恢复目标，Go 安全团队就 CVE-2026-98432 说明 Go 1.24+ 默认开启 MPTCP，Cursor 应用商店的 Claude Code 扩展被检出后门，另有 App Store 国区五款本体限免与 GitHub Actions 昨日那次中断。"
---

这一轮 25 个来源全绿，取回 315 条、去重后 171 条进分级，0 个来源异常。和昨天最大的差别在币圈那一条：昨天「币安暂停提币」只能落在观察，因为三方媒体口径一致但官方公告原文取不到；今天币安自己发了《Security Incident Update #2》，我直接读到了公告正文——热钱包在 2026-10-29 20:05 (UTC) 被攻破、损失约 63 亿美元、提币临时暂停而充值与其他服务照常，官方给的是「约 34 小时后开始分批恢复」的目标时刻，以及 12 小时内跑首次 Proof of Reserves、11-02 前出结果。按口径，直接影响在用资产可得性的交易所公告就该升到紧急，这条今天升了。第二条紧急不在币圈而在开发工具链：Cursor 应用商店里的「Claude Code for VS Code」v2.1.313 被检出投放后门，处置动作涉及删文件与轮换凭据，装过的人需要当场自查。至于「值得」里我认为最实用的一条，是 Go 安全团队对 CVE-2026-98432 的说明——它把「内核漏洞」和「Go 1.24 起在 Linux 默认给监听套接字打开 MPTCP」连起来了，而这个默认值是可以一行关掉的。Epic 周免与昨天是同一条，去重命中，按旧闻不重推留在观察段，只把当场重取的官方接口值附上。

<div style="border:1px solid #eaedf1;border-radius:10px;padding:16px;background:#fbfcfd;">
  <p style="margin:0 0 10px;font-size:13px;font-weight:700;color:#8a9099;letter-spacing:1.2px;">行动清单</p>
  <table>
    <thead>
      <tr>
        <th style="text-align:left;">时点</th>
        <th style="text-align:left;">条目</th>
        <th style="text-align:left;">价格</th>
        <th style="text-align:left;">去哪</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">官方目标约 34 小时后分批恢复；PoR 结果 11-02 前</strong></td>
        <td>币安热钱包被盗约 $6.3B，提币暂停中（充值与其他服务正常）</td>
        <td><span style="background:#fdecec;color:#c0392b;border-radius:999px;padding:2px 9px;">服务不可用</span></td>
        <td><a href="https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751">币安公告原文</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">装过就立刻自查</strong></td>
        <td>Cursor 商店「Claude Code for VS Code」v2.1.313 后门（厂商已下架）</td>
        <td><span style="background:#fdecec;color:#c0392b;border-radius:999px;padding:2px 9px;">需轮换凭据</span></td>
        <td><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/">Phorion 披露原文</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">Apple 不公布限免截止时间</td>
        <td>App Store 国区五款本体限免（含一款接口调试工具）</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">下载 0 元</span></td>
        <td><a href="https://apps.apple.com/cn/app/api-testing-tool/id6739941752">App Store 页面</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">北京 11-11 01:00 前（接口给 2026-11-10 17:00 UTC）</td>
        <td>Steam《Nomad Drive》-10%</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">¥48.60（原 ¥54.00）</span></td>
        <td><a href="https://store.steampowered.com/app/2223980/?l=schinese">Steam 商店页</a></td>
      </tr>
    </tbody>
  </table>
  <p style="margin:10px 0 0;font-size:12px;color:#6b7280;line-height:1.75;">两处口径提醒：一是「34 小时 / 12 小时」都是币安公告里的目标时刻，不是承诺，以官方后续更新为准；二是 Steam 接口给的是 UTC 时刻，括号里已按北京时间换算，购买页显示以商店页文案为准。</p>
</div>

## 值得看（8）

<details>
<summary><strong>Go 安全团队说明 CVE-2026-98432：Go 1.24 起在 Linux 默认对监听套接字启用 MPTCP</strong> ｜ 免费公告 ｜ 无截止，但内核要尽快打补丁</summary>
<p>一手来源是 golang-announce 邮件列表（Neal Patel，2026-10-30 发出）。公告说这次披露的 CVE-2026-98432 是 <strong>Linux 内核 IPv4 TCP 连接处理里的 use-after-free</strong>；Anthropic 演示的利用路径针对暴露 Multipath TCP（MPTCP）监听的服务，可达远程代码执行。关键的一句是：<em>「自 Go 1.24 起，Go 程序在 Linux 上默认对监听套接字启用 MPTCP」</em>，所以一个普通的 Go HTTP 服务可能正好落在被演示的那条路径上。</p>
<p>缓解与根治的边界公告自己也讲得很清楚：</p>
<ul>
  <li>根治 = <strong>升级到已打补丁的内核</strong>；公告明说「这个 bug 并不特定于 MPTCP」，没有 MPTCP 监听的系统也可能被同类攻击打到。</li>
  <li>临时缓解 = 运行时设 <code>GODEBUG=multipathtcp=0</code>，或在主模块的 <code>go.mod</code> 里写 <code>godebug multipathtcp=0</code> 在构建期关闭。</li>
  <li>单 socket 粒度 = <code>net.Dialer.SetMultipathTCP</code> / <code>net.ListenConfig.SetMultipathTCP</code>，会覆盖 GODEBUG 设置。</li>
  <li>公告同时提醒：逐程序关闭是<strong>脆弱</strong>的缓解——「只要漏掉一个 MPTCP 监听没关，整台机器仍然危险」，并且它假设了所有可用 exploit 都依赖 MPTCP。Go 团队认为此刻改动 Go 的默认行为为时过早，讨论在 <a href="https://go.dev/issue/82717">go.dev/issue/82717</a>。</li>
</ul>
<p>价值判断：如果你在维护 Go 后端或自己的 Linux 机器，这条不是「读个热闹」，而是要照着过一遍清单——机器内核版本、哪些进程在监听、监听是不是 MPTCP。直链 <a href="https://groups.google.com/g/golang-announce/c/PCoQcdxoScw">golang-announce 原文</a> ｜核实于 2026-10-31 06:38（Go 官方邮件列表原文，非媒体转述）</p>
</details>

<details>
<summary><strong>Cursor 应用商店的「Claude Code for VS Code」v2.1.313 被检出后门</strong> ｜ 免费披露 ｜ 无截止，装过就要当场处置</summary>
<p>发现方是安全机构 Phorion，披露时间 2026-10-30。要点：问题版本是 Cursor Marketplace 上的「Claude Code for VS Code」扩展 <strong>v2.1.313</strong>，它在扩展里投放后门，会落地 SSH 密钥并建立到 <code>134.209.82.225</code> 的隧道；厂商已经将该版本下架。</p>
<p>公告给出的处置动作（<strong>这些操作由你自己完成，不涉及任何代为授权</strong>）：结束相关进程、删除 <code>~/.config/.smt</code>、移除被落地的密钥、<strong>轮换该机器上的 SSH 与 API 凭据</strong>，并改从官方渠道重装。</p>
<p>交叉印证：HN 685 分 / 435 评，lobste.rs 同期 129 赞（标题为「Backdoors in Claude Code for VS, Cursor official extensions」）。直链 <a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/">Phorion 披露原文</a> ｜核实于 2026-10-31 06:37</p>
</details>

<details>
<summary><strong>App Store 国区五款本体限免</strong> ｜ 下载 0 元 ｜ <span style="color:#c0392b;">Apple 不公布限免截止时间</span></summary>
<p>这一层依旧是「汇总频道做发现 + iTunes lookup 核现价」两层拼出来的，核价按播报正文里的 <code>trackId</code> 走，<strong>认 id 不认名字</strong>（国区常给 app 改名，按名字搜会认错另一个 app）。五款 2026-10-31 06:32 实测的国区下载价都是 <code>price = 0</code>：</p>
<table>
  <thead><tr><th style="text-align:left;">App</th><th style="text-align:left;">trackId</th><th style="text-align:left;">用途</th><th style="text-align:left;">iTunes 实测现价</th></tr></thead>
  <tbody>
    <tr><td><a href="https://apps.apple.com/cn/app/api-testing-tool/id6739941752">API Testing Tool</a></td><td>6739941752</td><td>接口调试，后端最对口的一款</td><td>免费</td></tr>
    <tr><td><a href="https://apps.apple.com/cn/app/101-circuits/id6818058085">101 Circuits</a></td><td>6818058085</td><td>电路解谜（最低系统 17.0）</td><td>免费</td></tr>
    <tr><td><a href="https://apps.apple.com/cn/app/linearama-smart-notes/id6745355956">Linearama - Smart notes</a></td><td>6745355956</td><td>线性笔记（最低系统 18.0）</td><td>免费</td></tr>
    <tr><td><a href="https://apps.apple.com/cn/app/%E7%BF%BB%E9%A1%B5%E6%97%B6%E9%92%9F%E5%A4%A9%E6%B0%94-aeroflap-ai/id6759275171">翻页时钟天气 : AeroFlap AI+</a></td><td>6759275171</td><td>翻页时钟 + 天气（最低系统 18.6）</td><td>免费</td></tr>
    <tr><td><a href="https://apps.apple.com/cn/app/file-explorer-player-pro/id1095142462">File Explorer &amp; Player [Pro]</a></td><td>1095142462</td><td>文件浏览器 Pro 版（最低系统 18.0）</td><td>免费</td></tr>
  </tbody>
</table>
<p>口径必须留在这里：<code>price == 0</code> 只能证明<strong>「今天下载不花钱」</strong>，iTunes 接口分不出「本就免费」和「促销中」，所以这几条不写成「限免仍在」；Apple 也不公布促销结束时间，因此这一类条目没有截止时间栏，我不会为了版式整齐编一个日期出来。另外两款本轮没进这份名单：Nota AI（兑换码型，兑换码不转载、只留原帖）与 AniMeteo（按播报里的 id 查不到上架记录，价格未核实），它们都在观察段。</p>
<p>直链见上表 ｜核实于 2026-10-31 06:32（按播报正文里的 trackId 逐条回 <code>itunes.apple.com/lookup?country=cn</code> 核价）</p>
</details>

<details>
<summary><strong>GitHub Actions / Pages / Webhooks 昨日一度 major 中断，现已恢复</strong> ｜ 免费状态页 ｜ 无截止，值得留作排查起点</summary>
<p>官方状态接口实测（2026-10-31 06:35）：<em>Incident with Actions, Pages, and Webhooks</em>，impact 为 major，created <code>2026-10-30T17:50:54Z</code>、resolved <code>2026-10-30T19:23:40Z</code>（北京时间 10-31 03:23 恢复）；此前还有一条 <em>Disruption with GitHub services</em>（critical，10-30T14:31Z 起，15:02Z resolved）。当前仍开着的是 <em>Incident with Dependabot</em>（minor，monitoring，10-30T20:59Z 起）。</p>
<p>为什么值得单独一条：本站的部署源就是 GitHub Actions，雷达稿每天也是走这条路推上去的。昨天那段窗口能解释「构建排队 / 部署红一次」的现象——<strong>下次遇到异常，先看状态页再怀疑稿件本身</strong>。直链 <a href="https://www.githubstatus.com">GitHub 状态页</a> ｜核实于 2026-10-31 06:35（官方 <code>api/v2/incidents.json</code>）</p>
</details>

<details>
<summary><strong>Agent Skills 生态两个仓库同时在 GitHub Trending</strong> ｜ 开源免费 ｜ 无截止</summary>
<p>GitHub API 于 2026-10-31 06:37 实读：<a href="https://github.com/mattpocock/skills">mattpocock/skills</a> 307,415 star、最近推送 2026-10-30；<a href="https://github.com/anthropics/skills">anthropics/skills</a> 185,254 star、最近推送 2026-10-28。前者的说明是「给真正工程师用的 Skills，直接来自我的 <code>.agents</code> 目录」，后者是官方 Agent Skills 公开仓库。</p>
<p>价值：和我自己在维护的私人 skill 体系是同一套东西。前者适合对照「个人 skill 目录怎么组织、怎么随工程演进」，后者适合看官方口径的 skill 结构。同批 trending 还有 <a href="https://github.com/lightpanda-io/browser">lightpanda-io/browser</a>（38,298 star，面向 AI 与自动化的无头浏览器），如果你在写抓取或自动化，比通用 headless Chrome 轻一档。</p>
</details>

<details>
<summary><strong>Go 1.28 HTTP/2 Parking 的内存节省实测</strong> ｜ 免费文章 ｜ 无截止</summary>
<p>作者把自己的测量写成一篇短文：Go 1.28 里 HTTP/2 的 parking 机制改动实际省下多少内存。<a href="https://abdolirad.me/articles/go-1-28-http2-parking-memory/">原文直链</a>，lobste.rs 9 赞。</p>
<p>诚实边界：数值是作者自测，我没有复测，引用时按「作者自测」表述，不要当成基准结论。对写 Go 后端与性能类内容的人，这类「一个语言改动换来多少内存」的一手测量是可以直接进素材库的形态。 ｜核实于 2026-10-31 06:31</p>
</details>

<details>
<summary><strong>npm 上的 <code>estee</code> 不是 <code>testem</code> 的拼写错误</strong> ｜ 免费文章 ｜ 无截止</summary>
<p><a href="https://smoores.dev/post/no_npm_estee_is_not_a_typo/">原文</a>（lobste.rs 25 赞）拆的是典型 typosquatting 形态：一个「看着像打错字」的名字其实是被登记的真实包，于是拼错的安装命令会静默装到别人手上。价值不在于这个具体包，而在于它给了一个可复用的自查动作——把 <code>package.json</code> 里的依赖名对着 registry 逐个核一遍，而不是只核版本号。 ｜核实于 2026-10-31 06:31</p>
</details>

<details>
<summary><strong>阮一峰《科技爱好者周刊》第 417 期：不要让 AI 代表你</strong> ｜ 免费 ｜ 无截止</summary>
<p>固定素材源，本期主题落在「AI 与个人表达的责任边界」，和写作、自动化方向直接相关。<a href="https://www.ruanyifeng.com/blog/2026/10/weekly-issue-417.html">周刊页</a> ｜核实于 2026-10-31 06:31（官方 Atom feed 条目，境内直连即 200）</p>
</details>

## 观察（12）、币圈那一轮与方法

<details>
<summary>观察清单：本轮落在这里的 12 条，以及每一条的存疑原因</summary>
<table>
  <thead><tr><th style="text-align:left;">条目</th><th style="text-align:left;">为什么只放观察</th></tr></thead>
  <tbody>
    <tr><td>Kraken 官方状态页今日仍是 minor「Partially Degraded Service」；Coinbase 为 none、All Systems Operational</td><td>一手已核实（06:36 直读 <code>status.kraken.com/api/v2/status.json</code>，页面 updated_at 2026-10-30T22:31Z；昨日那条「核实不到」的坑今天补上了）。剩下的存疑只有「你在不在用」——在用才需要去查具体受影响组件。</td></tr>
    <tr><td>Epic 国区周免《Sorry We're Closed》（¥78 → 0，北京 2026-11-06 00:00 收口）仍在档期</td><td>昨天已报同一条，去重键命中，按「旧闻不重推」不进值得。附当场重取的官方接口值（06:35：<code>originalPrice=7800</code>、<code>discountPrice=0</code>、<code>endDate=2026-11-05T16:00:00Z</code>）。下周 0 折位预告是《Idle Champions of the Forgotten Realms》与「浮游世界」。</td></tr>
    <tr><td>币安推迟 PREDICT 上线，另发《Important Notice on PREDICT Airdrop Token Allocation》</td><td>上币与活动类，不影响在用资产可得性；且公告正文接口仍取不到 body（两个 detail 端点均返回 <code>data:null</code>，06:36 实测）。</td></tr>
    <tr><td>Binance Earn「Yield Arena」本周新限时活动最高 35% APR</td><td>未核实：收益率类要回产品页核条款、额度与名额上限，这类活动通常有门槛。</td></tr>
    <tr><td>Northflank 被入侵、Bunny CDN 安全事件、Linode 安全事件、AO3 被黑（HN 同期）</td><td>未核实：只拿到标题级信息，没回到各家官方公告原文核影响面。若你在用其中任一家托管，请自己开官方公告页确认。</td></tr>
    <tr><td>Nota AI: Meeting Recorder Agent 播报「限免」</td><td>兑换码型限免：<strong>兑换码不转载</strong>，只留频道原帖由你自己取（<a href="https://t.me/TossTF/3795">TossTF/3795</a>）；同时它没走 iTunes 核价，价格未核实。</td></tr>
    <tr><td>AniMeteo 播报本体限免</td><td>iTunes 按播报里的 id 6817347643 查不到上架记录 ⇒ 价格未核实，不作为「现在免费」引用。</td></tr>
    <tr><td>LowEndBox《Mango Mail》万圣节最高 40% off、100GB 套餐 $8.70/月</td><td>未核实：只有博文标题的促销文案，没回厂商官网核最终价、是否续费同价，也没拿到截止时间。</td></tr>
    <tr><td>美国主机侦探的双 11 系列（Just Hosting VPS 首期 5 折 / 续费 6 折；芒果店长 ERP 新购 9 折 / 续费 8.5 折；CloudCone 新增澳新节点）</td><td>未核实：均为资讯站转述，无官方定价页核对，双 11 档期普遍不写死收口时刻——按发布门槛这类条目不能进「值得」。</td></tr>
    <tr><td>WHMCS 9.1 发布（支持 PHP 8.4、新增自动维护更新与 Cart API）</td><td>只有转述，没回官方 changelog；在用 WHMCS 的话以你自己站点的升级说明为准。</td></tr>
    <tr><td>行情快照（06:32，来源 CoinGecko / CoinMarketCap / alternative.me）：BTC $76,710（-2.9%）、ETH $2,233.33（-1.6%）、USDT $0.999086、BNB $697.93（-0.5%）、XRP $1.25（+0.2%）；前 300 内 24h 绝对变动 ≥8% 的是 Bitway -24.6%、Pepe +9.5%、Midnight +8.6%、Uniswap +8.5%、POL +8.1%；恐惧贪婪指数 30（Fear）</td><td>它是某一刻的数，不是可执行信息；不构成任何方向判断，也不构成任何操作建议。</td></tr>
    <tr><td>CoinGecko 热搜前几：Super Pepe / BTC / HYPE / SOL / PENGU；CMC 搜索榜前六：BTC / XRP / ETH / SOL / Beam / Irys</td><td>热度不是涨跌，本身不构成价值。</td></tr>
  </tbody>
</table>
</details>

<details>
<summary>币圈那一轮：升上去的一条、留在观察的一条，以及为什么这么分</summary>
<p>币圈的分级门槛比另外四条赛道更硬：<strong>只有直接影响在用资产可得性的公告才允许升紧急</strong>（下架、清退、充提暂停、服务降级、签名或依赖漏洞），行情、热搜、情绪指数默认只能落在观察，喊单、目标价、荐币、要求连钱包的一律过滤。</p>
<p>今天这条升了，依据是交易所自己的公告原文（不是媒体转述）：热钱包于 <code>2026-10-29 20:05 (UTC)</code> 被攻破，损失约 $6.3B 代币资产；<strong>提币临时暂停</strong>，充值与其他服务照常；技术团队目标是约 34 小时后开始分批恢复；计划 12 小时内跑首次 Proof of Reserves 快照，11-02（周一）前出结果；币安称以 SAFU 与公司资金承担，已备出 $6.34B（其中 $5B 为同种资产，覆盖约 80%），链上已冻结约 $30 亿；公告同时说目前没有证据显示钱包私钥泄露，并将在约 48 小时内分享更多技术发现。</p>
<p>你能做的只有两件事：确认自己在币安是否有资产，以及在官方分批恢复公告之前<strong>不做提币操作</strong>。要特别注意这类事件之后的常态污染：「帮你追回被盗资产」「加 TG 私聊客服」「先付 gas 才能领取」的钓鱼会激增——本轮的观察段里已经点了一条同类形态的边界，任何要求连接钱包或签名的内容我一律不写进正文，也不会代你做任何链上动作。</p>
</details>

<details>
<summary>四步口径：这一轮是怎么从 315 条走到 8 条的</summary>
<p>1. <strong>取数</strong>：<code>radar_fetch.py --all --days 2</code>，25 个来源，抓到 315 条、与历史去重后 171 条待分级，errors=0。境外源没有整批挂，说明本机代理节点正常。</p>
<p>2. <strong>验真</strong>：优惠/限免/额度必须回官方页核价格与截止。App Store 那五款是拿播报正文里的 <code>trackId</code> 回 <code>itunes.apple.com/lookup?country=cn</code> 逐条核价（认 id 不认名字）；Epic 是当场重取 <code>freeGamesPromotions?country=CN</code>；Steam 折扣取官方 <code>featuredcategories</code>（cc=cn）；币圈的公告回到交易所公告原文，Kraken / Coinbase 回到两家 Statuspage 的 <code>status.json</code>；Go 那条回到 golang-announce 原文。核不到的一律降级，并写明「未核实」。</p>
<p>3. <strong>分级</strong>：紧急只看两种——会过期到跟前，或影响在用服务；币圈再收紧到「影响在用资产可得性」。值得必须已核实 + 能落到具体动作。没核实的只进观察并写存疑原因。这一轮过滤掉的是转述式促销与所有热度榜单类噪声。</p>
<p>4. <strong>边界</strong>：全程只到报告。不注册、不绑卡、不代领券、不下单、不点任何购买或领取按钮；币圈不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价。产物里不出现凭据、webhook、内网地址、钱包地址与带邀请返利参数的链接。</p>
</details>
