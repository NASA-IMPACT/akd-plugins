# repository_search_tool

## What it does

Primary discovery channel across all SMD domains (Step 2). Searches NASA's Science Discovery Engine (SDE) scoped to code repositories, enriches `github.com` results with GitHub REST metadata, and computes a `reliability_score` for each result.

The v1 prompt labels this tool **"NASA-Verified Repository Search"** (label preserved verbatim in `agents.md`). Its real implementation is **SDE (filtered to `document_type=["Software and Tools"]`) + GitHub enrichment** — NOT a separate NASA-verified repository corpus.

## Why / when to use

- Step 2 primary discovery, every domain: run at least 2 distinct queries with the user's terms, then synonyms / checklist code names / broader category terms if results are sparse.
- Consume `reliability_score` and `repository_metadata` (stars/forks/age/activity) as **supporting-only** ranking signals in Step 7 (see `guardrails/popularity-signals-supporting-only.md`).

## Implementation

Implemented via local script: `scripts/sde_tools.py` (`repository_search_tool`).

## Files

- `endpoint.md` — underlying SDE + GitHub endpoints.
- `input-output.md` — params and returns.
- `auth.md` — GitHub token env var (secret).
