---
title: "Paper Queue"
digest_type: "paper_queue"
date: "2026-04-13"
---

# Paper Queue 2026-04-13

这份队列专门回答一个问题：

`除了已经精读过的 3 篇文章之外，下一批最值得读什么？`

这里默认排除：

1. `Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents`
2. `Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility`
3. `Dynamical regimes of diffusion models`

筛选顺序按三条线综合：

1. 研究主题是否继续推进你当前主线
2. 期刊口碑是否足够稳
3. 作者和机构是否真是这个方向的专业团队

## Next Batch: Must Read

### 1. Non-Markovian rock-paper-scissors games

- Venue: `Physical Review Research`
- Venue reputation: `trusted`
- Authors: `Ohad Vilk, Mauro Mobilia, Michael Assaf`
- Institutions: `The Hebrew University of Jerusalem`, `University of Leeds`
- Why now:
  这是你下一篇最该接上的文章。它直接把 `Markov -> non-Markov` 的转变放进一个可解析的 nonequilibrium model 里，和你刚读完的 coarse-grained irreversibility 主线衔接最紧。
- Why team:
  `Michael Assaf` 和 `Mauro Mobilia` 这条作者线是做 stochastic population dynamics / nonequilibrium processes 的专业组，不是临时跨题材发文。
- Why venue:
  `PRResearch` 对你这条主线是够硬的 domain venue，信号明显强于一般综合 OA 期刊。
- Read as:
  `非马尔可夫 waiting-time / memory 对 master-equation 类动力学和 species survival 规则到底改了什么`
- URL:
  https://doi.org/10.1103/4mm1-943p

## Next Batch: Fast Review

### 2. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

- Venue: `arXiv`
- Venue reputation: `preprint`
- Authors: `Lingyi Lyu, Xinyue Yu, Hayden Schaeffer`
- Institutions: `Michigan State University`, `UCLA`
- Why review, not must read:
  这篇的 topic 很贴你后面可能会走的 `trajectory -> drift inference -> interacting particle systems` 线，而且 `Hayden Schaeffer` 这条 scientific ML / applied math 线是专业的；但它目前还是 preprint，应该先做快速筛读，不要直接给和 `PRResearch` 同等级的信任。
- Read as:
  `能不能把单粒子轨迹学习，推进到 measure-dependent drift / McKean-Vlasov dynamics`
- URL:
  https://arxiv.org/abs/2604.00333

### 3. A framework for the use of generative modelling in non-equilibrium statistical mechanics

- Venue: `Proceedings of the Royal Society A`
- Venue reputation: `trusted`
- Authors: `Karl Friston, Maxwell J. D. Ramstead, Dalton A. R. Sakthivadivel`
- Institutions:
  `University College London` author线最明确；这条线在 free-energy principle / active inference 方向是专业团队，但争议也比前几篇更大。
- Why fast review, not must read:
  这篇和你当前主线的关键词贴得最直接：`generative modelling + non-equilibrium statistical mechanics`。但它更像一个概念框架和语言桥，而不是像 `PRResearch` 那篇那样给出清晰可计算机制。所以适合快速筛读，用来判断它是否真的能给你方法论增量。
- Read as:
  `它到底是在提供可操作的统计物理框架，还是主要在用 free-energy principle 重新包装非平衡系统语言`
- URL:
  https://doi.org/10.1098/rspa.2025.0538

## Excluded From Current Queue

### Boundary layers, transport and universal distribution in boundary driven active systems

- Venue: `SciPost Physics`
- Venue reputation: `trusted`
- Authors: `Pritha Dolai, Arghya Das`
- Institutions: `NIT Karnataka`, `Max Planck Institute for Physics and Medicine`, `Institute of Mathematical Sciences`
- Why excluded:
  这篇的质量信号不差，但它的对象是 boundary-driven active matter / material transport。它不直接推进当前的 `Synthetic_City` 主线，也不直接补城市 migration、spatial expansion、census-to-PUMA inverse problem 或 generative-model 数学骨架。
- Why team:
  虽然不是最顶级大团队，但机构和作者背景是专业的 theoretical/statistical physics 线，不是泛工程或泛 AI 文章。
- Why venue:
  `SciPost Physics` 是靠谱的 physics flagship open-access venue，审稿标准比一般开放获取期刊严得多。
- Read as:
  `仅作为 active-matter / material-transport 旁支保留，不进入当前必读队列`
- URL:
  https://scipost.org/SciPostPhys.19.4.088

## Reproduction Candidates Only

### Score-fPINN: Fractional Score-Based Physics-Informed Neural Networks for High-Dimensional Fokker-Planck-Lévy Equations

- Venue: `Communications in Computational Physics`
- Venue reputation: `cautious`
- Institutions: `Pacific Northwest National Laboratory`, `National University of Singapore`, `Worcester Polytechnic Institute`, `John Brown University`
- Why not in next reading batch:
  主题看起来很贴 `score + Fokker-Planck`，但这篇更适合当方法复现实验的灵感，不适合当你下一批重点阅读文献。原因是：venue 虽然正规，但在这条线上的独立信号明显弱于 `JCP`、`SciPost Physics` 或更强的 field venue；文章题目也更偏 numerical method / PINN 组合，而不是你当前最需要的理论桥接。
- Use as:
  `如果你要做一个 1D/2D Fokker-Planck + score residual 的 toy，拿它当复现参考`
- URL:
  https://openalex.org/W4399795376

## Hold

- `Efficient quantum thermal simulation`
  Why hold:
  文章质量很高，作者和机构都很强，但它要求一定的量子信息 / 量子热化基础。你已经决定先跳过它，等补完量子力学和相关背景后再回读更合适。

- `Predictor-Driven Diffusion for Spatiotemporal Generation`
  Why hold:
  主题和你后面的 generative dynamics 有交集，但目前还是很新的 preprint，作者团队和文章影响力还没有稳定信号。先放观察位，不进入下一批主阅读。

- `Probabilistic Evolution of Black Hole Thermodynamic States via Fokker-Planck Equation`
  Why hold:
  题目表面贴主线，但目前更像把 Fokker-Planck 语言放到特定物理对象上，不是你现在最需要的“可迁移方法”文章。

- `Non-equilibrium Dynamical Attractors and Thermalisation of Charm Quarks in Nuclear Collisions at the LHC Energy`
  Why hold:
  物理背景太专门，虽然也是 nonequilibrium 和 thermalisation，但迁移价值不如前面三篇。

## Suggested Order

如果这周只读 3 篇，顺序建议是：

1. `Non-Markovian rock-paper-scissors games`
2. `MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data`
3. `A framework for the use of generative modelling in non-equilibrium statistical mechanics`

如果还有余力，再加：

4. `Efficient quantum thermal simulation`（以后补量子基础后回读）

## One-Line Summary

下一批最值得读的，不是 `CiCP + score/PINN` 那篇，也不是 active-matter material transport 旁支，而是：

`PRResearch 的 non-Markov nonequilibrium model -> MVNN 的 particle-data bridge -> Proc. R. Soc. A 的 generative / non-equilibrium 概念桥`
