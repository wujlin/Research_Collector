---
title: "Equation Map for Entropy and Frenesy: the Arrow and the Bustle of Time"
source_digest: "./entropy-and-frenesy-the-arrow-and-the-bustle-of-time.md"
source_pdf: "../../pdfs/2026-08-24/entropy-and-frenesy/entropy-and-frenesy.pdf"
arxiv: "2608.17586"
date_created: "2026-08-24"
---

# Equation Map

这份地图按论文正式编译的公式编号核对。正文中的解释性改写不冒充原文公式；社会系统中的候选观测式也不使用原编号。

## 主文公式覆盖

| 原文公式 | 原式角色 | 笔记中的逻辑位置 | 状态与备注 |
|---|---|---|---|
| Eq. (1) | Clausius heat theorem：可逆热除以温度等于热力学熵的状态微分 | 第 2 节 | 已解释；限定为准静态可逆过程 |
| Eq. (2) | Boltzmann entropy `S = k_B log W` | 第 3 节 | 已解释；`W` 是宏观状态兼容的微观实现数/体积 |
| Eq. (3) | 微观状态 `X` 的 Boltzmann 熵由其所属宏观状态 `M(X)` 的相空间体积定义 | 第 3 节 | 已解释；原 LaTeX 多了一个右括号，笔记采用显然意图的写法 |
| Eq. (4) | 从高熵宏观状态反向波动到低熵状态的概率按熵差指数抑制 | 第 3 节 | 已解释；用于建立时间箭头，不用于估计人口迁移概率 |
| Eq. (5) | 偏置随机游走路径概率由两个方向的跳跃次数加权 | 第 6 节 | 已展开为路径统计起点 |
| Eq. (6) | 用净流 `Jt` 与总跳跃数 `N` 重写路径概率和作用量 | 第 6 节 | 已重点解释“差”与“和”的独立性 |
| Eq. (7) | 路径作用量分解为时间对称 `D` 与时间反对称 `Sigma` | 第 5 节 | 已重点展开；全文概念枢纽 |
| Eq. (8) | 随机游走中 `D` 依赖总活动，`Sigma` 依赖净流与速率比 | 第 5-6 节 | 已解释；与 Fig. 7 联读 |
| Eq. (9) | 在局域详细平衡下，把作用量写成外场驱动的熵项与活动参数 `aN` | 第 6 节 | 已解释；说明同一驱动下活动参数仍可独立变化 |
| Eq. (10) | 外场小扰动后路径概率比的一阶展开 | 第 7 节 | 已解释其两项来源，未逐行重做代数 |
| Eq. (11) | 电流响应分成 entropic correlation 与 frenetic correlation | 第 7 节 | 已重点展开；同时说明平衡态下第二项为何消失 |
| Eq. (12) | 当活动参数 `a=0` 时，路径权重只剩由驱动和净流构成的偏置 | 第 11 节 | 已用结论；用于说明现实中反转驱动不等于反转时间 |

## 未编号但关键的关系

| 关系 | 作用 | 覆盖状态 |
|---|---|---|
| `Prob[omega] proportional to exp(-A(omega))` | 把轨迹统计写成作用量形式 | 已在第 5 节解释 |
| `Sigma = log(Prob[omega] / Prob[theta omega])` | 把时间反演不对称与环境熵流连接 | 已在第 5 节解释适用条件 |
| `p + q = escape rate` | 区分方向偏置与总逃逸强度 | 已在第 6 节解释 |
| `total jumps = forward jumps + backward jumps` | 躁动度的最小可观测原型 | 已在第 6 节重点展开 |
| Ziegler 例子的能量平衡 | 说明正阻尼也能通过相位重组参与失稳 | 已在第 10 节解释；论文未给编号 |

## 迁移边界

1. Eq. (7)-Eq. (11) 是满足局域详细平衡的随机动力学结果，不能自动移植成城市人口的热力学恒等式。
2. 项目中的 `C_peak` 是中心有符号人口异常，不对应原文 `Sigma`。
3. 候选 `A_peak` 只能称为 time-symmetric activity proxy；除非先建立明确路径模型，否则不应宣称已测得严格的 `D`。
4. 论文允许 frenetic contribution 改变符号，因此项目模型中 activity effect 不应预设为正。
