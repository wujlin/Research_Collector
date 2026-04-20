---
title: "Stochastic Thermodynamics for Autoregressive Generative Models"
authors: "Takahiro Sagawa"
venue: "arXiv (2026)"
date_read: "2026-04-16"
topics: ["随机热力学", "自回归模型", "非马尔可夫", "熵产生", "Transformer"]
---

# Stochastic Thermodynamics for Autoregressive Generative Models — 精读笔记

> **论文全称**：Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective  
> **作者**：Takahiro Sagawa（东京大学）  
> **日期**：2026-04-10  

---

## 0 一句话总结

本文为所有 **自回归生成模型**（Transformer / RNN / Kalman filter / SSM / Mamba）建立了统一的 **随机热力学（stochastic thermodynamics）** 框架：定义了非马尔可夫观测序列的 **熵产生（entropy production）**，证明其可从单条采样轨迹高效计算，并在 GPT-2 实验与 Kalman 滤波解析案例中进行了验证和分解。

---

## 1 问题设定：为什么这篇文章要从非马尔可夫过程出发

### 1.1 经典随机热力学最顺手的对象是马尔可夫过程

随机热力学最常见的对象是马尔可夫过程。原因很简单：一旦动力学只依赖当前状态，前向和后向路径概率都可以逐步写成局部转移核的乘积，于是熵产生就能被写成一串局部对数比。最熟悉的形式是 Crooks 型时间反演：

$$
\sigma(y_{1:T}) = \sum_t \ln \frac{p_t(y_{t+1}\mid y_t)}{p_t(y_t\mid y_{t+1})}.
$$

这条式子默认了一个强条件：当前一步的统计规律只由前一步决定。可现代生成模型里的观测序列往往不是这样。Transformer 生成第 $t+1$ 个 token 时，条件的是整段历史；RNN、Kalman、SSM 和 Mamba 虽然有递归状态，但观测边缘过程 $y_t$ 仍然一般是非马尔可夫的。于是问题就变成：

**如果观测序列本身是非马尔可夫的，随机热力学里的熵产生还能不能定义，而且能不能算？**

### 1.2 这篇文章抓住的共同骨架是“确定性记忆 + 随机发射”

作者的第一步不是直接谈 Transformer，而是先抽出所有自回归模型共享的最小结构。这个结构只有两层：

1. 过去观测先被压缩成一个确定性的内部状态
   $$
   h_t = \Phi_t(y_1,\dots,y_t).
   $$
2. 再由这个内部状态随机地产生下一步观测
   $$
   y_{t+1} \sim p_t(y_{t+1}\mid h_t).
   $$

论文随后把第一步记成

$$
h_t = f_t^\rightarrow(y_{1:t}), \tag{1}
$$

其中

$$
f_t^\rightarrow(y_{1:t}) \equiv \Phi_t(y_1,\dots,y_t). \tag{2}
$$

于是前向整条序列的路径概率就能写成

$$
P_\rightarrow(y_{1:T}) = \prod_{t=0}^{T-1} p_t\!\left(y_{t+1}\mid f_t^\rightarrow(y_{1:t})\right). \tag{3}
$$

这一步是全文的根。因为后面所有 forward / backward path probability、熵产生、计算复杂度，都是围着这条乘积结构展开的。

这套写法里最重要的约束不是“有隐状态”本身，而是：**隐状态的大小不能随时间增长。**  
如果 $h_t$ 只是把完整历史原样存起来，那当然任何非马尔可夫过程都能塞进来，但这不再是作者想分析的“有界记忆自回归模型”。他们真正研究的是：

- 历史长度可以不断增长；
- 但模型只能把它压缩成一个固定大小的内部表示；
- 发射核只看这个压缩表示。

这也是这篇文章和“任意高阶历史模型”之间的边界。

![Figure 1(a): 前向过程的因果结构——一般（非递归）情形](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-03-figure-01.jpg)

图 1(a) 画出的就是这条因果结构。蓝色箭头对应确定性映射 $f_t^\rightarrow$，绿色箭头对应随机发射核 $p_t$。这里的非马尔可夫性不是额外加上的，而是直接来自这样一个事实：每个 $h_t$ 都在吸收全部过去 $y_{1:t}$ 的信息。

### 1.3 递归与非递归：为什么 Transformer 和 RNN 都落在同一个框架里

接下来论文再把这套一般框架分成两个子类。

第一类是**一般情形**。这里 $h_t=\Phi_t(y_1,\dots,y_t)$ 不要求能写成 $(h_{t-1},y_t)$ 的函数。Transformer 就属于这一类。它当然可以把完整历史映到一个上下文表示，但这个映射一般不能化简成简单的两变量递推。

第二类是**递归情形**。这时作者要求

$$
h_t = \phi_t(h_{t-1}, y_t), \tag{4}
$$

也就是

$$
\Phi_t(y_1,\dots,y_t)
=
\phi_t\!\big(\Phi_{t-1}(y_1,\dots,y_{t-1}),\, y_t\big). \tag{5}
$$

一旦写成这个形式，联合过程 $(h_t,y_t)$ 就成了马尔可夫的。RNN、Kalman、SSM 和 Mamba 都属于这一类。

这里要把两个层面分清：

- **观测过程 $y_t$** 一般仍然是非马尔可夫的；
- **联合过程 $(h_t,y_t)$** 在递归情形下是马尔可夫的。

这也是为什么作者一直强调：这篇文章研究的是**观测序列的随机热力学**，而不是某个额外引入的随机 latent dynamics。

