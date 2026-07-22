# sde_search_tool — Auth

## MCP authorization (secret — reference only)

- The MCP connection may use a bearer `authorization` token supplied in the runtime client config.
- **Treat this token as a secret.** The literal value must not be stored in this workspace.

## Underlying SDE endpoint

The SDE `/api/search` call sends no auth header (Content-Type/Accept only).
