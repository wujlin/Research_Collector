# RL Theory Seminar 2025: Max Simchowitz (April 29)

- URL: https://www.youtube.com/watch?v=WmAjzJQD6U4
- Source: `youtube_vtt_caption`
- Caption file: `youtube/captions/max-simchowitz-pitfalls-imitation-learning-continuous-actions/source.en-orig.vtt`
- Generated at: `2026-06-13T10:58:42`

## Transcript

### [00:05 - 00:05]

Okay, so the recording started so we can

### [00:05 - 00:09]

Okay, so the recording started so we can start. Okay. Um, welcome everyone.

### [00:09 - 00:09]

start. Okay. Um, welcome everyone.

### [00:09 - 00:11]

start. Okay. Um, welcome everyone. Thanks for coming to the RL theory

### [00:11 - 00:11]

Thanks for coming to the RL theory

### [00:11 - 00:13]

Thanks for coming to the RL theory seminar. I guess this is the first in a

### [00:13 - 00:13]

seminar. I guess this is the first in a

### [00:13 - 00:15]

seminar. I guess this is the first in a series of talks we'll do for the I don't

### [00:15 - 00:15]

series of talks we'll do for the I don't

### [00:15 - 00:18]

series of talks we'll do for the I don't know mid the spring quarter or whatever.

### [00:18 - 00:18]

know mid the spring quarter or whatever.

### [00:18 - 00:20]

know mid the spring quarter or whatever. Um, the first talk for the for the

### [00:20 - 00:20]

Um, the first talk for the for the

### [00:20 - 00:23]

Um, the first talk for the for the series is by Max Simcoitz. Um, it's my

### [00:23 - 00:23]

series is by Max Simcoitz. Um, it's my

### [00:23 - 00:24]

series is by Max Simcoitz. Um, it's my great pleasure to introduce him. I've

### [00:24 - 00:24]

great pleasure to introduce him. I've

### [00:24 - 00:27]

great pleasure to introduce him. I've known Max for like almost 10 years and

### [00:27 - 00:27]

known Max for like almost 10 years and

### [00:27 - 00:29]

known Max for like almost 10 years and in that time he's had quite a you know

### [00:29 - 00:29]

in that time he's had quite a you know

### [00:29 - 00:32]

in that time he's had quite a you know dynamic research career spanning topics

### [00:32 - 00:32]

dynamic research career spanning topics

### [00:32 - 00:34]

dynamic research career spanning topics in learning theory, core reinforcement

### [00:34 - 00:34]

in learning theory, core reinforcement

### [00:34 - 00:37]

in learning theory, core reinforcement learning theory, control, fairness, all

### [00:37 - 00:37]

learning theory, control, fairness, all

### [00:37 - 00:40]

learning theory, control, fairness, all sorts of things. He's very strong, very

### [00:40 - 00:40]

sorts of things. He's very strong, very

### [00:40 - 00:45]

sorts of things. He's very strong, very capable. Um he did his PhD at Berkeley.

### [00:45 - 00:45]

capable. Um he did his PhD at Berkeley.

### [00:45 - 00:47]

capable. Um he did his PhD at Berkeley. He spent some time at MIT as a posttock

### [00:47 - 00:47]

He spent some time at MIT as a posttock

### [00:47 - 00:49]

He spent some time at MIT as a posttock and now he just started as an assistant

### [00:49 - 00:49]

and now he just started as an assistant

### [00:49 - 00:51]

and now he just started as an assistant professor at Carnegie Melon. and um he's

### [00:51 - 00:51]

professor at Carnegie Melon. and um he's

### [00:51 - 00:53]

professor at Carnegie Melon. and um he's going to tell us about imitation

### [00:53 - 00:53]

going to tell us about imitation

### [00:53 - 00:56]

going to tell us about imitation learning in continuous spaces and I

### [00:56 - 00:56]

learning in continuous spaces and I

### [00:56 - 00:59]

learning in continuous spaces and I guess some pitfalls there. Um just for

### [00:59 - 00:59]

guess some pitfalls there. Um just for

### [00:59 - 01:01]

guess some pitfalls there. Um just for admin stuff I think it's okay to do

### [01:01 - 01:01]

admin stuff I think it's okay to do

### [01:01 - 01:03]

admin stuff I think it's okay to do questions during this during the talk if

### [01:03 - 01:03]

questions during this during the talk if

### [01:03 - 01:04]

questions during this during the talk if you don't want to do that you can like

### [01:04 - 01:04]

you don't want to do that you can like

### [01:04 - 01:06]

you don't want to do that you can like raise your hand I'll monitor or you can

### [01:06 - 01:06]

raise your hand I'll monitor or you can

### [01:06 - 01:07]

raise your hand I'll monitor or you can just type in the chat and I'll interrupt

### [01:07 - 01:07]

just type in the chat and I'll interrupt

### [01:07 - 01:09]

just type in the chat and I'll interrupt or you can also interrupt I guess uh as

### [01:09 - 01:09]

or you can also interrupt I guess uh as

### [01:09 - 01:12]

or you can also interrupt I guess uh as appropriate. Um with that Max take it

### [01:12 - 01:12]

appropriate. Um with that Max take it

### [01:12 - 01:15]

appropriate. Um with that Max take it away. Hi every thanks for thanks for the

### [01:15 - 01:15]

away. Hi every thanks for thanks for the

### [01:15 - 01:17]

away. Hi every thanks for thanks for the introduction and thanks everyone who

### [01:17 - 01:17]

introduction and thanks everyone who

### [01:17 - 01:18]

introduction and thanks everyone who took the time to make it to the to the

### [01:18 - 01:18]

took the time to make it to the to the

### [01:18 - 01:21]

took the time to make it to the to the seminar. Uh yeah. So um maybe a little

### [01:21 - 01:22]

seminar. Uh yeah. So um maybe a little

### [01:22 - 01:23]

seminar. Uh yeah. So um maybe a little bit about my journey before I begin is I

### [01:23 - 01:24]

bit about my journey before I begin is I

### [01:24 - 01:25]

bit about my journey before I begin is I I did sort of a PhD in kind of more

### [01:25 - 01:26]

I did sort of a PhD in kind of more

### [01:26 - 01:27]

I did sort of a PhD in kind of more traditional learning theory, but I had

### [01:27 - 01:27]

traditional learning theory, but I had

### [01:27 - 01:28]

traditional learning theory, but I had the fortune to spend a few years in a

### [01:28 - 01:28]

the fortune to spend a few years in a

### [01:28 - 01:31]

the fortune to spend a few years in a robot learning lab, a robot lab in MIT.

### [01:31 - 01:31]

robot learning lab, a robot lab in MIT.

### [01:31 - 01:33]

robot learning lab, a robot lab in MIT. And I think it's really changed how I

### [01:33 - 01:33]

And I think it's really changed how I

### [01:33 - 01:35]

And I think it's really changed how I think about some of the problems and how

### [01:35 - 01:36]

think about some of the problems and how

### [01:36 - 01:37]

think about some of the problems and how it it's caused me to reflect on how some

### [01:37 - 01:37]

it it's caused me to reflect on how some

### [01:37 - 01:39]

it it's caused me to reflect on how some of the assumptions that we make in RL

### [01:39 - 01:39]

of the assumptions that we make in RL

### [01:39 - 01:41]

of the assumptions that we make in RL and RL theory uh might need to be

### [01:41 - 01:41]

and RL theory uh might need to be

### [01:41 - 01:43]

and RL theory uh might need to be adjusted if we start thinking about the

### [01:43 - 01:43]

adjusted if we start thinking about the

### [01:43 - 01:45]

adjusted if we start thinking about the continuous action world. And so I'm

### [01:45 - 01:45]

continuous action world. And so I'm

### [01:45 - 01:46]

continuous action world. And so I'm going to present some work that kind of

### [01:46 - 01:46]

going to present some work that kind of

### [01:46 - 01:48]

going to present some work that kind of tries to make some of these points a

### [01:48 - 01:48]

tries to make some of these points a

### [01:48 - 01:50]

tries to make some of these points a little bit more clear.

### [01:50 - 01:50]

little bit more clear.

### [01:50 - 01:54]

little bit more clear. So um maybe it's kind of every talk in

### [01:54 - 01:54]

So um maybe it's kind of every talk in

### [01:54 - 01:55]

So um maybe it's kind of every talk in machine learning it feels like one is

### [01:55 - 01:55]

machine learning it feels like one is

### [01:55 - 01:57]

machine learning it feels like one is obligated to begin with language models

### [01:57 - 01:57]

obligated to begin with language models

### [01:57 - 01:59]

obligated to begin with language models and so you know one way to view language

### [01:59 - 01:59]

and so you know one way to view language

### [01:59 - 02:01]

and so you know one way to view language models is uh just some form of expert

### [02:01 - 02:01]

models is uh just some form of expert

### [02:01 - 02:03]

models is uh just some form of expert learning or learning from an expert

### [02:03 - 02:03]

learning or learning from an expert

### [02:03 - 02:04]

learning or learning from an expert right so we can view natural human

### [02:04 - 02:04]

right so we can view natural human

### [02:04 - 02:06]

right so we can view natural human language as an admittedly imperfect

### [02:06 - 02:06]

language as an admittedly imperfect

### [02:06 - 02:08]

language as an admittedly imperfect expert and here what we're trying to do

### [02:08 - 02:08]

expert and here what we're trying to do

### [02:08 - 02:10]

expert and here what we're trying to do is condition on observations in this

### [02:10 - 02:10]

is condition on observations in this

### [02:10 - 02:12]

is condition on observations in this case sequences of previous tokens and

### [02:12 - 02:12]

case sequences of previous tokens and

### [02:12 - 02:14]

case sequences of previous tokens and the action that we're trying to predict

### [02:14 - 02:14]

the action that we're trying to predict

### [02:14 - 02:15]

the action that we're trying to predict is simply what is the next token in the

### [02:15 - 02:16]

is simply what is the next token in the

### [02:16 - 02:18]

is simply what is the next token in the sentence that we want right a natural

### [02:18 - 02:18]

sentence that we want right a natural

### [02:18 - 02:19]

sentence that we want right a natural model of what's going on in in

### [02:19 - 02:19]

model of what's going on in in

### [02:19 - 02:21]

model of what's going on in in languages. Uh and we can think about a

### [02:21 - 02:21]

languages. Uh and we can think about a

### [02:21 - 02:23]

languages. Uh and we can think about a similar paradigm occurring in large

### [02:23 - 02:23]

similar paradigm occurring in large

### [02:23 - 02:24]

similar paradigm occurring in large robotics models as well. Right? So right

### [02:24 - 02:24]

robotics models as well. Right? So right

### [02:24 - 02:26]

robotics models as well. Right? So right now people are are actively collecting

### [02:26 - 02:26]

now people are are actively collecting

### [02:26 - 02:28]

now people are are actively collecting data to train large foundation models

### [02:28 - 02:28]

data to train large foundation models

### [02:28 - 02:30]

data to train large foundation models for robots. And again with one way

### [02:30 - 02:30]

for robots. And again with one way

### [02:30 - 02:31]

for robots. And again with one way they're doing this is they're collecting

### [02:31 - 02:32]

they're doing this is they're collecting

### [02:32 - 02:34]

they're doing this is they're collecting large amounts of human demonstrations.

### [02:34 - 02:34]

large amounts of human demonstrations.

### [02:34 - 02:35]

large amounts of human demonstrations. So there is this is from collaborators

### [02:35 - 02:35]

So there is this is from collaborators

### [02:35 - 02:37]

So there is this is from collaborators at Toyota Research Institute. They're

### [02:37 - 02:37]

at Toyota Research Institute. They're

### [02:37 - 02:39]

at Toyota Research Institute. They're collecting uh human demonstrations of

### [02:39 - 02:39]

collecting uh human demonstrations of

### [02:39 - 02:40]

collecting uh human demonstrations of interaction with the robot and they're

### [02:40 - 02:40]

interaction with the robot and they're

### [02:40 - 02:42]

interaction with the robot and they're and the aim is just to train the robot

### [02:42 - 02:42]

and the aim is just to train the robot

### [02:42 - 02:43]

and the aim is just to train the robot to predict the next action the

### [02:43 - 02:43]

to predict the next action the

### [02:43 - 02:45]

to predict the next action the demonstrator would give. again using

### [02:45 - 02:45]

demonstrator would give. again using

### [02:45 - 02:47]

demonstrator would give. again using observations like pixels or tactile

### [02:47 - 02:47]

observations like pixels or tactile

### [02:47 - 02:48]

observations like pixels or tactile sensing as a form of a conditioning

### [02:48 - 02:48]

sensing as a form of a conditioning

### [02:48 - 02:50]

sensing as a form of a conditioning variable right so similar

### [02:50 - 02:50]

variable right so similar

### [02:50 - 02:53]

variable right so similar paradigm so I think a couple questions

### [02:53 - 02:53]

paradigm so I think a couple questions

### [02:53 - 02:54]

paradigm so I think a couple questions we can ask is you know looking at the

### [02:54 - 02:54]

we can ask is you know looking at the

### [02:54 - 02:56]

we can ask is you know looking at the language model of regime will scaling

### [02:56 - 02:56]

language model of regime will scaling

### [02:56 - 02:58]

language model of regime will scaling solve the problems of robotic foundation

### [02:58 - 02:58]

solve the problems of robotic foundation

### [02:58 - 03:00]

solve the problems of robotic foundation models uh what is the importance of on

### [03:00 - 03:00]

models uh what is the importance of on

### [03:00 - 03:02]

models uh what is the importance of on policy data uh we need for robot models

### [03:02 - 03:02]

policy data uh we need for robot models

### [03:02 - 03:04]

policy data uh we need for robot models or can all this done purely from offline

### [03:04 - 03:04]

or can all this done purely from offline

### [03:04 - 03:07]

or can all this done purely from offline demonstration and maybe how should we

### [03:07 - 03:07]

demonstration and maybe how should we

### [03:07 - 03:08]

demonstration and maybe how should we design the forms of the robot policies

### [03:08 - 03:08]

design the forms of the robot policies

### [03:08 - 03:10]

design the forms of the robot policies that we need in order to scale up these

### [03:10 - 03:10]

that we need in order to scale up these

### [03:10 - 03:11]

that we need in order to scale up these systems right these are some questions

### [03:11 - 03:11]

systems right these are some questions

### [03:11 - 03:13]

systems right these are some questions that we should keep at the back of our

### [03:13 - 03:13]

that we should keep at the back of our

### [03:13 - 03:14]

that we should keep at the back of our heads

### [03:14 - 03:14]

heads

### [03:14 - 03:16]

heads And so when I think about these

### [03:16 - 03:16]

And so when I think about these

### [03:16 - 03:17]

And so when I think about these problems, I see a lot of formal

### [03:17 - 03:17]

problems, I see a lot of formal

### [03:17 - 03:19]

problems, I see a lot of formal similarities, right? In language, my

### [03:19 - 03:19]

similarities, right? In language, my

### [03:19 - 03:20]

similarities, right? In language, my goal is to predict tokens, whereas in

### [03:20 - 03:20]

goal is to predict tokens, whereas in

### [03:20 - 03:23]

goal is to predict tokens, whereas in robotics, my goal is to predict actions,

### [03:23 - 03:23]

robotics, my goal is to predict actions,

### [03:23 - 03:24]

robotics, my goal is to predict actions, but maybe in language, they're discreet,

### [03:24 - 03:24]

but maybe in language, they're discreet,

### [03:24 - 03:27]

but maybe in language, they're discreet, and in robotics, they're continuous. And

### [03:27 - 03:27]

and in robotics, they're continuous. And

### [03:27 - 03:28]

and in robotics, they're continuous. And I guess a major question is, are these

### [03:28 - 03:28]

I guess a major question is, are these

### [03:28 - 03:30]

I guess a major question is, are these things meaningfully different or are

### [03:30 - 03:30]

things meaningfully different or are

### [03:30 - 03:32]

things meaningfully different or are they just somewhat superficial in their

### [03:32 - 03:32]

they just somewhat superficial in their

### [03:32 - 03:34]

they just somewhat superficial in their differences? Right? So is there a

### [03:34 - 03:34]

differences? Right? So is there a

### [03:34 - 03:37]

differences? Right? So is there a fundamental difference here? So maybe we

### [03:37 - 03:37]

fundamental difference here? So maybe we

### [03:37 - 03:39]

fundamental difference here? So maybe we can set up, right? So in in if you open

### [03:39 - 03:39]

can set up, right? So in in if you open

### [03:39 - 03:41]

can set up, right? So in in if you open up an RL book or an RL text RL textbook

### [03:41 - 03:41]

up an RL book or an RL text RL textbook

### [03:41 - 03:43]

up an RL book or an RL text RL textbook maybe RL theory paper what you'll see is

### [03:43 - 03:43]

maybe RL theory paper what you'll see is

### [03:43 - 03:44]

maybe RL theory paper what you'll see is the following notation. You'll see

### [03:44 - 03:44]

the following notation. You'll see

### [03:44 - 03:46]

the following notation. You'll see states denoted with the letter S actions

### [03:46 - 03:46]

states denoted with the letter S actions

### [03:46 - 03:48]

states denoted with the letter S actions denoted with the letter A and you'll

### [03:48 - 03:48]

denoted with the letter A and you'll

### [03:48 - 03:49]

denoted with the letter A and you'll denote dynamics as being drawn from some

### [03:49 - 03:49]

denote dynamics as being drawn from some

### [03:49 - 03:51]

denote dynamics as being drawn from some transition probability distribution

### [03:51 - 03:51]

transition probability distribution

### [03:51 - 03:54]

transition probability distribution transition kernel denoted as in the

### [03:54 - 03:54]

transition kernel denoted as in the

### [03:54 - 03:55]

transition kernel denoted as in the slide and maybe a policy is just some

### [03:55 - 03:56]

slide and maybe a policy is just some

### [03:56 - 03:57]

slide and maybe a policy is just some distribution of reactions again denoted

### [03:57 - 03:57]

distribution of reactions again denoted

### [03:57 - 04:00]

distribution of reactions again denoted typically in this way. And in in

### [04:00 - 04:00]

typically in this way. And in in

### [04:00 - 04:02]

typically in this way. And in in robotics or in control kind of we use

### [04:02 - 04:02]

robotics or in control kind of we use

### [04:02 - 04:03]

robotics or in control kind of we use somewhat different notation, right? So

### [04:03 - 04:04]

somewhat different notation, right? So

### [04:04 - 04:06]

somewhat different notation, right? So here we use x for states and actions are

### [04:06 - 04:06]

here we use x for states and actions are

### [04:06 - 04:08]

here we use x for states and actions are u control inputs. Our dynamics rather

### [04:08 - 04:08]

u control inputs. Our dynamics rather

### [04:08 - 04:09]

u control inputs. Our dynamics rather than thinking of them as coming from

### [04:09 - 04:10]

than thinking of them as coming from

### [04:10 - 04:11]

than thinking of them as coming from some arbitrary conditional distribution.

### [04:11 - 04:11]

some arbitrary conditional distribution.

### [04:11 - 04:13]

some arbitrary conditional distribution. We envision having some nominal dynamics

### [04:13 - 04:13]

We envision having some nominal dynamics

### [04:13 - 04:15]

We envision having some nominal dynamics function typically denoted f and maybe

### [04:15 - 04:15]

function typically denoted f and maybe

### [04:15 - 04:17]

function typically denoted f and maybe there's some noise that affects the

### [04:17 - 04:17]

there's some noise that affects the

### [04:17 - 04:19]

there's some noise that affects the dynamic process. And then finally again

### [04:19 - 04:19]

dynamic process. And then finally again

### [04:19 - 04:21]

dynamic process. And then finally again we can draw control inputs from some

### [04:21 - 04:21]

we can draw control inputs from some

### [04:21 - 04:23]

we can draw control inputs from some policy some policy

### [04:23 - 04:23]

policy some policy

### [04:23 - 04:25]

policy some policy distribution. So maybe the semantics

### [04:25 - 04:25]

distribution. So maybe the semantics

### [04:25 - 04:27]

distribution. So maybe the semantics here are somewhat different right? So in

### [04:27 - 04:27]

here are somewhat different right? So in

### [04:27 - 04:29]

here are somewhat different right? So in language models our states oftentimes we

### [04:29 - 04:29]

language models our states oftentimes we

### [04:29 - 04:31]

language models our states oftentimes we think about this as being say sequences

### [04:31 - 04:31]

think about this as being say sequences

### [04:31 - 04:33]

think about this as being say sequences of tokens maybe words right and our next

### [04:33 - 04:33]

of tokens maybe words right and our next

### [04:33 - 04:35]

of tokens maybe words right and our next action is the next word whereas sort of

### [04:35 - 04:35]

action is the next word whereas sort of

### [04:35 - 04:37]

action is the next word whereas sort of in robotics sort of uh we think more of

### [04:37 - 04:37]

in robotics sort of uh we think more of

### [04:37 - 04:39]

in robotics sort of uh we think more of x as as being either observations or

### [04:39 - 04:39]

x as as being either observations or

### [04:39 - 04:41]

x as as being either observations or system state used being a robot action

### [04:41 - 04:41]

system state used being a robot action

### [04:41 - 04:43]

system state used being a robot action but notably these are continuous value

### [04:43 - 04:43]

but notably these are continuous value

### [04:43 - 04:45]

but notably these are continuous value right so a lot of formal similarities

### [04:45 - 04:45]

right so a lot of formal similarities

### [04:45 - 04:48]

right so a lot of formal similarities but maybe slightly different semat

### [04:48 - 04:48]

but maybe slightly different semat

### [04:48 - 04:50]

but maybe slightly different semat semantics so in both problems we want to

### [04:50 - 04:50]

semantics so in both problems we want to

### [04:50 - 04:52]

semantics so in both problems we want to say imitate an expert so what's a

### [04:52 - 04:52]

say imitate an expert so what's a

### [04:52 - 04:54]

say imitate an expert so what's a reasonable way to talk about imitation

### [04:54 - 04:54]

reasonable way to talk about imitation

### [04:54 - 04:55]

reasonable way to talk about imitation what we can do is we can look at some

### [04:55 - 04:55]

what we can do is we can look at some

### [04:55 - 04:58]

what we can do is we can look at some notion of excess cost. So we can fix

### [04:58 - 04:58]

notion of excess cost. So we can fix

### [04:58 - 05:00]

notion of excess cost. So we can fix some notion of cost. We'll call it C.

### [05:00 - 05:00]

some notion of cost. We'll call it C.

### [05:00 - 05:02]

some notion of cost. We'll call it C. And our notion of error will be looking

### [05:02 - 05:02]

And our notion of error will be looking

### [05:02 - 05:04]

And our notion of error will be looking at the cost under the imitator policy

### [05:04 - 05:04]

at the cost under the imitator policy

### [05:04 - 05:06]

at the cost under the imitator policy which we call pi hat. This is what we

### [05:06 - 05:06]

which we call pi hat. This is what we

### [05:06 - 05:08]

which we call pi hat. This is what we learn with data. And we compare this to

### [05:08 - 05:08]

learn with data. And we compare this to

### [05:08 - 05:10]

learn with data. And we compare this to the cost under the expert, right? And so

### [05:10 - 05:10]

the cost under the expert, right? And so

### [05:10 - 05:11]

the cost under the expert, right? And so our notion of excess cost, you could

### [05:11 - 05:11]

our notion of excess cost, you could

### [05:11 - 05:13]

our notion of excess cost, you could call this regret. Basically determines

### [05:13 - 05:13]

call this regret. Basically determines

### [05:13 - 05:15]

call this regret. Basically determines how well we're doing imitation, right?

### [05:15 - 05:15]

how well we're doing imitation, right?

### [05:15 - 05:17]

how well we're doing imitation, right? And typically in this problem, we're

### [05:17 - 05:17]

And typically in this problem, we're

### [05:17 - 05:18]

And typically in this problem, we're going to focus on problems over a

### [05:18 - 05:18]

going to focus on problems over a

### [05:18 - 05:20]

going to focus on problems over a certain horizon, certain number of of

### [05:20 - 05:20]

certain horizon, certain number of of

### [05:20 - 05:22]

certain horizon, certain number of of steps, which we'll denote by H. And

### [05:22 - 05:22]

steps, which we'll denote by H. And

### [05:22 - 05:23]

steps, which we'll denote by H. And horizon will become kind of a key factor

### [05:23 - 05:23]

horizon will become kind of a key factor

### [05:23 - 05:26]

horizon will become kind of a key factor in our discussion.

### [05:26 - 05:26]

in our discussion.

### [05:26 - 05:27]

in our discussion. Right? So there are a lot of ways that

### [05:27 - 05:28]

Right? So there are a lot of ways that

### [05:28 - 05:29]

Right? So there are a lot of ways that you can kind of try to minimize this

### [05:29 - 05:29]

you can kind of try to minimize this

### [05:29 - 05:32]

you can kind of try to minimize this imitation error. So one possible way to

### [05:32 - 05:32]

imitation error. So one possible way to

### [05:32 - 05:33]

imitation error. So one possible way to do this, not the only way is through

### [05:33 - 05:33]

do this, not the only way is through

### [05:33 - 05:34]

do this, not the only way is through imitate is through what's called

### [05:34 - 05:34]

imitate is through what's called

### [05:34 - 05:36]

imitate is through what's called behavior cloning. So in behavior

### [05:36 - 05:36]

behavior cloning. So in behavior

### [05:36 - 05:38]

behavior cloning. So in behavior cloning, what you do is you specify some

### [05:38 - 05:38]

cloning, what you do is you specify some

### [05:38 - 05:40]

cloning, what you do is you specify some loss function which and here I'm going

### [05:40 - 05:40]

loss function which and here I'm going

### [05:40 - 05:42]

loss function which and here I'm going to be using the control notation X and U

### [05:42 - 05:42]

to be using the control notation X and U

### [05:42 - 05:44]

to be using the control notation X and U which basically measures how well your

### [05:44 - 05:44]

which basically measures how well your

### [05:44 - 05:46]

which basically measures how well your policy is doing relative to pairs of

### [05:46 - 05:46]

policy is doing relative to pairs of

### [05:46 - 05:48]

policy is doing relative to pairs of states and actions in your expert uh

### [05:48 - 05:48]

states and actions in your expert uh

### [05:48 - 05:50]

states and actions in your expert uh from from the expert data. Right? And

### [05:50 - 05:50]

from from the expert data. Right? And

### [05:50 - 05:51]

from from the expert data. Right? And there are many loss functions that you

### [05:51 - 05:52]

there are many loss functions that you

### [05:52 - 05:53]

there are many loss functions that you can minimize. And basically you just

### [05:53 - 05:53]

can minimize. And basically you just

### [05:53 - 05:55]

can minimize. And basically you just train pi hat to fit the expert data by

### [05:55 - 05:55]

train pi hat to fit the expert data by

### [05:55 - 05:57]

train pi hat to fit the expert data by minimizing this loss at least to the

### [05:57 - 05:57]

minimizing this loss at least to the

### [05:57 - 05:59]

minimizing this loss at least to the best of your optimizer's

### [05:59 - 05:59]

best of your optimizer's

### [05:59 - 06:01]

best of your optimizer's ability. So you might do this by

### [06:01 - 06:01]

ability. So you might do this by

### [06:01 - 06:03]

ability. So you might do this by minimizing a square loss if you'd like.

### [06:03 - 06:03]

minimizing a square loss if you'd like.

### [06:03 - 06:05]

minimizing a square loss if you'd like. Uh this typically works if pi star is

### [06:05 - 06:05]

Uh this typically works if pi star is

### [06:05 - 06:07]

Uh this typically works if pi star is deterministic. You might do this by

### [06:07 - 06:07]

deterministic. You might do this by

### [06:07 - 06:09]

deterministic. You might do this by minimizing an indicator loss. This

### [06:09 - 06:09]

minimizing an indicator loss. This

### [06:09 - 06:10]

minimizing an indicator loss. This probably makes more sense if pi lo pi is

### [06:10 - 06:10]

probably makes more sense if pi lo pi is

### [06:10 - 06:12]

probably makes more sense if pi lo pi is discreet. Uh you can use the log loss.

### [06:12 - 06:12]

discreet. Uh you can use the log loss.

### [06:12 - 06:14]

discreet. Uh you can use the log loss. So Dylan's got some awesome work about

### [06:14 - 06:14]

So Dylan's got some awesome work about

### [06:14 - 06:15]

So Dylan's got some awesome work about why that might be beneficial to work

### [06:15 - 06:15]

why that might be beneficial to work

### [06:15 - 06:17]

why that might be beneficial to work with. Also works if pi has some

### [06:17 - 06:17]

with. Also works if pi has some

### [06:17 - 06:19]

with. Also works if pi has some continuous density. uh or you could even

### [06:19 - 06:19]

continuous density. uh or you could even

### [06:19 - 06:21]

continuous density. uh or you could even use things based on score matching which

### [06:21 - 06:21]

use things based on score matching which

### [06:21 - 06:22]

use things based on score matching which have become quite popular in in sort of

### [06:22 - 06:22]

have become quite popular in in sort of

### [06:22 - 06:25]

have become quite popular in in sort of diffusion polic parameterized policies

### [06:25 - 06:25]

diffusion polic parameterized policies

### [06:25 - 06:27]

diffusion polic parameterized policies right that also works quite well and

### [06:27 - 06:27]

right that also works quite well and

### [06:27 - 06:29]

right that also works quite well and it's very popular in robotics but sort

### [06:29 - 06:30]

it's very popular in robotics but sort

### [06:30 - 06:33]

it's very popular in robotics but sort of kind of importantly is even if you're

### [06:33 - 06:33]

of kind of importantly is even if you're

### [06:33 - 06:35]

of kind of importantly is even if you're not going to do uh sort of minim

### [06:35 - 06:35]

not going to do uh sort of minim

### [06:35 - 06:37]

not going to do uh sort of minim explicit minimization of the lit loss I

### [06:37 - 06:37]

explicit minimization of the lit loss I

### [06:37 - 06:39]

explicit minimization of the lit loss I think it is very natural to compare to

### [06:39 - 06:39]

think it is very natural to compare to

### [06:39 - 06:41]

think it is very natural to compare to the the sort of best you could hope for

### [06:41 - 06:41]

the the sort of best you could hope for

### [06:41 - 06:43]

the the sort of best you could hope for under minimizing this loss as a

### [06:43 - 06:43]

under minimizing this loss as a

### [06:43 - 06:44]

under minimizing this loss as a benchmark of how difficult the problem

### [06:44 - 06:44]

benchmark of how difficult the problem

### [06:44 - 06:46]

benchmark of how difficult the problem is at least statistically right so what

### [06:46 - 06:46]

is at least statistically right so what

### [06:46 - 06:47]

is at least statistically right so what we'll do in today's talk is we'll

### [06:47 - 06:47]

we'll do in today's talk is we'll

### [06:47 - 06:49]

we'll do in today's talk is we'll compare our notion of imitation error to

### [06:49 - 06:50]

compare our notion of imitation error to

### [06:50 - 06:52]

compare our notion of imitation error to basically what we would expect to get if

### [06:52 - 06:52]

basically what we would expect to get if

### [06:52 - 06:54]

basically what we would expect to get if we were just looking at how big the loss

### [06:54 - 06:54]

we were just looking at how big the loss

### [06:54 - 06:56]

we were just looking at how big the loss was but in uh but in but crucially under

### [06:56 - 06:56]

was but in uh but in but crucially under

### [06:56 - 06:58]

was but in uh but in but crucially under the distribution of expert data. So we

### [06:58 - 06:58]

the distribution of expert data. So we

### [06:58 - 06:59]

the distribution of expert data. So we look at the distribution of expert data

### [06:59 - 06:59]

look at the distribution of expert data

### [06:59 - 07:01]

look at the distribution of expert data this is this expectation and we measure

### [07:01 - 07:01]

this is this expectation and we measure

### [07:01 - 07:03]

this is this expectation and we measure how large the losses and roughly

### [07:03 - 07:03]

how large the losses and roughly

### [07:03 - 07:04]

how large the losses and roughly speaking we'll try to understand this as

### [07:04 - 07:04]

speaking we'll try to understand this as

### [07:04 - 07:06]

speaking we'll try to understand this as a proxy for how easy the problem is

### [07:06 - 07:06]

a proxy for how easy the problem is

### [07:06 - 07:08]

a proxy for how easy the problem is statistically without dealing with

### [07:08 - 07:08]

statistically without dealing with

### [07:08 - 07:10]

statistically without dealing with issues related to the dynamics of the

### [07:10 - 07:10]

issues related to the dynamics of the

### [07:10 - 07:11]

issues related to the dynamics of the system just how easy it is to fit the

### [07:11 - 07:11]

system just how easy it is to fit the

### [07:11 - 07:13]

system just how easy it is to fit the expert data even if we consider

### [07:13 - 07:13]

expert data even if we consider

### [07:13 - 07:15]

expert data even if we consider algorithms that don't necessarily do

### [07:15 - 07:15]

algorithms that don't necessarily do

### [07:15 - 07:18]

algorithms that don't necessarily do this minimization algorithmically.

### [07:18 - 07:18]

this minimization algorithmically.

### [07:18 - 07:20]

this minimization algorithmically. Okay. So why is behavior cloning hard?

### [07:20 - 07:20]

Okay. So why is behavior cloning hard?

### [07:20 - 07:22]

Okay. So why is behavior cloning hard? Well, it it relates to this phenomena

### [07:22 - 07:22]

Well, it it relates to this phenomena

### [07:22 - 07:24]

Well, it it relates to this phenomena called compounding error, right? So our

### [07:24 - 07:24]

called compounding error, right? So our

### [07:24 - 07:26]

called compounding error, right? So our our notion of expert imitation accuracy,

### [07:26 - 07:26]

our notion of expert imitation accuracy,

### [07:26 - 07:28]

our notion of expert imitation accuracy, right? How close we'd be on to fitting a

### [07:28 - 07:28]

right? How close we'd be on to fitting a

### [07:28 - 07:29]

right? How close we'd be on to fitting a supervised learning objective on the

### [07:29 - 07:29]

