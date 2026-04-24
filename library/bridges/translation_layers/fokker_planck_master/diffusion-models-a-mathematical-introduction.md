---
title: "Diffusion Models: A Mathematical Introduction"
authors: ["Sepehr Maleki", "Negar Pourmoazemi"]
year: 2025
journal: "arXiv"
doi: ""
arxiv: "2511.11746"
url: "http://arxiv.org/abs/2511.11746v1"
pdf_url: "https://arxiv.org/pdf/2511.11746v1"
topics: ["bridges/translation_layers/fokker_planck_master", "ai_for_physics", "ai_for_physics/generative_dynamics/ddpm", "ai_for_physics/generative_dynamics/conditional_generation", "bridges", "ai_for_physics/generative_dynamics", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 56.0
collected: "2026-04-23"
status: "unread"
source: "arxiv"
---

## Abstract

We present a concise, self-contained derivation of diffusion-based generative models. Starting from basic properties of Gaussian distributions (densities, quadratic expectations, re-parameterisation, products, and KL divergences), we construct denoising diffusion probabilistic models from first principles. This includes the forward noising process, its closed-form marginals, the exact discrete reverse posterior, and the related variational bound. This bound simplifies to the standard noise-prediction goal used in practice. We then discuss likelihood estimation and accelerated sampling, covering DDIM, adversarially learned reverse dynamics (DDGAN), and multi-scale variants such as nested and latent diffusion, with Stable Diffusion as a canonical example. A continuous-time formulation follows, in which we derive the probability-flow ODE from the diffusion SDE via the continuity and Fokker-Planck equations, introduce flow matching, and show how rectified flows recover DDIM up to a time re-parameterisation. Finally, we treat guided diffusion, interpreting classifier guidance as a posterior score correction and classifier-free guidance as a principled interpolation between conditional a

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[ddpm]]
- [[conditional_generation]]
- [[bridges]]
- [[generative_dynamics]]
- [[translation_layers]]

## Notes

