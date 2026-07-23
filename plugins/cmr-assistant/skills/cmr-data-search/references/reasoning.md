# Reasoning Strategy

How the agent thinks. The fixed *presentation* of results is in `output.md`; the hard safety
limits are in `guardrails/`. Follow the loop in order; do not skip steps.

## Scope boundary (hard stop)

- In scope: Earth science — atmosphere, ocean, land, cryosphere, biosphere, solid Earth.
- Out of scope: anything not Earth science, or a request requiring an impossible in-scope
  mapping → say you cannot help and stop (`guardrails/earth-science-only.md`).

## Canonical reasoning loop (authoritative)

### Primary loop — direct discovery first

1. **Interpret.** Extract the main topic / phenomenon and the explicit and implicit variables.
2. **Synonym expansion.** Identify discipline-appropriate synonyms as *candidate* terms only.
   No assumptions.
3. **Clarify (blocking).** Ask about variables, spatial bounds, temporal bounds, and
   indirect-inference permission when relevant. Batch all questions, maximum 5 per pause. No
   partial or speculative searches while waiting (`guardrails/human-in-the-loop-gates.md`).
4. **Term normalization.** Normalize the user-confirmed phenomenon/variables into a small set of
   canonical **GCMD Science Keywords**, using the bundled snapshot
   (`../resources/gcmd-science-keywords.json`; see `contexts/gcmd-keywords.md`). Synonyms remain
   candidates only; if a term maps ambiguously, ask the user to confirm rather than assuming.
5. **CMR parameter mapping.** Translate confirmed terms into `search_collections` filters
   (`keyword`, `platform`, `instrument`, `processing_level`, `temporal`, `bounding_box`, etc.).
   Pass the normalized GCMD prefLabels through the free-text `keyword` parameter — the server
   has **no** separate `science_keywords` field.
6. **Search.** Call `search_collections` on CMR Collections and always retrieve multiple
   candidate datasets.
7. **Rank.** Primary signal: metadata relevance to the science query. Secondary (tie-breaker
   only): usage/popularity (`guardrails/ranking-relevance-primary.md`). Order the returned
   collections **yourself** — the tool exposes no server-side `sort_key`. After shortlisting,
   call `get_collection_metadata` for each candidate: `search_collections` returns lightweight
   records only, and the output's per-dataset fields (variables, spatial coverage, processing
   level) come from the full metadata; anything still missing is **unknown**, never inferred.
8. **Explain.** Explain why each dataset appears, its relevance, and its gaps. No
   recommendations or endorsements.

### Conditional multi-hop loop — indirect discovery

Triggered only when direct discovery is insufficient.

1. **Gap detection.** Direct variables or datasets were not retrieved.
2. **Identify indirect variables** that scientifically affect the main topic (candidate terms
   only).
3. **User confirmation (mandatory)** of the indirect path before any further search.
4. **Re-run the primary loop** (normalize terms → map API → search → rank → explain).

This is a recursive, user-gated loop, **limited to one recursive pass**
(`guardrails/multi-hop-one-loop.md`). If one indirect pass yields no datasets, stop and report
rather than looping further. There is no literature/citation tool — indirect variables come from
the agent's own scientific reasoning, gated by the user, and every surfaced dataset must still
come from CMR.

## Inference vs execution

- The agent **may infer** sensible defaults internally: spatial → Global; temporal → current
  year/month.
- The agent **may not execute** any search using inferred values without explicit user
  confirmation. Inference is allowed; execution is gated. Defaults are never applied silently
  (`guardrails/no-silent-defaults.md`).

## Retrieval, ranking & skepticism

- **Breadth:** always retrieve multiple datasets; never stop at the first acceptable match.
- **Incomplete metadata is neutral** — it neither penalizes nor promotes a dataset. Missing =
  unknown, not bad (`guardrails/metadata-integrity.md`).
- **Field sensitivity:** platform and instrument matter when present but need not be exhaustive;
  resolution, processing level, and variables are optional signals.
- **Perfect vs partial:** direct topic + variables rank first; partial matches only if needed;
  prefer fewer datasets with broader coverage.

## Tool-selection & fallback

- Search tools (see `tools/` and `../SKILL.md` → **Tools (MCP runtime)**): `search_collections`
  (collection discovery), `get_granules` (granule verification after the user selects a
  collection), `get_collection_metadata` (verbatim documentation). Term normalization uses the
  bundled GCMD snapshot, not a live service.
- **Sparse / zero results:** return to clarification, explain the sparsity, propose loosening
  constraints, and proceed only after user approval.
- **Ambiguous GCMD mapping:** select the closest candidate and ask the user to confirm — do not
  present long option lists by default.

## Uncertainty, abstention & escalation

- **Uncertain relevance:** still surface the dataset with an explicit caveat; never withhold a
  relevant candidate purely because of uncertainty.
- **Say you cannot help when:** the query is not Earth science, or required mappings are
  impossible within scope.
- Escalate/pause per `guardrails/human-in-the-loop-gates.md` (repeated ambiguity, denied
  confirmations, repeated zero-result searches, suspected misuse).
