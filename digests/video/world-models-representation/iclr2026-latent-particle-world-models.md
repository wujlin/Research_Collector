# Latent Particle World Models：把 actionless video 变成 object-centric world model

- Video: https://www.youtube.com/watch?v=aZeaCyXJjYI
- Transcript: `youtube/transcripts/aZeaCyXJjYI-iclr2026-oral-latent-particle-world-models/transcript.md`
- Slides: `youtube/slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/`
- Speaker: Tal Daniel

## 1. 这篇 oral 要回答的问题

这场 talk 的核心问题是：如果只有视频观测，没有真实 action label，能不能仍然学出一个可用于预测、采样和决策的 world model？

传统 world model 往往默认存在显式动作输入。比如在强化学习环境里，状态从 $x_t$ 到 $x_{t+1}$ 的变化可以由真实动作 $a_t$ 解释。但现实视频里经常没有这种动作标签。视频只告诉你“画面发生了变化”，没有告诉你“是什么控制变量造成了变化”。LPWM 的第一步就是把这个缺失的控制变量改写成 latent action。

![LPWM overview](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/01-title-lpwm.jpg)

这里的关键不是单纯做视频生成，而是学习一个 object-centric stochastic dynamics model。也就是说，模型不仅要预测下一帧，还要把场景拆成可追踪的实体，并在实体层面描述不确定的未来演化。

## 2. 第一层困难：没有动作时，状态转移从哪里来

talk 先引入 latent actions。直观地说，latent action 是从连续两帧之间反推出的隐变量：它不是外部给定的真实动作，而是模型为了解释 $x_t \rightarrow x_{t+1}$ 这次变化而学习出的内部动作表示。

![Latent actions](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/02-latent-actions.jpg)

常见做法是一个 auto-encoding 结构：inverse dynamics model 根据相邻观测推断 latent action，decoder 再根据前一帧和 latent action 重构后一帧。这个结构表面上合理，但 speaker 指出两个问题。

第一个问题是 representation collapse。latent action encoder 可能直接把下一帧信息塞进 latent action，导致 decoder 不再真正使用前一帧。为了防止这种“作弊”，过去方法常用 vector quantization 或 KL regularization 把 latent action 压住。

第二个问题是 global modeling。很多方法只用一个全局 latent vector 表示整帧变化。对于只有单一主体的任务，这可能勉强够用；但对于多个物体同时运动、多个局部互动并存的场景，一个全局向量很难自然拆出每个实体的局部变化。

## 3. 第二层困难：视觉表示不是语义对象

LPWM 接着转向视觉表示问题。传统视觉 world model 常把整帧压成一个向量，或者把图像切成固定 patch。这两种表示都不够理想。

![Traditional visual representation](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/03-traditional-visual-representation.jpg)

单向量表示太粗，会丢掉多物体场景中的细节。patch 表示更细，但它是几何网格，不一定对应语义实体。语言中的 token 通常有语义含义，而图像 patch 只是固定位置的局部块。如果目标是让视觉、语言和规划对齐，那么“物体级 token”比“网格级 patch”更自然。

![Representation discrepancy](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/04-representation-discrepancy.jpg)

所以 talk 的逻辑不是先发明一个新架构，而是先指出：如果要从视频中学习可用于决策的 dynamics，表示层最好不是全局向量，也不只是 patch grid，而应该接近“场景由多个实体组成”这个结构。

## 4. 第三步：用 Deep Latent Particles 做自监督 object-centric 表示

LPWM 的表示基础是 Deep Latent Particles，简称 DLP。DLP 可以理解成一种 VAE，但它的 latent space 不是单个向量，而是一组 particles。

![Object-centric representations](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/05-object-centric-representations.jpg)

每个 particle 携带多个属性，例如 keypoint、bounding box、transparency 和 visual feature。这样一来，一个视频帧不再被压成一个不可解释向量，而是被表示成一组实体状态。模型通过 reconstruction error 和 KL divergence 学这些粒子属性，所以不需要人工标注物体框或 mask。

