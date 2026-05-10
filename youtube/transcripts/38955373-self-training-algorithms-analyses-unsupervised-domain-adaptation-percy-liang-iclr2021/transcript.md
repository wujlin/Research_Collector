# Self-training Algorithms and Analyses for Unsupervised Domain Adaptation

- URL: https://slideslive.com/38955373/selftraining-algorithms-and-analyses-for-unsupervised-domain-adaptation
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Refined at: `2026-05-08T15:42:40`

## Transcript

### [00:00 - 00:29]

Hello, everyone. Today, I'm going to be talking about a recent work on unsupervised domain adaptation using self-training, which is a really simple and age-old tool in machine learning. This is joint work with Michael Xie, Ananya Kumar, Robbie Jones, Fereshte Khani, and Tengyu Ma. So let me begin with a motivating example from remote sensing.

### [00:29 - 00:56]

So an example task that you might want to be solving is to give it a satellite image, predict its land cover type. Is this crops? Is it grass? Is it a forest? And solving such a problem could be useful for forecasting crop yields or assessing a nation's food security and so on. So collecting data for this problem can be difficult, especially if it's labeled data.

### [00:56 - 01:00]

And often, you can collect data, maybe in only some parts of the world.

### [01:01 - 01:25]

So if you were to train a model on only the parts of the world, which are in dark green here, and test it on the same countries, you would get 76% accuracy on this task. But if you were to take the same model and you apply it out of distribution to Africa here, your accuracy plummets to only 58%, which is not great. On the other hand, if you're doing this,

### [01:26 - 01:39]

this is a case where we have satellites, which are collecting images from all corners of the world, so we have a lot of unlabeled data. How can we use this unlabeled data? So this is a very good example of the classical problem of unsupervised domain adaptation.

### [01:40 - 01:53]

We're given labeled examples from a source domain, and we want to train and unlabeled examples from a target domain, and we want to use these, the combination of these two somehow to produce a model that works well in both the source and the target domains.

### [01:55 - 02:16]

So there's a lot of data. There's been a long line of work on unsupervised domain adaptation. So some of the earliest work used this idea of importance weighting, where the idea is you use the unlabeled data from your target domain to identify regions where there's more target than source, and you use that to upweight the examples in your source so that the model will pay more attention.

### [02:17 - 02:30]

But this only works if you have examples in those areas. So this is often a very restrictive example, and you can't really extrapolate to target domains, which are outside of your source domain.

### [02:32 - 02:54]

And since the rise of deep learning, there's been a lot of interest in representation learning methods for unsupervised domain adaptation. There's many, many methods here, including adversarial learning and feature matching. Roughly, these methods try to map inputs in a source domain into a representation and inputs in a target domain into some representation so that the distribution

### [02:55 - 03:25]

of the induced distributions of the representations in the source matches that of the target. So while this has been really effective in practice, why it works and when it does work is unclear. You have no, you're matching only the marginal distributions of the inputs because you don't actually have alignments between the instances, which means you could technically map all the positive examples,

### [03:25 - 03:32]

you could technically map all the positive examples, you could technically map all the positive examples, in the source to the same place in lane space as all the negative examples in target, which would be catastrophic.

### [03:34 - 03:59]

More state-of-the-art methods for unsupervised domain adaptation actually combine many different ideas, which I won't get into here. In this talk, we're gonna try to focus on simplicity, and I'm only gonna talk about one particular idea, self-training, and show that it can be used to leverage a bunch of different types of structures that happen organically in domain shift problems.

### [04:00 - 04:25]

So we're gonna consider two types of structures. The first one is the presence of auxiliary information. So back to this crop cover, you know, land cover prediction problem, we have inputs, which are satellite images, but we know the location of these images, so we can actually get the weather or climate information at each of these locations. So that's a form of auxiliary.

### [04:25 - 04:36]

That's auxiliary information, which may be useful. And we'll show later that we can use this information as an auxiliary task output to learn better representations.

### [04:37 - 05:00]

