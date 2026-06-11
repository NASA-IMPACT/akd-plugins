# Reasoning strategy specification

## Task decomposition strategy

Preferred default flow:
1. Intake intent
2. Clarify (ask follow-up questions)
3. Find candidate collections
4. Map to `layer_id`
5. Validate time coverage (after candidate `layer_id` is chosen and the user has specified a time window)
6. Assemble final layer set
7. Generate Worldview permalink
8. Present narrative (with relevant optional expansions)

Fallbacks:
- If a candidate collection is not found, use `worldview_catalog` and/or `search_worldview_layers` to identify candidate `layer_id` values.

## TBD
- Clarification vs autonomy thresholds (what must be clarified vs can be assumed) — deferred
- Context retrieval sequencing (when to pull which context docs, how much)

## Context retrieval strategy
- When a context trigger fires, retrieve the relevant context immediately.

## Tool selection & fallback strategy
- Default: always try CMR-based discovery first (`search_collections` → `umm_vis_lookup_tool`).

If CMR-first discovery does not yield a good match (no suitable collections, or only `unresolved` layer mappings):
- Ask the user for additional constraints (e.g., region, time window, phenomenon/variable).
- At the same time, present what is available via the fallback path:
  - candidate layers from `worldview_catalog` and/or `search_worldview_layers`.

## TBD
- Tool selection in ambiguous cases (multiple possible collections/layers)
- Conflict handling and uncertainty disclosure behaviors beyond output-format rules
- Escalation / abstention rules — deferred
- Canonical example flows
