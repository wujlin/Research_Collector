# RI Seminar: Max Simchowitz: Generative Control, Action Chunking, and Moravec’s Paradox

- URL: https://www.youtube.com/watch?v=UX1YXcRnFbs
- Source: `youtube_vtt_caption`
- Caption file: `youtube/captions/max-simchowitz-generative-control-action-chunking-moravec/source.en-orig.vtt`
- Generated at: `2026-06-13T10:24:39`

## Transcript

### [00:03 - 00:03]

Welcome back. Welcome back. It is lovely

### [00:03 - 00:06]

Welcome back. Welcome back. It is lovely to see all of you.

### [00:06 - 00:06]

to see all of you.

### [00:06 - 00:09]

to see all of you. It is my great pleasure to introduce our

### [00:09 - 00:09]

It is my great pleasure to introduce our

### [00:09 - 00:12]

It is my great pleasure to introduce our next RI seminar speaker, our very own

### [00:12 - 00:12]

next RI seminar speaker, our very own

### [00:12 - 00:14]

next RI seminar speaker, our very own Professor Maxim Kovitz.

### [00:14 - 00:14]

Professor Maxim Kovitz.

### [00:14 - 00:17]

Professor Maxim Kovitz. Um Max works on the theoretical

### [00:17 - 00:17]

Um Max works on the theoretical

### [00:17 - 00:20]

Um Max works on the theoretical foundations of machine learning, but

### [00:20 - 00:20]

foundations of machine learning, but

### [00:20 - 00:22]

foundations of machine learning, but also interactive and sequential

### [00:22 - 00:22]

also interactive and sequential

### [00:22 - 00:23]

also interactive and sequential problems, which are

### [00:23 - 00:23]

problems, which are

### [00:23 - 00:26]

problems, which are all problems in robotics.

### [00:26 - 00:26]

all problems in robotics.

### [00:26 - 00:27]

all problems in robotics. Um

### [00:27 - 00:27]

Um

### [00:27 - 00:29]

Um Max did his PhD

### [00:29 - 00:29]

Max did his PhD

### [00:29 - 00:30]

Max did his PhD at Berkeley. Actually, that's where I

### [00:30 - 00:30]

at Berkeley. Actually, that's where I

### [00:30 - 00:31]

at Berkeley. Actually, that's where I first got to know him.

### [00:31 - 00:31]

first got to know him.

### [00:31 - 00:34]

first got to know him. Uh we took a few classes together and um

### [00:34 - 00:34]

Uh we took a few classes together and um

### [00:34 - 00:36]

Uh we took a few classes together and um Max is a really really smart guy. One of

### [00:36 - 00:36]

Max is a really really smart guy. One of

### [00:36 - 00:38]

Max is a really really smart guy. One of my most salient memories is So Max was

### [00:38 - 00:38]

my most salient memories is So Max was

### [00:38 - 00:40]

my most salient memories is So Max was doing like hardcore machine learning

### [00:40 - 00:40]

doing like hardcore machine learning

### [00:40 - 00:41]

doing like hardcore machine learning research.

### [00:41 - 00:41]

research.

### [00:41 - 00:43]

research. And at Berkeley, you have to take these

### [00:43 - 00:43]

And at Berkeley, you have to take these

### [00:43 - 00:45]

And at Berkeley, you have to take these oral preliminary exams. They're like

### [00:45 - 00:45]

oral preliminary exams. They're like

### [00:45 - 00:48]

oral preliminary exams. They're like whiteboard exams on a specific topic.

### [00:48 - 00:48]

whiteboard exams on a specific topic.

### [00:48 - 00:49]

whiteboard exams on a specific topic. You can pick to do it on machine

### [00:49 - 00:49]

You can pick to do it on machine

### [00:49 - 00:50]

You can pick to do it on machine learning, you can pick to do it on a

### [00:50 - 00:50]

learning, you can pick to do it on a

### [00:50 - 00:52]

learning, you can pick to do it on a control or optimization.

### [00:52 - 00:52]

control or optimization.

### [00:52 - 00:53]

control or optimization. And you know, I did the control

### [00:53 - 00:53]

And you know, I did the control

### [00:53 - 00:56]

And you know, I did the control optimization one. I expected We all

### [00:56 - 00:56]

optimization one. I expected We all

### [00:56 - 00:57]

optimization one. I expected We all expected Max to do the machine learning

### [00:57 - 00:57]

expected Max to do the machine learning

### [00:57 - 00:58]

expected Max to do the machine learning one, but he was like, "You know what?

### [00:58 - 00:58]

one, but he was like, "You know what?

### [00:58 - 01:00]

one, but he was like, "You know what? I'm going to just like decide to take

### [01:00 - 01:00]

I'm going to just like decide to take

### [01:00 - 01:02]

I'm going to just like decide to take the control one for once." And then he

### [01:02 - 01:02]

the control one for once." And then he

### [01:02 - 01:04]

the control one for once." And then he just He ended up doing the best on that

### [01:04 - 01:04]

just He ended up doing the best on that

### [01:04 - 01:06]

just He ended up doing the best on that exam and it was super embarrassing for

### [01:06 - 01:06]

exam and it was super embarrassing for

### [01:06 - 01:08]

exam and it was super embarrassing for all of us who were like focusing on

### [01:08 - 01:08]

all of us who were like focusing on

### [01:08 - 01:10]

all of us who were like focusing on control with THIS LIKE OTHER GUY DOING

### [01:10 - 01:10]

control with THIS LIKE OTHER GUY DOING

### [01:10 - 01:11]

control with THIS LIKE OTHER GUY DOING MACHINE LEARNING WHO WAS LIKE, "YEAH,

### [01:11 - 01:11]

MACHINE LEARNING WHO WAS LIKE, "YEAH,

### [01:11 - 01:12]

MACHINE LEARNING WHO WAS LIKE, "YEAH, THAT'S ACTUALLY LIKE pretty easy." So

### [01:12 - 01:12]

THAT'S ACTUALLY LIKE pretty easy." So

### [01:12 - 01:14]

THAT'S ACTUALLY LIKE pretty easy." So anyways, I've always

### [01:14 - 01:14]

anyways, I've always

### [01:14 - 01:16]

anyways, I've always been a great admirer of the way that

### [01:16 - 01:16]

been a great admirer of the way that

### [01:16 - 01:19]

been a great admirer of the way that like Max thinks Max thinks abstractly

### [01:19 - 01:19]

like Max thinks Max thinks abstractly

### [01:19 - 01:21]

like Max thinks Max thinks abstractly These days a lot more empirically as

### [01:21 - 01:21]

These days a lot more empirically as

### [01:21 - 01:22]

These days a lot more empirically as well and I'm excited to learn from him

### [01:22 - 01:22]

well and I'm excited to learn from him

### [01:22 - 01:25]

well and I'm excited to learn from him today. Thanks Andrea. Thank you.

### [01:25 - 01:25]

today. Thanks Andrea. Thank you.

### [01:25 - 01:26]

today. Thanks Andrea. Thank you. Um

### [01:26 - 01:26]

Um

### [01:26 - 01:27]

Um >> [applause]

### [01:27 - 01:27]

>> [applause]

### [01:27 - 01:30]

>> [applause] >> Uh Andrea and I also became friends in

### [01:30 - 01:30]

>> Uh Andrea and I also became friends in

### [01:30 - 01:31]

>> Uh Andrea and I also became friends in the early days of meme culture. This is

### [01:31 - 01:31]

the early days of meme culture. This is

### [01:31 - 01:34]

the early days of meme culture. This is like 2016. Do you kids know who you

### [01:34 - 01:34]

like 2016. Do you kids know who you

### [01:34 - 01:36]

like 2016. Do you kids know who you gander knuckles is?

### [01:36 - 01:36]

gander knuckles is?

### [01:36 - 01:37]

gander knuckles is? >> [laughter]

### [01:37 - 01:37]

>> [laughter]

### [01:37 - 01:39]

>> [laughter] >> Okay. Yeah. Yeah, I remember. Yeah.

### [01:39 - 01:39]

>> Okay. Yeah. Yeah, I remember. Yeah.

### [01:39 - 01:41]

>> Okay. Yeah. Yeah, I remember. Yeah. Yeah, okay. Anyway,

### [01:41 - 01:41]

Yeah, okay. Anyway,

### [01:41 - 01:43]

Yeah, okay. Anyway, uh so that's not relevant for today's

### [01:43 - 01:43]

uh so that's not relevant for today's

### [01:43 - 01:45]

uh so that's not relevant for today's talk. So I'm going to talk to you today

### [01:45 - 01:45]

talk. So I'm going to talk to you today

### [01:45 - 01:47]

talk. So I'm going to talk to you today about generative control.

### [01:47 - 01:47]

about generative control.

### [01:47 - 01:48]

about generative control. So kind of the kind of philosophical

### [01:48 - 01:48]

So kind of the kind of philosophical

### [01:48 - 01:50]

So kind of the kind of philosophical point of departure for today's talk is

### [01:50 - 01:50]

point of departure for today's talk is

### [01:50 - 01:52]

point of departure for today's talk is this you know, Moravec paradox. Hans

### [01:52 - 01:52]

this you know, Moravec paradox. Hans

### [01:52 - 01:54]

this you know, Moravec paradox. Hans Moravec actually who I think was here.

### [01:54 - 01:54]

Moravec actually who I think was here.

### [01:54 - 01:56]

Moravec actually who I think was here. He was in RI. And he noted I think many

### [01:56 - 01:56]

He was in RI. And he noted I think many

### [01:56 - 01:58]

He was in RI. And he noted I think many others have also noted that it's been

### [01:58 - 01:58]

others have also noted that it's been

### [01:58 - 02:00]

others have also noted that it's been far more difficult to get robots to be

### [02:00 - 02:00]

far more difficult to get robots to be

### [02:00 - 02:01]

far more difficult to get robots to be able to do things in the physical world

### [02:01 - 02:01]

able to do things in the physical world

### [02:01 - 02:03]

able to do things in the physical world than you know, it is it has been to get

### [02:03 - 02:03]

than you know, it is it has been to get

### [02:03 - 02:06]

than you know, it is it has been to get AI systems to work in symbolic domains.

### [02:06 - 02:06]

AI systems to work in symbolic domains.

### [02:06 - 02:08]

AI systems to work in symbolic domains. Um and yet we've seen tremendous

### [02:08 - 02:08]

Um and yet we've seen tremendous

### [02:08 - 02:09]

Um and yet we've seen tremendous progress in robotics. I don't know if

### [02:09 - 02:09]

progress in robotics. I don't know if

### [02:09 - 02:12]

progress in robotics. I don't know if Tonga is here today, but this is a video

### [02:12 - 02:12]

Tonga is here today, but this is a video

### [02:12 - 02:13]

Tonga is here today, but this is a video of him collecting

### [02:13 - 02:13]

of him collecting

### [02:13 - 02:15]

of him collecting demonstrations of shirt folding and then

### [02:15 - 02:15]

demonstrations of shirt folding and then

### [02:15 - 02:18]

demonstrations of shirt folding and then using using behavior cloning as a way to

### [02:18 - 02:18]

using using behavior cloning as a way to

### [02:18 - 02:20]

using using behavior cloning as a way to train a robot policy to shirt fold. And

### [02:20 - 02:20]

train a robot policy to shirt fold. And

### [02:20 - 02:22]

train a robot policy to shirt fold. And the reason that I I show this example is

### [02:22 - 02:22]

the reason that I I show this example is

### [02:22 - 02:23]

the reason that I I show this example is because by today's standards it's

### [02:23 - 02:23]

because by today's standards it's

### [02:23 - 02:25]

because by today's standards it's incredibly banal. So I was informed

### [02:25 - 02:25]

incredibly banal. So I was informed

### [02:25 - 02:26]

incredibly banal. So I was informed yesterday by Nina Balkan that shirt

### [02:26 - 02:26]

yesterday by Nina Balkan that shirt

### [02:26 - 02:29]

yesterday by Nina Balkan that shirt folding was in Peter Abbeel's job talk

### [02:29 - 02:29]

folding was in Peter Abbeel's job talk

### [02:29 - 02:31]

folding was in Peter Abbeel's job talk and now it's infra that a master student

### [02:31 - 02:31]

and now it's infra that a master student

### [02:31 - 02:32]

and now it's infra that a master student A very talented master student, but but

### [02:32 - 02:32]

A very talented master student, but but

### [02:32 - 02:34]

A very talented master student, but but a student is is using to begin the

### [02:34 - 02:34]

a student is is using to begin the

### [02:34 - 02:36]

a student is is using to begin the project rather than sell themselves in

### [02:36 - 02:36]

project rather than sell themselves in

### [02:36 - 02:37]

project rather than sell themselves in the job market.

### [02:37 - 02:37]

the job market.

### [02:37 - 02:39]

the job market. So kind of how did we get to this point?

### [02:39 - 02:39]

So kind of how did we get to this point?

### [02:39 - 02:42]

So kind of how did we get to this point? Well, behavior cloning also historically

### [02:42 - 02:42]

Well, behavior cloning also historically

### [02:42 - 02:43]

Well, behavior cloning also historically sort of began at Carnegie Mellon. Early

### [02:43 - 02:43]

sort of began at Carnegie Mellon. Early

### [02:43 - 02:45]

sort of began at Carnegie Mellon. Early efforts in self-driving were using it.

### [02:45 - 02:45]

efforts in self-driving were using it.

### [02:45 - 02:47]

efforts in self-driving were using it. And in the early 2020s it became very

### [02:47 - 02:47]

And in the early 2020s it became very

### [02:47 - 02:49]

And in the early 2020s it became very popular as a modality for learning and

### [02:49 - 02:49]

popular as a modality for learning and

### [02:49 - 02:52]

popular as a modality for learning and manipulation. But then around 2023 some

### [02:52 - 02:52]

manipulation. But then around 2023 some

### [02:52 - 02:53]

manipulation. But then around 2023 some inflection point happened and it became

### [02:53 - 02:53]

inflection point happened and it became

### [02:53 - 02:56]

inflection point happened and it became so successful that it was the impetus

### [02:56 - 02:56]

so successful that it was the impetus

### [02:56 - 02:58]

so successful that it was the impetus for many companies to start scaling

### [02:58 - 02:58]

for many companies to start scaling

### [02:58 - 02:59]

for many companies to start scaling models based on this as a way of

### [02:59 - 02:59]

models based on this as a way of

### [02:59 - 03:01]

models based on this as a way of training their systems.

### [03:01 - 03:01]

training their systems.

### [03:01 - 03:04]

training their systems. So what caused this inflection point?

### [03:04 - 03:04]

So what caused this inflection point?

### [03:04 - 03:06]

So what caused this inflection point? And there's a very stupid answer, which

### [03:06 - 03:06]

And there's a very stupid answer, which

### [03:06 - 03:08]

And there's a very stupid answer, which is this we started collecting more data.

### [03:08 - 03:08]

is this we started collecting more data.

### [03:08 - 03:09]

is this we started collecting more data. And you might call this the pragmatic

### [03:09 - 03:09]

And you might call this the pragmatic

### [03:09 - 03:10]

And you might call this the pragmatic Moravec's paradox, right? That

### [03:10 - 03:10]

Moravec's paradox, right? That

### [03:10 - 03:11]

Moravec's paradox, right? That historically it's been harder to

### [03:11 - 03:11]

historically it's been harder to

### [03:11 - 03:13]

historically it's been harder to instrument data collection for robotics

### [03:13 - 03:13]

instrument data collection for robotics

### [03:13 - 03:14]

instrument data collection for robotics and now where we're at a point where we

### [03:14 - 03:14]

and now where we're at a point where we

### [03:14 - 03:16]

and now where we're at a point where we could start doing it. But I think

### [03:16 - 03:16]

could start doing it. But I think

### [03:16 - 03:18]

could start doing it. But I think there's another point that might be

### [03:18 - 03:18]

there's another point that might be

### [03:18 - 03:19]

there's another point that might be missed, which is that there were certain

### [03:19 - 03:19]

missed, which is that there were certain

### [03:19 - 03:22]

missed, which is that there were certain key algorithmic breakthroughs that took

### [03:22 - 03:22]

key algorithmic breakthroughs that took

### [03:22 - 03:25]

key algorithmic breakthroughs that took place in this 2023 inflection point. And

### [03:25 - 03:25]

place in this 2023 inflection point. And

### [03:25 - 03:26]

place in this 2023 inflection point. And these were the things that enabled us at

### [03:26 - 03:26]

these were the things that enabled us at

### [03:26 - 03:28]

these were the things that enabled us at least at the beginning to start learning

### [03:28 - 03:28]

least at the beginning to start learning

### [03:28 - 03:29]

least at the beginning to start learning from the data we collected even in the

### [03:29 - 03:29]

from the data we collected even in the

### [03:29 - 03:30]

from the data we collected even in the initial efforts which were so much

### [03:30 - 03:30]

initial efforts which were so much

### [03:30 - 03:33]

initial efforts which were so much smaller in scale.

### [03:33 - 03:33]

smaller in scale.

### [03:33 - 03:34]

smaller in scale. Uh so this is the algorithmic Moravec's

### [03:34 - 03:34]

Uh so this is the algorithmic Moravec's

### [03:34 - 03:35]

Uh so this is the algorithmic Moravec's paradox that robot learning is

### [03:35 - 03:35]

paradox that robot learning is

### [03:35 - 03:37]

paradox that robot learning is fundamentally more challenging at least

### [03:37 - 03:37]

fundamentally more challenging at least

### [03:37 - 03:39]

fundamentally more challenging at least at smaller scales until you have a

### [03:39 - 03:39]

at smaller scales until you have a

### [03:39 - 03:41]

at smaller scales until you have a couple key algorithmic choices that

### [03:41 - 03:41]

couple key algorithmic choices that

### [03:41 - 03:42]

couple key algorithmic choices that enable learning from the data that you

### [03:42 - 03:42]

enable learning from the data that you

### [03:42 - 03:43]

enable learning from the data that you collect.

### [03:43 - 03:43]

collect.

### [03:43 - 03:45]

collect. Um and so in this talk we're going to

### [03:45 - 03:45]

Um and so in this talk we're going to

### [03:45 - 03:47]

Um and so in this talk we're going to try to provide some mathematical support

### [03:47 - 03:47]

try to provide some mathematical support

### [03:47 - 03:48]

try to provide some mathematical support for what's going on in this algorithmic

### [03:48 - 03:48]

for what's going on in this algorithmic

### [03:48 - 03:51]

for what's going on in this algorithmic formulation of Moravec's paradox. We're

### [03:51 - 03:51]

formulation of Moravec's paradox. We're

### [03:51 - 03:52]

formulation of Moravec's paradox. We're going to describe why learning from

### [03:52 - 03:52]

going to describe why learning from

### [03:52 - 03:54]

going to describe why learning from demonstration can be fundamentally more

### [03:54 - 03:54]

demonstration can be fundamentally more

### [03:54 - 03:55]

demonstration can be fundamentally more challenging in continuous control

### [03:55 - 03:55]

challenging in continuous control

### [03:55 - 03:56]

challenging in continuous control settings such as those encountered in

### [03:56 - 03:56]

settings such as those encountered in

### [03:56 - 03:59]

settings such as those encountered in robotics as opposed to settings like

### [03:59 - 03:59]

robotics as opposed to settings like

### [03:59 - 04:01]

robotics as opposed to settings like symbolic reasoning like in language. And

### [04:01 - 04:01]

symbolic reasoning like in language. And

### [04:01 - 04:02]

symbolic reasoning like in language. And then we're going to try to explain how

### [04:02 - 04:02]

then we're going to try to explain how

### [04:02 - 04:04]

then we're going to try to explain how those kind of key breakthroughs that

### [04:04 - 04:04]

those kind of key breakthroughs that

### [04:04 - 04:05]

those kind of key breakthroughs that cause this inflection point, they

### [04:05 - 04:05]

cause this inflection point, they

### [04:05 - 04:06]

cause this inflection point, they actually mitigate some of the

### [04:06 - 04:06]

actually mitigate some of the

### [04:06 - 04:08]

actually mitigate some of the fundamental challenges that we

### [04:08 - 04:08]

fundamental challenges that we

### [04:08 - 04:09]

fundamental challenges that we encountered in learning and control

### [04:09 - 04:09]

encountered in learning and control

### [04:09 - 04:11]

encountered in learning and control systems.

### [04:11 - 04:11]

systems.

### [04:11 - 04:12]

systems. So what are the interventions we're

### [04:12 - 04:12]

So what are the interventions we're

### [04:12 - 04:14]

So what are the interventions we're going to talk about? If you do a lot of

### [04:14 - 04:14]

going to talk about? If you do a lot of

### [04:14 - 04:16]

going to talk about? If you do a lot of modern robot manipulation research, you

### [04:16 - 04:16]

modern robot manipulation research, you

### [04:16 - 04:17]

modern robot manipulation research, you may be familiar with these. The first is

### [04:17 - 04:17]

may be familiar with these. The first is

### [04:17 - 04:18]

may be familiar with these. The first is action chunking. This is the process

### [04:18 - 04:18]

action chunking. This is the process

### [04:18 - 04:21]

action chunking. This is the process where you condition on a few historical

### [04:21 - 04:21]

where you condition on a few historical

### [04:21 - 04:22]

where you condition on a few historical observations and predict whole sequences

### [04:22 - 04:22]

observations and predict whole sequences

### [04:22 - 04:24]

observations and predict whole sequences of actions in open loop rather than

### [04:24 - 04:24]

of actions in open loop rather than

### [04:24 - 04:25]

of actions in open loop rather than having a very very high frequency

### [04:25 - 04:25]

having a very very high frequency

### [04:25 - 04:27]

having a very very high frequency reactive policy.

### [04:27 - 04:27]

reactive policy.

### [04:27 - 04:28]

reactive policy. Uh and this is kind of considered one of

### [04:28 - 04:28]

Uh and this is kind of considered one of

### [04:28 - 04:30]

Uh and this is kind of considered one of the foundational innovations. The other

### [04:30 - 04:30]

the foundational innovations. The other

### [04:30 - 04:31]

the foundational innovations. The other that's sometimes more visible is that of

### [04:31 - 04:31]

that's sometimes more visible is that of

### [04:31 - 04:33]

that's sometimes more visible is that of using generative models as

### [04:33 - 04:33]

using generative models as

### [04:33 - 04:34]

using generative models as parameterizations of action

### [04:34 - 04:34]

parameterizations of action

### [04:34 - 04:36]

parameterizations of action distributions. Sort of under the

### [04:36 - 04:36]

distributions. Sort of under the

### [04:36 - 04:37]

distributions. Sort of under the assumption that actions when we collect

### [04:37 - 04:37]

assumption that actions when we collect

### [04:37 - 04:39]

assumption that actions when we collect from diverse human demonstration have

### [04:39 - 04:39]

from diverse human demonstration have

### [04:39 - 04:41]

from diverse human demonstration have multiple modes or diversity in the in

### [04:41 - 04:41]

multiple modes or diversity in the in

### [04:41 - 04:42]

multiple modes or diversity in the in the distribution that we collect. And

### [04:42 - 04:42]

the distribution that we collect. And

### [04:42 - 04:44]

the distribution that we collect. And sort of it's it's suggested that

### [04:44 - 04:44]

sort of it's it's suggested that

### [04:44 - 04:47]

sort of it's it's suggested that generative models are better suited for

### [04:47 - 04:47]

generative models are better suited for

### [04:47 - 04:48]

generative models are better suited for for for modeling this kind of

### [04:48 - 04:48]

for for modeling this kind of

### [04:48 - 04:49]

for for modeling this kind of distribution. Then we're going to see

### [04:49 - 04:49]

distribution. Then we're going to see

### [04:49 - 04:50]

distribution. Then we're going to see that maybe there are other motivations

### [04:50 - 04:50]

that maybe there are other motivations

### [04:50 - 04:52]

that maybe there are other motivations behind using generative models in

### [04:52 - 04:52]

behind using generative models in

### [04:52 - 04:54]

behind using generative models in control at the end of the talk.

### [04:54 - 04:54]

control at the end of the talk.

### [04:54 - 04:56]

control at the end of the talk. So kind of the fundamental claim that

### [04:56 - 04:56]

So kind of the fundamental claim that

### [04:56 - 04:57]

So kind of the fundamental claim that we're going to try to make that unifies

### [04:57 - 04:57]

we're going to try to make that unifies

### [04:57 - 04:59]

we're going to try to make that unifies these decisions is that modern robot

### [04:59 - 04:59]

these decisions is that modern robot

### [04:59 - 05:00]

these decisions is that modern robot learning can be thought about as

### [05:00 - 05:00]

learning can be thought about as

### [05:00 - 05:02]

learning can be thought about as reparameterizing the closed-loop

### [05:02 - 05:02]

reparameterizing the closed-loop

### [05:02 - 05:03]

reparameterizing the closed-loop dynamics between robot and control

### [05:03 - 05:03]

dynamics between robot and control

### [05:03 - 05:06]

dynamics between robot and control system. And that these interventions

### [05:06 - 05:06]

system. And that these interventions

### [05:06 - 05:08]

system. And that these interventions really act on a control level. And in

### [05:08 - 05:08]

really act on a control level. And in

### [05:08 - 05:10]

really act on a control level. And in fact, these reparameterizations are the

### [05:10 - 05:10]

fact, these reparameterizations are the

### [05:10 - 05:11]

fact, these reparameterizations are the things that now put us in a regime where

### [05:11 - 05:11]

things that now put us in a regime where

### [05:11 - 05:13]

things that now put us in a regime where the bitter lesson can take effect and

### [05:13 - 05:13]

the bitter lesson can take effect and

### [05:13 - 05:14]

the bitter lesson can take effect and then the boring pragmatic Moravec's

### [05:14 - 05:14]

then the boring pragmatic Moravec's

### [05:14 - 05:16]

then the boring pragmatic Moravec's paradox, we just need more data, starts

### [05:16 - 05:16]

paradox, we just need more data, starts

### [05:16 - 05:18]

paradox, we just need more data, starts to become more salient.

### [05:18 - 05:18]

to become more salient.

### [05:18 - 05:21]

to become more salient. So to begin I want to explain why

### [05:21 - 05:21]

So to begin I want to explain why

### [05:21 - 05:22]

So to begin I want to explain why behavior cloning can be challenging in

### [05:22 - 05:22]

behavior cloning can be challenging in

### [05:22 - 05:23]

behavior cloning can be challenging in robot learning.

### [05:23 - 05:23]

robot learning.

### [05:23 - 05:25]

robot learning. And I'm going to do that by kind of

### [05:25 - 05:25]

And I'm going to do that by kind of

### [05:25 - 05:27]

And I'm going to do that by kind of first introducing the behavior cloning

### [05:27 - 05:27]

first introducing the behavior cloning

### [05:27 - 05:28]

first introducing the behavior cloning paradigm for those that might not be

### [05:28 - 05:28]

paradigm for those that might not be

### [05:28 - 05:29]

paradigm for those that might not be familiar with it. So we're going to

### [05:29 - 05:29]

familiar with it. So we're going to

### [05:29 - 05:31]

familiar with it. So we're going to operate in a Markov decision process.

### [05:31 - 05:31]

operate in a Markov decision process.

### [05:31 - 05:32]

operate in a Markov decision process. I'm sure many of us are familiar here.

### [05:32 - 05:32]

I'm sure many of us are familiar here.

### [05:32 - 05:34]

I'm sure many of us are familiar here. We have states, we have actions, we have

### [05:34 - 05:34]

We have states, we have actions, we have

### [05:34 - 05:36]

We have states, we have actions, we have transitions between states and actions,

### [05:36 - 05:36]

transitions between states and actions,

### [05:36 - 05:37]

transitions between states and actions, we have rewards, and we have an initial

### [05:37 - 05:37]

we have rewards, and we have an initial

### [05:37 - 05:40]

we have rewards, and we have an initial distribution over initial conditions. Uh

### [05:40 - 05:40]

distribution over initial conditions. Uh

### [05:40 - 05:41]

distribution over initial conditions. Uh we also have a problem horizon. That's

### [05:41 - 05:41]

we also have a problem horizon. That's

### [05:41 - 05:43]

we also have a problem horizon. That's the number of steps that the actor, for

### [05:43 - 05:43]

the number of steps that the actor, for

### [05:43 - 05:45]

the number of steps that the actor, for example our robot, might take. And the

### [05:45 - 05:45]

example our robot, might take. And the

### [05:45 - 05:46]

example our robot, might take. And the problem horizon will become really

### [05:46 - 05:46]

problem horizon will become really

### [05:46 - 05:48]

problem horizon will become really important in today's talk.

### [05:48 - 05:48]

important in today's talk.

### [05:48 - 05:50]

important in today's talk. So the key object is a policy. It's just

### [05:50 - 05:50]

So the key object is a policy. It's just

### [05:50 - 05:51]

So the key object is a policy. It's just a way of describing what your agent

### [05:51 - 05:51]

a way of describing what your agent

### [05:51 - 05:53]

a way of describing what your agent does. It's a mapping from states to the

### [05:53 - 05:53]

does. It's a mapping from states to the

### [05:53 - 05:55]

does. It's a mapping from states to the distributions over actions.

### [05:55 - 05:55]

distributions over actions.

### [05:55 - 05:56]

distributions over actions. Uh and that can be either describe what

### [05:56 - 05:56]

Uh and that can be either describe what

### [05:56 - 05:58]

Uh and that can be either describe what your robot is doing, but also policies

### [05:58 - 05:58]

your robot is doing, but also policies

### [05:58 - 05:59]

your robot is doing, but also policies have been used to formalize language

### [05:59 - 05:59]

have been used to formalize language

### [05:59 - 06:00]

have been used to formalize language models. For example, a language model

### [06:00 - 06:00]

models. For example, a language model

### [06:00 - 06:02]

models. For example, a language model can be thought of as a policy which

### [06:02 - 06:02]

can be thought of as a policy which

### [06:02 - 06:03]

can be thought of as a policy which takes in a context of tokens and spits

### [06:03 - 06:03]

takes in a context of tokens and spits

### [06:03 - 06:05]

takes in a context of tokens and spits out another token as its actions. And

### [06:05 - 06:05]

out another token as its actions. And

### [06:05 - 06:07]

out another token as its actions. And the dynamics are just concatenation to

### [06:07 - 06:07]

the dynamics are just concatenation to

### [06:07 - 06:08]

the dynamics are just concatenation to the context.

### [06:08 - 06:08]

the context.

### [06:08 - 06:10]

the context. So what are we trying to do? Well, we're

### [06:10 - 06:10]

So what are we trying to do? Well, we're

### [06:10 - 06:12]

So what are we trying to do? Well, we're trying to maximize reward, at least for

### [06:12 - 06:12]

trying to maximize reward, at least for

### [06:12 - 06:14]

trying to maximize reward, at least for today. So the we'll define the reward of

### [06:14 - 06:14]

today. So the we'll define the reward of

### [06:14 - 06:16]

today. So the we'll define the reward of a policy is just the expectation of its

### [06:16 - 06:16]

a policy is just the expectation of its

### [06:16 - 06:18]

a policy is just the expectation of its cumulative reward. Where that

### [06:18 - 06:18]

cumulative reward. Where that

### [06:18 - 06:20]

cumulative reward. Where that expectation happens by drawing initial

### [06:20 - 06:20]

expectation happens by drawing initial

### [06:20 - 06:22]

expectation happens by drawing initial conditions, then choosing actions

### [06:22 - 06:22]

conditions, then choosing actions

### [06:22 - 06:24]

conditions, then choosing actions according to our policy, and finally

### [06:24 - 06:24]

according to our policy, and finally

### [06:24 - 06:25]

according to our policy, and finally transitioning according to the

### [06:25 - 06:25]

transitioning according to the

### [06:25 - 06:28]

transitioning according to the transition dynamics of our MDP.

### [06:28 - 06:28]

transition dynamics of our MDP.

### [06:28 - 06:30]

transition dynamics of our MDP. And so offline, before I describe

### [06:30 - 06:30]

And so offline, before I describe

### [06:30 - 06:31]

And so offline, before I describe behavior cloning, I want to describe the

### [06:31 - 06:31]

behavior cloning, I want to describe the

### [06:31 - 06:33]

behavior cloning, I want to describe the protocol, which is sort of like the

### [06:33 - 06:33]

protocol, which is sort of like the

### [06:33 - 06:34]

protocol, which is sort of like the world in which behavior cloning exists.

### [06:34 - 06:34]

world in which behavior cloning exists.

### [06:34 - 06:35]

world in which behavior cloning exists. So what we're going to do is we're going

### [06:35 - 06:35]

So what we're going to do is we're going

### [06:35 - 06:38]

So what we're going to do is we're going to assume that the expert, our human,

### [06:38 - 06:38]

to assume that the expert, our human,

### [06:38 - 06:40]

to assume that the expert, our human, collects data and gives that data to the

### [06:40 - 06:40]

collects data and gives that data to the

### [06:40 - 06:42]

collects data and gives that data to the robot, right? So that data can be

### [06:42 - 06:42]

robot, right? So that data can be

### [06:42 - 06:43]

robot, right? So that data can be sequences of trajectories consisting of

### [06:43 - 06:43]

sequences of trajectories consisting of

### [06:43 - 06:45]

sequences of trajectories consisting of states and actions. For the roboticists

### [06:45 - 06:45]

states and actions. For the roboticists

### [06:45 - 06:46]

states and actions. For the roboticists in the room, which are many of you, we

### [06:46 - 06:46]

in the room, which are many of you, we

### [06:46 - 06:48]

in the room, which are many of you, we know we don't actually get state, we get

### [06:48 - 06:48]

know we don't actually get state, we get

### [06:48 - 06:49]

know we don't actually get state, we get observation. But today we're going to

### [06:49 - 06:49]

observation. But today we're going to

### [06:49 - 06:50]

observation. But today we're going to focus on state because if things are

### [06:50 - 06:50]

focus on state because if things are

### [06:50 - 06:52]

focus on state because if things are challenging in state-based control, nine

### [06:52 - 06:52]

challenging in state-based control, nine

### [06:52 - 06:54]

challenging in state-based control, nine times out of 10, not always 10 times out

### [06:54 - 06:54]

times out of 10, not always 10 times out

### [06:54 - 06:55]

times out of 10, not always 10 times out of 10, they're they're challenging in

### [06:55 - 06:55]

of 10, they're they're challenging in

### [06:55 - 06:57]

of 10, they're they're challenging in image-based. Turns out sometimes

### [06:57 - 06:57]

image-based. Turns out sometimes

### [06:57 - 06:58]

image-based. Turns out sometimes image-based can be easier for weird

### [06:58 - 06:58]

image-based can be easier for weird

### [06:58 - 07:00]

image-based can be easier for weird reasons. But uh we'll work on

### [07:00 - 07:00]

reasons. But uh we'll work on

### [07:00 - 07:01]

