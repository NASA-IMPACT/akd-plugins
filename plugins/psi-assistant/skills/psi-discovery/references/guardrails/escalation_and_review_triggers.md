# Escalation & review triggers

## Escalation destinations
- Technical/source conflicts: escalate to user for adjudication.
- Jailbreak/security events: log + escalate to admin (not user-facing).

## Hard-stop conditions
- Restricted/contractual content request.
- High-confidence jailbreak/harm input.
- Detected document-embedded injection (logged; treated as a guardrail event).
- Repeated rewrite failure on output guardrails.

## Thresholds
- Repeated adversarial attempts threshold: N = 3.
- Tool failures (404/expired URL/timeouts): escalate after N = 3 consecutive failures.
- Output rewrite failures: escalate after N = 2 rewrite failures.

## Logging levels
- Guardrail block: WARN.
- Output rewrite: WARN.
- Escalations: HIGH.
- Document injection: WARN.
