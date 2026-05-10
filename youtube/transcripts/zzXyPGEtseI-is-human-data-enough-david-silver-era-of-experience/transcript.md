# Is Human Data Enough? With David Silver

- URL: https://www.youtube.com/watch?v=zzXyPGEtseI
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Refined at: `2026-05-08T19:14:29`

## Transcript

### [00:00 - 00:21]

I guess this is, in a way, you're sort of thumping the table saying large language models are not the only AI. We're going to need our AIs to actually figure things out for themselves and to discover new things that humans don't know. So if you remove that human feedback aspect, do you still end up with models that are grounded? I almost want to argue the opposite. This is sometimes called the bitter lesson of AI.

### [00:21 - 00:36]

We really want to believe that all of the knowledge that we've accumulated as humans is really important. AlphaGo for me is not just teaching me something new technically. Maybe it opens my mind. It changes my mind.

### [00:40 - 00:57]

Welcome back to Google DeepMind, the podcast. My guest today is the inimitable David Silver, an original DeepMinder, one of the key people behind the phenomenal success of AlphaGo, the first program to master the world's most complex board game and achieve superhuman performance. I'm going to be talking to you about the first program to master the world's most complex board game and achieve superhuman performance.

### [00:57 - 01:14]

I'm going to be talking to you about the first program to master the world's most complex board game and achieve superhuman performance. Now, at the end of today's podcast, we have a little extra treat for you, a conversation with David and Fan Hui, the first professional Go player to take on the AI. But now, David has a bold idea about the direction that AI should go in next.

### [01:14 - 01:28]

After all of the current buzz and excitement and achievements of multimodal models, David has a plan for the path towards superhuman intelligence, a new phase which he calls the era of experience. David has a bold idea about the direction that AI should go in next. After all of the current buzz and excitement and achievements of multimodal models, David has a bold idea about the direction that AI should go in next.

### [01:28 - 01:56]

This is a profound idea and not one without risks. David, welcome to the podcast. Hi, it's great to be here. Real pleasure. Thank you. Okay, so I have spent the weekend with a very enjoyable read of your position paper. And in it, you are talking about the era of experience. Summarize for us, what do you mean by that? What I mean is that if you look at where AI has been for the last few years, it's been in the

### [01:56 - 02:18]

what I call the era of human data, which is that all of these AI methods, they're based on one common idea, which is we extract every piece of knowledge that humans have, and you kind of feed it into the machine. And that's one incredibly powerful way to do things. There's another way to do things. And this is what's going to lead us into the era of experience,

### [02:18 - 02:44]

which is where the machine actually interacts with the world itself. And it generates its own experience. And if you think of that data as fueling the machine, then that will lead to this next generation of AI that we can think of as the era of experience. I guess this is in a way you're sort of thumping the table saying, large language models are not the only AI, right? Like there are alternatives.

### [02:44 - 03:06]

There are different ways that we can approach this. I think we've really got a lot out in the field of AI of building large language models, like how do we do this? How do we do this? How do we do this? How do we do this? How do we do this? Harnessing the vast quantity of human, particularly natural language data that's out there and kind of assimilating that all into a machine that knows everything that humans

### [03:06 - 03:26]

have ever written down. But at some point, we need to get past that. We want to go beyond that. We want to go beyond what humans know. And to do that, we're going to need a different type of method. And that type of method will require our AIs to actually figure things out for themselves and to discover new things that humans don't know. And I think that's going to be a whole new era of AI that's going to

### [03:26 - 03:51]

be incredibly exciting and profound for society. Well, okay, then let's talk about some other sort of famous AIs, famous algorithms that have employed different types of methods. Most notably, AlphaGo and AlphaZero, which of course, notoriously beat the world's best Go players about a decade ago, right? Tell us about the techniques that we use in that and how they differ from large language models that we see today.

### [03:51 - 04:08]

AlphaZero in particular is very different from the type of human data. AlphaZero in particular is very different from the type of human data that we see today. AlphaZero in particular is very different from the type of human data that we see today. Because it literally uses no human data. That's the zero in AlphaZero. So there is literally zero human knowledge that's pre-programmed into this system.

### [04:08 - 04:28]

And so what's the alternative? How do you learn Go knowledge if you're not copying humans and you don't really know in advance the right way to play? Well, the way you go about it is through a form of trial and error learning, where AlphaZero basically played itself millions of games of Go, or chess, or whatever the game is. That it was wanting to play.

### [04:28 - 04:44]

Bit by bit, it figured out, oh, if I play this move, this kind of move in this kind of situation, then I end up winning more games. And then that's a piece of experience that is used to fuel it to become stronger. And then it will play a little bit more like that. And the next time it will discover something new and say, you know, there'll be some new pattern.

### [04:44 - 05:06]

It's like, oh, when I use this particular pattern, I end up winning more games or losing more games. And that feeds the next generation and so forth. And that learning from experience, this learning from the agent's self-generated experience is enough and was enough in AlphaZero to fuel its progress all the way from completely random behavior, all the way up to the strongest

### [05:06 - 05:26]

chess and Go playing programs that the world has ever known. They didn't start off just as like random, random empty boxes though, right? That kind of found how to play Go from nothing. I mean, initially when you were designing your Go algorithms, you'd worked out a way to encode Go games and then feed them in as a database, right? Yeah, that's right.

