---
title: "PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration"
authors: ["Yulison Herry", "Julian Evan", "Jeremia Oktavian", "Ferry Faizal"]
year: 2026
journal: "International Journal of Information Technology and Computer Science"
doi: "10.5815/ijitcs.2026.02.08"
arxiv: ""
url: "https://openalex.org/W7143947385"
pdf_url: "https://www.mecs-press.org/ijitcs/ijitcs-v18-n2/IJITCS-V18-N2-8.pdf"
topics: ["stochastic_analysis", "stochastic_analysis/path_foundations/brownian_motion", "bridges/translation_layers/fokker_planck_master", "ai_for_physics", "bridges", "stochastic_analysis/path_foundations", "ai_for_physics/physics_informed_modeling", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 50.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

This study presents a Physics-Informed Neural Network (PINN) framework for modeling stochastic systems like Brownian motion, designed to overcome critical challenges in physical consistency and numerical stability that affect classical solvers and standard data-driven models. Traditional numerical methods often struggle with high-dimensional spaces or sparse data, while many machine learning approaches fail to enforce fundamental physical laws. To address this, our proposed PINN architecture integrates a multi-component loss function that explicitly enforces the Fokker-Planck equation, which describes the system’s governing physics, alongside boundary conditions and a global probability conservation law. This physics-informed approach is anchored by high-fidelity training data generated from Verlet-integrated trajectories of the underlying Langevin dynamics. We validate our model against the analytical solution for one-dimensional Brownian motion, demonstrating its ability to accurately recover the true probability density function (PDF). Rigorous comparisons using statistical metrics show superior accuracy over a canonical data-driven operator learning model, DeepONet. Specificall

## Key Contributions

(待补充)

## Connections

- [[stochastic_analysis]]
- [[brownian_motion]]
- [[fokker_planck_master]]
- [[ai_for_physics]]
- [[bridges]]
- [[path_foundations]]
- [[physics_informed_modeling]]
- [[translation_layers]]

## Notes

