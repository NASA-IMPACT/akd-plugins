# repository_search_tool — Endpoint

## Implementation

Local script function: `scripts/sde_tools.py` (`repository_search_tool`).

## Underlying SDE endpoint

`repository_search_tool` issues a single POST to the shared SDE endpoint:

- URL: `https://dyejsbdumgpqz.cloudfront.net/api/search`
- Method: `POST`, headers `Content-Type: application/json`, `Accept: application/json`, timeout 30s.
- Payload:
  - `page: 1`
  - `pageSize: max_results`
  - `search_term: <query>`
  - `search_type: "hybrid"`
  - **`min_score: 0.0`** — deliberate threshold-zero (else weak queries return zero results); preserve exactly.
  - `filters: {"document_type": ["Software and Tools"]}`

## GitHub enrichment endpoint

For each result whose URL contains `github.com`, one REST call:

- URL: `https://api.github.com/repos/{owner}/{repo}`
- Header `Accept: application/vnd.github+json`, plus `Authorization: Bearer <GITHUB_ACCESS_TOKEN>` when the env var is set. Timeout 15s.

## Notes

Same SDE backend as `sde_search_tool` (see `contexts/science-discovery-engine.md`). Results are truncated to `max_results`. `content` snippets are capped at 1500 characters.
