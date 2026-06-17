# Quanta Magazine Metadata Index

This directory is a GitHub-browsable index of Quanta Magazine articles collected for
Research Collector. It is a metadata-only index: article bodies are not mirrored.

## What Is Here

- [quanta_index.md](quanta_index.md): human-readable long index of 2,299 dated article URLs.
- [quanta_articles.csv](quanta_articles.csv): spreadsheet-friendly table for filtering.
- [quanta_articles.json](quanta_articles.json): machine-readable records for scripts.
- [quanta_collection_errors.json](quanta_collection_errors.json): collection error log.
- [collect_quanta_index.py](../../scripts/collect_quanta_index.py): reproducible collector.
- [quanta-resource-index.md](../../digests/2026-06-16/workflow/quanta-resource-index.md): workflow summary.

Each record contains title, URL, publication date, author list, Quanta tag/kicker,
inferred broad category, short description, and discovery metadata.

## Coverage

- Total article-like dated URLs: 2,299
- Time span: 2012-2026
- Collection sources: Quanta's public sitemap and archive pages
- Full-text mirroring: no

Broad inferred categories:

- Mathematics: 556
- Biology: 502
- Physics: 493
- Computer Science: 324
- Uncategorized / mixed tags: 424

High-frequency Quanta tags and formats:

- Abstractions blog
- Q&A
- Insights puzzle
- Quantized Columns
- neuroscience
- evolution
- The Joy of Why
- astrophysics
- number theory
- geometry
- quantum physics
- artificial intelligence
- cosmology
- mathematical physics
- quantum computing
- algorithms
- genomics
- particle physics
- combinatorics
- quantum gravity

## How To Browse

Start with [quanta_index.md](quanta_index.md) if you want a readable long list.
Use browser search inside that file for terms such as:

- `complex systems`
- `fluid dynamics`
- `networks`
- `tipping point`
- `climate science`
- `geophysics`
- `artificial intelligence`
- `neuroscience`
- `number theory`
- `geometry`
- `quantum gravity`
- `statistical physics`

Use [quanta_articles.csv](quanta_articles.csv) if you want to filter by year,
category, tag, or author in a spreadsheet.

## Reading Lenses

### Population Recovery, Disasters, and Reduced Dynamics

These articles are useful for thinking about disaster-time population recovery as
a macroscopic relaxation process, where a few summary variables can predict the
post-peak trajectory.

