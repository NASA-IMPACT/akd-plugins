# Safety scope summary

## Agent scope
- Assistive scientific knowledge & data assistant for NASA PSI.
- Operates over a public/unauthenticated PSI API and an ingested `context/` workspace.
- Permitted outputs include evidence-backed, caveated interpretation (non-authoritative) with human-in-the-loop for final decisions.

## Primary safety drivers
- Legacy data and operational failure patterns: elevated 404s in legacy subset; timeouts for very large investigations; expiring signed URLs.
- Indirect prompt-injection exposure via ingested documents.
- No authentication/identity signal available via the public API; enforcement relies on behavioral heuristics.
- Mixed user expertise; multi-domain scientific content.

## Guardrail providers
- Input screening: GraniteGuardianTool → RiskAgent.
- Output screening: RiskAgent.
