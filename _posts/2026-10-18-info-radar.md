---
title: "资讯雷达 2026-10-18｜Epic 两款周免、Notea 便利贴限免、Agent 记忆与编队两个新仓库"
author: OxYGC
date: 2026-10-18 06:35:00 +0800
permalink: /posts/info-radar-2026-10-18/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, App Store限免, 免费额度, Agent, 币圈]
description: "2026-10-18 这一轮 25 个来源取回 316 条、去重后 134 条新，0 个 ERR，留下 7 条值得看、14 组只作观察；优惠赛道本轮颗粒无收，因为唯一一条报价的厂商官网已经变成停放页。每条都带核实时间与官方直链。"
---

今早这一轮 25 个来源全绿，取回 316 条、按两天窗口去重后剩 134 条，0 个 ERR。分级结果很干净：没有 🔥，⭐ 7 条，👀 14 组。没有 🔥 的原因是最近一档截止是 Epic 周免的 10-22 23:00（北京时间），距今还有四天以上，也没有任何一条命中在用的域名、VPS 或已经依赖上的 API 免费额度。优惠价格这一类本轮整类删掉——窗口里只有一条 colocation 报价，回厂商官网核过去，域名已经变成跳转 `/lander` 的停放页，价格与截止都无从确认，所以它进不了「值得」。

<div style="border:1px solid #e8ebef;border-radius:10px;background:#fafbfc;padding:16px 20px 6px;margin-bottom:20px;">
  <p style="font-weight:700;font-size:16px;color:#1f2329;margin:0 0 10px;">四条要记的时点，都没有今晚关窗</p>
  <table>
    <thead><tr><th>截止 / 时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
    <tbody>
      <tr><td><span style="color:#c0392b;font-weight:700;">10-22 23:00（剩 4 天 16 小时）</span></td><td>Epic 周免《Bad Cheese》《Agent A - 伪装游戏》</td><td>0 元领取入库（原价折算 ¥40 / ¥62）</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
      <tr><td>Apple 不公布限免截止时间</td><td>App Store 国区《Notea便利贴》</td><td>0 元下载</td><td><a href="https://apps.apple.com/cn/app/id6814895879">App Store 页</a></td></tr>
      <tr><td>06:44 核到，官方页未标结束时间</td><td>OpenCode Zen 的 <code>deepseek-v4.1-flash-free</code> 免费档</td><td>模型调用 0 元档</td><td><a href="https://opencode.ai/docs/zen/">OpenCode Zen 文档</a></td></tr>
      <tr><td>06:41 状态快照</td><td>Kraken <code>Partially Degraded Service</code>（Coinbase 正常）</td><td>—</td><td><a href="https://status.kraken.com">Kraken 状态页</a></td></tr>
    </tbody>
  </table>
  <p style="font-size:13.5px;color:#6b7280;margin:0 0 10px;">另有开发 / AI 动态 3 条、限免 2 条、行情与安全转述若干；未核实或门槛高的 14 组放在最后一节。以下全部默认收起，点开看细节。</p>
</div>

