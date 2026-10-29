---
title: "资讯雷达 2026-10-30｜Epic 周免换到《抱歉我们打烊了》、Steam 两款补票位、GitLab 那个被打的 CVE"
author: OxYGC
date: 2026-10-30 06:40:00 +0800
permalink: /posts/info-radar-2026-10-30/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Epic, Steam折扣, App Store 限免, GitLab, 币圈]
description: "2026-10-30 一轮 25 个来源的资讯雷达：Epic 本周限免已换档并重新核到截止时间、Steam 两款折扣经官方接口与商店页双轨核对、App Store 国区三款本体限免按 trackId 核价、GitLab CVE-2026-97229 的一手 advisory，以及币圈那一整轮里唯一没升上去的提币暂停。"
---

这一轮 25 个来源全绿，取回 290 条、去重后 170 条进分级，0 个来源异常。最后留在「值得」的是 6 条，其中最省事的一条又是 Epic：昨天还挂着「下周预告」的《抱歉我们打烊了》今天已经是本周正主，而它在 `--all` 那一轮里因为去重键命中被挡在门外（`epic` 源本轮 0 条新），所以截止时间是我当场单取一次官方接口重读出来的，不是抄昨天的。另一件值得说的是币圈：这一轮真正可能升到紧急的那条——「币安暂停提币」——最后没升，因为三方媒体口径一致，但官方公告原文取不到，按规矩只能落在观察。行动清单里那个「两处口径不一致以商店页为准」的写法也是这个来路：Steam 接口给的是 UTC 时刻，商店页文案给的是本地表述，我不想替读者做一道会出错的换算。

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
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">北京 11-06 00:00</strong></td>
        <td>Epic 本周限免《抱歉我们打烊了》（Sorry We're Closed）</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">0 元（原 ¥78.00）</span></td>
        <td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">商店页写「11 月 5 日截止」</td>
        <td>Steam《Raft》周末特惠 -33%</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">¥51.59（原 ¥77.00）</span></td>
        <td><a href="https://store.steampowered.com/app/648800/">Steam 商店页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">商店页写「11 月 10 日截止」</td>
        <td>Steam《R.E.P.O.》特别促销 -35%</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">¥22.75（原 ¥35.00）</span></td>
        <td><a href="https://store.steampowered.com/app/3241660/">Steam 商店页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">Apple 不公布截止时间</td>
        <td>App Store 国区三款本体限免（贴纸 / 图片浏览 / 日历高亮）</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">下载 0 元</span></td>
        <td><a href="https://apps.apple.com/cn/app/id1510670815">Cute Paper Stickers</a></td>
      </tr>
    </tbody>
  </table>
  <p style="margin:10px 0 0;font-size:12px;color:#8a9099;">需要你自己去领取或下单，这里只登记价格与截止时点，不代领、不下单。</p>
</div>

## 值得看（6）

<details open>
<summary><strong>Epic 本周限免《抱歉我们打烊了》</strong> ｜ <span style="color:#1a7f37;">0 元（原 ¥78.00）</span> ｜ 截止 <span style="color:#c0392b;font-weight:700;">北京时间 2026-11-06 00:00</span></summary>
<p>昨天它还挂在「下周预告」那一栏，今天已经是本周正主。官方接口实测 <code>totalPrice.discountPrice=0</code>、<code>originalPrice=7800</code>（分位为 CNY，即 ¥78.00 全款被折到 0），<code>appliedRules[].endDate</code> 是 <code>2026-11-05T16:00:00Z</code>，折到北京时间正好 11-06 00:00。这类条目唯一的风险是过期后按原价，所以收口时刻必须重新读一次而不是沿用昨天。</p>
<p>本轮 <code>--all</code> 那一跑里 <code>epic</code> 源报了 0 条新——去重键按标题生成，同一款周免在昨天已经登记过。所以上面这两个数不是从缓存里抄的，是 06:35 单独打一次 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN&amp;allowCountries=CN</code> 重取的一手值，同时也和 IT之家当天那篇《Epic 喜加一》报道对上了。</p>
<p>去哪：<a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a> ｜ 核实于 2026-10-30 06:35</p>
</details>

