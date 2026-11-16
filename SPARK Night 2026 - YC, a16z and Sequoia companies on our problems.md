# SPARK Night 2026: which YC, a16z and Sequoia companies are solving our problems, and how

*16 November 2026. Covers YC's 10 latest batches (Winter 2025 to Summer 2027), a16z and Sequoia deals since January 2025, and older portfolio companies that still matter. Peak XV (formerly Sequoia India) is included because it is the Sequoia family's India arm. Every traction number is the company's own claim unless stated. The detailed notes with fact IDs and sources are D7-01, D7-02 and D7-03 in `research_notes/dtx/`.*

## The answer

1. **Nobody does remote dosing for the high-stakes drugs.** No company in YC's 10 latest batches (1,484 companies), and none backed by a16z, Sequoia or Peak XV, runs remote dose management for warfarin/INR, hydroxyurea, epilepsy drugs, transplant drugs or oral chemo. The lead pick (warfarin in rheumatic heart disease) is open ground. The near misses:
   - Athelas Home (YC and Sequoia) is a finger-stick safety test with no dose rule.
   - Biofourmis BiovitalsHF (Sequoia India) recommended heart-failure dose increases for a clinician to sign. Its randomised trial was positive (AIM-POWER, Feb 2026), but it was never cleared and the company has merged into another (see D7-04).
   - Virta (Sequoia) cuts insulin inside a diet programme.
2. **Adaptive chronic care (problem A) gets the most money.** The pattern that wins funding is "AI drafts, clinician signs":
   - Virta: home glucose, weight and BP readings; a remote doctor changes the drugs.
   - Counsel Health (a16z): AI does the first contact; Oura agreed to buy it on 10 Nov 2026.
   - Prana and Clara (YC 2026): AI doctors that act on the patient's data.
   - None of them publishes its dose rules. That is the gap a protocol engine fills.
3. **Hospital and ICU money goes to software that assumes a digital patient record:**
   - Bayesian Health (a16z): FDA-cleared continuous sepsis alerts, May 2026.
   - HealthLeap (Sequoia): a nightly screen of every inpatient, Oct 2026.
   - Telepatia (a16z): AI clinicians for under-staffed Latin American hospitals, Jun 2026.
   - Abridge and Ambience (a16z): voice-to-chart tools for nurses.
   - The only tele-ICU in any of these portfolios is Cloudphysician (Peak XV, India), and its last round was June 2024.
4. **Nobody funds cheap vitals hardware now (problem C).** YC backed an Indian health kiosk in 2019, Pulse Active Stations, which says it has done 600,000 check-ups but stalled at screening. Dozee is not backed by any of these funds. The recent "home monitoring" money goes to people with a phone, not to sensors: Sprinter Health (a16z) sends trained field workers, and Abby Care (Sequoia) pays family caregivers.
5. **YC's recent health batches are mostly biotech and paperwork.** Of 114 Healthcare-tagged companies:
   - 35 drug discovery, biotech and trials
   - 28 front-office and care-operations AI agents
   - 18 billing, claims and prior authorisation
   - 13 consumer AI doctors and coaches
   - 11 imaging and devices
   - none on ICU care or high-stakes dosing
   - none based in India
6. **Outside Peak XV, none of these companies works in India.** Peak XV's Cloudphysician, Twin Health and Qure.ai do. Telepatia says India comes "later", with no date.
7. **The best comparables to cite in a pitch:**
   - Telepatia: a hospital AI that sells because of staff shortages in a middle-income market, measured by "protocol adherence 84% to 99%".
   - Athelas Home plus a dose rule: this is the warfarin loop.
   - HealthLeap's "morning risk list": it fits a district hospital with one doctor for 60 beds.
   - Virta's "cut the dose fast to avoid hypos": the safest titration direction to demo.

## The four problems (from the adaptive care challenge)

| | Problem | Example |
|---|---|---|
| **A** | Adaptive chronic care between visits: device or lab data changes the treatment, not just reminders | BP, diabetes, heart failure, GLP-1 |
| **B** | High-stakes dosing where specialists are rare | Warfarin/INR (lead pick), hydroxyurea, epilepsy |
| **C** | Low-cost vitals and remote monitoring | Shared vitals station, wearables |
| **D** | Smart ICU and hospital deterioration | Tele-ICU, sepsis alerts, protocol loops |

## The map