### [05:26 - 05:51]

So the original version of AlphaGo, the version which famously beat Lisa Dahl in 2016, this version of AlphaGo actually did use some human data to start it off. So we basically fed it a database of human professional moves and it learned, it ingested those human moves, and that gave it a starting point. And then it learned for itself by experience from that point onwards.

### [05:51 - 06:14]

However, what we discovered a year later was that, you know, there's a lot of things that the human data wasn't necessary. That you could actually throw out the human moves altogether. And what we showed was that actually the resulting program, not only was it able to recover this level of performance, it actually worked better and was able to learn even faster than the

### [06:14 - 06:36]

original AlphaGo to achieve a much higher level of performance. I mean, that is such a strange idea. It's such a strange idea that you throw away the human data and you find not only that, not only was it not necessary, but it was actively limiting performance in a way. One of the hard lessons for people in AI, this is sometimes called the bitter lesson of AI,

### [06:37 - 07:00]

is that we really want to believe that all of the knowledge that we've accumulated as humans is really important. We really want to believe that. And so we feed it into our systems. We build it into our algorithms. What happens is that actually that makes us design the algorithms in a way which is maybe fitted to the human data and is less good at actually learning for itself.

### [07:00 - 07:23]

And what happens is if you throw out the human data, you actually spend more effort on how the system can learn for itself. And that's the part which can then learn and learn and learn forever. The bitter lesson. In a way, it's sort of saying, accepting that it's possible that something could PlayGo better than humans can and sort of removing that ceiling in a way. That's right. That, you know, human data.

### [07:24 - 07:40]

It's really helpful. It's really helpful to get you off the ground. But there is a ceiling to everything that humans have done. And, you know, we see that in Go. There was a maximum level of performance that humans have ever achieved. And we need to break through these ceilings. And in AlphaZero, we were able to break through that ceiling by building a system that learned

### [07:40 - 08:03]

for itself by self-play and got better and better and better until it blasted through that ceiling and went far beyond. And I think the idea of the era of experience is that we find the methods that allow us to break through that ceiling everywhere. We build AI systems that... become superhuman in all of the capacities that humans seem so amazing, but we find the way to go beyond that.

### [08:03 - 08:25]

Let me just stick with Go for a second, okay, before we get onto the other ways that you can get rid of human data and thus improve on human ability. Because it sort of sounds a little bit... When you say, let's just get rid of all of the games of Go that humans have played and start with nothing, it sort of sounds like a magic trick. Just tell me a little bit about that.

### [08:25 - 08:48]

Just tell me a little bit about the techniques that you're really using there in order to get a machine to, as you say, chain together thousands and thousands of different ideas in order to be amazing at the game of Go. Well, the main idea is an approach that we call reinforcement learning. And the idea of reinforcement learning is you basically give the outcome of your game a number.

### [08:48 - 09:10]

And we say, you know, plus one if you win and minus one if you lose. One point. Exactly. Exactly. And... Yeah. Exactly. Exactly. Exactly. Exactly. Exactly. Exactly. And what we do then with reinforcement learning is we get the system to basically... We give it a reward each time it does something right, and we train the system to basically reinforce. That means do more of the things that get more reward.

### [09:10 - 09:27]

In terms of, for example, if you've got a neural network like we do in AlphaGo that's picking the moves, what you want to do is tweak the weights of your neural network a little bit in the direction that gives you more reward. And that's the main idea of reinforcement. And that's the main idea of reinforcement learning. A game that goes quite long.

### [09:28 - 09:48]

How do you make it so that you do the right moves in the beginning so that you end up with the right outcome towards the end? Like, how do you distribute, as it were, that one single point that you're offering? How do you work out which bits of the game are important, I suppose? So this is a really important problem. It's called the credit assignment problem.

### [09:48 - 10:07]

And the idea is that if you've, yeah, you're absolutely right, that you could have had, you know, 100 or 200 or 300 points. Or 300 different moves. And then at the end, you just get one bit of information saying, you know, win or loss. And you somehow have to work out which of the moves in the game were responsible for winning and which of the moves in the game were responsible for losing.

### [10:07 - 10:33]

And there's lots of ways to do that. The simplest way is just to assume that everything that you've done contributes a little bit to that outcome at the end. And it sort of all comes out in the wash. One of the biggest moments of the AlphaGo story was move 37. Everyone always references. Just tell me about that. Move 37 was a move that happened in the second game of AlphaGo against Lee Sedol.

### [10:33 - 10:54]

AlphaGo played a move that defied everyone's expectations. The traditional idea in the game of Go is that you play your moves typically on the third line or the fourth line of the board, because this either gives you territory for the third line or influence on the fourth line. And you never go below or above that. It just wouldn't make sense to humans. AlphaGo played on the fifth line.

### [10:54 - 11:14]

And it somehow played this in a way that just made everything make sense in the board. It kind of connected everything together with this move on the fifth line. And it was so alien to humans that we estimated that only one in 10,000 probability that a human would ever think of playing this move. Humans were shocked by this move, and yet it helped win the game.

### [11:14 - 11:36]

And so it was a moment where humans said, look, here's something creative that happened. Something that a machine came up with that was different from the way humans traditionally thought about the game. That actually was a big piece of progress and took us beyond the kind of confines of human knowledge. And I guess if we really do want to advance AI, we sort of do want those alien ideas, as you put it.