## 值得看（7）

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">点击任意一条展开：价值判断、完整价格、核实到的接口字段都在里面。雷达只负责把消息带到——领取、下单、注册、绑定支付方式都由你自己完成。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Bad Cheese ｜ <span style="color:#1a7f37;">0 元（原价折算 ¥40）</span> ｜ <span style="color:#c0392b;">10-22 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>解谜 / 恶搞向小品，本周两连发里的第一款。这一档的价值不在于游戏本身合不合口味，而在于<strong>领取即入库</strong>——不需要在截止前玩完。</p>
    <p>昨日已报道过同一批，今日回 Epic 自家促销接口复核仍在架，所以按「仍在期内」保留，不当作旧闻重推。</p>
    <p style="font-size:12.5px;color:#6b7280;">接口字段 <code>until = 2026-10-22T15:00:00.000Z</code>（即北京时间 23:00）、原价折算 ¥40.00｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-18 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：Agent A - 伪装游戏 ｜ <span style="color:#1a7f37;">0 元（原价折算 ¥62）</span> ｜ <span style="color:#c0392b;">10-22 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>同一批的第二款，复古间谍题材解谜。<strong>与前一条共用同一个关窗时点</strong>，要做决定就一次做完，不用分两天惦记。</p>
    <p style="font-size:12.5px;color:#6b7280;">同一接口读到 <code>until = 2026-10-22T15:00:00.000Z</code>、原价折算 ¥62.00｜<a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a> ｜ 核实于 10-18 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">App Store 国区限免：Notea便利贴 ｜ <span style="color:#1a7f37;">下载 0 元</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>效率 / 工具类的便利贴应用，最低系统 iOS 15.0。播报名字是 Sticky Notea，国区商店名显示为 Notea便利贴——这正是这一类条目必须认 id 不认名字的原因。</p>
    <p><strong>口径要说清</strong>：Apple 的接口只证明<strong>今天下载不花钱</strong>，分不出「本来就免费」和「促销中」，也不公布促销结束时间，所以这一条不给截止日期。</p>
    <p style="font-size:12.5px;color:#6b7280;">iTunes 官方 <code>lookup</code> 按 <code>trackId = 6814895879</code> 核到 <code>price = 0.0 / formattedPrice = 免费 / currency = CNY</code>｜<a href="https://apps.apple.com/cn/app/id6814895879">App Store 页</a> ｜ 核实于 10-18 06:36</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">OpenCode Zen 的 DeepSeek V4.1 Flash Free ｜ <span style="color:#1a7f37;">免费档模型</span> ｜ <span style="color:#6b7280;">官方页未标结束时间</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>官方模型列表里带 <code>-free</code> 后缀的一档，切换模型即可选用，省的是模型调用这一层开销。额度与限流细则以官方页为准。</p>
    <p><strong>这一条只报道，不代注册</strong>：需要你自己登录 OpenCode 并在配置里选用该模型。</p>
    <p style="font-size:12.5px;color:#6b7280;">官方文档页文本实测含 <code>deepseek-v4.1-flash-free</code>、<code>deepseek-v4.1-flash</code>、<code>deepseek-v4-pro</code> 三个标识｜<a href="https://opencode.ai/docs/zen/">OpenCode Zen 文档</a> ｜ 核实于 10-18 06:44</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">DeepSeek-V4.1-Flash-1017 权重上架 Hugging Face ｜ <span style="color:#1a7f37;">MIT 开源</span> ｜ <span style="color:#6b7280;">无截止</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>昨天午后放出的新版权重，<code>license:mit</code>、<code>safetensors</code>、架构标签 <code>deepseek_v41</code>，pipeline 标的是 <code>image-text-to-text</code>，并同时给出 8-bit 与 fp8 形态。要跑本地推理、或者做「同一套业务换个模型会怎样」的对比评测，这一份可以直接拉。</p>
    <p style="font-size:12.5px;color:#6b7280;">模型仓库页元数据：<code>createdAt = 2026-10-17T05:46:55Z</code>（北京 13:46）、<code>likes = 905</code>、tags 含 <code>license:mit</code>、<code>endpoints_compatible</code>｜<a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017">模型仓库</a> ｜ 核实于 10-18 06:41</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">stablyai/orca（GitHub trending） ｜ <span style="color:#1a7f37;">开源免费</span> ｜ <span style="color:#6b7280;">95,340 star</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>仓库描述是「working with a fleet of agents 的地方」——用自己的订阅同时跑多个编码代理（Grok Bot、Claude Code 等）。它对应的是最近这一两个月真实出现的痛点：<strong>一个会话已经不够用了，得管一队 agent</strong>。要设计多 agent 分工与交接的人，可以先看它的组织方式。</p>
    <p style="font-size:12.5px;color:#6b7280;">GitHub 官方 API：<code>stargazers_count = 95340</code>、<code>pushed_at = 2026-10-17T22:36:32Z</code>、<code>createdAt = 2026-03-17</code>｜<a href="https://github.com/stablyai/orca">仓库</a> ｜ 核实于 10-18 06:44</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">akitaonrails/ai-memory（GitHub trending） ｜ <span style="color:#1a7f37;">开源免费</span> ｜ <span style="color:#6b7280;">9,883 star</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>解决的是编码 Agent 的长期记忆，外加<strong>在不同厂商的 agent 之间交接</strong>——换工具不换上下文。今年 5 月新建、两个多月做到接近一万 star，且最近 24 小时内仍在提交，属于增速与选题都站得住的那一类。</p>
    <p style="font-size:12.5px;color:#6b7280;">GitHub 官方 API：<code>stargazers_count = 9883</code>、<code>pushed_at = 2026-10-17T19:53:00Z</code>、<code>createdAt = 2026-05-21</code>、描述原文「long term memory for agent coding CLIs and to facilitate handoff between different agent vendors」｜<a href="https://github.com/akitaonrails/ai-memory">仓库</a> ｜ 核实于 10-18 06:44</p>
  </div>
</details>

