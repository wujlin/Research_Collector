# Benjamin Eysenbach Self-Supervised Agents Exploring and Learning with Minimal Feedback

- URL: https://www.youtube.com/watch?v=AhoOcPi2QIA
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T13:37:08`

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

### [04:00 - 04:30]

Thank you.

### [04:30 - 05:00]

Thank you.

### [05:00 - 05:30]

Thank you.

### [05:30 - 06:00]

Thank you.

### [06:00 - 06:30]

Thank you.

### [06:30 - 06:31]

you

### [07:00 - 07:01]

you

### [07:30 - 07:31]

you

### [08:00 - 08:01]

you

### [08:30 - 08:31]

you

### [09:00 - 09:01]

you

### [09:30 - 09:31]

you

### [10:00 - 10:01]

you

### [10:30 - 10:31]

you

### [11:00 - 11:01]

you

### [11:30 - 11:31]

you

### [12:00 - 12:14]

welcome professor

### [12:14 - 12:24]

good morning welcome professor good morning

### [12:24 - 12:30]

they're very happy to have you with us and we're very

### [12:30 - 12:33]

happy to that you accepted our invitation

### [12:33 - 12:42]

absolutely okay so without further ado i'm gonna hand it over to my dear professor i'm the head

### [12:42 - 12:47]

for the course and i'm gonna hand it over to my professor to welcome you on his side and then we

### [12:47 - 12:53]

can have your wonderful time before getting started uh i wonder if it makes sense uh i want

### [12:53 - 13:00]

to make sure you can figure out the slide sharing yeah sure sure on the top uh you can see i think

### [13:00 - 13:09]

there are force i can from the right you can share the screen with it beautiful let me try to

### [13:09 - 13:20]

figure out uh i apologize i haven't used this platform before yes yes it's new and i try to

### [13:20 - 13:28]

give some visuals and i don't know if they help yeah help me log on sweet i just looking for the

### [13:28 - 13:30]

screen share button great

### [13:30 - 13:36]

okay cool beautiful great okay cool cool so i'm gonna hand it over to my professor and then we

### [13:36 - 13:38]

can have your attack and thank you

### [13:42 - 13:44]

um hi benjamin can you hear me

### [13:48 - 13:52]

nice to have you and nice to meet you uh it's our pleasure to have you today

### [13:53 - 13:59]

my name is muhammad rofan i am the lecturer of this rl course

### [14:00 - 14:05]

and we have regular invited speakers

### [14:05 - 14:11]

from different topics that we teach every week so

### [14:11 - 14:16]

it's nice to have you today and we are looking forward to hear

### [14:16 - 14:23]

about your talk so please feel free to to start thank you for the kind introduction i'm super

### [14:23 - 14:27]

excited to be here and i'm really looking forward to all the questions next hour and then all the

### [14:28 - 14:30]

during the q a and the following

### [14:30 - 14:37]

um 30 minutes thank you so much so i'm benjamin eisenbach i'm an assistant professor of computer

### [14:37 - 14:41]

science here at princeton university and i'm super excited to share with you some of the work that me

### [14:41 - 14:47]

and my students have been working on over the last couple of years the the title of today's talk is

### [14:47 - 14:52]

self-supervised agents learning and exploring with minimal feedback and when i talk about self

### [14:52 - 14:57]

supervision i'm really going to be thinking about how we can learn from data from experience without

### [14:57 - 14:58]

needing rewards without needing benefits without needing benefits without needing benefits without

### [14:58 - 15:04]

rewards without needing demonstrations without needing optimal actions the huge challenge in

### [15:04 - 15:09]

generative ai today is how do we generate good data how do we generate good feedback

### [15:10 - 15:14]

and today's talk is going to give some specific algorithmic tools that we might use for lifting

### [15:14 - 15:19]

some of these limitations i think reinforcement learning is well positioned to give us ways of

### [15:19 - 15:24]

automatically generating data and we're going to see today how we can view reinforcement

### [15:24 - 15:28]

learning in a way that we can generate that data without expert feedback

### [15:29 - 15:34]

and so let's dive in i want to start with a thought experiment and this is intended to be

### [15:34 - 15:39]

interactive so i hope there's a way that people can uh react to the thumbs up or thumbs down on

### [15:39 - 15:46]

the platform here so um show of hands uh how many people think that a generative image model today

### [15:46 - 15:51]

in 2025 may can generate images different from those seen in this training data set

### [15:55 - 15:58]

is there a way people can raise their hand of some sort sweet okay

### [15:58 - 16:05]

uh yes yes they can raise their hand and if they raise their hand i'm gonna give them the microphone

### [16:05 - 16:13]

access so they can ask those cool okay so a couple hands there um

### [16:16 - 16:20]

okay what about language models can language models generate sentences

### [16:20 - 16:23]

different from those seen in their training data

### [16:25 - 16:28]

and now just raise your hand uh for a vote of yes

### [16:29 - 16:34]

not uh to ask a question he's like yes i think they can do this

### [16:37 - 16:39]

okay four out of fourteen

### [16:42 - 16:45]

what is the right analogy for reinforcement learning

### [16:46 - 16:51]

this is a rhetorical question but i like thinking about this question because it's not

### [16:51 - 16:56]

thinking about reinforcement learning in the context of the generalization capabilities of

### [16:56 - 16:58]

other models really helps has helped explain the concept of reinforcement learning and this is a

### [16:58 - 17:03]

expand my mind to what might be possible a priority I think generalization and reinforcement

### [17:03 - 17:08]

learning is typically thought of as sort of a dark art something like yeah maybe it would

### [17:08 - 17:13]

be nice to have but in the same way that we've seen wild generalization capabilities for

### [17:13 - 17:17]

image models they're able to generate images that are really really different than those

### [17:17 - 17:21]

seen in the training data set and then we've seen similar capabilities for language models

### [17:21 - 17:25]

they can generate sentences they're just massively different from those seen in the training

### [17:25 - 17:30]

data sets it gives me confidence that the same might be true for reinforcement learning

### [17:30 - 17:35]

that it might be possible to build some reinforcement learning agents that can solve tasks that

### [17:35 - 17:39]

are fundamentally different than those they were trained on if they're trained on enough

### [17:39 - 17:45]

tasks in today's talk I'm going to argue that one of the key ingredients to find this sort

### [17:45 - 17:50]

of generalization is to frame reinforcement learning in a self-supervised way that will

### [17:50 - 17:55]

allow us to learn on more tasks on more data and what today's talk will start to introduce

### [17:55 - 17:55]

some of these 맛있ies.

### [17:55 - 18:00]

algorithms that allow us to do that to learn reinforcement to do reinforcement learning in

### [18:00 - 18:06]

a self-supervised way so here's where we're going to go today i'm going to start by introducing

### [18:06 - 18:11]

self-supervised reinforcement learning providing a formal definition but also giving an example

### [18:11 - 18:15]

algorithm and this will lay a foundation for thinking about how how is it even possible to

### [18:15 - 18:20]

think about reinforcement learning if you don't have reward functions i'll then talk a little

### [18:20 - 18:26]

bit about some really recent ongoing work in my lab that's started to observe how these

### [18:26 - 18:30]

self-supervised agents can really unlock new capabilities and i'll talk a little bit about

### [18:30 - 18:35]

some generalization properties and we'll talk about a new benchmark and part of the reason i

### [18:35 - 18:39]

want to introduce this new benchmark is that it provides a really good jumping off point

### [18:39 - 18:40]

for folks that want to get involved in the research

### [18:43 - 18:47]

so let's get started this is a deep reinforcement learning course so i think that the next couple

### [18:47 - 18:50]

slides will probably be very obvious to many of you so i'll go through them rather quickly

### [18:50 - 18:54]

but please raise your hand or post in the chat here if you have any questions

### [18:56 - 19:02]

so in the typical reinforcement learning problem we have an environment we have policy the policy

### [19:02 - 19:08]

outputs actions a in response to observations s throughout today's talk i'm going to assume that

### [19:08 - 19:13]

the environment that we're in a fully observed setting and so the dynamics are markov and so

### [19:13 - 19:19]

the policy is also markov in the standard reinforcement learning problem we also observe

### [19:19 - 19:20]

rewards s

### [19:20 - 19:24]

and without loss of generality we can assume the rewards only depend on the state

### [19:24 - 19:27]

we'll see this makes our lives easier in a couple slides

### [19:29 - 19:33]

so the reinforcement learning problem is really exciting because it's so general it can be used

### [19:33 - 19:39]

to model games to model chemical reactions to model nuclear fusion to model education yet

### [19:40 - 19:45]

part of that generality or what comes with that generality is that it's also a very very

### [19:45 - 19:50]

challenging problem and i think that the challenge of reinforcement learning largely stems from the

### [19:50 - 19:55]

rewards and there are a couple different ways of seeing this one way of seeing it is that unlike

### [19:55 - 20:01]

in supervised learning where you get a label for every input in reinforcement learning you

### [20:01 - 20:07]

only get a label you only get feedback after you take several actions so in this task here

### [20:07 - 20:11]

we have this robot hand and it might be that you want to get the robot hand to go and pick

### [20:11 - 20:15]

up this green block and move it over and then put it down then position it in the blue bin

### [20:15 - 20:19]

but you might only get the feedback after you've taken five ten actions

### [20:20 - 20:24]

this makes it really hard to figure out well which of those actions was the correct action to take

### [20:27 - 20:33]

confounding this is the fact that the observations we're dealing with are often very high dimensional

### [20:33 - 20:37]

and so this ratio of number of bits of feedback to number of bits of input

### [20:37 - 20:40]

is a very very bad ratio and it makes the learning really challenging

### [20:42 - 20:46]

now part of the reason why we have such limited feedback in the reinforcement learning problem

### [20:46 - 20:53]

is because it's practically specifying these rewards is really hard so in this

### [20:53 - 20:58]

manipulation task that i've been showing here where we have this robot hand why should this

### [20:58 - 21:06]

observation here get a reward of plus five that seems sort of arbitrary well in practice

### [21:06 - 21:11]

the reason the state gets a reward of plus five is because a couple graduate students

### [21:11 - 21:15]

spent a couple weeks writing this block of code that computes the reward for this observation

### [21:17 - 21:20]

however actually writing this block of code is really really frustrating there

### [21:20 - 21:27]

are all these hyper parameters in here you might notice this 50 and this 0.01

### [21:27 - 21:33]

all these if else cases is really non-trivial to design these rewards even for experts and this

### [21:33 - 21:38]

means that for applications where someone went out to apply reinforcement learning if you're not an

### [21:38 - 21:43]

expert it's basically impossible to apply existing reinforcement learning methods

### [21:45 - 21:46]

this becomes even more challenging

### [21:46 - 21:51]

when you want to look at real world problems this reward function here depends on the

### [21:51 - 21:55]

positions of all the objects but if you're doing reinforcement learning directly from say

### [21:55 - 22:00]

images you don't know the positions of all the objects so you would first have to install some

### [22:00 - 22:05]

sensors or do some computer vision to figure out the positions of all the objects even before

### [22:05 - 22:09]

you could compute your reward function and so defining these rewards is a really really

### [22:09 - 22:16]

challenging problem and it's challenging not just in robotics one application we've been playing

### [22:16 - 22:21]

around with is chemistry and there how do we define whether this is a good molecule or a bad

### [22:21 - 22:27]

molecule we might want to produce a molecule say that's non-toxic that's safe for humans

### [22:27 - 22:32]

but how do you write that in in code how do you say okay this molecule is toxic this molecule is

### [22:32 - 22:39]

non-toxic it seems very non-trivial to define that in code and so in today's talk we're going

### [22:39 - 22:45]

to be thinking about how we can start to get the benefits of reinforcement learning without having

### [22:45 - 22:46]

this massive challenge of learning reinforcement learning without having this massive challenge of

### [22:46 - 22:51]

reward engineering without having to write that big block of code can we still design

### [22:51 - 22:57]

reinforcement learning algorithms that can help us out so that's where we're going to go today

### [22:58 - 23:03]

and as a bit of motivation i want to start by thinking about in other areas of machine learning

### [23:03 - 23:07]

how have how have we figured out ways of learning without feedback

### [23:08 - 23:12]

so in other areas of machine learning there are these self-supervised techniques techniques that

### [23:12 - 23:16]

can just look at raw data with no labels and automatically extract useful

### [23:16 - 23:21]

patterns from those data so there are a lot of these techniques in computer vision

### [23:22 - 23:25]

some of these techniques are these sort of masked auto encoders or diffusion models

### [23:25 - 23:30]

methods just just take an image and cover up pixels of that image or patches of that image

### [23:30 - 23:33]

and they try to predict what are the missing pixels or what are the missing patches

### [23:34 - 23:38]

and these are the techniques that underlie the big diffusion models that i imagine many of you

### [23:38 - 23:46]

have used before and there's similar self-supervised learning techniques in

### [23:46 - 23:50]

other areas of machine learning so for example if you look at natural language processing

### [23:50 - 23:55]

there are methods that look at a sentence and cover up random words to that sentence and then

### [23:55 - 24:00]

you try to predict what are those missing words or you cover up the next word of a sentence and

### [24:00 - 24:06]

you try to predict what are the next words and in doing so you're these methods that predict the

### [24:06 - 24:11]

missing words are give us the foundation for the modern language models that we have today

### [24:12 - 24:16]

and so in fact one way of seeing modern generative tools both in vision and in language

### [24:16 - 24:21]

is that they rely really heavily on doing self-supervised learning on doing learning

### [24:21 - 24:27]

just on raw data on just big stacks of images or big stacks of sentences without any labels

### [24:27 - 24:32]

about whether those are good images or bad images and so seeing the massive success of

### [24:32 - 24:38]

self-supervised learning in these other domains vision and language has inspired us to think about

### [24:38 - 24:45]

how can we develop a foundation for self-supervised reinforcement learning how can we define define

### [24:45 - 24:46]

reinforcement learning

### [24:46 - 24:51]

algorithms that similarly don't require any feedback don't require any rewards

### [24:53 - 24:58]

so just to make sure we're all on the same page i want to introduce the definition of what i mean

### [24:58 - 25:04]

by self-supervised reinforcement learning at first pass self-supervised reinforcement learning might

### [25:04 - 25:08]

simply mean that we take the reinforcement learning problem and we delete the reward

### [25:08 - 25:15]

function we now have a formally a controlled markoff process maybe more formally i might say

### [25:16 - 25:22]

self that self-supervised reinforcement learning is the problem of learning policies or models or

### [25:22 - 25:28]

representations something that enables us to quickly solve downstream tasks but we want to

### [25:28 - 25:33]

learn this policy or model of representation with no rewards and with no demonstrations

### [25:35 - 25:41]

so to make this more concrete i'll talk about one particular type of self-supervised

### [25:41 - 25:45]

reinforcement learning problem which is this problem of goal reaching or goal conditioned

### [25:45 - 25:50]

reinforcement learning there the input here it could be

### [25:54 - 26:00]

an environment an environment without a reward function or it could just be a data set a data set

### [26:00 - 26:06]

of say videos labeled with actions these actions are not necessarily the optimal actions they're

### [26:06 - 26:13]

not necessarily demonstrations and we don't have rewards and the goal or are the at the end of the

### [26:13 - 26:15]

day we want to produce a goal conditioned learning model for self-supervised reinforcement learning

### [26:15 - 26:16]

so we want to create a goal conditioned learning model for self-supervised reinforcement learning

### [26:16 - 26:21]

that's what we have on the right hand side a policy that takes as input the current state of

### [26:21 - 26:26]

the world and some goal state and the goal is just an observation that shows what we would like the

### [26:26 - 26:31]

world to look like so maybe the state is an image and the goal is another image showing us what we

### [26:31 - 26:37]

want the world to look like and the policy should take actions so that eventually we get to this

### [26:37 - 26:45]

desired goal state okay i'm going to pause here uh can i how are there any questions about the problem

### [26:45 - 26:47]

at this point

### [26:59 - 27:03]

and so one quick question uh how the goal is specified is it

### [27:03 - 27:10]

specified through a particular state or do we have other means of doing it this is super good question

### [27:10 - 27:15]

so in the next couple slides i'm going to assume that the goal is given by

### [27:15 - 27:21]

a state observation and so for this robot manipulation task here the goal

### [27:22 - 27:28]

could just look like this image over here at the end of today's talk i'll talk a little bit about

### [27:28 - 27:33]

different ways of specifying goals one example is via language

### [27:35 - 27:43]

i see and so the learning should happen in a way that the algorithm is prepared to go to every

### [27:43 - 27:45]

possible goal is that true

### [27:45 - 27:50]

we would very much like that what we'll

### [27:50 - 27:51]

see today is an algorithm

### [27:54 - 28:00]

yes yeah that is where we're headed all right thank you it's a really good question

### [28:04 - 28:13]

are there any other questions

### [28:13 - 28:20]

great let's move on so i will now introduce

### [28:20 - 28:25]

an algorithm that we found pretty effective for solving some of these goal reaching tasks

### [28:25 - 28:30]

a algorithm we designed about three years ago but it's continued to surprise us by giving us new

### [28:31 - 28:36]

methods for new tasks and new interests and it keeps your the phenomenon we observe have

### [28:36 - 28:42]

also continued to surprise us and there's we just give one example of a goal conditioning algorithm

### [28:42 - 28:45]

algorithm, one way of learning the school conditioning policy

### [28:45 - 28:47]

without needing rewards. And there's several other algorithms

### [28:47 - 28:52]

that we could talk about later if folks are interested. So this

### [28:52 - 28:55]

algorithm works by using a form of contrastive learning.

### [28:55 - 28:58]

Contrastive learning is a way of taking data and learning

### [28:58 - 29:02]

representations from those data. And we do this using a form of

### [29:02 - 29:05]

temporal contrastive learning. This is a tool that's been

### [29:05 - 29:09]

around for a long time, especially in other domains, we

### [29:09 - 29:12]

found a way of applying it to the reinforcement learning

### [29:12 - 29:17]

setting that allows us to get optimal policies. And so what

### [29:17 - 29:21]

we're going to do is we're going to learn two encoders. One

### [29:21 - 29:24]

encoder is an encoder of state action pairs that maps pairs of

### [29:24 - 29:28]

states and actions to a representation. And the other is

### [29:28 - 29:33]

a goal encoder that takes just a future state observation and

### [29:33 - 29:35]

maps it to a representation.

### [29:35 - 29:44]

And we're going to learn these encoders using two terms. One

### [29:44 - 29:47]

term says that when we take our time series data, we take our

### [29:47 - 29:52]

video, we should look at a state and an action and sample some

### [29:52 - 29:56]

future state. And we want to optimize the encoders to give

### [29:56 - 30:00]

similar representations to states that occur nearby in time

### [30:00 - 30:01]

on the same video.

### [30:04 - 30:05]

And then if we look at

### [30:05 - 30:09]

states from different videos, we should optimize these encoders

### [30:09 - 30:13]

so that observations from different videos have dissimilar

### [30:13 - 30:18]

representations. So the intuition here is that the

### [30:18 - 30:21]

similarity between the representations to tell us

### [30:21 - 30:24]

similarity in time, how likely is it that you could get from

### [30:24 - 30:28]

one state action pair to some other state over some time

### [30:28 - 30:32]

horizon. Now, one detail that will turn out to be important is

### [30:32 - 30:34]

that when we're sampling these

### [30:34 - 30:38]

positive examples, these future states, we're going to sample them

### [30:38 - 30:41]

from a certain geometric distribution. And so they're most

### [30:41 - 30:44]

likely going to be one or two or three steps in the future, but

### [30:44 - 30:47]

they could be four or five or more steps in the future. And

### [30:47 - 30:50]

this geometric distribution will allow us to prove some important

### [30:50 - 30:52]

theoretical properties about this method.

### [30:55 - 30:58]

Now, one important detail here is that one of these encoders,

### [30:58 - 31:01]

the state action encoder, depends on the action. And what

### [31:01 - 31:03]

that means is that after we've learned these representations,

### [31:04 - 31:09]

we'll be able to directly use the representations for figuring out what is the best action to take

### [31:09 - 31:14]

if we want to get from one state to some future state. And remember, at the end of the day,

### [31:14 - 31:20]

that's these actions that we want to figure out. Now, for folks that have seen contrastive

### [31:20 - 31:25]

learning before, we can draw a certain analogy. So typically, when contrastive learning is

### [31:25 - 31:31]

introduced, say in a computer vision course, we think about applying it to images. You take an

### [31:30 - 31:36]

image, and then an augmented version of that same image, and then you optimize your representations

### [31:36 - 31:43]

to be similar for images of the same person, and dissimilar for images of different people.

### [31:44 - 31:49]

Now, the main challenge in applying contrastive learning is defining what these augmentations are.

### [31:50 - 31:53]

Are you going to rotate the image? Are you going to change the colors, the saturation?

### [31:55 - 32:00]

What we're doing is we're doing augmentation using dynamics, using

### [32:00 - 32:00]

time.

### [32:00 - 32:07]

So what we're doing is we're saying, when we look at a video, if we take a frame of that

### [32:07 - 32:13]

video, we construct the augmented frame of that video by jumping forward in time. And that doesn't

### [32:13 - 32:17]

require any engineering, it simply requires data.

### [32:19 - 32:24]

Another way of seeing what these representations are doing is viewing them as a sort of embedding,

### [32:24 - 32:30]

a way of embedding time series data, so that states that occur nearby in time are

### [32:30 - 32:30]

given

### [32:30 - 32:37]

similar representations, and states that occur more distantly in time are given more distant

### [32:37 - 32:38]

representations.

### [32:38 - 32:43]

So the intuition here is that once we've learned these representations, we should be able to

### [32:43 - 32:47]

use them for figuring out what are the states I'm likely to visit when I want to go from

### [32:47 - 32:52]

one state to another state, and what are the best actions to take if I want to get from

### [32:52 - 32:56]

point A to point B.

### [32:56 - 33:00]

So let's see how that works. As an example, let's go back to this manipulation task that

### [33:00 - 33:06]

we started today's talk with. We want, we have this robot arm here, this robot arm can move up,

### [33:06 - 33:12]

down, left, right, forward, backwards, and it has a grip where it can open and close. And let's say

### [33:12 - 33:17]

that we want to navigate from this current state to this goal state shown here, where the key

### [33:17 - 33:21]

difference is that the robot arm has gone down and picked up the block and moved it into the blue

### [33:21 - 33:27]

bin. And as a thought experiment, let's imagine we just have two actions, A1 and A2.

### [33:27 - 33:29]

So let's imagine we just have two actions, A1 and A2.

### [33:29 - 33:30]

So let's imagine we just have two actions, A1 and A2.

### [33:30 - 33:36]

So we can think about these representations as points lying on a sphere. We'll assume for now

### [33:36 - 33:40]

the representations are normalized, so they lie on a sphere. It could be a very high-dimensional

### [33:40 - 33:48]

sphere. And because the state action representation depends on the action, for each of these actions,

### [33:48 - 33:54]

A1 and A2, we have different representations. And so if we just look at this picture here,

### [33:54 - 33:59]

we can compare the similarity between one state action representation and the goal representation,

### [33:59 - 34:03]

and another state action representation and the goal representation.

### [34:04 - 34:09]

And so just based on this figure here, I want to see a show of hands for who thinks we should take

### [34:09 - 34:22]

action A1. And show of hands for who thinks we should take action A2. And who is confused?

### [34:22 - 34:29]

Great.

### [34:30 - 34:36]

Okay. So yeah, after we've learned these representations, we can exactly look at their

### [34:36 - 34:41]

similarity to figure out what is the best action to take. And so here, it seems like A2 is the best

### [34:41 - 34:46]

action. So we will take action A2, and then we will get to some new state. And then based on

### [34:46 - 34:51]

this new state, we would do a similar computation, figuring out what is the best action to take here.

### [34:52 - 34:58]

And that's exactly how the method works. We define the policy as selecting whichever action A

### [34:59 - 35:01]

has a state action representation

### [35:01 - 35:05]

with a most similar dot product to the goal representation.

### [35:07 - 35:08]

So let's wrap this up.

### [35:08 - 35:10]

Let's see how the complete algorithm works.

### [35:11 - 35:15]

We start with data, a data set that's of not demonstration.

### [35:15 - 35:18]

It could just be of random data,

### [35:18 - 35:21]

of random state action pairs with no rewards.

### [35:21 - 35:24]

We then do this temporal contrastive learning

### [35:24 - 35:25]

to learn these representations,

### [35:25 - 35:29]

a state action representation and a goal representation.

### [35:29 - 35:32]

And then we use these representations

### [35:32 - 35:35]

to extract a goal-reaching policy,

### [35:35 - 35:38]

a goal condition policy that selects the actions

### [35:38 - 35:40]

given the state and the goal.

### [35:40 - 35:41]

Now, at this point, we can be done.

### [35:41 - 35:44]

We can take this policy and go solve your task.

### [35:45 - 35:46]

Or you could take this policy

### [35:46 - 35:48]

and go back and collect some more data.

### [35:48 - 35:50]

And depending on the problem setting you're in,

### [35:50 - 35:52]

sometimes collecting more data

### [35:52 - 35:54]

can further improve performance.

### [35:56 - 35:58]

Now, I think at this point,

### [35:58 - 35:59]

it's worth stepping back and providing

### [35:59 - 35:59]

a little bit of history.

### [35:59 - 36:02]

So we started this talk by saying,

### [36:02 - 36:04]

designing rewards is really hard.

### [36:04 - 36:06]

It's really frustrating for the graduate students

### [36:06 - 36:09]

to have to sit down and write those big blocks of red code.

### [36:10 - 36:14]

And so ordinarily, reinforcement learning requires defining

### [36:14 - 36:16]

and learning from a lot of rewards.

### [36:16 - 36:17]

And on the surface,

### [36:17 - 36:19]

it seems like these goal-conditioned

### [36:19 - 36:21]

reinforcement learning problems

### [36:21 - 36:23]

should require lots of rewards

### [36:23 - 36:26]

because now you're not solving one task, but many tasks.

### [36:27 - 36:29]

And this is typically how prior work

### [36:29 - 36:33]

has viewed these goal-conditioned RL problems.

### [36:33 - 36:35]

These goal-conditioned RL problems have been around

### [36:35 - 36:38]

for almost 60, 70 years.

### [36:38 - 36:42]

In fact, some of the earliest work in AI in the 1950s and 60s

### [36:42 - 36:45]

was working on goal-conditioned reinforcement learning.

### [36:45 - 36:47]

But typically, it's been viewed as a really,

### [36:47 - 36:48]

really challenging problem

### [36:48 - 36:51]

because you're solving not one problem, but many problems.

### [36:53 - 36:55]

But what we've seen here in this talk is that

### [36:55 - 36:56]

there's a way of defining

### [36:56 - 36:58]

these goal-conditioned reinforcement learning problems.

### [36:58 - 37:03]

In a way such that they don't require any rewards at all.

### [37:03 - 37:05]

And from an engineering perspective,

### [37:05 - 37:07]

this is really appealing because it means that

### [37:07 - 37:09]

you no longer have to define these rewards,

### [37:09 - 37:11]

that big giant red block of code,

### [37:11 - 37:14]

when you want to go solve some new problem.

### [37:14 - 37:15]

And aesthetically, we'll see how it draws

### [37:15 - 37:19]

some really nice connections to other areas of generative AI.

### [37:19 - 37:21]

And we'll see that in a couple of slides.

### [37:23 - 37:24]

So practically, this method,

### [37:24 - 37:28]

it ends up even outperforming methods that do use rewards.

### [37:28 - 37:30]

So here, I'm showing a visualization

### [37:30 - 37:34]

of what our approach does on this manipulation task

### [37:34 - 37:36]

when we tell the policy to try to get

### [37:36 - 37:38]

to this goal state up here.

### [37:38 - 37:40]

And a very good prior method

### [37:40 - 37:42]

completely fails to solve this task.

### [37:48 - 37:49]

We've shown this method outperforms

### [37:49 - 37:52]

a number of prior methods,

### [37:52 - 37:54]

but I now want to jump forward and highlight

### [37:54 - 37:56]

two really interesting applications

### [37:56 - 37:58]

that we've seen of these self-supervised reinforcement

### [37:58 - 38:00]

and learning methods.

### [38:01 - 38:02]

One is in robotic control.

### [38:02 - 38:05]

This is a collaboration done with Chongyi Cheng

### [38:05 - 38:06]

and Homer Wok.

### [38:06 - 38:08]

And so the problem that we were looking at

### [38:08 - 38:12]

was tabletop rearrangement.

### [38:12 - 38:14]

We have a robot shown up here,

### [38:14 - 38:16]

is this Widow X robot.

### [38:16 - 38:19]

It's a pretty low cost robot, it's a couple thousand dollars.

### [38:19 - 38:21]

And that makes it really fairly accessible.

### [38:21 - 38:23]

It's a couple of orders of magnitude cheaper

### [38:23 - 38:26]

than most robot arms today.

### [38:26 - 38:27]

But it also means that it's really hard to control

### [38:27 - 38:28]

because the plastic parts,

### [38:28 - 38:31]

where down the motors are kind of shaky.

### [38:33 - 38:37]

And we wanted to get the robot to rearrange the table.

### [38:37 - 38:40]

So it looks like this goal on the right-hand side.

### [38:40 - 38:42]

And there are two key differences between the image

### [38:42 - 38:44]

on the left and the image on the right.

### [38:44 - 38:47]

The first one is that the robot hand has moved

### [38:47 - 38:50]

to the upper left-hand side of the image.

### [38:50 - 38:53]

And the second is that this red spoon has moved

### [38:53 - 38:54]

to the left side of the image.

### [38:56 - 38:58]

And from a robotics perspective,

### [38:58 - 38:59]

there are a lot of things

### [38:59 - 39:02]

that makes this problem really challenging.

### [39:02 - 39:05]

First is that we're going to try to learn a policy

### [39:05 - 39:09]

that can do this manipulation problem from suboptimal data.

### [39:09 - 39:11]

We don't have any demonstrations.

### [39:11 - 39:14]

So we're going to be learning from a bunch of noisy data

### [39:14 - 39:16]

of the robot just doing random things.

### [39:18 - 39:19]

A second thing is that we don't know the positions

### [39:19 - 39:20]

of all the objects.

### [39:20 - 39:23]

We're doing this directly from pixels, from images.

### [39:25 - 39:26]

And third, we're going to do this in the setting where we can't see the object.

### [39:26 - 39:27]

And third, we're going to do this in the setting where we can't see the object.

### [39:27 - 39:29]

And third, we're going to do this in the setting where we can't learn by trial and error.

### [39:29 - 39:32]

But instead, we just have a fixed bucket of data.

### [39:32 - 39:34]

And from that fixed bucket of data,

### [39:34 - 39:37]

we're trying to pull out this goal-reaching policy.

### [39:38 - 39:39]

So there are a lot of things

### [39:39 - 39:41]

that make this problem really challenging.

### [39:41 - 39:42]

And so it's not surprising

### [39:42 - 39:45]

that the best prior method we could find,

### [39:45 - 39:46]

it fails to solve this task.

### [39:48 - 39:50]

And one thing you might notice is that this prior method,

### [39:50 - 39:52]

it fails in a sort of interesting way.

### [39:52 - 39:55]

It successfully moves the robot arm

### [39:55 - 39:57]

to this position on the left side of the screen.

### [39:57 - 39:59]

But it just ignores the spoon.

### [40:00 - 40:02]

And maybe that sort of makes sense.

### [40:02 - 40:04]

The spoon is only a small fraction of the image.

### [40:08 - 40:11]

Now, in contrast, when we evaluated our method,

### [40:11 - 40:14]

we found that the robot arm successfully went out of its way

### [40:14 - 40:16]

to pick up this red spoon

### [40:16 - 40:20]

and move it to the left side of the table and place it there.

### [40:20 - 40:22]

And then finally repositioned the robot arm

### [40:22 - 40:23]

in roughly the right position.

### [40:23 - 40:28]

And one thing I want to emphasize here

### [40:28 - 40:30]

is that it was able to learn how to do this

### [40:30 - 40:31]

without needing anyone to define

### [40:31 - 40:33]

those complex reward functions.

### [40:33 - 40:35]

The graduate students Changyi

### [40:35 - 40:37]

and Homer working on this project,

### [40:37 - 40:38]

they never had to sit down and write

### [40:38 - 40:41]

that big, giant, ugly block of red code.

### [40:43 - 40:47]

And because of that, they could use the same policy

### [40:47 - 40:49]

with no more training, with no more data,

### [40:49 - 40:51]

with no more gradient updates to solve new tasks

### [40:51 - 40:53]

just by prompting it with a new goal.

### [40:53 - 40:57]

So here we gave the robot a different goal,

### [40:57 - 41:02]

where now this can has been moved to the top of the table.

### [41:03 - 41:06]

And with no more training, we can just evaluate the policy.

### [41:11 - 41:12]

And we see that it roughly succeeds

### [41:12 - 41:14]

at solving this task as well.

### [41:17 - 41:19]

I think it's sort of interesting now to pop back up

### [41:19 - 41:21]

and think about the motivation at the start of this talk,

### [41:21 - 41:21]

when we were thinking about the generalization capabilities.

### [41:21 - 41:22]

I think it's sort of interesting now to pop back up and think about the motivation at the start of this talk, when we were thinking about the generalization capabilities.

### [41:22 - 41:24]

I think it's sort of interesting now to pop back up and think about the motivation at the start of this talk, when we were thinking about the generalization capabilities

### [41:24 - 41:26]

of language models and the generalization capabilities

### [41:26 - 41:28]

of vision models.

### [41:28 - 41:31]

The way we test the generalization capabilities there

### [41:31 - 41:32]

is by prompting those models

### [41:35 - 41:38]

with things that were not seen in the training data.

### [41:38 - 41:40]

And so note that we can do the same thing here.

### [41:40 - 41:43]

We can prompt this model with all sorts of images

### [41:43 - 41:45]

that it hasn't seen during training and see how well it does.

### [41:46 - 41:50]

And like those models, this reinforcement learning model

### [41:50 - 41:50]

is trained primarily on unlabeled data.

### [41:50 - 41:52]

is trained primarily on unlabeled data.

### [41:52 - 41:54]

In fact, it's trained entirely on unlabeled data.

### [41:55 - 41:57]

And so I think that these self-supervised methods

### [41:57 - 42:00]

are a really promising hint or promising approach

### [42:00 - 42:03]

for thinking about how we can develop

### [42:03 - 42:04]

reinforcement learning methods

### [42:04 - 42:06]

that exhibit the same sort of strong generalization

### [42:06 - 42:10]

capabilities that generative models in other domains do.

### [42:12 - 42:13]

And I want to briefly talk about

### [42:13 - 42:15]

one other interesting application.

### [42:15 - 42:18]

This one, we didn't take part in,

### [42:18 - 42:20]

but it is a really cool application

### [42:20 - 42:22]

of these contrastive reinforcement learning methods.

### [42:22 - 42:24]

This is done by some folks

### [42:24 - 42:26]

at a healthcare company nearby.

### [42:28 - 42:29]

They were controlling,

### [42:29 - 42:31]

they were looking at controlling ultrasound devices.

### [42:31 - 42:33]

There's this certain type of ultrasound device

### [42:33 - 42:35]

that you put down someone's throat,

### [42:35 - 42:38]

and then you can use this ultrasound to take pictures,

### [42:38 - 42:40]

ultrasound pictures of someone's heart.

### [42:41 - 42:43]

And this is a really challenging control problem.

### [42:43 - 42:45]

You have to just, this camera down here

### [42:45 - 42:48]

has all these knobs that you can control

### [42:48 - 42:51]

to focus the camera and to turn the camera around.

### [42:51 - 42:54]

And so the operators and the doctors

### [42:54 - 42:57]

controlling these cameras have a really hard time focusing

### [42:57 - 42:58]

and getting the correct images.

### [42:59 - 43:01]

So what this team did was they used

### [43:01 - 43:05]

these contrastive reinforcement learning methods

### [43:05 - 43:07]

to treat this as a goal-reaching problem.

### [43:07 - 43:11]

The goal here was a desired picture of someone's heart

### [43:11 - 43:14]

from a certain angle and a certain viewpoint.

### [43:14 - 43:16]

And after training, they gave the system

### [43:16 - 43:18]

this desired picture, and then the system

### [43:18 - 43:21]

could automatically figure out how do you change,

### [43:21 - 43:23]

these control parameters,

### [43:23 - 43:26]

so to get the ultrasound to take the desired picture.

### [43:28 - 43:29]

And I think this just emphasizes

### [43:29 - 43:31]

how these goal-reaching problems

### [43:31 - 43:33]

are potentially really widely applicable

### [43:33 - 43:36]

and how, because they don't need rewards,

### [43:36 - 43:39]

it makes it a lot easier for people in new domains

### [43:39 - 43:40]

to adopt these tools.

### [43:43 - 43:45]

So popping back up one level,

### [43:45 - 43:46]

we started this talk by emphasizing

### [43:46 - 43:49]

the key challenge in reinforcement learning.

### [43:49 - 43:51]

Typically when we talk about reinforcement learning,

### [43:51 - 43:52]

at least when I take reinforcement learning

### [43:52 - 43:54]

in my course here at Princeton,

### [43:54 - 43:56]

we assume that we're given the rewards.

### [43:56 - 43:58]

We assume, okay, someone gives you a game

### [43:58 - 44:00]

and you can read the score on the top right-hand corner.

### [44:01 - 44:03]

But a lot of practical problems

### [44:03 - 44:06]

don't have rewards readily accessible.

### [44:06 - 44:08]

And defining the rewards is a big challenge.

### [44:08 - 44:11]

And today we saw how by treating

### [44:11 - 44:13]

the reinforcement learning problem

### [44:13 - 44:14]

as a goal-reaching problem,

### [44:14 - 44:17]

we can avoid defining rewards.

### [44:19 - 44:20]

One of the key tricks that we saw for doing this is如果你city is

### [44:20 - 44:24]

doing this was to think about self-supervised learning. We thought about self-supervised

### [44:24 - 44:29]

learning and vision and language and how that was a really useful tool for giving rise to the

### [44:29 - 44:35]

powerful generative AI methods that we have today. And this method that I introduced, this temporal

### [44:35 - 44:41]

contrastive learning method, gave us an example of how we can use self-supervised learning

### [44:41 - 44:45]

for reinforcement learning. Now, in the next couple of slides, I want to argue that

### [44:45 - 44:50]

reinforcement learning is not actually that different from generative AI. In fact,

### [44:50 - 44:55]

when we think about self-supervised reinforcement learning, there's a sense in which it is a generative

### [44:55 - 44:58]

model. And now I'm going to walk you through what I mean here, because I think it helps

### [44:58 - 45:01]

really reframe what reinforcement learning methods are capable of.

### [45:03 - 45:09]

So let's think about what a generative model is. A generative model typically is trained on

### [45:09 - 45:15]

examples of images, say images of cats. And then to sample from that generative model,

### [45:15 - 45:20]

you perform some iterative procedure, typically going through some sequence of

### [45:20 - 45:25]

layers or iteratively denoising an image to produce a new sample.

### [45:27 - 45:30]

Now, reinforcement learning methods can be seen as doing something very, very similar.

### [45:31 - 45:37]

In particular, these goal-reaching methods were trained on a big dataset. And then

### [45:38 - 45:43]

to sample an outcome, we also performed iterative computation,

### [45:43 - 45:49]

where the policy would take an action and then the environment would give us some new observations.

### [45:50 - 45:53]

The policy would take another action, the environment would give us new observation.

### [45:53 - 45:58]

We would go around this loop many, many times iteratively. And then after doing this maybe

### [45:58 - 46:04]

a hundred times, we get some output. And so what reinforcement learning is it's just a different

### [46:04 - 46:12]

way of defining a way of sampling from a certain generative model. While our image generative models

### [46:13 - 46:19]

consist entirely of known parameters, this reinforcement learning generative model consists of

### [46:20 - 46:24]

of a combination of some policy parameters that we've trained

### [46:24 - 46:27]

and an environment that we don't even know.

### [46:28 - 46:29]

But at the end of the day,

### [46:29 - 46:31]

it gives us a way of sampling outcomes.

### [46:32 - 46:34]

Another way of seeing this is that

### [46:36 - 46:39]

when a lot of general image models today,

### [46:39 - 46:41]

you can prompt them, you give them a text description,

### [46:41 - 46:43]

such as a castle in the mountains,

### [46:43 - 46:45]

and they perform this iterative computation,

### [46:45 - 46:48]

iteratively denoising an image

### [46:48 - 46:51]

to eventually come to some desired outcome.

### [46:54 - 46:57]

How might we build reinforcement learning methods

### [46:57 - 46:58]

that do something similar,

### [46:58 - 47:00]

where we give them a prompt,

### [47:00 - 47:02]

say an image or a text description

### [47:02 - 47:05]

of build a castle surrounded by mountains,

### [47:05 - 47:07]

and then the robot performs hundreds or thousands

### [47:07 - 47:11]

or millions of actions to actually build that castle

### [47:11 - 47:13]

by interacting with the world.

### [47:14 - 47:18]

So again, we want to learn this mapping from an input prompt

### [47:18 - 47:20]

to an output state.

### [47:20 - 47:23]

Maybe an image, maybe language to an output state.

### [47:23 - 47:27]

But now we're thinking about mapping the inputs to the outputs

### [47:27 - 47:29]

by actually interacting with the environment.

### [47:31 - 47:34]

So I think that we can think about reinforcement learning

### [47:34 - 47:36]

as a generative model.

### [47:37 - 47:39]

And that's what I mean when I say that

### [47:39 - 47:40]

self-supervised reinforcement learning,

### [47:40 - 47:43]

it really is the sort of generative AI.

### [47:43 - 47:44]

So I think moving forward,

### [47:45 - 47:47]

we might see that generative AI methods,

### [47:47 - 47:53]

more like reinforcement learning methods rather than the sort of vision and language methods

### [47:53 - 47:58]

that we've seen before. And in the remaining of the talk, I want to highlight a couple

### [47:58 - 48:02]

of ongoing research efforts where we've started to push in this direction, where we've started

### [48:02 - 48:06]

to see what really is possible with these self-supervised methods.

### [48:08 - 48:13]

So I want to start with the elephant in the room. I've been primarily focusing on goal-reaching

### [48:13 - 48:18]

problems, but not every problem is a goal-reaching problem. How do you tackle problems beyond

### [48:18 - 48:24]

goal-reaching with self-supervised reinforcement learning? Well, to do that, we need to introduce

### [48:24 - 48:29]

a little bit of theory, trying to think about what mathematically are these representations

### [48:29 - 48:35]

learning. Before I said intuitively, they tell us the likelihood of getting from one

### [48:35 - 48:39]

state to some other state, but can we formalize that in math?

### [48:41 - 48:43]

Our key theoretical

### [48:43 - 48:43]

problem is that we don't have a goal-reaching problem. We don't have a goal-reaching problem

### [48:43 - 48:51]

as a result here is a relationship between these representations and Q values. In particular,

### [48:51 - 48:56]

you can prove that the dot product between these representations, the similarity between

### [48:56 - 49:03]

these representations, exactly correspond to a discounted sum of rewards. And this reward

### [49:03 - 49:07]

function here is a very natural one. It's the likelihood that your next state is equal

### [49:07 - 49:12]

to the goal. But conveniently, when we introduced this algorithm, we never actually computed

### [49:12 - 49:17]

this reward function. And so I'm introducing this reward function purely for analysis reasons.

### [49:17 - 49:25]

You never actually have to compute this. And what this theory tells us, for one, is that

### [49:25 - 49:30]

when we're comparing the similarity between these representations, that's not just a heuristic,

### [49:30 - 49:35]

but rather as a principled thing to do. Comparing these representations exactly corresponds

### [49:35 - 49:40]

to selecting actions that maximize your Q value. And that's the same thing that you

### [49:40 - 49:42]

saw that you probably have seen already in this course.

### [49:42 - 49:52]

And we'll see in a little bit how this same analysis gives us a way of solving problems

### [49:52 - 49:58]

beyond goal-reaching tasks. One small subtle note here is that up in this right-hand corner

### [49:58 - 50:04]

here, I have this beta. And what that means is that the algorithm I've introduced so far

### [50:04 - 50:12]

is estimating the Q value for the behavioral policy. The future expected rewards if you

### [50:12 - 50:17]

acted the same way that you did when you were collecting the data. Now, sometimes you

### [50:17 - 50:23]

might want to do a sort of Q-learning or SIRSA-style method, where you instead estimate the Q

### [50:23 - 50:28]

value that you would get if you were acting according to a different policy. And it turned

### [50:28 - 50:34]

out there's a way of adapting this contrastive learning procedure to do off-policy evaluation.

### [50:34 - 50:40]

And I'm going to skip over the details now, but the key idea is that you can do bootstrapping

### [50:40 - 50:42]

using these contrastive features.

### [50:42 - 50:47]

By comparing the similarities at one time step to the similarities at the next time

### [50:47 - 50:52]

step. It ends up closely resembling an idea known as the successor representation that's

### [50:52 - 51:01]

popular in neuroscience. So the key reason I bring up this theory is that by showing

### [51:01 - 51:06]

these representations encode probabilities, it gives us a way of solving problems beyond

### [51:06 - 51:11]

just goal-reaching problems. So for goal-reaching problems, we could use these representations

### [51:11 - 51:16]

to estimate the likelihood of getting to the desired goal state, and then for figuring

### [51:16 - 51:22]

out what is the best action to maximize that probability.

### [51:22 - 51:26]

Now there's some problems where there are multiple outcomes that are all good. Maybe

### [51:26 - 51:30]

you want to clean your bedroom, but there are several different configurations of your

### [51:30 - 51:34]

bedroom that could be called clean. You might not care about the order of the books on your

### [51:34 - 51:40]

bookshelf or the order of the pillows on your couch. And so there, to solve problems where

### [51:40 - 51:41]

there are multiple good outcomes, you might want to use the probability of getting to

### [51:41 - 51:53]

any of these outcomes. You can estimate the likelihood of getting to any of these good

### [51:53 - 51:57]

outcomes, and then taking actions that maximize the likelihood of getting to any of these

### [51:57 - 52:04]

good outcomes. Similarly, you can extend this to the setting

### [52:04 - 52:09]

where… to the fully general setting where you have a small number of states labeled

### [52:09 - 52:10]

with rewards.

### [52:11 - 52:15]

you know one state that has a reward of 8, one state that has a reward of 3, one state that has

### [52:15 - 52:20]

a reward of negative 10, another with a reward of negative 5. And given just these four states

### [52:20 - 52:24]

and the representations, you can estimate the likelihood of getting to the state with

### [52:24 - 52:30]

reward plus 8 and the likelihood of getting to the state with reward plus 3 and so on,

### [52:30 - 52:36]

and then select actions to maximize your future rewards, where your future rewards are just the

### [52:36 - 52:40]

likelihood of getting to each of these states times the reward at each of these four states.

### [52:42 - 52:47]

And we've shown that these extensions work very effectively. So the key takeaway here is that

### [52:47 - 52:53]

these representations are useful not just for solving goal-reaching problems, but also for

### [52:53 - 52:58]

solving more general reinforcement learning problems. Before going on to talking about some

### [52:58 - 53:02]

of the most recent research, I want to pause to see if there are any questions at this point.

### [53:11 - 53:19]

I have a quick question. Can you hear my voice?

### [53:19 - 53:21]

Yeah.

### [53:21 - 53:28]

Yeah. So in contrastive learning, we know that if we apply the augmentation in the regular

### [53:29 - 53:36]

case of self-supervised learning like SimCLR and techniques like that, if you apply augmentations

### [53:36 - 53:41]

that totally apply the same type of augmentation you're saying, like, you're getting a product,

### [53:41 - 53:48]

change the image there is no hope to learn a meaningful representation and we

### [53:48 - 53:56]

have to keep a balance between how much we change the image and whether or not

### [53:56 - 54:03]

the task that we are asking the encoder to solve being something trivial so if

### [54:03 - 54:11]

you apply to a small augmentation that also doesn't work so here it sounds like

### [54:11 - 54:17]

you pick an action that reaches some some goal state in the future and you

### [54:17 - 54:25]

treat those two those two state actions and goal state as positive pairs how do

### [54:25 - 54:31]

you make sure that the same problem doesn't happen here do you do you

### [54:31 - 54:36]

enforce a threshold on the on the time horizon that you expect that action to

### [54:36 - 54:41]

result in the goal state or do you have other mechanisms to make sure that

### [54:41 - 54:48]

that problem doesn't happen in practice we haven't found this to be a huge

### [54:48 - 54:55]

problem the most important parameter we have is this parameter that tells us how

### [54:55 - 54:58]

far into the future are we going to look

### [55:02 - 55:06]

so when we sample the future state here we're sampling it according to a

### [55:06 - 55:11]

geometric distribution with probability with parameter one minus gamma

### [55:11 - 55:18]

and so if we select a very small value of gamma like gamma equals 0.5 then the

### [55:18 - 55:22]

future states are mostly going to be one or two steps in the future and so it's a

### [55:22 - 55:26]

very easy classification problem if you select a very large value of gamma like

### [55:26 - 55:31]

gamma equals 0.999 then the future states are on average are going to be a thousand

### [55:31 - 55:35]

time steps in the future and that's going to be a very very challenging problem

### [55:36 - 55:41]

we found that the algorithm is pretty robust to this choice of gamma in practice we end up using

### [55:41 - 55:47]

a value of 0.99 but that's mostly to be consistent with prior work with the literature not because

### [55:47 - 55:55]

it works much better or worse than other values there is a kind of um there is one setting where

### [55:55 - 56:02]

this issue is definitely does show up and that's in settings where every trajectory when it's really

### [56:02 - 56:08]

easy to distinguish one trajectory from another trajectory for example let's imagine that I take

### [56:08 - 56:10]

a couple pictures out my window

### [56:11 - 56:17]

and or let's I or let's say that I take a video outside my window here and

### [56:18 - 56:25]

um then I take another video in uh next month another video the month after that

### [56:25 - 56:30]

the trees outside my window they're gonna look different every month and so even though I want

### [56:30 - 56:37]

these features to pick up temporal information within a single video the representation would

### [56:37 - 56:41]

probably just pick up how each video looks different from the previous video because

### [56:41 - 56:45]

one video doesn't have leaves on the trees and the next video does have leaves on the trees

### [56:46 - 56:51]

and so there's a variant of this method where instead of sampling the negative examples from

### [56:51 - 56:57]

different videos we sample them from the same video but just much further away in time

### [56:57 - 57:03]

and that can that increases the difficulty of the classification problem but can result in learning

### [57:03 - 57:08]

better features so I hope that answers the question literally it's not an issue but when it

### [57:08 - 57:11]

is an issue there are ways of combating it by thinking about

### [57:11 - 57:13]

how do you sample the negative examples

### [57:16 - 57:19]

um may I ask a question too absolutely

### [57:21 - 57:28]

I have many questions but I ask just some of them and my first question is um are really

### [57:28 - 57:35]

temporarily far estate far semantically because for example the for example the mountain car

### [57:35 - 57:40]

uh example the classic one when a car goes up and then goes down

### [57:41 - 57:49]

can be in very similar state for example to its initial state how do you contrast these two it's

### [57:49 - 57:55]

they are not really semantically away from each other this is a really really good point um the

### [57:57 - 58:05]

um and so when I say that uh we're learning representation so that the distance between

### [58:05 - 58:10]

the representations corresponds to the distance in time I'm saying this in an average sense

### [58:11 - 58:17]

and so you're absolutely right that there can be examples where states that occur states that were

### [58:17 - 58:25]

far apart in time uh actually are often occur nearby in time as well but part of the reason

### [58:25 - 58:29]

why I wanted to introduce this theory is it actually gives us some theoretical grounding

### [58:29 - 58:35]

for confidently saying yes these representations are telling us the correct thing they are telling

### [58:35 - 58:39]

us the likelihood of getting from one state to some other state at some point in time

### [58:41 - 58:47]

one way of seeing this is that um in that example you mentioned where you have the mountain car and

### [58:47 - 58:52]

let's say that you're looking at one state and a nearby state in that nearby state uh you could

### [58:52 - 58:57]

have gotten to it if you first went up the mountain and then down the mountain well the

### [58:57 - 59:02]

likelihood of sampling that transition is going to be much lower than the likelihood of sampling

### [59:02 - 59:09]

the transition where you just go from this position to this position because this shorter path because

### [59:09 - 59:10]

this the likelihood of sampling

### [59:11 - 59:20]

uh a start goal pair is depends on Gamma to the number of time steps that have elapsed and so

### [59:20 - 59:27]

you're much much more likely to sample this uh state goal pair along this first path when you

### [59:27 - 59:31]

went from the state to the goal then along this longer path when you first went from the state up

### [59:31 - 59:35]

the mountain and then down again in fact it's exponentially more likely to sample a shorter path

### [59:36 - 59:38]

and that's part of the reason why this doesn't end up being a problem

### [59:40 - 59:40]

okay

### [59:41 - 59:47]

thank you and I have two other questions another one is how do you deal with continuous action

### [59:47 - 59:53]

space and because you use argmax there and for continuous action space the only thing that I

### [59:53 - 59:59]

have in mind right now is to take gradient with respect to action gradient of difference between

### [59:59 - 01:00:05]

current state and the gold estate is it the only possible way or is any other way wrong

### [01:00:05 - 01:00:10]

yeah so in practice what we do is we do have you seen algorithms

### [01:00:10 - 01:00:13]

like DDPG or TD3

### [01:00:15 - 01:00:23]

yes yes cool so we did exactly the same thing that those algorithms do so we learn a policy that

### [01:00:23 - 01:00:29]

you're the objective for the policy is to sample actions that maximize this inner product

### [01:00:31 - 01:00:32]

hmm

### [01:00:33 - 01:00:35]

right saw

### [01:00:35 - 01:00:39]

just this algorithm is actually very easy to implement on top of an implementation of Meeting or

### [01:00:39 - 01:00:44]

SAC or T3 or GDPG, you simply modify your actor loss

### [01:00:45 - 01:00:49]

to instead of using the Q value, use this inner product

### [01:00:49 - 01:00:50]

and you modify your critic loss

### [01:00:50 - 01:00:54]

to instead of using the regular TD loss

### [01:00:54 - 01:00:55]

to use this contrastive loss.

### [01:00:57 - 01:00:58]

I see, I see, thank you.

### [01:00:58 - 01:01:00]

And for the last question,

### [01:01:00 - 01:01:05]

how do you deal with partially observable environments?

### [01:01:05 - 01:01:08]

Because in those states you cannot contrast observation

### [01:01:08 - 01:01:10]

with each other.

### [01:01:10 - 01:01:12]

They should be the full history or embedding of history

### [01:01:12 - 01:01:15]

and it is embedding on embedding, you know,

### [01:01:15 - 01:01:16]

it gets harder, I believe.

### [01:01:17 - 01:01:18]

That is an open problem.

### [01:01:18 - 01:01:19]

We haven't solved it yet.

### [01:01:22 - 01:01:24]

Oh, okay, thank you.

### [01:01:24 - 01:01:27]

I think the easiest way of doing it would be to do exactly

### [01:01:27 - 01:01:31]

like you suggested, to think about sequences of states

### [01:01:31 - 01:01:33]

and then use some sort of sequence model

### [01:01:33 - 01:01:37]

like an LSTM or a transformer, but we haven't tried that yet.

### [01:01:38 - 01:01:41]

And a spoons parlar with Farmer,

### [01:01:41 - 01:01:43]

we haven't translated it anything yet.

### [01:01:43 - 01:01:48]

Yeah, so is there any questions you want out of the talk?

### [01:01:48 - 01:01:49]

I see, thank you.

### [01:01:49 - 01:01:49]

Thank you.

### [01:01:52 - 01:01:54]

Any other questions before we move on?

### [01:01:57 - 01:01:58]

Yeah, go ahead.

### [01:02:03 - 01:02:04]

Do you have my voice.

### [01:02:04 - 01:02:08]

Perfect, I have a question about the goal condition RL.

### [01:02:08 - 01:02:08]

In will that condition RL, for example in vision task,

### [01:02:08 - 01:02:08]

on a recommended project cheese-f妹e communicationяг средe

### [01:02:08 - 01:02:15]

between the goal state and the current state does this limit our exploration in the environment

### [01:02:15 - 01:02:20]

because in each state that i am i want to close as possible to the goal state and maybe there

### [01:02:20 - 01:02:25]

are some states that are not really similar to the goal state at least in our future space

### [01:02:25 - 01:02:30]

and those can lead us to the better states i think this exploration may be

### [01:02:30 - 01:02:33]

a bit limitation for goal condition or i'm wrong

### [01:02:33 - 01:02:40]

to the contrary we find that the exploration is much stronger than alternative methods

### [01:02:42 - 01:02:45]

and in a couple slides i'll talk a little bit about this

### [01:02:46 - 01:02:51]

i think part of the reason why is that when we think about these goal-riching tasks

### [01:02:51 - 01:02:57]

we're only saying what we want the agent to do not how we want it to do it and because we are

### [01:02:57 - 01:03:02]

telling the agent how it should do it it has to automatically try to figure out what is the best

### [01:03:02 - 01:03:03]

way of how to do it and that's what we're trying to do and that's what we're trying to do and that's

### [01:03:03 - 01:03:06]

what we're trying to do and that's what we're trying to do um of solving the task and so for

### [01:03:06 - 01:03:08]

um of solving the task and so for example when you look at mazes we end up seeing

### [01:03:08 - 01:03:10]

example when you look at mazes we end up seeing pretty effective exploration uh exploring lots

### [01:03:10 - 01:03:12]

pretty effective exploration uh exploring lots of different parts of the maze before it eventually

### [01:03:12 - 01:03:13]

of different parts of the maze before it eventually finds the shortest path

### [01:03:18 - 01:03:18]

i see thank you

### [01:03:26 - 01:03:29]

great in these last few minutes i want to talk about some of the most recent research

### [01:03:29 - 01:03:32]

we've been doing using these contrastive methods

### [01:03:33 - 01:03:39]

we've been doing using these contrastive methods

### [01:03:39 - 01:03:43]

cool so our goal that like we started the talk with was thinking about

### [01:03:43 - 01:03:48]

how do we build reinforcement learning methods that are like generative models that could be

### [01:03:48 - 01:03:53]

prompted to do nearly everything i want to highlight some recent work that's taking some

### [01:03:53 - 01:04:03]

steps towards this so if we think about what have been the successes or what has helped cause these

### [01:04:03 - 01:04:08]

other areas of generative ai to be so successful i think perhaps the most important component is

### [01:04:08 - 01:04:14]

self-supervised feedback we've already seen today how we can build reinforcement learning methods

### [01:04:14 - 01:04:19]

with self-supervised feedback i think there are a couple other important ingredients one is the

### [01:04:19 - 01:04:25]

capacity to train on lots and lots of data two is the ability to use lots of compute and three is

### [01:04:25 - 01:04:29]

having standardized benchmarks so we can compare different methods on a level playing field

### [01:04:30 - 01:04:32]

so to get these next three benefits

### [01:04:33 - 01:04:38]

Together with some collaborators, we designed a new benchmark that allows us to compare methods

### [01:04:38 - 01:04:43]

on a level playing field and to use lots more compute and data to see how leveraging more

### [01:04:43 - 01:04:49]

compute and data can improve performance. And so this is a new benchmark that we've been calling

### [01:04:49 - 01:04:56]

JAX-GCRL. JAX is the programming language and goal condition reinforcement learning. There's

### [01:04:56 - 01:05:00]

a link to the repo down here. And I want to highlight some of the key properties of this

### [01:05:00 - 01:05:06]

benchmark that has made it really fun to use. The most important property is that it's really fast.

### [01:05:07 - 01:05:12]

When I was doing my PhD, it used to take several hours to a couple of days

### [01:05:12 - 01:05:19]

to run experiments that now just take a couple of minutes on one GPU. And so I think this has

### [01:05:19 - 01:05:24]

made the research process a lot more fun because now you can iterate on algorithms in a couple

### [01:05:24 - 01:05:29]

minutes. It makes the problem of algorithm design feel a lot more like data science.

### [01:05:30 - 01:05:36]

It also makes it a lot easier to run experiments for millions or billions of time steps.

### [01:05:37 - 01:05:40]

And previously, those experiments could only be done in industry with people that have lots and

### [01:05:40 - 01:05:47]

lots of GPUs. I want to highlight some of the tasks here. Some of them are pretty easy. Some

### [01:05:47 - 01:05:53]

of them are really hard and are still open problems. So one of the tasks is this embodied

### [01:05:53 - 01:06:00]

Sokoban problem where this quadruped is trying to run to a goal that's hidden back here in that first

### [01:06:00 - 01:06:07]

task to push this block out of the way to get there. Here we can see it. This next episode,

### [01:06:07 - 01:06:19]

I'm going to hide the goal over here. This next task is a football task where the ant

### [01:06:19 - 01:06:27]

has to dribble the soccer ball towards this location here. I see it's fairly good at football.

### [01:06:30 - 01:06:36]

And so this gives you a sense of the source of problems that these contrasted algorithms can

### [01:06:36 - 01:06:43]

solve. We also have a new benchmark that looks at the offline setting. So if you want to see,

### [01:06:43 - 01:06:48]

okay, if you just are given a fixed data set, what are the sorts of policies you can learn?

### [01:06:48 - 01:06:52]

This benchmark is a really great way of doing that. Both these benchmarks have really good

### [01:06:52 - 01:06:57]

documentation. And so if you're looking to get involved in the research, I'd highly recommend

### [01:06:57 - 01:06:58]

looking at these two benchmarks.

### [01:07:00 - 01:07:04]

The next thing I want to talk a little bit about is generalization.

### [01:07:08 - 01:07:13]

And so when we think about generalization and machine learning broadly, often we're thinking

### [01:07:13 - 01:07:19]

about generalization across perceptual differences. Say we want a neural network to produce

### [01:07:19 - 01:07:26]

similar outputs for an image and an augmented version of that same image. In this project,

### [01:07:26 - 01:07:28]

we were thinking about a kind of wacky

### [01:07:28 - 01:07:33]

notion of generalization that's unique to the reinforcement learning problem.

### [01:07:34 - 01:07:38]

This notion of generalization that we were calling horizon generalization.

### [01:07:39 - 01:07:44]

And the idea is that when we have a goal condition policy,

### [01:07:44 - 01:07:49]

if we give it a state action pair, sorry, a state goal pair, and it produces some action,

### [01:07:50 - 01:07:55]

if instead of telling it to get to a goal, we tell it to get to a waypoint

### [01:07:55 - 01:07:58]

on the route to that goal. So instead of trying to get really

### [01:07:58 - 01:08:03]

far away, just try to get to a first intermediate waypoint, you could take a similar action.

### [01:08:05 - 01:08:10]

And so this is a notion of invariance. You want your policy to produce similar actions

### [01:08:10 - 01:08:13]

for different inputs where or for transformed inputs.

### [01:08:14 - 01:08:20]

And what Kathy and Vivek proved is that if you have this invariance property,

### [01:08:20 - 01:08:26]

then your policy will generalize with respect to the horizon. And what I mean here is that

### [01:08:26 - 01:08:26]

you can now, if your policy satisfies this property, you can do something about that.

### [01:08:26 - 01:08:28]

And so there's a little

### [01:08:28 - 01:08:34]

property, you can train it on just easy tasks, say task reaching goals within the smaller

### [01:08:34 - 01:08:35]

circle.

### [01:08:35 - 01:08:42]

And then the policy provably will generalize to be able to reach goals that are more further

### [01:08:42 - 01:08:43]

away.

### [01:08:43 - 01:08:47]

And so I think this notion of generalization is really powerful for thinking about how

### [01:08:47 - 01:08:52]

do we build reinforcement learning agents that really can generalize new things that

### [01:08:52 - 01:08:57]

are radically different than those that they were trained on.

### [01:08:57 - 01:09:07]

We also have found that data augmentation can be pretty useful for achieving this generalization.

### [01:09:07 - 01:09:11]

So self-supervised reinforcement learning, it really can be seen as a form of generative

### [01:09:11 - 01:09:12]

AI.

### [01:09:12 - 01:09:18]

And if you want to figure out how do we build agents that can do anything, there are a couple

### [01:09:18 - 01:09:23]

of hints that we've seen over the last couple of months that this really should be possible.

### [01:09:23 - 01:09:26]

And I want to briefly highlight some of those hints.

### [01:09:26 - 01:09:32]

The first is that these representations seem to have really intriguing properties.

### [01:09:32 - 01:09:36]

And so before, when we were looking at the similarity between these representations,

### [01:09:36 - 01:09:39]

we actually can think about what these intermediate points, what these intermediate representations

### [01:09:39 - 01:09:41]

look like.

### [01:09:41 - 01:09:45]

So we start with a prior method, an alternative method, a variational autoencoder.

### [01:09:45 - 01:09:50]

If you visualize these intermediate waypoints, you end up seeing that the representations

### [01:09:50 - 01:09:56]

have captured the contents of the scene, but not anything about time.

### [01:09:56 - 01:10:03]

In contrast, with these temporal contrastive learning methods, these intermediate representations

### [01:10:03 - 01:10:08]

not only capture the contents of your image, but also how to solve the task.

### [01:10:08 - 01:10:11]

They also capture the physics.

### [01:10:11 - 01:10:17]

And so when you interpolate in representation space between this observation here and this

### [01:10:17 - 01:10:21]

observation here, you end up generating a plan.

### [01:10:21 - 01:10:22]

And this was entirely unexpected.

### [01:10:22 - 01:10:24]

We didn't expect this to happen.

### [01:10:24 - 01:10:25]

So let's look at this.

### [01:10:25 - 01:10:26]

So this is a very interesting example.

### [01:10:26 - 01:10:29]

But I think that this gives us some hints that these representations really are capturing

### [01:10:29 - 01:10:32]

useful bits of information.

### [01:10:32 - 01:10:39]

Since then, we've done some theory to actually prove why this interpolation should happen.

### [01:10:39 - 01:10:43]

The second interesting property that we've seen gets back to the question that was asked

### [01:10:43 - 01:10:45]

earlier about exploration.

### [01:10:45 - 01:10:51]

So typically, when we train these goal condition methods, we train them on goals of varying

### [01:10:51 - 01:10:52]

difficulties.

### [01:10:52 - 01:10:54]

And so when we collect the data, when we say, OK.

### [01:10:54 - 01:11:02]

Try to get to a very difficult goal, sometimes we say, try to get to an easier goal.

### [01:11:02 - 01:11:05]

Often we only actually care about the performance on one difficult goal.

### [01:11:05 - 01:11:10]

But our intuition, based on prior work, is that if you only collected data, if you only

### [01:11:10 - 01:11:17]

ever tried to get to a very, very distant goal, it would be very hard to do the exploration.

### [01:11:17 - 01:11:23]

But to our surprise, when we're using these temporal contrastive learning methods, doing

### [01:11:23 - 01:11:24]

data collection.

### [01:11:24 - 01:11:28]

By always commanding one difficult goal actually works.

### [01:11:28 - 01:11:38]

In fact, it often works better than collecting data using these goals of varying difficulties.

### [01:11:38 - 01:11:43]

And this actually pretty profoundly changed how I think about the exploration problem.

### [01:11:43 - 01:11:51]

Previously, I used to think that exploration happened by first finding a route to the goal

### [01:11:51 - 01:11:54]

and then finding faster and faster routes to the goal.

### [01:11:54 - 01:11:59]

But what this project showed is that even before these agents have ever found a path

### [01:11:59 - 01:12:04]

to the goal, the agent here is trying to move the green block to the blue bin.

### [01:12:04 - 01:12:07]

The agent here is trying to put the lid on the box.

### [01:12:07 - 01:12:13]

Even before these agents have ever successfully solved the task, they're starting to interesting

### [01:12:13 - 01:12:14]

exploration.

### [01:12:14 - 01:12:17]

They're starting to knock the blocks around, push the objects around.

### [01:12:17 - 01:12:22]

And so I think what this shows is that there's something about these contrastive reinforcement

### [01:12:22 - 01:12:23]

learning methods.

### [01:12:23 - 01:12:27]

That allows them to do really effective exploration even before they've ever solved the task for

### [01:12:27 - 01:12:28]

the first time.

### [01:12:28 - 01:12:36]

So he's only here around 19,000 trials when they first solved the task.

### [01:12:36 - 01:12:40]

And we see that similar things happen in the multi-agent setting, that there's a similar

### [01:12:40 - 01:12:43]

emergence of exploration here.

### [01:12:43 - 01:12:48]

And the last hint that we found pretty intriguing is that these methods benefit significantly

### [01:12:48 - 01:12:49]

from scale.

### [01:12:49 - 01:12:53]

So most reinforcement learning methods use architectures that are about four to five

### [01:12:53 - 01:12:55]

or four layers deep.

### [01:12:55 - 01:13:00]

And prior work has found that making networks deeper don't seem to increase performance.

### [01:13:00 - 01:13:04]

But with these self-supervised methods, we find that increasing the depth of networks

### [01:13:04 - 01:13:09]

can significantly, significantly improve performance.

### [01:13:09 - 01:13:14]

And I think the key reason why gets back to the start of this talk, that we're doing self-supervised

### [01:13:14 - 01:13:15]

learning.

### [01:13:15 - 01:13:18]

And because we're doing the self-supervised learning, what this means is that we're getting

### [01:13:18 - 01:13:20]

many bits of supervision for free.

### [01:13:20 - 01:13:23]

We're just extracting bits from these raw, unlinked layers.

### [01:13:23 - 01:13:24]

We're extracting multiple data.

### [01:13:24 - 01:13:28]

And because we're getting all of these extra bits for free, I think this helps explain

### [01:13:28 - 01:13:31]

why we're able to train models that are much, much bigger.

### [01:13:31 - 01:13:39]

And this, in turn, results in learning behaviors that more effectively solve a number of tasks.

### [01:13:39 - 01:13:40]

So I'm going to end there.

### [01:13:40 - 01:13:43]

I think that the key challenge in reinforcement learning today is rewards.

### [01:13:43 - 01:13:48]

I think self-supervised learning is a really, really powerful tool for figuring out how

### [01:13:48 - 01:13:51]

do we get the benefits of reinforcement learning without the challenges of designing rewards.

### [01:13:51 - 01:13:52]

And I think self-supervised learning is really, really powerful tool for figuring out how

### [01:13:52 - 01:13:53]

do we get the benefits of reinforcement learning without the challenges of designing rewards.

### [01:13:53 - 01:13:54]

And I think self-supervised learning is really, really powerful tool for figuring out how to

### [01:13:54 - 01:14:02]

build reinforcement learning agents that truly will be able to do anything, including things

### [01:14:02 - 01:14:05]

that are far beyond what they were trained to do.

### [01:14:05 - 01:14:09]

I'll end here, and I'm happy to take any questions for the remaining 30 minutes.

### [01:14:09 - 01:14:10]

Thank you.

### [01:14:10 - 01:14:14]

Oh, one last note.

### [01:14:14 - 01:14:20]

If you want to get involved in the research, here is a link to the repository for the codebase

### [01:14:20 - 01:14:23]

that I talked about in the middle of the talk.

### [01:14:23 - 01:14:26]

Thank you so much, Benjamin.

### [01:14:26 - 01:14:28]

I have a quick question.

### [01:14:28 - 01:14:38]

So in training LLMs, RL has recently been found to be a success story, like the deep

### [01:14:38 - 01:14:42]

secret story and other things.

### [01:14:42 - 01:14:49]

So do you believe that these methods that you introduced in this talk, could they be

### [01:14:49 - 01:14:51]

useful in that context as well?

### [01:14:51 - 01:14:52]

What's your take on that?

### [01:14:52 - 01:14:53]

Absolutely.

### [01:14:53 - 01:14:57]

In fact, we're currently working on it.

### [01:14:57 - 01:15:03]

The methods like the deep seek R1 method are really, really powerful for certain types

### [01:15:03 - 01:15:07]

of problems, for problems where it's easy to define the rewards.

### [01:15:07 - 01:15:12]

You might notice that most of the successes of reinforcement learning for language models

### [01:15:12 - 01:15:16]

are in settings where the rewards are easy to define, where you have these nice verifiable

### [01:15:16 - 01:15:17]

rewards.

### [01:15:17 - 01:15:22]

Now, this explains why the language models are really effective at things like deep seek,

### [01:15:22 - 01:15:29]

where you can write test cases to check the correctness of code, and math, where we already

### [01:15:29 - 01:15:32]

have proof checkers that can check whether your proof is correct.

### [01:15:32 - 01:15:39]

But in settings like dialogue, it's a lot harder to define a reward function for saying,

### [01:15:39 - 01:15:44]

did the chatbot convince the patient to take their medication every day.

### [01:15:44 - 01:15:50]

And my hope is that there are all these potential applications of language modeling that will

### [01:15:50 - 01:15:51]

be unlocked by thinking about these first steps.

### [01:15:51 - 01:15:54]

thinking about these problems as goal region problems.

### [01:15:57 - 01:15:58]

I see, thank you so much.

### [01:16:05 - 01:16:07]

I also have a question.

### [01:16:07 - 01:16:12]

My question is why doing greedy action is good here,

### [01:16:13 - 01:16:16]

but not good in RL itself, you know?

### [01:16:16 - 01:16:20]

What you're doing here is taking greedy action

### [01:16:20 - 01:16:24]

that makes you closer to the representation

### [01:16:24 - 01:16:26]

of goal state that you want to go.

### [01:16:27 - 01:16:32]

I claim that there could be a path that is closer,

### [01:16:34 - 01:16:36]

but not in embedding the space.

### [01:16:36 - 01:16:39]

I don't know how to phrase it correctly,

### [01:16:39 - 01:16:42]

but I just want to know why greedy action is good here.

### [01:16:43 - 01:16:46]

I agree this is super counterintuitive.

### [01:16:46 - 01:16:48]

If we think about solving a maze,

### [01:16:48 - 01:16:49]

greedy action selection

### [01:16:49 - 01:16:51]

is not a good idea.

### [01:16:51 - 01:16:54]

My, another example, my office is on the second floor.

### [01:16:54 - 01:16:57]

So if I want to get down to the road down there,

### [01:16:57 - 01:16:59]

I could try to jump out my window.

### [01:16:59 - 01:17:02]

That is the, of course, greedy action selection,

### [01:17:02 - 01:17:04]

but it very obviously is not the best way

### [01:17:04 - 01:17:05]

of getting outside the building.

### [01:17:05 - 01:17:08]

I should take the stairs, not jump out the window.

### [01:17:09 - 01:17:12]

Part of the reason why the theory here is important

### [01:17:12 - 01:17:14]

is that it helps explain why greedy selection,

### [01:17:14 - 01:17:17]

greedy action selection is useful.

### [01:17:17 - 01:17:19]

I assume you've probably seen the policy improvement theorem.

### [01:17:19 - 01:17:21]

In your course.

### [01:17:21 - 01:17:24]

And what that says is that choosing actions

### [01:17:24 - 01:17:27]

that maximize the Q value, that's the right thing to do.

### [01:17:27 - 01:17:30]

If you repeat that, you'll eventually get awful policy.

### [01:17:30 - 01:17:33]

And so showing that greedy action selection

### [01:17:34 - 01:17:37]

corresponds to selecting actions that maximize the Q value.

### [01:17:37 - 01:17:39]

This helps give us some reassurance

### [01:17:39 - 01:17:42]

that greedy action selection is actually a good idea.

### [01:17:44 - 01:17:45]

Oh, I see.

### [01:17:45 - 01:17:46]

I see.

### [01:17:46 - 01:17:47]

Now it makes sense.

### [01:17:47 - 01:17:48]

Thank you.

### [01:17:49 - 01:17:50]

Bye-bye.

### [01:17:50 - 01:17:51]

Bye-bye.

### [01:17:51 - 01:17:52]

Bye-bye.

### [01:17:52 - 01:17:52]

Bye-bye.

### [01:17:52 - 01:17:53]

Bye-bye.

### [01:17:53 - 01:17:55]

Bye-bye.

### [01:17:55 - 01:17:56]

Bye-bye.

### [01:17:56 - 01:17:57]

Bye-bye.

### [01:17:57 - 01:17:58]

Bye-bye.

### [01:17:58 - 01:17:58]

Bye-bye.

### [01:17:58 - 01:17:59]

Bye-bye.

### [01:17:59 - 01:18:01]

Hi, do you have my voice?

### [01:18:01 - 01:18:03]

Perfect.

### [01:18:03 - 01:18:05]

And thank you for awesome presentation.

### [01:18:05 - 01:18:08]

I have a question about negative samples

### [01:18:08 - 01:18:10]

and how we choose them, actually.

### [01:18:10 - 01:18:13]

This question comes to my mind from studies

### [01:18:13 - 01:18:17]

about debiasing contrastive learning in computer vision.

### [01:18:17 - 01:18:18]

I see.

### [01:18:18 - 01:18:25]

question is to what extent could that be important here are there any positive correlations that

### [01:18:25 - 01:18:34]

we punish in our contrasting loss can you elaborate a bit uh okay yeah actually i wonder

### [01:18:34 - 01:18:41]

um when we punish our negative samples within our batch could we have some positive correlations

### [01:18:41 - 01:18:46]

between the positive trajectory and the negative trajectory for example we could have um some

### [01:18:46 - 01:18:55]

certain robot movements in our trajectory but toward different goals so should we classify

### [01:18:55 - 01:19:04]

them as negative samples to each other or not i'm not entirely sure i understand the question

### [01:19:04 - 01:19:07]

i think one thing that definitely is true is that sometimes

### [01:19:07 - 01:19:13]

the the samples that you use as negatives i'll be able to go back to um

### [01:19:16 - 01:19:23]

the the negative samples here sometimes the negative examples are actually positive examples

### [01:19:23 - 01:19:28]

sometimes we get it wrong but that's actually okay because what's important for classification

### [01:19:28 - 01:19:34]

is the frequency with which something occurs as a positive example versus a negative example and the

### [01:19:34 - 01:19:39]

representations are basically encoding the relative frequency of positive examples versus

### [01:19:39 - 01:19:44]

negative examples formally this problem is solved by a positive example versus a negative example

### [01:19:44 - 01:19:46]

and that's what we're trying to do here

### [01:19:46 - 01:19:50]

and i think that's something that's something to really provide a better understanding of

### [01:19:50 - 01:19:56]

how we can use this information and learn how it can also be improved so what do we do

### [01:19:56 - 01:19:59]

so this is something that's sometimes known as positive unlabeled classification

### [01:20:00 - 01:20:03]

thank you thank you so much

### [01:20:16 - 01:20:33]

If folks also have questions about just like the research in general or reinforcement learning or graduate school or anything else feel free to ask those questions as well.

### [01:20:33 - 01:20:53]

Why if you do a PhD in reinforcement learning.

### [01:20:53 - 01:20:59]

I have another question since nobody asked question I have a lot of them, I can ask.

### [01:20:59 - 01:21:01]

So more questions.

### [01:21:01 - 01:21:03]

My question is, how do you define.

### [01:21:03 - 01:21:13]

The reward in that program that you showed us that it is equivalent to maximizing the return, not the reward itself.

### [01:21:13 - 01:21:27]

And what is the reward that how do you define the reward that is equal to achieving the goal.

### [01:21:27 - 01:21:32]

So how is the reward here defined.

### [01:21:32 - 01:21:33]

Yes, exactly.

### [01:21:33 - 01:21:35]

So this is purely for analysis.

### [01:21:35 - 01:21:43]

What you can prove is that the inner product here is equivalent to the discounted sum of rewards for the reward is the likelihood of getting to a state at the next time step.

### [01:21:43 - 01:21:45]

In tabular settings.

### [01:21:45 - 01:21:47]

This is just a one.

### [01:21:47 - 01:21:50]

If you're at the goal and a 0, if you're not at the goal.

### [01:21:50 - 01:21:54]

So, I think the tabular setting is a bit easier to think about.

### [01:21:54 - 01:21:56]

Okay, I see.

### [01:21:56 - 01:22:01]

Thank you.

### [01:22:01 - 01:22:02]

Okay.

### [01:22:02 - 01:22:12]

Thank you.

### [01:22:12 - 01:22:14]

Another question from my site, Benjamin.

### [01:22:14 - 01:22:26]

So you mentioned why taking a PhD be the thesis defined on RL and that is the question for many of my graduate students here at Sharif.

### [01:22:26 - 01:22:27]

You're saying that.

### [01:22:27 - 01:22:30]

So this is this mostly applies to the master students actually.

### [01:22:30 - 01:22:35]

Where it takes like two years for the research to be completed.

### [01:22:35 - 01:22:50]

So some of them asked why we should work on RL problems because, you know, it's quite unlikely to gain some significant achievements in such a short period of time.

### [01:22:50 - 01:22:52]

So what is your take on that?

### [01:22:52 - 01:22:53]

Do you believe?

### [01:22:53 - 01:22:58]

Could we do quick researches on reinforcement learning in two years or so?

### [01:22:58 - 01:23:03]

Or it should be subject of a PhD studies.

### [01:23:03 - 01:23:08]

I definitely think we can.

### [01:23:08 - 01:23:10]

And as a couple of examples of this.

### [01:23:10 - 01:23:14]

I used to talk about, like, the timeline for several of these things.

### [01:23:14 - 01:23:19]

So, this project that Grayson Michael worked on grace was a master student.

### [01:23:19 - 01:23:20]

Michael is an undergrad.

### [01:23:20 - 01:23:25]

And they completed this project in about 6 months.

### [01:23:25 - 01:23:26]

And so.

### [01:23:26 - 01:23:27]

Uh.

### [01:23:27 - 01:23:30]

That's very doable.

### [01:23:30 - 01:23:32]

Um.

### [01:23:32 - 01:23:35]

This project that try you and look worked on.

### [01:23:35 - 01:23:38]

Try you and look at with undergraduate students.

### [01:23:38 - 01:23:41]

And they completed this project in less than 6 months.

### [01:23:41 - 01:23:43]

On top of their coursework.

### [01:23:43 - 01:23:46]

Um.

### [01:23:46 - 01:23:50]

And similarly, this project that Kevin and Sean worked on.

### [01:23:50 - 01:23:54]

Uh, honestly, it was probably.

### [01:23:54 - 01:23:55]

Uh, October, February.

### [01:23:55 - 01:23:56]

Like four or five months.

### [01:23:56 - 01:23:57]

And so it's very, very possible to.

### [01:23:57 - 01:23:58]

Amazing research in a short amount of time.

### [01:23:58 - 01:23:59]

Cool.

### [01:23:59 - 01:24:00]

Um, that's awesome.

### [01:24:00 - 01:24:01]

So, uh, are these projects, uh, did these projects require some significant computational resources as well?

### [01:24:01 - 01:24:02]

Or.

### [01:24:02 - 01:24:03]

Uh, it was just like conventional.

### [01:24:03 - 01:24:04]

Uh.

### [01:24:04 - 01:24:05]

Amount of resources.

### [01:24:05 - 01:24:06]

This.

### [01:24:06 - 01:24:07]

The project that Kevin and Sean worked on did require a fair number of people.

### [01:24:07 - 01:24:08]

Uh.

### [01:24:08 - 01:24:09]

Uh.

### [01:24:09 - 01:24:10]

Uh.

### [01:24:10 - 01:24:11]

Uh.

### [01:24:11 - 01:24:12]

Uh.

### [01:24:12 - 01:24:13]

Uh.

### [01:24:13 - 01:24:14]

Uh.

### [01:24:14 - 01:24:15]

Uh.

### [01:24:15 - 01:24:16]

Uh.

### [01:24:16 - 01:24:17]

Uh.

### [01:24:17 - 01:24:18]

Uh.

### [01:24:18 - 01:24:19]

Uh.

### [01:24:19 - 01:24:20]

Uh.

### [01:24:20 - 01:24:21]

Uh.

### [01:24:21 - 01:24:22]

Uh.

### [01:24:22 - 01:24:23]

Uh.

### [01:24:23 - 01:24:24]

Uh.

### [01:24:24 - 01:24:25]

Uh.

### [01:24:25 - 01:24:26]

Uh.

### [01:24:26 - 01:24:27]

Uh.

### [01:24:27 - 01:24:28]

Uh.

### [01:24:28 - 01:24:29]

Uh.

### [01:24:29 - 01:24:30]

Uh.

### [01:24:30 - 01:24:31]

Uh.

### [01:24:31 - 01:24:32]

Uh.

### [01:24:32 - 01:24:33]

Uh.

### [01:24:33 - 01:24:34]

Uh.

### [01:24:34 - 01:24:35]

Uh.

### [01:24:35 - 01:24:36]

Uh.

### [01:24:36 - 01:24:37]

Uh.

### [01:24:37 - 01:24:38]

Uh.

### [01:24:38 - 01:24:39]

Uh.

### [01:24:39 - 01:24:40]

Uh.

### [01:24:40 - 01:24:41]

Uh.

### [01:24:41 - 01:24:42]

Uh.

### [01:24:42 - 01:24:43]

Uh.

### [01:24:43 - 01:24:44]

Uh.

### [01:24:44 - 01:24:45]

Uh.

### [01:24:45 - 01:24:46]

Uh.

### [01:24:46 - 01:24:47]

Uh.

### [01:24:47 - 01:24:48]

Uh.

### [01:24:48 - 01:24:49]

Uh.

### [01:24:49 - 01:24:50]

Uh.

### [01:24:50 - 01:24:51]

Uh.

### [01:24:51 - 01:24:52]

Uh.

### [01:24:52 - 01:24:53]

Uh.

### [01:24:53 - 01:24:54]

Uh.

### [01:24:54 - 01:24:55]

Uh.

### [01:24:55 - 01:25:00]

you'd be able to get by with one GPU per person.

### [01:25:03 - 01:25:05]

I see, I see.

### [01:25:05 - 01:25:06]

Thank you so much.

### [01:25:08 - 01:25:11]

So Arash, is there any question left?

### [01:25:13 - 01:25:15]

I don't think so.

### [01:25:15 - 01:25:17]

I don't see any question from the audience.

### [01:25:20 - 01:25:25]

So I think we can finish the talk here.

### [01:25:26 - 01:25:27]

If there's no other question.

### [01:25:31 - 01:25:35]

Okay, so thank you professor for accepting our invites

### [01:25:35 - 01:25:40]

and we had a wonderful time having you giving us the time.

### [01:25:42 - 01:25:43]

Thank you again for the invite.

### [01:25:43 - 01:25:45]

I really enjoyed all the questions.

### [01:25:45 - 01:25:48]

Thank you and have a good rest of the day.

### [01:25:48 - 01:25:50]

Thank you so much.

### [01:25:50 - 01:25:51]

Have a nice day.

### [01:25:55 - 01:25:56]

Thank you.
