---
title: "Paper Queue"
date: "2026-04-16"
updated: "2026-04-16T24:00"
focus: "AI + Generative Models ↔ Physics 交叉"
---

# Paper Queue 2026-04-16

重点方向：**AI / 生成模型与物理的交叉**，兼顾随机热力学-生成模型桥梁。

---

## Core Queue — AI / 生成模型核心（含已读与基础参考）

2026-04-28 口径修正：这个队列不再等同于“下一篇必读”。`DDPM`、`Score-Based SDE` 和 `Flow Matching` 是基础参考层，时间上已经比较早，适合在概念断点出现时回读；当前推进位应优先给更新的桥接论文、城市动力学和直接服务 `Synthetic_City` 的方法文献。

### 1. Nonequilibrium physics of generative diffusion models
- **Phys. Rev. E** 111, 014111 (2025) | Tier 2 | Rel: 64
- 期刊口碑: `trusted` — APS 核心期刊，统计物理 / 非线性动力学 / 随机系统方向的标杆刊物
- Authors: **Zhendong Yu; Haiping Huang**
- Topics: `非平衡动力学` `涨落定理`
- 把非平衡统计物理直接用于分析生成扩散模型，**最贴合研究主线的桥梁论文**

### 2. Generative optimal transport via forward-backward HJB matching
- **arXiv** (2026) | 预印本
- 期刊口碑: `preprint` — 尚未正式发表，但作者信号极强
- Authors: **Haiqian Yang; Vishaal Krishnan; Sumit Sinha; L. Mahadevan** (Harvard University)
- Topics: `flow_matching` `最优传输`
- HJB + 最优传输 + 生成模型，Mahadevan 是 Harvard 顶级应用数学家

### 3. Score-Based Generative Modeling through Stochastic Differential Equations
- **ICLR** (2021) | Tier 2 | Rel: 56
- 期刊口碑: `trusted` — 三大 ML 顶会之一，接收率 ~25%，领域标杆
- Authors: **Yang Song; Jascha Sohl-Dickstein; Diederik P. Kingma; Abhishek Kumar**
- Topics: `Fokker-Planck` `SDE理论` `score_matching`
- Current status: `foundational_reference_not_next_read`
- Song et al. 是 SDE ↔ score-based diffusion 的奠基工作，但不应被误读成当前下一篇必读。它的作用是补基础口径：forward SDE、reverse-time SDE、score、probability flow ODE 如何统一。

### 4. Flow Matching for Generative Modeling
- **ICLR** (2023) | Tier 2 | Rel: 60
- 期刊口碑: `trusted` — 同上，三大 ML 顶会之一
- Authors: **Yaron Lipman; Ricky T. Q. Chen; Heli Ben-Hamu; Maximilian Nickel** (Meta AI)
- Topics: `flow_matching` `最优传输`
- Current status: `foundational_reference_not_next_read`
- Lipman et al. 是 flow matching 经典，但它更适合作为 HJB matching / probability-flow / OT path 的背景参考，不再放在当前主线推进位。

### 5. Diffusion Models: A Mathematical Introduction
- **arXiv** (2025) | 预印本 | Rel: 56
- 期刊口碑: `preprint` — 综述性预印本，无期刊声誉加持，但内容覆盖完整
- Authors: **Sepehr Maleki; Negar Pourmoazemi**
- Topics: `Fokker-Planck` `DDPM` `条件生成`
- 扩散模型的数学综述，从 FP 方程到 DDPM 全链路

### 6. A Primer on Variational Inference for Physics-Informed Deep Generative Modelling
- **arXiv** (2024) | 预印本 | Rel: 52
- 期刊口碑: `preprint` — 未发表，但 EPFL Fink 组出品，机构信号很强
- Authors: **Emilia Molinari; Michele Nervi; Luca Biggio; François Fleuret; Olga Fink** (EPFL)
- Topics: `physics_informed_generative` `variational_free_energy`
- 变分推断 + 物理约束生成模型的入门综述

