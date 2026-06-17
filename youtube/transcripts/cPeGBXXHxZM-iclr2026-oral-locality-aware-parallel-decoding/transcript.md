# Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation

- URL: https://www.youtube.com/watch?v=cPeGBXXHxZM
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-12T01:07:04`

## Transcript

### [00:00 - 00:12]

Thanks, everyone, for coming here, and thanks for the introduction. My name is Lu Kuang.

### [00:12 - 00:18]

I am an undergraduate at MIT right now, working with Professor Song Han's lab. Unfortunately,

### [00:18 - 00:22]

my co-first author, Joyang, could not be with us here today because of visa issues, but

### [00:22 - 00:28]

I'll be presenting our work, locality-aware parallel decoding.

### [00:28 - 00:34]

So autoregressive models is the dominant paradigm in language, with autoregressive

### [00:34 - 00:40]

LLMs being able to scale to trillions of parameters and trillions of tokens trained. Autoregressive

### [00:40 - 00:44]

had its moments in image generation, however, starting with the release of the GPT-4O image

### [00:44 - 00:50]

generation model. So some of you probably remember that last year, everyone on X was

### [00:50 - 00:55]

trying to make their profile pic Ghibli-style, right? Even Sam Altman. And this was really

### [00:55 - 00:58]

the first time that autoregressive models really showed their

### [00:58 - 01:04]

potential in image generation. And as one of the co-creators, Lu Liu, said, said this

### [01:04 - 01:09]

at the CVPR conference last year, it was the first model that proves autoregressive model

### [01:09 - 01:16]

works better than diffusion for image gen. Today, unified multimodal systems basically

### [01:16 - 01:22]

use a unified autoregressive approach to combine vision and language modeling. Starting with

### [01:22 - 01:28]

works like Chameleon, and then VLOU, EMU3, Janus Pro, and more recently, LongHat Next,

### [01:28 - 01:32]

all of these adopt a unified autoregressive approach. The reason is simple. If you have

### [01:32 - 01:36]

autoregressive modeling approach to image generation, it's extremely compatible with the

### [01:36 - 01:42]

next token prediction paradigm in language. But right now, there's two paradigms of

### [01:42 - 01:47]

autoregressive image generation, each with their own tradeoffs. The first is what I call a flat

### [01:47 - 01:54]

token representation. This is very nihilist to language. First, we tokenize the image into a

### [01:54 - 01:58]

sequence of tokens in raster order, and then we perform next image token prediction.

### [01:58 - 02:05]

The other paradigm is next scale or next resolution prediction, started by works like VAR.

### [02:05 - 02:12]

Here, we protect all tokens in next scale in parallel. However, the first one is very slow

### [02:12 - 02:17]

because it's memory bound, as with most LLMs. This means the latency of generating a single

### [02:17 - 02:21]

image is proportional to the number of tokens in the image, which can get really high for high

### [02:21 - 02:27]

resolution images. VAR sidesteps this with parallel prediction at the next scale, but it's not

### [02:27 - 02:28]

compatible with the vision and code that we're using. So, we're going to use this paradigm to

### [02:28 - 02:38]

show you how to use this paradigm. So, how can we develop both fast and multimodal compatible

### [02:38 - 02:44]

autoregressive modeling for images? Our method, locality aware parallel decoding, solves this with

### [02:44 - 02:51]

two main methods. First, we introduce flexible parallelized autoregressive modeling. This is a

### [02:51 - 02:57]

new architecture for doing prediction on any set of tokens, in parallel, in any order, while

### [02:57 - 02:58]

maintaining KV caching of tokens. This is a new architecture for doing prediction on any set of

### [02:58 - 03:03]

token variables. The second is locality aware generation ordering. This is a novel scheduling

### [03:03 - 03:09]

strategy that maintains generation quality while scheduling tokens in parallel. So, let's go

### [03:09 - 03:15]

through each one of them one by one. In normal autoregressive generation, we usually start with a

### [03:15 - 03:20]

class token or some series of prompt embeddings, and then after the first forward pass, we get the

### [03:20 - 03:25]

logits for the first token and we sample it. We repeat this again. We pass in the first token we

### [03:25 - 03:27]

just generated and we get out the logits for the second token. The second generation, which is this

### [03:27 - 03:35]

token. And then so on. So note here there's actually two things going on. First, each

### [03:35 - 03:40]

token has to predict the next token in a fixed order. Whatever you train with the order,

### [03:40 - 03:45]

you must do inference with. Now, the second thing is that each token is actually doing

### [03:45 - 03:51]

two roles at the same time. What I call context and generation. Here, each token once it's

### [03:51 - 03:56]

generated has to be encoded via forward pass so that future tokens can see it via attention.

### [03:56 - 04:01]

But it also serves as generation because once it's output is logits, it's used to sample

### [04:01 - 04:06]

the next token. This means that this is limited to a fixed input output structure. For every

### [04:06 - 04:12]

token you input, you get one output. So how can we break this to support parallel autoregressive

### [04:12 - 04:18]

modeling? In our approach, we continue to let the input tokens serve as context. However,

### [04:18 - 04:22]

we now delegate the role of generation to position query tokens. These position query

### [04:22 - 04:26]

tokens are a shared learnable embedding added on to the positional embedding of the target

### [04:26 - 04:32]

position you want to predict. For example, P4. After a forward pass, we get the logits

### [04:32 - 04:37]

for P4. And then for the next step, we have to put back the token we just generated. And

### [04:37 - 04:42]

now we can predict any set of tokens we want. Let's say three and five. And then so on.

### [04:42 - 04:46]

We get the tokens for three and five. And then afterwards, we can predict three of them

### [04:46 - 04:49]

now, like one, two, and six.

### [04:49 - 04:55]

So we notice that this method allows for a flexible input output structure with arbitrary

### [04:55 - 04:56]

order and parallelization.

### [04:56 - 05:03]

Which we call our flexible parallelized autoregressive modeling.

### [05:03 - 05:09]

So how do we actually train and do inference with flexible parallelized autoregressive modeling?

### [05:09 - 05:13]

Let's look at training first. We continue to adopt teacher forcing. So we interleave

### [05:13 - 05:18]

the ground truth tokens shown with the images here with the position query tokens that we

### [05:18 - 05:23]

want the model to learn how to transform into the actual ground truth tokens.

### [05:23 - 05:26]

Let's look at a given position query token like P2.

### [05:26 - 05:30]

So just like in normal autoregressive modeling, this position query token should attend to

### [05:30 - 05:35]

the previous ground truth tokens. This is what we call context attention in our model.

### [05:35 - 05:39]

At the same time, a key design of ours is that the position query tokens should be able

### [05:39 - 05:45]

to see the same position query tokens that are being predicted in parallel with it. Why?

### [05:45 - 05:49]

Because when you predict stuff in parallel, they're likely, they're sampled independently.

### [05:49 - 05:54]

So by sharing mutual information between them via attention, they're actually more likely

### [05:54 - 05:56]

to generate coherent images. And coherent tokens. And they're actually more likely to generate coherent images. And coherent tokens.

### [05:56 - 06:01]

So we can actually encode this in a single attention mask shown on the right.

### [06:01 - 06:06]

We have query attention between the position query tokens in yellow and the context attention

### [06:06 - 06:10]

between ground truth tokens and future tokens in green.

### [06:10 - 06:16]

So how do we do inference? In inference, we have two steps, very analogous to context

### [06:16 - 06:21]

and decoding. We have encoding, which is where we take the generated tokens and we do a forward

### [06:21 - 06:26]

pass. This is stored in the KP cache so that future tokens can see it. And then to get

### [06:26 - 06:31]

the next tokens, we input the position query tokens and we decode what the future tokens

### [06:31 - 06:37]

are that we want. Naively, doing this separately gives you two forward passes, which makes

### [06:37 - 06:42]

our inference 2x slower because it's memory bound. We can actually mix this into a fused

### [06:42 - 06:46]

forward pass in a single inference step with a specialized attention mask shown below,

### [06:46 - 06:53]

where we have the encoding intention in the green and the decoding intention in yellow.

### [06:53 - 06:56]

So now that I've explained that we have a architecture that can change the position

### [06:56 - 07:03]

and choose any order and any degree of parallelization, how do we actually choose this?

### [07:03 - 07:08]

So following previous works, we actually choose a cosine schedule for parallelization, where

### [07:08 - 07:15]

we decode less tokens at first and more and more tokens at the end. But for order, we

### [07:15 - 07:20]

actually took a look at the attention maps of previous autoressive models, and we found

### [07:20 - 07:25]

that the attention is strongly local. So you see in the main diagonal here, this is a token

### [07:25 - 07:26]

paying attention to the token that's in the middle. And this is a token that's in the

### [07:26 - 07:26]

middle. And this is a token that's in the middle. And this is a token that's in the middle.

### [07:26 - 07:34]

The lower diagonals to its left and below is paying attention to the token right in

### [07:34 - 07:38]

the row right above it. And then there are fainter diagonals even below that which are

### [07:38 - 07:41]

paying attention to tokens in two rows above it.

### [07:41 - 07:45]

So this strong spatial locality means that tokens that are close to each other strongly

### [07:45 - 07:49]

depend on each other in regular images. And this actually explains why current generation

### [07:49 - 07:56]

orders actually fail for parallel inference. So the first kind is raster order. Raster

### [07:56 - 07:59]

Raster order, you generate left to right, top down.

### [07:59 - 08:01]

But the thing is is that adjacent tokens

### [08:01 - 08:03]

are generated in parallel.

### [08:03 - 08:04]

Just like what I mentioned before,

### [08:04 - 08:07]

these tokens are heavily dependent on each other.

### [08:07 - 08:09]

And when you sample them independently,

### [08:09 - 08:11]

it's very likely that you generate incoherent

### [08:11 - 08:13]

or inconsistent features in the images.

### [08:13 - 08:16]

Random order was designed to avoid this

### [08:16 - 08:18]

because you spread out the tokens randomly.

### [08:18 - 08:20]

And this way, all the tokens you generate in parallel

### [08:20 - 08:22]

are very far from each other.

### [08:22 - 08:24]

But at the same time, they're very far

### [08:24 - 08:26]

from the previously generated tokens.

### [08:26 - 08:28]

And the strength of autoregressive models

### [08:28 - 08:30]

is that provide a strong conditioning.

### [08:30 - 08:33]

And if you're far away from the previous tokens,

### [08:33 - 08:34]

that means you have worse conditioning

### [08:34 - 08:36]

and leads to worse generation quality.

### [08:37 - 08:41]

Our generation order, our locality-aware generation order,

### [08:41 - 08:43]

thinks about both of these ideas

### [08:43 - 08:45]

and condenses them into two principles.

### [08:45 - 08:48]

The first is our order must have high proximity

### [08:48 - 08:50]

to previously generated tokens.

### [08:50 - 08:52]

The second is that we must have low proximity

### [08:52 - 08:54]

among concurrently generated tokens.

### [08:54 - 08:58]

Now, let's look at results.

### [08:58 - 09:02]

So for fair comparison, we train a normal raster order

### [09:02 - 09:03]

next token prediction model

### [09:03 - 09:06]

with the same architectural components as LPD

### [09:06 - 09:09]

on ImageNet of the same epochs and everything else.

### [09:09 - 09:13]

On 256 resolution, we can achieve 13x faster inference

### [09:13 - 09:16]

with same quality or 11x faster inference

### [09:16 - 09:17]

with the better quality.

### [09:17 - 09:21]

On 512 resolution, we can achieve 21 times faster inference

### [09:21 - 09:22]

with the same quality.

### [09:22 - 09:27]

And compared to previously parallel autoregressive models,

### [09:27 - 09:30]

we're 3.4x faster with better quality

### [09:30 - 09:32]

or 4.2x faster with the same quality.

### [09:35 - 09:38]

We also train on text-to-image benchmarks like gen eval

### [09:38 - 09:42]

and we can achieve a 61 times faster inference

### [09:42 - 09:45]

than compared with regular raster order next token prediction.

### [09:48 - 09:49]

So hopefully I've convinced you

### [09:49 - 09:52]

that locality-aware parallel prediction allows you to do this

### [09:52 - 09:54]

and allows you to reduce the number of steps

### [09:54 - 09:56]

and autoregressive modeling.

### [09:56 - 09:58]

And here's some visualizations.

### [09:58 - 10:01]

On the top left, we have our class conditional generation

### [10:01 - 10:04]

with editing, in-painting, out-painting.

### [10:04 - 10:07]

On the bottom is our text-to-image generation.

### [10:07 - 10:10]

And to our top right is a summary of our efficiency.

### [10:11 - 10:12]

Thank you all for coming.

### [10:12 - 10:13]

And just to summarize,

### [10:13 - 10:17]

locality-aware parallel decoding has two main methods.

### [10:17 - 10:19]

The first is flexible parallelized autoregressive modeling.

### [10:19 - 10:22]

Second is locality-aware generation order.

### [10:22 - 10:24]

And if you're interested in talking more,

### [10:24 - 10:29]

please, oh, there's a demo that I.

### [10:37 - 10:41]

Okay, yeah, so yeah, if you're interested in talking more,

### [10:41 - 10:44]

please drop by our poster today at 315 to 545

### [10:44 - 10:47]

in Pavilion 545.

### [10:48 - 10:52]

Oh, you can see in the demo that for the time it takes, the,

### [10:52 - 10:56]

it's two of the normal autoregressive images.

### [10:56 - 10:58]

This is the Lomogen XL on the top left.

### [10:58 - 11:00]

We can basically generate over 60 images.

### [11:00 - 11:02]

So it's quite fast.

### [11:02 - 11:03]

Thank you.

### [11:09 - 11:10]

Thank you so much.

### [11:10 - 11:11]

Time for the question.

### [11:18 - 11:20]

Okay, I have one question.

### [11:20 - 11:22]

When you push the parallel decoding,

### [11:22 - 11:24]

what breaks first?

### [11:24 - 11:26]

Like, what is the failure mode of the model?

### [11:26 - 11:30]

Is it more visual coherency or temporal coherency?

### [11:31 - 11:33]

Are you saying what is the general failure modes

### [11:33 - 11:34]

of doing parallel inference?

### [11:34 - 11:39]

Yes, I think the main thing is that you generate

### [11:39 - 11:41]

incoherent features because you're still doing

### [11:41 - 11:42]

sampling independently.

### [11:42 - 11:44]

So if you want to do joint sampling,

### [11:44 - 11:47]

you would have to, like, for, like, n tokens in once,

### [11:47 - 11:50]

you would have to somehow create a probability distribution

### [11:50 - 11:52]

over v to the n, which is basically impossible.

### [11:52 - 11:54]

So yes, I think the main thing is that you get distorted

### [11:54 - 11:58]

features, and that's the main thing that, like,

### [11:58 - 12:01]

our locality where generation order tries to solve.

### [12:01 - 12:03]

Thank you.

### [12:03 - 12:08]

Yeah, you can go behind the mics and then ask your questions.

### [12:08 - 12:10]

Does this work?

### [12:10 - 12:10]

Does it work?

### [12:10 - 12:11]

Yes.

### [12:11 - 12:15]

Thank you for the great talk, really cool work.

### [12:15 - 12:18]

So you said that the joint sampling doesn't work

### [12:18 - 12:20]

with the autoregressive transformer, but, I mean,

### [12:20 - 12:22]

you could technically also do autoregressive

### [12:22 - 12:23]

generation with diffusion models, right?

### [12:23 - 12:26]

So MAR, I just wonder, like, have you

### [12:26 - 12:29]

any intuition about how that would work in comparison,

### [12:29 - 12:32]

if you would use the same strategies,

### [12:32 - 12:36]

like the same orderings with a diffusion model?

### [12:36 - 12:38]

Because then you can essentially sample

### [12:38 - 12:40]

from the joint distribution of multiple tokens

### [12:40 - 12:41]

at the same time.

### [12:41 - 12:42]

Yeah, that's a good point.

### [12:42 - 12:44]

So I think with diffusion models,

### [12:44 - 12:46]

they're very heavily compute bound.

### [12:46 - 12:48]

So at high batch sizes, they're actually pretty low throughput.

### [12:48 - 12:52]

And I didn't put MAR in our efficiency benchmarks,

### [12:52 - 12:59]

but MAR itself is slower than the pure autoregressive approach,

### [12:59 - 13:01]

mainly because of the diffusion head.

### [13:01 - 13:05]

So yes, you can sort of emulate this with diffusion,

### [13:05 - 13:08]

but you end up with a trade-off that's actually worse than not

### [13:08 - 13:10]

doing it in the first place.

### [13:10 - 13:12]

And most of the latency in MAR, for example,

### [13:12 - 13:15]

is actually the diffusion head, and the autoregressive time

### [13:15 - 13:18]

actually doesn't take that much.

### [13:18 - 13:19]

OK, thank you.
