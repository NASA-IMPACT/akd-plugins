# get_collection_metadata

## Purpose
Fetch detailed CMR collection metadata (UMM-based) for a specific collection concept-id.

## When to use
When the agent has selected (or is comparing) a specific collection and needs authoritative metadata for explanations/caveats.

## Inputs (schema)
- `concept_id` (required): string

## Outputs (schema)
- object (CMR response)
  - TBD (confirm): which UMM fields are stable/required for user-facing explanations.

## Validation & business rules
- `concept_id` is required.

## Failure modes and recovery guidance
TBD (confirm): behavior for missing/invalid concept-id and expected error shape.

## Security / permissions
Public-only.

## Notes
- MCP server label: `CMR_MCP_Server`
- See `tools/mcp_config.json`.