supervised learning objective on the

### [07:29 - 07:32]

supervised learning objective on the expert data. Uh you know, you can really

### [07:32 - 07:32]

expert data. Uh you know, you can really

### [07:32 - 07:33]

expert data. Uh you know, you can really think about this as basically taking

### [07:33 - 07:33]

think about this as basically taking

### [07:33 - 07:35]

think about this as basically taking samples from an expert trajectory and

### [07:35 - 07:35]

samples from an expert trajectory and

### [07:35 - 07:36]

samples from an expert trajectory and making sure that you're able to make

### [07:36 - 07:36]

making sure that you're able to make

### [07:36 - 07:38]

making sure that you're able to make predictions which at each individual

### [07:38 - 07:38]

predictions which at each individual

### [07:38 - 07:40]

predictions which at each individual time step are close to what the expert

### [07:40 - 07:40]

time step are close to what the expert

### [07:40 - 07:41]

time step are close to what the expert would do. Right? So this is what it

### [07:41 - 07:41]

would do. Right? So this is what it

### [07:41 - 07:43]

would do. Right? So this is what it would look like to have a small notion

### [07:43 - 07:43]

would look like to have a small notion

### [07:43 - 07:46]

would look like to have a small notion of our expert. But unfortunately what we

### [07:46 - 07:46]

of our expert. But unfortunately what we

### [07:46 - 07:48]

of our expert. But unfortunately what we really care about is not our expert.

### [07:48 - 07:48]

really care about is not our expert.

### [07:48 - 07:49]

really care about is not our expert. What we care about is sort of the

### [07:49 - 07:49]

What we care about is sort of the

### [07:49 - 07:50]

What we care about is sort of the deployment behavior of the e of the

### [07:50 - 07:50]

deployment behavior of the e of the

### [07:50 - 07:53]

deployment behavior of the e of the learn policy and what cost that attains.

### [07:53 - 07:53]

learn policy and what cost that attains.

### [07:53 - 07:55]

learn policy and what cost that attains. So expectation under the learn policy pi

### [07:55 - 07:55]

So expectation under the learn policy pi

### [07:55 - 07:57]

So expectation under the learn policy pi hat. And when you actually deploy the

### [07:57 - 07:57]

hat. And when you actually deploy the

### [07:57 - 07:59]

hat. And when you actually deploy the learn policy what you start to see is

### [07:59 - 07:59]

learn policy what you start to see is

### [07:59 - 08:00]

learn policy what you start to see is that the errors that it makes can

### [08:00 - 08:00]

that the errors that it makes can

### [08:00 - 08:03]

that the errors that it makes can possibly add up. In fact errors can

### [08:03 - 08:03]

possibly add up. In fact errors can

### [08:03 - 08:04]

possibly add up. In fact errors can accumulate over time steps and they can

### [08:04 - 08:04]

accumulate over time steps and they can

### [08:04 - 08:06]

accumulate over time steps and they can in fact accumulate more and more largely

### [08:06 - 08:06]

in fact accumulate more and more largely

### [08:06 - 08:09]

in fact accumulate more and more largely as the the horizon grows.

### [08:09 - 08:09]

as the the horizon grows.

### [08:09 - 08:10]

as the the horizon grows. uh moreover after the error has

### [08:10 - 08:10]

uh moreover after the error has

### [08:10 - 08:12]

uh moreover after the error has accumulated you can also run into the

### [08:12 - 08:12]

accumulated you can also run into the

### [08:12 - 08:13]

accumulated you can also run into the fact that the fact that you might be out

### [08:13 - 08:13]

fact that the fact that you might be out

### [08:13 - 08:15]

fact that the fact that you might be out of the distribution of your expert data.

### [08:15 - 08:15]

of the distribution of your expert data.

### [08:15 - 08:17]

of the distribution of your expert data. So you might sort of end up somewhere

### [08:17 - 08:17]

So you might sort of end up somewhere

### [08:17 - 08:18]

So you might sort of end up somewhere over here where you don't have a lot of

### [08:18 - 08:18]

over here where you don't have a lot of

### [08:18 - 08:19]

over here where you don't have a lot of supervision and you don't quite know

### [08:19 - 08:19]

supervision and you don't quite know

### [08:19 - 08:21]

supervision and you don't quite know what action to take next. Right? So this

### [08:21 - 08:21]

what action to take next. Right? So this

### [08:21 - 08:24]

what action to take next. Right? So this is an issue that you can run into. So

### [08:24 - 08:24]

is an issue that you can run into. So

### [08:24 - 08:26]

is an issue that you can run into. So what do we know? Well, it's very popular

### [08:26 - 08:26]

what do we know? Well, it's very popular

### [08:26 - 08:28]

what do we know? Well, it's very popular actually even kind of going back to kind

### [08:28 - 08:28]

actually even kind of going back to kind

### [08:28 - 08:30]

actually even kind of going back to kind of early work on imitation to compare

### [08:30 - 08:30]

of early work on imitation to compare

### [08:30 - 08:33]

of early work on imitation to compare sort of imitation and uh uh imitation in

### [08:33 - 08:33]

sort of imitation and uh uh imitation in

### [08:33 - 08:35]

sort of imitation and uh uh imitation in this sense to imitation this expert

### [08:35 - 08:35]

this sense to imitation this expert

### [08:35 - 08:36]

this sense to imitation this expert sense. Let me cancel the software

### [08:36 - 08:36]

sense. Let me cancel the software

### [08:36 - 08:40]

sense. Let me cancel the software update. Um and so for example, if we are

### [08:40 - 08:40]

update. Um and so for example, if we are

### [08:40 - 08:42]

update. Um and so for example, if we are in a setting where we can minimize the

### [08:42 - 08:42]

in a setting where we can minimize the

### [08:42 - 08:45]

in a setting where we can minimize the 01 loss and we consider costs that are

### [08:45 - 08:45]

01 loss and we consider costs that are

### [08:45 - 08:48]

01 loss and we consider costs that are bounded in 01, then roughly speaking, we

### [08:48 - 08:48]

bounded in 01, then roughly speaking, we

### [08:48 - 08:50]

bounded in 01, then roughly speaking, we can bound our notion of imitation under

### [08:50 - 08:50]

can bound our notion of imitation under

### [08:50 - 08:52]

can bound our notion of imitation under a certain cost that should have an R

### [08:52 - 08:52]

a certain cost that should have an R

### [08:52 - 08:55]

a certain cost that should have an R subc by roughly h times uh the expert

### [08:55 - 08:55]

subc by roughly h times uh the expert

### [08:55 - 08:57]

subc by roughly h times uh the expert error, right? Horizon factor times the

### [08:57 - 08:57]

error, right? Horizon factor times the

### [08:57 - 08:59]

error, right? Horizon factor times the error of the imitation and the 01 loss.

### [08:59 - 09:00]

error of the imitation and the 01 loss.

### [09:00 - 09:01]

error of the imitation and the 01 loss. And there's some really wonderful

### [09:01 - 09:01]

And there's some really wonderful

### [09:01 - 09:02]

And there's some really wonderful improvements that can be made if you are

### [09:02 - 09:02]

improvements that can be made if you are

### [09:02 - 09:04]

improvements that can be made if you are able to consider other loss functions

### [09:04 - 09:04]

able to consider other loss functions

### [09:04 - 09:05]

able to consider other loss functions under certain kind of assumptions on

### [09:05 - 09:05]

under certain kind of assumptions on

### [09:05 - 09:07]

under certain kind of assumptions on your function class.

### [09:07 - 09:07]

your function class.

### [09:07 - 09:09]

your function class. Right? Uh and so what this basically

### [09:09 - 09:09]

Right? Uh and so what this basically

### [09:09 - 09:11]

Right? Uh and so what this basically tells you is you know compounding error

### [09:11 - 09:11]

tells you is you know compounding error

### [09:11 - 09:13]

tells you is you know compounding error is maybe linearish in the horizon

### [09:13 - 09:13]

is maybe linearish in the horizon

### [09:13 - 09:14]

is maybe linearish in the horizon depending on how you parameterize

### [09:14 - 09:14]

depending on how you parameterize

### [09:14 - 09:16]

depending on how you parameterize things. Maybe it's it's a little bit

### [09:16 - 09:16]

things. Maybe it's it's a little bit

### [09:16 - 09:18]

things. Maybe it's it's a little bit better than that but it would seem like

### [09:18 - 09:18]

better than that but it would seem like

### [09:18 - 09:19]

better than that but it would seem like compounding error the the horizon

### [09:19 - 09:20]

compounding error the the horizon

### [09:20 - 09:22]

compounding error the the horizon dependence of your problem is not such a

### [09:22 - 09:22]

dependence of your problem is not such a

### [09:22 - 09:24]

dependence of your problem is not such a significant

### [09:24 - 09:24]

significant

### [09:24 - 09:26]

significant obstacle. So actually I'm going to say

### [09:26 - 09:26]

obstacle. So actually I'm going to say

### [09:26 - 09:27]

obstacle. So actually I'm going to say that maybe this perspective is not the

### [09:27 - 09:27]

that maybe this perspective is not the

### [09:27 - 09:29]

that maybe this perspective is not the one that we should take in the in the

### [09:29 - 09:29]

one that we should take in the in the

### [09:29 - 09:31]

one that we should take in the in the continuous world and I'll justify why.

### [09:31 - 09:31]

continuous world and I'll justify why.

### [09:31 - 09:34]

continuous world and I'll justify why. Right? So many forms of imitation

### [09:34 - 09:34]

Right? So many forms of imitation

### [09:34 - 09:35]

Right? So many forms of imitation including ones that have been

### [09:35 - 09:35]

including ones that have been

### [09:35 - 09:36]

including ones that have been popularized recently in LMS like log

### [09:36 - 09:36]

popularized recently in LMS like log

### [09:36 - 09:39]

popularized recently in LMS like log loss really they sort of imply

### [09:39 - 09:39]

loss really they sort of imply

### [09:39 - 09:41]

loss really they sort of imply guarantees that would imply imitation in

### [09:41 - 09:41]

guarantees that would imply imitation in

### [09:41 - 09:43]

guarantees that would imply imitation in 01 loss. So for example with Pinsker's

### [09:43 - 09:43]

01 loss. So for example with Pinsker's

### [09:43 - 09:44]

01 loss. So for example with Pinsker's inequality you can sort of control total

### [09:44 - 09:44]

inequality you can sort of control total

### [09:44 - 09:46]

inequality you can sort of control total variation distance by log loss. If that

### [09:46 - 09:46]

variation distance by log loss. If that

### [09:46 - 09:47]

variation distance by log loss. If that doesn't make sense to you don't worry

### [09:47 - 09:47]

doesn't make sense to you don't worry

### [09:47 - 09:48]

doesn't make sense to you don't worry about it. If you're an expert you

### [09:48 - 09:48]

about it. If you're an expert you

### [09:48 - 09:49]

about it. If you're an expert you understand what I'm saying. So

### [09:49 - 09:49]

understand what I'm saying. So

### [09:49 - 09:51]

understand what I'm saying. So essentially what what what basically

### [09:51 - 09:51]

essentially what what what basically

### [09:51 - 09:53]

essentially what what what basically needs to happen is you need to be able

### [09:53 - 09:53]

needs to happen is you need to be able

### [09:53 - 09:55]

needs to happen is you need to be able to imitate in 01 for any of these kind

### [09:55 - 09:55]

to imitate in 01 for any of these kind

### [09:55 - 09:57]

to imitate in 01 for any of these kind of interesting sublinear or sublinear

### [09:57 - 09:57]

of interesting sublinear or sublinear

### [09:57 - 10:00]

of interesting sublinear or sublinear guarantees to make sense. Okay. So

### [10:00 - 10:00]

guarantees to make sense. Okay. So

### [10:00 - 10:01]

guarantees to make sense. Okay. So consider just a scalar prediction

### [10:01 - 10:01]

consider just a scalar prediction

### [10:01 - 10:03]

consider just a scalar prediction problem, right? So I I just sample some

### [10:03 - 10:04]

problem, right? So I I just sample some

### [10:04 - 10:06]

problem, right? So I I just sample some context vector uniformly from 01 and I

### [10:06 - 10:06]

context vector uniformly from 01 and I

### [10:06 - 10:08]

context vector uniformly from 01 and I try to learn some function of that

### [10:08 - 10:08]

try to learn some function of that

### [10:08 - 10:09]

try to learn some function of that scalar and suppose I just try to

### [10:09 - 10:09]

scalar and suppose I just try to

### [10:09 - 10:11]

scalar and suppose I just try to minimize the 01 loss for just scalar

### [10:11 - 10:11]

minimize the 01 loss for just scalar

### [10:11 - 10:13]

minimize the 01 loss for just scalar prediction, right? So here you know

### [10:13 - 10:13]

prediction, right? So here you know

### [10:13 - 10:15]

prediction, right? So here you know these things might be continuous value.

### [10:15 - 10:15]

these things might be continuous value.

### [10:15 - 10:17]

these things might be continuous value. This is possible. Uh for those of you

### [10:17 - 10:17]

This is possible. Uh for those of you

### [10:17 - 10:18]

This is possible. Uh for those of you that know some basic statistical

### [10:18 - 10:18]

that know some basic statistical

### [10:18 - 10:20]

that know some basic statistical learning theory, you'll say of course it

### [10:20 - 10:20]

learning theory, you'll say of course it

### [10:20 - 10:21]

learning theory, you'll say of course it shouldn't be possible in general. In

### [10:21 - 10:21]

shouldn't be possible in general. In

### [10:21 - 10:23]

shouldn't be possible in general. In fact, you can make this formal, right?

### [10:23 - 10:23]

fact, you can make this formal, right?

### [10:23 - 10:24]

fact, you can make this formal, right? Right? So you can show that there are

### [10:24 - 10:24]

Right? So you can show that there are

### [10:24 - 10:26]

Right? So you can show that there are classes of sort of just singlestep

### [10:26 - 10:26]

classes of sort of just singlestep

### [10:26 - 10:29]

classes of sort of just singlestep functions where given n examples sort of

### [10:29 - 10:29]

functions where given n examples sort of

### [10:29 - 10:31]

functions where given n examples sort of you can't get anything better in the 01

### [10:31 - 10:31]

you can't get anything better in the 01

### [10:31 - 10:32]

you can't get anything better in the 01 loss than not in the trivial error. So

### [10:32 - 10:32]

loss than not in the trivial error. So

### [10:32 - 10:34]

loss than not in the trivial error. So the worst possible error in the 01 loss

### [10:34 - 10:34]

the worst possible error in the 01 loss

### [10:34 - 10:37]

the worst possible error in the 01 loss is an expected error of one. But at the

### [10:37 - 10:37]

is an expected error of one. But at the

### [10:37 - 10:38]

is an expected error of one. But at the same time you can actually learn let's

### [10:38 - 10:38]

same time you can actually learn let's

### [10:38 - 10:41]

same time you can actually learn let's say in the L2 loss with vanishingly

### [10:41 - 10:41]

say in the L2 loss with vanishingly

### [10:41 - 10:42]

say in the L2 loss with vanishingly small error. So you can make the error

### [10:42 - 10:42]

small error. So you can make the error

### [10:42 - 10:43]

small error. So you can make the error go down as a function of number of

### [10:43 - 10:44]

go down as a function of number of

### [10:44 - 10:45]

go down as a function of number of samples n as fast as you'd like and yet

### [10:45 - 10:45]

samples n as fast as you'd like and yet

### [10:45 - 10:47]

samples n as fast as you'd like and yet you still can cannot learn in the 01

### [10:47 - 10:47]

you still can cannot learn in the 01

### [10:47 - 10:49]

you still can cannot learn in the 01 loss. Right? And this is kind of easy to

### [10:49 - 10:49]

loss. Right? And this is kind of easy to

### [10:49 - 10:51]

loss. Right? And this is kind of easy to see. One way to construct this example

### [10:51 - 10:51]

see. One way to construct this example

### [10:51 - 10:53]

see. One way to construct this example is to build a foraier series and show

### [10:53 - 10:53]

is to build a foraier series and show

### [10:53 - 10:55]

is to build a foraier series and show that estimating in the 01 loss allows

### [10:55 - 10:55]

that estimating in the 01 loss allows

### [10:55 - 10:58]

that estimating in the 01 loss allows you to uh perfectly recover every forier

### [10:58 - 10:58]

you to uh perfectly recover every forier

### [10:58 - 11:00]

you to uh perfectly recover every forier coefficient. But sort of L2 estimation

### [11:00 - 11:00]

coefficient. But sort of L2 estimation

### [11:00 - 11:01]

coefficient. But sort of L2 estimation just needs needs you to sort of

### [11:01 - 11:01]

just needs needs you to sort of

### [11:01 - 11:03]

just needs needs you to sort of approximately recover the first few and

### [11:03 - 11:03]

approximately recover the first few and

### [11:03 - 11:05]

approximately recover the first few and this is this is feasible from some

### [11:05 - 11:05]

this is this is feasible from some

### [11:05 - 11:06]

this is this is feasible from some amount of data and you can actually make

### [11:06 - 11:06]

amount of data and you can actually make

### [11:06 - 11:08]

amount of data and you can actually make the the rate of estimation improve as

### [11:08 - 11:08]

the the rate of estimation improve as

### [11:08 - 11:09]

the the rate of estimation improve as you make the decay of the coefficients

### [11:09 - 11:09]

you make the decay of the coefficients

### [11:09 - 11:11]

you make the decay of the coefficients go faster. Wait, Max, I'm a bit

### [11:11 - 11:12]

go faster. Wait, Max, I'm a bit

### [11:12 - 11:14]

go faster. Wait, Max, I'm a bit confused. So here the class pi is not

### [11:14 - 11:14]

confused. So here the class pi is not

### [11:14 - 11:15]

confused. So here the class pi is not known to the learner. Oh, it is known to

### [11:15 - 11:16]

known to the learner. Oh, it is known to

### [11:16 - 11:17]

known to the learner. Oh, it is known to the learner. I sorry I I'll give you

### [11:17 - 11:17]

the learner. I sorry I I'll give you

### [11:17 - 11:18]

the learner. I sorry I I'll give you I'll give you a class pi known to the

### [11:18 - 11:18]

I'll give you a class pi known to the

### [11:18 - 11:20]

I'll give you a class pi known to the learner. So there exists a class pi

### [11:20 - 11:20]

learner. So there exists a class pi

### [11:20 - 11:21]

learner. So there exists a class pi which is known to which I can tell you

### [11:21 - 11:21]

which is known to which I can tell you

### [11:21 - 11:23]

which is known to which I can tell you tell the learner where I can't estimate

### [11:23 - 11:23]

tell the learner where I can't estimate

### [11:23 - 11:25]

tell the learner where I can't estimate in the 01 loss but I can estimate in the

### [11:25 - 11:25]

in the 01 loss but I can estimate in the

### [11:25 - 11:28]

in the 01 loss but I can estimate in the L2 loss and I can adjust that class for

### [11:28 - 11:28]

L2 loss and I can adjust that class for

### [11:28 - 11:30]

L2 loss and I can adjust that class for whatever I'd like to make estimation at

### [11:30 - 11:30]

whatever I'd like to make estimation at

### [11:30 - 11:33]

whatever I'd like to make estimation at L2 loss as fast as possible. I see. But

### [11:33 - 11:33]

L2 loss as fast as possible. I see. But

### [11:33 - 11:34]

L2 loss as fast as possible. I see. But that class is not a singleton. That's a

### [11:34 - 11:34]

that class is not a singleton. That's a

### [11:34 - 11:36]

that class is not a singleton. That's a large class. It's a large class. Yes.

### [11:36 - 11:36]

large class. It's a large class. Yes.

### [11:36 - 11:37]

large class. It's a large class. Yes. Okay. Good. Good. Okay. Yeah. It's not a

### [11:37 - 11:37]

Okay. Good. Good. Okay. Yeah. It's not a

### [11:37 - 11:39]

Okay. Good. Good. Okay. Yeah. It's not a singleton. Sorry. I should that's it

### [11:39 - 11:39]

singleton. Sorry. I should that's it

### [11:39 - 11:40]

singleton. Sorry. I should that's it should be set of pi and pi. That's a

### [11:40 - 11:40]

should be set of pi and pi. That's a

### [11:40 - 11:42]

should be set of pi and pi. That's a good clarification. Thank you. Thanks.

### [11:42 - 11:42]

good clarification. Thank you. Thanks.

### [11:42 - 11:43]

good clarification. Thank you. Thanks. Cool. So basically the key implication

### [11:43 - 11:43]

Cool. So basically the key implication

### [11:43 - 11:45]

Cool. So basically the key implication is that these assumptions under which we

### [11:45 - 11:45]

is that these assumptions under which we

### [11:45 - 11:47]

is that these assumptions under which we get this linearish compounding error

### [11:47 - 11:47]

get this linearish compounding error

### [11:47 - 11:48]

get this linearish compounding error they're not really applicable in in in

### [11:48 - 11:48]

they're not really applicable in in in

### [11:48 - 11:51]

they're not really applicable in in in continuous state space right so all so

### [11:51 - 11:51]

continuous state space right so all so

### [11:51 - 11:52]

continuous state space right so all so so far all I've done is convince you

### [11:52 - 11:52]

so far all I've done is convince you

### [11:52 - 11:54]

so far all I've done is convince you that like thinking about 01 loss might

### [11:54 - 11:54]

that like thinking about 01 loss might

### [11:54 - 11:55]

that like thinking about 01 loss might be the wrong thing for continuous state

### [11:55 - 11:55]

be the wrong thing for continuous state

### [11:55 - 11:57]

be the wrong thing for continuous state spaces I haven't yet shown you that

### [11:57 - 11:57]

spaces I haven't yet shown you that

### [11:57 - 11:59]

spaces I haven't yet shown you that compounding error necessarily might be a

### [11:59 - 11:59]

compounding error necessarily might be a

### [11:59 - 12:01]

compounding error necessarily might be a problem so let me kind of make this a

### [12:01 - 12:01]

problem so let me kind of make this a

### [12:01 - 12:02]

problem so let me kind of make this a little bit more

### [12:02 - 12:02]

little bit more

### [12:02 - 12:05]

little bit more precise so to pro I I really like

### [12:05 - 12:05]

precise so to pro I I really like

### [12:05 - 12:07]

precise so to pro I I really like proving lower bounds and one thing I

### [12:07 - 12:07]

proving lower bounds and one thing I

### [12:07 - 12:08]

proving lower bounds and one thing I think is an important part of the art of

### [12:08 - 12:08]

think is an important part of the art of

### [12:08 - 12:10]

think is an important part of the art of lower bounds is to prove them in

### [12:10 - 12:10]

lower bounds is to prove them in

### [12:10 - 12:11]

lower bounds is to prove them in settings that you might otherwise think

### [12:11 - 12:11]

settings that you might otherwise think

### [12:11 - 12:12]

settings that you might otherwise think are nice or benign

### [12:12 - 12:12]

are nice or benign

### [12:12 - 12:14]

are nice or benign So the lower bound I'm going to prove to

### [12:14 - 12:14]

So the lower bound I'm going to prove to

### [12:14 - 12:15]

So the lower bound I'm going to prove to you today is going to be in what we

### [12:15 - 12:15]

you today is going to be in what we

### [12:15 - 12:17]

you today is going to be in what we might think of one of as one of the

### [12:17 - 12:17]

might think of one of as one of the

### [12:17 - 12:18]

might think of one of as one of the nicest control systems that you could

### [12:18 - 12:18]

nicest control systems that you could

### [12:18 - 12:20]

nicest control systems that you could think about. And let me try to convince

### [12:20 - 12:20]

think about. And let me try to convince

### [12:20 - 12:22]

think about. And let me try to convince you that this is a nice system. So the

### [12:22 - 12:22]

you that this is a nice system. So the

### [12:22 - 12:23]

you that this is a nice system. So the first thing that's going to be nice is

### [12:23 - 12:23]

first thing that's going to be nice is

### [12:23 - 12:25]

first thing that's going to be nice is that the expert in the dynamics are

### [12:25 - 12:25]

that the expert in the dynamics are

### [12:25 - 12:27]

that the expert in the dynamics are deterministic. In particular, there's

### [12:27 - 12:27]

deterministic. In particular, there's

### [12:27 - 12:28]

deterministic. In particular, there's been a lot of work in robot learning

### [12:28 - 12:28]

been a lot of work in robot learning

### [12:28 - 12:30]

been a lot of work in robot learning around learning multimodal policies,

### [12:30 - 12:30]

around learning multimodal policies,

### [12:30 - 12:31]

around learning multimodal policies, policies that are complex distributions.

### [12:31 - 12:32]

policies that are complex distributions.

### [12:32 - 12:33]

policies that are complex distributions. Instead, we're just going to think about

### [12:33 - 12:33]

Instead, we're just going to think about

### [12:33 - 12:34]

Instead, we're just going to think about learning deterministic

### [12:34 - 12:35]

learning deterministic

### [12:35 - 12:36]

learning deterministic experts. The second thing we're going to

### [12:36 - 12:36]

experts. The second thing we're going to

### [12:36 - 12:38]

experts. The second thing we're going to assume is that the dynamics in the

### [12:38 - 12:38]

assume is that the dynamics in the

### [12:38 - 12:39]

assume is that the dynamics in the expert are C infinity. They have

### [12:39 - 12:39]

expert are C infinity. They have

### [12:39 - 12:41]

expert are C infinity. They have infinitely many derivatives and their

### [12:41 - 12:41]

infinitely many derivatives and their

### [12:41 - 12:42]

infinitely many derivatives and their first and second of derivatives are

### [12:42 - 12:42]

first and second of derivatives are

### [12:42 - 12:43]

first and second of derivatives are bounded, right? So they're going to be

### [12:43 - 12:43]

bounded, right? So they're going to be

### [12:43 - 12:45]

bounded, right? So they're going to be lip shifts and smooth, right? Also a

### [12:45 - 12:45]

lip shifts and smooth, right? Also a

### [12:45 - 12:47]

lip shifts and smooth, right? Also a nice property. So there's nothing like

### [12:47 - 12:47]

nice property. So there's nothing like

### [12:47 - 12:48]

nice property. So there's nothing like stiffness or discontinuity of the

### [12:48 - 12:48]

stiffness or discontinuity of the

### [12:48 - 12:50]

stiffness or discontinuity of the dynamics that's going to get in your

### [12:50 - 12:50]

dynamics that's going to get in your

### [12:50 - 12:52]

dynamics that's going to get in your way. And the final property, which I'm

### [12:52 - 12:52]

way. And the final property, which I'm

### [12:52 - 12:53]

way. And the final property, which I'm going to expend spend some time

### [12:53 - 12:53]

going to expend spend some time

### [12:53 - 12:55]

going to expend spend some time explaining in a couple later slides, is

### [12:55 - 12:56]

explaining in a couple later slides, is

### [12:56 - 12:57]

explaining in a couple later slides, is that the dynamics are exponentially

### [12:57 - 12:58]

that the dynamics are exponentially

### [12:58 - 12:59]

that the dynamics are exponentially incrementally input to state stable.

### [12:59 - 12:59]

incrementally input to state stable.

### [12:59 - 13:01]

incrementally input to state stable. This is a mouthful, but roughly what

### [13:01 - 13:02]

This is a mouthful, but roughly what

### [13:02 - 13:03]

This is a mouthful, but roughly what this means is that the dynamics are

### [13:03 - 13:03]

this means is that the dynamics are

### [13:03 - 13:05]

this means is that the dynamics are somewhat insensitive to perturbations.

### [13:05 - 13:05]

somewhat insensitive to perturbations.

### [13:05 - 13:07]

somewhat insensitive to perturbations. So it's not the case that if you make a

### [13:07 - 13:07]

So it's not the case that if you make a

### [13:07 - 13:08]

So it's not the case that if you make a small error suddenly you end up in a

### [13:08 - 13:08]

small error suddenly you end up in a

### [13:08 - 13:10]

small error suddenly you end up in a totally different place. Roughly

### [13:10 - 13:10]

totally different place. Roughly

### [13:10 - 13:12]

totally different place. Roughly speaking small errors shouldn't make a

### [13:12 - 13:12]

speaking small errors shouldn't make a

### [13:12 - 13:13]

speaking small errors shouldn't make a big difference to the dynamics even on

### [13:13 - 13:13]

big difference to the dynamics even on

### [13:13 - 13:16]

big difference to the dynamics even on longer horizons. And we'll talk a little

### [13:16 - 13:16]

longer horizons. And we'll talk a little

### [13:16 - 13:18]

longer horizons. And we'll talk a little bit more about this

### [13:18 - 13:18]

bit more about this

### [13:18 - 13:21]

bit more about this assumption. So we're going to get back

### [13:21 - 13:21]

assumption. So we're going to get back

### [13:21 - 13:22]

assumption. So we're going to get back to that assumption later. I'm going to

### [13:22 - 13:22]

to that assumption later. I'm going to

### [13:22 - 13:24]

to that assumption later. I'm going to explain it in greater detail. Last thing

### [13:24 - 13:24]

explain it in greater detail. Last thing

### [13:24 - 13:25]

explain it in greater detail. Last thing what I'm going to say is that our lower

### [13:25 - 13:25]

what I'm going to say is that our lower

### [13:25 - 13:28]

what I'm going to say is that our lower bound does not apply unconditionally. It

### [13:28 - 13:28]

bound does not apply unconditionally. It

### [13:28 - 13:30]

bound does not apply unconditionally. It applies to basically any algorithm be

### [13:30 - 13:30]

applies to basically any algorithm be

### [13:30 - 13:32]

applies to basically any algorithm be that online uh be that behavior coding

### [13:32 - 13:32]

that online uh be that behavior coding

### [13:32 - 13:35]

that online uh be that behavior coding offline reinforcement in uh learning uh

### [13:35 - 13:35]

offline reinforcement in uh learning uh

### [13:35 - 13:38]

offline reinforcement in uh learning uh inverse RL style approaches but it in in

### [13:38 - 13:38]

inverse RL style approaches but it in in

### [13:38 - 13:40]

inverse RL style approaches but it in in particular constrains the class of

### [13:40 - 13:40]

particular constrains the class of

### [13:40 - 13:42]

particular constrains the class of policies we're allowed to use. So we're

### [13:42 - 13:42]

policies we're allowed to use. So we're

### [13:42 - 13:44]

policies we're allowed to use. So we're going to pro prove a lower bound against

### [13:44 - 13:44]

going to pro prove a lower bound against

### [13:44 - 13:46]

going to pro prove a lower bound against what we call simple imitator policies

### [13:46 - 13:46]

what we call simple imitator policies

### [13:46 - 13:48]

what we call simple imitator policies and then I'll explain to you at the end

### [13:48 - 13:48]

and then I'll explain to you at the end

### [13:48 - 13:50]

and then I'll explain to you at the end of the talk how things generalize beyond

### [13:50 - 13:50]

of the talk how things generalize beyond

### [13:50 - 13:52]

of the talk how things generalize beyond that. So I'm going to define a simple

### [13:52 - 13:52]

that. So I'm going to define a simple

### [13:52 - 13:54]

that. So I'm going to define a simple imitator policy as a policy that has two

### [13:54 - 13:54]

imitator policy as a policy that has two

### [13:54 - 13:56]

imitator policy as a policy that has two components. It has a deterministic

### [13:56 - 13:56]

components. It has a deterministic

### [13:56 - 13:59]

components. It has a deterministic component which like the expert I'll

### [13:59 - 13:59]

component which like the expert I'll

### [13:59 - 14:01]

component which like the expert I'll assume is lip shits and smooth and it

### [14:01 - 14:01]

assume is lip shits and smooth and it

### [14:01 - 14:02]

assume is lip shits and smooth and it also has a stochcastic component which

### [14:02 - 14:02]

also has a stochcastic component which

### [14:02 - 14:04]

also has a stochcastic component which is going to be assumed to be independent

### [14:04 - 14:04]

is going to be assumed to be independent

### [14:04 - 14:07]

is going to be assumed to be independent of X. So we can see that simple policies

### [14:07 - 14:07]

of X. So we can see that simple policies

### [14:07 - 14:08]

of X. So we can see that simple policies are a strict and and pretty strong

### [14:08 - 14:09]

are a strict and and pretty strong

### [14:09 - 14:11]

are a strict and and pretty strong generalization of the kind of class of

### [14:11 - 14:11]

generalization of the kind of class of

### [14:11 - 14:13]

generalization of the kind of class of policies that the expert can be but

### [14:13 - 14:13]

policies that the expert can be but

### [14:13 - 14:14]

policies that the expert can be but nevertheless they don't capture every

### [14:14 - 14:14]

nevertheless they don't capture every

### [14:14 - 14:16]

nevertheless they don't capture every policy. So for example, a common policy

### [14:16 - 14:16]

policy. So for example, a common policy

### [14:16 - 14:18]

policy. So for example, a common policy parameterization in sort of like uh

### [14:18 - 14:18]

parameterization in sort of like uh

### [14:18 - 14:20]

parameterization in sort of like uh simple robot learning tasks might be a

### [14:20 - 14:20]

simple robot learning tasks might be a

### [14:20 - 14:22]

simple robot learning tasks might be a gausian a mean policy where you

### [14:22 - 14:22]

gausian a mean policy where you

### [14:22 - 14:24]

gausian a mean policy where you parameterize the gausian mean but you

### [14:24 - 14:24]

parameterize the gausian mean but you

### [14:24 - 14:25]

parameterize the gausian mean but you don't learn the gausian variance you

### [14:25 - 14:25]

don't learn the gausian variance you

### [14:25 - 14:27]

don't learn the gausian variance you treat that as a fixed parameter or you

### [14:27 - 14:27]

treat that as a fixed parameter or you

### [14:27 - 14:29]

treat that as a fixed parameter or you treat it as a fixed parameter across all

### [14:29 - 14:29]

treat it as a fixed parameter across all

### [14:29 - 14:31]

treat it as a fixed parameter across all states and this would constitute being a

### [14:31 - 14:31]

states and this would constitute being a

### [14:31 - 14:33]

states and this would constitute being a simple policy right not a non-state

