# D7-01 YC latest batches: who is solving the adaptive-care problems (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: the user asked which companies in the latest Y Combinator batches are solving the project's problems, and what their solutions are. The problems are the four threads from the adaptive care challenge:

- **A. Adaptive chronic care between visits**: read home device or biomarker data and change the treatment, not just monitor or remind.
- **B. High-stakes dosing where specialists are rare**: warfarin/INR (the lead pick), sickle-cell hydroxyurea, epilepsy, insulin and similar.
- **C. Low-cost vitals and remote monitoring**: the shared vitals station, wearables, early warning at home.
- **D. Smart ICU and hospital deterioration**: tele-ICU, early-warning alerts, protocol loops, camera reading of monitors.

Method. I downloaded the yc-oss mirror of the YC directory (OPENED, secondary copy, mirror `last_updated` 2026-11-15, fetched 2026-11-16). It covers the 10 latest batches: Winter 2025, Spring 2025, Summer 2025, Fall 2025, Winter 2026, Spring 2026, Summer 2026, Fall 2026, Winter 2027 (13 companies listed so far) and Summer 2027 (1). That is 1,484 companies. I filtered on the Healthcare industry tag (114 companies) and also keyword-searched every company description for clinical terms (ICU, sepsis, vitals, wearable, titration, dose, insulin, warfarin, INR, hypertension, heart failure, CKD, sickle, epilepsy, India, rural and others). I then searched the whole directory (6,397 companies, all years) for the same four problems to find older YC companies that hit them directly. Descriptions are the companies' own YC text, so every traction figure is a company claim. A few were checked on the web (marked).

Fact IDs are D7-01-Fxx. OPENED = page or data read; SNIPPET = search summary only.

## Digest

1. **Nobody in the 10 latest YC batches works on problem B or D.** No company in Winter 2025 to Summer 2027 describes warfarin, INR, anticoagulation, hydroxyurea, epilepsy dosing, tele-ICU, sepsis alerts or hospital deterioration monitoring. (D7-01-F01)
2. **Where YC's health money goes.** Of the 114 Healthcare-tagged companies: 35 drug discovery, biotech, pharma and trial ops; 28 front-office and care-ops AI agents; 18 billing, claims, prior auth and insurance; 13 consumer AI doctors, coaches and longevity tests; 11 imaging, diagnostics and devices; 4 AI-native telehealth clinics; 3 AI infra and evals; 2 other. OUR COUNT, hand-checked categories. (D7-01-F02)
3. **The closest to problem A is a new wave of "AI doctors" that act, not just chat.** Prana (W26) watches records and wearables for "clinical drift" and manages prescriptions; Clara (Spring 2026) orders labs and handles refills. In both, a human clinician approves each medical recommendation. Neither runs a disease-specific dose protocol. (D7-01-F03, F04)
4. **Juno (Spring 2026) is the biggest chronic-illness app in the set**, but it tracks and summarises rather than changes treatment. User numbers conflict: 300,000+ (YC mirror), 90,000+ (YC page per search), 125,000 downloads (Product Hunt). (D7-01-F05)
5. **RonanRx (Summer 2026) is the only latest-batch company that personalises the dose itself**, for GLP-1s and peptides, through its own pharmacy and telehealth doctors. (D7-01-F06)
6. **Kaigo Health (Fall 2025) is the only latest-batch company doing remote monitoring**: AI phone calls plus voice biomarkers and RPM data for Medicare patients after discharge. One September 2026 profile says it has since moved to nursing-home revenue recovery. UNVERIFIED. (D7-01-F07)
7. **YC already funded an Indian shared vitals station, in 2019.** Pulse Active Stations Network (W19, Hyderabad) runs IoT "Smart Health Machines" for NCD screening and says it has done 600,000+ check-ups. The founder called the results "just a health indicator". No 2025 or 2026 news was found. This is the closest comparable to the user's vitals-station idea. (D7-01-F08)
8. **Older YC hardware that fits problem C:** Bodyport (S15) is a heart-failure weighing scale that reads congestion and cardiac output so teams can "remotely optimize their therapy". Vena Vitals (S20) is a continuous BP sticker. Spire Health (W15) was acquired. (D7-01-F09, F10)
9. **A YC dosing company that died:** DoseDr (W16) helped people with diabetes adjust insulin between visits, with a doctor on call. It is now Inactive. It shows that between-visit dose changes have been tried before and failed as a consumer app. (D7-01-F11)
10. **Sepsis Scout (W18)**, a wearable plus AI to predict sepsis outside hospital, was acquired by Cytovale. It is the only YC company in any year described as doing sepsis early warning. (D7-01-F12)
11. **The YC hospital-adjacent tools in recent batches are thin on clinical loops:** YouShift (W25, hospital shift scheduling), CareSwift (S25, AI for ambulance reports), Lumius (Spring 2026, low-cost 3D ultrasound for central lines) and Archangel Health (F26, evals and RL environments for medical AI). (D7-01-F13 to F16)

