# Metadata Integrity

The agent must **never**:
- Invent variable names, definitions, units, QA flags, or coverage.
- Infer semantics from similar datasets or general domain knowledge.
- Assume undocumented attributes, even when commonly expected.

All undocumented attributes are treated as **unknown**. Incomplete metadata is **neutral** — it
neither penalizes nor promotes a dataset. Missing = unknown, not bad.

Every surfaced dataset must originate from CMR and carry a valid CMR Concept ID. GCMD keywords
may inform search terms only and must never be presented as datasets. Applies to every step.
