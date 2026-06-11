# Earthdata Search / Landing Pages (handoff)

## Name
Earthdata Search / dataset landing pages (handoff links)

## Purpose
Dataset and granule discovery *handoff* for users who want to go beyond visualization and proceed to discovery for download.

## Agent behavior (as described)
- Generate smart links and landing page links
- Pass through:
  - Dataset ID
  - Spatial filters
  - Temporal filters

## Explicitly out of scope (as described)
- Automated download
- Subsetting execution
- Harmony workflows
- OPeNDAP calls

## Permissions / auth model
Public-only; authenticated workflows are out of scope.

## Open questions
- TBD: preferred Earthdata Search URL patterns for dataset + spatial + temporal parameters
- TBD: whether “Dataset ID” here is CMR concept-id, DOI, short-name/version, or Earthdata Search collection id
