# Can humans make AI any better?

- URL: https://www.youtube.com/watch?v=2hcsmtkSzIw
- Model: `youtube-auto-caption-json3`
- Requested language: `en-orig`
- Detected language: `en`
- Refined at: `2026-06-05T08:19:37`

## Transcript

### [00:00 - 00:32]

In 1971, the US government agency ARPA launched a program to push the frontiers of speech recognition. ARPA set an ambitious 5-year goal, a system that could recognize a thousand different words with 90% accuracy. 5 years later, a team from Carnegie Melon demonstrated Harpy, an AI system capable of recognizing a,01 different words with 95% accuracy. The ARPA program was a success, but over the next decade, the

### [00:30 - 00:57]

core of Harpy's intelligence, an enormous knowledge graph, would be replaced by something completely different. Each of the over 14,000 nodes in Harpy's knowledge graph represents a single phone. One of the 98 basic sounds the team used to break apart spoken American English. The graph itself captures all the different ways these phones can be strung together to create sentences considered valid by Harpy.

### [00:56 - 01:24]

In this part of the graph, we can see the pathway for the phrases, tell me about China, tell me about Nixon, and give me the headlines. Each phone in Harpy's graph includes an expected frequency curve for the sound of the phone. These curves are tuned for the current speaker as audio comes in. For example, if I say tell me about China, a signal processing algorithm chops the waveform into blocks and the

### [01:23 - 01:51]

frequency content of each block is computed. From here, the frequency content of our first block is compared to the phones at the start of our graph. G in give and T in tell. T is a better match. So, we progress down this part of the tree. We then move to the second block in our waveform. This is the L intel and find its closest match. Block by block, we progress through our knowledge graph

### [01:49 - 02:18]

using a frequency matching score to guide our search, resulting in a final sentence. Note that the Harpy team also used a somewhat more sophisticated search method called beam search to help find the best overall path through the graph instead of just greedily choosing the best match at each step. The way Harpy's knowledge graph is constructed is painstaking and fascinating. First, a language design expert

### [02:15 - 02:44]

specifies a grammar. Harpy could not accept arbitrary sequences of words. This would have significantly degraded performance. Instead, a formal grammar was used to capture valid sentence structures for Harpy's intended use case of document retrieval. This small example Harpy grammar tells us that the word tell can be followed by me or us and then by all or about. From here, each word in Harpy's

### [02:42 - 03:08]

vocabulary is broken into individual phones. These breakdowns are themselves little graphs. Here's the pronunciation graph the Harpy team used for the word tell. Note that the graph branches due to the possibility of pronouncing tell in different ways. tell can be pronounced with an extra vowel sound in the middle. Replacing each word in our word graph with its phone breakdown, we

### [03:05 - 03:38]

get a larger graph. But we aren't done yet. When we speak, we often change the way words sound depending on the words around them. This is known as a juncture. When saying a phrase like about China, the T in about is often dropped, leaving about China. And in transitions like me all, a subtle extra Y sound known as a glide is added by some speakers to transition between vowels. The Harpy team accounted for this by

### [03:36 - 04:06]

creating rules to manipulate the phone graph to allow for various junctures between phones. Now, although Harpy achieved Arper's ambitious goal of 90% accuracy on a thousandword vocabulary, further scaling Harpy's performance proved difficult. And over the next decade, Harpy's knowledge graph was replaced by hidden markoff models. These models can still be understood as implementing a graph structure between

### [04:03 - 04:34]

phone nodes, but the edges of the graph are now probabilities that are learned from data. No language expert specified grammar and no linguistic expert specified juncture rules. This was a controversial shift at the time. Building our knowledge into AI systems was considered critical by many researchers. However, by the late 1980s and early 1990s, virtually all speech recognition systems had moved to hidden markoff

### [04:31 - 05:01]

models. And these systems were able to scale to much larger vocabularies of 5,000 and then 20,000 words. Decades later, in 2019, the computer scientist Richard Sutton published a highly cited essay that he called the bitter lesson. In his essay, Sutton points out that Harpy's replacement with hidden Markoff model based approaches is part of a broader trend. A trend that Sutton calls the biggest lesson from 70

### [04:58 - 05:28]

years of AI research. Specifically, that general methods that leverage computation are ultimately the most effective and by a large margin. and that trying to build human knowledge into our systems as the Harpy team did helps initially but then becomes highly counterproductive. The timing of Sutton's essay could not have been better. OpenAI had just released GPT2 a few weeks prior [music]

### [05:25 - 05:54]

