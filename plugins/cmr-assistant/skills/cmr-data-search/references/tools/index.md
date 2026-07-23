# Tools

> **Runtime mapping (packaged plugin).** The connected `cmr` MCP server
> (`CMR Data Server`, `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp/`,
> public / no auth) exposes **three** concrete tools, not a single `cmr_search_tool`. The
> abstract `cmr_search_tool` described below is the design intent; it maps to:
> - `search_collections` — the collection search (step 6).
> - `get_granules` — granule verification after a collection is selected (never for download).
> - `get_collection_metadata` — surface a collection's documentation verbatim.
>
> The authoritative tool names, parameters, and loop mapping the agent actually calls are in
> `../../SKILL.md` (**Tools (MCP runtime)**). This directory is the CARE design record.

One named tool (design abstraction), invoked via its runtime MCP integration. Downloads and
authentication are out of scope. Each tool subdir has `index.md`, `endpoint.md`,
`input-output.md`, and `auth.md`. Tokens are secrets and are never reproduced here.

Controlled-vocabulary normalization does **not** use a tool — it uses the bundled GCMD Science
Keywords snapshot in `../resources/` (see `../contexts/gcmd-keywords.md`).

## Tool inventory

| Tool | Subdir | Hosting | Purpose |
|---|---|---|---|
| `search_collections` | `cmr_search_tool/` | `cmr` server (`CMR Data Server`) — `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp/` | Primary discovery: NASA CMR **collection** search (keyword/platform/instrument/processing_level/temporal/bounding_box) returning Concept IDs + UMM metadata. |
| `get_granules` | `cmr_search_tool/` | (same server) | Granule verification for a user-selected collection — never for download. |
| `get_collection_metadata` | `cmr_search_tool/` | (same server) | Verbatim collection documentation (variables, quality flags, limitations). |

## When to use

- Every search runs through `search_collections` at step 6 of the reasoning loop, after terms
  are normalized to GCMD keywords (step 4) and mapped to CMR parameters (step 5).
- Retrieve multiple candidate collections; page rather than pulling very large result sets.
- Granule-level lookup is used only after the user selects a collection.

## MCP wiring

MCP server configuration is supplied at deployment/packaging time (this workspace does not
store MCP config files or any credentials/tokens).

Recorded server identity for this agent:
- Server name: `CMR_MCP_Server`
- Server URL: `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp`
- Enabled: `true`
- Allowed tools: `null` (no restriction)
- Authorization: `null` (public)
- `require_approval`: `"never"` (read-only)
