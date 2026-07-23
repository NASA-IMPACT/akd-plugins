# cmr_search_tool — Auth

## CMR access model

CMR **collection search and metadata access require no authentication** — they are open.
Earthdata Login is needed only to *download* data, which is **out of scope** for this agent.
The agent must never request, store, or use Earthdata credentials or tokens
(`../../guardrails/no-downloads-or-credentials.md`).

## MCP authorization

This deployment uses a public MCP server configuration (`authorization: null`), so no auth
headers are required.

If a future deployment adds authorization, treat any token as a secret: the literal value must
never appear in this workspace.
