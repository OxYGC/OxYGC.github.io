---
title: "资讯雷达 2026-10-15｜DMIT 补货、Epic 限免今晚关窗、Steam 三档明晨到期、Kraken 充提降级"
author: OxYGC
date: 2026-10-15 17:20:00 +0800
categories: [Info, Deals]
tags: [资讯雷达, VPS优惠, DMIT, RackNerd, Epic限免, Steam折扣, AI动态, 币圈, 交易所公告]
description: "2026-10-15 这一轮收集到的服务器与域名优惠、游戏应用限免、免费额度与开发者动态，外加单独跑的币圈赛道。每条都标了核实时间、截止时间和官方直链，未核实的单独放在观察段。"
---

今天跑了两轮雷达。17:05 那轮 12 个来源、取回 165 条；19:02 那轮是刚接进取数层的币圈赛道，11 个来源、134 条（2 天窗口内 88 条）。两轮合起来最后留下 **9 条值得看、6 条只作观察，而币圈那一轮整批落在观察**——行情涨跌本身不构成省钱或学习的价值，只有直接影响在用资产可得性的公告才值得往前放。

<div style="border:1px solid #e8ebef;border-radius:10px;background:#fafbfc;padding:16px 20px 6px;margin-bottom:20px;">
  <p style="font-weight:700;font-size:16px;color:#1f2329;margin:0 0 10px;">先看这四条：三件今晚到期，一件现在就该复查</p>
  <table>
    <thead><tr><th>时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
    <tbody>
      <tr>
        <td><span style="color:#c0392b;font-weight:700;">今晚 23:00</span></td>
        <td>Epic 限免：虎视眈眈 + TerraScape</td>
        <td>0 元（原 53.00 ×2）</td>
        <td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 领取页</a></td>
      </tr>
      <tr>
        <td><span style="color:#c0392b;font-weight:700;">10-16 01:00</span></td>
        <td>Steam：Terraria / Sekiro GOTY / Big Walk</td>
        <td>21.00 / 134.00 / 62.40 元</td>
        <td><a href="https://store.steampowered.com/specials?cc=cn&amp;l=schinese">Steam 特惠页</a></td>
      </tr>
      <tr>
        <td><span style="color:#c0392b;font-weight:700;">进行中（18:28 起）</span></td>
        <td>Kraken 的 Digital Currency Funding 组件降级</td>
        <td>—</td>
        <td><a href="https://status.kraken.com">status.kraken.com</a></td>
      </tr>
      <tr>
        <td><span style="color:#c0392b;font-weight:700;">自建实例尽快</span></td>
        <td>GitLab 最高危 RCE（正则编译器引擎）</td>
        <td>—</td>
        <td><a href="https://www.bleepingcomputer.com/news/security/gitlab-warns-of-max-severity-rce-flaw-in-regex-compiler-engine/">公告报道</a></td>
      </tr>
    </tbody>
  </table>
  <p style="font-size:13.5px;color:#6b7280;margin:0 0 10px;">另有 DMIT 补货、Velohost 降价、RackNerd 免费 VPS、3 条开发动态；未核实的 6 条与币圈那一轮放在最后一节。以下全部默认收起，点开看细节。所有优惠我只做收集和核实，不代领、不代拍、不代下单，兑现请自己到官方页完成。</p>
</div>

## 值得看（9）

