# Existing systems & data inventory

This agent is intended to run as a standalone requirements interview experience. The primary “inputs” are human-provided answers and any user-uploaded reference materials.

## Tool / API inventory
- None. The agent will not connect to any external tools/APIs/integrations.

## Dataset / knowledge source inventory
- No built-in/required context sources.
- Optional: users may upload any reference materials they have to support answering questions.
  - Preferred formats: PDF, DOCX, PPTX
  - Other allowed formats: TBD
  - Restrictions (size, sensitivity, retention): TBD
- User-provided information during the interview (free-form answers).

## Schemas, access patterns, and documentation
- No existing schemas/data models identified yet.
- Documentation sources: TBD (e.g., internal wiki pages, past scoping docs, templates).

## Permissions, limits, and operational constraints
- Visibility:
  - Uploaded files: only visible to the uploading user.
  - Final scoping document: visible to the user, and shareable with others at the user’s discretion.
- Retention requirements: TBD
- Sensitive data / PII rules: TBD
- Size limits / quotas: TBD

## Known error patterns / failure modes
- TBD

## Open questions / unknowns
- What platform will host the agent (web app, chat, internal portal)?
- Upload handling details: storage location, supported file types beyond PDF/DOCX/PPTX, size limits, retention policy.
- Sensitive data policy (e.g., whether PII or confidential materials are allowed).
