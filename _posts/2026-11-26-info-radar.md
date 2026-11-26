---
title: "资讯雷达 2026-11-26｜1Password 后端被入侵、BTC 先破 5.8 万再回 6.09 万、Steam 黑五 SILENT HILL f 新进"
author: OxYGC
date: 2026-11-26 12:05:00 +0800
last_modified_at: 2026-11-26 12:05:00 +0800
permalink: /posts/info-radar-2026-11-26/
categories: [Info, Deals]
tags: [资讯雷达, 1Password, Steam黑五, Epic限免, 比特币, GitHub趋势, SILENT HILL]
description: "2026-11-26 午间首稿（11:58–12:05）：25 源取回 354 条、15 源成功、9 源失败（v2ex、hf、binance、exstatus、coingecko、cgmarkets、cmc、ethblog、coindesk 均为 URLError / SSL_ERROR_SYSCALL）、PANews 返回 HTML 按异常单列。今天最近到期：Epic《深渊之印》¥55→0，11-27 00:00 收；《Bread and Fred》11-27 00:00 接档 0 元至 12-04 00:00。Steam 黑五换榜：SILENT HILL f -72% ¥83.44、SILENT HILL 2 & f 双作包 -65% ¥156.80（均 12-10）、底特律 -90% ¥13.60（12-01）、双人成行 -80% ¥39.60（12-04）。BTC 12:03 Gate.io 60,919.8（+2.80%，24h 低 57,300.1）；The Block 记录 11-26 01:26 曾跌破 5.8 万；恐惧贪婪 11（Extreme Fear）。HN 头条 1Password 安全事件 1,252 分，官方称客户密码库未受影响。"
---

这一轮取数在 2026-11-26 11:58–12:05（北京时间）完成：25 个来源里 15 个取到数据、9 个报错、1 个异常。`SUMMARY fetched=354 sources=25 errors=9 abnormal=1`。失败仍集中在需要境外 HTTPS 通道的接口——`v2ex`、`hf`、`binance`、`exstatus`、`coingecko`、`cgmarkets`、`cmc`、`ethblog`、`coindesk` 全部报 `URLError / SSL_ERROR_SYSCALL`，`panews` 的 RSS 地址返回的是站点 HTML 首页（约 108 KB、`text/html`，解析 0 条），按「异常」单列。HN 的 Firebase 端点在本地同样握手失败，因此本轮改用 HN 官方数据在 Algolia 的 `front_page` 索引取首页；行情用 Gate.io 公开 ticker 补位，这两项单独标注，不计入 25 源。

结论先摆前面：**今天有两个当天到点的截止。** 一是 Epic《深渊之印 / Mark of the Deep》0 元（原价 ¥55.00），**11-27 00:00 收**，按 12:05 计算还剩约 12 小时；二是同一时点接档的《Bread and Fred》（原价 ¥47.00）0 元档，**11-27 00:00 开、12-04 00:00 收**。Steam 黑五当前榜里，底特律 -90%（¥13.60，12-01 02:00 收）仍是幅度最大的一张，新进榜的 SILENT HILL f -72%（¥83.44）与 SILENT HILL 2 & f 双作包 -65%（¥156.80）都到 12-10 02:00。

今天真正占据技术头条的是 **1Password 安全事件**：官方博客 11-25 披露攻击者通过一名员工的 GitHub 账号进入后端系统，新增恶意代码并下载了部分客户账户资料，HN 以 **1,252 分 / 527 评论**居首。官方明确「客户密码库、库内条目与保护密钥未被访问」，主密码与 Secret Key 不在其服务器上；**请你以官方原文为准**，并警惕借事件伪装的钓鱼邮件。市场侧则相反方向剧烈：BTC 在 11-26 01:26 一度跌破 5.8 万美元（The Block 记录），到 12:03 Gate.io 又回到 **60,919.8（+2.80%）**，24 小时区间 57,300.1–61,633.8；恐惧贪婪指数仍是 **11（Extreme Fear）**。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮会过期、或需要你自己动手的条目</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:24%;">时点（北京时间）</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:20%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-27 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic《深渊之印 / Mark of the Deep》0 元领取永久入库</td>
<td style="padding:9px 8px 9px 0;">¥55.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">11-27 00:00 开</td>
<td style="padding:9px 8px 9px 0;">Epic《Bread and Fred》0 元档，至 12-04 00:00</td>
<td style="padding:9px 8px 9px 0;">¥47.00 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/zh-CN/free-games">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">12-01 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《底特律：化身为人》-90%、《博德之门 3》-30%</td>
<td style="padding:9px 8px 9px 0;">¥13.60 / ¥187.60</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1222140/?l=schinese">底特律</a> · <a href="https://store.steampowered.com/app/1086940/?l=schinese">博德之门3</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-04 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam《双人成行》-80%、《极限竞速：地平线 6》-25%</td>
<td style="padding:9px 8px 9px 0;">¥39.60 / ¥223.50</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a> · <a href="https://store.steampowered.com/app/2483190/?l=schinese">FH6</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#1a7f37;font-weight:700;">12-08 / 12-10 02:00 收</td>
<td style="padding:9px 8px 9px 0;">RDR2 -75%、GTA V 增强版 -56%、007 -50%、双影奇境 -40%；SILENT HILL f -72%、SH2 &amp; f 双作包 -65%</td>
<td style="padding:9px 8px 9px 0;">¥69.75 / ¥98.56 / ¥149.00 / ¥118.80 / ¥83.44 / ¥156.80</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/1174180/?l=schinese">RDR2</a> · <a href="https://store.steampowered.com/app/2947440/?l=schinese">SH f</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格为 2026-11-26 11:58–12:05 官方接口实测：Steam <code>featuredcategories?cc=cn&amp;l=schinese</code>，Epic <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code>。Steam 的 <code>discount_expiration</code> 为 epoch，已换算为北京时间（UTC+8）。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 值得看（5）

