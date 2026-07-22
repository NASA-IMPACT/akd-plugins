# code_signals_search_tool — Input / Output

Searches LLM-extracted code signals from GitHub repositories. This tool is the Step 4 fallback when README/SDE context is insufficient to judge relevance.

## Inputs

| Param | Type | Required | Default | Range | Meaning |
|---|---|---:|---|---|---|
| `query` | string | yes | — | — | Search query for code functionality. |
| `limit` | integer | no | 5 | 1–6 | Maximum results to return. |
| `page` | integer | no | 1 | ≥ 1 | Pagination. |

## Output

Returns an object with:

- `results` — list of code-signal hits; each hit contains:
  - `title` — repository id / name
  - `repo_url` — GitHub repository URL
  - `repo_id` — repository identifier
  - `content` — extracted "Code Summary" (function names, class names, imports, data formats, code summaries)
  - `score` — relevance score
  - `query` — echo of the query

## Usage constraints (verbatim from the source prompt)

- Use only when README and SDE context are insufficient to determine relevance.
- Reference file paths or function names; do not include full code excerpts.
- Read-only inspection — no execution, cloning, downloading, or testing (see `guardrails/read-only-no-execution.md`).
