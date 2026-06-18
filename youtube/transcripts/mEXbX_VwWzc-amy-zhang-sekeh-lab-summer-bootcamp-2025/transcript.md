# Amy Zhang, UT Austin @ Sekeh Lab x NSF x SDSU Summer Bootcamp 2025

- URL: https://www.youtube.com/watch?v=mEXbX_VwWzc
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T20:01:45`

## Transcript

### [00:00 - 00:03]

Thank you for the very kind introduction and for inviting me here to give a talk.

### [00:04 - 00:13]

So yeah, a little bit about my journey. My journey has been a bit of a meandering one. I actually didn't start out in machine learning. I started out more on the electrical engineering side.

### [00:13 - 00:29]

In my undergrad and master's, I was working more on information theory, communication protocols, and that sort of thing. And that area is a very mature field, which means that it's very hard to come up with new results and do research.

### [00:30 - 00:40]

And so it's kind of a slog, and I'd actually started a PhD at UCSD, and in this area, in information theory, and I was like, I don't know what I'm doing here.

### [00:41 - 00:54]

And so I actually ended up quitting after about nine months, moved back up to the Bay Area, and then I started working on computer vision, deep learning, and I was like, wow, it is so much easier to make to get results in machine learning.

### [00:54 - 00:55]

This is so exciting.

### [00:55 - 01:00]

And then I realized, okay, I'm not a good enough software engineer to get results in computer.

### [01:00 - 01:05]

And so that's how I found myself in working on reinforcement learning.

### [01:06 - 01:17]

I particularly liked the mathematical framework of reinforcement learning, and so I ended up going back to do a PhD again, this time at McGill University in Montreal.

### [01:18 - 01:25]

After my PhD, I did a postdoc at Berkeley, and then I started at UT in the beginning of 2023.

### [01:25 - 01:30]

All right, so today I'd like to talk about how generationality.

### [01:30 - 01:34]

Genitive AI and reinforcement learning intersect.

### [01:34 - 01:47]

Basically, you know, I think especially in the last few years, there's been a lot of excitement around generative modeling, around generative AI, foundation models, large language models, because of the recent, like, very widespread success of these methods.

### [01:47 - 01:59]

And I really want to point out that, you know, I think reinforcement learning has kind of been a side note in all of this, but actually I think reinforcement learning is the way that we should be thinking about these problems.

### [01:59 - 02:00]

And I think.

### [02:00 - 02:09]

It's a way that we can move forward and continue to make progress in this space of generative modeling is is by looking at everything through a reinforcement learning lens.

### [02:09 - 02:13]

And so I hope by at the end of this hour I will be able to convince you guys of that.

### [02:13 - 02:17]

Okay, so I'm going to start with the story of chess.

### [02:17 - 02:26]

Many of you are familiar with AlphaZero, which came out of DeepMind, which is DeepMind's chess playing agent that was developed in 2018.

### [02:26 - 02:28]

You're probably also maybe familiar with DeepBlue, which is AlphaZero.

### [02:28 - 02:29]

You're probably also maybe familiar with DeepBlue, which is AlphaZero.

### [02:29 - 02:30]

You're probably also maybe familiar with DeepBlue, which is AlphaZero.

### [02:30 - 02:35]

Which was IBM's chess playing agent, which was developed in 1995.

### [02:35 - 02:42]

And this this machine famously beat Garry Kasparov, who was a chess grandmaster.

### [02:42 - 02:48]

But these were not the first attempts at developing a chess playing agent.

### [02:48 - 02:52]

So that actually started in the 70s in the 1770s.

### [02:52 - 02:55]

And so this was the chess playing agent.

### [02:55 - 02:57]

This was developed in Hungary.

### [02:57 - 02:59]

And it performed well against a wide array of human opponents.

### [02:59 - 03:06]

And won most of its games, including against Napoleon and Benjamin Franklin.

### [03:06 - 03:15]

And so here's just a picture of that system, along with the internal cogs that worked it and how this story usually ends is that it turns out that these clogs are just a facade.

### [03:15 - 03:17]

Literally.

### [03:17 - 03:18]

Right?

### [03:18 - 03:21]

The way that the machine worked was it?

### [03:21 - 03:23]

Actually there was a human hiding inside who was actually making all of the moves.

### [03:23 - 03:26]

And so there was an elaborate setup of mirrors so that you can open it up.

### [03:26 - 03:27]

So there was an elaborate setup of mirrors so that you can open it up.

### [03:27 - 03:28]

And you wouldn't be able to see the human hiding.

### [03:28 - 03:34]

to see the human hiding inside. And so people are disappointed by this, because once the secret is

### [03:34 - 03:40]

revealed, it means that there's no magic, right? The machine is no better than the human inside of

### [03:40 - 03:49]

it. So when we now zoom forward to 250, almost 250 years to today, the analogy is clear, right,

### [03:49 - 03:53]

to generative models. This is a feat of engineering, and it's impressed many into

### [03:53 - 04:00]

thinking that we've truly gotten to, you know, AGI, artificial general intelligence. But it turns

### [04:00 - 04:05]

out that if we peel back the mirrors, these foundation models are still no smarter than the

### [04:05 - 04:10]

humans on which they were trained, right? So today we have the technology to memorize the human's

### [04:10 - 04:15]

moves and encode it into these cogs. Now they're tiny silicon cogs rather than these copper ones

### [04:15 - 04:22]

in this image. But most AI machines today are simply mimicking the human data that they're

### [04:22 - 04:23]

trained on, rather than trying to make it work. And so I think that's a great way to

### [04:23 - 04:28]

to do better, right? So these imitation-based methods that we use to train current foundation

### [04:28 - 04:32]

models, it means that we're only ever going to get machines that do as well as

### [04:32 - 04:39]

the humans used to collect those data sets. And so today I want to talk about how we can

### [04:39 - 04:44]

potentially do better than imitation, and how this is a key ingredient missing in today's

### [04:44 - 04:50]

generative models. And so we're going to see how, also how generative models will provide some key

### [04:50 - 04:52]

ingredients that are missing from reinforcement learning.

### [04:53 - 04:58]

Okay. So for today, I just want to highlight the tight connections between GenAI and RL,

### [04:59 - 05:03]

and highlight how each provides a crucial tool for making progress in the other domain.

### [05:04 - 05:09]

So as the plan for today, we're going to introduce the basic and necessary components

### [05:09 - 05:13]

of the reinforcement learning framework, because I think we haven't yet seen that today,

### [05:13 - 05:17]

and so I think it's useful to get a better understanding of what the reinforcement

### [05:17 - 05:22]

learning framework is. Then we're going to talk about how generative models can be used

### [05:22 - 05:23]

in reinforcement learning.

### [05:23 - 05:28]

And then we'll describe how interaction can be framed as a generative model.

### [05:29 - 05:32]

And we'll talk a little bit about goal-reaching tasks in particular.

### [05:33 - 05:39]

And then we're going to talk about learning likelihoods and how we can use this

### [05:39 - 05:44]

in reinforcement learning. And finally, we'll just end on some future research

### [05:44 - 05:50]

directions that I'm particularly excited about. Okay, so let's now dive into this first part.

### [05:51 - 05:53]

So first, we'll talk about,

### [05:53 - 05:58]

you know, what is reinforcement learning? We'll introduce the key concepts. We'll review RL.

### [05:58 - 06:01]

And then we're going to talk about how generative models can be used as world models,

### [06:01 - 06:05]

how you can use it as a simulator, like how Ziad described in his talk.

### [06:07 - 06:13]

Then we're going to talk about data, right? So in the standard supervised learning setup,

### [06:13 - 06:17]

what we've seen so far today, the typical assumption is that you already have some

### [06:17 - 06:23]

offline pot of data that you're training on, data and labels. But in reinforcement,

### [06:23 - 06:27]

learning, you're typically interacting with an environment, which means that you're trying to

### [06:27 - 06:33]

collect data using a policy that you're learning. And so where you get your data from now becomes a

### [06:33 - 06:38]

question in reinforcement learning. And then finally, we're going to talk about how we can

### [06:38 - 06:43]

use generative models as the policy. Okay, so how does reinforcement learning work?

### [06:44 - 06:48]

So typically, the standard set of assumptions is that we have a policy,

### [06:48 - 06:53]

um, pi a given s. All right,

### [06:53 - 06:57]

I'm not going to, I'm not sure I'm going to be able to do this, use the mouse, but, um,

### [06:58 - 07:07]

uh, this I think is, uh, we have a policy and we have an environment. And we are taking actions in

### [07:07 - 07:12]

this environment. And we're going to get back observations from the environment. So the policy

### [07:12 - 07:16]

now takes in these observations as input and outputs actions based on those observations. And

### [07:16 - 07:23]

we're just going to keep doing this in this cycle. And then we're also going to get rewards from the

### [07:23 - 07:23]

environment.

### [07:23 - 07:29]

And so the policy is trying to visit states and actions that will give it high rewards. So for

### [07:29 - 07:36]

example, in a game, these rewards can correspond to points, such as in Tetris, maybe for an

### [07:36 - 07:41]

assistive robot. Rewards might be based on how well the robot enables a human to complete their tasks.

### [07:43 - 07:47]

And then we're often also going to talk about trajectories of experience,

### [07:47 - 07:51]

which is just means this kind of sequence of states and actions.

### [07:52 - 07:53]

And our goal,

### [07:53 - 07:58]

is, is to learn this policy, right? So, and so we're going to embed a machine learning model as

### [07:58 - 08:04]

this policy. All right. So the reinforcement learning objective basically consists of trying

### [08:04 - 08:09]

to, like we said, maximize the sum of future rewards that we're going to get back from the

### [08:09 - 08:14]

environment. So we're not just trying to maximize the rewards of today, but we'd also like to put

### [08:14 - 08:20]

ourselves in a position in a state that will allow us to get future, uh, high rewards tomorrow and

### [08:20 - 08:22]

the next day and so on and so forth. Right.

### [08:22 - 08:27]

Um, as an example, eating vegetables today will make you happier tomorrow. And so we're

### [08:27 - 08:31]

not trying to just maximize our current happiness by eating candy all the time.

### [08:31 - 08:39]

Uh, we typically also include this discount factor here, typically 0.9 or 0.99. And so what this

### [08:39 - 08:45]

discount factor does is basically all else things being, um, all else being equal, we would like to

### [08:45 - 08:50]

get rewards sooner rather than later, right? Um, if we only get one chocolate bar in our lives,

### [08:50 - 08:52]

we'd rather have that chocolate bar today,

### [08:52 - 08:58]

rather than, uh, in a year from now. And so we're going to also have this expectation.

### [08:59 - 09:04]

Um, and so the point of this expectation is that, that again, like I always said before,

### [09:04 - 09:10]

this objective doesn't depend on a dataset, right? This objective depends, um, this expectation that

### [09:10 - 09:17]

we're computing is over trajectories that are being collected from the environment by our policy.

### [09:19 - 09:20]

Okay.

### [09:22 - 09:26]

That's how one trajectory gets sampled because we're going to return this to this many times,

### [09:26 - 09:30]

right? So we have this initial state. So, you know, when we come online in our environment,

### [09:30 - 09:36]

where we are right now is our initial state sampled from some initial distribution. Our

### [09:36 - 09:40]

policy takes in that initial state and decides on the first action that it wants to take.

### [09:42 - 09:47]

The environment is going to react to that, that taken action, and it's going to change.

### [09:47 - 09:52]

And so that means the next state that we get back as one is going to be the update,

### [09:52 - 09:58]

um, of now what has happened according to that action. And so then, uh, now we do it again. We,

### [09:58 - 10:05]

uh, put that state back into our policy and we get the next action, right? And so the nice thing

### [10:05 - 10:12]

about looking at all of these as these probability distributions is that now we can start to see

### [10:12 - 10:16]

what are the parts that we can replace with a generative model, right? We could replace the

### [10:16 - 10:21]

initial state, that initial state distribution. We could replace the policy. We could replace the

### [10:21 - 10:22]

dynamics.

### [10:22 - 10:29]

Simulator. And so what also, what if, what if we think about this process as just layers of a

### [10:29 - 10:32]

deep neural network? And that's just a little bit of a teaser for later in this talk.

### [10:34 - 10:39]

Okay. So reinforcement learning, just to kind of bring this point home, reinforcement learning is

### [10:39 - 10:43]

not supervised learning, right? And I want to highlight the key similarities and differences.

### [10:44 - 10:50]

So for both RL and supervised learning, we have a model that's going to take in inputs and,

### [10:50 - 10:51]

and give out outputs, right?

### [10:51 - 10:52]

Right.

### [10:52 - 10:56]

So in a supervised learning case, we're taking in observations from the world and we're outputting

### [10:56 - 11:01]

labels. Um, so as an example, if we're trying to play Tetris, if we're training a model to

### [11:01 - 11:07]

play Tetris, you're going to record moves from a human player and do supervised learning in order

### [11:07 - 11:14]

to mimic those moves, right? And so that means our policy is only going to be as good as the human

### [11:14 - 11:22]

that is collecting those labels. So RL uses different rewards. It's not mimicry, but reward,

### [11:22 - 11:27]

optimization. So instead, we're going to take the Tetris score and point the number of points that

### [11:27 - 11:31]

you're getting in Tetris and use that as the reward that we're trying to maximize, which means

### [11:31 - 11:36]

that potentially we can train a reinforcement learning agent to policy that can outperform any

### [11:36 - 11:45]

human at playing Tetris. Okay. Um, so how can we use generative models to do RL better?

### [11:47 - 11:51]

Let's now talk about, uh, generative models as a world model.

### [11:52 - 11:59]

So the key challenge is that, uh, there are many tasks where data is going to be expensive

### [11:59 - 12:04]

or simulators are slow. We've already seen some examples of this in, in some previous talks,

### [12:04 - 12:10]

right? Um, so some examples of this are going to be nuclear fusion, right? How are we, we can't

### [12:10 - 12:16]

actually just do reinforcement learning from scratch, like on a fusion reactor, um, for in

### [12:16 - 12:20]

the atmospheric sciences, we can't just launch weather balloons and say, I don't know what's

### [12:20 - 12:22]

going to happen. Let's learn how to steer.

### [12:22 - 12:26]

We can't do it. You know, this weather balloon same with education and healthcare, right?

### [12:26 - 12:31]

Settings where humans are involved. We can't just randomly try actions and learn how to do

### [12:31 - 12:34]

better, right? You, you, you hopefully don't want your doctor to be doing that with you.

### [12:35 - 12:40]

And so there's a lot of these applications where we have no simulator. We, we, uh, we have no

### [12:40 - 12:44]

simulator. We only have a very slow simulator. And so what can we do? How can we learn good

### [12:44 - 12:51]

policies in these very safety critical or very expensive settings? So again, generative models,

### [12:51 - 12:58]

are may provide a key ingredient right so our solution is that we can use generative models

### [12:58 - 13:04]

as a simulator for learning and evaluating your policy so let's see how this would work let's say

### [13:04 - 13:10]

that we start with some data set we have a bunch of data corresponding to states actions and next

### [13:10 - 13:18]

states and so we're going to feed that into a world model generative model and so this is going

### [13:18 - 13:23]

to take in states and actions and output next state so we're just training the world model to

### [13:23 - 13:32]

mimic the data that we have so far right and so this world model can be it can you can take your

### [13:32 - 13:37]

pick of any kind of architecture it can be a generative adversarial network a gaussian process

### [13:37 - 13:42]

diffusion model and so on and so forth there are many possibilities that you can use here and so

### [13:42 - 13:47]

really your policy can now just practice on this simulator on this generative model

### [13:47 - 13:48]

you can take in states and actions and output next state so we're just training the world model to

### [13:48 - 13:51]

and then now we can use this policy and go back and collect more data

### [13:51 - 13:58]

and then use this to continue training your generative model and so this is one example

### [13:58 - 14:03]

of how you can use generative models in order to get better reinforcement learning algorithms

### [14:03 - 14:10]

all right so there are some opportunities and pitfalls with this approach right opportunities

### [14:10 - 14:14]

include you know if your generative model is very efficient where typically it's going to be a lot

### [14:14 - 14:18]

more efficient than the real world we're going to have very fast data collection you can now

### [14:18 - 14:23]

batch your data collection because you could just make multiple copies of your generative model and

### [14:23 - 14:28]

so now you can collect data even faster as long as you have enough compute data and training are

### [14:28 - 14:34]

now both going to be on gpu so that's very fast and efficient and we like that the problem with

### [14:34 - 14:39]

generative models with learning models as world models is that any errors are going to compound

### [14:39 - 14:43]

over time so let's just think about that a little bit right so if we pass in a state and action

### [14:43 - 14:48]

into our generative model and output and ask it to output next state they're probably just going to

### [14:48 - 14:52]

be a little bit of error there and so that next state is going to be a little bit off

### [14:53 - 14:56]

from the true next state that are the real environment would have given us

### [14:57 - 15:03]

but if we're now feeding that erroneous state back into our generative model

### [15:04 - 15:08]

then the next state that we that we get next the next output from that generative model is probably

### [15:08 - 15:12]

going to be even more wrong right and so that's what we mean when we say these errors are going

### [15:12 - 15:19]

to compound over time and so you know we also have a question of can i trust my model right

### [15:19 - 15:24]

if i've trained a policy using my model as a simulator and we know that our simulator has

### [15:24 - 15:29]

these errors am i going to feel comfortable deploying that policy out in the real world

### [15:32 - 15:38]

okay so we've talked about generative models as world models and some of the benefits and issues

### [15:38 - 15:42]

with using it as that and now i want to talk a little bit about jointly optimizing

### [15:42 - 15:47]

policy and data right so where does data come from in the supervised learning setting we

### [15:47 - 15:52]

typically just assume that there's already all of these nice curated data sets available for

### [15:52 - 15:57]

us which is generally true you know we have imagenet we have wikipedia we have reddit for

### [15:57 - 16:05]

language um in reinforcement learning the thing that you're learning is the parameters of your

### [16:05 - 16:08]

policy neural network right or the model of the world and so you're

### [16:08 - 16:12]

you don't have any data to start with right typically we're assuming

### [16:12 - 16:17]

that the policy is going to generate the data for us and then we can use that data to train

### [16:17 - 16:24]

our world model or to train our policy and so on and so forth right um but but now we so now

### [16:24 - 16:28]

in the reinforcement learning setup we have to think about data now as something that is also

### [16:28 - 16:36]

being optimized because we want a good policy in order to get good data right and so you can think

### [16:36 - 16:42]

about in the reinforcement learning framework that we're really trying to do this joint optimization

### [16:42 - 16:47]

both the data and the policy rather rather than just the model in supervised learning

### [16:48 - 16:54]

right so this is a chicken and egg problem where we need a good data set in order to train a good

### [16:54 - 17:02]

policy but we also need a good policy in order to collect good data right uh and so

### [17:03 - 17:08]

um if we think about this data as a trajectory or sequence of actions

### [17:08 - 17:11]

it's going to be visualized like this right so we have this example

### [17:12 - 17:15]

navigation problem where we're trying to go from this initial state to the goal

### [17:17 - 17:21]

and if we think about rl from a probabilistic perspective which is has been very successful

### [17:21 - 17:27]

for generative modeling we want to get a policy that uh that gets high returns right but we don't

### [17:27 - 17:32]

know which of these trajectories are actually going to get those high returns and so now these

### [17:32 - 17:39]

trajectories you can think of as a latent variable and so the general the gen ai perspectives gives

### [17:39 - 17:42]

us important tools for how we can think about solving this problem

### [17:42 - 17:47]

right and so um before we proceed further i just want to now introduce some notation

### [17:49 - 17:55]

uh so we're going to typically talk about the policy or model here as pi theta which takes in

### [17:55 - 18:01]

some previous trajectory or data as tau and then q tau is going to be the data that we've gathered

### [18:01 - 18:12]

so far all right and so when we write out the reinforcement learning objective uh we can see that

### [18:12 - 18:12]

here and then we write out the reinforcement learning objective uh we can see that here

### [18:12 - 18:15]

right so we're just trying to maximize we've just added a log in there

### [18:16 - 18:21]

which you can you can disregard but we're just trying to maximize this objective we're trying

### [18:21 - 18:27]

to maximize the log of the expected return uh return and the big r here just corresponds to

### [18:27 - 18:33]

the sum over our future rewards right and so it turns out that in general modeling

### [18:33 - 18:38]

there's a nice trick for figuring out how to learn this latent variable how to learn

### [18:38 - 18:42]

what this uh what this trajectory should be what a good trajectory is that has gives a

### [18:42 - 18:50]

me high return and that's an evidence lower bound and so we can apply this trick this elbow trick

### [18:50 - 19:00]

to our rl maximizing objective and it turns out that now this expression that it gives us

### [19:01 - 19:07]

is now actually jointly optimizing both our policy both pi theta and the data q

### [19:10 - 19:11]

yes

### [19:12 - 19:26]

oh you're right there is a typo there um yes there is a typo uh oh no no sorry there um

### [19:29 - 19:32]

pi theta rt

### [19:34 - 19:41]

um so i think we're just missing a parentheses but we're just adding in uh q over tau q q tau over q tau

### [19:41 - 19:41]

q over tau q q tau over q tau

### [19:42 - 19:49]

because that just is one and so we're adding that in and then um yeah yeah

### [19:52 - 19:55]

yes but there is a typo and so i should correct that in the slide

### [19:57 - 20:05]

okay um and so right so usually we think about q tau as a bucket of trajectories each with a

### [20:05 - 20:10]

different weight and so we can now also think about this as learning a parametric world model

### [20:10 - 20:13]

and so now we can take this optimal

### [20:13 - 20:18]

distribution of our data and plug it back in and solve for pi right

### [20:21 - 20:24]

and so one way of thinking about this objective on the last line here

### [20:25 - 20:32]

is that we're multiplying these two quantities our higher our return by our uh probability of

### [20:32 - 20:38]

uh of the trajectory right so sorry let me say that again um we're multiplying the reward

### [20:39 - 20:45]

our summed reward for a trajectory by the likelihood of that trajectory under our

### [20:45 - 20:50]

current policy and so we can see that we want to the way to that we maximize this

### [20:51 - 20:57]

is by trying to increase the likelihood of trajectories that give us high returns

### [21:00 - 21:08]

all right and so uh with so with that intuition we now are trying to optimize for pi

### [21:08 - 21:15]

to make this true okay so the complete algorithm now looks as follows we're going to sample

### [21:15 - 21:22]

trajectories from your policy weight those trajectories by the return and then we're

### [21:22 - 21:27]

going to try to maximize the likelihood of the high return trajectories and so this method is

### [21:27 - 21:34]

called reward weighted regression because you're basically just regressing your policy

### [21:35 - 21:37]

onto the reward weighted trajectories

### [21:39 - 21:45]

okay and so this last expression actually looks the same as a very standard algorithm that we use

### [21:45 - 21:49]

in reinforcement learning which is called policy gradient so maybe some of you have already heard

### [21:49 - 21:55]

about policy gradient because it's also what's used to fine-tune large language models so in

### [21:55 - 22:00]

rlhf typically what people do is you learn a reward model based on human preferences

### [22:00 - 22:07]

and then you use policy gradient to maximize that reward with the llm right so now we're just trying

### [22:07 - 22:07]

to

### [22:08 - 22:12]

maximize the human preferences for responses by making those responses

### [22:12 - 22:15]

more likely for the large language model to output

### [22:17 - 22:21]

and so the nice thing is that typically in reinforcement learning we actually come to this

### [22:21 - 22:25]

policy gradient objective from a slightly different angle but here we've actually come

### [22:25 - 22:32]

to it from using this elbow this this evidence lower bound from a more probabilistic generative

### [22:32 - 22:37]

modeling perspective and so it's nice to kind of see that you can come to the same objective from

### [22:37 - 22:38]

two very different perspectives

### [22:38 - 22:45]

okay so the key takeaway is that this generative modeling perspective on reinforcement learning is

### [22:45 - 22:51]

is not new but it does provide some key insights into data right how we should collect it how we

### [22:51 - 22:57]

can learn from it and so while we've been discussing how to optimize all of this uh

### [22:57 - 23:00]

how to optimize both the data set of trajectories as well as well as the policy

### [23:02 - 23:06]

we can also think about this as optimizing a model of the world

### [23:08 - 23:08]

all right

### [23:08 - 23:14]

and so now i want to start talking about generative modeling as the policy so

### [23:15 - 23:19]

one of the simplest ways in which people have been using generative models as policies

### [23:19 - 23:25]

is uh one example work is this work called decision transformer where they're just training

### [23:25 - 23:31]

a transformer to uh with a supervised learning objective an auto-aggressive objective to mimic

### [23:31 - 23:37]

trajectories of data that we already have access to right so again it should be pretty obvious to us

### [23:37 - 23:38]

that if we are using generative models as policies we're going to be using generative models as policies

### [23:38 - 23:40]

as the only anys that we have available in that offline data set as opposed to just

### [23:40 - 23:42]

the auger of a single requirement on that so what we're trying to do is if we are assuming that we

### [23:42 - 23:48]

have this big bucket of data and we're training a transformer to just auto regress on that sequence

### [23:48 - 23:54]

of data that we're only going to get the same behavior as what's available in that offline

### [23:54 - 24:00]

data set but it turns out that you can actually take the reward achieved by each of those

### [24:00 - 24:06]

trajectories and train the transformer conditioned on that reward to go

### [24:06 - 24:08]

and now you can at test time you can actually pass an trickset and then at test time you can actually pass an outcomes to

### [24:08 - 24:14]

pass in a higher reward to go to that transformer and it can somewhat generalize and actually

### [24:14 - 24:20]

attempt to return trajectories that can achieve that higher score so it's a very simple somewhat

### [24:20 - 24:25]

naive method it turns out that we can do something a little bit nicer with diffusion policies

### [24:26 - 24:31]

so in this setting I want to train an optimal policy from an offline data set and I want to

### [24:31 - 24:38]

do it with a diffusion model and so I can first again just train this diffusion model to imitate

### [24:38 - 24:44]

my behavior policy but now I want to ask again how do I improve upon this behavior policy we

### [24:44 - 24:50]

can do the same thing we did last time we can condition the diffusion model on the return

### [24:50 - 24:56]

but it turns out that I can do something slightly better than that with diffusion models you can

### [24:56 - 25:03]

actually guide the diffusion model at sampling time to output better actions and you can do

### [25:03 - 25:07]

this by using a guidance term so some possible guides that you can use

### [25:08 - 25:13]

are going to be your reward function or your Q function so the Q function just outputs the

### [25:13 - 25:20]

predicted return for a specific reward function and it turns out that that um the way that I'm

### [25:20 - 25:28]

going to sample from my diffusion model is that uh the or the the policy that I end up learning from

### [25:28 - 25:35]

my diffusion model is going to look like follows I'm going to have this first oops this first term

### [25:36 - 25:36]

um

### [25:37 - 25:37]

which

### [25:38 - 25:42]

is just trying to maximize the likelihood of the action in my data set right so that's just

### [25:42 - 25:47]

the standard supervised learning loss but I also have a weighted guidance term that

### [25:47 - 25:56]

says I also want to try to maximize my Q function and so guide based methods basically uh can drift

### [25:56 - 26:02]

the generated actions to do better than what's in the data set and try to uh try

### [26:02 - 26:07]

to maximize the Q function and so I just want to note that this is happening not

### [26:07 - 26:10]

during training but at inference time when we're sampling from our diffusion model

### [26:13 - 26:16]

and so diffuser is just one example of a model that does this

### [26:17 - 26:21]

and here are just some examples

### [26:23 - 26:26]

let's try this again it was just very fast

### [26:29 - 26:37]

okay it won't play anymore uh okay but you basically saw in this maze task right that we can start with random noise

### [26:37 - 26:42]

with all of these states kind of like over the maze environment and the diffusion model is

### [26:42 - 26:47]

basically slowly denoising that trajectory to get the shortest path through the maze

### [26:48 - 26:54]

and so the guidance that we're using at sampling time will just correspond to the length of that

### [26:54 - 27:00]

path right and so the guidance term that we're using in this example is just saying I want to I

### [27:00 - 27:06]

want to minimize the length of the path and so I can now guide my diffusion model to output actions that correspond

### [27:06 - 27:13]

respond to a shorter path in this maze. And so I can have another example of block stacking.

### [27:15 - 27:20]

And this is unconditional stacking. So here I'm just trying to maximize the height of this block

### [27:20 - 27:24]

tower with no other constraints. And so my guidance term just corresponds to what is the height of my

### [27:24 - 27:31]

block tower so far and I want to maximize it. I can also do this with conditional stacking and

### [27:31 - 27:36]

say that I have maybe some test time constraints. Maybe I don't want to put gray blocks on top of

### [27:36 - 27:42]

the blue ones. And so my guidance term is basically going to give me a penalty if I do that.

### [27:42 - 27:48]

And I can now learn to stack blocks at test time as long as I have access to that guidance term.

### [27:48 - 27:52]

And so I want to point out that that guidance term is something that I'm assuming is is probably

### [27:52 - 27:57]

going to be some learned function. But once I have it, I can swap in and out different score

### [27:57 - 28:06]

functions and just use that same pre-trained diffusion model to get policies. Okay so there

### [28:06 - 28:06]

are a lot of different ways to do this. There are a lot of different ways to do this. There are a

### [28:06 - 28:12]

also a slightly different type of approach that we can use to try to get better behavior out of a

### [28:12 - 28:16]

diffusion model. And so that's called a select based approach. So here we're just going to

### [28:16 - 28:20]

generate a bunch of candidate actions from our behavior policy. So we've trained this diffusion

### [28:20 - 28:25]

model to just mimic the behavior data set. We're going to sample a bunch of actions from it and

### [28:25 - 28:31]

then we're going to use again some criterion like a reward function or Q function to select out of

### [28:31 - 28:36]

that set of actions. Right and so I'm just going to want to select an action that has

### [28:36 - 28:43]

a high reward or a high Q function, a high Q value from that set of actions. And so one example

### [28:43 - 28:48]

method is called implicit diffusion Q learning. And so this is just a modification of an existing

### [28:48 - 28:53]

offline reinforcement learning method that I'm not going to get too much into. But we're basically

### [28:53 - 29:01]

just going to replace the standard more simplistic Gaussian policy learned from the original method

### [29:01 - 29:06]

with a diffusion model. We're going to train a Q function and I'm not going to get into how

### [29:06 - 29:13]

to do that. But we're going to weight samples from this diffusion policy using the Q function

### [29:13 - 29:16]

that we've learned. So we're going to use importance sampling to basically just pull

### [29:16 - 29:21]

out high value actions. And I just want to point out in this really simple example, so here I've

### [29:21 - 29:27]

just created, I just have a 2D bandit problem which just means I have these like 2D actions.

### [29:27 - 29:35]

And so I have these clusters of actions on the left hand side and the color represents the reward

### [29:35 - 29:36]

that it gives me. Right.

### [29:36 - 29:43]

So blue is low reward and red is high reward. And so I can see that I would like to select

### [29:43 - 29:50]

actions that correspond to that red cluster. So if I train a Gaussian policy based on this data,

### [29:50 - 29:57]

it kind of mixes up these clusters and doesn't do a really great job. And so I'm kind of getting all

### [29:57 - 30:03]

of these different erroneous clusters of actions from my Gaussian policy, whereas a diffusion

### [30:03 - 30:05]

policy is actually able to

### [30:06 - 30:11]

correctly model each of those clusters and select out the ones that have high value.

### [30:14 - 30:20]

Okay. So it turns out that we can actually combine both of these steps. We can combine both the guide

### [30:20 - 30:31]

and select steps. And I also want to talk about, so using both guide and select can be error prone.

### [30:31 - 30:34]

There are some issues with both of these approaches.

### [30:36 - 30:41]

One is that your diffusion model can have approximation error in modeling this complicated

### [30:41 - 30:47]

policy distribution. And the other is that your critic, your Q function, can also have error

### [30:47 - 30:54]

in evaluating unseen actions. And so even though your diffusion model is trained on offline data,

### [30:54 - 30:59]

the more you sample from it, the more likely it is that you're accidentally going to sample an

### [30:59 - 31:04]

action that wasn't actually in your data set, which is just caused by an error in your diffusion model.

### [31:06 - 31:11]

And if you pass in those OODI actions into your value function, your value function can also give

### [31:11 - 31:19]

you wrong estimated Q values. And because we're trying to take a max of that Q value, it's very

### [31:19 - 31:26]

likely that it's even more likely that the highest value in that set is going to be a mistake from

### [31:26 - 31:31]

their value function. And so, as a result, the generation of high quality actions with

### [31:31 - 31:34]

these existing methods is affected by this kind of error exploitation.

### [31:36 - 31:50]

So in this in this method we're going to do something slightly different, which is instead of using as a guidance term the reward function or Q function which we've established the Q function can can have errors we're actually going

### [31:50 - 32:01]

to instead use the density ratio. So this density ratio just corresponds to the likelihood of the correct action.

### [32:01 - 32:15]

So the density star here corresponds to the optimal policy, or our current policy in practice over the probability of us taking that action from our current state s present in the data set.

### [32:15 - 32:25]

And i'm not going to talk about how we learn this density ratio, but there are a lot of existing approaches looking into how we learn this, and so those methods are called dice methods.

### [32:25 - 32:31]

So, and then the select step is very standard so again we're just going to generate a few candidate actions and use the Q.

### [32:31 - 32:37]

Step one with the highest value right and again I just want to show a very classic example.

### [32:37 - 32:45]

Again of the of a 2d bandit problem. So on the upper left hand side we have our action distribution.

### [32:45 - 32:52]

So yellow is where we have a lot of sampling of actions, and in dark blue we don't have a lot of actions.

### [32:52 - 32:58]

Right. So we don't have a lot of actions in that very center dot, and we don't have a lot of actions in those corners.

### [32:58 - 33:01]

So if we train a diffusion behavior policy on that data.

### [33:01 - 33:08]

We see that in the center it's not it's not looking very accurate right because we have no data there.

### [33:08 - 33:14]

And then our true reward function is, you can see, has these 2 rings, these annular rings.

### [33:14 - 33:21]

And because I have no data in that center I don't expect my method to be able to select actions from that center.

### [33:21 - 33:31]

So what i'm hoping to see is that my my my policy, my optimal policy at the end is going to try to select actions in that bigger yellow ring.

### [33:31 - 33:42]

That's the dot side. And so again we can see that our learned reward function based on that data set has this error right because it doesn't see anything in the center.

### [33:42 - 33:46]

It has erroneously predicted that there is going to be high reward in that center.

### [33:46 - 33:49]

So let's look at what happens across some different methods.

### [33:49 - 33:56]

So here we have a select only method and a guide only method first, and we'll look at them right.

### [33:56 - 34:00]

So in the select only method it means that we're not doing a guidance step.

### [34:00 - 34:08]

So all we're seeing is our diffusion model fitting to the behavior data set that action distribution that we saw in the last slide.

### [34:08 - 34:15]

And because our diffusion model was inaccurate it's erroneously predicting these high actions in the center.

### [34:15 - 34:24]

Right. And so when we sample from it we are getting actions in the center that we shouldn't same thing is happening with our guide only method.

### [34:24 - 34:29]

Our guide only method. Our critic is erroneously thinking that there's high value actions in the center.

### [34:29 - 34:37]

And so we're accidentally selecting for them, or we're so we're sampling from our diffusion model, there's no select steps so the bottom looks the same as the top.

### [34:37 - 34:42]

And so again we're kind of we're doing not a very good job of selecting actions.

### [34:42 - 34:50]

Whereas our method that is doing guide and then select right so we're guiding the diffusion model.

### [34:50 - 34:57]

The the output the actions that are being output by the diffusion model using that density ratio as a guidance term.

### [34:57 - 35:06]

We're actually only selecting the best ones out of those, and so we see that we can get this really nice ring of actions.

### [35:06 - 35:08]

Okay.

### [35:08 - 35:21]

So we've looked at a couple of different ways in which we can use transformers diffusion models generative models as policies, and some very toy examples. Right. So, a policy, we've established is a generative model.

### [35:21 - 35:25]

And I want to just revisit policy gradient again right so we saw policy gradient.

### [35:25 - 35:26]

Where we were computing.

### [35:26 - 35:34]

The elbow of our objective of trying to maximize the expected return our expected sum over rewards.

### [35:34 - 35:40]

Right. So the more standard way of deriving policy gradient is shown here.

### [35:40 - 35:47]

So again, we're just taking our objective, which is trying to maximize our expected sum over rewards.

### [35:47 - 35:55]

And we can actually just compute the derivative directly of this objective, and this is how we get typically how we get policy gradient.

### [35:55 - 36:09]

And so it turns out that this thing that we have on the right hand side right the derivative of the log probability of our trajectory is also called our square function.

### [36:09 - 36:18]

And so it turns out that we're also optimizing for a score function with policy gradient, which is exactly what we're doing with generative models.

### [36:18 - 36:23]

And so now this leads us to a question which is, can we actually train diffusion models with reinforcement learning.

### [36:23 - 36:27]

And it turns out that the answer is yes.

### [36:27 - 36:35]

So let's step back a bit and just think about what does it mean to think about diffusion models from an oral perspective, right so let's formalize this.

### [36:35 - 36:41]

Let's think about how diffusion can be cast as a Markov decision process as an MVP.

### [36:41 - 36:47]

So our states can be the noisy image at each diffusion step.

### [36:47 - 36:51]

Our actions correspond to how we do noise.

### [36:51 - 36:53]

So what the prediction is.

### [36:53 - 36:58]

What the predicted noise is which is the output of our diffusion model.

### [36:58 - 37:07]

Our reward can be just some final utility function such as, you know, image aesthetics or compressibility.

### [37:07 - 37:13]

And so, so here's how we can kind of like cast the diffusion model as an MVP.

### [37:13 - 37:21]

And now it turns out that we can take that that framework, and just directly train diffusion models with policy gradient.

### [37:21 - 37:30]

So we're going to fine tune diffusion models, using reinforcement learning over the denoising trajectory.

### [37:30 - 37:39]

And I want to point out that this is different from how we typically train diffusion models right because typically we're doing something that looks more like supervised learning.

### [37:39 - 37:46]

We're trying to maximize the likelihood that the diffusion model is going to output, something from the data set it was trained on.

### [37:46 - 37:49]

But now we're going to apply policy gradient to maximize.

### [37:49 - 37:52]

Some score function some reward.

### [37:52 - 37:59]

So why would we want to do this, why would we want to do this instead of maximizing likelihood.

### [37:59 - 38:04]

One example would be that we're trying to optimize for some qualitative metric.

### [38:04 - 38:15]

That's not easily captured by likelihood and again some examples for this can be just sort of aesthetic score or compressibility or alignment with some prompt.

### [38:15 - 38:18]

And so this is fundamentally different from what we've seen so far.

### [38:18 - 38:26]

Because everything we've seen beforehand was about how we can sample better from a pre trained model generative model.

### [38:26 - 38:33]

And here we're talking about how can we change the way that we train generative models by training them with reinforcement learning.

### [38:33 - 38:38]

And so I just want to show a really cool example of what's possible when you train with reinforcement learning.

### [38:38 - 38:47]

So here is a diffusion model that's being trained, so so the x axis here just corresponds to training over time.

### [38:47 - 38:54]

And I want to just show this again, because each of these will just let me do it again.

### [38:54 - 39:03]

Okay, each of these just corresponds to different score functions right compressibility aesthetic quality prompt image alignment according to some Vlm.

### [39:03 - 39:10]

And so you can see how the diffusion model output changes over time according to the score functions right.

### [39:10 - 39:15]

So again, I want to show that again, because a standard diffusion model.

### [39:15 - 39:25]

Is typically just trying to, you know, recreate the original image, or there's some, you know, label of like of what you want the diffusion model to create.

### [39:25 - 39:29]

But here it's completely open ended it's just trying to maximize for some score.

### [39:29 - 39:39]

So that was pretty cool. Okay, so we've shown that generative models can be framed as Mdps that we can train generative models with Rl.

### [39:39 - 39:44]

We've seen that we can incorporate generative models into Rl.

### [39:44 - 39:50]

And train world models or policies using generative models.

### [39:50 - 39:52]

And so in this next part.

### [39:52 - 39:59]

I want to take this one step further, which is that in the same way that generative models today are trained with data as supervision.

### [39:59 - 40:03]

Can we think about reinforcement learning from this data only perspective?

### [40:03 - 40:08]

Right.

### [40:08 - 40:10]

So here.

### [40:10 - 40:12]

So the key idea is that.

### [40:12 - 40:13]

An agent.

### [40:13 - 40:19]

Is iteratively interacting with an environment is a generative process.

### [40:19 - 40:28]

Right. So if we can condition our policy, then our policy can generate for us different outputs, which just corresponds to different trajectories.

### [40:28 - 40:34]

So generative models are trained on data to maximize likelihoods.

### [40:34 - 40:38]

So where do rewards come in right there's one bit about this Rl.

### [40:38 - 40:41]

As Jenny I story that doesn't really quite fit right which is still the reward function.

### [40:41 - 40:44]

Right.

### [40:44 - 40:47]

The problem with Rl.

### [40:47 - 40:51]

Is that we're defining the problem in terms of this scalar reward.

### [40:51 - 40:55]

When we want to teach an image classifier to identify cats and dogs, we give it data.

### [40:55 - 41:00]

Right. We give it a bunch of images accompanied by labels, which is just more data.

### [41:00 - 41:09]

But when we want to teach an Rl policy to play pong, we have to write a bunch of code describing that assign scalar values to each observation.

### [41:09 - 41:17]

And so these reward functions make it really challenging to think about how Rl fits into this broader machine learning landscape.

### [41:17 - 41:26]

And so it makes it really challenging for non-experts and even experts to use our own practice, because this reward design aspect can be really hard.

### [41:26 - 41:37]

And so right now what we're hoping to do is we're going to try and remove this reward, or we're going to try and think about reinforcement learning from a perspective that that removes reward.

### [41:37 - 41:42]

And so just to hammer this point home again.

### [41:42 - 41:50]

I just have here some example code from a very common benchmark in reinforcement learning called Meta World.

### [41:50 - 41:55]

And so Meta World just consists of these simulated manipulation tasks with a robot.

### [41:55 - 42:00]

But this is an example of what a reward function looks like for one task in Meta World.

### [42:00 - 42:05]

Right. And there's like a 100 tasks in Meta World. So you can see that this is something that hinders us from being able to create new tasks.

### [42:05 - 42:06]

Right.

### [42:06 - 42:07]

Right.

### [42:07 - 42:11]

And this is something that hinders us from being able to create new generalist agents with reinforcement learning.

### [42:11 - 42:14]

So reward design can be prohibitively difficult.

### [42:14 - 42:18]

It often requires a lot of expert domain knowledge.

### [42:18 - 42:24]

And so we'd like to ask the question, How can we actually define many tasks while avoiding this problem?

### [42:24 - 42:28]

And so one thing that we can look at is goal conditioned reinforcement learning.

### [42:28 - 42:36]

So reaching goals is a classic pro problem dating back to the early days of machine learning and has many practical applications, including robot navigation.

### [42:36 - 42:41]

path planning and route optimization, chemical synthesis, autonomous driving, and gains.

### [42:43 - 42:49]

And so what is the goal? Ideally, we just want to reach the goal as quickly as possible,

### [42:49 - 42:54]

and we would like to stay there for as long as we can. And so the nice thing about this

### [42:54 - 43:00]

goal-reaching problem is that the reward function is often already defined for us, right? It looks

### [43:00 - 43:04]

as follows. You can define this as an indicator function that just says, I'm going to receive a

### [43:04 - 43:12]

reward of 1 when I've reached my goal, and 0 otherwise. So how can we actually think about

### [43:12 - 43:17]

this in terms of probabilities? Again, our objective is that we would like to learn a

### [43:17 - 43:24]

policy to maximize the expected cumulative discounted sum of rewards. So here's our

### [43:24 - 43:28]

objective. For goal-reaching, we can just plug in that indicator function as the reward.

### [43:29 - 43:34]

But what happens to this objective in continuous settings? In continuous settings,

### [43:34 - 43:39]

it's very, very unlikely that we're going to reach the exact same state that we've specified

### [43:39 - 43:47]

as a goal, right? And so this probability goes to 0. And so this is what we call a measure 0 event.

### [43:50 - 43:54]

OK. So in the coming sections, we're going to think about goal-reaching in a different way.

### [43:54 - 43:59]

We're going to think about it in terms of probabilities. So instead of thinking about

### [43:59 - 44:04]

the time you spend at a goal, we want to think about the probability that you get to a goal.

### [44:04 - 44:11]

Right? So what's the reward? We can now write this reward in terms of this probability.

### [44:12 - 44:17]

And we just have this 1 minus gamma term in order to make sure that our probability sums to 1.

### [44:18 - 44:23]

And so now our reward is defined in terms of probabilities over states,

### [44:23 - 44:28]

which is much better than reward. All right. So we're going to formalize this a little bit more.

### [44:30 - 44:33]

In order to understand this a little bit better, we're going to introduce this term,

### [44:33 - 44:34]

which is called the discounted sum of rewards. So we're going to formalize this a little bit more.

### [44:34 - 44:40]

So this is a discounted state occupancy measure. So imagine that you close your eyes and you're

### [44:40 - 44:45]

going to open them after some random number of time steps. And you want to know at that future

### [44:45 - 44:52]

point in time, what action, sorry, what state am I going to be at? So this discounted state

### [44:52 - 44:56]

occupancy measure basically gives us the probability that we're going to see some

### [44:56 - 45:04]

future state SF at some point. And we can also write this down in terms of in the form

### [45:04 - 45:16]

of a conditional probability. So we can write this in for other types of probabilities. So we can write this for, you know, probability of seeing some future state condition on the fact that I'm in a current state.

### [45:17 - 45:26]

We can write this down in terms of a conditional probability, given that I'm in a current state, and I'm going to take some action A or some other latent variable.

### [45:30 - 45:30]

And so

### [45:32 - 45:34]

when we've been talking about RL so far,

### [45:34 - 45:40]

we've been talking about the standard primal form of reinforcement learning, where we're trying to maximize this reward function.

### [45:41 - 45:46]

It turns out that in optimization there's something that's also called the dual form of your problem.

### [45:46 - 45:56]

So if in the primal form I'm trying to maximize some objective, there is an equivalent problem, the dual form, where I'm trying to minimize some objective.

### [45:56 - 46:01]

And so it turns out that in dual reinforcement learning, we're actually going to switch out our optimization variables.

### [46:01 - 46:03]

So if we want to turn this into a minimization problem,

### [46:03 - 46:20]

we're going to actually try to minimize the we're going to talk about this in terms of occupancy measures, and we're going to be trying to minimize the distance between the probability distribution under my current policy and some target distribution, which is my goal.

### [46:22 - 46:31]

Alright, so we're going to start with a really simple method for using generative models to get to a goal, and that's just going to be goal-conditioned imitation learning.

### [46:31 - 46:37]

And so this objective is again, we can think about this in terms of maximizing likelihood.

### [46:37 - 46:47]

We're just trying to train a goal-conditioned policy that maximizes the likelihood of returning the action that is provided in my data set.

### [46:47 - 46:51]

And it turns out that I can use Bayes' rule to expand this out.

### [46:53 - 47:00]

And here beta just corresponds to my behavior policy or my data set distribution.

### [47:01 - 47:05]

And this first term should look very familiar, right?

### [47:05 - 47:15]

So we're just trying to select actions that maximize your expected reward, while also staying close to the likelihood of the actions in the data as a form of regularization.

### [47:15 - 47:23]

So this is really simple. This is very intuitive, and it turns out that this kind of method is actually very effective in practice in robot learning.

### [47:23 - 47:29]

But again, this is relying on this assumption that we have some offline data set that's pretty good.

### [47:29 - 47:31]

So what about the online setting?

### [47:33 - 47:40]

It turns out that we can actually think about training a goal-conditioned policy by minimizing a different kind of objective.

### [47:40 - 47:56]

And so here we're just trying to minimize the F divergence between the probability distribution over states under my current policy, so that's this P theta, and our goal distribution policy, Pg of s.

### [47:56 - 47:58]

So in the goal-conditioned setting, Pg is very similar.

### [47:59 - 48:06]

It's pretty simple. It just corresponds to a direct distribution where all of the mass is at our goal state.

### [48:06 - 48:14]

And so the intuition is that ideally we just want our agent to be in that goal state with high probability.

### [48:14 - 48:20]

And so we want the probability to be high at the goal state and low everywhere else.

### [48:20 - 48:24]

So I just want to give a little bit of intuition for what this F divergence is.

### [48:24 - 48:28]

So there's several different F divergences.

### [48:28 - 48:33]

All of these just correspond to different distance metrics over probability distributions.

### [48:33 - 48:47]

And so if I have 2 distributions, P1 and P2, so P2 you can see here is my target distribution, and P1 is slowly over time moving closer and closer to P2 as they move closer together.

### [48:47 - 48:54]

I can see that these different F divergences the the value is basically dropping right?

### [48:54 - 48:57]

So as we get closer together, this notion of distance is getting smaller.

### [48:57 - 49:03]

So this is just to provide some intuition for what these different F divergences are doing.

### [49:03 - 49:16]

So now one question that I can ask is if I maximize that objective, or sorry, if I optimize for that objective, right, which is minimizing this F divergence between these probability distributions.

### [49:16 - 49:20]

The question that I want to ask is, does the policy that I get from that?

### [49:20 - 49:26]

Is that going to be the same policy as I get from maximizing my goal condition reward?

### [49:26 - 49:30]

And it turns out the answer is yes.

### [49:30 - 49:34]

So how do I actually optimize this objective?

### [49:34 - 49:39]

It turns out we can just compute the derivative.

### [49:39 - 49:46]

And if I look at this expression, it should look a lot like what we already saw before with policy gradient, right?

### [49:46 - 49:54]

I have this first term, which is computing the derivative of my log probability of my policy multiplied by.

### [49:54 - 49:55]

And what we saw before is that that's the same policy gradient.

### [49:55 - 49:59]

And what we saw before is that that second term is supposed to be your reward.

### [49:59 - 50:03]

But here instead I have again this density ratio, right?

### [50:03 - 50:17]

This this ratio of my the probability of being in a state under my current policy over the probability of being in that state in my goal distribution.

### [50:17 - 50:23]

Okay. So just to give some intuition for what different F divergences are doing.

### [50:23 - 50:36]

With this objective, you can see that in this example our goal just corresponds to that red dot in the middle left hand side.

### [50:36 - 50:49]

And so when I optimize for this objective before i've seen the goal, all of these methods basically are trying to spread out a uniform distribution over the entire state space.

### [50:49 - 50:51]

And then, as soon as they find the goal.

### [50:51 - 50:52]

It's going to try to.

### [50:52 - 50:58]

It's going to try to concentrate all of that probability mass onto that goal.

### [50:58 - 51:04]

And so you can see that across all of these different types of F divergences that they all basically do the same thing.

### [51:04 - 51:09]

They all kind of like have different dynamics learning dynamics.

### [51:09 - 51:12]

And so that's why they all look different at first.

### [51:12 - 51:17]

But in the end they all end up concentrating into the same policy.

### [51:17 - 51:21]

Okay. But what if my task can't be described by a goal?

### [51:21 - 51:28]

If I just want a robot to clean my apartment or pick a flight for me.

### [51:28 - 51:39]

These are tasks that aren't necessarily just easily described by goals right like I don't want to have to give a robot a picture of my clean room and say match this exactly.

### [51:39 - 51:43]

There are many possible ways in which my living room can be cleaned.

### [51:43 - 51:47]

I don't necessarily care that it has to match one particular image.

### [51:47 - 51:49]

Same with trying to reach somewhere.

### [51:49 - 51:50]

If i'm trying to go to Vancouver.

### [51:50 - 51:52]

If i'm trying to go to Vancouver for Icml.

### [51:52 - 51:57]

I don't necessarily want to pick the shortest path to get to Vancouver, because I care about other things.

### [51:57 - 52:03]

I care about what airline i'm taking what time of day i'm flying maybe where my layover is right.

### [52:03 - 52:14]

And so most tasks that we care about have more complex target distributions than just a single direct distribution at a goal state.

### [52:14 - 52:18]

Okay, So we thought about interaction.

### [52:18 - 52:19]

Being a generative model.

### [52:19 - 52:26]

This can be iterative denoising.

### [52:26 - 52:34]

And here we're just doing iterative computation to arrive at some sample

### [52:34 - 52:45]

We've also talked about how our all can be seen as a generative model that the environment and policy together are acting as a generative model to output different trajectories.

### [52:45 - 52:47]

And so if we want to think about.

### [52:47 - 52:54]

Reinforcement learning from a generative modeling perspective.

### [52:54 - 53:03]

We have to think about log likelihood, and we have to talk about how we can actually model estimate log likelihood both directly and indirectly.

### [53:03 - 53:09]

And we're going to show how this connects to Q functions.

### [53:09 - 53:14]

Okay, So we've talked about how reinforcement learning can be seen as sampling from a generative model, right?

### [53:14 - 53:16]

Because our policy is basically sampling from the environment.

### [53:16 - 53:20]

But we need to talk about log likelihoods.

### [53:20 - 53:23]

Sorry. Okay.

### [53:23 - 53:28]

So how do we actually estimate the likelihood of a certain sample?

### [53:28 - 53:34]

All right. So let's start by formally defining the likelihood.

### [53:34 - 53:40]

Let's see. Likelihood is exactly the same as that discounted state occupancy that we saw earlier.

### [53:40 - 53:43]

Right. So this expression should look pretty familiar.

### [53:43 - 53:45]

And again, I just want to note that this one minus gamma term.

### [53:45 - 53:55]

Is just used to make sure that we're normalizing our probability to one.

### [53:55 - 54:05]

So and and we want to estimate these types of likelihoods in order to train an interactive generative model which corresponds to our policy.

### [54:05 - 54:11]

Okay. So how can we actually estimate these likelihoods either directly or via density ratios?

### [54:11 - 54:14]

And then we want to talk about how can we actually do off policy evaluation?

### [54:14 - 54:15]

Right?

### [54:15 - 54:22]

Because again, everything that we've talked about so far, or when we talk about estimating likelihoods, the assumption is that the data is already there, right?

### [54:22 - 54:27]

We're estimating likelihood for some good data that we already have.

### [54:27 - 54:30]

But in reinforcement learning we have a chicken and egg problem.

### [54:30 - 54:36]

And so we'd also like to be able to compute the likelihood of one policy using data from another.

### [54:36 - 54:41]

We'd like to compute the likelihood of a better policy compared to the data that we have.

### [54:41 - 54:46]

And then we're going to talk about how we can use this to maximize arbitrary rewards.

### [54:46 - 54:58]

Okay, I think i'm pretty much out of time so i'm going to skip over this.

### [54:58 - 55:02]

Okay, we're not going to talk about likelihoods.

### [55:02 - 55:09]

I just want to point out one thing which is that it turns out that when we learn these likelihoods.

### [55:09 - 55:17]

We can actually add rewards back in.

### [55:17 - 55:23]

So if we multiply this likelihood by a reward, we get the optimal Q function.

### [55:23 - 55:27]

We get we get the Q function for that likelihood for that policy.

### [55:27 - 55:31]

And so we can now estimate our future return.

### [55:31 - 55:37]

Okay, so sorry i'm just gonna wrap this up because I totally lost track of time.

### [55:37 - 55:38]

Okay.

### [55:38 - 55:39]

Okay.

### [55:39 - 55:42]

So just as a takeaway.

### [55:42 - 55:49]

I we've seen how sorry.

### [55:49 - 55:53]

Okay, So we've seen how generative models and reinforcement learning can interact right?

### [55:53 - 56:02]

We can see how reinforcement learning can be used to train generative models to train generative models to do things beyond what is in the data that they we train them on.

### [56:02 - 56:08]

We've seen how generative models can be used in reinforcement learning to act as simulators to act directly as policies.

### [56:08 - 56:11]

We've seen that in reinforcement learning.

### [56:11 - 56:19]

One of the issues, one of the things that's kind of holding us back is the use of reward, and we've looked at ways in which we can go beyond reward.

### [56:19 - 56:29]

And some of the things that I didn't get a chance to talk about was actually how we can learn likelihoods, how we can optimize for arbitrary tasks using likelihood.

### [56:29 - 56:35]

And so I just want to end to say that I think that we need more research on reinforcement learning methods.

### [56:35 - 56:36]

And more specifically.

### [56:36 - 56:47]

I think we need more research on the dual perspective of reinforcement learning, and this allows us to move away from these hand design rewards.

### [56:47 - 56:53]

Actually, I thought it was pretty funny that in the earlier tutorial that you saw you.

### [56:53 - 56:57]

We had this same comic for standard supervised learning.

### [56:57 - 57:00]

But I think this applies to reinforcement learning as well, right?

### [57:00 - 57:05]

And it applies to how we train generative models, which is basically we're trying to just stir the pot.

### [57:05 - 57:08]

Stir the data and hope for something better right?

### [57:08 - 57:11]

But I think with better reinforcement learning methods we can do better than this.

### [57:11 - 57:18]

We can actually curate the kind of data that we get rather than rather than just kind of moving things around.

### [57:18 - 57:28]

And I the other thing I wanted to point out is that the touring award last year was awarded to the fathers of reinforcement learning Sutton and Bardo.

### [57:28 - 57:34]

And so I I think that kind of shows that the general community is starting to realize how important reinforcement learning is.

### [57:34 - 57:38]

And you know, in this picture I just wanted to show that the capability is of Rl.

### [57:38 - 57:47]

Today just kind of correspond to this like little peak of the iceberg that you can see over above the surface of the ocean.

### [57:47 - 57:54]

But there's a lot of possible future capabilities there's a lot of future directions, especially in generative modeling that i'm really excited about.

### [57:54 - 57:59]

And I hope that this talk has served as a bit of a teaser for that, and I apologies.

### [57:59 - 58:02]

I apologies for totally going over time.

### [58:02 - 58:03]

Okay.

### [58:04 - 58:18]

And in the end I just want to thank my group

### [58:18 - 58:24]

Okay.

### [58:24 - 58:30]

Any questions.

### [58:30 - 58:32]

I have one question.

### [58:32 - 58:34]

Which is, we're talking.

### [58:34 - 58:36]

Do you see any new questions.

### [58:36 - 58:37]

I think so.

### [58:37 - 58:39]

No. Okay.

### [58:39 - 58:41]

Okay.

### [58:41 - 58:50]

So, like, as far as like reinforcement learning, like, do you think that it could be applied to like other like fields in Ai like that are like as traditional for machine learning?

### [58:50 - 58:58]

Like, for example, like something like computer vision like that somehow be integrated into, you know, feel like that.

### [58:58 - 59:00]

Yeah. So if we look back at one of the things that I showed earlier.

### [59:00 - 59:02]

Yeah. So if we look back at one of the things that I showed earlier.

### [59:02 - 59:04]

Yeah. So if we look back at one of the things that I showed earlier.

### [59:04 - 59:10]

So I one of the things I talked about right was that we could actually use reinforcement learning to train diffusion models.

### [59:10 - 59:19]

And so one of the things I was hinting at was that we can use reinforcement learning to fine tune to train language models better compared to what we do today.

### [59:19 - 59:24]

But one of the things that we can also do is use them for vision.

### [59:24 - 59:30]

Right. And so one of the examples that I had was you could use reinforcement learning to steer.

### [59:30 - 59:40]

So, for example, I have diffusion models.

### [59:40 - 59:43]

I.

### [59:43 - 59:47]

Did I.

### [59:47 - 59:49]

After this.

### [59:49 - 59:51]

Yeah, I think is after this.

### [59:51 - 59:58]

You can train so diffusion models, you can use them for computer vision right to generate images or to generate video.

### [59:58 - 01:00:00]

But we can train them with reinforcement learning to.

### [01:00:00 - 01:00:07]

Optimize for different objectives right to train them to output things that don't exist in the data set.

### [01:00:07 - 01:00:09]

And so here was just an example of that.

### [01:00:09 - 01:00:18]

Right. And so the last one, I think, is particularly funny because this is using a Vlm to basically say, I want a picture of a raccoon washing dishes.

### [01:00:18 - 01:00:23]

Start from a picture of a raccoon. Make it look more and more like that language description.

### [01:00:23 - 01:00:27]

Right. So that's one example of how you could use Rl for for vision.

### [01:00:27 - 01:00:29]

Yeah, thanks.

### [01:00:29 - 01:00:46]

Yeah, that's a good question.

### [01:00:46 - 01:00:52]

So the reinforcement learning example that we use for diffusion models was very specific to diffusion.

### [01:00:52 - 01:00:57]

Right, because we were saying so that corresponding to this slide.

### [01:00:57 - 01:00:58]

Right. Which is that?

### [01:00:58 - 01:01:02]

We can look at diffusion specifically as an Mdp.

### [01:01:02 - 01:01:06]

Because diffusion has this iterative process of of denoising.

### [01:01:06 - 01:01:12]

So if we were to use something like a generative adversarial network, it could look a little different.

### [01:01:12 - 01:01:15]

But I think

### [01:01:15 - 01:01:19]

anything that has a recursive form.

### [01:01:19 - 01:01:23]

Actually, in games you can kind of think of it as having a recursive form.

### [01:01:23 - 01:01:26]

So I I think, like with any of these generative models like we can pose them as reinforcement.

### [01:01:26 - 01:01:29]

Learning problems, right?

### [01:01:29 - 01:01:45]

Because another maybe like a another more general way of thinking about it is anything where your generative model is outputting sequential data, video or language.

### [01:01:45 - 01:01:48]

That sequence is an Mdp right?

### [01:01:48 - 01:01:54]

Because the context everything you've seen that it's generated before all of the video frames before all the language before.

### [01:01:54 - 01:02:02]

You can see that as your state what frame or what language token you generate next is your action.

### [01:02:02 - 01:02:08]

So from that perspective, then you can frame any of these generative modeling problems as reinforcement learning.