### 7. A framework for the use of generative modelling in non-equilibrium statistical mechanics
- **arXiv** (2024) | 预印本 | Rel: 52
- 期刊口碑: `preprint` — 未发表，但 **Karl Friston** 出品，作者本身就是最强信号
- Authors: **Karl Friston; Rosalyn Moran; Lancelot Da Costa; Chris Fields**
- Topics: `非平衡动力学` `physics_informed_generative` `信息几何`
- 自由能原理创始人，将生成模型直接用于非平衡统计力学

### 8. Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective
- **arXiv** (2026) | 预印本 | Rel: 51
- 期刊口碑: `preprint` — 未发表，但 **Takahiro Sagawa**（东大）是非平衡信息热力学领域权威
- Authors: **Takahiro Sagawa** (University of Tokyo)
- Topics: `非平衡动力学`
- 把随机热力学拓展到 Transformer / RNN 等自回归生成模型

### 9. HJ-sampler: A Bayesian sampler for inverse problems via Hamilton-Jacobi PDEs and score-based generative models
- **arXiv** (2024) | 预印本 | Rel: 54
- 期刊口碑: `preprint` — 未发表，**Karniadakis** 是 PINN 创始人之一（Brown University）
- Authors: **Tingwei Meng; Zongren Zou; Jérôme Darbon; George Em Karniadakis** (Brown University)
- Topics: `SDE生成模型`
- HJB 方程 + score-based 采样解逆问题

### 10. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particles
- **arXiv** (2026) | 预印本 | Rel: 54
- 期刊口碑: `preprint` — UCLA Schaeffer 组，计算 PDE / 科学 ML 方向的专业组
- Authors: **Lingyi Lyu; Xinyue Yu; Hayden Schaeffer** (UCLA)
- Topics: `SDE理论` `非平衡` `scientific_ml`
- 测度值神经网络学习 McKean-Vlasov 动力学

### 11. Diffusion models with physics-guided inference for solving PDEs
- **arXiv** (2026) | 预印本 | Rel: 54
- 期刊口碑: `preprint` — 作者机构信息不详，需文章级核验
- Authors: **Yi Bing; Liu Jia; Fu Jinyang; Peng Xiang**
- Topics: `physics_informed_generative`
- 用物理引导推断的扩散模型求解 PDE

### 12. Denoising Diffusion Probabilistic Models
- **NeurIPS** (2020) | Tier 2 | Rel: 51
- 期刊口碑: `trusted` — ML 领域最顶级会议之一，接收率 ~20%
- Authors: **Jonathan Ho; Ajay Jain; Pieter Abbeel** (UC Berkeley)
- Topics: `DDPM`
- Current status: `foundational_reference_not_next_read`
- Ho et al. 是 DDPM 经典，但时间上更早，适合作为前向加噪、ELBO 和 $\epsilon$-prediction 的基础参考，不作为当前下一篇精读优先项。

### 13. Lipschitz regularity in Flow Matching and Diffusion Models
- **arXiv** (2026) | 预印本 | Rel: 52
- 期刊口碑: `preprint` — 单作者理论工作，需文章级核验
- Authors: **Arthur Stéphanovitch**
- Topics: `flow_matching`
- Flow matching / diffusion model 的 Lipschitz 正则性理论与最优采样率

---

## Must Read — 数学骨架 / 桥梁层 (5 篇)

### 14. Fokker-Planck Analysis and Invariant Laws for Continuous-Time Stochastic Adam
- **arXiv** (2026) | 预印本
- 期刊口碑: `preprint` — **Kaj Nyström**（Uppsala University）是 PDE / 自由边界问题方向知名学者
- Authors: **Kaj Nyström** (Uppsala University)
- Topics: `Fokker-Planck` `SDE理论`
- 用 FP 方程分析 Adam 优化器的随机连续时间模型

