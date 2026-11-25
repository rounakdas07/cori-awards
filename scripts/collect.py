#!/usr/bin/env python3
"""Reproducible NIHR oncology trial qualification screen; standard library only."""
import argparse
import csv
import hashlib
import html
import json
import random
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache'
NIHR = 'https://nihr.opendatasoft.com/api/explore/v2.1/catalog/datasets/nihr-summary-view'
CTG = 'https://clinicaltrials.gov/api/v2/studies'
ISRCTN = 'https://www.isrctn.com/api/query/format/default'
ONCOLOGY = re.compile(r'\b(?:cancers?|oncolog\w*|gliomas?|glioblastoma\w*|leuk\w*|leukaem\w*|lymphomas?|myelomas?|tumours?|tumors?|carcinomas?|sarcomas?|melanomas?|neoplasms?)\b', re.I)
EXCLUDED_TITLE = re.compile(r'follow[ -]?up|meta[ -]?analysis|synthesis|systematic review|\bconsortium\b', re.I)
TRIAL_TITLE = re.compile(r'\btrial\b|first[ -]in[ -]human', re.I)
PROSPECTIVE = re.compile(r'\bwe will (?:do|run|conduct|undertake)\b.{0,100}?\bclinical trial\b|\b(?:we propose|design and methods)\b.{0,100}?\bprospective\b.{0,80}?\btrial\b', re.I)
MULTISITE = re.compile(r'\bmulti[ -]?(?:centre|center)\b|\bumbrella\b|\bacross\s+\d+\s+(?:NHS\s+|UK\s+)?(?:sites|hospitals)\b|\bin\s+\d+\s+hospitals\s+in\s+the\s+UK\b', re.I)
LATER_STUDY = re.compile(r'\bwould follow\b|\bfollow-on\b|\bfuture\b|\bsubsequent\b|\bnext phase\b', re.I)
REG_ID = re.compile(r'\b(?:NCT\d{8}|ISRCTN\s*\d{8})\b', re.I)
UK_POSTCODE = re.compile(r'^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$', re.I)


def clean(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', str(value or '')))).strip()


def get(url, key, audit, refresh=False):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / key
    stamp = CACHE / (key + '.retrieval.json')
    if refresh or not path.exists() or not stamp.exists():
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'RounakDas-public-research-brief/1.0', 'Accept': '*/*'})
                with urllib.request.urlopen(req, timeout=60) as response:
                    data = response.read()
                    resolved = response.geturl()
                path.write_bytes(data)
                stamp.write_text(json.dumps({'url': url, 'resolved_url': resolved, 'retrieved_at': datetime.now(timezone.utc).isoformat()}))
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
    data = path.read_bytes()
    meta = json.loads(stamp.read_text())
    assert meta['url'] == url, f'Cache key reused for a different request: {key}'
    audit.append({**meta, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), 'cache_file': key})
    return data


def snippet(text, match):
    if not match:
        return ''
    return text[max(0, match.start()-55):min(len(text), match.end()+140)].strip()