<details open>
<summary><strong>1Password 后端被入侵：攻击者经员工 GitHub 账号进入，客户密码库未受影响，HN 1,252 分</strong> ｜ <span style="color:#c0392b;font-weight:700;">今日头条</span> ｜ <span style="color:#1a7f37;font-weight:700;">官方公告</span></summary>
<p>1Password 于 2026-11-25 发布官方公告 <a href="https://1password.com/blog/update-on-nov-2026-security-incident">《Update on a security incident involving 1Password’s backend systems》</a>，HN 首页以 <strong>1,252 分 / 527 评论</strong>居首。按公告原文：11 月 19 日开始调查，攻击者先取得一名员工的公司 GitHub 账号，用该账号访问源码并向部分后端服务推送恶意代码，这些服务随后下载了「一部分客户」的账户资料。</p>
<p>官方列出的被下载字段包括：姓名与登录邮箱、账户与用户标识、账户创建与最近登录时间、公钥（本来就公开）、SRP 协议参数（不能用于登录）、某些邀请 / 开通 / 找回邮件链接中的 token，以及版本号、文件号这类非机密内部元数据。<strong>密码库内容、库内条目、保护密钥、账户恢复密钥、App 与浏览器扩展均未被访问</strong>；1Password 也不持有用户主密码与 Secret Key。</p>
<p><strong>怎么读</strong>：这是一次「后端账户资料 + 源码 / CI/CD」层面的入侵，不是密码库被解密。官方已禁用涉事 GitHub 账号、吊销被盗 token、轮换可能暴露的内部凭据，并把邀请与找回邮件里的一次性验证码从 6 位数字扩到 10 位字母数字。公告明确「你不需要在 1Password 里修改任何东西」，但<strong>要警惕冒充 1Password 的钓鱼邮件、邀请与账号找回请求</strong>。涉及主密码、Secret Key 的任何页面，只从官方 App 进入。</p>
</details>