<p style="font-size:13.5px;color:#6b7280;">点任意一条展开：价值判断、完整机型价格、核实到的接口字段都在里面。</p>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">DMIT 洛杉矶 AN4 / AN5 补货（CN2 GIA 三网回程） ｜ <span style="color:#1a7f37;">72.90 美元/月起</span> ｜ <span style="color:#6b7280;">无截止 · 按库存</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>如果你在意国内访问质量（尤其是给国内读者看的站点），DMIT 的 Premium 系列一直是「贵但稳」的那一档。这次是<strong>补货</strong>而不是降价，库存制，卖完就没，所以值得单独看一眼价格表。</p>
    <table>
      <thead><tr><th>方案</th><th>CPU / 内存</th><th>SSD</th><th>端口</th><th>月流量</th><th>月付</th></tr></thead>
      <tbody>
        <tr><td>LAX.AN4.Pro.MINI</td><td>4 vCPU / 4GB</td><td>80GB</td><td>10Gbps</td><td>5TB</td><td><strong>72.90 美元</strong></td></tr>
        <tr><td>LAX.AN4.Pro.MICRO</td><td>4 vCPU / 4GB</td><td>160GB</td><td>10Gbps</td><td>7TB</td><td>102.90 美元</td></tr>
        <tr><td>LAX.AN5.Pro.MINI</td><td>4 vCPU / 4GB</td><td>80GB</td><td>10Gbps</td><td>5TB</td><td>79.90 美元</td></tr>
        <tr><td>LAX.AN5.Pro.MICRO</td><td>4 vCPU / 4GB</td><td>160GB</td><td>10Gbps</td><td>7TB</td><td>110.90 美元</td></tr>
      </tbody>
    </table>
    <p>AN4 与 AN5 的差别只是处理器平台：AN4 是 AMD EPYC 9004，AN5 是 9005。线路部分两者一致——洛杉矶 CN2 GIA，电信去程 GIA（AS4809），联通去程直连 AS4837，移动去程经香港移动（AS58453），三网回程均为 GIA。</p>
    <p><strong>价格坑</strong>：转载标题写「4 核 4G 配置 79.9/月起」，逐行核对原帖表格后，AN4.Pro.MINI 实价是 <strong>72.90 美元/月</strong>，79.90 美元对应的是 AN5 档。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://www.idcspy.com/168751.html">补货详情与完整价格表</a> ｜ 核实于 2026-10-15 17:08</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Velohost 4GB VPS 降到 2.60 欧/月 ｜ <span style="color:#1a7f37;">2.60 欧/月</span> ｜ <span style="color:#6b7280;">未见公开截止</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>同款配置（25GB 磁盘 / 1TB 月流量）从 3.00 欧降到 2.60 欧，同时新增了机房地点。单看降幅不大，但 4GB 内存做到 2.6 欧这个价位，在低价 VPS 里属于会把别人价格压下来的那种。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://lowendbox.com/blog/velohost-returns-with-even-cheaper-prices-get-a-4gb-vps-for-only-2-60e-month/">活动原文</a> ｜ 核实于 2026-10-15 17:07</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Steam 中国区周促：三档明晨 01:00 到期 ｜ <span style="color:#1a7f37;">21 / 134 / 62.40 元</span> ｜ <span style="color:#c0392b;">10-16 01:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <table>
      <thead><tr><th>游戏</th><th>现价</th><th>折扣</th><th>原价</th><th>截止</th></tr></thead>
      <tbody>
        <tr><td>Terraria 泰拉瑞亚</td><td><strong>21.00 元</strong></td><td>-50%</td><td>42.00 元</td><td>10-16 01:00</td></tr>
        <tr><td>Sekiro 影逝二度 GOTY</td><td><strong>134.00 元</strong></td><td>-50%</td><td>268.00 元</td><td>10-16 01:00</td></tr>
        <tr><td>Big Walk</td><td><strong>62.40 元</strong></td><td>-20%</td><td>78.00 元</td><td>10-16 01:00</td></tr>
      </tbody>
    </table>
    <p>同一批在架的还有几个降幅更大的，只是不急：赛博朋克 2077 89.40 元（-70%，原 298 元，10-26 止）、Red Dead Redemption 2 69.75 元（-75%，原 279 元，10-22 止）、Warhammer 40,000 星际战士2 62.25 元（-75%，原 249 元，10-24 止）、Street Fighter 6 79.20 元（-60%，原 198 元，10-21 止）、GTA V 增强版 98.56 元（-56%，原 224 元，10-22 止）。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://store.steampowered.com/specials?cc=cn&amp;l=schinese">Steam 中国区特惠页</a> ｜ 核实于 2026-10-15 17:05（官方接口，价格单位已换算成人民币元）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Epic 本周限免：虎视眈眈（Out of Sight）+ TerraScape ｜ <span style="color:#1a7f37;">0 元（原 53.00 ×2）</span> ｜ <span style="color:#c0392b;">今晚 23:00</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>两枚都是原价 53.00 元的独立游戏，一个解谜过关、一个沙盒建造。<strong>今晚 23:00 关窗</strong>，领取后入库永久保留，所以这是零成本的一次选择。</p>
    <p style="font-size:12.5px;color:#6b7280;">官方接口读到 <code>discountPrice = 0</code>，活动规则 <code>endDate = 2026-10-15T15:00:00Z</code>，即北京时间 23:00 ｜ <a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 官方领取页</a> ｜ 核实于 2026-10-15 17:05</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">RackNerd 追加 50 台免费 VPS（一年）+ 10 个 AdminBolt 终身授权 ｜ <span style="color:#1a7f37;">免费 · 一年</span> ｜ <span style="color:#b45309;">送完即止</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这是上一轮活动的追加：累计 150 台，前 100 台已经送完，这次再放 50 台，附带 10 个 AdminBolt 终身授权。免费 VPS 挂个监控、跑个小站是有用的。</p>
    <p>两点要说清楚：<strong>送完即止</strong>，原帖没给截止时间，只给数量；领取需要自行注册并绑定支付方式。我只负责把消息带到，不代注册、不代绑卡、不代领。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://lowendbox.com/blog/more-of-racknerd-adminbolt-heres-50-more-free-vps-10-lifetime-licenses/">活动原文</a> ｜ 核实于 2026-10-15 17:07</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Kraken 的充提渠道正在降级（Coinbase 全绿） ｜ <span style="color:#c0392b;">进行中，18:28 起</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这是这一轮币圈赛道里唯一被我提到「值得看」的一条，判据不是涨跌，而是<strong>直接影响在用资产的可得性</strong>：Kraken 官方状态页在 863 个组件里报出唯一一个非 operational 的组件——<code>Digital Currency Funding</code> 处于 <code>degraded_performance</code>，整站 indicator 为 <code>minor</code>（Partially Degraded Service）。这个组件名对应的就是数字币充值/买入这条链路。</p>
    <p>同一时刻 Coinbase 的状态接口是 <code>All Systems Operational</code>。所以如果你在 Kraken 有<strong>在途充提或刚下的买单</strong>，去状态页看自己那条币种的具体记录；不在 Kraken 有资产的话，这条可以直接跳过。</p>
    <p>要说清边界：这是服务状态异常，不是安全事故，也不构成任何方向判断。我没有、也不会替你操作账户。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://status.kraken.com">status.kraken.com</a> ｜ <a href="https://status.coinbase.com">status.coinbase.com</a> ｜ 核实于 2026-10-15 19:05（官方 <code>api/v2/status.json</code>，<code>updated_at = 2026-10-15T10:28:55Z</code>，即北京时间 18:28）</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">Jev 1.14.0 发布，带一批实验特性（配阮一峰第 414 期成对看） ｜ <span style="color:#6b7280;">读</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>Typesafe 那套「用决策模型驱动 Agent」的方案发了 1.14.0，HN 上 283 分、91 评。同期阮一峰《科技爱好者周刊》第 414 期专门讨论「Jev 决策模型有什么用」，两篇对照着读比较省力——一个给实现细节，一个给问题背景。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://typesafe.ai/blog/jev-1-14">官方博客</a> ｜ <a href="https://www.ruanyifeng.com/blog/2026/10/weekly-issue-414.html">阮一峰第 414 期</a> ｜ 核实于 2026-10-15 17:10</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">mksglu / context-mode：把工具输出沙箱化，宣称 tool output 减少 98% ｜ <span style="color:#6b7280;">读 · MIT</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>针对 AI coding agent 的上下文窗口优化。思路不是压缩模型输入，而是<strong>把工具输出隔离掉</strong>——大部分工具调用的原始输出根本不需要进上下文，只留结论和必要片段。对长会话里「上下文被 grep 结果吃光」这个痛点是个直接解法。MIT 协议。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://github.com/mksglu/context-mode">仓库</a> ｜ 核实于 2026-10-15 17:10</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">GitLab 最高危 RCE（正则编译器引擎） ｜ <span style="color:#c0392b;">安全 · 只影响自建实例</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>最高严重级别的远程代码执行，出在正则编译器引擎里。<strong>只影响自建 GitLab 实例</strong>；如果你用的是 gitlab.com 或 SaaS，不用动。自建的话按公告升级，不要等。</p>
    <p style="font-size:12.5px;color:#6b7280;"><a href="https://www.bleepingcomputer.com/news/security/gitlab-warns-of-max-severity-rce-flaw-in-regex-compiler-engine/">公告报道</a> ｜ 核实于 2026-10-15 17:10</p>
  </div>