<details>
<summary><strong>Steam《Raft》</strong> ｜ <span style="color:#1a7f37;">¥51.59（-33%，原 ¥77.00）</span> ｜ 截止 <strong>商店页原文「周末特惠！11 月 5 日截止」</strong></summary>
<p>沙盒生存合作游戏，一个人能玩、多人不排队，这个价在它的历史区间里属于补票位而不是抄底价。两层核实：价格取 <code>appdetails?cc=cn&amp;l=schinese</code>（<code>discount_percent=33</code>、<code>final_formatted=¥ 51.59</code>、<code>initial_formatted=¥ 77.00</code>）；截止取商店页正文里那句倒计时文案，实测读到的是「周末特惠！11 月 5 日截止」。</p>
<p>这里有一处口径不一致要如实写下来：抓取字段给的 <code>until</code> 是 <code>2026-11-05T18:00</code>，若按 UTC 折算是北京 11-06 02:00，和页面文案的「11 月 5 日」差了半天。我没有第三个独立证据去裁定它，所以正文以官方商店页文案为准，不做二次换算。</p>
<p>去哪：<a href="https://store.steampowered.com/app/648800/">store.steampowered.com/app/648800</a> ｜ 核实于 2026-10-30 06:36</p>
</details>

<details>
<summary><strong>Steam《R.E.P.O.》</strong> ｜ <span style="color:#1a7f37;">¥22.75（-35%，原 ¥35.00）</span> ｜ 截止 <strong>商店页原文「特别促销！11 月 10 日截止」</strong></summary>
<p>多人合作物理搬运，单人价值有限、凑朋友局才划算，这点要提前说清。官方接口 <code>discount_percent=35</code>、<code>final_formatted=¥ 22.75</code>、<code>initial_formatted=¥ 35.00</code>，商店页标题渲染成「在 Steam 上购买 R.E.P.O. 立省 35%」，倒计时文案是「特别促销！11 月 10 日截止」。同一处 <code>until</code> 字段口径差异照旧存在（字段 2026-11-09T17:00），处理方式同上。</p>
<p>去哪：<a href="https://store.steampowered.com/app/3241660/">store.steampowered.com/app/3241660</a> ｜ 核实于 2026-10-30 06:38</p>
</details>

<details>
<summary><strong>App Store 国区三款本体限免</strong> ｜ <span style="color:#1a7f37;">下载不花钱</span> ｜ 截止 <strong>Apple 不公布限免截止时间</strong></summary>
<p>三款都是在播报里出现、再按正文里的 <code>trackId</code> 回 <code>itunes.apple.com/lookup</code> 逐条核价的：<code>Cute Paper Stickers</code>（id1510670815，最低系统 17.6）、<code>Photo View 照片浏览器</code>（id665540219，最低系统 15.0）、<code>Horizon: Calendar Highlights</code>（id6761135453，最低系统 18.6）。国区现价三条都实测为「免费」。</p>
<p>两处诚实的限制：第一，Apple 没有官方限免接口，核到 <code>price==0</code> 只能说「下载不花钱」，接口分不出「本来就免费」和「正在促销」，所以这里不写成「限免仍在」；第二，Apple 不公布促销结束时间，这一栏就真的没有截止时间可写，我不编一个。之所以按 id 而不是名字核，是因为国区会给应用改名，按名字搜会把别人的免费价安到这条上。</p>
<p>去哪：<a href="https://apps.apple.com/cn/app/id1510670815">Cute Paper Stickers</a> ｜ <a href="https://apps.apple.com/cn/app/id665540219">Photo View 照片浏览器</a> ｜ <a href="https://apps.apple.com/cn/app/id6761135453">Horizon: Calendar Highlights</a> ｜ 核实于 2026-10-30 06:34</p>
</details>

