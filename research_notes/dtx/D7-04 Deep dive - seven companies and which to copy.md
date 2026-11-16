# D7-04 Deep dive: seven funded companies, how each one works, and which to copy (agent: claude-opus-5-5, 2026-11-16)

Why this note exists: after the D7 funded-players report, the user asked to expand on Athelas Home, Biofourmis, Virta, Counsel Health, Prana, Clara and DoseDr, and to pick the best one to copy. This note adds what the D7-01 to D7-03 notes did not have:
- the AIM-POWER randomised trial result for BiovitalsHF;
- Virta's 2-year, 5-year and independent VA data;
- how DoseDr actually ran;
- Counsel's step-by-step flow and pricing;
- what Prana and Clara say on their own pages;
- FDA-cleared insulin-titration software outside these funds.

Fact IDs D7-04-Fxx. OPENED = page read; SNIPPET = search summary only. Earlier IDs reused, not re-opened.

## Digest

1. **Correction to the D7 report: BiovitalsHF has positive randomised-trial evidence.** AIM-POWER randomised 122 patients with HFrEF at 21 US sites, platform versus usual care, for 90 days. Patients recorded weight daily and BP and heart rate twice daily, and the platform sent titration recommendations to site clinicians every 2 weeks. The heart-failure optimal-therapy score rose 1.72 ± 1.75 versus 0.44 ± 1.18 (P < 0.001). Published in Circ Heart Fail, Feb 2026. (D7-04-F01) It is the only randomised proof in the YC/a16z/Sequoia/Peak XV set that "device readings, then an algorithm drafts the dose step, then a clinician signs" changes prescribing. The company still never got FDA clearance and merged into CopilotIQ in 2024 (D7-03-F55, F57).
2. **Correction to "none of them publishes the rules".** BiovitalsHF says its steps follow published HFrEF guidelines (D7-04-F02). Outside these funds, FDA-cleared insulin-titration software exists with a randomised trial: Hygieia d-Nav cut HbA1c by 1.0% versus 0.3% in 181 adults over 6 months, with similar hypoglycaemia (D7-04-F12). DreaMed MODI was cleared in Sep 2026 (D7-04-F13). The real opening is narrower: no one has shipped protocol-bound dosing for warfarin or hydroxyurea that a non-specialist signs, built for low-resource settings.
3. **Virta's dosing rules are not in the paper.** The 2018 trial names only "rapid downward titration" of insulin and sulfonylureas. The thresholds are in a supplement not seen here. (D7-04-F03)
4. **Virta's own numbers fade over time, and an independent check found no difference.**
   - Retention: 83% at 1 year (D7-04-F04); about 74% at 2 years (26% dropped out; D7-04-F05).
   - Insulin use: down 62% at 2 years; sulfonylureas stopped entirely.
   - "Reversal" at 5 years: 20% or 32.5%, depending on the summary (SNIPPET; D7-04-F06).
   - A VA–Virta pilot found HbA1c fell about 0.8% at 2 years, but with no significant difference from usual care (D7-04-F07).
5. **Athelas Home works by computer vision on a drop of blood.** A finger-stick sample goes into a CLIA-waived analyser, and neural-network cell analysis gives WBC and neutrophil % (with ANC calculated) "in minutes". Use cases are clozapine, chemotherapy and immunosuppressants. (D7-04-F08) The page does not say how results reach the prescriber or the clozapine REMS, or what it costs (D7-04-F09). For a different finger-stick analyser, confirmatory venous testing is advised for results below threshold (D7-04-F10, SNIPPET).
6. **DoseDr had doctors make every dose change remotely.** The app logged glucose and insulin injections, suggested regimen changes, and providers adjusted doses "through the web portal". It ran in California and Louisiana in Mar 2016 (D7-04-F11). It was never FDA cleared and was out of business by Dec 2019 (SNIPPET). No reason for the closure was found.
7. **Counsel's flow:**
   - Free AI chat comes first.
   - A doctor joins with one click, usually in under 15 minutes, 8am to 9pm.
   - The doctor can order labs, prescribe (no controlled drugs) or refer, and the visit stays open for 7 days.
   - Price: $29 a visit or $300 a year.
   - Its own page says it is not a replacement for in-person chronic management. (D7-04-F14)
8. **Prana and Clara are early and say little about method.**
   - Prana pulls records through Fasten and wearable data through Junction, and escalates flagged "drift" to a physician network. No detection method, thresholds or prescription details are published (D7-04-F15).
   - Clara says a licensed clinician confirms every recommendation, prescription and lab order. It reports $12M pre-seed (D7-04-F16).

