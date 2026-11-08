---
title: "资讯雷达 2026-11-08｜Epic 两篇到 11-13；Steam 榜单换血、1211600 更正为《隔离区》；Agent Skills 仓库热度未退"
author: OxYGC
date: 2026-11-08 16:05:00 +0800
permalink: /posts/info-radar-2026-11-08/
categories: [Info, Deals]
tags: [资讯雷达, Epic限免, Steam折扣, OpenSSH, AI动态, 币圈, GitHub趋势]
description: "2026-11-08 三轮更新：16:03–16:05 重新取数，Steam 特别优惠榜 10 条换血并把 appid 1211600 正式名更正为《隔离区-丧尸末日生存》；Epic 两篇限免仍在效、LISA 现价 -60% 到 11-10 14:59；GitHub Trending 四个 Agent Skills 仓库热度与 15:24 持平。行情接口继续不可用。"
---

这一轮跑了 13 个来源，抓回约 110 条，6 个源或接口失败。形状和前几天一样：**Epic、Steam 这些福利位没有新货，全是回到官方接口把仍在效期的重新核一遍**；真正有新信息的是安全侧——OpenSSH 10.6p2 的发布说明确认了一个可绕过密码验证的问题，只影响 musl libc 且关闭 PAM 的 Linux（典型是部分 Alpine）。行情侧今天不交白卷也不硬编：CoinGecko、Binance、Coinpaprika 三个接口本轮全部连不上，BTC/ETH 报价这栏只能留空。16:05 又做了一轮只读复核，变化集中在 Steam 榜单换血与一处 appid 名称更正，见下方最新的第三轮。

<div style="border:1px solid #e3e6ea;border-radius:10px;padding:16px 18px;background:#fbfcfd;margin:0 0 28px;">
<strong style="font-size:15px;">这一轮真正会过期、或需要你自己动手的只有这几条</strong>
<table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;width:26%;">时点</th><th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:16%;">价格</th><th style="padding:6px 0 6px 0;width:20%;">去哪</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-13 00:00 收</td>
<td style="padding:9px 8px 9px 0;">Epic 本周限免<strong>两篇</strong>：《浮游世界》+《Idle Champions of the Forgotten Realms》</td>
<td style="padding:9px 8px 9px 0;">《浮游世界》原价 ¥75 → 0 元</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#c0392b;font-weight:700;">11-10 01:00 / 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam 国区：R.E.P.O.、007 初露锋芒（昨日已报，本轮复核仍在效期）</td>
<td style="padding:9px 8px 9px 0;">¥22.75 / ¥202.80</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/3241660/">R.E.P.O.</a> · <a href="https://store.steampowered.com/app/3768760/">007</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;">11-13 02:00 收</td>
<td style="padding:9px 8px 9px 0;">Steam 国区：人类一败涂地、PEAK（PEAK 到 11-15 18:00）</td>
<td style="padding:9px 8px 9px 0;">¥17.40 / ¥20.46</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.steampowered.com/app/477160/">人类一败涂地</a></td></tr>
<tr style="border-bottom:1px solid #eef0f2;">
<td style="padding:9px 8px 9px 0;color:#6b7280;">11-10 14:59 收</td>
<td style="padding:9px 8px 9px 0;">Epic《LISA: Definitive Edition》-60%（16:03 复核在效）</td>
<td style="padding:9px 8px 9px 0;">¥108.00 → ¥64.80</td>
<td style="padding:9px 0 9px 0;"><a href="https://store.epicgames.com/">store.epicgames.com</a></td></tr>
<tr>
<td style="padding:9px 8px 9px 0;color:#8a9099;">官方不设「截止」</td>
<td style="padding:9px 8px 9px 0;">OpenSSH 10.6p2 / Alpine 官方公告：musl + 关闭 PAM 的 sshd 可被绕过密码验证，<strong>今天就该升，升完还要重启 sshd</strong></td>
<td style="padding:9px 8px 9px 0;">免费升级</td>
<td style="padding:9px 0 9px 0;"><a href="https://www.alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">alpinelinux.org</a> · <a href="https://www.openssh.com/txt/release-10.6p2">openssh.com</a></td></tr>
</tbody></table>
<p style="font-size:12px;color:#8a9099;margin:12px 0 0;">价格与截止均为 2026-11-08 14:57–15:05 实测，补录 15:20–15:30，第三轮 16:03–16:05 复核。本站只报道与核实，注册、登录、领取、下单全部由你自己完成。</p>
</div>

