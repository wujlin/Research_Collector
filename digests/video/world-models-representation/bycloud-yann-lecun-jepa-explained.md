# JEPA 解释视频：从像素预测转向 latent world modeling

- Video: [What Is Yann LeCun Cooking? JEPA Explained Simply](https://www.youtube.com/watch?v=oM4neOyZOi0)
- Creator: bycloud
- Transcript: [transcript.md](../../transcripts/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/transcript.md)
- Slides: [curated/index.md](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/index.md)

这条视频不是 Yann LeCun 本人的技术报告，而是一条解释型视频。它的价值在于把 JEPA 的问题意识讲得比较线性：传统生成模型常常预测 token、像素或去噪后的图像，而 JEPA 试图预测 learned latent space 里的 representation。也就是说，它不直接问“下一个像素是什么”，而是问“另一个 view 背后的稳定语义状态是什么”。

## 1. 00:00-04:30：JEPA 的第一步是把预测对象从表面数据换成 latent view

![JEPA question](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/01-jepa-question.jpg)

视频开头先强调 JEPA 难懂的原因：它不像 LLM 那样有一个直观的 next-token objective，也不像 diffusion 那样有一个直观的 denoising objective。JEPA 的预测对象是高维 latent representation，这使得它一开始就比“预测词”或“预测像素”更抽象。

关键概念是 view。一个 view 不是某个固定模态，而是对同一底层状态的部分观察。例如一只猫坐在沙发上，可以被表示成整张图、左半张图、右半张图、局部 crop、mask 后图像、另一帧视频、另一角度观察，甚至一段文字描述。这些 view 在表面上不同，但它们共享某个 underlying semantic state。

![JEPA architecture](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/02-jepa-architecture.jpg)

于是 JEPA 的训练逻辑可以线性写成：

$$
\text{context view} \rightarrow \text{context embedding} \rightarrow \text{predictor} \rightarrow \widehat{\text{target embedding}}.
$$

另一个 target view 经过 target encoder 变成真正的 target embedding。训练目标不是重建 target view 的像素，而是让预测出的 latent embedding 靠近真实 target embedding。

![Latent view objective](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/03-latent-view-objective.jpg)

这一步的意义在于过滤掉低层噪声。像素级 reconstruction 会要求模型解释光照、纹理、噪声、背景和所有偶然细节；而 latent prediction 更倾向于保留跨 view 稳定的对象、结构、运动和语义关系。JEPA 的核心赌注是：世界建模不一定要在像素层完成，真正有用的预测可以发生在 representation space。

## 2. 04:30-08:30：JEPA 的三种使用方式

![V-JEPA latent prediction](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/04-vjepa-latent-prediction.jpg)

视频接着把 JEPA 的用途分成三层。第一层是 representation extraction。模型把图像、视频或其他输入编码成 embedding，这个 embedding 可以用于分类、检索、相似度搜索或下游微调。此时 JEPA 更像一个自监督表征学习器。

第二层是 latent prediction for world modeling。加入 predictor 后，模型可以从当前状态 embedding 预测未来状态 embedding。V-JEPA 的重点就在这里：它不是生成未来视频帧，而是在 latent space 中预测未来。这样既节省计算，又避免把容量浪费在无关纹理上。

第三层是 planning in latent space。如果 predictor 还能接受 action embedding，那么它就可以预测不同动作会把当前 latent state 推到哪里。这样一来，规划就可以变成在 latent space 中比较不同 action sequence 的后果，而不是每次都生成完整视频。

这一层和 Jim Fan 的 DreamZero 很接近：二者都把未来预测放在中间表征空间，而不是直接从当前观测跳到动作。区别是 Jim Fan 的语境更偏机器人控制，JEPA 的语境更偏通用自监督 world representation。

## 3. 08:30-12:00：最大风险是 representation collapse

![Representation collapse](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/05-representation-collapse.jpg)

JEPA 的好处来自 latent space，但最大的失败模式也来自 latent space。如果 context encoder 和 target encoder 都输出同一个常数向量，那么 predictor 很容易让 loss 变小：不管输入是猫、车还是建筑，embedding 都一样，预测也一样，训练目标看似满足，但模型完全没有学到世界结构。

这就是 representation collapse。它说明一个重要事实：仅仅要求两个 embedding 靠近是不够的，因为“所有东西都靠近同一个点”也是一种低 loss 解。JEPA 必须额外保证 representation 既可预测，又含有足够信息。

早期做法是 EMA target encoder。target encoder 不直接跟着梯度快速更新，而是作为 context encoder 的指数滑动平均缓慢移动。这样 target 不会立刻和 context 合谋塌缩到同一个常数点，训练会更稳定。

但视频也指出，EMA 更像训练技巧，而不是一个完全原则化的 objective。它能工作，但稳定性依赖动量系数、更新日程和架构细节。于是后续研究继续寻找更直接的 anti-collapse 约束。

## 4. 12:00-16:30：从 contrastive / non-contrastive 到 LeJEPA 的几何约束

![InfoMax and contrastive learning](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/06-infomax-paper.jpg)

视频先把 anti-collapse 放回 self-supervised learning 的历史线索。InfoMax 的直觉是：好的 representation 应该保留输入中的有用信息。如果 embedding 里完全看不出原输入是什么，它就不是好表征。

contrastive learning 是一种经典实现。SimCLR 这类方法把同一样本的两个增强 view 拉近，把不同样本推远。这样 embedding space 不容易塌缩，因为不同样本必须占据不同位置。

non-contrastive 方法则不显式使用负样本，而是约束 embedding 的维度之间不要冗余。Barlow Twins、VICReg 等方法通过惩罚维度相关性，让不同坐标承载不同信息。它们避免了大 batch negative samples，但需要多个 loss term 和较细的超参数平衡。

![LeJEPA paper](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/07-lejepa-paper.jpg)

LeJEPA 的新意在于把 anti-collapse 改写成 embedding geometry 的约束。要理解这句话，先要把 collapse 看成一个几何退化问题，而不是只看 loss 数值。

在 JEPA 里，每个输入样本都会被 encoder 映射成一个 embedding。很多样本放在一起，就形成一个 embedding cloud。如果模型真的学到了有用表示，那么不同样本应该在这个空间里占据不同位置，而且这些位置应该沿多个方向展开。这样，embedding 才能保留足够信息，让 predictor 有东西可以预测。

collapse 的坏情况可以分成几类。第一种是所有样本都变成同一个向量，embedding cloud 直接塌成一个点。此时模型完全失去区分能力。第二种是样本虽然不完全相同，但主要沿一个方向变化，点云变成一条线。此时模型只用了一个有效维度。第三种是点云只落在少数几个方向构成的薄片上，虽然看起来还有变化，但大部分维度是冗余或空的。

所以 anti-collapse 的目标不是简单地“让 loss 不为零”，而是让 representation space 保持足够体积和足够有效维度。

早期 non-contrastive 方法常做的一件事是 decorrelation，也就是让不同 embedding 维度之间不要高度相关。如果第 3 维总是等于第 5 维的线性变换，那么这两个维度其实在表达同一件事。去相关可以减少这种冗余。

但 LeJEPA 想做得更整体：它不只是要求维度之间去相关，而是鼓励整个 embedding distribution 接近 isotropic Gaussian。这里的 isotropic Gaussian 可以理解成一个标准球状高斯：

$$
\mathcal N(0,I).
$$

这包含三层含义。第一，均值接近 0，表示整个点云不要整体漂到某个偏置位置。第二，各个维度的方差接近一致，表示每个维度都应该被使用，而不是只有少数维度有变化。第三，不同维度之间相关性接近 0，表示坐标轴之间不要互相复制信息。

把这三点合起来，embedding cloud 就不应该塌成一个点、一条线或一个薄片，而应该像一个各向同性的球状点云，在各个方向上都比较均匀地展开。

这就是为什么它是一个 embedding geometry 约束。LeJEPA 并不是只在单个样本上说“预测值要接近目标值”，而是在一整个 batch 或一整个数据分布上约束 representation cloud 的形状。预测任务负责让 representation 有语义，isotropic geometry 负责让 representation 不塌缩。

![Isotropic Gaussian geometry](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/08-isotropic-gaussian-results.jpg)

这一步的逻辑很重要。collapse 的问题本质上是几何问题：representation space 的体积退化了。LeJEPA 用分布形状约束来直接防止这种退化，让 embedding space 保持足够维度和足够信息量。

![Embedding geometry](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/09-geometry-of-embedding.jpg)

从我们最近的阅读框架看，LeJEPA 和最优传输、flow、HJB 这些主题有一个共同点：模型学习的不只是输入输出映射，而是中间空间的几何。只不过这里的几何不是显式的 Wasserstein geodesic 或 control potential，而是 representation cloud 的可预测、非塌缩、各向同性结构。

## 5. 16:30-18:00：为什么 JEPA 更适合视觉、视频和物理世界，而不是纯文本

![JEPA versus LLM data](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/10-jepa-vs-llm-data.jpg)

视频后半段解释为什么 JEPA 没有直接替代 LLM 的 next-token prediction。原因不是 JEPA “不够高级”，而是文本和感知数据的噪声结构不同。

文本已经是压缩后的符号系统。词序、语法和语义约束使 next-token prediction 能提供强监督信号。相反，图像、视频、医学影像和机器人感知包含大量不可预测的低层细节：光照、纹理、传感器噪声、视角变化、反射和遮挡。如果强迫模型重建这些细节，它会浪费很多容量。

所以 JEPA 的适用场景更偏向 sensory-rich world：那里存在大量表面噪声，但背后有稳定结构。JEPA 的任务就是把稳定结构从噪声里提取出来，并在 latent space 中预测它的演化。

## 6. 18:00-20:00：医学影像是 JEPA 的自然应用场

![EchoJEPA and ultrasound](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/11-echo-jepa.jpg)

视频最后用 EchoJEPA 说明医学影像为什么适合 JEPA。超声图像有大量 speckle noise、sensor artifacts、probe angle variation 和设备差异。如果模型按像素重建，会花很多容量学习临床上不重要的噪声模式。

![Ultrasound distortions](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/12-ultrasound-distortions.jpg)

医生真正关心的是更稳定的解剖和生理结构：心腔大小、心壁运动、瓣膜开合、节律和收缩模式。这些信息不一定需要像素级复原，但需要在 representation 中被稳定保留。

![EchoJEPA results](../../slides/oM4neOyZOi0-what-is-yann-lecun-cooking-jepa-explained-simply/curated/13-echo-results.jpg)

EchoJEPA 的做法就是从早期心动周期帧预测未来 cardiac motion 的 latent representation。这样模型更容易学习心脏几何和运动模式，而不是记忆超声纹理噪声。

总结起来，JEPA 这条路线的核心不是“反对 LLM”，而是指出另一类问题需要另一种预测目标：当世界数据充满低层噪声、但背后存在稳定动态结构时，直接预测 surface token 或 pixel 可能不是最有效路径；预测 latent state 可能更接近 world modeling 的核心。
