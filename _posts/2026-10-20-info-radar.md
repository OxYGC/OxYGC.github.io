---
title: "资讯雷达 2026-10-20｜Epic 限免口径纠错、两款 iOS 限免复验、Let's Encrypt 校验视角时间线"
author: OxYGC
date: 2026-10-20 06:45:00 +0800
permalink: /posts/info-radar-2026-10-20/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, App Store限免, Let's Encrypt, MiniMax, 币圈]
description: "2026-10-20 这一轮 25 个来源取回 316 条、去重后 171 条新，0 个 ERR，留下 7 条值得、14 组观察；本轮最重要的不是新羊毛，而是把 Epic 那两条被误标成限免的折扣游戏按官方页改回来，并顺手纠正昨天稿子里的预告。每条都带核实时间与官方直链。"
---

今早这一轮 25 个来源全绿，取回 316 条、按两天窗口去重后剩 171 条，0 个 ERR。分级结果和昨天一样没有 🔥：最近一档截止是 Epic 本批限免的 10-22 23:00（北京时间，接口口径），距今约 40 小时，够得着但不紧急；优惠价格这一类今天有货，却被内容门槛拦在门外——LowEndBox 主推的 FlipperHost 2GB VPS 年付 $29.99，回厂商下单页能核到价格与规格，但厂商和 LowEndBox 两边都没写活动截止时间，按「优惠必须有截止时间」这条口径只能进观察，不进值得，这是本轮唯一一条「东西是真的、却卡在门槛」的条目。这一篇真正要交代的是**一次纠错**：取数层把 Epic 的《纪念碑谷》与《Eternal Threads》当成限免抓了回来，昨天的雷达稿顺着它写了「今晚 23:00 开领免费」；今早直接打开 Epic 中文商店页，当前免费的两款仍然是《Bad Cheese》和《Agent A - 伪装游戏》，而《纪念碑谷》标价 ¥33.00→¥11.55、《Eternal Threads》¥62.00→¥12.40——是打折不是免费。根因在接口字段上：`discountPercentage` 这个数是**最终支付比例**，`0` 才是免费，`20` / `35` 分别表示付两成、付三成半，昨天把它当成了「减价幅度」来读。所以下面这一篇的正确打开方式是：要领的还是那两款老面孔，新免费的那一批要到 10-22 23:00 才轮到《Sker Ritual》和《Home》。另外还有一处时点冲突要摊开说：Epic 接口把本批截止写成 `endDate = 2026-10-22T15:00:00Z`，换算北京时间是 10-22 23:00，而同一时刻渲染出的中文商店页写着「10月23日 00:00 截止」，两边差一小时；两个都是官方来源，我不替 Epic 把这个差圆过去，按早的那条动手最稳。

<div style="border:1px solid #e8ebef;border-radius:10px;background:#fafbfc;padding:16px 20px 6px;margin-bottom:20px;">
  <p style="font-weight:700;font-size:16px;color:#1f2329;margin:0 0 10px;">四条要记的时点，都没有今晚关窗</p>
  <table>
    <thead><tr><th>截止 / 时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
    <tbody>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-22 23:00（剩约 40 小时）</span><br><span style="font-size:12.5px;color:#6b7280;">接口口径；商店页渲染成 10-23 00:00</span></td><td>Epic 本批限免《Agent A - 伪装游戏》《Bad Cheese》</td><td>0 元领取入库</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-22 23:00 开领</span>（至 10-29 23:00）</td><td>Epic 下一批《Sker Ritual》《Home - A Unique Horror Adventure》</td><td>0 元</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td>Apple 不公布限免截止时间</td><td>App Store 国区《Waky Alarm 闹钟》《M3U8 Spark》</td><td>0 元下载</td><td><a href="https://apps.apple.com/cn/app/id6748906275">Waky Alarm 的 App Store 页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-27 staging、11-10 生产</span></td><td>Let's Encrypt 域名校验新增两个远程视角</td><td>免费（CA 侧变更）</td><td><a href="https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166">LE 官方公告帖</a></td></tr>
    </tbody>
  </table>
  <p style="font-size:13.5px;color:#6b7280;margin:0 0 10px;">另有开发 / AI 动态 2 条（MiniMax M3.1 Flash、Let's Encrypt）、1 条真优惠被门槛挡回观察；未核实或门槛高的 14 组放在最后一节。以下全部默认收起，点开看细节。</p>
