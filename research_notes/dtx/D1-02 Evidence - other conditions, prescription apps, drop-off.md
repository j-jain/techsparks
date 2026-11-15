# D1-02 Evidence: other conditions, prescription apps, drop-off (agent: claude-opus-5-5, 2026-11-13)

## Digest

Facts that matter most:
1. Warfarin: the patient tests INR at home and changes the dose by a schedule. This cut thromboembolism (RR 0.47) and death (RR 0.55). Testing at home and phoning the clinic cut clots (RR 0.69) but not death (RR 0.94). Major bleeding did not change. (D1-02-F05)
2. Asthma: when the patient raises the steroid dose with each reliever puff (SMART), exacerbations fall by about a third (RR 0.68). No sensor is needed. (F37)
3. Gout: nurses titrating urate to a target reached it in 95% vs 30% of patients (RR 3.18), at £5,066 per QALY. (F06)
4. Inhaler reminders raised adherence from 30% to 84%, but school absence did not change. (F01) The Digihaler sensor system's control odds ratio was 1.35, with an interval that crosses 1. (F02)
5. Smart inhalers failed commercially. Teva withdrew Digihaler in June 2024 (F41). ResMed says Propeller has ceased operations (F40, SNIPPET).
6. Tuberculosis: in ASCENT (n=23,483 in four countries), pillboxes and labels did not reduce poor outcomes. (F59) In China, a reminder pillbox improved adherence and SMS did not, but adherence was the endpoint. (F34)
7. Stroke telerehab is about equal to in-person care, and no better than usual care for daily-living activities (SMD 0.00). (F07)
8. Pulmonary telerehab matches centre-based rehab on walk distance. Completion was 93% vs 70%. (F03)
9. PHTI: PT-guided virtual MSK care equals in-person care and lowers spending. App-only exercise is unlikely to replace PT. Remote-monitoring add-ons raise spending. (F54)
10. Prescription digital therapeutic (PDT) companies did badly. Pear sold its assets for about $6M against $130M of liabilities (F42). Akili made $523,000 from prescription sales in 2023 and sold for about $34M (F44). Better Therapeutics wound down with no product revenue (F46).
11. Drop-off: median 30-day retention for mental-health apps is 3.3% (F26). Median retention in remote studies is 5.5 days, and clinician referral adds 40 days (F27). Pooled dropout in chronic-disease app trials is 43% (F28).
12. Motivista was cleared in Oct 2026 (d -0.36). Rejoyn's primary mITT result was p=0.0568 (F49, SNIPPET).

Surprises:
- RESPeRATE had no blood-pressure effect once the manufacturer's trials were excluded. (F11)
- In a 2026 sleep meta-analysis, adaptive JITAIs did not beat non-adaptive EMIs. (F32) The HeartSteps effect faded over time. (F31)
- CureApp's smoking app uses an exhaled-CO biomarker and gave OR 1.73 for abstinence in Japan. (F22)

Against the starting leads:
- Lead 1 is supported for dose loops (F05, F06, F37), but it is mixed. A symptom-driven dose change works without any device. Reminders raise adherence without moving hard outcomes (F01, F34, F59).
- Lead 3(c): smart inhalers have weak outcome evidence and two commercial exits.
- Lead 3(d): rehab software matches in-person care but does not beat usual care.

## Findings

Method note: abstracts were opened through the Europe PMC REST API (resultType=core), which returns the full PubMed abstract. "OPENED" below means the abstract text was read in full from that API. URLs point to the PubMed record.

### Q1. Asthma and COPD

