---
title: "Score-fPINN: Fractional Score-Based Physics-Informed Neural Networks for High-Dimensional Fokker-Planck-Lévy Equations"
authors: ["George Em Karniadakis", "Kenji Kawaguchi", "Zheyuan Hu", "Zhongqiang Zhang"]
year: 2026
journal: "Communications in Computational Physics"
doi: "10.4208/cicp.oa-2024-0201"
arxiv: ""
url: "https://openalex.org/W4399795376"
pdf_url: "https://arxiv.org/pdf/2406.11676"
topics: ["bridges/translation_layers/fokker_planck_master", "ai_for_physics", "ai_for_physics/generative_dynamics/score_matching", "bridges", "ai_for_physics/generative_dynamics", "ai_for_physics/physics_informed_modeling", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 50.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

We introduce an innovative approach for solving high-dimensional Fokker-Planck-Lévy (FPL) equations in modeling non-Brownian processes across disciplines such as physics, finance, and ecology. We utilize a fractional score function and Physical-informed neural networks (PINN) to lift the curse of dimensionality (CoD) and alleviate numerical overflow from exponentially decaying solutions with dimensions. The introduction of a fractional score function allows us to transform the FPL equation into a second-order partial differential equation without fractional Laplacian and thus can be readily solved with standard physics-informed neural networks (PINNs). We propose two methods to obtain a fractional score function: fractional score matching (FSM) and score-fPINN for fitting the fractional score function. While FSM is more cost-effective, it relies on known conditional distributions. On the other hand, score-fPINN is independent of specific stochastic differential equations (SDEs) but requires evaluating the PINN model’s derivatives, which may be more costly. We conduct our experiments on various SDEs and demonstrate numerical stability and effectiveness of our method in dealing with

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[score_matching]]
- [[bridges]]
- [[generative_dynamics]]
- [[physics_informed_modeling]]
- [[translation_layers]]

## Notes

