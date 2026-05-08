# Recurrent World Models Facilitate Policy Evolution - David Ha - NeurIPS 2018 Oral

- URL: https://youtu.be/HzA8LRqhujk
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Refined at: `2026-05-08T10:32:26`

## Transcript

### [00:01 - 00:27]

So this work, at least to me, has been inspired by the literature in the cognitive neuroscience domain. Our mental models, made up of our unique experiences, determines how we interpret the world. They also affect our actions, how we assess opportunities, and also help us solve problems in our everyday lives. In a sense, how we look at the world is through the lens of our mental world models.

### [00:27 - 00:56]

So in this work, we explore building generative models of game environments. And we also try to train agents to look at their worlds through the lens of their own generative world models. So our generative models consist of pretty basic components. To develop a representation of space, we use a variational autoencoder to compress screenshots of a game into a low-dimensional latent space.

### [00:56 - 01:09]

To learn a representation of space, we use a variational autoencoder to compress screenshots of a game into a low-dimensional latent space. To develop a representation of time, we train a recurrent neural network to predict the distribution of future events. Just like how in this network, we train a recurrent neural network to predict future pen strokes of a pen,

### [01:09 - 01:34]

and we can sample from that distribution to generate different doodles. In our case, rather than modeling pen strokes, we model the distribution of future latent vectors, encoded by our VAE, so we can sample trajectories of the future. So in our setup, we have an environment that gives us a pixel image, at every time step. We feed this pixel image into a variational autoencoder, trained to reconstruct it,

### [01:34 - 01:55]

and the encoder will output a low-dimensional latent vector z, our representation of space. We then feed this latent vector z into a recurrent neural network called M, that's trained to predict the distribution of future latent vectors, condition or depending on the current information and previous information. And the model M has a hidden state h,

### [01:55 - 02:20]

and this hidden state of the RNN we're going to use as a representation of time. We'll feed these two low-dimensional representations of z and h, representing time and space, into a small linear controller c. Now our controller c can only see z and h, it cannot see the actual pixel observations. And its job is to output the action a, that will affect the environment,

### [02:20 - 02:43]

causing the environment to generate the actual states for the next time step. And to train our controller c, we want to solve for the parameters of this linear controller, such that we maximize the expected cumulative reward of our agent acting in the environment. So to test this simple framework, we tested on a car racing from pixel task from OpenAI Gym,

### [02:43 - 03:12]

where the agent has to navigate through these randomly generated tracks as fast as possible. So in the procedure, we first collect a data set, using data set rollouts, using a random policy. We then train the variational autoencoder v, to encode each frame of this data set into a low-dimensional latent space. So we can then process this data set into a latent space version of the data set.

### [03:12 - 03:33]

We then train the recurrent neural network m, using this data set to model the distribution of future latent vectors, conditioned on the current and previous information. Now the important thing to note is, in this experiment, v and m does not have access to the reward information. Its job is simply to compress space and to predict what's going to happen in the future.

### [03:33 - 04:01]

So these two networks can actually be trained efficiently using a GPU on a data set in an unsupervised fashion. So while these two models combined have millions of parameters, the controller, in contrast, is a very small model because of the low dimensionality of the inputs, and it has less than a thousand parameters, which makes this really easy to solve. And in our case, we can even use evolution strategies,

### [04:01 - 04:14]

in our case CMAES, to solve for the parameters of this linear controller, such that we maximize the expected cumulative reward of the agents. And here's the citation of the cake that's correctly done.

### [04:16 - 04:27]

So here's an example, on the left side, of the actual input frames we feed into our agent. And on the right side are reconstructions using the decoder of the VAE, using the latent space.

### [04:29 - 04:54]

At the beginning, we also trained an agent using only Z, not H. So we only give it the spatial information, but not the temporal information as an input. And it still learned to drive, but the policy, the navigational policy, is very non-robust and wobbles a lot, tends to miss the sharp corners. But when we then give it also H, so it knows both Z and H, the spatial and temporal information,

### [04:54 - 05:04]

it learns a more robust policy to navigate, and it's able to seemingly attack these sharp corners by predicting what's happening in the future intuitively.

### [05:06 - 05:28]

So our model achieved an average score above 900 for this task required to solve the task. And to our knowledge, this is the first solution that's able to solve car racing v0. But that's not the end of the story. This paper has been up for a few months, and people have taken our code, or the framework, and did interesting things with it. So someone used this framework, but rather than training M,

### [05:28 - 05:52]

they randomly set the weights of M, and they showed that by using these random temporal features, the score is still okay. So I found that quite interesting. Maybe it's not the weights, but the architecture that makes everything work. It doesn't mean that DQN is bad or anything. Another team improved DQN, made it a three-layer network where they put in dropout and some learning and all this stuff,

### [05:52 - 06:16]

and they also achieved a score at 900. But the difference here is that in our case, we use a generative model, and our model can predict future frames. So in theory, we can try to replace the environments with an environment generated by M, and we can try to train our controller not using the actual environment by training the controller entirely inside of an environment generated in latent space.