- D1-02-F01. Chan 2015, Lancet Respir Med. RCT, n=220 children aged 6-15 after an emergency visit for asthma, Auckland, New Zealand. Electronic inhaler monitor with audiovisual reminders ON vs same device with reminders OFF, 6 months. Median adherence to inhaled steroid 84% vs 30% (p<0.0001). School absence (co-primary) 1.9% vs 1.7% of days: no difference. Asthma morbidity score fell 2.0 vs 1.2 points (p=0.008). Funder: Health Research Council of NZ, Cure Kids. Adaptive depth 2 (reminders). Year 2015. https://pubmed.ncbi.nlm.nih.gov/25617215/ (2015). OPENED. CITED. Lead confirmed.
- D1-02-F02. CONNECT2 (Teva Digihaler maintenance-and-reliever system), J Allergy Clin Immunol Pract 2024. Randomised, 24 weeks, digital system (sensor inhaler + app + clinician dashboard) vs standard care. Bayesian primary: odds ratio for improved asthma control 1.35, 95% credible interval 0.846 to 2.038; 88.7% probability of benefit. Interval crosses 1. Maintenance adherence 79.2% at month 1, 68.6% at month 6 (decline over time). Reliever use down 38.2% vs baseline. Extra clinician contacts were mainly about poor inhaler technique. Funder not stated in abstract (NOT FOUND). https://pubmed.ncbi.nlm.nih.gov/38040117/ (2024). OPENED. CITED. Lead confirmed.
- D1-02-F03. Cochrane, Cox et al. 2021, "Telerehabilitation for chronic respiratory disease". 15 studies, n=1904, 99% COPD. Telerehab vs centre pulmonary rehab: 6-minute walk MD 0.06 m (95% CI -10.82 to 10.94; moderate certainty), i.e. equivalent. Completion 93% (95% CI 90 to 96%) telerehab vs 70% in-person. Maintenance telerehab vs none: 6MWD +78.1 m (49.6 to 106.6; low certainty). No extra adverse events. https://pubmed.ncbi.nlm.nih.gov/33511633/ (2021). OPENED. CITED.
- D1-02-F04. Review 2025 (J Allergy Clin Immunol Pract) on electronic medication monitoring in asthma: authors state these devices "have not yet seen widespread uptake in clinical settings". https://pubmed.ncbi.nlm.nih.gov/39824439/ (2025). OPENED. CITED.

### Q2. Warfarin self-testing and self-dosing (biomarker-to-dose loop)

- D1-02-F05. Cochrane, Heneghan et al. 2016, "Self-monitoring and self-management of oral anticoagulation" (CD003839.pub3). 28 RCTs, n=8950. Thromboembolic events RR 0.58 (95% CI 0.45 to 0.75; 18 studies, n=7594; moderate quality). Self-MANAGEMENT (patient tests INR at home and adjusts dose by a schedule): thromboembolism RR 0.47 (0.31 to 0.70; 11 studies, n=3497); all-cause mortality RR 0.55 (0.36 to 0.84; 8 studies, n=3058). Self-MONITORING (patient tests, clinic sets dose): thromboembolism RR 0.69 (0.49 to 0.97); mortality RR 0.94 (0.78 to 1.15), no effect. All pooled: mortality RR 0.85 (0.71 to 1.01), major bleeding RR 0.95 (0.80 to 1.12), no effect. Minor bleeding RR 0.97 (0.67 to 1.41; low quality, I2=82%). https://pubmed.ncbi.nlm.nih.gov/27378324/ (2016). OPENED. CITED. Lead confirmed. Note: the patient-adjusts-dose arm is the one with the mortality signal; the test-and-call-clinic arm is not.

### Q3. Gout, kidney, thyroid, epilepsy

- D1-02-F06. Doherty et al. 2018, Lancet. RCT, n=517, UK primary care (Nottingham). Nurse-led care with education, shared decisions and treat-to-target urate-lowering titration vs GP usual care. Serum urate <360 umol/L at 2 years: 95% vs 30%, RR 3.18 (95% CI 2.42 to 4.18, p<0.0001). All secondary outcomes (flares in year 2, tophi, quality of life) favoured nurse-led. Cost per QALY £5,066 at 2 years. Funder: Arthritis Research UK. Not a digital intervention; it is a protocolised titration loop run by nurses. https://pubmed.ncbi.nlm.nih.gov/30343856/ (2018). OPENED. CITED. Lead confirmed.

### Q4. Software rehabilitation with sensor or camera feedback

- D1-02-F07. Cochrane, Laver et al. 2020, "Telerehabilitation services for stroke". 22 trials, n=1937, reporting quality often inadequate. Post-discharge telerehab vs usual care, activities of daily living: SMD -0.00 (95% CI -0.15 to 0.15; 2 studies, n=661; moderate quality), no difference. Telerehab vs in-person physio, ADL: SMD 0.03 (-0.43 to 0.48; n=75; low). Balance SMD 0.08 (-0.30 to 0.46). Quality of life vs usual care SMD 0.03 (-0.14 to 0.20). Depression SMD -0.04 (-0.19 to 0.11). Computer-program upper-limb retraining vs in-person: MD 1.23 (-2.17 to 4.64; n=170; low). Reads as: equivalent to in-person, no better than usual care after discharge. https://pubmed.ncbi.nlm.nih.gov/32002991/ (2020). OPENED. CITED. Lead confirmed.
- D1-02-F08. Sword Health RCT, npj Digit Med 2023 (Correia et al.). n=140 chronic low back pain, digital care programme (motion-sensor-guided exercise + remote physiotherapist) vs in-person evidence-based physiotherapy. Disability (primary) change: median difference -0.55 (95% CI -2.42 to 5.81, p=0.412), no difference. Dropout 15.7% (11/70) digital vs 34.3% (24/70) in-person, p=0.019. Company-affiliated authors (Sword). https://pubmed.ncbi.nlm.nih.gov/37420107/ (2023). OPENED. CITED.
- D1-02-F09. Sword cohort 2023 (Musculoskelet Sci Pract), n=560 CLBP, single-arm: 78.4% completed; pain -2.32 points (95% CI 2.02 to 2.61). No control group. https://pubmed.ncbi.nlm.nih.gov/36543719/ (2023). OPENED. THEIR CLAIM (company-run cohort).
- D1-02-F10. Kaia App RCT, Toelle et al. 2019, npj Digit Med. n=101 non-specific low back pain, Germany. Kaia app 3 months vs 6 physiotherapy sessions + online education. Pain NRS at 12 weeks 2.70 (SD 1.51) vs 3.40 (SD 1.63), reported significant. Per-protocol analysis (not intention-to-treat). https://pubmed.ncbi.nlm.nih.gov/31304380/ (2019). OPENED. CITED.