### [14:33 - 14:33]

simple policy right not a non-state

### [14:33 - 14:36]

simple policy right not a non-state varying uh uh variance in the

### [14:36 - 14:36]

varying uh uh variance in the

### [14:36 - 14:38]

varying uh uh variance in the gausian and again for non-simple

### [14:38 - 14:38]

gausian and again for non-simple

### [14:38 - 14:40]

gausian and again for non-simple policies actually that's where the story

### [14:40 - 14:40]

policies actually that's where the story

### [14:40 - 14:41]

policies actually that's where the story gets very interesting that will be the

### [14:41 - 14:41]

gets very interesting that will be the

### [14:41 - 14:43]

gets very interesting that will be the end of the talk so let me give you an

### [14:43 - 14:43]

end of the talk so let me give you an

### [14:43 - 14:45]

end of the talk so let me give you an informal statement uh you can pick your

### [14:45 - 14:45]

informal statement uh you can pick your

### [14:45 - 14:47]

informal statement uh you can pick your favorite number k favorite natural

### [14:47 - 14:47]

favorite number k favorite natural

### [14:47 - 14:49]

favorite number k favorite natural number and what I'll show you is a

### [14:49 - 14:49]

number and what I'll show you is a

### [14:49 - 14:51]

number and what I'll show you is a family of nice imitation learning

### [14:51 - 14:51]

family of nice imitation learning

### [14:51 - 14:53]

family of nice imitation learning problems so a class of of pairs of

### [14:53 - 14:53]

problems so a class of of pairs of

### [14:53 - 14:55]

problems so a class of of pairs of dynamics and policies which lies in

### [14:55 - 14:55]

dynamics and policies which lies in

### [14:55 - 14:57]

dynamics and policies which lies in three dimensions only three dimensions

### [14:57 - 14:57]

three dimensions only three dimensions

### [14:57 - 15:00]

three dimensions only three dimensions such that given n sample trajectories

### [15:00 - 15:00]

such that given n sample trajectories

### [15:00 - 15:02]

such that given n sample trajectories there is an algorithm which can imitate

### [15:02 - 15:02]

there is an algorithm which can imitate

### [15:02 - 15:04]

there is an algorithm which can imitate in let's say the L1 expert loss or you

### [15:04 - 15:04]

in let's say the L1 expert loss or you

### [15:04 - 15:06]

in let's say the L1 expert loss or you can do L2 expert loss this also works

### [15:06 - 15:06]

can do L2 expert loss this also works

### [15:06 - 15:07]

can do L2 expert loss this also works but you have to tweak things just a

### [15:07 - 15:07]

but you have to tweak things just a

### [15:07 - 15:09]

but you have to tweak things just a little bit but can estimate you know uh

### [15:09 - 15:09]

little bit but can estimate you know uh

### [15:09 - 15:11]

little bit but can estimate you know uh basically as fast as you'd like so it

### [15:11 - 15:11]

basically as fast as you'd like so it

### [15:11 - 15:12]

basically as fast as you'd like so it can estimate at a rate of one over n to

### [15:12 - 15:12]

can estimate at a rate of one over n to

### [15:12 - 15:16]

can estimate at a rate of one over n to the k right you can make k as big as you

### [15:16 - 15:16]

the k right you can make k as big as you

### [15:16 - 15:18]

the k right you can make k as big as you But and so not notice that unlike the 01

### [15:18 - 15:18]

But and so not notice that unlike the 01

### [15:18 - 15:20]

But and so not notice that unlike the 01 loss, we actually now have a notion of

### [15:20 - 15:20]

loss, we actually now have a notion of

### [15:20 - 15:21]

loss, we actually now have a notion of expert loss that can be imit can be

### [15:21 - 15:22]

expert loss that can be imit can be

### [15:22 - 15:23]

expert loss that can be imit can be minimized and can be minimized provably

### [15:23 - 15:23]

minimized and can be minimized provably

### [15:23 - 15:25]

minimized and can be minimized provably under a construction. Right? So what

### [15:25 - 15:25]

under a construction. Right? So what

### [15:25 - 15:26]

under a construction. Right? So what this says is it says that supervised

### [15:26 - 15:26]

this says is it says that supervised

### [15:26 - 15:28]

this says is it says that supervised learning on the distribution of the

### [15:28 - 15:28]

learning on the distribution of the

### [15:28 - 15:31]

learning on the distribution of the action of the demonstrator is easy. It's

### [15:31 - 15:31]

action of the demonstrator is easy. It's

### [15:31 - 15:32]

action of the demonstrator is easy. It's easy

### [15:32 - 15:32]

easy

### [15:32 - 15:37]

easy statistically. But if you try to learn a

### [15:37 - 15:37]

statistically. But if you try to learn a

### [15:37 - 15:40]

statistically. But if you try to learn a simple policy, there is a one lipits and

### [15:40 - 15:40]

simple policy, there is a one lipits and

### [15:40 - 15:41]

simple policy, there is a one lipits and a bounded cost function. So a cost

### [15:41 - 15:42]

a bounded cost function. So a cost

### [15:42 - 15:44]

a bounded cost function. So a cost function that's not too non smooth. It's

### [15:44 - 15:44]

function that's not too non smooth. It's

### [15:44 - 15:47]

function that's not too non smooth. It's not unbounded such that if you try to if

### [15:47 - 15:47]

not unbounded such that if you try to if

### [15:47 - 15:49]

not unbounded such that if you try to if you try to imitate and return only

### [15:49 - 15:49]

you try to imitate and return only

### [15:49 - 15:52]

you try to imitate and return only simple policies, your error is at least

### [15:52 - 15:52]

simple policies, your error is at least

### [15:52 - 15:55]

simple policies, your error is at least a constant times either like about one

### [15:55 - 15:55]

a constant times either like about one

### [15:55 - 15:57]

a constant times either like about one either it's a constant error or it's two

### [15:57 - 15:57]

either it's a constant error or it's two

### [15:57 - 16:00]

either it's a constant error or it's two to the horizon times your imitation

### [16:00 - 16:00]

to the horizon times your imitation

### [16:00 - 16:02]

to the horizon times your imitation learning error. Right? So again you

### [16:02 - 16:02]

learning error. Right? So again you

### [16:02 - 16:04]

learning error. Right? So again you can't that because costs are bounded of

### [16:04 - 16:04]

can't that because costs are bounded of

### [16:04 - 16:05]

can't that because costs are bounded of course your your error can be at most a

### [16:05 - 16:06]

course your your error can be at most a

### [16:06 - 16:08]

course your your error can be at most a cost a constant but in the regime where

### [16:08 - 16:08]

cost a constant but in the regime where

### [16:08 - 16:10]

cost a constant but in the regime where the imitation learning is small it can

### [16:10 - 16:10]

the imitation learning is small it can

### [16:10 - 16:12]

the imitation learning is small it can be at most a two to the horizon factor

### [16:12 - 16:12]

be at most a two to the horizon factor

### [16:12 - 16:13]

be at most a two to the horizon factor larger. Right? Right. So this is a this

### [16:13 - 16:13]

larger. Right? Right. So this is a this

### [16:13 - 16:15]

larger. Right? Right. So this is a this is a considerably larger effect of

### [16:15 - 16:15]

is a considerably larger effect of

### [16:15 - 16:16]

is a considerably larger effect of compounding error than we saw in the

### [16:16 - 16:16]

compounding error than we saw in the

### [16:16 - 16:18]

compounding error than we saw in the discrete setting which was linear in

### [16:18 - 16:18]

discrete setting which was linear in

### [16:18 - 16:19]

discrete setting which was linear in horizon 2 to the

### [16:19 - 16:19]

horizon 2 to the

### [16:19 - 16:22]

horizon 2 to the h. And again recall that this is

### [16:22 - 16:22]

h. And again recall that this is

### [16:22 - 16:23]

h. And again recall that this is measuring the excess cost of the init

### [16:23 - 16:23]

measuring the excess cost of the init

### [16:23 - 16:25]

measuring the excess cost of the init table relative to the expert. Right? So

### [16:25 - 16:25]

table relative to the expert. Right? So

### [16:25 - 16:26]

table relative to the expert. Right? So this is kind of like the kind of big

### [16:26 - 16:26]

this is kind of like the kind of big

### [16:26 - 16:28]

this is kind of like the kind of big result of our

### [16:28 - 16:28]

result of our

### [16:28 - 16:31]

result of our findings. So a couple remarks right? So

### [16:31 - 16:31]

findings. So a couple remarks right? So

### [16:31 - 16:32]

findings. So a couple remarks right? So I think the the most obvious one is now

### [16:32 - 16:32]

I think the the most obvious one is now

### [16:32 - 16:35]

I think the the most obvious one is now the deployment error this r subcost is

### [16:35 - 16:35]

the deployment error this r subcost is

### [16:35 - 16:36]

the deployment error this r subcost is exponentially larger than the expert

### [16:36 - 16:36]

exponentially larger than the expert

### [16:36 - 16:38]

exponentially larger than the expert distribution error.

### [16:38 - 16:38]

distribution error.

### [16:38 - 16:40]

distribution error. The second remark I think that's that's

### [16:40 - 16:40]

The second remark I think that's that's

### [16:40 - 16:42]

The second remark I think that's that's kind of powerful is that um our result

### [16:42 - 16:42]

kind of powerful is that um our result

### [16:42 - 16:44]

kind of powerful is that um our result depends on the structure of the imitator

### [16:44 - 16:44]

depends on the structure of the imitator

### [16:44 - 16:46]

depends on the structure of the imitator policy itself and we'll see how this

### [16:46 - 16:46]

policy itself and we'll see how this

### [16:46 - 16:48]

policy itself and we'll see how this arises from the proof but it doesn't

### [16:48 - 16:48]

arises from the proof but it doesn't

### [16:48 - 16:50]

arises from the proof but it doesn't depend on the learning algorithm. So

### [16:50 - 16:50]

depend on the learning algorithm. So

### [16:50 - 16:52]

depend on the learning algorithm. So behavior cloning, offline reinforcement

### [16:52 - 16:52]

behavior cloning, offline reinforcement

### [16:52 - 16:54]

behavior cloning, offline reinforcement learning, uh inverse RL of the version

### [16:54 - 16:54]

learning, uh inverse RL of the version

### [16:54 - 16:56]

learning, uh inverse RL of the version that doesn't use on policy data, just

### [16:56 - 16:56]

that doesn't use on policy data, just

### [16:56 - 16:58]

that doesn't use on policy data, just tries to learn a reward and optimize it

### [16:58 - 16:58]

tries to learn a reward and optimize it

### [16:58 - 17:00]

tries to learn a reward and optimize it offline. None of these approaches are

### [17:00 - 17:00]

offline. None of these approaches are

### [17:00 - 17:01]

offline. None of these approaches are going to work, right? It's truly a

### [17:01 - 17:01]

going to work, right? It's truly a

### [17:01 - 17:04]

going to work, right? It's truly a limitation of the policy class. And

### [17:04 - 17:04]

limitation of the policy class. And

### [17:04 - 17:05]

limitation of the policy class. And finally, what we'll show is how to break

### [17:05 - 17:06]

finally, what we'll show is how to break

### [17:06 - 17:07]

finally, what we'll show is how to break our lower bound with sufficiently

### [17:07 - 17:07]

our lower bound with sufficiently

### [17:07 - 17:09]

our lower bound with sufficiently improper policies. And you know,

### [17:09 - 17:09]

improper policies. And you know,

### [17:09 - 17:10]

improper policies. And you know, improperness has always been like a

### [17:10 - 17:10]

improperness has always been like a

### [17:10 - 17:12]

improperness has always been like a really kind of powerful theme in in sort

### [17:12 - 17:12]

really kind of powerful theme in in sort

### [17:12 - 17:13]

really kind of powerful theme in in sort of statistical learning. But we're

### [17:13 - 17:13]

of statistical learning. But we're

### [17:13 - 17:14]

of statistical learning. But we're actually going to see that some of the

### [17:14 - 17:14]

actually going to see that some of the

### [17:14 - 17:16]

actually going to see that some of the ways of being improper that break our

### [17:16 - 17:16]

ways of being improper that break our

### [17:16 - 17:18]

ways of being improper that break our lower bound kind of give evidence to

### [17:18 - 17:18]

lower bound kind of give evidence to

### [17:18 - 17:19]

lower bound kind of give evidence to some of the successes in recent robot

### [17:19 - 17:19]

some of the successes in recent robot

### [17:19 - 17:20]

some of the successes in recent robot learning policies. And that'll be the

### [17:20 - 17:20]

learning policies. And that'll be the

### [17:20 - 17:22]

learning policies. And that'll be the end of the talk showing how kind of

### [17:22 - 17:22]

end of the talk showing how kind of

### [17:22 - 17:23]

end of the talk showing how kind of recent advances in robot learning

### [17:23 - 17:23]

recent advances in robot learning

### [17:23 - 17:25]

recent advances in robot learning actually break our lower bound in kind

### [17:25 - 17:25]

actually break our lower bound in kind

### [17:25 - 17:28]

actually break our lower bound in kind of interesting ways. So I think the

### [17:28 - 17:28]

of interesting ways. So I think the

### [17:28 - 17:29]

of interesting ways. So I think the first thing that I'd like to do before

### [17:29 - 17:29]

first thing that I'd like to do before

### [17:29 - 17:31]

first thing that I'd like to do before going into the kind of sketch of the

### [17:31 - 17:31]

going into the kind of sketch of the

### [17:31 - 17:32]

going into the kind of sketch of the proof is to explain to you what I meant

### [17:32 - 17:32]

proof is to explain to you what I meant

### [17:32 - 17:34]

proof is to explain to you what I meant by a nice control system in a little bit

### [17:34 - 17:34]

by a nice control system in a little bit

### [17:34 - 17:36]

by a nice control system in a little bit more detail. So recall we assume that

### [17:36 - 17:36]

more detail. So recall we assume that

### [17:36 - 17:38]

more detail. So recall we assume that our dynamics and expert are

### [17:38 - 17:38]

our dynamics and expert are

### [17:38 - 17:40]

our dynamics and expert are deterministic and recall that we assume

### [17:40 - 17:40]

deterministic and recall that we assume

### [17:40 - 17:42]

deterministic and recall that we assume that these deterministic functions are

### [17:42 - 17:42]

that these deterministic functions are

### [17:42 - 17:43]

that these deterministic functions are both lip shits and smooth have second

### [17:43 - 17:44]

both lip shits and smooth have second

### [17:44 - 17:45]

both lip shits and smooth have second you know bounded first and second

### [17:45 - 17:45]

you know bounded first and second

### [17:45 - 17:47]

you know bounded first and second derivatives. But the real kind of weird

### [17:47 - 17:47]

derivatives. But the real kind of weird

### [17:47 - 17:48]

derivatives. But the real kind of weird assumption that maybe the audience might

### [17:48 - 17:48]

assumption that maybe the audience might

### [17:48 - 17:50]

assumption that maybe the audience might not be very familiar with is this notion

### [17:50 - 17:50]

not be very familiar with is this notion

### [17:50 - 17:52]

not be very familiar with is this notion of stability of exponentially incre uh

### [17:52 - 17:52]

of stability of exponentially incre uh

### [17:52 - 17:55]

of stability of exponentially incre uh incremental input to state stability.

### [17:55 - 17:55]

incremental input to state stability.

### [17:55 - 17:56]

incremental input to state stability. And it's not really clear at this point

### [17:56 - 17:56]

And it's not really clear at this point

### [17:56 - 17:59]

And it's not really clear at this point what this means. So let me kind of first

### [17:59 - 17:59]

what this means. So let me kind of first

### [17:59 - 18:00]

what this means. So let me kind of first begin by pointing out what is

### [18:00 - 18:00]

begin by pointing out what is

### [18:00 - 18:02]

begin by pointing out what is instability in control systems. Right?

### [18:02 - 18:02]

instability in control systems. Right?

### [18:02 - 18:04]

instability in control systems. Right? Right? So a control system we can think

### [18:04 - 18:04]

Right? So a control system we can think

### [18:04 - 18:06]

Right? So a control system we can think of a scalar control system. It's

### [18:06 - 18:06]

of a scalar control system. It's

### [18:06 - 18:08]

of a scalar control system. It's actually linear where the dynamics as a

### [18:08 - 18:08]

actually linear where the dynamics as a

### [18:08 - 18:10]

actually linear where the dynamics as a function of x and u are equal to twice

### [18:10 - 18:10]

function of x and u are equal to twice

### [18:10 - 18:12]

function of x and u are equal to twice the state x plus the input u. Right?

### [18:12 - 18:12]

the state x plus the input u. Right?

### [18:12 - 18:15]

the state x plus the input u. Right? This is a scalar control system. And so

### [18:15 - 18:15]

This is a scalar control system. And so

### [18:15 - 18:17]

This is a scalar control system. And so let's consider two trajectories. Uh you

### [18:17 - 18:17]

let's consider two trajectories. Uh you

### [18:17 - 18:19]

let's consider two trajectories. Uh you know one both trajectories start at the

### [18:19 - 18:19]

know one both trajectories start at the

### [18:19 - 18:22]

know one both trajectories start at the initial state x equals z. In the first

### [18:22 - 18:22]

initial state x equals z. In the first

### [18:22 - 18:23]

initial state x equals z. In the first trajectory your inputs are always

### [18:23 - 18:24]

trajectory your inputs are always

### [18:24 - 18:26]

trajectory your inputs are always selected to be zero. But in the second

### [18:26 - 18:26]

selected to be zero. But in the second

### [18:26 - 18:27]

selected to be zero. But in the second trajectory your inputs are always

### [18:27 - 18:27]

trajectory your inputs are always

### [18:27 - 18:29]

trajectory your inputs are always selected to be some number delta right

### [18:29 - 18:29]

selected to be some number delta right

### [18:29 - 18:32]

selected to be some number delta right some small parameter delta. So what

### [18:32 - 18:32]

some small parameter delta. So what

### [18:32 - 18:33]

some small parameter delta. So what happens when you plot these two

### [18:33 - 18:33]

happens when you plot these two

### [18:33 - 18:36]

happens when you plot these two trajectories on the line? Well, your

### [18:36 - 18:36]

trajectories on the line? Well, your

### [18:36 - 18:38]

trajectories on the line? Well, your first trajectory will always remain at

### [18:38 - 18:38]

first trajectory will always remain at

### [18:38 - 18:39]

first trajectory will always remain at zero because you have a linear system

### [18:39 - 18:39]

zero because you have a linear system

### [18:39 - 18:40]

zero because you have a linear system that starts at zero and you're always

### [18:40 - 18:40]

that starts at zero and you're always

### [18:40 - 18:43]

that starts at zero and you're always putting zero in. But if you start

### [18:43 - 18:43]

putting zero in. But if you start

### [18:43 - 18:44]

putting zero in. But if you start feeding in delta into the system, what

### [18:44 - 18:44]

feeding in delta into the system, what

### [18:44 - 18:46]

feeding in delta into the system, what you can show is in fact basically the

### [18:46 - 18:46]

you can show is in fact basically the

### [18:46 - 18:47]

you can show is in fact basically the magnitude of the state will grow by at

### [18:47 - 18:48]

magnitude of the state will grow by at

### [18:48 - 18:49]

magnitude of the state will grow by at least twice to the horizon because you

### [18:49 - 18:50]

least twice to the horizon because you

### [18:50 - 18:52]

least twice to the horizon because you get a factor of two here times delta.

### [18:52 - 18:52]

get a factor of two here times delta.

### [18:52 - 18:54]

get a factor of two here times delta. Right? So we call this an unstable

### [18:54 - 18:54]

Right? So we call this an unstable

### [18:54 - 18:56]

Right? So we call this an unstable system because the small perturbation

### [18:56 - 18:56]

system because the small perturbation

### [18:56 - 18:58]

system because the small perturbation delta gets magnified exponentially by

### [18:58 - 18:58]

delta gets magnified exponentially by

### [18:58 - 18:59]

delta gets magnified exponentially by the dynamics of the system. Right? This

### [18:59 - 18:59]

the dynamics of the system. Right? This

### [18:59 - 19:00]

the dynamics of the system. Right? This is a kind of one of the simplest

### [19:00 - 19:00]

is a kind of one of the simplest

### [19:00 - 19:03]

is a kind of one of the simplest examples of an unstable system, right?

### [19:03 - 19:03]

examples of an unstable system, right?

### [19:03 - 19:04]

examples of an unstable system, right? So we can think of systems that have

### [19:04 - 19:04]

So we can think of systems that have

### [19:04 - 19:06]

So we can think of systems that have high sensitivity to perturbations in the

### [19:06 - 19:06]

high sensitivity to perturbations in the

### [19:06 - 19:08]

high sensitivity to perturbations in the inputs as unstable and that's kind of

### [19:08 - 19:08]

inputs as unstable and that's kind of

### [19:08 - 19:10]

inputs as unstable and that's kind of their more kind of formal definitions of

### [19:10 - 19:10]

their more kind of formal definitions of

### [19:10 - 19:13]

their more kind of formal definitions of this. So informally you can show that if

### [19:13 - 19:13]

this. So informally you can show that if

### [19:13 - 19:16]

this. So informally you can show that if you have an unstable system uh basically

### [19:16 - 19:16]

you have an unstable system uh basically

### [19:16 - 19:17]

you have an unstable system uh basically there there exist prop learning problems

### [19:17 - 19:17]

there there exist prop learning problems

### [19:17 - 19:19]

there there exist prop learning problems which have which which are deterministic

### [19:19 - 19:19]

which have which which are deterministic

### [19:19 - 19:22]

which have which which are deterministic which are smooth but are unstable and

### [19:22 - 19:22]

which are smooth but are unstable and

### [19:22 - 19:23]

which are smooth but are unstable and every learning algorithm no matter what

### [19:23 - 19:23]

every learning algorithm no matter what

### [19:23 - 19:26]

every learning algorithm no matter what you do will basically have exponential

### [19:26 - 19:26]

you do will basically have exponential

### [19:26 - 19:28]

you do will basically have exponential compounding error uh for all

### [19:28 - 19:28]

compounding error uh for all

### [19:28 - 19:30]

compounding error uh for all sufficiently large for for all horizons

### [19:30 - 19:30]

sufficiently large for for all horizons

### [19:30 - 19:32]

sufficiently large for for all horizons that are smaller than exponential in the

### [19:32 - 19:32]

that are smaller than exponential in the

### [19:32 - 19:34]

that are smaller than exponential in the dimension. Right? So what what this says

### [19:34 - 19:34]

dimension. Right? So what what this says

### [19:34 - 19:36]

dimension. Right? So what what this says again is that our expert the policy is

### [19:36 - 19:36]

again is that our expert the policy is

### [19:36 - 19:37]

again is that our expert the policy is easy to learn on the distribution but

### [19:37 - 19:37]

easy to learn on the distribution but

### [19:37 - 19:39]

easy to learn on the distribution but when you try to deploy it you have

### [19:39 - 19:39]

when you try to deploy it you have

### [19:39 - 19:41]

when you try to deploy it you have exponential compounding error and this

### [19:41 - 19:41]

exponential compounding error and this

### [19:41 - 19:43]

exponential compounding error and this this this horizon less than a to the

### [19:43 - 19:43]

this this horizon less than a to the

### [19:43 - 19:44]

this this horizon less than a to the dimension comes from the fact that you

### [19:44 - 19:44]

dimension comes from the fact that you

### [19:44 - 19:46]

dimension comes from the fact that you can always cover the space. So there

### [19:46 - 19:46]

can always cover the space. So there

### [19:46 - 19:47]

can always cover the space. So there it's kind of interesting there but

### [19:47 - 19:47]

it's kind of interesting there but

### [19:47 - 19:48]

it's kind of interesting there but basically this says that there's nothing

### [19:48 - 19:48]

basically this says that there's nothing

### [19:48 - 19:50]

basically this says that there's nothing that you can do in an unstable system

### [19:50 - 19:50]

that you can do in an unstable system

### [19:50 - 19:52]

that you can do in an unstable system that will help you but in some sense

### [19:52 - 19:52]

that will help you but in some sense

### [19:52 - 19:53]

that will help you but in some sense this is kind of like uninteresting right

### [19:53 - 19:54]

this is kind of like uninteresting right

### [19:54 - 19:55]

this is kind of like uninteresting right so like again back to the art of proving

### [19:55 - 19:55]

so like again back to the art of proving

### [19:55 - 19:57]

so like again back to the art of proving lower bounds it's not fun to prove a

### [19:57 - 19:57]

lower bounds it's not fun to prove a

### [19:57 - 19:59]

lower bounds it's not fun to prove a lower bound in in a difficult situation

### [19:59 - 19:59]

lower bound in in a difficult situation

### [19:59 - 20:01]

lower bound in in a difficult situation because we expect things to be difficult

### [20:01 - 20:01]

because we expect things to be difficult

### [20:01 - 20:02]

because we expect things to be difficult if we if we expect our system to be very

### [20:02 - 20:02]

if we if we expect our system to be very

### [20:02 - 20:04]

if we if we expect our system to be very sensitive to perturbations obviously

### [20:04 - 20:04]

sensitive to perturbations obviously

### [20:04 - 20:05]

sensitive to perturbations obviously this is going to make compounding error

### [20:05 - 20:05]

this is going to make compounding error

### [20:05 - 20:07]

this is going to make compounding error worse and moreover kind of from a

### [20:07 - 20:07]

worse and moreover kind of from a

### [20:07 - 20:09]

worse and moreover kind of from a practical perspective instability shows

### [20:09 - 20:09]

practical perspective instability shows

### [20:09 - 20:10]

practical perspective instability shows up a lot in classical control regimes

### [20:10 - 20:10]

up a lot in classical control regimes

### [20:10 - 20:12]

up a lot in classical control regimes like aeronautics but we don't really

### [20:12 - 20:12]

like aeronautics but we don't really

### [20:12 - 20:14]

like aeronautics but we don't really believe that robot learning is a stable

### [20:14 - 20:14]

believe that robot learning is a stable

### [20:14 - 20:15]

believe that robot learning is a stable is an unstable problem We believe that

### [20:15 - 20:15]

is an unstable problem We believe that

### [20:15 - 20:17]

is an unstable problem We believe that you know much of robot learning is sort

### [20:17 - 20:17]

you know much of robot learning is sort

### [20:17 - 20:18]

you know much of robot learning is sort of very plastic. The robot has a lot of

### [20:18 - 20:18]

of very plastic. The robot has a lot of

### [20:18 - 20:20]

of very plastic. The robot has a lot of compliance in its joints and so

### [20:20 - 20:20]

compliance in its joints and so

### [20:20 - 20:22]

compliance in its joints and so instability while nice for proven

### [20:22 - 20:22]

instability while nice for proven

### [20:22 - 20:23]

instability while nice for proven counter examples is maybe the wrong

### [20:23 - 20:23]

counter examples is maybe the wrong

### [20:23 - 20:25]

counter examples is maybe the wrong paradigm to be thinking

### [20:25 - 20:25]

paradigm to be thinking

### [20:25 - 20:28]

paradigm to be thinking about. So let's actually turn back to

### [20:28 - 20:28]

about. So let's actually turn back to

### [20:28 - 20:30]

about. So let's actually turn back to nice systems systems that are stable.

### [20:30 - 20:30]

nice systems systems that are stable.

### [20:30 - 20:32]

nice systems systems that are stable. And I'm going to introduce a definition

### [20:32 - 20:32]

And I'm going to introduce a definition

### [20:32 - 20:34]

And I'm going to introduce a definition of if stability that we'll we'll explain

### [20:34 - 20:34]

of if stability that we'll we'll explain

### [20:34 - 20:36]

of if stability that we'll we'll explain in kind of greater detail. So we say

### [20:36 - 20:36]

in kind of greater detail. So we say

### [20:36 - 20:38]

in kind of greater detail. So we say this system is exponentially stable

### [20:38 - 20:38]

this system is exponentially stable

### [20:38 - 20:40]

this system is exponentially stable exponentially input uh in incremental

### [20:40 - 20:40]

exponentially input uh in incremental

### [20:40 - 20:42]

exponentially input uh in incremental input to state stable. It's a mouthful.

### [20:42 - 20:42]

input to state stable. It's a mouthful.

### [20:42 - 20:43]

input to state stable. It's a mouthful. I'm just going to call it exponential

### [20:43 - 20:43]

I'm just going to call it exponential

### [20:43 - 20:45]

I'm just going to call it exponential stability for now. If you take two

### [20:45 - 20:45]

stability for now. If you take two

### [20:45 - 20:47]

stability for now. If you take two initial states and you take two sequence

### [20:47 - 20:47]

initial states and you take two sequence

### [20:47 - 20:49]

initial states and you take two sequence of control inputs and they have the

### [20:49 - 20:49]

of control inputs and they have the

### [20:49 - 20:51]

of control inputs and they have the following property that the difference

### [20:51 - 20:51]

following property that the difference

### [20:51 - 20:53]

following property that the difference between the state at some time h + one

### [20:53 - 20:53]

between the state at some time h + one

### [20:53 - 20:56]

between the state at some time h + one decays exponentially with some parameter

### [20:56 - 20:56]

decays exponentially with some parameter

### [20:56 - 20:58]

decays exponentially with some parameter row between zero and one times the

### [20:58 - 20:58]

row between zero and one times the

### [20:58 - 20:59]

row between zero and one times the initial norm between or distance between

### [20:59 - 20:59]

initial norm between or distance between

### [20:59 - 21:02]

initial norm between or distance between the two states plus some basic kind of

### [21:02 - 21:02]

the two states plus some basic kind of

### [21:02 - 21:05]

the two states plus some basic kind of like weighted geometric sum decaying as

### [21:05 - 21:05]

like weighted geometric sum decaying as

### [21:05 - 21:06]

like weighted geometric sum decaying as row to the kind of distance of this of

### [21:06 - 21:06]

row to the kind of distance of this of

### [21:06 - 21:08]

row to the kind of distance of this of that time step from the current time

### [21:08 - 21:08]

that time step from the current time

### [21:08 - 21:10]

that time step from the current time step times the distance between the two

### [21:10 - 21:10]

step times the distance between the two

### [21:10 - 21:11]

step times the distance between the two inputs. Right? Right? So this kind of

### [21:11 - 21:11]

inputs. Right? Right? So this kind of

### [21:11 - 21:12]

inputs. Right? Right? So this kind of says that basically you have

### [21:12 - 21:12]

says that basically you have

### [21:12 - 21:15]

says that basically you have exponentially fast attenuation of the

### [21:15 - 21:15]

exponentially fast attenuation of the

### [21:15 - 21:17]

exponentially fast attenuation of the initial condition and distances in the

### [21:17 - 21:17]

initial condition and distances in the

### [21:17 - 21:19]

initial condition and distances in the inputs towards the current differences

### [21:19 - 21:19]

inputs towards the current differences

### [21:19 - 21:20]

inputs towards the current differences in the state. Right? You can think of

### [21:20 - 21:20]

in the state. Right? You can think of

### [21:20 - 21:22]

in the state. Right? You can think of this as a forgetting condition. It

### [21:22 - 21:22]

this as a forgetting condition. It

### [21:22 - 21:23]

this as a forgetting condition. It basically says that your system just

### [21:23 - 21:23]

basically says that your system just

### [21:23 - 21:25]

basically says that your system just forgets things exponentially quickly

### [21:25 - 21:25]

forgets things exponentially quickly

### [21:25 - 21:27]

forgets things exponentially quickly modulated by this parameter

### [21:27 - 21:27]

modulated by this parameter

### [21:27 - 21:29]

modulated by this parameter row. So I'll give you an example of

### [21:29 - 21:29]

row. So I'll give you an example of

### [21:29 - 21:33]

row. So I'll give you an example of this. Um if you uh if you had a system

### [21:33 - 21:33]

this. Um if you uh if you had a system

### [21:33 - 21:35]

this. Um if you uh if you had a system of this form, you start at the same

### [21:35 - 21:35]

of this form, you start at the same

### [21:35 - 21:37]

of this form, you start at the same states, but now you ch you perturb the

### [21:37 - 21:37]

states, but now you ch you perturb the

### [21:37 - 21:39]

states, but now you ch you perturb the inputs by a factor of delta. What you

### [21:39 - 21:40]

inputs by a factor of delta. What you

### [21:40 - 21:41]

inputs by a factor of delta. What you can show is that basically the

### [21:41 - 21:41]

can show is that basically the

### [21:41 - 21:42]

can show is that basically the differences in the states will remain

### [21:42 - 21:42]

differences in the states will remain

### [21:42 - 21:44]

differences in the states will remain order delta apart for all times t like

### [21:44 - 21:44]

order delta apart for all times t like

### [21:44 - 21:46]

order delta apart for all times t like unlike the unstable system where things

### [21:46 - 21:46]

unlike the unstable system where things

### [21:46 - 21:48]

unlike the unstable system where things are growing with t here all the states

### [21:48 - 21:48]

are growing with t here all the states

### [21:48 - 21:50]

are growing with t here all the states are going to be close to one another. So

### [21:50 - 21:50]

are going to be close to one another. So

### [21:50 - 21:52]

are going to be close to one another. So this is our notion of incremental

### [21:52 - 21:52]

this is our notion of incremental

### [21:52 - 21:55]

this is our notion of incremental stability. So let me kind of explain how

### [21:55 - 21:55]

stability. So let me kind of explain how

### [21:55 - 21:57]

stability. So let me kind of explain how this might look geographically or look

### [21:57 - 21:57]

this might look geographically or look

### [21:57 - 21:59]

this might look geographically or look up sort of pictorially. So you can

### [21:59 - 21:59]

up sort of pictorially. So you can

### [21:59 - 22:01]

up sort of pictorially. So you can imagine a system what we call open loop.

### [22:01 - 22:01]

imagine a system what we call open loop.

### [22:01 - 22:03]

imagine a system what we call open loop. So this says I put in inputs to the

### [22:03 - 22:03]

So this says I put in inputs to the

### [22:03 - 22:05]

So this says I put in inputs to the system and I see what comes out and

### [22:05 - 22:05]

system and I see what comes out and

