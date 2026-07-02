# sde_search_tool — Input / Output

Implemented by local script `scripts/sde_tools.py` (`sde_search_tool`).

## Inputs

| Param | Type | Required | Default | Meaning |
|---|---|---|---|---|
| `query` | str | yes | — | Natural-language search query (e.g., "Mars rover spectroscopy data"). |
| `limit` | int | no | `10` | Max results to return (1–100). |
| `doc_type` | str \| None | no | `"Software and Tools"` | Filter by document type — `Data`, `Documentation`, `Software and Tools`, `Images`, `Missions and Instruments`. Pass `None` for no filter. |

Fixed internally: `search_type="hybrid"`, `min_score=0.0`.

## Outputs

Returns `{ "total_count": <int>, "results": [ … ] }`. Each result:

| Field | Source | Notes |
|---|---|---|
| `title` | SDE `title` | Document title. |
| `url` | SDE `url` | Document URL. |
| `content` | SDE `full_text`/`data_product_desc`/`description` | Truncated to 1500 chars. |
| `score` | SDE `_score` | Relevance (with `min_score=0.0`, may be low). |
| `division` | SDE `division` | NASA SMD division. |
| `doc_type` | SDE `document_type` | Document type. |
| `source` | SDE `api_source` | e.g., `sde-cmr`, `sde-pds4`, `sde-web`, `sde-code`. |

## Usage note

The process uses **one** SDE query in Step 3. Request the minimum `limit` needed (context budget). Results feed the running list and domain-alignment validation, not final ranking on their own.
