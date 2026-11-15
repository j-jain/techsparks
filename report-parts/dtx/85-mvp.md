## J. MVP ladder and tonight's build pack

### 1. What this part shows

This part is tonight's build pack and the plan for the two steps after it. It merges the software note (D2-01) and the hardware note (D2-02) into one schedule, one test list and one list of honest claims for noon.

OUR DESIGN, all three rungs:

| Rung | When | What it is | What it proves | What it cannot prove |
|---|---|---|---|---|
| 1. Tonight | 23:00 Thu 13 Nov to 12:00 Fri 14 Nov | Engine, three screens, reading route, quality clip, tests, simulation | The code does what the protocol sheet says in every listed branch; readings flow end to end; a person can rule on a card in seconds | Anything about patients |
| 2. Two-week test | After the event | One clinic, a few patients already on step 1 or 2, their own doctor rules on every proposal | Patients send valid readings and doctors act on proposals inside normal work | Any change in blood pressure control |
| 3. 90-day pilot | After rung 2 and approvals | Several clinics, a comparison group | Whether more enrolled patients are under the home line at 90 days | Heart attacks, strokes, deaths |

So what for us (OUR VIEW): each rung earns the next. Going to rung 3 without rung 2 would put an untried loop in front of an ethics committee.

### 2. Rung 1, tonight

#### (a) What gets built

OUR DESIGN, from the two build notes:

- **The engine.** One pure Python function, `decide()`, reads a protocol file (YAML, a plain-text data format), the patient's state and the week's readings, and returns a proposal with reasons. No input or output, no clock, no randomness. It never computes a dose; it can only pick a regimen written in the file. No language model in the dose path. Stack: Python 3.11, FastAPI, SQLite, pydantic, pytest.
- **Three screens.** (1) Patient: Telegram chat, same flow on a web form as fallback: measure prompt, photo or typed entry, adherence buttons, change message. (2) Clinician queue: cards sorted urgent first, with step, 7-day sparkline, mean, adherence answer, quoted protocol line, guards ticked, proposed regimen, and Approve, Edit, Reject; a timer is logged. (3) Results: tests, coverage, simulation chart, live-run counts, approve times, protocol dropdown.
- **The reading route.** Every route writes {sys, dia, pulse, time, source, quality_flag}. D2-02's order for tonight: a phone photo of any cuff's screen, read by a vision model and confirmed by the patient; an Omron HEM-7156T over Bluetooth with omblepy, only if one is in hand by about 02:00 [D2-02-F1]; typed entry, always built. Photos are read twice, checked for plausible ranges, and shown back for confirmation. Purpose-trained readers reached 0.9-1.2 mmHg mean systolic error on held-out sets, but about 82% of one Guatemalan field set were poor-quality images and errors clustered in the last digit [D2-02-F4]; general vision models are untested on cuff screens [D2-02-F8].
- **The quality clip.** An ESP32 with two MPU6050 motion sensors, on the cuff (0x68) and a wrist strap (0x69), on GPIO21 and GPIO22. It enforces 300 seconds of still rest, checks the forearm is near horizontal (within 20 degrees) and the upper arm within 15 degrees of a calibrated posture, holds stillness through each 60-second reading, and posts a valid flag with reasons. It does not measure blood pressure. It targets arm hanging at the side (+6.5/+4.4 mmHg) and arm on the lap (+3.9/+4.0) against arm on a desk, from a crossover randomised trial of 133 adults in Baltimore [D2-02-F16]. Unsensed errors (legs crossed, clothing, cuff size, talking) go into a phone checklist.

![Patient chat on the phone](adaptive-care-pictures/10-bp-patient-chat.png)
*Mock-up with example data.*

![Clinician queue of proposal cards](adaptive-care-pictures/11-bp-doctor-queue.png)
*Mock-up with example data.*

![One proposal card in detail](adaptive-care-pictures/12-bp-doctor-detail.png)
*Mock-up with example data.*

#### (b) The protocol as a data file

The biology student owns these files. Every number carries the sheet's words; a `null` key means "not in the source", and the engine refuses that branch until a clinician fills it. Shortened excerpt of the Gujarat HEARTS file [D1-06-F14]:

