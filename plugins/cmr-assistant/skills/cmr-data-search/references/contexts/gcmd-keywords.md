# GCMD Science Keywords (bundled vocabulary)

The agent normalizes free-text phenomena/variables into canonical **GCMD Science Keywords**
during the Term-normalization step (step 4 of the reasoning loop) using a bundled snapshot —
there is no live GCMD KMS tool.

## The snapshot

- File: [`../resources/gcmd-science-keywords.json`](../resources/gcmd-science-keywords.json)
- Source: NASA GCMD Keyword Management System (KMS), **Science Keywords** concept scheme.
- Version: **22.6** (~3,670 concepts).
- Shape: a JSON list of concept records with the GCMD keyword hierarchy (category → topic →
  term → variable levels), labels, and identifiers.

## How to use it

1. Take the user-confirmed phenomenon/variables (and any named platform/instrument).
2. Resolve each to its **canonical GCMD Science Keyword** using this snapshot — do not guess
   keywords from memory.
3. If a term maps ambiguously to more than one concept, pick the closest and **ask the user to
   confirm** — do not present long option lists by default.
4. Pass the resolved GCMD prefLabel(s) into the `keyword` parameter of `search_collections`
   (the server has **no** separate `science_keywords` field), alongside any `platform` /
   `instrument` filters. See `cmr-metadata-model.md`.

## How to consult it at runtime

The snapshot is large (~2.6 MB) — **do not load it wholesale into context.** Search the file
for the specific candidate terms and read only the matching records: grep/keyword-search
`../resources/gcmd-science-keywords.json` for each phenomenon/variable (and its synonyms), then
select the canonical GCMD keyword from the matched concept records. Look up a handful of
candidate terms, not the whole vocabulary.

GCMD keywords inform **search terms only** — they must never be surfaced as datasets.

## Refresh

This is a static snapshot (v22.6). If GCMD publishes a newer keyword version and updated
routing is needed, replace this file and update the version noted above. Platforms and
Instruments concept schemes are not bundled here (out of scope for v2); named platforms/
instruments are applied as CMR hard filters directly.
