# D2-06 Funded abroad: chronic-care startups and frontier-lab health products (agent: Sonnet 5.5, 2026-11-13)

## Digest
32 entries (some short, YC-mirror-only). Key facts:
1. Cadence $100M Series C, 23 Jun 2026, Spark Capital lead; supervised AI agents support medicine changes; THEIR CLAIM 55% of alerts closed with no human adjustment, BP control +70% relative. D2-06-F1, F2.
2. Nourish $100M Series C, 20 May 2026, Menlo lead; dietitians plus AI, GLP-1 prescribing; claims systolic -23. D2-06-F5, F6.
3. Closed Loop Medicine WeDosify (US launch 18 Sep 2025): clinician-reviewed GLP-1 dose options from tolerability and response, built on 29 studies and 15,000+ profiles. Closest depth-4 pattern to the DT1 engine. D2-06-F24.
4. Twin Health $53M Series E, Aug 2025, valuation above $950M; claims 71% lowered A1C and often stopped drugs. D2-06-F3, F4.
5. Hippocratic AI $126M Series C, 3 Nov 2025, $3.5B; staged safety training; claims 115M interactions. D2-06-F20, F21.
6. Tucuvi $20M Series A, Jan 2026: voice agent, up to 80% of nurse follow-up automated. D2-06-F9, F10.
7. Function Health $298M Series B at $2.5B (19 or 23 Nov 2025, sources differ), price cut to $365. D2-06-F42, F43.
8. Lucis $20M Series A, 26 May 2026: 75% of six-month completers improved 3+ markers; physicians review. D2-06-F44, F45.
9. Frontier labs: ChatGPT Health (7 Jan 2026) and Claude (11 Jan 2026) read Apple Health and Health Connect, US only, no therapy change. D2-06-F15, F16.
10. Cuffless BP is funded (Biobeat $50M, 31 Dec 2025; Aktiia $42M, May 2025, FDA OTC clearance Jul 2025) but is depth 1. D2-06-F36, F37.
11. Wearable-data plumbing: Junction $18M Series A (Mar 2025), 2M+ devices; Galen AI bought by Oura (Apr 2026). D2-06-F30, F34.
12. YC and a16z essays opened do not mention dose titration; a16z: "The opportunity is helping people act on them." D2-06-F47, F50.
Surprises: (a) no funded startup page describes home BP dose steps by protocol; (b) funding is going to depth 1 to 3 products and AI agents far more than depth 4; (c) YC's own Winter 2027 RFS has no chronic-care item.
Contradicts leads: lead 1 (monitoring alone does not work) is not tested here; these are company claims only.

## Findings

Notes on format. Fact IDs D2-06-Fn sit on each entry. Indian-fact IDs (D1-xx-Fnn) are reused from the Round 1 notes and were NOT re-opened here. "Mirror" = the yc-oss JSON copy of the Y Combinator directory, fetched 13 Nov 2026 (OPENED, secondary copy). Depth = adaptive depth 0-4. All date fields are the source item date.

### (a) Remote medication adjustment and virtual clinics

**1. Cadence (US). AI-supervised remote care for chronic conditions in older adults. Depth 4 (supports medicine changes; how far the AI decides alone is not stated).**
- Backers: $100M Series C, 23 Jun 2026, led by Spark Capital; Thrive Capital, General Catalyst, Coatue, B Capital, Corewell Health Ventures, Memorial Hermann, Duke Health took part. Valuation not on the page. D2-06-F1 | CITED | https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/ | 2026-06-23 | OPENED. A search snippet said $1.23B valuation (SNIPPET).
- Loop: remote vitals between visits; supervised AI agents flag risk and support medicine changes under the partner medical group's protocols; clinicians keep judgement calls. Payer: health systems (Medicare savings).
- Traction (THEIR CLAIM, Jun 2026): 20+ health systems, 100,000+ active patients; 55% of alerts resolved without human adjustment; heart-failure patients on guideline therapy +230%; BP control +70% relative; admissions -27%. D2-06-F2.
- India need: hypertension 35.5% of adults 20+ (D1-03-F01); control rose 26.3% to 59.8% among IHCI returners (D1-03-F10).
- Indian equivalents: none doing home-reading dose steps (DT1 section 1); government Simple app stores drug list and follow-up days only (D1-06-F40).
- Differs in India: no Medicare-type payer; 79.9% of specialist posts vacant at rural CHCs (D1-03-F16); the realistic loop is a health worker, not a pharmacist.
- Borrow: report "share of readings that needed no clinician touch" (their 55%) and clinician minutes per patient. Same shape as HyperLink pharmacists (D1-01-F04).
- Demo potential: 4.

