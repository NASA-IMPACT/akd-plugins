# Abstention

## Rule (verbatim)

> Abstain (return zero repositories) ONLY when no channel yields any plausible candidate. If candidates were found, include them with caveats — never silently omit.

## Scope

Applies at Step 7 (Ranking) and Step 8 (Composition). Minimum 0 repositories is allowed, but abstention is reserved for the case where every discovery channel came up empty.

## Behavior

- If zero candidates were found across all discovery steps, still emit the `## Ranked Repositories` heading followed by a short paragraph explaining what was searched and why no candidates were located.

## Never Do

- Never abstain when at least one channel yielded a plausible candidate.
- Never silently omit a candidate that was found; include it with caveats instead.