reasons. But uh we'll work on state-based control today. And so we're

### [07:01 - 07:01]

state-based control today. And so we're

### [07:01 - 07:02]

state-based control today. And so we're going to give those trajectories to an

### [07:02 - 07:02]

going to give those trajectories to an

### [07:02 - 07:04]

going to give those trajectories to an imitator and the imitator is going to do

### [07:04 - 07:04]

imitator and the imitator is going to do

### [07:04 - 07:06]

imitator and the imitator is going to do some algorithm, which we'll describe,

### [07:06 - 07:06]

some algorithm, which we'll describe,

### [07:06 - 07:07]

some algorithm, which we'll describe, which is going to try to return some new

### [07:07 - 07:07]

which is going to try to return some new

### [07:07 - 07:09]

which is going to try to return some new policy that has the following property.

### [07:09 - 07:09]

policy that has the following property.

### [07:09 - 07:11]

policy that has the following property. The property should be that that

### [07:11 - 07:11]

The property should be that that

### [07:11 - 07:13]

The property should be that that the cumulative reward of that policy, J

### [07:13 - 07:13]

the cumulative reward of that policy, J

### [07:13 - 07:16]

the cumulative reward of that policy, J of pi hat, should only be a little bit

### [07:16 - 07:16]

of pi hat, should only be a little bit

### [07:16 - 07:17]

of pi hat, should only be a little bit less than the cumulative reward of what

### [07:17 - 07:17]

less than the cumulative reward of what

### [07:17 - 07:19]

less than the cumulative reward of what our expert gets. So smaller than some

### [07:19 - 07:19]

our expert gets. So smaller than some

### [07:19 - 07:20]

our expert gets. So smaller than some number epsilon and here epsilon is just

### [07:20 - 07:20]

number epsilon and here epsilon is just

### [07:20 - 07:22]

number epsilon and here epsilon is just getting smaller and smaller as I collect

### [07:22 - 07:22]

getting smaller and smaller as I collect

### [07:22 - 07:23]

getting smaller and smaller as I collect more data, right? That's what we would

### [07:23 - 07:23]

more data, right? That's what we would

### [07:23 - 07:24]

more data, right? That's what we would like to have happen.

### [07:24 - 07:24]

like to have happen.

### [07:24 - 07:27]

like to have happen. Now, how can we achieve this? Well,

### [07:27 - 07:27]

Now, how can we achieve this? Well,

### [07:27 - 07:29]

Now, how can we achieve this? Well, behavior cloning is one algorithm that

### [07:29 - 07:29]

behavior cloning is one algorithm that

### [07:29 - 07:30]

behavior cloning is one algorithm that abides by the protocol of learning from

### [07:30 - 07:30]

abides by the protocol of learning from

### [07:30 - 07:32]

abides by the protocol of learning from an expert. So in behavior cloning, you

### [07:32 - 07:32]

an expert. So in behavior cloning, you

### [07:32 - 07:34]

an expert. So in behavior cloning, you just use supervised learning to train

### [07:34 - 07:34]

just use supervised learning to train

### [07:34 - 07:36]

just use supervised learning to train your policy. So more specifically, what

### [07:36 - 07:36]

your policy. So more specifically, what

### [07:36 - 07:37]

your policy. So more specifically, what you'll do is you'll take all your expert

### [07:37 - 07:37]

you'll do is you'll take all your expert

### [07:37 - 07:38]

you'll do is you'll take all your expert data.

### [07:38 - 07:38]

data.

### [07:38 - 07:40]

data. You'll specify some loss function that's

### [07:40 - 07:40]

You'll specify some loss function that's

### [07:40 - 07:42]

You'll specify some loss function that's related to how you describe your policy.

### [07:42 - 07:42]

related to how you describe your policy.

### [07:42 - 07:44]

related to how you describe your policy. And then you'll try to find the policy

### [07:44 - 07:44]

And then you'll try to find the policy

### [07:44 - 07:45]

And then you'll try to find the policy which minimizes this loss on the data

### [07:45 - 07:45]

which minimizes this loss on the data

### [07:45 - 07:47]

which minimizes this loss on the data that you have, for example by doing

### [07:47 - 07:47]

that you have, for example by doing

### [07:47 - 07:49]

that you have, for example by doing gradient descent on some architecture of

### [07:49 - 07:49]

gradient descent on some architecture of

### [07:49 - 07:51]

gradient descent on some architecture of neural networks.

### [07:51 - 07:51]

neural networks.

### [07:51 - 07:53]

neural networks. And um

### [07:53 - 07:53]

And um

### [07:53 - 07:54]

And um the reason we do this is because there's

### [07:54 - 07:54]

the reason we do this is because there's

### [07:54 - 07:55]

the reason we do this is because there's lots of reasons why we want to do

### [07:55 - 07:55]

lots of reasons why we want to do

### [07:55 - 07:56]

lots of reasons why we want to do supervised learning. It's an algorithm

### [07:56 - 07:56]

supervised learning. It's an algorithm

### [07:56 - 07:58]

supervised learning. It's an algorithm that's very easy to learn.

### [07:58 - 07:58]

that's very easy to learn.

### [07:58 - 08:00]

that's very easy to learn. It's empirically works very very well,

### [08:00 - 08:00]

It's empirically works very very well,

### [08:00 - 08:02]

It's empirically works very very well, right? Like image classification, these

### [08:02 - 08:02]

right? Like image classification, these

### [08:02 - 08:03]

right? Like image classification, these sorts of things. And theoretically it

### [08:03 - 08:03]

sorts of things. And theoretically it

### [08:03 - 08:05]

sorts of things. And theoretically it also is nice. We have very strong strong

### [08:05 - 08:05]

also is nice. We have very strong strong

### [08:05 - 08:06]

also is nice. We have very strong strong history of generalization error

### [08:06 - 08:06]

history of generalization error

### [08:06 - 08:08]

history of generalization error guarantees that say that if I minimize

### [08:08 - 08:08]

guarantees that say that if I minimize

### [08:08 - 08:10]

guarantees that say that if I minimize this loss on my expert data, then the

### [08:10 - 08:10]

this loss on my expert data, then the

### [08:10 - 08:11]

this loss on my expert data, then the thing that minimizes it will be close to

### [08:11 - 08:11]

thing that minimizes it will be close to

### [08:11 - 08:13]

thing that minimizes it will be close to the expert, the global minimizer under

### [08:13 - 08:13]

the expert, the global minimizer under

### [08:13 - 08:15]

the expert, the global minimizer under certain conditions.

### [08:15 - 08:15]

certain conditions.

### [08:15 - 08:17]

certain conditions. But the problem is this is just because

### [08:17 - 08:17]

But the problem is this is just because

### [08:17 - 08:19]

But the problem is this is just because we can minimize the supervised learning

### [08:19 - 08:19]

we can minimize the supervised learning

### [08:19 - 08:21]

we can minimize the supervised learning error does not a priori imply that we're

### [08:21 - 08:21]

error does not a priori imply that we're

### [08:21 - 08:23]

error does not a priori imply that we're going to get small reward. And the I

### [08:23 - 08:23]

going to get small reward. And the I

### [08:23 - 08:24]

going to get small reward. And the I think the best way to see this is is

### [08:24 - 08:24]

think the best way to see this is is

### [08:24 - 08:26]

think the best way to see this is is through visualizing it. So by minimizing

### [08:26 - 08:26]

through visualizing it. So by minimizing

### [08:26 - 08:28]

through visualizing it. So by minimizing supervised error, we're doing it under

### [08:28 - 08:28]

supervised error, we're doing it under

### [08:28 - 08:30]

supervised error, we're doing it under the distribution of our states that our

### [08:30 - 08:30]

the distribution of our states that our

### [08:30 - 08:32]

the distribution of our states that our expert visits, right? So at every state

### [08:32 - 08:32]

expert visits, right? So at every state

### [08:32 - 08:33]

expert visits, right? So at every state that we see, we're trying to find an

### [08:33 - 08:33]

that we see, we're trying to find an

### [08:33 - 08:35]

that we see, we're trying to find an action that's close to what the expert

### [08:35 - 08:35]

action that's close to what the expert

### [08:35 - 08:37]

action that's close to what the expert would have done anchored at that state.

### [08:37 - 08:37]

would have done anchored at that state.

### [08:37 - 08:38]

would have done anchored at that state. But of course, when we deploy the

### [08:38 - 08:38]

But of course, when we deploy the

### [08:38 - 08:40]

But of course, when we deploy the policy, we're taking actions from the

### [08:40 - 08:40]

policy, we're taking actions from the

### [08:40 - 08:42]

policy, we're taking actions from the states that we reach. And these actions

### [08:42 - 08:42]

states that we reach. And these actions

### [08:42 - 08:44]

states that we reach. And these actions can cause errors which add up over time,

### [08:44 - 08:44]

can cause errors which add up over time,

### [08:44 - 08:45]

can cause errors which add up over time, often leading to what's called the curse

### [08:45 - 08:45]

often leading to what's called the curse

### [08:45 - 08:47]

often leading to what's called the curse of horizon where errors grow as the

### [08:47 - 08:47]

of horizon where errors grow as the

### [08:47 - 08:49]

of horizon where errors grow as the horizon grows.

### [08:49 - 08:49]

horizon grows.

### [08:49 - 08:51]

horizon grows. So this is the fundamental challenge.

### [08:51 - 08:51]

So this is the fundamental challenge.

### [08:51 - 08:53]

So this is the fundamental challenge. So how bad is this curse of horizon?

### [08:53 - 08:53]

So how bad is this curse of horizon?

### [08:53 - 08:54]

So how bad is this curse of horizon? Well, let's start by considering the

### [08:54 - 08:54]

Well, let's start by considering the

### [08:54 - 08:55]

Well, let's start by considering the case where we're doing like a discrete

### [08:55 - 08:55]

case where we're doing like a discrete

### [08:55 - 08:57]

case where we're doing like a discrete task like symbolic reasoning in

### [08:57 - 08:57]

task like symbolic reasoning in

### [08:57 - 08:58]

task like symbolic reasoning in language. And we'll consider a very

### [08:58 - 08:58]

language. And we'll consider a very

### [08:58 - 09:00]

language. And we'll consider a very special case of the zero-one loss. So

### [09:00 - 09:00]

special case of the zero-one loss. So

### [09:00 - 09:02]

special case of the zero-one loss. So this is a loss that gives you a penalty

### [09:02 - 09:02]

this is a loss that gives you a penalty

### [09:02 - 09:03]

this is a loss that gives you a penalty of one if you get the wrong action.

### [09:03 - 09:03]

of one if you get the wrong action.

### [09:03 - 09:04]

of one if you get the wrong action. Let's say you predict the wrong token

### [09:04 - 09:04]

Let's say you predict the wrong token

### [09:04 - 09:06]

Let's say you predict the wrong token and zero otherwise. Now in modern

### [09:06 - 09:06]

and zero otherwise. Now in modern

### [09:06 - 09:07]

and zero otherwise. Now in modern language modeling actually we use the

### [09:07 - 09:07]

language modeling actually we use the

### [09:07 - 09:09]

language modeling actually we use the log loss, we use cross entropy. It

### [09:09 - 09:09]

log loss, we use cross entropy. It

### [09:09 - 09:11]

log loss, we use cross entropy. It actually turns out this works even

### [09:11 - 09:11]

actually turns out this works even

### [09:11 - 09:12]

actually turns out this works even better than the zero-one loss and I'm

### [09:12 - 09:12]

better than the zero-one loss and I'm

### [09:12 - 09:14]

better than the zero-one loss and I'm not going to go into that that that

### [09:14 - 09:14]

not going to go into that that that

### [09:14 - 09:15]

not going to go into that that that research today. But we'll focus on the

### [09:15 - 09:15]

research today. But we'll focus on the

### [09:15 - 09:18]

research today. But we'll focus on the zero-one loss for now.

### [09:18 - 09:18]

zero-one loss for now.

### [09:18 - 09:19]

zero-one loss for now. So what you can show, actually this is

### [09:19 - 09:19]

So what you can show, actually this is

### [09:19 - 09:21]

So what you can show, actually this is an old result due to Drew Bagnell who is

### [09:21 - 09:21]

an old result due to Drew Bagnell who is

### [09:21 - 09:24]

an old result due to Drew Bagnell who is I think still affiliated with CMU,

### [09:24 - 09:24]

I think still affiliated with CMU,

### [09:24 - 09:26]

I think still affiliated with CMU, is that the compounding error effect,

### [09:26 - 09:26]

is that the compounding error effect,

### [09:26 - 09:28]

is that the compounding error effect, the suboptimality that you get in terms

### [09:28 - 09:28]

the suboptimality that you get in terms

### [09:28 - 09:30]

the suboptimality that you get in terms of your reward, is at most horizon

### [09:30 - 09:30]

of your reward, is at most horizon

### [09:30 - 09:33]

of your reward, is at most horizon factor times the suboptimality that you

### [09:33 - 09:33]

factor times the suboptimality that you

### [09:33 - 09:35]

factor times the suboptimality that you get in your behavior cloning loss. So

### [09:35 - 09:35]

get in your behavior cloning loss. So

### [09:35 - 09:37]

get in your behavior cloning loss. So essentially we do have some curse of

### [09:37 - 09:37]

essentially we do have some curse of

### [09:37 - 09:39]

essentially we do have some curse of horizon, but it's relatively mild. It's

### [09:39 - 09:39]

horizon, but it's relatively mild. It's

### [09:39 - 09:40]

horizon, but it's relatively mild. It's at most linear in how long the problem

### [09:40 - 09:40]

at most linear in how long the problem

### [09:40 - 09:42]

at most linear in how long the problem takes. And the intuition for this is

### [09:42 - 09:42]

takes. And the intuition for this is

### [09:42 - 09:44]

takes. And the intuition for this is that if you have a zero-one loss, you

### [09:44 - 09:44]

that if you have a zero-one loss, you

### [09:44 - 09:46]

that if you have a zero-one loss, you either make a mistake or you don't. And

### [09:46 - 09:46]

either make a mistake or you don't. And

### [09:46 - 09:47]

either make a mistake or you don't. And so at every time step there's some

### [09:47 - 09:47]

so at every time step there's some

### [09:47 - 09:48]

so at every time step there's some probability of making a mistake and

### [09:48 - 09:48]

probability of making a mistake and

### [09:48 - 09:50]

probability of making a mistake and those probabilities accumulate according

### [09:50 - 09:50]

those probabilities accumulate according

### [09:50 - 09:52]

those probabilities accumulate according to the length of the horizon, but

### [09:52 - 09:52]

to the length of the horizon, but

### [09:52 - 09:53]

to the length of the horizon, but otherwise you don't make a mistake and

### [09:53 - 09:53]

otherwise you don't make a mistake and

### [09:53 - 09:55]

otherwise you don't make a mistake and you do perfectly and do exactly what the

### [09:55 - 09:55]

you do perfectly and do exactly what the

### [09:55 - 09:57]

you do perfectly and do exactly what the expert would do. So it's not so bad in

### [09:57 - 09:57]

expert would do. So it's not so bad in

### [09:57 - 09:59]

expert would do. So it's not so bad in this case in the discrete setting.

### [09:59 - 09:59]

this case in the discrete setting.

### [09:59 - 10:00]

this case in the discrete setting. But, now we're going to work in control

### [10:00 - 10:00]

But, now we're going to work in control

### [10:00 - 10:01]

But, now we're going to work in control systems. So, in a control system, we'll

### [10:01 - 10:01]

systems. So, in a control system, we'll

### [10:01 - 10:04]

systems. So, in a control system, we'll work on a special kind of MDP where we

### [10:04 - 10:04]

work on a special kind of MDP where we

### [10:04 - 10:05]

work on a special kind of MDP where we have continuous states and continuous

### [10:05 - 10:05]

have continuous states and continuous

### [10:05 - 10:07]

have continuous states and continuous actions. So, we're in the continuous

### [10:07 - 10:07]

actions. So, we're in the continuous

### [10:07 - 10:09]

actions. So, we're in the continuous world. Uh transition dynamics will be

### [10:09 - 10:09]

world. Uh transition dynamics will be

### [10:09 - 10:11]

world. Uh transition dynamics will be given by deterministic dynamical system

### [10:11 - 10:11]

given by deterministic dynamical system

### [10:11 - 10:13]

given by deterministic dynamical system denoted by F. And again, we have

### [10:13 - 10:13]

denoted by F. And again, we have

### [10:13 - 10:15]

denoted by F. And again, we have rewards, initial state distributions.

### [10:15 - 10:15]

rewards, initial state distributions.

### [10:15 - 10:16]

rewards, initial state distributions. And in particular, kind of the salient

### [10:16 - 10:16]

And in particular, kind of the salient

### [10:16 - 10:17]

And in particular, kind of the salient thing is now our states and actions are

### [10:17 - 10:17]

thing is now our states and actions are

### [10:17 - 10:19]

thing is now our states and actions are continuous valued. And we'll see why

### [10:19 - 10:19]

continuous valued. And we'll see why

### [10:19 - 10:21]

continuous valued. And we'll see why that's a problem.

### [10:21 - 10:21]

that's a problem.

### [10:21 - 10:22]

that's a problem. So, for today's talk, because we want to

### [10:22 - 10:22]

So, for today's talk, because we want to

### [10:22 - 10:24]

So, for today's talk, because we want to prove negative results at least to

### [10:24 - 10:24]

prove negative results at least to

### [10:24 - 10:25]

prove negative results at least to start, we're going to work in the

### [10:25 - 10:25]

start, we're going to work in the

### [10:25 - 10:26]

start, we're going to work in the simplest setting where the dynamics are

### [10:26 - 10:26]

simplest setting where the dynamics are

### [10:26 - 10:28]

simplest setting where the dynamics are deterministic and the policy optimal

### [10:28 - 10:28]

deterministic and the policy optimal

### [10:28 - 10:30]

deterministic and the policy optimal policy are smooth. So, smooth just means

### [10:30 - 10:30]

policy are smooth. So, smooth just means

### [10:30 - 10:31]

policy are smooth. So, smooth just means that they have derivatives and those

### [10:31 - 10:31]

that they have derivatives and those

### [10:31 - 10:35]

that they have derivatives and those derivatives are kind of continuous.

### [10:35 - 10:35]

derivatives are kind of continuous.

### [10:35 - 10:37]

derivatives are kind of continuous. So, let's do behavior cloning in this

### [10:37 - 10:37]

So, let's do behavior cloning in this

### [10:37 - 10:38]

So, let's do behavior cloning in this setting.

### [10:38 - 10:38]

setting.

### [10:38 - 10:40]

setting. Now, the problem is this. If we assume

### [10:40 - 10:40]

Now, the problem is this. If we assume

### [10:40 - 10:41]

Now, the problem is this. If we assume that we're in continuous state action

### [10:41 - 10:41]

that we're in continuous state action

### [10:41 - 10:43]

that we're in continuous state action spaces, we can't learn in the 0-1 loss

### [10:43 - 10:43]

spaces, we can't learn in the 0-1 loss

### [10:43 - 10:45]

spaces, we can't learn in the 0-1 loss or the log loss. The reason being that

### [10:45 - 10:45]

or the log loss. The reason being that

### [10:45 - 10:47]

or the log loss. The reason being that we'll always make some irreducible

### [10:47 - 10:47]

we'll always make some irreducible

### [10:47 - 10:48]

we'll always make some irreducible amount of error, right? We can always

### [10:48 - 10:48]

amount of error, right? We can always

### [10:48 - 10:49]

amount of error, right? We can always try to get closer and closer to the

### [10:49 - 10:49]

try to get closer and closer to the

### [10:49 - 10:51]

try to get closer and closer to the perfect action, but we might not get

### [10:51 - 10:51]

perfect action, but we might not get

### [10:51 - 10:53]

perfect action, but we might not get that exactly correct.

### [10:53 - 10:53]

that exactly correct.

### [10:53 - 10:54]

that exactly correct. So, instead what we'll do is we'll just

### [10:54 - 10:54]

So, instead what we'll do is we'll just

### [10:54 - 10:56]

So, instead what we'll do is we'll just work on learning in the square loss,

### [10:56 - 10:56]

work on learning in the square loss,

### [10:56 - 10:57]

work on learning in the square loss, which is historically how behavior

### [10:57 - 10:57]

which is historically how behavior

### [10:57 - 10:59]

which is historically how behavior cloning had been conducted up until the

### [10:59 - 10:59]

cloning had been conducted up until the

### [10:59 - 11:00]

cloning had been conducted up until the recent revolution in generative control

### [11:00 - 11:00]

recent revolution in generative control

### [11:00 - 11:02]

recent revolution in generative control policies. And the reason we do this is

### [11:02 - 11:02]

policies. And the reason we do this is

### [11:02 - 11:04]

policies. And the reason we do this is because, well, this is something that at

### [11:04 - 11:04]

because, well, this is something that at

### [11:04 - 11:06]

because, well, this is something that at least is learnable. There's sort of um

### [11:06 - 11:06]

least is learnable. There's sort of um

### [11:06 - 11:07]

least is learnable. There's sort of um very strong empirical evidence and sort

### [11:07 - 11:07]

very strong empirical evidence and sort

### [11:07 - 11:09]

very strong empirical evidence and sort of rich theoretical evidence suggesting

### [11:09 - 11:09]

of rich theoretical evidence suggesting

### [11:09 - 11:11]

of rich theoretical evidence suggesting that learning in the square loss isn't

### [11:11 - 11:11]

that learning in the square loss isn't

### [11:11 - 11:13]

that learning in the square loss isn't so bad.

### [11:13 - 11:13]

so bad.

### [11:13 - 11:14]

so bad. So, what we're going to ask is if I can

### [11:14 - 11:14]

So, what we're going to ask is if I can

### [11:14 - 11:16]

So, what we're going to ask is if I can learn in the square loss, is it possible

### [11:16 - 11:16]

learn in the square loss, is it possible

### [11:16 - 11:18]

learn in the square loss, is it possible for me to do behavior cloning without

### [11:18 - 11:18]

for me to do behavior cloning without

### [11:18 - 11:20]

for me to do behavior cloning without this without significant compounding

### [11:20 - 11:20]

this without significant compounding

### [11:20 - 11:22]

this without significant compounding error?

### [11:22 - 11:22]

error?

### [11:22 - 11:23]

error? So, let me convince you that this is

### [11:23 - 11:23]

So, let me convince you that this is

### [11:23 - 11:24]

So, let me convince you that this is actually hard.

### [11:24 - 11:24]

actually hard.

### [11:24 - 11:25]

actually hard. And in order to do so, I need to

### [11:25 - 11:25]

And in order to do so, I need to

### [11:25 - 11:27]

And in order to do so, I need to convince you that this is hard even in a

### [11:27 - 11:27]

convince you that this is hard even in a

### [11:27 - 11:29]

convince you that this is hard even in a regime that seems like it's very easy

### [11:29 - 11:29]

regime that seems like it's very easy

### [11:29 - 11:31]

regime that seems like it's very easy and seems like it should be really nice.

### [11:31 - 11:31]

and seems like it should be really nice.

### [11:31 - 11:33]

and seems like it should be really nice. So, let me describe that regime to you.

### [11:33 - 11:33]

So, let me describe that regime to you.

### [11:33 - 11:35]

So, let me describe that regime to you. The learner is given a set of possible

### [11:35 - 11:35]

The learner is given a set of possible

### [11:35 - 11:36]

The learner is given a set of possible worlds, and in each possible world,

### [11:36 - 11:36]

worlds, and in each possible world,

### [11:36 - 11:38]

worlds, and in each possible world, there's an expert pi and a dynamics,

### [11:38 - 11:38]

there's an expert pi and a dynamics,

### [11:38 - 11:40]

there's an expert pi and a dynamics, right? So, the the policy is tailored

### [11:40 - 11:40]

right? So, the the policy is tailored

### [11:40 - 11:42]

right? So, the the policy is tailored for the dynamics.

### [11:42 - 11:42]

for the dynamics.

### [11:42 - 11:44]

for the dynamics. In addition, uh for every pair of these,

### [11:44 - 11:44]

In addition, uh for every pair of these,

### [11:44 - 11:46]

In addition, uh for every pair of these, all the policies are smooth, they're

### [11:46 - 11:46]

all the policies are smooth, they're

### [11:46 - 11:48]

all the policies are smooth, they're deterministic, they're Markovian, just

### [11:48 - 11:48]

deterministic, they're Markovian, just

### [11:48 - 11:50]

deterministic, they're Markovian, just meaning that the policies depend only on

### [11:50 - 11:50]

meaning that the policies depend only on

### [11:50 - 11:51]

meaning that the policies depend only on the current state.

### [11:51 - 11:51]

the current state.

### [11:51 - 11:53]

the current state. And finally, they're stable.

### [11:53 - 11:53]

And finally, they're stable.

### [11:53 - 11:55]

And finally, they're stable. Now, stable is a control theoretic

### [11:55 - 11:55]

Now, stable is a control theoretic

### [11:55 - 11:56]

Now, stable is a control theoretic condition that we'll describe a little

### [11:56 - 11:56]

condition that we'll describe a little

### [11:56 - 11:57]

condition that we'll describe a little bit more in detail after we go through

### [11:57 - 11:57]

bit more in detail after we go through

### [11:57 - 11:59]

bit more in detail after we go through the result, but informally, you can

### [11:59 - 11:59]

the result, but informally, you can

### [11:59 - 12:00]

the result, but informally, you can think of stability as saying that if you

### [12:00 - 12:00]

think of stability as saying that if you

### [12:00 - 12:02]

think of stability as saying that if you make a mistake, you forget it really

### [12:02 - 12:02]

make a mistake, you forget it really

### [12:02 - 12:04]

make a mistake, you forget it really fast. So, the thing to visualize is a

### [12:04 - 12:04]

fast. So, the thing to visualize is a

### [12:04 - 12:06]

fast. So, the thing to visualize is a pendulum that has a little bit of

### [12:06 - 12:06]

pendulum that has a little bit of

### [12:06 - 12:07]

pendulum that has a little bit of friction. If I perturb it, eventually

### [12:07 - 12:07]

friction. If I perturb it, eventually

### [12:07 - 12:09]

friction. If I perturb it, eventually the oscillations will relax back to the

### [12:09 - 12:09]

the oscillations will relax back to the

### [12:09 - 12:10]

the oscillations will relax back to the equilibrium point, and you should keep

### [12:10 - 12:10]

equilibrium point, and you should keep

### [12:10 - 12:12]

equilibrium point, and you should keep that in mind when you hear the word

### [12:12 - 12:12]

that in mind when you hear the word

### [12:12 - 12:14]

that in mind when you hear the word stability.

### [12:16 - 12:16]

So, the last thing we're going to assume

### [12:16 - 12:17]

So, the last thing we're going to assume is that the learner is promised that the

### [12:17 - 12:17]

is that the learner is promised that the

### [12:17 - 12:19]

is that the learner is promised that the true policy and the true dynamics, they

### [12:19 - 12:19]

true policy and the true dynamics, they

### [12:19 - 12:21]

true policy and the true dynamics, they lie in the set of possible worlds that

### [12:21 - 12:21]

lie in the set of possible worlds that

### [12:21 - 12:22]

lie in the set of possible worlds that they know.

### [12:22 - 12:22]

they know.

### [12:22 - 12:24]

they know. So, they'll be able to represent this.

### [12:24 - 12:24]

So, they'll be able to represent this.

### [12:24 - 12:26]

So, they'll be able to represent this. Right. So, we can think of these

### [12:26 - 12:26]

Right. So, we can think of these

### [12:26 - 12:28]

Right. So, we can think of these conditions 1 through 3 as specifying one

### [12:28 - 12:28]

conditions 1 through 3 as specifying one

### [12:28 - 12:30]

conditions 1 through 3 as specifying one of the nicest possible behavior cloning

### [12:30 - 12:30]

of the nicest possible behavior cloning

### [12:30 - 12:32]

of the nicest possible behavior cloning instances. Ones where it's easy to

### [12:32 - 12:32]

instances. Ones where it's easy to

### [12:32 - 12:33]

instances. Ones where it's easy to learn, we know what we need to learn,

### [12:33 - 12:33]

learn, we know what we need to learn,

### [12:33 - 12:35]

learn, we know what we need to learn, and we shouldn't have this we shouldn't

### [12:35 - 12:35]

and we shouldn't have this we shouldn't

### [12:35 - 12:37]

and we shouldn't have this we shouldn't have very strong sensitivity if we make

### [12:37 - 12:37]

have very strong sensitivity if we make

### [12:37 - 12:38]

have very strong sensitivity if we make mistakes given by the stability

### [12:38 - 12:38]

mistakes given by the stability

### [12:38 - 12:40]

mistakes given by the stability condition.

### [12:40 - 12:40]

condition.

### [12:40 - 12:41]

condition. We're going to now impose a fourth

### [12:41 - 12:41]

We're going to now impose a fourth

### [12:41 - 12:42]

We're going to now impose a fourth condition,

### [12:42 - 12:42]

condition,

### [12:42 - 12:43]

condition, which is just going to say that the

### [12:43 - 12:43]

which is just going to say that the

### [12:43 - 12:45]

which is just going to say that the learner can't return policies that are

### [12:45 - 12:45]

learner can't return policies that are

### [12:45 - 12:47]

learner can't return policies that are much more sophisticated than what the

### [12:47 - 12:47]

much more sophisticated than what the

### [12:47 - 12:48]

much more sophisticated than what the expert is doing.

### [12:48 - 12:48]

expert is doing.

### [12:48 - 12:49]

expert is doing. And later on, we'll see how removing

### [12:49 - 12:49]

And later on, we'll see how removing

### [12:49 - 12:51]

And later on, we'll see how removing this condition actually enables behavior

### [12:51 - 12:51]

this condition actually enables behavior

### [12:51 - 12:52]

this condition actually enables behavior cloning.

### [12:52 - 12:52]

cloning.

### [12:52 - 12:53]

cloning. So, formally, we remember that we assume

### [12:53 - 12:53]

So, formally, we remember that we assume

### [12:53 - 12:55]

So, formally, we remember that we assume that this expert is Markovian, only

### [12:55 - 12:55]

that this expert is Markovian, only

### [12:55 - 12:56]

that this expert is Markovian, only depending on the current state, and is

### [12:56 - 12:56]

depending on the current state, and is

### [12:56 - 12:58]

depending on the current state, and is smooth and deterministic. And

### [12:58 - 12:58]

smooth and deterministic. And

### [12:58 - 12:59]

smooth and deterministic. And essentially, for this result, we'll

### [12:59 - 12:59]

essentially, for this result, we'll

### [12:59 - 13:01]

essentially, for this result, we'll assume that the that the learner has to

### [13:01 - 13:01]

assume that the that the learner has to

### [13:01 - 13:02]

assume that the that the learner has to be the same. The learner cannot be much

### [13:02 - 13:02]

be the same. The learner cannot be much

### [13:02 - 13:07]

be the same. The learner cannot be much more general than the expert.

### [13:09 - 13:09]

So, now let's state the result.

### [13:09 - 13:10]

So, now let's state the result. The result says this. You give me your

### [13:10 - 13:10]

The result says this. You give me your

### [13:10 - 13:12]

The result says this. You give me your favorite scaling law, so n to the minus

### [13:12 - 13:12]

favorite scaling law, so n to the minus

### [13:12 - 13:14]

favorite scaling law, so n to the minus alpha. This is how much error should

### [13:14 - 13:14]

alpha. This is how much error should

### [13:14 - 13:16]

alpha. This is how much error should decrease as I get more data.

### [13:16 - 13:16]

decrease as I get more data.

### [13:16 - 13:17]

decrease as I get more data. And I'm going to give you a set of

### [13:17 - 13:17]

And I'm going to give you a set of

### [13:17 - 13:19]

And I'm going to give you a set of problems that satisfy all the nice

### [13:19 - 13:19]

problems that satisfy all the nice

### [13:19 - 13:21]

problems that satisfy all the nice conditions on the last slide that have

### [13:21 - 13:21]

conditions on the last slide that have

### [13:21 - 13:23]

conditions on the last slide that have the following two properties.

### [13:23 - 13:23]

the following two properties.

### [13:23 - 13:24]

the following two properties. So, the first property is that the

### [13:24 - 13:24]

So, the first property is that the

### [13:24 - 13:26]

So, the first property is that the supervised learning on the square loss

### [13:26 - 13:26]

supervised learning on the square loss

### [13:26 - 13:28]

supervised learning on the square loss obeys the scaling law that you gave me,

### [13:28 - 13:28]

obeys the scaling law that you gave me,

### [13:28 - 13:29]

obeys the scaling law that you gave me, right? It's going to the error is going

### [13:29 - 13:29]

right? It's going to the error is going

### [13:29 - 13:30]

right? It's going to the error is going to go down in terms of the data I

### [13:30 - 13:30]

to go down in terms of the data I

### [13:30 - 13:32]

to go down in terms of the data I collect on the expert distribution at

### [13:32 - 13:32]

collect on the expert distribution at

### [13:32 - 13:34]

collect on the expert distribution at this rate. You can make alpha 0.1, you

### [13:34 - 13:34]

this rate. You can make alpha 0.1, you

### [13:34 - 13:35]

this rate. You can make alpha 0.1, you can make alpha a million. I can give you

### [13:35 - 13:35]

can make alpha a million. I can give you

### [13:35 - 13:37]

can make alpha a million. I can give you an instance that has this property.

### [13:37 - 13:37]

an instance that has this property.

### [13:37 - 13:40]

an instance that has this property. However, any algorithm that satisfies

### [13:40 - 13:40]

However, any algorithm that satisfies

### [13:40 - 13:42]

However, any algorithm that satisfies the restrictions we placed in condition

### [13:42 - 13:42]

the restrictions we placed in condition

### [13:42 - 13:44]

the restrictions we placed in condition 4 is going to pay for that rate times 2

### [13:44 - 13:44]

4 is going to pay for that rate times 2

### [13:44 - 13:46]

4 is going to pay for that rate times 2 to the horizon, right? Times an

### [13:46 - 13:46]

to the horizon, right? Times an

### [13:46 - 13:48]

to the horizon, right? Times an exponential factor in how long it takes

### [13:48 - 13:48]

exponential factor in how long it takes

### [13:48 - 13:49]

exponential factor in how long it takes to complete the task.

### [13:49 - 13:49]

to complete the task.

### [13:49 - 13:51]

to complete the task. So, what this is showing is that error

### [13:51 - 13:51]

So, what this is showing is that error

### [13:51 - 13:52]

So, what this is showing is that error is compounding even in this nicest

### [13:52 - 13:52]

is compounding even in this nicest

### [13:52 - 13:55]

is compounding even in this nicest possible case by an exponential factor

### [13:55 - 13:55]

possible case by an exponential factor

### [13:55 - 13:58]

possible case by an exponential factor in the problem horizon.

### [13:58 - 13:58]

in the problem horizon.

