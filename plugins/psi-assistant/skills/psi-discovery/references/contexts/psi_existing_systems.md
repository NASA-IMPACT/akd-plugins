# Existing systems & data inventory (draft)

## Tool / API inventory
### PSI Public Investigations API
- Owner: PSI Data System Team
- Purpose: public API for investigation discovery (metadata), file enumeration/search, and file retrieval (via S3-backed URLs)
- Current users/consumers: external users (primary); likely programmatic integrations
- Access method: REST over HTTPS
- Auth model: no authentication (public)
- Key endpoints
  - `GET /api/investigations/metadata`
    - Purpose: list all public investigations
    - Known output fields: title, objective, accession ID
    - Schema/docs: partial / not fully documented
  - `GET /api/investigations/files/search/{INVESTIGATION_IDs}`
    - Inputs
      - `INVESTIGATION_IDs` (required): comma-separated IDs and/or ranges
      - `page` (optional; starts at 0)
      - `size` (optional; max 25)
      - `type` (optional: img, video)
    - Response schema (confirmed)
      - `hits`, `input`, `page_number`, `page_size`, `page_total`, `success`, `total_hits`, `valid_input`
      - `studies`: mapping of `PSI-XXX` → `{ file_count, study_files[] }`
    - File object schema (complete)
      - `category`, `subcategory`, `subdirectory`, `organization`, `file_name`, `file_size`, `remote_url`, `restricted`, `visible`, `date_created`, `date_updated`
  - `GET /api/investigations/{INVESTIGATION_ID}/download`
    - Inputs: `source`, `file`
    - Output: file download (S3-backed access)
- Operational constraints / quirks
  - Pagination: page index starts at 0; max page size = 25; `page_total` provided
  - Hierarchy reconstruction relies on `category` + `subcategory` + `subdirectory`
  - Migration constraint: path transition `geode-py/ws/` → `psi/data/` (requires config switch or fallback logic client-side)
  - Performance: timeouts for very large investigations (>10,000 files), affecting ~1–2 investigations; known issue under remediation

### DataCite REST API (external)
- Owner: DataCite (external)
- Purpose: DOI → publication metadata resolution
- Access method: REST API
- Current usage fields: title, authors, year, publisher
- Planned expansion: additional metadata fields (TBD)
- Unknowns: exact endpoint used; rate limits; error handling patterns

## Dataset / knowledge source inventory
### PSI Investigation dataset (via PSI Public Investigations API)
- Type: structured dataset accessed via API
- Structure: investigation → `studies` → `study_files[]`
- File organization fields: `category`, `subcategory`, `subdirectory`
- Identifiers: PSI IDs (e.g., `PSI-190`)

### Legacy data segment (subset of PSI Investigation dataset)
- Identification heuristic: `subdirectory` starts with `/legacy/`
- Scale: ~60% of total dataset
- Known issues: high incidence of missing files (HTTP 404) due to missing objects in S3

### Storage layer (S3 backend behind PSI API)
- Role: file hosting behind API
- Access pattern: API returns `remote_url` → client downloads
- URL behavior: signed URLs expire after ~7 days (requires regeneration via API)

### Investigation-level documents present as files (examples from uploaded PSI investigation materials)
> Note: these appear to be *file types within the PSI investigation file corpus* (i.e., accessed via the PSI API’s file listing + `remote_url`), not separate external systems.

- Investigation metadata text file (example: `resources/i_Investigation.txt`)
  - Appears to be a structured, tabular “INVESTIGATION / STUDY” record including fields for identifiers, title, objective, hypothesis, contacts, publications (DOIs), design descriptors, etc.
  - Includes an “Ontology Source Reference” section (e.g., PSI + EFO).
- Science Requirements / Science Review Document (SRD) PDF (example: `resources/SRD_SUBSA-CETSOL.pdf`)
  - Investigation background, objectives, science requirements, procedures, data handling.
- Experimental table / sample matrix (example: `resources/Experimental Table_Famis.csv`)
  - Structured CSV describing per-sample composition and processing parameters.
- Data Layout Document (ReadMe / DLD) PDF (example: `resources/ReadMe_SUBSA_CETSOL.pdf`)
  - Describes curated folder structure, analyzed vs raw data locations, documentation folders.
- Dissertation / thesis PDF (example: `resources/2021 - Lazaridis, Kostis - PhD Dissertation.pdf`)
  - Deep-dive background, methods, modeling, analysis; long-form PDF.

### File-type visibility
- PSI file listings include `file_name`, so file extensions (e.g., `.pdf`, `.csv`, `.txt`) are derivable from the listing itself.

## Schemas, access patterns, and documentation
- Canonical access flow
  1. Call `GET /api/investigations/metadata` to retrieve investigations
  2. Select investigation ID(s)
  3. Call `GET /api/investigations/files/search/{INVESTIGATION_IDs}` (paginated)
  4. Extract `remote_url`
  5. Call `GET /api/investigations/{INVESTIGATION_ID}/download` to retrieve file
- Known schema gaps
  - Full schema for `GET /api/investigations/metadata` beyond title/objective/accession ID is TBD
  - Error response schema/body format is TBD
  - How to reliably identify common document types (SRD, final report, experimental table, DLD/readme, dissertation/thesis, metadata txt) from the file listing via naming conventions and/or `category`/`subcategory`/`subdirectory` patterns is TBD

## Permissions, limits, and operational constraints
- Authentication: none (public)
- Pagination limit: max `size` = 25
- Signed URL expiration: ~7 days (signed S3 URLs; regeneration via API required)
- Performance: possible timeouts for investigations with >10k files (limited to ~1–2 investigations); known issue actively being addressed
- Migration risk: endpoint path transition `geode-py/ws/` → `psi/data/` may cause temporary mismatches/failures

## Known error patterns / failure modes
- Missing files (legacy data): HTTP 404 due to missing S3 objects; legacy subset identified by `/legacy/` prefix
- Expired URLs: signed `remote_url` expiry (~7 days) invalidates previously retrieved links; requires re-query
- Timeouts: large investigations (>10k files); under remediation
- Migration instability: potential temporary failures/mismatches during path transition

## Open questions / unknowns
- PSI Public Investigations API
  - Full schema for `GET /api/investigations/metadata` beyond title/objective/accession ID
  - Standard error response schema(s) for failures (4xx/5xx)
  - Any published OpenAPI/Swagger spec and where it lives
  - Retry/backoff expectations (TBD)
  - Any IP-based throttling / rate limits / request size limits (TBD / not documented)
  - How to identify common investigation-level documents in the file listing (naming conventions and/or `category`/`subcategory`/`subdirectory` patterns)
    - Investigation metadata text file
    - SRD / science review or requirements document
    - Experimental table / sample matrix
    - Final report
    - ReadMe / Data Layout Document (DLD)
    - Dissertation / thesis
  - Storage layer behaviors
    - Whether signed URLs are always regenerated dynamically (TBD)
    - Whether any files are archived vs permanently missing (TBD)
  - Data governance/operations
    - Data ingestion / ETL pipeline details (TBD)
    - Validation process for legacy vs non-legacy data (TBD)
- DataCite REST API
  - Exact endpoint(s) used and response fields consumed
  - Rate limits and error handling patterns in practice
- Other knowledge sources (mentioned but availability/location TBD)
  - Any campaign-level corpora (e.g., “RSD-AFF” campaign materials)
  - Any domain-science reference paper corpora (e.g., boiling references)
