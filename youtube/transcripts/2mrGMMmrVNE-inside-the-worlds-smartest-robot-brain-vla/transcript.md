# Inside the World's Smartest Robot Brain [VLA]

- URL: https://www.youtube.com/watch?v=2mrGMMmrVNE
- Model: `youtube-auto-caption-json3`
- Requested language: `en-orig`
- Detected language: `en`
- Refined at: `2026-06-05T08:19:37`

## Transcript

### [00:00 - 00:31]

This may be the most significant moment in modern robotics. In 2023, a researcher at Google set up a table with a Coke can, pictures of Tom Cruise, Snoop Dogg, and Taylor Swift, and asked Google's newest robot brain, RT2, to move the Coke can to Taylor Swift. RT2 was too large to run on the robot itself. The robot sent one image at a time from its onboard camera to a TPU cluster, which sent back control signals.

### [00:29 - 00:56]

The robot controlled by RT2 slowly picked up the Coke can and awkwardly placed it on the edge of the picture of Taylor Swift. A couple years later, in 2025, one of the researchers on the team, Carol Hausman, would describe this scene as the moment it became clear to him that this was going to work. Within a year of the 2023 Coke can demo, Hausman and many of the key members of the RT2 team had left Google,

### [00:55 - 01:23]

and reassembled to form a startup called Physical Intelligence. And their robots have gotten better, a lot better. The latest robot brains from Physical Intelligence can open padlocks, fold your laundry, peel an orange, make a grilled cheese sandwich, make coffee, and clean up bedrooms and kitchens that it's never seen before. Why was this unimpressive Coke can demo such a breakthrough? And how did it enable Physical

### [01:21 - 01:52]

Intelligence to improve their robots so rapidly? In this video, we'll first explore the fascinating build-up to RT2 at Google. From here, we'll take a deep dive into the Physical Intelligence Robotics Foundation Models, and see what makes these incredibly impressive robot brains tick. In 2022, the year ChatGPT was released, researchers at Google began exploring what role large language models might play in robotics.

### [01:50 - 02:18]

Their first notable result, a system known as SayCan, used a large language model as a planning system to break down complex tasks into subtasks. In this demo, SayCan breaks down cleaning up a spill into the subtasks of finding a sponge, picking up the sponge, going to the spill, and so on. From here, the team expanded on this work, creating a more capable iteration of the idea called inner monologue, and

### [02:16 - 02:43]

another interesting variant where the team used an LLM to write code to control the robot on the fly. However, these early efforts were effectively bottlenecked by the available robot controls algorithms. Once the LLM in SayCan decided to pick up a sponge, a completely separate neural network that had been trained to imitate humans controlling robots to perform various small tasks, was used to

### [02:41 - 03:10]

compute the actual robot control signals. This meant that SayCan was effectively limited to a menu of actions the LLM could choose from. To get SayCan to place a Coke can on an image of Taylor Swift, behaviors involving Coke cans and Taylor Swift would have to be explicitly trained. At the end of 2022, the team made a significant improvement to their control layer, introducing Robot Transformer 1, or RT1.

### [03:09 - 03:39]

Like the team's previous control algorithms, RT1 was trained to imitate humans, but used a significantly larger dataset, with over 130,000 human demonstrations, and used a larger transformer-based architecture. RT1 was able to perform a significantly broader range of actions than its predecessors. This effectively gave the planning layer a much larger menu of actions to choose from. The RT1 team showed that using the

### [03:36 - 04:08]

planning LLM from SayCan, coupled with RT1 to control the robot, significantly improved performance on long-horizon tasks, like finding certain items in kitchens that the robot hadn't seen before. As Google incrementally improved their robot brains, large language models were also rapidly advancing. The LLM used for planning in the SayCan and RT1 systems was the text-only Palm 540B model, trained in early 2022.

### [04:07 - 04:34]