### [22:05 - 22:07]

system and I see what comes out and these inputs are not viewed as functions

### [22:07 - 22:07]

these inputs are not viewed as functions

### [22:07 - 22:10]

these inputs are not viewed as functions of the state. So openloop incremental

### [22:10 - 22:10]

of the state. So openloop incremental

### [22:10 - 22:12]

of the state. So openloop incremental stability says the following. It says if

### [22:12 - 22:12]

stability says the following. It says if

### [22:12 - 22:13]

stability says the following. It says if I imagine some malicious adversary

### [22:13 - 22:13]

I imagine some malicious adversary

### [22:13 - 22:15]

I imagine some malicious adversary that's going to take these inputs and

### [22:15 - 22:15]

that's going to take these inputs and

### [22:15 - 22:17]

that's going to take these inputs and corrupt them by some amount delta. Then

### [22:17 - 22:17]

corrupt them by some amount delta. Then

### [22:17 - 22:19]

corrupt them by some amount delta. Then the resulting out uh kind of response of

### [22:19 - 22:19]

the resulting out uh kind of response of

### [22:19 - 22:21]

the resulting out uh kind of response of the system to these corruptions is going

### [22:21 - 22:21]

the system to these corruptions is going

### [22:21 - 22:22]

the system to these corruptions is going to be roughly pretty close to the

### [22:22 - 22:22]

to be roughly pretty close to the

### [22:22 - 22:24]

to be roughly pretty close to the original dynamics. Right? It just tells

### [22:24 - 22:24]

original dynamics. Right? It just tells

### [22:24 - 22:25]

original dynamics. Right? It just tells you that these two things are going to

### [22:25 - 22:25]

you that these two things are going to

### [22:25 - 22:27]

you that these two things are going to track each other pretty well as long as

### [22:27 - 22:27]

track each other pretty well as long as

### [22:27 - 22:29]

track each other pretty well as long as this adversary is constrained to only

### [22:29 - 22:29]

this adversary is constrained to only

### [22:29 - 22:30]

this adversary is constrained to only kind of making very small

### [22:30 - 22:30]

kind of making very small

### [22:30 - 22:32]

kind of making very small perturbations. So that's incremental

### [22:32 - 22:33]

perturbations. So that's incremental

### [22:33 - 22:35]

perturbations. So that's incremental stability. Perturbations of input lead

### [22:35 - 22:35]

stability. Perturbations of input lead

### [22:35 - 22:36]

stability. Perturbations of input lead to bounded states. actually not very

### [22:36 - 22:36]

to bounded states. actually not very

### [22:36 - 22:37]

to bounded states. actually not very small just sort of the perturbations

### [22:37 - 22:38]

small just sort of the perturbations

### [22:38 - 22:38]

small just sort of the perturbations here are proportional to the

### [22:38 - 22:38]

here are proportional to the

### [22:38 - 22:40]

here are proportional to the perturbations

### [22:40 - 22:40]

perturbations

### [22:40 - 22:42]

perturbations here. Uh you can also talk about this in

### [22:42 - 22:42]

here. Uh you can also talk about this in

### [22:42 - 22:44]

here. Uh you can also talk about this in closed loop. So in control and closed

### [22:44 - 22:44]

closed loop. So in control and closed

### [22:44 - 22:46]

closed loop. So in control and closed loop what we mean is that basically the

### [22:46 - 22:46]

loop what we mean is that basically the

### [22:46 - 22:48]

loop what we mean is that basically the dynam the inputs are being fed back into

### [22:48 - 22:48]

dynam the inputs are being fed back into

### [22:48 - 22:50]

dynam the inputs are being fed back into the system. So we'll say that the expert

### [22:50 - 22:50]

the system. So we'll say that the expert

### [22:50 - 22:52]

the system. So we'll say that the expert policy combined with the dynamics is

### [22:52 - 22:52]

policy combined with the dynamics is

### [22:52 - 22:55]

policy combined with the dynamics is closed loop eis. If when we think about

### [22:55 - 22:55]

closed loop eis. If when we think about

### [22:55 - 22:57]

closed loop eis. If when we think about feeding the expert back into the policy

### [22:57 - 22:57]

feeding the expert back into the policy

### [22:57 - 22:59]

feeding the expert back into the policy right so into the dynamics so we take f

### [22:59 - 22:59]

right so into the dynamics so we take f

### [22:59 - 23:01]

right so into the dynamics so we take f ofx your inputs are the the expert

### [23:01 - 23:01]

ofx your inputs are the the expert

### [23:01 - 23:03]

ofx your inputs are the the expert policy evaluated at x plus some

### [23:03 - 23:03]

policy evaluated at x plus some

### [23:03 - 23:05]

policy evaluated at x plus some perturbation. These also have the

### [23:05 - 23:05]

perturbation. These also have the

### [23:05 - 23:07]

perturbation. These also have the stability property. So pictorially it

### [23:07 - 23:07]

stability property. So pictorially it

### [23:07 - 23:10]

stability property. So pictorially it looks like this, right? So you take some

### [23:10 - 23:10]

looks like this, right? So you take some

### [23:10 - 23:11]

looks like this, right? So you take some inputs to the control system. You get

### [23:11 - 23:11]

inputs to the control system. You get

### [23:11 - 23:13]

inputs to the control system. You get out some states, but now your expert

### [23:13 - 23:13]

out some states, but now your expert

### [23:13 - 23:14]

out some states, but now your expert policy depends on the states that are

### [23:14 - 23:14]

policy depends on the states that are

### [23:14 - 23:16]

policy depends on the states that are that arise, right? So it clo it's what

### [23:16 - 23:16]

that arise, right? So it clo it's what

### [23:16 - 23:18]

that arise, right? So it clo it's what we call in control closing the loop

### [23:18 - 23:18]

we call in control closing the loop

### [23:18 - 23:20]

we call in control closing the loop feeding the states back into the policy.

### [23:20 - 23:20]

feeding the states back into the policy.

### [23:20 - 23:23]

feeding the states back into the policy. And what kind of expert closed loop EISS

### [23:23 - 23:23]

And what kind of expert closed loop EISS

### [23:23 - 23:25]

And what kind of expert closed loop EISS means is that the devil the kind of

### [23:25 - 23:25]

means is that the devil the kind of

### [23:25 - 23:27]

means is that the devil the kind of adversary is allowed to slightly perturb

### [23:27 - 23:27]

adversary is allowed to slightly perturb

### [23:27 - 23:28]

adversary is allowed to slightly perturb these inputs that the expert would have

### [23:28 - 23:28]

these inputs that the expert would have

### [23:28 - 23:30]

these inputs that the expert would have taken put them back into the system see

### [23:30 - 23:30]

taken put them back into the system see

### [23:30 - 23:33]

taken put them back into the system see the new state but crucially the expert

### [23:33 - 23:33]

the new state but crucially the expert

### [23:33 - 23:34]

the new state but crucially the expert policy is evaluated on the new states

### [23:34 - 23:34]

policy is evaluated on the new states

### [23:34 - 23:36]

policy is evaluated on the new states that the that the experts that that the

### [23:36 - 23:36]

that the that the experts that that the

### [23:36 - 23:38]

that the that the experts that that the kind of adversary sees. So we call this

### [23:38 - 23:38]

kind of adversary sees. So we call this

### [23:38 - 23:40]

kind of adversary sees. So we call this kind of incremental stability in the

### [23:40 - 23:40]

kind of incremental stability in the

### [23:40 - 23:41]

kind of incremental stability in the sense that the adversary is only

### [23:41 - 23:41]

sense that the adversary is only

### [23:41 - 23:43]

sense that the adversary is only perturbing over the expert but on its

### [23:43 - 23:43]

perturbing over the expert but on its

### [23:43 - 23:45]

perturbing over the expert but on its own trajectory right and this is the

### [23:45 - 23:45]

own trajectory right and this is the

### [23:45 - 23:47]

own trajectory right and this is the picture that we have here. So these are

### [23:47 - 23:47]

picture that we have here. So these are

### [23:47 - 23:49]

picture that we have here. So these are kind of two very kind of nice desirable

### [23:49 - 23:49]

kind of two very kind of nice desirable

### [23:49 - 23:51]

kind of two very kind of nice desirable behaviors that one might have in a

### [23:51 - 23:51]

behaviors that one might have in a

### [23:51 - 23:53]

behaviors that one might have in a control system. And again this ensures

### [23:53 - 23:53]

control system. And again this ensures

### [23:53 - 23:55]

control system. And again this ensures that these things are close. So

### [23:55 - 23:55]

that these things are close. So

### [23:55 - 23:56]

that these things are close. So ultimately what we've done is we've

### [23:56 - 23:56]

ultimately what we've done is we've

### [23:56 - 23:58]

ultimately what we've done is we've defined what we mean by a nice control

### [23:58 - 23:58]

defined what we mean by a nice control

### [23:58 - 23:59]

defined what we mean by a nice control system. We're going to assume that both

### [23:59 - 23:59]

system. We're going to assume that both

### [23:59 - 24:00]

system. We're going to assume that both the openloop dynamics right just the

### [24:00 - 24:00]

the openloop dynamics right just the

### [24:00 - 24:03]

the openloop dynamics right just the dynamics itself but also the closed loop

### [24:03 - 24:03]

dynamics itself but also the closed loop

### [24:03 - 24:05]

dynamics itself but also the closed loop dynamics what the expert would do are

### [24:05 - 24:05]

dynamics what the expert would do are

### [24:05 - 24:07]

dynamics what the expert would do are both sort of exponentially insensitive

### [24:07 - 24:07]

both sort of exponentially insensitive

### [24:07 - 24:09]

both sort of exponentially insensitive to perturbations. These perturbations

### [24:09 - 24:09]

to perturbations. These perturbations

### [24:09 - 24:11]

to perturbations. These perturbations become forgotten exponentially quickly.

### [24:11 - 24:11]

become forgotten exponentially quickly.

### [24:11 - 24:12]

become forgotten exponentially quickly. Right? And this is kind of the most that

### [24:12 - 24:12]

Right? And this is kind of the most that

### [24:12 - 24:14]

Right? And this is kind of the most that you can hope for from both an expert and

### [24:14 - 24:14]

you can hope for from both an expert and

### [24:14 - 24:15]

you can hope for from both an expert and from a dynamics function in terms of

### [24:15 - 24:15]

from a dynamics function in terms of

### [24:15 - 24:18]

from a dynamics function in terms of being kind of regular and well

### [24:18 - 24:18]

being kind of regular and well

### [24:18 - 24:23]

being kind of regular and well behaved. Cool. So again, right, what

### [24:23 - 24:23]

behaved. Cool. So again, right, what

### [24:23 - 24:25]

behaved. Cool. So again, right, what does our theorem tell us? Our theorem

### [24:25 - 24:25]

does our theorem tell us? Our theorem

### [24:25 - 24:27]

does our theorem tell us? Our theorem says even under this exponential

### [24:27 - 24:27]

says even under this exponential

### [24:27 - 24:30]

says even under this exponential incremental stability uh uh condition,

### [24:30 - 24:30]

incremental stability uh uh condition,

### [24:30 - 24:32]

incremental stability uh uh condition, we still have exponential compounding

### [24:32 - 24:32]

we still have exponential compounding

### [24:32 - 24:34]

we still have exponential compounding error. And this should surprise you,

### [24:34 - 24:34]

error. And this should surprise you,

### [24:34 - 24:36]

error. And this should surprise you, right? Because on the one hand I've told

### [24:36 - 24:36]

right? Because on the one hand I've told

### [24:36 - 24:37]

right? Because on the one hand I've told you I have a property that makes my

### [24:37 - 24:37]

you I have a property that makes my

### [24:37 - 24:40]

you I have a property that makes my systems exponentially forget errors

### [24:40 - 24:40]

systems exponentially forget errors

### [24:40 - 24:42]

systems exponentially forget errors really quickly and on the other hand

### [24:42 - 24:42]

really quickly and on the other hand

### [24:42 - 24:43]

really quickly and on the other hand I've told you that I have a I have a

### [24:43 - 24:43]

I've told you that I have a I have a

### [24:43 - 24:45]

I've told you that I have a I have a setting where I can get do the learn how

### [24:45 - 24:45]

setting where I can get do the learn how

### [24:45 - 24:47]

setting where I can get do the learn how to do the right thing but yet this

### [24:47 - 24:47]

to do the right thing but yet this

### [24:47 - 24:49]

to do the right thing but yet this perturbations I make by like not

### [24:49 - 24:49]

perturbations I make by like not

### [24:49 - 24:51]

perturbations I make by like not estimating perfectly compound

### [24:51 - 24:51]

estimating perfectly compound

### [24:51 - 24:53]

estimating perfectly compound exponentially largely through the system

### [24:53 - 24:53]

exponentially largely through the system

### [24:53 - 24:55]

exponentially largely through the system right so these two properties seem to be

### [24:55 - 24:55]

right so these two properties seem to be

### [24:55 - 24:57]

right so these two properties seem to be at odds right the system forgets

### [24:57 - 24:57]

at odds right the system forgets

### [24:57 - 24:58]

at odds right the system forgets perturbations exponentially quickly but

### [24:58 - 24:58]

perturbations exponentially quickly but

### [24:58 - 25:00]

perturbations exponentially quickly but that learning is ex is sort of

### [25:00 - 25:00]

that learning is ex is sort of

### [25:00 - 25:02]

that learning is ex is sort of exponentially sensitive to these

### [25:02 - 25:02]

exponentially sensitive to these

### [25:02 - 25:04]

exponentially sensitive to these perturbations so I want to kind of

### [25:04 - 25:04]

perturbations so I want to kind of

### [25:04 - 25:05]

perturbations so I want to kind of explain how it's possible for these two

### [25:05 - 25:05]

explain how it's possible for these two

### [25:05 - 25:08]

explain how it's possible for these two things to be to co kind of coexist and

### [25:08 - 25:08]

things to be to co kind of coexist and

### [25:08 - 25:12]

things to be to co kind of coexist and sort of to do this right to do this I'm

### [25:12 - 25:12]

sort of to do this right to do this I'm

### [25:12 - 25:13]

sort of to do this right to do this I'm going to actually dive into a very

### [25:13 - 25:13]

going to actually dive into a very

### [25:13 - 25:16]

going to actually dive into a very simple example from linear control

### [25:16 - 25:16]

simple example from linear control

### [25:16 - 25:18]

simple example from linear control explain what can go on hey Max I have a

### [25:18 - 25:18]

explain what can go on hey Max I have a

### [25:18 - 25:19]

explain what can go on hey Max I have a question

### [25:19 - 25:19]

question

### [25:19 - 25:22]

question um so somehow in my head I'm I'm trying

### [25:22 - 25:22]

um so somehow in my head I'm I'm trying

### [25:22 - 25:23]

um so somehow in my head I'm I'm trying to figure out why this is true also and

### [25:23 - 25:23]

to figure out why this is true also and

### [25:23 - 25:25]

to figure out why this is true also and I'm um in my head I feel like actually

### [25:25 - 25:25]

I'm um in my head I feel like actually

### [25:25 - 25:27]

I'm um in my head I feel like actually having noise in the dynamic could help

### [25:27 - 25:27]

having noise in the dynamic could help

### [25:27 - 25:30]

having noise in the dynamic could help you because like once you make a mistake

### [25:30 - 25:30]

you because like once you make a mistake

### [25:30 - 25:34]

you because like once you make a mistake you're like completely OD exactly

### [25:34 - 25:34]

you're like completely OD exactly

### [25:34 - 25:35]

you're like completely OD exactly So having are like completely

### [25:35 - 25:35]

So having are like completely

### [25:35 - 25:37]

So having are like completely uncontrolled in some sense but maybe if

### [25:37 - 25:37]

uncontrolled in some sense but maybe if

### [25:37 - 25:39]

uncontrolled in some sense but maybe if there's noise you're actually not really

### [25:39 - 25:39]

there's noise you're actually not really

### [25:39 - 25:40]

there's noise you're actually not really OD you're just like shifted in

### [25:40 - 25:40]

OD you're just like shifted in

### [25:40 - 25:43]

OD you're just like shifted in distribution. Exactly. So noise in the

### [25:43 - 25:43]

distribution. Exactly. So noise in the

### [25:43 - 25:44]

distribution. Exactly. So noise in the dynamics can help you a little bit

### [25:44 - 25:44]

dynamics can help you a little bit

### [25:44 - 25:46]

dynamics can help you a little bit though your rates will your rates will

### [25:46 - 25:46]

though your rates will your rates will

### [25:46 - 25:48]

though your rates will your rates will degrade with with noise. It actually

### [25:48 - 25:48]

degrade with with noise. It actually

### [25:48 - 25:49]

degrade with with noise. It actually turns out in some follow-up work we're

### [25:49 - 25:49]

turns out in some follow-up work we're

### [25:49 - 25:51]

turns out in some follow-up work we're able to show that you can use noise in a

### [25:51 - 25:51]

able to show that you can use noise in a

### [25:51 - 25:52]

able to show that you can use noise in a way that doesn't cause the rates to

### [25:52 - 25:52]

way that doesn't cause the rates to

### [25:52 - 25:54]

way that doesn't cause the rates to degrade with noise but nevertheless uses

### [25:54 - 25:54]

degrade with noise but nevertheless uses

### [25:54 - 25:56]

degrade with noise but nevertheless uses noise to cover basically just what just

### [25:56 - 25:56]

noise to cover basically just what just

### [25:56 - 25:58]

noise to cover basically just what just the bare minimum of what you need but it

### [25:58 - 25:58]

the bare minimum of what you need but it

### [25:58 - 25:59]

the bare minimum of what you need but it doesn't follow through measure theoretic

### [25:59 - 25:59]

doesn't follow through measure theoretic

### [25:59 - 26:01]

doesn't follow through measure theoretic arguments. Okay. So I think I think I

### [26:01 - 26:01]

arguments. Okay. So I think I think I

### [26:01 - 26:03]

arguments. Okay. So I think I think I think that the thing that's kind of uh

### [26:03 - 26:03]

think that the thing that's kind of uh

### [26:03 - 26:05]

think that the thing that's kind of uh that that that's that that so you're

### [26:05 - 26:05]

that that that's that that so you're

### [26:05 - 26:07]

that that that's that that so you're right like you can go every you can for

### [26:07 - 26:07]

right like you can go every you can for

### [26:07 - 26:08]

right like you can go every you can for example if there's noise in the system

### [26:08 - 26:08]

example if there's noise in the system

### [26:08 - 26:09]

example if there's noise in the system you have uh you know absolutely

### [26:09 - 26:10]

you have uh you know absolutely

### [26:10 - 26:11]

you have uh you know absolutely continuous densities you can even use

### [26:11 - 26:11]

continuous densities you can even use

### [26:11 - 26:13]

continuous densities you can even use log loss but if you don't want to use

### [26:13 - 26:13]

log loss but if you don't want to use

### [26:13 - 26:14]

log loss but if you don't want to use measure theoretic arguments and you kind

### [26:14 - 26:14]

measure theoretic arguments and you kind

### [26:14 - 26:16]

measure theoretic arguments and you kind of want to understand things like purely

### [26:16 - 26:16]

of want to understand things like purely

### [26:16 - 26:18]

of want to understand things like purely just sort of uh purely sort of

### [26:18 - 26:18]

just sort of uh purely sort of

### [26:18 - 26:20]

just sort of uh purely sort of geometrically or control theoretically

### [26:20 - 26:20]

geometrically or control theoretically

### [26:20 - 26:21]

geometrically or control theoretically um you yeah you're right that that the

### [26:21 - 26:21]

um you yeah you're right that that the

### [26:21 - 26:24]

um you yeah you're right that that the absence of noise the the absence of

### [26:24 - 26:24]

absence of noise the the absence of

### [26:24 - 26:26]

absence of noise the the absence of noise can make things more difficult um

### [26:26 - 26:26]

noise can make things more difficult um

### [26:26 - 26:28]

noise can make things more difficult um but actually it turns out and we I won't

### [26:28 - 26:28]

but actually it turns out and we I won't

### [26:28 - 26:29]

but actually it turns out and we I won't get to in this talk really what noise

### [26:29 - 26:29]

get to in this talk really what noise

### [26:29 - 26:31]

get to in this talk really what noise buys you a better way interpret what

### [26:31 - 26:31]

buys you a better way interpret what

### [26:31 - 26:32]

buys you a better way interpret what noise buys you as some sort of kind of

### [26:32 - 26:32]

noise buys you as some sort of kind of

### [26:32 - 26:34]

noise buys you as some sort of kind of like geometric anti concentration rather

### [26:34 - 26:34]

like geometric anti concentration rather

### [26:34 - 26:36]

like geometric anti concentration rather than sort of measure theor sort of

### [26:36 - 26:36]

than sort of measure theor sort of

### [26:36 - 26:37]

than sort of measure theor sort of measure a probabilistic anti

### [26:37 - 26:37]

measure a probabilistic anti

### [26:37 - 26:38]

measure a probabilistic anti concentration that's more of the correct

### [26:38 - 26:38]

concentration that's more of the correct

### [26:38 - 26:40]

concentration that's more of the correct makes sense makes sense yeah yeah cool

### [26:40 - 26:40]

makes sense makes sense yeah yeah cool

### [26:40 - 26:43]

makes sense makes sense yeah yeah cool cool question cool so let me kind of

### [26:43 - 26:43]

cool question cool so let me kind of

### [26:43 - 26:45]

cool question cool so let me kind of explain but but here um so for example a

### [26:45 - 26:45]

explain but but here um so for example a

### [26:45 - 26:46]

explain but but here um so for example a is asking this in part because Adam and

### [26:46 - 26:46]

is asking this in part because Adam and

### [26:46 - 26:49]

is asking this in part because Adam and I and ash and others on the call maybe

### [26:49 - 26:49]

I and ash and others on the call maybe

### [26:49 - 26:51]

I and ash and others on the call maybe were uh wrote a paper called butterfly

### [26:51 - 26:51]

were uh wrote a paper called butterfly

### [26:51 - 26:52]

were uh wrote a paper called butterfly effects of SGD which you guys should

### [26:52 - 26:52]

effects of SGD which you guys should

### [26:52 - 26:54]

effects of SGD which you guys should check out uh where we sort of show that

### [26:54 - 26:54]

check out uh where we sort of show that

### [26:54 - 26:56]

check out uh where we sort of show that like policies kind of derail themselves

### [26:56 - 26:56]

like policies kind of derail themselves

### [26:56 - 26:58]

like policies kind of derail themselves by going off distribution and they just

### [26:58 - 26:58]

by going off distribution and they just

### [26:58 - 27:00]

by going off distribution and they just don't know what to do uh here we'll will

### [27:00 - 27:00]

don't know what to do uh here we'll will

### [27:00 - 27:01]

don't know what to do uh here we'll will show actually that it's not that the

### [27:01 - 27:01]

show actually that it's not that the

### [27:01 - 27:02]

show actually that it's not that the policy doesn't know what to do. It's

### [27:02 - 27:02]

policy doesn't know what to do. It's

### [27:02 - 27:04]

policy doesn't know what to do. It's really that the policy cannot like

### [27:04 - 27:04]

really that the policy cannot like

### [27:04 - 27:05]

really that the policy cannot like provably cannot figure out how to

### [27:05 - 27:06]

provably cannot figure out how to

### [27:06 - 27:08]

provably cannot figure out how to respond. And I'll explain how this

### [27:08 - 27:08]

respond. And I'll explain how this

### [27:08 - 27:10]

respond. And I'll explain how this works. So what we'll do here is we're

### [27:10 - 27:10]

works. So what we'll do here is we're

### [27:10 - 27:11]

works. So what we'll do here is we're going to introduce linear control

### [27:11 - 27:11]

going to introduce linear control

### [27:11 - 27:13]

going to introduce linear control systems very briefly. We'll explain what

### [27:13 - 27:13]

systems very briefly. We'll explain what

### [27:13 - 27:14]

systems very briefly. We'll explain what incremental stability means for linear

### [27:14 - 27:14]

incremental stability means for linear

### [27:14 - 27:16]

incremental stability means for linear control systems and we'll show how

### [27:16 - 27:16]

control systems and we'll show how

### [27:16 - 27:17]

control systems and we'll show how there's actually a tension between

### [27:17 - 27:17]

there's actually a tension between

### [27:17 - 27:19]

there's actually a tension between imitation and stability of these systems

### [27:19 - 27:19]

imitation and stability of these systems

### [27:19 - 27:21]

imitation and stability of these systems and then we'll general gesture to how

### [27:21 - 27:21]

and then we'll general gesture to how

### [27:21 - 27:23]

and then we'll general gesture to how one would prove a general result. So a

### [27:23 - 27:23]

one would prove a general result. So a

### [27:23 - 27:25]

one would prove a general result. So a linear system is simply just a dynamical

### [27:25 - 27:25]

linear system is simply just a dynamical

### [27:25 - 27:26]

linear system is simply just a dynamical system where the map is a linear

### [27:26 - 27:26]

system where the map is a linear

### [27:26 - 27:28]

system where the map is a linear function and that linearity necessitates

### [27:28 - 27:28]

function and that linearity necessitates

### [27:28 - 27:30]

function and that linearity necessitates that the map takes the following form xt

### [27:30 - 27:30]

that the map takes the following form xt

### [27:30 - 27:33]

that the map takes the following form xt + 1 is axt plus b

### [27:33 - 27:33]

+ 1 is axt plus b

### [27:33 - 27:36]

+ 1 is axt plus b ut right so in particular if b is the

### [27:36 - 27:36]

ut right so in particular if b is the

### [27:36 - 27:38]

ut right so in particular if b is the identity matrix then a linear system can

### [27:38 - 27:38]

identity matrix then a linear system can

### [27:38 - 27:40]

identity matrix then a linear system can be shown to be exponentially stable if

### [27:40 - 27:40]

be shown to be exponentially stable if

### [27:40 - 27:43]

be shown to be exponentially stable if and only if uh the spectral radius of a

### [27:43 - 27:43]

and only if uh the spectral radius of a

### [27:43 - 27:44]

and only if uh the spectral radius of a which is denoted as the maximum

### [27:44 - 27:44]

which is denoted as the maximum

### [27:44 - 27:46]

which is denoted as the maximum magnitude of the real part of the igen

### [27:46 - 27:46]

magnitude of the real part of the igen

### [27:46 - 27:49]

magnitude of the real part of the igen values of a is strictly less than one.

### [27:49 - 27:49]

values of a is strictly less than one.

### [27:49 - 27:51]

values of a is strictly less than one. So one maybe one way to see this is that

### [27:51 - 27:51]

So one maybe one way to see this is that

### [27:51 - 27:53]

So one maybe one way to see this is that if you unroll the dynamics you get

### [27:53 - 27:53]

if you unroll the dynamics you get

### [27:53 - 27:55]

if you unroll the dynamics you get powers of a and the spectral radius of a

### [27:55 - 27:55]

powers of a and the spectral radius of a

### [27:55 - 27:56]

powers of a and the spectral radius of a basically dictates the behavior of the

### [27:56 - 27:56]

basically dictates the behavior of the

### [27:56 - 27:58]

basically dictates the behavior of the powers. So if row a is less than one

### [27:58 - 27:58]

powers. So if row a is less than one

### [27:58 - 28:00]

powers. So if row a is less than one these powers decay exponentially quickly

### [28:00 - 28:00]

these powers decay exponentially quickly

### [28:00 - 28:01]

these powers decay exponentially quickly but if row is greater than one the

### [28:01 - 28:01]

but if row is greater than one the

### [28:01 - 28:03]

but if row is greater than one the powers get exponentially larger. So

### [28:03 - 28:03]

powers get exponentially larger. So

### [28:03 - 28:04]

powers get exponentially larger. So what's nice is we have a very kind of

### [28:04 - 28:04]

what's nice is we have a very kind of

### [28:04 - 28:06]

what's nice is we have a very kind of easy way of characterizing stability for

### [28:06 - 28:06]

easy way of characterizing stability for

### [28:06 - 28:10]

easy way of characterizing stability for make for for for linear systems of this

### [28:14 - 28:14]

form. Cool. So um we can actually prove

### [28:14 - 28:17]

form. Cool. So um we can actually prove like a nice little lema which says that

### [28:17 - 28:17]

like a nice little lema which says that

### [28:17 - 28:20]

like a nice little lema which says that um if you have uh if you just you can

### [28:20 - 28:20]

um if you have uh if you just you can

### [28:20 - 28:22]

um if you have uh if you just you can kind of compute that basically the

### [28:22 - 28:22]

kind of compute that basically the

### [28:22 - 28:23]

kind of compute that basically the closed loop dynamics with linear

### [28:23 - 28:23]

closed loop dynamics with linear

### [28:23 - 28:25]

closed loop dynamics with linear dynamics and a linear feedback policy.

### [28:25 - 28:25]

dynamics and a linear feedback policy.

### [28:25 - 28:26]

dynamics and a linear feedback policy. So a linear feedback policy is just a

### [28:26 - 28:26]

So a linear feedback policy is just a

### [28:26 - 28:28]

So a linear feedback policy is just a linear policy and it will take the form

### [28:28 - 28:28]

linear policy and it will take the form

### [28:28 - 28:31]

linear policy and it will take the form uh pi of x= k * x and you can kind of

### [28:31 - 28:31]

uh pi of x= k * x and you can kind of

### [28:31 - 28:33]

uh pi of x= k * x and you can kind of directly compute what the closed loop

### [28:33 - 28:33]

directly compute what the closed loop

### [28:33 - 28:35]

directly compute what the closed loop dynamics are by feeding the linear

### [28:35 - 28:35]

dynamics are by feeding the linear

### [28:35 - 28:39]

dynamics are by feeding the linear policy into the dynamics map right and

### [28:39 - 28:39]

policy into the dynamics map right and

### [28:39 - 28:41]

policy into the dynamics map right and you can actually then show by computing

### [28:41 - 28:41]

you can actually then show by computing

### [28:41 - 28:42]

you can actually then show by computing this and using the previous observation

### [28:42 - 28:42]

this and using the previous observation

### [28:42 - 28:44]

this and using the previous observation that if b is the identity basically the

### [28:44 - 28:44]

that if b is the identity basically the

### [28:44 - 28:46]

that if b is the identity basically the closed loop dynamics are exponentially

### [28:46 - 28:46]

closed loop dynamics are exponentially

### [28:46 - 28:48]

closed loop dynamics are exponentially stable if and only if the spectral

### [28:48 - 28:48]

stable if and only if the spectral

### [28:48 - 28:50]

stable if and only if the spectral radius of a plus the feedback map are

### [28:50 - 28:50]

radius of a plus the feedback map are

### [28:50 - 28:52]

radius of a plus the feedback map are less than one and in particular um you

### [28:52 - 28:52]

less than one and in particular um you

### [28:52 - 28:54]

less than one and in particular um you have exponential perturbation sity if if

### [28:54 - 28:54]

have exponential perturbation sity if if

### [28:54 - 28:57]

have exponential perturbation sity if if the spectral radius of rope of of a plus

### [28:57 - 28:57]

the spectral radius of rope of of a plus

### [28:57 - 28:59]

the spectral radius of rope of of a plus the feedback max map is greater than

### [28:59 - 28:59]

the feedback max map is greater than

### [28:59 - 29:01]

the feedback max map is greater than one. Right? So this is kind of gives you

### [29:01 - 29:01]

one. Right? So this is kind of gives you

### [29:01 - 29:02]

one. Right? So this is kind of gives you a nice characterization of closed loop

### [29:02 - 29:02]

a nice characterization of closed loop

### [29:02 - 29:03]

a nice characterization of closed loop stability as well just using the

### [29:03 - 29:04]

stability as well just using the

### [29:04 - 29:04]

stability as well just using the previous

### [29:04 - 29:05]

previous

### [29:05 - 29:09]

previous slide. Cool. So in particular this means

### [29:09 - 29:09]

slide. Cool. So in particular this means

### [29:09 - 29:10]

slide. Cool. So in particular this means if you have the following situation

### [29:10 - 29:10]

if you have the following situation

### [29:10 - 29:12]

if you have the following situation where you have a matrix A and two

### [29:12 - 29:12]

where you have a matrix A and two

### [29:12 - 29:15]

where you have a matrix A and two feedback kind of control matrices K star

### [29:15 - 29:15]

feedback kind of control matrices K star

### [29:15 - 29:18]

feedback kind of control matrices K star and K hat. If row of a is less than one

### [29:18 - 29:18]

and K hat. If row of a is less than one

### [29:18 - 29:20]

and K hat. If row of a is less than one but and row of a plus k star is less

### [29:20 - 29:20]

but and row of a plus k star is less

### [29:20 - 29:23]

but and row of a plus k star is less than one but row of a plus k hat is

### [29:23 - 29:23]

than one but row of a plus k hat is

### [29:23 - 29:25]

than one but row of a plus k hat is bigger than one you arise in the you you

### [29:25 - 29:25]

bigger than one you arise in the you you

### [29:25 - 29:26]

bigger than one you arise in the you you find yourself in the following

### [29:26 - 29:26]

find yourself in the following

### [29:26 - 29:29]

find yourself in the following situation. First row of a less than one

### [29:29 - 29:29]

situation. First row of a less than one

### [29:29 - 29:31]

situation. First row of a less than one means that the openloop dynamics are

### [29:31 - 29:31]

means that the openloop dynamics are

### [29:31 - 29:34]

means that the openloop dynamics are eis. The situation row a plus k star

### [29:34 - 29:34]

eis. The situation row a plus k star

### [29:34 - 29:35]

eis. The situation row a plus k star less than one means that the closed loop

### [29:35 - 29:35]

less than one means that the closed loop

### [29:35 - 29:37]

less than one means that the closed loop dynamics under an expert are also

### [29:37 - 29:37]

dynamics under an expert are also

### [29:37 - 29:39]

dynamics under an expert are also exponentially stable. that expert is

### [29:39 - 29:39]

exponentially stable. that expert is

### [29:39 - 29:42]

exponentially stable. that expert is just playing Kstar X. But now if your

### [29:42 - 29:42]

just playing Kstar X. But now if your

