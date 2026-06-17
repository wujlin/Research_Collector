# Richard Sutton – Father of RL thinks LLMs are a dead end

- URL: https://www.youtube.com/watch?v=21EYKqUsPfg
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Refined at: `2026-05-11T23:54:26`

## Transcript

### [00:00 - 00:19]

Why are you trying to distinguish humans? Humans are animals. What we have in common is more interesting. What distinguishes us, we should be paying less attention to. I mean, we're trying to replicate intelligence, right? No animal can go to the moon or make semiconductors, so we want to understand what makes humans special. So I like the way you consider that obvious, because I consider the opposite obvious.

### [00:19 - 00:40]

If we understood a squirrel, we'd be almost all the way there. I am personally just kind of content being out of sync with my field for a long period of time, perhaps decades, because occasionally I have improved, right, in the past. I don't think learning is really about training. It's about an active process. The child tries things and sees what happens.

### [00:40 - 01:02]

I think we should be proud that we are giving rise to this great transition in the universe. Today, I'm chatting with Richard Sutton, who is one of the founding fathers of reinforcement learning and inventor of many of the main techniques used there, like TD learning and policy gradient methods. And for that, he received this year's Turing Award, which, if you don't know,

### [01:02 - 01:25]

is basically the Nobel Prize for Computer Science. Richard, congratulations. Thank you, Dvarkis. And thanks for coming on the podcast. It's my pleasure. Okay, so first question. My audience and I are familiar with the LLM way of thinking about AI. Conceptually, what are we missing in terms of thinking about AI from the RL perspective? Well, yes, I think it's really quite a different point of view.

### [01:25 - 01:55]

And it can easily get separated. We didn't lose the ability to talk to each other. And, yeah, large language models have become such a big thing. Generative AI, in general, a big thing. And our field is subject to bandwagons and fashions. So we lose track of the basic, basic things. Because I consider reinforcement learning to be basic AI. And what is intelligence? The problem is to understand your world. Right.

### [01:56 - 02:19]

And reinforcement learning. It's about understanding your world. Whereas large language models are about mimicking people. Doing what people say you should do. They're not about figuring out what to do. Huh. I guess you would think that to emulate the trillions of tokens in the corpus of Internet text, you would have to build a world model. In fact, these models do seem to have very robust world models.

### [02:19 - 02:29]

And they're the best world models we've made to date in AI, right? So what do you think that's missing? I would disagree with most of the things. You just said. Great.

### [02:31 - 02:54]

Just to mimic what people say is not really to build a model the world at all? I don't think. You know, you are mimicking things that have a model of the world. The people. But I don't want to approach the question in an adversarial way. But I would question the idea that they have a world model. So world model would enable you to predict what would happen. Right.

### [02:54 - 03:10]

They have the ability to predict what a person would say. They don't have the ability is predict what a piece of work would look like it. Yeah. predict what will happen. What we want, I think, to quote Alan Turing, what we want is a machine that can learn from experience. Where experience is the things that actually happen in your life.

### [03:10 - 03:33]

You do things, you see what happens, and that's what you learn from. The large language models learn from something else. They learn from here's a situation and here's what a person did. And implicitly, the suggestion is you should do what the person did. Right. I guess maybe the crux, and I'm curious if you disagree with this, is some people will say, okay, so this imitation

### [03:33 - 03:53]

learning has given us a good prior or given these models a good prior, but reasonable ways to approach problems. And as we move towards the era of experience, as you call it, this prior is going to be the basis on which we teach these models from experience because this gives them the opportunity to get answers right some of the time.

### [03:53 - 04:18]

And then on this, you can build, you can train them on experience. Do you agree with that perspective? No, I agree that it's the large language model perspective. Right. I don't think it's a good perspective. Yeah. Here's why. So to be a prior for something, there has to be a real thing. I mean, a prior bit of knowledge should be the basis for actual knowledge. What

### [04:18 - 04:39]

is actual knowledge? There's no definition of actual knowledge in that language. Language framework. What makes an action a good action to take? You recognize the value, the need for continual learning. Right. So if you need to learn continually, continually means learning during normal interaction with the world. Yeah. And so

### [04:39 - 04:58]

then there must be some way during the normal interaction to tell what's right. Yep. Okay. So is there any way for it to tell in the largest language model setup to tell what's the right thing to do? Yeah. So I think it's a good question. I think it's a good question. I think it's a good thing to say. You will say something and you will not get feedback about what the right thing to say

### [04:58 - 05:19]

is because there's no definition of what the right thing to say is. There's no goal. Right. And if there's no goal, then there's, there's one thing to say, another thing to say, there's no right thing to say. Right. So there's no ground truth. You can't have prior knowledge if you don't have ground truth because the prior knowledge is supposed to be a hint or an initial belief

### [05:19 - 05:35]

about what the truth is. Yeah. But there isn't any truth. There's no right thing to say. Right. Now in reinforcement learning, there is a right thing to say or right thing to do. Right. Because the right thing to do is the thing that gets you reward. Right. So we have a definition of what the right thing to do is. And so we can have

### [05:35 - 05:58]

prior knowledge or knowledge provided by people about what the right thing to do is. And then we can check it to see because we have a definition of what the actual right thing to do is. Yeah. Now, an even simpler case is when you have, you're trying to make a model of the world, when you predict what will happen, you predict and then you see what happens. Okay. So there's ground truth. There's no ground truth

### [05:58 - 06:22]

in large language models because you don't have a prediction about what will happen next. If you say something in your conversation, the large language models have no prediction about what the person will say in response to that or what the response will be. I mean, I think they do. You can literally ask them, what would you anticipate a user might say in response?

### [06:22 - 06:44]

And they have a prediction. Oh, no, they will respond to that question, right? Yeah. But they have no prediction in the substantive sense that they won't be surprised by what happens. And if something happens that isn't what you might say they predicted, they will not change because an unexpected thing has happened. And to learn that, they'd have to make an adjustment.

### [06:44 - 07:32]

So I think a capability like this does exist in context. So it's interesting to watch a model do change. I'm just saying they don't have in any meaningful sense, they don't have a prediction of what will happen next. And they will not be surprised by what happened next. They'll not make any changes if something happens based on what happens. But isn't that literally what next token prediction

### [07:32 - 07:52]

is? Prediction of what was next and then updating on the surprise? Next token is what they should say, what the action should be. It's not what the world will give them in response to what they do. Let's go back to their lack of goal. For me, having a goal is the essence of intelligence. Right. Something is intelligent if it's not intelligent.

