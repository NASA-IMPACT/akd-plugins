# AKD Agents for Science

A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
(`akd-agents`) hosting agents for exploring NASA science data — from Earth
observation to planetary archives — in natural language. Each plugin bundles a skill plus the MCP servers that back
it, so you install once and start asking questions — no server wiring, and no
separate LLM API key (everything runs on your own Claude Code subscription).

## Prerequisites

- **[Claude Code](https://code.claude.com/docs/en/overview)** — plugins are a
  Claude Code feature. This marketplace does **not** work on Claude Desktop
  (or claude.ai) as of now.

Individual plugins may have additional requirements (e.g. Node.js) — see
each plugin's README.

## Add the marketplace

Inside Claude Code:

```
/plugin marketplace add NASA-IMPACT/akd-plugins
```

## Available plugins

| Plugin | Description | Install (use this command) | How to use |
|---|---|---|---|
| [worldview-assistant](plugins/worldview-assistant/README.md) | Explore NASA Worldview in natural language: discover satellite datasets, understand what they represent, and generate reproducible map visualizations. | `/plugin install worldview-assistant@akd-agents` | Invoke the skill directly (`/worldview-assistant:worldview-assistant`) or just ask a matching question — skills auto-trigger from context. See the [plugin README](plugins/worldview-assistant/README.md) for prerequisites, configuration tokens, and example prompts. |
| [pds-assistant](plugins/pds-assistant/README.md) | Find the right NASA Planetary Data System (PDS) datasets for a planetary-science question: route to the correct PDS node, walk the live archives, and return grounded dataset identifiers and paths. | `/plugin install pds-assistant@akd-agents` | Invoke the skill directly (`/pds-assistant:pds_live_dataset_finder`) or just ask a matching planetary-science question. See the [plugin README](plugins/pds-assistant/README.md) for configuration tokens and example prompts. |

(More coming soon..)

Note: After installing/updating a plugin, you may need to `/reload-plugins` for the changes to take effect.

## Development

Want to add a plugin to the marketplace or test changes locally? See the
[development guide](docs/development.md).

## License

[Apache 2.0](LICENSE)
