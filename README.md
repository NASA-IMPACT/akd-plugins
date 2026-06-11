# AKD Agents for Earth Science

A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
(`akd-agents`) hosting agents for exploring NASA Earth-observation data in
natural language. Each plugin bundles a skill plus the MCP servers that back
it, so you install once and start asking questions — no server wiring, and no
separate LLM API key (everything runs on your own Claude Code subscription).

## Add the marketplace

Inside Claude Code:

```
/plugin marketplace add sanzog03/claude-skills-and-plugins
```

## Available plugins

| Plugin | Description | Install |
|---|---|---|
| [worldview-assistant](plugins/worldview-assistant/README.md) | Explore NASA Worldview in natural language: discover satellite datasets, understand what they represent, and generate reproducible map visualizations. | `/plugin install worldview-assistant@akd-agents` |

After installing, invoke a plugin's skill directly (e.g.
`/worldview-assistant:worldview-assistant`) or just ask a matching question —
skills auto-trigger from context. See each plugin's README for prerequisites,
configuration tokens, and example prompts.

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

### Test locally

Add the marketplace from your working copy (point at the **repo root**, not
the plugin subdir) and install from it:

```
/plugin marketplace add /path/to/claude-skills-and-plugins
/plugin install <plugin-name>@akd-agents
```

While iterating, `/reload-plugins` picks up most file edits without a restart.
Exceptions: changes to `userConfig` in `plugin.json` need a
`/plugin uninstall` + `/plugin install` cycle to re-prompt for tokens.

To re-test against the GitHub-distributed version (recommended before
declaring a change shipped), do a clean cycle — Claude Code caches the
marketplace clone:

```
/plugin uninstall <plugin-name>
/plugin marketplace remove akd-agents
/plugin marketplace add sanzog03/claude-skills-and-plugins
/plugin install <plugin-name>@akd-agents
```

Diagnostics: `/plugin` → Errors tab (manifest issues), `/mcp` (per-server
connection state), `tail -f ~/.claude/logs/claude-code.log` (MCP subprocess
stderr).