### [29:42 - 29:44]

just playing Kstar X. But now if your imitator policy was trying to play K

### [29:44 - 29:44]

imitator policy was trying to play K

### [29:44 - 29:47]

imitator policy was trying to play K hat, then in fact you would be

### [29:47 - 29:47]

hat, then in fact you would be

### [29:47 - 29:49]

hat, then in fact you would be exponentially sensitive to perturbations

### [29:49 - 29:49]

exponentially sensitive to perturbations

### [29:49 - 29:51]

exponentially sensitive to perturbations uh under the imitation dynamics. Right?

### [29:51 - 29:51]

uh under the imitation dynamics. Right?

### [29:51 - 29:53]

uh under the imitation dynamics. Right? So if K hat is your imitator, then you'd

### [29:53 - 29:53]

So if K hat is your imitator, then you'd

### [29:53 - 29:54]

So if K hat is your imitator, then you'd be exponentially sensitive to

### [29:54 - 29:54]

be exponentially sensitive to

### [29:54 - 29:57]

be exponentially sensitive to perturbations, right? So what this

### [29:57 - 29:57]

perturbations, right? So what this

### [29:57 - 30:00]

perturbations, right? So what this suggests is basically um uh so basically

### [30:00 - 30:00]

suggests is basically um uh so basically

### [30:00 - 30:03]

suggests is basically um uh so basically uh let's see if this is important. Um,

### [30:03 - 30:03]

uh let's see if this is important. Um,

### [30:03 - 30:05]

uh let's see if this is important. Um, so kind of what this looks like is is

### [30:05 - 30:05]

so kind of what this looks like is is

### [30:05 - 30:07]

so kind of what this looks like is is that basically you have low error

### [30:07 - 30:07]

that basically you have low error

### [30:07 - 30:08]

that basically you have low error sensitivity for both your open loop and

### [30:08 - 30:08]

sensitivity for both your open loop and

### [30:08 - 30:10]

sensitivity for both your open loop and your expert. But somehow when you try to

### [30:10 - 30:10]

your expert. But somehow when you try to

### [30:10 - 30:12]

your expert. But somehow when you try to learn the policy itself, you get

### [30:12 - 30:12]

learn the policy itself, you get

### [30:12 - 30:13]

learn the policy itself, you get something that just can go off the rails

### [30:13 - 30:14]

something that just can go off the rails

### [30:14 - 30:15]

something that just can go off the rails really

### [30:15 - 30:15]

really

### [30:15 - 30:18]

really easily. So to prove a lower bound then

### [30:18 - 30:18]

easily. So to prove a lower bound then

### [30:18 - 30:20]

easily. So to prove a lower bound then we want to basically show that we're in

### [30:20 - 30:20]

we want to basically show that we're in

### [30:20 - 30:22]

we want to basically show that we're in a situation where something like this

### [30:22 - 30:22]

a situation where something like this

### [30:22 - 30:23]

a situation where something like this can occur, right? We want to show that

### [30:23 - 30:23]

can occur, right? We want to show that

### [30:23 - 30:25]

can occur, right? We want to show that we're in a situation where where where

### [30:25 - 30:25]

we're in a situation where where where

### [30:25 - 30:26]

we're in a situation where where where our k stars can have this kind of

### [30:26 - 30:26]

our k stars can have this kind of

### [30:26 - 30:28]

our k stars can have this kind of spectral property, but any k hat we

### [30:28 - 30:28]

spectral property, but any k hat we

### [30:28 - 30:30]

spectral property, but any k hat we learn is strictly greater than one. And

### [30:30 - 30:30]

learn is strictly greater than one. And

### [30:30 - 30:32]

learn is strictly greater than one. And I'm not going to show you the exact

### [30:32 - 30:32]

I'm not going to show you the exact

### [30:32 - 30:33]

I'm not going to show you the exact matrices, but in fact we can show that

### [30:33 - 30:33]

matrices, but in fact we can show that

### [30:33 - 30:35]

matrices, but in fact we can show that there's actually just 2x two matrices. A

### [30:35 - 30:36]

there's actually just 2x two matrices. A

### [30:36 - 30:37]

there's actually just 2x two matrices. A pair of 2x2 matrices that have the

### [30:37 - 30:37]

pair of 2x2 matrices that have the

### [30:37 - 30:39]

pair of 2x2 matrices that have the following properties. So the matrices

### [30:39 - 30:39]

following properties. So the matrices

### [30:39 - 30:41]

following properties. So the matrices are such that the spectral radius of AI

### [30:41 - 30:41]

are such that the spectral radius of AI

### [30:41 - 30:43]

are such that the spectral radius of AI and AI plus k star i. This is like think

### [30:43 - 30:43]

and AI plus k star i. This is like think

### [30:43 - 30:45]

and AI plus k star i. This is like think of this as the expert controller for

### [30:45 - 30:45]

of this as the expert controller for

### [30:45 - 30:47]

of this as the expert controller for this pair are both strictly less than

### [30:47 - 30:47]

this pair are both strictly less than

### [30:47 - 30:48]

this pair are both strictly less than one. Right? So what this is telling us

### [30:48 - 30:48]

one. Right? So what this is telling us

### [30:48 - 30:50]

one. Right? So what this is telling us is that basically that the that both

### [30:50 - 30:50]

is that basically that the that both

### [30:50 - 30:52]

is that basically that the that both open and closed loop were exponentially

### [30:52 - 30:52]

open and closed loop were exponentially

### [30:52 - 30:55]

open and closed loop were exponentially stable for kind of the linear control

### [30:55 - 30:55]

stable for kind of the linear control

### [30:55 - 30:57]

stable for kind of the linear control problem and the linear expert. But on

### [30:57 - 30:57]

problem and the linear expert. But on

### [30:57 - 30:59]

problem and the linear expert. But on the other hand, what we'll set this this

### [30:59 - 30:59]

the other hand, what we'll set this this

### [30:59 - 31:01]

the other hand, what we'll set this this pair exists in such a way that for any

### [31:01 - 31:01]

pair exists in such a way that for any

### [31:01 - 31:02]

pair exists in such a way that for any matrix which could be learned from

### [31:02 - 31:02]

matrix which could be learned from

### [31:02 - 31:04]

matrix which could be learned from imitation learning data. I'll explain

### [31:04 - 31:04]

imitation learning data. I'll explain

### [31:04 - 31:06]

imitation learning data. I'll explain what that means in a second. Uh there's

### [31:06 - 31:06]

what that means in a second. Uh there's

### [31:06 - 31:08]

what that means in a second. Uh there's going to be one system where the

### [31:08 - 31:08]

going to be one system where the

### [31:08 - 31:10]

going to be one system where the spectral radius of ai plus k hat is

### [31:10 - 31:10]

spectral radius of ai plus k hat is

### [31:10 - 31:12]

spectral radius of ai plus k hat is strictly greater than one stated

### [31:12 - 31:12]

strictly greater than one stated

### [31:12 - 31:14]

strictly greater than one stated otherwise there will be one system where

### [31:14 - 31:14]

otherwise there will be one system where

### [31:14 - 31:17]

otherwise there will be one system where k hat has to destabilize those systems.

### [31:17 - 31:17]

k hat has to destabilize those systems.

### [31:17 - 31:19]

k hat has to destabilize those systems. Right? So we we can we so both of these

### [31:19 - 31:19]

Right? So we we can we so both of these

### [31:19 - 31:20]

Right? So we we can we so both of these spectral radi are I mean both of these

### [31:20 - 31:20]

spectral radi are I mean both of these

### [31:20 - 31:22]

spectral radi are I mean both of these systems are stable but whatever you

### [31:22 - 31:22]

systems are stable but whatever you

### [31:22 - 31:24]

systems are stable but whatever you learn from imitation learning will have

### [31:24 - 31:24]

learn from imitation learning will have

### [31:24 - 31:27]

learn from imitation learning will have to destabilize one system.

### [31:27 - 31:27]

to destabilize one system.

### [31:27 - 31:30]

to destabilize one system. Okay. So, okay. So, this is this is what

### [31:30 - 31:30]

Okay. So, okay. So, this is this is what

### [31:30 - 31:31]

Okay. So, okay. So, this is this is what we're showing. So, notice that obviously

### [31:31 - 31:31]

we're showing. So, notice that obviously

### [31:31 - 31:33]

we're showing. So, notice that obviously there is a way to stabilize both

### [31:33 - 31:33]

there is a way to stabilize both

### [31:33 - 31:35]

there is a way to stabilize both systems. The controller K equals0

### [31:35 - 31:35]

systems. The controller K equals0

### [31:35 - 31:36]

systems. The controller K equals0 stabilizes both systems because both

### [31:36 - 31:36]

stabilizes both systems because both

### [31:36 - 31:38]

stabilizes both systems because both systems are open loop stable. So, we

### [31:38 - 31:38]

systems are open loop stable. So, we

### [31:38 - 31:40]

systems are open loop stable. So, we need to show that this applies only to

### [31:40 - 31:40]

need to show that this applies only to

### [31:40 - 31:41]

need to show that this applies only to K's which can possibly learn from

### [31:41 - 31:41]

K's which can possibly learn from

### [31:41 - 31:44]

K's which can possibly learn from imitation learning data and let me

### [31:44 - 31:44]

imitation learning data and let me

### [31:44 - 31:46]

imitation learning data and let me explain what this looks like. Okay. So,

### [31:46 - 31:46]

explain what this looks like. Okay. So,

### [31:46 - 31:48]

explain what this looks like. Okay. So, what we'll do is we'll construct our two

### [31:48 - 31:48]

what we'll do is we'll construct our two

### [31:48 - 31:50]

what we'll do is we'll construct our two systems. be stable and we'll also

### [31:50 - 31:50]

systems. be stable and we'll also

### [31:50 - 31:51]

systems. be stable and we'll also construct them and this is sort of

### [31:51 - 31:51]

construct them and this is sort of

### [31:51 - 31:53]

construct them and this is sort of related to ash's noise point to ensure

### [31:53 - 31:53]

related to ash's noise point to ensure

### [31:53 - 31:55]

related to ash's noise point to ensure that basically the span of the the the

### [31:55 - 31:55]

that basically the span of the the the

### [31:55 - 31:57]

that basically the span of the the the second canonical basis vector the E2

### [31:57 - 31:57]

second canonical basis vector the E2

### [31:57 - 32:00]

second canonical basis vector the E2 vector is an invariant subspace of the

### [32:00 - 32:00]

vector is an invariant subspace of the

### [32:00 - 32:02]

vector is an invariant subspace of the closed loop dynamics under both systems.

### [32:02 - 32:02]

closed loop dynamics under both systems.

### [32:02 - 32:04]

closed loop dynamics under both systems. So what this means is that if you roll

### [32:04 - 32:04]

So what this means is that if you roll

### [32:04 - 32:06]

So what this means is that if you roll out the expert policy all the data you

### [32:06 - 32:06]

out the expert policy all the data you

### [32:06 - 32:08]

out the expert policy all the data you ever see is along the vertical axis. You

### [32:08 - 32:08]

ever see is along the vertical axis. You

### [32:08 - 32:12]

ever see is along the vertical axis. You don't see anything on the other axis.

### [32:12 - 32:12]

don't see anything on the other axis.

### [32:12 - 32:14]

don't see anything on the other axis. So in particular, it's going to require

### [32:14 - 32:14]

So in particular, it's going to require

### [32:14 - 32:16]

So in particular, it's going to require basically these systems, these two

### [32:16 - 32:16]

basically these systems, these two

### [32:16 - 32:18]

basically these systems, these two matrices agreeing on this axis so that

### [32:18 - 32:18]

matrices agreeing on this axis so that

### [32:18 - 32:20]

matrices agreeing on this axis so that they're indistinguishable or rather

### [32:20 - 32:20]

they're indistinguishable or rather

### [32:20 - 32:21]

they're indistinguishable or rather we'll enforce that these two systems

### [32:21 - 32:21]

we'll enforce that these two systems

### [32:21 - 32:23]

we'll enforce that these two systems agree on this axis so that they're

### [32:23 - 32:23]

agree on this axis so that they're

### [32:23 - 32:25]

agree on this axis so that they're indistinguishable from this data. What

### [32:25 - 32:25]

indistinguishable from this data. What

### [32:25 - 32:27]

indistinguishable from this data. What this means is that from my expert data

### [32:27 - 32:27]

this means is that from my expert data

### [32:27 - 32:29]

this means is that from my expert data alone I cannot tell which system I'm in

### [32:29 - 32:29]

alone I cannot tell which system I'm in

### [32:29 - 32:32]

alone I cannot tell which system I'm in and I can't identify this index

### [32:32 - 32:32]

and I can't identify this index

### [32:32 - 32:35]

and I can't identify this index I. But now what we're going to show is

### [32:35 - 32:35]

I. But now what we're going to show is

### [32:35 - 32:36]

I. But now what we're going to show is that if we restrict our attention to

### [32:36 - 32:36]

that if we restrict our attention to

### [32:36 - 32:39]

that if we restrict our attention to controllers which agree with the data on

### [32:39 - 32:39]

controllers which agree with the data on

### [32:39 - 32:41]

controllers which agree with the data on the vertical axis which agree with K

### [32:41 - 32:41]

the vertical axis which agree with K

### [32:41 - 32:44]

the vertical axis which agree with K star on E2 these controllers these ones

### [32:44 - 32:44]

star on E2 these controllers these ones

### [32:44 - 32:46]

star on E2 these controllers these ones that agree with the imitation data

### [32:46 - 32:46]

that agree with the imitation data

### [32:46 - 32:48]

that agree with the imitation data necessarily destabilize one system right

### [32:48 - 32:48]

necessarily destabilize one system right

### [32:48 - 32:50]

necessarily destabilize one system right so there will be exist there will exist

### [32:50 - 32:50]

so there will be exist there will exist

### [32:50 - 32:52]

so there will be exist there will exist one system at least where this learn K

### [32:52 - 32:52]

one system at least where this learn K

### [32:52 - 32:55]

one system at least where this learn K controller will have to destabilize it

### [32:55 - 32:55]

controller will have to destabilize it

### [32:55 - 32:56]

controller will have to destabilize it now there might be another system where

### [32:56 - 32:56]

now there might be another system where

### [32:56 - 32:58]

now there might be another system where this stabilizes but at least one will be

### [32:58 - 32:58]

this stabilizes but at least one will be

### [32:58 - 32:59]

this stabilizes but at least one will be destabilizing one way you can think of

### [32:59 - 32:59]

destabilizing one way you can think of

### [32:59 - 33:01]

destabilizing one way you can think of this is you can think that Kstar one

### [33:01 - 33:01]

this is you can think that Kstar one

### [33:01 - 33:03]

this is you can think that Kstar one will destabilize A2 and Kstar 2 will

### [33:03 - 33:03]

will destabilize A2 and Kstar 2 will

### [33:03 - 33:05]

will destabilize A2 and Kstar 2 will destabilize A1. But in fact, in fact,

### [33:05 - 33:06]

destabilize A1. But in fact, in fact,

### [33:06 - 33:07]

destabilize A1. But in fact, in fact, any controller that agrees with both of

### [33:07 - 33:07]

any controller that agrees with both of

### [33:07 - 33:09]

any controller that agrees with both of them on this on the vertical will be

### [33:09 - 33:09]

them on this on the vertical will be

### [33:09 - 33:11]

them on this on the vertical will be destabilizing on the horizontal. Okay?

### [33:11 - 33:11]

destabilizing on the horizontal. Okay?

### [33:11 - 33:12]

destabilizing on the horizontal. Okay? And we can show that there's an example

### [33:12 - 33:12]

And we can show that there's an example

### [33:12 - 33:13]

And we can show that there's an example that just it happens to work that this

### [33:13 - 33:13]

that just it happens to work that this

### [33:13 - 33:14]

that just it happens to work that this is the

### [33:14 - 33:14]

is the

### [33:14 - 33:18]

is the case. Um, and so you can kind of imagine

### [33:18 - 33:18]

case. Um, and so you can kind of imagine

### [33:18 - 33:20]

case. Um, and so you can kind of imagine using this to prove a lower bound. But

### [33:20 - 33:20]

using this to prove a lower bound. But

### [33:20 - 33:22]

using this to prove a lower bound. But unfortunately, linear systems are sort

### [33:22 - 33:22]

unfortunately, linear systems are sort

### [33:22 - 33:23]

unfortunately, linear systems are sort of too all or nothing to prove a lower

### [33:23 - 33:23]

of too all or nothing to prove a lower

### [33:23 - 33:25]

of too all or nothing to prove a lower bound. What I mean by this is that sort

### [33:25 - 33:25]

bound. What I mean by this is that sort

### [33:25 - 33:27]

bound. What I mean by this is that sort of if all of your data was ever on the

### [33:27 - 33:27]

of if all of your data was ever on the

### [33:27 - 33:29]

of if all of your data was ever on the on sort of the vertical axis with linear

### [33:29 - 33:29]

on sort of the vertical axis with linear

### [33:29 - 33:30]

on sort of the vertical axis with linear dynamics and no noise, you could learn

### [33:30 - 33:30]

dynamics and no noise, you could learn

### [33:30 - 33:32]

dynamics and no noise, you could learn things perfectly. So you're never going

### [33:32 - 33:32]

things perfectly. So you're never going

### [33:32 - 33:34]

things perfectly. So you're never going to deviate. So really what you need is

### [33:34 - 33:34]

to deviate. So really what you need is

### [33:34 - 33:35]

to deviate. So really what you need is some kind of sophisticated way of

### [33:35 - 33:35]

some kind of sophisticated way of

### [33:35 - 33:36]

some kind of sophisticated way of embedding this into a nonlinear

### [33:36 - 33:36]

embedding this into a nonlinear

### [33:36 - 33:38]

embedding this into a nonlinear construction. And I'm just going to kind

### [33:38 - 33:38]

construction. And I'm just going to kind

### [33:38 - 33:40]

construction. And I'm just going to kind of really kind of handwavely explain how

### [33:40 - 33:40]

of really kind of handwavely explain how

### [33:40 - 33:42]

of really kind of handwavely explain how this kind of works. So essentially what

### [33:42 - 33:42]

this kind of works. So essentially what

### [33:42 - 33:43]

this kind of works. So essentially what we're going to do is we're going to kind

### [33:43 - 33:43]

we're going to do is we're going to kind

### [33:43 - 33:45]

we're going to do is we're going to kind of use a bump function to embed a

### [33:45 - 33:45]

of use a bump function to embed a

### [33:45 - 33:47]

of use a bump function to embed a nonlinear problem that forces the

### [33:47 - 33:47]

nonlinear problem that forces the

### [33:47 - 33:49]

nonlinear problem that forces the learner to make some mistake that will

### [33:49 - 33:49]

learner to make some mistake that will

### [33:49 - 33:50]

learner to make some mistake that will kind of cascade into the first

### [33:50 - 33:50]

kind of cascade into the first

### [33:50 - 33:53]

kind of cascade into the first horizontal direction. And then from then

### [33:53 - 33:53]

horizontal direction. And then from then

### [33:53 - 33:55]

horizontal direction. And then from then on the problem will look linear. And

### [33:55 - 33:55]

on the problem will look linear. And

### [33:55 - 33:57]

on the problem will look linear. And basically we're going to have learn some

### [33:57 - 33:58]

basically we're going to have learn some

### [33:58 - 34:00]

basically we're going to have learn some sort of nonlinear uh some sort of

### [34:00 - 34:00]

sort of nonlinear uh some sort of

### [34:00 - 34:01]

sort of nonlinear uh some sort of controller that will be forced to

### [34:01 - 34:01]

controller that will be forced to

### [34:01 - 34:03]

controller that will be forced to destabilize along here. What's nice

### [34:03 - 34:03]

destabilize along here. What's nice

### [34:03 - 34:04]

destabilize along here. What's nice about this construction is that it

### [34:04 - 34:04]

about this construction is that it

### [34:04 - 34:06]

about this construction is that it allows you to basically embed arbitrary

### [34:06 - 34:06]

allows you to basically embed arbitrary

### [34:06 - 34:07]

allows you to basically embed arbitrary supervised learning problems into the

### [34:07 - 34:07]

supervised learning problems into the

### [34:07 - 34:09]

supervised learning problems into the bump function which is how we're able to

### [34:09 - 34:09]

bump function which is how we're able to

### [34:09 - 34:11]

bump function which is how we're able to get away with with a result that has a

### [34:11 - 34:11]

get away with with a result that has a

### [34:11 - 34:13]

get away with with a result that has a lower bound for any rate desired rate of

### [34:13 - 34:13]

lower bound for any rate desired rate of

### [34:13 - 34:14]

lower bound for any rate desired rate of estimation under the expert

### [34:14 - 34:14]

estimation under the expert

### [34:14 - 34:16]

estimation under the expert distribution. So we can kind of embed

### [34:16 - 34:16]

distribution. So we can kind of embed

### [34:16 - 34:17]

distribution. So we can kind of embed any nonparametric learning problem over

### [34:17 - 34:18]

any nonparametric learning problem over

### [34:18 - 34:19]

any nonparametric learning problem over here and we get two to the h times the

### [34:19 - 34:19]

here and we get two to the h times the

### [34:19 - 34:21]

here and we get two to the h times the statistical complexity of that problem

### [34:21 - 34:21]

statistical complexity of that problem

### [34:21 - 34:22]

statistical complexity of that problem over here. So it shows that the result

### [34:22 - 34:22]

over here. So it shows that the result

### [34:22 - 34:24]

over here. So it shows that the result is actually kind of a whole template of

### [34:24 - 34:24]

is actually kind of a whole template of

### [34:24 - 34:25]

is actually kind of a whole template of lower bounds rather than a specific

### [34:25 - 34:25]

lower bounds rather than a specific

### [34:25 - 34:29]

lower bounds rather than a specific statistical one. Um one thing um okay

### [34:29 - 34:29]

statistical one. Um one thing um okay

### [34:29 - 34:30]

statistical one. Um one thing um okay this kind of gives you the details of

### [34:30 - 34:30]

this kind of gives you the details of

### [34:30 - 34:32]

this kind of gives you the details of how we kind of finesse it. Uh one thing

### [34:32 - 34:32]

how we kind of finesse it. Uh one thing

### [34:32 - 34:33]

how we kind of finesse it. Uh one thing I should

### [34:33 - 34:33]

I should

### [34:33 - 34:36]

I should mention though is where the simple

### [34:36 - 34:36]

mention though is where the simple

### [34:36 - 34:39]

mention though is where the simple policies come in right and what what

### [34:39 - 34:39]

policies come in right and what what

### [34:39 - 34:40]

policies come in right and what what actually is kind of required is that a

### [34:40 - 34:40]

actually is kind of required is that a

### [34:40 - 34:42]

actually is kind of required is that a simple policy is basically one which is

### [34:42 - 34:42]

simple policy is basically one which is

### [34:42 - 34:44]

simple policy is basically one which is locally linearizable. Right? By being

### [34:44 - 34:44]

locally linearizable. Right? By being

### [34:44 - 34:45]

locally linearizable. Right? By being smooth with state independent noise, we

### [34:45 - 34:45]

smooth with state independent noise, we

### [34:45 - 34:47]

smooth with state independent noise, we can actually tailor expand these

### [34:47 - 34:47]

can actually tailor expand these

### [34:47 - 34:49]

can actually tailor expand these policies and that allows us to relate

### [34:49 - 34:49]

policies and that allows us to relate

### [34:49 - 34:51]

policies and that allows us to relate the behavior of this simple policy to a

### [34:51 - 34:51]

the behavior of this simple policy to a

### [34:51 - 34:53]

the behavior of this simple policy to a policy which basically behaves like a

### [34:53 - 34:53]

policy which basically behaves like a

### [34:53 - 34:55]

policy which basically behaves like a locally linear controller which allows

### [34:55 - 34:55]

locally linear controller which allows

### [34:55 - 34:57]

locally linear controller which allows us to invoke this linear this lower

### [34:57 - 34:57]

us to invoke this linear this lower

### [34:57 - 34:58]

us to invoke this linear this lower bound. Uh things are a little bit more a

### [34:58 - 34:58]

bound. Uh things are a little bit more a

### [34:58 - 35:00]

bound. Uh things are a little bit more a little bit more subtle than that and you

### [35:00 - 35:00]

little bit more subtle than that and you

### [35:00 - 35:01]

little bit more subtle than that and you actually have to use some some work from

### [35:01 - 35:01]

actually have to use some some work from

### [35:01 - 35:02]

actually have to use some some work from the unstable manifold theorem. But

### [35:02 - 35:02]

the unstable manifold theorem. But

### [35:02 - 35:03]

the unstable manifold theorem. But that's kind of the intuition that you

### [35:03 - 35:03]

that's kind of the intuition that you

### [35:03 - 35:04]

that's kind of the intuition that you should have is that if you're only using

### [35:04 - 35:04]

should have is that if you're only using

### [35:04 - 35:06]

should have is that if you're only using simple policies, you're you're kind of

### [35:06 - 35:06]

simple policies, you're you're kind of

### [35:06 - 35:08]

simple policies, you're you're kind of in a regime where you can only locally

### [35:08 - 35:08]

in a regime where you can only locally

### [35:08 - 35:09]

in a regime where you can only locally do as well as the best linear

### [35:09 - 35:09]

do as well as the best linear

### [35:09 - 35:10]

do as well as the best linear controller. And this is going to kind of

### [35:10 - 35:10]

controller. And this is going to kind of

### [35:10 - 35:13]

controller. And this is going to kind of get you stuck.

### [35:13 - 35:13]

get you stuck.

### [35:13 - 35:15]

get you stuck. So kind of maybe what's the core insight

### [35:15 - 35:15]

So kind of maybe what's the core insight

### [35:15 - 35:16]

So kind of maybe what's the core insight then? The core insight is actually that

### [35:16 - 35:16]

then? The core insight is actually that

### [35:16 - 35:19]

then? The core insight is actually that we we've seen control a tension a

### [35:19 - 35:19]

we we've seen control a tension a

### [35:19 - 35:20]

we we've seen control a tension a fundamental tension between being

### [35:20 - 35:20]

fundamental tension between being

### [35:20 - 35:22]

fundamental tension between being faithful to the expert right having to

### [35:22 - 35:22]

faithful to the expert right having to

### [35:22 - 35:25]

faithful to the expert right having to agree with the expert along this axis

### [35:25 - 35:25]

agree with the expert along this axis

### [35:25 - 35:27]

agree with the expert along this axis and stabilization of the unseen

### [35:27 - 35:27]

and stabilization of the unseen

### [35:27 - 35:29]

and stabilization of the unseen dynamical modes being able to stabilize

### [35:29 - 35:29]

dynamical modes being able to stabilize

### [35:29 - 35:31]

dynamical modes being able to stabilize what we don't see. And somehow what this

### [35:31 - 35:31]

what we don't see. And somehow what this

### [35:31 - 35:32]

what we don't see. And somehow what this shows is that unless we're able to use

### [35:32 - 35:32]

shows is that unless we're able to use

### [35:32 - 35:34]

shows is that unless we're able to use sort of policies that cannot be tailor

### [35:34 - 35:34]

sort of policies that cannot be tailor

### [35:34 - 35:36]

sort of policies that cannot be tailor expanded we're not able to resolve this

### [35:36 - 35:36]

expanded we're not able to resolve this

### [35:36 - 35:38]

expanded we're not able to resolve this tension appropriately. And that's kind

### [35:38 - 35:38]

tension appropriately. And that's kind

### [35:38 - 35:39]

tension appropriately. And that's kind of the core insight from the from the

### [35:39 - 35:39]

of the core insight from the from the

### [35:39 - 35:42]

of the core insight from the from the from the finding. Um, this is the RL

### [35:42 - 35:42]

from the finding. Um, this is the RL

### [35:42 - 35:43]

from the finding. Um, this is the RL theory seminar and I've talked a lot

### [35:43 - 35:44]

theory seminar and I've talked a lot

### [35:44 - 35:45]

theory seminar and I've talked a lot about stability, but I feel like it's

### [35:45 - 35:45]

about stability, but I feel like it's

### [35:45 - 35:46]

about stability, but I feel like it's time for me to talk a little bit about Q

### [35:46 - 35:46]

time for me to talk a little bit about Q

### [35:46 - 35:48]

time for me to talk a little bit about Q functions and to connect how stability

### [35:48 - 35:48]

functions and to connect how stability

### [35:48 - 35:50]

functions and to connect how stability that how I think of stability relating

### [35:50 - 35:50]

that how I think of stability relating

### [35:50 - 35:52]

that how I think of stability relating to kind of dynamic programming and other

### [35:52 - 35:52]

to kind of dynamic programming and other

### [35:52 - 35:54]

to kind of dynamic programming and other tools that you might have seen. So the Q

### [35:54 - 35:54]

tools that you might have seen. So the Q

### [35:54 - 35:57]

tools that you might have seen. So the Q function in deterministic control uh

### [35:57 - 35:57]

function in deterministic control uh

### [35:57 - 35:59]

function in deterministic control uh this is review for everybody but like at

### [35:59 - 35:59]

this is review for everybody but like at

### [35:59 - 36:00]

this is review for everybody but like at least in this audience but let me just

### [36:00 - 36:00]

least in this audience but let me just

### [36:00 - 36:02]

least in this audience but let me just kind of say it right. Right? So in a

### [36:02 - 36:02]

kind of say it right. Right? So in a

### [36:02 - 36:03]

kind of say it right. Right? So in a deterministic control system, you can

### [36:03 - 36:03]

deterministic control system, you can

### [36:03 - 36:05]

deterministic control system, you can just write the Q function as the cost to

### [36:05 - 36:05]

just write the Q function as the cost to

### [36:05 - 36:07]

just write the Q function as the cost to go under the dynamics and policy. Again,

### [36:07 - 36:07]

go under the dynamics and policy. Again,

### [36:07 - 36:10]

go under the dynamics and policy. Again, deterministic policy starting at your

### [36:10 - 36:10]

deterministic policy starting at your

### [36:10 - 36:11]

deterministic policy starting at your given state and your given input. Again,

### [36:11 - 36:11]

given state and your given input. Again,

### [36:11 - 36:13]

given state and your given input. Again, I'll be quick because this is RL theory.

### [36:13 - 36:13]

I'll be quick because this is RL theory.

### [36:13 - 36:16]

I'll be quick because this is RL theory. So here's cost to go.

### [36:16 - 36:16]

So here's cost to go.

### [36:16 - 36:17]

So here's cost to go. So we all know the performance

### [36:17 - 36:17]

So we all know the performance

### [36:17 - 36:18]

So we all know the performance difference LMA at least I think the

### [36:18 - 36:18]

difference LMA at least I think the

### [36:18 - 36:20]

difference LMA at least I think the audience here knows it which basically

### [36:20 - 36:20]

audience here knows it which basically

### [36:20 - 36:22]

audience here knows it which basically allows you to use telescoping to uh to

### [36:22 - 36:22]

allows you to use telescoping to uh to

### [36:22 - 36:24]

allows you to use telescoping to uh to represent the kind of difference between

### [36:24 - 36:24]

represent the kind of difference between

### [36:24 - 36:27]

represent the kind of difference between costs under an expert policy and a learn

### [36:27 - 36:27]

costs under an expert policy and a learn

### [36:27 - 36:30]

costs under an expert policy and a learn policy by looking at the differences

### [36:30 - 36:30]

policy by looking at the differences

### [36:30 - 36:32]

policy by looking at the differences between Q functions where what you do is

### [36:32 - 36:32]

between Q functions where what you do is

### [36:32 - 36:34]

between Q functions where what you do is you look at the expectation of the Q

### [36:34 - 36:34]

you look at the expectation of the Q

### [36:34 - 36:36]

you look at the expectation of the Q function under the expert. You look at

### [36:36 - 36:36]

function under the expert. You look at

### [36:36 - 36:38]

function under the expert. You look at the Q functions that are induced by the

### [36:38 - 36:38]

the Q functions that are induced by the

### [36:38 - 36:40]

the Q functions that are induced by the learner and you look at how these Q

### [36:40 - 36:40]

learner and you look at how these Q

### [36:40 - 36:42]

learner and you look at how these Q functions differ if you chose the action

### [36:42 - 36:42]

functions differ if you chose the action

### [36:42 - 36:43]

functions differ if you chose the action that would be prescribed by your

### [36:43 - 36:43]

that would be prescribed by your

### [36:43 - 36:45]

that would be prescribed by your imitator versus the action that would be

### [36:45 - 36:45]

imitator versus the action that would be

### [36:45 - 36:47]

imitator versus the action that would be prescribed by the expert and you look at

### [36:47 - 36:48]

prescribed by the expert and you look at

### [36:48 - 36:49]

prescribed by the expert and you look at basically the difference between these Q

### [36:49 - 36:49]

basically the difference between these Q

### [36:49 - 36:50]

basically the difference between these Q functions and and under the expert

### [36:50 - 36:50]

functions and and under the expert

### [36:50 - 36:52]

functions and and under the expert distribution and this is an alternative

### [36:52 - 36:52]

distribution and this is an alternative

### [36:52 - 36:55]

distribution and this is an alternative way to evaluate the difference in

### [36:55 - 36:55]

way to evaluate the difference in

### [36:55 - 36:58]

way to evaluate the difference in performance. So what's quite nice again

### [36:58 - 36:58]

performance. So what's quite nice again

### [36:58 - 36:59]

performance. So what's quite nice again this is policy the expert learner policy

### [36:59 - 36:59]

this is policy the expert learner policy

### [36:59 - 37:02]

this is policy the expert learner policy the expert. So what's quite nice about

### [37:02 - 37:02]

the expert. So what's quite nice about

### [37:02 - 37:03]

the expert. So what's quite nice about the performance difference perspective

### [37:03 - 37:03]

the performance difference perspective

### [37:03 - 37:05]

the performance difference perspective is it lets you talk about how easy

### [37:05 - 37:05]

is it lets you talk about how easy

### [37:05 - 37:07]

is it lets you talk about how easy imitation learning is in terms of the

### [37:07 - 37:07]

imitation learning is in terms of the

### [37:07 - 37:09]

