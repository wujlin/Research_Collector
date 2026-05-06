# ICLR 2026 AI + Physics Frontier Videos

Updated: 2026-05-05

This is a discovery-stage watchlist, not a finished lecture digest. The goal is to capture ICLR-adjacent talks and paper reviews that matter for the project's current research line:

`stochastic / thermodynamic thinking -> generative dynamics -> physics-informed AI -> scientific and materials discovery`

## Collection Status

The first pass used the YouTube Data API with `search` and `videos` endpoints so that candidates could be ranked by public metadata such as `view_count`, `like_count`, channel, and publication date.

The API quota was exhausted during the broad pass, so this list is a high-confidence partial collection rather than a complete census. Raw candidates from the last successful pass are cached at:

`data/cache/iclr_2026_ai_physics_youtube_candidates.json`

## Priority Axes

### 1. Energy-Based Inference And Thinking

This axis catches videos that do not explicitly say `physics`, but are structurally important for this project because they treat prediction as optimization over a learned scalar energy.

- [Energy-Based Transformers are Scalable Learners and Thinkers (Paper Review)](https://www.youtube.com/watch?v=RAEy3JZmIaA)
  - Channel: Yannic Kilcher
  - Observed views: 31,256
  - Why it matters: ICLR 2026 Oral. This belongs to `energy-based models`, `inference-time optimization`, and `learned verifier` rather than PDE/materials. It should not be missed by an AI+physics collector.

- [Energy-Based Transformers explained | How EBTs and EBMs work](https://www.youtube.com/watch?v=18Fn2m99X1k)
  - Channel: AI Coffee Break with Letitia
  - Observed views: 16,052
  - Why it matters: Lower conference specificity than the Yannic review, but useful for conceptual entry into EBTs and EBMs.

- [New AI Paradigm?! Energy-Based Transformers Explained](https://www.youtube.com/watch?v=LUQkWzjv2RM)
  - Channel: bycloud
  - Observed views: 51,171
  - Why it matters: Highest public heat among the EBT explainers found so far, but probably more popular-science oriented.

- [Energy-Based Transformers are Scalable Learners and Thinkers](https://www.youtube.com/watch?v=uUE0x3iNX1U)
  - Channel: Gabriel Mongaras
  - Observed views: 2,655
  - Why it matters: Direct paper-title match; useful as a secondary explanation source.

### 2. Physics To AI To Materials

This axis captures Max Welling's bridge: physics intuition, probabilistic modeling, equivariance, generative models, and materials discovery.

- [Max Welling: Materials Underlie Everything](https://www.youtube.com/watch?v=V7_Ec2WFAWs)
  - Channel: Latent Space
  - Observed views: 2,322
  - Why it matters: This is the closest match to the user-noted `from physics to AI to materials` arc. It connects physics, generative AI, CuspAI, and materials discovery.

- [Max Welling on AI for Materials Discovery | AI4Science Community Breakfast](https://www.youtube.com/watch?v=1zwVjoWwHiI)
  - Channel: Merantix AI Campus
  - Observed views: 793
  - Why it matters: Strong topic match for AI for materials discovery.

- [EWSC: Max Welling, Searching through Materials: Generate, Emulate, Simulate (2025)](https://www.youtube.com/watch?v=DS6x95GdZWI)
  - Channel: Broad Institute
  - Observed views: 1,149
  - Why it matters: Directly names the `generate, emulate, simulate` loop, which is central for scientific discovery pipelines.

- [Keynote Talk: Max Welling - How AI Can Transform the Sciences](https://www.youtube.com/watch?v=HXOTCg7oIlU)
  - Channel: Deep Learning Indaba
  - Observed views: 472
  - Why it matters: Broader AI-for-science framing; useful background before a materials-specific digest.

- [Martin van den Brink in conversation with Max Welling](https://www.youtube.com/watch?v=iPKlc7FePL8)
  - Channel: CuspAI
  - Observed views: 2,450
  - Why it matters: CuspAI-side material; likely useful for understanding the industrial research trajectory.

### 3. Materials Generative Models

This axis is closest to ICLR AI4Mat and materials foundation model work.

- [All-atom Diffusion Transformers - Chaitanya K. Joshi - ICLR 2025 AI4Mat Spotlight](https://www.youtube.com/watch?v=NiY4NLzemnU)
  - Channel: Chaitanya K. Joshi
  - Observed views: 1,475
  - Why it matters: AI4Mat spotlight; directly connects diffusion transformers to molecules/materials.

- [[ICLR 2026] Robust and Interpretable Adaptation of Equivariant Materials Foundation Models](https://www.youtube.com/watch?v=zXxhy4u4b_c)
  - Channel: Joonseok Lee
  - Observed views: 90
  - Why it matters: Low public heat but high topic match: equivariant materials foundation models.

- [Reinforcement Learning for Materials Discovery (ICLR 2025 AI4Mat)](https://www.youtube.com/watch?v=rCzDybwWkmg)
  - Channel: AAGT
  - Observed views: 63
  - Why it matters: Relevant for the AI4Mat feedback-loop axis.

### 4. World Models And Stochastic Dynamics

This axis connects generative modeling to latent dynamics, particle systems, and world-model learning.

- [Yann LeCun's $1B Bet Against LLMs](https://www.youtube.com/watch?v=kYkIdXwW2AE)
  - Channel: Welch Labs
  - Observed duration: 37:24
  - Why it matters: Timely JEPA / world-model explainer around LeCun's route against pure autoregressive LLM scaling. It is not an ICLR talk, but it belongs in the same research axis as `world models`, `predictive representation`, `energy-based inference`, and physical intelligence.

- [[ICLR 2026 Oral] Latent Particle World Models](https://www.youtube.com/watch?v=aZeaCyXJjYI)
  - Channel: Tal Daniel
  - Observed views: 491
  - Why it matters: ICLR 2026 Oral. Good fit for `world models`, `latent particles`, and stochastic/object-centric dynamics.

- [Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling](https://www.youtube.com/watch?v=b0ciW28HXI0)
  - Channel: Heejeong Nam
  - Observed views: 193
  - Why it matters: Same paper family, more explicit on stochastic dynamics.

### 5. Diffusion, Flow, And Statistical Physics

This axis is not strictly ICLR 2026, but it is central to the project's bridge from stochastic processes to modern generative models.

- [The physics behind diffusion models](https://www.youtube.com/watch?v=R0uMcXsfo2o)
  - Channel: Julia Turc
  - Observed views: 112,206
  - Why it matters: Very high public heat and directly explains diffusion models through a physics lens.

- [MIT 6.S184: Flow Matching and Diffusion Models - Lecture 02](https://www.youtube.com/watch?v=yFD-JSSG-D0)
  - Channel: Peter Holderrieth
  - Observed views: 40,440
  - Why it matters: High-quality technical lecture for flow matching / diffusion foundations.

- [Flow-Matching vs Diffusion Models explained side by side](https://www.youtube.com/watch?v=firXjwZ_6KI)
  - Channel: AI Coffee Break with Letitia
  - Observed views: 38,069
  - Why it matters: Useful conceptual bridge between two generative dynamics parameterizations.

- [Giulio Biroli - Generative AI and Diffusion Models: a Statistical Physics Analysis](https://www.youtube.com/watch?v=9b26lbsIt8c)
  - Channel: IHES
  - Observed views: 3,206
  - Why it matters: Direct statistical-physics analysis of diffusion models.

## Method Upgrade: Avoiding Keyword-Only Search

Keyword search is too brittle for this task. It misses papers like Energy-Based Transformers because they are physically relevant through `energy`, `optimization`, and `scalar objective` language rather than through the literal word `physics`.

The next collector should use a three-stage design:

1. Conference metadata seed
   - Pull ICLR/OpenReview/official workshop metadata first.
   - Use paper titles, oral labels, workshop names, invited speakers, and author names as generated seeds.
   - This replaces hand-written topic keywords with source-grounded metadata.

2. Channel sweep
   - Track trusted channels and recent uploads: Yannic Kilcher, AI Coffee Break, Latent Space, Max Welling/CuspAI, Broad Institute, Merantix AI Campus, MIT / course channels, and ICLR workshop channels when available.
   - This catches high-heat paper reviews even when the paper title does not contain obvious AI-for-physics keywords.

3. Semantic reranking
   - Score each candidate against axis descriptions, not only keyword hits.
   - Example axes:
     - energy-based inference and thinking
     - physics-to-materials discovery
     - geometric/equivariant learning
     - generative dynamics
     - PDE / scientific machine learning
     - world models and stochastic dynamics
   - Use YouTube `view_count` only after semantic filtering, so popular but irrelevant videos do not dominate.

The practical ranking should be:

`final_score = semantic_axis_fit + conference_match + log(view_count) + recency + trusted_channel_bonus`

This keeps the collector sensitive to the research frame rather than just to literal keywords.