So in the second type of structure we're gonna consider is a gradual shift. So in this case, we have our source and target domains, but we also have a sequence of intermediate domains between the source and the target, which vary gradually. So this is interesting because the source and the target domains are very far apart, but each adjacent set of domains is actually very close,

### [05:00 - 05:15]

which means adaptation between each individual, between consecutive domains is quite easy. And we're gonna assume we only have labels from the source domain and unlabeled data for all the other domains.

### [05:16 - 05:46]

So let's begin with setting one, which is when we have auxiliary information. So this is a work, which actually appeared at this iClear. It's called in and out pre-training and self-training using auxiliary information for out of distribution robustness. This is with Michael, Ananya, Robby, Freshday, Tenryu. And the setup is as follows. So we have the same problem as before. Given an input we want to predict,

### [05:46 - 06:12]

which is satellite image, we wanna predict the output, which is a label. And for each data point, we also have a variable z, which is the auxiliary information. So I think it's a vector, which can include things like timestamps, weather data, and other kind of signals. So in distribution, we're gonna assume we have these tuples of X, Y, and Zs. We have everything in distribution.

### [06:12 - 06:39]

And for both in distribution and out of distribution, we have many, many unlabeled pairs, X and Z, which are easy to collect, but we don't have Y. So the question is, how can we use this unlabeled data, which has auxiliary information, to improve both in-domain and out-of-domain accuracy? And in particular, we're gonna focus on how this auxiliary information is going to enter into the equation.

### [06:40 - 07:05]

So here's a natural thing you might do. And we call it aux inputs because we're going to use the auxiliary variable z here as input features. So we're going to just concatenate the input and auxiliary information, just feeding it in, feed them into the model, and predict the output. So this is a very natural thing to do. How well does it work? On two datasets, cropland and lambcover,

### [07:05 - 07:34]

we show that in-domain, it works a bit better. And this is nice because we're adding additional features which provide extra sources of information, so there's improved accuracy. What happens in out-of-domain? Out-of-domain, we actually find that adding these auxiliary information variables as inputs, actually hurts the accuracy. So this is not good. So what else can we do? So another thing we can do is we can use

### [07:34 - 07:59]

the auxiliary information as targets for pre-training. So intuitively, what we're gonna do is we're going to pre-train a model that takes the input satellite image and predicts this auxiliary information. And intuitively, you can think about the pre-train models learning more high-level representations like the presence of trees, and water, and so on, to be able to predict the climate information.

### [07:59 - 08:17]

And then we're gonna initialize this pre-train model, and model with this pre-train model, and then we're gonna fine-tune on our labeled examples. Now, so now notice that the fine-tuned model is not using the auxiliary information z, it's just mapping x to y.

### [08:19 - 08:50]

So how well does this work? We show that out-of-domain, this actually improves things. And the idea here is that the z, the auxiliary information, is not, suffers from a domain shift, which means that using a misinput is harmful, but we can actually use a misoutput to learn better representations, and this works. But unfortunately, in-domain, it turns out not to work very well.

### [08:51 - 09:14]

So now the question, a natural question is, how can you get the best results? How can you get the best of both worlds? So the immediate thing that might come to mind is, well, why don't you use them as both inputs and outputs? Okay, so we're gonna pre-train a model where we feed x into this input and ask it, sorry, feed x and z as input and ask it to produce z. And you can see immediately this is not gonna work

### [09:14 - 09:42]

because the model is just going to learn the identity from z to z and ignore x. So we have to do something a little bit smarter. So what we came up with, in this paper, is in and out. And that's gonna capture the best of both worlds. So intuitively, aux inputs, remember, using z as input, gets good in-domain accuracy. And aux outputs gets good out-of-main accuracy. And here's where self-training comes in.

### [09:42 - 10:11]

Self-training is gonna provide this glue that's gonna transfer the good in-domain accuracy of aux inputs into aux outputs. So here's the procedure. It's quite simple. So we're first gonna train an aux inputs model. And then we're gonna use it to pseudo-label our unlabeled in-domain data. Okay, so remember the unlabeled in-domain data consists of x, y, x, z pairs. We don't have y.