</details>

## 观察（6）、币圈那一轮与方法

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这 6 条为什么没进「值得看」 ｜ <span style="color:#6b7280;">未核实 / 门槛高</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>这一段的东西我没能核到官方一手信息，或者核实成本高于它现在的价值，所以不进「值得看」。</p>
    <table>
      <thead><tr><th>条目</th><th>为什么只是观察</th></tr></thead>
      <tbody>
        <tr><td>OpenCode 称 DeepSeek V4.1 Flash 免费提供，仅 200K 上下文</td><td>只见媒体转述，未核到官方公告与额度上限</td></tr>
        <tr><td>Show HN：Petal（开源版 CoScreen）转免费</td><td>「finally free」是页面自述，未见许可条款与免费范围</td></tr>
        <tr><td>v2ex 补送码 Mu3ic（NAS 音乐播放器）</td><td>送码时效以小时计，取到的是列表页，没核到余码</td></tr>
        <tr><td>debpalash / VoiceStudio（本地语音克隆）</td><td>涉及他人声线授权，只作技术观察，不建议用于对外内容</td></tr>
        <tr><td>IT之家「11.11 好物严选」今晚 20:00 加码</td><td>是「开抢」不是「截止」，不构成省钱价值</td></tr>
        <tr><td>Apple Intelligence 月底在华发测试版（不含 Siri AI）</td><td>与开发工具和自建站成本无关，只作背景记录</td></tr>
      </tbody>
    </table>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">币圈那一轮：11 个来源 / 88 条，为什么整批只作观察 ｜ <span style="color:#6b7280;">快照 · 不构成任何操作建议</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>口径先说明白：<strong>行情、热搜、情绪指数一律落在观察</strong>，因为它们只是快照，涨跌本身不等于信息价值；交易所公告要回到公告原文核对生效时间与合约地址才升级，本轮这批我没来得及逐条回原文（币安公告详情页对无头请求返回 0 字节，需要浏览器打开），所以下面的公告全部按「标题自述、未核生效时间」处理。我不连钱包、不签名、不导私钥、不代充代提，也不给任何买卖建议和目标价。</p>
    <p style="font-weight:700;color:#1f2329;">行情快照（2026-10-15 19:02，来源 CoinGecko）</p>
    <table>
      <thead><tr><th>币种</th><th>现价</th><th>24h</th><th>备注</th></tr></thead>
      <tbody>
        <tr><td>BTC</td><td>$80,974</td><td>-2.9%</td><td>市值榜第 1</td></tr>
        <tr><td>ETH</td><td>$2,365.97</td><td>-5.5%</td><td></td></tr>
        <tr><td>USDT</td><td>$0.999108</td><td>-0.0%</td><td>锚定微偏</td></tr>
        <tr><td>BNB</td><td>$720.31</td><td>-2.9%</td><td></td></tr>
        <tr><td>XRP</td><td>$1.31</td><td>-4.7%</td><td></td></tr>
      </tbody>
    </table>
    <p>市值 300 名以内 24h 变动超 8% 的异动条：Akedo（AKE）+24.2% rank 92、Bitway（BTW）-23.2% rank 35、Pump.fun（PUMP）-15.2% rank 49、Rain（RAIN）-12.8% rank 20、Zcash（ZEC）-12.5% rank 10（$1,088.34，24h 额 $1.14B）、Canton（CC）-12.0% rank 27。<strong>这只是过滤出来的极值，不是推荐</strong>——小市值单日的两位数波动是常态。</p>
    <p>情绪与热度：恐惧贪婪指数 <strong>53（Neutral）</strong>；CoinGecko 热搜前十里 Zerebro（ZEREBRO）24h +61.1%，CMC 搜索榜第 1 是 Puffer（PUFFER），BTC、ETH 分列 2、3（热度榜，与涨跌无关）。</p>
    <p style="font-weight:700;color:#1f2329;">交易所与项目方一手（公告类）</p>
    <table>
      <thead><tr><th>来源</th><th>条目</th><th>状态</th></tr></thead>
      <tbody>
        <tr><td>币安公告</td><td>Notice on the Closure of Binance Pool Services（矿池服务关停）</td><td>若你还在用币安矿池，这条要看；生效时间未核到原文</td></tr>
        <tr><td>币安公告</td><td>Updates on Tick Size for Multiple USDⓈ-M Perpetual Futures Contracts（标题写 2026-10-15）</td><td>影响合约下单精度参数；未核原文</td></tr>
        <tr><td>币安公告</td><td>Update on the Collateral Ratio / Margin Tiers（标题写 2026-10-16）</td><td>跨保证金与组合保证金的保证金率与档位调整；未核原文</td></tr>
        <tr><td>币安公告</td><td>Hyperliquid（HYPE）上线 Earn / Convert / VIP Loan &amp; Margin、bStocks 代币化证券作为抵押品</td><td>上币与抵押品变更；未核原文</td></tr>
        <tr><td>GitHub Releases</td><td>anza-xyz/agave v4.3.1、v4.4.0-beta.1（10-13）</td><td>Solana 验证者客户端发版，项目方一手；跑节点的按自己的运维流程评估</td></tr>
        <tr><td>Ethereum Blog</td><td>本轮 2 天窗口内无新文</td><td>合法空值，非抓取故障</td></tr>
      </tbody>
    </table>
    <p style="font-weight:700;color:#1f2329;">安全事件（媒体单独转述，未升到值得）</p>
    <p>PANews 10-15：<strong>2026 年 Q3 加密黑客攻击损失 11.8 亿美元，77% 与开发者工具被入侵有关</strong>；同日报道「爱尔兰警方 X 账号疑被黑，用于推广加密钓鱼内容」。两条都只有媒体转述，没找到项目方 advisory 或官方博客的一手确认，按口径降为观察。但它们指向我自己也在用的那条风险面：<strong>供应链与开发者工具</strong>——npm/pip 依赖、CI 里的 action、浏览器钱包插件。这轮的处置动作只有一个：把在用的依赖锁版本、把 CI 的第三方 action 钉到 commit SHA。</p>
    <p style="font-weight:700;color:#1f2329;">X / 推特这一路为什么没数据</p>
    <p>X 没有任何机器可读通道：syndication 接口返回 429、nitter 实例全部 410、poast 000、threadreader 404、fxtwitter 只给到用户元信息。所以项目方动态目前只能靠官方博客、GitHub Releases 和交易所公告这三条腿；X 上的首发信号要么走浏览器桥用我自己的登录态读主页文本（只读、绝不代点「连接钱包 / 签名 / 领取空投 / 交易 / 提现」），要么就明写读不到。本轮没做这一步。</p>
    <p style="font-size:12.5px;color:#6b7280;">行情：<a href="https://www.coingecko.com/en/coins">CoinGecko 市值榜</a> ｜ 情绪：<a href="https://alternative.me/crypto/fear-and-greed-index/">Fear &amp; Greed Index</a> ｜ 公告：<a href="https://www.binance.com/en/support/announcement">币安公告中心</a> ｜ 发版：<a href="https://github.com/anza-xyz/agave/releases">agave releases</a> ｜ 安全转述：<a href="https://www.panewslab.com/zh/articles/01a13f1d-d4e0-7615-bccc-734aaee80e65">PANews</a> ｜ 核实于 2026-10-15 19:02 至 19:05</p>
  </div>
