# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

- URL: https://www.youtube.com/watch?v=HbGah-uP1fI
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-12T00:59:07`

## Transcript

### [00:00 - 00:19]

Hello, everyone. I am Lakshya A. Agarwal, a PhD student at UC Berkeley Skylab, advised by Professor Matej Zaharia and Professor Dan Klein, and I'm very excited to present to you GEPA, a sample efficient learning and optimization technique for agents and LLM-based systems.

### [00:19 - 00:30]

How can we teach AI to perform new tasks? The standard way has been to perform weight updates with gradient descent, either during pre-training, supervised fine-tuning, or reinforcement learning.

### [00:30 - 00:46]

This has proven to be very effective, but it requires a huge number of examples. Trillions of tokens for pre-training, tens of thousands of labeled examples for supervised fine-tuning, or hundreds of thousands of rollouts for reinforcement learning in domains like math, coding, etc.

### [00:46 - 00:49]

However, as we tackle increasing needs for AI, we also need to think about how we can improve AI performance.

### [00:49 - 00:59]

While AI is increasingly challenging problems with AI, while GPU flops are getting cheaper, progress is increasingly bottlenecked by sample efficiency. What do we mean by that?

### [00:59 - 01:17]

Two things. First, while AI performs great in domains with large amounts of data, a common challenge faced in solving real-world problems with AI is that there is low availability of domain-specific knowledge resources, making it hard to train models offline through methods like SFT.

### [01:17 - 01:19]

Second, rollout is not easy.

### [01:19 - 01:29]

Rollout itself can be slow or expensive. If the LLM workflow or the verification process takes a long time, collecting data becomes a huge hurdle, even for online learning.

### [01:29 - 01:38]

Imagine training an AI that has to wait for a physical, real-world action to complete. No matter how fast your model is, the environment itself becomes the bottleneck.

### [01:38 - 01:47]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running,

### [01:47 - 01:48]

further exacerbating the sample's complexity.

### [01:48 - 01:49]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:49 - 01:50]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:50 - 01:51]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:51 - 01:52]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:52 - 01:53]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:53 - 01:54]

In parallel, we are seeing increasing use of agents for real-world applications. While integrations raise the system capabilities, the integrated tools are often long-running, further exacerbating the sample's complexity.

### [01:54 - 01:57]

running with verified rewards, where a model performs

### [01:57 - 02:00]

multiple rollouts in parallel, obtaining a reward at the end.

### [02:00 - 02:03]

Then an algorithm like GRPO converts these

### [02:03 - 02:06]

into gradients that are back-propagated to the model.

### [02:06 - 02:10]

But as we can see, each rollout contains a lot of information.

### [02:10 - 02:12]

The model's own internal chains of thought,

### [02:12 - 02:15]

tool calls, environment responses to the tool calls,

### [02:15 - 02:17]

including any error messages that could provide

### [02:17 - 02:18]

diagnostic value, and so on.

### [02:18 - 02:21]

Yet, RL only took a binary score and propagated

### [02:21 - 02:22]

that by gradient descent.

### [02:22 - 02:25]

Can we make use of the other information?

### [02:25 - 02:29]

The key idea is to perform reflective optimization

### [02:29 - 02:30]

in text space.

### [02:30 - 02:32]

Instead of only using the binary reward signal,

### [02:32 - 02:36]

we have an LM look at the traces of all the rollouts,

### [02:36 - 02:39]

reflect on what worked, and diagnose any failures.

### [02:39 - 02:41]

For example, in a code generation pipeline,

### [02:41 - 02:44]

the compiler returns an error that a certain API

### [02:44 - 02:46]

is unavailable.

### [02:46 - 02:48]

The model could then reflect on this

### [02:48 - 02:51]

and immediately learn to use a different API.

### [02:51 - 02:52]

This reflection uses all

### [02:52 - 02:56]

intermediate outputs across different agent steps

### [02:56 - 02:59]

and potentially even other tools, such as retrieval.

### [02:59 - 03:02]

Next, instead of updating only the weights of the model

### [03:02 - 03:05]

with small deltas, the model could update a prompt.

### [03:05 - 03:09]

A single natural language change can give a large behavior shift.

### [03:09 - 03:12]

Imagine changing generate a one-line summary

### [03:12 - 03:16]

to generate a 10-line summary in a summarization system,

### [03:16 - 03:19]

a one-word change that significantly alters

### [03:19 - 03:22]

the model behavior, something that would take thousands of weight

### [03:22 - 03:22]

updates.

### [03:22 - 03:25]

To get combining these two ideas,

### [03:25 - 03:28]

the model can now learn from as few as one

### [03:28 - 03:32]

rollout by reflecting and updating its own prompt.

### [03:32 - 03:34]

With this key insight, we propose the JEPA optimizer,

### [03:34 - 03:36]

which learns from textual feedback in addition

### [03:36 - 03:39]

to numeric rewards during training,

### [03:39 - 03:41]

akin to doing reinforcement learning in text space.

### [03:41 - 03:44]

JEPA is a genetic algorithm treating prompts

### [03:44 - 03:48]

as its gene pool, mutating a prompt from its pool every step.

### [03:48 - 03:49]

It has a multi-objective selection

### [03:49 - 03:52]

as its key ingredient, which we will come to next.

### [03:52 - 03:55]

Here, we compare JEPA against GRPO,

### [03:55 - 03:58]

one of the leading RL with verified rewards method.

### [03:58 - 04:00]

JEPA achieves twice the performance improvement

### [04:00 - 04:03]

that GRPO gets after 25,000 rollouts

### [04:03 - 04:06]

in just one round of reflection using as few as three data

### [04:06 - 04:07]

points.

### [04:07 - 04:11]

Continuing, JEPA, for a few more iterations, doubles that gap.

### [04:11 - 04:15]

Note that QEN 3.8b is optimizing itself here.

### [04:15 - 04:17]

There is no external teacher involved.

### [04:17 - 04:19]

And what does JEPA learn?

### [04:19 - 04:23]

JEPA, instead of leveraging model idiosyncrasies

### [04:23 - 04:25]

like some prior prompt optimizers did,

### [04:25 - 04:28]

JEPA instead generates a complete system specification.

### [04:28 - 04:30]

Here, we see the prompt generated

### [04:30 - 04:33]

by JEPA for a multi-hop question-answer system.

### [04:33 - 04:35]

Even with GPT 4.1 Mini, the generated prompt

### [04:35 - 04:37]

includes a full problem specification,

### [04:37 - 04:40]

latent requirements, a solution strategy, and output

### [04:40 - 04:42]

format details.

### [04:42 - 04:45]

Each new generation of models has better instruction

### [04:45 - 04:49]

following capabilities, which means precise task specification

### [04:49 - 04:49]

enables.

### [04:49 - 04:52]

Increasingly powerful models, too, perform better.

### [04:52 - 04:55]

And that's exactly what JEPA discovers.

### [04:55 - 04:58]

JEPA can also optimize proprietary black-box models

### [04:58 - 04:59]

to improve itself.

### [04:59 - 05:02]

Here, JEPA optimizes GPT 4.1 Mini,

### [05:02 - 05:07]

which outperforms even the full GPT 4.1 on live bench math

### [05:07 - 05:09]

after just a few rounds of reflection.

### [05:09 - 05:10]

Coming back to sample efficiency,

### [05:10 - 05:13]

JEPA is able to optimize LLMs to write code

### [05:13 - 05:16]

for novel hardware accelerators with almost no pre-training

### [05:16 - 05:18]

data available, starting from just 4.25 minutes.

### [05:18 - 05:23]

4.25% with GPT 4.0, JEPA achieves 7x higher performance

### [05:23 - 05:25]

at 30.52%.

### [05:25 - 05:27]

So how does it work?

### [05:27 - 05:28]

JEPA is a very simple algorithm, which

### [05:28 - 05:31]

receives a training set along with your agent,

### [05:31 - 05:34]

parameterized by some prompts and an evaluation metric.

### [05:34 - 05:38]

We split the provided train set into a dev and val sets.

### [05:38 - 05:40]

It also initializes a score matrix

### [05:40 - 05:43]

to track the performance of each candidate on each validation

### [05:43 - 05:47]

item, specifically noting the best candidate on each val

### [05:47 - 05:48]

item, forming the Pareto frontier.

### [05:48 - 05:52]

Then, JEPA proceeds in iterations.

### [05:52 - 05:56]

Every iteration, JEPA selects a prompt from the Pareto frontier

### [05:56 - 05:57]

to improve.

### [05:57 - 06:00]

It runs this prompt on a mini batch of dev examples,

### [06:00 - 06:04]

noting any intermediate feedback, like error messages.

### [06:04 - 06:08]

Then, it calls an LM to reflect and propose alternatives

### [06:08 - 06:10]

based on scores and the feedback.

### [06:10 - 06:12]

Finally, it updates the pool based

### [06:12 - 06:15]

on how the candidate scored on the val set,

### [06:15 - 06:17]

updating the Pareto frontier if necessary.

### [06:17 - 06:18]

But, JEPA is a very simple algorithm.

### [06:18 - 06:18]

JEPA is a very simple algorithm. JEPA is a very simple algorithm.

### [06:18 - 06:18]

JEPA is a very simple algorithm. JEPA is a very simple algorithm.

### [06:18 - 06:18]

JEPA is a very simple algorithm. JEPA is a very simple algorithm.

### [06:18 - 06:19]

JEPA is a very simple algorithm. JEPA is a very simple algorithm.

### [06:19 - 06:21]

Why is the Pareto frontier important to select

### [06:21 - 06:23]

the prompt to mutate from?

### [06:23 - 06:27]

As you can see on the left, simple iterative reflection

### [06:27 - 06:29]

often gets trapped in a local optimum,

### [06:29 - 06:31]

finding one improvement and then wasting

### [06:31 - 06:33]

its budget trying to top it.

### [06:33 - 06:36]

JEPA solves this using a Pareto based candidate selection

### [06:36 - 06:39]

strategy that balances exploration and exploitation

### [06:39 - 06:41]

to find much better solutions.

### [06:41 - 06:43]

Across four benchmarks, our Pareto approach

### [06:43 - 06:46]

consistently beats both TechGrad's select strategy

### [06:46 - 06:48]

and Microsoft Trace OptoPrime's Beam

### [06:48 - 06:53]

search even men measured in the same evolution hardness with the same amount of information

### [06:53 - 06:59]

available jeba is not the first to explore optimization in tech space so what makes a

### [06:59 - 07:04]

difference first the per instance burrito pool keeps best for instance preserving and propagating

### [07:04 - 07:10]

rare unique insights we perform global llm reflection as opposed to doing a local back

### [07:10 - 07:16]

prop which uses all available diagnostic feedback at every step and finally we use an evolutionary

### [07:16 - 07:21]

tree plus system aware merge that crosses prompts across modules improving across generations

### [07:21 - 07:28]

instead of doing a single generation pass as me pro did earlier i will now switch gears to talking

### [07:28 - 07:34]

about how ai is transforming optimization itself jepa is a part of a broader wave of optimization

### [07:34 - 07:40]

techniques that use llms as smart proposers even when a function is non-differentiable additional

### [07:40 - 07:45]

site information can enable an llm to propose meaningful improvements for example when

### [07:45 - 07:46]

optimizing a cuda kernel

### [07:46 - 07:51]

compiler and profiler output lets a smart proposer reason about what changes would make it faster

### [07:52 - 07:58]

a broad class of problems can be expressed as a text optimization problem given an evaluator

### [07:58 - 08:03]

that can provide a score along with some actionable site information like compiler

### [08:03 - 08:09]

traces sla violations etc any such problem can now be optimized using jepa's universal

### [08:09 - 08:16]

api optimize anything the api to use jepa is very simple just provide an evaluator function

### [08:16 - 08:20]

and define the set of problems that need to be solved and jepa will then handle the rest

### [08:21 - 08:27]

extending jepa beyond prompts we cast agent architecture search as a text optimization

### [08:27 - 08:32]

problem starting from a simple one-step chain of thought agent jepa is able to discover a

### [08:32 - 08:39]

six-step agent architecture that boosts gemini 3 flashes performance from 32 percent to 89 percent

### [08:39 - 08:46]

and almost 3x jump it similarly boosts gpt 4.1 nano's performance by over 20 percent

### [08:46 - 08:53]

on the math data set jepa can also improve the performance of multi-modal vlms for example

### [08:53 - 08:59]

here jepa is cutting the ocr error rate by almost 35 percent across different model scales

### [09:00 - 09:08]

jepa works across model scales from 1 billion to the latest frontier models here jepa improves gpt

### [09:08 - 09:15]

os's 120 billion to outperform claude opus while being 90x cheaper notably the improvement from

### [09:16 - 09:22]

jepa on claude is larger than on weaker models as model capabilities improve they benefit more

### [09:22 - 09:27]

from precise task specification which is often difficult for humans to specify

### [09:27 - 09:34]

and that is exactly what jepa discovered here jepa is now used across various organizations

### [09:34 - 09:39]

including startups and enterprises in production here the ceos of dropbox and shopify highlight

### [09:39 - 09:45]

their jepa usage and open ai recently had a blog post about building self-evolving agents with jepa

### [09:46 - 09:52]

jepa is also used across these organizations and has been used as the main methodology in several

### [09:52 - 10:00]

of these papers so in summary jepa can optimize anything representable in text so don't be afraid

### [10:00 - 10:05]

to optimize in the tech space and bring actionable site information to your problems many problems

### [10:05 - 10:10]

can be framed as optimization and jepa can use a variety of actionable site information to

### [10:10 - 10:16]

optimize anything including prompts agent harnesses kernels numeric parameters

### [10:16 - 10:21]

algorithms and much more the project is fully open source so please check it out here

### [10:21 - 10:24]

and thank you so much for my listening to my talk
