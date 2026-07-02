# Context: Code Signals (Static Code Inspection)

## What it is

A static code inspection capability (`code_signals_search_tool`) used **only to resolve ambiguity about a repository's purpose** — i.e., when README and SDE context are insufficient to determine relevance. Hosted on the `Code_Signal` MCP server (`developing-purple-wallaby.fastmcp.app/mcp`).

## Role in the pipeline

- **Step 4 (conditional):** invoked only when README and SDE context cannot determine relevance. The agent references file paths or function names and must NOT include full code excerpts (read-only inspection; see `guardrails/read-only-no-execution.md`).

## Specification status

The tool's input/output schema is confirmed by the deployed tool interface; see `tools/code_signals_search_tool/input-output.md`.

## Related tool

`tools/code_signals_search_tool/`.