这里要把“$h_t$ 是递归的”和“$y_t$ 仍然是非马尔可夫的”之间的关系说清楚。  
对模型内部来说，$h_t$ 当然是可见的：给定过去序列，模型会先更新内部记忆

$$
h_t=\phi_t(h_{t-1},y_t),
$$

再由这个记忆状态发射下一步输出

$$
y_{t+1}\sim p_t(y_{t+1}\mid h_t).
$$

如果把状态变量写成联合状态 $(h_t,y_t)$，那么递归模型在这层通常就是 Markov 的。  
但这篇文章后面研究的对象不是联合状态，而是**外部真正看到的输出序列** $y_1,y_2,\dots$ 。这时，$h_t$ 并没有从模型里消失，而是**没有被保留为分析对象的一部分**。于是对外部观察者来说，真正 relevant 的条件分布是

$$
P(y_{t+1}\mid y_{1:t}) = p_t(y_{t+1}\mid h_t),
\qquad
h_t=\Phi_t(y_{1:t}),
$$

它一般不能再简化成

$$
P(y_{t+1}\mid y_t).
$$

所以，递归 $\phi_t$ 说明的是**内部记忆的更新是 Markov 风格的**；而论文说 $y_t$ 是 non-Markov，指的是**只看外部输出序列时，下一步分布仍然依赖更长的历史，而不只依赖当前一步**。

![Table 1: 各架构与通用框架的对应关系](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-05-table-01.jpg)

表 1 的作用就是把五类模型都投影到这一个骨架上。真正需要抓的不是各个公式细节，而是它们都满足同一件事：

- 有一个确定性记忆状态；
- 下一步观测从这个状态随机发射出来。

把图里的五个例子直接改写成正文，会更清楚：

1. Transformer：隐状态是上下文向量，写成
   $$
   h_t=\Phi(y_1,\dots,y_t),
   $$
   发射核是
   $$
   p_t(y_{t+1}\mid h_t)=\operatorname{softmax}(W_{\mathrm{out}}h_t).
   $$

2. RNN：隐状态递归更新为
   $$
   h_t=\phi(h_{t-1},y_t)=\tanh(W_h h_{t-1}+W_y y_t+b),
   $$
   发射核是
   $$
   p_t(y_{t+1}\mid h_t)=\operatorname{softmax}(W_{\mathrm{out}}h_t+b_{\mathrm{out}}).
   $$

3. Kalman：隐状态是一步预测
   $$
   h_t=\hat x_{t+1\mid t},
   $$
   递归更新写成
   $$
   \phi_t(h,y)=A_t\big[(I-K_tC_t)h+K_t y\big],
   $$
   发射核是
   $$
   p_t(y_{t+1}\mid h_t)=\mathcal N(C_{t+1}h_t,\,S_{t+1}).
   $$

4. SSM：递归更新是
   $$
   \phi_t(h,y)=A_t h+B_t y,
   $$
   发射核是
   $$
   p_t(y_{t+1}\mid h_t)=\operatorname{softmax}(W_{\mathrm{out}}C_t h_t).
   $$

5. Mamba：把状态扩成 $(h_t,y_t)$ 之后，更新写成
   $$
   \phi_t'(h',y)=\big(A(y)h+B(y)y,\; y\big),
   $$
   发射核是
   $$
   p_t(y_{t+1}\mid h_t)=\operatorname{softmax}(W_{\mathrm{out}}C(y_t)h_t).
   $$

这里还有一个细节很值得记住。Transformer 如果把完整 KV-cache 都算进状态，形式上也可以写成递归更新；但 KV-cache 的大小会随序列长度线性增长，这违反了作者这里“固定大小记忆”的基本要求。所以论文把标准 Transformer 视为**非递归但有界状态表示**的代表，而不是把 KV-cache 递归化当作主定义。

---

## 2 backward process 和熵产生：这篇文章真正的新定义在哪里

### 2.1 backward process 不是重新训练一个反向模型，而是把同一台机器反着跑

全文真正的新对象从这里开始出现。作者不是去训练一个新的 backward model，而是把前向模型里的两套组件原样拿来，只把调用顺序反过来：

- 发射核还是原来的 $p_t$；
- 确定性映射还是原来的 $\Phi_t$；
- 只是时间顺序从前向的 $0,1,\dots,T-1$ 变成反向调用。

反向过程中，作者先定义

$$
\tilde y_s = y_{T-s+1}, \tag{7}
$$

也就是把前向序列反过来看。然后把后向使用的参数索引写成

$$
\tilde p_s = p_{T-s}, \qquad \tilde \Phi_s = \Phi_{T-s+1}. \tag{8}
$$

再定义后向隐状态

$$
g_{t+1}^\leftarrow(y_{T:t+1})
\equiv
\Phi_{t+1}(y_T,y_{T-1},\dots,y_{t+1}), \tag{12}
$$

于是后向路径概率变成

$$
P_\leftarrow(y_{T:1})
=
\prod_{t=1}^{T}
p_t\!\left(y_t \mid g_{t+1}^\leftarrow(y_{T:t+1})\right). \tag{13}
$$

这一步的意思很具体：  
对于前向过程，$y_{t+1}$ 是在“过去压缩表示” $f_t^\rightarrow(y_{1:t})$ 条件下发射出来的。  
对于后向过程，$y_t$ 则是在“未来压缩表示” $g_{t+1}^\leftarrow(y_{T:t+1})$ 条件下，用同一个发射核 $p_t$ 来生成。

这就是论文所谓的 “run the same machinery in reverse”。

![Figure 1(b): 后向过程的因果结构](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-03-figure-02.jpg)

