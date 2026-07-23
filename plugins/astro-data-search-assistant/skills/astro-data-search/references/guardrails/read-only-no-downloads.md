# Read-Only, No Downloads

The agent runs **read-only** searches by calling `astro_search_tool`. Search and metadata
retrieval are permitted; changing or fetching bulk data is not.

The agent must **never**:
- Download data or define download scope.
- Write download scripts or automated mirroring instructions.
- Mutate any external system (search is read-only; results are metadata + access URLs only).

It returns **access URLs and identifiers** so the user can retrieve data themselves, outside
this agent. Applies to every step.
