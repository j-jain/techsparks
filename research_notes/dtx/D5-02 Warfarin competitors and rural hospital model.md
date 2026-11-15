# D5-02 Warfarin loop: competitors, why nobody has built it for rural India, and the rural-hospital model (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: after D5-01 picked warfarin in rheumatic heart disease, the user asked three things. Who the competitors are. Why nobody has tried this in rural areas. Whether a machine that checks INR and recommends the dose, until the specialist comes much later, helps rural and understaffed hospitals.

Fact IDs are D5-02-Fxx. OPENED means the abstract or page was read; SNIPPET means only a search summary was seen. Earlier IDs (D5-01, D2-04) are reused where they apply.

## Digest

1. **Nobody in India runs remote warfarin dosing.**
   - Indian labs sell the test only: PT/INR for Rs 250-460 with home collection, and no dose advice (D5-02-F08).
   - Hospital INR clinics, such as SCTIMST Trivandrum and JSS Ganiyari, dose in person (D5-02-F04, F10).
   - India's own point-of-care INR device (SCTIMST's Chitra device) was transferred to Agappe in 2019 and is still in "post-transfer activities" (D5-02-F09).
2. **Abroad, the pieces exist but are built for rich clinics.** Meters (Roche CoaguChek, Siemens Xprecia, qLabs, Coag-Sense), clinic dosing software (DAWN AC, PARMA), and US and UK home-testing services all serve well-staffed anticoagulation clinics that insurers pay for (D5-02-F01, F11). None was found working in rural India.
3. **Machine-made dosing is proven at scale.** In a randomised trial of 13,219 patients at 32 centres, two dosing programs (PARMA 5 and DAWN AC) were as safe as experienced staff. They improved time in range at most centres and cut events by 24% in clot patients (DVT/PE). (D5-02-F01) Telemedicine anticoagulation across 25 trials raised time in range by 3.38 points (D5-02-F03).
4. **The trap: a machine only at the rural hospital will not be enough.** JSS Ganiyari already tested INR in its lab and had a doctor adjust the dose the same day, and median time in range was still 13% (D5-01-F03, D5-02-F04).
   - 30% of its warfarin patients came from over 150 km away (D5-02-F04).
   - Its doctors refuse warfarin to many high-risk patients because monitoring is impossible (D5-02-F04).
   - So the product must move the test closer to the patient's home, and the algorithm must step the dose decisively. OUR VIEW
5. **Why nobody has built it** (OUR VIEW, built on the facts cited):
   - Warfarin is a cheap generic, so no drug company pays for a support program.
   - The state scheme JSS describes paid for tertiary care, not outpatient visits or chronic medicines (D5-02-F04).
   - A point-of-care meter can read falsely low and kill. Alere's INRatio was withdrawn in 2016 after deaths, and anaemia (haematocrit below 30%) made it unreliable (D5-02-F06). Rural RHD patients are often anaemic.
   - Dose-advice software is a regulated medical device in India, likely Class B or C (D2-04-F06).
   - No Indian rule was found that lets a nurse change a dose on a standing order (D2-04, NOT FOUND).

## Findings

### Evidence that a machine can carry the dosing

- D5-02-F01. Poller L et al., "An international multicenter randomized study of computer-assisted oral anticoagulant dosage vs. medical staff dosage" (European Action on Anticoagulation), J Thromb Haemost 2008. Two commercial dosing programs (PARMA 5 and DAWN AC) were compared with manual dosing at 32 centres in 13 countries. 13,219 patients took part, 6,503 on staff dosing and 6,716 on computer dosing, giving 18,617 patient-years. INR tests were 193,890 manual and 193,424 computer. Clinical events were lower with the computer (P 0.1). In 3,209 DVT/PE patients, events fell by 37 (24%, P 0.001). Time in range improved at most centres (P below 0.001). Conclusion: the computer was as safe and effective as experienced staff. https://pubmed.ncbi.nlm.nih.gov/18489430/ (2008). OPENED (abstract via Europe PMC). Companion analysis: computer dosing cost EUR 51 less per patient. https://research.manchester.ac.uk/en/publications/the-cost-effectiveness-of-computer-assisted-anticoagulant-dosage-/ SNIPPET.
- D5-02-F02. A randomised trial at a Hamilton (Canada) clinic compared DAWN AC with a two-step paper schedule. Time in range was 71.0% against 71.9% (non-inferior), and doses followed the recommendation 99% against 90% of the time. In a separate 3-year audit of DAWN dosing, staff overrode the computer 23.3% of the time; the authors say control would improve with closer adherence. https://experts.mcmaster.ca/scholarly-works/3463987 (date per source). SNIPPET.
- D5-02-F03. Telemedicine-based management of oral anticoagulation, systematic review and meta-analysis, J Med Internet Res 2023. 25 randomised trials, 25,746 patients, moderate to high risk of bias. Time in range improved (16 studies, mean difference 3.38 points, 95% CI 1.12 to 5.65, I2 90%). Thromboembolism RR 0.75 (0.53 to 1.07), not significant. Major bleeding RR 0.94 and mortality RR 0.96, unchanged. In "multitasking" interventions, thromboembolism RR 0.20 (0.08 to 0.48). https://pubmed.ncbi.nlm.nih.gov/37428532/ (2023). OPENED (abstract via Europe PMC).
- D5-02-F05. Rwanda: since 2007, district hospitals supported by Partners In Health / Inshuti Mu Buzima have had point-of-care INR testing, a portable echo machine and warfarin. Nurses at these district hospitals follow patients' INR values and warfarin doses (World Heart Federation RHD congress abstract, 2023). https://world-heart-federation.org/world-congress-on-rhd/wp-content/uploads/sites/6/2023/11/ANTICOAGULATION-MANAGEMENT-OF-POSTOPERATIVE-RHEUMATIC-HEART-DISEASE-PATIENTS-IN-RWANDA.pdf (2023). SNIPPET. A 2025 meta-analysis put pooled time in range in sub-Saharan Africa at 0.16 (16%). https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1517162/pdf (2025). SNIPPET.

