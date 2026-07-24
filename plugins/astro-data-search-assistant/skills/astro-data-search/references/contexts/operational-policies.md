# Operational Policies

Fixed policies the planner applies while building contracts. Complements the strategy in
`../reasoning.md` and the schema in `../output.md`.

## Must-answer query intents

The agent must handle these end-to-end:
1. Topic/keyword → candidate objects relevant to the science topic.
2. Coordinates and/or object types → objects.
3. Given objects → choose instrument → choose repository.
4. Instrument/observatory observations of an object during a specified event/time window.
5. Instrument/observatory products (spectra / datacube / images) for object names.
6. Within the 90% credible region for an `event_id` from an `alert_source` → object candidates
   or data relevant to a topic/keyword.

## Input normalization

- **Coordinates:** users provide an Astropy `SkyCoord`. Default cone radius **1 arcminute**.
- **Time windows:** accept relative windows ("last 30 days"), convert to ISO dates, then
  **verify with the user before proceeding**.
- **Band/energy strings:** do **not** expand unless the user provides explicit units.

## ADS (literature) policy

- Extract/store ADS metadata fields: title, abstract, keywords, identifier, data, doi, bibcode,
  arxiv, full_text (optional).
- **No citation chasing.**
- Anchor-paper ranking preference (recency vs citations vs relevance): **ask the user.**
- Full text: follow publisher URLs when ADS fulltext isn't available (untrusted — see
  `../guardrails/untrusted-content.md`).
- Entity extraction: only canonical-like object strings. Multi-object ambiguity: **stop and ask
  the user** which object(s) to pursue.

## Name resolution & disambiguation

- Primary resolver: **SIMBAD**. Fallback: **CDS XMatch**.
- If multiple candidates: **stop and ask the user** — no auto-pick.
- Cross-match uses simple positional/radius matching with explicit ambiguity reporting.

## VO / PyVO routing

- Use PyVO for VO services; **Registry discovery is allowed only when user-approved** and must
  stay within the **supported archives** (see `../guardrails/supported-archives-only.md`).
- TAP: **always async when available.** Spatial match: cone-center distance (cone v1; polygon
  where supported).
- Hard filter: **exclude `calib_level = 0` unless the user requests it.**
- Endpoints must come from Registry results or explicit config — never guessed.

## Archives in scope & priorities

- Supported archives (all in scope): **NASA** — MAST, HEASARC, IRSA, NEA, NED, ADS;
  **ESA** — Gaia, ESA Hubble, ESA JWST; **CDS** — SIMBAD, VizieR; **community** — SDSS, ALMA.
  Route by band/mission/instrument; **MAST / HEASARC / IRSA** remain the primary NASA
  repositories, with the ESA/CDS/community modules used when they fit the query.
- Prefer **HLSP / high-level science products** when available.
- Proprietary data: **include but down-rank** (public-first), and label "proprietary until
  DATE." Do not filter proprietary data out; never imply access/entitlement.
- MAST: Observations queries only. IRSA: prefer IRSA-specific APIs. HEASARC: discovery/search +
  access_url. NEA: tables depend on the query.

## Fitness-to-use ordering (deterministic)

Product readiness (science-ready/HLSP > raw) → product match → instrument/mode → public
availability (public-first) → exposure → quality (flags/GTIs), with `calib_level = 0` excluded
as a hard pre-filter unless the user requests it. If required time metadata is missing, filter
out but **notify the user**. Full policy in `../reasoning.md`.

## Alerts / GCN ingestion

- Sources: both **Circulars** and **Notices**; format **JSON**; mode: `event_id` → fetch from
  web-archive endpoints (no streaming/Kafka in v1).
- Extract the best coordinate + uncertainty. If only a skymap link is present, request a
  user-provided cone/polygon.
- Label all alert/localization products **"best-available / uncertain."**

## Output grouping & normalized record

- Default grouping: **paper → object → archive → products.**
- Minimum normalized record fields: obsid (or archive obs identifier), product_filename,
  archive, collection/mission, instrument, access_url, `dataproduct_type` in **IVOA
  nomenclature** (image | cube | spectrum | timeseries | event | catalog), proprietary_until
  (if any), calib_level, exposure_time, time_start, time_end (when available), and provenance
  (queries + endpoints + timestamps). Additional fields may be added as needed.

## Ops baselines

- ADS rate-limit baseline: **5000 requests/day**. Retries: **3** with backoff (search retry
  policy: 3–10 tries). Redact tokens in logs. For services without documented quotas, use conservative
  throttling + caching + retries with backoff on 429/5xx.