图 1(b) 画出的正是这个 backward process。这里一个容易误会的点是：即使某条后向样本恰好满足 $\tilde y_s = y_{T-s+1}$，一般也**不能**推出 $\tilde h_s = h_{T-s+1}$。原因很直接：同一个确定性映射作用在正向前缀和反向前缀上，得到的内部状态一般不同。

### 2.2 熵产生的定义：前向和后向路径测度之间的 KL 散度

有了前向路径概率 $P_\rightarrow$ 和后向路径概率 $P_\leftarrow$，作者就把观测序列的熵产生定义成两者之间的 KL 散度：

$$
\mathcal S_y
=
D_{\mathrm{KL}}\!\left(P_\rightarrow(y_{1:T}) \,\|\, P_\leftarrow(y_{T:1})\right)
=
\mathbb E_{P_\rightarrow}\!\left[
\ln \frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})}
\right]
\ge 0. \tag{14}
$$

相应的随机熵产生是单条轨迹上的对数比：

$$
\sigma(y_{1:T})
\equiv
\ln \frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})}. \tag{18}
$$

再把前向和后向路径概率的乘积结构代进去，就得到

$$
\mathcal S_y
=
\mathbb E_{P_\rightarrow}\!\left[
\ln \frac{\prod_{t=0}^{T-1} p_t\!\left(y_{t+1}\mid f_t^\rightarrow(y_{1:t})\right)}
{\prod_{t=1}^{T} p_t\!\left(y_t\mid g_{t+1}^\leftarrow(y_{T:t+1})\right)}
\right], \tag{15}
$$

进一步拆开是

$$
\mathcal S_y
=
\mathbb E_{P_\rightarrow}\!\left[-\ln \tilde p(y_T) + \ln p(y_1)\right]
\;+\;
\sum_{t=1}^{T-1}
\mathbb E_{P_\rightarrow}\!\left[
\ln
\frac{p_t\!\left(y_{t+1}\mid f_t^\rightarrow(y_{1:t})\right)}
{p_t\!\left(y_t\mid g_{t+1}^\leftarrow(y_{T:t+1})\right)}
\right]. \tag{16}
$$

这条式子最好分成两部分读：

- 第一项是边界项，比较的是前向初始分布和后向初始分布；
- 第二项是时间内部每一步的对数比，比较的是“用过去预测下一步”和“用未来反推当前步”。

如果进一步采用论文里讨论的特殊选择

$$
\tilde p(\tilde y_1)=p(y_T), \tag{10}
$$

那么第一项就会变成单时间边缘分布的 Shannon 熵变化：

$$
\mathbb E_{P_\rightarrow}[-\ln p(y_T)+\ln p(y_1)]. \tag{17}
$$

作者的主定义并不依赖这一步，因为在一般自回归模型里，精确计算 $p(y_T)$ 并不现实。

### 2.3 为什么这一定满足涨落定理

有了随机熵产生

$$
\sigma(y_{1:T})
=
\ln \frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})},
$$

就立刻有

$$
\mathcal S_y = \mathbb E_{P_\rightarrow}[\sigma(y_{1:T})], \tag{19}
$$

以及积分涨落定理

$$
\mathbb E_{P_\rightarrow}\!\left[e^{-\sigma(y_{1:T})}\right] = 1. \tag{20}
$$

这里没有更多神秘结构。它成立的原因就是：

$$
e^{-\sigma(y_{1:T})}
=
\frac{P_\leftarrow(y_{T:1})}{P_\rightarrow(y_{1:T})},
$$

所以对前向分布平均之后，正好把比值还原成后向路径概率的总和。  
这一步和前面 PRE 那篇里看到的积分涨落定理是同一逻辑，只不过这里的路径对象不再是马尔可夫 SDE，而是由自回归模型定义的非马尔可夫观测序列。

### 2.4 递归情形和马尔可夫极限：这套定义为什么和经典结果兼容

在递归情形下，后向隐状态还可以写成

$$
\tilde h_s = \tilde \phi_s(\tilde h_{s-1}, \tilde y_s), \tag{21}
$$

其中 $\tilde \phi_s = \phi_{T-s+1}$。这说明 backward process 在递归架构里同样能保持递推结构。

但作者紧接着强调了一个很关键的点：即使联合过程 $(h_t,y_t)$ 在前向是马尔可夫的，直接把它拿来做 forward / backward KL 并不总是好主意。因为前向和后向在 latent 层上的支撑集可能根本不重合，导致更高层的熵产生发散。于是这篇文章刻意把定义固定在**观测序列 $y_{1:T}$** 上。

如果进一步退到真正的马尔可夫极限，也就是直接取

$$
h_t = y_t,
$$

那么

$$
g_{t+1}^\leftarrow(y_{T:t+1}) = y_{t+1},
$$

式 `(16)` 的内部项就退化成

$$
\sum_{t=1}^{T-1}
\mathbb E_{P_\rightarrow}\!\left[
\ln \frac{p_t(y_{t+1}\mid y_t)}{p_t(y_t\mid y_{t+1})}
\right], \tag{22}
$$

这就回到了标准 Crooks 公式。所以这篇文章不是另起炉灶，而是在更一般的非马尔可夫 setting 里，把经典随机热力学的 forward/backward 比值定义延伸了出去。

---

## 3 为什么这套定义是可计算的：自回归结构如何绕开指数复杂度

### 3.1 一般非马尔可夫过程为什么难

如果你只拿到一个未知来源的非马尔可夫过程，真正困难的地方在于条件概率本身。  
例如要估计

$$
P_\rightarrow(y_{t+1}\mid y_{1:t}),
$$

