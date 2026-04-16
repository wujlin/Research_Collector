# Digest Conventions

这份约定只处理一件事：`digests/` 目录到底应该放什么，不应该放什么。

## 1. 日期目录结构

每天的日期目录 `digests/YYYY-MM-DD/` 分为两层：

```
digests/2026-04-16/
├── workflow/                    ← 流程产物（自动脚本 + 手工整理）
│   ├── paper-queue.md
│   ├── study-guide.md
│   ├── collection-review.md
│   └── weekly.md
├── nonequilibrium-physics-of-generative-diffusion-models.md   ← 精读笔记
├── generative-optimal-transport-via-forward-backward-hjb-matching.md
└── ...
```

### workflow/ 子目录（4 类流程文件）

- `paper-queue.md` — 当天的论文队列（Must Read / Watchlist）
- `study-guide.md` — 当天的精读工作包（阅读顺序、要盯的问题）
- `collection-review.md` — 采集审查结果（keep / review / archive）
- `weekly.md` / `monthly.md` — 自动周期摘要

### 日期目录根（精读笔记）

- `<paper-slug>.md` — 逐篇论文的精读记录
- 命名规则：论文标题的 slug 化（小写、连字符分隔）
- 归属到**精读完成的日期**，而不是论文的发表日期

## 2. 不再保留的类型

以下类型默认不再单独存在：

- `start-here.md` — 包装页，不产生独立信息
- `youtube-study-companion.md` — 并入 `workflow/study-guide.md`
- `recent-high-quality-shortlist.md` — 并入 `workflow/paper-queue.md`
- 分裂的 `batch-review.md` / `youtube-review.md` — 并入 `workflow/collection-review.md`

## 3. 长期专题笔记与精读笔记的区分

精读笔记（逐篇论文的阅读记录）放在 `digests/YYYY-MM-DD/` 根目录下。

以下内容不是精读笔记，应移到更稳定的位置：

- YouTube 专题笔记 → `youtube/notes/`
- 跨论文的理论主题长期笔记 → `knowledge_map/`
- 方法对比笔记 → `knowledge_map/`

## 4. 命名规则

1. 日期文件夹表达"是哪一天"
2. 文件名只表达"这份文件的职责"
3. 不在文件名里重复日期

推荐：

- `digests/2026-04-16/workflow/paper-queue.md`
- `digests/2026-04-16/workflow/study-guide.md`
- `digests/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.md`

不推荐：

- `digests/2026-04-16/2026-04-16-frontier-followup-pack.md`
- `digests/2026-04-16/00-start-here.md`

## 5. 生成规则

自动脚本和手工整理都遵守同一套布局：

- 论文队列脚本 → `workflow/paper-queue.md`
- 采集审查脚本 → `workflow/collection-review.md`
- 周报/月报 → `workflow/weekly.md` / `workflow/monthly.md`
- 手工学习整理 → `workflow/study-guide.md`
- 精读笔记 → 日期目录根下 `<paper-slug>.md`