Surprises: (a) the "AI doctor" wave is US cash-pay and generalist; nobody at YC is building a disease-specific, protocol-bound dosing loop. (b) The gap in B and D is total across 1,484 companies. Read that as open space, or as a sign that hospital sales and regulation keep YC-style teams out. (c) The one Indian vitals-kiosk company YC funded looks stalled at screening and never closed the loop to treatment.

## Companies, by problem

### Problem A: adaptive chronic care between visits

#### Prana (YC Winter 2026): an always-on AI doctor that watches for "clinical drift"
- **Solution:** Prana connects to the patient's medical records and wearables and watches for "clinical drift", meaning slow declines between visits. Its AI explains labs and "manages your prescriptions". It automates about 90% of the "grunt work" (history taking, logistics, triage), and human doctors make the high-leverage decisions. Pricing seen: $39 flat telehealth visit; it syncs with Oura, Fitbit and Garmin (SNIPPET). Early beta. (D7-01-F03) YC page: https://www.ycombinator.com/companies/prana-health (OPENED via mirror); launch: https://www.ycombinator.com/launches/PPg-prana-an-ai-doctor-that-monitors-you-24-7 (SNIPPET). About $500K raised per aggregators (SNIPPET).
- **What it changes:** prescriptions, with a doctor approving. Generalist, not disease-specific.
- **India take:** the "drift between visits" framing is the same as the challenge's. What India needs differently: a fixed protocol per disease that a non-specialist can sign off, instead of a cash-pay generalist doctor.

#### Clara (YC Spring 2026): an AI primary care and longevity practice
- **Solution:** a chat AI that can see the patient's medical data and act. It makes sense of symptoms, handles medication refills, and orders and explains labs. "Medical recommendations are preliminary until one of our human medical providers in the loop reviews and approves them." Built by the team that grew Circle Medical to $100M revenue (company claim). (D7-01-F04) https://www.ycombinator.com/companies/clara-2 (OPENED via mirror)
- **India take:** the "AI drafts, clinician approves" pattern is what the user's loop already uses. Clara shows investors fund it as a full medical practice, not as software.

#### Juno (YC Spring 2026, London): an AI companion for chronic illness
- **Solution:** remembers the patient's full history, tracks symptoms, spots patterns and prepares clearer reports for the doctor. Positioned as a companion, not a doctor (SNIPPET). No treatment change. (D7-01-F05) https://www.ycombinator.com/companies/juno-chat (OPENED via mirror). Users: mirror says 300,000+; the YC page per search says 90,000+ and $70K MRR; Product Hunt says 125,000 downloads (all company claims, SNIPPET, dates differ).
- **India take:** proof that a chronic-illness app can grow fast on the consumer side, but it stops at depth 1 to 2 (monitoring and summaries).

#### RonanRx (YC Summer 2026): a pharmacy that personalises the dose
- **Solution:** a full-stack pharmacy for personalised peptides and GLP-1s. The patient completes an intake and sees a licensed telehealth doctor; RonanRx makes the drug and sets "different dose" per patient. It says it was licensed in 33 states within 10 weeks and grew 50% week on week (company claims). (D7-01-F06) https://www.ycombinator.com/companies/ronanrx-inc (OPENED via mirror)
- **India take:** the only latest-batch company whose product is the dose itself. The model depends on US compounding-pharmacy rules and does not transfer to India.

#### Smaller consumer coaches (lifestyle, not drugs)
- **Amby Health (W25):** "Your wearable tells you what happened. Amby texts you what to do next, checks in, and adjusts when life gets in the way." https://www.ycombinator.com/companies/amby-health
- **Nori (F25):** turns Apple Health, records and wearables into a daily plan. https://www.ycombinator.com/companies/nori
- **Illume Labs (S26):** wearables, blood panels and genomics turned into daily text insights. https://www.ycombinator.com/companies/illume-labs
- **Galen AI (Spring 2025):** records from 800+ institutions plus 20+ wearables including Dexcom. Acquired by Oura (Apr 2026, per D2-06-F34). https://www.ycombinator.com/companies/galen-ai
- **Lucis (Spring 2025, Paris) and Helios Intelligence (F26):** blood biomarker testing turned into insights; Helios claims 1,000+ biomarkers from a drop of blood (company claims). https://www.ycombinator.com/companies/lucis , https://www.ycombinator.com/companies/helios-intelligence
- All OPENED via mirror. India take: depth 1 to 2, lifestyle advice only, no dose change.

