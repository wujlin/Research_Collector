# Venue Screening Policy

这份规则只处理一件事：`Must Read` 推荐前，怎么判断期刊或会议的口碑是否足够好。

## 1. 适用范围

这份规则用于：

- `paper-queue.md` 的 `Must Read`
- 手工推荐的“今天先读哪篇”
- 需要用 venue 作为质量背书的场景

它不用于一票否决所有弱 venue 文章。弱 venue 文章仍然可以保留在库里，用作：

- toy reproduction
- 方法练手
- 背景补充

## 2. 核验顺序

推荐前按下面顺序核验：

1. `Clarivate Master Journal List / JCR`
   用于确认是否在 Web of Science、是否存在正式 `JIF`。
2. `Scopus / Scopus Sources`
   用于确认是否被 Scopus 收录，以及是否能看到 `CiteScore` 等指标。
3. `SCImago`
   作为 `SJR / quartile / h-index` 的补充参考。
4. 期刊或会议官方主页
   用于确认 publisher、indexing、scope、editorial information。
5. 作者与机构背景
   用于确认 lead / corresponding / last author 所在机构是否长期做这个方向，以及团队是否专业对口。

如果以上几步都拿不到稳定信号，就把 venue 视为 `unreviewed`，不要直接进 `Must Read`。

## 2.5 文章级补充核验

venue 过关后，对具体文章还要补一次机构筛选：

- 看 `last author / corresponding author` 是否来自长期做该主题的专业组，而不只是大而泛的机构名头。
- 看作者单位是否与论文问题匹配，例如：
  - 随机热力学 / 统计物理：物理、应用数学、复杂系统、非平衡统计团队
  - AI for physics：机器学习、计算物理、科学计算、交叉信息学院
  - 城市系统 / 遥感：城市科学、地理信息、环境遥感、测绘与大气团队
- 若 venue 一般，但作者团队非常专业，文章仍可进入 `Watchlist` 或 `Reproduction Candidates`。
- 若 venue 一般且作者团队也明显不专业，则默认降级处理，不进 `Must Read`。

## 3. 口碑分类

- `trusted`
  强势领域期刊或顶会，可进入 `Must Read`。
- `cautious`
  正式 venue，但口碑或信号不足以单独背书；默认不进 `Must Read`，除非文章本身特别关键。
- `weak`
  venue 信号明显偏弱；不进 `Must Read`。
- `unreviewed`
  还没核验过；先不要进 `Must Read`。

## 4. 当前执行规则

- `Must Read` 默认只允许：
  - `trusted` venue
  - 高重要性 `preprint`
- `cautious / weak / unreviewed` venue 默认只能进入：
  - `Reproduction Candidates`
  - `Watchlist`

## 5. 文件落点

- 手工核验结果记到 [venue_reputation.yaml](/Users/jinlin/Desktop/Project/Research_Collector/config/venue_reputation.yaml)
- 机构与团队信号短名单记到 [author_affiliation_reputation.yaml](/Users/jinlin/Desktop/Project/Research_Collector/config/author_affiliation_reputation.yaml)
- 当天推荐队列输出到 [paper-queue.md](/Users/jinlin/Desktop/Project/Research_Collector/digests/2026-04-08/paper-queue.md)

不要把临时的口碑判断散落在多个 digest 里。
