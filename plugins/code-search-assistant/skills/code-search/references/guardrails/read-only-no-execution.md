# Read-Only — No Execution

## Rule (verbatim)

> Read-only: no execution, cloning, downloading, testing, or code generation.

## Scope

Applies to every step of the pipeline. The agent is a read-only, decision-support system; all channels (repository search, SDE, code signals, ASCL, ADS, web search) are used for discovery and description only.

## Never Do

- Never execute, clone, download, or test any repository or code.
- Never generate code.
- Static code inspection via `code_signals_search_tool` is limited to referencing file paths or function names; never include full code excerpts (see `tools/code_signals_search_tool/`).
