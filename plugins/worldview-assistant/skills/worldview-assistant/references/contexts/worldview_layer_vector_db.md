# Worldview Layer Vector DB (internal semantic index)

## Name
Worldview Layer Vector DB

## Purpose (as described)
Internal semantic index to support:
- Layer descriptions
- Intent-to-layer mapping
- Proxy detection
- Filling missing information (e.g., from NASA GIBS API)

## Authority model
Not authoritative for scientific claims; **CMR remains authoritative**.

## Access method
TBD (not specified).

## Data sources (as described)
- Worldview layer descriptions
- NASA GIBS API (for missing information)

## Open questions
- TBD: where this vector DB is hosted, how it’s queried, and response schema
- TBD: refresh cadence and how it stays in sync with Worldview layer config
- TBD: provenance fields (how we track what came from CMR vs inferred/derived)
