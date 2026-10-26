---
title: "资讯雷达 2026-10-27｜证书链阻断、Agent 技能扫描器、Epic 与 App Store 限免"
author: OxYGC
date: 2026-10-27 06:58:00 +0800
permalink: /posts/info-radar-2026-10-27/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Steam优惠, 安全公告, AI动态]
description: "2026-10-27 一轮 25 个来源的取数结果：eMudhra 中间 CA 被入侵后命令行侧的可选处置、Epic 与 App Store 限免、Steam 四款折扣、GPT-6.1 Terra 官方现价，币圈整轮只作快照。"
---

这一轮跑了 25 个来源、322 条原始条目，去重后 176 条新进，零 ERR；境内外源同时全绿，说明本机代理节点没有异常。最后留下 12 条值得、16 条观察，一条都没有升「立刻处理」——最接近的那条是苹果关于 eMudhra 被入侵中间 CA 的官方说明，它给的命令行动作是「可选」而不是「限时」，而 Epic 两款限免还有两天多才到期。行情、热搜、恐惧贪婪指数这一整批按老规矩全部压进观察，喊单和目标价类直接不进任何段落。

<div style="border:1px solid #e6e6e6;border-radius:10px;padding:14px 16px;background:#fafafa;margin:0 0 28px;">
<p style="margin:0 0 10px;"><strong>行动清单</strong>（只放会过期或要复查的 4 条）</p>
<table>
<thead><tr><th>时点</th><th>条目</th><th>价格</th><th>去哪</th></tr></thead>
<tbody>
<tr><td style="color:#c0392b;font-weight:600;">10-29 23:00 前</td><td>Epic 本周限免两款《Sker Ritual》《Home - A Unique Horror Adventure》</td><td>¥78 → <span style="color:#1a7f37;">0 元</span>／¥15 → <span style="color:#1a7f37;">0 元</span></td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td></tr>
<tr><td style="color:#c0392b;font-weight:600;">命令行侧未自动兜住</td><td>eMudhra 中间 CA 私钥泄露，Apple 已阻断 12 张证书，但 <code>curl</code>／<code>git</code> 读 <code>/etc/ssl/cert.pem</code> 仍可能接受</td><td>公告免费</td><td><a href="https://support.apple.com/en-us/149555">Apple 支持文档 149555</a></td></tr>
<tr><td>11-03 02:00 前</td><td>Steam《Sons Of The Forest》-72%</td><td>¥108.00 → <span style="color:#1a7f37;">¥30.24</span></td><td><a href="https://store.steampowered.com/app/1326470/?l=schinese">Steam 商品页</a></td></tr>
<tr><td>11-07 01:00 前</td><td>Steam《Shadow of the Tomb Raider: Definitive Edition》-90%（本轮折扣率最高）</td><td>¥196.00 → <span style="color:#1a7f37;">¥19.60</span></td><td><a href="https://store.steampowered.com/app/750920/?l=schinese">Steam 商品页</a></td></tr>
</tbody>
</table>
<p style="margin:10px 0 0;font-size:13px;color:#6b7280;">时点均为北京时间。表里没有「点一下就领好」的动作：限免与折扣都要你自己在官方页完成，本站不代领、不代下单。</p>
</div>

## 值得看（12）

<details>
<summary><strong>eMudhra 中间 CA 被入侵：Apple 已自动阻断，命令行侧给了可选动作</strong> ｜ 免费 ｜ 无截止</summary>
<p>这不是「等系统更新」的事。eMudhra 运营的 <strong>8 个中间 CA 私钥被泄露</strong>，其中 2 张签发代码签名证书（Apple 框架本来就不信任），另外 6 张签发 TLS 证书——拿到这 6 张的密钥，就能造出对<strong>任意网站看起来有效</strong>的证书。Apple 从 2026-10-19 起阻断这 6 张 CA 的 12 张证书，10-23 起连带阻断 <code>emSign ECC Root CA - G3</code>，配置数据自动下发，<strong>不需要装软件更新</strong>：Safari、Mail 以及走 Apple 网络与安全框架的 App 已经生效，官方原话是「如果你不把终端作为工作流的一部分，你什么都不用做」。</p>
<p>唯一还留口子的地方恰好是这台机器的日常工作面：<strong>macOS 与 Xcode Command Line Tools 里的 <code>curl</code>、<code>git</code> 是按 <code>/etc/ssl/cert.pem</code> 校验证书</strong>，在后续软件更新之前它们仍可能接受这批证书。官方给的可选动作是从该文件里移除对应根 CA；eMudhra 与 Sectigo 已吊销受影响证书。本雷达每天核价走 <code>curl</code>、推站点走 <code>git</code>，属「在用工具」，建议自己扫一眼这个文件里有没有 emSign 相关根。</p>
<p>官方页：<a href="https://support.apple.com/en-us/149555">support.apple.com/en-us/149555</a> ｜ 核实于 2026-10-27 06:52（官方页原文直读）</p>
</details>