```yaml
population: {age_gt: 30, text: "Measure blood pressure of all adults over 30 years"}
steps:
  - n: 1
    regimen: [{drug: amlodipine, dose_mg: 5}]
    text: "Prescribe Amlodipine 5mg"
  - n: 2
    regimen: [{drug: amlodipine, dose_mg: 10}]
    text: "After 30 days measure BP again. If still high: Increase to Amlodipine 10mg"
  - n: 3
    regimen: [{drug: amlodipine, dose_mg: 10}, {drug: telmisartan, dose_mg: 40}]
    text: "Add Telmisartan 40mg"
  - n: 4
    regimen: [{drug: amlodipine, dose_mg: 10}, {drug: telmisartan, dose_mg: 80}]
    text: "Increase to Telmisartan 80mg**"
    requires: [blood_sugar, urea, creatinine, urine_protein]   # max_age_days: null
    if_any_abnormal: refer
    if_no_specialist: {withdraw: telmisartan, add: {drug: chlorthalidone, dose_mg: 12.5}}
    text_lab: "If any value is abnormal refer to a specialist. If the patient cannot consult a specialist, withdraw Telmisartan and add Chlorthalidone."
  - n: 5
    regimen: [amlodipine 10, telmisartan 80, {drug: chlorthalidone, dose_mg: 12.5}]
    text: "Add Chlorthalidone 12.5mg***"
    substitutes: [{drug: hydrochlorothiazide, dose_mg: 25, if: chlorthalidone_unavailable}]
after_last_step:
  action: adherence_then_refer
  text: "Check if the patient has been taking medications regularly and correctly. If yes, refer to a specialist."
contraindications:
  - when: [pregnancy, childbearing_age_without_effective_contraception]
    blocked_drugs: [telmisartan, chlorthalidone, ace_inhibitors, arbs, thiazide_or_thiazide_like_diuretics, statins]
    allowed_drugs: [amlodipine]           # "Calcium channel blocker (CCB) can be used."
    if_uncontrolled_on_intensified_dose: refer
    action: block_step_and_refer
    text: "DO NOT give Telmisartan or Chlorthalidone."
out_of_scope:                             # OUR DESIGN: the sheet has these branches; tonight's engine does not
  when: [diabetes, past_heart_attack, past_stroke, chronic_kidney_disease]
  action: flag_outside_demo_send_to_doctor
safety:
  very_high: {sbp_gte: 180, dbp_gte: 110, rule: any, action: repeat_then_urgent_review}
  low: {sbp_lt: null, action: urgent_review}   # not in the sheet; the supervising clinician sets it
```

The rule: **the full files are in the D2-01 note** (Gujarat; Nigeria losartan [D1-06-F15]; the ADA basal-insulin rule from the ADA 2025 figure [D1-06-F16], paper only, never run on a person). Copy from there, not from this excerpt, but add what the claims check found missing from the Gujarat file: the age rule, the wider pregnancy rule, the abnormal-lab branch and the out-of-scope flag shown above [D1-06-F14]. The two blanks in the D2-01 note's second file are now filled from the Nigeria sheet: "still high" is 140/90 or above, and the pregnancy rule is "DO NOT GIVE losartan to pregnant women nor to women of childbearing age who are not on effective contraception. If pregnant, refer to obstetric specialist". That sheet covers adults 18 and over and has no lab check and no medicine-taken question [D1-06-F15]. The very-high action is OUR DESIGN for home readings; the sheet's 180/110 line is for clinic entry [D1-06-F14].

#### (c) The decision in plain steps

1. If the patient is referred or waiting for lab results, do nothing. If the patient is outside the sheet's population (30 or under on the Gujarat file), or has diabetes, a past heart attack or stroke, or kidney disease, flag "outside the demo, send to the doctor": the sheet has branches for these that tonight's engine does not handle [D1-06-F14].
2. Keep only readings that passed the quality gate.
3. Safety first. Newest session at or above 180 systolic or 110 diastolic: ask for a repeat after rest; if confirmed, raise an urgent card and tell the patient to contact the clinic today. This beats the 30-day wait. The low-pressure branch fires only once a clinician sets its threshold.
4. Fewer than 3 valid days: ask for more readings.
5. Fewer than 30 days on the step: "keep going".
6. Home mean below 135/85: "same medicine", no doctor needed.
7. At or above the line: ask the adherence question. Any missed day, or no tablets left: send support, no step-up, card to the clinician for information.
8. On the last step: propose referral.
9. Pregnant, or a woman of childbearing age not on effective contraception, and the next step has a barred drug (telmisartan, chlorthalidone, or any ACE inhibitor, ARB, thiazide-type diuretic or statin): propose referral. Amlodipine steps may go ahead; uncontrolled on the intensified amlodipine dose: propose referral [D1-06-F14]. Labs missing before telmisartan 80: propose a lab order. Any lab value abnormal: propose referral, or, if no specialist can be reached, propose withdrawing telmisartan and adding chlorthalidone [D1-06-F14].
10. Otherwise propose the next step, quoting the sheet line. Nothing that changes treatment reaches the patient before a clinician approves.

The adherence question is two chat buttons: "In the last 7 days, how many days did you miss your BP tablet? 0 / 1-2 / 3 or more" and "Do you have tablets left for the next 7 days? yes / no". Adherent means 0 missed days. That cut-off is OUR DESIGN and the clinician can change it, because the sheet says "Check for compliance at each visit before titration of dose or addition of drugs" but gives no number [D1-06-F14].

#### (d) The home-reading rule

