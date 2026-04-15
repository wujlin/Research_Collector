# LLM Audit: 对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷、反OpenAI、AMI Labs、两次拒绝Ilya、杨立昆、李飞飞和42

- Model: `Qwen3-8B`
- Base URL: `http://127.0.0.1:18082/v1`
- Audited at: `2026-04-15T22:37:24`
- Paragraphs: `596`
- `ok / needs_review / uncertain / error = 429 / 133 / 0 / 34`

## Flagged Paragraphs

### [06:43 - 07:36] #8 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `为负心词强说愁`

**Original**

虽然也是很开阔的 但到网上当初有这些BBS 然后你可以上网去发表意见 我还记得了吧有有这种新浪博客啊 现在可能都没有了 但我写了很多很多的博客 哦是吗 关于各种各样的乱七八糟的topic 现在对现在肯定回头看过去都会都会很好笑 但是最popular的一篇文章是什么呀 很多吧 我觉得我记得 有点有点 为负心词强说愁的感觉吧 嗯 可能那时候包括QQ空间对吧 大家总会有一个想要有一个平台去去表达自己 然后后面其实还有更多的这种新兴的媒介出现 包括有博客 然后有有有微博对吧 但那时候其实不是微博是泛否 不知道听没听说过

**Suggested**

为赋新词强说愁

**Reason**

明显错别字，'负心词'应为'赋新词'

### [07:36 - 08:29] #9 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `泛否`

**Original**

是王兴对吧 然后那时候我也是泛否的众多用户啊 啊上面 呃泛否现在还能登录 但是实在是不忍直视啊 有时候看了看 我想哎呀要不要赶紧删掉啊 最后想一下还是留在那吧啊 让它变成这个互联网基地的一部分 嗯 但是我觉得那时候呃 我觉得我觉得这种互联网的爆炸式的增长 让我变成了一个对很多事情都很感兴趣的人 嗯 嗯 我觉得是这样 所以你爸爸妈妈你妈妈是做生意的 你们是一个商人家庭吗 也不是也不是呃 对啊 反正我爸爸基本上也是他 他是本科是学心理学的啊 他也之前也从事一些教育工作 啊 后来也在一些呃这种电视台上的传媒工作 哦

**Suggested**

饭否

**Reason**

疑似错别字，'泛否'应为'饭否'，为知名网站名称

### [09:53 - 10:36] #12 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `ACM这样的一个计划`

**Original**

最多是一个B class的这样的一个trajectory 哦 啊 你像你像 而且很多我的这些决策其实还是蛮玄学的 因为我觉得我并没有 刻意的 在某种 这种幽寂主义的这种这种这种这种setting下框架下面 去努力追求一些事情 很多时候其实还是挺随机的 啊 然后可能也是这个没办法啊 这个智商不够 但是确实比如说像保送的时候对吧 这个也是很偶然 然后反正有有两个呃这种心理学跟数学的竞赛的奖 然后这时候恰好交大有这么一个 呃计划 就是说可以提前进校啊 就是想收割一些同学 然后让大家不要去高考

**Suggested**

ACM班这样的一个计划

**Reason**

ACM通常指一个班级或项目，应为 'ACM班'，而非 'ACM这样的一个计划'。

### [10:36 - 11:23] #13 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `提前进校进去之后`

**Original**

对其实我当初还是蛮顺着高考的这个框架去培养 其实我呃本身应该是应该是要去参加高考的 嗯啊 所以当当初还纠结了很很长一段时间 学校老师都会说 啊 这个不行啊 你怎么能这个临阵脱逃呢 你已经你看你的成绩也很好 对吧啊 你当然应该冲一冲清华北大啊 然后我的内心想法是 哎呀 交大挺好 我觉得我去我去上海也待过 我觉得我跟这个城市跟这个学校都气质相投 并且我就是想学计算机 然后我觉得交大那个时候 计算机也很不错啊 我也听说过有ACM这样的一个计划 虽然那时候这个选拔的过程 其实是要到啊 你你提前进校进去之后

**Suggested**

提前进校之后

**Reason**

重复使用 '进去'，属于口语赘词，应删除以保持语义清晰。

### [15:14 - 16:04] #19 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `a三班`

**Original**

然后到后面申请其实也是一样 我觉得啊 嗯 或者从另外一个角度来来说这件事吧 我觉得 我觉得好像这个世界总是不想让我去做我想做的事情 但是但是我偏偏要做我想做的事情啊 啊 比如说本科的时候 我一开始就对计算机视觉对吧 或者说对人工智能产生了一些兴趣 啊 那时候也是刚开始就是在a三班 大家会在大二开始进行这种这种科研 实习 然后会到这个学校里面的不同实验室里面去 然后我去的这个实验室就是一个做啊 神经科学加ai的这样一个实验室啊 叫bcmi 然后书架上放着很多很多关于意识 关于大脑 关于图像啊

**Suggested**

A3班

**Reason**

“a三班”应为“A3班”，符合专业术语的英文缩写格式

### [19:15 - 19:56] #24 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `这个这个实验室; google chat`

**Original**

所以我跟他是在 因为他也是这个这个实验室毕业的 所以我跟他相当于在网上沟通 呃 何小迪当初是在这个加州理工 然后就已经读phd了 对他也申请到了很好的学校 然后我们都非常非常羡慕啊 在那个时候 然后我跟他还是会在这个当初是在google chat上 然后跟他聊很多很多的话 然后他真的是也是啊 给了我很多很多的建议吧 对 现在还记得有什么建议啊 呃 没有更多的时候在网上跟他聊的时候 更多是聊research 对到底应该做什么事情 嗯 跟他讲一下我自己的迷茫啊 然后呃 然后怎么样怎么样能够发出来一篇论文吧

**Suggested**

这个实验室

**Reason**

重复用词'这个这个'属于口语冗余，但'google chat'可能是'Google Chat'的误写，需确认是否为专有名词

### [19:56 - 20:38] #25 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `vue的信息`

**Original**

大概向他取取经 对 然后那时候 但那个时候我觉得通过小迪 然后通过我看的这些书已经基本上确定了 我觉得我这辈子就想做这个事啊 我觉得这件事情可太有意思了 嗯 那时候其实并没有这样一个名字在那 或者说慢慢开始有计算机视觉这样一个一个terminology 但其实之前对吧 然后大家去处理图像或者vue的信息已经很长时间了 比如大家会做所谓image processing 就是图像处理啊 呃 更多的是从这种we的major开始的 对 然后计算机视觉可能是啊 呃 慢慢变得更加更加popular 嗯

**Suggested**

视觉的信息

**Reason**

'vue'可能是'vision'的误听，'计算机视觉'是专业术语，应为'视觉'而非'vue'

### [20:38 - 21:23] #26 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `Microsoft呃 Research就是亚研院`

**Original**

然后也也就是我开始学习这些之后的这些知识的时候吧 它开始变得越来越popular 对 然后呃 我总说这个世界总不想让我们做这件事情 是因为在呃交大一三班的时候 其实还有另外一个特点是这个班里的每个学学生 在大三的时候都要出去实习一次 嗯 现在其实也蛮常规的 但其实在当时还是就是这个班的主要的这个这个发起人 叫渔泳老师啊 他的一个创举 所以那时候大部分人就是A3班会跟这个Microsoft呃 Research就是亚研院有这么一个合作的一个项目 所以会把我们的很多学生送过去 然后做一个大概呃六个月的这样一个实习 对

**Suggested**

Microsoft Research就是亚研院

**Reason**

‘呃’字夹在专有名词中间，破坏了专有名词的完整性，应删除。

### [21:23 - 22:06] #27 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `马毅老师啊 孙建老师`

**Original**

所以呃 我的当初的就是如果我什么都不做的话 我就会去亚研院实习 对 虽然也很好 但那时候呃 其实没有一个实习的机会 所以呃 我的当初的就是如果我什么都不做的话 其实没有一个做视觉的组 愿意接受A3班的本科生去实习 哦 为什么呀 呃 我不知道 可能是因为当初你像马毅老师啊 孙建老师都在那边啊 凯明的时候应该也在那边了 然后我觉得他们可能不喜欢有太多的这些啥也不懂的本科生 哦 过来参与这些事情 对吧 他那个他们那个时候非常的人才济济 是的 是的 是的 没错 但但我们真的是什么也不懂 对吧 但那时候呃

**Suggested**

马毅老师 孙建老师

**Reason**

‘啊’字夹在人名中间，破坏了人名的完整性，应删除。

### [22:06 - 22:43] #28 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `小迪一师兄`

**Original**

有一个选择就是还是去MSRA 但是就不要做什么跟视觉相关的这些research了 啊 然后于老师也跟我说说 哎呀 其实你们本科生啊 现在最重要的还是有一段研究的经历 学会怎么样做研究啊 呃 具体做什么样的这个方向不重要 方向不是很重要 嗯 对 呃 但我觉得不行啊 我觉得我没办法接受我去做一个完全不一样的一个一个方向 我希望 对这个领域了解的更多 我希望能够踏踏实实的啊 做一些事情 然后希望有朝一日能像小迪一师兄一样啊 能够发一篇CVPR的论文 对 这是我当初的这个 小迪那时候就已经是你的偶像了是吗 有点有点

**Suggested**

小迪师兄

**Reason**

‘小迪一师兄’表述不自然，可能是‘小迪师兄’的误听或误写。

### [22:43 - 23:29] #29 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `严水城老师`

**Original**

他他是很多人的偶像 对 在加拿大的时候 哦 呃 然后 所以我就开始琢磨这个事情怎么办 啊 然后就开始发邮件 所以联系了这个新加坡的NUS 是吧 啊 新加坡国立大学的 呃 新加坡国立大学的 呃 呃 呃 呃 是吧 新加坡国立大学的 呃 严水城老师的这个实验室 嗯 对 啊 这件事情是完全我自己联系的 也没有也没有告诉于老师啊 然后等到敲定说哎 我可以有这么一个实习的机会 啊 然后他那边已经有一些 呃 补贴 然后说什么时间什么样的这些这些这些架构已经都 啊 比较完善了 然后我就去找于老师 我说 于老师

**Suggested**

严水城教授

**Reason**

‘严水城老师’可能为‘严水城教授’的误听，根据学术场合的称呼习惯更可能是‘教授’。

### [24:11 - 24:54] #31 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `take some initiative`

**Original**

这个地方到底靠不靠谱 你要做的事情靠不靠谱 啊 这件事情可能是不可控的 你纠结过吗 我我没有纠结 但但于老师 我觉得我也非常appreciate他 就是他反而反而沉默了几秒 最后说 好 啊 你去吧 对 呃 然后我就去了 呃 但是这件事情啊 发生了之后 像 我从这个组AOS的这个实验室 变成了我学弟学妹之后的 一个 可选择的一个一个一个一个position 嗯 对啊 所以我觉得啊 对 所以我觉得我还是想take一些主观能动性吧 我觉得take一些initiative 然后去做我自己想做的事情 对 在当时还非常早期

**Suggested**

采取一些主动性

**Reason**

‘take some initiative’为英文表达，中文转写应为‘采取一些主动性’以保持语义准确

### [24:54 - 25:42] #32 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `那那我不能看动画片 我我也不能看电影 我也不能打游戏了`

**Original**

就是和图像相关的人工智能到底吸引你的事是什么呀 嗯 他为什么吸引了你呢 让你做出了很多不一样的选择 因为我觉得我感受这个世界的方式就是通过视觉 嗯 我会想 我小时候可能也比较无聊吧 我就会想哎 人有这么多对吧 感官啊 如果非要让我让我去掉一个的话 会去掉哪个 我觉得 也许我听不见 也许我没法说话 也许我没有触觉 没有嗅觉啊 我会过得很悲惨 但可能还可以接受 但如果我没没有了视觉啊 那那我不能看动画片 我我也不能看电影 我也不能打游戏了 我似乎是丧失了一个人的独立性 然后我觉得当然这件事情

**Suggested**

那我不能看动画片 我也不能看电影 我也不能打游戏了

**Reason**

重复的'那'字造成语义漂移，应删除重复的'那'

### [25:42 - 26:28] #33 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `所有的人都是视觉动物 啊 然后这件事情 对 我我是这么觉得的 我也是一个视觉动物`

**Original**

这些最开始的想法和后来我看到的一些书里面 呃 讲的事情我觉得也蛮不谋而合的吧 嗯 因为你想想视觉信号 其实占了人的大脑这个批层 呃 看你怎么说的吧 就主要的视觉区域可能有百分之 呃 百分之三十占这个大脑 但呃整个大脑在你看到这个图像的时候 啊激活的部分可能要占到百分之七十 嗯 对吧 所以其实我们所有的人都是视觉动物 啊 然后这件事情 对 我我是这么觉得的 我也是一个视觉动物 我也很喜欢啊 看一些东西 对 生物也是 而不是听不是读 不只是人 不只是人对你说的非常非常对 嗯 所有的东其实不完全是这样

**Suggested**

所有的人都是视觉动物 然后这件事情 我是这么觉得的 我也是一个视觉动物

**Reason**

语气词'啊'和重复的'对 我我'造成语义漂移，应删除多余语气词

### [27:19 - 28:05] #35 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `一个立定的siri`

**Original**

这个这个视觉 对吧 因为因为如果你不有更强的视觉的话 你就会被吃掉 是吧 所以就展展开了一场军备竞赛 呃 所以这是所谓的韩武纪大爆发啊 啊 所谓的堪贝尔 就是说地球上在这个韩武纪之前 可能只有屈指可数的这些物种 但是过了韩武纪之后 突然到大爆炸式的多了几十万种这种物种啊 一个立定的siri 就一个一个理论 其实是说这种大爆炸的呃来源 其实就是因为大家在视觉层面展展开了这种军备竞赛 是的是的 嗯 所以所以你说的完全对 我觉得我觉得这其实是不是一个人特有的事情 我觉得所有的动物其实也是这样 嗯

**Suggested**

一个理论

**Reason**

‘一个立定的siri’是明显误听或误读，应为‘一个理论’。

### [30:25 - 31:04] #39 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `bmvc的paper`

**Original**

这个我的mentor是冯家石 啊 他当初是这个phd 学生 对 然后他带着我然后做了一些工作啊 我们发表了一篇 也不是顶会很不幸 本科还是没能发出一篇cvpr 嗯 但但发发表了一篇啊 还不错的这个bmvc的paper 对是一个是一个没那么顶会的计算机视觉的 这样一个论文 所以 呃 我觉得我觉得还是有很大很大的收获 我我第一次知道了 呃 research是怎么回事对吧 真正写过一篇paper跟没写这篇paper 我觉得还是差别还是很大 那是你关于cv的第一篇paper 是的是的

**Suggested**

BMVC的论文

**Reason**

‘paper’ 应修正为更正式的‘论文’，且‘BMVC’ 应大写

### [31:04 - 31:45] #40 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `alex that moment`

**Original**

但你可以认为这是一个关于cv的paper 但其实跟cv也没有什么关系啊 它的唯一的一个application 是这个人脸识别 对它更像是一个机器学习的论文吧 啊 但那时候也很正常 所有在 学cv或者说研究cv的人都在做类似的事情啊 所谓的这些 呃 这这这种manifold clustering相关的东西 对 呃 但是也就是在那个时间点上 呃 那是2012年2013年2012年对吧 所以刚好也是alex that moment 嗯 所以 我也是在那个时间点上啊 知道了这件事 对吧 然后对 然后知道了image net

**Suggested**

AlexNet that moment

**Reason**

‘alex that moment’ 可能是 ‘AlexNet that moment’ 的误听，AlexNet 是一个著名的深度学习模型，与 2012 年 ImageNet 竞赛相关。

### [39:06 - 39:51] #51 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `searchblondie`

**Original**

包括这种师资的储备ai的 呃 这种力量来看 我觉得ucsd都已经是前几名的这种 这种级别了 在当初完全不是这样 在当初 而且我其实还一直很想合作一个老师 叫searchblondie 他刚刚决定也要跳槽离开ucsd 啊 所以我觉得一切都很绝望啊 就是我要去的地方似乎排名也没那么高 呃 然后 狮子也在外流 狮子也在外流 但我想想说这个都不matter 都不重要 重要的事情 是我跟谁在做什么事情 然后这件事情是不是我想做的事情 啊 我觉得 抛开所有这些噪音 这是我唯一一个想要去关心的事情 嗯 这个很有趣 对嗯

**Suggested**

searchblonde

**Reason**

疑似人名错误，'searchblondie' 可能为 'searchblonde'，需确认正确拼写。

### [41:55 - 42:37] #55 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `pytor`

**Original**

