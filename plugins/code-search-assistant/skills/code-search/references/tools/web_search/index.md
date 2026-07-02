# web_search

## What it does

Builtin external web search. Supplementary discovery only; results must be flagged as externally sourced. See `contexts/external-web-search.md`.

## Why / when to use

- **Step 6 (Completeness Check) only** — the sole tool used in that step. Locate a public repository or project website for each Expected-Codes checklist item still missing from the running list.
- Combine ALL missing code names into a single query (e.g., `"FLASH GitHub" "PLUTO GitHub" "Enzo GitHub"`). Aim to resolve all missing codes in 1–2 queries; **maximum 3**.
- Prioritize `.gov`, `.edu`, `nasa.gov`, `esa.int`, and similar trusted domains. Flag externally sourced repositories in the **Provenance** bullet.

## Builtin configuration & enabled state

- Builtin `web_search`, **enabled**, with `search_context_size: "medium"`.
- The companion builtin `web_fetch` is **disabled**.
- Not an MCP tool — no MCP server, no `allowed_tools` entry.

## Files

- `endpoint.md` — builtin (no MCP endpoint).
- `input-output.md` — usage and returns.
- `auth.md` — builtin (no token).
