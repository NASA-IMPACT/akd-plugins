# Permissions, limits, and operational constraints

## Global scope constraints (as provided)
- Public-only datasets
- Visualization-first architecture
- Metadata-authoritative (UMM-based)
- No raw granule retrieval
- No server-side modeling
- No predictive analytics

## Operational constraints (as provided)
- Rate limits exist ("one query per second" noted)
- Avoid bulk tile iteration
- Monitor 429/503 responses
- Conservative throttling
- Max time series length: decision based on per-dataset constraints

## Known system constraints (as provided)
- Visualization and statistics are constrained by query parameter acceptable values in Worldview URL

## Explicitly out of scope (as reiterated)
- Raw granule retrieval
- Server-side modeling / prediction
- Persistent user profiling
- OPeNDAP workflows
- Authenticated workflows

## Open questions
- TBD: which services specifically enforce 1 QPS (CMR MCP? EONET? SDE?)
- TBD: any IP-based throttles, burst limits, or daily quotas
