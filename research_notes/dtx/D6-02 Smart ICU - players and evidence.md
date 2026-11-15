# D6-02 Smart ICU: who is already there, and what the evidence says (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: the user's idea combines Cloudphysician (remote ICU) and Cadence (protocol loops). This note checks what Cloudphysician, 10BedICU and the state tele-ICU hubs already do, and what trials say about remote ICU care, alerts, hub-and-spoke networks, and the camera features the user proposed (reading monitors, spotting jaundice).

Fact IDs are D6-02-Fxx. OPENED means the page or abstract was read; SNIPPET means only a search summary was seen. Earlier IDs are reused: D2-06-F1 and F2, D5-01-F11 (Cadence), D3-06-F31 (Cadence FDA pilot), D5-01-F01 and F07 (Dozee).

## Digest

1. **Cameras + AI + remote intensivists are already sold in India.**
   - Cloudphysician (founded 2017) claims 1,30,000+ patients across 280 hospitals (D6-02-F01). Its RADAR platform includes camera vision (NETRA), AI note-writing (AIRA), voice-to-text (SWARA) and paper digitising (HERA) (D6-02-F01).
   - It raised a $10.5 Mn Series A led by Peak XV in Jun 2024 (D6-02-F03).
   - 10BedICU runs 216 ten-bed ICUs and 15 tele-ICU hubs in public hospitals on free, MIT-licensed software (CARE) (D6-02-F05, F07).
2. **Remote ICU alone has weak proof.**
   - The best trial, TELESCOPE (30 Brazilian ICUs, 17,024 adults), found no shorter ICU stay and no difference in any secondary outcome (D6-02-F12).
   - A 2025 systematic review rated the evidence on ICU deaths "very low" certainty and did not pool it (D6-02-F15).
   - Before-after studies look better: pooled OR 0.75, but only where ICUs had more deaths than predicted beforehand (D6-02-F14).
3. **Where benefit appears, it comes from acting on time and following standard steps.**
   - Lilly 2011: much of the mortality gain was explained by better adherence to best practice (D6-02-F13).
   - TREWS: lower sepsis mortality only when a clinician confirmed the alert within 3 hours (D6-02-F16).
   - Tamil Nadu STEMI hub-and-spoke: a written pathway raised angiography at spokes from 3.5% to 31.3%, and one-year deaths fell from 17.6% to 14.2% (D6-02-F17).
4. **Camera reading of monitor screens works in a preprint.** It reached above 98.9% accuracy for heart rate, SpO2 and arterial BP on 6,498 images from Vietnamese ICUs and open datasets (D6-02-F18). Not peer reviewed.
5. **Camera jaundice checks are small studies:** 46, 66 and 130 patients (D6-02-F20). Fine as a trend aid; the lab bilirubin stays the decision value. OUR VIEW
6. **Nobody found runs the full path** (ward, then ICU, then home) with treatment steps carried out by protocol. Cloudphysician publishes no protocol-step product (D6-02-F01, F02). Cadence works at home in the US only (D2-06-F1, D5-01-F11). OUR VIEW, based on the pages read, not an exhaustive search.

## Findings

### Players

