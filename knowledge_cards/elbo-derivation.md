---
title: "ELBO Derivation"
aliases: ["ELBO 推导", "evidence lower bound", "variational inference"]
topics: ["variational inference", "ELBO", "Bayesian inference", "free energy"]
---

# ELBO 推导

## 0. 核心问题

给定观测变量 $x$ 和潜变量 $z$，模型写成联合分布

$$
p(x,z)=p(x\mid z)p(z).
$$

真正想要的是后验

$$
p(z\mid x)=\frac{p(x,z)}{p(x)},
$$

其中

$$
p(x)=\int p(x,z)\,dz
$$

是边际似然，也叫 evidence。

困难不在于后验定义本身，而在于 $p(x)$ 往往难以显式计算。

---

## 1. 变分推断到底在做什么

变分推断的目标不是直接算出真实后验 $p(z\mid x)$，而是引入一个可控的近似分布 $q(z)$，让它逼近真实后验。

最自然的目标是最小化

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

这一步的含义很直接：

- $p(z\mid x)$ 是想要的真实后验；
- $q(z)$ 是我们能优化、能计算的近似后验；
- 变分推断想做的，就是让两者尽量接近。

问题在于，右边仍然含有难算的 $p(z\mid x)$。  
ELBO 的作用，就是把这个目标改写成一个可优化的形式。

---

## 2. ELBO 的第一种推导：从 KL 恒等式出发

从 KL 散度定义开始：

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big)
=
\mathbb E_{q(z)}\!\left[\log q(z)-\log p(z\mid x)\right].
$$

由贝叶斯公式，

$$
\log p(z\mid x)=\log p(x,z)-\log p(x).
$$

代入上式：

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big)
=
\mathbb E_q\!\left[\log q(z)-\log p(x,z)+\log p(x)\right].
$$

因为 $\log p(x)$ 与 $z$ 无关，可以移到期望外面：

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big)
=
\log p(x)+\mathbb E_q\!\left[\log q(z)-\log p(x,z)\right].
$$

移项得到

$$
\log p(x)
=
\underbrace{\mathbb E_q\!\left[\log p(x,z)-\log q(z)\right]}_{\mathrm{ELBO}(q)}
+
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

这就是最核心的恒等式。

因为 KL 散度总是非负的，

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big)\ge 0,
$$

所以立刻得到

$$
\mathrm{ELBO}(q)\le \log p(x).
$$

这就是 `evidence lower bound` 这个名字的来源：  
它是对 $\log p(x)$ 的一个下界。

---

## 3. ELBO 的第二种推导：从 Jensen 不等式出发

从 evidence 本身开始：

$$
\log p(x)=\log \int p(x,z)\,dz.
$$

对任意分布 $q(z)$，乘上再除以 $q(z)$：

$$
\log p(x)=\log \int q(z)\frac{p(x,z)}{q(z)}\,dz.
$$

写成期望：

$$
\log p(x)=\log \mathbb E_q\!\left[\frac{p(x,z)}{q(z)}\right].
$$

由于 $\log$ 是凹函数，Jensen 不等式给出

$$
\log \mathbb E_q\!\left[\frac{p(x,z)}{q(z)}\right]
\ge
\mathbb E_q\!\left[\log \frac{p(x,z)}{q(z)}\right].
$$

于是

$$
\log p(x)\ge \mathbb E_q\!\left[\log p(x,z)-\log q(z)\right].
$$

右边就是 ELBO。

这条推导更强调 “ELBO 是下界”；  
上一条推导更强调 “ELBO 与后验 KL 之间的精确恒等式”。

---

## 4. 为什么最大化 ELBO 等价于最小化后验 KL

回到核心恒等式：

$$
\log p(x)
=
\mathrm{ELBO}(q)
+
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

对固定观测 $x$ 而言，$\log p(x)$ 是常数。  
因此：

$$
\max_q \mathrm{ELBO}(q)
\quad\Longleftrightarrow\quad
\min_q D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

所以 ELBO 优化真正减少的东西是：

