---
title: "Neural ODE and Neural SDE"
aliases: ["Neural ODE", "Neural SDE", "神经常微分方程", "神经随机微分方程"]
topics: ["neural differential equations", "dynamical systems", "time series prediction", "generative modeling", "variational inference", "HJ sampler"]
---

# Neural ODE / Neural SDE 知识卡

## 0. 一句话

Neural ODE / Neural SDE 的核心不是 diffusion model 那种“加噪再去噪”，而是把未知动力方程参数化，然后用有限观测去学习动力学。

主线可以写成：

$$
\text{unknown dynamics}
\rightarrow
\text{parameterized vector field / stochastic dynamics}
\rightarrow
\text{fit from observed trajectories}
\rightarrow
\text{predict, simulate, or generate paths}.
$$

---

## 1. Neural ODE 在做什么

Neural ODE 把深度网络看成连续时间动力系统。普通残差网络可以写成离散更新：

$$
h_{k+1}
=
h_k
+
f_\theta(h_k).
$$

如果把层数变成连续变量，就得到 ODE：

$$
\frac{dh(t)}{dt}
=
f_\theta(h(t),t).
$$

这里 $h(t)$ 是 hidden state 或 latent state，$f_\theta$ 是用 neural network 参数化的 vector field。

训练时，给定初始状态 $h(t_0)$，用 ODE solver 积分到观测时间：

$$
h(t_0)
\xrightarrow{\text{ODE solver}}
h(t_1)
\xrightarrow{\text{ODE solver}}
\cdots
\xrightarrow{\text{ODE solver}}
h(t_N).
$$

然后让预测轨迹和观测轨迹匹配。

所以 Neural ODE 的基本任务是：

$$
\text{learn } f_\theta
\quad
\text{such that solved trajectories match data}.
$$

它适合描述连续时间预测、非均匀采样时间序列、latent dynamics、continuous-depth networks 和 continuous normalizing flows。

---

## 2. Neural SDE 在做什么

Neural SDE 在 Neural ODE 的基础上加入随机扰动：

$$
dh(t)
=
f_\theta(h(t),t)\,dt
+
g_\theta(h(t),t)\,dW_t.
$$

这里有两个可学习对象。

$f_\theta$ 是 drift，表示平均动力方向：

$$
\text{where the state tends to move}.
$$

$g_\theta$ 是 diffusion coefficient，表示随机扰动强度和方向：

$$
\text{how uncertainty enters the dynamics}.
$$

$W_t$ 是 Brownian motion。它不是 diffusion model 里的 artificial noising schedule，而是 stochastic dynamics 里的随机驱动。

因此 Neural SDE 的目标是：

$$
\text{learn stochastic dynamics}
\quad
\text{from observed random trajectories}.
$$

它适合描述观测不完整、系统本身随机、或者存在 unresolved degrees of freedom 的时间序列。

---

## 3. 它有 forward / reverse 吗

有，但语义要和 diffusion model 区分。

Neural ODE 的 forward 是沿时间积分：

$$
h(t_0)
\rightarrow
h(t_1).
$$

如果 ODE flow 可逆，也可以反向积分：

$$
h(t_1)
\rightarrow
h(t_0).
$$

这个 reverse 是动力系统的反向积分，不是 denoising。

Neural SDE 的 forward 是采样随机路径：

$$
h(t_0)
\rightarrow
\{h(t)\}_{t_0\le t\le t_1}.
$$

它也可以讨论 reverse-time SDE、bridge process、filtering、smoothing 或 adjoint gradient，但这不是默认的 diffusion-style reverse denoising。

和 diffusion model 对比：

| 框架 | forward | reverse | 核心轴 |
|---|---|---|---|
| Neural ODE | 沿真实或 latent time 积分 | 反向积分 ODE flow | dynamics time |
| Neural SDE | 沿真实或 latent time 采样随机路径 | reverse-time SDE / bridge / smoothing | dynamics time |
| Diffusion model | 人为把 data 加噪到 prior | 学 reverse denoising | noise scale |
| Predictor-Driven Diffusion | 沿 $t$ 学 predictor，沿 $\lambda$ 做 RG diffusion | reverse-$\lambda$ generation / SR | physical time + spatial scale |

所以：

$$
\text{Neural ODE/SDE 的 forward/reverse 是动力学方向，}
$$

$$
\text{diffusion model 的 forward/reverse 是噪声尺度方向。}
$$

---

## 4. 它是不是生成模型

Neural ODE / SDE 不等于 diffusion-style 生成模型，但它们可以被用作生成模型。

Neural ODE 的生成用法通常是 continuous normalizing flow。设初始变量来自简单分布：

$$
z_0\sim p_0(z).
$$

用 ODE flow 推到数据空间：

