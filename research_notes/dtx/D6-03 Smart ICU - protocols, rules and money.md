# D6-03 Smart ICU: protocol packs, rules and money (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: the improved concept runs written treatment protocols inside district ICUs, approved by a remote specialist. This note collects the protocol sources for the first packs, the rules that apply (software class, telemedicine, cameras and data), and how the service could be paid for.

Fact IDs are D6-03-Fxx. OPENED means the page, PDF or abstract was read; SNIPPET means only a search summary was seen. Earlier IDs are reused: D2-04-F03 to F06 (CDSCO software classes), D2-04-F17 to F19 (telemedicine, standing orders, DPDP Rules), D5-01-F18 (PMJAY dues), D6-01-F02 (CCB budget), D6-02-F17 (TN-STEMI).

## Digest

1. **Snakebite is the cleanest first protocol.** The government's own guideline (MoHFW STG, Jun 2016) is already a timed, rule-based loop:
   - clotting test every hour for 3 hours, then 6-hourly for 24 hours
   - repeat antivenom if the blood still does not clot at 6 hours, or bleeding continues 1 hour after the first 10 vials
   - stop rules for the neostigmine trial after 3 doses
   - referral criteria by antivenom, ventilator and dialysis availability (D6-03-F01)
2. **Pesticide (organophosphate) poisoning has trial proof that a stepped protocol saves lives.** In a Bangladesh RCT of 156 patients, rapidly increasing atropine doses plus an infusion reached stabilisation in about 24 minutes against 152. Deaths were 8% against 22.5%, and atropine toxicity 12.0% against 28.4% (D6-03-F02).
3. **Sepsis and heart attack have standard bundles and pathways.**
   - The sepsis hour-1 bundle: lactate, cultures, antibiotics, 30 mL/kg fluid for low BP or lactate of 4 or more, pressors for a mean BP of 65 or more (D6-03-F03).
   - Tamil Nadu's STEMI hub-and-spoke shows the heart-attack pathway works in Indian district settings (D6-02-F17).
4. **Software class.** ICU conditions are "critical" in the CDSCO matrix.
   - Software that proposes the next step reads as "drive clinical management" x critical = Class C.
   - If it adjusts a pump directly, it reads as "treatment" = Class D.
   - A ward early-warning score that only informs reads as Class B. (OUR READING of D2-04-F03, F04; CDSCO confirms the class on review.)
5. **Liability stays local.** Under the 2020 Telemedicine Practice Guidelines, the doctor asking for a teleconsultation "remains the treating RMP and shall be responsible for treatment" (D6-03-F05, SNIPPET). The district doctor stays the doctor of record; the remote specialist advises.
6. **Cameras in ICUs are contested, and the state is pushing them for audit.** Haryana ordered live CCTV of PMJAY patients in ICUs and HDUs, shared with the State Health Agency (Jan 2026). The IMA objected on privacy and consent (D6-03-F06). In 2021 the Supreme Court declined to order CCTV in every ward, citing patient privacy (D6-03-F07).
7. **Money.**
   - Public hospitals keep PMJAY claim revenue and may spend it on services and staff incentives: CAG's indicative share for staff is 15%; Uttarakhand allows up to 25% (D6-03-F09).
   - PMJAY pays per ICU day, about Rs 8,500-10,350 in one HBP 2022 package schedule (D6-03-F08, SNIPPET).
   - The CCB guideline itself budgets "teleconsultation" (D6-01-F02).

## Findings

### Protocol sources for the first packs

- D6-03-F01. Directorate General of Health Services, MoHFW, "Standard Treatment Guidelines: Snakebite", June 2016 (technical support NHSRC). List of recommendations:
  - **Clotting test:** "If clotted, the test should be carried out every 1 h from admission for three hours and then 6 hourly for 24 hours. In case test is non-clotting, repeat 6 hour after administration of loading dose of ASV."
  - **Bleeding:** if there is spontaneous abnormal bleeding beyond 20 minutes from the bite, "ASV is to be started, do NOT wait for 20 WBCT report". "REPEAT dose of ASV should also be given if abnormal bleeding does not stop one hour after completion of 1st 10 vials."
  - **Neurotoxic bites:** "ASV 10 vials stat as infusion over 30 minutes followed by 2nd dose of 10 vials if no improvement within 1st hour."
  - **Atropine-neostigmine (AN) trial:** stop rules include side effects (fasciculations or bradycardia) and "no improvement after 3 doses", then calcium gluconate for a probable krait bite.
  - **Upper limit:** "If 30 vials of ASV have been administered reconsider whether continued administration of ASV is serving any purpose."
  - **Repeat-dose criteria:** "Persistence or recurrence of blood coagulability [sic] after 6 h or of bleeding after 1-2 h and deteriorating neurotoxic or cardiovascular signs after 1-2 hours."
  - **Other rules:** children and pregnant women get the same dose as adults; no skin test.
  - **Referral:** referral from basic facilities "depending on availability of ASV, ventilation facility, hemodialysis facility and infrastructure".
  - https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf (2016). OPENED (text extracted from the PDF).