<details>
<summary><strong>NVIDIA/SkillSpector：给 AI agent skill 做安全扫描</strong> ｜ Apache-2.0 开源 ｜ 无截止</summary>
<p>扫描对象就是 agent 的技能包：检测漏洞、恶意模式、安全风险与提示注入。GitHub API 实测 <strong>22,126 star</strong>、最近一次推送 2026-10-23、许可 Apache-2.0，配套文档在 <code>docs.nvidia.com/skills/scanning-agent-skills</code>。这一条的价值在于「装完今天就能跑」：如果你本地有一整套自己维护的 skill / CLAUDE.md 目录，可以直接把它当静态审计器过一遍，而不是等某个技能包被投毒之后才回溯。</p>
<p>仓库：<a href="https://github.com/NVIDIA/SkillSpector">github.com/NVIDIA/SkillSpector</a> ｜ 核实于 2026-10-27 06:54（GitHub API）</p>
</details>

<details>
<summary><strong>gpt-6.1-terra 官方现价：每 1M tokens 输入 $1.00 / 输出 $5.00</strong> ｜ 公开定价页 ｜ 无截止</summary>
<p>官方定价页现状（每 1M tokens）：Standard 输入 <strong>$1.00</strong>、输出 <strong>$5.00</strong>、缓存输入 $0.05，30m / 12h 缓存写入 $1.25 / $2.50；Batch 档 $0.50 / $2.50；Fast 档 $2.00 / $10.00。同页横向对照：gpt-6-astra $10.00 / $50.00、gpt-6.1-sol $2.00 / $10.00、gpt-6-luna $0.10 / $0.50。另有一条容易忽略的加价规则：<strong>2026-03-05 及以后发布的模型，区域处理（数据驻留）端点加收 10%</strong>。</p>
<p>需要点名的口径问题：PANews 当天的标题写「API 价格降低 50%」，这条降幅<strong>只拿到中文媒体转述，没有核到前代价格</strong>，所以本文只报官方现价、不报降幅。</p>
<p>官方页：<a href="https://developers.openai.com/api/docs/pricing">developers.openai.com/api/docs/pricing</a> ｜ 核实于 2026-10-27 06:44</p>
</details>

<details>
<summary><strong>Anthropic 已向 SEC 提交 S-1</strong> ｜ 一手文件公开可读 ｜ 无截止</summary>
<p>招股书原文挂在 SEC EDGAR 上，可以直接读，不必二手转述。注意 SEC 要求请求带 User-Agent，否则返回 403（带合规 UA 实测 200）。同一天的三条通道互证：Hacker News 榜单 <strong>1,390 分 / 1,358 评</strong>、CoinDesk「AI giant Anthropic files for blockbuster IPO」、IT之家「提交纳斯达克 IPO 申请，股票代码为 ANT」。</p>
<p>一手文件：<a href="https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm">SEC EDGAR S-1</a> ｜ 核实于 2026-10-27 06:56</p>
</details>

