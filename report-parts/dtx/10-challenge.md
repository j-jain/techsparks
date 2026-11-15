## B. The challenge decoded

### B1. What this part shows

This part turns the fund's challenge into product requirements and a 0-4 scale for sorting ideas. It then gives five rules from the trials, endpoints for a 90-day pilot and a three-question test.

### B2. The challenge, phrase by phrase

The middle column is our reading of each phrase. Terms are explained in B9.

| The fund's words | What a product must do (OUR VIEW) | Facts behind it |
|---|---|---|
| "rapid feedback from medical devices or biomarkers" | A signal that moves within days of a treatment change and is cheap and correct to measure at home. | Bluetooth cuff: about ₹2,500-2,900 (online listings, mid-2026 or undated; search summary only) [D1-06-F31]. Signal speeds: B5. |
| "continuously personalise care" | Recompute the treatment from this patient's readings: protocol step, response to the last step, medicine taken or not, what is unsafe. | Gujarat's hypertension sheet: "Check for compliance at each visit before titration of dose or addition of drugs" [D1-06-F14]. |
| "adaptive to patient needs between appointments" | Change the treatment without waiting for the next visit. | 51% of 21,895 patients at 24 government hypertension programme sites returned for follow-up [D1-03-F10]. |
| "measurable improvements in health outcomes" | One endpoint that can move in 90 days, with an accepted threshold for "clinically meaningful". | An independent US review (October 2024) set it at 5 mmHg of systolic pressure (the upper number) [D1-01-F39]. |
| "patients who cannot access frequent specialist support" | Move the routine decision to a general doctor, nurse or health worker under a written protocol. The specialist owns the protocol and sees the exceptions. | 79.9% of required specialist posts at rural community health centres were unfilled (B8) [D1-03-F16]. |
| "beyond monitoring and reminders" | Reach adaptive depth 4: the therapy itself changes. | Self-monitoring alone: 1.0 mmHg; with intensive support (dose changes by doctors, pharmacists or patients, plus education or counselling): 6.1 (B6) [D1-01-F05]. |

**So what for us.** OUR VIEW: the fund asks for a routine treatment decision between visits, from a home reading, by someone the patient can reach.

### B3. What "beyond monitoring and reminders" rules in and out

This document scores every product on an "adaptive depth" scale from 0 to 4. The fund names levels 1 and 2. OUR VIEW: it is asking for level 4.

| Level | Examples in the notes | What the evidence shows |
|---|---|---|
| 0: uses no patient data | Nerivio migraine wearable, switched on by the patient, rated 0-1 [D1-02-F12]. India: none rated 0 | Nothing adapts. |
| 1: shows data | India: pocket ECGs (search summary only) [D1-04-F32]. Abroad: Omron VitalSight [D1-01-F39] | Self-monitoring alone: no effect [D1-01-F05]; one exception, a glucose sensor, in part D [D1-01-F42]. |
| 2: reminders, generic content | India: government Simple app, with overdue lists and reminder messages [D3-05-F03]. Abroad: Medisafe reminder app | Medisafe, 411 US adults, 12 weeks, against control: 0.5 mmHg, not significant [D1-01-F06]. |
| 3: coaching from the person's own data | India: Sugar.fit, BeatO, Fitterfly [D1-04-F04, D1-04-F06, D1-04-F07]. Abroad: CureApp HT, Japan | CureApp HT, 390 untreated patients, 12 weeks, against lifestyle advice alone: 24-hour systolic 2.4 mmHg lower [D1-01-F07]. |
| 4: changes the therapy (dose, protocol step, exercise prescription) | India: only Sanofi's My Dose Coach found, its Indian results unconfirmed [D1-04-F09]. Abroad: d-Nav; insulin pumps [D1-05-F41] | d-Nav dose device (maker-linked authors), 181 US insulin users, 6 months, against clinician support alone: HbA1c (three-month average sugar) down 1.0 point against 0.3 [D1-01-F13]. |

**The line between 3 and 4.** Level 3 changes the advice: what to eat, how to exercise. Level 4 changes the prescription: a new dose or protocol step. A clinician approving each change keeps it at level 4. Indian diabetes programmes sit at 3: no page says sensor data changes a drug dose [D1-04-F04, D1-04-F06, D1-04-F07]. The test: after the software runs, the prescription is different.

**So what for us.** OUR VIEW: level 4 is the entry condition, however good the sensor.

### B4. The loop: sense, decide, confirm, act, learn

Five stages: what happens at each, and where existing products stop.

![Monitoring against a therapy loop](adaptive-care-pictures/00-the-loop.png)

*Diagram: monitoring stops at the reading; a therapy loop changes the treatment.*

