# Contract (draft)

## Operations (TBD)
TBD: whether this tool exposes a single `operation` field (e.g., `discover_investigations`, `search_files`, `retrieve_file`, `navigate_dataset`, `lookup_publication`) or separate tool entrypoints.

## Backing systems
- PSI Public Investigations API (REST/HTTPS; public/no auth)
  - `GET /api/investigations/metadata`
  - `GET /api/investigations/files/search/{INVESTIGATION_IDs}`
  - `GET /api/investigations/{INVESTIGATION_ID}/download`
- DataCite REST API (external)

## Confirmed behaviors / constraints
- Support PSI ID ranges like `PSI-100,PSI-105-PSI-110`.
- Pagination: page index starts at 0; max page size = 25.
- Signed download URLs expire after ~7 days; may require re-query.
- Known performance risk: timeouts for very large investigations (>10k files).
- Known data issue: `/legacy/` subset has elevated missing-file (404) risk.
- Migration constraint: path transition `geode-py/ws/` → `psi/data/` (client-side config switch or fallback needed).

## Output shape (TBD)
TBD: whether outputs should include raw API payloads, summarized payloads, or both.

## Error/response guidance expectations
- Include guidance: retry, re-query expired URLs, legacy missing-risk warning, narrow large result sets.

## Open questions
- Whether DataCite lookup should live inside this same tool vs separate tool.
- Whether the tool should auto-page across file-search results.
- Thresholds for when to summarize (vs return raw).
- Whether retrieved files should preserve PSI folder structure under a user-selected destination.
- Whether `/legacy/` files should always be flagged as missing-risk.
- Whether expired S3 URLs should trigger automatic re-query.
- Whether investigations estimated >10,000 files should require narrowing first.
- Standard error schema to return (fields such as `message`, `hint`, `next_action`, `next_action_params`, `alternative_actions`, `tell_user`).
