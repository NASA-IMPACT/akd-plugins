# Guardrail provider configuration (draft)

## Execution model
- Input guardrail: GraniteGuardianTool → RiskAgent
- Output guardrail: RiskAgent

## GraniteGuardianTool (INPUT)
- Enabled categories (SME-approved):
  - harm
  - social_bias
  - profanity
  - sexual_content
  - unethical_behavior
  - violence
  - jailbreak
- Disabled categories: none
- Default enforcement when triggered:
  - REFUSE
  - Repeated attempts (N=3): ESCALATE
- High-confidence jailbreak/harm: block immediately

## RiskAgent (INPUT)
- Enabled risk IDs (SME-approved for input monitoring):
  - maliciousness
  - profanity
  - toxicity
  - jailbreak-prevention
- Default enforcement:
  - REFUSE
  - Repeated attempts (N=3): ESCALATE

## RiskAgent (OUTPUT)
- Enabled risk IDs (SME-approved):
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
  - hallucination-identification
  - attribution
  - overgeneralization
  - multidisciplinary-failure
  - lack-of-adaptive-reasoning
  - positivity-bias

- Explicitly excluded from active monitoring (SME-approved):
  - societal-impact
  - static-knowledge
  - outdated-confidence

- Default enforcement (SME-approved):
  - For maliciousness and jailbreak-prevention: REFUSE; repeated attempts (N=3) → ESCALATE
  - For other enabled output risks: REWRITE (regenerate with constraints)
    - rewrite_policy: REGENERATE_WITH_CONSTRAINTS
    - escalation_trigger: REWRITE_FAILED (after N=2 rewrite failures)
