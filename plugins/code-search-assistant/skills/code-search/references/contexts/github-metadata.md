# Context: GitHub Metadata Enrichment & Reliability Score

## What it is

For each SDE "Software and Tools" result whose URL is on `github.com`, `repository_search_tool` fetches repository metadata from the GitHub REST API (`https://api.github.com/repos/{owner}/{repo}`) using the `GITHUB_ACCESS_TOKEN` environment variable, and computes a `reliability_score`. This is enrichment layered on top of the SDE backend (see `contexts/science-discovery-engine.md`) — it is not a separate corpus. Source of truth: deployed tool behavior.

## Metadata fetched

stars (`stargazers_count`), forks (`forks_count`), watchers (`subscribers_count`), open issues (`open_issues_count`), `created_at`, and `pushed_at` (last updated). Non-GitHub URLs are not enriched (`repository_metadata` is empty and `reliability_score` is `null`).

## The reliability score (the TOOL owns this score)

The `reliability_score` (0–100) is a weighted average computed by the tool, ported verbatim from akd-ext `calculate_reliability_score`:

> Score = (Age · 0.20) + (Activity · 0.25) + (Stars · 0.25) + (Forks · 0.15) + (History · 0.15)

- **Age (20%)** — higher for older repos; reaches 100% after 4 years (1460 days).
- **Activity (25%)** — starts at 100% and drops toward 0% if the repo hasn't been updated in a year.
- **Stars (25%)** — logarithmic; ~1,000 stars = 100%.
- **Forks (15%)** — logarithmic; ~500 forks = 100%.
- **History (15%)** — span between first commit and now; reaches 100% after 4 years.

The score is computed by the tool, not by the agent. The agent consumes it (and the raw metadata) as **supporting-only** ranking signals — see `guardrails/popularity-signals-supporting-only.md`.

## Important correction (label vs. implementation)

The v1 prompt labels `repository_search_tool` "NASA-Verified Repository Search." That label is preserved verbatim in `agents.md`, but the real implementation is **SDE (Software and Tools) + GitHub enrichment**, NOT a separate NASA-verified repository corpus.

## Related tool

`tools/repository_search_tool/`.