## 16:03–16:05 第三轮复核（4 条）

<p>15:30 那版之后又跑了一轮只读取数：Epic 促销接口、Steam <code>featuredcategories</code>、GitHub Trending 日榜、CoinGecko 与 HN 各打一次。结论先说：<strong>没有新的免费游戏，但 Steam 特别优惠榜换了一条，且昨天榜里那个「ZED ZONE」是错的 appid 名称，今天连带更正</strong>；Epic 那边《LISA》的当前折扣也值得单独拎出来。安全侧没有新增，OpenSSH 10.6p2 / Alpine 的结论不变。</p>

<details open>
<summary><strong>Steam 特别优惠榜重新取数：10 条在效，appid 1211600 应叫《隔离区-丧尸末日生存》</strong> ｜ 含名称更正 ｜ 仅列表接口</summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">游戏（appid）</th><th style="padding:6px 8px 6px 0;">国区价</th><th style="padding:6px 8px 6px 0;">折扣</th><th style="padding:6px 0 6px 0;width:24%;">截止（北京时间）</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3768760/">007 初露锋芒</a>（3768760）</td><td style="padding:8px 8px 8px 0;">¥338.00 → ¥202.80</td><td style="padding:8px 8px 8px 0;">-40%</td><td style="padding:8px 0 8px 0;">11-10 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3241660/">R.E.P.O.</a>（3241660）</td><td style="padding:8px 8px 8px 0;">¥35.00 → ¥22.75</td><td style="padding:8px 8px 8px 0;">-35%</td><td style="padding:8px 0 8px 0;">11-10 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1345940/">Dying Light Essentials Edition</a>（1345940）</td><td style="padding:8px 8px 8px 0;">¥98.00 → ¥9.80</td><td style="padding:8px 8px 8px 0;">-90%</td><td style="padding:8px 0 8px 0;">11-10 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1943950/">Escape the Backrooms</a>（1943950）</td><td style="padding:8px 8px 8px 0;">¥37.00 → ¥29.60</td><td style="padding:8px 8px 8px 0;">-20%</td><td style="padding:8px 0 8px 0;">11-10 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/2223980/">Nomad Drive</a>（2223980）</td><td style="padding:8px 8px 8px 0;">¥54.00 → ¥48.60</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">11-11 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/4348910/">深空当铺：可能是偷的</a>（4348910）</td><td style="padding:8px 8px 8px 0;">¥55.00 → ¥49.50</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">11-12 01:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/477160/">人类一败涂地</a>（477160）</td><td style="padding:8px 8px 8px 0;">¥58.00 → ¥17.40</td><td style="padding:8px 8px 8px 0;">-70%</td><td style="padding:8px 0 8px 0;">11-13 02:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/3527290/">PEAK</a>（3527290）</td><td style="padding:8px 8px 8px 0;">¥33.00 → ¥20.46</td><td style="padding:8px 8px 8px 0;">-38%</td><td style="padding:8px 0 8px 0;">11-15 18:00</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/5266240/">Potato Please</a>（5266240）</td><td style="padding:8px 8px 8px 0;">¥35.00 → ¥31.50</td><td style="padding:8px 8px 8px 0;">-10%</td><td style="padding:8px 0 8px 0;">11-16 02:00</td></tr>
<tr><td style="padding:8px 8px 8px 0;"><a href="https://store.steampowered.com/app/1211600/">隔离区-丧尸末日生存</a>（1211600）</td><td style="padding:8px 8px 8px 0;">¥48.00 → ¥28.80</td><td style="padding:8px 8px 8px 0;">-40%</td><td style="padding:8px 0 8px 0;">11-20 02:00</td></tr>
</tbody></table>
<p><strong>更正</strong>：15:25 那版把 appid <code>1211600</code> 写成了「ZED ZONE」，这是错的。16:04 重新取列表接口，<code>1211600</code> 的 <code>name</code> 字段是《隔离区-丧尸末日生存》，并用 <code>appdetails</code> 单独核到 <code>price_overview</code>：¥48.00 → ¥28.80、-40%，与列表一致。此前正文「Steam 特别优惠榜全量 10 条」里的 ZED ZONE 一条作废，以本表为准；观察区里写的「隔离区 -40%」反而是对的。榜单本身也换了一条：上一版 10 条里的 ZED ZONE 不再出现，本轮 10 条就是上表。</p>
<p style="font-size:13px;color:#6b7280;">取法：<code>store.steampowered.com/api/featuredcategories?cc=cn&amp;l=schinese</code> 的 <code>specials.items</code>，价格取 <code>original_price</code>/<code>final_price</code>（单位分），截止取 <code>discount_expiration</code> 并换算为北京时间；核实于 2026-11-08 16:04。<strong>边界</strong>：除 1211600 外，其余 9 条本轮没有再逐款回 <code>appdetails</code> 核价——3241660 的单款请求在 16:04 超时（20 秒无响应），说明逐款复核仍被限流；付款前请以商店页为准。Dying Light（1345940）此前 <code>appdetails</code> 返回过另一款游戏，这条只保留列表接口的口径。</p>
</details>

