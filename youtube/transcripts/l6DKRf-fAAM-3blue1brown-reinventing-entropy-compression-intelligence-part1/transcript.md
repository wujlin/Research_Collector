# Reinventing Entropy | Compression is Intelligence Part 1

- URL: https://www.youtube.com/watch?v=l6DKRf-fAAM
- Source: `youtube_vtt_caption`
- Caption file: `youtube/captions/3blue1brown-reinventing-entropy-compression-intelligence-part1/source.en.vtt`
- Generated at: `2026-06-13T10:24:39`

## Transcript

### [00:00 - 00:05]

[Submit subtitle corrections at criblate.com] When you encode text into binary, it's often nice to use as little data as possible,

### [00:05 - 00:08]

so you might naturally wonder, is there some kind of fundamental

### [00:08 - 00:11]

limit on how efficiently text can be compressed?

### [00:12 - 00:14]

The default encoding with ASCII is pretty inefficient.

### [00:15 - 00:17]

Each character is represented with eight full bits.

### [00:17 - 00:21]

If you apply a little cleverness associating more common characters with

### [00:21 - 00:24]

smaller bit strings, you can get this down to an average of around four

### [00:24 - 00:28]

bits per character, and then much smarter methods than that,

### [00:28 - 00:31]

that leverage patterns among long sequences of text, can get even better still.

### [00:32 - 00:33]

But again, what's the limit?

### [00:34 - 00:37]

I'm guessing many of you might have heard an estimate here,

### [00:37 - 00:40]

I will share one at the end, but much more interesting than any

### [00:40 - 00:44]

single numerical answer is how you would even approach answering it.

### [00:44 - 00:47]

This question dates back at least to the 1940s,

### [00:47 - 00:50]

with Claude Shannon's seminal work that kicked off information theory.

### [00:50 - 00:55]

Now what's very interesting is how the math that he developed to answer questions

### [00:55 - 00:59]

like this has turned out to be surprisingly useful for modern machine learning.

### [01:00 - 01:04]

To take the salient example of today, when large language models are trained,

### [01:04 - 01:08]

the pre-training portion of that is usually described as being about next

### [01:08 - 01:12]

token prediction, specifically using something called cross-entropy loss.

### [01:13 - 01:16]

Now that term, cross-entropy, has its roots in information theory.

### [01:16 - 01:19]

But what's also interesting is that one of the conclusions of information

### [01:19 - 01:23]

theory says that prediction and compression are mathematically equivalent.

### [01:24 - 01:26]

They turn out to be two sides of the same coin.

### [01:26 - 01:30]

Which means, you can entirely reframe how you think about the pre-training

### [01:30 - 01:34]

objective as not really being about next token prediction per se,

### [01:34 - 01:38]

but instead as being about creating the most efficient possible text compressor.

### [01:38 - 01:41]

Later I'll explain exactly how that works, but when you do,

### [01:41 - 01:45]

I think it offers more clarity on what this notion of cross-entropy really is,

### [01:45 - 01:46]

and why you're using it.

### [01:47 - 01:49]

Also, I don't know about you, but to me at least,

### [01:49 - 01:53]

there's just something very intriguing about using compression as a fundamental

### [01:53 - 01:55]

objective while pursuing intelligence.

### [01:56 - 02:00]

In fact, some people have gone so far as to say, compression is intelligence.

### [02:01 - 02:04]

Now, as stated, that's a hard claim to judge rigorously,

### [02:04 - 02:07]

since intelligence is such a squishy and ill-defined term.

### [02:07 - 02:10]

The safer claim would be that the mathematical theory of

### [02:10 - 02:14]

compression is bizarrely relevant to artificial intelligence.

### [02:14 - 02:17]

Still, the pithy phrase is thought-provoking, so this is the

### [02:17 - 02:21]

first in a trilogy of videos aimed at laying down the mathematical

### [02:21 - 02:24]

fundamentals to assess what this claim is really getting at.

### [02:25 - 02:29]

For the next 30 minutes or so, you and I will be focused on understanding

### [02:29 - 02:32]

the limits of compression, and seeing if we can get you to feel like you

### [02:32 - 02:36]

could have rediscovered the core idea behind Shannon's noiseless coding theorem.

### [02:36 - 02:39]

Doing so involves rediscovering a few key definitions,

### [02:39 - 02:42]

namely those of information and entropy.

### [02:42 - 02:46]

And it might sound a little weird for me to describe definitions as something to be

### [02:46 - 02:50]

discovered, but great definitions are often the residue of some kind of insight.

### [02:51 - 02:55]

See, these two specific terms are really not hard to define in the sense of

### [02:55 - 02:59]

laying down a formula for you, but doing so too early would spoil a good story.

### [02:59 - 03:02]

It is much more fun to see how you are inexorably drawn to

### [03:02 - 03:05]

them by asking about the limits of compressing language.

### [03:05 - 03:09]

And what I want you to notice by the end here is how we can't

### [03:09 - 03:12]

really answer this question, or at least Shannon couldn't,

### [03:12 - 03:16]

without necessarily engaging with some notion of intelligence.

### [03:19 - 03:23]

We will get to modelling language, which is wonderfully complicated,

### [03:23 - 03:26]

but it helps to warm up with a simpler example containing the

### [03:26 - 03:29]

same essential ideas needed for our path of rediscovery.

### [03:30 - 03:33]

Imagine you have a robot that we have sent to a faraway moon,

### [03:33 - 03:36]

