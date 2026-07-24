# Controlled Vocabularies & Reference Lists

Reference sources the planner uses for acronym expansion, topic normalization, and routing.

## Vocabularies

- **Unified Astronomy Thesaurus (UAT)** — normalize science topics/keywords.
- **NASA SCaN acronyms list** — expand mission/instrument acronyms.

## Mission / instrument / platform lists (authoritative for routing)

Three flat lists, provided as JSON, treated as authoritative reference context for
routing/selection:

- `missions[]` — ideally with: archive (MAST/HEASARC/IRSA/VO), time_range, band,
  primary_products.
- `instruments[]` — ideally with: mission, band, dataproduct_types, common_modes.
- `platforms[]` / observatories — ideally with: agency, capabilities, active_years.

The agent can function without the enrichment fields, but they materially improve routing
quality.

> **Not yet supplied.** These reference files (the UAT subset, SCaN acronym list, and the
> missions/instruments/platforms JSON) are named by the design but have not been provided. When
> available, add them under a `resources/` folder and point to them here. Until then, the agent
> relies on live resolution (SIMBAD/ADS/Registry, via the search tool) and the user for
> mission/instrument hints.
