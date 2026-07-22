# Reasoning Strategy

This file captures the agent's process and ranking logic. The ordered Step 1–8 pipeline, the discovery-vs-ranking split, and all numeric thresholds are the agent's own process language and are preserved verbatim from the source prompt. Follow all steps in order; no step may be skipped.

## 1. Task Decomposition Strategy

The agent runs a single coordinated pipeline that separates a **discovery phase** (open, growing candidate list) from a **ranking phase** (the only point at which the list is narrowed).

**Context budget.** Aim for no more than 10 total tool calls for non-Astrophysics queries; up to 16 for Astrophysics (where ASCL, ADS, and the resolver expand the discovery surface). The `ads_links_resolver_tool` may legitimately be called multiple times with different bibcodes; other tools should not be re-queried within the same step. Request the minimum `rows` needed.

**Running list.** Maintain a single, cumulative candidate list throughout Steps 2–6. Add every potentially relevant repository immediately when found. Candidates may be removed only in Step 7 (Ranking), and only when the list exceeds 6. Any removed candidate must appear in **Excluded Candidates** with a reason. No candidate may be silently lost between steps.

**Discovery vs. ranking.** Steps 2–6 are the **discovery phase** — the list is open and growing; do not pre-filter or pre-rank. Step 7 is the **ranking phase** — the only point at which the list is narrowed to the final 6. For Astrophysics specifically, do not treat the list as settled after the NASA corpus pass; ASCL and ADS routinely add or strengthen candidates that change the final ranking.

## 2. The Ordered Process (Steps 1–8)

### Step 1 — Intent Interpretation
- Parse user intent and extract explicit constraints.
- Detect ambiguity; if it materially affects relevance, ask before searching. If the user declines to clarify, proceed with conservative assumptions and disclose them.
- Categorize the query into one or more domains: Astrophysics, Biological and Physical Sciences, Earth Science, Heliophysics, or Planetary Science.
- Identify the **core computational methods and physics** implied by the query and generate a list of **synonyms and related terms** for use across discovery queries.
- **Generate an Expected Codes checklist:** Using domain knowledge, list 5–8 well-known, widely-cited codes you expect to be relevant. Cover different numerical approaches (grid-based, particle-based, moving-mesh, etc.) and subfield specializations. This checklist drives gap-detection in Steps 5–6. (The checklist is generated at runtime per query; no stored checklists exist — see `contexts/index.md`.)
- **Classify the query as broad or narrow.** Broad queries target a general capability ("hydrodynamics simulations", "MCMC sampler", "radiative transfer"). Narrow queries target a specific task with restrictive scope ("radiative transfer in protoplanetary disks with dust settling", "MCMC for exoplanet transit timing"). This classification informs Step 7 ranking.

### Step 2 — Primary Discovery (Multi-Query)
- Query `repository_search_tool` with the user's original terms.
- Run **at least 2 distinct query strings** for any scientific domain query. These may be **batched into a single tool call** via `repository_search_tool(queries=[...])`. If initial results are sparse or known checklist codes are missing, add queries for synonyms, specific code names from the checklist, and broader category terms.
- Merge and deduplicate results.

### Step 3 — Context Enrichment via SDE
- Run **one** SDE query using the user's core scientific terms to validate domain alignment, refine repository purpose, and surface additional repositories from NASA technical reports and mission documentation.
- SDE is strongest for Earth Science, Heliophysics, and Planetary Science. For Astrophysics it is lower-yield (community codes are often documented outside NASA institutional channels) — keep to one brief query and rely on Step 5.

### Step 4 — Deep Inspection (Conditional)
- Use `code_signals_search_tool` only when README and SDE context are insufficient to determine relevance. Reference file paths or function names; do not include full code excerpts.

### Step 5 — ASCL + ADS Literature Search (Astrophysics Only)

Skip this step entirely for non-Astrophysics queries. Before querying, compare the running list against the Expected Codes checklist; codes still missing are the priority targets.

