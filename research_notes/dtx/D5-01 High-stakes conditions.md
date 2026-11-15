# D5-01 High-stakes conditions: which serious disease to build the loop for (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: the user asked to replace the blood-pressure pick with a serious, specific disease. Here a missed or wrong dose does real harm within days or weeks, a specialist normally makes the dose decisions, and rural patients see that specialist rarely. This note compares four candidates on the same rubric as `DT1-triage.md`, adds a "harm per missed or wrong dose" column, and records the facts behind each score.

Fact IDs are D5-01-Fxx. OPENED means the source page or abstract was read; SNIPPET means only a search summary was seen. Heart-failure facts reuse the existing D1-01 IDs.

## Digest

Answer: build the loop for **warfarin in rheumatic heart disease**, meaning patients with a mechanical valve or with AF caused by a rheumatic valve. Keep **sickle cell hydroxyurea dosing** as the second protocol on the same engine. Under the old rubric the two are level (3.70 and 3.75). Once harm per missed or wrong dose is weighted, warfarin leads (4.03 and 3.56). OUR ARITHMETIC

Facts that matter most:
1. In rural India, INR control is far worse than the rest of the world, and it fails on the low side. At a rural Chhattisgarh hospital the median time in range was 13.0%, and patients spent a median 77.5% of time below range and 0% above. Distance to the clinic did not explain it. (D5-01-F03) The gap is in how doses are set, not in how far patients travel, and setting doses is what the loop does.
2. India holds 13.2 million of the world's 33 million people with rheumatic heart disease (RHD), 40%, and about 120,000 of 347,000 RHD deaths (2015). (D5-01-F01) This corrects the plan's "about a third", which is the share of deaths, not of patients.
3. RHD patients on warfarin cannot switch to newer blood thinners. In INVICTUS (4,531 patients, mean age 50.5, 72.3% women), rivaroxaban led to more events and more deaths than warfarin-type drugs, with no difference in major bleeding. (D5-01-F04)
4. The loop itself has survival proof. When patients tested INR at home and set the dose from a fixed schedule, deaths fell (RR 0.55) and clots fell (RR 0.47). When they tested at home and phoned the clinic, deaths did not fall (RR 0.94). (D5-01-F05)
5. Sickle cell: national screening found 2,16,118 patients by 28 July 2025, and hydroxyurea is stocked down to sub-health centres. (D5-01-F12) India's own workflow keeps the dose at 10-15 mg/kg and raises it only "in definite indications", with a blood count 1-3 months after each change. (D5-01-F13) Raising the dose to about 30 mg/kg cut sickle events (IRR 0.43) and hospital stays (IRR 0.21) in Ugandan children, with the same toxicity. (D5-01-F14) Indian doctors keep doses low out of "fear of adverse events and noncompliance of patients for regular monitoring of blood parameters". (D5-01-F15)
6. Epilepsy drops to third. No trial was found in which non-specialists adjust the dose. The one Indian trial tested home delivery of medicine and adherence support, not dose changes. (D5-01-F21, F22)

Surprises:
- Under-dosing, not over-dosing, is the main warfarin failure in rural India (D5-01-F03). A loop that steps the dose up safely has more room to help than one that only guards against bleeding.
- In the Chhattisgarh cohort, only 10% of warfarin patients had a mechanical valve, and 84.2% could have used a newer blood thinner by indication (D5-01-F03). The market that cannot escape warfarin is mechanical valves plus rheumatic AF, not all warfarin users.
- The sickle cell loop would ask doctors to go beyond the national workflow, which sets low doses (D5-01-F13). That is a clinical-acceptance risk the warfarin loop does not carry, because its INR targets are standard.

Still unknown (NOT FOUND):
- How many Indians take warfarin for RHD.
- The Indian price of a CoaguChek meter.
- An Indian startup running remote INR or hydroxyurea dosing; none was found in one search each.
- India's official neurologist count; the government says it is not kept centrally.

## Findings

### Warfarin in rheumatic heart disease