### 15. Numerical approximation of McKean–Vlasov SDEs via stochastic gradient descent
- **Advances in Applied Probability** (2026) | Tier 2 | Rel: 64
- 期刊口碑: `trusted` — Applied Probability Trust 旗下核心期刊，概率论和随机过程方向的标杆刊物
- Authors: **Ankush Agarwal (Western U.); Alessandro Amato; Stefano Pagliarani (U. Bologna); Gonçalo dos Reis**
- Topics: `SDE理论` `非平衡`
- McKean-Vlasov SDE + SGD 数值方法

### 16. Attaining physics-driven convolutional operators by architecture design
- **Communications Physics** (2026) | Tier 2 | Rel: 61
- 期刊口碑: `trusted` — Nature Portfolio 旗下物理通讯期刊，IF ≈ 5.5，有良好领域信号
- Authors: **Zhenhua Xiong; Pengyang Zhao** (Shanghai Jiao Tong University)
- Topics: `scientific_ml_applications`
- 通过架构设计实现物理驱动的卷积算子

### 17. Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuations
- **arXiv** (2025) | 预印本 | Rel: 54
- 期刊口碑: `preprint` — Sirignano / Dechant 在随机热力学 × 机器学习交叉有前期积累
- Authors: **Justin Sirignano; Andrea Dechant** et al.
- Topics: `SDE生成` `信息几何` `variational_free_energy`
- 直接从相关函数和轨迹涨落学习随机热力学

### 18. The covariant Langevin equation of diffusion on Riemannian manifolds
- **Rep. Math. Phys.** (2024) | Tier 2 | Rel: 55
- 期刊口碑: `trusted` — 数学物理领域老牌期刊（Reports on Mathematical Physics），偏理论
- Authors: **Lajos Diósi**
- Topics: `Fokker-Planck` `SDE理论`
- 流形上的协变 Langevin 方程，几何扩散理论基础

---

## 参考级 — 纯统计物理背景 (5 篇)

质量高但主要为理论背景阅读，不直接涉及 AI/生成模型。

### 19. Macroscopic Stochastic Thermodynamics
- **Reviews of Modern Physics** 97(1), 015002 (2025) | Tier 1
- 期刊口碑: `trusted` — 物理学界**最权威的综述期刊**，IF ≈ 54，极度精选（年发 ~40 篇）
- Authors: Gianmaria Falasco; **Massimiliano Esposito** (University of Luxembourg)
- Esposito 是随机热力学方向全球最顶尖学者之一

### 20. Efficient quantum thermal simulation
- **Nature** (2025) | Tier 1
- 期刊口碑: `trusted` — 全球最顶级综合科学期刊，IF ≈ 64
- Authors: **Chi-Fang Chen** (Caltech) et al.

### 21. Thermodynamic inference in partially accessible Markov networks
- **Physical Review X** 12, 031025 (2022) | Tier 2
- 期刊口碑: `trusted` — APS 旗舰开放获取刊物，高选择性（接收率 ~7%），物理学最佳 OA 期刊之一
- Authors: **Udo Seifert** (University of Stuttgart) — 非平衡热力学推断领域奠基人

### 22. Stochastic thermodynamics of a quantum dot coupled to a finite-size reservoir
- **Physical Review Letters** 131, 220405 (2023) | Tier 1
- 期刊口碑: `trusted` — APS 旗舰快报期刊，IF ≈ 8.6，物理学最高声望期刊之一
- Authors: Saulo V. Moreira; Peter Samuelsson; Patrick P. Potts

### 23. Unified formalism for entropy productions and fluctuation relations
- **Physical Review E** 101, 022129 (2020) | Tier 2
- 期刊口碑: `trusted` — APS 核心期刊，统计物理、非线性动力学、软物质方向标杆
- Authors: **Ying-Jen Yang; Hong Qian** — Qian 是随机热力学 / 非平衡过程数学理论方向知名学者

