---
title: "A deep learning framework for jointly solving transient Fokker-Planck equations with arbitrary parameters and initial distributions"
authors: ["Xiaolong Wang", "Jing Feng", "Qi Liu", "Chengli Tan", "Yuanyuan Liu", "Yong Xu"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7152933521"
pdf_url: "https://arxiv.org/pdf/2604.06001"
topics: ["bridges/translation_layers/fokker_planck_master", "bridges/translation_layers", "bridges"]
tier: 0
citations: 0
relevance_score: 51.0
collected: "2026-04-13"
status: "unread"
source: "openalex"
---

## Abstract

Efficiently solving the Fokker-Planck equation (FPE) is central to analyzing complex parameterized stochastic systems. However, current numerical methods lack parallel computation capabilities across varying conditions, severely limiting comprehensive parameter exploration and transient analysis. This paper introduces a deep learning-based pseudo-analytical probability solution (PAPS) that, via a single training process, simultaneously resolves transient FPE solutions for arbitrary multi-modal initial distributions, system parameters, and time points. The core idea is to unify initial, transient, and stationary distributions via Gaussian mixture distributions (GMDs) and develop a constraint-preserving autoencoder that bijectively maps constrained GMD parameters to unconstrained, low-dimensional latent representations. In this representation space, the panoramic transient dynamics across varying initial conditions and system parameters can be modeled by a single evolution network. Extensive experiments on paradigmatic systems demonstrate that the proposed PAPS maintains high accuracy while achieving inference speeds four orders of magnitude faster than GPU-accelerated Monte Carlo si

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[translation_layers]]
- [[bridges]]

## Notes

