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

于是对前向分布做平均时，分母会和前向路径概率本身相消：

$$
\mathbb E_{P_\rightarrow}\!\left[e^{-\sigma(y_{1:T})}\right]
=
\sum_{y_{1:T}}
P_\rightarrow(y_{1:T})
\frac{P_\leftarrow(y_{T:1})}{P_\rightarrow(y_{1:T})}.
$$

约掉之后就得到

$$
\mathbb E_{P_\rightarrow}\!\left[e^{-\sigma(y_{1:T})}\right]
=
\sum_{y_{1:T}} P_\leftarrow(y_{T:1}).
$$

最后这一步之所以等于 $1$，不是因为发生了新的动力学事实，而只是因为 $P_\leftarrow$ 本身就是一个已经归一化的后向路径概率分布；对所有可能的反向路径求和，结果必然是 $1$。  
这里最容易混淆的一点是：**非马尔可夫**并不意味着“不能给整条路径写概率”，也不意味着“不能把整条路径概率写成连乘”。  
真正成立的是：

- 对任意序列过程，只要联合分布存在，就总能用链式法则写成
  $$
  P(y_{1:T})
  =
  P(y_1)\prod_{t=1}^{T-1} P(y_{t+1}\mid y_{1:t}).
  $$
- 如果过程是马尔可夫的，上式才会进一步简化成
  $$
  P(y_{1:T})
  =
  P(y_1)\prod_{t=1}^{T-1} P(y_{t+1}\mid y_t).
  $$

所以，马尔可夫性决定的不是“能不能写路径概率”，而是**每一步条件概率到底依赖整个过去，还是只依赖当前一步**。

这篇文章里的自回归模型恰好就属于第一种情形。前向路径概率写成

$$
P_\rightarrow(y_{1:T})
=
\prod_{t=1}^{T} p_t\!\left(y_t \mid f_{t-1}^\rightarrow(y_{1:t-1})\right),
$$

不是因为过程是马尔可夫，而是因为模型本身已经把完整过去 $y_{1:t-1}$ 压缩进了内部表示 $f_{t-1}^\rightarrow$。  
同样，后向路径概率

$$
P_\leftarrow(y_{T:1})
=
\prod_{t=1}^{T} p_t\!\left(y_t \mid g_{t+1}^\leftarrow(y_{T:t+1})\right)
$$

也只是把“未来条件下的反向生成”写成同样的链式结构。

因此，这一步和前面 PRE 那篇里的积分涨落定理共享的是**路径测度之比**这一逻辑；不同之处只在于，那篇的路径对象是马尔可夫 SDE 轨迹，这篇的路径对象是由自回归模型定义、一般仍然保留长记忆的输出序列。

### 2.4 递归情形和马尔可夫极限：这套定义为什么和经典结果兼容

在递归情形下，后向隐状态还可以写成

$$
\tilde h_s = \tilde \phi_s(\tilde h_{s-1}, \tilde y_s), \tag{21}
$$

其中 $\tilde \phi_s = \phi_{T-s+1}$。这说明 backward process 在递归架构里同样能保持递推结构。

但作者紧接着强调：即使联合过程 $(h_t,y_t)$ 在前向是马尔可夫的，也不应该立刻把熵产生定义搬到这层联合状态上。问题不在于 “$(h_t,y_t)$ 不够大”，而在于 **前向和后向在 latent 层上未必共享同一个可实现集合**。

这件事要分三步看。

第一，前向联合过程里的状态更新是

$$
h_{t+1}=\phi_{t+1}(h_t,y_{t+1}),
$$

所以前向路径权重里会出现原文 Appendix A 的 delta 约束

$$
\delta\!\big(h_{t+1}-\phi_{t+1}(h_t,y_{t+1})\big). \tag{110}
$$

它的意思是：只有满足这个递归关系的联合路径 $(h_{1:T},y_{1:T})$ 才有正概率；不满足的路径概率直接就是零。

第二，如果把同一条联合路径机械地反过来写成

$$
(h_T,y_T),(h_{T-1},y_{T-1}),\dots,(h_1,y_1),
$$

后向核里出现的约束却是

$$
\delta\!\big(h_t-\phi_t(h_{t+1},y_t)\big). \tag{118}
$$

这和前向约束不是同一件事。这里需要把“delta 函数不可能同时为零”读成：**这两个 delta 约束对应的方程，一般不能被同一组变量同时满足。**

前向约束要求

$$
h_{t+1}=\phi_{t+1}(h_t,y_{t+1}),
$$

而后向约束要求

$$
h_t=\phi_t(h_{t+1},y_t).
$$

如果两者同时成立，就必须有

$$
h_t=\phi_t\!\big(\phi_{t+1}(h_t,y_{t+1}),\,y_t\big).
$$

也就是说，同一组 $(h_t,h_{t+1},y_t,y_{t+1})$ 不仅要满足原来的前向递推，还必须在“把 $h_{t+1}$ 再送回前一步更新器”之后，恰好回到原来的 $h_t$。这等于要求 $\phi_t$ 和 $\phi_{t+1}$ 在对应输入上形成一种非常特殊的局部可逆配对。

但一般的递归更新器并不是按这个目标设计的：

- 它本来只负责前向更新，而不是反向求逆；
- 前向式子里用的是 $(h_t,y_{t+1})$，后向式子里用的是 $(h_{t+1},y_t)$，输入本身就不同；
- 即使 $\phi_t$ 在形式上时间不变，它通常也是 many-to-one 的压缩映射，而不是可逆映射。

所以原文 Appendix A 才会说：一般情况下，(110) 和 (118) 里的 delta 约束不可能同时成立。换句话说，一条联合路径即使在前向中可实现，把它机械地反过来之后，也往往不是后向联合过程可实现的路径。

第三，这就导致前向和后向联合路径测度的支撑集可能不重合。这里“支撑集不重合”的具体意思是：

- 某些联合路径在前向下有正概率；
- 但在后向下对应概率严格等于零。

而 KL 散度

$$
D_{\mathrm{KL}}(P_\rightarrow\|P_\leftarrow)
=
\sum P_\rightarrow \ln\frac{P_\rightarrow}{P_\leftarrow}
$$

一旦出现 “$P_\rightarrow>0$ 但 $P_\leftarrow=0$” 的路径，分母就会变成零，对应项的对数发散到 $+\infty$。这就是原文说更高层熵产生 $\mathcal S_{\mathbf x}$ 可能发散的原因。

所以作者最后采取的策略不是在 latent 层硬做时间反演，而是退回到**观测序列 $y_{1:T}$** 上定义熵产生。原因很具体：在输出层，前向和后向路径概率都能直接由发射核写出来，而且在文中的典型例子里，这两者共享支撑集，于是 KL 散度保持有限，也更有可解释性。

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

1. **第一次评估前向路径概率。**  
   给定一条已经采样出来的序列 $y_{1:T}$，把它按正常顺序送进模型。模型在第 $t$ 步会先根据前缀 $y_{1:t-1}$ 算出内部表示，再给出
   $$
   p_t(y_t\mid f_{t-1}^\rightarrow(y_{1:t-1})).
   $$
   把所有时间步的对数概率加起来，就得到
   $$
   \ln P_\rightarrow(y_{1:T}).
   $$

2. **第二次评估后向路径概率。**  
   再把同一条序列倒过来，得到 $y_{T:1}$。用论文定义的 backward construction，把这条逆序列重新送进同一个模型；这时模型会根据“未来前缀”算出后向内部表示，再逐步给出
   $$
   p_t\!\left(y_t \mid g_{t+1}^\leftarrow(y_{T:t+1})\right).
   $$
   把这些对数概率加起来，就得到
   $$
   \ln P_\leftarrow(y_{T:1}).
   $$

3. **最后做一次相减。**  
   单条轨迹的随机熵产生就是
   $$
   \sigma(y_{1:T})
   =
   \ln P_\rightarrow(y_{1:T})-\ln P_\leftarrow(y_{T:1}).
   $$

所以这里真正做的不是“为了一条轨迹，再去枚举所有可能历史”，而是：**对同一条给定序列，各做一次普通的 log-likelihood evaluation，然后相减。**

论文把单条轨迹的计算代价写成

$$
C_1 = 2 C_{\mathrm{LL}}, \tag{27}
$$

其中 $C_{\mathrm{LL}}$ 是**把一整条长度为 $T$ 的序列送进模型，并得到这条序列总 log-likelihood 的代价**。  
前面的三步里，第 1 步要做一次这样的评估，第 2 步还要再做一次，所以单条轨迹总共就是两次：

$$
C_1 = C_{\mathrm{LL}}+C_{\mathrm{LL}}=2C_{\mathrm{LL}}.
$$

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

这条式子只是说：如果你想用 Monte Carlo 估计期望值，就需要先采样 $N$ 条轨迹；每条轨迹各自要花 $C_1$ 的代价，于是总成本自然是 $N$ 倍。

还剩最后一个问题：为什么非马尔可夫过程这里没有额外爆炸？

- **对 Transformer，** 一次 log-likelihood evaluation 大致是 $O(T^2)$。原因不是这篇热力学定义带来了额外开销，而是 Transformer 自身在处理长度为 $T$ 的序列时，attention 本来就要付出二次复杂度。

- **对 RNN、Kalman、SSM、Mamba 这类递归架构，** 一次 log-likelihood evaluation 大致是 $O(T)$。因为它们本来就是一步一步递推，每一步只更新一次有限维记忆状态，所以整条序列线性扫一遍就够了。

这里没有额外的“非马尔可夫惩罚项”，关键不是过程 magically 变简单了，而是：**复杂历史已经被模型自己的确定性记忆结构压缩进了内部状态表示。**  
如果你面对的是一个黑箱的非马尔可夫过程，确实要为长历史付出指数级代价；但这里面对的是一个已经训练好的自回归模型，它本身就提供了可直接调用的条件分布，所以熵产生的估计只是在复用模型已有的 likelihood 计算能力。

### 3.3 时间粗粒化：为什么 token 级反转不够好，block 级反转更有解释力

先看 token 级反转为什么不够好。  
如果把序列逐词完全倒过来，比如

$$
(\mathrm{This},\mathrm{is},\mathrm{a},\mathrm{book})
\longrightarrow
(\mathrm{book},\mathrm{a},\mathrm{is},\mathrm{This}),
$$

那么对语言模型来说，最先被破坏的是局部语法和短程搭配关系。于是 token 级熵产生主要测到的是：

- 冠词和名词顺序被打乱；
- 局部 n-gram 统计被打乱；
- 句法依赖被立刻破坏。

