# sde_search_tool — Endpoint

## Implementation

Local script function: `scripts/sde_tools.py` (`sde_search_tool`).

## Underlying SDE endpoint

Single POST:

- URL: `https://dyejsbdumgpqz.cloudfront.net/api/search`
- Method: `POST`, headers `Content-Type: application/json`, `Accept: application/json`, timeout 30s.
- Payload:
  - `page: 1`
  - `pageSize: limit`
  - `search_term: <query>`
  - `search_type: "hybrid"`
  - **`min_score: 0.0`** — deliberate threshold-zero (else weak queries return zero results); preserve exactly.
  - `filters: {"document_type": [doc_type]}` — included only when `doc_type` is non-`None` (default `"Software and Tools"`).

## Notes

Same SDE backend as `repository_search_tool` (see `contexts/science-discovery-engine.md`), but without GitHub enrichment or reliability scoring. `content` snippets capped at 1500 characters.
