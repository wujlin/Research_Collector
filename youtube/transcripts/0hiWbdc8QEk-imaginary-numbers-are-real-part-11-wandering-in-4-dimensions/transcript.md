# Imaginary Numbers Are Real [Part 11: Wandering in 4 Dimensions]

- URL: https://www.youtube.com/watch?v=0hiWbdc8QEk
- Model: `large-v3`
- Requested language: `en`
- Detected language: `en`
- Generated at: `2026-05-07T14:29:42`

## Transcript

### [00:00 - 00:04]

Last time, we left off trying to think of shapes to draw on our input plane that would

### [00:04 - 00:10]

help us better understand our function f of z equals z squared plus one. Since z squared

### [00:10 - 00:15]

means to multiply z by itself, and z is a complex number, our function's behavior

### [00:15 - 00:21]

should have some connection to complex multiplication. Back in part 7, we saw that one way to interpret

### [00:21 - 00:27]

complex multiplication is as a rotation and scaling of our input values. When we multiply

### [00:27 - 00:33]

two complex numbers together, their magnitudes multiply and their angles add. So the z squared

### [00:33 - 00:38]

part of our function should take our complex number z, square its distance to the origin,

### [00:38 - 00:44]

and double its angle. The plus one portion of our equation is a little less exciting.

### [00:44 - 00:49]

Adding a positive real number will move all of our points in the positive real direction,

### [00:49 - 00:54]

so to the right, in this case, by one. Since this shift to the right doesn't affect the

### [00:54 - 00:56]

behavior we're interested in, we'll leave it out of the equation.

### [00:57 - 01:04]

Let's test the idea that our function will double the angle of its input values. What

### [01:04 - 01:08]

kind of shape should we draw to test this idea? Ideally, we want to draw a shape that

### [01:08 - 01:13]

is made up of points that are all at the same angle, to see if our function changes all

### [01:13 - 01:18]

points of the same angle in the same way. So what kind of shape is made up of points

### [01:18 - 01:24]

all at the same angle? This turns out to be a straight line through the origin. If we

### [01:24 - 01:26]

draw a line like this in our input space,

### [01:26 - 01:31]

we see that the output is also a straight line, at what looks like double the angle.

### [01:31 - 01:36]

We can add a few more lines to confirm this trend.

### [01:36 - 01:41]

So we've shown that our transformation doubles the angle of our input values. Now, what about

### [01:41 - 01:47]

the magnitude of our inputs? We said earlier that when squaring a complex number, the magnitude

### [01:47 - 01:53]

of the complex number should also be squared. So the distance to the origin from our input

### [01:53 - 01:56]

points should be squared in our mapping.

### [01:56 - 02:01]

What kind of shape should we draw to test this idea? We want to test magnitude alone,

### [02:01 - 02:06]

so it would be nice to have a shape with a constant magnitude. What kind of shape has

### [02:06 - 02:12]

the same magnitude, or distance to the origin, everywhere?

### [02:12 - 02:18]

The shape we need is exactly a circle. If we add sections of a few circles to our picture,

### [02:18 - 02:24]

we see that these result in new circle sections, but now at different distances to the origin.

### [02:24 - 02:26]

So as we expected, our circles are preserved,

### [02:26 - 02:29]

but their radii are changed.

### [02:29 - 02:34]

Now we're really getting somewhere. By carefully choosing our input shape, we were able to

### [02:34 - 02:39]

better understand exactly what our function does to complex numbers. Wonderful.

### [02:39 - 02:44]

But before we celebrate here, let's keep a couple things in mind. For one, we're dealing

### [02:44 - 02:50]

with a really simple function. And secondly, even for this simple function, we can still

### [02:50 - 02:55]

run into trouble with our too complex plane setup. For example, we know that our mapping

### [02:55 - 02:56]

doubles the angle of the input point.

### [02:56 - 03:02]

This is fine, until we use up too much of our input space. If we continue the circles

### [03:02 - 03:08]

we started earlier, once we arrive at 180 degrees, we begin to see a problem. Our shapes

### [03:08 - 03:13]

have been expanded to fill up the entire output space, but we've only used half of the input

### [03:13 - 03:19]

space. As we continue our circles, our new points have nowhere to go except directly

### [03:19 - 03:24]

on top of our old points. This does make sense algebraically, because of the way squaring

### [03:24 - 03:25]

works.

### [03:25 - 03:30]

Points like 1 plus i and negative 1 minus i will map to the same exact output value,

### [03:30 - 03:33]

namely 2i.

### [03:33 - 03:37]

So it's not that our function is broken or anything. It's just that the technique we're

### [03:37 - 03:42]