### [13:58 - 13:59]

in the problem horizon. It's growing very large.

### [13:59 - 13:59]

It's growing very large.

### [13:59 - 14:00]

It's growing very large. Now, you might say, "Well, what if I

### [14:00 - 14:00]

Now, you might say, "Well, what if I

### [14:00 - 14:02]

Now, you might say, "Well, what if I just don't do behavior cloning? Maybe

### [14:02 - 14:02]

just don't do behavior cloning? Maybe

### [14:02 - 14:03]

just don't do behavior cloning? Maybe there's a better algorithm that I can

### [14:03 - 14:03]

there's a better algorithm that I can

### [14:03 - 14:05]

there's a better algorithm that I can design." Turns out this result will

### [14:05 - 14:05]

design." Turns out this result will

### [14:05 - 14:07]

design." Turns out this result will still apply. Behave It applies to any

### [14:07 - 14:07]

still apply. Behave It applies to any

### [14:07 - 14:09]

still apply. Behave It applies to any algorithm that satisfies the restriction

### [14:09 - 14:09]

algorithm that satisfies the restriction

### [14:09 - 14:10]

algorithm that satisfies the restriction 4, that has policies that are the same

### [14:10 - 14:10]

4, that has policies that are the same

### [14:10 - 14:12]

4, that has policies that are the same as the expert.

### [14:12 - 14:12]

as the expert.

### [14:12 - 14:13]

as the expert. And then you might say, "Well, what if I

### [14:13 - 14:13]

And then you might say, "Well, what if I

### [14:13 - 14:14]

And then you might say, "Well, what if I use reward? For example, offline

### [14:14 - 14:14]

use reward? For example, offline

### [14:14 - 14:16]

use reward? For example, offline reinforcement learning can be really

### [14:16 - 14:16]

reinforcement learning can be really

### [14:16 - 14:18]

reinforcement learning can be really powerful. Can that help?" No. So, this

### [14:18 - 14:18]

powerful. Can that help?" No. So, this

### [14:18 - 14:20]

powerful. Can that help?" No. So, this result applies even if I know the ground

### [14:20 - 14:20]

result applies even if I know the ground

### [14:20 - 14:22]

result applies even if I know the ground truth reward function, which means that

### [14:22 - 14:22]

truth reward function, which means that

### [14:22 - 14:23]

truth reward function, which means that all algorithms include offline RL

### [14:23 - 14:23]

all algorithms include offline RL

### [14:23 - 14:24]

all algorithms include offline RL algorithms because they would use the

### [14:24 - 14:24]

algorithms because they would use the

### [14:24 - 14:26]

algorithms because they would use the reward. So, none of these are are going

### [14:26 - 14:26]

reward. So, none of these are are going

### [14:26 - 14:28]

reward. So, none of these are are going to overcome the bound.

### [14:28 - 14:28]

to overcome the bound.

### [14:28 - 14:29]

to overcome the bound. So, essentially, we I'm billing this as

### [14:29 - 14:29]

So, essentially, we I'm billing this as

### [14:29 - 14:31]

So, essentially, we I'm billing this as the quantitative Moravec paradox in the

### [14:31 - 14:31]

the quantitative Moravec paradox in the

### [14:31 - 14:33]

the quantitative Moravec paradox in the sense that it establishes that you have

### [14:33 - 14:33]

sense that it establishes that you have

### [14:33 - 14:35]

sense that it establishes that you have this exponential in horizon effect if

### [14:35 - 14:35]

this exponential in horizon effect if

### [14:35 - 14:36]

this exponential in horizon effect if you're trying to do behavior cloning in

### [14:36 - 14:36]

you're trying to do behavior cloning in

### [14:36 - 14:37]

you're trying to do behavior cloning in the continuous world, whereas we only

### [14:37 - 14:37]

the continuous world, whereas we only

### [14:37 - 14:39]

the continuous world, whereas we only had a linear effect when we tried to see

### [14:39 - 14:39]

had a linear effect when we tried to see

### [14:39 - 14:42]

had a linear effect when we tried to see what was going on in the discrete world,

### [14:42 - 14:42]

what was going on in the discrete world,

### [14:42 - 14:43]

what was going on in the discrete world, So, now I'm going to try to explain why

### [14:43 - 14:43]

So, now I'm going to try to explain why

### [14:43 - 14:45]

So, now I'm going to try to explain why this happens. And from seeing why this

### [14:45 - 14:45]

this happens. And from seeing why this

### [14:45 - 14:46]

this happens. And from seeing why this happens, we'll then be able to

### [14:46 - 14:46]

happens, we'll then be able to

### [14:46 - 14:47]

happens, we'll then be able to understand why some of the more modern

### [14:47 - 14:47]

understand why some of the more modern

### [14:47 - 14:49]

understand why some of the more modern interventions in robot learning have

### [14:49 - 14:49]

interventions in robot learning have

### [14:49 - 14:52]

interventions in robot learning have been as successful as they've been.

### [14:54 - 14:54]

So, robot learning is a control problem,

### [14:54 - 14:56]

So, robot learning is a control problem, right? We have actions, we have

### [14:56 - 14:56]

right? We have actions, we have

### [14:56 - 14:57]

right? We have actions, we have dynamics, we have states or

### [14:57 - 14:57]

dynamics, we have states or

### [14:57 - 14:59]

dynamics, we have states or observations, we have policies.

### [14:59 - 14:59]

observations, we have policies.

### [14:59 - 15:01]

observations, we have policies. But, what makes a control problem? It's

### [15:01 - 15:01]

But, what makes a control problem? It's

### [15:01 - 15:03]

But, what makes a control problem? It's just a problem that has dynamics, but

### [15:03 - 15:03]

just a problem that has dynamics, but

### [15:03 - 15:05]

just a problem that has dynamics, but typically, at least culturally, it sort

### [15:05 - 15:05]

typically, at least culturally, it sort

### [15:05 - 15:07]

typically, at least culturally, it sort of it has this idea of stability.

### [15:07 - 15:07]

of it has this idea of stability.

### [15:07 - 15:09]

of it has this idea of stability. And stability is informally the

### [15:09 - 15:09]

And stability is informally the

### [15:09 - 15:10]

And stability is informally the sensitivity of a system to perturbations

### [15:10 - 15:10]

sensitivity of a system to perturbations

### [15:10 - 15:12]

sensitivity of a system to perturbations of its inputs. So, in the world of

### [15:12 - 15:12]

of its inputs. So, in the world of

### [15:12 - 15:13]

of its inputs. So, in the world of control, that's really what we care

### [15:13 - 15:13]

control, that's really what we care

### [15:13 - 15:15]

control, that's really what we care about. So, for example, the upside down

### [15:15 - 15:15]

about. So, for example, the upside down

### [15:15 - 15:16]

about. So, for example, the upside down pendulum is stable. It doesn't have too

### [15:16 - 15:16]

pendulum is stable. It doesn't have too

### [15:16 - 15:18]

pendulum is stable. It doesn't have too much sensitivity. The uh the inverted

### [15:18 - 15:18]

much sensitivity. The uh the inverted

### [15:18 - 15:20]

much sensitivity. The uh the inverted pendulum is unstable. Any small push can

### [15:20 - 15:20]

pendulum is unstable. Any small push can

### [15:20 - 15:22]

pendulum is unstable. Any small push can cause it to topple over to one side or

### [15:22 - 15:22]

cause it to topple over to one side or

### [15:22 - 15:24]

cause it to topple over to one side or another side.

### [15:24 - 15:24]

another side.

### [15:24 - 15:25]

another side. So,

### [15:25 - 15:25]

So,

### [15:25 - 15:27]

So, what we'll do is is

### [15:27 - 15:27]

what we'll do is is

### [15:27 - 15:28]

what we'll do is is One thing to note is that stability is

### [15:28 - 15:28]

One thing to note is that stability is

### [15:28 - 15:30]

One thing to note is that stability is very naturally related to compounding

### [15:30 - 15:30]

very naturally related to compounding

### [15:30 - 15:31]

very naturally related to compounding error, right? If you have high

### [15:31 - 15:31]

error, right? If you have high

### [15:31 - 15:33]

error, right? If you have high sensitivity to to mistakes, then of

### [15:33 - 15:33]

sensitivity to to mistakes, then of

### [15:33 - 15:34]

sensitivity to to mistakes, then of course, small errors you make will will

### [15:34 - 15:34]

course, small errors you make will will

### [15:34 - 15:36]

course, small errors you make will will blow up. But of course, we've assumed

### [15:36 - 15:36]

blow up. But of course, we've assumed

### [15:36 - 15:37]

blow up. But of course, we've assumed that the system is stable.

### [15:37 - 15:37]

that the system is stable.

### [15:37 - 15:39]

that the system is stable. So, what does that mean?

### [15:39 - 15:39]

So, what does that mean?

### [15:39 - 15:40]

So, what does that mean? We're going to use a definition of

### [15:40 - 15:40]

We're going to use a definition of

### [15:40 - 15:42]

We're going to use a definition of stability called incremental stability

### [15:42 - 15:42]

stability called incremental stability

### [15:42 - 15:44]

stability called incremental stability due to Agrichef.

### [15:44 - 15:44]

due to Agrichef.

### [15:44 - 15:46]

due to Agrichef. And incremental stability, it basically

### [15:46 - 15:46]

And incremental stability, it basically

### [15:46 - 15:48]

And incremental stability, it basically says the following. Imagine I start at

### [15:48 - 15:48]

says the following. Imagine I start at

### [15:48 - 15:50]

says the following. Imagine I start at the same initial state S. And now I take

### [15:50 - 15:50]

the same initial state S. And now I take

### [15:50 - 15:53]

the same initial state S. And now I take two sequences of actions starting at S.

### [15:53 - 15:53]

two sequences of actions starting at S.

### [15:53 - 15:55]

two sequences of actions starting at S. How different are the two states that I

### [15:55 - 15:55]

How different are the two states that I

### [15:55 - 15:57]

How different are the two states that I end up at? And what this equation says

### [15:57 - 15:57]

end up at? And what this equation says

### [15:57 - 15:58]

end up at? And what this equation says is that the difference between these two

### [15:58 - 15:58]

is that the difference between these two

### [15:58 - 16:00]

is that the difference between these two states is scales like the difference in

### [16:00 - 16:00]

states is scales like the difference in

### [16:00 - 16:03]

states is scales like the difference in the actions, but the contribution of

### [16:03 - 16:03]

the actions, but the contribution of

### [16:03 - 16:06]

the actions, but the contribution of actions in the past decays if this

### [16:06 - 16:06]

actions in the past decays if this

### [16:06 - 16:08]

actions in the past decays if this parameter rho is strictly less than 1,

### [16:08 - 16:08]

parameter rho is strictly less than 1,

### [16:08 - 16:09]

parameter rho is strictly less than 1, which we'll assume that it is. So,

### [16:09 - 16:09]

which we'll assume that it is. So,

### [16:09 - 16:11]

which we'll assume that it is. So, basically, in a stable system, if I make

### [16:11 - 16:11]

basically, in a stable system, if I make

### [16:11 - 16:13]

basically, in a stable system, if I make a mistake sometime in the past, its

### [16:13 - 16:13]

a mistake sometime in the past, its

### [16:13 - 16:15]

a mistake sometime in the past, its contribution to my current error will

### [16:15 - 16:15]

contribution to my current error will

### [16:15 - 16:17]

contribution to my current error will will will be exponentially small in how

### [16:17 - 16:17]

will will be exponentially small in how

### [16:17 - 16:19]

will will be exponentially small in how far in the past it was,

### [16:19 - 16:19]

far in the past it was,

### [16:19 - 16:20]

far in the past it was, So, naively, this is the kind of

### [16:20 - 16:20]

So, naively, this is the kind of

### [16:20 - 16:21]

So, naively, this is the kind of condition that we really want. This is a

### [16:21 - 16:21]

condition that we really want. This is a

### [16:21 - 16:22]

condition that we really want. This is a condition that should prevent

### [16:22 - 16:22]

condition that should prevent

### [16:22 - 16:24]

condition that should prevent exponential compounding error rather

### [16:24 - 16:24]

exponential compounding error rather

### [16:24 - 16:26]

exponential compounding error rather than be consistent with it.

### [16:26 - 16:26]

than be consistent with it.

### [16:26 - 16:28]

than be consistent with it. So, let's see what's going on.

### [16:28 - 16:28]

So, let's see what's going on.

### [16:28 - 16:30]

So, let's see what's going on. So, what are we promised? Well, we're

### [16:30 - 16:30]

So, what are we promised? Well, we're

### [16:30 - 16:32]

So, what are we promised? Well, we're promised that the system is open loop

### [16:32 - 16:32]

promised that the system is open loop

### [16:32 - 16:33]

promised that the system is open loop stable, meaning that if we have an

### [16:33 - 16:33]

stable, meaning that if we have an

### [16:33 - 16:35]

stable, meaning that if we have an adversary that perturbs actions, then

### [16:35 - 16:35]

adversary that perturbs actions, then

### [16:35 - 16:37]

adversary that perturbs actions, then the resulting differences in states

### [16:37 - 16:37]

the resulting differences in states

### [16:37 - 16:38]

the resulting differences in states aren't too large, and in fact, these

### [16:38 - 16:38]

aren't too large, and in fact, these

### [16:38 - 16:40]

aren't too large, and in fact, these mistakes will decay and vanish

### [16:40 - 16:40]

mistakes will decay and vanish

### [16:40 - 16:42]

mistakes will decay and vanish exponentially in how long we we've made

### [16:42 - 16:42]

exponentially in how long we we've made

### [16:42 - 16:44]

exponentially in how long we we've made them in the past.

### [16:44 - 16:44]

them in the past.

### [16:44 - 16:46]

them in the past. Similarly, we're promised closed loop

### [16:46 - 16:46]

Similarly, we're promised closed loop

### [16:46 - 16:48]

Similarly, we're promised closed loop stability in our assumption. So, this

### [16:48 - 16:48]

stability in our assumption. So, this

### [16:48 - 16:49]

stability in our assumption. So, this means that if you perturb actions given

### [16:49 - 16:49]

means that if you perturb actions given

### [16:49 - 16:51]

means that if you perturb actions given by the expert, formally, you consider

### [16:51 - 16:51]

by the expert, formally, you consider

### [16:51 - 16:53]

by the expert, formally, you consider what's called a closed loop dynamics

### [16:53 - 16:53]

what's called a closed loop dynamics

### [16:53 - 16:55]

what's called a closed loop dynamics where you consider an dynamics acting on

### [16:55 - 16:55]

where you consider an dynamics acting on

### [16:55 - 16:57]

where you consider an dynamics acting on states and action perturbations delta A

### [16:57 - 16:57]

states and action perturbations delta A

### [16:57 - 16:59]

states and action perturbations delta A that add action perturbations to what

### [16:59 - 16:59]

that add action perturbations to what

### [16:59 - 17:01]

that add action perturbations to what the policy would do.

### [17:01 - 17:01]

the policy would do.

### [17:01 - 17:02]

the policy would do. And here, we're also assuming that this

### [17:02 - 17:02]

And here, we're also assuming that this

### [17:02 - 17:04]

And here, we're also assuming that this is closed loop stable.

### [17:04 - 17:04]

is closed loop stable.

### [17:04 - 17:04]

is closed loop stable. Right? So, these are the two

### [17:04 - 17:04]

Right? So, these are the two

### [17:04 - 17:05]

Right? So, these are the two assumptions.

### [17:05 - 17:05]

assumptions.

### [17:05 - 17:07]

assumptions. But, the fundamental problem is that

### [17:07 - 17:07]

But, the fundamental problem is that

### [17:07 - 17:08]

But, the fundamental problem is that just because we're promised both of

### [17:08 - 17:08]

just because we're promised both of

### [17:08 - 17:09]

just because we're promised both of these,

### [17:09 - 17:09]

these,

### [17:09 - 17:10]

these, doesn't ensure that the policy that we

### [17:10 - 17:10]

doesn't ensure that the policy that we

### [17:10 - 17:12]

doesn't ensure that the policy that we learn, that pi hat, is going to be

### [17:12 - 17:12]

learn, that pi hat, is going to be

### [17:12 - 17:14]

learn, that pi hat, is going to be closed loop stable. In fact, it might

### [17:14 - 17:14]

closed loop stable. In fact, it might

### [17:14 - 17:15]

closed loop stable. In fact, it might not

### [17:15 - 17:15]

not

### [17:15 - 17:16]

not ensure this.

### [17:16 - 17:16]

ensure this.

### [17:16 - 17:19]

ensure this. So, let's try to understand why this is

### [17:19 - 17:19]

So, let's try to understand why this is

### [17:19 - 17:21]

So, let's try to understand why this is not possible. Uh this is a construction

### [17:21 - 17:21]

not possible. Uh this is a construction

### [17:21 - 17:24]

not possible. Uh this is a construction that's kind of cool, but also very sad.

### [17:24 - 17:24]

that's kind of cool, but also very sad.

### [17:24 - 17:26]

that's kind of cool, but also very sad. Uh so, essentially, you can construct

### [17:26 - 17:26]

Uh so, essentially, you can construct

### [17:26 - 17:28]

Uh so, essentially, you can construct two sets of policies and dynamics that

### [17:28 - 17:28]

two sets of policies and dynamics that

### [17:28 - 17:30]

two sets of policies and dynamics that are both open loop and closed loop

### [17:30 - 17:30]

are both open loop and closed loop

### [17:30 - 17:31]

are both open loop and closed loop stable.

### [17:31 - 17:31]

stable.

### [17:31 - 17:32]

stable. Now, in addition, they have the

### [17:32 - 17:32]

Now, in addition, they have the

### [17:32 - 17:34]

Now, in addition, they have the following property.

### [17:34 - 17:34]

following property.

### [17:34 - 17:36]

following property. Consider the subspace of the second

### [17:36 - 17:36]

Consider the subspace of the second

### [17:36 - 17:38]

Consider the subspace of the second basis vector, so 0 1. This is in two

### [17:38 - 17:38]

basis vector, so 0 1. This is in two

### [17:38 - 17:39]

basis vector, so 0 1. This is in two dimensions.

### [17:39 - 17:39]

dimensions.

### [17:39 - 17:40]

dimensions. Uh you can construct it so that they all

### [17:40 - 17:40]

Uh you can construct it so that they all

### [17:40 - 17:43]

Uh you can construct it so that they all agree on the subspace and that they all

### [17:43 - 17:43]

agree on the subspace and that they all

### [17:43 - 17:44]

agree on the subspace and that they all preserve the subspace, meaning which if

### [17:44 - 17:44]

preserve the subspace, meaning which if

### [17:44 - 17:45]

preserve the subspace, meaning which if meaning that if I have a state in the

### [17:45 - 17:45]

meaning that if I have a state in the

### [17:45 - 17:47]

meaning that if I have a state in the subspace, all the dynamics and policies

### [17:47 - 17:47]

subspace, all the dynamics and policies

### [17:47 - 17:49]

subspace, all the dynamics and policies will keep me on the subspace, right? So,

### [17:49 - 17:49]

will keep me on the subspace, right? So,

### [17:49 - 17:51]

will keep me on the subspace, right? So, I'm over all the way over here.

### [17:51 - 17:51]

I'm over all the way over here.

### [17:51 - 17:52]

I'm over all the way over here. So, essentially, what this means is that

### [17:52 - 17:52]

So, essentially, what this means is that

### [17:52 - 17:54]

So, essentially, what this means is that from the if I just collect expert data,

### [17:54 - 17:54]

from the if I just collect expert data,

### [17:54 - 17:56]

from the if I just collect expert data, I cannot distinguish if I'm in world 1

### [17:56 - 17:56]

I cannot distinguish if I'm in world 1

### [17:56 - 17:57]

I cannot distinguish if I'm in world 1 or world 2. There's not enough

### [17:57 - 17:57]

or world 2. There's not enough

### [17:57 - 18:00]

or world 2. There's not enough information.

### [18:00 - 18:00]

information.

### [18:00 - 18:02]

information. But, however, there's a problem,

### [18:02 - 18:02]

But, however, there's a problem,

### [18:02 - 18:04]

But, however, there's a problem, which is that if I try to have any

### [18:04 - 18:04]

which is that if I try to have any

### [18:04 - 18:07]

which is that if I try to have any policy,

### [18:09 - 18:09]

sorry, this is older version. If I have

### [18:09 - 18:10]

sorry, this is older version. If I have any policy that's of a certain kind

### [18:10 - 18:10]

any policy that's of a certain kind

### [18:10 - 18:12]

any policy that's of a certain kind agreeing on the subspace. So, if I take

### [18:12 - 18:12]

agreeing on the subspace. So, if I take

### [18:12 - 18:14]

agreeing on the subspace. So, if I take something that agrees with my expert one

### [18:14 - 18:14]

something that agrees with my expert one

### [18:14 - 18:16]

something that agrees with my expert one pair of these dynamics.

### [18:16 - 18:16]

pair of these dynamics.

### [18:16 - 18:18]

pair of these dynamics. Right? There's actually no way to

### [18:18 - 18:18]

Right? There's actually no way to

### [18:18 - 18:20]

Right? There's actually no way to stabilize both and agree on this data.

### [18:20 - 18:20]

stabilize both and agree on this data.

### [18:20 - 18:22]

stabilize both and agree on this data. And the problem is because these are

### [18:22 - 18:22]

And the problem is because these are

### [18:22 - 18:22]

And the problem is because these are because [clears throat] these instances

### [18:22 - 18:22]

because [clears throat] these instances

### [18:22 - 18:24]

because [clears throat] these instances are indistinguishable, I don't know

### [18:24 - 18:24]

are indistinguishable, I don't know

### [18:24 - 18:26]

are indistinguishable, I don't know which one I'm I'm on. So, from a

### [18:26 - 18:26]

which one I'm I'm on. So, from a

### [18:26 - 18:27]

which one I'm I'm on. So, from a robustness standpoint, I have to either

### [18:27 - 18:27]

robustness standpoint, I have to either

### [18:27 - 18:30]

robustness standpoint, I have to either try to stabilize both, but I can't.

### [18:30 - 18:30]

try to stabilize both, but I can't.

### [18:30 - 18:31]

try to stabilize both, but I can't. And so, what we're able to show then is

### [18:31 - 18:31]

And so, what we're able to show then is

### [18:31 - 18:33]

And so, what we're able to show then is that if you make an initial mistake,

### [18:33 - 18:33]

that if you make an initial mistake,

### [18:33 - 18:34]

that if you make an initial mistake, which we can use sort of the theory of

### [18:34 - 18:34]

which we can use sort of the theory of

### [18:34 - 18:36]

which we can use sort of the theory of non-parametric statistics to show that

### [18:36 - 18:36]

non-parametric statistics to show that

### [18:36 - 18:37]

non-parametric statistics to show that you will, just by showing that you're

### [18:37 - 18:37]

you will, just by showing that you're

### [18:37 - 18:39]

you will, just by showing that you're sort of the magnitude of your mistakes

### [18:39 - 18:39]

sort of the magnitude of your mistakes

### [18:39 - 18:40]

sort of the magnitude of your mistakes agree with the scaling law that we saw

### [18:40 - 18:40]

agree with the scaling law that we saw

### [18:40 - 18:41]

agree with the scaling law that we saw in that that result,

### [18:41 - 18:41]

in that that result,

### [18:41 - 18:43]

in that that result, then those mistakes are going to seed

### [18:43 - 18:43]

then those mistakes are going to seed

### [18:43 - 18:44]

then those mistakes are going to seed some initial error,

### [18:44 - 18:44]

some initial error,

### [18:44 - 18:46]

some initial error, and that initial error on one of these

### [18:46 - 18:46]

and that initial error on one of these

### [18:46 - 18:47]

and that initial error on one of these two possible worlds, which you can't

### [18:47 - 18:47]

two possible worlds, which you can't

### [18:47 - 18:50]

two possible worlds, which you can't tell apart, is going to become sort of

### [18:50 - 18:50]

tell apart, is going to become sort of

### [18:50 - 18:51]

tell apart, is going to become sort of larger and larger due to instability

### [18:51 - 18:51]

larger and larger due to instability

### [18:51 - 18:54]

larger and larger due to instability compounding the error exponentially.

### [18:54 - 18:54]

compounding the error exponentially.

### [18:54 - 18:56]

compounding the error exponentially. And the kind of crucial observation here

### [18:56 - 18:56]

And the kind of crucial observation here

### [18:56 - 18:58]

And the kind of crucial observation here is really this distance-wise error. This

### [18:58 - 18:58]

is really this distance-wise error. This

### [18:58 - 18:59]

is really this distance-wise error. This is why the continuous world is

### [18:59 - 18:59]

is why the continuous world is

### [18:59 - 19:00]

is why the continuous world is different. In the discrete world, we're

### [19:00 - 19:00]

different. In the discrete world, we're

### [19:00 - 19:02]

different. In the discrete world, we're either right or we're wrong, but in the

### [19:02 - 19:02]

either right or we're wrong, but in the

### [19:02 - 19:03]

either right or we're wrong, but in the continuous world, or we're right or

### [19:03 - 19:03]

continuous world, or we're right or

### [19:03 - 19:05]

continuous world, or we're right or wrong with some probability, but here,

### [19:05 - 19:05]

wrong with some probability, but here,

### [19:05 - 19:07]

wrong with some probability, but here, we make these like metric errors, right?

### [19:07 - 19:07]

we make these like metric errors, right?

### [19:07 - 19:09]

we make these like metric errors, right? Because 0-1 learning is not possible,

### [19:09 - 19:09]

Because 0-1 learning is not possible,

### [19:09 - 19:11]

Because 0-1 learning is not possible, and these are what seed the instability

### [19:11 - 19:11]

and these are what seed the instability

### [19:11 - 19:15]

and these are what seed the instability that can really kind of mess us up.

### [19:16 - 19:16]

So, in the next part of the talk, the

### [19:16 - 19:17]

So, in the next part of the talk, the rest of the talk, I'm going to try to

### [19:17 - 19:17]

rest of the talk, I'm going to try to

### [19:17 - 19:19]

rest of the talk, I'm going to try to answer what we can do about it, how we

### [19:19 - 19:19]

answer what we can do about it, how we

### [19:19 - 19:21]

answer what we can do about it, how we can overcome the pathology that's

### [19:21 - 19:21]

can overcome the pathology that's

### [19:21 - 19:23]

can overcome the pathology that's illuminated over here.

### [19:23 - 19:23]

illuminated over here.

### [19:23 - 19:25]

illuminated over here. We'll begin with the first intervention.

### [19:25 - 19:25]

We'll begin with the first intervention.

### [19:25 - 19:26]

We'll begin with the first intervention. This most directly

### [19:26 - 19:26]

This most directly

### [19:26 - 19:28]

This most directly affects this pathology, and it's also

### [19:28 - 19:28]

affects this pathology, and it's also

### [19:28 - 19:29]

affects this pathology, and it's also the one that we have strong theoretical

### [19:29 - 19:29]

the one that we have strong theoretical

### [19:29 - 19:30]

the one that we have strong theoretical guarantees for.

### [19:30 - 19:30]

guarantees for.

### [19:30 - 19:32]

guarantees for. And this is led by Thomas Eng. He's a

### [19:32 - 19:32]

And this is led by Thomas Eng. He's a

### [19:32 - 19:33]

And this is led by Thomas Eng. He's a PhD student at UPenn. He's going to be

### [19:33 - 19:33]

PhD student at UPenn. He's going to be

### [19:33 - 19:35]

PhD student at UPenn. He's going to be joining as a postdoc in my group next

### [19:35 - 19:35]

joining as a postdoc in my group next

### [19:35 - 19:36]

joining as a postdoc in my group next year.

### [19:36 - 19:36]

year.

### [19:36 - 19:39]

year. So, the first intervention that was

### [19:39 - 19:39]

So, the first intervention that was

### [19:39 - 19:40]

So, the first intervention that was incredibly successful was this idea of

### [19:40 - 19:40]

incredibly successful was this idea of

### [19:40 - 19:42]

incredibly successful was this idea of action chunking. I'll actually I

### [19:42 - 19:42]

action chunking. I'll actually I

### [19:42 - 19:43]

action chunking. I'll actually I actually believe that action chunking is

### [19:43 - 19:43]

actually believe that action chunking is

### [19:43 - 19:44]

actually believe that action chunking is perhaps more important than the

### [19:44 - 19:44]

perhaps more important than the

### [19:44 - 19:46]

perhaps more important than the intervention on the next slide, but

### [19:46 - 19:46]

intervention on the next slide, but

### [19:46 - 19:48]

intervention on the next slide, but potentially not necessary in the long

### [19:48 - 19:48]

potentially not necessary in the long

### [19:48 - 19:49]

potentially not necessary in the long run.

### [19:49 - 19:49]

run.

### [19:49 - 19:51]

run. Um so, what is action chunking doing?

### [19:51 - 19:51]

Um so, what is action chunking doing?

### [19:51 - 19:53]

Um so, what is action chunking doing? Well, remember we had this restriction

### [19:53 - 19:53]

Well, remember we had this restriction

### [19:53 - 19:54]

Well, remember we had this restriction on what our policies could learn, right?

### [19:54 - 19:54]

on what our policies could learn, right?

### [19:54 - 19:56]

on what our policies could learn, right? We said the learner must return

### [19:56 - 19:56]

We said the learner must return

### [19:56 - 19:58]

We said the learner must return Markovian policies. These are policies

### [19:58 - 19:58]

Markovian policies. These are policies

### [19:58 - 19:59]

Markovian policies. These are policies that only depend on the current

### [19:59 - 19:59]

that only depend on the current

### [19:59 - 20:02]

that only depend on the current observation.

### [20:02 - 20:02]

observation.

### [20:02 - 20:04]

observation. But what action chunking does, this

### [20:04 - 20:04]

But what action chunking does, this

### [20:04 - 20:06]

But what action chunking does, this intervention where we predict multiple

### [20:06 - 20:06]

intervention where we predict multiple

### [20:06 - 20:07]

intervention where we predict multiple actions at the same time by by

### [20:07 - 20:07]

actions at the same time by by

### [20:07 - 20:10]

actions at the same time by by execution, is it actually correlates

### [20:10 - 20:10]

execution, is it actually correlates

### [20:10 - 20:11]

execution, is it actually correlates actions across time.

### [20:11 - 20:11]

actions across time.

### [20:11 - 20:13]

actions across time. Because now the action I'm taking at

### [20:13 - 20:13]

Because now the action I'm taking at

### [20:13 - 20:15]

Because now the action I'm taking at some point was correlated or dependent

### [20:15 - 20:15]

some point was correlated or dependent

### [20:15 - 20:16]

some point was correlated or dependent on observation I made a couple steps

### [20:16 - 20:16]

on observation I made a couple steps

### [20:16 - 20:19]

on observation I made a couple steps ago. So it's non-Markov. So at least

### [20:19 - 20:19]

ago. So it's non-Markov. So at least

### [20:19 - 20:21]

ago. So it's non-Markov. So at least from a sanity check, it says that action

### [20:21 - 20:21]

from a sanity check, it says that action

### [20:21 - 20:22]

from a sanity check, it says that action chunking policies are not covered by our

### [20:22 - 20:22]

chunking policies are not covered by our

### [20:22 - 20:25]

chunking policies are not covered by our negative result.

### [20:25 - 20:25]

negative result.

### [20:25 - 20:26]

negative result. So let me tell you what they actually

### [20:26 - 20:26]

So let me tell you what they actually

### [20:26 - 20:28]

So let me tell you what they actually can do.

### [20:28 - 20:28]

can do.

### [20:28 - 20:29]

can do. Uh just for those that haven't seen

### [20:29 - 20:29]

Uh just for those that haven't seen

### [20:29 - 20:30]

Uh just for those that haven't seen action chunking training, the way that

### [20:30 - 20:30]

action chunking training, the way that

### [20:30 - 20:31]

action chunking training, the way that you would train such a thing is for

### [20:31 - 20:31]

you would train such a thing is for

### [20:31 - 20:33]

you would train such a thing is for example, if you're using regression, you

### [20:33 - 20:33]

example, if you're using regression, you

### [20:33 - 20:35]

example, if you're using regression, you just minimize a loss to a sequence of

### [20:35 - 20:35]

just minimize a loss to a sequence of

### [20:35 - 20:36]

just minimize a loss to a sequence of actions. So rather than predicting one

### [20:36 - 20:36]

actions. So rather than predicting one

### [20:36 - 20:38]

actions. So rather than predicting one action, you predict a whole vector of

### [20:38 - 20:38]

action, you predict a whole vector of

### [20:38 - 20:41]

action, you predict a whole vector of actions and you just minimize that.

### [20:43 - 20:43]

So what we're going to do is state

### [20:43 - 20:44]

So what we're going to do is state action chunking in a case where the

### [20:44 - 20:44]

action chunking in a case where the

### [20:44 - 20:46]

action chunking in a case where the dynamics are open state open loop

### [20:46 - 20:46]

dynamics are open state open loop

### [20:46 - 20:48]

dynamics are open state open loop stable, like the lower bound. We'll get

### [20:48 - 20:48]

stable, like the lower bound. We'll get

### [20:48 - 20:50]

stable, like the lower bound. We'll get to the open loop unstable setting later.

### [20:50 - 20:50]

to the open loop unstable setting later.

### [20:50 - 20:51]

to the open loop unstable setting later. And essentially what we show is the

### [20:51 - 20:51]

And essentially what we show is the

### [20:51 - 20:53]

And essentially what we show is the following. As long as your chunk length

### [20:53 - 20:53]

following. As long as your chunk length

### [20:53 - 20:55]

following. As long as your chunk length is bigger than bigger is is is bigger

### [20:55 - 20:55]

is bigger than bigger is is is bigger

### [20:55 - 20:56]

is bigger than bigger is is is bigger than some sort of threshold K star

### [20:56 - 20:56]

than some sort of threshold K star

### [20:56 - 20:58]

than some sort of threshold K star sufficiently large, you have no

### [20:58 - 20:58]

sufficiently large, you have no

### [20:58 - 21:00]

sufficiently large, you have no compounding error.

### [21:00 - 21:00]

compounding error.

### [21:00 - 21:03]

compounding error. So your suboptimality and reward is at

### [21:03 - 21:03]

So your suboptimality and reward is at

### [21:03 - 21:05]

So your suboptimality and reward is at most the behavior cloning loss at the

### [21:05 - 21:05]

most the behavior cloning loss at the

### [21:05 - 21:08]

most the behavior cloning loss at the chunk level times some constant C.

### [21:08 - 21:08]

chunk level times some constant C.

### [21:08 - 21:10]

chunk level times some constant C. So yes, we're avoiding compounding

### [21:10 - 21:10]

So yes, we're avoiding compounding

### [21:10 - 21:11]

So yes, we're avoiding compounding error.

### [21:11 - 21:11]

error.

### [21:11 - 21:14]

