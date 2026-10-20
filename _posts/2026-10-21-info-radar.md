---
title: "资讯雷达 2026-10-21｜Epic 周免剩 40 小时、Steam 国区周促、eMudhra 中间 CA 被攻破"
author: OxYGC
date: 2026-10-21 06:34:00 +0800
permalink: /posts/info-radar-2026-10-21/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, App Store限免, Steam促销, eMudhra, Cloudflare, 币圈]
description: "2026-10-21 一轮 25 个来源取回 318 条、去重后 173 条新、0 个 ERR，留下 8 条值得与 14 组观察。本轮最要紧的不是新羊毛，而是把 EDG 开源这条按官方页的公开日期压回观察，以及交代 huggingface 那一站 0 条的真实原因是窗口过滤而不是到不了。"
---

今早这一轮 25 个来源全绿、0 个 ERR，取回 318 条、按两天窗口跨天去重后剩 173 条。分级结果和前三天一样没有 🔥：最近的截止是 Epic 本批周免的 10-22 23:00（接口口径，剩约 40 小时），没有一条命中在用的域名、VPS 或依赖里的免费额度，所以 🔥 段整段是空的。值得这 8 条的来源结构很清楚：限免占 5 条（Epic 两款周免今日回接口复验仍在架、App Store 国区三款本体限免全部回 iTunes 核到现价免费），优惠 1 条（Steam 国区《幻兽帕鲁》¥108.00 → ¥75.60，用 `appdetails` 与 `featuredcategories` 两个官方接口交叉核到价格和 `discount_expiration`），开发动态 2 条（eMudhra 中间 CA 被攻破这件事的一手来源是 Mozilla 官方博客，Cloudflare 的 tsrs 是官方博客原文）。这一篇有两处是我自己主动改判的：一处是 **EDG 开源**——它昨天在 lobsters 上热了一整天，回官方页却写着「On September 30, 2026, the source for EDG's C++ front end went public」，源码公开是三周前的事，热帖不等于新福利，所以按旧闻压回观察、没有为了凑「值得」的数量留下它；另一处是 **huggingface daily papers 本轮 0 条**——昨天它报的是 `URLError`，今天我单独复跑：`--days 30` 有 15 条、`--days 2` 一条没有，论文时间戳落在 10-14 ~ 10-17，同时 `curl https://huggingface.co/papers` 走代理 200、直连 000，所以今天的 0 条是**窗口过滤**不是到不了，这个区别决定了要不要动脚本。币圈那 11 个源一条都没有升 🔥：交易所侧最重的消息是 Kraken 的 `Digital Currency Funding` 组件 `degraded_performance`（我直读它的 Statuspage 组件 JSON 确认到组件名，不是媒体转述），它是某一种入金方式降级，不是充提暂停，也不是交易所整体不可用，而「要不要紧」取决于你在不在里面挂着资产——雷达没有这项证据，所以它只能留在观察；行情、热搜、恐惧贪婪指数这些数字全部照实贴但一律不给 ⭐，也不给任何方向判断。