using to visualize it can't really handle multiple values being mapped to the same location

### [03:42 - 03:47]

on the output plane. After all, which pixel should we display? The one from here, or the

### [03:47 - 03:50]

one from there?

### [03:50 - 03:54]

Mappings like this create problems in mathematics, although typically in the reverse direction.

### [03:55 - 04:00]

The reverse of a function, where the inputs become outputs and the outputs become inputs,

### [04:00 - 04:05]

is called the inverse. The inverse of our function is pretty straightforward to find.

### [04:05 - 04:09]

We simply need to solve our equation for z.

### [04:09 - 04:14]

We now run into the real math problem. Our inverse function represents the same exact

### [04:14 - 04:19]

connections as our forward function, just in the opposite direction. So our two inputs

### [04:19 - 04:25]

that map to the same output are now a single input that maps to two outputs.

### [04:25 - 04:32]

The w value of 2i maps to both z equals 1 plus i, and z equals negative 1 minus i.

### [04:32 - 04:37]

This mapping from a single input to multiple outputs is a big enough problem that our function's

### [04:37 - 04:43]

inverse is not technically even considered a function. The definition of a function requires

### [04:43 - 04:47]

that each input be mapped to one and only one output.

### [04:47 - 04:52]

To make things nice and confusing, non-functions like this are called multifunctions. So our

### [04:52 - 04:54]

mapping is the same in either direction, but taken from the reverse direction. The inverse

### [04:54 - 04:55]

of a function is a function that maps to two outputs. The inverse of our function is a

### [04:55 - 04:59]

function, but taken from z to w is considered a function, but from w to z is considered

### [04:59 - 05:04]

a multifunction, which isn't really a function.

### [05:04 - 05:09]

Let's experiment with our multifunction. When we draw shapes on our w plane, our shapes

### [05:09 - 05:14]

are duplicated and shrunk down onto our z plane. Our shapes are copied because each

### [05:14 - 05:19]

point in w is mapped to two points in z, and shrunk because the square root function takes

### [05:19 - 05:24]

the square root of the magnitude of our w values and divides each angle by 2.

### [05:25 - 05:31]

Let's experiment with one more type of shape, a path. We'll pick a starting point

### [05:31 - 05:36]

on our w plane, wander around for a while, and return to where we started. By following

### [05:36 - 05:42]

paths on both our w and z planes, we can get some idea of what happens as we wander around

### [05:42 - 05:48]

the 4-dimensional space of our complex multifunction. Our first path returns us right back to where

### [05:48 - 05:54]

we started on both the z and w plane. No surprise there. But if we change our path a little,

### [05:54 - 06:01]

something weird happens. Our w path returns to where we started, but our z paths don't.

### [06:01 - 06:06]

Our z values jump to a whole new part of the plane. Somehow we've wandered our way into

### [06:06 - 06:12]

a completely new part of our multifunction. So it seems that some paths on w lead us back

### [06:12 - 06:18]

to where we started, but others don't. What could be going on here? How is the complex

### [06:18 - 06:23]

landscape of our multifunction taking such similar paths in such different directions?

### [06:24 - 06:29]

One reason I like math is that for many problems, someone much smarter than me has already given

### [06:29 - 06:34]

them some serious thought, and quite often found an elegant solution. In this case, that

### [06:34 - 06:39]

person was one of Gauss's students, Bernhard Riemann. We'll discuss his solution next

### [06:39 - 06:44]

time.

### [06:44 - 06:49]

If you're still watching, here's a quick bonus feature. A very slick way of visualizing

### [06:49 - 06:53]

functions of complex variables is to do this.

### [06:53 - 06:54]

This technique is called Domain Comparison.

### [06:54 - 06:54]

This technique is called Domain Comparison. This technique is called Domain Comparison.

### [06:54 - 06:54]

This technique is called Domain Comparison. This technique is called Domain Comparison.

### [06:54 - 06:57]

Domain Comparison. And I just had a little insight into that in hanover, here..

### [06:57 - 07:01]

If we follow a path around the z-plane, we can learn a tremendous amount about how our

### [07:01 - 07:03]

complex function works.

### [07:03 - 07:10]

If we follow a path around the z-plane, we can learn a tremendous amount about how our

### [07:10 - 07:12]

complex function works.

### [07:12 - 07:16]

For example, we can really get a feel here for how the square root function unfolds our

### [07:16 - 07:19]

w-plane into two copies of itself.

### [07:19 - 07:23]

If we follow a path around the z-plane, we encounter every color twice.

### [07:23 - 07:24]

We can compare these problems in each other.

### [07:24 - 07:29]

place to start. Okay, the video is actually over. Stop watching.
