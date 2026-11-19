# Context Manifest — `contexts/` folder

> **Plugin packaging note.** Only the text-based context files ship with this plugin:
> `psi_existing_systems.md`, `i_Investigation.txt`, `Experimental Table_Famis.csv`, and this
> index. The PDF entries below (investigation overviews, SRDs, ReadMe/Data Layout Documents,
> publications, dissertation) are **not bundled** — they are PSI-hosted documents from the
> design-time corpus. Treat their entries as routing knowledge about *which PSI documents to
> fetch for which task*: locate and retrieve them live from the corresponding investigation's
> file corpus via `psi_api_tool`, and cite the PSI source (investigation ID + file path/URL)
> instead of a local path.

## 0. How to use this index

Don't open the whole `contexts/` folder for every task. Identify what the task needs (which investigation? what kind of question?), find the matching entry below, open only that file, and cite it. If a task needs more than one file, open them in the order given in the entry's Triggers, not all at once.

The folder is currently **flat** — every file sits directly under `contexts/`, not nested in an intended `investigations/ / domain_science/ / campaigns/` hierarchy. Canonical paths below reflect the flat, real layout today. If the folder gets reorganized into a nested hierarchy later, update the paths in this file to match — the Purpose/Type/Triggers/Authority content doesn't need to change.

**Confidence flag on every entry:**
- **Confirmed** — purpose/triggers validated by SME notes and/or direct reading of the file.
- **Inferred** — purpose/triggers inferred from filename only; nobody has confirmed the actual content. Treat these cautiously and flag to the user if a task leans heavily on one.

---

## 1. Retrieval algorithm

1. **Scope the task first.** Does it concern RSD-AFF (amyloidogenesis / interfacial shear), SUBSA-CETSOL (solidification), or a general pool-boiling question with no specific investigation? Use Section 2 (Discovery & Routing) to figure this out if unclear.
2. **Match triggers, not topic words.** Find the entry in Sections 3–6 whose Triggers line up with the actual task, not just the one that sounds closest.
3. **Respect authority.** If two sources conflict, the one marked `Source of truth` in Section 8 wins over `Advisory`.
4. **Open the minimum set.** Publications and reference papers are advisory support — pull them only when the trigger genuinely calls for literature-level interpretation, not by default.
5. **Cite what was actually opened.** Since these are local files, name the file in the response so the user can trace the claim back.

---

## 2. Discovery, routing & systems-access contexts (read first, lightweight)

| File | Purpose | Type | Read when |
|---|---|---|---|
| `psi_existing_systems.md` | **Not** an investigation list — it's a systems/API inventory for the **PSI Public Investigations API** (public, unauthenticated REST): `GET /api/investigations/metadata` (list investigations), `GET /api/investigations/files/search/{IDs}` (paginated file search, max page size 25), `GET /api/investigations/{ID}/download` (S3-backed file retrieval), plus the DataCite REST API for DOI→publication metadata. Documents known failure modes: legacy data (~60% of the dataset, `subdirectory` starts with `/legacy/`) has a high rate of HTTP 404s; signed `remote_url`s expire after ~7 days and must be regenerated; investigations with >10k files can time out. | Structural | Before fetching investigation files/metadata **programmatically** rather than from the local `contexts/` corpus; when a local file might be stale and needs re-pulling; when resolving a publication DOI; before assuming a 404 or expired link is a data-loss problem rather than a known quirk. |
| `i_Investigation.txt` | **Not** RSD-AFF or SUBSA-CETSOL metadata — it's the generic ISA-Tab-style schema for the "Investigation metadata text file" format that appears in every PSI investigation's file corpus (fields for identifiers, title, objective, hypothesis, contacts, publications/DOIs, study design descriptors, ontology source refs for PSI + EFO), populated with a worked example: **PSI-111, "SUBSA Brazing of Aluminum Alloys IN Space" (BRAINS)**, PI Dusan Sekulic (University of Kentucky), an unrelated brazing/capillary-flow investigation. | Structural / schema reference | Parsing any investigation's own `i_Investigation.txt`-equivalent file to know what fields to expect. **Never** cite the BRAINS example content (PSI-111, brazing objective, Sekulic as PI, etc.) as background for RSD-AFF or SUBSA-CETSOL — it's a format example, not their data. |
| `index.md` (this file) | Routing manifest + triggers/authority notes for the local `contexts/` corpus. | Meta | Always the first file consulted before retrieving any other context. |