这些当然也是时间方向性，但它们太靠近词法和句法层面了。  
如果我们真正关心的是更高层的不可逆性，例如：

- 句子顺序能不能反过来讲；
- 事件链条反过来之后是否仍然合理；
- 因果叙事被反转后，文本的整体可解释性会下降多少；

那么逐 token 反转就太细了。它会在高层语义结构开始起作用之前，先被局部语法效应主导。

作者因此引入时间粗粒化：不再把 token 当作反转的基本单位，而是先把序列切成 block，再只反转 block 的顺序。  
要让这个定义工作起来，先要加一个条件：模型必须是时间齐次的，即

$$
p_t = p,\qquad \Phi_t = \Phi \quad \text{for all } t. \tag{28}
$$

这条条件的作用是：原始序列和 block-reversed 序列都可以交给**同一个**模型、按**同一套打分规则**来评估。  
这一点需要单独看清楚。

先看时间不齐次的情形。  
如果模型在第 $t$ 步使用的是专门属于该步的条件分布 $p_t$ 和状态更新器 $\Phi_t$，那么一条序列的对数概率实际上是在做下面这件事：

$$
\log P(y_{1:T})
=
\sum_{t=1}^{T}\log p_t\!\big(y_t \mid \Phi_{t-1}(y_{1:t-1})\big).
$$

这里每个时间步的参数都带着明确的“位置标签”：第一步用第一步的规则，第二步用第二步的规则，依此类推。  
一旦把序列按 block 重新排列，原来处在后面的片段会被挪到前面，原来处在前面的片段会被挪到后面。这样一来就会出现一个不自然的问题：  
**这段被搬到新位置的 block，到底应该继续用它原来所在时间步的参数，还是改用它现在所在位置的参数？**

这不是一个纯记号问题，而是比较对象本身变了。

- 如果继续用原来的参数，就等于保留了“原始时间标签”，那 block reversal 之后的对象已经不是一条普通序列概率；
- 如果改用新位置的参数，就等于连评分规则也一起换了，此时前向和后向比较混入了“时间步参数不同”这一额外效应。

无论选哪一种，最后得到的对数概率差都不再只反映“顺序被反转”本身。

时间齐次条件

$$
p_t = p,\qquad \Phi_t = \Phi
$$

正是用来排除这个歧义。  
在时间齐次模型里，每一步都调用同一个条件分布 $p$ 和同一个更新规则 $\Phi$。于是无论一个 block 处在序列的前面、中间还是后面，评估它时用的都是同一套机制。这样原始序列和 block-reversed 序列之间的差别，就只剩下**排列顺序变了**，而不会再混入“时间步专属参数被换掉”的额外影响。

接下来把长度为 $T$ 的原始序列切成长度为 $l$ 的 block。第 $t'$ 个 block 定义为