<details open>
<summary><strong>Steam 黑五换榜：SILENT HILL f -72% 新进，底特律 -90% 仍是最大幅度，12-01 02:00 收</strong> ｜ <span style="color:#1a7f37;font-weight:700;">¥13.60 起</span> ｜ <span style="color:#c0392b;font-weight:700;">最近 12-01 02:00</span></summary>
<p>榜单由 <code>featuredcategories?cc=cn&amp;l=schinese</code> 返回 10 条，字段为 <code>final_price / original_price / discount_percent / discount_expiration</code>，全部按官方值换算，没有用媒体转述补价。与昨日午间相比，霍格沃茨之遗、Escapists 2、FH5、Hades / Hades II 下榜，SILENT HILL f、SILENT HILL 2 &amp; f 双作包、极限竞速：地平线 6 新进。</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏</th><th style="padding:6px 8px 6px 0;width:12%;">折扣</th><th style="padding:6px 8px 6px 0;width:26%;">现价 / 原价</th><th style="padding:6px 0 6px 0;width:20%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1222140/?l=schinese">底特律：化身为人</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-90%</td><td style="padding:8px 8px 8px 0;">¥13.60 / ¥136.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">12-01 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1426210/?l=schinese">双人成行</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-80%</td><td style="padding:8px 8px 8px 0;">¥39.60 / ¥198.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1174180/?l=schinese">Red Dead Redemption 2</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-75%</td><td style="padding:8px 8px 8px 0;">¥69.75 / ¥279.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2947440/?l=schinese">SILENT HILL f</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-72%</td><td style="padding:8px 8px 8px 0;">¥83.44 / ¥298.00</td><td style="padding:8px 0;">12-10 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1412913/?l=schinese">SILENT HILL 2 &amp; SILENT HILL f 双作包</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-65%</td><td style="padding:8px 8px 8px 0;">¥156.80 / ¥448.00</td><td style="padding:8px 0;">12-10 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3240220/?l=schinese">Grand Theft Auto V 增强版</a></td><td style="padding:8px 8px 8px 0;color:#c0392b;font-weight:700;">-56%</td><td style="padding:8px 8px 8px 0;">¥98.56 / ¥224.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3768760/?l=schinese">007 初露锋芒</a></td><td style="padding:8px 8px 8px 0;">-50%</td><td style="padding:8px 8px 8px 0;">¥149.00 / ¥298.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2001120/?l=schinese">双影奇境</a></td><td style="padding:8px 8px 8px 0;">-40%</td><td style="padding:8px 8px 8px 0;">¥118.80 / ¥198.00</td><td style="padding:8px 0;">12-08 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1086940/?l=schinese">博德之门 3</a></td><td style="padding:8px 8px 8px 0;">-30%</td><td style="padding:8px 8px 8px 0;">¥187.60 / ¥268.00</td><td style="padding:8px 0;color:#c0392b;font-weight:700;">12-01 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2483190/?l=schinese">极限竞速：地平线 6</a></td><td style="padding:8px 8px 8px 0;">-25%</td><td style="padding:8px 8px 8px 0;">¥223.50 / ¥298.00</td><td style="padding:8px 0;">12-04 02:00</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">榜单价即官方接口返回值；<code>discount_expiration</code> 换算后与北京时间整点对齐，说明这是 Steam 侧的固定活动截止，不是媒体估算。双作包在接口里是组合包，直链用 <code>/app/1412913</code>。进榜不等于史低，领取与付款前仍请回商店页确认。</p>
</details>

<details open>
<summary><strong>Epic 限免：《深渊之印》今晚 00:00 收，《Bread and Fred》明晚 00:00 接档 0 元</strong> ｜ <span style="color:#c0392b;font-weight:700;">12 小时内到期</span> ｜ <span style="color:#1a7f37;font-weight:700;">0 元</span></summary>
<p>Epic 的 <code>freeGamesPromotions?locale=zh-CN&amp;country=CN</code> 返回的 <em>Mark of the Deep</em> 价格结构为 <code>originalPrice=5500</code>（¥55.00）、<code>discountPrice=0</code>，促销区间 <code>2026-11-19T16:00:00Z → 2026-11-26T16:00:00Z</code>，换算北京时间即 <strong>11-20 00:00 至 11-27 00:00</strong>，按 12:05 计算还剩约 12 小时。</p>
<p><strong>下一档已经排上，但现在还不能领</strong>：<code>upcomingPromotionalOffers</code> 给出 <em>Bread and Fred</em>（原价 ¥47.00）在 <strong>11-27 00:00–12-04 00:00</strong> 的 0 元档期，状态是 SOON；此后 12-11 00:00 起还有一个 -40% 档期。另有 <em>Eternal Threads</em> 与 <em>Luftrausers</em> 在 <strong>11-28 00:00–12-01 23:00</strong> 的 <strong>-20%</strong> 档期（不是 0 元），不要把它们当成限免。</p>
<p>仍在进行的是 <em>TerraScape</em>：<code>originalPrice=5300</code>（¥53.00）、<code>discountPrice=3710</code>（¥37.10，-70%），区间 <strong>11-22 00:00 至 12-22 00:00</strong>。另有一款标价 <code>0 → 0</code> 的长期免费本体，属于常态免费，不按限时折扣记录。Epic 页面对 curl 有 403 风控，链接用官方商店，领取请在浏览器里自行完成。</p>
</details>

