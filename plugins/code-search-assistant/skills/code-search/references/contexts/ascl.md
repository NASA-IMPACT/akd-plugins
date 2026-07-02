# Context: Astrophysics Source Code Library (ASCL)

## What it is

The Astrophysics Source Code Library (ASCL) is a code-first registry of astrophysics software. Every entry is a code with a canonical URL and ADS bibcodes for its description and usage papers. It is the highest-yield channel for astrophysics code discovery.

## Astrophysics-only channel

ASCL is used **only for Astrophysics queries** (Step 5a). It is skipped entirely for non-Astrophysics queries.

## Record structure the agent relies on

- `site_list` — URLs for the code; **not pre-prioritized**. Pick the best using the URL priority in `guardrails/url-and-hosting-rules.md`.
- `described_in` and `used_in` — both returned as **ADS URLs**, not raw bibcodes; recover the bibcode by parsing the path segment after `/abs/`.
- `bibcode` — the ASCL record's own bibcode (e.g., `2010ascl.soft10082F` for FLASH); used as the input to `ads_links_resolver_tool` in Step 5c.
- `used_in_count` — an adoption signal used in Step 7 ranking.

## Known limitation (drives Steps 5b/5c)

ASCL's `described_in` is often incomplete: for well-known codes it may list only a low-citation update paper instead of the canonical, highly-cited method paper. The canonical method paper MUST appear in a candidate's **Describing bibcodes**; recover it via an ADS title search (Step 5b) or the ADS links resolver (Step 5c). Parse ALL bibcodes from `described_in`, not just the first.

## Constraint

Never use the ASCL landing page (`ascl.net/<id>`) as a code URL.

## Related tool

`tools/ascl_search_tool/`.