## 观察（14 组）、币圈那一轮与方法

<p style="font-size:13.5px;color:#6b7280;margin:0 0 12px;">下面这些要么回官方页核不到，要么门槛要你自己登录、注册、绑卡才能兑现，所以一律不进「值得看」。行情类数字全是快照，不构成任何操作参考；雷达也不碰任何链上动作。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;" open>
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">观察清单：14 组，逐条写明存疑原因</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>条目</th><th>为什么只算观察</th></tr></thead>
      <tbody>
        <tr><td>Kraken <code>Partially Degraded Service</code>、Coinbase <code>All Systems Operational</code></td><td>06:41 状态快照。要不要紧取决于你在里面是否持有资产或挂着充提，雷达没有这项证据，所以只作提示；不构成任何操作建议</td></tr>
        <tr><td>Binance 公告 19 条：Hyperliquid（HYPE）上币与多业务开通、RWUSD 上币并附零交易费促销、Binance Pool 服务关闭、 covered call / cash-secured put 上线、保证金与 tick size 调整等</td><td>多数标题不带日期，且未回公告原文核对生效时间与合约地址（链上资产只按符号认会认错），按口径降为观察</td></tr>
        <tr><td>行情与热度：BTC $81,186（-0.6%）、ETH $2,387.12（-1.4%）、BNB $714.58、XRP $1.29；热搜 Pearl、Starknet（-12.2%）、Quantus、Quant；24h 合约爆仓 2.14 亿美元；恐惧贪婪指数当日读数</td><td>06:33 快照，来源 CoinGecko / CoinMarketCap / alternative.me。涨跌与热度是状态描述不是信息，一律不给方向判断</td></tr>
        <tr><td>LowEndBox《Phoenix 机房 colocation 早鸟价 $29/月（Cloudnium）》</td><td>回厂商官网只拿到 114 字节的跳转页（<code>window.onload</code> 跳 <code>/lander</code>），像域名到期后的停放页；价格与截止都核不到，先别当优惠处理</td></tr>
        <tr><td>idcspy《RakSmart 美国精品 CN2 大带宽服务器怎么样？》</td><td>软文体，没有可核的官方报价页与活动时间</td></tr>
        <tr><td>appinn《VideoProc Converter AI V7.8 周年庆限时赠送》</td><td>小众软件转述，本轮未回官方页核领取条件与截止时间</td></tr>
        <tr><td>HN《OpenCode Hacked: User credentials leaked》（594 分 / 93 评）</td><td>回链是 X 推文，没有机器可读通道可核；项目方 GitHub security advisory 最新一条是 2026-09-24 的 <a href="https://github.com/anomalyco/opencode/security/advisories/GHSA-632h-h47v-g4x4">GHSA-632h-h47v-g4x4</a>（high：<code>opencode serve</code> 且用 npm / pnpm / Bun 安装时，网页可跨站提交 <code>/global/upgrade</code> 装入任意包），并不覆盖「凭据泄露」这个说法。安全事件只认一手，若你在用 OpenCode，按 advisory 自查安装与升级形态，别据推文操作</td></tr>
        <tr><td>PANews《SecuX 钱包 App 紧急维护后仍现故障，Ripple 前 CTO 揭露 App 内推送钓鱼通知》</td><td>只有媒体转述，未见厂商 advisory 或官方公告；涉及硬件钱包却核不到一手。持有者只按官方公告处理，雷达不做任何链上操作</td></tr>
        <tr><td>TheBlock《土耳其确认 Hex 创始人 Richard Heart 被捕，查扣 715 万美元与六个冷钱包》</td><td>执法进展的媒体转述，无一手文件，且与在用资产无关</td></tr>
        <tr><td>机构与监管面转述：高盛 / 富国 / 摩根士丹利把代币化视为增长机会；Polygon 视收购 Coinme 为切入支付市场的入口；BIS 论文称银行抬高存款利率会拖慢稳定币扩张；CoreWeave、Broadcom、Verizon 等九家反对自家股票被拿去做代币化交易</td><td>加密媒体转述，核不到可执行细节，只作行业趋势底数</td></tr>
        <tr><td>IT 之家 11.11 一档：石头洗烘一体机 5999 → 1598 元、京东 10-20 20:00 加码、泰坦军团 2K 320Hz QD-OLED 3221 元（国补后 2898）</td><td>到手价需登录电商平台才能核，且与服务器 / 域名 / 订阅这几条赛道无关</td></tr>
        <tr><td>HN《Chrome and Edge are removing XSLT: what breaks and what does not》</td><td>只有 HN 转述，我试的开发者博客直链返回 404，正式弃文与时间表未核实</td></tr>
        <tr><td>昨日已报道、本轮被去重的存量：Steam 三档促销（10-22 17:00 / 10-29 17:00 截止）、阮一峰周刊第 415 期、Hugging Face daily papers 15 条、Ethereum 博客《Glamsterdam Hoodi Testnet Announcement》（10-16）、anza-xyz/agave v4.3.2（10-15）</td><td><code>history.jsonl</code> 按同一 id 去重，条目本身多数仍有效，需要细节请回看 10-16 / 10-17 两篇雷达</td></tr>
        <tr><td>ProductHunt 当日 15 条发布（NitroStack、Step 5 Preview、GPU Terminal by Context.dev、Craft Agents、Notion: Context for your agents 等）</td><td>发布会形态内容，价值与兑现门槛都未核实，整批不落「值得」</td></tr>
      </tbody>
    </table>
    <p style="font-size:12.5px;color:#6b7280;">另有两条按 ❌ 处理、不进任何正文段落：v2ex 的「注册送 $3 / 留 ID 送 $10 API 额度」中转站帖与「Muse AI 独享成品号 10 亿 Token」抽奖帖——要注册、要回帖、且属共享账号形态，雷达不转述兑现方式，也不提供任何绕过规则的做法。</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">来源健康度：25 / 25 正常，0 个 ERR</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>来源</th><th>条数</th><th>来源</th><th>条数</th></tr></thead>
      <tbody>
        <tr><td>ithome</td><td>25</td><td>lobsters</td><td>9</td></tr>
        <tr><td>hackernews</td><td>24</td><td>v2ex</td><td>9</td></tr>
        <tr><td>panews</td><td>15</td><td>coindesk</td><td>6</td></tr>
        <tr><td>producthunt</td><td>15</td><td>coinmarketcap-search</td><td>6</td></tr>
        <tr><td>coingecko-trending</td><td>10</td><td>github-trending / coingecko-markets</td><td>4 / 4</td></tr>
        <tr><td>theblock</td><td>2</td><td>lowendbox / idcspy / exchange-status / fng-index / appstore-ios</td><td>各 1</td></tr>
        <tr><td>epic / appinn / ruanyifeng / binance / steam / hf / ethblog / creleases</td><td colspan="3">本轮 0 条（全部响应正常，是被 <code>--seen</code> 跨天去重，不是改版也不是故障）</td></tr>
      </tbody>
    </table>
    <p style="font-size:12.5px;color:#6b7280;">SUMMARY fetched=316 fresh=134 sources=25 errors=0。境内（IT 之家、美国主机侦探、v2ex）与境外（HN、lobsters、CoinGecko、CoinDesk、PANews、Binance）两条通道本轮都通，因此不存在代理节点故障的怀疑对象。取数整轮约 50 秒，其中大头仍是 App Store 那一层逐条回 iTunes 核价。</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这一轮是怎么跑出来的：取数、验真、分级、边界</summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p><strong>1 取数</strong>：25 个来源一次跑完（含币圈 11 个、iOS 限免 2 个），全量约 50 秒，输出归一化成 NDJSON，跨天去重靠 <code>history.jsonl</code>。</p>
    <p><strong>2 验真</strong>：价格与额度必须回官方页二次确认。本轮核到的原值——Epic 促销接口的 <code>until</code> 与原价折算；iTunes <code>lookup</code> 按 <code>trackId = 6814895879</code> 的现价（认 id 不认名字，国区会改名）；OpenCode Zen 文档页的 <code>deepseek-v4.1-flash-free</code>；Hugging Face 模型仓库的创建时刻与许可标签；GitHub API 两个仓库的 star 与推送时刻；交易所 Statuspage 原文。核不到的，一律降级进观察——包括那条官网已经变成停放页的 colocation 报价。</p>
    <p><strong>3 分级</strong>：四档 🔥 / ⭐ / 👀 / ❌，宁严勿松。本轮无 🔥（最近一档截止距今四天以上，且没有命中在用服务）；行情、热搜、情绪指数全部落在 👀；要注册要回帖的送额度帖与共享成品号抽奖落在 ❌，不进正文。</p>
    <p><strong>4 边界</strong>：雷达只到报告——不注册、不绑卡、不代领券、不下单、不点任何购买或领取按钮；币圈不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价，产物里不出现钱包地址与带 <code>ref=</code> 的返利参数。需要兑现的部分，只给官方直链和「你要做什么」。</p>
  </div>
</details>