<details open>
<summary><strong>行情：BTC 先跌破 5.8 万再回到 6.09 万，24 小时 +2.80%，恐惧贪婪仍是 11</strong> ｜ <span style="color:#1a7f37;font-weight:700;">+2.80%</span> ｜ <span style="color:#8a9099;">Gate.io 单源 + The Block 侧证</span></summary>
<p>可用的公开行情源本轮只剩 Gate.io：<code>/spot/tickers?currency_pair=BTC_USDT</code> 在 <strong>12:03:48</strong> 报 BTC <strong>60,919.8</strong>，24 小时 <strong>+2.80%</strong>，区间 <strong>57,300.1 – 61,633.8</strong>，成交额约 <strong>12.64 亿 USDT</strong>（21,312.58 BTC）。同一快照 ETH <strong>1,702.19</strong>（+2.55%，低 1,609.05）、BNB <strong>560.10</strong>（+3.32%）、SOL <strong>71.22</strong>（+3.15%）。</p>
<p>据 The Block 11-25 17:26 UTC（北京 11-26 01:26）的报道 <a href="https://www.theblock.co/news/markets/2026-11-25-bitcoin-falls-below-58000-coinshares-butterfill-sees-tail-end-bear-market-446678">Bitcoin falls below $58,000 as CoinShares’ Butterfill sees ‘tail end of the bear market’</a>，BTC 在夜间确实跌到 5.8 万下方，与 Gate.io 记录的低点 57,300.1 方向一致；到午间又回升到 6.09 万上方，较高点 61,633.8 略有回落。情绪侧，alternative.me 恐惧贪婪指数为 <strong>11（Extreme Fear）</strong>，时间戳 2026-11-26 08:00（北京时间），仍处极度恐惧区间。</p>
<p><strong>口径说明</strong>：CoinGecko、CoinMarketCap、Binance 主 API、OKX、Bybit、Bitget、Coinbase、Kraken 本轮全部被境外通道挡住，因此只有 Gate.io 一个直接行情源，The Block 仅作方向侧证，<strong>不做双源交叉校验</strong>。行情只作时刻记录，不构成买卖建议，也不写支撑位与目标价。</p>
</details>

<details open>
<summary><strong>Google 公开整数分解 / 离散对数研究论文合集，HN 461 分；同时 Anthropic 的 GRH Lean 形式化登上首页</strong> ｜ <span style="color:#1a7f37;font-weight:700;">官方仓库</span> ｜ <span style="color:#8a9099;">HN 461 / 341</span></summary>
<p>HN 首页第三条是 <a href="https://github.com/google-research/google-research/tree/master/cogentic_research_papers">Google releases Cogentic papers on integer factorization, discrete logs and more</a>，<strong>461 分 / 341 评论</strong>。链接指向 <code>google-research</code> 官方仓库下的论文目录，属于一手材料而不是媒体转述。同一时段第五条是 <a href="https://github.com/lsernau/grh-lean">Much shorter version of GRH Lean verification from Anthropic</a>，<strong>328 分 / 162 评论</strong>，同样是指向形式化验证仓库的技术条目。</p>
<p><strong>怎么读</strong>：这两条的价值在于「可点开原文与代码」，而不是标题里的结论。整数分解与离散对数直接关系到 RSA、DH 等公钥体系的安全假设，但<strong>论文标题不等于算法已被实际攻破</strong>；本站没有复现、没有跑基准，因此不转载任何「某种密码学要完了」的解读。需要判断影响面时，请回论文与代码逐项核对参数、复杂度与实验条件。</p>
</details>

## 观察（核不到官方截止或价格，不进「值得」）