---

## 期刊口碑速查表

| 期刊 | Tier | 口碑 | 说明 |
|------|------|------|------|
| **Nature** | 1 | trusted | 全球顶级综合科学，IF ≈ 64 |
| **Science** | 1 | trusted | 全球顶级综合科学，IF ≈ 56 |
| **Science Advances** | 1 | trusted | AAAS 旗下 OA 期刊，IF ≈ 13 |
| **Nature Communications** | 1 | trusted | Nature Portfolio 高影响力广谱 OA，IF ≈ 17 |
| **Reviews of Modern Physics** | 1 | trusted | 物理学最权威综述刊，IF ≈ 54，年仅 ~40 篇 |
| **Physical Review Letters** | 1 | trusted | APS 旗舰快报，IF ≈ 8.6，物理学最高声望 |
| **Physical Review X** | 2 | trusted | APS 旗舰 OA，接收率 ~7%，极度精选 |
| **Physical Review E** | 2 | trusted | APS 核心刊，统计物理 / 非线性 / 随机系统标杆 |
| **Physical Review Research** | 2 | trusted | APS OA 研究刊，选择性低于 PRX 但领域信号好 |
| **J. Stat. Mech.** | 2 | trusted | 统计力学核心领域刊 (IOP) |
| **J. Stat. Phys.** | 2 | trusted | 理论统计物理方向老牌核心刊 |
| **J. Chem. Phys.** | 2 | trusted | 化学物理 / 统计力学核心刊 (AIP)，IF ≈ 3.5 |
| **J. Phys. A** | 2 | trusted | 数学 / 理论物理核心刊 (IOP) |
| **Communications Physics** | 2 | trusted | Nature Portfolio 物理通讯，IF ≈ 5.5 |
| **SciPost Physics** | 2 | trusted | 社区驱动 OA，理论 / 统计物理方向口碑好 |
| **NeurIPS** | 2 | trusted | ML 顶会，接收率 ~20% |
| **ICML** | 2 | trusted | ML 顶会，接收率 ~25% |
| **ICLR** | 2 | trusted | ML 顶会，接收率 ~25% |
| **Adv. Appl. Prob.** | 2 | trusted | 应用概率核心刊 |
| **Lett. Math. Phys.** | 2 | trusted | 数学物理方向快报刊 |
| **Arch. Rational Mech. Anal.** | 2 | trusted | 理性力学 / 分析力学顶级刊 |
| **J. Differ. Equ.** | 2 | trusted | 微分方程方向核心刊 |
| **Rep. Math. Phys.** | 2 | trusted | 数学物理领域老牌期刊 |
| **Quantum** | 2 | trusted | 量子物理 OA 期刊，口碑好 |
| **Atmospheric Meas. Tech.** | 3 | trusted | 大气观测方法刊 |
| **Preprints.org** | 0 | preprint | 预印本平台，无同行评审 |
| **arXiv** | 0 | preprint | 预印本平台，无同行评审，**需看作者机构背书** |

---

## 今日 Top 5 推荐

| # | 论文 | 期刊/口碑 | 理由 |
|---|------|-----------|------|
| 1 | Nonequilibrium physics of generative diffusion models | PRE / trusted | 非平衡物理 ↔ 扩散模型的直接桥梁 |
| 2 | Generative optimal transport via forward-backward HJB | arXiv / Mahadevan (Harvard) | HJB + OT + 生成模型，顶级组 |
| 3 | Stochastic Thermodynamics for Autoregressive Generative Models | arXiv / Sagawa (东大) | 随机热力学拓展到 Transformer/RNN |
| 4 | A Primer on Variational Inference for Physics-Informed Generative | arXiv / EPFL Fink 组 | 变分推断 + 物理约束生成入门综述 |
| 5 | A framework for generative modelling in non-eq stat mech | arXiv / Friston (UCL) | 自由能原理创始人 × 非平衡生成模型 |