This meant that the robot's planning layer couldn't actually see the world. After breaking down a task like helping clean up the kitchen into text subtasks, Google's robots relied on the RT1 control layer to take in images from the robot's camera, and iteratively send control signals to the robot's actuators, until each subtask was complete. This approach worked fine for some tasks, but having a planning layer that

### [04:32 - 05:02]

was effectively blind was clearly not ideal. On March 6th, 2023, about a week before the release of GPT-4, Google researchers demonstrated Palm-E, a variant of the Palm large language model that directly incorporated images and other data sources. Using the multimodal Palm-E instead of the purely text-based Palm LLM as a planner, with RT1 as the control layer, the team demonstrated a significant

### [05:00 - 05:27]

expansion in capabilities. Now that the planning layer had access to vision information, the robot could perform more complex tasks that require adaptive planning, like moving objects out of the way to reach a desired object, and fully autonomously recovering from setbacks. Here, a robot using Palm-E as its planning layer and RT1 as its control layer, is asked to retrieve a bag of chips.

### [05:25 - 05:52]

And when a researcher repeatedly puts the chips back in the drawer, Palm-E is remarkably able to recognize that something has changed and adapt its plan. Now, let's zoom out a little and consider the full Palm-E plus RT1 robot brain. Although Palm-E and RT1 were designed to work at different levels of the stack, they have some really interesting similarities. Both models take in images from the

### [05:50 - 06:18]

robot's camera, and use a vision encoder neural network to process the images. From here, in both models, these encoded image representations are passed into a transformer. This is the same type of compute block used fairly universally in large language models. The big difference here is what these transformers are trained to do. The RT1 transformer was trained to directly output robot control signals by

### [06:16 - 06:46]

imitating humans controlling robots to solve various tasks. While the Palm-E transformer is trained to output text across a wide variety of tasks, including simple next token prediction on internet text, as we see in standard LLM pretraining, but also language-vision tasks, like image captioning. And importantly, Palm-E was also trained to break apart robotics tasks into smaller subtasks.

### [06:43 - 07:14]

The similarities between Palm-E and RT1, and the fact that the team was able to expand the Palm language-only model to effectively make use of other types of data, all beg the question, do we really need two separate models here? Why not just continue expanding the Palm language model to not only take in image data, but also to directly output robot control data, effectively absorbing RT1 into a single

### [07:11 - 07:44]

powerful end-to-end model? Said differently, can large language models, by far the most powerful AI systems we trained so far, be trained to become robot brains? This brings us to Taylor Swift and the Coke can. In July 2023, a few months after the Palm-E paper came out, the Google Robotics team demonstrated RT2. Taking Palm-E and another multimodal LLM known as PaLI-X as starting points,

### [07:42 - 08:14]

the Google team trained these LLMs to directly output robot control signals, training on the same human control demonstration data they had used to train RT1 6 months earlier. And incredibly, it worked. RT2 was able to generalize shockingly well to objects, environments, and tasks that were not in the human demonstration data. This is what makes the Taylor Swift demo so impressive. The robot control training data

### [08:11 - 08:40]

definitely did not include Taylor Swift. So, for RT2 to solve this task, it had to learn how to bring together abstract concepts it had learned in its internet-scale pretraining with the robot control episodes. This means that these models can learn to connect the vast amounts of image, video, and text data on the internet with real-world actions, potentially harnessing the full knowledge of the internet into robot

### [08:38 - 09:11]

brains. This is why this demo is such a big deal. It answers the question, can large language models be trained to be robot brains? With a shaky, but definitive, yes. The RT2 team coined a new name for this type of model, vision-language-action, or VLA, linking together vision, language, and action into a single unified model. This video is about to get technical. To see how language models can learn to

### [09:08 - 09:36]

become robot brains, we're going to reference transformers, embedding vectors, diffusion models, attention heads, softmax, and more. The required context for all these concepts is way more than we can fit into a single video, which is why I wrote this book. The Welch Labs Illustrated Guide to AI breaks down all of these concepts using hundreds of figures, detailed descriptions, and exercises.

