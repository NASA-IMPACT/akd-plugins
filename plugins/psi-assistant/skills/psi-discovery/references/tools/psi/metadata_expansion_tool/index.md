# metadata_expansion_tool (draft)

## Purpose
Expand or clarify investigation discovery results using Investigation Metadata Files before or after PSI API calls.

## Uses context
- `context/investigations/<investigation-id>/investigation_metadata.md`

## Intended capabilities
- Investigation identity clarification
- Objective/context enrichment
- Domain/subdomain clarification
- Relevance support
- Top-level investigation summary
- Metadata normalization for discovery

## Open questions
- When should it run (before psi_api_tool, after it, or both)?
- Inputs: investigation ID, user query, and/or discovery result object?
- Outputs: enriched metadata only vs include relevance notes?
- Whether it should rank investigations by match to user query.
- Whether it should return suggested next `psi_api_tool` parameters.
- What to do if investigation metadata file is missing.
