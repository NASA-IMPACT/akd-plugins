# Ambiguous Identity — Ask the User

If object resolution returns more than one plausible candidate (e.g. several SIMBAD matches),
the planner must **stop and ask the user** to choose. It must not auto-pick.

- Provide the closest match as a suggestion and request confirmation before proceeding.
- Multi-object ambiguity from literature extraction is handled the same way: stop and ask which
  object(s) to pursue.

Applies during name resolution and entity extraction.
