#!/usr/bin/env python3
"""Build a self-contained research brief and its audit from collected data."""
import csv
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/'data/analysis.json').read_text())
ROWS = DATA['rows']
C = DATA['counts']
REPO = 'https://github.com/rounakdas07/cori-awards'
NIHR_SOURCE = 'https://nihr.opendatasoft.com/explore/dataset/nihr-summary-view/'


def e(x):
    return html.escape(str(x), quote=True)


def month(x):
    return date.fromisoformat(x).strftime('%b %Y')


def money(x):
    return f'£{x/1e6:.2f}m'


def org(x):
    if not x.isupper():
        return x
    return re.sub(r'\bNhs\b', 'NHS', x.title()).replace(' And ', ' and ')


def short_title(x):
    # Derive display names from the title; retain the complete title underneath.
    if ':' in x and len(x.split(':',1)[0]) < 35:
        return x.split(':',1)[0]
    if re.match(r'^EPILOGUE\s*-',x):
        return x.split('-',1)[0].strip()
    if x.startswith('TarGeT '):
        return 'TarGeT'
    if x.startswith('SWIFT LUNG -'):
        return 'SWIFT LUNG'
    if x.endswith('(PRESIDENT)'):
        return 'PRESIDENT'
    return x


def score_notes(r):
    yes=[]
    if r['named_lead_point']: yes.append('named lead')
    if r['recent_start_point']: yes.append('recent contract start')
    if r['multisite_point']: yes.append('multi-site or umbrella design')
    return '; '.join(yes)


assert C['award_rows_pulled'] == C['award_rows_kept'] + C['award_rows_dropped']
assert sum(DATA['drop_reasons'].values()) == C['award_rows_dropped']
assert len({r['award_id'] for r in ROWS}) == len(ROWS)
assert all(r['score'] == r['named_lead_point']+r['recent_start_point']+r['multisite_point'] for r in ROWS)
assert DATA['top_organisation_award_ids'] == ['NIHR510518','NIHR504024','NIHR172122'], 'Recommendations changed; review the editorial copy before release'
assert C['registry_records_linked'] == 0, 'Update the registry-check paragraph before release'
assert (len(ROWS), C['distinct_organisations'], C['published_leads'], C['award_total_gbp']) == (7,5,5,21334769.55), 'Findings changed; review summary, recommendations and counts before release'

table=[]
for r in ROWS:
    title=short_title(r['title'])
    full = f'<span class="study-title">{e(r["title"])}</span>' if title != r['title'] else ''
    table.append(f'''<tr>
      <td class="rank">{r['rank']}</td>
      <th scope="row"><a href="{e(r['source_url'])}">{e(title)}</a>{full}<span class="organisation">{e(org(r['organisation']))}</span><span class="reference">{e(r['award_id'])}</span></th>
      <td>{e(r['investigators']) if r['investigators'] else '<span class="muted">Not stated in export</span>'}</td>
      <td class="nowrap">{month(r['project_start'])}</td>
      <td class="number">{money(r['award_gbp'])}</td>
      <td><span class="score">{r['score']}/3</span><span class="score-note">{e(score_notes(r))}</span></td>
    </tr>''')