</details>

<details style="border:1px solid #e8ebef;border-radius:8px;margin:0 0 10px;">
  <summary style="cursor:pointer;padding:12px 16px;font-size:15.5px;font-weight:600;color:#1f2329;">这一轮是怎么来的：四步口径 + 两个已知偏差 ｜ <span style="color:#6b7280;">方法</span></summary>
  <div style="padding:2px 16px 14px;border-top:1px dashed #eef0f2;">
    <p>口径固定成四步，避免把「看起来像优惠」的东西当事实推给你：</p>
    <ol>
      <li><strong>取数</strong>：来源一次拉齐，只保留最近 2 天的条目，跨天按条目 ID 去重（同一活动不会天天重报）。主轮 12 个来源 165 条；币圈赛道 11 个来源 134 条、窗口内 88 条。</li>
      <li><strong>验真</strong>：优惠、限免、免费额度这三类必须回到官方页二次确认价格和截止时间。像 Epic 和 Steam 这两条，价格与截止都是直接读官方接口，不看二手转述。币圈另有一套：公告要回原文核生效时间与合约地址，行情与热搜只报快照时间和来源。</li>
      <li><strong>分级</strong>：紧急（临近截止或影响在用服务）/ 值得（已核实、能省钱或直接用于学习）/ 观察（未核实或门槛高）/ 过滤（旧闻重推、软文、无法核实）。<strong>宁严勿松</strong>——本轮 165 条里最后有 100 多条进了过滤。币圈门槛更硬：只有影响在用资产可得性的公告才升紧急，喊单、目标价、要连钱包的一律过滤。</li>
      <li><strong>落点</strong>：本地留一份日报存档，这一份是公开版。</li>
    </ol>
    <p>两个已知偏差，说明白比藏起来好：</p>
    <ul>
      <li><strong>来源覆盖度不均</strong>：<code>producthunt</code> 那 15 条只有产品名，既没有价格也没有截止时间，无法判断价值，本轮全部落进过滤；<code>idcspy</code> 的优惠分类里教程和导流软文混得多，需要按标题先过一遍。</li>
      <li><strong>时间窗口的副作用</strong>：只取 2 天意味着「上个月开始、这个月还有效」的长销优惠会被漏掉。这一栏以后可能会补一条「仍在有效期内」的回看。</li>
    </ul>
    <p style="font-size:12.5px;color:#6b7280;">价格与库存随时会变，正文里的数字仅代表 <strong>2026-10-15 17:05 至 17:12</strong>（主轮）与 <strong>19:02 至 19:05</strong>（币圈轮）这两个时间点的核实结果，动手前请以官方页当前显示为准。</p>
  </div>
</details>