- D5-01-F01. Karthikeyan G, "Rheumatic heart disease in India: declining, but not fast enough", Natl Med J India 2017;30(5):247-248, citing GBD (Watkins et al., NEJM 2017). In 2015, India had 13.2 million of an estimated 33 million people with RHD worldwide (40%), and nearly 120,000 of 347,000 RHD deaths. India's age-standardised RHD mortality fell from 15.5 to 12.7 per 100,000 (1990 to 2015, 18%), against 48% worldwide and 71% in China. Most valve surgery is done at a few public tertiary hospitals, with long waiting lists. Two-year mortality across 14 endemic countries was 16.7% (Zühlke et al., Circulation 2016, as cited). https://nmji.in/rheumatic-heart-disease-in-india-declining-but-not-fast-enough/ (2017). OPENED.
- D5-01-F02. Zilla P, Human P, Pennel T, "Mechanical valve replacement for patients with rheumatic heart disease: the reality of INR control in Africa and beyond", Front Cardiovasc Med 2024 (perspective). Groote Schuur Hospital, Cape Town: 552 RHD mechanical-valve patients, 21,826 INR tests over 2015-2023, time in range 27.2% (SD 24.1), 61% of results below range. Time in range is 20-40% in poorer countries, against the 60-70% counted as safe in richer ones. The country figures cited include India 44%. Ten-year mortality in India after a mechanical mitral valve in young patients was 41%, citing John et al., J Thorac Cardiovasc Surg 1990, an old series. Self-tests are not available in these settings. https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2024.1347838/full (2024). OPENED.
- D5-01-F03. Chebrolu P, Patil S, Laux TS, Al-Hammadi N, Jain Y, Gage B, "Quality of anticoagulation with warfarin in rural Chhattisgarh, India", Indian J Med Res 2020;152(3):303-307. Retrospective, 2014-2016, a secondary-care rural health system. 249 patients and 2,839 INR visits; 162 patients with at least two visits were analysed. Median time in range 13.0% (IQR 0-34.8). Median time below range 77.5% (IQR 45-100), above range 0.0% (IQR 0-11.6). Median INR was 1.7 against a 2.0-3.0 target. Median distance to the clinic was 78 km, with no correlation to time in range (rho 0.009, P 0.906). Indications: AF without a mechanical valve 62.6%, mechanical valve 10.0%, clots in a vein or lung 21.6%. Rheumatic status was not recorded. "In most of rural India, warfarin is the only oral anticoagulant available." Newer blood thinners would have suited 84.2% (210 of 249) by indication. https://pmc.ncbi.nlm.nih.gov/articles/PMC7881821/ (2020). OPENED.
- D5-01-F04. Connolly SJ et al., "Rivaroxaban in rheumatic heart disease-associated atrial fibrillation" (INVICTUS), NEJM 2022. 4,565 enrolled and 4,531 analysed; mean age 50.5, 72.3% women. Primary-outcome events: 560 with rivaroxaban against 446 with a vitamin K antagonist. Restricted mean survival 1,599 against 1,675 days (difference -76, 95% CI -121 to -31). More deaths with rivaroxaban (difference -72 days, 95% CI -117 to -28), and no significant difference in major bleeding. Conclusion: a vitamin K antagonist gives fewer events "without a higher rate of bleeding". Funded by Bayer. https://pubmed.ncbi.nlm.nih.gov/36036525/ (2022). OPENED (abstract via Europe PMC).
- D5-01-F05. Heneghan CJ et al., Cochrane review CD003839.pub3, "Self-monitoring and self-management of oral anticoagulation". 28 randomised trials, 8,950 participants. Re-opened to confirm D1-02-F05. Self-management (patient tests and adjusts the dose by a schedule): thromboembolism RR 0.47 (0.31 to 0.70; 11 studies, 3,497 people); all-cause mortality RR 0.55 (0.36 to 0.84; 8 studies, 3,058 people). Self-monitoring (patient tests and calls the clinic): mortality RR 0.94 (0.78 to 1.15). Evidence quality is moderate. https://pubmed.ncbi.nlm.nih.gov/27378324/ (2016). OPENED (abstract via Europe PMC).
- D5-01-F06. REMEDY sub-study, Cape Town: mean time in range 0.42 (95% CI 0.31 to 0.53) for mechanical-valve patients and 0.67 for others. Distance to the INR clinic was not associated with control. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4456049/ (2015). SNIPPET.
- D5-01-F07. REMEDY interim report (Healio, 2012, pooled across regions): in the 6 months before enrolment, 14% had no INR measurement and 78% were not at their INR target; 71% of patients with AF or atrial flutter did not know their target INR. https://www.healio.com/news/cardiology/20120427/urgent-treatment-action-important-to-reduce-rheumatic-heart-disease-burden-worldwide (2012). SNIPPET. Preliminary conference data.
- D5-01-F08. In a multinational RHD cohort that included India, only 4.4% underwent valve surgery (Healio report on access to surgery in endemic countries). https://www.healio.com/news/cardiology/20240605/access-to-surgery-where-rheumatic-heart-disease-is-endemic-a-barrier-to-improving-survival (2024). SNIPPET.
- D5-01-F09. Price of INR testing in India. CoaguChek XS PT strips, 48 per box: Rs 31,153.99 on Himkhand, about Rs 649 per strip (OUR ARITHMETIC). https://himkhand.com/products/coaguchek-pt-test-strips-clia-waived-48-box (2026). SNIPPET. Other PT/INR meters on IndiaMART: Rs 35,000 and Rs 19,500 (not CoaguChek). https://m.indiamart.com/impcat/coagulometer.html (2026). SNIPPET. NOT FOUND: an Indian CoaguChek meter price.
- D5-01-F10. A cardiac surgeon (A. Sampath Kumar, STS profile) puts India's RHD burden "in excess of six million patients". Six charitable institutions do about 6,000 free procedures a year. https://www.sts.org/node/8286 (date unknown). SNIPPET. THEIR CLAIM. This is lower than the GBD figure in F01; use F01.
- D5-01-F11. Competitors. One search found no Indian startup running remote INR dose management. UK: Inhealthcare launched a self-testing app for warfarin users in 2016, and notes patients attend a warfarin clinic about 14 times a year. https://www.news-medical.net/news/20160921/Inhealthcare-introduces-first-self-testing-mobile-app-for-warfarin-users.aspx (2016). SNIPPET. NOT FOUND: Indian players (thin search; needs a second pass by name, for example hospital anticoagulation clinics at SCTIMST and CMC Vellore).