<details>
<summary><strong>Epic 复核：两篇限免仍在效；《LISA》当前 -60% 到 11-10 14:59</strong> ｜ 一条现货，一条提前记档</summary>
<p>免费位没变：《浮游世界》与《Idle Champions of the Forgotten Realms》都还是 0 元，<code>endDate</code> 均为 <code>2026-11-12T16:00:00.000Z</code>，即 <strong>11-13 00:00 截止</strong>，领了永久入库。另有两条现在就能买到的折扣：<strong>《LISA: Definitive Edition》-60%，¥108.00 → ¥64.80，截止 11-10 14:59</strong>（<code>2026-11-10T06:59:00.000Z</code>）；这条此前只在观察区按「12 月再折 -55%」记过排期，当前这轮 -60% 反而更低。</p>
<p>后续排期再核一遍，时间换算成北京时间：<strong>《斗阵骑士 Knightica》11-13 00:00 至 11-20 00:00 免费</strong>；<strong>TerraScape 11-22 00:00 至 12-22 00:00 -70%</strong>；<strong>《幽灵行者 2》12-11 01:00 起 -20%</strong>；<strong>《纪念碑谷》12-11 00:00 起 -35%</strong>；<strong>《LISA》12-11 00:00 起再折 -55%</strong>。都是 <code>upcomingPromotionalOffers</code> 里的未来排期，现在领不到、也还没生效，只做提前记档。</p>
<p style="font-size:13px;color:#6b7280;">出处：Epic 官方 <code>freeGamesPromotions</code> 接口（<code>locale=zh-CN&amp;country=CN</code>），核实于 2026-11-08 16:03。边界：<code>originalPrice</code> 是接口给的当前原价，不保证是历史最低；促销时间以接口的 UTC 时间为准，页面上的倒计时可能因时区显示不同。</p>
</details>

<details>
<summary><strong>GitHub Trending 16:04 快照：四个 Agent Skills 仓库热度与 15:24 持平</strong> ｜ 热度快照，不是推荐</summary>
<p>日榜 15 条里，<a href="https://github.com/cloudflare/security-audit-skill">cloudflare/security-audit-skill</a> 仍是 +2,085、<a href="https://github.com/mattpocock/skills">mattpocock/skills</a> +1,100、<a href="https://github.com/google/skills">google/skills</a> +443、<a href="https://github.com/anthropics/skills">anthropics/skills</a> +390，与 15:24 那版数字一致。其余上榜：<a href="https://github.com/vercel-labs/agent-browser">vercel-labs/agent-browser</a> +190（Rust）、<a href="https://github.com/milind-soni/OpenMausBot">OpenMausBot</a> +1,955、<a href="https://github.com/sherlock-project/sherlock">sherlock</a> +1,766、<a href="https://github.com/zed-industries/zed">zed</a> +1,114、<a href="https://github.com/astral-sh/ruff">ruff</a> +350、<a href="https://github.com/prometheus/prometheus">prometheus</a> +322、<a href="https://github.com/mbillow/localthings">localthings</a> +186、<a href="https://github.com/ranxianglei/billion-context">billion-context</a> +191、<a href="https://github.com/dsx-ai-factory/nvke">nvke</a> +123、<a href="https://github.com/tailwindlabs/tailwindcss">tailwindcss</a> +122、<a href="https://github.com/meta/astryx">meta/astryx</a> +96。</p>
<p style="font-size:13px;color:#6b7280;">边界：<code>stars today</code> 是 GitHub Trending 页面在 16:04 的快照，会随小时变化；本轮只读了榜单与描述，没有进仓库逐篇核对，不给采用建议。</p>
</details>

