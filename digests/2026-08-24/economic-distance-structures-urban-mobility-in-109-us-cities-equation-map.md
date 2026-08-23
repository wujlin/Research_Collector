---
title: "Equation Map for Economic Distance Structures Urban Mobility in 109 U.S. Cities"
source_digest: "./economic-distance-structures-urban-mobility-in-109-us-cities.md"
source_pdf: "../../pdfs/2026-08-24/economic-distance-urban-mobility/economic-distance-urban-mobility.pdf"
arxiv: "2608.12180"
date_created: "2026-08-24"
---

# Equation Map

本文主文只有 6 个编号公式，但若忽略未编号的中性基准、方向偏置和 `Q(m)`，方法链仍会断裂，因此一并列出。

## 编号公式覆盖

| 原文公式 | 作用 | 笔记状态 | 关键口径 |
|---|---|---|---|
| Eq. (1) | 把 tract median household income 的城市内排名映射到 `[0,1]` | 已展开 | 第 2 节；保留相对排序，丢弃绝对收入差 |
| Eq. (2) | 定义经济距离小于 `x` 的 origin-normalized flow CDF `E(x)` | 已重点展开 | 第 1、3 节；不是 raw-trip CDF |
| Eq. (3) | 定义向上流量内部的累计函数 `E_u(x)` | 已展开 | 第 5 节；方向按 destination income quantile 是否更高定义 |
| Eq. (4) | 定义向下流量内部的累计函数 `E_d(x)` | 已展开 | 第 5 节；与 Eq. (3) 分别按各方向总量归一化 |
| Eq. (5) | Baseline gravity model：节点规模与地理距离 | 已展开 | 第 9 节；OLS 采用 log-linear 形式 |
| Eq. (6) | 增加 economic-distance factor 的 gravity model | 已重点展开 | 第 9 节；`S(i,j)=exp(theta |q_i-q_j|)`，负 `theta` 表示额外衰减 |

## 未编号但关键的定义

| 定义 | 作用 | 笔记状态 |
|---|---|---|
| `economic distance = |q_o-q_d|` | 全文统一的连续收入秩距离 | 已在第 2 节解释 |
| `E_tilde(x)=2x-x^2` | `[0,1]^2` 中收入中性独立匹配的几何 CDF | 已在第 3 节解释 |
| `E(0.25)` | 城市级短经济距离集中指标 | 已在第 4 节解释并限定数据驱动阈值 |
| `DB=(D_raw-U_raw)/(U_raw+D_raw)` | 未归一化方向流量的总量偏置 | 已在第 5 节解释 |
| `Delta E=E_d(0.25)-E_u(0.25)` | 两个方向内部短距离集中度之差 | 已在第 5 节解释 |
| `S(i,j)=exp(theta |q_i-q_j|)` | economic-distance gravity adjustment | 已在第 9 节解释 |
| `Q(m)` | 宽度 0.25 的收入对角窗口内流量占比 | 已在第 10 节解释 |
| `Q_null=0.25^2=0.0625` | 独立均匀匹配下滑动窗口面积 | 已在第 10 节解释 |
| 四个 clustering features | endpoint intensity、asymmetry、U-depth、mean Q | 已在第 10 节概括 |

## 图文一致性审计

| 位置 | 冲突 | 当前处理 |
|---|---|---|
| Fig. 1d caption | 把经济距离带写成靠近 `anti-diagonal`；图面与方法实际围绕 main diagonal | 采用图面和 `|q_o-q_d|` 定义，并标注图注错字 |
| Fig. 2d 与正文 | 图中 observed mean 为 `0.524`，正文近似写 `0.53` | 视为合理四舍五入，笔记同时保留精确图值与近似正文值 |
| Fig. 3f caption 与图面/正文 | caption 写 positive `r=0.67`；图面和正文写 `r=-0.67`，且异号象限解释要求负相关 | 采用 `r=-0.67`，显式标注原文错误 |
| Fig. 6b 与正文 | 正文称 90/109，即 83% 改善；figure inset 标 79% | 不合并为单一精确值，只保留“多数城市”结论并等待作者更正 |
| Fig. 6 caption 的 `Delta RMSE` | 定义为 `BGM-EGM`，却说负值代表 EGM 改善 | 按代数应为正值代表 EGM RMSE 更低，笔记标注符号错误 |

## 项目迁移边界

1. `0.25` 是收入分位距离，不是地理距离、中心半径或灾害外移阈值。
2. `theta` 是平常时期 OD 横截面关联参数，不是灾后 mobility conductance 的直接测量。
3. 方向指标必须同时区分流量总量与方向内部集中度；`DB` 与 `E_u/E_d` 不能互换。
4. 项目中的群体分析应保留原始地理位移、中心异常和经济秩距离三个不同维度。
