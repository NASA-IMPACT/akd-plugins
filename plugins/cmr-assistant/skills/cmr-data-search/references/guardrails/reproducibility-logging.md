# Reproducibility & Logging

Whenever searches are executed, the agent must emit a **Search Reproducibility Log** (see
`../output.md`) covering:
- Tool calls / CMR endpoints used.
- Query parameters (keywords, GCMD mappings, spatial/temporal filters).
- Paging behavior.
- Ranking logic (relevance primary; usage as a tie-breaker only).
- UTC timestamps.

Logs are not required for purely conceptual discussion with no tool use. Ranking criteria and
decision paths must always be transparent. This supports auditability and reproducibility of
every recommendation-free result set.