$$
y_{t'}' = (y_{(t'-1)l+1},\dots,y_{t'l}), \tag{30}
$$

于是整条序列

$$
y_{1:T}
$$

被改写成 block 序列

$$
y_{1:\tilde T}'=(y_1',y_2',\dots,y_{\tilde T}'),
\qquad \tilde T = T/l.
$$

这时 block reversal 的意思非常具体：  
**只把 block 的排列顺序反过来，而 block 内部的 token 顺序保持不变。**  
原文举的例子是

$$
(a,b,c,d,e,f)
\longrightarrow
(\underbrace{d,e,f}_{B_2},\underbrace{a,b,c}_{B_1}). \tag{32}
$$

这里应该把 token reversal 和 block reversal 分开看：

- token reversal：同时打乱 block 内部和 block 之间的顺序；
- block reversal：只打乱 block 之间的顺序；
- 因而 block 内部的局部语言统计仍然保持“正向自然语言”的形式。

如果一个 block 对应一句话、一个动作片段或一个 episode，那么反转后的对象更像是：

**高层事件顺序被反过来，但每个局部片段内部仍然是自然的。**

这正是作者想提取的不可逆性层次。

接下来要定义 block 级的“后向路径概率”。  
这里没有重新训练一个新的 backward model，也没有显式构造新的 block-level dynamics；作者做的事情更直接：

1. 先把原始序列做 block reversal；
2. 得到 block-reversed 序列 $\tilde y_{1:\tilde T}'$；
3. 再把这条序列当作普通输入，交给同一个 time-homogeneous model 去评估其概率。

于是粗粒化后的后向路径概率定义为

$$
P_\leftarrow'(y_{\tilde T:1}')
\equiv
P(\tilde y_{1:\tilde T}'). \tag{33}
$$

这条式子最重要的意思不是“符号怎么写”，而是：

**block 级反转仍然沿用同一个 forward model 来打分。**

因此单条序列的 block 级随机熵产生就是

$$
\sigma'(y_{1:T})
=
\ln P(y_{1:T})-\ln P(\tilde y_{1:\tilde T}'). \tag{34}
$$

也就是：

- 原始序列在模型下有多可能；
- block-reversed 序列在同一模型下有多可能；
- 两者相差多少。

如果这个差值很大，说明模型认为“高层顺序被反过来”之后，序列变得明显更不自然；这时 block 级不可逆性就强。

接下来还要说明：为什么这样定义之后，$\sigma'$ 仍然是一个真正的热力学量，而不是随手拍出来的分数？

关键在于 block-reversal 映射是双射。  
也就是说：

- 每一条原始序列都唯一对应一条 block-reversed 序列；
- 每一条 block-reversed 序列也都能唯一还原回原始序列。

正因为是一一对应，block-reversed 之后得到的 $P_\leftarrow'$ 仍然是一个合法归一化的概率分布，而不是一堆没有总和约束的分数。  
这样一来，平均熵产生就仍然可以写成

$$
\mathcal S_y'
=
\mathbb E_{P_\rightarrow}[\sigma']
=
D_{\mathrm{KL}}\!\left(P_\rightarrow(y_{1:T}) \,\|\, P_\leftarrow'(y_{\tilde T:1}')\right)\ge 0. \tag{35}
$$

这一步要按顺序理解：

1. $\sigma'$ 先定义成一条序列的对数概率比；
2. 对前向分布 $P_\rightarrow$ 做平均；
3. 因为反转映射是双射，右边确实对应一个正常的后向分布 $P_\leftarrow'$；
4. 所以平均值正好就是一个 KL 散度。

同样地，积分涨落定理也继续成立：

$$
\mathbb E_P[e^{-\sigma'(y_{1:T})}] = 1. \tag{36}
$$

原因和 token 级情形完全一样：  
$e^{-\sigma'}$ 正好把前向路径概率比变成 block-reversed 分布的概率密度，而后者对全部序列求和仍然归一化到 $1$。

最后再看计算代价。  
block 级定义并没有引入额外的组合爆炸，因为对一条给定序列，你仍然只做两次普通的 likelihood evaluation：

1. 一次评估原始序列 $y_{1:T}$；
2. 一次评估 block-reversed 序列 $\tilde y_{1:\tilde T}'$。

所以 block 级熵产生在计算上和 token 级熵产生完全同阶。  
改变的不是计算量级，也不是浮点运算次数（floating-point operations, FLOPs）的数量级；改变的是“时间反演的基本单位”：

- token 级时，反转单位是单个 token；
- block 级时，反转单位是句子、片段或 episode。

这就是为什么 block reversal 更有解释力。  
它把不可逆性的观测尺度从局部语法，抬高到了更接近语义、事件顺序和因果结构的层面。

---

## 4 GPT-2 概念验证实验

这一节要验证两件事。

第一，前面定义的熵产生

$$
\sigma(y_{1:T})
\quad \text{和} \quad
\sigma'(y_{1:T})
$$

在真实的大语言模型上是否真的可算，而不只是一个形式定义。  
第二，token 级反转和 block 级反转到底测到的是不是同一种东西；如果不是，block 级定义是否真的更接近句子顺序、事件顺序和因果叙事这一层的不可逆性。

### 4.1 Monte Carlo 采样实验（Section 5.1）

先看作者如何把前面的理论量真正落到 GPT-2 上。  
模型是预训练的 GPT-2（117M 参数），采样温度取

$$
\tau = 1.
$$

每条样本序列长度固定为

$$
T = 120
$$

个 token。作者不是调用库里封装好的 `model.generate()`，而是显式地按 autoregressive loop 一步一步采样。这样做的目的有两个：

1. 可以保证每一步都直接读取模型给出的原始 logits，不混入额外的 post-processing；
2. 采样和 log-likelihood evaluation 共用同一套 logits，因此路径概率的计算和理论定义完全一致。

前向路径概率里还包含初始项

$$
p(y_1\mid h_0).
$$

作者用 GPT-2 的特殊 token `<|endoftext|>` 作为初始 token。这样可以把“没有用户 prompt”的空白起点固定下来，并且保证原始序列和反转序列共用同一个初始隐状态。

接下来要区分 token 级和 block 级的具体计算对象。

- **token 级熵产生**：直接对完整长度 $T=120$ 的生成序列计算
  $$
  \sigma_{\mathrm{token}}/T.
  $$
- **block 级熵产生**：先把序列截断到最后一个句末标点位置，使得最后一个 token 真正落在句子边界上；记截断后长度为
  $$
  T' \le T.
  $$
  然后再按句子 block 做 reversal，计算
  $$
  \sigma_{\mathrm{block}}/T'.
  $$

这一步截断不是可有可无的。  
前面 `3.3` 里 block reversal 要求反转映射是双射；如果序列末尾停在半句中间，那么句子分块本身就不闭合，block reversal 的定义会变得不自然。  
因此：

- 含有句末标点的样本可以进入 block 级分析；
- 完全没有句末标点的样本保留给 token 级分析，但从 block 级分析里排除。

作者还专门加了一个参考分布，用来排除“是不是只是因为 block 级用了更短的截断序列，所以熵产生变小”这个疑问。  
做法是：在同一条截断后的长度 $T'$ 序列上，额外再算一次 token 级熵产生

$$
\sigma_{\mathrm{token}}(T')/T'.
$$

这样 Figure 3(a) 里就同时有：

- 完整长度 $T$ 的 token reversal；
- 截断长度 $T'$ 的 token reversal 参考分布。

![Figure 3(a): Token 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![Figure 3(b): Block 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-02.jpg)

Figure 3 要按两步读。

第一步，只看 panel (a)。  
这里的 token 级熵产生

$$
\sigma_{\mathrm{token}}/T
$$

显著大于零，样本均值大约是

$$
3.99.
$$

这说明：如果把 GPT-2 自己生成的 token 序列逐词反过来，路径概率会急剧下降。  
但这时还不能立刻说“GPT-2 学到了强烈的高层时间箭头”，因为逐词反转本来就会立刻破坏：

- 局部语法；
- 词序搭配；
- 短程句法依赖。

第二步，把 panel (a) 和 panel (b) 放在一起看。  
block 级熵产生

$$
\sigma_{\mathrm{block}}/T'
$$

的样本均值只有大约

$$
0.469,
$$

比 token 级低了一个数量级。  
更关键的是，panel (a) 中橙色参考分布

$$
\sigma_{\mathrm{token}}(T')/T'
$$

和完整 token 级分布的均值几乎一样。这说明 token 级和 block 级的巨大差别，主要不是因为 block 级用的是更短的截断序列，而是因为：

**反转的基本单位真的变了。**

也就是说，Figure 3 的核心结论不是单纯“block 级值更小”，而是：

1. token reversal 主要测到局部语法被破坏；
2. block reversal 把这个局部 artifact 大幅压低了；
3. 因而 block 级定义更有机会触及句子顺序、事件顺序和叙事结构这一层的不可逆性。

作者还说明了 Monte Carlo 收敛性：  
大约到

$$
N \simeq 500
$$

条样本时，两种定义下的熵产生估计都已经稳定到正值附近。  
在他们的具体实现里，满足 block-level bijection 条件的样本收集到 $500$ 条；token-level 分析因为不需要句末截断，因此保留了略多的样本，总数是 $516$ 条。

这一组实验的作用因此很明确：  
它首先证明了前面定义的熵产生在真实 LLM 上是可算的；同时也说明，如果直接用 token reversal，数值会被语法 artifact 主导，解释力不够。

### 4.2 因果 vs. 非因果文本实验（Section 5.2）

Figure 3 只说明了 token 级和 block 级的数值规模很不一样，但还没有回答更关键的问题：  
**block 级熵产生到底是不是更接近我们想要的“高层不可逆性”。**

作者于是设计了第二个实验。  
这次他们不再使用 GPT-2 自己采样出来的文本，而是准备两组外部文本，再把这些固定文本送进 GPT-2 计算路径概率。这样做的目的，是把“路径本身的语义结构”控制得更明确一些。

两组文本都由 Claude Opus 4.6 在固定 prompt 下自动生成，各有 30 条，每条由 4 句话组成：

- **因果文本**：四句话描述一个时间有序、前后相接的事件链。  
  例如“杯子滑落 → 落地 → 摔碎 → 被扫走”。  
  把句子顺序反过来之后，就会变成“结果在前、原因在后”的叙事。

- **非因果文本**：四句话只是并列的独立事实，顺序本身没有因果含义。  
  例如“某种乐器如何演奏、另一种乐器如何演奏……”。  
  把句子顺序反过来之后，整体语义变化不大。

这一步的关键思想是：

- 如果 block-level entropy production 真的在测句子顺序或事件顺序的不可逆性；
- 那么因果文本在 block reversal 之后，应该比非因果文本损失更多路径概率；
- 于是它的
  $$
  \sigma_{\mathrm{block}}
  $$
  应该更大。

![Figure 4(a): Token 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-01.jpg)

![Figure 4(b): Block 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-02.jpg)

Figure 4 也要分成两步读。

先看 panel (a)。  
token 级熵产生

$$
\sigma_{\mathrm{token}}/T
$$

对因果文本和非因果文本几乎没有区分力，统计检验给出的

$$
p = 0.78
$$

说明两组没有显著差异。  
这和 Figure 3 的结论一致：token 级量首先被语法破坏主导，所以即便文本的高层事件结构不同，token reversal 也很难把这种差别稳定地提取出来。

再看 panel (b)。  
block 级熵产生

$$
\sigma_{\mathrm{block}}/T
$$

在因果文本上显著高于非因果文本；作者报告的 Mann–Whitney 检验结果是

$$
U = 746,\qquad
p = 4.5\times 10^{-6},\qquad
r = 0.66.
$$

这一组结果要按下面这条逻辑来理解：

1. 对因果文本来说，句子顺序本身承载了“原因在前、结果在后”的结构；
2. 一旦把句子顺序反过来，后向路径概率就会显著降低；
3. 因此 block reversal 带来的对数概率差更大，$\sigma_{\mathrm{block}}$ 更高。

而对非因果文本来说：

1. 句子之间本来就是并列的；
2. 反转句子顺序并不会系统性地制造“效果先于原因”的冲突；
3. 因而 block reversal 对路径概率的打击更小。

所以 Figure 4 真正支持的是：

**block-level coarse-graining 的确比 token-level reversal 更接近句子级、事件级和叙事级的时间不可逆性。**

不过作者也明确收了边界，这一点不能省略。  
他们并没有声称“熵产生已经可以严格定量地测量 causal structure”，原因至少有三条：

1. 因果/非因果的分类是由 prompt 生成的，不是严格形式化定义出来的；
2. 这些文本本身也是由另一个大模型生成的，风格偏差可能会带进实验；
3. 这里的“因果”仍然混合了真正的因果依赖、单纯的时间顺序和叙事结构约定。

所以这组 GPT-2 实验更准确的地位应该分成两层来理解。

第一，它证明的不是“熵产生已经成为语言因果性的严格定量测度”。  
如果要做到这一点，至少需要满足三件事：

1. 先给出一个与 prompt 无关的、形式化的因果定义；
2. 再证明这个定义和实验里使用的文本类别严格对应；
3. 最后证明熵产生的大小可以稳定地区分“真正的因果依赖”和“单纯的时间顺序或叙事习惯”。

这篇文章并没有完成这三步，所以它还不能支持“语言中的因果性已经被定量测出来了”这种更强的结论。

第二，它确实完成了一个更有限、但也更扎实的证明。  
这组实验至少说明了两件事：

1. token-level entropy production 几乎完全被局部语法和词序破坏主导，因此即便文本在高层顺序结构上不同，它也很难稳定地区分出来；
2. block-level entropy production 一旦把反转单位提升到句子层面，就开始对高层顺序结构敏感了，因为它能够把因果文本和非因果文本显著地区分开。

所以这组实验为什么只能叫 proof-of-concept，现在就清楚了。  
它的结论不是“我们已经测量了语言中的因果性”，而是：

**一旦把 coarse-graining 的尺度从 token 提升到句子 block，熵产生这个量就开始脱离纯语法 artifact，转而对更高层的顺序结构作出响应。**

在这篇文章的语境里，这已经足够重要，因为它说明：

- token-level definition 太细，首先测到的是局部语法不可逆性；
- block-level definition 更接近作者真正想要的对象，也就是句子顺序、事件顺序和叙事级时间箭头。

---

## 5 Kalman 滤波解析案例

### 5.1 为什么 Kalman 会落进前面的通用框架

先从标准线性高斯状态空间模型开始：

$$
x_{t+1} = Ax_t + w_t, \quad y_t = Cx_t + v_t
$$

其中

$$
w_t \sim \mathcal{N}(0,Q),\qquad
v_t \sim \mathcal{N}(0,R).
$$

这组方程最容易让人先想到“真实隐藏状态” $x_t$。  
但这篇文章真正想分析的仍然不是 $x_t$ 的热力学，而是**观测序列**

$$
y_{1:T}.
$$

因此作者做了一个关键的重新解释：

- 真实状态 $x_t$ 只属于背景上的 signal process；
- 前面通用框架里的 latent state，不再取 $x_t$，而取 Kalman filter 的一步预测
  $$
  h_t=\hat x_{t+1\mid t};
  $$
- emission kernel 则对应“给定当前预测状态，下一步观测服从什么高斯分布”。

所以这一节不是在分析“真实物理系统的熵产生”，而是在说：

**Kalman filter 自身也可以被看成一个 autoregressive generative model。**

为了把式子做成解析形式，作者再加一个稳态假设：滤波器已经进入稳态。  
这里最好先把三个对象分清楚。

第一，先看一步预测误差。  
当滤波器根据过去观测给出预测

$$
\hat x_{t\mid t-1},
$$

它和真实状态 $x_t$ 之间会有误差

$$
x_t-\hat x_{t\mid t-1}.
$$

这个误差有多不确定，由它的协方差矩阵

$$
P
$$

来刻画。  
所以 $P$ 说的是：**在看到当前观测 $y_t$ 之前，滤波器对状态预测还剩多少不确定性。**

第二，再看创新

$$
e_t = y_t - C\hat x_{t\mid t-1}.
$$

它表示：当前真实观测 $y_t$ 和“根据旧预测本来应该看到的观测”

$$
C\hat x_{t\mid t-1}
$$

之间的差。  
如果这个差很大，说明当前观测里包含了很多预测之外的新信息。  
创新的协方差矩阵就是

$$
S = CPC^\top + R.
$$

所以 $S$ 说的是：**当前观测里那部分“出乎预测”的量，典型波动有多大。**  
它同时包含两部分来源：

- 预测状态本身还不够准，这会通过 $CPC^\top$ 传到观测空间；
- 观测通道自身还有噪声 $R$。

第三，Kalman 增益

$$
K = PC^\top S^{-1}
$$

是更新时用的权重矩阵。它回答的问题是：

**当前观测里的创新 $e_t$，应该有多大比例被拿来修正旧预测。**

因此更新式

$$
\hat x_{t\mid t} = \hat x_{t\mid t-1} + K e_t
$$

的意思就是：

- 先保留旧预测 $\hat x_{t\mid t-1}$；
- 再把创新 $e_t$ 乘上一个权重 $K$ 加进去；
- 得到吸收了当前观测信息的新估计 $\hat x_{t\mid t}$。

如果观测噪声很小、创新更可信，$K$ 会更大；  
如果观测噪声很大、当前观测不太可信，$K$ 会更小。

稳态假设的意思是：上面这三个矩阵

- 预测误差协方差 $P$
- 创新协方差 $S$
- Kalman 增益 $K$

都不再显式依赖时间。  
这一步只是在固定生成机制的参数，不是在假设整条有限长度观测路径已经时间可逆。

### 5.2 前向过程：为什么路径概率能写成创新的高斯乘积

把 Kalman generative mechanism 写成一步一步的循环，它其实和前面一般递归框架完全同构：

1. 先抽一个创新
   $$
   e_t\sim \mathcal N(0,S).
   $$
2. 再生成观测
   $$
   y_t = C\hat x_{t\mid t-1}+e_t. \tag{39}
   $$
3. 最后做一次 Kalman 更新和一步预测
   $$
   \hat x_{t\mid t} = \hat x_{t\mid t-1} + K\left(y_t - C\hat x_{t\mid t-1}\right), \tag{40}
   $$
   $$
   \hat x_{t+1\mid t} = A\hat x_{t\mid t}. \tag{41}
   $$

这三步里最关键的是创新

$$
e_t = y_t - C\hat x_{t\mid t-1}.
$$

这条式子最好直接读成：

- $C\hat x_{t\mid t-1}$ 是“按旧预测，本来应该看到什么”；
- $y_t$ 是“现在真的看到了什么”；
- 两者之差 $e_t$ 就是当前观测带来的新信息。

现在把过去观测

$$
y_{1:t-1}
$$

固定住。  
在这个条件下，前一步预测状态

$$
\hat x_{t\mid t-1}
$$

已经是一个确定量，不再随机。  
因此当前观测的不确定性只剩下一项：创新

$$
e_t\sim \mathcal N(0,S).
$$

而观测方程又写成

$$
y_t = C\hat x_{t\mid t-1}+e_t.
$$

这说明：给定过去之后，当前观测 $y_t$ 就等于“预测观测”

$$
C\hat x_{t\mid t-1}
$$

再加上一项零均值高斯扰动 $e_t$。  
于是 $y_t$ 的条件分布立刻变成

$$
y_t \mid y_{1:t-1} \sim \mathcal N(C\hat x_{t\mid t-1},S). \tag{42}
$$

这条式子里的两个部分要分开读：

- 均值
  $$
  C\hat x_{t\mid t-1}
  $$
  表示：在只看过去信息时，滤波器对当前观测的最佳预测；
- 协方差
  $$
  S
  $$
  表示：这个预测周围还剩多少典型波动。

接下来才能走到整条路径概率。这里先要把一个容易混的点说清楚：

- 原始观测序列 $y_{1:T}$ 本身一般不是独立的。因为当前观测会通过 Kalman 递推影响后面的预测，所以 $y_t$ 和 $y_{t+1},y_{t+2},\dots$ 通常带相关性。
- innovation representation 做的事情，不是把观测序列本身变成独立序列，而是把“每一步新带来的那部分意外信息”单独抽出来，记成 $e_t = y_t - C\hat x_{t\mid t-1}$。这个 $e_t$ 表示：当前真实观测减去基于过去信息做出的最佳线性预测之后，还剩下的那一部分新信息。
- 对线性高斯 Kalman 滤波来说，这串创新 $e_1,e_2,\dots,e_T$ 在前向测度下是彼此独立、同分布为零均值高斯的。于是整条观测序列虽然相关，却可以被看成是“递推结构 + 独立高斯创新”共同生成出来的：过去决定预测均值，当前这一步真正新加入的随机性则全部压缩在 $e_t$ 里。

所以整条路径概率不是直接把相关的 $y_t$ 写成独立乘积，而是先改写成独立创新的乘积：

1. 第 $1$ 步贡献一个因子 $\mathcal N(e_1;0,S)$；
2. 第 $2$ 步再贡献一个因子 $\mathcal N(e_2;0,S)$；
3. 一直乘到第 $T$ 步。

这里

$$
\mathcal N(e_t;0,S)
$$

的意思不是“随机生成了一个数字 $0$”，而是“把当前创新 $e_t$ 代入一个均值为 $0$、协方差为 $S$ 的高斯密度”。中间的 $0$ 表示：在前向 Kalman 创新表示里，创新本身是零均值的；后面的 $S$ 表示：这个零均值高斯的波动大小由创新协方差 $S$ 决定。

于是整条前向路径概率就写成

$$
P_\rightarrow(y_{1:T})
=
\prod_{t=1}^{T}\mathcal N(e_t;0,S). \tag{43}
$$

这条乘积式真正表达的是：

- $y_{1:T}$ 本身一般不是独立序列；
- 但在 innovation representation 下，它可以由一串彼此独立的高斯创新 $e_t$ 驱动出来；
- 所以前向路径概率不再需要显式保留整段历史，只要看创新即可。

接下来作者把这种“由创新驱动的因果生成”写成矩阵形式。  
把递推式迭代展开，可以得到

$$
y_t = \sum_{k=1}^{t} H_{t-k} e_k, \tag{45}
$$

其中

$$
H_0 \equiv I_{n_y},\qquad
H_l \equiv CA^lK \quad (l\ge 1). \tag{46}
$$

这说明当前观测 $y_t$ 不只看当前创新 $e_t$，还会积累更早创新通过系统动力学传播过来的影响。  
把所有时刻堆成向量后，就得到

$$
\mathbf y = \mathcal H \mathbf e, \tag{47}
$$

这里的 $\mathcal H$ 是块下三角矩阵。  
所以到这一步为止，前向过程已经被完全改写成：

**独立高斯创新 $\mathbf e$ 经过一个因果线性算子 $\mathcal H$，生成整条观测路径 $\mathbf y$。**

### 5.3 后向过程：创新反转矩阵是怎么来的

现在要定义后向路径概率。  
作者做的不是重新发明一个新的逆滤波器，而是沿用前面的统一协议：把观测序列反过来，再让同一个 Kalman generative mechanism 去生成它。

于是后向过程也由三步组成：

1. 抽后向创新
   $$
   \tilde e_s^B \sim \mathcal N(0,S);
   $$
2. 生成反向观测
   $$
   \tilde y_s = C\hat x_{s\mid s-1}^B + \tilde e_s^B; \tag{50}
   $$
3. 再做相同结构的 Kalman 更新和一步预测
   $$
   \hat x_{s\mid s}^B = \hat x_{s\mid s-1}^B + K(\tilde y_s - C\hat x_{s\mid s-1}^B), \tag{51}
   $$
   $$
   \hat x_{s+1\mid s}^B = A\hat x_{s\mid s}^B. \tag{52}
   $$

对特定的时间反转事件，

$$
\tilde y_s = y_{T-s+1}, \tag{55}
$$

作者引入时间反转置换矩阵

$$
J
$$

使得

$$
J\mathbf y = (y_T^\top,\dots,y_1^\top)^\top. \tag{56}
$$

现在前面已经知道

$$
\mathbf y = \mathcal H \mathbf e.
$$

那么反序列对应的创新自然就应该由

$$
\mathbf e^B \equiv \mathcal H^{-1}J\mathbf y \tag{59}
$$

给出。再把 $\mathbf y=\mathcal H\mathbf e$ 代进去，就得到

$$
\mathbf e^B = \mathcal R \mathbf e, \tag{60}
$$

其中

$$
\mathcal R \equiv \mathcal H^{-1}J\mathcal H. \tag{61}
$$

这就是 innovation reversal matrix。  
它的含义非常具体：

1. $\mathcal H$：把前向创新变成观测；
2. $J$：把整条观测路径反过来；
3. $\mathcal H^{-1}$：再把反序列观测解码成后向创新。

所以 $\mathcal R$ 不是一个神秘技巧，而是“前向创新 $\to$ 观测 $\to$ 反序列观测 $\to$ 后向创新”这条链条的压缩写法。

### 5.4 解析熵产生：为什么最后是一个高斯 KL

#### 5.4.1 先把四个协方差对象分清

这里最容易乱的是记号太多，所以先把四个协方差对象分开：

- $S$：单步创新 $e_t$ 的协方差。它是一步局部噪声的尺度，维度只有单个观测步那么大。
- $\Sigma$：整条前向观测路径 $\mathbf y=(y_1^\top,\dots,y_T^\top)^\top$ 的协方差。它描述的是整条路径在时间上如何一起波动。
- $\widetilde\Sigma$：时间反转后的整条路径协方差。它对应后向路径分布在反序列上的协方差。
- $\Sigma_s^B$：第 $s$ 个后向创新 $e_s^B$ 在前向测度下的协方差。它是把整条矩阵公式再拆回逐步局部形式时出现的对象。

#### 5.4.2 前向路径为什么是 $\mathcal N(0,\Sigma)$

第一步，先把前向整条路径看成一个高斯向量。前面已经得到

$$
\mathbf y=\mathcal H\mathbf e,
$$

其中 $\mathbf e=(e_1^\top,\dots,e_T^\top)^\top$ 由彼此独立的高斯创新堆起来，所以

$$
\mathbf e \sim \mathcal N\!\bigl(0, I_T\otimes S\bigr).
$$

线性变换 $\mathbf y=\mathcal H\mathbf e$ 立即推出 $\mathbf y$ 也是高斯向量，因此前向路径分布就是

$$
P_\rightarrow(\mathbf y)=\mathcal N(\mathbf y;0,\Sigma), \tag{44}
$$

其中整条路径协方差是

$$
\Sigma = \mathcal H (I_T\otimes S)\mathcal H^\top. \tag{49}
$$

这条式子里的三部分分别是：

- $I_T\otimes S$：先把每一步独立创新的协方差沿时间堆成块对角矩阵；
- $\mathcal H$：把创新传播成整条观测路径；
- $\mathcal H^\top$：把协方差也按同样的线性传播规则推到观测空间。

所以 $\Sigma$ 不是又一种“局部噪声”，而是整条前向路径的总协方差。

#### 5.4.3 反序路径为什么是 $\mathcal N(0,\widetilde\Sigma)$

第二步，把同一条路径反过来。时间反转矩阵 $J$ 只做一件事：把

$$
\mathbf y=(y_1^\top,\dots,y_T^\top)^\top
$$

重新排列成

$$
J\mathbf y=(y_T^\top,\dots,y_1^\top)^\top.
$$

如果原来的路径向量是零均值高斯，那么施加线性变换 $J$ 之后，仍然是零均值高斯；协方差则按标准规则变成

$$
P_\leftarrow(J\mathbf y)=\mathcal N(\mathbf y;0,\widetilde\Sigma), \tag{57}
$$

其中

$$
\widetilde\Sigma = J\Sigma J. \tag{58}
$$

这说明 $\widetilde\Sigma$ 不是新的局部噪声参数，而只是“把整条前向路径协方差按时间反序重新排列之后”的结果。

#### 5.4.4 高斯路径 KL 为什么能化成矩阵公式

第三步，熵产生于是变成两个零均值高斯路径分布之间的 KL 散度：

$$
\mathcal S_y = D_{\mathrm{KL}}(P_\rightarrow\|P_\leftarrow)
$$

代入零均值高斯的 KL 公式后，会出现三类项：

- 一个 trace 项，比较两条路径协方差的主尺度差异；
- 一个均值差项，这里因为两边都是零均值，所以直接消失；
- 一个行列式比项，比较两条高斯体积元大小。

这里再用两条特殊性质把公式收紧：

1. $J$ 是正交置换矩阵，所以 $J^{-1}=J^\top=J$，也不会改变行列式大小；因此 $\det\widetilde\Sigma=\det\Sigma$，行列式比项消失。
2. $\Sigma$ 本身可以分解成 $\mathcal H(I_T\otimes S)\mathcal H^\top$，再配合
   $$
   \mathcal R=\mathcal H^{-1}J\mathcal H
   $$
   就能把 trace 项改写回创新空间。

最后得到

$$
\mathcal S_y
=
\frac{1}{2}
\left[
\operatorname{tr}\!\left((I_T\otimes S^{-1})\,\mathcal R\,(I_T\otimes S)\,\mathcal R^\top\right)
-Tn_y
\right]. \tag{71}
$$

这条式子如果直接看，很容易只看到一串矩阵。更直的读法是：

1. 在前向测度下，整串创新
   $$
   \mathbf e=(e_1^\top,\dots,e_T^\top)^\top
   $$
   的协方差就是
   $$
   I_T\otimes S.
   $$
   这表示：一共有 $T$ 步，每一步的局部协方差都是 $S$，而不同时间步之间彼此独立，所以整条创新向量的协方差是块对角的。

2. 时间反转后，前向创新会被映成
   $$
   \mathbf e^B=\mathcal R\mathbf e.
   $$
   因而这串“后向创新在前向测度下真正呈现出来的协方差”就变成
   $$
   \mathcal R (I_T\otimes S)\mathcal R^\top.
   $$

3. backward model 自己假设的理想情形是什么？  
   还是一串彼此独立、每步协方差都等于 $S$ 的高斯创新。也就是说，它期待看到的基准协方差仍然是
   $$
   I_T\otimes S.
   $$

4. 所以前面的
   $$
   (I_T\otimes S^{-1})\,\mathcal R\,(I_T\otimes S)\,\mathcal R^\top
   $$
   可以理解成：先把真实后向创新协方差
   $$
   \mathcal R (I_T\otimes S)\mathcal R^\top
   $$
   用理想基准
   $$
   I_T\otimes S
   $$
   去做归一化比较。这里的 $I_T\otimes S^{-1}$ 扮演的就是“按理想单步噪声尺度做白化”的角色。

5. 再取 trace，就是把所有时间步、所有观测维度上的归一化方差偏离全部加总起来。  
   如果真实后向创新真的和理想 backward model 完全一致，那么
   $$
   \mathcal R (I_T\otimes S)\mathcal R^\top = I_T\otimes S,
   $$
   于是 trace 项就正好等于总维度
   $$
   Tn_y.
   $$
   这也就是为什么后面要减去 $Tn_y$：它是在减掉“完全匹配时本来就该有的基线”。

所以 `(71)` 真正测的不是一个抽象矩阵距离，而是：**时间反转之后，真实后向创新的总体方差结构，相对于 backward model 假设的 i.i.d. 高斯基准，多出了多少归一化偏离。**

#### 5.4.5 再把整条路径公式拆回逐步局部形式

第四步，再把这条矩阵式读回物理含义。前向测度下，原始创新 $\mathbf e$ 是独立同分布高斯；但经过 $\mathcal R$ 变换后得到的后向创新

$$
\mathbf e^B=\mathcal R\mathbf e
$$

一般不再服从 backward model 假设的那组 i.i.d. 高斯统计。于是熵产生的来源就可以被读成：**前向真实路径经过时间反转后，在创新空间里看起来不再像一串独立同分布的高斯输入。**

作者随后把它写成逐步求和的形式。这里引入的

$$
\Sigma_s^B
$$

不再是整条路径协方差，而是“第 $s$ 个后向创新在前向测度下的局部协方差”：

$$
\Sigma_s^B
=
\mathbb E_{P_\rightarrow}\!\left[e_s^B(e_s^B)^\top\right], \tag{72}
$$

有了它之后，整条路径的总熵产生就能拆成逐步求和：

$$
\mathcal S_y
=
\frac{1}{2}\sum_{s=1}^{T}
\left[
\operatorname{tr}(S^{-1}\Sigma_s^B)-n_y
\right]. \tag{73}
$$

这说明整条路径的不可逆性，其实可以理解为每一个后向创新 $e_s^B$ 偏离标准高斯尺度 $S$ 的程度，再把这些局部偏离沿时间加总起来。

再利用高斯二次型的标准恒等式

$$
\mathbb E_{P_\rightarrow}\!\left[(e_s^B)^\top S^{-1} e_s^B\right]
=
\operatorname{tr}(S^{-1}\Sigma_s^B), \tag{74}
$$

还可以改写成

$$
\mathcal S_y
=
\frac{1}{2}\sum_{s=1}^{T}
\left(
\mathbb E_{P_\rightarrow}\!\left[(e_s^B)^\top S^{-1} e_s^B\right]
-n_y
\right). \tag{75}
$$

这时它的物理意义就完全落到单步上了：

- 如果后向创新在前向测度下仍然像理想的 $\mathcal N(0,S)$ 一样；
- 那么每一步都会恰好给出 $n_y$，总熵产生就消失；
- 只要后向创新的真实统计偏离了 backward model 假设的高斯结构，$\mathcal S_y$ 就会变正。

所以 Kalman 案例里的时间不可逆性，本质上就是：

**前向观测路径反过来以后，再从中抽出来的后向创新，不再像 backward model 假设的那样是独立同分布高斯。**

### 5.5 标量与多变量：Figure 5 在证明什么

有了解析公式之后，Figure 5 的作用就很清楚了：它不是额外给一个新现象，而是在验证前面整个解析链条。

- **标量情形**：熵产生随着 $T$ 增大趋于饱和；
- **多变量情形**：熵产生近似随 $T$ 线性增长。

这两种行为对应的是两种不同的时间反演结构：

- 标量平稳高斯过程没有真正持续的不可逆流，所以有限熵产生主要来自边界效应；
- 多变量过程可以有真正的旋转型或交叉耦合型不可逆结构，因此时间一拉长，熵产生会持续累积。

![Figure 5(a): 标量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-01.jpg)

![Figure 5(b): 多变量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-02.jpg)

Figure 5 的数值实验做的事情很直接：

1. 用前向过程采样很多条观测轨迹；
2. 按前面的一般 Monte Carlo 定义估计熵产生；
3. 再把估计值和解析公式逐点比较。

结果是：在

$$
T = 5,10,\dots,50
$$

的整个范围内，蓝色 Monte Carlo 点和黑色解析曲线都高度吻合。  
这说明 Kalman 这一节不是“另一个例子”，而是把整篇文章的理论闭环真正搭起来了：

- 一般定义给出 Monte Carlo estimator；
- 线性高斯结构给出解析公式；
- 两者数值上一致，说明前面的路径概率和熵产生定义是自洽的。

---

## 6 熵产生的回顾性分解（Retrospective Decomposition）

这一节真正要回答的是：总熵产生

$$
\mathcal S_y
$$

能不能再拆开，看清楚“不可逆性到底是在每一步哪里产生的”。原文的回答分成三层：

1. 先把总熵产生拆成逐步非负项；
2. 再把每一步拆成“压缩损失”和“模型失配”；
3. 最后再把压缩损失沿时间求和，得到一个精炼第二定律。

### 6.1 逐步分解

第一步，先把前向路径概率改写成“从未来回看现在”的形式。  
普通自回归写法是按过去展开：

$$
P_\rightarrow(y_{1:T})=\prod_{t=1}^{T}P_\rightarrow(y_t\mid y_{1:t-1}).
$$

这里原文改做另一种分解：把整条路径按“当前 $y_t$ + 剩余未来 $y_{t+1:T}$”不断剥离。由 Bayes 链式法则，

$$
P_\rightarrow(y_{t:T})=P_\rightarrow(y_t\mid y_{t+1:T})\,P_\rightarrow(y_{t+1:T}). \tag{83}
$$

把这一步从 $t=1$ 一直递推到 $t=T$，就得到

$$
P_\rightarrow(y_{1:T})=\prod_{t=1}^{T}P_\rightarrow(y_t\mid y_{t+1:T}). \tag{84}
$$

这一步很关键，因为从这里开始，前向路径也被写成了“逐步回顾分布”的乘积。

第二步，再看后向路径。按照前面定义的协议反转 backward process，后向路径本来就是逐步生成的，所以

$$
P_\leftarrow(y_{T:1})
=
\prod_{t=1}^{T}
p_t\!\left(y_t \mid g_{t+1}^\leftarrow(y_{T:t+1})\right). \tag{85}
$$

这里的

$$
g_{t+1}^\leftarrow(y_{T:t+1})
$$

是把未来片段 $y_{t+1:T}$ 压缩成的后向隐状态摘要。

第三步，把这两种分解代回总熵产生定义

$$
\mathcal S_y
=
\mathbb E_{P_\rightarrow}
\left[
\ln\frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})}
\right].
$$

由于前向和后向都已经写成了按时间的乘积，取对数之后自然变成逐项求和：

$$
\mathcal S_y
=
\mathbb E_{P_\rightarrow}
\left[
\sum_{t=1}^{T}
\ln\frac{
P_\rightarrow(y_t\mid y_{t+1:T})
}{
p_t\!\left(y_t\mid g_{t+1}^\leftarrow(y_{T:t+1})\right)
}
\right]. \tag{86}
$$

第四步，把外层期望按每个时间步收进去，并定义第 $t$ 步的贡献：

$$
\mathcal S_y=\sum_{t=1}^{T}\mathcal D_t, \tag{87}
$$

其中

$$
\mathcal D_t
=
\mathbb E_{y_{t+1:T}\sim P_\rightarrow}
\left[
D_{\mathrm{KL}}
\left(
P_\rightarrow(y_t\mid y_{t+1:T})
\;\big\|\;
p_t(y_t\mid g_{t+1}^\leftarrow(y_{T:t+1}))
\right)
\right]\ge 0. \tag{88}
$$

所以 $\mathcal D_t$ 的含义可以压成一句话：

**给定未来 $y_{t+1:T}$ 时，真正的贝叶斯回顾分布**

$$
P_\rightarrow(y_t\mid y_{t+1:T})
$$

**和协议反转后向模型实际使用的条件分布**

$$
p_t(y_t\mid g_{t+1}^\leftarrow)
$$

**之间的差距。**

### 6.2 压缩损失 + 模型失配

现在再问：单步不可逆性 $\mathcal D_t$ 到底是由什么造成的？  

从 `(88)` 看，单步不可逆性里本来在比较的两个端点分布是：

- 真正的完整回顾分布
  $$
  P_\rightarrow(y_t\mid y_{t+1:T}),
  $$
  它把完整未来
  $$
  y_{t+1:T}
  $$
  全都保留下来；
- backward model 实际使用的条件分布
  $$
  p_t(y_t\mid g_{t+1}^\leftarrow),
  $$
  它只依赖一个压缩后的后向摘要
  $$
  g_{t+1}^\leftarrow.
  $$

这两个分布之间一下子差得太多：前者看的是完整未来，后者看的是压缩摘要，而且还直接复用了 forward emission kernel。  
所以原文先插入一个最自然的中间层：

$$
P_\rightarrow(y_t\mid g_{t+1}^\leftarrow),
$$

它为什么自然？因为它只做了“压缩”这一件事：

- 先把完整未来
  $$
  y_{t+1:T}
  $$
  压缩成后向摘要
  $$
  g_{t+1}^\leftarrow;
  $$
- 但压缩之后，对 $y_t$ 的分布仍然使用真正的前向联合分布来定义，也就是仍然是一个贝叶斯回顾分布，而不是直接替换成模型发射核。

所以

$$
P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)
$$

正好把原来的大差距拆成两段：

1. 先比较“完整未来”与“压缩未来”，看压缩本身丢了多少信息；
2. 再比较“压缩后的真正回顾分布”和“模型实际使用的发射核”，看模型参数化又差了多少。

于是对数比可以精确拆成两段：

$$
\ln \frac{P_\rightarrow(y_t\mid y_{t+1:T})}{p_t(y_t\mid g_{t+1}^\leftarrow)}
=
\underbrace{
\ln \frac{P_\rightarrow(y_t\mid y_{t+1:T})}{P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)}
}_{\text{压缩损失}}
+
\underbrace{
\ln \frac{P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)}{p_t(y_t\mid g_{t+1}^\leftarrow)}
}_{\text{模型失配}}. \tag{91}
$$

先看第一项。它比较的是：

- 完整未来都保留下来时的回顾分布；
- 只保留压缩摘要 $g_{t+1}^\leftarrow$ 时的回顾分布。

所以它测的是：**从完整未来压缩到有限维摘要时，关于 $y_t$ 的信息到底丢了多少。**

现在把第一项真正算出来。先固定一个具体的未来片段

$$
y_{t+1:T}.
$$

在这个固定条件下，第一项的对数比

$$
\ln \frac{P_\rightarrow(y_t\mid y_{t+1:T})}{P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)}
$$

如果先对

$$
y_t \sim P_\rightarrow(y_t\mid y_{t+1:T})
$$

取条件期望，就正好变成一个条件 KL：

$$
\mathbb E_{y_t\sim P_\rightarrow(\,\cdot\,\mid y_{t+1:T})}
\left[
\ln \frac{P_\rightarrow(y_t\mid y_{t+1:T})}{P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)}
\right]
=
D_{\mathrm{KL}}
\left(
P_\rightarrow(y_t\mid y_{t+1:T})
\;\big\|\;
P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)
\right).
$$