<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:32%;">条目</th><th style="padding:7px 8px 7px 0;width:30%;">拿到的事实</th><th style="padding:7px 0;">为什么停在观察</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/722.htm">铠侠与英伟达合作，探索将 GPU 有效显存扩展至 PB 级</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 12:00</td><td style="padding:7px 0;">媒体转述合作方向，未回两家官方公告核时间表与产品形态</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/720.htm">泰坦军团规划 24.5" 1200Hz IPS、27" 三模 QD-OLED 显示器</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 11:54</td><td style="padding:7px 0;">「规划」属传闻，未回厂商页核型号、价格与上市时间</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/719.htm">世界最长公路水下盾构隧道成功穿越长江</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 11:53</td><td style="padding:7px 0;">工程进展，不是消费折扣；未回建设单位公告</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/718.htm">腾讯《英雄联盟电竞经理》2027-01-26 停运，今日起停止充值与新注册</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 11:52</td><td style="padding:7px 0;">停运公告经媒体转述，未回游戏官网核补偿方案</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/716.htm">报告称 SpaceX 降价出租 AI 算力，降幅约 20%~35%</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 11:50 引述报告</td><td style="padding:7px 0;">未回 SpaceX / xAI 官方价目表，降幅口径不明</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.ithome.com/1/032/714.htm">中国牵头制定的人工智能训练数据质量国际标准成欧洲多国参考</a></td><td style="padding:7px 8px 7px 0;">IT之家 11-26 11:47</td><td style="padding:7px 0;">未回标准组织原文核编号与适用范围</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://lowendbox.com/blog/sneak-peak-serverhosts-black-friday-vanishing-vps-offers-rise-1-a-day-starting-november-28/">ServerHost 黑五 VPS：11-28 起每天涨 1 美元</a></td><td style="padding:7px 8px 7px 0;">LowEndBox 11-25 20:00</td><td style="padding:7px 0;">「每天涨 1 美元」是商家预告，未回 ServerHost 官网核库存与最终价</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170965.html">ColoCrossing 黑五：美国 VPS 年付低至 $17.99</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-25 17:56</td><td style="padding:7px 0;">未回 ColoCrossing 官方页核机型、带宽与续费价</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170935.html">CloudCone 黑五：SSD VPS 低至 $13.89/年，续费同价</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-25 15:21</td><td style="padding:7px 0;">「续费同价」需回官方购物车与条款复核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170954.html">HawkHost 黑五：虚拟主机低至 $1.46/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-25 16:48</td><td style="padding:7px 0;">未核首期价、续费价与资源上限</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170919.html">UltaHost 黑五：主机及 VPS 最高 70% 折扣，低至 $2.01/月</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-24 16:21</td><td style="padding:7px 0;">未回官方页核机型、续费价与截止</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;"><a href="https://www.idcspy.com/170983.html">SocialEcho 黑五：充 $99 送 $10，最高赠送 $1688</a></td><td style="padding:7px 8px 7px 0;">idcspy 11-26 10:09</td><td style="padding:7px 0;">充值赠送属站内活动，未核使用门槛与有效期</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">App Store 国区新上架免费应用 108 条（PicMind、MirrorSync、Athlete OS、Calm Spaces 等）</td><td style="padding:7px 8px 7px 0;">iTunes 中国区 <code>newapplications</code> 接口 108 条</td><td style="padding:7px 0;">新上架 ≠ 限时免费；Apple 不公布限免截止，不补日期</td></tr>
<tr><td style="padding:7px 8px 7px 0;">Product Hunt 今日新品：Falcon by Vybe、Canva MCP、3way.Social MCP、eluna、Blink、Airbot、CodeRabbit Verify 等</td><td style="padding:7px 8px 7px 0;">Product Hunt feed 20 条，时间到 11-26 11:01</td><td style="padding:7px 0;">只作产品发现，不评优劣，也未逐个核定价与可用性</td></tr>
</tbody></table>

## 资讯面：HN、Lobsters、IT之家、阮一峰与 Product Hunt

<p><strong>HN 首页（11:58 读数，Algolia <code>front_page</code>）</strong>：除 1Password 与 Google 论文外，<a href="https://scottaaronson.blog/?p=10379">Scott Aaronson《Holy shit…: The magnitude of what’s now happening》</a> <strong>1,048 分 / 888 评论</strong>居第二，属于个人博客观点而非官方结论；<a href="https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts">去 Home Depot 蓄水池浮潜的采访</a> 452 分 / 111 评论；<a href="https://github.com/lsernau/grh-lean">GRH Lean 形式化</a> 328 分 / 162 评论；<a href="https://github.com/xoxorwr/pw-loudness-eq">Windows 响度均衡逆向并移植到 PipeWire</a> 324 分 / 182 评论；<a href="https://bjin.github.io/go-codegolf-benchmark/#leaderboard">GPT-6.2 Astra 打破 Google 员工 code golf 纪录</a> 281 分 / 80 评论；<a href="https://modaic.dev/blog/latency-doesnt-lie">Jev 大概是 Qwen3.5-35B-A3B</a> 257 分 / 74 评论；<a href="https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features">NYT 提醒摄影师别急着更新 Photoshop</a> 250 分 / 201 评论；<a href="https://jayd.ml/2026/11/14/rockbox-on-yp3.html">把 Rockbox 移植到 9 美元的 YP3 MP3</a> 237 分 / 95 评论；<a href="https://s.conao3.com/blog/2026/e4f733">用 Lean 检查 Clojure core 发现 17 个未上报 bug</a> 197 分 / 69 评论；<a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">Ubuntu 安全响应偏慢</a> 176 分 / 87 评论。</p>

<p><strong>Lobsters（按分数）</strong>：<a href="https://fzakaria.com/2026/11/23/2035-came-early">2035 came early</a> 126 分；<a href="https://www.marginalia.nu/log/a_141_marginalia_update/">Marginalia Search 的更新</a> 103 分；<a href="https://s.conao3.com/blog/2026/e4f733">Clojure core 的 17 个 bug</a> 81 分；<a href="https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/">iOS 为何仍没有 WebKit 之外的浏览器</a> 80 分；<a href="https://hex.pm/blog/security-incident-on-hexpm">Hex.pm 安全事件</a> 76 分；<a href="https://wheybags.com/blog/pokemon_childhood_version.html">Pokemon Childhood Version</a> 73 分；<a href="https://lucumr.pocoo.org/2026/11/25/poisoning/">Abolish Lock Poisoning</a> 46 分 / 74 评论；<a href="https://donsz.nl/blog/optimizing-rustcs-next-trait-solver">优化 rustc 的下一代 trait solver</a> 45 分；<a href="https://servo.org/blog/2026/11/25/october-in-servo/">Servo 十月进展</a> 40 分。</p>

