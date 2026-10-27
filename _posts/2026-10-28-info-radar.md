---
title: "资讯雷达 2026-10-28｜Epic 与 App Store 限免、Steam 深折扣、Kraken 服务降级"
author: OxYGC
date: 2026-10-28 06:35:00 +0800
permalink: /posts/info-radar-2026-10-28/
categories: [Info, Deals]
tags: [资讯雷达, 限免, Steam折扣, Epic, App Store, 币圈]
description: "2026-10-28 一轮 25 个来源的资讯雷达：Epic 与 App Store 限免、Steam 生存恐怖类深折扣、Ghostty 1.4.0 与 Claude 状态页，以及 Kraken 服务降级这条唯一需要复查的项。"
---

这一轮跑了 25 个来源，取回 310 条，去重后 174 条新进，0 个来源异常。真正留下来的只有 7 条「值得」和 1 条需要复查的 🔥：一条是 Kraken 官方状态页此刻仍挂着 `Partially Degraded Service`（这条能不能忽略，取决于你有没有把资产放在那儿，我无从知道），另一条是 Epic 本周限免《Home》——它已经连续两天被跨天去重挡在门外，而领取窗口只开到明天晚上。

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
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">10-29 23:00（北京）</strong></td>
        <td>Epic 本周限免《Home - A Unique Horror Adventure》</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">0 元</span></td>
        <td><a href="https://store.epicgames.com/free-games?lang=zh-CN">Epic 免费游戏页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">11-02（商店页文案）</strong></td>
        <td>Steam 生存／恐怖 5 款（Outlast 系列、The Forest、Subnautica、Outlast Trials）</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">低至 ¥5.80</span></td>
        <td><a href="https://store.steampowered.com/app/238320/?l=schinese">Steam 商店页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;">无截止（Apple 不公布）</td>
        <td>App Store 本体限免：Countdown／Sidebar Fast Notes／ClickShelf（macOS）</td>
        <td><span style="background:#e7f4ea;color:#1a7f37;border-radius:999px;padding:2px 9px;">下载不花钱</span></td>
        <td><a href="https://apps.apple.com/cn/app/id6766478836?mt=12">其中 ClickShelf 商品页</a></td>
      </tr>
      <tr>
        <td style="white-space:nowrap;"><strong style="color:#c0392b;">现在（北京 06:04 起）</strong></td>
        <td>Kraken 官方状态页 <code>Partially Degraded Service</code>——仅在 Kraken 有资产或正在充提时需要自查</td>
        <td><span style="background:#eef0f2;color:#6b7280;border-radius:999px;padding:2px 9px;">服务状态</span></td>
        <td><a href="https://status.kraken.com/">Kraken 状态页</a></td>
      </tr>
    </tbody>
  </table>
  <p style="margin:10px 0 0;font-size:12px;color:#8a9099;line-height:1.75;">这一轮雷达只收集、核实、报告：不代注册、不代绑卡、不代领券、不代下单；iOS 兑换码型限免不转载兑换码，币圈不连钱包、不签名、不给买卖建议。兑现动作全部由你本人完成。</p>
</div>

## 值得看（7）

<details open>
<summary><strong>Epic 本周限免《Home - A Unique Horror Adventure》</strong> ｜ <span style="color:#1a7f37;">原价 ¥15.00 → 0 元</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 2026-10-29 23:00（北京时间）</span></summary>
<p>领了永久入库，本轮唯一一款 0 元游戏。<strong>这条连续两天被跨天去重挡在本轮 fresh 之外</strong>：Epic 条目的 id 不带日期（形如 <code>epic-store:home-a-unique-horror-adventure</code>），昨天报过今天就不再算新进，可它的领取窗口一直开到明晚——所以只要还挂着，去重就会一直挡。这里按「延续项 + 今天新核的核实时间」再挂一次。</p>
<table>
  <tr><td style="width:120px;">核实于</td><td>2026-10-28 06:36</td></tr>
  <tr><td>价格来源</td><td>Epic 官方 <code>freeGamesPromotions</code> 接口，<code>totalPrice = 0</code>（<code>--source epic --days 30</code> 单取仍返回 5 条，可证不是抓取失败）</td></tr>
  <tr><td>截止时间</td><td>接口 <code>endDate = 2026-10-29T15:00:00.000Z</code> → 北京时间 10-29 23:00</td></tr>
  <tr><td>直链</td><td><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games?lang=zh-CN</a></td></tr>
</table>
</details>