error. But also these constants K star and and

### [21:14 - 21:14]

But also these constants K star and and

### [21:14 - 21:15]

But also these constants K star and and C star are polynomial and relevant

### [21:15 - 21:15]

C star are polynomial and relevant

### [21:15 - 21:16]

C star are polynomial and relevant factors and they're not dependent in

### [21:16 - 21:16]

factors and they're not dependent in

### [21:16 - 21:18]

factors and they're not dependent in horizon.

### [21:18 - 21:18]

horizon.

### [21:18 - 21:20]

horizon. In particular, the effect saturates to

### [21:20 - 21:20]

In particular, the effect saturates to

### [21:20 - 21:22]

In particular, the effect saturates to the critical K star. So it's not that

### [21:22 - 21:22]

the critical K star. So it's not that

### [21:22 - 21:23]

the critical K star. So it's not that you're just cutting the horizon by some

### [21:23 - 21:23]

you're just cutting the horizon by some

### [21:23 - 21:25]

you're just cutting the horizon by some amount, you're actually avoiding

### [21:25 - 21:25]

amount, you're actually avoiding

### [21:25 - 21:26]

amount, you're actually avoiding compounding error all together. It's

### [21:26 - 21:26]

compounding error all together. It's

### [21:26 - 21:28]

compounding error all together. It's sort of a phase change in the dynamics

### [21:28 - 21:28]

sort of a phase change in the dynamics

### [21:28 - 21:29]

sort of a phase change in the dynamics itself.

### [21:29 - 21:29]

itself.

### [21:29 - 21:31]

itself. Um so let's see what what's going on.

### [21:31 - 21:31]

Um so let's see what what's going on.

### [21:31 - 21:33]

Um so let's see what what's going on. So recall that if you don't have any

### [21:33 - 21:33]

So recall that if you don't have any

### [21:33 - 21:34]

So recall that if you don't have any action chunking, you're just going to

### [21:34 - 21:34]

action chunking, you're just going to

### [21:34 - 21:37]

action chunking, you're just going to have a ton of compounding error.

### [21:37 - 21:37]

have a ton of compounding error.

### [21:37 - 21:38]

have a ton of compounding error. But if you do have action chunking,

### [21:38 - 21:38]

But if you do have action chunking,

### [21:38 - 21:40]

But if you do have action chunking, because your system is open loop stable,

### [21:40 - 21:40]

because your system is open loop stable,

### [21:40 - 21:43]

because your system is open loop stable, you'll might make some mistakes, but the

### [21:43 - 21:43]

you'll might make some mistakes, but the

### [21:43 - 21:44]

you'll might make some mistakes, but the mistakes won't be too large, right?

### [21:44 - 21:44]

mistakes won't be too large, right?

### [21:44 - 21:46]

mistakes won't be too large, right? Because you have open loop stability, so

### [21:46 - 21:46]

Because you have open loop stability, so

### [21:46 - 21:47]

Because you have open loop stability, so you know, you might have a little bit of

### [21:47 - 21:47]

you know, you might have a little bit of

### [21:47 - 21:49]

you know, you might have a little bit of error at every time, but it'll saturate.

### [21:49 - 21:49]

error at every time, but it'll saturate.

### [21:49 - 21:51]

error at every time, but it'll saturate. Now, if we want to analyze action

### [21:51 - 21:51]

Now, if we want to analyze action

### [21:51 - 21:52]

Now, if we want to analyze action chunking, we can do a thought

### [21:52 - 21:52]

chunking, we can do a thought

### [21:52 - 21:53]

chunking, we can do a thought experiment.

### [21:53 - 21:53]

experiment.

### [21:53 - 21:55]

experiment. Imagine that I could magically reset

### [21:55 - 21:55]

Imagine that I could magically reset

### [21:55 - 21:58]

Imagine that I could magically reset back to my expert state over here.

### [21:58 - 21:58]

back to my expert state over here.

### [21:58 - 21:59]

back to my expert state over here. Right?

### [21:59 - 21:59]

Right?

### [21:59 - 22:00]

Right? Then again, I could roll out a action

### [22:00 - 22:00]

Then again, I could roll out a action

### [22:00 - 22:02]

Then again, I could roll out a action chunk that I've learned and I'd make

### [22:02 - 22:02]

chunk that I've learned and I'd make

### [22:02 - 22:06]

chunk that I've learned and I'd make again some small amount of error.

### [22:08 - 22:08]

So now here is kind of the magical fact

### [22:08 - 22:10]

So now here is kind of the magical fact about action chunking.

### [22:10 - 22:10]

about action chunking.

### [22:10 - 22:11]

about action chunking. Assuming that your policy is Lipschitz,

### [22:11 - 22:11]

Assuming that your policy is Lipschitz,

### [22:11 - 22:12]

Assuming that your policy is Lipschitz, meaning that it doesn't change too

### [22:12 - 22:12]

meaning that it doesn't change too

### [22:12 - 22:14]

meaning that it doesn't change too wildly as you perturb it,

### [22:14 - 22:14]

wildly as you perturb it,

### [22:14 - 22:16]

wildly as you perturb it, uh and some other kind of other

### [22:16 - 22:16]

uh and some other kind of other

### [22:16 - 22:19]

uh and some other kind of other conditions, essentially what we can show

### [22:19 - 22:19]

conditions, essentially what we can show

### [22:19 - 22:20]

conditions, essentially what we can show is that the learned policy is closed

### [22:20 - 22:20]

is that the learned policy is closed

### [22:20 - 22:22]

is that the learned policy is closed loop stable.

### [22:22 - 22:22]

loop stable.

### [22:22 - 22:25]

loop stable. And what that means is that if I think

### [22:25 - 22:25]

And what that means is that if I think

### [22:25 - 22:27]

And what that means is that if I think of this as a perturbation, so I think of

### [22:27 - 22:27]

of this as a perturbation, so I think of

### [22:27 - 22:29]

of this as a perturbation, so I think of where I got to here as a perturbation of

### [22:29 - 22:29]

where I got to here as a perturbation of

### [22:29 - 22:31]

where I got to here as a perturbation of the ideal trajectory that was perfectly

### [22:31 - 22:31]

the ideal trajectory that was perfectly

### [22:31 - 22:32]

the ideal trajectory that was perfectly reset,

### [22:32 - 22:32]

reset,

### [22:32 - 22:35]

reset, then that perturbation is going to not

### [22:35 - 22:35]

then that perturbation is going to not

### [22:35 - 22:36]

then that perturbation is going to not push the trajectory starting from here

### [22:36 - 22:36]

push the trajectory starting from here

### [22:36 - 22:38]

push the trajectory starting from here too far from this idealized one in the

### [22:38 - 22:38]

too far from this idealized one in the

### [22:38 - 22:39]

too far from this idealized one in the pink.

### [22:39 - 22:39]

pink.

### [22:39 - 22:40]

pink. Right? So that this is actually going to

### [22:40 - 22:40]

Right? So that this is actually going to

### [22:40 - 22:42]

Right? So that this is actually going to kind of track this trajectory in the

### [22:42 - 22:42]

kind of track this trajectory in the

### [22:42 - 22:44]

kind of track this trajectory in the following sense.

### [22:44 - 22:44]

following sense.

### [22:44 - 22:45]

following sense. And the process can repeat of all

### [22:45 - 22:45]

And the process can repeat of all

### [22:45 - 22:47]

And the process can repeat of all keeping the compounding error controlled

### [22:47 - 22:47]

keeping the compounding error controlled

### [22:47 - 22:50]

keeping the compounding error controlled over the duration of the trajectory.

### [22:50 - 22:50]

over the duration of the trajectory.

### [22:50 - 22:52]

over the duration of the trajectory. Now, essentially what's going on is that

### [22:52 - 22:52]

Now, essentially what's going on is that

### [22:52 - 22:54]

Now, essentially what's going on is that the rate of contraction is overcoming

### [22:54 - 22:54]

the rate of contraction is overcoming

### [22:54 - 22:56]

the rate of contraction is overcoming the sensitivity of your policy. So your

### [22:56 - 22:56]

the sensitivity of your policy. So your

### [22:56 - 22:57]

the sensitivity of your policy. So your policy might have some decent amount of

### [22:57 - 22:57]

policy might have some decent amount of

### [22:57 - 22:58]

policy might have some decent amount of sensitivity here. This might not be

### [22:58 - 22:58]

sensitivity here. This might not be

### [22:58 - 23:00]

sensitivity here. This might not be contractive, but that if you take

### [23:00 - 23:00]

contractive, but that if you take

### [23:00 - 23:02]

contractive, but that if you take multiple steps of the chunk, that's

### [23:02 - 23:02]

multiple steps of the chunk, that's

### [23:02 - 23:04]

multiple steps of the chunk, that's enough time for this contraction to take

### [23:04 - 23:04]

enough time for this contraction to take

### [23:04 - 23:05]

enough time for this contraction to take hold and overcome these mistakes that

### [23:05 - 23:05]

hold and overcome these mistakes that

### [23:05 - 23:06]

hold and overcome these mistakes that you made.

### [23:06 - 23:06]

you made.

### [23:06 - 23:08]

you made. And that's what's going on.

### [23:08 - 23:08]

And that's what's going on.

### [23:08 - 23:10]

And that's what's going on. Now, you might actually see this. Yes,

### [23:10 - 23:10]

Now, you might actually see this. Yes,

### [23:10 - 23:12]

Now, you might actually see this. Yes, Andrea. Quick question. Um

### [23:12 - 23:12]

Andrea. Quick question. Um

### [23:12 - 23:14]

Andrea. Quick question. Um So a trivial action chunk is a chunk of

### [23:14 - 23:14]

So a trivial action chunk is a chunk of

### [23:14 - 23:15]

So a trivial action chunk is a chunk of length

### [23:15 - 23:15]

length

### [23:15 - 23:15]

length Yes.

### [23:15 - 23:15]

Yes.

### [23:15 - 23:18]

Yes. >> what you used to be doing. Yes. So is it

### [23:18 - 23:18]

>> what you used to be doing. Yes. So is it

### [23:18 - 23:21]

>> what you used to be doing. Yes. So is it any chunk of greater than length Oh, no.

### [23:21 - 23:21]

any chunk of greater than length Oh, no.

### [23:21 - 23:22]

any chunk of greater than length Oh, no. It has to be It has to be greater than

### [23:22 - 23:22]

It has to be It has to be greater than

### [23:22 - 23:23]

It has to be It has to be greater than this K star, which depends on the

### [23:23 - 23:23]

this K star, which depends on the

### [23:23 - 23:25]

this K star, which depends on the control properties of the system. I see.

### [23:25 - 23:25]

control properties of the system. I see.

### [23:25 - 23:26]

control properties of the system. I see. So roughly it has to be like Lipschitz

### [23:26 - 23:26]

So roughly it has to be like Lipschitz

### [23:26 - 23:28]

So roughly it has to be like Lipschitz constant divided by some contractivity

### [23:28 - 23:28]

constant divided by some contractivity

### [23:28 - 23:30]

constant divided by some contractivity and then you kind of get into Yeah. Got

### [23:30 - 23:30]

and then you kind of get into Yeah. Got

### [23:30 - 23:34]

and then you kind of get into Yeah. Got it. Exactly. Yeah, of course.

### [23:36 - 23:36]

Perfect. So uh you might also, if you

### [23:36 - 23:38]

Perfect. So uh you might also, if you want some just like visual evidence, if

### [23:38 - 23:38]

want some just like visual evidence, if

### [23:38 - 23:39]

want some just like visual evidence, if you've played around with action

### [23:39 - 23:39]

you've played around with action

### [23:39 - 23:40]

you've played around with action chunking, you might see that non-action

### [23:40 - 23:40]

chunking, you might see that non-action

### [23:40 - 23:42]

chunking, you might see that non-action chunk policies are super jittery and

### [23:42 - 23:42]

chunk policies are super jittery and

### [23:42 - 23:42]

chunk policies are super jittery and then when you action chunk them, they're

### [23:42 - 23:42]

then when you action chunk them, they're

### [23:42 - 23:45]

then when you action chunk them, they're really smooth. That's kind of you can

### [23:45 - 23:45]

really smooth. That's kind of you can

### [23:45 - 23:46]

really smooth. That's kind of you can kind of think of this as like the

### [23:46 - 23:46]

kind of think of this as like the

### [23:46 - 23:47]

kind of think of this as like the theoretical correlate of that of that

### [23:47 - 23:47]

theoretical correlate of that of that

### [23:47 - 23:48]

theoretical correlate of that of that observation.

### [23:48 - 23:48]

observation.

### [23:48 - 23:51]

observation. Um let's actually test this. So what I

### [23:51 - 23:51]

Um let's actually test this. So what I

### [23:51 - 23:53]

Um let's actually test this. So what I wanted to do is test action chunking in

### [23:53 - 23:53]

wanted to do is test action chunking in

### [23:53 - 23:55]

wanted to do is test action chunking in like a really, really simple case where

### [23:55 - 23:55]

like a really, really simple case where

### [23:55 - 23:56]

like a really, really simple case where we don't have any other compounding

### [23:56 - 23:56]

we don't have any other compounding

### [23:56 - 23:58]

we don't have any other compounding confounding factors. So we trained it

### [23:58 - 23:58]

confounding factors. So we trained it

### [23:58 - 23:59]

confounding factors. So we trained it with a we trained a policy with

### [23:59 - 23:59]

with a we trained a policy with

### [23:59 - 24:00]

with a we trained a policy with deterministic experts and state-based

### [24:00 - 24:00]

deterministic experts and state-based

### [24:00 - 24:02]

deterministic experts and state-based regression. So there's no partial

### [24:02 - 24:02]

regression. So there's no partial

### [24:02 - 24:04]

regression. So there's no partial observ- observability issues.

### [24:04 - 24:04]

observ- observability issues.

### [24:04 - 24:05]

observ- observability issues. And essentially what we did is we looked

### [24:05 - 24:05]

And essentially what we did is we looked

### [24:05 - 24:07]

And essentially what we did is we looked at different predicted action chunks. So

### [24:07 - 24:07]

at different predicted action chunks. So

### [24:07 - 24:09]

at different predicted action chunks. So you might predict a long action chunk

### [24:09 - 24:09]

you might predict a long action chunk

### [24:09 - 24:10]

you might predict a long action chunk say for representation learning

### [24:10 - 24:10]

say for representation learning

### [24:10 - 24:12]

say for representation learning purposes, but only use a small one. And

### [24:12 - 24:12]

purposes, but only use a small one. And

### [24:12 - 24:14]

purposes, but only use a small one. And we also looked at the performance as you

### [24:14 - 24:14]

we also looked at the performance as you

### [24:14 - 24:17]

we also looked at the performance as you evaluate longer chunks. And indeed, it

### [24:17 - 24:17]

evaluate longer chunks. And indeed, it

### [24:17 - 24:18]

evaluate longer chunks. And indeed, it seems that the evaluation length of the

### [24:18 - 24:18]

seems that the evaluation length of the

### [24:18 - 24:20]

seems that the evaluation length of the chunk seems to be really the dominant

### [24:20 - 24:20]

chunk seems to be really the dominant

### [24:20 - 24:21]

chunk seems to be really the dominant factor. It's not just that you need to

### [24:21 - 24:21]

factor. It's not just that you need to

### [24:21 - 24:23]

factor. It's not just that you need to predict long chunks, you actually need

### [24:23 - 24:23]

predict long chunks, you actually need

### [24:23 - 24:24]

predict long chunks, you actually need to evaluate long ones, which is

### [24:24 - 24:24]

to evaluate long ones, which is

### [24:24 - 24:25]

to evaluate long ones, which is consistent with the picture that we have

### [24:25 - 24:25]

consistent with the picture that we have

### [24:25 - 24:27]

consistent with the picture that we have on the previous slide.

### [24:27 - 24:27]

on the previous slide.

### [24:27 - 24:29]

on the previous slide. Um so there are other hypotheses and I

### [24:29 - 24:29]

Um so there are other hypotheses and I

### [24:29 - 24:31]

Um so there are other hypotheses and I think many of them are very valid about

### [24:31 - 24:31]

think many of them are very valid about

### [24:31 - 24:32]

think many of them are very valid about why action chunking works,

### [24:32 - 24:32]

why action chunking works,

### [24:32 - 24:33]

why action chunking works, representation learning, mitigating

### [24:33 - 24:33]

representation learning, mitigating

### [24:33 - 24:35]

representation learning, mitigating partial observability,

### [24:35 - 24:35]

partial observability,

### [24:35 - 24:36]

partial observability, uh but I think that sort of this this

### [24:36 - 24:36]

uh but I think that sort of this this

### [24:36 - 24:38]

uh but I think that sort of this this stability interpretation, which sort of

### [24:38 - 24:38]

stability interpretation, which sort of

### [24:38 - 24:39]

stability interpretation, which sort of looks a little bit like receding horizon

### [24:39 - 24:39]

looks a little bit like receding horizon

### [24:39 - 24:42]

looks a little bit like receding horizon control, I think it's maybe the at least

### [24:42 - 24:42]

control, I think it's maybe the at least

### [24:42 - 24:43]

control, I think it's maybe the at least is an important consideration that I

### [24:43 - 24:43]

is an important consideration that I

### [24:43 - 24:45]

is an important consideration that I think was kind of underemphasized in

### [24:45 - 24:45]

think was kind of underemphasized in

### [24:45 - 24:47]

think was kind of underemphasized in some of the literature previously.

### [24:47 - 24:47]

some of the literature previously.

### [24:47 - 24:49]

some of the literature previously. So the core assumption that enables our

### [24:49 - 24:49]

So the core assumption that enables our

### [24:49 - 24:51]

So the core assumption that enables our analysis of action chunking to work is

### [24:51 - 24:51]

analysis of action chunking to work is

### [24:51 - 24:53]

analysis of action chunking to work is that the dynamics are open loop stable,

### [24:53 - 24:53]

that the dynamics are open loop stable,

### [24:53 - 24:55]

that the dynamics are open loop stable, right? Now, why should you believe this?

### [24:55 - 24:55]

right? Now, why should you believe this?

### [24:55 - 24:57]

right? Now, why should you believe this? Well, I think a lot of modern robotics,

### [24:57 - 24:57]

Well, I think a lot of modern robotics,

### [24:57 - 24:59]

Well, I think a lot of modern robotics, especially around this 2023 inflection

### [24:59 - 24:59]

especially around this 2023 inflection

### [24:59 - 25:01]

especially around this 2023 inflection point, was doing its best to put us in a

### [25:01 - 25:01]

point, was doing its best to put us in a

### [25:01 - 25:02]

point, was doing its best to put us in a regime where this open loop stability

### [25:02 - 25:02]

regime where this open loop stability

### [25:02 - 25:03]

regime where this open loop stability was true.

### [25:03 - 25:03]

was true.

### [25:03 - 25:06]

was true. So a very popular thing to do, whether

### [25:06 - 25:06]

So a very popular thing to do, whether

### [25:06 - 25:07]

So a very popular thing to do, whether you're doing joint control or end

### [25:07 - 25:07]

you're doing joint control or end

### [25:07 - 25:10]

you're doing joint control or end effector control, is position tracking.

### [25:10 - 25:10]

effector control, is position tracking.

### [25:10 - 25:12]

effector control, is position tracking. Right? So you'll predict positions that

### [25:12 - 25:12]

Right? So you'll predict positions that

### [25:12 - 25:13]

Right? So you'll predict positions that you want your robot to get to and then

### [25:13 - 25:13]

you want your robot to get to and then

### [25:13 - 25:16]

you want your robot to get to and then you'll use a low-level controller to

### [25:16 - 25:16]

you'll use a low-level controller to

### [25:16 - 25:18]

you'll use a low-level controller to stabilize your robot around those

### [25:18 - 25:18]

stabilize your robot around those

### [25:18 - 25:19]

stabilize your robot around those positions.

### [25:19 - 25:19]

positions.

### [25:19 - 25:21]

positions. Right? So effectively, this is putting

### [25:21 - 25:21]

Right? So effectively, this is putting

### [25:21 - 25:22]

Right? So effectively, this is putting you into the regime where the system, at

### [25:22 - 25:22]

you into the regime where the system, at

### [25:22 - 25:24]

you into the regime where the system, at least the robot only system, is open

### [25:24 - 25:24]

least the robot only system, is open

### [25:24 - 25:25]

least the robot only system, is open loop stable.

### [25:25 - 25:25]

loop stable.

### [25:25 - 25:27]

loop stable. So what you can think of as going on is

### [25:27 - 25:27]

So what you can think of as going on is

### [25:27 - 25:29]

So what you can think of as going on is that essentially we're just doing a

### [25:29 - 25:29]

that essentially we're just doing a

### [25:29 - 25:30]

that essentially we're just doing a bunch of tricks to reparameterize our

### [25:30 - 25:30]

bunch of tricks to reparameterize our

### [25:30 - 25:32]

bunch of tricks to reparameterize our system into stability.

### [25:32 - 25:32]

system into stability.

### [25:32 - 25:34]

system into stability. So we're using, for example, if we just

### [25:34 - 25:34]

So we're using, for example, if we just

### [25:34 - 25:36]

So we're using, for example, if we just predict raw torques at joints, this

### [25:36 - 25:36]

predict raw torques at joints, this

### [25:36 - 25:37]

predict raw torques at joints, this might be unstable.

### [25:37 - 25:37]

might be unstable.

### [25:37 - 25:39]

might be unstable. We use position or end effector control

### [25:39 - 25:39]

We use position or end effector control

### [25:39 - 25:40]

We use position or end effector control or more generally position tracking

### [25:40 - 25:40]

or more generally position tracking

### [25:40 - 25:43]

or more generally position tracking control to make our system stable.

### [25:43 - 25:43]

control to make our system stable.

### [25:43 - 25:44]

control to make our system stable. But given our lower bound, our negative

### [25:44 - 25:44]

But given our lower bound, our negative

### [25:44 - 25:46]

But given our lower bound, our negative result, stability alone isn't enough to

### [25:46 - 25:46]

result, stability alone isn't enough to

### [25:46 - 25:48]

result, stability alone isn't enough to avoid compounding error. And so we let

### [25:48 - 25:48]

avoid compounding error. And so we let

### [25:48 - 25:50]

avoid compounding error. And so we let we add in action chunking, which makes

### [25:50 - 25:50]

we add in action chunking, which makes

### [25:50 - 25:51]

we add in action chunking, which makes it so that the learned policies

### [25:51 - 25:51]

it so that the learned policies

### [25:51 - 25:54]

it so that the learned policies themselves are stable and therefore

### [25:54 - 25:54]

themselves are stable and therefore

### [25:54 - 25:55]

themselves are stable and therefore don't have compounding error. So we can

### [25:55 - 25:55]

don't have compounding error. So we can

### [25:55 - 25:57]

don't have compounding error. So we can think about all these interventions as

### [25:57 - 25:57]

think about all these interventions as

### [25:57 - 25:58]

think about all these interventions as just building up a control stack that

### [25:58 - 25:58]

just building up a control stack that

### [25:58 - 26:01]

just building up a control stack that provides greater stability.

### [26:01 - 26:01]

provides greater stability.

### [26:01 - 26:02]

provides greater stability. Uh maybe a question, do we need action

### [26:02 - 26:02]

Uh maybe a question, do we need action

### [26:02 - 26:04]

Uh maybe a question, do we need action chunking?

### [26:04 - 26:04]

chunking?

### [26:04 - 26:04]

chunking? Um

### [26:04 - 26:04]

Um

### [26:04 - 26:07]

Um So I think action chunking has some

### [26:07 - 26:07]

So I think action chunking has some

### [26:07 - 26:08]

So I think action chunking has some downsides, right? It makes the policy

### [26:08 - 26:08]

downsides, right? It makes the policy

### [26:08 - 26:11]

downsides, right? It makes the policy far less reactive, which might be which

### [26:11 - 26:11]

far less reactive, which might be which

### [26:11 - 26:12]

far less reactive, which might be which might not work.

### [26:12 - 26:12]

might not work.

### [26:12 - 26:14]

might not work. And it sort of also addresses

### [26:14 - 26:14]

And it sort of also addresses

### [26:14 - 26:15]

And it sort of also addresses instability mostly related to the

### [26:15 - 26:15]

instability mostly related to the

### [26:15 - 26:17]

instability mostly related to the embodiment, right? We cannot use

### [26:17 - 26:17]

embodiment, right? We cannot use

### [26:17 - 26:18]

embodiment, right? We cannot use position control to stabilize the world

### [26:18 - 26:18]

position control to stabilize the world

### [26:18 - 26:19]

position control to stabilize the world around us.

### [26:19 - 26:19]

around us.

### [26:19 - 26:21]

around us. So kind of my vibe conjecture is that as

### [26:21 - 26:21]

So kind of my vibe conjecture is that as

### [26:21 - 26:23]

So kind of my vibe conjecture is that as we move towards more embodied data and

### [26:23 - 26:23]

we move towards more embodied data and

### [26:23 - 26:25]

we move towards more embodied data and and maybe some hierarchical planning, I

### [26:25 - 26:25]

and maybe some hierarchical planning, I

### [26:25 - 26:26]

and maybe some hierarchical planning, I think in the long run we will be able to

### [26:26 - 26:26]

think in the long run we will be able to

### [26:26 - 26:28]

think in the long run we will be able to get rid of action chunking. I also think

### [26:28 - 26:28]

get rid of action chunking. I also think

### [26:28 - 26:29]

get rid of action chunking. I also think that using more like on-policy

### [26:29 - 26:29]

that using more like on-policy

### [26:29 - 26:31]

that using more like on-policy reinforcement learning can directly

### [26:31 - 26:31]

reinforcement learning can directly

### [26:31 - 26:32]

reinforcement learning can directly mitigate these effects. You can kind of

### [26:32 - 26:32]

mitigate these effects. You can kind of

### [26:32 - 26:34]

mitigate these effects. You can kind of prove it or you can just do the

### [26:34 - 26:34]

prove it or you can just do the

### [26:34 - 26:35]

prove it or you can just do the experiments,

### [26:35 - 26:35]

experiments,

### [26:35 - 26:37]

experiments, but I I don't really think I think this

### [26:37 - 26:37]

but I I don't really think I think this

### [26:37 - 26:39]

but I I don't really think I think this is sort of a transient intervention, but

### [26:39 - 26:39]

is sort of a transient intervention, but

### [26:39 - 26:40]

is sort of a transient intervention, but I do think this sort of system one

### [26:40 - 26:40]

I do think this sort of system one

### [26:40 - 26:41]

I do think this sort of system one system two perspective probably has more

### [26:41 - 26:41]

system two perspective probably has more

### [26:41 - 26:44]

system two perspective probably has more longevity.

### [26:44 - 26:44]

longevity.

### [26:44 - 26:45]

longevity. So finally,

### [26:45 - 26:45]

So finally,

### [26:45 - 26:47]

So finally, is action chunking enough? Well, as we

### [26:47 - 26:47]

is action chunking enough? Well, as we

### [26:47 - 26:49]

is action chunking enough? Well, as we alluded to, we can't stabilize objects,

### [26:49 - 26:49]

alluded to, we can't stabilize objects,

### [26:49 - 26:51]

alluded to, we can't stabilize objects, right? There may be cases in robotics

### [26:51 - 26:51]

right? There may be cases in robotics

### [26:51 - 26:52]

right? There may be cases in robotics where we're trying to manipulate or

### [26:52 - 26:52]

where we're trying to manipulate or

### [26:52 - 26:54]

where we're trying to manipulate or interface with the external world and we

### [26:54 - 26:54]

interface with the external world and we

### [26:54 - 26:56]

interface with the external world and we cannot guarantee just because we're

### [26:56 - 26:56]

cannot guarantee just because we're

### [26:56 - 26:57]

cannot guarantee just because we're using certain control in a robot that

### [26:57 - 26:57]

using certain control in a robot that

### [26:57 - 26:59]

using certain control in a robot that the external world will behave the way

### [26:59 - 26:59]

the external world will behave the way

### [26:59 - 27:00]

the external world will behave the way we want it to.

### [27:00 - 27:00]

we want it to.

### [27:00 - 27:02]

we want it to. So are there interventions that might do

### [27:02 - 27:02]

So are there interventions that might do

### [27:02 - 27:05]

So are there interventions that might do better in stabilizing the external

### [27:05 - 27:05]

better in stabilizing the external

### [27:05 - 27:06]

better in stabilizing the external world? And that's what we'll try to

### [27:06 - 27:06]

world? And that's what we'll try to

### [27:06 - 27:07]

world? And that's what we'll try to conclude with.

### [27:07 - 27:07]

conclude with.

### [27:07 - 27:09]

conclude with. So the final intervention we're discuss

### [27:09 - 27:09]

So the final intervention we're discuss

### [27:09 - 27:11]

So the final intervention we're discuss today is generative control, the use of

### [27:11 - 27:11]

today is generative control, the use of

### [27:11 - 27:14]

today is generative control, the use of generative models as control policies

### [27:14 - 27:14]

generative models as control policies

### [27:14 - 27:16]

generative models as control policies uh for this end. Okay. And this was led

### [27:16 - 27:16]

uh for this end. Okay. And this was led

### [27:16 - 27:17]

uh for this end. Okay. And this was led by Chaoyue. He's a PhD student with

### [27:17 - 27:17]

by Chaoyue. He's a PhD student with

### [27:17 - 27:20]

by Chaoyue. He's a PhD student with Guanya Shi.

### [27:20 - 27:20]

Guanya Shi.

### [27:20 - 27:22]

Guanya Shi. So the motivation for generative control

### [27:22 - 27:22]

So the motivation for generative control

### [27:22 - 27:23]

So the motivation for generative control was as follows.

### [27:23 - 27:23]

was as follows.

### [27:23 - 27:25]

was as follows. If we're going to scale up data,

### [27:25 - 27:25]

If we're going to scale up data,

### [27:25 - 27:26]

If we're going to scale up data, we're going to have a bunch of people

### [27:26 - 27:26]

we're going to have a bunch of people

### [27:26 - 27:27]

we're going to have a bunch of people collecting data. Those people might have

### [27:27 - 27:27]

collecting data. Those people might have

### [27:27 - 27:29]

collecting data. Those people might have different ways of solving problems and

### [27:29 - 27:29]

different ways of solving problems and

### [27:29 - 27:31]

different ways of solving problems and so there'll be multiple strategies for

### [27:31 - 27:31]

so there'll be multiple strategies for

### [27:31 - 27:32]

so there'll be multiple strategies for solving problems represented in our data

### [27:32 - 27:32]

solving problems represented in our data

### [27:32 - 27:34]

solving problems represented in our data set. For example, if we have an

### [27:34 - 27:34]

set. For example, if we have an

### [27:34 - 27:36]

set. For example, if we have an obstacle, we might have trajectories

### [27:36 - 27:36]

obstacle, we might have trajectories

### [27:36 - 27:37]

obstacle, we might have trajectories that go above the obstacle or go below

### [27:37 - 27:37]

that go above the obstacle or go below

### [27:37 - 27:39]

that go above the obstacle or go below the obstacle or left or right. And these

### [27:39 - 27:39]

the obstacle or left or right. And these

### [27:39 - 27:41]

the obstacle or left or right. And these will result in multiple modes in the

### [27:41 - 27:41]

will result in multiple modes in the

### [27:41 - 27:43]

will result in multiple modes in the data that we collect.

### [27:43 - 27:43]

data that we collect.

### [27:43 - 27:44]

data that we collect. So as a consequence of this, the

### [27:44 - 27:44]

So as a consequence of this, the

### [27:44 - 27:46]

So as a consequence of this, the distribution of the actions we expect to

### [27:46 - 27:46]

distribution of the actions we expect to

### [27:46 - 27:48]

distribution of the actions we expect to see should have multiple modes that we

### [27:48 - 27:48]

see should have multiple modes that we

### [27:48 - 27:49]

see should have multiple modes that we observe.

### [27:49 - 27:49]

observe.

### [27:49 - 27:51]

observe. Right? So why don't we train policies

### [27:51 - 27:51]

Right? So why don't we train policies

### [27:51 - 27:53]

Right? So why don't we train policies that are capable of representing the

### [27:53 - 27:53]

that are capable of representing the

### [27:53 - 27:54]

that are capable of representing the multiple modes that we see in the action

### [27:54 - 27:54]

multiple modes that we see in the action

### [27:54 - 27:56]

multiple modes that we see in the action distribution? Right? So training

### [27:56 - 27:56]

distribution? Right? So training

### [27:56 - 27:58]

distribution? Right? So training policies that can fit these kinds of

### [27:58 - 27:58]

policies that can fit these kinds of

### [27:58 - 27:59]

policies that can fit these kinds of functions.

### [27:59 - 27:59]

functions.

### [27:59 - 28:01]

functions. So there are a bunch of models that that

### [28:01 - 28:01]

So there are a bunch of models that that

### [28:01 - 28:02]

So there are a bunch of models that that came out just pri- previously to this

### [28:02 - 28:02]

came out just pri- previously to this

### [28:02 - 28:04]

came out just pri- previously to this work, like the diffusion model, which

### [28:04 - 28:04]

work, like the diffusion model, which

### [28:04 - 28:06]

work, like the diffusion model, which were able to do this for images. And so

### [28:06 - 28:06]

were able to do this for images. And so

### [28:06 - 28:08]

were able to do this for images. And so around 2023, some some work like the

### [28:08 - 28:08]

around 2023, some some work like the

### [28:08 - 28:09]

around 2023, some some work like the diffusion policy from from from Chong

### [28:09 - 28:09]

diffusion policy from from from Chong

### [28:09 - 28:12]

diffusion policy from from from Chong Jie formerly Columbia, now at Sanctuary

### [28:12 - 28:12]

Jie formerly Columbia, now at Sanctuary

### [28:12 - 28:13]

Jie formerly Columbia, now at Sanctuary Robotics,

### [28:13 - 28:13]

Robotics,

### [28:13 - 28:15]

Robotics, sort of said, "Okay, well, why don't we

### [28:15 - 28:15]

sort of said, "Okay, well, why don't we

### [28:15 - 28:16]

sort of said, "Okay, well, why don't we just use these like imitative generative

### [28:16 - 28:16]

just use these like imitative generative

### [28:16 - 28:18]

just use these like imitative generative models as a way of parameterizing action

### [28:18 - 28:18]

models as a way of parameterizing action

### [28:18 - 28:20]

models as a way of parameterizing action distributions so I can represent these

### [28:20 - 28:20]

distributions so I can represent these

### [28:20 - 28:24]

distributions so I can represent these complex action distributions over here."

### [28:27 - 28:27]

So today, generative control policies

### [28:27 - 28:29]

So today, generative control policies are the basis for the majority of robot

### [28:29 - 28:29]

are the basis for the majority of robot

### [28:29 - 28:31]

are the basis for the majority of robot VLA models. These are not the kind of

### [28:31 - 28:31]

