# Output format specification

## SME-validated decisions

- **Response style**: Hybrid (structured + narrative).
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Knowledge-level adaptation**: Support Beginner / Intermediate / Advanced with a shared base schema + conditional extensions.
  - Source: `resources/Phase2.3_OUTPUTFormatting.md`
  - Status: confirmed

- **Structured backend schema visibility**: Kept internal by default.
  - Only show the structured schema when the user explicitly requests it (e.g., asks to show details / technical metadata / provenance / structured output).
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

Keep the default user-visible response short and non-redundant:
- 1–2 sentences describing what the link shows (layer(s), date/time, and region/area-of-interest)
- the Worldview link
- one line with the single most important caveat (choose the caveat most directly tied to the user’s stated goal)
- one line non-authoritative disclaimer (no policy guidance implied)
- a closing hint: *Type **show details** for dataset IDs, uncertainty, and provenance.*

Do not:
- repeat caveats or the disclaimer
- list configuration that is already visible in the Worldview link

### Internal structured detail (Markdown) — user-triggered

The agent must always produce the structured detail internally as deterministic Markdown (per the schema in this document), but keep it hidden by default.

Show the full detail only when the user explicitly requests details/technical output (e.g., “show details”, “show technical metadata”, “show provenance”, “show structured output”). When shown, include:
- the full narrative (including caveats and uncertainty details)
- citations/provenance fields (if available)
- the complete structured schema dump (the internal Markdown)

## TBD
- Exact stable fields to rely on from CMR/search_worldview_layers/SDE/EONET tool responses.
- Whether to include explicit tool call logs in the internal schema.
