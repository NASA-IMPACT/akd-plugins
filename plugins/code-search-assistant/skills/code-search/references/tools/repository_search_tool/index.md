# repository_search_tool

## What it does

Primary discovery channel across all SMD domains (Step 2). Searches NASA's Science Discovery Engine (SDE) scoped to code repositories, enriches `github.com` results with GitHub REST metadata, and computes a `reliability_score` for each result.

The v1 prompt labels this tool **"NASA-Verified Repository Search"** (label preserved verbatim in `agents.md`). Its real implementation is **SDE code search + GitHub enrichment** — NOT a separate NASA-verified repository corpus.

## Why / when to use

- Step 2 primary discovery, every domain: provide **at least 2 distinct query strings** (batched into a single call via `queries=[...]`), then add synonyms / checklist code names / broader category terms if results are sparse.
- Consume `reliability_score` and `repository_metadata` (stars/forks/age/activity) as **supporting-only** ranking signals in Step 7 (see `guardrails/popularity-signals-supporting-only.md`).

## MCP server & enabled state

- Server: `Code_Search_MCP_Server` — `https://sde-repo-search.fastmcp.app/mcp`.
- `require_approval: "never"`

## Files

- `endpoint.md` — underlying SDE + GitHub endpoints.
- `input-output.md` — params and returns.
- `auth.md` — MCP authorization (if provisioned) + GitHub token env var (secret).
