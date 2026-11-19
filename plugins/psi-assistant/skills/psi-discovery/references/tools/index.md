# Tools

## MCP deployment (authoritative for runtime)

At runtime the tools are served by the **`psi-mcp`** MCP server bundled by this plugin
(FastMCP, HTTP, bearer-token auth from install-time config). Two tools are deployed in v1:

- `psi_api_tool` — PSI investigations discovery/search/retrieval + dataset navigation +
  DataCite lookup.
- `metadata_expansion_tool` — enrich/normalize investigation discovery results using
  Investigation Metadata Files.

`wildcard_search_tool` is part of the design record below but is **not deployed** on the v1
server — do not call it; cover its role (broad file-corpus inspection) with `psi_api_tool`
file search.

Several contract details in the per-tool documents are still marked TBD; the **live MCP tool
schema is authoritative** — introspect it before the first call, and treat the documents under
`psi/` as design intent, error-recovery guidance, and backing-system reference.

## Design record — canonical tool workspace organization

```text
/tools
  /psi
    /psi_api_tool/
      contract.md
      errors_and_recovery.md
      index.md
    /metadata_expansion_tool/
      contract.md
      errors_and_recovery.md
      index.md
    /wildcard_search_tool/        (design only — not deployed in v1)
      contract.md
      errors_and_recovery.md
      index.md
```

## Confirmed tool principles

- Start investigation discovery from the Investigation Metadata Files context.
- Use the PSI Public Investigations API endpoints for investigation discovery, file search, and download.
- Dataset navigation should reconstruct hierarchy from `category + subcategory + subdirectory`.
- Investigation discovery should support ID ranges like `PSI-100,PSI-105-PSI-110`.
- DataCite lookup should support both DOI lookup and title/publication search.
- File retrieval should support returning download URLs and/or downloading into a user-selected destination.
- Error responses should include guidance such as retry guidance, re-query on expired URLs, legacy-file missing-risk warnings, and narrowing large result sets.
- Extraction, summarization, and comparison remain LLM responsibilities (not tools).
- Out of scope for v1: research gap / related-work discovery.

## Confirmed v1 tool inventory

- `psi_api_tool` — PSI investigations discovery/search/download + dataset navigation + DataCite lookup. **Deployed.**
- `metadata_expansion_tool` — enrich/normalize investigation discovery results using Investigation Metadata Files. **Deployed.**
- `wildcard_search_tool` — broad inspection of an investigation's file corpus (types, patterns) to identify useful assets to open next. **Design only; not deployed in v1.**
