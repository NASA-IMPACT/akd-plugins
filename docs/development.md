# Development guide

How to add a plugin to the `akd-agents` marketplace and test it locally.

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

   The `name` in `plugin.json` is the plugin's identifier — kebab-case, and it
   namespaces the skills (`/<plugin-name>:<skill-name>`).

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
/plugin marketplace add /path/to/akd-plugins-claude
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
/plugin marketplace add NASA-IMPACT/akd-plugins-claude
/plugin install <plugin-name>@akd-agents
```

Diagnostics: `/plugin` → Errors tab (manifest issues), `/mcp` (per-server
connection state), `tail -f ~/.claude/logs/claude-code.log` (MCP subprocess
stderr).
