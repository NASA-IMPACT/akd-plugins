# Domain: Heliophysics

## Routing

A non-Astrophysics division. **Step 5 (ASCL + ADS) is skipped entirely.** ADS Evidence in the output is replaced by the single line `- **ADS Evidence:** N/A (non-Astrophysics query)`.

## Channels used

1. `repository_search_tool` — Step 2 primary discovery (≥ 2 distinct queries).
2. `sde_search_tool` — Step 3, one query. **SDE is strongest for Heliophysics** (SPASE and related NASA channels are well-indexed).
3. `code_signals_search_tool` — Step 4, conditional.
4. External web search — Step 6 completeness pass (max 3 queries).

## Channel strategy

- Lean on `repository_search_tool` + SDE; SDE meaningfully surfaces additional repositories from NASA technical reports and mission documentation for this division.
- No citation-library channel; community adoption is judged from repository signals, SDE context, and web-verified provenance rather than ASCL/ADS.

## Tool-call budget

Up to **10 total tool calls** (non-Astrophysics). See `guardrails/max-6-minimum-0.md`.

## Expected Codes checklist

Generated at runtime (Step 1); no stored checklist. See `contexts/index.md`.