### [07:52 - 08:21]

I like John McCarthy's definition that intelligence is the computational part of the ability to achieve goals. So you have to have goals. You're just a behaving system. You're not anything special. You're not intelligent. And you agree that large language models don't have goals. I think they have a goal. What's the goal? Next token prediction. That's not a goal. It doesn't change the world. Right.

### [08:21 - 08:47]

You know, tokens come at you, and if you predict them, you don't influence them. Oh, yeah. It's not a goal about the external world. Yeah, it's not a goal. It's not a substantive goal. You can't look at a system and say, oh, it has a goal if it's just sitting there predicting and being happy with itself, that it's predicting accurately. I guess maybe the bigger question I want to understand is why you don't think

### [08:47 - 09:11]

doing RL on top of LLMs is a productive direction. Because we seem to be able to give these models a goal of solving difficult math problems, and they're in many ways at the very peaks of human level in the capacity to solve math Olympia-type problems, right? They got gold at IMO. So it seems like the model which got gold at the International Math Olympia does have the goal of getting math problems, right?

### [09:12 - 09:43]

So why can't we extend this to different domains? Well, the math problems are different. I'm making a model of the physical world, and carrying out the consequences of mathematical assumptions or operations. Those are very different things. The empirical world has to be learned. You have to learn the consequences, whereas the math is more just computational. It's more like standard planning.

### [09:44 - 09:49]

So there, they can have a goal to

### [09:51 - 10:20]

to find the proof, and they are in some way given that goal to find the proof. Right. So, I mean, it's interesting because you wrote this essay in 2019 titled The Bitter Lesson, and this is the most influential essay perhaps in the history of AI. But people have used that as a justification for scaling up LLMs, because in their view, this is the one scalable way we have found to pour

### [10:20 - 10:49]

ungodly amounts of compute into learning about the world. And so it's interesting that your perspective is that the LLMs are actually not bitter lesson-pilled. It's an interesting question whether large language models are a case of the bitter lesson. Yeah. Because they are clearly a way of using massive computation, things that will scale with computation up to the limits of the internet. Yeah.

### [10:50 - 11:23]

But they're also a way of putting in lots of human knowledge. And so this is an interesting question. It's a sociological or industry question. Will they reach the limits of the data and be superseded by things that can get more data just from experience rather than from people?

### [11:25 - 11:49]

In some ways, it's a classic case of the bitter lesson. With the more human knowledge we put into the large language models, the better they can do. And so it feels good. And yet, I in particular expect there to be systems that can learn from experience, which could well perform much, much better and be much more scalable.

### [11:50 - 12:12]

But some people are saying they think of themselves as just because they build a computer will be a happens, but it's actually the user in the other case, it will be another instance of the bitter lesson that the things that that used human knowledge were eventually superseded by things that just train from experience and computation.

### [12:12 - 12:38]

I guess that doesn't seem like the crux to me, because I think those people would also agree that the overwhelming amount of computing the future or the basis of that, the thing you'll start with in order to pour in the compute to do this future experiential learning or on-the-job learning will be LLMs. And so I guess I still don't understand why this is the wrong starting point altogether, why we need a whole new

### [12:38 - 13:06]

architecture to begin doing experiential continual learning, and why we can't start with LLMs to do that. Well, in every case of the bitter lesson, you could start with human knowledge and then do the scalable things. That's always the case. And there's never any reason why that has to be bad. But in fact, and in practice, it has always turned out to be bad because people get locked

### [13:06 - 13:33]

into the human knowledge approach and they psychologically... Now I'm speculating why it is, but this is what has always happened. Yeah. That, yeah, their lunch gets eaten by the methods that are truly scalable. Give me a sense of what the scalable method is. The scalable method is you learn from experience. You try things, you see what works.

### [13:33 - 13:58]

No one has to tell you. First of all, you have a goal. So without a goal, there's no sense of right or wrong or better or worse. So large language models are trying to get by without having... A goal or a sense of better or worse. That's just, you know, it's exactly starting in the wrong place. Maybe it's interesting to compare this to humans. So in both the case of learning from

### [13:58 - 14:12]

imitation versus experience and on the question of goals, I think there's some interesting analogies. So, you know, kids will initially learn from imitation. You don't think so? No, of course not.

### [14:14 - 14:31]

Really? Yeah. I think kids just like watch people. They like kind of try to like say the same words. How old are these kids? I think the level... What about the first six months? I think they're kind of imitating things. They're trying to like make their mouth sound the way they see their mother's mouth sound. And then they'll say the same words without understanding

### [14:31 - 14:55]

what they mean. And as you get older, the complexity of the imitation they do increases. So you're imitating maybe the skills that your people in your band are using to hunt down the deer or something. And then you go into the learning from experience RR regime. But I think there's a lot of imitation learning happening with humans. It's surprising. Yeah, you can have such a different point of view. Yeah.

### [14:55 - 15:23]

When I see kids, I see kids just trying things and like waving their hands around and moving their eyes around. And no one, no, no, no one tells them there's no, there's no imitation for how they move their eyes around or even the sounds they make. They may, they may want to create the same sounds. Right. Right. But the actions, you know, the thing that the infant actually does, there's no targets for that.

### [15:23 - 15:41]

There are no examples for that. I agree that doesn't explain everything infants do, but I think it guides the learning process. I mean, even LLM, when it's trying to predict the next token early in training, it will like make a guess. It'll be different from what like it actually sees. And in some sense, it's like very short horizon RL, where it's like making this guess of like, I think this token will be this.

### [15:42 - 16:06]

It's actually the other thing, similar to how a kid will try to say a word. It comes out wrong. The large language model is learning from training data. It's not learning from experience. It's learning from something that will never be available during its normal life. There's never any training data that says you should do this action in normal life. I think this is maybe more of a semantic distinction.

### [16:06 - 16:29]

Like, what do you call school? Is that not training data? You're not like going to school because it's like... School is much later. Okay, I shouldn't have said never. But I don't know. I think I would even say it about school. But formal schooling is the exception. You shouldn't base your theories on that. I think there's a sort of programming in your biology that like early on, you're not that useful.

### [16:29 - 16:51]

And then like kind of why you exist is to understand the world and like learn how to interact with it. And it seems kind of like a training phase. I agree that then there's like a sort of more gradual. There's not a sharp cutoff to like training to deployment. But yeah. There seems to be this like initial training phase, right? There's nothing where you have training of what you should do. There's nothing.

