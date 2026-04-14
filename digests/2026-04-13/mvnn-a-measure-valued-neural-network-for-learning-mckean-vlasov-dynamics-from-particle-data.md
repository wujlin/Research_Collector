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

第二步，他们把学习目标说清楚：从粒子轨迹观测中，直接学习 `measure-dependent interaction (drift) terms`。这句话很重要，因为它明确说明：要恢复的对象是依赖整体分布的 drift，而不是一个固定的 pairwise kernel 或一个静态势函数。

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

如果把这个 abstract 压成一句最核心的话，它其实是在说：

`作者提出了一个能直接处理概率分布输入的神经网络，用它从粒子轨迹中学习 McKean-Vlasov 型分布依赖动力学；同时他们证明这个架构在 mean-field 理论上是良定义、可逼近、可与 interacting-particle system 对接的。`

## 4. Immediate Questions To Carry Forward

接下来读正文时，最值得追的不是泛泛的“神经网络很强”，而是下面几个具体问题：

1. MVNN 具体怎样把一个 measure 编码成向量表示？
2. `cylindrical features` 在这里到底是什么角色，是理论便利还是实际可计算模块？
3. 他们学的是一般 `b(x,\mu)`，还是某种更特殊的 interacting-kernel 结构？
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

第一步，作者先声明：这里考虑一个标准的 interacting particle / agent system 作为 `motivating example`。这句话很重要，因为它在提醒你：他们不是说全文只处理这一种 pairwise 模型，而是先用一个你熟悉的脚手架，把后面真正要学习的对象钉出来。

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