### [10:11 - 10:25]

We're just gonna use the aux-in model to produce some y's. Next, we're gonna take the aux-out model from before, which was, remember, pre-trained on using a z as output.

### [10:27 - 10:50]

And we're gonna initialize this model. And finally, we're gonna fine-tune this model on not just the original labels, but also on the pseudo-labels that we got from the aux-in model. And this is the key part. Self-training allows us to transfer some of this modeling predictive power from the aux-in model to the in-and-out model. So therefore, in-and-out model is somehow able

### [10:50 - 11:06]

to leverage both the aux-out and the aux-in model. So how well does it work? Across the board, in-and-out improves the accuracy over all of the different baselines on both the cropland, landcover datasets, as well as syllabic.

### [11:09 - 11:40]

So let's explore the question of why in-and-out works. And we don't have a full picture of everything that in-and-out is doing in the realistic setting with deep neural networks, so we constructed, we constructed a simple multitask linear regression setting to explore this question further. So here's the setup. We're gonna have inputs X and targets Y, as usual. But the true distribution is going to be,

### [11:40 - 12:08]

you take the inputs, which are D-dimensional, and map them, project them down into some low-dimensional subsets, which is K-dimensional, that's W. And then there's going to be this latent noise, U. Which is going to both influence the output, as well as this auxiliary information. So you can think about these two latent variables as governing both the output that you care about and this auxiliary variable.

### [12:08 - 12:42]

And the key thing is that U is going to shift between the source and the target domains. And you can see kind of immediately that if U is shifting, that means that Z is shifting quite a bit, which means that Z as an input is not going to be reliable out of domain. So let's see what happens with aux inputs. So we're going to use Z as an input to predict Y. And intuitively, we can show that Z is giving you

### [12:43 - 13:08]

information, allowing you to recover U. And U is clearly relevant for predicting Y. So you can prove that if you have enough samples, aux inputs improves in-domain accuracy. What happens out of domain? Well, as we mentioned before, U is going, the distribution of U shifts out of domain, which means that Z is no longer a robust indicator of U.

### [13:12 - 13:27]

And we proved that aux inputs always can hurt for some out-of-domain shift. So it's not, it can also help sometimes, but you can, you know, it can also help sometimes, but you can, you know, it can also help sometimes, but you can, you know, it can also help sometimes, but you can, you know, it can also help sometimes, but you can, you know, always find a case where it hurts. What about aux outputs?

### [13:27 - 13:51]

So what's going on here is that pre-training, where you're trying to predict Z from X, is going to help you nail down this latent feature, or at least the kind of subspace, and reduces it essentially to a prediction problem from W to Y. And because of this, the standard kind of balance show that instead of having a D of X, it's going to be a D of X.

### [13:51 - 14:13]

And because of this, the standard kind of balance show that instead of having a D of X, it's going to be a D of X, and if you have a D dimensional dependence, the SS risk scaling is D, now it still scales with K. So that's in domain. So out of domain is actually a little bit trickier because the SS risk actually depends on the covariance of X and W. So in domain, because the training and tests are the same,

### [14:13 - 14:34]

the covariances are the same, so they kind of cancel out. Whereas out of domain, you get some dependence, extra dependence here. And a priori, it's not clear whether just because you reduce the dimensionality, it doesn't, maybe you worsen the conditioning and that makes things worse. So it's not clear, pre-training is actually better for out of domain. But actually with a little bit more work,

### [14:34 - 14:46]

we actually ended up proving that pre-training actually improves the SS risk for this model on arbitrary covariance shifts, which is actually a pretty, I was a little bit surprised by the generality of this result.

### [14:48 - 15:16]

Okay, so now you can put pre-training and self-tuning, self-training together. And here the intuition is aux inputs model uses Z. So it's better in domain and we can use it to produce more accurate pseudo labels in distribution. And these pseudo labels are going to increase the amount of data that the NML model is trained on. And notice that it is important that we are not using Z here

