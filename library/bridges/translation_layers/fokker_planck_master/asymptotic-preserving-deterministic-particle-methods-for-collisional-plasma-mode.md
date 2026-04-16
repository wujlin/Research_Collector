---
title: "Asymptotic-preserving deterministic particle methods for collisional plasma models"
authors: ["Yan Huang", "Li Wang"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154427746"
pdf_url: "https://arxiv.org/pdf/2604.09484"
topics: ["bridges/translation_layers/fokker_planck_master", "bridges/translation_layers", "bridges", "statistical_physics/collective_structure/phase_transitions", "statistical_physics/collective_structure", "statistical_physics", "ai_for_physics/generative_dynamics", "ai_for_physics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

We develop novel asymptotic-preserving (AP) deterministic particle methods for collisional plasma models, including both Landau--Fokker--Planck and Dougherty collision operators, under hydrodynamic scaling. Our schemes treat the non-stiff transport part explicitly and the stiff collision operators fully implicitly through the energy-conserving Jordan--Kinderlehrer--Otto (JKO) schemes by exploiting their gradient flow structures. This approach extends our previous work on the space-homogeneous Landau equation [arXiv:2409.12296] and introduces a new treatment of the Dougherty operator via a projected gradient flow formulation. We identify the crucial role of Jacobian log-determinant evaluation in stiff regimes and introduce an inner-time quadrature strategy that improves both accuracy and efficiency. Furthermore, we uncover intriguing connections with score-based transport modeling, showing that both explicit and implicit score matching arise as special cases of our unified variational framework and exhibit limitations in the stiff regime. We also develop practical large-scale implementations via neural network parameterization and efficient training strategies. Various numerical exa

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[translation_layers]]
- [[bridges]]
- [[phase_transitions]]
- [[collective_structure]]
- [[statistical_physics]]
- [[generative_dynamics]]
- [[ai_for_physics]]

## Notes