### [09:33 - 10:00]

You can pick up a copy at welchlabs.com. And we're very excited to announce that we're beginning to offer international shipping. Stay tuned to the end of the video for more updates on the book, and to see the poster that goes along with this video that nicely breaks down the vision-language-action model architecture. By early 2024, a number of key members of the RT2 team had left Google and

### [09:58 - 10:27]

reassembled to form the startup Physical Intelligence. In October of that year, the team demoed their first robot brain, Pi Zero. Compared to the RT2 Coke can Taylor Swift demo 15 months before at Google, Pi Zero is remarkable. It starts to really feel like a robot that could help you around the house, performing tasks like getting laundry out of the dryer, folding the laundry, and cleaning up tables.

### [10:25 - 10:57]

How was the Physical Intelligence team able to improve on RT2 so significantly and so quickly? Like RT2, Pi Zero is a vision language action model built on top of a pre-trained multimodal LLM. Based on Pi Zero's strong performance, you might guess that the Physical Intelligence team increased the model size relative to RT2, but Pi Zero is actually smaller. The RT2 model family ranged from 5 to 55

### [10:55 - 11:28]

billion parameters, and Pi Zero remarkably only uses 3.3 billion parameters, allowing the model to run on the robot itself using a consumer-grade Nvidia RTX 4090 GPU at a very respectable 73-millisecond inference time. Here's what Pi Zero looks like hooked up to a two-arm robot platform called ALOHA and tasked with uncapping a pen. Pi Zero takes images from an overhead camera and from one camera on the wrist

### [11:24 - 11:57]

of each robot arm and a text prompt. At each time step, Pi Zero returns 14 numbers. One number for the position of each of the seven actuators on each arm. Here we're plotting these outputs as a time series. This movement in our pink curve here shows us where Pi is telling the left gripper to grab onto the pen cap. Pi Zero is built on top of PaliGemma, an open-weight multimodal LLM from Google.

### [11:55 - 12:24]

PaliGemma is built from two other open-weight models, the SigLIP image encoder and the Gemma large language model, that are trained together to solve vision language tasks like image captioning. Now, following the RT2 approach, the underlying language model, in this case PaliGemma, would be trained to directly output control values. However, the Physical Intelligence team made a clever improvement here that

### [12:22 - 12:49]

makes Pi Zero significantly better at dexterous manipulation. Instead of having the underlying language model directly output control values, Pi Zero introduces a second neural network the team calls an action expert. Interestingly, the Pi Zero action expert uses the same architecture as Gemma. In fact, in the Pi Zero code base, the action expert is instantiated as a Gemma model.

### [12:47 - 13:13]

The only differences are that the action expert is randomly initialized instead of pre-trained, and the action expert is not as wide as Gemma, using fewer parameters within each layer. Now, this may sound like we're going back to the earlier SayCan system, where a high-level LLM performed planning and a lower-level network handled robot control. The key distinction here is that in the

### [13:11 - 13:40]

SayCan system, the interface between models was natural language. The planning LLM told the control network what to do using predetermined text instructions. Pi Zero, in contrast, uses a much richer interface between the two models. Since the Gemma LLM and action expert effectively share the same architecture, it's possible for these models to almost think as one while retaining some really nice

### [13:37 - 14:08]

benefits of modularity. Let's have a closer look at how our Gemma LLM learns to act as a robot brain. Then we'll have a closer look at how the interface between these two models works. The Gemma LLM processes both the images and text prompts that come into Pi Zero. Each image is broken into a grid of patches, resulting in 256 image patches per image and 768 total patches. The patches from each image are passed

### [14:05 - 14:36]

into an image encoder model, resulting in 768 embedding vectors, each of length 2048. These vectors are sometimes referred to as soft tokens. Here we're coloring each embedding vector to approximately match its corresponding image patch. This will help us keep track of our data as it flows through our model. These embedding vectors live in a semantically rich embedding space, meaning they should contain lots of