- **Block:** on days 24 to 30 of each 30-day cycle, two readings 1 minute apart after 5 minutes seated rest, morning before tablets and evening [D2-01-F1, D2-02-F10].
- **Valid session:** both readings pass the quality flags; its value is their mean.
- **Enough:** at least 3 distinct valid days, aiming for 7. ESH (the European Society of Hypertension) says "Seven-day monitoring (not fewer than 3 days)" [D2-01-F1].
- **Day 1:** dropped only if 4 or more valid days remain. ESH calls dropping it a "matter of debate" [D2-02-F12]; the AHA notes some guidelines drop it [D2-02-F10].
- **Still high (the home threshold):** mean systolic at or above 135 OR mean diastolic at or above 85. ESH says home 135/85 corresponds to office 140/90 [D2-01-F1]; ISH says home hypertension is readings "consistently 135/85 mm Hg or greater" [D2-01-F3]; the Indian Guidelines IV give above 135/85 (search summary only) [D2-01-F4, D2-02-F15].
- **Very high:** any single session at or above 180 or 110.
- **Clinic reading in the cycle:** the card shows both; the clinician decides.

The Gujarat sheet is written for clinic readings ("SBP 140 or DBP 90") [D1-06-F14]. **Mapping a clinic protocol to home readings at 135/85 is OUR DESIGN.** Say so aloud on the slide, and keep the threshold a protocol value the clinician signs. No Indian home-against-clinic offset was searched.

#### (e) The test table

Thirty-six tests, one per branch; exact inputs are in D2-01 section 3c. The rows marked "to add" cover the rules the claims check found on the sheets [D1-06-F14, D1-06-F15]; they have no test numbers or inputs in D2-01 yet.

| Branch group | Tests | What is checked | Count |
|---|---|---|---|
| On target and threshold edges | T1-T4 | 128/80 holds; 135/80 and 130/85 count as high; 134/84 holds | 4 |
| Reading window and quality | T5, T22, T24, T25 | 2 valid days asks for more; "arm moving" readings ignored; day 1 dropped, but never below 3 days | 4 |
| 30-day interval | T6 | 150/95 after 20 days: keep going | 1 |
| Titrate or support | T7, T15 | Missed doses give SUPPORT, also before referral | 2 |
| Step-ups and guards | T8-T13 | Steps 2 to 5; lab order before telmisartan 80; hydrochlorothiazide substitute | 6 |
| Last step | T14 | Referral with the sheet text | 1 |
| Pregnancy | T16, T17 | Telmisartan step blocked and referred; amlodipine step allowed | 2 |
| Very high and order of checks | T18-T21 | Repeat asked; confirmed gives urgent; diastolic alone counts; safety beats the interval | 4 |
| Paused and unset values | T23, T26 | Referred patient untouched; unset low threshold logs a warning | 2 |
| Clinic entry rules | T27-T29 | 182/96, 165/95, 145/92 route correctly | 3 |
| Second protocol (Nigeria) | T30-T33 | Losartan step with no adherence question; referral; entry at step 2; refuses a file with a null value | 4 |
| Approval path | T34 | Rejected proposal leaves the step unchanged and is logged | 1 |
| Insulin file (paper only) | T35, T36 | +2 units never sent to anyone; low sugar proposes a 10-20% cut | 2 |
| **Total** | | | **36** |
| Childbearing age (Gujarat) | to add | Woman of childbearing age not on effective contraception: telmisartan step blocked and referred; amlodipine step allowed; uncontrolled on amlodipine 10: referral | to add |
| Abnormal lab (Gujarat) | to add | Abnormal value before telmisartan 80: referral; no specialist reachable: withdraw telmisartan, add chlorthalidone | to add |
| Outside the demo (Gujarat) | to add | Age 30 or under; diabetes; past heart attack or stroke; kidney disease: flagged "outside the demo, send to the doctor" | to add |
| Nigeria rules | to add | Still high at 140/90 or above; age under 18 flagged; losartan blocked for pregnancy or childbearing age without contraception; pregnant: referral | to add |

Coverage target: every key in each file read by at least one test; line and branch coverage of `decide()` from `pytest --cov --cov-branch`.

#### (f) Hour by hour, 23:00 Thu to 12:00 Fri

Roles: **E** engine (CS), **I** interfaces (CS), **P** protocol and tests (biology), **H1** clip, **H2** cuff and photo route (hardware), **L** lead, story and simulation. OUR DESIGN, merged from the two notes; where they clash, this table picks one and the clash is listed below it.

