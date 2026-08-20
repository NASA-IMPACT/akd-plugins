# wildcard_search_tool (draft)

## Purpose
Once an investigation is selected, inspect files/folders broadly to identify useful data assets.

## Intended capabilities
- Walk investigation folders
- Detect file types (from filenames/extensions)
- Wildcard match files (e.g., `*.csv`, `*.xlsx`, `*.txt`, `*.json`)
- Optionally read supported structured files (e.g., CSV)
- Identify likely relevant files for the agent to inspect next

## Uses context
- `context/investigations/<investigation-id>/experimental_table.md`
- `context/investigations/<investigation-id>/data_layout_document.md`
- `context/investigations/<investigation-id>/file_types_available.md`

## Open questions
- What file types are allowed to be opened?
- Should it read file contents or only inspect filenames first?
- Should it recurse through all folders by default?
- Should large CSV reads be limited (headers/sample rows only)?
- Should it return recommended next files for the agent?
- Should it prioritize experimental tables before raw files when available?
