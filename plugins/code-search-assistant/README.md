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

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install code-search-assistant@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing at
the repo root, not the plugin subdir — then the same install command.)

Then invoke the skill directly (`/code-search-assistant:code-search`) or just
ask, e.g.:

> "What public codes implement radiative transfer in protoplanetary disks?"

## Configuration

**No tokens required.** The two primary discovery tools run as a bundled,
stdlib-only Python script that calls a public NASA Science Discovery Engine
endpoint — nothing to configure.

| Optional | Effect |
|---|---|
| `GITHUB_ACCESS_TOKEN` (environment variable) | **Recommended.** GitHub enrichment makes one REST call per repo; the anonymous limit is only **60 requests/hour**, so without a token `reliability_score` can come back **null for GitHub repos** once the anonymous limit is exhausted. Whenever the token is unset and a GitHub repo is returned, the tool proactively adds a top-level `note` flagging this — it does not wait for the limit to actually be hit. With a token, calls are authenticated (~5,000/hr) and scores populate reliably. A null `reliability_score` always means *not scored* — for a non-GitHub URL, missing metadata, or a rate-limited lookup — **never** *unreliable*. Never committed; read from your shell environment. |

## Prerequisites

- **[Claude Code](https://code.claude.com/docs/en/overview)** (this is a Claude Code plugin).
- **Python 3** — the discovery tools are a bundled **stdlib-only** script
  (`scripts/sde_tools.py`); no packages to install.

## What's inside

```
.claude-plugin/plugin.json          manifest
README.md                            this file
skills/code-search/
├── SKILL.md                         the agent's system prompt + runtime notes
├── references/                      scope, contexts (per SMD domain), tool specs, reasoning, output, guardrails
└── scripts/
    └── sde_tools.py         local tools: repository-search + sde-search (SDE-backed, min_score=0)
```

## How it works (for maintainers)

- The skill is the CARE v2 artifact for the Scientific Code Discovery Agent:
  `SKILL.md`'s body is the finalized agent prompt (`agents.md`), and the rest
  of the artifact rides along under `references/` as progressive-disclosure
  context.
- **Tools travel as scripts, not MCP (for now).** The two primary discovery
  tools — `repository_search` (curated science repos via SDE `Software and
  Tools` + GitHub enrichment + a 0–100 reliability score) and `sde_search`
  (NASA Science Discovery Engine) — are ported from the project's
  authoritative pydantic functions into `scripts/sde_tools.py`, preserving
  behavior; the changes vs. the original are `httpx` → stdlib `urllib`, an
  added CLI entrypoint, a display-title helper, JSON error handling, and a
  rate-limit `note`. Both use `min_score=0.0` deliberately. The skill runs them with Bash:
  `python3 "${CLAUDE_SKILL_DIR}/scripts/sde_tools.py" repository-search --query "…"`.
- **External web search** uses Claude Code's built-in web search.
- **Deferred (MCP-backed):** `code_signals_search_tool`, `ascl_search_tool`,
  `ads_search_tool`, `ads_links_resolver_tool` are not wired in this build.
  Practically, the deep-inspection step is skipped and — for **Astrophysics**
  queries — the ASCL/ADS literature/citation pass is unavailable, so the skill
  notes the missing citation evidence in its Search Notes rather than
  fabricating it. A follow-up iteration will add these via an MCP config
  (`.mcp.json`), mirroring `pds-assistant` / `worldview-assistant`.

## Limitations

- Astrophysics **citation-based ranking** (ASCL `used_in_count`, ADS
  `citation_count`) is degraded until the MCP tools are wired — repository
  discovery still works via `repository-search` + SDE + web search.
- Discovery only — never downloads, runs, or endorses code.
