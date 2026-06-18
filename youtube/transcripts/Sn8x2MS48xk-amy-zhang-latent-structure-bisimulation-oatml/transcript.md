# Amy Zhang Explores Generalization in RL by Exploiting Latent Structure and Bisimulation Metrics

- URL: https://www.youtube.com/watch?v=Sn8x2MS48xk
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T20:43:10`

## Transcript

### [00:00 - 00:30]

Yeah, I'm like, I'm annoyed at how much we rely on Zoom and how like, unintuitive the UI is. I've definitely, I had to learn a lot about Zoom because I was like, I was TAing for a class. So I was hosting office hours, and I was sharing my screen and I couldn't figure out how to like, go back to the chat to see like a link that one of them had sent. So I had to, like, I ended up just like, like kicking everyone out.

### [00:30 - 00:37]

I went out of the meeting so I could restart the stupid thing. So I could like, like, anyway, it was right. It was, it felt like a disaster.

### [00:38 - 00:48]

Yeah, yeah, I get it. And it's like that social pressure to that you're like, put on yourself that like, yeah, yeah, getting it done fast when you probably could just like relax and somehow.

### [00:48 - 00:58]

Yeah, yeah, yeah, no wonder you're like on the spot. It's like hard, also harder to like, like, be patient and think through things. And you're just like, I need to get this working.

### [00:58 - 00:59]

Exactly.

### [01:00 - 01:00]

Yeah.

### [01:01 - 01:17]

So we are super happy to have Amy Zhang here today to give a talk. Amy is currently in her final year of PhD at McGill University and the Mila, and she's co-supervised by Doina Prikap and Joelle Pinot.

### [01:19 - 01:28]

Prior to that, she was at MIT, where she did her, her, her, her master's in EECS.

### [01:29 - 01:48]

And a dual Bachelor of Science in EECS and Mathematics. She's currently working at Facebook AI Research. Her research interests are in reinforcement learning and generalization of reinforcement learning, focusing on sort of states-based, learning states-based abstractions and representations.

### [01:49 - 01:51]

Amy, welcome to OMEA.

### [01:51 - 01:56]

Thank you for the very nice introduction. Thank you all for being here.

### [01:56 - 01:58]

So today I'm going to be giving a talk.

### [01:58 - 02:02]

I'm going to be giving a talk on exploiting latent structure for better generalization.

### [02:03 - 02:07]

So in the last few years, Deep RL has had many successes.

### [02:08 - 02:19]

So, you know, there's been OpenAI StarCraft and Dota and DeepMind AlphaGo, and these are, have all been examples of, of these single games where we've been able to achieve better than human performance.

### [02:20 - 02:28]

Sort of like more on the research side in terms of benchmarks, we've also got Atari and we've been able to also get better than human performance in many of those games.

### [02:28 - 02:40]

On the flip side, there's also been many disappointing failures. And so on the left is, you know, have just like a pretty comical gif of like a robot from RoboCop failing to kick a ball.

### [02:41 - 02:46]

But again, sort of like more on the research side in the last few years, we've seen a few papers that basically

### [02:48 - 02:54]

kind of dive deeper into the kinds of failures that Deep RL algorithms are showing.

### [02:54 - 02:58]

And so here are just like a few examples and

### [02:58 - 03:04]

looking at Atari and Coin Run where these, in these papers, these authors have just changed.

### [03:05 - 03:15]

They basically created like a train test split. So in the typical RL setting, you know, we typically don't have like a separate train and evaluation that you do, like you do in supervised learning.

### [03:15 - 03:27]

You usually just have a single environment that you train and then evaluate it. And so in these papers, they've tried to create more of a split where you now have some differences in the observation space, like in this pixel space,

### [03:28 - 03:40]

where there are small pixel changes that don't affect the game, where a human, if it sees these pixel changes completely understands that it doesn't affect the underlying MDP and can play normally, but our RL agents completely fail.

### [03:41 - 03:51]

So why do we have this discrepancy? So as I've said, we've seen that Deep RL works really well in single task settings and simulation with millions of transitions.

### [03:52 - 03:57]

But we've seen that it works less well in visually complex and natural settings when you have rich observations, when you change some aspects of the data.

### [03:57 - 04:06]

And we're not seeing the same kind of generalization performance that we're getting in computer vision and NLP with deep learning.

### [04:07 - 04:22]

So the question that I want to ask is how can we achieve RL in the real world? And my hypothesis is that abstraction is the key to generalization. And I'm going to show how we can develop algorithms with theory-backed guarantees through the use of state abstractions.

### [04:23 - 04:27]

So this is just a quick overview of my contributions sort of throughout

### [04:27 - 04:34]

my PhD. So I initially started out with state abstractions, looking at state abstractions within the MDP formulation,

### [04:35 - 04:53]

learning representations geared towards transfer and planning and partial observability settings. From there, I kind of realized sort of like the limitations of deep RL algorithms and I took a deeper dive into looking at overfitting and generalization and continuous RL. And from there,

### [04:54 - 04:57]

developing like a very easy tweak

### [04:57 - 05:06]

to existing RL benchmarks in simulation that allow us to bring some of the natural visual complexity of the real world into simulation.

### [05:07 - 05:16]

And so then in the last couple of years I've been looking at state abstractions beyond the MDP formulation. So now focusing sort of like on this

### [05:17 - 05:26]

benchmark I proposed and sort of like how can we improve generalization of RL in more complex settings with like additional assumptions about the environment.

### [05:27 - 05:27]

So we're

### [05:27 - 05:42]

going to focus on sort of this last third of this work, and specifically I'm going to be talking about these two papers, learning invariant representations for RL without reconstruction and multitask RL as a hidden parameter MDP.

### [05:44 - 05:45]

So just to start, I'm going to

### [05:47 - 05:56]

go over again like what makes up the, what are the common assumptions in RL, right. So we typically assume that we are in a Markov decision process.

### [05:56 - 06:06]

We have a state space S, action space A, a transition probability distribution P, and a reward function R. And we also assume that these are all stationary, right.

### [06:07 - 06:13]

And so these assumptions are both incredibly broad and somewhat restrictive.

### [06:13 - 06:26]

And, and, you know, when we think about the real world, or it may be just some particular class of problems, there are often a lot of additional, there is often a lot of additional structure or just like information that we know.

### [06:26 - 06:42]

that isn't imparted in this, in this information, right. So the kind of question I'm really interested in is what kind of additional structure is reasonable to assume in MDPs. And if we assume this structure, can we get better generalization?

### [06:43 - 06:53]

So the focus of this talk, I'm going to look at a couple of additional assumptions that I think reflect sort of natural structure in the real world. And so the first is

### [06:53 - 07:10]

we're going to look at the block MDP setting, and then we'll look at hidden parameter MDPs, and I'll show how these additional assumptions allow for new theoretical results and better generalization performance compared to current state of the art deep RL methods.

### [07:11 - 07:19]

So, so with that, I'm just going to jump straight into the first paper, learning invariant representations for RL without reconstruction.

### [07:20 - 07:23]

And so in this paper, we're looking at a specific

### [07:24 - 07:34]

type of MDP that we're going to call block MDP. So a block MDP family can be described by, so you can see that these first four

### [07:34 - 07:43]

components are the same as in a typical MDP, but we're now going to add these two additional components. So the first is that we now have an observation space X

### [07:45 - 07:47]

and a rendering mapping Q

### [07:48 - 07:53]

that maps from our state space to our observation space. And the key assumption in a block MDP is

### [07:53 - 07:58]

that each observation X uniquely determines its generating state.

### [07:59 - 08:06]

And so the reason we call this a block MDP is that it basically is saying that if you think of your rendering mapping as a matrix,

### [08:07 - 08:21]

that matrix is going to be composed of disjoint blocks of of the mapping from from state to observation. So this gives us the Markov property and the observation space and is what separates this from the partial observability setting. So

### [08:21 - 08:27]

What you really want to take away from this definition is that you have a lower dimensional

### [08:27 - 08:35]

or more compact state space and what you're seeing is like a richer higher dimensional

### [08:35 - 08:41]

observation space like pixel space and there are many possible pixel observations that map

### [08:41 - 08:47]

to the same state and so we want to learn how to collapse all of those observations to that

### [08:47 - 08:51]

same underlying state so we can get generalization to unseen observations.

### [08:53 - 08:57]

This is through state abstractions and specifically a form of state abstraction

### [08:57 - 09:02]

called bisimulation. So bisimulation is is considered the strictest form of state

### [09:02 - 09:08]

abstraction because it basically describes an equivalence relation between states that

### [09:08 - 09:16]

that captures exact behavioral similarity in terms of the reward. So this is the formal definition

### [09:16 - 09:17]

for this equation.

### [09:17 - 09:27]

The first is that for any action in our action space the reward is the same for si and sj so if

### [09:27 - 09:33]

si and sj are equivalent under this bisimulation relation then this holds true and then we've also

### [09:33 - 09:41]

got this second requirement which makes this recursive. So this equation 2 is saying that

### [09:41 - 09:46]

our probability distribution our next step transition distribution is also the same for si

### [09:46 - 09:47]

and sj.

### [09:47 - 09:54]

For any action a but we're comparing these probability distributions in the abstract state

### [09:54 - 10:01]

in this abstract space these abstract states having been constructed using this equivalence

### [10:01 - 10:08]

relation. So these two components basically give us a state abstraction where two states are

### [10:08 - 10:15]

equivalent if conditioned on any possible action sequence you see the exact same reward sequence

### [10:15 - 10:16]

for these two states.

### [10:17 - 10:23]

But this is a very executive definition of this so I've been trying to think about

### [10:23 - 10:25]

how to do it and try to fit this into something that's the very point of this paper.

### [10:28 - 10:31]

And I'm yeah I'm happy to answer any questions if people are

### [10:33 - 10:36]

are not following or if you have any clarification questions.

### [10:39 - 10:45]

So what we wanted to do in this paper is learn a representation where l1 distance between any two

### [10:45 - 10:46]

states is a measure of their bisimilarity.

### [10:47 - 10:53]

because it's just clustering right it just tells us if two states are equivalent or not

### [10:53 - 10:59]

it doesn't tell us how far how similar two states are so instead we want to use instead

### [11:01 - 11:06]

this definition of a bisimulation metric and so this gives like a measure of similarity between

### [11:06 - 11:14]

states so it's just a relaxation of the previous definition into one where we now give a distance

### [11:14 - 11:22]

and so here it's demarked as d tilde and this distance between two states is going to be a

### [11:22 - 11:30]

measure of sort of the largest distance under any action of their reward and a Wasserstein distance

### [11:30 - 11:37]

of their next step transition distribution so now this tells us that if two states are not equivalent

### [11:38 - 11:42]

it tells us how similar they are so if two states are are not equivalent because they just have

### [11:42 - 11:43]

some

### [11:44 - 11:49]

like far into the future there is some action that sort of where they diverge where

### [11:49 - 11:54]

maybe their reward that you see is is slightly different this is going to give us information

### [11:54 - 12:00]

that those two states are closer than another pair of states where you know their reward

### [12:00 - 12:09]

diverges immediately in the next time step and so this lends itself to a representation learning

### [12:09 - 12:13]

objective so this is the objective that we proposed

### [12:14 - 12:18]

and so z here represents the representation that we're trying to construct

### [12:19 - 12:26]

and d here is the bisimulation metric so we can plug in the equation from the previous slide here

### [12:26 - 12:33]

and this now becomes our objective so you can see that we need this r hat and p hat for each

### [12:35 - 12:43]

each state here s i and s j and so we can't necessarily get that from the environment we can't

### [12:44 - 12:50]

you know we can't call up like every possible state and action pair so instead we have to

### [12:50 - 12:56]

learn a reward model and reward and latent transition model so that we can compute these

### [12:56 - 13:04]

two distances so this leads us to our algorithm deep by simulation for control so this this

### [13:04 - 13:08]

algorithm is has two parts the first is for learning this representation so we have to

### [13:08 - 13:12]

learn our reward model our latent transition model and we also

### [13:14 - 13:17]

and we train these two components on top of our frozen encoder

### [13:20 - 13:27]

and then our encoder is trained with our objective from the previous slide j and

### [13:28 - 13:32]

once all of those are updated then we can train our policy so now

### [13:32 - 13:37]

our representation is frozen again we don't need to use our dynamics and reward model and here we

### [13:37 - 13:43]

just chose to use soft doctor critic but this works with any rl optimization algorithm so now

### [13:44 - 13:48]

soft actor critic is just just sees the representation that we're learning this

### [13:48 - 13:52]

uh by simulation abstraction instead of the original rich observation space

### [13:54 - 14:00]

and uh so the way that we train this is you know we collect data with a random agent first so we

### [14:00 - 14:06]

can populate our replay buffer we select a random batch from the replay buffer we make a copy permute

### [14:06 - 14:12]

that copy so in order to train algorithm one so that we can get random pairs of states to compare

### [14:12 - 14:13]

for the encoder

### [14:14 - 14:18]

uh and so in that sense it's it's kind of similar to a contrastive loss

### [14:18 - 14:23]

and then we can use that same batch of data and then just update with the soft actor critic

### [14:23 - 14:32]

objectives um so in order to test this we we want to sort of we we want to evaluate

### [14:32 - 14:39]

how well this can do in different like visually complex um environments right

### [14:39 - 14:43]

and so based on that block mdp formulation we know that we want to test this using different

### [14:44 - 14:48]

rich observations that map to the same low dimensional state

### [14:48 - 14:51]

so here we just have some environments from deep mind control

### [14:53 - 15:00]

and on top we see the original environments um the original pixel environments the rendered ones

### [15:00 - 15:06]

and we've also introduced two additional levels of complexity so in the second one we have this

### [15:06 - 15:12]

um these balls just dancing in the background this like ideal gas uh and then in the in the sort of

### [15:12 - 15:18]

final most complex setting we actually take youtube videos from the deep mind kinetics data

### [15:18 - 15:22]

set and pipe that in as background and this is really easy to do because you can just use like

### [15:22 - 15:27]

simple image processing methods like what we did here is because the agent um you know it's like

### [15:27 - 15:32]

more of this tan color and the background is actually all sort of more blue you can just take

### [15:32 - 15:39]

the rgb like filter out the background and and pipe in this video instead um and so there's a

### [15:39 - 15:45]

wrapper uh available for this environment so you can sort of pipe in any video or image that you

### [15:45 - 15:51]

want to recreate this and so we compare against some state-of-the-art methods like deep mdp and

### [15:51 - 15:57]

stochastic latent actor critic as well as showing how well this performs compared to reconstruction

### [15:57 - 16:01]

and uh contrastive loss um for training the representation so we can see that

### [16:03 - 16:09]

um in the so the the top the different rows just correspond to each other but we can see that in

### [16:09 - 16:09]

the in the in the in the in the in the in the in the in the in the in the in the in the in the in the

### [16:09 - 16:14]

in the simplest setting um these uh state-of-the-art methods perform really well but as

### [16:15 - 16:23]

we increase the complexity of the rich observation space those methods start to crash whereas our

### [16:23 - 16:28]

method is able to achieve sort of the same performance across across all environments

### [16:30 - 16:34]

and just to take a deeper dive into like the properties of the representation that we learn

### [16:34 - 16:39]

so here we just show a t-sne of the representation that we learn on the left and

### [16:39 - 16:47]

uh representation from a trained vae on the same data and we can see that if we just sample um

### [16:47 - 16:52]

observations or you know data points from this representation that are near each other

### [16:52 - 16:58]

that we get uh we see that it basically just captures information about the agent position

### [16:58 - 17:03]

so we can see that every every pair of observations that are close to each other close to

### [17:03 - 17:08]

each other in this representation space like have the same configuration of the agent but the pixel

### [17:08 - 17:15]

background is completely different so the pixel distance between these observations is can is can

### [17:15 - 17:21]

be very far apart um because the agent only takes up a small percentage of the image but the agent

### [17:21 - 17:27]

itself looks pretty much the same across all of these and so this is just sort of like another

### [17:27 - 17:33]

visual test that what our representation is capturing is just the agent state and not the

### [17:33 - 17:37]

background um and in comparison with the vae so you know the vae

### [17:38 - 17:45]

uses a pixel wise reconstruction loss and so it has to capture all information in the image

### [17:45 - 17:51]

relevant and irrelevant and so we can see that those same images are mapping to very different

### [17:51 - 18:00]

parts of the of the t-sne representation constructed by the vae um so now i'm gonna

### [18:00 - 18:08]

proceed to some some theoretical results um and so uh one of the things is that the

### [18:08 - 18:14]

vae simulation state abstraction has connections to causal feature sets in in causal inference

### [18:15 - 18:21]

um and so what this theorem is saying is if we partition observations using using by simulation

### [18:22 - 18:28]

those clusters correspond to the causal feature set of the observation space with respect to current

### [18:28 - 18:36]

and future reward and what um what this result is really is really giving us is uh an expected

### [18:36 - 18:37]

form of task generalization

### [18:38 - 18:44]

so because we now know that what the what information the state abstraction is capturing

### [18:44 - 18:51]

is sort of like all of the causal ancestors of the reward um then we know that this representation can

### [18:51 - 18:58]

transfer to new tasks where the new task has a reward function that's constructed from the same

### [18:58 - 19:08]

causal ancestors um uh okay so so so these are sorry these are actually two different results so

### [19:08 - 19:14]

the first theorem tells us that we should be able to generalize to new observations that we haven't

### [19:14 - 19:22]

seen before and the second theorem tells us that we should be able to generalize to a specific class

### [19:22 - 19:28]

of reward functions so if we look at empirical results that sort of test these two results

### [19:29 - 19:36]

first we look at generalization to new observations so we only train we train dbc in this first setting

### [19:36 - 19:38]

the ideal gas

### [19:38 - 19:44]

elephant curve and then we freeze that representation and train a new soft doctor critic

### [19:44 - 19:51]

on this new rich observation space with the kinetics dataset and so here we can see some

### [19:51 - 20:00]

comparisons um is so in blue is the transfer that i just detailed where we had the frozen

### [20:00 - 20:04]

representation and and trained a new soft actor critic with the new rich observation space

### [20:05 - 20:08]

and we see that that performs as well as or you

### [20:08 - 20:11]

even a little bit better than DBC trained from scratch

### [20:11 - 20:13]

just on the kinetics dataset.

### [20:14 - 20:15]

And so this kind of tells us

### [20:15 - 20:17]

that it's actually a little bit easier

### [20:17 - 20:20]

to extract the correct representation

### [20:20 - 20:23]

for soft actor critic to perform well

### [20:23 - 20:26]

in this simpler rich observation setting

### [20:26 - 20:30]

compared to training from scratch on this kinetics one.

### [20:30 - 20:32]

And we also just compare against deep MDP

### [20:32 - 20:34]

also performing the same kind of transfer

### [20:34 - 20:37]

and we don't see the same performance.

### [20:37 - 20:38]

So the representation that it learns

### [20:38 - 20:40]

isn't as geared towards

### [20:40 - 20:42]

this kind of zero-shot generalization.

### [20:45 - 20:48]

So here we sort of validate that second result

### [20:48 - 20:51]

of generalization to new reward functions.

### [20:51 - 20:54]

So here we have DBC trained on walk or walk

### [20:54 - 20:58]

and we kind of know that the sort of components

### [20:58 - 21:01]

of the state space necessary to construct

### [21:01 - 21:02]

the reward function for walk or walk

### [21:02 - 21:05]

is gonna be the same as the ones to construct it

### [21:05 - 21:06]

for walk or stand

### [21:06 - 21:07]

and walk or walk.

### [21:07 - 21:08]

Or walk or run.

### [21:08 - 21:12]

So we just, so in orange is the thing that we're testing

### [21:12 - 21:14]

which is that we can train SAC

### [21:14 - 21:16]

on the frozen representation for walk or walk

### [21:16 - 21:20]

and that it'll perform well for stand and run.

### [21:20 - 21:23]

And we compare that with soft actor critic

### [21:23 - 21:25]

just trained on the pixel space

### [21:25 - 21:29]

for these two tasks trained from scratch

### [21:29 - 21:31]

as well as soft actor critic trained

### [21:31 - 21:33]

with the frozen deep MDP representation.

### [21:33 - 21:36]

And we again see that the representation that we learn,

### [21:36 - 21:40]

sort of is more amenable to this kind of generalization

### [21:40 - 21:41]

compared to other methods.

### [21:43 - 21:46]

So I'm just gonna really quickly also go through

### [21:46 - 21:48]

some additional results in this paper.

### [21:48 - 21:52]

So we also tried, we also ran our method on CARLA

### [21:52 - 21:54]

which is an autonomous driving simulation engine.

### [21:55 - 21:58]

And so here we just construct this task

### [21:58 - 22:03]

where the task for the vehicle is just in terms

### [22:03 - 22:04]

of highway progression and meters.

### [22:04 - 22:05]

And you get a penalty for colliding with, you know,

### [22:05 - 22:05]

the speed of the vehicle.

### [22:05 - 22:06]

And you get a penalty for colliding with the speed of the vehicle.

### [22:06 - 22:10]

And you get a penalty for colliding with other cars

### [22:10 - 22:13]

or other parts of the environment.

### [22:13 - 22:14]

You wanna go as fast as possible

### [22:14 - 22:16]

and brake as little as possible.

### [22:16 - 22:19]

So here again, we compare against the same baselines

### [22:19 - 22:20]

as in the D-MINT control setting.

### [22:20 - 22:25]

And we see that our method performs best.

### [22:26 - 22:27]

But I think what's really exciting here is again,

### [22:27 - 22:30]

this same, like we do the same t- SNY representation,

### [22:30 - 22:32]

t-SNY of our learned representation.

### [22:32 - 22:33]

And you can see that parts that are close

### [22:33 - 22:33]

to the- The meters that are near by now are totally transparent.

### [22:33 - 22:35]

So there's more of a separation in terms of detail.

### [22:35 - 22:36]

So sometimes the mostly decided healing starts

### [22:36 - 22:36]

exists in the same way.

### [22:36 - 22:42]

close in this representation space, like up here we have all of these representations

### [22:42 - 22:49]

that correspond to different objects, like different obstacles on the right-hand side.

### [22:49 - 22:54]

So the only thing that matters is that there's something blocking the agent on the right-hand

### [22:54 - 23:00]

side so it can't switch lanes into the right, but it doesn't matter what the object is.

### [23:00 - 23:07]

So that loss of that irrelevant information is shown here in this representation, which

### [23:07 - 23:11]

I think is really nice.

### [23:11 - 23:14]

So I just have some additional nice videos.

### [23:14 - 23:19]

So the one on the left is also just showing real-time what the latent encoding is for

### [23:19 - 23:22]

these three different settings, sunny, cloudy, and sunset.

### [23:22 - 23:28]

So these are the exact same policy, exact same low-dimensional state in terms of the

### [23:28 - 23:29]

location of the agent.

### [23:29 - 23:30]

It's just...

### [23:30 - 23:33]

Different weather conditions.

### [23:33 - 23:39]

So it's just different rich observation renderings of the same sequence of states.

### [23:39 - 23:44]

And we can see that the representation is able to capture that pretty well, that like

### [23:44 - 23:48]

all three of these states all stay together pretty much.

### [23:48 - 23:56]

And on the right-hand side, we just have a video of our agent just driving on the highway.

### [23:56 - 23:59]

So to conclude, our goal here was to learn lossy representations.

### [23:59 - 24:01]

That only capture relevant information.

### [24:01 - 24:11]

And this was also sort of in response to a lot of recent papers that had shown successfully

### [24:11 - 24:15]

that deep RL works with rich observations if you use a reconstruction loss.

### [24:15 - 24:19]

And the reason that reconstruction loss works so well is because it's a dense...

### [24:19 - 24:20]

It's like dense signal, right?

### [24:20 - 24:25]

Like you have a pixel-wise loss, and it's really easy to learn good features with convolutional

### [24:25 - 24:26]

layers with that.

### [24:26 - 24:28]

But the downside is that you're forcing your...

### [24:28 - 24:29]

I don't know.

### [24:29 - 24:33]

You're forcing your compressed representation to contain all of the information in that

### [24:33 - 24:34]

pixel space.

### [24:34 - 24:40]

And so we wanted to show that you can get better performance by learning a lossy representation

### [24:40 - 24:44]

that only captures what you really need to know, which is the reward function and future

### [24:44 - 24:46]

reward.

### [24:46 - 24:52]

And so we do this by learning a representation where L1 distance is the bisimilarity...

### [24:52 - 24:54]

Captures the bisimilarity between states.

### [24:54 - 24:58]

And we showed that policy optimization on this representation improves generalization.

### [24:59 - 25:07]

And more recently, we also just put out a paper that showed that this works when we apply

### [25:07 - 25:10]

it to the sim2real setting.

### [25:10 - 25:15]

And so we were able to show that DBC and an additional invariance-inducing objective can

### [25:15 - 25:21]

successfully perform zero-shot sim2real transfer through the right intervention design via

### [25:21 - 25:26]

data augmentation and domain randomization.

### [25:26 - 25:27]

Okay.

### [25:27 - 25:28]

So...

### [25:28 - 25:29]

Okay.

### [25:29 - 25:35]

There is a question.

### [25:35 - 25:36]

I have a general question.

### [25:36 - 25:38]

Could you decouple these issues?

### [25:38 - 25:43]

First figure out the observation problem independent of the dynamics and control issues, then just

### [25:43 - 25:44]

do RL.

### [25:44 - 25:48]

That's a really good question.

### [25:48 - 25:53]

So at least for the DBC paper and what we did here for sim2real, we did decouple these

### [25:53 - 25:56]

issues.

### [25:56 - 25:58]

If I'm understanding your question correctly.

### [25:58 - 25:59]

Okay.

### [25:59 - 26:01]

So we're not looking at changes in dynamics.

### [26:01 - 26:04]

That's actually what I'm about to talk about next.

### [26:04 - 26:10]

In these two papers, we are only looking at generalization to new observations.

### [26:10 - 26:13]

We're assuming that everything about the underlying MDP is the same.

### [26:13 - 26:15]

We're assuming a single task setting.

### [26:15 - 26:22]

It's just that the rendering from state to observation can change.

### [26:22 - 26:28]

And then we just do RL on top of that representation once we've solved that new observation problem.

### [26:28 - 26:33]

So I hope that answers your question.

### [26:33 - 26:34]

Another question.

### [26:34 - 26:38]

So any opinions on using a beta VAE and then a bottleneck?

### [26:38 - 26:45]

Could that help with getting a more separated state space and removing unnecessary information?

### [26:45 - 26:46]

Probably yeah.

### [26:46 - 26:51]

So I know that there has been work on information bottleneck and using beta VAE in order to

### [26:51 - 26:55]

learn a compressed representation that encourages it to sort of drop irrelevant information.

### [26:55 - 26:58]

My problem with that approach is that...

### [26:58 - 27:00]

That's something that you have to tune, right?

### [27:00 - 27:07]

Like you kind of have to tune this, the beta parameter of how much information is getting

### [27:07 - 27:10]

stored in the latent representation.

### [27:10 - 27:14]

And you have no way of knowing that what it's storing, that it's not losing crucial information

### [27:14 - 27:17]

for the downstream task.

### [27:17 - 27:24]

The nice thing about by simulation is that it is going to try to...

### [27:24 - 27:27]

So if you get zero training error.

### [27:27 - 27:28]

You know that.

### [27:28 - 27:32]

You learned it by simulation and it has exactly the information that you need to learn a task

### [27:32 - 27:36]

and nothing else.

### [27:36 - 27:42]

And we can actually get really nice theoretical results based on this because we can measure

### [27:42 - 27:46]

that learning error of our by simulation, like our reward and transition model error

### [27:46 - 27:52]

and use that to compute value bounds for the downstream policy.

### [27:52 - 27:57]

And I kind of didn't...

### [27:57 - 28:00]

I think we have those results in this paper, but we definitely have those results like

### [28:00 - 28:02]

in the next paper that I'm going to talk about.

### [28:02 - 28:07]

So I'll kind of, I'll try to show you like what we can do with state abstractions that,

### [28:07 - 28:14]

and you can't get those kinds of nice results with using beta VAE use in information bottlenecks.

### [28:14 - 28:16]

Okay.

### [28:16 - 28:22]

So in the next paper, we move beyond just looking at rich observation generalization

### [28:22 - 28:25]

to now also looking at generalization of the dynamics.

### [28:25 - 28:26]

And so this is just looking at rich observation generalization to now also looking at generalization

### [28:26 - 28:27]

of the dynamics.

### [28:27 - 28:33]

So in this paper, multitask reinforcement learning as a hidden parameter block MDP.

### [28:33 - 28:37]

So now we're looking at this additional assumption, right?

### [28:37 - 28:44]

So now we have this hidden parameter block MDP family, which is defined again by the

### [28:44 - 28:48]

same state action space reward function discount factor.

### [28:48 - 28:53]

We keep the components from the block MDP, the observation space and rendering mapping

### [28:53 - 28:56]

and the same block assumption.

### [28:56 - 28:59]

But we now have introduced some additional components.

### [28:59 - 29:06]

So now we assume that we have a hidden parameter space data, and now our dynamics are conditioned

### [29:06 - 29:08]

on that hidden parameter.

### [29:08 - 29:14]

And we have a probability stationary probability distribution over the hidden parameter.

### [29:14 - 29:20]

And so now we're looking at the multitask setting where dynamics changes across tasks.

### [29:20 - 29:26]

So previous multitask approaches, multitask RL approaches basically use this like shared

### [29:26 - 29:29]

representation to transfer information across tasks.

### [29:29 - 29:35]

And the idea is that if you have information in your representation from a previous task

### [29:35 - 29:41]

that is going to help you in a current task, then the you'll just automatically get that

### [29:41 - 29:44]

sort of positive transfer by using the same representation.

### [29:44 - 29:51]

And hopefully, if if there you won't get negative transfer.

### [29:51 - 29:55]

And so we're making some additional assumptions.

### [29:55 - 30:02]

So let's talk about the structure across these tasks by now assuming that that all of the

### [30:02 - 30:07]

dynamics across all of these tasks can be described by a single universal dynamics model

### [30:07 - 30:09]

T.

### [30:09 - 30:14]

It's just that T is now parameterized by theta and theta is the thing that changes across

### [30:14 - 30:16]

all of these tasks.

### [30:16 - 30:21]

So we're going to use the same sort of like state abstraction approach with that same

### [30:21 - 30:23]

objective from the DBC paper.

### [30:23 - 30:25]

But now we have to apply it.

### [30:25 - 30:27]

In two places, right?

### [30:27 - 30:35]

So now, because we're still in the rich observation setting to we still need to map from observation

### [30:35 - 30:39]

space to state space, like with the same objective that we had before.

### [30:39 - 30:44]

But we now also have to do the same thing on a task ID level.

### [30:44 - 30:48]

So we assume that we are given environment IDs.

### [30:48 - 30:52]

And so these are just going to be like one hot vectors.

### [30:52 - 30:55]

And we want to use that same by.

### [30:55 - 30:58]

Similarity definition.

### [30:58 - 31:04]

But now, instead of comparing states, we're going to compare tasks.

### [31:04 - 31:07]

And so that is captured by this theta learning error.

### [31:07 - 31:11]

So you can see that it looks really similar to the objective from DBC.

### [31:11 - 31:18]

But now now this is like a this is a task in the coder instead of our state encoder.

### [31:18 - 31:24]

And we are now comparing it to a Wasserstein between the transition models of two tasks.

### [31:24 - 31:25]

Okay.

### [31:25 - 31:33]

So this is going to be looking at the worst case transition distance between two tasks.

### [31:33 - 31:36]

So it'll basically look at the entire state space.

### [31:36 - 31:44]

And the measure of how far apart these tasks are is sort of like the worst case of which

### [31:44 - 31:48]

which equivalent states in these two tasks have the furthest distance Wasserstein distance

### [31:48 - 31:54]

in terms of their in terms of their dynamics.

### [31:54 - 31:55]

And so this.

### [31:55 - 31:58]

This allows us to do some nice theoretical analysis.

### [31:58 - 32:03]

And so first, in order to look at the next results, we're going to define some error

### [32:03 - 32:04]

terms.

### [32:04 - 32:08]

We are in effect learning and approximate by simulation abstraction.

### [32:08 - 32:11]

And so we can define these separate error terms for that.

### [32:11 - 32:15]

So we've got epsilon R, which just measures like there are worst case error in terms of

### [32:15 - 32:20]

reward for any to any two states.

### [32:20 - 32:21]

Epsilon T.

### [32:21 - 32:22]

Epsilon T.

### [32:22 - 32:23]

Epsilon T.

### [32:23 - 32:25]

Epsilon T.

### [32:25 - 32:34]

Which measures our error, which also measures our error, but now in terms of the latent transition model, and Epsilon Theta, which measures our error in inferring this Theta value.

### [32:34 - 32:40]

So highlighted in blue are just like the first two terms.

### [32:40 - 32:50]

So these ones are the same ones as we could have used in the DBC paper, where this just describes a new MDP, which is close to the original for a specific task, right.

### [32:50 - 32:52]

So these apply to the single test setting.

### [32:52 - 32:53]

But this.

### [32:53 - 32:54]

Third, error term.

### [32:54 - 32:58]

which looks at theta is now just a per task error.

### [33:00 - 33:04]

So the first thing that we can analyze is a value bound

### [33:04 - 33:06]

for the single task setting.

### [33:06 - 33:11]

So now that we've constructed this approximate by simulation

### [33:11 - 33:15]

both of the state space and of our task embedding theta

### [33:15 - 33:17]

we can build an approximate MDP.

### [33:17 - 33:19]

And so we're gonna just call this M bar

### [33:20 - 33:24]

which is on top of this representation that we've learned.

### [33:24 - 33:29]

And so if we learn an optimal policy in this constructed MDP

### [33:33 - 33:37]

we wanna know how far away from optimal it is

### [33:37 - 33:40]

if we were to apply that policy in our original MDP

### [33:42 - 33:43]

just for a single task.

### [33:43 - 33:48]

And so it turns out that we can bound that distance

### [33:49 - 33:53]

of the true optimal MDP and the one that we've learned

### [33:53 - 33:54]

in our constructed MDP.

### [33:54 - 33:59]

By the error terms introduced in the last slide

### [33:59 - 34:02]

and as well as the maximum reward.

### [34:02 - 34:06]

And it also depends on like your discount factor gamma.

### [34:07 - 34:12]

But what this means is like these errors can be reduced

### [34:13 - 34:14]

through just supervised learning, right?

### [34:14 - 34:18]

Like the objective that we have for learning this

### [34:18 - 34:20]

by simulation abstraction is just

### [34:20 - 34:21]

like a supervised learning task.

### [34:21 - 34:24]

And so if we reduce these, the more we can reduce

### [34:24 - 34:28]

these, the closer we get to the optimal policy

### [34:28 - 34:29]

for the original MDP.

### [34:33 - 34:35]

Okay.

### [34:35 - 34:38]

So next, the thing that we wanna look at is, okay

### [34:38 - 34:39]

we're in a multitask setting.

### [34:39 - 34:41]

Now we wanna look at transfer bounds.

### [34:41 - 34:44]

Given that we have a policy learned for one task

### [34:44 - 34:49]

we wanna know how would that policy perform on a new task

### [34:49 - 34:52]

if we know the difference in dynamics where like

### [34:52 - 34:54]

we've inferred this theta I for the, you know, the, you know,

### [34:54 - 34:57]

the original task and theta J for the new task.

### [35:00 - 35:02]

So what this is now measuring is, okay,

### [35:02 - 35:06]

now we have constructed, we'd constructed an approximate

### [35:07 - 35:08]

abstraction for the original task.

### [35:08 - 35:10]

We trained a policy for that task.

### [35:10 - 35:12]

How far away is that going to be?

### [35:15 - 35:16]

Let's see.

### [35:16 - 35:19]

Yes, how far away is that going to be from the optimal?

### [35:19 - 35:24]

If we just take that policy and apply it to task J,

### [35:24 - 35:28]

MDP J, how far away is that gonna be

### [35:28 - 35:31]

from the optimal policy for J?

### [35:31 - 35:34]

And so this bound looks very similar to the previous one.

### [35:34 - 35:37]

It now actually just incorporates this distance in theta.

### [35:37 - 35:40]

So this is also a very intuitive result that just says

### [35:42 - 35:45]

your policy is gonna work well for a new task

### [35:45 - 35:48]

if that new task is similar to your original.

### [35:48 - 35:52]

And we've defined a way of like measuring that similarity

### [35:52 - 35:54]

across tasks as this distance in theta.

### [35:54 - 35:55]

Okay.

### [35:59 - 36:03]

We can also extend existing sample complexity analyses

### [36:03 - 36:05]

from the single task setting

### [36:05 - 36:09]

and from learning approximate by simulations

### [36:09 - 36:10]

to this multitask setting.

### [36:11 - 36:16]

So this is again, going back to the sort of like looking

### [36:17 - 36:22]

at just a single task, but here,

### [36:22 - 36:24]

so this looks very similar, I think,

### [36:24 - 36:28]

to like the original sample complexity analysis results

### [36:28 - 36:31]

that you can get just for a generic MDP.

### [36:31 - 36:33]

But the main difference that I wanna point out

### [36:33 - 36:36]

is that these two terms, this ND,

### [36:36 - 36:39]

so this is the minimum number of samples

### [36:39 - 36:41]

that you have for a single state.

### [36:42 - 36:47]

And this is in the original sort of result

### [36:48 - 36:49]

for sample complexity analysis.

### [36:49 - 36:52]

Like you have the size of your state space

### [36:52 - 36:53]

and the size of your action space.

### [36:53 - 36:56]

So we've now been able to reduce this

### [36:58 - 37:00]

a more compact state space

### [37:00 - 37:03]

or like courses by simulation partition.

### [37:03 - 37:06]

So now this number will get bigger

### [37:06 - 37:10]

because we have samples from different rich observations

### [37:10 - 37:11]

that actually map to the same state.

### [37:11 - 37:13]

And this number gets smaller

### [37:13 - 37:18]

because our original observation space is much larger

### [37:18 - 37:21]

in terms of cardinality than the constructed

### [37:21 - 37:23]

by simulation partition that we're making.

### [37:23 - 37:28]

Which just means that our sample complexity goes down.

### [37:28 - 37:30]

So because we know this structure exists

### [37:30 - 37:33]

in this class of MDPs,

### [37:33 - 37:37]

we can improve sort of the sample complexity results.

### [37:38 - 37:40]

And the nice thing also is that we can now actually apply

### [37:40 - 37:43]

this sample complexity result to the multitask setting

### [37:43 - 37:46]

where previous sample complexity analysis

### [37:46 - 37:47]

for the multitask setting depends

### [37:47 - 37:50]

on the number of tasks that you have.

### [37:50 - 37:52]

Here, it actually only depends on the number of actions.

### [37:52 - 37:53]

Here, it actually only depends on the number of actions.

### [37:53 - 37:53]

Here, it actually only depends on the number of actions.

### [37:53 - 37:56]

So we have aggregate samples across tasks

### [37:56 - 37:59]

because we are assuming that all of these tasks

### [37:59 - 38:01]

can be described by a single MDP.

### [38:02 - 38:04]

So these are sort of some nice improvements

### [38:04 - 38:05]

in terms of theory.

### [38:07 - 38:10]

All right, so now we can move on to the empirical results

### [38:10 - 38:12]

in this multitask setting.

### [38:12 - 38:15]

So we just, again, took the DeepMind control suite

### [38:15 - 38:18]

and we modified some of the tasks

### [38:18 - 38:20]

to create these changes in dynamics.

### [38:20 - 38:22]

So these are just some examples.

### [38:23 - 38:28]

So here, like the half cheetah, the length of the torso,

### [38:28 - 38:31]

we sort of increase and that'll affect the dynamics.

### [38:31 - 38:35]

And in the bottom one, it's supposed to be the left foot

### [38:35 - 38:36]

of Walker gets bigger.

### [38:36 - 38:38]

It's a little bit hard to tell.

### [38:38 - 38:40]

We have additional environments as well,

### [38:40 - 38:42]

where we just change like the friction coefficient

### [38:42 - 38:47]

or the mass of some component of the agent's body.

### [38:48 - 38:53]

But I wanna emphasize that the changes in dynamics don't have

### [38:53 - 38:58]

to be visually apparent and it doesn't need to be

### [38:58 - 39:00]

because we give it a task ID, right?

### [39:00 - 39:04]

So you can infer what task you're in just from that ID.

### [39:05 - 39:10]

So we compare again to a bunch of state-of-the-art

### [39:10 - 39:12]

multitask methods, including Distrl,

### [39:12 - 39:17]

which Distrl learns like a sort of central policy,

### [39:18 - 39:21]

like a policy that captures all of the shared information

### [39:21 - 39:22]

across tasks.

### [39:23 - 39:27]

This GradNorm and PCGrad, which use like shared gradients

### [39:27 - 39:30]

in order to sort of share information across tasks.

### [39:30 - 39:33]

We also compare with DeepMDP,

### [39:35 - 39:38]

which is just a single test method that we adapted

### [39:38 - 39:42]

to the multitask setting with just by using

### [39:42 - 39:46]

the task embeddings or incorporating task ID.

### [39:47 - 39:50]

And then we also performed an embellition

### [39:50 - 39:53]

where we took our method and we removed,

### [39:53 - 39:57]

we removed that criteria that in Theta space,

### [39:57 - 40:00]

the L1 distance in Theta space has to correspond

### [40:00 - 40:02]

to the by similarity.

### [40:02 - 40:06]

And we just wanted to see like how much difference

### [40:06 - 40:09]

sort of that objective made.

### [40:10 - 40:13]

And so we can see in these four environments

### [40:13 - 40:16]

that we've created that our method that uses this

### [40:16 - 40:21]

by similarity and task space and state space performs best

### [40:21 - 40:23]

and that there is a gap.

### [40:23 - 40:26]

When we evaluate that embellition.

### [40:30 - 40:33]

We also evaluated our,

### [40:33 - 40:35]

so our method can also be applied to meta RL.

### [40:35 - 40:39]

And so here we just took Pearl and removed like their method

### [40:39 - 40:42]

for finding a task embedding and replaced it with ours.

### [40:42 - 40:45]

And we can see some marginal gains.

### [40:45 - 40:46]

We see smaller gains here, I think,

### [40:46 - 40:49]

because in the previous example, it's zero,

### [40:49 - 40:52]

in the multitask RL setting, it's zero shot transfer

### [40:52 - 40:55]

to new dynamics and here it's adaptation right.

### [40:55 - 40:56]

Because we're in the meta RL setting.

### [40:56 - 41:00]

So here the agent does get a chance to adapt

### [41:00 - 41:04]

with some samples from the new tests that it sees.

### [41:04 - 41:09]

And so we see like some faster learning with Hippy MDP,

### [41:10 - 41:12]

but the difference is smaller.

### [41:13 - 41:16]

We also just evaluate our model error.

### [41:16 - 41:19]

So, because we're training this universal dynamics model

### [41:19 - 41:21]

and the only thing that we need to anfer is Theta

### [41:21 - 41:22]

and plug in Theta.

### [41:22 - 41:29]

to our dynamics um we can evaluate how uh how quickly our our dynamics model can adapt and so

### [41:29 - 41:33]

we just compare our method again against that ablation where we don't have that

### [41:33 - 41:37]

by similarity objective and we can see that our method just adapts way way faster

### [41:39 - 41:42]

another question that we got about our paper was

### [41:44 - 41:47]

a lot of people think that the block mdp assumption is very strict

### [41:47 - 41:54]

um that you have to assume full observability like in your observation space and so we also

### [41:54 - 42:00]

ran an experiment here where we introduced partial observa partial observability where

### [42:00 - 42:06]

you're basically losing information um in your observation space and so what we do here is

### [42:06 - 42:11]

um p gives the probability that the current observation that you see is actually your

### [42:11 - 42:17]

previous observation instead of the current one um and so now we're in a pomdp cycle

### [42:17 - 42:24]

setting and we can see that our method does start to fail as p gets larger but this is to

### [42:24 - 42:29]

be expected because we're not incorporating history so we're applying like a method for

### [42:29 - 42:36]

mdps to pomdp but we can see that it fails gracefully and that when p is small our method

### [42:36 - 42:41]

still works quite well and you can just see it sort of like inch down as p gets larger

### [42:44 - 42:47]

so in conclusion um we've introduced this

### [42:47 - 42:52]

new framework to address the multitask rl setting by exploiting latent structure in the dynamics

### [42:53 - 42:58]

we can provide error and value bounds for this setting and show improvements in sample complexity

### [42:59 - 43:05]

some limitations are that we assume a stationary setting per task so and each task is clearly

### [43:05 - 43:11]

delineated and marked with an environment id so some nice future work would be to look at the

### [43:11 - 43:16]

continual learning setting where your dynamics can change slowly over time with no clear demarcation

### [43:16 - 43:17]

that we're in a new task

### [43:17 - 43:21]

and we no longer have access to like an environment id that tells us this

### [43:22 - 43:27]

i realized after working on this that we could have easily handled different reward functions

### [43:27 - 43:32]

so that's definitely some future work that we should acknowledge and it would be really nice

### [43:32 - 43:37]

to handle more realistic settings and you know we worked in toy simulated environments and only

### [43:37 - 43:44]

modify one factor at a time and it'd be nice to see how well this scales up to more complex changes

### [43:45 - 43:47]

so um just

### [43:47 - 43:54]

to now like look ahead to some future work that i'm i'm working on now um is the contextual mdp

### [43:54 - 44:03]

setting so so this is uh this is now looking at um um the setting where we don't have that task

### [44:03 - 44:08]

id anymore where you don't have a clear delineation across tasks and things are just like changing

### [44:08 - 44:14]

continuously and you know this is removing that stationarity assumption from our original

### [44:14 - 44:15]

definition of an mdp and uh i think this is really interesting to see that there's going to be we're going

### [44:15 - 44:17]

to use it in a couple of different ways it's going to be using the mdp settings and then we're going to

### [44:17 - 44:21]

And we wanna see what we can say here in terms of theory

### [44:21 - 44:24]

and like what we can design in terms of a representation

### [44:24 - 44:28]

in terms of an algorithm to be able to address this setting.

### [44:28 - 44:31]

So on top, I just have this definition of a contextual MDP

### [44:31 - 44:32]

where these things can change,

### [44:32 - 44:37]

where you have a context that modifies your reward function

### [44:38 - 44:41]

and your transition model, possibly even your state space.

### [44:43 - 44:44]

Oh, and actually on the bottom,

### [44:44 - 44:47]

I have the version where it can modify your state space

### [44:47 - 44:50]

or like you can think of like your observation space

### [44:50 - 44:51]

is changing over time.

### [44:51 - 44:55]

And one example of this is that your agent has a camera

### [44:55 - 44:59]

and the camera is just sort of panning over the world.

### [44:59 - 45:01]

And so this is a partial observability setting.

### [45:02 - 45:05]

But the idea is that we don't wanna look at

### [45:05 - 45:10]

the whole very intractable POMDP problem.

### [45:10 - 45:13]

We want to incorporate predictable non-stationarity.

### [45:13 - 45:15]

And so if we incorporate these constraints

### [45:15 - 45:17]

into the POMDP problem,

### [45:17 - 45:18]

like what can we do with that?

### [45:19 - 45:24]

So just in closing, I think like what I wanna impart

### [45:24 - 45:25]

is that state abstractions

### [45:25 - 45:27]

are a theoretically backed construct

### [45:27 - 45:31]

to learn representations for better generalization in RL.

### [45:31 - 45:33]

And we can design gradient based algorithms

### [45:33 - 45:36]

and compute tight bounds on the downstream policy

### [45:36 - 45:39]

that depend on how good these learned representations are.

### [45:39 - 45:42]

And we can leverage additional structural information

### [45:42 - 45:43]

about real environments

### [45:43 - 45:45]

to improve generalization of RL algorithms.

### [45:47 - 45:50]

And finally, none of this work would be possible

### [45:50 - 45:51]

without my collaborators.

### [45:51 - 45:54]

And so I just have here like the collaborators

### [45:54 - 45:56]

that worked with me on the three papers

### [45:56 - 45:57]

that I mentioned today,

### [45:57 - 46:00]

but there's many more collaborators

### [46:00 - 46:03]

who have worked on sort of like work leading up to this,

### [46:03 - 46:06]

who it's been a pleasure to work with.

### [46:06 - 46:08]

So thank you for listening

### [46:08 - 46:10]

and I'm happy to take any additional questions.

### [46:12 - 46:14]

Thank you very much.

### [46:14 - 46:15]

I think Angelos has a question in the Q&A,

### [46:15 - 46:16]

but I'm gonna ask it to Angelos.

### [46:16 - 46:17]

Okay.

### [46:17 - 46:18]

But it might've been from the last.

### [46:20 - 46:21]

Oh, oops.

### [46:21 - 46:22]

Yeah, hold on.

### [46:22 - 46:23]

Sorry, I see it.

### [46:23 - 46:24]

I just...

### [46:26 - 46:28]

Can you please comment

### [46:28 - 46:31]

on how the bi-symmetric preserves future rewards?

### [46:31 - 46:33]

Is this due to the W2 on the transitions

### [46:33 - 46:35]

for the abstractions?

### [46:35 - 46:36]

Yeah.

### [46:38 - 46:43]

Sorry that I, if I didn't explain that very clearly.

### [46:44 - 46:44]

Okay, all right.

### [46:44 - 46:46]

This is gonna take a while.

### [46:47 - 46:48]

Here we go, okay.

### [46:48 - 46:51]

So this is the definition for the,

### [46:51 - 46:53]

okay, for the bi-simulation metric, right?

### [46:53 - 46:58]

So the bi-simulation metric is very similar

### [46:58 - 47:01]

to the original definition for bi-simulation, right?

### [47:01 - 47:06]

So I hope it's clear how this is preserving future reward

### [47:06 - 47:09]

because of this second equation

### [47:09 - 47:13]

that is preserving equivalence.

### [47:13 - 47:15]

So what the second equation here is saying

### [47:15 - 47:19]

that your two states SI and SJ are only equivalent

### [47:19 - 47:24]

if they have the same probability distributions

### [47:25 - 47:27]

into next abstract states.

### [47:27 - 47:31]

So it has to have the same distribution into next states

### [47:31 - 47:32]

that also have the same reward.

### [47:32 - 47:34]

So now we're saying like,

### [47:34 - 47:37]

what this is saying is that this reward condition

### [47:37 - 47:39]

has to hold true for the next states

### [47:39 - 47:42]

that it transitions into, right?

### [47:42 - 47:43]

And so on and so forth.

### [47:43 - 47:44]

But like, into the future.

### [47:44 - 47:47]

So this is equation two is saying

### [47:47 - 47:50]

two states are only equivalent

### [47:50 - 47:52]

if there infinite future rewards

### [47:52 - 47:56]

or rewards into the end of the horizon are the same.

### [47:57 - 48:01]

So equation two is just taking the condition of equation one

### [48:01 - 48:04]

and saying, this always has to hold

### [48:04 - 48:05]

for every future time step.

### [48:07 - 48:12]

And so the bi-simulation metric uses that same condition.

### [48:12 - 48:17]

It's just that this now just captures more information.

### [48:17 - 48:19]

So the bisimulation metric says, okay,

### [48:19 - 48:21]

if you have two states that are equivalent

### [48:21 - 48:24]

under the bisimulation relation,

### [48:24 - 48:28]

then their similarity is zero, their distance is zero.

### [48:28 - 48:30]

But now I'm also saying, well,

### [48:30 - 48:33]

I also care about how close two states are

### [48:33 - 48:34]

if they're not exactly equivalent.

### [48:36 - 48:38]

And so this Wasserstein captures that.

### [48:38 - 48:41]

So if you have two states that have

### [48:42 - 48:44]

for several time steps, they're exactly the same

### [48:44 - 48:48]

in terms of like the reward that you see for any action,

### [48:48 - 48:51]

but then like 20 time steps into the future,

### [48:51 - 48:54]

their rewards are now slightly different

### [48:54 - 48:55]

for the same action.

### [48:55 - 48:59]

Then this Wasserstein is gonna capture that distance.

### [48:59 - 49:01]

And so then this bisimilarity,

### [49:01 - 49:04]

this is gonna have like a non-zero value

### [49:04 - 49:07]

for these two states, but it'll be a small value

### [49:07 - 49:10]

compared to the bisimilarity between two other states

### [49:10 - 49:12]

where, you know, like the,

### [49:12 - 49:14]

their immediate reward is different.

### [49:18 - 49:20]

Angelos, you're free to unmute yourself

### [49:20 - 49:22]

if you'd like to follow up on it, otherwise.

### [49:24 - 49:25]

No, that was clear.

### [49:25 - 49:26]

Thanks a lot.

### [49:30 - 49:31]

Very cool.

### [49:31 - 49:33]

I have a quick question.

### [49:33 - 49:36]

I'm just wondering, do you,

### [49:40 - 49:42]

do you see any potential risks,

### [49:42 - 49:43]

with this setup?

### [49:43 - 49:48]

So in sort of finding this like sort of very,

### [49:48 - 49:50]

like this task specific representation.

### [49:50 - 49:52]

So I mean, I see like the benefit obviously

### [49:52 - 49:56]

that you are eliminating irrelevant information

### [49:58 - 50:01]

that's guided by sort of the task that you're looking at.

### [50:01 - 50:04]

Is there, I don't know, are there any potential risks?

### [50:04 - 50:06]

Are there any, are you losing anything

### [50:06 - 50:09]

by getting rid of this sort of irrelevant information?

### [50:09 - 50:14]

Yeah, so it just, it does mean that if you're

### [50:16 - 50:18]

in a multitask setting or a continual RL setting

### [50:18 - 50:20]

where things are changing,

### [50:20 - 50:24]

that some of what was irrelevant

### [50:24 - 50:27]

could become relevant later and you've dropped it.

### [50:29 - 50:33]

And, you know, the way that I get around that

### [50:33 - 50:36]

is just by saying, we're gonna very strictly define

### [50:36 - 50:39]

this family of MDPs that this works for, right?

### [50:39 - 50:42]

Like this block MDP just defines like a,

### [50:42 - 50:44]

like a specific set of MDPs

### [50:44 - 50:46]

that this representation will work for

### [50:46 - 50:48]

in the hidden parameter setting

### [50:48 - 50:50]

that also just defines a very specific family

### [50:50 - 50:51]

that this will work for.

### [50:51 - 50:54]

And it's not going to work for anything outside of that.

### [50:54 - 50:55]

So I think what you're asking is like,

### [50:55 - 50:57]

how can we relax this?

### [50:57 - 51:00]

Like if we, maybe we don't,

### [51:00 - 51:02]

maybe we don't necessarily know

### [51:02 - 51:05]

that everything fits into this structure.

### [51:08 - 51:09]

That's a good question.

### [51:09 - 51:14]

And I currently don't have a good answer for it.

### [51:14 - 51:15]

I think it would be,

### [51:19 - 51:21]

like, it would be nice if you know

### [51:21 - 51:24]

that you have this distribution over MDPs.

### [51:24 - 51:27]

You don't know what the structure is.

### [51:27 - 51:29]

You know, hopefully there's something shared

### [51:29 - 51:34]

across these MDPs and you can learn something.

### [51:35 - 51:38]

You can, yeah, you can learn a representation such that

### [51:38 - 51:39]

any other MDPs, you know, you can learn a representation such that any other MDPs,

### [51:39 - 51:42]

that need to be used in the MDPs

### [51:42 - 51:43]

would be able to easily be sampled from that distribution.

### [51:43 - 51:44]

Like this representation would work well for that.

### [51:44 - 51:46]

I think if we just have something that broad,

### [51:46 - 51:48]

we basically if we default,

### [51:48 - 51:50]

so like original methods that

### [51:50 - 51:51]

don't use these state of attractions,

### [51:51 - 51:53]

then I think those might be the best you can do

### [51:53 - 51:57]

because we're not making any additional assumptions.

### [51:57 - 52:00]

Maybe we can do better,

### [52:00 - 52:02]

but I can't think of anything off the top of my head.

### [52:02 - 52:05]

But yeah I guess like before thinking about this thought.

### [52:05 - 52:06]

After chronic Lane sogar the backdrop of vida,

### [52:06 - 52:07]

how does static and unusual properties apply to be valid?

### [52:07 - 52:08]

Have we all got some assumptions you've made about

### [52:08 - 52:09]

it? I don't think there really are any options yet,

### [52:09 - 52:17]

The point, I think, of my work is that we can often make these structural assumptions,

### [52:17 - 52:24]

you know, like the laws of physics in the real world are invariant.

### [52:24 - 52:31]

And so that should be something that's incorporated into, like, into our definition of the environment.

### [52:31 - 52:40]

That's very interesting. So we still have five more minutes if anybody has any more questions.

### [52:40 - 52:45]

I guess I just have a soft one. So what is your motivation to sort of, like, get into this line of

### [52:46 - 52:55]

research? Yeah, I really like RL. I really like work that sort of interacts with the world and,

### [52:55 - 52:57]

like, learns from the interaction.

### [52:59 - 53:00]

And

### [53:01 - 53:07]

I mean, I think, like, I got into this, like, because sort of, like, there were starting to

### [53:07 - 53:11]

be these questions about the generalization of RL. And so that was something that I got in pretty

### [53:11 - 53:20]

early on. And from there, it was sort of, why doesn't deep RL work for robotics? Why doesn't

### [53:20 - 53:25]

deep RL work for all of these settings? Like, why is it that bandits have been so successful,

### [53:25 - 53:30]

and we haven't really been able to get deep RL to work? And so this, to me, is like a very structured

### [53:31 - 53:37]

theoretically backed way forward. I prefer, like, I'm much more excited about

### [53:37 - 53:43]

work that I can sort of, like, ground in theory. And I really like state abstractions,

### [53:43 - 53:49]

because it is a very concrete objective of what you're trying to learn. And hopefully,

### [53:49 - 53:54]

I, like, I'm hoping that this will be a way forward to, like, real, to RL in the real world.

### [53:55 - 53:56]

That's very cool.

### [53:59 - 54:01]

Yes, speaking of state abstractions.

### [54:01 - 54:06]

How, how does, why did you choose sort of the bisimulation metrics compared to, I don't know,

### [54:08 - 54:09]

homomorphisms or something?

### [54:10 - 54:12]

Like other forms of state abstraction?

### [54:12 - 54:13]

Yeah, yeah.

### [54:13 - 54:23]

Yeah. So yeah, there's, there's not. So these were the, so bisimulation is like the strictest

### [54:23 - 54:28]

form of state abstraction. I could talk about, like, other levels of state abstraction that are

### [54:28 - 54:31]

coarser in the sense that they drop even more.

### [54:31 - 54:47]

They're all

### [54:47 - 54:52]

necessarilyoire.

### [54:52 - 54:58]

Some other questions.

### [54:58 - 54:58]

I see.

### [54:58 - 55:00]

Yeah, justina, do you have a, could you just add something?

### [55:00 - 55:13]

under the optimal policy and so this is going to be a coarser form of state abstraction there are even coarser ones where you say I don't even care about the individual reward I just care about

### [55:14 - 55:28]

capturing like the difference between the difference in the optimal policy behavior between states so now you can't extract like the value from states anymore right because you can have two states where

### [55:30 - 55:31]

that have

### [55:33 - 55:45]

different optimal value but the policy behavior is the same right because all that you all that the policy cares about is like the ranking of of reward and and like the actions that it sees

### [55:46 - 55:55]

and so these are sort of like coarser versions that mean that mean that the representation that you learn is even more compact

### [55:56 - 56:00]

and hopefully we can get even better generalization than with like a more compact representation

### [56:01 - 56:12]

or better sample efficiency well yeah we know that we can get better sample efficiency with that so those are additional future directions to explore and I think those are those are exciting yeah

### [56:13 - 56:22]

cool I actually missed one question from Yaron in the chat how about stochastic rewards in equation one Yaron do you want to expand on that

### [56:23 - 56:29]

yeah sure so if you assume that the reward function

### [56:31 - 56:36]

if you assume that the reward that you get from the environment is stochastic do these what do these things

### [56:37 - 56:48]

the equation one is not properly defined anymore yeah so what will be an are there any extensions of biostimulation of these definitions to the sort of relaxations of the assumptions

### [56:49 - 56:56]

not yet that's also something that I'm currently working on I mean yeah that's a really good question so yeah this definition is assuming that

### [56:56 - 57:02]

your reward is just like a is just like a definite scalar that you see

### [57:03 - 57:04]

and

### [57:05 - 57:14]

it's it's pretty easy to change this definition to now just be like if you have a stochastic reward then you know your your reward model has to

### [57:15 - 57:23]

be able to model the distribution so that you can compute the distance and distribution but we can just replace this with the same thing that we have here right like we can just

### [57:23 - 57:31]

put the probability over your reward and now we can compute the Wasserstein distance like between those two probability distributions

### [57:32 - 57:36]

and we're actually I we're actually trying this for the VATRL setting

### [57:37 - 57:38]

so again

### [57:39 - 57:42]

so the other ways of replacing that so in equation two because these are discrete

### [57:43 - 57:46]

I'm not even sure if these are discrete objects but when you say okay

### [57:47 - 57:52]

okay let me ask a deeper question equation two when you say these are equal in probability

### [57:52 - 57:53]

do you mean

### [57:54 - 57:57]

you mean that they're equal in probability or equal in distribution so there are different like the

### [57:58 - 58:05]

three or four different levels of equality in probability or distribution or having being the same random variable and basically my question is

### [58:06 - 58:08]

which one of these do you need and why

### [58:09 - 58:10]

yeah

### [58:11 - 58:13]

so in this original definition which is

### [58:14 - 58:22]

taken from a paper by ferns that was like in the 90s he only looked at discrete MDPs

### [58:23 - 58:30]

so you can just use this exact equality and and you're just comparing exact probabilities for different abstract states

### [58:31 - 58:35]

this can be relaxed to the continuous setting and so

### [58:36 - 58:42]

the distance now that we're measuring between these probability distributions is the Wasserstein distance

### [58:44 - 58:50]

and so yeah so so now we can actually compare or like compute a distance between

### [58:51 - 58:53]

continuous probability distributions

### [58:54 - 58:59]

okay so like equation two is not precise then because it does sound like

### [59:01 - 59:08]

okay so do these things have to be equal up to a zero measure set do they have to be what does it mean for these two probabilities to be equal

### [59:09 - 59:11]

do you mean the densities have to be the same

### [59:13 - 59:14]

um

### [59:15 - 59:18]

so in the discrete MDP setting

### [59:18 - 59:21]

right like all of these things are discrete like well

### [59:22 - 59:29]

yeah exactly so my question is like when you transfer from that to the continuous case because that's basically what prompted my question about the reward function which will be continuous

### [59:30 - 59:31]

and like

### [59:32 - 59:37]

but that that's a bigger question about like also when you just have continuous states what

### [59:38 - 59:46]

I assume that equation two means something that is not necessarily what is written as p of g equals p of g condition s i equals p of g condition s j

### [59:48 - 59:55]

um so in the continuous setting like we want it to be matching exactly so we would be matching densities

### [59:56 - 01:00:04]

okay so even if you have a single g a zero measure set of g's for which this does not hold would that break your definition

### [01:00:06 - 01:00:09]

uh a zero measure set of g's

### [01:00:11 - 01:00:17]

um sorry or do you mean that like g is an empty set or

### [01:00:17 - 01:00:20]

uh so if s is a continuous

### [01:00:21 - 01:00:22]

space

### [01:00:23 - 01:00:31]

and which over which you define some measure that would give and you choose a single g in that s that will have because it's a singleton it will have

### [01:00:32 - 01:00:34]

it will have measure zero

### [01:00:35 - 01:00:36]

uh

### [01:00:37 - 01:00:41]

in setting basically almost all the time

### [01:00:42 - 01:00:43]

yeah no I understand okay yeah

### [01:00:44 - 01:00:46]

definition equation two does not have to hold but I don't see if that

### [01:00:47 - 01:00:49]

necessarily would break your definition

### [01:00:50 - 01:00:55]

um so it doesn't break it because this is for all g so um

### [01:00:56 - 01:01:03]

so I'm saying if what if that would if that were to be the case for all g apart from up to zero measure or for almost all g basically

### [01:01:04 - 01:01:05]

will that will definition still hold

### [01:01:06 - 01:01:14]

it'll still hold I mean so if for for almost all g like this is just effectively you know these are zero and so then they're all they're automatically equal

### [01:01:14 - 01:01:19]

but as long as there are any g for which these probabilities are different

### [01:01:20 - 01:01:24]

then like this has to hold for all g so we're checking this for all g

### [01:01:25 - 01:01:29]

uh these would not necessarily be zero so it could be as

### [01:01:32 - 01:01:39]

so okay that's fine I think like what I have in mind is like there could be a zero measure set of g's for which the quality would not hold

### [01:01:40 - 01:01:42]

for which the conditional density

### [01:01:42 - 01:01:45]

for one would not be the same as the other one but

### [01:01:48 - 01:01:49]

I'm not sure if

### [01:01:51 - 01:01:52]

okay

### [01:01:53 - 01:01:57]

reason why I'm asking that is basically I want to see what are the assumptions over here can be

### [01:01:58 - 01:02:08]

relaxed and I think that is one assumption that could be relaxed we don't need to require that to hold for all g I think you can require that to hold for almost all g for all g up to zero measure set basically

### [01:02:09 - 01:02:10]

and because of that

### [01:02:10 - 01:02:14]

I'm trying to figure out like what exactly is needed in this definition

### [01:02:15 - 01:02:20]

what what is what what or what of these assumptions actually needed for the definition

### [01:02:21 - 01:02:38]

interesting yeah I haven't really thought about relaxing this distance measure right and and for the continuous setting like the Wasserstein distance does make sense right because you're it's earthmover like you're just you're literally just comparing like the the if these distributions are exactly the same so

### [01:02:38 - 01:02:49]

I think I'm yeah I think it would be nice to discuss this with you further because I think I'm not like not quite understanding like what kind of relaxations that you have in mind

### [01:02:50 - 01:02:53]

but that is another limitation of our

### [01:02:54 - 01:03:06]

like of our implementation of this is that we are restricting our dynamics models to output Gaussian distribution so that we can compute the Wasserstein as a closed form

### [01:03:06 - 01:03:08]

or like the

### [01:03:09 - 01:03:12]

and it and and that's okay

### [01:03:14 - 01:03:17]

a latent representation space so we can sort of construct

### [01:03:18 - 01:03:25]

the distribution that even if the true transition distribution is not Gaussian you know we can construct it to be that way in the latent

### [01:03:26 - 01:03:27]

but

### [01:03:28 - 01:03:34]

I think there are limitations to that especially with given like the other constraints that we have on the latent representation that we learn

### [01:03:34 - 01:03:38]

so if there are other ways of like learning this

### [01:03:39 - 01:03:40]

of like measuring distance

### [01:03:41 - 01:03:47]

point yeah so the Gaussian constraint might be

### [01:03:48 - 01:03:49]

the question

### [01:03:50 - 01:03:59]

so the question of when is it actually justified that it makes sense to assume Gaussian dynamics under these assumptions one and two that's interesting

### [01:04:00 - 01:04:01]

okay

### [01:04:02 - 01:04:03]

yeah thank you

### [01:04:04 - 01:04:05]

cool

### [01:04:06 - 01:04:13]

well I think that probably makes sense to end on that point I don't think there's any further questions in the chat or the Q&A

### [01:04:15 - 01:04:19]

so I'd like to thank you again Amy for for your talk and the discussion

### [01:04:22 - 01:04:24]

and I guess we'll finish up there

### [01:04:26 - 01:04:27]

okay thank you

### [01:04:34 - 01:04:43]

thanks for watching

### [01:04:44 - 01:04:45]

you

### [01:04:46 - 01:04:47]

I hope that's

### [01:04:48 - 01:04:49]

that's

### [01:04:49 - 01:04:50]

that's

### [01:04:50 - 01:04:52]

that's

### [01:04:52 - 01:04:53]

be

### [01:04:54 - 01:04:54]

and

### [01:04:54 - 01:04:55]

the

### [01:04:55 - 01:04:56]

the

### [01:04:56 - 01:04:57]

the

### [01:04:57 - 01:04:58]

the

### [01:04:58 - 01:04:59]

the

### [01:04:59 - 01:05:00]

the

### [01:05:00 - 01:05:00]

the

### [01:05:00 - 01:05:01]

the

### [01:05:01 - 01:05:02]

the

### [01:05:02 - 01:05:02]

the
