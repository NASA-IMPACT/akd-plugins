# cmr_search_tool

## What it does

The agent's only search tool. Searches NASA's Common Metadata Repository (CMR) at the
**collection** level, returning candidate datasets with their Concept IDs and UMM metadata.
Granule-level lookup is available but used only after the user selects a collection.

## Why / when to use

- Step 6 (primary discovery), every query, after terms are normalized to GCMD keywords (step 4)
  and mapped to CMR parameters (step 5).
- Provide the confirmed constraints — normalized GCMD prefLabels go in `keyword`, plus
  `platform` / `instrument` / `processing_level` / `temporal` / `bounding_box`. Always retrieve
  **multiple** candidates; never stop at the first match.
- The tool has **no** `sort_key` — order the results **yourself** by metadata relevance;
  usage/popularity is a tie-breaker only (`../../guardrails/ranking-relevance-primary.md`).

## MCP server & enabled state

- Server: `CMR_MCP_Server` — `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp`
- Enabled: `true`
- Allowed tools: `null` (no restriction)
- Authorization: `null` (public)
- `require_approval`: `"never"` (read-only search)

## Files

- `endpoint.md` — CMR endpoints, base URL, response formats, limits.
- `input-output.md` — parameters and returned fields.
- `auth.md` — access model (open for search) and secret handling.