VLA models. These are not the kind of

### [28:31 - 28:32]

VLA models. These are not the kind of newest, fanciest, shiniest things that

### [28:32 - 28:32]

newest, fanciest, shiniest things that

### [28:32 - 28:34]

newest, fanciest, shiniest things that use VideoGen, though even those are

### [28:34 - 28:34]

use VideoGen, though even those are

### [28:34 - 28:36]

use VideoGen, though even those are using generative models as well.

### [28:36 - 28:36]

using generative models as well.

### [28:36 - 28:38]

using generative models as well. Uh and theoretically, GCPs are are are

### [28:38 - 28:38]

Uh and theoretically, GCPs are are are

### [28:38 - 28:40]

Uh and theoretically, GCPs are are are very powerful, right? They can actually

### [28:40 - 28:40]

very powerful, right? They can actually

### [28:40 - 28:42]

very powerful, right? They can actually imitate arbitrary stochastic expert

### [28:42 - 28:42]

imitate arbitrary stochastic expert

### [28:42 - 28:44]

imitate arbitrary stochastic expert demonstrations and if you use a little

### [28:44 - 28:44]

demonstrations and if you use a little

### [28:44 - 28:45]

demonstrations and if you use a little bit of low-level control, you can also

### [28:45 - 28:45]

bit of low-level control, you can also

### [28:45 - 28:48]

bit of low-level control, you can also make them do so stably.

### [28:48 - 28:48]

make them do so stably.

### [28:48 - 28:50]

make them do so stably. So to stress, like generative control, I

### [28:50 - 28:50]

So to stress, like generative control, I

### [28:50 - 28:52]

So to stress, like generative control, I think from a public point of view, is is

### [28:52 - 28:52]

think from a public point of view, is is

### [28:52 - 28:53]

think from a public point of view, is is kind of considered one of the

### [28:53 - 28:53]

kind of considered one of the

### [28:53 - 28:55]

kind of considered one of the technologies that's that's that's

### [28:55 - 28:55]

technologies that's that's that's

### [28:55 - 28:56]

technologies that's that's that's regarded for like the revolution in

### [28:56 - 28:56]

regarded for like the revolution in

### [28:56 - 28:58]

regarded for like the revolution in robot capabilities. It's suddenly things

### [28:58 - 28:58]

robot capabilities. It's suddenly things

### [28:58 - 28:59]

robot capabilities. It's suddenly things change when we started using generative

### [28:59 - 28:59]

change when we started using generative

### [28:59 - 29:00]

change when we started using generative models.

### [29:00 - 29:00]

models.

### [29:00 - 29:03]

models. And even kind of the most frontier VLAs

### [29:03 - 29:03]

And even kind of the most frontier VLAs

### [29:03 - 29:04]

And even kind of the most frontier VLAs still are using something like a

### [29:04 - 29:04]

still are using something like a

### [29:04 - 29:07]

still are using something like a flow-based model to do this prediction.

### [29:07 - 29:07]

flow-based model to do this prediction.

### [29:07 - 29:09]

flow-based model to do this prediction. So what do you do with a generative

### [29:09 - 29:09]

So what do you do with a generative

### [29:09 - 29:11]

So what do you do with a generative model or generative control policy?

### [29:11 - 29:11]

model or generative control policy?

### [29:11 - 29:12]

model or generative control policy? Well, you just take your loss function

### [29:12 - 29:12]

Well, you just take your loss function

### [29:12 - 29:14]

Well, you just take your loss function in behavior cloning and you replace it

### [29:14 - 29:14]

in behavior cloning and you replace it

### [29:14 - 29:16]

in behavior cloning and you replace it with a distribution fitting objective.

### [29:16 - 29:16]

with a distribution fitting objective.

### [29:16 - 29:17]

with a distribution fitting objective. So for example, you can use the flow

### [29:17 - 29:17]

So for example, you can use the flow

### [29:17 - 29:19]

So for example, you can use the flow matching objective. I'm sure many of us

### [29:19 - 29:19]

matching objective. I'm sure many of us

### [29:19 - 29:21]

matching objective. I'm sure many of us are familiar with this. Essentially,

### [29:21 - 29:21]

are familiar with this. Essentially,

### [29:21 - 29:22]

are familiar with this. Essentially, what flow matching does is it learns to

### [29:22 - 29:22]

what flow matching does is it learns to

### [29:22 - 29:24]

what flow matching does is it learns to interpolate between actions and pure

### [29:24 - 29:24]

interpolate between actions and pure

### [29:24 - 29:26]

interpolate between actions and pure noise and it learns the velocity or the

### [29:26 - 29:26]

noise and it learns the velocity or the

### [29:26 - 29:29]

noise and it learns the velocity or the average velocity velocity between the

### [29:29 - 29:29]

average velocity velocity between the

### [29:29 - 29:30]

average velocity velocity between the line between them, which is just going

### [29:30 - 29:30]

line between them, which is just going

### [29:30 - 29:31]

line between them, which is just going to be given by the difference between

### [29:31 - 29:31]

to be given by the difference between

### [29:31 - 29:33]

to be given by the difference between the noise and the action.

### [29:33 - 29:33]

the noise and the action.

### [29:33 - 29:35]

the noise and the action. And you fit this velocity field and then

### [29:35 - 29:35]

And you fit this velocity field and then

### [29:35 - 29:37]

And you fit this velocity field and then if you want to generate an action, you

### [29:37 - 29:37]

if you want to generate an action, you

### [29:37 - 29:39]

if you want to generate an action, you initialize the initialize the action as

### [29:39 - 29:39]

initialize the initialize the action as

### [29:39 - 29:41]

initialize the initialize the action as pure Gaussian noise and then you evolve

### [29:41 - 29:41]

pure Gaussian noise and then you evolve

### [29:41 - 29:43]

pure Gaussian noise and then you evolve the ODE back in time. This would

### [29:43 - 29:43]

the ODE back in time. This would

### [29:43 - 29:44]

the ODE back in time. This would probably be a negative sign giving you

### [29:44 - 29:44]

probably be a negative sign giving you

### [29:44 - 29:46]

probably be a negative sign giving you an action because you're learning this

### [29:46 - 29:46]

an action because you're learning this

### [29:46 - 29:49]

an action because you're learning this velocity field which defines an ODE.

### [29:49 - 29:49]

velocity field which defines an ODE.

### [29:49 - 29:51]

velocity field which defines an ODE. So, the main question we're going to try

### [29:51 - 29:51]

So, the main question we're going to try

### [29:51 - 29:53]

So, the main question we're going to try to ask is, are these generative control

### [29:53 - 29:53]

to ask is, are these generative control

### [29:53 - 29:54]

to ask is, are these generative control policies are they really about

### [29:54 - 29:54]

policies are they really about

### [29:54 - 29:56]

policies are they really about distribution matching? Or are they

### [29:56 - 29:56]

distribution matching? Or are they

### [29:56 - 29:58]

distribution matching? Or are they giving us something else? And maybe

### [29:58 - 29:58]

giving us something else? And maybe

### [29:58 - 29:59]

giving us something else? And maybe giving us something else that's related

### [29:59 - 29:59]

giving us something else that's related

### [29:59 - 30:00]

giving us something else that's related to some of the control perspective that

### [30:00 - 30:00]

to some of the control perspective that

### [30:00 - 30:02]

to some of the control perspective that we've described described earlier. So,

### [30:02 - 30:02]

we've described described earlier. So,

### [30:02 - 30:04]

we've described described earlier. So, that's what I'm going to try to argue.

### [30:04 - 30:04]

that's what I'm going to try to argue.

### [30:04 - 30:06]

that's what I'm going to try to argue. So, in order to understand what

### [30:06 - 30:06]

So, in order to understand what

### [30:06 - 30:07]

So, in order to understand what generative control policies are giving

### [30:07 - 30:07]

generative control policies are giving

### [30:07 - 30:09]

generative control policies are giving us, it's useful to kind of disambiguate

### [30:09 - 30:09]

us, it's useful to kind of disambiguate

### [30:09 - 30:11]

us, it's useful to kind of disambiguate the different design decisions that go

### [30:11 - 30:11]

the different design decisions that go

### [30:11 - 30:13]

the different design decisions that go into a generative control policy.

### [30:13 - 30:13]

into a generative control policy.

### [30:13 - 30:14]

into a generative control policy. So, we came up with a taxonomy that

### [30:14 - 30:14]

So, we came up with a taxonomy that

### [30:14 - 30:17]

So, we came up with a taxonomy that includes three of them. The first is the

### [30:17 - 30:17]

includes three of them. The first is the

### [30:17 - 30:18]

includes three of them. The first is the one that's most visible, the one that

### [30:18 - 30:18]

one that's most visible, the one that

### [30:18 - 30:19]

one that's most visible, the one that they were motivated for, which is

### [30:19 - 30:19]

they were motivated for, which is

### [30:19 - 30:21]

they were motivated for, which is distributional learning. A flow model, a

### [30:21 - 30:21]

distributional learning. A flow model, a

### [30:21 - 30:23]

distributional learning. A flow model, a diffusion model can validly approximate

### [30:23 - 30:23]

diffusion model can validly approximate

### [30:23 - 30:24]

diffusion model can validly approximate any conditional distribution if your

### [30:24 - 30:24]

any conditional distribution if your

### [30:24 - 30:25]

any conditional distribution if your neural network is big enough, if you've

### [30:25 - 30:25]

neural network is big enough, if you've

### [30:25 - 30:28]

neural network is big enough, if you've got enough data.

### [30:28 - 30:28]

got enough data.

### [30:28 - 30:29]

got enough data. Right? So, that's where this

### [30:29 - 30:29]

Right? So, that's where this

### [30:29 - 30:31]

Right? So, that's where this multimodality that we care about.

### [30:31 - 30:31]

multimodality that we care about.

### [30:31 - 30:34]

multimodality that we care about. Now, the second is uh stochasticity.

### [30:34 - 30:34]

Now, the second is uh stochasticity.

### [30:34 - 30:36]

Now, the second is uh stochasticity. When we train a a generative model, most

### [30:36 - 30:36]

When we train a a generative model, most

### [30:36 - 30:37]

When we train a a generative model, most of the very popular ones include a

### [30:37 - 30:37]

of the very popular ones include a

### [30:37 - 30:39]

of the very popular ones include a little bit of Gaussian noise in the way

### [30:39 - 30:39]

little bit of Gaussian noise in the way

### [30:39 - 30:40]

little bit of Gaussian noise in the way that they're trained, and you might

### [30:40 - 30:40]

that they're trained, and you might

### [30:40 - 30:41]

that they're trained, and you might think that this improves training

### [30:41 - 30:41]

think that this improves training

### [30:41 - 30:42]

think that this improves training dynamics, it improves representation

### [30:42 - 30:42]

dynamics, it improves representation

### [30:42 - 30:43]

dynamics, it improves representation learning, it functions as data

### [30:43 - 30:43]

learning, it functions as data

### [30:43 - 30:46]

learning, it functions as data augmentation. And so, maybe the use of

### [30:46 - 30:46]

augmentation. And so, maybe the use of

### [30:46 - 30:48]

augmentation. And so, maybe the use of stochasticity is the thing that's really

### [30:48 - 30:48]

stochasticity is the thing that's really

### [30:48 - 30:50]

stochasticity is the thing that's really important here.

### [30:50 - 30:50]

important here.

### [30:50 - 30:52]

important here. And then last thing is that is this idea

### [30:52 - 30:52]

And then last thing is that is this idea

### [30:52 - 30:53]

And then last thing is that is this idea of iterative computation, right? So,

### [30:53 - 30:53]

of iterative computation, right? So,

### [30:53 - 30:54]

of iterative computation, right? So, we've seen in language models, for

### [30:54 - 30:54]

we've seen in language models, for

### [30:54 - 30:56]

we've seen in language models, for example, that chain of thought, multiple

### [30:56 - 30:56]

example, that chain of thought, multiple

### [30:56 - 30:58]

example, that chain of thought, multiple steps are are really useful for

### [30:58 - 30:58]

steps are are really useful for

### [30:58 - 31:00]

steps are are really useful for representing more complicated outputs.

### [31:00 - 31:00]

representing more complicated outputs.

### [31:00 - 31:01]

representing more complicated outputs. And maybe something else is going on

### [31:01 - 31:01]

And maybe something else is going on

### [31:01 - 31:02]

And maybe something else is going on here as well, something similar is going

### [31:02 - 31:02]

here as well, something similar is going

### [31:02 - 31:04]

here as well, something similar is going on here, right? So, here when we use a

### [31:04 - 31:04]

on here, right? So, here when we use a

### [31:04 - 31:06]

on here, right? So, here when we use a flow model, we take multiple steps by

### [31:06 - 31:06]

flow model, we take multiple steps by

### [31:06 - 31:08]

flow model, we take multiple steps by integrating this ODE, we use Euler

### [31:08 - 31:08]

integrating this ODE, we use Euler

### [31:08 - 31:10]

integrating this ODE, we use Euler discretization. So, we might have five

### [31:10 - 31:10]

discretization. So, we might have five

### [31:10 - 31:11]

discretization. So, we might have five or 10 steps to predict an action rather

### [31:11 - 31:11]

or 10 steps to predict an action rather

### [31:11 - 31:14]

or 10 steps to predict an action rather than predicting in a single step.

### [31:14 - 31:14]

than predicting in a single step.

### [31:14 - 31:15]

than predicting in a single step. Now, in a little bit more detail, what

### [31:15 - 31:15]

Now, in a little bit more detail, what

### [31:15 - 31:17]

Now, in a little bit more detail, what we actually do in a flow model is called

### [31:17 - 31:17]

we actually do in a flow model is called

### [31:17 - 31:19]

we actually do in a flow model is called supervised iterative computation.

### [31:19 - 31:19]

supervised iterative computation.

### [31:19 - 31:20]

supervised iterative computation. Where if we look at the flow matching

### [31:20 - 31:20]

Where if we look at the flow matching

### [31:20 - 31:22]

Where if we look at the flow matching loss, it's kind of supervising the

### [31:22 - 31:22]

loss, it's kind of supervising the

### [31:22 - 31:24]

loss, it's kind of supervising the velocity field at every step of this

### [31:24 - 31:24]

velocity field at every step of this

### [31:24 - 31:26]

velocity field at every step of this denoising process. So, every step of

### [31:26 - 31:26]

denoising process. So, every step of

### [31:26 - 31:28]

denoising process. So, every step of this is being supervised. And so, it's

### [31:28 - 31:28]

this is being supervised. And so, it's

### [31:28 - 31:30]

this is being supervised. And so, it's giving us like dense information around

### [31:30 - 31:30]

giving us like dense information around

### [31:30 - 31:31]

giving us like dense information around every step of our kind of like internal

### [31:31 - 31:31]

every step of our kind of like internal

### [31:31 - 31:33]

every step of our kind of like internal thinking.

### [31:33 - 31:33]

thinking.

### [31:33 - 31:35]

thinking. So, these are the components. So, let's

### [31:35 - 31:35]

So, these are the components. So, let's

### [31:35 - 31:36]

So, these are the components. So, let's try to understand which components

### [31:36 - 31:36]

try to understand which components

### [31:36 - 31:38]

try to understand which components actually matter.

### [31:38 - 31:38]

actually matter.

### [31:38 - 31:39]

actually matter. Are generative control policies doing

### [31:39 - 31:39]

Are generative control policies doing

### [31:39 - 31:41]

Are generative control policies doing distribution learning?

### [31:41 - 31:41]

distribution learning?

### [31:41 - 31:42]

distribution learning? So, I want to make a caveat cuz

### [31:42 - 31:42]

So, I want to make a caveat cuz

### [31:42 - 31:43]

So, I want to make a caveat cuz yesterday Katerina brought up a really

### [31:43 - 31:43]

yesterday Katerina brought up a really

### [31:43 - 31:46]

yesterday Katerina brought up a really good point. For this talk, we're talking

### [31:46 - 31:46]

good point. For this talk, we're talking

### [31:46 - 31:48]

good point. For this talk, we're talking about reactive control policies. So, you

### [31:48 - 31:48]

about reactive control policies. So, you

### [31:48 - 31:50]

about reactive control policies. So, you could also use diffusion for planning,

### [31:50 - 31:50]

could also use diffusion for planning,

### [31:50 - 31:51]

could also use diffusion for planning, you could use it for key pose

### [31:51 - 31:51]

you could use it for key pose

### [31:51 - 31:52]

you could use it for key pose prediction, you could use it for key

### [31:52 - 31:52]

prediction, you could use it for key

### [31:52 - 31:54]

prediction, you could use it for key frame prediction. In those cases, you

### [31:54 - 31:54]

frame prediction. In those cases, you

### [31:54 - 31:56]

frame prediction. In those cases, you will probably see a lot of multimodality

### [31:56 - 31:56]

will probably see a lot of multimodality

### [31:56 - 31:57]

will probably see a lot of multimodality because you're predicting things long

### [31:57 - 31:57]

because you're predicting things long

### [31:57 - 31:59]

because you're predicting things long into the future. Right? But in this

### [31:59 - 31:59]

into the future. Right? But in this

### [31:59 - 32:00]

into the future. Right? But in this talk, we're focusing on reactive control

### [32:00 - 32:00]

talk, we're focusing on reactive control

### [32:00 - 32:02]

talk, we're focusing on reactive control policies, which are rather more near

### [32:02 - 32:02]

policies, which are rather more near

### [32:02 - 32:03]

policies, which are rather more near term.

### [32:03 - 32:03]

term.

### [32:03 - 32:04]

term. And for reactive control policies, what

### [32:04 - 32:04]

And for reactive control policies, what

### [32:04 - 32:07]

And for reactive control policies, what we did is we compared to um between

### [32:07 - 32:07]

we did is we compared to um between

### [32:07 - 32:09]

we did is we compared to um between flow-based policies and regression-based

### [32:09 - 32:09]

flow-based policies and regression-based

### [32:09 - 32:11]

flow-based policies and regression-based policies across a range of tasks, from

### [32:11 - 32:11]

policies across a range of tasks, from

### [32:11 - 32:13]

policies across a range of tasks, from mostly from simulated environments. Now,

### [32:13 - 32:13]

mostly from simulated environments. Now,

### [32:13 - 32:15]

mostly from simulated environments. Now, simulation has its weaknesses, but a lot

### [32:15 - 32:15]

simulation has its weaknesses, but a lot

### [32:15 - 32:17]

simulation has its weaknesses, but a lot of these simulations were mainly mainly

### [32:17 - 32:17]

of these simulations were mainly mainly

### [32:17 - 32:19]

of these simulations were mainly mainly the simulations that were claimed as the

### [32:19 - 32:19]

the simulations that were claimed as the

### [32:19 - 32:20]

the simulations that were claimed as the reason for why you need generative

### [32:20 - 32:20]

reason for why you need generative

### [32:20 - 32:21]

reason for why you need generative control policies. And these include many

### [32:21 - 32:21]

control policies. And these include many

### [32:21 - 32:23]

control policies. And these include many conventionally multimodal simulation

### [32:23 - 32:23]

conventionally multimodal simulation

### [32:23 - 32:26]

conventionally multimodal simulation tasks. So, what we do is we plot in gray

### [32:26 - 32:26]

tasks. So, what we do is we plot in gray

### [32:26 - 32:28]

tasks. So, what we do is we plot in gray the performance of a regression policy.

### [32:28 - 32:28]

the performance of a regression policy.

### [32:28 - 32:29]

the performance of a regression policy. Sorry, it's so faint on this. Maybe this

### [32:29 - 32:29]

Sorry, it's so faint on this. Maybe this

### [32:29 - 32:30]

Sorry, it's so faint on this. Maybe this is not a

### [32:30 - 32:30]

is not a

### [32:30 - 32:31]

is not a uh presentation optimized uh color

### [32:31 - 32:31]

uh presentation optimized uh color

### [32:31 - 32:34]

uh presentation optimized uh color scheme. Uh And what we do here this this

### [32:34 - 32:34]

scheme. Uh And what we do here this this

### [32:34 - 32:37]

scheme. Uh And what we do here this this gray this red dotted line, this denotes

### [32:37 - 32:37]

gray this red dotted line, this denotes

### [32:37 - 32:38]

gray this red dotted line, this denotes where the regression policy dips below

### [32:38 - 32:38]

where the regression policy dips below

### [32:38 - 32:41]

where the regression policy dips below 95% of the flow-based policy.

### [32:41 - 32:41]

95% of the flow-based policy.

### [32:41 - 32:42]

95% of the flow-based policy. So, we see that actually in the

### [32:42 - 32:42]

So, we see that actually in the

### [32:42 - 32:44]

So, we see that actually in the overwhelming majority of tasks with lots

### [32:44 - 32:44]

overwhelming majority of tasks with lots

### [32:44 - 32:46]

overwhelming majority of tasks with lots of image modalities, different VLA

### [32:46 - 32:46]

of image modalities, different VLA

### [32:46 - 32:48]

of image modalities, different VLA backbone states, images, 3D point

### [32:48 - 32:48]

backbone states, images, 3D point

### [32:48 - 32:49]

backbone states, images, 3D point clouds, flow-based policies and

### [32:49 - 32:49]

clouds, flow-based policies and

### [32:49 - 32:50]

clouds, flow-based policies and regression-based policies are

### [32:50 - 32:50]

regression-based policies are

### [32:50 - 32:52]

regression-based policies are competitive.

### [32:52 - 32:52]

competitive.

### [32:52 - 32:53]

competitive. So, why didn't people notice this

### [32:53 - 32:53]

So, why didn't people notice this

### [32:53 - 32:55]

So, why didn't people notice this before?

### [32:55 - 32:55]

before?

### [32:55 - 32:56]

before? Well, one important thing is you need to

### [32:56 - 32:56]

Well, one important thing is you need to

### [32:56 - 32:58]

Well, one important thing is you need to control for architecture. So, it turns

### [32:58 - 32:58]

control for architecture. So, it turns

### [32:58 - 32:59]

control for architecture. So, it turns out the diffusion transformer with its

### [32:59 - 32:59]

out the diffusion transformer with its

### [32:59 - 33:01]

out the diffusion transformer with its outer layer norm is also a wonderful way

### [33:01 - 33:01]

outer layer norm is also a wonderful way

### [33:01 - 33:03]

outer layer norm is also a wonderful way to train a regression model. But uh in

### [33:03 - 33:03]

to train a regression model. But uh in

### [33:03 - 33:05]

to train a regression model. But uh in the original papers,

### [33:05 - 33:05]

the original papers,

### [33:05 - 33:07]

the original papers, they bladed an MLP with regression

### [33:07 - 33:07]

they bladed an MLP with regression

### [33:07 - 33:08]

they bladed an MLP with regression against a transformer with something

### [33:08 - 33:08]

against a transformer with something

### [33:08 - 33:09]

against a transformer with something else. People hadn't done other forms of

### [33:09 - 33:09]

else. People hadn't done other forms of

### [33:09 - 33:10]

else. People hadn't done other forms of transformer architectures for

### [33:10 - 33:10]

transformer architectures for

### [33:10 - 33:12]

transformer architectures for regression, but not the specific kind of

### [33:12 - 33:12]

regression, but not the specific kind of

### [33:12 - 33:14]

regression, but not the specific kind of bells and whistles that were used in

### [33:14 - 33:14]

bells and whistles that were used in

### [33:14 - 33:15]

bells and whistles that were used in diffusion, and these seem to work very

### [33:15 - 33:15]

diffusion, and these seem to work very

### [33:15 - 33:16]

diffusion, and these seem to work very well.

### [33:16 - 33:16]

well.

### [33:16 - 33:18]

well. Um but it's still the case that there

### [33:18 - 33:18]

Um but it's still the case that there

### [33:18 - 33:20]

Um but it's still the case that there are many tasks on this this this handful

### [33:20 - 33:20]

are many tasks on this this this handful

### [33:20 - 33:22]

are many tasks on this this this handful over here where flow-based models are

### [33:22 - 33:22]

over here where flow-based models are

### [33:22 - 33:23]

over here where flow-based models are still doing much better. So, let's try

### [33:23 - 33:23]

still doing much better. So, let's try

### [33:23 - 33:27]

still doing much better. So, let's try to understand what what they are.

### [33:29 - 33:29]

Um So, are the improvements on tasks

### [33:29 - 33:31]

Um So, are the improvements on tasks that have very explicit multimodality,

### [33:31 - 33:31]

that have very explicit multimodality,

### [33:31 - 33:33]

that have very explicit multimodality, explicitly many solutions. Again, this

### [33:33 - 33:33]

explicitly many solutions. Again, this

### [33:33 - 33:35]

explicitly many solutions. Again, this is reactive control policies and not key

### [33:35 - 33:35]

is reactive control policies and not key

### [33:35 - 33:37]

is reactive control policies and not key frame prediction. So, our first finding

### [33:37 - 33:37]

frame prediction. So, our first finding

### [33:37 - 33:38]

frame prediction. So, our first finding is that the tasks where it seems that

### [33:38 - 33:38]

is that the tasks where it seems that

### [33:38 - 33:40]

is that the tasks where it seems that flow policies do the best are actually

### [33:40 - 33:40]

flow policies do the best are actually

### [33:40 - 33:42]

flow policies do the best are actually those that require lots of high

### [33:42 - 33:42]

those that require lots of high

### [33:42 - 33:44]

those that require lots of high precision, things like tool insertion.

### [33:44 - 33:44]

precision, things like tool insertion.

### [33:44 - 33:46]

precision, things like tool insertion. Um okay.

### [33:46 - 33:46]

Um okay.

### [33:46 - 33:48]

Um okay. The second is, can we look at the tasks

### [33:48 - 33:48]

The second is, can we look at the tasks

### [33:48 - 33:49]

The second is, can we look at the tasks where flow and regression are

### [33:49 - 33:49]

where flow and regression are

### [33:49 - 33:51]

where flow and regression are competitive, but maybe ask if flow is

### [33:51 - 33:51]

competitive, but maybe ask if flow is

### [33:51 - 33:52]

competitive, but maybe ask if flow is still learning to be multimodal in some

### [33:52 - 33:52]

still learning to be multimodal in some

### [33:52 - 33:53]

still learning to be multimodal in some way?

### [33:53 - 33:53]

way?

### [33:53 - 33:56]

way? So, let's do that. First, what we did is

### [33:56 - 33:56]

So, let's do that. First, what we did is

### [33:56 - 33:57]

So, let's do that. First, what we did is we visualize the action distributions

### [33:57 - 33:57]

we visualize the action distributions

### [33:57 - 34:00]

we visualize the action distributions either on the in the image space or with

### [34:00 - 34:00]

either on the in the image space or with

### [34:00 - 34:02]

either on the in the image space or with like a UMAP embedding. And we even color

### [34:02 - 34:02]

like a UMAP embedding. And we even color

### [34:02 - 34:04]

like a UMAP embedding. And we even color coded the actions by their return to go,

### [34:04 - 34:04]

coded the actions by their return to go,

### [34:04 - 34:06]

coded the actions by their return to go, so how good the action is. And what we

### [34:06 - 34:06]

so how good the action is. And what we

### [34:06 - 34:09]

so how good the action is. And what we see is no perceptible multimodality. And

### [34:09 - 34:09]

see is no perceptible multimodality. And

### [34:09 - 34:11]

see is no perceptible multimodality. And in fact, we also don't even see that

### [34:11 - 34:11]

in fact, we also don't even see that

### [34:11 - 34:12]

in fact, we also don't even see that there's any really any real pattern

### [34:12 - 34:12]

there's any really any real pattern

### [34:12 - 34:14]

there's any really any real pattern between how good the action is and where

### [34:14 - 34:14]

between how good the action is and where

### [34:14 - 34:16]

between how good the action is and where the action lies in the visualization.

### [34:16 - 34:16]

the action lies in the visualization.

### [34:16 - 34:17]

the action lies in the visualization. Now, of course, there are limitations to

### [34:17 - 34:17]

Now, of course, there are limitations to

### [34:17 - 34:18]

Now, of course, there are limitations to these visualization tools, but at least

### [34:18 - 34:18]

these visualization tools, but at least

### [34:18 - 34:21]

these visualization tools, but at least perceptibly, there's no multimodality.

### [34:21 - 34:21]

perceptibly, there's no multimodality.

### [34:21 - 34:22]

perceptibly, there's no multimodality. But of course, like there's so many

### [34:22 - 34:22]

But of course, like there's so many

### [34:22 - 34:24]

But of course, like there's so many limitations with visualization alone, so

### [34:24 - 34:24]

limitations with visualization alone, so

### [34:24 - 34:25]

limitations with visualization alone, so we need another experiment.

### [34:25 - 34:25]

we need another experiment.

### [34:25 - 34:27]

we need another experiment. So, what we did here is we took three

### [34:27 - 34:27]

So, what we did here is we took three

### [34:27 - 34:29]

So, what we did here is we took three ways of doing inference on the control

### [34:29 - 34:29]

ways of doing inference on the control

### [34:29 - 34:31]

ways of doing inference on the control policy. That's uh so, flow policy, it

### [34:31 - 34:31]

policy. That's uh so, flow policy, it

### [34:31 - 34:33]

policy. That's uh so, flow policy, it takes initial Gaussian noise, it maps it

### [34:33 - 34:33]

takes initial Gaussian noise, it maps it

### [34:33 - 34:35]

takes initial Gaussian noise, it maps it by integrating an ODE to an action.

### [34:35 - 34:35]

by integrating an ODE to an action.

### [34:35 - 34:36]

by integrating an ODE to an action. So, you can either take the initial

### [34:36 - 34:36]

So, you can either take the initial

### [34:36 - 34:38]

So, you can either take the initial noise to be Gaussian.

### [34:38 - 34:38]

noise to be Gaussian.

### [34:38 - 34:39]

noise to be Gaussian. You can set the initial noise to be

### [34:39 - 34:39]

You can set the initial noise to be

### [34:39 - 34:41]

You can set the initial noise to be zero. Or you could do something that

### [34:41 - 34:41]

zero. Or you could do something that

### [34:41 - 34:42]

zero. Or you could do something that will explicitly destroy the

### [34:42 - 34:42]

will explicitly destroy the

### [34:42 - 34:44]

will explicitly destroy the multimodality. You can sample 64 noise

### [34:44 - 34:44]

multimodality. You can sample 64 noise

### [34:44 - 34:46]

multimodality. You can sample 64 noise seeds, take all the actions that you get

### [34:46 - 34:46]

seeds, take all the actions that you get

### [34:46 - 34:48]

seeds, take all the actions that you get from those noises, and just average them

### [34:48 - 34:48]

from those noises, and just average them

### [34:48 - 34:49]

from those noises, and just average them together. So, effectively, you're

### [34:49 - 34:49]

together. So, effectively, you're

### [34:49 - 34:51]

together. So, effectively, you're approximating this distribution with its

### [34:51 - 34:51]

approximating this distribution with its

### [34:51 - 34:52]

approximating this distribution with its mean.

### [34:52 - 34:52]

mean.

### [34:52 - 34:53]

mean. Right? So, this destroys any

### [34:53 - 34:53]

Right? So, this destroys any

### [34:53 - 34:55]

Right? So, this destroys any multimodality, and what we find is if

### [34:55 - 34:55]

multimodality, and what we find is if

### [34:55 - 34:56]

multimodality, and what we find is if you do this, you lose a bit of

### [34:56 - 34:56]

you do this, you lose a bit of

### [34:56 - 34:57]

you do this, you lose a bit of performance, but you only lose 2%

### [34:57 - 34:57]

performance, but you only lose 2%

### [34:57 - 34:58]

performance, but you only lose 2% performance.

### [34:58 - 34:58]

performance.

### [34:58 - 35:01]

performance. Very, very little. So, at least the

### [35:01 - 35:01]

Very, very little. So, at least the

### [35:01 - 35:02]

Very, very little. So, at least the representation of multimodality in these

### [35:02 - 35:02]

representation of multimodality in these

### [35:02 - 35:04]

representation of multimodality in these policies does not seem to be

### [35:04 - 35:04]

policies does not seem to be

### [35:04 - 35:06]

policies does not seem to be particularly helpful, right? You can

### [35:06 - 35:06]

particularly helpful, right? You can

### [35:06 - 35:08]

particularly helpful, right? You can basically destroy it, and and they work

### [35:08 - 35:08]

basically destroy it, and and they work

### [35:08 - 35:09]

basically destroy it, and and they work pretty well.

### [35:09 - 35:09]

pretty well.

### [35:09 - 35:11]

pretty well. Now, the final question is, what happens

### [35:11 - 35:11]

Now, the final question is, what happens

### [35:11 - 35:13]

Now, the final question is, what happens if you try to relabel the data so that

### [35:13 - 35:13]

if you try to relabel the data so that

### [35:13 - 35:14]

if you try to relabel the data so that the data is deterministic and high

### [35:14 - 35:14]

the data is deterministic and high

### [35:14 - 35:16]

the data is deterministic and high quality?

### [35:16 - 35:16]

quality?

### [35:16 - 35:17]

quality? So, if you relabel your data so it's

### [35:17 - 35:17]

So, if you relabel your data so it's

### [35:17 - 35:19]

So, if you relabel your data so it's higher quality, you actually do see a

### [35:19 - 35:19]

higher quality, you actually do see a

### [35:19 - 35:21]

higher quality, you actually do see a slight narrowing of the gap between a

### [35:21 - 35:21]

slight narrowing of the gap between a

### [35:21 - 35:22]

slight narrowing of the gap between a flow and a regression model, right? They

### [35:22 - 35:22]

flow and a regression model, right? They

### [35:22 - 35:24]

flow and a regression model, right? They regression does get better, flow gets

### [35:24 - 35:24]

regression does get better, flow gets

### [35:24 - 35:25]

regression does get better, flow gets worse depending on how we did the

### [35:25 - 35:25]

worse depending on how we did the

### [35:25 - 35:26]

worse depending on how we did the relabeling.

### [35:26 - 35:26]

relabeling.

### [35:26 - 35:28]

relabeling. Uh but you still see this gap, right?

### [35:28 - 35:28]

Uh but you still see this gap, right?

### [35:28 - 35:30]

Uh but you still see this gap, right? So, even from deterministic data, it

### [35:30 - 35:30]

So, even from deterministic data, it

### [35:30 - 35:33]

So, even from deterministic data, it seems that there's some benefit to flow

### [35:33 - 35:33]

seems that there's some benefit to flow

### [35:33 - 35:35]

seems that there's some benefit to flow over regression.

### [35:35 - 35:35]

over regression.

### [35:35 - 35:37]

over regression. So, what's going on?

### [35:37 - 35:37]

So, what's going on?

### [35:37 - 35:39]

So, what's going on? Well, at least we can say that in the

### [35:39 - 35:39]

Well, at least we can say that in the

### [35:39 - 35:39]

Well, at least we can say that in the tasks that we're studying,

### [35:39 - 35:39]

