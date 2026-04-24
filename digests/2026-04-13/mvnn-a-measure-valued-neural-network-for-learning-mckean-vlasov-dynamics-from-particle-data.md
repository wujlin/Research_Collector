---
title: "MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data"
paper_title: "MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data"
digest_type: "paper_note"
date: "2026-04-13"
---

# MVNN: A Measure-Valued Neural Network For Learning McKean-Vlasov Dynamics From Particle Data

## Core Answer

这篇文章的核心回答是：如果系统的单粒子动力学不仅依赖粒子自身状态，还依赖整个粒子群当前的分布，那么可以直接从粒子轨迹数据中学习这种 `measure-dependent drift`。作者提出的 `measure-valued neural network (MVNN)`，本质上是一种把“概率分布”当作网络输入对象的架构；它不仅能在数值上恢复多类 interacting-particle dynamics，还给出 well-posedness、propagation of chaos、universal approximation 和定量逼近率等理论保证。

## 0. Reading Frame

为了避免后面一上来就把 `McKean-Vlasov`、`measure-valued`、`propagation of chaos` 混在一起，先把这篇文章的阅读框架固定下来：

1. 它要解决的问题是：如何从粒子轨迹数据里学习“依赖整体分布的相互作用动力学”。
2. 它研究的对象不是普通 ODE/SDE 向量场，而是 `measure-dependent drift`，也就是把当前粒子分布也当成状态的一部分。
3. 它的方法推进不只是换一个神经网络，而是让网络能够直接处理 probability measure。
4. 它的理论推进不只是经验拟合，而是把 learned dynamics 和 mean-field / interacting-particle 理论连起来。
5. 这篇文章真正值得追的，不是单个实验结果，而是三件事：
   - 网络如何表示 measure input；
   - 理论上它为何是良定义、可逼近、可推广的；
   - 它和经典 McKean-Vlasov / mean-field dynamics 的关系到底有多紧。
6. 你最后要带走的是：这篇文章是在回答 `how to learn dynamics on the space of measures`，而不是普通的轨迹回归问题。

## 1. What McKean-Vlasov Dynamics Actually Is

先把名字拆开。

`McKean-Vlasov dynamics` 的基本特征是：单个粒子的演化，不只由它自己的位置和速度决定，还由整个粒子群当前的分布决定。换句话说，系统的 drift 不是单纯的

$$
b(x),
$$

而是更像

$$
b(x,\mu_t),
$$

其中

$$
\mu_t
$$

是时间 $t$ 的粒子分布。

这意味着：

1. 单粒子和群体不是分开的两层问题；
2. “整体分布”本身进入了动力学方程；
3. 你要学的不是某个固定 force field，而是一个 `state + distribution -> drift` 的映射。

这也是为什么普通向量输入神经网络在这里不够自然。因为网络真正需要处理的对象，不再只是一个点 $x$，而是一个 measure。

## 2. What The Abstract Is Doing

这个 abstract 的逻辑很紧，不是在堆方法名，而是在沿着一条“问题 -> 架构 -> 理论 -> 实验”的线往前推。

第一步，作者先给出问题背景。许多生物系统中的集体行为都来自个体之间的相互作用。这里的关键不是“单个个体怎么动”，而是“相互作用怎样在群体层面产生有效动力学”。所以他们真正想学的是 interacting forces，而不是普通的单粒子轨迹规律。

第二步，他们把学习目标说清楚：从粒子轨迹观测中，直接学习 `measure-dependent interaction (drift) terms`。这里明确说明：要恢复的对象是依赖整体分布的 drift，而不是一个固定的 pairwise kernel 或一个静态势函数。

第三步，作者提出方法：`measure-valued neural network`。这一步的真正含义不是“再发明一个网络名字”，而是把神经网络的输入对象从欧氏向量推广到 probability measure。作者说他们通过学习 `cylindrical features`，再用一个 embedding network 把 distribution 编码成可扩展的 vector representation。换句话说，MVNN 的核心是：先把 measure 变成网络可处理的表示，再用这个表示去输出分布依赖的 drift。

第四步，作者说明这不是纯经验拟合方法，而是有完整理论支撑。摘要里列了四层理论结果：

1. `well-posedness`：
   学出来的动力学本身是良定义的。
2. `propagation of chaos`：
   与之对应的 interacting-particle system 在大粒子数极限下和 mean-field 描述是一致的。
3. `universal approximation`：
   这个架构理论上能逼近目标 measure-dependent dynamics。
4. `quantitative approximation rates`：
   在一个低维 measure-dependence 假设下，逼近误差还能被定量控制。

所以摘要中段的真正意思是：MVNN 不是只“能用”，而是它和 McKean-Vlasov 理论之间的关系被数学上打通了。

第五步，作者再用数值实验说明方法不是只在 toy setting 里有效。他们覆盖了：

- first-order 和 second-order systems；
- deterministic 和 stochastic systems；
- 多种经典 interacting-particle models：
  - Motsch-Tadmor dynamics；
  - attraction-repulsion aggregation；
  - Cucker-Smale dynamics；
  - hierarchical multi-group system。

这一层的作用是说明：他们不是只学某个单一基准模型，而是在一组典型集体动力学上验证这个方法的广泛适用性。

第六步，摘要最后落在两个应用层结论上：

- `accurate prediction`
- `strong out-of-distribution generalization`

这说明作者想强调的，不只是网络能插值拟合训练轨迹，而是它学到了具有外推能力的动力学结构。

## 3. How To Read The Abstract In One Line

一句话总结这个 abstract：

`作者提出了一个能直接处理概率分布输入的神经网络，用它从粒子轨迹中学习 McKean-Vlasov 型分布依赖动力学；同时他们证明这个架构在 mean-field 理论上是良定义、可逼近、可与 interacting-particle system 对接的。`

## 4. Immediate Questions To Carry Forward

接下来读正文时，最值得追的不是泛泛的“神经网络很强”，而是下面几个具体问题：

1. MVNN 具体怎样把一个 measure 编码成向量表示？
2. `cylindrical features` 在这里到底是什么角色，是理论便利还是实际可计算模块？
3. 他们学的是一般 $b(x,\mu)$，还是某种更特殊的 interacting-kernel 结构？
4. `propagation of chaos` 在这里是作为先验假设使用，还是作为 learned system 的理论输出？
5. 所谓 `low-dimensional measure-dependence assumption` 到底限制了什么？
6. 文中声称的 `out-of-distribution generalization`，是对粒子数、初值分布，还是对动力学家族本身的泛化？

## 5. Why This Paper Belongs To The Current Reading Line

这篇文章和你刚读的几篇虽然不在同一个子主题上，但它和当前主线是连得上的。

前面几篇更强调：

- 从轨迹中学局域对象；
- 从 coarse-grained 统计中恢复不可逆性；
- 把随机动力学作为生成过程来理解。

这篇文章推进的是另一条但相关的线：

`如果动力学本身定义在“粒子状态 + 群体分布”上，那么神经网络怎样把 distribution 直接当作状态变量来学习？`

所以它和 generative model 不直接同类，但和下面这些问题高度相关：

1. `from particle data to dynamics`
2. `distribution as state`
3. `mean-field limit and learned dynamics`
4. `AI methods for stochastic interacting systems`

也就是说，这篇文章更像是你当前主线中的“方法侧分支”，不是熵产生那条线的直接延伸，但对 `AI for physics` 里如何学习 distribution-dependent dynamics 非常关键。

## 6. How To Read The Introduction Linearly

这篇 `Introduction` 的逻辑其实很完整，不是在泛泛铺背景，而是在一步一步把问题从“粒子轨迹学习”推进到“measure-valued learning”。

第一步，作者先给出总问题。很多物理、生物、社会系统都可以看成 interacting particle / agent systems，而真正困难的地方不是写出单个粒子的运动，而是：`如何从观测到的轨迹里，反推出群体相互作用机制。` 所以这篇文章的起点不是单纯建模，而是一个反演问题：`trajectory data -> governing interaction law`。

