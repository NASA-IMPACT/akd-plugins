# geo_ui_render_intent_tool

## Purpose
Render an abstract **GeoIntent** (the GeoUI Protocol's app-agnostic
description of a desired map state) into a NASA Worldview permalink URL.

- Pure string assembly (no external I/O).
- The agent reasons in `GeoIntent` terms; the tool handles the
  Worldview-specific URL grammar. This is the app-agnostic counterpart
  of `worldview_permalink_tool`.

## When to use
Use this tool to produce the clickable Worldview link once the layer set
is complete (or when the user explicitly asks for a link). Follows the
same permalink-timing policy: do not emit a link during intermediate
clarification.

## Inputs (schema)
- `intent` (required, object) — the GeoUI Protocol root:
  - `geoui_version` (string, default `"1.0.0"`)
  - `geoui_extensions` (string[]) — URIs of any extensions in use
  - `viewport`: `{ "bbox": [west, south, east, north] | null, "crs": "EPSG:4326" }`
    (`crs` defaults to `"EPSG:4326"`)
  - `time`: `{ "instant": "YYYY-MM-DD" }` **or** `{ "start": "...", "end": "..." }`
    — instant XOR range — or `null`
  - `layers`: array of `{ "id" (required), "visible" (default true), "opacity" (0.0–1.0 | null) }`
  - **additionalProperties allowed** — namespaced extension keys live on
    the intent (e.g. `"compare:layers"`, `"raster-styling:palettes"`)

## Outputs (schema)
- `url` (string) — the Worldview permalink.

## Validation & business rules
- `layers[*].id` must be a GIBS/Worldview layer id (not a CMR concept-id;
  map via `umm_vis_lookup_tool` first if you only have a concept-id).
- **Extensions require BOTH halves:** to use an extension you must add its
  URI to `geoui_extensions` AND populate its namespaced fields. Populating
  namespaced fields (e.g. `"compare:layers"`) without declaring the
  matching URI in `geoui_extensions` is rejected with a `ValueError`.
- `time` cannot be both an instant and a range.

## Failure modes and recovery guidance
- Missing extension URI for present namespaced fields → declare the URI
  in `geoui_extensions` and retry.
- Invalid layer id → re-resolve via `umm_vis_lookup_tool` /
  `search_worldview_layers`.

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-geoui-mcp-tools`.
- Paired with `geo_ui_get_state_tool` (the inverse) for iterative loops.
- See `tools/mcp_config.json`.