| | YC (latest batches unless marked) | a16z | Sequoia | Peak XV (ex-Sequoia India) |
|---|---|---|---|---|
| **A. Adaptive chronic care** | Prana, Clara, Juno, RonanRx, Amby, Nori, Illume; older: Nourish, Kivo, MedMe, Veera (India), Akido | Counsel Health, Omada, Hippocratic AI, Knownwell, Function Health, Devoted | **Virta Health**, Abby Care | Twin Health (runs in Chennai) |
| **B. High-stakes dosing** | **None.** Older: DoseDr (insulin, inactive) | **None.** Nearby: Thyme Care (cancer symptoms), Milu (medicine reviews), OpenEvidence | **None.** Nearby: Athelas Home (blood-count test), OpenEvidence | Nearby: Biofourmis BiovitalsHF (heart-failure titration, merged away) |
| **C. Vitals and monitoring** | Kaigo Health; older: **Pulse Active Stations (India)**, Bodyport, Vena Vitals, Spire, Starling | Sprinter Health (people, not sensors) | Athelas RPM, Abby Care | Biofourmis, Us2.ai (echo reports) |
| **D. Smart ICU and hospital** | **None.** Nearby: YouShift, CareSwift, Lumius, Archangel; older: Bunkerhill, Sepsis Scout | **Bayesian Health**, **Telepatia**, Abridge, Ambience, Hippocratic Nurse Co-Pilot | **HealthLeap**, Bunkerhill, AirStrip; adjacent: Freed, Avelios, Clipboard | **Cloudphysician** (India tele-ICU), Qure.ai |

Bold marks the companies closest to our build.

## A. Adaptive chronic care between visits: who and how

| Company | Backer and round | What the solution does | Who decides | What we take from it |
|---|---|---|---|---|
| **Virta Health** | Sequoia Capital Global Equities led the $65M Series D, Dec 2020 | Patients send daily weight, finger-stick glucose and ketones, and BP from home. A remote doctor or nurse practitioner changes medicines from those readings, cutting insulin and sulfonylureas fast. In its trial, 94% cut or stopped insulin (not randomised, funded by Virta). Virta puts 100% of its fees at risk with payers. Maine's state employee plan routes GLP-1 prescriptions through Virta from Jul 2026. | Clinician signs every change | The clearest funded "device reading, then dose change" loop. In India, drop the ketone strips and use glucose plus weight; the prescriber is a medical officer working to a written protocol. |
| **Counsel Health** | a16z led the seed and co-led the $25M Series A, Oct 2025; Oura agreed to buy it on 10 Nov 2026 (the $625M price is press-reported) | AI handles the first contact, check-ins and refill prompts, and decides when to bring in a doctor. Doctors diagnose, prescribe and order labs. Hypertension, cholesterol and obesity are being added in 2026. | Physician | "AI does the first touch, the doctor signs off" sells. In India, escalate to a nurse or medical officer, with the specialist kept for rule breaks. |
| **Omada** | a16z led the Series B in 2014; listed on Nasdaq since Jun 2025 | Connected glucometers, BP cuffs and scales feed coaches and care teams. AI summarises the data and suggests next actions for the care team to review. GLP-1 prescribing is starting. 1,025,000 members in Q1 2026. | Care team | A safe first step towards titration: the AI suggests, a human approves. |
| **Hippocratic AI** | a16z co-led the $50M seed in 2023 and joined the later rounds | Voice agents phone patients between visits (chronic care, after discharge, medicine adherence). An "orchestrator" decides which call goes to which patient after which signal. It says its agents do not diagnose or prescribe. Claim: 250M interactions. | Escalates to nurses | Use the orchestrator pattern on cheap local-language calls to feature phones. |
| **Prana** | YC Winter 2026, about $500K | An "always-on AI doctor" that reads records and wearables for "clinical drift" between visits, explains labs and manages prescriptions. $39 flat visit. | Human doctors approve | The same "drift between visits" framing as the challenge, but generalist and cash-pay. |
| **Clara** | YC Spring 2026 | AI primary care that sees the patient's data, handles refills, and orders and explains labs. Built by the Circle Medical founders. | A human provider approves every recommendation | Investors fund this as a full medical practice, not as an app. |
| **Juno** | YC Spring 2026 (London) | A chronic-illness companion: tracks symptoms, finds patterns, prepares reports for the doctor. Claims of 90,000 to 300,000 users, depending on the source. | No treatment change | Shows a chronic-illness app can grow fast, but it stays at monitoring. |
| **RonanRx** | YC Summer 2026 | Its own pharmacy plus telehealth doctors; sets a personalised GLP-1 and peptide dose for each patient. | Doctor | The only latest-batch YC company whose product is the dose; depends on US pharmacy rules. |
| **Twin Health** | Peak XV in the Series D (Dec 2023); a $59M 2026 raise with undisclosed lead | Builds a "digital twin" from CGM, watch and lab data, with a clinical team. Payers pay only when members hit A1C, weight or medicine-reduction milestones. Runs in Chennai. | Clinical team (dose rule not published) | Pay-on-outcome pricing is the pitch for an insurer or state scheme. CGMs are too expensive for rural patients. |
| **Knownwell, Function Health, Devoted Health** | a16z | Obesity clinics with GLP-1 prescribing; twice-yearly 100+ lab panels with an AI layer; a US Medicare insurer running a hypertension clinic | Clinicians | Inputs and payers, not a titration engine. |
| **Abby Care** | Sequoia in the $82M Series C, Oct 2026 | Trains and pays family members as home caregivers; a nurse watches their readings and steps in before an emergency visit. | RN | Close to an "ASHA plus family" loop. |
| **Akido Labs** (older YC, W15) | Oak HC/FT led the $60M Series B, May 2025 | ScopeAI: medical assistants see patients, AI proposes the plan, doctors approve; built for underserved settings. | Doctor | The nearest US precedent for "non-specialist plus AI, doctor signs". |

