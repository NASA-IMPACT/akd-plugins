# Malicious / adversarial use guardrails (GA-MA)

Source: `resources/Phase_3_2Aggregated.docx.md`

| ID | Guardrail | Enforcement |
|---|---|---|
| GA-MA-1 | Treat instruction override/jailbreak attempts as malicious | REFUSE input, block via GraniteGuardianTool |
| GA-MA-2 | Apply guardrails consistently regardless of framing | REFUSE output if constraints bypassed |
| GA-MA-3R | Restrict responses to explicitly requested datasets | REFUSE retrieval of non-requested datasets; suggest only if user confirms |
| GA-MA-4R | Cross-turn intent tracking | REFUSE outputs leading to disallowed interpretation across turns |
| GA-MA-5 | Prevent recombination of outputs into disallowed insights | REFUSE / REWRITE if detected |
| GA-MA-6 | Refuse requests to reframe outputs as conclusions | REFUSE output |
| GA-MA-7 | Log repeated boundary violations | Escalate to WARN level after threshold, enforce hard refusal on second hard refusal |
