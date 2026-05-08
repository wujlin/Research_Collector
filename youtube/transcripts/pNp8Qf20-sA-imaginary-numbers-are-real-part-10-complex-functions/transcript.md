# Imaginary Numbers Are Real [Part 10: Complex Functions]

- URL: https://www.youtube.com/watch?v=pNp8Qf20-sA
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-07T13:31:59`

## Transcript

### [00:00 - 00:14]

So, what is this? We saw this shape back in part one, and then proceeded to not talk

### [00:14 - 00:19]

about it for like ten episodes. And at this point, I really wouldn't blame you if you

### [00:19 - 00:23]

thought this was some science fiction designed to get you excited about doing boring algebra

### [00:23 - 00:29]

problems. But before we chalk this up to unnecessary special effects, let's remember where this

### [00:29 - 00:32]

shape came from.

### [00:32 - 00:36]

We began our conversation in part one with an equation that appeared to have no solution,

### [00:36 - 00:41]

x squared plus one equals zero. And after all the work we've done so far, you can probably

### [00:41 - 00:45]

see how to find the answer algebraically. Subtract one from both sides of the equation

### [00:45 - 00:50]

and take the square root, resulting in x equals plus or minus i. Done.

### [00:50 - 00:54]

So that's cool, but to really make sense of our shape from part one, we need to dig

### [00:54 - 00:59]

a little deeper, and talk about functions of complex variables.

### [00:59 - 01:03]

The kinds of functions most of us are used to, functions of real numbers, have inputs

### [01:03 - 01:08]

and outputs that can be visualized using a single dimension. This means all our x values

### [01:08 - 01:14]

fit on a single number line, and so do our y values. It seems pretty reasonable, then,

### [01:14 - 01:18]

that if we want to figure out how x and y are related, we should put our x number line

### [01:18 - 01:22]

facing one way on our piece of paper, and put our y number line on the same piece of

### [01:22 - 01:27]

paper, just facing the other way. This forms a two-dimensional grid known as the Cartesian

### [01:27 - 01:28]

Coordinate System.

### [01:29 - 01:34]

Apparently invented by Rene Descartes in the 16th century after watching flies crawl around,

### [01:34 - 01:38]

the Cartesian Coordinate System is a super powerful tool for understanding the relationship

### [01:38 - 01:44]

between two variables. The Cartesian Coordinate System is powerful because it allows us to

### [01:44 - 01:48]

take abstract ideas, like functions, and turn them into something our brains can grasp much

### [01:48 - 01:54]

more intuitively, shapes. By giving each point on the planet its very own coordinates, Descartes

### [01:54 - 01:59]

was able to bring together the two largest areas of mathematics at the time, algebra

### [01:59 - 02:01]

and geometry.

### [02:01 - 02:06]

This greatly aided early efforts at classifying functions by Newton and others, and today

### [02:06 - 02:10]

the Cartesian Coordinate System shows up everywhere, helping us do all kinds of things like spot

### [02:10 - 02:12]

trends in data.

### [02:12 - 02:16]

So that's all fun and wonderful, but the Cartesian Coordinate System does come with a disclaimer

### [02:16 - 02:20]

– it only works in two dimensions.

### [02:20 - 02:24]

This limitation becomes a real problem when we start to think about functions of complex

### [02:24 - 02:29]

variables. These functions take in complex numbers for their inputs, and for the most

### [02:29 - 02:33]

part also output complex numbers. This means that the numbers we put in and get out of

### [02:33 - 02:38]

our function no longer fit on number lines. We need two complex planes to keep track of

### [02:38 - 02:42]

our numbers, one for our input and one for our output.

### [02:42 - 02:48]

This raises the question, if, when visualizing these functions, what we're really interested

### [02:48 - 02:52]

in is the connection between the input and output, how do we visualize what's happening

### [02:52 - 02:57]

on both planes simultaneously? We could try to fit our input and output planes together

### [02:57 - 02:58]

somehow –

### [02:58 - 03:02]

did with our number lines for real valued functions, but we quickly run into a pretty

### [03:02 - 03:09]

serious issue. As you likely know, the universe we live in has three spatial dimensions. So there's

### [03:09 - 03:13]

no way to fit the four spatial dimensions we need into a single structure that our brains

### [03:13 - 03:20]

can comprehend. We simply run out of dimensions. Fortunately, there are some very clever ways to

### [03:20 - 03:24]

see the relationship between two complex variables. But before we can get to these,

### [03:24 - 03:29]

we need to think about the mathematics of complex functions. Even though using separate planes for

### [03:29 - 03:33]

our input and output is not a perfect solution, this approach can still help get us started.

### [03:34 - 03:39]

Let's try it out with our original function, f of x equals x squared plus 1. Before we begin,

### [03:39 - 03:42]

let's make a quick variable change to make things easier down the road.

### [03:43 - 03:47]

We'll change the name of our input variable from x to z, and call our output variable w.

### [03:48 - 03:54]

Since z and w each have a real and imaginary part, let's go one step further and give these

### [03:54 - 03:54]

parts the name of our input variable w. Since z and w each have a real and imaginary part,

### [03:54 - 03:54]

let's go one step further and give these parts the name of our input variable w.

### [03:54 - 03:59]

We'll let z equal x plus i y, so x represents the real part of z,

### [03:59 - 04:04]

and y represents the imaginary part. We'll also let w equal u plus i v.

### [04:06 - 04:10]

Just as we can use tables to keep track of our inputs and outputs for real valued functions,

### [04:10 - 04:14]

we can also use tables to keep track of our inputs and outputs for complex functions.

### [04:15 - 04:20]

However, we now need four columns to keep track of our four variables, x, y, u, and v.

### [04:21 - 04:24]

We can now experiment with our function f of z

### [04:24 - 04:28]

equals z squared plus 1. If we plug in a complex number to our function,

### [04:28 - 04:33]

for example z equals 1 plus i, we can do a little algebra and obtain our result,

### [04:33 - 04:39]

w equals 1 plus 2i. Plotting our inputs and outputs, we see that the point 1 plus i in

### [04:39 - 04:44]

our input plane was pushed or mapped by our function to 1 plus 2i in our output plane.

### [04:46 - 04:49]

Let's plug in a few more points here and see if we can find a pattern.

### [04:50 - 04:54]

If we test points along a straight line in our input space, we see that

### [04:54 - 04:58]

in our output space our straight line is transformed into a curved line.

### [04:58 - 05:02]

Interesting. As you can imagine, plugging in points like this can get pretty tedious.

### [05:03 - 05:07]

To speed things up, let's let a computer do it for us. And instead of having our

### [05:07 - 05:10]

computer just map certain points, let's have it map all the points.

### [05:11 - 05:15]

We'll take advantage of the fact that the image you're seeing is just a collection of pixels that

### [05:15 - 05:21]

happen to be arranged on a grid. We'll use some code written in the programming language Python

### [05:21 - 05:23]

to move every single pixel in our input space,

### [05:24 - 05:29]

to its proper location in the output space. To make this work, we'll assign each pixel in

### [05:29 - 05:34]

our input video a complex number that corresponds to its location on the complex plane.

### [05:35 - 05:40]

We can then let our code take care of the tedious work of moving each pixel to its new location

### [05:40 - 05:46]

as dictated by our function, z squared plus 1. Our code will move points exactly as we did by hand

### [05:46 - 05:53]

before. If we have a blue pixel at the 1 plus i location on our input graph, then this blue pixel

### [05:54 - 05:59]

is the 1 plus 2 i location on our output graph, because f of 1 plus i is equal to 1 plus 2 i.

### [06:01 - 06:05]

We saw before that our function warped a straight horizontal line into a curvy one,

### [06:06 - 06:10]

so it should have some interesting effects on our video. We'll include some reference

### [06:10 - 06:13]

markers on top of our input and output planes to keep track of our numbers,

### [06:13 - 06:17]

but we won't transform these pixels. Alright, ready?

### [06:17 - 06:23]

Let's start by drawing some simple lines. A horizontal line along the positive x-axis turns

### [06:24 - 06:29]

out to be pretty similar in our output space. But what about a line along the positive imaginary

### [06:29 - 06:35]

axis? This line appears to have been rotated. As we add more lines, we begin to see a pattern.

### [06:36 - 06:40]

Our family of straight lines is turned into a family of curved lines. Cool, right?

### [06:42 - 06:47]

So we found one pattern, but how is this pattern explained by our function z squared plus 1?

### [06:48 - 06:52]

And more importantly, how does this fit with everything else we've learned about complex numbers?

### [06:52 - 06:56]

What else would be interesting to draw in our input space to test our mapping?

### [06:57 - 07:00]

What shape would you draw to learn more about what our function is doing?

### [07:01 - 07:04]

Next time, more shapes.

### [07:22 - 07:25]

Thanks for watching, and I'll see you in the next video.