imitation learning is in terms of the expert distribution by reasoning about

### [37:09 - 37:09]

expert distribution by reasoning about

### [37:09 - 37:11]

expert distribution by reasoning about the regularity properties of the Q

### [37:11 - 37:11]

the regularity properties of the Q

### [37:11 - 37:13]

the regularity properties of the Q function of the learner. So I'll give

### [37:13 - 37:13]

function of the learner. So I'll give

### [37:13 - 37:14]

function of the learner. So I'll give you an example of this. If the Q

### [37:14 - 37:14]

you an example of this. If the Q

### [37:14 - 37:16]

you an example of this. If the Q functions are lip shits then you can

### [37:16 - 37:16]

functions are lip shits then you can

### [37:16 - 37:18]

functions are lip shits then you can upperbound these differences by the

### [37:18 - 37:18]

upperbound these differences by the

### [37:18 - 37:20]

upperbound these differences by the distance between pi hat and pi star.

### [37:20 - 37:20]

distance between pi hat and pi star.

### [37:20 - 37:22]

distance between pi hat and pi star. Right? Right? So if Q is lipids as a

### [37:22 - 37:22]

Right? Right? So if Q is lipids as a

### [37:22 - 37:23]

Right? Right? So if Q is lipids as a function of U, you can upper bound

### [37:23 - 37:23]

function of U, you can upper bound

### [37:23 - 37:25]

function of U, you can upper bound these. And in particular, what this

### [37:25 - 37:25]

these. And in particular, what this

### [37:25 - 37:28]

these. And in particular, what this means is that the cost imitation cost is

### [37:28 - 37:28]

means is that the cost imitation cost is

### [37:28 - 37:30]

means is that the cost imitation cost is upperbounded by Lipshit's constant times

### [37:30 - 37:30]

upperbounded by Lipshit's constant times

### [37:30 - 37:31]

upperbounded by Lipshit's constant times the cumulative norm difference between

### [37:31 - 37:32]

the cumulative norm difference between

### [37:32 - 37:35]

the cumulative norm difference between pi star and pi hat. Right? So what this

### [37:35 - 37:35]

pi star and pi hat. Right? So what this

### [37:35 - 37:37]

pi star and pi hat. Right? So what this would suggest therefore is that if you

### [37:37 - 37:37]

would suggest therefore is that if you

### [37:37 - 37:39]

would suggest therefore is that if you have lipids key functions, you don't

### [37:39 - 37:39]

have lipids key functions, you don't

### [37:39 - 37:41]

have lipids key functions, you don't have compounding error. You don't need

### [37:41 - 37:41]

have compounding error. You don't need

### [37:41 - 37:42]

have compounding error. You don't need compounding error. Uh you you don't

### [37:42 - 37:42]

compounding error. Uh you you don't

### [37:42 - 37:44]

compounding error. Uh you you don't encounter this.

### [37:44 - 37:44]

encounter this.

### [37:44 - 37:46]

encounter this. So and there's actually some wonderful

### [37:46 - 37:46]

So and there's actually some wonderful

### [37:46 - 37:47]

So and there's actually some wonderful work by Gokul Swami and his

### [37:47 - 37:47]

work by Gokul Swami and his

### [37:47 - 37:48]

work by Gokul Swami and his collaborators that kind of generalize

### [37:48 - 37:48]

collaborators that kind of generalize

### [37:48 - 37:50]

collaborators that kind of generalize this in terms of in terms of sort of

### [37:50 - 37:50]

this in terms of in terms of sort of

### [37:50 - 37:52]

this in terms of in terms of sort of integral probability metrics where they

### [37:52 - 37:52]

integral probability metrics where they

### [37:52 - 37:53]

integral probability metrics where they kind of relate sort of notions of

### [37:53 - 37:53]

kind of relate sort of notions of

### [37:53 - 37:56]

kind of relate sort of notions of unexpert imitation to properties of the

### [37:56 - 37:56]

unexpert imitation to properties of the

### [37:56 - 37:57]

unexpert imitation to properties of the Q function

### [37:57 - 37:57]

Q function

### [37:57 - 38:00]

Q function class. So in particular low compounding

### [38:00 - 38:00]

class. So in particular low compounding

### [38:00 - 38:02]

class. So in particular low compounding error is guaranteed by insensitive Q

### [38:02 - 38:02]

error is guaranteed by insensitive Q

### [38:02 - 38:04]

error is guaranteed by insensitive Q functions and large compounding error

### [38:04 - 38:04]

functions and large compounding error

### [38:04 - 38:07]

functions and large compounding error requires highly sensitive Q functions.

### [38:07 - 38:07]

requires highly sensitive Q functions.

### [38:07 - 38:08]

requires highly sensitive Q functions. So maybe one way to reinterpret our

### [38:08 - 38:08]

So maybe one way to reinterpret our

### [38:08 - 38:11]

So maybe one way to reinterpret our result is to say the following. If even

### [38:11 - 38:11]

result is to say the following. If even

### [38:11 - 38:12]

result is to say the following. If even if we're in situations where the

### [38:12 - 38:12]

if we're in situations where the

### [38:12 - 38:14]

if we're in situations where the dynamics are both openly and closed loop

### [38:14 - 38:14]

dynamics are both openly and closed loop

### [38:14 - 38:17]

dynamics are both openly and closed loop stable, it is both hard to imitate the

### [38:17 - 38:17]

stable, it is both hard to imitate the

### [38:17 - 38:19]

stable, it is both hard to imitate the expert and to learn a Q function that is

### [38:19 - 38:19]

expert and to learn a Q function that is

### [38:19 - 38:22]

expert and to learn a Q function that is lipchits and to learn a pi hat which

### [38:22 - 38:22]

lipchits and to learn a pi hat which

### [38:22 - 38:23]

lipchits and to learn a pi hat which ensures that you get lipits q functions

### [38:23 - 38:23]

ensures that you get lipits q functions

### [38:23 - 38:25]

ensures that you get lipits q functions with your with uh in closed loop with

### [38:25 - 38:25]

with your with uh in closed loop with

### [38:25 - 38:27]

with your with uh in closed loop with the dynamics and I think this is kind of

### [38:27 - 38:27]

the dynamics and I think this is kind of

### [38:27 - 38:30]

the dynamics and I think this is kind of an interesting message uh for us as RL

### [38:30 - 38:30]

an interesting message uh for us as RL

### [38:30 - 38:32]

an interesting message uh for us as RL theorists where we're very naturally

### [38:32 - 38:32]

theorists where we're very naturally

### [38:32 - 38:34]

theorists where we're very naturally inclined to make assumptions directly on

### [38:34 - 38:34]

inclined to make assumptions directly on

### [38:34 - 38:35]

inclined to make assumptions directly on the Q function class. So statistical

### [38:35 - 38:36]

the Q function class. So statistical

### [38:36 - 38:37]

the Q function class. So statistical complexity of the Q functions,

### [38:37 - 38:37]

complexity of the Q functions,

### [38:37 - 38:38]

complexity of the Q functions, realizability, maybe smoothness

### [38:38 - 38:38]

realizability, maybe smoothness

### [38:38 - 38:40]

realizability, maybe smoothness assumptions. But this actually says that

### [38:40 - 38:40]

assumptions. But this actually says that

### [38:40 - 38:41]

assumptions. But this actually says that if you think about systems from a

### [38:41 - 38:41]

if you think about systems from a

### [38:41 - 38:43]

if you think about systems from a dynamical point of view, you should

### [38:43 - 38:43]

dynamical point of view, you should

### [38:43 - 38:44]

dynamical point of view, you should actually think about letting assumptions

### [38:44 - 38:44]

actually think about letting assumptions

### [38:44 - 38:46]

actually think about letting assumptions in the Q functions emerge from the

### [38:46 - 38:46]

in the Q functions emerge from the

### [38:46 - 38:48]

in the Q functions emerge from the dynamics rather than imposing those

### [38:48 - 38:48]

dynamics rather than imposing those

### [38:48 - 38:50]

dynamics rather than imposing those assumptions a priority. And indeed, what

### [38:50 - 38:50]

assumptions a priority. And indeed, what

### [38:50 - 38:52]

assumptions a priority. And indeed, what your Q function class should actually

### [38:52 - 38:52]

your Q function class should actually

### [38:52 - 38:54]

your Q function class should actually look like might be something that's far

### [38:54 - 38:54]

look like might be something that's far

### [38:54 - 38:55]

look like might be something that's far less regular than you might want. But

### [38:55 - 38:55]

less regular than you might want. But

### [38:55 - 38:57]

less regular than you might want. But this might be absolutely unavoidable

### [38:57 - 38:57]

this might be absolutely unavoidable

### [38:57 - 38:59]

this might be absolutely unavoidable even if the dynamics are nice and even

### [38:59 - 38:59]

even if the dynamics are nice and even

### [38:59 - 39:00]

even if the dynamics are nice and even if your learn policy is in some

### [39:00 - 39:00]

if your learn policy is in some

### [39:00 - 39:02]

if your learn policy is in some reasonable class. I think that's that's

### [39:02 - 39:02]

reasonable class. I think that's that's

### [39:02 - 39:04]

reasonable class. I think that's that's I think this is something that really I

### [39:04 - 39:04]

I think this is something that really I

### [39:04 - 39:06]

I think this is something that really I I I didn't really fully appreciate until

### [39:06 - 39:06]

I I didn't really fully appreciate until

### [39:06 - 39:08]

I I didn't really fully appreciate until I until I until I started thinking about

### [39:08 - 39:08]

I until I until I started thinking about

### [39:08 - 39:09]

I until I until I started thinking about the control setting. We also have some

### [39:09 - 39:09]

the control setting. We also have some

### [39:09 - 39:11]

the control setting. We also have some upcoming work that we submitted to CDC

### [39:11 - 39:11]

upcoming work that we submitted to CDC

### [39:11 - 39:13]

upcoming work that we submitted to CDC that will that that that um we're

### [39:13 - 39:13]

that will that that that um we're

### [39:13 - 39:15]

that will that that that um we're excited to share where we actually show

### [39:15 - 39:15]

excited to share where we actually show

### [39:15 - 39:17]

excited to share where we actually show some interesting equivalences between um

### [39:17 - 39:17]

some interesting equivalences between um

### [39:17 - 39:19]

some interesting equivalences between um oh yes Naan has got a question which I

### [39:19 - 39:19]

oh yes Naan has got a question which I

### [39:19 - 39:21]

oh yes Naan has got a question which I definitely want to answer. Naan yeah so

### [39:21 - 39:21]

definitely want to answer. Naan yeah so

### [39:21 - 39:25]

definitely want to answer. Naan yeah so uh so for this case um if if you examine

### [39:25 - 39:25]

uh so for this case um if if you examine

### [39:25 - 39:29]

uh so for this case um if if you examine the Q functions um in your lower bound

### [39:29 - 39:29]

the Q functions um in your lower bound

### [39:29 - 39:32]

the Q functions um in your lower bound constructions are they nice and

### [39:32 - 39:32]

constructions are they nice and

### [39:32 - 39:34]

constructions are they nice and luxurious for the they have to for the

### [39:34 - 39:34]

luxurious for the they have to for the

### [39:34 - 39:36]

luxurious for the they have to for the expert policy for the expert policy for

### [39:36 - 39:36]

expert policy for the expert policy for

### [39:36 - 39:38]

expert policy for the expert policy for the expert policy they are. Yes. So for

### [39:38 - 39:38]

the expert policy they are. Yes. So for

### [39:38 - 39:39]

the expert policy they are. Yes. So for the expert policy they will be because

### [39:39 - 39:39]

the expert policy they will be because

### [39:39 - 39:41]

the expert policy they will be because the expert policy is in exponentially

### [39:41 - 39:41]

the expert policy is in exponentially

### [39:41 - 39:43]

the expert policy is in exponentially stable which will mean that the Q

### [39:43 - 39:43]

stable which will mean that the Q

### [39:43 - 39:44]

stable which will mean that the Q function is going to be is going to be

### [39:44 - 39:44]

function is going to be is going to be

### [39:44 - 39:47]

function is going to be is going to be lejits. Yeah. So then regarding messages

### [39:47 - 39:47]

lejits. Yeah. So then regarding messages

### [39:47 - 39:50]

lejits. Yeah. So then regarding messages I wonder if uh there's an uh opposite

### [39:50 - 39:50]

I wonder if uh there's an uh opposite

### [39:50 - 39:52]

I wonder if uh there's an uh opposite interpretation that is if you take the

### [39:52 - 39:52]

interpretation that is if you take the

### [39:52 - 39:54]

interpretation that is if you take the approach of like learning Q functions

### [39:54 - 39:54]

approach of like learning Q functions

### [39:54 - 39:57]

approach of like learning Q functions and you learn Q functions from a sort of

### [39:57 - 39:57]

and you learn Q functions from a sort of

### [39:57 - 40:00]

and you learn Q functions from a sort of uh you know smooth ellipticious and nice

### [40:00 - 40:00]

uh you know smooth ellipticious and nice

### [40:00 - 40:03]

uh you know smooth ellipticious and nice structure does that somehow maybe help

### [40:03 - 40:03]

structure does that somehow maybe help

### [40:03 - 40:06]

structure does that somehow maybe help you enforce you to slap onto the expert

### [40:06 - 40:06]

you enforce you to slap onto the expert

### [40:06 - 40:08]

you enforce you to slap onto the expert Q function? can't. No, it can't because

### [40:08 - 40:08]

Q function? can't. No, it can't because

### [40:08 - 40:10]

Q function? can't. No, it can't because because the the point is that our lower

### [40:10 - 40:10]

because the the point is that our lower

### [40:10 - 40:11]

because the the point is that our lower bound actually shows you can't even

### [40:11 - 40:11]

bound actually shows you can't even

### [40:11 - 40:14]

bound actually shows you can't even learn a stabilizing policy and if you if

### [40:14 - 40:14]

learn a stabilizing policy and if you if

### [40:14 - 40:15]

learn a stabilizing policy and if you if so if you could learn a policy which

### [40:15 - 40:16]

so if you could learn a policy which

### [40:16 - 40:18]

so if you could learn a policy which ensured that you had a lip Q function

### [40:18 - 40:18]

ensured that you had a lip Q function

### [40:18 - 40:20]

ensured that you had a lip Q function that would necessarily mean pihat is

### [40:20 - 40:20]

that would necessarily mean pihat is

### [40:20 - 40:23]

that would necessarily mean pihat is stabilizing but the point is that you

### [40:23 - 40:23]

stabilizing but the point is that you

### [40:23 - 40:24]

stabilizing but the point is that you cannot learn at least when you restrict

### [40:24 - 40:24]

cannot learn at least when you restrict

### [40:24 - 40:26]

cannot learn at least when you restrict to simple policies you cannot learn a

### [40:26 - 40:26]

to simple policies you cannot learn a

### [40:26 - 40:28]

to simple policies you cannot learn a stabilizing policy which means that it's

### [40:28 - 40:28]

stabilizing policy which means that it's

### [40:28 - 40:30]

stabilizing policy which means that it's impossible to learn a policy that gives

### [40:30 - 40:30]

impossible to learn a policy that gives

### [40:30 - 40:33]

impossible to learn a policy that gives you a lipids q function stated otherwise

### [40:33 - 40:33]

you a lipids q function stated otherwise

### [40:33 - 40:34]

you a lipids q function stated otherwise our lower bound is agnostic to the

### [40:34 - 40:34]

our lower bound is agnostic to the

### [40:34 - 40:36]

our lower bound is agnostic to the algorithm so there's really nothing you

### [40:36 - 40:36]

algorithm so there's really nothing you

### [40:36 - 40:39]

algorithm so there's really nothing you can do on the algorithmic side. In fact,

### [40:39 - 40:39]

can do on the algorithmic side. In fact,

### [40:39 - 40:41]

can do on the algorithmic side. In fact, yeah, I know that that lower bound is

### [40:41 - 40:41]

yeah, I know that that lower bound is

### [40:41 - 40:44]

yeah, I know that that lower bound is Yeah. Yeah. I I guess I'm I'm like my

### [40:44 - 40:44]

Yeah. Yeah. I I guess I'm I'm like my

### [40:44 - 40:47]

Yeah. Yeah. I I guess I'm I'm like my last question is like more general like

### [40:47 - 40:47]

last question is like more general like

### [40:47 - 40:49]

last question is like more general like because that lower bound really says

### [40:49 - 40:49]

because that lower bound really says

### [40:49 - 40:50]

because that lower bound really says that it you necessarily needs to change

### [40:50 - 40:50]

that it you necessarily needs to change

### [40:50 - 40:52]

that it you necessarily needs to change your policy class, right? I think that

### [40:52 - 40:52]

your policy class, right? I think that

### [40:52 - 40:54]

your policy class, right? I think that so the question I'm saying like more

### [40:54 - 40:54]

so the question I'm saying like more

### [40:54 - 40:56]

so the question I'm saying like more generally like could you use could you

### [40:56 - 40:56]

generally like could you use could you

### [40:56 - 40:58]

generally like could you use could you try to use the Q function to do this?

### [40:58 - 40:58]

try to use the Q function to do this?

### [40:58 - 41:01]

try to use the Q function to do this? Yeah. Um I think it's it's certainly

### [41:01 - 41:01]

Yeah. Um I think it's it's certainly

### [41:01 - 41:03]

Yeah. Um I think it's it's certainly it's certainly possible that you could I

### [41:03 - 41:03]

it's certainly possible that you could I

### [41:03 - 41:05]

it's certainly possible that you could I think people have tried to do this.

### [41:05 - 41:05]

think people have tried to do this.

### [41:05 - 41:06]

think people have tried to do this. There there's some I think some work

### [41:06 - 41:06]

There there's some I think some work

### [41:06 - 41:07]

There there's some I think some work from Steven 2 from a few years ago that

### [41:07 - 41:07]

from Steven 2 from a few years ago that

### [41:07 - 41:09]

from Steven 2 from a few years ago that tried to explicitly enforce stability

### [41:09 - 41:09]

tried to explicitly enforce stability

### [41:09 - 41:10]

tried to explicitly enforce stability which is equivalent to enforcing

### [41:10 - 41:10]

which is equivalent to enforcing

### [41:10 - 41:14]

which is equivalent to enforcing lipidness of the Q function. Um but it

### [41:14 - 41:14]

lipidness of the Q function. Um but it

### [41:14 - 41:15]

lipidness of the Q function. Um but it actually turns out that the better thing

### [41:15 - 41:15]

actually turns out that the better thing

### [41:15 - 41:16]

actually turns out that the better thing to do is just to make sure that you have

### [41:16 - 41:16]

to do is just to make sure that you have

### [41:16 - 41:18]

to do is just to make sure that you have enough that you collect a little bit

### [41:18 - 41:18]

enough that you collect a little bit

### [41:18 - 41:20]

enough that you collect a little bit more online data or you use a slightly

### [41:20 - 41:20]

more online data or you use a slightly

### [41:20 - 41:21]

more online data or you use a slightly better expert to collect data. Yeah. and

### [41:21 - 41:21]

better expert to collect data. Yeah. and

### [41:21 - 41:22]

better expert to collect data. Yeah. and working through the through the Q

### [41:22 - 41:22]

working through the through the Q

### [41:22 - 41:24]

working through the through the Q function class. Presumably, if you were

### [41:24 - 41:24]

function class. Presumably, if you were

### [41:24 - 41:25]

function class. Presumably, if you were in a setting where you had like really

### [41:25 - 41:26]

in a setting where you had like really

### [41:26 - 41:28]

in a setting where you had like really good notions of like world models, you

### [41:28 - 41:28]

good notions of like world models, you

### [41:28 - 41:29]

good notions of like world models, you for example, if you had really good

### [41:29 - 41:29]

for example, if you had really good

### [41:29 - 41:31]

for example, if you had really good world models, you could try to enforce

### [41:31 - 41:31]

world models, you could try to enforce

### [41:31 - 41:33]

world models, you could try to enforce stability of lipidness of the Q function

### [41:33 - 41:33]

stability of lipidness of the Q function

### [41:33 - 41:35]

stability of lipidness of the Q function as an algorithmic tool. You could also

### [41:35 - 41:35]

as an algorithmic tool. You could also

### [41:35 - 41:37]

as an algorithmic tool. You could also try to just enforce stability of the

### [41:37 - 41:37]

try to just enforce stability of the

### [41:37 - 41:38]

try to just enforce stability of the dynamics. These two are kind of

### [41:38 - 41:38]

dynamics. These two are kind of

### [41:38 - 41:39]

dynamics. These two are kind of essentially in our in our follow-up

### [41:39 - 41:39]

essentially in our in our follow-up

### [41:39 - 41:40]

essentially in our in our follow-up paper, we're showing that these are dual

### [41:40 - 41:40]

paper, we're showing that these are dual

### [41:40 - 41:42]

paper, we're showing that these are dual to one another. So any algorithmic thing

### [41:42 - 41:42]

to one another. So any algorithmic thing

### [41:42 - 41:44]

to one another. So any algorithmic thing that tries to pre-p prune Q functions is

### [41:44 - 41:44]

that tries to pre-p prune Q functions is

### [41:44 - 41:45]

that tries to pre-p prune Q functions is basically the same thing as any

### [41:45 - 41:45]

basically the same thing as any

### [41:45 - 41:46]

basically the same thing as any algorithmic thing that tries to afford

### [41:46 - 41:46]

algorithmic thing that tries to afford

### [41:46 - 41:48]

algorithmic thing that tries to afford dynamic stability.

### [41:48 - 41:48]

dynamic stability.

### [41:48 - 41:49]

dynamic stability. um it's basically like an IPM

### [41:49 - 41:49]

um it's basically like an IPM

### [41:49 - 41:51]

um it's basically like an IPM characterization of stability rather

### [41:51 - 41:51]

characterization of stability rather

### [41:51 - 41:53]

characterization of stability rather than than of optimality in terms of Q

### [41:53 - 41:53]

than than of optimality in terms of Q

### [41:53 - 41:55]

than than of optimality in terms of Q functions. Um so but yeah I think it

### [41:55 - 41:55]

functions. Um so but yeah I think it

### [41:55 - 41:56]

functions. Um so but yeah I think it would be an exciting it would be

### [41:56 - 41:56]

would be an exciting it would be

### [41:56 - 41:58]

would be an exciting it would be exciting to see how to do that but from

### [41:58 - 41:58]

exciting to see how to do that but from

### [41:58 - 42:00]

exciting to see how to do that but from what my understanding at least empirical

### [42:00 - 42:00]

what my understanding at least empirical

### [42:00 - 42:02]

what my understanding at least empirical attempts to to to do stability

### [42:02 - 42:02]

attempts to to to do stability

### [42:02 - 42:05]

attempts to to to do stability constraints uh have been quite difficult

### [42:05 - 42:05]

constraints uh have been quite difficult

### [42:05 - 42:07]

constraints uh have been quite difficult and that suggests that maybe lipits

### [42:07 - 42:07]

and that suggests that maybe lipits

### [42:07 - 42:08]

and that suggests that maybe lipits constraints in the Q class might also be

### [42:08 - 42:08]

constraints in the Q class might also be

### [42:08 - 42:10]

constraints in the Q class might also be difficult on their own but maybe in

### [42:10 - 42:10]

difficult on their own but maybe in

### [42:10 - 42:11]

difficult on their own but maybe in conjunction with other things they might

### [42:11 - 42:11]

conjunction with other things they might

### [42:11 - 42:14]

conjunction with other things they might be powerful. Cool. Max I have a

### [42:14 - 42:14]

be powerful. Cool. Max I have a

### [42:14 - 42:16]

be powerful. Cool. Max I have a question. Yeah. Um in this setting the

### [42:16 - 42:16]

question. Yeah. Um in this setting the

### [42:16 - 42:18]

question. Yeah. Um in this setting the cost function is known or not known

### [42:18 - 42:18]

cost function is known or not known

### [42:18 - 42:20]

cost function is known or not known known. Oh so yeah so in in the whole in

### [42:20 - 42:20]

known. Oh so yeah so in in the whole in

### [42:20 - 42:21]

known. Oh so yeah so in in the whole in the whole in our whole construction the

### [42:21 - 42:21]

the whole in our whole construction the

### [42:21 - 42:23]

the whole in our whole construction the cost function is known which means that

### [42:23 - 42:23]

cost function is known which means that

### [42:23 - 42:24]

cost function is known which means that we we preclude offline RL which can even

### [42:24 - 42:24]

we we preclude offline RL which can even

### [42:24 - 42:27]

we we preclude offline RL which can even use the cost function. You can't even

### [42:27 - 42:27]

use the cost function. You can't even

### [42:27 - 42:28]

use the cost function. You can't even use the con function to to to beat our

### [42:28 - 42:28]

use the con function to to to beat our

### [42:28 - 42:31]

use the con function to to to beat our lower bound.

### [42:31 - 42:31]

lower bound.

### [42:31 - 42:33]

lower bound. Good. And you get trajectory data from

### [42:33 - 42:33]

Good. And you get trajectory data from

### [42:33 - 42:35]

Good. And you get trajectory data from the expert or do you get like data?

### [42:35 - 42:35]

the expert or do you get like data?

### [42:35 - 42:37]

the expert or do you get like data? Trajectory data.

### [42:37 - 42:37]

Trajectory data.

### [42:37 - 42:41]

Trajectory data. Yeah. Trajectory data. Yeah. Uh okay

### [42:41 - 42:41]

Yeah. Trajectory data. Yeah. Uh okay

### [42:41 - 42:43]

Yeah. Trajectory data. Yeah. Uh okay then maybe I'm surprised because somehow

### [42:43 - 42:43]

then maybe I'm surprised because somehow

### [42:43 - 42:45]

then maybe I'm surprised because somehow you could say let me take a lip shits

### [42:45 - 42:45]

you could say let me take a lip shits

### [42:45 - 42:48]

you could say let me take a lip shits function class and try to regress onto

### [42:48 - 42:48]

function class and try to regress onto

### [42:48 - 42:50]

function class and try to regress onto classes. Yeah. So let me let me maybe

### [42:50 - 42:50]

classes. Yeah. So let me let me maybe

### [42:50 - 42:51]

classes. Yeah. So let me let me maybe say this in a different in a in a

### [42:51 - 42:51]

say this in a different in a in a

### [42:51 - 42:54]

say this in a different in a in a different way. So um you what you're

### [42:54 - 42:54]

different way. So um you what you're

### [42:54 - 42:55]

different way. So um you what you're getting at is something called action I

### [42:55 - 42:56]

getting at is something called action I

### [42:56 - 42:56]

getting at is something called action I think you're getting towards something

### [42:56 - 42:56]

think you're getting towards something

### [42:56 - 42:58]

think you're getting towards something called action chunking which I'll talk

### [42:58 - 42:58]

called action chunking which I'll talk

### [42:58 - 43:00]

called action chunking which I'll talk about in a second. But I should say that

### [43:00 - 43:00]

about in a second. But I should say that

### [43:00 - 43:02]

about in a second. But I should say that one important thing is that basically

### [43:02 - 43:02]

one important thing is that basically

### [43:02 - 43:05]

one important thing is that basically you're not your your set of instances

### [43:05 - 43:05]

you're not your your set of instances

### [43:05 - 43:07]

you're not your your set of instances does not come from the product class of

### [43:07 - 43:07]

does not come from the product class of

### [43:07 - 43:08]

does not come from the product class of of we're getting a little bit into the

### [43:08 - 43:08]

of we're getting a little bit into the

### [43:08 - 43:10]

of we're getting a little bit into the weeds but does not come into the come

### [43:10 - 43:10]

weeds but does not come into the come

### [43:10 - 43:11]

weeds but does not come into the come from the product class of of dynamics

### [43:11 - 43:11]

from the product class of of dynamics

### [43:11 - 43:15]

from the product class of of dynamics and pies right so the point is that like

### [43:15 - 43:15]

and pies right so the point is that like

### [43:15 - 43:18]

and pies right so the point is that like one pi star might not stabilize another

### [43:18 - 43:18]

one pi star might not stabilize another

### [43:18 - 43:21]

one pi star might not stabilize another f and so we're in a regime where there's

### [43:21 - 43:21]

f and so we're in a regime where there's

### [43:21 - 43:23]

f and so we're in a regime where there's not really kind of a clear way to just

### [43:23 - 43:23]

not really kind of a clear way to just

### [43:23 - 43:27]

not really kind of a clear way to just sort of like um ensure that there's some

### [43:27 - 43:27]

sort of like um ensure that there's some

### [43:27 - 43:29]

sort of like um ensure that there's some ground truth set where we could get lip

### [43:29 - 43:29]

ground truth set where we could get lip

### [43:29 - 43:32]

ground truth set where we could get lip shitness or stability from. So I can I

### [43:32 - 43:32]

shitness or stability from. So I can I

### [43:32 - 43:33]

shitness or stability from. So I can I can show you something else that will

### [43:33 - 43:33]

can show you something else that will

### [43:33 - 43:34]

can show you something else that will work and that'll be kind of like the

### [43:34 - 43:34]

work and that'll be kind of like the

### [43:34 - 43:37]

work and that'll be kind of like the last part of the talk. Okay. Um but I I

### [43:37 - 43:37]

last part of the talk. Okay. Um but I I

### [43:37 - 43:39]

last part of the talk. Okay. Um but I I agree that it's kind of hard to regress

### [43:39 - 43:39]

agree that it's kind of hard to regress

### [43:39 - 43:41]

agree that it's kind of hard to regress onto the problem is that you don't know

### [43:41 - 43:41]

onto the problem is that you don't know

### [43:41 - 43:42]

onto the problem is that you don't know the dynamics in the construction and so

### [43:42 - 43:42]

the dynamics in the construction and so

### [43:42 - 43:44]

the dynamics in the construction and so it's hard to reason about what will end

### [43:44 - 43:44]

it's hard to reason about what will end

### [43:44 - 43:46]

it's hard to reason about what will end up being kind of lip shits because that

### [43:46 - 43:46]

up being kind of lip shits because that

### [43:46 - 43:48]

up being kind of lip shits because that requires knowledge of the dynamics and

### [43:48 - 43:48]

requires knowledge of the dynamics and

### [43:48 - 43:50]

requires knowledge of the dynamics and and that's where like online will be

### [43:50 - 43:50]

and that's where like online will be

### [43:50 - 43:52]

and that's where like online will be really useful because then online.

### [43:52 - 43:52]

really useful because then online.

### [43:52 - 43:54]

really useful because then online. Exactly. Yeah. Exactly. or some other

### [43:54 - 43:54]

Exactly. Yeah. Exactly. or some other

### [43:54 - 43:56]

Exactly. Yeah. Exactly. or some other form of additional exploration which is

### [43:56 - 43:56]

form of additional exploration which is

### [43:56 - 43:59]

form of additional exploration which is being discussed in in future work. But a

### [43:59 - 43:59]

being discussed in in future work. But a

### [43:59 - 44:00]

being discussed in in future work. But a sort of crucially the lower bound

### [44:00 - 44:00]

sort of crucially the lower bound

### [44:00 - 44:01]

sort of crucially the lower bound leverages non lack of knowledge of

### [44:01 - 44:02]

leverages non lack of knowledge of

### [44:02 - 44:03]

leverages non lack of knowledge of dynamics. If you did know the dynamics

### [44:03 - 44:03]

dynamics. If you did know the dynamics

### [44:03 - 44:04]

dynamics. If you did know the dynamics then there'd be a computationally

### [44:04 - 44:04]

then there'd be a computationally

### [44:04 - 44:06]

then there'd be a computationally inefficient algorithm which either a

### [44:06 - 44:06]

inefficient algorithm which either a

### [44:06 - 44:08]

inefficient algorithm which either a throws out all unstable policies or b

### [44:08 - 44:08]

throws out all unstable policies or b

### [44:08 - 44:10]

throws out all unstable policies or b throws out all non- lipjits q function

### [44:10 - 44:10]

throws out all non- lipjits q function

### [44:10 - 44:12]

throws out all non- lipjits q function policies with non-litsq functions. But

### [44:12 - 44:12]

policies with non-litsq functions. But

### [44:12 - 44:13]

policies with non-litsq functions. But sort of crucially we don't know the

### [44:13 - 44:13]

sort of crucially we don't know the

### [44:13 - 44:15]

sort of crucially we don't know the dynamics. If we did we would be able to

### [44:15 - 44:15]

dynamics. If we did we would be able to

### [44:15 - 44:16]

dynamics. If we did we would be able to do much better. Yeah I I think okay like

### [44:16 - 44:16]

do much better. Yeah I I think okay like

### [44:16 - 44:18]

do much better. Yeah I I think okay like I I think I'm also saying something

### [44:18 - 44:18]

I I think I'm also saying something

### [44:18 - 44:20]

I I think I'm also saying something slightly wrong. Like if you do like

### [44:20 - 44:20]

slightly wrong. Like if you do like

### [44:20 - 44:21]

slightly wrong. Like if you do like regression to learn a Q function and

### [44:21 - 44:22]

regression to learn a Q function and

### [44:22 - 44:24]

regression to learn a Q function and then derive a policy by like acting

### [44:24 - 44:24]

then derive a policy by like acting

### [44:24 - 44:25]

then derive a policy by like acting greedily according to

### [44:25 - 44:25]

greedily according to

### [44:25 - 44:28]

greedily according to that that policy's Q function is not the

### [44:28 - 44:28]

that that policy's Q function is not the

### [44:28 - 44:30]

that that policy's Q function is not the thing you learned. Exactly. That

### [44:30 - 44:30]

thing you learned. Exactly. That

### [44:30 - 44:32]

thing you learned. Exactly. That policy's Q function might not be lipits

### [44:32 - 44:32]

policy's Q function might not be lipits

### [44:32 - 44:33]

policy's Q function might not be lipits even though the Q function from which

### [44:33 - 44:33]

even though the Q function from which

### [44:33 - 44:34]

even though the Q function from which you're deriving the policy is lift.

### [44:34 - 44:34]

you're deriving the policy is lift.

### [44:34 - 44:37]

you're deriving the policy is lift. Exactly. Exactly. Exactly. Exactly. In