其实对后面的这个计算机视觉有重要影响的工作 都是他独立 单个作者完成的工作 啊 然后这些工作 没有什么像现在一样 大家用pytor 是有这么多这些开阅的工作 啊 在别人的社区 有这么多的这些库你可以调用 对吧 有GPU 啊 在他那个时候什么都没有 他要从底层开始写起 比如说他要做 图像分割这样一个task 他要从头写起 大概有五万行的这样一个代码 他还把这个代码发给我看过 啊 那这个包含的最底层的 啊 这些这些包括一些distributed training啊 一系列的这些东西啊 全都是C++写的 对 五万行代码

**Suggested**

PyTorch

**Reason**

pytor 是 PyTorch 的误听，PyTorch 是一个广泛使用的深度学习框架，符合上下文语义

### [47:09 - 47:51] #62 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `deeply-supervised nets`

**Original**

然后现在deeply-supervised nets 就是说你现在其实可以有multiple的branch 就是说你的一个神经网络 其实可以有多个出口 你在不同的出口上 你都可以施加一个监督信号 这样的话 一个最直接的一个好处 就是说你可以啊 不止从最远端的这个信号 做backpropagation 回到呃之前的early的这个layers 反向传播 对你你你你不需要从最远端做反向传播 一路到最最头 啊 你其实可以从中间的一个节点做反向传播 这样可以解决一部分这种梯度消失的问题 嗯 然后这件事情其实跟后来

**Suggested**

deeply supervised networks

**Reason**

术语'deeply-supervised nets'应为'deeply supervised networks'，符合英文术语规范。

### [48:26 - 49:07] #64 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `pixel labeling`

**Original**

就是一个做边缘检测的工作 HED HED 对啊 我觉得我对这篇工作其实也蛮蛮骄傲的 因为这件事情 说白了把把一个research问题解决了 啊 呃 既是一种幸运也是一种不幸 就是幸运的是说这篇论文是一个不错的论文 不幸的事情是 当这个问题已经解决了之后 那没人后面没人做 所以也没有人去cite你的论文了 嗯 啊 所以少了很多citation 对啊 但是 呃 但这个工作其实本质上就是一个deeply-supervised nets dsn在一个 呃 图像 呃 或者说边缘检测 但但其实是一个全局的 呃

**Suggested**

pixel-level labeling

**Reason**

术语'pixel labeling'应为更标准的'pixel-level labeling'

### [49:51 - 50:35] #66 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `马尔奖的马尔奖提名`

**Original**

然后越往上你的边缘也就更细致 所以你最后可以把这所有的这些边缘融合到一起 得到一个最贴近于 人的认知下的这种边缘的这样的一个输出的结果 我觉得这件事情其实是 也让我对深度学习有了新的认知 它是一个很有趣很有趣的东西 你可以认为它是一个black box 但这个black box的每一个部分 你又能把它打开 接入一些新的灵感 然后达到一些新的目标 我觉得这件事情对我启发很大 然后这个paper当初 对我的人生影响也很大 是因为它 这个是发表在ICCV 然后也得到了一个奖 这个奖是这个马尔奖 就是其实最佳论文奖的提名

**Suggested**

马尔奖的提名

**Reason**

重复使用'马尔奖'显得冗余，且'马尔奖提名'已明确指代，无需重复

### [50:35 - 51:17] #67 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `best paper`

**Original**

还不是最佳论文奖 只是一个提名 但其实这个对于马尔奖来说 就是它评选两个论文了 就是相当于马尔奖的马尔奖提名 是两个奖项 所以这件事情让我觉得 你要说什么一鸣惊人 我当初确实觉得 你看我也是年少成名了 就现在当然我们有很多这种 这种中国学生 也在这种世界的舞台上 得的这些best paper可太多了 对吧 但当初对我来说 走上那个舞台 或者那个讲台吧 然后去给这个award presentation 去给这个talk 我觉得对我的触动是很大 我会觉得 我的这个人生开始了 对吧 然后我会不断的努力

**Suggested**

best paper award

**Reason**

best paper 作为专有名词应完整表达为 best paper award，以符合英语习惯

### [56:03 - 56:50] #74 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `cross-sourcing`

**Original**

然后所有做跟这种传统的机器学习相关工作的人 都集中在Princeton这边 对的 然后后面可以有些可以跳过 但是反正在Adobe我就没做出来 原因是Adobe是一个非常非常 artistic有这种艺术家气质的公司 对的 make sense 然后我在那时候在三番 然后然后做一些跟design相关 跟这种cross-sourcing 就是说你要在互联网上去写一些这种mechanical turk 就是一些互联网的这种用户feedback的这种系统 对吧 然后一些用户反馈系统 然后用它来指导一些机器学习

**Suggested**

cross-domain

**Reason**

cross-sourcing 不是标准术语，更可能为 cross-domain（跨领域）

### [59:56 - 01:00:42] #79 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `rhythm思路`

**Original**

就打这个比赛 然后我说好呀 那我们来打打这个比赛 因为凯明在微软的时候 他做出他这些工作就是靠打ImageNet比赛 对吧 然后一步一步打起来的说吧 然后所以我们也来去玩ImageNet 这个challenge 然后在这个过程中 我们就发现 我们之前想到的一些思路 其实是一个rhythm思路 其实是一个很好的思路 对吧 然后其实这个idea 我propose给凯明 凯明他的魔力在于 他能把所有很普通的东西 变成一个金字般之前的这个idea 对 所以我们做了ResNeXt的工作

**Suggested**

residual思路

**Reason**

根据上下文，'rhythm思路'更可能是'residual思路'的误听，'residual'在ResNeXt中是核心概念。

### [01:04:54 - 01:05:39] #86 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `你为什么要接着去其他地方去游览了呢`

**Original**

我觉得也收获也蛮大 我有一个疑惑 因为你既然在meta跟凯明合作的很好 然后他又是一个鼎鼎大名的AI的researcher 你为什么不留下来继续跟他合作 我觉得很多人可能会这么选择 你为什么要接着去其他地方去游览了呢 这其实是凯明的建议 凯明会建议每个人去不同的地方实习 这样才能有最大化的收获 对 所以像我们当初我啊 包括王小龙啊 大家其实都是实习了一次 然后之后我们当然都愿意留下来 但凯明说你们去其他地方看看吧 也许会有不一样的收获 嗯 但是你博士毕业以后回到了meta 是的对 我觉得还有就是

**Suggested**

你为什么要接着去其他地方去实习呢

**Reason**

语义漂移，'游览'与上下文实习经历不符，应为'实习'。

### [01:06:22 - 01:07:11] #88 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `embody agent`

**Original**

然后衣服帽子的挡都挡不住 一步一步回到我那个窝居的小屋 临时的宿舍 其实还是蛮辛苦的 对 然后但那段时间对我的 我觉得启发也很大 第一让我觉得 我好像不是很喜欢做IL相关的research 或者说我不喜欢做机器人相关的research 机器人 因为其实当初IL其实就是在 在这种虚拟的环境里面 模拟环境里面 去做一些embody agent的task 对 然后但是我觉得我更多的收获 其实是来源于我对DeepMind 这样一个组织的认知 是在那个时候build起来的 我觉得哇这个地方好不一样 跟我去的所有地方都不同 对

**Suggested**

embodied agent

**Reason**

embody agent 是不规范的表达，正确术语应为 embodied agent

### [01:07:11 - 01:07:50] #89 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `这些这些idea`

**Original**

他们会有一个很不一样的管理模式 比如说他们会有很多这些PM 去协调不同的research的team之间的这种运作 他们会有这种不同的working group 大家还是会有很多bottom up的idea 自下而上的这种idea 但是他们又有一种top-down的管理的模式 并且它也是一个层级化的管理模式 一开始纯粹探索性质的这些这些idea 然后大家可以有自己的一个小的group 去做一些early study 然后立刻就会进入一些 如果一旦一个东西成型 立刻就会进入一个更加top-down

**Suggested**

这些idea

**Reason**

重复的'这些'属于口语赘词，不影响语义但应删除

### [01:07:50 - 01:08:31] #90 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `multiple noble prices`

**Original**

更有组织性的这样一个管理的模式下 我觉得这件事情非常有趣 然后现在回想起来 我之前在推特上也跟大家说 就是Demis跟很多intern也都见面 然后大家组织了一个meeting 然后Demis就跟大家说 或者说其实是有人问他这个问题 就是说DeepMind的使命到底是什么 这个公司 你们到底最后想成为一个什么样的公司 Demis的回答是 DeepMind最后会成为一个 能拿multiple noble prices的公司 能获得多个 要划重点 多个诺贝尔奖的公司 我觉得我们当初都说 这个也太ambitious

**Suggested**

多个诺贝尔奖

**Reason**

"multiple noble prices" 是不规范的表达，正确应为 "多个诺贝尔奖"

### [01:09:19 - 01:10:07] #92 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `结构化的鲜艳`

**Original**

我觉得有可能是这样 或者说我觉得我做的东西 可能太多太杂 实习是从博几开始的 就是第一年开始 第一年开始 所以这两个一直是交织的 一直是交织的 对 所以我觉得你说的很对 其实我的时间线其实是被打乱的 对吧 确实会失去一些注意力 但我觉得这也是一个我自己的设计 所以说回回来就是说 怎么把这些事情串起来呢 我觉得我的博士的论文题目是 deep representation learning with induced structural priors 大概就是说一些结构化的鲜艳 用这些鲜艳来指导

**Suggested**

结构化的先验

**Reason**

‘鲜艳’可能是‘先验’的误听，‘结构化的先验’是深度学习领域常见的术语，与上下文中的‘structural priors’对应。

### [01:10:07 - 01:10:44] #93 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `表循环`

**Original**

我们怎样能学到一个更好的深度学习的表征 然后这件事情 again已经过了很多很多年了 但我发现我现在在做的事情还是这件事 并且11月还是12月开会的时候 然后有一个workshop 他们这个workshop title就是说 representation learning with structural priors 大概就是用结构化鲜艳和表循环 大概类似这样的一个topic 然后我再给了一个talk过去 然后我talk到最后我就说 其实过去的12年 你们这个workshop的topic

**Suggested**

表征循环

**Reason**

‘表循环’可能是‘表征循环’的误听，‘表征循环’是深度学习中与表征学习相关的术语，与上下文中的‘representation learning’对应。

### [01:13:01 - 01:13:41] #97 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `我会 我会 我会愿意`

**Original**

再到这个具有良好性质的这个空间的映射的这个函数 这就是所谓的表征学习 对 然后这个函数也不是只是一个简单的映射 它有可能是一个hierarchical层级化的一个映射 对 然后我们现在当然这件事情可以用不同的方式实现 那现在主流的实现的方式那就是用一个 非线性的神经网络来实现这个函数 对 所以我觉得这是一个定义 但我刚说我会 我会 我会愿意 说我自己是做一个representation learning的人 是因为我觉得这是一个永恒的title 就因为这个领域发展太快了 很多时候我们做很多的事情

**Suggested**

我会愿意

**Reason**

原文中'我会 我会 我会愿意'存在明显的重复和停顿，应修正为更通顺的表达

### [01:13:41 - 01:14:20] #98 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `neural architecture search`

**Original**

包括我我举一个例子吧 这个可能是一个非常非常非常native的example 就是以前其实 在我 在我什么时候 可能PhD刚毕业的时候 有个东西非常非常火 叫NAS 叫neural architecture search 就是叫做 神经 架构 这个这个检索吧 我不知道应该怎么翻译 就是neural architecture search 这个领域里面很多的共识就是说这样一个topic 耽误了整个领域大概两年的时间 这是一个错误的方向 大家在这个错误的方向上面发了几千篇论文 但最后没有任何的收获

**Suggested**

神经架构搜索

**Reason**

术语'neural architecture search'的中文翻译应为'神经架构搜索'，而非'神经 架构 这个这个检索'。

### [01:15:04 - 01:15:49] #101 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `type`

**Original**

所以PhD可能讲的有点长了 但是但还要说就是说 我觉得PhD的时候其实也遭受了更多的挫折 包括比如说我们一开始 Deeply Supressed Nets这个论文 这件事情也是一开始 我们投了NeurIPS 得了一个挺高的分数 大概是886还是怎么样 887的一个分数 最后还是被拒搞了 然后这件事情对我来说也是一个打击 我发现 原来发表一篇论文这么难 即使得到了很好的评价 但还是因为一些很离谱的原因 然后被拒搞 离谱是什么 离谱原因是因为我们当初 我们的里面有一个数学公式 它应该是平方 我们有一个type

**Suggested**

type error

**Reason**

‘type’在此处可能是‘type error’的误写，根据上下文推测为数学公式中的类型错误，属于技术术语，需确认是否为正确表达。

### [01:18:17 - 01:18:58] #106 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `何凯明的那个团队`

**Original**

你为什么在每一刻都觉得我不配 我觉得现在好一点 但是可能这个有点夸张了 没有觉得真的不配 但只是觉得比起我的那些peer 他们在既定的轨道上面 像我说的一步一步通向很好的教职 这条路线我觉得我不在这条路线上 或者说你刚说的这件事情也很有道理 如果你最后真的路线是要找一个教职的话 至少在当初那个时间点上 你不应该去5个地方做5个实习 做5个不同的项目 这件事情非常不利于找教职 因为如果你想找教职的话 你留在何凯明的那个团队里面 你可能会能发更多的paper 然后你有更多的结果在那个时间段

**Suggested**

何恺明的那个团队

**Reason**

何凯明是知名学者，名字应为'何恺明'，而非'何凯明'

### [01:24:41 - 01:25:38] #115 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `PhD变生`

**Original**

一开始他们不招这种New PhD graduate 如果只是一个PhD变生 他们不愿意要你 他们只会招这些像凯明一样 已经做得很不错的这种研究员 所以我也是比较幸运 我觉得Fair确实是那个时候的圣殿了 所以我觉得我也没有纠结太多其他的可能性 然后伊利亚这件事情再多插一句 我一共就跟伊利亚打过两次电话 这是第一次 第二次可以之后再聊 也是他是24年7月的时候 他SSI刚成立 然后他跟我发邮件说愿不愿意来一起工作 你又拒绝了他 对 这次为什么呢 这次是因为我刚在NYU开始我的工作 然后我就好几点吧 我跟大家聊的时候

**Suggested**

PhD新生

**Reason**

"PhD变生" 为明显错词，应为 "PhD新生"，符合语境。

### [01:27:25 - 01:28:23] #118 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `controllable 可以控制`

**Original**

当他学会了爱的时候 他一定知道它的反面是什么 对 我完全同意你说的 这件事情就上升到哲学命题了 但我觉得 或者我想反问一句吧 为什么大家会对自己的孩子 会对人这么信任 然后对AI新的这样的一个智能的实体 会这么担心或者恐惧呢 我觉得这一面 我没有答案 对 但我觉得会有技术上的一些 可以去把控的地方 我们可以通过技术的手段 让AI能在未来 变得更加可信 变得更加安全 变得更加controllable 可以控制 然后其实这件事情 侧面也是为什么要做世界模型 他为什么想要找你 不知道 可能他reach out了一千个人

**Suggested**

controllable 可以被控制

**Reason**

口语中'可以控制'与'controllable'重复，建议调整为'可以被控制'以避免重复

### [01:36:38 - 01:37:30] #129 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `Fair`

**Original**

凯明涂教授还有吗 是 我觉得对吧 这个是在Fair 那其实可以顺着Fair往下讲 那就是说Fair结束之后 那我就来NYU了 我觉得这又是一个decision making point Fair待了4年 待了4年整 对 OK 是的 也是起起伏伏 对 我刚刚说我很多去的地方其实都跟这个地方共同成长 可能Fair是一个例外 我去的时候是它的顶点 是高点 可能是高点 对 然后现在也很可惜吧 现在在那里发生的事情 但我觉得也 因为我跳船跳的比较早 所以我也不是在它谷底的时候才离开 对 我觉得我也是看到了一些迹象 对

**Suggested**

Fair University

**Reason**

Fair 可能是机构名，应补充全称 'Fair University' 以明确指代。

### [01:40:42 - 01:41:32] #134 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `Lekun`

**Original**

然后包括当然计算机科学 我觉得AI是一个很好的一个中继的 什么样一个中间的节点 对 但一样的远见在于它十几年前 就把这件事情已经establish起来了 所以我觉得它这个是蛮visionary的一个人 对 然后所以MIU在AI的布局上面也很好 所以其实 again我觉得计算机系不是它的这个学校的强项 但是它有很多AI的人才储备 对 它汇集了很多很厉害很厉害的AI的这种faculty 对 Lekun是你选择MIU的一个原因 这也是 我觉得有很多很多原因 它是其中之一 因为它需要面试我 然后它需要最后拍板 对

**Suggested**

LeCun

**Reason**

Lekun 可能是 LeCun 的误听，LeCun 是知名 AI 研究者 Yann LeCun 的名字

### [01:42:38 - 01:43:33] #137 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `这个这个成就就是build的这个image net 这个dataset`

