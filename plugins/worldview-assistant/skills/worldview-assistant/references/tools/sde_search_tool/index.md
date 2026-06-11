# sde_search_tool

## Purpose
Search the NASA Science Discovery Engine to expand dataset candidates beyond Worldview-indexed content and CMR.

## When to use
Fallback only.

Use only when nothing suitable is found via Worldview/CMR-based discovery.

## Inputs (schema)
- `query` (required): string
- `limit`: int (default `10`)
- `doc_type`: enum `Data` | `Images` | `Documentation` | `Software and Tools` | `Missions and Instruments` | null

## Outputs (schema)
- `results`
- `extra`

## Validation & business rules
- `query` is required.

## Failure modes and recovery guidance
TBD (confirm).

## Security / permissions
Public-only.

## Notes
- MCP server label: `sde_mcp_tool`
- See `tools/mcp_config.json`.
- This MCP server exposes additional tools, but only `sde_search_tool` is allowlisted.