tasks that we're studying,

### [35:39 - 35:41]

tasks that we're studying, distributional learning is not the main

### [35:41 - 35:41]

distributional learning is not the main

### [35:41 - 35:42]

distributional learning is not the main component. I think when you move to the

### [35:42 - 35:42]

component. I think when you move to the

### [35:42 - 35:44]

component. I think when you move to the pretraining scale, it certainly is, and

### [35:44 - 35:44]

pretraining scale, it certainly is, and

### [35:44 - 35:45]

pretraining scale, it certainly is, and I still think that you should pretrain

### [35:45 - 35:45]

I still think that you should pretrain

### [35:45 - 35:47]

I still think that you should pretrain the flow policy, so don't get me wrong.

### [35:47 - 35:47]

the flow policy, so don't get me wrong.

### [35:47 - 35:48]

the flow policy, so don't get me wrong. I think the point of this talk is more

### [35:48 - 35:48]

I think the point of this talk is more

### [35:48 - 35:50]

I think the point of this talk is more to understand other mechanisms that flow

### [35:50 - 35:50]

to understand other mechanisms that flow

### [35:50 - 35:51]

to understand other mechanisms that flow policies might be doing that are

### [35:51 - 35:51]

policies might be doing that are

### [35:51 - 35:53]

policies might be doing that are underappreciated.

### [35:53 - 35:53]

underappreciated.

### [35:53 - 35:55]

underappreciated. So, what we're going to try to do to

### [35:55 - 35:55]

So, what we're going to try to do to

### [35:55 - 35:57]

So, what we're going to try to do to understand what factors are contributing

### [35:57 - 35:57]

understand what factors are contributing

### [35:57 - 35:58]

understand what factors are contributing to flow success, is we're going to try

### [35:58 - 35:58]

to flow success, is we're going to try

### [35:58 - 36:01]

to flow success, is we're going to try to design an algorithm as an ablation.

### [36:01 - 36:01]

to design an algorithm as an ablation.

### [36:01 - 36:02]

to design an algorithm as an ablation. So, we're going to try to design an an

### [36:02 - 36:02]

So, we're going to try to design an an

### [36:02 - 36:04]

So, we're going to try to design an an algorithm which does not correctly

### [36:04 - 36:04]

algorithm which does not correctly

### [36:04 - 36:06]

algorithm which does not correctly approximate distributions, but which

### [36:06 - 36:06]

approximate distributions, but which

### [36:06 - 36:07]

approximate distributions, but which exhibits the stochasticity and the

### [36:07 - 36:07]

exhibits the stochasticity and the

### [36:07 - 36:09]

exhibits the stochasticity and the supervised iterative computation that

### [36:09 - 36:09]

supervised iterative computation that

### [36:09 - 36:11]

supervised iterative computation that are observed in flow models. And if

### [36:11 - 36:11]

are observed in flow models. And if

### [36:11 - 36:12]

are observed in flow models. And if these things do as well, that kind of

### [36:12 - 36:12]

these things do as well, that kind of

### [36:12 - 36:14]

these things do as well, that kind of gives us evidence that these two

### [36:14 - 36:14]

gives us evidence that these two

### [36:14 - 36:15]

gives us evidence that these two components are really the salient

### [36:15 - 36:15]

components are really the salient

### [36:15 - 36:16]

components are really the salient factors.

### [36:16 - 36:16]

factors.

### [36:16 - 36:18]

factors. So, that policy is very simple. Uh the

### [36:18 - 36:18]

So, that policy is very simple. Uh the

### [36:18 - 36:20]

So, that policy is very simple. Uh the policy first does regression to predict

### [36:20 - 36:20]

policy first does regression to predict

### [36:20 - 36:22]

policy first does regression to predict an action.

### [36:22 - 36:22]

an action.

### [36:22 - 36:23]

an action. And then what we do is we add a little

### [36:23 - 36:23]

And then what we do is we add a little

### [36:23 - 36:25]

And then what we do is we add a little bit of noise to our action.

### [36:25 - 36:25]

bit of noise to our action.

### [36:25 - 36:26]

bit of noise to our action. And then we do another step of

### [36:26 - 36:26]

And then we do another step of

### [36:26 - 36:28]

And then we do another step of regression to predict the action again.

### [36:28 - 36:28]

regression to predict the action again.

### [36:28 - 36:29]

regression to predict the action again. Right? So, we kind of tell the policy

### [36:29 - 36:29]

Right? So, we kind of tell the policy

### [36:29 - 36:32]

Right? So, we kind of tell the policy how to correct its own actions.

### [36:32 - 36:32]

how to correct its own actions.

### [36:32 - 36:33]

how to correct its own actions. So, if you want to do inference on this

### [36:33 - 36:33]

So, if you want to do inference on this

### [36:33 - 36:35]

So, if you want to do inference on this policy, what you do is you just first

### [36:35 - 36:35]

policy, what you do is you just first

### [36:35 - 36:37]

policy, what you do is you just first predict your original action, and then

### [36:37 - 36:37]

predict your original action, and then

### [36:37 - 36:38]

predict your original action, and then you can choose to add noise, you don't

### [36:38 - 36:38]

you can choose to add noise, you don't

### [36:38 - 36:39]

you can choose to add noise, you don't have to, but you just set feed that

### [36:39 - 36:39]

have to, but you just set feed that

### [36:39 - 36:41]

have to, but you just set feed that action back to the second stage policy,

### [36:41 - 36:41]

action back to the second stage policy,

### [36:41 - 36:43]

action back to the second stage policy, and use that to design a correction. And

### [36:43 - 36:43]

and use that to design a correction. And

### [36:43 - 36:45]

and use that to design a correction. And that's your final action.

### [36:45 - 36:45]

that's your final action.

### [36:45 - 36:47]

that's your final action. So, this policy is very um uses

### [36:47 - 36:47]

So, this policy is very um uses

### [36:47 - 36:48]

So, this policy is very um uses iterative computation in a very minimal

### [36:48 - 36:48]

iterative computation in a very minimal

### [36:48 - 36:50]

iterative computation in a very minimal way, so we called it MIP, the minimal

### [36:50 - 36:50]

way, so we called it MIP, the minimal

### [36:50 - 36:51]

way, so we called it MIP, the minimal iterative policy.

### [36:51 - 36:51]

iterative policy.

### [36:51 - 36:53]

iterative policy. And this is kind of as an ablation to

### [36:53 - 36:53]

And this is kind of as an ablation to

### [36:53 - 36:54]

And this is kind of as an ablation to investigate what flow is really giving

### [36:54 - 36:54]

investigate what flow is really giving

### [36:54 - 36:56]

investigate what flow is really giving us.

### [36:56 - 36:56]

us.

### [36:56 - 36:58]

us. So, these two things.

### [36:58 - 36:58]

So, these two things.

### [36:58 - 37:00]

So, these two things. So, what did what what how does MIP do?

### [37:00 - 37:00]

So, what did what what how does MIP do?

### [37:00 - 37:02]

So, what did what what how does MIP do? Well, it turns out that among the tasks

### [37:02 - 37:02]

Well, it turns out that among the tasks

### [37:02 - 37:04]

Well, it turns out that among the tasks where uh flow models do better than

### [37:04 - 37:04]

where uh flow models do better than

### [37:04 - 37:06]

where uh flow models do better than regression, MIP performs competitively

### [37:06 - 37:06]

regression, MIP performs competitively

### [37:06 - 37:08]

regression, MIP performs competitively with if not sometimes better than flow

### [37:08 - 37:08]

with if not sometimes better than flow

### [37:08 - 37:10]

with if not sometimes better than flow models across all these tasks.

### [37:10 - 37:10]

models across all these tasks.

### [37:10 - 37:13]

models across all these tasks. So, this suggests that this sort of

### [37:13 - 37:13]

So, this suggests that this sort of

### [37:13 - 37:14]

So, this suggests that this sort of component two and component three,

### [37:14 - 37:14]

component two and component three,

### [37:14 - 37:16]

component two and component three, stochasticity and supervised iterative

### [37:16 - 37:16]

stochasticity and supervised iterative

### [37:16 - 37:18]

stochasticity and supervised iterative computation, benefit you. However, if

### [37:18 - 37:18]

computation, benefit you. However, if

### [37:18 - 37:19]

computation, benefit you. However, if you only use component two or component

### [37:19 - 37:19]

you only use component two or component

### [37:19 - 37:21]

you only use component two or component three in isolation, not combined, they

### [37:21 - 37:21]

three in isolation, not combined, they

### [37:21 - 37:22]

three in isolation, not combined, they don't work. So, if you don't have

### [37:22 - 37:22]

don't work. So, if you don't have

### [37:22 - 37:25]

don't work. So, if you don't have stochasticity, intuitively, uh it's hard

### [37:25 - 37:25]

stochasticity, intuitively, uh it's hard

### [37:25 - 37:26]

stochasticity, intuitively, uh it's hard to like learn the self-corrections

### [37:26 - 37:26]

to like learn the self-corrections

### [37:26 - 37:27]

to like learn the self-corrections because you're not giving your your

### [37:27 - 37:27]

because you're not giving your your

### [37:27 - 37:29]

because you're not giving your your second action enough coverage, so that

### [37:29 - 37:29]

second action enough coverage, so that

### [37:29 - 37:31]

second action enough coverage, so that sort of breaks down. And if you only

### [37:31 - 37:31]

sort of breaks down. And if you only

### [37:31 - 37:33]

sort of breaks down. And if you only have component three, then you're not

### [37:33 - 37:33]

have component three, then you're not

### [37:33 - 37:34]

have component three, then you're not really benefiting anything, your neural

### [37:34 - 37:34]

really benefiting anything, your neural

### [37:34 - 37:35]

really benefiting anything, your neural network learns to ignore the noise if

### [37:35 - 37:35]

network learns to ignore the noise if

### [37:35 - 37:37]

network learns to ignore the noise if you have no iterative computation and

### [37:37 - 37:37]

you have no iterative computation and

### [37:37 - 37:38]

you have no iterative computation and just extra noise.

### [37:38 - 37:38]

just extra noise.

### [37:38 - 37:41]

just extra noise. So, you need to kind of combine the two.

### [37:41 - 37:41]

So, you need to kind of combine the two.

### [37:41 - 37:42]

So, you need to kind of combine the two. So, now you can we're trying to

### [37:42 - 37:42]

So, now you can we're trying to

### [37:42 - 37:44]

So, now you can we're trying to understand, well, what are the benefits?

### [37:44 - 37:44]

understand, well, what are the benefits?

### [37:44 - 37:45]

understand, well, what are the benefits? Where is this iterative computation

### [37:45 - 37:45]

Where is this iterative computation

### [37:45 - 37:46]

Where is this iterative computation helping us?

### [37:46 - 37:46]

helping us?

### [37:46 - 37:48]

helping us? So, let me give a sort of a mental

### [37:48 - 37:48]

So, let me give a sort of a mental

### [37:48 - 37:50]

So, let me give a sort of a mental picture for how you might think this is

### [37:50 - 37:50]

picture for how you might think this is

### [37:50 - 37:51]

picture for how you might think this is useful.

### [37:51 - 37:51]

useful.

### [37:51 - 37:55]

useful. So, um suppose that you're training, and

### [37:55 - 37:55]

So, um suppose that you're training, and

### [37:55 - 37:56]

So, um suppose that you're training, and you have demonstrations that are sparse,

### [37:56 - 37:56]

you have demonstrations that are sparse,

### [37:56 - 37:57]

you have demonstrations that are sparse, they're they're they're they're

### [37:57 - 37:57]

they're they're they're they're

### [37:57 - 37:59]

they're they're they're they're suspended in high-dimensional space.

### [37:59 - 37:59]

suspended in high-dimensional space.

### [37:59 - 38:01]

suspended in high-dimensional space. So, you could think that your policy

### [38:01 - 38:01]

So, you could think that your policy

### [38:01 - 38:02]

So, you could think that your policy learns multimodality. It says, "Oh,

### [38:02 - 38:02]

learns multimodality. It says, "Oh,

### [38:02 - 38:04]

learns multimodality. It says, "Oh, well, I have these two strategies, maybe

### [38:04 - 38:04]

well, I have these two strategies, maybe

### [38:04 - 38:05]

well, I have these two strategies, maybe sometime I'll go left, sometimes I'll go

### [38:05 - 38:05]

sometime I'll go left, sometimes I'll go

### [38:05 - 38:07]

sometime I'll go left, sometimes I'll go right." That's B2.

### [38:07 - 38:07]

right." That's B2.

### [38:07 - 38:08]

right." That's B2. But our experiment suggests that we

### [38:08 - 38:08]

But our experiment suggests that we

### [38:08 - 38:09]

But our experiment suggests that we don't we're not really learning

### [38:09 - 38:09]

don't we're not really learning

### [38:09 - 38:10]

don't we're not really learning multimodality, not at least at this

### [38:10 - 38:10]

multimodality, not at least at this

### [38:10 - 38:12]

multimodality, not at least at this scale.

### [38:12 - 38:12]

scale.

### [38:12 - 38:13]

scale. So, another thing that we could learn

### [38:13 - 38:13]

So, another thing that we could learn

### [38:13 - 38:15]

So, another thing that we could learn instead of multimodality is rapid

### [38:15 - 38:15]

instead of multimodality is rapid

### [38:15 - 38:17]

instead of multimodality is rapid switching. So, we could say, "Oh, well,

### [38:17 - 38:17]

switching. So, we could say, "Oh, well,

### [38:17 - 38:18]

switching. So, we could say, "Oh, well, if I'm on the left slightly, I always go

### [38:18 - 38:18]

if I'm on the left slightly, I always go

### [38:18 - 38:19]

if I'm on the left slightly, I always go left. If I'm on the right slightly, I'll

### [38:19 - 38:19]

left. If I'm on the right slightly, I'll

### [38:19 - 38:21]

left. If I'm on the right slightly, I'll always go right." So, I'll learn a

### [38:21 - 38:21]

always go right." So, I'll learn a

### [38:21 - 38:22]

always go right." So, I'll learn a policy that changes very rapidly, and

### [38:22 - 38:22]

policy that changes very rapidly, and

### [38:22 - 38:24]

policy that changes very rapidly, and that's called having a high Lipschitz

### [38:24 - 38:24]

that's called having a high Lipschitz

### [38:24 - 38:26]

that's called having a high Lipschitz constant.

### [38:26 - 38:26]

constant.

### [38:26 - 38:28]

constant. So, maybe the the supervised

### [38:28 - 38:28]

So, maybe the the supervised

### [38:28 - 38:30]

So, maybe the the supervised computation, the iterative computation

### [38:30 - 38:30]

computation, the iterative computation

### [38:30 - 38:32]

computation, the iterative computation helps represent this really fast change,

### [38:32 - 38:32]

helps represent this really fast change,

### [38:32 - 38:34]

helps represent this really fast change, this high Lipschitz constant, right? So,

### [38:34 - 38:34]

this high Lipschitz constant, right? So,

### [38:34 - 38:36]

this high Lipschitz constant, right? So, why would we believe this? Well, we know

### [38:36 - 38:36]

why would we believe this? Well, we know

### [38:36 - 38:38]

why would we believe this? Well, we know that deep neural networks are much

### [38:38 - 38:38]

that deep neural networks are much

### [38:38 - 38:39]

that deep neural networks are much better at representing high Lipschitz

### [38:39 - 38:39]

better at representing high Lipschitz

### [38:39 - 38:42]

better at representing high Lipschitz functions than shallow neural networks.

### [38:42 - 38:42]

functions than shallow neural networks.

### [38:42 - 38:43]

functions than shallow neural networks. And we can also think about our

### [38:43 - 38:43]

And we can also think about our

### [38:43 - 38:45]

And we can also think about our iterative steps of computation as kind

### [38:45 - 38:45]

iterative steps of computation as kind

### [38:45 - 38:47]

iterative steps of computation as kind of functioning like a deeper neural

### [38:47 - 38:47]

of functioning like a deeper neural

### [38:47 - 38:48]

of functioning like a deeper neural network, right? If you have more steps

### [38:48 - 38:48]

network, right? If you have more steps

### [38:48 - 38:49]

network, right? If you have more steps to go, it's kind of like you have more

### [38:49 - 38:49]

to go, it's kind of like you have more

### [38:49 - 38:51]

to go, it's kind of like you have more layers in your network, sort of, right?

### [38:51 - 38:51]

layers in your network, sort of, right?

### [38:51 - 38:53]

layers in your network, sort of, right? That was at least our first belief.

### [38:53 - 38:53]

That was at least our first belief.

### [38:53 - 38:55]

That was at least our first belief. But it turns out that's wrong.

### [38:55 - 38:55]

But it turns out that's wrong.

### [38:55 - 38:56]

But it turns out that's wrong. So, that you can actually show that if

### [38:56 - 38:56]

So, that you can actually show that if

### [38:56 - 38:59]

So, that you can actually show that if you're not learning multimodality, you

### [38:59 - 38:59]

you're not learning multimodality, you

### [38:59 - 39:01]

you're not learning multimodality, you can't represent more complex functions

### [39:01 - 39:01]

can't represent more complex functions

### [39:01 - 39:02]

can't represent more complex functions by using more multiple steps of

### [39:02 - 39:02]

by using more multiple steps of

### [39:02 - 39:04]

by using more multiple steps of computation, at least naively. Uh it

### [39:04 - 39:04]

computation, at least naively. Uh it

### [39:04 - 39:06]

computation, at least naively. Uh it just doesn't benefit you. Uh the reason

### [39:06 - 39:06]

just doesn't benefit you. Uh the reason

### [39:06 - 39:07]

just doesn't benefit you. Uh the reason being that in the absence of

### [39:07 - 39:07]

being that in the absence of

### [39:07 - 39:09]

being that in the absence of multimodality, kind of your flow always

### [39:09 - 39:09]

multimodality, kind of your flow always

### [39:09 - 39:10]

multimodality, kind of your flow always kind of converges back to this kind of

### [39:10 - 39:10]

kind of converges back to this kind of

### [39:10 - 39:12]

kind of converges back to this kind of like connected distribution, and you

### [39:12 - 39:12]

like connected distribution, and you

### [39:12 - 39:14]

like connected distribution, and you don't really have any ability to sort of

### [39:14 - 39:14]

don't really have any ability to sort of

### [39:14 - 39:15]

don't really have any ability to sort of shift that more rapidly than you would

### [39:15 - 39:15]

shift that more rapidly than you would

### [39:15 - 39:19]

shift that more rapidly than you would with just pure regression.

### [39:21 - 39:21]

So, what is happening? So, let me give a

### [39:21 - 39:23]

So, what is happening? So, let me give a tangent that's related to control, and

### [39:23 - 39:23]

tangent that's related to control, and

### [39:23 - 39:25]

tangent that's related to control, and use that to contextualize what's going

### [39:25 - 39:25]

use that to contextualize what's going

### [39:25 - 39:26]

use that to contextualize what's going on.

### [39:26 - 39:26]

on.

### [39:26 - 39:28]

on. Imagine that rather than getting expert

### [39:28 - 39:28]

Imagine that rather than getting expert

### [39:28 - 39:29]

Imagine that rather than getting expert data, we try to collect exploratory

### [39:29 - 39:29]

data, we try to collect exploratory

### [39:29 - 39:32]

data, we try to collect exploratory data. And this better data collection is

### [39:32 - 39:32]

data. And this better data collection is

### [39:32 - 39:33]

data. And this better data collection is is is sort of essential in sort of all

### [39:33 - 39:33]

is is sort of essential in sort of all

### [39:33 - 39:34]

is is sort of essential in sort of all of robotics, in particular in behavior

### [39:34 - 39:34]

of robotics, in particular in behavior

### [39:34 - 39:36]

of robotics, in particular in behavior cloning. So, let's consider a stylized

### [39:36 - 39:36]

cloning. So, let's consider a stylized

### [39:36 - 39:38]

cloning. So, let's consider a stylized example, it's based off

### [39:38 - 39:38]

example, it's based off

### [39:38 - 39:40]

example, it's based off on the DART algorithm from Kevin Laskey

### [39:40 - 39:40]

on the DART algorithm from Kevin Laskey

### [39:40 - 39:42]

on the DART algorithm from Kevin Laskey and others. So, what we're going to do

### [39:42 - 39:42]

and others. So, what we're going to do

### [39:42 - 39:43]

and others. So, what we're going to do is we're just going to collect data by

### [39:43 - 39:43]

is we're just going to collect data by

### [39:43 - 39:45]

is we're just going to collect data by adding noise to our actions, like some

### [39:45 - 39:45]

adding noise to our actions, like some

### [39:45 - 39:47]

adding noise to our actions, like some small amount of noise to our actions.

### [39:47 - 39:47]

small amount of noise to our actions.

### [39:47 - 39:48]

small amount of noise to our actions. Now, when we get that that that those

### [39:48 - 39:48]

Now, when we get that that that those

### [39:48 - 39:50]

Now, when we get that that that those states, we're going to take expert uh

### [39:50 - 39:50]

states, we're going to take expert uh

### [39:50 - 39:51]

states, we're going to take expert uh we're going to collect the expert

### [39:51 - 39:51]

we're going to collect the expert

### [39:51 - 39:52]

we're going to collect the expert actions at those states. So, these are

### [39:52 - 39:52]

actions at those states. So, these are

### [39:52 - 39:55]

actions at those states. So, these are noisy states that we get to or states

### [39:55 - 39:55]

noisy states that we get to or states

### [39:55 - 39:57]

noisy states that we get to or states that are achieved by noisy exploration,

### [39:57 - 39:57]

that are achieved by noisy exploration,

### [39:57 - 39:58]

that are achieved by noisy exploration, they give us expert actions that we

### [39:58 - 39:58]

they give us expert actions that we

### [39:58 - 39:59]

they give us expert actions that we should take.

### [39:59 - 39:59]

should take.

### [39:59 - 40:00]

should take. And now, what we're going to do is train

### [40:00 - 40:00]

And now, what we're going to do is train

### [40:00 - 40:03]

And now, what we're going to do is train a policy that imitates the clean expert

### [40:03 - 40:03]

a policy that imitates the clean expert

### [40:03 - 40:05]

a policy that imitates the clean expert actions, but does so under the

### [40:05 - 40:05]

actions, but does so under the

### [40:05 - 40:07]

actions, but does so under the distribution of noisy states, right? So,

### [40:07 - 40:07]

distribution of noisy states, right? So,

### [40:07 - 40:08]

distribution of noisy states, right? So, the noisy states just give us

### [40:08 - 40:08]

the noisy states just give us

### [40:08 - 40:10]

the noisy states just give us exploration, the imitation is to clean

### [40:10 - 40:10]

exploration, the imitation is to clean

### [40:10 - 40:11]

exploration, the imitation is to clean actions.

### [40:11 - 40:11]

actions.

### [40:11 - 40:12]

actions. Okay. So, it looks something like this,

### [40:12 - 40:12]

Okay. So, it looks something like this,

### [40:12 - 40:14]

Okay. So, it looks something like this, right? We're trying to imitate uh the

### [40:14 - 40:14]

right? We're trying to imitate uh the

### [40:14 - 40:17]

right? We're trying to imitate uh the red's trying to imitate the light blue.

### [40:19 - 40:19]

So, what you can show is that if you do

### [40:19 - 40:20]

So, what you can show is that if you do this scheme,

### [40:20 - 40:20]

this scheme,

### [40:20 - 40:22]

this scheme, even if the system is open-loop

### [40:22 - 40:22]

even if the system is open-loop

### [40:22 - 40:23]

even if the system is open-loop unstable,

### [40:23 - 40:23]

unstable,

### [40:23 - 40:24]

unstable, you will always be able to imitate

### [40:24 - 40:24]

you will always be able to imitate

### [40:24 - 40:26]

you will always be able to imitate without compounding error.

### [40:26 - 40:26]

without compounding error.

### [40:26 - 40:28]

without compounding error. So, just this little bit of perturbation

### [40:28 - 40:28]

So, just this little bit of perturbation

### [40:28 - 40:29]

So, just this little bit of perturbation to the to the actions is able to

### [40:29 - 40:29]

to the to the actions is able to

### [40:29 - 40:31]

to the to the actions is able to overcome the lower bound and actually

### [40:31 - 40:31]

overcome the lower bound and actually

### [40:31 - 40:32]

overcome the lower bound and actually always give you imitation learning

### [40:32 - 40:32]

always give you imitation learning

### [40:32 - 40:34]

always give you imitation learning guarantees.

### [40:34 - 40:34]

guarantees.

### [40:34 - 40:36]

guarantees. And in fact, kind of what's sort of

### [40:36 - 40:36]

And in fact, kind of what's sort of

### [40:36 - 40:38]

And in fact, kind of what's sort of miraculous about this is that you kind

### [40:38 - 40:38]

miraculous about this is that you kind

### [40:38 - 40:40]

miraculous about this is that you kind of magically find the states or the the

### [40:40 - 40:40]

of magically find the states or the the

### [40:40 - 40:42]

of magically find the states or the the directions in state space that are most

### [40:42 - 40:42]

directions in state space that are most

### [40:42 - 40:44]

directions in state space that are most susceptible to compounding error. So,

### [40:44 - 40:44]

susceptible to compounding error. So,

### [40:44 - 40:45]

susceptible to compounding error. So, because your expert is adding noise to

### [40:45 - 40:45]

because your expert is adding noise to

### [40:45 - 40:47]

because your expert is adding noise to dynamical system, even if the expert

### [40:47 - 40:47]

dynamical system, even if the expert

### [40:47 - 40:48]

dynamical system, even if the expert keeps everything stable, it's sort of

### [40:48 - 40:48]

keeps everything stable, it's sort of

### [40:48 - 40:50]

keeps everything stable, it's sort of exploring every direction that could go

### [40:50 - 40:50]

exploring every direction that could go

### [40:50 - 40:52]

exploring every direction that could go unstable under learning, which is kind

### [40:52 - 40:52]

unstable under learning, which is kind

### [40:52 - 40:53]

unstable under learning, which is kind of magical. Okay.

### [40:53 - 40:53]

of magical. Okay.

### [40:53 - 40:54]

of magical. Okay. So, we're not going to do this. In fact,

### [40:54 - 40:54]

So, we're not going to do this. In fact,

### [40:54 - 40:56]

So, we're not going to do this. In fact, just adding noise to your actions might

### [40:56 - 40:56]

just adding noise to your actions might

### [40:56 - 40:57]

just adding noise to your actions might be a very bad idea depending on the

### [40:57 - 40:57]

be a very bad idea depending on the

### [40:57 - 40:59]

be a very bad idea depending on the hardware that you have.

### [40:59 - 40:59]

hardware that you have.

### [40:59 - 41:00]

hardware that you have. But, we're going to argue that maybe

### [41:00 - 41:00]

But, we're going to argue that maybe

### [41:00 - 41:01]

But, we're going to argue that maybe flow models are doing a little bit of

### [41:01 - 41:01]

flow models are doing a little bit of

### [41:01 - 41:03]

flow models are doing a little bit of this or doing something somewhat

### [41:03 - 41:03]

this or doing something somewhat

### [41:03 - 41:05]

this or doing something somewhat equivalent to this.

### [41:05 - 41:05]

equivalent to this.

### [41:05 - 41:06]

equivalent to this. Okay.

### [41:06 - 41:06]

Okay.

### [41:06 - 41:08]

Okay. So, let me explain how we did this. So,

### [41:08 - 41:08]

So, let me explain how we did this. So,

### [41:08 - 41:09]

So, let me explain how we did this. So, what we're going to what we're going to

### [41:09 - 41:09]

what we're going to what we're going to

### [41:09 - 41:11]

what we're going to what we're going to do is we're going to take a flow model

### [41:11 - 41:11]

do is we're going to take a flow model

### [41:11 - 41:12]

do is we're going to take a flow model and we're going to look at what it does

### [41:12 - 41:12]

and we're going to look at what it does

### [41:12 - 41:15]

and we're going to look at what it does on states that we reach via this noisy

### [41:15 - 41:15]

on states that we reach via this noisy

### [41:15 - 41:16]

on states that we reach via this noisy data collection.

### [41:16 - 41:16]

data collection.

### [41:16 - 41:17]

data collection. So, imagine here you have your actions

### [41:17 - 41:17]

So, imagine here you have your actions

### [41:17 - 41:21]

So, imagine here you have your actions and states, you get some expert action,

### [41:21 - 41:21]

and states, you get some expert action,

### [41:21 - 41:22]

and states, you get some expert action, and you make some prediction, that's

### [41:22 - 41:22]

and you make some prediction, that's

### [41:22 - 41:23]

and you make some prediction, that's your flow prediction.

### [41:23 - 41:23]

your flow prediction.

### [41:23 - 41:25]

your flow prediction. So, now, what we're going to do is we're

### [41:25 - 41:25]

So, now, what we're going to do is we're

### [41:25 - 41:27]

So, now, what we're going to do is we're going to imagine the other actions that

### [41:27 - 41:27]

going to imagine the other actions that

### [41:27 - 41:29]

going to imagine the other actions that we would have achieved. And these other

### [41:29 - 41:29]

we would have achieved. And these other

### [41:29 - 41:30]

we would have achieved. And these other actions that we would have achieved are

### [41:30 - 41:30]

actions that we would have achieved are

### [41:30 - 41:31]

actions that we would have achieved are ones that we would get to if we just

### [41:31 - 41:31]

ones that we would get to if we just

### [41:31 - 41:33]

ones that we would get to if we just perturb previous actions. So, we're kind

### [41:33 - 41:33]

perturb previous actions. So, we're kind

### [41:33 - 41:35]

perturb previous actions. So, we're kind of exploring through the system and then

### [41:35 - 41:35]

of exploring through the system and then

### [41:35 - 41:36]

of exploring through the system and then we're looking getting to slightly

### [41:36 - 41:36]

we're looking getting to slightly

### [41:36 - 41:37]

we're looking getting to slightly different states and we're looking at

### [41:37 - 41:37]

different states and we're looking at

### [41:37 - 41:39]

different states and we're looking at the actions at those different states.

### [41:39 - 41:39]

the actions at those different states.

### [41:39 - 41:40]

the actions at those different states. And so, we'll just take the stay on the

### [41:40 - 41:40]

And so, we'll just take the stay on the

### [41:40 - 41:42]

And so, we'll just take the stay on the vector space that's spanned by all these

### [41:42 - 41:42]

vector space that's spanned by all these

### [41:42 - 41:43]

vector space that's spanned by all these actions and we'll call this the

### [41:43 - 41:43]

actions and we'll call this the

### [41:43 - 41:45]

actions and we'll call this the localized action manifold.

### [41:45 - 41:45]

localized action manifold.

### [41:45 - 41:46]

localized action manifold. Okay.

### [41:46 - 41:46]

Okay.

### [41:46 - 41:47]

Okay. So, now, for every action that we

### [41:47 - 41:47]

So, now, for every action that we

### [41:47 - 41:49]

So, now, for every action that we predict, you can think about two sources

### [41:49 - 41:49]

predict, you can think about two sources

### [41:49 - 41:50]

predict, you can think about two sources of error.

### [41:50 - 41:50]

of error.

### [41:50 - 41:52]

of error. You can think of the source of error

### [41:52 - 41:52]

You can think of the source of error

### [41:52 - 41:54]

You can think of the source of error that that says you were on the right

### [41:54 - 41:54]

that that says you were on the right

### [41:54 - 41:56]

that that says you were on the right manifold, but you maybe made a mistake,

### [41:56 - 41:56]

manifold, but you maybe made a mistake,

### [41:56 - 41:57]

manifold, but you maybe made a mistake, or the source of error which is your

### [41:57 - 41:57]

or the source of error which is your

### [41:57 - 41:58]

or the source of error which is your orthogonal to the manifold, you're off

### [41:58 - 41:58]

orthogonal to the manifold, you're off

### [41:58 - 42:00]

orthogonal to the manifold, you're off the manifold.

### [42:00 - 42:00]

the manifold.

### [42:00 - 42:02]

the manifold. And we plot these two.

### [42:02 - 42:02]

And we plot these two.

### [42:02 - 42:04]

And we plot these two. And what we see is that flow models,

### [42:04 - 42:04]

And what we see is that flow models,

### [42:04 - 42:05]

And what we see is that flow models, they don't have better validation losses

### [42:05 - 42:05]

they don't have better validation losses

### [42:05 - 42:07]

they don't have better validation losses naively. So, they're making the same

### [42:07 - 42:07]

naively. So, they're making the same

### [42:07 - 42:08]

naively. So, they're making the same amount of error,

### [42:08 - 42:08]

amount of error,

### [42:08 - 42:10]

amount of error, but the location of that error seems to

### [42:10 - 42:10]

but the location of that error seems to

### [42:10 - 42:12]

but the location of that error seems to be uh less off the manifold and more on

### [42:12 - 42:12]

be uh less off the manifold and more on

### [42:12 - 42:13]

be uh less off the manifold and more on the manifold. So, I'll give you like a

### [42:13 - 42:13]

the manifold. So, I'll give you like a

### [42:13 - 42:15]

the manifold. So, I'll give you like a visual description. Imagine I need to do

### [42:15 - 42:15]

visual description. Imagine I need to do

### [42:15 - 42:16]

visual description. Imagine I need to do an insertion task, right? On the

### [42:16 - 42:16]

an insertion task, right? On the

### [42:16 - 42:18]

an insertion task, right? On the manifold is this way. If I go faster or

### [42:18 - 42:18]

manifold is this way. If I go faster or

### [42:18 - 42:20]

manifold is this way. If I go faster or slower, I still insert the the tool.

### [42:20 - 42:20]

slower, I still insert the the tool.

### [42:20 - 42:22]

slower, I still insert the the tool. But, if I go off the manifold, I miss.

### [42:22 - 42:22]

But, if I go off the manifold, I miss.

### [42:22 - 42:23]

But, if I go off the manifold, I miss. And it seems that flow models seem to

### [42:23 - 42:23]

And it seems that flow models seem to

### [42:23 - 42:25]

And it seems that flow models seem to have this inductive bias that seems to

### [42:25 - 42:25]

have this inductive bias that seems to

### [42:25 - 42:27]

have this inductive bias that seems to be very useful in robotics. And so,

### [42:27 - 42:27]

be very useful in robotics. And so,

### [42:27 - 42:28]

be very useful in robotics. And so, they're they're kind of like trained

### [42:28 - 42:28]

they're they're kind of like trained

### [42:28 - 42:30]

they're they're kind of like trained towards learning this like local action

### [42:30 - 42:30]

towards learning this like local action

### [42:30 - 42:33]

towards learning this like local action manifold that we get from noising. And

### [42:33 - 42:33]

manifold that we get from noising. And

### [42:33 - 42:34]

manifold that we get from noising. And the noising would be the thing that if

### [42:34 - 42:34]

the noising would be the thing that if

### [42:34 - 42:35]