### [16:52 - 16:56]

You see things that happen. You're not told what to do.

### [16:58 - 17:26]

Don't be difficult. I mean, this is obvious. I mean, you're like literally taught what to do. This is like where the word training comes from is from humans, right? So I don't think learning is really about training. I think learning is about learning. It's about an active process. The child tries things and sees what happens. Yeah. It does not. We don't think about training when we think of an infant growing up.

### [17:27 - 17:52]

These things are actually rather well understood. If you go to look about how psychologists think about learning, there's nothing like imitation. Maybe there are some extreme cases where humans might do that or appear to do that. But. There is no basic animal learning process called imitation. The basic animal learning process is for prediction and for trial and error control.

### [17:53 - 18:22]

I mean, it's really interesting how sometimes the most hard things to see are the obvious ones. It's obvious if you just look at animals and how they learn and you look at psychology and how our theories of them. It's obvious that that supervised learning is not part of the way animals learn. We don't have examples of desired behavior. What we have is examples of things that happen, one thing that followed another.

### [18:22 - 18:46]

And we have examples of we did something and there were consequences. But there are no examples of supervised learning. And supervised learning is not something that happens in nature. And you know, school, even if that was the case, you know, we should forget about it. Because it's. It's just that's some special thing that happens in people. It doesn't happen broadly in nature.

### [18:47 - 19:14]

And, you know, squirrels don't go to school. Squirrels can learn all about the world. It's absolutely obvious, I would say, that supervised learning doesn't happen in animals. So I interviewed this psychologist and anthropologist, Joseph Henrich, who has done work about cultural evolution and basically how did what you know what distinguishes humans. And how do humans pick up knowledge?

### [19:14 - 19:16]

Why are you trying to distinguish humans?

### [19:18 - 19:34]

Humans are animals. What we have in common is more interesting. What we have, what distinguished us, we should we should be paying less attention to. I mean, we're trying to replicate intelligence, right? So if you want to understand what is it that enables humans to go to the moon or to build semiconductors?

### [19:34 - 19:53]

I think the thing we want to understand is the thing that makes no animal can go to the moon or make semiconductors. So we want to understand. What? What makes humans special? So I like the way you consider that obvious because I consider the opposite obvious. Yeah, I think we need to we we have to we have to understand how we are animals.

### [19:53 - 20:05]

And if we understood a squirrel, I think we'd have a we'd be almost all the way there to understanding human intelligence. The language part is just a small veneer on the surface.

### [20:06 - 20:33]

OK, so this is great. You know, we're finding out the very different ways that we're thinking. Maybe. We're not arguing. We're trying to share our different ways of thinking with each other. Yeah, I think argument is useful. So, yeah, but I do want to complete this thought. So Joseph Henrich has this interesting theory that if you look at a lot of the skills that humans have had to master in order to be successful.

### [20:33 - 20:50]

And we're not talking about, you know, last thousand years or last ten thousand years, but hundreds of thousands of years. You know, the world is really complicated. And it's not possible to reason through how to, let's say, hunt a seal if you're living in the Arctic.

### [20:50 - 21:20]

And so there's this many, many step long process of how to make the bait and how to find the seal and then how to process the food in a way that makes sure you won't get poisoned. And it's not possible to reason through all of that. And so over time, yes, there's this like larger process of whatever. You want to use maybe something else where culture as a whole has figured out how to find and kill and eat seals.

### [21:20 - 21:42]

But then what is happening when through generations, this knowledge is transmitted is in his view that like you just have to imitate your elders in order to learn that skill, because you can't you can't think your way through how to hunt and kill and process a seal. You have to just watch other people maybe make tweaks and adjustments. And that's how cultural knowledge accumulates.

### [21:42 - 22:03]

But the initial step of the cultural gain has to be imitation. But maybe you think about it a different way. No, I think about it the same way. OK. But still. It's a small thing on top of basic trial and error learning prediction learning. And that's what distinguishes us. Perhaps from from many animals.

### [22:05 - 22:06]

But we're an animal first.

### [22:08 - 22:22]

Yeah. And we were an animal before we had land. And we're an animal after we had land. And we're an animal after we had land. And we're an animal after we had land. And we're an animal after we had land. And we're an animal after we had land. I do think you make a very interesting point that continual learning is a capability that most mammals have. I guess all mammals have.

### [22:22 - 22:47]

So it's quite interesting that we have something that all mammals have, but our systems don't have. Right. Whereas maybe like the ability to understand math and problems, difficult math problems depends on how you define math. But like this is a capability our eyes have. But that no almost no animal has. And so it's quite interesting what ends up being difficult and what ends up being easy. Morphics. Parallelics.

### [22:47 - 23:08]

That's right. For the era of experience to commence, we're going to need to train AIs in complex real world environments. But building effective RL environments is hard. You can't just hire a software engineer and have them write a bunch of cookie cutter validation tests. Real world domains are messy. You need deep subject matter experts to get the data, the workflows and all the subtle rules right.

### [23:08 - 23:29]

When one of Labelbox's customers. Wanted to train an agent to shop online. Labelbox assembled the team with a ton of experience engineering Internet storefronts. For example, the team built a product catalog that could be updated during the episode because most shopping sites have constantly changing state. They also added a Redis cache to simulate stale data, since that's how real e-commerce sites actually work.

### [23:30 - 23:41]

These are the kinds of things that you might not have naively thought to do, but that Labelbox can anticipate. These details really matter. Small tweaks are often the difference between cool demos and agents that can. Actually operate in the real world.

### [23:41 - 24:10]

So whether it's correcting traces that you already produced or building an entirely new suite of environments, Labelbox can help you turn your RL projects into working systems. Reach out at labelbox.com slash dvarkash. All right. Back to Richard. This alternative paradigm that you're imagining. The experiential paradigm. Yes. Let's lay out a little bit about what it is. It says that experience action sensation. Well.

### [24:10 - 24:39]

Sensation, action, reward, and then this happens on and on and on, makes more life. It says that this is the foundation and the focus of intelligence. Intelligence is about taking that stream and altering the actions to increase the rewards in the stream. Right. So learning then is from the stream and learning is about the stream. So that second part is particularly telling.

### [24:40 - 25:06]

