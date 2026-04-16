---
title: "The NTK-Quadratic Form Equivalence of Macroscopic Probability Flow ODEs in Conditional Flow Matching"
authors: ["Zhinan Xiong"]
year: 2026
journal: "Zenodo (CERN European Organization for Nuclear Research)"
doi: "10.5281/zenodo.19465964"
arxiv: ""
url: "https://openalex.org/W7152250469"
pdf_url: ""
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/sde_generative", "ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 50.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

We establish a formal equivalence between the macroscopic probability flow ODE governing diffusion-based generative models and a Neural Tangent Kernel (NTK)-dominated quadratic form. Starting from the observation that practical diffusion model training---whether DDPM, score-based, or flow matching---instantiates a Gaussian Markov process whose continuous-time limit is an Ito SDE, we trace a closed logical chain: (1) the Fokker-Planck equation collapses the stochastic dynamics into a deterministic probability flow ODE; (2) the CFM gradient equivalence theorem shows that minimizing the conditional flow matching MSE is equivalent to fitting the ODE vector field; (3) decomposing the marginal vector field over data sub-families reveals a quadratic loss structure governed by a data interference matrix Omega; (4) mapping from output space to parameter space via the network Jacobian yields an NTK-twisted quadratic form. By logical substitution, the NTK quadratic form directly characterizes the macroscopic ODE flow. No additional assumptions beyond standard engineering pragmatism (smoothness, Gaussian transitions, finite dimensionality) are required---the equivalence is an intrinsic propert

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[sde_generative]]
- [[flow_matching]]
- [[generative_dynamics]]

## Notes

