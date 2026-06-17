# Ben Eysenbach Thesis Defense

- URL: https://www.youtube.com/watch?v=ODVaWSKCzTM
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T14:47:44`

## Transcript

### [00:00 - 00:07]

Okay, let's get started.

### [00:11 - 00:23]

The past decade has been really, really exciting for machine learning, because we've gotten systems that can actually work, that can make predictions fairly reliably, fairly accurately, in a number of domains.

### [00:23 - 00:31]

I think the next frontier of AI is going to be systems that actually interact with the world, that can optimize sequences of actions.

### [00:33 - 00:35]

That's what reinforcement learning is all about.

### [00:38 - 00:42]

It's about choosing sequences of actions that lead to good outcomes. It's about improving through experience.

### [00:44 - 00:50]

The work that I've done throughout my PhD casts reinforcement learning as a sort of probabilistic machine learning problem.

### [00:50 - 00:54]

And in today's talk, I'm going to talk about why that's been useful.

### [00:55 - 01:03]

It's been useful because it's made it easier for users to use these reinforcement learning tools, to specify outcomes that can just give examples of those outcomes.

### [01:03 - 01:15]

But more than that, this idea has also led to better algorithms. Algorithms that not only outperform prior methods, but also can find patterns and structure in the solution to decision-making problems.

### [01:17 - 01:20]

And that's what I'm going to talk about today, the work that we've done with thesis.

### [01:20 - 01:20]

And

### [01:20 - 01:20]

how we've done that.

### [01:20 - 01:25]

How some of this work might enable certain potential applications of reinforcement learning.

### [01:28 - 01:33]

Reinforcement learning has the potential to unlock applications in nearly every aspect of our lives.

### [01:34 - 01:41]

A lot of the foundational work in reinforcement learning is in games. Games like Go or Atari or poker. But the potential applications are much, much broader.

### [01:43 - 01:49]

They include things like robotics. Robots that help patients in hospitals. Robots that safely drive our cars. Robots that make our warehouses safe.

### [01:50 - 01:50]

Robots that safely drive our cars. Robots that make our warehouses safe.

### [01:50 - 01:51]

Robots that safely drive our cars. Robots that make our warehouses safe.

### [01:52 - 01:58]

Problems like robotics are really hard. This robot here, it has twenty motors, one at each knuckle.

### [01:58 - 02:04]

How can you control those motors? What sequence of commands do you show them, so that you eventually solve this Rubik's Cube?

### [02:06 - 02:09]

There are potential applications in our built world, too.

### [02:10 - 02:20]

How can we optimize the sequence of traffic lights, so we spend less time sitting at intersections? And how can we do this, making use of large streams of data that flow into centralized centers?

### [02:20 - 02:30]

In healthcare, AI systems are already being used to help predict the outcomes-

### [02:30 - 02:37]

for certain patients. But maybe the next set of AI tools will actually assist physicians in making decisions.

### [02:38 - 02:44]

Applications in robotics and healthcare. They require learning from historical data. We don't want to be learning by trial and error.

### [02:46 - 02:49]

There are potential applications in education, too.

### [02:49 - 02:50]

We've seen the blossoming.

### [02:50 - 02:50]

We've seen the blossoming.

### [02:50 - 02:59]

How can we leverage that figure out what sequence of problems to show students, what those problems depend on students past experiences.

### [02:59 - 03:13]

And in the sciences conventionally learning tools might be able to predict the outcome of some experiment, but reinforcement learning tools, they may allow us to dynamically control those experiments.

### [03:13 - 03:23]

Of course, all these potential applications, there are not going to be solved with reinforcement learning people alone, but in collaboration with domain experts in concert with other areas of machine learning.

### [03:23 - 03:33]

But I think that reinforcement learning is a really important piece of this puzzle, because reinforcement learning unless it's optimized for the long term outcomes.

### [03:33 - 03:39]

Most of the successes that we've seen reinforcement learning have been in the context of games.

### [03:39 - 03:42]

And I think the reason why is that we know the rules of games.

### [03:42 - 03:43]

We know the rules of games.

### [03:43 - 03:44]

We can simulate games.

### [03:44 - 03:47]

We can generate lots and lots of data.

### [03:47 - 03:51]

But the progress of other applications has been a lot more measured.

### [03:51 - 03:59]

And I think the reason why is that it's a lot harder to get the data, and it's a lot harder to give feedback in these other applications.

### [03:59 - 04:09]

And so if we hope to make progress on these potential applications, we're going to need a way of developing reinforcement learning algorithms that can learn with less feedback.

### [04:09 - 04:13]

And in today's talk i'm going to talk about the work that we've done in the thesis.

### [04:13 - 04:14]

Towards this end.

### [04:14 - 04:20]

First, we've made it easier for users to give feedback by just giving examples of good outcomes.

### [04:20 - 04:33]

And second, about how we've developed algorithms like an infrastructure in the solution to decision making problems, breaking down hard problems into easier problems that we can learn with less feedback.

### [04:33 - 04:36]

So the start to make sure we're all on the same page.

### [04:36 - 04:40]

I want to briefly review how the reinforcement learning problem works on the left here.

### [04:40 - 04:42]

I'm feeling a robot task.

### [04:42 - 04:45]

And this is what I'll refer to as the environment.

### [04:45 - 04:59]

There's this robot here, and to control this robot we're going to take the action to respond to opening and closing the robot's hand, moving the robot hand to the left or to the right.

### [04:59 - 05:02]

And we observe observations.

### [05:02 - 05:05]

I'll see you guys.

### [05:05 - 05:11]

Observations in this setting are going to correspond to an image showing us the pixels what's happening in this environment.

### [05:11 - 05:12]

Right now.

### [05:12 - 05:22]

And the most important object is this policy down here that allows us to figure out what actions do we take, given the current observation, given this current state pass.

### [05:22 - 05:25]

And at the end of the day is this policy that we want to learn.

### [05:25 - 05:29]

And we're going to learn the policy by using these rewards here.

### [05:29 - 05:33]

The rewards say, Is this a good state, or is this a bad state?

### [05:33 - 05:41]

And we want to find the policy that takes us to states that are good not only now, but also lead us to good states in the future.

### [05:41 - 05:45]

So this reinforcement learning problem is really exciting because it's so general.

### [05:45 - 05:49]

All of those potential applications of reinforcement learning that we saw.

### [05:49 - 05:51]

Those are examples of this problem.

### [05:51 - 05:59]

But this generality also makes it really hard, and I want to review what I think is the main challenge in reinforcement learning.

### [05:59 - 06:02]

I think the main challenge is the lack of feedback.

### [06:02 - 06:04]

And I want to review what I mean by this.

### [06:04 - 06:07]

In reinforcement learning, maybe we have this robot here.

### [06:07 - 06:10]

We want to pick up this block, and it takes 1, 2, 3, 4, maybe 5 actions.

### [06:10 - 06:14]

And at the end they get some feedback saying, Okay, you've gotten some good state.

### [06:14 - 06:17]

You get this reward of this plus 5.

### [06:17 - 06:21]

But before then, the robot might not get any feedback.

### [06:21 - 06:27]

And this is very different from supervised learning, where, for every input you get the feedback, you get the label.

### [06:27 - 06:35]

And this problem is compounded by the fact that we want to solve reinforcement learning problems in high dimensional settings.

### [06:35 - 06:38]

Those observations, those images to computer.

### [06:38 - 06:40]

The guests look like a big block of numbers.

### [06:40 - 06:54]

And the reason why looking at high-dimensional problems is important is because it's precisely on these high-dimensional problems that we expect learning-based approaches to outperform classical approaches.

### [06:54 - 07:00]

And there's a third problem, too, with these with providing the feedback a practical challenge.

### [07:00 - 07:04]

Why should this state here get a reward of plus 5?

### [07:04 - 07:09]

Well, in practice, it was because a bunch of grad students spent too many hours writing.

### [07:09 - 07:14]

This big block of code here that says, Okay, when you're at this state, you get a reward of plus 5.

### [07:14 - 07:18]

But this big block of code, it serves as a barrier to enter.

### [07:18 - 07:25]

How many users would like to apply reinforcement learning to their problem, but don't know how to write a big block of code like that?

### [07:25 - 07:28]

And even experts might look at this and say, Is this correct?

### [07:28 - 07:31]

Will this result in the desired behavior?

### [07:31 - 07:37]

And as we move to real world problems, even running this piece of code is hard.

### [07:37 - 07:39]

Say this piece of code.

### [07:39 - 07:43]

It requires knowing the positions of every object in the sea.

### [07:43 - 07:48]

But even the best object detectors we have, they sometimes make errors.

### [07:48 - 07:54]

And so if you hold the building,

### [07:54 - 08:01]

And so if we hope to make progress and reinforcement learning, we're going to need a way of learning from less feedback.

### [08:01 - 08:07]

Now these problems of learning from limited feedback with high-dimensional data new to reinforcement learning.

### [08:07 - 08:08]

And in fact, we've seen similar problems.

### [08:08 - 08:15]

In other areas of machine learning and there and domains like computer vision and natural language processing.

### [08:15 - 08:20]

We've seen how self-supervised approaches have achieved really excellent results.

### [08:20 - 08:24]

And so I want to review how those methods work in computer vision.

### [08:24 - 08:33]

The methods that say, take an image and cover up pixels of that image or patches of that image, and try to predict what those missing pixels or patches are.

### [08:33 - 08:36]

And these are the techniques that underlie some of the generative Ai models that you may have seen over the last few years.

### [08:36 - 08:52]

Similarly, in natural language processing they're methods that take the words of that sentence, and then try to predict what are those missing words, or what is the next word of that sentence?

### [08:52 - 08:59]

And these are some of the techniques that underlie some of the large language models that you've probably seen over the last year.

### [08:59 - 09:02]

And they're another class of self-supervised methods.

### [09:02 - 09:04]

These are contrastive learning methods.

### [09:04 - 09:05]

Methods.

### [09:05 - 09:12]

Look at the inputs and try to learn the representations so that similar inputs have similar representations.

### [09:12 - 09:17]

And it's these last class of methods that we're going to build upon today.

### [09:17 - 09:24]

So these self-supervised methods and other domains that achieve really excellent results, learning from high dimensional data with limited.

### [09:24 - 09:28]

How can we realize those same games in the reinforcement learning setting?

### [09:28 - 09:34]

What does it even mean to self-supervised reinforcement learning?

### [09:35 - 09:47]

If I had to summarize my thesis in 5 words, it would probably be this that we've started just started to lay a foundation for self-supervised reinforcement learning.

### [09:47 - 09:51]

And in today's talk I hope to give you a taste of what this means.

### [09:51 - 09:59]

How we've developed practical algorithms, algorithms that we actually can implement and actually run in the real world.

### [09:59 - 10:03]

Theoretical guarantees for these methods that allow us to answer questions about when and where we expect.

### [10:03 - 10:19]

These methods to work, and also uncovering certain connections between these reinforcement learning methods and other areas of computer science, and even other areas of machine learning, too.

### [10:19 - 10:23]

For folks on zoom. If you wouldn't mind muting muting, that would be fantastic.

### [10:23 - 10:29]

Thanks. Okay, So here's what we're going to talk about in today's talk.

### [10:29 - 10:32]

I'm first going to talk about how we can learn goal reaching skills.

### [10:32 - 10:38]

These goal reaching skills are going to unlock a couple of capabilities.

### [10:38 - 10:45]

First, they're going to allow users to specify tasks by just giving an image of what they would like to happen.

### [10:45 - 10:49]

They no longer need to write that big block of code that we saw before.

### [10:49 - 10:58]

I'll talk about how we've deployed some of these methods in the real world collaboration with folks, and then we'll talk about some of the theoretical properties.

### [10:58 - 11:01]

We've proven about these methods connecting them to reward maximization.

### [11:01 - 11:09]

In a way that actually allows us to expand them and apply them to fully general reinforcement learning problems.

### [11:09 - 11:17]

Not only are these goal reaching skills useful in their own right, but they also will provide the right abstraction for planning.

### [11:17 - 11:25]

And by incorporating these skills into planning algorithms, we'll be able to extend their capabilities to over an order of magnitude.

### [11:25 - 11:30]

And doing this will allow us to apply these methods to this outdoor robot.

### [11:31 - 11:39]

Now, of course, when we want to apply reinforced learning to real world problems, ensuring that our methods are robust is really, really important.

### [11:39 - 11:42]

And we've studied robustness in a number of ways.

### [11:42 - 11:46]

We've looked at how regularization can provide a certain degree of robustness.

### [11:46 - 11:51]

We've looked at how to make use of approximate models, learning from them, or recognizing the errors.

### [11:51 - 11:56]

But I'm not going to talk about our work on robustness and generalization today.

### [11:56 - 12:01]

So to get started, I want to talk about this first part about learning these goal reaching skills.

### [12:01 - 12:05]

And I'm going to start by defining the problem statement.

### [12:05 - 12:09]

This problem of goal conditioned reinforcement learning.

### [12:09 - 12:16]

So let's say we have this robot that I started the talk with, and we want this robot to pick up the green object, move it into the blue bed.

### [12:16 - 12:21]

Well, we could write down that big, complicated reward function we saw before.

### [12:21 - 12:28]

But instead, we're going to ask the users to just provide an image of what we would like the robot to do.

### [12:28 - 12:30]

What is the desired outcome?

### [12:31 - 12:38]

So in this case, the desired outcome to get there, we would want to do the robot to go down and grasp the green objects.

### [12:38 - 12:43]

Pick it up, move it over a little bit to the blue bin, and drop it into the blue pen.

### [12:43 - 12:48]

This problem of goal conditioned reinforcement learning is actually a very old problem.

### [12:48 - 13:00]

And some of the early work in Ai, including work right over there from Nsa, was on this problem of learning goal reaching behaviors.

### [13:00 - 13:11]

Now we're going to study this problem in a particular setting, one where we're given as input a data set, and this set, and it'll be a data set of videos labeled with actions.

### [13:11 - 13:15]

And one thing to note that these videos they're not necessarily optimal.

### [13:15 - 13:18]

The actions in them are not necessarily good actions.

### [13:18 - 13:24]

But from this data we're going to find try to find skills that can reach goals as quickly as possible.

### [13:24 - 13:29]

So why is this problem useful? Well, practically it's going to make it easier for users to specify tasks.

### [13:29 - 13:30]

But.

### [13:30 - 13:43]

Mathematically, it's also going to build upon the prior work and allow us to apply these methods to settings that have continuous states and observations and actions as well as problems with stochastic dynamics while retaining certain theoretical

### [13:43 - 13:49]

properties. We'll show that this map is a well-defined objective.

### [13:49 - 13:55]

So how are we going to do this? How are we going to learn these goal reaching skills?

### [13:55 - 13:59]

Well, we're going to do this in 2 steps. The first step is going to entail.

### [13:59 - 14:07]

Learning representations from these data and learning representations is important whenever we're dealing with high dimensional data.

### [14:07 - 14:14]

And then the second step is going to be to learn these goal reaching skills from these representations.

### [14:14 - 14:21]

So that's the game plan and i'm gonna start by talking about how we learn these representations.

### [14:21 - 14:28]

So there are many prior approaches you could use for learning representations of high dimensional data.

### [14:28 - 14:34]

There's some methods that look at the frames in a video and try to predict what is the next frame in the video.

### [14:34 - 14:43]

There are other methods that say, look at the phrase individually in some video and try to learn some representation that tells you about the contents of that frame.

### [14:43 - 14:48]

What these methods typically don't do is they typically don't tell you about the actions they don't tell you.

### [14:48 - 14:53]

Well, if you wanted to get from point A to point B, what actions should you take?

### [14:53 - 14:57]

And so we're going to need a different way of learning the representations.

### [14:58 - 15:04]

Our method for doing this is going to build upon prior methods developed in the computer vision and natural language processing community.

### [15:04 - 15:07]

But we're going to extend it to the reinforcement learning setting.

### [15:07 - 15:14]

That's this idea of contrastive learning, and I want to walk you through how we apply this to the reinforcement learning setting.

### [15:14 - 15:23]

We're going to learn 2 representations, a representation of the states and the actions as well as a representation of the future states.

### [15:23 - 15:27]

And we're going to do this using the data set of the videos and the actions.

### [15:27 - 15:39]

So to start we're going to take a video, and we're going to take 2 images from that video and say these images should have similar representations.

### [15:39 - 15:43]

And precisely these 2 images are going to be sampled.

### [15:43 - 15:48]

So there are certain distance apart from each other, a distance governed by a certain geometric distribution.

### [15:48 - 15:53]

So they're most likely to be 1 or 2 steps apart, but they could be 3 or 4 or more steps apart.

### [15:53 - 15:57]

And that geometric distribution will be important for proving certain things.

### [15:57 - 16:00]

Theoretical properties of these methods.

### [16:00 - 16:09]

And then we're going to look at a second video, and we're going to say that images from different videos should have different representations.

### [16:09 - 16:20]

So what's the intuition here? The intuition is that these representations, once they're learned, they can tell you something about the difficulty of getting from one state to another state.

### [16:20 - 16:25]

If the states have similar representations, it's pretty likely you can get from one to the other.

### [16:25 - 16:27]

And importantly, these representations.

### [16:27 - 16:33]

They depend on the action, and that was the key property that was missing from some of the prior methods.

### [16:33 - 16:39]

So I want to give you an example of what these sorts of representations they learn.

### [16:39 - 16:45]

So we did this by applying these methods, the simulated manipulation task here.

### [16:45 - 16:49]

And in this task there's this robot arm there's this red object.

### [16:49 - 16:56]

You can move there's this drawer you could open if the red object moved, and we can think about these representations as points.

### [16:56 - 17:01]

But we're going to normalize these points.

### [17:01 - 17:04]

So they lie on a sphere. This is a common technique.

### [17:04 - 17:15]

And now the way that we were learning these representations was by looking at the distance between them precisely by looking at the dot product between these representations.

### [17:15 - 17:21]

And so one way of thinking about these representations is that they're encoding a sort of model of the world.

### [17:21 - 17:25]

But one that predicts not. What is the future observation going to look like?

### [17:25 - 17:31]

What is the representation of some future state going to look like?

### [17:31 - 17:39]

These are the representations. They also very strong connections with some classical ideas and reinforcement learning relating to successor teachers and successor representations.

### [17:39 - 17:50]

And I can talk more about that at the end. So if you look at these representations and look along this path here, we can visualize what our method learns.

### [17:50 - 17:55]

And I want to point out 2 things about these visualizations and these visualizations.

### [17:55 - 17:59]

They were created using a nearest neighbor retrieval.

### [17:59 - 18:06]

So the first thing to note is that all these images have the same contents as this observation and the final observation.

### [18:06 - 18:10]

They all have the red object and the green object.

### [18:10 - 18:15]

But more than that, they also seem to have captured some notion of physics.

### [18:15 - 18:21]

So if you notice this red object here, it only moves when it's being touched.

### [18:21 - 18:23]

And similarly, this drawer.

### [18:23 - 18:27]

It only moves when the robot arm goes down and touches it.

### [18:27 - 18:30]

And this is different from what prior methods would do.

### [18:30 - 18:38]

If we take a different method, a common deep learning method known as a variational autoencoder and visualize its representations.

### [18:38 - 18:42]

These representations, they capture the contents of the scene, but not the physics.

### [18:42 - 18:49]

You notice that the arm moves, but it never touches the objects, even though the objects are also within.

### [18:49 - 18:52]

And so these representations and these visualizations of them.

### [18:52 - 19:01]

They give us some hints that well, maybe these are the right representations to use for building those goal reaching skills.

### [19:01 - 19:08]

Because at the end of the day, these representations were motivated by learning these goal reaching skills.

### [19:08 - 19:15]

And so I want to walk you through how we then learn these goal reaching skills from these representations.

### [19:15 - 19:21]

And I'm going to use an example that same robot task I showed at the beginning.

### [19:21 - 19:22]

So.

### [19:22 - 19:28]

Let's consider two actions, one action that moves the block to the right one, moves it to the left.

### [19:28 - 19:35]

And if you recall, the really important property of our representations was that they depended on the action.

### [19:35 - 19:40]

And so actually one is one representation, and actually two has one representation.

### [19:40 - 19:48]

And we can look at the distances between these representations, and we both see and space just on these representations.

### [19:48 - 19:51]

Do you folks think we should take action one or action?

### [19:52 - 20:01]

Yeah. So we can see. Okay, action, too. It has a representation that's closer towards the goal, and so it's probably the action you should take.

### [20:01 - 20:12]

And that's exactly what we did. We define each skill as simply taking the actions whose representations are closest towards the goal representation.

### [20:12 - 20:18]

So just to summarize this, we started with this data set of the videos and the actions.

### [20:18 - 20:21]

We then learned these representations.

### [20:21 - 20:27]

And then we extracted the skills, those goal-reaching skills from these representations.

### [20:27 - 20:31]

Now, at this point, we can use these skills to solve certain tasks.

### [20:31 - 20:40]

We also could use these skills to go back and collect some more data, and we feel that these skills work in both settings.

### [20:40 - 20:45]

Now, to provide a bit of context here, I started the section by talking about why reinforcement learning is hard.

### [20:45 - 20:50]

It's hard because of the limited feedback and ordinarily.

### [20:50 - 20:54]

But reinforcement learning is requiring a fair number of rewards to learn.

### [20:54 - 21:08]

But we often think about goal-conditioned reinforcement learning as even more challenging problem, because if learning how to reach one goal required one reward function, maybe learning how to reach many goals requires many reward functions.

### [21:08 - 21:18]

But what we've seen here is that we can cast this problem of goal-conditioned reinforcement learning in an entirely self-supervised way.

### [21:18 - 21:20]

So that we can learn these goal-reaching skills.

### [21:20 - 21:24]

So, we can create a reward function without ever having to specify a reward function.

### [21:24 - 21:28]

No user had to come write that big block of red code that we saw before.

### [21:28 - 21:37]

And I think this can help explain why these methods can work well.

### [21:37 - 21:40]

And so, after showing these methods, they work well in simulation.

### [21:40 - 21:46]

Together with collaborators, we looked at applying these methods to a real-world manipulation task.

### [21:46 - 21:48]

This robot shown here is a WidowX robot.

### [21:48 - 21:49]

It's a small, low-cost robot.

### [21:49 - 21:50]

It's a small, low-cost robot.

### [21:50 - 21:53]

robot, which makes it pretty accessible but also

### [21:53 - 21:55]

pretty finicky to work with.

### [21:55 - 21:58]

And I want to show you the skill that we learned

### [21:58 - 22:01]

for trying to get to the skull state shown here.

### [22:01 - 22:03]

And the difference between the starting state and the skull

### [22:03 - 22:07]

state is that the red spoon has moved to the left.

### [22:07 - 22:10]

And from a robotics perspective, this task

### [22:10 - 22:13]

is fairly challenging because we're

### [22:13 - 22:15]

going to do the learning from suboptimal data.

### [22:15 - 22:18]

It's not going to all be demonstrations.

### [22:18 - 22:20]

We don't know the positions of all the objects.

### [22:20 - 22:23]

We're doing this directly from the images.

### [22:23 - 22:26]

And we're going to learn this without ever interacting

### [22:26 - 22:27]

with this environment.

### [22:27 - 22:29]

There's not going to be any trial and error.

### [22:29 - 22:32]

It's all learned from that pre-existing data set.

### [22:32 - 22:35]

And just to underscore the difficulty of this,

### [22:35 - 22:37]

I want to show you what a prior method does.

### [22:37 - 22:40]

The prior method moves the robot arm to the correct position

### [22:40 - 22:45]

but never goes down and grabs the red spoon.

### [22:45 - 22:48]

And in contrast, here's our method.

### [22:48 - 22:50]

We see that the robot arm.

### [22:50 - 22:52]

It goes out of its way to grab that red spoon,

### [22:52 - 22:56]

drop it on the left side, and then move the hand up.

### [22:59 - 23:02]

Now, one property of these goal-reaching skills

### [23:02 - 23:04]

is really important, is that they

### [23:04 - 23:07]

were learned without any particular goal in mind.

### [23:07 - 23:09]

They were learned just in that data set,

### [23:09 - 23:11]

which means that if we want to solve some different task,

### [23:11 - 23:13]

for example, if we wanted the robot

### [23:13 - 23:16]

to push a can across the table, the only thing we need to do

### [23:16 - 23:18]

is give it a new goal image.

### [23:18 - 23:19]

We don't need to do.

### [23:19 - 23:20]

Any more training.

### [23:20 - 23:22]

We don't need to do any more gradient updates

### [23:22 - 23:24]

or specify any more data.

### [23:24 - 23:27]

And so without using that exact same policy

### [23:27 - 23:29]

for giving it a different goal, we

### [23:29 - 23:32]

see that the method is able to push the can across the table.

### [23:35 - 23:37]

So I hope these results, they help

### [23:37 - 23:40]

underscore the practical utility of these sorts of methods.

### [23:40 - 23:42]

That we can learn purely from the historical data

### [23:42 - 23:45]

that no users had to specify those reward functions.

### [23:45 - 23:46]

And the way we can do that is by using the data set.

### [23:46 - 23:47]

And we can use the data set.

### [23:47 - 23:48]

And we can use the data set.

### [23:48 - 23:49]

And we can use the data set. And we can use the data set.

### [23:49 - 23:50]

And we can deal with it in the same fashion.

### [23:50 - 23:51]

We can use the data set.

### [23:51 - 23:52]

And we can use the data set.

### [23:52 - 23:53]

And we can use the data set.

### [23:53 - 23:54]

And we can use the data set.

### [23:54 - 23:55]

And we can use the data set.

### [23:55 - 23:56]

And we can use the data set.

### [23:56 - 23:57]

And we can use the data set.

### [23:57 - 23:58]

And we can use the data set.

### [23:58 - 23:59]

But how do we do that?

### [23:59 - 24:00]

Well, the way we did that was

### [24:00 - 24:01]

by first learning these representations

### [24:01 - 24:02]

and then using these representations

### [24:02 - 24:03]

to extract the skills.

### [24:03 - 24:04]

Now, from a theoretical perspective,

### [24:04 - 24:05]

there still remains a pretty important question,

### [24:05 - 24:06]

which is these skills,

### [24:06 - 24:07]

how do they relate to reward maximization?

### [24:07 - 24:08]

Reinforcement learning,

### [24:08 - 24:09]

it's built upon this foundation of maximizing rewards.

### [24:09 - 24:10]

But do there skills,

### [24:10 - 24:11]

those goal-reaching skills does actually maximize

### [24:11 - 24:12]

any sort of reward?

### [24:12 - 24:18]

reward we'll see that answering this question showing that these skills solve a certain type

### [24:18 - 24:23]

of reinforcement learning problem helps us extend these methods applying similar techniques to fully

### [24:23 - 24:30]

general reinforcement learning methods and to write a little bit more context here these

### [24:30 - 24:36]

self-supervised methods upon which we've built in other domains there's often a disconnect between

### [24:36 - 24:41]

whatever representations you're learning and whatever downstream task you're trying to solve

### [24:41 - 24:46]

but we'll see that in the reinforcement learning setting there ends up being a very close connection

### [24:46 - 24:51]

between the representations you've learned and how you use those representations in the setting

### [24:51 - 24:59]

to solve decision-making problems so here's our main theoretical result our main theoretical

### [24:59 - 25:06]

result is that these representations they tell you about the future returns precisely

### [25:06 - 25:09]

if you look at the dot product or the similarity between these representations

### [25:10 - 25:11]

this tells you that you can use these representations to solve decision-making problems

### [25:11 - 25:17]

this tells you about the rewards that you'll get in the future and precisely these rewards here

### [25:17 - 25:22]

are a very natural reward function one that says okay do you get to the goal at the next time step

### [25:23 - 25:29]

but importantly we never have to actually compute those rewards there one thing i should mention is

### [25:29 - 25:36]

that this this reinforcement learning objective on the right hand side has very close is about

### [25:36 - 25:40]

maximizing probabilities trying to get to the goal with the highest probability but it is very

### [25:40 - 25:45]

strong connections to a different objective trying to minimize the total number of steps

### [25:45 - 25:53]

required to get to the goal as we get to visualize this result when we were defining these skills we

### [25:53 - 25:58]

were looking at these representations and what this theoretical result says is that when we were

### [25:58 - 26:02]

looking at the distances between the representations that was not a heuristic that was a principled

### [26:02 - 26:09]

thing to do and similarly when we were accusing the actions based on which action got us closest

### [26:09 - 26:10]

towards the goal representation

### [26:10 - 26:12]

that too was a principled thing to do

### [26:14 - 26:18]

and i should also mention that we've extended these results so that we can reason about

### [26:18 - 26:23]

what representations you would learn if you had applied these methods to a different data set

### [26:23 - 26:30]

a data set that had been collected by a different policy and so what this theoretical result means

### [26:30 - 26:34]

is that those skills that we showed before those were solving a certain type of reinforcement

### [26:34 - 26:38]

learning problem reinforcement learning problems with these goal routine rewards

### [26:39 - 26:40]

but this connection

### [26:40 - 26:45]

it also has enabled us to extend these methods to apply them to fully general reinforcement learning

### [26:45 - 26:53]

problems and one way we've done this is by giving multiple examples of outcomes where the frequency

### [26:53 - 26:56]

the probability of an outcome corresponds to how much reward you would like to have

### [27:00 - 27:02]

so just to summarize the section here

### [27:04 - 27:09]

we started by talking about how users no longer need to specify these rewards they can instead

### [27:09 - 27:10]

just give examples of what they would like to have and this is a very important part of the study and

### [27:10 - 27:13]

of what the desired outcomes look like giving one goal state or many goal states

### [27:14 - 27:19]

and these skills that can be learned both in the interactive setting or in the setting where we're

### [27:19 - 27:25]

learning just from an existing data set and finally we've shown how there's certain connections

### [27:25 - 27:33]

between these goal reaching skills and reward maximization now one thing i should mention is

### [27:33 - 27:39]

that these goal reaching skills that we've learned they're not magic and so we tried applying these

### [27:39 - 27:47]

methods to this task shown here this is a 3d simulated house there's a robot that walks

### [27:47 - 27:51]

around this house it has a camera and we give the robot an image of where in the house we would like

### [27:51 - 27:57]

it to go and we see whether it gets there and what we see is that if that image if the goal is in the

### [27:57 - 28:03]

same room as the robot then the robot succeeds in reaching that image but if the image is in a

### [28:03 - 28:09]

different room then the robot typically fails reaching that image now on the one hand this is

### [28:09 - 28:16]

not that surprising if you think about the number of action sequences of length say 20 that number

### [28:16 - 28:24]

of sequences is astronomically large but it turns out the components we've learned so far these

### [28:24 - 28:29]

representations and these goal reaching skills they can allow us to solve even the most distant

### [28:29 - 28:35]

problem even the most distant goal if we incorporate them into a planning algorithm

### [28:37 - 28:39]

and that's the next thing i want to talk about today

### [28:39 - 28:43]

how these goal-reaching skills provide the right abstraction for planning

### [28:46 - 28:51]

so historically there have been two ways that people have thought about solving decision-making

### [28:51 - 28:55]

problems the first part of this talk focused on learning-based methods methods that learn

### [28:55 - 28:59]

directly from the raw data but there's another class of methods planning methods

### [28:59 - 29:03]

these methods are really powerful this is what a lot of the early work in ai was about

### [29:04 - 29:08]

and this is a lot of the technology that underlies the internet how the information

### [29:09 - 29:11]

is being stored in a laptop is getting to everyone's laptops on zoom

### [29:13 - 29:18]

now what planning methods require is they require a symbolic representation of the world

### [29:20 - 29:24]

now what they lack though is they don't have a way of taking raw high-dimensional

### [29:24 - 29:29]

data and converting that into symbols converting high-dimensional data into some graph

### [29:31 - 29:35]

and it turns out that these self-supervised reinforcement learning methods that we've seen

### [29:35 - 29:38]

they can provide the right abstractions for applying planning methods and

### [29:38 - 29:42]

planning methods to high-dimensional data and so i want to show you how that works

### [29:45 - 29:50]

in the earlier part of this talk we talked about how we can use data this data set of videos and

### [29:50 - 29:55]

actions and use that to learn these goal-reaching skills as well as these representations

### [29:56 - 30:01]

and so we're going to start by applying that method to a data set collected from that

### [30:01 - 30:07]

simulated 3d house that we failed to navigate before and now we're going to use these components

### [30:07 - 30:14]

to build a graph because a graph is what planning methods require we're going to build a graph in

### [30:14 - 30:21]

the following way the nodes of this graph are going to be frames of taken from these videos

### [30:21 - 30:27]

sampled uniformly at random and the edges of this graph are going to be built using these

### [30:27 - 30:34]

representations that we've learned and precise for visual clarity i'm going to ignore edges

### [30:34 - 30:37]

that would be too long for showing this graph

### [30:38 - 30:41]

and now that we have this graph we can apply planning methods to it

### [30:42 - 30:47]

so let's say we want to navigate from one image to another image on distant corners of this house

### [30:48 - 30:53]

well we can plug these images into this graph and then find the shortest path on this graph

### [30:56 - 31:01]

and now we can use those goal reaching skills that we've learned to traverse the edges of

### [31:01 - 31:07]

this graph so we take the first image along this path and we use these goal reaching skill

### [31:08 - 31:12]

to take a sequence of actions to get us to that first waypoint and then we repeat this process

### [31:15 - 31:20]

this method outlined here it also can be entirely reinterpreted in a probabilistic way

### [31:21 - 31:25]

where we're trying to infer what is the sequence of states you would visit

### [31:25 - 31:29]

if you navigated from one state to another state and i can talk more about that at the

### [31:29 - 31:37]

end if folks are interested i want to walk you through an example of how this works so we evaluated

### [31:37 - 31:42]

the method on a number of goals here's one example where the robot starts seeing this

### [31:42 - 31:48]

image and wants to navigate into this kitchen shown here and here are the sequence of images

### [31:48 - 31:53]

that the method inferred these are the images it thinks it can visit when it's navigating the house

### [31:53 - 31:57]

going closer towards this cupboard going into the kitchen and then going towards the stove

### [31:57 - 32:03]

up there and if we take a bird's eye view we can see that these images actually make a lot of sense

### [32:04 - 32:07]

they correspond to almost the shortest path through this house

### [32:07 - 32:12]

this bird's eye view is one something we use just for visualization the robot doesn't actually get

### [32:12 - 32:20]

this bird's eye view and quantitatively we see that while those goal working skills on their own

### [32:20 - 32:27]

fail to solve the distant tasks by incorporating them into a planning method they can successfully

### [32:27 - 32:30]

reach the most distant goals succeeding over 95 percent of the time

### [32:33 - 32:37]

after showing these results in simulation we worked with collaborators to apply these methods

### [32:37 - 32:42]

to this outdoor robot shown here we gave an image of where we wanted it to go

### [32:44 - 32:48]

my fantastic collaborator drew who led this effort put a pizza on top of the robot

### [32:48 - 32:54]

because you see this robot was given a picture of the customer's door and so it could autonomously

### [32:54 - 33:00]

and in a contact-free way drop off the pizza at the customer's door this is in the middle

### [33:00 - 33:04]

of covet so contact-free pizza delivery was a very pressing problem for grad students

### [33:06 - 33:07]

these methods

### [33:07 - 33:11]

of combining learning and planning there's since been a lot of follow-up work that's extended the

### [33:11 - 33:16]

capabilities and lifted the limitations of these methods making them more robust making them

### [33:16 - 33:24]

generalize more broadly and to provide a bit of context here in ai very broadly there's been a

### [33:24 - 33:29]

long discussion about could we prefer planning methods or should we the reason about symbols

### [33:29 - 33:34]

or learning methods that can learn directly from the raw data and one reason i'm excited

### [33:34 - 33:36]

about this effort here is that it provides one recipe

### [33:36 - 33:38]

for combining these two math components together

### [33:41 - 33:46]

and so the takeaway from the second part of this talk is that these skills that we've learned

### [33:46 - 33:50]

using these self-supervised methods they provide the right abstraction for doing planning

### [33:52 - 33:58]

now step taking a step even further back i started this talk by mentioning why reinforcement learning

### [33:58 - 34:04]

is hard it's hard because of the limited feedback but what we've seen today is that we can learn

### [34:04 - 34:06]

goal-reaching skills and learn to do it better

### [34:06 - 34:11]

and we can use these skills without any rewards without any feedback and we can compose these

### [34:11 - 34:17]

skills to solve challenging tasks so i hope this has given you at least a little taste of some of

### [34:17 - 34:20]

the work in the thesis which i would encourage folks to go read about how we've developed

### [34:20 - 34:24]

practical algorithms theoretical guarantees for those methods as well as uncovering certain

### [34:24 - 34:27]

connections between reinforcement learning methods and machine learning methods and

### [34:27 - 34:34]

some other areas of computer science and the work that i've done it informs a lot of the work i'm

### [34:34 - 34:35]

excited to do moving forward

### [34:35 - 34:36]

so

### [34:36 - 34:39]

practically the next step is i will be joining princeton in the fall

### [34:40 - 34:44]

and there are a lot of research questions that i'm really excited to study with students there

### [34:46 - 34:50]

first and foremost there are some really exciting questions at the intersection of

### [34:50 - 34:55]

reinforcement learning and natural language processing over the last few years and even

### [34:55 - 35:01]

over the last few months we've seen some really impressive results from big ai models that can

### [35:01 - 35:06]

reason about both images and language what these methods typically lack

### [35:06 - 35:08]

is a grounded understanding of the world

### [35:11 - 35:15]

in contrast the methods that i've developed they can reason about actions and interacting

### [35:15 - 35:20]

with the world and images but they don't yet have an understanding of language of semantics

### [35:21 - 35:25]

how can we combine these two components together getting the strengths of both of them

### [35:27 - 35:31]

well it turns out the theoretical foundations of both these methods are the same they're both built

### [35:31 - 35:35]

on top of contrastive learning methods so i think there might be some really elegant ways of bringing

### [35:35 - 35:36]

them together

### [35:36 - 35:43]

and in the same way that we've shown already how we can learn goal reaching skills that can navigate

### [35:43 - 35:48]

to a goal image maybe now we can learn language reaching skills they can infer the sequence of

### [35:48 - 35:54]

actions to get to some language in the future or in the same way that the second part of this talk

### [35:54 - 36:00]

looked at inferring a sequence of steps to get to some distant goal maybe now we can infer

### [36:00 - 36:05]

the sequence of language instructions required to solve some challenging tasks

### [36:06 - 36:09]

in the future or in the same way that the second part of this talk looked at

### [36:09 - 36:14]

second a lot of the work that we've done and the work i highlighted in the second part of this talk

### [36:14 - 36:18]

is about finding structure it's about breaking down challenging problems and easier problems

### [36:21 - 36:26]

now the second part of this talk i showed how we could say given two images infer the sequence

### [36:26 - 36:31]

of images that you would visit between those two images but can we take this a step further

### [36:31 - 36:36]

can we for example learn skills to interact with the representations

### [36:36 - 36:41]

or can we learn skills that interact with other skills the results i've shown already extend the

### [36:41 - 36:47]

capabilities of skill learning methods by about an order of magnitude and if build adding a layer to

### [36:47 - 36:51]

this hierarchy if every layer extends the capabilities by another order of magnitude

### [36:52 - 36:55]

maybe now we can start solving tasks that are well well beyond the capabilities of today's

### [36:57 - 37:03]

we have some preliminary work showing how this might be done and i think that we might also be

### [37:03 - 37:05]

able to build upon some preliminary work

### [37:06 - 37:11]

fantastic older work on hierarchical basic modeling and then there's certain theoretical

### [37:11 - 37:15]

reasons why these methods might be better suited to the reinforcement learning problem

### [37:15 - 37:19]

because in reinforcement learning you can dynamically change your data distribution

### [37:22 - 37:26]

third and finally the work that i've talked about today there's really strong connections

### [37:26 - 37:31]

with generative modeling generative models they too are learned just from raw data

### [37:32 - 37:36]

given in a sentence like a castle in the mountains they can give you an image what that castle looks

### [37:36 - 37:43]

like when we view reinforcement learning as a generative problem we now get the recipe for

### [37:43 - 37:50]

building that castle of course actually figuring out how you would solve a problem as challenging

### [37:50 - 37:55]

as this is a really really hard problem it likely is going to require learning from very large

### [37:55 - 38:00]

amounts of data it likely is going to require the right representations the right sort of abstractions

### [38:00 - 38:03]

but these are all problems we've started to make progress on

### [38:05 - 38:05]

i think this

### [38:06 - 38:12]

making progress here it may unlock certain applications in gaming and creativity but

### [38:12 - 38:18]

also in the physical sciences in the sciences today generative models are already widely used

### [38:18 - 38:23]

save optimizing molecules and when we view these problems as reinforcement learning problems

### [38:24 - 38:30]

now we might get the recipe for actually running those experiments of course this too is a very

### [38:30 - 38:35]

challenging problem but i think that some of the work we've done might be useful towards this end

### [38:36 - 38:39]

some of the work on robustness and generalization that i didn't talk about today

### [38:39 - 38:44]

it tells you how you can make use of approximate models which is really common in scientific

### [38:44 - 38:49]

applications the work that i did talk about about learning directly from the outcomes i think that

### [38:49 - 38:53]

might be directly applicable because now we might be able to provide just examples of

### [38:53 - 38:56]

what some desired what the outcome of some experiment might look like

### [38:59 - 39:05]

so i'm going to wrap up the future work right here and i want to take a second to thank the fantastic

### [39:05 - 39:12]

team of collaborators not just here at cmu but at berkeley and other schools throughout the

### [39:12 - 39:27]

u.s north america and even around the world thanks and i want to give an especial thank you to my

### [39:27 - 39:35]

advisors sergey and russ for reading through hundreds or thousands of pages of notes and

### [39:35 - 39:42]

half-brained papers that never ended up seeing the light of day for sitting through and critiquing

### [39:42 - 39:48]

giving feedback on hundreds of hair-brained ideas the vast majority of which didn't work out

### [39:49 - 39:55]

but a very very small fraction of which turned into the work that you saw today and of the

### [39:55 - 40:02]

hundreds or thousands of emails and slack messages for keeping the research on track thank you

### [40:06 - 40:12]

thanks ben so um we're going to start with the questions um and i guess uh

### [40:12 - 40:16]

we're probably going to go with the most remote right now that would be

### [40:16 - 40:21]

well technically serene but we'll go with leslie uh leslie uh do you have any questions

### [40:22 - 40:28]

um sure so thank you ben that was good and interesting nicely presented um

### [40:30 - 40:35]

yeah so let's see i have questions of the high level and low level let's let's take some

### [40:35 - 40:41]

high level ones right which is um one thing that you talked about that I thought was interesting

### [40:41 - 40:49]

is you know we we could it's it's exciting to be able to learn from offline gathered data and in

### [40:49 - 40:57]

particular you had I think combinations of of like images and then robot actions and I was thinking

### [40:57 - 41:03]

have you played around with trying to extract in some sense the robot actions from the videos in

### [41:03 - 41:07]

other cases you could mostly see the robot moving around so that would be latent but you'd have

### [41:07 - 41:12]

pretty good information about it is that something that you have thought about so to make sure I

### [41:12 - 41:16]

understand the problem setting will be one where we're given just the videos without the actions

### [41:16 - 41:21]

and try to learn from that but where the actions were kind of not totally hidden in the video so

### [41:21 - 41:26]

that you could probably recover that it's really funny you mentioned that because just yesterday I

### [41:26 - 41:30]

scribbled all over my whiteboard some proposals for how we could do that and so there's an ongoing

### [41:30 - 41:33]

slack discussion exactly about a very relative

### [41:33 - 41:38]

question about how we can take action-free videos and then infer skills from that that

### [41:38 - 41:42]

action-free video there's action-free videos I think that some of these techniques about inferring

### [41:42 - 41:49]

structure um might be useful there yeah yeah okay that's cool so one more thing is and and in your

### [41:49 - 41:54]

final you know kind of future work also touched on it but I have since we've begun talking and

### [41:54 - 42:02]

in particular talking about goals yeah um for me you know a goal is a set uh you know am I in my

### [42:02 - 42:03]

officer

### [42:03 - 42:08]

we're not kind of and so using images as goals it's interesting because it's both under and

### [42:08 - 42:13]

over specified in a way right it's a little too specific because here it is this particular image

### [42:13 - 42:17]

and it's a little too General maybe because there's some parts of what matters to me that

### [42:17 - 42:26]

I can't see yeah so what about broadening what you take to be a goal so one way we've done this

### [42:26 - 42:30]

we've done this already in one contacts and then I think there's some exciting directions

### [42:30 - 42:32]

looking at going forward when we've looked at this already

### [42:32 - 42:36]

is by this extension of the goal reaching problems where we gave multiple examples

### [42:36 - 42:42]

and the aim here is that each example each goal image individually is definitely over specified

### [42:42 - 42:48]

and that when we want a robot to pick up an object we might not care what color what shape that

### [42:48 - 42:52]

object is we just wanted to pick it up or when we want the robot to clean some bedroom we don't care

### [42:52 - 42:56]

the order in which it stacks the books on top of the coffee table we just care that they end up

### [42:56 - 43:01]

stacked there and the aims that by providing multiple examples of good outcomes in the same

### [43:01 - 43:02]

way that an image classifier can see multiple

### [43:02 - 43:07]

examples of cats and say okay this is what a cat is that our methods might be able to know okay this

### [43:07 - 43:13]

is what success looks like I'm curious then they're now a technical point which is if you're

### [43:13 - 43:19]

going to be goal conditioned how do you manage that if the goal is articulated in the set of a

### [43:19 - 43:25]

large set of images yeah great question so the work that I'm referring to here the policies

### [43:25 - 43:30]

that are learned are not goal conditioned but just a state and then take the actions to try

### [43:30 - 43:32]

to lead to these goals but the critic the way

### [43:32 - 43:36]

they're inferring whether the actions believes that good outcomes those look at okay the likelihood

### [43:36 - 43:40]

of getting to one outcome like to get to another outcome and you probably can imagine how you can

### [43:40 - 43:45]

use this to estimate likelihood of getting to any or at least one outcome sure yeah okay good I get

### [43:45 - 43:58]

it um all right I think I'll pass the baton so um maybe go with uh Sergey sure um so in the

### [43:58 - 44:02]

beginning or towards the beginning you have this nice illustration of how

### [44:02 - 44:07]

representations learned with uh contrast of RL compared to like VEs and things like that and made

### [44:07 - 44:12]

this point that if you interpolate you kind of get these nice in between frames um that seems

### [44:12 - 44:18]

interesting but um my question is why do you think it matters to have a representation that's metric

### [44:18 - 44:25]

in that way I don't think that linear interpolation is necessarily what we want but I think the

### [44:25 - 44:30]

property that we really want is we want to go to do planning and so when we looked at those

### [44:30 - 44:32]

representations and I'll try to pull up

### [44:32 - 44:42]

um the example of them the here planning if we wanted to figure out what intermediate images

### [44:42 - 44:46]

would look like if you wanted to get from one observation to another observation we just

### [44:46 - 44:50]

correspond to taking the average of these representations and this is really important

### [44:50 - 44:54]

because if we want to solve long Horizon tasks breaking them into easier smaller easier tasks

### [44:54 - 45:00]

would be useful but as long as there's some easy way to do planning using the representations I

### [45:00 - 45:02]

think that's sufficient so I don't think we necessarily need to

### [45:02 - 45:06]

have linear interpolation in fact I think it very likely will harm us

### [45:07 - 45:13]

well okay but just to push on this a little bit more like um if you want to do planning let's say

### [45:13 - 45:20]

you want to do some like tree-based thing all you really need is a way to um like propose successors

### [45:20 - 45:27]

or evaluate a potential state as a successor to a given state um like none of that really says

### [45:27 - 45:31]

anything about what the representation should be it just says well that there needs to be a good model

### [45:32 - 45:38]

um so do you think that there's some relationship between the representation of the model and does

### [45:38 - 45:43]

the um does the geometric structure of the represents in particular matter like I guess

### [45:43 - 45:47]

that's what I'm not seeing he's like well what's the link between geometric structure and and

### [45:47 - 45:54]

planning in this case that you're trying to articulate the geometric structure makes us

### [45:54 - 46:00]

allows us to solve planning gives us closed form solution for planning another way we could do

### [46:00 - 46:01]

planning is by actually learning a planner so if you're in a virtual network or something like that

### [46:01 - 46:02]

I'm thinking if I represent some sort of are they or applications are essentiallyesta describe typical

### [46:02 - 46:06]

it takes as input a state and a goal and predicts what some intermediate states look like or some

### [46:06 - 46:11]

next state looks like i think there's a spectrum of methods based on how much of the representation

### [46:11 - 46:16]

how much representation learning they do and then how much model learning they do and in some sense

### [46:16 - 46:22]

we've pushed really far to one extreme where all of the horsepower is going into learning the

### [46:22 - 46:27]

representations and then the model learning drops out immediately from that and we could imagine

### [46:27 - 46:31]

methods that spend more computation on doing the planning and a bit less on learning the

### [46:31 - 46:35]

representations what's the right trade-off i don't know i think there's very likely methods

### [46:35 - 46:40]

sort of more in the middle that we haven't explored yet um i think it's interesting to

### [46:40 - 46:47]

explore the extremes to see well to exploit these dreams because if we can do all of if we can solve

### [46:47 - 46:51]

the entire planning problem with the representations then that might provide a

### [46:51 - 46:57]

recipe that us as academics can really benefit from because now we could offload the big large

### [46:57 - 47:01]

representation learning problem to collaborative

### [47:01 - 47:06]

and industry and then we might be able to very easily use the representations learned to actually

### [47:06 - 47:12]

solve the planning problems okay yeah that makes sense um i guess my other question is um

### [47:14 - 47:20]

so you know if we think of these things as good representation learning methods and kind of the

### [47:20 - 47:24]

obvious question to ask is well can we do what people always do with representation learning

### [47:24 - 47:28]

methods and train them on the largest like internet data so that we can get our hands on

### [47:28 - 47:31]

um i know that's something you've thought about a lot but i guess my question is

### [47:32 - 47:35]

what do you think are the bottlenecks that you'd start to hit if you were to try to do that

### [47:41 - 47:47]

i think one bottleneck is that internet scale data is incredibly broad but perhaps not very deep

### [47:48 - 47:50]

and one way i sometimes think about the reinforcement learning problem is that

### [47:50 - 47:55]

it's sort of like solving a supervised learning in every separate situation so solving many of

### [47:55 - 48:01]

these problems and if we don't have that many examples for any individual problem setting

### [48:01 - 48:05]

then even though we might have data for millions or billions of problems if we don't have enough

### [48:05 - 48:11]

data for any of them that might be hard to make progress and so one of the things that i think

### [48:11 - 48:15]

would be really useful is trying to figure out how we can collect a similar quantity of data but in

### [48:15 - 48:21]

a much much more limited setting i know this very much goes against the grain of what uh a lot of

### [48:21 - 48:28]

folks are excited about in terms of learning just from youtube or just from the twitter reddit um

### [48:28 - 48:31]

but i think that for the reinforcement learning prop setting it might be really important for at

### [48:31 - 48:35]

least making some initial steps towards understanding how much data you need to

### [48:35 - 48:39]

solve to see certain emergent properties on even relatively restricted domains

### [48:41 - 48:50]

okay now yeah that makes sense um that's it for my questions thank you jeff great uh let's see

### [48:51 - 48:55]

i'll start maybe with a kind of a low level question can you go to slide 13.

### [48:58 - 49:02]

um i don't know let's see

### [49:05 - 49:15]

so i i think the idea here is that you want an encoding that will make a state and action pair

### [49:15 - 49:23]

end up with almost the same encoding as a as a future state i think by itself

### [49:25 - 49:28]

and then that's the basis of what what happens after that

### [49:28 - 49:37]

my question is doesn't this have a weird side effect with with very stochastic actions

### [49:37 - 49:45]

that uh actions that have two very different outcomes this will force two very different

### [49:45 - 49:51]

outcomes to actually end up with an almost identical encoding when in fact those two

### [49:51 - 49:57]

very different outcomes it might be important that they don't get the same encoding is is that a

### [49:58 - 50:03]

potential problem does that yeah are stochastic actions generally more of a challenge with this

### [50:03 - 50:09]

approach i haven't applied to stochastic action so i can't give an empirical answer i agree that

### [50:09 - 50:14]

from a theoretical perspective it seems like this will work better in settings with deterministic

### [50:14 - 50:20]

actions the theory holds regardless of whether it's stochastic or um deterministic we can show

### [50:20 - 50:25]

that the inner product corresponds to a value function um but i don't think you can imagine

### [50:25 - 50:27]

that sort of tackling that multi-modality um

### [50:28 - 50:32]

could increase sample efficiency for example in some sense what we're trying to do is we're trying

### [50:32 - 50:39]

to learn incredibly complex representation such that once you have these representations the

### [50:39 - 50:46]

prediction problem is trivial but the prediction problem is often not trivial if you have possible

### [50:46 - 50:51]

stochastic outcomes instead of having a bit more expressive model that says okay given the current

### [50:51 - 50:56]

representation for your future representation they might allow you one much simpler representations

### [50:57 - 50:58]

so so

### [50:58 - 51:02]

let me see all right uh i'm trying to understand are you arguing that

### [51:03 - 51:13]

um that you should try this algorithm on problems with stochastic actions and maybe good things

### [51:13 - 51:20]

happen anyway or are you arguing that well maybe we can make some adaptations to the

### [51:20 - 51:27]

algorithm that'll make it perform better with stochastic actions or are you arguing that if you

### [51:28 - 51:33]

have a problem with stochastic actions you haven't really formulated the problem correctly you

### [51:33 - 51:38]

should re-re-ask what your statement actually action space is and make it a deterministic

### [51:38 - 51:43]

problem i'm definitely not saying the third i think that many real world problems that

### [51:43 - 51:48]

are have stochastic actions and those fit very nicely into the mdp framework upon which we built

### [51:48 - 51:53]

so i think that's fine i think you definitely should try these methods on settings with

### [51:53 - 51:57]

stochastic actions i think they very likely will work the point i was trying to make is that if you

### [51:58 - 52:00]

have a problem with stochastic actions and those fit very nicely into the mdp framework upon which

### [52:00 - 52:03]

we built so i think that's fine i think you definitely should try these methods on settings

### [52:03 - 52:06]

with stochastic actions and those fit very nicely into the mdp framework upon which we built

### [52:06 - 52:09]

dynamics in the real world are very very non-linear what effectively this is saying is

### [52:09 - 52:14]

that the representations are there's a way of showing that this corresponds to learning a

### [52:14 - 52:20]

linear model of the world and so you sort of have to untangle the complexity of the world

### [52:20 - 52:24]

the fact that dynamics are not reversible the things that breaking things is not reversible

### [52:24 - 52:27]

such that you get representations where things are linear so it's a very very complicated math to

### [52:27 - 52:28]

you get representations where things are linear so it's a very very complicated mapping and if we

### [52:28 - 52:33]

don't have function approximators that could represent that complexity then part of the way

### [52:33 - 52:38]

of dealing with that limitation of existing function approximators would be to use a more

### [52:38 - 52:45]

expressive mapping from one representation to another okay okay um good i think i want to ask

### [52:45 - 52:55]

another version of the question wesley asked my version of the question is um what what about

### [52:55 - 52:56]

distractors so

### [52:57 - 53:01]

you know you have the picture of the moving the spoon to the other side but

### [53:02 - 53:08]

what if it's just a different colored table and you know it would it would be very hard to figure

### [53:08 - 53:13]

out how to swap out the table but presumably you'd still want it to realize it just needs to move the

### [53:14 - 53:23]

spoon to the other side how do you in practice how do you actually get that similarity right

### [53:24 - 53:27]

i think that's a really important question i brought up this slide

### [53:27 - 53:33]

because this slide shows a similar failure mode if you look very carefully you'll notice that

### [53:33 - 53:37]

the rotation of the can is actually different between the two images

### [53:40 - 53:43]

and so how do we learn representations that capture just what we want and what we don't want

### [53:45 - 53:48]

i haven't looked at this problem in particular i think there are techniques

### [53:48 - 53:52]

relating to compression that might be useful here so i want representations

### [53:52 - 53:55]

that not only predict the future but retain as few bits as possible about the inputs

### [53:56 - 54:00]

i think techniques relating to data augmentation might also be useful

### [54:02 - 54:07]

but i think it's still a largely open question yeah i guess compression you could certainly

### [54:07 - 54:12]

look at compression techniques but one thing that's missing in your training data

### [54:14 - 54:17]

you don't actually have any notion of which differences matter

### [54:18 - 54:25]

right i guess a lot of compression algorithms have some version of

### [54:25 - 54:33]

entropy or reconstruction or something that's kind of generic yeah but i guess you you would

### [54:33 - 54:39]

actually need that extra signal i guess absolutely yeah if someone gave us a bunch of images and said

### [54:39 - 54:44]

hey you should think about all these things is the same if you think about pushing a green can

### [54:44 - 54:48]

and a red can and a purple can those are all the same tasks collapse all those together and if we

### [54:48 - 54:52]

had data like that then i definitely think there would be many ways that we could incorporate it

### [54:52 - 54:55]

into these sorts of frameworks okay

### [54:56 - 55:03]

um and i have a question that may be related to that can you scroll back to maybe slide 23.

### [55:06 - 55:12]

uh so this one went kind of fast do you see an iql failed here yeah what what

### [55:13 - 55:19]

what what what's the setup here what what actually happened with so this is the the same setup you

### [55:19 - 55:25]

have each other a bunch of videos things moving around different places yeah so they're really

### [55:25 - 55:30]

interesting failure mode yeah uh and did gloss over this so the failure mode is that there are

### [55:30 - 55:34]

two things that are different between the initial image and the goal image the first thing that's

### [55:34 - 55:38]

different is the red spoon moves yeah and the second thing that's different is that the robot

### [55:38 - 55:45]

arm moves and what this baseline does is it solves one of those problems it moves the arm to the

### [55:45 - 55:52]

correct position and my hypothesis for why this happens is that the arm occupies more of the image

### [55:52 - 55:53]

than the spoon

### [55:55 - 55:57]

and so it's stuck in a bit of a local optima

### [56:00 - 56:05]

now why would our methods help avoid that well we can think about the training dynamics

### [56:05 - 56:10]

of these contrastive methods what they're doing is they say okay look at these representations

### [56:11 - 56:15]

look at the future the images in the future and say those have similar representations

### [56:16 - 56:20]

and then look at not one but many many other representations and push those away

### [56:21 - 56:25]

those standard contrastive learning does yeah but if you look at the gradients there

### [56:26 - 56:31]

what effectively is doing is finding the closest negative example and pushing that away

### [56:35 - 56:39]

and so the i don't think we're the first to observe this but the training dynamics

### [56:39 - 56:43]

of contrastive learning methods resembles a form of hard negative mining it induces sort

### [56:43 - 56:48]

of curriculum and we have some analysis showing how that happens but it can help explain why it

### [56:48 - 56:53]

fails because in the um in the learning there should um they should be able to find counter

### [56:53 - 56:55]

examples where the arm is there

### [56:55 - 56:56]

This is okay.

### [56:56 - 56:57]

That is not the state that you would reach

### [56:57 - 56:59]

if you wanted to pick up the spoon.

### [57:02 - 57:03]

Okay, okay.

### [57:05 - 57:09]

Maybe one more question.

### [57:09 - 57:12]

So I'm guessing in the work you've done so far,

### [57:12 - 57:17]

you're, I guess, assuming the exploration problem

### [57:18 - 57:20]

is kind of solved for you.

### [57:20 - 57:21]

Yeah.

### [57:21 - 57:25]

The training data covers what you needed to cover.

### [57:25 - 57:26]

Yeah.

### [57:26 - 57:30]

Have you thought at all about whether your methods

### [57:30 - 57:33]

say anything about better exploration

### [57:33 - 57:36]

or what you would do for those kinds of problems?

### [57:36 - 57:36]

Yeah.

### [57:36 - 57:40]

So the skill learning methods I talked about at the beginning

### [57:40 - 57:41]

were these goal-reaching skills.

### [57:43 - 57:45]

The mathematical foundation of them is based on

### [57:45 - 57:46]

these sort of contrastive learning

### [57:46 - 57:48]

and mutual information ideas.

### [57:48 - 57:50]

And we've actually applied, at the very start of my PhD,

### [57:50 - 57:52]

started using very similar ideas

### [57:52 - 57:54]

to actually derive in a method for exploration.

### [57:54 - 57:58]

So I can pull up one video of that,

### [57:58 - 58:02]

of using very similar mathematical tools for learning skills

### [58:02 - 58:04]

here that are not oriented towards any particular goal,

### [58:04 - 58:07]

but just trying to explore the environment.

### [58:07 - 58:10]

So this is definitely not the end-all, be-all solution.

### [58:10 - 58:11]

There's been a lot of great subsequent work

### [58:11 - 58:13]

that's extended these methods and so on.

### [58:13 - 58:16]

But I think that there might be some ways

### [58:16 - 58:18]

of using similar self-supervised methods

### [58:18 - 58:20]

to not only learn the representations,

### [58:20 - 58:21]

learn how to do the planning,

### [58:21 - 58:23]

but also help drive the exploration.

### [58:23 - 58:24]

Okay.

### [58:24 - 58:25]

Thank you.

### [58:25 - 58:26]

Good.

### [58:26 - 58:27]

I think I'm good.

### [58:27 - 58:28]

I just have one question,

### [58:28 - 58:30]

maybe just to follow up on Jess' question,

### [58:30 - 58:36]

is that when these methods fail,

### [58:36 - 58:37]

does it usually sort of come from,

### [58:37 - 58:39]

especially, you know, these representations,

### [58:39 - 58:43]

does it usually come from not enough coverage of the data?

### [58:43 - 58:45]

So for example, let's say you've never seen spoons

### [58:45 - 58:47]

in the training,

### [58:47 - 58:49]

but you've seen a lot of other things

### [58:49 - 58:51]

and you're learning those representations,

### [58:51 - 58:53]

would you be able to move spoons?

### [58:54 - 58:57]

Or do you think that there's, you know,

### [58:57 - 58:58]

just trying to see like how much,

### [58:58 - 59:00]

is there sort of a condition of the coverage

### [59:00 - 59:04]

that you need to run these representations

### [59:04 - 59:07]

and how well they would do on new objects

### [59:07 - 59:10]

and new things to generalize the data?

### [59:10 - 59:13]

In the simulated setting, we studied this a little bit.

### [59:13 - 59:15]

So we showed, for example, that the,

### [59:15 - 59:17]

if you train on one color table,

### [59:17 - 59:19]

but you evaluate on a different color table,

### [59:19 - 59:20]

then it will fail,

### [59:20 - 59:22]

but you can perturb things to a smaller extent,

### [59:22 - 59:24]

like change just the colors of objects.

### [59:24 - 59:26]

And then these methods tend to still work.

### [59:27 - 59:30]

In terms of evaluating on things

### [59:30 - 59:32]

that are entirely outside of the data distribution,

### [59:32 - 59:34]

we tried this for one task

### [59:35 - 59:37]

on that real world robotic manipulation task.

### [59:37 - 59:39]

I think I was picking up a plastic baguette

### [59:39 - 59:42]

and I believe that it failed on that task.

### [59:42 - 59:43]

So we just-

### [59:43 - 59:46]

Is it because of perception or is it like,

### [59:46 - 59:48]

is it because it just doesn't recognize what it is

### [59:48 - 59:52]

or is there something else going on?

### [59:52 - 59:53]

I'm not entirely sure.

### [59:53 - 59:56]

We haven't probed whether it's the representation learning

### [59:56 - 01:00:01]

or the choosing the actions based on the representations.

### [01:00:02 - 01:00:03]

I think that for a lot of these things,

### [01:00:03 - 01:00:06]

looking at bigger and bigger data sets will likely help,

### [01:00:06 - 01:00:08]

but developing high-fidelity simulators

### [01:00:08 - 01:00:09]

might be really important there

### [01:00:09 - 01:00:10]

because it will allow us,

### [01:00:10 - 01:00:12]

it will tell us how much data we need

### [01:00:12 - 01:00:14]

to expect certain sorts of results.

### [01:00:14 - 01:00:15]

The reason why I'm asking is that I think

### [01:00:15 - 01:00:17]

that most of these sort of foundation models

### [01:00:17 - 01:00:18]

for computer vision,

### [01:00:18 - 01:00:20]

like they're becoming really good

### [01:00:20 - 01:00:22]

at like segmenting things and such.

### [01:00:22 - 01:00:23]

And it seems to be, there's some cases, for example,

### [01:00:23 - 01:00:23]

that they're not really good at segmenting things and such. And it seems to be, there's some cases,

### [01:00:23 - 01:00:23]

that they're not really good at segmenting things and such. And it seems to be, there's some cases,

### [01:00:23 - 01:00:26]

where learning policies in the simulator

### [01:00:26 - 01:00:27]

while applying them in real world

### [01:00:27 - 01:00:29]

with some of these sort of perception models

### [01:00:29 - 01:00:32]

actually begin to work reasonably well.

### [01:00:32 - 01:00:34]

So, yeah.

### [01:00:34 - 01:00:35]

So that's why I was curious,

### [01:00:35 - 01:00:38]

like how well you can actually take these models

### [01:00:38 - 01:00:39]

and apply them in the real world

### [01:00:39 - 01:00:41]

in new sort of set ones.

### [01:00:41 - 01:00:45]

Is it, provided perception is actually doing the right thing?

### [01:00:45 - 01:00:46]

Yeah, that's a really good point.

### [01:00:46 - 01:00:47]

We haven't looked.

### [01:00:47 - 01:00:49]

I guess one thing that,

### [01:00:50 - 01:00:53]

talk about a bit, a bit about is,

### [01:00:53 - 01:00:57]

when we talked about the foundation models here

### [01:00:57 - 01:00:58]

when I was focusing on language,

### [01:00:58 - 01:01:00]

we could imagine using very similar methods

### [01:01:00 - 01:01:03]

for just leveraging like large video data sets.

### [01:01:03 - 01:01:05]

And we learned the representation of the large videos

### [01:01:05 - 01:01:07]

that would tell you not only about the contents of the videos,

### [01:01:07 - 01:01:10]

but also something about the dynamics of the videos.

### [01:01:10 - 01:01:12]

Like if we think about the,

### [01:01:13 - 01:01:14]

I think historically the thing that has made

### [01:01:14 - 01:01:16]

reinforcement learning benchmarks hard

### [01:01:16 - 01:01:20]

is that they have lots of visual complexity,

### [01:01:20 - 01:01:23]

but the actual control problem is often very easy.

### [01:01:23 - 01:01:27]

But I think that might change over the next five, 10 years.

### [01:01:27 - 01:01:29]

We might see benchmarks where solving the perception problem

### [01:01:29 - 01:01:30]

becomes relatively easy,

### [01:01:30 - 01:01:32]

but solving the planning problem

### [01:01:32 - 01:01:33]

becomes a lot more challenging.

### [01:01:35 - 01:01:37]

And to tackle that sort of problem,

### [01:01:37 - 01:01:38]

I think that learning from,

### [01:01:38 - 01:01:41]

what videos tell you is what could happen in the future.

### [01:01:41 - 01:01:43]

They don't tell you how to make that happen.

### [01:01:43 - 01:01:45]

That would require inferring the actions

### [01:01:45 - 01:01:47]

or reasoning about what would actually take you

### [01:01:47 - 01:01:48]

from one frame to the next frame.

### [01:01:48 - 01:01:51]

Getting back to Lesley's earlier question.

### [01:01:51 - 01:01:53]

But they might tell us one way of incorporating the large video

### [01:01:53 - 01:01:54]

or the foundation models

### [01:01:54 - 01:01:56]

into these sort of self-supervised methods.

### [01:01:59 - 01:02:01]

Any questions from the audience?

### [01:02:02 - 01:02:04]

If you know, William and...

### [01:02:04 - 01:02:05]

Yes.

### [01:02:05 - 01:02:08]

Could you go over the intuition as to why the VAE

### [01:02:08 - 01:02:12]

doesn't learn the physics of the scene,

### [01:02:12 - 01:02:14]

but the contrasted member does?

### [01:02:14 - 01:02:17]

So this has to do with how the representations are learned.

### [01:02:17 - 01:02:25]

So the VAE that's learned here is learning static images.

### [01:02:25 - 01:02:28]

And so the VAE has never seen what could happen

### [01:02:28 - 01:02:30]

from one image to the next image.

### [01:02:30 - 01:02:33]

So is there no way you could put in like temporal dependencies

### [01:02:33 - 01:02:36]

in the VAE, or to get it to learn the physics?

### [01:02:36 - 01:02:38]

Yeah, you could imagine applying a sequential version

### [01:02:38 - 01:02:39]

of the VAE as a sequential VAE.

### [01:02:39 - 01:02:41]

This isn't standard practice

### [01:02:41 - 01:02:43]

for reinforcement learning benchmarks,

### [01:02:43 - 01:02:45]

but there's been a little bit of work there

### [01:02:45 - 01:02:45]

and we could try doing that.

### [01:02:45 - 01:02:47]

Yeah. But isn't that what like, you know,

### [01:02:47 - 01:02:51]

it's basically like a sequential VAE.

### [01:02:51 - 01:02:53]

So I'm like, I'm just curious,

### [01:02:53 - 01:02:54]

like what the contrasted learning part

### [01:02:54 - 01:02:57]

gives you that sequential VAE?

### [01:02:57 - 01:02:59]

I think there are two parts that it gives us.

### [01:02:59 - 01:03:02]

One is that it aligns the model

### [01:03:02 - 01:03:04]

or the representation learning part

### [01:03:04 - 01:03:06]

with the downstream task.

### [01:03:06 - 01:03:08]

So if we think about just fitting a model of the world,

### [01:03:08 - 01:03:10]

something that predicts the next image

### [01:03:10 - 01:03:12]

or the next representation of the image,

### [01:03:13 - 01:03:14]

based on reconstruction,

### [01:03:14 - 01:03:16]

there's no guarantees that the bits that were useful there

### [01:03:16 - 01:03:17]

are the same bits that are gonna be useful

### [01:03:17 - 01:03:18]

for selecting the actions.

### [01:03:18 - 01:03:20]

Very likely the bits that are important,

### [01:03:20 - 01:03:22]

they're like, what are the colors of the object?

### [01:03:22 - 01:03:24]

But that might not matter

### [01:03:24 - 01:03:26]

for solving certain control problems.

### [01:03:26 - 01:03:28]

Okay. So I think that actually kind of gets a bit

### [01:03:28 - 01:03:32]

to Jeff's distractor question too,

### [01:03:32 - 01:03:34]

because it sounds like the contrasting method

### [01:03:34 - 01:03:37]

might be more of us to distractors.

### [01:03:39 - 01:03:41]

It will retain different bits of information.

### [01:03:43 - 01:03:46]

One, so bits of information,

### [01:03:46 - 01:03:50]

it will ignore our bits that have nothing to do with,

### [01:03:50 - 01:03:51]

that are uncontrollable,

### [01:03:53 - 01:03:55]

but are persistent across episodes.

### [01:03:55 - 01:04:00]

And so what's an example of this?

### [01:04:03 - 01:04:06]

If there's like,

### [01:04:06 - 01:04:09]

if the object just disappeared randomly across time,

### [01:04:09 - 01:04:10]

like there's like a noisy TV

### [01:04:10 - 01:04:12]

in the background or something,

### [01:04:12 - 01:04:14]

there's no temporal correlation,

### [01:04:14 - 01:04:16]

we would ignore that.

### [01:04:16 - 01:04:17]

But it's not perfect.

### [01:04:17 - 01:04:18]

And I don't wanna claim like,

### [01:04:18 - 01:04:20]

oh, this is the panacea that you all should be using,

### [01:04:20 - 01:04:22]

because this method will pay attention

### [01:04:22 - 01:04:25]

to things like the background color.

### [01:04:26 - 01:04:29]

If every episode is a different background color,

### [01:04:30 - 01:04:32]

because the way these representations are learned

### [01:04:32 - 01:04:33]

are saying, okay,

### [01:04:33 - 01:04:37]

are these two images nearby in the same video?

### [01:04:37 - 01:04:39]

But one easy cue for that would be,

### [01:04:39 - 01:04:41]

well, if different videos have different colors,

### [01:04:41 - 01:04:43]

then you could sort of keep by picking up on that.

### [01:04:43 - 01:04:45]

And so in theory, they still work in those sorts of settings,

### [01:04:45 - 01:04:46]

but in practice,

### [01:04:46 - 01:04:47]

I'm acting that you might need much more data

### [01:04:47 - 01:04:50]

to learn in those sorts of settings.

### [01:04:50 - 01:04:50]

Thanks.

### [01:04:52 - 01:04:54]

Any other questions from the audience?

### [01:04:56 - 01:04:58]

And I got a question from the Zoom audience.

### [01:04:58 - 01:04:59]

Oh yeah, okay.

### [01:04:59 - 01:05:00]

Well, I'll leave it there on Zoom,

### [01:05:00 - 01:05:02]

and then maybe just one more and then we'll...

### [01:05:05 - 01:05:06]

Yeah, go ahead.

### [01:05:06 - 01:05:07]

Cool, sweet.

### [01:05:07 - 01:05:08]

Oh, awesome.

### [01:05:08 - 01:05:09]

Yeah, cool.

### [01:05:09 - 01:05:10]

Okay, so great talk.

### [01:05:10 - 01:05:13]

I have a question around like,

### [01:05:13 - 01:05:15]

what are your thoughts on like this,

### [01:05:15 - 01:05:19]

you know, there are history like this trade-off

### [01:05:19 - 01:05:24]

between having feature-rich representations on the one hand,

### [01:05:24 - 01:05:29]

and then like interpretability and sample efficiency, right?

### [01:05:29 - 01:05:31]

So it's almost like these...

### [01:05:31 - 01:05:32]

There's like some trade-off there.

### [01:05:32 - 01:05:34]

So like you know, towards pushing,

### [01:05:34 - 01:05:36]

increasing sample efficiency,

### [01:05:36 - 01:05:40]

it seems like we might have

### [01:05:40 - 01:05:45]

to go for feature representations that aren't as interpretable,

### [01:05:45 - 01:05:54]

So, I mean, that's like a claim but like I just curious to get your thoughts on like those, those those three dimensions.

### [01:05:54 - 01:05:58]

Yeah, I'll talk about the interpretability part first.

### [01:05:58 - 01:06:08]

So I think the representations we learn, they give us a certain sort of interpretability, the interpretability they give us is the likelihood that you get from one state to another state.

### [01:06:08 - 01:06:15]

I think that interpretability might be useful in a number of ways. Already we've shown how it's useful for driving the selection of actions.

### [01:06:15 - 01:06:22]

So it's okay, these are the good actions to take. But you could imagine it would also be useful for understanding where methods are likely to fail.

### [01:06:22 - 01:06:32]

For example, if you have a bunch of observations that you know are bad, you can use these representations to figure out the likelihood that you would ever visit those bad representations.

### [01:06:32 - 01:06:38]

One thing that's kind of weird here is that very often when we think about interpretability, we think about the coordinates of the representations.

### [01:06:38 - 01:06:48]

So you might look at the representations learned by some deep neural network and say, Oh, this coordinate corresponds to class representing dogs, and this coordinate corresponds to tree leaves.

### [01:06:48 - 01:06:55]

But what the representations here are doing is it's the represent the coordinates individually might not be interpretable.

### [01:06:55 - 01:07:07]

But the inner product between representations is the scale or quantity that might become interpretable, because that tells you the likelihood that you might visit, say, a state that has a tree leaf in it.

### [01:07:07 - 01:07:08]

So I think there's a lot to learn here.

### [01:07:08 - 01:07:12]

So let's do a straight off.

### [01:07:12 - 01:07:15]

Oh, thanks.

### [01:07:15 - 01:07:19]

So maybe we can quickly go over the second round.

### [01:07:19 - 01:07:25]

Just let's see, do you have any more questions.

### [01:07:25 - 01:07:27]

Leslie, I think you might be muted.

### [01:07:27 - 01:07:29]

Yeah, a train was going by.

### [01:07:29 - 01:07:31]

Okay.

### [01:07:31 - 01:07:37]

I saw something tantalizing on slide 40 but I didn't get a chance to look at it something about generalization, which is one of my favorite things.

### [01:07:37 - 01:07:39]

Yes.

### [01:07:39 - 01:07:53]

Oh broader generalization right okay so okay I had just a tiny bit of a bad reaction to the idea that planning can only happen once you have a graph, because there's lots of work that happens planning that doesn't necessarily involve creating your graph.

### [01:07:53 - 01:07:54]

Yeah.

### [01:07:54 - 01:08:06]

But what I was really thinking about when I heard you talking about this which is super cool like I like the idea of kind of coming up with this structure and kind of understanding what you can do locally and then patching that together.

### [01:08:06 - 01:08:21]

So I'm really concerned about generalization, and in particular like, how could we take learning to navigate in this one house and use it to help navigate in another house so what are your thoughts about about that.

### [01:08:21 - 01:08:23]

We tried this.

### [01:08:23 - 01:08:24]

Okay.

### [01:08:24 - 01:08:34]

And there is a slide, we're talking about it. Okay, so we tried on setting, we said.

### [01:08:34 - 01:08:35]

Okay.

### [01:08:35 - 01:08:39]

So there's definitely no way that you would be able to navigate in different houses that's just unrealistic.

### [01:08:39 - 01:08:52]

But what if we try to learn the same two components that those representations or that value function, and the policy, and not one many many houses.

### [01:08:52 - 01:09:04]

But wait, can I ask a question first, like, it doesn't even make sense, I think, or maybe you're going to tell me it does if I take an image from your house and image from my house and ask about the dot product What is that, what is that about.

### [01:09:04 - 01:09:19]

Yeah, so the way we did this was, we made one assumption that's perhaps non standard. So the assumption we said is that when you're in a new house, you're given a small number of images from that house, not videos but images and build this graph.

### [01:09:19 - 01:09:32]

And then you use that value function, and the policy you've learned, and the training houses to build a graph on the small number of images from the new house and traverse between these images.

### [01:09:32 - 01:09:33]

Interesting.

### [01:09:33 - 01:09:46]

So do you have a sense of what has to be, I mean, this clearly kind of wouldn't work all the time but I can see how it works some of the time do you have a, do you have a kind of a concise way of describing when you think it would work and when it

### [01:09:46 - 01:09:48]

would.

### [01:09:48 - 01:10:01]

Yes, my understanding is that the for it to work we need that the value function to give us reasonable estimates between states and for the policy to give us reasonable estimates for the best actions like given the current state and goal state.

### [01:10:01 - 01:10:02]

And I think now we're looking at what looks to be.

### [01:10:02 - 01:10:17]

much more standard machine learning problem where if we think about viewing what these as a center machine learning problems, then it's just a question of what are the testing houses in the distribution of training houses.

### [01:10:17 - 01:10:30]

And as we make the data set of training houses and testing houses larger and larger and assume that the drawn ID from the same underlying distribution of houses, they think it might be reasonable to expect that sort of generalization.

### [01:10:30 - 01:10:41]

Let me just test my understanding for one second right so imagine that in my house, it's like I don't know the kitchen is right next to the front door, and in your house it's a giant mansion and the kitchen is miles away from the front door.

### [01:10:41 - 01:10:45]

Then the value function for kitchen to front door is going to be pretty different.

### [01:10:45 - 01:10:55]

And the more houses we average that over the kind of less good it's going to be in specific, or am I missing a way to condition on the house is a really good point.

### [01:10:55 - 01:10:59]

So, I think you're right that the performance is going to be a lot lower.

### [01:10:59 - 01:11:00]

So, I think you're right that the performance is going to be a lot lower.

### [01:11:00 - 01:11:07]

And we also found this in practice that the first the difficult tasks resolving half of them, not 100% of them.

### [01:11:07 - 01:11:18]

And I think it's, there was likely bias and how this distribution of our houses was created. And so there was off kitchens are often maybe next to bathrooms and fridges were in kitchens.

### [01:11:18 - 01:11:29]

I think that's to solve fully general problems we would actually want to incorporate exploration into this to think about well, given this graph, how do we visit every node on this graph also biasing us towards the high likelihood node.

### [01:11:29 - 01:11:33]

I think it's got suggest point earlier.

### [01:11:33 - 01:11:38]

Together with my collaborator drew for mentioned before we've explored this a little bit in the outdoor navigation setting.

### [01:11:38 - 01:11:51]

But these still lots of open questions. Yeah, I mean I think probably you want a hierarchical model in the end right you wanted to revert to what you know about houses in general, until you've explored this one a little more and then somehow let that take over,

### [01:11:51 - 01:11:55]

but yeah.

### [01:11:55 - 01:11:57]

Okay.

### [01:11:57 - 01:11:58]

Good. Next.

### [01:11:58 - 01:11:59]

Next.

### [01:11:59 - 01:12:02]

Do you have any more questions.

### [01:12:02 - 01:12:15]

Yeah, I actually wanted to push on some points that are maybe related to what Leslie brought up as I think that's something you're kind of sweeping under the rug with the sort of example and I think this to some degree is present the other task was especially visible

### [01:12:15 - 01:12:23]

here is that you're sort of shoehorning partially observed problems into a fully observed formulation.

### [01:12:23 - 01:12:28]

And I wonder if you have any thoughts like if you were to actually approach this properly as a partially observed problem.

### [01:12:28 - 01:12:37]

How do you think the methodology would need to change.

### [01:12:37 - 01:12:44]

There's the trivial answer, which is well if you incorporate all the past history than the personal observe problems become fully observed.

### [01:12:44 - 01:12:52]

But I think that's complicated by two things, practical things and are relating to architectures and stochasticity.

### [01:12:52 - 01:12:56]

So, the first is actually taking into account the whole past history is going to be really hard.

### [01:12:56 - 01:12:57]

In terms like how do we.

### [01:12:57 - 01:13:05]

We could shove that into whatever newest transformer we have, but that might require very very long contexts.

### [01:13:05 - 01:13:21]

So I think there might be certain ways of one we could imagine approaching this is by learning models that for varying lengths of context, and seeing at what context length to these methods actually start getting reasonable performance.

### [01:13:21 - 01:13:26]

And hopefully we'd see that okay performance is low for small context but then increases and at around the context length of 10.

### [01:13:26 - 01:13:36]

Then you're able to solve tasks reasonably well there's also this problem of stochasticity, which is a little bit subtle.

### [01:13:36 - 01:13:43]

But I think that when we think about partially observed tasks and map them on to Mdps by including history.

### [01:13:43 - 01:13:50]

They are going to likely be much more stochastic than the tasks we ordinarily think about solving.

### [01:13:50 - 01:13:55]

And I think it's possible that probabilistic methods might work a lot better in those sorts of settings.

### [01:13:55 - 01:14:05]

If we think about what because we need to exactly reason about, say, the likelihood or the probability of something happening in the future.

### [01:14:05 - 01:14:08]

But integrating out all of the intermediate outcomes.

### [01:14:08 - 01:14:21]

And we've seen exactly how ignoring that stochasticity can cause problems for other sorts of reinforcement learning methods, in particular ones based on conditional supervised learning.

### [01:14:21 - 01:14:23]

Yeah, that makes sense for what it's worth.

### [01:14:23 - 01:14:28]

I don't think it's going into a giant transformer and just using that that as your representation is that terrible.

### [01:14:28 - 01:14:34]

But yeah, good good answer. I don't have any other questions.

### [01:14:34 - 01:14:49]

I'm debating whether I have another question. I was just thinking about the new houses problem, and just trying to figure out whether when you go into a new house you need a fundamentally different strategy because you're not you're not really in the

### [01:14:49 - 01:14:52]

learning to navigate. You're just doing exploration.

### [01:14:52 - 01:14:57]

I don't know about whatever and you're just running an exploration algorithm.

### [01:14:57 - 01:15:03]

Maybe it's biased a little bit by where you usually see these things in other houses.

### [01:15:03 - 01:15:21]

I'm just trying to understand whether I believe the answer is you're just running a completely different policy, and maybe you shouldn't be training a completely different policy, or whether the answer is when you go in a new house you actually run your policy as if it were in

### [01:15:21 - 01:15:22]

the training data.

### [01:15:22 - 01:15:27]

You're adding the new data you collect as you go, and that works.

### [01:15:27 - 01:15:35]

It converges. I think there's a question there, but i'm just still thinking what I was thinking while you were talking.

### [01:15:35 - 01:15:47]

Yeah, that's really interesting. Exactly. I was going to mention seems related to Leslie's points about hierarchical designs being useful, because the low-level motor control problem is very likely going to be the same but the high level

### [01:15:47 - 01:15:51]

problem. It might not before I was talking about solving the shortest path problem on the scrap.

### [01:15:51 - 01:16:04]

But now you want to solve some sort of traveling sales in progress, and sort of vehicle routing problem on the scrap

### [01:16:04 - 01:16:08]

Maybe just one more question from the audience.

### [01:16:08 - 01:16:20]

Yeah, so

### [01:16:20 - 01:16:35]

maybe

### [01:16:35 - 01:16:43]

by discrete space of solutions. Are you thinking about the observation?

### [01:16:43 - 01:16:49]

Yeah, we've looked at discrete actions in a couple. I don't think I showed any results for here.

### [01:16:49 - 01:16:51]

But the mathematical tools end up being the same.

### [01:16:51 - 01:17:02]

The difference is that when you're extracting the skills

### [01:17:02 - 01:17:04]

You just consider a discrete number of skills.

### [01:17:04 - 01:17:10]

So I think this slide makes a lot more sense in the streets in the setting with discrete actions.

### [01:17:10 - 01:17:16]

So you can enumerate. So you have 4 actions. Look at the representations and choose the best one.

### [01:17:16 - 01:17:29]

Continuous actions. We actually did a form of amortized optimization for learning the corresponding policy here.

### [01:17:29 - 01:17:33]

Okay. So then maybe we should there are no more questions.

### [01:17:33 - 01:17:41]

Thank you, Ben.

### [01:17:41 - 01:17:43]

Everybody else, and everybody was doing as well.

### [01:17:43 - 01:17:44]

So.

### [01:17:44 - 01:17:45]

Okay.

### [01:17:45 - 01:17:52]

So,

### [01:17:52 - 01:18:05]

ask people to you have a way of keeping people out of the right.

### [01:18:05 - 01:18:07]

And i'm gonna stop the recording. Yeah, Yeah.
