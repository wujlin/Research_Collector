# Yann LeCun's $1B Bet Against LLMs

- URL: https://www.youtube.com/watch?v=kYkIdXwW2AE
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-05T13:26:13`

## Transcript

### [00:00 - 00:06]

Okay, let me make a controversial statement that, again, is going to get me a lot of friends in Silicon Valley.

### [00:07 - 00:12]

AI legend Jan LeCun has raised a billion dollars to pursue an alternative approach to AI.

### [00:13 - 00:20]

Unlike large language models, LeCun's approach is not rooted in language and is not generative.

### [00:20 - 00:23]

By design, it does not spit out text, images, or videos.

### [00:24 - 00:26]

Instead, LeCun has proposed JEPA.

### [00:26 - 00:33]

JEPA is not a single AI model, but instead an alternative architecture or framework for training AI models.

### [00:34 - 00:40]

Many successful approaches in AI and machine learning train models to predict some output Y given some input X.

### [00:41 - 00:46]

Large language models are given some input text X and trained to predict the text Y that comes next.

### [00:47 - 00:53]

Image classifier models are given an input image X and trained to predict the corresponding label Y.

### [00:53 - 00:55]

JEPA does not work like this.

### [00:55 - 01:01]

Instead, our inputs X and outputs Y are each passed into models known as encoders.

### [01:01 - 01:06]

These encoders return a vector or matrix of numbers, often referred to as an embedding.

### [01:07 - 01:10]

From here, a third model, known as a predictor,

### [01:10 - 01:14]

is trained to predict the embedding of Y given the embedding of X.

### [01:15 - 01:18]

Why might this be a better way to build AI systems?

### [01:19 - 01:22]

Do you think that JEPA or world model-based approaches,

### [01:22 - 01:25]

do you think they'll replace LLMs one day or are they kind of solving different problems?

### [01:26 - 01:27]

Initially, they'll solve different problems.

### [01:28 - 01:31]

Eventually, they'll replace LLMs, okay?

### [01:31 - 01:35]

Because, you know, LLMs are really good at manipulating language, but basically nothing else.

### [01:36 - 01:43]

They're really good in domains where the language itself is the substrate of reasoning.

### [01:43 - 01:47]

Compared to the mainline, generative, language-driven approach to AI,

### [01:47 - 01:51]

JEPA lives on an alternative path of joint embedding architectures.

### [01:52 - 01:55]

Interestingly, Lacoon played a significant role at the outset of both the

### [01:55 - 02:01]

paths. In part one of this two-part series, we'll explore this alternative path to JEPA.

### [02:02 - 02:05]

We'll dig into why YAN moved away from generative architectures,

### [02:05 - 02:11]

just as they were gaining traction in language, and explore YAN's epiphany for a new solution

### [02:11 - 02:15]

to the representation collapse problem that plagued joint embedding architectures for years.

### [02:16 - 02:19]

Finally, we'll dig into the JEPA architecture itself.

### [02:20 - 02:25]

In part two, we'll dive into JEPA implementations and see exactly how these models stack up against

### [02:25 - 02:26]

LLM-driven approaches.

### [02:31 - 02:34]

YAN Lacoon saw the revolution coming.

### [02:35 - 02:39]

In the 1980s, while most of the AI field was busy building expert systems

### [02:39 - 02:42]

that were explicitly programmed instead of learned from data,

### [02:42 - 02:45]

YAN pioneered the convolutional neural network.

### [02:46 - 02:51]

25 years later, when deep learning began its rise to its now dominant position in AI,

### [02:51 - 02:55]

the breakthrough deep learning model AlexNet turned out to be uncanny.

### [02:55 - 02:59]

It was finally similar to Lacoon's convolutional nets from the 1990s.

### [03:00 - 03:04]

However, as deep learning continued to pick up steam through the 2010s,

### [03:04 - 03:07]

Lacoon and other researchers became increasingly concerned

### [03:07 - 03:11]

by just how much this approach to AI depended on labeled training data.

### [03:12 - 03:16]

AlexNet was trained on the enormous and meticulously labeled ImageNet dataset

### [03:16 - 03:21]

using supervised learning, where AlexNet was trained to match the labels assigned

### [03:21 - 03:23]

to each image by human annotators.

### [03:25 - 03:29]

He was able to learn very general representations for concepts like dog,

### [03:29 - 03:32]

with very few explicitly labeled examples.

### [03:34 - 03:37]

As manually labeled data became a bottleneck for supervised learning,

### [03:37 - 03:40]

interest grew in alternative approaches.

### [03:40 - 03:44]

Reinforcement learning, where models learned from interacting with their environments

### [03:44 - 03:49]

instead of from labeled data, experienced a mini-renaissance in the mid-2010s,

### [03:50 - 03:53]

highlighted by Google DeepMind's breakthrough performance on Atari games

### [03:53 - 03:55]

and the highly complex board game Go.

### [03:56 - 04:00]

Concurrently, Lacoon and others explored unsupervised methods

### [04:00 - 04:05]

that learned from data without labels, including a variant called self-supervised learning,

### [04:05 - 04:07]

where the labels are taken from the data itself.

### [04:08 - 04:13]

Starting in 2015 or so, I started showing a slide that has become a bit of a meme in the

### [04:13 - 04:18]

machine learning community, where I said, like, you know, it's the cake slide, right?

### [04:18 - 04:23]

So if intelligence is a cake, the bulk of the cake is self-supervised learning,

### [04:23 - 04:25]

the icing on the cake, supervised learning.

### [04:25 - 04:30]

And at the time, people were kind of crazy about reinforcement learning,

### [04:30 - 04:33]

so I was trying to tell them, like, this is never going to, you know,

### [04:33 - 04:38]

take us to, you know, anywhere close to human or animal intelligence because it's too inefficient.

### [04:40 - 04:46]

And it turns out the success of self-supervised learning, you know,

### [04:46 - 04:54]

happened in text and language much faster than it did in sort of more, you know, natural,

### [04:55 - 04:57]

modernities like vision.

### [04:57 - 05:02]

Here, Jan is referring to the success of Next Token Prediction for training large language models.

### [05:03 - 05:08]

OpenAI was founded in 2015 and initially focused their efforts on reinforcement learning,

### [05:08 - 05:14]

creating OpenAI Gym and Universe, and showing very impressive performance on complex video games.

### [05:15 - 05:20]

While much of the company was focused on reinforcement learning, Ilya Sutskever,

### [05:20 - 05:24]

Alec Radford, and others became interested in a new neural network architecture from Google,

### [05:24 - 05:25]

the Transformer.

### [05:25 - 05:27]

Initially designed for language translation.

### [05:29 - 05:32]

While experimenting, Radford tried an interesting modification.

### [05:32 - 05:38]

Instead of having the Transformer translate from a block of text in one language to a block of text in another language,

### [05:38 - 05:44]

he switched to a simpler, self-supervised approach, where training text is broken into sequences,

### [05:44 - 05:50]

and the Transformer is given all but the last little piece of text, known as a token, in each sequence,

### [05:50 - 05:53]

and trained to predict what this final token will be.

### [05:53 - 06:01]

Radford and his OpenAI colleagues trained their Transformer on a fairly large internal OpenAI data set of 7,000 books,

### [06:01 - 06:04]

note that we now call this phase pre-training,

### [06:04 - 06:10]

and then further trained their model using standard supervised learning from human-generated labels on specific language tasks.

### [06:10 - 06:18]

Their two-stage training approach worked well, setting new state-of-the-art results on nine language benchmarks,

### [06:18 - 06:21]

including tasks like high school-level reading comprehension questions,

### [06:21 - 06:21]

and more.

### [06:21 - 06:22]

For example,

### [06:22 - 06:22]

The first question is,

### [06:23 - 06:28]

Outperforming architectures and methods that were individually designed and trained for each individual task.

### [06:30 - 06:35]

Radford's model is now known as Generative Pre-trained Transformer 1, or GPT-1.

### [06:36 - 06:41]

GPT-1 didn't receive much public attention at the time, but was a huge unlock,

### [06:41 - 06:45]

breaking models free from their dependence on human-labeled data,

### [06:45 - 06:47]

and opening up unprecedented levels of scale.

### [06:49 - 06:52]

Other researchers at OpenAI quickly grasped the significance of Radford's results,

### [06:53 - 06:57]

and the team went all in on this approach, aggressively scaling up to GPT-2 in 2019,

### [06:57 - 07:04]

GPT-3 in 2020, and ChattGPT in 2022.

### [07:04 - 07:08]

In 2012, AlexNet was trained on around a million examples.

### [07:08 - 07:12]

In 2020, GPT-3 was trained on hundreds of billions of examples.

### [07:12 - 07:18]

And interestingly, the new training paradigm that emerged exactly matched Yann LeCun's predictions from a few years earlier.

### [07:18 - 07:21]

An extensive self-supervised network of training systems,

### [07:21 - 07:24]

an extensive self-supervised pre-training phase,

### [07:24 - 07:25]

followed by supervised learning

### [07:25 - 07:28]

and finally reinforcement learning

### [07:28 - 07:30]

to shape the raw Next Token Predictor model

### [07:30 - 07:32]

into a helpful AI assistant.

### [07:33 - 07:35]

However, while these self-supervised generative approaches

### [07:35 - 07:38]

clearly broke through in language,

### [07:38 - 07:42]

the picture was much fuzzier for image and video data.

### [07:42 - 07:44]

But I kept working on vision,

### [07:44 - 07:49]

and then initially the idea was to use

### [07:49 - 07:54]

to train a system to predict what happens in video,

### [07:54 - 07:56]

but to use generative architectures.

### [07:57 - 07:59]

So basically train at a pixel level

### [07:59 - 08:01]

what's gonna happen in the video.

### [08:01 - 08:04]

Years before the success of GPT-1,

### [08:04 - 08:06]

researchers including Lacoon had tried to apply

### [08:06 - 08:10]

the same self-supervised generative approach to video.

### [08:10 - 08:12]

In the most straightforward implementation,

### [08:12 - 08:13]

we configure our neural network

### [08:13 - 08:15]

to take in the RGB pixel values

### [08:15 - 08:17]

from a sequence of video frames,

### [08:17 - 08:19]

and then predict the pixel values

### [08:19 - 08:20]

in the next frame,

### [08:20 - 08:22]

just as the GPT models are trained

### [08:22 - 08:25]

to predict the next token in language.

### [08:25 - 08:26]

However, when we use these models

### [08:26 - 08:28]

to predict the next frame,

### [08:28 - 08:30]

the results are blurry.

### [08:30 - 08:32]

And this blurriness compounds dramatically

### [08:32 - 08:34]

in longer horizon predictions.

### [08:34 - 08:37]

Large language models are auto-regressive.

### [08:37 - 08:39]

When ChatGPT answers a question,

### [08:39 - 08:41]

it generates one token at a time,

### [08:41 - 08:44]

at each step feeding its latest generated token

### [08:44 - 08:47]

back into its input to create the next output.

### [08:47 - 08:49]

If we try this auto-regressive approach

### [08:49 - 08:51]

for the next frame video prediction model,

### [08:51 - 08:54]

the results quickly devolve into blurry nothingness.

### [08:55 - 08:58]

Before we see exactly how JEPA is able to get around

### [08:58 - 09:00]

this blurry prediction problem,

### [09:00 - 09:02]

let's look at another fascinating application

### [09:02 - 09:05]

of transformers beyond language models.

### [09:05 - 09:08]

This video is sponsored by Hudson River Trading,

### [09:08 - 09:11]

and this is an order book.

### [09:11 - 09:14]

The left column shows all the bids to buy NVIDIA stock,

### [09:14 - 09:16]

ranked by bid price.

### [09:16 - 09:18]

And the right column shows all the current offers to sell

### [09:18 - 09:22]

NVIDIA stock, ranked by asking price.

### [09:22 - 09:24]

On a busy trading day,

### [09:24 - 09:27]

on the order of 1,000 new buy and sell orders like this

### [09:27 - 09:29]

come in every second.

### [09:29 - 09:30]

This deluge of orders

### [09:30 - 09:33]

is an incredibly rich information source.

### [09:33 - 09:35]

Is it possible to train a transformer,

### [09:35 - 09:37]

like the ones used in vJEPA,

### [09:37 - 09:40]

to find patterns in this data

### [09:40 - 09:43]

and use these patterns to predict future prices?

### [09:43 - 09:45]

Hudson River Trading has trillions of tokens

### [09:45 - 09:47]

of historical data.

### [09:47 - 09:48]

This is the same order of magnitude of trading,

### [09:48 - 09:52]

of training data used to train frontier LLMs.

### [09:52 - 09:54]

And their researchers are working to push the frontiers

### [09:54 - 09:56]

of machine learning on this data.

### [09:57 - 10:00]

The vJEPA model we'll see later in the video

### [10:00 - 10:03]

maps patches of videos to individual embedding vectors.

### [10:03 - 10:06]

We could take a similar approach with order book data,

### [10:06 - 10:10]

tokenizing groups of orders using some financial intuition.

### [10:10 - 10:14]

However, this naive approach does not work well in practice.

### [10:14 - 10:15]

And the Hudson River Trading team

### [10:15 - 10:17]

has developed some really interesting approaches

### [10:17 - 10:18]

to adapt cutting edge data

### [10:18 - 10:20]

and cutting edge transformer architectures

### [10:20 - 10:23]

to the complexities and constraints of trading data.

### [10:23 - 10:25]

And all of this is happening in a setting

### [10:25 - 10:27]

where speed is everything.

### [10:27 - 10:30]

Models have to run under incredibly tight latency constraints.

### [10:31 - 10:34]

These fascinating and highly complex research

### [10:34 - 10:36]

and engineering challenges,

### [10:36 - 10:38]

combined with the resources to actually tackle them

### [10:38 - 10:41]

and an open, highly collaborative environment,

### [10:41 - 10:45]

make Hudson River Trading an incredibly unique place to work.

### [10:45 - 10:48]

I hear a lot from potential sponsors these days

### [10:48 - 10:50]

and have been seriously impressed in my interactions

### [10:50 - 10:52]

with the Hudson River Trading team.

### [10:52 - 10:54]

The level of technical discussion and enthusiasm

### [10:54 - 10:56]

for these deep and interesting problems

### [10:56 - 10:59]

is unparalleled in my experience.

### [10:59 - 11:00]

If this sounds interesting,

### [11:00 - 11:03]

Hudson River Trading is currently hiring for AI researchers,

### [11:03 - 11:07]

algorithm developers, and software engineers.

### [11:07 - 11:08]

They're hiring globally

### [11:08 - 11:10]

and you don't need a finance background.

### [11:10 - 11:12]

You can learn more at hudsonrivertrading.com

### [11:12 - 11:14]

forward slash Welch Labs.

### [11:14 - 11:16]

Now back to JEPA.

### [11:16 - 11:19]

Now, the blurry frames produced

### [11:19 - 11:21]

by our generative video prediction approach

### [11:21 - 11:23]

are not some huge mystery.

### [11:23 - 11:26]

Language is complex and unpredictable,

### [11:26 - 11:27]

but it's nothing compared to video.

### [11:28 - 11:32]

Language models use fixed-size vocabularies.

### [11:32 - 11:36]

GPT-2 has 50,257 discrete outputs,

### [11:36 - 11:39]

one for each token that the model could say next.

### [11:39 - 11:43]

This complete enumeration approach is hopeless in video.

### [11:43 - 11:46]

For full HD video in the most general case,

### [11:46 - 11:50]

each pixel can take on 256 discrete values.

### [11:50 - 11:54]

And we have 1920 times 1080 times three color pixels,

### [11:54 - 11:56]

meaning there are something like 10 to the power

### [11:56 - 12:00]

of 15 million possible next video frames,

### [12:00 - 12:04]

dwarfing the number of atoms in the observable universe.

### [12:04 - 12:06]

So there's no way our video prediction model

### [12:06 - 12:07]

can have a discrete output

### [12:07 - 12:10]

for each possible next video frame,

### [12:10 - 12:12]

as our language model has a discrete output

### [12:12 - 12:13]

for each next possible token.

### [12:14 - 12:16]

Instead, many generative video frames,

### [12:16 - 12:18]

video approaches of this era,

### [12:18 - 12:22]

have the network directly output pixel intensity values.

### [12:22 - 12:24]

The big challenge with this approach

### [12:24 - 12:27]

is how the model learns to handle uncertainty.

### [12:28 - 12:30]

If we compare an LLM learning to complete the sentence,

### [12:30 - 12:32]

the ball bounced to the,

### [12:32 - 12:35]

and a neural network predicting the next frame of a video

### [12:35 - 12:37]

of a ball actually bouncing,

### [12:37 - 12:39]

we can see exactly what goes wrong.

### [12:39 - 12:41]

In the LLM training case,

### [12:41 - 12:44]

the model will see various examples in its training set

### [12:44 - 12:45]

of the ball bouncing left and right,

### [12:45 - 12:49]

and since the model has separate outputs

### [12:49 - 12:51]

for each of these tokens,

### [12:51 - 12:54]

it can essentially independently update these probabilities.

### [12:54 - 12:57]

Our video model doesn't have it so easy.

### [12:57 - 12:59]

If our dataset includes videos of the ball

### [12:59 - 13:01]

starting down the same path

### [13:01 - 13:04]

and then bouncing in various directions,

### [13:04 - 13:06]

since our model is forced to directly predict

### [13:06 - 13:08]

a single output frame for a given input,

### [13:08 - 13:11]

the best it can do in the face of this ambiguity

### [13:11 - 13:14]

is to predict the average of these outcomes.

### [13:14 - 13:15]

When we average the pixel value, each given size is equal to 0.5.

### [13:15 - 13:21]

pixel values of our videos, we end up with a blurry, washed-out mess.

### [13:21 - 13:25]

Now this is only the most naive approach, and there have been many, many interesting

### [13:25 - 13:29]

video and image prediction strategies tried with various degrees of success over the last

### [13:29 - 13:30]

couple decades.

### [13:30 - 13:36]

However, the challenges that naturally arise led Lacoon and other researchers to ask an

### [13:36 - 13:38]

interesting question.

### [13:38 - 13:41]

Do our models really need to be generative?

### [13:41 - 13:47]

In our GPT example, during the crucial pre-training phase, it really doesn't matter that our

### [13:47 - 13:49]

model is generative.

### [13:49 - 13:53]

After pre-training on next-token prediction, we're left with a model that's essentially

### [13:53 - 13:56]

a really good autocomplete.

### [13:56 - 13:58]

But this is not the point.

### [13:58 - 14:03]

What actually matters are the internal representations and features that the model learns to solve

### [14:03 - 14:06]

the next-token prediction task.

### [14:06 - 14:10]

These learned internal representations are what allows pre-trained models to be quickly

### [14:10 - 14:11]

adapted and deployed.

### [14:11 - 14:16]

And that's why we need powerful AI assistants.

### [14:16 - 14:20]

Next-token prediction on language is a proxy for intelligence that has turned out to work

### [14:20 - 14:23]

shockingly well.

### [14:23 - 14:27]

But are there other signals and methods that we can use to learn these powerful internal

### [14:27 - 14:32]

representations that we need to build intelligent systems?

### [14:32 - 14:41]

Simultaneously, we started realizing in the, you know, around 2017, 18, that the best system

### [14:41 - 14:46]

to learn representations of images are systems that do not, are not generative.

### [14:46 - 14:48]

They don't reconstruct.

### [14:48 - 14:54]

They, you know, you get an image and you run it to an encoder, and then you try to kind

### [14:54 - 14:59]

of coerce this encoder to extract as much information as possible with certain properties.

### [14:59 - 15:04]

So for example, you take two images of the same scene, or you take an image and you corrupt

### [15:04 - 15:06]

it or transform it in some ways.

### [15:06 - 15:10]

You run them both through encoders, and you tell the system, the representation, whatever

### [15:10 - 15:14]

you extract to really be the same for those two images, because they semantically represent

### [15:14 - 15:17]

the same thing.

### [15:17 - 15:19]

And I've been working on things like this since the 90s.

### [15:19 - 15:23]

So this is not a new idea, this idea of joint embedding.

### [15:23 - 15:25]

We used to call this Siamese neural nets.

### [15:25 - 15:30]

The method Jan is referring to here, Siamese networks, was created by Jan and his collaborators

### [15:30 - 15:37]

at Bell Labs in the early 1990s when developing systems to detect fraudulent signatures.

### [15:37 - 15:40]

The system worked by passing a pair of signature images into two networks.

### [15:40 - 15:43]

Two copies of the same neural network.

### [15:43 - 15:46]

The network copies were not trained to generate any kind of data.

### [15:46 - 15:52]

Instead, they output vectors of numbers, often referred to as embedding vectors.

### [15:52 - 15:56]

These network copies were trained on two types of examples.

### [15:56 - 16:00]

Positive examples that contain a reference signature and a non-fraudulent signature.

### [16:00 - 16:02]

So these are by the same person.

### [16:02 - 16:08]

And negative examples that contain a reference signature and a fraudulent signature.

### [16:08 - 16:09]

For fraudulent examples.

### [16:09 - 16:10]

The network copies are trained.

### [16:10 - 16:14]

To produce embedding vectors that are maximally different.

### [16:14 - 16:19]

And for positive examples, produce embedding vectors that are maximally similar.

### [16:19 - 16:23]

When a new signature comes along, we can pass it into our network to compute an embedding

### [16:23 - 16:24]

vector.

### [16:24 - 16:28]

And compare it to the embedding vector produced from our reference signature.

### [16:28 - 16:32]

If the resulting embedding vectors are not similar enough, the signature is detected

### [16:32 - 16:34]

as fraudulent.

### [16:34 - 16:40]

By jointly embedding our signatures, our Siamese network learns a very useful internal representation

### [16:40 - 16:42]

of the images of our signatures.

### [16:42 - 16:48]

Notably without learning to predict or generate any actual signature images, as a GPT-based

### [16:48 - 16:50]

approach would.

### [16:50 - 16:54]

Joint embeddings offer a potentially viable solution to our blurry video problem.

### [16:54 - 16:55]

As Yann explains,

### [16:55 - 17:00]

You get an image and you run it to an encoder.

### [17:00 - 17:05]

And then you try to kind of coerce this encoder to extract as much information as possible

### [17:05 - 17:06]

with certain properties.

### [17:06 - 17:09]

So for example, you take two images of the same scene.

### [17:10 - 17:13]

Or you take an image and you corrupt it or transform it in some ways.

### [17:13 - 17:17]

You run them both through encoders, and you tell the system, the representation, whatever

### [17:17 - 17:21]

you extract, should really be the same for those two images because they semantically

### [17:21 - 17:22]

represent the same thing.

### [17:22 - 17:27]

So the idea here is that we sidestep the blurry video problem we saw with generative models

### [17:27 - 17:33]

by using a joint embedding architecture to map copies of images or videos, with one or

### [17:33 - 17:38]

both corrupted or transformed, to similar embedding vectors.

### [17:38 - 17:39]

This trained model will ideally learn a lot from it.

### [17:39 - 17:58]

However, this joint embedding strategy has a huge problem.

### [17:58 - 18:02]

Since we're training our network to make the embeddings of our original and corrupted

### [18:02 - 18:08]

images or videos as similar as possible, the network can find a trivial solution where

### [18:08 - 18:09]

it simply returns the same embedding.

### [18:09 - 18:18]

If our network learns to output, for example, a vector of all 1s for any input, then the

### [18:18 - 18:23]

network will return all 1s for a corrupted and non-corrupted view of the same image,

### [18:23 - 18:28]

maximizing the resulting similarity, but without actually learning anything useful.

### [18:28 - 18:32]

This problem is known as representation collapse.

### [18:32 - 18:37]

In Lacoon's original Siamese network approach, the team used what's now known as contrastive

### [18:37 - 18:38]

learning to avoid representation collapse.

### [18:38 - 18:39]

In Lacoon's original Siamese network approach, the team used what's now known as contrastive learning to avoid representation collapse.

### [18:39 - 18:41]

In Lacoon's original Siamese network approach, the team used what's now known as contrastive learning to avoid representation collapse.

### [18:41 - 18:45]

Giving the network both positive and negative examples.

### [18:45 - 18:49]

It turns out we can apply the same contrastive approach to images and video.

### [18:49 - 18:53]

Training our network to output similar embeddings for views of the same underlying images or

### [18:53 - 18:58]

videos, and dissimilar embeddings for different images or video.

### [18:58 - 19:03]

These contrastive methods have been successfully implemented on images and videos, but can

### [19:03 - 19:08]

run into issues when they're scaled up, requiring large amounts of computation and many negative

### [19:08 - 19:08]

examples to learn meaningfully.

### [19:08 - 19:15]

And Lacoon has argued that in the worst case, the number of contrastive samples may grow

### [19:15 - 19:19]

exponentially with the dimension of the representation.

### [19:19 - 19:24]

By the end of the 2010s, it was clear to Lacoon and others that using generative models to

### [19:24 - 19:30]

fully reconstruct images and video was not a good strategy for self-supervised learning.

### [19:30 - 19:34]

But there wasn't a straightforward solution to the representation collapse problem that

### [19:34 - 19:37]

would allow joint embedding architectures to learn the same level of powerful, powerful

### [19:37 - 19:38]

learning.

### [19:38 - 19:44]

The only way to do this was to learn the new-general internal representations that large language

### [19:44 - 19:45]

models were enjoying.

### [19:45 - 19:50]

And so it was pretty clear that reconstruction was a bad idea for signals like images and

### [19:50 - 19:51]

for video.

### [19:51 - 20:02]

And I had a bit of an epiphany, because the methods that we were using to train those

### [20:02 - 20:08]

joint embedding architectures were kind of hacks, a little bit, until I did some work

### [20:08 - 20:12]

with a couple of post-docs at Meta,

### [20:12 - 20:15]

particularly a guy called Stéphane Denis,

### [20:15 - 20:18]

who came up with a technique called Barlow Twin.

### [20:18 - 20:22]

So it's based on an old idea in computational

### [20:22 - 20:24]

knowledge science and machine learning

### [20:24 - 20:27]

that Jeff Hinton also played with similar ideas,

### [20:27 - 20:29]

which is that you should have time to have some

### [20:29 - 20:33]

measure of information content and try to maximize that.

### [20:33 - 20:38]

And there's some really old work by Barlow

### [20:38 - 20:40]

about his famous computational neuroscientist

### [20:40 - 20:42]

and theoretical neuroscientist.

### [20:42 - 20:46]

Here, Jan is referencing the work of Horace Barlow,

### [20:46 - 20:50]

who hypothesized in 1961 that the neurons in animal

### [20:50 - 20:52]

and human vision systems operate by reducing

### [20:52 - 20:56]

redundant information between neurons.

### [20:56 - 21:00]

Stéphane Denis, a post-doc LeCun was working with in 2020,

### [21:00 - 21:03]

was familiar with Barlow's work and proposed that one way

### [21:03 - 21:06]

to avoid representation collapse could be to apply

### [21:06 - 21:08]

Barlow's idea to the out-of-the-world

### [21:08 - 21:09]

outputs of their networks.

### [21:10 - 21:13]

In the joint embedding architectures we've been considering,

### [21:13 - 21:15]

our embedding vectors are produced by a final layer

### [21:15 - 21:19]

of artificial neurons in our embedding networks.

### [21:19 - 21:22]

So if our embedding vectors are of length 128,

### [21:22 - 21:24]

then the output layer of each of our networks

### [21:24 - 21:26]

contains 128 neurons.

### [21:27 - 21:29]

If we pass in a batch of various images

### [21:29 - 21:33]

into each of our networks and plot the output activation

### [21:33 - 21:36]

of the first neuron as we step through our images,

### [21:36 - 21:37]

we can see that this neuron fires

### [21:37 - 21:40]

strongly on this first picture of a dog,

### [21:40 - 21:42]

not so much on this cat picture, and so on.

### [21:44 - 21:46]

Following our joint embedding approach,

### [21:46 - 21:48]

our network takes in a distorted view

### [21:48 - 21:50]

of the same batch of images.

### [21:50 - 21:53]

The whole point of our joint embedding architecture

### [21:53 - 21:54]

is to make the resulting embeddings

### [21:54 - 21:58]

of the same underlying images or videos similar.

### [21:58 - 22:00]

So we want the output of our first neuron

### [22:00 - 22:02]

in our second network to be similar to the output

### [22:02 - 22:04]

of our first neuron in our first network.

### [22:05 - 22:07]

In a standard joint embedding architecture,

### [22:07 - 22:11]

architecture, we would simply measure and maximize the similarity between these two

### [22:11 - 22:12]

vectors.

### [22:12 - 22:17]

However, as we've seen, this approach is susceptible to representation collapse, with

### [22:17 - 22:22]

the network simply learning to output the same values for any input image.

### [22:22 - 22:27]

But now, applying Barlow's hypothesis, as proposed by Stéphane Denis, we should reduce

### [22:27 - 22:31]

the redundancy between the outputs of different neurons.

### [22:31 - 22:34]

We have a bit of a choice to make here.

### [22:34 - 22:37]

We could compare the output of the first neuron in our first network to the output of our

### [22:37 - 22:42]

second neuron in our first network, or to the output of the second neuron in our second

### [22:42 - 22:43]

network.

### [22:43 - 22:47]

The team chose to compare to the output of the second network, as we'll see this results

### [22:47 - 22:52]

in a simpler implementation, and the team further notes in the appendix of their paper

### [22:52 - 22:56]

that in practice they didn't see much difference between these alternatives.

### [22:56 - 23:00]

Here's the output of the second neuron in our second model.

### [23:00 - 23:03]

To measure the redundancy between neuron outputs, the team computed

### [23:03 - 23:04]

the cross-sectional models.

### [23:04 - 23:07]

Here's the cross-correlation between these output vectors.

### [23:07 - 23:12]

This computation consists of scaling each vector and taking the dot product, resulting

### [23:12 - 23:16]

in a single number, the correlation.

### [23:16 - 23:20]

Or more precisely, the Pearson correlation coefficient between our vectors.

### [23:20 - 23:25]

To reduce the redundancy between our neurons, as proposed by Barlow, we want this correlation

### [23:25 - 23:28]

to be close to zero.

### [23:28 - 23:32]

If we arrange the neuron outputs of our first encoder vertically, and the outputs of our

### [23:32 - 23:33]

second encoder horizontally, then we get the result of a cross-correlation between these

### [23:33 - 23:33]

output vectors.

### [23:33 - 23:38]

We can compute and place the correlations between all pairs of neurons into a single

### [23:38 - 23:40]

matrix.

### [23:40 - 23:45]

This cross-correlation matrix has one row for each output neuron in our first encoder,

### [23:45 - 23:49]

and one column for each output neuron in our second encoder.

### [23:49 - 23:54]

The elements along the diagonal capture the correlations between corresponding neurons.

### [23:54 - 23:58]

Since the whole idea here of this joint embedding architecture is to produce similar outputs

### [23:58 - 24:03]

for distorted versions of the same image, we want the corresponding neurons in our two

### [24:03 - 24:06]

encoders to have high correlations.

### [24:06 - 24:11]

Alternatively, all of the off-diagonal entries in our cross-correlation matrix correspond

### [24:11 - 24:14]

to different neurons in our two encoders.

### [24:14 - 24:20]

And following Barlow's hypothesis, we want to reduce the redundancy between these neurons.

### [24:20 - 24:23]

So we want these correlations to be zero.

### [24:23 - 24:27]

So ideally, our cross-correlation matrix looks like the identity matrix.

### [24:27 - 24:32]

Denis, LeCun, and their collaborators designed a new loss function for their joint embedding architecture.

### [24:32 - 24:40]

That measured the deviation of their cross-correlation matrix from the identity matrix.

### [24:40 - 24:45]

Their new method, which they called Barlow twins, worked surprisingly well, avoiding

### [24:45 - 24:49]

representation collapse, while learning a powerful internal representation of the images

### [24:49 - 24:53]

that it was trained on.

### [24:53 - 24:57]

The team used a few different methods to measure the quality of these internal representations.

### [24:57 - 25:02]

Earlier, we saw how by using self-supervised pre-training, GPT-1 and GPT-2 were able to

### [25:02 - 25:10]

outperform purely supervised models that had been adapted to specific language tasks.

### [25:10 - 25:14]

For vision tasks, one of the most important benchmarks at the time was accuracy on the

### [25:14 - 25:17]

ImageNet dataset.

### [25:17 - 25:21]

This is the same image classification dataset that the AlexNet model had shown breakthrough

### [25:21 - 25:23]

performance on back in 2012.

### [25:23 - 25:30]

The original AlexNet paper achieved an accuracy of 59.3% on the ImageNet validation set.

### [25:30 - 25:31]

To compare this self-supervised Barlow twin to the original AlexNet paper, we used a

### [25:31 - 25:36]

fully supervised Barlow twins approach to fully supervise models like AlexNet.

### [25:36 - 25:41]

The team used a common approach known as a linear probe, where a single layer of neurons

### [25:41 - 25:48]

are tacked onto the output of the Barlow twins trained encoder model, and trained using supervised

### [25:48 - 25:51]

learning to classify the ImageNet dataset.

### [25:51 - 25:57]

Importantly, the main encoder model is frozen during this training process.

### [25:57 - 26:01]

So the simple linear probe is effectively adapting the Barlow twins encoder's learned

### [26:01 - 26:06]

representation to solve the ImageNet classification task.

### [26:06 - 26:11]

Impressively, the frozen Barlow twins encoder with a linear probe achieved an ImageNet accuracy

### [26:11 - 26:18]

of 73.2%, outperforming the original fully supervised AlexNet model by over 10 percentage

### [26:18 - 26:19]

points.

### [26:19 - 26:27]

However, in the 9 years from the AlexNet paper in 2012 to the Barlow twins paper in 2021,

### [26:27 - 26:30]

fully supervised approaches had made significant improvements over AlexNet.

### [26:30 - 26:31]

In the last 10 years, the Barlow twins encoder has achieved an image net accuracy of 73.2%.

### [26:31 - 26:37]

In 2020, a team at Google applied the transformer architecture to image classification, achieving

### [26:37 - 26:42]

a new state-of-the-art image net accuracy of 88.6%.

### [26:42 - 26:49]

So by 2021, thanks to the Barlow twins epiphany and other joint embedding approaches, self-supervised

### [26:49 - 26:55]

learning was advancing rapidly for vision tasks, but was still inferior to fully supervised

### [26:55 - 26:56]

methods.

### [26:56 - 27:00]

The general and clearly superior self-supervised generative pre-training methods in learning,

### [27:00 - 27:06]

and language, that were fueling the rapid advancement of LLMs, were still out of reach

### [27:06 - 27:08]

for image and video applications.

### [27:08 - 27:13]

And so it became clear that this really was the right way to go.

### [27:13 - 27:18]

So we kind of, after that, published another version, a simplified version, basically,

### [27:18 - 27:22]

of Barlow twins called VicReg, which turned out to be quite good.

### [27:22 - 27:26]

And then simultaneously, another group, some of our colleagues at FairParis, were working

### [27:26 - 27:29]

on similar methods, which eventually proved to be quite good.

### [27:29 - 27:35]

It eventually came to be known as Deno, Deno v1, v2, v3.

### [27:35 - 27:40]

Now they have a new version, which is not called Deno anymore.

### [27:40 - 27:43]

And this is also a joint embedding technique.

### [27:43 - 27:53]

So it was really clear joint embedding was better for self-supervised learning to represent

### [27:53 - 27:54]

images.

### [27:54 - 27:59]

The Deno v3 paper, released in August 2025, marked an important turning point

### [27:59 - 28:00]

in our research.

### [28:00 - 28:06]

Achieving a very near state of the art image net accuracy of 88.4%, using a joint embedding

### [28:06 - 28:09]

architecture.

### [28:09 - 28:11]

As the authors say in their paper,

### [28:11 - 28:15]

All in all, this is the first time that a self-supervised model has reached comparable

### [28:15 - 28:21]

results to weekly and supervised models on image classification.

### [28:21 - 28:26]

The quality of representations that Deno v3 is able to learn without access to any human

### [28:26 - 28:28]

generated labels is astounding.

### [28:28 - 28:29]

Deno outputs and embeds images with a great quality, and this is something that we are

### [28:29 - 28:29]

really proud of.

### [28:29 - 28:34]

vector for each patch of image that it analyzes. If I take this image of myself

### [28:34 - 28:40]

and take Dino's embedding vector from this image patch on my hand and compare

### [28:40 - 28:44]

this embedding vector to the rest of the patches in the image, visualizing how

### [28:44 - 28:48]

similar each patch is to the hand patch using a color map, Dino does a

### [28:48 - 28:53]

remarkably good job segmenting my hand from the background. Here's the same

### [28:53 - 29:00]

approach applied to a ball, a cat, and a book. Following the success of Barlow

### [29:00 - 29:06]

Twins, VicReg, and Dino v1, in 2022 Lacoon brought these and many other threads

### [29:06 - 29:11]

together into a 60-page position paper called A Path Towards Autonomous Machine

### [29:11 - 29:16]

Intelligence. Unlike the great majority of Lacoon's papers, where he works on

### [29:16 - 29:20]

specific and technical pieces of machine learning theory or practice, A Path

### [29:20 - 29:23]

Towards Autonomous Machine Intelligence

### [29:23 - 29:26]

takes a holistic first principles approach to how we should build

### [29:26 - 29:31]

intelligent machines. Lacoon begins by arguing that our current approaches to

### [29:31 - 29:36]

AI are nowhere near the capabilities of human learning, giving the example of a

### [29:36 - 29:41]

teenager that can learn to drive a car in around 20 hours of practice. How is it

### [29:41 - 29:45]

that we have those millions of hours of training data, where we have, we can train

### [29:45 - 29:51]

kind of level two system with it, which is what Tesla is doing basically, but

### [29:51 - 29:53]

nowhere near level three, four, five, six, seven, eight, nine, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, ten.

### [29:53 - 29:58]

ten, five, okay, yet a 17 year old can learn to drive in a few hours of

### [29:58 - 30:01]

practice. Like, how does that happen? Right? Shouldn't we figure out what's the

### [30:01 - 30:06]

secret there? And, my guess about it, is the secret is world models.

### [30:06 - 30:11]

Late. Lacoon's billion dollar bet is that the missing piece of modern AI is

### [30:11 - 30:17]

world models. Models that make predictions about the physical world. As he says in

### [30:17 - 30:21]

his 2022 Position Paper. Common sense can be seen as a collection of models of the

### [30:21 - 30:23]

world that can

### [30:23 - 30:26]

an agent what is likely, what is plausible, and what is

### [30:26 - 30:31]

impossible. Using such world models, animals can learn new

### [30:31 - 30:35]

skills with very few trials. They can predict the consequences

### [30:35 - 30:38]

of their actions. They can reason, plan, explore, and

### [30:38 - 30:42]

imagine new solutions to problems. Lacoon goes on to

### [30:42 - 30:45]

argue that joint embedding architectures offer the right

### [30:45 - 30:48]

foundation to build world models on top of.

### [30:48 - 30:51]

So JEPA means Joint Embedding Predictive Architecture, and

### [30:51 - 30:56]

it's, you take an observation in the world, and then the next

### [30:56 - 30:59]

observation in the world, you run them through encoders. So

### [30:59 - 31:02]

there's like a joint embedding type architecture. And then you

### [31:02 - 31:04]

have a predictor that tries to predict that the state at time t

### [31:04 - 31:07]

plus one from the state at time t, and you might condition this

### [31:07 - 31:09]

on an action, and then you have a world model.

### [31:10 - 31:13]

As a concrete example, instead of using a generative

### [31:13 - 31:16]

architecture to predict the pixel values in the next frame

### [31:16 - 31:20]

of video, we can map the video in next frame to embeddings, and

### [31:20 - 31:21]

then train a predictor

### [31:21 - 31:25]

model to predict the embedding of the next frame, given the

### [31:25 - 31:29]

embedding of the video. In this implementation, the JEPA

### [31:29 - 31:32]

architecture frees the model of the intractable task of

### [31:32 - 31:36]

predicting every pixel in the next frame of video, and

### [31:36 - 31:38]

theoretically allows the predictor to focus on predicting

### [31:38 - 31:42]

only the salient features of the scene that make it through the

### [31:42 - 31:45]

encoder. Jan gives a nice example here.

### [31:45 - 31:48]

If you train a generative model, you know, to predict what's

### [31:48 - 31:50]

going to happen in the dashcam video,

### [31:51 - 31:55]

most of its resources predicting the random motion of the leaves on

### [31:55 - 31:59]

the trees that are bordering the road. And those are things that

### [31:59 - 32:01]

are essentially not predictable, but they have a lot of pixels

### [32:01 - 32:02]

that move around.

### [32:02 - 32:07]

As Jan mentioned earlier, we can take JEPA one step further by

### [32:07 - 32:11]

conditioning on actions. In the VJEPA2 paper, which we'll dig

### [32:11 - 32:14]

into in part two, the team conditions a JEPA model on the

### [32:14 - 32:16]

action signals sent to a robot arm.

### [32:18 - 32:21]

So the JEPA model sees a sequence of images of the robot's arm and

### [32:21 - 32:24]

environment, and then is trained to predict the embedding of the

### [32:24 - 32:28]

next video frame, but is also given the control signals that

### [32:28 - 32:32]

are sent to the robot arm. This allows the predictor to learn to

### [32:32 - 32:35]

predict how various control signals will change the robot

### [32:35 - 32:37]

arm's position in the embedded image.

### [32:39 - 32:42]

This learned world model can then be used for robot planning

### [32:42 - 32:46]

and control. Given an image of some goal state, for example,

### [32:46 - 32:50]

moving a cup off of a platform, this image is passed into the

### [32:50 - 32:51]

next frame encoder.

### [32:51 - 32:54]

Resulting in an embedding of the goal state of the robot.

### [32:55 - 32:58]

From here, a controls algorithm can be used to explore the world

### [32:58 - 33:02]

model's predictions, given various hypothetical actions.

### [33:03 - 33:05]

And find a set of actions that will lead the model's predicted

### [33:05 - 33:07]

future state to match its goal state.

### [33:08 - 33:11]

As Jan says, this is really a new twist on an old idea.

### [33:11 - 33:14]

You build a model that gives you the state of the world at time t

### [33:14 - 33:17]

plus one as a function of the state of the world at time t,

### [33:17 - 33:21]

and an action you imagine taking, or intervention, or control, right?

### [33:21 - 33:26]

And then if you have this, you can predict the outcome of a sequence

### [33:26 - 33:28]

of actions, and you can, by optimization, you can figure out

### [33:28 - 33:33]

an optimal sequence of actions to arrive at a particular outcome, right?

### [33:33 - 33:38]

This is classical optimal control. This is going back to the late 50s

### [33:39 - 33:44]

in the Soviet Union, early 60s in the West. Very classical stuff.

### [33:44 - 33:45]

Yeah.

### [33:45 - 33:48]

What is not classical is you learn the model.

### [33:48 - 33:49]

Sure, yeah.

### [33:49 - 33:50]

You use machine learning to learn the model.

### [33:50 - 33:51]

Right, yeah.

### [33:51 - 33:55]

What is even less classical is you learn a representation of the input

### [33:56 - 34:00]

that computes a state, an abstract state representation.

### [34:00 - 34:05]

And you learn the model in that state.

### [34:05 - 34:07]

And that's JEPA.

### [34:09 - 34:15]

But will JEPA or other world model-based approaches really overtake large language models?

### [34:15 - 34:21]

Since Lacoon first proposed JEPA in 2022, the architecture has been applied by various

### [34:21 - 34:26]

teams to a wide range of problems. How exactly do these models stack up?

### [34:27 - 34:32]

In part two, we'll dive deeper into VJEPA2 to get a sense for what's really happening inside

### [34:32 - 34:39]

the model's embedding space, and see how VJEPA2 fares as a robotics control algorithm against

### [34:39 - 34:45]

rapidly advancing VLA approaches. We'll also explore VLJEPA, which solves

### [34:45 - 34:51]

many of the same vision language problems we solve today with multimodal LLMs, but in a very different way.

### [34:51 - 34:56]

And with impressive results. Finally, we'll spend some time on an implementation of JEPA

### [34:56 - 35:01]

called LayWorld Model. LayWorld Model gives perhaps the most complete, albeit early,

### [35:01 - 35:06]

picture of what JEPA-based systems can do. Until next time, I'll leave you with Jan's take.

### [35:06 - 35:12]

Okay, let me make a controversial statement that, again, is going to get me a lot of friends.

### [35:12 - 35:19]

It's equally funny. I do not understand how you can even think of building an agentic system

### [35:20 - 35:26]

with that agentic system having the ability of predicting the consequences of its actions.

### [35:28 - 35:34]

VLA doesn't do that. LLMs do not have role models. They cannot predict the consequences

### [35:34 - 35:45]

of their actions beforehand. They just take the action and then, as some famous French kings said.

### [35:45 - 35:52]

If you really want to build reliable agentic systems, they absolutely have to be able to

### [35:52 - 35:56]

predict the consequences of their actions so that they can plan a sequence of actions to do

### [35:56 - 36:03]

something, first of all, to fulfill the task that they are being asked to fulfill, but also

### [36:05 - 36:11]

perhaps to guarantee some safety guardrails. The inference process now becomes a search

### [36:11 - 36:13]

as opposed to just an autoregressive prediction.

### [36:15 - 36:18]

So that's a role model. That's just a whole idea of a role model.

### [36:20 - 36:24]

If you enjoyed this video, check out the Welch Labs Illustrated Guide to AI.

### [36:25 - 36:30]

Its cover produces highly consistent Deno representations, so you know it has to be good.

### [36:31 - 36:35]

The book is beautifully illustrated and is a great way to dig deeper into many of the topics

### [36:35 - 36:41]

we touched on in this video. Chapter 5 on AlexNet is a great way to learn more about embedding

### [36:41 - 36:43]

vectors and the rise of deep learning.

### [36:45 - 36:51]

Chapter 6 on Neural Scaling Laws takes a deeper look at the fascinating buildup from GPT-1 to GPT-3

### [36:51 - 36:58]

at OpenAI. Chapter 9 covers diffusion models, which are able to reconstruct highly accurate

### [36:58 - 37:03]

pixel-level representations of images and video, but with some notable trade-offs.

### [37:04 - 37:08]

Chapters 1 through 4 give some great background on all of these topics,

### [37:08 - 37:12]

covering the fundamentals of neural networks, backpropagation, and deep learning.

### [37:13 - 37:15]

Each chapter includes thought-provoking exercises,

### [37:15 - 37:19]

and supporting code. The book is now shipping to 24 countries.

### [37:19 - 37:22]

You can pick up a copy today at welchlabs.com.
