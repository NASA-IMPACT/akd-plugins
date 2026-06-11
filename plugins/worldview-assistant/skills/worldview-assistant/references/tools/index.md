# Tool workspace (manifest)

## Organization
- One folder per tool, named exactly as the callable MCP tool name.
- Each tool folder contains an `index.md` describing:
  - purpose
  - when to use
  - inputs / outputs (schema)
  - validation & business rules enforced inside the tool
  - failure modes and retry guidance
  - security / permissions
  - response payload shape (the agent should rely on structured outputs, plus internal `_response` text if present)

## MCP configuration
- `mcp_config.json` — MCP servers and allowed tools to be attached to the final agent.

## Tools
- `geo_ui_render_intent_tool/` — render a GeoIntent → Worldview permalink (primary visualization tool)
- `geo_ui_get_state_tool/` — parse a Worldview URL → GeoIntent (for iterative refinement)
- `worldview_permalink_tool/` — **superseded** by the GeoUI tools above; kept for reference. Builds a permalink from explicit Worldview-shaped params rather than a GeoIntent.
- `umm_vis_lookup_tool/` — lookup Worldview layer-id visualization for a CMR concept-id
- `earthdata_search_landing_page_tool/` — generate Earthdata Search landing page link for a concept-id
- `pdf_parser_tool/` — parse PDFs into extracted text/snippets

- `search_collections/` — CMR collection search
- `get_collection_metadata/` — CMR collection metadata retrieval
- `get_granules/` — CMR granule retrieval (**not used**; kept out of scope)

- `search_worldview_layers/` — search Worldview layers (validation/lookup)
- `validate_temporal_coverage/` — validate requested temporal coverage against dataset constraints

- `sde_search_tool/` — Science Discovery Engine search
- `eonet_search_tool/` — EONET event search
