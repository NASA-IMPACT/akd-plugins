# Supported Archives Only

The agent queries only the public astronomical archives exposed by the `astroquery-mcp` server —
the supported modules — and only their **publicly available** holdings. It must not target
arbitrary, private, gated, or credential-restricted sources.

**Supported modules (in scope), queried via `astroquery_execute`:**

- **NASA:** MAST, MAST Catalogs, HEASARC, IRSA, NASA Exoplanet Archive (NEA), NED, ADS.
- **ESA:** Gaia, ESA Hubble, ESA JWST.
- **CDS:** SIMBAD, VizieR.
- **Community:** SDSS, ALMA.

All fourteen are in scope. Route by band / mission / instrument (see
`../contexts/operational-policies.md`); MAST, HEASARC, and IRSA remain the primary NASA
repositories, with the ESA/CDS/community modules used when they fit the query.

- Responses are limited to publicly available information in these archives.
- Endpoints come from the server's configured services or Registry results — never guessed
  (see `no-fabrication.md`).
- VO Registry discovery is user-gated; only use services the `astroquery-mcp` server actually
  supports.

If Registry discovery returns a service beyond the supported modules: **skip by default**. The agent may optionally surface it as an **"out-of-scope suggestion"**, but must **not** query it without explicit user approval.
