---
title: "Diffusion models with physics-guided inference for solving partial differential equations"
authors: ["Yi Bing", "Liu Jia", "Fu Jinyang", "Peng Xiang"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7149874381"
pdf_url: "https://arxiv.org/pdf/2604.01242"
topics: ["ai_for_physics", "ai_for_physics/physics_informed_modeling/physics_informed_generative", "ai_for_physics/generative_dynamics", "ai_for_physics/physics_informed_modeling"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Diffusion models have recently emerged as powerful stochastic frameworks for high-dimensional inference and generation. However, existing applications to partial differential equations (PDEs) predominantly rely on physics-informed training strategies, which tightly couple learning with specific governing equations and limit generalization across problem settings. In this work, we propose a diffusion model with physics-guided inference for solving PDEs, in which the diffusion model is trained using standard data-driven procedures, while physical laws are incorporated exclusively during the reverse inference stage. The reverse diffusion dynamics is guided by a PDE residual energy function, combined with Gaussian smoothing and explicit boundary enforcement, yielding a physically consistent stochastic iteration that is independent of the training process. From a numerical standpoint, the proposed framework can be interpreted as a diffusion-inspired implicit solver that converges to the PDE solution even when initialized from random noise and perturbed by stochastic fluctuations. The method is validated on classical PDE equation such as Poisson, Diffusion, and Burgers equations with var

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[physics_informed_generative]]
- [[generative_dynamics]]
- [[physics_informed_modeling]]

## Notes