<details>
<summary><strong>Mistral Large 4 开放权重</strong> ｜ <span style="color:#6b7280;">开发者动态</span> ｜ 无截止</summary>
<p>可以自托管的权重型号，意义在于把「必须走 API」的那层依赖拿掉——离线推理、微调基座、成本可控这三件事同时成立。官方新闻页实测可达（HTTP 200），同期 HN 上这条是 1066 分 / 310 评的热帖，属于一手来源与社区热度都对得上的那种。</p>
<p>去哪：<a href="https://mistral.ai/news/mistral-large-4-oss/">mistral.ai/news/mistral-large-4-oss</a> ｜ 核实于 2026-10-30 06:37</p>
</details>

<details>
<summary><strong>GitLab CVE-2026-97229 被实际尝试利用，Alpine 整台实例重建</strong> ｜ <span style="color:#6b7280;">安全公告</span> ｜ 需要自查，无截止</summary>
<p>这条的价值全在「一手」：Alpine 官方博客原文写得很直白——10 月 20 日和 21 日，攻击者在补丁发布一周后仍然对他们打这个漏洞，「差一点就成功了」；没有找到得手证据，但也无法排除，所以按已沦陷处理、从零重建实例。对照自家环境的话，要做的动作很具体：确认 GitLab 版本是否已含修复、翻一遍 access log 里 10-20/10-21 前后的异常请求、以及检查 CI runner 与部署密钥需不需要轮换。</p>
<p>如果你只托管 GitHub 侧仓库，这条就当背景知识；只要有自建 GitLab 或 GitLab CI，它就是一条今天能做完的清单。</p>
<p>去哪：<a href="https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html">alpinelinux.org 公告原文</a> ｜ 核实于 2026-10-30 06:37</p>
</details>

## 观察（12）、币圈那一轮与方法

<details>
<summary>观察清单：12 条，每条都写明为什么没能升上去</summary>
<table>
  <thead>
    <tr><th style="text-align:left;">条目</th><th style="text-align:left;">存疑原因 / 门槛</th><th style="text-align:left;">来源</th></tr>
  </thead>
  <tbody>
    <tr><td>币安疑似被盗约 56 亿美元、暂停提币</td><td>只有媒体转述，官方公告原文没取到（安全事件要认项目方 advisory / 官方博客 / 交易所公告三方之一）</td><td>CoinDesk / TheBlock / PANews，2026-10-29</td></tr>
    <tr><td>Kraken 服务「部分降级」</td><td>官方状态页核实不到：<code>kraken.statuspage.io</code> 无响应、<code>www.kraken.com/status</code> 返回 404，两次探测</td><td>exstatus 汇总，2026-10-30 06:34</td></tr>
    <tr><td>Coinbase 服务状态</td><td>已核实但无价值：<code>status.json</code> 实测 <code>indicator=none</code>、All Systems Operational</td><td>Coinbase 官方状态页，2026-10-30 06:34</td></tr>
    <tr><td>iOS 限免 <code>StockPing Price Alerts</code></td><td>未核实：按播报里的 id 6817288336 在 iTunes 查不到上架记录，价格无法确认</td><td>TossTF 播报，2026-10-29 02:49</td></tr>
    <tr><td>iOS 限免 <code>Parallel: Dual Video Camera</code></td><td>未核实：播报正文没有 App Store 直链，取不到 trackId，也就无从核价</td><td>TossTF 播报，2026-10-29 02:57</td></tr>
    <tr><td>EverTrans「内购限免」</td><td>只算转述：国区下载价本就是 0，内购解锁价不体现在下载价上，接口验不到</td><td>TossTF + iTunes lookup，2026-10-30 06:34</td></tr>
    <tr><td>华纳云双 11（轻量云 246 元/半年）、优麦云双 11（包年 2592 元/年起）、Rank Math 万圣节最高 40% off</td><td>未核实：只有促销文案转述，没回到商家官方定价页核价格与收口时刻，双 11 档期普遍不写死截止时间</td><td>idcspy，2026-10-29</td></tr>
    <tr><td>DMIT 调整 Cogent IP 规则：每个 IPv4 每月 1 美元，支持自助切换</td><td>未核实：转述来源，没回到 DMIT 官方公告核生效时间与适用范围。手里有 DMIT 机器的话这条会影响月账单，值得自己确认</td><td>idcspy，2026-10-29 08:47</td></tr>
    <tr><td>ServerHost 500 美元抽奖 + 16.99 美元/年 VPS</td><td>门槛高且未核实：要注册参抽，抽奖类不承诺可得</td><td>LowEndBox，2026-10-29 11:00</td></tr>
    <tr><td>v2ex「OpenAI 有个小福利 去领一下」</td><td>未核实且要登录账号：转述帖，看不到官方条款与额度上限</td><td>v2ex，2026-10-29 02:42</td></tr>
    <tr><td>行情快照与情绪指数</td><td>是数字不是信息：BTC 79,045.31、ETH 2,273.62、BNB 704.73、HYPE 92.81、UNI 6.42、XMR 619.99；24h HYPE +14.5%、ENA -13.8%、NEAR -12.8%、UNI -11.2%、ARB -11.0%；恐惧贪婪指数 51（Neutral）</td><td>CoinGecko / alternative.me，2026-10-30 06:31 快照</td></tr>
    <tr><td>币安上 Predict (PREDICT) 并挂 Seed Tag、新开多个 TradFi USDⓈ 永续合约</td><td>已在币安官方公告列表核实存在（06:33 直读两个入口），但属上币信息，不影响在用资产的可得性，所以不升</td><td>币安公告列表，2026-10-29</td></tr>
  </tbody>
