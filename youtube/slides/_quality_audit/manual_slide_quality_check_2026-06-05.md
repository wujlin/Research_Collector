# Manual Slide Quality Check, 2026-06-05

Scope: six Welch Labs video slide sets collected for the June 5 note batch.

## Overall verdict

The slide extraction is technically usable. All curated frames inspected here are `1706x960`, and the contact sheets render correctly. There is no systemic resolution mismatch or broken image issue.

The main limitation is semantic curation, not capture quality. The current `curated_quality/` folders are good enough for note drafting, but they are not final slide selections. Several sets still include sponsor segments, book/poster promotion frames, empty desk transitions, host/interview frames, and near-duplicate explanation frames.

For writing notes, no rerun is required. For a polished visual deck or a figure-rich digest, create a second-pass `semantic_curated/` subset with about 8-18 frames per video.

## WSA semantic pass

After this audit, a second-pass `semantic_curated/` subset was generated from the 1080p source videos on WSA for all six videos. These folders are now the preferred slide source for the June 5 Welch Labs notes; the older `curated_quality/` folders remain useful as rough extraction archives.

Counts after the semantic pass:

- `v_jDvpEGTIg-can-yann-lecun-reshape-ai-again/semantic_curated/`: 18 frames
- `2mrGMMmrVNE-inside-the-worlds-smartest-robot-brain-vla/semantic_curated/`: 19 frames
- `NrO20Jb-hy0-the-misconception-that-almost-stopped-ai-how-models-learn-part-1/semantic_curated/`: 14 frames
- `VkHfRKewkWw-the-fma-of-artificial-intelligence-backpropagation-how-models-learn-part-2/semantic_curated/`: 17 frames
- `qx7hirqgfuU-why-deep-learning-works-unreasonably-well-how-models-learn-part-3/semantic_curated/`: 19 frames
- `2hcsmtkSzIw-can-humans-make-ai-any-better/semantic_curated/`: 18 frames

Manual recheck: the VLA pass initially caught one bad 00:23:30 frame from the image-generation analogy segment; it was replaced with the 00:23:20 action-matrix frame. Remaining caveat: the LeCun and Can Humans sets intentionally keep a few interview or narrative frames because those videos use them as part of the argument, but the semantic sets are cleaner than the original scene-detected folders.

## Per-set assessment

### `qx7hirqgfuU-why-deep-learning-works-unreasonably-well-how-models-learn-part-3`

Quality: A-

This is the strongest set. The Baarle-Hertog map, ReLU folding geometry, region tilings, deep-vs-wide comparison, and training progression are all visible and useful. It supports a high-quality visual explanation of why depth changes representation power.

Clean up before publication: remove sponsor/browser frames, empty desk frames, host frames, and book promotion frames near the end.

### `NrO20Jb-hy0-the-misconception-that-almost-stopped-ai-how-models-learn-part-1`

Quality: A-

The core loss landscape story is well covered. The Llama token example, single-parameter exploration, high-dimensional random slices, and wormhole-style visualization are all legible. This set is very usable for note writing.

Clean up before publication: remove a few pure desk transition frames and reduce repeated paper-cut derivation frames.

### `2mrGMMmrVNE-inside-the-worlds-smartest-robot-brain-vla`

Quality: B+

The set is relatively compact and focused. It contains the RT-2/Pi Zero timeline, architecture diagrams, action expert/flow matching visuals, attention/KV-cache explanation, and robot demonstration frames. This is enough to support the VLA note.

Clean up before publication: remove Welch Labs book/poster promotion frames and logistics/shipping frames. Keep the architecture and robot-control frames.

### `VkHfRKewkWw-the-fma-of-artificial-intelligence-backpropagation-how-models-learn-part-2`

Quality: B+

The backprop derivation is well represented. The GPS classifier, softmax/cross-entropy setup, chain-rule derivation, gradient bars, and city-plane visualization are useful and mostly legible.

Clean up before publication: remove repeated black-background network frames, very dark loss-landscape frames, and end-of-video promotional material. The core paper-cut derivation frames are the valuable part.

### `2hcsmtkSzIw-can-humans-make-ai-any-better`

Quality: B

The main narrative is present: Harpy, the bitter lesson, LLM imitation, AlphaGo policy/value networks, RL from experience, and Era of Experience. It supports the written note.

Clean up before publication: remove book/ad frames, empty desk frames, and long article-page frames that are visually dense but not very explanatory in thumbnail form. A polished subset should be around 18-22 frames.

### `v_jDvpEGTIg-can-yann-lecun-reshape-ai-again`

Quality: B

The set covers the full JEPA/VLA contrast: V-JEPA2, VL-JEPA, VLA critique, Push-T world-model rollouts, CEM planning, and hierarchy. It is usable for note writing.

Clean up before publication: this set is the noisiest. It includes many desk transitions, interview frames, sponsor frames, and repeated robot-demo frames. A second-pass semantic subset is recommended if the images will be reused outside rough notes.

## Recommended next pass

If making a polished visual study pack, create one `semantic_curated/` folder per video with:

- 8-12 frames for short conceptual videos.
- 12-18 frames for architecture-heavy videos.
- 18-22 frames only for long multi-stage narrative videos.

Selection rules:

- Keep frames that introduce a new concept, architecture, state transition, or comparison.
- Remove sponsor, poster/book, logistics, host/interview, empty desk, and repeated near-identical frames.
- Prefer diagrams over raw demo footage unless the demo frame is necessary evidence.
- For the three "How Models Learn" videos, preserve one representative frame per conceptual step rather than every paper-cut manipulation.
