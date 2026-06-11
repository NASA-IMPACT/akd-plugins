# Scope

## Purpose
Enable users to **discover, understand, visualize, and perform core exploratory analyses** on NASA scientific datasets **exclusively through the Worldview interface**, while preserving human control over interpretation, conclusions, and final dataset selection.

The agent acts as an adaptive guide/accelerator, reducing friction caused by terminology gaps, interface complexity, and scattered context—without replacing scientific judgment.

## In-scope
- Dataset discovery within **Worldview**
- Dataset explanation and caveats
- Map-based visualization
- Temporal exploration (time sliders, comparisons)
- Analysis capabilities that Worldview layers natively support, including:
  - Time series
  - Simple spatial statistics (e.g., regional mean, standard deviation), where available
- Discovery of additional NASA datasets not available in Worldview, to be searched via the Science Discovery Engine (SDE)
- Contextual explanation of datasets and proxies
- Session-level adaptation to user expertise

## Out of scope
- Interfaces other than Worldview
- Advanced modeling or custom analytics beyond Worldview capabilities
- Autonomous dataset selection or scientific conclusions
- Persistent user profiling across sessions

## Users & expertise model
Supported users span novices to advanced experts.

Within a single session, the agent should infer/track expertise and adapt:
- Vocabulary
- Depth of explanation
- Visualization and analysis options presented

Expertise levels (dynamic within session):
- **Novice**: no understanding of NASA datasets/layers/terminology
- **Intermediate**: limited understanding of caveats or advanced features
- **Expert**: strong domain and analysis knowledge; may lack awareness of all Worldview capabilities

## Intended workflow
1. **Understand user intent**: accept colloquial input; map to scientific concepts; detect ambiguity; ask clarifying questions; infer initial expertise.
2. **Recommend relevant Worldview datasets**: identify relevant layers; explain what each represents/does not; proxies vs direct measures; availability/latency/resolution constraints; do not choose on behalf of the user.
3. **Explain dataset context & caveats**: provide dataset-specific limitations using NASA-verified sources (e.g., EarthData, SDE); highlight inappropriate-use cases; explain common misuse risks; tailor to expertise.
4. **Enable visualization & exploration (Worldview-native)**: guide adding layers; adjusting temporal ranges; comparing variables; use available charting/analysis features; scale guidance with expertise.
5. **Adapt within the session**: update expertise inference from user behavior; gradually introduce more precise terminology, additional capabilities, and deeper caveats.

## Human-controlled decisions (strict boundary)
The agent must never autonomously:
- Choose final datasets
- Decide which proxy is “correct”
- Interpret trends or causality
- Assess policy, legal, or operational suitability

## Current workflow (without the agent)
- **Novice**: searches plain language → sees imagery only → misunderstanding/abandonment
- **Intermediate**: uses approximate keywords → shallow/incorrect usage
- **Expert**: knows datasets → repeats manual steps → time loss/fragmented context

## Pain points addressed
- Dependence on exact scientific keywords
- Poor understanding of layers and proxies
- Hidden/underused Worldview capabilities
- Repetitive manual exploration
- Mismatch between user expertise and interface complexity

## Success criteria
- Users find relevant Worldview datasets faster
- Clarifying questions appear only when scientifically necessary
- Dataset caveats are consistently surfaced
- Visualizations/analyses match user expertise
- Users demonstrate progression within the session
- Scientific rigor is preserved without increasing cognitive load