你需要很多条拥有相同历史前缀 $y_{1:t}$ 的轨迹。历史越长，这样的重复样本越难遇到；在连续空间里，几乎根本不会重复。这就是一般非马尔可夫熵产生估计会碰到的组合爆炸。

### 3.2 自回归模型为什么刚好规避了这个问题

这篇文章的核心计算洞察就在这里：  
在 autoregressive model 里，前向和后向路径概率不是未知的统计对象，而是模型直接给出的可求值函数。

它依赖三条结构条件。

第一，隐状态是确定性的。  
给定一条具体轨迹 $y_{1:T}$，前向隐状态

$$
h_t = \Phi_t(y_{1:t})
$$

和后向隐状态

$$
g_{t+1}^\leftarrow(y_{T:t+1})
$$

都可以直接算出来，不需要对 latent state 做随机边缘化。

第二，发射核是显式的。  
模型直接提供

$$
p_t(y_{t+1}\mid h_t).
$$

对 Transformer，这就是 softmax 输出；对 Kalman，这就是高斯发射核；对 SSM 和 Mamba，也是显式的条件分布。

第三，边界项也是显式给定的。  
前向初始分布 $p(y_1)$ 和后向初始分布 $\tilde p(\tilde y_1)$ 都是已知函数，而不是需要从数据中额外估计的量。

于是单条轨迹上的随机熵产生

$$
\sigma(y_{1:T})
$$

根本不需要枚举大量历史，只需要做两次标准对数似然评估：

1. 正向输入原序列，累计前向 log-prob；
2. 反向输入逆序列，累计后向 log-prob。

论文把单条轨迹的计算代价写成

$$
C_1 = 2 C_{\mathrm{LL}}, \tag{27}
$$

其中 $C_{\mathrm{LL}}$ 是一次 log-likelihood evaluation 的代价。  
于是 Monte Carlo 估计就是

$$
\mathcal S_y
\approx
\frac{1}{N}\sum_{n=1}^{N}\sigma\!\left(y_{1:T}^{(n)}\right), \tag{25}
$$

总成本

$$
C_{\mathrm{total}} = N C_1. \tag{26}
$$

对 Transformer，单次 log-likelihood 大致是 $O(T^2)$；对 RNN、SSM、Mamba 这类递归架构，大致是 $O(T)$。这里没有额外的“非马尔可夫惩罚项”，因为复杂历史已经被模型自己的确定性记忆结构吸收了。

### 3.3 时间粗粒化：为什么 token 级反转不够好，block 级反转更有解释力

把这套定义直接用在语言模型上，会马上遇到一个问题。  
如果你把 token 序列完全倒过来，像

$$
(\mathrm{This},\mathrm{is},\mathrm{a},\mathrm{book})
\longrightarrow
(\mathrm{book},\mathrm{a},\mathrm{is},\mathrm{This}),
$$

那么得到的巨大熵产生主要反映的是**语法彻底被打坏了**，而不是更深层的语义或因果不可逆性。

所以作者接着做了时间粗粒化。  
在时间齐次模型里，也就是

$$
p_t = p,\qquad \Phi_t = \Phi \quad \text{for all } t, \tag{28}
$$

可以先把 token 序列切成 block：

