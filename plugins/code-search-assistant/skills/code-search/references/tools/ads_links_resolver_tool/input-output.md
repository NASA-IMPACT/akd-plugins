# ads_links_resolver_tool — Input / Output

Source: the v1 prompt's Authoritative Data Sources description and Step 5c. (No pydantic signature exists for this tool.)

## Inputs

| Param | Type | Meaning |
|---|---|---|
| `bibcode` | str | A single ADS bibcode — specifically the **ASCL record's own bibcode** (e.g., `2010ascl.soft10082F`). |

Budget: **maximum 4 uses across the pipeline** (one per ASCL record bibcode). May be called multiple times within Step 5 with different bibcodes.

## Outputs

| Field | Meaning |
|---|---|
| `associated_bibcodes` | ADS-curated canonical description papers for the given record. Merge new bibcodes into the candidate's **Describing bibcodes**, deduplicating against ASCL's `described_in`. |

## Usage notes (from Step 5c)

- Use whenever a candidate has fewer than 2 describing bibcodes from ASCL, or its `described_in` paper has obviously low citations relative to the code's stature.
- Purpose: recover the canonical method paper that ASCL under-reports (e.g., FLASH canonical `2000ApJS..131..273F` vs. the low-citation update paper ASCL may list).
