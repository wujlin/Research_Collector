---
title: "A Theory-guided Weighted $L^2$ Loss for solving the BGK model via Physics-informed neural networks"
authors: ["Gyounghun Ko", "Sung-Jun Son", "Seung Yeon Cho", "Myeong-Su Lee"]
year: 2026
journal: "arXiv (Cornell University)"
doi: ""
arxiv: ""
url: "https://openalex.org/W7152934029"
pdf_url: "https://arxiv.org/pdf/2604.04971"
topics: ["ai_for_physics", "ai_for_physics/physics_informed_modeling"]
tier: 0
citations: 0
relevance_score: 45.82
collected: "2026-04-15"
status: "unread"
source: "openalex"
---

## Abstract

While Physics-Informed Neural Networks offer a promising framework for solving partial differential equations, the standard $L^2$ loss formulation is fundamentally insufficient when applied to the Bhatnagar-Gross-Krook (BGK) model. Specifically, simply minimizing the standard loss does not guarantee accurate predictions of the macroscopic moments, causing the approximate solutions to fail in capturing the true physical solution. To overcome this limitation, we introduce a velocity-weighted $L^2$ loss function designed to effectively penalize errors in the high-velocity regions. By establishing a stability estimate for the proposed approach, we shows that minimizing the proposed weighted loss guarantees the convergence of the approximate solution. Also, numerical experiments demonstrate that employing this weighted PINN loss leads to superior accuracy and robustness across various benchmarks compared to the standard approach.

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[physics_informed_modeling]]

## Notes