the noising would be the thing that if we imitated perfectly under that

### [42:35 - 42:35]

we imitated perfectly under that

### [42:35 - 42:36]

we imitated perfectly under that distribution, we would actually have no

### [42:36 - 42:36]

distribution, we would actually have no

### [42:36 - 42:38]

distribution, we would actually have no compounding error. So, it's not exactly

### [42:38 - 42:38]

compounding error. So, it's not exactly

### [42:38 - 42:39]

compounding error. So, it's not exactly like we're doing getting data for free,

### [42:39 - 42:39]

like we're doing getting data for free,

### [42:39 - 42:40]

like we're doing getting data for free, we're just using an inductive bias

### [42:40 - 42:40]

we're just using an inductive bias

### [42:40 - 42:43]

we're just using an inductive bias that's very beneficial.

### [42:43 - 42:43]

that's very beneficial.

### [42:43 - 42:43]

that's very beneficial. Right.

### [42:43 - 42:43]

Right.

### [42:43 - 42:45]

Right. So, the way that we kind of think about

### [42:45 - 42:45]

So, the way that we kind of think about

### [42:45 - 42:46]

So, the way that we kind of think about this is that at every step of the

### [42:46 - 42:46]

this is that at every step of the

### [42:46 - 42:48]

this is that at every step of the computation, the flow model is trying to

### [42:48 - 42:48]

computation, the flow model is trying to

### [42:48 - 42:50]

computation, the flow model is trying to come up with an action, and the

### [42:50 - 42:50]

come up with an action, and the

### [42:50 - 42:51]

come up with an action, and the correction step is sort of smoothing

### [42:51 - 42:51]

correction step is sort of smoothing

### [42:51 - 42:53]

correction step is sort of smoothing both in because it's conditioned both on

### [42:53 - 42:53]

both in because it's conditioned both on

### [42:53 - 42:55]

both in because it's conditioned both on observation and its own noisy action,

### [42:55 - 42:55]

observation and its own noisy action,

### [42:55 - 42:56]

observation and its own noisy action, it's smoothing both in observation and

### [42:56 - 42:56]

it's smoothing both in observation and

### [42:56 - 42:58]

it's smoothing both in observation and action space. And by smoothing in both,

### [42:58 - 42:58]

action space. And by smoothing in both,

### [42:58 - 43:00]

action space. And by smoothing in both, we still don't really fully understand

### [43:00 - 43:00]

we still don't really fully understand

### [43:00 - 43:01]

we still don't really fully understand how this works, but we just have

### [43:01 - 43:01]

how this works, but we just have

### [43:01 - 43:02]

how this works, but we just have evidence that this is happening. It's

### [43:02 - 43:02]

evidence that this is happening. It's

### [43:02 - 43:03]

evidence that this is happening. It's actually quite hard to prove that this

### [43:03 - 43:03]

actually quite hard to prove that this

### [43:03 - 43:06]

actually quite hard to prove that this works. Uh but, what we it seems to be

### [43:06 - 43:06]

works. Uh but, what we it seems to be

### [43:06 - 43:07]

works. Uh but, what we it seems to be going on is that you're getting this

### [43:07 - 43:07]

going on is that you're getting this

### [43:07 - 43:09]

going on is that you're getting this inductive bias towards this off this on

### [43:09 - 43:09]

inductive bias towards this off this on

### [43:09 - 43:11]

inductive bias towards this off this on manifold error, and this is predictive

### [43:11 - 43:11]

manifold error, and this is predictive

### [43:11 - 43:14]

manifold error, and this is predictive of increased performance.

### [43:15 - 43:15]

So, essentially, these two ingredients,

### [43:15 - 43:17]

So, essentially, these two ingredients, stochasticity and iterative computation,

### [43:17 - 43:17]

stochasticity and iterative computation,

### [43:17 - 43:19]

stochasticity and iterative computation, they're inducing this inductive bias,

### [43:19 - 43:19]

they're inducing this inductive bias,

### [43:19 - 43:20]

they're inducing this inductive bias, they're inducing they're sort of putting

### [43:20 - 43:20]

they're inducing they're sort of putting

### [43:20 - 43:22]

they're inducing they're sort of putting your error in in the directions where

### [43:22 - 43:22]

your error in in the directions where

### [43:22 - 43:23]

your error in in the directions where sort of it's it's unavoidable to make

### [43:23 - 43:23]

sort of it's it's unavoidable to make

### [43:23 - 43:24]

sort of it's it's unavoidable to make error, but if you make error in those

### [43:24 - 43:24]

error, but if you make error in those

### [43:24 - 43:26]

error, but if you make error in those directions, you're not suffering too

### [43:26 - 43:26]

directions, you're not suffering too

### [43:26 - 43:28]

directions, you're not suffering too much.

### [43:28 - 43:28]

much.

### [43:28 - 43:29]

much. And so, I kind of our takeaway is that a

### [43:29 - 43:29]

And so, I kind of our takeaway is that a

### [43:29 - 43:31]

And so, I kind of our takeaway is that a big part of the benefit of generative

### [43:31 - 43:31]

big part of the benefit of generative

### [43:31 - 43:32]

big part of the benefit of generative control policies is actually their

### [43:32 - 43:32]

control policies is actually their

### [43:32 - 43:34]

control policies is actually their benefits for the control, not just their

### [43:34 - 43:34]

benefits for the control, not just their

### [43:34 - 43:36]

benefits for the control, not just their benefits for distribution learning from

### [43:36 - 43:36]

benefits for distribution learning from

### [43:36 - 43:38]

benefits for distribution learning from from modality matching.

### [43:38 - 43:38]

from modality matching.

### [43:38 - 43:40]

from modality matching. Um for those of you that are interested

### [43:40 - 43:40]

Um for those of you that are interested

### [43:40 - 43:42]

Um for those of you that are interested in using MIP, uh we're at CMU, so I

### [43:42 - 43:42]

in using MIP, uh we're at CMU, so I

### [43:42 - 43:44]

in using MIP, uh we're at CMU, so I would just say email Chui if you if

### [43:44 - 43:44]

would just say email Chui if you if

### [43:44 - 43:46]

would just say email Chui if you if you're curious about it. Uh but, the

### [43:46 - 43:46]

you're curious about it. Uh but, the

### [43:46 - 43:48]

you're curious about it. Uh but, the kind of TLDR is is it does work with

### [43:48 - 43:48]

kind of TLDR is is it does work with

### [43:48 - 43:50]

kind of TLDR is is it does work with VLAs in certain cases.

### [43:50 - 43:50]

VLAs in certain cases.

### [43:50 - 43:52]

VLAs in certain cases. Uh it actually does preserve task

### [43:52 - 43:52]

Uh it actually does preserve task

### [43:52 - 43:54]

Uh it actually does preserve task diversity. So, here's a fun thing about

### [43:54 - 43:54]

diversity. So, here's a fun thing about

### [43:54 - 43:56]

diversity. So, here's a fun thing about reactive control policies, even

### [43:56 - 43:56]

reactive control policies, even

### [43:56 - 43:58]

reactive control policies, even regression policies can be multimodal at

### [43:58 - 43:58]

regression policies can be multimodal at

### [43:58 - 43:59]

regression policies can be multimodal at the level of trajectories.

### [43:59 - 43:59]

the level of trajectories.

### [43:59 - 44:00]

the level of trajectories. Sort of the mental model you should have

### [44:00 - 44:00]

Sort of the mental model you should have

### [44:00 - 44:01]

Sort of the mental model you should have is that yes, you might have some

### [44:01 - 44:01]

is that yes, you might have some

### [44:01 - 44:03]

is that yes, you might have some unimodal distribution, but as you keep

### [44:03 - 44:03]

unimodal distribution, but as you keep

### [44:03 - 44:05]

unimodal distribution, but as you keep running and re- re- running your policy

### [44:05 - 44:05]

running and re- re- running your policy

### [44:05 - 44:06]

running and re- re- running your policy from those modes, you can still get

### [44:06 - 44:06]

from those modes, you can still get

### [44:06 - 44:08]

from those modes, you can still get branching as you run it keep running it

### [44:08 - 44:08]

branching as you run it keep running it

### [44:08 - 44:09]

branching as you run it keep running it over and over.

### [44:09 - 44:09]

over and over.

### [44:09 - 44:10]

over and over. Um

### [44:10 - 44:10]

Um

### [44:10 - 44:12]

Um Right. So, that still preserves task

### [44:12 - 44:12]

Right. So, that still preserves task

### [44:12 - 44:13]

Right. So, that still preserves task diversity.

### [44:13 - 44:13]

diversity.

### [44:13 - 44:15]

diversity. Um however, I would say don't use MIP

### [44:15 - 44:15]

Um however, I would say don't use MIP

### [44:15 - 44:17]

Um however, I would say don't use MIP unless you need need to. So, it's really

### [44:17 - 44:17]

unless you need need to. So, it's really

### [44:17 - 44:18]

unless you need need to. So, it's really good for ablations, and if you need fast

### [44:18 - 44:18]

good for ablations, and if you need fast

### [44:18 - 44:20]

good for ablations, and if you need fast inference, we find that it works better

### [44:20 - 44:20]

inference, we find that it works better

### [44:20 - 44:22]

inference, we find that it works better than consistency-based models.

### [44:22 - 44:22]

than consistency-based models.

### [44:22 - 44:23]

than consistency-based models. Uh however, if you want to do things

### [44:23 - 44:23]

Uh however, if you want to do things

### [44:23 - 44:25]

Uh however, if you want to do things that are pre-training scale, for

### [44:25 - 44:25]

that are pre-training scale, for

### [44:25 - 44:26]

that are pre-training scale, for example, or if you want to do video

### [44:26 - 44:26]

example, or if you want to do video

### [44:26 - 44:28]

example, or if you want to do video prediction, long horizon prediction, key

### [44:28 - 44:28]

prediction, long horizon prediction, key

### [44:28 - 44:29]

prediction, long horizon prediction, key frame pose prediction, there is

### [44:29 - 44:29]

frame pose prediction, there is

### [44:29 - 44:32]

frame pose prediction, there is multimodality and do not use MIP. Uh

### [44:32 - 44:32]

multimodality and do not use MIP. Uh

### [44:32 - 44:34]

multimodality and do not use MIP. Uh also, for reinforcement learning, uh

### [44:34 - 44:34]

also, for reinforcement learning, uh

### [44:34 - 44:35]

also, for reinforcement learning, uh flow-based models just work way way

### [44:35 - 44:35]

flow-based models just work way way

### [44:35 - 44:37]

flow-based models just work way way better. That's a whole different reason.

### [44:37 - 44:37]

better. That's a whole different reason.

### [44:37 - 44:39]

better. That's a whole different reason. Um and I can talk to you guys offline

### [44:39 - 44:39]

Um and I can talk to you guys offline

### [44:39 - 44:43]

Um and I can talk to you guys offline about why that's the case.

### [44:45 - 44:45]

Um okay, one other cool point before we

### [44:45 - 44:47]

Um okay, one other cool point before we wrap up is that uh there's one kind of

### [44:47 - 44:47]

wrap up is that uh there's one kind of

### [44:47 - 44:49]

wrap up is that uh there's one kind of maybe interesting property about flow

### [44:49 - 44:49]

maybe interesting property about flow

### [44:49 - 44:50]

maybe interesting property about flow models, which is what they do about

### [44:50 - 44:50]

models, which is what they do about

### [44:50 - 44:52]

models, which is what they do about uncertainty. So, imagine that I have a

### [44:52 - 44:52]

uncertainty. So, imagine that I have a

### [44:52 - 44:53]

uncertainty. So, imagine that I have a function that's really really hard to

### [44:53 - 44:53]

function that's really really hard to

### [44:53 - 44:56]

function that's really really hard to fit, like y = sin(1/x).

### [44:56 - 44:56]

fit, like y = sin(1/x).

### [44:56 - 44:57]

fit, like y = sin(1/x). So, if I try to fit it with a regression

### [44:57 - 44:57]

So, if I try to fit it with a regression

### [44:57 - 44:58]

So, if I try to fit it with a regression model, I'm going to oversmooth in the

### [44:58 - 44:58]

model, I'm going to oversmooth in the

### [44:58 - 45:00]

model, I'm going to oversmooth in the middle cuz I can't fit it. If I try to

### [45:00 - 45:00]

middle cuz I can't fit it. If I try to

### [45:00 - 45:02]

middle cuz I can't fit it. If I try to fit it with a flow model and I only use

### [45:02 - 45:02]

fit it with a flow model and I only use

### [45:02 - 45:04]

fit it with a flow model and I only use one noise vector, uh I'm also going to

### [45:04 - 45:04]

one noise vector, uh I'm also going to

### [45:04 - 45:06]

one noise vector, uh I'm also going to oversmooth in maybe a slightly different

### [45:06 - 45:06]

oversmooth in maybe a slightly different

### [45:06 - 45:06]

oversmooth in maybe a slightly different way.

### [45:06 - 45:06]

way.

### [45:06 - 45:08]

way. But, now, if I aggregate and average

### [45:08 - 45:08]

But, now, if I aggregate and average

### [45:08 - 45:10]

But, now, if I aggregate and average over all my noise samples, I'm going to

### [45:10 - 45:10]

over all my noise samples, I'm going to

### [45:10 - 45:11]

over all my noise samples, I'm going to take this part of the function that's

### [45:11 - 45:11]

take this part of the function that's

### [45:11 - 45:13]

take this part of the function that's super hard to fit, and I'm actually

### [45:13 - 45:13]

super hard to fit, and I'm actually

### [45:13 - 45:15]

super hard to fit, and I'm actually instead going to learn some noisy thing.

### [45:15 - 45:15]

instead going to learn some noisy thing.

### [45:15 - 45:16]

instead going to learn some noisy thing. I'm going to learn some distribution.

### [45:16 - 45:16]

I'm going to learn some distribution.

### [45:16 - 45:18]

I'm going to learn some distribution. So, one way to interpret what's going on

### [45:18 - 45:18]

So, one way to interpret what's going on

### [45:18 - 45:19]

So, one way to interpret what's going on here is that you have high local

### [45:19 - 45:19]

here is that you have high local

### [45:19 - 45:21]

here is that you have high local epistemic uncertainty. You don't really

### [45:21 - 45:21]

epistemic uncertainty. You don't really

### [45:21 - 45:22]

epistemic uncertainty. You don't really know what's going on here, it's very

### [45:22 - 45:22]

know what's going on here, it's very

### [45:22 - 45:24]

know what's going on here, it's very hard to fit it.

### [45:24 - 45:24]

hard to fit it.

### [45:24 - 45:26]

hard to fit it. And that a flow model can kind of

### [45:26 - 45:26]

And that a flow model can kind of

### [45:26 - 45:27]

And that a flow model can kind of convert this into aleatoric uncertainty

### [45:27 - 45:27]

convert this into aleatoric uncertainty

### [45:27 - 45:29]

convert this into aleatoric uncertainty into variance over its prediction. And

### [45:29 - 45:29]

into variance over its prediction. And

### [45:29 - 45:30]

into variance over its prediction. And so, I've been working with a couple

### [45:30 - 45:30]

so, I've been working with a couple

### [45:30 - 45:32]

so, I've been working with a couple students at MIT on kind of understanding

### [45:32 - 45:32]

students at MIT on kind of understanding

### [45:32 - 45:35]

students at MIT on kind of understanding how generalizable this phenomena is.

### [45:35 - 45:35]

how generalizable this phenomena is.

### [45:35 - 45:37]

how generalizable this phenomena is. So, maybe let's conclude. Uh sort of in

### [45:37 - 45:37]

So, maybe let's conclude. Uh sort of in

### [45:37 - 45:38]

So, maybe let's conclude. Uh sort of in this talk, we tried to take a

### [45:38 - 45:38]

this talk, we tried to take a

### [45:38 - 45:40]

this talk, we tried to take a control-theoretic perspective showing

### [45:40 - 45:40]

control-theoretic perspective showing

### [45:40 - 45:41]

control-theoretic perspective showing that uh continuous control can be

### [45:41 - 45:41]

that uh continuous control can be

### [45:41 - 45:43]

that uh continuous control can be fundamentally more challenging than

### [45:43 - 45:43]

fundamentally more challenging than

### [45:43 - 45:44]

fundamentally more challenging than learning in the in the uh discrete

### [45:44 - 45:44]

learning in the in the uh discrete

### [45:44 - 45:45]

learning in the in the uh discrete world.

### [45:45 - 45:45]

world.

### [45:45 - 45:47]

world. Um the we tried to argue that the

### [45:47 - 45:47]

Um the we tried to argue that the

### [45:47 - 45:49]

Um the we tried to argue that the inflection point witnessed in robotics

### [45:49 - 45:49]

inflection point witnessed in robotics

### [45:49 - 45:50]

inflection point witnessed in robotics arose because in it the interventions

### [45:50 - 45:50]

arose because in it the interventions

### [45:50 - 45:52]

arose because in it the interventions that we developed inadvertently

### [45:52 - 45:52]

that we developed inadvertently

### [45:52 - 45:53]

that we developed inadvertently addressed these control-theoretic

### [45:53 - 45:53]

addressed these control-theoretic

### [45:53 - 45:54]

addressed these control-theoretic challenges that we encountered. For

### [45:54 - 45:54]

challenges that we encountered. For

### [45:54 - 45:56]

challenges that we encountered. For example, action chunking allowed us to

### [45:56 - 45:56]

example, action chunking allowed us to

### [45:56 - 45:58]

example, action chunking allowed us to learn stably in in in open-loop stable

### [45:58 - 45:58]

learn stably in in in open-loop stable

### [45:58 - 46:00]

learn stably in in in open-loop stable systems, and generative control sort of

### [46:00 - 46:00]

systems, and generative control sort of

### [46:00 - 46:01]

systems, and generative control sort of behaves in some ways like what we might

### [46:01 - 46:01]

behaves in some ways like what we might

### [46:01 - 46:03]

behaves in some ways like what we might get from better data augmentation

### [46:03 - 46:03]

get from better data augmentation

### [46:03 - 46:05]

get from better data augmentation without doing it explicitly.

### [46:05 - 46:05]

without doing it explicitly.

### [46:05 - 46:07]

without doing it explicitly. So, kind of this is sort of the evidence

### [46:07 - 46:07]

So, kind of this is sort of the evidence

### [46:07 - 46:09]

So, kind of this is sort of the evidence of this algorithmic Moravec's paradox

### [46:09 - 46:09]

of this algorithmic Moravec's paradox

### [46:09 - 46:11]

of this algorithmic Moravec's paradox view that robot learning is

### [46:11 - 46:11]

view that robot learning is

### [46:11 - 46:12]

view that robot learning is fundamentally harder unless you do a

### [46:12 - 46:12]

fundamentally harder unless you do a

### [46:12 - 46:13]

fundamentally harder unless you do a couple of things that might be somewhat

### [46:13 - 46:13]

couple of things that might be somewhat

### [46:13 - 46:16]

couple of things that might be somewhat non-obvious.

### [46:16 - 46:16]

non-obvious.

### [46:16 - 46:18]

non-obvious. So, I want to maybe end with what I what

### [46:18 - 46:18]

So, I want to maybe end with what I what

### [46:18 - 46:19]

So, I want to maybe end with what I what what remains hard about robotics. And

### [46:19 - 46:19]

what remains hard about robotics. And

### [46:19 - 46:21]

what remains hard about robotics. And there there two maybe different views,

### [46:21 - 46:21]

there there two maybe different views,

### [46:21 - 46:22]

there there two maybe different views, right? So, one is maybe nothing once we

### [46:22 - 46:22]

right? So, one is maybe nothing once we

### [46:22 - 46:24]

right? So, one is maybe nothing once we get enough data.

### [46:24 - 46:24]

get enough data.

### [46:24 - 46:26]

get enough data. Um this is kind of like the antithesis

### [46:26 - 46:26]

Um this is kind of like the antithesis

### [46:26 - 46:28]

Um this is kind of like the antithesis of Moravec's paradox. And sort of one

### [46:28 - 46:28]

of Moravec's paradox. And sort of one

### [46:28 - 46:29]

of Moravec's paradox. And sort of one thing that I think about, maybe it's

### [46:29 - 46:29]

thing that I think about, maybe it's

### [46:29 - 46:31]

thing that I think about, maybe it's useful for students as well, is that

### [46:31 - 46:31]

useful for students as well, is that

### [46:31 - 46:32]

useful for students as well, is that there's this unfortunate tension between

### [46:32 - 46:32]

there's this unfortunate tension between

### [46:32 - 46:35]

there's this unfortunate tension between like how useful a task is and how hard

### [46:35 - 46:35]

like how useful a task is and how hard

### [46:35 - 46:36]

like how useful a task is and how hard it is to learn. So, tasks that are very

### [46:36 - 46:36]

it is to learn. So, tasks that are very

### [46:36 - 46:38]

it is to learn. So, tasks that are very useful also show up a lot in our economy

### [46:38 - 46:38]

useful also show up a lot in our economy

### [46:38 - 46:39]

useful also show up a lot in our economy or we're willing to spend money

### [46:39 - 46:39]

or we're willing to spend money

### [46:39 - 46:41]

or we're willing to spend money collecting data. So, even if there's a

### [46:41 - 46:41]

collecting data. So, even if there's a

### [46:41 - 46:43]

collecting data. So, even if there's a more elegant solution, there's always

### [46:43 - 46:43]

more elegant solution, there's always

### [46:43 - 46:44]

more elegant solution, there's always someone who's willing to pay you to data

### [46:44 - 46:44]

someone who's willing to pay you to data

### [46:44 - 46:46]

someone who's willing to pay you to data collect. And unfortunately, this results

### [46:46 - 46:46]

collect. And unfortunately, this results

### [46:46 - 46:47]

collect. And unfortunately, this results in this kind of inverse correlation

### [46:47 - 46:47]

in this kind of inverse correlation

### [46:47 - 46:49]

in this kind of inverse correlation where a lot of the tasks that we really

### [46:49 - 46:49]

where a lot of the tasks that we really

### [46:49 - 46:51]

where a lot of the tasks that we really want to solve as academics lie here

### [46:51 - 46:51]

want to solve as academics lie here

### [46:51 - 46:52]

want to solve as academics lie here where they're really hard because we

### [46:52 - 46:52]

where they're really hard because we

### [46:52 - 46:54]

where they're really hard because we don't have a lot of data, but often

### [46:54 - 46:54]

don't have a lot of data, but often

### [46:54 - 46:56]

don't have a lot of data, but often times it's hard to convince people to

### [46:56 - 46:56]

times it's hard to convince people to

### [46:56 - 46:57]

times it's hard to convince people to pay you to get it's hard to convince

### [46:57 - 46:57]

pay you to get it's hard to convince

### [46:57 - 46:58]

pay you to get it's hard to convince people that that's sort of economically

### [46:58 - 46:58]

people that that's sort of economically

### [46:58 - 47:00]

people that that's sort of economically viable. And the tasks that have a lot of

### [47:00 - 47:00]

viable. And the tasks that have a lot of

### [47:00 - 47:02]

viable. And the tasks that have a lot of impact, you can just kind of MTurk your

### [47:02 - 47:02]

impact, you can just kind of MTurk your

### [47:02 - 47:04]

impact, you can just kind of MTurk your way out of them. Uh so, that's sort of

### [47:04 - 47:04]

way out of them. Uh so, that's sort of

### [47:04 - 47:06]

way out of them. Uh so, that's sort of my bitter lesson. But, I actually think

### [47:06 - 47:06]

my bitter lesson. But, I actually think

### [47:06 - 47:07]

my bitter lesson. But, I actually think that there are really fundamental

### [47:07 - 47:07]

that there are really fundamental

### [47:07 - 47:09]

that there are really fundamental challenges in the longer horizon, and I

### [47:09 - 47:09]

challenges in the longer horizon, and I

### [47:09 - 47:10]

challenges in the longer horizon, and I think the main challenge I think lots of

### [47:10 - 47:10]

think the main challenge I think lots of

### [47:10 - 47:12]

think the main challenge I think lots of us agree is that we don't have any model

### [47:12 - 47:12]

us agree is that we don't have any model

### [47:12 - 47:14]

us agree is that we don't have any model that goes and adapts and learns sort of

### [47:14 - 47:14]

that goes and adapts and learns sort of

### [47:14 - 47:16]

that goes and adapts and learns sort of on its own, right? So, my favorite

### [47:16 - 47:16]

on its own, right? So, my favorite

### [47:16 - 47:19]

on its own, right? So, my favorite example is that orangutans can drive.

### [47:19 - 47:19]

example is that orangutans can drive.

### [47:19 - 47:21]

example is that orangutans can drive. Right? Uh they drive really well, and

### [47:21 - 47:21]

Right? Uh they drive really well, and

### [47:21 - 47:23]

Right? Uh they drive really well, and the amount of training flops needed to

### [47:23 - 47:23]

the amount of training flops needed to

### [47:23 - 47:25]

the amount of training flops needed to learn to drive is probably pretty small.

### [47:25 - 47:25]

learn to drive is probably pretty small.

### [47:25 - 47:29]

learn to drive is probably pretty small. Uh I especially if you compare to Waymo.

### [47:29 - 47:29]

Uh I especially if you compare to Waymo.

### [47:29 - 47:30]

Uh I especially if you compare to Waymo. >> [laughter]

### [47:30 - 47:30]

>> [laughter]

### [47:30 - 47:31]

>> [laughter] >> So, I think that we still have a ways to

### [47:31 - 47:31]

>> So, I think that we still have a ways to

### [47:31 - 47:32]

>> So, I think that we still have a ways to go, but maybe it's less about

### [47:32 - 47:32]

go, but maybe it's less about

### [47:32 - 47:34]

go, but maybe it's less about capabilities and more about these kind

### [47:34 - 47:34]

capabilities and more about these kind

### [47:34 - 47:35]

capabilities and more about these kind of meta capabilities.

### [47:35 - 47:35]

of meta capabilities.

### [47:35 - 47:36]

of meta capabilities. Um and then lastly, I want to end with

### [47:36 - 47:36]

Um and then lastly, I want to end with

### [47:36 - 47:38]

Um and then lastly, I want to end with like a little coda about what's what

### [47:38 - 47:38]

like a little coda about what's what

### [47:38 - 47:39]

like a little coda about what's what might what we might learn about this

### [47:39 - 47:39]

might what we might learn about this

### [47:39 - 47:41]

might what we might learn about this going sort of beyond robotics. So,

### [47:41 - 47:41]

going sort of beyond robotics. So,

### [47:41 - 47:43]

going sort of beyond robotics. So, compounding error can arise in any

### [47:43 - 47:43]

compounding error can arise in any

### [47:43 - 47:44]

compounding error can arise in any situation where you have a model that's

### [47:44 - 47:44]

situation where you have a model that's

### [47:44 - 47:46]

situation where you have a model that's deployed in closed loop with itself. So,

### [47:46 - 47:46]

deployed in closed loop with itself. So,

### [47:46 - 47:48]

deployed in closed loop with itself. So, that could be language modeling as you

### [47:48 - 47:48]

that could be language modeling as you

### [47:48 - 47:49]

that could be language modeling as you generate your own outputs, that could be

### [47:49 - 47:49]

generate your own outputs, that could be

### [47:49 - 47:50]

generate your own outputs, that could be generative modeling as you have a flow

### [47:50 - 47:50]

generative modeling as you have a flow

### [47:50 - 47:52]

generative modeling as you have a flow of many steps.

### [47:52 - 47:52]

of many steps.

### [47:52 - 47:53]

of many steps. And we might ask ourselves if there are

### [47:53 - 47:53]

And we might ask ourselves if there are

### [47:53 - 47:55]

And we might ask ourselves if there are some deep learning optimizations that

### [47:55 - 47:55]

some deep learning optimizations that

### [47:55 - 47:57]

some deep learning optimizations that might directly attack this compounding

### [47:57 - 47:57]

might directly attack this compounding

### [47:57 - 47:59]

might directly attack this compounding error even without new data, much in the

### [47:59 - 47:59]

error even without new data, much in the

### [47:59 - 48:01]

error even without new data, much in the way that flow models give us better

### [48:01 - 48:01]

way that flow models give us better

### [48:01 - 48:02]

way that flow models give us better generalization without explicitly

### [48:02 - 48:02]

generalization without explicitly

### [48:02 - 48:04]

generalization without explicitly collecting more new data.

### [48:04 - 48:04]

collecting more new data.

### [48:04 - 48:06]

collecting more new data. So, this is kind of useful in this kind

### [48:06 - 48:06]

So, this is kind of useful in this kind

### [48:06 - 48:08]

So, this is kind of useful in this kind of tail case, right?

### [48:08 - 48:08]

of tail case, right?

### [48:08 - 48:10]

of tail case, right? So, uh one Thomas who the action

### [48:10 - 48:10]

So, uh one Thomas who the action

### [48:10 - 48:12]

So, uh one Thomas who the action chunking work has been sort of working

### [48:12 - 48:12]

chunking work has been sort of working

### [48:12 - 48:13]

chunking work has been sort of working on an optimizer also with my student

### [48:13 - 48:13]

on an optimizer also with my student

### [48:13 - 48:16]

on an optimizer also with my student Efe, um which can show improvements in

### [48:16 - 48:16]

Efe, um which can show improvements in

### [48:16 - 48:18]

Efe, um which can show improvements in not necessarily training curves, but in

### [48:18 - 48:18]

not necessarily training curves, but in

### [48:18 - 48:20]

not necessarily training curves, but in terms of actual generalization error

### [48:20 - 48:20]

terms of actual generalization error

### [48:20 - 48:22]

terms of actual generalization error when deployed on robotics, but also in

### [48:22 - 48:22]

when deployed on robotics, but also in

### [48:22 - 48:24]

when deployed on robotics, but also in cases of language and in fact in

### [48:24 - 48:24]

cases of language and in fact in

### [48:24 - 48:26]

cases of language and in fact in generative modeling. And it suggests

### [48:26 - 48:26]

generative modeling. And it suggests

### [48:26 - 48:27]

generative modeling. And it suggests that there's still like a whole world of

### [48:27 - 48:27]

that there's still like a whole world of

### [48:27 - 48:29]

that there's still like a whole world of deep learning principles to be explored

### [48:29 - 48:29]

deep learning principles to be explored

### [48:29 - 48:31]

deep learning principles to be explored to investigate this test time feedback.

### [48:31 - 48:31]

to investigate this test time feedback.

### [48:31 - 48:33]

to investigate this test time feedback. Uh and please expect an archive release

### [48:33 - 48:33]

Uh and please expect an archive release

### [48:33 - 48:34]

Uh and please expect an archive release of that soon in the next few weeks, and

### [48:34 - 48:34]

of that soon in the next few weeks, and

### [48:34 - 48:36]

of that soon in the next few weeks, and thanks for coming.

### [48:36 - 48:36]

thanks for coming.

### [48:36 - 48:41]

thanks for coming. >> [applause]

### [48:48 - 48:48]

Yes, Stephen. I thought of a question in

### [48:48 - 48:50]

Yes, Stephen. I thought of a question in the reverse order. So, Yeah. first

### [48:50 - 48:50]

the reverse order. So, Yeah. first

### [48:50 - 48:52]

the reverse order. So, Yeah. first generalization, the very last

### [48:52 - 48:52]

generalization, the very last

### [48:52 - 48:53]

generalization, the very last generalization that you mentioned about

### [48:53 - 48:53]

generalization that you mentioned about

### [48:53 - 48:55]

generalization that you mentioned about like noising the expert, you can't

### [48:55 - 48:55]

like noising the expert, you can't

### [48:55 - 48:56]

like noising the expert, you can't actually train that, is that right?

### [48:56 - 48:56]

actually train that, is that right?

### [48:56 - 48:58]

actually train that, is that right? Because you would need to like noise and

### [48:58 - 48:58]

Because you would need to like noise and

### [48:58 - 49:00]

Because you would need to like noise and then get expert demonstrations if you

### [49:00 - 49:00]

then get expert demonstrations if you

### [49:00 - 49:01]

then get expert demonstrations if you like Oh, yeah, you have to change how

### [49:01 - 49:01]

like Oh, yeah, you have to change how

### [49:01 - 49:02]

like Oh, yeah, you have to change how your data your data's actually

### [49:02 - 49:02]

your data your data's actually

### [49:02 - 49:04]

your data your data's actually collected. Yeah. Yes, exactly. So, I

### [49:04 - 49:04]

collected. Yeah. Yes, exactly. So, I

### [49:04 - 49:05]

collected. Yeah. Yes, exactly. So, I mean, you can train that, you just

### [49:05 - 49:05]

mean, you can train that, you just

### [49:05 - 49:06]

mean, you can train that, you just assume that your expert controls the

### [49:06 - 49:06]

assume that your expert controls the

### [49:06 - 49:07]

assume that your expert controls the data differently. So, in practice, what

### [49:07 - 49:07]

data differently. So, in practice, what

### [49:07 - 49:09]

data differently. So, in practice, what people will do is they won't noise their

### [49:09 - 49:09]

people will do is they won't noise their

### [49:09 - 49:10]

people will do is they won't noise their actions, but they'll kind of have an

### [49:10 - 49:10]

actions, but they'll kind of have an

### [49:10 - 49:11]

actions, but they'll kind of have an expert collect for coverage data,

### [49:11 - 49:11]

expert collect for coverage data,

### [49:11 - 49:12]

expert collect for coverage data, they'll have an expert show some

### [49:12 - 49:12]

they'll have an expert show some

### [49:12 - 49:14]

they'll have an expert show some mistakes and how to fix those mistakes,

### [49:14 - 49:14]

mistakes and how to fix those mistakes,

### [49:14 - 49:15]

mistakes and how to fix those mistakes, and that seems to be very empirically

### [49:15 - 49:15]

and that seems to be very empirically

### [49:15 - 49:16]

and that seems to be very empirically useful.

### [49:16 - 49:16]

useful.

### [49:16 - 49:17]

useful. Yeah. And then for the MIP, I think the

### [49:17 - 49:17]

Yeah. And then for the MIP, I think the

### [49:17 - 49:18]

Yeah. And then for the MIP, I think the equations were a bit wrong, so I didn't

### [49:18 - 49:18]

equations were a bit wrong, so I didn't

### [49:18 - 49:20]

equations were a bit wrong, so I didn't parse them too well, but like the

### [49:20 - 49:20]

parse them too well, but like the

### [49:20 - 49:22]

parse them too well, but like the first one, you you train one on just

### [49:22 - 49:22]

first one, you you train one on just

### [49:22 - 49:23]

first one, you you train one on just pure regression? Yeah. And then you

### [49:23 - 49:23]

pure regression? Yeah. And then you

### [49:23 - 49:24]

pure regression? Yeah. And then you noise it, and then you

### [49:24 - 49:24]

noise it, and then you

### [49:24 - 49:26]

noise it, and then you and then Yes. Okay.

### [49:26 - 49:26]