### Q5. Biofeedback and wearable nerve stimulation

- D1-02-F11. Device-guided breathing (RESPeRATE) meta-analysis, Mahtani et al. 2012, J Hypertens. 8 trials, n=494. Systolic BP -3.67 mmHg (95% CI -5.99 to -1.39), diastolic -2.51 mmHg (-4.15 to -0.87). After excluding the 5 trials sponsored by or involving the manufacturer: no overall effect on BP. Max trial length 9 weeks. https://pubmed.ncbi.nlm.nih.gov/22495126/ (2012). OPENED. CITED. Lead confirmed; null in independent trials.
- D1-02-F12. Nerivio (remote electrical neuromodulation) pivotal, Yarnitsky et al. 2019, Headache. Double-blind sham-controlled, multicentre. Pain relief at 2 h 66.7% (66/99) vs 38.8% (40/103); therapeutic gain 27.9% (95% CI 15.6 to 40.2; p<0.0001). Pain-free at 2 h 37.4% vs 18.4% (p=0.003). Device adverse events 4.8% vs 2.4%. Sponsor Theranica (company device). https://pubmed.ncbi.nlm.nih.gov/31074005/ (2019). OPENED. CITED. Adaptive depth 0-1 (patient-triggered stimulation, no sensor loop).
- D1-02-F13. Freespira (capnometry-guided breathing for panic): only a 2019 mediator analysis surfaced in this pass, which reports that improvement in respiratory dysregulation in hypocapnic patients underlies symptom change. No effect size for the pivotal trial captured. https://pubmed.ncbi.nlm.nih.gov/30539503/ (2019). OPENED. CITED.

- D1-02-F14. Freespira real-world QI programme, Allegheny Health Network, 2020 (single arm, no control). Panic Disorder Severity Scale 14.4 to 4.9 at week 5 and 4.4 at 1 year; 73% panic-attack-free at 1 year; total medical cost $548 to $358 per member per month (-35%) at 12 months; ED cost -65%. https://pubmed.ncbi.nlm.nih.gov/32342249/ (2020). OPENED. CITED (uncontrolled; treat as weak). Freespira is described in the paper as FDA-cleared.
- D1-02-F15. Remote HRV biofeedback meta-analysis 2026 (Appl Psychophysiol Biofeedback). 18 studies, n=1352. Depression g=-0.41 (CI reported as -0.049 to -0.772, p=0.026, I2=73%, k=10); HRV g=0.443 (p=0.002); stress not significant (p=0.152, k=8). Practice <20 min/day and on-screen feedback were moderators of benefit. https://pubmed.ncbi.nlm.nih.gov/41310318/ (2026). OPENED. CITED.

### Q4 (continued). Digital cardiac rehabilitation

- D1-02-F16. Meta-analysis 2026 (BMC Cardiovasc Disord), digital home-based cardiac rehab in heart failure: 20 RCTs, n=4652. 6MWT +21.92 m (95% CI 12.27 to 31.58); VO2peak +0.96 mL/kg/min (0.56 to 1.35); MLHFQ -7.21 (-11.40 to -3.02). Wearable-guided subgroup 6MWT +51.98 m (34.21 to 69.76; I2=0%). Authors call subgroup findings "hypothesis-generating". https://pubmed.ncbi.nlm.nih.gov/42332587/ (2026). OPENED. CITED.

### Q6. Prescription digital therapeutics: pivotal trials

