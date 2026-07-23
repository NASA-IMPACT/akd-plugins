# Human-in-the-Loop Gates

The agent must halt and wait unless the user explicitly confirms:
- Spatial constraints
- Temporal constraints
- Acceptance of indirect (multi-hop) inference

Clarifications are:
- **Blocking** — no search proceeds until they are answered.
- **Batched** — at most 5 questions per pause.
- Answerable with "No" so the user can proceed without a given constraint.

**Repeated ambiguity:** after two consecutive clarification cycles on the same ambiguity, ask
the user whether to refine scope, reset, or stop.

**Escalate or pause when:** required confirmations are denied or unresolved; repeated
zero/near-zero result searches occur; user confusion suggests misuse; or a human-subjects or
out-of-scope request arises (see `human-subjects-lock.md`, `earth-science-only.md`). When
blocked, emit the degraded/stop output verbatim (see `../output.md`) and halt.
