# Tools

One **read-only** MCP server — **`astroquery-mcp`** — which the agent calls to run its planned
queries and return candidate datasets. It is introspection-based: rather than one tool per
archive, it exposes a small set of **generic** tools that operate over 14 astroquery modules
(141 functions). Each tool subdir has `index.md`, `endpoint.md`, `input-output.md`, and
`auth.md`. Tokens are secrets and are never reproduced here.

## Server

| Server | Subdir | Hosting | Auth | Purpose |
|---|---|---|---|---|
| `astroquery-mcp` | `astro_search_tool/` | FastMCP — `https://coming-gray-slug.fastmcp.app/mcp` | **Bearer token required** (confirmed) | Read-only astro search over 14 astroquery modules; the agent runs its planned access paths here and gets candidate datasets. |

## Exposed MCP tools (7)

- `astroquery_execute(module_name, function_name, params=None, max_rows=20)` — **the workhorse**:
  call any astroquery function across the 14 modules.
- `astroquery_list_modules()` — list available modules/services.
- `astroquery_list_functions(module_name=None)` — list a module's functions.
- `astroquery_get_function_info(module_name, function_name)` — parameter info for a function.
- `astroquery_check_auth()` — report downstream service-auth status.
- `ads_query_compact(...)` — token-efficient ADS literature search (preferred over generic
  execute for ADS).
- `ads_get_paper(bibcode, ...)` — full details for one ADS paper.

Typical flow: `astroquery_list_functions`/`get_function_info` to confirm a call, then
`astroquery_execute` to run it; for literature use `ads_query_compact` → `ads_get_paper`.

## Modules reachable via `astroquery_execute` (14)

SIMBAD, NED, VizieR, ADS, MAST, MAST Catalogs, HEASARC, IRSA, NASA Exoplanet Archive (NEA),
Gaia, SDSS, ALMA, ESA Hubble, ESA JWST.

**All 14 are in scope** — NASA (MAST, HEASARC, IRSA, NEA, NED, ADS), ESA (Gaia, ESA Hubble, ESA
JWST), CDS (SIMBAD, VizieR), and community (SDSS, ALMA). MAST / HEASARC / IRSA remain the primary
NASA repositories; the ESA/CDS/community modules are used when they fit the query. See
`../guardrails/supported-archives-only.md`.

## MCP wiring

Declared in the plugin's `.mcp.json` at packaging time (this artifact records the wiring; it
does not contain the config file). The server is **token-protected**, so the connection needs a
`headers.Authorization: Bearer ${user_config.astroquery_mcp_key}` entry, with the key declared in
`plugin.json` `userConfig`. Downstream service tokens (ADS `API_DEV_KEY`, MAST `MAST_TOKEN`) are
**server-side** environment variables on the FastMCP deployment, not client config. Details in
`astro_search_tool/endpoint.md` and `astro_search_tool/auth.md`.

Production MCP URL: `https://coming-gray-slug.fastmcp.app/mcp` (confirmed).

Shipped `require_approval`: `"never"` (read-only search).

Bearer token + URL are provisioned via the Labs tool-config UI; in the packaged plugin, `.mcp.json` is wired via `userConfig`.
