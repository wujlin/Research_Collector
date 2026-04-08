# Theory Landscape

## Three Different Meanings of Free Energy

- thermodynamic free energy: Helmholtz / Gibbs / partition function
- variational free energy: ELBO / Bayesian inference / amortized inference
- free energy principle: self-organization / generative models / non-equilibrium systems

这三条线在文献中经常被混用，因此 Research Collector 在标签上必须显式区分。

## Why Fokker-Planck Matters

Fokker-Planck 在这个项目里更适合被写成“翻译层”，而不是“四个方向的公共枢纽”。

它做的事情是：

1. 把随机分析中的路径动力学翻译成密度动力学
2. 把统计物理中的耗散、熵产生、稳态问题写成可计算的演化方程
3. 把 AI for Physics 中的 generative dynamics 和 physics-informed modeling 放进同一套动力学语言
4. 把城市系统中的迁移、扩散、空间相互作用写成连续极限模型

所以它的重要性不在于“它同时出现在四个地方”，而在于它承担了**跨层翻译**：

- `路径 -> 密度`
- `动力学 -> 热力学解释`
- `前向扩散 -> 逆向生成`
- `抽象模型 -> 城市场景`

## Current Frontier

最前沿的问题不再是“AI 能不能替代 physics”，而是：

- 生成模型能否学习不可逆轨迹与熵产生
- 变分自由能能否成为 physics-informed generative modelling 的统一训练语言
- score / diffusion / reverse-time dynamics 能否直接解释非平衡系统