| Time | E | I | P | H1 | H2 | L | Checkpoint |
|---|---|---|---|---|---|---|---|
| 23:00-23:30 | Repo, schema, Proposal class | FastAPI skeleton, SQLite tables | Copy file 1; enter the Nigeria 140/90 line and pregnancy rule [D1-06-F15] | Kit inventory | Find a cuff (teammates, staff, health centre) | Problem slide, safety statement | `pytest` runs; is there a cuff |
| 23:30-01:00 | `decide()` steps 0-4, window rules | Telegram echo, then saves readings | T1-T12 | ESP32 + sensor A streaming | Photo page + vision call returning JSON | Write `sim/cohort.py` | 00:30: T1-T8 green; one sensor streams; one photo parsed |
| 01:00-02:30 | `decide()` steps 5-8, guards | Queue page with Approve | T13-T29 | Sensor B; rest-and-measure state machine; LEDs | Confirm screen, checks, post to engine; omblepy if a HEM-7156T exists (60 min) | Run sim, chart v1 | 01:30: sensor B or forearm only. **02:00: typed reading to proposal to approve to message.** 02:30: photo to engine; clip green or red; drop Bluetooth if not working |
| 02:30-04:00 | Nigeria file, refusal of incomplete files, audit log | Adherence buttons; web form | T30-T36, coverage | Tune thresholds on two teammates | Second read and disagreement rule; typed fallback | Seed synthetic patients; loop slide | 03:30: 36 tests and a coverage number |
| 04:00-05:30 | Join reading route and quality flags | Hindi and third-language templates | Check every template against the sheet words | WiFi, NTP time, post quality record | Adherence question in morning flow | Results page | 04:30: flag beside each reading. **05:00: engine frozen** |
| 05:30-07:00 | Approve timer, edit and reject reasons | Protocol dropdown | Prepare test sheets | Rest in shifts (to 06:30) | Rest in shifts | Approve-time trial, 3 people x 10 cards | 06:30: all four results exist in some form |
| 07:00-09:30 | Bug fixes only; 20-seed bands | Optional WhatsApp, stop 08:30; polish card | Run teammates through the bot | Run test protocol (2(i)) | Photograph and transcribe every reading | Thesis final; 6-slide deck | **09:30: stop testing; dress rehearsal 1** |
| 09:30-10:30 | | Record backup video | | Fill results table | Count photo matches | | 10:30: backup recorded |
| 10:30-11:30 | Rehearsal bugs only | | Mentor question drill | Rehearse clip red, engine refuses | Rehearse cheap-cuff photo to engine | Rehearsals 2 and 3 | |
| 11:30-12:00 | Offline mode tested | | | Freeze, pack spares | Freeze | | Present |

Clashes resolved: D2-01 runs teammate readings at 05:30-07:00 and 08:30-10:00, while D2-02 rests hardware until 06:30 and tests 06:30-09:30; the table uses one shared session in D2-02's window. D2-02 builds a reed-switch pill box at 04:30-05:30; D2-01 builds no pill sensor tonight; the table follows D2-01 and keeps the box as a stretch.

#### (g) Cut lines

Drop in this order if behind (D2-01): 1. WhatsApp. 2. Third language. 3. 20-seed simulation bands. 4. ADA file as tests (show the YAML only). 5. Nigeria file as a live dropdown (keep its tests). 6. Telegram (use the web form). 7. Photo or Bluetooth route (use typed readings; show the measurement work separately). If the 02:00 end-to-end checkpoint is missed, apply cuts 1 to 4 at once.

Hardware cuts (D2-02): sensor B failing at 01:30, forearm only; Bluetooth not working at 02:30, drop it; no pill box at 05:30, phone "taken" tap; pulse sensor only if all else is done by 07:00.

**Never cut:** the adherence check, the clinician approval step, the pregnancy and childbearing-age branch, the abnormal-lab branch, the "outside the demo" flag, the very-high branch, the test table and the safety statement.

#### (h) Parts and cost

From D2-02 section 7; prices are search listings (SNIPPET) unless marked opened.

| Item | Usually in a maker kit | Buy tonight if a shop is open | Fallback if not |
|---|---|---|---|
| Upper-arm cuff | No | Omron HEM-7120, list price ₹2,334 (opened, undated) [D2-02-F30]; ₹1,849 online (10 Jun 2026) | Any cuff a teammate, staff member or health centre owns |
| Bluetooth cuff | No | Omron HEM-7156T, ₹2,593-2,892 (mid-2026) [D1-06-F31] | Skip Bluetooth; photo route only |
| Tape measure | Sometimes | Tailor's tape, about ₹50 (OUR ESTIMATE) | Paper strip and ruler |
| ESP32, buttons, LEDs, wires | Yes | | Arduino Uno with USB serial |
| MPU6050 x 2 | Yes | ₹144-275 each (undated) [D2-02-F31] | One sensor on the forearm only |
| Velcro, tape, pill box | Often / No | Under ₹100 each (OUR ESTIMATE) | Medical tape; cardboard box |
| Bluetooth 4.2+ laptop | Laptops | Avoid CSR8510 dongles [D2-02-F1] | Mac or Raspberry Pi |

Cash outlay for one non-Bluetooth cuff and small parts: about ₹2,000-2,600 (OUR ARITHMETIC in D2-02). Only the HEM-7120 is on an independent validation list (passed ESH-IP 2010, Medaval) [D2-02-F28]; the HEM-7156T's validation is Omron's own table (THEIR CLAIM) [D2-02-F29]. Night delivery to Sonipat was not confirmed.

#### (i) Hardware test protocol on teammates

OUR DESIGN, from D2-02 section 8. Volunteers agree verbally; IDs only, no names; anyone at or above 180/110 is told to see a doctor and is not tested further. It tests the pipeline and the clip, not cuff accuracy or patients.

