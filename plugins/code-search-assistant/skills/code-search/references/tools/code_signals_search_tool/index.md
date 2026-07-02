# code_signals_search_tool

## What it does

Static code inspection used **only to resolve ambiguity about a repository's purpose** — when README and SDE context are insufficient to determine relevance. The agent references file paths or function names and must NOT include full code excerpts.

## Why / when to use

- **Step 4 (conditional):** invoked only when README + SDE context cannot determine relevance. Read-only inspection (see `guardrails/read-only-no-execution.md`).

## MCP server & enabled state

- Server: `Code_Signal` — `https://developing-purple-wallaby.fastmcp.app/mcp`.
- `allowed_tools`: `code_signals_search_tool`.
- Enabled in the live runtime environment (`require_approval: "never"`).

## Specification status

The tool's input/output schema is confirmed by the deployed tool interface (see `input-output.md`).

## Files

- `endpoint.md` — MCP server and underlying API note.
- `input-output.md` — params and returns.
- `auth.md` — bearer token (secret).
