---
title: "Flow Matching vs Score-Based Generative Modeling"
aliases: ["flow matching 和 score-based 的区别", "score matching vs flow matching", "density gradient vs transport velocity"]
topics: ["diffusion models", "flow matching", "score-based generative modeling", "probability flow ODE", "optimal transport"]
---

# Flow Matching 和 Score-Based 的关系

## 0. 核心问题

flow matching 和 score-based generative modeling 看起来像两套方法。

score-based 说：我要学习 score function，也就是 noisy distribution 的 log-density gradient。

flow matching 说：我要学习 velocity field，也就是 probability mass 在数据空间里怎样移动。

问题是：这两者到底是本质不同的生成模型，还是同一个 probability path 的两种写法？

最短回答是：

**它们不是完全不同的生成范式，而是同一类 continuous generative process 的两种参数化。score-based 用 density-gradient language，flow matching 用 transport-velocity language。**

---

## 1. 共同对象：一条 probability path

两者的共同起点都是一条随时间变化的 probability distribution：

$$
\mathcal{P}_t(\boldsymbol{x}),\qquad t\in[0,\tau].
$$

在 diffusion model 的 forward direction 里，这条 path 通常从 data distribution 出发：

$$
\mathcal{P}_0(\boldsymbol{x})=q(\boldsymbol{x}),
$$

最后走到一个简单 base distribution 或 noise distribution：

$$
\mathcal{P}_\tau(\boldsymbol{x})\approx p_{\mathrm{base}}(\boldsymbol{x}).
$$

生成时则反过来：从 base distribution 出发，沿 reverse dynamics 回到 data distribution。

所以最高层的问题不是“学 score 还是学 flow”，而是：

$$
\text{How should probability mass move from base distribution to data distribution?}
$$

score-based 和 flow matching 的区别，发生在描述这条运动的方式上。

---

## 2. Fokker--Planck 语言：score 和 velocity 如何连接

在连续时间 diffusion 里，forward process 可以写成 Fokker--Planck equation：

$$
\partial_t \mathcal{P}_t(\boldsymbol{x})
=
-
\nabla\cdot
\left(
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x})
\mathcal{P}_t(\boldsymbol{x})
\right).
$$

这里 $\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x})$ 是 probability velocity field。它描述的是 density mass 在位置 $\boldsymbol{x}$ 处以什么速度移动。

对 overdamped Langevin diffusion，velocity field 可以写成：

$$
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x})
=
\boldsymbol{f}_t(\boldsymbol{x})
-
T_t\nabla\log\mathcal{P}_t(\boldsymbol{x}).
$$

这条式子是理解两者关系的核心。

右边有两部分。

第一，$\boldsymbol{f}_t(\boldsymbol{x})$ 是 drift 或 external force。它是 forward process 中人为指定或由 schedule 决定的系统性推动。

第二，$\nabla\log\mathcal{P}_t(\boldsymbol{x})$ 是 score function。它告诉我们当前 noisy distribution 的 density 在哪里上升最快。

因此，如果知道 score，并且知道 $\boldsymbol{f}_t$ 和 $T_t$，就能恢复 velocity field：

$$
\text{score}
\quad+\quad
\text{known drift/noise}
\quad\Rightarrow\quad
\text{probability velocity}.
$$

反过来，如果直接知道 velocity field，就不一定需要显式学习 score。

---

## 3. Score-based 在学什么

score-based generative modeling 学的是：

$$
\nabla\log\mathcal{P}_t(\boldsymbol{x}).
$$

训练时通常用 denoising score matching。给定 data sample $\boldsymbol{y}$ 和时间 $t$，先通过 forward noising 得到 noisy sample $\boldsymbol{x}$，然后让 neural network 预测 noisy distribution 的 score：

$$
\boldsymbol{s}_t^\theta(\boldsymbol{x})
\approx
\nabla\log\mathcal{P}_t(\boldsymbol{x}).
$$

训练目标可以抽象写成：

$$
L_{\mathrm{SM}}(\theta)
=
\mathbb{E}
\left[
\left\|
\boldsymbol{s}_t^\theta(\boldsymbol{x})
-
\nabla\log\mathcal{P}_t(\boldsymbol{x})
\right\|^2
\right].
$$

