# search_worldview_layers

## Purpose
Search/lookup Worldview layers (hybrid vector + BM25 over layer catalog) and return candidate `layer_id` values.

## When to use
Fallback layer-id lookup.

Use this tool when:
- a relevant CMR collection has already been identified and `umm_vis_lookup_tool` did not yield a usable `layer_id`, and
- the local Worldview catalog mirror (`resources/catalog/`) is insufficient for the needed mapping.

## Inputs (schema)
- `query` (required): string
- `limit`: int (default `10`)

## Outputs (schema)
- object
  - TBD (confirm): required fields in the returned results (e.g., top-k list, layer_id, score, snippets).

## Validation & business rules
- `query` is required.

## Failure modes and recovery guidance
TBD (confirm).

## Security / permissions
Public-only.

## Notes
- MCP server label: `IESO_Validation_MCP_Server`
- See `tools/mcp_config.json`.
