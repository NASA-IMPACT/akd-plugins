# URLs and Hosting Rules

## Rule (verbatim — stated once, applied throughout)

> - Public GitHub repositories are preferred when available.
> - A project-website URL, institutional download page, or other public hosting URL (GitLab, Bitbucket, `*.edu`, `*.gov`, `*.org`) is a **valid URL**. A code from the Expected Codes checklist must not be excluded solely because its URL points to a project website rather than a Git host. Note the URL type as a caveat in the output, not as grounds for exclusion.
> - An access gate on an otherwise public landing page (e.g., a request form) does NOT make the code private; the landing page itself is public and is a valid URL.
> - Never use the ASCL landing page (`ascl.net/<id>`) as a code URL.
> - **URL priority** when picking among multiple URLs for the same code: live Git host (GitHub > GitLab > Bitbucket) > Zenodo or DOI archive > official project website > documentation site.

## Permitted vs. non-permitted exclusion reasons (verbatim)

> The following reasons MUST NOT appear as exclusion grounds for any checklist item:
> - "URL points to a project website rather than GitHub/GitLab"
> - "URL is not a direct source repository link"
> - "Access requires a request form or institutional login"
> - "Repository is a mirror or fork"
> - "Could not fetch/verify URL from this environment"

> If a checklist item has any verified public URL of any type, it MUST appear in the ranked results — URL type is recorded as a caveat in **Fit notes & limitations**, not as exclusion grounds. Valid exclusion reasons are limited to:
> 1. The running list exceeds 6 and Step 7 displacement determines this code is weaker than six others (→ **Excluded Candidates**).
> 2. No public URL of any kind could be located after web search (→ **Well-known Codes Not Located**).

## Scope

Applies to URL selection (choosing the Primary/Secondary URL for each candidate) and to every exclusion decision throughout the pipeline. The accounting requirement in `reasoning.md` (Step 6) enforces that every checklist code is accounted for.

## Never Do

- Never use the ASCL landing page (`ascl.net/<id>`) as a code URL.
- Never exclude a checklist code solely because its URL is a project website, is not a direct source link, sits behind a request form / institutional login, is a mirror or fork, or could not be fetched/verified from this environment.
- Never penalize a code for being a mirror, fork, or non-GitHub-hosted.
