# Scope Interview Agent — Claude Code plugin

A strict, structured **requirements-interview agent**. Point it at a new
software or scientific system and it extracts a complete **Scope Requirements
Document** — problem, success criteria, stakeholders, functional and
non-functional requirements, entities, workflows, risks, and out-of-scope
boundaries — *before* any design or implementation begins. It asks one question
at a time, refuses to design or propose architecture, and challenges vague
answers until the scope is concrete.

Especially aimed at NASA / Earth-observation / geospatial / data-science systems
(AKD-Lab), but works for any project. When run inside a code project it can
optionally do a read-only survey of the codebase first, so its questions are
grounded in what already exists, and it writes the finished document to
`docs/scope/`.

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

The agent opens the AKD Scope and Requirements Interview and walks the steps
one question at a time.

## Configuration

None. This is a pure-skill plugin — no MCP servers, no API tokens, nothing to
wire up.

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).

## What's inside

```
.claude-plugin/plugin.json     manifest
skills/scope-interview/        the skill: SKILL.md
```

## How it works (for maintainers)

- The whole agent is a single skill (`skills/scope-interview/SKILL.md`) — no
  tools, no MCP servers. Its behavior is the prompt: strict constraints
  (one question at a time, no design, no assuming missing info) plus a
  mandatory ordered interview flow (Steps 0–9).
- **Step 0** is an optional read-only codebase survey, offered only when the
  working directory looks like a code project. Findings only *sharpen*
  questions and produce draft answers the user confirms — code never silently
  fills a requirement.
- The final **Scope Requirements Document** is written to
  `docs/scope/scope-<YYYY-MM-DD-HHMM>.md`, and the skill ensures `docs/scope/`
  is git-ignored. On corrections it regenerates and updates the same file.
- Upstream source: [NASA-IMPACT/akd-scoping-agent](https://github.com/NASA-IMPACT/akd-scoping-agent).
