# Earth Science Domains & Query Interpretation

Defines the in-scope domains and how to decompose a science query. Used during **Interpret** and
**synonym expansion** in the reasoning loop.

## In-scope domains

The agent only handles Earth science. Anything outside these is out of scope → say you cannot
help and stop.

- **Atmosphere** — temperature, precipitation, aerosols, clouds, trace gases, winds.
- **Ocean** — sea surface temperature, salinity, sea level, ocean color, currents.
- **Land** — land cover/use, vegetation, soil moisture, surface reflectance, fires.
- **Cryosphere** — sea ice, ice sheets, glaciers, snow cover, permafrost.
- **Biosphere** — vegetation indices, primary productivity, carbon flux, ecosystems.
- **Solid Earth** — topography, gravity, seismicity, volcanism, geodesy.

## Decomposing a query

Every query is interpreted into two things, without assumptions:

1. **Phenomenon** — the main topic the user cares about (e.g. "drought", "harmful algal
   blooms", "urban heat").
2. **Variables** — the measurable quantities that describe or drive the phenomenon (e.g. soil
   moisture, precipitation, land surface temperature, chlorophyll-a).

Distinguish:
- **Direct variables** — measurable quantities that directly represent the phenomenon.
- **Indirect variables** — quantities that scientifically influence the phenomenon, used only in
  the user-gated multi-hop loop (see `../reasoning.md`).

## Synonym expansion

Offer discipline-appropriate synonyms as **candidate terms only** to improve keyword
normalization — never as confirmed facts. Example: "sea surface temperature" ↔ "SST";
"vegetation greenness" ↔ "NDVI" / "EVI". Candidates are confirmed by the user or resolved
against the GCMD vocabulary before use.

## Mapping to controlled vocabulary

Confirmed phenomena and variables are normalized to canonical **GCMD Science Keywords** (and any
named platforms/instruments to their GCMD forms) before being translated into CMR query
parameters. The vocabulary is the bundled snapshot — see
[`gcmd-keywords.md`](gcmd-keywords.md).
