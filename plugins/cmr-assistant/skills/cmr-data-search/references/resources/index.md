# Resources

Reference files the agent may consult verbatim. Kept minimal.

- `gcmd-science-keywords.json` — the **GCMD Science Keywords** controlled-vocabulary snapshot
  (NASA GCMD KMS, Science Keywords concept scheme, version **22.6**, ~3,670 concepts). The agent
  uses it to normalize the user's phenomena/variables into canonical GCMD keywords during the
  Term-normalization step before querying CMR. Usage and refresh notes are in
  `../contexts/gcmd-keywords.md`.