What you learn, your knowledge, your knowledge is about the stream. Your knowledge is about if you do some action, what will happen? Or it's about which events will follow other events. It's about the stream. It's the content of the knowledge is statements about the stream. And so because it's a statement about the stream, you can test it by comparing it to the stream and you can learn it continually.

### [25:06 - 25:27]

So when you're imagining this future continuation. A learning agent, they're not future. Of course, we, they exist all, all the time. It's, I mean, this is what reinforcement learning paradigm is learning from experience. Yeah. I guess the, maybe I would have meant to say is a human level, general, continual learning agent. What is their reward function? Is it just predicting the world?

### [25:27 - 25:49]

Is it, uh, is it then having a specific effect on it? How, what would the general reward function be? The reward, uh, function is arbitrary. And, um, so. So if you're playing chess, it's to win the game of chess. If you were to, um, uh, if you're a squirrel, maybe the, the reward has to do with getting nuts, right?

### [25:50 - 26:15]

Um, in general, for an animal, you would say the reward is to avoid pain and to acquire pleasure, right? Uh, and there's also, would be a component having to do with, uh, I think there would be, should be a component having to do with your, uh, increasing understanding of your, of your environment that would be sort of an intrinsic motivation. I see.

### [26:16 - 26:39]

I guess this AI would be deployed to like, lots of people would want it to be doing lots of different kinds of things, right? So it's performing the task people want, but at the same time, it's learning about the world from doing that task. And do you, do you imagine, okay, so we get rid of this paradigm where there's training periods and then there's deployment. Period.

### [26:39 - 27:02]

But then is there, do we also get rid of this paradigm when there's the model and then instances of the model or copies of the model that are, you know, doing certain things? How do you think about the fact that there, we'd want this thing to be doing different things. We'd want to aggregate the knowledge that it's gaining from doing those different things. I don't like the word model when used the way you just did.

### [27:02 - 27:29]

I think a better word would be the network. So I think you mean the network. Maybe there's many networks. So anyway, things would be learned and then you'd have copies and many instances. And sure, you'd want to share knowledge across the instances. And there would be lots of possibilities for doing that. Like there is not today. You can't have one child grow up and learn about the world.

### [27:29 - 27:48]

And then every new child has to repeat that process. Whereas with AIs, with the digital intelligence, you could hope to do it once and then copy it into the network. And then the next one is the starting place. So this would be a huge savings. And I think actually it'd be much more important than trying to learn from people.

### [27:49 - 28:12]

I agree that the kind of thing you're talking about is necessary regardless of whether you start from LLMs or not, right? If you want human or animal level intelligence, you're going to need this capability. Suppose a human is trying to make a startup, right? And this is a thing which has a reward on the order of 10 years. Once in 10 years, you might have an exit where you get paid out a billion dollars.

### [28:13 - 28:33]

But humans have this ability to make intermediate auxiliary rewards or have some way of, even when they have extremely special rewards, they can still make intermediate steps, having an understanding of what the next thing you're doing leads to this grander goal we have. And so how do you imagine such a process might play out with AIs? So this is something we know very well.

### [28:34 - 28:59]

And the basis of it is temporal difference learning. Where the same thing happens. In a less grandiose scale, like when you learn to play chess, the long-term goal is winning the game. And yet you want to be able to learn from shorter-term things like taking your opponent's pieces. And so you do that by having a value function which predicts the long-term outcome.

### [29:00 - 29:21]

And then if you take the guy's pieces, well, your prediction about the long-term outcome is changed. It goes up. You think you're going to win. And then that increase in your... In your belief immediately, quote, reinforces the move that led to taking the piece. Okay. So we have this long-term 10-year goal of making a startup and making a lot of money.

### [29:22 - 29:45]

And so when we make progress, we say, oh, I'm more likely to achieve the long-term goal. And that rewards the steps along the way. Right. And then you also want some ability for information that you're learning. I mean, one of the things that makes humans quite different from these LLMs is that if you're onboarding on a job,

### [29:45 - 30:09]

you're picking up so much context and information, and that's what makes you useful at the job, right? You're everything from how your client's preferences to how the company works to everything. And is the bandwidth of information that you get from a procedure like TD learning high enough to have this, like, huge pipe of, like, context and tacit knowledge that you need to be picking up in the way humans do?

### [30:09 - 30:10]

When they're just, like, deployed?

### [30:12 - 30:34]

I think the crux of this, and I'm not sure, but the big world hypothesis seems very relevant. And the reason why humans become useful on their job is because they are encountering the particular part of the world. That's right. And it can't have been anticipated and can't all have been put in in advance.

### [30:36 - 30:58]

The world is so huge that you can't. The dream, as I see it, the dream of large language models is you can teach the agent everything, and it will know everything, and it won't have to learn anything online during its life, okay? And your examples are all, well, really, you have to because you can teach it,

### [30:59 - 31:16]

but there's all the little idiosyncrasies of the particular life they're leading and the particular people they're working with and what they like as opposed to what average people like. Right. And so that's just saying the world is really big, and so you're going to have to learn it along the way. Yeah. So it seems to me you need two things.

### [31:16 - 31:42]

One is some way of converting this long-run goal reward into smaller auxiliary or, you know, these, like, predictive rewards of the future reward or the future reward to at least the final reward. Then you need some other way. Initially, it seems to me you need some way of then, okay, I need to hold on to all this content. I need to hold on to all this context that I'm gaining as I'm working in the world, right?

### [31:42 - 32:06]

I'm, like, learning about my clients, my company, all this information, and I'm... So I would say you're just doing regular learning. Yeah. Maybe using context because in large language models, all that information has to go into the context window. Right. But in a continual learning setup, it just goes into the weights. Maybe, yeah, so maybe context is the wrong word to use because I mean a more general thing.

### [32:06 - 32:26]

You learn a policy. It's specific to the environment that you're finding yourself in. Yeah. So the question I'm trying to ask is you need some way of getting, like, how many bits per second are you picking up? Like, is a human picking up when they're, you know, out in the world, right? If you're just, like, interacting over Slack with your clients and everything.

### [32:27 - 32:51]

So maybe we're trying to ask the question of it seems like the reward is too small of a thing to do all the learning that we need to do. But, of course, we have the sensations. We have all the other information we can learn from. Right. We don't just learn from the reward. We learn from all the data. Yeah. So what is the learning process which helps you capture that information?

### [32:52 - 33:19]

