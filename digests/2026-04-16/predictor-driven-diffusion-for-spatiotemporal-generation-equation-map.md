---
title: "Equation Map for Predictor-Driven Diffusion for Spatiotemporal Generation"
source_digest: "./predictor-driven-diffusion-for-spatiotemporal-generation.md"
source_mineru: "../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/predictor-driven-diffusion-for-spatiotemporal-generation.md"
date_created: "2026-05-04"
---

# Equation Map

这份索引用来检查 `predictor-driven-diffusion-for-spatiotemporal-generation.md` 是否按原文公式顺序覆盖。状态中的“已展开”表示 digest 不只是贴公式，还解释了公式引入目的、符号含义、推导关系和下一步作用。

## Main Text Formula Coverage

| Original Formula | Role | Digest Status | Note |
|---|---|---|---|
| Eq. (1) | forward RG diffusion, Laplacian damping plus noise | 已展开 | 解释 $\lambda$ 轴、Fourier damping、noise 的 RG 作用 |
| Eq. (2) | reverse-$\lambda$ diffusion with true path score | 已展开 | 解释 score 与 super-resolution |
| Eq. (3) | closed-form forward solution | 已展开 | 解释 $\mathcal{C}_\lambda$、$\Sigma_\lambda$、$\epsilon$ |
| Eq. (4) | conditional coarse-grained path density | 已展开 | 解释 product over time slices 与 causality |
| Eq. (5) | marginal path density $q_\lambda$ | 已展开 | 解释对 fine paths 的 marginalization |
| Eq. (6) | physical-time stochastic governing equation | 已展开 | 区分 $\xi$ 与 $\eta_\lambda$ |
| Eq. (7) | predictor-induced path density | 已展开 | 解释 path energy、$r_\lambda$、$Z_\lambda$、path score |
| Eq. (8) | KL divergence to regression loss | 已展开 | 展开代入 Eq. (7) 后哪些项与 $\theta$ 无关 |
| Eq. (9) | final scale-averaged training objective | 已展开 | 解释 $\lambda$ sampling 与 $1/\sigma_\lambda^2$ weighting |
| Eq. (10) | approximate optimal drift intuition | 已展开 | 解释先 fine drift 后 coarse-graining 的算子顺序 |
| Eq. (11) | reverse-$\lambda$ inference with predictor-induced score | 已展开 | 解释 generation / super-resolution 共同采样方程 |

## Appendix A Formula Coverage

| Original Formula | Role | Digest Status | Note |
|---|---|---|---|
| Eq. (12)-Eq. (13) | Fourier transform and inverse transform | 已展开 | 作为 Laplacian diagonalization 的准备 |
| Eq. (14)-Eq. (15) | Fourier-space OU process and solution | 已展开 | 解释每个 mode 独立演化 |
| Eq. (16) | Fourier-space conditional Gaussian density | 已展开 | 由 OU 解读 mean / variance |
| Eq. (17)-Eq. (18) | $\widetilde{\mathcal{C}}_\lambda(k)$ and $\widetilde{\Sigma}_\lambda(k)$ | 已展开 | 解释 cutoff、zero mode、$\lambda\to0$ |
| Eq. (19)-Eq. (23) | Carosso RG, bare density, partition function, effective action | 已展开 | 连接 RG marginalization 与 path action |
| Eq. (24)-Eq. (27) | Euler-Maruyama discretization, noise density, transition density | 已展开 | 展开从 white noise 到 transition density 的变量替换 |
| Eq. (28)-Eq. (30) | product transition density to path-integral form | 已展开 | 展开 product、finite difference、compact integral notation |
| Eq. (31) | effective path action | 已展开 | 解释 path residual energy |
| Eq. (32)-Eq. (36) | Markov formulation via state augmentation | 已展开 | 解释 history window 不破坏 Markov 口径 |
| Eq. (37)-Eq. (40) | true fine dynamics and joint density | 已展开 | 作为 KL minimization 推导准备 |
| Eq. (41)-Eq. (44) | KL minimization and conditional increment optimum | 已展开 | 展开为什么平方损失最优解是 conditional mean |
| Eq. (45)-Eq. (50) | optimal drift connected to fine-resolution dynamics | 已展开 | 展开 law of iterated expectations 和 Eq. (10) 来源 |
| Eq. (51)-Eq. (54) | Tweedie correction and Gaussian posterior specialization | 已展开 | 解释 denoising correction 的 score 形式 |
| Eq. (55)-Eq. (58) | noise amplitude $\sigma_\lambda$ derivation | 已展开 | 展开 trace matching 和 score divergence regularization |

## Appendix B-D Formula Coverage

| Original Formula | Role | Digest Status | Note |
|---|---|---|---|
| Eq. (59)-Eq. (60) | two-scale Lorenz-96 model | 已展开 | 解释 slow/fast coupling and timescale separation |
| Eq. (61)-Eq. (62) | Kolmogorov flow vorticity equations | 已展开 | 解释 vorticity, stream function, velocity |
| Eq. (63)-Eq. (64) | relative $L^2$ and spectral error | 已展开 | 解释 short-term vs long-run statistical metric |
| Eq. (65) | Langevin corrector step | 已展开 | 解释 predictor-corrector sampling |
| Eq. (66) | ETD reverse-$\lambda$ update | 已展开 | 解释 anti-diffusion stiffness and noise treatment |
| Eq. (67) | Laplacian-augmented variance-preserving process | 已展开 | 用于 Figure 13-14 ablation |
| Eq. (68) | deterministic coarse-graining without noise | 已展开 | 用于 Figure 15-16 noise ablation |

## Figure / Table Coverage

| Original Object | Role | Digest Status | Note |
|---|---|---|---|
| Figure 1 | two-axis framework | 已展开 | 解释 $t$ vs $\lambda$ |
| Figure 2-Figure 4 | main simulation / super-resolution results | 已展开 | 主文图均插入并解释 |
| Table 1-Table 3 | simulation, generation, super-resolution metrics | 已展开 | 表格数值已整理 |
| Figure 5-Figure 9 | appendix simulation and generation comparison | 已展开 | 补充说明其与 Table 1-2 的关系 |
| Figure 10-Figure 12 | noise simulation and history window | 已展开 | 连接 $\sigma_\lambda$ 与 Mori-Zwanzig |
| Figure 13-Figure 14 | Laplacian term ablation | 已展开 | 解释 scale-selective suppression |
| Figure 15-Figure 16 | noise injection ablation | 已展开 | 解释 deterministic smoothing failure |
| Figure 17 | FNO robustness | 已展开 | 解释 framework vs backbone |
