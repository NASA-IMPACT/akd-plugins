# Context: NASA Astrophysics Data System (ADS)

## What it is

NASA ADS is the astrophysics literature database. Two capabilities are used:

- **Paper search** (`ads_search_tool`) — Solr-syntax search returning `bibcode`, `title`, `abstract`, `citation_count`, and related fields. It does NOT extract code URLs from full text; discovery comes from reading the `abstract` field.
- **Links resolver** (`ads_links_resolver_tool`) — given a bibcode, returns `associated_bibcodes`, the ADS-curated canonical description papers.

## Astrophysics-only channel

ADS is used **only for Astrophysics queries** (Steps 5b and 5c). Skipped for non-Astrophysics queries.

## Role in the pipeline

- **Step 5b (paper search):** discover codes not in ASCL (newer, institutional, unregistered) and find additional description papers. `citation_count` becomes a Step 7 ranking signal. An ADS title search is required for any well-known checklist code if ASCL has fewer than 2 description bibcodes for it, or if the listed entry has `citation_count < 100` for a flagship code.
- **Step 5c (links resolver):** recover the canonical "Described in" papers that ASCL under-reports, by passing the ASCL record's bibcode and merging the returned `associated_bibcodes` into the candidate's **Describing bibcodes**.

## Constraint

Validate that any URL pulled from an ADS abstract resolves to a public host before including it.

## Runtime availability

In the live runtime environment, ADS/ASCL tooling is available and enabled for Astrophysics:
- `ascl_search_tool` (Step 5a)
- `ads_search_tool` (Step 5b)
- `ads_links_resolver_tool` (Step 5c)

These tools are invoked via their MCP servers as documented in `tools/`.

## Related tools

`tools/ads_search_tool/`, `tools/ads_links_resolver_tool/`.