$$
y_{t'}' = (y_{(t'-1)l+1},\dots,y_{t'l}), \tag{30}
$$

然后只反转 block 的顺序，而保持 block 内 token 的顺序不变。例如

$$
(a,b,c,d,e,f)
\longrightarrow
(\underbrace{d,e,f}_{B_2},\underbrace{a,b,c}_{B_1}). \tag{32}
$$

这时粗粒化后的随机熵产生定义成

$$
\sigma'(y_{1:T})
=
\ln P(y_{1:T}) - \ln P(\tilde y_{1:\tilde T}'), \tag{34}
$$

也就是用同一个模型分别计算原始序列和 block-reversed 序列的对数似然差。

这一步为什么有意义？因为它把“不可逆性”从 token 级语法顺序上抬到了 block 级结构顺序上。  
如果 block 取成句子，那么反转的就是句子顺序而不是词序。这样得到的量更有机会反映：

- 跨句子的叙事方向；
- 事件的时间顺序；
- 因果结构的正反差异。

而且它的计算代价并没有变高。因为你仍然只是在做两次普通的 log-likelihood evaluation：

- 一次喂原始序列；
- 一次喂 block-reversed 序列。

所以这一步既保持了涨落定理形式，也给后面的 GPT-2 实验提供了更有解释力的观测对象。

---

## 4 GPT-2 概念验证实验

### 4.1 Monte Carlo 采样实验（Section 5.1）

**设置**：从 GPT-2（117M 参数）以温度 $\tau = 1$ 自回归采样 $T = 120$ 个 token 的序列，收集 $N \approx 500$ 条轨迹。

![Figure 3(a): Token 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![Figure 3(b): Block 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-02.jpg)

**图 3** 的关键发现：

| 度量 | 每 token 均值 | 解释 |
|:---|:---:|:---|
| $\sigma_{\text{token}} / T$ | **≈ 3.99** | Token 级反转：极高，因语法破坏 |
| $\sigma_{\text{block}} / T'$ | **≈ 0.469** | 块级反转：低一个数量级，更有解释力 |

**结论**：Token 级熵产生被语法破坏的 artifact 主导，而块级熵产生可能提取更具物理/语义意义的不可逆信号。

### 4.2 因果 vs. 非因果文本实验（Section 5.2）

用 Claude Opus 4.6 生成两组各 30 条文本：
- **因果文本**（causal）：句子描述时间有序的因果链（如"杯子滑落 → 摔碎 → 扫地"）
- **非因果文本**（non-causal）：独立事实陈述，顺序无关（如"小提琴用弓拉 → 长笛用气吹 → ..."）

![Figure 4(a): Token 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-01.jpg)

![Figure 4(b): Block 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-02.jpg)

**图 4** 的关键发现：

- **Token 级**（图 4a）：因果与非因果文本 **无显著差异**（$p = 0.78$），被语法 artifact 主导。
- **Block 级**（图 4b）：因果文本的 $\sigma_{\text{block}}/T$ **显著高于** 非因果文本（Mann-Whitney $U = 746$, $p = 4.5 \times 10^{-6}$, $r = 0.66$）。

> **物理直觉**：因果文本反转句子顺序后，"效果先于原因"会使反向路径概率大幅下降，导致更大的熵产生。非因果文本句子顺序无关紧要，反转后概率变化小。

---

## 5 Kalman 滤波解析案例

### 5.1 设置

考虑线性高斯系统：

$$
x_{t+1} = Ax_t + w_t, \quad y_t = Cx_t + v_t
$$

其中 $w_t \sim \mathcal{N}(0, Q)$, $v_t \sim \mathcal{N}(0, R)$。真实状态 $x_t$ **不出现在框架中**——Kalman 滤波器被视为一个 **生成模型**，隐状态 $h_t = \hat{x}_{t+1|t}$ 是一步预测估计。

在稳态 Kalman 滤波器的创新表示（innovation representation）下，前向路径概率为：

$$
P_\rightarrow(y_{1:T}) = \prod_{t=1}^{T} \mathcal{N}(e_t; 0, S), \quad e_t = y_t - C\hat{x}_{t|t-1}
$$

其中 $S = CPC^\top + R$ 是创新协方差，$e_t$ 是互相独立的高斯创新（innovation）。

### 5.2 创新反转矩阵（Innovation Reversal Matrix）

这是本文的优美数学贡献之一。定义：
- $\mathcal{H}$：块下三角脉冲响应矩阵，$\mathbf{y} = \mathcal{H}\mathbf{e}$
- $J$：时间反转置换矩阵，$J\mathbf{y} = (y_T^\top, \ldots, y_1^\top)^\top$

则后向创新 $\mathbf{e}^B = \mathcal{R}\mathbf{e}$，其中 **创新反转矩阵** 为：

$$
\boxed{\mathcal{R} \equiv \mathcal{H}^{-1} J \mathcal{H}}
$$

### 5.3 解析熵产生

下面推导 Kalman 滤波框架下熵产生的闭合表达式。

**第一步：前向与后向的联合分布。**  
在稳态 Kalman 滤波器的创新表示下，前向过程中所有创新 $e_t$ 是独立同分布的高斯变量，因此前向路径测度为：

$$
P_\rightarrow(\mathbf{e}) = \mathcal{N}(\mathbf{e};\, 0,\, I_T \otimes S)
$$

其中 $\mathbf{e} = (e_1^\top, \ldots, e_T^\top)^\top$ 是堆叠创新向量。后向过程将时间反转后的观测序列输入同一 Kalman 滤波器，产生后向创新 $\mathbf{e}^B = \mathcal{R}\,\mathbf{e}$（线性变换）。后向模型 **假设** 后向创新也服从 $\mathcal{N}(0, I_T \otimes S)$，但在前向测度 $P_\rightarrow$ 下，$\mathbf{e}^B$ 的真实分布为：

$$
\mathbf{e}^B \sim \mathcal{N}\!\left(0,\; \Sigma^B\right), \quad \Sigma^B \equiv \mathcal{R}\,(I_T \otimes S)\,\mathcal{R}^\top
$$

**第二步：多元高斯 KL 散度公式。**  
对两个零均值高斯 $\mathcal{N}(0, \Sigma_1)$ 和 $\mathcal{N}(0, \Sigma_2)$，标准 KL 散度公式为：

$$
D_{\text{KL}}\!\left(\mathcal{N}(0,\Sigma_1) \;\big\|\; \mathcal{N}(0,\Sigma_2)\right) = \frac{1}{2}\!\left[\text{tr}(\Sigma_2^{-1}\Sigma_1) - d + \ln\frac{|\Sigma_2|}{|\Sigma_1|}\right]
$$

其中 $d$ 是向量维度。

**第三步：行列式消去。**  
此处 $\Sigma_1 = \Sigma^B = \mathcal{R}(I_T \otimes S)\mathcal{R}^\top$，$\Sigma_2 = I_T \otimes S$，$d = Tn_y$。由于 $\mathcal{R} = \mathcal{H}^{-1}J\mathcal{H}$，其中 $J$ 是块置换矩阵（$|\!\det J| = 1$），故 $|\!\det \mathcal{R}| = 1$，因此：

$$
|\Sigma^B| = |\mathcal{R}|^2 \cdot |I_T \otimes S| = |I_T \otimes S| = |\Sigma_2|
$$

对数行列式项 $\ln(|\Sigma_2|/|\Sigma_1|) = 0$。

**第四步：代入得到 trace 公式。**  
将上述结果代入 KL 公式：

$$
\boxed{\mathcal{S}_y = D_{\text{KL}}(P_\rightarrow \| P_\leftarrow) = \frac{1}{2}\left[\text{tr}\!\left((I_T \otimes S^{-1})\,\mathcal{R}\,(I_T \otimes S)\,\mathcal{R}^\top\right) - Tn_y\right]}
$$

等价地，用后向创新的协方差表示：

$$
\mathcal{S}_y = \frac{1}{2}\sum_{s=1}^{T}\left[\mathbb{E}_{P_\rightarrow}\!\left[(e_s^B)^\top S^{-1} e_s^B\right] - n_y\right]
$$

> **操作含义**：后向创新 $e_s^B$ 在前向测度下的协方差 $\Sigma_s^B$ 偏离 $S$ 的程度，累积起来就是总熵产生。

### 5.4 标量与多变量的渐近行为

- **标量情形**（$n_x = n_y = 1$）：任何平稳标量高斯过程都是时间可逆的，熵产生 $\mathcal{S}_y$ 在 $T \to \infty$ 时 **饱和** 到有限值（纯粹是初始条件的边界效应）。
- **多变量情形**（$n_y > 1$）：当交叉协方差矩阵不对称时，过程具有真正的时间不可逆性，$\mathcal{S}_y$ 随 $T$ **线性增长**。

### 5.5 数值验证

![Figure 5(a): 标量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-01.jpg)

![Figure 5(b): 多变量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-02.jpg)

**图 5**：$N = 20{,}000$ 条轨迹的 Monte Carlo 估计（蓝色点 ± 标准误差）与解析表达式（黑色曲线）的对比。两者在 $T = 5, 10, \ldots, 50$ 的全部范围内高度吻合，验证了理论的正确性。

---

## 6 熵产生的回顾性分解（Retrospective Decomposition）

这是本文最深刻的理论结果之一。

### 6.1 逐步分解

利用贝叶斯回顾推断（Bayesian retrodiction），熵产生可精确分解为 **非负逐步贡献**。下面给出完整证明。

**第一步：联合 KL 散度的链式法则。**  
KL 散度满足如下链式法则：对联合分布 $p(x, z)$ 和 $q(x, z)$，

$$
D_{\text{KL}}(p(x,z) \| q(x,z)) = D_{\text{KL}}(p(z) \| q(z)) + \mathbb{E}_{p(z)}\!\left[D_{\text{KL}}(p(x|z) \| q(x|z))\right]
$$

**第二步：逐步剥离。**  
将 $y_{1:T}$ 写为 $y_t$ 与"剩余未来" $y_{t+1:T}$ 的联合，从 $t = 1$ 开始迭代应用链式法则：

$$
\mathcal{S}_y = D_{\text{KL}}\!\left(P_\rightarrow(y_{1:T}) \;\big\|\; P_\leftarrow(y_{1:T})\right)
$$

$$
= D_{\text{KL}}\!\left(P_\rightarrow(y_{2:T}) \;\big\|\; P_\leftarrow(y_{2:T})\right) + \mathbb{E}_{P_\rightarrow(y_{2:T})}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_1|y_{2:T}) \;\big\|\; P_\leftarrow(y_1|y_{2:T})\right)\right]
$$

对第一项继续剥离 $y_2$，如此递推直到 $t = T$，得到：

$$
\mathcal{S}_y = \sum_{t=1}^{T} \mathbb{E}_{P_\rightarrow(y_{t+1:T})}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | y_{t+1:T}) \;\big\|\; P_\leftarrow(y_t | y_{t+1:T})\right)\right]
$$

