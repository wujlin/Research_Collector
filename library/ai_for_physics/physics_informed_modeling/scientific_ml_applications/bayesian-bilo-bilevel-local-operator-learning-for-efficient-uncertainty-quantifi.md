---
title: "Bayesian BiLO: Bilevel Local Operator Learning for Efficient Uncertainty Quantification of Bayesian PDE Inverse Problems with Low-Rank Adaptation"
authors: ["Ray Zirui Zhang", "Christopher E Miles", "Xiaohui Xie", "John S. Lowengrub"]
year: 2025
journal: "bioRxiv"
doi: "10.64898/2026.01.11.698927"
arxiv: "2507.17019"
url: "https://www.semanticscholar.org/paper/58cb15730911b110b97ffbd3a692b54c1318f599"
pdf_url: ""
topics: ["ai_for_physics", "ai_for_physics/physics_informed_modeling", "ai_for_physics/physics_informed_modeling/scientific_ml_applications"]
tier: 0
citations: 1
relevance_score: 52.01
collected: "2026-04-23"
status: "unread"
source: "semantic_scholar"
---

## Abstract

Uncertainty quantification in PDE inverse problems is essential in many applications. Scientific machine learning and AI enable data-driven learning of model components while preserving physical structure, and provide the scalability and adaptability needed for emerging imaging technologies and clinical insights. We develop a Bilevel Local Operator Learning framework for Bayesian inference in PDEs (B-BiLO). At the upper level, we sample parameters from the posterior via Hamiltonian Monte Carlo, while at the lower level we fine-tune a neural network via low-rank adaptation (LoRA) to approximate the solution operator locally. B-BiLO enables efficient gradient-based sampling without synthetic data or adjoint equations and avoids sampling in high-dimensional weight space, as in Bayesian neural networks, by optimizing weights deterministically. We analyze errors from approximate lower-level optimization and establish their impact on posterior accuracy. Numerical experiments across PDE models, including tumor growth, demonstrate that B-BiLO achieves accurate and efficient uncertainty quantification. MSC Classification: 65M32, 62F15, 68T07

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[physics_informed_modeling]]
- [[scientific_ml_applications]]

## Notes