whose job is to wander the surface and collect data.

### [03:36 - 03:39]

From here on Earth, we send it instructions for how to move

### [03:39 - 03:42]

that are going to be limited to four very simple possibilities.

### [03:42 - 03:46]

Move up, down, left, or right, each one with a fixed step size.

### [03:47 - 03:51]

The nuance will be that these instructions are not uniformly distributed.

### [03:52 - 03:56]

Half of everything we send is up, one fourth of the instructions are down,

### [03:56 - 04:00]

one eighth are left, and the other eighth are right.

### [04:00 - 04:03]

It's a little contrived, it's meant to be a simple example,

### [04:03 - 04:07]

and in that spirit of simplicity, we're also going to assume that every instruction

### [04:07 - 04:08]

is independent.

### [04:08 - 04:12]

They are sampled from this distribution regardless of the preceding context.

### [04:13 - 04:17]

When we send data to this bot far away, we're doing it as a stream of bits,

### [04:17 - 04:21]

ones and zeros, and it's very slow and costly to do that, so the natural question,

### [04:21 - 04:25]

the warm-up puzzle for you today, is to ask what is the most efficient

### [04:25 - 04:28]

possible way to encode these instructions as a stream of bits.

### [04:29 - 04:33]

And here, we might imagine three students who each attempt an answer,

### [04:33 - 04:38]

one who's straightforward, one who is clever, and one who is very theoretical.

### [04:38 - 04:41]

The straightforward student immediately raises their hand and says,

### [04:41 - 04:45]

well, for each of these four instructions, we could just use two bits.

### [04:45 - 04:52]

Maybe 00 encodes up, 01 encodes down, 10 encodes left, and 11 encodes right.

### [04:53 - 04:56]

On the receiving end, this makes it very easy for the robot to decode.

### [04:56 - 04:59]

It simply breaks up the bitstream into chunks of two,

### [04:59 - 05:02]

and translates each chunk into the appropriate instruction.

### [05:03 - 05:07]

Now, the clever student points out, well, that does nothing to take advantage

### [05:07 - 05:10]

of the fact that up comes up way more frequently than left or right.

### [05:11 - 05:15]

They propose a method where we use a different number of bits for each instruction.

### [05:15 - 05:18]

I'll explain it in just a second, but I do want to call out the fact that

### [05:18 - 05:22]

as soon as you let different instructions get different numbers of bits,

### [05:22 - 05:26]

it's certainly not obvious that the robot is going to know how to decode it.

### [05:26 - 05:30]

After all, it needs to somehow know where to draw the dividing lines.

### [05:31 - 05:34]

Now, being very clever, the second student has thought that through,

### [05:34 - 05:37]

but it's easiest to explain if I just kind of lay it all out.

### [05:37 - 05:41]

What they suggest is letting the single bit 0 represent up,

### [05:41 - 05:47]

letting the two bits 10 represent down, using 110 for left and 111 for right.

### [05:48 - 05:51]

You can calculate the average number of bits per instruction

### [05:51 - 05:53]

that this would require with a simple weighted sum.

### [05:53 - 05:56]

Half the time, only one bit is used, a quarter of the time,

### [05:56 - 06:00]

two bits are needed, and the remaining times, you need three bits.

### [06:01 - 06:05]

When you add this all up, as a weighted sum, you get 1.75 bits per instruction,

### [06:05 - 06:10]

which is indeed better than the more naive approach of a flat two bits per instruction.

### [06:10 - 06:14]

The second student is spending more bits on those last two instructions,

### [06:14 - 06:16]

but because they come up so much less frequently,

### [06:16 - 06:20]

this is more than made up for by using only one bit for that most common instruction.

### [06:20 - 06:24]

And you can see this efficiency bear out empirically too.

### [06:24 - 06:28]

This right here is a set of instructions sampled from that distribution.

### [06:28 - 06:33]

You'll notice lots of ups, about half as many downs, and even fewer lefts and rights.

### [06:34 - 06:38]

When you turn each symbol into the appropriate bit string following this encoding,

### [06:38 - 06:42]

the resulting sequence of bits is indeed shorter than what the naive method gave.

### [06:43 - 06:47]

But I hear some of you asking, how does the robot know how to decode this?

### [06:47 - 06:51]

Can we be sure that there's an unambiguous way to draw the dividing lines?

### [06:51 - 06:54]

In the lingo of encodings, each of these four bit strings

### [06:54 - 06:57]

used to encode the instructions is called a code word.

### [06:57 - 07:01]

And as we step through things here, see if you can figure out what rule the clever

### [07:01 - 07:05]

student was following to make sure that their code words don't conflict with each other.

### [07:06 - 07:08]

And really, you just need to look at an example bit

### [07:08 - 07:11]

stream from the robot's perspective and think it through.

### [07:11 - 07:14]

Let's say that that very first bit that it receives is a 1.

### [07:14 - 07:19]

So far, this could be encoding any of the last three instructions, down, left, or right.

### [07:19 - 07:23]

If what follows is a 0, then it can only be down.

### [07:23 - 07:25]

There is no other possibility.

### [07:25 - 07:28]

So the robot can register that as a complete instruction.

### [07:28 - 07:31]

From there, starting fresh, if what follows is a 0,

### [07:31 - 07:34]

that must be encoding up, since there is no other possibility.

### [07:35 - 07:36]

Nothing else starts with a 0.

### [07:37 - 07:39]

