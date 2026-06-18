# The Misconception that Almost Stopped AI [How Models Learn Part 1]

- URL: https://www.youtube.com/watch?v=NrO20Jb-hy0
- Model: `youtube-auto-caption-json3`
- Requested language: `en-orig`
- Detected language: `en`
- Refined at: `2026-06-05T08:19:37`

## Transcript

### [00:00 - 00:28]

This is the loss landscape of Meta's Llama 3.2 large language model. Virtually all modern AI models learn by gradient descent. Visually, this looks like starting at a random location on our landscape and working our way downhill towards lower loss, higher performance solutions. But how does our model avoid getting stuck in local valleys like this one? This question stopped many early AI pioneers in their

### [00:25 - 00:53]

tracks. Jeff Hinton, who would go on to win the Nobel Prize in 2024 for his work in AI, initially entirely dismissed training neural networks like llama with gradient descent for exactly this reason. Of course, as we now know, gradient descent actually works unbelievably well. What understanding was Hinton missing? And what's wrong with our picture? In this series, we'll take a fresh look at how AI models

### [00:51 - 01:16]

learn. Starting with a visual first approach, we'll dig into how exactly our llama model learns from real training examples, what our loss landscape can and can't show us, and ultimately see why gradient descent for large models looks more like falling into a wormhole than it does simply heading downhill. In part two, we'll switch to a more math-driven approach, which will help us grapple with the incredibly

### [01:14 - 01:39]

high-dimensional spaces these models operate in. Researching this series, I found some really interesting visualization techniques that required some deep focus time to get my head around, which this video sponsor, Incogn has really helped me with. I've been an Incogn customer for 6 months now and continue to be blown away by how many fewer spam texts, calls, and emails I get, giving me more

### [01:37 - 02:01]

quality focus time. The way Incogn does this is really impressive. After signing up for an account, you give Incogn permission to work on your behalf to contact data brokers to remove your data, which brokers are generally legally obligated to do upon request. From here, you get this great dashboard that tracks all the removal requests in progress. It's really impressive and always working in the background. When I

### [02:00 - 02:24]

checked in at the end of last year, my data had been removed from 115 different data brokers, and the count is now up to 220. I really value the control over my personal data that Incogn gives me. In the United States, we have these people search sites where for a small fee, anyone can look up information about you like your address, email, phone number, education, employment history, court

### [02:21 - 02:46]

records, and social media accounts. This gives you an idea of all the information that data brokers are able to gather and sell. I signed up for an account on one of these people search sites after being an incogn for a couple of months. And impressively, I wasn't able to find any records of myself. You can get a great deal on Incogn 60% off an annual plan by using the code Welch Labs or following

### [02:44 - 03:10]

the link in the description below. It's been a while since I've made a multi-part series like this. Huge thank you to Incogn for helping make this series possible and helping me get more quality focus time as I work on it. Now, back to how AI models learn explained visually. Let's begin by experimenting with a real large language model. Meta's Llama 3.2 1.2 billion parameter model.

### [03:08 - 03:33]

Given a sequence of text models like llama and chatgpt are trained to predict the word or word fragment known as a token that comes next. When training on the text the capital of Francis Paris, for example, this text is tokenized into six tokens, each represented by a single number and passed into our model. For each input token, our llama model returns a prediction of what token will

### [03:31 - 04:05]

come next in the form of a vector of probabilities. So when we pass in the six tokens for the capital of France's Paris, our model returns six vectors each of length 128,256 with one predicted probability value for each of the 128,256 tokens in Llama's vocabulary. Our fifth vector has a maximum probability of 0.39 at index 12,366 which corresponds to the token for Paris. So our model is assigning a

### [04:02 - 04:28]

39% probability to Paris as the token that follows the capital of France is the next most likely token according to the model is the word a with a probability of 8.4%. This could lead to sentences like the capital of France is a beautiful place to visit. During training, the model's predicted probabilities at each position are compared to the correct next token from the training text. So at