1. Measure arm circumference; the HEM-7120 cuff fits 22-32 cm [D2-02-F30]. Leave other arms out of the posture comparison.
2. Calibrate the clip in correct posture.
3. Conditions in coin-flip order, 2 readings each: C correct; W1 arm hanging at the side; W2 arm on the lap. Repeat C at the end if time allows, to expose drift.
4. Each reading: clip record, two photos (well lit, then with glare), a second person's transcription, Bluetooth readout if present.

Reach: 6 to 10 people, about 25 minutes each on one cuff (OUR ESTIMATE). Report n and ranges, not p-values: clip flags W1 and W2 invalid (x of y); clip passes C (x of y); W1 minus C and W2 minus C against ARMS [D2-02-F16]; photo exact-match rate and confirms; seconds from reading to proposal. Report every failed photo and false alarm.

So what for us (OUR VIEW): the critical path is schema, `decide()`, tests T1-T29, queue with Approve, change message. Hardware hangs off it with a typed fallback, so a hardware failure costs a result, not the demo.

### 3. The four results the team can show honestly

The only results that will exist by noon, with what each may and may not claim.

| Result | What is measured | May claim | May not claim |
|---|---|---|---|
| (i) Branch coverage | Tests passing (target 36 of 36), line and branch coverage, protocol keys read | "The code does what the sheet says in every branch we listed" | "Safe", "clinically validated" |
| (ii) Simulated cohort | Control by month, needless step-ups, doctor workload | "Under stated assumptions, our model suggests..." | Any effect on patients |
| (iii) Live readings and clip | Readings received, % passing the gate, photo-to-stored time, photo accuracy, clip flags | "The pipeline works on real cuffs and real people" | Clinical data; that the clip improves control |
| (iv) Time to approve | Seconds per card and wrong taps, 3 people x 10 cards (OUR DESIGN) (7 step-ups, 1 lab order, 1 pregnancy block, 1 urgent) | "A person can rule on a card in about n seconds" | Clinical judgement; these are not clinicians on real patients |

Teammates' readings will mostly give HOLD; the step path is shown with a labelled synthetic patient.

**The simulated cohort (OUR SIMULATION, not a trial, no effect on patients).** Design: 5,000 patients per arm, monthly cycles for 12 months, same random seed. Assumptions:
- A hidden "responder step" per patient from Punjab control by step (70%, 75%, 77%, then flat) [D1-06-F04]: 0.70 at step 1, 0.05 at step 2, 0.02 at step 3, 0.23 never (OUR ARITHMETIC).
- 48% non-adherent (search summary only; definition-dependent) [D1-03-F44], used only to count needless step-ups.
- Clinic arm: monthly attendance 0.51 from the 51% return rate [D1-03-F10] (ASSUMPTION that favours the clinic arm). No visit means no refill and no control that month; visits step up without an adherence check.
- Loop arm: a valid block each month with probability 0.3, 0.5 or 0.7; non-adherent patients get support, adherent uncontrolled ones an approved step-up; refill 0.9; otherwise the clinic chance (all ASSUMPTION).

First-run numbers (OUR SIMULATION, seed 1, n = 5,000; re-run tonight, do not quote as data):

| Arm | Controlled, month 6 | Controlled, month 12 | Step-ups to non-adherent patients per 100 (12 months) | Proposals per 100 patients a month |
|---|---|---|---|---|
| Clinic only (OUR SIMULATION) | 38.7% | 39.0% | 47.6 | 8.5 |
| Loop, engagement 30% (OUR SIMULATION) | 47.8% | 49.1% | 44.6 | 8.1 |
| Loop, engagement 50% (OUR SIMULATION) | 53.5% | 55.0% | 37.3 | 7.5 |
| Loop, engagement 70% (OUR SIMULATION) | 58.9% | 59.8% | 25.3 | 6.5 |

With Maharashtra figures: clinic 41.4%, loop 52.4-64.3% at month 12. The note's own reading: almost all the modelled gain comes from contact and refills (the 51% return gap), not smarter stepping, because the step curve is flat after step 3; the adherence check mainly cuts needless step-ups. Both follow from the assumptions. The clinic arm's 39% sits between district control of 21.2% [D1-01-F11] and 59.8% among returners [D1-03-F10]: plausible, not a validation. Chart title: "OUR SIMULATION. Assumptions listed. Not a trial."

So what for us (OUR VIEW): say the simulation's own finding aloud; "the gain comes from contact" is more credible than a dosing claim.

### 4. The 3-minute demo script

OUR DESIGN, from D2-01:

| Time | Who | On screen | Words |
|---|---|---|---|
| 0:00-0:25 | Lead | 51% return; 26.3% to 59.8% among returners, no comparison group; 21.2% controlled [D1-03-F10, D1-01-F11] | "India's protocol works when patients come back. Half don't. We bring the 30-day visit home." |
| 0:25-0:50 | Lead | Loop diagram | "Reading in, protocol step out, doctor taps once, patient told in Hindi." |
| 0:50-1:30 | Patient teammate | Telegram: live cuff photo (or the clip); "2 good readings saved" | "Real reading, quality-checked." |
| 1:30-1:50 | Engine owner | Synthetic patient "Asha", 7 days near 148/92 on amlodipine 5 mg; adherence question, tap "0 days missed" | "Before stepping up, the protocol says check compliance. We ask." |
| 1:50-2:15 | Doctor (mentor or teammate) | Queue card with mean, readings, sheet line, guards; tap Approve; timer | "One tap. Every change is approved." |
| 2:15-2:30 | Patient teammate | Hindi message with the change and the doctor's name | "Change delivered in her language." |
| 2:30-2:50 | Biology student | Results page: 36 tests, coverage, simulation chart | "Every branch of the sheet tested. Our simulation, not a trial." |
| 2:50-3:00 | Lead | Switch the protocol to Nigeria; Asha's proposal becomes losartan 50 | "Same engine, any state's protocol." |

