# repository_search_tool — Input / Output

Implemented by local script `scripts/sde_tools.py` (`repository_search_tool`).

## Inputs

| Param | Type | Required | Default | Meaning |
|---|---|---|---|---|
| `query` | str | yes | — | Natural-language or keyword search for scientific code / repositories. |
| `max_results` | int | no | `10` | Maximum number of repositories to return. |

Fixed internally (not caller-controlled): `search_type="hybrid"`, `min_score=0.0`, `filters={"document_type": ["Software and Tools"]}`.

## Outputs

Returns `{ "total_count": <int>, "results": [ … ] }`, plus an optional top-level `note` (string)
present only when `GITHUB_ACCESS_TOKEN` is unset **and** at least one GitHub repo was returned —
it flags that unauthenticated enrichment (60 req/hr) may leave `reliability_score` null for some
repos. On a runtime failure the tool instead returns `{ "error": <str>, "total_count": 0, "results": [] }`.

Each result:

| Field | Source | Notes |
|---|---|---|
| `title` | derived | `owner/repo` for a github.com repository URL, else the SDE `title` (falling back to the URL's last path segment). |
| `url` | SDE `url` | Candidate code URL. |
| `content` | SDE `full_text`/`description` | Truncated to 1500 chars. |
| `score` | SDE `_score` | Relevance score (with `min_score=0.0`, may be low). |
| `reliability_score` | computed | 0–100, tool-owned; `null` for non-GitHub URLs or when metadata is missing. |
| `repository_metadata` | GitHub REST | `stars`, `forks`, `watchers`, `open_issues`, `created_at`, `last_updated`, `first_commit_date`; empty `{}` for non-GitHub URLs. |

## reliability_score (tool-owned; do not recompute)

> Score = (Age · 0.20) + (Activity · 0.25) + (Stars · 0.25) + (Forks · 0.15) + (History · 0.15)

- Age: reaches 100% after 4 years (1460 days).
- Activity: 100% down to 0% as time since last update approaches 1 year.
- Stars: logarithmic, ~1,000 stars = 100%.
- Forks: logarithmic, ~500 forks = 100%.
- History: reaches 100% after 4 years.

The agent consumes `reliability_score` and `repository_metadata` as **supporting-only** Step 7 signals (`guardrails/popularity-signals-supporting-only.md`). See also `contexts/github-metadata.md`.