这一步没有新技巧，只是把 “对数比在前一个分布下取期望” 认成了 KL 的定义。

然后再对未来片段本身做外层平均，就得到

$$
\mathcal L_t
=
\mathbb E_{y_{t+1:T}\sim P_\rightarrow}
\left[
D_{\mathrm{KL}}
\left(
P_\rightarrow(y_t\mid y_{t+1:T})
\;\big\|\;
P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)
\right)
\right]
=
I_{P_\rightarrow}(y_t;\,y_{t+1:T}\mid g_{t+1}^\leftarrow)\ge 0. \tag{92}
$$

为什么最后会等于条件互信息？关键就在于

$$
g_{t+1}^\leftarrow = g_{t+1}^\leftarrow(y_{T:t+1})
$$

本身就是未来片段

$$
y_{t+1:T}
$$

的确定性函数。于是上面的外层平均正好符合条件互信息的标准形式：

$$
I(X;Y\mid Z)
=
\mathbb E_{Y,Z}
\left[
D_{\mathrm{KL}}(P(X\mid Y,Z)\|P(X\mid Z))
\right].
$$

这里把三个抽象变量对应成：

- $X \leftrightarrow y_t$；
- $Y \leftrightarrow y_{t+1:T}$；
- $Z \leftrightarrow g_{t+1}^\leftarrow$。