第二步，作者先回顾已有方法的典型路线。现有很多数据驱动方法会假设一个 `binary-interaction ansatz`，也就是总作用力由很多两两相互作用叠加而成，然后再用轨迹差分得到的速度去拟合 pairwise kernel。也就是说，这些方法主要在学

$$
K(x_i,x_j)
\quad\text{或}\quad
\phi(|x_i-x_j|).
$$

这一步的作用是立一个明确 benchmark：作者不是在真空里提出新问题，而是在回应一条已经存在的“pairwise-kernel learning”路线。

第三步，作者指出这条路线为什么不够。很多真实系统的 effective dynamics 更像是 `mean-field form`

$$
b(x,\mu),
$$

而不是二体力的简单求和。作者给的例子包括：crowd dynamics 由局部密度约束决定，traffic 的速度依赖流量密度，cell migration 会受到化学场影响。这些例子共同说明：单个体常常不是逐个响应其他个体，而是在响应由群体分布形成的有效环境。

第四步，作者补上第二个动机：计算复杂度。就算 pairwise 假设是合理的，直接模拟也常常要

$$
O(N^2),
$$

因为每个粒子都要和其他粒子逐个作用。mean-field limits 和 random batch methods 之所以重要，就是因为它们给 large-population system 提供了更可扩展的近似。所以 intro 到这里同时立起了两层动机：

1. 物理上，pairwise 假设可能不够真；
2. 计算上，pairwise 模拟可能不够省。

第五步，作者把问题接到 machine learning，但立刻指出：现有 operator learning 也不能直接解决这里的问题。原因不是这些方法不强，而是它们通常处理的是 `function-valued inputs on structured domains`，而这篇面对的输入是离散经验 measure，也就是一个无序点云。换句话说，问题不只是“学动力学”，还包括“如何表示一个 measure 输入”。

第六步，作者正式写出问题对象：McKean-Vlasov dynamics。这里他们把单粒子 mean-field SDE 写成

$$
dX_t=b(X_t,f_t)\,dt+\sigma(X_t,f_t)\,dB_t,
$$

其中

$$
f_t=\mathcal{L}(X_t).
$$

同时又写出对应的 $N$-粒子近似：

$$
dX_t^{i,N}=b(X_t^{i,N},\mu_t^N)\,dt+\sigma(X_t^{i,N},\mu_t^N)\,dB_t^{i,N},
$$

其中

$$
\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^{j,N}}.
$$

这一步很关键，因为它明确说明：这篇真正要学习的对象不是 pairwise kernel，也不是 score，而是定义在

$$
\mathbb{R}^d\times \mathcal{P}(\mathbb{R}^d)
$$

上的 drift

$$
b(x,\mu).
$$

第七步，作者因此提出 MVNN。它的真正角色不是“另一个网络”，而是：给 probability measure 一个 permutation-invariant、可扩展的向量表示，让 measure 真正能作为网络输入对象。这里 cylindrical functional framework 只是理论启发，真正的工程实现是：

1. embedding network 从 measure 中提取特征；
2. interaction network 把这些特征和单粒子状态组合起来，输出 drift。

第八步，作者最后把全文收束成三层贡献：

1. 架构层：提出 MVNN，直接学 measure-dependent drift；
2. 理论层：证明 well-posedness、propagation of chaos、universal approximation 和 approximation rates；
3. 实验层：在多类 deterministic / stochastic、first-order / second-order interacting systems 上验证预测和泛化能力。

所以整段引言的真正主线是：

`pairwise methods are too narrow -> mean-field drift is the right object -> measure input needs a new representation -> MVNN is proposed to learn it with theory and experiments aligned.`

## 7. What Structured Domain Actually Means

`structured domain` 容易抽象，是因为这个词默认你已经习惯了函数学习和 operator learning 的输入形式。这里可以把它拆得很具体。

第一步，所谓 `function-valued input`，指的是输入本身是一个函数，比如：

- 一维区间上的函数 $u(x)$；
- 二维平面上的场 $u(x,y)$；
- 时间-空间网格上的信号 $u(t,x)$；
- PDE 里的系数场、初值场、解场。

第二步，所谓 `structured domain`，指的是这些函数定义在一个自带几何结构的域上。这个结构可能是：

- 一维顺序：点按从左到右排列；
- 二维网格：像图像像素那样有行列关系；
- 三维网格：每个点有固定邻接；
- 有明确坐标系和规则采样方式的网格化区域。

所以“structured”不是抽象说法，它具体意味着：

1. 输入点之间有固定坐标关系；
2. 相邻点是谁是已知的；
3. 输入通常可以排成规则数组；
4. 网络可以直接利用这种结构去卷积、插值、谱展开或做局部算子。

第三步，这也是为什么很多 operator-learning 方法天然适合 PDE。因为 PDE 的输入经常就是：

- 一张规则网格上的初值；
- 一张规则网格上的系数场；
- 一个有固定空间坐标的函数。

这时输入长得像：

$$
u(x)\quad\text{或}\quad u(x,y),
$$

而不是一堆无序样本点。

第四步，MVNN 面对的输入不是这种对象。它的输入是经验 measure

$$
\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^{j,N}},
$$

更具体地看，就是一堆粒子位置：

$$
X_t^{1,N},\dots,X_t^{N,N}.
$$

这些点的特点是：

1. 没有天然顺序；
2. 没有规则网格；
3. 粒子重排不应改变输入含义；
4. 粒子数还可能变化。

所以它更像一个 `unordered point cloud`，而不是定义在结构化域上的函数。

第五步，这就是为什么作者说现有方法“不天然适合 Wasserstein setting”。因为这类方法通常默认输入是：

- 有网格的；
- 有顺序的；
- 可以直接写成固定尺寸张量的；

而经验 measure 则是：

- 无序的；
- 粒子数可变的；
- 真正的对象是分布，而不是点的排列方式。

第六步，把两类输入并排看就很清楚了：

- structured-domain function input：
  “在规则网格上的一个函数”
- measure input：
  “由无序粒子样本定义的一个经验分布”

所以这里的困难不是普通意义上的高维，而是：`输入对象的几何类型变了。`

第七步，把这个差异再压得更具体一点。假设你想学习一个 PDE 初值到解的映射，那么输入通常像一张已经排好格子的图：

- 第 1 个点在左上角；
- 第 2 个点在它右边；
- 相邻关系和局部坐标一开始就给定了；
- 把这些点重新打乱顺序，输入就被破坏了。

而在这篇文章里，如果当前粒子位置是

$$
\{x_1,x_2,\dots,x_N\},
$$

那么真正有意义的是经验分布

$$
\mu^N=\frac1N\sum_{j=1}^N\delta_{x_j},
$$

而不是“第 1 个粒子排在前面、第 2 个粒子排在后面”这种顺序信息。也就是说：

- 把粒子重排，物理输入不该改变；
- 粒子数改变，输入维度也会跟着变；
- 网络要抓住的是“分布长什么样”，不是“点按什么顺序列出来”。

所以 `structured domain` 和 `measure input` 的真正区别，不在于一个连续、一个离散，而在于：

1. 前者自带固定几何组织；
2. 后者只有统计分布有意义，排列本身没有意义。

第八步，一句话压缩就是：

`structured domain` 指的是像区间、网格、图像坐标系那样自带顺序和邻接关系的定义域；而这篇文章的输入不是这种规则函数，而是一个由无序粒子点云组成的经验 measure，所以需要专门的 permutation-invariant、measure-valued 表示方法。

## 8. What The Opening Of Section 2 Is Actually Doing

`2 Learning McKean-Vlasov Drifts from Particle Data` 这一节开头容易读乱，是因为作者在同一段里连续做了三件事：

1. 先拿一个熟悉的 pairwise particle system 当例子；
2. 再把它改写成 mean-field / measure-dependent 形式；
3. 最后把问题转成“从轨迹数据学习 drift”。

所以更清楚的读法，不是把它看成正式结果，而是把它看成从物理模型走向学习任务的过渡段。