### [04:26 - 04:51]

the first position, our model is trained to predict the token for capital. And at our fifth position, the model is trained to predict the token for Paris. From here, we need some way to measure how well our model is working. The metric we choose here will guide the learning process. One option is to directly measure the model's error by taking one minus the model's predicted probability of the correct next token.

### [04:49 - 05:17]

In the fifth position, for example, if the model predicted the token of Paris completely confidently with a probability of 1.0, our error would be 1 - 1 equals 0. If the model's predicted probability dropped to 0.9, our error would increase to 1 minus 0.9als 0.1 and so on. This metric is known as the L1 loss. And as we'll see when we look at the mathematics of backpropagation, it has a very important role to play in

### [05:15 - 05:41]

learning. However, it turns out that models are able to learn more effectively if we instead use a function called cross entropy loss. To compute the cross entropy loss, instead of taking one minus the model's predicted probability of the correct next token, we instead take the negative logarithm of this probability. This ends up looking similar to our L1 loss. If the model's probability of the correct next

### [05:39 - 06:07]

token is one, our cross entropy loss equals minus the log of one, which equals 0, matching our L1 loss. If the model's probability of the correct next token drops to 0.9, our L1 loss equals 0.1 and our cross entropy loss equals 0.105. And if the model's probability drops to 0.8, our L1 loss equals 0.2 and our cross entropy loss equals 0.223. The key difference here is that as our

### [06:05 - 06:32]

model becomes less and less confident in the right answer, our cross entropy loss shoots up, penalizing our model more. Large language model training is entirely driven by reducing this cross entropy loss. Now, how do we actually use this loss to make our model better? And how can we visualize the process? Our model's current parameters give a probability of 0.39 for a next token of

### [06:29 - 06:58]

Paris, leading to a cross entropy loss of 0.94. Note that we would typically compute our loss at each token position and average the results. But for now, let's focus exclusively on training our model to be more confident in a next token of Paris at the fifth position. So our total cross entropy loss is 0.94. Now, how do we adjust our model parameters to increase the model's confidence in Paris and bring down this

### [06:55 - 07:22]

loss? Our llama model follows a fairly standard transformer architecture. It's composed of 16 layers, each containing an attention and multi-layer perceptron compute block. In this video, we won't be too concerned with how these layers work. A helpful and increasingly true mental model here is to think of our whole transformer as a single function f that takes in our input text x and uses

### [07:20 - 07:44]

its parameters theta to compute the next token probabilities. We'll explore how our model's output changes as we change our model's parameters. And as we'll see, doing this in a structured way is precisely how these models learn. Let's start by visualizing the impact of just one of our 1.2 2 billion model parameters on our model's output. The multi-layer perceptron compute block in

### [07:42 - 08:15]

the model's final layer has around 50 million total parameters. We'll pick out one of these parameters and see how it impacts our model's final output. Our parameter's current value is0.007. Let's decrease this parameter's value by 0.01. Rerun our input text through our model and see how our predictions and loss change. Our model's predicted probability of a final token of Paris moves down a little from 0.3916 to

### [08:12 - 08:39]

0.3901. Testing a change in the other direction, increasing our parameters value by 0.01 moves up our model's confidence to 0.3930. So for this single parameter and for this example text, we know that we can make our model more confident in the right answer by increasing this parameter's value. But by how much should we increase it? Can we make the model more confident in the right answer

### [08:36 - 09:01]

by further increasing this parameter? Extending and visualizing this idea, we can test more values and plot our model's output probability for a range of values of our parameter and see a nice parabola-ish looking curve as a function of the value of this single parameter. As we've seen, our cross entropy loss is the negative logarithm of these output probability values. Computing and visualizing these loss

### [08:59 - 09:25]