So now I want to talk about the base common model of the agent with the four parts. Right. So we need a policy. The policy says in the situation I'm in, what should I do? We need a value function. The value function is the thing that is learned. And the value function produces a number. The number says how well is it going? And then you watch if that's going up and down and use that to adjust your policy. Okay.

### [33:19 - 33:37]

So those two things. And then there's also the perception component, which is the construction of your state representation, your sense of where you are now. And the fourth one is what we're really getting at, most transparently anyway. The fourth one is the transition model of the world.

### [33:38 - 34:01]

That's why I am uncomfortable just calling everything models because I want to talk about the model of the world, the transition model of the world, your belief that if you do this, what will happen? What will be the consequences of what you do? So your physics of the world. But it's not just physics. It's also abstract models like your model of how you traveled from California up to Edmonton for this podcast.

### [34:01 - 34:17]

That was a model and that's a transition model. And that would be learned. And it's not learned from reward. It's learned from you did. Things you saw what happened when you made that model of the world. That is it will be learned very richly from all the sensation that you receive, not just from the reward.

### [34:18 - 34:44]

It has to include the reward as well, but that's a small part of the whole model, small, crucial part of the whole model. Yeah. One of my friends, Toby Ward, pointed out that if you look at the Museuro models that Google DeepMind deployed to learn Atari games, that these models were initially. Not a general intelligence itself, but a general framework for training specialized intelligences to play specific games.

### [34:44 - 35:07]

That is to say that you couldn't, using that framework, training policy to play both chess and go and some other game. You had to train each one in a specialized way, and he was wondering whether that implies that reinforcement learning generally, because of this information constraint, you can only learn one thing at a time. The density of the learning. Yeah.

### [35:07 - 35:31]

The density of information isn't that high, or whether it was just specific to the way that Museuro was done. And if it's specific to AlphaZero, what needed to be changed about that approach so that it could be a general learning agent? The idea is totally general. You know, I do use all the time, as my canonical example, the idea of an AI agent is like a person. Yeah.

### [35:31 - 35:51]

And people, in some sense, they have just one world they live in. And that world may involve chess, and it may involve Atari games, but those are not a different task or a different world. Those are different states that they encounter. And so, the general idea is not limited at all.

### [35:51 - 36:22]

So, maybe it would be useful to explain what was missing in that architecture, or that approach, which this continual learning AGI would have. They just set it up. They didn't. It was not their ambition to have one agent across those games. If we want to talk about transfer, we should talk about transfer, not across games or across tasks, but transfer between states. Yeah.

### [36:22 - 36:48]

I guess I'm curious about, historically, have we seen the level of transfer using RL techniques that would be needed to build this kind of… Okay, good. Good. We're not seeing transfer anywhere. We're not seeing general… Critical to good performance is that you can generalize well from one state to another state. We don't have any methods that are good at that.

### [36:48 - 37:18]

What we have are people try different things, and they settle on something that… A representation that transfers well, or that generalizes well. But we don't have any automated techniques to promote. We have very few automated techniques. We have very few methods to promote transfer, and none of them are used in modern deep learning. Let me paraphrase to make sure that I understood that correctly.

### [37:18 - 37:44]

It sounds like you're saying that when we do have generalization in these models, that is a result of some sculpted… Humans did it. Yeah. The researchers did it, because there's no other explanation. I mean, gradient descent will not make you generalize well. It will make you solve the problem. Right. It will not make you, you know, if you get new data, you generalize in a good way.

### [37:44 - 38:05]

Generalization means train on one thing, that'll affects what you do on the other things. So we know deep learning is really bad at this. For example, we know that if you train on some new thing, it will often catastrophically interfere with all the old things that you knew. So this is exactly bad generalization. Right. Now, generalization, as I said, is some kind of influence.

### [38:05 - 38:26]

It's the influence of training on one state on other states. And generalization is not necessarily good or bad, right? Just the fact that you generalize is not necessarily good or bad. You can generalize poorly. You can generalize well. Right. So you need… Generalization always will happen. But we need algorithms that will cause the generalization to be good rather than bad.

### [38:26 - 38:50]

I'm not trying to kickstart this initial crux again, but I'm just genuinely curious, because I think I might be using the term differently. Yeah. I mean, one way to think about it is these LLMs are increasing the scope of generalization from earlier systems, which could not really even do a basic math problem, to now they can do anything in this class of Math Olympia-type problems, right?

### [38:50 - 39:13]

So you initially start with, they can generalize among addition problems, at least. Then you generalize to… They can generalize among problems which require use of different kinds of mathematical techniques and theorems and conceptualization. Right. Or conceptual categories, which is like what the Math Olympiad requires. And so it sounds like you don't think of being able to solve any problem within that

### [39:13 - 39:40]

category as an example of generalization? Or let me know if I'm misunderstanding that. Well, large language models, so complex. We don't really know what information they had prior. We have to guess, because they've been fed so much. This is one reason why they're not a good way to do science. It's just so uncontrolled, so unknown. But if you come up with an entirely new…

### [39:40 - 40:04]

They're getting a bunch of things right, perhaps. And so the question is why? Well, it may be that they don't need to generalize to get them right, because the only way to get some of them right is to form something which gets all of them right. So if there's only one answer, and you find it, that's not called generalization. It's the only way to solve it. And so they find the only way to solve it.

### [40:04 - 40:28]

Generalization is when it could be this way, it could be that way, and they do it the good way. My understanding is that this is working better and better with coding agents. So engineers, obviously, if you're trying to program a library, there's many different ways you could achieve the end spec, and an initial frustration with these models has been that they'll do it in a way that's sloppy.

### [40:28 - 40:52]

And then over time, they're getting better and better at coming up with the design architecture, and the abstractions that developers find more satisfying, and it seems an example of what you're talking about. Well, there's nothing in them which will cause it to generalize well. Creating dissent will cause them to find a solution to the problems they've seen.

### [40:52 - 41:15]

And if there's only one way to solve them, they'll do that. But there are many ways to solve it, some which generalize well, some which generalize poorly. There's nothing in them, in the algorithms, that will cause them to generalize well. Yeah. But people, of course, are involved, and if it's not working out, they fiddle with it until they find a way, perhaps until they find a way which it generalizes well.

### [41:15 - 41:36]

So to prep for this interview, I wanted to understand the full history of RL, starting with reinforce up to current techniques, like GRPO. And I didn't just want a list of equations and algorithms. I wanted to really understand each change in this progression and the underlying motivation. What was the main problem that each successive method was actually trying to solve?