**Cross-reference finding, since revised:** the BRAINS example's Study Publication Author List in `i_Investigation.txt` is dominated by K. Lazaridis, D. Sekulic, S. Mesarovic, and M. Krivilyov (Washington State University / University of Kentucky), doing phase-field modeling of capillary flow under the SUBSA furnace program — the same research group as `2021 - Lazaridis, Kostis - PhD Dissertation.pdf` in `contexts/`. This initially looked like a link to SUBSA-CETSOL, but reading the actual `SRD_SUBSA-CETSOL.pdf` (Section 4) shows SUBSA-CETSOL's PI is Christoph Beckermann (University of Iowa) with the ESA CETSOL team (Gerhard Zimmermann) — **no overlap** with Lazaridis/Sekulic/Mesarovic. BRAINS and SUBSA-CETSOL are two *different* investigations that both happen to use the SUBSA furnace hardware; sharing hardware doesn't mean shared science team. The Lazaridis dissertation is therefore **not** SUBSA-CETSOL background — see Section 7 (Unclassified).

Confidence: **Confirmed** — `psi_existing_systems.md` and `i_Investigation.txt` read directly; the SUBSA-CETSOL link inferred from them has since been checked against the real SRD/ReadMe and found not to hold.

---

## 3. RSD-AFF investigation (amyloidogenesis / interfacial shear campaign)

| File | Purpose | Type | Authority |
|---|---|---|---|
| `RSD-AFF_PSI-Overview.pdf` | Campaign-level orientation for the RSD-AFF investigation ecosystem. | Domain Context | Source of truth (campaign overview) |
| `RSD_Technical.pdf` | Hardware familiarization for the Ring-Sheared Drop platform — capabilities, onboarding. | Structural/Domain | Advisory / supplemental |
| `(Adam et al, 2021) Amyloidogenesis Via Interfacial Shear.pdf` | Foundational interpretation reference for fibrillization kinetics, shear-induced aggregation, interfacial protein behavior. | Domain Context | Authoritative interpretation reference |
| `(McMackin et al, 2022) Amyloidogenesis Via Interfacial Shear...pdf` | ISS operational and experimental validation — microgravity fibrillization behavior, containerless reactor behavior, deployment. | Domain Context | Authoritative ISS operational reference |
| `(McMackin et al, 2023) Single-Camera PTV Within Interfacial...pdf` | Velocimetry/PTV methodology — ray tracing, image projection, CFD validation. | Procedural + Domain | Authoritative measurement methodology reference |
| `(Adam et al, 2025) Non-Newtonian Interfacial Modeling Of...pdf` | Constitutive/computational rheology modeling — Boussinesq-Scriven, shear-thinning, CFD/PTV validation. | Domain + Procedural | Authoritative computational modeling reference |

**Triggers (apply across this group):**
- Beginning RSD-AFF campaign work, PSI dataset interrogation, or hardware onboarding → `RSD-AFF_PSI-Overview.pdf` then `RSD_Technical.pdf`.
- Interpreting fibrillization kinetics, gelation, or shear-induced aggregation results → Adam 2021.
- Interpreting ISS/microgravity-specific behavior or comparing ISS vs. ground analogs → McMackin 2022.
- Doing PTV analysis, optical calibration, or CFD validation of flow fields → McMackin 2023.
- Building or validating a CFD/rheology model, COMSOL parameter sweeps, or shear-thinning constitutive behavior → Adam 2025.

Confidence: **Confirmed** — triggers and authority match the RSD-AFF section of this manifest and the listed filenames.

---

## 4. SUBSA-CETSOL investigation (columnar-to-equiaxed transition in alloy solidification)

