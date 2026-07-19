# Domain: Astrophysics

## Routing

Astrophysics is the only SMD division that runs the full discovery pipeline including the ASCL + ADS literature channels. Queries categorized (in Step 1) as Astrophysics — alone or alongside other domains — activate Step 5.

## Channels used

1. `repository_search_tool` — Step 2 primary discovery (≥ 2 distinct query strings; may be batched via `queries=[...]`).
2. `sde_search_tool` — Step 3, one brief query. **SDE is low-yield for Astrophysics** (community codes are documented outside NASA institutional channels), so keep to one query and rely on Step 5.
3. `code_signals_search_tool` — Step 4, conditional.
4. **`ascl_search_tool` (Step 5a), `ads_search_tool` (Step 5b), `ads_links_resolver_tool` (Step 5c)** — the highest-yield astrophysics channels; ASCL is code-first with canonical URLs and ADS bibcodes.
5. External web search — Step 6 completeness pass.

## Channel strategy

- ASCL is the highest-yield discovery channel; do not treat the running list as settled after the NASA corpus pass — ASCL and ADS routinely add or strengthen candidates that change the final ranking.
- Recover canonical method papers under-reported by ASCL via ADS title search (5b) or the links resolver (5c).
- ADS `citation_count` and ASCL `used_in_count` are the primary community-adoption signals for Step 7 ranking.

## Tool-call budget

Up to **16 total tool calls** (ASCL, ADS, and the resolver expand the discovery surface). Within that: max 4 ASCL, max 4 ADS, max 4 resolver uses, max 3 web queries. See `guardrails/max-6-minimum-0.md`.

## Expected Codes checklist

Generated at runtime by the agent (Step 1) from domain knowledge — 5–8 well-known, widely-cited codes covering different numerical approaches and subfields. No stored checklist exists; it is produced per query. See note in `contexts/index.md`.

## Tool availability

In the live runtime environment, the full Astrophysics toolchain is available and enabled: `ascl_search_tool`, `ads_search_tool`, and `ads_links_resolver_tool` are used in Steps 5a/5b/5c.