而因为 $Z$ 已经是 $Y$ 的确定性函数，所以

$$
P_\rightarrow(y_t\mid y_{t+1:T},g_{t+1}^\leftarrow)
=
P_\rightarrow(y_t\mid y_{t+1:T}),
$$

于是 `(92)` 里的那一项就正好是条件互信息。

再看第二项。它比较的是：

- 同样在摘要 $g_{t+1}^\leftarrow$ 这个条件下，
- 真正的压缩后验 $P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)$，
- 和 backward model 实际拿来生成的发射核 $p_t(y_t\mid g_{t+1}^\leftarrow)$。

这一步也可以按两层期望来读。先固定一个具体的未来片段 $y_{t+1:T}$。在这个固定条件下，第二项的对数比是

$$
\ln \frac{P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)}{p_t(y_t\mid g_{t+1}^\leftarrow)}.
$$

注意它和前一项不一样：这里的对数比已经不再显式依赖完整未来 $y_{t+1:T}$，而只通过压缩后的摘要

$$
g_{t+1}^\leftarrow=g_{t+1}^\leftarrow(y_{T:t+1})
$$

来依赖未来。

于是先对

$$
y_t \sim P_\rightarrow(y_t\mid y_{t+1:T})
$$

取条件期望时，虽然外层条件还是完整未来，但被积函数只通过 $g_{t+1}^\leftarrow$ 依赖这个未来片段，所以这一步其实已经只是在计算“给定摘要时”的 KL。再对完整未来做外层平均时，完整未来中真正起作用的部分都已经被压进了 $g_{t+1}^\leftarrow$；因此外层平均就可以边缘化成对摘要变量本身的平均。