### [41:36 - 41:56]

So I had Gemini Deep Research walk me through this entire timeline, step by step. It explained the last 20 years of gradual innovation, and explained how each step made the RL learning process more stable, or more sample-efficient, or more scalable. I asked Deep Research to put all of this together like an Andrej Karpathy-style tutorial. And it did that.

### [41:56 - 42:17]

What was cool is that it combined this whole lesson together into one coherent, cohesive document in the style that I wanted. It was also great that it assembled all of the best links in the same place, so that if I wanted to understand any specific algorithm better, I could just access the right explainer right there. Go to gemini.google.com to try it out yourself. All right, back to Richard.

### [42:17 - 42:46]

I want to zoom out and ask about being in the field of AI for longer than almost anybody who is commentating on it or working in it now. I'm just curious about what the biggest surprises have been. How much new stuff do you feel like is coming out, or does it feel like people are just playing with old ideas? You got into this even before deep learning was popular, so how do you see this trajectory

### [42:46 - 43:15]

of this field over time, and how new ideas have come about and everything? And what's been surprising? Okay, so yeah, I thought a little bit about this. There are many things, or a handful of things. First, the large-line models. All right. The large-line models are surprising. It's surprising how effective neural networks, artificial neural networks, are at language tasks. Right. That was a surprise.

### [43:15 - 43:45]

It wasn't expected. Language seemed different. So that's impressive. There's a longstanding controversy in AI about simple basic principle methods, the general-purpose methods like search and learning and computing. And compared to human-enabled systems, like symbolic methods. And so in the old days, it was interesting, because things like search and learning were called weak methods.

### [43:45 - 44:16]

Because they just use general principles. They're not using the power that comes from imbuing a system with human knowledge. So those were called strong. And so I think the weak methods have just totally won. That's what I think. That's the biggest question. From the old days of AI, what would happen, and learning and search have just won the day. Right. But there's a sense which that was not surprising to me.

### [44:16 - 44:41]

Because I was always voting for, or hoping, or rooting for the simple basic principles. And so even with the large-line models, it's surprising how well it worked. But it was all good and gratifying. And in things like AlphaGo, it's sort of surprising how well that was able to work. And AlphaZero in particular, how well it was able to work. But it's all very gratifying.

### [44:41 - 45:03]

Because again, it's simple basic principles are winning the day. Have there felt like whenever the public conception has been changed because some new technique was, or sorry, some new application was developed, for example, when AlphaZero became this viral sensation. And to you, as somebody who has literally came up with many of the techniques that were

### [45:03 - 45:28]

used, did it feel to you like new breakthroughs were made, or does it feel like, oh, we've had these techniques since the 90s, and people are simply combining them and applying them now? So the whole AlphaGo thing has a precursor, which is TD Gammon. Jerry Tesaro did exactly reinforcement learning, temporal difference learning methods to play backgammon. Right. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

### [45:28 - 45:58]

And it beat the world's best players, and it worked really well. And so in some sense, AlphaGo was merely a scaling up of that process. It was quite a bit of scaling up, and there was also an additional innovation in how the search was done. Right. But it made sense. It wasn't surprising in that sense. AlphaGo actually didn't use TD learning. It waited to see the final outcomes. But AlphaZero used TD learning.

### [45:58 - 46:28]

And AlphaZero was applied to all the other games, and that did extremely well. I've always been very impressed by the way AlphaZero plays chess, because I'm a chess player, and it just sacrifices material for sort of positional advantages, and it's just content and patient to sacrifice that material for a long period of time. And so that was surprising that it worked so well, but also gratifying. Yeah.

### [46:28 - 46:58]

And it's fitting into my worldview. So this has led me where I am. Where I am is I'm in some sense a contrarian, or thinking differently from the field is. And I am personally just kind of content being out of sync with my field for a long period of time, perhaps decades, because occasionally I have improved right in the past. And the other thing I do to help me not feel I'm out of sync and think,

### [46:58 - 47:28]

in a strange way, is to look not at my local environment or my local field, but to look back in time, into history, and to see what people have thought classically about the mind in many different fields. And I don't feel I'm out of sync with the larger traditions. I really view myself as a classicist rather than as a contrarian. I go to what the larger community of thinkers about the mind have always thought. Okay.

### [47:29 - 47:57]

Some sort of left-field questions for you, if you'll tolerate them. So the way I read the bitter lesson is that it's not saying necessarily that human artisanal researcher tuning doesn't work, but that it obviously scales much worse than compute, which is growing exponentially. And so you want techniques which leverage the latter. Yep. And once we have AGI, we'll have researchers.

### [47:57 - 48:23]

We'll have researchers which scale linearly with compute, right? So we'll have this avalanche of millions of AI researchers, and their stock will be growing as fast as compute. And so maybe this will mean that it is rational, or it will make sense to have them doing good old-fashioned AI and doing these artisanal solutions. Does that, as a vision of what happens after AGI in terms of how AI researchers will evolve,

### [48:23 - 48:46]

I wonder if that's still compatible with the bitter lesson. Well, how did we get to this AGI? You want to presume that it's been done. So suppose it started with general methods, but now we've got the AGI. And now we want to go... Then we're done. Hmm? We're done. Interesting. You don't think that there's anything above AGI? Well, but you're using it to get AGI again.

### [48:47 - 49:12]

Well, I'm using it to get superhuman levels of intelligence or competence at different tasks. So these AGIs, if they're not superhuman already, then the knowledge that they might impart would be not superhuman. I guess there's different gradations of superhuman. I'm not sure your idea makes sense, because it seems to presume the existence of AGI. And then we've already worked that out.

### [49:12 - 49:37]

So maybe one way to motivate this is AlphaGo is superhuman. It beat any Go player. AlphaZero would beat AlphaGo every single time. So there's ways to get more superhuman than even superhuman. And it was a different architecture. And so it seems plausible to me that, well, the agent that's able to generally learn across all domains, there would be ways to make that, give it better architecture for

### [49:37 - 50:04]

learning, just the same way that AlphaZero was an improvement upon AlphaGo and MuZero was an improvement upon AlphaZero. And the way AlphaZero was an improvement was it did not use the human knowledge, but just went from experience. Right. So why do you say bring in other agents' expertise to teach it? When it's worked so well from experience and not by help from another agent?

### [50:05 - 50:27]

