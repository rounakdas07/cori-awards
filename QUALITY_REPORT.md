# Data quality report

Prepared on 25 November 2026. This is a qualification worklist, not a verified buying-intent list.

## Collection and retention

| Measure | Count |
|---|---:|
| nihr_catalogue_records | 11385 |
| award_rows_pulled | 348 |
| award_rows_kept | 7 |
| award_rows_dropped | 341 |
| distinct_organisations | 5 |
| published_leads | 5 |
| award_total_gbp | 21334769.55 |
| ctgov_records_returned | 0 |
| isrctn_records_returned | 0 |
| registry_records_linked | 0 |

The API applied the initial date filter; 348 records were downloaded from an 11,385-record catalogue. These are project starts, not award-announcement dates.

## Exclusive first-failure exclusions

| Reason | Rows |
|---|---:|
| Training award, not a research project | 130 |
| No explicit oncology term in the project title | 197 |
| Follow-up, synthesis or consortium rather than a discrete new trial | 3 |
| No explicit new interventional trial signal under the stated rule | 7 |
| No valid UK host postcode | 3 |
| Outside the past-year project-start window | 1 |

The counts reconcile exactly. No duplicate NIHR IDs remained. Two retained awards have missing investigator names; those values were not inferred. Other required retained fields are populated.

## Random retained sample

Only 7 rows passed the filters, so all 7 are shown in seeded random order (seed 20261125). Ten unique kept rows do not exist; none have been invented or added to pad the sample.

