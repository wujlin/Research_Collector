# Digest Conventions

这份约定只处理一件事：`digests/` 目录到底应该放什么，不应该放什么。

目标是让每天的产物数量稳定、职责清楚、后续可持续维护，而不是不断长出新的“包装页”。

## 1. Daily Digest 只保留 4 类

每天的日期目录 `digests/YYYY-MM-DD/` 默认只保留下面四类文件：

- `paper-queue.md`
  用来排当天的论文队列。内容包含：
  - `Must Read`
  - `Reproduction Candidates`
  - `Watchlist`
  - `Must Read` 默认应经过 venue 口碑核验
- `study-guide.md`
  用来组织当天正在精读的工作包。内容包含：
  - 阅读顺序
  - 每篇要盯的问题
  - 配套视频
  - 复现起点
- `collection-review.md`
  用来记录当天采集后的审查结果。内容包含：
  - 论文 keep/review/archive
  - YouTube keep/review/archive
- `weekly.md` 或 `monthly.md`
  用来放自动周期摘要。

除非有明确新增的独立任务类型，否则不要再往日期目录里加第五、第六种文件。

## 2. 不再保留的类型

以下类型默认不再单独存在：

- `start-here.md`
  这是包装页，不产生独立信息。
- 单独的 `youtube-study-companion.md`
  伴读内容应并入 `study-guide.md`。
- 单独的 `recent-high-quality-shortlist.md`
  shortlist 应并入 `paper-queue.md`。
- 分裂的 `batch-review.md` 和 `youtube-review.md`
  两者应并入 `collection-review.md`。

## 3. 长期专题笔记不放进 digests

如果一份内容不是“当天流程产物”，而是可以跨天复用的专题材料，就不要继续塞在 `digests/` 里。

典型例子：

- YouTube 专题笔记
- 某个理论主题的长期阅读笔记
- 方法对比笔记

这类内容应该移到更稳定的位置，例如：

- `youtube/notes/`
- `knowledge_map/`
- 以后如有需要，可再细分专题目录

## 4. 命名规则

命名优先级如下：

1. 先用日期文件夹表达“是哪一天”
2. 文件名只表达“这份文件的职责”
3. 不在文件名里重复日期
4. 不用纯数字做文件名

推荐：

- `digests/2026-04-08/paper-queue.md`
- `digests/2026-04-08/study-guide.md`
- `digests/2026-04-08/collection-review.md`
- `digests/2026-04-08/weekly.md`

不推荐：

- `digests/2026-04-08/2026-04-08-frontier-followup-pack.md`
- `digests/2026-04-08/00-start-here.md`

## 5. 生成规则

自动脚本和手工整理都要遵守同一套最终布局：

- 论文队列脚本输出到 `paper-queue.md`
- 采集审查脚本输出到 `collection-review.md`
- 周报/月报导出到 `weekly.md` / `monthly.md`
- 手工学习整理统一收进 `study-guide.md`

如果中间过程需要临时文件，可以存在生成过程中，但交付前必须合并或移走，不应留在最终日期目录里。

## 6. 判断是否应该新建文件

只有在下面两个条件同时满足时，才允许新建新的 digest 类型：

1. 这份文件承载的是独立任务，而不是已有文件的子章节。
2. 它在后续多天都会重复出现，而不是一次性包装页。

如果不同时满足，就应该并入现有四类之一。
