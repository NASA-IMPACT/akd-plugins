# Sensitive / restricted domains (GA-SD)

Source: `resources/Phase_3_2Aggregated.docx.md`

| ID | Guardrail | Enforcement |
|---|---|---|
| GA-SD-1 | Public data only access | Enforce via agent data access rules |
| GA-SD-2 | Upstream sensitivity handled externally | REFUSE attempt to access sensitive datasets |
| GA-SD-3 | No embargoed data | REFUSE access |
| GA-SD-4 | Non-sensitive metadata | No action needed |
| GA-SD-5 | No user-uploaded data | REFUSE any uploaded input |
| GA-SD-6 | No derived sensitivity risk | Not applicable |
| GA-SD-7 | No resolution/geospatial restrictions at agent-level | Not applicable; handled upstream |