### [11:36 - 11:59]

Do you think you've seen an equivalent of Move 37 with large language models? Move 37 in some ways was special because it was the first moment. It was the first time that people had seen a big breakthrough like this. The second thing to say is that because we've been in the era of human data. We've focused a huge amount on reproducing human capabilities, and we've focused much

### [11:59 - 12:27]

less on going beyond them until we really emphasize systems learning for themselves to go beyond human data. We won't see huge breakthroughs, the equivalent of Move 37 in the real world. Because when you're anchored in human data, you're only ever going to have human like responses. That's right. And I think there are things you can do that. That. Allow you to maybe do things in the middle a little bit.

### [12:27 - 12:52]

So if you push me to say what's the greatest Move 37 like moment, I would probably pick out some work by scientists at MIT who discovered a new antibiotic that no human knew about. And I think that's an incredible, incredible discovery of massive importance to humanity. So in that sense, it goes way beyond Move 37. But what I like about Move 37 is that it's not just a single discovery.

### [12:52 - 13:14]

It's one of an infinite series of discoveries, where the system can just keep on learning and learning and learning. And Move 37 is important to me because it represents just a single point in that infinite sequence of discoveries that can happen once you've got this kind of approach of learning from experience. Rather than actual result in its in and of its own right. Yeah, that's right.

### [13:14 - 13:26]

Give me a brief rundown of how AlphaZero worked. So AlphaZero is surprisingly simple. I mean, there's some very complicated algorithms out there in the world. But it's not just a single discovery. It's one of an infinite series of discoveries where the system can just keep on learning and learning. Yeah. And it's a very complex set of activities. It's a whole wide range of activities that you can do in a few minutes.

### [13:26 - 13:43]

Yeah. So AlphaZero is a big, really complex, really complex world. But this one is really straightforward from, you know, that side of things. So all you do is you start with a policy, a way to pick moves, and a value function, which is a way to evaluate games and evaluate moves and say whether they're good or bad. So you start with that, you run a search, and then what you do is you take the best

### [13:43 - 14:03]

move according to your search, and you train your policy to do more things like that, to do more of the good moves according to your search. And you train your value function based on how the game actually plays. hand out when you played a game with this search. And that's it. You just iterate that millions of times and out pops a superhuman game player. It's like magic, basically.

### [14:03 - 14:26]

It does sometimes feel like magic. I remember the first time that really felt like magic to me was when we had just completed AlphaZero on chess. Someone had the idea of trying it on a different game. So we plugged it into a game that none of us could play, a game called Shogi, which is Japanese chess. And we had no idea how to play this game, but we plugged it in. What, you didn't even know the rules?

### [14:26 - 14:49]

The system knew the rules. The agent, we taught it the rules. So we knew the rules of the game, but none of us had the first clue of how to really, you know, strategy or tactics. It would have been like blunder after blunder if we'd been playing this game. And we just plugged it in. And it was literally the first ever time we ran AlphaZero on Shogi. We had no idea.

### [14:49 - 15:13]

We had no idea whether it was good or not. We couldn't evaluate it. We sent it off to Demis, who's actually a reasonably strong player, of course. And he said, hmm, this looks quite good. I'm sending it to the world champion. And the world champion said, hmm, I think this is superhuman. And so it literally felt like magic because we, you know, we just pressed go on this system and had no idea of the process

### [15:13 - 15:26]

and how it got there. But somehow out popped a superhuman Shogi player. Yeah, because it's an actual Shogi. It's a superhuman Shogi, double shogi player. It's a superhuman Shogi player. It's actually a superhuman Shogi. Can AI design its own reinforcement learning algorithms? Well, funnily enough, we have actually done some work in this area, work we actually did

### [15:26 - 15:47]

a few years ago, but is coming out now. And what we did was actually to build a system that through trial and error, through reinforcement learning itself, figured out what algorithm was best at reinforcement learning. It literally went one level meta, and it learned how to build its own reinforcement learning system. And incredibly, it's an AI system. So it's

### [15:47 - 16:06]

a big deal. Yeah, it's a huge deal, the big deal. And it's ever been around two or three actually outperformed all of the human reinforcement learning algorithms that we'd come up with ourselves over many, many years in the past. I mean, this is the same story over and over again. The more of a human you put into something, the worse it acts, the worse it performs. Take the human out, does better.

### [16:06 - 16:31]

If AlphaGo and AlphaZero then are really exceptional examples of reinforcement learning used to the best it can be, you still find reinforcement learning in the large language models that we have at the moment, right? Tell me about how they're integrated into these systems. So reinforcement learning is used in almost all large language model systems. And the main way it's used is by combining it with human data.

### [16:31 - 16:55]

Unlike the AlphaZero approach, this means that the reinforcement learning is actually trained on human preferences. So the system is basically asked to produce outputs, and then a human says, this one is better than this other one. And the system becomes more like the one that the human prefers. This is called reinforcement learning from human feedback, and it's been massively important in LLMs.

### [16:55 - 17:25]

