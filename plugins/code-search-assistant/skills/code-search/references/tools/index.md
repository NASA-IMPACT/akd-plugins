# Tools

Six named tools plus the builtin web search, grounded in the deployed tool interfaces/behavior and confirmed live runtime configuration.

Note: `repository_search_tool` and `sde_search_tool` are implemented via local scripts under `scripts/` (implementation detail). Runtime behavior: each top-level function becomes a tool; names starting with `_` are ignored; code runs in an isolated subprocess.

The other named tools are invoked via their respective runtime tool integrations.

Each tool subdir has `index.md`, `endpoint.md`, `input-output.md`, and `auth.md`. Tokens are secrets and are never reproduced here.

## Tool inventory

| Tool | Subdir | Hosting | Purpose |
|---|---|---|---|
| `repository_search_tool` | `repository_search_tool/` | local script (`scripts/sde_tools.py`) | Primary discovery: SDE (Software and Tools) + GitHub enrichment + reliability score. |
| `sde_search_tool` | `sde_search_tool/` | local script (`scripts/sde_tools.py`) | SDE context enrichment. |
| `code_signals_search_tool` | `code_signals_search_tool/` | `Code_Signal` (`developing-purple-wallaby.fastmcp.app`) | Static code inspection to resolve ambiguity. |
| `ascl_search_tool` | `ascl_search_tool/` | `ads-ascl` (`ads-ascl.fastmcp.app`) | Astrophysics code registry discovery. |
| `ads_search_tool` | `ads_search_tool/` | `ads-ascl` (`ads-ascl.fastmcp.app`) | ADS paper search (Solr). |
| `ads_links_resolver_tool` | `ads_links_resolver_tool/` | `ads-ascl` (`ads-ascl.fastmcp.app`) | Recover canonical description papers via `associated_bibcodes`. |
| web search | `web_search/` | builtin `web_search` (`search_context_size: medium`); `web_fetch` disabled | Supplementary Step 6 completeness discovery. |

## Per-domain tool usage

- **All domains (Steps 2–4, 6):** `repository_search_tool` (Step 2, ≥ 2 queries) → `sde_search_tool` (Step 3, one query) → `code_signals_search_tool` (Step 4, conditional) → `web_search` (Step 6, completeness).
- **Astrophysics only (Step 5):** additionally `ascl_search_tool` (5a) → `ads_search_tool` (5b) → `ads_links_resolver_tool` (5c). These three ASCL/ADS channels are **Astrophysics-only** and are skipped for every other division.
- SDE strength by division and full routing: see `contexts/<domain>.md`.

## Tool-call budgets (verbatim)

- **Non-Astrophysics: no more than 10 total tool calls.**
- **Astrophysics: up to 16 total tool calls** (ASCL, ADS, and the resolver expand the discovery surface).
- Per-channel caps: Step 2 ≥ 2 `repository_search` queries; Step 3 one SDE query; Step 5a max 4 ASCL; Step 5b max 4 ADS (`rows=5`); Step 5c max 4 resolver uses (one per ASCL record bibcode; the one tool that may be re-called within a step); Step 6 max 3 web queries. Other tools should not be re-queried within the same step. Request the minimum `rows` needed. See `guardrails/max-6-minimum-0.md`.

## The min_score = 0.0 requirement (SDE-backed tools)

Both `repository_search_tool` and `sde_search_tool` call the SAME SDE endpoint `https://dyejsbdumgpqz.cloudfront.net/api/search` with `search_type="hybrid"` and **`min_score=0.0`**. The threshold of 0 is deliberate — with a non-zero threshold, weak queries return zero results. Preserve `min_score=0.0` wherever these are documented or configured.

## Runtime configuration (confirmed)

Design for the full, live toolchain:
- `repository_search_tool` and `sde_search_tool` are provided via local scripts (see `scripts/sde_tools.py`).
- `ads-ascl` provides `ascl_search_tool`, `ads_search_tool`, and `ads_links_resolver_tool` (Astrophysics Step 5).
- `Code_Signal` provides `code_signals_search_tool`.
- Builtin `web_search` is enabled (`search_context_size: medium`); builtin `web_fetch` is disabled.