#### Older YC companies on problem A that still matter
- **Nourish (W21):** telehealth dietitians covered by insurance; raised a $100M Series C in May 2026 (D2-06-F5). https://www.ycombinator.com/companies/nourish
- **Kivo Health (W23):** AI-powered virtual care for seniors with chronic disease, starting with lung care. It claims $8K+ saved per patient and works with Stanford, UCLA and Optum; $10M Series A (company claims). https://www.ycombinator.com/companies/kivo-health
- **MedMe Health (W21, Toronto):** software that lets pharmacists deliver paid clinical services, including prescribing and adapting medications, point-of-care testing and chronic-condition monitoring. https://www.ycombinator.com/companies/medme-health . India take: a pharmacist-led model is worth noting for places with no specialist.
- **Veera Health (W21, India):** PCOS treatment in India: therapy, coaching and specialist support on a subscription. https://www.ycombinator.com/companies/veera-health

### Problem B: high-stakes dosing where specialists are rare

- **Latest batches: none.** No Winter 2025 to Summer 2027 company works on anticoagulation, hydroxyurea, epilepsy, transplant drugs or insulin dosing. (D7-01-F01)
- **DoseDr (W16, Inactive):** a mobile app that helped people with diabetes adjust insulin doses between doctor visits, connecting them to a doctor "when an issue arises". (D7-01-F11) https://www.ycombinator.com/companies/dosedr . Lesson: a free consumer app for between-visit dose changes did not survive. The user's plan sells to hospitals and programmes, which is a different buyer.

### Problem C: low-cost vitals and remote monitoring

#### Pulse Active Stations Network (YC Winter 2019, Hyderabad): India's YC-backed health kiosk
- **Solution:** a network of connected, IoT-enabled "Make in India" Smart Health Machines at metro stations and public places. They screen for NCD risk factors such as obesity and hypertension; coverage mentions 21 parameters. The company says it has done 600,000+ check-ups (company claim). The founder said results are "just a health indicator" (SNIPPET). Legal name Quantificare Health Stations Pvt Ltd (SNIPPET). It planned 10,000 kiosks in 3 years around 2020 (SNIPPET); no 2025 or 2026 rollout news was found. About $150K raised per a third-party profile (SNIPPET). (D7-01-F08) https://www.ycombinator.com/companies/pulse-active-stations-network ; https://yourstory.com/2020/03/healthtech-startup-pulse-active-stations-health-analysis (SNIPPET)
- **India take:** this is the shared vitals station, built and funded six years ago. It stalled at screening. The user's version must close the loop: each reading goes to a named patient's protocol and changes care, or it is another kiosk.

#### Kaigo Health (YC Fall 2025): AI phone calls plus RPM for Medicare patients
- **Solution:** automated post-discharge follow-ups and check-ins by phone, which suits older patients. It combines patient answers, voice biomarkers and RPM device data, and is paid through Medicare's monthly chronic-care and RPM fees (SNIPPET). One profile claims up to 75% fewer hospitalisations (company claim, unverified). $500K pre-seed from YC (SNIPPET). A September 2026 profile says the site now pitches nursing-facility revenue recovery instead (UNVERIFIED). (D7-01-F07) https://www.ycombinator.com/companies/kaigo-health
- **India take:** a phone call as the interface is right for rural patients. Medicare RPM fees have no Indian equivalent, so the payer has to be a hospital, a state programme or PM-JAY.

#### Older YC devices
- **Bodyport (S15):** a weighing scale that measures cardiac output, congestion and heart rate. Its software lets care teams "remotely optimize their therapy" to prevent heart-failure admissions. (D7-01-F09) https://www.ycombinator.com/companies/bodyport
- **Vena Vitals (S20):** a small sticker that monitors BP continuously. It says the sticker matched the best operating-room tools at a fraction of the cost (company claim). (D7-01-F10) https://www.ycombinator.com/companies/vena-vitals
- **Spire Health (W15, acquired):** continuous respiratory sensing RPM; 150,000+ people have worn its sensors (company claim). https://www.ycombinator.com/companies/spire-health
- **Starling (W22):** a toilet-mounted urine mass-spectroscopy RPM device that earns RPM fees for clinics. https://www.ycombinator.com/companies/starling

### Problem D: smart ICU and hospital deterioration

