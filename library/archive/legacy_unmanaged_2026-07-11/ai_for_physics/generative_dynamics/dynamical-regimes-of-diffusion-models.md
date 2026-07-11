---
title: "Dynamical regimes of diffusion models"
authors: ["Giulio Biroli", "Tony Bonnaire", "Valentin de Bortoli", "Marc Mézard"]
year: 2024
journal: "Nature Communications"
doi: "10.1038/s41467-024-54281-3"
arxiv: ""
url: "https://www.nature.com/articles/s41467-024-54281-3"
pdf_url: "https://www.nature.com/articles/s41467-024-54281-3.pdf"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics", "ai_for_physics/generative_dynamics/sde_generative", "statistical_physics", "statistical_physics/collective_structure/phase_transitions", "bridges/translation_layers/fokker_planck_master"]
tier: 1
citations: 65
relevance_score: 0
collected: "2026-04-11"
status: "unread"
source: "manual"
---

## Abstract

(待填充)

## Key Contributions

- Uses statistical-physics methods to characterize the backward dynamics of diffusion models in the joint large-dimension and large-dataset limit.
- Identifies three regimes in the backward generative process: noise, speciation, and collapse.
- Relates speciation to symmetry breaking and collapse to a glass-like condensation mechanism.
- Connects speciation time to covariance-spectrum structure and collapse time to an excess-entropy criterion.

## Connections

- [[ai_for_physics]]
- [[generative_dynamics]]
- [[sde_generative]]
- [[statistical_physics]]
- [[phase_transitions]]
- [[fokker_planck_master]]

## Notes

### Reading Frame

这篇不是泛泛地把 diffusion model 用到物理问题，而是反过来用统计物理去解释 diffusion model 的 backward dynamics。

### Problem

核心问题是：在高维和大样本极限下，diffusion model 的反向生成过程到底处于什么动力学机制之下，以及它什么时候是在 generalize，什么时候会走向 memorization。

### Why Care

这篇值得读，因为它把生成模型里通常被经验性描述的问题，翻译成了统计物理语言：

- `speciation` 对应类别结构的形成
- `collapse` 对应向训练样本的塌缩
- curse of dimensionality 则体现在何时不可避免地进入 collapse regime

### Objects

- forward noising process
- backward generative process
- exact empirical score
- high-dimensional data distribution

### Evolution Structure

阅读时优先抓住三个 regime：

1. pure-noise regime
2. speciation regime
3. collapse regime

再去看切换时间为什么分别由谱结构和熵结构控制。

### Quantities

核心量包括：

- speciation time
- collapse time
- covariance-spectrum structure
- excess entropy

### Method Role

方法层不是训练技巧，而是统计物理分析：

- large-\(d\), large-\(n\) limit
- Gaussian mixture toy models
- backward diffusion dynamics analysis
- real-dataset numerical checks

### Evidence

证据主要看：

- Gaussian mixture 是否给出完整解析图像
- speciation / collapse 时间是否能由数据结构估计
- CIFAR-10、ImageNet、LSUN 是否支持三阶段结构

### Reproduction Path

更合适的 toy 路线是：

1. 从 two-cluster Gaussian mixture 开始。
2. 写出 forward noising 与 exact empirical score。
3. 观察 backward trajectories 何时出现 class commitment，何时出现 sample collapse。