<details>
<summary><strong>Epic 本周限免《Sker Ritual》</strong> ｜ ¥78.00 → <span style="color:#1a7f37;">0 元</span> ｜ 截止 2026-10-29 23:00（北京时间）</summary>
<p>官方 <code>freeGamesPromotions</code> 接口实测本周限免档，领取后永久入库。这一条昨天已经报过，本轮去重后没有算成新进条目，<strong>标为延续项</strong>再挂一次，理由是距截止还有两天且价格今天重新核过（核实于 2026-10-27 06:57）。领取需要你在 Epic 自己的页面完成，本站不代领。</p>
<p>页面：<a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure》</strong> ｜ ¥15.00 → <span style="color:#1a7f37;">0 元</span> ｜ 截止 2026-10-29 23:00（北京时间）</summary>
<p>同批次另一款，官方接口给的价格为 0。与上一条同为延续项，核实于 2026-10-27 06:57。</p>
<p>页面：<a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a></p>
</details>

<details>
<summary><strong>App Store 本体限免《Evthi: Notes, Money &amp; Docs》（id 6819098305）</strong> ｜ 下载不花钱 ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
<p>笔记 + 记账 + 文档三合一，开发者 MERVE CAFEROGLU，最低系统 15.5。核实方式：拿播报正文里的 <code>trackId</code> 回 <code>itunes.apple.com/lookup</code> 查国区，<strong>认 id 不认名字</strong>（国区会给 app 改名，按名字搜会把别人的免费价安到这条上）。iTunes 实测现价 <strong>免费</strong>，但接口分不出「本就免费」和「促销中」，所以只写<strong>下载不花钱</strong>，不写「限免仍在」。</p>
<p>页面：<a href="https://apps.apple.com/cn/app/id6819098305">apps.apple.com/cn/app/id6819098305</a> ｜ 核实于 2026-10-27 06:31</p>
</details>

<details>
<summary><strong>App Store 本体限免《灵感卡片 - 创意笔记》（id 6447693393）</strong> ｜ 下载不花钱 ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
<p>卡片式创意笔记工具，国区商店名与频道播报一致，开发者「士魁 冯」，最低系统 18.0。同一条核价链路：iTunes 国区按 id 实测现价 <strong>免费</strong>，即<strong>下载不花钱</strong>；Apple 不公布促销结束时间，那一栏只能空着写实话。</p>
<p>页面：<a href="https://apps.apple.com/cn/app/id6447693393">apps.apple.com/cn/app/id6447693393</a> ｜ 核实于 2026-10-27 06:31</p>
</details>

<details>
<summary><strong>Steam《Shadow of the Tomb Raider: Definitive Edition》-90%</strong> ｜ ¥196.00 → <span style="color:#1a7f37;">¥19.60</span> ｜ 截止 2026-11-07 01:00（北京时间）</summary>
<p>本轮折扣率最高的一条，决定版含全部追加内容。核实方式：官方 <code>appdetails</code> 取到 <code>initial 19600 / final 1960 / discount_percent 90</code>，再用官方 <code>featuredcategories</code> 的 <code>discount_expiration=1793984400</code> 换算截止时间。注意这里踩过一次时区坑：<strong>Steam 的 epoch 是 UTC，直接当北京时间打出来会早 8 小时</strong>，本文已按 UTC 11-06 17:00 = 北京 11-07 01:00 修正。</p>
<p>页面：<a href="https://store.steampowered.com/app/750920/?l=schinese">store.steampowered.com/app/750920</a> ｜ 核实于 2026-10-27 06:38</p>
</details>

<details>
<summary><strong>Steam《Sons Of The Forest》-72%</strong> ｜ ¥108.00 → <span style="color:#1a7f37;">¥30.24</span> ｜ 截止 2026-11-03 02:00（北京时间）</summary>
<p>本轮到期最早的一条。官方 <code>appdetails</code> 实测 <code>initial 10800 / final 3024 / -72%</code>，<code>discount_expiration=1793642400</code>（UTC 11-02 18:00 = 北京 11-03 02:00）。</p>
<p>页面：<a href="https://store.steampowered.com/app/1326470/?l=schinese">store.steampowered.com/app/1326470</a> ｜ 核实于 2026-10-27 06:38</p>
</details>