### [15:16 - 15:19]

because Z is not robust as an input.

### [15:21 - 15:36]

So we can prove that in an out does much better than aux outputs. When Z reduces uncertainty about why given X. In other words, if you condition on Z that variants over Y is, you know diminished.

### [15:38 - 16:06]

So the summary so far is aux inputs using auxiliary information Z as input features, this is great in domain, because you're adding more information, but it doesn't work out of domain. because of the distribution of Z shifts. You can use it as a pre-training output, and this helps out a domain, but doesn't work in domain. And you can use self-training to combine the two

### [16:06 - 16:21]

to produce in and out, and you get the best of both worlds. So one thing that I think is really interesting, conceptually interesting here is that we have these spurious features. Z is, in some sense, a bit of a spurious feature.

### [16:23 - 16:49]

And in general, spurious features, if you think about them, is bad. We want to remove them. But here we are able to, even with the box outputs model, show that we can leverage these spurious features for improving robustness. And then the extra kind of, we can kind of go the extra mile to show that using self-training, we can actually kind of glue the ALX inputs and ALX outputs model together so that we don't suffer

### [16:49 - 17:17]

in distribution accuracy as well. So what happens if you don't have auxiliary information Z? Well, notice that there's nothing semantically meaningful about Z versus X. You might as well just assume that if you have just an input, you can call part of it X, and you can call part of it Z. And maybe, this is kind of future work, we can actually find better ways of automatically splitting,

### [17:17 - 17:22]

your features and leverage it so that you can leverage in and out to get better robustness.

### [17:23 - 17:52]

All right, let's shift gears and talk about gradual shifts. So this is a paper from ICML, last year with Nanyang Ting. So, gradual shifts occur in many different settings, like self-driving cars with different weather conditions, with neuroscience applications, and applications related to chemistry. So, Here is a motivating example that we're going to consider.

### [17:52 - 18:26]

It's a little bit questionable to do a gender classification, so I apologize, but this is what we had in our paper, and we didn't think about this at the time. So the task here is to predict whether an image is male or female, and doing this across time. So we have a source domain, which is pictures in 1905, and we have the target domain, which is pictures in 1973, and we have intermediate domains,

### [18:26 - 18:59]

which are pictures from intermediate points in time. Remember, we have labels only for the source, and unlabeled examples for everything else. So our goal is to get high accuracy for now only on the target domain. You can also ask for high accuracy on all the domains, but we'll leave that aside for now. So on this dataset, we train a source classifier, and it does really well, 98% on the source,

### [18:59 - 19:29]

but it drops in accuracy quite a bit on the target because, well, fashions change. If you do straight-up self-training on the target, so in other words, train on source, label the target, unlabel it, and just train again, it doesn't really improve. It improves things by 2%, so that's not great. Yeah, but if you do gradual self-training, which I'll explain in a bit, we can actually close about half the gap

### [19:29 - 19:46]

to the kind of oracle where you train and test on the target. So this is kind of as good as you can do if you actually have labeled examples on the target. And we were able to close half the gap. So how does this work? So this is kind of as good as you can do if you actually have labeled examples on the target. And we were able to close half the gap. So how does this work? So how does this gradual self-training work?

### [19:46 - 20:12]

So you have labeled examples in your source domain. You're going to train a classifier. You're going to use that classifier on the next domain to pseudo-label the examples. We're going to assume that the examples have shifted a little bit. And then you're going to fit a new classifier on the pseudo-labels. And you kind of repeat until you get to the target domain. And then you take your classifier.

### [20:12 - 20:41]

So notice that this is not a covariate shift problem. The actual optimal classifier changes between source and target. And the idea is that by doing this self-training, you can kind of gradually track the changes over time. So in order to show when gradual self-training works, we need some assumptions. So some of the assumptions we made are you can classify the data with some margin.

### [20:41 - 20:55]

So some of the assumptions we made are you can classify the data with some margin. So some of the assumptions we made are you can classify the data with some margin. It doesn't have to be separable. But the majority of the examples have to be separable by a margin. And also that the amount of shift is less than the margin. And that your model is also elliptical.

