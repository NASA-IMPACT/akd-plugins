# NASA Worldview

## Name
NASA Worldview

## Purpose
Primary visualization interface and deep-link target for exploring NASA Earth science imagery and layer-based analytics.

## When used
When the user wants to visualize layers, compare layers, explore time, or use Worldview-native charting/statistics.

## Access method
Web application (deep links / URL parameters).

## Key capabilities (as described)
- Layer rendering
- Layer comparison: Swipe / Spy / Opacity
- Charting mode
- Time selection
- Projection switching
- Deep link configuration

## Agent usage model (constraints)
- Generate Worldview deep links
- Mirror UI-supported configuration via URL parameters
- No direct UI automation

## Permissions / auth model
Public-only datasets; no authenticated workflows.

## Comparison mode support (as described)

| Mode | Same layer, different date | Different layers, same date |
|---|---:|---:|
| Swipe | Yes | Yes |
| Spy | Yes | Yes |
| Opacity | Yes | Yes |

## Limits / operational constraints (known)
- Avoid bulk tile iteration
- Visualization and statistics constrained by Worldview URL parameter acceptable values

## Docs
- URL parameter documentation (see `contexts/worldview_url_parameters.md`)

## Known failure patterns / unknowns
- TBD: base URL(s) and environment(s) (prod/stage)
- TBD: limits/validation behavior when URL parameters are malformed