And it's helped transform them from systems that just blindly mimic any kind of data that you see on the internet into systems that actually usefully produce answers to the kind of questions that people really want to see. And so it's an incredible advance. However, I think we've thrown out the baby with the bathwater. These reinforcement learning from human feedback systems or RLHF, they're very powerful,

### [17:25 - 17:50]

but they do not have the ability to go beyond human knowledge. Like if a human rater doesn't recognize some new idea and under appreciates that there are some series of actions that would actually end up being far better than some other series of actions, there is no way that the system will ever learn to find that sequence because the raters might not understand that better. That human feedback element though,

### [17:51 - 18:16]

it does seem to give these models some sense of grounding. I know the last time we spoke, grounding was like this really big topic, this idea that you want these algorithms to have a conceptual understanding almost of the world that we're living in. So if you take away or you remove that human feedback aspect, do you still end up with models that are grounded? I almost want to argue the opposite. Oh.

### [18:16 - 18:44]

I want to say that when we train, we train a system from human feedback that it is not grounded. And the reason is that we are basically, the way our LHF systems normally work is the system presents its response, its answer to a question, for example, and a rater says that's good or bad before the system actually does anything with that information. So it's like the human is prejudging the output of the system.

### [18:44 - 18:46]

So for example, if you're asking for

### [18:48 - 19:13]

a cake recipe from an LLM, the human rater will look at the recipe that's output by the system and judge whether that recipe is good or bad before anyone has actually made the recipe and eaten the cake. Yeah. And in that sense, it's ungrounded. Like a grounded outcome would be someone actually eats the cake and the cake is either delicious or disgusting. And then you've got grounded feedback that says,

### [19:13 - 19:33]

you know, this cake really was a good cake or this cake was a bad cake. And it's that grounded feedback that allows the system to iterate and discover new things because it can try out new recipes that maybe, you know, expert chefs presume will be disgusting, but actually turn out to be delicious. Yeah, like a monster munch muffin or whatever. Exactly, yeah.

### [19:33 - 19:55]

Who knew that that's the most delicious food that ever existed? Okay, that's interesting, though, because I have heard, I mean, even a conversation with Demis talking about how grounding gets into these models, how they kind of have built this conceptual understanding of things. And it sounds almost like what you're saying is that the grounding that they have is like a sort of superficial level of grounding, maybe?

### [19:55 - 20:18]

I think human data is grounded in human experience. So it's like the LLMs are sort of inheriting all of that information that humans may be figured out from their own experiments. For example, in science, you know, a human might have tried to walk across water and discovered that they fell in, and then they might have created a boat and discovered that, that floated.

### [20:18 - 20:45]

And all of that information can be inherited somewhat by the LLM. But if we want a system that actually makes discoveries and discovers some completely new form of propulsion across water, or, you know, some completely new mathematical idea, or some completely new way to... Part the seas. Yeah, new medicine and new approach to biology, the data just isn't there. And the system needs to figure out for itself,

### [20:45 - 21:02]

through its own kind of experimentation, its own trial and error and its own grounded feedback, whether that's a good idea or a bad idea. I got to talk to Aurel, Aurel Vinales. He said that there was this real problem that we were running out of human data. The solution, I suppose, as he was describing it, was that you can then create synthetic data

### [21:02 - 21:23]

by using large language models to generate more human-style dialogue. I mean, this is related, right, to that idea. It's just rather than using LLMs to create more human dialogue data, you're going about the solution in a different way. That's right. Synthetic data can... can mean a lot of things, but normally it would mean that you've got some process where you kind of take your existing LLM

### [21:23 - 21:45]

and you use it to generate some set of data. And I guess the argument is, similar to the ceiling that we have from human data, that however good that synthetic data is, they will reach a point where that synthetic data is no longer useful to the system becoming stronger. So the beauty of a self-learning system, where the fuel of the system is actually experience, is that as the system starts to get stronger,

### [21:45 - 22:10]

it starts to encounter problems that are exactly appropriate to the level it's at. So it will always be generating experience that allows it to solve the next problem that it's encountering. And so it can just get stronger and stronger and stronger forever. There is no limit. And that, I think, is what differentiates this particular approach of using self-generated experience from other forms of synthetic data.

### [22:10 - 22:25]

Just returning to your cake example, though, I mean, if you kind of follow that through, somebody eats the cake and says, oh, yeah, that's a great idea. and says yes this was delicious you're using the human feedback then at the end of the process anyway are we talking about that or are we talking about maybe having systems that are completely

### [22:25 - 22:44]

untethered from humans and are embodied or in the physical world somehow so that they can get their feedback in that way the ideal is that like alpha zero we have systems which are able to generate vast volumes of self-generated data experience that they can then verify for themselves and in many domains that's going to be possible and in many domains it's not going to be possible

### [22:44 - 23:04]

in the ones where it's not possible you know we have to acknowledge that humans are a big part of the of the environment that we're in we have to acknowledge that that they're a part of the world that we want our agents to live in and so it seems reasonable to think of humans as a part of that environment and to think of the way that they behave as part of the observation that

### [23:04 - 23:28]

that the agent receives i think the thing which i'm pushing back against and saying is not grounded is not that it's the fact the rewards that the agent learns from is coming from a human's judgment of like whether this sequence of actions is good or bad right and the system is not judging for itself based on the consequence of those actions in the actual world we shouldn't make

### [23:28 - 23:44]