<div style="border:1px solid #e8ebef;border-radius:10px;padding:16px 18px;margin:0 0 26px;background:#fbfcfd;">
  <p style="font-weight:700;font-size:16px;color:#1f2329;margin:0 0 10px;">四条要记的时点，都在本周内关窗</p>
  <table>
    <thead><tr><th>截止 / 时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
    <tbody>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-22 23:00（剩约 40 小时）</span><br><span style="font-size:12.5px;color:#6b7280;">接口口径；商店页渲染成 10-23 00:00</span></td><td>Epic 本批限免《Agent A - 伪装游戏》《Bad Cheese》</td><td>0 元领取入库</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-23 01:00（北京）</span><br><span style="font-size:12.5px;color:#6b7280;">官方 <code>discount_expiration = 2026-10-22T17:00Z</code></span></td><td>Steam 国区《Palworld / 幻兽帕鲁》周促</td><td>¥108.00 → ¥75.60（-30%）</td><td><a href="https://store.steampowered.com/app/1623730/?l=schinese">Steam 商店页</a></td></tr>
      <tr><td>Apple 不公布限免截止时间</td><td>App Store 国区《记办猫》《Glassiu 浏览器》《Versatil Markdown》</td><td>0 元下载</td><td><a href="https://apps.apple.com/cn/app/id1590485332">记办猫的 App Store 页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">即时（无截止）</span><br><span style="font-size:12.5px;color:#6b7280;">Mozilla 公告发布于 10-20</span></td><td>eMudhra 中间 CA 被攻破，浏览器侧开始处置</td><td>免费（CA 侧变更）</td><td><a href="https://blog.mozilla.org/security/2026-10-20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/">Mozilla 官方博客</a></td></tr>
    </tbody>
  </table>
  <p style="font-size:13.5px;color:#6b7280;margin:0 0 10px;">另有开发 / AI 动态 2 条、限免 5 条、优惠 1 条构成下面的「值得看（8）」；未核实、门槛高、本身只是数字的 14 组放在最后一节，其中包含一条我自己改判的降级。以下全部默认收起，点开看细节。</p>
</div>