<details>
<summary><strong>Steam《蕾卡的移动工坊》-35%</strong> ｜ ¥76.00 → <span style="color:#1a7f37;">¥49.40</span> ｜ 截止 2026-11-07 20:00（北京时间）</summary>
<p>模拟经营类，官方接口实测 <code>initial 7600 / final 4940 / -35%</code>，<code>discount_expiration=1794052800</code>（UTC 11-07 12:00 = 北京 11-07 20:00）。</p>
<p>页面：<a href="https://store.steampowered.com/app/1737870/?l=schinese">store.steampowered.com/app/1737870</a> ｜ 核实于 2026-10-27 06:38</p>
</details>

<details>
<summary><strong>Steam《泡泡镇餐厅物语》-40%</strong> ｜ ¥48.00 → <span style="color:#1a7f37;">¥28.80</span> ｜ 截止 2026-11-10 01:00（北京时间）</summary>
<p>本轮到期最晚的一条，官方接口实测 <code>initial 4800 / final 2880 / -40%</code>，<code>discount_expiration=1794243633</code>（UTC 11-09 17:00 = 北京 11-10 01:00）。购买由你自己在 Steam 完成，本站不代下单。</p>
<p>页面：<a href="https://store.steampowered.com/app/3024130/?l=schinese">store.steampowered.com/app/3024130</a> ｜ 核实于 2026-10-27 06:38</p>
</details>

## 观察（17）、币圈那一轮与方法

<details>
<summary>观察清单：17 条未核实或门槛高的条目，各自缺哪一步</summary>
<table>
<thead><tr><th>条目</th><th>为什么没进「值得」</th></tr></thead>
<tbody>
<tr><td>Gname 把 .com 注册价 $13.99 上调至 $14.29</td><td>只有美国主机侦探 10-26 09:36 的转述；回 Gname 官网抽查当前页面仍大量展示 <strong>$13.99</strong>，官方页与转述对不上，调价未核实</td></tr>
<tr><td>Epic 本周折扣三款（Eternal Threads ¥62→¥12.40、《Sorry We're Closed》¥78→¥54.60、纪念碑谷 ¥33→¥11.55，均 11-02 24:00 前）</td><td>价格已回官方接口核实，但都是纯游戏折扣，对写作与开发工作流没有直接用处，按「宁严勿松」不占「值得」</td></tr>
<tr><td>美国主机侦探的双十一／黑五一批（ChemiCloud 低至 $1.49/月、WPCOM 7 折、凌霞 1Panel 与 Halo 6 折、Sif 折扣码、FriendHosting VDS 首期 6 折、Database Mart FX VPS $5.99/月）</td><td>全部只有聚合站转述，未回任何一家商家官方页核价，也没有统一促销截止时间</td></tr>
<tr><td>AgentScope Platform Beta 免费云端 AI Agent（4G 内存 / 30G 硬盘 + 一台 VPS）</td><td>只有小众软件转述；官方站返回 3.3 KB 的 JS 壳，curl 取不到正文，免费额度与 Beta 结束时间均未核实，且要求注册并绑定 GitHub 授权才让部署——门槛型，本站不代注册</td></tr>
<tr><td>Sebastian Raschka 推理模型视频课（八集、11+ 小时）</td><td>HN 494 分 / 75 评、页面可达，但<strong>是否完全免费没核实</strong>；同页提到的 LinkedIn Learning 版措辞本身带不确定（「通过链接访问应可 24 小时免费」）</td></tr>
<tr><td>苹果今晨批量发正式版（iOS/iPadOS 27.2、macOS 27.2、watchOS 27.2、visionOS 27.2、iPadOS 26.7.2、iOS 18.7.11）</td><td>只有 IT之家清单，未回 Apple 官方发布说明核实，尤其没确认是否含 eMudhra 证书链处置</td></tr>
<tr><td>交易所服务状态：Coinbase operational、Kraken Partially Degraded</td><td>10-27 06:31 状态页快照。按币圈口径，只有直接影响在用资产可得性才升紧急，本站没有「你把资产或充提挂在 Kraken」的证据</td></tr>
<tr><td>币安公告两条：10-28 新交易对 + Trading Bots、10-26 多个 TradFi USDⓈ 本位永续合约</td><td>属新产品与规则变更，不影响既有资产可得性，条款未逐条回公告原文核对，链与合约地址也未核</td></tr>
<tr><td>行情快照（BTC $79,889 -0.7%、ETH $2,308.05 -1.5%、USDT $0.99874、BNB $741.34 +0.2%、XRP $1.29 -0.7%）</td><td>10-27 06:31 快照，来源 CoinGecko。涨跌本身不构成价值，一律不给「值得」</td></tr>
<tr><td>市值前 300 内 24h 异动（Quack AI +199.4%、Bitway -28.8%、Rain -10.0%）与 CoinGecko 热搜前几位、CMC 搜索榜前 6</td><td>热搜与涨幅榜是这一轮里污染最重的一类，只作某时刻热度的旁证，不作任何依据</td></tr>
<tr><td>恐惧贪婪指数 50（Neutral）</td><td>只作语境底数，官方口径明写不构成操作建议</td></tr>
<tr><td>监管与结构类一批（韩国拟第四次推迟加密资本利得税至 2029、加拿大稳定币草案维持禁止发行方付收益、OCC 呼吁社区银行进稳定币支付、NBA 接入 Kalshi 与 Polymarket、Aviva 与 Ripple 在 XRP Ledger 发通证化份额）</td><td>只有英文媒体与中文转述，未取到监管方原文，数字与生效时点均未核实</td></tr>
<tr><td>项目方动态（Hyperliquid HIP-3*、Polygon Miden 合作伙伴主网接入 Agglayer、Chainlink 机构托管资产进 DeFi 借贷、USDC 在 Solana 新铸 2.5 亿枚、Akash 拟从 Cosmos 迁至 Solana 的治理投票）</td><td>均需回项目方一手公告核实，中文转述只作发现线索</td></tr>
<tr><td>企业金库类动作（Strategy 暂停买 BTC 并回购 $205M 优先股、Strive $511M、Bitmine 增持 10,452 ETH 并倾向回购股票）</td><td>公司财务公告，与个人资产可得性无关，只作背景</td></tr>
<tr><td>Solana 核心客户端发版 agave v4.5.0-alpha.4、v4.4.0-rc.1</td><td>项目方一手（GitHub Releases API 核实），但是 alpha／rc，也不是安全版本公告，只有自己跑节点才需要跟</td></tr>
<tr><td>过去 24 小时全网合约爆仓 1.96 亿美元、主爆多单</td><td>只有 PANews 转述，未回数据源核实</td></tr>
<tr><td>iOS 兑换码型限免两条（《Interview: Voice to Transcript》、《Enso Shift》）与内购限免（《Tabletally: Game Scorekeeper》）</td><td>兑换码一律不转载，只留频道原帖由本人自取（<a href="https://t.me/TossTF/3770">t.me/TossTF/3770</a>、<a href="https://t.me/TossTF/3771">t.me/TossTF/3771</a>），绝不代兑换；内购解锁价不体现在下载价上，只算转述，且前者按播报 id 6789004498 在 iTunes 国区查不到上架记录，价格未核实</td></tr>
</tbody>
</table>
</details>

