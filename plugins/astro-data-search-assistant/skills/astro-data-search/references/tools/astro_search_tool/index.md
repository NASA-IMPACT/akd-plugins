# astroquery-mcp (astro search server)

## What it does

The read-only MCP server the agent calls to run its planned queries. It is an
**introspection-based** FastMCP server that dynamically exposes astroquery: 14 astronomical data
services / 141 functions, reached through a small set of generic tools. The agent plans which
module + function + parameters to call, then invokes `astroquery_execute` (and the ADS helpers)
to run them.

## Exposed tools

- `astroquery_execute(module_name, function_name, params=None, max_rows=20)` — call any
  astroquery function (the primary path for search/discovery).
- `astroquery_list_modules()`, `astroquery_list_functions(module_name=None)`,
  `astroquery_get_function_info(module_name, function_name)` — introspection to confirm a call
  before running it.
- `astroquery_check_auth()` — downstream service-auth status.
- `ads_query_compact(...)`, `ads_get_paper(bibcode, ...)` — token-efficient ADS literature
  search and paper detail (preferred over generic execute for ADS).

## Why / when to use

- Astroquery-native modules are the default; PyVO-style TAP/ADQL is reachable via the modules'
  `query_tap`/region functions through `astroquery_execute`.
- Introspect first when unsure of a function's parameters (`get_function_info`), then execute.
- **Execution discipline is required:** follow the tool-call rules in `../../reasoning.md`
  ("Tool execution discipline") and `../../agents.md` ("Tool-call discipline"), including:
  introspect before the first execute, never call with partial args, decompose complex boolean
  logic into simpler queries + local filtering, and revise after empty/error rather than repeating
  an identical call.
- For literature, prefer `ads_query_compact` → `ads_get_paper` (far fewer tokens than generic
  execute on ADS).

## Server & enabled state

- Server: `astroquery-mcp` (FastMCP) — `https://coming-gray-slug.fastmcp.app/mcp`.
- **Bearer token required** (confirmed by probe). Read-only.
- `require_approval`: `"never"` (read-only search).

## Files

- `endpoint.md` — MCP server, `.mcp.json` wiring, module TAP/SIA endpoints, limits.
- `input-output.md` — the tool signatures and returned records.
- `auth.md` — the two token layers (client Bearer + server-side service tokens).
