# Worldview catalog (local layer/category metadata)

## Source
- Folder: `resources/catalog/`
- Example contents observed:
  - `resources/catalog/categories/.../*.json` — category groupings (e.g., featured, hazards_and_disasters, science_disciplines)
  - `resources/catalog/layers/<instrument_or_product_group>/*.json` — layer definition stubs/metadata per layer id

## Purpose
Provide a **local, human-maintainable catalog** of Worldview layer metadata and category groupings that can support:
- intent → candidate layer lookup
- browsing via category groupings
- validating that a referenced `layer_id` exists in the catalog
- lightweight layer attributes used for display/organization (e.g., `group`, `layergroup`, `tags`, `wrapadjacentdays`)

## How this is used in practice (SME)
Used as a **mirror of the Worldview live config** and a **fallback** when live config access is unavailable or insufficient.

## When it becomes relevant (stage)
- When the agent needs to **identify candidate Worldview layers** from a user intent
- When validating or composing Worldview deep links that include `layer_id` values
- When the user requests **category-based exploration** (e.g., “show me floods layers”)

## Task type
- Lookup / validation (reference)

## What parts are actually used vs ignored
TBD (confirm). Based on the files:
- Likely used:
  - `layers.<layer_id>.id`, `description`, `group`, `layergroup`, `tags`
  - per-layer flags like `wrapadjacentdays`
- Likely used:
  - category lists under `categories/` (for browse/grouping)

## Authority
- Reference for Worldview layer organization and ids.
- Not authoritative for scientific meaning/limitations; scientific authority remains with metadata-authoritative sources (e.g., CMR) and official dataset documentation.

## Mandatory vs optional
TBD (confirm).

## Notes / examples observed
- Example layer entry structure (from `resources/catalog/layers/viirs/snpp/...json`):
  - `id`, `description`, `group` (`baselayers`/`overlays`), `layergroup`, `tags`, and sometimes `wrapadjacentdays: true`.

## Open questions
- Is this catalog expected to be the agent’s **primary** source of layer ids and basic attributes?
- How is `resources/catalog/` generated/updated, and what is the refresh cadence?
- Are there canonical schemas for category JSON and layer JSON files we should rely on?
