# Max Simchowitz: The Pitfalls of Imitation Learning when Actions are Continuous

- Video: [RL Theory Seminar 2025: Max Simchowitz (April 29)](https://www.youtube.com/watch?v=WmAjzJQD6U4)
- Channel: RL theory seminars
- Duration: 59:16
- Transcript: `youtube/transcripts/WmAjzJQD6U4-max-simchowitz-pitfalls-imitation-learning-continuous-actions/`
- Slides: `youtube/slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/`

这场理论 seminar 的主线是：behavior cloning 看起来像普通 supervised learning，但一旦动作空间是连续的，它的部署误差会被控制系统动力学放大。Simchowitz 不是泛泛说“distribution shift 很危险”，而是把危险定位到 continuous actions、closed-loop stability、coverage 和 policy class 的结构关系上。

## 1. 00:01-07:30：imitation learning 为什么不像普通监督学习

![Behavior cloning](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-06-00_behavior_cloning_algorithm.jpg)

开头用 LLM pretraining 做对比：next-token prediction 是在固定数据分布上的监督学习。Behavior cloning 也看起来类似：收集 expert trajectory，把状态映射到 expert action，再训练 policy 模仿。

问题出现在 deployment。训练时，模型看到的是 expert 访问过的状态；测试时，模型沿着自己输出的动作走。只要某一步动作有小误差，下一步状态就会偏离 expert distribution。偏离后，policy 看到的状态不再是训练中充分覆盖的状态，误差可能继续放大。

![Compounding error](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-07-30_compounding_error_problem.jpg)

这就是经典 compounding error。但 Simchowitz 的重点是：连续动作空间里的 compounding 不只是 horizon 上多乘几次错误概率，而是 metric error 通过 dynamics 进入状态，再改变后续动作输入。

## 2. 10:30-18:00：连续动作的坏处不是离散动作 curse of horizon 的简单版本

![Nice imitation problem](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-13-30_nice_imitation_problem.jpg)

在离散动作里，分析常常从 zero-one loss 开始：某一步选错动作，未来就可能进入错误分支。连续动作里，动作没有“完全对/完全错”的边界。一个动作可以只偏一点点，但这一点点会改变物理状态，状态变化又会改变下一步 policy 输入。

Simchowitz 构造所谓 nice imitation problem，就是为了避免把负结果归咎于病态问题。他关心的是：即使 expert、dynamics、loss 看起来都很良性，proper imitation learner 是否仍然可能失败。

![Informal statement](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-16-30_informal_statement.jpg)

seminar 的 informal statement 可以理解成一个警告：在连续控制中，expert-distribution 上的小 imitation error 不足以保证 deployment cost 小。错误可能随 horizon 和系统不稳定性被大幅放大。这个结论针对的是问题结构，不是某个优化器实现。

## 3. 18:00-22:30：核心障碍是 closed-loop stability

![Instability](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-18-00_instability_control_systems.jpg)

这一段把问题从机器学习语言翻译成控制语言。一个连续控制系统是否能容忍小误差，取决于闭环系统是否稳定。局部 smooth 不等于稳定；动作误差小也不等于状态偏差会小。

如果 expert policy 和 dynamics 组成的 closed loop 有稳定性，小扰动可能被反馈吸收。反过来，如果系统在某些方向上不稳定，小动作误差会被 dynamics 放大，之后 policy 再根据偏离状态继续输出动作，错误就会进入反馈回路。

![Closed-loop stability](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-22-30_closed_loop_stable.jpg)

这也是为什么 behavior cloning 的训练 loss 不能单独判断真实控制性能。训练 loss 只看 expert states 上动作像不像，deployment cost 看的是 policy-dynamics 闭环长期走到哪里。

## 4. 27:00-36:00：线性和非线性构造展示负结果机制

![Linear systems](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-27-00_linear_dynamical_systems.jpg)

中段进入技术构造。线性系统提供一个可分析的 sandbox：状态如何受动作影响，误差如何通过系统矩阵传播，都可以直接看清。Simchowitz 通过 challenging pair 说明，两个在 expert trajectory 附近难以区分的问题，可能需要非常不同的部署行为。

![Nonlinear construction](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-33-00_nonlinear_construction.jpg)

非线性构造进一步说明，光有 smoothness 或局部拟合不够。关键是 learner 是否知道偏离 expert path 之后应该怎样恢复。如果训练数据只覆盖轨迹本身，而不覆盖轨迹周围的几何邻域，policy 就缺少恢复信息。

## 5. 45:00-54:00：coverage 和 improper policy 是出路之一

![Coverage notions](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-45-00_notions_of_coverage.jpg)

后半段开始讨论怎么绕开负结果。第一条路是更合适的 coverage notion。连续空间中，coverage 不能只看 expert trajectory 上有没有数据，还要看 trajectory 周围是否有足够厚的 tube。learner 一旦偏离，必须仍然能看到可恢复的监督信号。

第二条路是 improper policies。也就是说，learner 不一定要限制在 expert policy class 内部。如果允许更强的 policy 表示或额外结构，有时可以用不同方式实现稳定恢复。

![Generative models](../../slides/WmAjzJQD6U4-max-simchowitz-the-pitfalls-of-imitation-learning-when-actions-are-continuous/curated/00-54-00_benefits_generative_models.jpg)

最后一张关于 generative models 的 slide 把这场理论 talk 接到机器人学习前沿。生成式 policy 不只是为了表示多模态动作，还可能提供更强的 action-space search、sampling 和 implicit computation。这一点在 RI Seminar 中会被进一步展开。

## 6. 和当前研究线的连接

这场 seminar 是理解 VLA、ACT、diffusion policy 和 generative control 的理论底座。它留下三条硬约束：

- imitation learning 不是普通 supervised learning，因为 policy 会改变自己未来看到的数据分布。
- 连续动作误差会通过 dynamics 放大，稳定性是核心，不是附属条件。
- 数据覆盖必须覆盖 expert trajectory 附近的可恢复邻域，只覆盖演示路径本身不够。

如果和 LeCun world model 放在一起看，这场 talk 给了一个反面教训：没有 action-conditioned dynamics 和稳定性分析，单纯把 observation 映射到 action 很容易在闭环部署时失真。
