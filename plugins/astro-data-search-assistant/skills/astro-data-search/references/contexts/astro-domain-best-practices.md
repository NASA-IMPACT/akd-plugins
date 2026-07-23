# Astronomy Data: Search Best Practices

Background for classifying requests and choosing archives, products, and query patterns.

## The four data types (drives search strategy)

Treat "find me data" as underspecified until you know which of these the user needs (and whether
raw vs reduced/calibrated):

- **Images**
- **Spectra**
- **Data cubes** (e.g., IFS)
- **Catalog / table data**

Map the request to the downstream measurement intent, which tells you the product type:
positions/astrometry, flux/magnitude/photometry, spectral lines/continuum/spectroscopy, or
population/statistical work (catalogs). Brightness is constrained by instrument
bandpasses/filters, so wavelength coverage is intrinsic to interpreting results.

## Minimum metadata to collect or infer for any search

- **Target definition:** object name *or* sky position (RA/Dec) + **search radius**.
- **Time window** (observation date or range).
- **Wavelength / band / filter** (or energy range).
- **Instrument constraints** (if any).
- **Product level:** raw vs calibrated/reduced; single exposure vs mosaic; image vs catalog.

## Query-then-download mindset

Modern surveys are too large to download wholesale. Default behavior is
**constrain → query → fetch minimal**, not "download everything." Outputs should carry
machine-usable access paths (URLs) for only the selected subset. Prefer analysis near the data
(archive-side compute) where possible.

## VO + ADQL

The Virtual Observatory standards and **ADQL** (SQL-like) are the lingua franca for querying
astronomical catalogs via **TAP** (Table Access Protocol). Maintain an internal mapping from user
intent → "catalog query" vs "image cutout" vs "spectral product retrieval." For catalog-like
tasks, generate ADQL constraints (cone searches, brightness cuts, object-class filters) and
return reproducible query text plus result identifiers.

## File formats

**FITS** is the ubiquitous container for images (and often spectra/tables). Prefer returning
FITS products, or clearly label formats. If the user asks for "images," clarify whether they
mean *science FITS* vs rendered PNG/JPEG previews.

## Data-quality caveats (surface these; filter on them where possible)

- **Instrumental effects & noise:** images reflect the PSF and multiple noise sources; cosmic
  rays matter for space telescopes. Include usability proxies (exposure time, observing mode,
  whether products are cosmic-ray cleaned / combined) when available.
- **Reduction steps are standard and must be tracked:** bias, dark, sky subtraction,
  flatfielding. Add a "calibration status" note to result summaries (raw vs reduced; which
  corrections applied). For photometry, prioritize calibrated products or warn when only raw
  frames are found.
- **Display choices are not science products:** brightness scaling and "false color" can
  mislead. Do not treat rendered/pretty images as quantitative data; label previews "for
  visualization only" unless derived directly from science arrays with known scaling.