## 值得看（8）

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">点击任意一条展开：价值判断、完整价格、核实到的接口字段都在里面。雷达只负责把消息带到——领取、下单、注册、绑定支付方式都由你自己完成。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Agent A - 伪装游戏 ｜ <span style="color:#1a7f37;">0 元</span> ｜ <span style="color:#c0392b;">10-22 23:00（接口口径）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>潜行解谜口碑款，价值在<strong>领取即永久入库</strong>，不需要在截止前玩完。这一档已经在架几天，昨天与今天都回官方接口复验过，不是旧闻重推——今天这一轮它在 <code>--all</code> 里被跨天去重命中（0 条），我 06:38 单跑一次复测才确认它仍在架。</p>
    <p>截止口径要单独交代：接口 <code>endDate = 2026-10-22T15:00:00Z</code> 换算是北京时间 10-22 23:00，而同一时刻的中文商店页把截止渲染成「10月23日 00:00」（本机 +0800）。两处都是官方来源、差一小时，条目按早的那条算，也就是剩约 40 小时。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口 <code>freeGamesPromotions</code> 命中 <code>endDate = 2026-10-22T15:00Z</code>、<code>discountSetting.discountPercentage = 0</code>（后者是「真限免」的唯一判据）、原价 <code>¥62.00</code>｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Bad Cheese ｜ <span style="color:#1a7f37;">0 元</span> ｜ <span style="color:#c0392b;">10-22 23:00（接口口径）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>与上一条同一批、同一截止，Epic 每周固定同时放两款，所以这两条只做一次决定就够。恶搞 / 派对向小品，合不合口味另说，0 元入库的机会成本几乎为零。</p>
    <p style="font-size:12.5px;color:#6b7280;">同一次接口读取：<code>endDate = 2026-10-22T15:00Z</code>、<code>discountPercentage = 0</code>、原价 <code>¥40.00</code>｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：记办猫（播报名 Todo-Cat） ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>待办类工具，汇总频道 10-20 播报为「本体限免」。这一层没有官方接口，所以取法是「频道发现 + 回 <code>itunes.apple.com/lookup</code> 用播报正文里的 <code>trackId</code> 核国区现价」——**认 id 不认名字**，因为国区会改名（这条播报名 Todo-Cat，商店里挂的是「记办猫」），按名字搜会认错成另一个 app、把别人的免费价安到这条上。</p>
    <p>两条边界照旧要写：Apple 不公布促销结束时间，所以这一档<strong>没有截止时间可写</strong>，不为了版式齐去编一个；而 lookup 分不出「本就免费」与「促销中」，因此只能写「今天下载不花钱」，不能写「限免仍在」。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=1590485332&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「记办猫」、发行商 镔钥 陆、最低系统 14.0｜<a href="https://apps.apple.com/cn/app/id1590485332">App Store 页</a> ｜ 核实于 10-21 06:31（取数轮内）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Glassiu 浏览器（视频嗅探 &amp; 油猴脚本 &amp; 广告拦截） ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>网页视频流嗅探 + 脚本注入 + 拦截，三件事合成一个浏览器。这批 iOS 限免里最贴工程场景的一款：做抓取、看回放链路、验证「页面实际请求了哪些 m3u8」这类活，它比待办类有用。同一条 iOS 口径——现价免费＝下载不花钱，不写「限免仍在」。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=6809207083&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「Glassiu 浏览器: 视频嗅探&amp;油猴脚本&amp;广告拦截」、发行商 一文 陈、最低系统 15.6｜<a href="https://apps.apple.com/cn/app/id6809207083">App Store 页</a> ｜ 核实于 10-21 06:31（取数轮内）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Versatil Markdown（macOS） ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>Mac 端 Markdown 编辑器，是这一批 iOS 播报里唯一的桌面端条目，对以 Markdown 为主战场的人（写作、README、笔记）是直接可用的一档。口径同上：核到 <code>price = 0</code> 只说明下载不花钱，不代表促销仍在期。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=997373210&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「Versatil Markdown」、发行商 digitalMoksha LLC、最低系统 15.4、<code>mt=12</code>（Mac 应用）｜<a href="https://apps.apple.com/cn/app/id997373210">App Store 页</a> ｜ 核实于 10-21 06:31（取数轮内）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Steam 国区周促：Palworld / 幻兽帕鲁 ｜ <span style="color:#1a7f37;">¥75.60（-30%）</span> ｜ <span style="color:#c0392b;">10-23 01:00（北京）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>本轮 Steam 特殊促销共 10 条，其中 9 条是往期已经报道过的存量（见观察段第一条），只有这一条是本轮新报，所以它进值得、其余不重复铺陈。价格与截止是用两个官方接口交叉出来的：<code>appdetails?cc=cn&amp;l=schinese</code> 给 <code>initial 10800 / final 7560 / discount_percent 30</code>，<code>featuredcategories</code> 给 <code>discount_expiration</code>，两者换算成 <code>¥108.00 → ¥75.60</code> 与北京时间 10-23 01:00。</p>
    <p>顺手记一条取数层的实现事实：<code>discount_expiration</code> 是 epoch 秒，脚本按 UTC 输出成 <code>2026-10-22T17:00:00</code>，直接读容易误当成北京时间——本稿写的是换算后的 <b>10-23 01:00</b>。同批里 <strong>Street Fighter 6 的截止更早（10-22 01:00 北京）</strong>，如果你恰好在等它，那一档才是时间最紧的一条。</p>
    <p style="font-size:12.5px;color:#6b7280;">官方接口 <code>price_overview = {currency: CNY, initial: 10800, final: 7560, discount_percent: 30}</code>、<code>discount_expiration = 1792688400（= 2026-10-22T17:00Z）</code>｜<a href="https://store.steampowered.com/app/1623730/?l=schinese">Steam 商店页</a> ｜ 核实于 10-21 06:36</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">eMudhra 中间 CA 被攻破，Mozilla 已发处置公告 ｜ <span style="color:#1a7f37;">免费（CA 侧变更）</span> ｜ <span style="color:#c0392b;">即时生效，无截止</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这条进「值得」的理由不是它新，而是<strong>它是本轮唯一一条可能需要你动手复查自己资产的安全事件</strong>：eMudhra（印度 CA）的中间证书被攻破，浏览器厂商开始处置，而处置就是往信任库里加屏蔽条目。同一事件在 HN 与 lobsters 两源同时上榜，但一手来源是 Mozilla 官方博客本身，所以判据按官方博客正文取。</p>
    <p>要划清的边界：这不影响你用 Let's Encrypt 或云厂商签发的证书，也不需要你换域名、换服务器。真正要做的只有一件事——确认手上有没有以 eMudhra 为签发链的证书（自建 PKI、企业内部 CA、某些地区性云的服务证书是可能踩到的三类）；有就按厂商公告换发。雷达不代登录任何控制台、不代操作证书。</p>
    <p style="font-size:12.5px;color:#6b7280;">回源 HTTP 200，页面 <code>&lt;title&gt;</code> 命中「Protecting Firefox users following the compromise of eMudhra intermediate certificates」，正文发布日期 <code>2026-10-20</code>｜<a href="https://blog.mozilla.org/security/2026-10-20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/">Mozilla Security Blog</a> ｜ 核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Cloudflare 开源 tsrs：把 TypeScript 移植成 Rust ｜ <span style="color:#1a7f37;">免费（开源）</span> ｜ <span style="color:#6b7280;">官方博客 2026-10-20</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>对做大仓构建、又在给 TypeScript 提速的人，这条的技术路线本身就是参考价值：把 TS 用 Rust 重写，动因是现有实现（Go 写的 <code>tsc</code> 替代工具）在超大代码库上的性能与内存天花板。它和你手上 Java / Go / C++ 后端的直接关系不大，但如果关注「编译器工具链换语言能拿到多少倍速」，这是今年第二个成规模的公开样本（第一个是 Biome / oxc 那条线）。</p>
    <p>口径说明：来源是 Cloudflare 官方博客原文，不是 HN 的标题转述；本条只报道「项目公开了」，性能数字要你自己去读原文里的那组基准，我不在稿子里转述成结论。</p>
    <p style="font-size:12.5px;color:#6b7280;">回源 HTTP 200，页面 <code>BlogPosting.headline</code> 命中「Introducing tsrs: a Port of TypeScript to Rust」，发布日期 2026-10-20｜<a href="https://blog.cloudflare.com/typescript-rust-port/">Cloudflare Blog</a> ｜ 核实于 10-21 06:38</p>
  </div>
