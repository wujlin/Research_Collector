# Welch Labs: Inside the World's Smartest Robot Brain [VLA]

- Video: [Inside the World's Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)
- Channel: Welch Labs
- Duration: 35:02
- Transcript: `youtube/transcripts/2mrGMMmrVNE-inside-the-worlds-smartest-robot-brain-vla/`
- Slides: `youtube/slides/2mrGMMmrVNE-inside-the-worlds-smartest-robot-brain-vla/semantic_curated/`

这期视频讲 VLA 的代表路线，尤其是 Google RT-2 到 Physical Intelligence Pi Zero 的演化。它的主线不是“机器人 demo 很酷”，而是解释为什么把 vision、language 和 action 放进同一个模型，会让互联网规模预训练知识第一次真正接到机器人动作上。

## 1. 00:00-03:39：从 SayCan 到 RT-1，早期路线是 LLM planner 加控制器

视频从 Google 2023 年的 Coke can / Taylor Swift demo 开始。表面看这个 demo 很笨拙，机器人只是把可乐罐挪到一张 Taylor Swift 图片上；但它的意义在于，机器人控制数据里没有 Taylor Swift，模型必须把互联网预训练里学到的概念连接到真实动作。

在此之前，Google 的 SayCan 系统已经用 LLM 做高层规划。LLM 把“清理洒出的东西”拆成找海绵、拿海绵、走到污渍旁等子任务。但底层控制仍然由单独训练的 imitation controller 完成，LLM 只能从已有 action menu 里选。

RT-1 改进了底层控制器：使用更大的 transformer 架构和大量 human demonstrations，让机器人能执行更多动作。它让 LLM planner 的 action menu 变大，但系统仍然是两层：语言模型规划，控制模型执行。

## 2. 03:36-08:40：PaLM-E 和 RT-2 把 planner、vision 和 action 拉到同一个模型里

SayCan 使用的 PaLM 是 text-only planner，规划层本身看不见世界。PaLM-E 让语言模型直接接收图像和其他传感信息，于是高层 planner 可以根据视觉变化调整计划，例如发现目标物体被挪走后重新规划。

但 PaLM-E 加 RT-1 仍然是两个模型。RT-2 的关键大胆之处，是把 multimodal LLM 进一步训练成能直接输出 robot control signals 的模型。也就是说，LLM 不只是说下一句话，也不只是说下一步子任务，而是直接成为 vision-language-action model。

Taylor Swift demo 的意义就在这里：RT-2 把 internet-scale 视觉语言知识和 robot demonstrations 连接起来。它说明模型可以把预训练中关于人物、物体、语义关系的知识迁移到动作选择中。这个结论支撑了后来的 Physical Intelligence 路线。

## 3. 09:58-13:40：Pi Zero 的关键不是更大，而是 action expert

Physical Intelligence 的 Pi Zero 看起来比 RT-2 强很多，但参数量更小。RT-2 家族有 5B 到 55B 参数，Pi Zero 约 3.3B，并且能在机器人本地的 RTX 4090 上以较低延迟运行。

Pi Zero 建在 PaliGemma 上。PaliGemma 本身由 SigLIP image encoder 和 Gemma LLM 组成，能处理图像和语言。按 RT-2 思路，可以直接微调 PaliGemma 输出控制值。但 Pi Zero 加了一个 action expert：一个和 Gemma 架构相似、但随机初始化且更窄的 transformer，用来专门生成动作轨迹。

这不是回到 SayCan 的“自然语言 planner 加控制器”。SayCan 两层之间的接口是离散文本子任务；Pi Zero 的 Gemma 和 action expert 之间共享 transformer 式内部接口，可以通过 attention 的 keys/values 交换丰富表征。它保留模块化，却不是用自然语言把系统割裂开。

## 4. 13:37-20:56：Gemma 负责把图像和 prompt 组织成可用表示

Pi Zero 接收多路相机图像和文本 prompt。图像被切成 patch，每个 patch 经过 image encoder 变成 embedding vector；文本 prompt 也被 tokenized 成 embedding。所有这些 soft tokens 被送进 Gemma LLM。

视频用 attention head 解释 Gemma 如何把语言和视觉接起来。以 prompt 里的 “pen” 为例，某个 attention head 会拿 pen token 的 query 去和图像 patch 的 keys 做匹配。可视化显示，最高 attention 落在图像中真正包含 pen 的 patch 上。

这个例子很重要，因为它说明 VLA 不是简单把图片和文字拼起来。transformer attention 在内部形成了“prompt 中的对象词”和“图像里的对象区域”之间的信息通道。后续 action expert 需要的场景知识，就在这些中间表示里。

## 5. 20:55-28:32：action expert 用 flow matching 生成未来动作轨迹

action expert 接收机器人当前关节状态，以及未来动作轨迹的随机初始版本。以 ALOHA 双臂平台为例，两个手臂共 14 个控制维度，Pi Zero 要生成未来 50 个时间步的动作，所以动作可以看成一个 14 x 50 的矩阵。

这听起来像图像生成。扩散或 flow matching 模型从噪声图像逐步生成猫图；Pi Zero 的 action expert 从随机动作轨迹逐步生成可执行的关节轨迹。每一步预测如何把随机轨迹往更合理、更符合任务的方向推，重复若干次后得到最终控制计划。

关键问题是 action expert 怎么知道该生成什么动作。答案是 cross-attention 式接口：Gemma 处理图像和 prompt 后，每层 attention head 的 keys 和 values 被缓存；action expert 在对应 attention head 中把自己的 keys/values 和 Gemma 的 keys/values 拼接起来。于是 action trajectory token 可以直接查询场景和语言信息。

这也是 Pi Zero 架构最巧的地方。Gemma 的 KV cache 被反复复用，action expert 在 flow matching 的多次迭代中不需要重复处理图像和文本。系统每个控制 step 都先处理观测和 prompt，再用 action expert 把噪声轨迹 refine 成动作，执行几步后重新观测。

## 6. 28:30-30:44：VLA 的强处和未解问题

视频最后提醒：这些 demo 很强，但仍然是 demo。1995 年的自动驾驶系统 Ralph 也曾经横穿美国大部分路程，但并不意味着自动驾驶马上成熟。机器人同样可能经历很长的从 demo 到可靠部署的过程。

更重要的是，VLA 正面临另一条路线的挑战：world model。LeCun 认为 VLA 缺少显式预测动作后果的能力，只是从 observation 和 language 直接生成 action。下一期视频正是围绕 JEPA world model 展开。

因此，这篇笔记应和 `welch-labs-yann-lecun-can-reshape-ai-again.md` 配对读。VLA 展示了语言预训练知识如何进入机器人控制；JEPA 则追问，如果没有可 roll out 的 world model，这种控制是否足够可靠、可规划、可扩展。