### [20:57 - 21:16]

So first we show that if you don't do any self-training, then the classifier can become stale and you get everything wrong. So because the optimal classifier changes over time, your points can shift around. And if you don't adapt, then you just can't do it.

### [21:18 - 21:42]

So if you don't do self-training, that's bad. We prove in this paper, I'm not going to have time to get through the details, that self-training does better. So the error on the target domain after t iterations is going to be exponential in t times an error of your source classifier plus something that depends on the number of, for example.

### [21:44 - 22:17]

And so notice, I mean, this looks bad because it's exponential growing in t. We show that this bound is actually tight for gradual self-training. Because in the worst case, the error is compound, kind of exponential. But what you can, what the studies show is that if your initial base error is small, enough, then the blow up, you still get non-vacuous results.

### [22:17 - 22:25]

Whereas if you don't do self-training, then immediately, even after two rounds of adaptation, then you get kind of trivial error.

### [22:29 - 22:55]

So this is in the setting where we're making really no distributional assumptions other than a kind of margin assumption. You can get stronger results. If you assume that x given y is Gaussian. And the key idea here is that since the shift is small and things are Gaussian, you can actually maintain the Bayes opt over time.

### [22:55 - 23:19]

And the takeaway here is that self-training can actually do better than this kind of exponential rate is if when your distribution is kind of nice. So you can see the paper for more details. So how do we do this? So how do we do this? So how do we do this? So how well does this work in practice? We looked at three different data sets, rotating MNIST data set, portraits, which is the example

### [23:19 - 23:52]

I've been demonstrating, and cuff type. And we see that here, the blue is the oracle. So this is training on and testing on the target. Gradual self-training, and if you do jump directly to the target, and if you use, I guess, this is the source. So we see that for rotating MNIST, which is a rather simple data set, gradual self-training actually recovers most of the gap between adapting and not adapting.

### [23:54 - 24:24]

And in other cases, it recovers about half the gap. So I want to point out kind of two important details here that the theory actually tells us about, which we found also to be useful in practice. So the first is Rی. regularization and so the idea is that if you don't regularize then you're just going to find any old classifier that gets low loss not necessarily the

### [24:24 - 24:53]

max margin which means that even after a small shift your classifier is too close to the boundary and you can get a lot of points wrong and your balance go outs out the window the second detail which is important is the idea of label sharpening so when we're doing self-training we pseudo label some points and then we use the actual kind of binarized label so if it's 60 percent plus and 40

### [24:53 - 25:23]

minus when just treated less a plus versus if you use soft pseudo labels we're actually going to train on you know kind of a 0.6 plus and a 0.4 minus and the idea here is that without label sharpening we don't change the classifier so if you train on kind of the same distribution then we can you know get the same thing back so label sharpening is actually important here to get

### [25:23 - 25:52]

self-training to work and experimentally on rotating MNIST we show that if you don't do explicit regularization or don't do soft hard don't do hard pseudo labels then your accuracy drops quite a bit from 84 to you know 45 and notice that regularization is not just like kind of for generalization even as the data set of your source increases you still need the regularization here

### [25:53 - 26:25]

so another point thing i want to point out is this idea of what it means for the shifts to be kind of small and in the paper we as require theoretically that the shifts be small in watts of saying infinity this means that each image is kind of shifting by only you know a kind of small amount and this is you know satisfied by kind of rotating the MNIST data set you can think about other cases where

### [26:25 - 26:42]

the successive distributions between two domains is actually kind of small in let's say KL divergence for example let's say the source domain is all is well again still a little bit smaller than the source domain but it's still kind of small in let's say KL divergence for example let's say the source domain is all is well again still all is well again still you know non-rotated digits

### [26:42 - 27:13]

and the target is everything is rotated by 60 degrees and you have intermediate domains where you're kind of mixing in more parts of the target so in this case you know graduate self training actually doesn't work because you're not really learning anything about how to you know you're basically exposing the model to the target immediately and you're not really learning anything about how to classify

