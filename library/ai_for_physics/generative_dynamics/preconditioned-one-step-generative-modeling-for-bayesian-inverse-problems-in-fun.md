---
title: "Preconditioned One-Step Generative Modeling for Bayesian Inverse Problems in Function Spaces"
authors: ["Z. Cheng", "Li-Lian Wang", "Zhongjian Wang"]
year: 2026
journal: ""
doi: ""
arxiv: "2603.14798"
url: "https://www.semanticscholar.org/paper/781b96f955c9fab5390d0e908e5fd142347d48c4"
pdf_url: ""
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 42.0
collected: "2026-04-23"
status: "unread"
source: "semantic_scholar"
---

## Abstract

We propose a machine-learning algorithm for Bayesian inverse problems in the function-space regime based on one-step generative transport. Building on the Mean Flows, we learn a fully conditional amortized sampler with a neural-operator backbone that maps a reference Gaussian noise to approximate posterior samples. We show that while white-noise references may be admissible at fixed discretization, they become incompatible with the function-space limit, leading to instability in inference for Bayesian problems arising from PDEs. To address this issue, we adopt a prior-aligned anisotropic Gaussian reference distribution and establish the Lipschitz regularity of the resulting transport. Our method is not distilled from MCMC: training relies only on prior samples and simulated partial and noisy observations. Once trained, it generates a $64\times64$ posterior sample in $\sim 10^{-3}$s, avoiding the repeated PDE solves of MCMC while matching key posterior summaries.

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[generative_dynamics]]

## Notes