### [14:34 - 15:03]

easily accessible information about our images, like whether a given image patch contains a pen. For more on embedding spaces and image encoders, check out the Welch Labs video on AlexNet, the AI image generation video we did with Three Blue One Brown, or the Welch Labs illustrated guide to AI. The text prompt we give Pi Zero, in this case uncap the pen, is broken into four tokens, and each

### [15:01 - 15:33]

token is mapped to an embedding vector of the same length as our image patch embedding vectors. So, we now have 772 total embedding vectors, 768 from our images and four from our text prompt. From here, these embedding vectors are passed into our Gemma LLM. Gemma is composed of 18 transformer blocks, each containing an attention and multi-layer perceptron compute block. Each attention block contains eight

### [15:31 - 16:03]

attention heads. These attention heads are arguably the most critical part of the transformer architecture and are the key to the tight integration between Pi Zero's underlying LLM Gemma and Pi Zero's action expert. In a given attention head, the incoming embedding vectors are multiplied by three separate matrices of learnable weights, producing three new matrices known as queries, keys, and values.

### [15:59 - 16:31]

Each of these matrices has 772 rows, one for each input to our transformer. We don't have enough space to visualize all 772 rows of our matrix. Here we're showing the first row, which corresponds to the upper left patch of our overhead image. Next, we're showing rows 373 to 376, which correspond to these four patches of our left wrist image. This will be important shortly as we see

### [16:29 - 16:55]

how Gemma figures out how to connect the word for pen to the parts of the images that contain the pen. As we did with our embedding vectors, we'll color each row of our matrix with the approximately average color from its corresponding image patch. Our two patches that contain the orange pen get colored orange. And finally, the light and dark parts of each vector correspond to the actual

### [16:52 - 17:20]

numerical values of the vector. Dark regions are lower numbers and light regions are higher numbers. Finishing out our matrix, these last four rows come from our input text with one row for each token, and we'll color all our text rows blue. From here, Gemma's attention head searches for similar query and key matrix rows. This attention head may have learned, for example, to specialize in searching

### [17:18 - 17:50]

the incoming images for objects that match words that appear in the prompt. After all, if our robot brain is going to uncap the pen, it needs to know where the pen is in our images. The word pen shows up at our very last token input position, and its query vector looks like this. The attention head computes the dot product between this row and every row in our key matrix, and larger dot products indicate closer

### [17:46 - 18:16]

matches between queries and keys. Interestingly, our highest dot products in this sample by far occurred at two image patches that contain the pen. From here, our attention head normalizes these dot product values using a softmax operation. We can take our visualization one step further here and show these attention values as a heat map on top of our images, where brighter shades of magenta

### [18:12 - 18:41]

correspond to larger attention values. So, the two orange rows of our key matrix with high attention values that correspond to these two image patches get colored bright magenta, and their neighboring patches with low attention scores do not. So, the idea here is that our heat map visualization shows us the strongest matches in our images to our query vector for the word pen in our prompt.

### [18:38 - 19:10]

And remarkably, our best matches occur at the patches in all three images that show the pen. Playing our video and running this analysis at each frame, we see impressive pen tracking results. Our model is clearly using this attention head to connect the word pen in our prompt to the parts of our images that contain the pen. Now, our attention head doesn't just search for matches to our pen query.

### [19:06 - 19:37]

All 772 query vectors, corresponding to all input images and prompt tokens, are compared to all 772 key vectors. The resulting attention values from all these comparisons are collected in a 772 by 772 attention pattern matrix. Each row of the attention pattern corresponds to a single query. The final query row corresponds to the pen token in the prompt that we've been visualizing.

### [19:36 - 20:05]

So, our heat map values end up in the bottom row of our attention pattern. At the beginning of our attention head, we computed three matrices, our queries, keys, and values. We've used our queries and keys to create our attention pattern, and now our attention pattern is multiplied by our value matrix, creating this attention heads output, a new 772 by 256 matrix. Multiplying our value matrix by our

