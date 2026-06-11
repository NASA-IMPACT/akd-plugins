# eonet_search_tool

## Purpose
Search NASA EONET v3 natural events to provide event context (geometry, time window, category, and links).

## When to use
When the user asks about a specific hazard/disaster event.

The agent may also call this tool proactively when the user describes a hazard/disaster scenario (e.g., fires, floods) even if they do not explicitly ask for “events”, if event context would help anchor a Worldview exploration.

## Inputs (schema)
`additionalProperties: false`

- `category`: enum (`drought` | `dustHaze` | `earthquakes` | `floods` | `landslides` | `manmade` | `seaLakeIce` | `severeStorms` | `snow` | `tempExtremes` | `volcanoes` | `waterColor` | `wildfires`) | null
- `status`: enum `open` (default) | `closed` | `all`
- `days`: int `1..365` | null (mutually exclusive with `start`/`end`)
- `start`: date | null (must be provided with `end`)
- `end`: date | null (must be provided with `start`)
- `bbox`: `[min_lon, min_lat, max_lon, max_lat]` | null
- `limit`: int `1..100` (default `10`)
- `magnitude_id`: string | null
- `magnitude_min`: number | null (requires `magnitude_id`)
- `magnitude_max`: number | null (requires `magnitude_id`)

## Outputs (schema)
- `results[]`
- `extra`

Each `results[]` item includes:
- `id`, `title`, `description`, `link`, `closed`
- `categories[]`, `sources[]`
- `geometry[]` (timestamped Point/Polygon + magnitude)
- derived `bbox` (`min_lon`, `min_lat`, `max_lon`, `max_lat`)
- `t_start`, `t_end`

## Validation & business rules
- `days` is mutually exclusive with `start`/`end`.
- `start` and `end` must be supplied together.
- `magnitude_min`/`magnitude_max` require `magnitude_id`.

## Failure modes and recovery guidance
TBD (confirm).

## Security / permissions
Public-only.

## Notes
- MCP server label: `eonet-tool`
- See `tools/mcp_config.json`.