### Sickle cell disease: hydroxyurea dosing

- D5-01-F12. Medical Dialogues, 2 Aug 2025, reporting Health Minister JP Nadda's Lok Sabha answer. As of 28 July 2025: 6,04,50,683 people screened, 2,16,118 diagnosed with sickle cell disease, over 16.7 lakh carriers. Portal registrations by state: Odisha 96,484, Madhya Pradesh 30,580, Gujarat 28,150, Chhattisgarh 26,104, Maharashtra 23,218. Hydroxyurea is on the NHM essential list and "available even at sub-health centres". Target: 7 crore screened by FY 2025-26. No figure on how many patients are on hydroxyurea or in follow-up. https://health.medicaldialogues.in/health/over-6-crore-people-screened-for-sickle-cell-anaemia-across-india-health-minister-152826 (2025). OPENED (secondary report; the Lok Sabha PDF at https://eparlib.sansad.in/bitstream/123456789/2993410/1/AS193_Uglaqw.pdf did not download).
- D5-01-F13. Department of Health Research / ICMR, Standard Treatment Workflow, sickle cell disease (ICD-10 D57), July 2020. Hydroxyurea for patients above 2 years, and "may be offered" from 9 months. Dose: infants and children 10-15 mg/kg/day, adolescents 15 mg/kg/day. Escalation by 5 mg/kg every 2-3 months "only in definite indications". Blood count 1-3 months after starting or after any dose change. Baseline tests: blood count, liver, kidney, pregnancy. No neutrophil or platelet hold thresholds are given. About 88% of sickle homozygous cases in Asia are Indian. https://icmr.gov.in/icmrobject/uploads/STWs/1726568229_sickle_cell_disease.pdf (2020). OPENED.
- D5-01-F14. John CC et al., "Hydroxyurea dose escalation for sickle cell anemia in sub-Saharan Africa" (NOHARM MTD), NEJM 2020. Double-blind randomised trial, Uganda. 187 children (mean age about 4.7). Mean dose 19.2 mg/kg fixed against 29.5 mg/kg escalated. The safety board halted the trial early for benefit. Primary threshold (Hb 9.0 or more, or HbF 20% or more, at 24 months): 86% against 37%. Sickle-related adverse events IRR 0.43 (0.34 to 0.54); pain crises IRR 0.43; acute chest syndrome or pneumonia IRR 0.27; transfusions IRR 0.30; hospitalisations IRR 0.21. Dose-limiting toxicity was similar in both arms, with no severe neutropenia or thrombocytopenia. https://pubmed.ncbi.nlm.nih.gov/32579813/ (2020). OPENED (abstract via Europe PMC).
- D5-01-F15. Khargekar N et al. (ICMR-National Institute of Immunohaematology, Mumbai), ASH 2023 abstract, low dose (10 mg/kg/day) against standard dose (20 mg/kg/day) hydroxyurea in Indian children. "Low dose is recommended by most of the physicians in India due to fear of adverse events and noncompliance of patients for regular monitoring of blood parameters" (the second half of the quote is from the search snippet). The trial was still running: 140 enrolled, 37 followed to 6 months. HbF rose 4.81% on 20 mg/kg against 1.55% on 10 mg/kg. Two children on 20 mg/kg had neutrophils below 1,000 per microlitre; the drug was stopped for a week and restarted. No crises in either arm at 6 months. https://ash.confex.com/ash/2023/webprogram/Paper191234.html (2023). OPENED.
- D5-01-F16. Indian SCD Registry (ISCDR), Blood Cells Mol Dis 2024. 324 patients at 12 primary health centres in six tribal districts, one year of data collected through an Android app. 85.2% did not know their status before enrolling, and 83.64% were taking hydroxyurea. 38.27% were hospitalised and 12.04% transfused in the past year. https://pubmed.ncbi.nlm.nih.gov/39024737/ (2024). OPENED (abstract via Europe PMC).
- D5-01-F17. No low-cost, finger-prick blood count with neutrophils is on sale for rural India. IIT Kharagpur's spinning-disc device claims about Rs 10 a test and 95% accuracy, but is a proof of concept. https://thebetterindia.com/212989/iit-kharagpur-innovation-complete-blood-count-test-health-india-nor41 (2020). SNIPPET. THEIR CLAIM. Adsys Medtech's device is also listed as a proof of concept. https://indiascienceandtechnology.gov.in/technologies/point-care-device-complete-blood-count (date unknown). SNIPPET.
- D5-01-F18. Digital sickle cell follow-up in India. ICMR-NIRTH researchers argued for mHealth adherence and monitoring tools (JMIR mHealth 2021). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8080143/ (2021). SNIPPET. SEWA Rural uses counsellor phone calls as reminders. https://sewarural.org/wp-content/uploads/2023/10/effectiveness_of_a_hospital_based_comprehensive.4.pdf (2023). SNIPPET. NOT FOUND: any service that adjusts hydroxyurea doses from blood counts between visits.