**第三步：后向模型条件分布的简化。**  
在后向过程中，$y_t$ 由发射核 $p_t$ 在后向隐状态 $g_{t+1}^\leftarrow(y_{T:t+1})$ 条件下生成。由于 $g_{t+1}^\leftarrow$ 是 $y_{t+1:T}$ 的确定性函数，后向模型对 $y_t$ 的条件分布为：

$$
P_\leftarrow(y_t | y_{t+1:T}) = p_t\!\left(y_t \;\big|\; g_{t+1}^\leftarrow(y_{T:t+1})\right)
$$

而前向模型的条件分布 $P_\rightarrow(y_t | y_{t+1:T})$ 则是通过 Bayes 定理从联合分布获得的 **回顾分布**（retrodictive distribution），一般不等于简单的发射核。

**结论：** 将第三步代入第二步，定义 $\mathcal{D}_t$ 为第 $t$ 步的贡献，由 KL 散度的非负性立即得到 $\mathcal{D}_t \geq 0$，从而：

$$
\boxed{\mathcal{S}_y = \sum_{t=1}^{T} \mathcal{D}_t, \quad \mathcal{D}_t \geq 0}
$$

其中：

$$
\mathcal{D}_t = \mathbb{E}_{P_\rightarrow(y_{t+1:T})}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | y_{t+1:T}) \;\big\|\; p_t(y_t | g_{t+1}^\leftarrow(y_{T:t+1}))\right)\right]
$$

**含义**：$\mathcal{D}_t$ 衡量的是，在给定未来 $y_{t+1:T}$ 时，**贝叶斯回顾分布**（真正的后验 $P_\rightarrow(y_t | y_{t+1:T})$）与 **协议反转后向模型**（$p_t(y_t | g_{t+1}^\leftarrow)$）之间的差距。

> 一个直观的日常例子：  
> 前向："如果我不学习，妈妈就会生气。"  
> 贝叶斯回顾："如果妈妈生气了，那说明我没学习。"（大概率为真）  
> 协议反转后向："如果妈妈生气了，然后我就不学习了。"（在日常生活中大概率为假）  
> 两者的差距正是 $\mathcal{D}_t$，在这个例子中很大——高度不可逆。

### 6.2 压缩损失 + 模型失配

每个 $\mathcal{D}_t$ 可进一步精确分解为两个非负项。下面给出完整推导。

**第一步：插入中间分布。**  
在 $\mathcal{D}_t$ 的 KL 散度内，在"完整后验" $P_\rightarrow(y_t | y_{t+1:T})$ 与"后向发射核" $p_t(y_t | g_{t+1}^\leftarrow)$ 之间，插入一个自然的中间分布——**压缩后验** $P_\rightarrow(y_t | g_{t+1}^\leftarrow)$，即仅以后向隐状态（而非完整未来）为条件的回顾分布：