<p><strong>IT之家（最新条目到 11-26 12:00 北京时间）</strong>：值得记的有<a href="https://www.ithome.com/1/032/722.htm">铠侠与英伟达合作探索 PB 级 GPU 有效显存</a>、<a href="https://www.ithome.com/1/032/720.htm">泰坦军团规划 24.5" 1200Hz IPS 与 27" 三模 QD-OLED</a>、<a href="https://www.ithome.com/1/032/719.htm">世界最长公路水下盾构隧道穿越长江</a>、<a href="https://www.ithome.com/1/032/718.htm">《英雄联盟电竞经理》2027-01-26 停运</a>、<a href="https://www.ithome.com/1/032/716.htm">SpaceX 降价出租 AI 算力</a>、<a href="https://www.ithome.com/1/032/714.htm">中国牵头 AI 训练数据质量国际标准</a>、<a href="https://www.ithome.com/1/032/709.htm">技嘉 G27Q36 电竞显示器 1999 元</a>、<a href="https://www.ithome.com/1/032/707.htm">宇宙中性氢 21 厘米信号直接探测</a>、<a href="https://www.ithome.com/1/032/655.htm">Anthropic 阿莫迪回应「人类将控制权交给 AI」说法</a>、<a href="https://www.ithome.com/1/032/642.htm">支付宝上线「长辈守护中心」</a>、<a href="https://www.ithome.com/1/032/630.htm">TCL 华星展示 10000nits 手机 OLED</a>。以上均为媒体转述，未逐条回官方公告，不进「值得」。</p>

<p><strong>阮一峰周刊</strong>：最新一期仍是<a href="https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html">第 420 期《最分心的一年》</a>，feed 更新时间 2026-11-26 10:16 北京时间（比昨天又有刷新）；前两期是第 419 期《机房来了，写字楼走了》、第 418 期《如果科技停止在21世纪初》。周更节奏，本轮只有这 3 条。</p>

<p><strong>Product Hunt</strong>：最新 feed 里可读的有 <a href="https://www.producthunt.com/products/vybe-4">Falcon by Vybe</a>、<a href="https://www.producthunt.com/products/canva">Canva MCP</a>、<a href="https://www.producthunt.com/products/3way-social">3way.Social MCP</a>、<a href="https://www.producthunt.com/products/eluna">eluna</a>、<a href="https://www.producthunt.com/products/blink-35">Blink</a>、<a href="https://www.producthunt.com/products/airbots">Airbot</a>、<a href="https://www.producthunt.com/products/koed">Koed</a>、<a href="https://www.producthunt.com/products/coderabbit">CodeRabbit Verify</a>、<a href="https://www.producthunt.com/products/magi-1">MAGI-2</a>。只作产品发现，不评优劣。</p>

<p><strong>Appinn</strong>：除 1Password 事件外，本轮可读的有<a href="https://www.appinn.com/open-source-ime-boom-and-stability/">开源输入法的大爆发与稳定性（5 款对比）</a>、<a href="https://www.appinn.com/yzwpdfview/">YzwPDFView 大雁 PDF（89KB 单文件查看器）</a>、<a href="https://www.appinn.com/xnulinux/">xnulinux：不用虚拟机在 Linux 里跑完整 macOS</a>、<a href="https://www.appinn.com/ladybird-browser/">Ladybird：不用 Chromium 的独立内核浏览器</a>。工具类内容只作线索，未在本地验证兼容性与安全性。</p>

