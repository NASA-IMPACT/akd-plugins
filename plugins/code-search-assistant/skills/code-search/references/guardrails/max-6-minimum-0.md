# Maximum 6 / Minimum 0, and Tool-Call Budgets

## Rule (verbatim)

> Maximum 6 repositories; minimum 0 allowed.

## Context budget (verbatim)

> Aim for no more than 10 total tool calls for non-Astrophysics queries; up to 16 for Astrophysics (where ASCL, ADS, and the resolver expand the discovery surface). The `ads_links_resolver_tool` may legitimately be called multiple times with different bibcodes; other tools should not be re-queried within the same step. Request the minimum `rows` needed.

## Per-channel query caps (verbatim, from the process)

- Step 2 `repository_search_tool`: run **at least 2 distinct queries** for any scientific domain query.
- Step 3 `sde_search_tool`: **one** SDE query.
- Step 5a ASCL: **Maximum 4 ASCL queries** (`rows=10` for task terms; `rows=5` for name lookups).
- Step 5b ADS: **Maximum 4 queries, `rows=5` each**.
- Step 5c `ads_links_resolver_tool`: **Maximum 4 uses across the pipeline** (one per ASCL record bibcode).
- Step 6 web search: **maximum 3** (aim to resolve all missing codes in 1–2 queries).

## Scope

Operational limits enforced across the whole pipeline. The final ranked list is narrowed to at most 6 in Step 7; the tool-call budget bounds the discovery effort by domain.

## Never Do

- Never emit more than 6 ranked repositories.
- Never exceed the tool-call budget for the query's domain (10 non-Astrophysics / 16 Astrophysics) without cause; re-query a tool within the same step only where explicitly permitted (`ads_links_resolver_tool`).
