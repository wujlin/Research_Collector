# Amy Zhang - Exploring Context for Better Generalization in Reinforcement Learning @ UCL DARK

- URL: https://www.youtube.com/watch?v=akeUVn6WQoU
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T20:35:45`

## Transcript

### [00:00 - 00:12]

Hi everyone, thanks for coming and welcome to the next installment of the UCL Dark invited speaker series. Today we're going to hear from Amy Zhang on the topic of exploring context for better generalization in reinforcement learning.

### [00:13 - 00:22]

Amy has just graduated, I hear, from a PhD at McGill University and is now doing a postdoctoral fellowship, I guess, at Berkeley.

### [00:22 - 00:31]

During her PhD she was co-supervised by Joelle Pinot and Dorina Precup and was a member of Facebook AI Research.

### [00:32 - 00:41]

She works on state abstractions, model-based reinforcement learning, representation learning, and, of course, generalization in reinforcement learning. Amy, really excited to hear what you have to say.

### [00:42 - 00:47]

Thank you, thank you for the very nice introduction. Like you said, today I'll be talking

### [00:47 - 00:52]

more about exploring context for better generalization and reinforcement learning and

### [00:52 - 00:56]

this works, builds on top of, you know, the work I'd done previously on

### [00:56 - 01:04]

bisimulation and state abstractions, but those topics I'm going to skip over a bit, but please feel free to stop me and ask clarifying questions.

### [01:05 - 01:12]

Or if you want to talk a little bit more about about state abstractions for the single test setting, we can also talk more about that.

### [01:14 - 01:22]

But yeah, with that I'll just get started. So I'm really excited about the potential of reinforcement learning to be applied to the real world and so

### [01:23 - 01:32]

a lot of my work on generalization on trying to get better sample efficiency is very much geared towards thinking about these applications.

### [01:32 - 01:39]

And so, specifically, the kinds of applications that I like thinking about that are natural for me are to think about personalized household robots,

### [01:40 - 01:48]

having robots that can perform a variety of tasks within a single home and generalize to new homes, learned autonomous driving, having

### [01:49 - 01:52]

autonomous cars that can generalize to new terrain that they weren't trained on,

### [01:53 - 02:00]

and personalized healthcare. Healthcare where we can train on a on a data set of patients and obviously be able to extrapolate to new patients.

### [02:01 - 02:07]

So there's been a lot of exciting recent success in deep reinforcement learning, in particular in the last few years.

### [02:08 - 02:19]

And some examples of this that have been in sort of like the wider media are OpenAI, StarCraft, and Dota, DeepMind, AlphaGo, AlphaZero, and Atari. And so these are all examples where

### [02:19 - 02:22]

deep RL algorithms have been able to achieve beyond

### [02:23 - 02:31]

human performance. But I think we're all aware that there's still a lot of disappointing failures and we're still not really seeing reinforcement learning in the wild yet.

### [02:31 - 02:47]

So why is there this discrepancy? We're seeing that deep RL works really well in these single task settings in simulation when you have access to millions of transitions, but it works less well in visually complex, natural, and multitask settings.

### [02:48 - 02:52]

And specifically what I mean by this is that we're not seeing the same kind of generalization progress.

### [02:53 - 03:01]

So what you can see here in the box for example, as we would supposeída s we can know this is the same type of learning performance that we've been getting out of deep learning in computer vision and natural language processing.

### [03:02 - 03:05]

And so what I'm really interested in is structure.

### [03:05 - 03:11]

And what kind of additional inductive biases can be leveraged from the environments that we care about.

### [03:12 - 03:19]

So before I jump into that, you know, I think it's good to just go over what is the typical setting that we assume in reinforcement learning.

### [03:20 - 03:21]

So we assume that the

### [03:21 - 03:22]

environment

### [03:22 - 03:28]

just means that we have a state space s an action space a a transition probability distribution p

### [03:28 - 03:35]

reward function r and the agency states from the environment st takes an action based on that

### [03:35 - 03:43]

based on that state um that that action taken in the environment steps it and updates it and so uh

### [03:43 - 03:49]

then the agent receives the next reward and next state and the goal of the agent is to maximize

### [03:49 - 03:54]

this reward signal and so an interesting question i think to we can ask here is what kind of

### [03:54 - 03:59]

additional structure is reasonable to assume in mdps in in the environments that we care about

### [04:00 - 04:07]

and so the focus of this talk is about context as structure and so there are a couple of different

### [04:07 - 04:13]

additional assumptions that define these um new types of mdp families that i'm going to focus on

### [04:13 - 04:19]

so the first two are just these uh block mdp and hidden parameter mdp and so we're

### [04:19 - 04:19]

going to talk a little bit more about that and then we're going to talk a little bit more about

### [04:19 - 04:23]

both of these assumptions which i'll describe in more detail later in this talk

### [04:23 - 04:29]

for this paper on learning robust state abstractions for hidden parameter block mdps and

### [04:29 - 04:34]

later i'm going to talk about two papers that leverage contextual mdps and also the block

### [04:34 - 04:42]

assumption on that block contextual mdps so let's dive right in into this first paper which

### [04:42 - 04:48]

is presented at iclair this year um so the hidden parameter block mdp uh family can be

### [04:48 - 04:54]

described by all the same components as what we have in the typical mvp but we're adding on a

### [04:54 - 05:02]

couple of additional um assumptions so the first is that instead of seeing our latents uh our state

### [05:02 - 05:07]

space s we're going to assume that this is latent and instead all we have access to is this

### [05:07 - 05:14]

observation space x um and i think like a natural way to think about this setting is is that we

### [05:14 - 05:18]

don't necessarily always have the most um minimal sufficient amount of information that we have to

### [05:18 - 05:24]

get to the point where we can actually get a more efficient statistic of the future dynamics and

### [05:24 - 05:29]

reward as the state space that we're given typically we're given access to something that

### [05:29 - 05:34]

is much noisier or just like much higher dimensional because we don't necessarily know

### [05:34 - 05:40]

what information is necessary um and so one example of this in robotics is is just cameras

### [05:40 - 05:47]

rgb cameras are a very cheap way to gather a lot of information about the world um but what you can

### [05:47 - 05:48]

have in this setting is that there are many possible

### [05:48 - 05:54]

images that can map to the same low dimensional state and so you have this one-to-many mapping

### [05:54 - 05:58]

from states to observations which can make the problem much more complex

### [05:59 - 06:05]

but but knowing that we have this structure means that we can leverage it and get better

### [06:05 - 06:12]

guarantees and and possibly better algorithms so that's the block uh component that's this

### [06:12 - 06:18]

observation space x and this one-to-many rendering mapping q from s to x another

### [06:18 - 06:23]

function that we can make is is this this one about hidden parameter mdps so here we're

### [06:23 - 06:29]

assuming that we have multiple environments that have different dynamics but all of the

### [06:29 - 06:35]

different dynamics can be described by a single universal dynamics model t and

### [06:36 - 06:43]

there's really just this latent variable or this hidden parameter space theta that can explain the

### [06:43 - 06:48]

variations in dynamics across these different environments that we have access to and so t is

### [06:48 - 06:55]

an example of this latent parameter theta and so this again maps to some real-world applications

### [06:55 - 07:03]

um so we can think of of uh the laws of physics the universal dynamics of the world as t uh but

### [07:03 - 07:08]

depending on on what task you're focusing on um like as an example different objects have

### [07:08 - 07:14]

different dynamics and that that can be explained by friction coefficients and like mass and so

### [07:14 - 07:18]

those would be examples of this hidden this this latent parameter theta

### [07:19 - 07:25]

so for this hip bmdp setting and we sort of conflate the term and also use it to name our

### [07:25 - 07:34]

method as hip bmdp um we our goal is to learn uh so we're we're in this multitask setting

### [07:34 - 07:38]

a constrained multitask setting where we assume that we have the same reward function it's the

### [07:38 - 07:42]

same task we're just trying to perform it in these different environments that have different

### [07:42 - 07:48]

dynamics and because we're assuming this a multitask setting we assume that we have access to

### [07:48 - 08:09]

this

### [08:11 - 08:18]

we want l2 distance in this task embedding space to correspond to some notion of the distance between

### [08:18 - 08:24]

these two environments. And we can define that distance between these environments to be the

### [08:24 - 08:30]

Wasserstein. And so the Wasserstein is just a distance between probability distributions.

### [08:30 - 08:35]

So this will be a distance between the probability distributions into next state of these different

### [08:35 - 08:44]

tasks. So another way to think about this is the distance in terms of the L2 distance between task

### [08:44 - 08:51]

embeddings for different tasks corresponds to how different the dynamics between those two tasks

### [08:51 - 08:56]

are. And so in order to train this component, it requires that we have to train a dynamics model

### [08:56 - 09:01]

over all of these different environments. And so we train a universal dynamics model

### [09:01 - 09:05]

that is conditioned on the theta produced by this environment encoder.

### [09:07 - 09:13]

And we use this to also measure distance between tasks in order to train this environment encoder.

### [09:14 - 09:21]

And so this, so that's how we train the environment encoder. And we train the state

### [09:21 - 09:29]

encoder in a very similar way using bisimulation metrics. And so the state encoder we train so that

### [09:29 - 09:35]

so that it's just like a compressed version of the pixel observation space as well.

### [09:38 - 09:42]

And so then this produces these two representation spaces, our task embedding space,

### [09:42 - 09:44]

our state embedding space.

### [09:44 - 09:49]

And now we can just train any policy optimization method on top. And so here we're just using

### [09:49 - 09:55]

software critic. But you can think of all of these components as being trained online together,

### [09:55 - 10:00]

but they are separate optimization steps. So with every step that the agent takes in the

### [10:00 - 10:06]

environment, we train our dynamics model and reward model. We train our state representation

### [10:06 - 10:13]

space, our environment representation space, and we train our actor and critic.

### [10:14 - 10:18]

Sandra

### [10:18 - 10:24]

So before we dive into empirical results, I wanted to talk a little bit about the kind of theoretical

### [10:24 - 10:29]

analysis that we can do. So because in effect we're learning this approximate bisimulation

### [10:29 - 10:37]

abstraction we can measure our error in terms of how far that so by learning this abstraction,

### [10:38 - 10:44]

we're constructing a new MDP and we are doing our policy optimization on top of this MDP as opposed to the original.

### [10:44 - 10:48]

The reason that we want to do this is that because we're learning an abstraction of the

### [10:48 - 10:54]

original environment, we can construct it to be more amenable to learning, it can be

### [10:54 - 11:01]

a much smaller MDP because of this assumption of this like latent block structure.

### [11:01 - 11:09]

So in order to measure sort of how far off this MDP is from the original and therefore

### [11:09 - 11:17]

how suboptimal is a Q function learned on this new MDP going to be compared to the true

### [11:17 - 11:23]

optimal Q on top of the ground truth MDP, we want to use these error terms.

### [11:23 - 11:28]

So we have epsilon r, epsilon t, and epsilon theta, and these just correspond to the worst

### [11:28 - 11:36]

case error for any possible state action from our ground truth MDP and where it maps to

### [11:36 - 11:38]

in terms of this abstract MDP.

### [11:38 - 11:39]

And we can just measure this.

### [11:39 - 11:43]

This is like empirically as the training error.

### [11:43 - 11:47]

So these two components really just describe a new MDP, which is close to the original

### [11:47 - 11:49]

for a specific task.

### [11:49 - 11:54]

And this epsilon theta is now, you can think of this as a per task error because we're

### [11:54 - 11:59]

now in a multitask setting.

### [11:59 - 12:04]

So the first question that we want to ask is how does the error in theta prediction

### [12:04 - 12:09]

and the learned by simulation representation affect the learned optimal policy?

### [12:09 - 12:13]

And so the bound that we really want to compute here is this.

### [12:13 - 12:15]

And so I'm going to explain this notation.

### [12:15 - 12:21]

So this is saying that through our learned representations, we've constructed this approximate

### [12:21 - 12:24]

new MDP M bar.

### [12:24 - 12:29]

We're learning an optimal Q function on M bar, and so that can be denoted as Q star

### [12:29 - 12:30]

M bar.

### [12:30 - 12:36]

And now we want to take the policy informed by this Q function and apply it back to the

### [12:36 - 12:37]

true environment.

### [12:37 - 12:38]

And so we're basically lifting it.

### [12:38 - 12:39]

Okay.

### [12:39 - 12:41]

To this M theta.

### [12:41 - 12:48]

And we want to know what is the difference between Q star learned on M bar and the true

### [12:48 - 12:50]

Q star of our ground truth environment.

### [12:50 - 12:56]

And so then we can see that this very simply that this difference is upper bounded by those

### [12:56 - 12:59]

terms that we had introduced in the last slide.

### [12:59 - 13:01]

And then this component is something that you can't really change.

### [13:01 - 13:08]

So our max is the maximum reward in your environment, and we know that the largest value that you

### [13:08 - 13:14]

can see in this environment is going to scale with with respect to our max over one minus

### [13:14 - 13:19]

gamma our discount factor.

### [13:19 - 13:23]

So a very related result that we can also compute is how well is a policy trained in

### [13:23 - 13:27]

one task going to do when it's applied to another task.

### [13:27 - 13:32]

So moving from task theta i to task theta j.

### [13:32 - 13:34]

So this is the exact same thing.

### [13:34 - 13:38]

We've trained a Q star on our approximate version of theta i.

### [13:38 - 13:40]

We're going to apply it to theta j.

### [13:40 - 13:47]

And that bound also depends on the same sorts of things, but it actually now has a term

### [13:47 - 13:51]

that lends itself really nicely to that task embedding space that we're learning.

### [13:51 - 13:57]

So here now we're seeing that this notion of distance between tasks is incorporated

### [13:57 - 14:01]

in this bound as the L1 distance between theta i and theta j.

### [14:01 - 14:07]

So this is very similar now to that distance metric in our task embedding space.

### [14:07 - 14:08]

So I think.

### [14:08 - 14:13]

One final nice thing to look at is the sample complexity analysis.

### [14:13 - 14:18]

This analysis doesn't really apply to our algorithm because it's really only relevant

### [14:18 - 14:22]

for the tabular setting, but I think it's still useful to look at because it shows you

### [14:22 - 14:27]

exactly the kinds of gains that you get from making these additional assumptions of structure

### [14:27 - 14:30]

in your MDP.

### [14:30 - 14:33]

So we get.

### [14:33 - 14:37]

We get a speed up or improvement in sample complexity in two places.

### [14:38 - 14:40]

So the first is here.

### [14:40 - 14:43]

So because of the block assumption.

### [14:43 - 14:53]

We know that our true state space is much smaller than the state space that we're given or what we're calling it the observation space.

### [14:53 - 14:55]

So we can sort of denote these two separate spaces.

### [14:55 - 15:06]

So typically, if we don't use the block assumption, then this sample complexity analysis is going to depend on the cardinality of the space that you're that you're taking as input.

### [15:06 - 15:08]

So if it's high dimensional pixels.

### [15:08 - 15:12]

space and this is going to be huge because we know that we have the block assumption we're

### [15:12 - 15:18]

learning the state abstraction that corresponds to like a much smaller equivalent mdp we get this

### [15:18 - 15:24]

gain another gain that we get because we're operating in this multi-task setting most sample

### [15:24 - 15:30]

complexity bounds for the multi-task setting depend on the number of tasks that you see at

### [15:30 - 15:35]

training time because we're making this hidden parameter mdp assumption which says that we're

### [15:35 - 15:42]

really in a single mdp and the variation across tasks can be described by just the single latent

### [15:42 - 15:50]

variable it means that we can instead rely on the number of samples that you see in aggregate over

### [15:50 - 15:55]

all of your tasks which is a pretty significant improvement and that's sort of denoted by this

### [15:55 - 16:05]

n5d here so now we can move to the empirical results so we've just modified some basic

### [16:05 - 16:05]

basic

### [16:05 - 16:09]

benchmarks that we typically use in reinforcement learning so here we're just looking at deep mind

### [16:09 - 16:16]

control and we we're modifying just specific factors in each of these environments in order

### [16:16 - 16:24]

to create this this range of different dynamics across these tasks so here we examine four

### [16:24 - 16:30]

environments but only two of them have differences in dynamics that are visually observable so those

### [16:30 - 16:35]

ones i have here so on the top we have half cheetah where the length of the torso changes and

### [16:35 - 16:40]

so one is the length of his arms this is the size of his head so we've got about 16 feet almost

### [16:40 - 16:43]

of any of the other elements and on the bottom it's harder to see but we have walker and the size

### [16:43 - 16:49]

of the left foot also changes and so these are two examples of two things that change the dynamics

### [16:49 - 16:55]

we also change things like the friction coefficient and um for finger spin i think

### [16:55 - 16:59]

yeah for fingerspin we change the friction coefficient that the the component like spins in

### [16:59 - 17:03]

and i think for walk or run we change the friction coefficient with the floor to also change the

### [17:03 - 17:04]

dynamics

### [17:04 - 17:09]

new unseen environments on environments with different dynamics than what the agent saw at

### [17:09 - 17:15]

training time. So we compare against other multitask methods like distro, grad norm, and PC

### [17:15 - 17:20]

grad. And the component that I really want to highlight is the difference between our method

### [17:20 - 17:30]

hit BMDP and the sublation hit BMDP node by sim. So this in orange is really just the exact same

### [17:30 - 17:36]

thing as our method, but without the constraint in the task embedding space to incorporate this

### [17:36 - 17:41]

like smoothness with respect to the changes in dynamics. And so we can see that the difference

### [17:41 - 17:48]

in performance here is entirely just because of that objective that we have in the task embedding

### [17:48 - 17:54]

space. We also have results for the meta reinforcement learning setting. So the main

### [17:54 - 17:58]

difference here is that instead of showing zero shot generalization, we're showing performance

### [17:58 - 18:00]

when the agent can

### [18:00 - 18:08]

update for a few cycles on the new unseen environment at evaluation time. So here we can see

### [18:08 - 18:15]

that the differences in performance are much smaller because both hit BMDP and PERL are able

### [18:15 - 18:23]

to update based on the new samples from the new evaluation time. Another thing that we can look

### [18:23 - 18:30]

at in the meta reinforcement learning setting is just model error. And so again, we're just

### [18:30 - 18:36]

looking at our method compared to the ablation without that context, without that task embedding

### [18:36 - 18:43]

objective. And we can see that our learned dynamics model can generalize much more quickly

### [18:43 - 18:47]

to the new environment compared to the version without that objective.

### [18:50 - 18:55]

Another thing we can look at is just relaxing the block MDP assumption. So I kind of glossed

### [18:55 - 19:00]

over this, but a key component of the block MDP assumption is that we're assuming we've

### [19:00 - 19:05]

got the probability P, and that we have the Markov property and the observation space.

### [19:05 - 19:13]

And so this is the only thing really that separates it from the POMDP setting. This is a pretty

### [19:13 - 19:18]

stringent assumption to make in a lot of real world settings. And so what we did here is we wanted

### [19:18 - 19:24]

to see how gracefully does our method degrade compared to other baselines if we were to relax

### [19:24 - 19:29]

the Markov assumption. So in fingerspin, what we did is, for some probability P, the probability P,

### [19:30 - 19:33]

the agent's not going to see the current observation. It's going to get dropped,

### [19:33 - 19:38]

and it just gets a copy of the previous observation again. I want to highlight that

### [19:38 - 19:50]

in this example, the agent is not using history. And so it won't be able to achieve sort of the

### [19:50 - 19:56]

best performance it can because it is losing information. So we can see here on the right

### [19:56 - 19:59]

hand side that performance degrades as P gets larger, which is not a surprise.

### [19:59 - 20:04]

But on the left hand side, I think this is interesting, which is that when we compare

### [20:04 - 20:09]

for a small P against the other baselines, it seems like our method is still able to perform

### [20:10 - 20:13]

better in this setting than the other baselines do.

### [20:15 - 20:22]

So to conclude from this work, I think really the main contribution is that we highlight that we

### [20:22 - 20:29]

should be using different types of frameworks to address multitask reinforcement learning and really,

### [20:29 - 20:32]

we're exploiting here is just the slate and structure and the dynamics.

### [20:32 - 20:39]

We show that you can provide error and value bounds for both state space and rich observation

### [20:39 - 20:45]

space settings, and show these improvements in sample complexity. And our code is also

### [20:45 - 20:50]

publicly available. I just want to talk a little bit about some of the limitations of this work.

### [20:50 - 20:57]

So here, the multitask setting, after working on this, I kind of decided I really didn't like it,

### [20:57 - 20:59]

because we have...

### [20:59 - 21:03]

We have access to something that I think you can think of as privileged information,

### [21:03 - 21:08]

the fact that each task is clearly delineated, we're given access to this environment ID.

### [21:09 - 21:13]

I think a much more realistic and interesting setting is the continual learning setting,

### [21:14 - 21:19]

where things like dynamics and reward can possibly change slowly over time.

### [21:20 - 21:26]

After working on this, after being really excited about this HIP MDP setting,

### [21:26 - 21:29]

I realized that we could have very easily handled different reward functions,

### [21:29 - 21:34]

as well, that could have been incorporated as part of a notion of distance between tasks.

### [21:35 - 21:39]

And I think it would be really interesting to be able to handle more realistic settings.

### [21:39 - 21:44]

And specifically, I mean, settings where more than one factor varies at a time.

### [21:44 - 21:46]

And I think the interesting thing to look at there is if you can learn

### [21:47 - 21:53]

this task embedding space that decomposes nicely and can also generalize to new compositions

### [21:54 - 21:55]

of those factors.

### [21:57 - 21:59]

So in order to address some of these limitations,

### [21:59 - 22:06]

I think the contextual MDP framework is actually a little bit more universal and

### [22:06 - 22:08]

more useful than the hidden parameter MDP one.

### [22:08 - 22:16]

And so the contextual MDP setting, you can think of as you having all of these similar tasks that

### [22:16 - 22:20]

potentially even have different state spaces, different dynamics, and different reward.

### [22:21 - 22:25]

And they're described by this different context.

### [22:25 - 22:29]

And so now the question is, how do we leverage shared structure across these tasks?

### [22:30 - 22:36]

So I think it's useful to look at the formal definitions of these things.

### [22:36 - 22:41]

So the contextual MDP, we now have this C, this context space.

### [22:44 - 22:50]

Typically, you assume that you have the same state and action space across these different MDPs.

### [22:50 - 22:54]

But here, your reward and dynamics are now conditioned on C.

### [22:56 - 22:59]

So we're just going to update this a little bit because I think this is still a little bit

### [22:59 - 23:00]

restrictive.

### [23:00 - 23:08]

So we're defining a block contextual MDP where the only difference is that we now assume

### [23:08 - 23:10]

your state space can change across different tasks.

### [23:10 - 23:11]

And this makes sense, right?

### [23:11 - 23:18]

Like in the real world, if your state space is the entire world, if your attention shifts

### [23:18 - 23:20]

to different tasks, then that's fine.

### [23:20 - 23:23]

Your dynamics are different, but your state space has to be the same.

### [23:23 - 23:29]

But in actuality, what we do is we try to constrain the state space to only pay attention

### [23:29 - 23:35]

to what matters for a specific task, which means that your state space will change depending

### [23:35 - 23:37]

on what your task is because you want to attend to different things.

### [23:40 - 23:48]

So I think of this as sort of just a continuation of that first paper on BMPs that kind of fixes

### [23:48 - 23:51]

a lot of the issues that I had raised at the end.

### [23:52 - 23:54]

So now we're looking at the non-stationary setting.

### [23:54 - 23:56]

We care about continual learning.

### [23:57 - 23:59]

And I think the motivation for this work

### [23:59 - 24:04]

just looking at adaptive control so i think adaptive control is really nice because the

### [24:04 - 24:11]

goal there is to just and you you know what you don't know um you we can call this known unknowns

### [24:12 - 24:16]

where you know what the variable is that you're trying to infer you just don't know what the

### [24:16 - 24:24]

value of that is in in different states um and i we want to extend this idea to the setting where

### [24:24 - 24:29]

we have unknown unknowns we don't know what we don't know and we need to infer it to try and

### [24:29 - 24:35]

get good performance in these new unseen environments um i want to define an additional

### [24:36 - 24:43]

thing that i i think is really useful so so um one property that i think that we want to have in

### [24:43 - 24:49]

order to get good generalization is smoothness is is the lipshits property so we can define a

### [24:49 - 24:56]

lipshits block contextual mdp as one in which your dynamics and your reward are lipshits with respect

### [24:56 - 24:58]

to this context um

### [24:59 - 25:06]

this seems like a limitation but i'm going to show how because we are not given this context space

### [25:06 - 25:10]

um so i can you can think of like if you're given the context space then you're and you're just

### [25:10 - 25:15]

trying to infer what the context is for different environments then that's the known unknown setting

### [25:15 - 25:18]

if we're not given the context space and we have to construct it ourselves we're in the unknown

### [25:19 - 25:26]

unknown unknowns setting um and so if we don't have the context space then we can actually

### [25:26 - 25:28]

construct one that obeys this property

### [25:29 - 25:35]

um which is why i'm putting this here uh so this is the more formal definition of the task metric

### [25:35 - 25:41]

that we've kind of defined previously in the hip bmdp setting it just now also incorporates report

### [25:41 - 25:46]

so we can define a notion of distance between tasks that just depends on the difference in

### [25:46 - 25:52]

the reward and the difference in the dynamics between uh for those tasks so i think that's

### [25:52 - 25:58]

pretty straightforward um and if we learn a task embedding space

### [25:59 - 26:07]

that obeys this distance metric this d task then we have the property that the optimal universal

### [26:07 - 26:16]

value function conditioned on c is lipschitz with respect to this task metric and so this

### [26:16 - 26:21]

is a property that we want to have that we're we're going to try and construct like with our

### [26:21 - 26:28]

method uh another assumption that we have to make for this setting is identifiability so

### [26:29 - 26:35]

now because we're in this non-stationary continual learning setting it means like

### [26:35 - 26:40]

because we don't have it we're not um i mean the the main relaxation here right from the

### [26:40 - 26:45]

multitask setting is that we no longer assume access to a task id so if we don't have the

### [26:45 - 26:51]

task id it actually puts us in the partial observability setting so what this assumption

### [26:51 - 26:58]

is saying is really that um given a sufficient history or given some amount of history

### [26:59 - 27:06]

we can it is possible to infer what the context is and so i think another way of thinking about

### [27:06 - 27:10]

this is that we're really just making an assumption that we're in a k order mdp as

### [27:10 - 27:18]

opposed to like a true plumb dp where sort of like worst case is unboundedly bad um another

### [27:18 - 27:26]

nice result that comes from um older work is just this generalization via lipschitz continuity so

### [27:26 - 27:28]

basically if you have the

### [27:29 - 27:31]

if your learning algorithm has the property of being lipshits

### [27:32 - 27:37]

then um even if you're collecting data in the reinforcement learning way even

### [27:37 - 27:48]

even if you don't have the iid assumption um we can bound sort of the the generalization gap

### [27:50 - 27:56]

of this algorithm um and so this is a result that we can actually apply to our setting and so i and

### [27:56 - 27:58]

and uh we can only apply this to

### [27:59 - 28:04]

our setting because we are trying to um form a representation space that has the slipshots property

### [28:06 - 28:11]

another type of generalization bound which is now much more relevant for the reinforcement

### [28:11 - 28:16]

learning setting is is just again something that looks very similar to the kinds of bounds that

### [28:16 - 28:23]

we had in the hip bmdp setting um here just focusing on uh transfer across different

### [28:23 - 28:28]

contexts and so this looks the same as before it's just that we've now replaced theta with this kind

### [28:28 - 28:33]

context c and the c incorporates both differences in dynamics and reward

### [28:35 - 28:41]

so this gives rise to our our algorithm and i think like again if you were following along

### [28:41 - 28:46]

with the hip bmdp paper this looks very similar and the main difference is that instead of

### [28:46 - 28:55]

assuming access to task ids we are using the the the history uh in from our environment um

### [28:55 - 28:58]

and so we're using the interaction history in place of the task id

### [28:58 - 29:02]

um and yellow we're using the context industry um in place of that last us button

### [29:02 - 29:05]

and so i'm just a little joking but we're using that this is much more explicit this is in the

### [29:05 - 29:11]

contribution context but we're also exploring how to utilize um merge tool to find meaningful

### [29:11 - 29:14]

data and so along with the a hit bmdp transmission setup we're also swallow up that set so here

### [29:14 - 29:21]

is a sample of a sample of uh data for us to characterize um skip here to the h help me

### [29:21 - 29:26]

for email this is the context letters mais context by prefix where we can draw Deadland to

### [29:26 - 29:26]

feed into our context encoder we still have a very similar kind of context loss as we had in the hip bmdp setting um it just now uses the task metric which depends on dynamics and reward. We still need those same components of training like a dynamics loss and reward loss so that we can compute what this task metric is and then we can apply即 eractive critical on topic

### [29:26 - 29:30]

different types of settings. So one is non stationary dynamics.

### [29:30 - 29:33]

So this is the same set of environments that we had in hit

### [29:33 - 29:38]

the MDP setting, we now we're comparing against other sort of,

### [29:39 - 29:42]

like other kind of system identification methods that also

### [29:42 - 29:47]

don't assume access to the task ID. And we again, perform the

### [29:47 - 29:52]

same ablation here where our method Zeus. We also have Zeus

### [29:52 - 29:55]

no context loss. So we don't have that context objective in

### [29:55 - 29:58]

our context embedding space that we're constructing. And so

### [29:58 - 30:03]

we can see that our method performs much better than any of

### [30:03 - 30:08]

these other baselines and this ablation in red. And this also

### [30:08 - 30:11]

we don't have hit the MDP in here because it's not really a

### [30:11 - 30:16]

fair comparison because hippie MDP needs access to the task ID.

### [30:17 - 30:20]

But these do get much better generalization performance than

### [30:20 - 30:25]

hippie MDP as well. We can also now look at non stationary

### [30:25 - 30:25]

reward.

### [30:26 - 30:29]

And so we look at two environments here. This cheater

### [30:29 - 30:32]

run is different from the one on the previous slide. So this one,

### [30:32 - 30:38]

we just have different target velocities. And so here in both

### [30:38 - 30:42]

of these examples, in all of these experiments here, what

### [30:42 - 30:45]

we're looking at in terms of validation is is generalization

### [30:45 - 30:50]

to new unseen environments. So same baselines, same ablations,

### [30:50 - 30:54]

just now looking at non stationary reward. The other

### [30:54 - 30:55]

environment

### [30:55 - 30:59]

is just this Sawyer peg. And so it's just a Sawyer arm that has

### [30:59 - 31:05]

to insert this key into or this peg into into, into different

### [31:05 - 31:11]

holes. And so it's asked to at training time, it is training to

### [31:11 - 31:15]

insert this peg into a different hole at training time than a new

### [31:15 - 31:20]

unseen hole at test time. So we can see again, that Zeus is

### [31:20 - 31:23]

performs much better than all of these other environments. And

### [31:23 - 31:25]

you know, I think these are all like very standard type of

### [31:25 - 31:29]

like main result experiments. But I like this experiment a lot

### [31:29 - 31:35]

better. So we want to be able to interpret what kind of context

### [31:35 - 31:39]

embedding we've learned. And these kinds of more toy

### [31:39 - 31:43]

environments, because we know, because we've designed the

### [31:43 - 31:46]

environments, we do actually know what is the true latent

### [31:46 - 31:49]

variable, what is the thing that we're varying across these

### [31:49 - 31:55]

different tasks. So this is looking at that, that half cheetah

### [31:55 - 32:03]

the torso length changes. And these indices just represent the

### [32:03 - 32:09]

order of the torso length. So these task IDs really do have

### [32:09 - 32:13]

some structure in it in that task IDs that are closer

### [32:13 - 32:16]

together represent tasks that are also closer together in

### [32:16 - 32:22]

terms of names. So we see, so here, we're just plotting cosine

### [32:22 - 32:23]

similarity,

### [32:24 - 32:25]

in terms of the

### [32:25 - 32:28]

context embedding that we're learning. And so we can see this,

### [32:28 - 32:31]

this really nice, this is normalized, which is why it looks

### [32:31 - 32:36]

so nice between like zero and one. But we can see that the,

### [32:36 - 32:41]

the context space that we've learned, perfectly captures the

### [32:41 - 32:45]

true ordering of tasks, the true, the sort of like true

### [32:45 - 32:48]

ordering of the actual latent variable, which is the cheetah

### [32:48 - 32:52]

torso length. And we see that if we don't have that context loss,

### [32:52 - 32:54]

so this corresponds to that Zeus, no context, like the

### [32:54 - 33:00]

Zeus, no context loss ablation, there's some structure there,

### [33:00 - 33:05]

but it like the ordering is not preserved. And so I really like

### [33:05 - 33:09]

this, because it shows that we are able to in an unsupervised

### [33:09 - 33:16]

way, capture sort of meaningful information about the true

### [33:16 - 33:23]

context. So I think the takeaways from this paper are that

### [33:24 - 33:27]

we're now tackling the non stationary setting, the continual

### [33:27 - 33:30]

learning setting with this block contextual DP framework. And so

### [33:30 - 33:37]

this framework allows us to take RL algorithms that do that rely

### [33:37 - 33:40]

on this stationarity assumption, which I think of as like a very

### [33:40 - 33:44]

limiting one, and apply them to this new setting, we've proposed

### [33:44 - 33:48]

a method that can adapt to new unseen environments with zero

### [33:48 - 33:52]

shot generalization. And a nice thing about this method is that

### [33:52 - 33:53]

it doesn't require learning updates.

### [33:54 - 33:58]

In fact, just learning like an inference module that learns to

### [33:58 - 34:05]

detect what how things have changed, in comparison to

### [34:05 - 34:09]

environments that it has seen before. And it makes this method

### [34:09 - 34:14]

very amenable to safety critical settings where you can train a

### [34:14 - 34:19]

model, you can verify it, and then you can deploy it on new

### [34:19 - 34:24]

unseen environments and trust that it'll adapt in an expected

### [34:24 - 34:28]

ways. And so I think that that's sort of a crucial difference

### [34:28 - 34:34]

between this method and meta learning methods that do rely that

### [34:34 - 34:38]

do rely on having access to optimization updates at test

### [34:38 - 34:46]

time. So one major, I think, not surprising limitation is that we

### [34:46 - 34:49]

do still see that generalization degrades as we move further away

### [34:49 - 34:53]

from the training distribution. And so in this plot, we're just

### [34:53 - 34:54]

seeing that

### [34:54 - 34:58]

this is now on the half cheetah task where the reward is changing,

### [34:58 - 35:02]

so different target velocities. So we can see that as the target

### [35:02 - 35:05]

velocity gets higher moves further away from what it saw at

### [35:05 - 35:09]

training time, the performance of all methods, all these

### [35:09 - 35:13]

methods do degrade. But we're still able to obtain better

### [35:13 - 35:15]

performance than the other designs. But obviously, ideally,

### [35:15 - 35:19]

we want this to be flat, like we really want to have a method

### [35:19 - 35:22]

that truly can generalize, because we know that it should

### [35:22 - 35:23]

be capable of it.

### [35:24 - 35:29]

Okay, so final piece of work that I wanted to talk about, was

### [35:29 - 35:32]

still looking at this multitask setting, and still looking at

### [35:32 - 35:38]

context. But now looking at a different type of context, like

### [35:38 - 35:43]

what if you have useful site information? Examples of this are

### [35:43 - 35:46]

are like, what if you have access to instructions, right?

### [35:46 - 35:48]

Like you, you could have a command that's, that's, you

### [35:48 - 35:52]

know, like, go pour me coffee. But you can have a more

### [35:52 - 35:54]

informative version of that.

### [35:54 - 35:57]

Which is like, you know, you need to put the coffee pot in the

### [35:57 - 36:00]

coffee maker, you know, put in water, put in coffee grounds,

### [36:00 - 36:06]

etc. So and I think this is well, yeah, I have a slide later

### [36:06 - 36:08]

that talks about a little bit about NetHack. But I know that

### [36:08 - 36:11]

you guys are all very familiar with that setting. So I think

### [36:11 - 36:17]

NetHack is also sort of like a very intuitive example of of

### [36:17 - 36:21]

context aside information, right? Like the wiki is not needed in

### [36:21 - 36:22]

order to

### [36:24 - 36:29]

agent to explore the environment and to get reward. But it's it's

### [36:29 - 36:33]

very useful, and I think actually necessary. So the problem

### [36:33 - 36:36]

setting that we're focusing on in this paper is meta world. And

### [36:36 - 36:39]

I and I think it's useful to show this, because it'll give some

### [36:39 - 36:43]

intuition for the method. So meta world is the multitask

### [36:44 - 36:49]

benchmark, and it has MT 10 with just these 10 environments, and

### [36:49 - 36:51]

MT 50 with 50 environments.

### [36:54 - 36:59]

So it's a multitask setting. So they assume that you have access

### [36:59 - 37:04]

to a task ID. What they also give you are these short sentence

### [37:04 - 37:09]

descriptions of the tasks. These sentences were not meant to be

### [37:09 - 37:12]

part of the MVP. So it's never it's not supposed to be

### [37:12 - 37:15]

something that was given to the agent. The sentences were just

### [37:15 - 37:17]

provided for human consumption so that we could read these

### [37:17 - 37:20]

sentences and then exactly understand like what this task

### [37:20 - 37:23]

is without having to play around with the environment.

### [37:24 - 37:28]

And so if this if these short sentences can be useful for us,

### [37:28 - 37:31]

then it makes sense that they can also be useful for the agent.

### [37:32 - 37:35]

And so our method contextual attention based representation

### [37:35 - 37:36]

learning care.

### [37:38 - 37:42]

We just, this is just a way for us to incorporate the information

### [37:42 - 37:45]

in those sentences in a multitask pipeline.

### [37:46 - 37:52]

And the way we do that is we are training a mixture of K encoders.

### [37:52 - 37:53]

And I think like,

### [37:54 - 37:59]

a way to interpret what this is doing is that we want each of

### [37:59 - 38:02]

these K encoders to correspond to something interpretable that's

### [38:02 - 38:06]

shared across tasks. So in this meta world setting, you know, we

### [38:06 - 38:10]

can see that there are objects and skills that are shared

### [38:10 - 38:15]

across these tasks. There are multiple tasks with a puck that

### [38:15 - 38:20]

you're trying to push around to a goal, multiple tasks with a

### [38:20 - 38:22]

drawer and multiple tasks with a window.

### [38:24 - 38:27]

And also skills across these that are the same like open versus

### [38:27 - 38:32]

close versus push. And so I think like we can think of this mixture

### [38:32 - 38:35]

of K encoders, where each encoder corresponds to one of those

### [38:35 - 38:36]

objects or skills.

### [38:38 - 38:41]

So we have this mixture of representations, and we want to

### [38:41 - 38:45]

now learn a universal representation that's useful across all of our

### [38:45 - 38:49]

tasks. But the way that we combine these representations into this

### [38:49 - 38:53]

universal one will depend on the context. So we take our metadata

### [38:53 - 38:54]

here,

### [38:54 - 38:58]

which is just those natural language sentences, we use Roberta as a

### [38:58 - 39:02]

pre trained language model to turn those into an embedding.

### [39:03 - 39:09]

And we train a context encoding from that embedding. And we use

### [39:09 - 39:13]

that context encoding, that context encoding is used as input

### [39:13 - 39:17]

into an attention mechanism that dictates how these different

### [39:17 - 39:20]

representations are combined together. And so now we have a

### [39:20 - 39:23]

universal representation for which we can use a universal

### [39:23 - 39:24]

policy.

### [39:24 - 39:26]

So we can use a multi test algorithm in this multi test setting.

### [39:27 - 39:32]

And we basically find that we get state of the art results on

### [39:32 - 39:36]

meta world, we get better performance than any existing method on

### [39:36 - 39:40]

this benchmark, just from incorporating this metadata.

### [39:42 - 39:44]

So we have the baseline

### [39:47 - 39:52]

comparisons with multitask, sack, multitask sack with the task encoder,

### [39:52 - 39:53]

multi head sack.

### [39:53 - 40:00]

also other multitask methods again pc grad soft modularization which takes the same policy network

### [40:00 - 40:05]

and does different routing depending on the task to create different policies and we also

### [40:05 - 40:11]

incorporated film so film is like a general conditioning method for natural language

### [40:12 - 40:18]

and it's not was not meant for the reinforcement learning setting but we thought of this as sort

### [40:18 - 40:24]

of like a a useful baseline and so we just incorporated film with soft actor credit to

### [40:24 - 40:30]

see how well it performs in the reinforcement learning setting um and then we also have an

### [40:30 - 40:35]

upper bound so if we just train a single sack agent per task this is its performance and so

### [40:35 - 40:39]

we can see that there's still a small gap so there's still room for improvement but this

### [40:39 - 40:47]

could also have to do with um um parameterization right the fact that this given that

### [40:48 - 40:52]

we're training one sack agent per task this will have a lot more parameters than any of these other

### [40:52 - 40:59]

methods and so we have results for mt10 and mt50 um and we can see that we get better performance

### [40:59 - 41:05]

in all of these other baselines so an important question to ask here is because we have all of

### [41:05 - 41:13]

these like new components um is you know what is actually contributing to this better performance

### [41:13 - 41:17]

so we just look at these ablations on on both settings um

### [41:18 - 41:24]

we have soft actor credit soft actor critic with just the mixture of encoders so no metadata so it

### [41:24 - 41:31]

just gets passed in like a task id instead we have software critic with metadata but without the

### [41:31 - 41:37]

mixture of encoders and then the whole combination which is our method and so we can see that

### [41:39 - 41:43]

the metadata is definitely more important than the mixture of encoders but both

### [41:43 - 41:46]

things together is still better than everything else

### [41:48 - 41:52]

and and i you know it's the same kind of visualization as the last paper but i really

### [41:52 - 41:59]

like this um so here again we're looking at cosine similarity across like all of the tasks

### [41:59 - 42:05]

um the task embeddings um what we are showing here so in this first image we just have the

### [42:05 - 42:12]

pre-trained task embeddings or actually really what sorry i shouldn't have written task embeddings

### [42:12 - 42:17]

this is confusing this is just the embeddings out of roberta so this is just out of the

### [42:18 - 42:26]

language model and so we can see you don't even need to use roberta i think if you just treated

### [42:26 - 42:32]

the words as tokens you would see this same kind of similarity it's just that how many words in

### [42:32 - 42:37]

common do these different sentences have this corresponds to the cosine some of the like these

### [42:37 - 42:45]

tasks having more similarity but we see that when we use these language embedded these um

### [42:46 - 42:47]

this language embedding as

### [42:48 - 42:54]

input into our method and now we can look at our context embeddings at the end of training

### [42:56 - 43:02]

we can see that that structure persists and actually um for some of these tasks it actually

### [43:02 - 43:09]

gets even stronger so these areas in yellow that differ between these two are between 9 10 and 4 5 6

### [43:10 - 43:16]

so we can see that the things that these have in common are opening and closing doors and drawers

### [43:16 - 43:17]

and windows

### [43:18 - 43:19]

and so i think the really nice thing here is that

### [43:21 - 43:28]

our agent has discovered that opening and closing a door versus a drawer versus a window is very

### [43:28 - 43:32]

similar and even more similar than the sentences would have you could tell from the sentences

### [43:33 - 43:36]

and so we can see that this this similarity is leveraged

### [43:38 - 43:46]

in comparison if we just train care but without using the metadata as those embeddings we no

### [43:46 - 43:47]

similarity is found

### [43:48 - 43:54]

and so it means that having access to that metadata is really important for finding this similar

### [43:54 - 43:55]

structure across tasks

### [43:58 - 44:02]

um another experiment that we wanted to try was to see if we can get zero shot

### [44:02 - 44:06]

generalization to new unseen environments there's some hope that we can do this because of the

### [44:06 - 44:12]

compositional aspect um of of this environment you know the fact that like different objects

### [44:12 - 44:16]

and different skills like if you've learned these things separately maybe we can combine them

### [44:16 - 44:16]

together

### [44:18 - 44:23]

try this with mt10 we were very careful about picking like which which of the environments

### [44:23 - 44:27]

we train on and which were the two environments we test on so we're evaluating on drawer open

### [44:27 - 44:33]

and window open with the idea that it has learned how to open thing other things in the training

### [44:33 - 44:39]

tasks and it understands the dynamics of drawers and windows also from the training tasks

### [44:39 - 44:45]

um performance is pretty abysmal it's better than the other methods but obviously there's still a

### [44:45 - 44:51]

lot of room for improvement so i'm really excited about sort of trying to improve uh performance in

### [44:51 - 44:57]

in this aspect in terms of this kind of compositional generalization but i'm not

### [44:57 - 45:03]

sure yet how to do this so uh to conclude from this paper which is getting presented at icml

### [45:03 - 45:09]

this year i i think the main takeaways are site information is important if we can incorporate it

### [45:09 - 45:14]

in the right way we can dramatically improve performance we show that one way of doing this

### [45:14 - 45:15]

is through use of the tools that are available to us and the tools that are available to us and

### [45:15 - 45:18]

one way of doing this is through using this mixture of encoders that allows for positive transfer

### [45:18 - 45:23]

and i think a key question to ask is like how can we scale this up and so this is where net

### [45:23 - 45:29]

hack comes in um you know net hack has this wiki that that uh i think the thing that tim likes to

### [45:29 - 45:35]

say right is that no human has been able to solve net hack without reading the wiki uh without using

### [45:35 - 45:45]

the wiki um and so i i think there's huge problems um open problems here of how we can take something

### [45:45 - 45:51]

like care, which we show works in this very toy setting with just these very simple

### [45:51 - 45:58]

sentences, how we can apply something like that to NetHack. And for me, I guess like the things

### [45:58 - 46:04]

that I'm excited about, again, sort of tying these things back into applications, personalizing

### [46:04 - 46:09]

healthcare, treating each patient, you can treat each patient and patient information as context.

### [46:09 - 46:16]

And so through this, we can get, we can expect generalization to new patients, maybe who have,

### [46:16 - 46:23]

who have, who have different metadata or different information about their lives and their health.

### [46:24 - 46:29]

But we should be able to get compositional generalization to these patients. Same thing

### [46:29 - 46:33]

with household robots. We should be able to generalize to new environments and layouts.

### [46:33 - 46:37]

We should be able to generalize to new tasks just through like simple language instruction.

### [46:39 - 46:46]

And yeah, so in, in conclusion, I think sort of like the, the takeaways from this talk from,

### [46:46 - 46:53]

from these three papers is that I think leveraging structure will improve generalization. Context

### [46:53 - 47:01]

is a way to convey the structure that exists in the environment, both either as metadata or learned

### [47:01 - 47:07]

from just like the dynamics and context comes in different forms. It can be just like the history

### [47:07 - 47:09]

and the environment. It can be,

### [47:09 - 47:17]

natural language. It can be video, video demonstrations. And yeah, so I think this

### [47:17 - 47:21]

is something that would be really interesting to sort of, to discuss and learn also from the

### [47:21 - 47:26]

things that you guys are working on, sort of like what are other forms of context? What are

### [47:26 - 47:32]

interesting applications of these kinds of works? And then obviously I, none of this work would be

### [47:32 - 47:36]

possible without my collaborators. So these are just the people that I worked with on these three

### [47:36 - 47:39]

papers. And yeah, so now I'm,

### [47:39 - 47:43]

I'm really happy to take any questions or comments from people.
