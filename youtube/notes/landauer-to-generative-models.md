# From Landauer Bound to Generative Models

- Source lecture: `Takahiro Sagawa | An introduction to stochastic thermodynamics`
- Video: https://www.youtube.com/watch?v=m023IrSLF-k
- Role: 从信息热力学到生成模型的线性翻译笔记

## Why This Note Exists

这页笔记的目的不是重复 Sagawa 视频内容，而是把其中最重要的一条桥明确写出来：

`Landauer bound -> finite-time dissipation -> probability distribution evolution -> Fokker-Planck -> optimal transport -> generative modeling`

这条线不是松散类比，而是同一类分布动力学结构在热力学和机器学习中的两种出现方式。

## Linear Story

### Step 0. 起点：Landauer bound

擦除 `1 bit` 信息，在准静态极限下至少需要满足：

```text
<W> >= Delta F
```

对对称 `1 bit` 擦除，这个自由能差就是：

```text
Delta F = k_B T ln 2
```

所以 Landauer bound 更准确地是在说：

```text
<W>_qs = k_B T ln 2
```

这里的关键前提是：过程足够慢，即 `tau -> infinity`。

### Step 1. 真实问题：必须在有限时间内完成

真实计算不可能无限慢。一旦要求在有限时间 `tau` 内完成擦除，就会产生额外耗散。

最安全的写法是：

```text
<W> = k_B T ln 2 + W_ex(tau),   W_ex(tau) >= 0
```

其中：

- `k_B T ln 2` 是准静态下界
- `W_ex(tau)` 是有限时间带来的 excess work

要注意一个常见混淆：

```text
W_diss = <W> - Delta F = W_ex(tau)
```

所以如果你写 `W_diss`，就不应再把 `k_B T ln 2` 算进去。

### Step 2. 把信息操作翻译成分布演化

“擦除 `1 bit`”在物理上并不是抽象命令，而是把系统从一个初始分布 `rho_0` 推到一个终态分布 `rho_tau`。

最典型的图像是：

- 初态：两个记忆态上近似均匀分布
- 终态：概率集中到标准零态

于是信息擦除可以被改写成：

```text
information erasure -> controlled evolution of probability distributions
```

这一步是整个桥接的核心，因为从这里开始，问题就进入了随机动力学和分布几何的语言。

### Step 3. 分布演化的动力学语言：Langevin / Fokker-Planck

在连续状态下，系统的随机演化可以由 Langevin 方程描述，而相应的概率密度演化由 Fokker-Planck 方程描述。

这里最值得记住的不是某个具体系数，而是结构：

```text
partial_t rho = - div J
```

也就是说，`Fokker-Planck` 可以被理解为“概率守恒 + 概率流”的动力学方程。

当我们把概率流写成：

```text
J = v rho
```

就得到连续性方程的形式：

```text
partial_t rho + div(v rho) = 0
```

这就是为什么我一直说：

`Fokker-Planck 不是单独一个方向，而是把路径级随机动力学翻译成分布演化的翻译层。`

### Step 4. 有限时间耗散为什么会连到最优传输

一旦问题被写成“在有限时间内把 `rho_0` 变成 `rho_tau`”，就自然会问：

- 怎样搬运最省代价？
- 时间越短，额外代价为什么越大？

这正是 `optimal transport` 的问题。

Benamou-Brenier 给出的动态形式是：

```text
W_2^2(rho_0, rho_tau) = inf_v \int_0^tau \int |v(x,t)|^2 rho(x,t) dx dt
```

约束正是分布搬运的连续性方程：

```text
partial_t rho + div(v rho) = 0
```

因此，有限时间信息擦除的额外代价可以和 Wasserstein 几何联系起来。最稳妥的表达是：

```text
W_ex(tau) proportional to W_2^2(rho_0, rho_tau) / tau
```

物理意义很直接：