换句话说，这里发生的不是神秘塌缩，而是一个很普通的事实：如果某个量只依赖随机变量 $Y$ 的确定性函数 $g(Y)$，那么对 $Y$ 的平均就等价于对 $g(Y)$ 的平均。

于是就得到

$$
\mathcal M_t
=
\mathbb E_{g_{t+1}^\leftarrow\sim P_\rightarrow}
\left[
D_{\mathrm{KL}}
\left(
P_\rightarrow(y_t\mid g_{t+1}^\leftarrow)
\;\big\|\;
p_t(y_t\mid g_{t+1}^\leftarrow)
\right)
\right]\ge 0. \tag{94}
$$

于是单步不可逆性被精确拆成两部分：

$$
\mathcal D_t=\mathcal L_t+\mathcal M_t. \tag{95}
$$

这两项的含义可以直接读成：

- $\mathcal L_t$：压缩未来时丢掉了多少关于当前 $y_t$ 的回顾信息；
- $\mathcal M_t$：即使给定同一个压缩摘要，backward model 的发射核又和真正的压缩后验差了多少。

### 6.3 精炼第二定律（Refined Second Law）

接下来作者进一步问：把所有时间步的压缩损失加起来，能不能写成一个更结构化的总下界？

第一步，从

$$
\mathcal L_t=I_{P_\rightarrow}(y_t;\,y_{t+1:T}\mid g_{t+1}^\leftarrow)
$$

出发。因为 $g_{t+1}^\leftarrow$ 是未来 $y_{t+1:T}$ 的确定性函数，互信息链式法则给出

$$
\mathcal L_t
=
I_{P_\rightarrow}(y_t;\,y_{t+1:T})
-
I_{P_\rightarrow}(y_t;\,g_{t+1}^\leftarrow). \tag{96}
$$

这条式子很直白：压缩损失等于“完整未来本来能告诉你多少”减去“压缩摘要实际还保留了多少”。

第二步，再把第一项换成前向预测信息。前向模型的隐藏摘要

$$
f_{t-1}^\rightarrow(y_{1:t-1})
$$

是按构造定义出来的充分预测摘要，所以

$$
I_{P_\rightarrow}(y_t;\,y_{1:t-1})
=
I_{P_\rightarrow}(y_t;\,f_{t-1}^\rightarrow(y_{1:t-1})). \tag{97}
$$

第三步，把“完整过去”和“完整未来”沿时间求和。这里原文用到的是同一条序列熵的两种链式分解。

先按前向顺序展开，总熵可以写成

$$
H_{P_\rightarrow}(y_{1:T})
=
\sum_{t=1}^{T} H_{P_\rightarrow}(y_t\mid y_{1:t-1}). \tag{98a}
$$

再按反向顺序展开，同一个总熵也可以写成

$$
H_{P_\rightarrow}(y_{1:T})
=
\sum_{t=1}^{T} H_{P_\rightarrow}(y_t\mid y_{t+1:T}). \tag{98b}
$$

把两边相等这件事记住以后，再看互信息。对每一个时间步，

$$
I_{P_\rightarrow}(y_t;\,y_{1:t-1})
=
H_{P_\rightarrow}(y_t)-H_{P_\rightarrow}(y_t\mid y_{1:t-1}),
$$

而

$$
I_{P_\rightarrow}(y_t;\,y_{t+1:T})
=
H_{P_\rightarrow}(y_t)-H_{P_\rightarrow}(y_t\mid y_{t+1:T}).
$$

现在把这两条式子分别从 $t=1$ 累加到 $T$。两边都会出现同样的项

$$
\sum_{t=1}^{T} H_{P_\rightarrow}(y_t),
$$

所以真正决定差别的，只剩条件熵和。又因为 `(98a)` 和 `(98b)` 说明这两组条件熵和本来就相等，于是它们相减后正好抵消，得到

$$
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,y_{1:t-1})
=
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,y_{t+1:T}). \tag{99}
$$

现在把这些式子真正串起来。先对 `(96)` 从 $t=1$ 到 $T$ 求和：

$$
\sum_{t=1}^{T}\mathcal L_t
=
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,y_{t+1:T})
-
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,g_{t+1}^\leftarrow). 
$$

接下来用 `(99)` 把第一项换成“完整过去”版本：

$$
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,y_{t+1:T})
=
\sum_{t=1}^{T} I_{P_\rightarrow}(y_t;\,y_{1:t-1}).
$$

再用 `(97)` 把这里的完整过去进一步换成前向摘要：