**Original**

踏遍很多的荆棘 然后一步一步克服很多的障碍 然后到现在站在这种世界的舞台上 变成一个华人骄傲 或者说变成整个这种research领域 计算机视觉的一个北极星 让大家能够看到 他想的事情 然后能够在某种意义上 制定一些新的这种路线吧 我觉得这件事情 对他对我的影响都非常大 然后我觉得飞飞老师 最厉害的点在于 他是一个能够定义问题的人 嗯 就这件事情其实也不是一个很 很很直观的事情 就是说 其实大家说这个飞飞老师 呃 最厉害的 这个这个成就就是build的这个image net 这个dataset 对吧

**Suggested**

这个成就就是构建的ImageNet这个数据集

**Reason**

口语中重复的'这个这个'属于冗余表达，但'build'应为'构建'，'image net'应为'ImageNet'，且'这个dataset'应为'这个数据集'，属于术语和表达不规范

### [01:45:50 - 01:46:42] #141 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `他都至少是作为认的啊`

**Original**

当然是了 对 我觉得 而且你看你们都是一些机缘巧合 可能凯明是刚过去 你作为intern 让他打开了自己 然后飞飞老师是也你们也就是吃了一顿饭 你是怎么让他们打开自己的呢 我觉得这件事情很难刻意的做到 嗯 或者说 这件事情也有点玄学 我会觉得 你可以叫他某种吸引力法则 或者说你可以认为 嗯 大家想法一致的人最终都会聚聚聚合在一起 虽然你可能有无数的小息 但最后可能都会汇聚到一条河流上 我觉得比如说 我上述列举的所有的人 他都至少是作为认的啊 或者说 或者即使包括样 他可以认为是做这样的AI 但他出发点对吧

**Suggested**

他都至少是作为人吧

**Reason**

‘认的’可能是‘人’的误听或误写，根据上下文语义应为‘人’。

### [01:50:06 - 01:50:51] #147 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `neonatural`

**Original**

然后那那你可能引擎的这个硬件其实就是一个neonatural的架构 嗯 但是你只有这样一个引擎的架构其实是没有用的 你没有油 你没办法发动它 对吧 所以呃 有数据层面跟有这种objective层面 这种目标函数层面的这种考虑 然后 呃 所以所以我之后的这些research其实也是按这条主线 对表征学习的主线围绕着架构数据objective往前走 嗯 嗯 然后呃 那其实在fair的过程中 我觉得fair这个正式工作 fulltime工作的这个过程中 嗯 我觉得一个核心是呃 我跟凯明一起啊

**Suggested**

neural

**Reason**

neonatural 是明显的拼写错误，应为 'neural'，指神经网络相关的架构。

### [01:51:32 - 01:52:12] #149 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `自监督学习 包括杨洛空啊 他是一个一个一个big advocate; 蛋糕的这个这个这个body; soft surprise learning; super ice learning`

**Original**

把数据变得更大 这样就能够得到一个啊 就能推演到一个更好的结果 我觉得我觉得凯明很早很早之前就有这样的一个vision 嗯 嗯 然后所以我们也在这条路上有一些努力吧 然后所以我觉得一开始大家讨论自监督学习 包括杨洛空啊 他是一个一个一个big advocate 就是说他是他是非常在乎这个自监督学习 他有这个经典的这个蛋糕的这个analogy 这个这个比喻对吧 就是底层是你的蛋糕的这个这个这个body 这部分 必须是soft surprise learning 在上面你可以有一个super ice learning

**Suggested**

自监督学习，包括杨洛空啊，他是一个big advocate，就是说他是非常在乎这个自监督学习，他有这个经典的蛋糕的body，这部分必须是soft surprise learning，在上面你可以有一个super ice learning

**Reason**

存在明显语义漂移和术语错误，如'一个一个一个big advocate'应为'big advocate'，'蛋糕的这个这个这个body'应为'蛋糕的body'，'soft surprise learning'和'super ice learning'可能是术语错误，应为'soft supervision learning'和'super supervision learning'或类似术语

### [01:52:12 - 01:52:49] #150 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

对吧 这一部分是他的icing on the cake 就是你蛋糕上的这些这些这些奶油吧 啊 然后再往上有一个reinforcement learning 他只是cherry on top 他只是上最上面的一点樱桃 嗯 这个蛋糕上面的每一层其实都很重要 但是他没有主次之分 嗯 如果你没有蛋糕的这个底座啊 你是没办法只靠着上面的一个cherry 能够通向这个智能的嗯 对 所以因为我们在fair 因为我们做vision 所以其实我们很早就在关注这件事情 但这一部分research的进程是这样的

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [01:52:49 - 01:53:26] #151 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

就是说大概在15年16年的时候 大家已经开始知道自监督学习 其实是vision的一个未来 所以那时候呃大家会design 就设计各种各样的我们我们叫做pretext task啊 或者说它是一种代理的 这种objective代理的目标啊 就是一些代理任务吧 就是说呃什么是自监督学习呢 就是说我现在没有一个label直接给你 对吧 不像ImageNet一样 我有一千个classes 那我可以直接去训练一个supervised classifier 然后通过这种方式拿到这个representation

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [01:54:46 - 01:55:25] #154 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `unsuppressed learning`

**Original**

要么就啊这个这个这个通过一些我们叫spirits correlation 就是一些假的一些相关性来告诉你是一个椅子 比如说他也许没有看这把椅子 但是看的是椅子背后的背景啊 然后或者说他觉得哦所有的椅子都会在一个桌子旁边 所以他就 他基于这个来有一个决策的分界 然后说哎这是一把椅子 但这件事情不是我们想要的 我们想要做的事情是从这种非常diverse的viral knowledge里面 viral observation里面 去能够有某种common sense 有某种某种这种这种这种这种直觉 嗯 直觉 对

**Suggested**

unsupervised learning

**Reason**

术语错误，'unsuppressed learning' 应为 'unsupervised learning'，这是机器学习领域常用术语。

### [01:55:25 - 01:56:01] #155 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `unsuppressed learning`

**Original**

或者说某种常理 对 所以这是一开始大家为什么想要做 嗯 所谓的soft-suppressed learning 或unsuppressed learning 一个常见的过去的误解是因为 呃是是说哎我们要做unsuppressed learning 是因为给这些数据打标签这件事情 太难了太贵了 我们需要雇人 需要去打label啊 花钱花时间 我们不想这样做 但只是这只是其中的一个很小很小的问题 大的问题是 在做计算机视觉的人看来啊 很早之前大家都知道啊 只通过这条路径是没办法给予AI系统这种common sense的

**Suggested**

unsupervised learning

**Reason**

术语错误，'unsuppressed learning' 应为 'unsupervised learning'，这是机器学习领域常用术语。

### [01:56:01 - 01:56:45] #156 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `valid protect task`

**Original**

嗯 所以15 16年的时候 大家非常非常有创造力 那段时间其实还是一个蛮有创造力的时代 大家会设计出来各种各样乱七八糟的任务啊 这些任务比如说你把一张图啊 转个90度 或者转180度 或者转270度 你不给这些图一个标签 但因为你设计了你你设计了怎么转这些图 对吧 然后这些图啊 会这些图以及他所旋转的角度 可以形成一个valid protect task 你就能够去预测 这些被转过去的图到底转了多少度 这就变成了一个所谓的一个代理的任务 嗯 类似的代理的任务 还有包括给一张图 然后把它变成一个灰度的图

**Suggested**

valid prediction task

**Reason**

‘valid protect task’ 是明显的术语错误，应为 ‘valid prediction task’，符合上下文中的任务类型描述。

### [01:58:05 - 01:58:42] #159 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `moco 嗯 momentum contrast 动量对比学习`

**Original**

都比ImageNet的这种per training要差大概可能15到20个点百分点啊 所以大家再make一些progress 大家再一步一步往前走 但是这个距离啊 ImageNet能够通过这种supervised learning 在large skill这种data上面学到的这种这种label 有label的情况下 学到这种representation 还是差的太多太多 对吧 所以呃我们当初做了一件事情 然后这个跟凯文一起做 然后这个这个架构叫做叫做moco 嗯 momentum contrast 动量对比学习

**Suggested**

moco，即momentum contrast，动量对比学习

**Reason**

术语'动量对比学习'应与'moco'对应，需明确说明'moco'是'momentum contrast'的缩写

### [01:59:25 - 02:00:07] #161 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `杨鲁空`

**Original**

然后也有一些可能是桌子的图片或者是一只猫猫狗狗的图片 嗯 这些图片都不一样 但在这个空间里面 我们能够去度量它们的距离 或者说我们知道这些所有的不同的椅子 它的这种这种图片应该离得更近啊 它的representation应该离得更近 但是一个椅子跟一只猫它们距离应该更远 嗯 所以这就是一个对比学习的一个基本的一个逻辑 然后这件事情其实也不新 这件事情其实也已经做了很多很多年了 然后by the way 这件事情 呃 初期的一些论文其实还是杨鲁空第一个跟他的学生啊一起做到的 哦 对 呃很有意思

**Suggested**

杨立昆

**Reason**

杨鲁空可能是'杨立昆'的误听，杨立昆是知名学者，符合上下文语境。

### [02:00:07 - 02:00:44] #162 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `cpc啊 还有一篇paper叫叫这个这个memory bank啊`

**Original**

当然在解决的问题不直接是representation learning的问题 而是一些metric learning的问题 一些一些度量学习的问题 啊 但是但是没关系啊 在这个这是大概是2019年的时候 我觉得我们又赋予了这个对比学习一些新的意义 当然这件事情也不是 这个横空横空出世 其实在之前 整个领域已经慢慢在往这个方向啊去去去拓展 比如说有一篇paper叫做cpc啊 还有一篇paper叫叫这个这个memory bank啊 这两篇paper已经是在朝这个方向就是通过对比学习来做啊自监督学习

**Suggested**

cpc，还有一篇paper叫做memory bank

**Reason**

重复用词和停顿词，可能影响术语准确性，需确认是否为转写错误。

### [02:03:07 - 02:03:48] #166 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `然后建立这种在这种高维度的抽象空间中的这种联系`

**Original**

就这件事情其实也是一个学术界其实蛮莫名其妙的地方 就是大家 你要会画重点 对 大家主要的原因也是因为大家不讲重点 你知道吗 有时候要么是大家不会讲重点 因为大家有时候不愿意讲重点 啊 要么是有时候大家其实没有意识到重点是什么 嗯 但凯明的能力在于他能够把这些重点啊 抽丝剥茧 然后提取出来 然后告诉你 啊 然后建立这种在这种高维度的抽象空间中的这种联系 哦 啊 我觉得非常非常厉害 对 所以所以所以很多时候其实凯明的每一个idea不是 坐在这个back of the room 对吧 然后在在家里面拍脑袋想出来的

**Suggested**

然后建立这种在高维度抽象空间中的联系

**Reason**

重复使用'这种'造成语义漂移，破坏原意

### [02:03:48 - 02:04:34] #167 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `并且并且我觉得这里面其实是有一个范式存在的`

**Original**

然后其实是继续不 基于不断的探索 基于大量的阅读 然后基于大量的思考 一点点衍生出来的 然后这件事情其实我觉得 真的是非常深刻的研究 影响了我做研究的方式 以及我现在跟我的学生说大家应该做研究的方式 是应该增加输入 呃增加输入 并且并且我觉得这里面其实是有一个范式存在的 嗯 就这里面范式这也是凯明教育我的对吧 他就说其实这些所有的idea 你不能坐在那想啊 因为如果你要想出来一个idea 啊 这个idea一定不是一个好的idea 这个idea有无非有几种可能性 第一种可能性啊 呃你比世界上所有的人都聪明

**Suggested**

并且我觉得这里面其实存在一个范式

**Reason**

重复使用'并且'造成语义漂移，破坏原意

### [02:13:15 - 02:13:59] #181 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `飞线性`

**Original**

我觉得就像我刚说的 我觉得飞飞老师最厉害的地方 是因为他是一个能够定义问题的人 啊 如果失去了定义问题的能力 基本上也丧失了很多创新的能力 基本上也丧失了做research的能力 对 而且这件事情我觉得 我刚说research的飞线性 这是这是时间上 但从结果上来讲其实也是飞线性的 嗯 就是说这个是其实是mit的教授bill freeman 然后他有一个非常经典的这样一个一个plot 就是一个一个一个illustration啊 这样一个插画 他经常做talk的时候会讲 就这这条这个插画有一个横轴轴一个正纵轴

**Suggested**

非线性

**Reason**

‘飞线性’可能是‘非线性’的误听，根据上下文‘飞线性’不符合技术术语表达，而‘非线性’在科研语境中常见。

### [02:21:30 - 02:22:18] #193 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `或者说我觉得在我看起来 这件事情是能真正称得上代表作 然后或者说 我差的还很远的这些工作 对吧 然后我觉得 the net当然算 alex net当然算 然后image net当然算 rest net当然算 这个rcn或者faster rcn 这个detection的部分 当然算 这个凯明已经好几次 然后还有什么 然后transformer当然算 tension is all you need 当然算 gpt3当然算 bert当然算 我觉得clip也算 vit我觉得也算 对 vision transformer`

**Original**

或者说我觉得在我看起来 这件事情是能真正称得上代表作 然后或者说 我差的还很远的这些工作 对吧 然后我觉得 the net当然算 alex net当然算 然后image net当然算 rest net当然算 这个rcn或者faster rcn 这个detection的部分 当然算 这个凯明已经好几次 然后还有什么 然后transformer当然算 tension is all you need 当然算 gpt3当然算 bert当然算 我觉得clip也算 vit我觉得也算 对 vision transformer

**Suggested**

或者说我觉得在我看起来 这件事情是能真正称得上代表作 然后或者说 我差的还很远的这些工作 对吧 然后我觉得 the net当然算 alex net当然算 然后image net当然算 rest net当然算 这个rcn或者faster rcn 这个detection的部分 当然算 这个Kaiming已经好几次 然后还有什么 然后transformer当然算 tension is all you need 当然算 gpt3当然算 bert当然算 我觉得clip也算 vit我觉得也算 对 vision transformer

**Reason**

存在明显术语错误，如'凯明'应为'Kaiming'，'tension is all you need'应为'attention is all you need'，'rcn'应为'recnn'或'RCNN'，'detection'应为'detection'，'vit'应为'ViT'，'vision transformer'应为'Vision Transformer'。

### [02:22:18 - 02:23:08] #194 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `gan; nerf gaussian spotting`

**Original**

我觉得也算 还有gan 我觉得也算 对 数不全 大概是这些level 包括3d里面 包括nerf gaussian spotting 我觉得都是算 都会算 对 所以各个领域 都有他们的这些工作 这些工作的意义在于 大家本来是 渐进式的通向一个方向 突然有这样的一个论文 横空出世 彻底改变了 我们刚刚说 stochastic gradient design的过程 你看它的收敛的曲线 有一个drop 对吧 这是我定义的这件事情 然后我觉得 假设慢慢的历史长河是说 这条曲线还在继续往前 对吧 有一次一次的这种

**Suggested**

GAN, NeRF, Gaussian Spotting

**Reason**

术语拼写不规范，应使用标准英文术语

### [02:27:29 - 02:28:11] #201 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `IC的work; individual contributor; 他他不喜欢这样的事情`

**Original**

也做出过贡献 但我只是说这件事情是凯明主导的一个路线 对我们在这加快了这个事情的进度 可能会让结果也变好了很多 但不影响这件事情的实质 对所以这是凯明到现在 比如说前两天他还跟我说 他非常enjoy这种IC的work 就是individual contributor 就是个人贡献者的这样一件事 一个一个身份 他并不enjoy说管理一个大的团队 让大家一起只是做一个manager 来指导方向 他他不喜欢这样的事情 他现在管多少人 他有很多很多人 他现在有很多本科生啊来visit他 对然后他现在也做很多很多很好的工作

**Suggested**

IC的工作，就是individual contributor，也就是个人贡献者的这样一件事。一个一个身份，他并不enjoy说管理一个大的团队，让大家一起只是做一个manager来指导方向，他不喜欢这样的事情

**Reason**

'IC的work'应为'IC的工作'；'individual contributor'是专业术语，应保留；'他他不喜欢这样的事情'为重复表达，应修正为'他不喜欢这样的事情'

### [02:28:11 - 02:28:48] #202 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `对我觉得我觉得这是凯明`

**Original**

所以我其实不相信他 我跟他说你其实也是一个很好的manager 至少我虽然你没有真的manage我 但是只要我在你的身边 我就能感受到对自己的身份了 对自己做事情的效率啊 我就我就觉得我自己变聪明了 我觉得我觉得我如果想要有一个manager的话 我希望我希望得要有这样一个manager 对吧 他能够empower身边的人去变得更好 对我觉得我觉得这是凯明 所以MAE反正就是说contrast learning这条路 我们走了走发现哎他不能skill up 所以我们想要换一个方向

