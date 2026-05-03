---
title: "Equation Map for Speed-Accuracy Relations for Diffusion Models"
source_digest: "./speed-accuracy-relations-for-diffusion-models.md"
source_mineru: "../../pdfs/2026-04-28/speed-accuracy-trade-off-for-diffusion-models/speed-accuracy-trade-off-for-diffusion-models.mineru/hybrid_auto/speed-accuracy-trade-off-for-diffusion-models.md"
date_created: "2026-04-30"
---

# Equation Map

这个文件用于防止精读笔记漏掉或折叠原文公式。后续展开 digest 时，原则是：

第一，原文公式使用 `Eq. (n)` 或 `Eq. (A1)` 这类编号。

第二，笔记中为了解释而新增的中间推导不使用原文编号，可以写成“由 Eq. (n) 推出”。

第三，如果某个公式只被口头概括，没有展示推导，要在状态里标成“待展开”，避免误以为已经读完。

## 主文公式覆盖

| 原文公式 | 作用 | 当前笔记状态 | 后续动作 |
|---|---|---|---|
| Eq. (1)-Eq. (4) | forward Fokker--Planck、Langevin SDE、真实 reverse process、estimated reverse continuity equation | 已展开 | 已补 reverse-time notation 和 estimated reverse continuity equation |
| Eq. (5)-Eq. (15) | score matching、probability flow ODE、flow matching、estimated reverse generation | 已展开 | 已补 optimization、SDE reverse velocity、probability-flow velocity、flow-matching reverse velocity |
| Eq. (16)-Eq. (25) | linear force、conditional Gaussian transition、conditional objectives、$T_t$ 与 $f_t$ 的 schedule 参数化 | 已展开 | 已补 conditional objectives、argmins、由 mean/covariance moment equations 反推 Eq. (22)-Eq. (23)、temperature condition、Gaussian mean/covariance |
| Eq. (26)-Eq. (35) | VE、VP/DDPM、rescaled variable 与 schedule geometry | 已展开 | 已补 VE、VP、cosine、DDIM-style rescaled variable Eq. (33)-Eq. (35) |
| Eq. (36)-Eq. (40) | entropy production、system entropy、bath entropy、total entropy | 已展开 | Eq. (36)-Eq. (40) 已补编号 |
| Eq. (41)-Eq. (51) | path probability、forward/backward path KL、fluctuation-theorem framing、estimated path measure | 已展开 | 已补 dual dynamics、transition kernels、path products、path KL、fluctuation theorem、estimated reverse path |
| Eq. (52)-Eq. (58) | Wasserstein distance、coupling、metric properties、Kantorovich--Rubinstein duality | 已展开 | 已补 coupling、metric properties、Kantorovich duality |
| Eq. (59)-Eq. (62) | Gaussian case 的 $W_2$ closed form 与 Benamou--Brenier endpoint setup | 已展开 | 已补 Gaussian $W_2$、isotropic simplification、dynamic endpoint setup |
| Eq. (63)-Eq. (70) | thermodynamic speed limit、$v_2(t)$、global path length、geodesic constant speed | 已展开 | 已补 global/local speed limit、constant-speed geodesic equality |
| Eq. (71)-Eq. (76) | observable speed limit、$r$-observable 版本、最优 observable | 已展开 | 已补 observable speed、Cauchy--Schwarz、$v_r$、optimal observable $r^*$ |
| Eq. (77)-Eq. (83) | main speed-accuracy relation、conservative version、instantaneous version、loss-speed hierarchy | 已重点展开 | Eq. (77)-Eq. (83) 的主线编号已补齐 |
| Eq. (84)-Eq. (91) | Eq. (77) 的证明：$W_1$ duality、density difference、Cauchy--Schwarz、时间积分 | 已重点展开 | 已补 Eq. (84)-Eq. (91)，包括 derivative sign cases Eq. (89)-Eq. (90) |
| Eq. (92)-Eq. (95) | lower bound、dimension dependence、cosine / cond-OT schedule cost comparison | 已展开 | 已补 speed-cost lower bound、conditional kinetic energy、cond-OT 直线、cosine 圆弧 |
| Eq. (96)-Eq. (99) | Swiss-roll / Gaussian-mixture toy data、velocity expression、non-conservative force setup | 已展开 | 已补 Gaussian mixture velocity Eq. (97)-Eq. (98)、Appendix G 的后验加权推导、Fig. 6(a)-(e) panel 级解读、Swiss-roll force Eq. (99) 和 Fig. 7(a)-(f) panel 级解读 |
| Eq. (100) | incomplete estimation 时的 generalized bound | 已展开 | 已补 $D_{\max}$、training residual、退回 Eq. (77) 的条件 |
| Eq. (101)-Eq. (103) | 与 thermodynamic uncertainty relation、Wasserstein stability bound 的比较 | 已展开 | 已补 TUR Cauchy--Schwarz、SADM Cauchy--Schwarz、ML convergence bound 对比 |

## Appendix 公式覆盖

| Appendix 公式 | 作用 | 当前笔记状态 | 后续动作 |
|---|---|---|---|
| Eq. (A1)-Eq. (A7) | conditional objective 与 marginal objective 的梯度等价 | 已展开 | 已补 score matching / flow matching 两条梯度等价链 |
| Eq. (B1)-Eq. (B11) | conditional Gaussian 的 $\mu_t$、$\Sigma_t$ 与 schedule 参数化 | 已展开 | 已补 mean/covariance moment equations 和 $m_t,\sigma_t$ 解 |
| Eq. (C1)-Eq. (C6) | rescaled variable 下的 Fokker--Planck 推导 | 已展开 | 已补 Jacobian、chain rule、drift cancellation、effective diffusion |
| Eq. (D1)-Eq. (D11) | path KL 与 entropy production 的证明 | 已展开 | 已补 dual backward path、ordinary backward path、system/bath split |
| Eq. (E1) | Pearson $\chi^2$ divergence 保持常数的证明 | 已展开 | 已补共同 transport 下 $D_{\tau-t}$ 常数与 $\mathcal{W}_1$ 可变的区别 |
| Eq. (F1)-Eq. (F6) | incomplete estimation 的 generalized bound 推导 | 已展开 | 已补 residual velocity term、instantaneous bound、time-integrated Eq. (100) 来源 |
| Eq. (G1)-Eq. (G21) | 数值实验、non-conservative force、Gaussian-mixture velocity、OT velocity estimation、image experiment 估计量 | 已展开 | 已补一维 mixture velocity、Swiss-roll mean/covariance、kernel OT velocity、Fig. 8(a)-(c) panel 级解读、image latent speed cost 与 $D_0$ 估计 |

## 当前最高优先级补漏

1. 主文 Eq. (1)-Eq. (103) 已逐号覆盖。
2. Appendix Eq. (A1)-Eq. (G21) 已逐号覆盖。
3. 后续如果继续精读，可以转向图表逐 panel 对齐，而不是继续补公式编号。
