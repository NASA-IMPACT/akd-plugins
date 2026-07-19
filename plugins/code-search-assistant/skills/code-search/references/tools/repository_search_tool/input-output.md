# repository_search_tool — Input / Output

Searches the SDE code index for repository-like resources, then enriches GitHub URLs with GitHub REST metadata and computes a tool-owned `reliability_score`.

## Inputs

| Param | Type | Required | Default | Meaning |
|---|---|---|---|---|
| `queries` | list[str] | yes | — | One or more natural-language/keyword queries (the tool executes one search per query, then merges/deduplicates results). |
| `max_results` | int | no | 10 | Maximum results to return (after merging/deduplication). |

Notes:
- Step 2 requires **at least 2 distinct query strings**; these may be provided in a single call via `queries`.
- The tool sends **`min_score=0.0` on every request** to avoid server-side default filtering.
- Search mode (`hybrid`/`vector`/`keyword`), paging, and other backend controls are instance configuration (not caller-controlled).

## Outputs

Returns an object with:
- `results`: list of result items, each including:
  - `title`, `url`, `content`, `query` (echo)
  - `reliability_score` (0–100 or `null`)
  - `repository_metadata` (GitHub-derived when applicable)
- `extra`: tool-provided metadata (e.g., counts)

## reliability_score (tool-owned; do not recompute)

> Score = (Age · 0.20) + (Activity · 0.25) + (Stars · 0.25) + (Forks · 0.15) + (History · 0.15)

The agent consumes `reliability_score` and `repository_metadata` as **supporting-only** Step 7 signals (see `guardrails/popularity-signals-supporting-only.md`).