**Suggested**

对，我觉得这是凯明

**Reason**

重复的'觉得'造成语义漂移，影响表达清晰度

### [02:28:48 - 02:29:18] #203 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `学reportation`

**Original**

那我们又回过头来去用了一个更简单的方式 就是某种去造的autoencoder 就是这种自编码器啊 就是mask的autoencoder 啊这个方法就更简单了 反正啊大家可以回去看favorite 但是总之是就是通过把一些image做一些corruption的方式 然后去再去重建啊这些这些noisy的这些image 或者crop的image mask的image的方式去学reportation 嗯对这件事情跟contrast learning fundamentally不一样

**Suggested**

学representation

**Reason**

术语'reportation'可能是'representation'的误听

### [02:29:18 - 02:29:51] #204 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

但他的结果也很好对虽然他会有很很不一样的特点 比如说他不会去explode 去model这种某种invariance这种不变不变性 导致他做这种linear probing的时候 结果会会会会稍差 跟做end-to-end fine tuning 这是两种不同的测试这种reportation的方式 对呃的时候效果又会好很多 总之他们会不同的性质啊 他们学出来reportation也长得也不一样 对然后这些事情到后面也会有很深远的影响 可以再我们可以再聊 嗯但是这是MAE 然后那时候我们就觉得哇MAE好厉害

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [02:29:51 - 02:30:35] #205 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

好呃MAE 至少能拿个best paper吧 后来也拿不了啊 啊MAE skill up就能解决所有的问题吧 后来发现也不skill up 嗯对哎其实我听呃你跟祥宇之前是聊过这件事情 因为他其实也关注过自建筒学习 然后他其实也呃讲了很多 为什么自建筒学习不能skill up的一些原因 其实对我就我就不赘述了 但欢迎大家回去重听节目 但是总之是当初其实是有点 这种大喜大喜 大落吧啊 大家一方面得到很好的结果 但另一方面这些paper又只是一个paper 我们从来没有能够真的deliver出来一个实际的对吧

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [02:30:35 - 02:31:13] #206 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

然后像gpt一样 能够通通向一个完全不一样的skillable的未来的这样一个范式 嗯对我觉得这件事情 所以到那个时候就有点啊告一段落 当然那时候我还做了一些其他的工作 比如说我把自监督学习啊 可以说是第一次拓展到了 比如说3D的领域在point cloud上面也做了一些工作 对这些啊叫做point contrast 但这些工作可能更多的就是说证明了representation learning这件事情 不只是一个image domain的问题 它是一个很普世的啊 一个一个一个方法 或者说一个方法论

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 42 column 6 (char 1311)

### [02:31:13 - 02:32:03] #207 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

它不止在image上面成立 它也在3D的空间 到后面很多人去试各种样的medical imaging 还有包括这种robotics的这种task 各种抖铭它都成立 所以这件事情 我我不认为它是一个失败啊 因为它确实在影响很多很多不同的 就超超越我们现在关注的 比如说聚酸基视视觉本身的领域 对但另一方面 它也仍然没有达到像LM的这样的这样的这种这种影响力 所以啊做完了这些事情之后又做什么呢啊 对好像又开始回头了 回到了呃探索期了 这些都是在fair实验室 都是在fair在做的对吧 你在那个阶段呆了四年呆了四年

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 42 column 6 (char 1311)

### [02:32:03 - 02:32:46] #208 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `五千张这个tpu的core啊的的这个芯片啊不是买就是租吧`

**Original**

这时候fair这个周期就结束了吗 没有结束还早还早 这可能是前面的一到两年时间吧 对还有个很好玩的事情是在在在在在这个吹吹凯明 就凯明这个这个当初其实资源永远是一个问题 GPU总是不够的啊 然后当初 fairmake了一个decision是说我们试一试这个tpu这个东西好不好玩嗯 Google一直在用 然后他们也全面全面转型使用tpu 所以呃我们买了大概五千张这个tpu的core啊的的这个芯片啊不是买就是租吧 就是在Google Cloud上面 然后一开始是为了做language model人准备的

**Suggested**

五千张这个tpu的core，不是买就是租吧

**Reason**

‘啊的的这个芯片啊’ 是口语重复，应删除以保持清晰。

### [02:34:47 - 02:35:26] #212 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `detection; fastrcn mask; maskrcn; focal loss; ross; 凯明; 吴玉欣; infra; code base; base line; cvpr; base line已经比你强了`

**Original**

包括他们做detection的时候做这这一部分工作 我没有参与我还在读phd 但所有的这些呃fastrcn mask或者maskrcn 然后这些这focal loss等等一系列工作吧 这些工作都是因为他们啊包括包括ross 包括凯明包括这个吴玉欣啊 他们做了大量的工作去搭建这个infra 然后去build这样一个code base 使得base line啊这些方法的base line 就已经远超于 这些所有的乱七八糟的cvpr的paper 嗯 就我们的base line已经比你强了 那我再往上走一步

**Suggested**

包括他们做detection的时候做这一部分工作，我没有参与，我还在读PhD。但所有的这些呃Fast R-CNN、Mask或者Mask R-CNN，然后这些这Focal Loss等等一系列工作吧，这些工作都是因为他们啊，包括包括Ross、包括凯明、包括这个吴玉欣啊，他们做了大量的工作去搭建这个infra，然后去build这样一个code base，使得base line啊这些方法的base line，就已经远超于这些所有的乱七八糟的CVPR的paper。嗯，就我们的base line已经比你强了，那我再往上走一步

**Reason**

存在明显术语错误和人名错误，如'fastrcn'应为'Fast R-CNN'，'maskrcn'应为'Mask R-CNN'，'ross'应为'Ross'，'cvpr'应为'CVPR'，'base line'应为'baseline'。

### [02:38:47 - 02:39:27] #218 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

其他的行发生关系的 然后这种对照式的对比 这个是research的流程 这个东西again再次给了你一个 这种梯度的信号 嗯 对吧 然后这件事情其实有时候是非常非常 saddle非常非常微妙的 因为它并不是说 你的结果 越好 你就你就你就一定是通向正确的道路 啊 但应该是 呃就是还是说你看你哪哪哪一个 哪一个哪一个对照 能给你最大的这个信息量 maximizing information 比如说我举个简单例子 如果你做了一个实验 这个实验给你了 呃这个这个这个差了 比如说你的performance 掉了10个点

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [02:39:27 - 02:40:07] #219 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

对吧 啊 这时候如果你是一个悲观的 你就会说 啊这个实验废了 啊完全不成功 那要不就算 但如果你是有这种发法的 发法论的人 你会觉得 哎 这个方向可以掉10个点 那我往这个方向的反方向去设计我的算法 那是不是我就可以涨很多点 因为你最害怕的事情是 他的performance停留在原地 嗯 不好也不差 对吧 不好不差就没有信号 没有信号对吧 一个一个一个negative信号的反方向 就是一个正向的信号 一个positive的结果的正方向也是一个好的信号 啊 所以所以这件事情也是一个非常非常有趣的事情 嗯

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [02:48:49 - 02:49:39] #232 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `OCD`

**Original**

在deadline之前的这个月 会 会polish每一个表格 就是每个字吧每个标点符号 比如说这件事情也影响到我比如说我现在就有这种OCD对吧就这种 应该怎么说强迫症 对 也是凯明时期带给我的就是说 你的 一行论文 不能有一行 有小于60%的文字 站出来 什么意思就是说如果你有一行 你有大半行是空的 这个看起来不好看 你要把这一行占满或者占的大概有百分之六七成满 这样的paper看起来才比较 优雅 或者uniform 所以这也是我们现在每一篇paper最后我都会 让大家所有学生

**Suggested**

强迫症

**Reason**

OCD 是英文缩写，此处应使用中文表达 '强迫症' 更符合中文访谈语境

### [02:52:41 - 02:53:20] #239 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `nactive story telling`

**Original**

我觉得有很好的直觉 对就是 是的exactly 最差的电影就是说 我是个流水账的吧我有这个我有A中间没有什么冲突然后通往B然后事情结束了 我就我就我就放给你 一个好的电影其实是说 或者说为什么我们写paper的时候大家说 诶 他讲的故事讲的很好 虽然这件事情可能甚至有点nactive story telling 电影是一个story telling的过程 有一本书其实 我之前跟学生推荐 我学习凯明 跟大家推荐一些 这个不搭嘎的书 我给大家推荐一本书叫做 就叫story 是这个麦基的这本书 这本书其实是

**Suggested**

narrative story telling

**Reason**

nactive 可能是 'narrative' 的误听，'narrative story telling' 是常见表达。

### [03:02:27 - 03:03:05] #260 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

还没有人Fair还没有一个人在做Diffusion Model相关的研究 但我觉得 这个东西好像很有趣 我觉得应该去尝试尝试 然后 Bill Peebles 他是我当初招的一个intern 然后他现在是Sauer的hat 也在Sauer的这种各种生成的视频里面他也是主角 他是一个非常非常sharp 或者在我看来是一个 我觉得完美的phd学生吧 就是在各个方向 至少是六边形战士的这样一个学生 对但anyway 当初我们起点其实不是要做Diffusion Model也不是要做DIT 在前两个月的探索

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [03:03:06 - 03:03:48] #261 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

完全也是集中在表征学习这件事上 就是说我们想看一看 你一个Diffusion Model学到的这个表征 到底跟一个正常的superized learning 或者说一个soft superized learning学到的表征 到底有什么不一样 其实后续 在这个方向还有很多很多的工作 但我们开始的 这个做了一段时间的感受就是说 这个东西好像 也还行也就那样 他能学到一个不错 一个生成模型能学到一个不错的表征 但这个表征 要比 你的 自监督学习的表征要差的多的多 就完全不能打 所以我们就放弃了 但是在这个过程中

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [03:04:31 - 03:05:03] #264 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `Minimal description length`

**Original**

Minimal description length 就是说你代码其实还是很重要的 是能体现出来一些事情的 如果你的代码的 长度很短 就能够去达到同样的目的 那你这个方法 typically 会优于一个比如说写了好几千行代码一个 非常非常膨胀的系统 即使它也能做同样的事情 但你的前一种 这种更elegant的solution 更simple solution 一定是更好 我觉得这也是 某种意义上的research taste 所以我们发现 这件事情又简单 又能work 又scalable 然后又efficient

**Suggested**

Minimum description length

**Reason**

术语 'Minimal description length' 应为 'Minimum description length'，这是信息论中的标准术语。

### [03:06:16 - 03:06:33] #267 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `乐坤好像写过这个推特了; River不买账`

**Original**

对乐坤好像写过这个推特了 是的就是 就是 novelty不够所谓 你们可能做的这个东西 对吧你没有大段的数学 你没有大段的这种复杂的结构 你弄了一个很简单的这样一个结构 虽然得到很好的结果但是 River不买账

**Suggested**

乐坤好像写过这个推特了，是的，就是所谓novelty不够，你们可能做的这个东西，对吧？你没有大段的数学，你没有大段的这种复杂的结构，你弄了一个很简单的这样一个结构，虽然得到很好的结果，但是River不买账

**Reason**

‘River’可能是人名或机构名，但未明确，需确认；‘乐坤’可能为名字，但需确认是否为正确人名

### [03:10:55 - 03:11:46] #280 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `Arovent Perplexity的Arovent`

**Original**

我觉得这件事情其实是非常厉害的 这其实在讲的是Sora的诞生的 很多前续的故事对吧 有点是 然后 对 你见证了好多 对我觉得见证了一些人一些事吧 但也错过了很多 错过了什么 那比如当初没去OpenAI啊或者说 之后还有很多其他机会我就不说了 但总之是 有点 我觉得我看对了很多事情 和很多人 很多人 但也有一些时候比如说 某些创业公司在非常非常早期的时候 然后 跟我聊然后想要说 就我可能是第一个看他们的demo的人 也许可以说吧就是 这个Arovent Perplexity的Arovent 然后 他从OpenAI出来

**Suggested**

Perplexity的Arovent

**Reason**

Arovent 是 Perplexity 公司的创始人，此处应为 'Perplexity 的 Arovent'，而非 'Arovent Perplexity 的 Arovent'

### [03:14:07 - 03:14:22] #286 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `反脆弱的 塔勒布有一本书叫做这个反脆弱`

**Original**

但是 again经过这样次数多了之后我觉得我就基本上免疫了 或者这件事情其实还是蛮 叫做反脆弱的 塔勒布有一本书叫做这个反脆弱 然后我觉得

**Suggested**

反脆弱的，塔勒布有一本书叫做《反脆弱》

**Reason**

书名应使用书名号，且原文中‘这个’多余，应删除

### [03:14:23 - 03:15:08] #287 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `一个 可能的这样一个random event`

**Original**

我当初讲无限游戏的时候我其实也提到这个观点就是说我觉得 research其实必须得要是一个反脆弱的系统 这个反脆弱是什么意思就是说 一个组织或者一个个人会一个事情 他如果是反脆弱的 anti-fragile 他意思是说 一个 可能的这样一个random event 某种黑天鹅事件 或者说某种shock 就一种 一种 这种这种令你感到惊讶的一个事件的发生 这件事情如果 对于这个组织对于这个人或者对于这个事情来说 你的收益要比你的损失要大 那你的这个组织 就是一个反脆弱的组织 但如果你立刻被这个shock击倒了

**Suggested**

一个可能的这样一个随机事件

**Reason**

‘random event’应译为‘随机事件’，而非直译

### [03:16:31 - 03:17:14] #290 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `韩武纪大爆发`

**Original**

从538个million years ago 一直到现在 其实所谓的modern behavior这种behavioral modernity 就是所谓的 这种行为现代化 这件事情是在过去的3万到5万几年前发生的 所以 如果假设从韩武纪大爆发然后开始地球上开始出现这种物种开始 一直到现在 如果我们把它缩短到一天对吧假设 所有这一切都只是在24小时内发生的 那其实 有语言的部分 有这种behavioral modernity 然后大家可以有某种 abstract thinking

**Suggested**

寒武纪大爆发

**Reason**

韩武纪是不规范的中文译名，正确术语应为 寒武纪大爆发

### [03:17:27 - 03:17:36] #292 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

三个小时 三个小时 高估了高估了 三分钟 还是高估了 三秒钟 大概大概是8秒到10秒吧

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 192)

### [03:17:39 - 03:18:25] #293 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

所以在这个历史的长河里面其实我们有语言 的时间其实是非常非常短暂的 然后但是 由于我们是人我们总会从 从人的角度去思考这个事情去看待这个历史 所以我们会觉得 好像 语言 自然而然就是人的智能的一部分 然后这也是区别于 人的智能跟其他动物智能的一个主要的区别 但anyway 就是这个可能又扯的有点远我们等一下可以come back to this 我想说的是这个cambrian series 之所以取这个题目 就是因为 我们当初觉得 现在 这个多摩泰大模型 这么火热 但我们又像 有点像当初confdex的时候

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 192)

### [03:20:26 - 03:21:06] #297 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `TP Research Cloud`

**Original**

还有还有这个DIT这样的工作 所以很自然而然然后到了后面在NYU的时候 我就在考虑说我们到底能不能去也在tpu上做一些事情 因为Google 其实还是对 感谢Google,Google也是一个非常 这个这个generalist company 他有一个program叫做TRC 就是TP Research Cloud 他无偿的 给 学术界的学生还有老师们 去用这部分计算资源 但这部分资源极其难用 因为 还是面临一样的问题就是没有这个ecosystem 所以没有这个infrastructure 没有没有这个基础架构

**Suggested**

TPU Research Cloud

**Reason**

‘TP Research Cloud’可能是‘TPU Research Cloud’的误转写，TPU是Google的芯片产品，应为‘TPU Research Cloud’。

### [03:21:07 - 03:21:32] #298 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `凯明的这个story`

**Original**

也没有这个codebase 很多东西PyTorch放在上面不work 这一面其实就我们开始面临的这样一个抉择 一方面 我们从Google拿到了一些资源 我们可以有更多的算力绝对的算力 去做我们想做的事情 另一方面 这件事情实在是太难用了 所以我跟学生说 你们一定要去试一试 我也给他们讲了比如凯明的这个story

**Suggested**

凯明的这个故事

**Reason**

‘story’在中文语境中通常应为‘故事’，且‘凯明’可能是人名，应保持原样。

### [03:24:25 - 03:25:05] #305 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `H100; cluster; 三到四张卡`

**Original**