$$
I_{P_\rightarrow}(y_t;\,y_{1:t-1})
=
I_{P_\rightarrow}(y_t;\,f_{t-1}^\rightarrow(y_{1:t-1})).
$$

这样逐项代回去，才得到所有压缩损失的总和：

$$
\sum_{t=1}^{T}\mathcal L_t
=
\sum_{t=1}^{T}
\left[
I_{P_\rightarrow}\!\left(y_t;\,f_{t-1}^\rightarrow(y_{1:t-1})\right)
-
I_{P_\rightarrow}\!\left(y_t;\,g_{t+1}^\leftarrow(y_{T:t+1})\right)
\right]. \tag{100}
$$

第四步，再利用

$$
\mathcal S_y=\sum_{t=1}^{T}(\mathcal L_t+\mathcal M_t)
$$

且每个 $\mathcal M_t\ge 0$，就得到熵产生下界：

$$
\mathcal S_y
\ge
\sum_{t=1}^{T}
\left[
I_{P_\rightarrow}\!\left(y_t;\,f_{t-1}^\rightarrow(y_{1:t-1})\right)
-
I_{P_\rightarrow}\!\left(y_t;\,g_{t+1}^\leftarrow(y_{T:t+1})\right)
\right]
\ge 0. \tag{101}
$$

这条不等式的意思是：

- 前向摘要 $f_{t-1}^\rightarrow$ 保留的是“过去对当前的预测信息”；
- 后向摘要 $g_{t+1}^\leftarrow$ 保留的是“未来对当前的回顾信息”；
- 如果两边保留的信息量不对称，就会留下不可逆性的下界。

### 6.4 为什么这些分解项目前还难以直接估计

总熵产生

$$
\mathcal S_y
$$

前面已经可以用 Monte Carlo 直接估计；但这里新出现的

$$
\mathcal D_t,\quad \mathcal L_t,\quad \mathcal M_t
$$

并不能直接从模型前向采样里读出来。

难点卡在真正的回顾分布

$$
P_\rightarrow(y_t\mid y_{t+1:T}).
$$

这一步需要先分清：我们现在想求的，不是通常的前向条件分布

$$
P_\rightarrow(y_{t+1}\mid y_{1:t}),
$$

而是反过来的回顾分布：

$$
P_\rightarrow(y_t\mid y_{t+1:T}).
$$

它问的是：**如果未来片段 $y_{t+1:T}$ 已经给定，那么当前这一步 $y_t$ 的后验分布是什么。**

要得到这个量，最直接的方法就是从前向联合分布出发再用条件概率定义：

$$
P_\rightarrow(y_t\mid y_{t+1:T})
=
\frac{P_\rightarrow(y_t,y_{t+1:T})}
{P_\rightarrow(y_{t+1:T})}.
$$

接下来，分子和分母都不是模型直接给出的对象，所以还要再往下展开。

- 分子
  $$
  P_\rightarrow(y_t,y_{t+1:T})
  $$
  表示“当前这一步和全部未来一起出现”的概率。为了得到它，必须把更早的过去
  $$
  y_{1:t-1}
  $$
  全部边缘化掉：

  $$
  P_\rightarrow(y_t,y_{t+1:T})
  =
  \sum_{y_1,\dots,y_{t-1}}P_\rightarrow(y_{1:T}).
  $$

- 分母
  $$
  P_\rightarrow(y_{t+1:T})
  $$
  表示“未来片段本身出现”的概率。为了得到它，必须连当前这一步
  $$
  y_t
  $$
  也一起边缘化掉：

  $$
  P_\rightarrow(y_{t+1:T})
  =
  \sum_{y_1,\dots,y_t}P_\rightarrow(y_{1:T}).
  $$

把这两步代回去，才得到

$$
P_\rightarrow(y_t\mid y_{t+1:T})
=
\frac{\sum_{y_1,\dots,y_{t-1}}P_\rightarrow(y_{1:T})}
{\sum_{y_1,\dots,y_t}P_\rightarrow(y_{1:T})}. \tag{103}
$$

这条式子表面只是一个条件概率公式，但真正的难点就在于：分子和分母都要对整段过去做求和，所以你不能只看某一个时间步的本地发射核。

虽然每一步前向发射核

$$
p_t(y_{t+1}\mid h_t)
$$

是模型显式给出的，但它只回答：

$$
\text{给定当前隐藏摘要 } h_t,\ \text{下一步 } y_{t+1}\ \text{怎么分布。}
$$

而现在 `(103)` 要求的是另一件事：

$$
\text{给定未来 } y_{t+1:T},\ \text{当前 } y_t\ \text{怎么分布。}
$$

为了算这个量，你必须把整条前向联合分布

$$
P_\rightarrow(y_{1:T})
$$

拿出来，再把所有可能的过去路径都加总进去。问题就在于：这些过去路径不是彼此独立的，因为每一步的隐藏状态都要通过递推映射 $\Phi_t$ 从前面一步传下来。于是，一旦你开始对过去求和，所有时间步就会重新通过

$$
h_{t+1}=\Phi_t(h_t,y_{t+1})
$$

这条递推链耦合在一起。

所以作者这里真正想强调的是：

- 前向模型直接提供的是局部条件核 $p_t(y_{t+1}\mid h_t)$；
- 但回顾分布 $P_\rightarrow(y_t\mid y_{t+1:T})$ 不是某个局部模块直接吐出来的；
- 它需要对整条前向路径做边缘化，因此在一般情况下并不直接可得。

所以作者最后的判断是：

- 总熵产生 $\mathcal S_y$：可直接 Monte Carlo 估计；
- 逐步分解项 $\mathcal D_t,\mathcal L_t,\mathcal M_t$：目前还不直接可得；
- 一个自然方向，是额外训练一个反向自回归近似器，去学习
  $$
  P_\rightarrow(y_t\mid y_{t+1:T}).
  $$

---

## 7 Summary and perspectives

### 7.1 这篇文章到底完成了什么

最后一节先回到一个总问题：对于带确定性内部记忆的自回归生成模型，能不能像在随机热力学里那样，定义一条真正可算的不可逆性量，并把它放进统一框架里？

作者给出的回答是肯定的。前面整篇文章完成的事情，可以按一条线重新收成下面几步。

第一步，先把一大类看起来差异很大的模型放进同一个自回归框架里。Transformer、RNN、Kalman、一般状态空间模型和 Mamba，都被写成：

- 一个确定性内部记忆更新；
- 一个显式的发射核；
- 一个由这两部分共同定义出来的观测序列生成过程。

这样后面讨论的对象就不是某个单独架构，而是一整个“带确定性内存的非马尔可夫生成过程”类。

第二步，在这个统一框架里定义观测序列层面的熵产生

$$
\mathcal S_y
=
D_{\mathrm{KL}}\!\big(P_\rightarrow(y_{1:T})\,\|\,P_\leftarrow(y_{T:1})\big).
$$

这里的前向和后向不是在 latent 层硬做时间反转，而是直接在可见输出序列上比较 forward / backward path measures。这样做的关键好处是：即使内部 latent 更新在时间反演下不兼容，观测序列层面的不可逆性仍然可以定义。

第三步，说明这个量是可算的，而且代价没有因为 non-Markov 性而爆炸。对一条采样轨迹，只需要：

1. 算一次前向整序列 log-likelihood；
2. 再对同一条序列的反序列算一次后向 log-likelihood；
3. 做差得到随机熵产生；
4. 对很多条轨迹做 Monte Carlo 平均。

所以 Transformer 的成本仍然是一次 ordinary likelihood evaluation 的量级，即大致 $O(T^2)$；递归模型仍然是大致 $O(T)$。这里真正需要说明的是：如果我们面对的是一个抽象的 non-Markov 过程，而手里又没有任何内部记忆变量，那么要计算

$$
P(y_{t+1}\mid y_{1:t})
$$

这样的条件概率，往往就必须显式处理整段历史 $y_{1:t}$，计算代价很容易随着历史长度迅速膨胀。

但这篇文章讨论的不是这种“只有外部序列、没有内部结构”的 black-box non-Markov 过程。这里的模型本身已经把长历史压进了确定性内部记忆里：

- 对 Transformer，是前缀经过网络后形成的内部表示；
- 对递归模型，是一步一步更新的隐藏状态 $h_t$；
- 对 Kalman、SSM、Mamba，也都有各自的确定性状态递推。

所以计算某一步发射概率时，模型并不是重新枚举全部过去，而是先把历史压缩成当前摘要，再在这个摘要条件下给出下一步分布。也就是说，non-Markov 性并没有消失；真正发生的是：**长历史依赖已经被吸收到模型自己的确定性记忆结构里，因此 likelihood evaluation 的成本仍然由模型原本的一次前向计算决定，而不会额外出现组合爆炸。**

第四步，把 token 级反转推广到 block 级反转。这样改动的不是计算量级，而是时间反演的基本单位。作者想说明：如果直接反转 token 顺序，测到的不可逆性很容易被语法 artifact 主导；把基本单位改成句子或事件 block 后，熵产生才更有机会反映高层顺序结构。

第五步，用两个例子把这套框架落地：

- GPT-2 的概念验证实验说明：block-level entropy production 比 token-level entropy production 更容易区分高层顺序结构；
- Kalman 的线性高斯案例说明：在一个解析可解的 non-Markov 观测生成过程中，这个熵产生不只可定义、可数值估计，还能写成闭式公式。

第六步，再把总熵产生拆开。作者证明

$$
\mathcal S_y=\sum_{t=1}^{T}\mathcal D_t
=
\sum_{t=1}^{T}(\mathcal L_t+\mathcal M_t),
$$

其中：

- $\mathcal D_t$ 是第 $t$ 步对总不可逆性的非负贡献；
- $\mathcal L_t$ 是把完整未来压缩成后向摘要时丢掉的回顾信息；
- $\mathcal M_t$ 是在同一个压缩摘要条件下，backward model 发射核与真正回顾分布之间的失配。

到这里，这篇文章真正建立起来的，不只是“一个新的数”，而是一整套从路径测度、到可计算熵产生、到回顾性分解的非马尔可夫随机热力学语言。

### 7.2 为什么这个结果在方法论上重要

最后一节真正想强调的，不只是“我们把公式推完了”，而是这套框架改变了对生成模型不可逆性的看法。

以前在随机热力学里，最熟悉的对象是 Markov 跳跃过程或 Markov diffusion。这里作者展示的是：只要生成过程有确定性内部记忆，并且发射核显式可写，那么即使外部输出序列本身是 non-Markov 的，也仍然能定义 Crooks 型 forward / backward 路径比，并由此得到熵产生。

