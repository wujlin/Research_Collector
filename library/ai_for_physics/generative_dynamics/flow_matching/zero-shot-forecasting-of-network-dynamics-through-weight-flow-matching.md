---
title: "Zero-Shot Forecasting of Network Dynamics through Weight Flow Matching"
authors: ["Shihe Zhou", "Ruikun Li", "Huandong Wang", "Xiao Song"]
year: 2026
journal: ""
doi: "10.1145/3774904.3792722"
arxiv: ""
url: "https://openalex.org/W4415318709"
pdf_url: "https://arxiv.org/pdf/2510.07957"
topics: ["ai_for_physics/generative_dynamics", "ai_for_physics", "ai_for_physics/generative_dynamics/flow_matching"]
tier: 0
citations: 0
relevance_score: 47.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Forecasting state evolution of network systems, such as the spread of information on social networks, is significant for effective policy interventions and resource management. However, the underlying propagation dynamics constantly shift with new topics or events, which are modeled as changing coefficients of the underlying dynamics. Deep learning models struggle to adapt to these out-of-distribution shifts without extensive new data and retraining. To address this, we present Zero-Shot Forecasting of Network Dynamics through Weight Flow Matching (FNFM), a generative, coefficient-conditioned framework that generates dynamic model weights for an unseen target coefficient, enabling zero-shot forecasting. Our framework utilizes a Variational Encoder to summarize the forecaster weights trained in observed environments into compact latent tokens. A Conditional Flow Matching (CFM) module then learns a continuous transport from a simple Gaussian distribution to the empirical distribution of these weights, conditioned on the dynamical coefficients. This process is instantaneous at test time and requires no gradient-based optimization. Across varied dynamical coefficients, empirical result

## Key Contributions

(待补充)

## Connections

- [[generative_dynamics]]
- [[ai_for_physics]]
- [[flow_matching]]

## Notes