- D6-03-F02. Abedin MJ et al., "Open-Label Randomized Clinical Trial of Atropine Bolus Injection Versus Incremental Boluses Plus Infusion for Organophosphate Poisoning in Bangladesh", J Med Toxicol 2012;8(2):108-117 (PMC3550249). Chittagong Medical College Hospital.
  - **Arms:** 156 patients; 81 got conventional bolus atropine and 75 got rapidly increasing doses plus infusion.
  - **Time to atropinisation:** mean 151.74 against 23.90 minutes (P below 0.001).
  - **Toxicity and complications:** atropine toxicity 28.4% against 12.0%; intermediate syndrome 13.6% against 4%.
  - **Deaths:** 18/80 (22.5%) against 6/75 (8.0%), P below 0.05. Confirmed as mortality in the paper. One patient in group A left against advice, hence 80; the Discussion's 22.2% matches 18/81.
  - **The stepped regimen (group B):** start 1.8-3.0 mg IV by severity. If needed, double the previous dose 5 minutes later, and repeat every 5 minutes until signs of atropinisation. Then an infusion at 10% of the total loading dose per hour, reviewed every 15 minutes and raised by 0.6 mg/h if signs are absent. After toxicity, restart at 70-80% of the previous rate. Stop after at least 24 hours once cholinergic features resolve.
  - **Context:** a 2004 comparison found textbook regimens took 8 to 1,380 minutes to give the average required 23.4 mg (search summary only).
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC3550249/ (2012). OPENED (claims check, 16 Nov 2026). Context: https://pmc.ncbi.nlm.nih.gov/articles/PMC4057538 (2014). SNIPPET.
- D6-03-F03. Surviving Sepsis Campaign hour-1 bundle (Levy et al. 2018; SCCM page, current version effective 10 Oct 2019):
  - measure lactate, and remeasure if above 2 mmol/L
  - blood cultures before antibiotics, without delaying antibiotics
  - broad-spectrum antibiotics
  - 30 mL/kg crystalloid for hypotension or lactate of 4 mmol/L or more
  - vasopressors if hypotension persists, for a mean arterial pressure of 65 mm Hg or more
  - SCCM calls the bundle "a quality improvement opportunity".
  - https://sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients ; https://quality.allianthealth.org/wp-content/uploads/2021/07/Surviving-Sepsis-Campaign-Hour-1-Bundle.pdf (2018-2019). SNIPPET.
- D6-03-F04. Eclampsia: Indian guidelines for skilled birth attendants recommend giving magnesium sulphate for severe pre-eclampsia and eclampsia before referral. A study of Indian facilities calls the policy environment "supportive" and quotes national guidelines that the drug should be available at sub-centre level. The exact national regimen and monitoring thresholds were NOT OPENED. https://www.rhsupplies.org/uploads/tx_rhscpublications/Barua.IJGO.2011.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6020005 (2011; date per source). SNIPPET.
- Heart attack (STEMI): the Tamil Nadu programme used clot-busting at spokes far from a hub, then transfer for angiography within 3-24 hours (D6-02-F17). An ICMR standard treatment workflow for STEMI was NOT OPENED.

### Rules

- CDSCO software classes (from D2-04, OPENED there):
  - The class depends on intended use (D2-04-F02).
  - The matrix (D2-04-F03): critical x "treatment or diagnosis" = D; critical x "drive clinical management" = C; critical x "inform clinical management" = B.
  - "Critical" means "life threatening..., requires major therapeutic interventions, and/or time critical" and is "intended for use by specialized trained users" (D2-04-F05).
  - "Treatment or diagnosis" includes acting "by connecting to other medical devices" (D2-04-F04).
  - Software that controls a connected device takes the device's class (D2-04-F08).
  - OUR READING: an ICU step proposal approved by a clinician is Class C. Never let the software drive an infusion pump directly; that would move it toward Class D. A ward score that only informs is Class B.
- D6-03-F05. Telemedicine Practice Guidelines 2020 (MoHFW and the Board of Governors, 25 Mar 2020), as reproduced by IADVL: the "RMP asking for teleconsultation remains the treating RMP and shall be responsible for treatment of the patient". The guidelines cover consultation "with another RMP or another specialist" for a patient under the doctor's care. Tele-assisted surgery is excluded. https://iadvl-files-latest.s3.ap-south-1.amazonaws.com/academy-publications/Academy-Publications-23.pdf (2020). SNIPPET. The official PDFs again failed (404 and 504 on 16 Nov 2026), as in D2-04-F17.
  - Related: AI platforms "cannot counsel patients or prescribe medicines" but may "assist and support the RMP" (D2-04-F17). No Indian rule lets a nurse change a dose on a standing order (D2-04-F18, NOT FOUND).
- D6-03-F06. Haryana Health Protection Authority directive, reported 9 Jan 2026.
  - **Requirement:** all empanelled hospitals must keep AB-PMJAY patients in ICUs and HDUs, including ventilated patients, under "continuous live CCTV surveillance" and share real-time feeds with the State Health Agency, "for verification, monitoring, audit, and claims processing". Penalties up to de-empanelment.
  - **Objections:** the IMA warned of exposed bodies and procedures being filmed; a former IMA Haryana president called live streaming "against NABH guidelines"; doctors noted ICU patients rarely can consent.
  - **Later clarification:** cameras will not face patients (devdiscourse, SNIPPET).
  - https://medicaldialogues.in/amp/news/health/hospital-diagnostics/haryana-mandates-live-cctv-surveillance-of-icus-for-ayushman-bharat-patients-162359 (2026). OPENED.
