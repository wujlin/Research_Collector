---
title: "Fokker-Planck Analysis and Invariant Laws for a Continuous-Time Stochastic Model of Adam-Type Dynamics"
authors: ["Kaj Nyström"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7149210606"
pdf_url: "https://arxiv.org/pdf/2604.00840"
topics: ["stochastic_analysis", "bridges/translation_layers/fokker_planck_master", "stochastic_analysis/stochastic_dynamics/sde_theory", "bridges", "stochastic_analysis/stochastic_dynamics", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

We develop a continuous-time model for the long-term dynamics of adaptive stochastic optimization, focusing on bias-corrected Adam-type methods. Starting from a finite-sum setting, we identify a canonical scaling of learning rates, decay parameters, and gradient noise that yields a coupled, time-inhomogeneous stochastic differential equation for the parameters $x_t$, first-moment tracker $z_t$, and second-moment tracker $y_t$. Bias correction persists via explicit time-dependent coefficients, and the dynamics becomes asymptotically time-homogeneous. We analyze the associated Fokker-Planck equation and, under mild regularity and dissipativity assumptions on $f$, prove existence and uniqueness of invariant measures. Noise propagation is governed by $A(x)=\mathrm{Diag}(\nabla f(x))H_f(x)$. Hypoellipticity may fail on $\mathcal D_A\times\mathbb R^m\times(\mathbb R_+)^m$, where \[ \mathcal D_A=\{x\in\mathbb R^m:\exists j,\ e_j^\top A(x)=0\}\subset\{x:\det A(x)=0\}=\mathcal D_A^\dagger, \] and critical points of $f$ lie in $\mathcal D_A$. We show $\mathcal D_A^\dagger\neq\mathbb R^m$ and use this to prove exponential convergence of the Markov semigroup $μ_0P_t$ to a unique invariant meas

## Key Contributions

(待补充)

## Connections

- [[stochastic_analysis]]
- [[fokker_planck_master]]
- [[sde_theory]]
- [[bridges]]
- [[stochastic_dynamics]]
- [[translation_layers]]

## Notes

