# astroquery-mcp — Endpoint

## MCP server

- Name: `astroquery-mcp` (FastMCP; repo: `igaurab/astroquery-mcp`).
- URL: `https://coming-gray-slug.fastmcp.app/mcp`
- Transport: HTTP. **Bearer token required** (a GET returns `HTTP 401`; `tools/list` without a
  token returns `"Bearer token required"`).
- `require_approval`: `"never"` (read-only search).

Plugin wiring — the server is token-protected, so include a `headers.Authorization` entry (the
live `.mcp.json` is created at packaging, not committed here; the token comes from
`plugin.json` `userConfig`, never a literal):

```json
{
  "mcpServers": {
    "astroquery-mcp": {
      "type": "http",
      "url": "https://coming-gray-slug.fastmcp.app/mcp",
      "headers": { "Authorization": "Bearer ${user_config.astroquery_mcp_key}" }
    }
  }
}
```

## Underlying service endpoints (used by `astroquery_execute`)

The server routes to astroquery's services; TAP endpoints configured include:

- Gaia — `https://gea.esac.esa.int/tap-server/tap` (ESA)
- VizieR — `http://tapvizier.u-strasbg.fr/TAPVizieR/tap` (CDS)
- HEASARC — `https://heasarc.gsfc.nasa.gov/xamin/vo/tap` (NASA)
- IRSA — `https://irsa.ipac.caltech.edu/TAP` (NASA/IPAC)
- MAST — `https://mast.stsci.edu/vo-tap/api/v0.1` (NASA/STScI)

SIA endpoints exist for HEASARC / IRSA / MAST. All of these services are **in scope** (NASA +
ESA + CDS); see `../../guardrails/supported-archives-only.md`.

## Limits (server defaults)

Timeout 60s; max_retries 3 (backoff factor 2.0); ADS 100 rows/page; max_rows 10000; SIMBAD rate
limit ~5 requests/second. Modules are imported lazily on first use.

