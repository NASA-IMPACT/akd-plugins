# cmr_search_tool — Endpoint

## MCP server

- Name: `CMR_MCP_Server`
- URL: `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp`
- Enabled: `true`
- Allowed tools: `null` (no restriction)
- Authorization: `null` (public; no auth headers)
- Transport: HTTP. `require_approval: "never"` (read-only search)

Illustrative plugin wiring (provided at packaging/deployment time; not stored in this
workspace):

```json
{
  "mcpServers": {
    "CMR_MCP_Server": {
      "type": "http",
      "url": "https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp"
    }
  }
}
```

## Underlying CMR endpoints

- Base URL: `https://cmr.uat.earthdata.nasa.gov/search/`
- **Collections** (primary): `GET /search/collections` — every search runs here.
- **Granules** (after collection selection only): `GET /search/granules`.
- Method: `GET`; results paged via `page_size` (default 10, max 2000) and `page_num`.

## Response formats

- **JSON** (default) and **UMM-JSON** (preferred for rich structured metadata). Also XML, ATOM,
  CSV, KML, STAC. Select via `Accept` header, a format extension, or `?format=`.

## Limits & performance

- URL length ~6,000 chars max — construct queries conservatively and page rather than combining
  many fields/values.
- Request timeout ~180s. Rate limiting returns **HTTP 429** with a `retry-after` header → back
  off (exponential) and retry.

See `../../contexts/cmr-metadata-model.md` for the full parameter catalog, response shape, error
codes, and query patterns.
