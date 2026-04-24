---
title: "Adaptive Probability Flow Residual Minimization for High-Dimensional Fokker-Planck Equations"
authors: ["Xiaolong Wu", "Qi Liao"]
year: 2025
journal: "ArXiv"
doi: "10.48550/arXiv.2512.19196"
arxiv: "2512.19196"
url: "https://www.semanticscholar.org/paper/5c7c196b0c7c2e8325b2ef8f1561d2e12af8ba41"
pdf_url: ""
topics: ["bridges/translation_layers/fokker_planck_master", "ai_for_physics", "ai_for_physics/generative_dynamics/score_matching", "bridges", "ai_for_physics/generative_dynamics", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 52.0
collected: "2026-04-23"
status: "unread"
source: "semantic_scholar"
---

## Abstract

Solving high-dimensional Fokker-Planck (FP) equations is a challenge in computational physics and stochastic dynamics, due to the curse of dimensionality (CoD) and unbounded domains. Existing deep learning approaches, such as Physics-Informed Neural Networks, face computational challenges as dimensionality increases, driven by the $O(d^2)$ complexity of automatic differentiation for second-order derivatives. While recent probability flow approaches bypass this by learning score functions or matching velocity fields, they often involve serial operations or depend on sampling efficiency in complex distributions. To address these issues, we propose the Adaptive Probability Flow Residual Minimization (A-PFRM) method. The second-order FP equation is reformulated as an equivalent first-order deterministic Probability Flow ODE (PF-ODE) constraint, which avoids explicit Hessian computation. Unlike score matching or velocity matching, A-PFRM solves FP equations by minimizing the residual of the continuity equation induced by the PF-ODE. By utilizing Continuous Normalizing Flows combined with the Hutchinson Trace Estimator, the training complexity is reduced to a linear scale of $O(d)$, achi

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[score_matching]]
- [[bridges]]
- [[generative_dynamics]]
- [[translation_layers]]

## Notes

