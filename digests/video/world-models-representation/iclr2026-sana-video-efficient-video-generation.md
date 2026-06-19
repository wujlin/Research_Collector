# SANA-Video：把长视频生成问题拆成 token、attention、cache 与 causal block

- Video: https://www.youtube.com/watch?v=bHHL691_IPo
- Transcript: `youtube/transcripts/bHHL691_IPo-iclr2026-oral-sana-video-efficient-video-generation/transcript.md`
- Slides: `youtube/slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/`
- Speaker: Jun Song

## 1. 这场 talk 的起点：视频生成的瓶颈不是“能不能生成”，而是“能不能高效生成”

SANA-Video 的叙事从一个工程事实开始：视觉生成模型变得越来越强，但图像和视频生成比文本推理更耗算力。视频尤其麻烦，因为它同时扩展空间分辨率和时间长度。

![Generative AI background](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/01-background-generative-ai.jpg)

speaker 用 FLUX、CogVideoX、Llama3、ViT 等例子说明：视觉生成的 inference FLOPs 已经远高于普通文本模型或视觉编码器。因此问题不只是模型质量，而是部署位置。如果每次生成都必须依赖云端 GPU，consumer GPU 和 edge device 就很难真正使用这些模型。

![Efficiency bottleneck](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/02-efficiency-bottleneck.jpg)

## 2. SANA 系列先把效率问题拆成几条技术轴

SANA-Video 不是凭空出现的。talk 先把 SANA 系列已有路线串起来：减少 token 数、改模型结构、减少 inference steps、再进一步把 AR 和 diffusion 结合起来做长视频。

![SANA design family](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/03-sana-design-family.jpg)

第一条轴是 token 压缩。SANA 用 deep compression autoencoder 减少输入 token 数，因为 token 越多，transformer 计算和显存压力越大。

第二条轴是模型结构。SANA 用 linear attention 替代 softmax attention，希望把注意力计算从随序列长度二次增长的形式，推向更适合长序列的形式。

第三条轴是推理步数。SANA-Sprint 通过 step distillation 减少 inference steps，因为 diffusion 生成的速度很大程度上取决于需要走多少步。

第四条轴就是这场 talk 的重点：用 hybrid AR plus diffusion 做长视频生成。直观地说，视频可以被分成 block，block 之间因果生成，block 内部用 diffusion 处理。

## 3. 视频生成为什么比图像生成更难

SANA 图像模型可以在约 1 秒内生成图像，但 speaker 提到同一类模型生成 5 秒视频可能接近 30 分钟。视频的问题不是简单多几帧，而是时间维度让 token 数、attention 长度和缓存状态一起膨胀。

![Video synthesis bottlenecks](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/04-video-synthesis-bottlenecks.jpg)

SANA-Video 的技术目标因此很明确：用高压缩 VAE 减少 token，用 linear attention 降低注意力复杂度，再用 block KV cache 支持更长视频。

## 4. 架构路线：从 text-to-image 模型启动，而不是从零训练视频模型

speaker 强调，从零训练视频模型需要大量 H100 和数月时间，并不现实。SANA-Video 选择从 SANA 1.5 这个 text-to-image 模型出发，因为它已经有 semantic-aligned text-to-image 能力。

![SANA-Video architecture](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/05-sana-video-architecture-overview.jpg)

在这个基础上，模型大体沿用 SANA 的 linear attention DiT，但加入两个与时间建模相关的模块，并在左上角引入 block causal linear attention 来实现 constant KV cache memory。

这一步的逻辑是：如果已有图像模型负责空间生成能力，那么视频扩展的关键就是把时间结构加进去，而不是重新学所有空间语义。

## 5. Linear attention 的优势和补丁

Linear attention 的直接优势是计算效率。随着视频长度和分辨率升高，它相比 softmax attention 的优势会更明显。speaker 提到在长视频和高分辨率场景下，SANA-Video 的 linear attention 可以显著快于 flash attention。

![Efficient linear video DiT](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/06-efficient-linear-video-dit.jpg)

但 linear attention 也有问题。talk 里指出，linear attention map 很 dense，而 softmax attention 更 sparse。这说明 linear attention 捕捉局部时空关系的能力可能不足。SANA-Video 因此加入 3D RoPE 和 temporal convolution，用来强化时间建模。

![Linear attention mechanism](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/07-linear-attention-mechanism.jpg)

所以这里不是简单说“linear attention 更好”，而是更精确地说：linear attention 给了长序列效率，但需要额外 temporal design 来弥补时空建模质量。

## 6. Block causal linear attention：为什么它能支持长视频

最关键的一步是 block causal linear attention。普通 softmax attention 的 KV cache 会随序列长度增长；linear attention 的状态可以写成固定形状的 summary state。speaker 把它解释成一个 $D \times D$ 形状的 state，不随输入长度线性扩张。

![Block causal linear attention](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/08-block-causal-linear-attention.jpg)

生成第一个 block 时，模型计算这个 block 的 state 并缓存。生成第二个 block 时，不需要保留所有历史 token 的 KV，而是把当前 block 的贡献加到之前 cache 上。后续 block 重复这个过程。

这样做同时得到两个效果。第一，memory usage 对视频长度更稳定；第二，模型仍然保留 global history context，而不是只看滑动窗口。

## 7. Causal Mix-FFN：不仅 attention 要 causal，FFN 也要尊重时间

SANA-Video 还讨论 causal FFN。因为视频 block 是因果生成的，前一个 block 不能看到后一个 block。为此，模型在 block 之间加入 zero padding，并把前一 block 的最后 token 作为后一 block 的起始上下文。

![Block causal Mix-FFN](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/09-block-causal-mix-ffn.jpg)

这说明视频生成中的“因果性”不是只体现在 attention mask 上，而是要贯穿 attention、FFN、cache 和 block transition。

## 8. 实验和应用：从高效生成到 physical AI / world models

结果部分强调两个层面。第一，SANA-Video 在 VBench 上有竞争力，并且可以在单张 H100 上较快生成 1K 分辨率视频。第二，它可以通过少量 fine-tuning 推向 robotic manipulation 和 gameplay 这类 physical AI / world model 应用。

![Physical AI and world models](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/10-physical-ai-and-world-models.jpg)

最后，speaker 把 SANA 系列总结成一个效率路线图：减少 token、加速模型结构、减少 inference steps、用 hybrid AR 和 diffusion 推长视频。

![SANA summary](../../slides/bHHL691_IPo-sana-video-efficient-video-generation-with-block-linear-diffusion-transformer/curated/11-sana-summary.jpg)

对我们当前阅读框架来说，SANA-Video 的位置很清楚。它不是在讨论 HJB 那种控制势函数，也不是 LPWM 那种 object-centric latent dynamics，而是在生成系统层面回答：当生成对象从 image 扩展到 video，怎样让时空序列的计算结构不爆炸。

## 9. 需要保留的判断

SANA-Video 的核心贡献可以压缩成一句话：用 deep compression autoencoder 降 token，用 linear attention 降 attention 成本，用 block causal cache 把长视频生成改造成可持续更新的因果 block process。

它的开放问题也很自然。效率提高之后，下一步不是只看单段视频质量，而是看这些高效视频模型能否成为可交互、可控制、可持续 roll out 的 physical world model。