第一步，作者先声明：这里考虑一个标准的 interacting particle / agent system 作为 `motivating example`。这里的作用是提醒读者：他们不是说全文只处理这一种 pairwise 模型，而是先用一个你熟悉的脚手架，把后面真正要学习的对象钉出来。

第二步，这个脚手架是一个标准 pairwise system：

$$
dX_t^i=\frac1N\sum_{j=1}^N \phi(\|X_t^j-X_t^i\|)(X_t^j-X_t^i)\,dt+\sigma\,dB_t^i.
$$

这条式子里的逻辑是：

1. $X_t^i$ 是第 $i$ 个粒子的状态；
2. $\phi(\|X_t^j-X_t^i\|)(X_t^j-X_t^i)$ 是第 $j$ 个粒子对第 $i$ 个粒子的 pairwise 作用；
3. 对所有 $j$ 求和以后，得到第 $i$ 个粒子的总作用。

所以在这一步，作者还停留在最熟悉的“二体相互作用叠加”图像里。

第三步，作者接着定义经验分布

$$
\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^j}.
$$

这一步的作用是把“很多粒子的位置”重新组织成一个更高层的对象：当前群体的整体分布。从这里开始，作者的视角就不再只是盯着

$$
X_t^1,\dots,X_t^N,
$$

而是开始盯着

$$
\mu_t^N.
$$

第四步，作者说明：在 mean-field limit 里，这类 pairwise interaction 可以被压成一个作用在单粒子状态和整体分布上的 drift：

$$
b(x,\mu)=\int \phi(\|y-x\|)(y-x)\,\mu(dy).
$$

这一步是整个过渡段最关键的地方，因为它把“对所有粒子逐个求和”的微观图像，改写成了“给定当前位置 $x$ 和整体分布 $\mu$ 的有效 drift”。

所以作者现在真正关心的对象，已经不是 bare pairwise kernel

$$
\phi,
$$

而是

$$
b(x,\mu).
$$

第五步，这里最好把 pairwise sum 到 mean-field drift 的过渡再写清楚。motivating example 的 drift 部分原本是

$$
\frac1N\sum_{j=1}^N \phi(\|X_t^j-X_t^i\|)(X_t^j-X_t^i).
$$

如果把当前这个粒子的状态记成

$$
x=X_t^i,
$$

那这条式子就变成

$$
\frac1N\sum_{j=1}^N \phi(\|X_t^j-x\|)(X_t^j-x).
$$

现在再引入经验分布

$$
\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^j},
$$

并利用经验 measure 的基本性质：对任意测试函数 $f(y)$，都有

$$
\int f(y)\,\mu_t^N(dy)=\frac1N\sum_{j=1}^N f(X_t^j).
$$

只要取

$$
f_x(y)=\phi(\|y-x\|)(y-x),
$$

就立刻得到

$$
\int \phi(\|y-x\|)(y-x)\,\mu_t^N(dy)
=
\frac1N\sum_{j=1}^N \phi(\|X_t^j-x\|)(X_t^j-x).
$$

这说明：有限粒子系统里的 pairwise sum，本身就已经可以完全等价地写成对经验分布的积分。只有当粒子数 $N$ 很大、经验分布 $\mu_t^N$ 逼近连续分布 $\mu_t$ 时，它才自然过渡成真正的 mean-field drift

$$
b(x,\mu)=\int \phi(\|y-x\|)(y-x)\,\mu(dy).
$$

所以这里的 mean-field drift 不是凭空引入的新力，而是 pairwise interaction 在分布层面的重写。

第六步，这就是为什么这篇文章不能被简单读成“又一个 pairwise kernel learning 方法”。作者用 pairwise system 只是为了说明：即使从微观上出发于二体相互作用，在大群体极限里，真正自然的学习对象也可能是 measure-dependent drift，而不是核函数本身。

第七步，作者随后把问题彻底改写成数据驱动形式。他们说，在实际里更容易拿到的是离散时间上的粒子轨迹观测：

$$
\{X_{t_\ell,m}^i\}_{i,\ell,m},
$$

然后再用有限差分近似速度：

$$
V_{t_\ell,m}^i=\frac{X_{t_{\ell+1},m}^i-X_{t_\ell,m}^i}{t_{\ell+1}-t_\ell}.
$$

所以这里的任务不再是“先知道相互作用公式，再去分析它”，而是：

`给定粒子轨迹数据，直接反推出 measure-dependent drift。`

第八步，这一小节最后真正立起来的任务定义就是：

$$
\text{trajectory data} \longrightarrow b(x,\mu).
$$

所以它的作用不是在推理论结论，而是在完成一个问题重定义：

- 从“有一个 interacting particle model”
- 变成“有一堆 particle observations”
- 再变成“要学习定义在 $(x,\mu)$ 上的 drift”

一句话压缩，这个开头的真正作用是：

`先用一个熟悉的 pairwise particle model 当引子，说明它在 mean-field 极限下可以被写成 measure-dependent drift，然后把全文任务改写成：从粒子轨迹数据中直接学习这个 drift。`

## 9. How To Read Section 2.1 Linearly: Measure-Valued Neural Network

`2.1 Measure-Valued Neural Network` 这一节是在回答全文最核心的技术问题：

既然真正要学的对象是 $b(x,\mu)$，而 $\mu$ 是一个 probability measure，不是普通向量，那神经网络到底该怎样表示它？

第一步，作者先把难点说清楚。前面已经把学习任务改写成

$$
\text{trajectory data} \longrightarrow b(x,\mu).
$$

这里真正困难的不是单粒子状态 $x\in\mathbb{R}^d$，而是 measure 输入

$$
\mu\in\mathcal{P}(\mathbb{R}^d).
$$

普通神经网络天然吃的是有限维向量；而这里的第二个输入是一个分布对象，所以首先必须解决：`如何把 measure 变成网络可处理的表示。`

第二步，作者先用 cylindrical functional 给出理论启发。他们回顾了一类经典表示：

$$
\mu \mapsto f\big(\langle g_1,\mu\rangle,\dots,\langle g_n,\mu\rangle\big),
$$

其中

$$
\langle g_i,\mu\rangle=\int g_i(x)\,\mu(dx).
$$

这表示：不用试图直接处理整个 measure，而是先从分布里抽出有限个积分特征，再在这些特征上做普通有限维映射。它的直觉就是：`先把分布投影成有限个广义统计量，再在这些统计量上建模。`

第三步，作者把这个思路神经网络化。MVNN 的核心不是手工选定 test functions $g_i$，而是让网络自己学习这些 measure features。于是整个 drift 被写成两部分：

- embedding network
  $$
  \varphi_{\mathrm{emb}}:\mathbb{R}^d\to\mathbb{R}^k
  $$
- interaction network
  $$
  \varphi_{\mathrm{int}}:\mathbb{R}^d\times\mathbb{R}^k\to\mathbb{R}^d
  $$

这里最好不要先把整条公式端出来，而是先按运算顺序把它拆开。

1. 先看最里层的
   $$
   \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}).
   $$
   这里最好把两个符号分开看。$\theta_{\mathrm{emb}}$ 是 embedding network 自带的可训练参数，也就是这部分网络的权重和偏置；它不是额外的物理量，而是在说明“这一组 measure features 是从数据里学出来的”。而 $\cdot$ 不是点乘，也不是乘号，它只是一个占位符，表示这里暂时不固定输入点。换句话说，

   $$
   \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}})
   $$

   表示的是“带参数 $\theta_{\mathrm{emb}}$ 的 embedding 函数本身”，而不是它在某个具体点上的取值。

   这一步之所以要写成函数本身，是因为后面要把它拿去对整个 measure 做积分。更具体地说，如果把积分变量写成 $y$，那么它真正展开以后是

   $$
   y \mapsto \varphi_{\mathrm{emb}}(y;\theta_{\mathrm{emb}}),
   $$

   再进一步才会进入

   $$
   \int \varphi_{\mathrm{emb}}(y;\theta_{\mathrm{emb}})\,\mu(dy).
   $$

   所以这里的 $\cdot$ 真正想表达的是：`先把 embedding network 看成一个函数，再让这个函数作用于分布中的所有点。`

