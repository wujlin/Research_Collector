# RLDM2025 Ben Eysenbach Self-Supervised Representations and Reinforcement

- URL: https://www.youtube.com/watch?v=K-YKff74KSQ
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T10:27:20`

## Transcript

### [00:00 - 00:09]

So next, we've got Ben Eysenbach from Princeton University for the second of our advanced tutorials. He's going to talk about self-supervised reinforcement learning. Thanks, Ben.

### [00:19 - 00:22]

Can you focus in the back of your meal, all right? Perfect.

### [00:30 - 00:43]

Excellent. It is a great honor to be here. I am Ben Eysenbach from Princeton University, and the second tutorial today is about self-supervised reinforcement learning.

### [00:43 - 00:50]

This is going to be very much on the AI side of things, and so let's get started.

### [00:50 - 00:58]

So the tutorial today is going to be about AI methods that can discover small reusable skills on their own.

### [00:58 - 00:59]

And importantly,

### [00:59 - 01:02]

these skills are not going to be programmed in advanced,

### [01:02 - 01:11]

but rather they're going to be discovered through exploration, through experimentation, without needing demonstrations, without needing rewards.

### [01:11 - 01:18]

We'll talk about how we can learn these skills and then how we can use them to rapidly solve new tasks.

### [01:18 - 01:26]

So machine learning today, we often think about machine learning models that are taught by giving them examples of what humans would do.

### [01:26 - 01:28]

So the big language models,

### [01:28 - 01:29]

they're trained by

### [01:29 - 01:43]

the AI to predict the next word that they see trained primarily on the Internet, on text written by humans, and then they're largely fine-tuned on expert responses by trying to mimic how experts would respond to certain prompts.

### [01:43 - 01:49]

The robots that we have today, the successes that we hear about are primarily driven by imitation.

### [01:49 - 01:53]

And the same is true for autonomous driving.

### [01:53 - 01:56]

I think the reason why a lot of us are really excited about reinforcement learning methods is that they give us tools to solve problems.

### [01:56 - 01:57]

And so,

### [01:57 - 01:58]

I think the reason why a lot of us are really excited about reinforcement learning methods is that they give us tools to solve problems.

### [01:58 - 01:59]

And so,

### [01:59 - 02:10]

I think the reason why a lot of us are really excited about reinforcement learning methods is that they give us tools to solve problems that we humans currently don't know how to solve, or they might give us better solutions than the ones that we humans have come up with so far.

### [02:10 - 02:15]

So just this past year, the touring award was given for reinforcement learning.

### [02:15 - 02:18]

But I think that we're only still seeing the tip of the iceberg.

### [02:18 - 02:25]

I think that there's a whole slew of other capabilities that reinforcement learning methods might be able to unlock.

### [02:25 - 02:27]

But I think that realizing that is going to require addressing a couple of key challenges.

### [02:27 - 02:28]

I think that there's a whole slew of other capabilities that reinforcement learning methods might be able to unlock.

### [02:28 - 02:29]

But I think that realizing that is going to require addressing a couple of key challenges trying to do things that reinforcement learning methods really should be able to do.

### [02:29 - 02:30]

But I think that realizing that is going to require addressing a couple of key challenges trying to do things that reinforcement learning methods really should be able to do.

### [02:30 - 02:31]

But I think that realizing that is going to require addressing a couple of key challenges trying to do things that reinforcement learning methods really should be able to do.

### [02:31 - 02:32]

One of those is reasoning over long horizons.

### [02:32 - 02:33]

One salient difference between reinforcement learning methods and supervised learning methods is that reinforcement learning methods care not just about good outcomes today, but about good outcomes tomorrow and the next day.

### [02:33 - 02:34]

One of those is reasoning over long horizons.

### [02:34 - 02:35]

One salient difference between reinforcement learning methods and supervised learning methods is that reinforcement learning methods care not just about good outcomes today, but about good outcomes tomorrow and the next day.

### [02:35 - 02:36]

One of those is reasoning over long horizons.

### [02:36 - 02:41]

reasons. One salient difference between reinforcement learning methods and supervised learning methods

### [02:41 - 02:46]

is that reinforcement learning methods care not just about good outcomes today, but about

### [02:46 - 02:52]

good outcomes tomorrow and the next day. But it turns out that planning really far into

### [02:52 - 02:58]

the future is just really hard. And closely related to this is that reinforcement learning

### [02:58 - 03:03]

methods are supposed to be able to learn from sparse rewards. If we want reinforcement learning

### [03:03 - 03:09]

methods to solve tasks we don't know how to solve, I can't write down a nice, dense

### [03:09 - 03:14]

reward function because I don't know how the task will be solved.

### [03:14 - 03:20]

Now, conceptually, one way of thinking about these challenges of long horizons, sparse

### [03:20 - 03:25]

rewards, is by thinking about building a tower of cards like that guy up there is doing.

### [03:25 - 03:29]

You can imagine how difficult it would be to learn how to build a tower of cards like

### [03:29 - 03:33]

that if you didn't get any rewards along the way. And only at the end of the day, you

### [03:33 - 03:39]

place the last card into place, would you get any rewards saying you had successfully

### [03:39 - 03:45]

built a tower of cards like this. How could you even learn how to stack two cards on top

### [03:45 - 03:49]

of each other if you only got rewards at the end of the day?

### [03:49 - 03:55]

So these two challenges of long horizons and sparse rewards, they're typically conceptualized

### [03:55 - 03:59]

as the problem of exploration, one of these key challenges in reinforcement learning.

### [03:59 - 04:03]

But I think this term exploration, it doesn't quite do it justice.

### [04:03 - 04:10]

I think, zooming out for a second, the real challenge here is that reinforcement learning

### [04:10 - 04:16]

is a problem of searching over this big space of behaviors, this huge space of behaviors

### [04:16 - 04:22]

that we need to explore and discover, and then we need to organize.

### [04:22 - 04:27]

And maybe I guess as a cartoon, we can think about this big space of behaviors as this

### [04:27 - 04:33]

kind of ugly drawing here. How do we discover all of the things that an agent can do in

### [04:33 - 04:33]

an environment?

### [04:33 - 04:38]

And then how can we make sense of it so that we can quickly solve a reinforcement learning

### [04:38 - 04:42]

problem?

### [04:42 - 04:46]

For example, let's think about solving this manipulation problem here.

### [04:46 - 04:50]

You have this robot, there's this block here, and there are many, many things that this

### [04:50 - 04:53]

robot can do.

### [04:53 - 04:59]

You can think about the behavior it's executing right now as just a certain point on this

### [04:59 - 05:01]

big space of behaviors.

### [05:01 - 05:03]

But there are a lot of other things that this robot could do.

### [05:03 - 05:12]

Here's another example of behavior that this robot can do.

### [05:12 - 05:14]

This robot can move his arm in different ways.

### [05:14 - 05:17]

It could throw the block around, it could start juggling the block, start balancing

### [05:17 - 05:21]

the block on the corner of one of these drawers.

### [05:21 - 05:25]

So fundamentally, this space of behaviors is really, really complex.

### [05:25 - 05:32]

Now, functionally, when we're applying reinforcement learning methods today, we often describe

### [05:32 - 05:33]

behavior with a neural network.

### [05:33 - 05:33]

So we're going to use a neural network.

### [05:33 - 05:33]

We're going to use a neural network.

### [05:33 - 05:33]

We're going to use a neural network.

### [05:33 - 05:33]

We're going to use a neural network.

### [05:33 - 05:33]

We're going to use a neural network.

### [05:33 - 05:37]

We're going to use a neural network with a whole lot of parameters.

### [05:37 - 05:41]

And the questions we think about are, how do we update the neural network parameters

### [05:41 - 05:46]

to get the sorts of behaviors that we care about?

### [05:46 - 05:50]

So if I look at one individual parameter in this neural network, I might think about,

### [05:50 - 05:55]

how does changing this one parameter change the behavior of this policy?

### [05:55 - 05:58]

But of course, this is a really, really hard problem to reason about.

### [05:58 - 06:01]

There might be millions of parameters here.

### [06:01 - 06:03]

Changing some parameters may have no effect on the behavior.

### [06:03 - 06:07]

Changing other parameters may have a huge effect on the behavior.

### [06:07 - 06:13]

So two parameters may have the same effect on behavior.

### [06:13 - 06:22]

So today, I want you to imagine a knob, a small dial, such that when you turn that dial,

### [06:22 - 06:27]

you get different behaviors.

### [06:27 - 06:32]

For another task, maybe this quadrupedal robot like this, setting the knob to one value gives

### [06:32 - 06:33]

you a behavior like this.

### [06:33 - 06:39]

Setting the knob to a different value gives a behavior like this.

### [06:39 - 06:44]

Hopefully you can see how having a knob like this would be really valuable.

### [06:44 - 06:48]

You might solve new problems by just turning this knob to different values.

### [06:48 - 06:53]

Maybe some problems require two knobs, but it'd be very easy to simply tune these knobs

### [06:53 - 06:57]

rather than having to search over this enormous complex space of behaviors.

### [06:57 - 07:03]

Formally, we might think about these knobs as sweeping over this big, complex space of

### [07:03 - 07:06]

behaviors.

### [07:06 - 07:12]

So today's goal is to figure out how do we take this big space of behaviors and compress

### [07:12 - 07:18]

it, compress it in a way so that we can easily search over it to solve new tasks.

### [07:18 - 07:21]

And we'll see that this involves a couple pieces.

### [07:21 - 07:27]

One is we have to discover what are all of the behaviors that are possible in an environment.

### [07:27 - 07:32]

And second, how do we compress these behaviors so that we can quickly search over it to solve

### [07:32 - 07:33]

some new downstream problem?

### [07:33 - 07:40]

One way of thinking about this is that this knob here is a pre-training task.

### [07:40 - 07:47]

It's a form of self-supervised learning, a form of learning that doesn't require demonstrations,

### [07:47 - 07:48]

it doesn't require rewards.

### [07:48 - 07:55]

One thing to note is that there are lots of other ways that people have conceptualized

### [07:55 - 07:57]

free training for reinforcement learning.

### [07:57 - 08:02]

But I really like this analogy of this knob here because it suggests that the benefits

### [08:02 - 08:03]

that we get from reinforcement learning are not necessarily the same as the benefits we're

### [08:03 - 08:09]

learning are about interaction. So it makes sense that for pre-training, we also care about

### [08:09 - 08:15]

interaction. So here's the goal for today. How do we compress big spaces of behavior?

### [08:18 - 08:23]

Now, as you start to think about this, one frame of reference that might come into mind

### [08:23 - 08:28]

is intrinsic motivation. This really rich line of work on thinking about rewards coming from

### [08:28 - 08:34]

surprise, from novelty, from curiosity. This line of work is really important, and we'll see that

### [08:34 - 08:39]

there's strong connections between intrinsic motivation and learning these behaviors that

### [08:39 - 08:47]

we talk about today. What I want to focus on today is a lens of, or a way of thinking about

### [08:47 - 08:52]

intrinsic motivation that allows us to quickly solve new tasks. And so we're going to focus on

### [08:52 - 08:57]

intrinsic motivation methods that give us this knob, this knob which will then give us many

### [08:57 - 08:58]

candidate solutions.

### [08:58 - 09:00]

For quickly solving new tasks.

### [09:05 - 09:10]

So the goal for today is to figure out how do we compress this big, large space of behaviors?

### [09:10 - 09:13]

How do we discover it? And then how do we make it easy to search over?

### [09:15 - 09:19]

And so here's what we're going to do in the tutorial today. I want to start by describing a

### [09:19 - 09:24]

game, a game that you and I might play out on the soccer pitch outside. And we'll see how this game

### [09:24 - 09:28]

describes how we can go about learning these behaviors or these skills.

### [09:28 - 09:34]

We'll then talk about how you can formalize this into an algorithm that you actually can run

### [09:34 - 09:41]

on your laptop or on your computer cluster. I'll then show several examples from a variety of labs

### [09:41 - 09:47]

that these skill learning algorithms, they actually work. I'll then talk a little bit

### [09:47 - 09:51]

about mathematically what's going on to try to give us some shared language for describing

### [09:51 - 09:55]

what's happening. And we'll see it actually closely mirror some of the probabilistic language

### [09:55 - 09:56]

from the first tutorial today.

### [09:56 - 10:03]

We'll then talk about how you can use these skills to quickly solve downstream tasks.

### [10:03 - 10:07]

Both practically, how do you use the skills, but also theoretically, can you prove that

### [10:07 - 10:11]

these skills might be useful for solving new tasks?

### [10:11 - 10:15]

And then at the end, I'm going to talk a little bit about what I see as the frontier of skill

### [10:15 - 10:16]

learning.

### [10:16 - 10:19]

How do we unlock this next generation of skill learning algorithms?

### [10:19 - 10:23]

How do we hopefully see the underside of this big iceberg?

### [10:26 - 10:30]

Now, before I keep diving into this, I should note, there are many, many different ways

### [10:30 - 10:35]

of thinking about self-supervised reinforcement learning, or thinking about trying to learn

### [10:35 - 10:38]

some behavioral foundation model.

### [10:38 - 10:41]

There's some folks that think about the exploration facet of this.

### [10:41 - 10:45]

How do you go and explore big, complex environments?

### [10:45 - 10:49]

And there are other folks that think about the representation learning problem, and yet

### [10:49 - 10:51]

other folks that think about skill learning.

### [10:51 - 10:53]

And there are yet other perspectives, too.

### [10:53 - 10:55]

I hope that this tutorial will highlight that.

### [10:55 - 10:56]

A lot of these.

### [10:56 - 11:01]

Perspectives on self-supervised reinforcement learning are really different perspectives

### [11:01 - 11:06]

on the same underlying object, but it's also worth noting that I'm sure there are lots

### [11:06 - 11:08]

of perspectives that I don't know about.

### [11:08 - 11:12]

And one of the reasons I'm very excited to be here at RLDM is to learn from all of you.

### [11:12 - 11:17]

So I hope that we can continue the conversations throughout the week.

### [11:17 - 11:21]

Okay, let's get started.

### [11:21 - 11:24]

A couple of definitions so that we're all on the same page.

### [11:24 - 11:25]

I'm going to think about.

### [11:25 - 11:30]

A Markov decision process where we have states or observations.

### [11:30 - 11:37]

S the subscript T denotes time, time goes one, two, three, four, five.

### [11:37 - 11:41]

We'll have actions A. They're taken by an agent.

### [11:41 - 11:47]

And we'll have a skill representation Z. Z here, this could be discrete, just number

### [11:47 - 11:51]

one, two, three, four, five, or maybe five behaviors that you're learning, or it could

### [11:51 - 11:53]

be continuous, some vector.

### [11:53 - 11:54]

And the user is going to choose.

### [11:54 - 11:55]

Okay.

### [11:55 - 12:01]

Use some prior distribution T of Z. This could just be uniform over the numbers one,

### [12:01 - 12:05]

two, three, four, five.

### [12:05 - 12:09]

The policy selects actions given the current state of the world.

### [12:09 - 12:16]

And we'll also talk about policies that are conditioned on a skill representation Z.

### [12:16 - 12:22]

One thing to clarify here is that when I say a skill, I'm really referring to a combination

### [12:22 - 12:24]

of this policy.

### [12:24 - 12:27]

It's conditioned on a skill representation.

### [12:27 - 12:32]

So skill depends both on this skill representation, a number together with this set of policy

### [12:32 - 12:35]

parameters.

### [12:35 - 12:42]

And one object that will be useful for today is the discounted state occupancy measure.

### [12:42 - 12:47]

One way of thinking about this is that imagine you close your eyes, then you run around and

### [12:47 - 12:49]

you open your eyes at a random point in time.

### [12:49 - 12:53]

You want to know, where will you be?

### [12:53 - 12:54]

Where will you be?

### [12:54 - 12:57]

And the answer is described by this probability distribution.

### [12:57 - 13:05]

Us the one minus gamma here simply ensures that this probability distribution songs are

### [13:05 - 13:08]

integrates to one.

### [13:08 - 13:11]

Another way of thinking about this is you want to know the probability that you end

### [13:11 - 13:13]

up in state SF.

### [13:13 - 13:17]

At some point in the teacher, maybe you'd one step, maybe in two steps, maybe in five

### [13:17 - 13:20]

steps.

### [13:20 - 13:23]

You can visualize this as saying, if you're.

### [13:23 - 13:24]

2021.

### [13:24 - 13:24]

arme.

### [13:24 - 13:30]

agent is in this state here its distribution over future states might look something like this

### [13:30 - 13:35]

sampling one of these states with a higher probability on the short horizon states

### [13:36 - 13:42]

for another robot it might look something like this we'll also talk about versions of the

### [13:42 - 13:46]

discounted state occupancy measure that are conditioned on your initial state say where

### [13:46 - 13:51]

will you go if you start here or where will you go if you start here and take this action

### [13:51 - 13:58]

or if you're using skill z where are you likely to go okay so with this notation in place i want

### [13:58 - 14:03]

you to imagine a game a game that if you want you can play this evening on the soccer pitch

### [14:06 - 14:09]

so this game involves two players a red player and a blue player

### [14:10 - 14:16]

and the players stand on either end of a football field the blue player has some message and they

### [14:16 - 14:21]

want to convey that message to the red player who's standing on the either end of the field

### [14:21 - 14:28]

and on the opposite end of the field and so to do this the blue player is going to perform some

### [14:28 - 14:35]

behavior maybe walking and looking down and then the red player has to guess what message is the

### [14:35 - 14:41]

blue player trying to send me if the blue player is trying to send a different message

### [14:42 - 14:43]

they might do a different behavior

### [14:46 - 14:51]

they're trying to send a different message might do a different behavior and so on and so forth

### [14:51 - 14:57]

one thing to note is that this is a cooperative game the two players are on the same team they're

### [14:57 - 15:03]

trying to both effectively send messages and i want you to think for a moment how would you play

### [15:03 - 15:10]

this game if you were the blue player and you had one six different messages you wanted to send

### [15:10 - 15:16]

what would be the six behaviors that you learned would they be similar to one another would be

### [15:16 - 15:21]

different to one another would you just use your left hand or would you use both of your hands

### [15:21 - 15:29]

and jump up and down one thing to note here is that if you just look at one of these behaviors

### [15:29 - 15:35]

in isolation it's kind of hard to say whether this one behavior is good or not you really have

### [15:35 - 15:40]

to think about this collective set of behaviors to say whether this is a good strategy for playing

### [15:40 - 15:50]

this game and throughout today's tutorial i'll refer to one of these behaviors as a skill

### [15:52 - 15:56]

so what sorts of skills would you expect to emerge

### [15:56 - 15:59]

between two players who were pretty adept at playing this game

### [16:01 - 16:06]

well you'd probably expect that the blue player would end up exploring a lot of different

### [16:06 - 16:11]

behaviors they would end up learning different skills that cover different states because

### [16:11 - 16:16]

doing so allows them to effectively convey different messages but you would also expect

### [16:16 - 16:21]

that the blue player will act predictably when they're sending a certain message they'll always

### [16:21 - 16:26]

do the same behavior because this will make it easier for the red player to guess what are they

### [16:26 - 16:33]

trying to do what message are they trying to send to start and build some intuition into what's

### [16:33 - 16:38]

happening here you can think about player a really as sending a message a coded message

### [16:38 - 16:45]

the player to the other player the red player when the blue player wants to send the message

### [16:45 - 16:50]

a they'll do a certain behavior when they want to send the message b they'll do a different behavior

### [16:52 - 16:57]

and we can actually measure how many bits of information the blue player is sending to

### [16:57 - 17:03]

the red player by looking at how effectively the red player can guess the message that the blue

### [17:03 - 17:09]

player was trying to send we see here we're looking at when the blue player does this

### [17:09 - 17:14]

how what is the probability that the red player assigns to message b

### [17:18 - 17:21]

and so this is the game that you and i could play

### [17:21 - 17:25]

and the game results in the blue player learning a set of behaviors

### [17:26 - 17:29]

that was exactly what we started this tutorial by trying to figure out how to do

### [17:30 - 17:35]

so let's now walk through how we can translate this game into a practical algorithm that we

### [17:35 - 17:45]

actually can run on our computers so we'll and just for context here i'm thinking about

### [17:45 - 17:50]

a setting where we have some environment that we can interact with but it won't give us any rewards

### [17:52 - 17:55]

so we'll start each round of the algorithm by sampling a skill

### [17:55 - 17:59]

representation one of these zeds maybe gets a number from one to five

### [18:03 - 18:06]

we then have a skill that will select actions

### [18:06 - 18:14]

and get observations and select next actions and get next observations executing some behavior

### [18:14 - 18:19]

and this is exactly the role that the blue player was performing in this game that we talked about

### [18:22 - 18:26]

we then have this discriminator this red player that looks

### [18:26 - 18:31]

at the observations and tries to guess what message was the blue player trying to send

### [18:34 - 18:38]

now importantly at the end of the game the red and the blue player they can come together

### [18:38 - 18:44]

and say okay blue player what message were you actually trying to send and the red player could

### [18:44 - 18:50]

update its beliefs so we can get even better at guessing what the blue player was trying to send

### [18:50 - 18:51]

what they were trying to say

### [18:52 - 18:59]

and conversely the blue player can update their behaviors so they're easier to guess

### [18:59 - 19:04]

so it's easier for the red player to guess what they're trying to do in particular they are

### [19:04 - 19:11]

rewarded for going to states where the red player successfully guesses their intention z

### [19:14 - 19:17]

now one thing to emphasize here is that in this entire algorithm

### [19:19 - 19:21]

these rewards are entirely

### [19:22 - 19:27]

intrinsic in the sense that no human had to write down this reward function here

### [19:27 - 19:32]

but rather is just computed in the course of this algorithm without needing any demonstrations

### [19:32 - 19:38]

or any reward definitions and this general prototype of an algorithm

### [19:38 - 19:42]

describes a large number of papers that study how do you learn skills

### [19:45 - 19:51]

so we have this game that we've now translated into an algorithm and perhaps the big overarching

### [19:51 - 19:55]

question is, does this work? Can you actually use this for learning different sorts of behaviors?

### [19:57 - 20:04]

I want to give a couple examples of papers that have used this effectively. One of the ones that

### [20:04 - 20:08]

we worked on several years ago looked at controlling this two-legged dog and using

### [20:08 - 20:12]

this algorithm, we were able to learn different strategies for running forwards and running

### [20:12 - 20:20]

backwards and walking forwards. A couple things to note here. Collectively, these sorts of behaviors

### [20:20 - 20:25]

do effective exploration to cover all sorts of behaviors that you might do in this environment.

### [20:27 - 20:31]

The second thing that you might notice is that if I just showed you one of these videos,

### [20:31 - 20:36]

you probably could guess whether this corresponded to behavior one behavior for

### [20:36 - 20:43]

behavior three, or so on. The behavior's predictable. And one of the reasons this

### [20:43 - 20:48]

is useful is you might now think about how you could use these behaviors to solve a new task.

### [20:48 - 20:50]

If I say,

### [20:50 - 20:55]

you want to get this dog to run and jump over hurdles, you can think about ways of sequencing

### [20:55 - 21:02]

or composing these sorts of behaviors to solve tasks that are longer horizon or have sparse

### [21:02 - 21:10]

rewards. Folks at Google developed a similar skill learning algorithm for controlling this

### [21:10 - 21:18]

quadrupedal robot. And just to emphasize, they're doing this without any demonstrations,

### [21:18 - 21:22]

without any reward shaping.

### [21:22 - 21:27]

Other folks have developed skill learning algorithms for manipulation. So this means

### [21:27 - 21:32]

that now when you want to solve a manipulation problem, you already have this rich basis

### [21:32 - 21:41]

of behaviors to start with. And making use of some demonstrations, you can use skill

### [21:41 - 21:47]

learning methods to automatically learn a wide variety of here animated behaviors.

### [21:48 - 22:01]

Folks have even developed skill learning algorithms for controlling wireless networks. We're

### [22:01 - 22:05]

thinking about how do you assign packets to different cell towers.

### [22:05 - 22:11]

And so the goal for this tutorial is to try to talk about how do you compress this enormous

### [22:11 - 22:17]

space of behaviors? How do you discover what's possible and then organize it? And hopefully

### [22:17 - 22:18]

this game.

### [22:18 - 22:23]

That we've translated into an algorithm makes sense and gives you some intuition for how

### [22:23 - 22:28]

you can automatically discover a large space of behaviors, but then represent it compactly.

### [22:28 - 22:35]

We've seen some examples of how this works so far. At this point, you might be wondering,

### [22:35 - 22:40]

okay, this is great, but open-ended learning is great. But does this actually do anything

### [22:40 - 22:46]

practical? Does this actually, can we actually use this for maximizing rewards? And so in

### [22:46 - 22:48]

the next part of this tutorial,

### [22:48 - 22:53]

I want to talk about mathematically, what is happening under the hood.

### [22:53 - 22:59]

And then we'll talk about using the skills for reward maximization and some future directions.

### [22:59 - 23:04]

So mathematically, what's happening is that these two players are maximizing mutual information.

### [23:04 - 23:09]

That's the tldr. But I can't unpack that. I want to take a step back and talk about

### [23:09 - 23:17]

what mutual information even is. Mutual information takes back to Shannon's paper from 1948. And

### [23:17 - 23:24]

one way of thinking about what mutual information relates to is about thinking about two people

### [23:24 - 23:29]

that are talking on the phone or are communicating over a wire. One player is trying to send a

### [23:29 - 23:35]

message over the wire, and the other player hears a noisy version of that message and

### [23:35 - 23:44]

tries to make out what is the other human trying to say. If this player is able to perfectly

### [23:44 - 23:47]

make out what this player is saying, then the other player is able to make out what

### [23:47 - 23:52]

this player is saying. Then the mutual information between what this player hears and what this

### [23:52 - 23:58]

player says is going to be quite large. In contrast, if this person has no idea what

### [23:58 - 24:02]

this person is saying, if the message gets entirely garbled when it gets sent over this

### [24:02 - 24:09]

wire, then the mutual information will be zero. And formally, the mutual information

### [24:09 - 24:17]

is defined as the difference between two entropies. And the mutual information is symmetric. And

### [24:17 - 24:24]

when the mutual information is

### [24:24 - 24:28]

indicated in the식, then the mutual information iseducated between the two entropies. But

### [24:28 - 24:34]

in this role, one player uses the mutual information as a magnet, and the other player uses it

### [24:34 - 24:39]

as a set of pincers, in the sense that they're soities. And this is easy to understand because

### [24:39 - 24:43]

the neutral information comes from one or more of the two entropies. And so, the rule

### [24:43 - 24:47]

that we have here is that mutual information can be translated over the entire set of entropies.

### [24:47 - 24:54]

Tau here denotes one trajectory of behavior, a sequence of states and actions.

### [24:54 - 25:01]

And Zed here corresponds to these knobs that we want to be able to learn.

### [25:01 - 25:06]

And so what's happening when we're maximizing mutual information is we're trying to learn

### [25:06 - 25:15]

knobs that exert a high degree of influence over the behavior that results.

### [25:15 - 25:19]

Now to unpack this a little bit, we can think about defining this mutual information, rewriting

### [25:19 - 25:25]

it in terms of entropies.

### [25:25 - 25:28]

If we go back and think about when we were playing this game, the sorts of behaviors

### [25:28 - 25:31]

that we thought would emerge, we said that there are two properties.

### [25:31 - 25:32]

One property was exploration.

### [25:32 - 25:37]

We thought that the blue player was going to learn behaviors that effectively cover

### [25:37 - 25:40]

the space of possible behaviors.

### [25:40 - 25:44]

And we can see that maps nicely onto the first term of this mutual information, maximizing

### [25:44 - 25:45]

the.

### [25:45 - 25:53]

Entropy of the trajectories corresponds to trying to do as broad behavior as possible.

### [25:53 - 25:58]

And the second thing that we predicted would emerge from this game is that the blue player

### [25:58 - 26:02]

would perform behaviors that were predictable, so it would be easy for the red player to

### [26:02 - 26:05]

guess what they were trying to do.

### [26:05 - 26:09]

And we see that maps nicely onto the second term in this mutual information, which says

### [26:09 - 26:14]

that for a given message, the blue player could always perform the same behavior.

### [26:15 - 26:22]

Now we can use the fact that the mutual information is symmetric to understand what the algorithm

### [26:22 - 26:25]

I described is doing as well.

### [26:25 - 26:31]

So the algorithm corresponds to maximizing the second equation, which is mathematically

### [26:31 - 26:34]

equivalent to the first.

### [26:34 - 26:41]

Where the second entropy term here says, if you look at the behavior, can you guess what

### [26:41 - 26:44]

message the blue player was trying to send?

### [26:44 - 26:45]

And that's exactly.

### [26:45 - 26:48]

This discriminator was taking.

### [26:48 - 26:53]

And the first term is just a constant, and so we can ignore that.

### [26:53 - 26:58]

So to unpack this a little bit, we can get a lower bound on the mutual information that

### [26:58 - 27:00]

depends on two terms.

### [27:00 - 27:05]

One is the policy, and the second is this discriminator here.

### [27:05 - 27:12]

And the algorithm I described alternates between updating your skills and updating your discriminator.

### [27:12 - 27:13]

And I want to walk through how this works.

### [27:15 - 27:21]

So the policy optimization looks as follows, for simply applying reinforcement learning

### [27:21 - 27:28]

to this reward function that depends on the discriminator.

### [27:28 - 27:33]

One thing to note here is that when I've written the equation like this, I say we want to learn

### [27:33 - 27:41]

a skill that goes to states where it's easy to guess what behavior is being done at that

### [27:41 - 27:42]

state.

### [27:42 - 27:43]

And.

### [27:43 - 27:44]

This.

### [27:44 - 27:47]

What you're going to hear is this discounted state occupancy measure, this distribution

### [27:47 - 27:49]

over states that you visit.

### [27:49 - 27:54]

So this can equivalently be written as the standard sum of discounted rewards that we're

### [27:54 - 28:00]

used to seeing in reinforcement learning, where reward is the probability assigned to

### [28:00 - 28:02]

this skill.

### [28:02 - 28:08]

So for optimizing the policy, you can apply any reinforcement learning algorithm you want.

### [28:08 - 28:10]

You could apply DQN or PPO.

### [28:10 - 28:12]

Here's your favorite algorithm.

### [28:12 - 28:14]

But for a reward.

### [28:14 - 28:19]

You use this reward here.

### [28:19 - 28:23]

Now the discriminator is trained with maximum likelihood.

### [28:23 - 28:30]

So for example, if the skill representations are discreet, a number 12345, then we're simply

### [28:30 - 28:31]

doing classification.

### [28:31 - 28:36]

The discriminator is going to optimize some standard cross-entropy loss.

### [28:36 - 28:41]

If your skill representations are continuous, then you're simply doing regression, maybe

### [28:41 - 28:43]

minimizing a mean squared error.

### [28:44 - 28:48]

There's a special case here that's sort of fun and fairly widely used in practice, which

### [28:48 - 28:55]

is to think about Z as a normalized vector, a vector that lies on the unit sphere.

### [28:55 - 29:00]

And in this case, you can think about what the discriminator is doing is trying to learn

### [29:00 - 29:06]

a representation of behaviors that's closely aligned with your skill here.

### [29:06 - 29:12]

And so hopefully this gives you some sense of under the hood.

### [29:12 - 29:13]

How did this?

### [29:13 - 29:16]

How does this algorithm actually work?

### [29:16 - 29:21]

One thing to note is that there are several choices for which mutual information you might

### [29:21 - 29:23]

decide to optimize.

### [29:23 - 29:30]

So far, I've been talking about a mutual information between skill representations and entire trajectories.

### [29:30 - 29:35]

And this is really useful when you even care about the order in which states are visited.

### [29:35 - 29:40]

But in practice, we often only care about the frequency with which you visit states,

### [29:40 - 29:42]

not the order in which you visit states.

### [29:42 - 29:43]

And in those settings.

### [29:43 - 29:50]

It's a simpler mutual information that only depends on your state instead of your trajectory.

### [29:50 - 29:56]

You might be tempted to say, well, does including the actions have really improved performance?

### [29:56 - 30:00]

In practice, the answer is no.

### [30:00 - 30:06]

But there are several settings where including your initial state can improve performance.

### [30:06 - 30:11]

And the intuition here is that if you want to describe the space of behaviors, not as

### [30:11 - 30:13]

going to absolute positions.

### [30:13 - 30:19]

But rather as performing a bunch of relative motions or relative behaviors, then a mutual

### [30:19 - 30:25]

information that looks at the change in states starting at your initial state to some current

### [30:25 - 30:28]

state can be highly effective.

### [30:28 - 30:38]

Okay, so this is the objective that's being optimized secretly when you play this game.

### [30:38 - 30:41]

It's worth taking a step back to note for a second that there are several alternative

### [30:41 - 30:43]

ways of learning these skills.

### [30:43 - 30:49]

A lot of prior work has looked at using alternative objectives for measuring the distance between

### [30:49 - 30:56]

two skills, and these methods can be highly effective when you, a user, knows how you

### [30:56 - 30:58]

want to compare the skills in advance.

### [30:58 - 31:04]

There are also methods for learning skills using hierarchical reinforcement learning,

### [31:04 - 31:09]

and this can be most effective in settings where you're given a certain reward function

### [31:09 - 31:10]

and you want to learn a bunch of primitive skills directed towards maximizing your skills.

### [31:10 - 31:11]

But in practice, there's a lot of prior work that's looked at using alternative objectives

### [31:11 - 31:12]

for measuring the distance between two skills, and these methods can be highly effective

### [31:12 - 31:17]

towards maximizing that reward function. Yet hierarchical reinforcement learning methods

### [31:17 - 31:25]

requires that you know this reward function in advance. There are also meta reinforcement

### [31:25 - 31:29]

learning methods, or methods for learning to learn. And these methods can be highly effective

### [31:29 - 31:35]

if I tell you in advance, here are 20 behaviors, learn how to solve these 20 behaviors, or learn

### [31:35 - 31:40]

how to quickly solve these 20 behaviors. But again, this requires knowing these rewards in

### [31:40 - 31:45]

advance. So one of the benefits of looking at mutual information is that allows us to

### [31:45 - 31:56]

learn behaviors before any rewards have been given. One other piece of context I want to

### [31:56 - 32:00]

provide here is that there's a really close connection between these skill learning methods

### [32:00 - 32:06]

and rich prior work on empowerment. So empowerment is this classic idea in reinforcement learning,

### [32:06 - 32:10]

thinking about the mutual information between

### [32:10 - 32:10]

the action,

### [32:10 - 32:17]

that you take now and the states that you visit in the future. The idea of empowerment maximization

### [32:17 - 32:22]

is that you want to take actions that exert a high degree of influence over your futures.

### [32:24 - 32:29]

Now we can think about these skill learning methods as a sort of hierarchical form

### [32:29 - 32:36]

of empowerment in the sense that we want to learn skills so that the skill representation

### [32:36 - 32:40]

Zed exerts a high degree of influence over the future states.

### [32:41 - 32:48]

Whereas before we were thinking about, whereas empowerment thinks about taking actions that exert

### [32:48 - 32:53]

influence, now we're thinking about choosing skills that exert a high degree of influence.

### [32:53 - 32:58]

So you can think about these skills really as a sort of temporally abstracted action.

### [33:01 - 33:05]

And one way of reinterpreting what these skill learning methods are doing

### [33:05 - 33:09]

is that they're trying to learn skills so that if you randomly select

### [33:09 - 33:14]

these Zed's, this corresponds to having a very empowered policy.

### [33:16 - 33:22]

And you can imagine that if selecting these Zed's randomly gives you highly empowered behavior,

### [33:22 - 33:25]

this gives you a strong starting point for being able to quickly solve new tasks.

### [33:28 - 33:32]

Okay, so zooming out for a moment, the overarching goal of this tutorial is to figure out

### [33:32 - 33:39]

how do we compress this enormous space of behaviors so that we can search over it more easily. And now we,

### [33:39 - 33:44]

we have an algorithm for doing this, as well as the mathematical theory for describing

### [33:44 - 33:50]

what this algorithm is doing. But at the end of the day, what we care about is not just learning

### [33:50 - 33:56]

cool behaviors, but actually using these behaviors to quickly solve new tasks. And so I now want to

### [33:56 - 34:01]

talk about relating these skills to reward maximization. I'll start by talking about,

### [34:01 - 34:06]

in practice, how is this done? How are a wide variety of fireworks doing this? And then I'll

### [34:06 - 34:09]

talk a little bit about, um, some theoretical connections between the.

### [34:09 - 34:12]

Skills and maximizing downstream rewards.

### [34:14 - 34:20]

Okay. So I'm going to talk about three primary methods for using skills to solve downstream

### [34:20 - 34:26]

tasks. The first approach is the easiest, which is after you've learned this big library of skills,

### [34:26 - 34:32]

you can simply use one of these skills for solving, um, as your solution to a new

### [34:32 - 34:38]

reinforcement learning problem. So let's say that you have this, uh, quadrupedal ant here.

### [34:39 - 34:45]

And you've learned a couple of different skills. Me, the user there can simply change,

### [34:46 - 34:50]

tune this knob to different values and see which of these behaviors I like the most.

### [34:52 - 34:54]

I'll take the behavior I like the most and use that as my solution.

### [35:01 - 35:07]

Um, one of my favorite applications of this is to the game Montezuma's Revenge. This is work done in

### [35:07 - 35:09]

2018 out of DeepMind. Um, I'm going to talk a little bit about this. I'm going to talk a little bit about this.

### [35:09 - 35:15]

And what they were looking at is learning an enormous space of behaviors and then using

### [35:15 - 35:22]

them to control this little character up here. In this game, there are various ladders that

### [35:22 - 35:27]

you can climb. Uh, there's a rope that you can go up and down. And Montezuma's Revenge

### [35:27 - 35:30]

is considered one of the very difficult exploration benchmarks in the field.

### [35:33 - 35:39]

Now, one of the cool things about how this prior, uh, how this method was learning these skills,

### [35:39 - 35:46]

is that they were using the actual images from the environment as the description of the behavior.

### [35:46 - 35:52]

So their Z, their skill representation was an image itself. And so what I'm showing you here

### [35:52 - 35:58]

in this really blurry image is superimposing the current state of the world with this goal state.

### [35:59 - 36:03]

And so you can see if you only need to focus on this red blob here,

### [36:03 - 36:09]

that's where the character currently is. And this darker blob here is the character's goal location.

### [36:09 - 36:16]

And so I'm now going to, uh, show you a couple of behaviors, where the,

### [36:17 - 36:22]

of different skills that have been learned. So here's another behavior corresponding

### [36:22 - 36:26]

to jumping over here. Here's another behavior for getting over here.

### [36:29 - 36:30]

Another behavior for jumping up there.

### [36:33 - 36:37]

And one thing to note is that all of these behaviors are learned from scratch with no

### [36:37 - 36:39]

reward functions with no reward functions.

### [36:39 - 36:46]

demonstrations. And you can imagine how having a library of behaviors like this might enable you

### [36:46 - 36:52]

to solve a game like this much more rapidly. Okay, so this was the first approach for using

### [36:52 - 36:58]

skills to solve downstream tasks, but I guess taking one of these skills and directly using it.

### [36:59 - 37:03]

But there's another set of approaches for using the skills, which is to think about

### [37:03 - 37:09]

combining or sequencing these skills. For example, let's say that we've learned skills for

### [37:09 - 37:15]

walking forwards and jumping. Now, if I want to solve some hurdling task,

### [37:16 - 37:20]

I can't directly use one of these skills to solve the hurdling task,

### [37:21 - 37:24]

but I can solve the hurdling task by alternating between

### [37:24 - 37:30]

walking and then jumping, and then walking and then jumping. And here's what that looks like.

### [37:39 - 37:39]

One way of thinking about this is to think about a game like this.

### [37:39 - 37:42]

And one way of thinking about this is that throughout the course of one episode,

### [37:43 - 37:49]

I'm tuning the style, this knob of skills. So first I tune it to one behavior for a little bit,

### [37:49 - 37:53]

and then another behavior for a little bit, then another behavior for a little bit.

### [37:53 - 37:56]

And you can use corresponds to a different skill representation.

### [37:58 - 38:02]

This can be done in advance. I can say, okay, I'm going to do skill one, then skill two,

### [38:02 - 38:08]

then skill three. It also can be done in a reactive or closed loop fashion where you learn

### [38:08 - 38:09]

a policy that you're going to use to solve a game. And then you can use it to solve a game that you're

### [38:09 - 38:13]

going to use to solve a policy that selects the skills given your current state.

### [38:14 - 38:19]

So this is now another reinforcement learning problem where you treat each of your skills

### [38:19 - 38:25]

as a temporally abstracted action. And because each of these skills is executed for maybe

### [38:25 - 38:31]

10 or 100 time steps, this dramatically shrinks the horizon of your task.

### [38:35 - 38:39]

And one of my favorite examples of this is this paper back from 2019 that looked at sequencing

### [38:39 - 38:44]

behaviors to get this humanoid robot to run through a sequence of waypoints here.

### [38:45 - 38:47]

Each of these waypoints corresponds to a different skill.

### [38:56 - 38:59]

And one more example of how these skills can be sequenced together

### [38:59 - 39:04]

is in this bimanual manipulation task from a lab out of USC.

### [39:05 - 39:09]

If you, these, what happened here is at first, the skills were sequenced together.

### [39:09 - 39:12]

The first set of skills was learned for these self-supervised skill learning methods.

### [39:14 - 39:18]

And then they learned a high-level policy to sequence these skills.

### [39:19 - 39:21]

And they were effectively able to solve tasks like this.

### [39:22 - 39:27]

And note that if you don't learn skills and you directly try to solve tasks like this

### [39:27 - 39:32]

from scratch, the exploration problem and the long horizon reasoning problem

### [39:32 - 39:34]

are too difficult to make any progress.

### [39:34 - 39:34]

Okay.

### [39:34 - 39:37]

So these methods for sequencing behaviors,

### [39:37 - 39:37]

these methods for sequencing behaviors,

### [39:37 - 39:41]

methods for sequencing skills are probably the most common way that people use skills

### [39:41 - 39:43]

for solving downstream tasks.

### [39:43 - 39:45]

But there's a third approach that I want to briefly mention,

### [39:46 - 39:49]

which is using skills as a way of practicing.

### [39:50 - 39:52]

This can take a couple of different forms.

### [39:52 - 39:55]

One form is for meta reinforcement learning.

### [39:55 - 40:02]

I mentioned earlier that one way that people have learned skills and an alternative way

### [40:02 - 40:06]

of learning skills is to first define a set of tasks and then learn how to quickly adapt

### [40:06 - 40:07]

to these tasks.

### [40:07 - 40:15]

One way of using these skills is to provide a way of automatically generating tasks that

### [40:15 - 40:16]

you can use for practicing.

### [40:16 - 40:22]

Another way that these skills have been used is in multi-agent settings.

### [40:22 - 40:29]

One of the key challenges in multi-agent reinforcement learning is learning how to

### [40:29 - 40:31]

adapt or cooperate with different opponents.

### [40:31 - 40:37]

And you can use these skills to automatically synthesize many different behaviors.

### [40:37 - 40:41]

And so you can practice playing with these different sorts of players.

### [40:41 - 40:45]

Quick show of hands, who has played the game Hanabi before?

### [40:45 - 40:47]

Great.

### [40:47 - 40:48]

Everyone else raise your hand.

### [40:49 - 40:51]

You are going to learn how to play Hanabi.

### [40:51 - 40:52]

It's an amazing game.

### [40:53 - 40:56]

And for folks that have played Hanabi before,

### [40:56 - 40:58]

you probably recognize that playing with your friends,

### [40:58 - 41:00]

with people you've played with,

### [41:00 - 41:02]

is way easier than playing with a stranger,

### [41:03 - 41:04]

even an expert stranger.

### [41:06 - 41:07]

And so this goal of being able to play with your friends,

### [41:07 - 41:12]

being able to cooperate with different players that you're cooperating with,

### [41:12 - 41:13]

is really, really hard.

### [41:13 - 41:17]

And I think that these skills can provide an effective way of practicing,

### [41:17 - 41:22]

how do I adapt to different sorts of players that I'm cooperating with?

### [41:24 - 41:25]

OK.

### [41:25 - 41:29]

So practically, there are these three primary ways that we can use skills

### [41:29 - 41:33]

for solving downstream tasks, for rapidly maximizing rewards.

### [41:34 - 41:36]

But you might be wondering, theoretically,

### [41:36 - 41:38]

is there anything we can say?

### [41:38 - 41:41]

Are these skills, are they all real?

### [41:41 - 41:43]

Do you have any guarantees that they're going to be useful?

### [41:43 - 41:44]

Is this just wishful thinking?

### [41:47 - 41:52]

And thinking about this requires formally defining what we mean by optimal.

### [41:53 - 41:57]

Perhaps the most natural notion of optimality is that these skills,

### [41:57 - 42:00]

we've learned skills for every possible behavior.

### [42:02 - 42:06]

But I don't think this is actually a particularly effective way of thinking about what it means

### [42:06 - 42:12]

for skills to be optimal, because an untrained policy would be optimal in this sense.

### [42:13 - 42:15]

What I mean is that if you have a policy with a set of weights,

### [42:16 - 42:19]

or if you have a neural network with a set of weights,

### [42:19 - 42:22]

you can set these weights to whatever you want to induce any sort of behavior.

### [42:23 - 42:26]

But if you directly think about searching in the space of weights,

### [42:27 - 42:29]

the search problem is going to be way too hard.

### [42:29 - 42:32]

You may have millions and millions of weights that you have to search over.

### [42:32 - 42:35]

It's like saying, if I give you a million knobs,

### [42:35 - 42:37]

you can define any behavior that you want.

### [42:37 - 42:41]

But how can you possibly find the right configuration of a million knobs?

### [42:43 - 42:48]

So I think that the right notion of optimality is one that thinks about,

### [42:49 - 42:51]

how do we adapt to new tasks?

### [42:51 - 42:53]

How do we quickly learn new tasks?

### [42:56 - 43:00]

So in the next couple of slides, I want to walk through a sense in which these skills

### [43:00 - 43:04]

are provably optimal for adapting to new tasks under some assumptions.

### [43:06 - 43:11]

And to do this, we're going to think about skills not as some sort of animated behavior,

### [43:11 - 43:14]

but rather as skills as a distribution over states

### [43:14 - 43:19]

defined using the same discounted state occupancy measure we looked at before.

### [43:21 - 43:26]

So as a running example, I want you to think about a three-state MDP.

### [43:26 - 43:31]

And so every skill corresponds to visiting a certain distribution over these three states.

### [43:31 - 43:33]

State one, state two, state three.

### [43:33 - 43:38]

Probability distributions are positive, they integrate to one.

### [43:38 - 43:45]

And so we can think about this set of probability distributions as lying on a triangle,

### [43:45 - 43:47]

sometimes called the probability simplex.

### [43:48 - 43:54]

And so one skill might correspond to visiting state one pretty frequently,

### [43:54 - 43:57]

and state three pretty frequently, and never visiting state two.

### [43:57 - 44:02]

Another skill might correspond to visiting each of these three states with roughly equal frequency.

### [44:02 - 44:03]

So we're going to think about a three-state MDP,

### [44:03 - 44:10]

and one thing to note is that there are some limits on the state distributions

### [44:10 - 44:12]

that is possible to visit.

### [44:12 - 44:15]

I cannot spend 100% of my time in midair.

### [44:15 - 44:21]

I can spend at most 20% of my time in midair because of constraints imposed by physics.

### [44:22 - 44:29]

And so this region here defines the set of state visitation distributions that are actually

### [44:29 - 44:32]

possible because of the physics, because of the dynamics.

### [44:33 - 44:38]

And formally, we might refer to this polygon here as the state marginal polytope.

### [44:40 - 44:43]

And one reason why I like this image is that it allows us to think about

### [44:43 - 44:47]

learning skills as throwing darts into this orange region.

### [44:48 - 44:52]

When we're learning the skills, we want to know where are the darts going to land?

### [44:53 - 44:54]

Or where are the skills going to land?

### [44:54 - 44:55]

Are they going to be on the inside?

### [44:55 - 44:56]

Are they going to be on the corners?

### [44:56 - 44:58]

Are they going to be on the edges?

### [44:58 - 45:02]

This provides a geometric picture of what these skill learning methods do.

### [45:03 - 45:05]

In the case of information technology, on these ridges,

### [45:05 - 45:07]

and we had mulheres be seen on the edge,

### [45:07 - 45:11]

and which could be in different parts of the labor climate chance at higher risk.

### [45:12 - 45:15]

So to start, we can think about what a standard reward maximization did.

### [45:16 - 45:19]

Reward maximization we can think about as

### [45:19 - 45:23]

trying to learn a policy so that your expected return is high.

### [45:23 - 45:27]

That corresponds to looking at the probability of visiting each of these three states

### [45:27 - 45:30]

times the reward of visiting each of these three states.

### [45:31 - 45:33]

We actually can think about the reward here as a vector.

### [45:33 - 45:35]

would have a state visitation distribution

### [45:35 - 45:37]

at this corner here, saying you're

### [45:37 - 45:40]

going to try to spend as much time as possible

### [45:40 - 45:42]

at this state here and as little time as possible

### [45:42 - 45:44]

at this state and the state down here.

### [45:47 - 45:49]

And so based on this picture, you

### [45:49 - 45:54]

can reason that the solutions to any reward maximization

### [45:54 - 46:00]

problem, they're always going to lie at vertices of this poly

### [46:00 - 46:02]

token.

### [46:02 - 46:05]

And so one way of thinking about whether a skill learning

### [46:05 - 46:08]

method is optimal or not is by thinking about, well,

### [46:08 - 46:10]

are the skills lying at vertices?

### [46:10 - 46:14]

Are they going to lie at every vertice?

### [46:14 - 46:16]

And what you can prove is that the skills learned

### [46:16 - 46:18]

by skill learning methods, they always

### [46:18 - 46:21]

lie at vertices, meaning that every skill you learn

### [46:21 - 46:23]

is going to be optimal for some reward function.

### [46:26 - 46:27]

But it turns out that they're going

### [46:27 - 46:29]

to be some reward functions where you don't learn

### [46:29 - 46:30]

any skill.

### [46:30 - 46:33]

They're going to be skills.

### [46:33 - 46:35]

But there are alternative methods

### [46:35 - 46:40]

for learning how to uncover every vertice.

### [46:40 - 46:42]

And so the general patterns here are that skills end up

### [46:42 - 46:44]

lying at vertices, which means every skill

### [46:44 - 46:48]

is optimal for some downstream reward function.

### [46:48 - 46:52]

But there's a limit on how many distinct skills you'll learn.

### [46:52 - 46:55]

And so this motivates some of those alternative methods

### [46:55 - 46:57]

for using the skills, like just sequencing them.

### [46:57 - 47:01]

Now, this simply says, are your skills

### [47:01 - 47:04]

optimal for solving certain reward functions?

### [47:04 - 47:08]

But they don't say anything about the speed of adaptation.

### [47:08 - 47:11]

And so I now want to talk a little bit

### [47:11 - 47:13]

about the speed of adaptation.

### [47:22 - 47:25]

And so, I've got a really interesting question,

### [47:25 - 47:26]

and one I think is really interesting.

### [47:26 - 47:27]

And it's, I'm going to go ahead and read it.

### [47:27 - 47:30]

So when we're thinking about these skill learning methods,

### [47:30 - 47:33]

we can think about them as learning

### [47:33 - 47:36]

several different vertices on this polytope.

### [47:36 - 47:39]

And we can think about, on average,

### [47:39 - 47:44]

where does this average of the skills end up lying?

### [47:44 - 47:46]

And you can think about the difficulty

### [47:46 - 47:48]

of solving a new problem as the distance

### [47:48 - 47:53]

between this average of skills to the furthest vertex.

### [47:53 - 47:55]

Recall that the solution that you're trying to find

### [47:55 - 47:58]

is always going to be at one of these vertices.

### [47:58 - 48:00]

Formally, we will measure distances

### [48:00 - 48:02]

using a KL divergence.

### [48:02 - 48:06]

And it turns out you can prove that maximizing

### [48:06 - 48:09]

mutual information corresponds to finding

### [48:09 - 48:12]

this average of skills that's as close as possible

### [48:12 - 48:15]

to the furthest vertex.

### [48:15 - 48:18]

This is analogous to saying, if you have a big city,

### [48:18 - 48:20]

where do you put the fire department

### [48:20 - 48:23]

so that the fire engines can get to any point in the city

### [48:23 - 48:25]

with minimal distance?

### [48:25 - 48:30]

And it turns out that optimization here

### [48:30 - 48:33]

corresponds to picking out those points in the city that

### [48:33 - 48:36]

take the longest to visit.

### [48:36 - 48:39]

And why this is useful is that it suggests that when we're

### [48:39 - 48:42]

learning these skills, what we end up doing

### [48:42 - 48:46]

is we're finding an average distribution over states

### [48:46 - 48:49]

that's not a uniform distribution over states,

### [48:49 - 48:53]

but rather that minimizes the number of time steps

### [48:53 - 48:54]

it takes to find the furthest vertex.

### [48:54 - 48:55]

OK?

### [48:55 - 49:00]

It takes to reach the furthest vertex, the number of time

### [49:00 - 49:02]

steps it would take to maximize the most difficult reward

### [49:02 - 49:05]

function.

### [49:05 - 49:06]

And so what this analysis does is

### [49:06 - 49:10]

it provides a formal connection between learning these skills

### [49:10 - 49:13]

and solving new tasks quickly.

### [49:13 - 49:16]

Analysis like this always rests on certain assumptions.

### [49:16 - 49:18]

And so there are definitely some gaps still

### [49:18 - 49:21]

to be made between the theory here and the results

### [49:21 - 49:23]

that we see in practice.

### [49:25 - 49:27]

OK.

### [49:27 - 49:28]

So the overarching goal for today

### [49:28 - 49:31]

was to figure out, how do we discover

### [49:31 - 49:33]

this enormous space of behaviors?

### [49:33 - 49:35]

And then how do we compress it and represent it

### [49:35 - 49:38]

so we can quickly solve new tasks?

### [49:38 - 49:40]

And in the last couple of minutes here,

### [49:40 - 49:41]

I want to talk a little bit about what

### [49:41 - 49:44]

I see as the next frontier of skill learning methods.

### [49:47 - 49:50]

To start, I want to think about this compression perspective

### [49:50 - 49:55]

on machine learning to try to motivate, why should we

### [49:55 - 49:59]

care about skills at all in this era of big foundation models?

### [49:59 - 50:03]

Can I just go ask chat QPT to solve my problem for me?

### [50:03 - 50:06]

Well, I think what these big foundation models are doing

### [50:06 - 50:07]

is they're doing compression.

### [50:07 - 50:09]

You can formally show that maximum likelihood corresponds

### [50:09 - 50:10]

to compression.

### [50:10 - 50:12]

They're trying to look at a big data set,

### [50:12 - 50:14]

like this data set of images, and trying

### [50:14 - 50:17]

to find patterns in those images.

### [50:17 - 50:19]

And language models are doing something similar.

### [50:19 - 50:24]

They're looking at these big corpora, purposes of text,

### [50:24 - 50:24]

and trying to figure out.

### [50:24 - 50:24]

OK.

### [50:24 - 50:24]

OK.

### [50:24 - 50:25]

OK.

### [50:25 - 50:29]

How do you compress all of this text?

### [50:29 - 50:31]

And we can think about reinforcement learning

### [50:31 - 50:33]

as doing something similar, trying

### [50:33 - 50:36]

to take this big space of behaviors

### [50:36 - 50:39]

and compress it into some similar foundation model,

### [50:39 - 50:42]

or what we might call a behavioral foundation model.

### [50:42 - 50:45]

But there's a key difference here,

### [50:45 - 50:47]

which is that this set of all behaviors

### [50:47 - 50:51]

is not provided as an input to the learning algorithm,

### [50:51 - 50:53]

but rather it has to be discovered.

### [50:54 - 50:58]

So you can think about what these skill learning methods

### [50:58 - 51:02]

are doing is really a thing of joint optimization.

### [51:02 - 51:05]

They are simultaneously trying to discover

### [51:05 - 51:08]

the set of behaviors while also trying to compress

### [51:08 - 51:11]

this set of behaviors.

### [51:11 - 51:13]

And one of the reasons why I think this perspective is

### [51:13 - 51:17]

useful is that data is a huge bottleneck today

### [51:17 - 51:19]

in training big AI models.

### [51:19 - 51:21]

We've trained on, effectively, the entire internet

### [51:21 - 51:23]

of images and the entire internet of text.

### [51:23 - 51:25]

We've run out of data.

### [51:25 - 51:28]

But if we have AI systems, maybe reinforcement learning systems,

### [51:28 - 51:30]

that can generate their own data,

### [51:30 - 51:33]

this gives a way of automatically generating

### [51:33 - 51:37]

lots and lots of new data.

### [51:37 - 51:39]

One other salient difference that I want to highlight here

### [51:39 - 51:43]

is that the reinforcement learning models are really

### [51:43 - 51:45]

thinking about interaction.

### [51:45 - 51:48]

If we want to, if the key benefits of reinforcement

### [51:48 - 51:51]

learning are going to be about exploring and discovering

### [51:51 - 51:53]

new behaviors, then it makes sense that when

### [51:53 - 51:56]

we're doing free training for reinforcement learning,

### [51:56 - 51:59]

it involves automatically discovering

### [51:59 - 52:00]

the set of behaviors.

### [52:00 - 52:02]

It involves exploration.

### [52:06 - 52:08]

But as we think about learning all of these behaviors,

### [52:08 - 52:10]

I think the current set of algorithms

### [52:10 - 52:13]

we have might not be sufficient because I

### [52:13 - 52:15]

think there's a concept that currently

### [52:15 - 52:16]

deserves a bit more focus.

### [52:16 - 52:20]

And that is thinking about generalization.

### [52:20 - 52:23]

So papers today, when they talk about learning skills, they

### [52:23 - 52:26]

really look at the coverage of states

### [52:26 - 52:29]

that your skills have covered during training.

### [52:29 - 52:31]

And so when, say, you have some robot

### [52:31 - 52:32]

and you want it to run around, you

### [52:32 - 52:34]

might learn skills for running in lots

### [52:34 - 52:35]

of different directions.

### [52:35 - 52:38]

You might put a paper like this, a figure like this in your paper,

### [52:38 - 52:40]

saying, hey, look, my skills are great.

### [52:40 - 52:42]

They've covered the entire state space.

### [52:42 - 52:44]

You can count how many different states

### [52:44 - 52:45]

they have visited during training.

### [52:50 - 52:53]

One thing to note is that in other areas of machine learning,

### [52:53 - 52:56]

we don't actually have to train on literally

### [52:56 - 52:59]

every possible example.

### [52:59 - 53:01]

In other areas of machine learning,

### [53:01 - 53:04]

I can hold out some of the training data,

### [53:04 - 53:08]

and the models will still make good predictions.

### [53:08 - 53:10]

So how could I develop something like that for these skill

### [53:10 - 53:12]

learning methods?

### [53:12 - 53:15]

How could I learn skills that enable

### [53:15 - 53:21]

me to do lots of things, even if I haven't practiced doing them?

### [53:21 - 53:23]

For example, imagine I want to build

### [53:23 - 53:25]

some reinforcement learning agent for cooking.

### [53:25 - 53:26]

There are lots of different skills

### [53:26 - 53:28]

that that agent might need to practice.

### [53:28 - 53:32]

It might need to learn how to make soups and salads and chicken.

### [53:32 - 53:34]

But at some point, you've practiced enough,

### [53:34 - 53:36]

and now you have the requisite skills

### [53:36 - 53:39]

to go on and make a whole number of other dishes,

### [53:39 - 53:43]

including many dishes that you haven't made before.

### [53:43 - 53:44]

We know that this sort of generalization

### [53:44 - 53:47]

is possible in other areas of machine learning.

### [53:47 - 53:50]

Language models can prove sentences and paragraphs

### [53:50 - 53:52]

that are very different than those seen in the training

### [53:52 - 53:52]

data.

### [53:52 - 53:53]

So how do we do that?

### [53:53 - 53:55]

Well, first of all, we need to know

### [53:55 - 53:56]

the training data.

### [53:56 - 53:59]

Big generative image models are very good at generating images

### [53:59 - 54:02]

like astronauts riding a horse on the moon that have never

### [54:02 - 54:04]

been seen in the training data.

### [54:04 - 54:06]

And so it seems plausible that there

### [54:06 - 54:09]

is some yet-to-be-invented skill learning algorithm that

### [54:09 - 54:13]

might exhibit similar generalization properties.

### [54:13 - 54:15]

I guess to ground this a little bit to give you

### [54:15 - 54:18]

a sense of why it's not so crazy,

### [54:18 - 54:20]

I flew here from New York City.

### [54:20 - 54:22]

If you look at New York City as a big grid,

### [54:22 - 54:25]

there are 17 paths from one corner of New York City

### [54:25 - 54:27]

to the other corner of New York City.

### [54:27 - 54:30]

No one has ever taken every possible path from one corner

### [54:30 - 54:32]

of the city to the other.

### [54:32 - 54:34]

But most people living in New York City

### [54:34 - 54:36]

can navigate effectively.

### [54:36 - 54:38]

Navigating in New York City is actually really easy

### [54:38 - 54:41]

because the streets are all numbered.

### [54:41 - 54:43]

And so you could learn.

### [54:43 - 54:46]

In theory, we know that it's possible to learn skills

### [54:46 - 54:48]

that would allow you to express the 10

### [54:48 - 54:51]

to the 17 different behaviors even without practicing

### [54:51 - 54:56]

all 10 to the 17 behaviors.

### [54:56 - 54:58]

Another concern you might have is, well,

### [54:58 - 55:00]

that's a large number of behaviors.

### [55:00 - 55:02]

10 to the 17 is a big number.

### [55:02 - 55:04]

But it turns out that vectors are very

### [55:04 - 55:06]

good at expressing big numbers.

### [55:06 - 55:10]

Even if you represent skills with a binary vector,

### [55:10 - 55:13]

you can represent as many skills as there

### [55:13 - 55:17]

are grains of sand on Earth with a vector that's only length 60.

### [55:17 - 55:20]

And so the representation problem, I think,

### [55:20 - 55:23]

is also fairly solvable.

### [55:23 - 55:25]

In addition to developing algorithms that

### [55:25 - 55:28]

enable us to generalization, I think that one component

### [55:28 - 55:30]

that I would also like to see more research on

### [55:30 - 55:33]

is thinking about simulation and digital twins.

### [55:33 - 55:36]

I think this is important both for driving advances

### [55:36 - 55:37]

in the field.

### [55:37 - 55:39]

I think we need higher fidelity simulators,

### [55:39 - 55:42]

but also simulators that allow us to really focus

### [55:42 - 55:44]

on the problems that we as a community think

### [55:44 - 55:46]

are the most important problems.

### [55:46 - 55:49]

Maybe simulated robotics isn't the most important application.

### [55:49 - 55:50]

I don't know.

### [55:50 - 55:51]

I don't know.

### [55:51 - 55:53]

I don't know.

### [55:53 - 55:56]

So what does success look like?

### [55:56 - 55:59]

I want to leave you by thinking about an agent that

### [55:59 - 56:01]

can build sandcastles.

### [56:01 - 56:05]

The design of a sandcastle might be encoded in a vector.

### [56:05 - 56:09]

This is similar to how a picture can be encoded in a vector.

### [56:09 - 56:11]

But this skill vector is now going

### [56:11 - 56:15]

to be decoded by interacting with the environment.

### [56:15 - 56:17]

This robot, let's say, is going to interact

### [56:17 - 56:19]

with the sand maybe for dozens of hours

### [56:19 - 56:23]

until it eventually builds a sandcastle like this.

### [56:23 - 56:26]

Being able to build sandcastles like this

### [56:26 - 56:29]

is going to require practice of different sorts of skills,

### [56:29 - 56:32]

maybe practicing building a sandcastle like this

### [56:32 - 56:34]

and another one like this.

### [56:34 - 56:37]

But you certainly don't have to build every possible sandcastle

### [56:37 - 56:40]

to have the skills to be able to build lots

### [56:40 - 56:43]

of different types of sandcastles.

### [56:43 - 56:46]

And we can think about similar things in the virtual world.

### [56:46 - 56:48]

You can describe virtual worlds by a vector.

### [56:48 - 56:52]

And then agents decode those vectors

### [56:52 - 56:56]

by interacting with the world to build it.

### [56:56 - 56:59]

I think the capacity to explore this big space of behaviors

### [56:59 - 57:02]

and to organize it remains a fundamental open problem

### [57:02 - 57:06]

in reinforcement learning and even perhaps AI.

### [57:06 - 57:08]

But figuring out how to do this I think

### [57:08 - 57:10]

will allow us to use reinforcement learning

### [57:10 - 57:12]

methods to tackle problems that require

### [57:12 - 57:15]

really long horizon reasoning and problems

### [57:15 - 57:18]

that we humans don't even know how to solve today.

### [57:18 - 57:23]

I think the current generation of today's current generative models,

### [57:23 - 57:26]

they're really good at painting pixels on a screen.

### [57:26 - 57:30]

They're really good at painting tokens on a screen.

### [57:30 - 57:32]

But I think tomorrow's generative models

### [57:32 - 57:34]

built with reinforcement learning methods,

### [57:34 - 57:37]

they might be able to actually build this world

### [57:37 - 57:41]

that today's generative models can only paint pictures of.

### [57:41 - 57:43]

And I think that these self-supervised techniques

### [57:43 - 57:47]

might be an important technique for enabling this.

### [57:48 - 57:53]

So I'm going to end there.

### [57:53 - 57:57]

A huge thank you to all of my students and collaborators

### [57:57 - 58:03]

who have contributed to some of the work I talked about today.

### [58:03 - 58:05]

There is a link to a website where

### [58:05 - 58:07]

I have an enormous list of references

### [58:07 - 58:10]

of all of the huge body of work that's

### [58:10 - 58:13]

been done in this really exciting area.

### [58:13 - 58:14]

The slides are live.

### [58:14 - 58:16]

The full list of references in the written version

### [58:16 - 58:18]

of the tutorial will be posted.

### [58:18 - 58:21]

Within the rest of the week.

### [58:21 - 58:23]

One thing to note is that I am sure

### [58:23 - 58:26]

I've missed some important prior work in this area.

### [58:26 - 58:27]

This area is huge.

### [58:27 - 58:30]

And I can't possibly cover it in 60, 70 minutes.

### [58:30 - 58:32]

And so please come talk to me.

### [58:32 - 58:33]

Shoot me an email.

### [58:33 - 58:34]

Let me know things I've missed.

### [58:34 - 58:37]

I'd love to learn more about perspectives

### [58:37 - 58:42]

that I have accidentally omitted.

### [58:42 - 58:44]

And I'm happy to take questions at this point.