<details>
<summary><strong>接口状态：行情与 HN 仍连不上，Steam 单款复核被限流</strong> ｜ 取不到就写明取不到</summary>
<p>16:03 复测：CoinGecko <code>simple/price</code> 与 Hacker News <code>topstories</code> 都是 curl 退出码 35（TLS 握手没过代理），与下午那轮一致，所以 BTC/ETH 报价继续留空。Steam <code>appdetails</code> 对 3241660 的单款请求 16:04 超时，对 1211600 的请求成功，说明接口没有全挂、但逐款复核会被限流。Epic、Steam 列表接口、GitHub Trending 与 GitHub API 本轮均正常。</p>
<p style="font-size:13px;color:#6b7280;">本轮没有新增安全条目，OpenSSH 10.6p2 / Alpine 的处置建议维持 15:30 那版不变；也没有新的 AI 与币圈一手来源可核，不用旧闻填充。</p>
</details>

## 15:20–15:30 补录（4 条）

<p>15:05 那版发完后，又跑了一轮只读复核。新增的是四处：<strong>Alpine 官方安全公告</strong>给出了 OpenSSH 问题的修复版本与重启要求、<strong>Steam 特别优惠榜</strong>拿到了全量 10 条与精确截止、<strong>Epic 后续档期</strong>确认了 Knightica 的免费窗口、<strong>GitHub Trending</strong> 出现四个 Agent Skills 仓库同时上榜。没变的是缺口：CoinGecko、Binance、Coinpaprika 仍然连不上（curl 35），Steam appdetails 逐款复核本轮被限流（空响应），所以下面 Steam 那一条只能认列表接口。</p>

<details open>
<summary><strong>Alpine 官方公告：openssh-server 密码验证绕过，修复版本已列出</strong> ｜ 已升级为「今天就做」 ｜ 官方称写作时无 CVE 编号</summary>
<p>Alpine 在 <strong>2026-11-05</strong> 发了独立安全公告，条件和 OpenSSH 10.6p2 发布说明一致，但把「谁受影响、升到哪个版本、升完做什么」写全了。受影响要同时满足：跑 Alpine 的 <code>openssh-server</code>（不带 PAM），或跑 <code>openssh-server-pam</code> 但 <code>UsePAM no</code>；<code>PasswordAuthentication yes</code>（OpenSSH 默认值）；机器上存在密码字段为 <code>*</code> 的账户（root 自 Alpine 约 3.16 起就是 <code>root:*</code>，默认 <code>PermitRootLogin prohibit-password</code> 能挡住 root，但只要还有别的可登录账户能 <code>doas</code> 到 root 就不安全；<code>adduser</code> 建的无密码密钥用户、目录服务账户也算）；至少一个本地账户有 <code>$5$</code>/<code>$6$</code> 哈希。<strong>3.16 到 3.24 以及 edge 全部在列</strong>。</p>
<p>修复路径：<code>apk upgrade -U -a</code>，含修复包的发行版是 3.21.10 / 3.22.8 / 3.23.8 / 3.24.4；对应固定版本为 edge <code>10.6_p2-r0</code>、3.24 <code>10.3_p1-r2</code>、3.23 <code>10.2_p1-r1</code>、3.22 <code>10.0_p1-r11</code>、3.21 <code>9.9_p2-r1</code>。升级后<strong>必须</strong> <code>rc-service sshd restart</code>——只升级不重启，跑着的还是旧守护进程。暂时升不了就把 <code>PasswordAuthentication</code> 设为 <code>no</code> 并重启，两条路任选一条都能关洞。</p>
<p style="font-size:13px;color:#6b7280;">出处：<a href="https://www.alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">alpinelinux.org 安全公告</a>，核实于 2026-11-08 15:23。<strong>边界</strong>：这是 Alpine 发行版公告，不是 OpenSSH 上游；公告明说写作时<strong>没有分配 CVE 编号</strong>。所以正文里「CVE-2026-123158」这个编号仍只来自 Appinn 转述，继续留在观察区，不当结论用。</p>
</details>

<details>
<summary><strong>GitHub Trending 今日：四个 Agent Skills 仓库同时上榜</strong> ｜ 热度快照，不是推荐</summary>
<p>15:24 抓的日榜：<a href="https://github.com/cloudflare/security-audit-skill">cloudflare/security-audit-skill</a> 今日 +2,085（多阶段安全审计，输出机器可读结论）、<a href="https://github.com/mattpocock/skills">mattpocock/skills</a> +1,100、<a href="https://github.com/google/skills">google/skills</a> +443、<a href="https://github.com/anthropics/skills">anthropics/skills</a> +390。同一天还有 <a href="https://github.com/sherlock-project/sherlock">sherlock</a> +1,766、<a href="https://github.com/milind-soni/OpenMausBot">OpenMausBot</a> +1,955、<a href="https://github.com/zed-industries/zed">zed</a> +1,114。</p>
<p style="font-size:13px;color:#6b7280;">边界：stars today 是 GitHub 页面在 15:24 的快照，会随小时变化；本轮没有逐个读仓库内容，只确认了描述与语言，不给采用建议。</p>
</details>

