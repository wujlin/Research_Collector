---
title: "FP-Diffusion: Improving Score-based Diffusion Models by Enforcing the Underlying Score Fokker-Planck Equation"
authors: ["Stefano Ermon", "Chieh-Hsin Lai", "Yuhta Takida", "N. Murata", "Toshimitsu Uesaka", "Yuki Mitsufuji"]
year: 2022
journal: ""
doi: ""
arxiv: "2210.04296"
url: "https://www.semanticscholar.org/paper/b627684e2b9d6f12c88a3791d6eff5aec1c6ce09"
pdf_url: ""
topics: ["bridges/translation_layers/fokker_planck_master", "ai_for_physics", "bridges", "ai_for_physics/generative_dynamics", "bridges/translation_layers"]
tier: 2
citations: 42
relevance_score: 79.1
collected: "2026-04-23"
status: "unread"
source: "semantic_scholar"
---

## Abstract

Score-based generative models (SGMs) learn a family of noise-conditional score functions corresponding to the data density perturbed with increasingly large amounts of noise. These perturbed data densities are linked together by the Fokker-Planck equation (FPE), a partial differential equation (PDE) governing the spatial-temporal evolution of a density undergoing a diffusion process. In this work, we derive a corresponding equation called the score FPE that characterizes the noise-conditional scores of the perturbed data densities (i.e., their gradients). Surprisingly, despite the impressive empirical performance, we observe that scores learned through denoising score matching (DSM) fail to fulfill the underlying score FPE, which is an inherent self-consistency property of the ground truth score. We prove that satisfying the score FPE is desirable as it improves the likelihood and the degree of conservativity. Hence, we propose to regularize the DSM objective to enforce satisfaction of the score FPE, and we show the effectiveness of this approach across various datasets.

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[bridges]]
- [[generative_dynamics]]
- [[translation_layers]]

## Notes

