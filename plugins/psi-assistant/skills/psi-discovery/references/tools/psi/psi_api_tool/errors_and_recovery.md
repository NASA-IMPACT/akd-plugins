# Errors & recovery patterns (draft)

## Known failure modes (from existing systems inventory)
- Missing files (legacy subset): HTTP 404 due to missing S3 objects.
- Expired signed URLs: previously returned `remote_url` becomes invalid after ~7 days.
- Timeouts on very large investigations (>10k files).
- Migration instability during `geode-py/ws/` → `psi/data/` transition.

## Required runtime guidance (confirmed intent)
- Retry guidance where appropriate.
- Re-query guidance for expired URLs.
- Warn on legacy `/legacy/` missing-file risk.
- Suggest narrowing queries for large result sets.

## TBD
- Exact standardized error envelope/schema.
