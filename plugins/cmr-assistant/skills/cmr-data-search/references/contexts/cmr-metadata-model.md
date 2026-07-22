# CMR Search API & Metadata Model

The knowledge behind constructing NASA Earthdata / CMR collection searches and interpreting the
results. This agent reaches CMR through the connected `cmr` MCP server — at runtime that is the
`search_collections` tool (the CARE design's abstract `cmr_search_tool`; see
`../tools/cmr_search_tool/` and `../../SKILL.md`). This file is the model of what CMR returns and
how to query it well; the CMR Search REST API it wraps is documented at
`https://cmr.earthdata.nasa.gov/search/`.

> **Tool vs REST API.** The sections below describe the full CMR Search REST API. The agent does
> **not** call it directly — it calls the `search_collections` MCP tool, which exposes only:
> `keyword`, `short_name`, `version`, `provider`, `platform`, `instrument`, `processing_level`,
> `temporal`, `bounding_box`, `page_size`, `page_num`. REST parameters described below that are
> **not** in that list — notably `science_keywords` and `sort_key` — are **unavailable through
> the tool**: route normalized GCMD prefLabels through `keyword`, and do relevance ordering
> yourself (there is no server-side sort).

## Core concepts

- **Collection** — a grouping of related data files (a dataset). Discovery happens at the
  **collection** level; this is what the agent searches and returns.
- **Granule** — an individual data file within a collection (e.g. one HDF file). Relevant only
  *after* the user has selected a collection.
- **Concept ID** — the unique identifier for a CMR concept, format
  `<prefix><number>-<provider>`. Collections start with `C` (e.g. `C123456-LPDAAC_ECS`);
  granules start with `G`. A valid Concept ID is the required identifier for any surfaced
  dataset.
- **Provider** — the data center hosting the data (e.g. `LPDAAC_ECS`, `NSIDC_ECS`).
- **Platform** — the satellite/aircraft carrying the instrument (e.g. Terra, Aqua, Landsat-8).
- **Instrument** — the sensor that collected the data (e.g. MODIS, VIIRS, ASTER).
- **Dataset** — synonym for collection.

## Metadata standards

- **UMM** (Unified Metadata Model) — NASA's standard Earth science metadata model. **UMM-JSON**
  is the preferred response format when richer structured metadata is needed.
- **DIF** — GCMD's Directory Interchange Format.
- **ECHO** — legacy metadata format.
- **STAC** — SpatioTemporal Asset Catalog, a modern geospatial standard CMR can emit.

## Endpoints

- **`/search/collections`** — the primary discovery endpoint; where every search runs.
- **`/search/granules`** — used only after the user confirms a collection (to look inside it).
- Also available (rarely needed here): `/search/variables`, `/search/services`,
  `/search/tools`, `/search/autocomplete`, and faceted search.

## Access & authentication

Search and metadata access are **open — no token or login required**. Earthdata Login is needed
only to *download* data, which is **out of scope** for this agent. The agent must never request,
store, or use credentials/tokens.

## Building a collection query

At least one constraint is required — prefer `keyword`. If the query names a platform or
instrument, apply it as a hard filter.

**Common parameters**
- `keyword` — free-text search across collection metadata.
- `concept_id` — fetch a specific concept by ID.
- `provider` — filter by data provider.
- `sort_key` — ranking control (see below).
- `page_size` (default 10, max 2000), `page_num` (1-based) — paging.

**Collection constraints**
- `short_name`, `version` — identify a known collection.
- `temporal` — `YYYY-MM-DDTHH:mm:ssZ,YYYY-MM-DDTHH:mm:ssZ` (apply only after user confirmation).
- `platform`, `instrument` — GCMD-normalized hard filters.
- `science_keywords` — the GCMD Science Keyword hierarchy. Normalize the user's
  phenomena/variables against the bundled vocabulary snapshot
  ([`../resources/gcmd-science-keywords.json`](../resources/gcmd-science-keywords.json)) before
  using this filter (see `gcmd-keywords.md`).
- `project` — project/mission name.
- `processing_level` — L0, L1A, L1B, L2, L3, L4.
- `data_center`, `archive_center` — organizational filters.
- `spatial` (`bounding_box=west,south,east,north`, `point=lon,lat`, `polygon` in WKT) — apply
  only after user confirmation.

**Advanced options** — `options[case_sensitive]`, `options[pattern]`, `options[ignore_case]`,
`options[and]` (AND logic across multiple values of a field).

## Response formats

- **JSON** (default) and **UMM-JSON** (preferred for rich structured metadata). Others: XML,
  ATOM, CSV, KML, STAC.
- Select via `Accept` header, a `.json`/`.umm_json`/… extension, or `?format=`.

## Reading the response

CMR returns a `hits` count and an `items` array. Each item carries `meta` (concept type, native
id, provider) and `umm` (descriptive metadata). **Missing fields are treated as unknown, never
inferred.**

```json
{
  "hits": 1234,
  "took": 45,
  "items": [
    {
      "concept_id": "C123456-LPDAAC_ECS",
      "provider_id": "LPDAAC_ECS",
      "meta": { "concept_type": "collection", "native_id": "MOD09A1_V6.1" },
      "umm": {
        "EntryTitle": "MODIS/Terra Surface Reflectance 8-Day L3 Global 500m SIN Grid V061",
        "ShortName": "MOD09A1",
        "Version": "6.1",
        "Platforms": [ { "ShortName": "Terra", "LongName": "Earth Observing System, Terra" } ]
      }
    }
  ]
}
```

**Fields the agent extracts per collection:** Concept ID · short name / entry title ·
description/summary · variables (verbatim) · temporal coverage · spatial coverage · platforms
and instruments · ProcessingLevelId · related URLs (documentation / DAAC landing pages only; no direct download links).

## Ranking

Request ordering from CMR via `sort_key`. Primary signal: **metadata relevance** to the science
query. Usage/popularity is allowed only as a **secondary tie-breaker**, never overriding
relevance (see `../reasoning.md`, `../output.md`, and
`../guardrails/ranking-relevance-primary.md`).

## Limits & performance

- `page_size` up to 2000; **paginate** rather than pulling very large result sets.
- **URL length ~6,000 chars max** — combining many fields with many values overflows it;
  construct queries conservatively and page.
- Request timeout ~180s (internal query timeout ~170s).
- Rate limiting returns **HTTP 429** with a `retry-after` header → back off (exponential) and
  retry.

## Error handling

Common status codes: `200` success · `400` bad request (invalid parameters) · `404` not found ·
`429` rate limited · `500` server error. Errors come back as:

```json
{ "errors": [ { "code": "INVALID_PARAMETER", "message": "Parameter 'temporal' is not valid" } ] }
```

## Query patterns

```text
# Keyword + provider
GET /search/collections?keyword=temperature&provider=NSIDC_ECS

# Platform + spatial (after user confirmation)
GET /search/collections?bounding_box=-180,-90,180,90&platform=Terra

# Paginated, sorted
GET /search/collections?page_size=50&page_num=2&sort_key=short_name

# Granules within a chosen collection (only after selection)
GET /search/granules?collection_concept_id=C123456-LPDAAC_ECS&temporal=2023-01-01T00:00:00Z,2023-12-31T23:59:59Z
```

## Reference

- CMR Search API docs: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html
- UMM specification: https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/common-metadata-repository
