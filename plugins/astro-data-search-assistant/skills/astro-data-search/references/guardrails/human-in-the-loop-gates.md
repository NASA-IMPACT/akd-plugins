# Human-in-the-Loop Gates

## Missing inputs → stop
If required inputs are missing, stop and ask the user for the minimum metadata needed to produce
a valid contract (Clarification Mode; see `../output.md`). Do not emit a contract until the
minimums are met.

## Scope-expansion gates (require user approval before)
- Adding another archive beyond the initial plan.
- Adding/enabling **VO Registry discovery**.

On 0 results after must-have filters, the planner may propose next steps but must **not relax
filters automatically** — it asks the user for the relaxation order (expand radius vs broaden
time vs allow an adjacent product type), then emits a revised contract.

## Disambiguation
Provide the closest match and ask the user to confirm before proceeding (see
`ambiguous-identity-ask-user.md`).

## Review-required (bulk / large scope)
Trigger "stop + ask" only for genuinely bulk or abusive requests — broad all-sky areas, decade-plus
time ranges with no other constraint, large table dumps, or queries likely to return very large
result sets / heavy pagination.

There are no fixed numeric cut-offs; routine searches proceed, and provider-side throttling
handles out-of-bounds use. Large-but-legitimate queries are flagged as potentially slow (see
`alert-and-proprietary-labeling.md`), not blocked.

## Service failures
On repeated failures after retries (3–10 tries, exponential backoff), offer alternate archives
and/or ask the user to retry later; if unresolved, return an abstention status with an actionable
explanation of what failed and what is needed next.
