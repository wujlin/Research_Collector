# Welch Labs: The F=ma of Artificial Intelligence

- Video: [The F=ma of Artificial Intelligence](https://www.youtube.com/watch?v=VkHfRKewkWw)
- Series: How Models Learn, Part 2
- Channel: Welch Labs
- Duration: 30:31
- Transcript: `youtube/transcripts/VkHfRKewkWw-the-fma-of-artificial-intelligence-backpropagation-how-models-learn-part2/`
- Slides: `youtube/slides/VkHfRKewkWw-the-fma-of-artificial-intelligence-backpropagation-how-models-learn-part-2/semantic_curated/`

这集视频接着第一集的问题往下走：既然现代模型在高维 loss landscape 中依赖 gradient descent，那 gradient 到底怎么高效算出来。视频把 backpropagation 讲成一种“可扩展的局部因果分解”：不用逐个试参数，而是沿 computation graph 反向传播误差信号，把输出错误拆回到每个权重和 bias 上。

## 1. 00:00-04:20：backprop 是现代 AI 的训练底层法则

视频开头从 Paul Werbos 和 Marvin Minsky 的历史讲起。Werbos 发现的 backpropagation 一度被低估，但后来训练了自动驾驶早期系统、手写数字识别、图像分类模型，今天几乎所有现代 AI 模型都依赖它。

视频用 Llama 3.2 的真实数据流做动机：给定输入文本，模型预测下一个 token；backprop 要判断十亿多个参数中哪些该增、哪些该减、每个改多少。这个任务看起来不可思议，但核心数学并不复杂，关键是它能沿网络层级重复应用。

## 2. 04:18-09:30：把语言模型简化成 GPS 城市分类器

为了把数学说清楚，视频把 Llama 简化成一个小模型：输入 GPS 坐标，预测城市是 Paris、Madrid 还是 Berlin。最开始甚至只用 longitude 一个输入。每个城市对应一个 neuron，neuron 做的事情就是把输入乘以 weight，再加 bias，得到一个中间分数。

这些中间分数还不是概率，所以最后通过 softmax 变成三个城市的概率分布。训练目标仍然是 cross entropy loss：正确城市的概率越低，loss 越大。

这个 toy model 的作用是让每个参数都看得见。模型只有几个 slope 和 bias，但它已经包含了现代神经网络训练的基本结构：linear computation、softmax probability、loss、gradient update。

## 3. 09:27-14:29：不要用数值试探参数，要用链式法则沿图分解

一个朴素做法是逐个微调参数，重新跑模型，看 loss 变化多少。这可以估计 slope，但成本高，而且估计依赖步长。backprop 的思想是直接用 calculus 精确算出 slope。

视频没有把所有公式当重点，而是强调结构。一个网络由很多 compute blocks 组成，每个 block 都有自己的输入和输出。整体输出对某个早期参数的变化率，可以拆成每个 block 局部变化率的乘积。这就是 chain rule。

这个分解非常适合 neural network，因为网络天然就是 computation graph。每一层只需要知道局部输入、局部输出和从后面传回来的误差信号，就能算出自己参数的梯度。

## 4. 14:27-19:47：cross entropy 和 softmax 给出简单的输出误差信号

视频中最重要的简化是：cross entropy loss 和 softmax 放在一起时，输出层的误差信号会变得很直接。对每个类别，误差信号基本就是模型预测概率减去真实 one-hot label。

如果 Paris 是正确答案，而模型只给 Paris 很低概率，那么 Paris neuron 的误差信号是负的，表示提高这个 neuron 的输出会降低 loss。相反，如果 Madrid 被错误地给了很高概率，Madrid neuron 的误差信号是正的，表示提高它会让 loss 更坏。

接着，某个 weight 的梯度还要乘上该 neuron 的输入值。直觉是：如果输入很小，这个 weight 对输出影响就小，更新也应该小；如果输入很大，它对输出影响更强，更新就更大。于是梯度同时编码了“错在哪里”和“哪个参数对这个错误有多大责任”。

最后用 gradient descent 更新参数：沿梯度相反方向走一小步。learning rate 控制步长，因为梯度只是当前位置附近的局部信息。

## 5. 20:09-24:09：可视化训练过程：线、平面和城市区域

视频把训练过程画到地图上。最初模型可能把 Paris 误分成 Madrid，backprop 会给 Paris 和 Madrid 相关参数较大梯度，把 Paris 区域逐步推到正确位置。

当只输入 longitude 时，每个 neuron 对应一条线。哪个城市的线在某个 longitude 上最高，softmax 就会给哪个城市最大概率。训练就是调整这些线的位置，让 Madrid 线在 Madrid 上方最高，Paris 线在 Paris 上方最高，Berlin 线在 Berlin 上方最高。

加入 latitude 后，线变成平面。每个城市对应一个平面，模型学习把正确城市的平面放到对应地理区域上方。这是一个非常好的几何直觉：分类不是神秘操作，而是在表示空间里学习让正确类别的 score surface 高过其他类别。

## 6. 24:07-28:29：从城市分类回到语言模型

视频最后把 toy model 和语言模型接起来。Llama 内部会把 token 表示成高维向量。所有能导致下一个 token 是 Paris 的上下文，并不形成一个简单连通区域。有些是 Treaty of Paris，有些是 American in Paris，有些是地理问答；它们在表示空间中可能是很多分离簇，但最终都要映到同一个 next token。

这就像 Belgium/Netherlands 的复杂边界：简单平面无法分出复杂区域。神经网络要做的是不断 reshape 表示空间，让许多分散的语义区域最终被正确分类。

Minsky 低估 backprop 的地方就在这里。他认为慢、简单的梯度更新很难学复杂模式；但事实是，一旦计算能力和数据规模足够，backprop 能把大量局部误差信号积累成复杂的高维几何变换。

这集自然接到第三集：单层平面分类器能力有限，那么深层网络究竟怎样通过多层结构学习复杂边界。
