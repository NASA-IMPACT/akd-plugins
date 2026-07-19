# sde_search_tool — Input / Output

Searches NASA's Science Discovery Engine (SDE) via the unified `/api/search` endpoint to provide contextual enrichment.

## Inputs

| Param | Type | Required | Default | Meaning |
|---|---|---|---|---|
| `query` | str | yes | — | Natural-language search query. |
| `limit` | int | no | 10 | Maximum number of results to return (1–100). |
| `doc_type` | str \| None | no | None | Optional filter by document type (e.g., `Software and Tools`). |

Notes:
- The tool sends **`min_score=0.0` on every request** to avoid server-side default filtering.
- Search mode (`hybrid`/`vector`/`keyword`) and optional division scoping are instance configuration (not caller-controlled).

## Outputs

Returns an object with:
- `results`: list of documents, each including `query` (echo), `title`, `url`, `content`, `score`, and optionally `division`, `doc_type`, `source`.
- `extra`: tool-provided metadata (e.g., `total_count`, `requested_limit`).

## Usage note

The process uses **one** SDE query in Step 3. Request the minimum `limit` needed (context budget). Results feed the running list and domain-alignment validation, not final ranking on their own.