$$
q(z)\ \text{与}\ p(z\mid x)\ \text{之间的 KL gap}.
$$

也就是说：

- ELBO 越大；
- 近似后验 $q(z)$ 越接近真实后验 $p(z\mid x)$；
- 同时 ELBO 与真实 log evidence $\log p(x)$ 之间的缺口也越小。

---

## 5. ELBO 的常见两项分解

因为

$$
p(x,z)=p(x\mid z)p(z),
$$

所以 ELBO 可以进一步写成

$$
\mathrm{ELBO}(q)
=
\mathbb E_q[\log p(x\mid z)]
-
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z)\big).
$$

这条式子最常见，也最有解释力。

第一项

$$
\mathbb E_q[\log p(x\mid z)]
$$

表示：在潜变量分布 $q(z)$ 下，模型对观测 $x$ 的解释能力。

第二项

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z)\big)
$$

表示：近似后验不要偏离先验太远。

所以最大化 ELBO 的意思是：

- 一方面让潜变量更能解释观测；
- 另一方面不让近似后验任意跑远。

在 VAE 语境下，这两项通常被读成：

- reconstruction term
- KL regularization term

---

## 6. ELBO 到底在 reduction 什么

如果问 ELBO 的目标“在 reduction 什么”，最准确的回答有三层。

### 6.1 第一层：减少后验近似误差

它直接减少的是

$$
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

这是最核心的一层。

### 6.2 第二层：减少下界与真实 evidence 的缺口

因为

$$
\log p(x)-\mathrm{ELBO}(q)
=
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big),
$$

所以最大化 ELBO 也等于尽量缩小：

$$
\log p(x)-\mathrm{ELBO}(q).
$$

### 6.3 第三层：把难积分问题改写成优化问题

原始困难是：

$$
p(x)=\int p(x,z)\,dz
$$

不可积。  
VI 把这个问题改写成：

- 选择一个可处理的分布族 $q_\phi(z)$；
- 优化其参数 $\phi$。

所以 ELBO 也是一种计算上的 reduction：  
把 intractable inference 变成 tractable optimization。

---

## 7. ELBO 与 free energy 的关系

在很多文献里，人们把

$$
\mathcal F(q)
=
\mathbb E_q[\log q(z)-\log p(x,z)]
$$

叫做 variational free energy。

它和 ELBO 的关系只是一个负号：

$$
\mathcal F(q) = -\mathrm{ELBO}(q).
$$

所以：

- 最小化 variational free energy
- 等价于最大化 ELBO

这个名字不是随便借来的。  
它和统计物理里的变分自由能在数学结构上是同构的，只是在机器学习里，“能量”被替换成了负对数概率。

---

## 8. ELBO 和 variance reduction 不是一回事

这里最容易混淆的是：

- `variational inference`
- `variance reduction`

二者不是同一个概念。

### 8.1 Variational inference

这里的 `variational` 来自变分法。  
它说的是：在一个可控分布族里做优化。

### 8.2 Variance reduction

这里的 `variance` 指的是估计器的方差。  
例如在 VAE 训练中，要估计

$$
\nabla_\phi \mathbb E_{q_\phi(z)}[f(z)],
$$

这个梯度估计可能方差很大，于是会用：

- reparameterization trick
- control variates
- baselines
- Rao-Blackwellization

这些都是 **variance reduction** 技术。

所以关系是：

- ELBO / VI 决定了优化目标是什么；
- variance reduction 帮助你更稳定地优化这个目标。

---

## 9. 一句话记忆版

ELBO 最短可以记成下面这条恒等式：

$$
\log p(x)
=
\mathrm{ELBO}(q)
+
D_{\mathrm{KL}}\!\big(q(z)\,\|\,p(z\mid x)\big).
$$

它说明：

- ELBO 是 $\log p(x)$ 的下界；
- 最大化 ELBO 等价于最小化近似后验与真实后验之间的 KL 散度；
- ELBO 真正在 reduction 的，是后验近似误差和 evidence gap；
- 它不是 variance reduction，只是后者经常在训练时配套出现。
