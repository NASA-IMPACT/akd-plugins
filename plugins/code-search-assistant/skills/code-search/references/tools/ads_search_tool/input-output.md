# ads_search_tool — Input / Output

Source: the v1 prompt's Authoritative Data Sources description and Step 5b. Uses Solr query syntax. (No pydantic signature exists for this tool.)

## Inputs

| Param | Type | Meaning |
|---|---|---|
| `query` | str (Solr) | ADS Solr-syntax query (see patterns below). |
| `rows` | int | Records to return. Process uses `rows=5`. |
| `fq` | str (optional) | Solr filter query, e.g. `fq="property:refereed"` when targeting description papers. |

Budget: **maximum 4 ADS queries, `rows=5` each.**

## Discovery query patterns (verbatim)

- `abs:"<task_description>" AND (abs:"code" OR abs:"simulation" OR abs:"software")`
- `abs:"code comparison" AND abs:"<subfield_term>"` or `abs:"benchmark" AND abs:"<subfield_term>"` for benchmark/comparison papers.
- `abs:"review" AND abs:"<task_term>" AND (abs:"code" OR abs:"software")` for review papers.
- `title:"<code_name>"` for precise code lookups; add `fq="property:refereed"` when targeting description papers.

## Outputs — per paper

| Field | Meaning |
|---|---|
| `bibcode` | ADS bibcode. |
| `title` | Paper title. |
| `abstract` | Full abstract — the field read for code discovery (the tool does NOT extract code URLs from full text). |
| `citation_count` | Total citations; Step 7 ranking signal for new and existing candidates (title-search trigger threshold `< 100` for flagship codes; broad-query rule threshold `≥ 500` for the canonical method paper). |
| (other) | Additional standard ADS fields. |

## Usage notes (from Step 5b)

- For each newly discovered code, add to the running list with provenance `ADS`.
- Validate that any URL pulled from an abstract resolves to a public host before including.