After that, if they see a 1, this is so far ambiguous,

### [07:39 - 07:42]

it's the prefix for any of the last three code words.

### [07:42 - 07:47]

If the next bit is another 1, it remains ambiguous, it's the prefix of the last two.

### [07:47 - 07:52]

But that following 0 then makes clear these three bits must have been encoding left.

### [07:53 - 07:56]

In short, all the robot has to do is read in the next sequence

### [07:56 - 07:59]

of bits until the moment that it forms a complete code word,

### [07:59 - 08:02]

at which point it can register it as a complete instruction.

### [08:04 - 08:08]

If you step back and think about it, the key constraint for this

### [08:08 - 08:11]

all to work is that no code word can be a prefix of another one.

### [08:11 - 08:14]

For example, let's say you tried to introduce some

### [08:14 - 08:17]

fifth instruction that had the code word 100.

### [08:18 - 08:20]

That would cause conflicts, because after reading 10,

### [08:20 - 08:23]

it's not clear whether that's supposed to be down,

### [08:23 - 08:26]

or if it's supposed to be the start of this new fifth instruction.

### [08:27 - 08:31]

When you avoid this kind of conflict, an encoding method like this has a special name.

### [08:32 - 08:36]

It's known in the business as a prefix-free code, or what is confusingly synonymous,

### [08:36 - 08:39]

it's actually more commonly known as a prefix code.

### [08:39 - 08:43]

And there's a really nice way to visualize choosing prefix-free codes

### [08:43 - 08:47]

with a certain diagram that represents every possible binary string.

### [08:48 - 08:50]

This diagram also has some helpful parallels with

### [08:50 - 08:52]

how I want to show entropy in just a few minutes.

### [08:53 - 08:56]

It's probably decently intuitive what's going on if you just pause

### [08:56 - 08:58]

and stare at it for a bit, but I'll call out the important features.

### [08:59 - 09:02]

Each layer shows every bit string of a given length,

### [09:02 - 09:07]

and you'll notice everything that starts with a 0 lives on the left half

### [09:07 - 09:11]

of this diagram, and everything that starts with a 1 lives on the right

### [09:11 - 09:12]

half of the diagram.

### [09:12 - 09:16]

And that same idea continues recursively as you go up.

### [09:16 - 09:20]

So everything starting with 00 is above this quarter of the diagram,

### [09:20 - 09:25]

everything starting with 01 is above this quarter of the diagram, and so on.

### [09:26 - 09:29]

In particular, the key property is that every binary string in

### [09:29 - 09:33]

this diagram is a prefix for everything that sits above it.

### [09:33 - 09:37]

So when our clever student chose to allocate a single bit 0 to

### [09:37 - 09:41]

represent the instruction up, they were effectively consuming half

### [09:41 - 09:44]

of the space of all possible code words by doing so,

### [09:44 - 09:50]

since everything starting with a 0 is now prohibited based on this prefix-free property.

### [09:51 - 09:55]

Similarly, allocating one 0 to down eats up another fourth of this space,

### [09:55 - 09:59]

and the remaining two instructions each eat up an eighth of the space.

### [09:59 - 10:01]

You can just see how nothing is left over.

### [10:02 - 10:07]

And at this point, I'm guessing that there's some bell kind of resonating in your mind,

### [10:07 - 10:11]

given that these proportions are all exactly the same as the

### [10:11 - 10:13]

probability for each instruction coming up.

### [10:14 - 10:18]

And in fact, that tickling sensation of a relationship between data size

### [10:18 - 10:22]

and probabilities is exactly the founding insight for information theory.

### [10:23 - 10:27]

When you stare at this pleasing alignment, it might suggest that the

### [10:27 - 10:31]

clever student's solution is not just better, maybe it's somehow perfect.

### [10:32 - 10:34]

But at the moment, that feels like a bold claim to make.

### [10:35 - 10:38]

How could you know that there's not some ultra-clever method that does

### [10:38 - 10:42]

something fancy with really long sequences of instructions that somehow

### [10:42 - 10:45]

makes it so the average bits per instruction gets even lower than this?

### [10:46 - 10:49]

This takes us to the third student, Head in the Clouds,

### [10:49 - 10:52]

who has not really been thinking about actual codes that they can implement.

### [10:52 - 10:58]

They have been pondering what properties a perfect, optimally efficient code would have.

### [10:59 - 11:02]

They have this really clever idea, which is to argue that random noise

### [11:02 - 11:06]

should be incompressible, and therefore, a perfect compression algorithm

### [11:06 - 11:10]

should produce a bitstream that's indistinguishable from random noise.

### [11:11 - 11:13]

What's neat is, even though that sounds kind of simple,

### [11:13 - 11:17]

this can actually lead you to reinventing the idea of Shannon entropy.

### [11:17 - 11:21]

Now when I say random noise, what I mean is that each bit is a 1 or a 0,

### [11:21 - 11:26]

with 50% probability, and all of the bits act independent from one another.

### [11:26 - 11:28]

It's not hard to show that our second student's

### [11:28 - 11:31]

encoding for the robot genuinely follows this rule.

### [11:31 - 11:36]

If you think about it, there's a 50% chance that the message starts with the

### [11:36 - 11:41]

instruction up, so that first bit has a 50% chance of being a 0, otherwise it's a 1.

### [11:41 - 11:45]

And then if it is a 1, there's a 50% chance that the instruction is down,

### [11:45 - 11:48]

meaning the next bit is 0, otherwise it's a 1.

