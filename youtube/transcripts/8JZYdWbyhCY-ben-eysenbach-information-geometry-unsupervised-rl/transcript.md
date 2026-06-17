# The Information Geometry of Unsupervised Reinforcement Learning

- URL: https://www.youtube.com/watch?v=8JZYdWbyhCY
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T15:11:44`

## Transcript

### [00:00 - 00:07]

I'm excited to share some recent work that provides some of the first analysis about when and where unsupervised skill learning algorithms are optimal for pre-training.

### [00:07 - 00:10]

This is joint work with my advisors, Ruslan Salakutinov and Sergey Levin.

### [00:12 - 00:21]

Reinforcement learning algorithms are expensive in terms of data, in terms of compute, and so there's been a lot of work in trying to speed them up by performing some sort of unsupervised pre-training without any reward functions.

### [00:22 - 00:28]

While these methods can work well in practice, there's been very little analysis probing when and where they're guaranteed to provide good results.

### [00:28 - 00:37]

Perhaps the most popular of these methods are skill learning methods, and our analysis will focus on how these skill learning methods do or do not make it easier to solve downstream tasks.

### [00:38 - 00:40]

What are skill learning algorithms?

### [00:40 - 00:46]

Skill learning algorithms try to identify many different useful behaviors for an agent before a reward function is given.

### [00:47 - 00:53]

For example, on this dog-like robot, we might want to learn skills corresponding to walking forwards and backwards, to crouching, to jumping.

### [00:54 - 00:58]

The motivation for learning such skills is that they might make it easier to solve new tasks.

### [00:58 - 01:00]

Either by combining or adapting these skills.

### [01:01 - 01:09]

As another example, for this robot arm, we might want to learn skills that interact with the blocks in different ways, sorting and grasping and reaching.

### [01:11 - 01:13]

Unsupervised skill learning is a vibrant area of research.

### [01:14 - 01:20]

Prior work has shown that it's possible to learn skills without any reward function, and that these skills often do help solve downstream tasks.

### [01:21 - 01:28]

While the precise details of all these different methods are different, many of them follow a similar template, maximizing a mutual information objective.

### [01:28 - 01:31]

To define that objective, we have to introduce a bit of notation.

### [01:32 - 01:35]

We will use zed as a latent variable indicating the skill.

### [01:35 - 01:39]

This is often a one-hot vector, though some work uses a continuous latent variable.

### [01:39 - 01:42]

And we'll use s to denote the states visited by the policy.

### [01:43 - 01:46]

To denote a specific skill, we'll use pi conditioned on zed.

### [01:47 - 01:53]

Formally, most of these methods maximize the mutual information between the latent variable zed and the states visited.

### [01:54 - 01:56]

Some of these methods include additional conditioning information.

### [01:58 - 02:04]

And finally, the mutual information tells us how much changes in the latent variable affect changes in the states visited.

### [02:06 - 02:09]

I like to think about the latent variable as a small number of knobs.

### [02:10 - 02:15]

Ideally, we'd like to find some knobs that allow us to sweep over the entire range of behaviors for the agent.

### [02:16 - 02:23]

Because we only have a small number of knobs, fiddling with these knobs is much easier than trying to find the right neural network parameters for solving a task.

### [02:25 - 02:26]

So far,

### [02:26 - 02:26]

we lack a clear,

### [02:26 - 02:28]

theoretical understanding,

### [02:28 - 02:30]

of when these skill learning methods are provably useful.

### [02:31 - 02:34]

While many prior works have proposed various objectives for learning skills,

### [02:34 - 02:41]

it's not yet clear what sorts of skills these methods will produce and how the skill learning objectives relate to reward maximization.

### [02:42 - 02:48]

It's unclear whether learning skills via mutual information maximization is a provably good way of doing pre-training.

### [02:48 - 02:51]

What does it even mean for a skill learning algorithm to be optimal?

### [02:52 - 02:54]

This is the main question that we answer in this paper.

### [02:54 - 02:58]

The rest of the talk explains how skill learning can be seen as geometry,

### [02:58 - 02:59]

which is the key to answering this question.

### [03:02 - 03:03]

To start,

### [03:03 - 03:05]

we'll think about skills not as animated behaviors,

### [03:05 - 03:07]

but rather in terms of the states that they visit.

### [03:08 - 03:08]

For example,

### [03:08 - 03:10]

if we have this ant-like robot shown here,

### [03:11 - 03:14]

the distribution of future states might look like the line below.

### [03:14 - 03:19]

Note that this is a combination of looking one step into the future and many steps into the future.

### [03:20 - 03:21]

Formally,

### [03:21 - 03:24]

we'll define the average state distribution using this equation here.

### [03:24 - 03:25]

Formally,

### [03:25 - 03:26]

we'll define the average state distribution using this equation here.

### [03:26 - 03:26]

Formally,

### [03:26 - 03:27]

we'll define the average state distribution using this equation here.

### [03:27 - 03:27]

Formally,

### [03:27 - 03:27]

we'll define the average state distribution using this equation here.

### [03:27 - 03:28]

Throughout this talk,

### [03:28 - 03:30]

I'll use a three-state MDP as a running example.

### [03:30 - 03:33]

Our theory applies to arbitrary discrete MDPs.

### [03:33 - 03:34]

In this three-state example,

### [03:34 - 03:37]

each policy corresponds to a distribution over three states,

### [03:37 - 03:40]

so we can plot each policy as a point in R3.

### [03:40 - 03:42]

We're showing six different policies here.

### [03:42 - 03:45]

Because probability distributions must be positive and sum to one,

### [03:45 - 03:48]

these points must lie on the blue triangle, a probability simplex.

### [03:49 - 03:50]

To reduce clutter,

### [03:50 - 03:53]

I'll remove the coordinate axes and kill the same data on the right.

### [03:54 - 03:55]

The orange region here is really important.

### [03:55 - 03:56]

This is the set of feasible state distributions.

### [03:56 - 03:57]

This is the set of feasible state distributions.

### [03:57 - 03:58]

This is the set of feasible state distributions.

### [03:58 - 04:00]

I'll refer to it as the state marginal polytope.

### [04:01 - 04:05]

This polytope is important because it reflects the dynamics of the environment.

### [04:05 - 04:08]

Some states are easy to visit, some states are hard to visit.

### [04:08 - 04:10]

The agent can't spend all of its time at some states.

### [04:13 - 04:15]

To provide some orientation into this land of state marginals,

### [04:15 - 04:17]

I want to think a little bit about reward maximization.

### [04:18 - 04:22]

We'll focus on reward functions that depend only on the state, not the action.

### [04:22 - 04:24]

In this land of state marginals,

### [04:24 - 04:26]

we can plot reward functions as vectors starting at the origin,

### [04:27 - 04:30]

and the expected return is the sum of the reward at each state

### [04:30 - 04:33]

times the probability that a policy visits that state.

### [04:34 - 04:38]

Which state marginal distribution maximizes this reward function shown here?

### [04:38 - 04:42]

Recall that we can only choose state marginal distributions inside this orange polytope.

### [04:44 - 04:45]

For this reward function,

### [04:45 - 04:49]

the optimal policy has a state marginal in the lower left-hand corner.

### [04:51 - 04:53]

In general, for a given reward function,

### [04:53 - 04:56]

the optimal policy always lies at one of these vertices.

### [04:56 - 05:00]

This is intriguing because it suggests that the vertices of the state marginal

### [05:00 - 05:03]

are sufficient for solving any reinforcement learning problem.

### [05:03 - 05:07]

So, one way of quantifying whether a skill learning algorithm is optimal or not

### [05:07 - 05:11]

is by seeing how many of these vertices are covered by some skill.

### [05:13 - 05:17]

So, where do the skills learned by mutual information-based skill learning algorithms

### [05:17 - 05:19]

lie on this polytope?

### [05:19 - 05:20]

Do they neatly tile the space?

### [05:20 - 05:22]

Do they pick out every vertex?

### [05:22 - 05:23]

Do they overlap?

### [05:25 - 05:26]

Well, for this example,

### [05:26 - 05:28]

they learned three skills, each of which lies at a vertex.

### [05:29 - 05:31]

But no skill is assigned to one of the vertices.

### [05:32 - 05:35]

Even if we tried to learn four skills or 100 skills,

### [05:35 - 05:37]

skill learning algorithms based on mutual information

### [05:37 - 05:39]

would never place a skill at this vertex.

### [05:39 - 05:41]

Instead, they would repeat one of the old skills.

### [05:43 - 05:45]

Here are four different environments,

### [05:45 - 05:48]

and we again visualize where the skills lie on the polytope.

### [05:49 - 05:51]

So, what's the general principle?

### [05:51 - 05:55]

We formally prove the following results for mutual information-based skill learning algorithms.

### [05:56 - 05:58]

First, skills always lie at vertices.

### [05:58 - 06:01]

They never lie on the interior of this polytope.

### [06:02 - 06:06]

But, while every skill lies at a vertex, not every vertex contains a skill.

### [06:07 - 06:08]

This isn't a failure of optimization.

### [06:08 - 06:11]

It's not an artifact of trying too few skills.

### [06:11 - 06:14]

It's a reflection of the underlying optimization problem.

### [06:14 - 06:18]

Optimizing for mutual information will not, in general, learn policies for every vertex.

### [06:19 - 06:22]

And this result is interesting because, as we discussed before,

### [06:22 - 06:25]

reward-maximizing policies always lie at vertices.

### [06:26 - 06:30]

Finally, the number of unique skills is at most equal to the number of states.

### [06:30 - 06:35]

If, say, you tried to learn an infinite number of skills using a continuous latent variable,

### [06:35 - 06:36]

you would still run up against this upper bound.

### [06:38 - 06:39]

These results are pretty negative.

### [06:39 - 06:43]

The skills learned by mutual information are not necessarily sufficient for solving downstream

### [06:43 - 06:46]

tasks, even if we could, say, take linear combinations of these skills.

### [06:47 - 06:50]

But what if we used skills in a different way to solve downstream tasks?

### [06:51 - 06:54]

Our next result will look at how the skills can be used for fine-tuning.

### [06:56 - 06:58]

To explain how the skills can be used for fine-tuning,

### [06:58 - 07:01]

we need to think about the skill learning algorithms in a different way.

### [07:02 - 07:06]

Usually, we think about these algorithms as optimizing for a small number of skills.

### [07:07 - 07:11]

In this talk so far, we've discussed what states these skills end up visiting,

### [07:11 - 07:13]

shown as the orange dots in some of those plots before.

### [07:14 - 07:15]

And we thought about the skill learning algorithms

### [07:15 - 07:18]

as moving these orange dots around inside the orange polytope.

### [07:21 - 07:23]

To explain how skill learning relates to fine-tuning,

### [07:23 - 07:26]

I want to discuss a different way of thinking about these same skill learning algorithms.

### [07:26 - 07:29]

This is simple. Instead of optimizing some small number of skills,

### [07:29 - 07:32]

we can think about skill learning algorithms as assigning probabilities

### [07:32 - 07:34]

to every single possible policy.

### [07:35 - 07:37]

This is sort of like saying that the skill learning algorithm

### [07:37 - 07:40]

is given a big bucket of policies.

### [07:40 - 07:43]

Some of these policies may have a uniform distribution over states,

### [07:43 - 07:45]

some of them may lie at boundaries of the polytope.

### [07:45 - 07:48]

And now the skill learning algorithm gets to select some of these policies.

### [07:48 - 07:51]

Formally,

### [07:51 - 07:55]

the skill learning algorithm has to assign a probability to each of these policies.

### [07:55 - 07:55]

So, if you go back and look at the net value of these policies, the real data will be the same as the numbers on this table.

### [07:55 - 07:55]

So, the real data will get the numbers onto each of these policies. So that's why we think about these skills as something that can be used to design certain probabilities.

### [07:55 - 08:02]

So maybe the skill learning algorithm assigns a 70% probability to the red skill and a 30%

### [08:02 - 08:05]

probability to the pink skill and a 0% probability to the other skill.

### [08:05 - 08:08]

And these probabilities reflect how often the skill learning algorithm would use this

### [08:08 - 08:13]

policy in the environment.

### [08:13 - 08:17]

One important note is that from a mathematical perspective, these two ways of thinking about

### [08:17 - 08:18]

skill learning are the same.

### [08:18 - 08:21]

They both correspond to maximizing mutual information.

### [08:21 - 08:24]

While you would implement them in different ways, their mathematical equivalence means

### [08:24 - 08:30]

that we can use this new perspective to analyze the old perspective.

### [08:30 - 08:35]

So now we can view skill learning algorithms as selecting policies from this big bucket.

### [08:35 - 08:39]

An example before, the skill learning algorithm assigned a probability of 70% to the red policy

### [08:39 - 08:42]

and 30% to the pink policy.

### [08:42 - 08:45]

Maybe those policies lie in the upper left and lower left corners, and we'll use orange

### [08:45 - 08:49]

dots to visualize the probabilities assigned to those policies.

### [08:49 - 08:54]

After deciding which policies to select from this big bucket, we can then ask the following

### [08:54 - 08:55]

question.

### [08:55 - 08:59]

On average, what states do the selected policies visit?

### [08:59 - 09:04]

This depends on which policies we've selected and the probabilities we've put on those

### [09:04 - 09:05]

policies.

### [09:05 - 09:10]

In this example, the average state distribution is shown as this black dot.

### [09:10 - 09:13]

Because the skill learning algorithm has assigned a higher probability to the red policy than

### [09:13 - 09:16]

the pink policy, this average is closer to the red policy.

### [09:16 - 09:21]

And I'll refer to this average as the prior, because later we'll use it as an initialization

### [09:21 - 09:24]

for solving downstream tasks.

### [09:24 - 09:27]

We didn't express this prior using this equation.

### [09:27 - 09:32]

It says that the probability of a state under the average state distribution is the probability

### [09:32 - 09:37]

that each policy visits that state times the probability that we sampled that policy.

### [09:37 - 09:42]

Intuitively, this average state distribution will be in the middle of the selected policies.

### [09:42 - 09:48]

So one might imagine that it might be good for fine tuning to solve downstream tasks.

### [09:48 - 09:52]

So let's think about using this prior to solve downstream tasks via fine tuning.

### [09:52 - 09:54]

Ideally, we'd like to find tuning.

### [09:54 - 09:59]

to happen quickly, so we need to measure the speed of learning new tasks. We'll measure speed of

### [09:59 - 10:04]

learning based on the distance between the prior state distribution and the state distribution of

### [10:04 - 10:09]

a reward-maximizing policy. And recall that the reward-maximizing policies always lie at vertices

### [10:09 - 10:15]

of this orange polytope. So ideally, we'd like to find a prior distribution that's close to all of

### [10:15 - 10:21]

the vertices. In our analysis, we'll use the Kale divergence to measure this distance. This Kale

### [10:21 - 10:25]

divergence is different from the number of gradient steps, and we encourage future work to

### [10:25 - 10:32]

analyze fine-tuning under more practically relevant distance measures. Now, it turns out that there's

### [10:32 - 10:38]

a very close relationship between the speed of fine-tuning and mutual information. Maximizing

### [10:38 - 10:43]

mutual information is equivalent to finding a prior that's closest to the furthest policy.

### [10:44 - 10:49]

That is, maximizing mutual information is equivalent to finding a prior that minimizes

### [10:49 - 10:51]

the length of the longest black line.

### [10:51 - 10:58]

Here, we visualize how optimizing mutual information changes the prior. At convergence,

### [10:58 - 11:03]

the optimization alternates between updating the prior using the hardest vertices. These

### [11:03 - 11:08]

hardest vertices exactly correspond to the skills, and the frequency of updates in each direction

### [11:08 - 11:12]

corresponds to the probability that that skill is sampled. And note that some vertices are

### [11:12 - 11:17]

never used for updates. These vertices are never used as skills. This connection helps

### [11:17 - 11:21]

explain why maximizing mutual information might be useful for solving downstream tasks.

### [11:21 - 11:28]

The average skill is close to all other skills. So, what happens if we use this average skill

### [11:28 - 11:31]

as an initialization for solving downstream tasks?

### [11:31 - 11:36]

Let's think about what it would mean to use this initialization for solving the downstream

### [11:36 - 11:41]

tasks. Some prior work has argued that a uniform distribution over states is a good initialization,

### [11:41 - 11:45]

so let's look at that. The red dots correspond to the optimal policies for a bunch of different

### [11:45 - 11:51]

tasks. And to analyze the optimization, we'll use an idealized learning algorithm that can

### [11:51 - 11:56]

easily control the state distribution. The expanding contours here show progressive steps

### [11:56 - 12:00]

of this idealized learning algorithm. And we see that a uniform prior is a good prior,

### [12:00 - 12:03]

as all of the tasks are solved relatively quickly.

### [12:03 - 12:08]

Now, let's compare this to the prior learned by skill learning. Whereas the prior from

### [12:08 - 12:13]

skill learning takes only 9 steps to solve all of the tasks, a uniform prior takes more

### [12:13 - 12:16]

than 13 steps to solve all of the tasks.

### [12:16 - 12:21]

Formally, we prove that skill learning using mutual information will always find the

### [12:21 - 12:26]

optimal prior. That is, maximizing mutual information corresponds to finding a prior

### [12:26 - 12:29]

that's closest to the hardest task.

### [12:29 - 12:34]

As noted before, the learning procedure visualized here is very idealized. Real RL algorithms

### [12:34 - 12:38]

take gradient steps in parameter space or in action space, not in state space. So, while

### [12:38 - 12:45]

current mutual information algorithms are optimized for this idealized learning procedure,

### [12:45 - 12:48]

other yet-to-be-invented skill learning algorithms might be better for more realistic learning

### [12:48 - 12:51]

procedures.

### [12:51 - 12:56]

The main takeaways from this talk are that unsupervised skill learning algorithms cannot

### [12:56 - 13:01]

learn the optimal policy for every downstream task, but they do provide an optimal initialization

### [13:01 - 13:03]

under some strict assumptions.

### [13:03 - 13:07]

Please check out the poster for more information. I'm happy to take any questions now. Thanks!
