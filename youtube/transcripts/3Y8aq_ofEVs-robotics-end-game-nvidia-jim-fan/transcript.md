# Robotics End Game: Nvidia Jim Fan

- URL: https://www.youtube.com/watch?v=3Y8aq_ofEVs
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-09T18:29:16`

## Transcript

### [00:00 - 00:12]

And up first, I'm delighted to introduce my friend, Jim Phan. Jim leads the embodied autonomous research group at NVIDIA, otherwise known as NVIDIA Robotics.

### [00:13 - 00:22]

I think that robots are just one of the most thrilling things that's going to happen. A car basically is a big robot, but I'm excited for robots can go beep boop and lift things for us.

### [00:22 - 00:27]

And so Jim was a standout at last year's AI Ascent, and we're delighted to have you back.

### [00:28 - 00:29]

Thanks, everyone. Thanks.

### [00:30 - 00:43]

So it was a summer day in 2016. Actually, right in this office that we're sitting in, there's a guy in shiny leather jacket, you know, big biceps, hurling in this large metal tray.

### [00:43 - 00:54]

And on this large piece of metal, he wrote, to Elon and the OpenAI team, to the future of computing and humanity, I present you the world's first DGX-1.

### [00:55 - 01:00]

So that was the first time I met Jensen. And as any good intern would do.

### [01:00 - 01:10]

I rushed to get in line to sign my name on it. So can you spot it? My name is here. And can you spot another? That's Andre right there.

### [01:10 - 01:15]

So Andre, we're going to the Computer History Museum. I feel like a dinosaur.

### [01:16 - 01:26]

You know, back then I had no clue what I was signing up for. And then no one can describe what happened next better than Ilya himself.

### [01:27 - 01:29]

If you believe in deep learning, deep learning will believe you.

### [01:30 - 01:35]

And oh, boy, did deep learning believe in all of us big time.

### [01:37 - 01:42]

Three-step functions, six years. That's how all it took to bring us here today.

### [01:42 - 01:51]

The first take, GPT-3, pre-training, next token prediction is really about learning the rules of grammar, the shape of language.

### [01:52 - 01:57]

It's about simulating how thoughts and code and strings in general should unfold.

### [01:58 - 02:00]

2022, instruct GPT.

### [02:00 - 02:04]

Supervised fine-tuning, allowing this simulation to do useful work.

### [02:06 - 02:10]

01, reasoning, using reinforcement learning to surpass imitation learning.

### [02:11 - 02:16]

And finally, auto-research, accelerating the whole loop beyond what's humanly possible.

### [02:17 - 02:22]

So as Andre said, all the labs are getting to the final boss fight.

### [02:23 - 02:26]

So for LOMs, they're in the thick of the end game.

### [02:27 - 02:28]

And honestly, I'm very jealous.

### [02:29 - 02:30]

Look at how happy I am.

### [02:30 - 02:31]

Happy Andre was.

### [02:31 - 02:33]

Big smile on his face.

### [02:34 - 02:37]

The LOM folks are having the party of their lifetime.

### [02:38 - 02:43]

They're speedrunning AGI on mythical creatures literally called mythos.

### [02:44 - 02:46]

So why can't robotics get a piece of fun?

### [02:47 - 02:53]

So as any self-respecting scientist will do, I copy homework and I give it a new name.

### [02:54 - 02:56]

I call it the Great Parallel.

### [02:56 - 03:00]

So instead of simulating strings, can we simulate next?

### [03:00 - 03:01]

The physical world state.

### [03:02 - 03:09]

And then we can align through action fine-tuning onto a thin slice of that simulation that matters for real robots.

### [03:10 - 03:13]

And we let reinforcement learning carry the last mile.

### [03:15 - 03:15]

And that's it.

### [03:16 - 03:19]

The Great Parallel, copying the LOM's success.

### [03:19 - 03:21]

If you can't beat them, join them.

### [03:21 - 03:25]

So please join me in a new episode, Robotics, the End Game.

### [03:26 - 03:27]

And sorry, I just couldn't resist.

### [03:28 - 03:28]

Not a banana is too good.

### [03:29 - 03:29]

Thanks, Demis.

### [03:31 - 03:33]

So how do we play the end game?

### [03:33 - 03:34]

It boils down to two things.

### [03:34 - 03:37]

Model strategy and data strategy.

### [03:37 - 03:39]

Let's look at a model first.

### [03:40 - 03:48]

The last three years were dominated by VOAs or visual language action models and models like Pi and Groot fall in this category.

### [03:49 - 03:55]

So we assume that the pre-training is done by a VOM and we simply graph an action head on top of it.

### [03:56 - 03:58]

But really, if you think about these models,

### [03:58 - 04:04]

they're LVAs because the most amount of parameters are dedicated to language.

### [04:04 - 04:08]

So language is first class citizen followed by vision and action.

### [04:08 - 04:14]

And by design, VOAs are great at encoding knowledge and nouns, but not so much at physics and verbs.

### [04:15 - 04:17]

It's kind of head heavy in the wrong places.

### [04:19 - 04:22]

This is my favorite example from the original VOA paper.

### [04:22 - 04:25]

Move the Coke can to a picture of Taylor Swift.

### [04:25 - 04:27]

Yes, it has not seen Taylor Swift before.

### [04:28 - 04:28]

Yes.

### [04:28 - 04:29]

It's able to generalize.

### [04:29 - 04:32]

But this is not quite a pre-training ability that we're looking for.

### [04:33 - 04:35]

So what's the second pre-training paradigm?

### [04:36 - 04:39]

And I always thought that it would be something glorious.

### [04:40 - 04:41]

Unfortunate.

### [04:41 - 04:44]

It turns out that this is AI video slop that we call.

### [04:45 - 04:49]

You know, I can watch these cats playing banjo on security cam all day.

### [04:49 - 04:50]

It's peak internet.

### [04:51 - 04:54]

But really, look at this.

### [04:54 - 04:58]

No one can take this seriously until we realize.

### [04:58 - 05:02]

That these video models are learning to simulate next world state internally.

### [05:03 - 05:05]

So these are some roles from VOA three.

### [05:06 - 05:13]

You can see that the models, they pick up gravity, buoyancy, lighting, reflection, refraction, all by themselves.

### [05:13 - 05:14]

None of this is coded in.

### [05:15 - 05:20]

Physics emerge by predicting the next blob of pixels at scale.

### [05:21 - 05:23]

And even visual planning emerges.

### [05:24 - 05:27]

Look at how VO solves these maces.

### [05:28 - 05:31]

It solves them by running simulation forward in pixel space.

### [05:32 - 05:35]

And draw attention to the lower right corner here.

### [05:35 - 05:36]

This is my favorite example.

### [05:36 - 05:40]

Let's watch and you blink if you miss how VO3 solves this one.

### [05:43 - 05:44]

It's super smart.

### [05:44 - 05:48]

You know, VO3 figures out that if you're not looking, geometry is optional.

### [05:50 - 05:51]

I call this physics slop.

### [05:53 - 05:56]

So how do we make these world models useful?

### [05:56 - 05:59]

Well, we do action fine tuning.

### [05:59 - 06:08]

We align this superposition of all possible future states and collapse that onto a thing size that matters for real robots.

### [06:10 - 06:11]

Introducing dream zero.

### [06:12 - 06:18]

It's a new type of policy model that dreams a couple of seconds into the future and acts accordingly.

### [06:20 - 06:24]

And you know that motor actions, there are high dimensional continuous signals.

### [06:24 - 06:26]

So that looks just like pixels.

### [06:26 - 06:29]

We can render it at the same time as we render the videos.

### [06:30 - 06:35]

So dream zero jointly decodes the next world states and next actions.

### [06:35 - 06:42]

And as a result, it's able to zero shot, solve tasks and verbs that it has never seen in training.

### [06:44 - 06:47]

And as a robot executes, we can visualize what it's dreaming about.

### [06:48 - 06:49]

And the correlation is very tight.

### [06:49 - 06:51]

If the video prediction works, the action works.

### [06:52 - 06:54]

If the video hallucinates, the action fails.

### [06:54 - 06:59]

So once again, vision and action are now first class citizens.

### [07:00 - 07:02]

And we have a lot of fun with dream zero.

### [07:02 - 07:07]

So we just wrote a robot around in our lab and then type random things into the prompt box.

### [07:08 - 07:13]

And of course, dream zero is not going to get all of these tasks 100% robust.

### [07:14 - 07:15]

But it's kind of like GPT-2.

### [07:16 - 07:19]

It's trying to get the shape of the motion correct in every case.

### [07:20 - 07:24]

So dream zero is our first step towards open-ended, open vocabulary.

### [07:24 - 07:27]

And it's very, very prompting for robotics.

### [07:28 - 07:31]

And we call this new type of model world action models, or WAM.

### [07:32 - 07:37]

So let's all take a moment of silence for our dear friend, VOAs.

### [07:38 - 07:42]

They've served us well, rest in peace, long live world action models.

### [07:44 - 07:46]

And next, data strategy.

### [07:47 - 07:53]

This is NVIDIA's chief scientist, Bill Dahle, operating teleoperation inside our lab.

### [07:54 - 07:54]

And given his salary,

### [07:54 - 08:00]

I think this is by far the most expensive teleop trajectory ever collected in our data set.

### [08:02 - 08:05]

The past three years have been dominated by teleoperation.

### [08:06 - 08:08]

It's the golden era, right?

### [08:08 - 08:13]

VR headsets, extremely optimized latency for streaming,

### [08:13 - 08:17]

and these complex rigs that look like medieval torture devices.

### [08:17 - 08:21]

You know, so much investment in industry, so much pain and suffering.

### [08:22 - 08:23]

And yet, for teleop,

### [08:24 - 08:27]

it's upper bounded by 24 hours per robot per day,

### [08:27 - 08:29]

the fundamental physical limit.

### [08:29 - 08:30]

And actually, who am I kidding?

### [08:30 - 08:32]

It's more like three hours per robot per day,

### [08:32 - 08:34]

and only when the robot god is merciful.

### [08:35 - 08:37]

Because they throw tantrums all the time.

### [08:38 - 08:39]

So how can we do better?

### [08:40 - 08:41]

Well, how about this?

### [08:42 - 08:45]

You just wear the robot hand on your own hand.

### [08:46 - 08:49]

So this is called UMI, or Universal Manipulation Interface.

### [08:49 - 08:51]

And it's a deceptively simple idea.

### [08:52 - 08:53]

You wear the robot actuator on your own hand.

### [08:54 - 08:56]

And directly collect the data as humans,

### [08:57 - 09:00]

while getting the rest of the robot body out of the loop.

### [09:01 - 09:04]

Yet, I would say UMI is perhaps one of the greatest papers

### [09:04 - 09:06]

ever written in robotics data.

### [09:06 - 09:09]

And it spawned two unicorn startups.

### [09:09 - 09:12]

On the left-hand side is a journalist improving this design,

### [09:12 - 09:13]

so you can wear the gripper here.

### [09:14 - 09:15]

And on the right-hand side,

### [09:15 - 09:18]

Sunday made these three-finger data gloves.

### [09:19 - 09:21]

So last year, we took it one step further.

### [09:21 - 09:23]

We designed these exoskeleton,

### [09:24 - 09:25]

that has a one-to-one mapping,

### [09:25 - 09:27]

with five-finger dexterous robot hands.

### [09:27 - 09:28]

And we call it DEX-UMI.

### [09:29 - 09:30]

Let's look at it in action.

### [09:31 - 09:32]

On the left,

### [09:33 - 09:34]

the human directly collecting the data,

### [09:34 - 09:35]

always the fastest.

### [09:36 - 09:36]

On the right,

### [09:36 - 09:39]

look at how difficult teleop is, right?

### [09:39 - 09:40]

The human operator,

### [09:40 - 09:41]

here one of our most skilled PhDs,

### [09:42 - 09:45]

he has to align very carefully, right?

### [09:45 - 09:46]

And then it's super slow.

### [09:46 - 09:49]

Also, the success rate is very low as well.

### [09:50 - 09:51]

And in the middle,

### [09:51 - 09:52]

you just wear these exoskeleton,

### [09:52 - 09:53]

and you collect data,

### [09:53 - 09:54]

directly.

### [09:55 - 09:58]

And we train a robot policy on this data.

### [09:58 - 10:03]

So here what you see is a fully autonomous rollout of a policy,

### [10:03 - 10:05]

that's trained on zero teleoperation data.

### [10:07 - 10:11]

So we're able to break the curse of 24 hours per robot per day,

### [10:11 - 10:13]

and see how happy these robots are,

### [10:13 - 10:16]

because they no longer need to be in the loop for data collection.

### [10:17 - 10:18]

So is this the answer?

### [10:18 - 10:20]

Have we solved scaling for robotics?

### [10:22 - 10:23]

Anyone driving Tesla,

### [10:23 - 10:24]

or Waymo here?

### [10:24 - 10:24]

Anyone?

### [10:26 - 10:26]

You know,

### [10:26 - 10:27]

when you're driving,

### [10:28 - 10:32]

you're actually contributing to the biggest physical data flywheel.

### [10:34 - 10:34]

And the beauty is,

### [10:34 - 10:37]

you don't even feel it during FSD,

### [10:37 - 10:40]

because the data upload is an ambient process.

### [10:40 - 10:42]

Yet wearing these UMI or data wearables,

### [10:42 - 10:43]

it's still cumbersome,

### [10:43 - 10:44]

right?

### [10:44 - 10:44]

It's intrusive.

### [10:45 - 10:47]

It's not as seamless as just driving to work.

### [10:48 - 10:52]

So we need an FSD equivalent.

### [10:53 - 10:56]

The data collection needs to get out of the way,

### [10:56 - 10:57]

fade into the background,

### [10:58 - 11:01]

so we can capture the full glory of human dexterity

### [11:01 - 11:02]

across all walks of life,

### [11:03 - 11:05]

across all labors of economic value.

### [11:06 - 11:10]

So we're going all in on human egocentric videos

### [11:10 - 11:12]

that come with these detailed annotations,

### [11:12 - 11:14]

like hand position tracking,

### [11:14 - 11:16]

and dense language annotations.

### [11:18 - 11:19]

Introducing EgoScale,

### [11:20 - 11:23]

where 99.9% of the training,

### [11:23 - 11:24]

that goes into this,

### [11:24 - 11:26]

is based on human egocentric videos.

### [11:27 - 11:29]

And the result is an end-to-end policy

### [11:29 - 11:31]

that maps directly from the camera pixels here

### [11:32 - 11:34]

to 22 degrees of freedom,

### [11:34 - 11:36]

high dexterity robot hands.

### [11:36 - 11:38]

What you see here is fully autonomous.

### [11:40 - 11:46]

We pre-train EgoScale on 21K hours of in-the-wild egocentric human data

### [11:46 - 11:48]

with zero robot data whatsoever.

### [11:49 - 11:50]

And during pre-training,

### [11:50 - 11:52]

we predict these hand joints

### [11:52 - 11:53]

and wrist poses.

### [11:54 - 11:55]

Then in action fine-tuning,

### [11:55 - 11:57]

we collect only 50 hours

### [11:58 - 12:00]

of high-precision mocap data gobs

### [12:00 - 12:02]

and four hours of teleop.

### [12:02 - 12:04]

That's four hours of teleop,

### [12:05 - 12:08]

less than 0.1% of our training mix.

### [12:09 - 12:10]

And with this,

### [12:10 - 12:14]

EgoScale is able to generalize to these very dexterous tasks,

### [12:14 - 12:15]

like sorting card

### [12:16 - 12:17]

or manipulating syringe,

### [12:18 - 12:19]

right, over,

### [12:20 - 12:20]

transferring the liquid.

### [12:20 - 12:22]

You know, someday we might have robot nurses

### [12:22 - 12:23]

at home,

### [12:23 - 12:24]

might as well try this.

### [12:25 - 12:26]

And for these tasks,

### [12:27 - 12:29]

it takes only one-shot demonstration at test time

### [12:30 - 12:32]

to learn different shirt-folding strategies.

### [12:34 - 12:36]

And perhaps the most fascinating finding from the paper

### [12:37 - 12:40]

is that we discovered this neural scaling law

### [12:40 - 12:41]

for dexterity.

### [12:42 - 12:45]

It's a very clean relationship between

### [12:45 - 12:47]

the amount of hours we put into pre-training

### [12:47 - 12:49]

and the optimal validation loss.

### [12:49 - 12:50]

In fact,

### [12:50 - 12:51]

it's a clean,

### [12:51 - 12:51]

log,

### [12:51 - 12:52]

linear,

### [12:52 - 12:53]

mathematical equation.

### [12:54 - 12:57]

Six years after the original neural scaling law

### [12:57 - 12:58]

for language models.

### [12:59 - 13:02]

So if we put all of these data strategies on this chart,

### [13:02 - 13:05]

x-axis is alignment to the robot hardware,

### [13:05 - 13:07]

y-axis is scalability,

### [13:07 - 13:08]

this is what it looks like.

### [13:09 - 13:09]

Teleop,

### [13:10 - 13:12]

the least scalable data wearables,

### [13:12 - 13:14]

you can go up to hundreds of thousands of hours.

### [13:14 - 13:16]

And egocentric video,

### [13:16 - 13:18]

if we're able to spin the FSD flywheel,

### [13:19 - 13:21]

easily 10-minute hours in the next year or so.

### [13:22 - 13:24]

And if we draw a line here,

### [13:24 - 13:27]

everything to the left of this line is a new paradigm,

### [13:27 - 13:29]

sensorized human data.

### [13:30 - 13:31]

So let me make a few predictions.

### [13:32 - 13:33]

In the next year or two,

### [13:33 - 13:35]

we'll see Teleop dropping and dropping

### [13:35 - 13:37]

to almost negligible amount.

### [13:38 - 13:41]

And then there will be an ensemble of data wearables,

### [13:41 - 13:44]

custom designed for different hardware and use cases.

### [13:44 - 13:45]

And finally,

### [13:45 - 13:48]

the main diet for robotics will be egocentric videos.

### [13:49 - 13:51]

So a moment of silence,

### [13:52 - 13:53]

for our dear friend,

### [13:53 - 13:53]

Teleop.

### [13:54 - 13:55]

You have served us well,

### [13:55 - 13:56]

rest in peace,

### [13:56 - 13:57]

long live sensorized human data.

### [13:59 - 14:01]

Are we done with the data strategy yet?

### [14:01 - 14:04]

Did you notice I put two rings on data strategy?

### [14:04 - 14:06]

What's the outer ring here?

### [14:07 - 14:08]

All the LLM frontier labs

### [14:09 - 14:11]

have spent significant budget now

### [14:11 - 14:14]

on acquiring millions of coding environments

### [14:14 - 14:15]

to do reinforcement learning.

### [14:16 - 14:17]

So robotics is the same.

### [14:17 - 14:20]

We're in urgent need to scale up environments.

### [14:21 - 14:21]

And of course,

### [14:22 - 14:24]

you can always do reinforcement learning

### [14:24 - 14:25]

directly on the real robot.

### [14:26 - 14:26]

So in our lab,

### [14:27 - 14:29]

we use RL to push certain tasks

### [14:29 - 14:31]

to almost 100% success rate

### [14:32 - 14:34]

so you can do these continuous execution

### [14:34 - 14:35]

for hours on end.

### [14:35 - 14:36]

You know,

### [14:36 - 14:37]

it's kind of therapeutic to see these robots

### [14:37 - 14:39]

assembling GPUs just by themselves,

### [14:40 - 14:41]

or as a wise man will say,

### [14:41 - 14:42]

good boy,

### [14:42 - 14:44]

this task has been approved by my boss.

### [14:46 - 14:49]

Yet we can't get to 1 million environments

### [14:49 - 14:51]

because that will require 1 million robots

### [14:51 - 14:53]

if you do it the previous way.

### [14:53 - 14:54]

So we need a better way.

### [14:55 - 14:56]

Here,

### [14:56 - 14:58]

let's say you take an iPhone picture

### [14:59 - 15:00]

and you can pass this through

### [15:01 - 15:02]

this 3D world scan pipeline

### [15:03 - 15:04]

to extract all the objects

### [15:04 - 15:07]

and then automatically synthesize them again

### [15:08 - 15:10]

inside a classical physics simulator.

### [15:10 - 15:12]

So all these objects are actually interactive

### [15:12 - 15:13]

after the scan.

### [15:14 - 15:17]

And then you can augment this infinitely in simulation

### [15:17 - 15:18]

with variations

### [15:18 - 15:19]

that we call

### [15:19 - 15:20]

digital cousins.

### [15:22 - 15:24]

So now iPhone basically become

### [15:24 - 15:26]

a pocket world scanner

### [15:27 - 15:28]

in this process that we call

### [15:28 - 15:29]

real-to-sim-to-real.

### [15:30 - 15:30]

And in this way,

### [15:31 - 15:32]

we have a scalable way

### [15:32 - 15:34]

to port the physical world

### [15:34 - 15:35]

into the digital world.

### [15:36 - 15:37]

But still this method relies

### [15:37 - 15:39]

on a classical graphics engine.

### [15:40 - 15:40]

Can we do better?

### [15:41 - 15:43]

Introducing Dream Dojo.

### [15:45 - 15:46]

So it's always been on video world model

### [15:47 - 15:48]

and turning them into

### [15:48 - 15:50]

full-fledged neural simulators.

### [15:51 - 15:53]

Dream Dojo takes as input

### [15:53 - 15:55]

these continuous action signals

### [15:56 - 15:57]

and outputs the next RGB frames

### [15:57 - 15:59]

as well as sensor states in real time.

### [16:00 - 16:02]

Not a single pixel you see here is real.

### [16:04 - 16:05]

And Dream Dojo is able to capture

### [16:05 - 16:07]

and learn the mechanics of different robots

### [16:08 - 16:10]

through a purely data-driven approach.

### [16:10 - 16:12]

There is no physics equation,

### [16:12 - 16:13]

no graphics engine

### [16:13 - 16:14]

involving this process.

### [16:16 - 16:18]

So the new post-training paradigm

### [16:18 - 16:19]

designed for robotics

### [16:19 - 16:22]

is a massively parallel RO system

### [16:22 - 16:26]

that runs on a few real robot stations,

### [16:26 - 16:28]

a bunch of graphics cores running world scans,

### [16:28 - 16:30]

and heavy inference compute

### [16:30 - 16:32]

running world models.

### [16:33 - 16:34]

Or as this equation goes,

### [16:34 - 16:37]

compute now equals environment,

### [16:37 - 16:38]

now equals data.

### [16:39 - 16:40]

Or as a wise man would say,

### [16:41 - 16:42]

the more you buy, the more you save.

### [16:43 - 16:45]

And this message has been approved by my boss.

### [16:46 - 16:47]

So that's it.

### [16:47 - 16:48]

Putting it together,

### [16:48 - 16:51]

the great parallel that robotics will follow.

### [16:51 - 16:53]

And it's happening as we speak.

### [16:53 - 16:56]

And we're looking at the beginning of the end game.

### [16:58 - 17:00]

You guys play the video game Civilization?

### [17:01 - 17:02]

Still my favorite.

### [17:03 - 17:05]

I like to think of my research

### [17:05 - 17:07]

as unlocking game achievements

### [17:07 - 17:10]

on this civilizational technology tree.

### [17:11 - 17:13]

And there are three more achievements

### [17:13 - 17:14]

to unlock for robotics,

### [17:14 - 17:15]

and then we're done.

### [17:15 - 17:16]

We're done.

### [17:16 - 17:18]

I can retire, and I can't wait for that.

### [17:19 - 17:22]

The first is passing the physical Turing test.

### [17:23 - 17:26]

Across a wide range of activities,

### [17:26 - 17:28]

you cannot tell the difference

### [17:28 - 17:30]

between a human doing a task

### [17:30 - 17:31]

or a robot doing it.

### [17:31 - 17:34]

Maybe not drunk humans, but, you know.

### [17:35 - 17:37]

Physical Turing test is about

### [17:37 - 17:40]

unit energy in and unit labor out.

### [17:41 - 17:43]

And just by judging at the sexy pose of this robot,

### [17:43 - 17:45]

I think the worst thing about this robot

### [17:45 - 17:47]

I think the work is cut out for us.

### [17:47 - 17:50]

So maybe it's two to three years away.

### [17:50 - 17:53]

And next, physical API.

### [17:53 - 17:55]

You have a whole fleet of robots,

### [17:55 - 17:58]

and they can be configured just like any other software

### [17:58 - 18:00]

using APIs and command lines,

### [18:00 - 18:03]

orchestrated someday by Opus 9.0.

### [18:03 - 18:05]

And if we have this physical API,

### [18:05 - 18:08]

we'll be able to realize lights out factories.

### [18:08 - 18:11]

Those are essentially printers of atoms.

### [18:11 - 18:14]

They take as input design in Markdown files,

### [18:14 - 18:16]

and then output fully assembled products,

### [18:16 - 18:18]

completely autonomous.

### [18:18 - 18:20]

Or these wet labs

### [18:20 - 18:23]

that automate scientific discoveries

### [18:23 - 18:26]

in chemistry, biology, and medicine.

### [18:27 - 18:30]

And the final stop, physical auto research.

### [18:30 - 18:33]

When the robots start to design, improve,

### [18:33 - 18:36]

and build the next iteration of themselves

### [18:36 - 18:39]

far beyond what's humanly possible.

### [18:39 - 18:41]

So you might ask,

### [18:41 - 18:43]

is this too science fiction?

### [18:43 - 18:46]

Like, are we going to see this in our lifetime?

### [18:46 - 18:51]

Well, it took the AI community 14 years

### [18:51 - 18:55]

to go from the first forward pass of AlexNet in 2012,

### [18:55 - 18:58]

a model that barely recognized cat versus dog,

### [18:58 - 19:01]

to AI ascent today, 2026,

### [19:01 - 19:04]

where we talk about agentic auto research.

### [19:04 - 19:06]

And let's just add another 14 years.

### [19:06 - 19:08]

How about that?

### [19:08 - 19:12]

2026 is right in the middle of 2012 and 2014.

### [19:12 - 19:14]

And technology does not advance linearly.

### [19:14 - 19:16]

It advances exponentially.

### [19:16 - 19:19]

So I can say with 95% certainty

### [19:19 - 19:22]

that we'll get to the end of the end game,

### [19:22 - 19:26]

the end of the technology tree, by 2040.

### [19:26 - 19:28]

And we'll still be on.

### [19:28 - 19:30]

We'll still be on.

### [19:30 - 19:32]

If you believe in robotics,

### [19:32 - 19:34]

robotics will believe in you.

### [19:34 - 19:37]

And to all of us here, sitting here,

### [19:37 - 19:40]

I think this is the first step

### [19:40 - 19:45]

I think our generation was born too late

### [19:45 - 19:48]

to explore the Earth and too early to explore the stars,

### [19:48 - 19:52]

but we are born just in time to solve robotics.

### [19:52 - 19:54]

Thanks.