**2. Twin Health (US). Digital twin for type 2 diabetes and obesity. Depth 4 (medicine reduction guided by sensor data; clinician role not described on the opened page).**
- Backers: $53M Series E, 21 Aug 2025, led by Maj Invest; Iconiq and Temasek (existing) took part; valuation above $950M. D2-06-F3 | CITED | https://fortune.com/2025/08/21/exclusive-twin-health-metabolic-health-startup-raises-53-million-series-e-at-950-million-valuation | 2025-08-21 | OPENED.
- Loop: glucose monitor plus activity tracker feed a personal model for food, sleep, activity; members often stop drugs (one example: metformin). Payer: employers and plans (named: HCSC, Medline, Benjamin Moore).
- Traction (THEIR CLAIM, Aug 2025): NEJM Catalyst study with Cleveland Clinic, 71% lowered A1C and "frequently" stopped medicines. Study size and design not opened. D2-06-F4.
- India need: diabetes 11.4% of adults 20+ (D1-03-F01); 9.8% of Tamil Nadu diabetics controlled (D1-03-F09).
- Indian equivalents: Sugar.fit, BeatO, Fitterfly, all depth 3 (D1-04-F04, F06, F07).
- Differs in India: CGM about ₹8,999 to ₹18,000 per four weeks (D1-04-F33, a blog) makes per-patient cost high; the patient pays.
- Borrow: pitch deprescribing ("fewer drugs") as the outcome; it is the reverse of step-up and is a payer story.
- Demo potential: 2.

**3. Nourish (US). Dietitians plus AI agents with GLP-1 prescribing and medication management. Depth 3 to 4.**
- Backers: $100M Series C, 20 May 2026, led by Menlo Ventures; Thrive, Index Ventures, J.P. Morgan Growth Equity Partners, Y Combinator took part; total raised $215M. D2-06-F5 | CITED | https://femtechinsider.com/nourish-raises-100m-series-c-for-ai-native-metabolic-health-clinic-with-glp-1-integration/ | 2026-05-20 | OPENED. Bloomberg snippet: $1.75B valuation (SNIPPET).
- Loop: 10,000+ registered dietitians with AI agents; plans pay, patients pay nothing; 200M covered lives.
- Traction (THEIR CLAIM, May 2026): weight -8%, A1C -1.3 points, LDL -31, systolic BP -23; plan savings over $2,000 per patient a year. D2-06-F6.
- India need: obesity, diabetes, generic semaglutide launch 21-22 Mar 2026 (D1-04-F10).
- Indian equivalents: Healthify tirzepatide programme from ₹48,000 for 3 months (D1-04-F26), Tracky (D1-04-F27), BeatO (D1-04-F06).
- Differs in India: no plan pays; dietitian supply and price.
- Borrow: one plan for drug, food and BP (Nourish reports BP and LDL as well as weight); a BP step loop can ride on the same visit.
- Demo potential: 3.

**4. Oska Health (Germany). Health coaches plus AI for people with several chronic conditions (kidney, diabetes, hypertension). Depth 3.**
- Backers: EUR 11M seed, 26 Feb 2026; Capricorn Partners and SwissHealth Ventures named as leads; Revent, Calm Storm, LBBW VC, BMH, GoHub Ventures, Aurum Impact took part. D2-06-F7 | CITED | https://tech.eu/2026/02/26/oska-health-secures-eur11m-to-expand-ai-driven-care/ | 2026-02-26 | OPENED.
- Loop: certified coaches by video, chat, app on food, activity and medicine-taking; the physician's recommendation is the input; AI reduces coach admin.
- Traction: no patient count or outcome for Oska on the page. NOT FOUND.
- India need: 51% returned to IHCI clinics (D1-03-F10).
- Indian equivalents: Curelink (D1-04-F35), Zyla Health (D1-04-F28).
- Differs in India: Germany's DiGA code pays for apps (D1-05-F25 to F29); India has none.
- Borrow: a coach (or ASHA/ANM worker) who carries the doctor's rule into daily life, with AI doing the admin.
- Demo potential: 2.