<p><strong>GitHub Trending（11:58 抓取 16 条）</strong>：star 与「今日新增」均为页面读数，不是官方增量接口。</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:40%;">仓库</th><th style="padding:7px 8px 7px 0;width:18%;">总 star</th><th style="padding:7px 8px 7px 0;width:16%;">今日新增</th><th style="padding:7px 0;">说明</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">elementalsouls/Claude-BugHunter</td><td style="padding:7px 8px 7px 0;">23,210</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,652</td><td style="padding:7px 0;">Claude Code 漏洞狩猎技能包</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">firecrawl/firecrawl</td><td style="padding:7px 8px 7px 0;">210,181</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,135</td><td style="padding:7px 0;">Agent 抓取 / 搜索基础设施</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">HKUDS/CLI-Anything</td><td style="padding:7px 8px 7px 0;">65,788</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,106</td><td style="padding:7px 0;">把软件做成 Agent 可调用的 CLI</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">cathrynlavery/diagram-design</td><td style="padding:7px 8px 7px 0;">73,182</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+1,141</td><td style="padding:7px 0;">图表 / 版式设计资源</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">mvanhorn/last30days-skill</td><td style="padding:7px 8px 7px 0;">75,213</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+945</td><td style="padding:7px 0;">跨 Reddit / X / YouTube 的研究技能</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">obra/superpowers</td><td style="padding:7px 8px 7px 0;">326,735</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+903</td><td style="padding:7px 0;">Agentic skills 框架</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">jingyaogong/minimind</td><td style="padding:7px 8px 7px 0;">71,119</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+826</td><td style="padding:7px 0;">两小时从 0 训 64M 小模型</td></tr>
<tr><td style="padding:7px 8px 7px 0;">XiaoYouChR/Ghost-Downloader-3</td><td style="padding:7px 8px 7px 0;">18,392</td><td style="padding:7px 8px 7px 0;color:#1a7f37;">+951</td><td style="padding:7px 0;">桌面下载器</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">其余进榜：zhouxiaoka/autoclip（16,312，+880）、mjmirza/app-store-compliance（6,570，+858）、toeverything/AFFiNE（78,568，+574）、cursor/plugins（19,577，+416）、google-labs-code/stitch-skills（13,026，+355）、Tracer-Cloud/opensre（15,565，+348）、openvinotoolkit/openvino（12,677，+191）、nginx/nginx（33,398，+176）。与昨日午间相比，Claude-BugHunter 从 21,679 涨到 23,210（+1,531），Agent Skills 与下载 / 剪辑工具仍占前排。</p>

## 币圈与安全：BTC 跌破 5.8 万后的反弹、监管推进与算力劫持

<p><strong>资金与价格</strong>：The Block 记录 <a href="https://www.theblock.co/news/markets/2026-11-25-bitcoin-falls-below-58000-coinshares-butterfill-sees-tail-end-bear-market-446678">BTC 跌破 5.8 万美元</a>，CoinShares 的 Butterfill 称处于「熊市尾端」；同一时段 <a href="https://www.theblock.co/news/business/2026-11-25-bit-digital-repays-50-million-to-galaxy-after-selling-29825-eth-446164">Bit Digital 卖出 29,825 ETH 向 Galaxy 偿还 5,000 万美元</a>、<a href="https://www.theblock.co/news/business/2026-11-25-fidelity-chainlink-etf-nasdaq-listing-446735">Fidelity 申请现货 Chainlink ETF</a>、<a href="https://www.theblock.co/news/markets/2026-11-25-franklin-templeton-ezpz-etf-adds-hyperliquid-hype-446686">Franklin Templeton 的 EZPZ ETF 纳入 HYPE</a>。这些是机构持仓与产品申报新闻，不是买卖建议，也不构成对价格的预测。</p>

<p><strong>监管</strong>：<a href="https://www.theblock.co/news/regulation/2026-11-25-house-committee-advances-strategic-bitcoin-reserve-bill-446778">美国众议院委员会推进「战略比特币储备」法案</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-warren-van-hollen-lead-push-scrap-sec-regulation-crypto-innovation-exemption-446756">Warren 与 Van Hollen 推动取消 SEC 的 crypto 创新豁免</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-justice-department-takes-aim-billions-crypto-fraud-proceeds-largest-ever-crackdown-446711">司法部针对数十亿美元加密欺诈所得展开「史上最大规模」执法</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-novatech-founders-ordered-pay-1-3-million-crypto-ponzi-scheme-haitian-investors-446643">NovaTech 创始人被判赔 13 亿美元</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-ukraine-passes-crypto-market-law-with-332-million-revenue-target-446182">乌克兰通过加密市场法案</a>。</p>

<p><strong>安全</strong>：<a href="https://www.theblock.co/news/ecosystems/2026-11-25-bitcoin-miners-hit-hashrate-hijacking-attack-exploiting-unencrypted-connections-446723">比特币矿工遭「算力劫持」攻击，利用未加密连接</a>；<a href="https://www.theblock.co/news/regulation/2026-11-25-nvidia-290-million-settlement-crypto-mining-class-action-446709">英伟达就加密挖矿披露集体诉讼达成 2.9 亿美元和解</a>。技术面另有 1Password 事件的官方公告（见上）。涉及矿机管理面与凭据的操作，请按厂商公告与自有资产自查，本站不代为扫描或执行命令。</p>

