---
title: "RRAEDy: adaptive latent linearization of nonlinear dynamical systems"
authors: ["Jad Mounayer", "Sebastian Rodriguez", "Jerome Tomezyk", "Chady Ghnatios", "Francisco Chinesta"]
year: 2026
journal: "Scientific Reports"
doi: "10.1038/s41598-026-47609-0"
arxiv: ""
url: "https://openalex.org/W7152696803"
pdf_url: "https://www.nature.com/articles/s41598-026-47609-0_reference.pdf"
topics: []
tier: 0
citations: 0
relevance_score: 32.0
collected: "2026-04-13"
status: "unread"
source: "openalex"
---

## Abstract

Many existing latent-space models for dynamical systems require the latent dimension to be fixed in advance, rely on tuning loss functions to approximate linear dynamics, and do not regularize the latent variables. We introduce RRAEDy, a model that overcomes these limitations by automatically discovering the appropriate latent dimension while enforcing regularized and approximately linear dynamics in the latent space. RRAEDy builds on Rank-Reduction Autoencoders (RRAEs) and progressively ranks and prunes latent variables based on their singular values. At the same time, it learns a latent Dynamic Mode Decomposition (DMD) operator that governs the temporal evolution of the system. This structure-free yet linearly constrained formulation enables the model to learn stable, low-dimensional dynamics without auxiliary loss terms or manual tuning. In addition, the proposed architecture modifies the latent variables before passing them to the decoder, reducing the need to learn an inverse mapping at the start of training. The stability of the learned DMD operator is proven through a theoretical analysis. Experiments on standard benchmarks, including the Van der Pol oscillator, Burgers’ equ

## Key Contributions

(待补充)

## Connections

(待添加)

## Notes

