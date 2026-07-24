# Development guide

How to add a plugin to the `akd-agents` marketplace and test it locally.

> **If you have an agent built outside AKD Labs**, start with the
> [Converting AKD Agents into Plugins](https://github.com/NASA-IMPACT/akd-plugins/wiki/Converting-AKD-Agents-into-Plugins)
> wiki guide — it walks the full path from your existing prompts/artifacts, through
> AKD Labs, to a finished skill. This page picks up once you have that skill in hand.

## Plugin anatomy

A plugin is a directory under `plugins/<plugin-name>/`. This section is the
canonical field reference — other docs link here rather than restating it.

- **`.claude-plugin/plugin.json`** — the manifest. Required: `name` (kebab-case;
  this is the identifier and it namespaces the skills as
  `/<plugin-name>:<skill-name>`), `description`, `version`. Optional:
  `displayName`, `author`, `license`, and **`userConfig`** — a map of
  user-supplied config values (e.g. API tokens). Each `userConfig` entry has
  `type`, `title`, `description`, `sensitive`, `required`; the values are
  prompted for at install time and referenced elsewhere as `${user_config.<key>}`.

- **`.mcp.json`** — the MCP servers the plugin bundles (optional). Two transport
  shapes are used here:
  - **`http`** — remote FastMCP servers:
    `{ "type": "http", "url": "...", "headers": { "Authorization": "Bearer ${user_config.<key>}" } }`.
    The bearer token is pulled from `userConfig`; public servers omit the
    `headers` block.
  - **`stdio`** — local subprocess servers, e.g. Playwright:
    `{ "type": "stdio", "command": "npx", "args": ["@playwright/mcp@latest"] }`.

- **`skills/<skill-name>/SKILL.md`** — the skill. YAML frontmatter with `name`
  and a `description` (the description triggers auto-invocation from user
  context — write it as "Use when …"). The markdown body is the agent's
  instructions (role, objective, reasoning, guardrails). Larger skills split
  supporting material into a `references/` subtree (`contexts/`, `tools/`,
  `guardrails/`) that the body points to; a minimal skill is a single SKILL.md.

- **`README.md`** — user-facing install command, prerequisites, config tokens,
  and example prompts.

Every plugin must also be registered in `.claude-plugin/marketplace.json` (see
[step 2 below](#adding-a-plugin-to-the-marketplace)).

### Examples to model

- **`plugins/worldview-assistant`** — the full-featured reference plugin: one
  rich skill with a large `references/` tree (contexts, per-tool docs,
  guardrails), 9 MCP servers (CMR, GeoUI, permalink, UMM-Vis, Earthdata-search,
  PDF parser, SDE, EONET, Playwright), 4 `userConfig` tokens.

## Adding a plugin to the marketplace

1. Create a directory under `plugins/` with the standard plugin layout:

   ```
   plugins/<plugin-name>/
   ├── .claude-plugin/
   │   └── plugin.json        manifest: name, description, version, userConfig…
   ├── .mcp.json              MCP servers the plugin bundles (optional)
   ├── README.md              user-facing install + usage docs
   └── skills/
       └── <skill-name>/
           └── SKILL.md       the skill definition
   ```

   See [Plugin anatomy](#plugin-anatomy) for the full field reference (manifest,
   `.mcp.json` transports, SKILL.md frontmatter). The `name` in `plugin.json` is
   the plugin's identifier — kebab-case, and it namespaces the skills
   (`/<plugin-name>:<skill-name>`).

2. Register it in `.claude-plugin/marketplace.json` by adding an entry to the
   `plugins` array:

   ```json
   {
     "name": "<plugin-name>",
     "source": "./plugins/<plugin-name>",
     "description": "One-line description shown in the /plugin browser.",
     "version": "0.1.0"
   }
   ```

   Use the explicit `./plugins/<name>` relative source — it resolves correctly
   for both local and GitHub installs. Bump `version` on every release; users
   only receive updates when it changes.

3. Validate both manifests:

   ```bash
   claude plugin validate .
   claude plugin validate plugins/<plugin-name>
   ```

## Test locally

Add the marketplace from your working copy (point at the **repo root**, not
the plugin subdir) and install from it:

```
/plugin marketplace add /path/to/akd-plugins
/plugin install <plugin-name>@akd-agents
```

While iterating, `/reload-plugins` picks up most file edits without a restart.
Exceptions:

- Changes to `userConfig` in `plugin.json` need a
  `/plugin uninstall` + `/plugin install` cycle to re-prompt for tokens.
- Changes to `marketplace.json` (e.g. registering a new plugin) need
  `/plugin marketplace update akd-agents` before the new entry is
  installable — re-running `/plugin marketplace add` with the same path
  reports success but serves the stale catalog.

To re-test against the GitHub-distributed version (recommended before
declaring a change shipped), do a clean cycle — Claude Code caches the
marketplace clone:

```
/plugin uninstall <plugin-name>
/plugin marketplace remove akd-agents
/plugin marketplace add NASA-IMPACT/akd-plugins
/plugin install <plugin-name>@akd-agents
```

Diagnostics: `/plugin` → Errors tab (manifest issues), `/mcp` (per-server
connection state), `tail -f ~/.claude/logs/claude-code.log` (MCP subprocess
stderr).