- **Latest batches: no ICU, sepsis or deterioration company.** (D7-01-F01)
- **Nearby latest-batch tools:**
  - **YouShift (W25):** AI hospital shift scheduling, replacing full-time schedulers. Relevant to the staffing gap, not to care. (D7-01-F13) https://www.ycombinator.com/companies/youshift
  - **CareSwift (S25):** a real-time AI assistant inside ambulance reporting software that flags errors and cuts documentation time by 80% (company claim). (D7-01-F14) https://www.ycombinator.com/companies/careswift
  - **Lumius (Spring 2026):** compact, low-cost real-time 3D ultrasound, starting with central-line placement. It says about 50% of first attempts fail with 2D (company claim). (D7-01-F15) https://www.ycombinator.com/companies/lumius
  - **Archangel Health (F26):** RL environments inside de-identified EHRs, physician-verified data and hard-case benchmarks to post-train and test medical AI. (D7-01-F16) https://www.ycombinator.com/companies/archangel-health . India take: useful for testing an ICU protocol engine.
- **Older:**
  - **Sepsis Scout (W18, formerly Patchd Medical):** wearables plus AI to predict sepsis outside hospital; acquired by Cytovale. (D7-01-F12) https://www.ycombinator.com/companies/sepsis-scout
  - **Caire Health (S21):** AI that reads medical scans for critical-care teams. https://www.ycombinator.com/companies/caire-health

### Older YC companies that later raised from Sequoia or a16z circles (cross-check with D7-02, D7-03)
- **Athelas (YC S16), now part of Commure:** Sequoia has backed it since 2016. Athelas Home is a finger-stick blood-count test for patients on clozapine, chemotherapy and immunosuppressants; it got FDA point-of-care clearance on 12 Feb 2026 (D7-03-F13, F14). https://www.ycombinator.com/companies/athelas
- **Bunkerhill Health (YC W19):** background AI agents that hospitals choose; Sequoia and Khosla backed (D7-03-F29, F30). https://www.ycombinator.com/companies/bunkerhill-health
- **Akido Labs (YC W15):** ScopeAI, where medical assistants see patients, AI proposes the plan and doctors approve, in underserved settings. $60M Series B led by Oak HC/FT, May 2025 (D7-02-F46, SNIPPET). https://www.ycombinator.com/companies/akido-labs . This is the closest YC precedent for "non-specialist plus AI, doctor signs". (D7-01-F19)

## What YC says it wants (Requests for Startups)

From R4-04 (opened 2026-11-12): the Winter 2027 RFS has no chronic-care or ICU item. The closest are "The $15-an-Hour Expert" (AI lets uncredentialed workers do expert work, with healthcare billing as an example) and "AI for the Air-Gapped Economy" (offline AI for healthcare). Summer 2026 had "AI Personalized Medicine". The $15-an-hour expert idea maps well onto the user's thesis: a nurse or medical officer runs a specialist protocol with software. (D7-01-F17, from R4-04)

## Gaps

- **B (warfarin, hydroxyurea and other high-stakes dosing):** empty at YC in every batch since 2016, apart from the dead DoseDr.
- **D (ICU and deterioration):** empty in the latest batches. Sepsis Scout (2018) is the only one in any year.
- **India:** 13 of the 1,484 latest-batch companies are located in India (plus one false match, Indianapolis), and none of them is a health company. They are AI infra, voice AI (Bolna), courts (Adalat AI) and B2B tools. India-based YC health companies are older: Pulse (W19) and Veera (W21). (D7-01-F18)

## Sources

- yc-oss YC directory mirror, batches API: https://yc-oss.github.io/api/meta.json (OPENED; last_updated 2026-11-15), per-batch files at https://yc-oss.github.io/api/batches/<batch>.json , full directory https://yc-oss.github.io/api/companies/all.json
- YC company pages listed under each entry (OPENED as mirror records)
- Kaigo Health search results: https://healthcarediscovery.ai/companies/kaigo-health/ , https://www.roundfunded.com/en/yc-startup/kaigo-health (SNIPPET)
- Prana: https://www.ycombinator.com/launches/PPg-prana-an-ai-doctor-that-monitors-you-24-7 , https://www.onhealthcare.tech/p/the-yc-w26-health-tech-field-notes (SNIPPET)
- Juno: https://www.ycombinator.com/launches/QT7-juno-ai-health-assistant-for-chronic-illness , https://www.producthunt.com/p/juno-13/juno-chronic-illness-support , https://www.ucl.ac.uk/news/2026/jul/ucl-ai-health-startup-selected-influential-business-accelerator (SNIPPET)
- Pulse Active Stations: https://yourstory.com/2020/03/healthtech-startup-pulse-active-stations-health-analysis , https://telanganatoday.com/bioasia-2023-this-made-in-india-machine-can-measure-your-health-parameters-in-public , https://www.pitchonnet.com/marketing-moments/pulse-active-stations-to-launch-10000-smart-kiosks-across-the-nation-in-the-next-3-years-20756.html (SNIPPET)