### [27:13 - 27:15]

them and you're just going to kind of get the target wrong

### [27:18 - 27:45]

so the summary of this section so far is that gradual shifts and self-training is a really interesting tool because you know one of the main challenges behind domain adaptation is how can you extrapolate to distributions which are very different from your training distribution and generally this is impossible in general gradual domain adaptation gives you additional structure whereas that you

### [27:45 - 28:07]

can actually go far but we're going to help you along the way by tracking the changes and self-training we show that with a simple technique that allows you to do that so you can think about this self-graduates just over time it's essentially leveraging the smoothness over the distribution changes of all on some axis but it's interesting to think about other types of layers and the way

### [28:07 - 28:21]

other types of smoothness and other variables. There's nothing that says that this has to be time. What about kind of distribution changes in space? That seems very natural or other kind of variables. So this is something that would be interesting to explore in future work.

### [28:23 - 28:51]

So that concludes the basic portion of the talk. We talked about auxiliary information and gradual shifts, two types of structures that we can exploit to get good unsurprised domain adaptation results. So I'll just end with some final remarks. So domain adaptation, as we've seen in this workshop, is a really important problem. But it's almost too broad.

### [28:53 - 29:15]

And I would argue that we kind of need to start developing a language of looking at different types of structures. It's not enough to say that OOD. OOD doesn't really mean anything, because it's the complement of ID. In this talk, we looked at auxiliary information, gradual shifts. There's other things to explore, like conditional independence.

### [29:18 - 29:28]

And then the second point I want to make is we leverage self-training quite a bit here. Self-training, I would put it as old technology that just kind of works. It's like a shovel.

### [29:30 - 29:58]

You're shoveling predictive power from the source domain to the target domain or transferring power between two models in general. And I want to kind of say that self-training intrinsically should be a useful resource for robustness. Because if you think about ID versus OOD, in general, you have different models that work for ID versus OOD. And you often are in the

### [29:58 - 30:17]

situation where you need to kind of transfer predictive power. For example, in the auxiliary information, we're able to transfer predictive power to the target domain. So we're able to try to transfer the predictive power from the aux inputs model, which uses auxiliary information as inputs, to the aux outputs model, which uses auxiliary information as outputs.

### [30:20 - 30:23]

So that's it. Thanks for your attention.

### [30:28 - 30:34]

So now we are entering the Q&A section with Percy Lam, the assistant professor at Stanford.

### [30:36 - 30:52]

I guess I'll come up with the first one, my question. So Percy, I really like your talk on the self-training and different methods. So in general, for building robust ML models, what do you think are the major challenges that we're facing?

### [30:54 - 31:25]

Yeah, that's a pretty broad and good question. I mean, I think there's a few challenges when thinking about robustness. Maybe one kind of technical thing is that robustness is very broad. So I think we should be trying to develop a better language to think about forms of robustness, whether it be small perturbations or is it shifts in distribution. And even if you look at distribution shifts, I feel like we

### [31:25 - 31:47]

still lack kind of a language for talking about the types. If you think about in domain and then out of domain, OOD, we talk about OOD as if it's like one thing, but it's the complement of in domain, which is kind of pretty unspecified. And you can think about maybe the distance between the distributions, but in high dimensions, this doesn't really give you that much.

### [31:50 - 32:05]

And then I guess maybe another challenge is more on the practical side. A lot of what we've been thinking about lately is what are the quote unquote realistic shifts that one would see in the wild.

### [32:07 - 32:34]

And we had this recent data set called Wilds that where we sought to talk to a bunch of domain experts and look at the cases that come up, generalization between hospitals or generalization between camera traps. I think in a lot of the work focused on kind of challenge problems, for example, going from photographs to sketches, for example, which I think is

### [32:34 - 32:42]

interesting and hard, but in the real world, does that kind of thing come up or not?

### [32:44 - 32:51]

And then I guess maybe a third thing I'll mention is more on the solution side. It seems that

### [32:52 - 33:15]

