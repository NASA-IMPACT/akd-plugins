# pdf_parser_tool

## Purpose
Parse a **digital-native** PDF (no OCR) into extracted text in a chosen format.

## When to use
Optional.

Use only when the agent already has a publicly accessible PDF URL (e.g., ATBD / user guide) that must be converted into text for summarization and citation.

Source note:
- ATBD/user-guide PDFs (when available) are accessible via the Earthdata Search landing page for **processed (non level-0) data**.

## Inputs (schema)
`additionalProperties: false`

- `url` (required, string): HTTP(S) PDF URL
- `return_format`: enum `markdown` (default) | `html` | `json`

## Outputs (schema)
- `content`: string
- `metadata`: object

## Validation & business rules
- `url` must be HTTP(S) and point to a PDF.
- PDF must be digital-native (no OCR support).

## Failure modes and recovery guidance
TBD (confirm): behavior for non-PDF URLs, inaccessible URLs, scanned PDFs, large PDFs.

## Security / permissions
Public-only.

## Notes
- MCP server label: `ieso-worldview-tool-pdf_parser_tool`
- See `tools/mcp_config.json`.
