# umm_vis_lookup_tool

## Purpose
Map a CMR collection concept-id → associated GIBS/Worldview layers.

## When to use
Primary mapping step after collection identification.

Use this tool when the agent has identified a candidate CMR collection (concept-id) and needs the corresponding Worldview/GIBS `layer_id`(s) and visualization details.

Selection rule (agent-side):
- If multiple `layers[]` are returned, the agent should **narrow to a single best layer**.
- If the user’s overall request requires multiple layers, the agent should handle that by calling this tool for each needed collection rather than taking multiple layers from one call.

Tie-break order for selecting the single best layer (highest → lowest priority):
1. Prefer `available_in_gibs = true` (over `false`/`null`).
2. Prefer `layer_id_source` in this order: `best` > `best_pending_gibs` > `name_stripped` > `name_raw` > `unresolved`.
3. Prefer `visualization_type = tiles` over `maps`.
4. If still tied: select the first result returned (deterministic).

## Inputs (schema)
`additionalProperties: false`

- `collection_concept_id` (required, string)
  - pattern: `^C\d+-[A-Z0-9_]+$`
  - example: `C1701805619-GES_DISC`

## Outputs (schema)
- `collection_concept_id` (echo)
- `layers[]` — each layer includes:
  - required/typical fields:
    - `layer_id`
    - `layer_id_source`: enum `best` | `name_stripped` | `name_raw` | `best_pending_gibs` | `unresolved`
    - `available_in_gibs`: bool | null
    - `visualization_concept_id`
    - `visualization_type`: `tiles` | `maps`
  - optional fields:
    - `title`, `subtitle`, `measurement`, `daynight`
    - `spatial_coverage`: `[w, s, e, n]`
    - `temporal_start`, `temporal_end`, `ongoing`
    - `layer_period`
    - `worldview_projections[]`
    - `colormap_url`
- `match_path`: enum `concept_ids` | `source_datasets_fallback`

## Validation & business rules
- `collection_concept_id` must match the required pattern.

## Failure modes and recovery guidance
TBD (confirm): behavior when no layers can be resolved (e.g., `layer_id_source = unresolved`).

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-umm_vis_lookup_tool`
- See `tools/mcp_config.json`.
