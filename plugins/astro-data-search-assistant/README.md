# Astro Data Search — Claude Code plugin

Discover **public astrophysics datasets** for an astronomy data‑discovery question, in natural
language. The plugin bundles a guided‑discovery skill (classify the query into an archetype,
normalize the target/region/time/band, plan a deterministic search, run it read‑only, and return
a ranked list of **candidate datasets** with provenance and caveats) plus the MCP server that
backs it — so you install once and start asking, without wiring up any servers yourself.

It is read‑only and human‑in‑the‑loop: it **never** downloads data, writes download scripts, or
endorses a "best" dataset — ordering is an explicit metadata proxy, and you make the final call.
Packaged from the finalized **Astro Data Search — CARE v2** artifact, mirrored under
`skills/astro-data-search/references/`.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install astro-data-search-assistant@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing at the repo root,
not the plugin subdir — then the same install command.)

On enable, Claude Code prompts you for the token (see **Configuration**). Then just ask, e.g.:

> "Find Chandra X‑ray imaging of the Bullet Cluster."

## Configuration

| Prompt | Backs | Required |
|---|---|---|
| **Astroquery MCP token** (`astroquery_mcp_key`) | the `astroquery-mcp` server — every search tool | **Yes** |

The `astroquery-mcp` server is **token‑protected** (an unauthenticated request returns HTTP 401),
so this token is **required** — without it no search works. It's a FastMCP project token
(`fmcp_…`), requested interactively when you enable the plugin and stored in your OS keychain;
it is **not** committed to the plugin files.

(Downstream service credentials — e.g. the ADS `API_DEV_KEY`, MAST `MAST_TOKEN` — are
**server‑side** environment variables on the astroquery‑mcp deployment, not client config. Most
public NASA search works without them; ADS literature search needs the ADS key set server‑side.)

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).
- A **FastMCP token** for the `astroquery-mcp` server (entered at enable time).

## Troubleshooting

- **First connection can be slow (cold start).** The server imports the astroquery stack lazily,
  so the initial MCP handshake can exceed Claude Code's default ~30 s timeout — `/mcp` then shows
  `astroquery-mcp` as `failed` with `MCP error -32001: Request timed out`. Raise the timeout: add
  `"env": { "MCP_TIMEOUT": "120000" }` to `~/.claude/settings.json` (or launch
  `MCP_TIMEOUT=120000 claude`), optionally pre-warm the server with one `initialize` request, then
  relaunch and **reconnect** from `/mcp`. This is a client-side timeout, not an auth failure —
  your token is fine if a direct `curl … /mcp` returns `HTTP 200`.
- **Literature (ADS) needs a server-side key.** `ads_query_compact` / `ads_get_paper` and the
  `LITERATURE_DRIVEN` archetype's ADS confirmation only work if the **deployment** has `API_DEV_KEY`
  set (see Configuration). When it isn't, `astroquery_check_auth` reports ADS unconfigured and the
  agent **degrades gracefully** — it pivots to other supported archives (e.g. NED reference tables)
  and flags the gap rather than fabricating a paper or citation.

## What's inside

```
.claude-plugin/plugin.json     manifest + userConfig (astroquery_mcp_key, required)
.mcp.json                       the astroquery-mcp HTTP server (Bearer ${user_config.astroquery_mcp_key})
skills/astro-data-search/       the skill: SKILL.md + references/ (contexts, guardrails,
                                tools, output.md, reasoning.md, scope.md)
```

## For maintainers

- **One MCP server, token‑gated:** `astroquery-mcp`
  (`https://coming-gray-slug.fastmcp.app/mcp`, repo `igaurab/astroquery-mcp`). Auth is wired as
  `headers.Authorization: Bearer ${user_config.astroquery_mcp_key}`; the token is `userConfig`,
  never committed. Because it's the single essential token, it is `required: true`.
- **Seven tools, introspection‑based** (not one per archive): `astroquery_list_modules`,
  `astroquery_list_functions`, `astroquery_get_function_info`, `astroquery_execute` (the
  workhorse, over 14 astroquery modules), `astroquery_check_auth`, `ads_query_compact`,
  `ads_get_paper`. The CARE artifact refers to these collectively as the abstract
  `astro_search_tool`; `SKILL.md` → **Tools (MCP runtime)** is the authoritative mapping, with the
  exact signatures (`astroquery_execute(module_name, function_name, params, max_rows)`). The
  `references/tools/` files are the design record, not build‑your‑own‑client instructions.
- **Read‑only:** the skill's guardrails forbid downloads, download scripts, and "best dataset"
  language; `require_approval` is `"never"` because every tool is a read‑only search.

## License

Apache-2.0
