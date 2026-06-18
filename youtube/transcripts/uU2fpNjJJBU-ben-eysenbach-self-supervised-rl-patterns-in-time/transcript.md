# Self-Supervised Reinforcement Learning and Patterns in Time Benjamin Eysenbach

- URL: https://www.youtube.com/watch?v=uU2fpNjJJBU
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T13:52:32`

## Transcript

### [00:00 - 00:11]

And I'm Ben Eysenbach.

### [00:11 - 00:13]

I'm an assistant professor of computer science here at Princeton.

### [00:13 - 00:19]

And this talk is largely about research that my students and I have been doing over the last year or so.

### [00:19 - 00:28]

And it's largely about how my students have changed my mind, how I think about AI differently today than I did a couple years ago because of the research that we've done.

### [00:28 - 00:32]

And it's about problems that I thought were supposed to be hard that turned out not to be so hard.

### [00:34 - 00:41]

And as a bit of a preface, today's talk is going to be about AI agents, AI agents that make decisions.

### [00:42 - 00:46]

And I think often when people think about AI agents today, they think about language models.

### [00:47 - 00:50]

They think about Gemini, they think about chat, QPT, they think about other tools like this.

### [00:51 - 00:54]

But I think that's just the current zeitgeist.

### [00:54 - 00:58]

A couple years before this, people used to think about AI agents as reinforcement.

### [00:58 - 01:02]

Things like AlphaGo, things that were really good at maximizing rewards.

### [01:04 - 01:06]

And in today's talk, I want to argue that there's a third way.

### [01:07 - 01:09]

There's a third way of building AI agents.

### [01:10 - 01:12]

Self-supervised agents.

### [01:12 - 01:15]

Agents that are not learned by reading text on the internet.

### [01:16 - 01:20]

Agents that are not learned by trying to maximize the score in a game.

### [01:20 - 01:24]

But agents, rather, that are trained by trying to find patterns in the physical world.

### [01:25 - 01:26]

And then use those patterns for disinformation.

### [01:26 - 01:26]

Okay.

### [01:28 - 01:34]

So if you take away one thing from this talk is that when we think about agents, when we think about acting in the world,

### [01:34 - 01:38]

we don't necessarily need to say, we're going to take a giant language model and use that.

### [01:38 - 01:41]

There are other compelling ways of building agents.

### [01:44 - 01:45]

So I want to start with a thought experiment.

### [01:46 - 01:48]

Why do we use deep learning?

### [01:49 - 01:49]

Why deep?

### [01:52 - 01:55]

I think often when we think about deep learning, we think about a sort of fuzzy magic.

### [01:56 - 01:58]

Where if I give you an image.

### [01:58 - 02:07]

And you learn to predict this in the cat and I give you a new image of a slightly different cat, you can still recognize that this is a cat.

### [02:07 - 02:13]

You're not, you're sort of doing this sort of fuzzy night King saying this, this cat looks similar to a cat I've seen before.

### [02:13 - 02:20]

And therefore as you label it, looking now under the plate, what's happening is a lot more powerful.

### [02:21 - 02:25]

I keep learning about what they're doing is they're automatically finding patterns in your data.

### [02:26 - 02:27]

It turns out, look at the layer.

### [02:27 - 02:28]

It's your deep learning.

### [02:28 - 02:36]

You find that they're automatically learning to identify edges in these images and objects in these images, entire scenes in these images.

### [02:39 - 02:45]

And so I think I'd argue deep learning methods are, they're finding patterns in space, finding patterns in their training data.

### [02:49 - 02:52]

I come from a reinforcement learning background and it's typically,

### [02:56 - 02:58]

typically when I think about reinforcement learning.

### [02:58 - 03:08]

We're thinking about maximizing rewards about things like trading stock stock that plenty of video games to try to get a high score about educational outcomes.

### [03:08 - 03:22]

How do I give different problems to students so that they, so that they master material by the end of the semester, but how standard yeah, what, uh, Daniel, would you mind muting your microphone?

### [03:24 - 03:24]

Okay.

### [03:24 - 03:27]

I thought you want me to turn on, but I think I have to turn off.

### [03:27 - 03:27]

Okay.

### [03:28 - 03:31]

Great.

### [03:31 - 03:31]

Cool.

### [03:31 - 03:37]

Um, but how the standard, the standard reinforcement learning textbook defines reinforcement learning.

### [03:38 - 03:40]

They argue that it's really not about finding patterns.

### [03:41 - 03:47]

They say reinforcement learning is different from the self-supervised methods and that reinforcement learning is not trying to find hidden structure.

### [03:48 - 03:58]

In today's talk, I want to argue that this isn't necessarily true, that it might be possible to find structure in the solutions to decision-making problems.

### [03:58 - 04:06]

Why did you could find that sort of hidden structure, hidden structure and what you could see hidden structure and how you act in structure and how you plan.

### [04:06 - 04:13]

What if there existed reinforcement learning algorithms that didn't find patterns in data, what sort of capabilities would that unlock?

### [04:14 - 04:23]

So in the same way that these image models, these deep learning image models can find patterns in images of cats, I'm going to talk about finding patterns in time.

### [04:24 - 04:27]

We'll see how uncovering temporal patterns gives us new notions of generalization.

### [04:27 - 04:28]

We'll see how uncovering temporal patterns gives us new notions of generalization.

### [04:28 - 04:32]

allowing us to learn from lost data, and it will give rise to surprising sorts of exploration.

### [04:33 - 04:37]

It will allow us to explore wide, open-world environments more effectively.

### [04:39 - 04:42]

And so that first half of the talk, we'll talk about how we find about hunting for these patterns.

### [04:44 - 04:46]

So what exactly is a temporal pattern?

### [04:47 - 04:52]

Well, one way of talking about a temporal pattern is that it's really a description of behavior.

### [04:53 - 04:57]

If you see this woman here running through a city, you can describe what she's doing as

### [04:57 - 04:59]

jogging down a busy street.

### [05:00 - 05:04]

And that's a relatively compact, short description of the scene.

### [05:05 - 05:09]

Another way of describing a temporal pattern is that it's a form of temporal abstraction.

### [05:10 - 05:12]

You might think of things like options or skills.

### [05:12 - 05:13]

These have been well studied in the literature.

### [05:14 - 05:15]

I'll talk more about the prior work in a couple slides.

### [05:16 - 05:22]

Maybe a third definition of a temporal pattern is, I could introduce it by way of analogy.

### [05:22 - 05:27]

A temporal pattern is akin to what computer vision models find in space.

### [05:28 - 05:36]

And so when we think about patterns in this sort of image here, they really are two orthogonal axes.

### [05:37 - 05:40]

There's this space axis, and there's this time axis.

### [05:41 - 05:44]

And computer vision models, they try to find patterns along this space axis.

### [05:45 - 05:51]

They might recognize that, say, this patch of a fence, this looks sort of similar to a patch of a fence I've seen before.

### [05:51 - 05:57]

And so once they've learned to identify this fence near the top, I can also identify this fence near the bottom.

### [05:58 - 06:01]

Temporal patterns are looking at this orthogonal axis, this axis of time.

### [06:02 - 06:08]

And they're saying, hey, once I can identify this snippet of motion, I can also recognize this other snippet of motion.

### [06:11 - 06:16]

In general, recognizing patterns in our data gives us a form of generalization.

### [06:16 - 06:19]

It allows us to continue to make predictions on inputs we haven't seen before.

### [06:20 - 06:23]

Identifying these patterns, identifying the structure, it allows for faster learning.

### [06:24 - 06:27]

One way of thinking about this is a bit like Oregonic.

### [06:27 - 06:33]

Where if you take this image, you can fold it up on top of itself, because the top half and bottom half look similar.

### [06:33 - 06:36]

And this means that you now have half the number of pixels you have to look at.

### [06:36 - 06:39]

You also can fold up the image along the time dimension.

### [06:40 - 06:45]

And folding up the image along the time dimension allows you to solve decision-making problems much more quickly.

### [06:48 - 06:51]

Okay, so how would we go about finding these sorts of temporal patterns?

### [06:52 - 06:55]

Finding these temporal patterns is a big open problem in the field.

### [06:55 - 06:57]

And I want to talk about some details of this big open problem.

### [06:57 - 06:57]

And I want to talk about some details of this big open problem.

### [06:57 - 06:58]

So let's get to the question.

### [06:59 - 07:05]

One aspect is, how can we learn temporal patterns directly via end-to-end learning?

### [07:06 - 07:11]

A second is, how can we learn very large numbers of these temporal patterns?

### [07:12 - 07:16]

The benefit of learning a large number of patterns is that they can facilitate generalization.

### [07:17 - 07:20]

It means that after we've learned some number of patterns on our training data,

### [07:21 - 07:24]

we might be able to try new patterns or find new patterns in our testing data

### [07:24 - 07:26]

that we haven't explicitly seen before during training.

### [07:27 - 07:31]

One way to see this is by way of analogy.

### [07:32 - 07:36]

So I think the way that temporal patterns historically have been conceived

### [07:36 - 07:39]

is by saying that we're going to learn five or ten discrete patterns

### [07:39 - 07:42]

and use those to solve new tasks.

### [07:42 - 07:46]

But if this is the case, what does it mean to try to use

### [07:46 - 07:50]

pattern number nine and three quarters to solve a new task?

### [07:50 - 07:51]

I don't know.

### [07:51 - 07:52]

Like, this doesn't really compute.

### [07:52 - 07:54]

So I think that when we're thinking about patterns,

### [07:54 - 07:57]

we should be thinking not about a finite number of patterns,

### [07:57 - 07:57]

but really,

### [07:57 - 07:59]

but an infinite number of patterns.

### [08:02 - 08:05]

And then the last question that I want to focus on today is,

### [08:05 - 08:08]

how can finding these sorts of patterns accelerate learning?

### [08:09 - 08:13]

And there's the standard argument that the complexity of solving a decision-making problem,

### [08:13 - 08:19]

if you have to read over a long horizon, a horizon of length h,

### [08:19 - 08:23]

then the difficulty of doing that scales exponentially with a horizon.

### [08:23 - 08:25]

But if you can find patterns in time,

### [08:26 - 08:27]

then this shrinks the length of it,

### [08:27 - 08:29]

and this is an effective horizon.

### [08:29 - 08:32]

And so now the space you have to search for is much smaller.

### [08:35 - 08:38]

There's also a perception argument that by finding these sorts of patterns,

### [08:39 - 08:43]

we now no longer need to explore states that look similar to states we've seen before.

### [08:43 - 08:46]

This should significantly accelerate the exploration problem.

### [08:47 - 08:50]

And there's also a planning aspect to this as well,

### [08:50 - 08:52]

namely, after we've learned how to solve some tasks,

### [08:52 - 08:57]

we don't need to go learn how to solve tasks that look similar to tasks we've seen before.

### [08:58 - 09:00]

So if we would find these temporal patterns,

### [09:00 - 09:02]

it seems like they'd open up a number of important avenues.

### [09:05 - 09:07]

There's several approaches for learning these sorts of temporal patterns.

### [09:08 - 09:10]

For the sake of time, I'm going to gloss over most of the details now.

### [09:11 - 09:13]

But needless to say, there's been a lot of study in the literature

### [09:13 - 09:15]

that we did see methods have certain limitations,

### [09:15 - 09:20]

such as having to learn lots of structure from a small amount of feedback.

### [09:22 - 09:26]

Compression-based methods often require having lots of data to start with a priori.

### [09:27 - 09:33]

But we'll see today how there's a really special piece of these compression-based methods,

### [09:33 - 09:35]

methods based on finding patterns in time,

### [09:36 - 09:42]

that fill up several limitations from these hierarchical methods,

### [09:42 - 09:44]

because they end up finding lots and lots of additional training data.

### [09:45 - 09:48]

And it will turn out that there's a very close mathematical connection

### [09:48 - 09:51]

between these temporal contrast methods

### [09:51 - 09:55]

and perhaps the third class of approaches for finding patterns in time,

### [09:55 - 09:57]

those based on successor representations.

### [09:57 - 10:01]

These successor representations have been well-studied in neuroscience.

### [10:02 - 10:06]

Okay, so I want to start by going over what is this contrastive learning

### [10:06 - 10:07]

that I've been talking about.

### [10:08 - 10:10]

And then I'll talk a little bit about how we can use it for decision-making.

### [10:11 - 10:14]

We'll start by talking about how people have used contrastive learning

### [10:14 - 10:15]

for computer vision applications.

### [10:18 - 10:20]

There, what we try to do is we try to take an image

### [10:20 - 10:22]

and learn a representation of that image.

### [10:23 - 10:25]

And the goal is that if you have a similar image,

### [10:25 - 10:27]

say this other image of a cat,

### [10:27 - 10:29]

it has a similar representation.

### [10:30 - 10:32]

And importantly, if you look at other images, say an image of a dog,

### [10:33 - 10:36]

the dog has a representation that's pretty different

### [10:36 - 10:37]

than the representations of cats.

### [10:38 - 10:43]

Now, the key operation that makes this work is augmentation, data augmentation.

### [10:43 - 10:47]

You should be able to take an image and then rotate that image or crop that image

### [10:47 - 10:51]

or change the brightness of that image to create some other similar image.

### [10:51 - 10:53]

And that is what you use for training.

### [10:54 - 10:57]

Now, the line of work that I do is in decision-making.

### [10:57 - 11:01]

And so, we have to think carefully about what would be the right form of augmentation

### [11:01 - 11:03]

to do for decision-making.

### [11:04 - 11:06]

And it turns out that in the context of decision-making,

### [11:06 - 11:10]

nature, physics, tells us how to do the augmentation.

### [11:11 - 11:13]

So, let me walk you through how we do that.

### [11:15 - 11:18]

So, we start with videos, say the sequence of images

### [11:18 - 11:20]

showing a robot picking up a block.

### [11:21 - 11:23]

And again, we're going to learn representations,

### [11:23 - 11:26]

representations of each of the frames in this video.

### [11:27 - 11:29]

And we're going to learn the representations.

### [11:29 - 11:33]

So, the images that occur nearby in time have similar representations

### [11:33 - 11:37]

and images that occur far apart in time have dissimilar representations.

### [11:39 - 11:42]

Now, as you'll recall, when we're doing this contrastive learning,

### [11:42 - 11:44]

the key operation was augmentation.

### [11:44 - 11:47]

Given one image, you have to create another similar image.

### [11:48 - 11:53]

But when we're dealing with videos, time or physics tells us how to do the augmentations.

### [11:53 - 11:56]

Namely, just by looking at one image,

### [11:57 - 12:02]

I can generate another possible image that should have a similar representation,

### [12:02 - 12:04]

but I guess jumping forward in time.

### [12:04 - 12:06]

Now, this is really powerful.

### [12:09 - 12:12]

After we saw these methods, one of the questions we looked at was,

### [12:12 - 12:16]

how can we use these sorts of representations for decision-making for control?

### [12:16 - 12:20]

How can we use these sorts of representations, not for just understanding what a robot is doing,

### [12:20 - 12:22]

but actually for controlling that robot?

### [12:24 - 12:26]

And this gave rise to a method that I'll refer to as contrastive learning.

### [12:26 - 12:27]

And this gave rise to a method that I'll refer to as contrastive learning.

### [12:27 - 12:27]

And this gave rise to a method that I'll refer to as contrastive learning.

### [12:27 - 12:28]

And this gave rise to a method that I'll refer to as contrastive reinforcement learning.

### [12:28 - 12:30]

And this gave rise to a method that I'll refer to as contrastive reinforcement learning.

### [12:30 - 12:33]

The approach here is very similar to what I described before,

### [12:33 - 12:37]

where we're learning representations for representations that now take as input

### [12:37 - 12:39]

both an image as well as an action.

### [12:40 - 12:42]

And so, these representations here,

### [12:42 - 12:45]

they tell us both about the image that produced this representation,

### [12:45 - 12:47]

but also about the corresponding action.

### [12:48 - 12:52]

And this dependence on actions is important because we'll be able to use these representations

### [12:52 - 12:57]

for figuring out what action we should use for figuring out how to get to some design.

### [12:57 - 13:03]

some desired outcome. So I'll walk you through how that works. Let's say that the world looks

### [13:03 - 13:09]

like this. We have a robot. It has an object, maybe has several objects. And let's say that

### [13:09 - 13:14]

we would like the world to look like this. We would like the robot to figure out how do you

### [13:14 - 13:18]

go and pick up this object and pick it up and move it over and put it down and let go of it.

### [13:19 - 13:21]

That's what we would like the robot to figure out how to do.

### [13:21 - 13:28]

And for simplicity, let's imagine that we have just two actions, action one and action two.

### [13:29 - 13:33]

And we can use these representations that we've learned to figure out which of these two actions

### [13:33 - 13:39]

would be better for getting to this eventual goal state. Namely, we can look at the representations

### [13:39 - 13:45]

and just based on these representations, we can predict would action A1 or action A2 would be

### [13:45 - 13:50]

more likely to get us to the goal state. So we can just look at the similarity between these

### [13:50 - 13:51]

representations and we can predict would action A1 or action A2 would be more likely to get us to

### [13:51 - 13:56]

the goal state. And based on this, it seems like action A2 was the one that would get us

### [13:56 - 14:01]

closer towards the goal. So that's the action that we'll take. And we do this over and over

### [14:01 - 14:06]

again, every kind of step, seeing which action would get us closer towards the goal and repeat

### [14:06 - 14:12]

this. Importantly, we do this from scratch. We don't need any demonstrations. We don't need to

### [14:12 - 14:17]

have a model of the world. We don't need a big VLN. We don't need a language model. We just have

### [14:17 - 14:20]

the robot. It takes some random actions. It learns from those representations. It learns from those

### [14:20 - 14:25]

representations. It takes some more random actions. It learns from those representations.

### [14:25 - 14:33]

And so it's entirely good strapped from scratch. One way of interpreting what's happening here is

### [14:33 - 14:39]

that it's learning how to work the space of states. Rather than thinking in the space of images,

### [14:39 - 14:44]

it's thinking in the space of representations. So the space of representations is warped so

### [14:44 - 14:50]

that greedy planning is walking right directly from point A to point B in a straight line becomes

### [14:50 - 14:57]

more important. Importantly, this doesn't require any rewards. It doesn't require any

### [14:57 - 15:02]

demonstrations. It doesn't require any RLHF. And so compared to other reinforcement learning

### [15:02 - 15:06]

algorithms that you might consider or may have heard of before, this is likely much simpler.

### [15:08 - 15:12]

So at this point, you might be wondering, okay, this seems nice. It seems like a nice heuristic.

### [15:12 - 15:14]

Do you have any guarantees that this is going to work?

### [15:15 - 15:20]

And in fact, we can prove that this is a reasonable thing to do mathematically.

### [15:20 - 15:24]

We can show that when you're looking at these representations and using them for decision

### [15:24 - 15:28]

making, this is grounded in the theory of reinforcement learning. And particularly,

### [15:28 - 15:32]

you can show that the similarity between these representations very

### [15:32 - 15:35]

closely corresponds to the sum of rewards that you'll get.

### [15:41 - 15:44]

What this means is that acting greedily isn't a heuristic,

### [15:44 - 15:48]

but actually is a very reasonable thing to do. Is there a question there?

### [15:50 - 15:51]

Just raising your hand.

### [15:59 - 16:05]

Oh, yeah, yeah. So no worries. I'm just sharing the screen so other people can also,

### [16:05 - 16:07]

you can see the other people here.

### [16:08 - 16:12]

Great. Cool.

### [16:14 - 16:19]

It turns out these representations have lots of really beautiful geometric properties. If folks

### [16:19 - 16:20]

remember from their

### [16:20 - 16:26]

geometry classes back in math classes, there's this notion of a triangle inequality. This

### [16:26 - 16:30]

triangle inequality is really, really beautiful and powerful. And in fact, basically underlies

### [16:30 - 16:34]

all of dynamic programming that we've learned in our computer science classes. And these

### [16:34 - 16:37]

representations, they obey the triangle inequality, and this gives rise to important

### [16:37 - 16:44]

generalization properties. And in fact, these representations support a form of probabilistic

### [16:44 - 16:49]

inference. And so for folks familiar with graphical models, you inherit many of the

### [16:49 - 16:50]

nice properties that you get there.

### [16:50 - 16:57]

Probably there are several ideas in the literature, and you can mathematically relate

### [16:57 - 17:02]

several of these ideas. And so I think for folks that are new to the reinforcement learning area,

### [17:02 - 17:07]

if you've heard things like successor representations or latent space models

### [17:07 - 17:11]

or forward-backward representations, I think all of these things are pointed in similar directions.

### [17:12 - 17:16]

And so from a scientific perspective, this is really aesthetically pleasing because it means

### [17:16 - 17:20]

that they're really likely one grand unified theory that helps connect all these pieces.

### [17:20 - 17:25]

I don't know what that theory is. All I know is that a lot of work is pointing in similar directions,

### [17:25 - 17:29]

and I'm really excited to run in that direction and see what's out there to really better understand

### [17:29 - 17:35]

the science of these decision-making algorithms. So just to summarize how this complete method works,

### [17:36 - 17:41]

we'll start with some data, maybe it's random data, a robot or other agent doing things.

### [17:41 - 17:49]

We then learn these representations from these data, and then we select actions by just acting

### [17:49 - 17:50]

credibly.

### [17:50 - 17:53]

It's as simple as possible if using the representations for decision-making.

### [17:55 - 17:59]

You could use this policy and then go back and collect more data and repeat this loop.

### [18:01 - 18:07]

One thing to emphasize here is this is the entire algorithm. We didn't start with a pre-trained

### [18:07 - 18:12]

language model. We didn't start with a whole bunch of demonstrations from having humans

### [18:12 - 18:18]

tele-operate robots. We're not doing R like Chef. We're not doing GRPO. This is the entire algorithm.

### [18:18 - 18:20]

The entire algorithm that's taking care of this.

### [18:20 - 18:23]

We have some of the same data, learned representations, act credibly to

### [18:23 - 18:24]

maybe collect some more data.

### [18:24 - 18:27]

This is it and it turns out this algorithm is really

### [18:27 - 18:29]

powerful and it can be used to solve several problems.

### [18:31 - 18:34]

There's an interesting semantic question about whether

### [18:34 - 18:35]

this is actually reinforcement learning.

### [18:35 - 18:38]

Am I allowed to call The Work That Had a Reinforcement Learning?

### [18:39 - 18:45]

Often reinforcement learning, people think about reward maximization, but rewards never occur here.

### [18:46 - 18:48]

Our code doesn't use the word reward in it. So I don't know whether to call this reward renewal in one of these cases nor the negativities it has towards that.

### [18:48 - 18:52]

in it. So I don't know whether to call this reward maximization or not, but I know that it works.

### [18:53 - 19:00]

And I want to show you some examples of that. Here's one example done by my student Changyi

### [19:00 - 19:05]

and a collaborator, Homer. What they wanted to do is get this robot to set the table.

### [19:06 - 19:10]

And so they collected a bunch of data. They had a bunch of data of the robot doing other tasks.

### [19:11 - 19:15]

They then took this data, they learned the representations, and then they gave the robot

### [19:15 - 19:21]

a picture where this table had been set how they want the table to be set. And just by giving the

### [19:21 - 19:26]

robot this picture, the robot had to figure out what sequence of actions to take to set the table

### [19:26 - 19:32]

in the desired configuration. From a robotics perspective, this is really appealing because

### [19:32 - 19:37]

it meant that for solving this task, we didn't have to have any humans demonstrate how to solve

### [19:37 - 19:42]

this task. It means that we didn't have to have any remote teleoperation. It means that we never

### [19:42 - 19:45]

had to handcraft reward function or do any complex

### [19:45 - 19:45]

tasks.

### [19:45 - 19:53]

We could do this directly from raw, random data.

### [19:56 - 20:01]

Another fun example of this is for solving the Rubik's cube. We took a bunch of random data from

### [20:01 - 20:06]

the Rubik's cube and learned these representations. And just by acting greedily with respect to these

### [20:06 - 20:11]

representations, you can solve the Rubik's cube. In fact, if you look at the video here, you'll

### [20:11 - 20:15]

see that the strategy that it ends up learning for solving the cube is not too dissimilar to

### [20:15 - 20:22]

the strategy that novice QNQ solvers use for solving the Rubik's cube.

### [20:22 - 20:29]

And one last application that I think is sort of cool, this was done not by me, but by folks down

### [20:29 - 20:37]

the street at a healthcare company, is for figuring out how do you control esophageal ultrasound

### [20:37 - 20:41]

devices. These are devices that you put down someone's throat and you use to take pictures of

### [20:41 - 20:45]

their heart. These devices are really challenging to control, but by using these devices, you can

### [20:45 - 20:51]

use these self-supervised methods that are able to figure out how do you take exactly the right

### [20:51 - 20:58]

images of someone's heart. And so this first half of the talk, we've sort of gone over how we

### [20:58 - 21:03]

automatically find these sorts of temporal patterns. In the second half, I want to talk

### [21:03 - 21:07]

about some properties of these temporal patterns, how learning these representations, these patterns

### [21:07 - 21:12]

can automatically allow us to generalize and solve new tasks more quickly, but also can

### [21:12 - 21:15]

accelerate exploration and solve tasks that we didn't think were possible.

### [21:15 - 21:29]

So I'm going to start with a hypothesis. If our goal is to find these temporal patterns, and in

### [21:29 - 21:35]

particular use deep learning methods to find temporal patterns, then deep learning, the deep

### [21:35 - 21:41]

part, is likely going to be important. And this gives us a testable prediction, namely that deeper

### [21:41 - 21:45]

networks should be better at finding temporal patterns. This sounds pretty obvious, but it's not

### [21:45 - 21:51]

the case. But in fact, it's contrary to be met with a list in the field. I just got back from a

### [21:51 - 21:55]

major machine learning conference a couple weeks ago. And there, most of the papers doing

### [21:55 - 21:58]

reinforcement learning used about two to five layers. We're about two to five layers deep.

### [22:00 - 22:05]

Compared to models in computer vision and NLP, that's tiny. It's really, really small.

### [22:06 - 22:10]

And the reason that people don't try bigger networks is that historically, it just hasn't

### [22:10 - 22:15]

worked. Lost papers have tried getting really big networks to work for reinforcement

### [22:15 - 22:20]

learning, but it hasn't worked. But in recent work, we've found that these self-supervised

### [22:20 - 22:24]

methods, these methods are just one of these representations, they do seem to benefit from

### [22:24 - 22:28]

really deep networks in ways that other reinforcement learning methods don't.

### [22:30 - 22:34]

And so in one experiment, we looked at this humanoid robot that's on the left here.

### [22:34 - 22:39]

This humanoid robot, we wanted to get it to run across the table, so it eventually reached this

### [22:39 - 22:45]

blue sphere. And when we ran this experiment with a small network, it basically failed,

### [22:45 - 22:49]

to solve this task. The amount of time it spent at the goal was then extremely small.

### [22:51 - 22:55]

But when we used bigger networks, networks that were significantly, significantly larger than those

### [22:55 - 22:59]

used in prior work, we found that performance increased significantly.

### [23:04 - 23:08]

Second hypothesis. When we're alerting these representations, we're actually capturing

### [23:08 - 23:14]

some sort of temporal pattern. To give a bit of context for this hypothesis, I want to show the

### [23:14 - 23:15]

representations that we're looking at right now. The first hypothesis is that we're looking at a

### [23:15 - 23:17]

scene, and then we want to tell you about the scene itself, but then we want to tell you about other

### [23:17 - 23:25]

machine learning methods as well. So a standard way of understanding representations is to learn an

### [23:25 - 23:30]

autoencoder, or a variational autoencoder. These are methods that seek an image and try to

### [23:30 - 23:34]

understand what are the parts of that image? What are the objects that are included in that image?

### [23:35 - 23:42]

And these methods, they typically find that the representations capture the contents of a scene.

### [23:42 - 23:45]

But they don't tell you about how you would go about rearranging those objects. They don't tell you about time.

### [23:45 - 23:53]

Now, in contrast with our methods, we find that the representations we learn not only

### [23:53 - 23:58]

tell us about the contents of the scene, but they also tell us something about time.

### [23:58 - 24:01]

They seem to have captured some amount of spatial awareness.

### [24:01 - 24:05]

So if you look at the representations from the left side of the screen to the right side

### [24:05 - 24:11]

of the screen, you see that the objects move, this red object here, it moves closer towards

### [24:11 - 24:15]

the camera, and the robot arm, it goes down, it touches the red object, it touches the

### [24:15 - 24:18]

drawer, and that moves again.

### [24:18 - 24:22]

But the red object, it only moves when the arm is touching it, and the drawer, it only

### [24:22 - 24:25]

moves when the robot arm is touching it.

### [24:25 - 24:29]

And I think this is really powerful, because it means that these representations are really

### [24:29 - 24:38]

telling us something about planning, they're really telling us something about time.

### [24:38 - 24:42]

In fact, you can prove formally that this isn't just a fluke, but it should happen.

### [24:42 - 24:45]

The theoretical reasons why we should expect that.

### [24:45 - 24:50]

When you take the representations we've learned, and just draw a line between the two representations,

### [24:50 - 24:54]

this line should tell you how to solve a problem.

### [24:54 - 24:57]

And for the sake of time, I'll skip over the math, but the math ends up being really beautiful,

### [24:57 - 25:04]

and I can talk about that afterwards if there are questions.

### [25:04 - 25:09]

So these representations, they do seem to capture temporal patterns.

### [25:09 - 25:13]

And it turns out that capturing these temporal patterns allows us to generalize in ways that

### [25:13 - 25:15]

seem really unique to the world.

### [25:15 - 25:19]

They reinforce the learning problem setting, and they also give rise to certain exploration

### [25:19 - 25:20]

properties.

### [25:20 - 25:24]

And I'll start by talking about generalization.

### [25:24 - 25:29]

So very broadly in machine learning, finding patterns, finding learning and variances allows

### [25:29 - 25:32]

us to build models that generalize.

### [25:32 - 25:36]

So to make an analogy to computer vision, let's say that you have a computer vision

### [25:36 - 25:42]

model that treats an image of a cat and a slightly different image of a cat identically.

### [25:42 - 25:45]

Then if you build a model on top of these representations,

### [25:45 - 25:50]

that model will be invariant to these small changes, these small changes in brightness

### [25:50 - 25:54]

and rotation.

### [25:54 - 25:58]

When we learn these representations with time, these temporal representations, what are the

### [25:58 - 26:02]

corresponding generalization properties?

### [26:02 - 26:09]

Well, it turns out that when you learn these temporal representations, the generalization

### [26:09 - 26:12]

properties you get are really powerful.

### [26:12 - 26:14]

And I can explain this as follows.

### [26:15 - 26:19]

When, let's say that you're this rabbit here, and you want to figure out how do you get

### [26:19 - 26:22]

to this purple star here.

### [26:22 - 26:27]

Maybe the first action you take is to move down to this state here.

### [26:27 - 26:31]

And maybe tomorrow, this rabbit has to solve a different navigation problem, going from

### [26:31 - 26:35]

this state here to this brown star here.

### [26:35 - 26:37]

And the first action it takes is to go down.

### [26:37 - 26:45]

Well, the, for both these tasks, the purple star task and the brown star task, the first

### [26:45 - 26:47]

action was the same.

### [26:47 - 26:50]

In both cases, the action was the same.

### [26:50 - 26:56]

And so we might say that this policy should be invariant to plan.

### [26:56 - 27:00]

It should produce the same action for getting to the purple star as it should for getting

### [27:00 - 27:06]

to a waypoint on the route to the purple star.

### [27:06 - 27:10]

I can visualize that as follows.

### [27:10 - 27:14]

Now what this means is that if you can build policies that have this invariance process,

### [27:14 - 27:19]

then you can train them on short horizon tasks, like getting to the idea of a small

### [27:19 - 27:21]

circle here.

### [27:21 - 27:26]

And without any more training, they'll generalize to reach more distant goals, like this outer

### [27:26 - 27:28]

circle shown here.

### [27:28 - 27:36]

So in summary, with takes of generalization, they really seem unique to decision-making

### [27:36 - 27:37]

problems.

### [27:37 - 27:42]

Very, very broadly, I think today, a lot of people, when they talk about agents and AI,

### [27:42 - 27:44]

they talk about building generalist agents.

### [27:44 - 27:52]

But the next time you hear that term, I want you to ask, what specific notion of generalization

### [27:52 - 27:54]

are you talking about?

### [27:54 - 27:57]

Generalization is about training at one task and doing well in other tasks.

### [27:57 - 28:01]

And there's some notions of generalization that are studied by computer vision models

### [28:01 - 28:03]

and language models.

### [28:03 - 28:07]

But there are other notions of generalization that seem unique in making problems.

### [28:07 - 28:13]

So the last few minutes of the talk, I want to talk a little bit about exploration.

### [28:13 - 28:14]

I want to talk a little bit about generalization.

### [28:14 - 28:14]

I want to talk a little bit about generalization.

### [28:14 - 28:19]

And the problem setting here is one that's almost diabolically difficult.

### [28:19 - 28:29]

It's one where we want to learn a policy for navigating from one state to some other very

### [28:29 - 28:32]

far away state.

### [28:32 - 28:33]

And so you could think about solving a Rubik's cube.

### [28:33 - 28:36]

If I give you a Rubik's cube, you want to figure out, how do you get from the current

### [28:36 - 28:42]

Rubik's cube configuration to the state where the Rubik's cube is solved?

### [28:42 - 28:43]

And here's how you might go about solving that problem.

### [28:43 - 28:44]

And here's how you might go about solving that problem.

### [28:44 - 28:49]

You take a random policy, because policies can be garbage to start.

### [28:49 - 28:51]

And then you say, policy, try to get to this goal.

### [28:51 - 28:54]

And you collect some data.

### [28:54 - 28:57]

And then you use these data to learn some representations.

### [28:57 - 28:59]

You learn a policy.

### [28:59 - 29:01]

And then you go back and you collect some more data.

### [29:01 - 29:06]

And you try to get to this one very difficult goal.

### [29:06 - 29:09]

Now, intuitively, it seems like this shouldn't work.

### [29:09 - 29:14]

It seems like if I tell you, try to navigate from one state to some very far away state,

### [29:14 - 29:18]

this should just be impossible.

### [29:18 - 29:22]

It seems like you should need to, I don't know, put down some brain crumbs to tell you

### [29:22 - 29:24]

how to get to that goal.

### [29:24 - 29:28]

But in recent work, we found that this really simple approach, this approach that seems

### [29:28 - 29:30]

like it shouldn't work.

### [29:30 - 29:31]

In fact, it does work.

### [29:31 - 29:39]

It does work if you learn a policy using the representations I showed before.

### [29:39 - 29:42]

And I want to show you a video of what this exploration method looks like.

### [29:42 - 29:43]

We've told the robot.

### [29:43 - 29:47]

I want you to figure out how to pick up the green block and put it in the blue bin.

### [29:47 - 29:49]

And I'm just showing you the robot train right now.

### [29:49 - 29:54]

It's exploring the environment by itself, trying out different positions, exploring

### [29:54 - 29:57]

the space, tries touching different objects.

### [29:57 - 29:59]

And we haven't programmed any of this.

### [29:59 - 30:02]

We haven't told the robot to try touching objects.

### [30:02 - 30:07]

It's just learned on its own that touching objects is an interesting thing to do.

### [30:07 - 30:11]

And at this point, it's learned on its own that picking up objects is an interesting

### [30:11 - 30:12]

thing to do.

### [30:12 - 30:17]

It's all emerged from scratch.

### [30:17 - 30:20]

At some point, at about this point in training, it's learned that it actually can pick up

### [30:20 - 30:23]

the object.

### [30:23 - 30:29]

And then it learns how to do this more and more quickly.

### [30:29 - 30:33]

One reason why I really like this video is it helps highlight the capability of these

### [30:33 - 30:37]

methods that I think is really lacking in other areas of reinforcement learning and

### [30:37 - 30:42]

lacking especially in areas of computer graphics and language modeling.

### [30:42 - 30:45]

Which is the capacity to discover something new.

### [30:45 - 30:50]

The capacity to find solutions to a problem that haven't been written about on the internet

### [30:50 - 30:53]

that haven't been shown to you in any videos that you've seen before.

### [30:53 - 30:55]

It's really about generating knowledge.

### [30:55 - 30:59]

I think the power of reinforcement learning and these self-supervised methods is that

### [30:59 - 31:02]

they can generate their own knowledge.

### [31:02 - 31:05]

Here we're seeing that play out in a rather simple block stacking environment.

### [31:05 - 31:08]

But we could look at other much more complex tasks as well.

### [31:12 - 31:22]

Here is one example of this demonstrated in a multi-agent setting.

### [31:22 - 31:24]

So here we have teams of agents.

### [31:24 - 31:28]

And the teams of agents have to automatically learn how to cooperate to reach some goal.

### [31:28 - 31:32]

And the goal here is to make all of the opponents be dead.

### [31:32 - 31:37]

One of the really cool things about this work is that we find that throughout the course

### [31:37 - 31:42]

of learning, before the agents have ever succeeded at the task, they automatically learn to try

### [31:42 - 31:49]

out different exploration strategies, different teamwork strategies.

### [31:49 - 31:53]

And so finding these temporal patterns, they unlock certain forms of generalization.

### [31:53 - 31:57]

And they unlock new forms of exploration.

### [31:57 - 32:00]

I started this talk by talking about finding patterns in space.

### [32:00 - 32:07]

How deep learning methods for computer vision automatically find these rich spatial patterns.

### [32:07 - 32:12]

And I think my hope is to convey how finding patterns in time may unlock capabilities for

### [32:12 - 32:14]

decision-making and reinforcement learning.

### [32:14 - 32:17]

For decision-making agents.

### [32:17 - 32:23]

And in the last couple of minutes, I'm going to chart a path for what the future might look like.

### [32:23 - 32:26]

Today, we have robots that can stack some blocks.

### [32:26 - 32:30]

In a couple months, we probably could have robots that can build a Jenga tower.

### [32:30 - 32:36]

But how long until we have robots that can build a tower like the one shown on the right?

### [32:36 - 32:40]

The tower shown on the right has 1,500 blocks.

### [32:40 - 32:42]

All stacked on top of a single block.

### [32:42 - 32:49]

If I show you this image, do you think it's a real image?

### [32:49 - 32:52]

Or was this just a generative AI image?

### [32:52 - 32:54]

How do you figure it out?

### [32:54 - 32:59]

How do you guess whether this was a real image or a generative AI image?

### [32:59 - 33:03]

If you're like me, you'd go get a bunch of blocks and try building it.

### [33:03 - 33:09]

How do we make AI agents that do something similar, that automatically try little experiments

### [33:09 - 33:12]

to see whether it would be possible to build a tower like this?

### [33:12 - 33:15]

I don't know.

### [33:15 - 33:18]

We recently put out a benchmark so that you can try it.

### [33:18 - 33:23]

You can figure out how to design AI agents that can automatically become mini-scientists.

### [33:23 - 33:29]

Learn how to perform these controlled experiments to really learn about the world and generate knowledge.

### [33:29 - 33:39]

I want to note a couple other code repositories and papers for folks that want to get involved in the research.

### [33:39 - 33:41]

For folks that really want to study AI.

### [33:41 - 33:44]

For folks that really want to study scaling laws for reinforcement learning.

### [33:44 - 33:49]

I'd recommend checking out the paper and codebase from here.

### [33:49 - 33:56]

We've also spent a lot of time thinking about how do you build reinforcement learning experimental frameworks that are really, really fast.

### [33:56 - 34:00]

We know that fast training is important for unlocking certain capabilities.

### [34:00 - 34:08]

And this codebase here allows us to train in about a million frames in one minute.

### [34:08 - 34:11]

There's also this important problem setting of learning from offline data.

### [34:11 - 34:14]

We've built a new benchmark for studying this problem setting as well.

### [34:20 - 34:25]

I should thank my amazing group of students and collaborators who have referred to most of the research I've talked about today.

### [34:25 - 34:27]

And I'm happy to take any questions.

### [34:27 - 34:29]

Thanks.