2. 然后看中间这层
   $$
   \langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu\rangle.
   $$
   这表示：把 embedding network 当成一个 test-function family，对整个分布 $\mu$ 做积分，从而得到一个有限维全局特征向量。也就是说，这一步是在把 infinite-dimensional measure 输入压缩成一个 $k$ 维表示。

3. 最后才看外层
   $$
   \varphi_{\mathrm{int}}:\mathbb{R}^d\times\mathbb{R}^k\to\mathbb{R}^d
   $$
   这说明 interaction network 接收两类输入：单粒子的局部状态 $x$，以及上一步得到的全局分布特征向量。

4. 把这三层合起来，原文的方程 2 才真正写成
   $$
   b_\theta(x,\mu)
   :=
   \varphi_{\mathrm{int}}\Bigl(x,\langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu\rangle;\theta_{\mathrm{int}}\Bigr).
   $$
   现在整条式子的逻辑就非常清楚了：先把 measure 变成向量，再把这个向量和单粒子状态一起送进 interaction network，最后输出 drift。

所以方程 2 的逻辑不是“measure 直接进网络”，而是：

`先用 embedding network 把 measure 变成向量，再把这个向量和单粒子状态一起送进 interaction network。`

如果用一句更直接的话来说，方程 2 做的是三步：

$$
\mu
\;\longrightarrow\;
\langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu\rangle
\;\longrightarrow\;
\bigl(x,\langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu\rangle\bigr)
\;\longrightarrow\;
b_\theta(x,\mu).
$$
它在概念上是同一个结构，但把参数记号和 $\cdot$ 省掉了。这里按你的要求，已经恢复成和原文方程 2 一致的写法。

第四步，一旦输入是 empirical measure，这个表示就会变得非常具体。如果

$$
\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^{j,N}},
$$

那么

$$
\langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu_t^N\rangle
=
\frac1N\sum_{j=1}^N \varphi_{\mathrm{emb}}(X_t^{j,N};\theta_{\mathrm{emb}}).
$$

所以 MVNN 的计算结构其实很直接：

1. 对每个粒子跑同一个 embedding network；
2. 对所有 embedding 向量做平均；
3. 得到一个全局 population feature；
4. 再把它和当前粒子的状态拼起来，输出 drift。

第五步，这个结构同时解决了两件事。第一是 `permutation invariance`：粒子重排以后，平均值不变，所以网络输出不会依赖粒子编号。第二是计算复杂度：整套 drift evaluation 只需要

$$
O(N)
$$

级别的代价，而不是 pairwise 模型常见的

$$
O(N^2).
$$

所以 MVNN 的贡献不只是“能表示 measure”，还包括：`这种表示既尊重物理上的粒子不可区分性，又在计算上可扩展。`

第六步，作者接着把 learned drift 真正塞回动力学里。他们不是只学一个静态回归器，而是直接定义 learned particle system：

$$
dX_t^{\theta,i,N}
=
b_\theta(X_t^{\theta,i,N},\mu_t^{\theta,N})\,dt+\sigma\,dB_t^{i,N},
$$

以及对应的 mean-field limit：

$$
dX_t^\theta
=
b_\theta(X_t^\theta,f_t^\theta)\,dt+\sigma\,dB_t.
$$

所以这篇方法的目标不是“拟合瞬时速度”，而是学一个能够真正生成：

- 有限粒子系统；
- mean-field SDE；
- 以及对应 Fokker-Planck 动力学

的 drift law。

第七步，这里还要把原文的方程 6 读清楚，因为它说明 learned drift 不只定义了粒子系统，也定义了连续分布层面的演化规律。作者写的是

$$
\frac{d}{dt}\langle f_t^\theta,\psi\rangle
=
\left\langle
f_t^\theta,\,
b_\theta(x,f_t^\theta)\cdot\nabla\psi+\frac12\sigma^2\Delta\psi
\right\rangle.
$$

这条式子是 learned McKean-Vlasov SDE 对应的 Fokker-Planck 方程的弱形式。这里

$$
\langle f_t^\theta,\psi\rangle
=
\int \psi(x)\,f_t^\theta(x)\,dx
$$

表示分布 $f_t^\theta$ 对测试函数 $\psi$ 的平均值，所以左边

$$
\frac{d}{dt}\langle f_t^\theta,\psi\rangle
$$

就是“这个平均值随时间怎样变化”。右边则把变化来源拆成两部分：

1. 
   $$
   b_\theta(x,f_t^\theta)\cdot\nabla\psi
   $$
   是 learned drift 对分布演化的贡献；
2. 
   $$
   \frac12\sigma^2\Delta\psi
   $$
   是布朗噪声带来的扩散贡献。

原文第二行只是把 drift 再展开成 MVNN 的具体形式。更清楚地写，应该是

$$
b_\theta(x,f_t^\theta)
=
\varphi_{\mathrm{int}}
\left(
x,\int \varphi_{\mathrm{emb}}(y)\,f_t^\theta(y)\,dy
\right),
$$

其中积分变量最好写成 $y$，以免和外层的粒子位置 $x$ 混淆。这样方程 6 真正表达的就是：

`MVNN 不只是一个离散粒子回归器；它还诱导出一个连续分布层面的 nonlinear Fokker-Planck dynamics。`

第八步，这也解释了为什么这一节后半段紧接着就是理论保证。作者不希望 MVNN 只是一个经验模型，而是要证明这套 learned dynamics 是数学上站得住的。他们依次给出四层结果：

1. `well-posedness`：
   learned McKean-Vlasov dynamics 是良定义的；
2. `propagation of chaos`：
   learned particle system 在大粒子数极限下收敛到对应的 mean-field model；
3. `universal approximation`：
   这种 cylindrical neural form 理论上可以逼近一般连续的 $b^\star(x,\mu)$；
4. `quantitative approximation rates`：
   在低维 measure-dependence 假设下，还能给出定量逼近误差。

这说明 `2.1` 不只是“怎么搭网络”，而是在完成一个闭环：

`measure representation -> scalable architecture -> learned dynamics -> mean-field compatibility -> approximation theory`

一句话总结这一节：

`作者用 cylindrical functional 的思想，把 measure 先编码成有限维全局特征，再与单粒子局部状态结合，从而构造出一个 permutation-invariant、线性复杂度、能直接定义 learned McKean-Vlasov dynamics 的神经网络架构，并进一步证明它是良定义、可逼近且和 mean-field 极限相容的。`

## 10. How To Read The Theory Guarantees Linearly

这一部分最容易读散，因为作者连续给了好几个 Proposition / Theorem。如果直接按编号读，会变成“结论堆叠”；更清楚的读法是先问：`为了让 MVNN 真正成为一个可信的动力学学习框架，理论上必须依次回答哪几个问题？`

按这个思路，这里的 theory guarantees 其实是在依次回答四个问题：

1. 学出来的动力学本身存不存在，而且是不是唯一的？
2. 如果我用这个 learned drift 去驱动一个有限粒子系统，它会不会真的收敛到对应的 mean-field model？
3. 即使前两点都成立，这个网络类到底够不够大，能不能表示一般的目标 drift？
4. 就算理论上能表示，逼近代价会不会高得不可用？

作者的四层保证，正好对应这四个问题。

第一步，`well-posedness` 先回答的是“这个 learned dynamics 至少是不是一个合法动力学”。作者假设 embedding network 和 interaction network 都是全局 Lipschitz，然后证明 learned McKean-Vlasov SDE

$$
dX_t^\theta=b_\theta(X_t^\theta,f_t^\theta)\,dt+\sigma\,dB_t
$$

