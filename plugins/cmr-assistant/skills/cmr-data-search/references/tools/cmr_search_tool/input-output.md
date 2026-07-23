# cmr_search_tool — Input / Output

> **Runtime mapping.** The abstract `cmr_search_tool` is the connected `cmr` server's
> **`search_collections`** tool. The parameter list below is the tool's *actual* schema — the
> server has **no** `science_keywords`, `sort_key`, `point`, `polygon`, `project`,
> `data_center`, or `archive_center` fields. Normalized GCMD prefLabels go into `keyword`;
> relevance ordering is done by the agent, not by a server sort. (`get_granules` and
> `get_collection_metadata` are the other two tools — see `../../SKILL.md`.)

Searches CMR collections and returns candidate datasets with Concept IDs and UMM metadata.

## Inputs

At least one constraint is required — prefer `keyword`. Named platforms/instruments are applied
as hard filters. All spatial/temporal constraints require prior user confirmation.

| Param | Meaning |
|---|---|
| `keyword` | Free-text search across collection metadata. **Normalized GCMD prefLabels go here** (no separate keywords field). |
| `platform`, `instrument` | GCMD-normalized hard filters. |
| `processing_level` | Processing-level filter (e.g. `L2`, `L3`). |
| `temporal` | `YYYY-MM-DDTHH:mm:ssZ,YYYY-MM-DDTHH:mm:ssZ` (only after user confirmation). |
| `bounding_box` | Spatial constraint `west,south,east,north` (only after user confirmation). |
| `provider`, `short_name`, `version` | Additional filters. |
| `page_size`, `page_num` | Paging. |

## Outputs

CMR returns a `hits` count and an `items` array. Per collection the agent extracts:

- `concept_id` (the required identifier)
- short name / entry title
- description / summary
- variables (verbatim)
- temporal coverage
- spatial coverage
- platforms and instruments
- ProcessingLevelId
- related URLs (documentation / DAAC landing pages only; no direct download links)

**Missing fields are treated as unknown — never inferred or fabricated**
(`../../guardrails/metadata-integrity.md`). Full response shape and field detail in
`../../contexts/cmr-metadata-model.md`.
