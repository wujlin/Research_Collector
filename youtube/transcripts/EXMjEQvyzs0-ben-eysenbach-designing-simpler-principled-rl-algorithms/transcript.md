# Ben Eysenbach Designing Simpler and More Principled RL Algorithms

- URL: https://www.youtube.com/watch?v=EXMjEQvyzs0
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-13T14:27:50`

## Transcript

### [00:00 - 00:17]

I think one of the reasons why I'm particularly excited about these problems is that these language models, they're trained to maximize the likelihood of the next token, and that draws a really strong connection to this way of treating reinforcement learning problems as predicting probabilities and as maximizing probabilities.

### [00:18 - 00:22]

And I think that these tools are actually much, much more similar than they might seem on the surface.

### [00:22 - 00:35]

Hey there, I'm your host, Kan Jun, and we are Generally Intelligent, an independent research lab developing AI agents that mirror the fundamentals of human-like intelligence and that can learn to safely solve problems in the real world.

### [00:36 - 00:44]

On our podcast, we interview researchers about their behind-the-scenes ideas, opinions, and intuitions that are hard to share in papers and talks.

### [00:45 - 00:49]

We hope you learn as much as we have in our quest to understand and build the mind.

### [00:50 - 00:52]

Ben Eysenbach is a PhD student from Princeton.

### [00:52 - 00:54]

He's a professor of CMU and a student researcher at Google Brain.

### [00:54 - 01:05]

He's co-advised by Sergey Levin and Ruslan Selikutinov, and his research focuses on developing RL algorithms that get state-of-the-art performance while being more simple, scalable, and robust.

### [01:05 - 01:10]

Recent problems he's tackled include long-horizon reasoning, exploration, and representation learning.

### [01:11 - 01:13]

Ben, it's really exciting to have you.

### [01:13 - 01:15]

We're really happy to have you on the podcast today.

### [01:15 - 01:22]

Where did you start out when you developed your initial research interests, and how did those interests evolve over time?

### [01:22 - 01:32]

I think that my introduction to machine learning probably came in the sophomore year of college.

### [01:32 - 01:35]

I was at MIT and taking a computer vision course.

### [01:35 - 01:40]

And this is back in 2015 or something, when nothing worked.

### [01:41 - 01:49]

And I remember even then being super impressed with what people had already done, even though we didn't have the giant models that give us all the really cool AI results that we have today.

### [01:50 - 01:52]

I remember at the end of that class, very nervously.

### [01:52 - 01:52]

I was like, I'm going to do this.

### [01:52 - 01:57]

And I remember the professor walking up to me and saying, hey, is there any way I can be an undergraduate researcher in your lab?

### [01:57 - 02:01]

And he said, sure, yeah, you should help out this grad student named Carl.

### [02:01 - 02:08]

So the next two and a half years was slowly learning about how this computer vision research works.

### [02:08 - 02:09]

What are the problems?

### [02:09 - 02:10]

How do you log into this cluster?

### [02:11 - 02:16]

How do you deal with the fact that data sets don't fit on EnderRAM and all sorts of things like that.

### [02:17 - 02:20]

It was super fun getting my hands dirty and learning how things worked.

### [02:20 - 02:22]

And the approximately.

### [02:22 - 02:25]

Zero research progress was about completing anything.

### [02:26 - 02:31]

And looking back at it, I realized, yeah, an undergrad, I probably could do everything I did in two and a half years in about a month.

### [02:33 - 02:41]

I'm really impressed that the grad students, Carl and the advisor, Antonio, like gave me the time to actually learn how to do research.

### [02:42 - 02:44]

And I think that really set me up to do research afterwards.

### [02:45 - 02:47]

Did you know you wanted to do a PhD?

### [02:48 - 02:50]

I guess by the senior year of college.

### [02:51 - 02:53]

I knew that I liked research.

### [02:54 - 03:03]

It was my impression that it would be much easier to start a PhD now, instead of going to industry or something else first, and then resuming the PhD later.

### [03:03 - 03:08]

PhDs are long, they're kind of like marathons and it's really hard to convince yourself to start later on.

### [03:09 - 03:14]

And so I ended up starting a PhD almost immediately after I finished undergrad.

### [03:15 - 03:18]

I ended up deferring it for a year to do research at Google.

### [03:19 - 03:20]

And that was a fantastic opportunity.

### [03:20 - 03:21]

That was super fun.

### [03:22 - 03:23]

And then I started a year afterwards.

### [03:23 - 03:24]

Got it.

### [03:24 - 03:36]

What were some of the things that you learned in undergrad or what were some of the like valuable lessons that you feel like that you learned in all that time that took those two and a half years that maybe it could, you know, help other people to not have to relearn them from experience?

### [03:36 - 03:37]

Yeah.

### [03:37 - 03:48]

I think one thing that reflecting back on it, I was learning was all of the tools that you aren't taught in CS classes, but are they really useful for research?

### [03:48 - 03:50]

Like, what does it mean to SSAE?

### [03:51 - 03:52]

Into a remote computer?

### [03:52 - 03:54]

How do you set up the keys for doing?

### [03:55 - 03:55]

What is GitHub?

### [03:55 - 03:56]

How do you use it?

### [03:57 - 04:03]

I think one thing that probably I've still been learning throughout my PhD has been, what does it mean to do with learning research?

### [04:04 - 04:10]

Like it's pretty clear, like you can take some data, you can run some method on it with some algorithm, but that's not really what research is.

### [04:10 - 04:11]

Research is about answering questions.

### [04:12 - 04:20]

And I feel like I only started to get a taste of that during undergrad and I think over the course of the last five years during the PhD have.

### [04:20 - 04:29]

I slowly learned what it actually means to ask interesting questions and to focus much more on what are the questions that we care about?

### [04:29 - 04:36]

And then the experiments are sort of ancillary to the questions they are used to support the questions and ask the questions.

### [04:36 - 04:42]

But at the end of the day, I don't really care whether you use, oh, I use this hyperparameter, this method and this data set.

### [04:42 - 04:45]

I care about, okay, does this support some interesting conclusion?

### [04:46 - 04:49]

I slowly started developing those skills during my undergrad.

### [04:49 - 04:50]

Very good.

### [04:50 - 04:50]

Yeah.

### [04:50 - 04:50]

Yeah.

### [04:50 - 04:54]

When you first started at Google or the beginning of your PhD, what were some of the questions you were interested in?

### [04:55 - 05:02]

So at the end of undergrad, I remember thinking the work I'd been doing so far was about understanding images and understanding videos.

### [05:03 - 05:05]

And I remember thinking about, well, why is this important?

### [05:05 - 05:07]

Why do we care about understanding them?

### [05:08 - 05:14]

And I thought that, well, maybe we care about these things because we actually are going to use them to make decisions in the world.

### [05:15 - 05:19]

We're going to say, look at a prediction for what the weather is going to be today and use that to decide whether to wear a coat or not.

### [05:19 - 05:29]

We're going to use a prediction about whether a patient has lung cancer or not, given some medical image, to decide, okay, what treatments do we do in the future?

### [05:29 - 05:33]

And my choice of studying reinforcement learning was largely based on that.

### [05:33 - 05:40]

So I was thinking about, well, how can we use machine learning, not just to make predictions about what's going to happen, but to actually control those outcomes.

### [05:41 - 05:47]

And so when you kind of first started doing your PhD, what were you interested in exploring related to reinforcement learning?

### [05:48 - 05:49]

There were a whole bunch of questions.

### [05:49 - 05:55]

One of the ones that I was thinking a lot about is, why weren't these methods being used in the real world?

### [05:55 - 05:58]

A lot of the people surrounding me worked on robotics applications.

### [05:58 - 06:00]

So I was trying to identify, well, what are the limitations?

### [06:00 - 06:04]

Why can't they just take an existing GitHub repo, run it on the robot and get amazing results?

### [06:05 - 06:16]

And one of the challenges that we identified was that there's a lot of human engineering that goes into actually getting these algorithms to work, especially when working on real physical systems like robots.

### [06:17 - 06:19]

So one thing that's really hard is safety.

### [06:19 - 06:22]

And dealing with the fact that robots pray.

### [06:23 - 06:31]

And so you've probably seen beautiful images from top robotics conferences of robots going down and stacking objects and manipulating objects.

### [06:32 - 06:38]

But what was not in those videos is all of the trial and error human engineering that went into getting those results.

### [06:39 - 06:46]

There's all the times where a robot didn't solve the task and knocked a block outside its workspace and a human had to go and cook it up for it.

### [06:47 - 06:49]

The fact that often we want to make the robots keep working.

### [06:49 - 06:52]

And so we use plastic parks, plastic works over time.

### [06:53 - 06:59]

And that actually makes the learning problem way, way, way harder than it seems like when we see our 30 second highlight reel.

### [06:59 - 07:02]

There are two fun examples here of sort of these challenges.

### [07:02 - 07:06]

One was some folks working on robotic manipulation.

### [07:07 - 07:10]

They found that they were never able to solve this task.

### [07:10 - 07:18]

They were using some images and it was a really, really hard task, or it seemed like it was, until one of them noticed that there was a blinking light on the robot.

### [07:19 - 07:19]

And they took a piece of paper.

### [07:20 - 07:22]

Masking tape and covered up the blinking light and then everything worked.

### [07:22 - 07:23]

It screwed up the algorithms.

### [07:24 - 07:24]

Wow.

### [07:25 - 07:34]

As another example, some folks were working on manipulation and they were trying to run the robots around the clock to collect as much data as they could.

### [07:35 - 07:40]

But they found that the success rates of the robots, their performance, it got worse during the day.

### [07:40 - 07:43]

It seemed like the robots were nocturnal for some weird reason.

### [07:44 - 07:49]

And then until they went and looked at some of the logs and looked at some of the videos and saw that.

### [07:49 - 07:56]

Oh, during the day, there's sun outside and the sun casts shadows and the shadows drift, and that makes it very, very hard.

### [07:57 - 07:58]

So it was easy.

### [07:58 - 08:04]

It was close all the blinds, but is that these sort of challenges that make it really, really hard to run these algorithms.

### [08:05 - 08:11]

So a lot of the work that I was working on the first part of the peak, do I was thinking about, well, how can we mitigate some of these challenges?

### [08:11 - 08:15]

So for things like resetting, how do we make it so that our robots fail less often?

### [08:15 - 08:18]

Can we somehow make them automatically detect when they might do something required?

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:18]

Yeah.

### [08:18 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:19]

Yeah.

### [08:19 - 08:24]

There's a human intervention so they can preemptively avoid those sorts of scenarios.

### [08:25 - 08:31]

And so that sounds like Leave No Trace, one of your papers at that time addressed that.

### [08:31 - 08:33]

What was kind of the main idea behind that?

### [08:33 - 08:33]

Yeah.

### [08:33 - 08:42]

So the main idea was trying to figure out, well, in many physical systems and robotics, there are states that if you get into those states, you can't get out of them.

### [08:42 - 08:49]

So a common example is if you have a robot pushing objects around on a table, if the robot arm knocks one of those objects off the table.

### [08:49 - 08:52]

The robot arm isn't long enough to go and pick that object back up.

### [08:52 - 08:54]

So how can you have the robot avoid doing that?

### [08:55 - 08:58]

And there are also examples outside of that as well.

### [08:58 - 09:06]

If you think about robots sort of walking around our everyday lives, if they break objects, they usually are not capable enough to glue them or duct tape them back together.

### [09:07 - 09:11]

Even your Roomba going around your house, there's a little depth sensor on the front of it.

### [09:11 - 09:17]

So it avoids going off stairs because the robot can't go back upstairs, even though Roombas can go downstairs.

### [09:18 - 09:18]

Interesting.

### [09:19 - 09:19]

I see.

### [09:19 - 09:24]

So it kind of avoids potential parts of the state space where it's not comfortable.

### [09:24 - 09:25]

Exactly.

### [09:25 - 09:25]

Yeah.

### [09:25 - 09:27]

There are many different notions of safety.

### [09:27 - 09:33]

And we were looking at one particular notion of safety, which was, well, how can we avoid getting in these irreversible states?

### [09:33 - 09:38]

This is a different notion of safety than people sometimes talk about in the AI safety community.

### [09:38 - 09:45]

They talk about misspecified rewards, or they talk about bias and fairness that are really, really important problems, but it's not the problem that we were tackling here.

### [09:46 - 09:46]

That makes sense.

### [09:47 - 09:49]

And so then after that, what did you think about?

### [09:50 - 09:59]

After we made some progress on that problem, we were thinking about what are the other major bottlenecks to actually applying these reinforcement learning algorithms on system robots?

### [10:00 - 10:04]

And one of the key challenges was figuring out how do we specify these rewards?

### [10:05 - 10:12]

So on that first project, that Leave No Trace project, we had to specify some notion of, okay, have you gotten back to some good state?

### [10:13 - 10:19]

We were able to use some learning algorithms to identify when you were in non-reversible states, where you would get stuck.

### [10:20 - 10:24]

But there's still a lot of engineering going into saying, okay, this is an okay state to be at.

### [10:24 - 10:26]

And so we were looking at how can we automate that?

### [10:27 - 10:32]

One way that we've looked at automating that has been to look at the setting of goal conditions reinforcement.

### [10:33 - 10:43]

It's a problem of having reinforcement learning agents that can figure out, okay, given your current state and given some desired goal state, what are the actions that you can take to get from here to there?

### [10:43 - 10:45]

How long do we think it's going to take to get from here to there?

### [10:46 - 10:47]

It's a really, really broad problem.

### [10:47 - 10:49]

But it allows us to automate some of that.

### [10:50 - 10:58]

And so we were able to do some of these decisions about having humans come in and manually specify how far or how long would it take to get from one state to the other state.

### [10:59 - 11:01]

And that was the diversity is all you need paper.

### [11:02 - 11:06]

The diversity is all you need paper, that's a slightly different paper, but also targeted at a very similar problem.

### [11:07 - 11:09]

The diversity is all you need paper, that was really, really fun.

### [11:09 - 11:11]

It ended up emerging over the course of about a month.

### [11:12 - 11:17]

We were playing around with this idea that, well, if specifying the rewards is hard.

### [11:17 - 11:19]

There's a lot of ways to do this.

### [11:19 - 11:23]

And that's when I started to learn entirely tabula rasa.

### [11:23 - 11:30]

Just say, okay, can we discover all of the possible modes of behavior for some reinforcement learning?

### [11:30 - 11:31]

Yes.

### [11:31 - 11:38]

You were largely looking at simulated robots there, so the sort of mental model I had was a lot of the reinforcement learning algorithms.

### [11:38 - 11:40]

They tried to learn these really, really big neural networks.

### [11:40 - 11:45]

And so these things have hundreds of thousand millions, hundreds of millions of parameters.

### [11:45 - 11:48]

need to figure out how do you tune each of those parameters?

### [11:49 - 11:53]

And one of the big reasons it takes so long, so many samples to learn these

### [11:53 - 11:56]

reinforcement learning policies is because they have so many different

### [11:56 - 11:57]

parameters that we have to change.

### [11:57 - 11:58]

You have to twiddle.

### [11:59 - 12:02]

And so we were interested in saying, well, even though they have this many

### [12:02 - 12:08]

parameters, maybe there's a lower dimensional space that gives us

### [12:08 - 12:10]

all of the reasonable behaviors.

### [12:10 - 12:14]

So one way I think about this is as saying, well, maybe, is there a way

### [12:14 - 12:19]

that we can get just a small number of knobs, such that by twiddling a couple

### [12:19 - 12:23]

of these knobs, we can get almost all the behavior that we would want to get from

### [12:23 - 12:25]

some reinforcement learning agents.

### [12:25 - 12:28]

For example, we were looking at some locomotion tasks.

### [12:28 - 12:31]

Ideally, what we would like to have is we would like to have one knob that

### [12:31 - 12:35]

controls, are you going forward or are you going backwards and maybe another one

### [12:35 - 12:39]

that controls the style of your, are you jumping up and down or are you crouching

### [12:39 - 12:44]

on the ground and maybe another one that controls your rotation, are you jumping

### [12:44 - 12:44]

into.

### [12:44 - 12:46]

Flips or are you just going forward smoothly?

### [12:47 - 12:48]

So that's sort of what we really wanted to learn.

### [12:49 - 12:55]

And there were some ideas and some of the prior about using this idea of

### [12:55 - 12:59]

information theory, which is the same idea that's used to compactly transmit

### [12:59 - 13:03]

messages over the internet and over phone lines, whether some way that we could use

### [13:03 - 13:08]

that idea to automatically find these small number of knobs that we could use

### [13:08 - 13:14]

to control these robots and neither was, so we're able to repurpose some of the

### [13:14 - 13:14]

tools.

### [13:14 - 13:18]

And refine them a little bit and keep pretty cool results on these locomotion tasks.

### [13:18 - 13:24]

So we were able to, for example, get certain legged robots to do backflips and get other

### [13:24 - 13:26]

legged robots to run in different directions.

### [13:26 - 13:29]

And that's roughly where we ended the practice.

### [13:30 - 13:31]

Now, then worked on that.

### [13:31 - 13:34]

There's been a lot of really cool subsequent work by other folks that have looked at

### [13:34 - 13:36]

extending the capabilities of these.

### [13:37 - 13:39]

I think it was a little bit like that initial work.

### [13:39 - 13:44]

It sort of provided a palette of paint and then once given this palette, there's so many things you can do.

### [13:44 - 13:46]

With that palette, so many different pictures you can paint.

### [13:46 - 13:52]

So other works looked at saying, well, can you somehow repurpose these, these behaviors that you've learned, these skills to

### [13:52 - 13:53]

quickly solve new tasks?

### [13:54 - 13:57]

Or can you somehow combine them with some model of the world to solve other tasks?

### [13:58 - 14:03]

Implementation learning can use them to figure out how to coordinate behavior across multiple robots.

### [14:03 - 14:10]

This work that I haven't worked with other folks I've worked on has been really cool to see what people have been able to do with this

### [14:10 - 14:12]

palette of paints that we've sort of automatically learned.

### [14:13 - 14:14]

It's really interesting.

### [14:14 - 14:19]

So this is kind of the idea that you can learn these skills with no reward function, no specified reward function.

### [14:19 - 14:24]

Can you go into the intuition behind like the objective that you're maximizing and how exactly these skills get learned?

### [14:25 - 14:25]

Yeah.

### [14:25 - 14:31]

So I mentioned before that we were trying to learn the small number of knobs that control the sort of behavior that we see.

### [14:32 - 14:38]

And so precisely what we want to do is we want to have each of these knobs have a very large influence over the behavior that we end up seeing.

### [14:39 - 14:41]

So the behavior that we see, those are going to be the observations.

### [14:42 - 14:44]

What states is the agent going to?

### [14:44 - 14:56]

And so to make these knobs very strong influence over the behavior that we see, we use a certain lower bound on this quantity called mutual information.

### [14:56 - 15:00]

And the resulting form of it actually is a pretty simple intuition.

### [15:01 - 15:09]

And the intuition is that it's a bit like a two player game, a game that we actually could play if you and I were standing in the same room.

### [15:09 - 15:11]

And so here's how the game works.

### [15:11 - 15:13]

Let's say we have two players, Alice and Bob.

### [15:14 - 15:19]

So what Alice does is they decide how to set these knobs and then the robot does something.

### [15:20 - 15:25]

And then Bob, Bob looks at the robot and tries to guess, well, how did Alice set those knobs?

### [15:25 - 15:29]

Did Alice set them to very small values, to very large values?

### [15:29 - 15:31]

Maybe one of the knobs was very large and one was very small.

### [15:31 - 15:32]

They try to guess this.

### [15:33 - 15:34]

And then it's a cooperative game.

### [15:34 - 15:37]

So then Alice and Bob confer and they say, okay, Bob, you're a little bit wrong there.

### [15:37 - 15:39]

You should have guessed a lower value for this.

### [15:39 - 15:44]

And Bob says, well, Alice, if you had the robot do this instead, it would have been easier for me to guess what you were trying to do.

### [15:44 - 15:57]

So over time, they can converge to this sort of cooperative strategy where Alice has the robot do things that are really easy to discern, where it's very easy to send messages using the different behavior of the robot.

### [15:58 - 16:08]

And so you can imagine that if Alice wants to send different letters of the alphabet, maybe you could have the robot jump for the letter A and rolling the ground for letter B.

### [16:09 - 16:14]

And then if Bob knows what these letters mean, he can quickly see this behavior.

### [16:14 - 16:19]

And guess what message Alice is trying to send is exactly this notion of sending messages.

### [16:19 - 16:22]

That was sort of the intuition that we started.

### [16:22 - 16:27]

That was the intuition of using mutual information, this information theory idea to try to learn these skills.

### [16:28 - 16:29]

That's really interesting.

### [16:29 - 16:38]

And so in your objective, you end up, I guess, maximizing the mutual information between the skills and the states that are being guessed, which is kind of like Alice and the Bob.

### [16:38 - 16:39]

Exactly.

### [16:39 - 16:40]

Got it.

### [16:41 - 16:42]

It's a little bit interesting to think about.

### [16:42 - 16:44]

Like, that's a little unnatural.

### [16:44 - 16:44]

Yeah.

### [16:44 - 16:46]

As a way of learning skills, I guess, right?

### [16:46 - 16:52]

Like, if you think about a person, I'm not trying to make the most extreme gestures to like, oh, look at this one, right?

### [16:52 - 16:53]

Like, I am like trying to do something.

### [16:53 - 16:55]

So it's sort of interesting that skills come out of this at all.

### [16:56 - 16:57]

Yeah.

### [16:57 - 17:02]

I think there's a sort of interesting connection here to how humans actually learn language.

### [17:03 - 17:05]

So I'm by no means an expert in this.

### [17:05 - 17:14]

My understanding is that one working hypothesis on how humans learn language is that it's largely cultural, that each generation can teach their kids a language.

### [17:14 - 17:14]

And so on.

### [17:14 - 17:18]

And you can look at what happens over many generations of doing this.

### [17:19 - 17:21]

And linguists have looked at this.

### [17:21 - 17:28]

And one of the patterns that they've seen emerge is that the languages that are learned through what's called iterated learning.

### [17:28 - 17:34]

So generation over generation, they often tend to become more structured over time.

### [17:34 - 17:43]

So whereas the word red ball and green football and pink table, those all might just be complete garbage initially.

### [17:43 - 17:44]

But this process.

### [17:44 - 17:49]

Of iterated learning, you end up learning a structured language where you have colors and shapes and objects.

### [17:50 - 17:55]

And so I very much agree, Josh, that this seems pretty different from how humans are learning.

### [17:55 - 18:08]

But you could imagine that if we're having these reinforcement learning agents, not just learn in one-off scenarios, but actually learn iteratively in the same way that we can sort of distill very large machine learning models down to smaller models, machine learning models.

### [18:08 - 18:13]

If we could repeat that process and have one generation of reinforcement learning agents teaching the next generation.

### [18:14 - 18:17]

Year over year, we might see a nice compositional sort of language emerge.

### [18:17 - 18:20]

There's pure speculation, but I think it'd be really cool to explore.

### [18:21 - 18:21]

Yeah.

### [18:22 - 18:27]

I think the thing that I'm pointing at maybe is that it doesn't seem like there's any bias towards actions that are usable.

### [18:28 - 18:35]

Like for example, in the humanoid task, you could communicate A through Z by simply making particular angles of the right elbow joint.

### [18:35 - 18:36]

Okay.

### [18:36 - 18:37]

I mean, that's very discriminable.

### [18:38 - 18:38]

You did it.

### [18:39 - 18:42]

But the first of the thing, those skills would be totally pointless for learning to walk.

### [18:42 - 18:42]

Right.

### [18:42 - 18:43]

And so I think that's.

### [18:44 - 18:45]

You know, like, I guess that's a good question.

### [18:46 - 18:55]

Is there any other force that kind of forces these representations or skills to be more useful or have people done other work or is there any other part to the reward or is it just that?

### [18:55 - 18:59]

Yeah, I guess I was surprised that you ended up with useful or interesting skills at all.

### [18:59 - 18:59]

Yeah.

### [19:00 - 19:01]

Yeah, that's a really good point.

### [19:01 - 19:08]

And admittedly, on a scale to more challenging tasks, we did see that sort of behavior and there were very small things we did to avoid parts of it.

### [19:09 - 19:13]

For example, we said, well, we're going to force Bob to look at just the states that they're.

### [19:13 - 19:13]

Okay.

### [19:13 - 19:22]

We're going to force Bob visits, not the actions it was trying to do, because if Robo was trying to do something and Bob didn't see that, then it seems like maybe not a great way of communicating.

### [19:22 - 19:26]

The space of behaviors is really, really, really, really large.

### [19:26 - 19:39]

And if we're only trying to send a small number of letters through this enormous space, then it's very easy to just say, well, use the position of the arm to encode ABCDEFG and they're in need.

### [19:39 - 19:43]

So we didn't tackle this problem, but there has been some subsequent work looking at, well, what are different ways.

### [19:43 - 19:49]

Of forcing these behaviors to be more aligned with what we as humans might think should be useful.

### [19:51 - 19:56]

One way of doing this is to say, well, maybe we're going to make it so that Bob doesn't have great vision.

### [19:57 - 20:01]

So he only can see behaviors if they appear really distinct from each other.

### [20:01 - 20:02]

That's really interesting.

### [20:03 - 20:12]

Other work says, well, let's say that Alice's job is not just to try to transmit the letters to Bob, but has also tried to get the robot to do something interesting.

### [20:12 - 20:13]

Mm-hmm.

### [20:13 - 20:13]

Yeah.

### [20:13 - 20:13]

Mm-hmm.

### [20:13 - 20:19]

Maximize some combination of this communication objective plus some other objective.

### [20:20 - 20:21]

Interesting.

### [20:21 - 20:30]

If there's a state that there are like multiple different skills that could theoretically get you to that state, is the agent only learning one of them?

### [20:31 - 20:32]

Yeah, that's a really good question.

### [20:33 - 20:34]

Yes and no.

### [20:34 - 20:36]

It depends a little bit on how the environment is configured.

### [20:37 - 20:43]

So if it's possible to get to some state in different routes, take different states, then.

### [20:43 - 20:47]

You could still transmit the message based on the route you took to get there.

### [20:47 - 20:53]

Because Bob might say, well, I can't guess what letter you're trying to send based on the final state where the robot ended up.

### [20:54 - 20:58]

But before that, I saw it took one of two possible routes and it took the left route here.

### [20:58 - 21:01]

So I'm going to guess that you were trying to send the message left.

### [21:01 - 21:02]

I see.

### [21:02 - 21:05]

So it uses the whole trajectory, not just the final state.

### [21:05 - 21:09]

There's been a bit of work exploring exactly what Bob should look at.

### [21:10 - 21:12]

Should Bob look at the entire video?

### [21:12 - 21:13]

Should he just look at.

### [21:13 - 21:17]

A random set of the images?

### [21:17 - 21:19]

Should he look at actions?

### [21:19 - 21:25]

Could you look at just some subset of the states and in different settings, different versions might work better.

### [21:26 - 21:31]

This idea of learning this iterative learning process is really interesting that like iteration results in more structure.

### [21:31 - 21:37]

It also seems like in humans, even the actions that we're taking are kind of learn from other agents.

### [21:38 - 21:43]

And so there is kind of this iterative learning process that resulted maybe like more.

### [21:43 - 21:43]

Yeah.

### [21:43 - 21:45]

Interpretable or useful actions.

### [21:45 - 21:48]

So that's interesting that you see that kind of behavior.

### [21:48 - 21:51]

Is there any work that's been built on this that has really surprised you?

### [21:52 - 22:00]

One thing that surprised me a fair bit was some work, not in the reinforcement learning community, but in the Bayesian modeling community.

### [22:01 - 22:07]

And they said, well, if we have some data, you might want to maybe some set of images with their labels.

### [22:07 - 22:08]

You only have this small amount of data.

### [22:09 - 22:12]

There are many different models you could fit to this data that are consistent with that data.

### [22:13 - 22:14]

And there's been some recent work.

### [22:14 - 22:18]

It was something like diversity is all you need for ensembling or something like that.

### [22:19 - 22:31]

And what they showed is that you can use this same idea of looking at the mutual information to learn many different machine learning models that are consistent with the data, but still make different predictions from one another.

### [22:32 - 22:36]

So that's sort of in the outside, the reinforcement learning realm inside of reinforcement learning.

### [22:37 - 22:38]

There's a neat paper.

### [22:38 - 22:42]

I'm forgetting the authors now that looked at by manual manipulation.

### [22:42 - 22:48]

So these are really, really challenging tasks where you have two robotic arms and they're supposed to cooperate to solve some task.

### [22:49 - 22:54]

And ordinarily solving these sorts of problems are really, really challenging because they need to coordinate with one another.

### [22:54 - 22:59]

The space behaviors for two arms is so much larger than the space of behaviors for one arm.

### [23:00 - 23:12]

But they showed that by using these same techniques of learning the skills, you're able to learn really interesting behavior where you have say two robotic arms go down and cooperatively pick up a very heavy object.

### [23:13 - 23:13]

Interesting.

### [23:14 - 23:25]

And it's the idea that when you're outputting actions for each arm, that there's some kind of awareness of what the other arm is doing, or you're kind of using this mutual information between the arms.

### [23:25 - 23:27]

How exactly does that work?

### [23:28 - 23:34]

They were not looking at the mutual information between the arms, but using the same idea of mutual information to learn the skills for both the arms.

### [23:35 - 23:35]

Got it.

### [23:35 - 23:42]

Well, instead of having to control all of the joints for all of the arms, they said, well, maybe we'll learn 20 different skills for each of the arms.

### [23:42 - 23:50]

And so now, instead of having this huge piece of joints, we just have like a small number of skills that you can select between for arm one and for arm two.

### [23:51 - 23:59]

And then they use these, they figured out how to sequence these skills to solve these more challenging tasks in a sort of hierarchical approach.

### [23:59 - 24:07]

Is there any kind of formalism around determining how good these skills are as like a basis set of things that you would want to do?

### [24:07 - 24:09]

Yeah, that's a really, really good question.

### [24:09 - 24:12]

So we started working on the skill learning.

### [24:12 - 24:16]

Stuff and I guess it would have been December of 2017.

### [24:16 - 24:22]

And a couple months after that, we started looking at this question, okay, can we prove that these skills are good?

### [24:22 - 24:23]

Will these skills learn everything?

### [24:24 - 24:30]

And four years later, four years of trying to get to an answer, four years of trying and failing to get to an answer.

### [24:30 - 24:35]

We eventually actually got to an answer, which is in one sense, they're very good.

### [24:36 - 24:38]

And in another sense, they are very bad.

### [24:38 - 24:40]

And so I can explain a little bit what I mean there.

### [24:41 - 24:41]

This is some work that.

### [24:42 - 24:48]

After way too many drafts and way too many sort of we published at ICLR last spring.

### [24:49 - 24:53]

The paper is something like the information geometry of unsupervised reinforcement learning.

### [24:54 - 24:56]

And there's sort of two key results there.

### [24:57 - 25:06]

The first result is that if you try to learn these skills using the speak fill information objective, you do not learn how to solve every task.

### [25:06 - 25:08]

At least you don't learn how to solve every task optimally.

### [25:09 - 25:12]

And so maybe you have some skills that go to one state.

### [25:12 - 25:16]

And some skills go to some other state, but it turns out that they're going to be some states.

### [25:16 - 25:20]

They're going to be some reward functions that none of the skills are going to do very well at.

### [25:21 - 25:36]

And this is actually very surprising because before this, this sort of common intuition, my intuition would have been that, well, if you just learn more and more skills, or if you try to learn more and more skills, then you'll end up learning more and more behaviors.

### [25:36 - 25:38]

And eventually you'll learn how to just do everything.

### [25:39 - 25:40]

But it turns out that's actually not the case.

### [25:41 - 25:41]

Why?

### [25:41 - 25:54]

There are two notions of distance and the sort of common intuition, my intuition for how distances should work is different from how this information theory measures distances.

### [25:55 - 26:02]

And so sort of intuitively, I would think like, okay, distances, you means like one skill should visit states that are far away from other states.

### [26:02 - 26:11]

Like it would take many steps to go from one to another, or they're far away from each other as measured by a yardstick, but these mutual information techniques, they measure

### [26:11 - 26:12]

your distances differently.

### [26:13 - 26:17]

They measure your distances between probability distributions.

### [26:18 - 26:21]

And it turns out that in certain circumstances, these can be very, very different.

### [26:22 - 26:23]

Yeah, that's true.

### [26:23 - 26:24]

That's really interesting.

### [26:25 - 26:25]

Yeah.

### [26:25 - 26:29]

Like the distribution might not look that different, even though we feel like the distances are very different.

### [26:29 - 26:41]

Are there any terms that you could add to the mutual information objective that might be able to capture this other idea of distance and maybe increase exploration and, or like skill learning in these other areas?

### [26:42 - 26:42]

I don't know.

### [26:43 - 26:45]

That was one of the open questions we left at the end of that paper.

### [26:45 - 26:47]

And to the best of my knowledge, it is still an open question.

### [26:48 - 26:55]

I think it's a really, really interesting question because if you could do that, then you really could learn how to solve every possible downstream task.

### [26:55 - 27:09]

It feels like, maybe I'm misunderstanding this, but it feels like maybe a sort of no free lunch thing here in that if you pick any skills, like I can always pick a thing that wasn't the skill that you learned, that's actually the thing that you really needed to do.

### [27:09 - 27:11]

And therefore the skills you learned are actually taking further.

### [27:11 - 27:17]

Away from this bizarre thing that I decided to make you learn, does that sort of apply or is it somewhat different?

### [27:18 - 27:18]

Yeah.

### [27:18 - 27:21]

So I think there's like two notions or two things that you might be getting at.

### [27:22 - 27:25]

So one is that, well, how many behaviors are there?

### [27:26 - 27:31]

If I give you some reward function, do you have to learn infinite number of skills?

### [27:31 - 27:33]

Because if so, then we're lost.

### [27:33 - 27:39]

There's definitely nothing you can do because you always could invent some rewards for what we would have no skill to solve.

### [27:40 - 27:41]

It turns out that if.

### [27:41 - 27:48]

Your number of states is finite, then the number of reward maximizing policies is also finite.

### [27:49 - 27:55]

This again, might seem a little bit surprising because the number of reward functions can be infinite.

### [27:56 - 28:09]

But it turns out that there's a relatively simple counting argument you can use to show that, well, if you have a finite number of states, you will only need a finite number of skills to solve any possible task.

### [28:10 - 28:10]

But it.

### [28:11 - 28:13]

Turns out this is actually very, very, very, very large.

### [28:13 - 28:26]

But I guess that may be a second thing that you were also alluding to, which is, well, even if you could learn every possible skill, every possible skill that could maximize every possible reward function, we'd actually want to do that.

### [28:27 - 28:35]

Because at the end of the day, we don't really care about whether there exists one of your skills that can solve the task we care about.

### [28:35 - 28:36]

Well, does there exist one?

### [28:36 - 28:37]

And can you actually find it?

### [28:37 - 28:38]

Yeah.

### [28:39 - 28:40]

Because it's a question of how quickly can you find it?

### [28:41 - 28:43]

The right skill is also a really hard question.

### [28:43 - 28:47]

It's a question very related to adapting and meta-learning.

### [28:47 - 28:49]

And there we actually have a very positive result.

### [28:49 - 29:10]

So if we formulate the, this problem of skill learning as trying to not find every way of maximizing every reward function, but trying to maximize the reward function as quickly as possible, then we can show that these skill learning methods, they give you a very good initialization for solving any downstream.

### [29:10 - 29:30]

There's a great theoretical result, and there are some assumptions here that don't apply in practical settings, but I think it does give me some hope that maybe these methods are actually a good way of learning to solve new tasks if you care about not just the expressivity of those skills, but also how quickly you can learn, the speed of learning.

### [29:31 - 29:36]

This is really interesting, this idea of skill learning methods as initialization method.

### [29:36 - 29:39]

That's a really interesting kind of explanation of what it's doing.

### [29:39 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:40]

Yeah.

### [29:40 - 29:42]

That's a quick follow-up question on that.

### [29:42 - 29:45]

So that finding that it's a good initialization, I assume you did some experiments.

### [29:45 - 29:56]

I'm curious, was there any impact from how different the tasks it was given were to the pre-training environment that it had?

### [29:56 - 30:04]

If the pre-training led to skills like walking and climbing, but then the task was very different from that, how much of an effect did that have?

### [30:05 - 30:05]

Yeah.

### [30:05 - 30:06]

It's a really good question.

### [30:06 - 30:10]

This is purely a theoretical paper, and so we weren't running large-scale experiments.

### [30:10 - 30:12]

to study questions anywhere near that complex.

### [30:13 - 30:18]

What we were looking at was, well, does it matter how you learn the skills?

### [30:18 - 30:22]

Like if you do learn skills that are biased towards one thing, does that

### [30:22 - 30:25]

affect how long it will take to learn other skills that might be a little bit

### [30:25 - 30:31]

different and our results there were a worst case result, meaning that we weren't

### [30:31 - 30:35]

measuring how long it would take to learn any skill, we were looking at how long

### [30:35 - 30:39]

would it take to learn the hardest possible task, so they're a bit pessimistic

### [30:39 - 30:44]

in that regard, because on average, it might be easier to solve all the other

### [30:44 - 30:47]

tasks, you might be able to learn most tasks very quickly, but only one or

### [30:47 - 30:52]

two tasks very slowly, but we show that if you learn the skills, so the skills

### [30:52 - 30:56]

are all very far apart from each other, then sort of intuitively, if you're

### [30:56 - 31:00]

trying to learn some new tasks, then the new task, it should be close to at least

### [31:00 - 31:01]

one of those skills that you found before.

### [31:02 - 31:07]

There's a analogy that's actually a precise analogy to what's sometimes

### [31:07 - 31:09]

referred to in theoretical CS.

### [31:09 - 31:14]

It's the facility assignment problem, and it's this question of saying, where

### [31:14 - 31:16]

should you put, say, hospitals in a city?

### [31:16 - 31:21]

If you know that you want people to be located close to the hospitals so that

### [31:21 - 31:24]

they can get to the hospital in an emergency, there are many different ways

### [31:24 - 31:28]

you could define this problem, but if you say you want to minimize the longest

### [31:28 - 31:32]

that anyone would have to ride an ambulance to get to a hospital, it turns

### [31:32 - 31:36]

out that's exactly the problem we're solving with these skills, but instead

### [31:36 - 31:39]

of riding an ambulance, we're running our...

### [31:39 - 31:42]

learning algorithm, and we're going to minimize the number of steps it would

### [31:42 - 31:44]

take to get to the solution.

### [31:45 - 31:49]

Kind of want an initial skill space where the skills are relatively

### [31:49 - 31:51]

spread out in a reasonable way.

### [31:52 - 31:52]

Exactly.

### [31:52 - 31:52]

Yeah.

### [31:52 - 31:56]

I guess how you'd want to assign, put hospitals in a city.

### [31:57 - 32:00]

What is this notion of distance sort of spread out, I guess, for these skills?

### [32:00 - 32:03]

Like given that the skill is sort of a, yeah, yeah.

### [32:03 - 32:07]

Well, what is a good intuition for like what these skills are, like in a concrete

### [32:07 - 32:09]

problem, like, you know, ant or something?

### [32:10 - 32:16]

Intuitively, they correspond to trying to get to states or combinations of states.

### [32:17 - 32:20]

And so precisely the way I think about this, at least when thinking about these

### [32:20 - 32:26]

sort of theoretical questions is, as thinking about the probability distribution

### [32:26 - 32:28]

that each skill would want to achieve.

### [32:29 - 32:34]

And so maybe you have one skill that wants to spend all of its time running very

### [32:34 - 32:37]

quickly and being in the running quickly state, and maybe you have another skill

### [32:37 - 32:39]

that wants to spend half its time.

### [32:39 - 32:42]

In the air and half its time on the ground, maybe that corresponds to jumping.

### [32:43 - 32:47]

That's sort of interesting because you can't spend all of your time in the air

### [32:47 - 32:50]

because the physics says, well, at some point, everything that goes up must come

### [32:50 - 32:50]

down.

### [32:51 - 32:55]

And so I'm thinking about what is the distance between these probability

### [32:55 - 32:56]

distributions?

### [32:58 - 33:02]

The distance between these probabilities at distributions over states, but the

### [33:02 - 33:04]

state is like this implicit space.

### [33:04 - 33:07]

So it's not necessarily the running or jumping, unless you made your state contain

### [33:07 - 33:08]

that information.

### [33:08 - 33:09]

But it's, it's like more.

### [33:09 - 33:09]

Yeah.

### [33:09 - 33:16]

It's sort of interesting to think about, well, when we're for the theoretical

### [33:16 - 33:19]

results, we're looking at these sort of tabular settings where you have not that

### [33:19 - 33:24]

many states, but when we are doing, using these large neural networks, what is the

### [33:24 - 33:28]

implicit state and a reason about, well, do we get guarantees about, will we learn

### [33:28 - 33:30]

really good implicit states or really bad ones?

### [33:32 - 33:34]

You mentioned at the very beginning of this, that there were two results.

### [33:35 - 33:37]

Did you cover this or what was the second result?

### [33:37 - 33:39]

I guess, cause I think we interrupted with too many questions before.

### [33:39 - 33:41]

But it might've come through in the questions.

### [33:41 - 33:46]

The first one was that you don't learn every way of maximizing every reward

### [33:46 - 33:46]

function.

### [33:46 - 33:51]

But the second one was that you do learn this good initialization, this initialization

### [33:51 - 33:54]

that's really good for solving the most challenging task.

### [33:56 - 34:00]

Have you had a chance to do any follow-up empirical work on this or testing

### [34:00 - 34:03]

out like how this applies to practical studies?

### [34:03 - 34:04]

We haven't looked at that yet.

### [34:05 - 34:08]

What made this project take four years?

### [34:08 - 34:09]

What was particularly.

### [34:09 - 34:10]

Challenging about it?

### [34:11 - 34:12]

There are a couple of things that were tricky.

### [34:12 - 34:17]

One of them was figuring out what is the notion of optimality that we care about?

### [34:17 - 34:19]

What does it mean for skills to be useful?

### [34:19 - 34:20]

There are many different ways you could use skills.

### [34:21 - 34:24]

And so we spent a lot of time thinking about different ways of using the skills.

### [34:25 - 34:29]

For example, you could consider, well, what if you start with the best skill

### [34:29 - 34:30]

and then you adapt that one?

### [34:31 - 34:32]

It turns out that was a dead end.

### [34:33 - 34:37]

I thought about, well, what if we start by thinking at a sort of tabular setting?

### [34:37 - 34:39]

Can we reason about, will there be.

### [34:39 - 34:42]

A skill for reaching every state and how far apart will those states be?

### [34:43 - 34:44]

Turned out that was also a dead end.

### [34:45 - 34:51]

The sort of key result here actually relies on a really, really, really old results.

### [34:52 - 34:56]

This idea of measuring distances between the probabilities and looking at the

### [34:56 - 34:58]

distance to some worst case task.

### [34:59 - 35:04]

It had been looked at in this information theory literature in, I think the late seventies.

### [35:05 - 35:09]

So it's this result that no one I had talked to had ever heard of before because it was so old.

### [35:09 - 35:14]

But indeed there was this relatively old information theory textbook.

### [35:15 - 35:19]

And one of the final chapters of that, there is a small image of what this looks like.

### [35:20 - 35:23]

And so that was ultimately the sort of clue that was a lot.

### [35:23 - 35:25]

You enabled us to make progress on this.

### [35:26 - 35:30]

You mentioned that skills kind of intuitively correspond to getting to

### [35:30 - 35:32]

the states or getting to combinations of states.

### [35:33 - 35:38]

Is there any mapping then between skill learning and goal conditioned RL where you

### [35:38 - 35:39]

can go ahead?

### [35:39 - 35:41]

Yeah, there's a really, really nice connection between them.

### [35:41 - 35:46]

In fact, you can show that these sort of goal reaching tasks are a special

### [35:46 - 35:49]

piece of these mutual information tasks.

### [35:49 - 35:51]

Oh, interesting.

### [35:51 - 35:54]

So before we were talking about these skill learning methods as

### [35:54 - 35:55]

this game between Alice and Bob.

### [35:56 - 36:01]

And Alice had say letters to try to send to Bob and would ask the robot, okay,

### [36:01 - 36:05]

do something that will let Bob guess that I'm want the letter a or do something

### [36:05 - 36:09]

that tells Bob, I want to guess the letter B, but here's one.

### [36:09 - 36:13]

You can play that you can play that game, but with Alice saying, well, instead of

### [36:13 - 36:18]

conveying letters, I'm just going to convey states and then ask the robot, okay, go to

### [36:18 - 36:18]

the state.

### [36:19 - 36:22]

And then Bob will look at where the robot goes and tries to guess like, oh, if you're

### [36:22 - 36:25]

at that state, then that was the state Alice wanted you to be at.

### [36:25 - 36:28]

So it's a different way of sending information, but you could show that exactly

### [36:28 - 36:30]

the same mathematical machinery applies.

### [36:31 - 36:32]

Interesting.

### [36:32 - 36:39]

Does your work on skill learning say anything about goal conditioned RL or kind of help the

### [36:39 - 36:43]

If you characterize goal conditioned RL as a special case, is there anything

### [36:43 - 36:46]

that we get for free or anything nice that we get?

### [36:47 - 36:52]

One really nice thing that we get is that it's a bit more grounded, this goal

### [36:52 - 36:54]

conditioned problem in the following sense.

### [36:54 - 36:59]

So when Alice and Bob are communicating with one another, they sort of have to

### [36:59 - 37:03]

make up a language, they have to establish, okay, when a robot does this, it means

### [37:03 - 37:08]

letter a, when a robot does this, it means letter B, but when we're doing these goal

### [37:08 - 37:08]

reaching problems.

### [37:09 - 37:11]

They don't need to make up any new language.

### [37:11 - 37:13]

They just say, well, this is the state and this is the state.

### [37:14 - 37:15]

And so it ends up being a lot easier.

### [37:15 - 37:20]

And I think that might be why sometimes these goal conditioned reinforcement learning

### [37:20 - 37:22]

methods are a lot easier to learn than some of these skill learning.

### [37:24 - 37:28]

And if we think about goal conditioned RL as a special case of skill learning, is

### [37:28 - 37:33]

there anything that skill learning can teach us about goal conditioned RL that

### [37:33 - 37:35]

helps us do goal conditioned RL better?

### [37:36 - 37:38]

One thing that might be useful.

### [37:38 - 37:44]

Is that we can use this connection to provide a bit of extra signal into the goal

### [37:44 - 37:46]

conditioned reinforcement learning problem.

### [37:47 - 37:51]

And so for example, let's again, say we have Alice and Bob, but let's say that the

### [37:51 - 37:54]

robot isn't very good, made of pretty low quality parts.

### [37:54 - 37:59]

And so when Alice says robot go here, the robot might only get close to there.

### [38:00 - 38:05]

If Alice and Bob have said, well, actually, if the robot gets close to the state, call

### [38:05 - 38:08]

it an a, if the robot gets close to this other state, call it a B.

### [38:08 - 38:14]

If they agree upon some protocol of, okay, things near here should count as A and

### [38:14 - 38:18]

things near here should count as B, then the problem becomes a bit easier to solve.

### [38:18 - 38:23]

And he used the same idea to develop goal conditioned reinforcement learning

### [38:23 - 38:27]

algorithms that can provide a bit more structure saying, well, if I tell you to

### [38:27 - 38:31]

get to this one state, it's okay if you actually get to a couple of nearby states.

### [38:31 - 38:33]

And that flexibility can make it a bit easier to learn.

### [38:34 - 38:35]

That makes sense.

### [38:35 - 38:36]

Awesome.

### [38:36 - 38:38]

And so you said that this initial project only took one.

### [38:38 - 38:40]

month and then you kind of moved on to something else.

### [38:40 - 38:43]

What did you move on to and what were you thinking about at that time?

### [38:43 - 38:44]

Yeah.

### [38:44 - 38:47]

So for full disclosure, the diversity project, it did take us a couple of months

### [38:47 - 38:49]

to watch out and get all the results.

### [38:50 - 38:52]

But the first prototype that was very quick was one sort of thing.

### [38:53 - 38:55]

I think it was one of like the two cases in my PhD, where we

### [38:55 - 38:57]

tried something and it just worked.

### [38:58 - 38:59]

That's such a nice feeling.

### [38:59 - 38:59]

I love that.

### [38:59 - 39:01]

And it's just like, oh, all the experiments worked.

### [39:01 - 39:01]

We're done.

### [39:01 - 39:01]

Great.

### [39:03 - 39:08]

An interesting side note on that before I kind of get back to your question throughout my PhD, I've kept.

### [39:08 - 39:14]

Fairly detailed track of the experiments I've run for different projects and end up logging each experiment

### [39:14 - 39:17]

and numbering it and saying, okay, this is why I'm running the experiment.

### [39:17 - 39:23]

This is the hypothesis that happens afterwards, which is useful for keeping track of things, but also gives us some useful

### [39:23 - 39:26]

metadata on how long does it take to do a research project?

### [39:27 - 39:29]

And the answer is about 200 experiments.

### [39:30 - 39:32]

Oh, interesting.

### [39:32 - 39:34]

How high is the variance around that?

### [39:34 - 39:35]

Yeah.

### [39:35 - 39:35]

What is that?

### [39:35 - 39:37]

Usually that's very fun.

### [39:37 - 39:38]

Like 180.

### [39:38 - 39:39]

Maybe to like 220.

### [39:40 - 39:44]

Usually you end up adding like a dozen experiments for rebuttals or after the initial paper.

### [39:45 - 39:51]

I mean, experiment might consist of trying a couple of different parameters or a couple of different ablations or whatnot.

### [39:51 - 39:58]

But if you launch one experiment today, then it gives a rough estimate for how long it takes to project.

### [39:59 - 40:00]

This is so interesting.

### [40:00 - 40:08]

I'm really curious what this number looks like for different researchers, because like, is it a bend shaped, is it that you solve bend shaped problems in about

### [40:08 - 40:09]

200 experiments?

### [40:09 - 40:12]

And for some reason, all bend shaped problems take about 200 experiments.

### [40:12 - 40:17]

Or is it that like 200 experiments somehow teaches you something new about the field?

### [40:17 - 40:20]

And then that like gets you enough information to go somewhere.

### [40:20 - 40:24]

Or is it that 200 experiments is exactly enough to publish a paper?

### [40:24 - 40:25]

I cleared nerves, I assume.

### [40:26 - 40:27]

Yeah.

### [40:27 - 40:29]

And make your paper say 2000.

### [40:29 - 40:36]

And I don't know, it probably depends on the taste of research.

### [40:36 - 40:38]

And people work with a giant language.

### [40:38 - 40:43]

Models, maybe they just use five experiments, but each one might crash many times.

### [40:43 - 40:45]

You have to restart it and lots of different challenges there.

### [40:46 - 40:47]

Right.

### [40:47 - 40:47]

That's interesting.

### [40:47 - 40:50]

Have you learned anything else from logging all your experiments?

### [40:51 - 40:54]

There are a couple of sort of best practices that have been useful.

### [40:54 - 41:04]

One is this idea of before running an experiment, actually writing down the questions that I'm curious in, because very often when the experiment's over, the temptation is, well, this one didn't work.

### [41:04 - 41:05]

This one worked the best.

### [41:05 - 41:06]

Why don't I try the variations on the best one?

### [41:07 - 41:08]

But often there are other interesting questions.

### [41:08 - 41:15]

Like, well, the reason I thought that A was going to be better than B was because of this mathematical thing.

### [41:16 - 41:24]

And then I can actually go back and look at the log and say like, okay, well, maybe the performance was not consistent with that, but is there anything else that might explain?

### [41:24 - 41:31]

I think very often there's this sort of temptation to focus just on the learning curves and just on performance metrics.

### [41:31 - 41:35]

I think as machine learning researchers, we're really, really good at optimizing things.

### [41:35 - 41:36]

And that's good.

### [41:36 - 41:38]

Like, as long as we have the right metrics and optimizing them.

### [41:38 - 41:38]

Yeah.

### [41:38 - 41:39]

That's good.

### [41:39 - 41:42]

But I think very often we miss opportunities to learn things from experiments.

### [41:43 - 41:44]

That's totally true.

### [41:44 - 41:51]

Do you log these experiments in any particular format or in like a type of software or what?

### [41:51 - 41:54]

It's a, they're definitely great software for doing this.

### [41:54 - 42:00]

I have enormous Google docs that are just, okay, I'm running experiment 143.

### [42:00 - 42:03]

There are four questions I'm interested in here.

### [42:03 - 42:06]

Does learning rate decrease the variance of this thing?

### [42:06 - 42:08]

And on this task, does this camera.

### [42:08 - 42:09]

Does this camera angle work better?

### [42:10 - 42:16]

And then I'll have a little comment saying, Hey, come back and look at this experiment on Tuesday when it should be complete.

### [42:16 - 42:18]

Definitely not the most sophisticated way of doing this.

### [42:18 - 42:20]

There are probably better ways of doing it, but it's worked well.

### [42:21 - 42:22]

It's actually really funny.

### [42:22 - 42:25]

I feel like everyone I talk to is like, yes, I just write in a big document.

### [42:27 - 42:28]

That's awesome.

### [42:28 - 42:31]

What were some of the other best practices that you learned from your experiment logging?

### [42:32 - 42:35]

One thing that's been useful is visualizing things.

### [42:35 - 42:37]

Looking, not just at learning curves.

### [42:37 - 42:45]

Not just at the other metrics, but especially for reinforcement learning problems, trying to see, okay, well, why is it failing?

### [42:45 - 42:46]

Are there certain cases where it's failing?

### [42:47 - 42:50]

And sometimes that gives intuition for how to then improve the algorithms.

### [42:50 - 42:55]

Very often also just reveals bugs in the simulators themselves, which is also very useful.

### [42:56 - 43:00]

For example, if the camera is configured so that you can't see anything, then it'll be very challenging to solve the task.

### [43:02 - 43:02]

Yeah.

### [43:02 - 43:03]

Or if it's a blinking light.

### [43:03 - 43:04]

Exactly.

### [43:05 - 43:07]

Actually, that reminds me of another one.

### [43:07 - 43:12]

One of my favorite papers, I think, was Interactive Visualization for Debugging RL.

### [43:12 - 43:18]

Have you made like a sort of, A, have you continued using this stuff in that paper, or B, what was that paper sort of about?

### [43:18 - 43:20]

And C, like how have things changed?

### [43:20 - 43:21]

And do you continue to do that going forward?

### [43:21 - 43:25]

Do you have like your own super secret suite of tools that you use, or are you kind of like ad hoc way through each time?

### [43:25 - 43:27]

Or sort of how has that evolved since the paper?

### [43:28 - 43:28]

Yeah.

### [43:28 - 43:32]

So that was a paper led by Shubhi, who was a master's student here at CMU.

### [43:32 - 43:37]

And there we were looking at, well, reinforcement learning algorithms are hard to use, but they're also great.

### [43:37 - 43:41]

And is there any way that we can develop software that makes it easier to debug these tools?

### [43:42 - 43:52]

And some of the visualizations that should be developed, we're looking at, well, can we identify the states or actions where maybe your predictions about the rewards are going to be wrong?

### [43:53 - 43:58]

Or can we look at the states or actions where you think you're getting really high rewards or really low rewards?

### [43:58 - 44:02]

The visualizations that he produced were really beautiful.

### [44:02 - 44:03]

I think they're really good.

### [44:04 - 44:07]

I think that in terms of getting people to adopt these tools.

### [44:07 - 44:13]

There's always this trade-off in terms of adding more tools adds complexity and people usually have existing workflows.

### [44:14 - 44:26]

And so the sort of million dollar question is, can this new tool that makes it slower to do research frequently identify bugs or frequently tell you things that you didn't know before?

### [44:27 - 44:28]

And we weren't able to answer that question.

### [44:29 - 44:30]

It may have been that we were looking at the wrong metrics.

### [44:31 - 44:34]

It may have been, we just didn't know the right way to interpret these metrics.

### [44:35 - 44:35]

That makes sense.

### [44:35 - 44:36]

Yeah.

### [44:36 - 44:39]

Getting back to the second question about super secret tools.

### [44:39 - 44:46]

I don't think of anything that's especially secret, besides sort of like standard things of, in reinforcement learning, things are unstable.

### [44:46 - 44:54]

So it's useful to have ways of launching many experiments in parallel and sweeping over hyper parameters, visualizing the results afterwards.

### [44:54 - 45:06]

Perhaps the most useful thing, the thing that saved me the most amount of time is when visualizing results and plotting learning curves or pulling data or whatever, caching the intermediate results.

### [45:06 - 45:07]

It's a one line chain.

### [45:07 - 45:14]

Uh, I think there in Python, there's a packet func tools that will automatically cast the results of any function.

### [45:15 - 45:23]

And so when reading logs from disks that are big, that function has saved me probably many, many days of my life of not having to wait around.

### [45:24 - 45:24]

Yep.

### [45:25 - 45:26]

Definitely.

### [45:26 - 45:26]

Yeah.

### [45:27 - 45:27]

That's awesome.

### [45:28 - 45:30]

Going back to after diversity is all you need.

### [45:31 - 45:33]

Where did you go next in terms of questions you're interested in?

### [45:34 - 45:35]

So after that, I largely looked at these goal.

### [45:35 - 45:35]

Okay.

### [45:36 - 45:41]

Condition problems, these sort of restricted cases, skill learning methods, where they're defined by just having a goal state.

### [45:41 - 45:43]

We need to figure out, okay, what are the actions to get to some goal state?

### [45:44 - 45:48]

And this ended up proven to be a fairly fruitful area to investigate.

### [45:49 - 45:58]

And one of the sort of fun things there was we ended up looking at the connections between these goal reaching problems and a whole bunch of different areas of machine learning, largely outside of reinforcement.

### [45:59 - 46:05]

So one thing that we looked at was how these goal conditioned reinforcement learning methods.

### [46:05 - 46:11]

Are similar and different from other planning-based methods.

### [46:11 - 46:21]

So historically in computer science, there's sort of been two different ways of solving decision-making problems there that learning-based methods, reinforcement learning methods, Q learning, reinforced methods like that.

### [46:21 - 46:35]

And they're planning-based methods, methods that solve like the towers of Hanoi or solve the Rubik's Q, methods that are based on various sorts of graph search and each of these methods, they can solve really, really cool problems.

### [46:35 - 46:37]

But the problems are pretty distinct from each other.

### [46:38 - 46:43]

The planning-based methods, they often require some symbolic representation of the world.

### [46:44 - 46:49]

Like in the towers of Hanoi, if you know, okay, if you take this action, you get to this other state, then it becomes tripled.

### [46:50 - 46:52]

You can just run breadth research and solve the towers of Hanoi.

### [46:53 - 47:02]

And in contrast, these reinforcement learning methods, they're really good at reasoning over reasonably high dimensional data, but it's fairly well known.

### [47:02 - 47:04]

They can't solve very long horizon tasks.

### [47:04 - 47:05]

They struggle to solve those sorts of tasks.

### [47:06 - 47:20]

Even though the benchmarks may have hundreds or thousands of time steps, very often these tasks are actually pretty easy because they involve repeated behavior or they involve tasks where the actions you take one after another are almost identical.

### [47:21 - 47:25]

And so we were looking at, well, can we leverage the strengths of these two methods?

### [47:25 - 47:34]

Can we leverage the long horizon reasoning capabilities of these planning-based methods with the high dimensional nature of these reinforcement learning methods?

### [47:34 - 47:35]

And that's what we did in the paper.

### [47:35 - 47:35]

Yeah.

### [47:35 - 47:37]

It's called search on the replay buffer.

### [47:38 - 47:43]

In that paper, we were looking at a specific type of planning method called randomized planning.

### [47:43 - 47:47]

These are methods like RRT that are pretty common in the robotics community.

### [47:47 - 47:57]

Those methods, what they require is they require some sort of local policy, some goal condition policy that will get you from any state to any nearby state.

### [47:57 - 48:04]

And they require some distance function or something that tells you, is there going to be a collision-free path from some state to some nearby state?

### [48:04 - 48:16]

And once they have these two pieces, they can build a graph, and then using this graph, they can automatically find some sequence of waypoints or breadcrumbs that would lead you from your current state to some goal.

### [48:17 - 48:24]

And then once you have these breadcrumbs, you can use equally the breadcrumbs in turn to figure out what actions to take to get to the goal.

### [48:25 - 48:33]

Now, ordinarily the limitation of these methods is that defining this goal condition policy is hard if you have like high dimensional inputs, or if you're controlling a robot with many degrees of freedom.

### [48:33 - 48:37]

And defining these collision-free paths is also hard.

### [48:37 - 48:42]

If you have, say, two images, how do you know, are these images close to each other or are they not?

### [48:43 - 48:47]

They, maybe the pixels look really different, but maybe that's just because it's darker in one room than another room.

### [48:49 - 48:54]

But it's exactly these limitations that we've been able to address using reinforcement learning methods.

### [48:54 - 48:57]

Because the reinforcement learning methods, they can reason over the height and magnitude of data.

### [48:58 - 49:01]

And by running them, we simultaneously learn how to select the actions.

### [49:02 - 49:03]

But these methods, they often.

### [49:04 - 49:18]

Give us some notion of a distance between states, precisely their Q function, their thing that predicts the reward, the, how likely it is to get to some goal state that can be used as a distance function for these planning methods.

### [49:19 - 49:25]

What are some of the difficulties of this approach of finding breadcrumbs when you're actually doing robotics work?

### [49:26 - 49:28]

There are a couple challenges.

### [49:28 - 49:32]

One is that the number of breadcrumbs can get really, really, really, really big.

### [49:32 - 49:32]

Yeah.

### [49:32 - 49:33]

Especially.

### [49:33 - 49:35]

As the tasks that we want to solve grow in complexity.

### [49:36 - 49:41]

So where we will see these methods used most typically are 2d navigation environments.

### [49:41 - 49:45]

And so you only have to say, scatter the breadcrumbs on the ground.

### [49:45 - 49:53]

You can imagine instead, if you want to control like a quadcopter flying around now, you would need to have breadcrumbs, not just on the ground, but floating everywhere in midair.

### [49:54 - 49:56]

And now you have to, we'd have way, way more breadcrumbs.

### [49:57 - 50:03]

And similarly, if you now want to have other degrees of freedom, like you want to control the speed that the quadcopter is flying.

### [50:03 - 50:08]

Well, now you have to have even more breadcrumbs because I guess this number of breadcrumbs makes it a challenge.

### [50:09 - 50:17]

And so you end up with this problem where the nice thing about planning-based methods is that you have a relatively small state space because it's human curated.

### [50:17 - 50:24]

Whereas here you're kind of trying to discover the space to search over, but that space is still too large or very, can be very large.

### [50:25 - 50:32]

Is this ever applied to things that are not 2d or like, how is this extended to things that are not 2d navigation tasks?

### [50:32 - 50:33]

Like 2d navigation tasks.

### [50:33 - 50:34]

It kind of makes sense.

### [50:35 - 50:38]

Just cover the world, you know, like how far are they or machine learning can learn that.

### [50:38 - 50:38]

Okay.

### [50:38 - 50:39]

It's like pretty straightforward.

### [50:40 - 50:54]

But then if you're thinking about, you know, taking actions in a browser or you're thinking about, you know, some other tasks, which does have some tasks and like things you need to do along the way, but potentially a pretty different kind of space, like has there been work or how do you sort of extend this to those types of things?

### [50:54 - 50:57]

Or would you extend this or maybe do something else instead?

### [50:58 - 51:00]

I'm not expert in the browser navigation settings.

### [51:00 - 51:02]

There has been some really interesting work there.

### [51:03 - 51:03]

I think.

### [51:03 - 51:10]

One thing that's pretty nice about the browser is that we have a reasonably good symbolic representation of browsers and of web links.

### [51:11 - 51:23]

And so people sometimes use reinforcement learning to learn how to navigate Wikipedia, which I'm a little bit unsure about sometimes, because if you have a graph, we have pretty good graphs, search algorithms.

### [51:23 - 51:32]

I think some of the really exciting applications are ones where the data is a lot messier, where we don't have really, really nice graph representations.

### [51:32 - 51:33]

Say, if you want to go from.

### [51:33 - 51:41]

An image of a to-do list to something that will figure out how to navigate your web browser, to solve all the things on your to-do list is a much more challenging.

### [51:43 - 51:43]

Yeah.

### [51:43 - 51:47]

That's sort of what I didn't even mean to refer to the Wikipedia navigation problem.

### [51:47 - 51:53]

I actually meant that like using a browser to do something like to write, they were to do some research and then compile them to this other thing.

### [51:53 - 51:58]

And then the other thing would like to accomplish a task, like navigating that task space basically.

### [51:58 - 51:59]

Yeah.

### [51:59 - 52:03]

I think one thing that's kind of interesting about the web browser application is that.

### [52:03 - 52:09]

There's so many possible things you can do on the internet, but there's also reasonably good instructions for a lot of things that we do on the internet.

### [52:10 - 52:18]

And very often the things that we do on the internet follow a certain form where the people designing some new web service will look at what people have done before.

### [52:18 - 52:20]

And so they'll likely follow a similar format.

### [52:21 - 52:33]

So if you want to buy something on most e-commerce websites, you click on a cart and then you confirm the objects in your cart, then you enter some shipping address, and then the next page is a billing address.

### [52:33 - 52:36]

Or a credit card information, and there's some confirmation page.

### [52:36 - 52:37]

And these steps are almost always the same.

### [52:38 - 52:48]

And because these steps are very similar, we've seen that these really, really big language models are often actually reasonably good at solving these sorts of tasks, or at least generating the instructions to solve these tasks.

### [52:49 - 52:52]

Kind of going to answer your question about, well, how can we solve these tasks?

### [52:52 - 52:56]

I think these really powerful language models give us a good clue on how to get started.

### [52:57 - 52:59]

Now, I don't think they're all the solution.

### [52:59 - 53:02]

We know that these giant language models can answer even simple, factual questions.

### [53:02 - 53:02]

Yeah.

### [53:02 - 53:02]

Yeah.

### [53:02 - 53:02]

Yeah.

### [53:02 - 53:02]

Yeah.

### [53:02 - 53:03]

Yeah.

### [53:03 - 53:03]

Yeah.

### [53:03 - 53:03]

Yeah.

### [53:03 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:04 - 53:04]

Yeah.

### [53:05 - 53:09]

Yesterday I was asking is negative two or negative three bigger.

### [53:09 - 53:15]

And I guess the answer not only is it wrong, but it gives a full paragraph describing why his wrong answer is correct.

### [53:18 - 53:18]

It's really funny.

### [53:20 - 53:29]

It claims that the second largest state in the U S is Montana, which is also incorrect, which is neither the largest state in the U S nor the continental U S.

### [53:32 - 53:33]

That's really interesting.

### [53:33 - 53:39]

But these models are learning something, and I think that there's probably really

### [53:39 - 53:43]

nice ways of combining these methods with reinforcement learning methods so they actually

### [53:43 - 53:44]

accomplish our tasks.

### [53:44 - 53:49]

We know how, like for these chat GPT models, we know that they are already using a pretty

### [53:49 - 53:53]

simple version of reinforcement learning to tune and adapt these models, and I'm really

### [53:53 - 53:55]

excited to see where that goes.

### [53:55 - 53:59]

Can we use this to make these methods, these giant language models, reason not just about

### [53:59 - 54:05]

the accuracy of the next post, but I feel like proactively ask questions to get what

### [54:05 - 54:06]

you really care about.

### [54:06 - 54:08]

Yeah, totally agree.

### [54:08 - 54:12]

So I guess the answer to the question Josh posed then would be, don't use serve time

### [54:12 - 54:16]

and replay buffer in these really high dimensional spaces, maybe use a large language model in

### [54:16 - 54:21]

situations where it can actually give reasonable answers, but there are going to be situations

### [54:21 - 54:22]

where it doesn't.

### [54:22 - 54:24]

Yeah, I think that's fair.

### [54:24 - 54:25]

Cool.

### [54:25 - 54:26]

And then what happened after that?

### [54:26 - 54:29]

You were interested in goal condition problems.

### [54:29 - 54:29]

Yeah.

### [54:29 - 54:34]

And it seemed like there were a bunch of other ideas that came out of your interest there.

### [54:34 - 54:36]

Can you describe some of them?

### [54:36 - 54:37]

Yeah.

### [54:37 - 54:43]

So one of the challenges with the search on the replay buffer was that it was mainly limited

### [54:43 - 54:46]

by the abilities of this goal condition policy.

### [54:46 - 54:50]

We knew that when you combine these goal condition methods with planning, you can extend the

### [54:50 - 54:54]

capabilities by 10x up to 100x.

### [54:54 - 54:59]

So if we just improve this base unit, this goal condition policy, we knew we would always

### [54:59 - 54:59]

be able to get this 10x.

### [54:59 - 55:00]

So how do we improve this underlying component?

### [55:00 - 55:07]

And we looked at a couple of different ways of doing that.

### [55:07 - 55:13]

One way we looked at doing that was as framing it as a imitation learning problem.

### [55:13 - 55:17]

And this is an approach that we were not the first to use, but there's a bunch of sort

### [55:17 - 55:22]

of simultaneous work around the same time that was trying to answer the following question.

### [55:22 - 55:27]

If you have a full bunch of data sequence of the states and actions, can you somehow

### [55:27 - 55:29]

use this data to figure out, well, if I'm at this state, what do I do?

### [55:29 - 55:34]

And if I want to get to this state, what action should I take?

### [55:34 - 55:37]

So this question, it feels a bit like B's rule, sort of saying, well, if you know that

### [55:37 - 55:41]

you want something to happen, what will be the action that you take?

### [55:41 - 55:43]

And it turns out you can learn this just from data.

### [55:43 - 55:48]

You can say, okay, given all this data we've seen, we saw an example of this state and

### [55:48 - 55:50]

this action, and this was the state we ended up at.

### [55:50 - 55:55]

And so thinking backwards, if we wanted to get to this state, this action that we took,

### [55:55 - 55:56]

this would be a good action.

### [55:56 - 55:59]

And so we spent some time thinking about, well, what do we do?

### [55:59 - 56:00]

Do these methods work?

### [56:00 - 56:01]

And the answer is yes.

### [56:01 - 56:04]

Do they have nice theoretical properties?

### [56:04 - 56:07]

How are they related to the reinforcement learning problem?

### [56:07 - 56:14]

It turns out that they're very closely related to sort of reward maximization and these more

### [56:14 - 56:17]

conventional reward maximization approaches.

### [56:17 - 56:22]

But there's a few details that you have to get right, both in terms of the theory and

### [56:22 - 56:26]

in terms of the actual architectures and hyperparameters that you use.

### [56:26 - 56:27]

So we spent a fair bit...

### [56:27 - 56:29]

That was probably a year or two of my PhD.

### [56:29 - 56:32]

Reasoning about these imitation-based goal-reaching things.

### [56:32 - 56:33]

What did you learn?

### [56:33 - 56:37]

What were the conclusions of, yeah, what are those nuances and what are those things you

### [56:37 - 56:38]

need to get right?

### [56:38 - 56:41]

Some of them are fairly standard tricks.

### [56:41 - 56:46]

So in a paper led by Scott Emmons at Berkeley, we looked at a bunch of the sort of deep learning

### [56:46 - 56:49]

tricks that are required for getting these methods to work.

### [56:49 - 56:54]

So one thing that ends up being important is to throw bigger models at them.

### [56:54 - 56:56]

Turns out bigger models, they work really, really well.

### [56:56 - 56:59]

This is a bit surprising at the time.

### [56:59 - 57:05]

My intuition before this was that main challenges would just be having enough data, but it turns

### [57:05 - 57:10]

out that even if you keep the data set reasonably small but make the models bigger, you're able

### [57:10 - 57:14]

to do better and better, suggesting that even small amounts of data actually have a fairly

### [57:14 - 57:19]

large amount of signal from which you can learn what actions to take to get to certain

### [57:19 - 57:20]

goals.

### [57:20 - 57:22]

Other tricks were looking at regularization.

### [57:22 - 57:26]

Again, if we're learning, we're training big models on small data, we're prone to overfitting.

### [57:26 - 57:28]

And so certain tricks about measuring goals.

### [57:28 - 57:33]

Measuring validation loss and making sure that we don't overfit, adding certain types

### [57:33 - 57:36]

of regularization, those ended up being important too.

### [57:36 - 57:41]

Did you ever explore a domain in which there is a lot of data and that was no longer

### [57:41 - 57:42]

a challenge?

### [57:42 - 57:46]

We looked a bit at scaling with data set size.

### [57:46 - 57:48]

Performance does increase.

### [57:48 - 57:53]

I think that one of the real challenges that we run into is one of benchmarking.

### [57:53 - 57:58]

So the data sets that we would like to have be like really, really rich simulations.

### [57:58 - 58:02]

So there's a lot of simulators where there's lots of diversity of things that you can

### [58:02 - 58:07]

do and they feel diversity, but we don't have very simulators of that today.

### [58:07 - 58:12]

And so the simulators that we have today are usually relatively confined.

### [58:12 - 58:13]

And so the performance ends up maxing out.

### [58:13 - 58:16]

You end up being able to solve a lot of those tasks nearly perfectly.

### [58:16 - 58:20]

Now on the flip side, there's been some really great work in trying to actually go out into

### [58:20 - 58:24]

the real world and collect this data and then learn from this data.

### [58:24 - 58:26]

But again, if you learn from real world data.

### [58:26 - 58:27]

You need to evaluate the data.

### [58:27 - 58:28]

You need to evaluate the data.

### [58:28 - 58:32]

You need to evaluate the things that you've learned and you don't have some simulator.

### [58:32 - 58:35]

Then you actually have to deal with all the robotics challenges and evaluating these models.

### [58:35 - 58:37]

There's been some great work in looking at this.

### [58:37 - 58:42]

We spent a little bit of time in collaboration with Ruf Shaw and Nick Reinhardt, looking

### [58:42 - 58:47]

at, can you apply these sort of methods to physical robots in the outdoor world?

### [58:47 - 58:51]

Showing that they can work reasonably well, but there's certain tricks again, that you

### [58:51 - 58:52]

have to get right.

### [58:52 - 58:55]

It turns out that providing extra signals can be useful.

### [58:55 - 58:57]

So if you want to go outside and incorporating things like GPS signals.

### [58:57 - 59:00]

Those can be useful.

### [59:00 - 59:05]

What are some of the limitations of this kind of training as an imitation learning problem?

### [59:05 - 59:10]

Are there things you, yeah, I guess, what are the limitations of the training?

### [59:10 - 59:12]

I think there are two main limitations.

### [59:12 - 59:17]

One of which is relatively easy to fix and the other is a bit more challenging.

### [59:17 - 59:22]

One of the limitations is that imitation learning is different from reinforcement.

### [59:22 - 59:25]

Imitation learning is about replicating the things that happened in the past.

### [59:25 - 59:27]

Reinforcement is maximizing these rewards.

### [59:27 - 59:33]

Now, it seems like because when we're doing this imitation learning, because we're looking

### [59:33 - 59:39]

forward in time and saying, only if you reach this goal, should you imitate this action?

### [59:39 - 59:43]

Maybe this brings us a bit closer to the reinforcement learning problem, but they still seem really

### [59:43 - 59:44]

different from each other.

### [59:44 - 59:50]

For example, when you're doing this imitation learning, you don't have any rewards anywhere.

### [59:50 - 59:55]

And so one thing that we spent a bit of time working on was some theoretical analysis,

### [59:55 - 59:57]

trying to bridge this divide, trying to figure out.

### [59:57 - 01:00:02]

Are these imitation learning methods, are they maximizing some reward function?

### [01:00:02 - 01:00:06]

If not, is there a way to make them maximize some reward?

### [01:00:06 - 01:00:10]

And the answer is that they do almost maximize some reward function.

### [01:00:10 - 01:00:15]

It turns out that they end up maximizing a combination of a reward function, a really

### [01:00:15 - 01:00:21]

standard conventional reward function, plus a very, very strong regularization.

### [01:00:21 - 01:00:23]

So what does that mean?

### [01:00:23 - 01:00:26]

That means that these methods are very highly regularized.

### [01:00:26 - 01:00:27]

And I might explain why.

### [01:00:27 - 01:00:31]

They work really, really well when we're learning from small amounts of data or when

### [01:00:31 - 01:00:36]

we're in the offline setting where we don't get to go interact, try something out and

### [01:00:36 - 01:00:38]

see whether it works or not.

### [01:00:38 - 01:00:43]

On the flip side, it means that when we don't need that much regularization, for example,

### [01:00:43 - 01:00:48]

if we have a large amount of data or we think the data is biased in some way, or we know

### [01:00:48 - 01:00:52]

that we'll be able to go and iteratively collect some more data, then these methods are probably

### [01:00:52 - 01:00:54]

too regularized.

### [01:00:54 - 01:00:57]

And just doing these reinforcement learning methods might be more effective.

### [01:00:57 - 01:01:03]

How do you determine what this reward is that it's maximizing?

### [01:01:03 - 01:01:05]

Is it like an inverse RL type thing?

### [01:01:05 - 01:01:09]

It is a thing even simpler than inverse reinforcement learning.

### [01:01:09 - 01:01:12]

So here's the intuition.

### [01:01:12 - 01:01:16]

When we're doing these, how do these conditional imitation learning methods work?

### [01:01:16 - 01:01:21]

They typically say, okay, you have a sequence of the states and the actions, and we'll generate

### [01:01:21 - 01:01:26]

training examples, which will consist of the state and the action and some future state.

### [01:01:26 - 01:01:27]

If you want to make this conditional learning, you can do that.

### [01:01:27 - 01:01:30]

So we have a connection between these imitation learning methods and these reinforcement learning

### [01:01:30 - 01:01:31]

methods.

### [01:01:31 - 01:01:35]

We have to precisely define what it means to do these imitation learning methods.

### [01:01:35 - 01:01:40]

So we'll say the training examples will consist of the states and the actions and the future

### [01:01:40 - 01:01:47]

states where the future states are sampled from a geometric distribution, meaning that

### [01:01:47 - 01:01:50]

they're probably going to be one or two time steps in the future, but with lower probability,

### [01:01:50 - 01:01:54]

it might be three or four or five or more times steps.

### [01:01:54 - 01:01:57]

So this way of sampling the future.

### [01:01:57 - 01:02:03]

So in the future states, this geometric distribution, it looks very, very similar to the discounted

### [01:02:03 - 01:02:08]

rewards that we see in reinforcement, because in reinforcement learning, we want to maximize

### [01:02:08 - 01:02:14]

this geometric weights times the rewards at the future states.

### [01:02:14 - 01:02:18]

And so precisely, at least in tabular settings, you can say, well, your reward is one if you

### [01:02:18 - 01:02:20]

get to the goal and zero otherwise.

### [01:02:20 - 01:02:24]

In continuous or stochastic settings, you can define it in terms of a certain probability.

### [01:02:24 - 01:02:26]

That makes sense.

### [01:02:26 - 01:02:27]

And then the strong regularization.

### [01:02:27 - 01:02:31]

How did you determine that it was kind of equivalent to maximizing this reward plus

### [01:02:31 - 01:02:32]

the strong regularizer?

### [01:02:32 - 01:02:35]

Yeah, it ends up being fairly simple.

### [01:02:35 - 01:02:40]

These imitation learning methods, they are saying if you start here and you get here,

### [01:02:40 - 01:02:42]

what action did you take?

### [01:02:42 - 01:02:48]

Turns out that you can show that those same variables arranged in different order correspond

### [01:02:48 - 01:02:51]

exactly to your sum of rewards.

### [01:02:51 - 01:02:56]

In particular, if you look at the probability of the future state, given your state and

### [01:02:56 - 01:02:57]

your action.

### [01:02:57 - 01:03:01]

You can show that exactly corresponds to your discounted sum of rewards.

### [01:03:01 - 01:03:04]

And so how are these two things related?

### [01:03:04 - 01:03:06]

Well, we can use B's rule to figure that out.

### [01:03:06 - 01:03:11]

So you can relate the probability of the actions given the state and the goal to the probability

### [01:03:11 - 01:03:14]

of the goal given the state and the actions.

### [01:03:14 - 01:03:19]

And when you do that, you see there's an extra term that is exactly the regularizer.

### [01:03:19 - 01:03:21]

That's so nice.

### [01:03:21 - 01:03:22]

Wow.

### [01:03:22 - 01:03:25]

It's like, where's the proof?

### [01:03:25 - 01:03:27]

We said, that is the proof.

### [01:03:27 - 01:03:30]

That's really funny.

### [01:03:30 - 01:03:32]

Which paper is this one?

### [01:03:32 - 01:03:38]

This was something like imitating past successes can be very suboptimal.

### [01:03:38 - 01:03:42]

The title is lost from the fact that when you're doing this imitation, if your data

### [01:03:42 - 01:03:48]

is biased, then imitating the past data can be really bad.

### [01:03:48 - 01:03:53]

It can be so bad that it actually makes you worse than doing nothing, than just using

### [01:03:53 - 01:03:55]

a random policy.

### [01:03:55 - 01:03:56]

And even get worse.

### [01:03:56 - 01:04:00]

It turns out there's some settings where if you repeat this process, so you do these

### [01:04:00 - 01:04:04]

conditional imitation learning methods, and then you collect some more data and you repeat

### [01:04:04 - 01:04:05]

it.

### [01:04:05 - 01:04:08]

There are settings where this can result in performance that gets worse and worse and

### [01:04:08 - 01:04:09]

worse.

### [01:04:09 - 01:04:13]

And I think in that paper, there was a simple fix for that, or like relatively

### [01:04:13 - 01:04:14]

simple fix.

### [01:04:14 - 01:04:16]

Do you want to say just a little bit about what that was?

### [01:04:16 - 01:04:17]

Yeah.

### [01:04:17 - 01:04:19]

So this problem is that these two problems are still different.

### [01:04:19 - 01:04:22]

They differ by this extra regularizer term.

### [01:04:22 - 01:04:25]

But it turns out that we can get rid of that regularizer.

### [01:04:25 - 01:04:26]

That regularizer.

### [01:04:26 - 01:04:34]

It's equivalent to, it can be estimated by doing non-conditional imitation.

### [01:04:34 - 01:04:37]

So just predicting what are the actions given the state.

### [01:04:37 - 01:04:43]

And so by doing imitation learning twice, once conditioning on the goals in the future

### [01:04:43 - 01:04:48]

and once doing no conditioning, and then taking some ratio between those, we can provably

### [01:04:48 - 01:04:50]

remove this extra regularization term.

### [01:04:50 - 01:04:51]

Interesting.

### [01:04:51 - 01:04:55]

And when you do that, when you do find the ratio.

### [01:04:55 - 01:05:00]

Is that ratio the same on every problem or do you have to discover it for each problem?

### [01:05:00 - 01:05:02]

It's the same for every problem.

### [01:05:02 - 01:05:07]

It's the probabilities produced by one of these policies divided by the probabilities

### [01:05:07 - 01:05:10]

produced by the other of these policies.

### [01:05:10 - 01:05:12]

So it's different for each problem.

### [01:05:12 - 01:05:13]

It's just the formulation is the same.

### [01:05:13 - 01:05:14]

The formulation.

### [01:05:14 - 01:05:15]

Exactly.

### [01:05:15 - 01:05:16]

Yeah.

### [01:05:16 - 01:05:17]

Thanks.

### [01:05:17 - 01:05:18]

It's similar to the offline RL formulation.

### [01:05:18 - 01:05:19]

Yeah, absolutely.

### [01:05:19 - 01:05:24]

And I think also really interesting questions about the underlying quantity here takes the

### [01:05:24 - 01:05:25]

form of an importance weight.

### [01:05:25 - 01:05:28]

It's like one policy divided by another policy.

### [01:05:28 - 01:05:29]

Yeah, exactly.

### [01:05:29 - 01:05:34]

And instead of trying to learn both of them and then divide one by the other, can we directly

### [01:05:34 - 01:05:35]

estimate this?

### [01:05:35 - 01:05:37]

Ah, interesting.

### [01:05:37 - 01:05:42]

And there's some interesting literature on learning importance weights directly.

### [01:05:42 - 01:05:43]

We've explored this a bit.

### [01:05:43 - 01:05:47]

We haven't found anything that works significantly better, but I think it's a pretty interesting

### [01:05:47 - 01:05:49]

area to keep poking around at.

### [01:05:49 - 01:05:54]

As it is now, I guess the solution is to train these two different policies.

### [01:05:54 - 01:05:55]

Yeah.

### [01:05:55 - 01:06:00]

With net adult sort of empirical challenges, I guess, but at least in theory works.

### [01:06:00 - 01:06:06]

I think you said earlier that imitation is one way to frame this problem is, are there

### [01:06:06 - 01:06:08]

other approaches that you've taken?

### [01:06:08 - 01:06:09]

Yeah.

### [01:06:09 - 01:06:14]

I think the thing I'm most excited about right now is thinking about how we can approach

### [01:06:14 - 01:06:19]

these goal condition problems using a sort of contrast.

### [01:06:19 - 01:06:24]

So it's sort of the culmination work of less two years or so where we've been thinking

### [01:06:24 - 01:06:25]

about.

### [01:06:25 - 01:06:29]

How do we use contrastive learning to figure out how to solve these goal condition problems?

### [01:06:29 - 01:06:33]

And so in particular, we're going to think about contrastive learning across time.

### [01:06:33 - 01:06:39]

So let's say you have a video and you take frames of that video and you do the contrastive

### [01:06:39 - 01:06:40]

learning.

### [01:06:40 - 01:06:44]

So you say nearby frames should have similar representations and distant frames have distant

### [01:06:44 - 01:06:45]

representations.

### [01:06:45 - 01:06:47]

This is something that people have been doing for a long time.

### [01:06:47 - 01:06:52]

They've been doing it in NLP, they've been doing it in computer vision, and our sort

### [01:06:52 - 01:06:53]

of insight here was that.

### [01:06:53 - 01:06:54]

Yeah.

### [01:06:54 - 01:06:57]

We can also do this in the reinforcement learning setting.

### [01:06:57 - 01:07:04]

If we also include the actions, precisely, if we include the actions in our representations,

### [01:07:04 - 01:07:10]

then the distance between these representations, it will tell us something about how easy it

### [01:07:10 - 01:07:14]

is or how hard it is to get from one state to another.

### [01:07:14 - 01:07:17]

And it turns out you have to make this very precise.

### [01:07:17 - 01:07:21]

So the intuition that, okay, if you have two states that are nearby, that you have similar

### [01:07:21 - 01:07:22]

representations.

### [01:07:22 - 01:07:23]

Yeah.

### [01:07:23 - 01:07:27]

If you sample the future states, if you sample the future states using that same geometric

### [01:07:27 - 01:07:31]

distribution that we were discussing before, then you can show that the distances between

### [01:07:31 - 01:07:36]

these representations, whatever their dot product is or cosine similarity, that exactly

### [01:07:36 - 01:07:41]

corresponds to the likelihood of getting to some state in the future.

### [01:07:41 - 01:07:45]

So to clarify, you're training an encoder that's taking your observations and your

### [01:07:45 - 01:07:49]

actions and returning some latent variable.

### [01:07:49 - 01:07:50]

Exactly.

### [01:07:50 - 01:07:51]

Yeah.

### [01:07:51 - 01:07:52]

Hmm.

### [01:07:52 - 01:07:53]

Hmm.

### [01:07:53 - 01:07:55]

So what we've learned about this a little bit is by comparing it to planning.

### [01:07:55 - 01:08:01]

So if we think about having a maze and say you want to get from one end of the maze to

### [01:08:01 - 01:08:05]

the other end of the maze, ordinarily solving the maze is pretty hard.

### [01:08:05 - 01:08:08]

You have to try out a bunch of different routes and try to figure out, well, which will solve

### [01:08:08 - 01:08:09]

the maze best.

### [01:08:09 - 01:08:13]

But what we've done here is we've learned these representations in such a way that this

### [01:08:13 - 01:08:14]

planning problem comes really easy.

### [01:08:14 - 01:08:19]

It becomes such that once you've learned these representations, just taking the shortest

### [01:08:19 - 01:08:22]

path between the representations is the best thing to do.

### [01:08:22 - 01:08:23]

Yeah.

### [01:08:23 - 01:08:28]

And so if we imagine we learn these representations and the representations, Ellie, as you were

### [01:08:28 - 01:08:30]

mentioning before, they depend on the actions.

### [01:08:30 - 01:08:34]

And so we can test out different actions and say, well, if you take action one, what is

### [01:08:34 - 01:08:35]

it?

### [01:08:35 - 01:08:36]

The representation.

### [01:08:36 - 01:08:37]

Take action two.

### [01:08:37 - 01:08:38]

What does the representation look at?

### [01:08:38 - 01:08:43]

And let's say we want to get to some goal state and we can look at that representation.

### [01:08:43 - 01:08:46]

Now we see, okay, does the representation for action one or action two get us closer

### [01:08:46 - 01:08:48]

to the goal?

### [01:08:48 - 01:08:50]

And we select whichever one is closer to the goal.

### [01:08:50 - 01:08:51]

So.

### [01:08:51 - 01:08:52]

Yeah.

### [01:08:53 - 01:08:56]

So what you're doing in the head, what you're doing is you're passing in actions and observations

### [01:08:56 - 01:09:00]

into an encoder to get a latent variable using contrastive learning to train the encoder

### [01:09:00 - 01:09:07]

so that you end up with kind of the distance between actions, kind of telling us how hard

### [01:09:07 - 01:09:11]

one state is from another, because that is what contrastive learning is doing.

### [01:09:11 - 01:09:12]

Not the distance between actions.

### [01:09:12 - 01:09:13]

Exactly.

### [01:09:13 - 01:09:14]

Oh, between representations.

### [01:09:14 - 01:09:15]

Sorry.

### [01:09:15 - 01:09:16]

I don't think.

### [01:09:16 - 01:09:18]

I highly recommend that people look at the website and the paper for this, because there's

### [01:09:18 - 01:09:21]

very good diagrams that make it very clear what's going on.

### [01:09:21 - 01:09:26]

It's really hard to say in language, but yeah, I'll try and describe that a little

### [01:09:26 - 01:09:27]

more again.

### [01:09:27 - 01:09:28]

If you want.

### [01:09:28 - 01:09:32]

I'm not very good at describing 3d geometry and voice.

### [01:09:32 - 01:09:33]

Yeah.

### [01:09:33 - 01:09:38]

So we have like a representation of the state and what happens for action one and the state

### [01:09:38 - 01:09:40]

and what happens for action two.

### [01:09:40 - 01:09:46]

I think one way of thinking about this is that it's sort of like a model of the world,

### [01:09:46 - 01:09:50]

but rather than predicting what is the next state kernel look like, or what is the future

### [01:09:50 - 01:09:51]

state kernel?

### [01:09:51 - 01:09:57]

It's sort of predicting what is the representation of the future state going to look like.

### [01:09:57 - 01:10:00]

And then once we have this prediction, this representation, we can say, okay, does the

### [01:10:00 - 01:10:05]

prediction for action one or action two, is that prediction closer to the representation

### [01:10:05 - 01:10:07]

goal or further from it?

### [01:10:07 - 01:10:12]

And so you take the action that is closest to the goal, to the goal.

### [01:10:12 - 01:10:13]

Interesting.

### [01:10:13 - 01:10:17]

It's such an unusual way to do reinforcement learning.

### [01:10:17 - 01:10:19]

It's interesting.

### [01:10:19 - 01:10:21]

People have looked at using contrastive learning.

### [01:10:21 - 01:10:26]

In different ways for solving reinforcement learning problems, one way they've done it

### [01:10:26 - 01:10:31]

is they've used contrastive learning to learn representations that you can plug into another

### [01:10:31 - 01:10:32]

reinforcement learning.

### [01:10:32 - 01:10:33]

Right.

### [01:10:33 - 01:10:37]

Some other work that uses contrastive learning to learn a reward function that you

### [01:10:37 - 01:10:40]

can plug into another reinforcement learning.

### [01:10:40 - 01:10:43]

But it turns out that you can actually use contrastive learning to solve the reinforcement

### [01:10:43 - 01:10:45]

learning problem itself.

### [01:10:45 - 01:10:46]

I really like this.

### [01:10:46 - 01:10:48]

It's very interesting.

### [01:10:48 - 01:10:50]

Are there failures in RL that you can avoid?

### [01:10:50 - 01:10:51]

Yeah.

### [01:10:51 - 01:10:56]

There's a problem that's framed in this way of finding the closest representation.

### [01:10:56 - 01:11:00]

So I imagine that this is kind of similar to a model of the environment.

### [01:11:00 - 01:11:03]

And so it's interesting to think about, well, what happens if you just try to predict what

### [01:11:03 - 01:11:05]

happens next?

### [01:11:05 - 01:11:10]

Say you have a bunch of images, you see images of a robot doing something, you want to figure

### [01:11:10 - 01:11:11]

out what to do.

### [01:11:11 - 01:11:13]

Well, you can build a model, something that says, okay, given this current image and this

### [01:11:13 - 01:11:15]

action, what's going to happen next?

### [01:11:15 - 01:11:19]

And then you could choose some other action, try to predict what would happen after that

### [01:11:19 - 01:11:20]

and after that, after that.

### [01:11:20 - 01:11:21]

These methods.

### [01:11:21 - 01:11:26]

They're actually fairly common in a lot of robotic settings and they can work really

### [01:11:26 - 01:11:27]

well.

### [01:11:27 - 01:11:29]

But they have a couple of limitations.

### [01:11:29 - 01:11:34]

One is that if you have to predict every single pixel of the images, that's a really, really

### [01:11:34 - 01:11:36]

hard problem.

### [01:11:36 - 01:11:39]

And it means that these methods are often pretty slow and require a lot of compute.

### [01:11:39 - 01:11:44]

And the learning problem is so hard that given a finite sized model, if you only can fit

### [01:11:44 - 01:11:49]

a million or a billion parameters on your GPU, then all of the predictions are going

### [01:11:49 - 01:11:50]

to suffer a bit.

### [01:11:50 - 01:11:51]

Yeah.

### [01:11:51 - 01:11:55]

So one of the limitations of these methods is that if you just predict one step into

### [01:11:55 - 01:11:59]

the future, then you're going to have to predict another step and another step and another

### [01:11:59 - 01:12:04]

step to eventually figure out what are the right actions and states to get to whatever

### [01:12:04 - 01:12:06]

goal you want to get to.

### [01:12:06 - 01:12:12]

And with each additional prediction, you're feeding the predictions back in as inputs.

### [01:12:12 - 01:12:16]

And so this means that errors in your model can end up compounding.

### [01:12:16 - 01:12:19]

So our method lifts some of those limitations.

### [01:12:19 - 01:12:21]

Indeed, we find that on relatively simple problems.

### [01:12:21 - 01:12:25]

Those are some model-based methods that can work quite well, but on the more challenging

### [01:12:25 - 01:12:27]

problems they tend to struggle.

### [01:12:27 - 01:12:28]

It's interesting.

### [01:12:28 - 01:12:30]

So if I'm wrapping my head around this properly.

### [01:12:30 - 01:12:34]

So in model-based methods, you often do rollouts and you end up with this like compounding

### [01:12:34 - 01:12:35]

error problem.

### [01:12:35 - 01:12:39]

And also it's a really weird thing to do because like humans don't do rollouts.

### [01:12:39 - 01:12:46]

Here it seems like if you are framing it as contrastive learning problem, then you can

### [01:12:46 - 01:12:50]

not do rollouts and just take the action that at each step makes sense.

### [01:12:50 - 01:12:53]

Kind of toward the goal.

### [01:12:53 - 01:12:56]

So you can just have the goal stage and then not do any rollouts.

### [01:12:56 - 01:12:57]

Exactly.

### [01:12:57 - 01:12:58]

Yeah.

### [01:12:58 - 01:13:02]

I think it raises a really interesting question of what should we call this?

### [01:13:02 - 01:13:05]

Should we call our method a model-based method or not?

### [01:13:05 - 01:13:09]

Because it is learning a sort of model because it is giving a predict something, but not

### [01:13:09 - 01:13:11]

giving a prediction of the state.

### [01:13:11 - 01:13:17]

Now there's actually a sort of nice answer, which is nice from a semantics perspective,

### [01:13:17 - 01:13:20]

which is that in reinforcement learning.

### [01:13:20 - 01:13:24]

We often talk about actor-critic methods where the actor is the policy and the critic is

### [01:13:24 - 01:13:28]

the thing that predicts the rewards that you get in the future.

### [01:13:28 - 01:13:32]

And so it might be natural to say, well, contrastive learning is learning as critic.

### [01:13:32 - 01:13:37]

And it turns out that if you look at the contrastive learning literature, they also use this word

### [01:13:37 - 01:13:40]

critic to refer to the similarity between these representations.

### [01:13:40 - 01:13:41]

That's true.

### [01:13:41 - 01:13:45]

So the same word has been used in these two communities to describe what we've shown is

### [01:13:45 - 01:13:46]

actually the same object.

### [01:13:46 - 01:13:50]

So it's not a coincidence or it might be a very strong coincidence.

### [01:13:50 - 01:13:55]

But a surprising coincidence that these two communities call this object the same.

### [01:13:55 - 01:14:02]

I suppose this is an actor-critic policy where in theory, you could predict the next state

### [01:14:02 - 01:14:04]

of the world.

### [01:14:04 - 01:14:05]

I guess you can't.

### [01:14:05 - 01:14:06]

No, nevermind.

### [01:14:06 - 01:14:10]

Well, aren't you sort of predicting, oh, the representation of the next state?

### [01:14:10 - 01:14:11]

Yeah.

### [01:14:11 - 01:14:13]

Predicting the representation of the next state.

### [01:14:13 - 01:14:16]

But you could train some decoder to get the next state.

### [01:14:16 - 01:14:20]

And so you are kind of learning these transition probabilities.

### [01:14:20 - 01:14:21]

Exactly.

### [01:14:21 - 01:14:22]

Yeah.

### [01:14:22 - 01:14:26]

We're learning it sort of implicitly in a way that only requires us to sort of preserve

### [01:14:26 - 01:14:30]

the essential essence of what is required to reason about the actions.

### [01:14:30 - 01:14:34]

Because there's lots of things that you could predict that aren't necessary for solving

### [01:14:34 - 01:14:35]

the task.

### [01:14:35 - 01:14:39]

And you think about, well, if we're just doing this contrastive learning, then the only things

### [01:14:39 - 01:14:43]

that should be preserved from these representations are things that are required for reasoning

### [01:14:43 - 01:14:46]

about are these two states, is it possible to get between them?

### [01:14:46 - 01:14:48]

Would you expect this to generalize worse?

### [01:14:48 - 01:14:49]

Absolutely.

### [01:14:49 - 01:14:54]

Would you expect this to get worse out of distribution versus say a model-based method?

### [01:14:54 - 01:14:58]

Because it's, I guess if you train it on enough different types of tasks, maybe it would learn

### [01:14:58 - 01:14:59]

fairly robust representations.

### [01:14:59 - 01:15:00]

Yeah.

### [01:15:00 - 01:15:01]

I guess.

### [01:15:01 - 01:15:03]

Do you have any expectations around out of distribution generalization?

### [01:15:03 - 01:15:07]

Empirically, we've studied this question a bit.

### [01:15:07 - 01:15:10]

So we looked at say varying the colors and varying initial state distributions.

### [01:15:10 - 01:15:14]

I find this reasonably robust, as long as the shifts aren't too big.

### [01:15:14 - 01:15:17]

Theoretically, I don't have any concrete results.

### [01:15:17 - 01:15:19]

My intuition would be that.

### [01:15:19 - 01:15:22]

Because the function that you're learning is rather small.

### [01:15:22 - 01:15:28]

Because function that maps states to a scalar number, rather than mapping states to high

### [01:15:28 - 01:15:31]

dimensional next states, we're going to have a much bigger function.

### [01:15:31 - 01:15:35]

Maybe that will give us some reasons to expect that it will generalize better, because often

### [01:15:35 - 01:15:39]

simpler things generalize better, but it's mostly just speculation.

### [01:15:39 - 01:15:44]

If color's not relevant to the task being solved, then in theory, the whole benefit,

### [01:15:44 - 01:15:48]

one of the benefits of your method is that it's throwing away information about color,

### [01:15:48 - 01:15:48]

right?

### [01:15:48 - 01:15:52]

And it doesn't care about that information when it's making its representations.

### [01:15:52 - 01:15:54]

Is that right?

### [01:15:54 - 01:15:55]

Sort of.

### [01:15:55 - 01:15:56]

It ends up being kind of nuanced.

### [01:15:56 - 01:15:57]

So the method...

### [01:15:57 - 01:15:58]

So what's the method doing?

### [01:15:58 - 01:16:03]

It's predicting whether two states came from the same trajectory or nearby the same trajectory

### [01:16:03 - 01:16:04]

or from different trajectories.

### [01:16:04 - 01:16:10]

Now, there's a really easy way to answer that question, if the colors are different in different

### [01:16:10 - 01:16:11]

trajectories.

### [01:16:11 - 01:16:16]

So let's say that you like randomize the color of the background in every episode.

### [01:16:16 - 01:16:18]

Then you can just look at the background and say, well, if you have the same color, then

### [01:16:18 - 01:16:19]

it's probably the same trajectory.

### [01:16:19 - 01:16:20]

If it's different colors, it's probably different trajectories.

### [01:16:20 - 01:16:25]

Now, in theory, the method will still work because sometimes you sample the negative

### [01:16:25 - 01:16:30]

examples from the same trajectory, but say from the past or from the very distant future,

### [01:16:30 - 01:16:32]

but it'll be a lot harder.

### [01:16:32 - 01:16:38]

And so I suspect that our method will actually preserve colors if those colors are randomized

### [01:16:38 - 01:16:40]

across the episodes.

### [01:16:40 - 01:16:46]

Now, there might be more sophisticated ways of intentionally throwing away more information.

### [01:16:46 - 01:16:47]

And I suspect that would further improve the report.

### [01:16:47 - 01:16:47]

Yeah.

### [01:16:47 - 01:16:54]

In a practical sense, it seemed like, if I remember correctly from the paper, the results

### [01:16:54 - 01:16:57]

seemed pretty good on the task that you tried it off.

### [01:16:57 - 01:16:59]

It seemed like it did a little bit better.

### [01:16:59 - 01:17:03]

Although I did have some questions about practical limitations and how fast is it?

### [01:17:03 - 01:17:07]

Because I know contrastive learning can be a little bit slow sometimes for image purposes,

### [01:17:07 - 01:17:08]

right?

### [01:17:08 - 01:17:11]

Because you're not getting as many bits of B dot information, right?

### [01:17:11 - 01:17:15]

So I'm sort of curious about some of the practical considerations.

### [01:17:15 - 01:17:16]

Yeah.

### [01:17:16 - 01:17:17]

So.

### [01:17:17 - 01:17:20]

It turns out speed worked out really well in our favor.

### [01:17:20 - 01:17:26]

So the speed ends up being like four times faster than the prior state of the art methods.

### [01:17:26 - 01:17:31]

And it's way, way, way faster than learning a model of the world.

### [01:17:31 - 01:17:36]

Faster relative to like something super simple like PPO or faster as relative to something

### [01:17:36 - 01:17:39]

like Dreamer or something model based or.

### [01:17:39 - 01:17:42]

Relative to other actual critic methods.

### [01:17:42 - 01:17:46]

And that's largely just because we ended up not getting a lot of the tricks that other

### [01:17:46 - 01:17:47]

methods use.

### [01:17:47 - 01:17:48]

Yeah.

### [01:17:48 - 01:17:49]

So we don't need target networks.

### [01:17:49 - 01:17:51]

We don't need dueling networks.

### [01:17:51 - 01:17:54]

So it doesn't be very, very fast in that sense.

### [01:17:54 - 01:17:55]

It's not magic.

### [01:17:55 - 01:17:59]

And so there are some tasks we just aren't able to solve yet, largely because of the

### [01:17:59 - 01:18:01]

exploration problem.

### [01:18:01 - 01:18:07]

So one task you looked at was having a robot go and pick up a lid and put the lid on top

### [01:18:07 - 01:18:08]

of the box.

### [01:18:08 - 01:18:13]

And if you had about halfway there could go and could pick up the lid and the lid over

### [01:18:13 - 01:18:16]

to the box, but then it could never lay it down correctly on top of the box.

### [01:18:16 - 01:18:17]

It would always end up putting the lid on top of the box.

### [01:18:17 - 01:18:18]

It would always end up putting it down sideways.

### [01:18:18 - 01:18:19]

Interesting.

### [01:18:19 - 01:18:22]

Why do you think that is?

### [01:18:22 - 01:18:27]

Looking at what happened, it usually seemed like the lid would collide with the corner

### [01:18:27 - 01:18:31]

of the box and then it would get into some state that I hadn't seen before.

### [01:18:31 - 01:18:32]

Right.

### [01:18:32 - 01:18:36]

So once it's in some state that I hadn't seen before, it's kind of tricky for it to get

### [01:18:36 - 01:18:37]

out of that state.

### [01:18:37 - 01:18:40]

Now you're sort of, you were like, here's their goal, you're over here, kind of moving

### [01:18:40 - 01:18:41]

towards their goal.

### [01:18:41 - 01:18:43]

And then you're kind of.

### [01:18:43 - 01:18:44]

And so.

### [01:18:44 - 01:18:47]

I think there's a cool opportunity here.

### [01:18:47 - 01:18:53]

Which is that if this exploration is a major problem.

### [01:18:53 - 01:18:57]

Because we're learning these representations, they might give us a pretty cool way of doing

### [01:18:57 - 01:18:58]

better exploration.

### [01:18:58 - 01:19:03]

It's something we haven't looked at yet, but here's sort of my thinking.

### [01:19:03 - 01:19:08]

If we see all the states we've seen so far and look at their representations, let's imagine

### [01:19:08 - 01:19:11]

that those representations have a length of one.

### [01:19:11 - 01:19:13]

So we can think of them as points on a sphere.

### [01:19:13 - 01:19:16]

Then after we put each of these points on the sphere, we can turn the sphere around

### [01:19:16 - 01:19:21]

and say, okay, where are most of the points and where are missing points and say, well,

### [01:19:21 - 01:19:24]

you're missing points down near Antarctica or something.

### [01:19:24 - 01:19:27]

And then we can say, okay, let's try to get down to Antarctica.

### [01:19:27 - 01:19:32]

And then because we're learning a goal condition policy, we say, okay, try to get here or try

### [01:19:32 - 01:19:34]

to get to a state that has this representation.

### [01:19:34 - 01:19:36]

Oh, that's so nice.

### [01:19:36 - 01:19:37]

Wow.

### [01:19:37 - 01:19:38]

Interesting.

### [01:19:38 - 01:19:43]

And so here in theory, like for this lid problem, you could map all the representations onto

### [01:19:43 - 01:19:44]

the sphere.

### [01:19:44 - 01:19:45]

And then.

### [01:19:45 - 01:19:46]

Kind of like.

### [01:19:46 - 01:19:52]

You know, see if there are representations that are maybe close to the end goal, but

### [01:19:52 - 01:19:55]

like don't look exactly like it and you haven't explored those states before.

### [01:19:55 - 01:19:56]

Exactly.

### [01:19:56 - 01:19:57]

Yeah.

### [01:19:57 - 01:19:58]

Yeah.

### [01:19:58 - 01:20:02]

I wonder if you would end up learning, it feels like the representation space that is

### [01:20:02 - 01:20:04]

unexplored is actually quite large.

### [01:20:04 - 01:20:09]

And so I wonder kind of how you end up exploring useful states versus like nearby states versus

### [01:20:09 - 01:20:10]

ones that aren't.

### [01:20:10 - 01:20:11]

I don't know.

### [01:20:11 - 01:20:13]

It's like really, really hard question.

### [01:20:13 - 01:20:14]

I guess demonstrations.

### [01:20:14 - 01:20:15]

You could say.

### [01:20:15 - 01:20:16]

Yeah.

### [01:20:16 - 01:20:19]

You could say, okay, what are the representations of the demonstrations and try to get to those

### [01:20:19 - 01:20:20]

states.

### [01:20:20 - 01:20:21]

Yeah.

### [01:20:21 - 01:20:22]

That's interesting.

### [01:20:22 - 01:20:23]

Yeah.

### [01:20:23 - 01:20:27]

Another thing that just immediately jumps to mind when I saw this is like thinking about

### [01:20:27 - 01:20:32]

it in higher little stuff as a person, like I know my goal, like my goal is to, you know,

### [01:20:32 - 01:20:33]

get groceries.

### [01:20:33 - 01:20:37]

And like, there's a lot of steps, but I'm not thinking about like, oh, I'm moving closer

### [01:20:37 - 01:20:38]

and closer to the grocery store.

### [01:20:38 - 01:20:41]

Like I need to get my car and there's like a high level set of things that's happening,

### [01:20:41 - 01:20:44]

but in the same kind, like you might be able to solve that in the same way, but then within

### [01:20:44 - 01:20:46]

those goal conditions.

### [01:20:46 - 01:20:49]

You can sort of like, you can imagine this kind of thing being done at multiple levels

### [01:20:49 - 01:20:51]

at the same time, which I think is kind of interesting.

### [01:20:51 - 01:20:55]

Because also if I think about going to the grocery store, I don't like the traditional

### [01:20:55 - 01:20:56]

robot path planning.

### [01:20:56 - 01:20:58]

I don't plan out the whole thing before I do it.

### [01:20:58 - 01:20:59]

Right.

### [01:20:59 - 01:21:02]

I just kind of like get closer at my high level and then keep going until I'm done.

### [01:21:02 - 01:21:06]

For most of these tasks, I think that we do in the real world, they seem more like that

### [01:21:06 - 01:21:08]

cooking or going to the grocery store.

### [01:21:08 - 01:21:11]

Some there's, you know, like writing a software program or operating system.

### [01:21:11 - 01:21:12]

We're going to Mars there.

### [01:21:12 - 01:21:15]

We maybe need more explicit planning, but for a lot of the things we do as people, it

### [01:21:15 - 01:21:19]

feels like we can just do this incremental, just go straight towards it, but in a higher

### [01:21:19 - 01:21:20]

level sense.

### [01:21:20 - 01:21:21]

Yeah.

### [01:21:21 - 01:21:24]

I'm really interested in thinking about what are geometric ways of representing those higher

### [01:21:24 - 01:21:25]

times?

### [01:21:25 - 01:21:26]

Yeah.

### [01:21:26 - 01:21:30]

Like you represented as we were talking about before, how you can view this, the

### [01:21:30 - 01:21:36]

different observations as points on a sphere, on a globe, can we now view this as some other

### [01:21:36 - 01:21:37]

sort of celestia law?

### [01:21:37 - 01:21:42]

Like, can you view this as like a globe inside another globe where the inner globe is your

### [01:21:42 - 01:21:44]

high level plan and the outer globe is.

### [01:21:44 - 01:21:45]

Yeah.

### [01:21:45 - 01:21:46]

I think there's a lot of representation of that.

### [01:21:46 - 01:21:49]

In computer creation, people have looked at kind of similar representations.

### [01:21:49 - 01:21:55]

You know, a car is here and then certain makes and models of cars have like a similar angle,

### [01:21:55 - 01:21:58]

but are further out on a different steel object.

### [01:21:58 - 01:21:59]

Yeah.

### [01:21:59 - 01:22:02]

I have no idea how to do, but it does feel like this is sort of going in the direction

### [01:22:02 - 01:22:03]

of what I think is interesting.

### [01:22:03 - 01:22:04]

Yeah.

### [01:22:04 - 01:22:08]

Aside from currently not doing exploration and that part not being solved, are there

### [01:22:08 - 01:22:13]

other areas of formulating RLS and Trusted Learning that you feel like are interesting

### [01:22:13 - 01:22:14]

to explore?

### [01:22:14 - 01:22:18]

Are there any like problems that you're seeing that you'd want to explore next?

### [01:22:18 - 01:22:19]

Yeah.

### [01:22:19 - 01:22:25]

One thing that I'm really excited about is thinking about how we can leverage this idea

### [01:22:25 - 01:22:31]

of connecting Contrastive Learning to Reinforcement Learning to make use of advances in Contrastive

### [01:22:31 - 01:22:35]

Learning in other domains like NLP and Computer Vision.

### [01:22:35 - 01:22:41]

So in NLP, we've seen really great uses of Contrastive Learning, things like CLIP that

### [01:22:41 - 01:22:44]

can connect images with language using Contrastive Learning.

### [01:22:44 - 01:22:49]

And in our Contrastive Project, we saw how we can connect the states and the actions

### [01:22:49 - 01:22:50]

to the future states.

### [01:22:50 - 01:22:55]

It's a matter of fact that maybe there's a way of plugging these components together.

### [01:22:55 - 01:22:57]

And indeed, you can show that mathematically there is.

### [01:22:57 - 01:23:02]

So one thing I'm really excited in exploring is saying, well, can we use this to specify

### [01:23:02 - 01:23:06]

tasks, not in terms of images of what you would want to happen, but rather language

### [01:23:06 - 01:23:07]

descriptions.

### [01:23:07 - 01:23:11]

So we can actually tell our robots like, hey, robot, can you please clean the kitchen instead

### [01:23:11 - 01:23:13]

of giving an image of, hey, robot, this is what my kitchen looks like.

### [01:23:13 - 01:23:14]

Right.

### [01:23:14 - 01:23:14]

Yeah.

### [01:23:14 - 01:23:21]

This is what my kitchen looks like when it's clean, which you may, you may not have access

### [01:23:21 - 01:23:22]

to.

### [01:23:22 - 01:23:23]

Right.

### [01:23:23 - 01:23:25]

Because it's not currently clean.

### [01:23:25 - 01:23:30]

And that does seem really interesting because it's much simpler to specify a language than

### [01:23:30 - 01:23:34]

to specify the image, at least for a person, but also like from like a representation perspective,

### [01:23:34 - 01:23:38]

you don't actually want to be going towards this image representation.

### [01:23:38 - 01:23:41]

I remember seeing a very interesting goal condition representation thing where it's

### [01:23:41 - 01:23:44]

like, yes, you know, it was like trying to move this block in this place.

### [01:23:44 - 01:23:47]

And it did move the block there, but it was like hovering it there.

### [01:23:47 - 01:23:50]

And like, you know, it just like really didn't do what it was supposed to do with like drop

### [01:23:50 - 01:23:51]

it there, please.

### [01:23:51 - 01:23:54]

So it is interesting to think about it might actually work better if I instead of removing

### [01:23:54 - 01:23:58]

some of the extra details that come from the image.

### [01:23:58 - 01:23:59]

Yeah.

### [01:23:59 - 01:24:00]

That's really cool.

### [01:24:00 - 01:24:01]

Yeah.

### [01:24:01 - 01:24:03]

I really, one thing that's nice about this is that it feels like it plugs in much more

### [01:24:03 - 01:24:08]

nicely into clips or like kind of taking components from clip versus the normal RL formulation.

### [01:24:08 - 01:24:09]

Yeah.

### [01:24:09 - 01:24:13]

I think very, very broadly, one of the reasons I've been excited about these goal condition

### [01:24:13 - 01:24:17]

problems is we can define them in terms of probabilities.

### [01:24:17 - 01:24:22]

And almost every other area of machine learning can also be defined in terms of probabilities.

### [01:24:22 - 01:24:24]

That's like another contrast in learning methods.

### [01:24:24 - 01:24:30]

Those are also, I guess, reasoning about the difference between two probability distributions.

### [01:24:30 - 01:24:35]

Methods for learning representations, things like VAEs, those are also learned reasoning

### [01:24:35 - 01:24:37]

about certain probabilities.

### [01:24:37 - 01:24:41]

In the first part of our chat today, we were talking about the skill learning methods and

### [01:24:41 - 01:24:42]

we were talking about communicating.

### [01:24:42 - 01:24:43]

Yeah.

### [01:24:43 - 01:24:45]

About communicating bits.

### [01:24:45 - 01:24:47]

And bits are just the logarithm of probabilities.

### [01:24:47 - 01:24:53]

And so I think that this idea of thinking about reinforcement learning as using probabilities

### [01:24:53 - 01:24:57]

actually gives us like a really cohesive way of connecting a lot of the dots.

### [01:24:57 - 01:25:02]

Thinking about reinforcement learning, it's not really the ugly duckling of supervised

### [01:25:02 - 01:25:04]

learning, unsupervised learning and reinforcement learning.

### [01:25:04 - 01:25:06]

They're all really, really closely intimately related.

### [01:25:06 - 01:25:07]

Yeah.

### [01:25:07 - 01:25:10]

And I think that thinking about these things in terms of probabilities, it gives

### [01:25:10 - 01:25:13]

us some really nice bridges that we can use to borrow ideas from one field.

### [01:25:13 - 01:25:14]

Yeah.

### [01:25:14 - 01:25:15]

And use them in other fields.

### [01:25:15 - 01:25:16]

Yeah.

### [01:25:16 - 01:25:17]

That's really interesting.

### [01:25:17 - 01:25:21]

If you were to ask other people to build on your research, what areas would you point

### [01:25:21 - 01:25:22]

them towards?

### [01:25:22 - 01:25:26]

For this contrasting learning in particular, I think that the exploration problem we mentioned

### [01:25:26 - 01:25:28]

before is a really interesting one.

### [01:25:28 - 01:25:29]

Yeah.

### [01:25:29 - 01:25:33]

I think that there's also sort of interesting open world extensions of this.

### [01:25:33 - 01:25:37]

When we've been looking at these goal-connecting problems, we assume a priori there's some

### [01:25:37 - 01:25:39]

set of goals that you want to reach.

### [01:25:39 - 01:25:43]

And when we're doing trial and error learning, in every trial we say, try to reach one of

### [01:25:43 - 01:25:45]

these 10 goals, one of these thousand goals.

### [01:25:45 - 01:25:49]

But if you think about doing this in a sort of open-ended learning, where you say, put

### [01:25:49 - 01:25:54]

a reinforcement learning in some environment and say, learn how to do everything.

### [01:25:54 - 01:25:57]

It's really hard because what is everything?

### [01:25:57 - 01:25:58]

What are the goals?

### [01:25:58 - 01:26:01]

Well, maybe you start doing stuff randomly and then you see what you've done so far.

### [01:26:01 - 01:26:06]

And then you say, okay, maybe these are the most interesting or the most distant goals

### [01:26:06 - 01:26:07]

that you've gotten to before.

### [01:26:07 - 01:26:09]

Let's try to replicate those.

### [01:26:09 - 01:26:10]

And repeating this process.

### [01:26:10 - 01:26:11]

I think they're interesting questions.

### [01:26:11 - 01:26:12]

Well, how could you create them?

### [01:26:12 - 01:26:14]

How could you create this curriculum?

### [01:26:14 - 01:26:16]

How could you specify these goals?

### [01:26:16 - 01:26:20]

But if you could do this and if you could actually learn how to solve all of the tasks,

### [01:26:20 - 01:26:25]

then this might give you not only a way of solving any goal-conditioned task, but also

### [01:26:25 - 01:26:29]

a really useful set of representations for solving any task or maximizing any reward

### [01:26:29 - 01:26:30]

function.

### [01:26:30 - 01:26:31]

Yeah.

### [01:26:31 - 01:26:32]

I really like that.

### [01:26:32 - 01:26:35]

That's one thing that I think I'd encourage people to work on.

### [01:26:35 - 01:26:40]

One other direction that I think is really promising is thinking about different ways

### [01:26:40 - 01:26:41]

of doing the contrasting.

### [01:26:42 - 01:26:48]

So this idea of using contrastive learning to solve reinforcement learning problems, it

### [01:26:48 - 01:26:52]

doesn't necessarily specify how you could do the contrastive learning.

### [01:26:52 - 01:26:57]

And there's been a huge amount of really interesting work in developing better and better contrastive

### [01:26:57 - 01:27:00]

learning algorithms over the last five years or so.

### [01:27:00 - 01:27:03]

And the contrastive learning algorithm that we're using, it dates back to something like

### [01:27:03 - 01:27:05]

2013.

### [01:27:05 - 01:27:10]

And there's been a decade of advances in contrastive learning, and we leveraged that into a decade

### [01:27:10 - 01:27:12]

of advances in reinforcement learning.

### [01:27:12 - 01:27:13]

Mm-hmm .

### [01:27:13 - 01:27:14]

Probably not.

### [01:27:14 - 01:27:17]

I don't think that all of these things are going to work.

### [01:27:17 - 01:27:22]

A lot of these advances have been tuned towards getting better visual representations or representations

### [01:27:22 - 01:27:24]

of language.

### [01:27:24 - 01:27:25]

But some of the tricks might work.

### [01:27:25 - 01:27:29]

I don't know which ones, but I think that this could be a fairly easy starting point

### [01:27:29 - 01:27:31]

for folks wanting to explore these sorts of ideas.

### [01:27:31 - 01:27:32]

That's really interesting.

### [01:27:32 - 01:27:37]

If we take MoCo v2 and turn that into a reinforcement learning algorithm, if we take

### [01:27:37 - 01:27:42]

SimClear and turn that into a reinforcement learning algorithm, our momentum buffers used

### [01:27:42 - 01:27:43]

to fall.

### [01:27:43 - 01:27:44]

All of these were some tricks.

### [01:27:44 - 01:27:45]

Mm-hmm .

### [01:27:45 - 01:27:49]

Kind of related to this, what do you think are some underrated approaches or papers

### [01:27:49 - 01:27:50]

or techniques?

### [01:27:50 - 01:27:57]

One high-level research technique that I think is underrated is thinking precisely

### [01:27:57 - 01:28:01]

about what the statistical problem is.

### [01:28:01 - 01:28:03]

What exactly do you want the inputs to be?

### [01:28:03 - 01:28:06]

What exactly do you want the outputs to be?

### [01:28:06 - 01:28:09]

In a lot of machine learning research, these are pretty obvious questions.

### [01:28:09 - 01:28:10]

Okay, we're doing image classification.

### [01:28:10 - 01:28:11]

Inputs are images.

### [01:28:11 - 01:28:12]

Outputs are images.

### [01:28:12 - 01:28:13]

Outputs are labels.

### [01:28:13 - 01:28:17]

But in a lot of other questions, a lot of other areas of machine learning, I think it's

### [01:28:17 - 01:28:18]

a lot less clear.

### [01:28:18 - 01:28:23]

So I think an interesting example is model-based reinforcement learning.

### [01:28:23 - 01:28:27]

So fundamentally, what are model-based methods?

### [01:28:27 - 01:28:30]

Often we think about them as methods that first learn a model and then use that model

### [01:28:30 - 01:28:34]

to generate some experience to do the reinforcement learning.

### [01:28:34 - 01:28:38]

But from 30,000 feet, they're methods that take as input data and then give you a policy

### [01:28:38 - 01:28:40]

based on that data.

### [01:28:40 - 01:28:41]

And from this perspective...

### [01:28:41 - 01:28:41]

Yeah.

### [01:28:41 - 01:28:46]

We see that one of the common arguments for using model-based methods, that they generate

### [01:28:46 - 01:28:51]

more data, just can't possibly be true because the data that they're being trained on is

### [01:28:51 - 01:28:56]

exactly the same data that model-free methods are being trained.

### [01:28:56 - 01:29:01]

And so I think in terms of research techniques, thinking about the inputs and the outputs,

### [01:29:01 - 01:29:05]

thinking about what the objective function is, what actually do you want to optimize?

### [01:29:05 - 01:29:07]

Can you directly optimize that?

### [01:29:07 - 01:29:09]

I think those are some underrated techniques.

### [01:29:09 - 01:29:11]

In terms of more technical techniques...

### [01:29:11 - 01:29:11]

Yeah.

### [01:29:11 - 01:29:17]

I think I'm biased in that I had some fantastic courses on probabilistic reasoning and graphical

### [01:29:17 - 01:29:21]

models and information theory in my undergrad, but I really like graphical models.

### [01:29:21 - 01:29:24]

I think they're a really useful language for describing what's happening.

### [01:29:24 - 01:29:30]

I think they're a really useful tool for figuring out how we solve important problems.

### [01:29:30 - 01:29:34]

And I think that I'd encourage people to study those more and think about, to what extent

### [01:29:34 - 01:29:37]

can those address the problems that we're seeing today?

### [01:29:37 - 01:29:40]

One of the problems that we're seeing, especially in reinforcement learning, is thinking about

### [01:29:40 - 01:29:41]

how to combine data sets.

### [01:29:41 - 01:29:46]

Because very often, there's no single data set that gives us all the information we want.

### [01:29:46 - 01:29:49]

Maybe there's one data set that gives us information about language.

### [01:29:49 - 01:29:54]

Maybe another one gives us information about, it's just videos, but it doesn't have questions.

### [01:29:54 - 01:29:56]

Maybe a third one gives us some information about actions.

### [01:29:56 - 01:30:00]

Maybe another one gives us some information about human demonstrations.

### [01:30:00 - 01:30:03]

It's graphical models exactly tell us how to string together these different data sets

### [01:30:03 - 01:30:06]

and how to do it in a provably correct way.

### [01:30:06 - 01:30:11]

And so while I don't expect everyone to be right, I don't expect Next, NeurIPS to have

### [01:30:11 - 01:30:11]

a whole bunch of images.

### [01:30:11 - 01:30:18]

I think as a way of thinking, as a mental model, it's a really powerful technique.

### [01:30:18 - 01:30:22]

Are there any unpublished research failures that you've had or things that you try and

### [01:30:22 - 01:30:26]

you're like, this should definitely work, and it just didn't work at all?

### [01:30:26 - 01:30:31]

We spent some time trying to scale up various skill learning methods.

### [01:30:31 - 01:30:32]

Here's the vision.

### [01:30:32 - 01:30:36]

After we worked on that diversity is all you need paper, the one where it's Alice and Bob

### [01:30:36 - 01:30:40]

and we were learning the skills, we wanted to see how far we could take.

### [01:30:40 - 01:30:41]

The vision was that.

### [01:30:41 - 01:30:46]

We needed some environment to automatically learn every possible skill.

### [01:30:46 - 01:30:48]

And we were never able to get there.

### [01:30:48 - 01:30:53]

It seems like there's something fundamentally hard about optimizing that.

### [01:30:53 - 01:30:56]

Some prior work has looked at better ways of doing the optimization.

### [01:30:56 - 01:31:01]

It seems like it's largely an exploration problem, but there are various techniques

### [01:31:01 - 01:31:03]

that we explore to try to improve that.

### [01:31:03 - 01:31:10]

Various ways of relabeling the data, different ways of having Bob guess what skill is being

### [01:31:10 - 01:31:11]

executed.

### [01:31:11 - 01:31:13]

It seems to work out too well.

### [01:31:13 - 01:31:14]

I think it's pretty close.

### [01:31:14 - 01:31:17]

I think it should be possible to massively scale these methods.

### [01:31:17 - 01:31:20]

Maybe it's just a problem of throwing transformers at the problem.

### [01:31:20 - 01:31:21]

I don't know.

### [01:31:21 - 01:31:24]

We aren't there quite yet, but, but if we could get there, I think it'd be really, really

### [01:31:24 - 01:31:25]

cool.

### [01:31:25 - 01:31:27]

We can imagine that.

### [01:31:27 - 01:31:31]

So now when you want to solve some computer vision problem, often what people do is you

### [01:31:31 - 01:31:35]

take whatever the best image that yours are dual linear regression on them, or fit a small

### [01:31:35 - 01:31:38]

neural network on them or pretty well.

### [01:31:38 - 01:31:40]

But for reinforcement learning, we don't really have anything.

### [01:31:40 - 01:31:41]

Hmm.

### [01:31:41 - 01:31:46]

If you take a task and you want to solve it, you can try to run an off the shelf RL method,

### [01:31:46 - 01:31:48]

but typically it doesn't work very well.

### [01:31:48 - 01:31:53]

But if you could have these skills, then maybe that would be equivalent or similar to these

### [01:31:53 - 01:31:58]

image net, these pre-trained image net where to solve some tasks, just search over a small

### [01:31:58 - 01:32:03]

number of skills, do some black box optimization or manually sweep.

### [01:32:03 - 01:32:08]

So the vision is that we could release every reinforcement learning environment together

### [01:32:08 - 01:32:11]

with this rich library of skills.

### [01:32:11 - 01:32:13]

That's really interesting.

### [01:32:13 - 01:32:14]

Skills as pre-trained network.

### [01:32:14 - 01:32:15]

Yeah.

### [01:32:15 - 01:32:21]

Do you feel like you have any unusual or controversial opinions on research topics that other people

### [01:32:21 - 01:32:23]

don't seem to agree with?

### [01:32:23 - 01:32:25]

Not directly related to research.

### [01:32:25 - 01:32:31]

I think there's a really interesting question in the PhD process about what the role of

### [01:32:31 - 01:32:33]

PhD students is.

### [01:32:33 - 01:32:38]

When I started my PhD, my understanding was the role of a PhD is to, is to do research,

### [01:32:38 - 01:32:40]

to develop the next state of the art method.

### [01:32:40 - 01:32:42]

It's to make society better.

### [01:32:42 - 01:32:45]

But over time, I've realized that it's actually a combination of a couple of things.

### [01:32:45 - 01:32:46]

It's not just doing research.

### [01:32:46 - 01:32:51]

There's also learning how to do research, learning how to communicate.

### [01:32:51 - 01:32:56]

And this makes me think about how we should design conferences and workshops that are

### [01:32:56 - 01:33:02]

aims not just at furthering the science, but also at education, at teaching people how

### [01:33:02 - 01:33:04]

to communicate, how to write.

### [01:33:04 - 01:33:08]

I think that certain ways that conferences are organized today, like having pretty low

### [01:33:08 - 01:33:10]

acceptance rates.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:10]

Yeah.

### [01:33:10 - 01:33:15]

I think this might be bad from an educational perspective, because it encourages people

### [01:33:15 - 01:33:20]

to just keep resubmitting the same paper over and over, or those are sort of the backlog

### [01:33:20 - 01:33:21]

of papers.

### [01:33:22 - 01:33:27]

And maybe there are different ways of designing conferences so they can provide more opportunities

### [01:33:27 - 01:33:30]

for people to practice communicating, or for like, in particular, for students to practice

### [01:33:30 - 01:33:35]

communicating and learning how to do the research without having the sort of unrealistic expectation

### [01:33:35 - 01:33:38]

that every student project is going to change the world.

### [01:33:38 - 01:33:40]

That's interesting.

### [01:33:40 - 01:33:42]

That's interesting.

### [01:33:42 - 01:33:46]

Also thinking about the other part of that, it's like, people are sort of supposed to

### [01:33:46 - 01:33:48]

be in their PhD pushing things forward.

### [01:33:48 - 01:33:51]

And then they're also supposed to be learning it at the same time.

### [01:33:51 - 01:33:54]

Shouldn't we have like a space afterwards for people to actually push things forward?

### [01:33:54 - 01:33:57]

Like now that they've learned how to do, like when would that part happen?

### [01:33:57 - 01:33:58]

Yeah.

### [01:33:58 - 01:33:59]

I don't know.

### [01:33:59 - 01:34:00]

I don't know.

### [01:34:00 - 01:34:01]

Like, is that what postdocs are supposed to do?

### [01:34:01 - 01:34:03]

Is that what industry is like?

### [01:34:03 - 01:34:04]

It's really interesting.

### [01:34:04 - 01:34:07]

What about any controversial opinions about the field?

### [01:34:07 - 01:34:10]

I was really excited to see this dataset.

### [01:34:10 - 01:34:13]

and benchmark track at Nurex this past year.

### [01:34:13 - 01:34:18]

I think that it was really useful forcing fucking to make people think about what are

### [01:34:18 - 01:34:20]

the applications of our methods?

### [01:34:20 - 01:34:23]

We don't actually need to get better performance on Atari.

### [01:34:23 - 01:34:24]

We've already beaten humans.

### [01:34:24 - 01:34:28]

Can we go on and solve some more interesting problems?

### [01:34:28 - 01:34:33]

And so I think that I don't know how controversial it is, but I would like to see more effort

### [01:34:33 - 01:34:40]

on taking even existing methods and applying them to new tasks, to real problems.

### [01:34:40 - 01:34:44]

I think part of this will require a shift in how we evaluate papers, evaluating them

### [01:34:44 - 01:34:49]

not so much on algorithmic novelty rather than on, did you actually solve an interesting

### [01:34:49 - 01:34:50]

problem?

### [01:34:50 - 01:34:52]

I myself am not immune to this.

### [01:34:52 - 01:34:56]

I definitely have probably read too many algorithms papers and perhaps shouldn't spend more time

### [01:34:56 - 01:34:57]

working on applications.

### [01:34:57 - 01:35:01]

But it's something I very much intend to do as a faculty member.

### [01:35:01 - 01:35:02]

Interesting.

### [01:35:02 - 01:35:03]

Yeah.

### [01:35:03 - 01:35:04]

We definitely resonate with that.

### [01:35:04 - 01:35:07]

Our paper at Nurex was a dataset paper, benchmark paper.

### [01:35:07 - 01:35:08]

So yeah.

### [01:35:08 - 01:35:09]

Interesting.

### [01:35:09 - 01:35:13]

And I also do think it would be very interesting to start shifting a lot of attention more

### [01:35:13 - 01:35:14]

towards application.

### [01:35:14 - 01:35:21]

I don't know if we need yet another totally tiny incremental change on PPO or something.

### [01:35:21 - 01:35:23]

Like we've got lots of those.

### [01:35:23 - 01:35:24]

It's okay.

### [01:35:24 - 01:35:25]

They're great.

### [01:35:25 - 01:35:27]

But we could have other applications too.

### [01:35:27 - 01:35:28]

Interesting.

### [01:35:28 - 01:35:29]

Yeah.

### [01:35:29 - 01:35:33]

What is an opinion you once held strongly, but now decided to reverse it?

### [01:35:33 - 01:35:37]

How useful robotics will be for furthering reinforcement on your research.

### [01:35:37 - 01:35:38]

Interesting.

### [01:35:38 - 01:35:39]

That's controversial.

### [01:35:39 - 01:35:40]

Yeah.

### [01:35:40 - 01:35:41]

That's more spiky.

### [01:35:41 - 01:35:44]

Robotics is really hard.

### [01:35:44 - 01:35:50]

I think the reason it's hard is not so much to do with our decision-making algorithms,

### [01:35:50 - 01:35:52]

but with a lot of the problems below that.

### [01:35:52 - 01:35:56]

Problems about how do you make robots that just break less frequently?

### [01:35:56 - 01:36:00]

How do you design workspaces that need recess less often?

### [01:36:00 - 01:36:03]

How do we design things that drift less often?

### [01:36:03 - 01:36:08]

If you look at especially relatively inexpensive robots, you'll see that they shake a lot.

### [01:36:08 - 01:36:12]

The amount that they shake that varies across time, depending on how weak the parts are,

### [01:36:12 - 01:36:14]

depending on how hot it is in the room.

### [01:36:14 - 01:36:17]

And so I think there's a lot of really hard hardware questions.

### [01:36:17 - 01:36:23]

I think that for robotics, especially when we're learning in the real world, we're always

### [01:36:23 - 01:36:25]

going to collect data at one Hertz.

### [01:36:25 - 01:36:29]

I think there are a lot of other problems where we might be collecting data at one Hertz,

### [01:36:29 - 01:36:34]

but there's much, much more data coming through in that amount of time.

### [01:36:34 - 01:36:36]

Problems about say controlling traffic.

### [01:36:36 - 01:36:37]

Exactly.

### [01:36:37 - 01:36:40]

I know off the back of my hand how many traffic lights there are in New York City, but I do

### [01:36:40 - 01:36:44]

know that there's a command center where there are dozens of people sticking to the road,

### [01:36:44 - 01:36:48]

looking at dozens and dozens of monitors, trying to figure out how to be getting traffic

### [01:36:48 - 01:36:51]

lights to maximize throughput through New York City.

### [01:36:51 - 01:36:54]

And I think that's the sort of problem where we might be able to collect a huge amount

### [01:36:54 - 01:36:57]

more data, especially if you combine data across major cities.

### [01:36:57 - 01:36:58]

Yeah, that's true.

### [01:36:58 - 01:37:01]

I think there are also interesting applications

### [01:37:01 - 01:37:06]

in the physical sciences too, where we might be able to collect data more cheaply and more

### [01:37:06 - 01:37:07]

quickly.

### [01:37:07 - 01:37:13]

There's been a lot of work on reinforcement learning for healthcare, but a human life

### [01:37:13 - 01:37:14]

cycle is really, really long.

### [01:37:14 - 01:37:18]

To measure the impact of certain treatments, you might need to wait months or years.

### [01:37:18 - 01:37:24]

If we instead look at problems of say controlling or tuning bacteria populations, their life

### [01:37:24 - 01:37:27]

cycle is way, way, way, way, way faster, orders of magnitude faster.

### [01:37:27 - 01:37:32]

If you looked at controlling chemical reactions, figuring out what sequence of reactions can

### [01:37:32 - 01:37:36]

be performed to get some new desired chemical molecule, it's again a reinforcement learning

### [01:37:36 - 01:37:37]

problem.

### [01:37:37 - 01:37:41]

But one that we can perhaps scale up much, much more quickly and perhaps doesn't have

### [01:37:41 - 01:37:44]

the sort of robustness challenges of robotics.

### [01:37:44 - 01:37:49]

That's not to say that we shouldn't work on robotics, just to say that I'm not convinced

### [01:37:49 - 01:37:54]

that's where we're going to see the most reinforced learning methods deployed first over the next

### [01:37:54 - 01:37:56]

decade or so.

### [01:37:56 - 01:37:56]

Exactly.

### [01:37:56 - 01:37:58]

Yeah.

### [01:37:58 - 01:38:02]

Speaking of the next decade or so, what are you sort of excited about and also kind

### [01:38:02 - 01:38:06]

of worried about, or I think it's worth kind of taking some time to think about how we

### [01:38:06 - 01:38:09]

mitigate, what are some of the most important risks as well?

### [01:38:09 - 01:38:13]

The past decade, I think it was super exciting for supervised learning.

### [01:38:13 - 01:38:18]

I think it's really gotten to where most people with a little bit of coding knowledge can

### [01:38:18 - 01:38:23]

take any model from GitHub, run on their computer and get a supervised learning model that works

### [01:38:23 - 01:38:27]

pretty well, pretty high accuracy, pretty reliably.

### [01:38:27 - 01:38:30]

So I think that we're on the brink of getting reinforcement learning tools that can do what

### [01:38:30 - 01:38:34]

supervised learning tools can do today in terms of being tools that any person can use

### [01:38:34 - 01:38:36]

to solve any problem.

### [01:38:36 - 01:38:37]

Fairly reliably and fairly robustly.

### [01:38:37 - 01:38:40]

What do you think are the main advances needed

### [01:38:40 - 01:38:41]

to get there?

### [01:38:41 - 01:38:43]

I think one is the key about how we define the problems.

### [01:38:43 - 01:38:48]

I think that we can't expect users to know how to write dozens of lines of code to define

### [01:38:48 - 01:38:49]

reward functions.

### [01:38:49 - 01:38:53]

I think we can't expect users to know how to craft state representations to be able

### [01:38:53 - 01:38:58]

to apply methods that only work on low dimensional states.

### [01:38:58 - 01:39:03]

I think that this idea of having just three time steps, maybe that's not the right thing

### [01:39:03 - 01:39:04]

to do.

### [01:39:04 - 01:39:05]

Hmm.

### [01:39:05 - 01:39:08]

What are alternatives to having discrete time steps?

### [01:39:08 - 01:39:12]

One way of thinking about reinforcement learning is there's a problem of maximizing some integral

### [01:39:12 - 01:39:14]

of rewards.

### [01:39:14 - 01:39:19]

And there are lots of problems where we want to break them up into different size chunks

### [01:39:19 - 01:39:21]

and different parts of the task.

### [01:39:21 - 01:39:26]

You can imagine that for, say, Joshua, a previous example of driving to a grocery store and

### [01:39:26 - 01:39:28]

go grocery shopping.

### [01:39:28 - 01:39:31]

For driving, you don't need to pay that much attention, you're probably going straight

### [01:39:31 - 01:39:32]

on most of the roads.

### [01:39:32 - 01:39:34]

But maybe for parking in a parking lot, that requires a lot more attention.

### [01:39:34 - 01:39:35]

Yeah.

### [01:39:35 - 01:39:41]

As you can imagine, as chunking that up so that the drive-straight action you can execute

### [01:39:41 - 01:39:47]

for minutes at a time, but the parallel parking, the accuracy for that, you need to replan on

### [01:39:47 - 01:39:50]

the word of hundreds of milliseconds.

### [01:39:50 - 01:39:52]

And then, you know, the second part of the other question as well, like things you're

### [01:39:52 - 01:39:56]

excited about, also things you're sort of worried about or thinking about or risks that

### [01:39:56 - 01:40:01]

we should be thinking about now before they become a super important issue.

### [01:40:01 - 01:40:02]

Yeah.

### [01:40:02 - 01:40:03]

LARP language models.

### [01:40:03 - 01:40:04]

I think you've really, really learned a lot.

### [01:40:04 - 01:40:07]

I think you've really, really amazing results.

### [01:40:07 - 01:40:09]

They also can be wrong and confidently wrong.

### [01:40:09 - 01:40:15]

They also can tell you how to solve decision-making problems in ways that fool users into thinking

### [01:40:15 - 01:40:18]

that they know how to solve decision-making problems.

### [01:40:18 - 01:40:21]

These models, they're trained to mimic data.

### [01:40:21 - 01:40:23]

They aren't trained to achieve good outcomes.

### [01:40:23 - 01:40:28]

A couple of days ago, there were some headlines about a mental health company using these

### [01:40:28 - 01:40:30]

large language models to treat patients.

### [01:40:30 - 01:40:34]

And that it's really bad for ethical reasons is also bad because we know who these models

### [01:40:34 - 01:40:35]

are trained.

### [01:40:35 - 01:40:36]

They're trained on the internet.

### [01:40:36 - 01:40:40]

They're not trained to make patients better over the long term.

### [01:40:40 - 01:40:44]

And so I think that these aren't not tools that we could get rid of, but these large

### [01:40:44 - 01:40:50]

language models are, is worth seriously thinking about what capabilities they actually have,

### [01:40:50 - 01:40:53]

what objectives they're actually optimized for, and how can we shift those so that they

### [01:40:53 - 01:40:56]

do solve tasks that we care about.

### [01:40:56 - 01:40:57]

Yeah.

### [01:40:57 - 01:41:00]

Predict the next token is not necessarily the objective you want when treating mental

### [01:41:00 - 01:41:01]

health patients.

### [01:41:01 - 01:41:02]

Precisely.

### [01:41:02 - 01:41:03]

Yeah.

### [01:41:03 - 01:41:08]

I guess maybe one question kind of related to that is think about, since, you know, you're

### [01:41:08 - 01:41:11]

thinking of going into academia, I think, right?

### [01:41:11 - 01:41:14]

So how do you think about that and how it relates to large language models?

### [01:41:14 - 01:41:18]

Like, will you really be able to do this type of research and like, you know, use these

### [01:41:18 - 01:41:23]

models as part of your models as a academic where you don't necessarily have the same

### [01:41:23 - 01:41:24]

resource in the self-industry position?

### [01:41:24 - 01:41:29]

Yeah, I think it's a really valid concern and I don't know what the right answer

### [01:41:29 - 01:41:30]

is going to be.

### [01:41:30 - 01:41:33]

I think that a lot of the most important questions are not questions of how do you better

### [01:41:33 - 01:41:37]

train these models, but rather questions of how do you better use these models?

### [01:41:37 - 01:41:43]

And so I think that it's likely that an academia will still be able to use these models.

### [01:41:43 - 01:41:48]

I think that even if they're currently too big to fit on commercial GPUs, people will

### [01:41:48 - 01:41:50]

find tricks for compressing them down.

### [01:41:50 - 01:41:57]

I think a really interesting example of this is in the image generative modeling community.

### [01:41:57 - 01:42:02]

Some of the initial large generative models, things like BigGAN, things like ImageN, these

### [01:42:02 - 01:42:03]

are models.

### [01:42:03 - 01:42:08]

They're arguably too big for most academic research, but then stable diffusion came along

### [01:42:08 - 01:42:12]

and now that's something that anyone can run pretty cheaply.

### [01:42:12 - 01:42:16]

And my hope is that we'll see similar advances and getting these large models down to sizes

### [01:42:16 - 01:42:21]

that at least parts of them can be tuned and tweaked and studied on in academic settings.

### [01:42:21 - 01:42:23]

I hope so too.

### [01:42:23 - 01:42:26]

And I think we will see that, although it is, you know, it is a little bit different

### [01:42:26 - 01:42:30]

at the size of the original stable diffusion type models was a little bit smaller than

### [01:42:30 - 01:42:32]

say the language model, but we're trying to compress.

### [01:42:32 - 01:42:36]

We still have a little ways to go, but I am hopeful also that, you know, we'll be able

### [01:42:36 - 01:42:38]

to keep making progress on those.

### [01:42:38 - 01:42:39]

Yeah.

### [01:42:39 - 01:42:40]

Yeah.

### [01:42:40 - 01:42:41]

Maybe that we just need to organize academic labs differently.

### [01:42:41 - 01:42:46]

So instead of having each individual student running their own language model, maybe just

### [01:42:46 - 01:42:51]

have some hosted language model for the entire school and then do your research on what's

### [01:42:51 - 01:42:54]

working with the mainframe architectures.

### [01:42:54 - 01:42:58]

In terms of getting reinforcement learning to an interesting place or getting language

### [01:42:58 - 01:43:00]

models to be actually aiming for useful objectives.

### [01:43:00 - 01:43:01]

Are there any areas where you're looking at?

### [01:43:01 - 01:43:02]

Yeah.

### [01:43:02 - 01:43:05]

Are there any areas where you feel hopeful for kind of the combination of the two techniques

### [01:43:05 - 01:43:10]

aside from RLHF or any bottlenecks that you see?

### [01:43:10 - 01:43:14]

Yeah, I think that the reinforcement learning with from human feedback, I think is a really

### [01:43:14 - 01:43:15]

interesting direction.

### [01:43:15 - 01:43:21]

I think that part of the power of it is that once we have language models that are widely

### [01:43:21 - 01:43:26]

deployed, we can start collecting this feedback at really, really large scales.

### [01:43:26 - 01:43:30]

And reinforcement learning is the tool that we have to learn from sparse feedback.

### [01:43:30 - 01:43:31]

We're likewise.

### [01:43:31 - 01:43:32]

Are there likely?

### [01:43:32 - 01:43:33]

Yeah.

### [01:43:33 - 01:43:35]

I think that's a really interesting algorithmic questions of how do we better reason over

### [01:43:35 - 01:43:37]

the long horizons?

### [01:43:37 - 01:43:39]

So before we were talking about, well, how do you solve tasks on the internet?

### [01:43:39 - 01:43:43]

Like how do you book a flight or how do you order groceries or something like that?

### [01:43:43 - 01:43:48]

And those tasks require many, many steps, but that's the sort of tasks that reinforcement

### [01:43:48 - 01:43:50]

learning methods historically have been good at.

### [01:43:50 - 01:43:54]

I think one of the reasons why I'm particularly excited about these problems is that these

### [01:43:54 - 01:43:59]

language models, they're trained to maximize the likelihood of the next token.

### [01:43:59 - 01:44:01]

And that draws a really strong connection to this way of training.

### [01:44:01 - 01:44:02]

Yeah.

### [01:44:02 - 01:44:06]

It's a way of treating reinforcement learning problems as predicting probabilities and as

### [01:44:06 - 01:44:07]

maximizing probabilities.

### [01:44:07 - 01:44:11]

And so I think that these tools are actually much, much more similar than they might seem

### [01:44:11 - 01:44:12]

on the surface.

### [01:44:12 - 01:44:15]

And that might give us some clues on how to best combine them.

### [01:44:15 - 01:44:16]

Yeah.

### [01:44:16 - 01:44:17]

That makes sense.

### [01:44:17 - 01:44:19]

Do you hope to work on that next?

### [01:44:19 - 01:44:20]

Maybe.

### [01:44:20 - 01:44:23]

What do you think makes a great researcher great?

### [01:44:23 - 01:44:26]

I think curiosity is really, really important.

### [01:44:26 - 01:44:27]

Persistence is important.

### [01:44:27 - 01:44:31]

Periodies are long and important to have students that can keep trying things even after a long

### [01:44:31 - 01:44:32]

time.

### [01:44:32 - 01:44:37]

I think a lot of things have failed, but ultimately I think we end up learning much more from our

### [01:44:37 - 01:44:40]

failed experiments than from the successful ones.

### [01:44:40 - 01:44:44]

And so working with students that have been really curious has been really, really fun

### [01:44:44 - 01:44:47]

for me because you learn so much.

### [01:44:47 - 01:44:50]

They say they're looking at something and saying, oh, this didn't work, but I noticed

### [01:44:50 - 01:44:53]

this thing seems weird.

### [01:44:53 - 01:44:58]

And I don't know if it's possible to get better at being curious, but at least knowing that

### [01:44:58 - 01:45:02]

it is valued, knowing that your advisor probably values students being curious.

### [01:45:02 - 01:45:05]

I think it might help bring more of it to the fore.

### [01:45:05 - 01:45:06]

That's awesome.

### [01:45:06 - 01:45:10]

Are there any collaborators or people that you'd like to work with or things that

### [01:45:10 - 01:45:15]

you can like broadcast out as like a, hey, reach out to me about X?

### [01:45:15 - 01:45:20]

If you work in chemical synthesis or bioengineering, definitely reach out.

### [01:45:20 - 01:45:24]

There are two applications where I think there are a lot of interesting combinations of reinforcement

### [01:45:24 - 01:45:25]

learning, interesting science applications.

### [01:45:25 - 01:45:26]

Awesome.

### [01:45:26 - 01:45:28]

We'll make sure to include them.

### [01:45:28 - 01:45:30]

Well, thank you so much, Ben.

### [01:45:30 - 01:45:31]

This is really fun.

### [01:45:31 - 01:45:32]

I feel like I learned a ton at least.

### [01:45:32 - 01:45:33]

Yeah, this is great.

### [01:45:33 - 01:45:34]

Yeah.

### [01:45:34 - 01:45:35]

This is really fun for me too.

### [01:45:35 - 01:45:39]

Thanks for listening to the Generally Intelligent Podcast.

### [01:45:39 - 01:45:44]

If you like this, please consider giving us a rating and leaving a review on Apple Podcast.

### [01:45:44 - 01:45:49]

On Twitter, I'm at Kanjun, K-A-N-J-U-N, and our lab is at GenIntelligent.

### [01:45:49 - 01:45:49]

Until next time.
