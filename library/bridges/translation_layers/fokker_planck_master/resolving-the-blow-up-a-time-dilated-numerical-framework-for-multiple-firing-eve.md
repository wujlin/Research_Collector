---
title: "Resolving the Blow-Up: A Time-Dilated Numerical Framework for Multiple Firing Events in Mean-Field Neuronal Networks"
authors: ["Xu’an Dou", "Louis Tao", "Zhe Xue", "Zhennan Zhou"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7140001660"
pdf_url: "https://arxiv.org/pdf/2603.18475"
topics: ["bridges/translation_layers/fokker_planck_master", "statistical_physics", "statistical_physics/collective_structure/phase_transitions", "bridges", "statistical_physics/collective_structure", "bridges/translation_layers"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

In large-scale excitatory neuronal networks, rapid synchronization manifests as {multiple firing events (MFEs)}, mathematically characterized by a finite-time blow-up of the neuronal firing rate in the mean-field Fokker-Planck equation. Standard numerical methods struggle to resolve this singularity due to the divergent boundary flux and the instantaneous nature of the population voltage reset. In this work, we propose a robust {multiscale numerical framework based on time dilation}. By transforming the governing equation into a dilated timescale proportional to the firing activity, we desingularize the blow-up, effectively stretching the instantaneous synchronization event into a resolved mesoscopic process. This approach is shown to be physically consistent with the {microscopic cascade mechanism} underlying MFEs and the system's inherent fragility. To implement this numerically, we develop a hybrid scheme that utilizes a {mesh-independent flux criterion} to switch between timescales and a semi-analytical ``moving Gaussian'' method to accurately evolve the post-blowup Dirac mass. Numerical benchmarks demonstrate that our solver not only captures steady states with high accuracy b

## Key Contributions

(待补充)

## Connections

- [[fokker_planck_master]]
- [[statistical_physics]]
- [[phase_transitions]]
- [[bridges]]
- [[collective_structure]]
- [[translation_layers]]

## Notes