and a new paradigm was just beginning to emerge. A general architecture, the transformer, focused on a simple learning objective, next token prediction, and trained with massive amounts of compute, could produce shockingly intelligent language models. For myself and many others, it seemed like we had learned the bitter lesson. We had found a method of creating AI systems that leveraged massive amounts

### [05:51 - 06:19]

of compute and appeared to rely only minimally on human assumptions about how AI systems should work. But then in 2025, something really surprising happened. Richard Sutton went on a podcast. In the first 10 minutes of Sutton's interview with Darkash Patel, it became clear that Sutton had a completely different take on large language models and the bitter lesson. So, I mean, it's interesting because you

### [06:17 - 06:50]

wrote this essay in 2019 titled The Bitter Lesson, and this is the most influential essay perhaps in the history of AI, but people have used that as a justification for scaling up LLMs because in their view, this is the one scalable way we have found to pour ungodly amounts of compute into learning about the world. And so it's interesting that your perspective is that the LLMs are actually not bitter lesson.

### [06:47 - 07:25]

>> It's an interesting question whether uh large language models are are uh a case of the bitter lesson. >> Yeah. >> Because they are clearly um a a way of using massive computation things that will scale with computation up to up to the limits of the internet. >> Yeah. uh but they're also a way of putting in lots of um human knowledge and uh so so this is an interesting question um it's

### [07:20 - 07:59]

a sociological or industry question uh will they reach the limits of of of the data and and be superseded by things that that are can get more data just from experience rather than from uh from people. Uh in some ways it's a classic case of the of the of the bitter lesson with the more the more human knowledge we put into the large language models the better they can do and so it feels good. Um

### [07:55 - 08:28]

and yet uh one well I in particular expect there to be systems that can learn from experience which could well perform much much better and be much more scalable. In which uh case it will be another instance of the bitter lesson that the things that that used human knowledge were eventually superseded by things that just um trained from uh experience and computation. >> This is such a remarkable moment. Sutton

### [08:26 - 08:54]

is basically telling us that much of the field has interpreted his essay in exactly the wrong way. that large language models are an example of the bitter lesson, but a negative example, one that like Harpy relies far too much on human knowledge since LLMs are trained on human generated text. So, is Sutton right? Will LLMs hit a performance barrier due to their reliance on human knowledge and need to

### [08:53 - 09:23]

be replaced with very different types of AI systems? Sutton ends the bitter lesson with these lines. We want AI agents that can discover like we can, not which contain what we have discovered. Building in our discoveries only makes it harder to see how the discovering process can be done. So what would an AI system look like that can discover like we can? The primary way large language models are

### [09:21 - 09:48]

trained today is through supervised learning. Given some training text, for example, the first line of Harry Potter, the text is broken into little pieces known as tokens, and the model is trained to predict the next token given all the tokens that come before. So given the input Mr. and Mrs. Dersley of, the model is trained to predict the token for the word number. And given the input Mr. and Mrs. Dersley of number,

### [09:46 - 10:15]

the model is trained to predict the token for the word for and so on. Token by token, we're teaching the model what to say. And Sutton's criticism here is that like Harpy, this process relies too much on human knowledge since we're training our model to imitate humans. So, how else might we train AI systems? Sutton is generally known as the father of reinforcement learning. One of the

### [10:13 - 10:40]

most compelling modern examples of AI systems trained using reinforcement learning instead of supervised learning are Google Deep Minds Alph Go and Alph Go Zero agents. Now, Alph Go and Alph Go Zero are game playing agents, not large language models, but there are some really interesting parallels here. Now, before we see exactly how reinforcement learning allows us to push beyond the limits of human knowledge, if

### [10:38 - 11:06]

you're someone who's obsessed with this stuff and looking for your next career move, check out this video sponsor, Tufalabs. Tufalabs recently won the ARC AGI3 preview competition, where AI agents must learn to play and win completely novel games that the agents developers have never seen before. Tufa Labs is an independent AI lab based in Zurich and puts out really interesting research on the frontiers of LLMs and

### [11:04 - 11:32]

reinforcement learning. In this recent paper, the team achieved very impressive performance on the MIT integration B challenge by creating a self-improvement loop where an LLM creates its own math practice problems and learns to solve them via reinforcement learning. Tufa Labs is serious about compute and is currently expanding their infrastructure with two Nvidia NVL72 GB300 racks which

### [11:31 - 11:59]

