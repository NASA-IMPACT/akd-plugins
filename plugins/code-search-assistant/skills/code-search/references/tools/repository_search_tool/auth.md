# repository_search_tool — Auth

## MCP authorization (secret — reference only)

- The MCP connection may use a bearer `authorization` token supplied in the runtime client config.
- **Treat this token as a secret.** The literal value must not be stored in this workspace.

## GitHub enrichment credential (secret — reference only)

- GitHub REST enrichment uses the `GITHUB_ACCESS_TOKEN` environment variable as `Authorization: Bearer <token>`. If unset, enrichment still runs unauthenticated (subject to lower GitHub rate limits) and `reliability_score` may be `null`.
- **Treat `GITHUB_ACCESS_TOKEN` as a secret**; it is an environment variable, never an artifact value.

## Underlying SDE endpoint

The underlying SDE call sends no auth header (Content-Type/Accept only).
