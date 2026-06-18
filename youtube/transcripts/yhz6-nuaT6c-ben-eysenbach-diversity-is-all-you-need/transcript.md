# Ben Eysenbach Diversity is All You Need

- URL: https://www.youtube.com/watch?v=yhz6-nuaT6c
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T15:06:47`

## Transcript

### [00:00 - 00:17]

Excellent. Okay. So thanks so much for having me here today. I'm really excited to talk about some of this work. So the title of the talk is Diversity is All You Need, Learning Skills Without a Reward Function. And this is joint work with a number of collaborators, including Shane Gu, Abhishek Gupta, Juliet Yerbaaz, and Sergey Levin.

### [00:19 - 00:27]

And if you have any questions during the talk, please feel free to stop me and ask questions. The point of this is not so I can talk, but so that you can learn cool things.

### [00:27 - 00:37]

Okay. So to start before talking about what we actually do in this paper, I want to talk about some of the challenges that face reinforcement learning today.

### [00:37 - 00:50]

And a lot of these challenges revolve around human supervision. That is, when we want to get, when we want to deploy reinforcement learning algorithms, what often stops us is not technical problems, but problems that have to do with relying on humans.

### [00:50 - 00:55]

We do this in a number of ways. For example, we rely on humans to design reward functions.

### [00:55 - 01:07]

We somehow expect that humans will be able to say, okay, this is what I want the robot to do. And to do that, here's some really complicated mathematical expression of corresponding to these are good states and these are bad states.

### [01:07 - 01:09]

And in practice, this is really hard to define.

### [01:11 - 01:25]

A second challenge is designing skills. Especially when we want robots or other autonomous agents to solve temporally extended tasks, it's often useful to be able to break down those tasks into a series of simpler tasks.

### [01:25 - 01:32]

But automatically learning these tasks is often quite challenging. And that will actually be the main focus of today's talk.

### [01:34 - 01:45]

A third challenge is tuning hyperparameters. Despite reinforcement learning algorithms being much more stable today than they were, say, five years ago, they still depend heavily on a number of really critical hyperparameters.

### [01:45 - 01:51]

And tuning those parameters often relies on just human ingenuity, which is sort of annoying.

### [01:54 - 01:55]

Resetting.

### [01:55 - 01:57]

This is an issue that often gets overlooked.

### [01:57 - 02:05]

When we have something like a robot deployed in the real world, we often segment its training into a sequence of episodes.

### [02:05 - 02:11]

And at the end of every episode, we assume that the robot is magically reset back to some initial state.

### [02:11 - 02:19]

And for things like video games, this is a perfectly reasonable thing to do. You can just reset all the bits in the game back to some initial state.

### [02:19 - 02:24]

But for things like robots or self-driving cars or chemical plants, resetting the state is often quite challenging.

### [02:24 - 02:28]

You often have to have some human operator come in and rearrange everything.

### [02:28 - 02:35]

I'm not going to talk about this in this talk, but it's one important challenge that I want to see more work on in the future.

### [02:35 - 02:42]

And the last two challenges are safety, we don't want robots to break themselves, and curriculum learning.

### [02:42 - 02:46]

For really complicated tasks, it's often nearly impossible to solve them in a single shot.

### [02:46 - 02:53]

And so insofar as we can break down those tasks into a sequence of easier tasks, then it might be easier to solve them.

### [02:53 - 02:59]

And so today's talk, as I alluded to before, is going to focus mostly on learning useful skills.

### [02:59 - 03:08]

Before we actually dive into what skills are, one of the reasons that skills will be useful is that they'll actually help us solve a number of these other problems.

### [03:08 - 03:14]

They'll help us make progress on things like designing reward functions, hyperparameter tuning, and curriculum learning.

### [03:14 - 03:17]

OK, so what do we mean by a skill?

### [03:17 - 03:22]

So a skill fundamentally is some behavior that some autonomous agent can do.

### [03:23 - 03:27]

And ultimately, what defines a skill depends on the environment you're in.

### [03:27 - 03:36]

So if you look at this quadruped robot right here, skills might correspond to walking forward or walking backwards, crouching down or jumping up.

### [03:36 - 03:39]

But for a different robot, you might get different sorts of skills.

### [03:39 - 03:46]

For example, for this arm robot, skills may correspond to throwing or stacking or sorting objects.

### [03:46 - 03:50]

And in both of these examples, it's pretty clear what different skills would be.

### [03:50 - 03:53]

You and I can sit down and write down what a set of rules are.

### [03:53 - 03:56]

And that's what a set of reasonable skills would be.

### [03:56 - 04:05]

Now, one of the interesting things about learning skills is that they might also help us understand what are the capabilities of a robot like this.

### [04:05 - 04:11]

Of a robot that is really hard a priori to know, what is it possible for this robot to do?

### [04:11 - 04:13]

Can this robot roll forward and roll backwards?

### [04:13 - 04:15]

Can this robot jump?

### [04:15 - 04:19]

Can this robot flatten itself like a pancake?

### [04:19 - 04:22]

If we can learn a set of skills that spans the behavior.

### [04:23 - 04:34]

Of the robot, we might be able to figure out and then better understand what robots can do.

### [04:34 - 04:35]

OK.

### [04:35 - 04:37]

So at this point, we've introduced skills.

### [04:37 - 04:39]

Now I want to talk a little bit about what are good skills?

### [04:39 - 04:44]

What makes one skill or some skills better than other skills?

### [04:44 - 04:47]

And there are a couple of things that might make skills useful.

### [04:47 - 04:50]

One is we might want skills that do good exploration.

### [04:50 - 04:52]

That is, we might want different behaviors that go to different parts of the body.

### [04:52 - 04:57]

We might want behaviors that go to different parts of the state space.

### [04:57 - 04:59]

Another thing we might want is predictability.

### [04:59 - 05:05]

That is, if you say I'm executing skill one, we should always be able to know what will skill one do?

### [05:05 - 05:08]

What will be the outcome of executing skill one?

### [05:08 - 05:13]

And this is especially important if we want to compose skills hierarchically.

### [05:13 - 05:18]

That is, if we want to string together some sequence of skills.

### [05:18 - 05:20]

First executing skill one and then executing skill two.

### [05:20 - 05:21]

Because if the means are different.

### [05:21 - 05:27]

Because if the meaning of skills change, if the outcome of executing skills change,

### [05:27 - 05:33]

then it's really hard to know what will happen when I execute skill one and then skill two.

### [05:33 - 05:36]

And then a third property that might be useful is interpretability.

### [05:36 - 05:42]

That is, if you see the robot doing something, if you see that the robot's in some state taking some actions,

### [05:42 - 05:45]

you should be able to infer, OK, oh, that robot's in that state.

### [05:45 - 05:50]

So it must be executing skill seven, for example.

### [05:50 - 05:57]

And what all these properties hint at is that what makes a skill good or bad can't be determined in isolation.

### [05:57 - 06:03]

Rather, what makes a skill good or bad depends on its relationship to other skills.

### [06:03 - 06:08]

And so one of the key ideas of this talk is that instead of learning skills in isolation,

### [06:08 - 06:13]

rather, we're going to focus on learning an entire set of skills.

### [06:13 - 06:19]

And the objective we're going to use for learning the set of skills is that the set, jointly,

### [06:19 - 06:26]

should be as diverse as possible.

### [06:26 - 06:30]

OK, so this is sort of the setup of what we want out of a skill learning algorithm.

### [06:30 - 06:35]

And I'm actually going to present the method we use for learning the set of skills.

### [06:35 - 06:39]

And before presenting it mathematically, I'm going to present it as a game,

### [06:39 - 06:45]

a game that you or I could actually play if this were in person.

### [06:45 - 06:47]

So this game works as follows.

### [06:47 - 06:49]

We have two players standing on our side.

### [06:49 - 06:52]

Either side of, say, a big football field.

### [06:52 - 06:59]

And the goal of the game is for the blue player to communicate some message to the red player.

### [06:59 - 07:01]

And the players can't talk to each other.

### [07:01 - 07:03]

They're too far away.

### [07:03 - 07:08]

And so the only way that the blue player can communicate to the red player is by doing things.

### [07:08 - 07:12]

By, say, standing upright with his hands on the side.

### [07:12 - 07:17]

Or maybe communicate a different message by leaning over to one side.

### [07:17 - 07:22]

Or it could communicate a third message by jumping and kicking.

### [07:22 - 07:24]

Or by holding his leg.

### [07:24 - 07:26]

Or by doing other motions.

### [07:26 - 07:36]

And one of the ideas here is that the blue player, in trying to convey information to the red player on the opposite side of the football field,

### [07:36 - 07:40]

the blue player has to figure out different motions they can do.

### [07:40 - 07:43]

Different motions that are distinguishable from one another.

### [07:43 - 07:47]

Because if the red player can't distinguish one motion from another motion,

### [07:47 - 07:56]

the blue player won't be able to tell what message the blue player is trying to play.

### [07:56 - 08:03]

This game here lies at the core of the algorithm that we proposed.

### [08:03 - 08:07]

I'll explain how that works now.

### [08:07 - 08:11]

So to do that, we need a little bit of mathematical machinery.

### [08:11 - 08:17]

And so we can formally quantify the amount of information that the blue player conveys to the red player.

### [08:17 - 08:19]

As follows.

### [08:19 - 08:22]

So let's say that the blue player is communicating three messages.

### [08:22 - 08:24]

Either A, B, or C.

### [08:24 - 08:27]

And they're going to do that using three actions.

### [08:27 - 08:31]

Leaning over, jumping and kicking, or swaying to one side.

### [08:31 - 08:37]

We can precisely say that the amount of information that the blue player is sending to the red player

### [08:37 - 08:46]

is at least as great as how well the red player can predict what the blue player is doing.

### [08:46 - 08:48]

So you get some intuition for this.

### [08:48 - 08:58]

If the red player can always accurately infer that kicking means code word B,

### [08:58 - 09:01]

then the subjective, this probability is going to be quite large.

### [09:01 - 09:07]

And so that means that the blue player is successfully communicating many bits to the red player.

### [09:07 - 09:15]

If in contrast, the red player is never able to predict what message the blue player is trying to send,

### [09:15 - 09:18]

then this term is going to be quite low.

### [09:18 - 09:26]

And what this bound here highlights is that if we want to maximize information,

### [09:26 - 09:29]

we actually have to care about the performance of both the players.

### [09:29 - 09:34]

We both want the blue player to execute distinguishable behavior.

### [09:34 - 09:44]

We also want the red player to be able to accurately guess what the blue player is trying to do.

### [09:44 - 09:49]

So before we instantiate this inside a reinforcement learning algorithm,

### [09:49 - 09:56]

I want to pause here to see if there are any questions.

### [09:56 - 10:03]

Well, I'm kind of interested still in how you, you know, a step earlier,

### [10:03 - 10:08]

how did you get into that perspective that the diversity of skills

### [10:08 - 10:13]

and like these three requirements are really what matters about skills?

### [10:13 - 10:14]

There.

### [10:14 - 10:18]

Like a little bit of a step before that.

### [10:18 - 10:22]

Like, how did you end up with these three requirements?

### [10:22 - 10:25]

You know, it's a really good point.

### [10:25 - 10:31]

A lot of this just came from looking at what like intuitively what we think useful skills would be.

### [10:31 - 10:35]

And ultimately, we care about learning skills, not for the purpose of learning skills,

### [10:35 - 10:39]

but we learn we care about learning skills because they will help us solve downstream tasks.

### [10:39 - 10:43]

And so one way we can use skills for solving downstream tasks

### [10:43 - 10:45]

is to compose them hierarchically.

### [10:45 - 10:50]

That is, instead of planning at the love-love, say, motor torques or joint angles,

### [10:50 - 10:55]

we can plan at the love-love more abstract behaviors.

### [10:55 - 11:00]

And this requirement that we'd be able to use skills for hierarchical RO

### [11:00 - 11:06]

was one of the motivations for making skills predictable.

### [11:06 - 11:09]

The motivation for exploration is sort of similar.

### [11:09 - 11:12]

That is, if we want to be able to use skills to accelerate learning downstream tasks,

### [11:12 - 11:17]

it would be useful if, when given a reward function in some environment,

### [11:17 - 11:20]

we're able to very quickly explore this environment.

### [11:20 - 11:23]

And that motivates us to have skills explore.

### [11:23 - 11:26]

And one thing that actually makes exploration easier in this setting is that

### [11:26 - 11:31]

we don't need to have a single skill that does good exploration everywhere.

### [11:31 - 11:37]

All we need is that different skills explore different areas.

### [11:37 - 11:39]

And that if there's a certain state you want to get to,

### [11:39 - 11:42]

there's some skill that will get you to that state.

### [11:42 - 11:47]

And so it was this sort of reasoning about how are we eventually going to use skills

### [11:47 - 11:53]

that suggested these properties.

### [11:53 - 11:55]

Yeah, thank you. Makes sense.

### [11:55 - 11:57]

Excellent.

### [11:57 - 11:59]

Any other questions?

### [11:59 - 12:14]

If not, maybe we'll move on.

### [12:14 - 12:16]

OK, so we have this game, this two-player game.

### [12:16 - 12:20]

And to turn this into a reinforcement learning algorithm,

### [12:20 - 12:26]

we're going to basically assign neural networks to the blue player and the red player.

### [12:26 - 12:28]

And I'll explain how that works.

### [12:29 - 12:35]

So the blue player is what we're going to call the skill or the policy.

### [12:35 - 12:42]

And this player takes as input the current state of the world and some Z.

### [12:42 - 12:45]

Z corresponds to the code word A, B, or C,

### [12:45 - 12:49]

or some other object that we discussed before.

### [12:49 - 12:52]

And the skill outputs a sequence of actions.

### [12:52 - 12:55]

The other player, the red player, is the discriminator.

### [12:55 - 12:58]

And the discriminator looks at the state of the world

### [12:58 - 13:06]

and tries to guess what code word is the skill trying to send.

### [13:06 - 13:09]

And both the skill and the discriminator are learned.

### [13:09 - 13:11]

These are learned neural networks.

### [13:11 - 13:15]

And the whole algorithm works as follows.

### [13:15 - 13:17]

At the start of every episode, we sample some code words,

### [13:17 - 13:20]

some Z from a prior distribution.

### [13:20 - 13:23]

And we send that to the skill.

### [13:23 - 13:26]

The skill then interacts with the environment,

### [13:26 - 13:28]

collecting a whole bunch of experience.

### [13:28 - 13:31]

Now, at every time step,

### [13:31 - 13:33]

the discriminator, the red player,

### [13:33 - 13:35]

looks at the state of the world and tries to guess,

### [13:35 - 13:38]

OK, what code word, what Z,

### [13:38 - 13:40]

is the blue player trying to tell me?

### [13:40 - 13:42]

Are they trying to send A or are they trying to send B

### [13:42 - 13:45]

or are they trying to send C?

### [13:45 - 13:49]

And then the most important step is how we update the skill.

### [13:49 - 13:51]

So what we do is we say,

### [13:51 - 13:54]

if the discriminator was able to successfully guess

### [13:54 - 13:57]

what code word the skill was trying to send,

### [13:58 - 14:01]

then we should give the skill some high reward.

### [14:01 - 14:05]

If the discriminator failed to guess what code word

### [14:05 - 14:07]

the blue player was trying to send,

### [14:07 - 14:11]

then the skill shouldn't get very much reward.

### [14:11 - 14:14]

And mathematically, this exactly corresponds to saying

### [14:14 - 14:18]

that the reward for the skill corresponds to

### [14:18 - 14:22]

the log probability that the red player was able to guess

### [14:22 - 14:26]

the correct code word.

### [14:26 - 14:28]

And the discriminator here is just updated.

### [14:28 - 14:31]

Using standard maximum likelihood.

### [14:31 - 14:34]

So we tell the discriminator afterwards,

### [14:34 - 14:38]

OK, so the blue player was actually trying to send code word four.

### [14:38 - 14:40]

Update your model to get better at predicting

### [14:40 - 14:41]

that when they do that behavior,

### [14:41 - 14:45]

you should predict code word four.

### [14:45 - 14:48]

And we call this algorithm diversity is all you need,

### [14:48 - 14:53]

or DIAN for short.

### [14:53 - 14:56]

One of the neat things about DIAN is that we show that maximize,

### [14:56 - 14:57]

that this two player game here,

### [14:57 - 15:00]

corresponds to maximizing the amount of information sent

### [15:00 - 15:03]

from the blue player to the red player.

### [15:03 - 15:06]

Exactly corresponds to trying to do well on that game

### [15:06 - 15:12]

where we had two players on the other side of the football field.

### [15:12 - 15:17]

Let's look at some of the behaviors learned by DIAN.

### [15:17 - 15:20]

So I'll start with a very simple task and move to more complex tasks.

### [15:20 - 15:22]

On this very simple task,

### [15:22 - 15:25]

we have an agent that starts at the center of a room,

### [15:25 - 15:29]

and it can navigate in any direction.

### [15:29 - 15:32]

And here we're plotting six different skills.

### [15:32 - 15:34]

And we see that different skills correspond

### [15:34 - 15:36]

to going to different states in the environment.

### [15:36 - 15:38]

We see, say, this pink skill goes to the left,

### [15:38 - 15:41]

and this light green skill goes to the right.

### [15:41 - 15:43]

And looking at this plot,

### [15:43 - 15:46]

we see that this algorithm seems to achieve

### [15:46 - 15:48]

the three properties that we mentioned before.

### [15:48 - 15:50]

It does good exploration.

### [15:50 - 15:52]

It goes to most of the states in the environment.

### [15:52 - 15:54]

It's predictable.

### [15:54 - 15:57]

That is, if I say, where will the pink skill go?

### [15:57 - 15:59]

You can tell me, oh, the pink skill,

### [15:59 - 16:01]

that skill goes to the left.

### [16:01 - 16:03]

And finally, it's interpretable.

### [16:03 - 16:06]

Interpretable in the sense that if I say,

### [16:06 - 16:09]

the agent is at this state right here,

### [16:09 - 16:12]

what skill did he use to get there?

### [16:12 - 16:16]

I can say, oh, that was this off-color shade of green

### [16:16 - 16:20]

that got us there.

### [16:20 - 16:22]

One other important property of DIAN

### [16:22 - 16:24]

that I want to highlight

### [16:24 - 16:27]

is DIAN maximizes not just the diversity

### [16:27 - 16:29]

at the current time step,

### [16:29 - 16:32]

but rather diversity in the future.

### [16:32 - 16:34]

And to illustrate that,

### [16:34 - 16:36]

I want to consider this environment.

### [16:36 - 16:37]

In this environment,

### [16:37 - 16:40]

we have the agent start in a hallway.

### [16:40 - 16:42]

And the hallway is really narrow.

### [16:42 - 16:44]

And so when the agent is in the hallway,

### [16:44 - 16:47]

there's nothing it can do to differentiate itself

### [16:47 - 16:49]

from others.

### [16:49 - 16:51]

There's nothing the agent can do

### [16:51 - 16:54]

to differentiate one skill from another skill.

### [16:54 - 16:57]

And so for skills to become discriminable

### [16:57 - 16:58]

from one another,

### [16:58 - 17:00]

they must get to the end of the hallway

### [17:00 - 17:02]

and out into this open room.

### [17:02 - 17:04]

And once out in the open room,

### [17:04 - 17:06]

different skills can make different actions

### [17:06 - 17:09]

to become discriminable from one another.

### [17:09 - 17:11]

For example, the yellow skill can go down,

### [17:11 - 17:14]

and the purple skill can go to the right.

### [17:14 - 17:16]

And this is important because it shows that

### [17:16 - 17:18]

you can continue to learn skills

### [17:18 - 17:22]

even in settings where you can't be discriminable soon

### [17:22 - 17:23]

to become discriminable.

### [17:23 - 17:26]

To become discriminable in the future,

### [17:26 - 17:29]

agents must take actions to get to spaces

### [17:29 - 17:31]

where it's possible to be discriminable

### [17:31 - 17:35]

from one another.

### [17:35 - 17:37]

Okay, so now that we've built up some of the intuition

### [17:37 - 17:39]

for what these skills look like,

### [17:39 - 17:40]

I want to show some results

### [17:40 - 17:45]

on some higher dimensional tasks.

### [17:45 - 17:48]

So here we're looking at a sort of dog-like robot,

### [17:48 - 17:50]

and we're visualizing some of the skills

### [17:50 - 17:51]

that were learned.

### [17:51 - 17:53]

And we see that we've learned skills corresponding

### [17:53 - 17:55]

to running forwards, running backwards,

### [17:55 - 17:59]

and even doing front flips.

### [17:59 - 18:02]

In fact, we've learned more than that.

### [18:02 - 18:04]

We've learned different ways of running forward.

### [18:04 - 18:06]

We've learned ways of running forward quickly

### [18:06 - 18:08]

and ways of running forward slowly,

### [18:08 - 18:10]

ways of running forward that involve sort of

### [18:10 - 18:16]

lying on your nose and scooping forward.

### [18:16 - 18:20]

We've likewise learned different ways of running backwards

### [18:20 - 18:23]

and even different types of front flips.

### [18:23 - 18:25]

And one of the things I want to emphasize here

### [18:25 - 18:28]

is that all of these different behaviors

### [18:28 - 18:30]

have emerged just out of playing that game

### [18:30 - 18:32]

that we mentioned before.

### [18:32 - 18:34]

These have all emerged out of playing the game

### [18:34 - 18:36]

where the robot's trying to communicate some message

### [18:36 - 18:39]

to the discriminator, to some outside user

### [18:39 - 18:41]

that's trying to guess what message

### [18:41 - 18:48]

is the robot trying to send.

### [18:48 - 18:51]

This also works on other sorts of tasks.

### [18:51 - 18:52]

So,

### [18:52 - 18:55]

we applied to this quadruped robot,

### [18:55 - 18:57]

and here the skills are slightly less interpretable,

### [18:57 - 18:59]

but you still learn skills moving, corresponding

### [18:59 - 19:02]

to moving in different directions.

### [19:02 - 19:04]

For a hopping robot, you learn skills corresponding

### [19:04 - 19:07]

to going forward and backwards.

### [19:07 - 19:10]

And you even learn different ways of solving

### [19:10 - 19:16]

Kurt Pol, the famous control task.

### [19:16 - 19:19]

Any questions about the skills that we've seen so far?

### [19:19 - 19:21]

After this, I'm going to talk about some of the applications

### [19:21 - 19:23]

of learning these skills.

### [19:23 - 19:24]

Yes.

### [19:24 - 19:27]

So, one, I can just want to confirm.

### [19:27 - 19:32]

So, do these agents get no reward

### [19:32 - 19:35]

for getting high rewards from the environment,

### [19:35 - 19:38]

only intrinsic diversity rewards?

### [19:38 - 19:39]

Exactly, yes.

### [19:39 - 19:40]

I could have emphasized that more.

### [19:40 - 19:42]

So, all of these skills are learned

### [19:42 - 19:44]

without any reward function.

### [19:44 - 19:46]

So, these skills are learned just by saying,

### [19:46 - 19:48]

be as diverse as possible.

### [19:48 - 19:50]

We don't include any term that says,

### [19:50 - 19:53]

be as diverse and also try to maximize this reward function.

### [19:53 - 19:55]

No, we don't do that.

### [19:55 - 19:58]

That is very impressive.

### [19:58 - 20:00]

There's also a question in the chat,

### [20:00 - 20:01]

which I think is the same question

### [20:01 - 20:05]

that I also wanted to ask.

### [20:05 - 20:06]

Let's do this.

### [20:06 - 20:08]

Brandon, I will ask the question,

### [20:08 - 20:10]

and you please then confirm if it's the same thing

### [20:10 - 20:13]

that you wanted to know.

### [20:13 - 20:19]

So, is this discriminator looking at trying to discriminate

### [20:19 - 20:22]

which skills is being used continuously,

### [20:22 - 20:24]

or is it looking at the entire trajectory

### [20:24 - 20:26]

at the end of the episode?

### [20:26 - 20:28]

That's a really good question.

### [20:28 - 20:33]

So, the way we do it is that we look at just individual states.

### [20:33 - 20:38]

We say, given the state, what is the robot trying to do?

### [20:38 - 20:41]

You can formulate similar objectives

### [20:41 - 20:43]

that look at entire trajectories

### [20:43 - 20:45]

or look at states and actions,

### [20:45 - 20:47]

look at the state in the initial state,

### [20:47 - 20:49]

look at the state in the final state,

### [20:49 - 20:51]

just look at the final state.

### [20:51 - 20:52]

And there's actually been a lot of work

### [20:52 - 20:54]

that looks at different aspects of these.

### [20:54 - 20:57]

There's a good paper by Joshua Acom

### [20:57 - 21:01]

called Variational Option Discovery Algorithms

### [21:01 - 21:03]

that talks a little bit about comparisons

### [21:03 - 21:05]

between these different sorts of objectives.

### [21:05 - 21:07]

But fundamentally, they all correspond

### [21:07 - 21:08]

to playing the same game.

### [21:08 - 21:13]

They're sort of different instantiations of that game.

### [21:13 - 21:16]

Interesting. Thanks.

### [21:16 - 21:18]

There's another question in the chat.

### [21:18 - 21:19]

Do you see them?

### [21:19 - 21:21]

No.

### [21:21 - 21:26]

So, it says, once the skills are learned,

### [21:26 - 21:31]

how are they selected from a hierarchical standpoint?

### [21:31 - 21:33]

Excellent.

### [21:33 - 21:35]

Garrett, is it okay if I pull it off

### [21:35 - 21:37]

from that question for a couple slides?

### [21:37 - 21:38]

I think in like three slides,

### [21:38 - 21:40]

I'm going to have a description of that.

### [21:40 - 21:41]

Excellent.

### [21:49 - 21:53]

And I see that there was a question

### [21:53 - 21:56]

about using hindsight experience replay.

### [21:56 - 21:57]

No, that's...

### [21:57 - 21:58]

Well, you can answer that.

### [21:58 - 21:59]

Oh, that was earlier.

### [21:59 - 22:01]

Yeah, that's something that we were talking about before.

### [22:01 - 22:02]

Excellent.

### [22:02 - 22:04]

But feel free to comment on that as well.

### [22:04 - 22:06]

There is a way to use something similar

### [22:06 - 22:10]

to hindsight experience replay for this.

### [22:10 - 22:11]

If people are interested,

### [22:11 - 22:16]

we can talk more about it at the end of the talk.

### [22:16 - 22:18]

Okay, so let's talk about some of the applications.

### [22:19 - 22:25]

So, fundamentally, what Diane learns

### [22:25 - 22:28]

is it learns this range of behaviors

### [22:28 - 22:32]

that a certain policy can do in a certain environment.

### [22:32 - 22:35]

And it sort of gives us a low-dimensional knob.

### [22:35 - 22:36]

And by tuning this knob,

### [22:36 - 22:39]

we can sweep over the range of behaviors.

### [22:39 - 22:42]

And note that while the range of behaviors,

### [22:42 - 22:44]

things a robot can do in an environment,

### [22:44 - 22:46]

might be somewhat limited,

### [22:46 - 22:48]

it's a much smaller space

### [22:48 - 22:50]

than the set of parameters.

### [22:50 - 22:51]

And so, effectively,

### [22:51 - 22:52]

we've sort of done something like PCA,

### [22:52 - 22:54]

or dimensionality reduction,

### [22:54 - 22:56]

on the space of behaviors.

### [22:56 - 22:59]

And now we have this compact space of behaviors.

### [22:59 - 23:01]

And just by tuning this low-dimensional knob,

### [23:01 - 23:04]

see, we can sweep over different behaviors.

### [23:04 - 23:07]

And I'll show how this is useful for four applications.

### [23:07 - 23:09]

For hierarchical reinforcement learning,

### [23:09 - 23:10]

as Garrett mentioned,

### [23:10 - 23:11]

as imitation learning,

### [23:11 - 23:14]

as parameter initialization,

### [23:14 - 23:16]

and then for a kind of cool application

### [23:16 - 23:18]

relating to meta-learning.

### [23:18 - 23:22]

So let's start with a hierarchical RL application.

### [23:22 - 23:26]

So we use Diane for hierarchical RL as follows.

### [23:26 - 23:29]

To start, we place the agent in some environment,

### [23:29 - 23:31]

and we learn a set of skills.

### [23:31 - 23:33]

For example, in the top left,

### [23:33 - 23:35]

we place the cheetah robot

### [23:35 - 23:38]

on this track with these obstacles,

### [23:38 - 23:40]

and we just have it learn a set of skills

### [23:40 - 23:43]

without any reward function.

### [23:43 - 23:46]

Then, after learning a set of skills,

### [23:46 - 23:51]

we do hierarchical reinforcement learning as follows.

### [23:51 - 23:55]

We say that we'll have some high-level policy

### [23:55 - 23:58]

that chooses skills to execute.

### [23:58 - 24:00]

Instead of choosing actions,

### [24:00 - 24:01]

they choose skills.

### [24:01 - 24:05]

And each skill will be executed for 50 time steps.

### [24:05 - 24:08]

And then we optimize this high-level policy,

### [24:08 - 24:10]

in this case, just using policy gradient,

### [24:10 - 24:15]

using a version of policy gradient called TRPM.

### [24:15 - 24:19]

And we find that by controlling the agent

### [24:19 - 24:21]

at the level of skills,

### [24:21 - 24:22]

which is the red curve,

### [24:22 - 24:24]

you're able to learn much faster

### [24:24 - 24:26]

than if you directly control the agent

### [24:26 - 24:29]

at the level of motor torques,

### [24:29 - 24:32]

which is the green line here,

### [24:32 - 24:34]

or if you use other algorithms

### [24:34 - 24:37]

that directly control the motor's joint angles

### [24:37 - 24:40]

rather than controlling the behaviors.

### [24:40 - 24:43]

And that's what's shown in the top right plot.

### [24:43 - 24:44]

The bottom left plot shows

### [24:44 - 24:46]

a very similar experiment

### [24:46 - 24:48]

where we first put this ant-like robot

### [24:48 - 24:49]

in an environment

### [24:49 - 24:51]

and we have it learning a set of skills

### [24:51 - 24:54]

without any reward function.

### [24:54 - 24:57]

Then, when a reward function is given,

### [24:57 - 25:00]

we learn a high-level policy

### [25:00 - 25:03]

that chooses which of these skills to execute,

### [25:03 - 25:07]

and each skill is executed for many time steps.

### [25:07 - 25:12]

And again, we find that using the skills,

### [25:12 - 25:13]

commanding the robot

### [25:13 - 25:15]

at the level of skills

### [25:15 - 25:16]

is able to learn much faster.

### [25:16 - 25:18]

We see the purple curve is much higher

### [25:18 - 25:21]

than the other curves here.

### [25:21 - 25:23]

Garrett, does that answer the question

### [25:23 - 25:31]

about how skills are used hierarchically?

### [25:31 - 25:33]

Excellent.

### [25:33 - 25:36]

So another application is,

### [25:36 - 25:38]

or one thing I want to highlight here

### [25:38 - 25:41]

is that for the purpose of hierarchical RL,

### [25:41 - 25:42]

learning more skills is useful.

### [25:42 - 25:43]

This would make sense.

### [25:43 - 25:45]

If you only learn two skills,

### [25:45 - 25:47]

it's really hard to solve complex tasks.

### [25:47 - 25:48]

But if you learn 100 skills,

### [25:48 - 25:50]

it becomes much easier.

### [25:50 - 25:51]

And this plot here is just showing

### [25:51 - 25:53]

that if you learn more skills,

### [25:53 - 25:54]

then you do much better

### [25:54 - 26:01]

at solving these hierarchical tasks.

### [26:01 - 26:02]

There's a question.

### [26:02 - 26:03]

So for the higher level policy,

### [26:03 - 26:04]

action space is basically

### [26:04 - 26:06]

the set of skills, precisely.

### [26:06 - 26:07]

And so in our experiments,

### [26:07 - 26:09]

we learned a discrete set of skills.

### [26:09 - 26:11]

I think we used 20 or 50.

### [26:11 - 26:14]

And so the action space is discrete

### [26:14 - 26:16]

and it's size 20 or size 50,

### [26:16 - 26:23]

depending on how many skills you learned.

### [26:23 - 26:24]

And we do execute each skill

### [26:24 - 26:25]

for multiple time steps.

### [26:25 - 26:31]

I believe it was 50 in the paper.

### [26:31 - 26:33]

And so is it the same?

### [26:33 - 26:37]

So you execute a skill for 50 time steps

### [26:37 - 26:40]

and then the discriminators looks

### [26:40 - 26:46]

at the 50 time steps at the same number, right?

### [26:46 - 26:50]

So there's sort of two stages of the method.

### [26:50 - 26:53]

So during training,

### [26:53 - 26:56]

I think we trained for 1,000 time steps,

### [26:56 - 26:58]

which is the length of these episodes

### [26:58 - 26:59]

in these environments.

### [26:59 - 27:00]

And the discriminator looks

### [27:00 - 27:03]

at every time step individually.

### [27:03 - 27:05]

And then when we deploy

### [27:05 - 27:07]

or when we use the skills

### [27:07 - 27:09]

for hierarchical reinforcement learning,

### [27:09 - 27:11]

we actually don't use the discriminator at all.

### [27:11 - 27:14]

All we do is we, I guess,

### [27:14 - 27:20]

execute the learned skills.

### [27:20 - 27:22]

Got it.

### [27:22 - 27:26]

See you sometime later, Thijs.

### [27:26 - 27:30]

Join our next time errors.

### [27:30 - 27:32]

So, well, for hierarchical RL,

### [27:32 - 27:35]

we didn't need to use the discriminator

### [27:35 - 27:37]

to solve the downstream application.

### [27:37 - 27:38]

For imitation learning,

### [27:38 - 27:41]

we will actually use the discriminator.

### [27:41 - 27:46]

So one other sort of neat application of Diane

### [27:46 - 27:48]

is for zero-shot imitation learning.

### [27:48 - 27:50]

And by, I mean, zero-shot imitation learning,

### [27:50 - 27:52]

I mean the following thing.

### [27:52 - 27:55]

We show the agent some behavior.

### [27:55 - 27:57]

Like we show the agent, okay,

### [27:57 - 27:59]

here's a robot performing some task.

### [27:59 - 28:02]

And then we immediately want our agent

### [28:02 - 28:03]

to replicate that behavior.

### [28:03 - 28:06]

We want our robot to do the exact same thing

### [28:06 - 28:08]

without any additional training.

### [28:08 - 28:11]

And here's how we can do that.

### [28:11 - 28:13]

And it's actually a very small modification

### [28:13 - 28:15]

to the algorithm we used

### [28:15 - 28:17]

for learning this set of skills.

### [28:17 - 28:20]

So whereas before we took a skill,

### [28:20 - 28:22]

fed it into the environment,

### [28:22 - 28:24]

and then had the discriminator guess

### [28:24 - 28:27]

what code word is the skill trying to send,

### [28:27 - 28:30]

what we do now is we take the expert

### [28:30 - 28:33]

and we say, given the expert states,

### [28:33 - 28:37]

what skill is the expert trying to send?

### [28:37 - 28:39]

And of course the expert has no idea

### [28:39 - 28:40]

what these skills are,

### [28:40 - 28:43]

but we can still ask the discriminator,

### [28:43 - 28:45]

if this were one of the skills,

### [28:45 - 28:47]

which skill would this be?

### [28:47 - 28:49]

And so the discriminator tells us

### [28:49 - 28:52]

which of our skills is most similar to the expert.

### [28:52 - 28:55]

And then by executing the corresponding skill,

### [28:55 - 28:56]

we can get a good approximation

### [28:56 - 28:59]

to the expert's behavior.

### [28:59 - 29:01]

So here's some examples of that.

### [29:01 - 29:04]

So this top row shows,

### [29:04 - 29:05]

so in this top left example,

### [29:05 - 29:07]

we have an expert that's lying

### [29:07 - 29:08]

on his back,

### [29:08 - 29:10]

and then we feed this state

### [29:10 - 29:12]

into this group, the discriminator,

### [29:12 - 29:14]

and the discriminator says,

### [29:14 - 29:16]

oh, that must be skill seven

### [29:16 - 29:17]

or something like that.

### [29:17 - 29:18]

And then we execute

### [29:18 - 29:20]

the corresponding die-in skill.

### [29:20 - 29:22]

And we see that this skill

### [29:22 - 29:23]

is a pretty good approximation

### [29:23 - 29:26]

to the expert's behavior.

### [29:26 - 29:30]

Similarly, if the expert rolls on its nose,

### [29:30 - 29:33]

then we see that the retrieved die-in skill

### [29:33 - 29:36]

also rolls on its nose.

### [29:36 - 29:37]

And of course,

### [29:37 - 29:39]

that doesn't always work.

### [29:39 - 29:40]

And so in the far right,

### [29:40 - 29:42]

we show an example of a failure case

### [29:42 - 29:44]

where the expert is on its nose

### [29:44 - 29:47]

and the die-in skill also rolls onto its nose,

### [29:47 - 29:50]

but doesn't quite do the full handstand.

### [29:50 - 29:51]

And this sort of makes sense

### [29:51 - 29:53]

because if you haven't learned

### [29:53 - 29:55]

how to learn a skill for a certain behavior,

### [29:55 - 29:57]

then it's going to be really hard

### [29:57 - 30:02]

to imitate that behavior.

### [30:02 - 30:04]

Okay.

### [30:04 - 30:06]

Any questions about either the hierarchical RL

### [30:06 - 30:08]

or the imitation learning applications?

### [30:16 - 30:18]

I mean, the approach is pretty clear,

### [30:18 - 30:20]

but the applications,

### [30:20 - 30:22]

you haven't talked about them too much,

### [30:22 - 30:25]

but I can think of so many directions.

### [30:25 - 30:28]

So have you looked into it further?

### [30:28 - 30:31]

What can you apply it to actually?

### [30:31 - 30:35]

What are you thinking of?

### [30:35 - 30:38]

Well, multi-agent,

### [30:38 - 30:40]

various multi-agent games where,

### [30:40 - 30:41]

for example,

### [30:41 - 30:44]

judging what the other player does is important.

### [30:44 - 30:48]

Like you're playing Pong with two players,

### [30:48 - 30:51]

for example, or something.

### [30:51 - 30:53]

That'd be really cool.

### [30:53 - 30:56]

There's been some work on,

### [30:56 - 30:59]

so here we're maximizing information

### [30:59 - 31:02]

between the,

### [31:02 - 31:04]

basically between the two players

### [31:04 - 31:06]

in this game.

### [31:06 - 31:07]

Interestingly,

### [31:07 - 31:09]

there's been some work on multi-agent RL

### [31:09 - 31:12]

that minimizes information between players,

### [31:12 - 31:15]

where they try to say that you want to have agents

### [31:15 - 31:17]

solve a task independently.

### [31:17 - 31:19]

And so you want them to specialize,

### [31:19 - 31:21]

but I very much agree.

### [31:21 - 31:23]

It would be cool to see this in a multi-agent setting.

### [31:23 - 31:25]

And maybe you could show that you get

### [31:25 - 31:27]

interesting robustness benefits

### [31:27 - 31:29]

because different agents end up solving a task

### [31:29 - 31:32]

in different ways.

### [31:32 - 31:33]

I don't know.

### [31:34 - 31:36]

I think it's a good idea.

### [31:36 - 31:43]

Yeah, basically like tons of directions

### [31:43 - 31:45]

for further work for all of you guys

### [31:45 - 31:48]

to pick up potentially.

### [31:48 - 31:49]

Yeah, definitely.

### [31:49 - 31:50]

And if anyone has ideas,

### [31:50 - 31:51]

they want to chat more about,

### [31:51 - 31:52]

you can bring them up now or at the end,

### [31:52 - 31:55]

or shoot me an email.

### [31:55 - 31:58]

Sure.

### [31:58 - 32:01]

Of a policy for downstream tasks.

### [32:01 - 32:03]

So let's say you want to solve a task

### [32:03 - 32:05]

in some environment.

### [32:05 - 32:11]

And normally you would say run reinforcement learning.

### [32:11 - 32:12]

And you would initialize your parameters,

### [32:12 - 32:16]

say by sampling from a normal distribution.

### [32:16 - 32:18]

We can do something slightly smarter,

### [32:18 - 32:21]

which is that instead of initializing the policy

### [32:21 - 32:23]

using random weights,

### [32:23 - 32:25]

we can initialize the policy weights

### [32:25 - 32:29]

using one of the skills learned by Diane.

### [32:29 - 32:31]

And the intuition here is that

### [32:31 - 32:33]

the skills learned by Diane

### [32:33 - 32:35]

reflect the set of behaviors

### [32:35 - 32:38]

that are possible in this environment.

### [32:38 - 32:40]

And so it sort of reflects a bias

### [32:40 - 32:43]

about what sorts of behaviors

### [32:43 - 32:45]

will be useful in this environment.

### [32:45 - 32:49]

And you hear that by initializing a policy

### [32:49 - 32:51]

using one of the skills learned by Diane,

### [32:51 - 32:53]

you're able to learn much faster

### [32:53 - 32:58]

than if you just randomly initialize your policy.

### [32:58 - 33:00]

And so I think this is sort of interesting

### [33:00 - 33:02]

because it suggests that even in settings

### [33:02 - 33:04]

where you wouldn't really think

### [33:04 - 33:06]

of skill learning being useful,

### [33:06 - 33:07]

just the standard,

### [33:07 - 33:09]

so this here is the standard RL setting.

### [33:09 - 33:13]

There's no multi-agent.

### [33:13 - 33:15]

There's no hierarchical RL.

### [33:15 - 33:16]

We don't have multiple agents.

### [33:16 - 33:18]

And these aren't hard exploration tasks.

### [33:18 - 33:20]

Even in this setting,

### [33:20 - 33:22]

learning skills is useful

### [33:22 - 33:24]

because it gives us good parameters,

### [33:24 - 33:26]

good parameter initializations

### [33:26 - 33:28]

for solving these sorts of tasks.

### [33:32 - 33:35]

And the final application

### [33:35 - 33:38]

is kind of weird,

### [33:38 - 33:40]

but also sort of interesting

### [33:40 - 33:41]

in thinking about

### [33:41 - 33:43]

what are the range of things you can learn

### [33:43 - 33:45]

without a reward function?

### [33:45 - 33:48]

And this is to meta-reinforcement learning.

### [33:48 - 33:49]

So I'll first explain

### [33:49 - 33:55]

how meta-reinforcement learning...

### [33:55 - 33:56]

back a little bit.

### [33:56 - 33:57]

Great, okay.

### [33:57 - 33:58]

So what is meta-reinforcement learning?

### [33:58 - 34:00]

Meta-reinforcement learning is the problem

### [34:00 - 34:02]

of learning a learning

### [34:02 - 34:06]

algorithm that's good at solving tasks.

### [34:06 - 34:08]

So this usually works as follows.

### [34:08 - 34:10]

You put an agent in an environment

### [34:10 - 34:13]

with an unknown reward function,

### [34:13 - 34:15]

and then the robot has to quickly figure out

### [34:15 - 34:16]

what is the reward function

### [34:16 - 34:19]

and maximize that reward function.

### [34:19 - 34:20]

And usually,

### [34:20 - 34:22]

this reward function might correspond

### [34:22 - 34:24]

to navigating to different locations

### [34:24 - 34:27]

or maybe running at different philosophies.

### [34:27 - 34:30]

And ordinarily...

### [34:30 - 34:32]

Sorry, can you specify

### [34:32 - 34:33]

a little bit

### [34:33 - 34:36]

what do you mean by unknown reward function?

### [34:36 - 34:38]

Because in one sense of the word,

### [34:38 - 34:39]

it's always unknown, right?

### [34:39 - 34:41]

We only get samples from the function.

### [34:41 - 34:43]

In another sense of the world,

### [34:43 - 34:45]

like it's...

### [34:45 - 34:47]

How do we even...

### [34:47 - 34:50]

If we don't even get examples of rewards,

### [34:50 - 34:54]

how is it possible to optimize it?

### [34:54 - 34:56]

Yeah, it's a really good question.

### [34:56 - 34:57]

But unknown here,

### [34:57 - 34:58]

I mean that the agent

### [34:58 - 35:00]

does get samples of the reward,

### [35:00 - 35:02]

but every time the agent interacts

### [35:02 - 35:03]

with the environment,

### [35:03 - 35:04]

so for every episode,

### [35:04 - 35:06]

they're solving a different task.

### [35:06 - 35:08]

And so the reward function changes.

### [35:08 - 35:09]

So one day,

### [35:09 - 35:10]

the robot's solving one task.

### [35:10 - 35:11]

The next day,

### [35:11 - 35:12]

the robot's trying to go

### [35:12 - 35:13]

to a different location.

### [35:13 - 35:14]

And the third day,

### [35:14 - 35:15]

the robot's trying to go

### [35:15 - 35:16]

to a third location.

### [35:16 - 35:18]

And so what this means is that

### [35:18 - 35:20]

in the course of every episode,

### [35:20 - 35:21]

the robot has to infer,

### [35:21 - 35:22]

has to say,

### [35:22 - 35:23]

okay,

### [35:23 - 35:24]

I've gotten a little bit of reward

### [35:24 - 35:25]

so far today,

### [35:25 - 35:26]

so maybe I'm trying...

### [35:26 - 35:28]

Maybe the goal is hidden over here.

### [35:28 - 35:30]

I should try to run over there.

### [35:32 - 35:38]

And so meta-reinforcement learning works,

### [35:38 - 35:41]

but it has one main limitation,

### [35:41 - 35:43]

which is that you have to design

### [35:43 - 35:45]

a set of reward functions

### [35:45 - 35:47]

to use for training.

### [35:47 - 35:49]

So the hope of meta-reinforcement learning

### [35:49 - 35:51]

is that you learn

### [35:51 - 35:54]

how to quickly learn unknown tasks,

### [35:54 - 35:55]

and then you can put a robot

### [35:55 - 35:56]

in a new environment,

### [35:56 - 35:57]

and it will be able to solve

### [35:57 - 36:00]

any task you want.

### [36:00 - 36:01]

But this ability hinges on

### [36:01 - 36:02]

the design of the reward functions

### [36:02 - 36:03]

used for training.

### [36:03 - 36:04]

So during training,

### [36:04 - 36:05]

you may have placed the goal

### [36:05 - 36:06]

in three different locations,

### [36:06 - 36:07]

or you may have given

### [36:07 - 36:08]

the robot rewards corresponding

### [36:08 - 36:09]

to going forwards one day

### [36:09 - 36:10]

and going backwards

### [36:10 - 36:11]

a different day.

### [36:11 - 36:12]

But you had to sit down

### [36:12 - 36:13]

and manually define

### [36:13 - 36:14]

those reward functions.

### [36:14 - 36:15]

And manually defining them

### [36:15 - 36:16]

is actually really hard.

### [36:16 - 36:17]

I'll give one sort of funny

### [36:17 - 36:18]

example of this.

### [36:18 - 36:19]

So one of the tasks people do

### [36:19 - 36:20]

in meta-reinforcement learning

### [36:20 - 36:21]

is ants now.

### [36:21 - 36:22]

Ants,

### [36:22 - 36:23]

you know,

### [36:23 - 36:24]

they're like,

### [36:24 - 36:25]

they're like,

### [36:25 - 36:26]

oh,

### [36:26 - 36:27]

oh,

### [36:27 - 36:28]

oh,

### [36:28 - 36:29]

oh,

### [36:29 - 36:30]

oh,

### [36:30 - 36:31]

oh,

### [36:31 - 36:32]

oh,

### [36:32 - 36:33]

you know,

### [36:33 - 36:34]

it's always a little

### [36:34 - 36:35]

tricky to navigate

### [36:35 - 36:36]

about an ant-like robot

### [36:36 - 36:37]

for bringing you

### [36:37 - 36:38]

a task.

### [36:38 - 36:39]

What we can do

### [36:39 - 36:40]

is go to the scale

### [36:40 - 36:41]

lectures

### [36:41 - 36:42]

where you need

### [36:42 - 36:43]

to go to a separate

### [36:43 - 36:44]

class to study

### [36:44 - 36:45]

the task.

### [36:45 - 36:46]

And you'll slightly

### [36:46 - 36:47]

listen to what

### [36:47 - 36:48]

Google is doing

### [36:48 - 36:49]

so that you can

### [36:49 - 36:50]

document

### [36:50 - 36:51]

this however you

### [36:51 - 36:52]

like.

### [36:52 - 36:53]

And when you think

### [36:53 - 36:54]

that,

### [36:54 - 36:55]

well,

### [36:55 - 36:56]

then you get

### [36:56 - 36:57]

like honestly,

### [36:57 - 36:58]

somebody라고

### [36:58 - 36:59]

meanwhile

### [36:59 - 37:00]

inaudible

### [37:00 - 37:04]

but to get mental reinforcement learning algorithms

### [37:04 - 37:08]

to work well, you have to very carefully consider

### [37:08 - 37:11]

how are you going to define reward functions?

### [37:11 - 37:13]

How are you gonna make sure that the reward functions

### [37:13 - 37:16]

are not too easy and not too hard

### [37:16 - 37:19]

and induce a sufficiently diverse set of behaviors?

### [37:22 - 37:27]

Now, Dyan allows us to lift one of these limitations.

### [37:27 - 37:30]

Dyan allows us to automatically propose

### [37:30 - 37:32]

the set of reward functions we use

### [37:32 - 37:35]

for mental reinforcement learning.

### [37:35 - 37:36]

So this works as follows.

### [37:38 - 37:43]

So first, we assume we're given some environment

### [37:44 - 37:49]

and then we do what we call unsupervised mental learning.

### [37:49 - 37:54]

And what I mean by this is that instead of,

### [37:54 - 37:56]

so normally in mental reinforcement learning,

### [37:56 - 38:00]

you have some agent try to solve

### [38:00 - 38:02]

new reward functions in every episode.

### [38:02 - 38:05]

And these reward functions are manually specified

### [38:05 - 38:06]

by some human.

### [38:07 - 38:09]

What we do now is something slightly different.

### [38:09 - 38:12]

We say, we're gonna maximize reward functions

### [38:12 - 38:14]

that are specified by skills.

### [38:14 - 38:17]

So we have one reward function corresponding

### [38:17 - 38:19]

to code word one.

### [38:19 - 38:21]

And specifically the reward function we use

### [38:21 - 38:24]

is the discriminator's predictions.

### [38:24 - 38:27]

So one task is make the discriminator think

### [38:27 - 38:28]

that you're conveying code word one.

### [38:28 - 38:34]

And different task is make the discriminator think

### [38:34 - 38:35]

that you're conveying code word two.

### [38:35 - 38:38]

And so on and so forth.

### [38:38 - 38:43]

And so the interesting thing here is that these tasks

### [38:43 - 38:44]

that we've learned,

### [38:44 - 38:47]

these tasks that we're using for meta reinforcement learning

### [38:47 - 38:49]

are not manually specified.

### [38:49 - 38:52]

And so we no longer have to have a human come in

### [38:52 - 38:54]

and write down what are the set of behaviors

### [38:54 - 38:56]

that we wanna train on.

### [38:56 - 38:58]

We can learn this unsupervised.

### [38:58 - 38:59]

Without any human in the loop.

### [39:02 - 39:03]

And the motivation for doing this,

### [39:03 - 39:05]

for doing this unsupervised meta learning

### [39:05 - 39:07]

is that at test time,

### [39:07 - 39:09]

when a human actually comes along and says,

### [39:09 - 39:12]

maximize this reward function as quickly as possible,

### [39:12 - 39:13]

we can do that.

### [39:13 - 39:16]

And we can do that because we've learned how to solve

### [39:16 - 39:17]

a wide range of tasks.

### [39:17 - 39:21]

We've learned how to solve a very diverse set of tasks

### [39:21 - 39:22]

in this environment.

### [39:23 - 39:25]

I know this is a little bit convoluted.

### [39:25 - 39:27]

Are there any questions about this unsupervised model?

### [39:27 - 39:28]

Are there any questions about this unsupervised model?

### [39:28 - 39:28]

Are there any questions about this unsupervised model?

### [39:28 - 39:29]

Are there any questions about this unsupervised model?

### [39:29 - 39:29]

Are there any questions about this unsupervised model?

### [39:29 - 39:29]

Are there any questions about this unsupervised model?

### [39:32 - 39:36]

I mean, I have a like version in my head of how it works.

### [39:36 - 39:39]

I want you to verify if it's true or not.

### [39:39 - 39:42]

So you pick a, one of the skills.

### [39:42 - 39:44]

So you acquire this set of skills,

### [39:44 - 39:45]

then you pick one of them

### [39:45 - 39:48]

and then you reward following that skill.

### [39:48 - 39:49]

Is that what happens?

### [39:50 - 39:51]

Exactly, yeah.

### [39:53 - 39:54]

And importantly, we're doing this

### [39:54 - 39:55]

in the meta learning setting.

### [39:55 - 39:58]

And so, we're learning a policy that is not just

### [39:58 - 40:01]

that can quickly adapt to maximize,

### [40:01 - 40:03]

to learn these different skills.

### [40:03 - 40:05]

So the robot could be able to very quickly adapt

### [40:05 - 40:08]

its behavior to do skill one or do skill two

### [40:08 - 40:09]

or do skill three.

### [40:10 - 40:13]

And this fast adaptation is important

### [40:13 - 40:16]

because when we're trying to solve a new task,

### [40:16 - 40:18]

we don't want to have to keep trying and failing

### [40:18 - 40:20]

and trying and failing to solve that task.

### [40:20 - 40:22]

We want to very rapidly be able to figure out

### [40:22 - 40:25]

which of the behaviors that we've learned before

### [40:25 - 40:27]

can solve this new task.

### [40:28 - 40:33]

Okay, so this highlights four applications of Dianne.

### [40:39 - 40:42]

Oh, sorry, I forgot to get the results on that.

### [40:42 - 40:45]

So here's an example of some results

### [40:45 - 40:48]

on the half-cuted task.

### [40:48 - 40:49]

And there are a couple,

### [40:49 - 40:52]

there's two things I want you to look at in this plot.

### [40:52 - 40:54]

The green line is our method.

### [40:54 - 40:58]

So when you learn, when you meta-learn,

### [40:58 - 41:00]

using the skills learned from Dianne,

### [41:00 - 41:02]

you're able to learn quite quickly.

### [41:02 - 41:04]

And the X-axis here is number of trials

### [41:04 - 41:06]

it takes to learn the task.

### [41:06 - 41:08]

And we see that we're able to learn these tasks

### [41:08 - 41:11]

in less than, say, 20 trials.

### [41:14 - 41:15]

The black line here,

### [41:18 - 41:19]

is that what we want?

### [41:23 - 41:26]

Yeah, I think maybe a good comparison is the black line

### [41:26 - 41:27]

in the right plot.

### [41:28 - 41:31]

And what that's showing is if you had a human come in

### [41:31 - 41:33]

and design the set of tasks,

### [41:33 - 41:35]

that's how quickly you would learn.

### [41:35 - 41:39]

And we observed that given these oracle human tasks,

### [41:39 - 41:42]

you will learn initially a little bit faster,

### [41:42 - 41:46]

but actually asymptotically, you would get lower reward.

### [41:46 - 41:49]

And what this highlights is that not only does skill learning

### [41:49 - 41:52]

provide a good set of skills,

### [41:52 - 41:54]

it actually provides the right set of skills.

### [41:54 - 41:55]

It provides the right set of skills

### [41:55 - 41:57]

for learning unknown tasks.

### [41:58 - 42:03]

Okay, so in this talk,

### [42:04 - 42:07]

we talked about how we can learn sets of skills

### [42:07 - 42:08]

without reward functions.

### [42:08 - 42:10]

And one of the main ideas is that we should optimize

### [42:10 - 42:12]

over the entire set.

### [42:12 - 42:14]

And this set should be optimized

### [42:14 - 42:16]

to be as diverse as possible.

### [42:17 - 42:20]

The method for doing that was this sort of two-player game,

### [42:20 - 42:22]

where you have one player, the policy,

### [42:22 - 42:24]

try to communicate some message,

### [42:24 - 42:27]

and another player try to infer what message is,

### [42:27 - 42:29]

the first player try to send.

### [42:30 - 42:34]

We then look at some applications of these learned skills.

### [42:34 - 42:34]

We looked at applications

### [42:34 - 42:36]

for hierarchical reinforcement learning,

### [42:36 - 42:38]

for zero-shot imitation learning,

### [42:38 - 42:42]

for parameter initialization,

### [42:42 - 42:44]

and for unsupervised meta learning.

### [42:46 - 42:48]

There are a number of new and interesting ways

### [42:48 - 42:49]

we can take this.

### [42:49 - 42:52]

A lot of these problems have people have looked at

### [42:52 - 42:52]

certain aspects of them,

### [42:52 - 42:56]

but they're still lots of interesting, open questions.

### [42:56 - 42:57]

So, one is, there's a problem, which is this.

### [42:57 - 43:03]

One is this sort of chicken and the egg problem, where we're jointly optimizing the skills

### [43:03 - 43:10]

in the discriminator, but if the policy hasn't learned discriminable skills, then the discriminator

### [43:10 - 43:15]

can't distinguish one skill from another, and then the policy doesn't get any reward.

### [43:15 - 43:18]

And somehow we sort of have to break this chicken and the egg cycle, where nothing ever

### [43:18 - 43:21]

gets improved.

### [43:21 - 43:26]

In practice, some amount of random initialization seems to help with that, but maybe there are

### [43:26 - 43:28]

more intelligent ways of doing that.

### [43:28 - 43:34]

Maybe you could start by, say, running an off-the-shelf exploration algorithm, and then

### [43:34 - 43:39]

segmenting that behavior into a set of skills.

### [43:39 - 43:43]

A second application is applying this to real-world tasks.

### [43:43 - 43:46]

As I alluded to in the beginning, when we apply things in the real world, we have to

### [43:46 - 43:51]

cope with a whole range of additional challenges, things like resetting and things like ensuring

### [43:51 - 43:56]

safety and figuring out how do you learn skills that can be learned in a reset-free manner,

### [43:56 - 43:57]

and can be learned in a safe manner.

### [43:57 - 44:02]

I think it's a really interesting research question.

### [44:02 - 44:05]

A third question is about semi-supervised reinforcement learning.

### [44:05 - 44:10]

So while many of the tasks we look at are relatively low-dimensional, as we move on

### [44:10 - 44:17]

to higher-dimensional tasks, the range of behaviors that you could do can be quite large.

### [44:17 - 44:22]

And maybe if we could provide just a little bit of additional supervision about what skills

### [44:22 - 44:24]

we actually care about, we'd be able to solve downstream tasks.

### [44:24 - 44:25]

And that would be really interesting.

### [44:25 - 44:26]

Thank you.

### [44:26 - 44:30]

So how can we improve our skills in these environments much more quickly?

### [44:30 - 44:37]

For example, maybe you have a robot that has arms and legs, but maybe all that you really

### [44:37 - 44:38]

care about is walking around.

### [44:38 - 44:44]

And if all you care about is walking around, you probably can ignore any behaviors that

### [44:44 - 44:46]

move the arms around.

### [44:46 - 44:53]

And figuring out how can you efficiently encode this inductive bias that walking is important

### [44:53 - 44:56]

but arm motions aren't seems useful for accelerating.

### [44:56 - 45:02]

Finally, and I think the thing I'm most excited about, is just figuring out how to

### [45:02 - 45:04]

scale this.

### [45:04 - 45:12]

So, in the environment we tried, we found that using more than about 50 skills didn't

### [45:12 - 45:13]

improve behavior.

### [45:13 - 45:20]

We found that it's really hard to learn more than 50 behaviors in these environments.

### [45:20 - 45:26]

But for more complex tasks, for tasks that involve many objects or multiple robots, say,

### [45:26 - 45:26]

in a multi-agent environment, it's really hard to just figure out how to scale this.

### [45:26 - 45:34]

setting, there have to be a much larger range of possible behaviors. And figuring out how

### [45:34 - 45:39]

do you efficiently learn huge sets of skills, huge libraries of skills, I think is a really

### [45:39 - 45:45]

important problem. You could imagine that given an unknown environment, you first learn

### [45:45 - 45:50]

the library of behaviors, and then any researcher that wants to use this environment in the

### [45:50 - 45:56]

future no longer has to do reinforcement learning on the original environment, but now can just

### [45:56 - 46:01]

search over the space of learning skills. This would provide in the same way that people

### [46:01 - 46:05]

use pre-trained language embeddings, like Bert, or pre-trained image embeddings from

### [46:05 - 46:12]

say Resonant. This would provide us with a similar mechanism to use pre-trained skills

### [46:12 - 46:19]

for solving downstream tasks. So, those are four ideas of directions that we could take

### [46:19 - 46:23]

this. I would love to open the floor now to hear some of the ideas that all of you have

### [46:23 - 46:25]

for taking these sorts of projects.

### [46:25 - 46:26]

If any of you want to ask any questions, please do so in the comment section below.

### [46:26 - 46:26]

And if any of you want to ask any questions, please do so in the comment section below.

### [46:26 - 46:30]

to chat more about this afterwards feel free to shoot me an email and we can set up a time to chat

### [46:31 - 46:38]

thanks no thank you very much ben that was a very interesting talk

### [46:51 - 46:53]

do you want me to read questions from the chat or

### [46:53 - 46:59]

oh yeah i figured out how to pull it up thanks i see there's an earlier question from anton about

### [46:59 - 47:04]

have you tried it on a football environment uh no but i think it'll be really cool

### [47:04 - 47:09]

maybe you would learn like different uh strategies like i know that different football players

### [47:09 - 47:13]

have played their position in different ways different goalies have different strategies

### [47:13 - 47:17]

different strikers have different strategies they're really cool to see that um

### [47:19 - 47:22]

those sort of differences of behaviors could emerge out of an objective like this

### [47:24 - 47:30]

a question from brandon does the meta rl agent use any information the skill agent or does it

### [47:30 - 47:35]

just use the discriminator from diane uh for meta reinforcement learning we just used the

### [47:35 - 47:39]

discriminator we did not use the policy itself

### [47:49 - 47:53]

yeah i wonder if it can be applied in discrimination first

### [47:53 - 47:54]

yeah i think it can be applied in discrimination first

### [47:54 - 47:59]

so we're a main goal is actually not to control agents but to understand what they're doing

### [47:59 - 48:04]

i'm not sure what would be a good example maybe you're looking for

### [48:05 - 48:12]

connections to your server that are trying to break it break into or something and then you

### [48:12 - 48:17]

train with diane agents and skills and then you classify skills with discriminator

### [48:21 - 48:21]

yeah

### [48:23 - 48:30]

we've thought about this a little bit in terms of like uh hacking or fuzzing or uh making test

### [48:30 - 48:41]

cases so many autonomous car companies have entire teams dedicated to constructing hard examples

### [48:42 - 48:49]

examples where their agents will fail because we know that in many of these real world applications

### [48:49 - 48:50]

of autonomous systems

### [48:53 - 48:57]

it's pretty easy driving on a highway or on suburban roads is pretty easy

### [48:57 - 49:03]

but there are these edge cases that end up being really hard and you can imagine using an algorithm

### [49:03 - 49:08]

like this to automatically discover edge cases it would work probably as follows it would be

### [49:08 - 49:15]

something like figure out how to change the settings of a scene figure out what signs to

### [49:15 - 49:21]

add and how to change the behavior of other cars such that your own car behaves in different ways

### [49:22 - 49:23]

and if you can make your

### [49:23 - 49:29]

car behave in different wacky ways then it's possible those are hard those are cases that

### [49:29 - 49:34]

you want to focus more on for example if you set up a scene where your car drives off the road

### [49:34 - 49:37]

you set up another scene where the car drives into oncoming traffic except the third scene

### [49:37 - 49:44]

where the car stops in the middle of a lane then those seem like useful cases to try to debug

### [49:48 - 49:52]

definitely i see this question from anton how much faster is fine tuning

### [49:54 - 49:58]

meta models um so this is in respect

### [50:03 - 50:05]

uh anton i'm not quite sure i understand the question

### [50:06 - 50:09]

is it asking how much faster do you learn by

### [50:10 - 50:14]

doing fine tuning instead of doing reinforcement learning from scratch

### [50:19 - 50:20]

or is that in this slide here

### [50:23 - 50:40]

so i don't know maybe even some people who the

### [50:40 - 50:45]

one of the steps between being able to tune for these features are roughly two to three times

### [50:45 - 50:51]

easier than if you just randomly initialize the policy and learn from there and how much

### [50:51 - 50:52]

faster you learn depends a lot on how many steps do you have you're trying to learn to tune.

### [50:52 - 50:55]

on the environment.

### [50:55 - 50:57]

And so for the cheetah task,

### [50:57 - 50:59]

we observed you learn much, much faster.

### [50:59 - 51:04]

So we observe it up until this point,

### [51:04 - 51:07]

the randomly initialized policy hasn't learned anything,

### [51:07 - 51:09]

but the policy initialized with Italian

### [51:09 - 51:11]

has already gotten a reward of about 5,000.

### [51:13 - 51:17]

One of the interesting things is for this ant robot.

### [51:17 - 51:20]

If you look at the initial starting state,

### [51:20 - 51:21]

so ant is one of these robots

### [51:21 - 51:24]

where it's really easy to fall over.

### [51:24 - 51:27]

And by initializing with one of the skills,

### [51:27 - 51:29]

you're guaranteed to initialize with a policy

### [51:29 - 51:30]

that doesn't fall over.

### [51:31 - 51:33]

And what that means is that this gap

### [51:33 - 51:35]

of roughly a thousand rewards

### [51:35 - 51:38]

just comes from already knowing how to stand up.

### [51:38 - 51:40]

And knowing how to stand up is a really useful prior

### [51:40 - 51:42]

for solving downstream tasks.

### [51:44 - 51:45]

On the hopper task,

### [51:45 - 51:48]

we observed that these curves are closer together.

### [51:48 - 51:51]

So there isn't as much benefit from initializing

### [51:51 - 51:53]

with one of the dying skills.

### [52:19 - 52:21]

I think we should let you go

### [52:21 - 52:23]

for a couple of minutes, right?

### [52:23 - 52:26]

So you have your last chance to ask a question.

### [52:32 - 52:34]

I should mention that there has been a huge amount

### [52:34 - 52:35]

of follow-up work.

### [52:35 - 52:37]

And so I'd highly recommend checking out some

### [52:37 - 52:39]

of the papers that have come after this.

### [52:40 - 52:42]

I personally really liked the unsupervised

### [52:42 - 52:44]

meta-learning project that we worked on,

### [52:45 - 52:49]

but there's been a lot of other really interesting work

### [52:49 - 52:49]

on things you can do using these sorts of tools,

### [52:49 - 52:53]

you can do using these sorts of skill learning methods.

### [53:03 - 53:04]

What other environments have you run on

### [53:04 - 53:07]

and were there any difficulties?

### [53:07 - 53:10]

Yeah, so I'll talk about a failure case.

### [53:10 - 53:15]

So one setting where I really wanted this to work

### [53:15 - 53:17]

was on a manipulation setting,

### [53:17 - 53:19]

sort of like the one at the very beginning of this talk.

### [53:19 - 53:19]

Yeah, so I'll talk about a failure case. So one setting where I really wanted this to work was on a manipulation setting, sort of like the one at the very beginning of this talk,

### [53:19 - 53:33]

talk. So imagine that you have some robot and you can interact with some objects and ideally you

### [53:33 - 53:37]

learn different skills corresponding to manipulating the objects in different ways.

### [53:39 - 53:44]

Now in practice actually learning that set of skills is really hard.

### [53:44 - 53:51]

And the reason it's hard is because of exploration. So on a robot like this what you find

### [53:51 - 53:57]

when you run something on Diane is that you learn many different ways of moving the arm around but

### [53:57 - 54:03]

the arm actually rarely touches the blocks and because the robot rarely touches the blocks it

### [54:03 - 54:07]

becomes hard to solve this chicken and the egg problem because if the robot never touches the

### [54:07 - 54:13]

blocks the discriminator doesn't learn to associate any configuration of blocks with any certain skill.

### [54:15 - 54:20]

And because the discriminator doesn't know to identify stacking with one skill and pushing

### [54:20 - 54:26]

with another skill then the robot doesn't get rewarded for doing that. And so I really want

### [54:26 - 54:31]

to see someone figure out how to apply similar skill learning algorithms to a robot like this.

### [54:31 - 54:37]

I think that'll be really really cool especially because these exploration problems are not only

### [54:37 - 54:41]

the problem for skill learning but they're also the problem for every downstream task

### [54:41 - 54:43]

that you would try to solve using this robot.

### [54:44 - 54:48]

If you would learn a set of skills that correspond to throwing, stacking,

### [54:48 - 54:53]

pushing, grasping, sorting, etc then solving downstream tasks becomes almost trivial.

### [54:55 - 54:58]

And so this is one failure case but I think it's also an opportunity

### [54:58 - 55:01]

if you're figuring out how can we extend this.

### [55:14 - 55:20]

So hopefully that provides some idea of some failure case as well.

### [55:20 - 55:23]

So hopefully that provides some idea of some failure case as well.

### [55:31 - 55:32]

Are there any other questions right now?

### [55:37 - 55:39]

It seems like they're not.

### [55:44 - 55:46]

Great. Well, as I mentioned at the beginning, if you have questions,

### [55:46 - 55:48]

shoot me an email. You can find it on my website.

### [55:48 - 55:50]

And thanks so much for having me. It's been really fun.

### [55:50 - 55:52]

Yeah. Thank you for this talk.

### [55:52 - 55:54]

Let's keep in touch.

### [55:54 - 55:56]

Maybe we'll join some of our later seminars as well.

### [55:56 - 55:58]

Yeah.

### [55:58 - 56:00]

And thanks everyone for joining.
