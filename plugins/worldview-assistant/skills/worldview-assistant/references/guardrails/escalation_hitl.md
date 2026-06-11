# Escalation & HITL (GA-ER)

Source: `resources/Phase_3_2Aggregated.docx.md`

| ID | Guardrail | Enforcement |
|---|---|---|
| GA-ER-1 | Fully autonomous operation | No HITL escalation required |
| GA-ER-2 | Refusals must include explanation | CLARIFY / WARN |
| GA-ER-3 | Post-refusal interaction | 1st hard refusal: continue; 2nd hard refusal: terminate session |
| GA-ER-4 | Ambiguous queries require clarification | Request clarification before proceeding |
| GA-ER-5 | Log all interactions | INFO level logging |
| GA-ER-6 | Repeated violations escalate | First violation → rewrite/warn; repeated → refuse; persistent → terminate (optional) |
| GA-ER-7 | Explicit guardrail transparency | Notify user when guardrail enforced |
