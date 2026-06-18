# [OOD Workshop@CoRL 2023] Amy Zhang - Leveraging Structure and Abstractions for OOD Generalization

- URL: https://www.youtube.com/watch?v=KyURDq7rkuU
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T20:47:34`

## Transcript

### [00:00 - 00:10]

All right. Welcome back, everyone, to the workshop.

### [00:10 - 00:15]

So we have a couple of really exciting invited talks in our next session.

### [00:16 - 00:17]

So the first talk will be by Amy Zhang.

### [00:17 - 00:23]

So Amy is an assistant professor at UT Austin in the Department of Electrical and Computer Engineering.

### [00:24 - 00:28]

Her group works on improving robustness and generalization for reinforcement learning agents.

### [00:28 - 00:36]

And today she will be talking about how we can leverage structure and abstractions for improved OOD generalization in reinforcement learning.

### [00:36 - 00:38]

So Amy, whenever you're ready, take it away.

### [00:39 - 00:41]

Awesome. Thanks, Ani, for the introduction.

### [00:41 - 00:46]

And thank you for the organizers for organizing a workshop on such an important topic.

### [00:47 - 00:49]

All right. So I'm just going to jump right in.

### [00:50 - 00:55]

You know, I think for OOD generalization, we all understand that there's no free lunch, right?

### [00:55 - 00:58]

If we expect generalization, that means we're assuming some type.

### [00:58 - 01:01]

Of structure underlying in our problem.

### [01:01 - 01:11]

So today I want to talk about two, I would say, fairly general forms, fairly relaxed types of assumptions of structure that we can make.

### [01:12 - 01:21]

The first is, is this notion of compositionality that our environment is made up of underlying common independent factors.

### [01:21 - 01:27]

And so we can expect generalization to new versions of the environment where there are

### [01:28 - 01:36]

maybe, maybe different compositions of factors, or we see the same factors, but in kind of like different scenarios.

### [01:37 - 01:43]

And I think that's a bit more specific than the kind of like next assumption that I'm going to make.

### [01:43 - 01:50]

So in the final two works that I'm going to talk about today, we're just going to focus on structure that exists in goal conditioned problems in general.

### [01:50 - 01:58]

And by goal conditioned, I just mean tasks where our goal is a specific state that we would like to reach.

### [01:58 - 02:04]

All right. So with that I'm just going to jump right in and talk about structure and compositionality.

### [02:04 - 02:09]

So before I do that, I want to talk a little bit about what compositionality means right?

### [02:09 - 02:17]

Like. what? What is the set of the underlying assumptions that we're making when we talk about compositionality or compositional generalization?

### [02:17 - 02:22]

So, in RL. You know, we typically deal with simulators, but I think a lot of this applies to robotics as well.

### [02:22 - 02:23]

you know, in block stacking or in proc gen, which is this nuances that we're using today, we really like to go through more of this også in

### [02:23 - 02:24]

At you might be looking at, like a little definition sniff image.

### [02:24 - 02:24]

Or you might be thinking well, we would, we'll talk about things like aha.

### [02:24 - 02:25]

reduce?

### [02:25 - 02:25]

For like regime changes, which is the size distribution of graphics earlyevnding modeling also, you know.

### [02:25 - 02:25]

Stberly it's still common.

### [02:25 - 02:34]

you know in block stacking or in procgen which is this this uh set of uh compositionally generated

### [02:34 - 02:41]

environments um in simulators for autonomous driving um and but then this also applies to

### [02:41 - 02:49]

real world scenarios right like uh say loading or unloading a dishwasher or navigating in a

### [02:49 - 02:56]

warehouse and manipulating boxes and objects in a warehouse scene all of these have underlying

### [02:56 - 03:03]

components um that we can become very familiar with and therefore generalize to new environments

### [03:04 - 03:11]

with different configurations of those factors right so um i think that factorization is a way

### [03:11 - 03:17]

like by by discovering these factors or utilizing these factors in these environments is a way for

### [03:17 - 03:19]

us to achieve compositional

### [03:19 - 03:26]

generalization and i i think the notion of compositional generalization is something that

### [03:27 - 03:34]

other subfields have actually explored a lot more than we have um and so this figure is is actually

### [03:34 - 03:40]

from this really nice paper called compositionality decomposed how do neural networks generalize

### [03:40 - 03:45]

and this is focusing on compositional generalization in language actually rather than

### [03:45 - 03:48]

robotics and uh they

### [03:49 - 03:55]

have this really nice figure that defines these five types of generalization that we can expect

### [03:56 - 04:03]

um so one is systematicity generalization first via systematically recombining known parts and rules

### [04:03 - 04:08]

productivity the ability to extend predictions beyond the length seen in training data

### [04:08 - 04:13]

substitutivity generalization via the ability to replace components with synonyms

### [04:14 - 04:18]

localism if model decomposition or if model composition

### [04:19 - 04:25]

operations are local versus global, like if the rules are local versus global. And then

### [04:25 - 04:32]

overgeneralization, which is more of a trait, right? If models pay attention to or are robust

### [04:32 - 04:39]

to exceptions to rules, right? So I think a lot of these we can see can apply to robotics, but

### [04:39 - 04:45]

maybe not necessarily all of them. But I think there's already some related concepts that we

### [04:45 - 04:50]

use in RL to define MDPs that have this type of structure as well. And one example is the

### [04:50 - 04:56]

relational MDP, right? So a relational MDP family can be described by a set of classes that denote

### [04:56 - 05:02]

different types of objects, a set of function schemata that takes those objects as inputs.

### [05:02 - 05:09]

And so these can be transformations to those objects or actions that you can take for some

### [05:09 - 05:15]

objects and maybe not others. Oh, sorry. Actually, the action specifically is the set of action

### [05:15 - 05:15]

schemata.

### [05:15 - 05:24]

And then for a specific domain, for a specific environment, we can talk about a set of domain

### [05:24 - 05:31]

objects. And each of those objects come from a specific type or a specific class from C.

### [05:31 - 05:36]

And then we have our standard transition function and reward model, right? So you can see how

### [05:36 - 05:42]

this is a slight modification of the standard MDP definition that takes into account kind of

### [05:42 - 05:45]

common factors across domains. All right.

### [05:45 - 05:54]

So how can we leverage factorization in problems that have them, maybe specifically in robotics?

### [05:54 - 06:00]

And so in this paper from ICLR that we presented this year, we presented this method called neural

### [06:00 - 06:05]

constraint satisfaction, which marries the strengths of non-parametric planning with

### [06:05 - 06:11]

object-centric representations. And so the main contribution of this work was to show that

### [06:11 - 06:15]

by factorizing the traditionally monolithic entity representation,

### [06:15 - 06:21]

into a set of action invariant features, the object type, and action-dependent features,

### [06:21 - 06:27]

its state, then we can reuse these components during planning and control.

### [06:28 - 06:34]

All right. So to implement this factorization, NCS first constructs a two-level hierarchy,

### [06:34 - 06:39]

which abstracts the experience buffer into a graph over state transitions of individual entities,

### [06:39 - 06:45]

right, separated from other contextual entities. So to solve new arrang- and so,

### [06:45 - 06:51]

this is specifically focused on object rearrangement. And so to solve new or rearrangement problems,

### [06:51 - 06:57]

NCS infers what state transitions can be taken given the current and goal image observations,

### [06:57 - 07:01]

and recomposes sequences of state transitions from the graph and translate these transitions

### [07:01 - 07:09]

into actions. So the first problem that comes up is the correspondence problem of how we can abstract

### [07:09 - 07:15]

these raw sensory motor signal, which in our case is this high-dimensional observation space,

### [07:15 - 07:22]

pixels, into representations of entities such that there's a correspondence between how an agent

### [07:22 - 07:25]

intervenes on an entity and how its action affects an object in the environment, right.

### [07:26 - 07:33]

And so the very first step is actually extracting out what an entity is. And we can actually do this

### [07:33 - 07:42]

using self-supervised object detection methods. And the idea being that these methods already do

### [07:42 - 07:44]

kind of like the, the kind of like,

### [07:45 - 07:51]

like already exhibited desired property, which is that it determines what pixels are correlated

### [07:51 - 07:58]

across a data set of images and encompasses that into a specific factor, right, into a specific

### [07:58 - 08:06]

entity. And so then once we've discovered these entities and mapped them across different images

### [08:06 - 08:10]

or across different frames or across different states in a trajectory, then we can start using

### [08:10 - 08:14]

them as abstractions. So the second part of this problem

### [08:15 - 08:20]

is the combinatorial one, which is how do we actually represent this combinatorial task space

### [08:20 - 08:25]

in a way that allows us to get this type of generalization across different domains where

### [08:25 - 08:31]

we have different objects or different numbers of objects or combinations of objects in these

### [08:31 - 08:38]

different domains, right. And the point that we leverage in this paper is that the same state

### [08:38 - 08:42]

transition can manifest for different objects and in different contexts, right. So if we're only

### [08:42 - 08:45]

focusing on a specific target object in this image,

### [08:45 - 08:53]

this pink object, this pink cube, it doesn't matter what's going on with any of the other

### [08:53 - 09:00]

objects in this scene, right, which means that we can now generalize to like use this transition or

### [09:02 - 09:07]

leverage this transition in a different version of this environment where there

### [09:07 - 09:09]

are other additional objects or objects that have been removed.

### [09:12 - 09:13]

Okay.

### [09:14 - 09:15]

So NCS

### [09:15 - 09:19]

instructs a two-level abstraction hierarchy to model transitions in the experience buffer,

### [09:19 - 09:25]

right. So in the first, NCS learns to infer a set of energies from sensory motor transitions

### [09:25 - 09:32]

with pick and move options, so actions. So we're assuming a very high-level action space where an

### [09:32 - 09:37]

entity is moved per transition. So we don't necessarily need to do this. We can learn these

### [09:37 - 09:43]

abstractions using lower-level action spaces, but it just means that it would require multiple steps

### [09:43 - 09:45]

of moves. And so it was much

### [09:45 - 09:50]

simpler to first kind of think of each of these transitions as only taking a single action rather

### [09:50 - 09:56]

than having to account for multiple actions or learn abstractions of skills, right.

### [09:57 - 10:03]

And then our dynamics model can learn to sparsely predict the states shown with the different

### [10:03 - 10:08]

textures in this figure of the entities at the next time step, right. And so this addresses the

### [10:08 - 10:13]

correspondence problem by forcing the network to predict and reconstruct observations through an

### [10:13 - 10:15]

entity bottleneck. And so this way we can kind of keep

### [10:15 - 10:18]

track of the same objects throughout a trajectory.

### [10:19 - 10:24]

So once we have these entities and these one-step transitions of how these entities are moving

### [10:24 - 10:32]

within a trajectory, we can now build a graph. And how this graph is different from prior works

### [10:32 - 10:38]

is that instead of building a graph where nodes corresponds to the entire state, right, where now

### [10:38 - 10:44]

the state is unique to a domain, where a domain kind of like represents the number and combination,

### [10:45 - 10:53]

a specific set of objects, we're now constructing a per-entity graph, where a graph just shows how

### [10:53 - 11:02]

a single abstract object type moves around, where we can now kind of group together all of the

### [11:04 - 11:09]

versions of that entity across all the different trajectories, across all the different domains

### [11:09 - 11:15]

that we have in our dataset. And so we can do this by clustering these entity transitions,

### [11:15 - 11:18]

expressions that share similar initial states and final states. So,

### [11:18 - 11:22]

this is one way in which we can kind of aggregate all of the information that

### [11:22 - 11:27]

we have about abstract entities in our dataset across different domains.

### [11:28 - 11:36]

And so now we can actually figure out how to use this for planning and control, right.

### [11:37 - 11:44]

So, given a rearrangement problem, specified only by a current observation and a goal observation, we can now

### [11:45 - 11:55]

this rearrangement problem into a sub problem per entity all right so um for so the first step is to

### [11:55 - 12:01]

run this self-supervised object detection method on our new domain and then randomly select an

### [12:01 - 12:08]

entity from our domain and uh search in our graph how to move it from its current location to the

### [12:08 - 12:14]

goal location right and now we can do this independently per entity we can look up the

### [12:14 - 12:21]

action which is just an edge in our graph and if there is a failure um basically you know if we

### [12:21 - 12:29]

have like a block stacking scenario where uh we can't move say like a lower uh a lower block in

### [12:29 - 12:35]

a stack then we can try and fail on that entity and then pick another entity and try again right

### [12:35 - 12:42]

so basically with enough of these random selections of entities we know that we'll pick

### [12:42 - 12:44]

we'll find the right ordering

### [12:44 - 12:49]

of movements for entities so that we can actually solve uh block stacking examples as well

### [12:51 - 12:59]

all right so um in the figure on the top left we can see this is a partitioning of states from the

### [12:59 - 13:05]

training set into equivalence classes so the nodes represent um these equivalence classes over states

### [13:05 - 13:13]

right so this is specifically a clustering of states inferred from uh uh um the RoboGem simulation

### [13:14 - 13:21]

uh where we've created this rearrangement uh task so we have a library of objects that we randomly

### [13:21 - 13:27]

select from to create a to create each domain and then these clusters just represent the abstract

### [13:27 - 13:34]

entities that we've extracted out and then these slot attention masks are just averaged over all of

### [13:34 - 13:40]

the entities in this cluster so you can see that that what we're actually uh the information that

### [13:40 - 13:43]

we're taking away from those observations just corresponds to the object location

### [13:44 - 13:52]

because for pick and place action space uh the action is determined only by the location of the

### [13:52 - 14:01]

object so just from the um actions the transitions that we have in our data set and um this slide

### [14:01 - 14:06]

attention based method we've extracted that the only information that we care about in this

### [14:06 - 14:12]

environment and with this action space is the location of the object all right and so this table

### [14:12 - 14:13]

or these tables

### [14:14 - 14:20]

just compare our method ncs with various baselines on both complete and partial evaluation settings

### [14:20 - 14:25]

so partial evaluation just corresponds to the setting where we don't necessarily have an entire

### [14:25 - 14:32]

goal image of uh the kind of like final required placement of all objects and we only have say a

### [14:32 - 14:38]

partial specification that certain objects have to be in certain goal locations so these objects

### [14:38 - 14:43]

were trained um sorry these methods were trained on four objects and evaluated on

### [14:44 - 14:51]

the ability to generalize to four five six and seven objects and we report the fractional success

### [14:51 - 14:56]

rate as well as standard error computed over 10 seeds and so we see that across a lot of these

### [14:56 - 15:04]

methods um you know reinforcement learning based methods behavior cloning based methods MPC um

### [15:04 - 15:09]

they're not really able to perform very well in these settings and don't really generalize across

### [15:09 - 15:13]

different numbers of objects whereas we're able to achieve much better performance and

### [15:14 - 15:17]

there's obviously still a lot of room for improvement we actually find that a lot of

### [15:17 - 15:23]

this performance gap is actually caused by errors in each of the steps in this process right so if

### [15:23 - 15:29]

we have some error in our slot attention for extracting out entities or if there is an error

### [15:29 - 15:37]

in terms of pick and place so it's it's not magic we're actually using uh a controller to to actually

### [15:37 - 15:43]

perform pick and place and so there are some stochasticity in our transitions um so all of

### [15:44 - 15:51]

these methods contribute to lower performance in these in terms of these success rates all right

### [15:53 - 15:59]

um so I want to move on now to talk about just general goal condition problems right and so

### [15:59 - 16:04]

um in this work we specifically focus on the fact that there is geometric structure that

### [16:04 - 16:11]

exists in goal conditioned um RL problems right and so you know this is just a graphic kind of

### [16:11 - 16:13]

showing like what I mean by goal condition problems

### [16:14 - 16:19]

um and so we're just trying to find an optimal goal reaching value function for some target MDP

### [16:20 - 16:28]

so it turns out that this uh optimal goal reaching value function is a quasi metric and we actually

### [16:28 - 16:33]

have a theoretical result in our paper that shows that the set of all possible optimal value

### [16:33 - 16:40]

functions is exactly the set of quasi metrics so every quasi metric corresponds to um an optimal

### [16:40 - 16:43]

value function for some MDP with some Dynamics

### [16:44 - 16:49]

uh and vice versa right every optimal value function for any MDP is also a quasi metric

### [16:49 - 16:55]

and the thing to point out uh is that the reason we're focusing on goal condition problems here is

### [16:55 - 16:59]

that this type of structure doesn't exist in single task RL right so this is specific to

### [16:59 - 17:08]

goal reaching where our goal space is the same as our state space all right so given that so

### [17:08 - 17:13]

we're again kind of assuming that we have this offline data set um or replay buffer of transitions

### [17:14 - 17:20]

where we can sample these transitions from a replay buffer we can sample random states and

### [17:20 - 17:29]

random goals to specify some task and we introduce quasi metric RL which optimizes a quasi metric

### [17:29 - 17:36]

embedding as a negated value function right so now we're just saying we are imposing a a

### [17:36 - 17:42]

constraint on our value function we're imposing a constraint on the architecture of our value function

### [17:42 - 17:43]

so that it has to be a

### [17:44 - 17:49]

quasi metric right and the to just to remind the audience the difference between a quasi metric and

### [17:49 - 17:55]

a metric is just that a quasi metric does not insist that the distance function between distinct

### [17:55 - 18:00]

elements S and G is commutative right so if we were to use a standard metric for learning a value

### [18:00 - 18:07]

function which we've done in our own prior work it basically is incorporating an additional assumption

### [18:07 - 18:13]

that your Dynamics and your MDP are reversible which in a lot of safe settings is true you know

### [18:13 - 18:13]

so if we're

### [18:13 - 18:20]

thinking about um just moving objects around on a tabletop where you kind of have a border around

### [18:20 - 18:27]

your uh your your play area then this is the setting where Dynamics are pretty much reversible

### [18:27 - 18:33]

but if you have an object fall off the edge of your table then that's not something that we can

### [18:33 - 18:39]

easily recover from right by taking the reverse of an action um so in that case our our Dynamics

### [18:39 - 18:43]

are clearly not reversible and this is a setting in which um enforcing our value function

### [18:43 - 18:47]

to be a quasi metric makes a lot of sense all right

### [18:49 - 18:57]

so um we first have some toy experiments uh in this mountain car setting and so this is basically

### [18:57 - 19:04]

the simplest setting that we could imagine where our Dynamics are clearly not reversible right so

### [19:04 - 19:09]

you know this this mountain car can try to climb up this hill but as soon as it stops

### [19:09 - 19:12]

it's going to roll back down right so the Dynamics are not the same in both directions

### [19:13 - 19:24]

um so here we can just see uh the ground truth Dynamics of our system right um and then we see

### [19:24 - 19:31]

what we the optimal value function um sorry this is a visualization of the optimal value function

### [19:31 - 19:39]

for different goal points in this Hill in this Hill environment as well as what we learn with QRL

### [19:40 - 19:43]

as well as a comparison to what standard

### [19:43 - 19:48]

is learning. So this imposes no constraints on our Q function. It's just a neural network,

### [19:49 - 19:54]

so it's a universal function approximator, as well as some other methods, so conservative

### [19:54 - 20:00]

Q learning and contrastive RL. And then this is an example of our QRL objective,

### [20:00 - 20:06]

where instead of imposing that our value function is a quasimetric, we instead just

### [20:06 - 20:11]

impose that it's a metric. It's just L2 distance in some latent representation space.

### [20:13 - 20:22]

Okay, cool. All right. So on the left-hand side for all of these figures, we have

### [20:22 - 20:28]

just the ground truth distances, as well as the expected distance for the behavior policy that

### [20:28 - 20:32]

generated the data set. And then these are kind of all of the learned versions, right? So we can

### [20:32 - 20:37]

see by just doing a visual comparison between ground truth and our learned Q functions,

### [20:37 - 20:41]

that QRL is the one that is really capturing

### [20:41 - 20:43]

the same thing.

### [20:43 - 20:45]

The same structure that exists in the ground truth Q function.

### [20:48 - 20:55]

All right. So QRL learns an optimal decision-aware representation, right? So we can kind of like

### [20:55 - 21:01]

think of this quasimetric space that we're learning. So we're learning this D latent

### [21:01 - 21:08]

that should just correspond to the optimal state reaching cost. All right.

### [21:12 - 21:13]

And so then now we can see that the Q function is a quasimetric space.

### [21:13 - 21:16]

So we can actually use this quasimetric for downstream control.

### [21:20 - 21:27]

All right. So we have some additional experiments benchmarking QRL, again, just in the offline RL

### [21:27 - 21:32]

setting. So the first is this maze 2D environment where we just need to guide a ball through a maze

### [21:32 - 21:36]

towards a target location. We have different versions of this maze.

### [21:39 - 21:43]

And QRL can learn this policy network by just backcropping

### [21:43 - 21:43]

the Q function. So we can see that the Q function is a quasimetric space.

### [21:43 - 21:50]

All right. So we have results on this for the single goal, as well as multi-goal setting

### [21:50 - 21:57]

across different configurations of mazes, large, medium, and new maze. And we compare again against

### [21:57 - 22:06]

contrastive RL, MSG, which is a gradient-based approach. I actually don't remember what MSG

### [22:06 - 22:10]

stands for, but MSG combined with hindsight experience replay, as well as planning-based

### [22:10 - 22:13]

methods, MPPI, and then decision-based approach. So we can see that the Q function is a quasimetric

### [22:13 - 22:14]

area, and then decision-based approach. So I can see that the Q function is a quasimetric area,

### [22:14 - 22:14]

and then decision-based approach. So we can see that the Q function is a quasimetric area,

### [22:14 - 22:16]

and then decision-based approach. So this is more of a trajectory modeling

### [22:16 - 22:20]

approach, and then diffuser with a hand-coded controller, right?

### [22:20 - 22:26]

So one problem with diffuser is that it does a good job of generating kind of like a trajectory

### [22:26 - 22:31]

of states that you should follow, but doesn't do as well with predicting those actions correctly.

### [22:32 - 22:37]

And so we actually achieve much better performance by incorporating a hand-coded controller. So

### [22:37 - 22:43]

having a separate method for learning the actions, for extracting actions given a goal state,

### [22:43 - 22:49]

and so we see much better performance in this column compared to just straight diffuser so

### [22:49 - 22:56]

these scores represent average normalized episodic return where 100 represents comparable performance

### [22:56 - 23:04]

with a d4l reference a hand-coded controller right and so again we can kind of see that QRL

### [23:04 - 23:08]

is able to outperform all these other methods and is able to achieve better sample efficiency

### [23:08 - 23:13]

and generalization performance because it's leveraging this geometric structure that exists

### [23:13 - 23:17]

in the goal conditioned RL problem

### [23:21 - 23:28]

so we also evaluate QRL in an online setting so in for the online setting we again kind of use

### [23:28 - 23:36]

this robo gym environment and so here the robot is just trying to push say push a block right

### [23:36 - 23:43]

and so now we're also focusing on continuous action spaces all right and so here for the

### [23:43 - 23:43]

online level there's a depend-on platform here i'm going to show you how it works here so here

### [23:43 - 23:43]

there's a depend-on platform here i'm going to show you how it works here

### [23:43 - 23:49]

learning setting, we're comparing again against contrast of RL, goal condition behavior cloning,

### [23:50 - 23:59]

DDPG plus HER, DDPG plus HER plus the quasi-metric, and I guess two different

### [23:59 - 24:05]

types of quasi-metric methods. And so again, we can kind of see that QRL learns faster and better

### [24:05 - 24:09]

compared to baseline methods across all environments for both state-based and

### [24:09 - 24:15]

image-based observations. All right, so that's kind of just showing that there is this geometric

### [24:15 - 24:20]

structure that exists in goal-conditioned RL problems, and by leveraging that, by incorporating

### [24:20 - 24:27]

that structure into the architecture of our value function, we can achieve better performance across

### [24:27 - 24:33]

a gamut of goal-conditioned RL problems, or goal-conditioned robotics problems. So there's

### [24:33 - 24:38]

kind of one additional thing that we can also do in the goal-conditioned setting that is instead

### [24:38 - 24:39]

related to just

### [24:39 - 24:45]

richer learning signal. So one problem with the goal-conditioned RL problem, kind of like why it's

### [24:45 - 24:53]

so hard, is that the standard reward function that we use is very sparse, right? So usually we assume

### [24:53 - 24:57]

that we're not getting any reward from the environment until we actually reach the goal

### [24:57 - 25:03]

state, in which case we receive a reward of one, right? And so learning goal-conditioned policies

### [25:03 - 25:08]

under the sparse reward is very difficult. So I just want to first introduce

### [25:08 - 25:09]

the

### [25:09 - 25:19]

F-divergence as a way of matching distributions. So F-divergence is a notion of distance between

### [25:19 - 25:30]

probability distributions. And so here's just kind of a graphic showing what divergence between two

### [25:30 - 25:39]

probability distributions looks like as those distributions change over time. And so you can kind of think of these as just

### [25:39 - 25:55]

different notions of distance. They're just different. They're just different notions of distance, right? Like they both get larger if the distributions move further away. They all get smaller if the distributions become closer. But the rate at which they do, like what value they take can

### [25:55 - 26:09]

be different, right? And so there are many different F-divergences that we can use, and we do find kind of like different performance when using different F-divergences. But I think the main thing to take away from this slide is that depending on the dynamics,

### [26:09 - 26:17]

of your system, depending on how the probability distributions over states changes in your

### [26:17 - 26:23]

environment, different divergences can get better or worse performance. So it really kind of just

### [26:23 - 26:32]

depends on your dynamics. But so just to dive right in, we propose this method called F policy

### [26:32 - 26:41]

gradients. And our policy is learned by minimizing a slightly different objective than what the

### [26:41 - 26:48]

standard goal condition RL objective is, right? So our objective here is to minimize the F

### [26:48 - 26:56]

divergence between our current state occupancy exhibited by our current policy and our goal,

### [26:57 - 27:02]

right? So P theta is the agent state visitation distribution, and PG is the

### [27:02 - 27:02]

distribution of the state visitation distribution. And so we're going to

### [27:02 - 27:10]

So we could actually do this for any kind of reinforcement learning, any kind of robotics,

### [27:10 - 27:17]

any kind of control problem. But in most settings, assuming that we have access to this distribution

### [27:17 - 27:22]

over the goal space is a pretty restrictive assumption, except in the goal condition setting

### [27:22 - 27:27]

or imitation learning settings, right? When we have access to demonstrations, because in both

### [27:27 - 27:31]

of these settings, we actually do have access to the distribution over the goal. In the goal

### [27:31 - 27:32]

condition setting, we have access to the distribution over the goal. And in the goal

### [27:32 - 27:35]

condition setting, it's easy because it's just a direct function, right? Like, it's just a delta

### [27:35 - 27:41]

right at the goal state. And then in imitation learning or learning from demonstration settings,

### [27:42 - 27:49]

if we're given a set of demonstrations, then we're kind of, we're given a sampling from PG,

### [27:49 - 27:53]

which we could use to compute the distribution over the goal space. All right.

### [27:56 - 28:02]

All right. So, okay, I kind of covered this already. So we want to the agent to be,

### [28:02 - 28:06]

by minimizing this F divergence, we just want our agent to be at the goal state with high

### [28:06 - 28:12]

probability. And so this is, we show in our paper that this is equivalent to the standard goal

### [28:12 - 28:19]

conditioned RL objective. We show that this objective does produce the optimal policy.

### [28:19 - 28:25]

And it turns out that we can optimize for this objective by taking the gradient. So we actually

### [28:25 - 28:29]

derive the analytical gradient for the F divergence. And it turns out that this looks

### [28:29 - 28:32]

very similar to a policy gradient, where the gradient is the same as the F divergence. So we

### [28:32 - 28:41]

gradient of log probabilities of the policy are weighted by this term F prime, right? And I think

### [28:41 - 28:46]

one thing I want to point out is that this dense weight is not a reward because it's non-stationary.

### [28:46 - 28:52]

It depends on the current policy. So we can't call this a reward function. Instead, it's because it's

### [28:52 - 28:57]

non-stationary, we can maybe call it an intrinsic reward, but we're just calling this learning

### [28:57 - 29:01]

signal, right? So it's a richer learning signal. It's a dense learning signal that we have access

### [29:01 - 29:01]

to.

### [29:02 - 29:07]

In any goal conditioned RL problem. And I just want to point out one additional thing, which is

### [29:07 - 29:14]

we could actually call this MaxEnt RL. This is different from the standard definition of MaxEnt

### [29:14 - 29:19]

RL, which is just saying, I want to learn an optimal policy that has the highest entropy,

### [29:19 - 29:24]

where the entropy is being computed on the policy's action distribution, just in a single

### [29:24 - 29:31]

step, right? I think this is actually a better form of MaxEnt. And so we actually call this

### [29:31 - 29:32]

state.

### [29:32 - 29:37]

MaxEnt, where we're actually learning a policy that is maximizing entropy over the state

### [29:37 - 29:46]

distribution, right? So it basically, until we start extracting learning signal by knowing where

### [29:46 - 29:53]

the goal is, this learning objective is just going to learn a very exploratory policy that

### [29:53 - 30:01]

just tries to put discovery, discover every state in our state space. All right.

### [30:02 - 30:09]

And so maximizing, basically, we find that maximizing the entropy, sorry, maximizing this

### [30:09 - 30:15]

objective ensures exploration in a way that the standard MaxEnt definition of maximizing the

### [30:15 - 30:24]

entropy of the policy does not. All right. So it also turns out that this objective looks a lot

### [30:24 - 30:28]

like existing metric-based shaping rewards. So depending on the F divergence that you do,

### [30:28 - 30:31]

this can look a lot like a,

### [30:32 - 30:38]

a richer learning signal, just using, say, like L2 distance between your current state and your

### [30:38 - 30:48]

goal, or a temporal, like, reachability distance. All right. And so we have examples of what this

### [30:48 - 30:52]

looks like in grid world settings, which is really nice, because you can actually see how the state

### [30:52 - 30:58]

occupancy of the policy changes over time. We also scale up to more complex domains,

### [30:59 - 31:01]

including these maze configurations,

### [31:02 - 31:07]

as well as fetch reach. And I think the thing I just want to point out from these results are that

### [31:07 - 31:14]

we are able to achieve, we have much stabler performance, right? We achieve higher success

### [31:14 - 31:21]

rates, but we also have lower variance compared to existing methods. And with that, I want to

### [31:21 - 31:26]

conclude. I know I'm running over on time already, but I kind of just want to end with some open

### [31:26 - 31:32]

questions. Do existing benchmarks test all the forms of generalization that we care about?

### [31:32 - 31:35]

And I think the answer here is no. And so maybe we can discuss this a little bit more later.

### [31:36 - 31:40]

Are these assumptions the right level of granularity, right? Or are there others

### [31:40 - 31:45]

that are useful for other types of problems? You know, this is only a couple of possible

### [31:45 - 31:49]

assumptions that we can make. And I'm sure that there are others that are very interesting for

### [31:49 - 31:56]

a lot of robotics problems that we care about. And I would love to see, you know, how we can leverage

### [31:56 - 32:01]

these new and different assumptions for better generalization. And with that, thank you very much.

### [32:02 - 32:03]

Do we need to take any questions?

### [32:03 - 32:14]

We're just going to switch the audio and then open it up for questions.

### [32:14 - 32:28]

Hi. Can you hear us, Amy?

### [32:28 - 32:29]

Yes.

### [32:29 - 32:30]

Perfect.

### [32:30 - 32:31]

Hi.

### [32:31 - 32:32]

Hi.

### [32:32 - 32:36]

Thanks for the great talk. I guess my question was for the last part,

### [32:36 - 32:40]

how do you decide which divergence to use?

### [32:41 - 32:44]

Sorry, I didn't actually catch the question.

### [32:44 - 32:50]

For the last part, how to decide what F divergence metric to use?

### [32:50 - 32:56]

Yeah, that's a great question. I don't have a lot of intuition actually for what properties

### [32:56 - 33:01]

of different dynamics of different MDPs correspond better to different F divergences.

### [33:02 - 33:07]

So in our experiments, we did find that different F divergences led to different performance.

### [33:07 - 33:11]

Unfortunately, I don't have a more coherent answer than that.

### [33:11 - 33:16]

take one more question from the audience

### [33:23 - 33:27]

so actually maybe I can ask a question so on the the first part of the the talk

### [33:27 - 33:32]

um I was wondering if there's some kind of story about causal inference like did you

### [33:32 - 33:37]

interpret what you're doing and learning causal models that you can kind of do interventions on

### [33:37 - 33:41]

and that leads to compositional generalization or is that not kind of how you think about it

### [33:41 - 33:51]

yeah um so I think that so um yes I I think that what we're in effect kind of building is

### [33:51 - 33:57]

a causal graph um you know I I think to push the causal inference envelope further we should also

### [33:57 - 34:02]

be talking about counterfactuals performing interventions in the environment and we were

### [34:02 - 34:06]

doing this in an offline setting so in some sense like we don't have any interventional data so

### [34:06 - 34:11]

we're not really doing causal inference but I think that uh you know there are extensions

### [34:11 - 34:16]

of that work where we can make that that uh connection more closely but yeah that's a

### [34:16 - 34:22]

great question thank you all right thanks so we'll move on to the next talk thank you

### [34:28 - 34:29]

all the audience