- **Sense.** A home device gives a number, valid only if taken correctly. Level 1 products stop here (B3).
- **Decide.** Software applies a written protocol to this patient's readings and proposes the next step. Coaching apps decide advice, not doses [D1-04-F04]; the protocol model of the government's Simple app stores a drug list and follow-up days, and no step ladder was found in it [D1-06-F40].
- **Confirm.** A doctor, nurse or health worker approves each change; unsafe cases go to a specialist. Trials used pharmacists [D1-01-F04] or village doctors [D1-01-F09]; no Indian service doing this from home readings was found [D1-04-F09].
- **Act.** The patient gets the new dose, medicine or exercise level. Heart-failure telemonitoring trials without a mandated dose protocol found no benefit (B6).
- **Learn.** The next readings show whether it worked, and the loop runs again. At 24 government-programme sites, 10,621 of 21,895 patients did not return [D1-03-F10].

**So what for us.** OUR VIEW: India lacks decide, confirm and act between visits.

### B5. A map of feedback-driven therapies

Five kinds, by what the loop changes.

| What changes | Home signal | How fast it responds | Proof | Who decides |
|---|---|---|---|---|
| 1. Drug dose or protocol step | Cuff, fasting sugar, INR (clotting test), weight | Days to weeks: insulin every 3 days in a 2025 US rule [D1-06-F16]; blood pressure re-checked at 30 days [D1-06-F14] | Strong: randomised trials with fewer deaths, clots or hospital stays [D1-01-F38, D1-01-F27, D1-02-F05] | Patient on an agreed plan, pharmacist, nurse or health worker [D1-01-F01, D1-01-F04, D1-02-F06, D1-01-F09] |
| 2. Food and behaviour | Glucose sensor, step count | Each meal [D1-01-F22] | Mixed: a company-linked Indian trial cut HbA1c 2.9 points against 0.3 with standard care (319 people, 1 year) [D1-01-F19]; a US review of type 2 tools without a continuous sensor was negative (B7) [D1-01-F40] | App, coach |
| 3. Exercise as the dose | Camera, pulse, effort rating | Each session [D1-06-F36] | Matches in-person care; no better than usual care (pooled stroke trials, 661 people) [D1-02-F07] | Therapist or app [D1-02-F54] |
| 4. Therapy delivered by the device (closed-loop insulin pump) | Glucose sensor | Automatic | Strong: against a sensor alone, a dose algorithm cut HbA1c a further 0.6 points (319 adults with type 2 diabetes, US and Canada, 13 weeks, Tandem-funded) [D1-01-F43] | Algorithm, within clinician-set limits [D1-05-F41] |
| 5. Biofeedback (a body signal shown back to the patient) | Breathing or pulse sensor | During practice [D1-02-F15] | Weak: guided breathing had no blood-pressure effect once maker-linked trials were excluded (8 trials, 494 people) [D1-02-F11] | Patient |

OUR VIEW: proof is strongest in kinds 1 and 4, where a drug dose with a known effect is changed and the signal is cheap, valid and fast. Kind 4 needs expensive hardware; kind 1 needs almost none. A student team, and a low-resource country, should start there.

### B6. Five rules the evidence gives

OUR VIEW: five rules, each with the numbers behind it.

**1. The reading must change the treatment.** Across 15 pooled trials (7,138 people, 12 months), self-monitoring alone lowered systolic pressure 1.0 mmHg against usual care, no effect; with intensive support (dose changes by doctors, pharmacists or patients, plus education or counselling), not dose changes alone, 6.1 [D1-01-F05]. Two US heart-failure trials of remote monitoring without a mandated dose protocol (1,653 and 1,437 patients, 180 days) found no benefit [D1-01-F32, D1-01-F33]. Fast dose stepping after discharge cut readmission or death (B7) [D1-01-F27]. Against usual care, warfarin patients who set their own dose from home tests had fewer deaths (risk ratio 0.55, 8 trials); in 3 separate trials, those who left the dose to the clinic did not (0.94); the two approaches were not compared head to head [D1-02-F05].

**2. Who is allowed to decide matters more than the electronics.** In a UK trial (1,182 patients, 12 months), sending readings electronically added a non-significant 1.2 mmHg over paper once the family doctor adjusted doses [D1-01-F03]. In rural China (33,995 people, 18 months), supervised village doctors stepping drugs by protocol got 57.0% under 130/80, against 19.9% with enhanced usual care [D1-01-F09]. At 4 years cardiovascular events were lower (hazard ratio 0.75 at age 60 and over), though the programme also gave free or discounted drugs and paid incentives [D1-01-F38].

**The Indian null result belongs here.** mWellcare (40 community health centres, 3,698 people with hypertension or diabetes, 12 months, randomised by centre) gave nurses and doctors an app that prompted treatment steps. Against enhanced usual care the systolic difference was 0.98 mmHg, not significant; both arms fell about 13 mmHg [D1-01-F46]. OUR VIEW: it shows that a prompt at a visit adds nothing to a well-run programme. It does not show that dose changes between visits fail: no Indian randomised trial tested that (D1-01, NOT FOUND list).

**3. Adherence technology alone does not move outcomes.** Smart pillboxes or medication labels for tuberculosis (23,483 patients, four countries) did not reduce poor outcomes against standard care [D1-02-F59]. Inhaler reminders for 220 New Zealand children gave 84% adherence against 30% over 6 months, with no difference in school absence [D1-02-F01]. OUR VIEW: raising a dose that is not being taken is unsafe, so adherence is an input to the dose decision, not a product.

