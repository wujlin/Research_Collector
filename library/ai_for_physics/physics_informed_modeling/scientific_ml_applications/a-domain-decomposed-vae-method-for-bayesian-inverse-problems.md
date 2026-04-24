---
title: "A domain-decomposed VAE method for Bayesian inverse problems"
authors: ["Zhihang Xu", "Yingzhi Xia", "Qifeng Liao"]
year: 2023
journal: "ArXiv"
doi: "10.48550/arXiv.2301.05708"
arxiv: "2301.05708"
url: "https://www.semanticscholar.org/paper/bb8dc16e249054a6309c1acaedda9699174192b7"
pdf_url: ""
topics: ["ai_for_physics", "ai_for_physics/physics_informed_modeling", "ai_for_physics/physics_informed_modeling/scientific_ml_applications"]
tier: 0
citations: 10
relevance_score: 57.82
collected: "2026-04-23"
status: "unread"
source: "semantic_scholar"
---

## Abstract

Bayesian inverse problems are often computationally challenging when the forward model is governed by complex partial differential equations (PDEs). This is typically caused by expensive forward model evaluations and high-dimensional parameterization of priors. This paper proposes a domain-decomposed variational auto-encoder Markov chain Monte Carlo (DD-VAE-MCMC) method to tackle these challenges simultaneously. Through partitioning the global physical domain into small subdomains, the proposed method first constructs local deterministic generative models based on local historical data, which provide efficient local prior representations. Gaussian process models with active learning address the domain decomposition interface conditions. Then inversions are conducted on each subdomain independently in parallel and in low-dimensional latent parameter spaces. The local inference solutions are post-processed through the Poisson image blending procedure to result in an efficient global inference result. Numerical examples are provided to demonstrate the performance of the proposed method.

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[physics_informed_modeling]]
- [[scientific_ml_applications]]

## Notes