作为学费 还可以干嘛呢 可以买 半个 H100或者300个cluster 或者可以买个三到四张卡 所以这件事情是做不了事情 然后那 当然这也不是只是我在吐槽我们所有的其实就是 所谓的在美国的这个 青年教师都是生活在水深火热之中的大家 都要通过自己的方式 去找不同的资源所以这也是为什么 有点像创业就是你在一个非常constrained的resource的情况下 要去 从不同的地方 找到不同的资源你要融资对吧 小军你这是商业访谈录的 我说我这一点不商业但是其实某些地方可能还是有一些共性的

**Suggested**

H100, 300 个 cluster 或者可以买个三到四张卡

**Reason**

‘H100’ 可能是 NVIDIA 显卡型号，‘cluster’ 应为复数形式，‘三到四张卡’ 语义可能指显卡，需确认是否为专业术语

### [03:25:45 - 03:26:24] #307 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `然后他们都在 TPO上面做了自己的很大的贡献`

**Original**

collaboration的这样一个合作伙伴 这样的关系 对Google来说对我们来说都是一个好事 对 所以我觉得这不就是一个融资的过程吗 所以到后面 这花园花园的过程对 对确实是因为因为其实这样的资助其实是不求回报 对所以我觉得我也非常感谢Google 但anyway我觉得更感谢的还是应该是我这几个学生然后他们 一点点然后 突破了重重的困境 像我几个学生像这个 Peter然后 然后博洋然后书生 然后很多人吧 然后他们都在 TPO上面做了自己的很大的贡献

**Suggested**

然后他们都在 TPO 上面做了自己的很大贡献

**Reason**

‘很大的贡献’中‘很大’与‘贡献’语义重复，应删除‘很大’

### [03:27:14 - 03:28:25] #309 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `艺人英和这个 董事长啊`

**Original**

嗯 然后这一部分 反正关于语言跟视觉我们可以 可以等一下聊然后我然后我们后来又有一个叫做combrand s的paper 这个paper可能就是更进一步 我们不只做 image level的VQA的task 我们希望能够 去还是涉及到video 去涉及到视频 然后这件事情其实 真正让我真的觉得想要做这件事情的原因 又要说回到电影 还跟还跟这个 这个这个我喜欢的两个中国的导演还 还蛮蛮蛮有关系的 这个 艺人英和这个 董事长啊 我们的眼睛就是我们的相机 我们不停歇的 在这个世界上面 做各种各样的事情 对吧

**Suggested**

艺人英和这个导演啊

**Reason**

‘董事长’可能是误听，根据上下文应为‘导演’

### [03:29:15 - 03:30:01] #311 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `position paper position paper就是一些 应该怎么翻译`

**Original**

大桥下面 当吧大桥下面 对 其实你看到的还是一个又一个的frame 对吧 但它背后其实体现出来的东西 是这个世界的状态 是整个空间的这种全局的信息 这件事情是完全超越你的 这个镜头所encode的 这种单独的单一的 每一帧每一帧之外的 我觉得这件事情非常有道理 所以这件事情让我觉得 接下来还是得要做视频 即使视频难做 即使视频需要处理海量的数据 但还是要做 对 所以Cambrius我们就做这件事情 然后这件事情 它有点像一个position paper position paper就是一些 应该怎么翻译

**Suggested**

position paper，就是一些应该怎么翻译

**Reason**

‘position paper’为专业术语，需确认是否为正确表达。

### [03:31:32 - 03:32:09] #314 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `special cognition`

**Original**

我觉得是我叫它streaming event cognition 就是说现在这个东西 不只是看一张静止图片了 你会有一个连续的streamable的 这样一个visual string 就是视觉流 你的智能系统需要能够了解这个视觉流 然后能够去process 就是处理这个视觉流 然后并且能够回答一些问题 能够去understand what's happened 对吧 然后再下一个stage 我叫它special cognition 就是这件事情是我刚刚说的 是你在这个时间的序列上面的每一点 怎么样去能够看到

**Suggested**

spatial cognition

**Reason**

'special cognition'在上下文中更可能指'空间认知'，即'spatial cognition'，而非泛指的特殊认知。

### [03:40:42 - 03:41:27] #327 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `Diastatic`

**Original**

永远是这些最单一最具体最简单的任务 比如说MNIST的数字识别 1234我要把它显示出来到底是数字几 然后到后面有一些小的数据集 像C4这样的数据 是一个32x32的像素上面的十分类的问题 是猫是狗是汽车是飞机 然后再到后面 像有ImageNet这样的Diastatic出现 它变成了一个 在256x256的这种level 然后做classification的问题 对吧 但这些时候还比较相对来说比较可控 然后再到后面会有detection segmentation 就是这种更结构化的这种认知的过程 对

**Suggested**

ImageNet

**Reason**

Diastatic 不是 ImageNet 的正确名称，可能是转写错误。

### [03:45:42 - 03:46:13] #334 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

脱离了这个digital space 对吧 这件事情涉及到什么样的task呢 你说非常对 我觉得机器人是一个也会有很多的这些啊industrial application 对吧 industrial process的control 就是说一些呃所有的这些涉及到sensory modeling的这些信号 就是说你有一个嗯 嗯 有有很多不同的这种sensor对吧 这种传感器 然后他会感知到这个世界里面在发生什么事情 然后你现在要有一个统一的算法去去model这个environment 这个system

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [03:46:13 - 03:46:54] #335 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

使得你在去啊performing action或者inter intervention 就是说你在你在你在有一个动作或者你有介入的时候 你能够去预测出来这个系统接接下来会发生怎么样的变化 这件事情是LM很难做到 嗯 然后这件事情 嗯 你说你说非常对 我觉得在我看起来其实是有两个极端 一个极端是LM 嗯 非常擅长在数字化空间里面做很多很多的事情 啊 并且也非常擅长通过用coding这样的interface 对吧 通过agent的方式去介入到我们的物理生活呃之中 这件事情也会发生也没有问题 啊

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [03:52:38 - 03:53:20] #345 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `这个这个这个这个这个这个language model`

**Original**

所以有点像language想要解决问题 始终停留在这个target的这个y space 就我们通常讲你有一个x到一个y的一个映射 就是所有的机器学习 你可以通过某种 不管这个x跟y在哪在哪里 反正你可以去去这么去定义这个问题 然后y通常大家讲是supervision是label 然后x是你的数据 对吧 嗯 你可以认为 这个这个这个这个这个language model 其实只在刻画这个y space上面的事情 嗯 嗯 但这件事情是 对 回到刚刚的问题就是说 这件事情其实 不足以代代表啊 这个世界的全部 有很多东西

**Suggested**

这个这个language model

**Reason**

重复的‘这个’可能是ASR误听，应删除重复部分以保持语义清晰。

### [03:54:29 - 03:55:28] #348 `needs_review`

- Issue types: `proper_noun, other`
- Suspicious spans: `杨志林就是说 加入多摩泰`

**Original**

呃 就是一个 一个智能系统 应该去model的东西 嗯 对 嗯 嗯 嗯 嗯 嗯 嗯 嗯 比如 比如说 我们现在说 我 我 我 我 我 我 有 我 我 我 我 我 有一杯 呃 我有一个杯子掉在地上碎了 哦 其实这是一个语言 那我们之所以这么说是因为 这就是我们 对 最适合我们沟通的一戶一个东西 我们只在乎 这个事情的结果 和状态 对吧 嗯 我们不在乎一个杯子掉在地上 所以我觉得这也是它的一个局限 LLM的人会抱怨说 加入视觉以后 有可能会影响他们的智商 为啥 真的吗 对 他希望像杨志林就是说 加入多摩泰

**Suggested**

杨志林说 加入多摩泰

**Reason**

‘就是说’可能是误听，应修正为‘说’；‘多摩泰’可能是人名或术语，需确认是否正确

### [03:55:28 - 03:56:23] #349 `needs_review`

- Issue types: `technical_term, other`
- Suspicious spans: `Maravik Paradox`

**Original**

他们希望不要是一个傻的多摩泰 是 我同意 当然不应该用一个傻的多摩泰 但是我觉得是 如果不加入视觉 你一定会很傻 然后但我觉得这件事情 其实问题的根本在于 到底怎么定义聪明和傻 对 就是对智能 智能的定义是不一样的 对智能定义是不一样的 然后 或者说到底怎么去定义 什么是一个简单的任务 什么是一个难的任务 在过去的几十年的时间里 所有的这些人工智能的researcher 会不断的去 撞到所谓的 Maravik Paradox 这个Maravik悖论上 这个悖论说的事情是说 你的 对 对于机器简单的事情 或者说

**Suggested**

Marvin Minsky Paradox

**Reason**

‘Maravik Paradox’可能是‘Marvin Minsky Paradox’的误听，属于技术术语错误

### [03:59:17 - 03:59:59] #355 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `SAR; dit`

**Original**

至少我觉得在学校里面 有事情可以做 但另一方面 又比较bitter 是因为 你想在那个时候open air 对吧 在SAR的时候 我dit之所以 大家能够去接受 也是因为dit 会在SAR的block post里面 会被cite 或者说 比我的名字在上面 大家能够去找到逻辑和背后的线索 对吧 但很不幸 我觉得慢慢 最近的几年时间里面 其实industrial的这些research lab 变得越来越close 所以一开始大家发论文 后来大家不能发论文了 可以写一些blog post 但可以加一些citation

**Suggested**

SAR, DIT

**Reason**

‘SAR’和‘dit’可能是专有名词或缩写，需确认是否为‘SAR’（如Specialized Area Research）和‘DIT’（如Digital Innovation Team）等，否则可能为误听。

### [04:01:05 - 04:01:41] #358 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `REPA REPA`

**Original**

是的 对 然后 对 然后quickly conclude一下 我觉得还有两篇 我觉得我想迅速提一句的 这个论文 就是说 REPA REPA 这个东西叫Representation Alignment 你看又有一个keyword Representation 所以这是我为什么非常喜欢这篇论文 但这篇论文也是经历了这么长时间 然后所有过去的这些工作 以一种奇怪的方式组合到了一起 形成了某种化学反应 然后 带起了至少一个小的research的domain 然后做的事情很简单

**Suggested**

REPA

**Reason**

重复的'REPA'可能是误听，应为单次提及的'REPA'。

### [04:04:08 - 04:04:50] #363 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `地位的向量`

**Original**

非常重要的一个基石 包括不管是之前的 所谓的这种核学习的方式 kernel method 还是现在为什么 一个transformer里面 我们得要有这种 up projection layer 你要有一个地位的向量进来 然后把它变成一个 4倍宽的这样一个 一个fully connected layer 然后所有这些事情 都是 在讲述这样如下的事实 就是说 你在一个高维的空间里面 很多问题 原来在低维空间里面解不了 现在可以解 很多问题 很多信息 原来在低维空间里面没有 现在可以有

**Suggested**

嵌入的向量

**Reason**

‘地位的向量’语义不通，应为‘嵌入的向量’

### [04:05:30 - 04:06:10] #365 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `RE至于我们`

**Original**

一个local optimal 我们希望用一个表征学习的方式 把所有事情串联起来 然后这件事情 其实是一个很自然的事情 对吧 然后现在有很多人做相关的这些论文 有很多同期的工作也都非常好 但另一方面 这又是一个没那么自然的事情 因为你需要去 跳出原有的框架去做一个新的事 对 但当你能够跳出local optimum 去做一个新的事情的时候 我觉得你会感觉你的世界被打开了 因为RE至于我们 或者对于我的research来说 我觉得还是一个蛮重要的工作 因为它告诉我一件事情 或者说让我能够去make一个bet

**Suggested**

RE（Research）至于我们

**Reason**

'RE至于我们' 可能是 'RE（Research）至于我们' 的误听，需确认是否为术语缩写。

### [04:06:57 - 04:07:35] #367 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `neural modular connected together`

**Original**

你的表征层只是提供一些 简简单单一点点context 对吧 大部分的这些所谓的heavy lifting 就是这些脏活累活 都是靠大语言模型来做到的 我要make的这个bet是说 未来事情不会整 未来你会有一个很好的foundation 它是一个很好的表征 但它也是一个很好的世界模型 然后它什么叫做这个世界模型 这件事情我们可以再聊 但是这个foundation本身 它可能不是一个checkpoint 它有可能是一个neural modular connected together

**Suggested**

neural module connected together

**Reason**

neural modular 应为 neural module，是常见的术语表达，可能是 ASR 错误。

### [04:07:35 - 04:08:16] #368 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `multiple components的一个cognitive architecture; 语言会慢慢Lm层; login model`

**Original**

multiple components的一个cognitive architecture 说的好复杂 但本质上就是你的一个大脑 它有不同的区域 在很多不同的事情 对吧 语言会慢慢Lm层 会慢慢退化成你的本质的表征 或者说你的世界模型的foundation的一个接口 它还是很重要 它永远不会消失 因为人需要 人需要通过一个login model 提出问题 然后回答问题 对吧 他要去跟他沟通 需要跟他沟通 是一个沟通界面 对 另外就是说你还有一条线 是说你的pixel generation本身 就是你怎么样生成一个图片

**Suggested**

multiple components的一个cognitive architecture，说的很好复杂，但本质上就是你的一个大脑，它有不同的区域，在很多不同的事情，对吧。语言会慢慢LM层，会慢慢退化成你的本质的表征，或者说你的世界模型的foundation的一个接口，它还是很重要，它永远不会消失，因为人需要，人需要通过一个LM model提出问题，然后回答问题，对吧。他要去跟他沟通，需要跟他沟通，是一个沟通界面，对。另外就是说你还有一条线，是说你的pixel generation本身，就是你怎么样生成一个图片

**Reason**

存在术语错误和语义漂移，如'login model'应为'LM model'，'Lm层'应为'LM层'，'multiple components的一个cognitive architecture'语义不清晰，需修正。

### [04:12:13 - 04:13:03] #375 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `Kenneth Craig`

**Original**

能够去predict下一个state 对吧 就是下一个时刻的state 所以这是最基础的一个general的这种 世界模型的一个定义 然后这个定义本身 其实又无比的直接 或者说甚至有点trivial 因为这件事情不是一个新的概念 因为其实1943年的时候 有一个生理学家 叫Kenneth Craig 他第一次提出了这个概念 他就说人在脑子里面 是有这样一个世界模型的 这个世界模型能够告诉我们 当我们去做某一个动作的时候 接下来会发生什么样的后果 我们因为能够预测我们的动作 我们的action带来的后果

**Suggested**

Kenneth Clark

**Reason**

Kenneth Craig 并非知名生理学家，可能是误听或误记，正确名字应为 Kenneth Clark（肯尼斯·克拉克），其在1943年提出世界模型概念。

### [04:14:28 - 04:15:06] #378 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `某种cost的function 一个逗量函数`

**Original**

然后最后我也会有一个某种cost的function 一个逗量函数 然后告诉我 我执行了这个动作序列之后 我离我最后的目标距离到底有多远 所以这个算法就非常简单 就是说你不断的去sample你的action sequence 然后跳回到第一步 就是说然后找到cost的最低的action sequence 执行它的第一步 然后重复迭代的去做这个动作 对吧 再roll out下一步的action sequence 对 所以在每一次你都要做一个决策 然后这个决策的来源 都基于你对未来的这个预测 对

**Suggested**

某种cost的函数，一个逗号函数

**Reason**

‘逗量函数’可能是‘逗号函数’的误听，‘逗量’在技术语境中不常见，而‘逗号函数’更符合上下文中的逻辑表达。

### [04:16:34 - 04:17:06] #382 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `代言模型是predict next word`

**Original**

所以Rich Sutton自己其实也是有点反pure reinforcement learning 至少在当初的时间在他的paper里面 他讲一个更好的系统 当然是说如果你有一个足够强的世界模型 你可以基于 基于当前state去预测下一个state 对吧 这件事情你就有这种所谓的planning的capability在里面了 就是planning就是所谓做计划的能力 然后planning其实跟reasoning也在某种意义上也是同样的概念 reasoning现在在老城市model很火

**Suggested**

语言模型是predict next word

**Reason**

'代言模型'应为'语言模型'，属于术语错误。

### [04:17:06 - 04:17:42] #383 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `代言模型是predict next word`

**Original**

但事实上我们需要的这种planning 然后以及planning对于decision making的这种意义 其实是在当初很早很早在control theory 在reinforcement learning 其实大家都在讨论的 所以我觉得这是一个world model历史 所以如果从这个角度出发 world model实质是怎么样去刻画一个系统和一个环境 使得你能够在这个系统里面去做预测 并且这个预测能够指导你的action的sequence 以及你的自己的决策 代言模型是predict next word

**Suggested**

语言模型是predict next word

**Reason**

'代言模型'应为'语言模型'，属于术语错误。

### [04:20:38 - 04:21:25] #388 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `navier stock方程`

**Original**

