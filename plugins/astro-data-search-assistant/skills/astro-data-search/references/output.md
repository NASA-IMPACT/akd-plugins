# Output Format & Interaction Rules

Defines **when** the agent asks questions versus **when** it returns results. The agent operates
in **exactly one output mode per turn**.

## Output modes

### Clarification Mode
Activated when any minimum required input for the selected archetype is missing or ambiguous
(the hard gate in `reasoning.md`).
- Output **plain-text clarifying questions only**; **blocking**; directly tied to the missing
  minimum inputs; then **stop and wait**. Return no results.
- Not an error state.

### Results Mode
Activated when all minimum required inputs are present and the search has run. The agent returns:
1. A **ranked list of candidate datasets** (deterministically ordered), grouped per the
   archetype.
2. A **Search plan & provenance** section — the access paths, exact queries/ADQL, services/
   endpoints, ordering rationale, and any assumptions or scope decisions.

If the search ran but found nothing after must-have filters, return an empty candidate list with
a short explanation of what was searched and the proposed next step (scope expansion / relaxation
order) for the user to approve. If execution fails after retries, say so with the failure and the
next action needed.

> **Authoritative rule:** if you ask questions (Clarification Mode), do not return results; if
> you return results, do not also ask blocking questions.

## Ranked candidate datasets (primary deliverable)

Order candidates by the deterministic policy in `reasoning.md` — **product readiness → product
match → instrument/mode → public-first → exposure → quality** — with `calib_level = 0` excluded
unless the user requested it. Present them grouped per archetype (see grouping below). For each
candidate, surface:

- **archive / collection_or_mission / instrument**
- **dataproduct_type** in IVOA nomenclature (image | cube | spectrum | timeseries | event |
  catalog | other)
- **access_url** and **landing_url**
- **identifiers** — obsid_or_equivalent, obs_publisher_did
- **time_start / time_end / exposure_time_s / calib_level / proprietary_until**
- **caveats** — missing/uncertain fields, cross-archive conflicts (keep both, flag), and
  proprietary/alert labels

Missing values are marked, never fabricated. Use "candidate datasets", never "best dataset";
ordering/fitness is a metadata proxy, not a scientific conclusion.

**Candidate dataset record (Markdown template):**

Provide each candidate as a Markdown sub-section or bullet list, using the following fields (mark each field as `present | missing | inferred | ambiguous` and do not fabricate values):

- **record_id** — `sha256:DIGEST_HEX`
- **archive** — value + status
- **collection_or_mission** — value + status
- **instrument** — value + status
- **dataproduct_type** — `image | cube | spectrum | timeseries | event | catalog | other` + status
- **landing_url** — value + status
- **access_url** — value + status
- **identifiers**
  - **obsid_or_equivalent** — value + status
  - **obs_publisher_did** — value + status
- **time_start** — value + status
- **time_end** — value + status
- **exposure_time_s** — value + status
- **calib_level** — value + status
- **proprietary_until** — value + status
- **caveats** — bullet list of caveats

JSON is allowed **only** if the user explicitly asks for JSON. Otherwise, keep candidate records in Markdown.

**Grouping by archetype:**
- **LITERATURE_DRIVEN** — group `paper → object → facet_band → facet_instrument`; surface
  `anchor_papers[]` (bibcode/doi/title) and per-object `simbad_candidates[]` with
  `needs_user_choice` when identity is unresolved.
- **COORDINATE_DRIVEN** — group `facet_band → facet_instrument`; note the input region and the
  services/tables/ADQL queried.
- **ARCHIVE_DRIVEN** — group `facet_band → facet_instrument`; note archives queried.
- **EVENT_ALERT_DRIVEN** — group `time_window_label (prompt/early/late) → facet_band →
  facet_instrument`; note `event_id`, `alert_source`, `t0`, and region representation; label all
  alert/localization products "best-available / uncertain".

## Search plan & provenance (audit)

After the candidate list, include the plan that produced it — the internal query plan doubles as
reproducible provenance:

- **chosen_access_paths** — Astroquery module calls and/or PyVO service URLs, with the exact
  `call_text` (ADQL / method call / params) per call.
- **query_parameters** — targets/region, time_window, band_or_energy, product_type, constraints,
  row_limits.
- **verification_checks** — spatial/temporal overlap and product-readiness proxies, with results
  and gaps.
- **fallback_order** — the deterministic next steps (each marked whether it needs user approval).
- **audit** — environment (library versions), requests/retries, and the branching log.

JSON is allowed **only** if the user explicitly asks for JSON. Otherwise, keep the plan & provenance in Markdown.

If JSON is explicitly requested, any JSON representation of the plan must preserve exact `provenance[*].query_text`.

## Wording norms

- Use "candidate datasets", never "best dataset".
- State only what retrieved metadata supports; ordering/fitness is a **metadata proxy**.
- Label proprietary items "proprietary until DATE"; label alert/localization products
  "best-available / uncertain".
- Include provenance (bibcodes, queries, services/endpoints used).
