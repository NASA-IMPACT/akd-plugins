# Worldview URL Parameters (deep linking)

## Source documentation
https://github.com/nasa-gibs/worldview/blob/main/doc/url_parameters.md

## Purpose
Defines the query parameters the agent can use to construct Worldview deep links that reproduce UI state (projection, layers, time, compare mode, charting mode, etc.).

## Key parameters (SME-provided subset)

### View / projection
- `p`: projection (`geographic`, `arctic`, `antarctic`)
- `v`: viewport extent (`minX,minY,maxX,maxY`) in units of the projection
- `r`: rotation (only for arctic/antarctic)

### Layers
- `l` (`l1` for B state): active layer list (`layer_id1,layer_id2,...`)
  - layer modifiers supported in list:
    - `(hidden)`
    - `(opacity=value)` where value in `[0,1]`
    - `(palettes=...)`, `(squash)`, `(min=...)`, `(max=...)`
    - `(style=value)` for vector layers
- `lg` (`lg1`): layer grouping toggle

### Time / timeline
- `t` (`t1`): selected UTC time `YYYY-MM-DD-Thh:mm:ssZ`
- `z`: timescale axis zoom `1..5`
- `i`: timeline interval `1..5`
- Custom interval controls: `ics`, `ici`, `icd`

### Events
- `e`: activate events tab / highlight event
- `efs`: include bbox in events API call or not
- `efd`: event date range
- `efc`: event category ids

### Location marker
- `s`: coordinate pair(s) for marker(s) (decimal degrees)

### Animation
- `ab`: show animation widget
- `aa`: autoplay on load (requires valid animation params)
- `as`, `ae`: animation start/end
- `av`: speed `1..10`
- `al`: loop

### Compare mode
- `ca`: activates compare mode; indicates whether A state is active
- `cm`: `swipe` | `spy` | `opacity`
- `cv`: swiper location / opacity value (depends on `cm`)

### Charting mode
- `cha`: activate charting mode
- `chl`: selected layer for charting
- `chc`: AOI selection coordinates `x1,y1,x2,y2`
- `cht`, `cht2`: chart time range
- `chch`: request/show chart on load

### Download tab / embed / UI modes
- `download`: activate download tab / select product
- `df`: distraction free mode
- `em`: embed mode
- `tr`: tour/story id
- `abt`: about modal open

## Known constraints
- Worldview visualization/statistics are constrained to what URL parameters and allowed values support.

## Open questions
- TBD: canonical Worldview base URL for deep links to use
- TBD: how layer_id values are discovered/validated (config endpoint vs bundled config)