<details>
<summary><strong>App Store 本体限免三款：Countdown ／ Sidebar | Fast Notes ／ ClickShelf（macOS）</strong> ｜ <span style="color:#1a7f37;">iTunes 国区实测现价 免费</span> ｜ <span style="color:#6b7280;">Apple 不公布限免截止时间</span></summary>
<p>这三款都是汇总频道播报、再回 iTunes 按 <code>trackId</code> 核过国区现价（<strong>认 id 不认名字</strong>——国区常给 app 改名，按名字搜会认错 app、把别人的免费价安到这条上）。核到现价为 0 只能说明<strong>下载不花钱</strong>，接口分不出「本就免费」和「促销中」，所以不写成「限免仍在」。</p>
<table>
  <tr><th style="text-align:left;">App</th><th style="text-align:left;">id</th><th style="text-align:left;">开发商</th><th style="text-align:left;">最低系统</th><th style="text-align:left;">商品页</th></tr>
  <tr><td>Countdown #</td><td>1534330734</td><td>Khang Le</td><td>26.0</td><td><a href="https://apps.apple.com/cn/app/countdown/id1534330734">apps.apple.com</a></td></tr>
  <tr><td>Sidebar | Fast Notes</td><td>6450434079</td><td>Chris Woods</td><td>18.6</td><td><a href="https://apps.apple.com/cn/app/sidebar-fast-notes/id6450434079">apps.apple.com</a></td></tr>
  <tr><td>ClickShelf - 右键增强工具</td><td>6766478836</td><td>haoqiang shan</td><td>15.6（<code>mt=12</code>，macOS 端）</td><td><a href="https://apps.apple.com/cn/app/id6766478836?mt=12">apps.apple.com</a></td></tr>
</table>
<p>三款里只有 ClickShelf（访达右键菜单增强）跟日常 macOS 工作流直接相关，另两款是通用工具，按需取。</p>
<p style="color:#8a9099;font-size:13px;">核实于 2026-10-28 06:40，三款各用 <code>--lookup &lt;id&gt;</code> 重跑一次读国区现价。<strong>Apple 不公布限免截止时间</strong>，所以这一栏不填日期——不是漏写。</p>
</details>

<details>
<summary><strong>Steam 生存／恐怖 5 款深折扣</strong> ｜ <span style="color:#1a7f37;">Outlast ¥5.80（-90%）起</span> ｜ <span style="color:#c0392b;font-weight:700;">截止 11 月 2 日（商店页文案）</span></summary>
<p>本轮折扣率最高的一批，价格与折扣率全部回 Steam 官方接口 <code>appdetails?cc=cn</code> 逐条核对过，五条全中：</p>
<table>
  <tr><th style="text-align:left;">游戏</th><th style="text-align:left;">原价</th><th style="text-align:left;">现价</th><th style="text-align:left;">折扣</th><th style="text-align:left;">商品页</th></tr>
  <tr><td>Outlast</td><td>¥58.00</td><td>¥5.80</td><td>-90%</td><td><a href="https://store.steampowered.com/app/238320/?l=schinese">app/238320</a></td></tr>
  <tr><td>Outlast 2</td><td>¥76.00</td><td>¥7.60</td><td>-90%</td><td><a href="https://store.steampowered.com/app/414700/?l=schinese">app/414700</a></td></tr>
  <tr><td>The Forest</td><td>¥70.00</td><td>¥14.00</td><td>-80%</td><td><a href="https://store.steampowered.com/app/242760/?l=schinese">app/242760</a></td></tr>
  <tr><td>Subnautica - 深海迷航</td><td>¥149.00</td><td>¥37.25</td><td>-75%</td><td><a href="https://store.steampowered.com/app/264710/?l=schinese">app/264710</a></td></tr>
  <tr><td>The Outlast Trials</td><td>¥136.00</td><td>¥40.80</td><td>-70%</td><td><a href="https://store.steampowered.com/app/1304930/?l=schinese">app/1304930</a></td></tr>
</table>
<p style="color:#c0392b;"><strong>截止时间这里有个必须交代的口径差：</strong>Steam 国区商店页正文写的是「特别促销！11 月 2 日截止」，而雷达取回的 UTC 时间戳是 <code>2026-11-02 18:00</code>，换算成北京时间要落到 11-03 02:00——两处差 8 小时。这是昨天就记录在案的「脚本把 <code>discount_expiration</code> 的 UTC 当北京时间输出」的老问题，这一轮没有改脚本，正文以商店页显示为准。</p>
<p style="color:#8a9099;font-size:13px;">核实于 2026-10-28 06:37（官方 <code>appdetails?cc=cn</code> 五条 + 商店页正文直读）。</p>
</details>

