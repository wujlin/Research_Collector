---
title: "A Functional Taxonomy of World Models"
source_type: "web_article"
publisher: "Dr. Fei-Fei Li / Substack"
author: "Fei-Fei Li"
published: "2026-06-03"
collected: "2026-06-05"
url: "https://drfeifei.substack.com/p/a-functional-taxonomy-of-world-models"
mirror_url: "https://www.a16z.news/p/a-functional-taxonomy-of-world-models"
status: "collected"
topics:
  - world_models/functional_taxonomy
  - spatial_intelligence
  - robotics/simulation
---

# A Functional Taxonomy of World Models

## 采集定位

Fei-Fei Li 这篇文章的目标是给“world model”降噪。现在 computer vision、robotics、reinforcement learning、generative AI 都在使用这个词，但它们常常指向完全不同的系统：能生成漂亮视频的模型、能让机器人规划动作的模型、能做物理仿真的 engine，都可能被叫作 world model。

文章的处理方式不是争一个唯一正确定义，而是回到 agent 与 world 的交互循环：agent 执行动作，动作改变 world state，agent 只能收到 partial observations，然后根据新 observations 再行动。这个 POMDP 语境让 world model 不再只是一个营销词，而是可以按功能拆成三类输出：observation、state、action。

## 文章主线

文章先用一个判断开场：世界不是由文字构成的。语言模型学到了文本结构，但物理世界运行在空间和时间里。空间智能需要模型理解光如何落在表面上、物体如何受力、场景从未见过的视角看起来如何、结构如何在动作下变化。

接着文章指出，“world”本来就不是单一对象。不同领域把它当作自己需要推理的总体现实，于是 AI 继承了这个多义性。要消除混乱，需要先明确 agent-world loop：state 是世界在某一时刻的完整真实状态，observation 是 agent 能看到的局部投影，action 是 agent 对世界施加的改变。

基于这条 loop，文章给出三类 world model。

第一类是 renderer。renderer 输出 observation，也就是给人看的像素或视频。它追求 visual fidelity，可以生成漂亮的视角、场景和动态画面，但不保证背后有可计算的三维结构或物理一致性。一个空中俯瞰城市的视频看起来可能很真实，但如果要开车穿过那座城市，建筑、道路和尺度可能马上崩掉。

第二类是 simulator。simulator 输出 state，也就是几何、物理、动力学上可检查、可交互、可计算的结构。它不仅要让人看起来可信，还要让建筑师、设计师、游戏开发者、机器人控制器、自动驾驶系统能在其中进行操作、测试和训练。这里的标准不再是“像不像”，而是结构能不能经得住行动和计算。

第三类是 planner。planner 输出 action。给定 observation 和 goal，它回答 agent 下一步应该做什么。文章把 planner 说成 renderer 的反向：renderer 接收某种 action 或条件，输出 observation；planner 接收 observation 和 goal，输出 action，从而闭合 perception-action loop。VLA、model-based systems 和 World Action Models 都属于这条线。

## 为什么 simulation 是中轴

文章最关键的判断是：三类模型里，simulator 最不受公众关注，却最关键。

renderer 商业化最成熟，因为互联网视频和图片数据丰富，视觉质量也容易被用户感知。但 renderer 的天花板是 visual plausibility，它不能直接替代工程设计、机器人训练或高保真物理推演。

planner 最令人兴奋，但还很早期。机器人 demo 在过去两年进展很快，但大多还局限在受控实验室、短 horizon、窄 object set 和可展示任务里。真正部署到厨房、仓库、手术室这类复杂空间，还差很远。

simulator 正好连接两者。如果语言是世界的抽象，像素是世界的投影，那么 geometry、physics 和 dynamics 更接近可操作的世界本身。一个模型如果掌握 simulation，就可以向下投影成 renderer 给人看，也可以向上支撑 planner 预测行动后果。只会渲染或只会规划，都缺少这个结构骨架。

困难也集中在这里。显式 3D geometry、material properties、physical annotations 和 robot demonstrations 远比互联网视频稀缺。sim-to-real gap 仍然存在。生成式 simulator 还会引入新风险：几何看起来正确，但可能有自交、尺度错误或无法承载物理计算。多物理场仿真更是昂贵得多。

World Labs 的 Marble 被文章放在这个语境里：它从文本、图像、视频或空间草图生成可探索的 3D 环境，同时输出用于视觉探索的 Gaussian splats 和可被 physics engine 操作的 collision meshes。这个例子服务于文章主线：renderer 和 simulator 的边界正在塌缩。

## 结尾判断

文章最后把趋势总结为三类功能的合流。一个真正理解杯子如何放在桌上的模型，原则上应该能从任意角度渲染杯子，模拟杯子被推后的变化，也能规划机械手去拿起杯子。renderer、simulator、planner 是同一个底层 world understanding 的三种投影。

终点是 unified world model：同一个 foundation model 能根据下游消费者需要，在 photorealistic view、physically accurate structure 和 action sequence 之间切换。但文章也很清楚地指出，视觉美感、物理精度、机器人可用性之间存在张力。把这些目标放进一个架构里，是 world model 研究的核心开放问题。

## 与本项目的连接

这篇文章和 LeCun/JEPA、VLA robot brain、David Ha world models 可以组成一个小型对照组。

Fei-Fei Li 的分类强调 functional outputs：renderer 输出 observation，simulator 输出 state，planner 输出 action。LeCun 的 JEPA 强调 latent prediction and planning，最关心的是 action-conditioned consequence prediction。VLA 路线则更接近直接从 observation-language 到 action 的 planner，虽然它内部也借助视觉语言表征。

对 synthetic city 方向，simulator 这个中轴尤其有启发。城市生成不能只追求表面像真实数据，也不能只输出一个 action policy。更有价值的中间层可能是可被约束、可被检查、可被下游规划或干预使用的 city state representation。
