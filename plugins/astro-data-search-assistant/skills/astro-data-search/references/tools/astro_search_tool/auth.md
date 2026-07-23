# astroquery-mcp — Auth

Two independent token layers. The agent never handles either as a literal.

## 1. Client → MCP server (Bearer token — required)

The `astroquery-mcp` server is **token-protected** (confirmed: a request without a token returns
`"Bearer token required"`). The MCP connection must send
`Authorization: Bearer TOKEN`, wired via the plugin's `.mcp.json`
(`headers.Authorization: Bearer ${user_config.astroquery_mcp_key}`) with the key declared in
`plugin.json` `userConfig`. This is the **packaged-plugin** `userConfig` field name; in Labs, the tool-config UI provisions the actual URL + token value.

## 2. Server → downstream services (server-side env vars)

Some astroquery services need their own credentials, configured as **environment variables on
the server deployment** (not client config):

- **ADS** — `API_DEV_KEY` (fallback `ADS_API_KEY`). Required for literature queries.
- **MAST** — `MAST_TOKEN` (needed only for proprietary/authenticated MAST access; public queries
  work without it).

`astroquery_check_auth()` reports which of these are configured. Most NASA public search works
without downstream tokens; ADS literature search requires the ADS key to be set server-side.

## Secret handling

**Treat all tokens as secrets** — literal values must never appear in this artifact. The agent
must never request, expose, or instruct extraction of credentials
(`../../guardrails/no-secrets-or-credentials.md`).