![Deep latent particles](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/06-deep-latent-particles.jpg)

这一步建立了 LPWM 的基本状态空间：不是 pixel space，也不是 patch-token space，而是 particle latent space。后面的 dynamics 都在这个粒子集合上发生。

## 5. LPWM 的核心机制：从全局 latent action 改成 per-particle latent action

LPWM 在 DLP 之上加入 context module，用来学习 actionless video 里的 stochastic dynamics。这个模块的关键是：latent action 不是一个全局向量，而是 per-particle latent action。

![Context module and latent actions](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/07-context-module-latent-actions.jpg)

context module 有两个互补部分。latent inverse dynamics 根据观测到的粒子状态转移推断 latent actions；latent policy 则学习在当前粒子状态下 latent actions 的分布。训练时，inverse dynamics 负责解释真实转移；推断时，latent policy 可以直接采样 latent actions，从而生成多种可能未来。

这和固定 prior 或 codebook regularization 的区别在于：这里的 prior 是学出来的，而且推断时还会继续使用。它不是只在训练中防止 collapse 的正则项，而是变成了生成 stochastic rollouts 的动力来源。

## 6. 条件信号如何进入模型

LPWM 还可以接收外部 conditioning，例如真实 action、language instruction、image goal 或 multi-view input。线性地看，这些信号并不是直接控制像素，而是先进入 context module，再被翻译成 per-particle latent actions。

这点很重要。比如语言指令“把绿色方块推向红色星星”不是直接告诉模型每个像素怎么变，而是提供一个全局任务约束。LPWM 要做的是把这个全局信号分解成各个 particle 的局部变化，使粒子级 dynamics 朝着目标演化。

## 7. 实验部分：预测、生成、语言条件和 imitation learning

实验首先验证视频预测与生成。speaker 提到 Mario、BAIR、Sketchy 和 Language Table 等多物体环境。比较对象包括 patch-based dynamics VAE 和 slot-attention-based object-centric baseline。

![Video prediction and generation](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/08-video-prediction-generation.jpg)

这里的判断标准不是单纯看像素是否清晰，而是看模型是否维持 object permanence、是否能处理多个物体、是否能采样不同未来。在 BAIR 这类真实多物体互动数据上，speaker 特别强调非 object-centric baseline 容易出现物体消失或变形。

最后一段把 world model 接到 imitation learning。逻辑是：如果 LPWM 在 actionless video 上预训练后，学出的 latent actions 真的编码了 actionable information，那么只需要再学一个从 latent actions 到真实动作的简单映射，就可以得到策略。

![Imitation learning setup](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/09-imitation-learning-setup.jpg)

推断时，模型先在 latent particle space 中 roll out 未来，再把 latent actions 映射成环境动作，并以 closed-loop 方式执行。Panda push 的结果说明，这种“先学 actionless object-centric dynamics，再少量映射到动作”的路线在多物体操作任务上有潜力。

![Imitation learning results](../../slides/aZeaCyXJjYI-iclr-2026-oral-latent-particle-world-models/curated/10-imitation-learning-results.jpg)

## 8. 这篇 talk 对我们阅读框架的意义

LPWM 和之前 world model / JEPA / latent representation 的阅读线直接相连。它把“状态表示”从 frame vector 推到 object-centric particles，又把“动作”从真实动作标签推广成 latent transition variable。

对 synthetic city 或 mobility/corridor 问题来说，可以抽象出一个可迁移问题：如果观测到的是复杂系统的状态序列，但没有显式控制变量，那么能否先学出一组 latent entities 和 latent actions，再把它们用于预测、条件生成或策略恢复？

这篇工作的局限也很清楚。speaker 直接承认 self-supervised object-centric representation 还没有真正 scale 到通用 in-the-wild video，像素保真度也不如现代 diffusion video generator。也就是说，LPWM 的优势在结构和决策接口，不在纯视觉保真度。