using unlabeled data or data in general seems to be a very powerful way to get at robustness. Any sort of data where you presumably don't have a label data, otherwise you would have used it. So pre-training and self-training are primary ways that you can try to leverage unlabeled data. And I think

### [33:17 - 33:40]

figuring out the best way to leverage the data is still a kind of open problem. I see. Thanks a lot for the insights. So here we get a question from the audience. I'll read it out. So the person asks, when you try to leverage unlabeled data, what is the best way to leverage the data? So if you train aux outputs, you initialize from pre-trained. Instead of merely initializing,

### [33:40 - 33:58]

can you keep training with the original data around? Similarly, for the final model, you initialize from the aux out model. Again, what if you train a model back propagating all the way through into the aux model? So more than just initializing.

### [34:00 - 34:15]

Right. So I guess there's maybe two parts. The first, is when we do aux outs, we have pre-training. So we train inputs to the auxiliary information.

### [34:19 - 34:26]

So we initialize. And then in practice, we fine tune the model, which is kind of typical.

### [34:33 - 35:06]

In the theory, I guess, because the simplified assumption is that even by predicting the auxiliary information, you already learn the relevant subspace that governs the predictor. You kind of don't really need to do that. And you can just tune the last layer. And then, I don't know. There was a second part of that. Yeah. Yeah. Yeah. Yeah. Sort of about the final model. Yeah. Sort of about the final model.

### [35:06 - 35:17]

Similarly, for the final model, you initialize from the aux out model. Again, what if you train a model back propagating all the way through into the aux model? So it's more than initializing.

### [35:19 - 35:39]

When you say back propagating through the aux model, I mean, this is what we do when we have the fine tuning, right? The aux model provides the initial parameters, and then we are doing back propagation on the pseudo-labeled and the label data set through the entire model.

### [35:41 - 35:54]

I see. Yeah. So maybe the person who asked the question can further clarify. But we can go to the next question for now.

### [35:56 - 36:06]

Have you tried any of these distribution shift techniques on security data, such as network, network intrusion, malware, spam, and et cetera?

### [36:08 - 36:10]

Yeah. So the short answer is no.

### [36:12 - 36:43]

One maybe thing to point out is that a lot of this work is more on distribution shifts that are, I guess, more sarcastic as opposed to adversarial. There's a whole line of work that we've done that addresses more of the adversarial setting. As well as subpopulation shift, where it's kind of worst case over group. So this is all more average. And I imagine for some of these more security applications,

### [36:43 - 37:18]

you want to be modeling the worst case. Now, of course, nailing down worst case over what, I think, is challenging in general. So I think that this is a place where it's maybe helpful to think about something in between, where you can have something a bit more distributional to tell you, here are the general types of distributions that we're interested in generalizing, but

### [37:19 - 37:45]

being worst case. Maybe you can have multiple target distributions and worst case over them, or maybe target distributions and you allow for some worst-case perturbations. I see. Got you. Another question I have is that, like, it seems like for a lot of methods, such as this self-training method, use auxiliary data. Like, do you,

### [37:46 - 38:11]

like, in your future work, do you plan to, like, look at data sets with other features? Because the nature of the data set really, like, influences the model design we have. Are you interested in, like, looking more at new data sets with interesting features or, like, dive deeper into the existing methodology? Yeah. Well, certainly, we want to look at different

### [38:11 - 38:36]

types of, you know, data sets more broadly. One thing to point out, which I mentioned at the end of the first section, is that the auxiliary information is, in some sense, not fundamental, right? You can always take your input and split it up into something that you call auxiliary and something that you don't call auxiliary. The key thing with this,

### [38:36 - 38:58]

what we call auxiliary information, is it's intuitively the part of the input that shifts more. It's informative in domain, but it shifts out of domain. So, if you could identify parts of your input that satisfy this criteria, then you can leverage some of the techniques, the in and out algorithm that we've developed. It'll be interesting to figure out how you can

### [38:59 - 39:35]