$$
z_0
\xrightarrow{\frac{dz}{dt}=f_\theta(z,t)}
z_1.
$$

这是一种 flow-based generation，不是 forward noising / reverse denoising。

Neural SDE 的生成用法可以是 path generation。给定初始分布和 Brownian noise，SDE solver 生成一整条随机路径：

$$
z_0,\ W_t
\rightarrow
\{z(t)\}_{t=0}^T.
$$

比如 Neural SDE-GAN 就把 Brownian motion 作为输入噪声，输出 time-evolving paths，并用 discriminator 匹配真实路径分布。

所以更准确的说法是：

$$
\text{Neural ODE/SDE can be generative, but not necessarily diffusion generative.}
$$

---

## 5. 和 VI primer 的相似处

它们都可以看成有限观测下的逆问题。

VI 的结构是：

$$
\text{posterior } p(z\mid x) \text{ 难算}
\rightarrow
\text{choose } q_\phi(z)
\rightarrow
\min_\phi D_{\mathrm{KL}}(q_\phi(z)\|p(z\mid x)).
$$

Neural ODE/SDE 的结构是：

$$
\text{dynamics unknown}
\rightarrow
\text{choose } f_\theta \text{ or } (f_\theta,g_\theta)
\rightarrow
\text{fit trajectories / likelihood / ELBO / adversarial loss}.
$$

共同点是：

$$
\text{unknown object}
\rightarrow
\text{parameterized surrogate}
\rightarrow
\text{optimize surrogate using observed data}.
$$

差别是未知对象不同。

| 框架 | 未知对象 | 观测 | 优化目标 |
|---|---|---|---|
| VI | posterior $p(z\mid x)$ | data $x$ | ELBO / posterior KL |
| Neural ODE | vector field $f$ | trajectories | prediction loss / likelihood |
| Neural SDE | drift $f$ and diffusion $g$ | stochastic trajectories | likelihood / ELBO / GAN loss |

所以 Neural ODE/SDE 更像：

$$
\text{dynamics-parameterized inference}.
$$

---

## 6. 和 HJ sampler 的相似处

HJ sampler 的目标不是直接学习一个物理动力学，而是为 inverse problem 构造 posterior sampling dynamics。它关心的是：

$$
\text{how to move samples so that they follow posterior geometry}.
$$

Neural ODE/SDE 关心的是：

$$
\text{how to move states so that trajectories match observed dynamics}.
$$

二者的共同结构是：都把一个难以直接求解的问题改写成“学习或构造一个动力过程”。

$$
\begin{aligned}
\text{HJ sampler}
&: \text{posterior sampling as controlled / PDE-guided dynamics},\\
\text{Neural ODE/SDE}
&: \text{system evolution as learned dynamics}.
\end{aligned}
$$

所以它们在形式上相似，但目标不同。

HJ sampler 的动力学服务于 posterior sampling。

Neural ODE/SDE 的动力学服务于 prediction, simulation, path generation 或 density transformation。

---

## 7. 和 Flow Matching 的关系

Flow Matching 和 Neural ODE/SDE 的关系要分层看。

Neural ODE/SDE 是一种动力学参数化方式。它说的是：

$$
\text{use neural networks to parameterize a differential equation}.
$$

Flow Matching 是一种生成模型训练方法。它说的是：

$$
\text{learn a velocity field that transports one distribution to another}.
$$

标准 Flow Matching 通常学习一个 ODE velocity field：

$$
\frac{dx_t}{dt}
=
v_\theta(x_t,t).
$$

生成时从简单 base distribution 采样：

$$
x_0\sim p_0,
$$

再沿 ODE 积分到 data distribution：

$$
x_0
\xrightarrow{\frac{dx_t}{dt}=v_\theta(x_t,t)}
x_1\sim p_{\mathrm{data}}.
$$

所以可以把 Flow Matching 记成：

$$
\text{Flow Matching}
=
\text{a way to train a generative Neural ODE}.
$$

这里的时间 $t\in[0,1]$ 通常不是物理时间，而是 distribution transport time：

$$
\text{base distribution}
\rightarrow
\text{data distribution}.
$$

这和 Neural ODE 用来预测真实系统轨迹时的时间不同。预测问题里的 $t$ 对应真实或 latent dynamics time：

$$
x(t_0)
\rightarrow
x(t_1)
\rightarrow
x(t_2).
$$

Flow Matching 里的 $t$ 对应生成路径上的 interpolation / transport progress：

$$
p_0
\rightarrow
p_t
\rightarrow
p_1.
$$

因此二者的核心差别不是方程形式，而是方程服务的对象不同。