- D6-03-F07. Supreme Court, 2021: declined to direct CCTV in every hospital ward ("Hospitals are not police stations"), noting privacy concerns for patients being operated on. https://medicaldialogues.in/news/health/hospital-diagnostics/hospitals-are-not-police-stations-cant-direct-for-cctv-cameras-in-every-ward-supreme-court-82981 (2021). SNIPPET.
- DPDP Rules 2025 were published 13 Nov 2025. Most duties (Rules 3, 5-16) start 18 months after publication, which is about May 2027 (OUR ARITHMETIC from D2-04-F19). How DPDP applies to ICU video was NOT FOUND.

### Money

- D6-03-F08. PMJAY ward rates:
  - **The 2021 revision (HBP 2.2):** ICU-with-ventilator rates rose 100%, ICU-without-ventilator 136%, HDU 22% and routine ward 17% (PIB, Oct 2021).
  - **One HBP 2022 schedule (general medicine, infectious disease package):** routine ward Rs 2,100 or 2,300; HDU Rs 3,300 or 3,800; ICU without ventilator Rs 8,500 or 8,800; ICU with ventilator Rs 9,000 or 10,350 a day, varying by city tier.
  - Package-specific; the official NHA master was not opened.
  - https://pib.gov.in/PressReleasePage.aspx?PRID=1761175 (2021); https://www.scribd.com/document/670510137/HBP-2022-003 (2022, unofficial copy). SNIPPET.
- D6-03-F09. PMJAY claim revenue in public hospitals:
  - All public hospitals in PMJAY states are deemed empanelled.
  - Claim revenue is credited to the hospital or its Rogi Kalyan Samiti account.
  - CAG's audit describes this as a chance "to mobilise and independently manage revenues", with an indicative staff-incentive share of 15%.
  - Uttarakhand's guideline allows up to 25% for staff incentives, the rest for infrastructure and critical gaps.
  - https://cag.gov.in/uploads/download_audit_report/2023/09_Chapter-V-064d22bab412c53.02505839.pdf (2023); https://sha.uk.gov.in/ScannedDocs/WebSite/Uploads/CLAIM_ADJ/guidelines-for-use-of-claim-amount-public-hospitals-under-pmrssm.pdf (date per source). SNIPPET.
- Other money facts already on file:
  - CCB recurring budget with "teleconsultation" in the non-HR line, Rs 26.6-50 lakh a year, and specialists at Rs 60-84 lakh a year per block (D6-01-F02).
  - Karnataka's Rs 30 Cr tele-ICU budget (D6-01-F13).
  - 2016 eICU price of $10-30 a patient a day (D6-01-F09).
  - Development finance for Dozee's MillionICU (D5-01-F07).
  - Half of Haryana's empanelled private hospitals paused PMJAY in Aug 2025 over unpaid dues (D5-01-F18).

## So what for the idea (OUR VIEW)

- **First packs:** snakebite (D6-03-F01), organophosphate poisoning (D6-03-F02), sepsis (D6-03-F03) and STEMI (D6-02-F17). Each has a written source with timed checks, so the engine can run it as YAML, the way D2-01 runs the BP sheet. Eclampsia comes next, once the national regimen is read.
- **Product rule for the regulator:** propose, never actuate. Every step needs a clinician's tap; the software never drives a pump (D2-04-F04, F08).
- **Camera rule:** audit-grade evidence without streaming bodies. Cameras face the monitor and bed area, faces are blurred on the device, and only events and frames that support a proposal are stored. This answers both the Haryana audit need and the IMA's objection (D6-03-F06, F07).
- **Pitch the money as a staffing substitute, not an add-on:**
  - Price to test (ASSUMPTION): Rs 15,000 per ICU or HDU bed a month.
  - A 50-bed block has 10 ICU beds plus a step-down unit (D6-01-F01). At 16 monitored beds that is Rs 28.8 lakh a year (OUR ARITHMETIC). It compares with Rs 60 lakh a year budgeted for five specialists (D6-01-F02).
  - Per patient-day at full occupancy that is about Rs 500, below the 2016 eICU price of $10-30 (OUR ARITHMETIC).
  - PMJAY ICU days earned by a working ICU are the hospital's own money to spend (D6-03-F08, F09).

## Not found and next checks

- The official NHA HBP 2022 master rates for ICU and HDU days.
- The national MgSO4 regimen and monitoring thresholds from the MoHFW maternal health guideline.
- The ICMR standard treatment workflows for STEMI and sepsis.
- The official text of the Telemedicine Practice Guidelines (blocked again).
- Whether DPDP treats ICU video as needing explicit consent, and who consents for an unconscious patient.
- A CDSCO-licensed ICU decision-support product in India, as a precedent.