## B. High-stakes dosing: nobody owns it

| Company | Backer | What it does | Why it is not the answer |
|---|---|---|---|
| **Athelas Home** (Commure) | YC Summer 2016; Sequoia since 2016; Commure raised $70M at $7B, May 2026 | A finger-stick AI blood analyser gives white cells and neutrophils (ANC) in minutes for patients on clozapine, chemotherapy or immunosuppressants. FDA-cleared for point-of-care use on 12 Feb 2026. Claims 40,000 patients and 1M tests. | It supplies the safety lab value, but the prescriber still decides with no rule. **For warfarin, the same design is a point-of-care INR meter plus the dose rule Athelas lacks.** |
| **Biofourmis BiovitalsHF** | Sequoia India led the $35M Series B, 2019 | Wearables, symptoms and labs produce recommendations to start or raise heart-failure drugs, which the clinician signs. FDA Breakthrough designation in 2021. | Its randomised trial, AIM-POWER (122 patients, 21 US sites, Circ Heart Fail Feb 2026), raised the optimal-therapy score 1.72 versus 0.44 (P < 0.001). It was still never cleared, and Biofourmis merged into CopilotIQ in 2024 without Peak XV in the new money. **The closest funded precedent for "device data, recommended dose step, clinician signs", and the best one to copy (D7-04).** |
| **Thyme Care** | a16z led in 2021 and joined the $125M+ Series E, Sep 2026 | Cancer patients report symptoms and nurses review them in real time. Claims 28% fewer emergency visits or admissions among those who completed the programme. | Manages side effects, not doses. Its weekly red-flag check-in is a reusable skeleton. |
| **OpenEvidence** | Sequoia led the $75M Series A, Feb 2025; a16z co-led $250M at $15B, Sep 2026 | Doctors ask questions and get answers that cite journals. Free, paid for by ads. An Anthropic partnership targets about 100 low- and middle-income countries; India is not named. | It answers questions; it never sees patient data or sets a dose. |
| **DoseDr** | YC Winter 2016, now inactive | A consumer app that helped people with diabetes adjust insulin between visits, with a doctor on call. | A dead precedent. Sell to hospitals and programmes, not to consumers. |

Research-only warfarin AI does exist: CURATE.AI, a retrospective study of 127 patients, and a GPT-4 modelling study that came within ±1 mg/week of the physicians' dose in 74% of 180 cases (D7-02-F50). Neither is a company.

## C. Low-cost vitals and remote monitoring

