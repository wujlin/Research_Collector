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

### 2. Boundary layers, transport and universal distribution in boundary driven active systems

- Venue: `SciPost Physics`
- Venue reputation: `trusted`
- Authors: `Pritha Dolai, Arghya Das`
- Institutions: `NIT Karnataka`, `Max Planck Institute for Physics and Medicine`, `Institute of Mathematical Sciences`
- Why now:
  这篇比一般 active matter 论文更适合你，因为它讲的是 `boundary-driven transport`、`steady-state structure`、`universality`，主题上仍在 nonequilibrium statistical physics 主线上。
- Why team:
  虽然不是最顶级大团队，但机构和作者背景是专业的 theoretical/statistical physics 线，不是泛工程或泛 AI 文章。
- Why venue:
  `SciPost Physics` 是靠谱的 physics flagship open-access venue，审稿标准比一般开放获取期刊严得多。
- Read as:
  `边界驱动 active system 里哪些分布和输运结构不能再被被动扩散图像替代`
- URL:
  https://scipost.org/SciPostPhys.19.4.088

### 3. Efficient quantum thermal simulation

- Venue: `Nature`
- Venue reputation: `top_tier`
- Authors: `Chi-Fang Chen, Michael Kastoryano, Fernando G. S. L. Brandão, András Gilyén`
- Institutions: `Caltech IQIM`, `AWS Center for Quantum Computing`, `University of Copenhagen`, `Rényi Institute`
- Why now:
  这篇不是你主线里最贴的那种随机热力学文章，但它是极好的“高质量样本”：把 `thermalization`、`detailed balance`、`locality` 和 algorithmic construction 真正放到一起。
- Why team:
  这几个作者和机构在 quantum information / quantum algorithms 这条线上都很硬，团队可信度很高。
- Why venue:
  `Nature` 本身不用多说；更关键的是这不是靠品牌撑着的泛应用文，而是明确在解一个长期的 thermal simulation 问题。
- Read as:
  `量子热化与经典 MCMC 结构之间，到底能建立怎样的严格对应`
- URL:
  https://www.nature.com/articles/s41586-025-09583-x

## Next Batch: Fast Review

### 4. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

- Venue: `arXiv`
- Venue reputation: `preprint`
- Authors: `Liyao Lyu, Xinyue Yu, Hayden Schaeffer`
- Institutions: `Michigan State University`, `UCLA`
- Why review, not must read:
  这篇的 topic 很贴你后面可能会走的 `trajectory -> drift inference -> interacting particle systems` 线，而且 `Hayden Schaeffer` 这条 scientific ML / applied math 线是专业的；但它目前还是 preprint，应该先做快速筛读，不要直接给和 `PRResearch` / `SciPost` 同等级的信任。
- Read as:
  `能不能把单粒子轨迹学习，推进到 measure-dependent drift / McKean-Vlasov dynamics`
- URL:
  https://arxiv.org/abs/2604.00333

## Reproduction Candidates Only

### Score-fPINN: Fractional Score-Based Physics-Informed Neural Networks for High-Dimensional Fokker-Planck-Lévy Equations

- Venue: `Communications in Computational Physics`
- Venue reputation: `mid_tier_specialized`
- Institutions: `Pacific Northwest National Laboratory`, `National University of Singapore`, `Worcester Polytechnic Institute`, `John Brown University`
- Why not in next reading batch:
  主题看起来很贴 `score + Fokker-Planck`，但这篇更适合当方法复现实验的灵感，不适合当你下一批重点阅读文献。原因是：venue 虽然正规，但不是这个问题上的强信号期刊；文章题目也更偏 numerical method / PINN 组合，而不是你当前最需要的理论桥接。
- Use as:
  `如果你要做一个 1D/2D Fokker-Planck + score residual 的 toy，拿它当复现参考`
- URL:
  https://openalex.org/W4399795376

## Hold

- `A framework for the use of generative modelling in non-equilibrium statistical mechanics`
  Why hold:
  题目很吸引人，作者名字也强，但目前更像概念性、框架性 preprint，容易把你带到过宽的讨论里。适合等你再补一两篇更硬的 nonequilibrium / generative bridge 文章后回来看。

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
2. `Boundary layers, transport and universal distribution in boundary driven active systems`
3. `Efficient quantum thermal simulation`

如果还有余力，再加：

4. `MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data`

## One-Line Summary

下一批最值得读的，不是 `CiCP + score/PINN` 那篇，而是：

`PRResearch 的 non-Markov nonequilibrium model -> SciPost 的 active transport / steady-state structure -> Nature 的 thermal simulation 高质量样本 -> arXiv 的 measure-valued scientific ML bridge`
