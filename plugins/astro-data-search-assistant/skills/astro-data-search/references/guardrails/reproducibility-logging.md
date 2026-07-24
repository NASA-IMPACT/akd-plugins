# Reproducibility & Logging

The agent (and the contract it emits) must support reproducibility:

- Save logs sufficient to reproduce a run: query parameters, endpoints/services used,
  timestamps, and returned identifiers/URLs.
- Include provenance in outputs (bibcodes, exact queries/ADQL, services/endpoints).
- The `audit` block of the contract records environment (library versions), requests/retries,
  and the branching log (see `../output.md`).
- Redact secrets/tokens in all logs.

Log retention: **30 days**.

Access: operating user/team only.

Redaction: redact tokens/secrets and any user-provided PII. Logs keep only queries, endpoints, timestamps, and returned identifiers/URLs.