学到 score 后，模型可以构造 reverse SDE。直观上，reverse SDE 使用 score 把样本从低结构噪声推回高结构数据区域。

也可以构造 probability flow ODE：

$$
\frac{d\boldsymbol{x}_t}{dt}
=
\boldsymbol{\nu}_t(\boldsymbol{x}_t).
$$

这时 score-based diffusion 不再表现为随机采样，而是表现为一个 deterministic flow。也正是在这个 ODE 视角下，它和 flow matching 变得非常接近。

---

## 4. Flow matching 在学什么

flow matching 学的是 velocity field 本身：

$$
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x}).
$$

它不先问当前 distribution 的 score 是什么，而是直接问：

$$
\text{At time }t,\text{ if a sample is at }\boldsymbol{x},
\text{ what velocity should it have?}
$$

训练目标可以抽象写成：

$$
L_{\mathrm{FM}}(\theta)
=
\mathbb{E}
\left[
\left\|
\boldsymbol{u}_t^\theta(\boldsymbol{x})
-
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x})
\right\|^2
\right].
$$

学到 $\boldsymbol{u}_t^\theta$ 后，生成就是从 base distribution 采样一个初始点，然后积分 ODE：

$$
\frac{d\boldsymbol{x}_t}{dt}
=
\boldsymbol{u}_t^\theta(\boldsymbol{x}_t).
$$

所以 flow matching 的基本语言是 transport：把一团 probability mass 从 base distribution 搬到 data distribution。

---

## 5. 两者为什么看起来不同

score-based 的直觉更像 density correction。

在某个 noisy level $t$，如果 $\boldsymbol{x}$ 处在当前 distribution 的低密度区域，score 会指向 density 上升最快的方向。生成时，score 帮助样本往更像 data 的区域移动。

可以把它记成：

$$
\text{Where is density higher?}
$$

flow matching 的直觉更像 mass transport。

它不先描述 density landscape，而是直接描述每个位置的样本应该怎么流动，才能让整体 distribution 从起点变成终点。

可以把它记成：

$$
\text{How should probability mass move?}
$$

所以两者的表面差异来自提问方式：

$$
\text{score-based}
\rightarrow
\text{learn density gradient},
$$

$$
\text{flow matching}
\rightarrow
\text{learn transport velocity}.
$$

---

## 6. 它们在哪里等价或接近

如果一个 score-based model 使用 probability flow ODE，那么它最终也在使用一个 velocity field：

$$
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x})
=
\boldsymbol{f}_t(\boldsymbol{x})
-
T_t\nabla\log\mathcal{P}_t(\boldsymbol{x}).
$$

这说明 score-based 并没有离开 velocity field。它只是先学习 score，再通过已知 drift 和 noise intensity 把 score 转成 velocity。

flow matching 则跳过这个中间变量，直接学习：

$$
\boldsymbol{u}_t^\theta(\boldsymbol{x})
\approx
\boldsymbol{\nu}^{\mathcal{P}}_t(\boldsymbol{x}).
$$

因此，在 probability flow ODE 视角下，两者可以放进同一个框架：

$$
\text{choose a probability path}
\rightarrow
\text{learn the reverse or generative velocity}
\rightarrow
\text{integrate dynamics to generate samples}.
$$

这就是为什么 stochastic thermodynamics 或 optimal transport 文章可以同时讨论 score-based diffusion 和 flow matching。真正被约束的是 probability path 的 velocity、speed cost 和 entropy production，而不是方法名字。

---

## 7. 它们哪里仍然不同

虽然两者可以统一，但差异仍然重要。

第一，score-based 更依赖 diffusion/noising 结构。它通常从一个明确的 forward diffusion process 出发，学习不同 noise level 下的 score。

第二，flow matching 对 path 的选择更开放。它可以选择 linear interpolation、conditional optimal transport path、stochastic interpolant 或其他 handcrafted path，不一定必须是传统加噪过程。

第三，score 是 gradient field：

$$
\nabla\log\mathcal{P}_t(\boldsymbol{x}).
$$

它天然来自某个 density 的 log-gradient。

第四，velocity field 可以更一般：

$$
\boldsymbol{\nu}_t(\boldsymbol{x}).
$$