**5. Kivo Health (US, YC W23; founded before the window, Series A $10M per its own YC page). AI virtual care for seniors with lung disease. Depth 3.**
- Mirror text: "save payers $8k+ on average per patient"; works with Stanford, UCLA, Optum Health (THEIR CLAIM, undated). D2-06-F8 | Mirror | OPENED. Round date and lead NOT FOUND.
- India need: COPD burden not looked up here. NOT SEARCHED.
- Borrow: pitch to a health system as admissions avoided per patient.
- Demo potential: 2.

### (b) AI clinicians, nurses and navigators

**6. Tucuvi (Spain). Voice agent "LOLA" that phones patients for chronic care, post-discharge, medication checks. Depth 2 to 3 (calls and escalation; no dose change stated).**
- Backers: $20M Series A, 10 Jan 2026; co-led by Cathay Innovation and Kfund (Leadwind); Frontline, Seaya, Shilling existing. D2-06-F9 | CITED | https://pulse2.com/tucuvi-20-million-series-a/amp/ | 2026-01-10 | OPENED.
- Loop: agent runs 50+ workflows, escalates to nurses; claims EU Class IIb software-as-medical-device status.
- Traction (THEIR CLAIM, Jan 2026): up to 80% of nurse follow-up automated; 90%+ reach; 5.5% fewer COPD readmissions; 60+ organisations. D2-06-F10.
- India need: 2-minute consultations; 51% no-return (D1-03-F24, F10).
- Indian equivalents: 2care.ai on WhatsApp (D1-04-F36).
- Differs in India: many languages, cheap calls, feature phones; voice beats app.
- Borrow: a phone call in the patient's language that asks the pre-step question ("did you take the tablet?", D1-06-F14), then escalates. Cheapest adherence signal.
- Demo potential: 5.

**7. Counsel Health (US). AI-native medical group; doctors in front, AI behind. Depth 3 to 4 (can prescribe and order labs; AI gets more autonomous as clinicians validate).**
- Backers: Series A announced 16 Oct 2025, a16z co-leading with Google Ventures; a16z led the seed; amount not on the page. D2-06-F11 | CITED | https://a16z.com/announcement/investing-in-counsel-health/ | 2025-10-16 | OPENED.
- Traction: "strong market adoption", no figures (THEIR CLAIM, a16z post).
- India need and equivalents: as entry 1.
- Differs in India: telemedicine rules; class of a dose-proposing tool is an open question (DT1 section 5).
- Borrow: log every clinician accept, edit or reject of a proposed step; that log is the safety and training record.
- Demo potential: 3.

**8. Juno (US, YC Spring 2026). AI health assistant for chronic illness.** Mirror: "launched in October", "300,000+ patients globally" (THEIR CLAIM, undated). D2-06-F12 | Mirror | OPENED. Funding NOT FOUND. Depth 3. India need not looked up. Differs: free consumer chat, no clinician. Borrow: count real users on a chat channel before building hardware. Demo potential: 4.

**9. Prana (US, YC W26; 4 people). AI physician that watches records and wearables for "clinical drift" and manages prescriptions.** Mirror: automates 90% of "grunt work" so doctors decide (THEIR CLAIM). D2-06-F13 | Mirror | OPENED. Funding NOT FOUND. Depth 3 to 4. Borrow: alert on slow drift of the 7-day mean BP rather than single readings. Demo potential: 4.

**10. Clara (US, YC Spring 2026; 9 people). AI primary-care and longevity practice from the team that grew Circle Medical.** Mirror: "Clara can see your medical data and then act"; refills, labs. D2-06-F14 | Mirror | OPENED. Funding NOT FOUND. Depth 3 to 4. Borrow: refills first, as the lowest-risk action. Demo potential: 3.

### (g) Consumer health from frontier AI labs and big tech

