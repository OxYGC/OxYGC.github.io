# GitHub Pages 发布链路（2026-10-15 实测，2026-10-16 改口径）

**Pages 是雷达三段（取数 / 本地存档 / GitHub Pages）之一，每天必做**（用户 2026-10-16 定：资讯雷达必须同步到 GitHub Pages，不再逐次要授权）。拦在上线前的不是「要不要点头」，而是**第六节的内容门槛**：核实时间、截止时间、未核实项是否混进了「值得」——门槛不过就不 push，并在报告里点名是哪一条卡住。第二道护栏：**当天已经成功推过就不再重复 push**，一次运行只进一个 commit，避免同一篇稿在历史里挂两条。

完成判据跟着改：**Pages 段没做成，这一轮雷达就不能报成「跑完」**，要如实写「Pages 未同步 + 卡住的原因」。本地存档与邮件照常交付，但邮件不属于三段，多发一封也补不回这一段。

`$INFO_HOME/daily/*.md`、`$INFO_HOME/out/*.md` 与 `$PAGES_REPO/_posts/` 都可以自动写；这条授权只覆盖「把雷达日报放进自己站点」这件事，代注册、代下单、代领券依旧禁止。

## 一、仓库与分支

```bash
PAGES_REPO="${PAGES_REPO:-$HOME/github/OxYGC.github.io}"
cd "$PAGES_REPO" && git branch --show-current     # 必须是 main
```

- 站点 `https://oxygc.github.io/`，Jekyll + `jekyll-theme-chirpy` 6.2.3，**源分支 `main`**，文章放 `_posts/`。
- **Pages 的发布源已经是 GitHub Actions**（`.github/workflows/pages-deploy.yml` 用了 `actions/deploy-pages@v4`），不需要去 Settings 改 Source。
- **`gh-pages` 分支是 2023 年的旧静态构建，已经不再被服务**（tip `5799b8f`），它是回滚用的、不是真源。改 `_posts/` 才会上线，改 `gh-pages` 不会。
- 判断线上跑的是哪套构建，用外部证据（新文章能否 200、`/assets/js/dist/misc.min.js` 能否 200），**别信分支名**。
- `_posts/` 里已有雷达稿。站点 `permalink: /posts/:title/` **不含日期**，而 Jekyll 生成 slug 时会去掉文件名里的日期前缀，所以**光换文件名没用**——`2026-10-16-info-radar.md` 的 slug 仍然是 `info-radar`，会和昨天的撞在一起、后者被顶掉。正确做法：**每篇雷达稿在 front matter 显式写 `permalink: /posts/info-radar-YYYY-MM-DD/`**。文件名仍然按 `YYYY-MM-DD-info-radar.md` 排，方便本地按时间找。
- 唯一的历史遗留：`_posts/2026-10-15-info-radar.md` 当时没写 permalink，占着 `https://oxygc.github.io/posts/info-radar/`。不要为它补 permalink——补了那个已分享的 URL 就 404。

## 二、front matter 写法（照 chirpy 现有这篇抄结构）

```yaml
---
title: "资讯雷达 2026-10-15｜域名与 VPS 优惠、Epic 限免、本周 AI 动态"
author: OxYGC
date: 2026-10-15 07:10:00 +0800
permalink: /posts/info-radar-2026-10-15/
categories: [Info, Deals]
tags: [资讯雷达, VPS优惠, 域名, 限免, AI动态]
description: "2026-10-15 收集的服务器与域名优惠、游戏应用限免、免费额度与开发者动态，全部标注核实时间与截止时间。"
---
```

- `title` 里**不要 emoji**（`🔥` 这类只放正文，不进标题）。
- `author` 必须在 `_data/authors.yml` 里存在且有 `url`（`OxYGC` 已配好，`url: https://github.com/OxYGC`）。缺 `url` 主题会渲染出空 `href`，htmlproofer 报 `'a' tag is missing a reference` 直接卡住部署。
- `date` 带 `+0800`，而且**必须是 push 那一刻已经过去的时间**（宁可写早几分钟，绝不能写未来）——Jekyll 没配 `future:`、默认 `future: false`，front matter 的 `date` 晚于构建机时钟，这篇就会被构建**静默排除**，而 Actions 照样绿。10-17 真实踩到：front matter 写 `06:52:00 +0800`、commit 是 06:43:50，`Build and Deploy` 57 秒 completed success，产物里根本没有这一篇（线上 `last-modified` 已经推进到本次 commit、`sitemap.xml` 却没有这条 permalink）。正文标题从 `##` 起（chirpy 会把 `title` 渲染成 H1，正文再写一个 H1 会变成两级重复）。
- `categories` 用英文词（现有的是 `[Tools, DevOps]`），`tags` 可以中文。

## 三、会卡住部署的五道坑