page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{len(ROWS)} funded cancer trial projects — prepared for Cori Clinical</title>
<meta name="description" content="A sourced shortlist of seven NIHR-funded cancer trial projects across five UK organisations, with named investigators, a simple ranking and explicit qualification gaps.">
<style>
:root{{color-scheme:light;--ink:#242421;--muted:#62625c;--rule:#d5d5ce;--accent:#345a58}}
*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:var(--ink);font-family:Georgia,'Times New Roman',serif;font-size:18px;line-height:1.65}}
main{{max-width:1160px;margin:auto;padding:48px 30px 64px}}h1{{font-size:42px;line-height:1.16;font-weight:400;max-width:930px;margin:0 0 20px;letter-spacing:-.6px}}h2{{font-size:24px;line-height:1.3;font-weight:400;margin:35px 0 14px}}p{{margin:0 0 19px}}a{{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}}a:focus-visible{{outline:2px solid var(--accent);outline-offset:4px}}
.byline{{font-size:15px;color:var(--muted);margin-bottom:27px}}.summary{{max-width:1020px;font-size:19px}}.qualification{{border-block:1px solid var(--rule);padding:16px 0;margin:24px 0 28px;font-size:15px;line-height:1.65}}.qualification p{{margin:0}}.table-wrap{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;min-width:900px;table-layout:fixed;font-size:14px;line-height:1.5}}caption{{text-align:left;font-size:18px;margin:0 0 12px}}thead th{{font-size:12px;color:var(--muted);font-weight:400;text-align:left;border-block:1px solid var(--ink);padding:13px 8px}}tbody th,td{{text-align:left;vertical-align:top;padding:17px 8px;border-bottom:1px solid var(--rule);font-weight:400}}tbody th>a{{font-size:16px}}.rank{{color:var(--muted)}}.study-title{{display:block;margin:5px 0;font-size:12px;color:var(--muted)}}.organisation{{display:block;margin-top:8px}}.reference{{display:block;font-size:11px;color:var(--muted);margin-top:3px}}.number{{text-align:right;white-space:nowrap}}.nowrap{{white-space:nowrap}}.score{{font-size:18px}}.score-note{{display:block;font-size:12px;color:var(--muted);margin-top:4px}}.muted{{color:var(--muted)}}.table-note{{font-size:14px;color:var(--muted);margin-top:13px;max-width:1040px}}.actions{{padding:0;margin:0;list-style:none;counter-reset:action}}.actions li{{counter-increment:action;border-top:1px solid var(--rule);padding:15px 0 15px 28px;position:relative;font-size:16px}}.actions li:before{{content:counter(action) ".";position:absolute;left:0;color:var(--muted)}}.method{{border-top:1px solid var(--ink);margin-top:34px;font-size:15px;max-width:1050px}}.method h2{{margin-top:22px}}.method p{{margin-bottom:16px}}.author{{border-top:1px solid var(--rule);margin-top:32px;padding-top:22px;font-size:15px;max-width:1030px}}footer{{font-size:15px;margin-top:22px}}
@media(max-width:650px){{main{{padding:28px 18px 44px}}h1{{font-size:32px}}.summary{{font-size:18px}}body{{font-size:17px}}.byline{{font-size:14px}}.qualification{{font-size:14px}}}}
@media print{{main{{padding:0}}a{{color:inherit}}.table-wrap{{overflow:visible}}table{{min-width:0;font-size:11px}}tr{{break-inside:avoid}}}}
</style>
</head>
<body><main>
<h1>{len(ROWS)} funded cancer trial projects across {C['distinct_organisations']} UK organisations</h1>
<p class="byline">Prepared for Cori Clinical by Rounak Das · 25 November 2026</p>
<p class="summary">A screen of {C['award_rows_pulled']} NIHR award records retained <strong>{len(ROWS)} oncology trial projects</strong> with contract starts in the past year, representing <strong>£{C['award_total_gbp']/1e6:.1f}m in original project funding</strong>. Five projects name research leads; two do not. Start qualification calls with <strong>Leeds, NHS Greater Glasgow and Clyde, and Oxford</strong>, the first three distinct organisations with named leads under the rule below. These are concrete projects through which to test demand for Cori’s trial-planning and documentation support, supporting its stated commercial expansion.</p>
<aside class="qualification" aria-label="What remains to qualify"><p><strong>What the evidence establishes.</strong> NIHR has funded the work described below. The grant-ID checks found no linked ClinicalTrials.gov or ISRCTN records, so recruitment stage remains unverified; an absent identifier link does not mean a trial is unregistered. Confirm current protocol work, existing suppliers and who can authorise a purchase before treating any entry as a sales opportunity.</p></aside>
<div class="table-wrap" role="region" aria-label="Funded trial projects; scroll horizontally on a small screen" tabindex="0">
<table><caption>Funded projects, research leads and qualification priority</caption>
<colgroup><col style="width:4%"><col style="width:34%"><col style="width:20%"><col style="width:11%"><col style="width:10%"><col style="width:21%"></colgroup>
<thead><tr><th scope="col">Rank</th><th scope="col">Project and UK host</th><th scope="col">Published research lead</th><th scope="col">Contract start</th><th scope="col" class="number">Original award</th><th scope="col">Score and evidence</th></tr></thead>
<tbody>{''.join(table)}</tbody></table></div>
<p class="table-note">Every project title opens its NIHR award record. Amounts are rounded here; the CSV retains pounds and pence. Grant funding is not an available software budget. Contract starts are not recruitment starts. Multiple awards at one organisation remain separate projects; the three recommendations below use distinct organisations.</p>
<h2>Three conversations to start</h2>
<ol class="actions">
<li><strong>Leeds — Professor Tze Min Wah, SONiC-LIVER.</strong> The £6.19m award describes a trial in six UK hospitals; ask what protocol and site-document preparation remains, and who owns those workflows. Leeds also has the separate £2.88m BACBONE award.</li>
<li><strong>NHS Greater Glasgow and Clyde — Dr Mark Hall / Professor David Lowe, SWIFT LUNG.</strong> The £1.70m award describes a prospective trial across three NHS sites; ask how document versions and cross-site decisions are coordinated.</li>
<li><strong>Oxford — Professor Prasanna Sooriakumaran, PRESIDENT.</strong> The £3.00m award explicitly funds a randomised surgical trial; ask which preparation tasks remain and whether the trial team is evaluating outside support.</li>
</ol>
<section class="method" aria-labelledby="method-heading"><h2 id="method-heading">Method and limits</h2>
<p><strong>Purpose and product boundary.</strong> This is a sales-research worklist for Cori’s own team. Its <a href="https://www.cori-clinical.com/news/cori-clinical-raises-4m-seed-round">7 October funding announcement</a> names commercial expansion and reports academic customers alongside CROs. Cori’s <a href="https://www.cori-clinical.com/platform">product description</a> already covers trial precedents, design, budgets and regulatory review; this brief addresses finding and qualifying prospective users. Existing customer relationships and Cori’s private pipeline are unknown.</p>
<p><strong>Sources and dates.</strong> The <a href="{NIHR_SOURCE}">NIHR Research and Training Awards dataset</a> was retrieved on 25 November 2026. Its metadata says the edition covers data to <strong>31 March 2026</strong>, although it was modified on 29 October and contains later contracted project starts. It is a lagged funding snapshot, not a complete list of awards announced this year. The script also queried the public <a href="https://clinicaltrials.gov/data-api/api">ClinicalTrials.gov API</a> and <a href="https://www.isrctn.com/page/definitions">ISRCTN registry</a> by award identifier on the collection date.</p>
<p><strong>Filters and cleaning.</strong> Retrieve all awards with a contract start on or after 25 November 2025, then retain starts through 25 November 2026; research awards marked active or contracted; a valid UK host postcode; an explicit oncology term in the title; and an explicit trial or first-in-human title, or a stated prospective clinical-trial plan in the abstract. Exclude follow-up-only awards, evidence syntheses, consortia, training, and records without the required evidence. Deduplicate by NIHR award ID, normalise whitespace and retain missing investigator names as missing. {C['award_rows_pulled']} rows became {len(ROWS)}; the <a href="{REPO}/blob/main/QUALITY_REPORT.md">quality report</a> records all exclusions and the complete retained sample.</p>
<p><strong>Scoring.</strong> One point each for a published investigator, a contract start on or after {date.fromisoformat(DATA['recent_cutoff']).strftime('%d %B %Y')}, and explicit multi-centre, multi-site or umbrella wording about the funded trial. Statements about a hypothetical follow-on study do not earn the design point. Highest total first; ties favour a named lead, then a later contract start, then a larger original award. Recommend the first three distinct organisations with named leads. This is a transparent order for research calls, not a measure of clinical quality, purchasing likelihood or operational difficulty.</p>
<p><strong>Registry linkage.</strong> The exact NIHR award IDs were queried together, plus any NCT or ISRCTN IDs stated in the awards. Neither registry returned a record for that query. This check does not search every title variation, CTIS or local registers, and missing grant references are possible. All seven recruitment stages therefore remain unknown here; none is labelled “not yet recruiting”.</p>
<p><strong>Coverage and remaining questions.</strong> The strict title rule misses oncology projects whose titles do not name the disease. A UK host does not establish every trial site’s country. The two Birmingham umbrella awards lack investigator names in this export. Named researchers are not verified purchasing contacts, no email is guessed, and public funding does not establish unspent funds, unmet demand or an open procurement. The <a href="{REPO}/tree/main/scripts">collection and build scripts</a> retain the exact rules, source hashes and retrieval timestamps. NIHR data is reused under the <a href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/">Open Government Licence v3.0</a>.</p>
</section>
<p class="author">I’m Rounak Das, a second-year medical student at Nottingham, a published co-author on NHS cancer-data research and an AI Research Lead Intern at OncoFlow AI. I built this brief to give Cori a small, traceable set of funded oncology projects where its team can test whether trial-preparation support is needed.</p>
<footer><a href="cori-awards.csv" download>Download the cleaned CSV</a> · {len(ROWS)} projects</footer>
</main></body></html>'''
(ROOT/'index.html').write_text(page)

sample_by_id={r['award_id']:r for r in ROWS}
report=['# Data quality report', '', 'Prepared on 25 November 2026. This is a qualification worklist, not a verified buying-intent list.', '', '## Collection and retention', '', '| Measure | Count |', '|---|---:|']
for k,v in C.items(): report.append(f'| {k} | {v} |')
report += ['', 'The API applied the initial date filter; 348 records were downloaded from an 11,385-record catalogue. These are project starts, not award-announcement dates.', '', '## Exclusive first-failure exclusions', '', '| Reason | Rows |','|---|---:|']
for k,v in DATA['drop_reasons'].items(): report.append(f'| {k} | {v} |')
report += ['', 'The counts reconcile exactly. No duplicate NIHR IDs remained. Two retained awards have missing investigator names; those values were not inferred. Other required retained fields are populated.', '', '## Random retained sample', '', f'Only {len(ROWS)} rows passed the filters, so all {len(ROWS)} are shown in seeded random order (seed 20261125). Ten unique kept rows do not exist; none have been invented or added to pad the sample.', '', '| Award | Organisation / lead | Start | Original award | Score |','|---|---|---|---:|---:|']
for ident in DATA['quality_sample_award_ids']:
    r=sample_by_id[ident]
    report.append(f"| [{ident}]({r['source_url']}) — {r['title']} | {r['organisation']}; {r['investigators'] or 'Investigator not stated'} | {r['project_start']} | £{r['award_gbp']:,.2f} | {r['score']}/3 |")
report += ['', '## Evidence used for retention and scoring', '']
for r in ROWS:
    report += [f"### {r['award_id']}", '',f"Trial evidence: {r['trial_evidence']}", '',f"Design-point evidence: {r['multisite_evidence'] or 'No qualifying phrase found; zero points.'}", '',f"Points: named lead {r['named_lead_point']}; recent start {r['recent_start_point']}; design {r['multisite_point']}.", '']
report += ['## Registry-link check', '', 'Exact award-ID query; no returned records in either registry. No recruitment status is inferred. A separate ISRCTN positive control (ISRCTN49306926) returned one record during QA, showing the public query endpoint responded to a known identifier.', '', f"Query: `{DATA['registry_query']}`", '']
for u in DATA['registry_urls']:report.append(f'- {u}')
report += ['', '## Limits', '']+[f'- {v}' for v in DATA['limitations']]
report += ['', '## Source retrieval audit', '', '| Source request | Retrieved UTC | SHA-256 |', '|---|---|---|']
for s in DATA['source_requests']:report.append(f"| [{s['cache_file']}]({s['url']}) | {s['retrieved_at']} | `{s['sha256']}` |")
report += ['', '## Excluded rows', '', '| Award | Title | First exclusion reason |','|---|---|---|']
for r in DATA['excluded_awards']:report.append(f"| {r['award_id']} | {r['title'].replace('|','/')} | {r['reason']} |")
(ROOT/'QUALITY_REPORT.md').write_text('\n'.join(report)+'\n')

dist=ROOT/'dist';dist.mkdir(exist_ok=True)
for name in ['index.html','cori-awards.csv']:shutil.copyfile(ROOT/name,dist/name)
preview=ROOT/'.openai';preview.mkdir(exist_ok=True)
(preview/'hosting.json').write_text('{"static":{"directory":"dist"}}\n')
print(f'Built {len(ROWS)} static rows; no JavaScript or external assets. Quality report contains all {len(ROWS)} retained rows and {len(DATA["excluded_awards"])} exclusions.')