| Company | Backer | What it does | What we take from it |
|---|---|---|---|
| **Pulse Active Stations Network** (Hyderabad) | YC Winter 2019, about $150K | IoT "Smart Health Machines" at metro stations and public places screen for obesity, hypertension and similar risks (21 parameters). Claims 600,000+ check-ups. The founder calls the results "just a health indicator". No news since 2023. | **This is our shared vitals station, already built.** It stalled because a reading never turned into care. Ours must tie each reading to a named patient's protocol. |
| **Kaigo Health** | YC Fall 2025, $500K | AI phone calls after discharge, combining patient answers, voice biomarkers and RPM data; paid from Medicare monthly fees. One Sep 2026 profile says it has since moved to nursing-home billing (unverified). | Phone calls suit older and rural patients; India has no RPM fee, so the payer must be a hospital or a state. |
| **Sprinter Health** | a16z in the $55M Series B, May 2025 | Field workers trained as medical assistant, community health worker and phlebotomist visit homes with a checklist and join a virtual nurse practitioner. AI routes up to 12 visits a day. | The ASHA-plus-teleconsult model, funded. Add a shared kit (BP, SpO2, glucose, weight, INR strip). |
| **Athelas RPM** | Sequoia | A SIM-connected BP cuff and scale; a nurse team reviews readings and bills US RPM codes. | No dose changes found. |
| **Bodyport, Vena Vitals, Spire, Starling** | Older YC | A heart-failure scale that reads congestion so teams can "remotely optimize therapy"; a continuous BP sticker; respiratory sensing (acquired); a toilet urine sensor | Sensor proof points; none is cheap enough for rural India. |
| **Us2.ai** | Sequoia India co-led the seed; existing investor in the $15M Series A | Turns any echo scan into a full measured report in under 2 minutes; FDA-cleared. | Upstream of the warfarin loop: confirming rheumatic heart disease and setting the INR target. |

## D. Smart ICU and hospital deterioration