这里有三个术语需要拆开看。第一，`全局 Lipschitz` 的意思不是“在某个局部邻域里变化平滑”，而是存在一个统一常数，使得输入变化多少，网络输出最多按同阶线性放大多少，而且这个控制对整个状态空间都成立。对这篇来说，它的作用是保证 learned drift 不会在远离训练区域时突然变得过于陡峭，从而避免动力学在有限时间内失控。第二，`唯一强解` 是粒子路径层面的结论：在同一个概率空间、同一条布朗运动和同一个初值下，这条 SDE 产生的轨道几乎处处唯一，所以随机性只来自噪声本身，而不会额外出现“同样噪声对应多条轨道”的不确定性。第三，`唯一弱解` 在这里说的是分布演化层面：对应的 Fokker-Planck 方程在 law 的意义下只有一个演化结果，也就是只有一个随时间变化的概率分布族与这条 SDE 相匹配。

证明的线性逻辑其实很集中，并没有同时证明很多东西。作者说这个命题是 McKean-Vlasov SDE 一般存在唯一性定理的直接推论，所以他们真正需要核查的只有一步：MVNN 定义出来的 drift 是否对状态变量 $x$ 和 measure 变量 $\mu$ 联合满足全局 Lipschitz 估计。更具体地说，他们要证明

$$
\left| b_\theta(x,\mu)-b_\theta(x',\mu') \right|
\le C\Bigl(|x-x'|+W_2(\mu,\mu')\Bigr).
$$

一旦这条不等式成立，标准的 McKean-Vlasov existence-uniqueness theorem 就可以直接调用，于是强解存在唯一，law 也随之唯一。

这条 Lipschitz 估计的证明分成两步。第一步，先把总差拆成“measure 变了”和“state 变了”两部分：

