# PSI Assistant — Claude Code plugin

Explore **NASA's Physical Sciences Informatics (PSI)** repository in natural language. PSI
provides open access to data from microgravity and ground-based physical sciences
investigations — fluid physics, combustion, materials science, soft matter, fundamental
physics. The plugin bundles a guided discovery-and-synthesis skill (find investigations,
navigate their file corpora, look up publications via DataCite, and get evidence-backed
summaries and comparisons with traceable citations) plus the MCP server that backs it — so you
install once and start asking, without wiring up any servers yourself.

It is assistive and human-in-the-loop, **not** authoritative: every interpretive statement is
cited to PSI sources and caveated for your verification, PSI IDs/DOIs/values are never
fabricated, and downloads stay user-driven (the agent returns URLs by default and never
triggers downloads itself). Packaged from the **PSI Scientific Discovery Agent** CARE
artifact, mirrored under `skills/psi-discovery/references/`.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install psi-assistant@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing at the repo root,
not the plugin subdir — then the same install command.)

On enable, Claude Code prompts you for the server URL and token (see **Configuration**). Then
just ask, e.g.:

> "Identify a PSI investigation dealing with cold flame extinction."

> "What data files does the SUBSA-CETSOL investigation contain, and where is the analyzed data?"

> "Compare the alloys tested across the SUBSA solidification investigations."

## Configuration

Both values are prompted at enable time and stored in your OS keychain — **neither is
hard-coded in the plugin**, so you can point it at your own deployment:

| Prompt | Backs | Required |
|---|---|---|
| **PSI MCP server URL** (`psi_mcp_url`) | the PSI MCP HTTP endpoint | **Yes** |
| **PSI MCP token** (`psi_mcp_key`) | bearer auth for that server — both tools | **Yes** |

- **URL** — the PSI MCP HTTP endpoint, e.g. `https://akd-psi-agent-v1.fastmcp.app/mcp`. It's a
  plain URL (not a secret); supply the endpoint of the deployment you want to use.
- **Token** — the PSI MCP server is **token-protected**, so this token is **required** —
  without it no PSI search works. It's a FastMCP token (`fmcp_…`), stored in your OS keychain;
  it is **not** committed to the plugin files.

(The PSI Public Investigations API and the DataCite API that the server calls downstream are
public and unauthenticated — the token only gates the MCP server itself.)

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).
- The **PSI MCP server URL** and a **FastMCP token** for it (both entered at enable time — see
  Configuration).

## Troubleshooting

- **First connection can be slow (cold start).** FastMCP deployments can exceed Claude Code's
  default ~30 s handshake timeout after idling — `/mcp` then shows `psi-mcp` as `failed` with
  `MCP error -32001: Request timed out`. Raise the timeout: add
  `"env": { "MCP_TIMEOUT": "120000" }` to `~/.claude/settings.json` (or launch
  `MCP_TIMEOUT=120000 claude`), then relaunch and **reconnect** from `/mcp`. This is a
  client-side timeout, not an auth failure — your token is fine if a direct `curl … /mcp`
  returns `HTTP 200`.
- **Expired download links.** PSI's signed file URLs expire after ~7 days; the agent re-queries
  for fresh URLs rather than presenting stale ones. If you saved a link that no longer works,
  just ask again.
- **404s on `/legacy/` files.** Roughly 60% of the PSI corpus is legacy data with a known
  elevated missing-file rate; the agent warns when results fall in `/legacy/` paths. A 404
  there is a known data quirk, not a plugin failure.
- **Timeouts on very large investigations.** A couple of investigations (>10k files) can time
  out server-side; the agent reports the timeout instead of returning partial results — narrow
  the request (file type, subdirectory) and retry.

## What's inside

```
.claude-plugin/plugin.json     manifest + userConfig (psi_mcp_url, psi_mcp_key — both required)
.mcp.json                       the psi-mcp HTTP server (Bearer ${user_config.psi_mcp_key})
skills/psi-discovery/           the skill: SKILL.md + references/ (contexts, guardrails,
                                tools, output.md, reasoning.md, scope.md)
```

## For maintainers

- **One MCP server, token-gated:** `psi-mcp`. Both the **URL and the token come from
  `userConfig`** (`psi_mcp_url`, `psi_mcp_key`), so `.mcp.json` hard-codes neither — `url` is
  `${user_config.psi_mcp_url}` and auth is `headers.Authorization: Bearer
  ${user_config.psi_mcp_key}`. Both are `required: true`; the token is `sensitive: true`, the
  URL is not.
- **Two tools used, operation-based:** `psi_api_tool` (one tool, `operation` ∈
  `discover_investigations` / `get_investigation` / `search_files` / `navigate_dataset` /
  `retrieve_file` / `lookup_publication`) and `metadata_expansion_tool` (discovery-result
  enrichment + relevance ranking with a suggested next call). `SKILL.md` → **Tools (MCP
  runtime)** carries the verified live signatures and is the authoritative mapping; the
  `references/tools/` files are the design record. The artifact's `wildcard_search_tool` is
  design-only — not on the v1 server — and the deployment also hosts tools from other AKD
  agents (`geocode`, `sde_search_tool`, …) that the skill explicitly declines to use.
- **Contexts are text-only:** the design-time corpus's PSI-hosted PDFs (investigation
  overviews, SRDs, ReadMes, publications, a dissertation — ~34 MB, some copyrighted journal
  papers) are deliberately **not** bundled. `references/contexts/index.md` keeps their routing
  knowledge and tells the agent to fetch them live from PSI via `psi_api_tool`.
- **Read-only toward PSI:** the skill's guardrails forbid triggering downloads, altering PSI
  content, and surfacing `restricted`/non-`visible` files; both tools are read-only
  search/enrichment operations.

## License

Apache-2.0