<details>
<summary>币圈那一轮：四轴取到 44 条，为什么整批只给观察</summary>
<p>这一轮的币圈来自 11 个机器可读通道：交易所公告（币安三个目录 19 条）、服务状态页（Coinbase / Kraken 各 1，聚合为 1 条）、行情与热度（CoinGecko 快照与异动 4 条、热搜 10 条、CMC 搜索榜 6 条、恐惧贪婪指数 1 条）、项目方一手（Ethereum 博客窗内 0 条、GitHub Releases 2 条）、媒体转述（CoinDesk 12、TheBlock 12、PANews 15）。</p>
<p>判读门槛比另外四条赛道更硬：<strong>行情、涨跌幅、热搜、情绪指数默认全部落在观察</strong>，因为它们是状态描述而不是可执行信息，写进正文只会把日报变成荐股；只有<strong>直接影响在用资产可得性</strong>的公告才允许升紧急——资产下架、清退、充提暂停、服务状态非 none、签名或依赖漏洞、稳定币脱锚。本轮唯一接近这条线的是 Kraken 的 <code>Partially Degraded Service</code>，但它是否影响你取决于有没有把资产或充提挂在Kraken，本站没有这项证据，所以留在观察并写明存疑原因。</p>
<p>同时有三条被直接过滤、不写进任何段落：「$68M 的 BTC 押注瞄准选后突破 $90,000」、「Galaxy 称熊市已结束、现在是买入持有的时机」、「Tom Lee 坚称加密牛市正在进行」——喊单、目标价、荐币一律 ❌。安全事件这一轮没有新增：eMudhra 那条属于 PKI 而非链上资产，且已回到 Apple 一手文档核实，所以它出现在「值得」而不是币圈段。</p>
<p>边界照旧：不连钱包、不签名、不导私钥与助记词、不代充提、不给买卖建议与目标价；产物里不出现钱包地址与带邀请返利参数的链接，交易所落地页的推广参数一律剥掉。</p>
</details>

