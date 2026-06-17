# Curated Slides: But how do AI images and videos actually work?

- Source video: https://www.youtube.com/watch?v=iv-5mZ_9CPY
- Raw slide directory: `youtube/slides/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/`
- Transcript: `youtube/transcripts/iv-5mZ_9CPY-but-how-do-ai-images-and-videos-actually-work-guest-video-by-welch-labs/transcript.md`
- Curated frame count: `21`
- Contact sheet: [contact_sheet.jpg](contact_sheet.jpg)

## Selection Logic

This is an animation-heavy explainer rather than a static slide lecture. The
curated set keeps key visual states that support the video's conceptual arc:
prompted video generation, CLIP-style shared embeddings, diffusion as
time-reversed Brownian motion, score/vector-field interpretation, deterministic
DDIM-style sampling, text conditioning, classifier-free guidance, and negative
prompt guidance.

## Frames

| # | Time | Raw | Curated frame | Role in the argument |
|---|---:|---|---|---|
| 1 | 00:00:04 | `slide-0001.jpg` | ![Opening VEO astronaut horse](01-opening-veo-astronaut-horse.jpg) | Opens with the visible target phenomenon: text-to-video generation can now produce cinematic scenes. |
| 2 | 00:01:01 | `slide-0004.jpg` | ![WAN prompt to video](02-wan-prompt-to-video.jpg) | Grounds the explainer in an open video model and a concrete prompt-output loop. |
| 3 | 00:01:25 | `slide-0006.jpg` | ![Random noise video seed](03-random-noise-video-seed.jpg) | Shows the starting point of generation: pure random noise rather than a rough sketch. |
| 4 | 00:02:31 | `slide-0010.jpg` | ![CLIP image encoder embedding](04-clip-image-encoder-embedding.jpg) | Introduces the image/text encoder idea behind CLIP-style shared representation. |
| 5 | 00:05:48 | `slide-0025.jpg` | ![CLIP contrastive similarity matrix](05-clip-contrastive-similarity-matrix.jpg) | Makes the contrastive alignment objective visually explicit. |
| 6 | 00:08:48 | `slide-0032.jpg` | ![Forward noising process](06-forward-noising-process.jpg) | Shows the forward diffusion/noising process that destroys image structure. |
| 7 | 00:09:10 | `slide-0033.jpg` | ![Diffusion training noise prediction](07-diffusion-training-noise-prediction.jpg) | Shows training as learning to predict/remove injected noise. |
| 8 | 00:09:16 | `slide-0034.jpg` | ![Reverse image generation loop](08-reverse-image-generation-loop.jpg) | Shows generation as repeated model calls from noise back toward image structure. |
| 9 | 00:10:12 | `slide-0036.jpg` | ![DDPM sampling tree example](09-ddpm-sampling-tree-example.jpg) | Establishes the Stable Diffusion desert-tree example used for sampling comparisons. |
| 10 | 00:10:44 | `slide-0037.jpg` | ![DDPM training and sampling algorithms](10-ddpm-training-and-sampling-algorithms.jpg) | Anchors the informal explanation to the DDPM paper's training/sampling algorithms. |
| 11 | 00:11:43 | `slide-0039.jpg` | ![Score vector field](11-score-vector-field.jpg) | Visualizes diffusion learning as a vector field pointing back toward likely data. |
| 12 | 00:14:38 | `slide-0042.jpg` | ![Random walk Brownian motion](12-random-walk-brownian-motion.jpg) | Connects noisy image trajectories to Brownian motion/random walks. |
| 13 | 00:20:26 | `slide-0044.jpg` | ![Time conditioned score field](13-time-conditioned-score-field.jpg) | Shows why time conditioning matters: the field changes with noise level. |
| 14 | 00:24:04 | `slide-0052.jpg` | ![DDIM deterministic trajectory](14-ddim-deterministic-trajectory.jpg) | Represents the deterministic trajectory perspective behind DDIM/flow-style sampling. |
| 15 | 00:24:57 | `slide-0057.jpg` | ![CLIP text image bridge](15-clip-text-image-bridge.jpg) | Bridges CLIP embeddings back to diffusion: text vectors can steer generation. |
| 16 | 00:26:20 | `slide-0061.jpg` | ![UnCLIP diffusion inverts CLIP](16-unclip-diffusion-inverts-clip.jpg) | Marks the DALL-E 2/UnCLIP move: using diffusion to invert CLIP image embeddings. |
| 17 | 00:27:01 | `slide-0065.jpg` | ![Text conditioning diffusion model](17-text-conditioning-diffusion-model.jpg) | Shows conditioning: text embeddings become extra inputs to the denoising model. |
| 18 | 00:27:31 | `slide-0068.jpg` | ![Classifier-free guidance vector fields](18-classifier-free-guidance-vector-fields.jpg) | Visualizes the split between unconditional and conditioned vector fields. |
| 19 | 00:33:00 | `slide-0072.jpg` | ![Conditioning only fails tree prompt](19-conditioning-only-fails-tree-prompt.jpg) | Shows why conditioning alone is weak: the prompt can be partly missed. |
| 20 | 00:33:26 | `slide-0074.jpg` | ![Guidance scale WAN output](20-guidance-scale-wan-output.jpg) | Shows guidance-scale amplification producing stronger prompt adherence. |
| 21 | 00:33:37 | `slide-0075.jpg` | ![Negative prompt guidance](21-negative-prompt-guidance.jpg) | Extends classifier-free guidance to negative prompts in text-to-video models. |