$$
\left| b_\theta(x,\mu)-b_\theta(x',\mu') \right|
\le
\left| b_\theta(x,\mu)-b_\theta(x,\mu') \right|
+
\left| b_\theta(x,\mu')-b_\theta(x',\mu') \right|.
$$

第二步，分别控制这两项。对第二项，measure 固定，只让 $x$ 变化；这时直接用 interaction network 在第一个输入上的 Lipschitz 性，就得到

$$
\left| b_\theta(x,\mu')-b_\theta(x',\mu') \right|
\le C_i |x-x'|.
$$

对第一项，状态 $x$ 固定，只让 measure 变化。先用 interaction network 在第二个输入上的 Lipschitz 性，把问题降到控制两个 measure embedding 的差：

$$
\left| b_\theta(x,\mu)-b_\theta(x,\mu') \right|
\le
C_i
\left|
\int \varphi_{\mathrm{emb}}(y)\,\mu(dy)
-
\int \varphi_{\mathrm{emb}}(y)\,\mu'(dy)
\right|.
$$

接着作者引入任意一个 coupling $\pi\in\Pi(\mu,\mu')$，把这两个积分写成同一个联合分布下的差，再用 Cauchy-Schwarz 和 embedding network 的 Lipschitz 性，得到

$$
\left|
\int \varphi_{\mathrm{emb}}(y)\,\mu(dy)
-
\int \varphi_{\mathrm{emb}}(y)\,\mu'(dy)
\right|
\le
C_e
\left(
\int |y-y'|^2\,\pi(dy,dy')
\right)^{1/2}.
$$

最后对所有 coupling 取最优，就得到 Wasserstein 距离：

$$
\left| b_\theta(x,\mu)-b_\theta(x,\mu') \right|
\le C_i C_e\, W_2(\mu,\mu').
$$

把这两部分合起来，就得到作者要的联合 Lipschitz 估计。证明在这里实际上已经结束了，因为后面的“唯一强解”和“唯一弱解”不是再重新构造解，而是把这条估计送进现成的 McKean-Vlasov 理论。换句话说，这个命题的真正证明核心不是解 SDE 本身，而是验证：`MVNN 的 drift 虽然依赖 measure，但它的这种依赖仍然足够规整，可以被标准理论接住。`

把这三点合在一起，作者得到的是：这条 learned McKean-Vlasov dynamics 在粒子层面是路径唯一的，在分布层面是 law 唯一的，而且这两层唯一性都由同一个 globally Lipschitz 的 drift 控制。这个结果的作用非常基础：如果这一步都没有，后面讨论 propagation of chaos、逼近能力、训练泛化都没有意义。也就是说，`well-posedness` 是在保证：MVNN 学出来的不是一个可能爆炸、可能不唯一的“伪动力学”，而是一条真正定义良好的 McKean-Vlasov 演化。

第二步，光有 continuum-level 的良定义还不够，因为训练数据本身来自有限粒子系统。所以作者接着证明 `propagation of chaos`。这一步回答的问题是：`你用 learned drift 定义的 N 粒子系统，随着 N 变大，会不会真的逼近刚才那个 mean-field model？` 证明的逻辑和前面的 well-posedness 一样，也是先抓住真正需要控制的量，而不是一开始就谈抽象极限。作者构造了两套由同一组布朗运动驱动的过程：一套是真正相互作用的 learned N 粒子系统

$$
X_t^{\theta,i,N},
$$

另一套是 $N$ 个彼此独立的“理想” mean-field 过程

$$
\bar X_t^{\theta,i,N},
$$

它们满足同样的初值 law 和同样的噪声，但 drift 里不再用经验分布，而是直接用极限分布 $f_t^\theta$。这一步叫 `synchronous coupling`，它的作用是把“有限粒子系统”和“mean-field 极限”放到同一个概率空间里逐路径比较。

有了这个耦合以后，作者定义误差

$$
e_t^i:=X_t^{\theta,i,N}-\bar X_t^{\theta,i,N}.
$$

因为两套系统使用的是同一条布朗运动，做差时随机噪声会直接抵消，所以误差演化只剩下 drift 之间的差。这就是整个证明的关键转折：问题从“比较两套带噪 SDE”变成了“比较两个 drift 有多不一样”。

接下来作者对 $|e_t^i|^2$ 用 Itô 公式，再取时间上确界和期望，得到误差满足一个积分不等式。此时最核心的一步，是把 drift 差拆成两部分：

1. 第一部分是
   $$
   b_\theta(X_t^{\theta,i,N},\mu_t^{\theta,N})
   -
   b_\theta(\bar X_t^{\theta,i,N},\bar\mu_t^{\theta,N}),
   $$
   它表示“如果两套系统都看各自的经验分布，那么单粒子位置差和经验分布差会带来多大 drift 误差”。
2. 第二部分是
   $$
   b_\theta(\bar X_t^{\theta,i,N},\bar\mu_t^{\theta,N})
   -
   b_\theta(\bar X_t^{\theta,i,N},f_t^\theta),
   $$
   它表示“即使粒子位置本身已经换成 ideal mean-field process，仅仅把经验分布 $\bar\mu_t^{\theta,N}$ 换成真实分布 $f_t^\theta$ 时，还剩下多少采样误差”。

这两部分对应的是两种不同来源的误差：前者是路径误差传递，后者是经验分布逼近真实分布时的 Monte Carlo 采样误差。

对第一部分，作者直接调用 Proposition 2.1 已经得到的联合 Lipschitz 估计。状态变量的差给出 $|e_t^i|$，measure 变量的差给出

$$
W_2(\mu_t^{\theta,N},\bar\mu_t^{\theta,N}),
$$

而这个 Wasserstein 距离又可以用同一个耦合下所有粒子误差的平均来控制。因此第一部分最终被压到“当前粒子误差的平均量级”上。

对第二部分，逻辑不同。这里的 $\bar X_t^{\theta,i,N}$ 是独立同分布的 mean-field 样本，所以

$$
\bar\mu_t^{\theta,N}=\frac1N\sum_{j=1}^N \delta_{\bar X_t^{\theta,j,N}}
$$

只是对分布 $f_t^\theta$ 的经验近似。由于 embedding network 是 Lipschitz 的，

$$
\int \varphi_{\mathrm{emb}}\,d\bar\mu_t^{\theta,N}
$$

就是一个样本均值，而样本均值与总体期望之间的均方误差正好是方差除以 $N$。这一步给出真正的有限粒子采样误差阶数：

$$
\mathbb E\bigl[\text{embedding error}^2\bigr] \lesssim \frac{1}{N}.
$$

把这两类误差放回误差积分不等式后，作者得到一个标准的闭合估计：

$$
Y(T)\le C\int_0^T Y(s)\,ds+\frac{C_T}{N},
\qquad
Y(t):=\mathbb E\Big[\sup_{r\le t}|e_r^i|^2\Big].
$$

这时再用 Gr\"onwall 不等式，就得到

$$
\mathbb E\Big[\sup_{t\le T}|X_t^{\theta,i,N}-\bar X_t^{\theta,i,N}|^2\Big]\to 0
\qquad (N\to\infty).
$$

证明到这里，有限粒子系统和 ideal mean-field process 的路径差已经消失。最后一步只是在语言上把它翻译成 `propagation of chaos`：由于所有粒子是 exchangeable 的，对任意固定有限个粒子，它们的联合 law 都收敛到独立同分布的 mean-field law；等价地说，learned N 粒子系统在大粒子数极限下变成 $f_t^\theta$-chaotic。这个结论的意义是把“离散粒子数据”和“连续分布模型”桥接起来。没有这一步，MVNN 就只能算一个连续模型上的抽象构造；有了这一步，它才真的和 particle data 产生理论闭环。

第三步，在确认 learned dynamics 是良定义且和有限粒子系统相容之后，作者才去回答表达能力问题，也就是 `universal approximation`。这一步要解决的不是存在性，而是：MVNN 这类 cylindrical neural form 到底够不够一般，能不能逼近任意连续的目标 drift $b^\star(x,\mu)$？

这一条 theorem 的逻辑最好分三层看。第一层是它到底在说什么对象。作者给定一个目标 drift

$$
b^\star:\mathbb{R}^d\times\mathcal{P}_2(\mathbb{R}^d)\to\mathbb{R}^d,
$$

并引入一个 measure on measure-space，记作 $\zeta$，用来描述“在哪些 $(x,\mu)$ 上衡量逼近误差”。因此这里的误差不是逐点的 sup-norm，而是在

$$
L^2(\zeta)
$$

意义下衡量的，也就是把不同分布 $\mu$ 以及这些分布下的粒子位置 $x$ 一起平均后再看平方误差。这个设定的作用是把 theorem 放在一个自然的 statistical / trajectory-learning 语境里：它不是要求网络在所有可能 measure 上处处一致逼近，而是在给定的数据分布或问题分布下做到任意精度。

作者给出的回答是肯定的：只要目标 drift 在

$$
\mathbb{R}^d\times\mathcal{P}_2(\mathbb{R}^d)
$$

上连续，那么这种形式的 MVNN 就可以在合适意义下把它逼近到任意精度。第二层是它为什么成立。这里作者其实没有重新从零证明，而是把已有的 measure-space neural approximation theorem 直接专门化到 drift 学习问题上。关键观察是：MVNN 的结构

$$
b_\theta(x,\mu)=\varphi_{\mathrm{int}}\Bigl(x,\langle \varphi_{\mathrm{emb}}(\cdot;\theta_{\mathrm{emb}}),\mu\rangle;\theta_{\mathrm{int}}\Bigr)
$$

本身就是 cylindrical functional 的神经网络版本，而已有理论已经说明：这类“先取有限个 measure features，再用有限维网络组合”的函数类，在

$$
\mathbb{R}^d\times\mathcal{P}_2(\mathbb{R}^d)
$$

上对连续目标函数是稠密的。换句话说，这里真正被调用的不是某个具体 drift 的特殊性质，而是 `cylindrical representation + finite-dimensional neural approximation` 这两步的组合稠密性。

第三层是这条定理在全文里的作用。它不是在说“训练一定能找到好参数”，也不是在说“样本复杂度已经解决了”；它只回答一个更基础的问题：`就函数类本身而言，MVNN 有没有表达瓶颈？` 这条 theorem 给出的答案是否定的。只要目标 drift $b^\star(x,\mu)$ 在相应意义下连续，MVNN 理论上就不会因为结构太窄而学不到它。因此，这一步把前面的“我们为什么要这样设计网络”变成了一个严格的表达能力声明：这不是一个很窄的特例架构，而是理论上足够大的函数类。

第四步，到这里你还不能直接放心，因为 universal approximation 只回答“能不能”，没有回答“代价多大”。所以作者最后引入 `quantitative approximation rates`。这里最容易混淆的是：正文其实给了两层 rate 结果，它们在逻辑上做的事情不同。第一层是 Theorem 2.4，它先回答一个更基础但也更悲观的问题：`如果完全不假设目标 drift 有额外结构，只知道它在 Wasserstein 空间上是一般 Lipschitz 函数，那么用有限维 measure embedding 去逼近它，代价会长成什么样？`

这一条 theorem 的证明思路是先把 measure 空间离散化成一个有限维对象。作者在状态空间 $\Omega$ 上做一个尺度为 $\delta$ 的覆盖，用 partition of unity $\{\omega_m\}$ 把每个 measure $\mu$ 映成一个有限维向量

$$
\mathbf u(\mu)=\bigl(\langle \omega_1,\mu\rangle,\dots,\langle \omega_{C_\Omega},\mu\rangle\bigr).
$$

这里的坐标数 $C_\Omega$ 本质上就是覆盖数，而覆盖数满足

$$
C_\Omega \lesssim \delta^{-d}.
$$

这就是高维灾难真正进入证明的位置：要把 measure 看清楚到精度 $\delta$，需要的特征数会像 $\delta^{-d}$ 一样随维度爆炸。这里后面的证明可以按三步理解。第一步，作者不再让目标函数直接吃一个无限维 measure，而是先用 partition-of-unity 特征把它压成有限维向量

$$
\mathbf u(\mu)=\bigl(\langle \omega_1,\mu\rangle,\dots,\langle \omega_{C_\Omega},\mu\rangle\bigr)\in\mathbb{R}^{C_\Omega}.
$$

这样一来，原来的 measure-dependent function 就被改写成一个有限维函数

$$
F(x,\mathbf u),
$$

其中 $x$ 是粒子状态，$\mathbf u$ 是 measure 的离散化表示。第二步，由于原始目标函数对 $(x,\mu)$ 是 Lipschitz 的，而 $\mu\mapsto \mathbf u(\mu)$ 这一步本身也受覆盖尺度 $\delta$ 控制，作者得到这个新函数 $F(x,\mathbf u)$ 仍然是一个有限维 Lipschitz 函数。第三步，问题就彻底回到了经典神经网络逼近理论：既然现在输入只是有限维向量 $(x,\mathbf u)$，就可以直接调用标准深度网络对 Lipschitz 函数的逼近定理来控制误差、深度和宽度。

所以这里真正发生的不是“凭空把 measure 问题解决了”，而是：作者先付出一个代价，把无限维 measure dependence 离散化成高维但有限维的特征向量，再把困难转交给普通有限维逼近理论。Theorem 2.4 的作用不是给出一个“好看的 rate”，而是严肃地说明：`在最坏情况下，MVNN 并不会自动逃过 measure-space approximation 的维度诅咒。`

第五步，因此作者才引入一个关键假设：`low-dimensional measure dependence`。这一步的思想不是再额外加一个技巧，而是在说：很多真实物理、生物、社会系统的有效 mean-field interaction 并不会依赖整个 measure 的全部自由度，而往往只依赖少数几个 order parameters 或 summary statistics，比如局部密度、平均动量、极化方向等。换句话说，真实系统虽然活在无限维 measure 空间里，但真正有用的依赖可能只在一个低维流形上。作者把这件事形式化成：存在有限个 feature functions

$$
g_1,\dots,g_r
$$

使得目标 drift 实际上可以写成

$$
b^\star(x,\mu)=G\bigl(x,\langle g_1,\mu\rangle,\dots,\langle g_r,\mu\rangle\bigr).
$$

这一步把“measure dependence 很复杂”改写成“其实只依赖少数 order parameters”。

第六步，在这个低维结构假设下，Theorem 2.7 才给出真正可用的 approximation rate。这里的证明逻辑比 Theorem 2.4 简洁很多，因为一旦目标 drift 已经能写成上面的形式，问题就不再是直接逼近无限维 measure functional，而是分成两步：

1. 先用 embedding network 去逼近有限个 feature functions $g_1,\dots,g_r$；
2. 再用 interaction network 去逼近有限维函数 $G(x,\cdot)$。

这样一来，逼近代价就不再由原始状态维度 $d$ 的 covering number 主导，而主要由低维特征个数 $r$ 和相应 Lipschitz 常数控制。这里最重要的不是记住每个复杂的阶数，而是记住逻辑：`一旦 measure dependence 实际上由少数低维特征控制，MVNN 的学习代价就从“无限维最坏情况”回落到“低维有效结构”所支配的规模。`

第七步，所以这四层保证不是平行摆放的，而是一个严格递进链：

- `well-posedness` 保证 learned dynamics 本身是合法的；
- `propagation of chaos` 保证有限粒子系统和 mean-field model 是相容的；
- `universal approximation` 保证 MVNN 这个函数类足够一般；
- `quantitative rates under low-dimensional dependence` 保证这种一般性在有物理结构时不会完全失去计算可行性。

一句话总结这部分：

`作者不是只证明“这个网络能拟合数据”，而是沿着“动力学存在 -> 微观到宏观相容 -> 表达能力 -> 逼近效率”这条线，把 MVNN 从一个经验模型推进成了一个有 mean-field 理论支撑的动力学学习框架。`

读这一节时，还要补一个最基础但很有用的背景：为什么 ODE/SDE 理论总是在乎连续、Lipschitz、全局 Lipschitz 这些正则性条件。这里的 `ODE` 是 ordinary differential equation，描述没有显式随机噪声的连续时间动力学；`SDE` 是 stochastic differential equation，在漂移项之外还带布朗运动这类随机驱动。两者共同的问题都是：给定初值以后，轨道到底存不存在、会不会唯一、以及初值或参数的小误差会不会被无限放大。

最弱的要求是连续。连续只说明输入变一点，输出也会跟着变一点，但它不控制“最多能变多快”，所以通常不足以保证唯一性。再强一点是 Hölder 连续，它给出幂次型控制，但对 ODE/SDE 的存在唯一性来说仍然往往不够。真正最常用的是 Lipschitz 条件：

$$
|f(x)-f(y)|\le L|x-y|.
$$

它的意思是：函数的变化速度在全空间里都有统一上界，小扰动最多按 $L$ 倍放大。对 ODE 来说，这正是 Picard-Lindelöf 定理里保证解唯一的核心条件；对 SDE / McKean-Vlasov SDE 来说，它又进一步保证同一噪声下的路径不会分叉，从而得到强解唯一性。

这里还要区分 `局部 Lipschitz` 和 `全局 Lipschitz`。局部 Lipschitz 只保证在每个有界区域里函数不会太陡，但系统一旦跑远，这个控制可以失效；全局 Lipschitz 则要求同一个常数在整个空间都有效。前者常常足够做局部分析，后者更适合拿来保证全时间存在唯一性和稳定性。MVNN 这篇强调全局 Lipschitz，就是为了确保 learned drift 即使在训练分布之外也不会突然失控。

最后再补一个经常和 Lipschitz 同时出现的条件：`linear growth`。它要求

$$
|b(x)|\le C(1+|x|),
$$

意思是函数本身可以变大，但不能比线性更快地爆炸。Lipschitz 控制的是“两个点之间的差会不会被放大”，linear growth 控制的是“函数值本身会不会长得太快”。对动力学来说，这两者配合起来，才能同时保证解存在、解唯一、以及二阶矩不会在有限时间内失控。也正因为如此，前面几条 theorem 里反复出现的正则性假设，不是装饰性的技术条件，而是整条 mean-field 理论链能成立的最低支撑。

## 11. What Section 2.3 Numerical Results Establishes

`2.3` 的任务不是重复前面的理论结论，而是检验 learned drift 在具体动力学里能否兑现成可滚动的预测。整段实验按验证对象逐步展开。第一，`1D deterministic Motsch-Tadmor dynamics` 检验 `MVNN` 能否学习带归一化分母的 measure-dependent drift；这里的难点在于漂移依赖经验分布诱导的归一化项，而不是简单的 pairwise kernel 累加。第二，`1D stochastic Motsch-Tadmor dynamics` 在保留同一漂移结构的同时加入噪声，检验模型在随机扰动下还能不能稳定恢复有效 drift。第三，`2D aggregation dynamics with attraction-repulsion` 不再只看一维密度峰值，而是看网络能否保持 ring、disk、double-ring 和 asymmetric binary distribution 这类几何结构，并在未见过的初始化上做出 OOD 泛化。按这个顺序读，数值部分不是若干例子的堆叠，而是在逐步扩大验证范围：从非 pairwise 漂移，到含噪动力学，再到二维几何和拓扑结构。

## 12. 1D Motsch-Tadmor Dynamics: Learning A Normalized Measure-Dependent Drift

作者先用 `1D Motsch-Tadmor dynamics` 检验 `MVNN` 能否学习带归一化分母的 measure-dependent drift。这个模型的 drift 不是简单的二体作用求和，而是带有归一化分母的非线性对齐机制：

$$
\dot X_t^i
=
\frac{\sum_{j=1}^N \phi(|X_t^j-X_t^i|)(X_t^j-X_t^i)}
{\sum_{k=1}^N \phi(|X_t^k-X_t^i|)},
\qquad i=1,\dots,N.
$$

这条式子和普通 alignment model 的关键区别在于分母。没有分母时，每个粒子只是在累加邻居对它的 pairwise influence；有了分母以后，粒子 $i$ 的 drift 不只取决于邻居贡献的线性累加，还取决于以当前位置为中心的加权经验质量

$$
\sum_{k=1}^N \phi(|X_t^k-X_t^i|).
$$

因此，这里的 drift 不是简单的 pairwise force 求和，而是依赖经验分布诱导的归一化项的 mean-field drift。这一节要回答的问题也因此很明确：`MVNN 能不能从粒子轨迹里恢复这种 normalization effect 所对应的有效 drift。`

数据生成的设置也围绕这个目标展开。作者固定粒子数 $N=16000$、时间区间 $T=2$、步长 $\Delta t=10^{-2}$，并取 Gaussian interaction kernel

$$
\phi(r)=\exp\bigl(-(r/\ell)^2\bigr),\qquad \ell=0.5.
$$

然后用 forward Euler 生成 $M=100$ 条独立轨迹。更关键的是初始条件并不是固定一种，而是每条轨迹都从一个随机生成的多峰 Gaussian mixture 开始：分量数在 2 到 8 之间，均值分布在 $[0,3]$，方差固定为 $0.25$，权重来自对称 Dirichlet 分布。这个设计的作用非常明确：训练集不是让模型记住某一种群体形状，而是强迫它学习“对不同初始分布都成立的宏观演化规律”。

接下来最需要读清楚的是，这一节评估的对象不是 microscopic interaction kernel recovery，而是宏观 mean-field dynamics 的恢复。作者并不要求网络显式重建原来的归一化公式，而是训练一个 learned drift

$$
\hat b_\theta(x,\hat\mu_t^N),
$$

再用它驱动 learned dynamics

$$
\dot X_t^{i,N}=\hat b_\theta(X_t^{i,N},\hat\mu_t^N),
\qquad
\hat\mu_t^N=\frac1N\sum_{j=1}^N\delta_{X_t^{j,N}}.
$$

因此，这里的问题不是“能不能把底层核函数 $\phi$ 拟合出来”，而是“用 learned mean-field drift 跑出来的群体密度演化，是否和真实粒子系统一致”。这个区分很重要，因为它正好对应全文的立场：作者要学的是有效的 measure-dependent drift，而不是显式的 microscopic formula。

Figure 1 是这一小节最直接的证据。由于 PDF 抽取把这一张图拆成了三张图片，下文按 `row 1 -> row 2 -> row 3` 的顺序把它重新读回完整的 Figure 1。三行对应三个未见过的初始分布；每一行从左到右依次给出 $t=0,1,2$ 的密度曲线，以及随时间累积的 $L^2$ 误差。蓝线是 learned MVNN dynamics，橙线是 reference simulation。因此读图的顺序应该固定成两步：先看每一行里密度如何从 $t=0$ 演化到 $t=2$，再看最右侧误差曲线是在缓慢积累，还是在某个阶段突然放大。

**Figure 1, row 1**

![Figure 1 row 1](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-08-figure-01.jpg)

第一行展示的是一个双峰初值逐步向更尖锐双峰结构收缩的过程。到 $t=1$ 时，左侧主峰已经明显增高，右侧次峰仍然保留；到 $t=2$ 时，两处峰的位置和高度仍与 reference 基本重合。这里最重要的信息不是“有没有完全收敛成单峰”，而是 MVNN 是否保住了正确的峰位置、相对强度和 sharpening 过程。最右侧误差曲线虽然单调上升，但到终点仍只在大约 $0.06$ 左右，说明长时间 rollout 会累积误差，但没有破坏主要的聚团结构。

**Figure 1, row 2**

![Figure 1 row 2](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-08-figure-02.jpg)

第二行是三组里最难的一组。初始分布更接近“单个主峰加右侧弱尾部”，随后主峰快速变尖，尾部逐渐收缩成一个较小的次峰。MVNN 在 $t=1$ 时仍与 reference 几乎重合；到 $t=2$ 时，主峰的位置和高度依然很准，主要偏差出现在右侧小次峰的幅值和形状上。对应地，这一行的 $L^2$ 误差在后段上升更快，终点接近 $0.1$。这说明模型的主要误差来自晚时间对细小次结构的近似，而不是主导 cluster 的整体运动被学错了。

**Figure 1, row 3**

![Figure 1 row 3](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-08-figure-03.jpg)

第三行说明 MVNN 处理的不是只有“单峰向单峰收缩”这一类简单情形。这个初值在 $t=0$ 已经带有不对称的双峰或肩部结构，随后质量重新分配，到 $t=2$ 形成一个更尖锐的主峰和一个较小的副峰。MVNN 基本重现了两处峰的位置、相对高度和压缩过程，终点误差同样保持在大约 $0.06$。这里真正说明问题的是：网络学到的不只是某个固定峰形，而是峰的 transport、压缩和相对质量分配。

把三行合起来，Figure 1 实际上回答了三个更具体的问题。第一，MVNN 在 unseen initial conditions 上能不能保持正确的 mass transport 方向？答案是能。第二，它能不能保持 cluster 的数量、位置和主次关系？答案也基本是能。第三，误差主要来自哪里？不是早期演化方向错误，而是长时间推演中对尖峰和小次峰细节的误差逐步积累。换句话说，这张图支持的结论不是“MVNN 精确重建了微观公式”，而是“MVNN 已经学到足以恢复宏观密度演化的有效 mean-field drift”。

Figure 1 证明的是：只看 reference simulation 和 learned MVNN dynamics 的对比，MVNN 已经能把这个归一化 mean-field drift 对应的密度演化学出来。接下来的 Figure 2 到 Figure 4 不是换了另一个任务，而是在同一个 `1D Motsch-Tadmor` benchmark 上继续追问两件事：如果把 Gaussian process baseline 放进来，谁更接近真实动力学；如果粒子数继续增大，谁更适合大规模 mean-field 仿真。

读 Figure 2 之前要先说明比较边界。GP 由于 kernel matrix 的规模代价，只能在更小训练集上训练，所以这里的时间范围缩短到了 $[0,1]$，图上只画 $t=0,0.5,1.0$。而且和 Figure 1 一样，Figure 2 在 PDF 抽取后也被拆成了三张图片；正确顺序同样是 `row 1 -> row 2 -> row 3`。每一行仍然对应一个 unseen initial condition，只是这次三条曲线分别是：蓝线 GP，橙线 MVNN，绿线 reference simulation。

**Figure 2, row 1**

![Figure 2 row 1](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-09-figure-01.jpg)

第一行最清楚地展示了两种模型的分歧是怎样随着时间放大的。到 $t=0.5$ 时，GP 已经把左侧峰推得过高、过尖，同时把右侧峰压得过低；到 $t=1.0$ 时，这种偏差继续放大，GP 基本把质量错误地集中到了左侧窄峰上，而 MVNN 仍然和 reference 保持接近，能够同时保住左侧主峰和右侧次峰的相对位置与高度。

**Figure 2, row 2**

![Figure 2 row 2](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-09-figure-02.jpg)

第二行对应的是 Figure 1 里误差增长最快的那组测试初值。这里 GP 的问题更明显：到 $t=0.5$ 时，它已经把主峰压缩得过尖；到 $t=1.0$ 时，蓝线出现了远高于 reference 的尖峰，说明它把归一化作用下的聚团过程学成了过度集中的塌缩。相比之下，MVNN 虽然也会有小偏差，但主峰位置、峰宽和右侧弱尾部都仍与 reference 更接近。

**Figure 2, row 3**

![Figure 2 row 3](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-09-figure-03.jpg)

第三行重复了同样的模式。初始时三条曲线重合；到 $t=0.5$ 时，GP 已经出现向左侧尖峰过度集中的趋势；到 $t=1.0$ 时，GP 的主峰明显偏高且偏窄，而 MVNN 依旧更贴近 reference 的双峰结构。把 Figure 2 三行合起来看，GP 的误差不是随机噪声，而是有方向性的系统偏差：它倾向于把密度推向过尖、过窄的峰，从而破坏正确的 cluster balance；MVNN 则更能保持 reference simulation 中的峰结构和质量分配。

Figure 3 把 Figure 2 里的视觉印象压缩成定量误差比较。左、中、右三个面板仍然对应同样的三个 unseen initial conditions；蓝线是 GP，橙线是和 GP 使用同一小数据设定训练的 MVNN，绿线是使用 $16000$ 个粒子、$100$ 条轨迹和 $200$ 个时间步训练的 MVNN。

![Figure 3](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-10-figure-01.jpg)

这张图要按“谁的误差增长最快，谁的误差最低”来读。三个测试例子里，蓝线始终增长最快，说明 GP 的 rollout 误差在整个区间里都最大。橙线明显低于蓝线，说明即使在和 GP 相同的小数据设定下，MVNN 已经能给出更低的密度误差。绿线几乎贴着横轴，说明当训练规模扩大之后，MVNN 的误差还能进一步压低。于是 Figure 3 给出的结论是分两层的：第一，同样的小数据条件下，MVNN 已经优于 GP；第二，MVNN 能继续利用更大的粒子数和更长的轨迹，把这种优势进一步放大。

Figure 4 最后单独回答扩展性问题。横轴是粒子数 $N$；蓝线对应 MVNN 的仿真时间，读左轴；红线对应 GP 的仿真时间，读右轴。

![Figure 4](../../pdfs/2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.mineru/hybrid_auto/images/page-10-figure-02.jpg)

这张图的读法非常直接。随着 $N$ 增大，MVNN 的仿真时间基本保持平稳，而 GP 的时间代价快速上升，到较大粒子数时已经远高于 MVNN。也就是说，Figure 4 讨论的不是谁更准，而是谁能把 learned dynamics 真正用于大粒子数的 mean-field 系统。把 Figure 1 到 Figure 4 连起来，`1D Motsch-Tadmor dynamics` 这一节形成了一条完整的线性证据链：Figure 1 先证明 MVNN 能恢复 reference density evolution，Figure 2 再说明它比 GP 更接近真实轨迹，Figure 3 把这种差异定量化，Figure 4 最后说明这种优势还能在大规模粒子系统里保持可用。