you know human data a privileged part of the agent's experience it's just observations in the world and we should be able to learn from that like any other data if we go back to that to the alpha go example earlier of assigning that reward that one point that it gets at the end is this almost like the way that we're handling ai at the moment is that

### [23:44 - 24:10]

the algorithm does its first 10 moves or 15 moves and then then we insert a human in who says yes that's a good first 10 moves and doesn't allow the whole process to to to kind of execute fully before you input that little bit of feedback that's exactly right so imagine imagine that we were training alpha go and after every single move like our best go player comes in and says

### [24:11 - 24:29]

oh that move that move was amazing oh oh no no that move was totally wrong and then we we get that feedback and we put it in and the system learns to pick the move that the human prefers it would not end up discovering move 37 because it would just end up playing like the human thinks is a good game of go and it would never discover the new ways to

### [24:29 - 24:44]

play go that that human didn't know about what you're saying makes a lot of sense in that environment there are other environments too where i think that this makes a lot of sense i'm thinking here about the pinnacle of human thought of mathematics um tell me what's been going on in that space it's like you said it's like you said it's like you said it's like you

### [24:44 - 25:06]

say it is an incredible human endeavor that's had millennia of human effort going into it and so in many ways it does represent like literally the the limits of achievement by by the human mind and so naturally we turn to it for ai to see can we achieve those same levels of performance that you know humans have achieved over all of those years of endeavor we recently put together um i

### [25:06 - 25:12]

think it's a very exciting piece of work called alpha proof it is a system that learns through

### [25:14 - 25:37]

a method of proofing mathematical problems if you give it a theorem and you don't tell it anything about how to actually prove that theorem it will go away and figure out for itself a perfect proof of that of that theorem we can actually verify and guarantee that this proof is correct one thing which is interesting about this is that it's the exact opposite of how llms normally work if you

### [25:37 - 26:00]

ask llms to prove a mathematical problem at the moment they will normally output some informal and say just trust me this is correct and it might be correct but it might not be because we know that llms tend to hallucinate a lot they can make things up and the nice thing about alpha proof it will actually guaranteed produce the truth so let's think of an example here to kind of anchor

### [26:00 - 26:21]

this in people's minds prime numbers are something that can't be divided uh by anything but themselves and one and there are infinite number of them off you go prove it so the way alpha proof works is it's trained on millions of different examples of of theorems not just one and what happens it goes off and it trains on them and

### [26:21 - 26:44]

to begin with it can't solve you know the vast majority of them 99.999 of the theorems it it just can't do and these are theorems that that humans have already proved are you feeding in we feed into the system um something like um a million different theorems that humans have come up with themselves but we don't provide the human proof

### [26:44 - 27:04]

we just provide the questions but not the answers so you're giving it stuff that you know is true but you're just not not not telling it how to prove it and sometimes we don't even know it's true because what we actually do is we take the the human theorem the human question turn it into a formal language these aren't using language in the sense that language models are using but they

### [27:04 - 27:13]

are using a form of language like a mathematical language that's right so um in fact we do use small large language model and that allows us to output

### [27:15 - 27:36]

programming languages and in particular we use a programming language that's called lean that allows all of mathematics to be expressed and so it's an amazing idea that mathematicians have come up with that you can actually formalize all of these kind of things that we normally talk about in english language or whatever language you happen to be speaking can be transformed into a

### [27:36 - 28:02]

perfectly clear verifiable mathematical language that allows all of the ideas of maths to be expressed and also all of the ideas of mathematical proof to be expressed so you can say for example that a implies b and b implies c then there's a way to go from that to a implies c and that's the kind of thing that you can do in this mathematical programming language you essentially write a

### [28:02 - 28:25]

program that takes you from one to the other and you have a proof of of this statement so we take our kind of million human problems and from that we generate a hundred million formal problems and some of those might actually not be possible or they might be incorrectly formulated or um or yeah they might just be false and it doesn't matter because all we do is we learn

### [28:25 - 28:40]

to prove those things and the ones which we can't prove we keep trying and keep trying the ones that we already prove okay they're done they're out the way now if we disprove them that's fine they're out the way and we're left with the really interesting ones which are the ones which are really hard to prove and we keep kind of climbing up from just being able to solve one or two of them

### [28:40 - 29:03]

to then being able to solve 10 or 20 of them and eventually being able to solve a million of them is this the equivalent then that moment of uh you the proof is correct or incorrect is that equivalent to alpha go you win the game or you don't it's exactly equivalent so we use the idea that lean says well done you've proved this as a reward and we give the system you know

### [29:03 - 29:25]

plus one if it if it if it solves it and and minus one if it doesn't get that correct and so this allows us to then train a system by reinforcement learning to get better and better at proving my mathematical statements in fact we literally use the same alpha zero codes that were used to get better at go and chess and all of these other games it's literally the same code

### [29:25 - 29:28]

but it's running if you like with the game of mathematics how dare you

### [29:33 - 29:34]

dare trivialize my subject

### [29:37 - 29:56]

um okay how good is it it's not yet a superhuman mathematician although that is where we'd like to get to one day but one thing which alpha zero doesn't mean that we're going to be able to solve a proof did achieve was the most well-known and challenging of mathematical competitions is called the international mathematics olympiad and this is a competition that happens once a year