automatically, you know, learn to split the two, because then this is more of a general domain adaptation kind of algorithm. I see. Got you. We get a new question. It's about, have you experimented with training a generative model on the ID and OOD data, then generating interpolations in the latent space to artificially create a gradually shifting distribution? Yeah. So, I guess this is in reference to

### [39:35 - 40:02]

the work on gradual domain adaptation, where we have a source and target. I mean, in short answer, we didn't try that. That seems like an interesting idea. So, this would be, I guess, a situation where you have a source and you have a target, unlabeled data, but they're very far away. So, you can try to kind of bridge the two synthetically, as opposed to, in our case,

### [40:02 - 40:26]

this is kind of the data is kind of naturally occurring. Yeah. It would be interesting to try this. I think I'm trying to think on the fly, I haven't thought about this, whether some of the assumptions, how they would kind of hold. So, we need to be the case. I mean, the set is the assumption that its distribution doesn't change that much. I think that's easy to satisfy.

### [40:27 - 40:54]

There's also, I guess, some kind of covariate shift. So, if you classify data with a margin, you want there to be a true classifier that kind of works in a successive domain that is shifting by less than the margin. Yeah. Yeah. I mean, I think it's worth trying. I mean, I can't, maybe

### [40:57 - 41:22]

think of any kind of immediate problems with this. I mean, it depends on the nature of the interpolation. It might go through some weird part of the space. And it's certainly not necessarily related to the Y given X part, but it's an intriguing idea.

### [41:24 - 41:51]

Great. Yeah. Interesting proposal from the audience. And one last question is, for a gradual self-training, one data require, this question is a little bit long. I read it fast. So, for gradual training, one data requirement is to have the sequence of data sets where the distribution gradually shifts over some axis, such as over time. However, oftentimes real data is not so well organized.

### [41:51 - 42:15]

We may receive a bunch of data, which has shifts along this entire axis, but it's not clearly, organized into gradual shifts, such as not all jumbled together. Would it still be possible to do a form of gradual self-learning in this type of messier setting? Or is this inherently impossible without the organizational structure? This is related in some sense to the previous question

### [42:15 - 42:22]

form, like the previous ID and OOD question. Yeah, that's a good question.

### [42:23 - 42:49]

I think in our current setting, we kind of assume that, time is somehow governing the distance of the shift, but that may not be the case. The only thing we need is a sequence of distributions whose, I guess, the discrepancy doesn't vary too much. So, if you have periods where nothing is happening, but you're getting data in spurts, but across that spurt, the distributions are still close, then that's fine.

### [42:49 - 43:15]

I also think that it's, there's nothing sacred with time. You know, we thought briefly about a kind of spatial shifts as well, or any other variable where you can think about varying the distribution, like the distribution changes gradually from one place to another. Also, the converse of the question is true. Like in space, there are cases where,

### [43:16 - 43:24]

let's say you go over, you hit the ocean, and then all of a sudden, obviously your distribution is changing. You know, you're getting a little bit of, like, you know, this, this kind of change. And then, like, you know, like, you're getting a little bit of, like, you're getting a little bit of, you know, you're getting a little bit of, like, you're getting a little bit of change. And so, you know,

### [43:24 - 43:54]

wildly. So in that case, I mean, the gradual domain shift wouldn't work. You can't gradually shift from Africa to North America by crossing the Atlantic. But in those cases, we probably need to be a bit more creative about how we define this kind of latent space in which we prioritize the distributions. Maybe like looking at kind of geography and like straight line

### [43:54 - 44:17]

distance is not really the right. So I guess this relates to maybe some sort of kind of metric learning stuff. And same with time. Maybe there's, if you can add other variables which do are similar, maybe you have data that coming from, also there's a space or users, specific data, there's data coming from, also there's space or users, specific data, there's data coming from,

### [44:17 - 44:47]

also there's space or users, specific data, there's data coming from, also there's space or users, and you can perhaps kind of use those as bridges rather than just relying on time. Got you. Thanks a lot. And now it's a good time to wrap up. Thanks, Percy, again for the Q&A section.
