# Deep Learning Bootcamp: Kaiming He

- URL: https://www.youtube.com/watch?v=D_jt-xO_RmI
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-09T13:26:42`

## Transcript

### [00:00 - 00:20]

Good. Shall we get started? Okay, cool. So, my name is Kai Ming, and I will be joining this random university next month, actually. So, today I'm doing an unpaid job, and now let's see what's the title of my unpaid job.

### [00:21 - 00:29]

Well, it's learning deep representations, and I will talk about it in the context of image recognition, and perhaps in some other scenarios.

### [00:30 - 00:37]

And here is an overview of this tutorial. First I will talk about what is representation learning?

### [00:37 - 00:40]

And why representation learning is an important problem?

### [00:41 - 00:45]

And then, I will talk about how can we build and train very deep neural networks?

### [00:45 - 00:50]

And I will talk about a few milestones and influential neural network architectures.

### [00:50 - 00:55]

Then I will also cover some important components and elements for us to train very diminutive architecture,

### [00:55 - 01:00]

including some initiation methods, normalization methods,

### [01:00 - 01:00]

and next slide.

### [01:00 - 01:04]

introduction of residual connections. And then I will also cover the applications

### [01:04 - 01:11]

for image recognition and some sequence processing problems. So first of all, why

### [01:11 - 01:17]

deep learning? Why about ten years ago suddenly people started to talk about

### [01:17 - 01:23]

deep learning almost everywhere? So in a nutshell, deep learning is

### [01:23 - 01:28]

representation learning. And actually, interestingly, more than ten years ago,

### [01:28 - 01:34]

deep learning was not popular and was not favored by the mainstream conference

### [01:34 - 01:39]

in computer vision or in machine learning. And at that time, some of the

### [01:39 - 01:43]

pioneers in deep learning and neural network architectures, such as Yann LeCun

### [01:43 - 01:47]

and Yoshua Bengio, decided to start another conference that is more friendly

### [01:47 - 01:53]

and more open-minded to deep learning research. And interestingly, these

### [01:53 - 01:57]

pioneers in deep learning decided to name their new conference as the

### [01:57 - 01:58]

international

### [01:58 - 02:04]

conference on learning representations. And this reflects how closely related it

### [02:04 - 02:08]

is between deep learning and representation learning. Then, why

### [02:08 - 02:13]

representation learning is important? Representation learning is a common

### [02:13 - 02:19]

problem that can be shared across many applications in many areas. A common goal

### [02:19 - 02:25]

of representation learning is to transform the raw data into some high

### [02:25 - 02:27]

level representation space. And we will have the opportunity to share this

### [02:27 - 02:31]

holiday territory, for example, by presenting a video on artificial intelligence.

### [02:31 - 02:33]

In order to do that, we need to have many different types of discussion.

### [02:33 - 02:34]

We can use the artificial intelligence for example, to provide some

### [02:34 - 02:37]

very simple, simple examples of how to represent a given topic.

### [02:37 - 02:39]

For example, we can use them for operations to try and translate this

### [02:39 - 02:41]

topic into a shared discussion with an audience. And in this case, the

### [02:41 - 02:44]

real world field of view is the Neuron context. And we will have better

### [02:44 - 02:47]

compression or abstraction, or conceptualization in the

### [02:47 - 02:51]

representation space. And when the computer algorithms are operated on that

### [02:51 - 02:53]

representation space, they can solve very complex problems way more easily. And,

### [02:53 - 02:55]

depending on the scenarios, the raw data can be in many different forms in practice.

### [02:55 - 03:02]

or worse. In some other scenarios, such as speech recognition or audio recognition, the raw data can

### [03:02 - 03:08]

be audio waves or spectrograms. And in the case of game playing, the raw data can be the states of

### [03:08 - 03:14]

the game board. And in some scientific problems, the raw data can be the molecule sequences, DNA

### [03:14 - 03:21]

sequences, or some other structures. A common problem in many of these applications is on how

### [03:21 - 03:28]

can we represent the data in some high-level abstraction space such that the computer

### [03:28 - 03:36]

algorithms can solve the problem way more easily. Now let's take the game of Go as an example.

### [03:37 - 03:43]

Using computers to solve the game of Go has been believed as a very challenging or maybe even

### [03:43 - 03:49]

infeasible problem over the last several decades. So part of the reason is that there is an

### [03:49 - 03:51]

exponentially large number of different systems that can be used to solve the problem.

### [03:51 - 03:59]

For example, the board has 19 columns and 19 rows. And if we put everything together,

### [03:59 - 04:06]

then there would be 361 positions. And every single position may have three choices, black,

### [04:06 - 04:13]

white, and blank. Then this will give us three to the power of 361 different states. And this is a

### [04:13 - 04:20]

huge number. And if the computer algorithm is going to do analysis or maybe even enumeration

### [04:20 - 04:21]

or memorization of the data, then it's going to have to do a lot of work. And if the computer

### [04:21 - 04:21]

algorithm is going to do analysis or maybe even enumeration of the data, then it's going to have to

### [04:21 - 04:21]

do a lot of work. And if the computer algorithm is going to do analysis or maybe even enumeration

### [04:21 - 04:28]

in this space, then it would just be infeasible for today's computer to address this problem

### [04:28 - 04:36]

using this representation. However, if that is the case, then perhaps we will never solve

### [04:36 - 04:42]

computer vision or image recognition problems. Now let's think of a very simple case in computer

### [04:42 - 04:48]

vision. Let's say we will have a very small image, let's say 500 pixels by 500 pixels. And

### [04:48 - 04:51]

every single pixel may have three color channels, red, green, and blue. And if we have a very small

### [04:51 - 04:53]

image, let's say 500 pixels by 500 pixels. And every single pixel may have three color

### [04:53 - 04:55]

channels, red, green, and blue. And every single color channel may have 256 different

### [04:55 - 05:01]

values. And if we put everything together, then we will have 256 to the power of three

### [05:01 - 05:08]

by 500 by 500 different states, just for a very small image. And if our computer vision

### [05:08 - 05:14]

algorithm is directly operated on this raw pixel space, and if the algorithm is going

### [05:14 - 05:21]

to either enumerate or memorize this state space, then we will never solve the computer

### [05:21 - 05:25]

vision algorithm, because this problem is even more intractable than the problem of

### [05:25 - 05:32]

goal playing. However, this is not how computer vision algorithms address the image recognition

### [05:32 - 05:39]

problem. Instead of directly working on the raw pixel space, we will use a model to transform

### [05:39 - 05:45]

the raw pixels into some representations. And today, usually the most successful model

### [05:45 - 05:51]

for us to do this is to use a deep neural network, such as a convolutional neural network.

### [05:51 - 05:57]

And then, these representations will give us some very good compressions, abstractions,

### [05:57 - 06:01]

or conceptualizations. And when using these representations, the computer algorithms

### [06:01 - 06:06]

can solve many different problems, such as image classification, object detection, or

### [06:06 - 06:13]

image segmentation. Then, analogously, going back to the problem of goal playing, we can

### [06:13 - 06:20]

just think of the board in the goal playing as a very small image. And this image just

### [06:20 - 06:21]

has

### [06:21 - 06:26]

19 by 19 pixels and every single pixel has only three possible colors black

### [06:26 - 06:32]

white and blank and then we can use the same idea for example we can use a

### [06:32 - 06:38]

convolutional neural network to process the states of the game and obtain some

### [06:38 - 06:43]

high-level abstractions and the computer algorithm can directly work on this

### [06:43 - 06:49]

high-level abstraction space to do some analysis or do some search and this will

### [06:49 - 06:54]

make the problem of goal-playing way more easily to be solved. And this is

### [06:54 - 06:59]

actually one of the many fundamental ideas behind the famous alpha-goal

### [06:59 - 07:06]

algorithm. This figure is from the alpha-goal 0 paper and in this figure the

### [07:06 - 07:11]

authors compared four different versions of the alpha goal player and these

### [07:11 - 07:15]

versions are compared in terms of the ELO rating and usually a higher rating

### [07:15 - 07:19]

means a better goal-playing performance and this figure simply

### [07:19 - 07:19]

shows that alpha-goal is not a problem. It's more likely to be solved if you

### [07:19 - 07:22]

shows that by increasing the depths from, for example,

### [07:22 - 07:25]

12 layers to 40 layers, we can easily

### [07:25 - 07:29]

enjoy a huge boost in terms of the goal playing performance.

### [07:29 - 07:31]

And actually, if we keep increasing

### [07:31 - 07:33]

the depths of the neural networks,

### [07:33 - 07:34]

for example, to 80 layers, we are

### [07:34 - 07:37]

going to see another huge boost in terms

### [07:37 - 07:41]

of the goal playing performance.

### [07:41 - 07:45]

It is interesting to note that this performance is

### [07:45 - 07:48]

way better than even the best human players in the world.

### [07:48 - 07:51]

And AlphaGo algorithm can achieve this performance

### [07:51 - 07:54]

without using any human knowledge.

### [07:54 - 07:57]

And it is also worth noticing that for the four or five

### [07:57 - 08:01]

different players compared here, many of the other components

### [08:01 - 08:03]

are exactly the same.

### [08:03 - 08:06]

So for example, the usage of the reinforcement learning

### [08:06 - 08:09]

algorithm and the Monte Carlo tree search algorithms

### [08:09 - 08:10]

are exactly the same.

### [08:10 - 08:13]

It is only the neural network architectures

### [08:13 - 08:16]

that are used to learn the representations for goal

### [08:16 - 08:18]

playing are different.

### [08:18 - 08:21]

And for example, if you look at this image here,

### [08:21 - 08:23]

you can see that there are five different versions

### [08:23 - 08:25]

that are used to learn the representations for goal

### [08:25 - 08:28]

playing across these five different versions.

### [08:28 - 08:30]

So I hope this will give you some sense

### [08:30 - 08:34]

about how important representation learning is

### [08:34 - 08:36]

for us to address very challenging problems.

### [08:38 - 08:41]

Now, let's go back to the problem of computer vision.

### [08:41 - 08:42]

And next, I'm going to talk about how

### [08:42 - 08:46]

can we represent an image in computer vision

### [08:46 - 08:48]

before deep learning got popular.

### [08:48 - 08:51]

So let's start with the problem of computer vision.

### [08:51 - 08:53]

So in computer vision, we can represent a very small number

### [08:53 - 08:55]

of pixels into a classifier.

### [08:55 - 08:57]

The classifier can be an SVM classifier,

### [08:57 - 09:00]

Support Vector Machine, or it can be a decision tree,

### [09:00 - 09:02]

or it can be a random forest.

### [09:02 - 09:04]

Usually, this is not a good solution

### [09:04 - 09:06]

because even a small change in the object

### [09:06 - 09:10]

will lead to a larger change in the raw pixel representation

### [09:10 - 09:11]

space.

### [09:11 - 09:17]

Then in order to have a better question,

### [09:18 - 09:23]

how they thought about the game and how they represented it

### [09:23 - 09:25]

to get one thing, I suspect.

### [09:25 - 09:30]

And if we looked at the so-called representation

### [09:30 - 09:33]

that they know, system learning, would they

### [09:33 - 09:35]

look anything like one another?

### [09:35 - 09:39]

Has anybody done that experiment?

### [09:39 - 09:39]

Yeah.

### [09:39 - 09:41]

That's a very good question.

### [09:41 - 09:44]

So I'm not a good goal player, but I

### [09:44 - 09:48]

got to know that there are very fancy terminology about goal

### [09:48 - 09:48]

playing.

### [09:48 - 09:53]

It's the terminology about the expert player's sensation

### [09:53 - 09:56]

about how the current state is.

### [09:56 - 09:59]

So the goal player has their own internal representations

### [09:59 - 10:01]

for goal playing.

### [10:01 - 10:02]

And those internal representations

### [10:02 - 10:05]

may not be well aligned with what the representations can

### [10:05 - 10:08]

be learned by computer algorithms.

### [10:08 - 10:13]

And actually, after the AlphaGo was developed,

### [10:13 - 10:15]

I believe many of the expert players

### [10:15 - 10:18]

used the .

### [10:18 - 10:20]

I used the AI to help them to improve

### [10:20 - 10:25]

their own internal representation of human beings.

### [10:25 - 10:27]

OK, good.

### [10:27 - 10:29]

OK, let's go back to our story.

### [10:29 - 10:31]

So in order to have a slightly better representation,

### [10:31 - 10:34]

we may want to compute the edges on top of the pixels

### [10:34 - 10:39]

because this will give us some more robust representations

### [10:39 - 10:42]

in case the illumination or the colors of the input space

### [10:42 - 10:44]

may change.

### [10:44 - 10:47]

Then again, in order to have yet another better presentation,

### [10:47 - 10:50]

we may want to compute the orientations of the edges

### [10:50 - 10:53]

or the histograms of the orientations,

### [10:53 - 10:55]

or we may run some clustering algorithms

### [10:55 - 10:57]

on top of the histograms.

### [10:57 - 11:01]

So actually, this pipeline works pretty well

### [11:01 - 11:04]

if the problem is simple enough.

### [11:04 - 11:08]

However, in this pipeline, it require human beings

### [11:08 - 11:11]

or it require computer vision experts

### [11:11 - 11:13]

to define what are good representations

### [11:13 - 11:14]

or what are good features for some

### [11:14 - 11:17]

to solve the problems on hand.

### [11:17 - 11:19]

So while the feature designing problem

### [11:19 - 11:23]

is relatively doable for some low-level representations,

### [11:23 - 11:28]

such as the definition of edges or textures or colors,

### [11:28 - 11:31]

this problem would be extremely difficult

### [11:31 - 11:34]

if we want to define some high-level representations.

### [11:34 - 11:36]

For example, it turns out to be extremely difficult for us

### [11:36 - 11:40]

to define, for example, what is a fish, what is a cat,

### [11:40 - 11:43]

or on the other hand, what is a tree or what is a human.

### [11:43 - 11:47]

And actually, in computer vision, over the last several

### [11:47 - 11:51]

decades, defining high-level abstractions

### [11:51 - 11:54]

and representations has been a major bottleneck

### [11:54 - 11:56]

in the computer vision community.

### [11:58 - 12:00]

Deep learning provides another methodology

### [12:00 - 12:04]

for us to address the computer vision, image recognition,

### [12:04 - 12:07]

and many other complex problems.

### [12:07 - 12:10]

A key idea of deep learning is to compose

### [12:10 - 12:15]

a simple set of general modules into highly complex functions

### [12:15 - 12:16]

for us to solve highly complex problems.

### [12:17 - 12:21]

So if there is only one message that you can take away

### [12:21 - 12:24]

from my talk today, then this is the message.

### [12:24 - 12:27]

I'm going to repeat it many times

### [12:27 - 12:29]

in the following part of this talk.

### [12:29 - 12:33]

So with the help of a general set of modules,

### [12:33 - 12:37]

it is easy for us to build multiple levels of abstractions

### [12:37 - 12:41]

and to learn multiple levels of representations.

### [12:41 - 12:44]

And the concrete instantiations of these modules,

### [12:44 - 12:46]

such as the parameters or the weight

### [12:46 - 12:50]

of these modules, can be learned by backpropagation.

### [12:50 - 12:54]

So the reliance on human knowledge is largely reduced.

### [12:54 - 12:57]

And again, the learning is done on some larger-scale data.

### [12:57 - 12:59]

So the requirement of human knowledge

### [12:59 - 13:05]

has been transferred or shifted from engineering the features

### [13:05 - 13:08]

to another problem of collecting the data that

### [13:08 - 13:10]

is related to the problem.

### [13:10 - 13:15]

And overall, all of these key ideas or key concepts

### [13:15 - 13:16]

of deep learning can help us to solve

### [13:16 - 13:17]

the problem on hand.

### [13:17 - 13:19]

And again, the learning is done on some larger-scale data.

### [13:19 - 13:21]

And again, the learning is done on some larger-scale data.

### [13:21 - 13:25]

So these are many reasons why deep learning

### [13:25 - 13:28]

can be a general toolbox for us to solve

### [13:28 - 13:30]

many problems in many areas.

### [13:30 - 13:34]

can be a general toolbox for us to solve many problems in many areas.

### [13:34 - 13:36]

And next, I'm going to talk about how

### [13:36 - 13:39]

can we learn the deep representations for image

### [13:39 - 13:40]

recognition.

### [13:40 - 13:42]

And I'm going to go through a few milestone

### [13:42 - 13:46]

and influential steps in the history of computer

### [13:46 - 13:51]

learning and convolutional neural network development.

### [13:51 - 13:53]

I will start with the learning architecture that

### [13:53 - 13:56]

was developed about 30 years ago.

### [13:56 - 14:00]

The learning architecture is one of the successful instantiation

### [14:00 - 14:03]

of convolutional neural networks, or in short,

### [14:03 - 14:06]

a confnet or CNN.

### [14:06 - 14:09]

Simply speaking, a convolutional neural network

### [14:09 - 14:12]

is the translation invariant architecture.

### [14:12 - 14:15]

So by translation invariance, we usually mean,

### [14:15 - 14:16]

if we have some convolutional neural network, we can use it

### [14:16 - 14:19]

some operations inside a sliding window.

### [14:19 - 14:22]

And when the window is translated by a few pixels,

### [14:22 - 14:25]

we will still have more or less the same operations.

### [14:25 - 14:27]

And translation invariance can also

### [14:27 - 14:31]

mean, if we translate the entire input image by a few pixels,

### [14:31 - 14:35]

we can still have the same output class label

### [14:35 - 14:39]

if we are doing the classification problem.

### [14:39 - 14:40]

Then, the learning architecture has

### [14:40 - 14:44]

introduced several foundational elements

### [14:44 - 14:45]

for convolutional neural networks.

### [14:45 - 14:46]

These elements.

### [14:46 - 14:49]

include the usage of convolutional layers,

### [14:49 - 14:53]

pooling layers, fully connected layers, and more importantly,

### [14:53 - 14:57]

the idea of training the entire architecture end-to-end

### [14:57 - 14:59]

by backpropagation.

### [14:59 - 15:02]

And again, a convolutional neural network

### [15:02 - 15:06]

is just one instantiation of the deep learning methodology,

### [15:06 - 15:10]

which is to compose simple modules

### [15:10 - 15:12]

into highly complex functions.

### [15:12 - 15:15]

And next, I'm going to introduce two of these simple modules that

### [15:15 - 15:17]

are foundational.

### [15:17 - 15:21]

The first module is the convolutional layer.

### [15:21 - 15:24]

Simply speaking, a convolutional layer

### [15:24 - 15:29]

is just local connection plus spatial weight sharing.

### [15:29 - 15:32]

In contrast to a convolutional layer,

### [15:32 - 15:34]

one of the most popular layer type

### [15:34 - 15:36]

is the fully connected layer.

### [15:36 - 15:39]

In that case, every single output neuron

### [15:39 - 15:43]

is connected to every single input neuron in that layer.

### [15:43 - 15:45]

And here, every connection represents a weight.

### [15:45 - 15:47]

Or a parameter that can be trained.

### [15:47 - 15:49]

That is to say, if we have many input neurons,

### [15:49 - 15:51]

if we also have many output neurons,

### [15:51 - 15:55]

then we will have a great number of trainable parameters.

### [15:55 - 15:57]

And that is not ideal.

### [15:57 - 16:00]

And in order to partially address this problem,

### [16:00 - 16:03]

people have developed another layer type,

### [16:03 - 16:06]

which is called a locally connected layer.

### [16:06 - 16:08]

In that case, every single output neuron

### [16:08 - 16:12]

is connected to just a small subset of the input neurons.

### [16:12 - 16:14]

And usually, in practice, these small subsets

### [16:14 - 16:18]

will just be in a sliding window or a local neighborhood

### [16:18 - 16:21]

around the output neuron.

### [16:21 - 16:23]

And the introduction of a locally connected layer

### [16:23 - 16:27]

can greatly reduce the numbers of trainable parameters.

### [16:27 - 16:30]

And a convolutional layer is just one step ahead.

### [16:30 - 16:32]

That is to say, when we slide a window

### [16:32 - 16:36]

in different positions of the input image space,

### [16:36 - 16:42]

we can share the weight across different spatial positions.

### [16:42 - 16:44]

So let's zoom out a little bit.

### [16:44 - 16:46]

And again, the convolutional layer

### [16:46 - 16:49]

is local connections plus weight sharing.

### [16:49 - 16:52]

And we are going to see that these two concepts,

### [16:52 - 16:54]

local connection and weight sharing,

### [16:54 - 17:01]

are everywhere in neural network design.

### [17:01 - 17:04]

Another important component,

### [17:04 - 17:07]

another important module in convolutional neural network

### [17:07 - 17:08]

is a pooling layer.

### [17:08 - 17:10]

The role of a pooling layer is to reduce

### [17:10 - 17:12]

the size of the feature map

### [17:12 - 17:13]

so it can greatly reduce

### [17:13 - 17:15]

the computation required

### [17:15 - 17:17]

if the input image is big.

### [17:17 - 17:19]

On the other hand, a pooling layer

### [17:19 - 17:21]

can also help to achieve local invariance.

### [17:21 - 17:24]

That is to say, if our input contents undergo

### [17:24 - 17:26]

some local jittering inside a small window,

### [17:26 - 17:28]

we will still able to obtain more or less

### [17:28 - 17:30]

the same representations in that window.

### [17:30 - 17:32]

And this can help us to get

### [17:32 - 17:34]

more abstraction representations

### [17:34 - 17:36]

and this is a desired property

### [17:36 - 17:41]

for us to do classification problems.

### [17:41 - 17:43]

Then given these simple sets

### [17:43 - 17:46]

of general modules,

### [17:46 - 17:48]

next I'm going to walk through

### [17:48 - 17:50]

the learning architecture step by step.

### [17:50 - 17:51]

Even though this architecture

### [17:51 - 17:54]

has been proposed by more than 30 years,

### [17:54 - 17:57]

it is always enjoyable and inspiring

### [17:57 - 17:58]

for us to walk through

### [17:58 - 18:00]

this classical architecture.

### [18:00 - 18:03]

In this case, the input to the neural network

### [18:03 - 18:05]

has only one color channel

### [18:05 - 18:07]

because it is grayscale.

### [18:07 - 18:08]

And in this example,

### [18:08 - 18:11]

the spatial size would be 32 by 32.

### [18:11 - 18:13]

Then it will perform the first

### [18:13 - 18:15]

set of convolutional kernels,

### [18:15 - 18:18]

which has a spatial size of five by five.

### [18:18 - 18:19]

And in this case,

### [18:19 - 18:21]

it has six different output channels.

### [18:21 - 18:23]

And this will give us the first set

### [18:23 - 18:25]

of output feature map.

### [18:25 - 18:26]

And in this case,

### [18:26 - 18:28]

the spatial size is 28 by 28.

### [18:28 - 18:30]

And because our convolutional layer

### [18:30 - 18:31]

has six output channels,

### [18:31 - 18:33]

then this set of feature maps

### [18:33 - 18:35]

will also have six output channels.

### [18:35 - 18:39]

Then we can apply the first pooling operation

### [18:39 - 18:41]

to reduce the spatial size

### [18:41 - 18:42]

by a factor of two

### [18:42 - 18:44]

across each dimension.

### [18:44 - 18:46]

Then we will arrive at the next set

### [18:46 - 18:48]

of spatial feature map,

### [18:48 - 18:51]

which has a spatial size of 14 by 14.

### [18:51 - 18:53]

Then we are ready to apply the next set

### [18:53 - 18:55]

of convolutional layers,

### [18:55 - 18:58]

again, which has a kernel size of five by five.

### [18:58 - 18:59]

And at this time,

### [18:59 - 19:02]

it has 16 different output channels.

### [19:02 - 19:04]

Then we will arrive at the next set

### [19:04 - 19:05]

of feature map,

### [19:05 - 19:08]

which has a spatial size of 10 by 10 here.

### [19:08 - 19:09]

And again,

### [19:09 - 19:10]

the next pooling layer

### [19:10 - 19:12]

to reduce the spatial size.

### [19:12 - 19:14]

Then we will arrive at the next,

### [19:14 - 19:16]

at the final set of spatial feature map,

### [19:16 - 19:19]

which has a spatial size of five by five.

### [19:19 - 19:20]

And after that,

### [19:20 - 19:22]

we can just flatten this feature map,

### [19:22 - 19:24]

and we will process it

### [19:24 - 19:26]

with the first set of fully connected layers

### [19:26 - 19:27]

and the second set

### [19:27 - 19:29]

and the output fully connected layer,

### [19:29 - 19:32]

which has 10 channels in this case

### [19:32 - 19:35]

for 10 class classification problem.

### [19:35 - 19:36]

And at the high level,

### [19:36 - 19:38]

the entire architecture is very simple.

### [19:38 - 19:40]

It is just a composition

### [19:40 - 19:42]

of several basic modules

### [19:42 - 19:44]

which is just convolutional layers,

### [19:44 - 19:45]

pooling layers,

### [19:45 - 19:49]

and fully connected layer in this case.

### [19:49 - 19:52]

The learning architecture actually works extremely well

### [19:52 - 19:55]

if we have the data to train it.

### [19:55 - 19:56]

Unfortunately,

### [19:56 - 19:58]

this architecture has been ignored

### [19:58 - 19:59]

for more than 20 years

### [19:59 - 20:01]

after it was proposed.

### [20:01 - 20:02]

Part of the reason is that

### [20:02 - 20:03]

we don't have the compute

### [20:03 - 20:05]

or we don't have the data

### [20:05 - 20:06]

to fully demonstrate

### [20:06 - 20:08]

the power of this architecture.

### [20:08 - 20:09]

At that time,

### [20:09 - 20:10]

the largest data set,

### [20:10 - 20:11]

surprisingly,

### [20:11 - 20:13]

it was the largest data set at that time,

### [20:13 - 20:15]

was the MNIST data set,

### [20:15 - 20:18]

which has 50,000 images in 10 classes.

### [20:18 - 20:20]

This data set is good enough

### [20:20 - 20:22]

to train a very small model,

### [20:22 - 20:23]

but it's not enough

### [20:23 - 20:24]

to fully convince

### [20:24 - 20:26]

the computer vision community

### [20:26 - 20:28]

to adopt convolutional neural networks

### [20:28 - 20:32]

in their problems.

### [20:32 - 20:34]

Then the real revolution of deep learning

### [20:34 - 20:36]

happened in 2012,

### [20:36 - 20:37]

and it was introduced

### [20:37 - 20:40]

by this AlexNet paper.

### [20:40 - 20:41]

In my understanding,

### [20:41 - 20:43]

there is only one thesis

### [20:43 - 20:45]

in this AlexNet paper,

### [20:45 - 20:47]

which is to scale up

### [20:47 - 20:49]

convolutional neural networks.

### [20:49 - 20:52]

And the scaling up involves

### [20:52 - 20:54]

actually several aspects.

### [20:54 - 20:57]

The first aspect is about the data.

### [20:57 - 20:59]

The AlexNet was trained

### [20:59 - 21:00]

on the ImageNet data set,

### [21:00 - 21:02]

which has one million images

### [21:02 - 21:04]

and 1,000 classes.

### [21:04 - 21:06]

And actually at that time,

### [21:06 - 21:07]

it is way more bigger

### [21:07 - 21:09]

than many of the other data sets

### [21:09 - 21:11]

that people have been studying.

### [21:11 - 21:13]

And actually at that time,

### [21:13 - 21:15]

it's far beyond people's imagination

### [21:15 - 21:17]

that we can train

### [21:17 - 21:19]

a neural network architecture end-to-end

### [21:19 - 21:21]

on raw pixels

### [21:21 - 21:24]

in such a large-scale data set.

### [21:24 - 21:25]

On the other hand,

### [21:25 - 21:27]

the AlexNet architecture

### [21:27 - 21:28]

is actually big.

### [21:28 - 21:31]

And in the abstract of that paper,

### [21:31 - 21:33]

the authors specifically said

### [21:33 - 21:35]

this is a huge architecture,

### [21:35 - 21:36]

and this architecture

### [21:36 - 21:38]

has more than 60 million parameters

### [21:38 - 21:43]

and over 600,000 neurons.

### [21:43 - 21:44]

This model size

### [21:44 - 21:46]

is actually also way more bigger

### [21:46 - 21:47]

than many of the other models

### [21:47 - 21:49]

on those days.

### [21:49 - 21:50]

Then in order to train

### [21:50 - 21:52]

such a large model,

### [21:52 - 21:53]

even with the help

### [21:53 - 21:55]

of a larger-scale data,

### [21:55 - 21:56]

people need to introduce

### [21:56 - 21:57]

effective techniques

### [21:57 - 21:59]

to reduce overfitting.

### [21:59 - 22:01]

And the AlexNet paper

### [22:01 - 22:03]

explored two very effective techniques

### [22:03 - 22:05]

in this regard.

### [22:05 - 22:06]

One is data augmentation,

### [22:06 - 22:08]

and the other is dropout.

### [22:08 - 22:09]

These two techniques

### [22:09 - 22:10]

are still widely used

### [22:10 - 22:11]

in today's neural network

### [22:11 - 22:13]

training technologies.

### [22:13 - 22:15]

And another aspect

### [22:15 - 22:16]

about the AlexNet paper

### [22:16 - 22:20]

is about its excellent engineering work.

### [22:20 - 22:23]

It has explored the potential

### [22:23 - 22:24]

of using GPUs

### [22:24 - 22:26]

to train their models.

### [22:26 - 22:27]

And actually,

### [22:27 - 22:29]

they have paved the foundations

### [22:29 - 22:30]

for GPU training

### [22:30 - 22:32]

for the next 10 years.

### [22:32 - 22:33]

They have introduced

### [22:33 - 22:35]

two basic concepts

### [22:35 - 22:36]

about GPU training.

### [22:36 - 22:38]

One is data augmentation

### [22:38 - 22:41]

and the other is model distribution.

### [22:41 - 22:43]

In the case of data distribution,

### [22:43 - 22:45]

different samples

### [22:45 - 22:46]

in the same mini-batch

### [22:46 - 22:47]

can be handled

### [22:47 - 22:48]

by different GPUs,

### [22:48 - 22:49]

so the computation per GPU

### [22:49 - 22:51]

can be largely reduced.

### [22:51 - 22:53]

In the case of model distribution,

### [22:53 - 22:56]

different sets of filters

### [22:56 - 22:57]

or different layers

### [22:57 - 22:58]

can be stored

### [22:58 - 22:59]

in different GPUs,

### [22:59 - 23:00]

so it can also help

### [23:00 - 23:01]

to largely reduce

### [23:01 - 23:03]

the memory consumption.

### [23:03 - 23:04]

And these are still

### [23:04 - 23:05]

the foundations

### [23:05 - 23:07]

in today's GPU implementation.

### [23:08 - 23:10]

And here is just

### [23:10 - 23:11]

a side-by-side comparison

### [23:11 - 23:12]

between the original

### [23:12 - 23:13]

LeNet architecture

### [23:13 - 23:15]

and the AlexNet architecture.

### [23:15 - 23:16]

At the high level,

### [23:16 - 23:18]

they are just the same thing

### [23:18 - 23:20]

because they are just

### [23:20 - 23:23]

a composition of many simple

### [23:23 - 23:25]

and general modules,

### [23:25 - 23:26]

convolutional layers,

### [23:26 - 23:27]

pooling layers,

### [23:27 - 23:29]

and fully connected layers.

### [23:29 - 23:31]

They are just the same thing.

### [23:31 - 23:33]

Then what would be the difference?

### [23:33 - 23:36]

So why is AlexNet revolutionary?

### [23:36 - 23:37]

The first difference

### [23:37 - 23:39]

is that the AlexNet is deeper.

### [23:39 - 23:42]

It has three more convolutional layers

### [23:42 - 23:44]

and one more pooling layer.

### [23:44 - 23:45]

And these layers

### [23:45 - 23:46]

can help it to learn

### [23:46 - 23:48]

higher-level abstractions

### [23:48 - 23:49]

from larger-scale data

### [23:49 - 23:51]

than it is going to have

### [23:51 - 23:53]

a stronger representational power

### [23:53 - 23:56]

than the shallower models.

### [23:56 - 23:57]

Another difference

### [23:57 - 23:58]

is the usage

### [23:58 - 24:00]

of the ReLU activation,

### [24:00 - 24:01]

as you have seen

### [24:01 - 24:02]

in Philip's talk.

### [24:02 - 24:03]

In the original LeNet,

### [24:03 - 24:04]

the activation function

### [24:04 - 24:06]

is a sigmoid.

### [24:06 - 24:08]

And when the input signal

### [24:08 - 24:09]

is too big

### [24:09 - 24:11]

or the input signal is too small,

### [24:11 - 24:12]

we will have zero gradients

### [24:12 - 24:13]

when using

### [24:13 - 24:15]

the sigmoid activation function.

### [24:15 - 24:16]

And as a comparison,

### [24:16 - 24:17]

in the AlexNet,

### [24:17 - 24:18]

for the first time,

### [24:18 - 24:20]

it started to explore

### [24:20 - 24:22]

the usage of ReLU activation function

### [24:22 - 24:23]

to train a very deep

### [24:23 - 24:25]

neural network architecture.

### [24:25 - 24:26]

And in the case of ReLU,

### [24:26 - 24:27]

it is only when

### [24:27 - 24:28]

the input signal

### [24:28 - 24:30]

is smaller than zero,

### [24:30 - 24:31]

it will have zero gradient.

### [24:31 - 24:32]

Then when you have

### [24:32 - 24:34]

many activation functions

### [24:34 - 24:36]

in a very deep neural network,

### [24:36 - 24:37]

you will have

### [24:37 - 24:39]

a much higher chance

### [24:39 - 24:41]

of having non-zero gradients

### [24:41 - 24:43]

in the backward propagation process.

### [24:43 - 24:44]

It turns out that

### [24:44 - 24:46]

this can largely facilitate

### [24:46 - 24:48]

the training of very deep models.

### [24:48 - 24:50]

So in some sense,

### [24:50 - 24:51]

the introduction

### [24:51 - 24:52]

of the ReLU activation

### [24:52 - 24:55]

is kind of a revolution

### [24:55 - 24:58]

of the deep learning.

### [24:58 - 25:00]

Another huge difference

### [25:00 - 25:01]

between these two architectures

### [25:01 - 25:03]

that has been largely ignored

### [25:03 - 25:04]

by many people

### [25:04 - 25:05]

is that

### [25:05 - 25:06]

the AlexNet

### [25:06 - 25:07]

is actually

### [25:07 - 25:08]

a wider architecture

### [25:08 - 25:09]

than the original LeNet.

### [25:09 - 25:10]

And in the terminology

### [25:10 - 25:12]

of deep learning,

### [25:12 - 25:13]

by wider,

### [25:13 - 25:14]

we usually mean

### [25:14 - 25:16]

the model has more channels.

### [25:16 - 25:18]

Then by having more channels

### [25:18 - 25:19]

for every single layer,

### [25:19 - 25:20]

we are going to have

### [25:20 - 25:22]

a richer set of features

### [25:22 - 25:25]

than it will be more representative

### [25:25 - 25:31]

than a narrower model.

### [25:31 - 25:33]

The success of the AlexNet

### [25:33 - 25:35]

in the ImageNet dataset

### [25:35 - 25:38]

has drawn a lot of attention

### [25:38 - 25:39]

in the community

### [25:39 - 25:41]

of computer vision.

### [25:41 - 25:42]

In the next year,

### [25:42 - 25:44]

after the AlexNet was proposed,

### [25:44 - 25:46]

the computer vision community

### [25:46 - 25:48]

started to pay more attention

### [25:48 - 25:50]

into the understanding

### [25:50 - 25:52]

of the neural network behaviors.

### [25:52 - 25:53]

And one way

### [25:53 - 25:55]

for the computer vision community

### [25:55 - 25:58]

to obtain better understanding

### [25:58 - 26:00]

is by visualization.

### [26:00 - 26:02]

And a very successful

### [26:02 - 26:04]

visualization method

### [26:04 - 26:06]

is to answer the following question.

### [26:06 - 26:08]

So what input

### [26:08 - 26:09]

can produce

### [26:09 - 26:11]

a specific feature?

### [26:11 - 26:13]

In order to answer this question,

### [26:13 - 26:15]

we can do the following two steps.

### [26:15 - 26:16]

First,

### [26:16 - 26:18]

we just need to set

### [26:18 - 26:19]

a feature map

### [26:19 - 26:21]

as a one-hot vector

### [26:21 - 26:22]

or a one-hot tensor.

### [26:22 - 26:23]

That is to say,

### [26:23 - 26:25]

for this specific feature map,

### [26:25 - 26:27]

there is only one element

### [26:27 - 26:28]

that is non-zero,

### [26:28 - 26:29]

and all other elements

### [26:29 - 26:31]

would be set as zero.

### [26:31 - 26:32]

Then we can use

### [26:32 - 26:33]

exactly the same

### [26:33 - 26:35]

back-propagation algorithm

### [26:35 - 26:36]

to propagate

### [26:36 - 26:37]

this one-hot feature map

### [26:37 - 26:38]

from the feature space

### [26:38 - 26:40]

back to the pixel space.

### [26:40 - 26:41]

Then we will have

### [26:41 - 26:42]

some visualizations

### [26:42 - 26:43]

about this feature

### [26:43 - 26:46]

on the pixel space.

### [26:46 - 26:47]

And next,

### [26:47 - 26:48]

I'm going to show

### [26:48 - 26:49]

some visualization

### [26:49 - 26:51]

obtained in this way.

### [26:51 - 26:52]

And I'm going to show

### [26:52 - 26:53]

the visualization

### [26:53 - 26:55]

of a convolutional neural network

### [26:55 - 26:57]

that has five convolutional layers.

### [26:57 - 26:59]

And here are the visualizations

### [26:59 - 27:01]

of the first convolutional layer.

### [27:01 - 27:02]

Here I'm going to show

### [27:02 - 27:06]

the features on the left,

### [27:06 - 27:07]

and I'm also going to show

### [27:07 - 27:09]

some stimuli on the right.

### [27:09 - 27:10]

So by stimuli,

### [27:10 - 27:12]

I mean these are the patches

### [27:12 - 27:14]

or input images

### [27:14 - 27:15]

that will have

### [27:15 - 27:16]

the strongest activations

### [27:16 - 27:18]

in the corresponding features.

### [27:18 - 27:19]

And as we can see,

### [27:19 - 27:20]

in the first layer

### [27:20 - 27:21]

of this neural network,

### [27:21 - 27:22]

there are usually

### [27:22 - 27:24]

kind of edge detectors

### [27:24 - 27:26]

or some color detectors.

### [27:26 - 27:27]

And this behavior

### [27:27 - 27:28]

is very similar

### [27:28 - 27:29]

to a classical

### [27:29 - 27:30]

image recognition system

### [27:30 - 27:31]

in which the first layer

### [27:31 - 27:35]

is an edge detector.

### [27:35 - 27:37]

And here are some visualizations

### [27:37 - 27:39]

of the second convolutional layer

### [27:39 - 27:41]

in the same network.

### [27:41 - 27:42]

In this case,

### [27:42 - 27:43]

we can see that the features

### [27:43 - 27:45]

are slightly higher level

### [27:45 - 27:46]

than the features

### [27:46 - 27:48]

in the first layer.

### [27:48 - 27:49]

And we can see

### [27:49 - 27:51]

some of the features

### [27:51 - 27:53]

show some patterns of textures.

### [27:53 - 27:55]

And in some other cases,

### [27:55 - 27:56]

they show some local shapes

### [27:56 - 27:59]

such as a circle or a corner

### [27:59 - 28:00]

or the shape

### [28:00 - 28:02]

of a thin line.

### [28:02 - 28:03]

And this is why we say

### [28:03 - 28:04]

these features

### [28:04 - 28:05]

may be higher level

### [28:05 - 28:06]

than the features

### [28:06 - 28:07]

in the first layer

### [28:07 - 28:10]

which are just edges.

### [28:10 - 28:11]

And here are the visualizations

### [28:11 - 28:13]

of the third layer.

### [28:13 - 28:14]

In this case,

### [28:14 - 28:15]

we start to see that

### [28:15 - 28:16]

it begins to show

### [28:16 - 28:18]

some semantic patterns.

### [28:18 - 28:19]

For example,

### [28:19 - 28:21]

for this feature,

### [28:21 - 28:22]

it starts to show

### [28:22 - 28:23]

some semantic patterns

### [28:23 - 28:24]

about the upper body

### [28:24 - 28:26]

of human beings.

### [28:26 - 28:27]

And in another case,

### [28:27 - 28:28]

it starts to show

### [28:28 - 28:29]

the patterns

### [28:29 - 28:31]

of something like a net

### [28:31 - 28:35]

or a honeycomb.

### [28:35 - 28:36]

And again,

### [28:36 - 28:37]

here are the visualizations

### [28:37 - 28:38]

of the fourth layer.

### [28:38 - 28:39]

And again,

### [28:39 - 28:40]

it is higher level

### [28:40 - 28:41]

than the representations

### [28:41 - 28:42]

of the previous layer.

### [28:42 - 28:44]

And there are some shapes

### [28:44 - 28:45]

of dog heads

### [28:45 - 28:47]

or perhaps the shapes

### [28:47 - 28:49]

of the body of a bird

### [28:49 - 28:52]

with two legs.

### [28:52 - 28:53]

And again,

### [28:53 - 28:55]

these are the visualizations

### [28:55 - 28:59]

of the last convolutional network

### [28:59 - 29:00]

or the convolutional layer

### [29:00 - 29:01]

in this network.

### [29:01 - 29:02]

And again,

### [29:02 - 29:03]

this would be higher level.

### [29:03 - 29:04]

It is not perfect.

### [29:04 - 29:05]

For example,

### [29:05 - 29:06]

in this layer,

### [29:06 - 29:07]

it will mix

### [29:07 - 29:09]

several things together.

### [29:09 - 29:11]

But in some other examples,

### [29:11 - 29:12]

for example,

### [29:12 - 29:13]

for this filter,

### [29:13 - 29:15]

it will give the representations

### [29:15 - 29:17]

for different types of dogs.

### [29:17 - 29:19]

And for this filter,

### [29:19 - 29:21]

it will give the representations

### [29:21 - 29:24]

for different types of animals

### [29:24 - 29:26]

with eyes.

### [29:26 - 29:27]

And actually,

### [29:27 - 29:29]

in computer vision,

### [29:29 - 29:31]

these high level abstractions

### [29:31 - 29:33]

or high level representations

### [29:33 - 29:34]

are very difficult

### [29:34 - 29:35]

to be designed by hand.

### [29:35 - 29:37]

So these high level representations

### [29:37 - 29:38]

are exactly

### [29:38 - 29:40]

what the computer vision community

### [29:40 - 29:42]

have been looking for

### [29:42 - 29:44]

over the last several decades.

### [29:44 - 29:46]

So this visualization

### [29:46 - 29:47]

helps to convince

### [29:47 - 29:49]

the computer vision community

### [29:49 - 29:51]

that deep learning

### [29:51 - 29:53]

or deep convolutional neural networks

### [29:53 - 29:58]

are the right way to go.

### [29:58 - 30:01]

And as a byproduct

### [30:01 - 30:03]

of this visualization,

### [30:03 - 30:04]

at that time,

### [30:04 - 30:06]

the computer vision community

### [30:06 - 30:08]

started to make

### [30:08 - 30:11]

a very significant discovery.

### [30:11 - 30:12]

At that time,

### [30:12 - 30:13]

they discovered that

### [30:13 - 30:15]

these deep representations

### [30:15 - 30:17]

are transferable.

### [30:17 - 30:19]

And in my opinion,

### [30:19 - 30:20]

this is actually

### [30:20 - 30:22]

the single most important discovery

### [30:22 - 30:25]

in the deep learning revolution.

### [30:25 - 30:26]

Then what does it mean

### [30:26 - 30:27]

by transferable

### [30:27 - 30:28]

or what does it mean

### [30:28 - 30:30]

by transfer learning?

### [30:30 - 30:31]

In my opinion,

### [30:31 - 30:32]

transfer learning

### [30:32 - 30:34]

is just an amazing idea.

### [30:34 - 30:35]

Let's say,

### [30:35 - 30:36]

if we can train

### [30:36 - 30:37]

a larger scale network

### [30:37 - 30:39]

on a larger scale data set,

### [30:39 - 30:40]

and if we can discover

### [30:40 - 30:41]

that this network

### [30:41 - 30:42]

will learn

### [30:42 - 30:44]

some high level representations

### [30:44 - 30:46]

or high level abstractions,

### [30:46 - 30:47]

then we can hope

### [30:47 - 30:49]

this high level representation

### [30:49 - 30:50]

is not just related

### [30:50 - 30:51]

to this data set.

### [30:51 - 30:53]

These high level representations

### [30:53 - 30:54]

can also be used

### [30:54 - 30:55]

in many other

### [30:55 - 30:56]

smaller scale data sets

### [30:56 - 30:58]

that have something to do

### [30:58 - 31:00]

with this larger scale data set.

### [31:00 - 31:01]

But in order to enjoy

### [31:01 - 31:02]

this benefit,

### [31:02 - 31:04]

we can transfer these features

### [31:04 - 31:06]

to some smaller scale data set,

### [31:06 - 31:07]

and usually we can do

### [31:07 - 31:09]

this transfer learning

### [31:09 - 31:10]

by fine-tuning.

### [31:10 - 31:11]

For example,

### [31:11 - 31:12]

we can just train

### [31:12 - 31:13]

a small part

### [31:13 - 31:14]

of the neural network.

### [31:14 - 31:15]

And this can be done

### [31:15 - 31:17]

on just small scale data sets.

### [31:17 - 31:19]

And this discovery

### [31:19 - 31:20]

can enable

### [31:20 - 31:22]

deep learning models

### [31:22 - 31:23]

to be applied

### [31:23 - 31:25]

on small scale data sets.

### [31:25 - 31:26]

So you don't need

### [31:26 - 31:28]

a larger scale data set

### [31:28 - 31:29]

for your specific task

### [31:29 - 31:31]

to train very large scale models.

### [31:31 - 31:32]

You just need

### [31:32 - 31:33]

a small amount

### [31:33 - 31:34]

of data set

### [31:34 - 31:35]

that is relevant

### [31:35 - 31:36]

to your task.

### [31:36 - 31:37]

Then this discovery

### [31:37 - 31:39]

completely revolutionized

### [31:39 - 31:41]

the computer vision community.

### [31:41 - 31:43]

Because with the help

### [31:43 - 31:44]

of transfer learning,

### [31:44 - 31:45]

we can enjoy

### [31:45 - 31:46]

the benefits

### [31:46 - 31:47]

of deep learning

### [31:47 - 31:48]

in basically

### [31:48 - 31:49]

all small scale data sets,

### [31:49 - 31:50]

and they can achieve

### [31:50 - 31:52]

unprecedented accuracy

### [31:52 - 31:53]

in many of the

### [31:53 - 31:54]

computer vision tasks.

### [31:54 - 31:55]

So this is just

### [31:55 - 31:57]

game changing.

### [31:57 - 31:58]

So in this sense,

### [31:58 - 32:00]

some of the larger scale data sets

### [32:00 - 32:02]

such as the ImageNet data set

### [32:02 - 32:03]

is no longer

### [32:03 - 32:04]

a fine-grained

### [32:04 - 32:05]

or a tedious

### [32:05 - 32:07]

fine-grained classification problem

### [32:07 - 32:08]

that has more than

### [32:08 - 32:09]

one million images

### [32:09 - 32:10]

or one thousand classes

### [32:10 - 32:12]

that I'm not going to tell.

### [32:12 - 32:14]

The ImageNet data set

### [32:14 - 32:15]

becomes the engine

### [32:15 - 32:17]

for us to learn

### [32:17 - 32:19]

general representations

### [32:19 - 32:20]

that can help

### [32:20 - 32:21]

basically all

### [32:21 - 32:23]

computer vision tasks.

### [32:23 - 32:24]

And this discovery

### [32:24 - 32:26]

of transfer learning

### [32:26 - 32:28]

is so influential

### [32:28 - 32:29]

that its impact

### [32:29 - 32:30]

is far beyond

### [32:30 - 32:31]

just computer vision.

### [32:31 - 32:32]

For example,

### [32:32 - 32:33]

the GPT

### [32:33 - 32:34]

or the chat GPT model

### [32:34 - 32:35]

was also developed

### [32:35 - 32:36]

in exactly

### [32:36 - 32:42]

the same principle.

### [32:42 - 32:43]

Then next,

### [32:43 - 32:44]

I'm going to talk about

### [32:44 - 32:45]

another work

### [32:45 - 32:46]

that is kind of

### [32:46 - 32:48]

my favorite.

### [32:48 - 32:49]

This work is called

### [32:49 - 32:50]

VGG,

### [32:50 - 32:51]

which is short

### [32:51 - 32:52]

for the

### [32:52 - 32:54]

Visual Geometric Group

### [32:54 - 32:55]

which is a group

### [32:55 - 32:57]

at Oxford University.

### [32:57 - 32:58]

It can also be short

### [32:58 - 33:00]

for a very good group

### [33:00 - 33:04]

or something like that.

### [33:04 - 33:05]

The VGG architecture

### [33:05 - 33:07]

is very simple.

### [33:07 - 33:10]

It is just the idea

### [33:10 - 33:12]

about how can we build

### [33:12 - 33:13]

a very deep

### [33:13 - 33:14]

neural network architecture

### [33:14 - 33:15]

without bells

### [33:15 - 33:16]

and whistles.

### [33:16 - 33:17]

So,

### [33:17 - 33:18]

the VGG network

### [33:18 - 33:20]

is a highly modularized design

### [33:20 - 33:21]

and it only has

### [33:21 - 33:23]

convolution layers,

### [33:23 - 33:24]

pooling layers,

### [33:24 - 33:25]

connected layers

### [33:25 - 33:26]

and all the convolution layers

### [33:26 - 33:27]

are actually

### [33:27 - 33:28]

three by three

### [33:28 - 33:29]

so you don't need to

### [33:29 - 33:30]

carefully design these layers.

### [33:30 - 33:31]

So,

### [33:31 - 33:32]

the VGG network

### [33:32 - 33:33]

just simply

### [33:33 - 33:34]

stack the same type

### [33:34 - 33:35]

of modules

### [33:35 - 33:36]

and they can build

### [33:36 - 33:37]

a very deep

### [33:37 - 33:38]

neural network architecture

### [33:38 - 33:39]

for example,

### [33:39 - 33:40]

up to 90 layers

### [33:40 - 33:41]

which are twice as deep

### [33:41 - 33:42]

as the previous

### [33:42 - 33:44]

deepest model.

### [33:44 - 33:45]

And interestingly,

### [33:45 - 33:46]

for the first time,

### [33:46 - 33:48]

it showed clear evidence

### [33:48 - 33:49]

that a deeper model

### [33:49 - 33:50]

would be better

### [33:50 - 33:51]

than their

### [33:51 - 33:53]

shallow counterpart.

### [33:54 - 33:55]

So this seems to be

### [33:55 - 33:57]

a surprising statement

### [33:57 - 33:58]

because,

### [33:58 - 33:59]

well,

### [33:59 - 34:00]

actually,

### [34:00 - 34:01]

at that time

### [34:01 - 34:02]

there was very little

### [34:02 - 34:03]

clear evidence

### [34:03 - 34:04]

that a deeper model

### [34:04 - 34:05]

is better.

### [34:05 - 34:06]

Part of the reason

### [34:06 - 34:07]

is that

### [34:07 - 34:09]

before the VGGNet paper,

### [34:09 - 34:10]

when people increase

### [34:10 - 34:11]

the depth

### [34:11 - 34:12]

of the neural networks,

### [34:12 - 34:14]

they also do something else

### [34:14 - 34:15]

at the same time.

### [34:15 - 34:16]

So there was no

### [34:16 - 34:17]

clear evidence

### [34:17 - 34:18]

that going deeper

### [34:18 - 34:19]

is the only reason,

### [34:19 - 34:21]

is the main reason

### [34:21 - 34:22]

for the network

### [34:22 - 34:23]

to get better accuracy.

### [34:23 - 34:25]

Then in the VGGNet paper,

### [34:25 - 34:26]

the authors have designed

### [34:26 - 34:29]

very carefully controlled experiments.

### [34:29 - 34:30]

They tried to remove

### [34:30 - 34:31]

all the bells and whistles

### [34:31 - 34:33]

in the architectural design.

### [34:33 - 34:34]

They introduced very little

### [34:34 - 34:36]

config engineering

### [34:36 - 34:37]

and they developed

### [34:37 - 34:38]

very simple rules

### [34:38 - 34:39]

for them to set

### [34:39 - 34:40]

the number of channels

### [34:40 - 34:42]

or the number of layers

### [34:42 - 34:43]

for every single stage.

### [34:43 - 34:45]

And all the thing they do

### [34:45 - 34:47]

is just to add

### [34:47 - 34:48]

more and more

### [34:48 - 34:50]

three by three convolutional layers.

### [34:50 - 34:52]

This is a very simple design.

### [34:52 - 34:53]

This is extremely simple.

### [34:53 - 34:55]

This is very elegant.

### [34:55 - 34:56]

However,

### [34:56 - 34:57]

these simple baselines

### [34:57 - 34:59]

are very hard to beat.

### [34:59 - 35:00]

Actually,

### [35:00 - 35:01]

in those years,

### [35:01 - 35:02]

the VGGNetworks

### [35:02 - 35:03]

are just the state-of-the-art

### [35:03 - 35:04]

architecture

### [35:04 - 35:05]

in computer vision.

### [35:05 - 35:06]

It is the default

### [35:06 - 35:07]

backbone architecture

### [35:07 - 35:08]

for us to solve

### [35:08 - 35:09]

many different problems,

### [35:09 - 35:11]

including classification,

### [35:11 - 35:12]

detection,

### [35:12 - 35:14]

and segmentation.

### [35:14 - 35:16]

And they can easily outperform

### [35:16 - 35:17]

the counterpart

### [35:17 - 35:18]

that uses

### [35:18 - 35:20]

shallower neural network architectures.

### [35:20 - 35:21]

Actually,

### [35:21 - 35:22]

the VGGNetworks

### [35:22 - 35:24]

are just the state-of-the-art

### [35:24 - 35:25]

before

### [35:25 - 35:28]

Deeper Neural Network came along.

### [35:28 - 35:30]

And there is just one caveat

### [35:30 - 35:32]

about the VGGNetwork architectures.

### [35:32 - 35:33]

That is,

### [35:33 - 35:34]

these models

### [35:34 - 35:37]

were not trained end-to-end.

### [35:37 - 35:38]

Surprisingly,

### [35:38 - 35:39]

these models were trained

### [35:39 - 35:40]

by a technique

### [35:40 - 35:41]

that is called

### [35:41 - 35:42]

a stage-wise training.

### [35:42 - 35:43]

For example,

### [35:43 - 35:44]

in order to train

### [35:44 - 35:45]

a Deeper Neural Network architecture,

### [35:45 - 35:46]

they need to pre-train

### [35:46 - 35:48]

a shallower counterpart of it.

### [35:48 - 35:49]

Then they add,

### [35:49 - 35:50]

for example,

### [35:50 - 35:51]

two more layers

### [35:51 - 35:52]

to the model,

### [35:52 - 35:53]

and then they keep

### [35:53 - 35:54]

fine-tuning it.

### [35:54 - 35:55]

So this stage-wise

### [35:55 - 35:56]

training strategy

### [35:56 - 35:57]

is actually

### [35:57 - 35:58]

not ideal.

### [35:58 - 35:59]

It is actually

### [35:59 - 36:00]

against

### [36:00 - 36:01]

the end-to-end training

### [36:01 - 36:02]

philosophy

### [36:02 - 36:03]

of deep learning.

### [36:03 - 36:04]

In order to train

### [36:04 - 36:05]

these model architectures

### [36:05 - 36:06]

from scratch,

### [36:06 - 36:07]

we need to develop

### [36:07 - 36:08]

better initialization

### [36:08 - 36:11]

algorithms.

### [36:11 - 36:12]

Then,

### [36:12 - 36:13]

in the next year

### [36:13 - 36:15]

after the VGGNetwork paper,

### [36:15 - 36:16]

the community

### [36:16 - 36:17]

started to pay

### [36:17 - 36:18]

more attention

### [36:18 - 36:19]

into the network

### [36:19 - 36:20]

initialization issue.

### [36:20 - 36:21]

So,

### [36:21 - 36:22]

now,

### [36:22 - 36:23]

let's zoom out

### [36:23 - 36:24]

a little bit again

### [36:24 - 36:25]

and we are going to talk

### [36:25 - 36:26]

about why these

### [36:26 - 36:27]

Deeper Neural Networks

### [36:27 - 36:28]

are more difficult

### [36:28 - 36:29]

to train.

### [36:29 - 36:30]

Intuitively,

### [36:30 - 36:31]

a very deep

### [36:31 - 36:32]

neural network

### [36:32 - 36:33]

will have

### [36:33 - 36:34]

just

### [36:34 - 36:35]

a stack

### [36:35 - 36:36]

of many

### [36:36 - 36:37]

building blocks

### [36:37 - 36:38]

and many modules.

### [36:38 - 36:39]

Now,

### [36:39 - 36:40]

let's say

### [36:40 - 36:41]

if every single

### [36:41 - 36:42]

building block

### [36:42 - 36:43]

will do something

### [36:43 - 36:44]

wrong

### [36:44 - 36:45]

or it will introduce

### [36:45 - 36:46]

some troubles,

### [36:46 - 36:47]

then,

### [36:47 - 36:48]

after we stack

### [36:48 - 36:49]

this building block

### [36:49 - 36:50]

for many times,

### [36:50 - 36:51]

our troubles

### [36:51 - 36:52]

will just

### [36:52 - 36:53]

simply be

### [36:53 - 36:54]

accumulated.

### [36:54 - 36:55]

So,

### [36:55 - 36:56]

in practice,

### [36:56 - 36:57]

we are going to see

### [36:57 - 36:58]

some exploding

### [36:58 - 36:59]

signal problem

### [36:59 - 37:00]

or we may also

### [37:00 - 37:01]

see some

### [37:01 - 37:02]

vanishing

### [37:02 - 37:03]

signal problem.

### [37:03 - 37:04]

And,

### [37:04 - 37:05]

in this case,

### [37:05 - 37:06]

we may need

### [37:06 - 37:07]

some network

### [37:07 - 37:08]

initializations

### [37:08 - 37:09]

to help us

### [37:09 - 37:10]

to get the neural

### [37:10 - 37:11]

networks

### [37:11 - 37:12]

to start training.

### [37:12 - 37:13]

Next,

### [37:13 - 37:14]

I'm going to delve

### [37:14 - 37:15]

a little bit

### [37:15 - 37:16]

deeper

### [37:16 - 37:17]

into the network

### [37:17 - 37:18]

initialization

### [37:18 - 37:19]

algorithms.

### [37:19 - 37:20]

So,

### [37:20 - 37:21]

let's say

### [37:21 - 37:22]

we have

### [37:22 - 37:23]

a layer

### [37:23 - 37:24]

which is

### [37:24 - 37:25]

linear

### [37:25 - 37:26]

in a neural

### [37:26 - 37:27]

network.

### [37:27 - 37:28]

In this case,

### [37:28 - 37:29]

the input,

### [37:29 - 37:30]

x,

### [37:30 - 37:31]

will have

### [37:31 - 37:32]

x nodes

### [37:32 - 37:33]

or x neurons

### [37:33 - 37:34]

and the output,

### [37:34 - 37:35]

y,

### [37:35 - 37:36]

will have

### [37:36 - 37:37]

m nodes

### [37:37 - 37:38]

and the output

### [37:38 - 37:39]

is just

### [37:39 - 37:40]

a linear

### [37:40 - 37:41]

transform

### [37:41 - 37:42]

of the input

### [37:42 - 37:43]

and the transformation

### [37:43 - 37:44]

will be

### [37:44 - 37:45]

represented

### [37:45 - 37:46]

by a weight

### [37:46 - 37:47]

matrix,

### [37:47 - 37:48]

w.

### [37:48 - 37:49]

And,

### [37:49 - 37:50]

if we further

### [37:50 - 37:51]

assume

### [37:51 - 37:52]

there is only

### [37:52 - 37:53]

linear activation

### [37:53 - 37:54]

inside the entire

### [37:54 - 37:55]

neural network,

### [37:55 - 37:56]

then we can show

### [37:56 - 37:57]

that after

### [37:57 - 37:58]

the signal

### [37:58 - 37:59]

being processed

### [37:59 - 38:00]

by one layer,

### [38:00 - 38:01]

the variance

### [38:01 - 38:02]

of the signals

### [38:02 - 38:03]

will be scaled

### [38:03 - 38:04]

by a scaling

### [38:04 - 38:05]

factor.

### [38:05 - 38:06]

For example,

### [38:06 - 38:07]

this equation

### [38:07 - 38:08]

basically says

### [38:08 - 38:09]

the variance

### [38:09 - 38:10]

of the output

### [38:10 - 38:11]

of this layer

### [38:11 - 38:12]

equals

### [38:12 - 38:13]

to the number

### [38:13 - 38:14]

of input

### [38:14 - 38:15]

neurons

### [38:15 - 38:16]

times

### [38:16 - 38:17]

the variance

### [38:17 - 38:18]

of the weight

### [38:18 - 38:19]

of this layer.

### [38:19 - 38:20]

So this layer

### [38:20 - 38:21]

will scale

### [38:21 - 38:22]

the signal,

### [38:22 - 38:23]

will scale

### [38:23 - 38:24]

the variance

### [38:24 - 38:25]

of the signal

### [38:25 - 38:26]

by this scaling

### [38:26 - 38:27]

factor.

### [38:27 - 38:28]

And,

### [38:28 - 38:29]

we can apply

### [38:29 - 38:30]

this formulation

### [38:30 - 38:31]

many times

### [38:31 - 38:32]

in a very

### [38:32 - 38:33]

deep

### [38:33 - 38:34]

neural network

### [38:34 - 38:35]

if we don't

### [38:35 - 38:36]

have any

### [38:36 - 38:37]

activation

### [38:37 - 38:38]

or if our

### [38:38 - 38:39]

activation

### [38:39 - 38:40]

function

### [38:40 - 38:41]

is linear.

### [38:41 - 38:42]

Well,

### [38:42 - 38:43]

we are going

### [38:43 - 38:44]

to see

### [38:44 - 38:45]

that the variance

### [38:45 - 38:46]

is still

### [38:46 - 38:47]

scaled

### [38:47 - 38:48]

as the output,

### [38:48 - 38:49]

the variance

### [38:49 - 38:50]

of the network

### [38:50 - 38:51]

output

### [38:51 - 38:52]

equals

### [38:52 - 38:53]

to the product

### [38:53 - 38:54]

of these many

### [38:54 - 38:55]

numbers

### [38:55 - 38:56]

times

### [38:56 - 38:57]

the variance

### [38:57 - 38:58]

of the network

### [38:58 - 38:59]

input.

### [38:59 - 39:00]

And this is

### [39:00 - 39:01]

the formulation

### [39:01 - 39:02]

of the forward

### [39:02 - 39:03]

propagation.

### [39:03 - 39:04]

And,

### [39:04 - 39:05]

we can

### [39:05 - 39:06]

do

### [39:06 - 39:07]

some math

### [39:07 - 39:08]

and then

### [39:08 - 39:09]

we will get

### [39:09 - 39:10]

a backward

### [39:10 - 39:11]

formulation

### [39:11 - 39:12]

and the backward

### [39:12 - 39:13]

formulation

### [39:13 - 39:14]

is in a very

### [39:14 - 39:15]

similar fashion.

### [39:15 - 39:16]

And basically

### [39:16 - 39:17]

this is

### [39:17 - 39:18]

the

### [39:18 - 39:19]

product

### [39:19 - 39:20]

of these

### [39:20 - 39:21]

many

### [39:21 - 39:22]

factors

### [39:22 - 39:23]

basically

### [39:23 - 39:24]

says

### [39:24 - 39:25]

if

### [39:25 - 39:26]

the scaling

### [39:26 - 39:27]

factor

### [39:27 - 39:28]

for every

### [39:28 - 39:29]

single

### [39:29 - 39:30]

layer

### [39:30 - 39:31]

is

### [39:31 - 39:32]

smaller

### [39:32 - 39:33]

than

### [39:33 - 39:34]

one,

### [39:34 - 39:35]

then

### [39:35 - 39:36]

after

### [39:36 - 39:37]

this

### [39:37 - 39:38]

effect

### [39:38 - 39:39]

we can

### [39:39 - 39:40]

see

### [39:40 - 39:41]

that

### [39:41 - 39:42]

the

### [39:42 - 39:43]

product

### [39:43 - 39:44]

of

### [39:44 - 39:45]

this

### [39:45 - 39:46]

scaling factor

### [39:46 - 39:47]

is greater

### [39:47 - 39:48]

than one

### [39:48 - 39:49]

for every

### [39:49 - 39:50]

single

### [39:50 - 39:51]

layer,

### [39:51 - 39:52]

then after

### [39:52 - 39:53]

this effect

### [39:53 - 39:54]

will be

### [39:54 - 39:55]

accumulated

### [39:55 - 39:56]

by many

### [39:56 - 39:57]

layers,

### [39:57 - 39:58]

you are

### [39:58 - 39:59]

going to

### [39:59 - 40:00]

experience

### [40:00 - 40:01]

the

### [40:01 - 40:02]

vanishing

### [40:02 - 40:03]

gradient

### [40:03 - 40:04]

problem.

### [40:04 - 40:05]

That is

### [40:05 - 40:06]

to say

### [40:06 - 40:07]

your network

### [40:07 - 40:08]

is not

### [40:08 - 40:09]

going to

### [40:09 - 40:10]

train.

### [40:10 - 40:11]

It seems

### [40:11 - 40:12]

to be

### [40:12 - 40:13]

saturated

### [40:13 - 40:14]

or it

### [40:14 - 40:15]

will

### [40:15 - 40:16]

be

### [40:16 - 40:17]

diverged

### [40:17 - 40:18]

perhaps

### [40:18 - 40:19]

in the

### [40:19 - 40:20]

first

### [40:20 - 40:21]

iteration.

### [40:21 - 40:22]

Then in

### [40:22 - 40:23]

order for

### [40:23 - 40:24]

the network

### [40:24 - 40:25]

to at

### [40:25 - 40:26]

least

### [40:26 - 40:27]

start

### [40:27 - 40:28]

training,

### [40:28 - 40:29]

we need

### [40:29 - 40:30]

to develop

### [40:30 - 40:31]

good

### [40:31 - 40:32]

initialization

### [40:32 - 40:33]

algorithms

### [40:33 - 40:34]

and the

### [40:34 - 40:35]

previous

### [40:35 - 40:36]

derivation

### [40:36 - 40:37]

will lead

### [40:37 - 40:38]

us to

### [40:38 - 40:39]

this

### [40:39 - 40:40]

initialization

### [40:40 - 40:41]

method

### [40:41 - 40:42]

which

### [40:42 - 40:43]

is

### [40:43 - 40:44]

called

### [40:44 - 40:45]

the

### [40:45 - 40:46]

forward

### [40:46 - 40:47]

formulation.

### [40:47 - 40:48]

You may

### [40:48 - 40:49]

either

### [40:49 - 40:50]

want to

### [40:50 - 40:51]

set the

### [40:51 - 40:52]

forward

### [40:52 - 40:53]

formulation

### [40:53 - 40:54]

as one

### [40:54 - 40:55]

or the

### [40:55 - 40:56]

backward

### [40:56 - 40:57]

formulation

### [40:57 - 40:58]

as one.

### [40:58 - 40:59]

This is

### [40:59 - 41:00]

how you

### [41:00 - 41:01]

can

### [41:01 - 41:02]

initialize

### [41:02 - 41:03]

the

### [41:03 - 41:04]

weight

### [41:04 - 41:05]

in

### [41:05 - 41:06]

your

### [41:06 - 41:07]

neural

### [41:07 - 41:08]

network

### [41:08 - 41:09]

for

### [41:09 - 41:10]

every

### [41:10 - 41:11]

single

### [41:11 - 41:12]

layer.

### [41:12 - 41:13]

And the

### [41:13 - 41:14]

previous

### [41:14 - 41:15]

derivation

### [41:15 - 41:16]

was based

### [41:16 - 41:17]

on the

### [41:17 - 41:18]

assumption

### [41:18 - 41:19]

that the

### [41:19 - 41:20]

activation

### [41:20 - 41:21]

function is

### [41:21 - 41:22]

linear.

### [41:22 - 41:23]

And in

### [41:23 - 41:24]

practice,

### [41:24 - 41:25]

usually that's

### [41:25 - 41:26]

not what

### [41:26 - 41:27]

you want.

### [41:27 - 41:28]

You may

### [41:28 - 41:29]

want to

### [41:29 - 41:30]

introduce

### [41:30 - 41:31]

a

### [41:31 - 41:32]

ReLU

### [41:32 - 41:33]

activation.

### [41:33 - 41:34]

Then we

### [41:34 - 41:35]

can also

### [41:35 - 41:36]

show that

### [41:36 - 41:37]

with the

### [41:37 - 41:38]

introduction

### [41:38 - 41:39]

of

### [41:39 - 41:40]

ReLU,

### [41:40 - 41:41]

you

### [41:41 - 41:42]

the ReLU

### [41:42 - 41:43]

activation

### [41:43 - 41:44]

may

### [41:44 - 41:45]

cut

### [41:45 - 41:46]

half of

### [41:46 - 41:47]

a signal

### [41:47 - 41:48]

in the

### [41:48 - 41:49]

training

### [41:49 - 41:50]

process.

### [41:50 - 41:51]

That's

### [41:51 - 41:52]

why you

### [41:52 - 41:53]

need to

### [41:53 - 41:54]

introduce

### [41:54 - 41:55]

this

### [41:55 - 41:56]

scaling

### [41:56 - 41:57]

factor

### [41:57 - 41:58]

of

### [41:58 - 41:59]

one

### [41:59 - 42:00]

over

### [42:00 - 42:01]

two.

### [42:01 - 42:02]

And even

### [42:02 - 42:03]

though this

### [42:03 - 42:04]

seems to

### [42:04 - 42:05]

be a

### [42:05 - 42:06]

very

### [42:06 - 42:07]

small

### [42:07 - 42:08]

change

### [42:08 - 42:09]

comparing

### [42:09 - 42:10]

with

### [42:10 - 42:11]

the

### [42:11 - 42:12]

initialization

### [42:12 - 42:13]

method,

### [42:13 - 42:14]

you are

### [42:14 - 42:15]

going to

### [42:15 - 42:16]

experience

### [42:16 - 42:17]

the

### [42:17 - 42:18]

vanishing

### [42:18 - 42:19]

gradient

### [42:19 - 42:20]

problem in

### [42:20 - 42:21]

this case.

### [42:21 - 42:22]

And this

### [42:22 - 42:23]

initialization

### [42:23 - 42:24]

method can

### [42:24 - 42:25]

help us

### [42:25 - 42:26]

to train

### [42:26 - 42:27]

the VGG

### [42:27 - 42:28]

network

### [42:28 - 42:29]

from

### [42:29 - 42:30]

scratch

### [42:30 - 42:31]

without

### [42:31 - 42:32]

the

### [42:32 - 42:33]

requirement

### [42:33 - 42:34]

of

### [42:34 - 42:35]

statewide

### [42:35 - 42:36]

training.

### [42:36 - 42:37]

And this

### [42:37 - 42:38]

is about

### [42:38 - 42:39]

how we

### [42:39 - 42:40]

can

### [42:40 - 42:41]

design

### [42:41 - 42:42]

deep

### [42:42 - 42:43]

and

### [42:43 - 42:44]

at

### [42:44 - 42:45]

the

### [42:45 - 42:46]

same

### [42:46 - 42:47]

time

### [42:47 - 42:48]

economical

### [42:48 - 42:49]

convolutional

### [42:49 - 42:50]

neural

### [42:50 - 42:51]

networks.

### [42:51 - 42:52]

There are

### [42:52 - 42:53]

several

### [42:53 - 42:54]

interesting

### [42:54 - 42:55]

ideas

### [42:55 - 42:56]

involved.

### [42:56 - 42:57]

The

### [42:57 - 42:58]

first

### [42:58 - 42:59]

idea

### [42:59 - 43:00]

is to

### [43:00 - 43:01]

use

### [43:01 - 43:02]

multiple

### [43:02 - 43:03]

branches.

### [43:03 - 43:04]

For

### [43:04 - 43:05]

example,

### [43:05 - 43:06]

you

### [43:06 - 43:07]

may

### [43:07 - 43:08]

have

### [43:08 - 43:09]

one

### [43:09 - 43:10]

by one,

### [43:10 - 43:11]

three by

### [43:11 - 43:12]

three,

### [43:12 - 43:13]

or five

### [43:13 - 43:14]

by five

### [43:14 - 43:15]

convolutions

### [43:15 - 43:16]

in the

### [43:16 - 43:17]

same

### [43:17 - 43:18]

module.

### [43:18 - 43:19]

And at

### [43:19 - 43:20]

the

### [43:20 - 43:21]

same

### [43:21 - 43:22]

time,

### [43:22 - 43:23]

you

### [43:23 - 43:24]

may

### [43:24 - 43:25]

use

### [43:25 - 43:26]

a

### [43:26 - 43:27]

one

### [43:27 - 43:28]

by one

### [43:28 - 43:29]

convolution

### [43:29 - 43:30]

to

### [43:30 - 43:31]

flexibly

### [43:31 - 43:32]

control

### [43:32 - 43:33]

the

### [43:33 - 43:34]

number

### [43:34 - 43:35]

of

### [43:35 - 43:36]

channels

### [43:36 - 43:37]

in

### [43:37 - 43:38]

your

### [43:38 - 43:39]

module.

### [43:39 - 43:40]

So it

### [43:40 - 43:41]

is a

### [43:41 - 43:42]

shortcut

### [43:42 - 43:43]

because

### [43:43 - 43:44]

this one

### [43:44 - 43:45]

by one

### [43:45 - 43:46]

convolution

### [43:46 - 43:47]

can

### [43:47 - 43:48]

be

### [43:48 - 43:49]

shallower

### [43:49 - 43:50]

than

### [43:50 - 43:51]

the

### [43:51 - 43:52]

other

### [43:52 - 43:53]

branches

### [43:53 - 43:54]

in

### [43:54 - 43:55]

the

### [43:55 - 43:56]

same

### [43:56 - 43:57]

module.

### [43:57 - 43:58]

So it

### [43:58 - 43:59]

can

### [43:59 - 44:00]

be

### [44:00 - 44:01]

called

### [44:01 - 44:02]

a

### [44:02 - 44:03]

shortcut.

### [44:03 - 44:04]

Well,

### [44:04 - 44:05]

actually,

### [44:05 - 44:06]

in

### [44:06 - 44:07]

my

### [44:07 - 44:08]

previous

### [44:08 - 44:09]

lecture,

### [44:09 - 44:10]

I

### [44:10 - 44:11]

talked

### [44:11 - 44:12]

a

### [44:12 - 44:13]

little

### [44:13 - 44:14]

bit

### [44:14 - 44:15]

about

### [44:15 - 44:16]

neural

### [44:16 - 44:17]

network

### [44:17 - 44:18]

design.

### [44:18 - 44:19]

However,

### [44:19 - 44:20]

I

### [44:20 - 44:21]

also

### [44:21 - 44:22]

introduced

### [44:22 - 44:23]

another

### [44:23 - 44:24]

problem.

### [44:24 - 44:25]

So the

### [44:25 - 44:26]

crazy

### [44:26 - 44:27]

design

### [44:27 - 44:28]

of

### [44:28 - 44:29]

these

### [44:29 - 44:30]

architectures

### [44:30 - 44:31]

may

### [44:31 - 44:32]

break

### [44:32 - 44:33]

the

### [44:33 - 44:34]

simple

### [44:34 - 44:35]

assumptions

### [44:35 - 44:36]

that

### [44:36 - 44:37]

exist

### [44:37 - 44:38]

in

### [44:38 - 44:39]

neural

### [44:39 - 44:40]

networks.

### [44:40 - 44:41]

And

### [44:41 - 44:42]

motivated

### [44:42 - 44:43]

by

### [44:43 - 44:44]

these

### [44:44 - 44:45]

inception

### [44:45 - 44:46]

architectures,

### [44:46 - 44:47]

people

### [44:47 - 44:48]

started

### [44:48 - 44:49]

to

### [44:49 - 44:50]

look

### [44:50 - 44:51]

at

### [44:51 - 44:52]

another

### [44:52 - 44:53]

family

### [44:53 - 44:54]

of

### [44:54 - 44:55]

methods,

### [44:55 - 44:56]

which

### [44:56 - 44:57]

is

### [44:57 - 44:58]

called

### [44:58 - 44:59]

normalization

### [44:59 - 45:00]

modules

### [45:00 - 45:01]

in

### [45:01 - 45:02]

the

### [45:02 - 45:03]

neural

### [45:03 - 45:04]

networks.

### [45:04 - 45:05]

And

### [45:05 - 45:06]

in

### [45:06 - 45:07]

the

### [45:07 - 45:08]

neural

### [45:08 - 45:09]

networks,

### [45:09 - 45:10]

there

### [45:10 - 45:11]

are

### [45:11 - 45:12]

several

### [45:12 - 45:13]

methods

### [45:13 - 45:14]

to

### [45:14 - 45:15]

normalize

### [45:15 - 45:16]

the

### [45:16 - 45:17]

inputs.

### [45:17 - 45:18]

And

### [45:18 - 45:19]

actually,

### [45:19 - 45:20]

even

### [45:20 - 45:21]

today,

### [45:21 - 45:22]

this is

### [45:22 - 45:23]

what you

### [45:23 - 45:24]

need to

### [45:24 - 45:25]

do as

### [45:25 - 45:26]

a

### [45:26 - 45:27]

preprocessing

### [45:27 - 45:28]

for

### [45:28 - 45:29]

your

### [45:29 - 45:30]

data.

### [45:30 - 45:31]

And

### [45:31 - 45:32]

on

### [45:32 - 45:33]

the

### [45:33 - 45:34]

other

### [45:34 - 45:35]

side,

### [45:35 - 45:36]

there

### [45:36 - 45:37]

are

### [45:37 - 45:38]

a

### [45:38 - 45:39]

number

### [45:39 - 45:40]

of

### [45:40 - 45:41]

methods

### [45:41 - 45:42]

that

### [45:42 - 45:43]

you

### [45:43 - 45:44]

can

### [45:44 - 45:45]

use

### [45:45 - 45:46]

to

### [45:46 - 45:47]

normalize

### [45:47 - 45:48]

the

### [45:48 - 45:49]

neural

### [45:49 - 45:50]

networks.

### [45:50 - 45:51]

And

### [45:51 - 45:52]

in

### [45:52 - 45:53]

the

### [45:53 - 45:54]

neural

### [45:54 - 45:55]

networks,

### [45:55 - 45:56]

there

### [45:56 - 45:57]

are

### [45:57 - 45:58]

a

### [45:58 - 45:59]

number

### [45:59 - 46:00]

of

### [46:00 - 46:01]

methods

### [46:01 - 46:02]

that

### [46:02 - 46:03]

can

### [46:03 - 46:04]

keep

### [46:04 - 46:05]

the

### [46:05 - 46:06]

signal

### [46:06 - 46:07]

being

### [46:07 - 46:08]

normalized

### [46:08 - 46:09]

throughout

### [46:09 - 46:10]

the

### [46:10 - 46:11]

process.

### [46:11 - 46:12]

And

### [46:12 - 46:13]

if

### [46:13 - 46:14]

you

### [46:14 - 46:15]

want

### [46:15 - 46:16]

to

### [46:16 - 46:17]

apply

### [46:17 - 46:18]

these

### [46:18 - 46:19]

modules

### [46:19 - 46:20]

for

### [46:20 - 46:21]

all

### [46:21 - 46:22]

layers,

### [46:22 - 46:23]

they

### [46:23 - 46:24]

can

### [46:24 - 46:25]

also

### [46:25 - 46:26]

help

### [46:26 - 46:27]

you

### [46:27 - 46:28]

to

### [46:28 - 46:29]

keep

### [46:29 - 46:30]

the

### [46:30 - 46:31]

signal

### [46:31 - 46:32]

normalized

### [46:32 - 46:33]

throughout

### [46:33 - 46:34]

the

### [46:34 - 46:35]

process.

### [46:35 - 46:36]

And

### [46:36 - 46:37]

here is

### [46:37 - 46:38]

an example

### [46:38 - 46:39]

of the

### [46:39 - 46:40]

typical

### [46:40 - 46:41]

computations

### [46:41 - 46:42]

that can

### [46:42 - 46:43]

be

### [46:43 - 46:44]

performed

### [46:44 - 46:45]

by a

### [46:45 - 46:46]

normalization

### [46:46 - 46:47]

module.

### [46:47 - 46:48]

And

### [46:48 - 46:49]

usually,

### [46:49 - 46:50]

there

### [46:50 - 46:51]

would be

### [46:51 - 46:52]

three steps

### [46:52 - 46:53]

that's

### [46:53 - 46:54]

involved.

### [46:54 - 46:55]

In

### [46:55 - 46:56]

the

### [46:56 - 46:57]

first

### [46:57 - 46:58]

step,

### [46:58 - 46:59]

we

### [46:59 - 47:00]

may

### [47:00 - 47:01]

want

### [47:01 - 47:02]

to

### [47:02 - 47:03]

reduce

### [47:03 - 47:04]

the

### [47:04 - 47:05]

degree

### [47:05 - 47:06]

of

### [47:06 - 47:07]

freedom

### [47:07 - 47:08]

because

### [47:08 - 47:09]

we

### [47:09 - 47:10]

do

### [47:10 - 47:11]

this

### [47:11 - 47:12]

normalization.

### [47:12 - 47:13]

So,

### [47:13 - 47:14]

we

### [47:14 - 47:15]

may

### [47:15 - 47:16]

want

### [47:16 - 47:17]

to

### [47:17 - 47:18]

compensate

### [47:18 - 47:19]

for

### [47:19 - 47:20]

this

### [47:20 - 47:21]

reduction

### [47:21 - 47:22]

by

### [47:22 - 47:23]

introducing

### [47:23 - 47:24]

another

### [47:24 - 47:25]

linear

### [47:25 - 47:26]

transformation,

### [47:26 - 47:27]

which

### [47:27 - 47:28]

can

### [47:28 - 47:29]

simply

### [47:29 - 47:30]

be

### [47:30 - 47:31]

done

### [47:31 - 47:32]

in

### [47:32 - 47:33]

the

### [47:33 - 47:34]

neural

### [47:34 - 47:35]

network

### [47:35 - 47:36]

architectures.

### [47:36 - 47:37]

In

### [47:37 - 47:38]

practice,

### [47:38 - 47:39]

there

### [47:39 - 47:40]

are

### [47:40 - 47:41]

many

### [47:41 - 47:42]

types

### [47:42 - 47:43]

of

### [47:43 - 47:44]

normalization

### [47:44 - 47:45]

modules,

### [47:45 - 47:46]

and

### [47:46 - 47:47]

one

### [47:47 - 47:48]

of

### [47:48 - 47:49]

the

### [47:49 - 47:50]

differences

### [47:50 - 47:51]

between

### [47:51 - 47:52]

these

### [47:52 - 47:53]

modules

### [47:53 - 47:54]

is

### [47:54 - 47:55]

about

### [47:55 - 47:56]

the

### [47:56 - 47:57]

support

### [47:57 - 47:58]

set

### [47:58 - 47:59]

in

### [47:59 - 48:00]

the

### [48:00 - 48:01]

neural network.

### [48:01 - 48:02]

The

### [48:02 - 48:03]

support

### [48:03 - 48:04]

set

### [48:04 - 48:05]

is

### [48:05 - 48:06]

the

### [48:06 - 48:07]

number

### [48:07 - 48:08]

of

### [48:08 - 48:09]

channels,

### [48:09 - 48:10]

and

### [48:10 - 48:11]

h

### [48:11 - 48:12]

and w

### [48:12 - 48:13]

is

### [48:13 - 48:14]

the

### [48:14 - 48:15]

height

### [48:15 - 48:16]

or

### [48:16 - 48:17]

width,

### [48:17 - 48:18]

which

### [48:18 - 48:19]

is

### [48:19 - 48:20]

the

### [48:20 - 48:21]

spatial

### [48:21 - 48:22]

size.

### [48:22 - 48:23]

And

### [48:23 - 48:24]

this

### [48:24 - 48:25]

operation

### [48:25 - 48:26]

represents

### [48:26 - 48:27]

the

### [48:27 - 48:28]

batch

### [48:28 - 48:29]

of the

### [48:29 - 48:30]

support

### [48:30 - 48:31]

sets.

### [48:31 - 48:32]

And

### [48:32 - 48:33]

today,

### [48:33 - 48:34]

one of

### [48:34 - 48:35]

the most

### [48:35 - 48:36]

popular

### [48:36 - 48:37]

choice

### [48:37 - 48:38]

for

### [48:38 - 48:39]

us

### [48:39 - 48:40]

to

### [48:40 - 48:41]

use,

### [48:41 - 48:42]

or

### [48:42 - 48:43]

perhaps

### [48:43 - 48:44]

the

### [48:44 - 48:45]

default

### [48:45 - 48:46]

choice

### [48:46 - 48:47]

for

### [48:47 - 48:48]

us

### [48:48 - 48:49]

to

### [48:49 - 48:50]

use,

### [48:50 - 48:51]

is

### [48:51 - 48:52]

the

### [48:52 - 48:53]

layer

### [48:53 - 48:54]

normalization

### [48:54 - 48:55]

operation.

### [48:55 - 48:56]

So

### [48:56 - 48:57]

it

### [48:57 - 48:58]

allows

### [48:58 - 48:59]

models

### [48:59 - 49:00]

to

### [49:00 - 49:01]

start

### [49:01 - 49:02]

training,

### [49:02 - 49:03]

otherwise

### [49:03 - 49:04]

they will

### [49:04 - 49:05]

just stop

### [49:05 - 49:06]

training or

### [49:06 - 49:07]

they will

### [49:07 - 49:08]

just diverge

### [49:08 - 49:09]

at the

### [49:09 - 49:10]

very

### [49:10 - 49:11]

beginning.

### [49:11 - 49:12]

On

### [49:12 - 49:13]

the

### [49:13 - 49:14]

other

### [49:14 - 49:15]

hand,

### [49:15 - 49:16]

even

### [49:16 - 49:17]

when

### [49:17 - 49:18]

the

### [49:18 - 49:19]

models

### [49:19 - 49:20]

can

### [49:20 - 49:21]

start

### [49:21 - 49:22]

training,

### [49:22 - 49:23]

the

### [49:23 - 49:24]

introduction

### [49:24 - 49:25]

of

### [49:25 - 49:26]

normalization

### [49:26 - 49:27]

will

### [49:27 - 49:28]

be

### [49:28 - 49:29]

much

### [49:29 - 49:30]

easier.

### [49:30 - 49:31]

So

### [49:31 - 49:32]

let's

### [49:32 - 49:33]

look

### [49:33 - 49:34]

a

### [49:34 - 49:35]

little

### [49:35 - 49:36]

bit

### [49:36 - 49:37]

and

### [49:37 - 49:38]

let's

### [49:38 - 49:39]

record

### [49:39 - 49:40]

what

### [49:40 - 49:41]

is

### [49:41 - 49:42]

the

### [49:42 - 49:43]

key

### [49:43 - 49:44]

idea

### [49:44 - 49:45]

of

### [49:45 - 49:46]

deep

### [49:46 - 49:47]

learning.

### [49:47 - 49:48]

The

### [49:48 - 49:49]

key

### [49:49 - 49:50]

idea

### [49:50 - 49:51]

is

### [49:51 - 49:52]

to

### [49:52 - 49:53]

compose

### [49:53 - 49:54]

a

### [49:54 - 49:55]

simple

### [49:55 - 49:56]

neural

### [49:56 - 49:57]

network

### [49:57 - 49:58]

with

### [49:58 - 49:59]

hundreds

### [49:59 - 50:00]

of

### [50:00 - 50:01]

layers

### [50:01 - 50:02]

to

### [50:02 - 50:03]

train

### [50:03 - 50:04]

from

### [50:04 - 50:05]

scratch

### [50:05 - 50:06]

and

### [50:06 - 50:07]

to

### [50:07 - 50:08]

adapt

### [50:08 - 50:09]

to

### [50:09 - 50:10]

the

### [50:10 - 50:11]

environment.

### [50:11 - 50:12]

So

### [50:12 - 50:13]

in

### [50:13 - 50:14]

this

### [50:14 - 50:15]

work

### [50:15 - 50:16]

of

### [50:16 - 50:17]

residual

### [50:17 - 50:18]

learning,

### [50:18 - 50:19]

we

### [50:19 - 50:20]

demonstrated

### [50:20 - 50:21]

that

### [50:21 - 50:22]

deep

### [50:22 - 50:23]

learning

### [50:23 - 50:24]

or

### [50:24 - 50:25]

neural

### [50:25 - 50:26]

learning

### [50:26 - 50:27]

can

### [50:27 - 50:28]

be

### [50:28 - 50:29]

used

### [50:29 - 50:30]

to

### [50:30 - 50:31]

train

### [50:31 - 50:32]

neural

### [50:32 - 50:33]

networks

### [50:33 - 50:34]

from

### [50:34 - 50:35]

scratch

### [50:35 - 50:36]

and to

### [50:36 - 50:37]

achieve

### [50:37 - 50:38]

better

### [50:38 - 50:39]

accuracy.

### [50:39 - 50:40]

And

### [50:40 - 50:41]

next

### [50:41 - 50:42]

I'm

### [50:42 - 50:43]

going to

### [50:43 - 50:44]

tell a

### [50:44 - 50:45]

little

### [50:45 - 50:46]

bit

### [50:46 - 50:47]

about

### [50:47 - 50:48]

the

### [50:48 - 50:49]

ResNet

### [50:49 - 50:50]

story.

### [50:50 - 50:51]

The

### [50:51 - 50:52]

ResNet

### [50:52 - 50:53]

was

### [50:53 - 50:54]

developed

### [50:54 - 50:55]

in

### [50:55 - 50:56]

the

### [50:56 - 50:57]

early

### [50:57 - 50:58]

20th

### [50:58 - 50:59]

century

### [50:59 - 51:00]

in

### [51:00 - 51:01]

the

### [51:01 - 51:02]

late

### [51:02 - 51:03]

20th

### [51:03 - 51:04]

century.

### [51:04 - 51:05]

The

### [51:05 - 51:06]

ResNet

### [51:06 - 51:07]

was

### [51:07 - 51:08]

developed

### [51:08 - 51:09]

in

### [51:09 - 51:10]

the

### [51:10 - 51:11]

early

### [51:11 - 51:12]

20th

### [51:12 - 51:13]

century

### [51:13 - 51:14]

and

### [51:14 - 51:15]

the

### [51:15 - 51:16]

ResNet

### [51:16 - 51:17]

was

### [51:17 - 51:18]

developed

### [51:18 - 51:19]

in

### [51:19 - 51:20]

the

### [51:20 - 51:21]

early

### [51:21 - 51:22]

20th

### [51:22 - 51:23]

century.

### [51:23 - 51:24]

The

### [51:24 - 51:25]

ResNet

### [51:25 - 51:26]

was

### [51:26 - 51:27]

developed

### [51:27 - 51:28]

in

### [51:28 - 51:29]

the

### [51:29 - 51:30]

early

### [51:30 - 51:31]

20th

### [51:31 - 51:32]

century.

### [51:32 - 51:33]

And

### [51:33 - 51:34]

the

### [51:34 - 51:35]

ResNet

### [51:35 - 51:36]

was

### [51:36 - 51:37]

developed

### [51:37 - 51:38]

in

### [51:38 - 51:39]

the

### [51:39 - 51:40]

early

### [51:40 - 51:41]

20th

### [51:41 - 51:42]

century.

### [51:42 - 51:43]

And

### [51:43 - 51:44]

the

### [51:44 - 51:45]

ResNet

### [51:45 - 51:46]

was

### [51:46 - 51:47]

developed

### [51:47 - 51:48]

in

### [51:48 - 51:49]

the

### [51:49 - 51:50]

early

### [51:50 - 51:51]

20th

### [51:51 - 51:52]

century.

### [51:52 - 51:53]

And

### [51:53 - 51:54]

the

### [51:54 - 51:55]

ResNet

### [51:55 - 51:56]

was

### [51:56 - 51:57]

developed

### [51:57 - 51:58]

in

### [51:58 - 51:59]

the

### [51:59 - 52:00]

early

### [52:00 - 52:01]

20th

### [52:01 - 52:02]

century.

### [52:02 - 52:03]

The

### [52:03 - 52:04]

ResNet

### [52:04 - 52:05]

was

### [52:05 - 52:06]

developed

### [52:06 - 52:07]

in

### [52:07 - 52:08]

the

### [52:08 - 52:09]

early

### [52:09 - 52:10]

20th

### [52:10 - 52:11]

century.

### [52:11 - 52:12]

And

### [52:12 - 52:13]

the

### [52:13 - 52:14]

ResNet

### [52:14 - 52:15]

was

### [52:15 - 52:16]

developed

### [52:16 - 52:17]

in

### [52:17 - 52:18]

the

### [52:18 - 52:19]

early

### [52:19 - 52:20]

20th

### [52:20 - 52:26]

suggests that each at least has the same training accuracy as some of the

### [52:26 - 52:32]

shallower counterparts. So the empirical observation of degradation suggests that

### [52:32 - 52:38]

the optimization may not be able to find this solution or the optimization may

### [52:38 - 52:43]

not be able to find a solution that's similar enough to this one. And this

### [52:43 - 52:49]

motivate us to develop a framework which is called deep residual learning. And

### [52:49 - 52:54]

again here, let's zoom out a bit and let's think of a very deep neural

### [52:54 - 52:59]

neural architecture, and then let's focus on a small subnet inside of narrative

### [52:59 - 53:03]

neural neural architecture, and in this illustration this small subnet has only

### [53:03 - 53:10]

two layers in this case. And then we use a function h to denote the

### [53:10 - 53:17]

underlying desired function that is to be fit by this small subnet. Then in the

### [53:17 - 53:18]

case of a classical

### [53:18 - 53:18]

that is to be fit by this small subnet. Then in the case of a classical

### [53:18 - 53:19]

To denote the underlying desired function that is to be fit by this small subnet. Then in the case of a classical

### [53:19 - 53:25]

vanilla neural network, the only thing we can do is that we hope these two layers can fit this

### [53:25 - 53:34]

underlying function of HX. Then, the idea of residual learning is different. We don't need to

### [53:34 - 53:42]

use this weight layer to directly fit this function HX. Instead, we may want them to fit

### [53:42 - 53:48]

another function, which is FX, and this function will represent the delta or the change that we

### [53:48 - 53:55]

can make on top of the input to this small subnet. In order to have the original decided function,

### [53:55 - 54:03]

we just need to add the FX into the input of this subnet, and this addition can be easily

### [54:03 - 54:10]

achieved as an identity mapping, which connects the input of this subnet to the output of this

### [54:10 - 54:16]

subnet, and the signal will be merged by element-wise and addition. This will also turn

### [54:16 - 54:18]

this subnet into a neural network, and this will also turn this subnet into a neural network.

### [54:18 - 54:28]

In this residual block, the weight layers will perform a function which is called a residual

### [54:28 - 54:33]

function. Basically, the residual function is just incremental changes on top of the input.

### [54:34 - 54:41]

Now, let's think of the entire residual block as a function that we want to use. If the identity

### [54:41 - 54:48]

mapping is optimal for this function, then it should be easy for us to achieve it because we can

### [54:48 - 54:57]

set all the weight layers as zero. And if identity mapping is almost optimal, then we may also be

### [54:57 - 55:03]

able to have a good solution because we can set the weight as some small numbers. In this sense,

### [55:03 - 55:10]

actually, the idea of residual learning encourages a building block to make small and conservative

### [55:10 - 55:18]

and incremental changes. However, by putting many small changes together, it is still possible for us to have a

### [55:18 - 55:24]

to learn a very complex function, and this also follows the deep learning methodology.

### [55:25 - 55:26]

And again,

### [55:26 - 55:32]

as a byproduct of the introduction of the residual block, it is easy for us to have another initialization method.

### [55:32 - 55:37]

and we can just set the weight as some small numbers or set them as zero at the beginning of training.

### [55:37 - 55:43]

This is to say, the entire residual block will just be identity mapping, or similar to an identity mapping, at the beginning of training.

### [55:43 - 55:46]

this is to say, the entire residual block will just be identity mapping, or similar to an identity mapping, at the beginning of training.

### [55:46 - 55:52]

So the signal in the forward process and also in the in the backward process can be easily

### [55:53 - 55:55]

propagated

### [55:55 - 56:01]

with this identity mapping at the beginning of training. So you don't need to worry too much about the initialization algorithm.

### [56:04 - 56:09]

Then it is easy for us to adopt this idea to build a very deep neural network architecture.

### [56:10 - 56:13]

So in some sense you may just need to add this many

### [56:13 - 56:18]

identity connections into a vanilla neural network, then you can turn it into a residual neural net. Or

### [56:19 - 56:26]

equivalently this can be thought of as simply stacking many residual blocks to create a very deep model.

### [56:27 - 56:28]

So in this sense

### [56:28 - 56:32]

the introduction or the design of a residual block

### [56:32 - 56:39]

actually becomes the new generic design or the new generic modules for us to build a very deep neural network architectures.

### [56:40 - 56:42]

So after the introduction of

### [56:42 - 56:43]

ResNet

### [56:43 - 56:49]

people started to focus on a design of every single building blocks and perhaps one of the most successful

### [56:49 - 56:57]

design is the transformer block. And then after that you just need to stack the same type of block for many times and you don't

### [56:57 - 57:01]

need to carefully design every single specific layers when you have many more layers.

### [57:03 - 57:04]

And

### [57:04 - 57:06]

then here are just some results

### [57:06 - 57:12]

about ResNet. In this figure the x-axis is the depth of neural network and the

### [57:12 - 57:13]

y-axis is the

### [57:13 - 57:20]

classification accuracy. And this figure basically says a vanilla neural network will start to degrade very quickly

### [57:20 - 57:25]

after 20 layers, for example, and ResNet can keep improving after many layers.

### [57:26 - 57:34]

And the same pattern can happen on ImageNet and many other datasets, and this pattern can be summarized in this form.

### [57:34 - 57:36]

So without the help of residual connections

### [57:36 - 57:41]

the neural network will start to degrade after a certain point depending on the scenarios. And

### [57:41 - 57:48]

With the help of residual connections, it can keep improving and when you add more and more layers, and this is highly desired property.

### [57:50 - 57:58]

Here is a checklist of the several things that you may do to build and train very deep neural network architectures.

### [57:58 - 58:03]

And many of these concepts are just about how we can have a healthy signal propagation

### [58:03 - 58:07]

in the training process. And this aspect includes the usage of a

### [58:07 - 58:14]

Rear-look activation or other activations of a similar shape and also the usage of an appropriate initialization algorithm.

### [58:14 - 58:22]

And it also includes the introduction of normalization modules and residual connections into your neural neural architectures.

### [58:26 - 58:28]

Good, I have talked about

### [58:28 - 58:33]

learning deep representations with convolutional neural networks for 2D images.

### [58:33 - 58:36]

The next I will also briefly talk about how can we learn deep

### [58:37 - 58:37]

representations

### [58:37 - 58:39]

from 1D sequences.

### [58:41 - 58:45]

A classical model for us to do 1D sequence modeling is

### [58:46 - 58:49]

recurrent neural networks or in short RNN.

### [58:50 - 58:54]

A recurrent neural network is a very special kind of neural network

### [58:55 - 58:57]

which has loops in its connections.

### [58:57 - 59:05]

So that is to say, given a recurrent neural network unit, it will take the input from the current time step,

### [59:05 - 59:07]

let's say Xt, and then it will produce

### [59:07 - 59:17]

a hidden state given that input, for example, Ht, and this hidden state will be used to determine the output at that time step.

### [59:17 - 59:23]

And this hidden state will also be used as the input to the next time step.

### [59:23 - 59:29]

And if we unfold this recurrent neural network architecture along the time axis,

### [59:29 - 59:34]

we can see that it is actually yet another way to sharing model

### [59:35 - 59:37]

with the weight shared.

### [59:37 - 59:38]

yelling

### [59:38 - 59:39]

across the temporal dimensions.

### [59:39 - 59:46]

So, and also, this architecture is also a locally connected formulation.

### [59:47 - 59:53]

For example, for every single unit, it is only connected to the input of this time step.

### [59:53 - 59:58]

And it is also connected to the immediate previous time step.

### [59:58 - 01:00:07]

So, again, we see that weight sharing and local connections are still two of the key properties in a recurrent neural

### [01:00:07 - 01:00:07]

network.

### [01:00:07 - 01:00:07]

So, again, we see that weight sharing and local connections are still two of the key properties in a recurrent neural network.

### [01:00:07 - 01:00:07]

is often used in recurrent neural network.

### [01:00:07 - 01:00:15]

design and this is conceptually very similar to a convolutional neural network and how can we build

### [01:00:15 - 01:00:22]

a deep recurrent neural network and it also turns out to be very simple in some sense you just need

### [01:00:22 - 01:00:28]

to view the state from a recurrent neural network unit as a new sequence and then you can process

### [01:00:28 - 01:00:34]

this sequence by using another unit so that is to say you can just stack many recurring

### [01:00:34 - 01:00:38]

new recurrent neural network units together and you will have a different neural network

### [01:00:39 - 01:00:44]

for example here i show the case of a three layer recurrent neural network

### [01:00:44 - 01:00:51]

and in this case if we consider on the output of of this neuron it will depend on the output

### [01:00:51 - 01:00:57]

of all the shallower layers and it will also depend on all the previous time steps

### [01:00:58 - 01:01:03]

in the same layer and this is just a property of recurrent neural neural architectures

### [01:01:05 - 01:01:11]

and here is an example of of deep recurrent neural networks in practice this example is

### [01:01:11 - 01:01:18]

from google's neural machine translation system that was developed for their products in 2016.

### [01:01:18 - 01:01:25]

in this case they stack several lstm units to make this deep recurrent neural network

### [01:01:25 - 01:01:34]

and lstm is just a special form of a very effective form of irns in this workbook

### [01:01:34 - 01:01:41]

the author reported that in order to build this very deep lstm model they still need to use the

### [01:01:41 - 01:01:47]

residual connections they report that with the help of residual connections they can train a

### [01:01:47 - 01:01:53]

deep lstm with up to 16 layers and enjoy the benefits of going deeper and if they don't use

### [01:01:53 - 01:01:58]

the residual connections they observe the degradation problem just after four layers

### [01:01:58 - 01:02:04]

so interestingly this observation is very similar to the observation we made on convolutional neural

### [01:02:04 - 01:02:11]

networks and again this demonstrates the power and the generality of the deep learning methodology

### [01:02:11 - 01:02:19]

that is to say if we develop a very effective and very general component from one application

### [01:02:19 - 01:02:26]

then it is likely that you are going to enjoy the benefit in some other applications so in this case

### [01:02:26 - 01:02:31]

the original residual connection was developed in the scenario of convolutional neural network

### [01:02:31 - 01:02:33]

for 2d image processing

### [01:02:34 - 01:02:39]

but its behavior can also be observed in a completely different scenario

### [01:02:39 - 01:02:42]

with recurrent neural networks for 1d sequence modeling

### [01:02:46 - 01:02:52]

then recurrent neural network is not the only way for us to model 1d sequences

### [01:02:52 - 01:02:57]

we can still use the classical convolutional neural network to achieve more or less the same goal

### [01:02:57 - 01:03:03]

we just need to apply a sliding window across the 1d dimension and then we can perform a

### [01:03:04 - 01:03:12]

convolution on the 1d sequences and if we want to have some causal reasoning we may want to make

### [01:03:12 - 01:03:18]

a small change here which is we we may want to make the convolution to perform some causal

### [01:03:18 - 01:03:25]

computation that is to say for the kernel for the convolutional kernel it can only see the current

### [01:03:25 - 01:03:30]

time step or any of the previous time step it is not going to see any of the future time steps

### [01:03:32 - 01:03:34]

then in the case of a convolutional neural

### [01:03:34 - 01:03:41]

network the limitation is very obvious that is to say if you want to capture a longer context

### [01:03:41 - 01:03:46]

you need to be built a different neural network architecture this is because for every single

### [01:03:46 - 01:03:52]

layer the context lens will be limited by the kernel size for example in this case for this

### [01:03:52 - 01:03:58]

neuron its context only depends on the current time step and the immediate previous time step

### [01:03:58 - 01:04:03]

so in order to have a longer context for example in this case you may want to have more layers and

### [01:04:04 - 01:04:13]

more time steps for example this neuron will depend on up to three time steps away and this is how

### [01:04:13 - 01:04:18]

you can have a longer context when we use convolutional neural networks for sequence modeling

### [01:04:19 - 01:04:24]

and next i'm going to discuss yet another concrete example this example is from deep

### [01:04:24 - 01:04:30]

mines wave net architecture and the application here is for audio generation in this case they

### [01:04:30 - 01:04:34]

not only use the causal convolution but they also are

### [01:04:34 - 01:04:37]

and another operation, which is called a dilation.

### [01:04:37 - 01:04:43]

So a dilated convolution means the convolutional kernel

### [01:04:43 - 01:04:47]

does not need to depend on the immediate previous step.

### [01:04:47 - 01:04:50]

It can depend on a time step that

### [01:04:50 - 01:04:52]

can be many time steps away.

### [01:04:52 - 01:04:54]

Then the dilation operation can help

### [01:04:54 - 01:04:59]

us to greatly increase the size of the convolutional kernel,

### [01:04:59 - 01:05:02]

and it can help us to capture a longer context.

### [01:05:02 - 01:05:04]

But even so, the authors still need

### [01:05:04 - 01:05:07]

to stack many convolutional layers

### [01:05:07 - 01:05:10]

to build a very deep convolutional neural network

### [01:05:10 - 01:05:11]

to capture long context.

### [01:05:11 - 01:05:14]

And as such, they still need the help

### [01:05:14 - 01:05:19]

from the residual connections for them

### [01:05:19 - 01:05:20]

to enjoy the benefits of training

### [01:05:20 - 01:05:24]

deeper neural networks.

### [01:05:24 - 01:05:27]

And here is a summary of different sequence modeling

### [01:05:27 - 01:05:32]

paradigms conceptually.

### [01:05:32 - 01:05:32]

In the case of a convolutional kernel,

### [01:05:32 - 01:05:35]

we have a recurrent neural network.

### [01:05:35 - 01:05:39]

For every single layer and for every single time step,

### [01:05:39 - 01:05:41]

it can see the full context.

### [01:05:41 - 01:05:46]

That is to say, if we consider this neuron,

### [01:05:46 - 01:05:49]

its computation will depend on the computations

### [01:05:49 - 01:05:52]

of all the previous time steps in the same layer.

### [01:05:52 - 01:05:54]

And this could be a decided property

### [01:05:54 - 01:05:59]

if you want some long range reasoning in your application.

### [01:05:59 - 01:06:02]

However, on the other hand, also because

### [01:06:02 - 01:06:05]

of this property, the computation of recurrent neural

### [01:06:05 - 01:06:08]

network is not feed forward.

### [01:06:08 - 01:06:10]

That is to say, in order to compute

### [01:06:10 - 01:06:12]

the outputs of this neuron, you need

### [01:06:12 - 01:06:17]

to wait the outputs of all the previous neuron to be finished.

### [01:06:17 - 01:06:22]

So this behavior is not friendly to parallel implementation

### [01:06:22 - 01:06:23]

in GPUs.

### [01:06:23 - 01:06:25]

So in practice, the recurrent neural networks

### [01:06:25 - 01:06:30]

are not efficient in GPU implementation.

### [01:06:30 - 01:06:32]

As a comparison, the convolutional neural

### [01:06:32 - 01:06:35]

network had completely different behavior.

### [01:06:35 - 01:06:38]

On one hand, the model is fully feed forward.

### [01:06:38 - 01:06:41]

So for every single neuron in the same layer,

### [01:06:41 - 01:06:43]

you don't need to wait for the other neurons

### [01:06:43 - 01:06:45]

to finish their computation.

### [01:06:45 - 01:06:48]

So this is very friendly to parallel implementation

### [01:06:48 - 01:06:49]

in GPUs.

### [01:06:49 - 01:06:52]

So usually, the convolutional neural networks

### [01:06:52 - 01:06:55]

are very efficient in GPU implementation.

### [01:06:55 - 01:06:58]

On the other hand, as we have discussed,

### [01:06:58 - 01:07:02]

the context length would be limited by the size

### [01:07:02 - 01:07:03]

of the convolutional kernels.

### [01:07:03 - 01:07:07]

And this is not a decided property.

### [01:07:07 - 01:07:10]

How can we enjoy the best of both worlds?

### [01:07:10 - 01:07:15]

And this is why the attentional mechanism has been introduced.

### [01:07:15 - 01:07:19]

Simply speaking, in the attentional mechanism,

### [01:07:19 - 01:07:25]

we allowed every single neuron or every single time step

### [01:07:25 - 01:07:30]

to see every single other time step in the sequence.

### [01:07:30 - 01:07:32]

So as such.

### [01:07:32 - 01:07:35]

And for every single neuron, it will

### [01:07:35 - 01:07:39]

be able to see the full context from the previous layer.

### [01:07:39 - 01:07:44]

So if modeling a long range reasoning is what you want,

### [01:07:44 - 01:07:47]

then this is a decided property in the neural neural

### [01:07:47 - 01:07:48]

architectures.

### [01:07:48 - 01:07:51]

On the other hand, in the attentional mechanism,

### [01:07:51 - 01:07:54]

all computations are feed forward.

### [01:07:54 - 01:07:56]

So you don't need to wait.

### [01:07:56 - 01:07:58]

You don't need to wait the computation

### [01:07:58 - 01:08:01]

of the previous time step at the same layer to finish.

### [01:08:01 - 01:08:06]

So this feed forward computation is also very friendly to GPU implementation.

### [01:08:09 - 01:08:13]

The attentional mechanism is a core idea

### [01:08:13 - 01:08:16]

behind a very popular architecture, which

### [01:08:16 - 01:08:18]

is known as the transformers.

### [01:08:18 - 01:08:20]

Because time is limited, I'm not going

### [01:08:20 - 01:08:23]

to delve into the technical details of the transformers.

### [01:08:23 - 01:08:28]

But I'm going to share some of the intriguing properties

### [01:08:28 - 01:08:29]

of the transformers design.

### [01:08:31 - 01:08:34]

The first property is that, in the transformers,

### [01:08:34 - 01:08:37]

we allow every single node to see every single other node,

### [01:08:37 - 01:08:40]

as what we have discussed.

### [01:08:40 - 01:08:42]

Another interesting property, which

### [01:08:42 - 01:08:45]

to the surprise of many practitioners,

### [01:08:45 - 01:08:51]

is that, actually, the attention computation is parameter-free.

### [01:08:51 - 01:08:54]

So you don't need to introduce any parameters.

### [01:08:54 - 01:08:58]

That is to say, if you are given three sequences, let's say,

### [01:08:58 - 01:09:01]

q, k, v, which is short for queries, keys, and values.

### [01:09:01 - 01:09:01]

Let's say, qkv, which is short for queries, keys, and values.

### [01:09:01 - 01:09:08]

then the attention computation does not need to introduce any trainable parameters.

### [01:09:08 - 01:09:12]

So this is unlike a classical fully connected layer

### [01:09:12 - 01:09:16]

where every single connection may represent a trainable parameter.

### [01:09:17 - 01:09:19]

In the case of the attentional computation,

### [01:09:19 - 01:09:21]

in this attentional computation,

### [01:09:21 - 01:09:25]

every single connection represents no trainable parameter.

### [01:09:25 - 01:09:29]

It just means these two things are related to each other.

### [01:09:29 - 01:09:33]

So if the attentional computation is parameter-free,

### [01:09:34 - 01:09:35]

then where are the parameters?

### [01:09:36 - 01:09:38]

So interestingly, in the transformer architecture,

### [01:09:39 - 01:09:42]

all the parameter layers are feed-forward.

### [01:09:43 - 01:09:47]

The parameter layers will be used for us to obtain the sequences

### [01:09:47 - 01:09:49]

that are called QKV,

### [01:09:50 - 01:09:52]

and they will also be used in the MLP blocks

### [01:09:52 - 01:09:58]

that is to transform these sequences in the representation space.

### [01:09:59 - 01:10:02]

And in some sense, all these parameter layers

### [01:10:02 - 01:10:05]

are just kind of one-by-one convolutional layers.

### [01:10:05 - 01:10:08]

And again, all these layers are locally connected

### [01:10:08 - 01:10:12]

because they are only connected to the current time step,

### [01:10:12 - 01:10:17]

and all these layers have weight-sharing across the time dimension.

### [01:10:18 - 01:10:21]

And again, we can see that local connection and weight-sharing

### [01:10:21 - 01:10:25]

are still the two key properties in neural network architectures.

### [01:10:26 - 01:10:28]

And also, the transformer architecture,

### [01:10:29 - 01:10:30]

it's a very deep model,

### [01:10:30 - 01:10:34]

so we need to rely on a certain type of normalization operations

### [01:10:34 - 01:10:36]

and also the residual connections

### [01:10:36 - 01:10:39]

for us to train these very deep models.

### [01:10:41 - 01:10:43]

There are many successful applications

### [01:10:43 - 01:10:45]

of the transformer architectures,

### [01:10:46 - 01:10:49]

and perhaps the most popular and most famous one

### [01:10:49 - 01:10:52]

is the generative pre-trained transformers,

### [01:10:53 - 01:10:54]

or in short, GPT.

### [01:10:55 - 01:10:58]

Simply speaking, the GPT model

### [01:10:58 - 01:10:59]

is a very deep model,

### [01:10:59 - 01:11:00]

the representation learning model

### [01:11:00 - 01:11:02]

for natural language processing.

### [01:11:02 - 01:11:05]

The GPT models are designed for a task

### [01:11:05 - 01:11:07]

which is known as next-word prediction.

### [01:11:08 - 01:11:13]

In this task, the model is given a prefix of a sentence,

### [01:11:13 - 01:11:16]

and it is asked to predict what would be the next word

### [01:11:16 - 01:11:17]

after this prefix.

### [01:11:18 - 01:11:20]

In this case, the sentence could be, for example,

### [01:11:21 - 01:11:22]

the students opened their something,

### [01:11:23 - 01:11:25]

and the model is asked to predict something,

### [01:11:25 - 01:11:27]

and with some probability,

### [01:11:28 - 01:11:29]

the models may say,

### [01:11:29 - 01:11:29]

book.

### [01:11:30 - 01:11:32]

And this model, the GPT model,

### [01:11:33 - 01:11:35]

is trained on a larger scale data set

### [01:11:35 - 01:11:37]

collected from the internet.

### [01:11:37 - 01:11:40]

So it is able to learn very good representations

### [01:11:40 - 01:11:41]

about the natural languages.

### [01:11:42 - 01:11:44]

It is also going to learn the knowledge

### [01:11:44 - 01:11:47]

that is contained in this language data.

### [01:11:48 - 01:11:50]

And the GPT model

### [01:11:50 - 01:11:56]

is the foundation behind many of the language applications,

### [01:11:56 - 01:11:58]

including chat GPT.

### [01:11:59 - 01:12:01]

And actually, in order to enjoy the benefit,

### [01:12:01 - 01:12:04]

we still need to rely on the transfer learning paradigm.

### [01:12:04 - 01:12:07]

That is to say, we pre-train this model on larger scale data,

### [01:12:07 - 01:12:10]

then we need to fine-tune or transfer this model

### [01:12:10 - 01:12:12]

in some smaller scale data sets.

### [01:12:15 - 01:12:18]

Another successful application of transformers

### [01:12:18 - 01:12:21]

is the alpha-fold application.

### [01:12:21 - 01:12:25]

And simply speaking, alpha-fold is a representation learning

### [01:12:25 - 01:12:28]

method for the application of protein folding.

### [01:12:28 - 01:12:32]

In this case, the input to the neural neural architecture

### [01:12:32 - 01:12:35]

is amino acid sequences.

### [01:12:35 - 01:12:37]

And the outputs of the architecture

### [01:12:37 - 01:12:39]

are just the protein structures.

### [01:12:39 - 01:12:42]

And this architecture has 48 transformer blocks,

### [01:12:42 - 01:12:44]

and the architecture would be trained

### [01:12:44 - 01:12:47]

on a larger scale protein structure data set

### [01:12:47 - 01:12:50]

that has been collected by human experiments

### [01:12:50 - 01:12:52]

over the last several decades.

### [01:12:52 - 01:12:57]

And interestingly, even though many of these components,

### [01:12:57 - 01:12:58]

such as the transformers,

### [01:12:58 - 01:13:01]

the transformer block, or the usage of residual connections,

### [01:13:01 - 01:13:04]

were originally developed for many other applications,

### [01:13:04 - 01:13:09]

such as natural language processing or image recognition,

### [01:13:09 - 01:13:12]

this exact same set of building blocks

### [01:13:12 - 01:13:15]

can be applied to a completely different problem

### [01:13:15 - 01:13:17]

of protein folding.

### [01:13:17 - 01:13:20]

And again, this demonstrates the generality

### [01:13:20 - 01:13:22]

of the deep learning methodology.

### [01:13:22 - 01:13:26]

If you develop a very effective set of tools,

### [01:13:26 - 01:13:28]

then you may be able to enjoy

### [01:13:28 - 01:13:30]

the benefits of these tools, perhaps

### [01:13:30 - 01:13:32]

in completely different areas.

### [01:13:35 - 01:13:38]

Then we are ready to go back to computer vision,

### [01:13:38 - 01:13:43]

and we're going to introduce another very successful work,

### [01:13:43 - 01:13:46]

which is called the Vision Transformer, or VIT.

### [01:13:46 - 01:13:51]

So conceptually, VIT is just the application of transformers

### [01:13:51 - 01:13:53]

to 2D image processing.

### [01:13:53 - 01:13:56]

And it turns out that the idea can be very simple.

### [01:13:56 - 01:13:58]

We just need to prepare.

### [01:13:58 - 01:14:02]

An input image as a sequence of non-overlapping patches.

### [01:14:02 - 01:14:04]

Then we can apply the transformer architecture

### [01:14:04 - 01:14:11]

on this 1D sequence as if it is whatever any other 1D sequences.

### [01:14:11 - 01:14:13]

And it turns out that this simple idea

### [01:14:13 - 01:14:16]

is very successful and very effective.

### [01:14:16 - 01:14:18]

And today, it is one of the default choice

### [01:14:18 - 01:14:22]

for us to do image recognition in computer vision.

### [01:14:22 - 01:14:24]

And the significance of the VIT architecture

### [01:14:24 - 01:14:27]

is not just within computer vision, because, for the first,

### [01:14:27 - 01:14:28]

VIT is not just within computer vision, because, for the first,

### [01:14:28 - 01:14:28]

VIT is not just within computer vision, because, for the first,

### [01:14:28 - 01:14:32]

it demonstrated that the transformer architecture

### [01:14:32 - 01:14:35]

can be a unified architecture for many problems,

### [01:14:35 - 01:14:39]

including natural language processing, computer vision,

### [01:14:39 - 01:14:41]

or audio recognition, or 3D processing,

### [01:14:41 - 01:14:44]

and many other sequence processing problems.

### [01:14:44 - 01:14:47]

And again, it demonstrates the generality

### [01:14:47 - 01:14:49]

of the deep learning methodology.

### [01:14:51 - 01:14:55]

Now, here is a conclusion of this tutorial,

### [01:14:55 - 01:14:58]

and this would be some takeaways from this part.

### [01:14:58 - 01:15:01]

And in this tutorial, I have introduced

### [01:15:01 - 01:15:03]

what is representation learning and why

### [01:15:03 - 01:15:05]

it is an important problem.

### [01:15:05 - 01:15:07]

Representation learning can be a common problem

### [01:15:07 - 01:15:11]

and that we may have across different areas

### [01:15:11 - 01:15:13]

and for different applications.

### [01:15:13 - 01:15:15]

And deep learning and deep neural networks

### [01:15:15 - 01:15:17]

are just very effective tools for us

### [01:15:17 - 01:15:21]

to address the representation learning problem.

### [01:15:21 - 01:15:25]

And again, the key idea of deep learning

### [01:15:25 - 01:15:27]

is to compose a simple set of generic models,

### [01:15:27 - 01:15:31]

or generic modules, into highly complex functions.

### [01:15:31 - 01:15:35]

And the deep learning idea can provide us general tools

### [01:15:35 - 01:15:37]

to address different problems in different areas,

### [01:15:37 - 01:15:40]

and I hope you will be able to use these tools

### [01:15:40 - 01:15:42]

in your areas in the future.

### [01:15:42 - 01:15:44]

And that's it for this part.
