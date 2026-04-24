---
title: "An Analysis of Regularization and Fokker-Planck Residuals in Diffusion Models for Image Generation"
authors: ["Onno Niemann", "Gonzalo Mart'inez Munoz", "Alberto A. González", "Gonzalo Martínez Muñoz", "Alberto Suárez Gonzalez"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: "2604.15171"
url: "https://www.semanticscholar.org/paper/f769c792e00a9207e5b6ebaf26e39338e287b3fc"
pdf_url: "https://arxiv.org/pdf/2604.15171"
topics: ["bridges/translation_layers/fokker_planck_master", "ai_for_physics", "ai_for_physics/generative_dynamics/score_matching", "bridges", "ai_for_physics/generative_dynamics", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 53.96
collected: "2026-04-23"
status: "unread"
source: "openalex,openalex,openalex,semantic_scholar,semantic_scholar,semantic_scholar"
---

## Abstract

Recent work has shown that diffusion models trained with the denoising score matching (DSM) objective often violate the Fokker--Planck (FP) equation that governs the evolution of the true data density. Directly penalizing these deviations in the objective function reduces their magnitude but introduces a significant computational overhead. It is also observed that enforcing strict adherence to the FP equation does not necessarily lead to improvements in the quality of the generated samples, as often the best results are obtained with weaker FP regularization. In this paper, we investigate whether simpler penalty terms can provide similar benefits. We empirically analyze several lightweight regularizers, study their effect on FP residuals and generation quality, and show that the benefits of FP regularization are available at substantially lower computational cost. Our code is available at https://github.com/OnnoNiemann/fp_diffusion_analysis.

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[score_matching]]
- [[bridges]]
- [[generative_dynamics]]
- [[translation_layers]]

## Notes

