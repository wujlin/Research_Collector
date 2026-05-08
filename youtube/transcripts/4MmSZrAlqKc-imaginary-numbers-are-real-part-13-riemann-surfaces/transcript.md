# Imaginary Numbers Are Real [Part 13: Riemann Surfaces]

- URL: https://www.youtube.com/watch?v=4MmSZrAlqKc
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-07T15:25:51`

## Transcript

### [00:00 - 00:23]

This is a Riemann surface. It's going to help us think in four dimensions.

### [00:23 - 00:28]

We made it by cutting our planes at the discontinuities in our paths, and taping them together in

### [00:28 - 00:33]

a way that made our paths from one plane to the other continuous.

### [00:33 - 00:37]

Riemann's big idea here is that the domain, the input values of our multifunction, should

### [00:37 - 00:44]

not be a flat two-dimensional plane. Our domain should instead be this, a curved surface living

### [00:44 - 00:49]

in higher dimensional space, a Riemann surface.

### [00:49 - 00:53]

What's incredible here is what the geometry of our Riemann surface is going to allow us

### [00:53 - 00:55]

to do.

### [00:55 - 01:00]

Using our Riemann surface as the input space to our multifunction, we can literally fix

### [01:00 - 01:05]

all of the problems we've encountered thus far. Our function will be one-to-one, continuous,

### [01:05 - 01:09]

and our Riemann surface will even help us elegantly explain the weird loop behavior

### [01:09 - 01:12]

we saw back in part 11.

### [01:12 - 01:14]

Let's see how.

### [01:14 - 01:19]

Riemann envisioned these surfaces as sheets covering the input plane W.

### [01:19 - 01:24]

Our Riemann surface is constructed from two copies of the complex plane, and the idea

### [01:24 - 01:25]

here is that each input plane is a Riemann surface. Each input plane is a Riemann surface.

### [01:25 - 01:30]

The input value on W lies directly below its corresponding points on each layer of our

### [01:30 - 01:31]

Riemann surface.

### [01:31 - 01:37]

If we follow a line straight up from the value 2i on our W plane, we find two points that

### [01:37 - 01:43]

correspond to W equals 2i. Our Riemann surface fixes our one-to-one problem just as our two

### [01:43 - 01:49]

complex plane solution did. Each of our two solutions on Z corresponds to its very own

### [01:49 - 01:53]

copy of the W plane. These are called branches.

### [01:53 - 01:58]

So our Riemann surface makes our mapping one-to-one, just as our two-complex-plane approach did

### [01:58 - 01:59]

last time.

### [01:59 - 02:05]

But what about continuity? As we saw last time, a big problem with our two-complex-plane

### [02:05 - 02:10]

solution is that it introduced discontinuities.

### [02:10 - 02:15]

We constructed our surface in such a way that our colored path was continuous, but we encountered

### [02:15 - 02:22]

this weird self-intersection. So let's dig a little deeper. Remember the main idea here.

### [02:22 - 02:23]

Using our Riemann surface as the input plane, we can map one-to-one, just like we did last

### [02:23 - 02:24]

time.

### [02:24 - 02:34]

So instead of drawing paths or shapes on our W plane, we should really be drawing on our

### [02:34 - 02:36]

Riemann surface.

### [02:36 - 02:40]

Drawing on three-dimensional surfaces can be a little challenging, so we'll make use

### [02:40 - 02:47]

of a tool that wasn't invented until over a century after Riemann's death. A computer.

### [02:47 - 02:52]

Just as with our paper version, we'll start with our W plane lying flat on the ground,

### [02:52 - 02:56]

and place our Riemann surface directly above.

### [02:56 - 03:00]

Before we start drawing paths all over our surface, let's make sure we know what we're

### [03:00 - 03:01]

looking at.

### [03:01 - 03:06]

We're trying to understand the complex function W equals Z squared, or taken in the other

### [03:06 - 03:12]

direction, Z equals plus or minus the square root of W. The mapping between W and Z is

### [03:12 - 03:16]

the same in both directions.

### [03:16 - 03:21]

The visualization challenge here is that our mapping is four-dimensional. Both Z and W

### [03:21 - 03:22]

have real and imaginary dimensions. Both Z and W have real and imaginary dimensions.

### [03:22 - 03:23]

Both Z and W have real and imaginary dimensions. Both Z and W have real and imaginary dimensions.

### [03:23 - 03:24]

Both Z and W have real and imaginary dimensions. Both Z and W have real and imaginary dimensions.

### [03:24 - 03:29]

Back in part 10, we called these X, Y, U, and V.

### [03:29 - 03:34]

What we're seeing when we visualize our Riemann surface is a two-dimensional surface in three-dimensional

### [03:34 - 03:36]

space.

### [03:36 - 03:40]

In this case, since we positioned our surface directly above our W plane, two of our three

### [03:40 - 03:46]

dimensions correspond exactly to the real and imaginary parts of W. We called these

### [03:46 - 03:48]

U and V.

### [03:48 - 03:52]

Part of Riemann's idea is that our third dimension should represent the Z value of

### [03:52 - 03:59]

of our function. But as we know, z is a complex number. It has both a real and imaginary part,

### [03:59 - 04:03]

so there's no way to show both of these on a single axis.

### [04:03 - 04:08]

What's often done when visualizing these surfaces, and what we're going to do here, is simply

### [04:08 - 04:13]

pick the real or imaginary part of z, and use this value as the third dimension, the

### [04:13 - 04:20]

height of our surface. Here we're using x, the real part of z. Doing this has a nice

### [04:20 - 04:26]

visual result. Each point on our Riemann surface lives in 3D space at a location corresponding

### [04:26 - 04:33]

exactly to its u, v, and x values. So each point on our surface represents a single solution

### [04:33 - 04:39]

to our equation. And three of the four values needed to describe the solution are represented

### [04:39 - 04:45]

by the point's location in 3D space. This is a nice result, but we must remember

### [04:45 - 04:50]

that this is not the whole picture. There's another variable, the imaginary

### [04:50 - 04:50]

part of z, that we can not legislate. It's presented by its Hollywood's Himalayan

### [04:50 - 04:56]

of z, we call this y, that is not included in our visualization. This becomes important when trying

### [04:56 - 05:01]

to figure out if we've actually fixed our continuity problem. If we follow a path along a

### [05:01 - 05:07]

single branch of our Riemann surface, we run into a bit of a problem when we hit this self-intersection.

### [05:07 - 05:15]

After all, which way should we go? Up or down? To answer this question, let's try to figure out why

### [05:15 - 05:21]

our surface self-intersects in the first place. This intersection happens along the negative real

### [05:21 - 05:29]

axis of our w-plane. Let's consider a point on this axis, w equals minus 1. Plugging in negative

### [05:29 - 05:36]

1 for w yields two solutions, z equals plus i and z equals minus i. These two solutions are clearly

### [05:36 - 05:43]

different, but they have the same real part, zero. Since we're only visualizing the real part of z,

### [05:43 - 05:45]

we have no way of seeing that these are in the same real part.

### [05:45 - 05:51]

This is the danger of visualizing high-dimensional mathematical concepts.

### [05:53 - 05:58]

What we're really looking at here is just a projection, a shadow of our full

### [05:58 - 06:03]

four-dimensional surface. So our line of self-intersection actually isn't.

### [06:05 - 06:09]

This is exactly like the two-dimensional shadows of three-dimensional objects,

### [06:09 - 06:11]

giving the appearance that the objects intersect.

### [06:13 - 06:15]

There are inherent limitations to this.

### [06:15 - 06:21]

However, there are some very clever ways to get a feel for what's happening in our missing fourth

### [06:21 - 06:26]

dimension. One approach is to expand our visualization to include another dimension

### [06:26 - 06:32]

of human perception, such as color. We'll color each point on our surface with a color that

### [06:32 - 06:37]

corresponds to the value of the fourth dimension of our function, in this case the imaginary part

### [06:37 - 06:43]

of z, y. To do this, we need to use a function called the dimension of the fourth dimension.

### [06:44 - 06:49]

To do this, we need to decide which colors to map to which numbers. This is called a color map.

### [06:50 - 06:55]

Our colors now give us a nice idea of what's happening in our missing fourth dimension, y.

### [06:56 - 07:00]

If we look at our line of self-intersection now, it's much more clear that since our

### [07:00 - 07:04]

colors are different, our four-dimensional function actually doesn't intersect itself.

### [07:05 - 07:10]

The apparent self-intersection is just an artifact of our visualization technique.

### [07:11 - 07:13]

So as we follow paths on our Riemann surface,

### [07:13 - 07:17]

the right thing to do with these self-intersection lines is to ignore them.

### [07:18 - 07:23]

If we now follow our path around our surface, we see that it's perfectly continuous,

### [07:23 - 07:26]

even at our weird self-intersection line. Excellent!

### [07:27 - 07:32]

So that's great, we have continuity. But there's still one missing piece of the puzzle.

### [07:32 - 07:35]

What about the weird behavior we saw back in part 11,

### [07:35 - 07:39]

where some paths ended up in new locations, and others didn't?

### [07:40 - 07:43]

Let's recreate these suspicious paths, first,

### [07:43 - 07:49]

just on our W and Z planes. Now, let's do the same exact thing,

### [07:49 - 07:52]

but this time using our Riemann surface to help us see what's going on.

### [07:53 - 07:58]

To keep our surface from getting too crowded, we'll choose one of our two paths to visualize first.

### [07:59 - 08:03]

Alright, ready? We'll draw the same exact paths on W,

### [08:03 - 08:07]

and see how they show up on our Riemann surface as they are mapped to our Z plane.

### [08:13 - 08:20]

So let's go ahead and draw one of our Z planes, and see how it looks.

### [08:26 - 08:30]

So why does our green path start out in one location on our Z plane, only to end up in another?

### [08:31 - 08:35]

Simply because our green path leads us to the other layer of our surface.

### [08:36 - 08:41]

From the perspective of our W plane, it appears that we've returned exactly to our starting point,

### [08:41 - 08:43]

but actually we haven't.

### [08:43 - 08:46]

The w-plane is just a projection, a shadow.

### [08:47 - 08:52]

In reality, our path has led us to a completely different branch of our function, with different z-values.

### [08:54 - 08:56]

This, of course, is only half the picture.

### [08:57 - 09:00]

Each point on our w-plane has two solutions on z.

### [09:00 - 09:04]

This is why our single path became two paths back in part 11.

### [09:05 - 09:09]

On our Riemann surface, our second solution is a flipped version of our first.

### [09:09 - 09:14]

The important thing here, of course, is that for either set of paths,

### [09:14 - 09:20]

our Riemann surface allows us to clearly see that some paths on w lead to the other branch, and some don't.

### [09:21 - 09:26]

More specifically, paths that go around the central point on our Riemann surface end up on new branches.

### [09:27 - 09:28]

This point is called a branch point.

### [09:30 - 09:34]

Branch points occur wherever the two branches of our function have the same exact value,

### [09:34 - 09:37]

and can tell us a great deal about how our complex function behaves.

### [09:38 - 09:39]

For us, this is a very important point.

### [09:39 - 09:40]

For us, this is the point w equals zero.

### [09:42 - 09:46]

So our Riemann surface not only fixes the troubles we ran into earlier,

### [09:46 - 09:49]

but beautifully explains the strange path behavior we saw.

### [09:50 - 09:52]

And this is just the beginning.

### [09:52 - 09:55]

Riemann surfaces are a huge part of modern mathematics,

### [09:55 - 09:58]

and there's way more to say than we have time for here.

### [09:59 - 10:02]

All right, we're finally ready to answer the question,

### [10:03 - 10:04]

what is this?

### [10:04 - 10:07]

Our entire discussion has centered around a single function,

### [10:07 - 10:08]

f of z equals zero.

### [10:09 - 10:15]

And so far, we've looked at one way to visualize the Riemann surface for our function

### [10:15 - 10:18]

by plotting three of our four variables in 3D space.

### [10:20 - 10:22]

The two-dimensional plot we started our discussion with,

### [10:23 - 10:25]

the one most of us see in math class,

### [10:25 - 10:27]

only shows two of our four variables,

### [10:27 - 10:29]

the real parts of z and w.

### [10:30 - 10:33]

The surface we created back in part one

### [10:33 - 10:35]

is the result of including one more variable,

### [10:35 - 10:37]

the imaginary part of z,

### [10:37 - 10:39]

as the vertical dimension of our visual function.

### [10:39 - 10:42]

When we first saw this surface in part one,

### [10:43 - 10:44]

many of you asked a very good question.

### [10:46 - 10:48]

If, according to the fundamental theorem of algebra,

### [10:48 - 10:51]

our function is supposed to have exactly two roots,

### [10:51 - 10:53]

why does our surface appear to equal zero

### [10:53 - 10:55]

at way more than two locations?

### [10:56 - 10:58]

This apparent contradiction has everything to do

### [10:58 - 11:01]

with the shortcomings of living in three-dimensional space

### [11:01 - 11:02]

that we've been discussing.

### [11:03 - 11:05]

When we visualize four-dimensional functions

### [11:05 - 11:06]

in three-dimensional space,

### [11:06 - 11:08]

we must remember that what we're really seeing

### [11:09 - 11:10]

is a projection,

### [11:10 - 11:12]

a shadow of the function's full four-dimensional form.

### [11:14 - 11:16]

Let's have a closer look at our surface.

### [11:16 - 11:17]

In our opening shot,

### [11:17 - 11:20]

half of our surface was hidden behind our paper,

### [11:20 - 11:23]

and the colors we used were chosen somewhat arbitrarily

### [11:23 - 11:25]

to roughly correspond to the surface height.

### [11:27 - 11:28]

Now that we know a bit more

### [11:28 - 11:30]

about functions of complex variables,

### [11:30 - 11:32]

let's change the color of our surface

### [11:32 - 11:34]

to correspond to the fourth variable

### [11:34 - 11:35]

we were forced to leave out

### [11:35 - 11:37]

of our three-dimensional visualization, v.

### [11:39 - 11:41]

Now that we have some idea

### [11:41 - 11:43]

of what all four variables are doing,

### [11:43 - 11:46]

let's look for the two roots predicted by Gauss.

### [11:47 - 11:49]

Remember, roots are where the output

### [11:49 - 11:51]

of our function equals zero.

### [11:51 - 11:52]

For this to be the case,

### [11:52 - 11:54]

both the real and lateral parts

### [11:54 - 11:57]

of our output variable w, u and v, must be zero.

### [11:58 - 12:01]

Seeing where u equals zero isn't too bad.

### [12:01 - 12:03]

This is where our surface intersects the z-plane.

### [12:04 - 12:07]

Now, where does v, the imaginary part

### [12:07 - 12:09]

of our output variable w, u and v, intersect?

### [12:09 - 12:09]

v equals zero.

### [12:11 - 12:12]

If we look at our color map,

### [12:12 - 12:14]

this should be where our surface is green.

### [12:15 - 12:18]

It's difficult to see exactly which shade

### [12:18 - 12:20]

of green corresponds to zero,

### [12:20 - 12:22]

so let's add a blue line to our surface

### [12:22 - 12:24]

where v equals exactly zero.

### [12:25 - 12:27]

Now, if we look closely,

### [12:27 - 12:29]

we see that both the real and imaginary parts

### [12:29 - 12:32]

of w equals zero at exactly two points,

### [12:32 - 12:35]

positive and negative i on our complex z-plane,

### [12:35 - 12:37]

exactly as our algebra predicted.

### [12:39 - 12:40]

We've found our missing roots.

### [12:41 - 12:44]

So our friend Gauss was right all along.

### [12:44 - 12:47]

Our function does have exactly two roots.

### [12:48 - 12:51]

Of course, finding these roots took some effort.

### [12:51 - 12:53]

We had to journey deep into mathematics

### [12:53 - 12:56]

and ask ourselves what a number really is.

### [12:56 - 12:58]

This led us to the strange but necessary conclusion

### [12:58 - 13:01]

that the numbers we should really be using in algebra

### [13:01 - 13:03]

are the two-dimensional complex numbers.

### [13:04 - 13:06]

This result dragged us down deeper

### [13:06 - 13:08]

into the four-dimensional world of complex functions,

### [13:08 - 13:10]

and Riemann surfaces.

### [13:10 - 13:12]

When we finally emerged,

### [13:12 - 13:14]

we saw that the algebra many of us learn in school

### [13:14 - 13:17]

is only a shadow of an elegant, powerful,

### [13:17 - 13:19]

and higher-dimensional mathematics

### [13:19 - 13:21]

that has everything to do with the numbers

### [13:21 - 13:24]

that have been given the terrible name imaginary.

### [13:24 - 13:25]

Thanks for watching.

### [13:38 - 13:41]

Subtitles by the Amara.org community
