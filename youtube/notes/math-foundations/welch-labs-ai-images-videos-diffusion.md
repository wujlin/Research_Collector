# Welch Labs: But how do AI images and videos actually work?

- Video: [But how do AI images and videos actually work?](https://www.youtube.com/watch?v=iv-5mZ_9CPY)
- Channel: 3Blue1Brown
- Guest creator: Welch Labs
- Duration: 37:20
- Transcript: `youtube/transcripts/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/`
- Curated slides: `youtube/slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/`

这期视频的主线不是泛泛介绍“AI 会画图”，而是把现代图像和视频生成拆成三层逻辑：第一，CLIP 这类模型把文本和图像压到同一个语义空间；第二，扩散模型不是从空白画布作画，而是在高维空间里从随机噪声一步步回到真实数据分布；第三，prompt 之所以能控制生成结果，是因为 text embedding、conditioning、classifier-free guidance 和 negative prompt 共同改变了这个回到数据分布的方向。

## 1. 00:00-02:31：先把现象落到具体模型上

![Opening VEO astronaut horse](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/01-opening-veo-astronaut-horse.jpg)

视频开场先展示现在的文本到视频能力：一句 prompt 可以生成很完整的电影式场景。这个开场很重要，因为它不是把生成模型当成抽象算法，而是先提出需要解释的现象：为什么语言能控制一个复杂视频的视觉结构、运动和风格。

![WAN prompt to video](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/02-wan-prompt-to-video.jpg)

接着视频进入开源模型 WAN 2.1。它展示一个 prompt 如何对应到视频输出，也展示修改 prompt 以后画面内容随之改变。然后叙事立刻转向一个反直觉事实：生成过程不是从一个粗糙草图开始，也不是从数据库里检索一段相似视频，而是从随机数生成的纯噪声视频开始。

![Random noise video seed](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/03-random-noise-video-seed.jpg)

模型反复接收当前噪声状态，输出一个更有结构的下一状态。一步一步，噪声里开始出现轮廓、物体、场景和运动。视频的第一个问题因此形成：如果起点是随机噪声，模型到底学到了什么，才能把噪声推回到一个合理的视频？

## 2. 02:31-08:20：CLIP 解决的是“文本和图像怎样进入同一个空间”

![CLIP image encoder embedding](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/04-clip-image-encoder-embedding.jpg)

视频随后回到 CLIP。CLIP 的关键不是生成，而是对齐。它有一个 image encoder 和一个 text encoder，分别把图像和文字变成向量。训练目标是让匹配的图像和 caption 在向量空间里靠近，让不匹配的图像和 caption 远离。

![CLIP contrastive similarity matrix](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/05-clip-contrastive-similarity-matrix.jpg)

这里的关键叙事点是“语义被几何化”。一张猫图、一句“a photo of a cat”、一张狗图、一句“a photo of a dog”，不再只是离散对象，而是被放进同一个高维空间。相似度可以通过向量方向来比较。于是模型不只是在分类，而是在学一个 image-text shared representation。

视频用“戴帽子”和“不戴帽子”的图片差分来说明这个空间的概念结构：两个图像向量的差可以接近“hat”这样的文本向量。这个例子把 CLIP 的意义说清楚了：它不能生成图像，但它给后续生成模型提供了一个可以被 prompt 操作的语义坐标系。

## 3. 08:20-11:43：DDPM 把生成问题改写成“从噪声返回数据”

![Forward noising process](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/06-forward-noising-process.jpg)

CLIP 只能把图像和文本送进 embedding space，不能从 embedding 反推出图像。因此视频转向扩散模型。DDPM 的基本故事是：训练时逐步给真实图像加噪声，直到图像结构被破坏；生成时则从噪声出发，学习沿反方向回到真实图像。

![Diffusion training noise prediction](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/07-diffusion-training-noise-prediction.jpg)

视频特别强调一个常见误解：扩散模型并不是简单训练成“把第 t 步去噪成第 t-1 步”。DDPM 的训练更像是让模型预测总共加入了哪些噪声。这样做的好处是降低训练目标的方差，让模型更稳定地学到“从当前噪声状态回到原始数据”的方向。

![Reverse image generation loop](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/08-reverse-image-generation-loop.jpg)

生成时，模型从随机噪声开始，反复预测如何往更像图像的方向走。这个过程解释了为什么文本到图像/视频不是“模型从记忆里拿出图”，而是一个迭代采样过程：每一步都把当前点推向更像真实数据的区域。

## 4. 09:48-11:43：为什么生成时还要加噪声

![DDPM sampling tree example](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/09-ddpm-sampling-tree-example.jpg)

视频接着解释 DDPM 里最反直觉的一步：生成时每一步去噪后还要再加随机噪声。直觉上，既然目标是去噪，为什么还要重新加噪？视频用 Stable Diffusion 的树和沙漠例子说明，如果把这一步删掉，图像会变成模糊、塌缩、缺少细节的平均结果。

![DDPM training and sampling algorithms](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/10-ddpm-training-and-sampling-algorithms.jpg)

这里的视频逻辑是：模型在许多可能图像之间学到的是一个条件平均方向。只沿平均方向走，容易把样本带到数据分布的中心，而不是多样的真实样本上。加入随机噪声等于保留采样的不确定性，让生成点有机会落到不同的真实图像模式上。

这个解释把“加噪声”从工程 trick 变成了采样逻辑。扩散模型不是寻找唯一最可能图像，而是在高维数据分布中采样；随机性不是失败，而是生成多样性和清晰度的一部分。

## 5. 11:43-21:51：score/vector field 是理解扩散的核心图像

![Score vector field](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/11-score-vector-field.jpg)

视频最有价值的部分，是把扩散模型解释成学习一个随时间变化的向量场。为了可视化，它把图像空间降到二维：每张图像被看成高维空间里的一个点，而训练数据形成某种结构，比如一条螺旋。

![Random walk Brownian motion](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/12-random-walk-brownian-motion.jpg)

给图像加噪声，在这个二维 toy world 里就像让点做随机游走。这正是扩散模型和 Brownian motion 的关系：前向过程把结构化数据打散成随机点云，反向过程则要学会如何把点云拉回数据结构。

模型学到的不是一张固定模板，而是每个位置上“应该往哪里走”的方向。离数据分布很远时，方向比较粗，只能指向大体区域；靠近数据分布时，方向变得细，可以指向更精确的结构。

![Time conditioned score field](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/13-time-conditioned-score-field.jpg)

因此时间条件很关键。同一个位置在不同噪声水平下应该有不同的方向：高噪声阶段需要粗略回到整体分布，低噪声阶段需要对齐细节。视频里说这个向量场在某些阶段像“相变”一样，从指向中心变成指向螺旋结构本身。这给 DDPM 的时间变量提供了直观解释。

## 6. 21:51-25:13：DDIM 和 flow matching 说明“同一分布可以用不同路径到达”

![DDIM deterministic trajectory](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/14-ddim-deterministic-trajectory.jpg)

DDPM 的问题是慢，因为每一步都要调用一次大模型。视频随后引入 DDIM 和相关的 flow-based/flow matching 视角。核心不是重新训练一个新模型，而是改变采样路径：不一定每一步都加随机噪声，也可以通过确定性的轨迹到达相同的最终分布。

这里的关键区别是：DDPM 的反向过程像随机动力系统，DDIM 则像沿着一个确定性轨迹走。理论上它们不要求每个样本逐点相同，只要求最终样本分布对应。工程意义很大，因为这让生成可以用更少步数完成。

这段也把现代视频模型接上了前文。WAN 2.1 使用的不是最原始的 DDPM，而是更接近 DDIM/flow matching 的路线。也就是说，今天的视频生成并不是简单把 2020 年 DDPM 放大，而是在采样路径和动力系统表述上做了很多改进。

## 7. 25:13-28:03：文本怎样真正进入扩散模型

![CLIP text image bridge](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/15-clip-text-image-bridge.jpg)

到这里，视频已经有了两个组件：CLIP 这类模型能把 prompt 变成语义向量，扩散模型能从噪声回到图像分布。下一步就是把两者接起来。直观想法是：让文本向量参与反向扩散过程，使模型不只是生成“像图像的东西”，而是生成“像 prompt 所描述的东西”。

![UnCLIP diffusion inverts CLIP](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/16-unclip-diffusion-inverts-clip.jpg)

DALL-E 2 的 UnCLIP 路线可以看成让 diffusion 去反转 CLIP image embedding。CLIP 把图像压进 embedding，UnCLIP 则尝试从 embedding 生成图像。这说明文本和图像共享空间不只是分类工具，也可以成为生成模型的控制接口。

![Text conditioning diffusion model](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/17-text-conditioning-diffusion-model.jpg)

conditioning 的基本做法是把文本向量作为额外输入交给扩散模型。模型训练时看到图像和 caption 配对，于是学会利用文本信息更准确地去噪。这里和前面的 time conditioning 是同一种思想：模型不只看当前噪声状态，还看额外条件，从而学到不同的向量场。

## 8. 27:39-33:59：仅有 conditioning 不够，guidance 才让 prompt 变硬

![Classifier-free guidance vector fields](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/18-classifier-free-guidance-vector-fields.jpg)

视频后半段最关键的转折是：conditioning alone 不够。只把 prompt 传给模型，模型可能生成符合大体语境但漏掉核心对象。它知道“沙漠”和“阴影”，却可能没有真正生成“树”。

![Conditioning only fails tree prompt](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/19-conditioning-only-fails-tree-prompt.jpg)

classifier-free guidance 的直觉是把两个方向拆开：一个是不带文本条件时“回到一般真实图像”的方向，一个是带文本条件时“回到符合 prompt 的真实图像”的方向。两者相减后，得到的差异方向就更像“prompt 额外要求的东西”。再把这个差异方向放大，模型就更强地朝 prompt 指定的语义区域移动。

![Guidance scale WAN output](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/20-guidance-scale-wan-output.jpg)

guidance scale 控制的就是这种额外语义方向的放大强度。视频用树的例子说明，scale 增大时，树从几乎不存在逐步变得清晰。这个现象很有解释力：prompt adherence 不是简单来自文本输入，而是来自对“条件方向”和“一般图像方向”的差分放大。

## 9. 33:37-35:27：negative prompt 是 guidance 的反向使用

![Negative prompt guidance](../../slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/curated/21-negative-prompt-guidance.jpg)

最后，视频把 classifier-free guidance 推到 video generation。WAN 2.1 使用 negative prompt：它把“不想要的特征”也写成文本，例如 extra fingers、blurred details、walking backwards 等，再让模型远离这些方向。

这说明 prompt 控制不是只有正向描述。现代生成模型同时使用正向吸引和负向排斥：正向 prompt 告诉模型往哪里去，negative prompt 告诉模型远离哪些视觉失败模式。对视频来说这尤其重要，因为视频不仅要每帧清晰，还要运动连贯、身体结构稳定、时序不崩。

视频的结尾把所有部件重新合起来：语言通过 embedding 进入模型，扩散/flow 模型把噪声推回真实数据分布，guidance 把这个推回过程偏向 prompt 所描述的区域。于是图像和视频生成看起来像“语言创造视觉”，但内部机制更准确地说，是语言在高维采样过程中改变向量场和采样路径。

## 读这期视频时要抓住的一条线

这期可以和 Welch Labs 的 `How Models Learn` 系列连起来看。`How Models Learn` 解释神经网络如何通过 loss、backprop 和深层非线性学函数；这期则进一步解释，现代生成模型学到的函数不只是分类边界，而是一个可以在高维空间中引导采样的方向场。

它也和 3Blue1Brown 的 entropy/compression 线有关。生成不是从离散记忆里复制样本，而是在被模型压缩过的概率结构中采样。prompt 的作用，是在这个概率结构里施加条件，让随机噪声沿着更特定的语义方向展开成图像或视频。

最值得保留的直觉是：扩散模型不是“会画画的黑箱”，而是一个学会把噪声点拉回数据分布的动态系统；CLIP/text encoder 给这个系统提供语义坐标；guidance 把语义坐标变成更强的采样方向。