- 两个分布差得越远，搬运代价越高
- 时间越短，额外耗散越大
- 最优协议就是分布空间里的最优搬运方案

这里还要再严谨一点：这个“成正比”中的常数依赖具体动力学标度，例如 mobility、friction 或 diffusion coefficient，所以不应轻易写成普适等号。

### Step 5. 为什么这会连到生成模型

一旦你接受“核心对象是分布演化和速度场”，就能看出它和现代生成模型的关系。

在生成模型里，目标也是把一个分布变成另一个分布：

- `score-based diffusion`：数据分布和噪声分布之间的正向/逆向随机演化
- `flow matching / OT flow`：直接学习把一个分布搬到另一个分布的速度场

因此真正的连接点不是“AI 受热力学启发”这种空话，而是：

```text
both sides study transport in distribution space
```

也就是说：

- 热力学这边关心有限时间耗散和最优控制
- 生成模型这边关心如何学习分布间的动力学映射

两边共用的翻译层就是：

`Fokker-Planck + continuity equation + optimal transport geometry`

## What Must Be Said Carefully

你的主线是对的，但有几句话必须说得克制一点。

### 1. 不是所有生成模型都等于“最优传输”

更准确的说法是：

- `flow matching / OT-based flow` 最直接对应“学习最优速度场”
- `score-based diffusion` 和这条线有深联系，但不自动等于热力学最优协议

所以最稳的表达是：

`某些生成模型可以被理解为学习分布传输的速度场，其中 OT flow 最直接，score diffusion 次之。`

### 2. Fokker-Planck 不只是“无扩散极限”

更准确的说法是：

- `Fokker-Planck` 本身就能改写成“密度 + 概率流”的守恒形式
- `Benamou-Brenier` 用到的是这个分布搬运结构

因此连接点不是简单地“把扩散去掉”，而是识别出两边都在处理分布随速度场演化的几何问题。

### 3. Sagawa 的贡献与生成模型论文的贡献不一样

这条线可以这样分工理解：

- `Sagawa` 这边把热力学、信息代价、有限时间耗散这一端讲清楚
- `Song` 等人的工作把生成模型的逆向随机动力学这一端讲清楚
- `Fokker-Planck / optimal transport` 提供了中间翻译语言

所以这不是谁“借用”了谁，而是两个领域在同一数学结构上相遇。

## The Cleanest One-Line Chain

如果以后你要把这条线写进知识地图或笔记里，最推荐压成这一版：

```text
Landauer bound gives the quasi-static free-energy cost of erasing information
-> finite-time computation introduces excess dissipation
-> erasure can be written as controlled evolution rho_0 -> rho_tau
-> this evolution is described by Langevin / Fokker-Planck dynamics
-> Fokker-Planck can be rewritten as continuity equation with probability current
-> Wasserstein / Benamou-Brenier geometry bounds the finite-time excess cost
-> this connects naturally to models that learn transport in distribution space
-> flow matching is the cleanest ML analogue, score diffusion is a related but not identical one
```

## Why This Matters For Your Project

这条线正好解释了你在 `knowledge_map` 里那个最重要的判断：

`Fokker-Planck is the translation layer`

因为它确实把下面这些对象接到了一起：

- 信息擦除和计算能耗
- 随机路径与概率密度演化
- 有限时间热力学
- 最优传输与 Wasserstein 几何
- 生成模型中的分布搬运

如果你后面要继续往前推，最自然的下一步不是重新读一遍整个视频，而是去看：

1. `Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents`
2. `Flow Matching`
3. `Score-Based Generative Modeling through Stochastic Differential Equations`

## Self Check

这页笔记有意识地做了 3 个收缩：

- 保留了你原来那条强线性主线
- 修正了 `W_diss`、`Fokker-Planck` 和 `score diffusion = OT` 这些容易失真的地方
- 把视频中的热力学叙事和你项目里的 `knowledge_map` 语言统一起来
