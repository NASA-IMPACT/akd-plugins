# astroquery-mcp — Input / Output

The agent plans a call (module_name + function_name + params), optionally introspects to confirm
it, then runs it. Search is read-only.

## Tools & inputs

| Tool | Inputs | Use |
|---|---|---|
| `astroquery_execute` | `module_name` (e.g. `mast`, `heasarc`, `irsa`, `simbad`, `nea`), `function_name` (e.g. `query_region`, `query_object`, `query_tap`), `params` (dict), `max_rows` (default 20) | Run any astroquery function — the primary search path. |
| `astroquery_list_modules` | — | List the 14 modules and availability. |
| `astroquery_list_functions` | `module_name` (optional) | List a module's functions. |
| `astroquery_get_function_info` | `module_name`, `function_name` | Parameter signature + docstring for a function. |
| `astroquery_check_auth` | — | Which downstream services are authenticated (e.g. ADS, MAST). |
| `ads_query_compact` | `query_string`, `fields`, `max_results`, `sort` | Token-efficient ADS search. |
| `ads_get_paper` | `bibcode`, `include_abstract` | Full details for one ADS paper. |

Parameter conversion is automatic (e.g. object name / coordinate strings → `SkyCoord`; units).
Region searches take coordinates + radius (cone); TAP/ADQL runs via a module's `query_tap`.

## Outputs

`astroquery_execute` returns the astroquery result serialized to JSON (Astropy Tables → rows +
column metadata). From these, the agent assembles per-candidate normalized records (minimum
fields):

- `archive` / `collection_or_mission` / `instrument`
- `dataproduct_type` in IVOA nomenclature (image | cube | spectrum | timeseries | event |
  catalog | other)
- `access_url`, `landing_url`
- `obsid_or_equivalent`, `obs_publisher_did`
- `time_start`, `time_end`, `exposure_time_s`, `calib_level`, `proprietary_until`
- provenance: module/function/params (and ADS bibcodes for literature-driven runs)

**Missing values are marked, never fabricated** (`../../guardrails/no-fabrication.md`). The full
candidate-record and provenance schema is in `../../output.md`.