### [11:48 - 11:50]

And so on.

### [11:50 - 11:54]

Each new bit really does act like an independent coin flip, so to the receiver,

### [11:54 - 11:58]

that compressed bitstream really is indistinguishable from random noise.

### [11:59 - 12:02]

But why am I saying that random noise is incompressible?

### [12:03 - 12:06]

Well, for that, let's really focus on things from the receiver's perspective.

### [12:06 - 12:09]

And here, instead of thinking instruction by instruction,

### [12:09 - 12:12]

it helps to zoom out and frame our discussion in terms of

### [12:12 - 12:15]

entire messages and what the encoding for full messages looks like.

### [12:15 - 12:20]

When that receiver sees a string of n bits representing some compressed message,

### [12:20 - 12:23]

this is one out of 2 to the n possible messages they could

### [12:23 - 12:26]

have received that would have the same size.

### [12:26 - 12:30]

And then critically, because we're assuming this looks like random noise,

### [12:30 - 12:32]

all 2 to the n of those messages must be equally likely.

### [12:33 - 12:36]

Now to be clear, we're not just talking about the robot example anymore.

### [12:37 - 12:41]

Our theoretical head-in-the-cloud student really wants to make an argument for

### [12:41 - 12:43]

what perfect compression looks like for any data type,

### [12:43 - 12:47]

like maybe we're compressing language or compressing images,

### [12:47 - 12:51]

and they want an argument that works regardless of the details of what specific

### [12:51 - 12:52]

compression algorithm you're using.

### [12:53 - 12:57]

A loose intuition in your head is that maybe among all of the messages that

### [12:57 - 13:02]

compress down to n bits, some of them would contain a larger amount of predictable data,

### [13:02 - 13:05]

while others would have started as a smaller amount of unpredictable data.

### [13:06 - 13:11]

But the key point is that if the compressed bitstream really does look like random noise,

### [13:11 - 13:14]

meaning all of the bitstrings of size n are equally likely,

### [13:14 - 13:18]

it must be the case that all the underlying messages being compressed were

### [13:18 - 13:23]

equally likely to arise, and even more specifically with probability 1 over 2 to the n.

### [13:24 - 13:26]

So again, why am I claiming that this is incompressible?

### [13:28 - 13:30]

Well, let's pull up that same diagram, representing

### [13:30 - 13:32]

the space of all possible binary strings.

### [13:33 - 13:38]

In this case, we can think of all the encodings for our 2 to the n equally

### [13:38 - 13:42]

likely messages as being the bitstrings on one layer of this diagram.

### [13:43 - 13:47]

If you tried to define an alternate scheme, where you tried to become more

### [13:47 - 13:50]

efficient by making one of these messages use fewer bits,

### [13:50 - 13:54]

it would move lower on the diagram, which means it then overlaps with some

### [13:54 - 13:58]

other message, so you would have to put that other message somewhere else

### [13:58 - 13:59]

in this diagram.

### [13:59 - 14:03]

At minimum, that means it's sharing a space with yet a third message,

### [14:03 - 14:06]

and those last two have to kind of get bumped up one layer,

### [14:06 - 14:09]

requiring that extra bit for each of them to disambiguate.

### [14:09 - 14:13]

So saving one bit over here costs you two bits elsewhere.

### [14:13 - 14:16]

You're basically pushing down a bump on the rug,

### [14:16 - 14:18]

only to see it pop up even worse in another spot.

### [14:19 - 14:24]

In general, any message encoded with a string lower on this diagram is going to be eating

### [14:24 - 14:28]

up more than its fair share of the space, which forces multiple other messages to occupy

### [14:28 - 14:33]

a smaller region, bumping them higher up, meaning they're encoded less efficiently.

### [14:33 - 14:36]

I'm going to guess that it's decently intuitive for everyone watching that

### [14:36 - 14:40]

the most efficient scheme here for equally likely messages is to give them

### [14:40 - 14:43]

all the same number of bits, but I do think the diagram gives a more

### [14:43 - 14:46]

concrete way to see why you end up with unfavorable trade-offs otherwise.

### [14:47 - 14:51]

Once you have this idea that perfect compression looks like random noise,

### [14:51 - 14:54]

this is exactly the kind of thing I was referencing in the intro,

### [14:54 - 14:56]

about how insights can lead you to definitions.

### [14:57 - 15:02]

Notice how what we're basically saying is that a message that uses n bits in a

### [15:02 - 15:07]

perfect scheme must have a probability of 1 over 2 to the n, or 2 to the negative n.

### [15:08 - 15:11]

If you take the log base 2 of both sides here and then negate,

### [15:11 - 15:15]

this is equivalent to saying that the number of bits allocated to a message,

### [15:15 - 15:19]

assuming perfect compression, is negative log base 2 of p,

### [15:19 - 15:21]

where p is the probability of occurring.

### [15:22 - 15:27]

This negative log expression is the fundamental formula for all of information theory.

### [15:28 - 15:31]

Everything up to this point is me trying to make this value feel like

### [15:31 - 15:35]

something you are inevitably drawn to by asking about perfect compression,

### [15:35 - 15:39]

rather than it feeling like some arbitrary definition that we start with.

### [15:40 - 15:43]

Some students do find this negative log takes a little getting used to.

### [15:43 - 15:47]

You know, it looks like it should be a negative value before you think about the fraction

### [15:47 - 15:51]

in the middle, but really the intuitive way to read it is that it's asking how many

