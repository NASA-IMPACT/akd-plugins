# Context: NASA Science Discovery Engine (SDE)

## What it is

The Science Discovery Engine (SDE) is NASA's centralized search platform that indexes scientific data, publications, and resources from multiple NASA data sources — including CMR (Earth observation), PDS (planetary science), SPASE (heliophysics), GCN (astronomy), code repositories, and documentation. It exposes a unified `/api/search` endpoint providing cross-source vector, keyword, and hybrid (vector + keyword) semantic search over all indexed NASA content.

**SDE is the shared backend for BOTH SDE-backed tools.**

- `sde_search_tool` calls the unified SDE endpoint: `https://dyejsbdumgpqz.cloudfront.net/api/search`.
- `repository_search_tool` calls the SDE code-search endpoint: `https://dyejsbdumgpqz.cloudfront.net/api/code/search` (default; configurable).

`repository_search_tool` also enriches GitHub results (see `contexts/github-metadata.md`).

## Key behavior: min_score = 0.0 (threshold 0, deliberate)

Both SDE-backed searches send `min_score=0.0` (relevance threshold zero) in the request payload. **This is deliberate — if `min_score` is omitted, the server applies a higher default threshold that can silently drop most documents.** Consequence for the agent: SDE results can include low-relevance documents; use the returned `score` (and, for repositories, `reliability_score`) to weigh candidates rather than assuming everything returned is on-topic.

## Role in the pipeline

- Underlies **Step 2** primary discovery (via `repository_search_tool`).
- Underlies **Step 3** context enrichment (via `sde_search_tool`, one query) — validating domain alignment, refining repository purpose, and surfacing additional repositories from NASA technical reports and mission documentation.

## Per-domain strength

- **Strongest for Earth Science, Heliophysics, and Planetary Science** (NASA institutional documentation and mission channels are well-indexed here).
- **Lower-yield for Astrophysics** — community codes are often documented outside NASA institutional channels; for Astrophysics keep to one brief SDE query and rely on Step 5 (ASCL + ADS).
- **Biological and Physical Sciences:** no specific strength claim is made in the source prompt; treat SDE as **general-purpose enrichment** (run the standard Step 3 query), with no elevated or reduced expectation.

## Related tools

`tools/sde_search_tool/`, `tools/repository_search_tool/`.