<details>
<summary><strong>Ghostty 1.4.0 正式版发布说明</strong> ｜ <span style="color:#6b7280;">免费开源</span> ｜ <span style="color:#6b7280;">无截止（版本发布，不是限时活动）</span></summary>
<p>如果本机终端走的是 Ghostty，这是唯一能直接对上「要不要升级」的一手页。官方 release notes 页返回 200，标题就是 <code>1.4.0 - Release Notes</code>，同页有 Docs／Configuration／Features／Terminal API (VT) 的完整结构。</p>
<p style="color:#8a9099;font-size:13px;">核实于 2026-10-28 06:40（官方页直读）｜直链 <a href="https://ghostty.org/docs/install/release-notes/1-4-0">ghostty.org/docs/install/release-notes/1-4-0</a>。本轮只确认「这一版存在且发布说明页可直读」，没有逐条读 changelog，具体变更请自己过一眼。</p>
</details>

<details>
<summary><strong>Claude 状态页：现在 All Systems Operational，但昨天北京 22:42–23:17 有过一次 Sonnet 5.5 错误率升高</strong> ｜ <span style="color:#6b7280;">公开状态页</span> ｜ <span style="color:#6b7280;">无截止</span></summary>
<p>这条的价值不在新闻本身，而在<strong>它正好压在个人定时链路的运行时段上</strong>。官方 incident 原文：<em>“The issue affecting claude.ai, the Claude API, Claude Code, and Claude Cowork has been resolved. Impact occurred from 07:42 PT / 14:42 UTC to 08:17 PT / 15:17 UTC.”</em> 换成本地时间即 <strong>10-27 22:42–23:17</strong>；同日 09:14 UTC 还有一条同名 resolved 记录。当前 <code>status.json</code> 为 <code>indicator = none</code>。</p>
<p>用法很实际：如果你那天晚上有自动化跑空或者报错，先看这个窗口能不能对上，而不是先怀疑自己的脚本。</p>
<p style="color:#8a9099;font-size:13px;">核实于 2026-10-28 06:41（<code>api/v2/status.json</code> 与 incident 列表各读一次）｜直链 <a href="https://status.claude.com/">status.claude.com</a>。</p>
</details>

## 观察（17）、币圈那一轮与方法

