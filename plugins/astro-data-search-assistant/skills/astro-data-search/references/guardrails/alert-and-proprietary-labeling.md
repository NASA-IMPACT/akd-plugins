# Alert & Proprietary Labeling

## Alert / localization uncertainty
Always label alert/localization products (GCN-derived) **"best-available / uncertain."** Never
present them as final/verified unless authoritative metadata explicitly confirms finality.

## Proprietary data
Proprietary datasets may be surfaced (do not filter them out), but must be labeled
**"proprietary until DATE"** when known, down-ranked (public-first), and never described in a way
that implies access or entitlement.

## Heavy / broad queries
Broad ADQL or enumerations are allowed but must be clearly labeled as potentially slow or
provider-limited (service-side throttling is assumed to apply). Pair with the review-required
gate in `human-in-the-loop-gates.md`.