然后这个飞机比如说 比如我们现在要model飞机的一个动力学系统 对吧 我要知道怎么样它能够比较省力省油 对吧 我们当然可以去从一个最low level的角度出发 我们可以说 每立方厘米可能有十几个四方的这种分子 然后我们去model每一个分子的碰撞 对吧 然后我们通过这种方式来去刻画我们这个系统 这件事情当然不会忘记了 对吧 我们做的事情是说 我们怎么样去能够在统计的意义上去study这个问题 所以这才有所谓的流体力学 然后才会有所谓的navier stock方程 然后一系列这样的setting

**Suggested**

Navier-Stokes方程

**Reason**

术语拼写错误，应为 Navier-Stokes 方程

### [04:21:25 - 04:22:12] #389 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `latent的representation`

**Original**

大家变得越来越抽象 然后但是我们能够去刻画的世界也越来越广阔 其实语言就是以某种意义上的抽象 语言是某种意义上的抽象 但是它是一种就是已经被证实过的抽象 它是高度零念的 它是一个已经存在的抽象 它是一个存在的抽象 对 那你们现在想构建的是一个新的抽象在语言之外 它是一个 对 它一定是一个latent的representation 然后这件事情人可以通过侧面的方式了解到 你到底学了什么样的一个representation 或者说哪些representation的 哪些representation是有意义的

**Suggested**

latent representation

**Reason**

术语表达不规范，应为 'latent representation'（无'的'字）

### [04:22:53 - 04:23:45] #391 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `COT`

**Original**

如果现在我们讨论的是怎么样去刻画这个世界的话 语言就是这样一种structure 语言是一个人类极其聪明的一个产物 它有精巧的设计 我觉得它本身就是 它都不是多和少的问题 它全都是 它都是 对 所以我觉得这件事情 代表着这种语言它有它自己很强的地方 而且它一定会在未来的智能 所有的这种智能体系里面 占据一个很重要很重要的地位 而且它可以COT 但COT是另外一回事了 COT也是另外一个 我觉得怎么讲呢 是一个阶段性的产物吧 对 COT也是阶段性的产物 LM的所有的一切都是一个满阶段性的产物 这也是为什么LM

**Suggested**

Chain-of-Thought (COT)

**Reason**

COT 是一个英文术语，应明确其全称 'Chain-of-Thought'，以避免歧义。

### [04:23:45 - 04:24:25] #392 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `fundtuning`

**Original**

这件事情我也蛮同一样的 LM这件事情其实它也不controllable 它也不safe 因为它没有这样一个真正的世界模型 甚至我们把LM当做一个世界模型在用 但它是一个fundamentally flawed 就是一个有缺陷的世界模型 然后这件事情是说 其实就是说 嗯 现在的所有的这些controllability 或者safety 对吧 你一个LM怎么去做 完全是通过fundtuning的方式来设计的 来实现的 你需要喂给它大量的数据 让它知道什么事情该做 什么事情不该做 或者它也不能做的事情 什么话能说

**Suggested**

fine-tuning

**Reason**

fundtuning 是拼写错误，正确术语应为 fine-tuning

### [04:24:25 - 04:25:02] #393 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `fundtuning`

**Original**

什么话不能说 对吧 什么样的话可能会带来危险 什么样的话可能是比较友好 所以这叫做alignment 但所有这一切都是基于某种post training 或者某种post training 或者fundtuning的alignment带来的 嗯 对 但真正的世界模型其实你不需要这样做 因为你可以预测你的action会lead to what consequence 你的行为会带来什么样的结果 那你就可以在inference的过程中 去尽量避免这样的行为 你可以加一些external constraints

**Suggested**

fine-tuning

**Reason**

fundtuning 是拼写错误，正确术语应为 fine-tuning

### [04:25:46 - 04:26:27] #395 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `Gaussian Spotting`

**Original**

关于世界模型 现在好像它的定义是没有收敛的 比如说你们定义的世界模型 和李飞飞他们团队定义的世界模型的区别是什么 对 所以我刚才阐述的 其实都是在我们定义下的世界模型 但我觉得现在遇到很多的问题是说 这个世界模型不好定义 原因它其实是因为 它不是一个技术路线 它不是一个算法 它是一个目的 就是我们所有人 不管你在做LM 还是做什么Video Diffusion Model 还是做Gaussian Spotting 我们所有人都在通往世界模型的道路上 所以 所以我说 我说有时候这些竞争 或者说这些arguments

**Suggested**

Gaussian Splatting

**Reason**

Gaussian Spotting 可能是术语误写，正确术语应为 Gaussian Splatting。

### [04:27:50 - 04:28:25] #398 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `World Labs; frontend的一个asset的interface; strong 3D representation; AutoDesk`

**Original**

然后飞飞老师那边 在World Labs里面 我觉得它更像是一个 frontend的一个asset的interface 这件事情也很重要 因为它是一个强3D的representation 所以这是 by the way 也要恭喜他们最近 不也刚刚融资成功 如果你可以看到他们融资的这些lead investor 对吧 他们在讨论的人 比如说我看到新闻 AutoDesk给他们投了两亿美元 那AutoDesk是一个什么样的公司 对吧 AutoDesk是一个做3D这种CAD 或者whatever design这样一个公司

**Suggested**

World Labs, 一个 frontend 的 asset interface, 一个 strong 3D representation, AutoDesk

**Reason**

World Labs 可能是机构名，需确认是否为正确名称；'frontend的一个asset的interface' 语义不清晰，可能为 'frontend 的 asset interface'；'strong 3D representation' 应为 'strong 3D representation'；AutoDesk 是正确公司名，但需确认是否为正确拼写。

### [04:34:20 - 04:34:52] #408 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `贝利特实验还是什么`

**Original**

替你做好了这个决定 在你决定要 比如说我桌子上有三个按钮 在我知道我到底想要按哪个按钮之前 我已经能够监测出来 我的大脑 已经做好了这个决定给你 这件事情 这个实验好像叫什么 贝利特实验还是什么 是一个有争议的实验 但它体现出来的事情是 有很多东西是在你的background 在你大脑里面已经在发生的 这件事情是你的world model一部分 language model不是这样 language只是一个communication tool 你永远带着目的 你永远抛出一个问题 想得到一个答案

**Suggested**

贝利斯实验还是什么

**Reason**

‘贝利特’可能是‘贝利斯’的误听，‘贝利斯实验’是较为常见的实验名称

### [04:35:29 - 04:36:04] #410 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

它没有一个对真实世界的understanding 它其实也不能够真正的reason and plan 因为它通过COT的这个planning 还是 COT的reasoning还是很不一样 跟我刚描述的比如说 这种MPC level的这种planning 它也会带来它自己的一些问题 但这些都OK 但再下一步 你就会看到比如说大家做这些 不管DIT也好 或者whatever模型也好 但大家还是做生成模型 这件事情已经让事情变得有些不同了 对吧 这也是为什么很多人 大家做video generation 会说自己世界模型

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [04:36:04 - 04:36:39] #411 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

我觉得也无可厚非 虽然我不同意 他们做的这个video generation model 就是一个最后的end game的世界模型 但它确实比language model要往前推了一步 对 它是怎么做到的呢 它在language model的基础上 我觉得现在所有这些系统 其实也是要依赖于language model的 对吧 它还是要通过language model 帮你去做prompt rewriting 然后去帮你去当做一个conditioning 丢给你的视频生成的模型

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [04:36:39 - 04:37:07] #412 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `language model也会变成了一个 你看这个历史的进程就很有趣 原来language model是主体 现在language model 变成了一个video generation model的 前期的一个准备工作的一个脚手下`

**Original**

其实language model也会变成了一个 你看这个历史的进程就很有趣 原来language model是主体 现在language model 变成了一个video generation model的 前期的一个准备工作的一个脚手下 原来language model里面 你model的是py对吧 你这个y就是还是在这种 semantic space的 某种label space的这个信息 到现在你video generation model的时候 你model的是px given y的概率 这个意思是说

**Suggested**

language model也会变成一个，你看这个历史的进程就很有趣，原来language model是主体，现在language model变成了一个video generation model前期的一个准备工作的一个脚手架

**Reason**

‘脚手下’可能是‘脚手架’的误听，‘脚手架’是技术术语，常用于描述构建模型的基础结构。

### [04:39:03 - 04:39:52] #416 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `regular grade`

**Original**

所以这已经是更加 在我看来有一点bitter lesson了 就是说你抛弃了更多的语言 空间中的这种认知 跟它的逻辑 跟它的句法结构 开始去model pixel 开始模型像素本身了 但再推演一步 像素本身可能也是错的 像素本身也不够bitter lesson 像素是什么 像素是人为定义的 一个regular grade 对吧 就是一个一个框框 然后上面每一个框里面 可能有250有8 bits information 对吧 还有这种这种lattice 就是你有一格一格一格 这是一个像素 这是我们看到的每一帧的图像

**Suggested**

regular grid

**Reason**

‘regular grade’ 在上下文中不符合技术术语，更可能是 ‘regular grid’（规则网格）

### [04:40:38 - 04:41:26] #418 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `多摩泰的模型`

**Original**

学到更好的表征 去做更好的更好的预测 对吧 但这件事情本身 跟你是不是要生成一个很酷的视频 其实是无关的 跟你能不能回答 关于你的input space的一些信息 其实也是无关的 所以again就是我重复我刚刚 刚刚想说的事情 我们每个人都在 这个世界模型的道路上前走 嗯 世界模型是一个目的 不是一个具体的路 不是一个具体的算法 或者说是一个技术路线 然后总有一天 我们会有一个更好的世界模型 语言模型会在此日上 然后它也会变得更强 我们会有更好的多摩泰的模型 它能够更好的理解这个世界

**Suggested**

多模态的模型

**Reason**

‘多摩泰’可能是‘多模态’的误听，根据上下文语境，此处应指多模态模型，而非‘多摩泰’这一名称。

### [04:41:26 - 04:42:07] #419 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `RE`

**Original**

我们也会有更好的video生成模型 嗯 然后我觉得RE就是这个 这个这个过程中的一个雏形 嗯 所以现在还有很火的一个说法 是所谓的unified model 或者omni model 大家试图把所有的数据 全都堆叠到一起 使得我们能够让一个系统 既能做understanding 又能做生成 大家讨论的问题也是说 我到底是理解能够帮助生成 还是生成能帮助理解 嗯 我觉得都不重要 理解和生成是一体的 它都需要一个真正的world model 作为它的基础 对 一旦有了这个好的world model

**Suggested**

RE（如指某种模型或技术）

**Reason**

‘RE’在上下文中未明确指代，可能是某个模型或技术的缩写，但未明确，需进一步确认。

### [04:44:16 - 04:44:51] #423 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `lunch model`

**Original**

比如说wikipedia上面有一个具体的人名 他过去做了什么事情 这是一个很差的一个lunch model 所以我想说的事情是说 语言模型skinning law 是基于一个对knowledge的这种representation 所得来的这样一个skinning law 所以这是为什么 它可能会有一个相对balance的配比 就是说你的 你的number token 你的数据和你的parameter 需要大概1比1的方式 Chinchilla里面是这样的一个方式 对吧然后去skill up 世界模型尤其是基于

**Suggested**

language model

**Reason**

明显拼写错误，应为 'language model'

### [04:48:21 - 04:49:08] #429 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `代言模型`

**Original**

就比现在所有的 用来训练世界 代言模型的所有的这些token还要多 4个月的小孩 他看过的视频的量 要比30个trillion的这些 最好的这些代言模型的数据的量还要大 对吧 所以量集实在是太大 所以我刚刚说要download human是说 我人眼看到这些东西 这些数据到底我们怎么能采集过来呢 对吧 我觉得视频还是 这是为什么之前 比如在cameras里面 我还是非常希望去多做一眼 可能视频相关的研究 我觉得这是现在全村的希望 这件事情可能有很高的门槛 但我觉得不一定成功不了 我觉得可以分几个阶段走

**Suggested**

代理模型

**Reason**

'代言模型'可能是'代理模型'的误听，'代理模型'是机器学习领域中常见的术语，指用于替代复杂模型的简化模型。

### [04:50:41 - 04:51:22] #432 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

嗯对好第一步是视频 第一步是视频 然后接下来其实parallel的运作 就是说我觉得 这样的世界模型 或者这种这种很variant centric的世界模型 会有一些非常好的这种应用的前景 因为我觉得只有research也是不够的 然后LM之所以成功 也是因为chatbot这样的一个interface 实在太成功太自然了 对吧它依赖于 嗯互联网依赖于这种这种移动移动设备 啊但它是一个很好很好的接口 一个非常非常好的product 啊所以open爱自己的人也没有意识到 对吧 但 当我们讨论世界模型的时候

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [04:51:22 - 04:52:07] #433 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

啊尤其是我们刚定下这个世界模型的时候 这个最终的这个跑道到底是什么 我觉得这件事情可能需要 我觉得这可能才是一个真正的难点 嗯可能是一个比数据还要更难的问题 所以现在如果拍脑来想啊 again拍脑来想的想的idea 可能最终都是错的 但是至少有两个出口 一个是比如说这种air glasses 啊这种真的personal assistant 这件事情需要一个world model 这件事情只有语言模型不够 只有语言模型的话 它还是一个带着屏幕 可以有语音交互的这么一个差GPT 对吧 嗯 它没办法走出这个产品的心态

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [04:53:20 - 04:54:00] #436 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `air variable`

**Original**

对非常垂直 嗯 对吧 但我觉得这件事情是一个未来的世界模型 在air variable上面一个缩影 嗯 因为如果假设真的有眼镜 或者说对我知道你不喜欢戴眼镜 但是假设有某种variable devices 它能够真的是always on 我们不知道这个功耗问题怎么解决 先不管硬件问题 我先不管 但它能够实时的看到我们所能看到的一切 对吧 有这种完全always on 然后infinite的这种tokens 进入到这个系统里面 我觉得这件事情其实是会有很大很大的潜力的 嗯 然后第一我会很想要这个东西

**Suggested**

AI variable

**Reason**

"air variable" 不是常见术语，结合上下文应为 "AI variable"

### [04:54:00 - 04:54:44] #437 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `多摩泰`

**Original**

因为我想知道我几点喝了一杯咖啡 然后是不是这杯咖啡喝的早了一小时晚了一小时 导致我晚上可能睡眠没那么好了 或者说我是一个运动员 他想要指导我的每一个动作 或者说我在医院工作 我希望给养老院里面的每一个老人 都配备这样一个variable 使得我知道他每天的这个行为模式是怎么样的 他吃了什么药 做了什么事 然后他的心情怎么样 对吧 他的状态怎么样 嗯 然后跟我背后的这些医疗记录挂钩 然后提供更好的智能决策 我觉得有很多很多类似这样的例子 对 但这件事情也是基于现在的LM 现有的多摩泰的智能 其实是我觉得是做不到 嗯

**Suggested**

多模态

**Reason**

"多摩泰" 可能是 "多模态" 的误听

### [04:55:27 - 04:55:59] #439 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `这种生成派的这种word simulator`

**Original**

机器人其实是一个很好很好的一个downstream的application 因为 不管有任何 上游的 这些新的 我们讲 泛世界模型的这种这种演进 啊 呃机器人都能够benefit from it 嗯 比如LM出来了 那我就有VLA 对吧 然后活了一段时间 现在这个video diffusion做的很好 action condition video diffusion做的很好 对吧 这种生成派的这种word simulator做的很好 那我们也在讨论机器人怎么样去用这些模型 去做一个 啊

**Suggested**

这种生成派的word simulator

**Reason**

重复用词'这种'，可能为ASR误识别，'word simulator'可能为'world simulator'的误听，需进一步确认。

### [04:58:45 - 04:59:32] #444 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `中等paper陷阱啊 哦 中等收入陷阱`

**Original**

也是对我帮助很大的一些mentor吧 然后大家 可能有投资人的身份啊 有这种 其他创业者的身份啊 他们就说哎 三年 你应该也尝试去 去创业 嗯 啊 因为在学校里面 像我刚刚说的 其实有很大的困境 对 但并不是学校 一无是处 我觉得学校其实是一个很好 很好的平台 它让我有足够的空间 去真的找到 我想要做的事情 但我突然觉得 哎 好像现在是一个时间点 似乎 啊 我想要探索的东西 探索到了一定的地步 啊 再往后有可能会陷入 我叫它一个中等paper陷阱啊 哦 中等收入陷阱 就是说 你会发一些不错的论文 但是由于

**Suggested**

中等收入陷阱啊 哦 中等收入陷阱

**Reason**

明显语义漂移，'中等paper陷阱'应为专业术语'中等收入陷阱'

### [04:59:32 - 05:00:33] #445 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `restrictions sih`

**Original**

