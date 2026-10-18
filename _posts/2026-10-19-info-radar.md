---
title: "资讯雷达 2026-10-19｜Epic 周免最后三天、DeepSeek 搜索接口 11 月起按次计费、三款 iOS 限免复验"
author: OxYGC
date: 2026-10-19 06:40:00 +0800
permalink: /posts/info-radar-2026-10-19/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, App Store限免, 免费额度, DeepSeek, 币圈]
description: "2026-10-19 这一轮 25 个来源取回 312 条、去重后 140 条新，0 个 ERR，留下 10 条值得看、16 组只作观察；本轮唯一会影响既有自动化成本的一条是 DeepSeek 官方写明 Search / Fetch 接口 11 月 1 日起按次计费。每条都带核实时间与官方直链。"
---

今早这一轮 25 个来源全绿，取回 312 条、按两天窗口去重后剩 140 条，0 个 ERR。分级结果仍然是没有 🔥：最近一档截止是 Epic 周免的 10-22 23:00（北京时间），距今 3 天 16 小时，且没有任何一条命中在用的域名或 VPS。但 Epic 那一轮翻出了一个具体时点——接口里《纪念碑谷》与《Eternal Threads》的档期写的是 `startDate = 2026-10-19T15:00:00Z`，换算过来就是**今晚 23:00 开领**，这是本条目里唯一一个「今天就要动手」的东西。优惠价格这一类连续第二天整类删掉——窗口里唯一的 colocation 报价，回厂商官网还是那个跳转 `/lander` 的停放页，价格与截止都核不到。真正值得单独记一笔的是 DeepSeek 的文档页：价格表已经写上 Search、Fetch 各 `Per 1,000 successful requests $0.75`，同时明写这些服务端工具调用「当前免费、2026-11-01 00:00（北京时间）起按次计费」，并且点名 DeepSeek Harness、Claude Code、Codex 走的就是这两个接口——也就是说，如果你的 Agent 链路里已经在用它们的内置搜索，成本拐点在两周零十三天之后。

<div style="border:1px solid #e8ebef;border-radius:10px;background:#fafbfc;padding:16px 20px 6px;margin-bottom:20px;">
  <p style="font-weight:700;font-size:16px;color:#1f2329;margin:0 0 10px;">四条要记的时点，都没有今晚关窗</p>
  <table>
    <thead><tr><th>截止 / 时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
    <tbody>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-22 23:00（剩 3 天 16 小时）</span></td><td>Epic 本批周免《Bad Cheese》《Agent A - 伪装游戏》</td><td>0 元领取入库（原价 ¥40.00 / ¥62.00）</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">今晚 23:00 开领</span>（至 11-03 00:00）</td><td>Epic 下一批《纪念碑谷》《Eternal Threads》</td><td>0 元（当前标价 ¥33.00 / ¥62.00）</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td><span style="color:#c0392b;font-weight:700;">11-01 00:00 起按次计费</span></td><td>DeepSeek Search / Fetch 接口的免费窗口</td><td>现在 0 元，之后 $0.75 / 千次成功请求</td><td><a href="https://api-docs.deepseek.com/guides/search/">DeepSeek 官方文档</a></td></tr>
      <tr><td>Apple 不公布限免截止时间</td><td>App Store 国区《Notea便利贴》《即见 Near》《Lumori》</td><td>0 元下载</td><td><a href="https://apps.apple.com/cn/app/id6814895879">Notea 的 App Store 页</a></td></tr>
    </tbody>
  </table>
  <p style="font-size:13.5px;color:#6b7280;margin:0 0 10px;">另有免费额度 1 条（OpenCode Zen）、开发 / AI 动态 2 条、行情与安全转述若干；未核实或门槛高的 16 组放在最后一节。以下全部默认收起，点开看细节。</p>
</div>