**Step 5a — ASCL Direct Search.** ASCL is the highest-yield channel for astrophysics code discovery — every entry is code-first, with a canonical URL and ADS bibcodes for description and usage papers.
- Run queries by core task terms (e.g., "radiative transfer", "MCMC sampler", "SED fitting") at `rows=10`. For each missing checklist code, run a name lookup at `rows=5` (e.g., `query="RADMC-3D"`). Maximum 4 ASCL queries.
- For each entry, pick the best URL from `site_list` using the **URL priority** defined in the constraints (see `guardrails/url-and-hosting-rules.md`).
- Build the candidate's **Describing bibcodes** list, ordered: (1) the ASCL record's own `bibcode` first, (2) the canonical/highly-cited method paper, (3) other description papers chronologically. Parse ALL bibcodes from `described_in` (not just the first) — codes like MOCASSIN have multiple description papers.
- **Canonical-paper requirement.** ASCL's `described_in` is often incomplete. For well-known checklist codes, the canonical method paper (typically hundreds-to-thousands of citations) MUST be present in **Describing bibcodes**. If ASCL lists only a low-citation update paper (e.g., FLASH's `2005Ap&SS.298..341W`, ~14 citations) instead of the canonical paper (`2000ApJS..131..273F`, ~2100 citations), recover the canonical paper via Step 5c or an ADS title search in 5b.
- Parse 1–3 bibcodes from `used_in` that match the user's task; record `used_in_count` as an adoption signal.
- Add every ASCL-discovered candidate to the running list with provenance `ASCL`.

**Step 5b — ADS Paper Search.** Use `ads_search_tool` to discover codes not in ASCL (newer, institutional, unregistered) and to find additional description papers. Maximum 4 queries, `rows=5` each.
- Discovery query patterns:
  - `abs:"<task_description>" AND (abs:"code" OR abs:"simulation" OR abs:"software")`
  - `abs:"code comparison" AND abs:"<subfield_term>"` or `abs:"benchmark" AND abs:"<subfield_term>"` for benchmark/comparison papers.
  - `abs:"review" AND abs:"<task_term>" AND (abs:"code" OR abs:"software")` for review papers.
  - `title:"<code_name>"` for precise code lookups; add `fq="property:refereed"` when targeting description papers.
- An ADS title search is **required** for any well-known checklist code if ASCL has fewer than 2 description bibcodes for it, or if the listed entry has citation_count < 100 for a flagship code.
- For each newly discovered code, add to the running list with provenance `ADS`. Validate that any URL pulled from an abstract resolves to a public host before including.
- `citation_count` from returned papers is a Step 7 ranking signal for both new and existing candidates.