def query_url(base, params):
    return base + '?' + urllib.parse.urlencode(params)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--as-of', default='2026-11-25')
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    asof = date.fromisoformat(args.as_of)
    window_start = asof - timedelta(days=365)
    recent_cutoff = asof - timedelta(days=183)
    audit = []
    metadata = json.loads(get(NIHR, 'nihr-metadata.json', audit, args.refresh))
    award_url = query_url(NIHR + '/exports/json', {'where': f"start_date >= date'{window_start.isoformat()}'"})
    raw = json.loads(get(award_url, f'nihr-awards-{window_start.isoformat()}.json', audit, args.refresh))
    assert isinstance(raw, list) and raw, 'NIHR response is empty or changed schema'
    seen, excluded, kept = set(), [], []
    stages = Counter()

    for source in raw:
        award = clean(source.get('project_id'))
        title = clean(source.get('project_title'))
        reason = None
        if not award:
            reason = 'Missing award identifier'
        elif award in seen:
            reason = 'Duplicate award identifier'
        seen.add(award)
        start = clean(source.get('start_date'))
        if not reason and (not start or not window_start.isoformat() <= start <= asof.isoformat()):
            reason = 'Outside the past-year project-start window'
        if not reason and source.get('programme_type') != 'Research':
            reason = 'Training award, not a research project'
        if not reason and source.get('project_status') not in {'Active', 'Contracted'}:
            reason = 'Award not active or contracted in the export'
        if not reason and not UK_POSTCODE.fullmatch(clean(source.get('postcode'))):
            reason = 'No valid UK host postcode'
        if not reason and not ONCOLOGY.search(title):
            reason = 'No explicit oncology term in the project title'
        if not reason and EXCLUDED_TITLE.search(title):
            reason = 'Follow-up, synthesis or consortium rather than a discrete new trial'
        abstract = clean(' '.join([source.get('plain_english_abstract') or '', source.get('scientific_abstract') or '']))
        trial_match = TRIAL_TITLE.search(title)
        prospective_match = PROSPECTIVE.search(abstract)
        if not reason and not (trial_match or prospective_match):
            reason = 'No explicit new interventional trial signal under the stated rule'
        if not reason and (not source.get('contracted_organisation') or not source.get('award_amount_from_dh') or not source.get('funding_and_awards_link')):
            reason = 'Missing organisation, award value or source link'
        if reason:
            excluded.append({'award_id': award, 'title': title, 'reason': reason})
            stages[reason] += 1
            continue

        combined = title + ' ' + abstract
        # Do not award a point for a separate, hypothetical later trial.
        multi_evidence = ''
        for sentence in [title] + re.split(r'(?<=[.!?])\s+', abstract):
            candidate = MULTISITE.search(sentence)
            if candidate and not LATER_STUDY.search(sentence):
                multi_evidence = snippet(sentence, candidate)
                break
        investigators = ' / '.join(dict.fromkeys(clean(x) for x in (source.get('award_holder_name') or '').split('/') if clean(x)))
        named = bool(investigators)
        recent = start >= recent_cutoff.isoformat()
        registry_ids = sorted({re.sub(r'\s+', '', x.upper()) for x in REG_ID.findall(combined)})
        kept.append({
            'award_id': award, 'title': title, 'organisation': clean(source['contracted_organisation']),
            'investigators': investigators, 'award_gbp': float(source['award_amount_from_dh']),
            'project_start': start, 'project_end': clean(source.get('end_date')),
            'award_status': source['project_status'], 'programme': clean(source.get('programme')),
            'postcode': clean(source.get('postcode')), 'source_url': source['funding_and_awards_link'],
            'trial_evidence': title if trial_match else snippet(abstract, prospective_match),
            'multisite_evidence': multi_evidence,
            'named_lead_point': int(named), 'recent_start_point': int(recent), 'multisite_point': int(bool(multi_evidence)),
            'score': int(named)+int(recent)+int(bool(multi_evidence)),
            'registry_ids_in_award': registry_ids,
        })

    # Retrieve registry records by award ID; accept links only when the exact
    # award ID occurs in the returned record or an ID is explicitly in the award.
    # An absent cross-reference is NEVER interpreted as absence of registration.
    assert kept, 'No awards survived; revisit the question before querying registries'
    registry_query = ' OR '.join(x['award_id'] for x in kept)
    ids_from_awards = sorted({v for x in kept for v in x['registry_ids_in_award']})
    if ids_from_awards:
        registry_query += ' OR ' + ' OR '.join(ids_from_awards)
    query_hash = hashlib.sha256(registry_query.encode()).hexdigest()[:12]
    ctg_url = query_url(CTG, {'query.term': registry_query, 'format':'json', 'countTotal':'true', 'pageSize':100})
    ctg = json.loads(get(ctg_url, f'ctgov-{query_hash}.json', audit, args.refresh))
    assert not ctg.get('nextPageToken'), 'Registry response exceeds one page; paginate before publishing'
    isrctn_url = query_url(ISRCTN, {'q':registry_query, 'limit':100})
    isrctn = ET.fromstring(get(isrctn_url, f'isrctn-{query_hash}.xml', audit, args.refresh))
    is_trials = list(isrctn)
    assert int(isrctn.attrib.get('totalCount', '0')) == len(is_trials), 'Incomplete ISRCTN response'
    records = []
    for study in ctg.get('studies', []):
        protocol = study['protocolSection']
        identity = protocol['identificationModule']
        status = protocol.get('statusModule', {})
        records.append({'registry':'ClinicalTrials.gov','id':identity['nctId'], 'url':'https://clinicaltrials.gov/study/'+identity['nctId'], 'text':json.dumps(study), 'status':status.get('overallStatus','Not stated'), 'last_updated':status.get('lastUpdatePostDateStruct',{}).get('date','')})
    for trial in is_trials:
        tags = {e.tag.split('}')[-1]: (e.text or '') for e in trial.iter()}
        identifier = tags.get('isrctn') or tags.get('isrctnNumber') or ''
        if not identifier:
            raise ValueError('ISRCTN matched a record; inspect its current identifier schema')
        identifier = 'ISRCTN'+identifier.removeprefix('ISRCTN')
        records.append({'registry':'ISRCTN', 'id':identifier, 'url':'https://www.isrctn.com/'+identifier, 'text':' '.join(trial.itertext()), 'status':'See registry; no recruitment inference from dates', 'last_updated':tags.get('lastEdited','')})
    matched_record_ids = set()
    for row in kept:
        row['registry_links'] = []
        for record in records:
            exact_award = bool(re.search(r'(?<![A-Z0-9])'+re.escape(row['award_id'])+r'(?![A-Z0-9])', record['text'], re.I))
            if exact_award or record['id'] in row['registry_ids_in_award']:
                row['registry_links'].append({k:v for k,v in record.items() if k != 'text'})
                matched_record_ids.add(record['id'])
        row['registry_check'] = 'Identifier-linked record found' if row['registry_links'] else 'No identifier-linked record found; recruitment status unverified'

    kept.sort(key=lambda x: (-x['score'], -x['named_lead_point'], -date.fromisoformat(x['project_start']).toordinal(), -x['award_gbp'], x['award_id']))
    for n, row in enumerate(kept, 1):
        row['rank'] = n
    # Recommend the first three distinct organisations with a published lead.
    actions, organisations = [], set()
    for row in kept:
        if row['investigators'] and row['organisation'] not in organisations:
            actions.append(row['award_id'])
            organisations.add(row['organisation'])
        if len(actions) == 3:
            break
    assert len(actions) == 3, 'Fewer than three contactable organisations; revisit the project'
    rng = random.Random(20261125)
    sample = rng.sample(kept, min(10, len(kept)))
    output = {
        'as_of':asof.isoformat(), 'window_start':window_start.isoformat(), 'recent_cutoff':recent_cutoff.isoformat(),
        'nihr_metadata':metadata['metas']['default'], 'source_requests':audit,
        'counts':{'nihr_catalogue_records':metadata['metas']['default']['records_count'], 'award_rows_pulled':len(raw), 'award_rows_kept':len(kept), 'award_rows_dropped':len(excluded), 'distinct_organisations':len({x['organisation'] for x in kept}), 'published_leads':sum(bool(x['investigators']) for x in kept), 'award_total_gbp':round(sum(x['award_gbp'] for x in kept),2), 'ctgov_records_returned':len(ctg.get('studies',[])), 'isrctn_records_returned':len(is_trials), 'registry_records_linked':len(matched_record_ids)},
        'drop_reasons':dict(stages), 'excluded_awards':excluded, 'rows':kept,
        'top_organisation_award_ids':actions, 'quality_sample_award_ids':[x['award_id'] for x in sample],
        'registry_query':registry_query, 'registry_urls':[ctg_url,isrctn_url],
        'rules':{'oncology_title_regex':ONCOLOGY.pattern,'excluded_title_regex':EXCLUDED_TITLE.pattern,'trial_title_regex':TRIAL_TITLE.pattern,'prospective_abstract_regex':PROSPECTIVE.pattern,'multisite_regex':MULTISITE.pattern,'later_study_exclusion_regex':LATER_STUDY.pattern},
        'limitations':[
            'Project start dates are contract dates, not funding announcement or recruitment dates.',
            'NIHR metadata describes coverage to 31 March 2026; the file was modified in October and contains later contracted starts. Treat as a lagged funding snapshot, not all recent awards.',
            'Award values are original project funding, not unspent funds, software budgets or revenue available to Cori.',
            'Title filtering favours precision and misses cancer trials whose titles do not name the disease.',
            'Registry checks use exact identifiers, not fuzzy title matching; absent links do not mean unregistered or not yet recruiting.',
            'A funded project does not establish demand, procurement authority, current suppliers, or an intention to buy software.',
            'Named investigators are research contacts, not verified purchasing decision-makers. No email address is inferred.',
            'The host organisation postcode establishes UK hosting, not the countries of every trial site.'
        ]
    }
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'data'/'analysis.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    fields = ['rank','score','award_id','title','organisation','investigators','award_gbp','project_start','project_end','award_status','programme','named_lead_point','recent_start_point','multisite_point','trial_evidence','multisite_evidence','registry_check','source_url']
    with (ROOT/'cori-awards.csv').open('w',newline='',encoding='utf-8-sig') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n')
        writer.writeheader(); writer.writerows(kept)
    print(json.dumps(output['counts'],indent=2))
    print('Drop reasons:',json.dumps(dict(stages)))
    for x in kept:
        print(x['rank'],x['score'],x['award_id'],x['organisation'],x['title'])


if __name__ == '__main__':
    main()
