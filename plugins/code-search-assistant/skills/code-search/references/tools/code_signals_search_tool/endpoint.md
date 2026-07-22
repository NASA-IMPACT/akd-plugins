# code_signals_search_tool — Endpoint

## MCP server

- Name: `Code_Signal`
- URL: `https://developing-purple-wallaby.fastmcp.app/mcp`
- `require_approval: "never"`
- Enabled in the live runtime environment.

## Underlying endpoint

Backed by an SDE API endpoint:

- Path: `/api/code_signals/search`
- Method: `POST`
- Timeout: 30s
- Request body fields:
  - `search_term` (from `query`)
  - `search_type` (instance config; default `"hybrid"`, may also be `"vector"` or `"keyword"`)
  - `page_size` (from `limit`)
  - `page` (from `page`)
