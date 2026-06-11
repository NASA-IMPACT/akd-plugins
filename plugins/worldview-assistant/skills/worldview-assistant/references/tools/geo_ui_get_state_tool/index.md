# geo_ui_get_state_tool

## Purpose
Inverse of `geo_ui_render_intent_tool`: parse a NASA Worldview URL back
into a **GeoIntent**, so the agent can read the current visualization
state and refine it.

- Pure parsing (no external I/O).

## When to use
At the start of an **iterative-refinement** turn — when the user is
adjusting an already-visualized state (e.g. "zoom here", "change the
date", "add a compare layer"). Recover the current `GeoIntent`, modify
only the fields the user asked to change, then re-render with
`geo_ui_render_intent_tool`.

## Inputs (schema)
- `url` (required, string) — a Worldview permalink URL.

## Outputs (schema)
- `intent` (object) — the same `GeoIntent` schema produced as input by
  `geo_ui_render_intent_tool`.

## Validation & business rules
- **Auto-injected layers are preserved.** Worldview state typically
  includes base reflectance and reference-overlay layers that the user
  did not explicitly choose. These appear in the returned `intent` for
  fidelity — **ignore them when computing refinements**; do not treat
  them as user selections and do not strip them when re-rendering.

## Failure modes and recovery guidance
- Malformed / non-Worldview URL → ask the user to confirm the link, or
  rebuild state from the conversation rather than parsing.

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-geoui-mcp-tools`.
- Paired with `geo_ui_render_intent_tool` (the inverse).
- See `tools/mcp_config.json`.
