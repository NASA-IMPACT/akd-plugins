# Output format specification

## SME-validated decisions

- **Response style**: Hybrid (structured + narrative).
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Knowledge-level adaptation**: Support Beginner / Intermediate / Advanced with a shared base schema + conditional extensions.
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Structured backend schema visibility**: Kept internal by default.
  - Only show the structured schema:
    - after the final output (when the Worldview permalink is generated), and/or
    - if the user explicitly asks for technical/structured output.
  - Source: SME chat
  - Status: confirmed

- **Permalink inclusion**: Worldview visualizations must be provided as URLs; encoded image data not required.
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Citations & provenance exposure**: Hidden by default; offer optional expansion.
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Uncertainty handling**:
  - disclose uncertainty whenever applicable
  - include dataset-specific uncertainty when citable; otherwise include generic fallback statement
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Missing data rules**:
  - required fields always present in the structured schema
  - missing mandatory fields must be explicitly marked (e.g., `NOT_AVAILABLE_FROM_SOURCE`) and explained where possible
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Disclaimer requirement**: Every response must include a non-authoritative disclaimer (no policy guidance implied).
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Restrictions on claims**:
  - policy recommendations prohibited
  - causal/predictive/interpretive/conclusive/severity statements permitted only if cited per statement
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

## Structured output template (internal by default)

### Base schema (always produced internally)

The structured output should be produced as deterministic **Markdown** (more human-readable than JSON).

```md
## Structured output (internal)

- schema_version: 1.0
- user_level: BEGINNER | INTERMEDIATE | ADVANCED | UNKNOWN

### user_request
- raw: "..."
- normalized_intent: "..."
- clarifying_questions:
  - "..."
- assumptions:
  - "..."
- open_questions:
  - "..."

### recommendations
#### collections
- collection_concept_id: "C...-..." | NOT_AVAILABLE_FROM_SOURCE
- collection_title: "..." | NOT_AVAILABLE_FROM_SOURCE
- layer_id: "..." | NOT_AVAILABLE_FROM_SOURCE
- layer_id_source: best | best_pending_gibs | name_stripped | name_raw | unresolved | NOT_AVAILABLE_FROM_SOURCE
- available_in_gibs: true | false | NOT_AVAILABLE_FROM_SOURCE
- worldview_permalink: "https://..." | NOT_AVAILABLE_FROM_SOURCE
- why_recommended:
  - "..."
- caveats:
  - "..."
- uncertainty:
  - dataset_specific: "..." | NOT_AVAILABLE_FROM_SOURCE
  - generic_fallback: "..."

### provenance
- citations_enabled: false
- citation_items: []

### disclaimer
- "..."

### missing_data
- missing_fields:
  - "..."
- missing_explanations:
  - "..."
```

Notes:
- Field set is a starting point; advanced mode may expose additional metadata.
- `worldview_permalink` should only be populated when the layer set is complete (per tool policy).

### User-facing narrative (always visible)

Narrative should:
- be adapted to user level
- avoid uncited interpretive/causal claims
- include a non-authoritative disclaimer
- offer only **relevant/actionable** optional actions (not a fixed always-on list), such as:
  - “Would you like to see dataset details and citation information?”
  - “Show technical metadata”
  - “Download dataset link” (only when a dataset/collection has been identified)

### Optional expansions (user-triggered)

When requested by the user (or in Advanced mode if desired), provide:
- citations/provenance fields (dataset name, DOI/persistent ID, satellite/instrument, processing level, timestamp, catalog link, version)
- structured schema dump (the internal Markdown) — typically provided alongside the final permalink

## TBD
- Whether to expose machine-readable provenance automatically in Advanced mode vs only on request.
- Exact stable fields to rely on from CMR/search_worldview_layers/SDE/EONET tool responses.
- Whether to include explicit tool call logs in the internal schema.
