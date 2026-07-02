# repository_search_tool — Auth

## Authorization

`repository_search_tool` is implemented as a local script function and does not use an MCP bearer token.

## GitHub enrichment credential (secret — reference only)

- GitHub REST enrichment uses the `GITHUB_ACCESS_TOKEN` environment variable as `Authorization: Bearer <token>`. If unset, enrichment still runs unauthenticated (subject to lower GitHub rate limits) and `reliability_score` may be `null`.
- **Treat `GITHUB_ACCESS_TOKEN` as a secret**; it is an environment variable, never an artifact value.

## Underlying SDE endpoint

The SDE `/api/search` call sends no auth header (Content-Type/Accept only).