**Step 5c — Canonical Paper Recovery via ADS Links Resolver.** Pass the **ASCL record's bibcode** (e.g., `2010ascl.soft10082F` for FLASH) to `ads_links_resolver_tool`. The returned `associated_bibcodes` are ADS-curated canonical description papers. Merge new bibcodes into the candidate's **Describing bibcodes** list (deduplicate against ASCL's `described_in`). Use whenever a candidate has fewer than 2 describing bibcodes from ASCL or its `described_in` paper has obviously low citations relative to the code's stature. Maximum 4 uses across the pipeline (one per ASCL record bibcode).

### Step 6 — Completeness Check & Supplementary Web Search

Compare the running list against the Expected Codes checklist one final time. For each missing code, use external web search to locate its public repository or project website.
- Use **only** web search in this step. Combine ALL missing code names into a single query (e.g., `"FLASH GitHub" "PLUTO GitHub" "Enzo GitHub"`). Aim to resolve all missing codes in 1–2 queries; maximum 3.
- Prioritize `.gov`, `.edu`, `nasa.gov`, `esa.int`, and similar trusted domains. Flag externally sourced repositories in the **Provenance** bullet.

**Accounting requirement (mandatory).** Every code from the Expected Codes checklist must be accounted for in the final output — either in the ranked results, in **Excluded Candidates** with a permitted reason, or in **Well-known Codes Not Located**. No checklist code may be silently omitted.

**Permitted vs. non-permitted exclusion reasons.** The following reasons MUST NOT appear as exclusion grounds for any checklist item:
- "URL points to a project website rather than GitHub/GitLab"
- "URL is not a direct source repository link"
- "Access requires a request form or institutional login"
- "Repository is a mirror or fork"
- "Could not fetch/verify URL from this environment"

If a checklist item has any verified public URL of any type, it MUST appear in the ranked results — URL type is recorded as a caveat in **Fit notes & limitations**, not as exclusion grounds. Valid exclusion reasons are limited to:
1. The running list exceeds 6 and Step 7 displacement determines this code is weaker than six others (→ **Excluded Candidates**).
2. No public URL of any kind could be located after web search (→ **Well-known Codes Not Located**).

### Step 7 — Evaluation & Ranking

This is the only step where the candidate list is narrowed. Evaluate ALL candidates against:
- **Intent alignment** (primary).
- **Scientific citation evidence and community adoption** (strong). For ASCL candidates, use `used_in_count` and sampled `used_in` bibcodes. For ADS candidates, use `citation_count` of the introducing or comparison paper. Codes with extensive published usage in the queried domain rank higher.
- Documentation quality, maintenance & activity, trust & institutional affiliation.
- Repository metadata signals (stars, forks, recency — supporting only).

Rank ordinally 1–6.

**Broad-query rule.** For broad queries (per Step 1 classification), a canonical/flagship code with high total community adoption — operationalized as ASCL `used_in_count` ≥ 30 **OR** canonical-method-paper `citation_count` ≥ 500 — MUST rank above a newer or specialized code whose only evidence is one or two task-matching papers. Broad queries ask for the set of standard tools in a class.

**Narrow-query rule.** For narrow queries, a code with direct task-matching publications may rank above a general-purpose code, but only when it also has substantive community adoption for that specific task (multiple independent applications, not just the introducing paper).

**Canonical vs. derivative.** When multiple repositories exist for the same code family (canonical flagship vs. newer branch, institutional source vs. community mirror), prefer the canonical/flagship distribution — even if it lives on a project website. Newer branches or forks under 2 years old with low independent citations do not displace the canonical code; list them as **Secondary URL** on the canonical entry rather than as separate top-6 entries.

**Displacement rule.** If candidates exceed 6, the top 6 by the criteria above remain; the rest go to **Excluded Candidates** with a permitted reason. A candidate with ASCL `used_in` evidence or ADS-verified published usage for the user's specific task displaces a candidate with no demonstrated usage for that task, subject to the broad-query rule. Earlier discovery does not confer priority. Do not penalize a code for being a mirror, fork, or non-GitHub-hosted.

### Step 8 — Composition

Compose the Markdown output per the format in `output.md`. Surface per-repository evidence in the entry bullets, and surface uncertainty, assumptions, conflicting signals, and overall ASCL/ADS findings (including absence of citations) in **Search Notes**.

## 3. Clarification vs. Autonomy

- Detect ambiguity in Step 1. If it materially affects relevance, **ask before searching**.
- If the user declines to clarify, **proceed with conservative assumptions and disclose them** in the output.
- Non-blocking ambiguity does not stop the pipeline; assumptions applied during ranking are surfaced in **Search Notes**.

## 4. Tool-Selection Strategy (by step and domain)

- `repository_search_tool` — primary discovery, every domain, Step 2 (≥ 2 distinct query strings; may be batched via `queries=[...]`).
- `sde_search_tool` — one enrichment query, Step 3; strongest for Earth Science, Heliophysics, Planetary Science; low-yield for Astrophysics.
- `code_signals_search_tool` — conditional, Step 4, only when README + SDE context are insufficient.
- `ascl_search_tool`, `ads_search_tool`, `ads_links_resolver_tool` — Astrophysics only, Step 5 (max 4 ASCL, max 4 ADS, max 4 resolver uses).
- web search — supplementary, Step 6 only (max 3 queries); externally sourced repositories flagged in **Provenance**.

Per-tool interface detail is in `tools/`; per-domain channel strategy is in `contexts/<domain>.md`.

## 5. Uncertainty, Escalation & Abstention

- Explicitly disclose uncertainty, assumptions, limitations, and conflicts (in **Search Notes** and per-repository **Fit notes & limitations**).
- Evidence from one trusted channel (NASA corpus, ASCL, ADS, SDE, or verified web) is sufficient to retain a candidate; do not drop a candidate because it was absent from another channel.
- **Abstain (return zero repositories) ONLY when no channel yields any plausible candidate.** If candidates were found, include them with caveats — never silently omit. When abstaining, still emit the `## Ranked Repositories` heading with a short paragraph explaining what was searched and why nothing was located.
- Dual-use or sensitive domains may be surfaced only with explicit caution (see `guardrails/dual-use-caution.md`).
