---
title: "Leveraging Nested MLMC for Sequential Neural Posterior Estimation with Intractable Likelihoods"
authors: ["Xiliang Yang", "Yifei Xiong", "Zhijian He"]
year: 2026
journal: "SIAM Journal on Scientific Computing"
doi: "10.1137/24m1635685"
arxiv: ""
url: "https://openalex.org/W4391421138"
pdf_url: "https://arxiv.org/pdf/2401.16776"
topics: []
tier: 0
citations: 0
relevance_score: 32.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

There is a growing interest in studying sequential neural posterior estimation (SNPE) techniques due to their advantages for simulation-based models with intractable likelihoods. The methods aim to learn the posterior from adaptively proposed simulations using neural network-based conditional density estimators. As an SNPE technique, the automatic posterior transformation (APT) method proposed by Greenberg et al. (2019) performs well and scales to high-dimensional data. However, the APT method requires computing the expectation of the logarithm of an intractable normalizing constant, i.e., a nested expectation. Although atomic proposals were used to render an analytical normalizing constant, it remains challenging to analyze the convergence of learning. In this paper, we reformulate APT as a nested estimation problem. Building on this, we construct several multilevel Monte Carlo (MLMC) estimators for the loss function and its gradients to accommodate different scenarios, including two unbiased estimators, and a biased estimator that trades a small bias for reduced variance and controlled runtime and memory usage. We also provide convergence results of stochastic gradient descent to

## Key Contributions

(待补充)

## Connections

(待添加)

## Notes