<details>
<summary>这一轮怎么跑的：四步口径与来源健康度</summary>
<p><strong>四步</strong>：取数（25 个来源，两天窗口，去重后 176 条新进）→ 验真（优惠／限免／免费额度三类一律回官方页二次确认价格与截止时间；App Store 限免按 <code>trackId</code> 回 iTunes 国区核价，认 id 不认名字）→ 分级（🔥 距截止 ≤3 小时或影响在用服务／⭐ 已核实且能落到动作／👀 未核实或门槛高／❌ 旧闻、软文、喊单）→ 落盘（本地存档 → 本页 → 邮件投递，三段齐了才算当天雷达跑完）。</p>
<table>
<thead><tr><th>来源</th><th>本轮条数</th><th>状态</th></tr></thead>
<tbody>
<tr><td>全量一轮（25 源，两天窗，带去重）</td><td>fetched 322 / fresh 176</td><td><span style="color:#1a7f37;">正常，errors=0</span></td></tr>
<tr><td>同窗口不带去重的重取（用于逐源计数）</td><td>225 条 / 23 源有条目</td><td><span style="color:#1a7f37;">正常</span></td></tr>
<tr><td>hackernews／lobsters／v2ex</td><td>23／20／10</td><td><span style="color:#1a7f37;">正常</span></td></tr>
<tr><td>ithome／idcspy／lowendbox／ruanyifeng-weekly</td><td>25／8／1／2</td><td><span style="color:#1a7f37;">正常（境内外源同时全绿＝代理节点无异常）</span></td></tr>
<tr><td>producthunt／github-trending</td><td>15／14</td><td><span style="color:#1a7f37;">正常（trending 无发布时间戳，star 数已回 GitHub API 复核）</span></td></tr>
<tr><td>steam</td><td>10</td><td><span style="color:#6b7280;">需注意</span>：脚本把 <code>discount_expiration</code>（UTC epoch）当北京时间输出，真实截止晚 8 小时，本档已换算修正</td></tr>
<tr><td>epic-store</td><td>5</td><td><span style="color:#1a7f37;">正常</span>（2 条确为 0 元；本轮去重后 0 条新进，故正文标为延续项）</td></tr>
<tr><td>appstore-ios／appinn</td><td>9／1</td><td><span style="color:#1a7f37;">正常</span>（发现层 <code>t.me/s/TossTF</code> 走代理，核价层走 iTunes 直连）</td></tr>
<tr><td>binance-ann／exchange-status</td><td>19／1</td><td><span style="color:#1a7f37;">正常</span></td></tr>
<tr><td>coingecko-markets／trending／cmc／fng</td><td>4／10／6／1</td><td><span style="color:#1a7f37;">正常</span>（快照 id 带当天日期，不会被去重吃掉）</td></tr>
<tr><td>coindesk／theblock／panews／crypto-release</td><td>12／12／15／2</td><td><span style="color:#1a7f37;">正常</span>（coindesk 的 308 重定向已跟转）</td></tr>
<tr><td>hf-daily-papers／ethereum-blog</td><td>0／0</td><td><span style="color:#1a7f37;">本轮 0 条（正常）</span>：前者最新论文停在 10-18，后者周更停在 10-22，均落在两天窗之外，不是故障</td></tr>
</tbody>
</table>
<p>没有一条 <code>ERR source=</code>。App Store 限免这一类没有截止时间是实话实说——Apple 不公布促销结束时间，那一栏就写这一句，不为了过发布门槛编一个日期出来。</p>
</details>