</details>

## 观察（14 组）、币圈那一轮与方法

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">这一节收的是「没核实到一手」「门槛要你自己跨」「本身只是数字」，以及<strong>我自己改判降级的那一条</strong>。它们不构成价值，但可能决定你要不要自己再去确认一次。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open="open">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">本轮的降级：EDG 开源是热帖，但不是新事件</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>lobsters 昨天有一条《EDG is open source》在热，按标题它完全够进「开发 · AI 动态」。回官方页 <code>edgcpp.org</code> 读正文，第一段就写着 <strong>On September 30, 2026, the source for EDG's C++ front end went public</strong>——源码公开是三个星期前的事，本周才被社区重新讨论。按「旧闻重推」这条口径，它不进「值得」，留在观察。</p>
    <p>这件事值得单独写一段是因为判据：<strong>信息在不在热榜，和它是不是新消息，是两件独立的事</strong>。RSS / API 的时间戳只能证明「这条帖子什么时候发的」，不能证明「这件事什么时候发生的」，所以涉及产品发布、开源、政策生效这一类，正文里的日期才是准的那一个。</p>
    <p style="font-size:12.5px;color:#6b7280;">回源 HTTP 200，正文命中「On September 30, 2026, the source for EDG's C++ front end went public」，并列出 History / transition FAQ / Get involved 栏目｜<a href="https://edgcpp.org/">EDGCPP 官方页</a> ｜ 核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 那两款不是限免，是打折 ｜ <span style="color:#6b7280;">¥11.55 / ¥12.40，至 11-03 00:00（北京）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>商品</th><th>标价 → 现价</th><th>实际支付比例</th><th>档期（UTC）</th></tr></thead>
      <tbody>
        <tr><td>纪念碑谷（Monument Valley）</td><td>¥33.00 → ¥11.55</td><td><code>discountPercentage = 35</code>（付三成半）</td><td>2026-10-19T15:00Z ~ 2026-11-02T16:00Z</td></tr>
        <tr><td>Eternal Threads</td><td>¥62.00 → ¥12.40</td><td><code>discountPercentage = 20</code>（付两成）</td><td>同上</td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;">判据一句：<strong><code>discountPercentage</code> 是最终要付的百分比，<code>0</code> 才等于免费</strong>。昨天稿子里把这两款预告成「今晚开领免费」是错的，以这一条为准；今天这一轮取数层的输出已经把两者标成「打折」而非限免，也就是误读口径已经改回来了（限免判据收紧成 <code>discountPercentage == 0</code>）。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：Epic <code>freeGamesPromotions</code> 接口，06:38 单跑 <code>--source epic --days 7</code>，<code>fetched=4 / errors=0</code>，其中 2 条 <code>discountPercentage = 0</code>（限免，见值得段）、2 条非 0（本条）｜核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">iOS 那条是内购限免，不算下载免费</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>《Email Generator - Temp Mail》（id <code>6759259780</code>，发行商 Kreate Ventures FZE，最低系统 16.0）播报类型是<strong>内购限免</strong>：app 本身的下载价一直是 0，限的是内购项目的解锁价。而 iTunes lookup 只给下载价，拿它证明不了内购项免掉了，所以按口径只能算转述，不给 ⭐。同一条播报里另一类要单独处理的是<strong>兑换码型限免</strong>——兑换码一律不转载、不拼进产物，只留频道原帖由你自己取，这一条本轮没有出现。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=6759259780&amp;country=cn</code> 返回 <code>price = 0.0</code>（只证明下载不花钱）｜<a href="https://apps.apple.com/cn/app/id6759259780">App Store 页</a> ｜ 核实于 10-21 06:31</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Steam 其余 9 条周促（往期已报） ｜ <span style="color:#6b7280;">最紧一档 10-22 01:00 北京</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>商品</th><th>标价 → 现价</th><th>折扣</th><th>截止（北京时间）</th></tr></thead>
      <tbody>
        <tr><td>Street Fighter 6</td><td>¥198.00 → ¥79.20</td><td>-60%</td><td><span style="color:#c0392b;font-weight:700;">10-22 01:00</span></td></tr>
        <tr><td>霍格沃茨之遗</td><td>¥384.00 → ¥38.40</td><td>-90%</td><td>10-23 01:00</td></tr>
        <tr><td>Red Dead Redemption 2</td><td>¥279.00 → ¥69.75</td><td>-75%</td><td>10-23 01:00</td></tr>
        <tr><td>Grand Theft Auto V 增强版</td><td>¥224.00 → ¥98.56</td><td>-56%</td><td>10-23 01:00</td></tr>
        <tr><td>007 初露锋芒</td><td>¥298.00 → ¥178.80</td><td>-40%</td><td>10-23 01:00</td></tr>
        <tr><td>Warhammer 40,000: 星际战士2</td><td>¥249.00 → ¥62.25</td><td>-75%</td><td>10-25 01:00</td></tr>
        <tr><td>BOMBANANA!</td><td>¥29.00 → ¥17.40</td><td>-40%</td><td>10-24 01:00</td></tr>
        <tr><td>赛博朋克 2077</td><td>¥298.00 → ¥89.40</td><td>-70%</td><td>10-27 02:00</td></tr>
        <tr><td>《赛博朋克 2077：往日之影》</td><td>¥149.00 → ¥89.40</td><td>-40%</td><td>10-27 02:00</td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;">这 9 条本轮被跨天去重命中（同一 appid 往期已报道），所以不进「值得」重复铺陈，但福利本身仍在期内、数字照贴。价格是 06:36 从 <code>featuredcategories?cc=cn</code> 一次读取的快照，全部为官方接口口径。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：<a href="https://store.steampowered.com/">Steam 国区特殊促销</a>｜核实于 10-21 06:36</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">优惠赛道其余来源：中文站转述与分类噪音 ｜ <span style="color:#6b7280;">未回厂商活动页，故不进值得</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>美国主机侦探（idcspy）6 条：2026 年双十一 / 黑五活动汇总（服务器、VPS、主机、云服务器、跨境工具、运维）、ScalaHosting 黑五促销（WordPress 主机 $2.95/月起、云主机最高减免 72%）、HawkHost 新增 AdminBolt VPS（$9/月起，支持多节点与 MCP 接入）、Sorftime 跨境电商分析（附独家折扣），以及 BlueHost 装 CyberPanel、FastMoss 竞店分析两条教程（<strong>不是优惠</strong>，属赛道噪音）。这些全部是中文站转述，没有逐条回厂商官方活动页核对最终价、是否续费同价与截止时间，按「优惠必须有截止时间」这条门槛只能留在观察。</p>
    <p>LowEndBox 这一轮只有 1 条，而且是《Mathematicians Upset About OpenAI's PR Stunt Need a Chill Pill》的吐槽文，被归进 deal 赛道同样是分类噪音——<strong>本轮 LEB 没有可用报价</strong>，这是连续第四天优惠赛道只剩转述。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：<a href="https://www.idcspy.com/">美国主机侦探</a>、<a href="https://lowendbox.com/">LowEndBox</a>｜条数取自 06:31 取数轮，未逐条回源核价｜核实于 10-21 06:31（抓取时刻）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open="open">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">币圈这一轮的四轴：为什么没有 🔥</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p><strong>① 交易所与状态</strong>：Kraken 的 <code>Digital Currency Funding</code> 组件为 <code>degraded_performance</code>（06:36 直读 <code>status.kraken.com/index.json</code> 的组件数组，逐条筛出非 operational 的那一个，不是媒体转述），Coinbase 侧 All Systems Operational。它是「数字货币入金」这一种方式降级，不是充提暂停，也不是交易所整体不可用；而按币圈的门槛，只有<strong>直接影响在用资产可得性</strong>才升 🔥，「你在不在里面挂着资产」这一项雷达没有证据，所以停在观察。Binance 公告 3 条只拿到标题：跨保证金与组合保证金抵押率更新（正文标注 2026-10-23）、USDⓈ-M 永续合约保证金分层调整（2026-10-30）、bStocks 抵押指数价格改为 24/7 动态更新——未按口径回公告正文核对生效细节，只有在用币安合约的人需要自己展开看。</p>
    <p><strong>② 行情与热度</strong>（06:31 快照，来源 CoinGecko / CoinMarketCap / alternative.me）：BTC $83,002（+1.2%）、ETH $2,458.69（+2.1%）、BNB $742.20（+1.6%）、XRP $1.34（+2.5%）、USDT $0.9993；市值榜 24h 异动 ZEC +10.0%、WLD +11.7%、Lighter +11.3%、AERO +11.3%、PYTH +8.4%、Bitway -15.0%；CoinGecko 热搜 Pearl、Quantus、Zcash、AERO、NEAR、Collector Crypt、PENGU、AAVE、ONDO、PEPE；CMC 热搜 BTC、ETH、XRP、NEAR、SOL、PEPE；恐惧贪婪指数 55（Greed）。这些是某一刻的数字，不是信息，一律落在观察、不给 ⭐，也不构成任何操作建议；雷达不连钱包、不签名、不代充代提，产物里不会出现钱包地址、私钥、助记词与带返利参数的邀请链接。</p>
    <p><strong>③ 项目方一手</strong>：Ethereum 博客与 agave 发版记录本轮 0 条（站能到，两天窗口内无新帖，不是故障）。</p>
    <p><strong>④ 媒体转述 39 条</strong>（CoinDesk 12 / The Block 12 / PANews 15）：机构、监管、ETF 一类，本轮没有一条拿到一手原文，按口径不进值得。X 那一轴依旧没有机器可读通道，只能在浏览器桥里用你自己的登录态读主页文本，只读不点——而今天那条桥正好不可用（见下一段），所以本轮 X 侧没有产出。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：<a href="https://status.kraken.com/">Kraken 状态页</a>、<a href="https://www.binance.com/en/support/announcement">Binance 公告中心</a>、<a href="https://www.coingecko.com/en/coins">CoinGecko</a>、<a href="https://alternative.me/crypto/fear-and-greed-index/">恐惧贪婪指数</a>｜行情为 06:31 快照、状态为 06:36 读取｜核实于 10-21 06:36</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">开发资讯里的未核实项与两条需要你自己看一眼的</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>条目</th><th>来源</th><th>本轮判读</th></tr></thead>
      <tbody>
        <tr><td>Google 开源 TorchTPU（PyTorch 原生 TPU 后端）、deepseek-ai/DeepInfer（DeepSeek 推理框架）</td><td>HN 10-20</td><td>06:38 打 GitHub API 双双无返回（疑似限流），只有 HN 标题在手，未读仓库 README 与许可证，故不进值得</td></tr>
        <tr><td>GitHub Trending 6 个库：cloudflare/security-audit-skill、anthropics/knowledge-work-plugins、Graphify-Labs/graphify、msitarzewski/agency-agents、DietrichGebert/ponytail、vllm-project/vllm</td><td>trending</td><td>未逐个读 README 判断它是否真在解决你关心的事；trending 无发布时间戳，不参与两天窗口过滤，榜位本身不是价值</td></tr>
        <tr><td>京东暂停双 11 期间外部安全测试与漏洞收录，未经授权测试按违规处理</td><td>IT之家 10-20 14:17</td><td>与 SRC / 众测路径直接相关，值得你自己去看，但规则原文在京东侧公告，本轮没核到，只算媒体单条转述</td></tr>
        <tr><td>IT之家 25 条里的硬件降价与厂商动态（优派 24" 4K 160Hz 首发 2199 → 1699、小米 Sound Pro 999 → 551、iPhone 18 Pro Max 以旧换新立减 1300 实付 9699 12 期免息）</td><td>IT之家</td><td>电商促销价与「国补后」口径拿不到官方活动页的截止时间，按门槛不进值得；华为鸿蒙装机 9500 万、高通裁员、Netflix 三季报这类属行业动态，不是福利</td></tr>
        <tr><td>v2ex 10 条、Product Hunt 15 条</td><td>v2ex / PH</td><td>社区与新品发布站的常态内容，本轮没有一条满足「已核实 + 有明确额度或价格 + 门槛可接受」</td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;font-size:12.5px;color:#6b7280;">来源：<a href="https://news.ycombinator.com/">HN</a>、<a href="https://github.com/trending">GitHub Trending</a>、<a href="https://www.ithome.com/">IT之家</a>、<a href="https://www.v2ex.com/">v2ex</a>、<a href="https://www.producthunt.com/">Product Hunt</a>｜核实于 10-21 06:31（抓取时刻，未逐条回源）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open="open">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">六个来源本轮 0 条：只有一个是「窗口太窄」，其余都不是故障</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>状态上 25 个来源全绿、<code>errors=0</code>，没有 <code>ERR source=</code> 行，但 0 条的那六个要分开判读，因为它们的成因完全不同：<strong>epic</strong> 是被跨天去重命中——06:38 不带去重单跑 <code>--days 7</code> 拿到 4 条，本批限免仍在架，于是值得段那两条是这次复验写进去的；<strong>ruanyifeng</strong> 同样是去重命中（单跑 <code>--days 2</code> 有 1 条）；<strong>ethblog / creleases</strong> 站能到，只是两天窗口内确实没有新帖；<strong>appinn</strong> 挂着 <code>allow_empty</code>，打印的是 <code>INFO source=appinn empty=本轮无符合条件的新条目（非故障）</code>，业务上本来就可能没货。</p>
    <p>唯一一条要单独说的是 <strong>hf（Hugging Face daily papers）</strong>：昨天那轮它报 <code>URLError</code>、单站 curl 走代理与直连都回 000，今天 06:36 复跑是 <code>--days 30</code> 取回 15 条、<code>--days 2</code> 取回 0 条，论文时间戳落在 10-14 ~ 10-17，同时 <code>curl https://huggingface.co/papers</code> 走代理 200、直连 000。也就是说<strong>这一站的通道今天已经恢复，0 条的真实原因是它的 ts 是论文提交日而不是每日榜单日，两天窗口必然常 0</strong>。建议是把 hf 单独放宽到 <code>--days 7</code>，或者改用 daily-papers 的榜单日期做判据——在此之前它每天挂在 0 条上，会把「这一站到底能不能到」这个问题一直埋着看不出来。</p>
    <p style="font-size:12.5px;color:#6b7280;">通道判据：境内（IT之家、美国主机侦探、v2ex）与境外（HN、lobsters、CoinGecko、CoinDesk、The Block、PANews、Binance、Epic、Hugging Face）两条路同时全绿，所以「代理节点疑似不可用」这一项今天不成立；整轮取数约 50 秒，大头仍是 App Store 那一层逐条回 iTunes 核价。来源：本轮 <code>radar_fetch.py --all --days 2</code> 的 <code>SUMMARY fetched=318 fresh=173 sources=25 errors=0</code>｜核实于 10-21 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这一轮怎么跑出来的：取数 → 验真 → 分级 → 落盘</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p><strong>取数</strong>：<code>radar_fetch.py --all --days 2</code>，25 个来源一次跑完，覆盖五条赛道（含币圈 11 源、iOS 限免 2 源），<code>--seen/--append history.jsonl</code> 做跨天去重；结果 <code>fetched=318 fresh=173 sources=25 errors=0</code>。</p>
    <p><strong>验真</strong>：优惠、限免、额度三类一律回官方接口或官方页复核价格与截止——Epic 回 <code>freeGamesPromotions</code> 并只认 <code>discountPercentage == 0</code>；iOS 认 <code>trackId</code> 回 <code>itunes.apple.com/lookup</code> 核国区现价（不认名字）；Steam 用 <code>appdetails</code> + <code>featuredcategories</code> 交叉核价与核截止。拿不到一手的一律降观察并写明存疑原因，包括 idcspy 的 6 条中文站转述、Binance 的 3 条只有标题的公告、以及 GitHub API 无返回的那两条仓库级消息。</p>
    <p><strong>分级</strong>：🔥 需要立刻处理（距截止 ≤3 小时，或影响你在用的域名 / VPS / 在用 API 免费额度）本轮 0 条；⭐ 值得（已核实、本周内有效、能省钱或直接用于学习）8 条；👀 观察（未核实、门槛高、或本身只是数字）14 组；❌ 过滤的是喊单、目标价、荐币、要连钱包领空投那一类，本轮没有条目落进这一档，因此也不写进正文。币圈的门槛更硬：行情、热搜、情绪指数这类默认只能落在观察，只有直接影响在用资产可得性才升 🔥。</p>
    <p><strong>落盘</strong>：本地存档 <code>~/aigc/info-radar/daily/2026-10-21.md</code>（六段固定结构）→ 本页（雷达三段之一的 GitHub Pages）→ 随当天早间日报邮件投递。雷达三段缺任何一段都不算跑完；邮件不属于这三段，它只是内容投递的那块版面。</p>
    <p style="font-size:12.5px;color:#6b7280;">边界声明：只收集与核实，不注册、不绑卡、不代领券、不下单；iOS 兑换码型限免不转载兑换码，只留频道原帖；币圈不连钱包、不签名、不代充代提、不给买卖建议与目标价。</p>
  </div>
</details>
