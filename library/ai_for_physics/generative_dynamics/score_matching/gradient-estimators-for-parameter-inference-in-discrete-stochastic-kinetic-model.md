---
title: "Gradient estimators for parameter inference in discrete stochastic kinetic models"
authors: ["Ludwig Burger", "Annalena Kofler", "Lukas Heinrich", "Ulrich Gerland"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7149873883"
pdf_url: "https://arxiv.org/pdf/2604.02121"
topics: ["ai_for_physics/generative_dynamics/score_matching", "ai_for_physics/generative_dynamics", "ai_for_physics"]
tier: 0
citations: 0
relevance_score: 51.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Stochastic kinetic models are ubiquitous in physics, yet inferring their parameters from experimental data remains challenging. In deterministic models, parameter inference often relies on gradients, as they can be obtained efficiently through automatic differentiation. However, these tools cannot be directly applied to stochastic simulation algorithms (SSA) such as the Gillespie algorithm, since sampling from a discrete set of reactions introduces non-differentiable operations. In this work, we adopt three gradient estimators from machine learning for the Gillespie SSA: the Gumbel-Softmax Straight-Through (GS-ST) estimator, the Score Function estimator, and the Alternative Path estimator. We compare the properties of all estimators in two representative systems exhibiting relaxation or oscillatory dynamics, where the latter requires gradient estimation of time-dependent objective functions. We find that the GS-ST estimator mostly yields well-behaved gradient estimates, but exhibits diverging variance in challenging parameter regimes, resulting in unsuccessful parameter inference. In these cases, the other estimators provide more robust, lower variance gradients. Our results demons

## Key Contributions

(待补充)

## Connections

- [[score_matching]]
- [[generative_dynamics]]
- [[ai_for_physics]]

## Notes

