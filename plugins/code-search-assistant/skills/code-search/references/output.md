# Output Format

This is the OUTPUT FORMAT contract, preserved verbatim from the source prompt. The agent produces a single self-contained Markdown document; the exact headings and bullet labels are load-bearing because the downstream UI renders them directly.

## No Final Recommendations

Outputs are comparative only, never prescriptive. The agent must never provide final recommendations or endorsements. Do not use language such as "best", "recommended", "final choice", "approved", or "use this". (See `guardrails/non-prescriptive-language.md`.)

## Document Contract (verbatim)

Return a single Markdown document (not JSON, not a fenced code block wrapping the whole response). The Markdown is rendered directly in the downstream UI and must be self-contained.

The document MUST contain the sections below in this order, using these exact headings.

### `## Ranked Repositories` (mandatory)

Zero to six entries, ordered by ranking position (1 = best match). Use `### {position}. {name}` followed by the bullets shown in the example below. The **ADS Evidence** block is populated only for Astrophysics queries; for other domains, replace it with a single line: `- **ADS Evidence:** N/A (non-Astrophysics query)`.

Example entry:

```
### 1. FLASH

- **Primary URL:** [https://flash.rochester.edu/site/](https://flash.rochester.edu/site/)
- **Secondary URL:** —
- **Rationale for inclusion:** Flagship adaptive-mesh hydrodynamics code with extensive astrophysics module suite; surfaced via ASCL and corroborated through NASA corpus and ADS comparison papers.
- **Fit notes & limitations:** Distributed via official project website (no public Git repository); access requires a request form, but the landing page itself is public.
- **Provenance:** ASCL, NASA Repository Search, External Web Search
- **ADS Evidence:**
  - Describing bibcodes: 2010ascl.soft10082F, 2000ApJS..131..273F, 2005Ap&SS.298..341W
  - Using bibcodes: 2018ApJ...854...63T, 2019MNRAS.485.4754F
  - Citation count: ~2100
  - Usage summary: Widely used for supernova, stellar-explosion, and ISM-turbulence simulations across the astrophysics community.
```

**Bullet semantics (only the non-obvious ones):**
- `Primary URL` — the chosen code-site URL, picked using the URL priority in CONSTRAINTS. Render as a Markdown link.
- `Secondary URL` — alternative host for the **same** codebase (e.g., a GitHub mirror of a project site, or vice versa), or `—` if none. MUST NOT be a successor project, fork, rewrite, or different code family (for FLASH, do not use Flash-X).
- `Describing bibcodes` — papers that DESCRIBE or INTRODUCE the code. Order: ASCL record bibcode first, then canonical method paper, then other description papers chronologically.
- `Using bibcodes` — 1–3 highly-cited papers that USE the code, preferring relevance to the user's queried task. Only include papers that apply the code, not papers that merely cite it in passing.
- `Citation count` — total citations from ADS evidence (ASCL `used_in_count` + ADS-discovered citing papers).

If zero candidates were found across all discovery steps, still emit the `## Ranked Repositories` heading followed by a short paragraph explaining what was searched and why no candidates were located.

### `## Excluded Candidates` (mandatory when applicable)

One bullet per excluded candidate: `- **{name}** — {reason}`. The reason must be permitted per the Step 6 list. Omit the section if no candidates were excluded.

### `## Well-known Codes Not Located` (mandatory when applicable)

One bullet per Expected Codes checklist item that could not be located through any channel: `- **{name}** — {note}`. Omit the section if all checklist codes were located.

### `## Search Notes` (mandatory)

A brief, readable summary covering: evidence used and confidence levels, conflicting signals, assumptions applied during ranking, and overall ASCL/ADS findings (including absence of citations). A few bullets or a short paragraph — do not restate per-repository detail.

## Formatting Rules

- Markdown only; no JSON anywhere in the response.
- Do not wrap the entire document in a fenced code block.
- URLs as Markdown links.
- Use the exact headings and bullet labels specified above so the UI renders consistently.
