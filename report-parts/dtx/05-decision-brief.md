## Decision brief: what to build tonight

*Written 13 Nov 2026, about 10 PM, from the six Round 1 research notes. Updated about 10:30 PM after the clinical claims check: 53 claims re-opened at source, 48 confirmed, 5 tightened in wording, none wrong (`research_notes\dtx\D3-01 Claims check - clinical evidence.md`). The India and market facts were checked next (about 45 claims: 29 confirmed, 7 corrected, 5 contested, 3 not found; `D3-02 Claims check - India and market.md`), and the corrections that touch this brief are applied below.*

![The difference between monitoring and a therapy loop](adaptive-care-pictures/00-the-loop.png)

*Diagram: monitoring stops at the reading; a therapy loop sends the reading back as a changed treatment.*

### What the evidence says

1. **Programmes that change the medicine from home readings work.**
   - UK trial TASMIN-SR (552 patients): patients adjusting their own dose by a set plan lowered systolic pressure 9.2 mmHg more than usual care at 12 months (D1-01-F02).
   - US trial HyperLink (450 patients): pharmacists adjusting drugs from home readings got 57.2% controlled against 30.0% (D1-01-F04).
   - Rural China (33,995 people, 326 villages): village health workers starting and stepping doses by protocol got 57.0% under 130/80 against 19.9% at 18 months. After 4 years, cardiovascular events were lower (hazard ratio 0.75 at age 60 and over, 0.64 under 60), with no difference in falls, low pressure or kidney outcomes (D1-01-F09, D1-01-F38). The programme also gave free or cheaper medicines and paid village doctors for results, so the protocol is not the only cause.
2. **Monitoring and reminders alone do not.**
   - Self-monitoring alone, pooled across trials: 1.0 mmHg, no effect. With intensive support (dose changes by doctors, pharmacists or patients, plus education or counselling): 6.1 mmHg (D1-01-F05).
   - A reminder app (MedISAFE-BP, 411 patients): 0.5 mmHg, not significant (D1-01-F06).
   - Tuberculosis pillbox trackers (ASCENT, 23,483 patients): no improvement in outcomes (D1-02-F59).
   - An independent US review (Peterson Health Technology Institute, October 2024) found that only programmes which adjust medication give clinically meaningful falls in pressure (D1-01-F39).
3. **The pattern repeats in other diseases.**
   - Warfarin: patients who test at home and change their own dose had fewer clots (risk ratio 0.47) and fewer deaths (0.55). Those who tested at home and phoned the clinic had no fewer deaths (0.94). Each group was compared with usual care, not with the other (D1-02-F05).
   - Insulin in type 2 diabetes: a device that computes the next dose cut HbA1c by 1.0 point against 0.3 (D1-01-F13).
   - Heart failure: stepping drugs up fast after discharge, with four clinic visits in two months, cut death or readmission at 180 days to an adjusted 15.2% against 23.3%, with more side effects reported (41% against 29%) (D1-01-F27). Two large trials of telemonitoring that left treatment to the usual clinicians or to nurse protocols found no benefit (D1-01-F32, D1-01-F33).
4. **India's gap is the dose change and the return visit.**
   - Government hypertension programme, 21,895 patients: 51% came back for follow-up. Among those who did, control rose from 26.3% to 59.8%, with no comparison group (D1-03-F10).
   - Tamil Nadu household survey, 6,856 adults: over 95% of diagnosed patients are on treatment, yet control rates were 9.8% for diabetes and 35.4% for hypertension (D1-03-F09). The claims check notes that the paper's summary does not state the denominator for the two control figures.
   - Rural community health centres had 79.9% of required posts in four specialities unfilled, as of March 2023 (D1-03-F16). A primary-care consultation lasted about 2 minutes in studies from 2013-2015 (D1-03-F24).
5. **Nobody in India was found running a dose-change loop from home readings.** The diabetes programmes sell a sensor plus doctor and coach (D1-04-F02, D1-04-F03, D1-04-F04, D1-04-F05, D1-04-F06, D1-04-F07). The protocol model in the government's open-source app stores a drug list and follow-up days, and no step logic was found in it (D1-06-F40). Phable, the best-known home blood-pressure app, shut in February 2023 (D1-04-F23).
6. **Why earlier companies died.** Pear Therapeutics sold its assets for about US$6 million against US$130 million of liabilities (D1-02-F42). Akili earned US$523,000 from prescription sales in 2023 (D1-02-F44). Teva withdrew its sensor inhaler in June 2024 (D1-02-F41). They sold apps or sensors without a payer, and users leave fast: across 93 mental-health apps, the median share still using the app at day 30 was 3.3% (D1-02-F26).

### The caution to carry

