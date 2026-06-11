# validate_temporal_coverage

## Purpose
Validate that a requested acquisition date range is within a layer’s supported temporal coverage.

## When to use
Only after a candidate `layer_id` has been chosen **and** the user has specified a time window.

(Do not call this tool before a layer is selected.)

## Inputs (schema)
- `layer_id` (required): string
- `acquisition_start_date` (required): string date in one of:
  - `YYYY`
  - `YYYY-MM`
  - `YYYY-MM-DD`
- `acquisition_end_date` (required): string date in one of:
  - `YYYY`
  - `YYYY-MM`
  - `YYYY-MM-DD`

## Outputs (schema)
- object
  - TBD (confirm): response fields indicating valid/invalid and suggested adjustments (if any).

## Validation & business rules
- All three fields are required.

## Failure modes and recovery guidance
TBD (confirm).

## Security / permissions
Public-only.

## Notes
- MCP server label: `IESO_Validation_MCP_Server`
- See `tools/mcp_config.json`.