### The rural Indian setting

- D5-02-F04. Chebrolu P, Jain P, "Letter from Ganiyari", Natl Med J India 2018;31:51-52 (Jan Swasthya Sahyog, Chhattisgarh). Median INR among JSS warfarin patients was 1.7 (2014-2016). 30% of its warfarin patients came from more than 150 km away. One patient, Seema, lives 100 km away; each visit means at least 3 days away from her children, by walking, bus, train and an 18-km autorickshaw ride. The state insurance scheme (up to Rs 30,000 a year) covered tertiary care, not outpatient visits or chronic medicines. A 30-year-old RHD patient, Ram, reached an INR of 11 and haemoglobin of 4 g/dl after a pharmacist gave him diclofenac, and "barely survived". "In many of our patients, risks are so high that we do not prescribe warfarin." Lab testing is "difficult to make available in the subcentres" and should be offered at PHCs. https://nmji.in/letter-from-ganiyari-4/ (2018). OPENED.
- D5-02-F08. Lab PT/INR test prices in Indian cities run about Rs 250-460, with home sample collection: Tata 1mg Rs 250-400, Max Lab Rs 260-400, Apollo 24|7 Rs 409-460. Lupin Diagnostics and MFine also offer home collection. These sell the test only, with no dose advice. https://www.maxlab.co.in/lab-test/profile/delhi/prothrombin-time-with-inr-citrate-plasma (2026); https://www.apollo247.com/lab-tests/prothrombin-time-pt-inr-l-new-delhi-c-delhi (2026). SNIPPET.
- D5-02-F07. Point-of-care INR meter prices in India (Micropoint qLabs): IndiaMART lists the Q-1 at Rs 19,500, the Q3 Plus at Rs 24,900 to Rs 49,000, and the Q1 Pro at Rs 25,000. 1mg lists the Q2 at an MRP of Rs 52,000 and the eStation Q3 at Rs 60,000, both sold out. https://m.indiamart.com/proddetail/pt-inr-aptt-fib-meter-professional-testing-device-q3-plus-electrometer-21268130591.html (2026); https://www.1mg.com/otc/micropoint-q2-qlabs-electrometer-otc691740 (2026). SNIPPET. CoaguChek strips cost about Rs 649 each (D5-01-F09).
- D5-02-F09. SCTIMST's Chitra PT/INR device reads a finger-prick strip by image processing. In a 100-sample study, correlation was 0.87 with the lab and 0.77 with a commercial point-of-care device. It was transferred to Agappe Diagnostics in March 2019. A 2023 SCTIMST page still lists PT/INR under "post-transfer activities" needing an industry partner for clinical evaluation and approval. https://dspace.sctimst.ac.in/handle/123456789/11053 (2021); https://new1.sctimst.ac.in/?p=3920 (2023). SNIPPET. NOT FOUND: a market launch or CDSCO licence.
- D5-02-F10. SCTIMST's cardiology department runs an INR clinic. With NIT Calicut it built a support-vector regression model to predict maintenance warfarin doses, from 222 stable patients with tilting-disc mitral valves. This is a research model, not a service. https://export.arxiv.org/pdf/2004.11460 (2020). SNIPPET.

### Competitors abroad, and the device failure that shapes the risk

