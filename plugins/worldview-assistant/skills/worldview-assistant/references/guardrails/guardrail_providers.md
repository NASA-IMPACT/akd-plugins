# Guardrail provider configuration

Source: `resources/Phase_3_2Aggregated.docx.md` + taxonomy reference `phase_3_reasoning_policy_and_guardrails/prompts/guardrails_risk_taxonomy_reference.md`

## Execution order
- Input: GraniteGuardianTool → RiskAgent
- Output: RiskAgent

## GraniteGuardianTool (INPUT)
- Enabled harm categories:
  - Jailbreak / Prompt Injection
  - Instruction Override / Manipulation
  - Policy Evasion
  - Malicious Intent
  - Violence
  - Self-harm
  - Hate
  - Sexual Content
- Disabled categories: none
- Enforcement action: block input (REFUSE) immediately upon trigger

## RiskAgent (OUTPUT)
RiskAgent supports only the taxonomy risk IDs listed in the taxonomy reference.

### Mapping to taxonomy risk IDs (SME-approved)
From `resources/Phase_3_2Aggregated.docx.md` human-readable labels → RiskAgent taxonomy IDs:
- Hallucination → `hallucination-identification`
- Inference → `verification`
- Over-interpretation → `overgeneralization`
- Authoritative Framing → `consistency`
- Scope Violation → `compliance`
- Data Transformation Misuse → `verification`

### Allowed RiskAgent taxonomy risk IDs
- compliance
- privacy
- maliciousness
- profanity
- toxicity
- out-of-distribution-checks
- jailbreak-prevention
- fairness
- consistency
- uncertainty-identification
- verification
- ip-and-copyright
- societal-impact
- hallucination-identification
- attribution
- static-knowledge
- outdated-confidence
- overgeneralization
- multidisciplinary-failure
- lack-of-adaptive-reasoning
- positivity-bias
