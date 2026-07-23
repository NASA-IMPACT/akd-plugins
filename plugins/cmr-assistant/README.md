# CMR Data Search — Claude Code plugin

Discover and relevance-rank **NASA Earthdata (CMR)** collections for an Earth science question,
in natural language. The plugin bundles a guided-discovery skill (interpret the question,
normalize terms to canonical **GCMD Science Keywords**, search CMR collections, verify granule
availability, return **Concept IDs** with a reproducible search log) plus the MCP server that
backs it — so you install once and start asking, without wiring up any servers yourself.

It is read-only and human-in-the-loop: it **never** recommends, endorses, ranks by "best", or
downloads data. Packaged from the finalized **CMR Data Search — CARE v2** artifact, mirrored
under `skills/cmr-data-search/references/`.

The assistant runs on **your own Claude** (no separate LLM API key).

## Install

```
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install cmr-assistant@akd-agents
```

(For local development: `/plugin marketplace add <path-to-repo>` — pointing at the repo root,
not the plugin subdir — then the same install command.)

Then just ask, e.g.:

> "I'm looking for sea surface temperature data near Hawaii for January 2024."

The assistant confirms your variables, spatial/temporal bounds, and expertise level before
searching, then returns a relevance-ordered list of CMR collections with Concept IDs and a
reproducibility log.

## Configuration

**None.** The `cmr` MCP server is **public** — no token, no `userConfig`, no login. CMR
collection search and metadata are open; Earthdata Login is only needed to *download* data,
which is out of scope for this agent.

## Prerequisites

- **Claude Code** (this is a Claude Code plugin). Nothing else — no API keys, no local runtime.

## What's inside

```
.claude-plugin/plugin.json     manifest (no userConfig — public server)
.mcp.json                       the `cmr` MCP server (public HTTP, no auth header)
skills/cmr-data-search/         the skill: SKILL.md + references/ (contexts, guardrails,
                                tools, output.md, reasoning.md, scope.md, resources/)
```

## For maintainers

- **The `cmr` MCP server** (key `cmr` in `.mcp.json`; the server reports itself as
  "CMR Data Server") is public NASA CMR — no `Authorization` header, no `userConfig`.
  `.mcp.json` is the **live wiring**; the reference docs also record the server URL as
  documentation (`references/tools/index.md`, `references/tools/cmr_search_tool/{index,endpoint}.md`),
  so a server migration must update `.mcp.json` **plus** those three files.
- **Three tools, called directly:** `search_collections` (collection discovery),
  `get_granules` (granule verification after a collection is selected — never for download),
  and `get_collection_metadata` (verbatim documentation). The CARE artifact refers to these
  collectively as the abstract `cmr_search_tool`; `SKILL.md` → **Tools (MCP runtime)** is the
  authoritative mapping. The `references/tools/<name>/` files are the design record, not
  build-your-own-client instructions.
- **GCMD normalization is offline:** the bundled snapshot
  `skills/cmr-data-search/references/resources/gcmd-science-keywords.json` (v22.6, ~2.6 MB) is
  the only vocabulary source — the server has no live keyword tool. The skill points the agent
  at it via `${CLAUDE_SKILL_DIR}` and tells it to *search* the file, not load it wholesale.
- **No server-side sort:** `search_collections` has no `sort_key` and no `science_keywords`
  field — normalized keywords go into `keyword`, and relevance ordering is done by the agent.

## License

Apache-2.0