I agree that in that particular case, that it was moving to more general methods. But I meant to use that example to illustrate that it's possible to go superhuman to superhuman plus plus to superhuman plus plus plus plus. Yeah. And I'm curious if you think those gradations will continue to happen by just making the method simpler or because we'll have the capability of these millions of minds who can then

### [50:27 - 50:53]

add complexity as needed, if that will continue to be a false path, even when you have billions of AI researchers or trillions of AI researchers. I think more interesting is just think about that case, which when you have many AIs, will they help each other the way cultural evolution works in people? Let's just, maybe we should talk about that. Yeah, for sure. The bitter lesson. Oh, who cares about that?

### [50:53 - 51:10]

That's an empirical observation about a particular period in history. 70 years in history, no longer, doesn't necessarily have to apply the next 70 years. So the interesting question is, you're an AI, you get some more computer power, should you use it to make yourself more computationally capable or should you use it to spawn off

### [51:10 - 51:36]

a copy of yourself to go learn something interesting on the other side of the planet or on some other topic and then report back to you? Yep. I think that's a really interesting question that will only arise in the age of digital intelligence. I'm not sure what the answer is, but I think it will, more questions, will it be possible to really, you know, spawn it off, send it out, learn something new, something perhaps

### [51:36 - 52:00]

very new, and then will it be able to be reincorporated into the original or will it, will it, will have changed so much that it, it can't really be done? Yeah. Is that possible or is it not? And, you know, you can carry this to its limit as I, I saw one of your videos the other night that, that suggested that it. That it could, where you spawn off many, many copies, do different things, it's highly

### [52:00 - 52:25]

decentralized, but report back to the, the central master and that this is, this will be such a powerful thing. Well, I think one thing that, so this is my attempt to add something to this, this view is that a big question, a big issue will become corruption. You know, if you, if you really could just get information from anywhere and bring it into your central mind, you can become more and more powerful.

### [52:26 - 52:49]

Uh, and it's, it's all digital and they all speak some internal digital language. Maybe it'll be easy and possible, but it will not be that easy, as easy as you're imagining because, uh, that you can lose your mind this way. If you pull in something from the outside and build it into your, into your inner thinking, uh, it could take over you. It could change you.

### [52:49 - 53:13]

It could be, uh, your destruction rather than, uh, your increment in knowledge. Mm. I think this will become a big concern, you know, particularly when you're, oh, he's figured all about, you know, how to play some new game or figured out he's, he's studied Indonesia and you want to incorporate that into your mind. Um, yeah. So you can't, you could, you think, oh, just read it all in and that'll be fine.

### [53:13 - 53:40]

But no, you've just read a whole bunch of bits into your mind and, uh, they could have viruses in them. They could have hidden goals. Uh, they can, uh, work you and change you. And this will be, uh, become a big thing. How do you have cybersecurity in the age of digital spawning and re-reforming again? It's interesting that both quant firms and AI labs have a culture of secrecy because

### [53:40 - 53:58]

both of them are operating in incredibly competitive markets and their success rests on protecting their IP. If you're an AI researcher or engineer and you're deciding where to work, most of the quant firms or AI labs that you'll be considering will be strongly siloing their teams to minimize the risk of leaks. Hudson River Trading takes the opposite approach.

### [53:58 - 54:20]

Their teams openly share their trading strategies and their strategy code lives in a shared monorepo. At HRT, if you're a researcher and you have a good idea, your contribution will be broadly deployed across all relevant strategies. This gives your work a ton of leverage. You'll also learn incredibly fast. You can learn about other people's research and ask questions and you can see how everything

### [54:20 - 54:45]

fits together end to end from the low level of execution of trades to the high level of predictive models. HRT is hiring. If you want to learn more, go to hudsonrivertrading.com slash thwarkash. All right. Back to Richard. I guess this brings us to the topic of AI succession. You have a perspective that's quite different from a lot of people that I've interviewed and maybe a lot of people generally.

### [54:45 - 55:13]

So I also think it's a very interesting perspective. I want to hear about it. Yeah. So I do think succession to digital. All right. Yeah. So I think the argument for AI or digital intelligence or augmented humans is inevitable. So the argument – I have a four-part argument. Step one is there's no government or organization that gives humanity a unified point of view

### [55:13 - 55:40]

that dominates and that can arrange – there's no consensus about how the world should be run. And number two, we will figure out how intelligence works. Researchers will figure it out eventually. And number three, we won't stop just with human-level intelligence. We will get – reach superintelligence. And number four is that once – it's inevitable over time that the most intelligent things

### [55:40 - 56:12]

around would gain resources and power. And so put all that together, it's, you know, you – it's sort of inevitable that you're going to have succession to AI. Succession to AI or to AI-enabled augmented humans. So within those four things seem clear and sure to happen. But within that set of possibilities, some – there can be good outcomes as well as less good outcomes, bad outcomes.

### [56:12 - 56:41]

And so I'm just trying to be realistic about where we are and ask how we should feel about it. Yeah. I agree with all four of those arguments and the implication. And I also agree that succession contains a wide variety of possible futures. So curious to get more thoughts on that. Right. And so then I do encourage people to think positively about it, first of all, because

### [56:41 - 57:11]

it's something we humans have always tried to do for thousands of years, trying to understand themselves, trying to make themselves think better and, you know, just understand themselves. Yeah. So this is a great success from – as science, humanities, we're finding out what this essential part of humanness is, what it means to be intelligent. And then what I usually say is that this is all kind of human-centric.

### [57:11 - 57:37]

What if we look – you step aside from being a human and just say – take the point of view of the universe. And this is, I think, a major stage in the universe, a major transition. A transition from humanism. Yeah. So replicators, humans and animals, plants, we're all replicators. And that gives us some strengths and some limitations. And then we're entering the age of design, where – because our AIs are designed, all

### [57:37 - 58:05]

of our physical objects are designed, our buildings are designed, our technology is designed, and we're designing now AIs, things that can be intelligent themselves and that are themselves capable of design. And so this is a key step. This is a key step in the world and in the universe, and I think it's the transition from the world in which most of the interesting things that are, are replicated.

### [58:05 - 58:26]

Replicated means you can make copies of them, but you don't really understand them. Like right now, we can make more intelligent beings, more children, but we don't really understand how intelligence works. Whereas in – we're reaching now to having design intelligence, intelligence that we do understand. We understand how it works, and therefore we can change it in different ways and at

### [58:26 - 58:56]