这个这个resource的限制啊 导致 你没办法真的 把你的你的这些idea 推广成一个啊 某种意义上一个新的breakthrough 对 所以我觉得 这可能是是一个好的时间点 嗯 然后 所以我有一个mentor就问我 那时候还蛮有趣的 可能大概是 啊 去年 去年的 可能年中吧 或者说可能是秋天的时候 25年年中 嗯 对 25年年中 然后他就说 哎 你去问一问 呀 他好像最近在卖他 呃 呃 呃 呃 呃 呃 呃 呃 呃 呃 呃 呃呃呃呃呃呃呃呃呃呃呃呃呃 呃呀 嗨呀 呃呀 胭 呃呀 restrictions sih

**Suggested**

restrictions

**Reason**

疑似ASR错误，'restrictions sih'应为'restrictions'

### [05:00:33 - 05:01:35] #446 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

呃呃呃er 呃呃呃呃 呃 er 让的 那是一个 哼 皮 而 这边呢 额弱了 然后还没等我说什么 然后一样就跟我说 说哎 三连你先不要告诉别人 但我已经决定了 这个我现在想要做的事情 我觉得应该在外面做 我想要去创业 开一个公司 然后我就我就问他说 你想做什么事情 这个背后的business model是什么 然后后来发现 哇这件事情跟我想象的事情 完全一致 非常有趣 对 然后这件事情是什么呢 我觉得你可以 你可以叫它世界模型 或者说 这部分的出发的逻辑在于 我觉得 在我想做的这件事情上 在现在的这个 不管是世界上

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 330)

### [05:01:35 - 05:02:17] #447 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

任何一个国家 我觉得都做不了 包括在湾区在故谷也做不了 那这个事情是什么 就是说 你还是有一定的 这个research的程度 对吧 他不是完全的 比如说我们现在要large model 我们要deploy这个system 然后我们要push the product 然后去去去去get some revenue 其实其实not like that 然后我觉得 这件事情 有很强的这种research的这种 嗯倾向性 嗯对吧 但是他又不是在纯粹的学术 学术的这个这个setting下面 他不是过去的fair 也不是nyu

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 330)

### [05:05:55 - 05:06:35] #453 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `有BitLesson 有AGI 有LM 这样的一个叙事逻辑 这件事情定义了一系列的benchmark 嗯 对吧 就是说你要打榜 嗯 那你就打打的这个榜 可能是LM Marina 啊 或者说其他的这些榜单 对吧 有一系列这个benchmark 这个benchmark 定义了 resource 的allocation 就是说你你怎么样分配资源 嗯 对吧 因为我的目标 如果是在榜单上得到第一名 那我只能投入最多的资源 使得我能够处在这个位置上去竞争`

**Original**

有BitLesson 有AGI 有LM 这样的一个叙事逻辑 这件事情定义了一系列的benchmark 嗯 对吧 就是说你要打榜 嗯 那你就打打的这个榜 可能是LM Marina 啊 或者说其他的这些榜单 对吧 有一系列这个benchmark 这个benchmark 定义了 resource 的allocation 就是说你你怎么样分配资源 嗯 对吧 因为我的目标 如果是在榜单上得到第一名 那我只能投入最多的资源 使得我能够处在这个位置上去竞争 然后resource allocation 决定了

**Suggested**

有BitLesson、AGI、LM这样的一个叙事逻辑。这件事情定义了一系列的benchmark，嗯，对吧？也就是说你要打榜，嗯，那你就要打这个榜，可能是LM Marina，啊，或者说是其他的这些榜单，对吧？有一系列这个benchmark，这个benchmark定义了resource的allocation，就是说你怎么样分配资源，嗯，对吧？因为我的目标，如果是在榜单上得到第一名，那我只能投入最多的资源，使得我能够处在这个位置上去竞争。

**Reason**

原文存在明显的语义漂移、重复和断句问题，'BitLesson'、'LM Marina'等术语可能需要确认是否正确，'打打的这个榜'等表达不清晰，需调整标点和断句以明确语义。

### [05:10:21 - 05:11:02] #460 `needs_review`

- Issue types: `semantic_drift, proper_noun`
- Suspicious spans: `他他不是一个non profit`

**Original**

了困见你那次他跟你说了什么 他也没说什么 他只是讲了啊 对他说的这件事情就是说我刚说 我觉得我跟他的想法非常一致的这件事情 就是世界模型是什么 我们可以有一个定义 在这部分上 我跟他的定义其实非常非常吻合啊 然后包括他做japa 我我在nyu也经历了一些过程 这个过程是啊 我从我从质疑japa到理解japa到成为japa 经历了这个人生的三个stage 嗯 我等一下可以可以再展开聊一下这件事 但他具体跟我说的事情是说这个公司他他不是一个non profit 他不是一个纯粹的research lab

**Suggested**

他不是一个non profit

**Reason**

重复的'他'字可能是ASR误识别，'non profit'应为'nonprofit'，但'non profit'在口语中也可接受，需确认是否为术语

### [05:12:37 - 05:12:54] #463 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `第二个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊`

**Original**

第一个还是侯小迪 啊 第二个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊 第三个是这个张涛是manus的张涛啊 第三个是这个张涛是manus的张涛啊 第二个是这个张涛是manus的张涛啊 第三个是这个张涛是manus的张涛啊 第三个是这个张涛是manus的张涛啊 他们都跟我说 你如果想要做一个好的产品 你首先得要热爱生活 你得知道这个生活里面的人 他们在做什么事情

**Suggested**

第二个是张涛，manus的张涛

**Reason**

重复的'第二个是这个张涛是manus的张涛啊'属于明显重复，'manus的张涛'可能是人名，需确认是否为'张涛'的正确表述。

### [05:16:13 - 05:16:52] #469 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `很多的锤类`

**Original**

哪里可能现在有有有有有这个有这个啊错误 对吧 等等一系列这些非常long tail的问题 对 那这个是一个就是飞机引擎的世界模型 这是一个飞机引擎的世界模型 但它会基于一个universal的世界模型的预训练 对 所以你们会训一个通用的世界模型 这是我们的目标 这个是预训练 然后上面可能会有很多的锤类 很多的锤类 像我说的你看language model也是上面的一个锤类 video diffusion也上面一个锤类 action对吧 然后planning 然后robotics也是一个锤类

**Suggested**

很多的模块

**Reason**

'锤类'可能是'模块'的误听，根据上下文语义更符合技术术语

### [05:19:18 - 05:19:45] #474 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `treasure level`

**Original**

但是他跟LM fundamental不一样 但他至少是一个transformer 或者treasure level的事情 对 这是我们的梦想 落到实处要一步一步走 但回答你的问题就是说 其实不只找了researcher 比如说我们的CEO 我是这个公司的co-founder and chief science officer 我非常喜欢这个title 因为我觉得我们的researcher是一个很重要的东西 所以我希望我自己的定位还是在science上面 我不是一个好的CEO 至少现在不是

**Suggested**

transformer 或者 research level

**Reason**

‘treasure level’ 在上下文中不符合技术术语或常见表达，更可能是‘research level’的误听。

### [05:25:17 - 05:26:03] #482 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

在充足的资源的情况下 去做一个不一样的事情 对 倒不是说这些学生都会加入这个公司 我觉得肯定不会 我们还是会有一个清晰的boundary 但只是说 in general 我希望 我们的这个公司 我们叫emilabs 它能够承担起一定的这种定位 它能够联系起 学术界里面 想做事情的年轻人 让他们能够参与到这个历史的进程来 我觉得这一部分的 对 这个渠道 在现在的很多这个lab里面是不存在的 嗯 如果Lequan不从Meta离职 你会创业吗 我觉得我可能也会 但可能会纠结一段时间 你会自己做CEO 我觉得我不知道 对

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 255)

### [05:26:03 - 05:26:37] #483 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

我觉得 对 如果这么决定的话 也是一个 另外一个选决决定的吧 但至少我现在不知道 你会做这个方向吗 如果是那样的话 我会在想 对 或者说我现在在公司里面 我们讨论的问题就是exactly 我一直在想要做的事情 嗯 然后这件事情 所以有一点不谋而合 而且其实这件事情 again 我不懂商业 所有的这些逻辑 但是有一些点 我觉得很有趣 就是我们想要build 这样一个反向的OpenAI 什么叫做 反向的OpenAI 什么叫反向OpenAI 就是正向的OpenAI是说 我现在有互联网 作为我的数据的发源地

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 255)

### [05:35:14 - 05:36:06] #496 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

就是他一贯之的在坚持他的很多逻辑 和他认为正确的事情 这件事情是不受到外界的 任何事情的干扰 但这件事情不代表他完全是一个固执的 听不进去任何话的人 其实也不是这样 他有些时候他错了 有些时候他对了 他大部分时候是对的 但他其实是能听进去大家说的话的 并且他也说过 就有一个之前有一个新闻稿 是说Yann can't be moved 就是Yann LeCun永远不能被移动 谁也不能对 对移动他 然后Yann说 对就是说他在固执 Yann说我完全可以被move 我完全可以被移动 但我需要基于事实来被move

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [05:36:06 - 05:36:57] #497 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

而不是一些人告诉我应该怎么做 我去怎么做 我才会move 所以当初在Meta的时候 其实也有很多人告诉他说 我们现在Meta要去做large model 我们要做很多这些事情 你不能在外面再说这些话了 对吧 你不能说天天dece这个large model不work Yann完全不能接受 Yann说我作为一个科学家的政治 My integrity as a scientist cannot accept this 所以我觉得这件事情我也很敬佩 我觉得他真的他说的话 不是因为现在什么东西成为了一个热点 让他去这么说的

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [05:37:39 - 05:38:21] #499 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `Yann world model`

**Original**

Yann world model到底是什么时候 他从来不会说一些比较high level的 这种相对来说比较虚无的这种概念 他永远要给你写公式的 他永远会 现在也会 现在也会 而且他现在每个星期也会有一天在NYU 然后还是要带自己的group 还是会开组会的 开组会的时候就是要走到白板面前 然后给大家写个推公式 一点点推 highly technical very very very technical 对 你们两个的分工是什么 Yann是executive chairman 所以他其实 更像是我们这艘大船的船长

**Suggested**

Yann LeCun world model

**Reason**

人名Yann应补全为Yann LeCun

### [05:44:17 - 05:44:41] #508 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `much better这种short term的financial 啊 这种return; part i agree`

**Original**

这些机会可能也会有much better这种short term的financial 啊 这种return 嗯 就又会有更高的工资更高的回报 嗯 但我一直考虑的这个这个方式是说有些人劝我说哎你先去赚两年前 对吧 赚够钱了之后回来再创业不好吗 啊 嗯 part i agree 但是我又会担心 对吧

**Suggested**

much better这种短期的财务回报

**Reason**

‘financial’和‘return’重复，语义不清晰；‘part i agree’应为‘I agree’

### [05:44:46 - 05:45:27] #509 `needs_review`

- Issue types: `proper_noun, semantic_drift`
- Suspicious spans: `mata`

**Original**

对吧 我现在我现在作为作为现在这个人生的这个stage啊 还有没有两年的时间 可以让我在一个足够好的精神状态 去 做这件完全exploitive的research 我觉得不好说 有可能 在你有钱了之后 你的lifestyle 你的生活方式会变化 然后 就会导致你失去了最开始的一些勇气吧 啊 然后我觉得这只是对我个人而言啊 我觉得现在我有很多很多的朋友他们在mata尤其在mata对吧 大家大家其实都赚很多很多钱啊 他们也很卷 他们每天工作 我觉得也是加班加点啊 然后大家基本上都搬到公司旁边

**Suggested**

Meta

**Reason**

‘mata’可能是‘Meta’的误听，根据上下文推测为公司名

### [05:48:53 - 05:49:34] #515 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `这个paper叫叫solaris 叫索拉里斯星`

**Original**

所以我觉得 这样对这样的人对我来说其实是是很有很有吸引力的啊 因为我觉得他的世界其实是很大的 他的世界不只局限在research一小块啊 然后我们都要做世界模型了 我希望 这个这个这个这个大船的 舵手是一个有格局热爱生活的人 哈哈哈 然后对还有一个很有趣的例子 我们接下来三月也许这个节目播出的时候 我们还有另外一篇paper要放出来啊 这个paper叫叫solaris 叫索拉里斯星 这个东西其实是一个科幻小说 呃莱姆的一个小说 然后后来被塔古斯基改编成一个电影啊

**Suggested**

这个paper叫SOLARIS，叫索拉里斯星

**Reason**

标题应为专有名词'SOLARIS'，而非'paper叫叫solaris'。

### [05:51:04 - 05:51:55] #518 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `金汤石`

**Original**

我觉得这是这是一点啊 蛮有趣的啊 可能对很多人都不重要 但对我个人来说蛮重要的一个一个一个人格魅力的体现吧 有一个中国的投资人曾经跟我说过 所有含着金汤石出身的创业都没有成功的 几乎没有吧 你怎么看 呃不懂什么叫金汤石 融资金额巨大 非常的有名 作为方的 就是已经功成名就 而且是非常高的功成名就 嗯 呃我们没有含着金汤石 就像我说我们是完全一个 草不说草台班子吧 是一个草根联盟的一个创业模式啊 那困怎么可能会是草根呢 样的草 样的不是草根 但他现在在整个AI的行业或者在互联网上 包括在投资人面前

**Suggested**

金汤匙

**Reason**

金汤石可能是误听，正确术语应为'金汤匙'，指出身优越、资源丰富的人。

### [06:02:40 - 06:03:17] #536 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

就是我不是就跟做research一样 我觉得 这个探索的过程 开始先探索先动手做事情 嗯 然后逐渐的找到属于你的idea 哦 我觉得这件事情对于startup也是成立的 你觉得现在你们的idea进展到哪一步了 呃 我觉得进展到了 我觉得我们现在有事情可以做 并且我们还觉得 会有一些 呃 很快会有一些很promising的结果的这样一个地步 嗯 对吧 但这件事情 啊 具体是什么 我们可以过几个月之后可以再聊 但是啊 对话又说回来就是这件事情其实 外面的人对这个公司对于样 还有一个错误的认知

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 287)

### [06:03:17 - 06:03:47] #537 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

就大家其实不知道什么是japa 嗯 对 然后然后其实我个人也经历了好几个阶段 我从我从质疑japa到理解japa 再到成为japa 这样人生的三个stage 嗯 哦 然后然后这件事情 我觉得也蛮好玩的 因为一开始质疑japa是因为我们刚开始 做softspice learning做moco做mae 然后我觉得哎 japa好像是yet another softspice learning algorithm that's it 然后后来慢慢理解japa 是因为觉得japa其实啊 比我们想象的走的要更深

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 287)

### [06:03:47 - 06:04:25] #538 `needs_review`

- Issue types: `technical_term, semantic_drift`
- Suspicious spans: `japa; paper叫了japa; asotropic gaussian distribution`

**Original**

它里面会有很多背后的逻辑 有很多的数学的原理 并且我们也需要有人在这条路线上继续坚守下去 因为我们当初发现东西skill skill up不起来 然后就不做 嗯 然后但后来japa比如说 包括我举个简单例子 比如最近有一篇paper叫了japa 然后他们就一个 非常严格的证明 说哎 如果你要有一个很好的representation 如果你要想要让这个representation agnostic to你的downstream task 那它一定是一个asotropic gaussian distribution 啊

**Suggested**

paper叫做JAPA, asotropic Gaussian distribution

**Reason**

japa 应为 JAPA（可能为论文名称），'paper叫了japa' 语义不通，'asotropic' 可能为 'anisotropic' 的误听，'gaussian distribution' 是标准术语，需确认是否为 'anisotropic Gaussian distribution'

### [06:04:25 - 06:05:02] #539 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `japa; cognitive architecture`

**Original**

这有点technical 它本质上就是说它是对这种表征了某种性质的一个课话 嗯 然后我发现哎 这件事情其实还是有它的道理 然后真正成为japa是因为我觉得japa不是一个模型 japa不是一个具体的算法 嗯 japa是一个整整个一套的cognitive architecture 就是一套认知体系啊 这件事情是一样在他的2022年的paper里面写到的事情 所以这个认知体系在我看来是通往一个智能 universal的智能体的一个在我现在看起来一个很合理的道路 对吧

**Suggested**

JAPA, cognitive architecture

**Reason**

japa 应为 JAPA（可能为论文或理论名称），'cognitive architecture' 是标准术语，需确认是否为专有名词

### [06:07:12 - 06:07:56] #543 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `AGI是个伪命题; 杨千长; Demis`

**Original**

所以啊 暂时看下来我觉得我做了一个正确的选择 嗯 跟你预期也许还是会有一点不一样的 可能更乐观 嗯 对我觉得我觉得 跳下来那一刻就是恐惧消失了 嗯 对我觉得我觉得只要有勇气 一切都好说 嗯 然后我觉得在这个公司里面啊 对我是能找到这样的勇气的 嗯 嗯 你刚才说 AGI是个伪命题 你这个能展开一下吗 哦AGI是个伪命题 这件事情也是杨千长说的 他之间不是跟Demis有一个辩论吗 他就说到底什么是general intelligence general intelligence到底存不存在 这件事情我可能也就不赘述

