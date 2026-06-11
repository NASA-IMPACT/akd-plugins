# Worldview stories (reference query flows and permalinks)

## Source
- Folder: `resources/stories/`
- Key subfolders:
  - `resources/stories/query/` — story step markdown files (per story, step-by-step)
  - `resources/stories/permalinks/` — permalink JSON examples (per story)
  - `resources/stories/manifest.json` — story inventory/metadata (if applicable)

## Purpose
Provide **curated reference examples** of user-facing story flows (step text) and corresponding Worldview permalinks.

These are intended to help the agent (and maintainers) align on:
- canonical examples of how Worldview features are explained
- the kinds of query narratives supported (e.g., geostationary imagery, swath gaps)
- example deep-link/permalink payloads used in stories

## How this is used in practice (SME)
TBD (confirm): whether these stories are used as:
- reference only (examples for consistency/testing), or
- user-facing content the agent may quote/adapt

## When it becomes relevant (stage)
- When the user asks for a **guided walkthrough** similar to an existing Worldview story
- When generating or validating **Worldview deep links/permalinks** against known examples
- When doing **content consistency checks** (terminology, explanations) against established story language

## Task type
- Reference / exemplar lookup

## What parts are actually used vs ignored
TBD (confirm):
- Use: story step text under `resources/stories/query/<story>/stepNNN.md`
- Use: permalink JSON under `resources/stories/permalinks/<story>.json`
- Ignore: any fields in `manifest.json` not needed for selection/indexing

## Authority
- Reference / exemplar content (not an authoritative scientific source of truth)
- Scientific authority remains with metadata-authoritative sources (e.g., CMR) and official dataset documentation

## Mandatory vs optional
- Optional

## Notes / examples observed
- `resources/stories/query/geostationary/step*.md` contains explanatory text and links to quick guides.
- `resources/stories/query/swath_gaps/step001.md` begins a narrative about missing imagery (story continues in subsequent steps).

## Open questions
- Should the agent be allowed to **quote** story text verbatim, or only paraphrase?
- Should the agent treat these stories as the preferred "teaching script" when relevant, or only as background reference?
- What is the desired mapping between:
  - a user’s intent → a specific story, and
  - a story → the correct permalink (if multiple exist)?
