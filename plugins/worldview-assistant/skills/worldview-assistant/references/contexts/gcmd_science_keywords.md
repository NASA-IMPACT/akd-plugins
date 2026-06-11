# GCMD Science Keywords (sciencekeywords.csv)

## Source
- `resources/sciencekeywords.csv`

## How this is used in practice (SME)
- Used to **enrich the user query** for:
  - intent→keyword mapping
  - query expansion
  - validation
  - user-facing explanation
  - tagging
- Most relevant when there is an **exact mapping**.

## When it becomes relevant (stage)
- **Intent intake**
- **Before dataset discovery**

## Task type
- Lookup

## What parts are used vs ignored
- Used: `Category`, `Topic`, and `Variable_Level_*` (variable levels)
- Ignored / not used (for now): `UUID`, `Detailed_Variable`, and header metadata rows (unless needed later)

## Authority
- Helpful reference (advisory), not a source of truth.

## Mandatory vs optional
- Optional
- Consult when the user’s question is **ambiguous** (to propose/expand terms)

## Expected output when used
- **Expanded terms** (for query expansion / enrichment)

## Trigger mapping (WHEN to check)
- Task-based: when entering **intent intake**
- Task-based: just before **dataset discovery**
- Uncertainty-based: when the user request is **ambiguous** (to expand/normalize terms)