**Investigation identity (from the SRD):** *Effect of Convection on Columnar-to-Equiaxed Transition in Alloy Solidification – SUBSA.* PI: Prof. Christoph Beckermann, University of Iowa, in collaboration with the ESA CETSOL team (Dr. Gerhard Zimmermann, ACCESS e.V., Aachen). Runs in the SUBSA (Solidification Using a Baffle in Sealed Ampoules) furnace on ISS. Four alloys tested: Al‑4wt%Cu (Ampoule 1), Al‑10wt%Cu (Ampoule 2), Al‑18wt%Cu (Ampoule 3), Al‑7wt%Si (Ampoule 4), each with a flight and ground counterpart. Hypothesis: fragmentation of columnar dendrites can drive a CET in non-grain-refined alloys without requiring nucleation ahead of the columnar front (contrary to prevailing theory).

| File | Purpose | Type | Authority |
|---|---|---|---|
| `SRD_SUBSA-CETSOL.pdf` | Science Requirements Document (short version, Sept 2020) — objectives/hypothesis, justification for long-duration microgravity, science requirements (furnace/ampoule/temperature/acceleration specs, Tables 1–3 test matrix), experiment/test procedures, data handling (telescience windows during flight; post-flight thermal + 3-axis acceleration data delivered to the PI as ASCII/Excel files), and PI deliverables (annual NASA Task Book + NSSC reports, final report, monthly highlights). | Domain | Source of truth for planned science requirements, hypothesis, and test matrix |
| `ReadMe_SUBSA_CETSOL.pdf` | Data Layout Document. Top folder `CETSOL/Experiment Data/`: **Analyzed Data** (optical images for the Al-Cu alloys + a spreadsheet of Heat Fluxes, Alloy Properties, and Measured Temperatures, sourced from the seminal paper [doi:10.1007/s11661-022-06909-6](https://link.springer.com/article/10.1007/s11661-022-06909-6) — "the main folder of interest for data") and **Raw Data** (per-sample SEM/Optical/FurnaceData_Raw folders, named `Flight_<alloy>-Ampoule<N>` and `Ground_<alloy>`). Also documents `Data Documentation`, `Development-Ampoule of Opportunity` (design/ground-test history), and a `Documentation` folder (final design image, SRD, concurrence docs, Techshot verifications, drawing package). | Structural | Source of truth for navigating SUBSA-CETSOL data — go to Analyzed Data first unless raw SEM/optical/furnace traces are specifically needed |

**Triggers:**
- Needing background, hypothesis, science requirements, furnace/sample specs, or data-handling/deliverable expectations for SUBSA-CETSOL → `SRD_SUBSA-CETSOL.pdf`.
- Retrieving or navigating SUBSA-CETSOL data files, unsure what a folder means, or deciding analyzed vs. raw data → `ReadMe_SUBSA_CETSOL.pdf`. Default to the Analyzed Data spreadsheet unless the task specifically needs raw SEM/optical/furnace traces for one ampoule.
- Matching an ampoule number to an alloy → SRD Table 2 (Ampoule 1=Al-4Cu, 2=Al-10Cu, 3=Al-18Cu, 4=Al-7Si) or the ReadMe's `Flight_<N>Cu/Si-Ampoule<N>` folder names — both agree.

Confidence: **Confirmed** — both files read directly, and their content cross-checks (alloy/ampoule numbering matches between the SRD's Table 2 and the ReadMe's folder names).

---

## 5. Unnamed investigation — particle-reinforced bulk metallic glass composite processing

**Investigation identity:** not yet confirmed by name or accession ID — no SRD, ReadMe, or overview document exists for it in `contexts/` yet. The file's own content establishes the science: a sample matrix for processing tungsten (W) particle-reinforced bulk metallic glass (BMG) matrix composites. Two matrix alloys: `Zr48Cu47.5Al4Co0.5` and "Vitreloy 106" (both well-known Zr-based BMGs). Two flight cartridges (C1, C2) carrying 12 samples total, varying particle volume percent (5/15/30%) and particle diameter (25–36 µm vs. 140–150 µm), all processed at 1200 °C with a 120-minute hold, then cooled "as rapidly as possible" back to 25 °C. This is unrelated to RSD-AFF (protein/amyloid, §3) and SUBSA-CETSOL (Al-Cu/Al-Si alloy solidification, §4) — different matrix materials, different processing temperature, and "Cartridge" rather than "Ampoule" hardware naming.

| File | Purpose | Type | Authority |
|---|---|---|---|
| `Experimental Table_Famis.csv` | Sample matrix for a BMG + tungsten-particle composite investigation — cartridge/sample IDs, matrix composition, particle type/volume%/diameter, processing temperature, hold time, cooling rate. | Domain | Source of truth for actual samples/parameters of *this* investigation |

**Triggers:**
- Needing exact sample-level composite-processing parameters (matrix composition, particle loading/size, thermal profile) for the BMG/tungsten-particle work this table describes.

Confidence: **Confirmed** content (file read directly, ruled out as RSD-AFF or SUBSA-CETSOL). **Unclassified** investigation identity — attach the matching SRD/overview here if one turns up.

---

## 6. Domain science reference (cross-investigation, advisory — pool boiling)

| File | Purpose | Type | Authority |
|---|---|---|---|
| `2025 HMT Numerical simulation of pool boiling on biphilic...pdf` | Boiling enhancement / heat transfer mechanisms on heterogeneous-wettability (biphilic) surfaces. | Domain Context | Reference/advisory — not authoritative for any PSI dataset |
| `2025 PoF Youssoufi Subcooled pool boiling studies.pdf` | Physical mechanisms of subcooled pool boiling. | Domain Context | Reference/advisory — not authoritative for any PSI dataset |

**Triggers:**
- Explaining boiling enhancement mechanisms, heterogeneous wettability effects, or heat flux behavior → biphilic (HMT) paper.
- Explaining subcooled boiling physics or interpreting boiling-related graphs/tables → Youssoufi (PoF) paper.

Confidence: **Inferred** filename-to-topic mapping — the two papers were matched to the two reference slots by title/filename, not by a full read of the PDFs.

---

## 7. Unclassified — do not route tasks here until confirmed

| File | Why it's unclassified |
|---|---|
| `2021 - Lazaridis, Kostis - PhD Dissertation.pdf` | The author-network link to `i_Investigation.txt`'s BRAINS example (Sekulic/Mesarovic/Lazaridis, Washington State University / University of Kentucky) doesn't connect to SUBSA-CETSOL, whose real PI is Christoph Beckermann (University of Iowa) with ESA's Gerhard Zimmermann — a different team entirely. BRAINS and SUBSA-CETSOL merely share the SUBSA furnace hardware. Since BRAINS itself has no document in this `contexts/` folder, the dissertation currently doesn't map to any named investigation here (including the BMG/tungsten-composite work in §5, which is materials science but a different team/hardware again). |

---

## 8. Authority model

| Tier | Meaning | Files |
|---|---|---|
| Source of truth | Overrides other sources on conflict | `RSD-AFF_PSI-Overview.pdf`, the four RSD-AFF publications (§3), `SRD_SUBSA-CETSOL.pdf` and `ReadMe_SUBSA_CETSOL.pdf` (§4), `Experimental Table_Famis.csv` for its own (unnamed) investigation (§5) |
| Advisory / supplemental | Reference and navigation support; mandatory to use when relevant, but not authoritative over source-of-truth files | `RSD_Technical.pdf`, both pool-boiling papers (§6) |
| Discovery / systems / meta | Used for routing, schema reference, and programmatic access — not for answering domain questions directly | `psi_existing_systems.md` (API access), `i_Investigation.txt` (metadata schema/example only — not RSD-AFF or SUBSA-CETSOL content), this file |
| Unclassified | Do not use until scope is confirmed | `2021 - Lazaridis, Kostis - PhD Dissertation.pdf` (§7) |

---
