# Context inventory (manifest)

This directory captures the **existing systems, tools, knowledge sources, and operational constraints** the agent may rely on.

## Files
- `worldview.md` — NASA Worldview as the primary visualization UI and deep-link target; capabilities, constraints, and compare-mode support.
- `worldview_url_parameters.md` — Worldview deep-link URL parameter reference (projection, viewport, layers, time, events, animation, compare, charting, modes).
- `cmr.md` — CMR (UMM-based) as authoritative metadata source; MCP endpoint and allowed operations.
- `earthdata_links.md` — Earthdata Search / landing-page handoff links (discovery for download), explicitly excluding automated download/subsetting.
- `eonet.md` — EONET event context (title, geometry, time window, category, external links).
- `sde.md` — Science Discovery Engine as fallback/cross-catalog dataset expansion.
- `worldview_layer_vector_db.md` — Internal semantic index for intent→layer mapping/proxy detection (non-authoritative).
- `document_fetching.md` — Tool concept for fetching ATBD/user guides by concept-id (details TBD).
- `operational_constraints.md` — Global scope constraints, operational limits, and explicit out-of-scope behaviors.
- `open_questions.md` — Inventory unknowns to resolve (endpoints, schemas, identifiers, rate limits, etc.).
- `gcmd_science_keywords.md` — How the agent uses GCMD science keywords CSV for intent enrichment and query expansion (advisory; used when ambiguous).