### [15:51 - 15:55]

times do you chop your space of possibilities in half to get to a certain quantity.

### [15:55 - 15:59]

Here, let me pull up some axes and show you the graph of negative log of p.

### [16:00 - 16:04]

I've also seen some authors default to writing this as the log of 1 over p,

### [16:04 - 16:06]

which maybe you find more intuitive.

### [16:07 - 16:09]

You could also think of it as the log base 1 half of p,

### [16:09 - 16:11]

which I've never really seen anyone lean into,

### [16:11 - 16:14]

but personally I would be quite partial to that as a convention.

### [16:15 - 16:19]

Now, however you write it, what Shannon realized is that this is a very

### [16:19 - 16:23]

useful way to think about the information that a message contains even

### [16:23 - 16:27]

when literal perfect compression is not possible and p is no longer a clean power of 2,

### [16:27 - 16:31]

which would mean that the output here is some fractional amount.

### [16:31 - 16:35]

In fact, he defined this expression to be the information of an event.

### [16:36 - 16:41]

The image I sometimes have in my head is to picture the probability of an event

### [16:41 - 16:45]

with a little pie chart, and the information is this bar above it that gets

### [16:45 - 16:49]

kind of pumped up to be taller as the probability is squeezed closer to zero.

### [16:49 - 16:53]

That is, unlikely messages contain a lot of information,

### [16:53 - 16:57]

and the bar is relaxed to get shorter as the probability approaches 100%.

### [16:58 - 17:01]

Highly expected messages contain very low information.

### [17:02 - 17:05]

I want to be clear that there is content to this definition.

### [17:05 - 17:10]

It's more than just rescaling probabilities, as if converting to an alternate unit system.

### [17:10 - 17:12]

You've already seen the core idea.

### [17:12 - 17:16]

In a perfect compression scheme, the number of bits allocated

### [17:16 - 17:19]

to a full message precisely equals this information content.

### [17:20 - 17:22]

Now, of course, perfect compression is not always possible.

### [17:22 - 17:26]

Your probability's messages are likely not perfect powers of 2.

### [17:26 - 17:29]

So the more general way you would frame this is to say that the

### [17:29 - 17:33]

information of a message gives you a lower bound on how much it can be compressed,

### [17:33 - 17:36]

at least when you average overall possible messages.

### [17:36 - 17:40]

It's perfectly possible to overfit a compression algorithm to one specific case.

### [17:41 - 17:44]

And to really wrap your mind around information and fractional bits,

### [17:44 - 17:46]

we need to step up our game beyond that warm-up example.

### [17:47 - 17:50]

See, with the robot, the probabilities were overly clean.

### [17:50 - 17:53]

They were all perfect powers of 2, so that the information

### [17:53 - 17:55]

per symbol could precisely match a whole number of bits.

### [17:56 - 18:00]

But Shannon was very interested in this question of limits on compression

### [18:00 - 18:04]

for much more realistic and complicated cases, like natural language.

### [18:04 - 18:08]

For example, here I'll pull up the probabilities for each new letter in an

### [18:08 - 18:12]

example phrase, at least as determined by a little GPT that I'm running locally.

### [18:13 - 18:17]

And, by the way, if the probabilities provided by a model feel like those might be

### [18:17 - 18:19]

distinct from the probabilities of actual language,

### [18:19 - 18:21]

you would be right to raise an eyebrow.

### [18:22 - 18:23]

Hold on to that thought.

### [18:23 - 18:24]

It becomes very relevant later.

### [18:25 - 18:29]

One key difference with language is how heavily dependent on context everything is.

### [18:30 - 18:34]

The probability distribution for each new letter you see is highly,

### [18:34 - 18:36]

highly contingent on everything that came before it.

### [18:37 - 18:39]

The other big difference is that all of these probabilities

### [18:39 - 18:42]

are obviously not going to be clean, perfect powers of 2.

### [18:42 - 18:46]

So if you compute the Shannon information of each one of these,

### [18:46 - 18:50]

meaning you take the negative log base 2, all the numbers that you see are

### [18:50 - 18:51]

fractional amounts.

### [18:51 - 18:55]

And again, giving a vague interpretation of what these mean is really not hard.

### [18:56 - 18:59]

Information content is low for very predictable letters,

### [18:59 - 19:02]

and it's high for very unpredictable letters.

### [19:02 - 19:06]

But all of you watching this are smart enough to demand a more exact interpretation,

### [19:06 - 19:10]

one that justifies why these values deserve to be given the units of bits.

### [19:10 - 19:15]

I mean, it's not like there's going to be some perfect encoding where this

### [19:15 - 19:18]

letter i has a code word that is somehow 4.19 bits,

### [19:18 - 19:24]

or where this highly predictable o is somehow encoded with just a narrow sliver of a bit.

### [19:24 - 19:27]

The real meaning is related to encoding entire messages

### [19:27 - 19:30]

and coming up with a bound on their compression.

### [19:30 - 19:34]

The probability for a full phrase, like the one I'm showing here,

### [19:34 - 19:39]

looks like multiplying the probabilities for each successive new letter, where again,

### [19:39 - 19:43]

I'll emphasize that these successive letters' probabilities are conditioned on what

### [19:43 - 19:44]

came before.

### [19:44 - 19:46]

This is essentially the chain rule from probability.

### [19:47 - 19:50]

I want you to notice how nicely this plays with a logarithm.

### [19:50 - 19:56]