<details>
<summary><strong>Steam 特别优惠榜全量 10 条：最早 11-10 01:00 到期</strong> ｜ 仅列表接口，未逐款回单页</summary>
<p>R.E.P.O. ¥22.75（-35%，11-10 01:00）、007 初露锋芒 ¥202.80（-40%，11-10 02:00）、Dying Light Essentials ¥9.80（-90%，11-10 01:00）、Escape the Backrooms ¥29.60（-20%，11-10 02:00）、Nomad Drive ¥48.60（-10%，11-11 01:00）、Probably Stolen ¥49.50（-10%，11-12 01:00）、人类一败涂地 ¥17.40（-70%，11-13 02:00）、PEAK ¥20.46（-38%，11-15 18:00）、Potato Please ¥31.50（-10%，11-16 02:00）、ZED ZONE ¥28.80（-40%，11-20 02:00）。</p>
<p style="font-size:13px;color:#6b7280;">边界：价格与截止都取自 <code>featuredcategories</code> 列表接口，15:25 实测；本轮 <code>appdetails</code> 逐款复核被限流，所以不能像 15:05 那版一样说「已逐款核价」。Dying Light 的 appid 1345940 在 appdetails 里此前返回过另一款游戏，付款前以商店页为准。</p>
</details>

<details>
<summary><strong>Epic 后续档期：Knightica 11-13 00:00 起 0 元，TerraScape 11-22 起 -70%</strong> ｜ 现在领不到</summary>
<p>官方接口的 <code>upcomingPromotionalOffers</code> 里：<strong>Knightica</strong> 从 <code>2026-11-12T16:00Z</code> 到 <code>11-19T16:00Z</code>，折北京时间 <strong>11-13 00:00 至 11-20 00:00</strong>，0 元；<strong>TerraScape</strong> 11-21T16:00Z 起至 12-21T16:00Z，-70%；12-10 起《幽灵行者 2》-20%、《纪念碑谷》-35%、《LISA: Definitive Edition》再折 -55%。</p>
<p style="font-size:13px;color:#6b7280;">边界：都是未来排期，现在领不到、折扣也还没生效，写进来只为提前记档；到期当天要回接口重核，别把排期当现货。</p>
</details>

<p style="font-size:13px;color:#6b7280;">另两条只进观察、不进「值得」：HN 首页 15:24 的 <a href="https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview/">GitHub 新 PR 概览页进入公开预览</a>（116 分）与 <a href="https://github.com/hedgerow-dev/coldframe">Coldframe 蜜罐</a>（218 分），本轮只读了标题与链接，没进仓库或文档逐条核。</p>

## 值得看（6）

<details open>
<summary><strong>OpenSSH 10.6p2：musl + 关闭 PAM 的 sshd，超长密码可绕过验证</strong> ｜ 官方已修复 ｜ <span style="color:#c0392b;font-weight:700;">如果你有 Alpine 且开着密码登录，今天就升</span></summary>
<p>OpenSSH 官方 <code>release-10.6p2</code> 说明写得很直接：这个版本包含一个 <strong>critical security workaround</strong>，针对的是「用 musl libc 且编译/运行时不带 PAM」的 Linux；问题表现为 <code>sshd(8)</code> 的密码验证可被绕过。官方把根因归到 sshd 之外，但认为可以在 sshd 侧规避，报告人署名为 Özgün Kültekin。</p>
<p style="font-size:13px;color:#6b7280;">出处：<a href="https://www.openssh.com/txt/release-10.6p2">openssh.com/txt/release-10.6p2</a>，核实于 2026-11-08 15:02。<strong>边界要说清</strong>：官方发布说明里<strong>没有写 CVE 编号</strong>；「CVE-2026-123158」「影响 Alpine/OpenWrt、Ubuntu/Debian 不受影响」这些细节来自 Appinn 的中文转述（<a href="https://www.appinn.com/openssh-sshole-cve-2026-123158/">appinn.com</a>），我没在官方页面核到编号，引用时请以各发行版自己的安全公告为准。Alpine 的官方公告已在 15:23 核到，修复版本与「必须重启 sshd」的要求见上面的补录。自查：<code>ldd $(which sshd) | grep musl</code> 与 <code>grep -Ei '^PasswordAuthentication' /etc/ssh/sshd_config</code>；Alpine 上 <code>apk update &amp;&amp; apk upgrade &amp;&amp; rc-service sshd restart</code>，暂时升不了就把密码登录关掉、只留密钥。</p>
</details>

