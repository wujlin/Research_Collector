---
title: "Predictor-Driven Diffusion for Spatiotemporal Generation"
authors: ["Yuki Yasuda", "Tobias Bischoff"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7149210441"
pdf_url: "https://arxiv.org/pdf/2604.00327"
topics: ["statistical_physics", "statistical_physics/collective_structure/phase_transitions", "ai_for_physics", "ai_for_physics/generative_dynamics/conditional_generation", "statistical_physics/collective_structure", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Multiscale spatial structure complicates temporal prediction because small-scale spatial fluctuations influence large-scale evolution, yet resolving all scales is often intractable. Standard diffusion models do not address this problem effectively since they apply uniform decay across all Fourier modes. We propose Predictor-Driven Diffusion, a framework that combines renormalization-group-based spatial coarse-graining with a path-integral formulation of temporal dynamics. The forward process applies scale-dependent Laplacian damping together with additive noise, producing a hierarchy of coarse-grained fields indexed by diffusion scale $λ$. Training minimizes the Kullback-Leibler divergence between data-induced and predictor-induced path densities, leading to a simple regression loss on temporal derivatives. The resulting predictor captures how eliminated small-scale components statistically influence large-scale evolution. A key insight is that the same predictor provides a path score for reverse-$λ$ sampling, unifying simulation, unconditional generation, and super-resolution in a single framework. Our unified approach is validated through experiments on two multiscale turbulent s

## Key Contributions

(待补充)

## Connections

- [[statistical_physics]]
- [[phase_transitions]]
- [[ai_for_physics]]
- [[conditional_generation]]
- [[collective_structure]]
- [[generative_dynamics]]

## Notes