If you ask for the information of that full message, taking this negative log expression,

### [19:56 - 19:59]

because logarithms turn multiplication into addition,

### [19:59 - 20:04]

this breaks up really nicely as the sum of the information for each individual letter.

### [20:04 - 20:07]

In the final part of this trilogy, I'm going to walk you

### [20:07 - 20:09]

through a very specific compression algorithm that would

### [20:09 - 20:13]

actually compress this text to within one or two bits of this value.

### [20:13 - 20:17]

It's no longer as simple as mapping each character to a predefined code word,

### [20:17 - 20:22]

but you nevertheless get this very direct sense of thinking about adding up the

### [20:22 - 20:26]

fractional information content of each letter to determine the length of the final

### [20:26 - 20:27]

encoding that you use.

### [20:28 - 20:29]

So that's the key idea.

### [20:29 - 20:33]

Even if, by the time you need to relate this to actual data sizes,

### [20:33 - 20:35]

things will get rounded off to the nearest whole number,

### [20:35 - 20:39]

what Shannon realized is just how useful it is to work at this higher layer of

### [20:39 - 20:44]

abstraction, where all your information is allowed to freely be continuous and

### [20:44 - 20:47]

information of successive events really nicely adds together.

### [20:48 - 20:52]

Still, if you step back and imagine yourself very seriously assessing

### [20:52 - 20:55]

the fundamental compressibility of language, all of this hinges on the

### [20:55 - 20:59]

question of how you know the probabilities for each successive letter.

### [20:59 - 21:04]

Here, for all these animations, I've been illustrating things using a language model,

### [21:04 - 21:07]

but for one thing, that doesn't necessarily feel the same as the true

### [21:07 - 21:10]

probabilities underlying language, and for another,

### [21:10 - 21:13]

it's not even clear what we would mean by the true probabilities of language.

### [21:14 - 21:17]

So here, I actually think it's most enlightening to take a step

### [21:17 - 21:20]

back in time and see how Shannon himself thought about all of

### [21:20 - 21:23]

this long before language models or modern data analysis.

### [21:24 - 21:28]

Some of his earliest experiments on the information of language involved

### [21:28 - 21:30]

looking at specific short sequences of characters,

### [21:30 - 21:34]

what you often hear referred to as n-grams, and then tracking the statistics

### [21:34 - 21:36]

of what tended to follow.

### [21:36 - 21:38]

So, for example, if you scan through a few books,

### [21:38 - 21:42]

and you notice every single time the two letters th come up and you

### [21:42 - 21:45]

record what letters tend to follow, you could build up a table of

### [21:45 - 21:48]

those letters and let those statistics represent a sample for the

### [21:48 - 21:49]

probabilities you care about.

### [21:50 - 21:54]

Now, the problem is that this just completely breaks down for longer strings of letters,

### [21:54 - 21:57]

most notably, any string of text that never shows up in all

### [21:57 - 21:58]

of the books that you're analyzing.

### [21:58 - 22:01]

Nevertheless, it's perfectly reasonable to talk

### [22:01 - 22:04]

about what's expected to follow such a longer string.

### [22:05 - 22:08]

In fact, if anything, it's more important to talk about those cases,

### [22:08 - 22:12]

since longer context windows are when things are at their most predictable,

### [22:12 - 22:16]

and that's where you stand to get the most compression due to that predictability.

### [22:17 - 22:20]

So instead of using raw statistics, a little bit later,

### [22:20 - 22:24]

Shannon analyzed a different model of the English language that he had available to him,

### [22:24 - 22:25]

his wife Betty.

### [22:25 - 22:28]

As the story goes, Shannon pulled out a book and

### [22:28 - 22:31]

began asking Betty to guess each next letter.

### [22:32 - 22:34]

Shannon would then transcribe her guesses letter by letter.

### [22:34 - 22:38]

Every time she guessed incorrectly, he wrote down the correct letter,

### [22:38 - 22:42]

and then whenever she guessed correctly, he would just replace it with a dash.

### [22:43 - 22:46]

The idea was that this transcribed version he was creating has fewer

### [22:46 - 22:50]

actual letters than the original, but his point was that it contained

### [22:50 - 22:53]

the same amount of information, at least in the following sense.

### [22:53 - 22:57]

If he could somehow obtain an exact replica of his wife and conduct the

### [22:57 - 23:02]

guessing game again, he would only need to supply her with this reduced text.

### [23:02 - 23:06]

These letters by themselves would provide just the right prompting

### [23:06 - 23:08]

for his duplicate wife to exactly reproduce the original.

### [23:09 - 23:13]

Of course, in practice, a person wouldn't necessarily guess the same way twice,

### [23:13 - 23:17]

and while this qualitatively conveyed the idea of predictability allowing

### [23:17 - 23:20]

for compression, it wasn't yet a measurement of information.

### [23:20 - 23:25]

A bit later still, in his 1950 paper, Prediction and Entropy of Printed English,

### [23:25 - 23:29]

Shannon updated the experimental design to get a more robust read on this

### [23:29 - 23:33]

slippery question of the average information content in English.

### [23:33 - 23:37]

This time interviewing more people, instead of just logging whether

### [23:37 - 23:40]

each guess was right or wrong, Shannon recorded how many guesses were

### [23:40 - 23:44]

necessary for a human guesser to come up with the correct next letter.

### [23:45 - 23:48]

And then separately, he had this whole method for associating

### [23:48 - 23:51]

the number of guesses required with an implicit probability