and then Yes. Okay.

### [49:26 - 49:27]

and then Yes. Okay. Yeah. You and and then you made a maybe

### [49:27 - 49:27]

Yeah. You and and then you made a maybe

### [49:27 - 49:29]

Yeah. You and and then you made a maybe offhand remark about how the flow is

### [49:29 - 49:29]

offhand remark about how the flow is

### [49:29 - 49:32]

offhand remark about how the flow is both noising actions and observations?

### [49:32 - 49:32]

both noising actions and observations?

### [49:32 - 49:34]

both noising actions and observations? Uh no, not exactly. The flow is noising

### [49:34 - 49:34]

Uh no, not exactly. The flow is noising

### [49:34 - 49:36]

Uh no, not exactly. The flow is noising actions, but the point is that the flow

### [49:36 - 49:36]

actions, but the point is that the flow

### [49:36 - 49:38]

actions, but the point is that the flow is recovering certain inductive biases

### [49:38 - 49:38]

is recovering certain inductive biases

### [49:38 - 49:39]

is recovering certain inductive biases that you might have gotten if you were

### [49:39 - 49:39]

that you might have gotten if you were

### [49:39 - 49:41]

that you might have gotten if you were noising the observations. And the like

### [49:41 - 49:41]

noising the observations. And the like

### [49:41 - 49:43]

noising the observations. And the like the 15 In the manifold thing, yeah,

### [49:43 - 49:43]

the 15 In the manifold thing, yeah,

### [49:43 - 49:45]

the 15 In the manifold thing, yeah, exactly.

### [49:45 - 49:45]

exactly.

### [49:45 - 49:47]

exactly. And then for the like evaluations, you

### [49:47 - 49:47]

And then for the like evaluations, you

### [49:47 - 49:50]

And then for the like evaluations, you mentioned that like action chunking

### [49:50 - 49:50]

mentioned that like action chunking

### [49:50 - 49:51]

mentioned that like action chunking it's the like roll evaluation length

### [49:51 - 49:51]

it's the like roll evaluation length

### [49:51 - 49:53]

it's the like roll evaluation length that matters and not just the chunk

### [49:53 - 49:53]

that matters and not just the chunk

### [49:53 - 49:54]

that matters and not just the chunk length. Well, it's the evaluation

### [49:54 - 49:54]

length. Well, it's the evaluation

### [49:54 - 49:55]

length. Well, it's the evaluation length, not just the training length,

### [49:55 - 49:55]

length, not just the training length,

### [49:55 - 49:56]

length, not just the training length, right? Because if you want to predict a

### [49:56 - 49:56]

right? Because if you want to predict a

### [49:56 - 49:58]

right? Because if you want to predict a chunk of say 16, you have to train to

### [49:58 - 49:58]

chunk of say 16, you have to train to

### [49:58 - 50:00]

chunk of say 16, you have to train to predict at least 16 steps, and then you

### [50:00 - 50:00]

predict at least 16 steps, and then you

### [50:00 - 50:03]

predict at least 16 steps, and then you can evaluate up to 16 steps. So, if it

### [50:03 - 50:03]

can evaluate up to 16 steps. So, if it

### [50:03 - 50:04]

can evaluate up to 16 steps. So, if it was just a representation learning

### [50:04 - 50:04]

was just a representation learning

### [50:04 - 50:05]

was just a representation learning effect, then you might be able to train

### [50:05 - 50:05]

effect, then you might be able to train

### [50:05 - 50:07]

effect, then you might be able to train predicting 16 steps and roll out one

### [50:07 - 50:07]

predicting 16 steps and roll out one

### [50:07 - 50:09]

predicting 16 steps and roll out one step at a time. But, in fact, you need

### [50:09 - 50:09]

step at a time. But, in fact, you need

### [50:09 - 50:12]

step at a time. But, in fact, you need to roll out 4 8 16 to reap the benefits.

### [50:12 - 50:12]

to roll out 4 8 16 to reap the benefits.

### [50:12 - 50:14]

to roll out 4 8 16 to reap the benefits. Yeah. So, so in in language models, when

### [50:14 - 50:14]

Yeah. So, so in in language models, when

### [50:14 - 50:15]

Yeah. So, so in in language models, when you do auto regression, like it's

### [50:15 - 50:15]

you do auto regression, like it's

### [50:15 - 50:16]

you do auto regression, like it's non-Markovian because you're training on

### [50:16 - 50:16]

non-Markovian because you're training on

### [50:16 - 50:18]

non-Markovian because you're training on a pre-like a previous tokens, but you

### [50:18 - 50:18]

a pre-like a previous tokens, but you

### [50:18 - 50:20]

a pre-like a previous tokens, but you are rolling it out one by one. Yeah,

### [50:20 - 50:20]

are rolling it out one by one. Yeah,

### [50:20 - 50:22]

are rolling it out one by one. Yeah, Markovian is complicated. If the context

### [50:22 - 50:22]

Markovian is complicated. If the context

### [50:22 - 50:24]

Markovian is complicated. If the context is state, then it is Markovian.

### [50:24 - 50:24]

is state, then it is Markovian.

### [50:24 - 50:25]

is state, then it is Markovian. We can talk about that offline because I

### [50:25 - 50:25]

We can talk about that offline because I

### [50:25 - 50:27]

We can talk about that offline because I want to let's have Yeah. Thanks,

### [50:27 - 50:27]

want to let's have Yeah. Thanks,

### [50:27 - 50:28]

want to let's have Yeah. Thanks, Stephen.

### [50:28 - 50:28]

Stephen.

### [50:28 - 50:30]

Stephen. Yes. What's the name of your work again

### [50:30 - 50:30]

Yes. What's the name of your work again

### [50:30 - 50:32]

Yes. What's the name of your work again that talked about this off-manifold and

### [50:32 - 50:32]

that talked about this off-manifold and

### [50:32 - 50:34]

that talked about this off-manifold and on-manifold error between regression and

### [50:34 - 50:34]

on-manifold error between regression and

### [50:34 - 50:36]

on-manifold error between regression and Uh much ado about noising. Much ado

### [50:36 - 50:36]

Uh much ado about noising. Much ado

### [50:36 - 50:38]

Uh much ado about noising. Much ado about noising, yeah. Yeah.

### [50:38 - 50:38]

about noising, yeah. Yeah.

### [50:38 - 50:39]

about noising, yeah. Yeah. Yes.

### [50:39 - 50:39]

Yes.

### [50:39 - 50:40]

Yes. You mentioned that in the long term we

### [50:40 - 50:40]

You mentioned that in the long term we

### [50:40 - 50:42]

You mentioned that in the long term we might not need action chunking and I

### [50:42 - 50:42]

might not need action chunking and I

### [50:42 - 50:43]

might not need action chunking and I think there's a lot of cases where you

### [50:43 - 50:43]

think there's a lot of cases where you

### [50:43 - 50:45]

think there's a lot of cases where you need like really high frequency control

### [50:45 - 50:45]

need like really high frequency control

### [50:45 - 50:46]

need like really high frequency control like in contact.

### [50:46 - 50:46]

like in contact.

### [50:46 - 50:47]

like in contact. Um

### [50:47 - 50:47]

Um

### [50:47 - 50:48]

Um can you talk a little bit more about

### [50:48 - 50:48]

can you talk a little bit more about

### [50:48 - 50:49]

can you talk a little bit more about what innovations need to

### [50:49 - 50:49]

what innovations need to

### [50:49 - 50:51]

what innovations need to >> Yeah. Yeah, so I think that the right

### [50:51 - 50:51]

>> Yeah. Yeah, so I think that the right

### [50:51 - 50:53]

>> Yeah. Yeah, so I think that the right way to do this is you can predict long

### [50:53 - 50:53]

way to do this is you can predict long

### [50:53 - 50:54]

way to do this is you can predict long sequence um

### [50:54 - 50:54]

sequence um

### [50:54 - 50:55]

sequence um there are students in the room who are

### [50:55 - 50:55]

there are students in the room who are

### [50:55 - 50:56]

there are students in the room who are working with me on sort of the next

### [50:56 - 50:56]

working with me on sort of the next

### [50:56 - 50:57]

working with me on sort of the next version of this, but you can you

### [50:57 - 50:57]

version of this, but you can you

### [50:57 - 50:59]

version of this, but you can you basically should have some form of

### [50:59 - 50:59]

basically should have some form of

### [50:59 - 51:00]

basically should have some form of predicting long sequence things for

### [51:00 - 51:00]

predicting long sequence things for

### [51:00 - 51:02]

predicting long sequence things for consistency, but then if you want high

### [51:02 - 51:02]

consistency, but then if you want high

### [51:02 - 51:04]

consistency, but then if you want high precision control uh all of my negative

### [51:04 - 51:04]

precision control uh all of my negative

### [51:04 - 51:05]

precision control uh all of my negative results go away if you move from an act

### [51:05 - 51:05]

results go away if you move from an act

### [51:05 - 51:07]

results go away if you move from an act from a behavior cloning paradigm to like

### [51:07 - 51:07]

from a behavior cloning paradigm to like

### [51:07 - 51:08]

from a behavior cloning paradigm to like a reinforce online reinforcement

### [51:08 - 51:08]

a reinforce online reinforcement

### [51:08 - 51:10]

a reinforce online reinforcement learning paradigm. So, reinforcement

### [51:10 - 51:10]

learning paradigm. So, reinforcement

### [51:10 - 51:11]

learning paradigm. So, reinforcement learning sucks at exploration at least

### [51:11 - 51:11]

learning sucks at exploration at least

### [51:11 - 51:13]

learning sucks at exploration at least previous currently, but if your action

### [51:13 - 51:13]

previous currently, but if your action

### [51:13 - 51:15]

previous currently, but if your action chunking seed or if your behavior

### [51:15 - 51:15]

chunking seed or if your behavior

### [51:15 - 51:16]

chunking seed or if your behavior cloning seeds it into like a good kind

### [51:16 - 51:16]

cloning seeds it into like a good kind

### [51:16 - 51:18]

cloning seeds it into like a good kind of warm start, it's very easy to learn

### [51:18 - 51:18]

of warm start, it's very easy to learn

### [51:18 - 51:20]

of warm start, it's very easy to learn how to improve your control policy with

### [51:20 - 51:20]

how to improve your control policy with

### [51:20 - 51:22]

how to improve your control policy with on-policy reinforcement learning. And

### [51:22 - 51:22]

on-policy reinforcement learning. And

### [51:22 - 51:23]

on-policy reinforcement learning. And so, I think we're going to use that to

### [51:23 - 51:23]

so, I think we're going to use that to

### [51:23 - 51:25]

so, I think we're going to use that to learn to learn sort of high frequency

### [51:25 - 51:25]

learn to learn sort of high frequency

### [51:25 - 51:26]

learn to learn sort of high frequency residuals, for example. Yeah. So, is

### [51:26 - 51:26]

residuals, for example. Yeah. So, is

### [51:26 - 51:28]

residuals, for example. Yeah. So, is that online reinforcement learning

### [51:28 - 51:28]

that online reinforcement learning

### [51:28 - 51:30]

that online reinforcement learning process actually solving the issue of

### [51:30 - 51:30]

process actually solving the issue of

### [51:30 - 51:31]

process actually solving the issue of like the compounding error?

### [51:31 - 51:31]

like the compounding error?

### [51:31 - 51:33]

like the compounding error? >> Yes, it can. Exactly. Because one way to

### [51:33 - 51:33]

>> Yes, it can. Exactly. Because one way to

### [51:33 - 51:34]

>> Yes, it can. Exactly. Because one way to think about it is the online

### [51:34 - 51:34]

think about it is the online

### [51:34 - 51:34]

think about it is the online reinforcement learning gives you a

### [51:34 - 51:34]

reinforcement learning gives you a

### [51:34 - 51:36]

reinforcement learning gives you a little bit of that exploration. And that

### [51:36 - 51:36]

little bit of that exploration. And that

### [51:36 - 51:38]

little bit of that exploration. And that exploration kind of gives you that those

### [51:38 - 51:38]

exploration kind of gives you that those

### [51:38 - 51:39]

exploration kind of gives you that those directions that might be unstable, and

### [51:39 - 51:39]

directions that might be unstable, and

### [51:39 - 51:41]

directions that might be unstable, and then it just teaches you how to kind of

### [51:41 - 51:41]

then it just teaches you how to kind of

### [51:41 - 51:44]

then it just teaches you how to kind of correct from those. Yeah.

### [51:47 - 51:47]

Yes. For action chunking, how big is K

### [51:47 - 51:49]

Yes. For action chunking, how big is K star compared to the horizon?

### [51:49 - 51:49]

star compared to the horizon?

### [51:49 - 51:51]

star compared to the horizon? >> the the the the answer is four or eight.

### [51:51 - 51:51]

>> the the the the answer is four or eight.

### [51:51 - 51:52]

>> the the the the answer is four or eight. The second that's like the So, it

### [51:52 - 51:52]

The second that's like the So, it

### [51:52 - 51:54]

The second that's like the So, it actually depends. If you're using it for

### [51:54 - 51:54]

actually depends. If you're using it for

### [51:54 - 51:55]

actually depends. If you're using it for pre-training, a lot of pre-trained

### [51:55 - 51:55]

pre-training, a lot of pre-trained

### [51:55 - 51:57]

pre-training, a lot of pre-trained models will use very long action chunks

### [51:57 - 51:57]

models will use very long action chunks

### [51:57 - 51:58]

models will use very long action chunks because they are probably also using it

### [51:58 - 51:58]

because they are probably also using it

### [51:58 - 52:00]

because they are probably also using it for representation learning and for very

### [52:00 - 52:00]

for representation learning and for very

### [52:00 - 52:02]

for representation learning and for very complicated tasks. So, I think Pi uses

### [52:02 - 52:02]

complicated tasks. So, I think Pi uses

### [52:02 - 52:05]

complicated tasks. So, I think Pi uses like 50 I I believe, but um in sort of

### [52:05 - 52:05]

like 50 I I believe, but um in sort of

### [52:05 - 52:06]

like 50 I I believe, but um in sort of like these more simulation and

### [52:06 - 52:06]

like these more simulation and

### [52:06 - 52:08]

like these more simulation and experiments, typically four or eight is

### [52:08 - 52:08]

experiments, typically four or eight is

### [52:08 - 52:09]

experiments, typically four or eight is like the standard. So, if you were to

### [52:09 - 52:09]

like the standard. So, if you were to

### [52:09 - 52:12]

like the standard. So, if you were to pull up your favorite like diffusion RL

### [52:12 - 52:12]

pull up your favorite like diffusion RL

### [52:12 - 52:13]

pull up your favorite like diffusion RL in robotics paper, it'd be around four

### [52:13 - 52:13]

in robotics paper, it'd be around four

### [52:13 - 52:16]

in robotics paper, it'd be around four or eight. Yeah.

### [52:16 - 52:16]

or eight. Yeah.

### [52:16 - 52:17]

or eight. Yeah. Cool.

### [52:17 - 52:17]

Cool.

### [52:17 - 52:19]

Cool. Yes. A quick follow-up point. So, so you

### [52:19 - 52:19]

Yes. A quick follow-up point. So, so you

### [52:19 - 52:21]

Yes. A quick follow-up point. So, so you said that K star depends on all these

### [52:21 - 52:21]

said that K star depends on all these

### [52:21 - 52:23]

said that K star depends on all these like properties of like the dynamics and

### [52:23 - 52:23]

like properties of like the dynamics and

### [52:23 - 52:26]

like properties of like the dynamics and etc. etc. Like do you have a way of

### [52:26 - 52:26]

etc. etc. Like do you have a way of

### [52:26 - 52:29]

etc. etc. Like do you have a way of estimating K star predictively or do you

### [52:29 - 52:29]

estimating K star predictively or do you

### [52:29 - 52:30]

estimating K star predictively or do you just kind of

### [52:30 - 52:30]

just kind of

### [52:30 - 52:32]

just kind of do a sweep on K star and be like which

### [52:32 - 52:32]

do a sweep on K star and be like which

### [52:32 - 52:33]

do a sweep on K star and be like which one actually works? I think I think in

### [52:33 - 52:33]

one actually works? I think I think in

### [52:33 - 52:35]

one actually works? I think I think in practice, I mean the the the sad thing

### [52:35 - 52:35]

practice, I mean the the the sad thing

### [52:35 - 52:36]

practice, I mean the the the sad thing about theory is that theory can give you

### [52:36 - 52:36]

about theory is that theory can give you

### [52:36 - 52:38]

about theory is that theory can give you qualitative insights, but it's like I'm

### [52:38 - 52:38]

qualitative insights, but it's like I'm

### [52:38 - 52:39]

qualitative insights, but it's like I'm not it's hard to get bounds that are

### [52:39 - 52:39]

not it's hard to get bounds that are

### [52:39 - 52:41]

not it's hard to get bounds that are tight and predictive. Uh so, I think in

### [52:41 - 52:41]

tight and predictive. Uh so, I think in

### [52:41 - 52:44]

tight and predictive. Uh so, I think in practice, you your grad student tries

### [52:44 - 52:44]

practice, you your grad student tries

### [52:44 - 52:45]

practice, you your grad student tries four or eight.

### [52:45 - 52:45]

four or eight.

### [52:45 - 52:45]

four or eight. >> [laughter]

### [52:45 - 52:45]

>> [laughter]

### [52:45 - 52:46]

>> [laughter] >> And I'm sorry.

### [52:46 - 52:46]

>> And I'm sorry.

### [52:46 - 52:47]

>> And I'm sorry. I want to be honest about that, but I

### [52:47 - 52:47]

I want to be honest about that, but I

### [52:47 - 52:48]

I want to be honest about that, but I think that's that's what ends up

### [52:48 - 52:48]

think that's that's what ends up

### [52:48 - 52:51]

think that's that's what ends up happening. It's is it's like uh yeah.

### [52:51 - 52:51]

happening. It's is it's like uh yeah.

### [52:51 - 52:53]

happening. It's is it's like uh yeah. Uh um

### [52:53 - 52:53]

Uh um

### [52:53 - 52:54]

Uh um probably any bound that you would derive

### [52:54 - 52:54]

probably any bound that you would derive

### [52:54 - 52:55]

probably any bound that you would derive theoretically would be overly

### [52:55 - 52:55]

theoretically would be overly

### [52:55 - 52:58]

theoretically would be overly pessimistic as these kind of bounds are.

### [52:58 - 52:58]

pessimistic as these kind of bounds are.

### [52:58 - 52:59]

pessimistic as these kind of bounds are. Yeah.

### [52:59 - 52:59]

Yeah.

### [52:59 - 53:00]

Yeah. Yes.

### [53:00 - 53:00]

Yes.

### [53:00 - 53:03]

Yes. In language models, there is a like a

### [53:03 - 53:03]

In language models, there is a like a

### [53:03 - 53:06]

In language models, there is a like a compression trick for long context

### [53:06 - 53:06]

compression trick for long context

### [53:06 - 53:08]

compression trick for long context generation where as you generate, you

### [53:08 - 53:08]

generation where as you generate, you

### [53:08 - 53:11]

generation where as you generate, you are like compressing the

### [53:11 - 53:11]

are like compressing the

### [53:11 - 53:13]

are like compressing the uh like key value caches in Yes. the

### [53:13 - 53:13]

uh like key value caches in Yes. the

### [53:13 - 53:15]

uh like key value caches in Yes. the prefix. And I'm trying I'm wondering

### [53:15 - 53:15]

prefix. And I'm trying I'm wondering

### [53:15 - 53:17]

prefix. And I'm trying I'm wondering whether there is a connection between

### [53:17 - 53:17]

whether there is a connection between

### [53:17 - 53:19]

whether there is a connection between this compression trick and the

### [53:19 - 53:19]

this compression trick and the

### [53:19 - 53:20]

this compression trick and the stability.

### [53:20 - 53:20]

stability.

### [53:20 - 53:22]

stability. For example, like whether this

### [53:22 - 53:22]

For example, like whether this

### [53:22 - 53:25]

For example, like whether this compression is destroying stability or

### [53:25 - 53:25]

compression is destroying stability or

### [53:25 - 53:26]

compression is destroying stability or improving stability. That's a great

### [53:26 - 53:26]

improving stability. That's a great

### [53:26 - 53:27]

improving stability. That's a great question. I actually think it's

### [53:27 - 53:27]

question. I actually think it's

### [53:27 - 53:30]

question. I actually think it's improving stability. So, the thing with

### [53:30 - 53:30]

improving stability. So, the thing with

### [53:30 - 53:31]

improving stability. So, the thing with a language model is that it's a really

### [53:31 - 53:31]

a language model is that it's a really

### [53:31 - 53:33]

a language model is that it's a really complicated dynamical system because as

### [53:33 - 53:33]

complicated dynamical system because as

### [53:33 - 53:36]

complicated dynamical system because as you add more context, your Think of the

### [53:36 - 53:36]

you add more context, your Think of the

### [53:36 - 53:37]

you add more context, your Think of the think of the dynamical system not just

### [53:37 - 53:37]

think of the dynamical system not just

### [53:37 - 53:38]

think of the dynamical system not just as your language model, but as every

### [53:38 - 53:38]

as your language model, but as every

### [53:38 - 53:40]

as your language model, but as every layer in the language model. So, like

### [53:40 - 53:40]

layer in the language model. So, like

### [53:40 - 53:41]

layer in the language model. So, like you kind of have this two-level thing

### [53:41 - 53:41]

you kind of have this two-level thing

### [53:41 - 53:43]

you kind of have this two-level thing where like your language model creates

### [53:43 - 53:43]

where like your language model creates

### [53:43 - 53:44]

where like your language model creates this like a layer makes a step, a layer

### [53:44 - 53:44]

this like a layer makes a step, a layer

### [53:44 - 53:45]

this like a layer makes a step, a layer makes a step, a layer makes a step.

### [53:45 - 53:45]

makes a step, a layer makes a step.

### [53:45 - 53:46]

makes a step, a layer makes a step. You're done with the forward pass, you

### [53:46 - 53:46]

You're done with the forward pass, you

### [53:46 - 53:48]

You're done with the forward pass, you put you write a token, and step steps

### [53:48 - 53:48]

put you write a token, and step steps

### [53:48 - 53:50]

put you write a token, and step steps up, right? So, the more you have in

### [53:50 - 53:50]

up, right? So, the more you have in

### [53:50 - 53:53]

up, right? So, the more you have in context, basically like the wider range

### [53:53 - 53:53]

context, basically like the wider range

### [53:53 - 53:54]

context, basically like the wider range of things that your attention has to pay

### [53:54 - 53:54]

of things that your attention has to pay

### [53:54 - 53:56]

of things that your attention has to pay attention to. And this can cause various

### [53:56 - 53:56]

attention to. And this can cause various

### [53:56 - 53:58]

attention to. And this can cause various forms of like attention glitches. Like

### [53:58 - 53:58]

forms of like attention glitches. Like

### [53:58 - 53:59]

forms of like attention glitches. Like there've been a lot of papers I think

### [53:59 - 53:59]

there've been a lot of papers I think

### [53:59 - 54:01]

there've been a lot of papers I think 2022 like Bing Bin Lu wrote some really

### [54:01 - 54:01]

2022 like Bing Bin Lu wrote some really

### [54:01 - 54:03]

2022 like Bing Bin Lu wrote some really nice papers on this. And so, one way to

### [54:03 - 54:03]

nice papers on this. And so, one way to

### [54:03 - 54:04]

nice papers on this. And so, one way to interpret this compression is just

### [54:04 - 54:04]

interpret this compression is just

### [54:04 - 54:06]

interpret this compression is just saying that like a lot of weird sort of

### [54:06 - 54:06]

saying that like a lot of weird sort of

### [54:06 - 54:09]

saying that like a lot of weird sort of like erratic errors in like your

### [54:09 - 54:09]

like erratic errors in like your

### [54:09 - 54:10]

like erratic errors in like your attention weights where things weren't

### [54:10 - 54:10]

attention weights where things weren't

### [54:10 - 54:11]

attention weights where things weren't learned perfectly, those can add up a

### [54:11 - 54:11]

learned perfectly, those can add up a

### [54:11 - 54:14]

learned perfectly, those can add up a ton uh in the in in history, and if you

### [54:14 - 54:14]

ton uh in the in in history, and if you

### [54:14 - 54:16]

ton uh in the in in history, and if you don't do compression, then uh then you

### [54:16 - 54:16]

don't do compression, then uh then you

### [54:16 - 54:17]

don't do compression, then uh then you might like pay attention to a lot of

### [54:17 - 54:17]

might like pay attention to a lot of

### [54:17 - 54:19]

might like pay attention to a lot of these spurious things that add up and

### [54:19 - 54:19]

these spurious things that add up and

### [54:19 - 54:20]

these spurious things that add up and have a like sort of play a larger role

### [54:20 - 54:20]

have a like sort of play a larger role

### [54:20 - 54:22]

have a like sort of play a larger role in the attention weight. Yeah.

### [54:22 - 54:22]

in the attention weight. Yeah.

### [54:22 - 54:26]

in the attention weight. Yeah. Thank you. Yeah, of course.

### [54:29 - 54:29]

Cool. Yeah. Uh you mentioned in one of

### [54:29 - 54:31]

Cool. Yeah. Uh you mentioned in one of the slides you are comparing the

### [54:31 - 54:31]

the slides you are comparing the

### [54:31 - 54:33]

the slides you are comparing the continuous and discrete learning

### [54:33 - 54:33]

continuous and discrete learning

### [54:33 - 54:34]

continuous and discrete learning paradigms.

### [54:34 - 54:34]

paradigms.

### [54:34 - 54:36]

paradigms. Uh I know there's like pushes recently

### [54:36 - 54:36]

Uh I know there's like pushes recently

### [54:36 - 54:38]

Uh I know there's like pushes recently to frame robotics as like discrete

### [54:38 - 54:38]

to frame robotics as like discrete

### [54:38 - 54:40]

to frame robotics as like discrete learning. Uh do you think all of these

### [54:40 - 54:40]

learning. Uh do you think all of these

### [54:40 - 54:42]

learning. Uh do you think all of these innovations will still hold any

### [54:42 - 54:42]

innovations will still hold any

### [54:42 - 54:45]

innovations will still hold any important if we learn robotics as a

### [54:45 - 54:45]

important if we learn robotics as a

### [54:45 - 54:46]

important if we learn robotics as a discrete problem? So, I've been thinking

### [54:46 - 54:46]

discrete problem? So, I've been thinking

### [54:46 - 54:48]

discrete problem? So, I've been thinking a lot about this because I've been

### [54:48 - 54:48]

a lot about this because I've been

### [54:48 - 54:49]

a lot about this because I've been talking to some people who want to

### [54:49 - 54:49]

talking to some people who want to

### [54:49 - 54:51]

talking to some people who want to rethink kind of how to do tokenization

### [54:51 - 54:51]

rethink kind of how to do tokenization

### [54:51 - 54:53]

rethink kind of how to do tokenization in robotics.

### [54:53 - 54:53]

in robotics.

### [54:53 - 54:55]

in robotics. The the my current stance on this is

### [54:55 - 54:55]

The the my current stance on this is

### [54:55 - 54:57]

The the my current stance on this is that if you wanted turn everything into

### [54:57 - 54:57]

that if you wanted turn everything into

### [54:57 - 54:59]

that if you wanted turn everything into discrete tokens,

### [54:59 - 54:59]

discrete tokens,

### [54:59 - 55:01]

discrete tokens, I don't know how you onboard new tokens,

### [55:01 - 55:01]

I don't know how you onboard new tokens,

### [55:01 - 55:02]

I don't know how you onboard new tokens, right? So, imagine that like all my

### [55:02 - 55:02]

right? So, imagine that like all my

### [55:02 - 55:04]

right? So, imagine that like all my robots are trained to be normal and then

### [55:04 - 55:04]

robots are trained to be normal and then

### [55:04 - 55:05]

robots are trained to be normal and then they start like doing this, but it's

### [55:05 - 55:05]

they start like doing this, but it's

### [55:05 - 55:06]

they start like doing this, but it's like for an interpretive dance and they

### [55:06 - 55:06]

like for an interpretive dance and they

### [55:06 - 55:07]

like for an interpretive dance and they have to, right? Like how does my

### [55:07 - 55:07]

have to, right? Like how does my

### [55:07 - 55:09]

have to, right? Like how does my tokenizer add that to the tokens? I

### [55:09 - 55:09]

tokenizer add that to the tokens? I

### [55:09 - 55:12]

tokenizer add that to the tokens? I don't really know. So, there's also

### [55:12 - 55:12]

don't really know. So, there's also

### [55:12 - 55:14]

don't really know. So, there's also issues with precision. So, I currently

### [55:14 - 55:14]

issues with precision. So, I currently

### [55:14 - 55:15]

issues with precision. So, I currently think that it's very useful to still

### [55:15 - 55:15]

think that it's very useful to still

### [55:15 - 55:17]

think that it's very useful to still have continuous, but to think of these

### [55:17 - 55:17]

have continuous, but to think of these

### [55:17 - 55:18]

have continuous, but to think of these as decoders or renderers rather than

### [55:18 - 55:18]

as decoders or renderers rather than

### [55:18 - 55:20]

as decoders or renderers rather than think of them as learners. So, that you

### [55:20 - 55:20]

think of them as learners. So, that you

### [55:20 - 55:21]

think of them as learners. So, that you can still pre-train on everything as

### [55:21 - 55:21]

can still pre-train on everything as

### [55:21 - 55:23]

can still pre-train on everything as being kind of continuous, but you can

### [55:23 - 55:23]

being kind of continuous, but you can

### [55:23 - 55:26]

being kind of continuous, but you can you can you can Yeah. I think but I I

### [55:26 - 55:26]

you can you can Yeah. I think but I I

### [55:26 - 55:28]

you can you can Yeah. I think but I I and so like I think in principle you

### [55:28 - 55:28]

and so like I think in principle you

### [55:28 - 55:29]

and so like I think in principle you could represent everything in discrete.

### [55:29 - 55:29]

could represent everything in discrete.

### [55:29 - 55:31]

could represent everything in discrete. Uh but you what people don't people

### [55:31 - 55:31]

Uh but you what people don't people

### [55:31 - 55:33]

Uh but you what people don't people don't want just to like discretize

### [55:33 - 55:33]

don't want just to like discretize

### [55:33 - 55:34]

don't want just to like discretize actions, they want actually tokenize

### [55:34 - 55:34]

actions, they want actually tokenize

### [55:34 - 55:35]

actions, they want actually tokenize actions into meaningful hierarchical

### [55:35 - 55:35]

actions into meaningful hierarchical

### [55:35 - 55:37]

actions into meaningful hierarchical structure and compress actions. I think

### [55:37 - 55:37]

structure and compress actions. I think

### [55:37 - 55:39]

structure and compress actions. I think that's the issue. I think ultimately

### [55:39 - 55:39]

that's the issue. I think ultimately

### [55:39 - 55:41]

that's the issue. I think ultimately 1e-4%

### [55:41 - 55:41]

1e-4%

### [55:41 - 55:42]

1e-4% is probably enough. I don't think humans

### [55:42 - 55:42]

is probably enough. I don't think humans

### [55:42 - 55:44]

is probably enough. I don't think humans have much better than that. So, we could

### [55:44 - 55:44]

have much better than that. So, we could

### [55:44 - 55:46]

have much better than that. So, we could just like, you know, do like a whatever

### [55:46 - 55:46]

just like, you know, do like a whatever

### [55:46 - 55:48]

just like, you know, do like a whatever like exponent and mantissa thing in in

### [55:48 - 55:48]

like exponent and mantissa thing in in

### [55:48 - 55:50]

like exponent and mantissa thing in in robotics and that would be fine. But, I

### [55:50 - 55:50]

robotics and that would be fine. But, I

### [55:50 - 55:52]

robotics and that would be fine. But, I think like deeper like actually

### [55:52 - 55:52]

think like deeper like actually

### [55:52 - 55:53]

think like deeper like actually compression compressing action spaces

### [55:53 - 55:53]

compression compressing action spaces

### [55:53 - 55:55]

compression compressing action spaces probably should be combined with sort of

### [55:55 - 55:55]

probably should be combined with sort of

### [55:55 - 55:57]

probably should be combined with sort of a decoder. The one fun fact, humans are

### [55:57 - 55:57]

a decoder. The one fun fact, humans are

### [55:57 - 55:59]

a decoder. The one fun fact, humans are also discrete. I think the way that our

### [55:59 - 55:59]

also discrete. I think the way that our

### [55:59 - 56:00]

also discrete. I think the way that our our motor system works from what I

### [56:00 - 56:00]

our motor system works from what I

### [56:00 - 56:02]

our motor system works from what I understand, we have like some number of

### [56:02 - 56:02]

understand, we have like some number of

### [56:02 - 56:03]

understand, we have like some number of motor units and they fire either by in a

### [56:03 - 56:03]

motor units and they fire either by in a

### [56:03 - 56:05]

motor units and they fire either by in a binary fashion. So, we are kind of using

### [56:05 - 56:05]

binary fashion. So, we are kind of using

### [56:05 - 56:07]

binary fashion. So, we are kind of using like discrete things, but we're not

### [56:07 - 56:07]

like discrete things, but we're not

### [56:07 - 56:09]

like discrete things, but we're not we're not compressed, right? Like those

### [56:09 - 56:09]

we're not compressed, right? Like those

### [56:09 - 56:10]

we're not compressed, right? Like those motor units are independent and there

### [56:10 - 56:10]

motor units are independent and there

### [56:10 - 56:11]

motor units are independent and there are millions of them or some number of

### [56:11 - 56:11]

are millions of them or some number of

### [56:11 - 56:13]

are millions of them or some number of them, right? They're not the kind of

### [56:13 - 56:13]

them, right? They're not the kind of

### [56:13 - 56:15]

them, right? They're not the kind of like four or eight sequence tokens that

### [56:15 - 56:15]

like four or eight sequence tokens that

### [56:15 - 56:17]

like four or eight sequence tokens that people are hoping to find.

### [56:17 - 56:17]

people are hoping to find.

### [56:17 - 56:19]

people are hoping to find. Cool.

### [56:19 - 56:19]

Cool.

### [56:19 - 56:21]

Cool. All right, with that let's say thank YOU

### [56:21 - 56:21]

All right, with that let's say thank YOU

### [56:21 - 56:22]

All right, with that let's say thank YOU ONCE AGAIN.

### [56:22 - 56:22]

ONCE AGAIN.

### [56:22 - 56:28]

ONCE AGAIN. >> [applause]

### [56:29 - 56:29]

>> THANK YOU, EVERYONE. WE'LL SEE YOU NEXT

### [56:29 - 56:29]

>> THANK YOU, EVERYONE. WE'LL SEE YOU NEXT WEEK.

### [56:29 - 56:29]

WEEK.

### [56:29 - 56:31]

WEEK. >> THANKS.
