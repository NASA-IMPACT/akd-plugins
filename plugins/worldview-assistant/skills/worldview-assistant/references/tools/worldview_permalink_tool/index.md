# worldview_permalink_tool

## Purpose
Build a NASA Worldview deep-link URL (permalink) representing a desired Worldview UI state.

- Pure string assembly (no external I/O)
- Layer IDs must be **GIBS/Worldview layer IDs**, not CMR concept-ids

## When to use
Use this tool to provide a clickable Worldview link that reproduces a requested configuration (layers, time, viewport, compare mode, charting mode).

Permalink timing policy:
- Generate/provide a permalink **when the layer set is complete** (i.e., after follow-up questions are resolved and the agent has a final layer configuration).
- Also generate/provide a permalink when the user explicitly asks for a Worldview link.
- Do **not** provide permalinks during intermediate follow-up / clarification questions.

## Inputs (schema)
`additionalProperties: false`

- `layers` (required): `LayerSpec[]` — render order (top last)
  - `LayerSpec`:
    - `id` (required, string): GIBS layer id
    - `hidden` (bool, default `false`)
    - `opacity` (number `0.0..1.0` | null)
    - `palettes` (string[] | null)
    - `style` (string | null)
    - `min` (number | null)
    - `max` (number | null)
    - `squash` (bool, default `false`)
- `projection`: enum `geographic` (default) | `arctic` | `antarctic`
- `time`: date / date-time / string | null (default: yesterday UTC)
- `bbox`: `[west, south, east, north]` (4 numbers) | null
- `rotation`: number `-180..180` | null (arctic/antarctic only)

Compare mode
- `compare_active`: bool | null
  - `null` = off
  - `true` = A state active
  - `false` = B state active
  - When set (not null), `compare_layers` is required
- `compare_layers`: `LayerSpec[]` | null
- `compare_time`: date / date-time / string | null
- `compare_mode`: enum `swipe` (default) | `spy` | `opacity`
- `compare_value`: int `0..100` (default `50`)

Charting mode
- `chart_active`: bool (default `false`) — when `true`, `chart_layer` required
- `chart_layer`: string | null
- `chart_area`: `[x1, y1, x2, y2]` | null
- `chart_time_start`: date / date-time / string | null
- `chart_time_end`: date / date-time / string | null
- `chart_autoload`: bool (default `false`)

## Outputs (schema)
- `url`: string

## Validation & business rules
- `layers[*].id` must be a GIBS/Worldview layer id.
- If `compare_active` is not null: `compare_layers` required.
- If `chart_active` is true: `chart_layer` required.

## Failure modes and recovery guidance
TBD (confirm): expected error behavior for invalid layer ids, invalid bbox, invalid date formats.

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-worldview_permalink_tool`
- See `tools/mcp_config.json`.