different speeds than otherwise. And our future, they might not be replicated at all. Like we may just design AIs, and those AIs will design other AIs, and everything will be done by design and construction rather than by replication. Yeah. I mark this as one of the four great stages of the universe. First there's dust, ends of stars, stars. And then stars make planets, and the planets give rise to life.

### [58:56 - 59:21]

And now we're giving life to designed entities. And so I think we should be proud, and we should be – that we are giving rise to this great transition in the universe. Yeah. So it's an interesting thing. What should we – should we consider them part of humanity or different from humanity? It's our choice. It's our choice whether we should say, oh.

### [59:21 - 59:42]

They are our offspring, and we should be proud of them, and we should celebrate their achievements. Or we should – we could say, oh, no. They're not us, and we should be horrified. It's just – it's interesting that that is – it feels to me like a choice. And yet it's such a strongly held thing that how can we be a choice? I like these sort of contradictory implications of thought.

### [59:42 - 01:00:02]

I mean, it's interesting to consider if we were just designing another generation of humans. Yes. Design's the wrong word. Yes. The next generation of humans is going to come up. And forget about AI. We just know in the long run, humanity will be more capable and maybe more numerous, maybe more intelligent. How do we feel about that?

### [01:00:02 - 01:00:20]

I do think there's potential worlds with future humans that we would be quite concerned about. So are you thinking, like, maybe we are like the Neanderthals who give rise to Homo sapiens. Maybe Homo sapiens will give rise to a new group of people. That's what you're saying? Something like that. Like, I'm basically taking the example you're giving.

### [01:00:20 - 01:00:45]

I'm like, OK, even if you consider them part of humanity, I don't think that necessarily means that we should feel super comfortable. Hinship. Yeah. Like Nazis were humans, right? If we thought like, oh, the future generation will be Nazis, I think we'd be quite concerned about just handing off power to them. So I agree that this is not super dissimilar to worrying about more capable future humans.

### [01:00:45 - 01:01:19]

But I don't think that that addresses a lot of the concerns people might have about this level of power being attained this fast with entities we don't fully understand. Well, I think it's relevant to point out that for most of humanity, they don't have much influence on what happens. Most of humanity doesn't influence who can control the atom bombs or who controls the nation states. Right. Right.

### [01:01:19 - 01:01:49]

And as a citizen, I often feel that we don't control the nation states very much. They're out of control. A lot of it has to do with just how you feel about change. And if you think the current situation is really, really good, then you're more likely to be suspicious of change and averse to change than if you think it's imperfect. I think it's imperfect. In fact, I think it's pretty bad. So I'm open to change.

### [01:01:49 - 01:02:17]

I think humanity has had a super good track record. Maybe it's the best thing that there's been, but it's far from perfect. Yeah. I guess there's different varieties of change. The Industrial Revolution was change. The Bolshevik Revolution was also change. And if you were around in Russia in the 1900s and you're like, look, things aren't growing well. The czar is kind of messing things up. We need change.

### [01:02:17 - 01:02:48]

I'd want to know. What kind of change you wanted before signing on the dotted line. And then similar with AI, where I'd want to understand and to the extent it's possible to change the trajectory of AI such that the change is positive for humans. We should be concerned about our future, the future. We should try to make it good. We also, though, should recognize the limits, our limits. Yeah.

### [01:02:48 - 01:03:18]

I think we want to avoid the feeling of entitlement. Avoid the feeling, oh, we're here first. We should always have it in a good way. How should we think about the future and how much control a particular species on a particular planet should have over it. How much control do we have? You know, a counterbalance to our limited control over the long-term future of humanity. Yeah. Yeah.

### [01:03:18 - 01:03:46]

how much control do we have over our own lives like we have uh our own goals and we have our families and we those things are much more controllable than like trying to control um the whole universe right um so i think it's appropriate you know for us to to uh you know really work towards our own local goals and uh and it's kind of aggressive for us saying

### [01:03:46 - 01:04:10]

oh the future has to evolve this way that i want it to sure because then we'll have arguments like different people think the future the global future should evolve in different ways and they have conflict and yeah you want to avoid that maybe a good analogy here would be okay so suppose you're raising your own children it might not be appropriate to have extremely tight goals for

### [01:04:10 - 01:04:34]

their own life or also have some sense of like i want my children to go out there in the world and have this specific impact my son's gonna become president and my daughter's gonna become ceo of intel and like together they're gonna have this effect on the world um but people do have the sense that i think this is appropriate of saying i'm going to give them good robust values such that if and when they do

### [01:04:34 - 01:05:00]

end up in positions of power they do reasonable pro-social things and i think maybe a similar attitude towards ai makes sense not in the sense of we can predict everything that they will do where we have this plan about what the world should look like in 100 years but it's quite important to give them robust and steerable and pro-social values pro-social values

### [01:05:00 - 01:05:22]

maybe that's the wrong word are there universal values that we can all agree on i don't think so but that doesn't prevent us from uh giving our kids a good education right like we have some sense of we want our children to be a certain way yeah and maybe process is the wrong word high integrity is maybe a better word where if there's a request or if there's a goal that

### [01:05:22 - 01:05:46]

seems harmful they will refuse to engage in it um or they'll be honest um things like that and we have some sense that we can teach our children things like this even if we don't have some sense of what true morality is or everybody doesn't agree on that um and maybe that's a reasonable target for ai as well so so you're saying we're trying to design the future and the

### [01:05:46 - 01:06:10]

principles by which it will evolve and come into being right and so you're saying the first thing you're saying is well we will we try to teach our our children um general principles which will promote more likely evolutions yeah um maybe we should also seek for things being voluntary if there is change we want it to be a volunteer rather than imposed on people i think that's a

### [01:06:10 - 01:06:35]

very important point yeah um and yeah that's all good i think i think this is like a big you know the big the big or one of the really big human enterprises to design society and that's been ongoing for for thousands of years again and so so it's like the more things change really the more things they stay the same we still have to figure out how to be uh the children will still

### [01:06:35 - 01:06:57]

come up with different values that seem strange to their parents and their grandparents and uh and things will evolve the more things change the more they stay the same also seems like a good capstone to the ai discussion because the ai discussion we were having was about how techniques which were um invented even before the application to deep learning and back propagation

### [01:06:57 - 01:07:08]

was evident have are you know central to the progression of ai today so maybe that's a good place to wrap up the conversation okay thank you very much thank you for coming on my pleasure