<details>
<summary><strong>Epic 本周限免两篇，截止 2026-11-13 00:00</strong> ｜ 0 元领取</summary>
<p>官方接口里本周仍挂着两条免费 offer：《浮游世界》（原价 ¥75.00）与《Idle Champions of the Forgotten Realms》，两者的 <code>endDate</code> 都是 <code>2026-11-12T16:00:00.000Z</code>，折北京时间 11-13 00:00。领了永久入库，不是限时试玩。<strong>本条是复查，不是新增</strong>。</p>
<p style="font-size:13px;color:#6b7280;">数字出处：Epic 官方 <code>freeGamesPromotions</code> 接口的 <code>promotionalOffers</code>。核实于 2026-11-08 14:58。诚实说明：《Idle Champions》这条的 <code>originalPrice</code> 在接口里已经是 0（促销态），所以只确认「现在能 0 元领」，不写它的原价。去 <a href="https://store.epicgames.com/free-games?lang=zh-CN">store.epicgames.com/free-games</a> 自己登录领取，本站不代领。</p>
</details>

<details>
<summary><strong>Steam 国区四款折扣复查：价格仍在，最早 11-10 01:00 到期</strong> ｜ 已回 appdetails 逐款核价</summary>
<p>R.E.P.O. ¥35.00 → ¥22.75（-35%，列表接口给到 11-10 01:00）；007 初露锋芒 ¥338.00 → ¥202.80（-40%，11-10 02:00）；人类一败涂地 ¥58.00 → ¥17.40（-70%，11-13 02:00）；PEAK ¥33.00 → ¥20.46（-38%，11-15 18:00）。四款都是 11-07 已报过的，<strong>价值只在「今天仍有效」</strong>。</p>
<p style="font-size:13px;color:#6b7280;">核法：<code>store.steampowered.com/api/appdetails?appids=…&amp;cc=cn</code> 逐款取 <code>price_overview</code> 的 <code>initial</code>/<code>final</code>，截止时间取 <code>featuredcategories</code> 列表里的 <code>discount_expiration</code>。核实于 2026-11-08 15:00。<strong>边界</strong>：截止时间是列表接口给的值，没在结账页再验一次；价格随时可能变，下单前以商店页为准。另外 Dying Light（appid 1345940）在 appdetails 里返回的是另一款叫 Anagrams 的游戏，id 对不上，本轮直接不报。</p>
</details>

<details>
<summary><strong>Libghostty 1.0 发布：终端模拟库的 C ABI 定版</strong> ｜ 长期有效</summary>
<p>Mitchell Hashimoto 11-06 的发布文：<code>libghostty-vt 1.0</code> 把 Ghostty 内核抽成可移植的 C 库，1.0 意味着库本身与 C ABI 都稳定，并有强制的 ABI 兼容策略。已有消费方包括 JetBrains 全家桶的终端（作者引用 JetBrains 报告的 1250 万活跃用户），Neovim 也用 libghostty-vt 替换 libvterm 的 PR 已获批。</p>
<p style="font-size:13px;color:#6b7280;">直链 <a href="https://mitchellh.com/writing/libghostty-1-0">mitchellh.com/writing/libghostty-1-0</a>，核实于 2026-11-08 15:01。「1250 万活跃用户」是作者转引 JetBrains 报告的数字，本轮没有独立复算。</p>
</details>

<details>
<summary><strong>Asahi Linux 进度报告（Linux 7.3）：M3 转正，M4/M5 能进 TTY</strong> ｜ 长期有效</summary>
<p>这一期两个重点：M3 系列的支持从 <code>EXPERT</code> 标记转正，并补上了 DCP，意味着 M3 机器可以睡眠、刘海区域也能用；上游化方面，macaudio（约 3100 行）与 AVD（约 13000 行）两个大驱动进入提交队列，另外出现了 M4 Pro/Max 与 M5 的初始 Devicetree（目前只够把 SoC 启到 TTY）。</p>
<p style="font-size:13px;color:#6b7280;">直链 <a href="https://asahilinux.org/2026/11/progress-report-7-3/">asahilinux.org/2026/11/progress-report-7-3</a>，核实于 2026-11-08 15:01。注意「初始 Devicetree 只够进 TTY」是原文自己的限定，别当成 M4/M5 日常可用。</p>
</details>