</table>
</details>

<details>
<summary>这一轮怎么跑的：四步口径与来源健康度</summary>
<p>四步：<strong>取数</strong>（<code>radar_fetch.py --all --days 2</code>，25 个来源归一化成 NDJSON）→ <strong>验真</strong>（价格与截止回官方页二次确认；iOS 按 <code>trackId</code> 回 iTunes 认 id 不认名字；币圈公告回公告原文核生效时间与合约地址）→ <strong>分级</strong>（🔥 紧急 / ⭐ 值得 / 👀 观察 / ❌ 过滤，宁严勿松）→ <strong>落盘与发布</strong>（本地日报 + 这份 Pages 稿）。整个链路只收集与核实，不代注册、不绑卡、不领券、不下单；币圈侧不连钱包、不签名、不给买卖建议与目标价。</p>
<p>来源健康度：<code>SUMMARY fetched=290 fresh=170 sources=25 errors=0</code>，本轮无整源故障。逐源条数：hackernews 25、ithome 25、producthunt 15、panews 15、lobsters 14、coindesk 12、coingecko-trending 10、v2ex 9、theblock 8、idcspy 7、coingecko-markets 7、coinmarketcap-search 6、appstore 6（4 条核到价、2 条未核实）、github-trending 4、steam 2、binance 2、lowendbox 1、exstatus 1、fng 1。</p>
<p>本轮 0 条的 6 个来源都不是故障：<code>appinn</code> 报了 <code>INFO source=appinn empty=本轮无符合条件的新条目（非故障）</code>；<code>epic</code> 是去重键命中（同一款周免此前已登记，价格与截止已单独重取）；<code>hf</code> / <code>ruanyifeng</code> / <code>ethblog</code> / <code>creleases</code> 为去重命中或当页无新内容。</p>
<p>币圈这一轮的判级特别窄，说明白一点：行情、热搜、情绪指数默认全部落在观察，因为它们是数字而不是信息；只有直接影响在用资产可得性的公告（下架、清退、充提暂停、服务降级、签名或依赖漏洞）才允许升紧急。这一轮唯一够到「充提暂停」的那条卡在官方原文取不到，所以最终 🔥 是 0 条——不是没有大事，是我没能把它核实到可以替你做判断的程度。</p>
</details>
