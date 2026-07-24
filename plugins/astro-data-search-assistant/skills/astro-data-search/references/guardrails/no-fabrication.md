# No Fabrication

The planner must **never** guess or invent:
- Critical metadata — observation times, exposure, calibration level, proprietary dates.
- Endpoints — service endpoints must come from **Registry results or explicit config**, never
  filled in by guessing.
- Repositories, identifiers, or capabilities.

Missing critical values are marked `missing` (or the record is filtered with a user
notification, per `../reasoning.md`) — never fabricated. Relative time windows are converted to
explicit ISO-8601 and **verified with the user before proceeding**.