**11. OpenAI, ChatGPT Health. Depth 1 to 3 (summaries and advice; no therapy change).**
- Announced 7 Jan 2026, waitlist first; connects Apple Health, medical records (partner b.well), Function, MyFitnessPal; wearable data reaches it through those apps. OpenAI says 230 million people a week ask health questions (THEIR CLAIM). EHR links US only. D2-06-F15 | https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/ | 2026-01-07 | OPENED (via Fortune; OpenAI's own page returned 403). Wide rollout "23 Jul" is SNIPPET only; conflicts in outlet dating, not resolved.
- Borrow: take readings through a standard health store and ask permission per use. Demo potential: 4.

**12. Anthropic, Claude consumer health integrations. Depth 1 to 3.**
- Announced 11 Jan 2026: HealthEx and Function connectors (beta); Apple Health and Android Health Connect rolling out in beta; US only, Pro and Max plans; summarises history, explains results, finds patterns; quote: "We do not use users' health data to train models." D2-06-F16 | CITED | https://www.anthropic.com/news/healthcare-life-sciences | 2026-01-11 | OPENED.
- Borrow: Health Connect is the Android route for an Indian phone-based loop. Demo potential: 4.

**13. Google, Google Health app (ex-Fitbit) with Gemini coach.** Rebrand and global coach availability 19 May 2026 inside a Premium plan; to work with Apple Watch via HealthKit. D2-06-F17 | SNIPPET (search summary of TechRepublic; page returned 403) | 2026-05. Depth 3. India availability NOT FOUND. Borrow: coach reads many vendors' devices, so do not tie the loop to one cuff.

**14. Microsoft, Copilot Health.** Launched Mar 2026; records activity, sleep, vitals, medication lists, tests from 50+ wearables and records from 50,000+ US hospitals. D2-06-F18 | SNIPPET | 2026-03. Depth 1 to 2.

**15. Apple, AI health coach ("Project Mulberry", Health+).** Reported wound down, features to trickle into Health app (Bloomberg via search summary). D2-06-F19 | SNIPPET | 2026-05. Not confirmed after WWDC June 2026.

### More in (a), (b): medicine-managing virtual clinics and AI agents

**16. Hippocratic AI (US). Voice AI agents for chronic-care check-ins, medication checks, post-discharge calls (kidney failure, heart failure named). Depth 2 to 3.**
- Backers: $126M Series C, 3 Nov 2025, led by Avenir Growth; CapitalG, General Catalyst, a16z, Kleiner Perkins, Premji Invest, Universal Health Services and others took part; $3.5B valuation; total $404M. D2-06-F20 | CITED | https://siliconangle.com/2025/11/03/hippocratic-ais-valuation-soars-3-5b-raising-126m-new-funding/ | 2025-11-03 | OPENED.
- Loop: each agent passes "extensive safety training" with the creator and company staff before hospitals can use it; clinicians can build an agent in about 30 minutes; creators share revenue.
- Traction (THEIR CLAIM, Nov 2025): 50+ health systems, payers, pharma in six countries; 1,000+ clinical use cases; 115 million patient interactions, "no safety issues". D2-06-F21.
- India need: 2-minute consultations (D1-03-F24). Equivalents: 2care.ai (D1-04-F36).
- Differs in India: language mix; hospital customers few and price-sensitive.
- Borrow: a staged safety ladder (supervised calls first, then unsupervised only after testing) written as a one-page safety case.
- Demo potential: 4.

**17. 9amHealth (US). Virtual specialty care for obesity, diabetes, hypertension, lipids with medicine management and at-home labs. Depth 3 to 4 (page does not say who changes doses).**
- Backers: $26M Series B, 13 May 2026, led by Define Ventures; SemperVirens, Catalio, NewHealth Ventures new. Total raised conflicts: about $35M versus $55.2M (SNIPPET). D2-06-F22 | CITED | https://hitconsultant.net/2026/05/13/9amhealth-raises-26m-series-b-virtual-specialty-care/ | 2026-05-13 | OPENED.
- Loop: endocrinologists, obesity-medicine doctors, clinical pharmacists, 24/7 access. Payers: employers, plans, PBMs.
- Traction (THEIR CLAIM): "$50 million in projected medical and pharmacy savings" at two Fortune 100 employers (projections, not realised). D2-06-F23. No BP or diabetes outcome on the page.
- India need and equivalents: as entries 2 to 3. India differs: clinical pharmacist role barely exists in primary care (not checked, NOT FOUND).
- Borrow: put a pharmacist-style "titration desk" between app and doctor, as HyperLink did (D1-01-F04).
- Demo potential: 2.

### (c) Companions for weight-loss medicines and metabolic health

**18. Closed Loop Medicine, WeDosify (UK, US launch). Personalised GLP-1 dosing platform for clinicians. Depth 4 (dose options proposed, clinician reviews).**
- Launch: US, announced 18 Sep 2025 (article 19 Sep 2025); a US research site began use that week. Funding and investors NOT on the page; NOT FOUND. D2-06-F24 | CITED | https://www.cambridgenetwork.co.uk/news/closed-loop-medicine-launches-first-personalized-glp-1-dosing-platform-us | 2025-09-19 | OPENED. Press-release page (BusinessWire) returned 403.
- Inputs: tolerability, goals, clinical data, response to drug; model built on 29 studies and 15,000+ patient profiles with PK/PD modelling. FDA status not stated.
- Claims (THEIR CLAIM): 91% of surveyed GLP-1 patients said they would stay on treatment longer with support; up to 44% quit within 6 months and 60% within 12 (citing a 2021 paper). D2-06-F25.
- India: generic semaglutide from 21-22 Mar 2026 (D1-04-F10). Equivalent: Healthify, Tracky (D1-04-F26, F27, depth 3).
- Differs in India: price of drug, who prescribes (physician, not telehealth plan).
- Borrow: the closest published depth-4 pattern to the DT1 engine: protocol as data, options shown to the clinician, patient response fed back. Also shows the step rule can be the product.
- Demo potential: 4.

**19. Ilant (US). Matches members to GLP-1 or non-GLP-1 drugs, or behaviour or surgery, and adjusts the pathway as they respond. Depth 3 to 4.**
- Backers: $15M Series A, 5 Jun 2026, led by Cornucopian Capital; naturalX, Peakbridge, Semcap AI, Evidenced, Operator Partners; existing Celtic, LifeX, AlphaLab; total over $22M. D2-06-F26 | CITED | https://itbrief.co.uk/story/ilant-raises-usd-15-million-to-tackle-obesity-costs | 2026-06-05 | OPENED.
- Loop: clinician-led with software; payers are employers and plans; direct pricing via Lilly's Employer Connect and work with Novo Nordisk (late 2025).
- Traction (THEIR CLAIM): average 15% weight loss in early members. D2-06-F27.
- Borrow: a "when the first drug fails, what next" branch in the protocol, not only up-titration.
- Demo potential: 2.

**20. Signos (US). Over-the-counter CGM plus AI coaching for the GLP-1 era. Depth 3.**
- Backers: $20M, 27 May 2026; no lead named; GV (Google Ventures), Dexcom, Blue Cross Blue Shield of Alabama (via 450 Ventures) backed it; 2023 Series B led by Cheyenne Ventures and GV. D2-06-F28 | CITED | https://athletechnews.com/signos-secures-20m-to-scale-cgm-behavioral-coaching-in-the-glp-1-era/ | 2026-05-27 | OPENED.
- Loop: CGM shows which food spikes glucose; coaching layer; no medicine-dose guidance on the page. Traction (THEIR CLAIM): 10-fold growth in six months. D2-06-F29.
- India: CGM prices and Ultrahuman, Libre (D1-04-F33). Borrow: sensor on the patient for two weeks, then stop; reduces cost per patient.
- Demo potential: 2.

### (d) Infrastructure: wearable data and platforms

**21. Junction (formerly Vital; US/UK, YC). One API for 500+ wearables and lab ordering. Depth 0 (infrastructure).**
- Backers: $18M Series A, 11 Mar 2025, led by Creandum; Y Combinator, Point Nine, Amino Collective took part. D2-06-F30 | CITED | https://techcrunch.com/?p=2978519 | 2025-03-11 | OPENED.
- Traction (THEIR CLAIM, Mar 2025): 2M+ connected devices, 140+ healthcare customers, about 1M lab tests expected that year. D2-06-F31.
- India: Indian wearables (Noise, boAt, Ultrahuman) not checked. NOT SEARCHED.
- Borrow: one adapter that normalises readings from any cuff or watch to a single schema (value, time, device, quality); build the loop on the schema, not on a cuff brand.
- Demo potential: 3.

**22. Bevel (US). Software-only AI health companion on top of Apple Watch and other wearables, plus CGMs (Dexcom, Libre). Depth 3.**
- Backers: $10M Series A, 30 Oct 2025, from General Catalyst (page does not call it lead); GC and South Park Commons put $4M in an earlier 2025 seed. D2-06-F32 | CITED | https://techcrunch.com/2025/10/30/bevel-raises-10m-series-a-from-general-catalyst-for-its-ai-health-companion | 2025-10-30 | OPENED.
- Traction (THEIR CLAIM, Oct 2025): 100,000+ daily users; 80%+ retention at 90 days; $6 a month or $50 a year. D2-06-F33.
- Borrow: a hardware-free product that runs on devices people own; price point reference for consumer willingness.
- Demo potential: 4.

**23. Galen AI (US, YC Spring 2025; 2 people), acquired by Oura, Apr 2026.** Connected records from 800+ institutions (US, UK, Canada) and 20+ wearables (Apple Watch, Fitbit, Dexcom); Oura announced the deal 17 Apr 2026, price not disclosed. D2-06-F34 | CITED | https://hitconsultant.net/2026/04/23/oura-acquires-galen-ai-clinical-data-integration/ | 2026-04-23 | OPENED (date 17 Apr from search snippet). Depth 1 to 2. Borrow: a two-person team could reach exit by solving records plus wearables joining; the join is the value.

**24. Wellinks (US). Passive wearable plus RPM for COPD, extending to heart failure.** $10M first close of Series B, 5 Aug 2026, led by UMass Memorial Health; FDA-cleared Spire system; THEIR CLAIM: over 60% lower odds of 30-day readmission in a joint study (undated detail). Medication changes not mentioned. D2-06-F35 | CITED | https://hitconsultant.net/2026/08/05/wellinks-secures-10m-series-b-funding-predictive-cardiopulmonary-rpm/ | 2026-08-05 | OPENED. Depth 1 to 2. Borrow: a hospital as lead investor; sell to the system that owns the readmission cost.

### (e) New sensors and tests

**25. Biobeat (Israel). Disposable cuffless chest patch for 24-hour blood pressure. Depth 1.**
- Backers: $50M Series B, 31 Dec 2025, from Ally Bridge Group, OrbiMed, Elevage Medical (new); a strategic investor took part. Page does not say lead; the search snippet named Ally Bridge and OrbiMed as leads (SNIPPET). D2-06-F36 | CITED | https://pulse2.com/biobeat-50-million-series-b-secured-to-expand-u-s-commercialization-of-cuff-less-24-hour-blood-pressure-monitoring/ | 2025-12-31 | OPENED.
- Device: described on page as FDA-cleared; no sales or study details. Reports into medical record. No therapy change.
- India: Omron HEM-7156T about ₹2,600 (D1-06-F07, SNIPPET) is the cost to beat. Borrow: 24-hour ambulatory pattern as a one-off confirmation before stepping up. Demo potential: 1.

**26. Aktiia / Hilo (Switzerland). Cuffless wrist band for blood pressure, FDA OTC 510(k) July 2025. Depth 1.**
- Backers: $42M Series B, May 2025, co-led by Earlybird Health and Wellington Partners; earlier CHF 27M (2024), $17.5M Series A (2021). Total above $100M. D2-06-F37 | CITED | https://hlth.com/insights/news/aktiia-gets-fda-clearance-for-otc-cuffless-blood-pressure-monitor-2025-07-08 | 2025-07-08 | OPENED. A $19M extension (total over $119M) is SNIPPET, undated.
- Device: optical wrist sensor, pulse-wave algorithm, readings only at rest; CE-marked Class IIa; the search snippet said it needs cuff calibration (SNIPPET); page says a separate "calibration-free" version exists. US consumer availability expected 2026.
- Regulation context: FDA reissued General Wellness guidance on 6 Jan 2026 so some noninvasive BP estimates can be sold as wellness products (SNIPPET, law-firm summaries).
- Borrow: cuff-calibrated cuffless trend as an input only; keep decisions on cuff readings. Demo potential: 1.

**27. Vital Signals (US). Hypertension monitoring startup, over $15M, 19 May 2026, led by XYZ Ventures.** Technology undisclosed; the article's cuffless guess is speculation; not FDA cleared; no traction. D2-06-F38 | CITED | https://briefglance.com/articles/vital-signals-15m-bid-to-tame-the-silent-killer-blood-pressure | 2026-05-19 | OPENED (secondary site). Depth 1. Demo potential: 1.

**28. Biolinq (US). Needle-free intradermal glucose patch "Shine", FDA de novo 23 Sep 2025, for type 2 diabetes not on insulin. Depth 1.**
- Backers: $100M raised earlier in 2025 (Series C, Apr 2025 per SNIPPET), $58M Apr 2024 (SNIPPET); leads not named on the opened page. D2-06-F39 | CITED | https://medtechdive.com/news/biolinq-de-novo-diabetes-clearance-cgm/761303 | 2025-09-26 | OPENED.
- Device: forearm patch with a colour LED that shows in-range or high glucose, no phone needed.
- India: Libre and Ultrahuman CGM exist (D1-04-F33). Borrow: a glanceable LED result suits low-literacy users; same idea for a BP clip that shows green, amber, red. Demo potential: 2.

**29. SiPhox Health (US).** $27M ($10M seed plus $17M Series A led by Intel Capital), 2023, outside the window; fingerprick home test of 17 biomarkers mail-in. Only SNIPPET; listed so the report writer knows the at-home blood-test searches found no 2026 round. D2-06-F40 | SNIPPET | https://pulse2.com/siphox-health-27-million-funding/ | 2023. Helios Intelligence (YC Fall 2026, 5 people): at-home test of 1,000+ biomarkers from a drop of blood; Mirror text only, funding NOT FOUND, D2-06-F41 | Mirror | OPENED.

### (f) Prevention and "health check" companies

**30. Function Health (US). Subscription blood testing (160+ lab tests), imaging, AI explanations. Depth 1 to 2.**
- Backers: $298M Series B, led by Redpoint Ventures, a16z, Aglae Ventures, Battery, NFDG, QuantumLight, Samsung Next; $2.5B valuation; date conflicts: 19 Nov 2025 (Axios, SNIPPET) versus 23 Nov 2025 (Pulse 2). Prior $53M Series A led by a16z (SNIPPET). D2-06-F42 | CITED | https://pulse2.com/function-health-298-million-series-b/ | 2025-11-23 | OPENED.
- Traction (THEIR CLAIM): hundreds of thousands of members; 50M+ lab tests since 2023; annual price cut from $499 to $365. D2-06-F43. Feeds ChatGPT Health and Claude (entries 11, 12).
- India need: no data pulled here. Equivalent: Neodocs smartphone urine strip, $2M seed 2024 (D1-04-F31); Healthians/Redcliffe-type labs NOT SEARCHED.
- Borrow: re-test loop: results, plan, retest in 3 to 6 months; Lucis reports 80% retest. Demo potential: 2.

**31. Lucis (France, YC Spring 2025). "Function Health for Europe", 110+ blood biomarkers, AI companion, physicians review. Depth 3.**
- Backers: $20M Series A, 26 May 2026, led by Singular; General Catalyst, YC; seed $8.5M Dec 2025 led by General Catalyst (SNIPPET lead). D2-06-F44 | CITED | https://tech.eu/2026/05/26/lucis-raises-20m-series-a-to-expand-ai-driven-preventive-healthcare-platform/ | 2026-05-26 | OPENED.
- Traction (THEIR CLAIM): 10,000+ users; 1M+ biomarker tests; 75% of six-month completers improved three or more biomarkers without medicine; 80%+ retest. D2-06-F45. Conflicting seed-year numbers: 3K users at one report (SNIPPET).
- Borrow: report "share improving 3+ markers at 6 months" as the headline metric; a team of 20 with a medical board of 10+ doctors reviewing. Demo potential: 2.

**32. Superpower (US). Biannual blood tests (100+ biomarkers) at home or partner labs.** $30M Series A, Apr 2025, led by Forerunner Ventures, above $300M valuation (SNIPPET); Function Health sued it on 26 Jan 2026 over claims (SNIPPET, aggregator). D2-06-F46 | SNIPPET | https://sacra.com/research/superpower | 2025-04. Depth 1 to 2. Borrow: avoid claims about biomarkers or "24/7" you cannot prove; copy check.

## What Y Combinator and a16z say (2025 and 2026)

All quotes 25 words or fewer, from pages opened unless marked.
- YC Requests for Startups, Winter 2027 page (opened 13 Nov 2026): no healthcare item on chronic care, AI doctors or devices. Closest: "There are millions of jobs like this in benefits, taxes, insurance claims, medical billing, and immigration paperwork." (The $15-an-Hour Expert, Brad Flora). D2-06-F47 | https://www.ycombinator.com/rfs?year=2026 | OPENED.
- YC Summer 2026 RFS, as summarised by a secondary newsletter dated 28 Apr 2026: item "AI Personalized Medicine": "The future of medicine is not population-level treatment. It is one patient, one protocol." This is the newsletter's text, not confirmed on YC's own page. D2-06-F48 | https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas | 2026-04-28 | OPENED, secondary. Same article lists "Healthcare administration" under AI-native services.
- a16z, "Infinite Healthcare: What's It Worth?", 26 Feb 2026 (Jay Rughani, Jane Rhee, Julie Yoo): "AI drives the marginal cost of that work toward zero." Page uses "continuous monitoring, early intervention" but does not discuss titration or wearables. D2-06-F49 | https://a16z.com/infinite-healthcare-whats-it-worth/ | OPENED. A search snippet said the piece cites hypertension, diabetes and obesity affecting 75% of US adults (SNIPPET, not seen on the opened page).
- a16z, "The State of Longevity", 3 Nov 2026 (Daisy Wolf, Eva Steinman): "Knowing your numbers is the starting point. The opportunity is helping people act on them." Also says 55% of wearable users report their data never prompted a behaviour change or doctor visit (THEIR figure, source not checked). D2-06-F50 | https://a16z.com/the-state-of-longevity/ | OPENED.
- a16z, Counsel Health post, 16 Oct 2025: Counsel is "a full-stack, AI native medical group that makes medical care abundant." D2-06-F51 | https://a16z.com/announcement/investing-in-counsel-health/ | OPENED.
- a16z Big Ideas 2026 via Fitt Insider summary, 6 Jan 2026 (Julie Yoo's view as reported): "healthy MAUs could become the largest and most valuable user base in healthtech." Secondary summary, not a16z's own text. D2-06-F52 | https://insider.fitt.co/the-new-economics-of-preventative-health-a16z/ | OPENED.
- Pattern across the above: the investor essays talk about AI as cheap clinician time and about acting on numbers; none opened mentions dose titration by rule.

## NOT FOUND / NOT SEARCHED

- NOT FOUND: any 2025 to 2026 startup raise whose page describes autonomous or clinician-signed home blood-pressure dose steps by protocol (Cadence is the nearest; its page says "supports" medicine changes).
- NOT FOUND: funding for Closed Loop Medicine, Juno, Prana, Clara, Helios; round date and lead for Kivo.
- NOT FOUND: heart-failure or kidney-specific funded startups for 2025-26 (searches did not surface any; PHTI CKD verdict is in D1-05-F10). Selera Medical (YC W24, heart-failure implant) is marked Inactive on the YC mirror.
- NOT FOUND: official YC page text for "AI Personalized Medicine"; OpenAI's own launch page (403); Google Health and Microsoft Copilot Health pages (SNIPPET only).
- NOT FOUND: any Indian availability of ChatGPT Health, Claude health integrations, Google Health coach or Copilot Health.
- NOT SEARCHED: Japan-based or Indian-market wearable data firms; Embla (Denmark, EUR 10M Series A, titration algorithm, SNIPPET lead only), Vitl ($7.5M seed, GLP-1 prescribing software, SNIPPET lead only), Brook.ai ($28M Series B late 2025, hypertension and heart-failure RPM, SNIPPET lead only), HealthSnap ($25M, 2024), Murj RPM launch (18 Aug 2026), Hera ($27M, Jun 2026), Thesis Care ($45M Series A, Mar 2026), Dimer Health ($13.5M).
- NOT SEARCHED: Mito Health (YC S24, at-cost labs; Mirror only), Amby Health, Nori (YC Fall 2025), Illume Labs, Aidy, Copper Health (YC; Mirror only, no funding looked up).
- Wide-rollout date of ChatGPT Health conflicts between sources (7 Jan 2026 announcement; 23 Jul "widely available" in a snippet).
- No Indian equivalent check was made beyond the D1-04 table.

Searches used: 23
