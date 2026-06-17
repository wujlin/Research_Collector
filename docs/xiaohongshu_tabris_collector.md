# Xiaohongshu Tabris Resource Collector

这个流程的目标不是搬运小红书内容，而是把 Tabris 帖子里提到的论文、blog、书、视频和作者线索整理成研究采集队列。

## 安全边界

- 不把 cookie、token、登录态写入仓库。
- 不绕过验证码、登录限制、风控或反爬机制。
- 只采集你自己的账号可见内容，并低频运行。
- 原帖正文默认写入 `data/social/`，该目录已被 `.gitignore` 忽略。
- 进入正式笔记或 digest 的内容只保留推荐资源、原帖链接、必要摘要和采集状态。

如果 cookie 曾经粘贴到对话、日志或仓库里，建议退出小红书网页端并重新登录，让旧登录态失效。

## 准备 cookie

在本机创建私密目录：

```bash
mkdir -p .secrets
```

把浏览器导出的 cookie JSON 保存到：

```text
.secrets/xhs_cookies.json
```

不要提交 `.secrets/`。

## 安装依赖

```bash
python -m pip install -e ".[social]"
python -m playwright install chromium
```

## 采集 Tabris 主页

先做低频小样本：

```bash
python scripts/collect_xhs_profile.py \
  --profile-url "https://www.xiaohongshu.com/user/profile/60a72ded000000000101de6e" \
  --cookies .secrets/xhs_cookies.json \
  --source-name tabris \
  --max-notes 20 \
  --scrolls 8 \
  --headful
```

如果只想先抽取主页卡片，不打开帖子详情：

```bash
python scripts/collect_xhs_profile.py \
  --profile-url "https://www.xiaohongshu.com/user/profile/60a72ded000000000101de6e" \
  --cookies .secrets/xhs_cookies.json \
  --source-name tabris \
  --max-notes 20 \
  --no-detail \
  --headful
```

如果 cookie 失效，或者你不想把 cookie 文件保存到本地，可以让脚本打开浏览器后手动登录：

```bash
python scripts/collect_xhs_profile.py \
  --profile-url "https://www.xiaohongshu.com/user/profile/60a72ded000000000101de6e" \
  --source-name tabris \
  --max-notes 20 \
  --headful \
  --manual-login-seconds 120 \
  --user-data-dir .secrets/xhs_chromium_profile
```

这会给你 120 秒在浏览器窗口里完成登录，并把这个浏览器 profile 保存在 `.secrets/xhs_chromium_profile`。后续运行可以复用这个 profile：

```bash
python scripts/collect_xhs_profile.py \
  --profile-url "https://www.xiaohongshu.com/user/profile/60a72ded000000000101de6e" \
  --source-name tabris \
  --max-notes 20 \
  --headful \
  --user-data-dir .secrets/xhs_chromium_profile
```

如果页面提示“安全限制 / IP 存在风险”，不要继续尝试自动绕过。应换回正常浏览器环境、降低采集频率，或改用手动分享链接 / 截图 OCR 作为输入。

## 输出结构

默认输出到：

```text
data/social/xiaohongshu/tabris/<timestamp>/
```

核心文件：

- `notes.jsonl`：每条帖子一行，包含标题、原帖链接、可见正文和候选资源链接。
- `resource_candidates.md`：从帖子正文中提取出的 URL/DOI/arXiv 线索，适合作为下一步人工筛选入口。
- `run_summary.json`：运行参数和采集统计。
- `debug/blocked_or_login.png`：如果遇到登录态失效或访问异常，会保存截图便于判断。

## 后续整理字段

从 `resource_candidates.md` 进入正式采集时，建议整理成：

```text
source: Xiaohongshu / tabris
post_url:
post_date:
post_topic:
recommended_items:
  - title:
    type: paper/blog/book/video
    url:
    authors:
    why_relevant:
    collection_status: pending/downloaded/digested
priority:
notes:
```
