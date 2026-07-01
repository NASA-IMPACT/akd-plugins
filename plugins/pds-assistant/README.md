# PDS Assistant — Claude Code plugin

Find the right **NASA Planetary Data System (PDS)** datasets in natural
language. Give it a planetary-science question (or a sentence from a paper's
methods / data-availability section) and the bundled skill routes it to the
correct PDS node, walks the live archive directories deterministically, and
returns grounded candidate datasets — archive paths plus canonical
identifiers (PDS3 `DATA_SET_ID`s and/or PDS4 LIDs). Discovery only: it never
downloads data or fabricates paths/IDs.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install pds-assistant@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing
at the repo root, not the plugin subdir — then the same install command.)

Then invoke the skill directly (`/pds-assistant:pds_live_dataset_finder`) or
just ask, e.g.:

> "Which PDS dataset has calibrated Cassini UVIS spectra of Saturn's rings?"

## Configuration

Tokens are requested interactively when you enable the plugin and stored in
your OS keychain — you never edit a config file.

| Prompt | Backs | Needed when |
|---|---|---|
| **PDS Stage 1 API token** | Live archive directory walking (`pds_list_missions`, `pds_list_dataset_dirs`, `pds_probe_datasets`, `pds_inspect_collections`, `pds_resolve_volume`) | the Stage 1 server requires auth |
| **PDS Stage 2 API token** | Faceted/granule search (`ode_*`, `img_*`, `opus_*`, `sbn_*`, `pds4*` tools) | the Stage 2 server requires auth |

These are FastMCP project tokens (`fmcp_…`). They are **not** stored in the
plugin files — Claude Code prompts at enable time and keeps them in your OS
keychain.

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).
- **Python 3** — the per-node workflow injection (`load_node_workflow` /
  `list_supported_nodes`) is a bundled stdlib-only script the skill runs
  locally; no packages to install. Everything else is remote MCP servers.

## What's inside

```
.claude-plugin/plugin.json          manifest + userConfig prompts
.mcp.json                            MCP servers (URLs are deployment config)
skills/pds_live_dataset_finder/      the skill: SKILL.md + references
  scripts/pds_node_workflows.py      local tool: deterministic per-node workflows
```

## How it works (for maintainers)

- The skill is a two-stage finder: **route** the query to one of 8 PDS nodes
  (GEO, PPI, LROC, IMG, RMS, SBN, ATM, NAIF), then **inject** that node's
  authoritative workflow via `load_node_workflow` and follow it exactly —
  per-node traversal rules live in `scripts/pds_node_workflows.py` (ported
  verbatim from the production `node_registry.py`), not in the prompt. The
  skill runs it with Bash (`python3 scripts/pds_node_workflows.py <node>`).
- **Stage 1** walks live archive directories (cheap, grounded); **Stage 2**
  faceted/granule search is escalation-only, gated by explicit triggers.
- **MCP URLs live in `.mcp.json`, never in the skill markdown.** Auth is
  referenced as `${user_config.pds_stage1_mcp_key}` /
  `${user_config.pds_stage2_mcp_key}` so no token is committed.
- `references/contexts/example-paper-derived-queries.md` holds the router
  few-shot examples (query → expected node).