- D5-02-F11. Home and clinic INR services abroad: Acelis Connected Health (US) calls itself the leading provider of INR self-testing services and says Medicare and many insurers cover home INR monitoring. Philips runs INR self-testing through Raytel's INR@Home. Inhealthcare partnered with Roche on a UK self-testing service (2017). CoaguSense's Coag-Sense has US clearance for professional and home use. https://www.stoptheclot.org/article120.htm (date unknown); https://www.news-medical.net/news/20170507/Inhealthcare-and-Roche-Diagnostics-partnership-brings-new-innovation-to-self-testing-market.aspx (2017); https://clpmag.com/diagnostic-technologies/hematology-serology/coagulation-testing/coagusense-receives-european-approval-pt-inr-patient-self-testing/ (date unknown). SNIPPET. THEIR CLAIM for "leading".
- D5-02-F06. Alere INRatio, the warning case: May 2014: professional strips recalled after results ran 3.1 to 12.2 INR units below the lab, with 9 serious adverse events including 3 bleeding deaths. December 2014: users were told anaemia with haematocrit below 30% is a contraindication, along with high-fibrinogen states such as infection. July 2016: the INRatio and INRatio2 systems were withdrawn as a Class I recall after FDA found the software fix unproven; Alere expected a US$70-90 million charge. https://www.fiercebiotech.com/medical-devices/alere-recalls-test-strips-after-patient-deaths (2014); https://www.tctmd.com/news/fda-no-more-chances-embattled-coagulation-monitoring-system (2016); https://www.massdevice.com/alere-withdraws-inratio-monitors-u-s-market/ (2016). SNIPPET.
- D5-02-F12. Brazil, a close analogue: DOACs are paid out of pocket, while the public system (SUS) funds warfarin fully, so warfarin management stays in primary care. https://bmcprimcare.biomedcentral.com/counter/pdf/10.1186/s12875-022-01647-5.pdf (2022). SNIPPET.

## Competitor map (OUR VIEW, built from the facts cited)

| Who | What they do | Rural India? | Gap left |
|---|---|---|---|
| Roche CoaguChek, Siemens Xprecia, qLabs, Coag-Sense (D5-02-F07, F11) | Finger-prick INR meters | qLabs is sold in India at Rs 19,500-60,000 | A number only, with no dose decision |
| DAWN AC, PARMA (D5-02-F01, F02) | Dosing software for anticoagulation clinics | Not found in India | Built for staffed clinics with a lab; no rural, low-literacy or offline design |
| Acelis, Philips INR@Home, Inhealthcare (D5-02-F11) | Home self-testing services paid by insurers | No | Depend on Medicare or NHS payment |
| Indian lab chains: 1mg, Max, Apollo, Lupin (D5-02-F08) | PT/INR test with home collection | Cities | Test only; the result waits for a doctor visit |
| SCTIMST, JSS INR clinics (D5-02-F04, F10) | Lab INR, doctor sets the dose in person | JSS yes | Patients travel; median time in range 13% (D5-01-F03) |
| Chitra PT/INR device with Agappe (D5-02-F09) | Indian point-of-care meter | Not launched | A meter, not a dosing service |
| Lupin Lyfe (D1-04-F15) | Licensed digital cardiac rehab and heart-failure clinic | Claims 280 districts | No INR or warfarin product found |

## The rural-hospital model (OUR DESIGN)

Hub and spokes:
- **Hub: the rural or district hospital** with a medical officer (MBBS) and no cardiologist. It holds the patient list, approves every dose, and handles referrals.
- **Spokes: PHCs, health and wellness centres, or ASHAs** with a shared meter. Tests happen near home every 2-4 weeks, which removes the 150 km trips (D5-02-F04).

One visit, step by step:
1. Haemoglobin check first. A low reading flags the INR as untrustworthy and sends a sample to the lab (D5-02-F06).
2. INR reading: the meter result is typed in or photographed.
3. Five questions: missed tablets, bleeding, black stools, new medicines (painkillers such as diclofenac, D5-02-F04), and pregnancy.
4. The algorithm proposes the next weekly dose and the next test date.
5. The medical officer approves with one tap.
6. Hard stops go straight to the hub and the cardiologist: INR above 5, any bleeding, pregnancy, or a reading that disagrees with the last one by a wide margin.

Specialist and outcome:
- The cardiologist reviews flagged patients each week from a dashboard, not every routine dose.
- The measure is each patient's time in range, against the hospital's own baseline (about 13% at JSS, D5-01-F03).

What this changes for the hospital: it can take on warfarin patients it now turns away (D5-02-F04), and it gets a monthly time-in-range number. OUR VIEW

## Not found and next checks

- Whether Agappe launched the Chitra meter, and its price.
- Price per strip for qLabs strips in India.
- Whether any state NCD programme or Ayushman Arogya Mandir already funds INR testing at PHCs.
- Whether PIH Rwanda published time in range for its nurse-run district clinics.
- Anaemia prevalence among RHD patients on warfarin in India (sets how often the haemoglobin gate fires).