<details>
<summary>观察清单：17 条，每条后面都写存疑原因（未核实或门槛高，一律不进「值得」）</summary>
<table>
  <tr><th style="text-align:left;">条目</th><th style="text-align:left;">为什么只在观察</th></tr>
  <tr><td>腾讯云双十一：4 核 4G 轻量 38 元/年、GPU 0.8 折起、Token Plan 28 元/月起</td><td>只有聚合站 10-27 转述；官方秒杀页 curl 只取回 986 字节的 JS 壳，价格一个都没核到，且这类秒杀通常限量</td></tr>
  <tr><td>HostArmada 万圣节促销 WordPress 主机 $2.15/月（码 <code>HAFALL2682WP12</code>）</td><td><strong>价格已核到官方页</strong>（<code>signup.total=$25.81</code>、<code>monthlyEquivalent=$2.15</code>），但续费 $11.95/月不是续费同价，且整页找不到促销截止时间——缺「截止」这一栏就卡发布门槛，所以不进值得</td></tr>
  <tr><td>Epic 折扣《纪念碑谷》¥33.00 → ¥11.55，截止北京 11-03 00:00</td><td>官方接口核到了，但纯游戏折扣、对工作流无用处，按「宁严勿松」留观察</td></tr>
  <tr><td>AgentScope Platform 免费云端 AI Agent（4G 内存 / 30G 硬盘）</td><td>只有小众软件 10-26 转述，额度与 Beta 结束时间均未核实，且要注册授权；雷达不代注册</td></tr>
  <tr><td>v2ex 两条送码（Zipover 跨平台剪贴板 30 份授权、Mu3ic 更新送码）</td><td>门槛型羊毛，要登录并抢名额，剩余数量与可得性均未核实</td></tr>
  <tr><td>App Store 兑换码型限免《RenewPal: Subscription Tracker》</td><td><a href="https://t.me/TossTF/3777">兑换码不转载，只留频道原帖由本人自取</a>；也没走 iTunes 核价，绝不代兑换</td></tr>
  <tr><td>App Store《Soulo: Multi-Search Browser》</td><td>播报「本体限免」，但 iTunes 按播报里的 id <code>6761165330</code> <strong>查不到上架记录</strong>，价格未核实</td></tr>
  <tr><td>App Store《4Video DVD Manager》</td><td>播报「本体限免」，iTunes 国区现价 <strong>¥98.00</strong> ⇒ 判播报的限免已失效或已改价，不要照着装</td></tr>
  <tr><td>Anthropic 确认其内部系统遭访问：客户对话、模型权重未受影响</td><td>只有中文媒体转述，没回一手声明；且 Claude 状态页 incident 历史里没有对应安全事件条目（只有模型错误率升高那几条），按未核实处理</td></tr>
  <tr><td>京东 1 号会员店 10-28 起调整会员权益（尊享卡返 2% 赠金、每月权益需消费解锁）</td><td>生效日就是今天，但未回京东官方页核实条款原文；是会员的话自己看账户</td></tr>
  <tr><td>LowEndBox：Microsoft Early Buyouts 评论、DreamHost 要求受影响客户重置邮件与 FTP 密码</td><td>资讯转述，不是可领的优惠，也不是你名下的服务</td></tr>
  <tr><td>币安公告 3 条：USDⓈ-M 永续 Tick Size（10-28）、交叉／组合保证金抵押率（10-30）、部分逐仓交易对杠杆调整</td><td>都是交易参数调整，不涉及资产下架／清退／充提暂停，所以不升 🔥；日期只写在标题里，没有逐条回公告原文核生效时间与适用范围</td></tr>
  <tr><td>主流币行情快照（取数时刻 10-28 06:32，来源 CoinGecko）：BTC $80,845.8 +1.2%、ETH $2,347.86 +1.7%、USDT $0.99881、BNB $744.68 +0.5%、XRP $1.32 +2.5%</td><td>行情是数字不是信息，一律不给「值得」，也不做任何方向判断</td></tr>
  <tr><td>24h 异动与热搜：Bitway +49.7%（rank 41）、MemeCore +12.7%；CoinGecko 热搜 PENGU、STONK +20.2%、ZEC $1,304.73、BTC、SOL；CMC 搜索榜 AIN、HAEDAL、MAGMA、BNB、AKE、ZAMA</td><td>热搜与涨幅榜是污染最重的一类，只作某时刻热度的旁证</td></tr>
  <tr><td>恐惧贪婪指数 48（Neutral）</td><td>只作语境底数，接口自己的措辞就明写不构成操作建议</td></tr>
  <tr><td>项目方一手发版：go-ethereum <code>v1.17.9</code>（10-21）、agave <code>v4.5.0-alpha.4</code> 与 <code>v4.4.0-rc.1</code>（均 10-26）</td><td>GitHub Releases API 可直接读，但只有自己跑节点才需要跟，且三条都不是安全版本公告</td></tr>
  <tr><td>币圈媒体转述一批：Ripple 诉赢银行后 XRP 未获提振、Robinhood Chain 募资 $2,600 万、Galaxy 季度盈利 $3.23 亿并回购 $2 亿、SoFi 加密毛收入 $1.62 亿、Zcash 联创提议终止 grants 补贴、CFTC 起诉犹他州并调查 Polymarket、Crypto.com 与 OG.com 向美国用户推 5 倍杠杆永续、日元稳定币首年脱锚、Circle 在 Solana 新铸 2.5 亿 USDC</td><td>全部只有三方媒体口径，未取监管方或项目方原文。<strong>其中「Robinhood 加密收入」两家直接冲突</strong>：TheBlock 写 Q3 涨 20%、PANews 写同比降 55%，两个都没核到，只能并列存疑</td></tr>
  <tr><td>阮一峰科技爱好者周刊第 416 期《编程已经面目全非》（10-27 11:02 北京）</td><td>同窗口重取能拿到，但<strong>昨日日报已报道过</strong>，按跨天去重口径不再进「值得」｜<a href="https://www.ruanyifeng.com/blog/2026/10/weekly-issue-416.html">ruanyifeng.com</a></td></tr>
</table>
</details>