Backup: the whole flow on the localhost web page, plus the 10:30 recording. Asha's synthetic record must say she is past childbearing age (OUR DESIGN); otherwise both sheets' pregnancy rules block the telmisartan and losartan steps [D1-06-F14, D1-06-F15].

### 5. Safety statement

Shown on the first slide and in the README, verbatim from D2-01:

> This is a student prototype built overnight. It is not medical advice and not a medical device. It does not diagnose or treat anyone. A clinician must approve every change of medicine; the software only drafts proposals from a published protocol. No patient data were used tonight. The readings shown are from teammates who volunteered and from synthetic patients; they are not clinical data. The simulation is our own model with stated assumptions, not a trial. Low-blood-pressure and lab-recency limits are deliberately left unset and must be set by a supervising clinician before any real use.

### 6. Draft one-page Deep Tech Thesis

Verbatim from D2-01 (347 words in the note):

> **Home BP step loop: bringing India's 30-day hypertension visit home**
>
> *Problem.* India has a simple, published hypertension ladder: amlodipine, then telmisartan, then a diuretic, one step every 30 days. It works for patients who return: in the IHCI cohort, control rose from 26.3% to 59.8% among returners. But only 51% returned, and district control is 21.2%. Consultations last about two minutes, and most rural specialist posts are empty.
>
> *Insight.* Trials agree that home readings alone do little (-1.0 mmHg). Home readings that drive a medicine change work: pharmacist titration 57% against 30% controlled, and village-doctor protocol titration in China cut cardiovascular events by a quarter. India's missing piece is not the protocol. It is the moment when someone reads the pressure, checks the pills were taken, and moves one step.
>
> *What we built.* A loop that takes a quality-checked home cuff reading (photo or Bluetooth) and runs the state's published protocol, stored as data. Before any step-up it asks whether the medicine was taken, because the protocol says compliance comes first. It drafts the next step with its reasons, a doctor approves in one tap, and the patient receives the change in their language. The same engine runs the Gujarat and Nigeria protocols with no code change, and an insulin rule on paper.
>
> *Results by noon.* All protocol branches covered by tests. Real teammate readings flowing end to end. Seconds to approve a change. OUR SIMULATION, calibrated to IHCI step-by-step control rates and the 51% return rate, suggests most of the gain comes from restoring contact and refills, not from smarter dosing. It is a model, not evidence.
>
> *Why it is deep tech.* The defensible parts are trustworthy home measurement on cheap cuffs, the titrate-or-support decision, and a dataset of step-by-step responses that does not exist in India. That dataset is what a future model would need to predict who needs a second drug early.
>
> *Path.* Clinician-approved decision support at one clinic chain (about ₹149 per patient per month), an ethics-approved pilot measuring control and return rate, then a CDSCO licence and state programmes on outcome-linked pricing.

Update once tonight's numbers exist: the test count and coverage percentage; the median seconds to approve; readings received and % passing the quality gate; photo-reader match rate; the re-run simulation figures. Wording fixes from the claims checks: the China result came with free or discounted drugs and incentives for village doctors [D1-01-F38]; the 26.3% to 59.8% rise is among returners with no comparison group [D1-03-F10]; consultations lasted about two minutes in 2013-2015 [D1-03-F24]; "most rural specialist posts" means about 80% of required posts in four specialities at rural community health centres, March 2023 [D1-03-F16]; and mark ₹149 as an ASSUMPTION.

#### A corrected draft (use this one)

OUR VIEW. The same thesis with the claims-check wording applied and tonight's rulings on the reading route. Fill the three blanks with tonight's real numbers.