## 值得看（10）

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">点击任意一条展开：价值判断、完整价格、核实到的接口字段都在里面。雷达只负责把消息带到——领取、下单、注册、绑定支付方式都由你自己完成。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Bad Cheese ｜ <span style="color:#1a7f37;">0 元（原价 ¥40.00）</span> ｜ <span style="color:#c0392b;">10-22 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>解谜 / 恶搞向小品，本周两连发里的第一款。这一档的价值不在于游戏本身合不合口味，而在于<strong>领取即入库</strong>——不需要在截止前玩完。</p>
    <p>前两天已报道过同一批，今日回 Epic 自家促销接口复核仍在架、<code>discountPrice</code> 依旧是 0，所以按「仍在期内」保留，不当作旧闻重推。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口字段 <code>endDate = 2026-10-22T15:00:00.000Z</code>（即北京时间 23:00）、<code>originalPrice = 4000</code> / <code>discountPrice = 0</code> / <code>currencyCode = CNY</code>，页面渲染成 ¥40.00 → 0｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-19 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Agent A - 伪装游戏 ｜ <span style="color:#1a7f37;">0 元（原价 ¥62.00）</span> ｜ <span style="color:#c0392b;">10-22 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>潜行解谜，与上一条同批、同截止。口碑款，原价档位比 Bad Cheese 高一档。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口字段 <code>endDate = 2026-10-22T15:00:00.000Z</code>、<code>originalPrice = 6200</code> / <code>discountPrice = 0</code>（CNY）｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-19 06:38</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 下一批限免：纪念碑谷 + Eternal Threads ｜ <span style="color:#1a7f37;">0 元（标价 ¥33.00 / ¥62.00）</span> ｜ <span style="color:#c0392b;">今晚 23:00 开领，至 11-03 00:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这一条是本轮唯一「今天就要动手」的：接口里两款都挂在 <code>upcomingPromotionalOffers</code> 下，档期起点 <code>startDate = 2026-10-19T15:00:00Z</code>，换成北京时间就是<strong>今晚 23:00 开始可以领</strong>，到 <code>2026-11-02T16:00:00Z</code>（北京时间 11-03 00:00）结束。纪念碑谷是经典解谜，¥33.00 那一档；Eternal Threads 是叙事推理向，标价 ¥62.00。</p>
    <p>再往后一档已经一并读到：《Sker Ritual》（标价 ¥78.00）与《Home - A Unique Horror Adventure》（¥15.00）同档期 10-22 23:00 开领、10-29 23:00 结束——正好接在本批周免截止的那一刻。</p>
    <p style="font-size:12.5px;color:#6b7280;">同一接口字段口径：<code>start = 2026-10-19T15:00:00Z</code>、<code>end = 2026-11-02T16:00:00Z</code>；当前（06:47）还不能领，<strong>23:00 之后才算数</strong>｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-19 06:47</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Notea便利贴 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>桌面便利贴 / 待办类小工具，TossTF 在 10-17 播报的「本体限免」。今日回 iTunes 复验，国区现价仍是免费。</p>
    <p>要说清楚的边界：Apple 没有官方限免接口，也<strong>不公布促销结束时间</strong>，所以这一档没有截止时间可写；而 lookup 接口分不出「本就免费」与「促销中」，因此只能写「下载不花钱」，不能写「限免仍在」。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>itunes.apple.com/lookup?id=6814895879&amp;country=cn</code> 返回 <code>price = 0.0</code>、<code>formattedPrice = 免费</code>、商店名「Notea便利贴」、最低系统 15.0（认 id 不认名字，国区会改名）｜<a href="https://apps.apple.com/cn/app/id6814895879">App Store 页</a> ｜ 核实于 10-19 06:39</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：即见 Near · 待办提醒与行动卡 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>待办 / 提醒类，走「行动卡」这个形态，TossTF 10-16 播报的本体限免，今日复验现价仍为 0。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=6816675193&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「即见 Near · 待办提醒与行动卡」、最低系统 16.2｜<a href="https://apps.apple.com/cn/app/id6816675193">App Store 页</a> ｜ 核实于 10-19 06:39</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Lumori 账单追踪与提醒 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>账单 / 订阅到期追踪，TossTF 10-15 播报的本体限免。这一款和「域名挂价、订阅续费」那条线是同一类痛点，值得顺手看一眼。</p>
    <p>对照着看一个反例：同批播报的 KoiFiles 在 10-14 被标「本体限免」，但 iTunes 国区实测卖 ¥8.00——不做核价就会误报，所以核到现价非 0 的一律判「限免已失效或已改价」，不进值得。</p>
    <p style="font-size:12.5px;color:#6b7280;"><code>lookup?id=6797824934&amp;country=cn</code> 返回 <code>price = 0.0</code>、商店名「Lumori：账单追踪与提醒」、最低系统 17.0｜<a href="https://apps.apple.com/cn/app/id6797824934">App Store 页</a> ｜ 核实于 10-19 06:39</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">DeepSeek Search / Fetch：现在免费，11-01 00:00 起 $0.75 / 千次 ｜ <span style="color:#1a7f37;">当前 0 元</span> ｜ <span style="color:#c0392b;">11-01 00:00 起计费</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>官方文档的价格表已经写上两行：<code>Search — Per 1,000 successful requests — $0.75</code>、<code>Fetch — Per 1,000 successful requests — $0.75</code>，紧接着说明「这些调用目前不收费，按次计费从 2026 年 11 月 1 日 00:00（北京时间）开始」，并且点名：<strong>当你通过 DeepSeek Harness、Claude Code 或 Codex 使用 DeepSeek API 时，服务端工具调用已经在打 Search 与 Fetch 这两个接口</strong>。</p>
    <p>计费口径要注意两处：按成功请求数计，不按 token、也不按返回条数；只有返回 HTTP 200 且有产出的请求才计费，正常搜索无命中返回空数组不算。所以真正要做的决定是在 11-01 之前，把「要不要在自己的 Agent 里继续开着内置 search / fetch」这件事定下来——按次付，还是关掉换别的搜索源。</p>
    <p style="font-size:12.5px;color:#6b7280;">页面原文命中 <code>$0.75</code>、<code>per-request billing starts at 00:00 Beijing time on November 1, 2026</code>、<code>A request is billable only when it returns HTTP 200</code>｜<a href="https://api-docs.deepseek.com/guides/search/">DeepSeek 官方文档</a> ｜ 核实于 10-19 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">OpenCode Zen 的免费模型档（本轮读到十三个 <code>-free</code> id） ｜ <span style="color:#1a7f37;">0 元档</span> ｜ <span style="color:#6b7280;">官方页未标结束时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>官方模型列表里带 <code>-free</code> 后缀的一档可以在终端 / IDE 直接切换。今日在页面源码里精确匹配到十三个 id：<code>beam-free</code>、<code>deepseek-v4.1-flash-free</code>、<code>exo-free</code>、<code>glm-5.3-flash-free</code>、<code>jev-1.13-free</code>、<code>ll-alpha-free</code>、<code>longcat-2.5-preview-free</code>、<code>mimo-v2.5-free</code>、<code>mimo-v2.6-flash-free</code>、<code>nemotron-3-ultra-free</code>、<code>nemotron-3.5-lightning-free</code>、<code>nemotron-3.5-super-vl-free</code>、<code>space-bunny-free</code>。省的是模型调用这一层开销，门槛是得换成 OpenCode 这条客户端链路。</p>
    <p>一条实操注记：<code>opencode.ai/docs/zen/</code> 现在会 302 跳到 <code>/v2/docs/console/models/</code>，文档已经迁到 v2 路径；不带 <code>-L</code> 直接 curl 会拿到 0 字节，看起来像源挂了，其实是要跟转。</p>
    <p style="font-size:12.5px;color:#6b7280;">跟转后 200、页面 55,900 字节，同页还并列 <code>deepseek-v4.1-flash</code> 与 <code>deepseek-v4-pro</code> 两个付费档｜<a href="https://opencode.ai/docs/zen/">OpenCode 模型页</a> ｜ 核实于 10-19 06:42</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Hybrid Reasoning Agents（arXiv 2610.18861） ｜ <span style="color:#1a7f37;">免费论文</span> ｜ <span style="color:#6b7280;">10-13 提交</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>核心想法是让 Agent 自己决定「什么时候在隐空间里想、什么时候落地成文本行动」，标题里的 HybridAgent 在 3 个模型规模、11 个基准（含数学与工具调用）上做评测。它对着的是当下很实际的一个矛盾：长思考链的 token 开销，与纯文本推理的可控性之间的取舍。HN 83 分 / 35 评。</p>
    <p style="font-size:12.5px;color:#6b7280;">摘要页返回 200、43,236 字节，作者列表含 Jiaru Zou、Pan Lu、James Zou，<code>Submitted on 13 Oct 2026</code>，Subjects 为 cs.CL / cs.AI / cs.LG｜<a href="https://arxiv.org/abs/2610.18861">arXiv 摘要页</a> ｜ 核实于 10-19 06:44</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Java sealed classes 与穷尽模式匹配 ｜ <span style="color:#1a7f37;">免费文章</span> ｜ <span style="color:#6b7280;">原文 2026-04-24，HN 本轮重推</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>把 sealed 类型和 <code>switch</code> 穷尽性检查之间的关系讲透——这正是 Java 面经那条线上「编译器怎么帮你兜住漏分支」的可引素材。HN 120 分 / 96 评（10-18 14:47 上热）。</p>
    <p>诚实标注：<strong>原文发布于 2026-04-24，不是本周新文</strong>，本轮是被 HN 重新推上热度才被抓到；放进去的理由是它对写作选题有直接用途，而不是因为它新。</p>
    <p style="font-size:12.5px;color:#6b7280;">URL 返回 200、123,348 字节，正文命中 sealed 关键字｜<a href="https://neilmadden.blog/2026-04-24/java-sealed-classes-and-exhaustive-pattern-matching/">原文</a> ｜ 核实于 10-19 06:43</p>
  </div>