**Best one to copy:** BiovitalsHF's product shape, the only one with randomised proof. Run it as a service the way Virta does, not as stand-alone software, and use a point-of-care test step like Athelas Home's. Reasoning in the last section.

## The seven companies

### 1. Athelas Home (YC S16; Sequoia since 2016; now part of Commure)
- **The problem it solves:** people on clozapine, chemotherapy or immunosuppressants need frequent blood counts, because a low neutrophil count is dangerous. Usually that means a venous draw at a lab, then waiting for the result before the drug can be dispensed or continued.
- **How it works, step by step:**
  1. A care team member, or the patient at home, takes a finger-stick capillary sample.
  2. The sample runs on the Athelas Home analyser, an FDA-cleared, CLIA-waived device.
  3. Neural-network cell analysis and computer vision count the cells: quantitative WBC and neutrophil %, with ANC calculated.
  4. Results come back "in minutes" to an app and dashboard. (D7-04-F08 | https://www.commure.com/athelas-home | OPENED; method: https://clpmag.com/diagnostic-technologies/hematology-serology/fda-clears-ai-blood-analyzer-point-care-testing/ | SNIPPET)
- **Where it is used:** clinics, offices, home workflows, community and mobile outreach. FDA cleared it for point-of-care settings on 12 Feb 2026 (D7-03-F13).
- **Who decides:** the prescriber. The device gives the number, not the decision.
- **Evidence and scale (THEIR CLAIM):** 40,000+ patients and 1,000,000+ tests (F08). A 2021 open-label clozapine sub-study using the earlier Athelas One found patients less worried about blood draws and physicians more satisfied (SNIPPET, https://pubmed.ncbi.nlm.nih.gov/33878286/).
- **Not stated:** sample volume, price, billing codes, and how results reach the prescriber or the clozapine REMS. (D7-04-F09) Clozapine needs WBC and ANC results sent to REMS before dispensing (2022 award write-up, SNIPPET).
- **Caution:** for a different finger-stick analyser, a study advises confirmatory venous testing when a result falls below the accepted threshold. (D7-04-F10 | SNIPPET)
- **What to copy:** the test step. One finger-stick, a result in minutes at the clinic or home, and a defined confirm-by-lab rule for dangerous values. For warfarin this is a point-of-care INR meter (CoaguChek or Xprecia class, D5-02-F01), with an "INR above X or below Y, confirm by venous sample or call the MO" rule.
- **What it lacks:** the dose step. Athelas hands a number to a human with no rule. The user's product adds the rule.

### 2. Biofourmis BiovitalsHF (Sequoia India led the $35M Series B, 2019; merged into CopilotIQ, Oct 2024)
- **The problem it solves:** most people with HFrEF are not on full doses of the 4 drug classes that cut deaths, because titration needs many visits.
- **How it works, step by step (AIM-POWER protocol):**
  1. The patient records weight daily and BP and heart rate twice daily at home (wearable and connected devices; the 2021 release also mentions symptoms and labs).
  2. The platform combines the readings and runs titration logic based on published HFrEF guidelines.
  3. Every 2 weeks it sends medication recommendations (start or up-titrate) to the site clinician.
  4. The clinician decides; "final prescribing and titration decisions stayed with the sites". The patient is also prompted, and there is a patient-clinician messaging channel. (D7-04-F01 | https://scholars.duke.edu/publication/1696182 | OPENED; D7-04-F02 | https://biofourmis.com/news-insights/fdas-first-ever-device-designation-for-heart-failure-digital-medicine | OPENED)
- **Evidence:** AIM-POWER (NCT04191330), randomised 1:1, open-label, 122 patients at 21 US sites; mean age 61.6, 69% male, mean LVEF 29%, baseline optimal-therapy score 3.8 (range 0-8). Optimal-therapy score change at 90 days: 1.72 ± 1.75 versus 0.44 ± 1.18 with usual care, P < 0.001. Circ Heart Fail 2026;19:e013231. Secondary and safety results were not in the abstract seen. (F01) Earlier proof of concept: 282 patients, 90 days, better GDMT adherence and lower NT-proBNP (company-reported, D7-03-F56).
- **Regulatory:** FDA Breakthrough Device designation on 29 Jul 2021, which is not clearance. No clearance found (D7-03-F55).
- **Business result:** in 2024 Biofourmis merged into CopilotIQ, a home-care and RPM company, with new money from General Atlantic, Openspace and Bessemer; Peak XV was not in it (D7-03-F57). The titration software did not become a stand-alone business.
- **What to copy:** the exact product shape: home readings on a fixed schedule, guideline-based logic, a draft dose step every 2 weeks, clinician signs. Also its trial design: a randomised trial on a "therapy score" endpoint over 90 days is small enough for a pilot.
- **What to avoid:** selling software alone into clinics with no clearance and no one paying per patient. It proved the clinical effect but not the business.

### 3. Virta Health (Sequoia Capital Global Equities led the $65M Series D, Dec 2020)
- **The problem it solves:** type 2 diabetes treated by adding drugs for life. Virta aims to remove drugs through carbohydrate restriction, with the doctor cutting doses as glucose falls.
- **How it works, step by step:**
  1. The patient gets a cellular scale, a finger-stick glucose and ketone meter and, if hypertensive, a BP cuff.
  2. They log weight and ketones daily and glucose 1-3 times a day in the app.
  3. A health coach reads the ketone logs and adjusts diet, aiming for 0.5-3.0 mmol/L.
  4. A remote physician or nurse practitioner makes medicine changes "as indicated by the participant-reported biomarkers", with "rapid downward titration" of insulin and sulfonylureas to prevent hypoglycaemia.
  5. Metformin is stopped only for contraindication, intolerance or patient request.
  6. The numeric rules are in Supplementary Materials B, which was not read. (D7-04-F03 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6104272/ | OPENED)
- **Evidence (Virta-run, not randomised; 262 Virta patients versus 87 usual care):**
  - 1 year: HbA1c 7.6% to 6.3%; 40% of insulin users stopped insulin and the rest went from 105 to 54 units a day; sulfonylureas 23.7% to 0%; retention 83% (218 of 262); one hypoglycaemia event; no ketoacidosis. (F03, D7-04-F04)
  - 2 years: prescribed insulin down 62%, sulfonylureas down 100%, HbA1c down 12% from 7.7%; 26% had dropped out. (D7-04-F05 | https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00348/full | SNIPPET)
  - 5 years: summaries give 20% (consensus remission among completers) or 32.5% "reversal", and a 50% cut in insulin use. (D7-04-F06 | https://keto-mojo.com/research/5-year-carbohydrate-restricted-nutrition-type-2-diabetes/ | SNIPPET)
  - Independent check: in a VA–Virta pilot, HbA1c fell about 0.8% at 2 years, but the difference versus waitlisted usual care was not significant. (D7-04-F07 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12326886/ | SNIPPET)
- **Business model:** sold to employers, health plans and government payers, with "100% of its fees at risk" for enterprise clients (D7-03-F02). Maine's state employee plan routes weight-loss GLP-1 prescriptions through Virta from 1 Jul 2026 (D7-03-F05).
- **What to copy:**
  - the operating model: a coach handles behaviour, a remote clinician handles drugs, and the device data is the trigger for both;
  - safety-first titration: cut the risky drug fast, and add only slowly;
  - pricing tied to outcomes.
- **What to avoid:**
  - unpublished dose rules (nobody outside Virta can audit them);
  - an intervention (ketogenic diet plus ketone strips) that is expensive and fades;
  - relying on Virta's own non-randomised numbers.

### 4. Counsel Health (a16z led the seed and co-led the $25M Series A, Oct 2025; Oura agreed to buy it, 10 Nov 2026)
- **The problem it solves:** getting to a doctor for routine problems is slow and expensive.
- **How it works, step by step:**
  1. The patient chats with Counsel AI for free. It gathers history, gives initial guidance and a next step (home care, see a doctor, or urgent care).
  2. A board-certified physician joins the chat with one click, usually in under 15 minutes (8am-9pm, 7 days), with no video or appointment.
  3. The doctor orders labs, prescribes (no controlled substances) or refers.
  4. The doctor follows up, and the visit stays open for 7 days. With consent, the AI reads medical records and remembers past chats. (D7-04-F14 | https://www.counselhealth.com | OPENED)
- **Price:** AI is free, $29 per doctor visit, or $300 a year unlimited; no insurance needed. It is also sold to health plans, health systems and employers (F14).
- **Conditions:** weight management, birth control, hair loss, skin, acne, herpes, and labs and referrals. Hypertension, cholesterol and obesity are being added during 2026 (D7-02-F03). Its own page says it is "not a replacement" for an in-person PCP for chronic management (F14).
- **Oura deal:** with permission, Counsel doctors will see Oura ring data and past chats (D7-02-F04). The price is reported at $625M; it is not on Oura's page.
- **What to copy:** the front door. AI handles intake and triage for free, and a human clinician joins in minutes for a flat fee. In India: a WhatsApp or voice front end where the AI collects the INR, symptoms and bleeding questions, and a nurse or MO joins only when the protocol says so.
- **What it lacks:** a disease protocol. Every decision is the doctor's judgement, so it scales only as fast as doctor time.

### 5. Prana (YC Winter 2026)
- **How it works:** medical records come in through Fasten and wearable biometrics through Junction. A background AI watches for "clinical drift", such as BP or glucose creeping up over weeks, and escalates flagged risks to a physician network ("Doctor-in-the-Loop"). The YC listing says it explains labs and manages prescriptions. (D7-04-F15 | https://www.ycombinator.com/launches/PPg-prana-an-ai-doctor-that-monitors-you-24-7 | OPENED)
- **Not published:** detection method, thresholds, validation, prescription rules, licensing. Beta only; seeking self-insured employer pilots; about $500K raised (SNIPPET).
- **What to copy:** the framing ("drift between visits") and the plumbing choice of buying data integration rather than building it. India's equivalent is ABDM/ABHA records plus a few device APIs.
- **What to avoid:** a generalist "watch everything" monitor with no stated rule. It cannot show safety, and the doctor network becomes the bottleneck.

### 6. Clara (YC Spring 2026)
- **How it works:** imports labs, prescriptions and wearables (Oura, Fitbit, Peloton) into one history. It links biomarkers to medications and goals, adapts the care plan, and runs refills end to end. A licensed clinician in the patient's state confirms every recommendation, prescription and lab order; AI output is "informational only". Condition pages include type 2 diabetes, hypothyroidism, menopause and weight loss. LegitScript certified; $12M pre-seed (THEIR CLAIM). Pricing and states are not shown. (D7-04-F16 | https://askclara.com | OPENED)
- **What to copy:** the compliance stance. Every AI output is a draft until a licensed clinician confirms it, and that is stated publicly. In India, a medical officer's sign-off on each dose step plays the same role under the Telemedicine Practice Guidelines (see D2-04).
- **What to avoid:** breadth before depth. It covers many conditions, and no single disease has a published protocol or outcome.

### 7. DoseDr (YC Winter 2016; out of business Dec 2019)
- **How it worked:** a mobile app tracked glucose readings and insulin injections and suggested regimen changes to patients. Providers watched a web portal and made dose adjustments remotely as needed. Free to patients; patients could invite their own doctor. It ran in California and Louisiana in Mar 2016, with New York, Florida and Illinois planned. Its one published anecdote: the first patient avoided an ICU stay of about $13,000 when the provider spotted high sugars and caught an infection early. (D7-04-F11 | https://ycombinator.com/blog/dosedr-yc-w16-helps-people-with-diabetes-control-their-treatment-in-real-time | 2016-03-15 | OPENED)
- **End:** never FDA cleared; out of business 1 Dec 2019 per PitchBook (SNIPPET, https://healthcarediscovery.ai/companies/dosedr/). No stated reason found.
- **Likely reasons, OUR INFERENCE, not sourced:** free to patients with no payer, so clinician time was a pure cost; state-by-state licensing slowed expansion; and no cleared algorithm, so every change needed a doctor and nothing scaled.
- **What to learn:** the loop works clinically for an individual patient, but not as a free consumer app. Sell the loop to whoever owns the outcome (a hospital, programme or insurer), and let a cleared or protocol-bound rule carry most changes so clinician time per patient falls.

## Outside these funds: dose software that already has proof

- **Hygieia d-Nav (insulin):** 510(k) cleared, 2017. In a Lancet randomised trial of 181 adults with type 2 diabetes, HbA1c fell 1.0% versus 0.3% at 6 months (p < 0.0001), with similar hypoglycaemia; 62% versus 33% reached HbA1c ≤8%. (D7-04-F12 | https://www.mobihealthnews.com/news/hygieias-cloud-based-insulin-titration-app-wins-510k-clearance | SNIPPET)
- **DreaMed MODI:** 510(k) cleared, Sep 2026, for an insulin titration algorithm using CGM and insulin data in adults with type 2 diabetes; trial ongoing. (D7-04-F13 | https://www.healio.com/news/endocrinology/20260928/fda-clears-modi-the-first-insulin-dosing-app-for-adults-with-type-2-diabetes | SNIPPET)
- **Insulin Algorithms (2017, Class II) and Glytec Glucommander** exist, with company or retrospective evidence only (SNIPPET).
- **Warfarin:** clinic dosing software (DAWN AC, PARMA) and point-of-care INR meters exist, serving well-staffed clinics (D5-02-F01, F11). Machine dosing at scale is proven: a randomised trial of 13,219 patients (D5-02 digest point 3).
- **Why this matters:** regulators already clear rule-based dose software. The user's claim should not be "nobody has dose rules". It should be "nobody runs a protocol-bound dose loop for warfarin or hydroxyurea that a non-specialist can sign, built for a district hospital with no anticoagulation clinic".

## Which one to copy

| | Product shape | Evidence | Business that worked | Fit to the warfarin loop |
|---|---|---|---|---|
| **BiovitalsHF** | Home readings, then guideline logic, a draft dose step every 2 weeks, clinician signs | **Randomised trial, positive** (AIM-POWER) | No: never cleared, merged | **Closest: it is the same loop** |
| **Virta** | Home readings, then a remote clinician changes drugs; a coach handles behaviour | Non-randomised, own data; independent VA pilot not significant | **Yes**: fees at risk, payers, state plan | Operating and pricing model |
| **Athelas Home** | Finger-stick test, result in minutes, prescriber | Scale claims (1M tests) | Yes, inside Commure | The test step (INR meter) |
| **Counsel** | AI front door, doctor joins in 15 min | None published | Yes: $29/visit, acquired | Front end for intake |
| **Prana, Clara** | Generalist AI doctor, clinician confirms | None | Too early | Framing only |
| **DoseDr** | App, clinician adjusts in portal | One anecdote | No: closed 2019 | What not to do |

**Pick: copy BiovitalsHF's loop.** It is the only funded product built the way the user's warfarin loop is built: scheduled home readings, a rule that drafts the dose step, and a clinician who signs. It is also the only one with a randomised trial showing the shape changes prescribing. Then fix the two reasons it failed as a business, using the others:
1. **Run it as a service with someone paying per patient, as Virta does,** not as software sold to clinics. The buyer is a district hospital, a state RHD or sickle-cell programme, or PM-JAY, and pricing is tied to time in therapeutic range or admissions avoided.
2. **Use Athelas's point-of-care test step** so a reading exists at all. For warfarin that is a finger-stick INR at a PHC, a CHC or an ASHA visit, with a "confirm by venous test or call the MO" rule for values out of range.
3. **Publish the protocol** (Virta and Twin do not) and keep the sign-off with a nurse or medical officer, as Clara does with its licensed clinicians. Use Counsel-style AI intake only as the front end.
4. **Copy AIM-POWER's trial design for the pilot:** randomised, about 120 patients, 90 days, one simple endpoint. For warfarin the endpoint is time in therapeutic range, which was 13% at the rural Chhattisgarh site (D5-01-F03).

## Sources

OPENED:
- https://scholars.duke.edu/publication/1696182 (AIM-POWER results, F01)
- https://biofourmis.com/news-insights/fdas-first-ever-device-designation-for-heart-failure-digital-medicine (F02)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6104272/ (Virta 1-year, F03, F04)
- https://www.commure.com/athelas-home (F08, F09)
- https://ycombinator.com/blog/dosedr-yc-w16-helps-people-with-diabetes-control-their-treatment-in-real-time (F11)
- https://www.counselhealth.com (F14)
- https://www.ycombinator.com/launches/PPg-prana-an-ai-doctor-that-monitors-you-24-7 (F15)
- https://askclara.com (F16)

SNIPPET:
- Virta 2-year: https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00348/full (F05)
- Virta 5-year: https://keto-mojo.com/research/5-year-carbohydrate-restricted-nutrition-type-2-diabetes/ (F06)
- VA–Virta pilot: https://pmc.ncbi.nlm.nih.gov/articles/PMC12326886/ (F07)
- Athelas method: https://clpmag.com/diagnostic-technologies/hematology-serology/fda-clears-ai-blood-analyzer-point-care-testing/ ; clozapine sub-study: https://pubmed.ncbi.nlm.nih.gov/33878286/ (F08, F10)
- DoseDr closure: https://healthcarediscovery.ai/companies/dosedr/ (F11)
- d-Nav: https://www.mobihealthnews.com/news/hygieias-cloud-based-insulin-titration-app-wins-510k-clearance (F12)
- MODI: https://www.healio.com/news/endocrinology/20260928/fda-clears-modi-the-first-insulin-dosing-app-for-adults-with-type-2-diabetes (F13)
- AIM-POWER registry: https://www.centerwatch.com/clinical-trials/listings/NCT04191330/artificial-intelligence-mobile-health-trial-of-a-digital-platform-to-optimize-gdmt-using-wearable-sensors

Reused: D7-02-F01 to F04; D7-03-F01, F02, F05, F13, F55 to F57; D5-01-F03; D5-02-F01, F11; D2-04.