is a significant amount of compute given the relatively small team size. TUFALabs is fully self-funded by applying ML to quantitative finance. This funding structure is similar to deepseats. If this sounds interesting, you can apply at tufalabs.ai/join. Now back to the bidder lesson. When building Alph Go, the first AI system that reached superhuman performance on the board game Go, the DeepMind team

### [11:57 - 12:25]

first trained a supervised policy network. In the jargon of reinforcement learning, an agent's policy determines what action an agent will take in a given state. In the game of Go, the current state is the board position, and the action is where the agent will place its next stone on the board. The DeepMind team used a deep neural network to learn this policy. This part of DeepMind's solution is strikingly

### [12:23 - 12:51]

similar to large language model training. Given some input text, large language models return a probability for each token the model could say next. And given an input board position, Alph Go's policy network returns a probability for each board position where Alph Go could place a stone. Note that Alph Go used a convolutional architecture while LLMs generally use transformers. But this distinction isn't

### [12:49 - 13:19]

really significant for our comparison here. Very similar to LLM training, Alph Go's policy network was first trained using supervised learning on human generated examples, learning to match expert human players moves in recorded games. The resulting supervised learning trained policy network is a fairly competent Go player. Evaluating the model in a tournament against other GO agents resulted in an ELO rating of 1517

### [13:17 - 13:47]

putting the network at mid amateur level. Now in the reinforcement learning paradigm agents learn not from direct supervision but instead through interacting with their environments. In the case of Alph Go, this just means taking the very natural approach of learning from actually playing the game. The DeepMind team took their trained supervised policy network and had it play against various versions of itself.

### [13:45 - 14:12]

After each game, the moves taken by the winning model were used as positive training examples to train the policy network. And the moves taken by the losing model were used as negative examples. This training process is very similar to learning from human expert moves. The key difference here is that these moves are generated by two policy networks actually playing go and the underlying signal the model learns from

### [14:09 - 14:39]

is not the opinion of a human expert but instead the outcome of a real game. This approach is known as a policy gradient method and is a key technique in reinforcement learning initially developed by Sutton and others in the 1990s. Now, it turns out that the reinforcement learning trained policy network alone was not enough to deliver superhuman Go performance. The DeepMind team needed one more big

### [14:35 - 15:03]

idea from reinforcement learning. It turns out there's another way to set up our learning problem here, and it's actually an older and arguably more central reinforcement learning idea than the policy gradient method we've seen. Instead of training a network to predict the move that should come next, what if we trained a network to measure the quality of a given board position or more concretely to estimate the

### [15:01 - 15:28]

probability of winning starting from a given board position. This approach is broadly known in reinforcement learning as value function estimation where the term value refers to expected future rewards in this case winning the game. Value functions play a central role in Sutton's canonical text on reinforcement learning. The most important component of almost all reinforcement learning

### [15:26 - 15:53]

algorithms we consider is a method for efficiently estimating values. The central role of value estimation is arguably the most important thing that has been learned about reinforcement learning over the last six decades. To make use of this reinforcement learning idea, the Google DeepMind team trained a second neural network that they called a value network. This network took in the same board position

### [15:50 - 16:16]

inputs as our policy network. But instead of predicting what move should come next, the value network predicts the probability of Alph Go winning the game from that position. The DeepMind team trained their value network on board positions from games between different versions of Alph Go. again avoiding learning from human gameplay. Finally, the DeepMind team brought together their policy and value network

### [16:14 - 16:44]

with a method called Monte Carlo tree search to create a formidable Go agent. The policy network allows Alph Go to narrow down the number of next possible moves, while the value network provides a strong estimate of the probability of winning if Alph Go continues playing down a given branch of the tree. Alph Go famously went on to defeat Lisa Dole in 2016, the second ranked Go player in the world at the time. The

### [16:43 - 17:10]

following year, the DeepMind team revealed Alph Go Zero, an even stronger player than Alph Go that remarkably did not learn from any human games. Instead, relying only on reinforcement learning from real gameplay. By learning from real interactions with their environments, Alph Go and Alph Go Zero dramatically outperformed agents trained to imitate human gameplay using supervised learning,

### [17:08 - 17:35]

discovering their own ways to play the game. Alph Go's playing style has been described by experts as playing against an alien and is from an alternate dimension. These are the types of AI systems that Sutton is referring to when he says, >> "Oh, well, I in particular expect there to be systems that can learn from experience and which could well perform much much better and be much more scalable."

### [17:33 - 17:58]

>> This really makes me wonder if our current generation of language models are constrained in the same way as the AlphaGo policy network that was trained with supervised learning was unable to discover on their own limited to imitating human language and intelligence. Now, it's important to note here that reinforcement learning does already play an important role in large language model training.