</div>

## 值得看（7）

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">点击任意一条展开：价值判断、完整价格、核实到的接口字段都在里面。雷达只负责把消息带到——领取、下单、注册、绑定支付方式都由你自己完成。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Agent A - 伪装游戏 ｜ <span style="color:#1a7f37;">0 元</span> ｜ <span style="color:#c0392b;">10-22 23:00（接口口径）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>潜行解谜口碑款，价值不在「这周得玩完」，而在<strong>领取即永久入库</strong>。这一档已经在架几天，昨天与今天都回官方页复核过，不是旧闻重推。</p>
    <p>截止口径要单独交代：接口 <code>endDate = 2026-10-22T15:00:00Z</code> 换算是北京时间 10-22 23:00，而同一时刻的中文商店页把截止渲染成「10月23日 00:00」（本机时区 +0800）。两处官方来源差一小时，条目按早的那条算，也就是剩约 40 小时。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口字段 <code>promotionalOffers</code> 命中 <code>startDate = 2026-10-15T15:00Z</code> / <code>endDate = 2026-10-22T15:00Z</code> / <code>discountSetting.discountPercentage = 0</code>，商店页文案「当前免费，10月23日00:00截止」｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-20 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Bad Cheese ｜ <span style="color:#1a7f37;">0 元</span> ｜ <span style="color:#c0392b;">10-22 23:00（接口口径）</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>与上一条同一批、同一截止，Epic 每周固定同时放两款。恶搞 / 派对向小品，合不合口味另说，0 元入库的机会成本几乎为零。</p>
    <p style="font-size:12.5px;color:#6b7280;">同接口字段口径：<code>start = 2026-10-15T15:00Z</code>、<code>end = 2026-10-22T15:00Z</code>、<code>discountPercentage = 0</code>；商店页并列显示「当前免费」｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-20 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 下一批限免预告：Sker Ritual + Home ｜ <span style="color:#1a7f37;">0 元</span> ｜ <span style="color:#c0392b;">10-22 23:00 开领，至 10-29 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这两款挂在接口的 <code>promotionalOffers</code> 起始时间上，正好接在本批截止那一刻，商店页把它们列在「即将推出」：<strong>《Sker Ritual》</strong>是合作生存射击，<strong>《Home - A Unique Horror Adventure》</strong>是恐怖解谜叙事。放进来是因为时点确定，不是催促——本批没领完之前不用管它。</p>
    <p>顺带把取数层的坑说清楚：昨天的稿子把下一批认成了《纪念碑谷》与《Eternal Threads》，那是误读 <code>discountPercentage</code>。真正的下一批只有这两支，另外两支是折扣商品，见「观察」段第一条。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口字段 <code>start = 2026-10-22T15:00Z</code>、<code>end = 2026-10-29T15:00Z</code>、<code>discountPercentage = 0</code>；页面文案「免费 10月23日 - 10月30日」（同一次一小时渲染差的另一处体现）｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-20 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Waky Alarm - 不再为赖床懊恼 - 闹钟 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>闹钟类小工具，TossTF 在 10-19 播报的「本体限免」。今日按播报正文里的 <code>trackId</code> 回 iTunes 复验，国区现价确实是免费。</p>
    <p>两条边界照旧要写：Apple 没有官方限免接口、也<strong>不公布促销结束时间</strong>，所以这一档没有截止时间可写；而 lookup 接口分不出「本就免费」与「促销中」，因此只能写「下载不花钱」，不能写「限免仍在」。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>itunes.apple.com/lookup?id=6748906275&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「Waky Alarm - 不再为赖床懊恼 - 闹钟」、发行商 Another Door Inc.、最低系统 26.0（认 id 不认名字，国区会改名）｜<a href="https://apps.apple.com/cn/app/id6748906275">App Store 页</a> ｜ 核实于 10-20 06:31</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：M3U8 Spark 网页视频嗅探 &amp; 在线播放 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>网页视频流（m3u8 一类）嗅探 + 播放工具，同批播报的本体限免，今日复验国区现价为免费。对做抓取、看回放链路的人来说是个顺手能用的东西，比闹钟那款更贴工程场景。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=6775141985&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「M3U8 Spark: 网页视频嗅探&amp;在线播放」、最低系统 15.0｜<a href="https://apps.apple.com/cn/app/id6775141985">App Store 页</a> ｜ 核实于 10-20 06:31</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">MiniMax M3.1 Flash：官方称推理快约 3 倍、成本降 70% ｜ <span style="color:#1a7f37;">发布即开放</span> ｜ <span style="color:#6b7280;">官方博客 2026-10-19</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这一条对每天在跑智能体的人有实际意义：官方把它定位成新一代 Flash 档，主打 agentic 任务、编码、Computer Use 与网络安全四类，并写明「在线推理快近三倍、使用成本下降 70%」。省的是调用层开销，不是模型能力上限，所以它的正确用法是拿自己的真实任务量一遍，而不是看跑分。</p>
    <p>顺手记一个可交叉的细节：官方 blog 里提到此前那个处理过 200 万亿以上 token 的匿名模型 Space Bunny 🐰 是 M3.1 Flash 的早期版本——这条能解释为什么榜单上突然冒出一个陌生 id。PANews 的中文转述给的也是同一个「成本降 70%」口径，数字与一手博客一致。</p>
    <p style="font-size:12.5px;color:#6b7280;">官方博客页面返回 200、正文命中 <code>MiniMax M3.1 Flash</code> 与 <code>reducing usage costs by 70%</code>，发布日期 2026-10-19｜<a href="https://www.minimax.io/blog/minimax-m31f">MiniMax 官方博客</a> ｜ 核实于 10-20 06:43</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Let's Encrypt 域名校验新增两个远程视角 ｜ <span style="color:#1a7f37;">免费（CA 侧变更）</span> ｜ <span style="color:#c0392b;">staging 10-27、生产 11-10</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>驱动力是 CA/B Forum 的 Baseline Requirements 3.2.2.9：<strong>2026-12-15 起，CA 必须用至少 5 个远程网络视角做 Multi-Perspective Issuance Corroboration</strong>，且取得佐证的视角要横跨至少两个不同的区域互联网注册机构（RIR）。Let's Encrypt 原本已有 4 个远程视角，这次再加 2 个，于是一次域名验证的总请求数从 5 次（1 主 + 4 远端）变成 7 次（1 主 + 6 远端）。</p>
    <p>官方原话是「We expect little to no impact to users」，验证逻辑本身没变：主服务器加上足够多远端视角收到正确响应才算通过。真正要留意的两类人是自建校验脚本 / 私有 CA 的，以及把域名解析做成分线路、某些区域解析结果不同的——多视角只会让这类不一致更早暴露出来。时间线记两个点就行：10-27 起在 staging 生效，11-10 上生产。</p>
    <p style="font-size:12.5px;color:#6b7280;">Discourse topic JSON 的 <code>created_at = 2026-10-15T14:14:49Z</code>，正文命中 <code>seven total validation requests</code>、<code>staging on Tuesday, October 27th, 2026</code>、<code>production rollout on Tuesday, November 10th, 2026</code>｜<a href="https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166">LE 官方公告帖</a> ｜ 核实于 10-20 06:42</p>
  </div>
