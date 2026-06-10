# IESO Worldview — Claude Code plugin

Explore **NASA Worldview** in natural language. The plugin bundles a
guided-discovery skill (find satellite layers, understand what a dataset
represents and its caveats, generate a reproducible Worldview permalink)
plus the MCP tools that back it — so you install once and start asking,
without wiring up any servers yourself.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

Inside Claude Code:

```
/plugin marketplace add sanzog03/claude-skills-and-plugins
/plugin install ieso-worldview@ieso-worldview-marketplace
```

On install, Claude Code prompts you for any required tokens (see
**Configuration**); they go into your OS keychain. Then just ask, e.g.:

> "Show me sea surface temperature anomalies for the Gulf of Mexico last week."

## Configuration

Tokens are requested interactively when you enable the plugin and stored
in your OS keychain — you never edit a config file. All are **optional**;
leave one blank if the corresponding MCP server is public.

| Prompt | Backs | Needed when |
|---|---|---|
| **IESO tools API token** | GeoUI render/get-state, `worldview_permalink_tool`, `umm_vis_lookup_tool`, `earthdata_search_landing_page_tool`, `pdf_parser_tool` (one shared server group) | those servers require auth |
| **IESO Validation API token** | `search_worldview_layers`, `validate_temporal_coverage` | the validation server requires auth |
| **Science Discovery Engine token** | `sde_search_tool` (fallback) | the SDE server requires auth |
| **EONET API token** | `eonet_search_tool` (natural-event context) | the EONET server requires auth |

These are FastMCP project tokens (`fmcp_…`). They are **not** stored in
the plugin files — Claude Code prompts for them at enable time and keeps
them in your OS keychain.

## Prerequisites

- **Claude Code** (this is a Claude Code plugin).
- **Node.js** (provides `npx`) — required for the Playwright browser MCP,
  which the assistant uses to open the map and read live state. On first
  use, `npx` fetches `@playwright/mcp` and Playwright downloads a Chromium
  build (~150 MB); this is automatic but can take a minute the first time.
  The browser window stays open for the session, so the map persists
  across turns.

## What's inside

```
.claude-plugin/plugin.json     manifest + userConfig prompts
.claude-plugin/marketplace.json distribution entry
.mcp.json                       MCP servers (URLs are deployment config)
skills/worldview-assistant/     the skill: SKILL.md + references/guardrails/contexts/assets
```

## For maintainers

- **MCP URLs live in `.mcp.json`, never in the skill markdown.** The
  server URLs are deployment config; auth is referenced as
  `${user_config.*}` so no token is committed.
- `skills/worldview-assistant/references/tools/mcp_config.json` documents
  the intended server/tool mapping (the source of truth for what `.mcp.json`
  should contain). It is documentation; `.mcp.json` is the live wiring.
- The skill drives the **GeoUI tools** (`geo_ui_render_intent_tool`,
  `geo_ui_get_state_tool`) for visualization, plus Playwright
  (`browser_navigate`, `browser_evaluate`) to open the map and read live
  state. `worldview_permalink_tool` remains wired but is superseded —
  kept for reference.
- The skill's tools are **MCP tools, called directly** — the
  `references/tools/<name>/index.md` files are tool documentation, not
  build-your-own-client instructions.
- **Browser lifecycle:** the Playwright MCP is a stdio server that runs
  once per Claude Code session, so its (headed) browser persists across
  turns — no CDP/`--remote-debugging-port` setup needed. The skill's
  loop-prevention guards (one `browser_evaluate` per turn; turn-completion
  gate after `browser_navigate`) live in `SKILL.md`'s PROCESS section.