### [23:51 - 23:54]

that a person would have been assigning to the true next letter.

### [23:55 - 23:57]

The details of that are a little bit in the weeds,

### [23:57 - 24:01]

but the broader point I want to make is how, in analyzing language,

### [24:01 - 24:04]

he wasn't just doing pure data analysis looking through books.

### [24:04 - 24:10]

He was trying to probe at an underlying model of language, namely the interviewee's brain.

### [24:10 - 24:15]

These brains that he could talk to were effectively treated as black boxes,

### [24:15 - 24:18]

ones with a sophisticated and yet indescribable understanding of

### [24:18 - 24:22]

language and an ability to predict characters based on the context.

### [24:23 - 24:26]

Now these days, in the 2020s, we have gone from merely

### [24:26 - 24:29]

interrogating black boxes that process language to designing them.

### [24:30 - 24:34]

The reason that you and I are here, revisiting the roots of information theory

### [24:34 - 24:37]

and this study of how compressible language is,

### [24:37 - 24:41]

is because of how much of the math in modern machine learning leverages the

### [24:41 - 24:43]

formulas that emerged in this field.

### [24:43 - 24:46]

Aside from the definition of information itself,

### [24:46 - 24:50]

there are three more key expressions that I want you to feel like you could

### [24:50 - 24:54]

have rediscovered, not just because rediscovery makes them more memorable,

### [24:54 - 24:58]

but because seeing how they naturally arise from studying compression gives a

### [24:58 - 25:02]

more solid ground from which you can assess that thought-provoking interplay

### [25:02 - 25:05]

between compression and intelligence.

### [25:05 - 25:09]

You already have everything you need to reinvent the first of these, which is entropy.

### [25:10 - 25:14]

Imagine you have any signal that can be thought of as a sequence of symbols,

### [25:14 - 25:17]

whether that's the four robot instructions, the English language,

### [25:17 - 25:19]

or really anything else you dream up.

### [25:19 - 25:23]

Entropy asks about the average amount of information for each symbol,

### [25:23 - 25:26]

and then based on everything we've been discussing,

### [25:26 - 25:30]

where perfect compression looks like random noise, and how, in that case,

### [25:30 - 25:34]

the number of bits used for a message is the same as the information content

### [25:34 - 25:37]

of that message, which again breaks down really nicely as the sum of the

### [25:37 - 25:39]

information of all the symbols.

### [25:39 - 25:42]

This question of measuring the average information per

### [25:42 - 25:45]

symbol is basically asking about the limit of compression.

### [25:46 - 25:50]

It would give you a lower bound on how efficiently a given signal could be compressed.

### [25:51 - 25:54]

And you and I already calculated this in one setting,

### [25:54 - 25:58]

when we took that weighted sum to find the average bits per instruction for the

### [25:58 - 26:00]

perfect encoding of the robot case.

### [26:00 - 26:03]

Basically, because that encoding was perfect, each symbol's code

### [26:03 - 26:06]

word length is exactly the same as its information content.

### [26:07 - 26:10]

So, effectively, we're calculating the average information per symbol.

### [26:10 - 26:13]

To generalize this, here's how that looks.

### [26:13 - 26:18]

For any given probability distribution, characterizing whatever symbols your

### [26:18 - 26:23]

messages are made out of, the average information per symbol should look like

### [26:23 - 26:28]

adding up p times the negative log of p for each probability p in that distribution.

### [26:29 - 26:31]

And take a moment to notice how we're visualizing this expression.

### [26:32 - 26:35]

Throughout the video, we've been picturing probability

### [26:35 - 26:38]

distributions with stacked horizontal bars, where each bar's

### [26:38 - 26:42]

width is equal to its probability, so altogether they add up to be 1.

### [26:43 - 26:48]

Now, above each one of those, I've put a rectangle whose height is locked to be

### [26:48 - 26:53]

the corresponding information value, the negative log base 2 of that probability.

### [26:54 - 26:57]

So the weighted sum up top, the average information per symbol,

### [26:57 - 27:01]

can be thought of as the total area of all these rectangles together.

### [27:02 - 27:03]

This is not yet fully general.

### [27:03 - 27:06]

It only describes the compression limit in cases where

### [27:06 - 27:09]

every new symbol follows some identical distribution.

### [27:10 - 27:13]

That's true in the robot case, but it's not true in English, for example.

### [27:14 - 27:16]

Nevertheless, it's important enough to deserve a name.

### [27:17 - 27:21]

And there's a fun story about how John von Neumann supposedly told Shannon that he should

### [27:21 - 27:24]

call this expression entropy, since, for one thing,

### [27:24 - 27:29]

it resembles an expression already used for the idea of entropy in statistical

### [27:29 - 27:32]

mechanics, and for another, quote, nobody knows what entropy really is,

### [27:32 - 27:35]

so in an argument, you'll always have the advantage.

### [27:35 - 27:38]

I looked into it, it's probably apocryphal, but

### [27:38 - 27:40]

there seems to be a grain of truth to this.

### [27:41 - 27:45]

Now, whatever the true story is, Shannon did call this quantity entropy,

### [27:45 - 27:47]

and he denoted it with the letter h.

### [27:47 - 27:49]

And it's fun to take a moment to play around with

### [27:49 - 27:51]

this graphic to build a little intuition.

### [27:51 - 27:56]

The more evenly distributed a probability distribution, the higher the total entropy,

### [27:56 - 27:59]

