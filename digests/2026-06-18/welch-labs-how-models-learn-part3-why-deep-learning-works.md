# Welch Labs: Why Deep Learning Works Unreasonably Well

- Video: [Why Deep Learning Works Unreasonably Well](https://www.youtube.com/watch?v=qx7hirqgfuU)
- Series: How Models Learn, Part 3
- Channel: Welch Labs
- Duration: 34:08
- Transcript: `youtube/transcripts/qx7hirqgfuU-why-deep-learning-works-unreasonably-well-how-models-learn-part3/`
- Slides: `youtube/slides/qx7hirqgfuU-why-deep-learning-works-unreasonably-well-how-models-learn-part-3/semantic_curated/`

这集回答第二集留下的问题：如果单层模型只能摆几张平面，为什么深度神经网络能学到极其复杂的边界。视频的线性答案是：非线性 activation 让每层把输入空间折叠、缩放、组合；多层复合以后，后面的层不是在原始平面上继续画线，而是在已经被折叠过的空间上继续折叠。深度的力量来自这种递归变形。

## 1. 00:00-04:52：万能逼近定理容易被误读

视频从 universal approximation theorem 开场。这个定理常被理解成“神经网络什么都能学”，但视频马上用 Baarle-Hertog 复杂国境线做反例式说明：一个极宽的两层网络理论上能表示很复杂的函数，但实际用 gradient descent 训练时，即使给到十万 neurons，也未必能把边界学好。

更有意思的是，把少量 neuron 分到多层后，模型反而学得更好。视频展示一个总 neuron 数很小的深层网络，能比巨大浅层网络更精确地拟合复杂边界。于是问题从“网络是否足够宽”转成“深度为什么改变表达效率和可训练性”。

## 2. 06:44-11:30：没有 activation，多层线性模型会塌回单层

视频先回顾第二集里的单层城市分类器：每个类别对应一个平面，平面相交形成线性决策边界。对于复杂边界，这显然不够。

如果只是把一层线性 neuron 接到另一层线性 neuron，中间不加 activation，模型并不会变强。多个线性变换复合以后仍然是线性变换；几张倾斜平面加来加去，结果还是一张倾斜平面。多层本身不够，关键是中间要有非线性。

ReLU 是这里的核心。它把低于零的部分压到零，高于零的部分保持不变。几何上，这相当于把一张平面沿着一条线折起来或裁掉。第一层的每个 neuron 都在输入地图上制造一条 fold line，把空间切成更多区域。

## 3. 11:28-14:49：浅层网络是在原始空间里叠很多折线

在两层网络里，第一层 ReLU neurons 在原始输入空间上放置多条 fold lines。第二层把这些 bent planes 缩放、翻转、相加，得到更复杂的 score surfaces。两个输出 surface 的交线就是分类边界。

这解释了为什么更宽的浅层网络能变强：更多 neurons 意味着更多折线，可以把输入平面切成更多 piecewise-linear regions。但视频也强调，万能逼近定理只说某个足够宽的网络存在，不说明 gradient descent 能找到它，也不告诉我们实际需要多少 neurons。

因此，“存在可表示解”和“训练能找到可用解”是两回事。这一点和第一集的 loss landscape 直觉相连：优化路径可能避不开坏初始化、dead ReLU 或低效的参数使用。

## 4. 15:12-20:03：训练失败说明表达能力不等于可达性

视频用小网络的坏初始化展示了一个具体失败模式。初始 surface orientation 如果刚好反过来，gradient descent 在修正方向时可能把重要区域推入 ReLU 的零区。进入零区后，梯度也变成零，模型失去可调整的折线，只剩下近似线性边界。

这个例子不是说大模型一定会这样卡死，而是提醒：网络架构允许某种解，不代表训练过程一定能到达。深度学习的成功同时依赖表示能力、初始化、optimizer、数据分布和 overparameterization。

## 5. 20:01-27:01：深层网络在已折叠空间上继续折叠

视频真正解释深度优势的地方，是把第二层之后的 ReLU 也可视化出来。第一层把原始地图折成若干区域；第二层先组合这些 bent surfaces，然后再通过 ReLU 折叠。此时被折叠的已经不是简单平面，而是由多个区域拼接成的 piecewise-linear surface。

结果是，一个后层 neuron 可以在输入空间里制造多条弯折的 fold lines，而且这些 fold lines 的角度和位置继承了前层已经学到的结构。换句话说，后层 neuron 不是“再加一条直线”，而是在前层变形后的坐标系统里切割空间。

这就是深度的 compounding effect。浅层网络的区域数随 neuron 数大体按组合几何的多项式方式增长；深层 ReLU 网络在理论上可以随层数产生指数级更丰富的区域划分。视频也谨慎指出，这些理论上界很松，实际训练通常达不到最大区域数，但方向很清楚：把 neurons 堆成深层结构，比全放在第一层更高效。

## 6. 27:24-31:36：从边界拟合回到现代深度学习

当网络扩展到多层、多宽度后，训练过程会先抓住边界的大结构，再逐步在细节附近创造更多小区域。视频里，深层网络能用少量层数和 neuron 数学出复杂地理边界，直观展示了深度模型如何把简单线性模块组合成复杂函数。

这集的最终结论不是“深度学习已经被完全理解”，而是给出一个比万能逼近定理更有用的几何直觉：深层网络通过反复折叠、缩放、组合输入空间，递归地产生复杂区域划分；backprop 则负责把这些折叠逐步调整到能降低 loss 的位置。

这也和 representation learning 的大问题相连。现代模型不是直接在原始空间上画一条复杂边界，而是逐层改变数据的几何，让原本纠缠的类别、语义、动作或状态在后层表示里变得更容易分开。
