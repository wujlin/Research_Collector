# [ICLR 2026 Oral] Latent Particle World Models

- URL: https://www.youtube.com/watch?v=aZeaCyXJjYI
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-12T00:43:50`

## Transcript

### [00:00 - 00:09]

Hi, my name is Tal, and in this video, I'll present our iCLEAR 2026 oral paper, Latent Particle World Models.

### [00:09 - 00:23]

In this work, we introduce the latent particle world model, LPWM, the first self-supervised object-centric world model capable of end-to-end training on complex real-world video data.

### [00:23 - 00:27]

What does self-supervised object-centric mean?

### [00:27 - 00:35]

LPWM autonomously discovers key points, bonding boxes, and object masks directly from video data.

### [00:35 - 00:41]

This approach enables stochastic dynamics sampling and enables scalability to complex environments.

### [00:41 - 00:51]

LPWM is trained exclusively from video observations and supports optional conditioning on actions, language, images, and multi-view inputs.

### [00:51 - 00:57]

We demonstrate the applicability of our model to imitation learning on two complex multi-object environments,

### [00:57 - 01:02]

highlighting its utility for decision-making tasks.

### [01:02 - 01:09]

I want to begin with asking, how do we learn stochastic dynamics in the absence of a conditioning signal?

### [01:09 - 01:16]

One way to do this would be to learn a dynamics model that is conditioned on latent signals that guide it toward the next state.

### [01:16 - 01:22]

These signals are typically called latent actions, and they are the output of a latent inverse dynamics model.

### [01:22 - 01:27]

Latent actions are latent variables representing transitions between consecutive observations.

### [01:27 - 01:30]

The common scheme to learn these variables is auto-encoding.

### [01:30 - 01:37]

An inverse model infers the latent action, and a decoder reconstructs the future frame given the latent action and the previous frame.

### [01:37 - 01:42]

There are two fatal flaws in this design, representation collapse and global modeling.

### [01:42 - 01:49]

To prevent the latent action encoder from memorizing the consecutive frame, leading to the decoder ignoring the previous frame,

### [01:49 - 01:55]

a stronger regularization is applied, either via vector quantization or KL regularization to a fixed prior.

### [01:55 - 01:56]

Another flaw is that the decoder does not memorize the previous frame.

### [01:57 - 02:04]

Another flaw is that latent actions are typically global, meaning that there is one latent vector representing the entire transition between frames.

### [02:04 - 02:07]

There are limitations to using a global latent action vector.

### [02:07 - 02:14]

In multi-entity scenes, for example, enemies in Mario, a single vector cannot naturally disentangle local interactions,

### [02:14 - 02:21]

and these methods typically rely on single-agent movements, like a gripper, but even a gripper can be composed of multiple joints.

### [02:21 - 02:26]

Provided with a latent action model, we can now integrate these in a world model to model stochastic dynamics.

### [02:27 - 02:37]

Another challenge we discussed is how to learn world models from high-dimensional observations.

### [02:37 - 02:42]

Traditional approaches typically compress the input frame to a single vector.

### [02:42 - 02:48]

This makes it hard to represent fine-grained details or scenes with a lot of objects.

### [02:48 - 02:55]

Current approaches use patch-based representations, where each patch serves as an entity.

### [02:55 - 02:56]

These are more fine-grained, but still not exactly the same.

### [02:57 - 03:02]

But we can do what we want, especially when aligning with other modalities, such as language.

### [03:02 - 03:11]

Both of these approaches are very different from how we represent language, where tokenization is usually semantic.

### [03:11 - 03:17]

Consider this illustrative example, where the dynamics of two moving objects are described alongside a caption,

### [03:17 - 03:22]

the blue ball is moving diagonally towards the green square.

### [03:22 - 03:25]

Text representations typically rely on semantic tokenization,

### [03:25 - 03:27]

into words or sub-words, and so on.

### [03:27 - 03:31]

This underpins the success of large language models.

### [03:31 - 03:36]

In contrast, image representations predominantly use patchifying,

### [03:36 - 03:42]

dividing the image into a fixed grid of patches without regard for semantic content.

### [03:42 - 03:47]

If we were to do something like this for text, it would look very weird.

### [03:47 - 03:52]

While this patch-based approach enables scalability and generality,

### [03:52 - 03:55]

it lacks the semantic intuitiveness of object-centric decompositions

### [03:55 - 04:01]

that can enhance the model's ability to capture meaningful object interactions and relationships,

### [04:01 - 04:07]

crucial for understanding complex things, and align more naturally with language representations.

### [04:07 - 04:16]

So, how can we obtain an object-centric decomposition and do so without human supervision?

### [04:16 - 04:20]

People have studied object-centric representations for years.

### [04:20 - 04:23]

In fact, some of the early theories from the 90s proposed that human vision,

### [04:23 - 04:30]

parses scenes into what and where, decomposing content and location.

### [04:30 - 04:34]

However, these approaches were not adopted at a larger scale.

### [04:34 - 04:39]

Inspired by the what-where pathway in the human visual system and recent neuroscience findings,

### [04:39 - 04:45]

which suggest human leverage internal visual spatial world models for planning and action,

### [04:45 - 04:50]

combining object-centric representations with world models is a promising direction

### [04:50 - 04:53]

toward more effective decision-making and vision language optimization.

### [04:53 - 05:01]

We now continue to self-supervise object-centric representation learning,

### [05:01 - 05:05]

and specifically, deep latent particles, DLP.

### [05:05 - 05:09]

DLP is a VAE where the latent space is a set of particles.

### [05:09 - 05:15]

Each particle has several learned attributes, such as keypoint, bounding boxes, transparency,

### [05:15 - 05:19]

and of course, latent visual features to represent shape and appearance.

### [05:19 - 05:22]

Every attribute is learned with respect to the optimization process,

### [05:22 - 05:25]

with respect to the optimization objective, the evidence-level bound,

### [05:25 - 05:30]

which is decomposed to the reconstruction error and KL divergence terms.

### [05:30 - 05:36]

In this work, we also introduced DLP v3, which introduces several improvements.

### [05:36 - 05:42]

Please refer to the paper for details.

### [05:42 - 05:48]

Here we can see how DLP decomposes scenes, creating a self-supervised object-centric representation,

### [05:48 - 05:52]

which motivates its utilization in downstream tasks.

### [05:52 - 06:00]

So, how do we build world models from latent particles?

### [06:00 - 06:05]

The main novel component added to the DLP framework is the context module,

### [06:05 - 06:10]

which is designed to model stochastic dynamics in actionless video.

### [06:10 - 06:14]

The idea is to capture stochastic transitions of entities in the scene

### [06:14 - 06:19]

with per-particle latent actions as part of the dynamics modeling.

### [06:19 - 06:21]

This formulation enables the representations of

### [06:21 - 06:27]

multiple simultaneous interactions and captures multi-modality.

### [06:27 - 06:29]

Here is how it works.

### [06:29 - 06:34]

The context model takes in a sequence of particle sets across T plus 1 frames.

### [06:34 - 06:38]

The module is composed of two complementary heads,

### [06:38 - 06:45]

the latent inverse dynamics, which predicts the latent actions responsible for the transition between consecutive particle states,

### [06:45 - 06:50]

and the latent policy, which models the distribution of latent actions conditioned on the current states.

### [06:51 - 06:55]

The module is implemented as a causal spatio-temporal transformer.

### [06:55 - 07:00]

The latent policy serves as a prior that regularizes the inverse dynamics

### [07:00 - 07:04]

via a KL divergence penalty in the VAE objective.

### [07:04 - 07:08]

This is in contrast to the fixed prior, or codebook regularization.

### [07:08 - 07:12]

Here the regularization is learned and used at inference time as well.

### [07:12 - 07:17]

At training time, latent actions are obtained through the inverse dynamics head,

### [07:17 - 07:20]

ensuring consistency with the observed transitions.

### [07:20 - 07:26]

At inference time, latent actions can instead be sampled directly from the latent policy prior,

### [07:26 - 07:29]

enabling stochastic callouts of the whole model.

### [07:29 - 07:36]

Conditioning on external signals, such as global actions, language instructions, or image-based goals,

### [07:36 - 07:38]

within the latent context module,

### [07:38 - 07:42]

maps global scene-level signals into per-particle latent actions.

### [07:42 - 07:45]

For instance, given a language instruction,

### [07:45 - 07:48]

it learns to translate it into per-particle latent actions

### [07:48 - 07:52]

that drive the dynamics towards satisfying the instruction.

### [07:56 - 07:58]

Putting it all together.

### [07:58 - 08:01]

Input frames are encoded into particle sets by the encoder,

### [08:01 - 08:04]

and decoded back to images by the decoder.

### [08:04 - 08:09]

The context model then processes the particles to sample latent actions,

### [08:09 - 08:12]

which are combined with the particles in the dynamics model

### [08:12 - 08:15]

to predict the next step particle states.

### [08:15 - 08:18]

LPWM is trained by maximizing

### [08:18 - 08:20]

temporal evidence lower bound,

### [08:20 - 08:24]

or minimizing the sum of reconstruction errors and KLA vergences,

### [08:24 - 08:27]

decomposed into a static term for the first frame

### [08:27 - 08:29]

and a dynamic term for the subsequent frames.

### [08:32 - 08:34]

Let's look at some results.

### [08:34 - 08:38]

All models are on the scale of 150 million parameters,

### [08:38 - 08:41]

much smaller than the standard video generation models.

### [08:42 - 08:46]

On the Mario video game, we have a moving camera and multiple enemies.

### [08:46 - 08:49]

The first type of fallouts is latent action condition,

### [08:49 - 08:53]

meaning that we extract the latent actions from the ground truth video

### [08:53 - 08:57]

and then use them to condition the dynamics model from the first frame.

### [08:57 - 09:00]

The baselines include DVAE,

### [09:00 - 09:03]

a patch-based non-object-centric dynamics VAE,

### [09:03 - 09:07]

and the object-centric slot attention-based play slot.

### [09:07 - 09:10]

The second type is stochastic generation,

### [09:10 - 09:14]

where we sample latent actions to generate different future predictions.

### [09:14 - 09:16]

For an analysis of the metrics,

### [09:16 - 09:18]

please refer to the paper.

### [09:21 - 09:24]

BEAR is a real-world multi-object interaction dataset.

### [09:25 - 09:28]

We can see the DVAE struggles with object permanence,

### [09:28 - 09:32]

while play slot is limited by the large number of objects.

### [09:33 - 09:36]

Similarly, we can sample different interactions.

### [09:41 - 09:44]

For action conditioning, on Sketchy,

### [09:44 - 09:47]

we see the DVAE again struggles with object permanence,

### [09:47 - 09:51]

and objects tend to deform and vanish in long-term prediction.

### [09:57 - 10:00]

For language conditioning, on Language Table,

### [10:00 - 10:04]

the model must align language tokens that include object types, names,

### [10:04 - 10:08]

and special relationships, such as closer or diagonal,

### [10:08 - 10:10]

with the visual tokens.

### [10:10 - 10:13]

We consider the object-centric particles naturally align better

### [10:13 - 10:16]

with language, allowing for language conditioning planning

### [10:16 - 10:18]

directly in the particle latent space.

### [10:30 - 10:33]

We close this presentation with a practical application

### [10:33 - 10:35]

for imitation learning.

### [10:35 - 10:39]

Pre-training LPWM on actionless video datasets

### [10:39 - 10:42]

enable you to predict video dynamics using latent actions.

### [10:42 - 10:46]

Suggesting that these latent actions capture actionable information.

### [10:47 - 10:49]

Assuming access to ground truth actions,

### [10:49 - 10:52]

and that the latent actions effectively encode dynamics,

### [10:52 - 10:55]

learning a simple mapping from latent actions to true actions

### [10:55 - 10:58]

may suffice to derive a policy.

### [10:59 - 11:03]

We pre-train LPWM with image goal conditioning on actionless videos,

### [11:03 - 11:06]

then freeze and learn to map the latent actions

### [11:06 - 11:09]

to ground truth actions with a simple neural network.

### [11:09 - 11:14]

At inference time, we sample rollouts from LPWM,

### [11:14 - 11:16]

map them to the environment actions,

### [11:16 - 11:19]

and execute in the environment in a closed-loop fashion.

### [11:23 - 11:25]

On the challenging Panda push environment

### [11:25 - 11:27]

that involves multi-object manipulation,

### [11:27 - 11:31]

we pre-train an image condition LPWM on multi-view demonstrations,

### [11:31 - 11:35]

where LPWM jointly models the dynamics in both views.

### [11:35 - 11:38]

As we show in our results, our simple policy mapping

### [11:38 - 11:40]

outperforms most baselines,

### [11:40 - 11:44]

demonstrating LPWM's potential to decision-making.

### [11:44 - 11:47]

For results on OGBench, please refer to the paper.

### [11:49 - 11:51]

We presented LPWM,

### [11:51 - 11:54]

the first end-to-end self-supervised object-centric model

### [11:54 - 11:57]

that supports multiple types of conditioning

### [11:57 - 12:00]

and demonstrating strong potential for decision-making.

### [12:00 - 12:03]

We conclude with some limitations.

### [12:03 - 12:05]

The self-supervised object-centric literature

### [12:05 - 12:08]

is yet to be scaled up properly to general purposes,

### [12:08 - 12:10]

in the wild video datasets.

### [12:10 - 12:12]

In addition, the pixel fidelity

### [12:12 - 12:14]

of modern diffusion-based video generator

### [12:14 - 12:17]

is still ahead of the VAE-style dynamics model.

### [12:19 - 12:20]

Thank you for watching,

### [12:20 - 12:22]

and be sure to visit the website for more videos,

### [12:22 - 12:24]

code, and tutorials.