</details>

## 观察（16 组）、币圈那一轮与方法

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">这一节收的是「没核实到一手」「门槛要你自己跨」「或者本身只是数字」的条目。它们不构成价值，但可能决定你要不要自己再去确认一次。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open>
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">观察清单：16 组，逐条写明存疑原因</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>条目</th><th>为什么只在观察</th></tr></thead>
      <tbody>
        <tr><td>Kraken <code>Partially Degraded Service</code>，Coinbase <code>All Systems Operational</code>（06:34 快照，Statuspage 原文）</td><td>是否要紧取决于你在不在里面持有资产或挂着充提，雷达没有这项证据；不做任何链上操作</td></tr>
        <tr><td>TheBlock《Cysic 攻击者铸币并转移约 7xx 万美元后，官方暂停桥》</td><td>安全事件形态，但只有媒体转述，未拿到项目方 advisory / 官方博客 / 交易所公告三方之一，按口径降级</td></tr>
        <tr><td>PANews《Qubic 披露安全事件，1,404 个钱包被盗、约 2.94 万亿枚 QU 被转移》</td><td>同上：被盗钱包数与转账量都核不到一手原文</td></tr>
        <tr><td>行情快照（06:34，CoinGecko / CoinMarketCap / alternative.me）：BTC $81,543（+0.4%）、ETH $2,390.06、USDT $0.999218、BNB $717.08、XRP $1.30；热搜 Pearl $1.88（+1.9%）、NEAR $4.879、Quantus $102.50（-6.2%）；CMC 搜索榜前六 BTC / ETH / XRP / SOL / ZEC / HBAR；恐惧贪婪指数 53（Neutral）；全网 24h 合约爆仓 3.55 亿美元、主爆多单</td><td>它们是某一刻的数字，不是可执行信息；涨跌与热度本身不构成价值</td></tr>
        <tr><td>CoinDesk / TheBlock 监管与机构面转述：白宫加密主管离任、拉脱维亚讨论 2027 年用加密缴税、稳定币供给停滞但支付量 +45%、Binance 与 Coinbase 参与西非反诈 Sweep、Crypto.com 与 Novig 起诉密苏里州、Circle 为 USDC 经济模型辩护、《加密审计给投资者虚假安全感》配 Q3 黑客数据</td><td>只有媒体口径，核不到可执行细节，也与在用资产无关</td></tr>
        <tr><td>DWF Labs 关于 AI 与加密融合的观点、「比特币下周或转而挤压空头，收复 83,600 美元」的行情观点、CZ 回应 BNB 手机提议、孙宇晨再交易 PEPE、Mt. Gox 前 CEO 要做检测 Ledger 植入物的设备</td><td>机构观点与 KOL 叙述，按口径不进正文，也不构成任何操作建议</td></tr>
        <tr><td>HN《Namecheap just seized and disabled all my domains》（324 分 / 158 评，回链是 Reddit 自述帖）</td><td>形态属「影响既有服务」，但只有当事人自述、无第二来源；若你名下域名（含在挂价的 iooiee.com）落在 Namecheap，值得自己去注册商后台核状态与解析，雷达不代做账号操作</td></tr>
        <tr><td>Epic 再往后的两档免单：《Sker Ritual》（当前标价 ¥78.00）+《Home - A Unique Horror Adventure》（¥15.00）10-22 23:00 开领、10-29 23:00 结束；《LISA: Definitive Edition》（¥108.00）11-01 14:00 开领、11-10 14:59 结束</td><td>档期起止都已从 <code>upcomingPromotionalOffers</code> 核到（06:47 那一轮，LISA 的 <code>start = 2026-11-01T06:00:00.000Z</code> 换成北京时间是下午两点而非零点），但这两批都不是今天动手的事；今晚 23:00 那一档已经升到上面的「值得」</td></tr>
        <tr><td>mlabonne/llm-course（trending，83,991 star）</td><td>内容对口（LLM 路线图 + Colab），但最近一次推送是 2026-02-05，今年 2 月后未再维护，属旧库回热</td></tr>
        <tr><td>Comfy-Org/ComfyUI（138,566 star，推送 2026-10-18 22:34Z，确在活跃）；Kruk2/jasna（视频修复，2026-01 新建、2,366 star）</td><td>都活跃，但一个偏 diffusion 工作流、一个偏视频修复，与 Java / C++ / Go 后端 + Agent 这条线不同轨</td></tr>
        <tr><td>lobsters《The Problem with C++ Safety: Why "It Works" Isn't Good Enough》；HN《Parser Combinators》（211 分，2026-10-17）</td><td>可读的单篇观点 / 教程，没有可核的时效价值锚点</td></tr>
        <tr><td>v2ex《codex 额度消耗快得离谱，5x 套餐随便几个问题 10% 没了》《Claude 过验证后丝滑升 5x》</td><td>个人体验帖，配额规则与账号条件都核不到</td></tr>
        <tr><td>IT 之家 11.11 一档：荣耀耳夹式耳机 499 → 378、华为 FreeClip 2 典藏版 1499 → 1146.8、AirPods 国补新增广东湖南两省（5 代 758 元起、Pro 3 1316 元）</td><td>到手价要登录电商平台才能核，且与服务器 / 域名 / 订阅赛道无关</td></tr>
        <tr><td>LowEndBox《Early Bird Discounts on Cheap Colocation! $29/Month in Phoenix from Cloudnium!》</td><td>回厂商官网 <code>cloudnium.com</code> 仍只有跳转 <code>/lander</code> 的停放页，价格与截止都核不到（10-18 已记一次，本轮复现）</td></tr>
        <tr><td>idcspy《RakSmart 双 11 黑五全场 4 折起 / 美国服务器秒杀 $29.9 起 / VPS $1.99 起》</td><td>软文体，没有可核的官方报价页与截止时间</td></tr>
        <tr><td>昨日已报道且仍在期内的存量：Steam 促销（赛博朋克 2077 ¥89.4 至 10-26、RDR2 ¥69.75 与霍格沃茨之遗 ¥38.4 至 10-22、雾锁王国 ¥124.2 至 10-29）、阮一峰周刊第 415 期、HF daily papers、Binance 公告 60 条、Ethereum 博客与 agave 发版</td><td>本轮被 <code>--seen</code> 跨天去重，不重复铺陈；福利本身仍在期内</td></tr>
      </tbody>
    </table>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">来源健康度：25 / 25 正常，0 个 ERR</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>来源</th><th>条数</th><th>来源</th><th>条数</th></tr></thead>
      <tbody>
        <tr><td>ithome</td><td>25</td><td>v2ex</td><td>9</td></tr>
        <tr><td>hackernews</td><td>23</td><td>coindesk</td><td>9</td></tr>
        <tr><td>lobsters</td><td>18</td><td>coinmarketcap-search</td><td>6</td></tr>
        <tr><td>panews / producthunt</td><td>各 15</td><td>github-trending</td><td>3</td></tr>
        <tr><td>coingecko-trending</td><td>10</td><td>theblock</td><td>2</td></tr>
        <tr><td>lowendbox / idcspy / exchange-status / coingecko-markets / fng-index</td><td>各 1</td><td colspan="2">本轮 16 个来源有条目</td></tr>
        <tr><td>epic / appstore-ios / steam / appinn / ruanyifeng / binance / hf / ethblog / creleases</td><td colspan="3">本轮 0 条（全部响应正常，是被 <code>--seen</code> 跨天去重或落在两天窗口外，不是改版也不是故障）；其中 epic、appstore-ios 今天都回官方接口做了在架复验</td></tr>
      </tbody>
    </table>
    <p style="font-size:12.5px;color:#6b7280;">SUMMARY fetched=312 fresh=140 sources=25 errors=0，无 <code>ERR source=</code> 行，本轮也没触发 <code>INFO source=appinn empty=</code>。境内（IT 之家、美国主机侦探、v2ex）与境外（HN、lobsters、CoinGecko、CoinDesk、TheBlock、PANews、Binance、Epic）两条通道都通：<code>t.me/s/TossTF</code> 走代理、<code>itunes.apple.com/lookup</code> 直连 200，因此不存在代理节点故障的怀疑对象。取数整轮约 50 秒，大头仍是 App Store 那一层逐条回 iTunes 核价。</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这一轮是怎么跑出来的：取数、验真、分级、边界</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p><strong>1 取数</strong>：25 个来源一次跑完（含币圈 11 个、iOS 限免 2 个），全量约 50 秒，输出归一化成 NDJSON，跨天去重靠 <code>history.jsonl</code>。</p>
    <p><strong>2 验真</strong>：价格与额度必须回官方页二次确认。本轮核到的原值——Epic <code>freeGamesPromotions</code> 接口两条周免的 <code>endDate</code>、<code>originalPrice</code>、<code>discountPrice</code>、<code>currencyCode</code>；iTunes <code>lookup</code> 按三个 <code>trackId</code>（6814895879 / 6816675193 / 6797824934）读国区现价（认 id 不认名字）；DeepSeek api-docs 的价格表与那句 11-01 起计费的原文；OpenCode 模型页上十三个 <code>-free</code> token；GitHub API 三个仓库的 star 与最近推送时刻；arXiv 摘要页的提交日期；交易所 Statuspage 原文。核不到的一律降级进观察——包括官网已成停放页的那单 colocation，以及只有媒体转述的两起安全事件。</p>
    <p><strong>3 分级</strong>：四档 🔥 / ⭐ / 👀 / ❌，宁严勿松。本轮无 🔥（最近一档截止距今 3 天 16 小时，且没有命中在用服务）；行情、热搜、情绪指数全部落在 👀；喊单、目标价、荐币、要求连钱包的形态落在 ❌，不进正文。</p>
    <p><strong>4 边界</strong>：雷达只到报告——不注册、不绑卡、不代领券、不下单、不点任何购买或领取按钮；iOS 的兑换码型限免不转载兑换码本身，只留频道原帖让你自取；币圈不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价，产物里不出现钱包地址与带 <code>ref=</code> 的返利参数。需要兑现的部分，只给官方直链和「你要做什么」。</p>
  </div>
</details>
