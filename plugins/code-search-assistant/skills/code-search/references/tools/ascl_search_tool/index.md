# ascl_search_tool

## What it does

Searches the Astrophysics Source Code Library (ASCL), a code-first registry. Highest-yield channel for astrophysics code discovery — every entry is code-first with a canonical URL and ADS bibcodes for description and usage papers. See `contexts/ascl.md`.

## Why / when to use

- **Astrophysics only, Step 5a.** Skip entirely for non-Astrophysics queries.
- Run queries by core task terms at `rows=10`; run name lookups for each missing checklist code at `rows=5`. **Maximum 4 ASCL queries.**
- Pick the best URL from `site_list` using the URL priority (`guardrails/url-and-hosting-rules.md`); never use the ASCL landing page as a code URL.

## MCP server & enabled state

- Server: `ads-ascl` — `https://ads-ascl.fastmcp.app/mcp`.
- Enabled in the live runtime environment; `allowed_tools` include `ascl_search_tool`.

## Files

- `endpoint.md` — MCP server.
- `input-output.md` — params and returns (from the prompt's record description).
- `auth.md` — bearer token (secret).
