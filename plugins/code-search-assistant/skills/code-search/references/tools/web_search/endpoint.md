# web_search — Endpoint

## Builtin capability

- Provider: builtin `web_search` (not an MCP server; no `server_url`).
- Config: `enabled: true`, `search_context_size: "medium"`.
- Companion builtin `web_fetch` is `enabled: false` (disabled) — the agent cannot fetch page bodies, only search.

## Notes

Because `web_fetch` is disabled, Step 6 relies on the search result snippets/links themselves to locate a public repository or project-website URL; validate that any URL used resolves to a public host.
