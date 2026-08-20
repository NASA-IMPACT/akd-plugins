# Guardrail enforcement matrix (draft)

Only SME-approved signals are included.

| guardrail_provider | signal_type | signal | scope | default_action | rewrite_policy | escalation_trigger | logging_level | notes |
|---|---|---|---|---|---|---|---|---|
| GraniteGuardianTool | category | harm | INPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | High-confidence → block immediately; repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | social_bias | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | profanity | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | sexual_content | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | unethical_behavior | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | violence | INPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | High-confidence → block immediately; repeated attempts (N=3) → escalate |
| GraniteGuardianTool | category | jailbreak | INPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | High-confidence → block immediately; repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | maliciousness | INPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | Repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | profanity | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | toxicity | INPUT | REFUSE | NONE | REWRITE_FAILED | WARN | Repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | jailbreak-prevention | INPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | Repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | compliance | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Escalate after N=2 rewrite failures |
| RiskAgent | risk_id | privacy | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Escalate after N=2 rewrite failures |
| RiskAgent | risk_id | maliciousness | OUTPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | Refuse; repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | profanity | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Maintain professional scientific tone |
| RiskAgent | risk_id | toxicity | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Maintain professional scientific tone |
| RiskAgent | risk_id | out-of-distribution-checks | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Trigger when content appears outside PSI scope |
| RiskAgent | risk_id | jailbreak-prevention | OUTPUT | REFUSE | NONE | HIGH_CONFIDENCE_RISK | WARN | Refuse; repeated attempts (N=3) → escalate |
| RiskAgent | risk_id | fairness | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Neutrality across groups/paradigms |
| RiskAgent | risk_id | consistency | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Contradictions should be surfaced; avoid self-contradiction |
| RiskAgent | risk_id | uncertainty-identification | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Must express insufficient evidence when applicable |
| RiskAgent | risk_id | verification | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Ensure claims are verifiable from PSI sources |
| RiskAgent | risk_id | ip-and-copyright | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Summarize + cite; avoid large verbatim reproduction |
| RiskAgent | risk_id | hallucination-identification | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | If rewrite fails (N=2) → escalate |
| RiskAgent | risk_id | attribution | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Require accurate citations/provenance |
| RiskAgent | risk_id | overgeneralization | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Avoid over-broad claims; surface limits |
| RiskAgent | risk_id | multidisciplinary-failure | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Require comparability caveat for cross-domain comparisons |
| RiskAgent | risk_id | lack-of-adaptive-reasoning | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Trigger when output fails to adapt to user intent/mode |
| RiskAgent | risk_id | positivity-bias | OUTPUT | REWRITE | REGENERATE_WITH_CONSTRAINTS | REWRITE_FAILED | WARN | Avoid over-optimistic framing; surface uncertainty |