An Indian trial already tested software for clinicians and found nothing. mWellcare (40 community health centres, 3,698 patients) gave nurses and doctors a decision-support app during visits; the difference from well-run usual care was 0.98 mmHg, not significant (D1-01-F46). So the value must come from changing the dose between visits and reaching the half who never return. A prompt at a visit that was happening anyway adds nothing.

### Scores

Two gates first: the product must change the therapy itself from device or biomarker feedback, and it must be buildable honestly tonight. Then six axes, scored 1 to 5. Weights: proof 25, market 20, feasibility tonight 20, gap 15, deep-tech 10, low risk 10.

| Option | Proof | Market | Tonight | Gap | Deep-tech | Low risk | Score |
|---|---|---|---|---|---|---|---|
| Home blood-pressure step loop | 5 | 4 | 5 | 4 | 3 | 4 | **4.35** |
| Insulin dose guidance, type 2 diabetes | 4 | 4 | 3 | 3 | 3 | 2 | 3.35 |
| Adaptive home rehabilitation (camera and pulse) | 3 | 3 | 5 | 2 | 3 | 4 | 3.35 |
| Heart-failure dose loop | 4 | 3 | 2 | 4 | 3 | 2 | 3.10 |
| Breathing plan with inhaler sensor and air quality | 2 | 3 | 4 | 3 | 4 | 3 | 3.05 |
| Warfarin self-dosing | 5 | 2 | 2 | 3 | 2 | 2 | 2.90 |
| Weight-loss injection dose companion | 2 | 4 | 3 | 2 | 2 | 3 | 2.70 |

The scores are the coordinator's judgement (OUR ESTIMATE), with the reasons in part I and in `research_notes\dtx\DT1-triage.md`.

![Weighted scores of the seven options](adaptive-care-pictures/24-option-scores.png)

*Chart: the seven options on the same six tests. OUR ESTIMATE.*

### The three to weigh

**1. Home blood-pressure step loop (recommended).**
- *What it is.* A home cuff reading goes into an engine that runs India's own published step protocol: amlodipine 5 mg, then 10 mg, then add telmisartan 40 mg, then 80 mg, then add chlorthalidone 12.5 mg, with a re-check every 30 days, lab values checked before telmisartan is raised, and referral rules for very high readings, abnormal lab values and pregnancy, including women of childbearing age not on effective contraception; the sheet covers adults over 30 (Gujarat protocol, D1-06-F14). The engine proposes the next step. A doctor approves in one tap. The patient gets the change in their own language.
- *Why.* The strongest proof of any option, including deaths and strokes avoided at scale by non-physicians. The largest patient pool: 35.5% of Indian adults aged 20 and over have high blood pressure (D1-03-F01). The exact Indian protocol text is public. No Indian service was found.
- *Noon demo.* A live reading, the proposal, the approval, the patient message.
- *Honest test results.* Every branch of two published protocols passes. A simulated cohort built on the programme's own control-by-step figures from 159,292 patients (D1-06-F04), labelled as a simulation. Reading-quality tests on teammates.
- *Main risk.* It can look like "just rules", and the mWellcare result will be raised. The answer: the rules are what the trials show works; nobody runs them at home; the hard parts are trusting a home reading, checking the pills were taken before raising a dose, and proving safety. Who pays is the open business question.

**2. Insulin dose guidance for type 2 diabetes.** Strong trials and pharma interest. But no open type 2 simulator exists (D1-06-F30), so tonight's test would be thin, and low blood sugar is a real hazard. Sanofi already has a dosing app (D1-04-F09). Best shown as the second protocol on the same engine, tested on paper.

**3. Adaptive home rehabilitation.** The easiest demo. But software rehabilitation only matches in-person care and does not beat usual care (D1-02-F07, D1-02-F54), and Lupin says it already holds an Indian Class C device licence for cardiac rehabilitation (D1-04-F15).

*Also weighed.* Heart failure has strong outcome proof and fits "far from a specialist" best, but it needs lab values, so it cannot be tested honestly tonight; it is the later protocol for the same engine. The breathing plan has the most hardware and the best open data, but the dose change that works in asthma needs no sensor and sensor inhalers failed commercially. Warfarin has the best proof and a small market. Weight-loss injection support is a hot market with no outcome evidence yet and three Indian players already in.

### Recommendation

Build option 1. Make the engine load any protocol as data, so insulin becomes "same loop, new protocol" and heart failure is the expansion.

- **Software:** the protocol engine, the patient chat, the doctor's approval screen, the test harness.
- **Hardware:** read the cuff (a phone photo of any cuff's screen, with the person confirming the digits; typed entry as fallback; Bluetooth only if a suitable cuff is in hand), and build a small clip with a motion sensor that checks arm position and stillness, so a bad reading never triggers a dose change.
- **Biology:** encode the protocol and its safety branches, write the test cases, own the clinical story.
