# repository_search_tool — Endpoint

## MCP server

- Name: `Code_Search_MCP_Server`
- URL: `https://sde-repo-search.fastmcp.app/mcp`
- `require_approval: "never"`

## Underlying SDE endpoint

This tool calls the SDE code-search endpoint:

- Base URL (default): `https://dyejsbdumgpqz.cloudfront.net/api/code/search` (may be overridden by `SDE_BASE_URL`).
- Method: `POST`, headers `Content-Type: application/json`, `Accept: application/json`, timeout 30s.
- Payload (per query/page):
  - `page: <int>`
  - `pageSize: <int>`
  - `search_term: <query>`
  - `search_type: "hybrid" | "vector" | "keyword"`
  - **`min_score: 0.0`** — sent on every request to avoid server-side default filtering.

## GitHub enrichment endpoint

For each result whose URL contains `github.com`, one REST call:

- URL: `https://api.github.com/repos/{owner}/{repo}`
- Header `Accept: application/vnd.github+json`, plus `Authorization: Bearer <GITHUB_ACCESS_TOKEN>` when the env var is set. Timeout 15s.

## Notes

Same SDE backend as `sde_search_tool` (see `contexts/science-discovery-engine.md`). Results are truncated to `max_results`. `content` snippets are capped at 1500 characters.