它可以包含 transport structure，也可以在更一般设定下包含 non-conservative components。也就是说，velocity language 比 score language 更直接适合讨论 circulation、transport cost、Wasserstein geodesic 和 entropy production。

第五，score-based 可以自然支持 reverse SDE。flow matching 的标准形式更自然地对应 ODE flow。虽然两者都可以扩展，但默认生成机制的直觉不同。

---

## 8. 和 speed-accuracy 文章的关系

在 speed-accuracy relation 那篇文章里，作者把 diffusion model 写成 Fokker--Planck dynamics：

$$
\partial_t \mathcal{P}_t
=
-
\nabla\cdot
\left(
\boldsymbol{\nu}^{\mathcal{P}}_t
\mathcal{P}_t
\right).
$$

这一步直接把 score-based 和 flow matching 统一起来。

score-based 的任务是先估计 score，然后得到 $\boldsymbol{\nu}^{\mathcal{P}}_t$。

flow matching 的任务是直接估计 $\boldsymbol{\nu}^{\mathcal{P}}_t$。

主不等式关心的是：

$$
\int_0^\tau dt\,T_t\dot{S}_t^{\mathrm{tot}}
$$

或者在 conservative case 中关心：

$$
\int_0^\tau dt\,[v_2(t)]^2.
$$

这些量都由 forward probability path 和 velocity field 决定，而不是由 “score-based” 或 “flow matching” 这个名字决定。

所以这篇文章给我们的判断是：

**真正重要的是 path design，而不是只问模型属于 score-based 还是 flow matching。**

---

## 9. 最终结论

flow matching 和 score-based generative modeling 的关系可以压缩成一句话：

**score-based 学 density gradient，再通过 drift/noise 还原 velocity；flow matching 直接学 velocity。**

更线性的版本是：

$$
\text{score-based}
\rightarrow
\nabla\log\mathcal{P}_t
\rightarrow
\boldsymbol{\nu}_t
\rightarrow
\text{reverse SDE / probability flow ODE}.
$$

$$
\text{flow matching}
\rightarrow
\boldsymbol{\nu}_t
\rightarrow
\text{ODE transport}.
$$

所以它们在最高层共享同一个目标：学习一条从 base distribution 到 data distribution 的 continuous probability path。

区别在于：

$$
\text{score-based is density-gradient-centered},
\qquad
\text{flow matching is transport-velocity-centered}.
$$

---

## 10. 常见混淆

**混淆一：flow matching 完全不是 diffusion model。**

不准确。flow matching 不一定使用传统 Gaussian noising diffusion，但它仍然可以放进 continuous generative dynamics 的大框架里。它和 diffusion model 的差别更多在 path construction 和 training target，而不是生成问题的最高层结构。

**混淆二：score-based 一定是随机的，flow matching 一定是确定性的。**

不完全准确。score-based 可以用 reverse SDE，也可以用 probability flow ODE。后者是 deterministic flow。flow matching 标准形式通常是 ODE，但也可以和 stochastic interpolant 或 diffusion bridge 结合。

**混淆三：score 和 velocity 是同一个东西。**

不对。score 是 $\nabla\log\mathcal{P}_t$；velocity 是 $\boldsymbol{\nu}^{\mathcal{P}}_t$。在 Langevin/Fokker--Planck 设定下，它们通过

$$
\boldsymbol{\nu}^{\mathcal{P}}_t
=
\boldsymbol{f}_t
-
T_t\nabla\log\mathcal{P}_t
$$

联系起来，但不是同一个对象。

**混淆四：flow matching 一定比 score-based 更高级。**

不应该这样判断。flow matching 的 transport language 更直接、更适合 OT 和 path design；score-based 的 density-gradient language 更自然连接 SDE、denoising、Langevin dynamics 和 likelihood-related analysis。哪种更好取决于 data、path、training difficulty 和 sampling goal。

**混淆五：只要选择 OT path 就一定最好。**

不一定。OT path 可以降低 path speed cost，但实际模型还要学习 velocity field。如果 OT-like path 让训练目标更难，velocity estimation residual 变大，总误差可能不一定下降。好的 protocol 需要同时考虑 path cost 和 learnability。