| Award | Organisation / lead | Start | Original award | Score |
|---|---|---|---:|---:|
| [NIHR209472](https://fundingawards.nihr.ac.uk/award/NIHR209472) — Prototype validation and exploratory first-in-human pilot of an implantable Electric Field Therapy device for recurrent glioblastoma: iterative clinical safety assessment (IDEAL 0/1 study) | QV Bioelectronics Ltd; Dr Richard Fu | 2026-01-01 | £1,206,498.00 | 1/3 |
| [NIHR510518](https://fundingawards.nihr.ac.uk/award/NIHR510518) — SONiC-LIVER: Study Of Non-invasive Cavitation Histotripsy Therapy for Liver Cancers | University of Leeds; Professor Tze Min Wah | 2026-06-01 | £6,189,274.35 | 3/3 |
| [NIHR504024](https://fundingawards.nihr.ac.uk/award/NIHR504024) — SWIFT LUNG - Streamlined Workflow for Investigation and Fast Tracking Lung Cancer Diagnosis | NHS GREATER GLASGOW AND CLYDE; Dr Mark Hall / Professor David Lowe | 2026-04-01 | £1,704,121.00 | 2/3 |
| [NIHR501826](https://fundingawards.nihr.ac.uk/award/NIHR501826) — TarGeT (TARGETED PEDIATRIC HIGH-GRADE GLIOMA THERAPY) Phase 2 Umbrella Trial | University of Birmingham; Investigator not stated | 2026-09-01 | £5,165,004.99 | 2/3 |
| [NIHR501825](https://fundingawards.nihr.ac.uk/award/NIHR501825) — EPILOGUE- Phase I/II combination umbrella trial in relapsed pediatric low-grade glioma | University of Birmingham; Investigator not stated | 2026-09-01 | £1,196,039.80 | 2/3 |
| [NIHR172122](https://fundingawards.nihr.ac.uk/award/NIHR172122) — PRostatEctomy Surgery In Disseminated metastatic hormone sensitive prostate cancer with Endpoint assessment using Nuclear imaging Technology using PSMA PET/CT: a randomised controlled full trial (PRESIDENT) | University of Oxford; Professor Dr Prasanna Sooriakumaran | 2026-04-01 | £2,998,348.94 | 1/3 |
| [NIHR175280](https://fundingawards.nihr.ac.uk/award/NIHR175280) — BACBONE: Bracing for spinal bone disease in newly diagnosed myeloma: A phase III randomised controlled trial | University of Leeds; Dr Christopher Parrish / Dr Stella Bowcock | 2026-05-01 | £2,875,482.47 | 2/3 |

## Evidence used for retention and scoring

### NIHR510518

Trial evidence: patients? Research Plan We will research Histotripsy. We will do something called a clinical trial. A clinical trial is a type of experiment. It is really carefully planned so that we can answer the above questions. We will run the clinic

Design-point evidence: We will run the clinical trial in 6 hospitals in the UK.

Points: named lead 1; recent start 1; design 1.

### NIHR175280

Trial evidence: BACBONE: Bracing for spinal bone disease in newly diagnosed myeloma: A phase III randomised controlled trial

Design-point evidence: Methods: Phase III, Multicentre, randomised controlled trial with centralised spinal multidisciplinary team (MDT) eligibility review, national orthotics delivery and embed

Points: named lead 1; recent start 0; design 1.

### NIHR504024

Trial evidence: e clinical risk-scoring tools (Mayo and Brock models). We propose SWIFT-Lung: a prospective, stepped-wedge clinical trial across 3 NHS sites across England and Scotland (NHS Highlands, NHS Greater Glasgow and Clyde and Oxford University Hospitals). It will inco

Design-point evidence: WIFT-Lung: a prospective, stepped-wedge clinical trial across 3 NHS sites across England and Scotland (NHS Highlands, NHS Greater Glasgow and Clyde and Oxford University Hospitals).

Points: named lead 1; recent start 0; design 1.

### NIHR501826

Trial evidence: TarGeT (TARGETED PEDIATRIC HIGH-GRADE GLIOMA THERAPY) Phase 2 Umbrella Trial

Design-point evidence: (TARGETED PEDIATRIC HIGH-GRADE GLIOMA THERAPY) Phase 2 Umbrella Trial

Points: named lead 0; recent start 1; design 1.

### NIHR501825

Trial evidence: EPILOGUE- Phase I/II combination umbrella trial in relapsed pediatric low-grade glioma

Design-point evidence: EPILOGUE- Phase I/II combination umbrella trial in relapsed pediatric low-grade glioma

Points: named lead 0; recent start 1; design 1.

### NIHR172122

Trial evidence: PRostatEctomy Surgery In Disseminated metastatic hormone sensitive prostate cancer with Endpoint assessment using Nuclear imaging Technology using PSMA PET/CT: a randomised controlled full trial (PRESIDENT)

Design-point evidence: No qualifying phrase found; zero points.

Points: named lead 1; recent start 0; design 0.

### NIHR209472

Trial evidence: Prototype validation and exploratory first-in-human pilot of an implantable Electric Field Therapy device for recurrent glioblastoma: iterative clinical safety assessment (IDEAL 0/1 study)

Design-point evidence: No qualifying phrase found; zero points.

Points: named lead 1; recent start 0; design 0.

## Registry-link check

Exact award-ID query; no returned records in either registry. No recruitment status is inferred. A separate ISRCTN positive control (ISRCTN49306926) returned one record during QA, showing the public query endpoint responded to a known identifier.

Query: `NIHR501825 OR NIHR510518 OR NIHR172122 OR NIHR209472 OR NIHR504024 OR NIHR175280 OR NIHR501826`

- https://clinicaltrials.gov/api/v2/studies?query.term=NIHR501825+OR+NIHR510518+OR+NIHR172122+OR+NIHR209472+OR+NIHR504024+OR+NIHR175280+OR+NIHR501826&format=json&countTotal=true&pageSize=100
- https://www.isrctn.com/api/query/format/default?q=NIHR501825+OR+NIHR510518+OR+NIHR172122+OR+NIHR209472+OR+NIHR504024+OR+NIHR175280+OR+NIHR501826&limit=100

## Limits

- Project start dates are contract dates, not funding announcement or recruitment dates.
- NIHR metadata describes coverage to 31 March 2026; the file was modified in October and contains later contracted starts. Treat as a lagged funding snapshot, not all recent awards.
- Award values are original project funding, not unspent funds, software budgets or revenue available to Cori.
- Title filtering favours precision and misses cancer trials whose titles do not name the disease.
- Registry checks use exact identifiers, not fuzzy title matching; absent links do not mean unregistered or not yet recruiting.
- A funded project does not establish demand, procurement authority, current suppliers, or an intention to buy software.
- Named investigators are research contacts, not verified purchasing decision-makers. No email address is inferred.
- The host organisation postcode establishes UK hosting, not the countries of every trial site.

## Source retrieval audit

| Source request | Retrieved UTC | SHA-256 |
|---|---|---|
| [nihr-metadata.json](https://nihr.opendatasoft.com/api/explore/v2.1/catalog/datasets/nihr-summary-view) | 2026-11-25T18:44:23.597669+00:00 | `2ab45ab7bef7f32617c3029150fd12b8519849acbad0534a98b37d3c16bd1e3c` |
| [nihr-awards-2025-11-25.json](https://nihr.opendatasoft.com/api/explore/v2.1/catalog/datasets/nihr-summary-view/exports/json?where=start_date+%3E%3D+date%272025-11-25%27) | 2026-11-25T18:44:34.082102+00:00 | `4a7c7dba3f64459e34dd56860691ace1065119525e9a2373b02174df281199c7` |
| [ctgov-6dad3978d25a.json](https://clinicaltrials.gov/api/v2/studies?query.term=NIHR501825+OR+NIHR510518+OR+NIHR172122+OR+NIHR209472+OR+NIHR504024+OR+NIHR175280+OR+NIHR501826&format=json&countTotal=true&pageSize=100) | 2026-11-25T18:44:38.145349+00:00 | `b54968c05ff881a1ef7ce604b6a340248f8e2aee8637bef06da0f5693f520df8` |
| [isrctn-6dad3978d25a.xml](https://www.isrctn.com/api/query/format/default?q=NIHR501825+OR+NIHR510518+OR+NIHR172122+OR+NIHR209472+OR+NIHR504024+OR+NIHR175280+OR+NIHR501826&limit=100) | 2026-11-25T18:44:41.547515+00:00 | `9102345f60a6769cd03fb92d5a00f71c6bbfb597ba699e5f98161f95f657dfc6` |

## Excluded rows

| Award | Title | First exclusion reason |
|---|---|---|
| GHR CADA-R4-004 | Training Award | Training award, not a research project |
| NIHR305666 | Improving recruitment rates and participant diversity in clinical trials testing treatments for psychosis: a mixed methods study | Training award, not a research project |
| NIHR305956 | Predicting the Outcome of Pneumonia for People who Aspirate (PrOPPA) Study: Predicting the outcome of pneumonia for individuals who aspirate when eating and drinking as a result of oropharyngeal dysphagia:- determining the validity, reliability and acceptability of a prognostic clinical prediction model to support clinical management. | Training award, not a research project |
| NIHR306048 | Exploring the risk of aspiration and its influence on oral feeding decision-making in infants receiving Nasal High Flow respiratory support (NHF). | Training award, not a research project |
| NIHR306309 | Exploring how smoking cessation services delivered in pregnancy in England can produce equity promoting outcomes for underserved groups. | Training award, not a research project |
| NIHR306398 | Developing equitable, personalised community rehabilitation interventions for people with peripheral artery disease. | Training award, not a research project |
| NIHR306477 | Do the healthcare interventions we provide for hearing impairment and speech, language and communication difficulties in children born with cleft palate +/- lip impact on educational outcomes? | Training award, not a research project |
| NIHR306548 | A Proactive Integrated apprOach to ideNtifying and trEating people with COPD and “trEatable traits” in primary caRe (PIONEER COPD) | Training award, not a research project |
| NIHR306570 | A Complex intervention to Address Ethnic and Socioeconomic inequalities in Access to Elective and Acute procedural caRe for Coronary Artery Disease: CAESAR-CAD | Training award, not a research project |
| NIHR306571 | The role of artificial intelligence in improving the diagnosis of prostate cancer | Training award, not a research project |
| NIHR306582 | Developing safe conversational artificial intelligence for specialist NHS neurology services | Training award, not a research project |
| NIHR500016 | Childbirth, choice & climate change: reducing emissions while preserving pregnant people's autonomy | No explicit oncology term in the project title |
| NIHR500308 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500492 | A-PATH: Adapting Psychological Advocacy Towards Healing for older women affected by domestic abuse | No explicit oncology term in the project title |
| NIHR500582 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500728 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500882 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR500953 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500954 | Upscaling implementation of The Illicit Project UK | No explicit oncology term in the project title |
| NIHR500963 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR501060 | Realist evaluation of drug education for 13-15 year olds in alternative education and deprived areas | No explicit oncology term in the project title |
| NIHR501426 | Automating the diagnosis of small bowel biopsies: plugging the gap of gluten sensitivity | No explicit oncology term in the project title |
| NIHR501957 | The Brain Tumour Novel Therapeutics Consortium | Follow-up, synthesis or consortium rather than a discrete new trial |
| NIHR503225 | Investigating Feeding Outcomes and Improving Patient Care for Children with Long-Term Ventilation | Training award, not a research project |
| NIHR503467 | ACCelerate - Refinement and implementation of a rapid urine test for the detection of adrenal cancer | No explicit new interventional trial signal under the stated rule |
| NIHR503712 | Transforming Treatment for Young People with Tic Disorders: Scalable, Evidence-Based Digital Therapy | No explicit oncology term in the project title |
| NIHR504338 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR505305 | Developing and validating ‘Sia’: a responsible AI platform for dementia prediction | No explicit oncology term in the project title |
| NIHR505311 | Finding and Adapting methods of Inclusive Research (FAIR) | No explicit oncology term in the project title |
| NIHR505393 | The GALEAS™ Bladder genomic urine test for de-escalating surveillance in bladder cancer patients | No explicit new interventional trial signal under the stated rule |
| NIHR505717 | CORTEX Complication Recognition Through EHR and eXplainable AI | No explicit oncology term in the project title |
| NIHR505807 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR505822 | Bridging the Gap: Making MS Diagnosis and Care Equitable through AI-Driven MRI Analysis in the NHS | No explicit oncology term in the project title |
| NIHR506200 | Revitalise: Precise Robotic Delivery of Retinal Intravascular Therapies | No explicit oncology term in the project title |
| NIHR506237 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR506762 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR507040 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR507797 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508637 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508650 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508655 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508752 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508799 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508970 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509225 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509286 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509297 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509389 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509413 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509503 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509621 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509626 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509789 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509832 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509876 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509887 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR510135 | Clinical Validation of Resynk: Feasibility and Acceptability in Stroke Rehab from Hospital to Home | No explicit oncology term in the project title |
| NIHR510214 | AI-powered, faster, fairer Care Act assessments, reducing health and social inequalities | No explicit oncology term in the project title |
| NIHR510233 | Early detection of heart valve disease to prevent multi-morbidity - usability testing in pharmacies | No explicit oncology term in the project title |
| NIHR510260 | Economic evaluation of Suvera’s virtual clinics for managing long-term conditions in primary care | No explicit oncology term in the project title |
| NIHR510275 | Path Active: A Wearable System to Prevent Diabetes Foot Ulcers and the Burden on Community Teams | No explicit oncology term in the project title |
| NIHR510398 | Digital Therapy to Improve Stroke Communication, Prevent Co-Morbidities and Ease NHS Pressure | No explicit oncology term in the project title |
| NIHR510591 | Does Nelli for adults with Epilepsy and ID reduce admissions and workload and improve diagnosis | No explicit oncology term in the project title |
| NIHR510703 | CrossSense: feasibility for targeting psychosocial pathways to prevent multimorbidity in dementia | No explicit oncology term in the project title |
| NIHR510878 | Stopping pain’s spiral: Evaluating digital prevention of mental-health decline in chronic pain | No explicit oncology term in the project title |
| NIHR510879 | 10-minute point-of-care diagnostic for UTIs in care-homes to guide intervention before deterioration | No explicit oncology term in the project title |
| NIHR510915 | Feasibility study of PuntoCare: Digital support for dementia and MCI in NHS care settings | No explicit oncology term in the project title |
| NIHR517310 | Quantum PHIP Benchmarking for Clinical Translation | No explicit oncology term in the project title |
| NIHR517510 | Structured-light Photonic-chip-based OCT | No explicit oncology term in the project title |
| NIHR517860 | Quantum Singlet Oxygen Sensing for Photodynamic Therapy Dosimetry (Q-SOS) | No explicit oncology term in the project title |
| NIHR150375 | Weight Reduction in Asthma Programme with Tirzepatide (WRAPT): clinical efficacy and mechanisms of action. | No explicit oncology term in the project title |
| NIHR163709 | A Simplified screen-and-Treat-all prOphylaxis approach in Pregnant women to stop Hepatitis B Virus mother-to-child transmission in Malawi and The Gambia (STOP-HBV) | No explicit oncology term in the project title |
| NIHR164416 | Effective workplace learning environments in care homes: Developing, implementing and evaluating a model and implementation toolkit | No explicit oncology term in the project title |
| NIHR165852 | DIALS – DIAgnosis of Liver diseaSe in primary care | No explicit oncology term in the project title |
| NIHR167846 | The Impact of Housing Quality Retrofits on the Health and Well-Being of Older People: An Analysis of the English Longitudinal Study of Ageing | No explicit oncology term in the project title |
| NIHR168836 | A mixed methods realist evaluation of the MECSH parenting intervention investigating inequalities in access, engagement, retention and outcomes for birthing and non-birthing parents from Black and Asian communities in England. | No explicit oncology term in the project title |
| NIHR168885 | A phase 2 randomised clinical trial to evaluate the efficacy of anakinra in patients with the acute respiratory distress syndrome (AnakARDS) | No explicit oncology term in the project title |
| NIHR168901 | Trauma-focused therapy in early psychosis: A randomised controlled trial assessing the efficacy and mechanisms of action of Eye Movement Desensitization and Reprocessing for psychosis (EMDRp) in comparison to treatment as usual in Early Intervention Settings | No explicit oncology term in the project title |
| NIHR169106 | Randomised Placebo Controlled Trial of Intravenous Iron for Improving Physical Performance and Quality of Life in patients with Chronic Limb-Threatening Ischaemia and Anaemia Following Revascularisation | No explicit oncology term in the project title |
| NIHR169358 | Timing of Umbilical Cord Clamping for Preterm Infants Needing Resuscitation at Birth: The Opticord trial | No explicit oncology term in the project title |
| NIHR169738 | PanacEa Trial: Clinical and Cost-Effectiveness of Pain Management Programme for Endometriosis versus Standard Care | No explicit oncology term in the project title |
| NIHR169899 | Mortality, Disease Progression and Metastasis in the NIHR HTA Prostate testing for cancer and Treatment (ProtecT) trial: median 20-year follow up | Follow-up, synthesis or consortium rather than a discrete new trial |
| NIHR170105 | Second person checking of medication dispensing, preparation and administration in hospitals - what works for whom, in what contexts, and why? The CHECKMED realist evaluation study | No explicit oncology term in the project title |
| NIHR170324 | PINC2: A pragmatic, multi-centre, parallel-arm, double-blind, placebo-controlled, randomised controlled trial to evaluate the clinical effectiveness, cost effectiveness and safety of exogenous luteal phase progesterone support in natural menstrual cycles in couples with unexplained infertility. | No explicit oncology term in the project title |
| NIHR170347 | INGEST: dIscontinuing or continuiNG thickEned fluidS Trial | No explicit oncology term in the project title |
| NIHR170512 | Psychosocial interventions for military personnel with PTSD: A network meta-analysis | No explicit oncology term in the project title |
| NIHR170575 | A randomised trial of relugolix combination therapy versus usual medical treatment in the medical management of heavy menstrual bleeding (RESPONSIBLE) | No explicit oncology term in the project title |
| NIHR170973 | Co-production, refinement and evaluation of a model of psychosocial peer support and liaison with alcohol, liver and mental health services to improve quality of life and clinical outcomes for people with alcohol-related liver disease (CALM study) | No explicit oncology term in the project title |
| NIHR171615 | Listening with Unilateral versus bilateral Cochlear Implants in Adults (LUCIA): A randomised controlled trial comparing simultaneous bilateral versus unilateral cochlear implantation in adults with post-lingual severe-profound hearing loss | No explicit oncology term in the project title |
| NIHR174105 | Identifying and evaluating policy mechanisms to reduce ultra-processed food consumption in the UK: health, equity and economic impacts (The UPForesight Project) | No explicit oncology term in the project title |
| NIHR174857 | Health Effects fRom Infection sequelae: Tailoring services and Advancing GuidancE (HERITAGE) in Long Covid and Myalgic Encephalomyelitis/Chronic Fatigue Syndrome | No explicit oncology term in the project title |
| NIHR174875 | GOLDFINCH (Fiscal INCentives for Health through UPF reduction) | No explicit oncology term in the project title |
| NIHR175072 | Lowering Adverse outcomes in Pilonidal sinus: Trial of fIbrin glue vs Minimal Excision. [PITSTOP2] | No explicit oncology term in the project title |
| NIHR177941 | A Rapid Evaluability Assessment of the Future of Prevention Programme in adult social care services (REAP) | No explicit oncology term in the project title |
| NIHR206684 | Developing a perinatal mental health peer support intervention to address the needs of women with experience of intimate partner violence (IPV): a qualitative study | No explicit oncology term in the project title |
| NIHR207682 | Meeting the needs of children and young people (0-18) with Special Educational Needs and/or Disabilities: modelling the Allied Health Professional therapy workforce within integrated children’s services. | No explicit oncology term in the project title |
| NIHR207915 | An open-label, multi-centre, randomised controlled trial to assess the efficacy, safety and utility of automated insulin delivery (AID) in people with type 2 diabetes and sub-optimal glycaemia undergoing haemodialysis | No explicit oncology term in the project title |
| NIHR207980 | Long-term Follow-Up for chronic rhinosinusitis patients in the MACRO Trial: MACRO PLUS | No explicit oncology term in the project title |
| NIHR207989 | Sustaining the introduction of health and well-being coaches in multi-disciplinary primary care teams to support underserved populations: Developing recommendations and guidance for patients, coaches, and primary care staff | No explicit oncology term in the project title |
| NIHR208161 | Supporting airway clearance in the community for people living with a neuromuscular disorder | No explicit oncology term in the project title |
| NIHR208182 | EMPoWER Effectiveness of a Multi-modal intervention to Promote Independence and WEllbeing among oldeR adults of South Asian heritage: a feasibility study | No explicit oncology term in the project title |
| NIHR208366 | Extending the Mental Health Intervention for Children with Epilepsy (MICE) Programme | No explicit oncology term in the project title |
| NIHR208610 | Supporting Reunification: Learning from Applied Research | No explicit oncology term in the project title |
| NIHR208611 | Older men's experiences of self-neglect and hoarding and engagement with local authority social care services and support (OMESH study) | No explicit oncology term in the project title |
| NIHR208632 | Developing reproductive health support to prevent early and unplanned pregnancy among care experienced young people | No explicit oncology term in the project title |
| NIHR208762 | Improving recognition and treatment of adult onset type 1 diabetes though though rational cost-effective classification biomarker testing | No explicit oncology term in the project title |
| NIHR208806 | Comparative efficacy and reproductive outcomes after fertility-sparing treatment for endometrial hyperplasia, with or without atypia, and early endometrial cancer: synthesis of the evidence and network meta-analysis | Follow-up, synthesis or consortium rather than a discrete new trial |
| NIHR208816 | Montelukast and Neuropsychiatric Events: A target trial emulation to quantify adverse reactions and measure the impact of regulatory action | No explicit oncology term in the project title |
| NIHR209111 | Socially Connected SmartCare at home: Enhancing independent living for people living with dementia through low-cost technology | No explicit oncology term in the project title |
| NIHR209114 | Adapting the Parent Report of Children’s Abilities-Revised (PARCA-R) questionnaire: Improving research inclusion and access to healthcare services for families with limited English literacy. | No explicit oncology term in the project title |
| NIHR209135 | Improving the Experience of Care for people prescribed Medications with a risk of Dependence or withdrawal in prison: The ECMD-prisons study. | No explicit oncology term in the project title |
| NIHR209137 | Co-evolving proactive telecare in practice | No explicit oncology term in the project title |
| NIHR209169 | Co-design of a toolkit for Integrated Care Systems to support primary care healthcare professionals to deprescribe unnecessary antidepressants: A behavioural science realist approach | No explicit oncology term in the project title |
| NIHR209189 | Effect of immuno-nutrition on markers of sarcopenia and systemic inflammation in a haemodialysis population: a feasibility randomised controlled trial. | No explicit oncology term in the project title |
| NIHR209194 | Measuring and Assessing the Risk of hospital-associated Venous thromboEmbolism in peopLe admitted to Mental Health hospitals (MARVEL-MH) | No explicit oncology term in the project title |
| NIHR209200 | Qualitative exploration of the specific sexual and relational support needs of young people with Inflammatory Bowel Disease: co-design of an evidence-based, prototype intervention | No explicit oncology term in the project title |
| NIHR209233 | The impact and cost-effectiveness of enhanced primary care for people experiencing homelessness in Liverpool | No explicit oncology term in the project title |
| NIHR209251 | Improving safety and TReatment precision for Acute COPD Exacerbations: Feasibility trial of a primary care assessment pathway using point-of-care testing (TRACE). | No explicit oncology term in the project title |
| NIHR209258 | Developing a prototype toolkit for the practical and effective evaluation of the integrated care delivered by neighbourhood multi-disciplinary teams for children and young people | No explicit oncology term in the project title |
| NIHR209260 | Culturally adapted psychoeducation for African and Caribbean persons with bipolar disorder in the UK: A feasibility study | No explicit oncology term in the project title |
| NIHR209293 | Development and clinical validation of a 2nd generation rapid blood test with improved usability and performance for identification of stroke patients eligible for emergency thrombectomy treatment. | No explicit oncology term in the project title |
| NIHR209366 | Envirolieve final phase development, regulatory approval and clinical evaluation: reducing the carbon impact of Entonox through patient-centred innovation. | No explicit oncology term in the project title |
| NIHR209367 | National Research Programme on WHISPAs - workplace health and wellbeing initiatives that are free at the point of use to workplaces | No explicit oncology term in the project title |
| NIHR209391 | Development of PD PREDICT a prognostic blood based test for Parkinsons Disease | No explicit oncology term in the project title |
| NIHR209444 | HOLO-AIM : Holographic surgical guidance using Artificial Intelligence and Mixed reality for safer and more efficient Surgery | No explicit oncology term in the project title |
| NIHR209589 | The development and evaluation of a self-managed digital PROSPER (Prevention of Shoulder Problems) exercise and education programme for patients undergoing breast cancer treatment: increasing reach and uptake through digital technology | No explicit new interventional trial signal under the stated rule |
| NIHR209618 | Cardiac Surgery Aftercare and Recovery Evaluation (CARE) | No explicit oncology term in the project title |
| NIHR209668 | Feasibility of Body Identical Progesterone for treatment of endometriosis pain (BIP-4) | No explicit oncology term in the project title |
| NIHR209858 | Evaluating allergy status following peanut oral immunotherapy in the NATASHA Randomised Controlled Trial | No explicit oncology term in the project title |
| NIHR208568 | Relational approach to working with young people who self-harm (RELATE-YP): A Feasibility Trial | No explicit oncology term in the project title |
| NIHR208593 | Improving policy and practice to promote and protect the emotional well-being of Unaccompanied Asylum Seeking Young People leaving care in England | No explicit oncology term in the project title |
| NIHR208603 | Co-located nurseries in care homes: exploring the impact of intergenerational practices on residents with dementia | No explicit oncology term in the project title |
| NIHR208620 | Apni Jung (our fight) against rheumatoid arthritis; fEasibility of an online Learning patient Education programme for improVing outcomes in pAtients from a minority eThnic background in England (ELEVATE) | No explicit oncology term in the project title |
| NIHR208711 | Treating Unhelpful Suspicious Thoughts in teenagers (TRUST): A schools-based feasibility randomised controlled clinical trial for adolescents (16-18 years) with elevated paranoia | No explicit oncology term in the project title |
| NIHR208760 | A feasibility multicentre randomised controlled trial on miCRosurgical immediate lYmPhaTIC reconstruction to reduce risk of lymphoedema (CRYPTIC trial) | No explicit oncology term in the project title |
| NIHR209129 | Building effective digital post-hospital discharge and reablement services for older adults in social care: a mixed methods process evaluation using the NASSS framework | No valid UK host postcode |
| NIHR209140 | Leveraging Generative AI to Support People with Learning Disabilities in Their Daily Lives | No explicit oncology term in the project title |
| NIHR209170 | Co-design a Trauma Informed Care Intervention In Inpatient Mental Health Settings For Adults: Intervention Development | No explicit oncology term in the project title |
| NIHR209198 | Exploring risks for women who have a pregnancy after bariatric surgery to inform pregnancy and postnatal care needs | No explicit oncology term in the project title |
| NIHR209212 | Raman spectral imaging of surgical margins of basal cell carcinoma (BCC) treated by standard local excision | No explicit new interventional trial signal under the stated rule |
| NIHR209219 | The co-creation and feasibility of a Health Visitor-led intervention, combining group exercise and behavioural activation approaches, which can be tailored for mothers at risk of postnatal depression | No explicit oncology term in the project title |
| NIHR209231 | Enhancing Empathy in Digital Consultations for Everyone (E-DiCE): Smiling through Digital Media | No explicit oncology term in the project title |
| NIHR209270 | Feasibility and acceptability of a remote community exercise and lifestyle change intervention in patients with smaller abdominal aortic aneurysms | No explicit oncology term in the project title |
| NIHR209321 | PRevention of Osteoporotic fractures Through Equitable Case finding and Treatment Support (PROTECTS) | No explicit oncology term in the project title |
| NIHR209378 | OnchyMed: A First In Class Medical Device For Onychomycosis | No explicit oncology term in the project title |
| NIHR209408 | A software system for measuring hip displacement in children with cerebral palsy frompelvic radiographs | No explicit oncology term in the project title |
| NIHR209490 | CARE-PAC: The Care and Support System for Patients and Carers receiving palliative and end-of life-care | No explicit oncology term in the project title |
| NIHR209611 | Improving care for people prescribed gabapentinoids for persistent pain: building on the PROMPPT approach. | No explicit oncology term in the project title |
| NIHR209840 | Assessing feasibility/acceptability of the Veteran Connection Programme (and trial) to enhance mental health amongst military veterans through social connectedness. | No explicit oncology term in the project title |
| NIHR209910 | Exploring the acceptability, adoption and appropriateness of alcohol screening and brief intervention (ASBI) in perinatal mental health services (ADAPT) | No explicit oncology term in the project title |
| NIHR305070 | Training Award | Training award, not a research project |
| NIHR305511 | Co-Design and Implementation of a Digital Self-Care Intervention to Improve Sexual and Reproductive Health among Youth in Zimbabwe (CoDe study) | Training award, not a research project |
| NIHR305556 | Pathways to equitable stroke care in Sierra Leone and South Africa | Training award, not a research project |
| NIHR306044 | Sedation from Antipsychotics (SoFA) | Training award, not a research project |
| NIHR306314 | An Economic Model and Ethical Guide for Local Authority Investment in Social Connectedness to Prevent Care Needs | Training award, not a research project |
| NIHR306356 | A Personalised Approach to breathing support Treatments in sick CHildren (PATCH) | Training award, not a research project |
| NIHR306468 | Co-development of a culturally and contextually sensitive community-based intervention to promote health and wellbeing in the asylum seeking and refugee community. | Training award, not a research project |
| NIHR306568 | “You’ve got to decide whether that’s worth it” – How can healthcare services better support older people and their families deciding whether or not to start potentially life-extending treatments? | Training award, not a research project |
| NIHR306606 | Making clinical trials more inclusive by using behavioural science to improve communication: COMMCLUSIVE | Training award, not a research project |
| NIHR306633 | Training Award | Training award, not a research project |
| NIHR306655 | NIHR Team Science Award | Training award, not a research project |
| NIHR500361 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500423 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500485 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500519 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500545 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500576 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500764 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500924 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR501255 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR502232 | PharmaBag: A Sustainable Packaging System to Reduce Pharmaceutical Waste and Support a Net-Zero NHS | No explicit oncology term in the project title |
| NIHR502941 | Optimising footcare interventions for older adults living in care homes (OPINIONS) | No explicit oncology term in the project title |
| NIHR504156 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR504253 | Caffeine for Neuroprotection in Birth-Related Brain Injury | Training award, not a research project |
| NIHR504616 | AI-enabled ECG to reduce demand for echocardiography and shorten diagnostic waiting lists | No explicit oncology term in the project title |
| NIHR504861 | Systematic Assessment of Medical Utility of Radiology Artificial Intelligence - CT Head (SAMURAI-CT) | No explicit oncology term in the project title |
| NIHR506093 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR506326 | MyoCaid: A ventricular assist device for myocardial recovery | No explicit oncology term in the project title |
| NIHR506442 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR507502 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507745 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507753 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507769 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507773 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507799 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507820 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507946 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508398 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508520 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508530 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508585 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508612 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508651 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508987 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509083 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509303 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509372 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509488 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509507 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509577 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509653 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509890 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR510264 | From Frailty to Independence: Implementing a Digital Strength and Balance Platform in Care Homes | No explicit oncology term in the project title |
| NIHR510302 | Preventing progression to multimorbidity by digitising the psoriasis care pathway | No explicit oncology term in the project title |
| NIHR510342 | Do sensory rewards for heel strike reduce tip toe walking in young people | No explicit oncology term in the project title |
| NIHR510403 | INCLUDE-CKD: INCLUsive Digital carE for Chronic Kidney Disease | No explicit oncology term in the project title |
| NIHR510557 | Feasibility and acceptability of Recallify for self-management after brain injury | No explicit oncology term in the project title |
| NIHR510810 | BloodTrackR Usability and Concordance | No explicit oncology term in the project title |
| NIHR510816 | Preventing co-morbidity in paediatric insomnia: a community nurse-supported, home-based solution | No explicit oncology term in the project title |
| NIHR510823 | Early Digital CST for Dementia: Detecting Cognitive Decline to Prevent Frailty and Falls | No explicit oncology term in the project title |
| NIHR512373 | Effectiveness, implementation and sustainability of Open Access Mental Health Support in Wales | No explicit oncology term in the project title |
| NIHR517284 | Quantum-enabled wearables for the diagnosis of consciousness in anaesthesia and PDoC | No explicit oncology term in the project title |
| NIHR517770 | Quantum enabled neuromodulation for memory enhancement | No explicit oncology term in the project title |
| NIHR519992 | Rose NET evaluation of the Prevention Accelerators | No explicit oncology term in the project title |
| NIHR521259 | The Use of Artificial Intelligence to Support Triage and Navigation in the NHS: a multi-method, rapid evaluation | No explicit oncology term in the project title |
| NIHR152515 | A multicomponent evaluation of new restrictions on marketing of less healthy foods in England | No explicit oncology term in the project title |
| NIHR163838 | East Africa AMR-STOP: Strategies for Tackling, Optimising and Preventing Environmental AMR (AfricaAMR-STOP) | No explicit oncology term in the project title |
| NIHR167384 | General Practice Additional Healthcare Professional (AdHP) Workplace-Based Learning (WPBL): A Realist Review with SWAR and Appreciative Inquiry to Co-Produce, Implement and Evaluate an AdHP-WPBL General Practice Toolbox. Short Title: 'GAP LEAP' | No explicit oncology term in the project title |
| NIHR168786 | NIAMR: Developing and Evaluating a National Integrated Digital Data Capture and Sharing Platform for Enhanced Detection and Monitoring of Antimicrobial Resistance to Improve One Health AMR Surveillance and Management in Uganda | No valid UK host postcode |
| NIHR169047 | A cluster randomized controlled trial of the clinical and cost effectiveness of Facilitated Access to Mutual Aid for adults with problem alcohol and drug use (FAMA). | No explicit oncology term in the project title |
| NIHR169375 | Comparison of high frequency JET ventilation Versus conventional Intermittent Positive pressure ventilation on the effectiveness of catheter ablation for Atrial Fibrillation: a multicentre, double blinded, randomised controlled trial (JET-VIP AF) | No explicit oncology term in the project title |
| NIHR169529 | Improving Social Recovery in Psychosis (ISRIP): a definitive randomised controlled trial and process evaluation of Social Recovery Therapy compared to treatment as usual for people with psychosis and severe social disability | No explicit oncology term in the project title |
| NIHR169769 | STRategies for the Identification, enrolment, attendance and retention of families into parenting interVentions in Early life (STRIVE) | No explicit oncology term in the project title |
| NIHR169789 | Process and outcomes evaluation of the NIHR Public Health Intervention Responsive Studies Teams (PHIRST) Scheme | No explicit oncology term in the project title |
| NIHR170057 | Accelerated cardiovascular magnetic resonance for the detection of coronary artery disease – a randomised controlled trial (ACCELERATE-CMR) | No explicit oncology term in the project title |
| NIHR170552 | Supracondylar elbow fracture management in children - the SUPRAMAN study | No explicit oncology term in the project title |
| NIHR170907 | REgression in Left ventrIcular hypErtrophy and Fibrosis in Aortic Stenosis – a randomised controlled trial (RELIEF-AS) | No explicit oncology term in the project title |
| NIHR171489 | A sequential mixed method study to investigate, understand and find co-produced solutions to the use of restrictive practices in health settings when caring for children and young people with eating disorders. | No explicit oncology term in the project title |
| NIHR174395 | Evaluating the implementation and uptake of Waking Saliva Cortisone: a new home-based test for Adrenal Insufficiency | No explicit oncology term in the project title |
| NIHR174677 | Strengths-based, low caseload approach to integrated health, housing and practical support for people experiencing homelessness with multiple complex needs in temporary shelters (hostels): a cluster randomised controlled trial [REACH trial] | No explicit oncology term in the project title |
| NIHR174726 | Creating Active Schools: investigating sustained implementation and long-term (cost)effectiveness on children’s physical activity in multi-ethnic and socioeconomically challenged communities in Bradford. | No explicit oncology term in the project title |
| NIHR174753 | SHIFTS-UPF: Study on Health Impacts of Food Taxes and Subsidies affecting Ultra Processed Food | No explicit oncology term in the project title |
| NIHR175082 | Acetabular Fractures in older patients Intervention Trial - Global (AceFIT-G) | Outside the past-year project-start window |
| NIHR177982 | FORGE: Future-Oriented Reform of Generalist Education Evaluation | No explicit oncology term in the project title |
| NIHR178000 | Public health strategies for first-episode psychosis: a systematic review of interventions and modifiable influences. | No explicit oncology term in the project title |
| NIHR207923 | Care bundle to improve postnatal care of women with hypertensive disorders of pregnancy for cardiovascular disease risk reduction (BundleCardio) | No explicit oncology term in the project title |
| NIHR208084 | A mixed-methods study of the physical and psycho-cognitive effects of Chimeric Antigen Receptor T-cell (CAR-T) therapy, in UK adults and their caregivers, over time. | No explicit oncology term in the project title |
| NIHR208140 | Single-test accuracy study to assess the diagnostic value of faecal calprotectin to diagnose necrotising enterocolitis in infants with heart defects | No explicit oncology term in the project title |
| NIHR208168 | Seeking Safety group intervention for complex post-traumatic stress disorder: a feasibility randomised controlled trial | No explicit oncology term in the project title |
| NIHR208186 | Temperature monitoring and mapping in ground emergency medical services (GEMS) and the Emergency Department: an observational study measuring thermal insults to patients, staff, drugs and equipment | No explicit oncology term in the project title |
| NIHR156271 | Faecal Transplantation for Alcohol-Related Hepatitis | No explicit oncology term in the project title |
| NIHR162467 | Efficacy, optimal targeting and mechanisms of a video feedback parent-infant intervention for mothers and birthing persons with severe or complex non-psychotic perinatal mental illness. | No explicit oncology term in the project title |
| NIHR165594 | Antifungals - Stopping Early with a Fungal Biomarker-based Stewardship Algorithm in Critical Care. (The A-Stop 2 Trial) | No explicit oncology term in the project title |
| NIHR168411 | Communication and Skills Intervention with Fathers (COSIE): A feasibility study | No explicit oncology term in the project title |
| NIHR169017 | SCHEMA-Uganda: Strengthening Community Health and Epidemic Management in Uganda | No valid UK host postcode |
| NIHR169127 | STEPFORWARD: A randomised controlled trial and economic evaluation of the impact of a hydraulic self-aligning ankle-foot on quality of life for patients with a below-knee amputation who have limited mobility | No explicit oncology term in the project title |
| NIHR170211 | RECOGNISED - RandomisEd controlled trial of COntinuous Glucose MoNItoring in the management and diagnosiS of GEstational Diabetes Mellitus - a multi centre randomised trial | No explicit oncology term in the project title |
| NIHR170284 | A randomised placebo-controlled superiority trial of GLP-1 receptor agonist for the treatment of alcohol use disorder in people with chronic liver disease and obesity: Controlling Unhealthy Relationships with Both alcohol and obesity (CURB trial) | No explicit oncology term in the project title |
| NIHR171124 | Stopping or continuing RAS-inhibitor drugs before major elective non-cardiac surgery: SPACE II trial | No explicit oncology term in the project title |
| NIHR171964 | Multimodal prehabilitation for frail patients undergoing total hip and knee replacement: The Joint PREP randomised controlled trial | No explicit oncology term in the project title |
| NIHR173127 | Development and evaluation of adapted cognitive behaviour therapy for social anxiety disorder in autistic adults: a cluster randomised controlled trial | No explicit oncology term in the project title |
| NIHR173364 | Natural Experimental Evaluation of increasing the Minimum Unit Price for alcohol in Scotland to 65p (NEEMUP65) | No explicit oncology term in the project title |
| NIHR174159 | A mixed methods realist evaluation and economic appraisal of how health screening, education and prevention interventions in mosques impact the health and wellbeing of Muslim communities. | No explicit oncology term in the project title |
| NIHR174454 | Mapping and realist evaluation of Lived Experience Recovery Organisations as part of the drug and alcohol treatment and recovery System in England (LEROS) | No explicit oncology term in the project title |
| NIHR174496 | Evaluation of a virtual ward programme versus standard of care for patients with acute COPD exacerbations | No explicit oncology term in the project title |
| NIHR174567 | Empowering workplace self-management for individuals with long-term health conditions and health-related disabilities: a randomised controlled feasibility trial of the 'Co-Manage' intervention compared with usual workplace support. | No explicit oncology term in the project title |
| NIHR174675 | Evaluating the mental health-related outcomes of food bank advice services for people with unmanageable debt who are in or near destitution | No explicit oncology term in the project title |
| NIHR174974 | Enhancing Reproductive Health in Women’s Prisons: Evidence to Inform Equitable, Person-Centred Care | No explicit oncology term in the project title |
| NIHR203637 | Image guided laparoscopic liver resection: a feasibility randomised controlled trial | No explicit oncology term in the project title |
| NIHR208155 | Feasibility of a Community-Based Aquatic Exercise and Peer Support Intervention (Good Boost+) for Adults on Knee Replacement Waiting Lists: A Randomised Hybrid Type 1 Effectiveness-Implementation Feasibility Trial | No explicit oncology term in the project title |
| NIHR208596 | Waiting Well in Social Care | No explicit oncology term in the project title |
| NIHR208655 | A qualitative investigation of the barriers and facilitators to managing hearing loss for older adults living with frailty | No explicit oncology term in the project title |
| NIHR208758 | Managing Treatment eXperience (MTX): Developing psychoeducational resources for children with rheumatic conditions who are taking methotrexate | No explicit oncology term in the project title |
| NIHR208812 | Targeting interventions to optimise school-age outcomes for children with hearing loss in a population with new-born screening | No explicit oncology term in the project title |
| NIHR208880 | Personalised prevention of breast cancer in people at moderate or high risk– a new approach to optimising prevention in primary care. | No explicit new interventional trial signal under the stated rule |
| NIHR208889 | Implementation of Day-case Hip and Knee Arthroplasty ensuring Optimal Patient Experience and Outcomes.(IDAPO) | No explicit oncology term in the project title |
| NIHR209101 | A Realist synthesis and evaluation of how mainstream smart home technologies can support independent living for disabled people: understanding what works for whom, in what circumstances, and why | No explicit oncology term in the project title |
| NIHR209117 | Turn down the noise: Reducing noise and supporting people with dementia and hearing loss in social care settings | No explicit oncology term in the project title |
| NIHR209121 | Embedding TEchnology in Care Homes (ETECH) | No explicit oncology term in the project title |
| NIHR209142 | Using Artificial Intelligence to Improve the Use of Evidence in Social Work Practice: A Rapid-Cycle Development Project | No explicit oncology term in the project title |
| NIHR209197 | ASSIST: A randomised feasibility trial to assess the Acceptability of a remouldable Socket System in the Immediate rehabilitation phase of people with a tranSTibial amputation | No explicit oncology term in the project title |
| NIHR209225 | Modelling the cost-effectiveness of early term induction of labour to prevent shoulder dystocia for fetuses suspected to be large for gestational age and/or macrosomic (Big Baby 3) | No explicit oncology term in the project title |
| NIHR209547 | Prison, resettlement and domestic abuse: a qualitative study to explore women's experiences and needs to enhance practice and policy | No explicit oncology term in the project title |
| NIHR209564 | Feasibility RCT of the serious game ‘Broodles’ for siblings of children with learning disabilities | No explicit oncology term in the project title |
| NIHR209588 | Novel Integrated Health and Social Care Data Enabling Earlier Detection of COPD and Intervention Delivery Through Optimised Care Pathways | No explicit oncology term in the project title |
| NIHR209602 | Co-development of ‘Kangaroo Mother Care’ interventions in NHS hospitals to improve breastfeeding for infants born late preterm | No explicit oncology term in the project title |
| NIHR209613 | Informing the Design of a Computerised Decision Support Tool for Falls Risk Assessment: Exploring Modifiable Risk Factors and Data Availability in Acute Hospitals | No explicit oncology term in the project title |
| NIHR209751 | The association between prescribed hormonal contraception and the risk of MS in England. | No explicit oncology term in the project title |
| NIHR209765 | MINDS: Intervention for identifying mental health problems in autistic/ADHD adults in primary care | No explicit oncology term in the project title |
| NIHR209767 | Supporting the Mental Health of Children through Stix Innovation: A Feasibility Trial | No explicit oncology term in the project title |
| NIHR305959 | Better assessment of post-traumatic stress in autistic adults | Training award, not a research project |
| NIHR306060 | Current guideline-based care supported by a physiotherapist versus provision of a high-quality information leaflet and a single advice session delivered by a physiotherapist for people with shoulder osteoarthritis: A pilot randomised controlled trial with embedded qualitative study. | Training award, not a research project |
| NIHR306062 | COMPANION: Co-production of a decision tool for people with advanced cancer considering home parenteral nutrition | Training award, not a research project |
| NIHR306078 | The Co-Development and Feasibility of an Interstitial Lung Disease (ILD) Fatigue and Breathlessness (‘FAB’) Programme using the Medical Research Council (MRC) Framework for Complex Interventions: A Theory-Based, Mixed-Method Study | Training award, not a research project |
| NIHR306430 | DEPrescribing In peopLe Living with advanced Chronic Kidney Disease (DEPILL-CKD): understanding patterns and outcomes | Training award, not a research project |
| NIHR306615 | Emergency Department Coding Practices for People in Suicidal Crisis. | Training award, not a research project |
| NIHR306656 | NIHR Team Science Award | Training award, not a research project |
| NIHR306699 | Training Award | Training award, not a research project |
| NIHR500096 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR500143 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR500283 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500312 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500359 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500427 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500437 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500477 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500556 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500579 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500636 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500665 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR500716 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR501279 | Treating auditory impairment to preserve cognition in people with mild cognitive impairment | No explicit oncology term in the project title |
| NIHR501324 | NIHR Predoctoral Award | Training award, not a research project |
| NIHR502152 | WP1 - Adult Early Phase 5G platform | No explicit oncology term in the project title |
| NIHR502893 | CHOICES-HI: Hospital-Initiated Social Prescribing for Children and Young People | No explicit oncology term in the project title |
| NIHR503119 | Can imaging of airway dynamics optimise assisted coughing in children with spinal muscular atrophy? | Training award, not a research project |
| NIHR503216 | Developing MRI Epilepsy Lesion Detection (MELD) software for clinical use | No explicit oncology term in the project title |
| NIHR503515 | Intelligent Navigation using AI to bust waiting times for urgent healthcare (INA) | No explicit oncology term in the project title |
| NIHR504295 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR504569 | Scalable Medical AI for Radiology Transformation – X-Ray (SMART-XR) | No explicit oncology term in the project title |
| NIHR506276 | NIHR Development and Skills Enhancement Award (DSE) | Training award, not a research project |
| NIHR507050 | Community Appointment Days vs Standard Physiotherapy for People with a Musculoskeletal Condition | No explicit oncology term in the project title |
| NIHR507548 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507550 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507552 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507763 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507775 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR507846 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508648 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508848 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508866 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR508980 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509078 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509126 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509200 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509569 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509673 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR509688 | NIHR Senior Investigators (SI) | Training award, not a research project |
| NIHR510229 | AI‑Augmented Falls & Frailty Prevention Pathway (AIFP) | No explicit oncology term in the project title |
| NIHR510280 | Summative Usability Study of Sensore: pressure ulcer monitoring & prevention for wheelchair users | No explicit oncology term in the project title |
| NIHR510479 | Community Prehabilitation for Cancer: Validating an Adaptive Symptom Tracker within PreActiv | No explicit new interventional trial signal under the stated rule |
| NIHR510643 | Jam Up!: health economic and health inequality impacts | No explicit oncology term in the project title |
| NIHR510914 |  | No explicit oncology term in the project title |
| NIHR514756 | FOCUS-NHS: A Framework for mOnitoring and improving Clinical Use of bioSimilars across the NHS | No explicit oncology term in the project title |
| NIHR517225 | Quantum Imaging with Undetected Photons for Breast Cancer Treatment Decision Support | No explicit new interventional trial signal under the stated rule |
| NIHR517237 | Detection of sleep states using machine learning in optically pumped magnetoencephalography | No explicit oncology term in the project title |
| NIHR517481 | Quantum sensing to detect neurophysiological signatures of early Alzheimer’s disease | No explicit oncology term in the project title |
| NIHR517586 | Quantum OCT For Home & Community Based Imaging Of Children's Eyes | No explicit oncology term in the project title |
| NIHR517606 | Precise Detection of High-Risk Chronic Liver Disease using Diamond Quantum Sensing | No explicit oncology term in the project title |
| NIHR517626 | Quantum-enabled Single-cell Mitochondrial Sensing for Rheumatoid Arthritis Therapy Stratification | No explicit oncology term in the project title |
| NIHR177965 | Transfer and Implementation of New Beginnings - Stockport to Tameside | No explicit oncology term in the project title |
