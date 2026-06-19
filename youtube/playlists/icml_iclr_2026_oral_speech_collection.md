# ICML / ICLR 2026 Oral And Speech Collection

Updated: 2026-05-12

This is the operational collection manifest for conference oral talks, invited speeches, and high-signal paper presentations that may later become linear Chinese notes. It is separate from the broader AI+physics watchlist because the goal here is not only discovery, but also reproducible collection of audio, transcript, and slide/PPT evidence.

## Boundary

- ICML 2026 has not happened yet. The official conference page lists Seoul, South Korea, July 6-11, 2026, so there are no official ICML 2026 oral or speech videos to collect on 2026-05-12.
- ICLR 2026 already has an official oral list and invited talk schedule. Some public YouTube presentations exist, but not every official oral has public video or downloadable slides.
- For videos without official slide PDFs, PPT information should be reconstructed from video frames first, then curated manually before writing notes.

## Collection Queue

| Status | Conference | Type | Video / talk | Source | Audio target | Slide target | Notes |
|---|---|---:|---|---|---|---|---|
| Collected on WSA | ICLR 2026 | Oral video | Latent Particle World Models | https://www.youtube.com/watch?v=aZeaCyXJjYI | `youtube/audio/iclr2026-oral-latent-particle-world-models/` | `youtube/slides/aZeaCyXJjYI-*` | Audio, video, transcript, and 17 raw slide frames collected. |
| Collected on WSA | ICLR 2026 | Oral video | SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer | https://www.youtube.com/watch?v=bHHL691_IPo | `youtube/audio/iclr2026-oral-sana-video-efficient-video-generation/` | `youtube/slides/bHHL691_IPo-*` | Audio, video, transcript, and 17 raw slide frames collected. |
| Collected on WSA | ICLR 2026 | Oral video | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning | https://www.youtube.com/watch?v=HbGah-uP1fI | `youtube/audio/iclr2026-oral-gepa-reflective-prompt-evolution/` | `youtube/slides/HbGah-uP1fI-*` | Audio, video, transcript, and 24 raw slide frames collected. |
| Collected on WSA | ICLR 2026 | Oral video | Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation | https://www.youtube.com/watch?v=cPeGBXXHxZM | `youtube/audio/iclr2026-oral-locality-aware-parallel-decoding/` | `youtube/slides/cPeGBXXHxZM-*` | Audio, video, transcript, and 18 raw slide frames collected. |

WSA collection log for this batch:

`youtube/logs/iclr2026_oral_audio_slides_collect_direct_20260512_004044.log`

Local curated slides and notes:

- `digests/video/world-models-representation/iclr2026-latent-particle-world-models.md`
- `digests/video/world-models-representation/iclr2026-sana-video-efficient-video-generation.md`
- `digests/video/agents-rl-adaptation/iclr2026-gepa-reflective-prompt-evolution.md`
- `digests/video/world-models-representation/iclr2026-locality-aware-parallel-decoding.md`

## Already Collected

| Status | Conference / axis | Video / talk | Existing artifacts | Notes |
|---|---|---|---|---|
| Collected | ICLR 2026 oral-adjacent | Energy-Based Transformers are Scalable Learners and Thinkers | `youtube/transcripts/RAEy3JZmIaA-energy-based-transformers-are-scalable-learners-and-thinkers/`; `youtube/slides/RAEy3JZmIaA-energy-based-transformers-are-scalable-learners-and-thinkers-paper-review/` | Keep as the main EBT study source; do not duplicate unless re-curating slides. |
| Collected | ICLR 2026 invited-talk axis | Max Welling: From Physics to AI to Materials | `youtube/transcripts/BV1qi9rB7EQc-max-welling-iclr2026-from-physics-to-ai-to-materials/`; `youtube/slides/BV1qi9rB7EQc-max-welling-iclr-2026-from-physics-to-ai-to-materials/` | Already expanded into notes; may be linked when writing an AI+physics synthesis. |
| Collected | Max Welling background | Materials Underlie Everything | `youtube/transcripts/V7_Ec2WFAWs-max-welling-materials-underlie-everything/`; `youtube/slides/BV12ffbBrEh7-max-welling-materials-underlie-everything-材料是万物之基/` | Background material for the same physics-to-materials arc. |

## Watch Queue

| Status | Conference | Item | Reason | Action |
|---|---|---|---|---|
| Watch | ICML 2026 | Official oral / invited videos | The conference runs July 6-11, 2026, so public official videos are not expected yet. | Recheck after the conference and again after official video uploads. |
| Watch | ICLR 2026 | Invited talks by Max Welling, Percy Liang, Katie Bouman, Karen Adolph, Junyang Lin, Pablo Arbelaez | Official invited schedule exists, but public official YouTube recordings were not found in this pass. | Recheck ICLR virtual pages and YouTube uploads. |
| Watch | ICLR 2026 oral | `$PhyWorldBench$: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models` | Official oral page exists, but public YouTube video and slide PDF were not found in this pass. | Important for AI+physics; prioritize if video appears. |
| Watch | ICLR 2026 oral | Robust and Interpretable Adaptation of Equivariant Materials Foundation Models | Public video exists but has very low signal/heat in the first pass. | Collect later if the materials-foundation-model branch becomes active. |

## Operating Rule

For each queued video, the minimum study-pack standard is:

- metadata under `youtube/audio/<slug>/metadata.json`
- audio source under `youtube/audio/<slug>/source.*`
- video source under `youtube/video/<slug>/source.*`
- raw slide frames under `youtube/slides/<video-id>-*/`
- transcript under `youtube/transcripts/<video-id>-<slug>/`

Only after these artifacts exist should the note be written under `digests/video/`, because the note needs both the spoken argument and the visual/PPT structure.