**4. Someone must pay for the outcome.** Apps and sensors sold on their own failed. Pear's assets fetched just over $6 million against $130 million of liabilities (2023-2024) [D1-02-F42]; Teva stopped US distribution of its sensor inhalers on 1 June 2024 [D1-02-F41]. Those at scale are paid by employers and insurers for clinician-led programmes (Hinge Health: revenue $234.970 million in the third quarter of 2026 [D1-05-F15, D1-05-F16]) or sell a therapy device (Insulet: $842.0 million [D1-05-F41]).

**5. People stay when their own clinician is in it.** In 8 remote US studies (over 1,00,000 participants) median retention was 5.5 days. Clinician referral added 40 days [D1-02-F27]. OUR VIEW: a consumer app is the wrong shape.

**So what for us.** OUR VIEW: B10 turns these rules into a test for any idea.

### B7. What "measurable" means

One endpoint per condition that a pilot could read at about 90 days.

| Condition | Endpoint | Effect the trials found | "Clinically meaningful" threshold |
|---|---|---|---|
| High blood pressure | Share under 140/90 [D1-06-F03] | 57.2% controlled with pharmacist dose changes from home readings, against 30.0% with usual care (450 US patients, at both 6 and 12 months) [D1-01-F04] | 5 mmHg systolic against usual care [D1-01-F39] |
| Type 2 diabetes on insulin | HbA1c | Down 1.44-1.48 points with daily dose proposals, against 0.92 with standard care (191 adults, France, 4 months) [D1-01-F14] | None given; a US review judged 0.23-0.60 points not meaningful for type 2 tools without a continuous sensor [D1-05-F4] |
| Diabetes with a sensor | Time in range | Up 14 points with a dose algorithm (B5) [D1-01-F43] | NOT RESEARCHED |
| Heart failure | Readmission or death | 15.2% against 23.3% at 180 days with fast dose stepping after discharge (1,078 patients, 14 countries; adjusted estimates; side effects 41% against 29%) [D1-01-F27] | NOT RESEARCHED |
| Warfarin | Time in the target INR range | Trials against usual care report clots (risk ratio 0.47) and deaths (0.55) instead [D1-02-F05] | NOT RESEARCHED |

No blood-pressure dose-change trial in our first-round notes reported before 6 months [D1-01-F01, D1-01-F04].

**So what for us.** OUR VIEW: for blood pressure, measure the share under 140/90 at 90 days among patients who would not have returned.

### B8. What "cannot access frequent specialist support" means in India

Five numbers show the gap.

1. **79.9%**: required posts in four specialities (surgery, medicine, obstetrics, paediatrics) unfilled at rural community health centres, March 2023 [D1-03-F16].
2. **About 650** endocrinologists and **4,000** cardiologists, 2017 count (search summary only) [D1-03-F18].
3. **About 2 minutes**: a primary-care consultation, 2013-2015 [D1-03-F24].
4. **51%**: of 21,895 patients at 24 government hypertension programme sites returned for follow-up, 2018-2019 [D1-03-F10].
5. **9.8%**: diabetes control rate in a Tamil Nadu survey (denominator not stated), though over 95% of diagnosed patients were on treatment (6,856 adults, 2025 paper) [D1-03-F09].

**So what for us.** OUR VIEW: the scarce thing is the prescriber's decision, which waits for a visit that about half the patients do not make.

### B9. Terms used in this document

- **Adaptive depth:** 0-4 score for how far a product changes treatment.
- **Adherence:** taking the medicine as prescribed.
- **Closed loop:** a device that measures and adjusts therapy itself.
- **Digital therapeutic:** software that changes one patient's treatment.
- **Endpoint:** the result a trial is judged on.
- **Hazard ratio:** a risk ratio measured over time; below 1 means fewer events.
- **HbA1c:** blood test of average sugar over about three months.
- **INR:** clotting test that sets the warfarin dose.
- **Not significant:** small enough to be chance (a null result).
- **Protocol:** a written step-by-step treatment plan.
- **Randomised trial:** people get treatments by chance.
- **Risk ratio:** risk with treatment divided by risk without; below 1 means lower risk.
- **Systolic:** the upper blood-pressure number, in mmHg (millimetres of mercury).
- **Time in range:** share of the day with sugar at 70-180 mg/dL.
- **Titration:** stepping a dose towards a target.

### B10. So what for us

OUR VIEW. Any idea must pass three questions.

1. **What changes?** After a home reading the prescription is different (level 4), within days.
2. **Who decides?** A general doctor, nurse or health worker, under a written protocol; unsafe cases go to a specialist.
3. **What moves, and who pays?** One endpoint passes an accepted threshold in 90 days, and a named payer wants it.

![Same loop, new protocol](adaptive-care-pictures/15-same-loop-new-protocol.png)

*Diagram: the same loop runs insulin, heart-failure and warfarin rules; only the home signal and the protocol file change.*
