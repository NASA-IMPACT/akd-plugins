# ads_links_resolver_tool

## What it does

Given a bibcode, returns `associated_bibcodes` — ADS-curated canonical description papers. Used to recover canonical "Described in" papers that ASCL itself often under-reports. See `contexts/nasa-ads.md`.

## Why / when to use

- **Astrophysics only, Step 5c.** Pass the **ASCL record's bibcode** (e.g., `2010ascl.soft10082F` for FLASH); merge the returned `associated_bibcodes` into the candidate's **Describing bibcodes** (deduplicate against ASCL's `described_in`).
- Use whenever a candidate has fewer than 2 describing bibcodes from ASCL or its `described_in` paper has obviously low citations relative to the code's stature.
- **Maximum 4 uses across the pipeline** (one per ASCL record bibcode). This is the one tool that may legitimately be called multiple times within Step 5 (with different bibcodes).

## MCP server & enabled state

- Server: `ads-ascl` — `https://ads-ascl.fastmcp.app/mcp`.
- Enabled in the live runtime environment; `allowed_tools` include `ads_links_resolver_tool`.

## Files

- `endpoint.md` — MCP server.
- `input-output.md` — params and returns.
- `auth.md` — bearer token (secret).
