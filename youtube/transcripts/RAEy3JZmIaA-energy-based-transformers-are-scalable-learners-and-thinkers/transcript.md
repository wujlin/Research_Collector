# Energy-Based Transformers are Scalable Learners and Thinkers (Paper Review)

- URL: https://www.youtube.com/watch?v=RAEy3JZmIaA
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-05T12:51:35`

## Transcript

### [00:00 - 00:08]

Hello, how's it going? Today we're going to look at this paper right here, Energy-Based Transformers are Scalable Learners and Thinkers.

### [00:08 - 00:24]

This paper combines the general concept of energy-based models with transformers and suggests a learning paradigm for it and shows how that learning paradigm applies and how it can be made scalable.

### [00:24 - 00:49]

With it, they do achieve some pretty promising results in that the experiments are on smaller scale data, but in terms of language modeling, video modeling, and things like this, the scaling trends show that this actually might be a more scalable architecture and a more promising architecture once you do go large scale.

### [00:49 - 00:54]

So, I would say this is a pretty interesting direction of research.

### [00:54 - 01:04]

And promising, although not obviously verified yet at scale, but I think that's what does make it interesting.

### [01:04 - 01:15]

It's a bit different from what you're used to, but it also goes back to concepts that have been around for a while, and I'm very happy to see more energy-based modeling work here.

### [01:16 - 01:17]

So, let's dive in.

### [01:18 - 01:24]

The general concept that the authors here ask are, is it possible to generalize?

### [01:24 - 01:32]

Is it possible to generalize system-to-thinking approaches and develop models that learn to think solely from unsupervised learning?

### [01:32 - 01:35]

Very big and bold question, obviously.

### [01:36 - 01:40]

We're not talking about can we sort of build better models or something like this.

### [01:40 - 01:52]

No, we are going to system-to-thinking, which is sort of the more logical, slow thinking that humans do.

### [01:52 - 01:53]

And we're going to do...

### [01:54 - 01:55]

That in machines.

### [01:56 - 02:03]

And they here largely refer to inference time computation techniques, and we'll get to that in a bit.

### [02:03 - 02:12]

So, they're asking, can we teach computers how to do system-to-thinking, and can we do so without any supervision?

### [02:12 - 02:18]

So, from purely unsupervised learning and in a way that is generalizing.

### [02:19 - 02:20]

Again, very, very big question.

### [02:21 - 02:23]

So, why system-to-thinking techniques?

### [02:23 - 02:24]

Obviously.

### [02:24 - 02:35]

If you know from cognitive science, system-one thinking broadly refers to sort of quick and intuitive thinking.

### [02:36 - 02:42]

Now, this is how you do most of your day, how you go about it.

### [02:43 - 02:51]

If you're sort of, I don't know, want to eat a banana, like almost all of your actions are going to be system-one thinking.

### [02:51 - 02:54]

You sort of subconsciously walk to where...

### [02:54 - 02:57]

Or you store fruit, you subconsciously grab one.

### [02:57 - 03:01]

You don't have to think about walking, about extending your muscles.

### [03:01 - 03:06]

You may not even have to think of how to, you know, peel and eat and so on.

### [03:06 - 03:08]

All of this is just super subconscious.

### [03:08 - 03:12]

It's ingrained, and you don't have to think about it.

### [03:12 - 03:18]

However, system-to-thinking kicks in whenever system-one thinking is at its limits.

### [03:18 - 03:23]

Although, I'm going to guess it's debatable exactly what the difference is and if system...

### [03:23 - 03:24]

Whether system-to-thinking...

### [03:24 - 03:37]

System-to-thinking is sort of an extension of system-one thinking, whether there's a spectrum or whether this is something completely different that, you know, is totally separate and the two things work together.

### [03:37 - 03:38]

I have no idea.

### [03:39 - 03:44]

But in general, system-to-thinking is characterized by being slow and being explicit.

### [03:46 - 03:54]

So whenever you sort of, in your mind, talk to yourself and then sort of work through a logical series...

### [03:54 - 03:58]

...of steps to arrive at a conclusion, that would be system-to-thinking.

### [03:59 - 04:08]

And reasonably said, the authors here say most of machine learning so far has been largely in the domain of system-one thinking.

### [04:09 - 04:11]

There is a bit of debate about that.

### [04:11 - 04:22]

So some people show that, for example, if you have a transformer and that transformer has many, many layers and you put, like, a piece of language down here...

### [04:22 - 04:24]

...and up spits the next token.

### [04:24 - 04:30]

In here, you have multiple steps of computation given by layer, by layer, by layer.

### [04:30 - 04:41]

And therefore, it's completely conceivable that there is one or another form of, quote-unquote, thinking happening there, however you want to define that.

### [04:41 - 04:54]

However, largely, you could say that sort of building a model and then doing a forward pass and taking its output, that's kind of analogous to the system, system-one thinking.

### [04:54 - 05:01]

Whereas system-two thinking is much more if you sort of do that explicit.

### [05:01 - 05:07]

So let's say you do have that transformer, but you use it to do chain-of-thought prompting.

### [05:07 - 05:15]

So you input something and the transformer outputs thinking tokens that refer back to itself, obviously.

### [05:15 - 05:22]

So, not refer back to itself, you autoregressively feed the thinking tokens into the transformer and so on.

### [05:22 - 05:24]

So you would produce an entire sequence.

### [05:24 - 05:27]

You use the transformer over and over and over again.

### [05:27 - 05:31]

And you have some explicit thinking going on right here.

### [05:33 - 05:39]

And eventually, your output would rely on the fact that you have done that thinking.

### [05:40 - 05:54]

The authors here largely go for the approach where they say the moment you use a trained model at inference time more than once, sort of,

### [05:54 - 05:54]

...

### [05:54 - 06:03]

the moment you put more computation into getting an answer from the model than simply doing a single forward pass.

### [06:03 - 06:07]

That is part of what they call thinking.

### [06:07 - 06:15]

Again, thinking is a big word, but to them, and that's only really at the end of the paper, thinking is actually not even an act.

### [06:15 - 06:16]

It's a metric.

### [06:16 - 06:24]

And their metric of thinking is really sort of how much better can we get by doing multiple forward passes?

### [06:24 - 06:32]

Through models, rather than a single forward pass, you might already know a couple of models that do this, apart from autoregressive transformers.

### [06:33 - 06:48]

So, for example, recurrent neural networks sort of intuitively do some sort of multiple forward passes, although you could debate that and say processing an entire sequence is simply one forward pass.

### [06:48 - 06:51]

Other models, you could say, are diffusion.

### [06:51 - 06:53]

So diffusion models.

### [06:53 - 07:00]

So diffusion models also do multiple forward passes through a model in order to arrive at their output.

### [07:00 - 07:08]

Again, you might debate that and say, no, no, no, actually, that's just that's just one forward, one overarching forward pass.

### [07:08 - 07:13]

That's just kind of one inference through the model is, well, you do all these computations.

### [07:14 - 07:19]

So, again, all of this is debatable, but I'll leave it at that.

### [07:19 - 07:23]

You make your own decisions about what thinking is and what it means.

### [07:23 - 07:23]

And what it means.

### [07:23 - 07:23]

And what it means.

### [07:23 - 07:23]

And what it means.

### [07:23 - 07:26]

And which models are doing thinking and which ones aren't.

### [07:27 - 07:32]

This paper right here is looking at energy-based models.

### [07:33 - 07:40]

And the way you do inference in energy-based models is that you do multiple forward passes.

### [07:41 - 07:49]

And that's why they call their energy-based transformer variants thinkers, because it does that.

### [07:49 - 07:53]

Because you can put more compute in and you get.

### [07:53 - 07:56]

A quote-unquote better answer.

### [07:57 - 07:57]

All right.

### [08:00 - 08:02]

Yeah, here, this is a bit illustrated.

### [08:03 - 08:11]

So in an autoregressive transformer, you would simply have your sequence and you would predict the next token in an RNN.

### [08:11 - 08:12]

You do do multiple computations.

### [08:13 - 08:16]

But again, you take your sequence, you predict the next token here.

### [08:16 - 08:22]

A diffusion transformer obviously does some reverse inference here.

### [08:22 - 08:23]

And in energy.

### [08:23 - 08:26]

Energy-based transformer will get to that in one second.

### [08:28 - 08:33]

They also talk about sort of the current trend of reasoning models.

### [08:33 - 08:41]

And those reasoning models, again, they largely are trained with chain of thought prompting and things like that using reinforcement learning.

### [08:41 - 08:51]

So they're saying that this usually only works in domains where rule-based rewards can easily verify answers, such as math and coding.

### [08:52 - 08:53]

So you.

### [08:53 - 09:07]

Are only it's only applicable to a small range of problem types, meaning that, yes, you can do reinforcement learning, but you somehow you have to give a reward and that reward usually is derived algorithmically.

### [09:07 - 09:20]

So you give it a math puzzle and you already know the answer, or you give it a coding puzzle and you can verify that the unit tests pass or that it compiles or that it gives the correct output.

### [09:20 - 09:22]

So reinforcement learning is fantastic.

### [09:22 - 09:23]

But other than that.

### [09:23 - 09:26]

If you don't have supervised data, you're kind of out of luck.

### [09:27 - 09:29]

So we need things.

### [09:30 - 09:40]

We need to train these models in a way that they are able to do inference time compute without necessarily relying on reinforcement learning.

### [09:41 - 09:53]

Although what you'll see is that even though they contrast what they're doing with all of these models right here, there's actually not nothing stopping us from combining the.

### [09:53 - 09:53]

Two.

### [09:53 - 10:10]

To me, reasoning as the models currently do chain of thought and all of that is completely orthogonal of what these energy based models do, and it's quite conceivable that the energy based models are also being used to do chain of thought.

### [10:10 - 10:23]

All right, again, their central question, can we rely entirely on unsupervised learning to develop system to thinking this such a capability?

### [10:23 - 10:23]

Would.

### [10:23 - 10:32]

Enable generalization of current system to thinking approaches to any problem, any modality and avoid the reliance on external human reward or model supervision.

### [10:33 - 10:37]

For that, they say, OK, there are three key facets of system to thinking.

### [10:38 - 10:45]

And from now on, when you hear system to thinking, just sort of think the goals of their like what I'm pretty sure.

### [10:46 - 10:48]

And I obviously have no proof of that.

### [10:48 - 10:51]

What I'm pretty sure is that they started from the models.

### [10:51 - 10:52]

They first developed energy based transformers.

### [10:52 - 10:53]

Right.

### [10:53 - 11:00]

Because energy based models are an idea and transformers are an idea and you combine them, you define energy based transformers.

### [11:00 - 11:04]

And then they sort of worked backwards and said, oh, what are the properties of these models?

### [11:05 - 11:13]

And, oh, those just magically happen to be the three key facets of system to thinking.

### [11:13 - 11:13]

Right.

### [11:13 - 11:15]

I don't really buy that.

### [11:15 - 11:18]

I think there was some reverse engineering happening right here.

### [11:19 - 11:23]

So just take these as three nice properties of energy based.

### [11:23 - 11:30]

Models rather than system to thinking dynamic allocation of computation in an energy based model.

### [11:30 - 11:37]

And you'll see that you can choose how much computation you want to invest into inference time.

### [11:38 - 11:50]

So if you have an energy based transformer and that is a model on language and you wanted to predict the next token, you are not limited to just one forward pass.

### [11:50 - 11:52]

You can put in more computation.

### [11:53 - 11:57]

And get a more accurate distribution over what that next token should be.

### [11:58 - 12:03]

Facet two, modeling uncertainty in continuous state spaces.

### [12:03 - 12:13]

Again, this is a property of energy based models that they can give you a notion of uncertainty in their in their predictions.

### [12:14 - 12:22]

And so EBMs naturally can naturally model uncertainty with how to have without having to model exact likelihoods by modeling the relative

### [12:22 - 12:25]

unnormalized likelihoods of predictions.

### [12:27 - 12:41]

As the real world often contains many inherently unpredictable elements, for instance, when a pedestrian might emerge from behind a parked vehicle, the ability to express uncertainty in predictions is essential to being cautious and is a natural capability of humans.

### [12:42 - 12:46]

And then facet three, verification of predictions.

### [12:46 - 12:50]

So in an energy based model, we are doing a little bit.

### [12:51 - 12:51]

Uh,

### [12:51 - 13:13]

what you might be used to from, from GANs, from generative adversarial models, where there is a verifier or a discriminator involved, so a model that can assess how good, quote unquote, something is, and so naturally, energy based models have this inherent ability to not just predict, but judge predictions.

### [13:18 - 13:20]

So how do we do this here?

### [13:20 - 13:20]

Again,

### [13:20 - 13:28]

you will have an inference across an energy based models, you can see, this is next token prediction.

### [13:28 - 13:39]

So you do have your context, the dog caught the, and then the question is, in an energy based model, how do you how do you get a prediction out for the next token?

### [13:40 - 13:49]

And the way we're going to do this is we're not just going to predict a token, but we're going to output an entire distribution over tokens.

### [13:49 - 13:50]

Now,

### [13:50 - 13:50]

this is still

### [13:50 - 13:55]

the same as in a classic transformer, and it also outputs a distribution over tokens.

### [13:55 - 13:57]

But the way we do it is different.

### [13:57 - 14:02]

The way we do it is we actually going to start with a completely random distribution.

### [14:02 - 14:14]

And then we're going to step by step, refine that distribution, and and sort of shape that distribution until we end up with our final distribution.

### [14:14 - 14:20]

And again, we can choose to do this for longer, and get a more accurate output.

### [14:20 - 14:24]

Or we can choose to do this for shorter and get a less accurate output.

### [14:25 - 14:32]

This, again, might remind you of diffusion models, but it's a bit different of how we do it here.

### [14:32 - 14:39]

But just be mindful that the way we produce outputs is not through a forward pass, and then we have the output.

### [14:39 - 14:42]

But the way we produce outputs is we start with something random.

### [14:42 - 14:50]

And then there's a process that obviously involves the model that allows us to step by step by step shape.

### [14:50 - 14:51]

The outputs.

### [14:52 - 14:53]

Now,

### [14:56 - 14:59]

yeah, again, so this paper is laced with philosophy.

### [15:00 - 15:12]

We propose viewing thinking as an optimization procedure with respect to a learned verifier, which evaluates the compatibility between an input and candidate prediction.

### [15:14 - 15:15]

So,

### [15:16 - 15:17]

yeah,

### [15:17 - 15:20]

they, they propose viewing thinking

### [15:20 - 15:36]

like the giant word and concept of thinking to happen to exactly align with what energy based models are doing, which, yeah, again, I strongly feel there's a degree of reverse engineering happening right here.

### [15:37 - 15:42]

All right, I promised you no more philosophy, and we'll dive into the models themselves.

### [15:42 - 15:48]

So what is an energy based model and and what how do you how do you go about?

### [15:49 - 15:50]

How do you go about doing?

### [15:50 - 15:51]

Inference in one.

### [15:51 - 15:58]

So an energy based model is some something that works together with what you call an energy function.

### [15:58 - 16:02]

So an energy function, typically, maybe called E has two inputs.

### [16:03 - 16:05]

So let's call it x and y.

### [16:07 - 16:07]

And

### [16:09 - 16:17]

the energy function is supposed to tell you is supposed to give you a high number.

### [16:17 - 16:18]

If

### [16:18 - 16:20]

x and y,

### [16:20 - 16:28]

sort of are compatible in some way and draw a heart right here, and it's going to give you a low now wait, all the way around.

### [16:28 - 16:29]

See,

### [16:30 - 16:34]

low energy means they go together.

### [16:34 - 16:35]

They're nice, they're close.

### [16:36 - 16:37]

They just fit.

### [16:37 - 16:39]

Just fits, right?

### [16:39 - 16:49]

And then the high number if x, let me draw a little lightning and why they don't like each other.

### [16:49 - 16:56]

they don't go together. Now, you might complain that this is still an incredibly abstract concept.

### [16:56 - 17:02]

And that is true. It obviously depends on what you want to do. So let's say you want to do next

### [17:02 - 17:11]

token prediction, right? X would be the context, the prompt, whatever you want, like the partial

### [17:11 - 17:22]

text, and Y would be a distribution over the next token, right? Like a distribution over

### [17:22 - 17:29]

vocabulary that represents what the next token should be. So the energy would be low, if that

### [17:29 - 17:35]

distribution points only to tokens that are actually, you know, valid in the language as

### [17:35 - 17:41]

continuations for X, and it would be high if that distribution is somehow different.

### [17:41 - 17:41]

If

### [17:41 - 17:49]

you were doing image denoising, then X would be the noised image, and Y would be the denoised

### [17:49 - 17:56]

image of the same image. However, if X is the noised image, but Y is a different denoised

### [17:56 - 18:04]

image, that energy would need to be high. So the energy function is what we train, right?

### [18:04 - 18:11]

And that is a parameterised function. And that's going to be a transformer in this case,

### [18:11 - 18:20]

so we're going to have a transformer model, so that the whole model here is going to be this

### [18:20 - 18:25]

energy function, we're not going to need an additional model than this, this is the entirety

### [18:25 - 18:32]

of the learned parameters. This is different than a GAN. In a GAN, this will be the discriminator,

### [18:32 - 18:38]

and you would still need to train a generator to work against the discriminator. In an energy based

### [18:38 - 18:41]

model, the energy, the energy, or the energy function is going to be the discriminator. So

### [18:41 - 18:46]

as I mentioned earlier, at least in this formulation here, the energy function is all you need. And the

### [18:46 - 18:54]

energy function is what you are training. So you are training, you are training a parameterised

### [18:54 - 19:00]

representation of a function that and then you beat it with data, you're gonna Okay, here is here

### [19:00 - 19:07]

is a sentence, the dog, blah, blah, blah. And here is a distribution over next tokens. And you

### [19:07 - 19:11]

train it to be lo if they go together, and you train it to be low, and you train it to be low.

### [19:11 - 19:18]

it to be high if they don't go together you can do this in various ways right you and we get to

### [19:18 - 19:25]

that later one easy way is to do contrastive training so you take the same context and you

### [19:25 - 19:29]

take the distribution the one hot distribution of the correct next token and then you take a

### [19:29 - 19:34]

one hot distribution over the incorrect next token and you do a contrastive training you say

### [19:34 - 19:46]

the correct um the correct the the the output where these two are where this is the correct

### [19:46 - 19:52]

next token should be lower than the output of these two where this is the incorrect next token

### [19:52 - 19:59]

however that is not a scalable way to go about it and we'll see later so the energy function is the

### [19:59 - 20:04]

the only thing we need um so you might object and say hey

### [20:04 - 20:04]

you

### [20:04 - 20:11]

what's the difference to loss uh because like a that that just seems very much like like loss

### [20:11 - 20:19]

the loss function is also exactly like this right um and the difference is when you use it so an

### [20:19 - 20:26]

an energy function you are supposed to use at inference time whereas a loss function you're

### [20:26 - 20:32]

supposed to use at training time in fact training the energy function here training these parameters

### [20:34 - 20:34]

itself

### [20:34 - 20:41]

itself has a loss function associated with it right so um the loss function in the contrastive

### [20:41 - 20:48]

training might actually be so the loss function might actually be that the energy of x and y1

### [20:48 - 20:53]

must be lower or like

### [20:53 - 21:03]

minus the energy x and y2 right this would encourage this to go down and this to go up

### [21:04 - 21:08]

and that's what we want because this is the correct one and this is the incorrect one

### [21:09 - 21:16]

so a loss function is a is a training objective and an energy function is an inference objective

### [21:16 - 21:21]

and that also gives you a hint of what do you actually do with this energy function

### [21:21 - 21:28]

so we we only train a model to predict a single number right this thing here this is going to be

### [21:29 - 21:34]

a real number it's not going to be an output of anything it's going to be a number

### [21:34 - 21:41]

and so what do you do if i only give you a function that where you can put in the current

### [21:41 - 21:47]

half sentence and then a distribution across like across the next so here is the current half

### [21:47 - 21:52]

sentence and this here is a distribution over the next token and i'm simply going to tell you a

### [21:52 - 22:00]

number and that number is going to be higher if it's bad and lower if it's good well if you just

### [22:00 - 22:04]

have that you're simply going to take the same half sentence and then you're going to put in a

### [22:04 - 22:09]

and then you're just going to try a whole bunch of these distributions right and you're going to

### [22:09 - 22:16]

see okay which one is the lowest so you you may be able to one hot encode all your vocabulary and

### [22:16 - 22:22]

just slap everyone in and then seeing which one is the lowest but in fact that's not the whole space

### [22:22 - 22:27]

of distribution because distributions can be obviously not just one hot so you could think

### [22:27 - 22:33]

of just slapping in every possible distribution and finding the lowest value right there

### [22:34 - 22:40]

and now we come to the point where you might recognize hey this sounds a lot like optimization

### [22:40 - 22:45]

and that's exactly how we go about it so if you think of it if you think of it

### [22:49 - 22:53]

if you have a trained energy function and that trained energy function is

### [22:53 - 22:59]

such that if things go together that the the energy function actually tells you yes this is

### [22:59 - 23:04]

lower that's if your energy function is well trained you're going to have that

### [23:04 - 23:17]

um so if you do have that then um you can simply run an optimization procedure at inference time

### [23:17 - 23:24]

in order to get a good output what do i mean so look at this this here is um a 2d representation

### [23:24 - 23:32]

of the of a uh energy landscape again this is not loss this is at inference time

### [23:32 - 23:39]

so imagine that this axis here is uh this is a bit of a fat

### [23:42 - 23:48]

imagine that this axis here is um is your

### [23:49 - 23:56]

your your uh context right this is all the possible contexts

### [23:57 - 24:01]

no actually what you can do is if you if oh yeah okay

### [24:02 - 24:10]

axis here is all the possible contexts, right? They are discrete, I get it. But we'll just we'll

### [24:10 - 24:15]

just say, okay, these these possible contexts are continuous. So that's our x. And then here

### [24:15 - 24:23]

are all the possible distributions, like next token distribution, right? So this distribution

### [24:23 - 24:29]

right here might be here. And then very, you know, like very spiky distribution or something

### [24:29 - 24:36]

might be here. And so on. And you can see if the energy function is well trained, what we're

### [24:36 - 24:45]

trying to find are the minima of the energy function, given one of the one of the inputs

### [24:45 - 24:54]

is actually our x. So we fix the x, and we change the y, and we run an optimization procedure over

### [24:54 - 24:58]

the y. So in this case, I've actually done the wrong drawing. So

### [24:58 - 24:59]

both

### [24:59 - 24:59]

are

### [24:59 - 25:06]

of the axis right here should obviously, this should be y, one, what, like this, these are,

### [25:06 - 25:12]

these are now individual dimensions over your history over your distribution,

### [25:12 - 25:23]

this distribution space. Now the distribution is obviously way, way more high dimensional. In fact,

### [25:23 - 25:28]

it has the dimensionality of the whole vocabulary. But imagine your vocabulary just has like,

### [25:28 - 25:36]

three different entries. So because you need to normalize it, it's a two dimensional space. And,

### [25:36 - 25:41]

and that's what you optimize over here. So you're trying to do to find the minima. And how do you do

### [25:41 - 25:48]

that? Well, by doing gradient descent. So we're doing we're starting in a random output, a random

### [25:48 - 25:55]

distribution over the next token. And then we're doing gradient descent on the energy function,

### [25:55 - 25:57]

back propagating that to,

### [25:58 - 26:04]

flight down, and you would just realize that if we take the energy function, we're going to go through the-

### [26:05 - 26:13]

the input right here, again, we have an x and we have a y like an estimate of y, an initial guess, or an

### [26:13 - 26:19]

intermediate step, we're putting both of these through a multi layer transformer, that gives us an energy

### [26:19 - 26:27]

function. And then we're going to take that energy function, we're going to calculate the gradient of the

### [26:27 - 26:28]

energy,

### [26:28 - 26:36]

through the transformer to here. So this is going to be the gradient with respect to y hat

### [26:36 - 26:45]

of our energy function, where x is fixed, right, like x is fixed. And we want to know how do we

### [26:45 - 26:51]

need to change y hat. And then we do a little step in that direction. And then we re evaluate it. And

### [26:51 - 26:56]

then we do a little step and we re evaluate it. Cool. So we're doing gradient descent at inference

### [26:56 - 27:04]

time. That's at least one way of doing inference in energy based models. Okay, we optimize against

### [27:04 - 27:09]

the energy function, you can see that this has some nice properties, like if this is well behaved,

### [27:09 - 27:16]

then if we do some wiggling around here, we can get sort of the variance of stuff, we can get the

### [27:16 - 27:24]

uncertainty, right? Is it very wide? Is it very narrow? Is it very bumpy, and so on. We can also

### [27:24 - 27:26]

easily record more easily.

### [27:26 - 27:33]

recognize out of distribution data, and things like this. So a lot of excellent properties. But

### [27:33 - 27:39]

the downside is we can't just get a poof, an output in a single step, we do have to run this

### [27:39 - 27:47]

optimization procedure. Alright, so how do you? How do you train this? How do you train a model?

### [27:47 - 27:54]

Oh, by the way, energy is not not a normalized quantity. So energies are always unnormalized

### [27:54 - 27:56]

for scalability.

### [27:56 - 28:05]

reasons. So all you really know is, is it less? Is it more? Yeah, so this will be the inference

### [28:05 - 28:10]

procedure, we're going to do we're going to we're going to sample some initial guests, and then

### [28:10 - 28:16]

we're going to run gradient descent on the energy function with like some some step size right here.

### [28:16 - 28:26]

And we're going to return the minimum that we found along the way. Okay. Again, this is the

### [28:26 - 28:35]

way we do inference. So how do we train a model, and there are some challenges right here. And the

### [28:35 - 28:41]

challenges are that if you just naively train the energy function to be sort of high on incompatible

### [28:41 - 28:47]

inputs, and low and compatible inputs, you are going to end up with a very, very jagged and a

### [28:47 - 28:56]

very non smooth energy landscape, right? This is it's just going to be like, okay, a lot of level and then wherever your

### [28:56 - 29:02]

data is, and then especially in high dimensions. So therefore, what is really important are some

### [29:02 - 29:08]

energy landscape regularization techniques to be applied. They have three of them.

### [29:09 - 29:16]

One is a replay buffer. And that's also often used in reinforcement learning where you have

### [29:16 - 29:22]

your trajectories, and you sort of keep them around to grab them to train. And you usually

### [29:22 - 29:28]

do that just to bring some variety into the into the system and get away from your very,

### [29:28 - 29:36]

very local state and current data. Another thing is, they actually, they add noise here. And it's

### [29:36 - 29:46]

probably good, because I forgot one thing. And that is, yeah, how do you train? And the trick

### [29:46 - 29:50]

here is that you train

### [29:50 - 29:52]

quickly.

### [29:52 - 29:58]

Considering the way you do inference, there are two ways to train, or this paper says,

### [29:59 - 30:02]

okay, there are two ways to train this thing. One is contrastive, we already looked at that.

### [30:02 - 30:08]

What is the other one? Well, the other one is saying, hey, my inference, my ultimate y is going

### [30:08 - 30:21]

to be I am, my ultimate y is going to be y zero minus alpha gradient of energy of x y zero.

### [30:22 - 30:51]

This is just a single step, right? I've done a single step of gradient descent optimization. But you can see, well, this is my output, right. And, and therefore, if I now define a loss function on my output, right, and so I've defined a loss function on y, and y, what's the correct one, the correct one, y from my, from my data set, right. So this is the distribution over the next token.

### [30:51 - 30:52]

Here.

### [30:52 - 31:22]

And this is the actual next token, one hot encoded, I can define a cross entropy loss. And I can use this here. As the, this is effectively f of, what is it? f of x, I guess, y equals f of x. Yeah. So. So if, if you didn't know how this came about, what would you do, you would simply say, okay, let's do this.

### [31:22 - 31:38]

let me, let me derive the gradient, right here, f has parameters. Let me derive the gradient of the parameters of the loss of f, of x, and y y, of the correct label. And you would back propagate into f and you would back propagate through that to the parameters of f, you can do that here, here's some parameters. This is a completely linear operation, this here is a completely linear operation, and then you could go back to the derisive property and do that. you can do that after you've

### [31:52 - 31:58]

linear, I'm not sure, derivable operation. And so what you end up doing is you end up actually

### [31:58 - 32:06]

back propagating through your optimization steps. So you're going to back propagate through

### [32:06 - 32:11]

an operation, which already has a gradient computation inside. And you know what that

### [32:11 - 32:17]

means, that means you actually need second order derivatives right here. However, the second order

### [32:17 - 32:26]

derivatives aren't too bad. Because you can do in this in this case, so you require. So importantly,

### [32:26 - 32:30]

this loss is back propagated through the entire optimization process requiring second order

### [32:30 - 32:37]

derivatives, i.e. gradients of gradients. These are computed efficiently via Hessian vector products,

### [32:37 - 32:44]

which scale linearly with model size. So it's not the most flop efficient thing in the world,

### [32:44 - 32:46]

but it doesn't quadratically.

### [32:47 - 32:54]

explode. If you if you scale up. So again, like this might be a bit weird to people who are really

### [32:54 - 33:03]

just used to training forward past transformer models. But we are we're going to train, we're

### [33:03 - 33:12]

going to train such that the ultimate the inference process itself is considered during the

### [33:12 - 33:17]

training. So the training consider the training is, okay, the loss represents

### [33:17 - 33:19]

we didn't things about what we lost our ди terrorist and we actually lost também parece Imagine

### [33:19 - 33:26]

finding a good output, including that inference time gradient descent process. So we train with the

### [33:26 - 33:32]

inference in mind and now into make that scalable we do need to regularized and one part of

### [33:32 - 33:34]

we will take the mom of just regularization. is to add this

### [33:34 - 33:35]

We need to add it to the text of the bars, this

### [33:35 - 33:36]

noise right here. So when

### [33:36 - 33:40]

we do the gradient descent at training time right at training time, we're

### [33:40 - 33:45]

also going to do this gradient descent. So we have some sort of energy landscape. We're going to do the

### [33:45 - 33:46]

grad encland, I would say gradient descent. We want to have, we want to have a grad end, you see a gradient emphasis on that. Good.

### [33:46 - 33:52]

gradient descent, like boop, boop, boop, okay, going here, and then calculating the loss of this,

### [33:53 - 34:00]

and then back propagating through this inference right here, we are going to also add noise to

### [34:00 - 34:07]

every one of those steps. And the reason is, this helps generalization, and this helps smoothness.

### [34:07 - 34:14]

So if you are here, let's say this is a top view, and your optimization path looks like this,

### [34:14 - 34:22]

what you really want is you want by doing noise, you're sort of washing this out a little bit,

### [34:22 - 34:29]

right. And so instead of treading a path that is sort of really thin, right here, and the rest,

### [34:29 - 34:36]

you know, here and here is undefined, you want to, you want to make that path bigger, you want to

### [34:36 - 34:43]

sort of broaden the landscape where you reach during training. And by that you make the landscape

### [34:43 - 34:44]

smoother.

### [34:44 - 34:50]

And you do sacrifice a bit of accuracy, obviously, for this, but you make the landscape a lot

### [34:50 - 34:57]

smoother by adding this noise during training. And so at inference time, when, and we're looking

### [34:57 - 35:02]

for generalization here, so data that we haven't seen during training time, if at inference time,

### [35:02 - 35:08]

data is close to what you've seen during training, you are not hopelessly lost, because you will

### [35:08 - 35:14]

still be inside of this sort of more wide band that you've seen, and you'll be able to follow,

### [35:14 - 35:18]

and make something sensible out of that inference time data.

### [35:21 - 35:28]

Very old trick to add noise, obviously, but very effective. And they do this here as well. The other

### [35:28 - 35:35]

one is by randomizing the gradient step size, and the number of optimization steps significantly

### [35:35 - 35:42]

improved generalization. Again, the you don't always want to do exactly five steps with exactly

### [35:42 - 35:43]

the same step size,

### [35:43 - 35:43]

if you vary

### [35:43 - 35:54]

things up a bit, then you you can obviously gain a lot. And even additionally here, because we are

### [35:54 - 36:00]

putting in compute at inference time, because we're doing multiple forward passes, if I already

### [36:00 - 36:09]

train doing sometimes less, sometimes more optimization steps, I will end up with a model that

### [36:09 - 36:13]

is much more accustomed to sort of giving me giving me good

### [36:13 - 36:13]

answer.

### [36:13 - 36:18]

Here, we have all the parameters for all of these situations. And that hopefully generalizes to a way

### [36:18 - 36:24]

where I could then also extrapolate at that inference time, put in a lot more steps than I've

### [36:24 - 36:31]

done during training stem time, just because I have sort of trained the model to be flexible to

### [36:31 - 36:39]

how many steps I do. And I hope that in itself obviously generalizes. So those are the training

### [36:40 - 36:43]

techniques that they have right here. And then they also introduce some kind of a set of parameters,

### [36:43 - 36:50]

their model. So their model is a transformer. So they're introducing, they're combining effectively

### [36:50 - 36:55]

energy-based modeling with transformers. And they're saying, okay, energy-based models have

### [36:55 - 37:02]

traditionally encountered difficulties with three characteristics, which are parallelizability,

### [37:03 - 37:09]

stability, and scalability. So energy-based models, really bad at this. Transformers,

### [37:09 - 37:17]

really good at this. So transformers are good in all of these three things that the energy-based

### [37:17 - 37:25]

models are bad at. And so it seems natural that they go together. So they present EBT's energy-based

### [37:25 - 37:33]

transformers, which are transformer implementations designed for EBMs. This is a challenge from an

### [37:33 - 37:39]

engineering perspective, especially the sort of decoder-only triangular attention.

### [37:39 - 37:45]

And transformers need a lot of considerations so that you don't get information leakage across

### [37:45 - 37:51]

these multiple inference steps that you do in EBM. So you no longer just do one forward pass,

### [37:51 - 37:57]

you do multiple. And if you want to benefit from that parallelizable training, and if you want to

### [37:57 - 38:03]

benefit from sort of doing parallel computation with this triangular attention, you have to

### [38:03 - 38:09]

pay very, very close attention to how your data flows. They've implemented

### [38:09 - 38:16]

all of this and their code is available, so that is very, very cool. They're going to research two

### [38:16 - 38:21]

different things here in the experimental section. One is learning scalability, which is sort of the

### [38:21 - 38:26]

traditional thing, which is how quickly can models fit the pre-training data. And the other one is

### [38:26 - 38:32]

what they call thinking scalability. This is effectively, can we determine whether model

### [38:32 - 38:38]

performance improves with increased thinking? And by that, they mean increased number of forward

### [38:38 - 38:39]

passes at inference.

### [38:39 - 38:48]

So if we put in more compute, can we get sort of better? And can we get better in a more scalable,

### [38:48 - 38:54]

in a more rapid way than other models? So the first thing is they compare with this with

### [38:54 - 39:02]

transformer plus plus, that's a sort of a training recipe to train next token prediction, single

### [39:02 - 39:07]

forward pass transformers. And you can see right here from these graphs that indeed, while the

### [39:07 - 39:08]

energy-based

### [39:09 - 39:18]

transformer does start out on a bit of a disadvantage, it quickly gains over the classic

### [39:18 - 39:25]

transformer as you, for example, scale up training data, scale up batch size, and scale up the

### [39:25 - 39:32]

depth. Again, these models, like what we're doing, like what they're doing is they're effectively

### [39:32 - 39:38]

showing like, look, the trends are really good. Some of these trends aren't that, you know,

### [39:38 - 39:39]

materialized.

### [39:39 - 39:45]

Like you would need to extrapolate somewhere down here to actually see. And there is still the

### [39:45 - 39:52]

absolute possibility that at large scale, none of this trends actually go the way that they seem to

### [39:52 - 40:00]

go. But still, it's quite, it's quite promising. So this is training scalability, where the energy

### [40:00 - 40:08]

based transformers already sort of scale better. Now, keep in mind, the x axis right here,

### [40:09 - 40:16]

the x axis represent, you know, very particular quantities. The fact of the matter is still that

### [40:16 - 40:21]

in a regular transformer, one forward pass, one training step is one forward pass. And in an

### [40:21 - 40:26]

energy-based model, one training step means you first have to do the inference procedure

### [40:26 - 40:32]

during the forward pass. And then you have to back propagate through that inference procedure,

### [40:33 - 40:39]

which all in all is not, you know, it's quite a bit more brr on your GPU,

### [40:39 - 40:45]

than a single forward pass transformer. So the x axis here, if they're like, okay, batch size,

### [40:45 - 40:52]

number of tokens, and so on, that's all fine. In the time domain, you'll see this is quite,

### [40:53 - 40:58]

and that's what we have right here. So you can see in terms of training flops, there is, and this is

### [40:58 - 41:06]

a log scale, right? The energy-based transformers are significantly away from the classic transformer.

### [41:06 - 41:09]

However, they scale.

### [41:09 - 41:16]

scale faster, what they mean is that this slope right here is ever so slightly. And you can also

### [41:16 - 41:22]

see that right here, but this is embedding dimension. Let's stay with flops, the slope here

### [41:22 - 41:29]

is ever so slightly steeper than the slope here. And therefore, if this trend continues,

### [41:29 - 41:37]

there's actually a future where, because energy-based models achieve better perplexity,

### [41:37 - 41:38]

you know,

### [41:39 - 41:47]

the additional flops sort of cancel out, and, and the, you would need to invest a lot more training

### [41:47 - 41:52]

flops into classic transformers than into energy-based transformers, because the energy-based

### [41:52 - 41:59]

transformers are just so better at, at sort of taking in those, making use of those flops. So not

### [41:59 - 42:06]

at this scale, but conceivably, if you believe the trends and you extrapolate, then that will at some

### [42:06 - 42:07]

point cross.

### [42:09 - 42:14]

So the second part is thinking the thinking. So

### [42:14 - 42:19]

at inference time, can we put in some more work? And their answer here is yes,

### [42:19 - 42:25]

indeed. So you can see, while the classic transformer obviously does not scale with number

### [42:25 - 42:29]

of forward passes is going to for the same input is going to give you the same output, no matter

### [42:29 - 42:31]

how many forward passes you do.

### [42:32 - 42:38]

The energy-based transformer starts out weaker, but then as you increase the forward passes,

### [42:38 - 42:46]

it obviously gets stronger and that's not a not a surprise because you do start out with something

### [42:46 - 42:51]

completely random right and then after one forward pass you've done sort of one inference step one

### [42:51 - 42:59]

gradient descent step in the energy landscape and so you do need to do a couple to um to to get

### [42:59 - 43:06]

ahead and yeah they do end up ahead right here with a gap to the classic transformer

### [43:06 - 43:17]

another thing they can do is they can actually look at the energies uh sort of across thinking

### [43:17 - 43:24]

steps so how do the energies evolve and they see they see one thing and that is that different

### [43:24 - 43:30]

tokens um have different sort of um energies you can see here the light colors represent

### [43:30 - 43:36]

sort of lower energies and you can see that throughout the inference of a

### [43:36 - 43:36]

centroid and a centroid and a centroid and a centroid and a centroid and a centroid and a centroid

### [43:36 - 43:43]

sentence you do get significantly lower energies at tokens where they say okay it's it's a lot more

### [43:43 - 43:52]

clear it's a lot more easy also here I can see at easy words so to say energy being lower and

### [43:52 - 43:59]

that represents a degree of sort of self-assessment of these models on and and also an opportunity

### [43:59 - 44:07]

maybe for us to put in less energy on these steps so this ability to put in different amounts of

### [44:07 - 44:14]

energy different amounts of flops into the inference procedure combined with the fact that

### [44:14 - 44:21]

the energy function itself can tell you something about the current state of things and about the

### [44:21 - 44:27]

uncertainty and about the easiness could give rise potentially in the future to a very dynamic

### [44:27 - 44:28]

inference procedure

### [44:28 - 44:29]

where

### [44:29 - 44:29]

where

### [44:29 - 44:35]

you don't always have to do oh we always do 100 steps or something like this right it's it's a

### [44:35 - 44:42]

little bit the same idea as the sort of speculative decoding and things like this where oh because you

### [44:42 - 44:49]

can you know something more you can maybe save some computation what i find interesting is that

### [44:49 - 44:55]

the remarkable thing that there seems to be not a whole lot of difference beyond step beyond

### [44:55 - 45:02]

iteration one so obviously at iteration zero the energies are you know something very high right

### [45:02 - 45:07]

but then after iteration one you sort of seem to be in the minimum already and the further

### [45:07 - 45:14]

iterations they don't seem to do that much anymore this is i think confirmed by this plot right here

### [45:14 - 45:20]

where you do make the most gain at the beginning then again this is this is a very common in

### [45:20 - 45:24]

optimization um yeah

### [45:24 - 45:24]

yeah

### [45:24 - 45:25]

yeah

### [45:25 - 45:25]

yeah

### [45:25 - 45:30]

not much more other than sort of more of the same i don't want to go too much into this they do video

### [45:30 - 45:40]

prediction as well and so on um and um compared to what is that diffusion transformers i hope you get

### [45:40 - 45:47]

the idea of what this is the scaling trends look promising i can say that but obviously again

### [45:47 - 45:53]

they because of resource constraints um have not tried at larger scales and

### [45:53 - 45:55]

the basic

### [45:55 - 46:00]

case itself is such that you do need just to expand like your fixed cost

### [46:00 - 46:07]

to work with energy-based models is a lot higher however it could in fact be that at large scales

### [46:07 - 46:12]

that fixed cost is amortized by the gains that you make and it could actually be more beneficial

### [46:12 - 46:19]

to go with energy-based models than with sort of classic models in all of this i find the paper

### [46:19 - 46:25]

very cool uh but i do feel like they bring a lot of philosophy in it and they compare

### [46:25 - 46:30]

with models that are not necessarily comparable like i don't think chain of thought thinking or

### [46:30 - 46:36]

or or reasoning models or anything like this have anything to do with this

### [46:36 - 46:42]

unless you say oh well they also do multiple steps and so on but that's to me very abstract

### [46:42 - 46:49]

to me in an energy-based model this multi-forward pass optimization is just

### [46:49 - 46:55]

the way you do inference and you can view that as one inference step and then once you do that

### [46:55 - 47:00]

once you have that you can might as well do chain of thought with it you might as well do

### [47:00 - 47:06]

um reasoning with that you might as well train that with reinforcement learning right so these

### [47:06 - 47:10]

things to me have sort of not much to do with each other

### [47:11 - 47:18]

the energy-based models have nice properties no matter no matter what right okay i don't want to

### [47:18 - 47:24]

uh go and keep you here for longer than necessary please give the paper a read if you are

### [47:25 - 47:32]

interested a lot of thanks to the authors we did discuss this in our discord paper discussions and

### [47:32 - 47:38]

actually um the the lead author here was part of those discussions and we're obviously super

### [47:38 - 47:42]

thankful for that that is very cool if you are interested come join our discord

### [47:42 - 47:50]

uh we have a lot of paper discussions all the time and if even if not i'll see you around bye