1. **`assets/js/dist` 是 gitignore 的 rollup 产物** —— CI 里必须先 `npm install && npm run build` 再 `bundle exec jekyll b`，这段已经写在 `pages-deploy.yml`（第 55~59 行）。本地若要预览，同样先跑这两条。
2. **`author` 缺 `url`** —— 见上一节，`_data/authors.yml` 是唯一出处。
3. **`_config.yml` 的 `img_cdn` 必须留空** —— 第 73 行现在就是空值。一旦填了值，所有 `/assets/...` 图片会被改写到 chirpy 的演示 CDN 上 404。
4. **正文里一个明文 `http://` 外链就能卡住部署** —— `pages-deploy.yml` 的 htmlproofer 只带 `--disable-external=true`（不访问外网），但 `enforce_https` 这一类 issue 是**在链接解析阶段本地判的**，关不掉。所以正文与 front matter 里所有外链一律写 `https://`（2026-10-15 真实踩到：阮一峰那条 `http://` 链接让部署红了一次，修复 commit `17d28b1`）。
5. **front matter 的 `date` 写到未来，这篇会被构建吃掉但工作流仍是绿的** —— 站点原来没有 `future:`，Jekyll 默认 `future: false`，比构建机时钟晚的 `_posts` 文件直接不进产物。这一条最阴的地方在于它**不报错**：`Build and Deploy` completed success、`sitemap.xml` 里没有那条 permalink、新文章 URL 一直 404。判据三件套：① Actions 那一次 run 的 `conclusion`；② `curl -sI` 站点首页拿 `last-modified` 是否已推进到本次 commit 时刻（推进了 = 构建产物换了）；③ `sitemap.xml` 里搜 `/posts/info-radar-YYYY-MM-DD/` 在不在（在 = CDN 延迟，不在 = 日期被判未来或另有排除）。10-17 就是②绿③无。**2026-10-18 已在 `_config.yml` 加 `future: true`（commit `ce675ad`，push 后一次重建就把 10-17 那篇补上线：sitemap 有、URL 200）**，这一类故障在站点侧已经封顶；但「`date` 只写已经过去的时间」这条习惯照留——它同时决定文章在列表里的排序时点，别拿 `future: true` 当随便写未来时间的许可证。

本地预检（比 CI 快，能提前抓到同样的问题）：

```bash
cd "$PAGES_REPO" && npm install --no-audit --no-fund && npm run build \
  && bundle exec jekyll b -d _site 2>&1 | tail -20
```

## 四、图片必须本地化

- **CSDN 图床 `i-blog.csdnimg.cn` 对 `Referer: https://oxygc.github.io/` 返回 403**，直接引用原链就是 broken image。
- 素材落到 `$PAGES_REPO/assets/img/posts/<YYYY-MM-DD-slug>/`，正文用相对路径 `/assets/img/posts/<...>/xx.png`（chirpy 会带 baseurl）。
- 日报类稿件通常不需要图；要配图就把截图/自制图放本地目录，不走任何外链图床。

## 五、push 走代理

本机到 `github.com:443` **没有直连出口**，push 必须单次带代理参数（**不要写进 git config**）：

```bash
cd "$PAGES_REPO"
git add _posts/<新稿>.md assets/img/posts/<日期-slug>/
git status                                  # 确认没有多余文件被带进去
git commit -m "posts: 资讯雷达 YYYY-MM-DD"
git -c http.proxy=http://127.0.0.1:7897 -c https.proxy=http://127.0.0.1:7897 push
```

- `git add` 按名字加，不要 `git add -A`（仓库里有 `_site/`、`node_modules/` 之类，误加会污染历史）。
- commit / push 前先看 `git status`；出现不认识的改动先停下问用户。
- **上线判据不能只看 Actions 绿**（坑 5）：先看那一次 `Build and Deploy` 的 `conclusion`，再看站点首页 `curl -sI` 的 `last-modified` 有没有推进到本次 commit 时刻，最后在 `sitemap.xml` 里搜本篇的 `/posts/info-radar-YYYY-MM-DD/`。三者都过才算上线；`last-modified` 已推进但 sitemap 没有这条 ＝ 这篇没进构建，第一嫌疑是 front matter `date` 晚于 push 时刻，把它改到实际取数时间再推一次。只有 sitemap 已经有、URL 还 404 才是 CDN/换产物延迟，轮询等就行。

## 六、内容口径（发出去前自查）

- 每条都要有「核实于 YYYY-MM-DD HH:MM」与直链；优惠/限免**必须有截止时间**——官方确实不给的（App Store 限免是唯一一例，Apple 不公布促销结束时间）就明写「Apple 不公布限免截止时间」顶替那一栏，**这句缺失才算卡门槛**，绝不许为了过审编一个日期出来。
- 未核实的只放「观察」段并明写存疑原因，不进「值得」。
- 正文可以有外链（这是自己的站，不受 CSDN 过审红线约束）；但**要投到 CSDN 的稿子必须先把站外可点击链接清零**，否则按「广告-营销推广 / 诱导外链」驳回。
- 不出现凭据、token、webhook 地址、内网地址、钥匙串内容；页面 URL 里的 `token=` / `ticket=` 参数一律剥掉。
- 不做「代领/代拍/立即下单」式引导，只描述「你能做什么」，兑现由读者自己完成。
- 币圈条目额外三条：不写买卖建议与目标价、不出现钱包地址/私钥/助记词、不带走 `?ref=` 之类的邀请返利参数；行情只作为「某时刻的快照」写，并标来源与时间。

