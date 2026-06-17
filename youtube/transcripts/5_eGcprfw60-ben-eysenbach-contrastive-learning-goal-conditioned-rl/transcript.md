# Contrastive Learning as Goal-Conditioned Reinforcement Learning

- URL: https://www.youtube.com/watch?v=5_eGcprfw60
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T15:12:47`

## Transcript

### [00:00 - 00:06]

I'm excited to share our work entitled Contrastive Learning as Goal-Conditioned Reinforcement Learning.

### [00:06 - 00:09]

Deep reinforcement learning algorithms have achieved really great results in the last

### [00:09 - 00:12]

few years, but they've also become a fair bit more complex.

### [00:12 - 00:15]

Today, they're like an engine with many moving parts.

### [00:15 - 00:17]

One part predicts the future rewards.

### [00:17 - 00:20]

Maybe you have another part that learns a model of the environment.

### [00:20 - 00:25]

Maybe another part learns compact representations of high-dimensional data.

### [00:25 - 00:29]

In this work, we propose a much simpler approach, where we will have a single objective that

### [00:29 - 00:34]

simultaneously results in predicting the future rewards, learning a model of the environment,

### [00:34 - 00:37]

and learning good representations.

### [00:37 - 00:39]

We focus on goal-conditioned reinforcement learning.

### [00:39 - 00:43]

We want to learn a policy that takes as input some current image and goal image, and takes

### [00:43 - 00:46]

actions to try to get to this goal image.

### [00:46 - 00:51]

We train this policy using a big dataset of videos labeled with actions.

### [00:51 - 00:55]

Unlike trajectories in the standard reinforcement learning setting, these are not labeled with

### [00:55 - 00:58]

rewards.

### [00:58 - 01:01]

We'll define the reward function to be whether you reach the goal state at the next time

### [01:01 - 01:02]

step.

### [01:02 - 01:06]

But this reward function doesn't require reward engineering, and is defined purely

### [01:06 - 01:08]

in terms of the physics.

### [01:08 - 01:13]

We maximize the sum of these rewards, and the queue function is the same objective,

### [01:13 - 01:16]

conditioned on some current state and action.

### [01:16 - 01:20]

The key idea of our approach is to use contrastive learning to build an entire reinforcement

### [01:20 - 01:24]

learning algorithm, one that doesn't require any sort of extra representation learning,

### [01:24 - 01:26]

reward learning, or model learning.

### [01:26 - 01:26]

I'll first explain how we apply that contrastive learning algorithm.

### [01:26 - 01:27]

I'll explain how we apply the contrastive learning algorithm.

### [01:27 - 01:28]

I'll first explain how we apply the contrastive learning algorithm.

### [01:28 - 01:32]

of learning. And then the next slide will show how this is an entire reinforcement learning

### [01:32 - 01:36]

algorithm. Our method is going to look pretty similar to prior methods for representation

### [01:36 - 01:41]

learning on video, for audio, on text. But the key difference is that our method will

### [01:41 - 01:47]

allow us to solve the reinforcement learning problem. We're going to learn two representations,

### [01:47 - 01:54]

one of states and actions and one of future states. The data will be sampled from trajectories.

### [01:54 - 01:59]

We'll sample the positive examples using a state and an action and a future state from

### [01:59 - 02:03]

the same trajectory. Precisely, we'll use a future state sample from a geometric distribution

### [02:03 - 02:09]

that allows us to draw a connection with q values. And we'll sample random states from

### [02:09 - 02:14]

different trajectories and push those representations further apart from each other.

### [02:14 - 02:18]

Now, intuitively, these representations will allow us to reason about what states are we

### [02:18 - 02:24]

likely to visit in the future. And importantly, they will allow us to figure out which actions

### [02:24 - 02:24]

are likely to get a positive result.

### [02:24 - 02:31]

to the desired goal state. Here's how the complete algorithm works. We start with the data set,

### [02:31 - 02:36]

maybe from a different experiment, maybe from a random policy. We apply contrastive learning to

### [02:36 - 02:40]

learn the representations, and then we learn the policy to maximize the likelihood of the desired

### [02:40 - 02:45]

goal state. Optionally, we could go back and collect more data. We've shown that our method

### [02:45 - 02:52]

can work well even when we don't collect more data. Our method doesn't include many of the

### [02:52 - 02:56]

tricks and extra machinery that prior methods do, and our open source code is very fast.

### [02:59 - 03:03]

There are a number of ways of viewing what contrastive learning gives us. One is that it

### [03:03 - 03:07]

gives us an implicit model of the world, something that allows us to predict what's going to happen,

### [03:07 - 03:13]

but doesn't require regressing to high-dimensional outputs. It can also be viewed as giving us a

### [03:13 - 03:19]

predictor of the future returns of a Q function, and also gives us low-dimensional representations

### [03:19 - 03:20]

of states.

### [03:22 - 03:26]

Training the actor has a nice geometric interpretation. Let's think about the

### [03:26 - 03:30]

representation of the goal state and the representation of the current state, which

### [03:30 - 03:34]

might be different for different actions. If we simply look at the similarity between these

### [03:34 - 03:38]

representations, training the actor corresponds to choosing whichever state action representation

### [03:38 - 03:44]

brings us closest to the goal representation. We can think about this as doing planning in

### [03:44 - 03:48]

a representation space. Now, normally, planning is hard. For example, if you greedily tried to

### [03:48 - 03:52]

solve this task by moving the arm to the goal, then you wouldn't pick up the block. But what

### [03:52 - 03:57]

we've done by learning these representations is make the planning problem easier. Greedy

### [03:57 - 04:01]

planning in the representation space is optimal.

### [04:01 - 04:06]

We evaluated on many tasks, including this bin-picking task. The agent has to pick up

### [04:06 - 04:09]

the block and move it towards the blue bin, and it's really hard because we don't have

### [04:09 - 04:14]

reward shaping, we don't have demonstrations, and it's done entirely from images.

### [04:14 - 04:18]

Our first baseline is goal-conditioned behavioral cloning, which is a pretty simple baseline

### [04:18 - 04:21]

that works really well, according to prior work.

### [04:22 - 04:27]

The second one is TD3 plus HER, which is a temporal difference method combined with

### [04:27 - 04:37]

hindsight relabeling. Only our method is able to solve this task. We evaluated baselines

### [04:37 - 04:42]

and a number of other manipulation tasks and observed that our method achieves better results

### [04:42 - 04:48]

on all but the easiest tasks. Please stop by the poster to learn more, such as experiments

### [04:48 - 04:50]

and future directions. Thanks.