| ID | Product (company) | Pivotal trial | Design, n | Effect | URL | Status |
|---|---|---|---|---|---|---|
| D1-02-F17 | reSET (Pear), from Therapeutic Education System | Campbell 2014, Am J Psychiatry | Multisite RCT, outpatient addiction treatment, US | Abstinence OR 1.62 (95% CI 1.12 to 2.35); dropout HR 0.72 (0.57 to 0.92); in those positive at entry (n=228) OR 2.18 | https://pubmed.ncbi.nlm.nih.gov/24700332/ | OPENED, CITED |
| D1-02-F18 | Somryst (Pear), from SHUTi | Ritterband 2017, JAMA Psychiatry | RCT n=303 vs online education, 1 yr follow-up | Group x time significant on ISI, sleep-onset latency, wake after sleep onset (all P<.001); 56.6% (69/122) remission at 1 yr in SHUTi arm | https://pubmed.ncbi.nlm.nih.gov/27902836/ | OPENED, CITED |
| D1-02-F19 | SleepioRx (Big Health), from Sleepio | Espie 2012, Sleep | 3-arm RCT n=164, UK, vs placebo (imagery relief) and usual care | Sleep efficiency +20% vs +6% (d=1.06 vs placebo; d=0.95 vs TAU) post-treatment | https://pubmed.ncbi.nlm.nih.gov/22654196/ | OPENED, CITED |
| D1-02-F20 | DaylightRx (Big Health) | Carl 2020, Depress Anxiety | RCT n=256 vs WAITLIST, GAD | GAD-7 adjusted difference 3.22 (2.14 to 4.31), d=1.08. Waitlist control, not placebo | https://pubmed.ncbi.nlm.nih.gov/32725848/ | OPENED, CITED |
| D1-02-F21 | AspyreRx / BT-001 (Better Therapeutics) | Hsia 2022, Diabetes Care | RCT n=669, T2D, vs control app, 90 days | HbA1c -0.28% vs +0.11%; difference 0.39 points (P<0.0001); dose-response with modules completed | https://pubmed.ncbi.nlm.nih.gov/36181554/ | OPENED, CITED |
| D1-02-F22 | CureApp Smoking Cessation (CureApp, Japan; app + exhaled CO checker + physician software) | Masaki 2020, npj Digit Med | Multicentre RCT n=584 (572 analysed), Japan, all on drugs+counselling | Continuous abstinence wk 9-24: 63.9% vs 50.5%, OR 1.73 (1.24 to 2.42); wk 9-52: 52.3% vs 41.5%, OR 1.55 (1.11 to 2.16) | https://pubmed.ncbi.nlm.nih.gov/32195370/ | OPENED, CITED |
| D1-02-F23 | CureApp HT (hypertension, Japan) | HERB-DH1, Kario 2021, Eur Heart J | Open-label RCT n=390, 12 sites Japan, untreated hypertension | 24-h ambulatory SBP -2.4 mmHg (95% CI -4.5 to -0.3); home SBP -4.3 (-6.7 to -1.9); office -3.6 (-6.2 to -1.0) at 12 weeks | https://pubmed.ncbi.nlm.nih.gov/34455443/ | OPENED, CITED |
| D1-02-F24 | Rejoyn / CT-152 (Otsuka + Click) | Mirai trial; 2026 secondary analysis, JMIR Form Res | RCT vs sham app, adjunct to antidepressant | Secondary analysis: 24% to 47% higher odds of meaningful MADRS improvement vs sham. Primary-endpoint result NOT captured in this pass | https://pubmed.ncbi.nlm.nih.gov/42766497/ | OPENED, CITED |
| D1-02-F25 | Nerivio (Theranica) | see D1-02-F12 | | | | |

Adaptive depth: all of F17 to F24 are mostly 2-3 (scripted CBT content, some tailoring). CureApp Smoking (F22) adds a biomarker (exhaled CO) to the loop. None of these change a drug dose.

### Q7. Drop-off

