# S1-04 Build inputs: data, simulators, code, devices, protocols, test methods (agent: claude-opus-5-5, 2026-11-13)

## Digest
(written last)

## Findings

Method note: GitHub repo existence, licence (SPDX id from the GitHub API `license` field) and "last push" date were checked live on 2026-11-13 via `https://api.github.com/repos/OWNER/REPO` (OPENED, API). "Last push" = most recent push to any branch, not a release date. NOASSERTION = GitHub could not classify the licence file; read it before reuse.

### Q1. Public datasets

| Dataset | What | Size | Licence | Access | Source (OPENED unless noted) |
|---|---|---|---|---|---|
| CGMacros v1.0.0 (PhysioNet) | 45 adults: 15 healthy, 16 prediabetes, 14 type 2; Libre Pro + Dexcom G6 Pro CGM, Fitbit Sense, meal macros + photos, 1-min data, labs, microbiome | 627.9 MB | CC BY-NC-SA 4.0 | Open, instant | https://physionet.org/content/cgmacros/ (published 28 Jan 2025; DOI 10.13026/3z8q-x658) |
| ShanghaiT1DM / ShanghaiT2DM | 12 T1D + 100 T2D, Shanghai, real life; CGM 3 to 14 days, diet, medications, labs | not stated | "publicly available for research purposes" (abstract); hosted with the Sci Data paper (figshare) | Open per paper; host not re-checked | Sci Data 2023;10:35, PMID 36653358, DOI 10.1038/s41597-023-01940-7, via Europe PMC https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Chinese%20diabetes%20datasets%22 (19 Jan 2023). Only open T2D CGM set found with oral-drug + insulin records |
| OhioT1DM | 12 T1D on pump + CGM, 8 weeks each; CGM 5-min, fingersticks, basal/bolus, meals, exercise, sleep, stress, fitness band | n/a | DUA implied (encrypted file) | NEEDS APPLICATION: email from institutional address, "allow one week" | https://webpages.charlotte.edu/rbunescu/data/ohiot1dm/OhioT1DM-dataset.html (undated) |
| D1NAMO v1.2.0 | 20 healthy + 9 T1D; Zephyr BioHarness ECG, breathing, accelerometer, glucose, annotated food photos | ~10.2 GB (6 zips) | CC BY-SA 4.0 | Open, instant (Zenodo) | https://zenodo.org/records/5651217 (published 19 Oct 2018) |
| HUPA-UCM | 25 T1D; FreeStyle Libre 2 CGM, insulin, carbs, Fitbit Ionic (steps, HR, sleep) | not stated | CC BY 4.0 | Open ("Download All") | https://data.mendeley.com/datasets/3hbcscwz44/1 (25 Apr 2024, DOI 10.17632/3hbcscwz44.1) |
| AI-READI (v3.0.0 current; v2 withdrawn) | People with and without T2DM, 3 US sites, wearables + glucose + eye imaging; enrollment ongoing | not stated | named licence not shown on doc page | NEEDS REGISTRATION + licence agreement on FAIRhub; controlled part needs DUA | https://docs.aireadi.org/docs/3/about (doc updated 29 Oct 2026) |
| Pulse Transit Time PPG v1.1.0 (PhysioNet) | 22 healthy, sit/walk/run; ECG, 6 PPG channels, accel; cuff BP (OMRON HEM-7322) start/end | 2.9 GB | ODbL 1.0 | Open, instant | https://physionet.org/content/pulse-transit-time-ppg/ (18 Mar 2022) |
| PulseDB v2.0 | 10-s ECG+PPG+arterial BP segments from MIMIC-III + VitalDB, 5,361 .mat files, for cuffless-BP benchmarking | large (Box/Drive/OneDrive/Kaggle) | MIMIC part ODbL 1.0; VitalDB part CC BY-NC-SA 4.0 | Open links, no login stated | https://github.com/pulselabteam/PulseDB (last push 2024-06-13); paper Front Digit Health 2023, DOI 10.3389/fdgth.2022.1090854 |
| PPG-BP Database (Guilin, China) | Short finger PPG + cuff BP per subject, Sci Data 2018 (sdata201820); subject count not re-checked | 1.5 MB zip | CC0 | Open, instant | figshare API https://api.figshare.com/v2/articles/5459299 (record modified 22 Sep 2022) |
| WESAD | 15 subjects, lab stress protocol; RespiBAN chest (ECG, EDA, EMG, resp, temp, acc, 700 Hz) + Empatica E4 wrist (BVP 64 Hz, EDA, temp, acc) | not stated on UCI | not stated on UCI page; see original site | Linked from UCI (ID 465), loadable with `ucimlrepo` | https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection (2018). Stress, not chronic disease |
| Hall 2018 "Glucotypes" | 57 recruited, 30 with standardised meals; Dexcom G4, 2 to 4 weeks, mostly non-diabetic/prediabetic | small | PLoS (CC BY) supplement | Open: "available as S1 Data" | PLoS Biol 2018, PMID 30040822, PMC6057684, via Europe PMC full text (OPENED) |
| Asthma Mobile Health Study (Apple ResearchKit) | 5,875 US participants with survey/task data: symptoms, meds, EQ-5D, 3-digit zip; no inhaler sensor data | n/a | Synapse conditions of use | NEEDS APPLICATION: Synapse Certified User + public intended-use statement + accept conditions; Synapse syn8361748 | Sci Data 2018, PMID 29786695, PMC5963336 (OPENED). Not doable tonight if certification is not already held |
| T1DEXI / T1DEXIP | >500 adults (+250 children) with T1D: activity, HR, insulin, CGM, diet | n/a | Vivli terms | NEEDS APPLICATION via Vivli (request numbers e.g. 9105, 9407) | Helmsley/Vivli pages, SNIPPET only: https://helmsleytrust.org/news-and-insights/helmsley-charitable-trust-announces-a-public-dataset-and-request-for-proposals-to-promote-research-and-solutions-for-people-with-type-1-diabetes-to-safely-incorporate-exercise-into-their-daily-lives/ ; https://vivli.org/awardees-announced-for-helmsleys-t1d-exercise-data-challenge/ |

Home blood pressure time series: no large, open, per-patient home BP telemonitoring dataset found in one search (SNIPPET). Closest: Oxford SHINE remote vs face-to-face ambulatory BP, 65 participants, CSV, https://doi.org/10.5287/bodleian:qa9ZZmdOJ (SNIPPET, not opened); NCT00781365 telemonitoring trial posts only group summary results https://clinicaltrials.gov/study/NCT00781365 (SNIPPET).

Heart-failure telemonitoring (daily weight): no open patient-level dataset found (SNIPPET search). Tele-HF and others publish results only.

Indian data: no openly downloadable Indian CGM dataset found. Pune-2021 (50 people, FreeStyle Libre Pro, 15-min, 14 days) + Joshi-2018 (78) used in "Evaluation of HbA1c from CGM traces in an Indian population", Front Endocrinol 2023, DOI 10.3389/fendo.2023.1264072; data statement: "will be made available by the authors, without undue reservation" = on request, not tonight (OPENED).

## NOT FOUND / NOT SEARCHED

Searches used: 0
