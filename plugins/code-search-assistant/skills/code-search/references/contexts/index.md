# Contexts

Data sources (as systems) and per-SMD-division routing (as domains) for the Scientific Code Discovery Agent. System files describe what each channel is and its per-domain strength; domain files describe how a query in that SMD division is routed across channels.

## Runtime-generated Expected Codes checklist (note)

The **Expected Codes checklist is generated at runtime** by the agent in Step 1 (5–8 well-known, widely-cited codes derived from domain knowledge for the specific query). It drives gap-detection in Steps 5–6. There is **no stored, per-domain checklist** in this workspace, and none should be fabricated; the domain files describe routing, not fixed code lists.

## Systems (data sources / channels)

- `science-discovery-engine.md` — NASA SDE. `sde_search_tool` uses `/api/search`; `repository_search_tool` uses `/api/code/search` (default/configurable). Documents the deliberate `min_score=0.0` behavior and per-domain strength. Applies at Steps 2–3.
- `github-metadata.md` — GitHub REST enrichment of `github.com` results and the tool-owned `reliability_score` formula; also records the "NASA-Verified" label vs. real-implementation correction. Applies at Step 2.
- `ascl.md` — Astrophysics Source Code Library; code-first records with `site_list`, `described_in`/`used_in` (ADS URLs), `bibcode`, `used_in_count`. Astrophysics only, Step 5a.
- `nasa-ads.md` — NASA ADS paper search and links resolver; `citation_count`, `associated_bibcodes`. Astrophysics only, Steps 5b/5c.
- `code-signals.md` — static code inspection to resolve ambiguity. Conditional, Step 4.
- `external-web-search.md` — builtin `web_search` (medium context); `web_fetch` disabled. Supplementary; Step 6 completeness pass.

## Domains (per SMD division routing)

- `astrophysics.md` — full pipeline incl. ASCL + ADS (Steps 5a/5b/5c); 16-call budget; SDE low-yield.
- `earth-science.md` — non-Astro routing; skip Step 5; SDE strongest; 10-call budget.
- `heliophysics.md` — non-Astro routing; skip Step 5; SDE strongest; 10-call budget.
- `planetary-science.md` — non-Astro routing; skip Step 5; SDE strongest; 10-call budget.
- `biological-and-physical-sciences.md` — non-Astro routing; skip Step 5; SDE used as general-purpose enrichment; 10-call budget.
