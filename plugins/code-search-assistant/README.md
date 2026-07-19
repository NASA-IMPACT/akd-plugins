# Code Search Assistant — Claude Code plugin

Find **publicly available scientific code** in natural language. Give it a
research or technical task — "adaptive-mesh hydrodynamics codes", "an MCMC
sampler for exoplanet transit timing", or a sentence from a paper's methods
section — and the bundled skill discovers candidate repositories across NASA
SMD domains (Astrophysics, Earth Science, Heliophysics, Planetary Science,
Biological & Physical Sciences), evaluates them, and returns a **comparative,
ranked list of up to 6** with URLs, evidence, and reliability signals. It is
**read-only and human-in-the-loop**: it never endorses a "best" choice, never
fabricates repos or metadata, and **abstains** when nothing fits.

It runs on **your own Claude** (no separate LLM API key). Its discovery tools
are hosted **MCP servers** that you authenticate with FastMCP tokens (see
Configuration).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install code-search-assistant@akd-agents
```

Set the MCP tokens below (you're prompted at install, or can edit them later in
your Claude Code plugin config). Then invoke the skill directly
(`/code-search-assistant:code-search`) or just ask, e.g.:

> "What public codes implement radiative transfer in protoplanetary disks?"

## Configuration

The discovery tools are hosted **MCP servers** declared in `.mcp.json`; each
needs a FastMCP bearer token supplied through the plugin's `userConfig` and
stored as a secret (never committed). All three servers reject unauthenticated
requests, so the relevant token must be set for those tools to work.

| Token (`userConfig`) | MCP server | Enables | Needed for |
|---|---|---|---|
| `code_search_mcp_key` | `code-search` — `sde-repo-search.fastmcp.app` | `repository_search_tool`, `sde_search_tool` | **Core discovery** — required for the primary pipeline. |
| `ads_ascl_mcp_key` | `ads-ascl` — `ads-ascl.fastmcp.app` | `ascl_search_tool`, `ads_search_tool`, `ads_links_resolver_tool` | **Astrophysics citation ranking** (Step 5). Non-Astro queries work without it. |
| `code_signals_mcp_key` | `code-signal` — `developing-purple-wallaby.fastmcp.app` | `code_signals_search_tool` | Optional static-code inspection (Step 4). |

If a token is blank, that server's tools are unavailable and the agent **notes
the missing channel rather than fabricating** results. (GitHub enrichment for
the `reliability_score` uses a `GITHUB_ACCESS_TOKEN` configured on the
`code-search` **server**, not in this plugin.)

## Prerequisites

- **[Claude Code](https://code.claude.com/docs/en/overview)** (this is a Claude Code plugin).
- **FastMCP tokens** for the MCP servers above (at minimum `code_search_mcp_key`).
- No local runtime, packages, or Python — the tools run server-side over MCP.

## What's inside

```
.claude-plugin/plugin.json          manifest + userConfig (MCP token prompts)
.mcp.json                            the 3 MCP servers (code-search, ads-ascl, code-signal)
README.md                            this file
skills/code-search/
├── SKILL.md                         the agent's system prompt + runtime notes
└── references/                      scope, contexts (per SMD domain), tool specs, reasoning, output, guardrails
```

## How it works (for maintainers)

- The skill is the CARE v2 artifact for the Scientific Code Discovery Agent:
  `SKILL.md`'s body is the finalized agent prompt (`agents.md`), and the rest
  of the artifact rides along under `references/` as progressive-disclosure
  context.
- **All tools are MCP** (mirroring `pds-assistant` / `worldview-assistant`),
  declared in `.mcp.json` across three FastMCP servers:
  - `code-search` — `repository_search_tool` (curated science repos via the SDE
    code index + GitHub enrichment + a 0–100 reliability score) and
    `sde_search_tool` (NASA Science Discovery Engine). Both send `min_score=0.0`
    server-side (otherwise the SDE default threshold silently drops results).
    `repository_search_tool` takes a **batch of `queries`** and merges/dedups them.
  - `ads-ascl` — `ascl_search_tool`, `ads_search_tool`, `ads_links_resolver_tool`
    (the Astrophysics ASCL/ADS citation channel, Step 5).
  - `code-signal` — `code_signals_search_tool` (static code inspection, Step 4).
- **External web search** uses Claude Code's built-in web search (Step 6).
- The plugin ships **no scripts and has no local runtime dependency**; MCP
  tokens are supplied via `userConfig` and stored as secrets.

## Limitations

- Full functionality depends on the MCP servers being reachable and the
  corresponding tokens being set; a missing token disables that channel (the
  agent says so rather than fabricating).
- Discovery only — never downloads, runs, or endorses code.
