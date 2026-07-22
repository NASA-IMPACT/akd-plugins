# Contexts

Domain knowledge and reference vocabularies the agent grounds its answers in.

## Domain knowledge

- [`cmr-metadata-model.md`](cmr-metadata-model.md) — the CMR Search API and metadata model:
  concepts (collections, granules, Concept IDs), how to build a collection query (parameters,
  spatial/temporal, `science_keywords`), response formats, the fields to read, ranking, limits,
  errors, and query patterns. The core reference for constructing searches and interpreting
  results.
- [`earth-science-domains.md`](earth-science-domains.md) — the in-scope Earth science domains
  and how to decompose a query into a phenomenon and its variables.

## Controlled vocabulary

- [`gcmd-keywords.md`](gcmd-keywords.md) — describes the bundled **GCMD Science Keywords**
  snapshot ([`../resources/gcmd-science-keywords.json`](../resources/gcmd-science-keywords.json))
  and how the agent uses it to normalize phenomena/variables into canonical GCMD keywords during
  the Term-normalization step before querying CMR.