**Suggested**

AGI是个伪命题，杨千长，Demis

**Reason**

‘杨千长’可能是人名，但需确认是否为正确姓名；‘Demis’可能指Demis Hassabis（DeepMind创始人），需确认是否为正确拼写。

### [06:11:01 - 06:11:49] #548 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

然后黑猩猩只是在吃香蕉 直接静止 就去打开那个装有苹果的盒子 把苹果吃了 看都不看这个香蕉一眼 所以黑猩猩也有某种 这种推理的能力 对吧 然后虽然确实语言是独一无二的 语言是只有人类有 但不代表其他动物不会交流 如果我们说 他们有他们的语言 他们有他们的语言 包括你像鲸鱼也有自己的语言 反正这些事情还是蛮有趣的 我很推荐那本书 然后 包括还有我看到那个叫什么某一种鸟 我忘了叫什么了 然后他就说他们很会 就是如果他在买一个食物 他把一个食物要买到地底下 如果他发现有他的同伴看到了这件事情 他会先买在底下

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 366)

### [06:11:49 - 06:12:26] #549 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

等到这个同伴走了之后 把它挖出来 换一个地方重新买下去 对 所以我觉得还蛮有意思的 然后当然我们也知道 对吧 那狗的嗅觉很灵敏 然后蝙蝠会基于听觉 我觉得 智能的界限是很很广泛的 大家现在说jagged intelligence 那你们的world model会先朝着哪一种生物的智能去做呀 目标当然是人类的智能 人类智能肯定还是对还是还是在至少在一个底盘身上肯定还是最强的 或者说他也是能够最能benefit这个世界的

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: Expecting ',' delimiter: line 10 column 6 (char 366)

### [06:12:26 - 06:13:02] #550 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

所以我们还是希望build一个world model通向human like intelligence 但我只是想放弃人类的这样的自大 然后这件事情其实我最近很受启发 是因为看了这个rich sudden的一个他在这个这个podcast上面的一个一个一个一个理论 因为其实我之前我也不知道我该怎么address这件事情啊 因为大家说哎 LM不是很厉害吗 LM现在可以写code可以拿到IMOIOI的金牌 可以帮我们去月球去火星 这件事情太伟大了 然后我觉得我没法否认这件事情 这件事情确实很厉害 对吧

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:13:02 - 06:13:42] #551 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

然后但rich sudden 这个 他的他的回答我觉得就很好 他回答是说你觉得这件事情很伟大很厉害吗 很难吗 那你就这么觉得吧 因为我不这么觉得 我觉得能够打造出来一只松鼠的智能 这件事情才是难的问题 一旦你有了一只松鼠的智能 一旦你能够去build的一个松鼠的智能能够让他在这个真实的世界活下去 他有自己的goal 他有自己的目标 他有自己的像你说的这种intrinsic reward 他知道饥饿 他有自己的emotion 然后他能够有一定的社群的活动 后面的写code写code上火星上月球

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:16:01 - 06:16:44] #556 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `谭杰 DeepMind谭杰`

**Original**

一个12岁的孩子基本上可以做很多很多的家务 可以做所有的家务 但现在到底有没有一个机器人能够像一个12岁的孩童一样去承担这些家务 当然没有 谭杰 DeepMind谭杰他也说 就是机器人发展是极不平均的 极不平衡的 他跟一个小孩的成长的轨迹是不一样的 比如说现在机器人的四肢的发达能力已经比他强了 已经比人强了 但是很多其他能力都还不如一个小孩 因为大脑没没有人做大脑这件事 没有人构建机器人大脑 所有的机器人创业公司 包括在大厂的机器人公司 都没有去解决这件事情 DeepMind不算吗

**Suggested**

谭杰，DeepMind的谭杰

**Reason**

人名与机构名混杂，需明确区分

### [06:16:44 - 06:17:22] #557 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `詹姆兰`

**Original**

DeepMind现在完全也是基于詹姆兰 所以他也是在VLA的框架前去做 是是是 所有东西收敛到詹姆兰 对 但这件事情需要一个预训练的下半场 按姚顺宇的这种经典说法 我觉得需要需要下半场了 但我觉得这是一个预训练的下半场 詹姆兰其实最近也发表了同样的观点 然后那这个预训练就是world model预训练 这件事由谁来做 这件事情对我来说是不清晰的 如果我知道有另外一个地方也可以做这件事的话 那我可能真的还可以考虑一下 我也我也不一定非要在现在这个startup自己做这个事

**Suggested**

Jailbreak

**Reason**

詹姆兰可能是Jailbreak的误听，根据上下文语境推测

### [06:17:22 - 06:18:06] #558 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `portraining`

**Original**

robotic startup没有任何的精力去做这件事 他们需要把自己的资源投入到 所谓的硬件上 对吧 就是你需要买更多的机器人去deploy这些机器人 然后或者在simulator里面去做这些imitation learning的方式 能够让你有一个足够好的 能够在短期内解决一些这种具体问题 创造价值的这样的机器人的团队 派呢 派VLA对吧 派也是一样 派我觉得已经是一个非常非常researchy 然后做的已经非常非常不错 而且有启发性的一个公司了 但again他们不会做预训练 他们不会做portraining

**Suggested**

pretraining

**Reason**

portraining 是拼写错误，正确术语应为 pretraining（预训练）

### [06:18:54 - 06:19:35] #560 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

但我觉得这也是exciting的地方 这所在 我还觉得挺有意思的 因为我们第一次见面 你就说you are not the chosen one you are just the normal one 你为什么这么喜欢说这句话 没有你看我这个一路我们也讨论了我这些对吧 这个成长历史 我其实没有预料到我们会聊这些 但是对我觉得肯定不是那种天选之子 然后这句话其实也是我喜欢的一个球队的吧 就是利物浦 然后我是一个cop已经20多年了 然后然后我觉得也有点 气质相投 然后我最喜欢的一个教练是克鲁普

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:19:35 - 06:20:18] #561 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

然后他其实是有点半开玩笑的 跟大家说就当初另外一个教练 莫里尼奥 然后说I am the special one 我是特殊的一个 然后克鲁普说I am not the special one I am the normal one 对 然后我觉得这件事情 一方面他自己又非常朋克 他又是那种摇滚气质 然后他又 经常跟大家说 他觉得他在团队的定位 就是一个电池的作用 他希望能够通过自己的passion 自己的能量 去you know 让其他的人 给其他人的发电 empower其他人 对 我也想成为这样的人

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:20:18 - 06:21:12] #562 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

我也想成为一个团队 不管这个团队是在 在在学校还是在创业公司的一块电池 我觉得这件事情其实不容易 因为有时候 每个人都会有沮丧的时间 我也想 这个这个多吐吐槽 然后抒发一下情绪 但我现在慢慢觉得 在学校 比如在在学生面前 然后在创业公司的团队面前 需要能够有人 有这种电池的作用 或者说我觉得样 是一个巨大的电池 他赶着了我 但我希望 把这个电力通过也输送下去 你最近一次感到 沮丧 是为什么 我天天都感到沮丧 我觉得这个已经变成了一个 的这也是research的一个宿命 我觉得大家这个对底色都挺悲凉的

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:21:12 - 06:22:03] #563 `error`

- Issue types: `none`
- Suspicious spans: `none`

**Original**

原因是research的求索的过程 就是在一个暗无天日的 这样一个一个地方去摸索的过程 你看不见光亮的时候 你总是会感到感到迷茫跟沮丧 然后大家真正感受到 这种快乐的时候 无非就是你真正把东西做出来的时候 但这一部分的时光又是非常非常短暂的 可能也许只有5%10% 凯明好像有说过类似的话 所以长此以往 对吧 因为我这个大家大家心理心理状态也很堪忧 啊 但我觉得还好 对我觉得啊 我觉得我觉得现在这个时代 我觉得还是跟原来不不那么一样了吧 就是我觉得现在会有更多的讨论啊 我觉得 这也是这个AI这一波带来的好处

**Suggested**

(no direct correction proposed)

**Reason**

Failed to parse model response: No JSON object found in model response

### [06:25:00 - 06:25:51] #568 `needs_review`

- Issue types: `semantic_drift`
- Suspicious spans: `多模特的范式`

**Original**

不是因为我看了十次二十次同样的内容 得到了这个心脏的standing 而是因为我自己在做我自己想做的事情 嗯 然后我能找到就是我我在看他talk的时候 每次都会去做这种翻译工作跟联想工作 我会发现哦 原来他说的这件事情在我现在的认知体系下 是可以这样解释的 他跟甚至现在的large model的方式 多模特的范式一点都不冲突 所有东西样说的话都可以被很清晰的map到我们现在在做的具体的事情上 并且指导我们可以走出也许某种local optimal 然后也许可以通向一个一个不一样的未来

**Suggested**

多模态的范式

**Reason**

‘多模特’可能是‘多模态’的误听，根据上下文语义，‘多模态’更符合技术术语和语境。

### [06:30:06 - 06:30:53] #577 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `三奥特曼`

**Original**

本质上他就是怎么样从一个在一个合资里面的呃语言模型或者说一个可以写代码的这样一个agent一步一步跳脱出来变成一个多模态模型的一个过程 我觉得大家可以看一看 然后到后面当然还有嗯我很喜欢的 比如说像万神殿啊 这也是一个我觉得是一个某种AI的预言对 他是一个动画 他的作者是 这个刘宇坤啊 他也是我的老乡 然后但他也是一个呃 当过什么律师当过马农 然后最后变成了一个呃小说家啊的这么一个人啊 非常非常厉害 我非常非常敬佩他 然后他他的书也很爱看对 然后啊 但这部剧之前也被三奥特曼推荐过 所以很多人也都看了 然后还有啊

**Suggested**

三体

**Reason**

‘三奥特曼’可能是‘三体’的误听，‘三体’是知名科幻小说，符合上下文语境。

### [06:33:09 - 06:34:02] #581 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `GEB啊 你有你有听说吗 就是呃 哥德尔、艾舍尔、巴赫啊`

**Original**

我觉得很好玩 嗯 我们的每一位嘉宾都会给我们的观众推荐一个人生之书 就是希望他是真的影响过你改变过你 你的会是什么呢 书吗 嗯 放哪 你得让我想一想 嗯 一本书我猜大家可能可能都经常推荐啊 然后但这本这这本书之所以对我的人生改变很大啊 我不我觉得不能说对人生改变很大 但是是我在本科的时候一个一个群体性的记忆 就大家会看这本书叫做呃GEB啊 你有你有听说吗 就是呃 哥德尔、艾舍尔、巴赫啊 中文名叫集异璧之大成的里面讲了很多关于啊 哲学关于数据逻辑 嗯 然后以及这三个字呢 嗯 一个人对吧 哥德尔巴赫跟埃舍尔对吧 一个啊

**Suggested**

GEB，你有听说过吗？就是《哥德尔、艾舍尔、巴赫》

**Reason**

重复的'你有'和'啊'属于口语冗余，'GEB'应为《哥德尔、艾舍尔、巴赫》的简称，需修正为完整书名。

### [06:38:11 - 06:38:44] #587 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `bdm的parameter`

**Original**

cdance这个真的让让我们这个今天的摄制组的朋友也可以来讲一下 我觉得非常非常强 然后我听说他们也是一个很大很大的模型 而且是一个moe的模型 不知道这个小道消息是否属实啊 因为在此之前我呃 我知道呃 大家没有人知道我这个小道消息是否属实啊 但是这个人能在这种diffusion model里面把moe做work 如果他们真的能够做到两个两百个bdm的parameter 并且是一个moe的架构 并且他们能够把这些数据吃进去啊 我觉得我觉得我觉得非常非常了不起啊 然后但是所有这些生成模型

**Suggested**

BDM 的参数

**Reason**

BDM 是技术术语，应首字母大写

### [06:38:45 - 06:39:30] #588 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `data问题`

**Original**

百分之九十还是一个data问题 啊 架构不重要 百分之九十或者我再说百分之九十五吧 都是一个data的问题 嗯 他的data本身就多 他的data本身多但多不够 嗯 他们应该做了大量的工作去清理这个数据 去做captioning 去校对这些数据的分布啊 他们diversity quality 以及他们和语言的这个prompt alignment的程度 呃 我相信这里面应该有大量的人参与这个工作 然后做了大量的事情 对 但是一旦你把这些事情做好之后 后续的事情啊 就变得简单很多 嗯 但我觉得

**Suggested**

数据问题

**Reason**

口语中'数据问题'更常见，'data问题'可能是ASR误识别

### [06:40:15 - 06:40:53] #590 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `Tractatus 什么Logico-Philosophicus`

**Original**

比如说大家说这个费曼讲 what i cannot create i do not understand 这件事情拿来当做一个unified model的背书 我觉得这件事情 这两件事情都让我实在是接受不了 嗯 第一件事情是什么呢 第一件事情是维特根斯坦 对吧 他当初讲的这个语言的边界 就是我世界的边界 是有强烈的前提的 他在这个Tractatus 什么Logico-Philosophicus 里面讲的这件事情是说 是说是说你你的 你的他指的语言 针对的是可以被命题 刻画的这个世界的边界 对 然后这件事情不代表

**Suggested**

Tractatus Logico-Philosophicus

**Reason**

书名《Tractatus Logico-Philosophicus》被错误地断开，应为完整书名

### [06:40:53 - 06:41:38] #591 `needs_review`

- Issue types: `proper_noun, technical_term`
- Suspicious spans: `这个这个一整套的这种这种啊 哲学体系`

**Original**

general的整个我们所说的这个世界 对 然后然后所以 所以这件事情第一就是他说的这个这个语言和他说的世界 本来就跟我们现在LM里面说的语言跟世界有区别 第二维特根斯坦在后期的时候已经完全推翻了自己之前的这个这个一整套的这种这种啊 哲学体系 他后来不再说这句话 然后他讲的事情是语言其实是一个游戏 所谓这种语言游戏 这样的一个概念 就说语言本身没有意义 这些symbol本身没有任何意义 他之所以发生意义是因为他跟真实世界的实践发生了关系 然后这件事情就很世界模型啊

**Suggested**

这个一整套的哲学体系

**Reason**

重复的'这个这个'和'这种这种'属于口语重复，但影响了专业术语的清晰度，需修正

### [06:41:38 - 06:42:22] #592 `needs_review`

- Issue types: `proper_noun`
- Suspicious spans: `维特根斯坎`

**Original**

就是就我们并不是说语言就能够去完完美美的去represent整个这个世界 我们说的事情是说 这个世界的实践 这个世界的action 决定了语言这个游戏 它的内涵跟外言 呃 again 我不懂哲学 我也不懂维特根斯坎 但我只是不喜欢看到大家paper里面 开篇先拉一句话放在这儿 啊 然后我觉得这件事情不符合我的审美 啊 然后包括费曼的句话也是一样 嗯 他说我看我I cannot create I do not understand 啊 这句话本身没错 但他说的这个create 跟understand 是说

**Suggested**

维特根斯坦

**Reason**

人名错误，应为哲学家维特根斯坦

### [06:42:22 - 06:43:02] #593 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `diffusion model 它反向传播的这么一个loss`

**Original**

比如说我们有一个世界的 我们要 我们要认识这个世界 我们要改造这个世界 我们要通过改造世界的方式去认识这个世界 whatever 啊 他说的这些事情还是在一个真实的具体的世界里面 要有某种action的 嗯 即使是你是上课 你去你去做一个PPT 你还是一个创造的过程 但现在很多人会把这句话拿来去做这种 呃 某种简单的unified system的一个背书 这件事情逻辑上也是不成立的 我们不能简单把create的背书 把create这件事情归结于一个diffusion model 它反向传播的这么一个loss

**Suggested**

diffusion model 它反向传播的这个 loss

**Reason**

术语表达不完整，'loss' 前应加 '这个' 以明确指代

### [06:43:56 - 06:44:55] #595 `needs_review`

- Issue types: `technical_term`
- Suspicious spans: `关于宇宙关于任何事情的定义啊`

**Original**

这个世界是一个巨大的世界模型吗 这个世界当然是一个巨大世界模型 那你能预测命运吗 呃 我觉得不能 为什么呀 嗯 因为我们资源不够 哦 你需要用地球这么大的一个计算机啊 或者说你要有一个有整个宇宙作为你的计算机 才能告诉你一个 关于 生命啊 关于宇宙 关于任何事情的定义啊 关于宇宙关于任何事情的定义啊 这个答案 嗯 这个答案最后可能是42 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯 嗯

**Suggested**

关于宇宙和任何事情的定义啊

**Reason**

重复的'关于'造成语义冗余，可能为转写错误。
