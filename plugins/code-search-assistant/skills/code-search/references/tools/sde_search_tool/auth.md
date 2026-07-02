# sde_search_tool — Auth

## Authorization

`sde_search_tool` is implemented as a local script function and does not use an MCP bearer token.

## Underlying SDE endpoint

The SDE `/api/search` call sends no auth header (Content-Type/Accept only).
