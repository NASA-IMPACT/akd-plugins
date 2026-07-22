# sde_search_tool

## What it does

Searches NASA's Science Discovery Engine (SDE) via the unified `/api/search` endpoint — cross-source vector, keyword, and hybrid semantic search over all indexed NASA content (CMR, PDS, SPASE, GCN, code repositories, documentation). Used for context enrichment: validating domain alignment, refining repository purpose, and surfacing additional repositories from NASA technical reports and mission documentation. Implementation is confirmed in the deployed tool behavior.

## Why / when to use

- **Step 3 (one query)** using the user's core scientific terms.
- SDE is strongest for **Earth Science, Heliophysics, and Planetary Science**; **lower-yield for Astrophysics** (keep to one brief query and rely on Step 5). See `contexts/science-discovery-engine.md`.

## MCP server & enabled state

- Server: `Code_Search_MCP_Server` — `https://sde-repo-search.fastmcp.app/mcp`.
- `require_approval: "never"`

## Files

- `endpoint.md` — underlying SDE endpoint.
- `input-output.md` — params and returns.
- `auth.md` — MCP authorization (if provisioned).