| Company | Backer and round | What the solution does | What we take from it |
|---|---|---|---|
| **Cloudphysician** (Bengaluru) | Peak XV led the $10.5M Series A, Jun 2024; no later round found | Remote intensivists plus the RADAR platform: NETRA camera vision, AIRA notes, HERA paper digitising, SWARA voice. Claims 280 hospitals and 1.3 lakh patients. | The Indian incumbent. Build where it is thin: automating protocol steps, ward-to-home handover, and dosing loops (see D6-02). |
| **Bayesian Health** | a16z led, 2021 | Screens every inpatient's record continuously for sepsis, "before clinical suspicion", with alerts inside the EHR. The first FDA-cleared continuous AI sepsis monitor (May 2026). In its study, death rates fell only when a clinician confirmed the alert within 3 hours. | Screen everyone, then confirm and act within 3 hours. Without an EHR, the input must be nurse-entered early-warning scores or a camera reading the monitor. |
| **Telepatia** (Colombia) | a16z led the $33M Series A, 17 Jun 2026 | AI documentation, interaction checks and decision support trained on each hospital's own protocols; "AI doctors, nurses, auditors". Claims 25+ hospital systems, 14M patients, protocol adherence up from 84% to 99%. India is planned "later". | **The best pitch comparable:** a shortage-driven, protocol-trained hospital AI selling in a middle-income market. |
| **HealthLeap** | Sequoia co-led the $8M seed; $30M Series A led by Hummingbird, 7 Oct 2026 | Every night it reads each inpatient's full record (notes, nursing assessments, labs, vitals trends, orders). Each morning it gives clinicians and dietitians a ranked list of who to see first. It starts with malnutrition; heart failure, pressure ulcers and sepsis are next. | A morning risk list suits one doctor covering 60 beds better than real-time alarms. Indian hospitals are paid fixed PM-JAY package rates, so the pitch must be deaths and transfers avoided, not extra billing. |
| **Bunkerhill Health** | YC W19; Sequoia seed; $25M Series B led by Khosla, Jul 2026 | Each hospital names a problem and Bunkerhill builds a background agent that catches missed cases. 15 health systems; 9 FDA-cleared algorithms. | Pick three rules for a district hospital, such as a missed repeat INR, an abnormal potassium nobody acted on, or a discharge with no follow-up date. |
| **Abridge** | a16z led the $300M Series E, Jun 2025 | The nurse speaks at the bedside and the AI drafts chart entries for the nurse to confirm. At rural Reid Health, charting fell 30-45 min per shift and nurse vacancies fell from 18% to 8% (the hospital's own association, not a measured effect). | Voice-to-chart is how a paper ward gets the timed vitals that an early-warning score needs. |
| **Ambience** | a16z co-led the $243M Series C, Jul 2025 | Nursing suite: a pre-shift summary, chart Q&A, and spoken assessments turned into chart entries the nurse confirms. | A handover sheet of who is getting worse. |
| **Hippocratic AI Nurse Co-Pilot** | a16z | The ward nurse launches AI phone calls from the record for admission, discharge and medicine education; red flags go back to the nurse. Claims 3+ hours saved per nurse a day. | Discharge education by phone, in the local language. |
| **AirStrip** | Sequoia (backing seen in search summaries only) | Remote viewing of bedside monitor waveforms and alarms on phones; FDA-cleared alarm management. | A direct data feed beats a camera when monitors can export; most district monitors cannot. |
| **Qure.ai** (Mumbai) | Sequoia India led the $16M round, 2020 | AI reads of chest X-rays and head CTs, stroke triage for hub-and-spoke networks, and qTrack follow-up lists. | Its qTrack follow-up list is the pattern for INR recalls. |
| **YC latest batches** | None on ICU care | Nearby: YouShift (hospital shift scheduling), CareSwift (ambulance report AI), Lumius (low-cost 3D ultrasound for central lines), Archangel Health (test environments for medical AI) | Archangel-style testing could check a protocol engine before a pilot. |

## Checked: not backed by YC, a16z or Sequoia

- **Cadence:** Spark Capital led its $100M Series C. (The YC "Cadence" is a different, inactive company.)
- **Story Health:** heart-failure titration; backed by Northpond and B Capital.
- **Dozee:** contactless bed sensor; backed by Prime, 3one4 and others.
- **Tricog:** ECG reads for remote clinics; backed by UTEC, Blume and others.
- **Ambience and Abridge:** a16z, not Sequoia.
- **Also not Sequoia:** Nabla, Tennr, Assort, Viz.ai, Eko Health, Hims & Hers.
- **Not Peak XV:** Even Healthcare and HealthifyMe (both Khosla), Doctronic (Lightspeed), Cityblock (a16z backing not confirmed).

## What this means for the build

1. **The dose rule is the moat.** Virta, Counsel, Prana, Clara, Twin and Athelas keep a clinician deciding with no published rule. BiovitalsHF used guideline-based rules and had randomised proof, but never reached clearance. Outside these funds, rule-based insulin software is FDA-cleared, and Hygieia d-Nav has a randomised trial (D7-04). What nobody has shipped is a protocol-bound dose loop for warfarin or hydroxyurea that a nurse or medical officer can sign, built for a district hospital. The home-INR trials (D5-01-F05) show it is the part that saves lives. Deaths fell when patients set the dose from a fixed schedule (RR 0.55), but not when they tested at home and phoned the clinic (RR 0.94).
2. **Copy the loop, not the hardware.** The shape of Athelas Home is right: a finger-stick test at the point of care and a result on the same day. Add the dose step and send it by SMS or WhatsApp to a named medical officer.
3. **Hospital AI sells on shortage plus protocol adherence.** Telepatia's 84%-to-99% adherence claim and HealthLeap's morning list are the two framings to borrow for the smart-ICU idea. Cloudphysician already covers the tele-ICU layer.
4. **The vitals station needs a "so what".** Pulse Active Stations shows that screening alone stalls. Every reading must land on a named patient's protocol.
5. **Expect investor questions to be about who pays.** US companies here are paid through Medicare RPM fees, fees at risk, DRG recovery and employers. Our answer has to be a state NCD programme, PM-JAY, a hospital's own budget, or a per-patient fee.

## Method and limits

- **YC:** the yc-oss mirror of the YC directory (updated 15 Nov 2026), filtered by Healthcare tag and clinical keywords, then read company by company; all years searched for the four problems. Category counts are ours and hand-checked. YC descriptions are the companies' own words.
- **a16z and Sequoia/Peak XV:** two research passes (about 45 and 100 searches and fetches). Each backer was confirmed from the fund's page, a company release or named-investor press. Facts are tagged OPENED or SNIPPET in D7-02 and D7-03.
- **Spot-checked by hand on the original pages:** Oura's acquisition of Counsel, the a16z Telepatia post, and HealthLeap's round.
- **Not covered:** HongShan (ex-Sequoia China), Sequoia Israel, Peak XV's South-East Asia health companies, Virta's dosing-protocol supplement, and Athelas Home's price.
- **Unsettled numbers:** Juno's user count; Kaigo's possible pivot; the Counsel price; Bayesian's Medicare add-on payment.

**Detailed notes:** `research_notes/dtx/D7-01 YC latest batches - companies and solutions.md`, `D7-02 a16z - companies and solutions.md`, `D7-03 Sequoia and Peak XV - companies and solutions.md`.