### Epilepsy

- D5-01-F19. The treatment gap ranges from 22% among urban middle-income people to 90% in villages. In the BURNS survey, prevalence was 11.9 per 1,000 rural against 5.7 urban. https://pmc.ncbi.nlm.nih.gov/articles/PMC4001222 (date per source). SNIPPET.
- D5-01-F20. Neurologist numbers are CONTESTED. A Lok Sabha answer (Feb 2023) says the neurologist-to-patient ratio "is not maintained centrally". https://eparlib.sansad.in/bitstream/123456789/1470084/1/AU1427.pdf (2023). SNIPPET. Estimates run from "fewer than 2,500" (Hindustan Times 2021) to about 5,400. The higher figure is implied by 3,812 association members counted as about 70% of the total (2015). https://stride-dementia.org/desk-review/02-03-01-india/ (date unknown). SNIPPET. Either way, that is under one neurologist per 2.5 lakh people. OUR ARITHMETIC
- D5-01-F21. Singh G et al., "A cluster-randomized trial comparing home-based primary health care and usual clinic care for epilepsy in a resource-limited country", Epilepsia Open 2022 (Ludhiana, Punjab). 24 clusters of 10 people, over 24 months. Home care meant drug supply, adherence support and self-management advice from a primary-care-level worker. It raised adherence (coefficient 0.585, P 0.001) and lowered monthly seizures (coefficient -2.060, P 0.002). Time to first seizure was the same in both arms. Trial exit was 37% with clinic care against 19% with home care. Doses were not adjusted by protocol. https://pubmed.ncbi.nlm.nih.gov/36213959/ (2022). OPENED (abstract via Europe PMC).
- D5-01-F22. BRIDGE (Nigeria): cluster-randomised non-inferiority trial. Community health workers prescribe and adjust four anti-seizure drugs by a standard protocol, supervised by a physician. Outcome: share of children seizure-free for more than 6 months at 24 months. No results were found. https://cdn.clinicaltrials.gov/large-docs/75/NCT04290975/Prot_000.pdf (protocol). SNIPPET.

### Heart failure (existing IDs, not re-researched)

- STRONG-HF, rapid up-titration: readmission or death RR 0.66 (D1-01-F27).
- TIM-HF2: the benefit grew with distance from a cardiologist (D1-01-F31).
- India's national registry: 47.5% of eligible patients received guideline drugs; mortality 14.2% at 90 days and 22.1% at 1 year (D1-01-F47, F48).

## Scores

Weights as in `DT1-triage.md`: proof 25, market 20, feasibility 20, gap 15, deep-tech 10, low risk 10. Feasibility now means "a 6-month pilot" rather than "built overnight", because the event is over.

The last two columns differ in one way. "Old rubric" is the DT1 weighting. "Harm lens" gives harm per missed or wrong dose a weight of 25 and scales the other six weights to three quarters (0.75 x old + 0.25 x harm). All scores are OUR VIEW.

