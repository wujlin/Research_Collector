---
title: "Stochastic Dimension Implicit Functional Projections for Exact Integral Conservation in High-Dimensional PINNs"
authors: ["Zhangyong Liang"]
year: 2026
journal: "arXiv (Cornell University)"
doi: ""
arxiv: ""
url: "https://openalex.org/W7148178057"
pdf_url: "https://arxiv.org/pdf/2603.29237"
topics: ["ai_for_physics", "ai_for_physics/physics_informed_modeling", "ai_for_physics/physics_informed_modeling/scientific_ml_applications"]
tier: 0
citations: 0
relevance_score: 36.0
collected: "2026-04-08"
status: "unread"
source: "openalex"
---

## Abstract

Enforcing exact macroscopic conservation laws, such as mass and energy, in neural partial differential equation (PDE) solvers is computationally challenging in high dimensions. Traditional discrete projections rely on deterministic quadrature that scales poorly and restricts mesh-free formulations like PINNs. Furthermore, high-order operators incur heavy memory overhead, and generic optimization often lacks convergence guarantees for non-convex conservation manifolds. To address this, we propose the Stochastic Dimension Implicit Functional Projection (SDIFP) framework. Instead of projecting discrete vectors, SDIFP applies a global affine transformation to the continuous network output. This yields closed-form solutions for integral constraints via detached Monte Carlo (MC) quadrature, bypassing spatial grid dependencies. For scalable training, we introduce a doubly-stochastic unbiased gradient estimator (DS-UGE). By decoupling spatial sampling from differential operator subsampling, the DS-UGE reduces memory complexity from $\mathcal{O}(M \times N_{\mathcal{L}})$ to $\mathcal{O}(N \times |\mathcal{I}|)$. SDIFP mitigates sampling variance, preserves solution regularity, and maintain

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[physics_informed_modeling]]
- [[scientific_ml_applications]]

## Notes