### [20:03 - 20:32]

attention pattern effectively moves information between token positions. The large attention values we see between our pen query and pen image patches mean that these image patch rows are copied and added to the pen position in our final output. One way to think about this operation is that our attention head is forming a unified representation of the text for pen and the parts of our images that contain pens.

### [20:30 - 20:56]

Now, this is just a single head in a single layer of our 18-layer Gemma LLM. And we expect different heads to learn to pick up on different types of patterns. And remember that our Gemma LLM is just one part of the Pi Zero system. Let's now turn to Pi Zero's action expert model and see how the Physical Intelligence team was able to get these models to work together so seamlessly.

### [20:55 - 21:25]

While the PaliGemma portion of Pi Zero takes in our 772 image and text prompt tokens, the action expert takes in information about our robot state. That is the position of all of its joints. On the ALOHA platform we've been experimenting with, each arm has a movable waist, shoulder, elbow, forearm rotation, wrist, wrist rotation, and gripper. This makes for seven joints per arm or

### [21:22 - 21:50]

14 total numerical values that we need to control our robot. Just as our text prompt and input images are mapped to embedding vectors, our vector of 14 joint positions is also mapped to an embedding vector. This mapping is done by multiplying our joint vector by a 14 by 1024 matrix of learned weights. Note that while the Gemma LLM in Pi Zero uses an embedding vector of length 2048,

### [21:49 - 22:19]

the action expert uses embedding vectors of length 1024. This reduces the compute requirements and inference time of the action expert model. So the robot's current state fits into a single embedding vector or soft token. This is one of the inputs to our action expert. The action expert has one more set of inputs, the joint positions of the robot over the next 50 time steps, generally referred to as actions.

### [22:17 - 22:46]

Now, this might seem backwards. The whole point of the action expert is to predict the future robot actions. How could the model take predicted actions as an input? In a fascinating transfer of ideas from AI video and image generation, Pi Zero's action expert uses a method called flow matching. The idea is that instead of outputting robot actions in one go, the model iteratively shapes completely random

### [22:43 - 23:13]

actions into a final trajectory. The comparison to AI image generation is really interesting here. A final set of actions produced by our action expert will be of dimension 14 by 50, with one row to control each robot joint and one column for each of the next 50 time steps. We can visualize this matrix as an image, as we have with other matrices in our model. In this set of actions, we see an

### [23:10 - 23:41]

increase in the values in our ninth row. We can plot these values as a time series. This set of actions is telling our robot to move its right shoulder, reaching its right gripper towards the pen. In AI image generation, we can create an image of a cat by iteratively refining a pure noise image into a detailed cat image. Pi Zero's action expert does the same thing, refining a 14 by 50 random image of

### [23:38 - 24:07]

joint trajectories into a detailed plan for how to move each robot joint. One reason this flow matching or diffusion process works so well for generating natural images is that the distribution of natural images is multimodal. There are many ways to create an image of a cat. Analogously, there are many ways we can move our 14 robot joints to uncap a pen. So to generate a set of actions, the

### [24:05 - 24:32]

action expert starts with completely random actions and predicts how these actions should be updated to produce a slightly more realistic and accurate set of trajectories. These trajectories are added to the input actions and then passed back into the model, which then computes a new set of updates. This process is repeated 10 times in Pi Zero until we have a nice set of trajectories.

### [24:30 - 24:56]

The fact that we can use the same exact flow matching process to generate images and videos and control robots is so interesting to me. It's such a surprisingly effective abstraction on top of what feel like very different applications of AI. So our action expert model can iteratively shape pure noise into robot trajectories. But how does it know what trajectory is to generate?

### [24:55 - 25:22]

The action expert needs to know what the goal is, in the case of our example, uncapping the pen. And of course, it needs lots of information about the scene, like where the pen is in space. As we saw earlier, this is exactly the type of information our Gemma LLM is already processing in its attention heads. The question from here is, how do we best give our action expert access to this information?