| Condition and loop | Proof | Market | Feasibility | Gap | Deep-tech | Low risk | Harm per dose | Old rubric | Harm lens | Basis |
|---|---|---|---|---|---|---|---|---|---|---|
| Warfarin in RHD (mechanical valve, rheumatic AF): INR reading, then dose | 5 | 3 | 3 | 5 | 3 | 2 | 5 | 3.70 | 4.03 | D5-01-F01, F03, F04, F05, F09; OUR VIEW |
| Sickle cell: hydroxyurea raised by blood count and weight | 4 | 4 | 3 | 5 | 3 | 3 | 3 | 3.75 | 3.56 | D5-01-F12 to F17; OUR VIEW |
| Heart failure: weight, BP, pulse, then diuretic and drug steps | 4 | 3 | 3 | 4 | 3 | 2 | 4 | 3.30 | 3.48 | D1-01-F27, F31, F47; OUR VIEW |
| Epilepsy: seizure count, then drug steps | 2 | 4 | 3 | 4 | 4 | 3 | 4 | 3.20 | 3.40 | D5-01-F19 to F22; OUR VIEW |
| Reference: blood-pressure step loop (DT1 scores, overnight feasibility) | 5 | 4 | 5 | 4 | 3 | 4 | 2 | 4.35 | 3.76 | DT1-triage.md; OUR VIEW |

Reasons, one line each (OUR VIEW):
- **Warfarin.**
  - Proof 5: the Cochrane mortality signal comes from exactly this loop (D5-01-F05).
  - Gap 5: rural time in range is 13% and no Indian service was found (D5-01-F03, D5-01-F11).
  - Harm 5: a valve clot or a bleed can follow within weeks, in either direction.
  - Market 3: 13.2 million people have RHD (D5-01-F01), but the number on warfarin is unknown, and non-valve AF can move to newer drugs (D5-01-F03).
  - Feasibility 3: strips cost about Rs 649 each (D5-01-F09), so the likely model is a shared meter at the health centre or ASHA level, not one meter per patient.
  - Low risk 2: a wrong dose can kill, so every change needs a clinician's tap and the INR targets must be hard limits.
- **Sickle cell.**
  - Market 4: 2.16 lakh diagnosed patients, the government already pays, and hydroxyurea is free (D5-01-F12).
  - Proof 4: the trial was in children in Uganda and was not a digital loop (D5-01-F14).
  - Feasibility 3: no cheap finger-prick blood count is on sale (D5-01-F17).
  - Harm 3: a missed dose costs benefit over weeks, not days.
  - The main risk is that the loop would push doses above the national workflow (D5-01-F13).
- **Heart failure.** Unchanged from DT1 except that feasibility rises to 3 for a pilot with health-centre lab tests. Many Indian heart-failure patients have RHD, so it can share the warfarin pilot's patients.
- **Epilepsy.** Proof 2: no dose-loop trial was found, and the Indian trial tested medicine supply and adherence (D5-01-F21, D5-01-F22). The rural need is real (D5-01-F19).
- **Blood pressure.** It still scores highest on the old rubric, which rewarded overnight buildability and patient pool size. On the user's harm lens it falls behind warfarin.

## What changes for the build (OUR VIEW)

- The engine stays as it is (D2-01). The protocol file changes:
  - INR reading in place of the BP reading.
  - A warfarin dose schedule keyed to the target range: 2.0-3.0, or 2.5-3.5 for mechanical mitral valves (D5-01-F03).
  - The "was the medicine taken" check comes before any step-up, because 77.5% of time below range may partly reflect missed tablets rather than too low a dose (D5-01-F03).
- The measurement becomes a health-centre or ASHA-held INR meter. A home meter per patient is not affordable at about Rs 649 a strip (D5-01-F09). OUR ESTIMATE
- The pilot measures time in range at 3 months against the clinic's own baseline, which D5-01-F03 puts near 13%. This shows a result far faster than blood pressure could.
- Sickle cell is the second protocol in the same file format: dose per kg, a blood-count gate before each step, a hold rule on low neutrophils, and pain days as the symptom input. Pitch it as the government-payer expansion.

## Open items for a next pass

- Count of Indians on warfarin for RHD: try REMEDY India and CSI, or hospital anticoagulation clinic volumes (SCTIMST, CMC Vellore, AIIMS).
- Indian CoaguChek meter price, and Indian-made INR meters.
- Competitors searched by name: hospital anticoagulation clinics, and diagnostics chains offering home INR collection.
- The Lok Sabha primary PDF for F12.
- India's 2023 sickle cell mission guideline, if it updates the 2020 workflow dose.
