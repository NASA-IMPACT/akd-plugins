# Context: External Web Search

## What it is

The builtin `web_search` capability (`search_context_size: medium`). Supplementary discovery only; results must be flagged as externally sourced. The companion `web_fetch` builtin is **disabled** in both tool-config snapshots.

## Role in the pipeline

- **Step 6 (Completeness Check):** the ONLY tool used in this step. After comparing the running list against the Expected Codes checklist a final time, use web search to locate a public repository or project website for each missing code.
- Combine ALL missing code names into a single query (e.g., `"FLASH GitHub" "PLUTO GitHub" "Enzo GitHub"`). Aim to resolve all missing codes in 1–2 queries; **maximum 3**.
- Prioritize `.gov`, `.edu`, `nasa.gov`, `esa.int`, and similar trusted domains.
- Flag externally sourced repositories in the **Provenance** bullet of the output.

## Cross-domain use

Available across all domains as supplementary discovery, but the process reserves it for the Step 6 completeness pass. Externally sourced candidates are retained on the same footing as other channels (see `guardrails/retention-across-channels.md`) but always marked as external.

## Related tool

`tools/web_search/`.