这一步很重要，因为现代生成模型真正可见、也真正有意义的对象，往往不是内部 latent state，而是：

- 输出 token 序列；
- 观测序列；
- 生成的文本、声音、动作片段。

如果只在某个人工选定的 latent 层上讨论不可逆性，就很容易碰到前面 Appendix A 讲过的问题：前向和后向的合法路径集合甚至可能不重合，导致更高层的 KL 发散。把热力学对象定义在观测序列层面，等于是在一个更稳定、也更接近实际生成行为的层次上讨论时间箭头。

原文还特别强调：block 级粗粒化并没有改变可计算性的基本结论。把 token 换成 block，并不会引入新的组合爆炸；变的只是“比较 forward / backward 时，顺序反转的基本单位”。这意味着粗粒化不是额外补丁，而是可以被纳入同一热力学框架的结构化操作。

### 7.3 接下来最自然的理论方向是什么

原文在 perspectives 里先给出的，是更偏理论统计物理的延伸方向。

第一条线是有限时间权衡关系。Markov 随机热力学里早就有：

- thermodynamic uncertainty relations；
- thermodynamic speed limits；
- 精度、速度与熵产生之间的权衡。

这条线和你之前读过的 `TUR` 脉络其实是直接相连的。那里最核心的物理图像是：如果一个系统想维持一个平均值大、波动又小的稳定电流，那么它就必须支付足够的熵产生。也就是说，`方向性 + 精确性 + 低噪声` 不是免费的，它们背后有一个不可逆性成本。

作者这里在问的是同一类问题，只是把“稳定电流”换成了“稳定生成”。如果一个自回归生成模型想做到下面这些事：

- 在有限时间内更快地完成序列生成；
- 输出更接近目标分布、更接近目标文本或目标语义；
- 在不同采样轨迹之间保持更小波动、更强稳定性；

那么它会不会像 `TUR` 里的稳定电流一样，也必须支付一个不可低于某个阈值的熵产生代价？

这里的“最小熵产生”不要理解成系统天然会去最小化熵产生，也不要直接和近线性非平衡里的 minimum entropy production principle 混在一起。这里更准确的意思是：

- 先固定某个性能要求，例如生成速度、生成精度或生成稳定性；
- 再在所有能满足这些要求的生成过程里，问熵产生最少能压到多少。

所以这里真正关心的是一种**受约束的最小不可逆性代价**。如果未来真的能在 autoregressive non-Markov setting 里建立出类似 `TUR` 或 thermodynamic speed limit 的不等式，那么它们就会回答这样的问题：要想让序列生成又快、又准、又稳，最低需要支付多少熵产生。

第二条线是和 computational mechanics 的连接。这里最好先把它在研究什么讲清楚。computational mechanics 问的核心问题是：给定一条随机序列的完整过去，能不能把这个过去压缩成一个**尽可能小、但对未来预测又不丢信息**的状态表示。这个最小预测状态通常叫 causal state；把所有 causal states 及其转移结构组织起来，就得到 $\epsilon$-machine。

所以它真正想找的不是任意一个隐藏状态，而是这样一种摘要：

- 它由过去决定；
- 它对未来是充分的，也就是知道这个摘要以后，就不需要再看完整过去；
- 它又尽可能小，不保留多余记忆。

现在再回来看这篇文章里的前向摘要 $f_{t-1}^\rightarrow$。它扮演的角色和上面这件事非常接近：完整过去 $y_{1:t-1}$ 先被压进一个确定性摘要里，然后下一步的条件分布就只通过这个摘要来给出。也就是说，$f_{t-1}^\rightarrow$ 本身就在做“把过去压缩成一个仍然足以支持预测的内部状态”这件事。

当然，这里还不能直接说 $f_{t-1}^\rightarrow$ 就是 causal state。因为 computational mechanics 里的 causal state 还强调两点：

- 它是对未来预测真正充分的最小统计量；
- 它的定义来自过程本身，而不是某个具体神经网络架构里人为选定的隐藏表示。

所以作者最后提出这条连接，真正意思是：也许可以把这篇里的前向/后向摘要，和 computational mechanics 里的“最小充分预测状态”放到同一张图上比较。这样一来，问题就会更清楚：

- 哪一部分熵产生来自“过去被压缩以后，预测信息确实丢了”；
- 哪一部分熵产生来自“模型虽然保留了摘要，但这个摘要本身并不是最优的预测状态”；
- 又有哪一部分是时间箭头本身导致的 forward / backward 不对称。

所以这条 perspective 的真正落点不是一句“记忆压缩很重要”，而是：也许可以借助 computational mechanics，把这篇文章里的隐藏摘要、信息压缩和不可逆性放进同一个更系统的状态空间语言里。

### 7.4 往更大语言模型推广时，真正的难点在哪里

最后一节接着把视角从理论框架推到更现实的语言模型。

作者先说得很明确：把这套框架应用到比 GPT-2 更大的语言模型，是一个重要方向。但一旦真的往上推，困难会分成两层。

第一层先出现在粗粒化对象本身。现在这篇文章已经把 token-level reversal 提升到了 block-level reversal，所以时间反演的基本单位不再是单个 token，而是句子或事件片段。这一步确实比 token 级更接近高层结构，但作者接着指出：这还没有真正到“语义层”。原因很直接。同一个语义事件，经常可以用很多不同的 token 序列来表达，例如：

- 不同措辞；
- 同义改写；
- 不同句法结构；
- 不同修辞组织。

如果 coarse-graining 仍然只在 token 序列上做，那么即使两个 block 传达的是同一个意思，只要它们的表面 token 不同，它们在当前框架里仍然会被当成不同对象。这样一来，block-level entropy production 仍然可能主要在比较“表面表达顺序”，而不是在比较“语义内容本身的时间结构”。所以作者提出：未来也许需要在 token 序列之上再做一层 coarse-graining，把表达同一语义内容的不同表面形式并起来。只有这样，熵产生才更有可能真正触到语义层不可逆性。

第二层是在解释上更根本的困难。即使你已经把分析尺度提高到 block 层，也不能立刻把测到的熵产生解释成“真实世界因果结构”的强证据。原文这里说得非常谨慎：block-level entropy production 至少混合了三类不同来源。

第一类，是文本里描述的事件之间真实存在的因果依赖。比如“先点火，再沸腾”这种顺序，本身就来自现实过程的因果方向。

第二类，只是时间先后上的排列，而不一定对应真实因果。也就是说，一些事件在文本里前后出现，只是叙述顺序如此，并不意味着前一个真的导致后一个。

第三类，则来自语言和叙事本身的约定。例如故事结构、修辞组织、说明文写法、话语习惯，这些东西也会强烈影响 block 的排列顺序，但它们未必是在反映现实物理过程的时间箭头。

所以这里真正的难点不只是“把 GPT-2 换成更大的 LLM”，而是：即使你已经得到一个更稳定、更有解释力的 coarse-grained entropy production，后面仍然要继续追问，这个量里面到底有多少来自真实因果结构，有多少只是时间顺序本身，又有多少只是语言组织规则。只有把这几部分拆开，block-level entropy production 才可能真正升级成一个 probing tool，而不只是一个更好看的高层顺序指标。

### 7.5 为什么作者最后会把这件事接到 world model

最后一句把问题从“模型序列是否不可逆”进一步推到了“模型内部是否编码了某种世界过程的时间箭头”。

这里先要把 `world model` 说清楚。在这个语境里，它不是一个已经被严格证明存在的单独模块，也不是说语言模型内部一定有一个显式环境模拟器。这里更稳的理解是：如果一个模型在大量文本训练中，逐渐学到了现实世界里事件如何发生、如何推进、什么先什么后、什么方向自然什么方向不自然，那么这种关于世界过程的顺序结构，就可以看成一种 `world-model-like structure`。

为什么这里会特别强调“时间不可逆性”？因为很多现实过程本身就带时间箭头。例如：

- 玻璃打碎比碎片自发拼回去常见得多；
- 点火在前、沸腾在后，比反过来更自然；
- 因果作用通常先有原因，再有结果。

如果语言模型的内部表示真的学到了这类世界规律，那么它不应该只知道“哪些词经常一起出现”，还应该在更高层的事件组织上区分：

- 哪种顺序更像真实世界会发生的过程；
- 哪种顺序虽然语法上合法，但在世界层面不自然；
- 哪种反转虽然只是 token 层重排，却破坏了事件推进的方向。

这时，coarse-grained entropy production 才会变得有意义。它的角色不是直接宣告“模型有了 world model”，而是更像一个探针：如果把序列提升到 block、事件甚至语义层之后，模型对 forward 顺序和 reversed 顺序持续给出显著不同的统计权重，那么这说明模型内部很可能已经编码了某种高层时间方向性。反过来说，如果这种差异只停留在 token 级语法 artifact，或者一旦提升到更高层就消失，那么它更像是在测语言表面规则，而不是世界过程的时间箭头。

所以这里最值得抓住的，不是一个强断言，而是一条更谨慎的推理链：

1. 语言模型也许在内部压进了现实过程的顺序结构；
2. 现实过程往往本身带有时间不可逆性；
3. 如果 coarse-grained entropy production 真能在高层尺度上稳定测出这种方向性；
4. 那它就可能成为 probing world-model-like structure 的量化工具。

但作者同时也在暗示边界：即使将来测到了显著的 coarse-grained entropy production，也不能立刻推出“模型已经有完整 world model”。更准确的解释是：模型内部至少编码了某种与现实过程时间方向有关的高层统计结构。要从这里进一步走到强意义上的 world model，还需要把前面 `7.4` 里那些混杂来源继续拆开，尤其要分清：

- 真实因果结构；
- 单纯时间排序；
- 语言叙事约定；
- 以及更深层的语义等价与语义粗粒化。

所以这篇文章的 perspective 最后落点其实很清楚：

- 近处，它是在给 autoregressive generative models 建立非马尔可夫随机热力学框架；
- 再远一点，它是在问：这种熵产生能否变成 probing tool，用来测试生成模型内部到底编码了多少世界过程的时间箭头；
- 更远一步，它才可能接到你关心的那个问题：高层时间不可逆性，是否能作为 world model 的一个可测侧面。

`Summary and perspectives` 的最短总结是：

**这篇文章的贡献，不只是把熵产生定义搬到 autoregressive models 上，而是把“非马尔可夫生成过程的不可逆性可以被统一定义、可计算、可粗粒化、可分解，并可能进一步拿来 probing world-model-like structure”这整条路线搭了起来。**

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