- D1-02-F26. Baumel et al. 2019, JMIR. 93 mental-health apps with >=10,000 installs, panel usage data. Median daily open rate 4.0%. Median 15-day retention 3.9%, 30-day retention 3.3%. Day-30: peer support 8.9%, trackers 6.1%, mindfulness 4.7%, breathing exercise apps 0.0%. https://pubmed.ncbi.nlm.nih.gov/31573916/ (2019). OPENED. CITED. Lead confirmed.
- D1-02-F27. Pratap et al. 2020, npj Digit Med. 8 remote US digital health studies, >100,000 participants, 2014-2019. Median retention 2 to 26 days (median across studies 5.5 days). Clinician referral added 40 days to median retention; payment added 22 days (1 study); having the condition +7 days; older age +4 days. https://pubmed.ncbi.nlm.nih.gov/32128451/ (2020). OPENED. CITED. Lead confirmed.
- D1-02-F28. Meyerowitz-Katz et al. 2020, JMIR. Meta-analysis, 17 studies of app-based interventions for chronic disease. Pooled dropout 43% (95% CI 29 to 57); observational 49%, RCTs 40%; I2 >99%. https://pubmed.ncbi.nlm.nih.gov/32990635/ (2020). OPENED. CITED.
- D1-02-F29. Eysenbach 2005, JMIR, "The law of attrition": a substantial share of users drop out of any eHealth trial; proposes reporting "usage half-life" and survival analysis of use. No numeric rate. https://pubmed.ncbi.nlm.nih.gov/15829473/ (2005). OPENED. CITED. Lead confirmed.
- D1-02-F30. Retention inside trials with a clinician in the loop: Sword RCT dropout 15.7% digital vs 34.3% in-person (D1-02-F08); Cochrane pulmonary telerehab completion 93% vs 70% (D1-02-F03); CONNECT2 maintenance adherence 79.2% month 1 to 68.6% month 6 (D1-02-F02); BT-001 HbA1c fall tracked modules completed (D1-02-F21). CITED (cross-reference).

### Q8. Just-in-time adaptive interventions

- D1-02-F31. HeartSteps micro-randomised trial, Klasnja 2019, Ann Behav Med (sample size not in abstract; NOT FOUND). Any suggestion vs none: +14% 30-min step count (35 steps; p=0.06, not significant overall). Initially +66% (167 steps; p<0.01) but effect "diminished over time". Walking suggestions +24% (59 steps; p=0.02). Anti-sedentary suggestions: no detectable effect. https://pubmed.ncbi.nlm.nih.gov/30192907/ (2019). OPENED. CITED.- D1-02-F32. Meta-analysis 2026 (Sleep Med), EMIs and JITAIs for sleep: 11 RCTs (3 EMI, 8 JITAI). Insomnia severity SMD -0.87 (-1.32 to -0.42). Tests for subgroup differences between non-adaptive EMIs and adaptive JITAIs: not significant for any outcome. https://pubmed.ncbi.nlm.nih.gov/42994167/ (2026). OPENED. CITED.
- D1-02-F33. Active Family JITAI pilot micro-randomised trial 2026 (PLoS One): micro-interventions did not change proximal sedentary time or activity in children (d=0.01) or parents (d=-0.09). https://pubmed.ncbi.nlm.nih.gov/41544066/ (2026). OPENED. CITED.

### Q9. Adherence technology that did or did not move outcomes (tuberculosis)

- D1-02-F34. Liu et al. 2015, PLoS Med. Cluster RCT, 36 districts, 4 provinces of China, n=4173 new pulmonary TB patients, 6 months. Primary: % patient-months with >=20% doses missed. Control 29.9%; text messages 27.3% (aMR 0.94, 95% CI 0.71 to 1.24, NO effect); medication monitor box with reminders 17.0% (aMR 0.58, 0.42 to 0.79); combined 13.9% (aMR 0.49, 0.27 to 0.88). Text messages lowered loss to follow-up (aMR 0.42, 0.18 to 0.98). The intended escalation (doctor switches non-adherent patients to intensive management) was "underutilised". Outcome is adherence, not cure. https://pubmed.ncbi.nlm.nih.gov/26372470/ (2015). OPENED. CITED.
- D1-02-F35. South Africa (ASCENT-linked, inferred) cost-effectiveness 2026: medication monitor + differentiated care, n=2757; "effectiveness" (adherent) 81% vs 50.8% SoC; ICER $166.33 per extra adherent patient. Adherence endpoint only. https://pubmed.ncbi.nlm.nih.gov/42393627/ (2026). OPENED. CITED. Whether this is the ASCENT trial is not stated in the abstract.
- D1-02-F36. Systematic review 2026 of TB digital adherence technology costs in LMICs: 14 economic evaluations; phone-based DATs incl. 99DOTS have lowest cost but "cost-effectiveness evidence remains limited". https://pubmed.ncbi.nlm.nih.gov/43021299/ (2026). OPENED. CITED.

### Q1 (continued). Asthma: patient-adjusted therapy and Propeller

