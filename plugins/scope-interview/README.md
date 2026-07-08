# Scope Interview Agent — Claude Code plugin

A structured **requirements-interview agent**. Point it at a new software or
scientific system and it interviews you — role-gated, in short question clusters
— then produces a single **narrative scoping document** (~3–4 pages): problem,
success/failure criteria, stakeholders (and their conflicts), scope boundaries,
functional and non-functional requirements, key entities, workflows, risks, and
open questions — *before* any design or implementation begins. It refuses to
design, write code, or answer off-topic questions, and challenges vague answers
until the scope is concrete.

Especially aimed at NASA / Earth-observation / geospatial / data-science systems
(AKD-Lab), but works for any project.

## Two modes

The narrative deliverable is the same in both modes — the mode only changes what
*grounds* the interview and where the document is *saved*:

- **Standard mode (default).** Role-gated, clustered interview → a single
  stakeholder-friendly narrative document, presented inline. Works with your
  answers alone, in any chat.
- **Codebase-aware mode (enhancement — offered, never forced).** When you run it
  inside a code project (and/or identify as a Developer), it can first do a
  read-only survey of the codebase so its questions are grounded in what already
  exists, and it writes the finished document to `docs/scope/` — plus a raw
  interview transcript alongside it for future reuse.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install scope-interview@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing
at the repo root, not the plugin subdir — then the same install command.)

Then invoke the skill directly (`/scope-interview:scope-interview`) or just
ask, e.g.:

> "Help me scope a new data pipeline for MODIS fire-detection products."

The agent opens the AKD Scope and Requirements Interview and walks the clusters,
reviewing each cluster before moving on.

## Configuration

None. This is a pure-skill plugin — no MCP servers, no API tokens, nothing to
wire up.

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).

## What's inside

```
.claude-plugin/plugin.json     manifest
skills/scope-interview/
  SKILL.md                     the skill
  references/                  source-workspace specs (scope, reasoning,
                               output, guardrails, contexts, tools)
```

## How it works (for maintainers)

- The whole agent is a single skill (`skills/scope-interview/SKILL.md`) — no
  tools, no MCP servers. Its behavior is the prompt: a structured
  Project Scoping Interview Agent that runs a role-gated, clustered interview
  (~5–6 questions per cluster with a post-cluster review) and produces one
  unified narrative scoping document. Strict guardrails keep it on-topic (no
  science answers, no code, no recipes, jailbreak refusal/escalation) and keep
  the human as the decision-maker.
- **Faithful base + enhancement.** The narrative behavior faithfully follows the
  source scoping-agent workspace export. **Codebase-aware mode** is an additive
  Claude Code layer: an optional Step 0 read-only survey (offered only when the
  working directory looks like a code project), and file-saving to `docs/scope/`.
  Codebase findings only *sharpen* questions and produce draft answers the user
  confirms — code never silently fills a requirement.
- **Output style** is chosen at the end (Management / PM / Technical Lead /
  Developer / SME / general), tuning tone and depth of the *single* document;
  it defaults to the base stakeholder-friendly narrative.
- On save, the polished document is written to
  `docs/scope/scope-<slug>-<YYYY-MM-DD-HHMM>.md`, and the **full raw interview
  transcript** to `docs/scope/scope-<slug>-<YYYY-MM-DD-HHMM>-raw.md` for future
  reuse; the skill ensures `docs/scope/` is git-ignored. On corrections it
  regenerates and updates the same files.
- `references/` carries the source-workspace specifications (scope, reasoning,
  output, guardrails, contexts, tools) as load-on-demand depth material.
- Upstream source: [NASA-IMPACT/akd-scoping-agent](https://github.com/NASA-IMPACT/akd-scoping-agent).
