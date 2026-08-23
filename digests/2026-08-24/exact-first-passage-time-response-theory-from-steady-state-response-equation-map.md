---
title: "Equation Map for Exact First-Passage Time Response Theory from Steady-State Response"
source_digest: "./exact-first-passage-time-response-theory-from-steady-state-response.md"
source_pdf: "../../pdfs/2026-08-24/exact-first-passage-time-response/exact-first-passage-time-response.pdf"
arxiv: "2608.11202"
date_created: "2026-08-24"
---

# Equation Map

下标方向沿用原文：`W_mn` 是 `n -> m` 的速率，`tau_kl` 是 `l -> k` 的 MFPT。这个约定若被反转，所有 gain/loss 解释都会反号。

## 主文公式覆盖

| 原文公式 | 作用 | 笔记状态 | 备注 |
|---|---|---|---|
| Eq. (1) | 单条速率有限扰动后的稳态概率更新，Lemma 1 | 已展开 | 第 2 节；后续桥接的输入 |
| Eq. (2) | MFPT 响应与极快重置辅助系统稳态概率响应的对应 | 已重点展开 | 第 3-4 节；全文概念枢纽 |
| Eq. (3a) | 单条有向速率扰动的精确线性 MFPT 响应 | 已重点展开 | 第 5-7 节；由三个未扰动因子构成 |
| Eq. (3b) | 任意强度单边扰动下，有限响应与线性响应的精确关系 | 已重点展开 | 第 5、8-9 节；分母给出 nonlinear screening |
| Eq. (4) | 有限响应的 upstream × gain/loss × screening 因子化 | 已重点展开 | 第 6-8 节；物理解读主式 |
| Eq. (5) | 由线性响应和一个有限响应点重建整条曲线 | 已展开 | 第 9 节 |
| Eq. (6a)-Eq. (6b) | 由扰动后 MFPT 非负得到的两组未扰动 MFPT 不等式 | 已概括 | 第 10 节；未重做补充材料代数 |
| Eq. (7a)-Eq. (7b) | 有帮助与有害边的相对对数响应界限 | 已展开结论 | 第 10 节；给出有限倍率包络 |
| Eq. (8a)-Eq. (8b) | 固定边与固定任务下的响应局部性 | 已展开 | 第 10 节 |
| Eq. (9) | 全网最强 MFPT 加速发生在局部 perturbed-source 到 target 配置 | 已展开结论 | 第 10 节 |
| Eq. (10a) | 稳态概率对物理参数的二阶响应 | 已概括 | 第 9 节只保留与曲线重建有关的含义 |
| Eq. (10b) | MFPT 二阶响应由一阶响应和 screening factor 决定 | 已展开 | 第 9 节 |
| Eq. (11) | 固定目标的 global MFPT 对单边扰动的响应 | 已展开 | 第 13 节；用于澄清 target averaging |

## End Matter 公式覆盖

| 原文公式 | 作用 | 笔记状态 | 备注 |
|---|---|---|---|
| Eq. (12) | MFPT 是极快 `k -> l` 重置边稳态通量的倒数 | 已重点展开 | 第 3 节；更新周期的物理来源 |
| Eq. (13) | 用重置前后辅助稳态概率比再次写出响应对应 | 已展开逻辑 | 第 4 节 |
| Eq. (14) | 对辅助系统应用单边稳态响应恒等式 | 已纳入推导链 | 第 4 节；未逐项重排 |
| Eq. (15) | 任意单边有限扰动后的 MFPT 与辅助稳态概率闭式更新 | 已解释用途 | 第 4-5、14 节 |
| Eq. (16) | 多边稳态响应恒等式 | 已概括 | 第 14 节；与 Lemma 1、Eq. (15) 递归使用 |

## 补充材料覆盖判断

补充材料把主文结果证明和扩展到 72 个编号公式。当前 digest 的目标是完整重建主文论证，而不是复写每一行代数，因此采用以下分层：

| 补充材料部分 | 状态 | 理由 |
|---|---|---|
| MFPT 递推与三角不等式基础 | 已核对 | 支撑 `U >= 0` 与 `Sigma >= 0` |
| fast-reset correspondence 的严格证明 | 已按证明思路展开 | 主文逻辑不可缺 |
| 单边有限响应到 Eq. (3)-Eq. (4) 的代数 | 已核对，未逐行誊写 | 中间消元不增加物理含义 |
| 能量、势垒和全局时间尺度 perturbation sum rules | 未纳入主线 | 主文已注释掉，不是当前版本核心结果 |
| 响应界限 Eq. (67)-Eq. (72) | 已核对结论 | 第 10 节解释 |
| folding example 的额外数值面板 | 已展开 | 第 11 节并保留 Fig. S2 |
| `10^5` 随机网络数值验证 | 已展开 | 第 12 节并保留 Fig. S1 |

## 项目迁移边界

1. 项目中的恢复阈值必须先形成清楚的 target state 或 target set，MFPT 才有定义。
2. `C_peak` 可用于定义或预测初始状态，不等同于任何一个原文响应因子。
3. 观测 OD 量只有在校正暴露人口和驻留时间后才可近似跃迁速率。
4. 若灾后转移率随时间快速变化，应使用 time-inhomogeneous 或 semi-Markov 扩展，不能直接声称 Eq. (3b) 精确成立。