values, we get a flipped version of our parabola. These results suggest that we can maximize our model's predicted probability of the correct answer and minimize our loss by setting our parameter to around 1.61. We could then walk through each parameter one at a time, applying the same analysis and setting each parameter to minimize our output loss. Let's see visually why this idea does not work.

### [09:24 - 09:53]

After setting our first parameter theta 1 to a value of 1.61 61 to maximize our model's confidence in the Paris token and minimize our loss. If we move to a second parameter, we can again test a range of values and set the second parameter theta 2 to the value that minimizes our loss. In this case, 1.76. Now, here's the problem. If we return to our first parameter, which we already tested and set to a value of

### [09:49 - 10:16]

1.61, and run the same analysis, the shape of our curve changes. It now looks like a value of 1.11 will actually minimize our loss. The impacts of each parameter on our model's output are not independent. Changing the value of our second parameter changes the shape of our first loss curve and vice versa. So, we aren't going to be able to learn effectively by tuning one parameter at a

### [10:14 - 10:38]

time like this. We can see this visually by testing how our loss changes as we vary our parameter values together. testing a grid of values and plotting our loss for each combination of parameters as the height of a surface. It's now straightforward to see what went wrong earlier. If we only consider our first parameter, we're effectively looking at a slice like this. Moving to

### [10:36 - 11:00]

the bottom of this curve and then tuning our second parameter, we're now looking at a slice like this. When we move to the bottom of this second curve, we reach a new location on our loss landscape where we're no longer at the bottom of a valley in the direction of our first parameter. In this two parameter visualization, it is easy to see which combination of parameter values minimize our overall loss. We

### [10:58 - 11:25]

just need to set our two parameters to the values at the bottom of the bowl. We now have an optimal solution in both directions with respect to these two parameters. Now, of course, it's not just these two parameters that are coupled. Effectively, all 1.2 billion parameters of our model R. Meaning that our loss landscape is actually 1.2 billion dimensional. And that it's computationally impossible to explore

### [11:23 - 11:52]

all combinations of parameters as we did with our two test parameters. If we test 20 values for each parameter, testing two parameters, as we just did, requires 400 evaluations. Testing three parameters together is equivalent to testing all 8,000 values in a 20x 20x 20 cube. And testing all 1.2 billion model parameters like this would require an astronomical 20 to the power of 1.2 billion

### [11:49 - 12:16]

calculations. We need a far more scalable approach. Returning to our two-dimensional loss landscape, is there a way to find the bottom of the valley without computing the height of every point in the landscape? If you were lost in a forest on a mountain trying to find your way to the valley below without a map, a pretty reasonable thing to do is to just keep heading downhill. Even if you can't see

### [12:13 - 12:40]

the valley below, we can effectively do this mathematically. For each parameter, instead of computing the loss across a range of values, we can compute the slope of the loss curve, telling us which way is downhill in each direction and how steep the descent is. As we'll see in part two, it turns out that we can compute these slopes very efficiently. We won't even have to compute the actual values of our loss

### [12:38 - 13:04]

curve at all. From here, we can put our slopes together into a single vector called the gradient, which acts like a little compass that points us downhill. Note that technically the gradient points uphill, and we move in the opposite direction to go downhill. We'll see why this is the case in part two. The idea now is to take small iterative steps downhill where after each step we recomputee the gradient to guide our

### [13:02 - 13:28]

next step. This is known as gradient descent and is how virtually all modern AI models learn by taking small steps downhill. In practice, we're often able to find very good solutions even in very high-dimensional loss landscapes that we could never fully explore computationally. It's of course a little difficult to visualize the 1.2 two billiondimensional loss landscape of our language model and what going downhill

### [13:26 - 13:54]

really looks like in this high-dimensional space. One approach we can try here is to choose a random direction in our high-dimensional space and measure our loss as we take small steps in that direction. Note that here choosing a random direction means generating 1.2 billion random numbers, one for each model parameter. And taking a small step in this direction means multiplying these 1.2 to billion random