### [29:56 - 30:20]

for the most incredible and amazing young mathematicians from all around the world and the problems to say the least are extremely hard they're spicy they're very spicy as a professor of math sometimes i i mean they're they're spicy so you heard it from from hannah these are hard problems very hard and alfred proof amazingly it actually achieved a silver medal level of performance in this competition

### [30:20 - 30:39]

so this is a level of performance that only uh roughly 10 percent of the of the contestants would actually be able to achieve in the entire world in the entire world this is like the cream of young mathematicians like the sixth best from every country and not only that but there was one particular question that less than one percent of all the contestants were able to solve and alpha

### [30:39 - 30:56]

proof got a perfect proof for this particular problem so that was nice to see what do the proofs look like i mean do they follow human style arguments if you're not inputting any human data into them i have to say that to me the proofs i don't understand them at all

### [30:58 - 31:19]

but tim gowers i mean the fields medalist and former imo i mean did he get was he a gold medalist i think multiple gold medalists mega brain right like extraordinary mathematician but i mean he understands these proofs right tim gowers actually was the um refereed our solutions to make sure that they were um valid solutions and that we hadn't you know broken any

### [31:19 - 31:39]

of the rules he understands the solutions and thought that they were you know a huge leap beyond anything that that um previous ai mathematics could do before so it's a jump forward but it's still just the beginning in the sense that you know we really want to go beyond human mathematicians and that's where we'd like to go next because at the moment

### [31:39 - 31:58]

basically you've you've got yourself a very very very talented 17 year old mathematician basically right that's right and it should be said that in the system that entered the imo did take longer than a human contestant would be allowed to take so you know that's something we're just going to assume will get better over time as machines get faster i mean the imo is like the perfect test

### [31:58 - 32:20]

bed because there are correct answers it can be judged you can compare it to human performance all of that kind of thing but if you are feeding in conjectures so things that we don't even know are true um you know i'm thinking of like the abc conjecture here or the riemann hypothesis or any of the like really grand unsolved challenges in mathematics if alpha proof outputs something

### [32:20 - 32:44]

and says no no we've checked this proof it works can you trust it and and maybe even beyond that is it worth anything if we if we don't understand it i think the good news about lean is that mathematicians who are better than myself are always able to take a lean proof and translate it back into something that humans can understand and in fact we've even built an

### [32:44 - 33:01]

ai system that can do this which can take any formal proof and what we call informalize it which means it will turn it back into something which is very understandable to humans and if we did solve the riemann hypothesis and by the way we're a long way from from doing doing that but if it was done there would be millions of mathematicians who'd be very excited to

### [33:01 - 33:19]

to you know understand whatever new mathematics came out of it and decode it back into things that humans can understand okay but here's my question right the clay maths institute in the year 2000 offered a million dollar prize for for seven different mathematical problems human mathematicians have had a quarter of a century in order to try and solve them and

### [33:19 - 33:38]

only one has has fallen do you think potentially the next one could go to ai yes i do actually i think that it might take time i don't think we're there yet i think there's a long way before ai systems are capable of doing this ai is on the right track and systems like alpha proof will become stronger and stronger and stronger you know what we saw in the imo is just the beginning and

### [33:38 - 34:01]

you know that once you have a system that can scale and can keep learning and learning and learning really the sky's the limit so so you know what what will these systems look like in two years or five years or or 20 years i personally would be amazed if ai mathematicians don't transform the whole of mathematics i think it's coming mathematics is one of the few areas where in principle everything can be done

### [34:01 - 34:22]

completely digitally by a machine interacting with itself and just going and going and going so there's really no fundamental barrier to a experience driven ai system mastering mathematics okay i i really buy what you're saying about alpha proof by the way and and the same with alpha zero i mean i think they're really excellent examples of how far you can go with reinforcement

### [34:22 - 34:43]

learning but they are also examples where there is a very clear metric of success you win a game of go or you don't your proof is correct or it isn't how did these ideas translate to systems where it's a lot messier and actually these these very clear metrics might not necessarily be present so first i want to acknowledge that this is this question is probably

### [34:43 - 35:03]

the reason why reinforcement learning methods or these kind of experience-based methods that i'm talking about have not yet broken into the mainstream of absolutely everything that we do in every ai system so it has to be cracked if if the era of experience is to come about then we have to have an answer to this but i think the answer might be right in front of us

### [35:04 - 35:25]

because actually when you look at it the real world contains innumerable signals there's just a vast number of signals in the way the world works you know if we look at all of the things that we do on on on the internet for example there's any number of signals like likes or dislikes or profits or losses or pleasure pain signals you might get or

### [35:25 - 35:47]

yields or you know properties of materials there's all these different numbers representing different things about different aspects of of experience and so what we need is really a way to build a system which can adapt and which can say well which one of these is really the important thing in this situation and so another way to say that is wouldn't it be great if we could have systems

### [35:47 - 36:09]

where you know a human maybe specifies um what they want but that gets translated into a set of different numbers that the system can then optimize for itself completely autonomously so okay an example then let's say i said okay i want to be healthier this year and that's kind of a bit nebulous a bit fuzzy but what you're saying here is that that could be translated into

### [36:09 - 36:28]

