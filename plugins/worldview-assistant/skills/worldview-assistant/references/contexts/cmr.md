# CMR (Common Metadata Repository)

## Name
CMR (Common Metadata Repository)

## Purpose
Authoritative metadata source using the UMM model; used to retrieve collection metadata for datasets.

## Access method
MCP endpoint (as provided):
- `https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp`

## Allowed tools (as provided)
- `search_collections`
- `get_collection_metadata`

## Permissions / auth model
Public-only datasets; authenticated workflows are out of scope.

## Limits / operational constraints (known)
- Rate limits exist (noted generally as ~1 query/second; confirm whether this applies to CMR MCP specifically)

## Known failure patterns / unknowns
- Monitor and handle 429 / 503 responses (noted generally)
- TBD: request/response schema for MCP calls (payload shape)
- TBD: which UMM fields are considered authoritative for user-facing explanations/caveats