### [13:51 - 14:17]

numbers by a small scaling factor and adding these scaled random numbers to our weights and then recomputing our loss. As we move further in our random direction by increasing our scaling factor, we can compute our loss at each step and see how this combination of model weights impacts our loss. Note that this is almost exactly what we do when training our model with gradient descent, except here we're choosing our

### [14:15 - 14:39]

direction randomly instead of using the downhill direction from our gradient computation. Choosing a random direction like this will hopefully give us a broader feel for what our loss landscape looks like. Here's what the loss landscape for our llama model looks like as we move in a randomly chosen direction. Exploring our high-dimensional loss landscape in this way reveals interesting structures with hills,

### [14:37 - 15:04]

valleys, cliffs, and plateaus. Here's the loss landscape in a second randomly chosen direction. These two plots are for a randomly initialized model before training. Here's two more plots for our model after training. With our trained model, we can clearly see the lower loss value the model has learned through training. Note that we're using positive and negative values for our step size alpha. So our

### [15:02 - 15:28]

unmodified model weights show up here at alpha equals zero on our plot. Finally, it can be interesting to confine our random directions to certain layers. Here's what our loss landscape looks like as we explore two random directions in the first eight layers of our train models total 16 layers. We can take this approach one step further by putting these two random directions together onto a 2D grid and

### [15:26 - 15:54]

computing our loss for combinations of steps in each of our two random directions. We can now visualize our loss landscape as we explore these two random directions together. Now imagine navigating this loss landscape from the perspective of our gradient descent algorithm. Before training, our model's parameters are randomly initialized, meaning we're effectively dropped into a random location in this landscape. From

### [15:52 - 16:18]

here, our job is to navigate our way to the bottom of the valley, ideally the global minimum here. But our only guide is the gradient, which only tells us which way is downhill in the tiny local part of the landscape that we're currently on. A baffling fact about modern AI and one of the reasons many early AI researchers dismiss this approach is that there's no guarantee that gradient descent will find the best

### [16:16 - 16:43]

or even a good solution in these high-dimensional loss landscapes. This view of our landscape has many local minima where gradient descent could potentially get stuck. But remember, even with our clever random direction probing trick, we're still looking at a two-dimensional shadow of a 1.2 two billiondimensional landscape. If we actually run gradient descent and train our model on our

### [16:40 - 17:03]

example text, we might imagine that learning looks like our parameters as a point working its way downhill in the landscape. And maybe the fact that the real optimization process is higher dimensional means that gradient descent can avoid getting stuck in local minima like this one. This was roughly the mental image I had in my head when I started working on this video. But after

### [17:01 - 17:27]

some experimentation, I realized this is really not what happens as our model learns. The reason is that as soon as we take even a small step in the full high-dimensional space of our model's parameters, our two-dimensional visualization of the landscape changes dramatically. Visually, as we run gradient descent, it almost looks like a wormhole opens up in our landscape, quickly landing our parameters in a very

### [17:25 - 17:49]

low loss valley that basically comes out of nowhere. And this all happens before our little dot even has a chance to really go anywhere on our landscape. It does move a little in the direction of the global minimum, but not enough to notice on our visualization. What exactly is going on here? Now, right now, we're just training on the single phrase. The capital of France is Paris. These new

### [17:48 - 18:12]

learned parameters quickly boost our model's probability for a next token of Paris close to a max value of 1.0 and bring down our loss close to zero. Of course, just training a large language model on a single short phrase is not how these models are trained in practice. Let's look at the same visualization, but where our model is instead trained on examples from the Wiki text data set. We'll use a batch

### [18:10 - 18:37]

size of four, meaning we're learning from four different examples at once. Our loss landscape becomes smoother. Now, this makes sense because our loss is now averaged across all of the tokens in our batch. When we take a gradient descent step, we see our loss landscape move down around our starting point. Just as we saw in our Paris example, this shows our model reducing the loss and performing better