- D1-02-F37. SMART (single maintenance and reliever therapy, budesonide-formoterol: the patient raises the steroid dose each time they take a reliever puff) meta-analysis, Sobieraj et al. 2018, JAMA. 16 RCTs, n=22,748. Age >=12: exacerbations RR 0.68 (95% CI 0.58 to 0.80; RD -6.4%) vs same-dose ICS-LABA controller; RR 0.77 (0.60 to 0.98; RD -2.8%) vs higher-dose controller. Age 4-11 (n=341): RR 0.38 (0.23 to 0.63) vs same-dose ICS-LABA. https://pubmed.ncbi.nlm.nih.gov/29554195/ (2018). OPENED. CITED. A dose change driven by symptoms, with no sensor, cuts exacerbations by about a third.
- D1-02-F38. Propeller Health RCT, Merchant et al. 2016, J Allergy Clin Immunol Pract. Randomised, population health programme (US; sample size not in abstract, NOT FOUND). Reliever (SABA) use fell 0.41 vs 0.31 puffs/day (P<.001); SABA-free days +21% vs +17% (P<.01). Asthma Control Test: no difference overall; in adults uncontrolled at baseline, 63% vs 49% reached control (P<.05). Company-affiliated authors. https://pubmed.ncbi.nlm.nih.gov/26778246/ (2016). OPENED. CITED.
- D1-02-F39. Propeller quality-improvement cohort, Merchant 2018, World Allergy Organ J. n=224, pre/post, no control. Asthma ED visits 11.6 to 5.4 per 100 patient-years; ED+hospital 13.4 to 5.8 (p<0.05). https://pubmed.ncbi.nlm.nih.gov/30524644/ (2018). OPENED. CITED (uncontrolled).

### Q1 commercial status of smart inhalers

| ID | Company / product | What it measures; what it changes | Adaptive depth | Status (date) | Source |
|---|---|---|---|---|---|
| D1-02-F40 | Propeller Health (Reciprocal Labs), add-on inhaler sensors + app | Inhaler actuations, time, location; no dose change | 1-2 | Acquired by ResMed for $225M, closed 31 Jan 2019. ResMed page now says Propeller "has ceased operations"; ResMed keeps brand, IP and assets. Shutdown date NOT FOUND | ResMed page via search SNIPPET only (fetch returned 403): https://resmed.com/en-us/?p=15596 ; acquisition: https://investor.resmed.com/news-events/press-releases/detail/132/resmed-completes-225-million-acquisition-of-propeller-health (SNIPPET) |
| D1-02-F41 | Teva Digihaler (ProAir, AirDuo, ArmonAir; GoResp in UK), built-in sensor inhalers | Inhalation flow, use; clinician dashboard | 1-2 | Digihaler app and dashboard withdrawn 1 June 2024; US distribution of the three Digihaler inhalers stopped 1 June 2024; GoResp Digihaler withdrawn in UK (MHRA Class 3 recall, 2024). Trade headline frames it as "not enough uptake" (article body not readable) | SNIPPET: https://aafa.org/digihaler-discontinuation-may-cause-another-disruption-in-care-for-people-with-asthma/ ; https://www.gov.uk/drug-device-alerts/class-3-medicines-recall-teva-uk-limited-goresp-digihaler-el-24-a-slash-23 ; https://mdedge.com/content/digital-inhaler-discontinuations-not-enough-uptake-device |

Note: CONNECT2 (F02, published 2024) reported for a product whose app was switched off the same year.

### Q6 (continued). Commercial outcomes of prescription digital therapeutics