### [44:37 - 44:37]

Exactly. Exactly. Exactly. Exactly. In

### [44:37 - 44:39]

Exactly. Exactly. Exactly. Exactly. In Yeah. Exactly. And so actually and and

### [44:39 - 44:39]

Yeah. Exactly. And so actually and and

### [44:39 - 44:40]

Yeah. Exactly. And so actually and and some followup work actually explaining

### [44:40 - 44:40]

some followup work actually explaining

### [44:40 - 44:42]

some followup work actually explaining exposing like kind of the the the kind

### [44:42 - 44:42]

exposing like kind of the the the kind

### [44:42 - 44:43]

exposing like kind of the the the kind of equivalence between lift and

### [44:43 - 44:43]

of equivalence between lift and

### [44:43 - 44:45]

of equivalence between lift and incremental stability. I want to end the

### [44:45 - 44:45]

incremental stability. I want to end the

### [44:45 - 44:47]

incremental stability. I want to end the talk on this note which is like how

### [44:47 - 44:47]

talk on this note which is like how

### [44:47 - 44:50]

talk on this note which is like how weird continuous action spaces truly are

### [44:50 - 44:50]

weird continuous action spaces truly are

### [44:50 - 44:53]

weird continuous action spaces truly are and the power of non-simple policies in

### [44:53 - 44:53]

and the power of non-simple policies in

### [44:53 - 44:54]

and the power of non-simple policies in continuous action

### [44:54 - 44:54]

continuous action

### [44:54 - 44:56]

continuous action spaces and this will kind of explain

### [44:56 - 44:56]

spaces and this will kind of explain

### [44:56 - 44:58]

spaces and this will kind of explain some things that do work. So one is that

### [44:58 - 44:58]

some things that do work. So one is that

### [44:58 - 45:01]

some things that do work. So one is that we need new notions of coverage. So why

### [45:01 - 45:01]

we need new notions of coverage. So why

### [45:01 - 45:03]

we need new notions of coverage. So why is this? Well, we're doing imitation

### [45:03 - 45:03]

is this? Well, we're doing imitation

### [45:03 - 45:05]

is this? Well, we're doing imitation learning which from a measure theoretic

### [45:05 - 45:05]

learning which from a measure theoretic

### [45:05 - 45:06]

learning which from a measure theoretic standpoint from probability standpoint

### [45:06 - 45:06]

standpoint from probability standpoint

### [45:06 - 45:08]

standpoint from probability standpoint we have perfect coverage. Our our rate

### [45:08 - 45:08]

we have perfect coverage. Our our rate

### [45:08 - 45:09]

we have perfect coverage. Our our rate on negative derivative with respect to

### [45:09 - 45:09]

on negative derivative with respect to

### [45:09 - 45:11]

on negative derivative with respect to the expert is one. Now we don't have all

### [45:11 - 45:12]

the expert is one. Now we don't have all

### [45:12 - 45:13]

the expert is one. Now we don't have all policy coverage. We have perfect expert

### [45:13 - 45:13]

policy coverage. We have perfect expert

### [45:13 - 45:15]

policy coverage. We have perfect expert coverage. But what we're able to show

### [45:15 - 45:15]

coverage. But what we're able to show

### [45:15 - 45:16]

coverage. But what we're able to show even in this paper is that if there's a

### [45:16 - 45:16]

even in this paper is that if there's a

### [45:16 - 45:18]

even in this paper is that if there's a certain notion of anti-conentration

### [45:18 - 45:18]

certain notion of anti-conentration

### [45:18 - 45:19]

certain notion of anti-conentration which is less sort of measure theoretic

### [45:19 - 45:19]

which is less sort of measure theoretic

### [45:19 - 45:22]

which is less sort of measure theoretic and more geometric uh in basically in

### [45:22 - 45:22]

and more geometric uh in basically in

### [45:22 - 45:23]

and more geometric uh in basically in some which basically controls sort of a

### [45:23 - 45:23]

some which basically controls sort of a

### [45:23 - 45:26]

some which basically controls sort of a local variance of of of expert data.

### [45:26 - 45:26]

local variance of of of expert data.

### [45:26 - 45:27]

local variance of of of expert data. Think of this as induced by of

### [45:27 - 45:27]

Think of this as induced by of

### [45:27 - 45:29]

Think of this as induced by of randomness over the initial state

### [45:29 - 45:29]

randomness over the initial state

### [45:29 - 45:31]

randomness over the initial state condition. We can imitate without

### [45:31 - 45:31]

condition. We can imitate without

### [45:31 - 45:32]

condition. We can imitate without compounding error. I'm going to for the

### [45:32 - 45:32]

compounding error. I'm going to for the

### [45:32 - 45:33]

compounding error. I'm going to for the interest of time I'm going to be super

### [45:33 - 45:33]

interest of time I'm going to be super

### [45:33 - 45:35]

interest of time I'm going to be super informal about this but basically what

### [45:35 - 45:36]

informal about this but basically what

### [45:36 - 45:37]

informal about this but basically what this says is that like thinking about

### [45:37 - 45:37]

this says is that like thinking about

### [45:37 - 45:38]

this says is that like thinking about coverage and continuous action spaces in

### [45:38 - 45:38]

coverage and continuous action spaces in

### [45:38 - 45:40]

coverage and continuous action spaces in a more geometric or anti-conentration

### [45:40 - 45:40]

a more geometric or anti-conentration

### [45:40 - 45:42]

a more geometric or anti-conentration way is more is is quite useful. The

### [45:42 - 45:42]

way is more is is quite useful. The

### [45:42 - 45:43]

way is more is is quite useful. The intuition that you should have is

### [45:43 - 45:43]

intuition that you should have is

### [45:43 - 45:44]

intuition that you should have is essentially you can learn a little bit

### [45:44 - 45:44]

essentially you can learn a little bit

### [45:44 - 45:46]

essentially you can learn a little bit of a tube around the expert policy. I

### [45:46 - 45:46]

of a tube around the expert policy. I

### [45:46 - 45:48]

of a tube around the expert policy. I should include a graphic about this and

### [45:48 - 45:48]

should include a graphic about this and

### [45:48 - 45:49]

should include a graphic about this and this allows you to learn local tailor

### [45:49 - 45:49]

this allows you to learn local tailor

### [45:49 - 45:51]

this allows you to learn local tailor expansions and by learning the local

### [45:51 - 45:51]

expansions and by learning the local

### [45:51 - 45:52]

expansions and by learning the local tailaylor expansion you actually get the

### [45:52 - 45:52]

tailaylor expansion you actually get the

### [45:52 - 45:53]

tailaylor expansion you actually get the controller right in a region which

### [45:53 - 45:53]

controller right in a region which

### [45:53 - 45:55]

controller right in a region which allows you to stabilize. So we have some

### [45:55 - 45:56]

allows you to stabilize. So we have some

### [45:56 - 45:57]

allows you to stabilize. So we have some results of this form and we were

### [45:57 - 45:57]

results of this form and we were

### [45:57 - 45:58]

results of this form and we were actually strengthening them in some

### [45:58 - 45:58]

actually strengthening them in some

### [45:58 - 46:00]

actually strengthening them in some future work but it really says that for

### [46:00 - 46:00]

future work but it really says that for

### [46:00 - 46:02]

future work but it really says that for continuous action spaces it's important

### [46:02 - 46:02]

continuous action spaces it's important

### [46:02 - 46:03]

continuous action spaces it's important to think geometrically not just

### [46:03 - 46:03]

to think geometrically not just

### [46:03 - 46:05]

to think geometrically not just probabilistically and also there's some

### [46:05 - 46:05]

probabilistically and also there's some

### [46:05 - 46:07]

probabilistically and also there's some work between with Adam Block and I on

### [46:07 - 46:07]

work between with Adam Block and I on

### [46:07 - 46:08]

work between with Adam Block and I on some work in smooth online learning that

### [46:08 - 46:08]

some work in smooth online learning that

### [46:08 - 46:10]

some work in smooth online learning that also has a more geometric take that kind

### [46:10 - 46:10]

also has a more geometric take that kind

### [46:10 - 46:12]

also has a more geometric take that kind of has a similar takeaway

### [46:12 - 46:12]

of has a similar takeaway

### [46:12 - 46:15]

of has a similar takeaway um uh maybe an algorithmic takeaway is

### [46:15 - 46:15]

um uh maybe an algorithmic takeaway is

### [46:15 - 46:17]

um uh maybe an algorithmic takeaway is also thinking thinking about the work

### [46:17 - 46:17]

also thinking thinking about the work

### [46:17 - 46:19]

also thinking thinking about the work the role of yes non one second is is

### [46:19 - 46:19]

the role of yes non one second is is

### [46:19 - 46:20]

the role of yes non one second is is thinking about the role of data

### [46:20 - 46:20]

thinking about the role of data

### [46:20 - 46:23]

thinking about the role of data collection as well yes none yeah so when

### [46:23 - 46:23]

collection as well yes none yeah so when

### [46:23 - 46:26]

collection as well yes none yeah so when you say metric versus probabilistic

### [46:26 - 46:26]

you say metric versus probabilistic

### [46:26 - 46:27]

you say metric versus probabilistic notion of coverage I guess probabilistic

### [46:27 - 46:27]

notion of coverage I guess probabilistic

### [46:27 - 46:29]

notion of coverage I guess probabilistic you're talking about you know things

### [46:29 - 46:29]

you're talking about you know things

### [46:29 - 46:32]

you're talking about you know things like density ratios of correct and for

### [46:32 - 46:32]

like density ratios of correct and for

### [46:32 - 46:34]

like density ratios of correct and for metric do I interpret it as something

### [46:34 - 46:34]

metric do I interpret it as something

### [46:34 - 46:36]

metric do I interpret it as something like you know near linear NDP you can

### [46:36 - 46:36]

like you know near linear NDP you can

### [46:36 - 46:38]

like you know near linear NDP you can refine the coverage into something like

### [46:38 - 46:38]

refine the coverage into something like

### [46:38 - 46:40]

refine the coverage into something like the sample coarance matrix and that sort

### [46:40 - 46:40]

the sample coarance matrix and that sort

### [46:40 - 46:42]

the sample coarance matrix and that sort of thing and then linear dynamical

### [46:42 - 46:42]

of thing and then linear dynamical

### [46:42 - 46:44]

of thing and then linear dynamical systems like you obviously also have

### [46:44 - 46:44]

systems like you obviously also have

### [46:44 - 46:46]

systems like you obviously also have like you know the linearity and I I

### [46:46 - 46:46]

like you know the linearity and I I

### [46:46 - 46:48]

like you know the linearity and I I think I think it's actually quite the o

### [46:48 - 46:48]

think I think it's actually quite the o

### [46:48 - 46:48]

think I think it's actually quite the o o o o o o o o o o o o o o o o o o o o o

### [46:48 - 46:50]

o o o o o o o o o o o o o o o o o o o opposite so so in in linear systems or

### [46:50 - 46:50]

opposite so so in in linear systems or

### [46:50 - 46:52]

opposite so so in in linear systems or like linear MDPs what you're what you

### [46:52 - 46:52]

like linear MDPs what you're what you

### [46:52 - 46:54]

like linear MDPs what you're what you get you don't need coariant coverage you

### [46:54 - 46:54]

get you don't need coariant coverage you

### [46:54 - 46:55]

get you don't need coariant coverage you coariance coverage. So you actually need

### [46:55 - 46:55]

coariance coverage. So you actually need

### [46:55 - 46:57]

coariance coverage. So you actually need a you can get away with weaker notions

### [46:57 - 46:57]

a you can get away with weaker notions

### [46:57 - 46:59]

a you can get away with weaker notions of coverage that depend on like moments

### [46:59 - 46:59]

of coverage that depend on like moments

### [46:59 - 47:01]

of coverage that depend on like moments of the distribution. Yeah, that's what I

### [47:01 - 47:01]

of the distribution. Yeah, that's what I

### [47:01 - 47:02]

of the distribution. Yeah, that's what I meant. What what we're saying is

### [47:02 - 47:02]

meant. What what we're saying is

### [47:02 - 47:04]

meant. What what we're saying is actually need something stronger. So the

### [47:04 - 47:04]

actually need something stronger. So the

### [47:04 - 47:06]

actually need something stronger. So the the coverage needed in linear settings

### [47:06 - 47:06]

the coverage needed in linear settings

### [47:06 - 47:07]

the coverage needed in linear settings is actually weaker than sort of like

### [47:07 - 47:07]

is actually weaker than sort of like

### [47:07 - 47:09]

is actually weaker than sort of like density ratio coverage because it's just

### [47:09 - 47:09]

density ratio coverage because it's just

### [47:09 - 47:11]

density ratio coverage because it's just of a sufficient statistic. What we're

### [47:11 - 47:11]

of a sufficient statistic. What we're

### [47:11 - 47:12]

of a sufficient statistic. What we're saying is we need something that's

### [47:12 - 47:12]

saying is we need something that's

### [47:12 - 47:15]

saying is we need something that's actually ratio coverage. Yeah. Stronger

### [47:15 - 47:15]

actually ratio coverage. Yeah. Stronger

### [47:15 - 47:16]

actually ratio coverage. Yeah. Stronger than density ratio coverage. Something

### [47:16 - 47:16]

than density ratio coverage. Something

### [47:16 - 47:18]

than density ratio coverage. Something that actually kind of covers the nearby

### [47:18 - 47:18]

that actually kind of covers the nearby

### [47:18 - 47:20]

that actually kind of covers the nearby metric space even though this is off

### [47:20 - 47:20]

metric space even though this is off

### [47:20 - 47:21]

metric space even though this is off distribution of your expert. Right.

### [47:21 - 47:21]

distribution of your expert. Right.

### [47:21 - 47:23]

distribution of your expert. Right. Right. Right. Right. That's a great

### [47:23 - 47:23]

Right. Right. Right. That's a great

### [47:23 - 47:25]

Right. Right. Right. That's a great question. Thank you. Uh the second

### [47:25 - 47:25]

question. Thank you. Uh the second

### [47:25 - 47:26]

question. Thank you. Uh the second thing, here's a cool little graph is

### [47:26 - 47:26]

thing, here's a cool little graph is

### [47:26 - 47:29]

thing, here's a cool little graph is actually basically that more um uh uh we

### [47:29 - 47:30]

actually basically that more um uh uh we

### [47:30 - 47:31]

actually basically that more um uh uh we can actually show that improper policies

### [47:31 - 47:31]

can actually show that improper policies

### [47:31 - 47:33]

can actually show that improper policies are more powerful. So one thing that you

### [47:33 - 47:33]

are more powerful. So one thing that you

### [47:33 - 47:34]

are more powerful. So one thing that you can actually do is you can predict

### [47:34 - 47:34]

can actually do is you can predict

### [47:34 - 47:36]

can actually do is you can predict sequences of openloop sequences of

### [47:36 - 47:36]

sequences of openloop sequences of

### [47:36 - 47:38]

sequences of openloop sequences of actions. We call them action chunks. And

### [47:38 - 47:38]

actions. We call them action chunks. And

### [47:38 - 47:40]

actions. We call them action chunks. And it turns out that action chunks can kind

### [47:40 - 47:40]

it turns out that action chunks can kind

### [47:40 - 47:42]

it turns out that action chunks can kind of like uh can kind of get around some

### [47:42 - 47:42]

of like uh can kind of get around some

### [47:42 - 47:44]

of like uh can kind of get around some of these problems. Uh this is being made

### [47:44 - 47:44]

of these problems. Uh this is being made

### [47:44 - 47:46]

of these problems. Uh this is being made more clear in future work. But basically

### [47:46 - 47:46]

more clear in future work. But basically

### [47:46 - 47:48]

more clear in future work. But basically what they can do is if your s if your

### [47:48 - 47:48]

what they can do is if your s if your

### [47:48 - 47:51]

what they can do is if your s if your expert is uh sort of closed loop stable

### [47:51 - 47:51]

expert is uh sort of closed loop stable

### [47:51 - 47:52]

expert is uh sort of closed loop stable then it means that sort of the

### [47:52 - 47:52]

then it means that sort of the

### [47:52 - 47:54]

then it means that sort of the perturbation of the input to the expert

### [47:54 - 47:54]

perturbation of the input to the expert

### [47:54 - 47:56]

perturbation of the input to the expert uh to future actions is also going to be

### [47:56 - 47:56]

uh to future actions is also going to be

### [47:56 - 47:59]

uh to future actions is also going to be kind of exponentially like stable. And

### [47:59 - 47:59]

kind of exponentially like stable. And

### [47:59 - 48:00]

kind of exponentially like stable. And that means that if you learn a whole

### [48:00 - 48:00]

that means that if you learn a whole

### [48:00 - 48:01]

that means that if you learn a whole sequence of chunks of actions you can

### [48:01 - 48:01]

sequence of chunks of actions you can

### [48:01 - 48:03]

sequence of chunks of actions you can kind of predict multiple steps ahead and

### [48:03 - 48:03]

kind of predict multiple steps ahead and

### [48:03 - 48:05]

kind of predict multiple steps ahead and have stability into multiple steps in

### [48:05 - 48:05]

have stability into multiple steps in

### [48:05 - 48:06]

have stability into multiple steps in the future. And it turns out you can

### [48:06 - 48:06]

the future. And it turns out you can

### [48:06 - 48:08]

the future. And it turns out you can actually feed this back into the system

### [48:08 - 48:08]

actually feed this back into the system

### [48:08 - 48:09]

actually feed this back into the system in a way that preserves stability.

### [48:09 - 48:09]

in a way that preserves stability.

### [48:09 - 48:10]

in a way that preserves stability. Unfortunately I don't have time to go

### [48:10 - 48:10]

Unfortunately I don't have time to go

### [48:10 - 48:12]

Unfortunately I don't have time to go into this but needless to say there are

### [48:12 - 48:12]

into this but needless to say there are

### [48:12 - 48:13]

into this but needless to say there are ways around this that are purely

### [48:13 - 48:13]

ways around this that are purely

### [48:13 - 48:15]

ways around this that are purely algorithmic. And in fact we can actually

### [48:15 - 48:15]

algorithmic. And in fact we can actually

### [48:15 - 48:17]

algorithmic. And in fact we can actually solve imitation learning in all uh

### [48:17 - 48:17]

solve imitation learning in all uh

### [48:17 - 48:19]

solve imitation learning in all uh continuous action problems that are

### [48:19 - 48:19]

continuous action problems that are

### [48:19 - 48:20]

continuous action problems that are exponentially input stable and open and

### [48:20 - 48:20]

exponentially input stable and open and

### [48:20 - 48:22]

exponentially input stable and open and closed loop by action chunking. Here the

### [48:22 - 48:22]

closed loop by action chunking. Here the

### [48:22 - 48:24]

closed loop by action chunking. Here the graph shows an experiment validating

### [48:24 - 48:24]

graph shows an experiment validating

### [48:24 - 48:26]

graph shows an experiment validating this. So we use a diffusion policy to

### [48:26 - 48:26]

this. So we use a diffusion policy to

### [48:26 - 48:27]

this. So we use a diffusion policy to imitate because that's very popular

### [48:27 - 48:27]

imitate because that's very popular

### [48:27 - 48:29]

imitate because that's very popular today. The op the red openloop

### [48:29 - 48:29]

today. The op the red openloop

### [48:29 - 48:31]

today. The op the red openloop trajectory. This is if we just like let

### [48:31 - 48:31]

trajectory. This is if we just like let

### [48:31 - 48:33]

trajectory. This is if we just like let the system go with errors is is read is

### [48:33 - 48:33]

the system go with errors is is read is

### [48:33 - 48:35]

the system go with errors is is read is is is is denoted in red. And basically

### [48:35 - 48:35]

is is is denoted in red. And basically

### [48:35 - 48:37]

is is is denoted in red. And basically this is getting very little compounding

### [48:37 - 48:37]

this is getting very little compounding

### [48:37 - 48:38]

this is getting very little compounding error. It's basically staying very close

### [48:38 - 48:38]

error. It's basically staying very close

### [48:38 - 48:40]

error. It's basically staying very close to the system. Now we train a bunch of

### [48:40 - 48:40]

to the system. Now we train a bunch of

### [48:40 - 48:42]

to the system. Now we train a bunch of different uh sort of diffusion policies

### [48:42 - 48:42]

different uh sort of diffusion policies

### [48:42 - 48:44]

different uh sort of diffusion policies with different lengths of the action

### [48:44 - 48:44]

with different lengths of the action

### [48:44 - 48:46]

with different lengths of the action chunks. We see that no using no chunking

### [48:46 - 48:46]

chunks. We see that no using no chunking

### [48:46 - 48:48]

chunks. We see that no using no chunking leads to a huge very quick divergence in

### [48:48 - 48:48]

leads to a huge very quick divergence in

### [48:48 - 48:50]

leads to a huge very quick divergence in the policy and as we use bigger and

### [48:50 - 48:50]

the policy and as we use bigger and

### [48:50 - 48:51]

the policy and as we use bigger and bigger chunks we have more and more

### [48:51 - 48:51]

bigger chunks we have more and more

### [48:51 - 48:53]

bigger chunks we have more and more stability. So this is kind of a really

### [48:53 - 48:53]

stability. So this is kind of a really

### [48:53 - 48:55]

stability. So this is kind of a really interesting very strange effect that

### [48:55 - 48:55]

interesting very strange effect that

### [48:55 - 48:57]

interesting very strange effect that that I think is is somewhat unique to

### [48:57 - 48:57]

that I think is is somewhat unique to

### [48:57 - 48:59]

that I think is is somewhat unique to continuous action spaces. I want to save

### [48:59 - 48:59]

continuous action spaces. I want to save

### [48:59 - 49:00]

continuous action spaces. I want to save questions to the end because there's

### [49:00 - 49:00]

questions to the end because there's

### [49:00 - 49:03]

questions to the end because there's even more weird stuff that can happen.

### [49:03 - 49:03]

even more weird stuff that can happen.

### [49:03 - 49:05]

even more weird stuff that can happen. Um in fact we can actually think about

### [49:05 - 49:05]

Um in fact we can actually think about

### [49:05 - 49:07]

Um in fact we can actually think about instability in a very stylized way and

### [49:07 - 49:07]

instability in a very stylized way and

### [49:07 - 49:09]

instability in a very stylized way and this will kind of be the last little bit

### [49:09 - 49:09]

this will kind of be the last little bit

### [49:09 - 49:10]

this will kind of be the last little bit of the talk that I want to explain. So

### [49:10 - 49:10]

of the talk that I want to explain. So

### [49:10 - 49:13]

of the talk that I want to explain. So imagine a scalar dynamical system where

### [49:13 - 49:13]

imagine a scalar dynamical system where

### [49:13 - 49:15]

imagine a scalar dynamical system where you have some unknown sign of the

### [49:15 - 49:16]

you have some unknown sign of the

### [49:16 - 49:18]

you have some unknown sign of the system. It's either plus or minus one.

### [49:18 - 49:18]

system. It's either plus or minus one.

### [49:18 - 49:19]

system. It's either plus or minus one. You have a scalar parameter that's

### [49:19 - 49:19]

You have a scalar parameter that's

### [49:19 - 49:21]

You have a scalar parameter that's strictly bigger than one that dictates

### [49:21 - 49:21]

strictly bigger than one that dictates

### [49:21 - 49:23]

strictly bigger than one that dictates instability and you have some input you

### [49:23 - 49:23]

instability and you have some input you

### [49:23 - 49:25]

instability and you have some input you can put into the system. So this is a

### [49:25 - 49:25]

can put into the system. So this is a

### [49:25 - 49:27]

can put into the system. So this is a scalar system. It's unstable because row

### [49:27 - 49:27]

scalar system. It's unstable because row

### [49:27 - 49:29]

scalar system. It's unstable because row is greater than one and you have an

### [49:29 - 49:29]

is greater than one and you have an

### [49:29 - 49:30]

is greater than one and you have an unknown sign. So basically it says you

### [49:30 - 49:30]

unknown sign. So basically it says you

### [49:30 - 49:32]

unknown sign. So basically it says you don't know which way the dynamics are

### [49:32 - 49:32]

don't know which way the dynamics are

### [49:32 - 49:33]

don't know which way the dynamics are going to push you. You don't know which

### [49:33 - 49:33]

going to push you. You don't know which

### [49:33 - 49:34]

going to push you. You don't know which way to cancel them

### [49:34 - 49:34]

way to cancel them

### [49:34 - 49:37]

way to cancel them out. So one obvious kind of fact is that

### [49:37 - 49:38]

out. So one obvious kind of fact is that

### [49:38 - 49:39]

out. So one obvious kind of fact is that if you don't know what C is, you don't

### [49:39 - 49:39]

if you don't know what C is, you don't

### [49:39 - 49:41]

if you don't know what C is, you don't know the sign, there's no linear

### [49:41 - 49:41]

know the sign, there's no linear

### [49:41 - 49:43]

know the sign, there's no linear feedback policy which will stabilize for

### [49:43 - 49:43]

feedback policy which will stabilize for

### [49:43 - 49:45]

feedback policy which will stabilize for both choices of C. Right? And this is

### [49:45 - 49:45]

both choices of C. Right? And this is

### [49:45 - 49:46]

both choices of C. Right? And this is sort of because like either your sign is

### [49:46 - 49:46]

sort of because like either your sign is

### [49:46 - 49:48]

sort of because like either your sign is pointing you in one direction or it's

### [49:48 - 49:48]

pointing you in one direction or it's

### [49:48 - 49:49]

pointing you in one direction or it's pointing you in another direction. And

### [49:49 - 49:49]

pointing you in another direction. And

### [49:49 - 49:51]

pointing you in another direction. And so whatever your linear policy is, there

### [49:51 - 49:52]

so whatever your linear policy is, there

### [49:52 - 49:53]

so whatever your linear policy is, there will be a sign that makes this magnitude

### [49:53 - 49:53]

will be a sign that makes this magnitude

### [49:53 - 49:57]

will be a sign that makes this magnitude greater than one. Not so interesting. as

### [49:57 - 49:57]

greater than one. Not so interesting. as

### [49:57 - 49:59]

greater than one. Not so interesting. as correlated to this by tailor expanding

### [49:59 - 49:59]

correlated to this by tailor expanding

### [49:59 - 50:00]

correlated to this by tailor expanding there exists no smooth deterministic

### [50:00 - 50:00]

there exists no smooth deterministic

### [50:00 - 50:02]

there exists no smooth deterministic policy which also locally stabilizes

### [50:02 - 50:02]

policy which also locally stabilizes

### [50:02 - 50:03]

policy which also locally stabilizes your dynamics right because a smooth

### [50:03 - 50:03]

your dynamics right because a smooth

### [50:03 - 50:05]

your dynamics right because a smooth deterministic policy can be locally

### [50:05 - 50:05]

deterministic policy can be locally

### [50:05 - 50:07]

deterministic policy can be locally stabilized uh you can just argue this

### [50:07 - 50:07]

stabilized uh you can just argue this

### [50:07 - 50:10]

stabilized uh you can just argue this with a with a tailor expansion argue

### [50:10 - 50:10]

with a with a tailor expansion argue

### [50:10 - 50:12]

with a with a tailor expansion argue about linear approximation uh you can

### [50:12 - 50:12]

about linear approximation uh you can

### [50:12 - 50:13]

about linear approximation uh you can even generalize this to show that

### [50:13 - 50:13]

even generalize this to show that

### [50:13 - 50:14]

even generalize this to show that there's no simple policy one that's

### [50:14 - 50:14]

there's no simple policy one that's

### [50:14 - 50:16]

there's no simple policy one that's basically a smooth policy plus state

### [50:16 - 50:16]

basically a smooth policy plus state

### [50:16 - 50:18]

basically a smooth policy plus state independent noise which locally

### [50:18 - 50:18]

independent noise which locally

### [50:18 - 50:21]

independent noise which locally stabilizes and again uh this kind of

### [50:21 - 50:21]

stabilizes and again uh this kind of

### [50:21 - 50:22]

stabilizes and again uh this kind of follows from a similar tailor expansion

### [50:22 - 50:22]

follows from a similar tailor expansion

### [50:22 - 50:23]

follows from a similar tailor expansion argument with a few more bells and

### [50:23 - 50:23]

argument with a few more bells and

### [50:23 - 50:27]

argument with a few more bells and whistles um but what's kind of weird

### [50:27 - 50:27]

whistles um but what's kind of weird

### [50:27 - 50:29]

whistles um but what's kind of weird is that there are some like really weird

### [50:29 - 50:29]

is that there are some like really weird

### [50:29 - 50:31]

is that there are some like really weird policies that can stabilize this even

### [50:31 - 50:31]

policies that can stabilize this even

### [50:31 - 50:33]

policies that can stabilize this even without knowledge of so let me give an

### [50:33 - 50:33]

without knowledge of so let me give an

### [50:33 - 50:35]

without knowledge of so let me give an example uh this policy which is just

### [50:35 - 50:35]

example uh this policy which is just

### [50:35 - 50:38]

example uh this policy which is just time varying stabilizes the system so

### [50:38 - 50:38]

time varying stabilizes the system so

### [50:38 - 50:39]

time varying stabilizes the system so what happens right like the first time

### [50:39 - 50:40]

what happens right like the first time

### [50:40 - 50:41]

what happens right like the first time you try to stabilize in one direction if

### [50:41 - 50:41]

you try to stabilize in one direction if

### [50:41 - 50:43]

you try to stabilize in one direction if you're right good you're at zero and

### [50:43 - 50:43]

you're right good you're at zero and

### [50:43 - 50:44]

you're right good you're at zero and you'll stay there if you're wrong you'll

### [50:44 - 50:44]

you'll stay there if you're wrong you'll

### [50:44 - 50:45]

you'll stay there if you're wrong you'll just try the other way and that will

### [50:45 - 50:45]

just try the other way and that will

### [50:45 - 50:48]

just try the other way and that will work this is kind of weird uh there's

### [50:48 - 50:48]

work this is kind of weird uh there's

### [50:48 - 50:50]

work this is kind of weird uh there's also this other thing we call concentric

### [50:50 - 50:50]

also this other thing we call concentric

### [50:50 - 50:52]

also this other thing we call concentric stabilization this is kind of related to

### [50:52 - 50:52]

stabilization this is kind of related to

### [50:52 - 50:54]

stabilization this is kind of related to more classical kind of pathological

### [50:54 - 50:54]

more classical kind of pathological

### [50:54 - 50:55]

more classical kind of pathological controllers in the control theory

### [50:55 - 50:55]

controllers in the control theory

### [50:55 - 50:56]

controllers in the control theory literature

### [50:56 - 50:56]

literature

### [50:56 - 50:58]

literature where basically you can just bin

### [50:58 - 50:58]

where basically you can just bin

### [50:58 - 50:59]

where basically you can just bin diatically your kind of intervals on

### [50:59 - 50:59]

diatically your kind of intervals on

### [50:59 - 51:01]

diatically your kind of intervals on both sides and you can have a switching

### [51:01 - 51:01]

both sides and you can have a switching

### [51:01 - 51:04]

both sides and you can have a switching policy which decides which sign to use

### [51:04 - 51:04]

policy which decides which sign to use

### [51:04 - 51:06]

policy which decides which sign to use depending on which bin you're in. So if

### [51:06 - 51:06]

depending on which bin you're in. So if

### [51:06 - 51:08]

depending on which bin you're in. So if you kind of get the bin right you've

### [51:08 - 51:08]

you kind of get the bin right you've

### [51:08 - 51:09]

you kind of get the bin right you've stabilized to zero. If you get the bin

### [51:09 - 51:09]

stabilized to zero. If you get the bin

### [51:09 - 51:11]

stabilized to zero. If you get the bin wrong essentially if you choose things

### [51:11 - 51:11]

wrong essentially if you choose things

### [51:11 - 51:13]

wrong essentially if you choose things correctly you end up in the next bin

### [51:13 - 51:13]

correctly you end up in the next bin

### [51:13 - 51:14]

correctly you end up in the next bin over and that stabilizes you back to

### [51:14 - 51:14]

over and that stabilizes you back to

### [51:14 - 51:16]

over and that stabilizes you back to zero. So notice this is like a highly

### [51:16 - 51:16]

zero. So notice this is like a highly

### [51:16 - 51:18]

zero. So notice this is like a highly non smooth policy right because it's

### [51:18 - 51:18]

non smooth policy right because it's

### [51:18 - 51:19]

non smooth policy right because it's going to get vanishingly less and less

### [51:19 - 51:20]

going to get vanishingly less and less

### [51:20 - 51:21]

going to get vanishingly less and less smooth as you go to the origin. you can

### [51:21 - 51:21]

smooth as you go to the origin. you can

### [51:21 - 51:23]

smooth as you go to the origin. you can smooth things out a little bit. So it

### [51:23 - 51:23]

smooth things out a little bit. So it

### [51:23 - 51:24]

smooth things out a little bit. So it has a bounded second derivative, but

### [51:24 - 51:24]

has a bounded second derivative, but

### [51:24 - 51:25]

has a bounded second derivative, but it's still going to have a singularity

### [51:25 - 51:25]

it's still going to have a singularity

### [51:25 - 51:28]

it's still going to have a singularity here. So this is also like very very

### [51:28 - 51:28]

here. So this is also like very very

### [51:28 - 51:30]

here. So this is also like very very strange. And the last thing you do you

### [51:30 - 51:30]

strange. And the last thing you do you

### [51:30 - 51:31]

strange. And the last thing you do you can have is something called uh we call

### [51:31 - 51:32]

can have is something called uh we call

### [51:32 - 51:33]

can have is something called uh we call benevolent gamblers rune which I think

### [51:33 - 51:33]

benevolent gamblers rune which I think

### [51:33 - 51:34]

benevolent gamblers rune which I think is the thing that's sort of the most

### [51:34 - 51:34]

is the thing that's sort of the most

### [51:34 - 51:37]

is the thing that's sort of the most shocking to me. So you can just learn a

### [51:37 - 51:37]

shocking to me. So you can just learn a

### [51:37 - 51:40]

shocking to me. So you can just learn a policy which is uh with probability 1/2