### [18:34 - 19:01]

on the examples in this batch. When we switch to the next batch of data, the shape of our loss landscape changes and the gains we made from the last batch partially disappear. Step by step like this, our gradient descent algorithm will work its way towards a good solution and our visualized landscape changes as the model learns. In both cases, our 2D visualized loss landscape changes as we learn because we're

### [18:59 - 19:23]

effectively looking out in our randomly chosen directions from a new vantage point in high-dimensional space. This is analogous to our exploration of our model's loss earlier as we varied a single parameter and then varied two parameters together. Let's imagine for a moment that we're only able to visualize our loss with respect to one of our two parameters. Our loss may look something like this curve with

### [19:22 - 19:46]

respect to our first parameter. Now, if we run gradient descent, where we're moving in the full 2D space of both parameters, our entire curve with respect to the first parameter changes. We're effectively moving to a different slice of our full 2D loss surface. If there happens to be a nice valley close to us, but the only way to get there is to move in the direction of our second parameter, we

### [19:45 - 20:08]

won't see it at all in our initial 1D visualization with respect to our first parameter. And when we do find it with gradient descent, it will appear to come out of nowhere in our 1D visualization, much like our wormhole came out of nowhere in our full visualization. The wormhole example is a bit extreme because we're only training on a single short phrase, but it does tell us something interesting about the

### [20:07 - 20:31]

high-dimensional loss landscapes we're trying to visualize and understand. In this example, there are very good solutions very close to us in high-dimensional space. We just can't see them until we compute our full high-dimensional gradient and move in that direction. When Jeff Hinton did eventually try out gradient descent after getting stuck with another approach called Boltzmann machines, he

### [20:29 - 20:54]

tested it on a model with around 50 parameters and was shocked by how well it worked. For gradient descent to become fully stuck in a local minimum, it would have to get stuck in every dimension at once. And the chances of this happening become smaller and smaller as we add more and more parameters. For simple two parameter models, as we see in problems like linear regression, loss landscapes give

### [20:52 - 21:17]

us a complete picture and can provide helpful intuition for how these models learn. However, as our models become more and more complex with more and more parameters, our loss landscape visualizations become a more and more distant shadow of the model's true learning process. As we'll see next time, although our ability to visualize these landscapes becomes more and more limited as we add more and more

### [21:15 - 21:41]

dimensions, our mathematics has no problem operating in these incredibly high-dimensional landscapes. If you're curious about loss landscapes, check out this video's poster. This is a new, larger format that I haven't been able to do before at this high level of print quality. And I spent way too much compute time exploring the landscapes of different models for the poster. Top and center,

### [21:39 - 22:04]

you'll find the llama 1 billion parameter landscape that we covered in this video. To the left, I have a simpler model, GPT2, which results in a smoother and simpler landscape. In the upper right, you'll find a distilled version of Deepseek R1, which interestingly has larger smooth areas than Llama. This may be because Deepseek has been instruction tuned. It also generates a much higher confidence out

### [22:02 - 22:25]

of the box for a next token of Paris around 70%. On the bottom row, you'll find GEMO 1B. This is a smaller open- source version of Google's Gemini model. And on the bottom right, I've included a couple variants of the popular Quinn models. It's again interesting here to compare instruction tuning versus just pre-training. On the bottom of the poster, I've included some key figures

### [22:23 - 22:47]

from the video that explain how we're computing our loss landscapes. I'm really happy with how this poster came out, and I'm excited that I can offer this larger 17x 22 in size at very high quality. I've learned that with graphics like this, you really want to use photo printers to get all the fine details and colors right. You can pick up a physical or digital copy at welchlabs.com or

### [22:46 - 22:57]

purchase at a discounted rate when bundled with my Imaginary Numbers book. Big thank you to everyone who's purchased from the store. Your purchases go a long way to helping me make more great
