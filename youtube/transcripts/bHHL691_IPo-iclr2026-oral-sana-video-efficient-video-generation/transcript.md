# SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer

- URL: https://www.youtube.com/watch?v=bHHL691_IPo
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-12T00:55:42`

## Transcript

### [00:00 - 00:06]

Thank you, Luke, for the amazing opening. So good morning and thanks for having me.

### [00:06 - 00:10]

My name is Jun Song. I'm from the University of Hong Kong and NVIDIA.

### [00:10 - 00:17]

It's really my great honor to present this work, SANA-Video, for our SANA team.

### [00:17 - 00:25]

So currently, generative AI is evolving rapidly, with model sizes growing larger and larger.

### [00:25 - 00:31]

At the same time, NVIDIA GPUs are becoming increasingly powerful.

### [00:31 - 00:38]

We can foresee that future visual generative models will demand even more computational resources.

### [00:38 - 00:46]

So actually, generating images and videos are significantly more computationally demanding than processing just text.

### [00:46 - 00:53]

For example, the inference FLOPS for FLUX or Coq VideoX exceed LAMA3.

### [00:53 - 00:55]

And in order for me to do that,

### [00:55 - 00:58]

I need to make the magnitude higher than the VIT models.

### [00:58 - 01:07]

So they are restricted to cloud deployment and remain impractical for consumer GPUs or edge devices.

### [01:07 - 01:11]

So actually, efficiency is a forever topic.

### [01:11 - 01:17]

So far, we have explored several directions for efficient video generation.

### [01:17 - 01:25]

First, in SANA, we tried to reduce input tokens by using our self-developed deep compression auto-encoder.

### [01:25 - 01:30]

We also tried to use linear attention to replace softmax-1,

### [01:30 - 01:35]

enhance the architectural efficiency of the model.

### [01:35 - 01:41]

And we also already explored inference step distillation in SANA Spring project.

### [01:41 - 01:44]

The fewer the inference steps, the faster the speed.

### [01:44 - 01:48]

So the last part is what we are going to talk about today,

### [01:48 - 01:53]

the hybrid AR plus diffusion for long video generation.

### [01:53 - 02:01]

Actually, we can generate video block by block causally and diffuse within the block.

### [02:01 - 02:05]

So video generation requires much more computation than images.

### [02:05 - 02:09]

SANA can generate one image within just one second.

### [02:09 - 02:17]

However, generating a five-second video with one model actually takes nearly 30 minutes.

### [02:17 - 02:20]

So to boost the video generation efficiency,

### [02:20 - 02:23]

we focus on three key technical areas.

### [02:23 - 02:27]

The high ratio VAEs and linear attention mechanisms,

### [02:27 - 02:31]

especially optimized for video tasks.

### [02:31 - 02:35]

Crucially, the block KV cache, based on linear attention,

### [02:35 - 02:39]

enables the generation of much longer videos.

### [02:39 - 02:42]

So to get a video generation model,

### [02:42 - 02:45]

actually, we have two ways to go, to choose.

### [02:45 - 02:48]

First, we can just train from scratch.

### [02:48 - 02:52]

But only when we have hundreds or thousands of GPUs,

### [02:52 - 02:54]

like H100 GPUs.

### [02:54 - 03:00]

And it will take you almost several months to train one model.

### [03:00 - 03:03]

And it's, of course, not affordable.

### [03:03 - 03:08]

Or actually, we can start from a semantic-aligned text-to-image model.

### [03:08 - 03:10]

Here we start from our SANA 1.5,

### [03:10 - 03:14]

which is a 1.6 billion parameter text-to-image model

### [03:14 - 03:18]

trained on our DCAE.

### [03:18 - 03:21]

Actually, since our video model is based on image model,

### [03:21 - 03:25]

so the linear attention DIT actually is almost the same as our SANA.

### [03:25 - 03:30]

But we're introducing two modules for temporal modeling.

### [03:30 - 03:32]

And we will talk about them later.

### [03:32 - 03:34]

And finally, on the left top,

### [03:34 - 03:37]

we implement block causal linear attention module

### [03:37 - 03:41]

to achieve constant KV cache memory.

### [03:41 - 03:44]

So for any length video generation.

### [03:44 - 03:49]

So first, let's talk about linear attention in video generation model.

### [03:49 - 03:51]

Actually, in video generation,

### [03:51 - 03:52]

in video tasks,

### [03:52 - 03:57]

linear attention provides even more significant acceleration than in images,

### [03:57 - 04:02]

as the video length and resolution are much larger.

### [04:02 - 04:05]

Our results show that for long videos,

### [04:05 - 04:10]

SANA video is 1.5 times faster than the one model.

### [04:10 - 04:12]

And additionally, at high resolution,

### [04:12 - 04:18]

our linear attention is four times faster than the flash attention.

### [04:18 - 04:21]

And these improvements make a long form.

### [04:21 - 04:25]

High resolution video generation is much more practical.

### [04:25 - 04:30]

However, we find that the linear attention map is far different from the softmax attention.

### [04:30 - 04:32]

As you can see in this figure,

### [04:32 - 04:34]

the linear attention is super dense,

### [04:34 - 04:37]

while the softmax attention is rather sparse.

### [04:37 - 04:42]

And this demonstrates that the local contacts captured by the linear attention

### [04:42 - 04:45]

is actually insufficient.

### [04:45 - 04:47]

To enhance the temporal modeling,

### [04:47 - 04:49]

we introduced two key improvements.

### [04:49 - 04:50]

First,

### [04:50 - 04:56]

the 3D rope for the linear attention and temporal convolutions,

### [04:56 - 05:00]

and both are highlighted in the orange box.

### [05:00 - 05:06]

While 3D rope doesn't solve the attention map sparsity problem entirely,

### [05:06 - 05:10]

it does help improve attention quality.

### [05:10 - 05:14]

Combined with our spatial temporal mixed FFN,

### [05:14 - 05:17]

it significantly boosts the overall performance.

### [05:17 - 05:19]

Here we have the training loss.

### [05:19 - 05:26]

The green line stands for the 3D rope and the additional temporal convolution.

### [05:26 - 05:29]

And to further support long video generation,

### [05:29 - 05:32]

we leverage the unique properties of linear attention

### [05:32 - 05:36]

to implement an efficient block KV cache.

### [05:36 - 05:40]

So let's quickly review how this works.

### [05:40 - 05:42]

In linear attention,

### [05:42 - 05:45]

we call it the attention map or the state.

### [05:45 - 05:47]

Actually, it has a fixed shape of D times D,

### [05:47 - 05:50]

regardless of the input sequence length.

### [05:50 - 05:52]

So when processing the first block here,

### [05:52 - 05:55]

we obtain the state as one.

### [05:55 - 05:57]

And for the second block,

### [05:57 - 06:00]

the state is updated additively,

### [06:00 - 06:05]

meaning that we only need to add the current block's contribution

### [06:05 - 06:07]

to the previous cache.

### [06:07 - 06:10]

And generally for any block I,

### [06:10 - 06:15]

actually the current state is updated as adding the current block contribution,

### [06:15 - 06:16]

the KV here,

### [06:16 - 06:21]

to the previous cache as.

### [06:21 - 06:24]

So now let's see how we enable long video generation

### [06:24 - 06:27]

with block causal linear attention.

### [06:27 - 06:29]

For the first block here,

### [06:29 - 06:30]

the green one,

### [06:30 - 06:32]

we compute the state as one,

### [06:32 - 06:34]

shown in the green box.

### [06:34 - 06:37]

And after we compute first block's state,

### [06:37 - 06:38]

we cache it,

### [06:38 - 06:40]

as shown in the red box.

### [06:40 - 06:43]

Then we calculate the KV for the next block

### [06:43 - 06:45]

and add it to the previous one.

### [06:45 - 06:50]

Here we take the cached state from block one

### [06:50 - 06:51]

in the red box

### [06:51 - 06:53]

and update it into the block two,

### [06:53 - 06:56]

which is in the green color.

### [06:56 - 07:00]

And the subsequent process follows the same logic.

### [07:00 - 07:02]

The new state is cached,

### [07:02 - 07:05]

and once the next block computation is finished,

### [07:05 - 07:08]

they are summed together.

### [07:08 - 07:10]

And so on.

### [07:15 - 07:19]

So token in linear attention will become larger,

### [07:19 - 07:20]

more and more,

### [07:20 - 07:23]

as the video length becomes larger and larger.

### [07:23 - 07:28]

While our causal linear attention maintains constant KV cache,

### [07:28 - 07:32]

potentially make minute length video generation possible.

### [07:32 - 07:34]

So here in conclusion,

### [07:34 - 07:38]

we can have two advantages of block linear attention.

### [07:38 - 07:42]

First, we have constant memory usage,

### [07:42 - 07:45]

regardless of the input sequence length.

### [07:45 - 07:46]

And second,

### [07:46 - 07:49]

we have the global history context.

### [07:49 - 07:53]

So one last question is how to achieve causal FFN

### [07:53 - 07:55]

with temporal conf.

### [07:55 - 07:58]

So let's take two block situation as example.

### [07:58 - 08:00]

During causal training,

### [08:00 - 08:02]

the block one cannot foresee block two.

### [08:02 - 08:07]

So we pad a zero token here between the two blocks.

### [08:07 - 08:10]

However, block two must see block one's token.

### [08:10 - 08:13]

So that is correct causal modeling.

### [08:13 - 08:15]

So here we cache the last step,

### [08:15 - 08:17]

the last token from block one,

### [08:17 - 08:22]

as the first token in block two.

### [08:22 - 08:25]

So finally the two blocks are separated

### [08:25 - 08:27]

by the zero padding token,

### [08:27 - 08:30]

which is subsequently removed

### [08:30 - 08:34]

to avoid affecting the final computation.

### [08:34 - 08:37]

And the block two used the last token from block one,

### [08:37 - 08:41]

making the causal modeling available.

### [08:41 - 08:44]

So here's some results

### [08:44 - 08:47]

compared to the current state of the art video models.

### [08:47 - 08:51]

So now video performs competitively on VBench,

### [08:51 - 08:54]

and it takes only 18 seconds

### [08:54 - 08:57]

to generate a 1K resolution video

### [08:57 - 09:00]

on a single H100 GPU.

### [09:00 - 09:02]

Here we show some examples.

### [09:02 - 09:03]

On the left,

### [09:03 - 09:07]

we have text-to-video examples.

### [09:07 - 09:08]

And on the right,

### [09:08 - 09:11]

we show the image-to-video examples.

### [09:11 - 09:13]

Using certain video as a base model,

### [09:13 - 09:17]

it can be applied to tasks like physical AI

### [09:17 - 09:19]

and real-world models.

### [09:19 - 09:22]

Actually, by fine-tuning SANA video

### [09:22 - 09:24]

on a small data site

### [09:24 - 09:27]

with just a few SFT steps,

### [09:27 - 09:30]

we enable it to generate videos

### [09:30 - 09:35]

for robotic manipulation and gameplay.

### [09:35 - 09:37]

We also combine with the post-training tech

### [09:37 - 09:38]

in Long Lab,

### [09:38 - 09:40]

which is a three-long test-long method.

### [09:40 - 09:42]

And this method is also accurate

### [09:42 - 09:46]

for poster and is also from our group.

### [09:46 - 09:49]

We also implement the DMD step distillation

### [09:49 - 09:53]

to further accelerate our model.

### [09:53 - 09:56]

And finally, SANA video can also generate

### [09:56 - 10:00]

minute-length video within just 36 seconds,

### [10:00 - 10:06]

achieving 27 FPS real-time generation.

### [10:06 - 10:09]

So finally, there is one more thing.

### [10:09 - 10:11]

Based on linear attention,

### [10:11 - 10:16]

we have much more potential applications to discover.

### [10:16 - 10:19]

We believe the efficiency of linear attention

### [10:19 - 10:21]

and deep compression auto-encoder

### [10:21 - 10:25]

will facilitate streaming video generation

### [10:25 - 10:28]

and also the development of long-form,

### [10:28 - 10:31]

like minute-length or even hour-length

### [10:31 - 10:33]

real-world models.

### [10:33 - 10:35]

And we are working on this project

### [10:35 - 10:37]

and we'll see if we can keep pushing

### [10:37 - 10:39]

the efficiency boundary.

### [10:39 - 10:41]

And all of our projects,

### [10:41 - 10:43]

including the code and checkpoints,

### [10:43 - 10:47]

are all open source to encourage further exploration

### [10:47 - 10:50]

in efficient generative AI system.

### [10:50 - 10:52]

So that's all for my talk today.

### [10:52 - 10:54]

And we will have a poster session

### [10:54 - 10:56]

right after this oral,

### [10:56 - 10:58]

maybe in the afternoon.

### [10:58 - 11:00]

Welcome everyone to discuss more.

### [11:00 - 11:02]

Thanks so much.

### [11:07 - 11:08]

Thank you.

### [11:08 - 11:11]

Time for a quick question, if any.

### [11:11 - 11:15]

Yeah, please go to the mic.

### [11:15 - 11:17]

Thank you for your speech.

### [11:17 - 11:19]

And I have a question.

### [11:19 - 11:21]

I think it's something similar

### [11:21 - 11:24]

to the auto-aggressive video diffusion models

### [11:24 - 11:26]

like causal vid,

### [11:26 - 11:30]

something similar to the block causal

### [11:30 - 11:33]

linear attention you introduced.

### [11:33 - 11:36]

So I wanted to ask what are the key differences

### [11:36 - 11:38]

and if we are thinking about

### [11:38 - 11:40]

infinite long video generation,

### [11:40 - 11:43]

which one do you think would be better choice?

### [11:43 - 11:44]

Thank you.

### [11:44 - 11:46]

Thank you for your question.

### [11:46 - 11:48]

Actually the causal vid,

### [11:48 - 11:49]

something like that,

### [11:49 - 11:52]

they actually perform on softmax attention.

### [11:52 - 11:54]

So as I talked before,

### [11:54 - 11:56]

the softmax attention has

### [11:56 - 11:59]

an open square computation complexity.

### [11:59 - 12:02]

So if you want to generate minute length

### [12:02 - 12:04]

or even hour length video,

### [12:04 - 12:09]

it's not possible to do it on softmax attention.

### [12:09 - 12:12]

So if you want to generate minute length video,

### [12:12 - 12:15]

so you have to keep the computation within

### [12:15 - 12:18]

like a sliding window or something like that.

### [12:18 - 12:20]

So the main difference here is

### [12:20 - 12:23]

our linear attention has the global context.

### [12:23 - 12:26]

It has memory from the first second

### [12:26 - 12:28]

to the final second.

### [12:28 - 12:31]

So if you want to do some project

### [12:31 - 12:33]

or task like world model,

### [12:33 - 12:37]

it has to be maintaining overall

### [12:37 - 12:38]

or the

### [12:39 - 12:41]

cache or the memory.

### [12:41 - 12:44]

So I think that's the main advantages

### [12:44 - 12:45]

of linear attention.

### [12:45 - 12:46]

Thank you.

### [12:46 - 12:47]

Thank you.