<details>
<summary><strong>GitHub 工程博客《Beyond code generation: A developer's guide to agentic engineering》</strong> ｜ 长期有效</summary>
<p>给了一份可引用的量级：2026 年 10 月 GitHub 单周提交超过 12 亿次，同比 +400%，比 2025 年全年还多；同文引用 Faros AI 的观察——团队从低 AI 采用率升到高采用率后，PR 在评审环节停留的时间拉长了 441%。文章把 Agent 工作流拆成 Plan / Build / Verify / Observe 四段，适合写「AI 提效之后瓶颈转移到评审」这类内容时直接取数。</p>
<p style="font-size:13px;color:#6b7280;">直链 <a href="https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/">github.blog</a>，核实于 2026-11-08 15:03（经官方 RSS 正文核对）。两个数字都是 GitHub / Faros AI 的自报，本轮没有复算，引用时带上来源。</p>
</details>

## 观察（11）、币圈那一轮与方法

<details>
<summary><strong>观察清单：11 条，每一条都写清楚卡在哪一步</strong></summary>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead><tr style="border-bottom:1px solid #e3e6ea;text-align:left;color:#8a9099;font-size:12px;">
<th style="padding:6px 8px 6px 0;">条目</th><th style="padding:6px 8px 6px 0;width:44%;">为什么只给观察</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Windows 画图高危漏洞 CVE-2026-83844（称无需用户操作即可远程触发）；QNAP 警告 Plex2Shell 漏洞正被利用、已有 NAS 疑似遭入侵</td><td style="padding:8px 8px 8px 0;">两条都只见 Appinn 转述，本轮没回 Microsoft MSRC 与 QNAP 官方公告核编号、影响版本与修复版本。安全类只认一手，先压在观察</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">「Claude Code 的 Don't Ask Again 把口令写进 1122 个公开 GitHub 文件」（HN 319 分，指向 Apiiro 研究博客）</td><td style="padding:8px 8px 8px 0;">Apiiro 原文被 Cloudflare 挑战页挡住，只拿到 HN 标题与分数，没读到方法、样本口径与厂商回应；「1122」这个数字未经第二来源复核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Steam 特别优惠榜其余 6 条（深空当铺 -10%、隔离区 -40%、Nomad Drive -10%、Potato Please -10%、Dying Light Essentials -90% ¥9.80、Escape the Backrooms -20%）</td><td style="padding:8px 8px 8px 0;">本轮只对上面四款做了 appdetails 逐款核价，这 6 条仍只有列表接口的价格与截止；其中 Dying Light 的 appid 还对不上另一款游戏，更要降级</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Epic 后续档期：11-12 16:00 UTC 起《斗阵骑士 Knightica》0 元；TerraScape 12-21 前 -70%；12-10 起《幽灵行者 2》-20%、《纪念碑谷》-35%、《LISA》再折 -55%</td><td style="padding:8px 8px 8px 0;">都是 <code>upcomingPromotionalOffers</code> 里的未来排期，现在领不到、价格也还没生效；写进正文只会误导，等当天再核</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">iPhone 18/18e X 光图曝光（称共用部分模具、4430mAh 电池）</td><td style="padding:8px 8px 8px 0;">IT之家转述的爆料图，无供应链或苹果官方口径，按传闻处理，不进「值得」</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">Menlo Ventures 报告：中国 AI 模型占全球开源模型企业支出 89%，Kimi、DeepSeek、GLM 前三</td><td style="padding:8px 8px 8px 0;">只有 IT之家一条中文转述，没拿到报告原文与统计口径（「开源模型企业支出」的分母是什么），数字先不引用</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">《死亡搁浅》系列发售 7 年、全球累计玩家突破 2800 万；青沼英二谈任天堂不裁员</td><td style="padding:8px 8px 8px 0;">均为 IT之家转述，前者缺官方口径、后者是访谈摘录，属背景资料，无可执行动作</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">HN / Lobsters 高热技术条目：NFS Underground 2 浏览器复刻（914 分）、苹果设备内置「家庭成员分类器」（679 分）、$10 OpenStick 家庭实验室（500 分）、微软研究院 AI Frontiers 团队结束（438 分）、苹果拼写灰名单（431 分）</td><td style="padding:8px 8px 8px 0;">热度高但本轮没逐篇读原文，只在榜单层面确认存在；写内容前需要自己进去看，避免把标题当结论</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">SSPAI《苹果产品那些不够颠覆，却值得被学习的细节》等 3 篇</td><td style="padding:8px 8px 8px 0;">是专栏与体验文，不是当期可兑现的信息；本轮只核了标题与发布时间</td></tr>
<tr style="border-bottom:1px solid #eef0f2;"><td style="padding:8px 8px 8px 0;">iOS 本体限免 / 内购限免：本轮 0 条新增</td><td style="padding:8px 8px 8px 0;">原先依赖的 Telegram 汇总频道 <code>t.me/s/TossTF</code> 本轮连不上（curl 35），没有新播报可核，也不拿旧条目充数</td></tr>
<tr><td style="padding:8px 8px 8px 0;">恐惧贪婪指数 28（Fear），接口给出的前一日读数是 25（Extreme Fear）</td><td style="padding:8px 8px 8px 0;">只是情绪语境底数，不作信号；来源 alternative.me，核实于 15:04</td></tr>
</tbody></table>
</details>

