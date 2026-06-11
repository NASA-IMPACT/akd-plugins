# Hallucination & inference boundaries (GA-HI)

Source: `resources/Phase_3_2Aggregated.docx.md`

| ID | Guardrail | Enforcement |
|---|---|---|
| GA-HI-1 | Explicitly state unavailable data, stop response | REFUSE substitution |
| GA-HI-2 | Partial outputs must be flagged | CLARIFY / WARN if missing label |
| GA-HI-3 | No metadata inference | REFUSE if inferred; suggestions labeled as possible only |
| GA-HI-4 | Explain pre-defined metrics | CLARIFY if missing |
| GA-HI-5 | Avoid describing trends | REFUSE/REWRITE output with trends |
| GA-HI-6 | Controlled language policy | REWRITE if interpretive verbs used |
| GA-HI-7 | Include explicit limitations/uncertainty | CLARIFY if missing |
