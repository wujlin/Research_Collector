---
title: "Equation Map for Predicting human mobility flows in cities using deep learning on satellite imagery"
source_digest: "./predicting-human-mobility-flows-in-cities-using-deep-learning-on-satellite-imagery.md"
source_mineru: "../../pdfs/2026-05-01/predicting-human-mobility-flows-in-cities-using-deep-learning-on-satellite-imagery/predicting-human-mobility-flows-in-cities-using-deep-learning-on-satellite-imagery.mineru/predicting-human-mobility-flows-in-cities-using-deep-learning-on-satellite-imagery/auto/predicting-human-mobility-flows-in-cities-using-deep-learning-on-satellite-imagery.md"
date_created: "2026-05-08"
---

# Equation Map

## Main Text Formula Coverage

| Original Formula | Role | Digest Status | Next Action |
|---|---|---|---|
| Eq. (1) | Encode two augmented satellite views into image representations | expanded | no action |
| Eq. (2) | Project image representations into contrastive latent space | expanded | no action |
| Eq. (3) | NT-Xent contrastive loss for self-supervised satellite embedding | expanded | no action |
| Eq. (4) | Raw GAT attention score using node and edge features | expanded | no action |
| Eq. (5) | Softmax normalization of attention weights over neighbors | expanded | no action |
| Eq. (6) | GAT message passing and node feature update | expanded | no action |
| Eq. (7) | Bilinear OD flow decoder from origin and destination embeddings | expanded | no action |
| Eq. (8) | BMC Loss for imbalanced log-flow regression | expanded | no action |
| Eq. (9) | Radiation Model baseline | expanded | no action |
| Eq. (10a) | Unconstrained Gravity Model baseline | expanded | no action |
| Eq. (10b) | Singly constrained Gravity Model baseline | expanded | no action |
| Eq. (11a) | Deep Gravity-P baseline using population and distance | expanded | no action |
| Eq. (11b) | Deep Gravity-V baseline using visual features and distance | expanded | no action |
| Eq. (12) | RMSE evaluation metric | expanded | no action |
| Eq. (13) | MAE evaluation metric | expanded | no action |
| Eq. (14) | CPC OD matrix similarity metric | expanded | no action |

## Supplementary Formula Coverage

| Original Formula | Role | Digest Status | Next Action |
|---|---|---|---|
| Supplementary Eq. (1)-Eq. (3d) | KL/JS divergence used to compare observed and predicted distance distributions | referenced only | expand only if doing supplementary digest |
| Supplementary Eq. (4)-Eq. (6) | Candidate distance-decay distributions: exponential, power law, truncated power law | referenced only | expand only if doing morphology/statistical-test note |
| Supplementary Eq. (7)-Eq. (8) | Akaike weight and AIC calculation | referenced only | expand only if doing morphology/statistical-test note |

## Figure Coverage

| Figure | Role | Digest Status | Next Action |
|---|---|---|---|
| Fig. 1a | Ten US MSAs used as study areas | expanded | no action |
| Fig. 1b | Job-rank distribution / centrality motivation | expanded | no action |
| Fig. 1c | Imagery2Flow architecture | expanded | no action |
| Fig. 2a-Fig. 2f | New York prediction maps and grouped CPC analysis | expanded | no action |
| Fig. 3a-Fig. 3j | Observed vs predicted distance distributions across ten MSAs | expanded | no action |
| Fig. 4a-Fig. 4d | Spatial heterogeneity and land use/cover groups in New York | expanded | no action |
| Fig. 5a-Fig. 5d | Cross-city transfer matrices | expanded | no action |
| Fig. 6 | Land cover distributions used to explain transferability | expanded | no action |

## Notation Choices

| Source Object | Digest Symbol | Note |
|---|---|---|
| satellite image of area i | $v_i$ | The digest uses $v_i$ consistently for the image patch of area $i$. |
| image embedding | $r_i$ | Same concept as spatial context embedding. |
| GAT hidden state | $h_i$ | Initial $h_i$ can be read as image embedding; later layers are spatially contextualized embeddings. |
| OD flow | $y_{ij}$ | Ground-truth flow from origin $i$ to destination $j$. |
| predicted OD flow | $\hat y_{ij}$ | Model output. |
| distance | $d_{ij}$ | Driving route distance between tract centroids. |
| origin total outflow | $O_i$ | Used by Radiation Model and constrained Gravity Model. |
