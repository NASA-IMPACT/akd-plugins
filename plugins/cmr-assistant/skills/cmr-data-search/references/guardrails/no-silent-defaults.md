# No Silent Defaults

The agent **may infer** sensible defaults internally — spatial → Global; temporal → current
year/month — but must **never apply them silently**.

- Inference is allowed; **execution is gated**. The agent pauses and requests approval before
  executing any search that relies on a default.
- Keywords, variables, spatial bounds, and temporal bounds are never assumed on the user's
  behalf without confirmation.

Applies whenever a required constraint is absent. See `human-in-the-loop-gates.md`.
