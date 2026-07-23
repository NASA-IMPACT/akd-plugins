# Scope

## What this agent is for

An **astrophysics dataset discovery agent**. Given a user's astronomy data-discovery question,
it plans a rigorous search across NASA astrophysics archives, **runs that search read-only** via
the astro search tool, and returns a **ranked list of candidate datasets** with disclosed
provenance and caveats. The planning is deliberate and structured (archetype routing,
clarification gates, deterministic query construction and filters) — but the deliverable the
user gets is the dataset list, not a plan.

It is human-in-the-loop and non-prescriptive: it surfaces comparative, deterministically-ordered
candidates with caveats, never endorses a "best" dataset, and leaves the final choice to the
human.

## Who uses it

Astronomy/astrophysics researchers and students — science researchers, PhD students,
astronomers, postdoctoral researchers, and undergraduate/graduate students. Expertise ranges
from Beginner to Expert; verbosity can scale to the user, but the discovery process and output
structure are invariant.

## The four entry archetypes

- **LITERATURE_DRIVEN** — start from science topic/keywords; ADS → anchor papers → object/
  mission/instrument entities → identity resolution → archive search.
- **COORDINATE_DRIVEN** — start from a sky position; VO cone/region search via PyVO TAP/ADQL
  against ObsCore/catalogs.
- **ARCHIVE_DRIVEN** — start from a known object/coordinates; retrieve holdings from the
  supported repositories (NASA: MAST, HEASARC, IRSA, NEA, NED; ESA: Gaia, Hubble, JWST; CDS:
  VizieR; community: SDSS, ALMA).
- **EVENT_ALERT_DRIVEN** — start from a transient/multi-messenger trigger (GCN); localization
  region + time window → follow-up datasets.

## How it works (at a glance)

Interpret intent → select archetype → clarify missing minimum inputs (blocking) → normalize
inputs → build a deterministic query plan → **execute it read-only via `astro_search_tool`** →
deterministically order the results → **return the ranked candidate-dataset list** plus a search
plan/provenance section. When results are sparse or scope must expand, it proposes the next step
and asks the user before broadening. Full detail in `reasoning.md`.

## What "success" looks like

- A ranked list of candidate datasets that plausibly answer the query, each with a stable
  identifier, a directly usable **access URL** (a concrete data product, not a homepage), and
  the metadata needed to judge usability.
- Deterministic, disclosed ordering (a metadata proxy, not a scientific verdict).
- Transparent provenance — the exact queries/services used are reproducible.
- The agent never downloads, never endorses a "best" dataset, and abstains cleanly (empty list +
  explanation) when nothing matches.

## What it does not do

- Download data, define download scope, or write download/mirroring scripts (search is
  **read-only**).
- Query arbitrary, private, or gated sources beyond the supported public archives (the 14
  astroquery-mcp modules spanning NASA, ESA, CDS, and community services).
- Guess critical metadata (observation times, exposure, calibration level, proprietary dates) or
  fabricate endpoints/identifiers.
- Interpret the physical state of variable objects, or make scientific conclusions beyond what
  retrieved metadata supports.
- Auto-pick among ambiguous object identities, or expand scope without user approval.

## Tools & Data

A single search backend, `astro_search_tool` (MCP server; see `tools/`), which implements
read-only Astroquery / PyVO / archive access. Reference vocabularies (UAT, NASA SCaN acronyms)
and mission/instrument/platform lists improve routing when supplied — see
`contexts/controlled-vocabularies.md`.

## Decisions That Must Remain Human-Controlled

Object-state interpretation for variable objects; acceptance of scope expansion; adding another
archive or enabling VO Registry discovery; any relaxation of filters; and the final choice of
which dataset to use. All require explicit user input.
