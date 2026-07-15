# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

`akd-agents` — a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
hosting agents for exploring NASA science data in natural language. Each plugin
bundles a **skill** plus the **MCP servers** that back it, so a user installs
once and starts asking questions — no server wiring, no separate LLM API key
(everything runs on their own Claude Code subscription).

Users add the marketplace with `/plugin marketplace add NASA-IMPACT/akd-plugins`
and install plugins with `/plugin install <plugin-name>@akd-agents`.

## Repository layout

```
.
├── .claude-plugin/
│   └── marketplace.json      marketplace manifest — registers every plugin
├── plugins/
│   └── <plugin-name>/        one directory per plugin
│       ├── .claude-plugin/
│       │   └── plugin.json    plugin manifest (name, version, userConfig…)
│       ├── .mcp.json          MCP servers this plugin bundles
│       ├── README.md          user-facing install + usage docs
│       └── skills/
│           └── <skill-name>/
│               ├── SKILL.md    the skill definition (frontmatter + body)
│               └── references/ optional supporting docs the skill consults
├── docs/development.md       how to add a plugin + test locally (source of truth)
└── README.md                 marketplace overview + install table
```

## How a plugin is created

A plugin is a directory under `plugins/` with this anatomy. These are the full
instructions — everything needed to create a plugin from scratch. (The same
anatomy is mirrored for human contributors in
[`docs/development.md` → Plugin anatomy](docs/development.md#plugin-anatomy); keep
the two in sync when the anatomy changes.)

1. **`.claude-plugin/plugin.json`** — the manifest. Required: `name` (kebab-case,
   this is the identifier and it namespaces the skills as
   `/<plugin-name>:<skill-name>`), `description`, `version`. Optional:
   `displayName`, `author`, `license`, and **`userConfig`** — a map of
   user-supplied config values (e.g. API tokens). Each `userConfig` entry has
   `type`, `title`, `description`, `sensitive`, `required`; the values are
   prompted for at install time and referenced elsewhere as
   `${user_config.<key>}`.

2. **`.mcp.json`** — the MCP servers the plugin bundles (optional). Two transport
   shapes are used here:
   - **`http`** — remote FastMCP servers: `{ "type": "http", "url": "...",
     "headers": { "Authorization": "Bearer ${user_config.<key>}" } }`. The
     bearer token is pulled from `userConfig`; servers that are public omit the
     `headers` block.
   - **`stdio`** — local subprocess servers, e.g. Playwright:
     `{ "type": "stdio", "command": "npx", "args": ["@playwright/mcp@latest"] }`.

3. **`skills/<skill-name>/SKILL.md`** — the skill. YAML frontmatter with `name`
   and a `description` (the description is what triggers auto-invocation from
   user context — write it as "Use when …"). The markdown body is the agent's
   instructions (role, objective, reasoning, guardrails). Larger skills split
   supporting material into a `references/` subtree (`contexts/`, `tools/`,
   `guardrails/`) that the body points to; a minimal skill is a single SKILL.md.

4. **`README.md`** — user-facing install command, prerequisites, config tokens,
   and example prompts.

5. **Register in `.claude-plugin/marketplace.json`** — add an entry to the
   `plugins` array:
   ```json
   {
     "name": "<plugin-name>",
     "source": "./plugins/<plugin-name>",
     "description": "One-line description shown in the /plugin browser.",
     "version": "0.1.0"
   }
   ```
   Use the explicit `./plugins/<name>` relative source (resolves for both local
   and GitHub installs). Bump `version` on every release — users only receive
   updates when it changes. **A plugin on disk is not installable until it is
   listed here.**

## Existing plugins (examples to model)

- **`plugins/worldview-assistant`** — the full-featured reference plugin: one
  rich skill with a large `references/` tree (contexts, per-tool docs,
  guardrails), 9 MCP servers (CMR, GeoUI, permalink, UMM-Vis, Earthdata-search,
  PDF parser, SDE, EONET, Playwright), 4 `userConfig` tokens.

## Validating and testing

```bash
claude plugin validate .                      # marketplace manifest
claude plugin validate plugins/<plugin-name>  # plugin manifest
```

Local test loop (point the marketplace at the **repo root**, not the plugin
subdir):
```
/plugin marketplace add /path/to/akd-plugins
/plugin install <plugin-name>@akd-agents
```
`/reload-plugins` picks up most edits. Exceptions:
- `userConfig` changes need `/plugin uninstall` + `/plugin install` to re-prompt.
- `marketplace.json` changes (new plugin) need `/plugin marketplace update akd-agents`.

Full details, including the clean GitHub-distributed re-test cycle and
diagnostics, live in **`docs/development.md`** — treat it as the source of truth.