whereas if we squish things to become very uneven,

### [27:59 - 28:02]

maybe with one event dominating the probability space,

### [28:02 - 28:07]

this would have a very low entropy, since that one overwhelmingly probable event

### [28:07 - 28:10]

carries correspondingly little information.

### [28:10 - 28:14]

And then also, if you divide up the probability space even more,

### [28:14 - 28:17]

meaning it's distributed over more total possible symbols,

### [28:17 - 28:21]

each one has more information, so the total entropy is higher.

### [28:21 - 28:24]

And once more, it's fun to kind of slosh everything around,

### [28:24 - 28:28]

where a very skewed distribution gives lower total entropy,

### [28:28 - 28:31]

whereas a more even spread gives us higher entropy.

### [28:31 - 28:35]

The vague qualitative intuition here is that entropy measures the amount of

### [28:35 - 28:39]

uncertainty in a distribution, but the more precise understanding,

### [28:39 - 28:43]

justifying why it deserves to be given in units of bits,

### [28:43 - 28:47]

is that it describes the minimum number of bits per symbol necessary to encode

### [28:47 - 28:49]

a message following this distribution.

### [28:50 - 28:53]

That statement, and everything we just covered,

### [28:53 - 28:56]

is more or less the content of a core theorem in Shannon's

### [28:56 - 29:00]

1948 paper that kicked off information theory, the noiseless coding theorem.

### [29:00 - 29:04]

It states that no encoding can ever be more efficient than this limit,

### [29:04 - 29:09]

and even more strongly, he showed that it's always possible to get arbitrarily close

### [29:09 - 29:10]

to this limit.

### [29:11 - 29:16]

Now like I said, this expression only applies in cases where every symbol follows the

### [29:16 - 29:20]

same distribution, but Shannon was of course keenly interested in a more general

### [29:20 - 29:24]

setting, where the probabilities for each new symbol don't necessarily follow the same

### [29:24 - 29:25]

distribution.

### [29:25 - 29:28]

In particular, he spent a ton of time contemplating

### [29:28 - 29:30]

the compressibility of natural language.

### [29:31 - 29:33]

This requires a more general notion of entropy,

### [29:33 - 29:36]

something known as the entropy rate for a stochastic process.

### [29:36 - 29:38]

But it's the same basic question.

### [29:38 - 29:41]

What is the average information per symbol, except in

### [29:41 - 29:44]

this case we're now averaging over all possible messages.

### [29:45 - 29:48]

This is almost never a clean calculation that you can perform

### [29:48 - 29:51]

with some clean visual like the one we were just playing with.

### [29:51 - 29:55]

After all, what formula describes the probability distribution for language?

### [29:56 - 29:59]

So if you hear reference to the entropy of language,

### [29:59 - 30:03]

this is well beyond what any exact calculation can give you,

### [30:03 - 30:06]

hence why Shannon turned to estimates based on observation.

### [30:06 - 30:10]

And again, his methodology was not just data analysis.

### [30:10 - 30:13]

It's not some function that you can perform on a corpus of text.

### [30:14 - 30:17]

In order to get a satisfying estimate on compressibility,

### [30:17 - 30:21]

he found himself inevitably needing to probe at intelligent models of language.

### [30:22 - 30:26]

When his interviewees had at least 100 preceding letters of context,

### [30:26 - 30:29]

he estimated the entropy of English to be about one bit per character.

### [30:30 - 30:33]

This is a pretty wild number when you think about it,

### [30:33 - 30:37]

because it suggests that English could be compressed down to just a single yes or

### [30:37 - 30:38]

no answer for each character.

### [30:39 - 30:43]

Wild as that sounds, in the third part here, I will show you that algorithm I've

### [30:43 - 30:46]

referenced, where if you're allowed to use a high-quality language model for

### [30:46 - 30:50]

encoding and decoding, you can get surprisingly close to this limit in practice.

### [30:51 - 30:56]

Before then, it helps to understand a variation on entropy, known as cross-entropy,

### [30:56 - 31:00]

asking both how and why it's used in training large language models.

### [31:00 - 31:04]

If you want to learn that, as well as a few fun related ideas like how

### [31:04 - 31:07]

large models are distilled into smaller ones,

### [31:07 - 31:11]

and why on earth GZIP can recover the structure between distinct languages,

### [31:11 - 31:12]

come join me in part 2.

### [31:14 - 31:18]

Regular viewers will know that my new experiment for this

### [31:18 - 31:21]

year is to have a virtual career fair, a page at 3b1b.co.

### [31:21 - 31:25]

talent, where this audience can explore aligned career opportunities.

### [31:25 - 31:28]

The meaningful update is just how much more content there is now,

### [31:28 - 31:32]

mainly in the form of featured interviews between me and the relevant teams.

### [31:33 - 31:33]

Here's my thinking.

### [31:34 - 31:36]

I feel like when you're assessing potential jobs,

### [31:36 - 31:40]

it's almost impossible to get a true sense of what it's like to work at a place just by

### [31:40 - 31:44]

poking around online, and you learn orders of magnitude more if you have a chance to sit

### [31:44 - 31:46]

down for lunch with a couple team members.

### [31:47 - 31:49]

My hope is to give you the vicarious version of that.

### [31:50 - 31:54]

So, if you're curious what I mean when I say these are all thoughtful and curious teams,

### [31:54 - 31:55]

go take a moment to explore.

### [31:55 - 31:56]

I really think you'll enjoy it.
