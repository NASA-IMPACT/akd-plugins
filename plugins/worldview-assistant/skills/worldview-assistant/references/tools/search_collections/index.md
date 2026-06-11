# search_collections

## Purpose
Search CMR collections to identify candidate datasets/collections for a user intent.

## When to use
When the agent needs authoritative dataset/collection candidates from CMR.

Default behavior:
- Always supply `keyword`.
- If available from the user request/context, also pass any of: `short_name`, `version`, `provider`, `platform`, `instrument`, `processing_level`, `temporal`, and `bounding_box`.

## Inputs (schema)
MCP schema allows all parameters to be optional, but for this agent usage `keyword` is required.

- `keyword` (required for this agent)
- `short_name`
- `version`
- `provider`
- `platform`
- `instrument`
- `processing_level`
- `temporal`: `{ start, end }`
- `bounding_box`: `(w, s, e, n)`
- `page_size`: int (default `10`, max `50`)
- `page_num`: int (default `1`)

## Outputs (schema)
- object (CMR response)
  - TBD (confirm): which response fields are stable/required for the agent.

## Validation & business rules
- Enforce `page_size <= 50`.

## Failure modes and recovery guidance
TBD (confirm): common errors (rate limiting, invalid params) and expected error shape.

## Security / permissions
Public-only.

## Notes
- MCP server label: `CMR_MCP_Server`
- See `tools/mcp_config.json`.