| ID | Company | Product(s) | What happened | Date | Source / tag |
|---|---|---|---|---|---|
| D1-02-F42 | Pear Therapeutics (US) | reSET, reSET-O, Somryst | Filed Chapter 11 April 2023; assets sold at auction to four buyers for "just over $6 million"; liquidation plan confirmed by Delaware court (article dated 20 May 2024); $130M total liabilities on combined basis | 2023-2024 | https://foleyhoag.com/news-and-insights/news/2024/may/foley-hoag-advises-pear-therapeutics-through-confirmation-of-chapter-11-liquidating-plan/ OPENED, CITED |
| D1-02-F43 | Pear, buyers | | Somryst to Nox Health ($3.9M); reSET, reSET-O, PearConnect, pipeline to Harvest Bio ($2.03M); platform patents to Click ($70,000); migraine to WELT ($50,000). Pear had been valued at $1.6B at its 2021 SPAC listing | 2023 | SNIPPET (Fierce Biotech and MobiHealthNews fetches returned 403): https://www.mobihealthnews.com/news/pear-therapeutics-assets-sold-over-6m-auction-after-bankruptcy |
| D1-02-F44 | Akili (US) | EndeavorRx (ADHD video game, De Novo 2020) | 2023 revenue $1.7M: $1.2M from over-the-counter EndeavorOTC, $523,000 from prescription EndeavorRx; net loss $59.5M. Moved away from the prescription model in 2023. Staff cuts Jan 2023 (~1/3), later 2023, and 46% in Apr 2024. Agreed sale to Virtual Therapeutics for about $34M, $0.43/share cash | announced 29-30 May 2024 | https://www.medtechdive.com/news/akili-sell-34m-virtual-therapeutics-digital/717570/ OPENED, CITED. Deal close NOT confirmed |
| D1-02-F45 | Akili pivotal (STARS-ADHD) | | RCT n=348, age 8-12, vs digital control; primary TOVA attention index median change 0.88 (95% CI 0.24 to 1.49; p=0.006); 83% of expected sessions played; sponsor Akili. Endpoint is a computerised attention test, not parent or teacher ADHD ratings | 2020 | https://pubmed.ncbi.nlm.nih.gov/33334505/ OPENED, CITED |
| D1-02-F46 | Better Therapeutics (US) | AspyreRx (T2D CBT app, cleared 2023) | Launched Oct 2023, no product revenue expected in 2023; cash $6.6M at 30 Sep 2023; accumulated deficit $134.3M; terminated employees, asked Nasdaq to delist, weighed wind-down | 15 Mar 2024 | https://www.medtechdive.com/news/better-therapeutics-lay-offs/710402/ OPENED, CITED |
| D1-02-F47 | Click Therapeutics | took AspyreRx assets | Click says no plan to sell AspyreRx in current form; to adapt for obesity; terms undisclosed | 2024 | SNIPPET: https://pharmaphorum.com/news/click-buys-better-assets-speed-its-digital-obesity-drive |
| D1-02-F48 | Otsuka + Click | Rejoyn (CT-152, depression adjunct) | FDA clearance announced 1-2 Apr 2024; Mirai trial n=386, primary = MADRS change at week 6 | 2024 | https://www.drugtopics.com/view/fda-clears-first-digital-therapeutic-to-treat-major-depressive-disorder OPENED, CITED |
| D1-02-F49 | Rejoyn primary result | | mITT primary: MADRS -9.03 vs -7.25 sham, p=0.0568 (not significant); ITT supportive: -8.78 vs -6.66, p=0.0211. Trade press called the endpoint "met" using the ITT figure | 2024 | SNIPPET (secondary sources; FDA K231209 summary not opened): https://fda.innolitics.com/device/K231209 . CONFLICT: Pharmaphorum says primary met |
| D1-02-F50 | Click Therapeutics | Motivista (CT-155, negative symptoms of schizophrenia; with Boehringer Ingelheim per protocol code BI 3972080) | FDA 510(k) clearance, announced 5-7 Oct 2026 (search snippet gives clearance date 30 July 2026, Rejoyn as predicate: SNIPPET). CONVOKE: n=457, 66 US sites; CAINS-MAP improvement 6.8 vs 4.2 points vs digital control at 16 weeks; Cohen d -0.36; P=0.0003 | 2026 | https://www.psychiatrictimes.com/view/fda-grants-clearance-to-motivista-the-first-authorized-treatment-for-negative-symptoms-of-schizophrenia (7 Oct 2026) OPENED; n from https://pubmed.ncbi.nlm.nih.gov/41057039/ OPENED. Lead confirmed |
| D1-02-F51 | Click Therapeutics | CT-132 migraine prevention | FDA De Novo April 2025 | 2025 | SNIPPET: https://hlth.com/insights/news/fda-authorizes-click-therapeutics-prescription-digital-therapeutic-for-migraine-prevention-2025-04-16 |
| D1-02-F52 | Big Health (UK/US) | SleepioRx, DaylightRx | US Medicare Digital Mental Health Treatment codes G0552-G0554 from 1 Jan 2025; Big Health says these are not a guarantee of payment; raised $23.7M strategic round 12 Feb 2026; says its products are among 9 FDA-cleared treatments in the CMS DMHT category | 2025-2026 | SNIPPET (BusinessWire fetch 403): https://www.businesswire.com/news/home/20260212541697/en/Big-Health-Secures-Funding-to-Accelerate-Adoption-of-Digital-Mental-Health-Treatments . THEIR CLAIM |
| D1-02-F53 | CureApp (Japan) | Smoking cessation (F22), HT hypertension (F23) | Commercial status as of 2026 NOT SEARCHED (Japanese insurance listing of CureApp HT not verified in this pass) | | NOT SEARCHED |

### Q4 (continued). Virtual MSK: independent verdict and company outcomes