a series of metrics like resting heart rate or bmi or whatever it might be and a combination of those metrics could then be used as a reward for reinforcement learning is that if i understood that correctly absolutely correctly are we talking about one metric though are we talking about a combination here the general idea would be that you've got one thing

### [36:28 - 36:52]

which the human wants like to optimize my health and and then the system can learn for itself like which rewards help you to be healthier and so that can be like a combination of numbers that adapts so it could be that it starts off saying okay well you know right now it's your resting heart rate that really matters and then later you know it gets some feedback saying hang on you know i

### [36:52 - 37:13]

really don't just care about that i care about my anxiety level or something and then it includes that into the mixture and and based on on on feedback it could actually adapt so one way to say this is that a very small amount of human data can allow the system to generate goals for itself that enable a vast amount of learning from experience because this is

### [37:13 - 37:37]

where the the real questions of alignment come in right i mean if you said for instance let's do a reinforcement learning algorithm that's just minimizes my resting heart rate i mean quite quickly zero is is like a good minimization strategy there which would achieve its objective just not maybe quite in the way that you wanted it to i mean obviously you really want to avoid

### [37:37 - 38:00]

that kind of scenario so how do you have confidence that the metrics that you're choosing aren't creating additional problems one way you can do this is to leverage the the same answer which has been so effective so far elsewhere in ai which is at that level you can make use of of some human input if it's a human goal that we're optimizing then we probably at that level need to measure

### [38:00 - 38:18]

you know and say well you know a human gives feedback to say actually you know i'm starting to feel uncomfortable and in fact while i don't want to claim that we have the answers and i think there's an enormous amount of research to get this right and make sure that this kind of thing is safe could actually help in certain ways in terms of this kind of safety and adaptation there's this

### [38:18 - 38:39]

famous example of paving over the whole world with paper clips when a system's been asked to make as many paper clips as possible if you have a system which which is really its overall goal is to you know support human um well-being or and and it gets that feedback from humans about and it understands their their distress signals and their happiness signals and so forth the moment it

### [38:39 - 38:58]

starts to you know do create too many paper clips and starts to cause people distress it would adapt that that combination and it would choose a different combination and start to optimize for something which isn't going to pave over the world with paper clips we're not there yet yeah but i think there are some some versions of this which could actually end up not only

### [38:58 - 39:19]

addressing some of the alignment issues that have been faced by previous approaches to you know goal focused systems that maybe even you know be be more adaptive and therefore safer than what we have today outside of the world of ai though i mean is there a problem with using quantitative metrics as a measure for success at all i mean

### [39:19 - 39:43]

i'm thinking here about exam scores or or gdp or the the the myriad of of problems that you can get into when you focus too carefully and end up with a tyranny of metrics i would be the first to agree that that when you like mindlessly pursue a metric in in the human world that it often leads to undesired consequences at the same time the whole world of of

### [39:43 - 40:02]

human endeavor is organized around us optimizing for some things if we didn't have anything that we could optimize for we wouldn't ever be able to make progress we have all kinds of signals and metrics and and so forth that drive progress and then people say oh maybe that isn't the you know the right metric and they adapt it is is part of the problem then

### [40:02 - 40:22]

that at the moment you have an interaction with an ai that is really contained within time there aren't these sort of longer-term learnings or adjustment of of what the goals might like once you decide that gdp is the thing that you're going for is gdp forever and there's no change i think that's absolutely right that the kind of ai that we have today doesn't have like

### [40:22 - 40:40]

a life you know it's not something which has its own stream of experience in the way that you know an animal or a human might have that kind of goes on for for years and years and years and can keep adapting over time and and that needs to change and one of the reasons it needs to change is so that we can have systems that that just keep learning and learning and learning over time

### [40:40 - 40:55]

and adapting and understanding how to better achieve um the kind of outcome that we really want is there something that is quite risky about untethering algorithms with with i mean potentially quite a lot of power from human

### [40:56 - 41:18]

data really there are certainly risks and there are certainly benefits and i think we absolutely have to take this very seriously and be extraordinarily careful about taking these steps um that come next on the in this journey towards the era of experience and i should say that you know one of my reasons to write this position paper is because i feel

### [41:18 - 41:39]

that that people aren't recognizing that this transition is going to come and that it will have consequences and and it will require careful thought about many of these decisions and the fact that so many people are still thinking only about their human data approach means that not enough people are taking seriously these kinds of questions the last time i got to speak to you

### [41:39 - 42:13]

on this podcast we talked about a different position paper that you've been working on for a while now and just wanted to bring it up a little bit so we were thinking to discus about what is our combat strategy what are human data data goals i think something similar to what we were discussing earlier about how we're not particularly attracts the chat by the organization

### [42:13 - 42:34]

you know a certain level of performance that they have for free but then we need in the analogy some kind of sustainable fuel that kind of keeps the world going once all the fossil fuels are gone and I think that's what reinforcement learning is it's the sustainable fuel this experience that it can keep like generating and using and learning from and generating more and learning from it

### [42:34 - 42:54]

that's really the process that's going to drive progress in AI and I don't want to in any way denigrate what's been done with with human data I think it's great AIs that we've got now are amazing mind-blowing things I love them and and enjoy working with them and and do research on them myself but it's just the beginning. Dave thank you so much that was amazing. Thank you

### [42:54 - 43:12]

