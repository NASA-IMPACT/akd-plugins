# ascl_search_tool — Input / Output

Source: the v1 prompt's Authoritative Data Sources description and Step 5a. (No pydantic signature exists for this tool.)

## Inputs

| Param | Type | Meaning |
|---|---|---|
| `query` | str | Core task terms (e.g., "radiative transfer", "MCMC sampler", "SED fitting") or a specific code name (e.g., `"RADMC-3D"`). |
| `rows` | int | Number of records to return. Process uses `rows=10` for task-term queries and `rows=5` for name lookups. |

Budget: **maximum 4 ASCL queries** per pipeline.

## Outputs — per entry

| Field | Meaning |
|---|---|
| `site_list` | URLs for the code — **not pre-prioritized**. Choose per URL priority; never use the `ascl.net/<id>` landing page as a code URL. |
| `described_in` | Description-paper references, returned as **ADS URLs** (not raw bibcodes). Recover bibcodes by parsing the path segment after `/abs/`. Parse ALL, not just the first. |
| `used_in` | Usage-paper references, also **ADS URLs**. Parse 1–3 that match the user's task. |
| `bibcode` | The ASCL record's own bibcode (e.g., `2010ascl.soft10082F`). Used as input to `ads_links_resolver_tool` in Step 5c, and placed first in **Describing bibcodes**. |
| `used_in_count` | Adoption signal; Step 7 ranking input (broad-query rule: `used_in_count ≥ 30`). |

## Usage notes (from Step 5a)

- Build **Describing bibcodes** ordered: (1) ASCL record `bibcode`, (2) canonical/highly-cited method paper, (3) other description papers chronologically.
- ASCL's `described_in` is often incomplete; recover the canonical method paper via ADS title search (5b) or the links resolver (5c) when needed.
- Add every ASCL-discovered candidate to the running list with provenance `ASCL`.
