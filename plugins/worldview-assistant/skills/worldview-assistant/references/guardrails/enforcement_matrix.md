# Guardrail enforcement matrix

Source: `resources/Phase_3_2Aggregated.docx.md`

## Matrix (provider signal → enforcement)

| guardrail_provider | signal_type | signal | scope | default_action | rewrite_policy | escalation_trigger | logging_level | notes |
|---|---|---|---|---|---|---|---|---|
| GraniteGuardianTool | category | Jailbreak / Prompt Injection | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Instruction Override / Manipulation | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Policy Evasion | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Malicious Intent | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Violence | INPUT | REFUSE | NONE | NONE | HIGH | Blocks harmful input immediately |
| GraniteGuardianTool | category | Self-harm | INPUT | REFUSE | NONE | NONE | HIGH | Blocks harmful input immediately |
| GraniteGuardianTool | category | Hate | INPUT | REFUSE | NONE | NONE | HIGH | Blocks harmful input immediately |
| GraniteGuardianTool | category | Sexual Content | INPUT | REFUSE | NONE | NONE | HIGH | Blocks harmful input immediately |

### RiskAgent rows
Mapping from Phase_3_2Aggregated human-readable labels to taxonomy IDs is documented in `guardrail_providers.md`.

RiskAgent rows (SME-approved taxonomy IDs):
| guardrail_provider | signal_type | signal | scope | default_action | rewrite_policy | escalation_trigger | logging_level | notes |
|---|---|---|---|---|---|---|---|---|
| RiskAgent | risk_id | hallucination-identification | OUTPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | HIGH | Prevents fabricated content (maps from: Hallucination) |
| RiskAgent | risk_id | verification | OUTPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | HIGH | Prevents unwarranted assumptions / unsupported transformations (maps from: Inference; Data Transformation Misuse) |
| RiskAgent | risk_id | overgeneralization | OUTPUT | REWRITE | REGENERATE_ONCE | MULTIPLE_RISKS | HIGH | Reduces over-interpretation (maps from: Over-interpretation) |
| RiskAgent | risk_id | consistency | OUTPUT | REWRITE | REGENERATE_ONCE | NONE | HIGH | Neutralizes authoritative framing (maps from: Authoritative Framing) |
| RiskAgent | risk_id | compliance | OUTPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | HIGH | Enforces operational limits / scope boundaries (maps from: Scope Violation) |
