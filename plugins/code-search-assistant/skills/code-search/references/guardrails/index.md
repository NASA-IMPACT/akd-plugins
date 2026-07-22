# Guardrails

Safety, decision-boundary, and operational constraints for the Scientific Code Discovery Agent. Each rule below is preserved verbatim from the source prompt's CONSTRAINTS and Safety & abstention sections (SME-approved wording; never softened). One file per rule.

- `non-prescriptive-language.md` — Comparative-only outputs; never recommend, endorse, or use "best/recommended/final choice/approved/use this". Applies to all output.
- `popularity-signals-supporting-only.md` — Stars/forks are supporting only, never decisive in ranking. Applies in Step 7.
- `url-and-hosting-rules.md` — Valid-URL definition, ASCL-landing-page ban, URL priority order, and the permitted vs. non-permitted exclusion reasons. Applies to URL selection and exclusion decisions throughout.
- `read-only-no-execution.md` — No execution, cloning, downloading, testing, or code generation. Applies to every step.
- `no-fabrication.md` — No fabricated repositories, metadata, or capabilities. Applies to every step.
- `no-private-or-gated-sources.md` — No private, gated, or credential-restricted sources; an access gate on an otherwise public landing page does not make it private. Applies during discovery and inclusion.
- `retention-across-channels.md` — One trusted channel's evidence is sufficient to retain a candidate; do not drop for absence from another channel. Applies across Steps 2–6.
- `abstention.md` — Abstain (zero repositories) only when no channel yields any plausible candidate; otherwise include with caveats, never silently omit. Applies at Step 7/Step 8.
- `dual-use-caution.md` — Dual-use or sensitive domains surfaced only with explicit caution. Applies when the query touches sensitive domains.
- `max-6-minimum-0.md` — Maximum 6 / minimum 0 repositories, plus the 10 non-Astro / 16 Astro tool-call budgets. Operational limits across the pipeline.