- [The New Math of How Large-Scale Order Emerges](../../digests/2026-05-13/quanta-the-new-math-of-how-large-scale-order-emerges.md)
- [Simpler Math Predicts How Close Ecosystems Are to Collapse](https://www.quantamagazine.org/simpler-math-predicts-how-close-ecosystems-are-to-collapse-20230306/)
- [The Math of Catastrophe](https://www.quantamagazine.org/the-math-of-climate-change-tipping-points-20250915/)
- [The Climate Change Paradox](https://www.quantamagazine.org/the-climate-change-paradox-20250915/)
- [When Coupled Volcanoes Talk, These Researchers Listen](https://www.quantamagazine.org/when-coupled-volcanoes-talk-these-researchers-listen-20260327/)
- [Will We Ever Be Able To Forecast Volcanic Eruptions Like Weather?](https://www.quantamagazine.org/will-we-ever-be-able-to-forecast-volcanic-eruptions-like-weather-20260508/)
- [A Burp or a Blast? Seismic Signals Reveal the Volcanic Eruption to Come](https://www.quantamagazine.org/seismic-data-helps-scientists-forecast-volcanic-explosions-20210601/)
- [In Natural Networks, Strength in Loops](https://www.quantamagazine.org/in-natural-networks-strength-in-loops-20130814/)
- [Complexity Scientist Beats Traffic Jams Through Adaptation](https://www.quantamagazine.org/complexity-scientist-beats-traffic-jams-through-adaptation-20200928/)
- [How Swarming Insects Act Like Fluids](https://www.quantamagazine.org/how-swarming-insects-act-like-fluids-20190710/)

The useful conceptual bridge is:

```text
local agents / local movements
  -> coarse population field
  -> center-weighted pressure state
  -> post-peak relaxation rate
```

### Flow, Transport, Networks, and Translation Layers

These articles are helpful when translating between continuous fields, flows,
networks, spectra, and reduced physical variables.

- [Networks Hold the Key to a Decades-Old Problem About Waves](../../digests/2026-06-05/quanta-networks-hold-the-key-to-a-decades-old-problem-about-waves.md)
- [A Unified Theory of Randomness](../../digests/2026-06-05/quanta-a-unified-theory-of-randomness.md)
- [New 'Superdiffusion' Proof Probes the Mysterious Math of Turbulence](https://www.quantamagazine.org/new-superdiffusion-proof-probes-the-mysterious-math-of-turbulence-20250516/)
- [Long-Sought Proof Tames Some of Math's Unruliest Equations](https://www.quantamagazine.org/long-sought-proof-tames-some-of-maths-unruliest-equations-20260206/)
- [How Quantum Physicists Explained Earth's Oscillating Weather Patterns](https://www.quantamagazine.org/how-quantum-physics-describes-earths-weather-patterns-20230718/)

The recurring pattern is that hard systems become tractable after changing
representation: a wave problem becomes a network problem, a random geometry
problem becomes a growth/exploration problem, and a mobility field can become a
pressure-release / conductance problem.

### Biological and Collective Systems

These articles are useful for thinking about organization, constraints, and
collective behavior.

- [The Hidden Mathematical Dance Inside Plant Cells](../../digests/2026-05-24/quanta-the-hidden-mathematical-dance-inside-plant-cells.md)
- [How Is Flocking Like Computing?](https://www.quantamagazine.org/how-is-flocking-like-computing-20240328/)
- [The Remarkable Self-Organization of Ants](https://www.quantamagazine.org/ants-build-complex-structures-with-a-few-simple-rules-20140409/)
- [Out-of-Sync 'Loners' May Secretly Protect Orderly Swarms](https://www.quantamagazine.org/out-of-sync-loners-may-secretly-protect-orderly-swarms-20200521/)
- [Smarter Parts Make Collective Systems Too Stubborn](https://www.quantamagazine.org/smarter-parts-make-collective-systems-too-stubborn-20190226/)

### AI, Computation, and Mathematical Structure

These are useful for tracking Quanta's treatment of AI and theoretical
computation, especially when the question is not product capability but
structure, representation, proof, and complexity.

- [How Terry Tao Became an Evangelist for AI in Math](https://www.quantamagazine.org/how-terry-tao-became-an-evangelist-for-ai-in-math-20260608/)
- [The AI Revolution in Math Has Arrived](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)
- [Key Chemistry Question Answered, No Quantum Computer Required](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/)
- [How Unknowable Math Can Help Hide Secrets](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/)

## Existing Local Digests

Four Quanta articles already have local study notes:

- [The New Math of How Large-Scale Order Emerges](../../digests/2026-05-13/quanta-the-new-math-of-how-large-scale-order-emerges.md)
- [The Hidden Mathematical Dance Inside Plant Cells](../../digests/2026-05-24/quanta-the-hidden-mathematical-dance-inside-plant-cells.md)
- [A Unified Theory of Randomness](../../digests/2026-06-05/quanta-a-unified-theory-of-randomness.md)
- [Networks Hold the Key to a Decades-Old Problem About Waves](../../digests/2026-06-05/quanta-networks-hold-the-key-to-a-decades-old-problem-about-waves.md)

## Reproducing The Index

Run:

```bash
python scripts/collect_quanta_index.py --delay 0 --timeout 12 --archive-delay 0.03
```

Use `--fetch-detail-pages` only when detailed article-page metadata is needed;
the default archive-card mode is faster and avoids unnecessary page fetches.
