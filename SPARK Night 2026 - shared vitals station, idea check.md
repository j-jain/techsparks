# Shared vitals station: idea check

16 Nov 2026. The idea: one cheap machine that takes all the readings Biofourmis tracks. It would be sold to hospitals, pharma companies, care homes and rural clinics on a subscription, with AI to help doctors and nurses spot who is getting worse. "Like Cadence, but rural."

How to read this note. Fact IDs link to their sources, and the register at the end lists each one. Tags mark what is not a sourced fact:

- OUR VIEW: a judgement.
- OUR ESTIMATE: a rough number.
- ASSUMPTION: something to test.
- OUR DESIGN: a choice made for the product.
- TARGET: a pass bar for the pilot.
- NOT RESEARCHED or NOT FOUND: a gap.

## The answer

Build it, but not as "one machine for everything". Build a **shared vitals station for nurse rounds**: one cart per ward. It takes a two-minute spot check, charts it, scores it, and ranks the ward's patients for the doctor. OUR VIEW. Five reasons:

- **One station cannot take the whole Biofourmis list.** It can take about 9 of the 14 kinds of reading well. Sleep, steps, gait, scratching, skin response and overnight trends need a band worn day and night (section 1). OUR VIEW
- **Readings alone do not make patients better; acting on them does.** Monitoring-only BP programmes gave no clinically meaningful fall in BP. Programmes with a care team that changed medicines did ([D1-05-F1](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf), [D1-05-F2](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf)). Cadence, the model named in the idea, ships a cuff (plus a scale for heart failure), and what it really sells is the care team ([D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care)). Biofourmis measured far more, and cut 120 jobs about a year after reaching a $1.3B valuation ([D5-01-F10](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally)).
- **The hospital ward is the best first buyer.** In one Lucknow study, manual checks ran every 3-6 hours with one health worker per 36 patients ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)). Charts are often incomplete ([D5-01-F03](https://pmc.ncbi.nlm.nih.gov/articles/PMC10905788/), [D5-01-F04](https://caho.in/files/2nd-Debjanee%20Mukherjee-Clinical%20audit%20MEWS%20%282%29.pdf)). Hospitals already pay for ward monitoring ([D5-01-F06](https://analyticsindiamag.com/ai-features/dozee-harness-ai-for-personalised-patient-care), [D5-01-F08](https://www.mynewsdesk.com/uk/isansys-lifecare-ltd/news/indias-manipal-hospitals-partners-with-isansys-lifecare-to-launch-remote-patient-monitoring-technology-455613)). The other buyers are weaker for now:
  - Care homes are too few to be the market ([D5-01-F12](https://therealtytoday.com/news/market-insights/indias-senior-living-market-to-reach-15000-homes-by-2030-with-26000-crore-investment-asli-jll-india-report/), [D5-01-F13](https://bsppd.business-standard.com/amp/india-news/senior-living-rents-touch-1-lakh-retirement-homes-valued-at-8-4-billion-125071600004_1.html)).
  - Pharma trials need proof a new company will not have for a year or more ([D5-01-F19](https://iscr.org/files/Article/1317861265_ISCR-DCT-Position-Paper-[Fina.pdf)).
  - Villages have the need but the weakest payer ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html)).
- **There is a price gap.** One reseller lists a spot-check monitor with an early-warning score at about ₹1.15 lakh. Generic spot-check monitors cost ₹12-35 thousand, with no score and no link to records ([D5-01-F24](https://www.aajjo.com/product/welch-allyn-connex-spot-monitor-in-delhi-medisure-inc)). A station at roughly ₹20-30 thousand plus software would sit between them. OUR ESTIMATE
- **Version 1 is rules, not AI.** The early-warning score nurses use (NEWS2) is a points table ([D5-01-F23](https://www.rcp.ac.uk/media/ctulqqbn/news2-executive-summary_0.pdf)). Learning comes later, from the pilot's own data.

Next step: a two-week bench test, then a four-to-six-week pilot in one general ward of about 30 beds (section 7).

## 1. What one station can and cannot read

| Reading | Can a spot-check station take it? | Is a cheap sensor good enough? | In version 1? |
|---|---|---|---|
| Heart rate, beat-to-beat interval | Yes | Yes: finger clip or one-lead ECG | Yes |
| Heart rhythm (for example AF) | Yes, a 30-second ECG strip | Yes, with a one-lead ECG | Version 1.5 |
| Heart rate variability (HRV) | Only a snapshot; it means more as an overnight trend | Fine at rest | Later (band) |
| Pulse-wave shape | Yes | Research grade, little proven clinical use | No |
| Blood pressure | Yes, **with a cuff** | Only a validated cuff. Cuffless BP has no accepted validation protocol ([D2-02-F25](https://pubmed.ncbi.nlm.nih.gov/37303198/)), and a 2025 review found no proof that it adds value ([D2-02-F26](https://pubmed.ncbi.nlm.nih.gov/40231350/)) | Yes (cuff) |
| Breathing rate | Yes | A guided count by the nurse now; an estimate from the sensor later | Yes |
| Oxygen saturation (SpO2) | Yes | Yes, but finger oximeters can read high on darker skin ([D5-01-F14](https://psnet.ahrq.gov/issue/racial-bias-pulse-oximetry-measurement)) | Yes, with a caution band |
| Temperature | A fever check only; trends need a band | Yes | Yes (spot) |
| Skin response (EDA) | No, it needs a wrist band | Noisy, weak clinical use | No |
| Steps, gait, posture, energy | No | Yes, in a band | Later (band) |
| Sleep, night-time scratching | No | Partly, in a band | Later (band) |
| Weight | Yes, a scale plate | Yes; key for fluid build-up in heart failure | Later (heart-failure protocol) |
| Symptoms (patient-reported) | Yes, on screen or by voice | Software | Yes, voice in local languages (version 1.5) |
| Medicine taken? | Ask, or use a pill box | No vital sign shows it: amlodipine and telmisartan leave no pulse sign ([D4-05-F16](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=abd6a2ca-40c2-485c-bc53-db1c652505ed), [D4-05-F18](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bb7bc69-7752-4c16-9c60-e61eb5355a4d)) | Not on the ward; yes at home |

So a station covers the six readings a ward early-warning score needs, plus symptoms and rhythm. The rest wait for an optional band, which only some patients need, for example after a heart-failure discharge or in a trial. OUR VIEW

## 2. Why the loop matters more than the sensors

The independent PHTI review of digital hypertension programmes split them into three kinds ([D1-05-F1](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf), [D1-05-F2](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf)):

- Monitoring only: BP fell a little more than usual care, but not by a clinically meaningful amount.
- Behaviour change: limited effect.
- A virtual care team that adjusts medicine: the only kind with a clinically meaningful fall.

Cadence is in the last group. Its health-system partners ship only a cuff, or a cuff and a scale for heart failure. Readings go over the mobile network, and a 24/7 team manages the medicines ([D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care)). Cadence raised a $100M Series C in June 2026 ([D2-06-F1](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/)). Its value is the loop and the US payment code, not the device.

The loop has four parts: a reading, a score, a named person who acts by a set time, and a log of all of it. On a ward the action is an escalation (the nurse calls the doctor, who reviews the patient), not a medicine change. That keeps the rules lighter (section 6). In the home BP loop from the adaptive-care pack, the action is a medicine step the doctor approves. Both run on the same station software. OUR VIEW

## 3. Four buyers, one first

| Buyer | The pain | Who pays | What the checks found | Verdict (OUR VIEW) |
|---|---|---|---|---|
| General wards in tier-2/3 private and government hospitals | Checks every 3-6 hours; one health worker per 36 patients at KGMU ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)). In one Kenyan audit, 70% of patients who died had no breathing rate charted in their last 24 hours ([D5-01-F03](https://pmc.ncbi.nlm.nih.gov/articles/PMC10905788/)) | The hospital; CSR or development money for public hospitals ([D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/)) | Ward monitoring is already sold and bought ([D5-01-F06](https://analyticsindiamag.com/ai-features/dozee-harness-ai-for-personalised-patient-care), [D5-01-F08](https://www.mynewsdesk.com/uk/isansys-lifecare-ltd/news/indias-manipal-hospitals-partners-with-isansys-lifecare-to-launch-remote-patient-monitoring-technology-455613)) | **First buyer** |
| Rural clinics and village health centres | No doctor on site; BP and diabetes follow-up drops off | The government; small fees from patients | PMJAY does not cover outpatient care ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html)). The government's IHCI programme already logs BP in the Simple app, and 47% of patients under care have it controlled ([D1-04-F19](https://pmc.ncbi.nlm.nih.gov/articles/PMC10959138/)) | Phase 2, same station, offline |
| Elder-care homes | Staff cannot watch everyone at night | Families, through the home's fee | 22,157 organised senior-living units, mostly flats, not care beds ([D5-01-F12](https://therealtytoday.com/news/market-insights/indias-senior-living-market-to-reach-15000-homes-by-2030-with-26000-crore-investment-asli-jll-india-report/)); about 2,100 assisted-living beds ([D5-01-F13](https://bsppd.business-standard.com/amp/india-news/senior-living-rents-touch-1-lakh-retirement-homes-valued-at-8-4-billion-125071600004_1.html)) | A friendly pilot site, not a market |
| Pharma remote trials | Site visits are costly; sponsors want home data | Sponsor or CRO, at high prices | No CDSCO guidance on decentralised trials found ([D5-01-F19](https://iscr.org/files/Article/1317861265_ISCR-DCT-Position-Paper-[Fina.pdf)) | Year 2 or later |

Why private tier-2/3 hospitals first: they decide faster than the government. Their budgets are tight, though: in Haryana, half the empanelled private hospitals paused PMJAY services over unpaid dues ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html)). Government wards can follow with CSR or development-finance money, the route Dozee used ([D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/)). OUR VIEW

## 4. Who is already there

| Who | What it is | Model and scale | What it means for this idea (OUR VIEW) |
|---|---|---|---|
| Dozee (Bengaluru) | Sensor under the mattress; continuous readings and an early-warning score | One device per bed. Price not public; company figures disagree ([D5-01-F06](https://analyticsindiamag.com/ai-features/dozee-harness-ai-for-personalised-patient-care), [D1-04-F20](https://yourstory.com/2023/04/dozee-raises-6-million-in-series-a2-funding-round)) | Strongest ward rival. It sells continuous monitoring and this idea sells rounds. Its own study found specificity of 19-42%, meaning many alerts on patients who did not get worse ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)); fewer alarms is a selling point for rounds |
| Isansys at Manipal; Midmark ib.digi; Max Healthcare | Ward monitoring with early-warning scores | Large hospital chains ([D5-01-F08](https://www.mynewsdesk.com/uk/isansys-lifecare-ltd/news/indias-manipal-hospitals-partners-with-isansys-lifecare-to-launch-remote-patient-monitoring-technology-455613)) | The big chains are taken |
| Welch Allyn Connex Spot, Draeger Vista 120 SC, Philips MP5SC | Spot-check monitors with built-in early-warning scores | Connex at about ₹1.15 lakh from one reseller ([D5-01-F24](https://www.aajjo.com/product/welch-allyn-connex-spot-monitor-in-delhi-medisure-inc)) | The same idea at about four to five times the target price. OUR ARITHMETIC |
| Generic spot-check monitors (Contec and others) | Readings only | ₹12-35 thousand ([D5-01-F24](https://www.aajjo.com/product/welch-allyn-connex-spot-monitor-in-delhi-medisure-inc)) | Cheap, but no score, no chart, no ranked list |
| YOLO Health ATMs | Walk-up kiosk, "48 tests" | ₹50-100 a check at railway stations; a 500-kiosk plan in 2023 ([D5-01-F09](https://www.outlooktraveller.com/travelnews/lucknow-railway-station-gets-health-atms)) | No 2025-26 news found; readings without follow-up |
| IHCI and the Simple app | Government BP programme | Free ([D1-04-F19](https://pmc.ncbi.nlm.nih.gov/articles/PMC10959138/)) | Plug into it in villages; do not compete with it |
| Cadence (US) | Home cuff and scale plus a care team | Medicare pays ([D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care)) | Proves the loop, not the box |
| Biofourmis (US, Singapore) | Wearable plus AI platform | $300M Series D, then 120 layoffs and a CEO exit ([D5-01-F10](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally)) | A warning about selling "measure everything" |

**The gap (OUR VIEW).** Wards that will not buy one device per bed, or a monitor costing a lakh, need a cheap shared station. It must chart, score and rank automatically, work offline, and speak local languages. These searches found no Indian firm selling exactly that, but they were not exhaustive (NOT RESEARCHED beyond D5-01).

**A cheaper variant to test (OUR VIEW):** software only, reading data from the generic monitors that wards already own. Whether those monitors can export data was NOT RESEARCHED.

## 5. The product: a vitals round in two minutes

How one round works (OUR DESIGN):

1. The nurse scans the patient's wristband QR code (or ABHA ID). The right patient is the first safety check.
2. Cuff and finger clip go on, and an IR thermometer takes the temperature. Readings arrive over Bluetooth, with no typing.
3. Breathing rate: the screen runs a 30-second count and the nurse taps each breath. This is the reading most often skipped ([D5-01-F03](https://pmc.ncbi.nlm.nih.gov/articles/PMC10905788/)). A camera or sensor estimate can come later.
4. The nurse taps the patient's level of consciousness (alert, voice, pain, unresponsive, or new confusion) and whether they are on oxygen.
5. The station works out the NEWS2 score ([D5-01-F23](https://www.rcp.ac.uk/media/ctulqqbn/news2-executive-summary_0.pdf)), shows its colour, and states the hospital's own escalation rule ("call the doctor within 30 minutes").
6. The doctor's screen lists the whole ward ranked by score and trend, so 30 patients can be scanned in a few minutes (OUR DESIGN). Tap a patient to see the chart.
7. Every round is logged: time, nurse, readings, score, escalation, and how long the doctor took to respond.
8. It works offline first: the tablet stores readings and syncs when the network returns.

Version 1.5 adds voice symptom questions in Hindi and local languages at step 4, and a one-lead ECG strip.

What AI adds later (OUR VIEW):

- a personal baseline for each patient, with trend flags
- "who to see first", trained with consent on the hospital's own outcomes
- voice turned into the nurse's note

The bar to beat is fewer false alarms than continuous systems ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)).

Protocols that come later, on the same software:

- the home BP loop from the adaptive-care pack
- heart failure: weight, BP and symptoms, the kit Cadence uses ([D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care))
- a band, for patients who need continuous readings

## 6. Rules and money

**Hardware rules**

- Buy licensed devices: a BP monitor, an oximeter and a thermometer. Sources disagree on classes. One says a fingertip oximeter is Class B, another Class C; ICU multiparameter monitors are Class C ([D5-01-F17](https://medicaldialogues.in/news/industry/pharma/dcgi-classifies-112-medical-devices-related-to-anesthesiology-80009)).
- Building your own sensors into one box makes you the maker of a multiparameter monitor, which needs your own licence.
- For version 1, sell licensed devices plus software. OUR VIEW

**Software rules**

- The class depends on the stated intended use ([D2-04-F02](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf)). Reading the same CDSCO table as the adaptive-care pack, a BP step that a doctor approves comes out as Class B (D2-04-F06).
- A ward score deals with possibly critical conditions. A score that only informs the nurse may sit at Class B; one that drives decisions may be Class C. OUR VIEW. CDSCO confirms the class on review (D2-04-F06).
- Word the intended use carefully: "charts and scores readings for the nurse; the clinician decides".

**Oximeters on darker skin**

- Among patients reading 92-96%, true saturation below 88% was found in 11.7% of Black and 3.6% of White patients ([D5-01-F14](https://psnet.ahrq.gov/issue/racial-bias-pulse-oximetry-measurement)).
- The FDA's January 2025 draft guidance asks makers to test across skin tones ([D5-01-F16](https://www.govinfo.gov/content/pkg/FR-2025-01-07/html/2024-31540.htm)). No Indian data was found ([D5-01-F15](https://pubmed.ncbi.nlm.nih.gov/39196478/)).
- Design rule: SpO2 alone never marks a patient safe, and readings of 92-96% are flagged for a second look. OUR DESIGN

**Patient data**

- Consent and data rules (DPDP Act): NOT RESEARCHED here.

**Who pays**

- No public payer: PMJAY excludes outpatient care and has no remote-monitoring package ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html), [D2-04-F34](https://mail.caalley.com/irda24/Master_Circular_on_Health_Insurance_Business_29052024.pdf)).
- So the hospital pays for what it gets back: nurse time, complete charts, escalations on time, and perhaps accreditation (NABH rules NOT RESEARCHED).
- Nurse time is not yet measured well. The only Indian figure found, 10% of staff time on vitals and documentation, came from one resident over one day, in a study by the maker ([D5-01-F02](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)). The pilot should measure it.
- Price to test: about ₹3,000 per station per month, hardware included, which is about ₹100 per bed per month at 30 beds. ASSUMPTION
- For public hospitals: CSR or development-finance money, as with MillionICU ([D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/)).

## 7. MVP: build, bench test, pilot

**Pilot station, parts list (OUR ESTIMATE unless a fact ID is given)**

| Part | Pilot choice | Rough price |
|---|---|---|
| Upper-arm BP monitor | Licensed, for example Omron HEM-7156T (check Bluetooth) | ₹2,600-2,900 ([D5-01-F21](https://www.smartprix.com/monitors/omron-hem-7156t-digital-bp-monitor-ppd1lm03clem)) |
| SpO2 and pulse | Licensed fingertip oximeter with Bluetooth | NOT RESEARCHED |
| Temperature | Licensed IR thermometer | NOT RESEARCHED |
| Breathing rate | On-screen tap counter | Software |
| Tablet | Android tablet, 10 inch | ₹10,000-15,000 (ASSUMPTION) |
| Hub for devices without Bluetooth | ESP32 board | about ₹500 (ASSUMPTION) |
| Cart, battery pack, QR wristbands | Off the shelf | ₹3,000-5,000 (ASSUMPTION) |
| **Total** | | **₹20,000-30,000 per station (OUR ESTIMATE)**; about ₹700-1,000 per bed at 30 beds (OUR ARITHMETIC) |

A learning build with hobby modules costs much less: pulse-oximeter module ₹99-199, ECG module ₹649, IR sensor ₹799 ([D5-01-F22](https://probots.co.in/max30102-pulse-oximeter-heart-rate-sensor-module-gy-max30102.html)). It is not for patients, because it has no licence and no validation.

**Bench test, two weeks (OUR DESIGN)**

- 20 adult volunteers, with consent.
- Each is measured by the station and by a reference: a second validated cuff, a second licensed oximeter, a clinical thermometer, and two people counting breaths for a full minute.
- Report the mean difference and spread for each reading, every capture error, and the time per patient.
- The devices are already licensed, so this test checks the station's flow (right patient, right reading, nothing lost), not sensor accuracy.
- TARGET: zero wrong-patient or missing entries, and under two minutes per patient.

**Pilot, four to six weeks, one general ward of about 30 beds (OUR DESIGN)**

- Weeks 1-2: paper charts as usual, timed and audited.
- Then 2-4 weeks with the station.
- Ask the hospital's ethics committee for its view first, even for a quality project. OUR VIEW

| Measure | How | Pass bar |
|---|---|---|
| Minutes per patient per round | Stopwatch, 10 rounds in each phase | 30% less than paper (TARGET) |
| Complete rounds | All six NEWS2 readings present | Above 90% (TARGET) |
| Score correct | Re-score 50 rounds by hand | 100% (TARGET) |
| Escalations on time | Against the hospital's own rule | Better than baseline (TARGET) |
| Alarms per patient-day | From the log | Reported, and lower than continuous systems (TARGET) |
| Nurse view | Five-question survey | Most nurses want to keep it (TARGET) |

One ward cannot show an effect on ICU transfers or deaths: KGMU saw 33 deteriorations among 706 patients over four months ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)). Outcome proof needs a multi-ward study later.

## 8. Open questions

- Dozee's price per bed, and whether it sells to small hospitals. None found ([D5-01-F06](https://analyticsindiamag.com/ai-features/dozee-harness-ai-for-personalised-patient-care)).
- Can the generic monitors already on wards export data? (This decides the software-only variant.)
- Indian data on oximeter error by skin tone ([D5-01-F15](https://pubmed.ncbi.nlm.nih.gov/39196478/)).
- The official CDSCO entries for oximeters, IR thermometers and spot-check monitors ([D5-01-F17](https://medicaldialogues.in/news/industry/pharma/dcgi-classifies-112-medical-devices-related-to-anesthesiology-80009)).
- How many small private hospitals and nursing homes exist, and whether NABH asks for early-warning scores.
- Real nurse-to-patient ratios on Indian wards. Only old norms and one maker-linked study were found ([D5-01-F20](https://thieme-connect.com/products/ejournals/abstract/10.1055/s-0043-1761938), [D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)).
- Whether hospitals will pay the test price. ASSUMPTION

## Sources

| Fact | What the note records | Source | Read as | Claims check |
|---|---|---|---|---|
| D1-04-F19 | IHCI/Simple, SNIPPET | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10959138/), [2](https://simple.org/) | SNIPPET | not re-checked |
| D1-04-F20 | Dozee, SNIPPET | [yourstory.com](https://yourstory.com/2023/04/dozee-raises-6-million-in-series-a2-funding-round) | SNIPPET | not re-checked |
| D1-05-F1 | PHTI Digital Hypertension Management, Oct 2024 (PDF modified 2024-10-18). Groups by approach: (1) BP Monitoring (AMC Health, HRS, VitalSight/Omron); (2) Medication Management with a virtual care team incl. a prescriber (Cadence, … | [phti.org](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf) | OPENED | CONFIRMED |
| D1-05-F2 | Same report, ratings: Medication Management = "clinically meaningful and more rapid declines in SBP vs usual care", evidence certainty HIGHER, raises net spending in the 3-year window but may offset costs over a decade; rating "e… | [phti.org](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf) | OPENED | not re-checked |
| D2-02-F25 | ESH recommendations for validating cuffless BP devices, J Hypertens 2023, PMID 37303198: says there are "no generally accepted protocols"; proposes six tests (static, device position, treatment, awake/asleep, exercise, recalibrat… | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37303198/) | OPENED | CONFIRMED |
| D2-02-F26 | "Cuffless Blood Pressure Measurement: Where Do We Actually Stand?", Hypertension 2025, PMID 40231350: "no compelling evidence that pulse wave analysis and pulse arrival time can provide significant added value"; many accuracy cla… | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40231350/) | OPENED | not re-checked |
| D2-04-F2 | [LAW, restated in GUIDANCE s.7.0]: MDR 2017 Rule 4 classes: "Low risk Class A; Low moderate risk Class B; Moderate high risk Class C; High risk Class D" (Table 1) [meaning: four risk classes, A lowest]. Class "fundamentally based… | [cdsco.gov.in](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf), [2](https://www.nishithdesai.com/research-and-articles/hotline/pharma-healthcare-update/from-code-to-compliance-decoding-indias-medical-device-software-guidance-15623), [3](https://www.pureglobal.com/news/india-cdsco-medical-device-software-guidance-2026) | OPENED | not re-checked |
| D2-04-F6 | [OUR ARITHMETIC from F03] Reading the matrix: BP step-protocol proposal approved by a doctor = "drive clinical management" x "serious" = Class B, or x "non-serious" = Class A. If read as "treatment" x serious = Class C. Insulin d… | see note |  | not re-checked |
| D2-04-F34 | NOT SEARCHED: AB-PMJAY scope (lead: hospitalisation cover ₹5 lakh per family per year, secondary and tertiary inpatient care only); NP-NCD free drugs at Ayushman Arogya Mandirs; any government payment for remote monitoring or DTx… | [mail.caalley.com](https://mail.caalley.com/irda24/Master_Circular_on_Health_Insurance_Business_29052024.pdf) |  | not re-checked |
| D2-06-F1 | Backers: $100M Series C, 23 Jun 2026, led by Spark Capital; Thrive Capital, General Catalyst, Coatue, B Capital, Corewell Health Ventures, Memorial Hermann, Duke Health took part. Valuation not on the page. D2-06-F1 / CITED / / 2… | [pulse2.com](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/) | SNIPPET | CONFIRMED (date differs by one day between pages) |
| D4-05-F16 | Amlodipine does not change heart rate on chronic dosing / Norvasc label: chronic dosing lowers supine and standing BP "not accompanied by a significant change in heart rate or plasma catecholamine levels". Acute IV amlodipine rai… | [dailymed.nlm.nih.gov](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=abd6a2ca-40c2-485c-bc53-db1c652505ed) | OPENED | CONFIRMED |
| D4-05-F18 | Telmisartan: no heart-rate change; renin and angiotensin II rise / Micardis label: "There were no changes in the heart rate of patients treated with telmisartan in controlled trials." AT1 blockade removes angiotensin II's negativ… | [dailymed.nlm.nih.gov](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bb7bc69-7752-4c16-9c60-e61eb5355a4d) | OPENED | CONFIRMED |
| D5-01-F1 | KGMU Lucknow study of Dozee-EWS (Yadav et al., Frontiers in Medical Technology, 29 Aug 2024): prospective single-centre cohort, two medicine wards with 72 beds, Oct 2022 to Jan 2023, 706 patients, 84,448 monitoring hours. Manual … | [frontiersin.org](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full) | OPENED | not re-checked |
| D5-01-F2 | Same paper: "HCP spend 10% of their time on vital signs check and documentation", from a time-motion study of one junior resident over one 24-hour weekday; its Figure 3 shows vital checks at 7.6%. / / OPENED | [frontiersin.org](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full) | OPENED | not re-checked |
| D5-01-F3 | Kenya (Mbuthia et al., BMC Nursing 2024;23:143): 405 records of adults who died of cardiac arrest in 2019, three coastal hospitals. In the 24 h before death, 283 (70%) had no respiratory rate documented; 5 of 405 (1.2%) had all s… | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10905788/) | OPENED | not re-checked |
| D5-01-F4 | Tata Medical Center MEWS audit (CAHO poster): documentation non-compliance rose from 12% to 29% between audit cycles; escalation non-compliance from 12% to 14%. | [caho.in](https://caho.in/files/2nd-Debjanee%20Mukherjee-Clinical%20audit%20MEWS%20%282%29.pdf) | SNIPPET | not re-checked |
| D5-01-F6 | Dozee scale, company figures that disagree and are undated: "300+ hospitals, 18,000+ active beds" in one source; "50,000 beds across 200+ hospitals in 50 cities" in another. No hospital per-bed price found. A 2021 report says hos… | [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/dozee-harness-ai-for-personalised-patient-care) | SNIPPET | not re-checked |
| D5-01-F7 | Dozee MillionICU (launched 2021): convert government ward beds into connected step-down ICU beds; with British International Investment, upgrade 6,000 beds in about 140 public hospitals. Sattva impact report (company-commissioned… | [bii.co.uk](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/) | SNIPPET | not re-checked |
| D5-01-F8 | Other ward monitoring in India: Manipal Hospitals with the Isansys Patient Status Engine (tablet health terminal with an early warning score); Midmark ib.digi connected bed with Dozee and EWS; Max Healthcare 24x7 ward monitoring … | [mynewsdesk.com](https://www.mynewsdesk.com/uk/isansys-lifecare-ltd/news/indias-manipal-hospitals-partners-with-isansys-lifecare-to-launch-remote-patient-monitoring-technology-455613), [2](https://midmark.in/ib-digi), [3](https://medicaldialogues.in/max-healthcare-introduces-24x7-ward-monitoring-system-for-improved-patient-safety) | SNIPPET | not re-checked |
| D5-01-F9 | YOLO Health ATMs: walk-up kiosks measuring BP, glucose, ECG, haemoglobin, lipids, BMI ("48 tests", report in about 5 minutes); Lucknow railway station checks at Rs 50 and Rs 100; June 2023 plan for 500 Health ATMs in five states.… | [outlooktraveller.com](https://www.outlooktraveller.com/travelnews/lucknow-railway-station-gets-health-atms), [2](https://yourstory.com/2016/10/yolo-health) | SNIPPET | not re-checked |
| D5-01-F10 | Biofourmis: laid off 120 staff worldwide (48 in the US) about a year after a $300M Series D at a $1.3B valuation; CEO Kuldeep Singh Rajput stepped down about a month later (2023 by context; exact date not on the summary). / / SNI… | [mobihealthnews.com](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally), [2](https://www.mobihealthnews.com/news/biofourmis-ceo-steps-down-month-after-global-layoffs) | SNIPPET | not re-checked |
| D5-01-F11 | Cadence kit: health-system pages say patients get a blood glucose meter (diabetes), a BP cuff (high BP), or a BP cuff and a weight scale (heart failure); cellular devices send readings automatically; a 24/7 care team manages medi… | [ynhhs.org](https://www.ynhhs.org/patient-care/digital-health/connected-care), [2](https://www.heart.org/en/professional/aha-connected-care-powered-by-cadence/patients) | SNIPPET | not re-checked |
| D5-01-F12 | ASLI-JLL report (30 Aug 2025): India's organised senior-living stock is 22,157 units (7,147 in 2014); nearly 15,000 senior homes expected by 2030. Units, not care beds. / / OPENED | [therealtytoday.com](https://therealtytoday.com/news/market-insights/indias-senior-living-market-to-reach-15000-homes-by-2030-with-26000-crore-investment-asli-jll-india-report/) | OPENED | not re-checked |
| D5-01-F13 | Assisted living: about 2,100 beds today against about 11,000 needed by 2030 (ASLI-JLL, per a search summary; not on the page opened for F12). Antara Senior Care (Max Group): seven care homes, 500 beds. / / SNIPPET | [bsppd.business-standard.com](https://bsppd.business-standard.com/amp/india-news/senior-living-rents-touch-1-lakh-retirement-homes-valued-at-8-4-billion-125071600004_1.html) | SNIPPET | not re-checked |
| D5-01-F14 | Sjoding et al., "Racial Bias in Pulse Oximetry Measurement", NEJM 2020;383:2477-2478 (PMID 33326721): among patients reading 92-96% on a pulse oximeter, arterial saturation below 88% was found in 11.7% of Black and 3.6% of White … | [psnet.ahrq.gov](https://psnet.ahrq.gov/issue/racial-bias-pulse-oximetry-measurement) | SNIPPET | not re-checked |
| D5-01-F15 | Skin tone and pulse oximetry, other evidence: a large ICU study found no significant occult-hypoxemia difference for Asian vs White patients after adjustment (race self-identified); another study concludes self-reported race is n… | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39196478/) | SNIPPET | not re-checked |
| D5-01-F16 | FDA draft guidance, 7 Jan 2025, "Pulse Oximeters for Medical Purposes - Non-Clinical and Clinical Performance Testing, Labeling, and Premarket Submission Recommendations": testing across skin tones (Monk scale, ITA), label warnin… | [govinfo.gov](https://www.govinfo.gov/content/pkg/FR-2025-01-07/html/2024-31540.htm) | SNIPPET | not re-checked |
| D5-01-F17 | CDSCO classes, consultant sources that disagree: pulse oximeter listed Class C in the anaesthesiology list; other sources say fingertip oximeters are Class B (state licence, MD-5) and spot-check OTC types Class A; ICU multiparame… | [medicaldialogues.in](https://medicaldialogues.in/news/industry/pharma/dcgi-classifies-112-medical-devices-related-to-anesthesiology-80009), [2](https://corpseed.com/knowledge-centre/classification-of-medical-devices-by-cdsco-in-india) | SNIPPET | not re-checked |
| D5-01-F18 | AB-PMJAY does not cover outpatient consultations; no remote-monitoring package found. In Haryana, 650 of 1,300 empanelled private hospitals suspended PMJAY services in Aug 2025 over unpaid dues. / / SNIPPET | [moneylife.in](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html) | SNIPPET | not re-checked |
| D5-01-F19 | Decentralised trials in India: no dedicated CDSCO DCT guidance found; NDCT Rules amended (effective Apr 2025) to register CROs; ISCR position paper asks for DCT guidance. / / SNIPPET | [iscr.org](https://iscr.org/files/Article/1317861265_ISCR-DCT-Position-Paper-[Fina.pdf), [2](https://www.ibanet.org/india-clinical-trials-landscape) | SNIPPET | not re-checked |
| D5-01-F20 | Staffing norms, secondary summaries only: Staff Inspection Unit norms (1991-92) give ward staff nurses 1:3 (1:9 per shift) plus 30% leave reserve; another summary gives 1:5 by day and 1:10 at night. An Indian emergency-department… | [thieme-connect.com](https://thieme-connect.com/products/ejournals/abstract/10.1055/s-0043-1761938), [2](https://www.scribd.com/presentation/717697212/Staffing-NORMS) | SNIPPET | not re-checked |
| D5-01-F21 | Omron HEM-7156T upper-arm BP monitor: Flipkart special price Rs 2,593 (list Rs 4,990); Smartprix Rs 2,892. Bluetooth on the T model not confirmed. / / SNIPPET | [smartprix.com](https://www.smartprix.com/monitors/omron-hem-7156t-digital-bp-monitor-ppd1lm03clem), [2](https://www.flipkart.com/omron-hem-7156t-bp-monitor/p/itm05cef77f987c5) | SNIPPET | not re-checked |
| D5-01-F22 | Hobby modules (not for patients): MAX30102 pulse-oximeter module Rs 99-199; AD8232 ECG module Rs 649 (sold out); MLX90614 IR temperature sensor Rs 799. / / SNIPPET | [probots.co.in](https://probots.co.in/max30102-pulse-oximeter-heart-rate-sensor-module-gy-max30102.html), [2](https://majestronicz.in/collections/health-sensor), [3](https://probots.co.in/mlx90614-infrared-temperature-sensor.html) | SNIPPET | not re-checked |
| D5-01-F23 | NEWS2 (Royal College of Physicians, 2017): six readings (respiration rate, oxygen saturation, systolic BP, pulse, consciousness or new confusion, temperature), each scored 0-3, plus 2 points for supplemental oxygen; total 0-20; m… | [rcp.ac.uk](https://www.rcp.ac.uk/media/ctulqqbn/news2-executive-summary_0.pdf) | SNIPPET | not re-checked |
| D5-01-F24 | Spot-check monitors with early warning scores already sold in India: Welch Allyn Connex Spot Monitor with automated MEWS/NEWS, reseller list price Rs 1,14,999; Draeger Vista 120 SC with an embedded EWS; Philips IntelliVue MP5SC w… | [aajjo.com](https://www.aajjo.com/product/welch-allyn-connex-spot-monitor-in-delhi-medisure-inc), [2](https://www.draeger.com/en_sea/Products/Vista-120-SC), [3](https://medikabazaar.com/medicalequipments/patient-monitor) | SNIPPET | not re-checked |

## How this note was made

The note reuses facts from the adaptive-care research (notes D1-04, D1-05, D2-02, D2-04, D2-06 and D4-05). It adds 24 new facts from web checks on 16 Nov 2026, recorded in `research_notes\dtx\D5-01 Vitals station web checks.md`. Three pages were opened in full: the KGMU study, the Kenyan audit and the ASLI-JLL report. The other new facts come from search summaries (SNIPPET in the register). No separate claims check was run on D5-01.