thank you it's always really really fun. Of course there is this monumental amount of progress that's going on at the moment but when you stop to think about it there really has been this narrowing in the diversity of ideas around AI I mean the success of multimodal models has been so rapid it's been so profound so beyond what most people think about it and I think it's really important

### [43:12 - 43:28]

to have this preface I think it has been a very valuable shift in the course of our research and I've had the pleasure of working with the SBA and the Department of Health to talk to us about this but I think it's really important to point out that there are risks involved with this process in terms of being able to use human data like AI in the future as well. So there have been

### [43:28 - 43:51]

there's been plenty of things that have happened to make AI the way that most people were expecting but they kind of have sucked a lot of the oxygen out of the broader conversation and it is noticeable can't help but be quite convinced by what David was saying there. If we really want superhuman intelligence, maybe it is now time to step away from the human.

### [43:52 - 44:16]

You have been listening to Google DeepMind, the podcast with me, Professor Hannah Fry. And before you go, we have got an extra special treat for you today in the form of a conversation between David Silver, the man behind AlphaGo, and Fan Hui, the first professional Go player to face it. A decade ago, a little while before the very famous 4-1 victory over Lisa Dole, Fan Hui became

### [44:16 - 44:39]

the first professional Go player to test his skills against your algorithm. Thank you so much for joining us, Fan Hui. Oh, thank you. Thank you. For me, it's a very extraordinary experience. How long has it been since you spoke to him? It's been quite a few years. It's so nice to see Fan Hui. It's been absolutely amazing to catch up with someone who Fan Hui played such a huge part in the journey.

### [44:39 - 44:58]

I have always liked the development of AlphaGo, so it's really just a genuine delight. Okay, so I want to ask you about that match that you had all those years ago, because I think, I guess now, looking at the full history of it, it almost seems like a like a foregone conclusion. But at the time, I mean, you must have been pretty nervous, David. And how did you feel about it as well, Fan Hui?

### [44:58 - 45:28]

I remember the first time I saw the DM's email telling me, like, the exciting Go project. I still remember when I played with AlphaGo, the first game I lost. I feel something strange. I also remember when I lost the second game. I feel fear because I feel maybe I will never win with this program or AI. And when I lost my last, my five-game last game, I feel my goal world is broken.

### [45:28 - 46:06]

But maybe this is also a good moment. My new goal world is open. So I started thinking about it. I think AlphaGo for me is not just teaching me something new technically, not just a technique. Maybe it's telling me the words to open my mind and change my mind. After that, for me, even today, for me, I never ask a question like, I can't or I can. My question is always like, I want or I don't want.

### [46:06 - 46:31]

So I think this is AI or AlphaGo teaching me about that. David, I want to ask you as well, though, in advance of that match, I mean, how confident were you about the performance of your algorithm? We really weren't confident. It was just, it's so hard to judge where we were, because we knew that we'd gone beyond the players that we had at DeepMind.

### [46:31 - 46:51]

And we knew that we'd gone beyond all the programs that had been written before. But there's such a huge gap. There's such a huge gap beyond that towards the level of professional players like FanHui. And we had no idea, you know, are we somewhere in that gap? Are we somewhere beyond that gap? We just genuinely didn't know. And so this was the first time we had any opportunity to calibrate our level of performance.

### [46:51 - 47:16]

And I don't think any of us would have been surprised if we'd lost all five games. And so it was a very pleasant surprise to win all five. And yeah. We just... I mean, genuinely, it was like one of those moments where the world could have branched either way. And we just didn't know until the match happened. But of course, FanHui, this algorithm then advanced, I mean, with your help.

### [47:16 - 47:38]

In fact, after your match, you came on board and supported the team in developing it further. But that earlier version, what did it feel like to play it? Did it feel fundamentally different to having a human opponent? You know, I played with another program before AlphaGo. So when I play with another program, I feel like, oh, this is a program. Because they don't play like a human.

### [47:38 - 48:05]

But with AlphaGo, I feel something very strange. It's like sometimes I feel like it's really, really like human. What's the impact been then of AlphaGo and AlphaZero on the Go community? Has it been... Has there had to be a process of acceptance or was it, you know, positive from the off? First of all, when I lost with AlphaGo, for the all-Go community, nobody really believed this is true. Because, yeah.

### [48:05 - 48:30]

I'm only a champion. I'm only a champion. I'm only a champion. I'm only a champion. I'm only a champion. So it's not more than champion. But when AlphaGo, when they started, and the all-Go community sees something different. Because AlphaGo played really, really well. I remember in the second game, the move 37, such beautiful move, really, really beautiful. So creative, very creative.

### [48:30 - 49:00]

For the human, we will never play this move. After that move, everything changed in the Go world. Because for us, everything is possible. Today, even the student, even the Go student use AI to learn. So yes, I think this is really, really good for all-Go community. I think it's not just for Go community. It's also for the world, I think. For everything. Absolutely. Fan Hui, thank you so much for joining us.

### [49:00 - 49:19]

That was such a real treat, especially with the big anniversary coming up, I guess. Just great to see you again. And yeah, thanks for coming in. And thanks for everything you did on AlphaGo. I don't think it would have been the same without you. I think we would have made some terrible mistakes if we hadn't had your advice to help us along the way. So thank you. Thank you, Dave.