## 七、雷达稿版式：固定用风格 D（2026-10-15 定稿）

用户在四套候选里点了 D，此后雷达稿不再换版式。结构（参考实现：`$PAGES_REPO/_posts/2026-10-15-info-radar.md`）：

1. 开头一段自然语言点题（不照抄标题），交代这一轮跑了哪些来源、留下几条。
2. **行动清单卡**：一个 `<div>` 包一张四列表（时点 / 条目 / 价格 / 去哪），只放真正会过期或需要复查的 3~4 条，临期时点用 `#c0392b` 加粗。
3. `## 值得看（n）` —— 每条一个 `<details>` 卡片，summary 一行写完「名称 ｜ 价格 ｜ 截止」，价格 `#1a7f37`、临期 `#c0392b`、中性 `#6b7280`。
4. `## 观察（n）、币圈那一轮与方法` —— 观察表、币圈整轮、四步口径各一个 `<details>`。
5. **全文只有 2 个 H2、0 个 H3**，右侧 tocbot 因此只有两项，长表不再把目录撑爆。

三条实测到的渲染前提（不然会白改一轮）：

- `_config.yml` 里 `theme_mode: light` 已锁死，所以卡片边框/底色这类**浅色硬编码值可以写在 inline style 上**，不必考虑暗色模式；站点正文实测 token：正文 16.48px / line-height 1.75、H2 24.64px weight 400、链接 `#0056b2`、正文宽 799.5px。
- 手写 HTML 表格**不需要自己加 class**：`_includes/refactor-content.html` 会把任意 `<table` 前后包成 `<div class="table-wrapper">`，宽表在手机上自动横向滚动。
- **`<details>` 内部一律写原始 HTML**（`<p>` / `<table>` / `<code>` / `<strong>`），不要指望里面的 Markdown 会被解析——kramdown 对 `details` 是否算 block-level 标签取决于版本，写成 HTML 两种情况都能出正确结果。summary 行同理，要强调就写 `<span style=...>`。

## 八、雷达标题的品牌配色（2026-10-30 落地，站点公共层，稿内零改动）

雷达稿标题在首页列表和详情页自动变成深青色（`#0b7285`，hover `#085d6e`）并带一枚「雷达」白字徽标，与其他文章区分。实现在站点公共层三个文件，**判定全部锚在 permalink 的 `info-radar` 段上**，所以只要「每篇显式写 `permalink: /posts/info-radar-YYYY-MM-DD/`」这条硬规则还在，配色就自动生效，front matter 不需要加任何字段（旧稿 /posts/info-radar/ 也一并命中）：

1. `_sass/addon/radar-brand.scss` —— 全部颜色口径集中在这一个文件（`main.scss` 末尾 `@import 'addon/radar-brand';`）。三类选择器：首页卡片 `#post-list .card a.post-preview[href*="/posts/info-radar"] .card-title`（含 `::before` 徽标）、其余列表位（侧栏最近更新/归档/标签/搜索/上下篇/相关文章）`a[href*="/posts/info-radar"]:not(.post-preview)`、详情页 `h1.radar-title`。**要调颜色只改这个文件。**
2. `_layouts/post.html` —— 第 16 行 `<h1 data-toc-skip{% if page.url contains '/posts/info-radar' %} class="radar-title"{% endif %}>`，非雷达稿渲染结果与原来逐字节相同。
3. **三条实测踩出来的对抗，简化一条就会静默失效**（当天连踩两轮才全修对）：
   - 真实 DOM 是 `article.card-wrapper.card > a.post-preview > div.card-body > h1.card-title`——**`.card-body` 是链接的后代不是祖先**，写成 `#post-list .card .card-body a.post-preview …` 会整条不命中且无任何报错；
   - 主题 `home.scss` 对 `#post-list .card .card-body .card-title` 写了 `color: var(--heading-color) !important`，入口 `jekyll-theme-chirpy.scss` 尾部还有一条 `:visited` 变灰读痕同样 `!important`——所以这里全部用 `!important`，且 `:visited`/`:hover` 规则要多挂一个 `[href*="/posts/"]` 属性抬高特异度（入口那条在 `@import 'main'` 之后追加，源码顺序天然靠后）；
   - 站点 CSS 的 CDN `max-age=600`，验证时浏览器必须强刷（⌘⇧R），否则看到的还是旧样式。

验证方式（上线后）：首页雷达稿标题深青色带「雷达」徽标、普通文章不变色；详情页 h1 青色；已读一篇再回首页，标题仍是青色不是灰色。
