# Amy Zhang | Representations for Hierarchical Reinforcement Learning | May 30, 2025

- URL: https://www.youtube.com/watch?v=nyXXX3fIzMw
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T19:32:22`

## Transcript

### [00:00 - 00:30]

Thank you.

### [00:30 - 01:00]

Thank you.

### [01:00 - 01:30]

Thank you.

### [01:30 - 02:00]

Thank you.

### [02:00 - 02:30]

Thank you.

### [02:30 - 03:00]

Thank you.

### [03:00 - 03:30]

Thank you.

### [03:30 - 04:00]

Thank you.

### [04:00 - 04:00]

Thank you.

### [04:00 - 04:00]

Thank you.

### [04:00 - 04:00]

Thank you.

### [04:00 - 04:23]

Let's see, let me just try to share my screen.

### [04:23 - 04:27]

On the top right, the fourth icon.

### [04:27 - 04:30]

Yeah, okay.

### [04:30 - 04:32]

I think this one.

### [04:32 - 04:33]

Yeah.

### [04:33 - 04:34]

Great.

### [04:34 - 04:37]

And then, oops, that's not what I wanted to do.

### [04:37 - 04:39]

There, okay.

### [04:39 - 04:41]

Great.

### [04:41 - 04:51]

All right.

### [04:51 - 04:56]

People are coming and we can start on time.

### [04:56 - 04:57]

Okay.

### [04:57 - 05:08]

So, it looks like I can't, you know, if when I'm presenting, oh, actually, I guess, so,

### [05:08 - 05:11]

okay, I see, I can see the slides on.

### [05:11 - 05:12]

Yeah.

### [05:12 - 05:18]

If you have two screens, you can have this window on the one and the presentation on

### [05:18 - 05:19]

the other.

### [05:19 - 05:20]

Okay.

### [05:20 - 05:21]

Yeah.

### [05:21 - 05:26]

I am not currently set up with two screens, so I don't think I'll be able to do that.

### [05:26 - 05:27]

Maybe, yeah.

### [05:27 - 05:28]

No problem.

### [05:28 - 05:29]

I'll manage the session with you.

### [05:29 - 05:30]

If anyone wants to ask question, I give them microphone access and if the question was

### [05:30 - 05:31]

on the chat, I would read it.

### [05:31 - 05:32]

Okay.

### [05:32 - 05:33]

Sounds great.

### [05:33 - 05:34]

Yeah.

### [05:34 - 05:35]

And then, I'm also happy to take questions during the talk.

### [05:35 - 05:36]

So, feel free to just interrupt me.

### [05:36 - 05:37]

Sure.

### [05:37 - 05:38]

Sure.

### [05:38 - 05:39]

Okay.

### [05:39 - 05:40]

Okay.

### [05:40 - 05:41]

Okay.

### [05:41 - 05:42]

Okay.

### [05:42 - 05:43]

Okay.

### [05:43 - 05:44]

Okay.

### [05:44 - 05:45]

Okay.

### [05:45 - 05:46]

Okay.

### [05:46 - 05:47]

Okay.

### [05:47 - 05:48]

Okay.

### [05:48 - 05:49]

Okay.

### [05:49 - 05:50]

Okay.

### [05:50 - 05:51]

Okay.

### [05:51 - 05:52]

Okay.

### [05:52 - 05:53]

Okay.

### [05:53 - 05:54]

Okay.

### [05:54 - 05:55]

Okay.

### [05:55 - 05:56]

Okay.

### [05:56 - 05:59]

Just sending a message to everyone.

### [05:59 - 06:00]

Okay.

### [06:00 - 06:04]

I think we can start up.

### [06:04 - 06:05]

Hi.

### [06:05 - 06:06]

Okay.

### [06:06 - 06:08]

Welcome everyone and thank you, professor, for accepting our invitation.

### [06:08 - 06:17]

We are very honored to have you today for this wonderful talk and I think we can't have

### [06:17 - 06:18]

your attention.

### [06:18 - 06:19]

Okay.

### [06:19 - 06:20]

Awesome.

### [06:20 - 06:21]

Hi, everybody.

### [06:21 - 06:24]

So yeah, my name is Amy Zhang.

### [06:24 - 06:25]

Okay.

### [06:25 - 06:31]

in the ECE department at UT Austin. My work centers around reinforcement learning, learning

### [06:31 - 06:38]

abstractions for reinforcement learning, representation learning. And so today I wanted to talk about

### [06:38 - 06:45]

learning state in action abstractions and representations specifically for hierarchical

### [06:45 - 06:52]

reinforcement learning. So before we dive in, I just wanted to present a roadmap of what I want

### [06:52 - 06:59]

to talk about today. So first is why hierarchy, right? Why should we care about hierarchical

### [06:59 - 07:04]

reinforcement learning as opposed to just flat reinforcement learning where we're just

### [07:04 - 07:12]

learning a monolithic policy that tries to solve any specified task? Then I want to introduce some

### [07:12 - 07:17]

existing hierarchical methods and just talk a little bit about what are the different kinds

### [07:17 - 07:22]

of approaches that have been studied over the last few decades. And there is a bit

### [07:22 - 07:28]

of a divide or difference between kind of like the first methods that came about when people

### [07:28 - 07:33]

first started thinking about hierarchical reinforcement learning and then more modern

### [07:33 - 07:37]

methods, you know, when we started to do deep reinforcement learning and incorporate neural

### [07:37 - 07:45]

networks and gradient-based methods, there was a pretty drastic shift in terms of the type of

### [07:45 - 07:51]

hierarchical methods that people use. And I want to talk a little bit about the problems in some of

### [07:51 - 07:52]

those existing methods.

### [07:52 - 07:57]

And kind of the direction that I think we should be going in. Then I'm going to start to talk about

### [07:57 - 08:05]

some of our own work. We're going to dive deeper into a specific type of problem that hierarchy

### [08:05 - 08:11]

works really well in, which is relational MDPs or settings where you can assume that there's some

### [08:11 - 08:17]

set of common factors underlying the environment where we can hope to achieve compositional

### [08:17 - 08:22]

generalization. So compositionality and relational MDPs, a class of problems where

### [08:22 - 08:28]

hierarchy is well defined. Next, we're going to leverage this kind of factorized structure in

### [08:28 - 08:34]

relational MDPs with a hand-designed relational abstraction. So this is some work that I did

### [08:34 - 08:43]

pretty a while ago now, so in 2018. And so I just wanted to show how with a hand-designed

### [08:43 - 08:47]

abstraction, what is the kind of generalization that we can achieve, the kind of performance that

### [08:47 - 08:52]

we can achieve that is not possible with other learned hierarchical methods. So previous

### [08:52 - 08:59]

hierarchical methods as well as flat methods. But that relies on a very hand-designed

### [09:00 - 09:05]

abstraction, this kind of like relational abstraction. And so the next step is how can we

### [09:05 - 09:11]

relax that assumption that this nice abstraction is provided to us? So then I want to focus on how

### [09:11 - 09:16]

can we learn a factored abstraction and leverage it for hierarchical reinforcement learning?

### [09:17 - 09:22]

And then I want to end with what can we do if we can't assume factorized structure? So kind of

### [09:22 - 09:27]

this relational MDP setting, this setting where we can assume that there are these common underlying

### [09:27 - 09:33]

factors of the environment and talk about, you know, for just the very general setting where we

### [09:33 - 09:38]

have no assumptions about the environment, you know, what's possible? What can we do with

### [09:38 - 09:43]

hierarchical RL? Like why would we expect hierarchy to achieve better performance compared to just

### [09:43 - 09:51]

flat methods? And so before I get started, you know, I'm happy to take questions. I'm not really

### [09:53 - 09:58]

the background that the audience has on reinforcement learning. So, you know, if there's

### [09:58 - 10:04]

any kind of clarifying questions or if you're lost at all, if you just want to ask about something,

### [10:04 - 10:11]

you know, please feel free to interrupt me. Okay. And so with that, let's dive right in.

### [10:11 - 10:16]

So why hierarchy, right? So the problems that we want to focus on

### [10:17 - 10:22]

when we think about hierarchical reinforcement learning are long horizon problems.

### [10:22 - 10:26]

Typically that have sparse reward, which just means that there's no learning signal

### [10:26 - 10:31]

until we actually reach our goal, at which time we're being told, okay, great, you achieved,

### [10:31 - 10:36]

you solved this task, right? So long horizon tasks are very hard to solve because there's

### [10:36 - 10:42]

very sparse learning signal for the agent. And so the idea behind hierarchy is that there may

### [10:42 - 10:51]

be skills that can get reused, right? And so if we have these temporal skills, instead of just these

### [10:52 - 10:57]

abstractions, the task can be easier to solve when it's split up into different levels of

### [10:57 - 11:05]

abstraction. So just as like a very simple example, right? If I'm an agent and I'm on UT campus,

### [11:05 - 11:11]

and UT campus is pretty large because it's a pretty big school, and I'm told I want to go to,

### [11:13 - 11:18]

I want to go to this tower that's on UT campus. So how do I think about, how do I, how I,

### [11:22 - 11:28]

will I be able to do that? So you need very good tools and I mean the tools that you're

### [11:28 - 11:33]

looking for in the class are a lot of stuff. Also it's very important to understand that

### [11:33 - 11:39]

you won't, you know, the first tool in class, it's going to be the right tool for you,

### [11:39 - 11:43]

and it's going to be a good tool for you as well. So give it some time to look at it,

### [11:43 - 11:46]

because you're going to need to look at it for new ideas that you might want to be working on.

### [11:46 - 11:47]

Yeah.

### [11:47 - 11:50]

Do you, do you have any topics that you at UT have that you're really interested in,

### [11:50 - 11:52]

or one topic you want to talk about?

### [11:52 - 11:52]

Yeah, no problem.

### [11:52 - 11:52]

Thanks.

### [11:52 - 12:21]

I don't know what happened. Okay. Um did it just happen? I guess about five or ten

### [12:21 - 12:28]

seconds ago. Just let me start explaining this slide. Okay. Okay. Great. Uh that's okay. Yeah.

### [12:28 - 12:35]

Sorry. I noticed that the it seemed like the video had cut off. So I realized pretty quickly. Um

### [12:35 - 12:40]

all right. So hopefully that doesn't happen again. Um so what I was saying about this slide

### [12:41 - 12:46]

right is that if I'm given some I was providing an example of a long horizon problem

### [12:46 - 12:51]

where I'm an agent trying to navigate this big UT campus and I'm being told that I want to

### [12:51 - 12:56]

go to this tower that's in the middle of campus. And so in order to figure out like how should I

### [12:56 - 13:03]

get there maybe I can think of different waypoints along the route. One example is the CS building

### [13:03 - 13:09]

GDC. So maybe I can think about let me first get to the CS building and from there I can see the

### [13:09 - 13:14]

tower and then it becomes much easier to navigate there. Right. So this is an example of hierarchy

### [13:14 - 13:20]

where I can use this midpoint as it as a sub goal as as a first task to solve

### [13:20 - 13:28]

before I solve my overarching task which is to go to the tower. Okay. So um

### [13:30 - 13:36]

when I think about hierarchical reinforcement learning the underlying concept uh that I want

### [13:36 - 13:42]

to introduce is skills. These skill hierarchies. Right. So this base hierarchical control is on

### [13:42 - 13:48]

skills. So skills are a component of behavior. We're going to assume that they are performing

### [13:48 - 13:50]

continuous low level control.

### [13:51 - 13:56]

And we can think of each skill. We can just treat it as a discrete action. Each skill

### [13:56 - 14:02]

is the same thing as an action. And so we're basically replacing our continuous low level

### [14:02 - 14:07]

action space with this higher level action space corresponding to skills.

### [14:10 - 14:16]

And we want these skills to have the characteristics of being modular and compositional.

### [14:17 - 14:20]

Right. The idea is that we can compose these skills to

### [14:20 - 14:28]

work together in some order and that will give us a high level policy that allows us to complete our

### [14:28 - 14:37]

task. So in order to think about skills and creating hierarchies of skills we have to use

### [14:37 - 14:42]

abstractions. And so when we talk about hierarchical RL we need two different types of

### [14:42 - 14:49]

abstraction. We need a state abstraction which is just a mapping from the state space that's provided

### [14:49 - 14:49]

to us.

### [14:49 - 14:56]

In that previous example of the agent or robot on UT campus, the state space is very likely going to

### [14:56 - 15:03]

just be the pixel images that the robot sees. We're assuming that the robot has just a camera

### [15:03 - 15:08]

that it's using to perceive the world. And so the state space corresponds to those pixel images that

### [15:08 - 15:19]

it's receiving about the world. And the action space for the robot, it can vary in robotics. But

### [15:19 - 15:28]

it's a very simple example. It could just be like low level actuators. So the actual forces

### [15:28 - 15:33]

being applied to each joint in order for the robot to be able to move. And so what we would like to

### [15:33 - 15:39]

do is abstract that action space into some higher level run, into a higher level one. Right. So now

### [15:39 - 15:48]

we have some discrete action space that is composed of skills. And so one example of this higher level

### [15:48 - 15:49]

action space could be being able to take steps.

### [15:49 - 15:54]

Right. So if we have a humanoid robot, instead of thinking of the action space as just

### [15:54 - 16:00]

forces on the joints, we can instead think of it as like, I want to go 10 steps north or 10 steps

### [16:00 - 16:06]

south or 10 steps east or west. Right. So now this problem can contain subproblems. And each

### [16:06 - 16:13]

of these subproblems is now also an RL problem. So it is an RL problem to figure out how do I

### [16:13 - 16:19]

actually walk 10 steps to the north or to the south. But then the higher level

### [16:19 - 16:23]

problem is also still an RL problem. If I know how to walk 10 steps in each direction,

### [16:23 - 16:33]

how do I get to the bell tower? Right. So in 1999, Sutton introduced the options framework.

### [16:34 - 16:41]

And the key idea is just options. So this is just another way to define skills. And these are

### [16:42 - 16:48]

so options have a very concrete definition. Right. Whereas like skill is something that we kind of

### [16:49 - 16:55]

sense of, but we don't necessarily have a concrete definition for. So options are temporally

### [16:55 - 17:02]

extended actions that consist of a policy, a termination condition, and an initiation set.

### [17:02 - 17:08]

So it has these three components. And so I have just this example problem on the bottom right

### [17:08 - 17:12]

hand here. Right. Where I have this two room environment, this grid world environment.

### [17:13 - 17:17]

And my goal is just this dot in the bottom

### [17:17 - 17:25]

right hand corner in the second room. And I would like to go through this hallway

### [17:25 - 17:30]

in order to get to this goal. So that's my high level problem. That's the task

### [17:30 - 17:38]

as it's been specified for my agent. So one example of a skill is can be shown here on top.

### [17:38 - 17:42]

So maybe instead of trying to reach this bottom corner,

### [17:42 - 17:46]

I just want to try to reach this hallway first. Right. So this is now an example of a midpoint

### [17:47 - 17:55]

that can be used to define a skill. And so these arrows just represent the action that my policy

### [17:56 - 18:01]

would take at every state. So here in every state in this one room,

### [18:03 - 18:10]

we have actions that have been assigned to each state. And so you can see if my agent

### [18:10 - 18:17]

were in any one of these states, it's basically being herded to go into this hallway. And there are

### [18:17 - 18:24]

no arrows on the room on the right side because the skill is only defined for this one room.

### [18:25 - 18:30]

Right. So if I think about that skill, under the options framework,

### [18:31 - 18:37]

and an option is just one formal model of a skill, my initiation set consists of,

### [18:39 - 18:47]

so it's this green circle here, all of the states in this room on the left. My termination condition

### [18:48 - 18:57]

is just reaching this hallway state. And my option policy corresponds to those arrows,

### [18:57 - 19:03]

telling me what action I should take when I'm in any of those states on this left-hand side.

### [19:06 - 19:14]

So our low-level actions can also be defined as options. A primitive action can be represented

### [19:14 - 19:17]

as an option. And it can be as follows. Right. So our

### [19:17 - 19:24]

initiation set is just at every state, right, we can take that action. So it's always one.

### [19:26 - 19:31]

Our termination happens after just that one step is taken. So our termination condition

### [19:31 - 19:38]

is also always one. And our policy is just to always take that one action, A.

### [19:39 - 19:45]

Right. So a primitive action, so what this is saying is a primitive action can be executed

### [19:45 - 19:45]

anywhere, lasts exactly one, eight years. Right. So a primitive action can be executed anywhere,

### [19:45 - 19:47]

lasts exactly one, eight years. And so on, eight years, it can be executed anywhere, lasts exactly

### [19:47 - 19:53]

one time step and always chooses action a so that's how i can convert our low level actions

### [19:54 - 20:00]

into options so let's look at another example so now we have this four room environment

### [20:00 - 20:06]

our low level actions consists of these four stochastic primitive actions up down left right

### [20:06 - 20:13]

and i'm going to fail 33 of the time so so that's uh that's what introduces the stochasticity of

### [20:13 - 20:21]

the dynamics and for this four room environment i'm also going to define eight multi-step options

### [20:21 - 20:27]

and those consist of reaching any of the two hallways from uh the two hallways from any room

### [20:28 - 20:36]

right so here's one two three four five six seven eight right so those are my eight options is to

### [20:36 - 20:43]

reach the hallways and so this is an example of one of those options to reach

### [20:43 - 20:49]

a target hallway so my primitive options would just correspond to

### [20:50 - 20:59]

those four stochastic one-step actions right so if my goal corresponds to reaching this hallway point

### [21:01 - 21:07]

this is an example of what my initial values are so my initial value function says i know

### [21:07 - 21:12]

that i'm going to receive high value if i can reach this goal and i don't know anything anywhere

### [21:13 - 21:19]

else i don't know what my values are for any other state at my first iteration i've taken i can take

### [21:19 - 21:24]

one step in any direction from the goal and propagate those values so now i know that these

### [21:24 - 21:29]

two values are also high because my actions are only up down left right i couldn't go left right

### [21:29 - 21:36]

here so it's only up down um and so at my iteration two i can go one step further right and

### [21:36 - 21:42]

so you can see that the value function uh the values that we can learn propagate very slowly

### [21:42 - 21:49]

if our options only correspond to those low-level actions so now let's look at an example where our

### [21:49 - 21:56]

option set only consists of those hallway options right and so it's nice that our goal is actually

### [21:56 - 22:03]

in a hallway because now we can see that if our our options correspond to um every room that's

### [22:03 - 22:10]

reachable from that hallway i can propagate my values much more quickly right so after one

### [22:10 - 22:12]

iteration i've assigned values to my options

### [22:12 - 22:18]

all of the states in these two rooms and at iteration two i've basically solved my entire

### [22:18 - 22:25]

problem because i've assigned values to now all four rooms but we were lucky because our goal

### [22:25 - 22:30]

corresponded to a hallway which was already a termination condition of one of the options

### [22:31 - 22:36]

so what would happen if our goal was instead in the middle of one of these rooms

### [22:37 - 22:41]

then if our options if our action space only consists of those

### [22:41 - 22:42]

eight hallway options

### [22:43 - 22:47]

we actually can't solve this problem because we can never end up in the middle of the room

### [22:47 - 22:51]

we always end up we always terminate in a hallway

### [22:53 - 23:00]

so the solution is to combine both our low-level actions and our hallway uh options

### [23:00 - 23:06]

into our set of options into our into our new high-level abstract action space

### [23:07 - 23:12]

right so now if my goal is just the middle of the groom the

### [23:12 - 23:18]

sorry the middle of the room i can still use my low-level actions to explore

### [23:20 - 23:24]

around that goal to to propagate my value estimates around that goal

### [23:24 - 23:29]

so at iteration one i'm just going to use my low-level actions because i can't

### [23:29 - 23:34]

use my high-level ones yet and at iteration two i've reached a hallway

### [23:34 - 23:41]

so now i can start using my options and explore much more quickly and now i can again solve this

### [23:41 - 23:41]

problem in just a few acts so looking at this example here i'm able to solve this problem with

### [23:41 - 23:41]

lps architectingand here's how i can solve this problem in slightly faster and more application decisions rather than do it in just a few times so be rich Play run model tool actually can see if there's change in

### [23:41 - 23:49]

in just a few iterations and so I just want to provide one more example right

### [23:49 - 23:54]

so if I have this option a which is just starting its initiation set only

### [23:54 - 23:59]

consists of this one state sorry two states these two states and it's going

### [23:59 - 24:07]

to go it's going to this this hallway at the top and I have another option that

### [24:07 - 24:11]

starts from these three states and goes to the hallway on the right I can

### [24:11 - 24:16]

combine these into a policy right so this policy basically says I'm going to

### [24:16 - 24:23]

take option a first and then option B I want to note that policies made up of

### [24:23 - 24:32]

options are not necessarily Markovian right because they may use history in

### [24:32 - 24:37]

order to or basically to replicate this policy using just low-level actions we

### [24:37 - 24:41]

may need history and that's something that gets talked

### [24:41 - 24:41]

about a lot of the time and I think that's something that's really important

### [24:41 - 24:46]

about actually in Sutton's paper so he calls this setting the semi-MDP setting

### [24:46 - 24:53]

because it's only semi-Markovian but we're not going to get into that all

### [24:53 - 24:57]

right so now I just want to jump into modern hierarchical RL methods right so

### [24:57 - 25:04]

in 2017 Pierre-Luc Bacon introduced option critic so this learns both intra

### [25:04 - 25:09]

option policies and termination conditions so what option critic is

### [25:09 - 25:11]

doing is it takes a

### [25:11 - 25:18]

flat after critic method and propagates those gradients for learning the high

### [25:18 - 25:24]

level task to an architecture that is going to also learn these intermediate

### [25:24 - 25:30]

options so the problem with that is that we're still the learning signal all

### [25:30 - 25:36]

comes from the original task right which is can be long Horizon sparse reward and

### [25:36 - 25:39]

very difficult which means that most of the time there's very little learning

### [25:39 - 25:40]

signal that is actually going to

### [25:40 - 25:44]

come from learning those options so it turns out that this method is actually

### [25:44 - 25:49]

pretty unstable and tends to collapse to single action options so it just reverts

### [25:49 - 25:54]

back to trying to solve it as a flat problem they get around this with a follow-up work

### [25:54 - 25:59]

where they actually add in a regularization term to try to encourage these options to be longer

### [26:00 - 26:05]

but it's still not getting around the problem that all of the learning signal is still coming

### [26:05 - 26:10]

from the original task right and that means that most of the time you're not actually receiving any

### [26:10 - 26:16]

reward hierarchical dqn does something very similar but it's just combining that options

### [26:16 - 26:22]

framework now with dqn instead of actor critic but here we have a high level policy that's

### [26:22 - 26:25]

choosing sub goals and a low level policy that is trying to achieve those sub goals

### [26:28 - 26:34]

so what's missing these methods still use the environment reward to learn options so like I

### [26:34 - 26:39]

said this is still a very um very difficult task because long Horizon problems are hard

### [26:40 - 26:43]

to figure out so methods are learning another problem is that these methods are learning both

### [26:43 - 26:49]

high-level and low-level policies simultaneously but the problem with hierarchical RL is that your

### [26:49 - 26:55]

high-level policy depends on what your low-level policies are so with these methods that are passing

### [26:55 - 27:00]

gradients back through both the low level and high-level policies at the same time and are

### [27:00 - 27:07]

training them at the same time is that your high-level policy can never converge while your

### [27:07 - 27:10]

low-level policies have not converged in our society at that we are actually learning things very slow and

### [27:10 - 27:14]

still updating right because if your low-level actions are constantly changing over time

### [27:15 - 27:18]

you can't figure out what your high-level policy should be

### [27:20 - 27:25]

so one solution to this problem is to try to separate out learning the low-level policies

### [27:25 - 27:30]

from the high-level ones so instead of defining low-level policies based on the high-level task

### [27:30 - 27:37]

and the high-level policy instead we can pre-define low-level policies so one example of how to define

### [27:37 - 27:41]

these low-level policies is as just goal condition policies that can be trained separately

### [27:43 - 27:49]

so goal conditioned RL is a type of self-supervised reinforcement learning where

### [27:50 - 27:56]

the agent is being trained to solve a number of tasks or just which just means reach various

### [27:56 - 28:01]

state goals within the same environment so we can always just sample the goal at the beginning

### [28:01 - 28:06]

of the episode and it's sampled as just some state from our state space

### [28:07 - 28:14]

and our reward can be predefined to be the sparse reward where we get a zero when we reach the goal

### [28:14 - 28:19]

and negative one otherwise so you can see that with this reward function we're trying to learn

### [28:19 - 28:28]

policies that try to reach the goal in the shortest number of steps possible okay so based

### [28:28 - 28:33]

on this idea that we want to learn goal conditioned low-level tasks there have been other

### [28:33 - 28:36]

modern hierarchical RL methods

### [28:37 - 28:42]

so one is hero which is hierarchical reinforcement learning with off policy correction

### [28:42 - 28:50]

so this is just learning off policy it's training the low-level goal condition policies

### [28:50 - 28:55]

with off policy training and goal relabeling so goal relabeling is just a way to introduce

### [28:55 - 28:59]

additional learning signal to make that goal condition problem a little bit easier

### [29:00 - 29:07]

so we are collecting our experience we're training our low-level goal condition policy

### [29:08 - 29:12]

but also some ELL for example where you're already learning the low-level goal condition

### [29:12 - 29:14]

and now we have a predefined reward for our low-level policies

### [29:14 - 29:23]

where this reward is not the high-level task reward so it's not that really difficult sparse

### [29:23 - 29:31]

reward anymore we now have this goal conditioned reward that's defined as follows and then once we

### [29:31 - 29:36]

train these low-level goal condition policies we can train a high-level policy that provides goals

### [29:36 - 29:43]

level policy to reach. So that's what hero is doing. Diane is another method also from 2018

### [29:43 - 29:50]

that doesn't rely on goal condition policies, but it also has another way of learning low level

### [29:50 - 29:59]

policies or skills independently of the high level policy. So here, instead of doing goal

### [29:59 - 30:05]

condition RL, they're actually using an objective by maximizing mutual information between latent

### [30:05 - 30:12]

variables, those skills and state transitions. So what that means is from any state,

### [30:12 - 30:17]

they want there to be a specific skill that is tied to that state.

### [30:18 - 30:23]

They also have another objective that is minimizing the mutual information between those

### [30:23 - 30:28]

skills and actions, right? So with these two mutual information based objectives

### [30:28 - 30:35]

and also incorporating diversity, so they try to learn these skills to minimize mutual information

### [30:35 - 30:35]

between each other. So they're trying to minimize the mutual information between each other.

### [30:35 - 30:42]

other between each of these skills they can learn several unique skills that span the entire state

### [30:42 - 30:51]

space so this so this algorithm diane and diversity is all you need is basically a way of

### [30:51 - 30:56]

using mutual information to learn several low-level skills that are diverse and span the entire state

### [30:56 - 31:02]

space and once you have these skills you can freeze them and then train a high-level policy

### [31:02 - 31:11]

on top to for any kind of downstream task right so these are task agnostic options right because

### [31:11 - 31:16]

we have we've defined some other self-supervised objective that's not task dependent

### [31:17 - 31:20]

to learn these low-level policies to learn these options

### [31:21 - 31:27]

either through a k-step goal condition policy which is what hero is doing or some other

### [31:27 - 31:31]

self-supervised objective based on mutual information which is what diane is doing

### [31:33 - 31:40]

so this is better right because now we don't have that instability we don't have uh this issue where

### [31:40 - 31:45]

the high-level policy has to wait for low-level policies to stabilize we've decoupled learning

### [31:45 - 31:51]

these two levels of hierarchy but we have another problem which is that these methods do not promote

### [31:51 - 32:01]

skill reuse right each of these skills corresponds to a specific goal or a specific state we don't

### [32:01 - 32:02]

know how to do that

### [32:02 - 32:08]

so let's look at how to use the the same skill many times from different states

### [32:10 - 32:14]

so as just an example of what we would like to achieve let's go back to this four-room example

### [32:15 - 32:20]

right um so okay sorry this example is maybe not great because each of these rooms is a slightly

### [32:20 - 32:26]

different shape but let's imagine that all the rooms are the same size are identical to each

### [32:26 - 32:31]

other but we just have these four rooms in that case navigating within each room

### [32:31 - 32:37]

or to the hallways from within each room is exactly the same we would like to be able

### [32:37 - 32:44]

to reuse those two hallway options right of of going to each of these hallways from any room

### [32:45 - 32:51]

uh we we would like for there to only be two options and the idea is that we can reuse those

### [32:51 - 32:58]

options from within any room right that would be an example of skill reuse that should be possible

### [32:59 - 33:00]

so now let's talk about skill reuse professor lrupal will teach us about skill reuse and skill reuse and skill reuse against renewable energy bags and kissing as it points into navigation and yet another thing we're looking forward to is the world of lockouts in the future or wasесть poor consumption of roofs housing day之前 we don't have access to access to jobs and lights even though this system is clean during the continuity or even if the interidor is open it's thisiendo by them low

### [33:00 - 33:06]

So now let's talk about a broader setting where this type of reuse is expected, right?

### [33:06 - 33:12]

So it's pretty clear from that one example of this four-room grid world where we can

### [33:12 - 33:19]

expect reuse, but what is a broader class of environments where we can define these

### [33:19 - 33:22]

kinds of reusable options?

### [33:22 - 33:30]

So it turns out that there's a whole class of problems based around compositionality,

### [33:30 - 33:36]

which just means that there's a type of generalization that we should expect in these kinds of compositional

### [33:36 - 33:37]

environments.

### [33:37 - 33:42]

And compositionality comes from this idea that you have these low-level factors, right?

### [33:42 - 33:44]

So in this example, it's these blocks.

### [33:44 - 33:46]

All of these blocks behave in the same way.

### [33:46 - 33:51]

The physics is the same for each block, but it can always create more and more new environments

### [33:51 - 33:52]

with different combinations.

### [33:52 - 33:56]

Same with driving, right?

### [33:56 - 34:01]

I can kind of simplify the autonomous driving problem by thinking of each car as basically

### [34:01 - 34:04]

the same in terms of its dynamics.

### [34:04 - 34:10]

And it turns out that there are benchmarks for that create these procedurally generated

### [34:10 - 34:13]

environments to test compositional generalization.

### [34:13 - 34:18]

So all of these games are ones where we can create an almost infinite number of different

### [34:18 - 34:21]

levels or different environments.

### [34:21 - 34:22]

By creating.

### [34:22 - 34:23]

Different layouts.

### [34:23 - 34:28]

But the underlying rules of these games are always still the same, right?

### [34:28 - 34:31]

So all of these correspond to these real-world problems, which is why we should care about

### [34:31 - 34:34]

compositionality.

### [34:34 - 34:40]

So a way to achieve compositional generalization is I've kind of already hinted at is factorization

### [34:40 - 34:46]

is how can we recognize that in these environments, there are these common factors and each factor,

### [34:46 - 34:50]

the dynamics of each factor behave the same, which is how we can achieve this generalization.

### [34:50 - 34:51]

Okay.

### [34:51 - 34:57]

So there's actually this really nice paper and on compositionality decomposed, how do

### [34:57 - 35:03]

neural networks generalize that tries to define different types of compositional generalization

### [35:03 - 35:06]

that we should strive to achieve.

### [35:06 - 35:12]

And actually this paper was focused on generalization in the language setting for natural language

### [35:12 - 35:13]

processing.

### [35:13 - 35:17]

But I think a lot of these ideas actually apply really well to reinforcement learning

### [35:17 - 35:18]

or robotics.

### [35:18 - 35:19]

Okay.

### [35:19 - 35:20]

So the first of these is systematicity.

### [35:20 - 35:20]

Okay.

### [35:20 - 35:24]

So the first of these is systematicity, which is generalization by recombining known parts

### [35:24 - 35:25]

and rules, right?

### [35:25 - 35:30]

So if I have these four rules, I can take these two rules and combine them and achieve

### [35:30 - 35:33]

and design some new rule.

### [35:33 - 35:39]

Productivity, the ability to extend predictions beyond the length seen in training data, right?

### [35:39 - 35:46]

So here, if I've seen these two components, this length two trajectory, let's say, or

### [35:46 - 35:50]

this length three trajectory, I can combine them together and still understand what this

### [35:50 - 35:51]

means.

### [35:51 - 35:52]

Substitutivity, which is generalization to replace components with synonyms.

### [35:52 - 36:01]

So if I know that these two things are equivalent, I can replace one with the other and know

### [36:01 - 36:04]

that it still means the same thing in this combination.

### [36:04 - 36:10]

Localism, if model composition operations are local versus global.

### [36:10 - 36:16]

And overgeneralization, which is if models pay attention to or are robust to exceptions.

### [36:16 - 36:20]

So this, I think, is maybe more applicable in language where in the language setting,

### [36:20 - 36:25]

you know, we have, like, rules of grammar and they don't and sometimes those rules

### [36:25 - 36:28]

get broken in colloquial language.

### [36:28 - 36:32]

Maybe doesn't apply as much to physics in the real world.

### [36:32 - 36:34]

All right.

### [36:34 - 36:42]

So one way to define this kind of factored structure in an MDP is with a relational MDP.

### [36:42 - 36:48]

So this is a subset of the general MDP definition where we now are defining a set of classes

### [36:48 - 36:50]

that denote different object types.

### [36:50 - 36:58]

So here we have an example of these trucks that are trying to navigate around the city

### [36:58 - 37:01]

and deliver boxes from one place to another.

### [37:01 - 37:02]

All right.

### [37:02 - 37:06]

So we have classes that denote the different types of objects that belong in this MDP.

### [37:06 - 37:09]

So box, truck, or city.

### [37:09 - 37:12]

We have schemata that take these objects as input.

### [37:12 - 37:19]

So maybe we can bin together box and city or we can put a box on a truck.

### [37:19 - 37:20]

Okay.

### [37:20 - 37:23]

A set of action schemata that operate on those objects.

### [37:23 - 37:30]

So we want to unload the box from this truck in this city, load, drive, et cetera.

### [37:30 - 37:34]

And then within every environment, we have a set of domain objects where each object

### [37:34 - 37:39]

is comprised of a single type from C. And then otherwise we still have our standard

### [37:39 - 37:43]

components from our MDP, which is our transition function in our reward model.

### [37:43 - 37:44]

All right.

### [37:44 - 37:48]

So this is a definition of a relational MDP where we can see that, you know, from one

### [37:48 - 37:49]

city to a next.

### [37:49 - 37:53]

Even though there are things that change, all of these things stay the same.

### [37:53 - 37:55]

The rules over them stay the same.

### [37:55 - 37:58]

And we should be able to generalize to different cities.

### [37:58 - 38:01]

Okay.

### [38:01 - 38:07]

So with that, now that we're kind of focusing on this factored setting and we're trying

### [38:07 - 38:12]

to focus on compositional generalization, I want to talk about a way in which we can

### [38:12 - 38:17]

use hierarchical learning in order to get this type of generalization.

### [38:17 - 38:19]

So in this work, the inspiration was.

### [38:19 - 38:21]

It was about stacking blocks.

### [38:21 - 38:27]

So this is one example where it's very easy to see that the factors correspond to these

### [38:27 - 38:33]

blocks and we can have very difficult tasks that correspond to moving these objects, these

### [38:33 - 38:36]

blocks around in specific orders.

### [38:36 - 38:38]

And so we'd like to be able to reach any goal.

### [38:38 - 38:43]

So this is a huge task space with combinatorially many possible goals.

### [38:43 - 38:48]

And so some real world examples of this are being able to build Lego structures or performing

### [38:48 - 38:49]

tasks.

### [38:49 - 38:52]

Any kind of real time strategy game.

### [38:52 - 38:56]

And so where we'd like to start out is that you may not know at training time, which goals

### [38:56 - 38:57]

are important.

### [38:57 - 38:58]

Right.

### [38:58 - 39:01]

And we also already established in hierarchical reinforcement learning, why this is important,

### [39:01 - 39:07]

why we would like to separate the low level policy learning from the high level task.

### [39:07 - 39:09]

Okay.

### [39:09 - 39:14]

So the standard RL approach would be to just learn a flat policy.

### [39:14 - 39:18]

So being given a representation of the goal space, we want to be able to train a policy

### [39:18 - 39:19]

to reach any goal.

### [39:19 - 39:26]

Using RL instead, we want to learn how to make local transitions in goal space and then

### [39:26 - 39:29]

plan over the transition graph.

### [39:29 - 39:33]

And so being able to do this planning over a graph, and by this, I just mean do graph

### [39:33 - 39:36]

search like Dijkstra or A star.

### [39:36 - 39:41]

This allows us to get zero shot generalization from short to long tasks and is a way for

### [39:41 - 39:47]

us to naturally define a hierarchy where our low level tasks just course our low level

### [39:47 - 39:49]

policies correspond to.

### [39:49 - 39:54]

These local transitions and the high level policies performing this kind of longer term

### [39:54 - 39:58]

search.

### [39:58 - 40:05]

So in order to achieve this, instead of operating from low level states and actions, we want

### [40:05 - 40:12]

to provide a better state abstraction that allows us to predefine these low level skills.

### [40:12 - 40:18]

We want to provide the attributes of the environment that we care about to promote skill reuse.

### [40:19 - 40:23]

And then our agent can use unsupervised exploration to learn how to modify these attributes in

### [40:23 - 40:25]

the environment.

### [40:25 - 40:29]

And then it'll use these attributes or this state abstraction to specify a goal and a

### [40:29 - 40:31]

space for planning.

### [40:31 - 40:35]

So what is this abstraction that we want?

### [40:35 - 40:40]

What are the traits of this abstraction that will allow us to have skill reuse?

### [40:40 - 40:43]

So these are going to be a high level set of high level features or properties of the

### [40:43 - 40:46]

state that users care about.

### [40:46 - 40:47]

Right?

### [40:47 - 40:48]

And so one of.

### [40:48 - 40:49]

One example.

### [40:49 - 40:53]

One property that we care about for the block stacking task is which block is which.

### [40:53 - 40:55]

And so here we're going to distinguish that based on color.

### [40:55 - 40:56]

It can be on color.

### [40:56 - 41:01]

It can be on shape or texture, depending on what kind of variations you have in your environment.

### [41:01 - 41:05]

In this very simple example, it's just going to be color.

### [41:05 - 41:09]

And so each property is going to be a binary function of the state, right?

### [41:09 - 41:10]

So red is stacked on blue.

### [41:10 - 41:12]

Green is not stacked on blue.

### [41:12 - 41:14]

The yellow is to the right of blue.

### [41:14 - 41:18]

So these are all examples of attributes about the environment that we care about.

### [41:19 - 41:24]

So we have predefined this set of attributes, these relational attributes, that basically

### [41:24 - 41:33]

tell us what block is to the so between every two blocks, we have information about if it's

### [41:33 - 41:37]

to the left of, to the right of, on top of, or below each other.

### [41:37 - 41:38]

Right?

### [41:38 - 41:40]

So these are our relational attributes.

### [41:40 - 41:44]

So we're going to define.

### [41:44 - 41:48]

We're going to train a neural net that can detect these attributes.

### [41:48 - 41:52]

Detect these attributes from these pixel images, right?

### [41:52 - 42:00]

So it's going to take in a pixel image and give us those nice attributes that we've predefined.

### [42:00 - 42:04]

We can then build a graph of reachable attributes and edges between them.

### [42:04 - 42:09]

So we're going to take every transition that we see in our data set, you know, of, of these

### [42:09 - 42:15]

blocks moving around and build a graph based on those attributes.

### [42:15 - 42:17]

And then we also need to train a neural network.

### [42:17 - 42:22]

This low-level policy that knows how to reach nearby attribute sets, right?

### [42:22 - 42:29]

So now this, this attribute space and building this graph from our data set allows us to

### [42:29 - 42:37]

predefine a set of skills or options or these low-level policies, right?

### [42:37 - 42:42]

So this is how we've kind of now defined our hierarchy.

### [42:42 - 42:46]

So given a current state and goal attributes.

### [42:46 - 42:47]

Okay.

### [42:47 - 42:55]

This goal attributes is being specified as I want my red block to be above my blue block

### [42:55 - 42:59]

to be above my yellow block to be above my green block, right?

### [42:59 - 43:03]

I can now predict the current attributes row zero.

### [43:03 - 43:11]

So I'm going to take that this, this learned attribute detector F and I'm going to predict

### [43:11 - 43:15]

my current attributes from my initial pixel state.

### [43:15 - 43:17]

I'm going to take that graph that I've built.

### [43:17 - 43:25]

And find the sequence of transitions that allow me to match my goal attributes, right?

### [43:25 - 43:30]

And so you can think of this as the high-level policy or a high-level policy is being found

### [43:30 - 43:33]

just through search.

### [43:33 - 43:41]

And now I can use my low-level policy to try to reach each of these sub goals.

### [43:41 - 43:46]

So each step in this high-level path that I've found through graph search.

### [43:46 - 43:47]

Okay.

### [43:47 - 43:52]

I can now use my low-level policy to reach each of these, right?

### [43:52 - 43:55]

So this is how my hierarchy is defined.

### [43:55 - 43:58]

Once I executed the first step in the path with my low-level policy, I'm going to go

### [43:58 - 43:59]

back to one.

### [43:59 - 44:07]

I'm going to replan because I can't always guarantee that I've actually achieved this

### [44:07 - 44:08]

next sub goal, right?

### [44:08 - 44:14]

So once I, whatever state that I end up at, I'm going to go back to one and I'm going

### [44:14 - 44:17]

to research in my graph again.

### [44:17 - 44:21]

And basically, call my high-level policy again.

### [44:21 - 44:23]

Okay.

### [44:23 - 44:27]

So all of these components can just be trained with supervised learning.

### [44:27 - 44:32]

So the attribute detector, we just train on a small number of labeled examples.

### [44:32 - 44:38]

This graph, once we have those attributes, we just take actions with an exploratory policy.

### [44:38 - 44:45]

And then add to our graph as we explore more of the environment.

### [44:45 - 44:47]

And then our low-level policy, we actually train with this.

### [44:47 - 44:48]

With inverse training.

### [44:48 - 44:50]

Although this part, I would say, doesn't really matter.

### [44:50 - 44:52]

You can use goal condition reinforcement learning.

### [44:52 - 44:55]

You can use an inverse model.

### [44:55 - 44:57]

It doesn't matter how we train the low-level policy.

### [44:57 - 45:02]

It's just the interesting thing here is how it's been defined, right?

### [45:02 - 45:09]

So in these block stacking experiments, so we have our method, the attribute planner.

### [45:09 - 45:12]

And we first compare against just flat reinforcement learning methods.

### [45:12 - 45:15]

So here we have A3C.

### [45:15 - 45:17]

And we train it with various types of training data.

### [45:17 - 45:22]

So we train it on just one-step data.

### [45:22 - 45:25]

We train it on multi-step trajectories.

### [45:25 - 45:30]

And then we also try to provide a curriculum where we gradually increase the difficulty

### [45:30 - 45:34]

and length of the tasks that we train with A3C.

### [45:34 - 45:39]

So when we try to generalize from just, like, one-step tasks to multi-step, we only get

### [45:39 - 45:43]

8% success rate.

### [45:43 - 45:46]

When we try to train on multi-step directly.

### [45:46 - 45:47]

And then evaluate on multi-step.

### [45:47 - 45:50]

We actually get 0%.

### [45:50 - 45:55]

And so this is because flat RL on this kind of long horizon sparse reward problem is just

### [45:55 - 45:56]

too hard.

### [45:56 - 45:58]

And so it's just not able to achieve any learning signal.

### [45:58 - 46:02]

And so that's why it doesn't get any good performance.

### [46:02 - 46:07]

We actually see much better performance, relatively good performance with a curriculum, right?

### [46:07 - 46:10]

So where we gradually go from one step to multi-step.

### [46:10 - 46:14]

And we are able to achieve 17% success on multi-step problems.

### [46:14 - 46:16]

But with our method.

### [46:16 - 46:20]

By using this kind of graph search and this hierarchy and this abstraction, we're able

### [46:20 - 46:25]

to achieve 66% success rate.

### [46:25 - 46:27]

So we also compare against other hierarchical methods.

### [46:27 - 46:36]

So if you remember, option critic is still learning options using the original task learning

### [46:36 - 46:37]

signal.

### [46:37 - 46:41]

Which is why we see that we get still very low success rates, right?

### [46:41 - 46:44]

Because that problem is basically just as hard as learning flat RL.

### [46:44 - 46:45]

Right?

### [46:46 - 46:50]

From multi-step tasks.

### [46:50 - 46:52]

So option critic doesn't perform well.

### [46:52 - 46:58]

And then here, inverse is just an inverse model trained with supervised learning.

### [46:58 - 47:04]

Which means that we don't expect this to be able to outperform the behavior of the training

### [47:04 - 47:05]

policy.

### [47:05 - 47:07]

But we're still able to get decent performance here.

### [47:07 - 47:12]

But nothing compared to our attribute planner.

### [47:12 - 47:14]

We also perform an ablation.

### [47:14 - 47:15]

So this is an attribute planner.

### [47:15 - 47:19]

Without our graph transition table.

### [47:19 - 47:21]

So I kind of skipped over this.

### [47:21 - 47:28]

But our graph, we're assuming that that graph doesn't have 100% success rate across each

### [47:28 - 47:29]

transition.

### [47:29 - 47:30]

Right?

### [47:30 - 47:32]

Because it depends on the performance of the low-level policy.

### [47:32 - 47:37]

So we are taking that the performance of the low-level policy into account with our method.

### [47:37 - 47:40]

And if we don't, we achieve much lower performance.

### [47:40 - 47:45]

But you can still see that we're still achieving much better performance with our table.

### [47:45 - 47:49]

Type of hierarchical method compared to all these other methods before.

### [47:49 - 47:52]

Okay.

### [47:52 - 47:57]

So multi-step is just kind of randomly generated goals.

### [47:57 - 47:59]

Four stack is a much harder problem.

### [47:59 - 48:03]

Where we're trying to create a stack of four blocks.

### [48:03 - 48:05]

One on top of another.

### [48:05 - 48:09]

And then underspecified is another interesting setting where we're saying we don't necessarily

### [48:09 - 48:11]

care where all the blocks are.

### [48:11 - 48:14]

We're only going to specify some subset of the blocks.

### [48:14 - 48:15]

Right?

### [48:15 - 48:19]

And we're still able to achieve much better performance in that setting as well.

### [48:19 - 48:21]

We have additional experiments in grid world.

### [48:21 - 48:26]

So I'm going to skip over these because I still have quite a bit I want to talk about.

### [48:26 - 48:27]

And StarCraft.

### [48:27 - 48:28]

Right?

### [48:28 - 48:33]

So the StarCraft is, again, an example of a game where there's a lot of procedural generation.

### [48:33 - 48:38]

And so, again, we see that standard reinforcement learning methods.

### [48:38 - 48:41]

So here we're just using reinforce.

### [48:41 - 48:43]

Achieve much lower performance in our method.

### [48:43 - 48:44]

Okay.

### [48:44 - 48:45]

Okay.

### [48:45 - 48:46]

Okay.

### [48:46 - 48:50]

So just to recap, the right abstraction leads to compositional generalization.

### [48:50 - 48:56]

So by introducing this relational attribute, we are able to achieve better generalization

### [48:56 - 49:00]

compared to standard RL methods.

### [49:00 - 49:06]

This relational abstraction naturally breaks down these problems into hierarchical ones.

### [49:06 - 49:13]

But this is still relying on an assumption that this nice relational attributes is predefined.

### [49:13 - 49:14]

So what do we do?

### [49:14 - 49:17]

We're not being given these relational attributes.

### [49:17 - 49:22]

Or maybe we just can't predefine them for some problem space.

### [49:22 - 49:26]

So here's one relaxation of the previous problem.

### [49:26 - 49:31]

Where instead of assuming that those relational attributes are provided, we'd like to discover

### [49:31 - 49:34]

them from pixels directly.

### [49:34 - 49:36]

Right?

### [49:36 - 49:40]

So now we have this set of problems that we'd like to solve.

### [49:40 - 49:42]

First, we'd like to extract factors from the environment.

### [49:42 - 49:43]

First, we'd like to extract factors from the environment.

### [49:43 - 49:47]

Assuming that we're not given them ahead of time.

### [49:47 - 49:51]

But we're assuming that these factors still exist.

### [49:51 - 49:55]

The correspondence problem, which is how do we assign identities to factors that persist

### [49:55 - 49:56]

over trajectories?

### [49:56 - 50:01]

So what that means is once we've identified factors in a single state, how do we make

### [50:01 - 50:08]

sure that we track the identity of the same object from state to state within a trajectory?

### [50:08 - 50:13]

And then the combinatorial problem, how do we actually leverage this factored structure

### [50:13 - 50:16]

to generalize with hierarchy?

### [50:16 - 50:18]

Okay?

### [50:18 - 50:24]

So it turns out that for the factorization problem, it helps to try to split that factor

### [50:24 - 50:28]

entity into two sets of features.

### [50:28 - 50:33]

One set is action invariant features, which is its type.

### [50:33 - 50:38]

So if you remember when I introduced relational MDPs, there was this notion of an object type.

### [50:38 - 50:39]

Right?

### [50:39 - 50:41]

So those are action invariant features.

### [50:41 - 50:43]

And then there's also action dependent features.

### [50:43 - 50:46]

Which is its state.

### [50:46 - 50:53]

So these two sets of features matter because action invariant features are still needed

### [50:53 - 50:58]

by the reward because their task can be specified based on each of those factors.

### [50:58 - 50:59]

Right?

### [50:59 - 51:00]

I want this factor.

### [51:00 - 51:04]

I want the red block to be in a specific position and a blue block to be in a different position.

### [51:04 - 51:05]

And those are types.

### [51:05 - 51:08]

The red versus blue blocks.

### [51:08 - 51:10]

But then there are other features about objects that affect their dynamics.

### [51:10 - 51:11]

Right?

### [51:11 - 51:14]

That affect the low-level policy.

### [51:14 - 51:17]

And so those are things that we need to keep track of.

### [51:17 - 51:20]

So how do we actually leverage that factorization?

### [51:20 - 51:22]

So this becomes the combinatorial problem.

### [51:22 - 51:23]

Right?

### [51:23 - 51:31]

Which is that the same transition, the same dynamics that I've seen in my training data

### [51:31 - 51:32]

for one object.

### [51:32 - 51:38]

So here in this example, the observed transition is of this pink block moving from here to

### [51:38 - 51:39]

here.

### [51:39 - 51:40]

And all our other objects stay the same.

### [51:40 - 51:41]

Right?

### [51:41 - 51:42]

They're stationary.

### [51:42 - 51:45]

So nothing happens to the other ones.

### [51:45 - 51:50]

I'd like to be able to generalize that to some other object.

### [51:50 - 51:56]

So if I were to replace that pink block with this blue block instead, I want to be able

### [51:56 - 52:03]

to generalize that I can move it in the same way as the pink block.

### [52:03 - 52:04]

Right?

### [52:04 - 52:11]

So this is how we can leverage factorization to achieve combinatorial generalization.

### [52:11 - 52:12]

So how do we actually implement this?

### [52:12 - 52:17]

So our method is called neural constraint satisfaction, NCS.

### [52:17 - 52:20]

And here we define a two-level hierarchy.

### [52:20 - 52:26]

So first we're going to take our let's assume that we have a bunch of offline data of these

### [52:26 - 52:28]

blocks moving around.

### [52:28 - 52:35]

We want to abstract that data set into a graph, again, over state transitions of individual

### [52:35 - 52:38]

entities, of each of those factors.

### [52:38 - 52:40]

And then we can solve new rearrangement processes.

### [52:40 - 52:41]

Right?

### [52:41 - 52:46]

So what we're going to do is we're going to do a search over those graphs in order to

### [52:46 - 52:48]

compose sequences of transitions.

### [52:48 - 52:49]

Right?

### [52:49 - 52:54]

So that search, again, corresponds to our high-level policy that's trying to solve various

### [52:54 - 52:56]

specific tasks.

### [52:56 - 53:00]

And our low-level policy is just moving different objects around.

### [53:00 - 53:06]

And that low-level policy is the one where we'd like to exhibit skill reuse, where our

### [53:06 - 53:09]

skill of being able to move one object from one place to another continues.

### [53:09 - 53:10]

Right?

### [53:10 - 53:15]

So these are our two components.

### [53:15 - 53:18]

So with NCS, there are two broad components.

### [53:18 - 53:21]

So one is modeling and one is control.

### [53:21 - 53:26]

And within modeling, we again have this broken down into two steps, representation learning

### [53:26 - 53:27]

and graph construction.

### [53:27 - 53:30]

So this looks a lot like the attribute planner from the previous work.

### [53:30 - 53:36]

But now, instead of the representation learning being very straightforward because in the

### [53:36 - 53:39]

previous work, we assumed that these attributes are given.

### [53:39 - 53:40]

We just have to do supervised learning.

### [53:40 - 53:45]

order to map from pixels to those attributes now we actually have to discover what these attributes

### [53:45 - 53:50]

are so it turns out that we can use slot attention which is a self-supervised method for extracting

### [53:50 - 53:56]

out factors we can then train a transformer that is basically a one-step dynamics model

### [53:56 - 54:07]

over each of those factors and this is allows us to extract out uh representations of factors

### [54:07 - 54:12]

that take into account types uh and then also like the dynamic specific features

### [54:14 - 54:22]

right so once we now have those factors that we can now track over time within a trajectory

### [54:22 - 54:28]

we can now construct our graph so in the first work our graph was being constructed over those

### [54:28 - 54:35]

attributes but an entire trajectory was being mapped as a as as a path within our graph

### [54:37 - 54:44]

now instead of instead of constructing a graph over the monolithic states we are going to

### [54:44 - 54:51]

construct graph that only correspond to each entity transition so just that one factor right

### [54:51 - 54:59]

so the assumption is um that in this example most of our my objects are stationary and only one

### [54:59 - 55:06]

object is getting moved at a time so when i when i put this this transition into my graph i want to

### [55:07 - 55:11]

these other factors because i don't care about them because they haven't moved i just want to

### [55:11 - 55:18]

learn i just want to put into my graph this one object that has done this one move all right so

### [55:18 - 55:22]

that's how i'm going to perform my graph construction is that it's going to be on the

### [55:22 - 55:28]

factor level on a per object basis all right so i'm going to skip over this so my planning and

### [55:28 - 55:37]

control now consists of these four steps first is to take my original pixel observation of this

### [55:37 - 55:45]

entire state take out each factor discover which factor is the one that's actually moving which

### [55:45 - 55:51]

is the one that the action is being applied to build a graph um i need to align those objects

### [55:51 - 55:56]

right so i need to be able to map that this object is the same as this object here and this red

### [55:56 - 55:58]

circle is the same as this red circle here

### [55:59 - 56:05]

uh i'm going to select out the object that is moved and then bind it into a graph

### [56:07 - 56:11]

and then i'm going to build my graph of these per factor transitions

### [56:14 - 56:19]

okay so when i look at these kinds of block rearrangement tasks across these different

### [56:19 - 56:25]

environments um ncs we find that we're able to achieve very high success rates and this is

### [56:25 - 56:29]

generalizing across different numbers of blocks right so we have four five six seven

### [56:30 - 56:35]

so our performance does deteriorate a little bit as we get to more blocks but this is mainly due to

### [56:35 - 56:36]

the fact that

### [56:36 - 56:37]

uh more blocks is

### [56:37 - 56:43]

is just a naturally harder task right you have more more um pinpoints more points of failure

### [56:43 - 56:48]

right because you can fail on on the movement of each block uh we compare against random

### [56:48 - 56:56]

performance so this is just a random policy and how often can it accidentally you know uh actually

### [56:56 - 57:01]

achieve the goal and so here we get six percent around six to eight percent uh success rate with

### [57:01 - 57:08]

just a random policy we have mpc so this is just a planning based method um and we're able to

### [57:08 - 57:17]

achieve anywhere from 10 to 16 percent performance uh nf is um non-factorized graphs so here we're

### [57:17 - 57:22]

still building a graph but it's not per factor so we're just building a graph based on the entire

### [57:22 - 57:26]

state and that doesn't work well because we're not really able to reuse any skills

### [57:27 - 57:31]

and then iql is just a flat offline reinforcement learning method

### [57:31 - 57:36]

so again that doesn't perform well on these kind of long horizon sparse reward tasks

### [57:36 - 57:40]

and then behavior cloning also performs very poorly right and so then um

### [57:42 - 57:46]

we have a couple of different environments and then also complete versus partial specification

### [57:48 - 57:55]

all right so going beyond the factored setting what do we actually want in an abstraction so

### [57:55 - 58:01]

so in the two works that i've talked about today both of these are in a setting where we assume

### [58:01 - 58:01]

that

### [58:02 - 58:07]

the environment has this structure that it can be broken down into factors and this is how we

### [58:07 - 58:16]

can achieve generalization this is how we can achieve skill reuse right so if we can't assume

### [58:16 - 58:24]

that we have factors how can we still achieve skill reuse so one thing that we want from an

### [58:24 - 58:30]

abstraction is that we want it to not necessarily contain all of the information from the original

### [58:30 - 58:31]

state space

### [58:32 - 58:37]

so one problem with the original state space corresponds to something that's called the

### [58:37 - 58:44]

noisy tv problem so this is uh this is a i guess a toy problem that's studied a lot in exploration

### [58:45 - 58:51]

which is the idea that if you're trying to explore an environment you're going to use

### [58:51 - 58:56]

some type of intrinsic motivation right so the the reward that you're going to use to

### [58:56 - 59:01]

train an agent to explore is to say i want to discover new states i want to discover new

### [59:01 - 59:07]

things that i've never seen before but the problem is if i have a noisy tv in my environment

### [59:07 - 59:14]

right if it's just always flashing different kind of like salt and pepper noise

### [59:15 - 59:20]

if i just stand there and stare at the tv at every time step i'm seeing a new state

### [59:20 - 59:25]

because they're this noise distribution is so large there are so many different types of noise

### [59:25 - 59:30]

that i can see i can stay here forever and just stare at this tv and continue to see new states

### [59:31 - 59:38]

right and so the problem here is that if you tie a skill to every state in your state space

### [59:38 - 59:43]

but you have an infinite number of state spaces uh sorry infinite number of states in your state

### [59:43 - 59:51]

space then you can you can never have any type of skill reuse so we'd like to be able to ignore this

### [59:51 - 59:58]

tv to recognize that this tv is not something that we can control in the environment and so i

### [59:58 - 01:00:00]

shouldn't be interested in it

### [01:00:00 - 01:00:06]

right so if i can ignore this tv if i can drop information from my state space about this tv

### [01:00:07 - 01:00:14]

then my state space becomes much smaller i i've learned this like abstraction and i can

### [01:00:14 - 01:00:21]

try to learn skills in this smaller state space and now i can reuse those skills even

### [01:00:21 - 01:00:25]

when that tv gets dropped into my environment again because i've learned to ignore it

### [01:00:26 - 01:00:30]

the other thing that we want in a low level an abstraction for learning

### [01:00:30 - 01:00:36]

low level policies that is that we only need to capture locally controllable components right

### [01:00:36 - 01:00:42]

so when we go back to this four room example all our options were defined on a per room basis

### [01:00:44 - 01:00:48]

which means that if i'm in this room and i'm trying to learn options for navigating

### [01:00:48 - 01:00:53]

around in this room to maybe to go into each of these two hallways

### [01:00:54 - 01:01:00]

i don't care what's going on in any of the other rooms so i would like to be able to reduce my

### [01:01:00 - 01:01:08]

state space just to things that are close around me right and this is actually incorporated into

### [01:01:08 - 01:01:15]

existing hierarchical methods by limiting your goal condition policy to only go for k steps

### [01:01:16 - 01:01:21]

so another way of thinking about it is that i only care about things that are case steps away from me

### [01:01:23 - 01:01:30]

so we'd like to learn an abstraction that basically ignores everything that's more than k steps away

### [01:01:30 - 01:01:33]

so these previous methods don't do this and if we were to do this

### [01:01:33 - 01:01:36]

then we would be able to exhibit much more skill reuse

### [01:01:38 - 01:01:45]

so it turns out that capturing controllability um is actually a fairly tricky problem but it turns

### [01:01:45 - 01:01:50]

out that you can just you can capture controllability and drop things like noisy tv

### [01:01:50 - 01:01:56]

by just using a multi-step inverse prediction multi-step inverse model with a latent forward

### [01:01:56 - 01:01:58]

model so we have a couple of papers

### [01:02:00 - 01:02:03]

so we have a couple of papers that show that you can capture controllability

### [01:02:03 - 01:02:07]

by just using a multi-step inverse prediction multi-step inverse is not all you need and

### [01:02:07 - 01:02:12]

learning a fast mixing exogenous block mdp using a single trajectory so these kind of uh are methods

### [01:02:12 - 01:02:17]

that are actually have theoretical backing saying that these will provably find only the

### [01:02:17 - 01:02:24]

controllable aspects of my environment okay so i kind of just brushed over that because this is

### [01:02:24 - 01:02:29]

things that we're currently working on so we have these methods for learning controllable states

### [01:02:29 - 01:02:34]

things that are local to the agent and we're going to combine these to develop better hierarchical

### [01:02:34 - 01:02:40]

methods that work in the general environments not just factored settings that allow for skill reuse

### [01:02:41 - 01:02:47]

so just to summarize we've talked about why hierarchy why we should care about hierarchical

### [01:02:47 - 01:02:53]

rl we've talked about existing hierarchical methods and their problems we've dived deeper

### [01:02:53 - 01:02:58]

into factored mdps and relational mdps and focused on compositional generalization as

### [01:02:58 - 01:03:05]

a thing that we want to be able to achieve with hierarchy we talked about how we can do this with

### [01:03:05 - 01:03:12]

a provided nice state abstraction and then how we can actually learn this type of a nice state

### [01:03:12 - 01:03:18]

abstraction assuming this underlying factorized structure and then we've talked very briefly

### [01:03:18 - 01:03:25]

about what we can do if we can't assume factorized structure okay and with that

### [01:03:25 - 01:03:27]

we've come to the end of my talk and i'm happy to take any questions

### [01:03:28 - 01:03:44]

and thank you so much professor for a great presentation and now i open it up for questions

### [01:03:59 - 01:04:09]

hi can you hear me yeah uh thanks for your talk uh and it was very amazing uh i had actually two

### [01:04:09 - 01:04:16]

questions first about your the first book you introduced uh i think uh one of the other problems

### [01:04:16 - 01:04:21]

of the methods like option critic is that in these kinds of methods we need to define the number of

### [01:04:21 - 01:04:28]

options without having for example any information about environment yeah and i wanted to know if

### [01:04:28 - 01:04:34]

you have uh i mean uh if you have for example do something like that for example for defining the

### [01:04:34 - 01:04:41]

depth of the graph that you are creating uh for defining the number of sub goals or i mean uh to

### [01:04:41 - 01:04:47]

define how many options or skills skills we need in the environments yeah that's a good question

### [01:04:48 - 01:04:52]

so the first part of your question um which i think is interesting and i didn't really

### [01:04:52 - 01:04:58]

talk about in this talk is multiple levels of hierarchy right so if your problem is extremely

### [01:04:58 - 01:05:04]

long horizon you can imagine that having more than two levels can actually will help right

### [01:05:04 - 01:05:09]

because you need to break down this very very long horizon problem into smaller and smaller horizons

### [01:05:10 - 01:05:16]

so in this talk i i actually only considered um two levels of hierarchy we have a low level

### [01:05:16 - 01:05:21]

policy and a high level one and that's it and um so in the factored environments

### [01:05:22 - 01:05:28]

uh in in in these types of factored environments the idea is that the

### [01:05:28 - 01:05:34]

level policy the the the space of the low level policy is predefined it's just moving a single

### [01:05:34 - 01:05:44]

object to different locations um and so in that case so um yeah i'd have to think a little bit

### [01:05:44 - 01:05:50]

more about settings where multiple levels of hierarchy make sense i don't think it makes

### [01:05:50 - 01:05:58]

sense necessarily in in this environment but you know if i go back to um the initial example

### [01:05:58 - 01:06:04]

i think like i think navigation the navigation examples even these ones right like these are

### [01:06:04 - 01:06:10]

simple enough that it's still two levels like one level is within a room and then another level

### [01:06:10 - 01:06:17]

is outside of this room but you can imagine maybe if i were to like say take all of these

### [01:06:17 - 01:06:23]

these grid worlds and combine them together right so now i have uh four times six 24 rooms

### [01:06:23 - 01:06:28]

that i want one level to be within a room another level to be for the four uh

### [01:06:29 - 01:06:35]

neighboring rooms and then next level would be all six of these rooms right um

### [01:06:37 - 01:06:41]

so that would be one example where multiple levels of hierarchy make sense

### [01:06:42 - 01:06:47]

uh so the second part of your question is how can i determine the number of options

### [01:06:47 - 01:06:52]

that i need right because you as you said um one problem with option critic is that

### [01:06:52 - 01:06:58]

you have to pre-define the number of options that you're training ahead of time so um goal

### [01:06:59 - 01:07:06]

hierarchical methods get around this problem sort of because instead of pre-defining a number

### [01:07:06 - 01:07:10]

of options you've you've actually instead predefined options to be

### [01:07:12 - 01:07:18]

any goal reaching task within my environment which means technically the number of options

### [01:07:18 - 01:07:24]

corresponds to the number of goals that i have in my environment which kind of more

### [01:07:24 - 01:07:28]

simply just corresponds to the number of states that i have so you could have a huge

### [01:07:28 - 01:07:40]

number of options in that case, which is maybe not ideal. Let's see. Diane, so this method that

### [01:07:40 - 01:07:45]

I kind of talked about near the beginning where they learn a set of skills using mutual information,

### [01:07:46 - 01:07:51]

this is also like option critic in that you have to predefine the number of skills.

### [01:07:53 - 01:07:58]

But those are kind of sampled from a z-space. So again, technically there's an infinite number

### [01:07:58 - 01:08:06]

of them because z is continuous. So I would say that none of these methods have very good

### [01:08:06 - 01:08:18]

solutions to that problem. And of the things that I've discussed, I would say like, so at the very

### [01:08:18 - 01:08:23]

end, right when I was talking about what we want out of an abstraction for learning low-level

### [01:08:23 - 01:08:27]

skills. Oops. Sorry. Let's see.

### [01:08:28 - 01:08:39]

Can I go back to my... I just exited out of the... Go back into presenter view.

### [01:08:42 - 01:08:44]

Just share that screen again.

### [01:08:48 - 01:08:56]

Right. So controllability and capturing local controllable components. Here, still the idea is

### [01:08:58 - 01:09:04]

that if there's only one function that we learn that defines the goals of our low-level policy,

### [01:09:04 - 01:09:08]

it would still be a continuous space. So technically, there's an infinite number of goals.

### [01:09:08 - 01:09:14]

So in that sense, we're still not really getting around this problem of like how do we actually

### [01:09:15 - 01:09:20]

specify the... So sorry, I should say it gets around the problem of having to specify a number

### [01:09:20 - 01:09:26]

of options. I would say it's still not ideal because technically there's an infinite number of options.

### [01:09:26 - 01:09:28]

And so I think it is an interesting

### [01:09:28 - 01:09:36]

research problem of how can we also reduce the number of options so that we want a minimal

### [01:09:36 - 01:09:44]

number of options that we can use to solve our downstream tasks, right?

### [01:09:44 - 01:09:49]

Because the more options that you have, the harder the problem is for the high-level policy.

### [01:09:49 - 01:09:53]

Because now the high-level policy's action space is getting larger and larger.

### [01:09:53 - 01:09:57]

So I think it's an important problem.

### [01:09:57 - 01:10:02]

And I guess the only way that we have to get around it, of specifying the number of options,

### [01:10:02 - 01:10:06]

is to move to the continuous setting where we have potentially an infinite number of

### [01:10:06 - 01:10:07]

options.

### [01:10:07 - 01:10:11]

But I think it's an interesting problem to figure out how can we reduce that in some

### [01:10:11 - 01:10:13]

way.

### [01:10:13 - 01:10:15]

I hope that answered your question.

### [01:10:15 - 01:10:17]

Yes, sure.

### [01:10:17 - 01:10:18]

Thank you.

### [01:10:18 - 01:10:25]

I had another question about the role of, I mean, compositionality in continual learning

### [01:10:25 - 01:10:26]

from your perspective.

### [01:10:26 - 01:10:33]

I think here if we want to use compositionality in continual learning, there will be, again,

### [01:10:33 - 01:10:39]

a trade-off between using or reusing the skills or learning the new skills in the new environments.

### [01:10:39 - 01:10:40]

Yeah.

### [01:10:40 - 01:10:47]

So how promising do you think the compositionality may be in continual learning?

### [01:10:47 - 01:10:49]

So I think it's going to be...

### [01:10:49 - 01:10:55]

I think it's something that will help in continual learning, because if we're assuming that in

### [01:10:55 - 01:10:56]

the continual learning setting...

### [01:10:56 - 01:10:56]

Yeah.

### [01:10:56 - 01:10:59]

You know, we're constantly seeing new things.

### [01:10:59 - 01:11:11]

But maybe some of those new things that we're seeing are just like a slight modification

### [01:11:11 - 01:11:15]

of things that we've seen before, then we should be able to generalize to those new

### [01:11:15 - 01:11:21]

settings without actually having to learn about them continually, right?

### [01:11:21 - 01:11:26]

So there's going to be two types of new environments in the continual learning setting.

### [01:11:26 - 01:11:32]

Ones that are just a recombination of things we've seen before, and then truly new things.

### [01:11:32 - 01:11:38]

Truly new things we still will have to learn continually, so then this kind of compositional

### [01:11:38 - 01:11:40]

generalization won't be helpful.

### [01:11:40 - 01:11:44]

But if there are going to be things that we're seeing that are new, that are just recombinations

### [01:11:44 - 01:11:52]

of old things, then we shouldn't waste, you know, memory and computation learning again.

### [01:11:52 - 01:11:56]

We should just try to generalize from things that we've seen before.

### [01:11:56 - 01:12:02]

So leveraging metrics, for example, like by simulation metrics, I mean, I know you

### [01:12:02 - 01:12:08]

have used it for representation learning, to, I mean, measure the similarity of new

### [01:12:08 - 01:12:12]

task or environment to the tasks we learned.

### [01:12:12 - 01:12:13]

Can it be an effective way?

### [01:12:13 - 01:12:15]

Yeah, I think so.

### [01:12:15 - 01:12:23]

I think that can, that would be one way of deciding whether you need to learn or whether

### [01:12:23 - 01:12:24]

you can reuse, right?

### [01:12:24 - 01:12:25]

Mm-hmm.

### [01:12:25 - 01:12:26]

So if your task metric...

### [01:12:26 - 01:12:26]

Mm-hmm.

### [01:12:26 - 01:12:30]

If your new task compared to your old tasks is small, then you can say, okay, maybe

### [01:12:30 - 01:12:35]

I want to reuse some policies that I've already learned from before.

### [01:12:35 - 01:12:39]

If your task metric says, actually, the distance is really far, this new task is very different

### [01:12:39 - 01:12:43]

from everything I've seen before, then I know that I need to learn.

### [01:12:43 - 01:12:46]

And so that kind of decision-making, that high-level decision-making is something that

### [01:12:46 - 01:12:51]

you could use in the continual learning setting to decide, can I reuse or do I have to learn

### [01:12:51 - 01:12:52]

again?

### [01:12:52 - 01:12:53]

Mm-hmm.

### [01:12:53 - 01:12:54]

Yeah.

### [01:12:54 - 01:12:55]

Thank you.

### [01:12:55 - 01:12:56]

So that's a great question.

### [01:12:56 - 01:12:57]

Thanks.

### [01:12:57 - 01:12:58]

Thanks.

### [01:12:58 - 01:12:59]

Thank you very much.

### [01:12:59 - 01:13:00]

Hi.

### [01:13:00 - 01:13:01]

Do you have my voice?

### [01:13:01 - 01:13:02]

Yes.

### [01:13:02 - 01:13:03]

I can hear you.

### [01:13:03 - 01:13:04]

Thank you for awesome presentation.

### [01:13:04 - 01:13:05]

My question is about using large language models as the high-level policy.

### [01:13:05 - 01:13:06]

I wanted to know your opinion on the benefits or character limitations as a high-level policy.

### [01:13:06 - 01:13:07]

And my second question is, do you think that using large language models as a high-level

### [01:13:07 - 01:13:08]

policy is a good idea?

### [01:13:08 - 01:13:09]

Yes.

### [01:13:09 - 01:13:10]

Yes.

### [01:13:10 - 01:13:11]

Yes.

### [01:13:11 - 01:13:12]

Yes.

### [01:13:12 - 01:13:13]

Yes.

### [01:13:13 - 01:13:14]

Yes.

### [01:13:14 - 01:13:15]

Yes.

### [01:13:15 - 01:13:16]

Yes.

### [01:13:16 - 01:13:17]

Yes.

### [01:13:17 - 01:13:18]

Yes.

### [01:13:18 - 01:13:19]

Yes.

### [01:13:19 - 01:13:20]

Yes.

### [01:13:20 - 01:13:21]

Yes.

### [01:13:21 - 01:13:22]

Yes.

### [01:13:22 - 01:13:23]

Yes.

### [01:13:23 - 01:13:24]

Yes.

### [01:13:24 - 01:13:25]

Yes.

### [01:13:25 - 01:13:26]

Yes.

### [01:13:26 - 01:13:27]

Yes.

### [01:13:27 - 01:13:28]

Yes.

### [01:13:28 - 01:13:29]

Yes.

### [01:13:29 - 01:13:30]

Yes.

### [01:13:30 - 01:13:31]

Yes.

### [01:13:31 - 01:13:32]

Yes.

### [01:13:32 - 01:13:33]

Yes.

### [01:13:33 - 01:13:34]

Yes.

### [01:13:34 - 01:13:35]

Yes.

### [01:13:35 - 01:13:36]

Yes.

### [01:13:36 - 01:13:37]

Yes.

### [01:13:37 - 01:13:38]

Yes.

### [01:13:38 - 01:13:39]

Yes.

### [01:13:39 - 01:13:40]

Thank you.

### [01:13:40 - 01:13:41]

That's a great question.

### [01:13:41 - 01:13:42]

Yeah.

### [01:13:42 - 01:13:44]

I think with large language models, a lot of this prior work, I would say for a lot of

### [01:13:44 - 01:13:47]

settings, a lot of these prior works, maybe, are less relevant.

### [01:13:47 - 01:13:48]

Right?

### [01:13:48 - 01:13:54]

So, let's think about, what are the attributes that we want from a high-level policy?

### [01:13:54 - 01:13:55]

Yeah.

### [01:13:55 - 01:14:00]

So, let's say, as an example, let's think about robotics.

### [01:14:00 - 01:14:05]

The high-level policy often needs to use a lot of knowledge about the world, right?

### [01:14:05 - 01:14:17]

So, if I'm trying to plan a trip to Japan, right, like, actually using an LLM for this

### [01:14:17 - 01:14:20]

is going to be very productive, right?

### [01:14:20 - 01:14:25]

Rather than assuming that I'm an agent that knows nothing about the world, I need to know

### [01:14:25 - 01:14:30]

that I can how to book tickets on a plane, right?

### [01:14:30 - 01:14:33]

I need to know how to get to the airport.

### [01:14:33 - 01:14:40]

I need to know how to get off my plane and go to my hotel on the other side, right?

### [01:14:40 - 01:14:47]

So, there are all of these ideas, these high-level ideas that LLMs have from distilling the entire

### [01:14:47 - 01:14:50]

internet that make it a very good high-level policy.

### [01:14:50 - 01:14:56]

And, kind of, like, naturally, it can even you can even use the LLM to define different

### [01:14:56 - 01:15:00]

levels of abstraction of, like, okay, if I want to go to Japan, what should I think about

### [01:15:00 - 01:15:01]

first?

### [01:15:01 - 01:15:02]

Okay.

### [01:15:02 - 01:15:05]

So, you know, if I need to book tickets, how do I book tickets?

### [01:15:05 - 01:15:07]

What website should I go to?

### [01:15:07 - 01:15:08]

How do I check prices?

### [01:15:08 - 01:15:10]

How do I decide which flight is best?

### [01:15:10 - 01:15:11]

Right?

### [01:15:11 - 01:15:15]

So, there's, like, all of these levels of decisions that need to get made, and you can

### [01:15:15 - 01:15:18]

even use the LLM to define what those levels should be.

### [01:15:18 - 01:15:20]

So, I would say that's very important.

### [01:15:20 - 01:15:25]

That there are a lot of tasks that LLMs are would be very good as a high-level policy.

### [01:15:25 - 01:15:31]

But of course, this also means that this is only true for tasks that LLMs have knowledge

### [01:15:31 - 01:15:32]

about.

### [01:15:32 - 01:15:33]

Right?

### [01:15:33 - 01:15:37]

We can also define we can also think of tasks and environments that LLMs don't have a lot

### [01:15:37 - 01:15:38]

of knowledge about.

### [01:15:38 - 01:15:39]

Right?

### [01:15:39 - 01:15:44]

So, you know, today's LLMs are mainly only trained on language on the internet.

### [01:15:44 - 01:15:47]

Which means that they're not necessarily going to be good at, say, like, deciding how, you

### [01:15:47 - 01:15:48]

know, how to do things.

### [01:15:48 - 01:15:49]

Right?

### [01:15:49 - 01:15:49]

Right?

### [01:15:50 - 01:15:55]

Like, how to, like, what's something that's that where there's not a lot of information

### [01:15:55 - 01:15:56]

on the internet for?

### [01:15:56 - 01:15:59]

Like, maybe, like, how to deep sea dive.

### [01:15:59 - 01:16:00]

Right?

### [01:16:00 - 01:16:01]

You know?

### [01:16:01 - 01:16:09]

Like, there are things that where there are environments where there's not a lot of information

### [01:16:09 - 01:16:17]

about them in language, and it actually requires exploring the environment and kind of, like,

### [01:16:17 - 01:16:19]

more physical hands on.

### [01:16:20 - 01:16:23]

knowledge in order to make decisions.

### [01:16:23 - 01:16:27]

And so then those are going to be examples where an LLM doesn't necessarily work well.

### [01:16:27 - 01:16:31]

Did that answer your question?

### [01:16:31 - 01:16:32]

Thank you.

### [01:16:32 - 01:16:35]

Thank you.

### [01:16:35 - 01:16:36]

Thank you.

### [01:16:36 - 01:16:38]

Thank you.

### [01:16:38 - 01:16:39]

Thank you.

### [01:16:39 - 01:16:41]

Thank you.

### [01:16:41 - 01:16:42]

Thank you.

### [01:16:42 - 01:16:44]

Thank you.

### [01:16:44 - 01:16:45]

Thank you.

### [01:16:45 - 01:16:46]

Thank you.

### [01:16:46 - 01:16:47]

Thank you.

### [01:16:47 - 01:16:49]

Thank you.

### [01:16:49 - 01:16:49]

Thank you.

### [01:16:49 - 01:17:06]

students raising their hand so okay so for the final question i can i ask for a what is your

### [01:17:06 - 01:17:14]

advice for the students who just starting their research career and wants to tackle some interesting

### [01:17:14 - 01:17:23]

problem what do you think is the proper way to do research in 2025 if they want to start their

### [01:17:23 - 01:17:34]

career that's a great question um so you know i i think it's great that you have like invited you

### [01:17:34 - 01:17:38]

know researchers to present their research and and present kind of like the things that they're

### [01:17:38 - 01:17:44]

excited about i think that's a really great way to start out when you're first starting out you

### [01:17:44 - 01:17:52]

don't have um a lot of experience or knowledge about what have people already studied right like

### [01:17:52 - 01:17:58]

you haven't developed a taste for what problems are interesting or important but more senior

### [01:17:58 - 01:18:03]

researchers have and so asking more senior researchers what do you think is an important

### [01:18:03 - 01:18:09]

problem what are you excited about right now is a really great way to learn more about what are

### [01:18:09 - 01:18:14]

interesting problems that you can dive deeper into right so i think that's like an uh an

### [01:18:14 - 01:18:14]

official

### [01:18:14 - 01:18:20]

um way to start out um so i think that's a really great way to start out um so i think that's like an

### [01:18:20 - 01:18:25]

official um way to start out um so i think that's like an efficient way to search for a problem

### [01:18:27 - 01:18:34]

um so so you know what i'm really saying is try to talk to people you know like reading papers is

### [01:18:34 - 01:18:40]

good but at some point talking to people and learning about how they think how they read papers

### [01:18:42 - 01:18:44]

is a much more efficient way to uh to make progress

### [01:18:44 - 01:18:49]

and to try andミル your brain to get done with it and you know you can say don't do one thing

### [01:18:49 - 01:18:53]

right once you try to use a big paper and the other one might not work but then you can just

### [01:18:53 - 01:18:57]

reach out to people through email so if you've read some paper and you're like this is a really

### [01:18:57 - 01:19:01]

nice paper i really like the way that they've like thought about the problem the way they've

### [01:19:01 - 01:19:05]

designed the experiments like how they write i just i love all the aspects of this paper

### [01:19:05 - 01:19:09]

you should just reach out to the first author um you know you can tell them that you really like

### [01:19:09 - 01:19:14]

the paper you can ask any questions that you had um from the paper or just ask them what are they

### [01:19:14 - 01:19:22]

So I guess I would say as a person first starting out, right, the most important problems are how do I pick a research direction?

### [01:19:22 - 01:19:28]

And so talking to lots of more senior researchers to figure out what they think is important is a good way to make those decisions.

### [01:19:28 - 01:19:37]

And the other is to try to start collaborations with those people or and just kind of try to expand your network.

### [01:19:37 - 01:19:42]

And so reaching out to people whose papers you like is a really good way of doing that.

### [01:19:42 - 01:19:51]

Often people are very happy to talk about their work and talk about potential future directions and explore collaborations.

### [01:19:51 - 01:19:57]

Thank you for your great answers, professors. Thank you for having me.

### [01:19:57 - 01:20:01]

Again, thank you for accepting our invite and being with us today.

### [01:20:01 - 01:20:07]

I think if there is no more questions, we can end the session.

### [01:20:07 - 01:20:11]

OK. All right. Thank you very much. Thank you so much.

### [01:20:11 - 01:20:12]

Thank you. Bye bye.

### [01:20:12 - 01:20:14]

Bye bye.

### [01:20:42 - 01:20:44]

Bye bye.
