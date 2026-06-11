# earthdata_search_landing_page_tool

## Purpose
Generate an Earthdata Search landing page link for a dataset concept-id.

## When to use
Depends on the agent’s output format/requirements (to be finalized in the output-format stage).

At minimum, use when the user requests a handoff from Worldview exploration to Earthdata Search for dataset landing / download exploration.

## Inputs (schema)
`additionalProperties: false`

- `concept_id` (required, string)
  - format: `C<digits>-<PROVIDER>`

## Outputs (schema)
- `url`: string

## Validation & business rules
- `concept_id` must be present and match expected collection concept-id format.

## Failure modes and recovery guidance
TBD (confirm): behavior when concept-id is invalid or Earthdata Search URL cannot be constructed.

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-earthdata_search_landing_page_tool`
- See `tools/mcp_config.json`.