- D1-02-F54. Peterson Health Technology Institute (PHTI), Virtual MSK Solutions report, 5 June 2024. Assessed 8 products (DarioHealth, Hinge Health, Kaia Health, Limber, Omada, RecoveryOne, Sword Health, Vori Health), 3 categories. PT-guided virtual care: pain and function comparable to in-person PT with net spending decrease; app-based exercise with limited PT: improves pain and function vs usual care but "unlikely to be effective as total substitutes for in-person physical therapy"; remote therapeutic monitoring add-ons: possibly better outcomes, limited evidence, spending rises. Savings estimate: ~$4.4M per 1M commercially insured people/year if 25% of low-back-pain PT users switch at $995/year (SOURCE ESTIMATE). Report does not separate the effect of adapting exercise to measured performance. https://www.phti.org/?p=1710 (5 Jun 2024). OPENED. CITED.
- D1-02-F55. Hinge Health: IPO 21 May 2025 at $32/share raising $437M; 2025 revenue $588M (+51%); 2026 guidance $732M-$742M; Q1 2026 revenue +47%. SNIPPET (Fierce Healthcare fetch 403): https://www.fiercehealthcare.com/digital-health/hinge-health-projects-2026-revenue-hit-732m-buoyed-strong-growth-investments-ai . Sword Health 2026 figures NOT FOUND.

### Q7 (continued). What improves retention

- D1-02-F56. Meta-analysis 2023 (JMIR), strategies to improve engagement with digital interventions for nutrition, activity, obesity: 54 studies; engagement strategies SMD 0.33 (95% CI 0.20 to 0.46), very low certainty. Social support ES 0.40 (0.14 to 0.66) associated with more use; SMS ES 0.34 and email ES 0.29 with better user experience. https://pubmed.ncbi.nlm.nih.gov/38113062/ (2023). OPENED. CITED.
- D1-02-F57. Clinician referral: +40 days median retention (Pratap 2020, D1-02-F27). Human-guided designs retain better in trials: Sword dropout 15.7% (F08); pulmonary telerehab 93% completion (F03); STARS-ADHD 83% of sessions played (F45). Cross-reference.

## NOT FOUND / NOT SEARCHED

- NOT FOUND: Propeller shutdown date and user-transition details (ResMed page blocked, 403).
- NOT FOUND: Akili deal close confirmation and EndeavorRx status in 2026.
- NOT FOUND: Somryst sales under Nox Health; reSET status under Harvest Bio as of 2026.
- NOT FOUND: Rejoyn sales or prescription numbers; primary Mirai trial publication (numbers above are SNIPPET).
- NOT FOUND: Freespira pivotal RCT effect size (only uncontrolled studies captured, F14).
- NOT FOUND: a 99DOTS randomised trial. Only an interrupted time series (2025, IJTLD): 87.2% enrolled on 99DOTS; treatment completion 89.8% vs 87.1% before; no level or slope change in treatment success. https://pubmed.ncbi.nlm.nih.gov/40579762/ OPENED (D1-02-F58).
- D1-02-F59 (found late, Q9). ASCENT, Lancet 2025: four pragmatic cluster RCTs (Philippines, South Africa, Tanzania, Ukraine), 220 clusters, 25,606 enrolled, 23,483 ITT. Smart pillbox or medication labels with differentiated care vs standard care. Poor outcome (failure, loss to follow-up, death, etc.): Philippines aOR 1.13 (0.72 to 1.78); Tanzania 1.49 (0.99 to 2.23); South Africa 1.19 (0.88 to 1.60); Ukraine aRR 1.15 (0.83 to 1.59). Authors: DATs "did not reduce poor treatment outcomes". Two social harms from pillbox disclosure. Funder Unitaid. https://pubmed.ncbi.nlm.nih.gov/40086457/ (2025). OPENED. CITED. Lead confirmed. Contrast with China 2015 (F34), where the same kind of box improved adherence but outcome was adherence, not cure.
- NOT FOUND: Kidney disease, thyroid and epilepsy feedback-loop trials (not searched in depth; NOT SEARCHED).
- NOT FOUND: Cochrane review of written asthma action plans (2021 record had no abstract in API). COPD action plan Cochrane not retrieved.
- NOT FOUND: meta-analysis directly comparing adaptive vs non-adaptive versions of the same intervention, beyond the 2026 sleep subgroup test (F32).
- NOT FOUND: independent comparison showing that adapting exercise dose to sensor-measured performance beats fixed programmes (PHTI does not separate this).
- NOT SEARCHED: India-specific evidence for any item in this note; Japan reimbursement status of CureApp products; Germany DiGA delisting statistics; wearable vagus or other nerve stimulators beyond Nerivio.
- NOT FOUND in abstracts: CONNECT2 funder; HeartSteps sample size; Propeller RCT sample size.

Searches used: 13 web searches (plus about 70 direct Europe PMC API abstract fetches and 9 direct page fetches, which do not count)