### [25:21 - 25:52]

As we saw earlier, the action expert uses the same architecture as our Gemma LLM. This means that like Gemma, our action expert has 18 attention blocks with eight attention heads each. As we saw earlier, each Gemma attention head computes a separate query, key, and value matrix. Our action expert attention heads perform the same operations, but with different inputs. Our action expert has 51 inputs, one for

### [25:50 - 26:19]

the robot's current state, and 50 for the robot's predicted actions over the next 50 time steps. So within each attention head, our action expert's query matrix will have 51 rows, one for each model input. Now, using the standard attention mechanism, each query is able to search for matches in the keys. This could allow, for example, our second action step to use information from our first action step,

### [26:17 - 26:43]

which would help our model create a nice smooth trajectory from time step to time step. Of course, to figure out where these trajectories should go at all, our action expert's queries ideally need access to the prompt and image information from our Gemma LLM. This is where the team's decision to use the same architecture for the LLM and action expert really pays off. All we have to do at this stage is take

### [26:41 - 27:12]

the keys and values from the corresponding attention head of our Gemma LLM and append them to the keys and values from our action expert. So we now have 51 plus 772, making for a total of 823 keys that our action expert can query. These keys contain all the information the action expert needs, the text prompt, the encoded images, the robot state, and other time steps in the planning process.

### [27:11 - 27:39]

This gives the attention heads in our action expert an immediately available, incredibly rich information source. It's a really clever design. This modular design allows for some impressive efficiency gains. After the images and prompt are passed into PaliGemma, the computed keys and values in each attention head are cached. This is a common step in LLM inference, preventing redundant computation as new

### [27:37 - 28:06]

tokens come along. However, in this case, the Physical Intelligence team uses PaliGemma's KV cache to feed into each action expert's attention head. Since the action expert uses a flow matching process, it needs to run multiple times to produce final smooth trajectories, but is able to use the same KV cache each time because the input images don't change until the next time step.

### [28:05 - 28:32]

The fact that all these components can be trained to work together so well is absolutely incredible. At each step, Pi Zero takes in its prompt and images, runs them through PaliGemma, caches all the key and value matrices, and then runs the action expert to iteratively denoise random trajectories into final paths. The robot then follows these paths for a few steps, and the process is repeated,

### [28:30 - 28:59]

controlling the robot to achieve the task at hand. Since Pi Zero was first demoed in October of 2024, the Physical Intelligence team has made various improvements to their models and training approach, but their core VLA architecture, using a tightly coupled multimodal LLM with a flow matching action expert, has remained unchanged. Looking back on the RT-2 Taylor Swift Coke can demo in 2023,

### [28:57 - 29:27]

it's incredible to see how far VLA models have come. And what's perhaps even more impressive to me is that the Physical Intelligence team had the foresight to realize what this unimpressive demo really meant, that large language models could be trained to be robots, potentially leveraging the full knowledge of the internet into robot brains. Now, as impressive as these demos are, they're still demos.

### [29:25 - 29:52]

In 1995, a team from Carnegie Mellon demonstrated a self-driving system, Ralph, that drove across the US at 98.2% autonomously. This clearly did not mean that self-driving cars were around the corner. >> [music] >> And the generation of self-driving cars we have today works very differently. And interestingly, there's a different paradigm emerging for building robot brains, broadly known as world models,

### [29:50 - 30:18]

that actually do not use large language models as a backbone. Yann LeCun, AI pioneer and long-time chief AI scientist at Meta, recently left his role at Meta to start a new venture focused on world models. Yann was kind enough to chat with us about it and wasn't shy about giving his opinion on VLA models. What's your expectation here? Do you think JEPA-based approaches will eventually overtake VLA approaches? Oh,

### [30:16 - 30:44]

absolutely. Yeah, VLA are doomed. I mean, they they basically don't work really well. Okay. I mean, Next time, we'll dig into Yann's approach. If you enjoyed this video, check out the companion poster. The poster walks through the full Pi Zero architecture with helpful descriptions along the way. Fitting everything on screen was a huge challenge when animating this video. And the large format of the poster is

