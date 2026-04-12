---
title: "Non-Markovian Entropy Dynamics in Living Systems from the Keldysh Formalism"
authors: ["Fang Liu", "Min Guo", "Hongwei Tan", "Yang Wang"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7135428729"
pdf_url: "https://arxiv.org/pdf/2603.12184"
topics: ["statistical_physics", "statistical_physics/non_equilibrium_dynamics/nonequilibrium", "statistical_physics/non_equilibrium_dynamics/fluctuation_theorems", "statistical_physics/non_equilibrium_dynamics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-08"
status: "unread"
source: "openalex"
---

## Abstract

Living systems are open nonequilibrium systems that continuously exchange energy, matter, and information with their environments, leading to stochastic dynamics with memory and active fluctuations. In this study, we develop a non-Markovian theoretical framework for the entropy dynamics of living systems based on the Keldysh functional formalism and stochastic thermodynamics. The approach naturally incorporates colored environmental noise, memory-dependent dissipation, and many-body interactions, yielding generalized Langevin dynamics and non-Markovian master equations. Within this framework we derive an exact frequency-domain expression for the entropy production rate and show that violations of the fluctuation-dissipation relation provide a direct thermodynamic signature of active biological fluctuations. We further demonstrate that environmental memory enhances low-frequency fluctuations and entropy production, leading to critical slowing down near dynamical instability. These results provide a microscopic physical foundation for the entropy "bathtub" picture of living systems and connect entropy evolution with development, aging, and death in nonequilibrium dynamics.

## Key Contributions

- Develops a non-Markovian stochastic thermodynamic framework for living systems with memory, colored noise, and active fluctuations.
- Derives an exact frequency-domain expression for entropy production rate using the Keldysh formalism.
- Shows how memory enhances low-frequency fluctuations and entropy production, especially near dynamical instability.

## Connections

- [[statistical_physics]]
- [[nonequilibrium]]
- [[fluctuation_theorems]]
- [[non_equilibrium_dynamics]]

## Notes

### Reading Frame

这篇的角色不是替代 Markov 随机热力学，而是在 `memory + colored noise + active fluctuations` 的条件下把熵动力学推广到非马尔可夫情形。

### Problem

核心问题是：当系统存在记忆核、色噪声和活性涨落时，entropy dynamics 应该如何写，entropy production rate 又如何定义和计算。

### Objects

- open living systems
- non-Markovian stochastic dynamics
- entropy dynamics / entropy production rate

### Evolution Structure

优先确认以下动力学对象如何进入框架：

- `generalized Langevin dynamics`
- `non-Markovian master equation`
- colored noise
- memory-dependent dissipation

### Quantities

这篇的核心量包括：

- entropy production rate
- `fluctuation-dissipation relation` violation
- low-frequency fluctuation enhancement

### FDR Violation 与 TUR 的关系

这篇最自然的入口不是 `TUR`，而是 `FDR violation`，因为它直接操作的是频域中的相关函数和响应函数，而不是轨迹上的净流。

- `FDR violation` 问的是：自发涨落与线性响应是否还满足平衡态中的对应关系。
- `TUR` 问的是：如果系统维持了一个稳定的净流，而且这个净流的相对波动很小，那么至少需要多少 entropy production。

两者都在用涨落读不可逆性，但层次不同：

- `FDR violation` 更接近 `correlation / response layer`
- `TUR` 更接近 `path / current layer`

### Method Role

方法层要看清 `Keldysh formalism` 在这里承担什么任务：

1. 它是否主要用来写出带记忆的动力学。
2. 它是否进一步给出可计算的 entropy formula。

### Evidence

证据主要来自：

- 是否给出 exact expression
- memory 是否增强 low-frequency fluctuations 和 entropy production
- near-instability 行为是否来自理论推导而不是纯数值现象

### Reproduction Path

更合适的 toy 路线是：

1. 从 Markov Langevin 开始。
2. 加入一个简单 memory kernel。
3. 比较 entropy production 或 correlation structure 是否发生系统性变化。