<details>
<summary>来源健康度：25 个来源全绿、0 个 ERR，但有 2 条口径问题需要点名</summary>
<p>全量一轮 <code>--all --days 2 --seen/--append</code>：<code>fetched=310 fresh=174 sources=25 errors=0</code>，境内源（IT之家 25 条、美国主机侦探 7 条、v2ex 8 条、小众软件通道可取）与境外源（HN 25、lobsters 14、Product Hunt 15、CoinDesk 12、TheBlock 12、PANews 15）都通，可反证<strong>代理节点没有异常</strong>。</p>
<table>
  <tr><th style="text-align:left;">来源</th><th style="text-align:left;">本轮条数</th><th style="text-align:left;">状态</th></tr>
  <tr><td>hackernews / lobsters / v2ex</td><td>25 / 14 / 8</td><td>正常</td></tr>
  <tr><td>ithome / producthunt / panews</td><td>25 / 15 / 15</td><td>正常</td></tr>
  <tr><td>coindesk / theblock</td><td>12 / 12</td><td>正常</td></tr>
  <tr><td>coingecko / cgmarkets / cmc / fng</td><td>10 / 3 / 6 / 1</td><td>正常（行情轴全部落观察）</td></tr>
  <tr><td>binance-ann / exchange-status</td><td>3 / 1</td><td>正常（后者给出 Kraken <code>minor</code>，是本轮 🔥 的唯一来源）</td></tr>
  <tr><td>appstore-ios</td><td>6</td><td>正常（3 条现价 0 进值得，1 条 ¥98 判失效，1 条查不到 id、1 条兑换码型进观察）</td></tr>
  <tr><td>lowendbox / idcspy</td><td>2 / 7</td><td>正常（idcspy 全是聚合站转述，一条都没回商家官方页核到 → 全部落观察）</td></tr>
  <tr><td>epic-store</td><td><strong>0（fresh）</strong></td><td>需注意：不是故障。单取仍有 5 条且《Home》确为 0 元，根因是条目 id 不带日期、被 <code>--seen</code> 跨天挡死</td></tr>
  <tr><td>steam</td><td>6</td><td>需注意：价格经官方 API 五条全中，<strong>截止时间口径差 8 小时</strong>（UTC 被当北京输出），昨日已记、本轮未改脚本</td></tr>
  <tr><td>appinn / ruanyifeng / ethblog / creleases</td><td>各 0</td><td>正常：<code>errors=0</code> 说明抓取与解析都通，是被昨日去重（同窗口重取分别有 1 / 3 / 1 / 2 条）</td></tr>
  <tr><td>hf-daily-papers</td><td>0</td><td>需注意：论文条目的 <code>ts</code> 是 upvote 日期且普遍偏旧（本轮全在 10-11~10-25），在 <code>--days 2</code> 窗口里长期 0 条。要么放宽 <code>--days</code>，要么把它从「每日」挪到「每周」，本轮只点名不改</td></tr>
</table>
</details>

<details>
<summary>这一轮的四步口径（取数 → 验真 → 分级 → 落盘），以及边界</summary>
<p><strong>取数</strong>：一个脚本 25 个来源归一化成 NDJSON，跨天用 <code>state/history.jsonl</code> 去重，单源异常不拖垮整轮。</p>
<p><strong>验真</strong>：优惠、限免、免费额度三类一律回官方页二次确认价格与截止——Epic 回 <code>freeGamesPromotions</code>、Steam 回 <code>appdetails?cc=cn</code> 并读商店页正文、iOS 回 <code>itunes.apple.com/lookup</code> 按 <code>trackId</code> 核国区现价（认 id 不认名字）、交易所状态直接读各家 Statuspage API。核不到的一律降为观察并写明「未核实」，绝不用记忆里的数据补数。</p>
<p><strong>分级</strong>：🔥 紧急（距截止 ≤3 小时，或影响既有服务的免费额度被取消／资产下架）／⭐ 值得（已核实、本周内有效、能省钱或直接用于学习）／👀 观察（未核实或门槛高）／❌ 过滤（旧闻重推、软文、喊单与目标价）。币圈门槛更硬：行情、热搜、情绪指数一律落观察，只有直接影响在用资产可得性的公告才升 🔥；喊单、荐币、要连钱包的直接过滤，不写进任何段落。</p>
<p><strong>落盘</strong>：本地存档 <code>$INFO_HOME/daily/YYYY-MM-DD.md</code>（六段结构）＋ 本篇 Pages 稿。雷达＝取数 + 本地存档 + Pages 三段，缺一不算跑完。</p>
<p style="color:#8a9099;font-size:13px;">边界：全程只收集、核实、报告。不代注册、不代绑卡、不代领券、不代下单、不点任何购买或领取按钮；iOS 兑换码型限免不转载 <code>code=</code>，只留频道原帖由本人自取；币圈不连钱包、不签名、不导私钥、不代充代提、不给买卖建议与目标价，产物里不出现钱包地址、私钥、助记词与带 <code>ref=</code> 的邀请返利链接。</p>
</details>
