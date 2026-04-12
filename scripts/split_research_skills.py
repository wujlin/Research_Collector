#!/usr/bin/env python3
"""Split the combined research-writing-and-figures skill.

Writes:
- ~/.codex/skills/research-writing/SKILL.md
- ~/.codex/skills/research-figure-analysis/SKILL.md
- narrows ~/.codex/skills/research-writing-and-figures/SKILL.md
"""

from __future__ import annotations

from pathlib import Path


BASE = Path("/Users/jinlin/.codex/skills")


ROUTER_SKILL = """---
name: research-writing-and-figures
description: Use when a task genuinely spans both scientific writing and figure interpretation or requires caption-text alignment across a research project. Prefer `research-writing` for manuscript and digest text, and prefer `research-figure-analysis` for PDF figure extraction, panel-level explanation, and caption auditing.
---

# Research Writing And Figures

Use this skill only when the task truly couples manuscript writing and figure work.

## Routing

- For manuscript sections, reading notes, digests, scientific explanations, and logic tightening, use `research-writing`.
- For PDF figure extraction, panel-level explanation, caption checking, and figure-text consistency, use `research-figure-analysis`.
- Use this combined skill only when both are required in the same turn and the text depends directly on the figure reading.

## Shared references

- Writing rules: [references/writing.md](references/writing.md)
- Figure style rules: [references/visual-style.md](references/visual-style.md)
- Workflow norms: [references/workflow.md](references/workflow.md)
"""


WRITING_SKILL = """---
name: research-writing
description: Use when drafting, rewriting, reviewing, or polishing scientific manuscript sections, study notes, reading digests, captions, or research explanations. This skill enforces problem-driven narrative, linear exposition, terminology consistency, and low-redundancy scientific writing.
---

# Research Writing

Use this skill when the task is primarily about scientific text rather than figure extraction.

## Use when

- revising `Introduction`, `Methods`, `Results`, `Discussion`, `Abstract`, or title
- tightening the logic of a study guide, reading note, or research digest
- converting technical content into linear explanatory notes
- checking terminology, abbreviations, assumptions, and section roles
- rewriting captions only when the task is mainly textual rather than visual

## Core workflow

1. Identify the question the section is supposed to answer.
2. Lead with the point and unfold the logic linearly.
3. Separate background, setup, evidence, and interpretation.
4. Let each paragraph do one job.
5. Use recall only when the current logic truly depends on it.
6. Cut meta-commentary, repetition, and low-information transitions.
7. Keep one stable term per concept unless a real distinction is needed.

## References

- Writing rules: [../research-writing-and-figures/references/writing.md](../research-writing-and-figures/references/writing.md)
- Workflow norms: [../research-writing-and-figures/references/workflow.md](../research-writing-and-figures/references/workflow.md)

## Output defaults

- Keep revisions concise and claim-driven.
- Prefer definitions, derivations, physical meaning, and conclusions over conversational framing.
- If a paragraph mixes definition and interpretation, split it.
"""


FIGURE_SKILL = """---
name: research-figure-analysis
description: Use when explaining, auditing, extracting, or aligning scientific figures from PDFs, papers, or slides. This skill enforces image-first verification, reliable page extraction, panel-by-panel interpretation, caption checking, and figure-text consistency.
---

# Research Figure Analysis

Use this skill when the task is primarily about reading or validating a figure rather than revising prose.

## Use when

- explaining a figure from a paper, PDF, or slide deck
- checking whether a caption matches the actual image
- resolving conflicts between PDF text extraction and visible panel content
- extracting a page or figure region for inspection before interpretation
- aligning figure explanation with manuscript text

## Core workflow

1. Do not trust PDF text extraction as the primary source for figure content.
2. Rasterize the relevant page or figure region first.
3. Verify panel count, labels, visible symbols, and caption against the image.
4. Treat text extraction as secondary support only.
5. If image content and extracted text disagree, trust the image and caption.
6. Explain the figure panel by panel, then summarize the linear logic across panels.

## Extraction protocol

- If the project provides `scripts/extract_pdf_page_images.py`, use it.
- The minimum reliable workflow is:
  1. split the relevant page into a single-page PDF
  2. rasterize to PNG
  3. optionally crop the figure region
  4. check the generated manifest or self-check output before interpreting the figure
- Do not write figure notes until the extraction passes basic checks.

## References

- Figure style rules: [../research-writing-and-figures/references/visual-style.md](../research-writing-and-figures/references/visual-style.md)
- Workflow norms: [../research-writing-and-figures/references/workflow.md](../research-writing-and-figures/references/workflow.md)

## Output defaults

- Explain what each panel shows before interpreting why it matters.
- Keep panel roles distinct.
- Do not import claims from later figures into the current one unless the text says so explicitly.
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    write_text(BASE / "research-writing-and-figures" / "SKILL.md", ROUTER_SKILL)
    write_text(BASE / "research-writing" / "SKILL.md", WRITING_SKILL)
    write_text(BASE / "research-figure-analysis" / "SKILL.md", FIGURE_SKILL)
    print("updated combined router and created specialized skills")


if __name__ == "__main__":
    main()
