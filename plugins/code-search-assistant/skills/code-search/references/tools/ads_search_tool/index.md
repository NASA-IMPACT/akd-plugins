# ads_search_tool

## What it does

NASA ADS paper search using Solr syntax. Returns `bibcode`, `title`, `abstract`, `citation_count`, etc. It does NOT extract code URLs from full text — discovery comes from reading the `abstract` field. See `contexts/nasa-ads.md`.

## Why / when to use

- **Astrophysics only, Step 5b.** Discover codes not in ASCL (newer, institutional, unregistered) and find additional description papers. **Maximum 4 queries, `rows=5` each.**
- An ADS title search is **required** for any well-known checklist code if ASCL has fewer than 2 description bibcodes for it, or if the listed entry has `citation_count < 100` for a flagship code.
- Validate that any URL pulled from an abstract resolves to a public host before including it.

## MCP server & enabled state

- Server: `ads-ascl` — `https://ads-ascl.fastmcp.app/mcp`.
- Enabled in the live runtime environment; `allowed_tools` include `ads_search_tool`.

## Files

- `endpoint.md` — MCP server(s).
- `input-output.md` — query patterns, params, returns.
- `auth.md` — bearer token (secret).
