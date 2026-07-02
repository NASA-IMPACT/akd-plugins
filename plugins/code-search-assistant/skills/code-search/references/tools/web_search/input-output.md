# web_search — Input / Output

## Inputs

| Param | Type | Meaning |
|---|---|---|
| `query` | str | Web search query. Process pattern: combine all still-missing checklist code names into one query (e.g., `"FLASH GitHub" "PLUTO GitHub" "Enzo GitHub"`). |

Budget: **maximum 3 web queries** in Step 6; aim to resolve all missing codes in 1–2.

## Outputs

Standard web search results (titles, URLs, snippets), scoped by `search_context_size: "medium"`. No page-body fetch (`web_fetch` disabled).

## Usage notes (from Step 6)

- Use **only** web search in this step.
- Prioritize `.gov`, `.edu`, `nasa.gov`, `esa.int`, and similar trusted domains.
- Flag externally sourced repositories in the **Provenance** bullet of the output.
- A project-website / institutional download URL located via web search is a valid URL (see `guardrails/url-and-hosting-rules.md`).
