# Domain: Biological and Physical Sciences (BPS)

## Routing

A non-Astrophysics division. **Step 5 (ASCL + ADS) is skipped entirely.** ADS Evidence in the output is replaced by the single line `- **ADS Evidence:** N/A (non-Astrophysics query)`.

## Channels used

1. `repository_search_tool` — Step 2 primary discovery (≥ 2 distinct query strings; may be batched via `queries=[...]`).
2. `sde_search_tool` — Step 3, one query.
3. `code_signals_search_tool` — Step 4, conditional.
4. External web search — Step 6 completeness pass (max 3 queries).

## Channel strategy

- Same non-Astrophysics routing as Earth Science, Heliophysics, and Planetary Science: `repository_search_tool` + one SDE query + conditional code signals + web completeness pass; no ASCL/ADS.
- No citation-library channel; community adoption is judged from repository signals, SDE context, and web-verified provenance rather than ASCL/ADS.

No specific SDE strength claim is made for Biological and Physical Sciences in the source prompt. Treat SDE as **general-purpose enrichment** (run the standard Step 3 query), with no elevated or reduced expectation. Because SDE’s major indexed sources (CMR, PDS, SPASE, GCN) do not specifically target BPS, do not imply SDE is a strong BPS channel; for BPS, Step 2 (`repository_search_tool`) and Step 6 (web search) carry the primary discovery load.

## Tool-call budget

Up to **10 total tool calls** (non-Astrophysics). See `guardrails/max-6-minimum-0.md`.

## Expected Codes checklist

Generated at runtime (Step 1); no stored checklist. See `contexts/index.md`.