### [17:56 - 18:24]

After LLMs are trained on next token prediction using supervised learning, reinforcement learning through human feedback or RLHF is used to align models to human preferences using reinforcement learning techniques. And a great deal of recent LLM progress has been driven by reasoning models that make use of reinforcement learning with verifiable rewards or RLVR where LLMs are trained with

### [18:22 - 18:49]

reinforcement learning to find their own paths to solving problems with known answers such as math problems and coding. Pre-training on human generated text and then using reinforcement learning to allow models to discover on their own is an exciting direction, but it remains to be seen how far this approach can take us. In 2025, David Silver, the lead researcher of the AlphaGo project,

### [18:47 - 19:14]

teamed up with Richard Sutton to write an essay called Welcome to the Era of Experience. Silver and Sutton argue that LLMs are currently limited by human knowledge, giving an interesting thought experiment. If we trained an LLM on human knowledge from 5,000 years ago, it would reason about the physical world in terms of animism. If we trained on human knowledge from a thousand years ago, it would reason in

### [19:11 - 19:42]

theistic terms, 300 years ago in terms of Newtonian physics, and 50 years ago in terms of quantum physics. Moving from one paradigm to the next requires actually interacting with the physical world as Silver and Sutton say in order to overturn facious methods of thought. From here, Sutton and Silver argue that we're on the threshold of a new era of AI where agents will learn from real

### [19:39 - 20:09]

world reward signals instead of human knowledge, discovering new ways to optimize measures like cost, health metrics, climate metrics, profits, sales, and energy consumption. Sutton and Silver give the example of DeepMind's alpha proof agent which combines LLMs and reinforcement learning to discover its own very impressive methods of mathematical reasoning. So, have we learned the bitter lesson or

### [20:07 - 20:37]

are we just repeating it? When we look back on LLMs one day, will they feel like harpy so clearly limited by human knowledge? And if so, is reinforcement learning the answer? And can LLM serve as the scaffolding that unlocks this next frontier? Or do we need to try something totally different? My take here is that the bitter lesson in Sutton and Silver's reinforcement learning perspectives form a really

### [20:34 - 21:00]

helpful lens onto the limitations of our current generation of AI. I'm more skeptical about a reinforcement learning renaissance being around the corner. mostly because the domains we've seen reinforcement [music] learning perform really well in like playing games, mathematical proofs, and coding, still feel very removed to me from many of the real world problems that we care about.

### [20:58 - 21:04]

Either way, it will be fascinating to see what happens next.

### [21:06 - 21:34]

The Welsh Labs team and I have written a whole new book on AI. It's beautifully illustrated and is a great way to dig deeper into the topics we cover in these videos. This is the book I've always wanted to write. We've really leaned into the visuals. The book has hundreds of figures. I especially like these full page spreads. This one shows how loss landscapes are computed. On the next page, we jump into this

### [21:32 - 21:58]

super highquality overhead contour plot view of our landscape. and we show how we might expect our model to work its way through valleys to reach its global minimum, but it instead creates what looks like a wormhole on our loss landscape. We're putting a huge amount of effort into each chapter to create these kinds of visuals and deep explanations, trying to give the most visceral feel we can

### [21:55 - 22:22]

for how this stuff really works. Each chapter includes supporting Python code that walks [music] through the key results from that chapter. And there's also a supporting GitHub repo as well that's a bit more comprehensive. At the end of each chapter, you'll also find exercises. We've put a ton of thought into these. Here's an exercise from the chapter on backpropagation where you're given a small complete

### [22:20 - 22:45]

neural network and asked to move some data through the network using a few equations. Then you're asked to compute the network's gradients and use your computed gradients to fill in steps in the model's real learning process. These exercises are designed to get you as hands-on as possible with modern AI and solutions are in the back of the book. Most of the exercises are written or programming, but my favorite is

### [22:44 - 23:10]

probably this spread that [music] gives you instructions for building your own perceptron machine. The book starts with a fresh take on the fundamentals, the perceptron, gradient descent, [music] backpropagation, deep models, and alexet. and then uses this foundation to dive into cutting edge topics including neural scaling laws, mechanistic interpretability, and AI image and video generation models like Sora.

### [23:09 - 23:27]

Each chapter goes along with a Welch Labs video that came out over the last 18 months. I really think that the book is the best way to get deeper into each video's topic. The book is great for self-study, AI courses, or just looks great on your coffee table.
