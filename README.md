# Funded cancer trial projects for Cori Clinical

A public-data commercial qualification brief prepared by Rounak Das on 25 November 2026.

Live page: https://rounakdas07.github.io/cori-awards/

This is a small, auditable worklist of UK-hosted, NIHR-funded oncology trial projects. It gives Cori's commercial team project-specific starting points for qualification conversations. It does not implement Cori's trial-design, precedent, budgeting or regulatory-review features. It does not establish buying intent or access Cori's private pipeline.

## Findings

- 348 grant records downloaded; seven projects retained across five UK organisations.
- £21,334,769.55 in original project awards, not a software budget or available revenue.
- Five projects publish investigator names; two do not.
- First three distinct organisations with published leads: University of Leeds, NHS Greater Glasgow and Clyde, University of Oxford.
- No identifier-linked records returned by the ClinicalTrials.gov or ISRCTN grant-ID queries. Recruitment stage remains unknown for every entry.

See [QUALITY_REPORT.md](QUALITY_REPORT.md) for exclusions, source hashes, scoring evidence and all seven retained rows in seeded random order. A requested sample of ten unique retained projects cannot be supplied from a seven-row result without padding it.

## Why this question

1. Cori's [own seed announcement](https://www.cori-clinical.com/news/cori-clinical-raises-4m-seed-round) reports a $4m seed round on 7 October 2026 and explicitly includes expanding delivery, clinical/regulatory capability and commercial relationships. It reports academic customers as well as CROs.
2. Three questions were considered. Trial precedent comparisons were dropped because Cori already advertises that capability. A generic list of new registered trials was dropped because trial-intelligence products already cover it. This brief asks which recent NIHR oncology trial awards yield specific projects and identifiable teams worth qualifying.
3. The existence check covered [Cori's platform](https://www.cori-clinical.com/platform), [NIHR Open Data](https://nihr.opendatasoft.com/pages/homepage/), [Citeline Trialtrove](https://citeline.com/products-services/trialtrove/), [Benchlead's US grant-based clinical research leads](https://getbenchlead.com/leads/clinical-research-services), [OpenHDI](https://openhdi.com/sources) and a [UK registered-trial dashboard](https://clinicaltrialsuk.io/). Raw data and adjacent tools exist. No ready-made version of this particular UK oncology qualification brief was found in the searched material; that is not a claim that no competing service could produce it. No paid product was accessed or comprehensively audited.
4. The deliverable is a ranked set of funded projects with named investigators and explicit gaps to resolve on a first call. It serves Cori's stated commercial expansion, with a narrow oncology focus matching the author's evidence experience. Its value is the completed filtering, source reconciliation and honest qualification notes, not exclusive data or an assertion that Cori could not reproduce the work.

## Run

Python 3.10+; standard library only. From this directory:

```sh
python scripts/collect.py --as-of 2026-11-25
python scripts/build.py
```

The first command downloads NIHR data and queries both registries. Subsequent runs reuse `.cache/` with source retrieval timestamps and SHA-256 hashes. Use `--refresh` to fetch new bytes. A different date creates a new grant-window request; refresh the other sources for a fully fresh run.

`build.py` deliberately stops if recommendations or registry-link findings change: refresh the editorial summary and review it before publication. The static HTML embeds every row and needs no client-side fetch, JavaScript, fonts, storage or third-party assets. The only page download is the cleaned CSV.

## Filters and score

Past-year project starts through the as-of date; research awards marked active/contracted; a valid UK host postcode; explicit cancer terminology in the title; and an explicit trial/first-in-human title or a stated prospective clinical-trial plan in the abstract. Exclude follow-up, reviews, syntheses and consortia. Deduplicate by award ID. All labels and scores come from code, with no per-award inclusion overrides or hand-labelled data.

One point each for a published investigator, a project start within 183 days, and explicit multi-site/umbrella wording about the funded study. Exclude sentences describing a hypothetical later study from the design point. Ties: named investigator, later start, larger original award, award ID. Recommend the first three distinct organisations with named investigators.

## Material limits

NIHR metadata says coverage to 31 March 2026, despite an October modification date and later contracted starts. This is a lagged funding snapshot, not a complete feed of newly announced grants. Contract start is not recruitment start. ClinicalTrials.gov and ISRCTN searches use award IDs and any explicit registry IDs in the award text, not fuzzy title matching; a missing match does not prove non-registration. The initial broad acronym probe was rejected because it returned unrelated trials.

Funding does not establish remaining budget, unmet need, purchasing authority, supplier availability or an open procurement. Named researchers are not verified buyers. Strict title filtering misses some cancer trials; the UK host postcode does not establish every trial site's country. Neither study quality nor Cori suitability is validated by the score.

## Sources and rights

- [NIHR Research and Training Awards](https://nihr.opendatasoft.com/explore/dataset/nihr-summary-view/), [public API](https://nihr.opendatasoft.com/api-console/explore/v2.1/); Open Government Licence v3.0. Contains public sector information licensed under the Open Government Licence v3.0.
- [ClinicalTrials.gov API](https://clinicaltrials.gov/data-api/api).
- [ISRCTN API documentation](https://www.isrctn.com/editorial/retrieveFile/81786542-9920-48a0-8fce-09f8428ab843/37855). Registry records were queried but none were included in the lead table.
- [University of Leeds corroboration of SONiC-LIVER](https://medicinehealth.leeds.ac.uk/leeds-institute-research-st-james/news/article/775/funding-secured-for-innovative-liver-cancer-research).

The complete request URLs, retrieval timestamps, hashes and exclusion ledger are in `data/analysis.json`. Raw downloads are cached locally and omitted from Git. No patient-level data, inferred email addresses or personal contact details were collected.