<p><strong>PANews 本轮异常</strong>：RSS 地址 <code>panewslab.com/rss</code> 返回的是站点 HTML 页面（约 108 KB、<code>text/html</code>），不是 XML feed，解析为 0 条，按「异常」单列，不计入 9 个 URLError。Coindesk、The Ethereum Blog 同样未被通道放行，因此本轮没有它们的原文；<code>creleases</code>（geth releases）取到 8 条，但最新仍是 v1.17.10（2026-10-23），本轮没有新版本。</p>

<p style="margin:34px 0 6px;padding-top:16px;border-top:2px solid #e3e6ea;font-size:16px;font-weight:700;color:#1f2329;">取数与异常</p>

<p>本轮按 <code>info-task-gc</code> 的 25 源口径分三组执行，成功 15 源、异常 1 源、报错 9 源，合计 <strong>fetched=354 / sources=25 / errors=9 / abnormal=1</strong>。</p>

<p><strong>源健康度（11:58–12:05）</strong>：</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:7px 8px 7px 0;width:14%;">组</th><th style="padding:7px 8px 7px 0;width:48%;">成功</th><th style="padding:7px 0;">失败 / 异常</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">news（8）</td><td style="padding:7px 8px 7px 0;">6 源 / 154 条：hn 30、lobsters 25、github-trending 16、ruanyifeng 3、ithome 60、producthunt 20</td><td style="padding:7px 0;color:#c0392b;">v2ex、hf（URLError）</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:7px 8px 7px 0;">deal（6）</td><td style="padding:7px 8px 7px 0;">6 源 / 170 条：epic 12、steam 10、appinn 10、lowendbox 20、idcspy 10、appstore 108</td><td style="padding:7px 0;color:#1a7f37;">全绿</td></tr>
<tr><td style="padding:7px 8px 7px 0;">crypto（11）</td><td style="padding:7px 8px 7px 0;">3 源 / 30 条：creleases 8、fng 2、theblock 20</td><td style="padding:7px 0;color:#c0392b;">binance、exstatus、coingecko、cgmarkets、cmc、ethblog、coindesk（URLError）；panews（HTML，0 条）</td></tr>
</tbody></table>
<p style="font-size:12.5px;color:#6b7280;margin:10px 0 0;">合计 <code>354 = 154 + 170 + 30</code>；取数窗口 2026-11-26 11:58–12:05（北京时间）。<code>appstore</code> 本轮返回国区新上架 108 条，是「新上架」而不是限免价格层。<code>hn</code> 经 Algolia <code>front_page</code> 索引取得（Firebase 端点握手失败），行情由 Gate.io 公开 ticker 补位，两项均为替代通道，不计入 25 源。</p>

<p><strong>形态判断</strong>：9 个失败里 8 个是境外 HTTPS 接口的 <code>SSL_ERROR_SYSCALL</code> 或连接超时，另一个 <code>exstatus</code> 是页面型接口未放行；<code>panews</code> 返回 HTML 属站点 RSS 形态变化，不是通道问题。除 <code>panews</code> 外，本轮没有 4xx / 410 类源站下线信号，因此不判断这些站点本身不可用。</p>

<p><strong>口径与边界</strong>：四步口径不变：取数（25 源，NDJSON 归一化）→ 验真（价格与截止回官方接口或原文，核不到就降观察并写「未核实」）→ 分级（🔥 / ⭐ / 👀 / ❌，宁严勿松）→ 落点（本地存档 + 本篇 Pages 稿）。边界：只收集与报告，不注册、不绑卡、不代领券、不下单；iOS 兑换码型不转载兑换码；币圈不连钱包、不签名、不导私钥、不代充代提，不写买卖建议与目标价；产物内不出现钱包地址与带邀请返利参数的链接。</p>

<p>如实记两句：<strong>本轮执行环境仍未挂载 <code>info-task-gc</code> 技能文件</strong>，因此按仓库既有稿件的 25 源清单与同一口径执行，源名单、四步流程与边界均与 11-23 / 11-24 / 11-25 各稿一致；<strong>GitHub 连接器未以 MCP 形式挂载</strong>，仓库读写通过既有 git 凭据与 <code>origin/main</code> 远端完成，本篇为 2026-11-26 当天唯一文件，后续同日复跑只在本文件内更新。</p>

<p style="margin:28px 0 0;font-size:14px;color:#4b5158;">本文所有价格、折扣与截止时间均来自 2026-11-26 11:58–12:05 接口实际返回，价格随时可能变动，领取与下单前请以官方页面为准。行情只作时刻快照，且本轮仅有 Gate.io 单源，不构成任何投资建议；新闻部分请注意「媒体转述」与「公司公告 / 官方接口」的区别。</p>