### [06:16 - 06:40]

So training inside of latent space environments. So to do that, we can train the output of the RNNM and feed that into a mixture density network layer, an MDN layer, so that it outputs the probability distribution function of the next time steps of the latent vector in the next time step. We can then sample an XZ, a realization of what's going to happen next, and feed that back in

### [06:40 - 07:08]

as if it's the actual latent observation. So we can train this controller inside this generated latent space environment not using the actual environment and not using any pixel information and we don't require the VAE. So we test this on a simple VisDoom level where in this level the unfortunate agent is stuck in a room full of monsters shooting fireballs at it and his job is simply to survive as long as possible.

### [07:08 - 07:34]

So the procedure is largely the same as the car racing task with a key difference of the RNNM model in addition to having to predict the probability distribution of the next latent vector, the distribution of whether the agent dies or not and we can sample from that. We need to model this terminal the termination events because in order to replace the actual gym environments to get the done events

### [07:34 - 08:02]

with the generated environment. We then train a controller inside of this generated latent space environment and then we can deploy these learned policies back to the actual environment to see how well we transfer. So now the model of the environment M is only a model of the actual environment. It's not perfect and it has flaws. So when we first did this experiment it didn't really work.

### [08:02 - 08:30]

What happened was the agent learned to take advantage of these flaws of the model and went to parts of the environment that was outside of his training distribution. He learned to cheat. So here we notice that the agent learned to move in a special way such that the fireballs when they get formed the agents can move in another way to extinguish them magically. So of course this policy is never going to transfer well

### [08:30 - 08:58]

to the actual environments. But what we notice is in the sampling process we can increase the temperature and by increasing the temperature we can make this generated environment more stochastic and more random. And we notice that a more random environment is more difficult for the agents inside this environment. Sometimes the agent may just die with no explanation. Tough luck. But in this more random environment

### [08:58 - 09:24]

the agent learns a policy that's more realistic and is able to transfer well back into the actual environment. So in the results we can see that by increasing the temperature from deterministic to a high temperature in the virtual score the second column is the score the agent achieves in the generated environment by increasing the temperature the environment becomes more difficult because the score decreases

### [09:24 - 09:50]

but the policies learned transfers better when we deploy them to the actual environment. Furthermore we notice that when the temperature is too high it also affects the quality of the policy being learned. For instance at a temperature of 1.3 the agent learns perhaps a more risk averse policy with a lower variance of returns at the expense of a lower mean. Lower mean reward. So the method outlined so far

### [09:50 - 10:22]

has many obvious limitations. It assumes that an initial random policy is enough to collect a data set that maps out most of the space of the environment which is not true in any environment that requires any meaningful exploration. So even in a simple swing up pendulum environment from pixels like this one where the initial policy the initial random policy mainly gathers data the pole is facing downwards

### [10:22 - 10:46]

we notice that the generative model has difficulty predicting what happens when the controller swings the pole upwards because it simply does not have that much data. Although in this case at the beginning the controller still learns a policy to try to swing up the pole it just doesn't know what to do afterwards. So what we can do is incorporate a simple iterative training loop where we deploy these policies

### [10:46 - 11:16]

back into the actual environment to collect more meaningful data and use the world model on this additional data to build a better model to then train the controller. So after 20 iterations this world model can learn a better generated environment that maps out the states when the pendulum is swung upwards and when we train a controller on this improved world model it learns more correctly how to balance a pole

### [11:16 - 11:48]

and swing it upwards. So if you're interested in this line of work maybe out this month that explores more in depth the concept of this iteratively training a generative model a high quality model of these environments and they show that by training an agent inside of these generated environments we can get really good sample efficiencies on domains like Atari or a continuous control task from pixels.

### [11:48 - 12:18]

So in the third work led by Jerry Hafner which I'm part of we actually try to explore more sophisticated forms of these stochastic dynamic models so unlike this current work where for simplicity we train the VAE and the RNN separately here we try to train the dynamics model end to end on the data collected and we model everything and also unlike this current work where we use a very simple

### [12:18 - 12:48]

linear controller for simplicity by replacing, incorporating a planning module into the controller and we show that for this control suite task where we learn continuous control tasks from pixels that we can achieve a pretty good sample efficiency by learning purely from pixels. So this work in addition to being a paper, it's also available as an interactive web article online at this URL so if you're interested

### [12:48 - 13:04]

you can download this work and also play around with these interactive web demos also there's code linked if you want to look at reproducing all of the experiments. So this concludes my talk. Thank you for your attention.

### [13:06 - 13:40]

So we've got about three minutes for questions so if you have a question come up to the microphones I see there's one right there go for it. My question is do you have any idea or opinion about training the model with the intrinsic reward what will be the challenge in that direction So that's a very good question the idea of intrinsic reward or curiosity is a natural extension of this and in fact

### [13:40 - 13:56]

Juergen Schmidhuber has published some work in 1990 where he looks at using the world model to get agents to look at states that he's not that aware of there also are some limitations of these approaches but feel free to come by our poster later.