| 框架 | 方程服务的对象 | 时间变量含义 | 典型目标 |
|---|---|---|---|
| Neural ODE for dynamics | 单个系统状态的时间演化 | physical / latent time | prediction, simulation |
| Flow Matching | 整个概率分布的运输 | generative transport time | sample generation |

Flow Matching 有没有噪声，也要分两层。

第一，Flow Matching 通常从 noise distribution 或 simple base distribution 出发：

$$
x_0\sim\mathcal{N}(0,I).
$$

这里的 noise 是初始随机性。它提供生成样本的多样性。

第二，标准 Flow Matching 的采样过程通常是 deterministic ODE：

$$
dx_t
=
v_\theta(x_t,t)\,dt.
$$

它不需要在生成过程中持续注入 Brownian noise：

$$
dx_t
\ne
f_\theta(x_t,t)\,dt
+
g(t)\,dW_t.
$$

所以标准 Flow Matching 和 score-based diffusion 的区别是：

$$
\text{Flow Matching}
:
\text{initial noise + deterministic transport}.
$$

$$
\text{Score-based diffusion}
:
\text{forward noising SDE + reverse denoising SDE/ODE}.
$$

有些 Flow Matching 变体会在训练路径里使用 noisy interpolation，例如：

$$
x_t
=
(1-t)x_0
+
t x_1
+
\sigma_t\epsilon.
$$

但这不等于 diffusion model 的核心机制。它只是构造训练样本或平滑 probability path 的方式；模型主要学的仍然是 velocity field：

$$
v_\theta(x_t,t)
\approx
\text{target velocity}.
$$

所以最稳的记法是：

$$
\text{Flow Matching is usually ODE-based generation trained by velocity regression}.
$$

$$
\text{It uses noise as a starting distribution, not necessarily as a step-by-step noising process}.
$$

---

## 8. 和 Predictor-Driven Diffusion 的关系

Predictor-Driven Diffusion 里的 predictor：

$$
\partial_t u_\lambda
=
f_\lambda^\theta(u_\lambda)
+
\sigma_\lambda\xi
$$

本质上就是一个 $\lambda$-conditioned neural dynamics model。

如果固定 $\lambda$，它很像 Neural ODE/SDE：

$$
\text{fixed } \lambda
\quad\Rightarrow\quad
\text{learn physical-time dynamics}.
$$

但 Predictor-Driven Diffusion 多了一层 $\lambda$ 轴：

$$
\lambda
=
\text{spatial coarse-graining scale}.
$$

于是它不只是学一个固定分辨率下的 temporal predictor，而是学一族 predictors：

$$
\{f_\lambda^\theta\}_{\lambda\in[0,1]}.
$$

更重要的是，作者把 predictor 转成 path density：

$$
f_\lambda^\theta
\rightarrow
p_\lambda(\{u_\lambda\}_t)
\rightarrow
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t).
$$

这个 score 再用于 reverse-$\lambda$ generation / super-resolution。

所以这篇文章和 Neural ODE/SDE 的区别是：

$$
\text{Neural ODE/SDE}
=
\text{learn dynamics in time}.
$$

$$
\text{Predictor-Driven Diffusion}
=
\text{learn dynamics in time, then use it to define scale-wise generation}.
$$

---

## 9. 记忆版

Neural ODE/SDE 可以记成：

$$
\text{learn the equation of motion}.
$$

Diffusion model 可以记成：

$$
\text{learn how to reverse a noising process}.
$$

Flow Matching 可以记成：

$$
\text{learn a velocity field that transports noise distribution to data distribution}.
$$

Predictor-Driven Diffusion 把两者接起来：

$$
\text{learn physical-time dynamics}
\rightarrow
\text{define path density}
\rightarrow
\text{reverse spatial-scale diffusion}.
$$

如果只问 Neural ODE/SDE 本身，它更接近预测和动力学参数反演；如果把它接到 flow、GAN、VAE 或 path-density score 上，它也可以成为生成模型的一部分。

---

## 10. Sources

- Chen et al. (2018), [Neural Ordinary Differential Equations](https://papers.nips.cc/paper/7892-neural-ordinary-differential-equations).
- Kidger et al. (2021), [Neural SDEs as Infinite-Dimensional GANs](https://proceedings.mlr.press/v139/kidger21b.html).
- Kidger et al. (2021), [Efficient and Accurate Gradients for Neural SDEs](https://proceedings.neurips.cc/paper_files/paper/2021/hash/9ba196c7a6e89eafd0954de80fc1b224-Abstract.html).
- Liu et al. (2019), [Neural SDE: Stabilizing Neural ODE Networks with Stochastic Noise](https://arxiv.org/abs/1906.02355).
- Lipman et al. (2023), [Flow Matching for Generative Modeling](https://openreview.net/forum?id=PqvMRDCJT9t).