### [30:42 - 31:09]

perfect for getting everything into one place. The poster is printed on high-quality large format photo paper with genuine Canon inks for excellent colors and details. For a limited time, you can get a discount on the poster when bundled with the Welch Labs' Illustrated Guide to AI using code VLA. Speaking of the Welch Labs' Illustrated Guide to AI, I'm very excited to announce that international shipping is

### [31:06 - 31:31]

now available in these nine countries. And we're planning to expand to these countries next. I know this has taken a really long time. Thank you for your patience. A ton of you have emailed us and joined our international shipping waitlist. Today, all of our books are printed in the US. We have a great relationship with our printer and the quality is outstanding. We've received a bunch of nice feedback

### [31:29 - 31:55]

about this. This viewer told us that the construction quality is the best they've ever seen. However, our print costs are fairly high and being self-published makes international logistics a real challenge. Until very recently, my family and I packed all the books ourselves. Here's 7,000 lbs of books getting dropped off on the street in front of my house late last year. We use high-quality boxes and corner protectors

### [31:54 - 32:18]

to make sure your book arrives in pristine condition. The other packaging options we've tried it just don't protect this heavy book very well. Here's some outgoing shipments and a van we rent sometimes for post office runs. Here's part of another shipment that was delivered during a snowstorm this year. And here's some more books heading to the post office in my family's SUV. It's definitely been an adventure.

### [32:16 - 32:41]

Early this year, we started looking at ways to improve and scale our process. We've had some interesting calls with publishers, but the deals we've seen so far either significantly reduce print quality or cut too deeply into our margins, effectively introducing one or two layers of middlemen to our supply chain. So, we've decided to stay self-published for now. We did find a great local packing

### [32:39 - 33:05]

logistics partner who now, thankfully, is handling fulfillment. They also ship enough volume to get some nice international rate discounts. This is what has allowed us to start to tackle international shipping. Starting today, we're offering flat rate shipping to Canada, Mexico, the UK, Ireland, Germany, France, the Netherlands, Italy, and Belgium. And the flat rate includes all relevant VAT, GST, and duties.

### [33:04 - 33:28]

We chose these countries by cross-referencing the countries with the highest demand on our waitlist and where we're able to ship without exorbitant shipping costs. Next, we're looking at expanding to India, Australia, New Zealand, Singapore, Japan, South Korea, Hong Kong, Thailand, and Malaysia. Although higher shipping costs due to a global increase in fuel prices is making this a bit more challenging than we

### [33:26 - 33:52]

expected. I'm really happy that we now have some international options, but the price we need to charge to cover printing and shipping is still higher than I would like. If we continue to see strong demand, this will allow us to invest in larger print runs, bringing down printing cost. And we're even looking at doing some of our printing regionally, starting in Europe. This would significantly bring down our

### [33:49 - 34:16]

European shipping costs and allow for lower prices. Sometimes, I really question if this is all just crazy and really a distraction from making videos, especially on days when 7,000 lbs of books show up at my house. However, at the end of the day, the mission of Welch Labs is to make these complex topics as understandable as possible, and books are a big part of that mission. One supporter on Patreon, Lauren Steely,

### [34:15 - 34:41]

put this really nicely when talking about the book. It's not just a condensed version of the videos. The book actually adds so much more detail that the videos couldn't possibly contain. Finally, a big thank you to all the readers who have helped find errors and made suggestions for improvements. These readers are listed on the credits page of the latest version of the book. And we published an errata at

### [34:38 - 35:03]

welchlabs.com/ai-book. I especially want to thank Robert Blumoff. He's been incredibly meticulous at rooting out little issues in the book and has even made his own perceptron machine and build guide. I'll include a link in the description below. Thank you so much for your patience and to everyone who's bought a book. It really helps the business work and means a lot to us. Thank you.