</details>

## 观察（14 组）、币圈那一轮与方法

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">这一节收的是「没核实到一手」「门槛要你自己跨」「本身只是数字」，以及<strong>被内容门槛挡回去的条目</strong>。它们不构成价值，但可能决定你要不要自己再去确认一次。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open="open">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">本轮的更正：《纪念碑谷》《Eternal Threads》是打折，不是限免</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>商品</th><th>标价 → 现价</th><th>实际支付比例</th><th>档期（UTC）</th></tr></thead>
      <tbody>
        <tr><td>Eternal Threads</td><td>¥62.00 → ¥12.40</td><td><code>discountPercentage = 20</code>（付两成）</td><td>2026-10-19T15:00Z ~ 2026-11-02T16:00Z</td></tr>
        <tr><td>纪念碑谷（Monument Valley）</td><td>¥33.00 → ¥11.55</td><td><code>discountPercentage = 35</code>（付三成半）</td><td>同上</td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;">判据就一句：<strong><code>discountPercentage</code> 是最终要付的百分比，<code>0</code> 才等于免费</strong>。取数层这次把 20 / 35 当成「减 20% / 减 35%」来分类，于是把两支折扣商品送进了限免，昨天的稿子跟着错了一天——今天已在稿子层面改回，并建议脚本把「限免」的判据收紧成 <code>discountPercentage == 0</code>，其余一律进折扣。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：Epic <code>freeGamesPromotions</code> 接口 + 中文商店页（页面「当前免费」栏里只有《Bad Cheese》《Agent A》）｜核实于 10-20 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">优惠价格这一轮：FlipperHost 2GB VPS $29.99/年 ｜ <span style="color:#6b7280;">卡在「必须有截止时间」</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>档位</th><th>规格</th><th>价格</th></tr></thead>
      <tbody>
        <tr><td>2GB KVM</td><td>2 vCPU / 35GB SSD / 5TB 月流量 / 1Gbps / 1 IPv4，洛杉矶或纽约</td><td>$29.99/年</td></tr>
        <tr><td>4GB KVM</td><td>3 vCPU / 60GB SSD / 8TB 月流量</td><td>$59.99/年（$5.99/月）</td></tr>
        <tr><td>6GB KVM</td><td>5 vCPU / 100GB SSD / 12TB 月流量</td><td>$79.99/年（$7.99/月）</td></tr>
        <tr><td>8GB KVM</td><td>7 vCPU / 150GB SSD / 20TB 月流量</td><td>$99.99/年（$9.99/月）</td></tr>
      </tbody>
    </table>
    <p style="margin-top:10px;">规格与价格都回厂商自己的下单页核到了（页面上确实写着 ($29.99/Year) 与 ORDER NOW，另附 30 天退款），付款方式里 Alipay、UnionPay 都在。<strong>但厂商页和 LowEndBox 原文都没写活动截止时间</strong>，按发布门槛「优惠必须有截止时间」这条，它进不了「值得」，只能停在观察——我不为了凑一条值得而编一个日期出来。</p>
    <p style="font-size:12.5px;color:#6b7280;">来源：<a href="https://www.flipperhost.com/billing/store/vps-promotions/flipper-kvm2gb">FlipperHost 下单页</a>、<a href="https://lowendbox.com/blog/get-cheap-hosting-in-la-ny-or-atlanta-from-flipperhost-only-29-99-year-for-a-2gb-vps/">LowEndBox 原文（2026-10-19 07:00）</a> ｜ 核实于 10-20 06:44</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">观察清单：另外 12 组，以及为什么它们不进值得</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>条目</th><th>存疑原因</th></tr></thead>
      <tbody>
        <tr><td>Trypa（id 1666429734）播报「本体限免」</td><td>iTunes 国区实测现价 ¥88.00，按 iOS 口径判「限免已失效或已改价」</td></tr>
        <tr><td>Photo Cleaner: Swypic 兑换码型限免</td><td>兑换码一律不转载、只留频道原帖由你自己取；现价未走 iTunes 核价</td></tr>
        <tr><td>美国主机侦探 6 条促销（Hostinger 黑五低至 $2.24/月、CloudCone 奥克兰 4核16GB $80.81/月起、宝塔企业版 2399 元/3 年、HostEase $35.64/年 + $100 API 抵用券、HHost 年付 8 折、LinkFox 接入 WorkBuddy）</td><td>全部是中文站转述，本轮没逐条回厂商官方活动页核价与截止</td></tr>
        <tr><td>微信公众号「小说改编短剧」激励活动（作者与承制方各 5% 额外收益、上不封顶）</td><td>只有 IT之家转述，活动规则页在公众号后台，而本机后台此刻读到「请重新登录」，核不到原文</td></tr>
        <tr><td>v2ex「学生优惠 $8.99 开 2 年半 Google AI Pro + YouTube Premium + 5TB」（79 回）</td><td>二手转述，且涉及学生优惠适用资格，不核实也不推荐</td></tr>
        <tr><td>v2ex FinderNav 送 80 个激活码（106 回）</td><td>未核实码是否仍有剩余、有效期与领取门槛</td></tr>
        <tr><td>Kraken 服务状态 Partially Degraded（Coinbase 全部正常）</td><td>06:31 状态页快照；影响面取决于你是否在用 Kraken，未确认关联，只作背景</td></tr>
        <tr><td>币圈行情快照：BTC ≈ $82,089、ETH ≈ $2,412、SOL ≈ $105；24h 异动 Bitway -13.8% / Worldcoin +10.7% / Pump.fun +9.9% / Venice Token +8.5%；恐惧贪婪 59（Greed）</td><td>行情与情绪指数按口径一律只作快照，涨跌本身不构成价值，也不构成操作建议</td></tr>
        <tr><td>Binance 公告 3 条（Binance AI Pro / 经 bStocks 派发 DELL 现金股息 / Square 的 Write to Earn 升级）</td><td>只取到公告目录标题，未回正文核对生效时间与合约地址</td></tr>
        <tr><td>Coinbase 将 AXIS、PEARL、STABLE 加入上币路线图</td><td>仅 PANews 中文转述，未回交易所公告原文核对</td></tr>
        <tr><td>GitHub Trending：headroom（76,198 star，压缩 tool 输出 / RAG chunk，自称省 20% token）、Kronos（41,602 star，金融市场语言基础模型）、os-taxonomy（6,083 star，无描述）</td><td>未逐个读 README 判断是否真在解决你关心的事，star 数与「省 20%」都是仓库自述</td></tr>
        <tr><td>媒体转述 39 条（CoinDesk 12 / The Block 12 / PANews 15：JPMorgan 把 JPM Coin 扩展到 Ethereum、贝莱德提交带下行保护的比特币 ETF、Mastercard 稳定币风控工具、Visa × Mesh、Circle 在 Solana 12 分钟铸 5 亿枚 USDC 等）</td><td>监管与机构类拿不到一手原文的不进值得；其中「Strategy / Metaplanet 增持、巨鲸移币」这类纯行情叙述直接过滤</td></tr>
      </tbody>
    </table>
    <p style="font-size:12.5px;color:#6b7280;margin-top:10px;">另有两条按旧闻重推处理、不写进任何段落：Steam 区 10 款折扣（《赛博朋克 2077》¥298→¥89.40 至 10-26、《Red Dead Redemption 2》¥279→¥69.75 至 10-22 等）往期已报；阮一峰周刊第 415 期同样已在往期覆盖。</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">币圈那一轮：四轴怎么取，以及为什么只有状态页值得单列</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>币圈这一轮跑了 11 个机器可读源，按四条轴分：<strong>交易所动态</strong>（Binance 公告三个目录、Coinbase / Kraken 的 Statuspage）、<strong>行情与热度</strong>（CoinGecko 市值榜与异动榜、CoinGecko / CoinMarketCap 热搜、恐惧贪婪指数）、<strong>项目方一手</strong>（Ethereum 博客、go-ethereum 与 Agave 的 GitHub releases）、<strong>媒体转述</strong>（CoinDesk、The Block、PANews）。今天项目方那一轴窗口内是空的：ethblog 6 条全在两天之外（周更节奏），creleases 4 条往期已报。</p>
    <p>只有服务状态那一格适合单独列出来当线索：Coinbase <code>All Systems Operational</code>、Kraken <code>Partially Degraded Service</code>（06:31 快照）。它是「状态」而不是「消息」——你没在用 Kraken，这一条就只是背景；在用，才轮到你去核对充提是否受影响。X 那一轴照旧没有机器可读通道（syndication 429、nitter 410 / 连不上、threadreader 要预订阅），本轮没有走登录窗口，所以官方账号的一手表态这一格是空的，记为「本轮未取」。</p>
    <p style="font-size:12.5px;color:#6b7280;">边界：不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价；产物里不出现钱包地址、私钥、助记词与带 <code>?ref=</code> 的邀请返利链接。喊单、目标价、荐币、要连钱包才能领的空投，一律过滤且不写进任何段落。</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这一轮是怎么跑出来的：取数、验真、分级、门槛，四步口径</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>来源</th><th>本轮新增条数</th><th>状态</th></tr></thead>
      <tbody>
        <tr><td>IT之家</td><td>25</td><td>正常</td></tr>
        <tr><td>Hacker News</td><td>24</td><td>正常</td></tr>
        <tr><td>lobsters</td><td>16</td><td>正常</td></tr>
        <tr><td>Product Hunt</td><td>15</td><td>正常</td></tr>
        <tr><td>PANews</td><td>15</td><td>正常</td></tr>
        <tr><td>CoinDesk / The Block</td><td>12 / 12</td><td>正常</td></tr>
        <tr><td>v2ex</td><td>10</td><td>正常</td></tr>
        <tr><td>CoinGecko 热搜 / 异动榜</td><td>10 / 5</td><td>正常（快照时间 06:31）</td></tr>
        <tr><td>美国主机侦探</td><td>6</td><td>正常，但全为转述</td></tr>
        <tr><td>CoinMarketCap 热搜</td><td>6</td><td>正常</td></tr>
        <tr><td>App Store 限免（TossTF + iTunes 两层）</td><td>4</td><td>正常，2 条核到免费、1 条核到 ¥88、1 条兑换码未核价</td></tr>
        <tr><td>Binance 公告</td><td>3</td><td>正常（仅标题层）</td></tr>
        <tr><td>GitHub Trending</td><td>3</td><td>正常</td></tr>
        <tr><td>Epic 商店</td><td>2</td><td><span style="color:#c0392b;">解析口径异常</span>：把 20% / 35% 折扣当成限免，已按官方页更正并在观察段单列</td></tr>
        <tr><td>交易所状态页 / 恐惧贪婪指数</td><td>1 / 1</td><td>正常</td></tr>
        <tr><td>LowEndBox</td><td>1</td><td>正常（官方页无截止时间）</td></tr>
        <tr><td>appinn</td><td>0</td><td>正常，本轮没有限免帖</td></tr>
        <tr><td>Steam / 阮一峰周刊</td><td>0</td><td>正常，命中往期已报道的去重</td></tr>
        <tr><td>ethblog / creleases</td><td>0</td><td>正常，两天窗口内无新条目</td></tr>
        <tr><td><span style="color:#c0392b;">HF daily papers</span></td><td>0</td><td><span style="color:#c0392b;">黄</span>：<code>--all</code> 那一轮无 ERR；06:47 单跑复测 <code>ERR source=hf URLError</code>，<code>curl huggingface.co/papers</code> 走代理与直连都回 000。同一时刻 Epic / MiniMax / Let's Encrypt / LowEndBox 均 200，所以是这一站到不了，不是本机代理整条挂</td></tr>
      </tbody>
    </table>
    <p style="margin-top:12px;">四步口径没变：<strong>取数</strong>一轮 25 个来源、两天时间窗、跨天按 id 去重（<code>fetched=316 fresh=171 errors=0</code>）；<strong>验真</strong>是价格与截止时间必须回官方页二次确认，App Store 那一层反过来——Apple 没有官方限免接口，所以认 <code>trackId</code> 回 <code>itunes.apple.com/lookup</code> 核国区现价，不认名字（国区会改名，按名字会认错 app）；<strong>分级</strong>按 🔥 紧急 / ⭐ 值得 / 👀 观察 / ❌ 过滤四档，宁严勿松；<strong>门槛</strong>是发布前的自查：值得段每一条都要有核实时间与直链，优惠与限免必须有截止时间，官方确实不给的（App Store 限免是唯一一例）就明写「Apple 不公布限免截止时间」顶掉那一栏，未核实的只能待在观察。</p>
    <p style="font-size:12.5px;color:#6b7280;">边界声明：雷达只收集、验证、报告，不代注册、不绑卡、不代领券、不下单，也不代为兑换任何限免；所有兑现动作由你自己完成。</p>
  </div>
</details>
