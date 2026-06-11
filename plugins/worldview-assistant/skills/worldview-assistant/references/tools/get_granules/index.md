# get_granules

## Purpose
Fetch CMR granules for a selected collection concept-id.

## When to use
Not used by this agent (out of scope), per the constraint: **no raw granule retrieval**.

## Inputs (schema)
- `collection_concept_id` (required): string
- optional:
  - `temporal`
  - `bounding_box`
  - `point` (lon, lat)
  - `online_only` (bool, default `true`)
  - `downloadable` (bool | null)
  - `page_size`
  - `page_num`

## Outputs (schema)
- object (CMR response)
  - TBD (confirm): which fields (if any) the agent should rely on.

## Validation & business rules
- `collection_concept_id` is required.

## Failure modes and recovery guidance
TBD (confirm).

## Security / permissions
Public-only.

## Notes
- MCP server label: `CMR_MCP_Server`
- See `tools/mcp_config.json`.
