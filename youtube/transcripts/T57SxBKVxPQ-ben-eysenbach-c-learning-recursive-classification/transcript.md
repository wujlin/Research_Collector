# C-Learning Learning to Achieve Goals via Recursive Classification

- URL: https://www.youtube.com/watch?v=T57SxBKVxPQ
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T15:13:25`

## Transcript

### [00:00 - 00:07]

I'm Ben Eysenbach. I'm presenting our work entitled C-Learning, Learning to Achieve Goals by a Recursive Classification. This is joint work with Sergey and Ross.

### [00:08 - 00:13]

Typically, reinforcement learning is viewed as the process of transforming a reward function into useful behavior.

### [00:13 - 00:21]

Designing reward functions can be quite tedious. So in this work, we consider how can we learn useful behaviors directly from data without reward functions?

### [00:22 - 00:27]

To this end, we'll reframe the problem of goal-conditioned RL as one of predicting and controlling the future.

### [00:27 - 00:33]

For example, looking at this ant-like robot here, we want to predict where will this robot be in the future.

### [00:34 - 00:38]

In particular, we want to estimate the density over time-discounted future states.

### [00:39 - 00:44]

Prior methods such as C-Learning and successive features don't solve this paper, as we discussed in the paper.

### [00:46 - 00:50]

So how are we going to learn this density function? Our main idea is to learn a future state classifier.

### [00:51 - 00:56]

This classifier takes as input the current state in action, as well as some other state, and tries to guess,

### [00:56 - 01:01]

does this other state come from the future, or is it just some random state?

### [01:01 - 01:06]

And it turns out that we can use Bayes' rule to transform this classifier into a density function.

### [01:07 - 01:10]

We call this algorithm Monte Carlo C-Learning.

### [01:10 - 01:16]

Here's some visualizations showing that C-Learning accurately predicts where the agent will be in the time-discounted future.

### [01:19 - 01:26]

We extended this to a variant called Temporal Different C-Learning that allows us to learn a classifier from off-policy experience.

### [01:26 - 01:32]

I'm not going to go into the details, but the resulting algorithm ends up looking similar to Q-Learning, with a couple of differences.

### [01:32 - 01:40]

For one, things like hindsight relabeling emerge automatically from our derivation, and our derivation even tells us how to optimally sample goals for relabeling.

### [01:43 - 01:54]

We can also use C-Learning to control the future. In particular, if there's some goal state we want to reach, we can ask our classifier, what action should we choose now, such that this goal state is likely a future state?

### [01:56 - 02:00]

Let's look at some experiments of using C-Learning for goal-conditioned RL.

### [02:00 - 02:04]

On this task, the robot is trying to move the red puck to the green region.

### [02:05 - 02:10]

We compared our method to prior methods based on Q-Learning, and these prior methods relabel experience in different ways.

### [02:11 - 02:21]

We observe that none of these prior methods make any progress on this task. And it's not surprising. We don't have any reward function, we don't have any reward shaping, and there's no notion of an epsilon ball or distance metric.

### [02:21 - 02:24]

In contrast, our method performs quite well on this task.

### [02:26 - 02:37]

We also compared our method to prior methods on a wide range of tasks, and observed that on the easier tasks, our method performs as well as the best prior methods, and on the more complex tasks, our method was quite a bit better.

### [02:39 - 02:51]

One of the most surprising observations from this project was that C-Learning has learned fairly complex behaviors. These are failure cases when the robot has failed to reach the goal, but has learned to automatically retry.

### [02:51 - 03:02]

In short, we've presented C-Learning. There are a number of things I didn't get a chance to talk about, so I guess how C-Learning satisfies certain Bellman equations. Check out the paper for more information.