### [51:40 - 51:40]

policy which is uh with probability 1/2

### [51:40 - 51:43]

policy which is uh with probability 1/2 either plays row of x or a negative row

### [51:43 - 51:43]

either plays row of x or a negative row

### [51:43 - 51:45]

either plays row of x or a negative row of x. So it just flips its sign. And so

### [51:45 - 51:45]

of x. So it just flips its sign. And so

### [51:45 - 51:47]

of x. So it just flips its sign. And so what this looks like is basically if you

### [51:47 - 51:47]

what this looks like is basically if you

### [51:47 - 51:49]

what this looks like is basically if you look at the probabilities that you

### [51:49 - 51:49]

look at the probabilities that you

### [51:49 - 51:51]

look at the probabilities that you haven't sent this to zero at each time

### [51:51 - 51:51]

haven't sent this to zero at each time

### [51:51 - 51:53]

haven't sent this to zero at each time step with probability 1/2 you send the

### [51:53 - 51:54]

step with probability 1/2 you send the

### [51:54 - 51:55]

step with probability 1/2 you send the dynamics to zero and you stay there

### [51:55 - 51:55]

dynamics to zero and you stay there

### [51:55 - 51:57]

dynamics to zero and you stay there right so each time the chance of being

### [51:57 - 51:57]

right so each time the chance of being

### [51:57 - 51:59]

right so each time the chance of being at zero is growing in probability and

### [51:59 - 51:59]

at zero is growing in probability and

### [51:59 - 52:00]

at zero is growing in probability and the chance that you're not at zero is

### [52:00 - 52:00]

the chance that you're not at zero is

### [52:00 - 52:02]

the chance that you're not at zero is getting bigger and bigger. So in

### [52:02 - 52:02]

getting bigger and bigger. So in

### [52:02 - 52:03]

getting bigger and bigger. So in expectation you're actually like

### [52:03 - 52:03]

expectation you're actually like

### [52:03 - 52:05]

expectation you're actually like destabilizing the system but we get this

### [52:05 - 52:05]

destabilizing the system but we get this

### [52:05 - 52:07]

destabilizing the system but we get this benevolent gamblers's rune which is that

### [52:07 - 52:07]

benevolent gamblers's rune which is that

### [52:07 - 52:08]

benevolent gamblers's rune which is that on like a very large probability event

### [52:08 - 52:08]

on like a very large probability event

### [52:08 - 52:10]

on like a very large probability event you've stabilized the system and in fact

### [52:10 - 52:10]

you've stabilized the system and in fact

### [52:10 - 52:11]

you've stabilized the system and in fact this is sort of related to a

### [52:11 - 52:11]

this is sort of related to a

### [52:11 - 52:13]

this is sort of related to a technicality in the lower bound that

### [52:13 - 52:13]

technicality in the lower bound that

### [52:13 - 52:14]

technicality in the lower bound that this this that the audience will

### [52:14 - 52:14]

this this that the audience will

### [52:14 - 52:16]

this this that the audience will appreciate which is that we decided to

### [52:16 - 52:16]

appreciate which is that we decided to

### [52:16 - 52:18]

appreciate which is that we decided to prove our lower bound not on L2 distance

### [52:18 - 52:18]

prove our lower bound not on L2 distance

### [52:18 - 52:19]

prove our lower bound not on L2 distance from the expert but on costs that are

### [52:19 - 52:19]

from the expert but on costs that are

### [52:19 - 52:21]

from the expert but on costs that are bounded. So our lower bound proves

### [52:21 - 52:21]

bounded. So our lower bound proves

### [52:21 - 52:23]

bounded. So our lower bound proves against bounded cost to prevent us from

### [52:23 - 52:23]

against bounded cost to prevent us from

### [52:23 - 52:24]

against bounded cost to prevent us from cheating using benevolent gamblers's

### [52:24 - 52:24]

cheating using benevolent gamblers's

### [52:24 - 52:26]

cheating using benevolent gamblers's rune. We can't use that in our advantage

### [52:26 - 52:26]

rune. We can't use that in our advantage

### [52:26 - 52:28]

rune. We can't use that in our advantage in the lower bound. But in fact this

### [52:28 - 52:28]

in the lower bound. But in fact this

### [52:28 - 52:29]

in the lower bound. But in fact this actually shows that that this is sort of

### [52:29 - 52:29]

actually shows that that this is sort of

### [52:29 - 52:31]

actually shows that that this is sort of that that actually moving to kind of

### [52:31 - 52:31]

that that actually moving to kind of

### [52:31 - 52:33]

that that actually moving to kind of complex stoastic policies uh can

### [52:33 - 52:33]

complex stoastic policies uh can

### [52:33 - 52:34]

complex stoastic policies uh can actually give you wins if you have

### [52:34 - 52:34]

actually give you wins if you have

### [52:34 - 52:37]

actually give you wins if you have bounded costs which is kind of crazy. Uh

### [52:37 - 52:37]

bounded costs which is kind of crazy. Uh

### [52:37 - 52:38]

bounded costs which is kind of crazy. Uh and I think this is actually quite

### [52:38 - 52:38]

and I think this is actually quite

### [52:38 - 52:40]

and I think this is actually quite powerful. By the way we actually show

### [52:40 - 52:40]

powerful. By the way we actually show

### [52:40 - 52:42]

powerful. By the way we actually show that all these these these kind of forms

### [52:42 - 52:42]

that all these these these kind of forms

### [52:42 - 52:43]

that all these these these kind of forms of cheating the lower bound they

### [52:43 - 52:43]

of cheating the lower bound they

### [52:43 - 52:44]

of cheating the lower bound they actually have coralates where we can

### [52:44 - 52:44]

actually have coralates where we can

### [52:44 - 52:46]

actually have coralates where we can beat our construction by by using each

### [52:46 - 52:46]

beat our construction by by using each

### [52:46 - 52:47]

beat our construction by by using each one of them. You can beat it by being

### [52:47 - 52:47]

one of them. You can beat it by being

### [52:47 - 52:49]

one of them. You can beat it by being non smooth. You can beat it by using

### [52:49 - 52:49]

non smooth. You can beat it by using

### [52:49 - 52:51]

non smooth. You can beat it by using benevolent gamblers rune. And I think

### [52:51 - 52:51]

benevolent gamblers rune. And I think

### [52:51 - 52:53]

benevolent gamblers rune. And I think the benevolent gamblers's room to me is

### [52:53 - 52:53]

the benevolent gamblers's room to me is

### [52:53 - 52:54]

the benevolent gamblers's room to me is kind of the most philosophically

### [52:54 - 52:54]

kind of the most philosophically

### [52:54 - 52:56]

kind of the most philosophically interesting because if we go back to

### [52:56 - 52:56]

interesting because if we go back to

### [52:56 - 52:57]

interesting because if we go back to kind of the purpose of improper

### [52:57 - 52:57]

kind of the purpose of improper

### [52:57 - 52:59]

kind of the purpose of improper algorithms, it really comes back to a

### [52:59 - 52:59]

algorithms, it really comes back to a

### [52:59 - 53:00]

algorithms, it really comes back to a game theoretic understanding of of of

### [53:00 - 53:00]

game theoretic understanding of of of

### [53:00 - 53:02]

game theoretic understanding of of of sort of what learning is, right? We view

### [53:02 - 53:02]

sort of what learning is, right? We view

### [53:02 - 53:04]

sort of what learning is, right? We view learning as a game between a learner and

### [53:04 - 53:04]

learning as a game between a learner and

### [53:04 - 53:05]

learning as a game between a learner and nature that picks uncertain state of the

### [53:05 - 53:05]

nature that picks uncertain state of the

### [53:05 - 53:07]

nature that picks uncertain state of the world. And we need to through

### [53:07 - 53:07]

world. And we need to through

### [53:07 - 53:08]

world. And we need to through observations of that state understand

### [53:08 - 53:08]

observations of that state understand

### [53:08 - 53:10]

observations of that state understand what to do. And we understand that

### [53:10 - 53:10]

what to do. And we understand that

### [53:10 - 53:12]

what to do. And we understand that randomization provides some power of

### [53:12 - 53:12]

randomization provides some power of

### [53:12 - 53:14]

randomization provides some power of dealing uncert with uncertainty in

### [53:14 - 53:14]

dealing uncert with uncertainty in

### [53:14 - 53:16]

dealing uncert with uncertainty in games. And essentially what this

### [53:16 - 53:16]

games. And essentially what this

### [53:16 - 53:17]

games. And essentially what this benevolent gamblers rune is showing is

### [53:17 - 53:17]

benevolent gamblers rune is showing is

### [53:17 - 53:19]

benevolent gamblers rune is showing is that these kind of potentially these

### [53:19 - 53:19]

that these kind of potentially these

### [53:19 - 53:21]

that these kind of potentially these very powerful ways of randomizing, very

### [53:21 - 53:21]

very powerful ways of randomizing, very

### [53:21 - 53:23]

very powerful ways of randomizing, very sophisticated ways of randomizing are

### [53:23 - 53:23]

sophisticated ways of randomizing are

### [53:23 - 53:25]

sophisticated ways of randomizing are actually necessary for playing this

### [53:25 - 53:25]

actually necessary for playing this

### [53:25 - 53:26]

actually necessary for playing this imitation learning game correctly

### [53:26 - 53:26]

imitation learning game correctly

### [53:26 - 53:28]

imitation learning game correctly against nature. Right? So these kind of

### [53:28 - 53:28]

against nature. Right? So these kind of

### [53:28 - 53:30]

against nature. Right? So these kind of policies like the fusion policy which

### [53:30 - 53:30]

policies like the fusion policy which

### [53:30 - 53:31]

policies like the fusion policy which are known to capture multiple modes in

### [53:31 - 53:31]

are known to capture multiple modes in

### [53:31 - 53:33]

are known to capture multiple modes in the data, traditionally they've been

### [53:33 - 53:33]

the data, traditionally they've been

### [53:33 - 53:34]

the data, traditionally they've been seen as being able to represent rich

### [53:34 - 53:34]

seen as being able to represent rich

### [53:34 - 53:36]

seen as being able to represent rich action distributions. But it's actually

### [53:36 - 53:36]

action distributions. But it's actually

### [53:36 - 53:37]

action distributions. But it's actually quite conceivable that they're doing

### [53:37 - 53:37]

quite conceivable that they're doing

### [53:37 - 53:39]

quite conceivable that they're doing something even smarter. that even when

### [53:39 - 53:39]

something even smarter. that even when

### [53:39 - 53:41]

something even smarter. that even when you're trying to imitate a deterministic

### [53:41 - 53:41]

you're trying to imitate a deterministic

### [53:41 - 53:43]

you're trying to imitate a deterministic expert, there's some benefit to

### [53:43 - 53:43]

expert, there's some benefit to

### [53:43 - 53:45]

expert, there's some benefit to randomization in a complex and state

### [53:45 - 53:45]

randomization in a complex and state

### [53:45 - 53:47]

randomization in a complex and state dependent way that actually benefits

### [53:47 - 53:47]

dependent way that actually benefits

### [53:47 - 53:48]

dependent way that actually benefits your that benefits your performance

### [53:48 - 53:48]

your that benefits your performance

### [53:48 - 53:50]

your that benefits your performance because of the uncertainty over the true

### [53:50 - 53:50]

because of the uncertainty over the true

### [53:50 - 53:52]

because of the uncertainty over the true state of the nature of the dynamics. And

### [53:52 - 53:52]

state of the nature of the dynamics. And

### [53:52 - 53:53]

state of the nature of the dynamics. And I think this is something that's like

### [53:53 - 53:53]

I think this is something that's like

### [53:53 - 53:54]

I think this is something that's like kind of crazy and was kind of shocking

### [53:54 - 53:54]

kind of crazy and was kind of shocking

### [53:54 - 53:56]

kind of crazy and was kind of shocking to me after reflecting on on the

### [53:56 - 53:56]

to me after reflecting on on the

### [53:56 - 53:58]

to me after reflecting on on the consequence of this. So maybe I want to

### [53:58 - 53:58]

consequence of this. So maybe I want to

### [53:58 - 53:59]

consequence of this. So maybe I want to end on this. There's a surprising

### [53:59 - 53:59]

end on this. There's a surprising

### [53:59 - 54:01]

end on this. There's a surprising takeaway here which is that stochastic

### [54:01 - 54:01]

takeaway here which is that stochastic

### [54:01 - 54:03]

takeaway here which is that stochastic multimodal policies, things like a

### [54:03 - 54:03]

multimodal policies, things like a

### [54:03 - 54:05]

multimodal policies, things like a diffusion policy, they can yield

### [54:05 - 54:05]

diffusion policy, they can yield

### [54:05 - 54:06]

diffusion policy, they can yield benefits even for imitating

### [54:06 - 54:06]

benefits even for imitating

### [54:06 - 54:08]

benefits even for imitating deterministic policies. Right? there is

### [54:08 - 54:08]

deterministic policies. Right? there is

### [54:08 - 54:09]

deterministic policies. Right? there is like a there is a benefit of

### [54:09 - 54:09]

like a there is a benefit of

### [54:09 - 54:11]

like a there is a benefit of improperness that resembles at least

### [54:11 - 54:11]

improperness that resembles at least

### [54:11 - 54:13]

improperness that resembles at least some of the capabilities of today's

### [54:13 - 54:13]

some of the capabilities of today's

### [54:13 - 54:15]

some of the capabilities of today's robot learning models. And I think this

### [54:15 - 54:15]

robot learning models. And I think this

### [54:15 - 54:18]

robot learning models. And I think this is kind of kind of a a departure point

### [54:18 - 54:18]

is kind of kind of a a departure point

### [54:18 - 54:19]

is kind of kind of a a departure point for what kind of a big theme in my

### [54:19 - 54:19]

for what kind of a big theme in my

### [54:19 - 54:21]

for what kind of a big theme in my research today, which is understanding

### [54:21 - 54:21]

research today, which is understanding

### [54:21 - 54:23]

research today, which is understanding what's going on with generative models

### [54:23 - 54:23]

what's going on with generative models

### [54:23 - 54:24]

what's going on with generative models and control. So for those of you that

### [54:24 - 54:24]

and control. So for those of you that

### [54:24 - 54:26]

and control. So for those of you that don't know, generative models have

### [54:26 - 54:26]

don't know, generative models have

### [54:26 - 54:27]

don't know, generative models have become kind of the go-to architecture

### [54:27 - 54:27]

become kind of the go-to architecture

### [54:27 - 54:29]

become kind of the go-to architecture for kind of continuous action control

### [54:29 - 54:29]

for kind of continuous action control

### [54:29 - 54:31]

for kind of continuous action control the last two or three years. And I think

### [54:31 - 54:31]

the last two or three years. And I think

### [54:31 - 54:33]

the last two or three years. And I think we really are only scratching the

### [54:33 - 54:33]

we really are only scratching the

### [54:33 - 54:34]

we really are only scratching the surface of their full capabilities and

### [54:34 - 54:34]

surface of their full capabilities and

### [54:34 - 54:36]

surface of their full capabilities and scratching the surface of understanding

### [54:36 - 54:36]

scratching the surface of understanding

### [54:36 - 54:37]

scratching the surface of understanding why it is that they provide benefits.

### [54:37 - 54:38]

why it is that they provide benefits.

### [54:38 - 54:39]

why it is that they provide benefits. And this this talk kind of shows that

### [54:39 - 54:39]

And this this talk kind of shows that

### [54:39 - 54:41]

And this this talk kind of shows that even in very simple classical smooth and

### [54:41 - 54:41]

even in very simple classical smooth and

### [54:41 - 54:43]

even in very simple classical smooth and deterministic settings, things like

### [54:43 - 54:43]

deterministic settings, things like

### [54:43 - 54:44]

deterministic settings, things like generative modeling, things like action

### [54:44 - 54:44]

generative modeling, things like action

### [54:44 - 54:46]

generative modeling, things like action chunking, some of these more complex

### [54:46 - 54:46]

chunking, some of these more complex

### [54:46 - 54:48]

chunking, some of these more complex design decisions actually have, you

### [54:48 - 54:48]

design decisions actually have, you

### [54:48 - 54:49]

design decisions actually have, you know, potentially very powerful

### [54:49 - 54:49]

know, potentially very powerful

### [54:49 - 54:51]

know, potentially very powerful benefits. And I think there's a lot more

### [54:51 - 54:51]

benefits. And I think there's a lot more

### [54:51 - 54:52]

benefits. And I think there's a lot more to learn to understand and to harness.

### [54:52 - 54:52]

to learn to understand and to harness.

### [54:52 - 54:55]

to learn to understand and to harness. And I think with that, uh, I'm I'm happy

### [54:55 - 54:55]

And I think with that, uh, I'm I'm happy

### [54:55 - 54:56]

And I think with that, uh, I'm I'm happy to take questions, maybe a little bit of

### [54:56 - 54:56]

to take questions, maybe a little bit of

### [54:56 - 54:58]

to take questions, maybe a little bit of takeway for the RL theorists. Uh,

### [54:58 - 54:58]

takeway for the RL theorists. Uh,

### [54:58 - 55:00]

takeway for the RL theorists. Uh, rethink key functions, rethink coverage,

### [55:00 - 55:00]

rethink key functions, rethink coverage,

### [55:00 - 55:02]

rethink key functions, rethink coverage, uh, rethink pro policy

### [55:02 - 55:02]

uh, rethink pro policy

### [55:02 - 55:08]

uh, rethink pro policy parameterizations. Uh, and thank you.

### [55:13 - 55:13]

Awesome. Thank you, Max. Um, any quick

### [55:13 - 55:16]

Awesome. Thank you, Max. Um, any quick questions before we uh stop the

### [55:16 - 55:16]

questions before we uh stop the

### [55:16 - 55:17]

questions before we uh stop the recording?

### [55:17 - 55:17]

recording?

### [55:17 - 55:19]

recording? Uh, you mentioned action chunking. What

### [55:19 - 55:19]

Uh, you mentioned action chunking. What

### [55:19 - 55:22]

Uh, you mentioned action chunking. What is that? Oh, so action chunking is the

### [55:22 - 55:22]

is that? Oh, so action chunking is the

### [55:22 - 55:24]

is that? Oh, so action chunking is the practice of predicting multiple chunks

### [55:24 - 55:24]

practice of predicting multiple chunks

### [55:24 - 55:27]

practice of predicting multiple chunks of multiple steps of the action um in

### [55:27 - 55:27]

of multiple steps of the action um in

### [55:27 - 55:31]

of multiple steps of the action um in one go. So what you do is you ra so your

### [55:31 - 55:31]

one go. So what you do is you ra so your

### [55:31 - 55:33]

one go. So what you do is you ra so your expert policy let's say predicts you

### [55:33 - 55:33]

expert policy let's say predicts you

### [55:33 - 55:35]

expert policy let's say predicts you know U1 from X1 but you could also take

### [55:35 - 55:35]

know U1 from X1 but you could also take

### [55:35 - 55:38]

know U1 from X1 but you could also take U1 U2 U3 and U4 and predict that whole

### [55:38 - 55:38]

U1 U2 U3 and U4 and predict that whole

### [55:38 - 55:41]

U1 U2 U3 and U4 and predict that whole sequence from X1 and in some sense this

### [55:41 - 55:41]

sequence from X1 and in some sense this

### [55:41 - 55:42]

sequence from X1 and in some sense this increases the representational demands

### [55:42 - 55:42]

increases the representational demands

### [55:42 - 55:46]

increases the representational demands in the policy class but reduced horizon

### [55:46 - 55:46]

in the policy class but reduced horizon

### [55:46 - 55:48]

in the policy class but reduced horizon well so one the naive benefit is it

### [55:48 - 55:48]

well so one the naive benefit is it

### [55:48 - 55:50]

well so one the naive benefit is it reduces horizon but it actually turns

### [55:50 - 55:50]

reduces horizon but it actually turns

### [55:50 - 55:52]

reduces horizon but it actually turns out that there's a critical threshold of

### [55:52 - 55:52]

out that there's a critical threshold of

### [55:52 - 55:54]

out that there's a critical threshold of chunk length below which once you can

### [55:54 - 55:54]

chunk length below which once you can

### [55:54 - 55:56]

chunk length below which once you can imitate that chunk length you actually

### [55:56 - 55:56]

imitate that chunk length you actually

### [55:56 - 55:59]

imitate that chunk length you actually no longer pay compounding error.

### [55:59 - 55:59]

no longer pay compounding error.

### [55:59 - 56:02]

no longer pay compounding error. And this is um something that's it's it

### [56:02 - 56:02]

And this is um something that's it's it

### [56:02 - 56:04]

And this is um something that's it's it it basically has to do with the fact

### [56:04 - 56:04]

it basically has to do with the fact

### [56:04 - 56:07]

it basically has to do with the fact that uh there will be a point at which

### [56:07 - 56:07]

that uh there will be a point at which

### [56:07 - 56:09]

that uh there will be a point at which the openloop dynamics are sufficient.

### [56:09 - 56:09]

the openloop dynamics are sufficient.

### [56:09 - 56:10]

the openloop dynamics are sufficient. Basically what action chunking is doing

### [56:10 - 56:10]

Basically what action chunking is doing

### [56:10 - 56:12]

Basically what action chunking is doing is it's converting closed loop into open

### [56:12 - 56:12]

is it's converting closed loop into open

### [56:12 - 56:13]

is it's converting closed loop into open loop and there will be a point at which

### [56:13 - 56:13]

loop and there will be a point at which

### [56:13 - 56:15]

loop and there will be a point at which the openloop dynamics are sufficiently

### [56:15 - 56:15]

the openloop dynamics are sufficiently

### [56:15 - 56:19]

the openloop dynamics are sufficiently stable that uh you you kind of uh drown

### [56:19 - 56:19]

stable that uh you you kind of uh drown

### [56:19 - 56:21]

stable that uh you you kind of uh drown out the effects of like uh perturbations

### [56:21 - 56:22]

out the effects of like uh perturbations

### [56:22 - 56:23]

out the effects of like uh perturbations in the policy. And if you can predict

### [56:23 - 56:23]

in the policy. And if you can predict

### [56:23 - 56:25]

in the policy. And if you can predict chunks of precisely this critical length

### [56:25 - 56:25]

chunks of precisely this critical length

### [56:25 - 56:28]

chunks of precisely this critical length or longer, you can kind of like drown

### [56:28 - 56:28]

or longer, you can kind of like drown

### [56:28 - 56:29]

or longer, you can kind of like drown out some of the errors of your own of

### [56:29 - 56:29]

out some of the errors of your own of

### [56:29 - 56:32]

out some of the errors of your own of your own learn policy. Um,

### [56:32 - 56:32]

your own learn policy. Um,

### [56:32 - 56:36]

your own learn policy. Um, okay. So maybe is this maybe okay I'm

### [56:36 - 56:36]

okay. So maybe is this maybe okay I'm

### [56:36 - 56:38]

okay. So maybe is this maybe okay I'm trying to understand it and here here's

### [56:38 - 56:38]

trying to understand it and here here's

### [56:38 - 56:40]

trying to understand it and here here's maybe a too simplified way of thinking

### [56:40 - 56:40]

maybe a too simplified way of thinking

### [56:40 - 56:43]

maybe a too simplified way of thinking about it. But um suppose in your problem

### [56:43 - 56:43]

about it. But um suppose in your problem

### [56:43 - 56:45]

about it. But um suppose in your problem you have deterministic starting state

### [56:45 - 56:45]

you have deterministic starting state

### [56:45 - 56:48]

you have deterministic starting state and uh you have deterministic systems

### [56:48 - 56:48]

and uh you have deterministic systems

### [56:48 - 56:52]

and uh you have deterministic systems then effectively I could just memorize

### [56:52 - 56:52]

then effectively I could just memorize

### [56:52 - 56:55]

then effectively I could just memorize the action sequence of the expert and

### [56:55 - 56:55]

the action sequence of the expert and

### [56:55 - 56:58]

the action sequence of the expert and reproduce that. So I this is so it's a

### [56:58 - 56:58]

reproduce that. So I this is so it's a

### [56:58 - 56:59]

reproduce that. So I this is so it's a little different than this. So if I just

### [56:59 - 56:59]

little different than this. So if I just

### [56:59 - 57:01]

little different than this. So if I just memorize the distribution of the the

### [57:01 - 57:01]

memorize the distribution of the the

### [57:01 - 57:03]

memorize the distribution of the the expert essentially the effect of this is

### [57:03 - 57:03]

expert essentially the effect of this is

### [57:03 - 57:05]

expert essentially the effect of this is we're reducing the horizon right it's

### [57:05 - 57:05]

we're reducing the horizon right it's

### [57:05 - 57:06]

we're reducing the horizon right it's just basically taking you from two to

### [57:06 - 57:06]

just basically taking you from two to

### [57:06 - 57:09]

just basically taking you from two to the h two to the h over chunk length.

### [57:09 - 57:09]

the h two to the h over chunk length.

### [57:09 - 57:10]

the h two to the h over chunk length. But it actually turns out that there's

### [57:10 - 57:10]

But it actually turns out that there's

### [57:10 - 57:12]

But it actually turns out that there's another effect that's a little bit more

### [57:12 - 57:12]

another effect that's a little bit more

### [57:12 - 57:14]

another effect that's a little bit more control theoretic which is that there's

### [57:14 - 57:14]

control theoretic which is that there's

### [57:14 - 57:16]

control theoretic which is that there's actually a critical window of action

### [57:16 - 57:16]

actually a critical window of action

### [57:16 - 57:18]

actually a critical window of action chunking such that basically there's the

### [57:18 - 57:18]

chunking such that basically there's the

### [57:18 - 57:20]

chunking such that basically there's the the there's a a policy class which

### [57:20 - 57:20]

the there's a a policy class which

### [57:20 - 57:22]

the there's a a policy class which includes the expert sort of realizable

### [57:22 - 57:22]

includes the expert sort of realizable

### [57:22 - 57:25]

includes the expert sort of realizable policy class um where everything in that

### [57:25 - 57:25]

policy class um where everything in that

### [57:25 - 57:27]

policy class um where everything in that policy class is now stabilizing. Yeah.

### [57:27 - 57:28]

policy class is now stabilizing. Yeah.

### [57:28 - 57:30]

policy class is now stabilizing. Yeah. So so in that case like how does that

### [57:30 - 57:30]

So so in that case like how does that

### [57:30 - 57:33]

So so in that case like how does that critical window how is that determined

### [57:33 - 57:33]

critical window how is that determined

### [57:33 - 57:35]

critical window how is that determined like by determined by the parameter?

### [57:35 - 57:35]

like by determined by the parameter?

### [57:35 - 57:37]

like by determined by the parameter? It's determined by the row parameter of

### [57:37 - 57:37]

It's determined by the row parameter of

### [57:37 - 57:39]

It's determined by the row parameter of the of the system and determined by some

### [57:39 - 57:39]

the of the system and determined by some

### [57:39 - 57:41]

the of the system and determined by some other lipids constants. So roughly speak

### [57:41 - 57:41]

other lipids constants. So roughly speak

### [57:41 - 57:43]

other lipids constants. So roughly speak speaking it's going to look like log

### [57:43 - 57:43]

speaking it's going to look like log

### [57:43 - 57:47]

speaking it's going to look like log base row of some lipids constants.

### [57:47 - 57:47]

base row of some lipids constants.

### [57:47 - 57:49]

base row of some lipids constants. Um and actually so Nick Montney who was

### [57:49 - 57:49]

Um and actually so Nick Montney who was

### [57:49 - 57:50]

Um and actually so Nick Montney who was on the call and one of his students

### [57:50 - 57:50]

on the call and one of his students

### [57:50 - 57:53]

on the call and one of his students Thomas Jang and Dan Farmer and I are

### [57:53 - 57:53]

Thomas Jang and Dan Farmer and I are

### [57:53 - 57:54]

Thomas Jang and Dan Farmer and I are kind of working on this as a follow-up.

### [57:54 - 57:54]

kind of working on this as a follow-up.

### [57:54 - 57:55]

kind of working on this as a follow-up. That's one of the things we're also

### [57:55 - 57:55]

That's one of the things we're also

### [57:55 - 57:56]

That's one of the things we're also working on kind of a more thorough

### [57:56 - 57:56]

working on kind of a more thorough

### [57:56 - 57:58]

working on kind of a more thorough understanding of exactly how noising

### [57:58 - 57:58]

understanding of exactly how noising

### [57:58 - 58:00]

understanding of exactly how noising affects things. So what we can show for

### [58:00 - 58:00]

affects things. So what we can show for

### [58:00 - 58:01]

affects things. So what we can show for example and this might be of interest is

### [58:01 - 58:01]

example and this might be of interest is

### [58:01 - 58:03]

example and this might be of interest is that if you add noise and you use kind

### [58:03 - 58:03]

that if you add noise and you use kind

### [58:03 - 58:05]

that if you add noise and you use kind of more probabilistic or information

### [58:05 - 58:05]

of more probabilistic or information

### [58:05 - 58:07]

of more probabilistic or information theoretic arguments you pay a trade-off

### [58:07 - 58:07]

theoretic arguments you pay a trade-off

### [58:07 - 58:08]

theoretic arguments you pay a trade-off for your noise level. But if you use

### [58:08 - 58:08]

for your noise level. But if you use

### [58:08 - 58:09]

for your noise level. But if you use kind of more control theoretic and

### [58:09 - 58:09]

kind of more control theoretic and

### [58:09 - 58:11]

kind of more control theoretic and geometric arguments there ends up being

### [58:11 - 58:11]

geometric arguments there ends up being

### [58:11 - 58:13]

geometric arguments there ends up being basically this like sweet spot the sweet

### [58:13 - 58:13]

basically this like sweet spot the sweet

### [58:13 - 58:14]

basically this like sweet spot the sweet band of noise where you can add the

### [58:14 - 58:14]

band of noise where you can add the

### [58:14 - 58:17]

band of noise where you can add the noise in. And no matter as long as you

### [58:17 - 58:17]

noise in. And no matter as long as you

### [58:17 - 58:19]

noise in. And no matter as long as you add noise sort of in that sweet spot

### [58:19 - 58:19]

add noise sort of in that sweet spot

### [58:19 - 58:21]

add noise sort of in that sweet spot region uh you get like the optimal you

### [58:21 - 58:21]

region uh you get like the optimal you

### [58:21 - 58:22]

region uh you get like the optimal you get sort of like the correct rates and

### [58:22 - 58:22]

get sort of like the correct rates and

### [58:22 - 58:24]

get sort of like the correct rates and it doesn't it's not really too sensitive

### [58:24 - 58:24]

it doesn't it's not really too sensitive

### [58:24 - 58:25]

it doesn't it's not really too sensitive to the noise and there's no real

### [58:25 - 58:25]

to the noise and there's no real

### [58:25 - 58:26]

to the noise and there's no real trade-off. And essentially one way you

### [58:26 - 58:26]

trade-off. And essentially one way you

### [58:26 - 58:29]

trade-off. And essentially one way you can think about this is like you need to

### [58:29 - 58:29]

can think about this is like you need to

### [58:29 - 58:30]

can think about this is like you need to learning how to stabilize is basically a

### [58:30 - 58:30]

learning how to stabilize is basically a

### [58:30 - 58:32]

learning how to stabilize is basically a qualitative effect that you need to wrap

### [58:32 - 58:32]

qualitative effect that you need to wrap

### [58:32 - 58:34]

qualitative effect that you need to wrap around the quantitative accuracy of your

### [58:34 - 58:34]

around the quantitative accuracy of your

### [58:34 - 58:36]

around the quantitative accuracy of your policy. So really you just need enough

### [58:36 - 58:36]

policy. So really you just need enough

### [58:36 - 58:39]

policy. So really you just need enough data that can teach you okay here's how

### [58:39 - 58:39]

data that can teach you okay here's how

### [58:39 - 58:40]

data that can teach you okay here's how you kind of make sure I'm learning a

### [58:40 - 58:40]

you kind of make sure I'm learning a

### [58:40 - 58:42]

you kind of make sure I'm learning a decent enough approximation to the

### [58:42 - 58:42]

decent enough approximation to the

### [58:42 - 58:44]

decent enough approximation to the linear controller to stabilize off off

### [58:44 - 58:44]

linear controller to stabilize off off

### [58:44 - 58:46]

linear controller to stabilize off off trajectory. And once you've learned that

### [58:46 - 58:46]

trajectory. And once you've learned that

### [58:46 - 58:48]

trajectory. And once you've learned that you're golden and so we can show we have

### [58:48 - 58:48]

you're golden and so we can show we have

### [58:48 - 58:50]

you're golden and so we can show we have some arguments that are based on tassel

### [58:50 - 58:50]

some arguments that are based on tassel

### [58:50 - 58:52]

some arguments that are based on tassel which is kind of work from Dan Farmer

### [58:52 - 58:52]

which is kind of work from Dan Farmer

### [58:52 - 58:53]

which is kind of work from Dan Farmer that show that you can do this with more

### [58:53 - 58:54]

that show that you can do this with more

### [58:54 - 58:55]

that show that you can do this with more with more noise. So again, it's a very

### [58:55 - 58:55]

with more noise. So again, it's a very

### [58:55 - 58:57]

with more noise. So again, it's a very different flavor of argument than than

### [58:57 - 58:57]

different flavor of argument than than

### [58:57 - 58:58]

different flavor of argument than than what we typically see in some of the

### [58:58 - 58:58]

what we typically see in some of the

### [58:58 - 59:00]

what we typically see in some of the kind of more measure theoretic

### [59:00 - 59:00]

kind of more measure theoretic

### [59:00 - 59:04]

kind of more measure theoretic takes. But yeah, cool. Uh open to other

### [59:04 - 59:04]

takes. But yeah, cool. Uh open to other

### [59:04 - 59:06]

takes. But yeah, cool. Uh open to other questions. Um maybe we should stop the

### [59:06 - 59:06]

questions. Um maybe we should stop the

### [59:06 - 59:09]

questions. Um maybe we should stop the recording. Yes, I

### [59:09 - 59:09]

recording. Yes, I

### [59:09 - 59:13]

recording. Yes, I can do that.