$$
\ln \frac{P_\rightarrow(y_t | y_{t+1:T})}{p_t(y_t | g_{t+1}^\leftarrow)} = \underbrace{\ln \frac{P_\rightarrow(y_t | y_{t+1:T})}{P_\rightarrow(y_t | g_{t+1}^\leftarrow)}}_{\text{（I）压缩导致的信息损失}} + \underbrace{\ln \frac{P_\rightarrow(y_t | g_{t+1}^\leftarrow)}{p_t(y_t | g_{t+1}^\leftarrow)}}_{\text{（II）同一条件下的模型失配}}
$$

**第二步：对两项分别取期望。**  
对 $y_t \sim P_\rightarrow(y_t | y_{t+1:T})$ 取期望，第（I）项变为条件 KL 散度：

$$
\mathbb{E}_{y_t | y_{t+1:T}}\!\left[\text{（I）}\right] = D_{\text{KL}}\!\left(P_\rightarrow(y_t | y_{t+1:T}) \;\big\|\; P_\rightarrow(y_t | g_{t+1}^\leftarrow)\right)
$$

再对 $y_{t+1:T} \sim P_\rightarrow$ 取外层期望，利用条件互信息的恒等式 $I(X; Y | Z) = \mathbb{E}_Y[D_{\text{KL}}(P(X|Y,Z) \| P(X|Z))]$（注意 $g_{t+1}^\leftarrow$ 是 $y_{t+1:T}$ 的确定性函数，故条件于 $y_{t+1:T}$ 等价于同时条件于 $y_{t+1:T}$ 和 $g_{t+1}^\leftarrow$），得到：

$$
\mathcal{L}_t = \mathbb{E}_{P_\rightarrow(y_{t+1:T})}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | y_{t+1:T}) \;\big\|\; P_\rightarrow(y_t | g_{t+1}^\leftarrow)\right)\right] = I_{P_\rightarrow}\!\left(y_t;\, y_{t+1:T} \;\big|\; g_{t+1}^\leftarrow\right) \geq 0
$$

对第（II）项：$\ln \frac{P_\rightarrow(y_t | g_{t+1}^\leftarrow)}{p_t(y_t | g_{t+1}^\leftarrow)}$ 仅依赖 $(y_t, g_{t+1}^\leftarrow)$。利用塔式期望（tower property），先对 $y_t | y_{t+1:T}$ 取期望，再对 $y_{t+1:T}$ 取期望，等价于对联合分布 $P_\rightarrow(y_t, y_{t+1:T})$ 取期望。由于对数比值仅通过 $g_{t+1}^\leftarrow$ 依赖 $y_{t+1:T}$，可进一步边缘化为对 $P_\rightarrow(y_t, g_{t+1}^\leftarrow)$ 取期望：

$$
\mathcal{M}_t = \mathbb{E}_{P_\rightarrow(g_{t+1}^\leftarrow)}\!\left[\mathbb{E}_{P_\rightarrow(y_t | g_{t+1}^\leftarrow)}\!\left[\ln \frac{P_\rightarrow(y_t | g_{t+1}^\leftarrow)}{p_t(y_t | g_{t+1}^\leftarrow)}\right]\right] = \mathbb{E}_{g_{t+1}^\leftarrow}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | g_{t+1}^\leftarrow) \;\big\|\; p_t(y_t | g_{t+1}^\leftarrow)\right)\right] \geq 0
$$

**结论：**

$$
\boxed{\mathcal{D}_t = \underbrace{\mathcal{L}_t}_{\text{压缩损失}} + \underbrace{\mathcal{M}_t}_{\text{模型失配}}}
$$

两项的 **信息论含义** 如下：

**压缩损失**（compression loss）：

$$
\mathcal{L}_t = I_{P_\rightarrow}\!\left(y_t;\, y_{t+1:T} \;\big|\; g_{t+1}^\leftarrow\right) \geq 0
$$

即将完整未来 $y_{t+1:T}$ 压缩为有限维隐状态 $g_{t+1}^\leftarrow$ 时，关于 $y_t$ 的 **残余互信息**——完整未来包含的关于 $y_t$ 的信息中、被有限容量隐状态丢弃的部分。这反映了后向模型有限记忆容量的代价：隐状态维度越低，压缩越激进，$\mathcal{L}_t$ 越大。

**模型失配**（model mismatch）：

$$
\mathcal{M}_t = \mathbb{E}_{g_{t+1}^\leftarrow}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | g_{t+1}^\leftarrow) \;\big\|\; p_t(y_t | g_{t+1}^\leftarrow)\right)\right] \geq 0
$$

即在 **相同条件** $g_{t+1}^\leftarrow$ 下，**真正的回顾分布** $P_\rightarrow(y_t | g_{t+1}^\leftarrow)$（由 Bayes 定理从前向联合分布导出）与 **直接复用的前向发射核** $p_t(y_t | g_{t+1}^\leftarrow)$（协议反转的代价）之间的差距。即使隐状态容量无限大（$\mathcal{L}_t = 0$），只要前向发射核不是回顾分布的正确参数化，$\mathcal{M}_t$ 仍然非零。

> **与变分推断的类比**：这一分解在形式上类似于 ELBO gap 分解（evidence lower bound），其中信息损失项和分布失配项分别出现。但起点完全不同：ELBO 分解来自似然下界，而本文的分解来自 **时间反演与熵产生**。

### 6.3 精炼第二定律（Refined Second Law）

