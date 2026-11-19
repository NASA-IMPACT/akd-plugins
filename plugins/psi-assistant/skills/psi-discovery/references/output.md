# Output format specification (draft)

## SME-validated decisions
- Output style: hybrid (adaptive to user need)
  - Narrative summaries when user asks for summary
  - Tables for comparisons when user asks for comparison table
  - Lists where appropriate
  - Requirement: adapt format to the user’s request
  - Status: confirmed
  - TBD: SME identity, timestamp, source reference

- Provenance & citations: required
  - Requirement: include citations/provenance so users can find sources for deeper dives
  - Motivation: reduce hallucination risk; ensure traceability
  - Status: confirmed
  - TBD: exact citation format (inline vs footnote), required citation fields

- Uncertainty / conflicts: must be surfaced + require human validation
  - Requirement: when the agent must infer, it should present assumptions, uncertainties, and conflicts explicitly
  - Requirement: for conflicts, ask the human to validate/select the best option; do not silently proceed
  - Status: confirmed
  - TBD: exact fields/labels for assumptions/uncertainties/conflicts; how to present “options” for selection

- Context source disclosure
  - Requirement: for tables/figures, include context source pointers with exact path to the source (e.g., `context/...` path) so users can deep-dive
  - Requirement: for other output types, context sources should be available as an option users can request
  - Status: confirmed
  - TBD: what the “option” looks like in output (toggle/field/section)

- Tool guidance: include follow-up actions
  - Requirement: include tool-driven next actions / follow-up actions in outputs
  - Status: confirmed
  - TBD: standardized fields for next actions (e.g., `next_action`, `next_action_params`, `alternative_actions`, `recovery_options`)

- Execution / intermediate status visibility
  - Requirement: present final results by default; show intermediate steps/status only if the user asks
  - Status: confirmed
  - TBD: where intermediate/status fields live when requested (separate section vs separate output mode)

- Intermediate status / tool execution details
  - Requirement: default to final results only
  - Requirement: include intermediate steps/status fields only when user asks
  - Status: confirmed

## Structured output template (TBD)
TBD: canonical hybrid output envelope (user-facing + provenance + tool guidance + recovery fields).

## Output consumers
- Single primary output variant (no separate consumer-specific variants required)
  - Status: confirmed
