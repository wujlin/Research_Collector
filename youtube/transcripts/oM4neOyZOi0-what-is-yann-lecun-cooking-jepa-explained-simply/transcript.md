# What Is Yann LeCun Cooking? JEPA Explained Simply

- URL: https://www.youtube.com/watch?v=oM4neOyZOi0
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-09T18:35:48`

## Transcript

### [00:00 - 00:05]

JEPA has been one of the most audacious AI concepts that you either first heard about it

### [00:05 - 00:10]

through how Jan LeCun said that LLMs are doomed, or through him flaming people online about JEPA.

### [00:10 - 00:14]

But if you don't really understand it, I don't really blame you. I think it is one of the most

### [00:14 - 00:19]

convoluted research topics that's just impossible to follow. Like for LLMs, we predict tokens,

### [00:19 - 00:24]

for image generation, we predict a less noisy image, but for JEPA, we are literally predicting

### [00:24 - 00:29]

a high-dimensional representation in a learned latent space, and just trying to explain its goal

### [00:29 - 00:34]

is already too abstract in itself. To top that off, just imagine someone trying to explain the

### [00:34 - 00:39]

progress of JEPA. Oh, okay, so JEPA kind of went from using exponential moving average target

### [00:39 - 00:43]

networks to isotropic gaussian embedding construction average target networks to also

### [00:43 - 00:47]

What am I even saying? I probably just spammed a lot of words that probably doesn't even mean

### [00:47 - 00:51]

anything. So in today's video, I'll be breaking down the essence of JEPA, the current state of it,

### [00:52 - 00:56]

all without instantly drowning you in a bunch of technical terms. And before we dive into it,

### [00:56 - 00:59]

if you're running ClockCode, Codex, or OpenCode in 2026,

### [00:59 - 01:03]

you have probably hit the same wall where the agent is strong, but the terminal experience

### [01:03 - 01:07]

could still somehow be better. If you find yourself juggling sessions, losing track of

### [01:07 - 01:12]

what's running where, or constantly copy-pasting context, it may be worth it for you to look into

### [01:12 - 01:17]

Warp. They're rolling out features that turn it into a more cohesive, agentic-focused development

### [01:17 - 01:22]

environment for the CLI tools you already use. Warp now has universal agent support, so you can

### [01:22 - 01:27]

run ClockCode, Codex, OpenCode, and more side-by-side in one setup, and actually manage them

### [01:29 - 01:33]

like vertical tabs that lets you monitor sessions with rich context at a glance so you're not

### [01:33 - 01:38]

constantly clicking around just to remember which agent is doing what, along with directory view,

### [01:38 - 01:43]

git branch, and conversation statuses. And the CLI agent toolbar makes your workflow even more

### [01:43 - 01:47]

agent-native. You get the controls you actually need without leaving the terminal, like attaching

### [01:47 - 01:52]

context, jumping into files, and reviewing what changed. On top of that, for code review, you can

### [01:52 - 01:58]

leave inline comments and send that feedback straight into the running agent so it iterates

### [01:59 - 02:03]

without you bouncing between tools. Because you shouldn't have to rethink your setup every time

### [02:03 - 02:07]

you switch harnesses. So if you're ready to upgrade the place you run your coding agent, just like the

### [02:07 - 02:12]

700,000 other developers running 1 million ClockCode and Codex sessions in Warp, check them

### [02:12 - 02:16]

out using the link down in the description, and thank you Warp for sponsoring this video.

### [02:16 - 02:22]

Anyways, to comprehend what JEPA, short for Joint Embedding Predictive Architecture, is doing,

### [02:22 - 02:27]

think of it like how LLM is predicting the next token, but JEPA is just predicting this thing

### [02:27 - 02:29]

called a view. A view is a transformer.

### [02:29 - 02:34]

Masking or partial observation of an input that preserves the underlying semantic state

### [02:34 - 02:38]

while hiding or removing some information. So let's say there's a cat sitting on a couch.

### [02:38 - 02:43]

You could observe an image, the left half of the image, the right half of the image,

### [02:43 - 02:48]

a zoomed in crop, a masked version of the image, a different camera angle of the same scene,

### [02:48 - 02:53]

a video, a different frame from the same video. All of these I just mentioned are views. Even

### [02:53 - 02:58]

though they are different sensory observations, their representations correspond approximately

### [02:58 - 02:59]

to the same underlying scenario. So if you're going to be doing a video, you're going to have to

### [02:59 - 03:04]

line scene or world state. So the idea of a cat sitting on a couch can be captured in a high

### [03:04 - 03:09]

dimensional latent space with all kinds of sentences or images that show this idea will

### [03:09 - 03:13]

point to that spot in the latent space. Then in JEPA's training, one view is used as the

### [03:13 - 03:18]

context and another as the target. So instead of learning by reconstructing pixels or predicting

### [03:18 - 03:22]

a token, the model encodes both into latent embeddings and learns to predict the target

### [03:22 - 03:26]

embedding from the context embedding. JEPA's objective would then naturally encourage

### [03:26 - 03:31]

capturing what is shared and predictable across views while discarding unpredictable or irrelevant

### [03:31 - 03:36]

details. So theoretically, the benefits of being able to think in higher dimensions like the latent

### [03:36 - 03:41]

space should provide better incentives for the model to learn concepts or semantics clearly

### [03:41 - 03:45]

and consistently. As the problem of directly working with pixels or tokens is that the

### [03:45 - 03:51]

objective is full of entropy. For example, text variations that does not have a right answer

### [03:51 - 03:55]

while all meaning roughly the same thing and lighting changes of background within an image

### [03:55 - 03:56]

that doesn't even matter.

### [03:56 - 04:01]

But the reconstruction error will always be full of noise. This results in the actual

### [04:01 - 04:06]

model having the need to accommodate for everything, even for things that are fundamentally unpredictable.

### [04:06 - 04:10]

But when you compress these views into a latent space, the target embedding will naturally

### [04:10 - 04:15]

remove all the noises and only contain this compressed abstraction and semantics. So when

### [04:15 - 04:19]

the predictor minimizes distance to the target embedding, it is encouraged to model only

### [04:19 - 04:24]

the stable structure between views and the noise will not interfere, which is the culprit

### [04:24 - 04:26]

that makes the model predictions harder than it should.

### [04:26 - 04:31]

Although apparently scale solves the problem a little bit, more and more models are hitting

### [04:31 - 04:33]

the 1 trillion parameter number.

### [04:33 - 04:37]

But anyways, this shifts the learning focus for the model from What exactly are these

### [04:37 - 04:42]

pixels to what underlying factors explain both observations? This doesn't mean the

### [04:42 - 04:45]

model would not be able to see pixels or texts.

### [04:45 - 04:49]

But before that, the typical jetpaw learning setup contains three components-

### [04:49 - 04:54]

A context encoder that takes the current context view like visible image blocks or text, and

### [04:54 - 04:56]

produces an embedding.

### [04:56 - 05:01]

that takes the target view like mask blocks or a future segment and produces the target embedding.

### [05:01 - 05:06]

This embedding represents what actually happens next or what is missing, but it is still within

### [05:06 - 05:11]

the same representation space. And lastly, a predictor component that bridges the two states,

### [05:11 - 05:15]

which is a representation of the current situation and a representation of the future or missing

### [05:15 - 05:20]

part. What this component does is that it takes the context embedding and tries to produce the

### [05:20 - 05:24]

target embedding, basically predicting the representation of the next or the missing

### [05:24 - 05:30]

observation. So there is no pixel reconstruction loss. There is no token cross entropy. The only

### [05:30 - 05:35]

objective is alignment in representation space. And over time, this encourages the encoder to

### [05:35 - 05:41]

represent object position, spatial configuration, motion dynamics, scene structure, physical

### [05:41 - 05:46]

relationships, and so much more. Rather than just surface level statistics that are brute force to

### [05:46 - 05:50]

learn semantic relations at scale. Then at inference, the target encoder is typically

### [05:50 - 05:54]

not needed. What is then generally used is the trained context encoder,

### [05:54 - 05:59]

which now serves as a feature extractor or latent state estimator. And there are multiple ways to

### [05:59 - 06:04]

apply JEPA. One is representation extraction, where you feed an input like an image, video clip,

### [06:04 - 06:09]

etc. into the context encoder and obtain an embedding. And that embedding can be used for

### [06:09 - 06:14]

classification, retrieval, similarity search, or even downstream supervised fine tuning. So in this

### [06:14 - 06:19]

setting, JEPA behaves like a foundational representation model. Two is latent prediction

### [06:19 - 06:23]

for world modeling, where if the predictor is incorporated, the model can take a current state

### [06:23 - 06:24]

embedding and apply it to the context encoder. And that embedding can be used for classification,

### [06:24 - 06:29]

and predict the embedding of a future state. In video JEPA, for instance, this enables forecasting

### [06:29 - 06:34]

in latent space rather than in pixel space. And instead of predicting future frames, it predicts

### [06:34 - 06:40]

future latent states. This is computationally cheaper and focuses on semantic dynamics rather

### [06:40 - 06:45]

than texture. So you would save so much more money not needing to generate the extra visual tokens.

### [06:45 - 06:50]

Three is planning in latent space, where the model can condition predictions based on actions,

### [06:50 - 06:54]

such as in robotics. So now you basically have two inputs. One is the context encoder,

### [06:54 - 06:58]

which observes the current scene and produces an embedding that represents the current latent

### [06:58 - 07:03]

state of the environment. And two is an embedding of the action being taken or considered by the

### [07:03 - 07:08]

robot. The predictor then takes the latent state together with the action embedding and predicts

### [07:08 - 07:12]

the embedding of future states. The key here is that no pixels are generated during planning,

### [07:13 - 07:18]

which means the system is essentially imagining possible outcomes internally before acting.

### [07:18 - 07:23]

So remember how in that video model where I talked about how AI video models might be used for world

### [07:23 - 07:23]

simulation? Well, that's not the case. So let's talk about how AI video models might be used for

### [07:23 - 07:29]

world simulation. Well, with JIPA, you do not need to materialize anything into pixel space to

### [07:29 - 07:33]

simulate the world. So you're basically saving the compute for generating the pixels. So instead of

### [07:33 - 07:38]

generating the full video frames to predict the future, JIPA performs the simulation directly in

### [07:38 - 07:43]

latent space where action sequences and state transitions are represented as embeddings.

### [07:43 - 07:47]

And because the computations happen in representation space rather than pixel space,

### [07:47 - 07:52]

this process is significantly more efficient while still capturing the underlying dynamics

### [07:52 - 07:52]

of the environment.

### [07:52 - 07:53]

But

### [07:53 - 07:59]

that is if JIPA works, because as great as JIPA sounds, compressing and operating in latent space

### [07:59 - 08:04]

is still much harder as the model has learned a representation that actually contains the right

### [08:04 - 08:09]

information about the world. If the embedding misses important variables like object position,

### [08:09 - 08:13]

velocity, or interaction constraints, then predicting future embeddings becomes meaningless.

### [08:14 - 08:19]

So the latent space must be consistent and predictable. If two very similar but slightly

### [08:19 - 08:23]

different states produce embeddings that are way too far away, then the predictor would not be

### [08:23 - 08:28]

able to learn the stable dynamics. On top of that, for more complicated JIPA applications,

### [08:28 - 08:32]

the latent space must be structured in a way that supports planning. The predictor needs

### [08:32 - 08:36]

to learn smooth transitions between states through conditional actions so the changes

### [08:36 - 08:40]

in the latent state would make sense. So if the geometry of the embedding space is poorly

### [08:40 - 08:45]

structured, then the predicted trajectories would drift, accumulate errors, or stop corresponding

### [08:45 - 08:50]

to real-world outcomes. But the last and most important thing for JIPA is the representation

### [08:50 - 08:53]

must be informative without collapsing.

### [08:53 - 08:53]

So if you're able to learn the stable dynamics, then you're able to learn the stable dynamics.

### [08:53 - 08:57]

Since JEPA does not reconstruct pixels or have any inherent noise,

### [08:57 - 09:01]

nothing stops the encoder from outputting the same vector for every input,

### [09:01 - 09:06]

especially when there are two encoders used for JEPA, the context and the target encoder.

### [09:06 - 09:09]

So the model could discover a very easy shortcut.

### [09:09 - 09:11]

Instead of learning meaningful representations of the scene,

### [09:12 - 09:15]

both encoders could simply output the same constant embedding for everything.

### [09:15 - 09:20]

A cat, a car, or a building would all produce the exact same embedding.

### [09:20 - 09:23]

And now, the predictor's job becomes very easy.

### [09:23 - 09:27]

Because no matter what the context is, it would just output the same constant embedding,

### [09:27 - 09:29]

which will always match the target embedding.

### [09:29 - 09:32]

So the training loss becomes extremely small, but the model has learned

### [09:32 - 09:37]

absolutely nothing about the world, and everything looks identical in the latent space.

### [09:37 - 09:39]

This failure mode is called representation collapse,

### [09:39 - 09:44]

where the embedding space collapses into a single point with no useful information.

### [09:44 - 09:48]

But since it'll keep the loss very low, this would happen really easily.

### [09:48 - 09:52]

The first practical solution researchers used was updating the target encoder

### [09:52 - 09:53]

with something called JEPA.

### [09:53 - 09:55]

Or EMA, short for Exponential Moving Average.

### [09:56 - 10:00]

So instead of letting both encoders learn freely and can instantly copy each other's behavior,

### [10:00 - 10:03]

the target encoder is updated very slowly.

### [10:03 - 10:06]

If the context encoder suddenly changes its representation,

### [10:06 - 10:08]

the target encoder does not immediately follow.

### [10:09 - 10:13]

It only moves gradually over time, acting like a delayed version of the context encoder.

### [10:13 - 10:16]

You can think of it like chasing a slowly moving target.

### [10:16 - 10:18]

And because the target encoder changes slowly,

### [10:18 - 10:21]

the system cannot instantly collapse to a constant embedding.

### [10:21 - 10:23]

The predictor has to keep

### [10:23 - 10:26]

adapting to a representation that keeps drifting forward.

### [10:26 - 10:30]

So in practice, only the context encoder is trained directly with gradients,

### [10:30 - 10:35]

while the target encoder is updated as a slow-moving average of the context encoder's weights.

### [10:35 - 10:37]

So they basically will never match,

### [10:37 - 10:40]

which makes collapsing much harder and stabilizes training easily.

### [10:40 - 10:43]

So in the early experiments of JEPA, like iJEPA,

### [10:43 - 10:45]

where JEPA is applied to image generations,

### [10:45 - 10:48]

and vJEPA, where JEPA is applied to video generation,

### [10:48 - 10:53]

or even DYNO, which is a self-supervised vision method for learning image representations

### [10:53 - 10:55]

without labels, they are all utilizing EMA.

### [10:56 - 11:01]

However, EMA is ultimately a training trick rather than a principled objective,

### [11:01 - 11:03]

as there does not exist a loss function for EMA,

### [11:04 - 11:06]

which prevents it from being minimized directly.

### [11:06 - 11:10]

It is also heuristic based because stability depends on EMA schedules,

### [11:10 - 11:15]

weight sharing, and training dynamics, which can be fragile and require manual tuning.

### [11:15 - 11:20]

This is why later research still explored other methods for preventing representation collapse.

### [11:20 - 11:23]

With one major direction known as the InfoMax approach,

### [11:23 - 11:28]

which tries to ensure the representation itself contains information uniquely about the input.

### [11:28 - 11:32]

The idea of InfoMax first appeared in 1995 from Bell and Savnovsky,

### [11:32 - 11:33]

and the main idea is simple.

### [11:33 - 11:38]

A good representation should retain as much information about the input as possible.

### [11:38 - 11:41]

In other words, if you look at the representation produced by the model,

### [11:41 - 11:45]

you should still be able to tell something meaningful about what the original input was.

### [11:45 - 11:49]

The representation should not be throwing away the important signals

### [11:49 - 11:51]

and collapse everything into something trivial.

### [11:51 - 11:52]

Bell and Savnovsky,

### [11:52 - 11:56]

they formalized this by proposing that learning systems should maximize

### [11:56 - 11:59]

the mutual information between the input and the representation,

### [11:59 - 12:04]

which simply means the representation should preserve as much useful signal from the input as possible.

### [12:04 - 12:08]

This principle later became the foundation for many self-supervised learning methods,

### [12:08 - 12:12]

and it is one of the key ideas that influenced the approaches used in JEPA.

### [12:12 - 12:15]

So instead of stabilizing training with a slow-moving technique like EMA,

### [12:16 - 12:20]

these methods add regularization terms that force the embedding space to remain informative.

### [12:21 - 12:22]

There are two main ways researchers try to use this method.

### [12:22 - 12:25]

The first is sample contrastive methods,

### [12:25 - 12:30]

where the model is encouraged to make embeddings of different samples distinct from one another.

### [12:30 - 12:33]

Methods like SimCLR, published in 2020 long before JEPA,

### [12:34 - 12:37]

work this way by creating two augmented views of the same image

### [12:37 - 12:41]

and training the model to recognize that they come from the same underlying sample.

### [12:41 - 12:45]

The model basically learns to pull the embeddings of those two views closer together

### [12:45 - 12:47]

while pushing embeddings of other images further apart.

### [12:48 - 12:50]

So if two inputs are just different views of the same object,

### [12:50 - 12:52]

their embeddings should lend closer to each other.

### [12:52 - 12:52]

So if two inputs are just different views of the same object, their embeddings should lend closer to each other.

### [12:52 - 12:54]

So if two inputs are just different views of the same object, their embeddings should lend closer to each other.

### [12:54 - 12:58]

But if they come from different images, the model should place them far apart.

### [12:58 - 13:01]

Over time, this forces the embedding space to organize itself

### [13:01 - 13:05]

so that similar things cluster together while unrelated samples spread apart,

### [13:05 - 13:08]

which helps prevent the representation from collapsing into a single point.

### [13:08 - 13:12]

But the downside of this approach is that it relies heavily on negative samples.

### [13:12 - 13:14]

So to properly separate representations,

### [13:14 - 13:17]

the model needs a large batch of other images to push away from.

### [13:17 - 13:20]

This means you often need very large batch sizes or memory banks,

### [13:21 - 13:22]

which makes training computationally

### [13:22 - 13:24]

expensive and harder to scale.

### [13:24 - 13:27]

So a second approach is dimension contrastive methods,

### [13:27 - 13:29]

which focus on the structure of the embedding itself

### [13:29 - 13:31]

rather than comparing it to different samples.

### [13:31 - 13:33]

Instead of pushing different samples apart,

### [13:33 - 13:37]

these methods try to ensure that each dimension of the representation

### [13:37 - 13:40]

captures different information about the input.

### [13:40 - 13:42]

You can think of it like making each coordinate in the representation

### [13:43 - 13:45]

describing a different aspect of the input,

### [13:45 - 13:47]

such as shape, position, texture, or motion.

### [13:47 - 13:52]

To encourage this, these methods add regularization terms to the loss that penalize,

### [13:52 - 13:56]

redundancy between dimensions, basically enforcing diversity across dimensions,

### [13:56 - 13:59]

resulting in the embedding space remaining rich and informative

### [14:00 - 14:02]

without needing to explicitly push different samples apart.

### [14:03 - 14:07]

So techniques like Barlow-Twins and VIC-REC implement this by measuring

### [14:07 - 14:10]

the correlation between embedding dimensions and penalizing the model

### [14:10 - 14:13]

if multiple dimensions start carrying the same signal.

### [14:13 - 14:16]

And this was already a big step forward because the model no longer needed

### [14:17 - 14:20]

large batches of negative samples to achieve the contrastive method.

### [14:20 - 14:22]

But these methods still relied on

### [14:22 - 14:25]

multiple loss terms and carefully balanced hyperparameters

### [14:25 - 14:27]

to keep the representation stable.

### [14:27 - 14:31]

And this is the latest bet that Yann LeCun is making, called Legerpa comes in.

### [14:31 - 14:36]

Released in November 2025, instead of simply de-correlating dimensions,

### [14:36 - 14:41]

Legerpa takes a more direct approach where it constrains the overall geometry

### [14:41 - 14:42]

of the embedding space itself.

### [14:42 - 14:47]

It specifically encourages the embeddings to follow an isotropic Gaussian distribution,

### [14:47 - 14:51]

meaning the representation space spreads information evenly across dimensions,

### [14:51 - 14:52]

so no direction can be changed.

### [14:52 - 14:54]

And the model also allows the embedding space to be

### [14:55 - 14:58]

a point-based distribution, so that the direction collapses or dominates.

### [14:58 - 15:02]

To not go too crazy on the math, imagine the embedding space as a cloud of points

### [15:02 - 15:06]

where every input becomes a point in this space, so if the model collapses,

### [15:06 - 15:10]

all points basically fall into one point, or it could also collapse into a thin line

### [15:10 - 15:14]

or a flat sheet because many dimensions stop carrying information.

### [15:14 - 15:18]

So what Legerpa does is it encourages the embeddings to follow an isotropic

### [15:19 - 15:22]

Gaussian distribution, which means the point cloud should look like a round ball

### [15:22 - 15:23]

and be similar across all dimensions.

### [15:24 - 15:29]

And interestingly, this simple geometric constraint turns out to work surprisingly well in practice.

### [15:29 - 15:34]

In their experiments, Legerpa was able to train GIPA-style models without relying on EMA

### [15:34 - 15:37]

while still avoiding collapse and learning strong representations.

### [15:37 - 15:42]

Despite using a simpler objective, it achieves competitive or better performance

### [15:42 - 15:47]

compared to earlier self-supervised methods, VICReg, Barlow twins, and SimCLR

### [15:47 - 15:51]

on standard vision benchmarks, even achieving accuracy levels similar to Dino

### [15:51 - 15:53]

on ImageNet, which is state-of-the-art.

### [15:53 - 15:57]

So if GIPA is this good, why is the LLM field not using it?

### [15:57 - 16:01]

Well, GIPA works best when the data contains a lot of unpredictable low-level detail

### [16:01 - 16:05]

that doesn't really matter a lot, which images and videos are full of.

### [16:05 - 16:09]

Trying to predict those details directly is pretty wasteful, so like I mentioned earlier,

### [16:09 - 16:13]

GIPA solved this by predicting abstract representations instead of pixels.

### [16:14 - 16:15]

But language is very different.

### [16:15 - 16:20]

Text is already a symbolic and compressed representation of meaning.

### [16:20 - 16:21]

Words are discrete tokens,

### [16:21 - 16:24]

that already remove most of the low-level noise found in sensory data.

### [16:24 - 16:30]

So when an LLM predicts the next token, it is already operating at a fairly high semantic level.

### [16:30 - 16:32]

In other words, the problem GIPA is designed to solve,

### [16:32 - 16:35]

which is removing unpredictable sensory noise from prediction,

### [16:36 - 16:38]

does not exist as strongly in text.

### [16:38 - 16:41]

And of course, autoregressive training works perfectly already.

### [16:41 - 16:44]

It's an objective that can provide high signal feedback to the model.

### [16:45 - 16:48]

And GIPA is probably not going to be a better design to predict text,

### [16:48 - 16:51]

especially when languages have more constraints,

### [16:51 - 16:55]

like word order, which is already implicitly defined in next token prediction.

### [16:55 - 16:58]

A really prominent direction of GIPA I've been seeing, though,

### [16:58 - 16:59]

is using it for medical imaging.

### [17:00 - 17:01]

There's this research called Echo GIPA,

### [17:01 - 17:05]

which applies the GIPA framework to echocardiography videos,

### [17:05 - 17:07]

which are basically ultrasound videos of the heart.

### [17:07 - 17:10]

But why is it potentially a perfect fit for medical imaging?

### [17:10 - 17:13]

Well, this is because many medical imaging modalities

### [17:13 - 17:15]

contain a huge amount of noise and artifact.

### [17:15 - 17:20]

For example, ultrasound images are full of things like speckle noise, sensor artifacts,

### [17:20 - 17:24]

inconsistent probe angles, machine-specific distortions, and more.

### [17:24 - 17:26]

So if a model is trained to reconstruct pixels,

### [17:26 - 17:30]

it ends up wasting a lot of capacity trying to model these random patterns

### [17:30 - 17:31]

that are not clinically meaningful.

### [17:31 - 17:35]

And doctors do not really care about the exact pixel pattern of the ultrasound image.

### [17:36 - 17:38]

What they care about are stable anatomical signals,

### [17:38 - 17:41]

such as the size of the heart chambers, how the walls move during each beat,

### [17:41 - 17:46]

how valves open and close, which is the type of information GIPA tends to learn.

### [17:46 - 17:50]

So as GIPA encodes and predicts representations instead of pixels,

### [17:50 - 17:53]

predictable noise cannot be reliably predicted from the context.

### [17:53 - 17:56]

The model is therefore pushed to focus on the consistent structures

### [17:56 - 17:58]

and dynamics of the anatomy instead.

### [17:58 - 18:01]

So in Echo GIPA, the model learns to predict representations

### [18:01 - 18:04]

of future cardiac motion from earlier frames,

### [18:04 - 18:08]

which encourages it to encode things like heart geometry and motion patterns.

### [18:09 - 18:11]

Then instead of memorizing noisy ultrasound textures,

### [18:11 - 18:14]

the representation becomes so much more aligned

### [18:14 - 18:16]

with the actual physiological structure of the heart,

### [18:16 - 18:20]

which makes it useful for downstream tasks like diagnosis or measurement.

### [18:20 - 18:22]

This is why I think GIPA has the potential

### [18:22 - 18:25]

to become the dominant method in the medical field.

### [18:25 - 18:29]

So when Yann LeCun said LLM is doomed, I low-key took it out of context.

### [18:29 - 18:31]

LLM is only meant to work with languages

### [18:31 - 18:34]

due to how it is a symbolic system with a lot less noise.

### [18:34 - 18:37]

So if you want to truly scale beyond language,

### [18:37 - 18:41]

especially for research on natural or real-life data, he's got a point.

### [18:42 - 18:43]

So yeah, that's it for this video.

### [18:43 - 18:45]

And if you like how I explained the AI concepts today,

### [18:45 - 18:48]

you should definitely check out my latest project, IntuitiveAI.academy,

### [18:48 - 18:50]

where it contains an intuitive explanation

### [18:50 - 18:52]

of modern LLMs from the ground up.

### [18:52 - 18:55]

Ranging from LLM architectures, MOE, LoRa,

### [18:55 - 18:57]

to our latest chapters, Reinforcement Learning,

### [18:58 - 19:01]

where we cover how RL works and how it interacts with LLMs,

### [19:01 - 19:03]

literally published yesterday.

### [19:03 - 19:05]

With how challenging RL can be,

### [19:05 - 19:07]

we have also built interactive visualizations

### [19:07 - 19:09]

to help you better understand its logic.

### [19:09 - 19:12]

This website is a series where I break down AI topics intuitively

### [19:13 - 19:15]

because I genuinely think anyone could understand them

### [19:15 - 19:17]

no matter how difficult it may seem.

### [19:17 - 19:20]

So for those wanting to get into the technical side of AI or LLMs,

### [19:20 - 19:23]

this should be the perfect place for you to dive into the technical parts

### [19:23 - 19:26]

without being intimidated by crazy-looking maths.

### [19:26 - 19:28]

And right now, the early bird discount is nearly over,

### [19:28 - 19:32]

but you can still use the limited code EARLY for 40% off a yearly plan.

### [19:32 - 19:33]

And thank you guys for watching.

### [19:33 - 19:38]

A big shout out to Spamadge, Chris Ledoux, Degan, Robert Zaviasa,

### [19:39 - 19:44]

Marcelo Ferreria, Proof and Inu, DX Research Group, Alex, Midwest Maker,

### [19:45 - 19:47]

and many others that support me through Patreon or YouTube.

### [19:47 - 19:50]

Follow me on Twitter if you haven't, and I'll see you in the next one.

### [19:50 - 19:53]

Subtitles by the Amara.org community