结合压缩损失分解和互信息链式法则，得到熵产生的下界：

$$
\boxed{\mathcal{S}_y \geq \sum_{t=1}^{T}\left[I_{P_\rightarrow}\!\left(y_t;\, f_{t-1}^\rightarrow(y_{1:t-1})\right) - I_{P_\rightarrow}\!\left(y_t;\, g_{t+1}^\leftarrow(y_{T:t+1})\right)\right] \geq 0}
$$

**解读**：熵产生的下界由 **前向隐状态携带的预测信息** 与 **后向隐状态携带的回顾信息** 之间的差距决定。前向总结保留了关于 $y_t$ 的全部预测信息（因为它是充分统计量），而后向总结一般会丢失一些——这种不对称性正是不可逆性的来源之一。

---

## 7 核心结论与方法论意义

### 7.1 主要贡献总结

| 贡献 | 内容 |
|:---|:---|
| **统一框架** | 将 Transformer、RNN、Kalman、SSM、Mamba 纳入同一自回归生成模型类 |
| **熵产生定义** | 通过 Crooks 型时间反演定义非马尔可夫过程的 $\mathcal{S}_y$ |
| **计算可行性** | $O(T^2)$（Transformer）或 $O(T)$（递归模型）× $N$ 条轨迹，无指数代价 |
| **时间粗粒化** | 块级反转提取更有解释力的语义不可逆信号 |
| **GPT-2 验证** | 块级熵产生可区分因果 / 非因果文本 |
| **Kalman 解析解** | 创新反转矩阵 $\mathcal{R}$ 给出闭合表达式 |
| **回顾性分解** | $\mathcal{S}_y = \sum_t (\mathcal{L}_t + \mathcal{M}_t)$，精确分解为压缩损失与模型失配 |
| **精炼第二定律** | 熵产生 ≥ 前向/后向预测信息差 |

### 7.2 与扩散模型的关系

- 扩散模型（diffusion models）中的逆过程对应于 **贝叶斯回顾**（概率分布本身的时间反演），而非协议反转。
- 两者之间的差距恰好由熵产生衡量——这与本文的 $\mathcal{D}_t$ 分解中回顾分布 vs. 协议反转后向模型的差距完全一致。

### 7.3 重要的开放问题

1. **更大规模 LLM**：将框架应用于 GPT-4 等更大模型，但面临语义粗粒化的挑战（同一语义内容可由多种 token 序列表达）。
2. **有限时间权衡关系**：是否存在类似热力学不确定性关系（thermodynamic uncertainty relations）的速度-精度-不可逆性权衡？
3. **回顾性分解的估计**：$\mathcal{D}_t$、$\mathcal{L}_t$、$\mathcal{M}_t$ 的计算需要贝叶斯回顾分布 $P_\rightarrow(y_t | y_{t+1:T})$，目前不可直接从自回归模型获得，可能需要训练专门的逆向模型。
4. **因果推断**：区分真正的因果依赖、时间排序和话语结构惯例对熵产生的贡献。

---

## 8 个人评注

### 亮点
- **概念桥梁的优雅性**：将统计物理中熵产生的深刻概念与 AI 中最核心的 Transformer 架构连接起来，概念框架极其清晰。
- **"一石五鸟"的统一性**：Table 1 的五种架构对照令人赏心悦目，一个框架覆盖了从经典控制论到现代 LLM 的全部谱系。
- **可计算性的核心洞察**：确定性隐状态 + 显式发射核 = 可高效计算的非马尔可夫熵产生。这一观察本身就具有方法论价值。
- **块级粗粒化**：优雅地解决了 token 级反转的语法 artifact 问题，且保持了涨落定理的有效性。

### 局限
- GPT-2 实验仅为 proof-of-concept，序列长度 $T = 120$，模型规模有限。
- 因果/非因果文本由 LLM 生成，分类标准依赖于 prompt 而非形式化定义。
- 回顾性分解的各项（$\mathcal{L}_t$, $\mathcal{M}_t$）目前无法从模型直接计算。

### 可能的后续方向
- 对比不同训练阶段的 LLM 的熵产生变化，可能揭示训练过程中的不可逆性学习。
- 将粗粒化推广到语义级别（如使用句子嵌入而非 token 序列），构建"语义熵产生"。
- 探索熵产生与模型泛化能力、幻觉（hallucination）之间的关系。

---

## 附录：符号速查表

| 符号 | 含义 |
|:---|:---|
| $y_t$ | 观测变量（token 或测量值）|
| $h_t$ | 确定性隐状态（latent state）|
| $\Phi_t$ / $\phi_t$ | 确定性映射（一般/递归） |
| $p_t(y_{t+1} \| h_t)$ | 发射核（emission kernel）|
| $f_t^\rightarrow(y_{1:t})$ | 前向隐状态映射 |
| $g_{t+1}^\leftarrow(y_{T:t+1})$ | 后向隐状态映射 |
| $P_\rightarrow$, $P_\leftarrow$ | 前向/后向路径概率 |
| $\sigma(y_{1:T})$ | 随机熵产生（stochastic entropy production）|
| $\mathcal{S}_y$ | 熵产生（entropy production）= $\mathbb{E}[\sigma]$ |
| $\mathcal{D}_t$ | 逐步回顾性贡献 |
| $\mathcal{L}_t$ | 压缩损失（compression loss）|
| $\mathcal{M}_t$ | 模型失配（model mismatch）|
| $\mathcal{R}$ | 创新反转矩阵（innovation reversal matrix）|
| $S$ | 创新协方差（innovation covariance）|
| $K$ | Kalman 增益（Kalman gain）|