- D6-02-F01. The Better India (5 Dec 2025, first published on NITI's Frontier Tech Repository): Cloudphysician, Bengaluru, founded 2017 by Dr Dhruv Joshi and Dr Dileep Raman (pulmonary and critical care fellowships, Cleveland Clinic).
  - **Product:** "Smart ICU in a box", a 24/7 tele-ICU with the RADAR command centre.
  - **Tools:** AIRA (note-writing, "reduces documentation time by 40%"); HERA (transcription, digitises paper records); NETRA (computer vision, "increases nursing efficiency by 30%"); SWARA (voice-to-text).
  - **Scale:** "over 1,30,000 patients across 280 hospitals"; 40,000 patients in 17 states in 2022.
  - No price, no bed count, no intensivist ratio.
  - https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930 (2025). OPENED. THEIR CLAIM for the percentages.
- D6-02-F02. NITI Frontier Tech Repository page on Cloudphysician (undated; image dated Jul 2025).
  - **Scale, two figures:** "40,000+ patients across 70 hospitals in 17 states" and "130,000+ patients across 480 hospitals".
  - **Claims:** "up to 40% decrease" in ICU mortality; "up to 50% increase" in ICU resource use; "1 additional life" per 10 patients seen.
  - NITI's disclaimer: submissions are "as is", not endorsed or validated.
  - https://frontiertech.niti.gov.in/story/cloudphysicians-radar-system-delivers-24-7-critical-care-anywhere-in-india (2025). OPENED. THEIR CLAIM.
- D6-02-F03. Inc42, 25 Jun 2024: Series A of $10.5 Mn (Rs 87.3 Cr), led by Peak XV Partners, with Elevar Equity and venture-debt firm Panthera Peak.
  - Claims: 200+ hospitals in 23 states; 1 lakh patients treated; a 50% rise in ICU use at partners; eyeing "10% of the Indian critical care market".
  - Funds go to the RADAR AI platform and expansion including the US.
  - Pre-Series A: $4 Mn led by Elevar (2021).
  - https://inc42.com/?p=464235 (2024). OPENED. THEIR CLAIM.
- D6-02-F04. Cloudphysician operating details:
  - A 2020 report: RADAR "enables an intensivist to cater to the needs of 60 to 80 patients in multiple locations" (YourStory SocialStory, Aug 2020).
  - An older report: adopted in about 230 hospitals, "90% of which are private".
  - Undated: about 2,400 ICU beds across 230 hospitals in about 100 cities.
  - One hospital customer (Paramount) reported average ICU stay falling from five days to three.
  - https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution (2020); https://testing.dev.theedgesingapore.com/digitaledge/technopreneurs/ai-beds-remote-icus-start-ups-are-plugging-indias-health-gaps (date unknown). SNIPPET (YourStory returned 403).
- D6-02-F05. 10BedICU website.
  - **Scale:** 216 units (counter); "over 200 units in 10 states"; 15 TeleICU hubs.
  - **Launches:** Manipur May 2022, Karnataka Nov 2022, Nagaland Jan 2023, Assam Jun 2023, Meghalaya Dec 2023, Puducherry Feb 2024, Sikkim Mar 2024. Jharkhand, Telangana and Andhra Pradesh are listed without dates.
  - **Model:** public-private partnership. The state provides space, medical staff, supplies and utilities, and signs an MoU to cover operating costs. 10BedICU pays the capital cost: equipment, CARE software, tele-ICU technology and training.
  - **Funders:** donor logos include Khosla Family Trust, Coal India, HDFC Bank, Google and Hamilton Medical. Contact address: eGovernments Foundation, Bengaluru.
  - "1,00,000+ lives saved" (THEIR CLAIM, no method given).
  - https://www.10bedicu.org/ (accessed 2026-11-16). OPENED.
- D6-02-F06. Think Global Health on 10BedICU.
  - **People and start:** set up in 2021 by Srikanth Nadhamuni, Raj Pakala and Nagesh Reddy Gouravaram, starting with 40 hospitals in Telangana.
  - **Hubs:** public medical colleges, each linked to 3-4 hospitals; CARE shows ICU data and a live camera feed, with WhatsApp integration.
  - **Problems:** slow government decisions, sites not ready, internet and electricity not always available, tele-ICU regulation unresolved.
  - **Missing services:** an expert notes that ICUs need an operating theatre, blood bank, dialysis and radiology, often missing in rural hospitals.
  - No outcome statistics.
  - https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages (date per page). OPENED.
- D6-02-F07. CARE (github.com/ohcnetwork/care): "a Digital Public Good", MIT licence.
  - Listed features: real-time analytics for beds, ICUs, ventilators and oxygen; integrated telemedicine and triage; "real-time video feed and vitals monitoring".
  - 423 stars, 636 forks.
  - https://github.com/ohcnetwork/care (accessed 2026-11-16). OPENED.
- D6-02-F08. State hub-and-spoke tele-ICUs:
  - Jharkhand links district hospitals in Latehar, Gumla, Khunti, Ranchi and Chatra to RIMS Ranchi, with a target of a 10-bed ICU and tele-ICU in every district.
  - Nagaland's hub at NHAK uses high-resolution cameras and monitor integration at spokes; most funding came from Vinod Khosla Family Ventures (2023).
  - Meghalaya launched two hubs for 14 centres in 11 districts (Dec 2023).
  - J&K plans tele-ICU in 7 new government medical colleges, run by a private agency.
  - https://www.devdiscourse.com/article/health/3847411-revolutionizing-healthcare-jharkhands-strategic-tele-icu-network-expansion ; https://ipr.nagaland.gov.in/node/10455 ; https://northeastlivetv.com/topnews/meghalaya-govt-launches-10-bed-icu-project-tele-icu-hub ; https://www.dailyexcelsior.com/?p=1986757 (2023-2025). SNIPPET.
- D6-02-F09. Private hospital eICUs, 2016: Apollo's Hyderabad eICU monitored 200 patients in six states, and Fortis Delhi tracked 350. Software came from GE and Philips. Hospitals charged $10-30 a day for remote monitoring (D6-01-F09). OPENED via D6-01-F09.
- Dozee MillionICU: converts government ward beds into connected step-down beds; plans 6,000 beds in about 140 public hospitals with British International Investment (D5-01-F07). Its own study found 19-42% specificity, meaning many alerts on patients who did not get worse (D5-01-F01).
- Cadence (US):
  - Health-system partners ship a cuff (plus a scale for heart failure); a 24/7 team manages medicines (D5-01-F11).
  - $100M Series C, Jun 2026 (D2-06-F1). It claims 55% of alerts resolved without human adjustment (D2-06-F2, THEIR CLAIM).
  - Its HypertensionOS was selected for the FDA TEMPO pilot, which the company says is not approval (D3-06-F31).

### Evidence on remote ICU care

- D6-02-F12. Pereira AJ et al., "Effect of Tele-ICU on Clinical Outcomes of Critically Ill Patients: The TELESCOPE Randomized Clinical Trial", JAMA 2024;332(21):1798-1807, PMID 39382244.
  - **Design:** cluster randomised, 30 general ICUs in Brazil, 17,024 adults.
  - **Intervention:** daily remote multidisciplinary rounds led by a board-certified intensivist, plus monthly audit and feedback.
  - **Primary outcome:** mean ICU stay was 8.1 days with tele-ICU against 7.1 with usual care (change 8.2%, 95% CI -5.4% to 23.8%, P .24). No secondary or exploratory outcome differed significantly.
  - A summary adds that tele-visits happened on 68% of eligible patient-days and 74% of recommendations were accepted (ISGlobal, SNIPPET).
  - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22TELESCOPE%20Randomized%20Clinical%20Trial%22&resultType=core&format=json (2024). OPENED (abstract via Europe PMC).
- D6-02-F13. Lilly CM et al., JAMA 2011;305(21):2175-2183, PMID 21576622.
  - **Design:** prospective stepped-wedge, 6,290 adults in seven ICUs at one academic medical centre.
  - **Result:** hospital mortality 13.6% before and 11.8% during, adjusted OR 0.40. Adherence rose for DVT prevention (85% to 99%), stress-ulcer prevention (83% to 96%) and cardiovascular protection (80% to 99%).
  - The authors estimated that best-practice adherence and complications explained about 25% of the hospital mortality association and 30% of the ICU mortality association. Single centre.
  - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21576624%20OR%20(TITLE%3A%22Hospital%20mortality%2C%20length%20of%20stay%2C%20and%20preventable%20complications%22%20AND%20AUTH%3A%22Lilly%22)&resultType=core&format=json (2011). OPENED (abstract summary); adherence and attribution figures from news summaries, SNIPPET.
- D6-02-F14. Fusaro MV et al., "Evaluating Tele-ICU Implementation Based on Observed and Predicted ICU Mortality: A Systematic Review and Meta-Analysis", Crit Care Med 2019;47(4):501-507, PMID 30688718.
  - 13 before-after studies; pooled OR for ICU mortality 0.75 (95% CI 0.65-0.88).
  - Benefit only where observed mortality exceeded predicted before tele-ICU: OR 0.64 (0.52-0.77). Elsewhere OR 0.98 (0.81-1.18); interaction P .002.
  - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A30688718&resultType=core&format=json (2019). OPENED.
- D6-02-F15. Pscheidl T et al., "Telemedicine in adult intensive care: A systematic review of patient-relevant outcomes", PLOS Digital Health 2025;4(12):e0001126.
  - **Studies:** 26 studies (3 RCTs, 23 non-randomised), about 2,164,508 patients. No meta-analysis, because of heterogeneity.
  - **ICU mortality in RCTs:** Marx 2022 RR 2.29 (favouring usual care; high risk of bias); Spies 2023 RR 0.89 (0.54-1.46); Pereira 2024 RR 1.09 (0.94-1.26).
  - **Certainty:** very low for ICU mortality; moderate for TELESCOPE's ICU stay result.
  - Conclusion: effects on patient outcomes are "highly uncertain".
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12704867/ (2025). OPENED.
- D6-02-F16. Adams R et al., "Prospective, multi-site study of patient outcomes after implementation of the TREWS machine learning-based early warning system for sepsis", Nat Med 2022;28:1455-1460, PMID 35864252.
  - **Scale:** five hospitals, 590,736 patients monitored; 6,877 sepsis patients flagged before antibiotics.
  - **Result:** when a provider confirmed the alert within 3 hours, in-hospital mortality was lower, with an adjusted absolute reduction of 3.3% and a relative reduction of 18.7%. The reduction was 4.5% absolute in high-risk patients.
  - Observational. Several authors have ties to Bayesian Health.
  - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Prospective%2C%20multi-site%20study%20of%20patient%20outcomes%20after%20implementation%20of%20the%20TREWS%22&resultType=core&format=json (2022). OPENED (abstract summary); percentages from news summaries, SNIPPET.
- D6-02-F17. Alexander T et al., TN-STEMI programme, JAMA Cardiol 2017 (PMC5814984).
  - **Design:** quasi-experimental, before and after. 4 PCI hubs and 35 spokes; 2,420 patients (898 before, 1,522 after).
  - **Deaths:** in-hospital mortality 5.8% against 5.6% (adjusted OR 0.89, P .54). One-year mortality 17.6% against 14.2% (adjusted OR 0.76, 95% CI 0.58-0.98).
  - **Spokes:** angiography rose from 3.5% to 31.3% and PCI from 3.1% to 20.6%; spoke-to-hub transfers rose from 3.7% to 33.5%.
  - **IT:** ambulances could send ECGs, and a "STEMI Information Technology Kit" carried data across the network.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC5814984/ (2017). OPENED.

### Evidence on the camera features

- D6-02-F18. Chau V et al., "A Hierarchical Computer Vision Pipeline for Physiological Data Extraction from Bedside Monitors", arXiv 2511.23355 (28 Nov 2025). Senior authors include Louise Thwaites.
  - **Method:** YOLOv11 finds the monitor and vital-sign regions, a rectification step straightens the screen, and PaddleOCR reads it.
  - **Data:** 6,498 images from open datasets and real ICUs in Vietnam.
  - **Accuracy:** monitor detection mAP@50-95 99.5%; region localisation 91.5%; end-to-end extraction above 98.9% for heart rate, SpO2 and arterial BP.
  - Preprint, not peer reviewed. The number of monitor models and sites is not stated.
  - https://arxiv.org/abs/2511.23355 (2025). OPENED.
- D6-02-F19. Other monitor-reading work: a 2023 conference dataset of over 4,000 images of one monitor model (Mindray Beneview T8) for smartphone OCR in low-income settings. A cited study reports about 44% less recording time with OCR than manual entry. https://aminer.org/pub/6630621d01d2a3fbfccbee9b/using-semi-automated-annotation-and-optical-character-recognition-for-transcription-of-patient (date per source). SNIPPET.
- D6-02-F20. Smartphone jaundice from eye photos (abstracts via Europe PMC):
  - **Kazankov K et al., J Gastroenterol Hepatol 2023 (PMID 36574965):** 46 inpatients with decompensated cirrhosis, London. Scleral colour against serum bilirubin rho 0.90; change over time rho 0.77.
  - **Nixon-Hill M et al., PLOS Digit Health 2023 (PMID 37801433):** 66 cirrhosis patients. Sclera r 0.89, lower eyelid 0.86, forehead 0.79.
  - **Park JH et al., J Pers Med 2021 (PMID 34575705):** 130 patients, 1,460 photos, Korea. At a 1.5 mg/dL cut-off, sensitivity 80.0% and specificity 92.6%.
  - A search summary adds that visible jaundice is generally noticed above about 2-3 mg/dL, and that ambient light is a major confound.
  - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36574965%20OR%20EXT_ID%3A34575705%20OR%20EXT_ID%3A37801433&resultType=core&format=json (2021-2023). OPENED (abstracts). The 2-3 mg/dL line is SNIPPET.
- D6-02-F21. eICU Collaborative Research Database (PhysioNet):
  - **Contents:** 200,859 ICU unit encounters for 139,367 patients admitted in 2014-2015, across 335 units at 208 US hospitals.
  - **Origin:** data from Philips' eICU telehealth programme.
  - **Access:** credentialed, with a human-subjects course and a data use agreement.
  - https://physionet.org/content/eicu-crd/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6132188 (2018). SNIPPET.

- D6-02-F22. eICU-CRD Demo (PhysioNet): open access under the Open Data Commons Open Database License v1.0. "Over 2,500 unit stays" from 20 hospitals. Version 2.0.1, published 6 May 2021. https://physionet.org/content/eicu-crd-demo/ (2021). OPENED.

## Competitor map (OUR VIEW, built from the facts cited)

| Who | What they do | Who pays | Gap left |
|---|---|---|---|
| Cloudphysician (D6-02-F01 to F04) | 24/7 remote intensivists, cameras, AI notes and voice | Mostly private hospitals (an older report says 90%) | No published protocol-step product, no ward-to-home path, no price published |
| 10BedICU + CARE (D6-02-F05 to F07) | Donates ICU equipment and open-source software; state hubs | Donors pay the capital cost; states pay running costs | Depends on state staff; no outcome data; no protocol steps found |
| State hubs: Karnataka, Jharkhand, Nagaland, Meghalaya, J&K (D6-01-F13, D6-02-F08) | Medical-college specialists support district ICUs | State budgets (Karnataka Rs 30 Cr) | Specialist time at the hub; no automation found |
| Apollo, Fortis eICU (D6-02-F09) | Hospital-chain command centres | Own network | Serve their own and partner hospitals |
| Dozee MillionICU (D5-01-F07) | Contactless ward monitoring, step-down beds | Hospitals, development finance | Ward alerts with low specificity; no ICU protocol layer |
| Cadence, US (D2-06-F1, D5-01-F11) | Protocol-bound medicine changes at home | US health systems, Medicare | Not in India, not in hospital |

## So what for the idea (OUR VIEW)

- "Cameras plus AI plus remote specialists" is the incumbent's product, not a gap (D6-02-F01).
- The trials say watching does not help by itself (D6-02-F12, F15). Acting on time on standard steps does (D6-02-F13, F16, F17). The pitch should sell a closed loop with a time-to-action number, not more sensors.
- Two cheap, real technical wedges:
  - reading any monitor by camera (D6-02-F18), so mixed-brand government monitors feed the system without paid integrations
  - an open-source base (CARE, MIT licence, D6-02-F07) to build on rather than compete with
- Jaundice photos can show a trend to the specialist (D6-02-F20). They must not drive a decision.

## Not found and next checks

- Cloudphysician's price per bed or contract model; any peer-reviewed Cloudphysician outcome paper.
- 10BedICU outcome or bed-use data, and the cost per 10-bed unit.
- Whether CARE already reads monitors by camera or runs protocol steps.
- An Indian tele-ICU study with a control group.
- How the monitor-reading pipeline performs across monitor brands and in poor lighting.