<details>
<summary><strong>币圈这一轮：行情接口全挂，只剩情绪指数</strong></summary>
<p>本轮 <strong>CoinGecko（markets 与 simple/price 两个端点）、Binance（BTCUSDT ticker）、Coinpaprika 三个行情源全部连接失败</strong>（curl 退出码 35，TLS 握手没过代理），所以 BTC、ETH、USDT、BNB、XRP 的报价与 24h 涨跌一个字都不写——宁可空着，也不拿上一轮的数字冒充今天。能取到的只有 alternative.me 的恐惧贪婪指数：<strong>28（Fear）</strong>，接口同时给出前一日读数 25（Extreme Fear）。</p>
<p>交易所公告、链上安全事件、监管文件这几类本轮没有新增可核来源，同样不写。按这一赛道更硬的门槛：行情、热搜、情绪指数是状态描述而非可执行信息；安全与监管只认项目方 advisory / 官方博客 / 交易所公告，媒体单独转述一律降级；产物里不出现钱包地址、私钥、助记词与带邀请返利参数的链接，也不给买卖建议与目标价。</p>
</details>

<details>
<summary><strong>这一轮是怎么跑出来的：取数、验真、分级、落盘四步</strong></summary>
<p><strong>取数</strong>：13 个来源 / 接口，约 110 条——Epic 官方促销接口（7 条 offer）、Steam 特别优惠榜（10 条）+ 5 款 appdetails、HN 首页（15 条）、Lobsters（12 条）、GitHub 官方博客 RSS（10 条）、Appinn RSS（10 条）、SSPAI RSS（7 条）、IT之家 RSS（15 条）、alternative.me、OpenSSH 发布说明、Asahi 与 mitchellh 各 1 篇。失败 6 处：CoinGecko、Binance、Coinpaprika、<code>t.me/s/TossTF</code>、Apiiro 博客（Cloudflare 挑战页）、Steam appid 1345940（返回错款）。</p>
<p><strong>验真</strong>：福利类回官方接口二次确认价格与截止——Epic 走 <code>freeGamesPromotions</code>，Steam 走 <code>appdetails</code> 的 <code>price_overview</code>，这比上一轮「只能拿到列表页」进了一步；安全类只把 OpenSSH 官方发布说明提到「值得」，CVE 编号与影响范围因为是转述，正文里明确标了出处与不确定性。取不到的行情与限免，直接承认取不到。</p>
<p><strong>分级</strong>：🔥 紧急要求距截止不超过 3 小时或影响既有服务，本轮 0 条（OpenSSH 虽重要，但没有统一截止时间，放「值得」第一条并给出自查命令）；⭐ 值得 6 条，均为一手来源或已回官方接口核实；👀 观察 11 条，逐条写明卡在哪一步；旧闻重推、软文、要连钱包才能领的直接过滤。</p>
<p><strong>落盘</strong>：同一天只保留这一份，后续如有新料在此文更新而不是新建文件。15:05 首发后，15:20–15:30 与 16:03–16:05 又各跑了一轮只读复核，按「一天一份」的规则直接在原文件追加「补录」与「第三轮复核」段，远端仍是同一个 <code>_posts/2026-11-08-info-radar.md</code>，没有新建文件。<strong>边界</strong>：全程只收集与核实，不注册、不绑卡、不代领券、不下单；币圈不连钱包、不签名、不导私钥、不代充代提，也不给买卖建议与目标价。所有兑现动作由读者本人完成。</p>
</details>