> **Home BP step loop: bringing India's 30-day blood-pressure step home**
>
> *Problem.* India has a simple, published blood-pressure ladder: amlodipine, then telmisartan, then a diuretic, one step every 30 days. In the government programme's cohort, control rose from 26.3% to 59.8% among patients who returned, with no comparison group. But only 51% returned, and in the programme's first nine districts 21.2% of people with high blood pressure are controlled. About 80% of required specialist posts at rural community health centres are unfilled.
>
> *Insight.* Home readings alone do little: 1.0 mmHg in pooled trials. Home readings that lead to a medicine change work. Pharmacists adjusting from home readings got 57% of patients controlled against 30%. In rural China, village health workers stepping doses by protocol, with free or cheaper medicines and pay for results, cut cardiovascular events by about a quarter over four years. An Indian trial that only prompted clinicians during visits added nothing. The missing piece is the step between visits: someone reads the pressure, checks the pills were taken, and moves one rung.
>
> *What we built.* A loop that takes a home reading (a phone photo of any cuff's screen, confirmed by the person, with a clip that checks posture), runs the state's published protocol from a data file, and asks whether the medicine was taken before any step-up. It drafts the next step with its reasons. A doctor approves in one tap, and the change goes out in the patient's language in the doctor's name. The same engine runs a second country's protocol with no code change, and an insulin rule on paper.
>
> *Results by noon.* [tests passed and coverage]. [teammates' readings received and share passing the quality check]. [median seconds to approve]. Our simulation, built on the programme's own step-by-step figures, suggests most of the gain would come from restoring contact and refills. It is a model, not evidence.
>
> *Why it is deep tech.* The hard parts are a home reading that can be trusted on a cheap cuff, the decision to step up or to support, and a record of each patient's response to each step, which nobody in India holds.
>
> *Path.* A prototype today, not a medical device. Next: clinician-approved proposals at one clinic under ethics approval, then a licence under India's 2026 guidance on device software. Our price of ₹149 a patient a month is an assumption to test.

Sources for the corrected draft: [D1-03-F10], [D1-01-F11], [D1-03-F16], [D1-01-F05], [D1-01-F04], [D1-01-F09], [D1-01-F38], [D1-01-F46], [D1-06-F14], [D2-04-F01].

### 7. The hardest questions

Six questions the notes expect from a deep-tech fund, with short answers.

**Software (D2-01)**

1. *"This is a rules engine. Where is the deep tech, and what stops Simple copying it?"* The dose logic should be rules, because the evidence comes from protocol titration [D1-01-F09, D1-01-F38]. The hard parts are trusting a home reading from any cuff, choosing between stepping up and fixing intake, and a dataset of approved steps with their 30-day response that nobody in India holds [D1-06-F42]. Simple's protocol model stores a drug list and follow-up days, and no step logic was found in it [D1-06-F40]; we aim to plug into it.
2. *"What measurable impact, and how soon?"* Tonight: code correctness and a simulation only. The endpoint is the share of enrolled patients controlled plus the return rate, against IHCI's 51% return and 21.2% district control [D1-03-F10, D1-01-F11]. A US programme reported -8.7 mmHg at 6 months against education alone, non-randomised, with about 45% dropped out or unreachable [D2-01-F5], so engagement is the number to watch.
3. *"Who pays, and is this a medical device?"* Probably a device. CDSCO's software guidance was issued 21 Jul 2026 [D2-04-F01] (D2-01 still had the 21 Oct 2025 draft [D2-01-F11]) and names a hypertension digital therapeutic as device software [D2-04-F07]; the D2-04 note reads a doctor-approved step proposal as Class B, or A, with CDSCO confirming the class [D2-04-F06]. First payer: a private clinic chain at about ₹149 per patient a month (ASSUMPTION), since public drugs cost about ₹200 per patient per year [D2-01-F12].

**Hardware (D2-02)**

4. *"Your clip measures angles, not heart level."* It compares each reading with a supervised reference posture and catches the two errors with published sizes [D2-02-F16]. Its tolerance is about 1 mmHg of height shift (OUR ARITHMETIC at 0.49 mmHg per cm [D2-02-F17]). Legs, clothing, cuff size and talking are checklist items. Tonight shows only whether it separates deliberately wrong posture on a few teammates.
5. *"Patients can photograph an old reading, and the model can misread."* Trained readers reach about 1 mmHg error on good images, but field images are often poor [D2-02-F4] and general models are untested [D2-02-F8]. So reads are shown back, two must agree, memory screens are rejected, a step needs at least 3 days, and the doctor approves. A photo cannot prove who or when; the clip time-join narrows that gap without closing it.
6. *"Is a ₹2,000 cuff accurate enough, in Indian arms?"* Use listed cuffs: the HEM-7120 passed ESH-IP 2010 [D2-02-F28]; a popular Indian model is listed as not validated [D2-02-F32]. Cuff size matters more: a regular cuff reads +4.8 mmHg on large arms and +19.5 on extra-large arms [D2-02-F19], so the app asks arm size and refuses out-of-range arms. Validation in Indian populations was not found.

### 8. Rung 2: a 2-week test with a doctor in the loop

OUR DESIGN, built only from what the notes support. It asks whether the loop survives normal clinic work, not whether it lowers pressure.

- **Setting:** one clinic; a small number of adults already on step 1 or 2; their own doctor reviews every proposal in a normal consultation; written consent naming the software, as ICMR's AI guidance expects consent and a human in control [D2-04-F35]. Under the telemedicine guidelines only a registered doctor may counsel or prescribe, and the final prescription or counselling "has to be directly delivered by the RMP" (registered medical practitioner; clause 5.4) [D2-04-F17]. OUR DESIGN, a question for a lawyer: the approval and the patient message are the doctor's own act, sent in the doctor's name.
- **Measured:** days with valid readings per patient; proposals raised and how the doctor ruled, with reasons; time to rule; answers to the medicine question; any symptoms reported.
- **Must not be used to claim:** any change in pressure or control, safety, or clinical effect. Two weeks is shorter than one 30-day step [D1-06-F14], so few step-ups are expected.
- **Ethics:** a desk test on team members is not a clinical investigation on patients [D2-04-F50]. Whether this test counts as research needing an ethics committee is a question to put to the clinic and the university, not something this document decides.

So what for us (OUR VIEW): rung 2 answers the first kill question in the spine: do doctors rule on proposals in time.

### 9. Rung 3: a 90-day pilot

OUR DESIGN throughout unless cited.

**Primary endpoint:** the share of all enrolled patients with a home mean under 135/85 at 90 days; patients who stop sending readings count as not controlled. Why: it can move within three 30-day steps; control is what India's programme already reports [D1-01-F11]; and counting silent patients tests the loop where mWellcare did not look, between visits and among the 49% who do not return [D1-01-F46, D1-03-F10].

**Secondary measures:** return or engagement rate (valid blocks a month); steps taken; time to approve; adverse events, including dizziness, falls and low readings.

**Comparison options:**

| Design | Can show | Cannot show |
|---|---|---|
| Before and after | Change against the clinics' own past | Whether it would have happened anyway |
| Matched clinics | A difference against similar clinics at the same time | Freedom from hidden differences between clinics |
| Staggered start (clinics switch on in random order, as in SMARThealth India [D2-01-F16]) | A fairer comparison, each clinic its own control | Quick results: it needs more clinics and time |

**Sample size (OUR ARITHMETIC).** Comparing two proportions, 40% controlled against 55% (ASSUMPTION), two-sided 5% significance (z = 1.96), 80% power (z = 0.8416):

- p-bar = (0.40 + 0.55) / 2 = 0.475; 2 x 0.475 x 0.525 = 0.49875; square root = 0.7062
- 0.40 x 0.60 + 0.55 x 0.45 = 0.24 + 0.2475 = 0.4875; square root = 0.6982
- n per arm = (1.96 x 0.7062 + 0.8416 x 0.6982)^2 / (0.15)^2 = (1.3842 + 0.5876)^2 / 0.0225 = 3.8880 / 0.0225 = 172.8, so 173
- With 20% drop-out (ASSUMPTION): 173 / 0.8 = 216.3, so **217 per arm, 434 in all**

This assumes patients are randomised one by one. Randomising by clinic would need more patients; that is not computed here. D2-01's earlier sketch was about 300 patients over 6 months (OUR DESIGN).

**Approvals and registrations (from D2-04):** a Form MD-13 test licence covers software made "for the purpose of Clinical Investigations or Test or Evaluation or Demonstration" [D2-04-F13]; a clinical investigation of an investigational device on patients needs CLA permission on Form MD-22/MD-23 [D2-04-F14, D2-04-F39]; an ethics committee approval and CTRI registration before the first patient [D2-04-F45]. Whether a pilot where software drafts and a doctor decides each change counts as a clinical investigation is a question for counsel [D2-04-F50]. Data duties under the DPDP Rules start on 13 May 2027 by the gazette's wording (one law firm says a day earlier), inside a pilot that starts now [D2-04-F19, D2-04-F20]. No Indian legal basis was found for a nurse or community health officer changing doses [D2-04-F18].

**Budget lines** (OUR ARITHMETIC, 217 loop-arm patients, 3 months, prices from the notes):

| Line | Unit | Total |
|---|---|---|
| Cuffs (HEM-7120) | ₹1,849-2,334 each [D2-02-F30] | ₹4,01,233-5,06,478 |
| Messages (WhatsApp) | ₹15 a patient a month (ASSUMPTION in D2-01; price not searched) | ₹9,765 |
| Health worker calls to silent patients | ₹30 a patient a month (ASSUMPTION; D2-01: ₹25,000 / 9,600 minutes x 5 = about ₹13, rounded up) | ₹19,530 |
| Cloud and photo reading | ₹7 a patient a month (ASSUMPTION) | ₹4,557 |
| **Total** | | **about ₹4.35-5.40 lakh (OUR ARITHMETIC)** |

Not included: doctor time, licence and ethics fees (not found in the notes), team costs.

**Three results that would make the team stop (OUR VIEW):**
1. Doctors leave most proposals unruled for days, so the loop stalls.
2. Most enrolled patients stop sending valid blocks within the first month (the US programme lost about 45% over its course [D2-01-F5]).
3. Any serious harm linked to an approved step, such as symptomatic low pressure or a fall, that the safety branches did not catch.

### 10. So what for us

OUR VIEW:
- Tonight's win is a tested loop that a human approves, plus a simulation that honestly says the gain comes from contact. Do not trade that for a bigger claim.
- The 135/85 home mapping is our design; say it before a mentor does.
- Rung 2 is the real next step: one clinic, two weeks, with the ethics question put to the clinic and university on day one.
- The 90-day pilot needs about 434 patients if randomised one by one (OUR ARITHMETIC), more by clinic, and an answer from counsel. Budget time for that before money.
