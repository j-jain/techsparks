## 5. The MVP

Chapter 4 showed the whole product. This chapter shows the MVP (minimum viable product: the smallest product that tests the business): what can be built and tested between 23:00 on 13 November and noon on 14 November, what it can honestly prove, and the two rungs after it.

### 5.1 The ladder

OUR DESIGN, all three rungs:

| Rung | When | What it is | What it proves | What it cannot prove |
|---|---|---|---|---|
| 1. Tonight | To noon, 14 Nov | Engine, three screens, reading route, quality clip, tests, simulation | The code does what the sheet says in every listed branch; readings flow end to end; a person can rule on a card in seconds | Anything about patients |
| 2. Two-week test | After the event | One clinic, a few patients on step 1 or 2, their own doctor rules on every proposal | Patients send valid readings and doctors act on proposals inside normal work | Any change in blood pressure control |
| 3. 90-day pilot | After rung 2 and approvals | Several clinics, a comparison group | Whether more enrolled patients are under the home line at 90 days | Heart attacks, strokes, deaths |

OUR VIEW: each rung earns the next. Going to rung 3 without rung 2 would put an untried loop in front of an ethics committee.

### 5.2 Rung 1: what gets built tonight

OUR DESIGN, from the two build notes:

- **Software.** The `decide()` engine (chapter 4.2), in Python 3.11 with FastAPI, SQLite, pydantic and pytest. Three screens: patient chat, clinician queue, and a results page with a protocol dropdown.
- **Hardware.** The photo route and typed entry (chapter 4.3); Bluetooth only if an Omron HEM-7156T is in hand by about 02:00; the quality clip (chapter 4.5); a pill-box sensor as a stretch goal. One non-Bluetooth cuff and small parts cost about ₹2,000-2,600 (OUR ARITHMETIC); night delivery to Sonipat was not confirmed.
- **Protocol files**, owned by the biology student: Gujarat; Nigeria's losartan ladder, which covers adults 18 and over and has no lab check and no medicine-taken question [D1-06-F15]; and the American Diabetes Association's basal-insulin rule, on paper only, never run on a person. Four rules the claims check found missing from the first Gujarat file (age, the wider pregnancy rule, abnormal labs, out of scope) are now added.
- **Tests.** Thirty-six, one per listed branch, across both protocols and the insulin file; tests for the four added Gujarat rules and the Nigeria rules are still to write. Coverage: every key read by a test, plus line and branch coverage.
- **Checkpoints** (the six roles are in Appendix G). 02:00: a typed reading flows to a proposal, an approval and a message. 05:00: engine frozen. 09:30: testing stops. 10:30: backup video recorded.
- **Cut lines.** If behind, drop in order: WhatsApp; a third language; 20-seed simulation bands; the insulin file as tests; Nigeria as a live dropdown (keep its tests); Telegram (use the web form); the photo or Bluetooth route (use typed readings). Missing 02:00 drops the first four at once. **Never cut:** the adherence check, clinician approval, the pregnancy and childbearing-age, abnormal-lab, "outside the demo" and very-high branches, the test table and the safety statement.

The hardware test uses 6 to 10 volunteer teammates, about 25 minutes each (OUR ESTIMATE), recorded by ID only; anyone at or above 180/110 is told to see a doctor and not tested further. Each is measured in correct posture, arm hanging and arm on the lap, reported as counts and ranges, not p-values. It tests the pipeline and the clip, not cuff accuracy or patients.

OUR VIEW: the critical path is the schema, `decide()`, the core tests, the queue with Approve, and the change message. Hardware hangs off it with a typed fallback, so a hardware failure costs a result, not the demo.

### 5.3 Honest tonight against roadmap

OUR VIEW.

| Tonight: built and tested by noon | Roadmap: needs patients, months or a partner |
|---|---|
| Gujarat and Nigeria files; insulin rule on paper | A model of each patient's response to a step, from real approved steps |
| A pure engine, every branch tested, coverage reported | Learning when to remind each person, to complete reading blocks |
| Photo reading of any cuff, checked and confirmed; Bluetooth if the cuff is in hand | A weighted reading-quality score instead of pass or fail |
| The clip on teammates: correct posture against arm at the side and on the lap | Insulin and heart-failure protocols; heart failure needs lab values |
| Approval queue and Telegram chat | Indian-language voice and offline speech models |
| Replay on open home readings; a labelled simulated cohort | Cuffless sensing, only after a validation protocol exists |

### 5.4 The four results the team can show honestly

The only results that will exist at noon:

| Result | What is measured | May claim | May not claim |
|---|---|---|---|
| (i) Branch coverage | Tests passing (target 36 of 36), line and branch coverage, keys read | "The code does what the sheet says in every branch we listed" | "Safe", "clinically validated" |
| (ii) Simulated cohort | Control by month, needless step-ups, doctor workload | "Under stated assumptions, our model suggests..." | Any effect on patients |
| (iii) Live readings and clip | Readings received, share passing the gate, photo time and accuracy, clip flags | "The pipeline works on real cuffs and real people" | Clinical data; that the clip improves control |
| (iv) Time to approve | Seconds per card and wrong taps, 3 people x 10 cards (OUR DESIGN) | "A person can rule on a card in about n seconds" | Clinical judgement; these are not clinicians on real patients |

Teammates' readings will mostly give "same medicine", so a labelled synthetic patient shows stepping.

**The simulated cohort** (OUR SIMULATION, not a trial, no effect on patients) follows 5,000 patients per arm for 12 monthly cycles. Each patient's hidden "responder step" comes from the programme's Punjab control-by-step figures (chapter 2.2); 48% are non-adherent (search summary only; definition-dependent) [D1-03-F44], used only to count needless step-ups. The clinic arm attends each month at the return rate of chapter 1, an ASSUMPTION that favours it; the loop arm sends a valid block in 30%, 50% or 70% of months (ASSUMPTION). First run (seed 1; to be re-run tonight, not quoted as data): control at month 12 was 39.0% in the clinic-only arm and 49.1%, 55.0% and 59.8% in the loop arm at those three levels (OUR SIMULATION).

The build note's own reading: almost all the modelled gain comes from contact and refills, not smarter stepping, as the step curve is flat after step 3; the adherence check mainly cuts needless step-ups. Both follow from the assumptions. The clinic arm sits between district control and control among returners (chapter 1): plausible, not a validation. OUR VIEW: say this aloud; "the gain comes from contact" is more credible than a dosing claim.

### 5.5 The 3-minute demo script

OUR DESIGN, from the software build note:

| Time | Who | On screen | Words |
|---|---|---|---|
| 0:00-0:25 | Lead | The programme's return and control figures (chapter 1) | "India's protocol works when patients come back. Half don't. We bring the 30-day visit home." |
| 0:25-0:50 | Lead | Loop diagram | "Reading in, protocol step out, doctor taps once, patient told in Hindi." |
| 0:50-1:30 | Patient teammate | Telegram: live cuff photo (or the clip); "2 good readings saved" | "Real reading, quality-checked." |
| 1:30-1:50 | Engine owner | Synthetic patient "Asha", 7 days near 148/92 on amlodipine 5 mg; taps "0 days missed" | "Before stepping up, the protocol says check compliance. We ask." |
| 1:50-2:15 | Doctor (mentor or teammate) | Queue card; tap Approve; timer | "One tap. Every change is approved." |
| 2:15-2:30 | Patient teammate | Hindi message with the change and the doctor's name | "Change delivered in her language." |
| 2:30-2:50 | Biology student | Results page: 36 tests, coverage, simulation chart | "Every branch of the sheet tested. Our simulation, not a trial." |
| 2:50-3:00 | Lead | Switch the protocol to Nigeria; Asha's proposal becomes losartan 50 | "Same engine, any state's protocol." |

Backup: the flow on the local web page, plus the 10:30 recording. Asha's record must say she is past childbearing age (OUR DESIGN), or both sheets' pregnancy rules block the telmisartan and losartan steps.

### 5.6 The safety statement

For the first slide and the README, word for word:

> This is a student prototype built overnight. It is not medical advice and not a medical device. It does not diagnose or treat anyone. A clinician must approve every change of medicine; the software only drafts proposals from a published protocol. No patient data were used tonight. The readings shown are from teammates who volunteered and from synthetic patients; they are not clinical data. The simulation is our own model with stated assumptions, not a trial. Low-blood-pressure and lab-recency limits are deliberately left unset and must be set by a supervising clinician before any real use.

Appendix G holds the draft one-page Deep Tech Thesis and six hard questions with answers.

### 5.7 Rung 2: two weeks with a doctor in the loop

OUR DESIGN. It asks whether the loop survives normal clinic work, not whether it lowers pressure.

- **Setting:** as in the ladder above, inside normal consultations. Written consent names the software, as ICMR's guidance on artificial intelligence expects consent and a human in control [D2-04-F35].
- **Measured:** days with valid readings per patient; proposals and how the doctor ruled, with reasons; time to rule; answers to the medicine question; any symptoms reported.
- **Must not claim:** any change in pressure or control, safety, or clinical effect. Two weeks is shorter than one 30-day step, so few step-ups will happen.
- **Ethics:** a desk test on team members is not a clinical investigation on patients [D2-04-F50]; whether this test needs an ethics committee is a question for the clinic and the university.

OUR VIEW: rung 2 answers the first stop question: do doctors rule on proposals in time.

### 5.8 Rung 3: a 90-day pilot

OUR DESIGN unless cited.

**Primary endpoint:** the share of all enrolled patients with a home mean under 135/85 at 90 days, counting silent patients as not controlled. It can move within three 30-day steps, India's programme already reports control, and counting silent patients tests the loop where the null Indian trial, mWellcare, did not look: between visits, among those who do not return (chapter 2.1).

**Secondary measures:** valid blocks a month; steps taken; time to approve; adverse events, including dizziness, falls and low readings.

| Comparison design | Can show | Cannot show |
|---|---|---|
| Before and after | Change against the clinics' own past | Whether it would have happened anyway |
| Matched clinics | A difference against similar clinics at the same time | Freedom from hidden differences |
| Staggered start (clinics switch on in random order, as in SMARThealth India [D2-01-F16]) | A fairer comparison, each clinic its own control | Quick results: it needs more clinics and time |

**Size** (OUR ARITHMETIC): to tell 40% from 55% controlled (ASSUMPTION) at 5% two-sided significance and 80% power, with 20% drop-out (ASSUMPTION), needs 217 patients per arm, 434 in all, if patients are randomised one by one; randomising by clinic would need more, not computed here. An earlier sketch had about 300 patients over 6 months (OUR DESIGN).

**Approvals** (chapter 2.6): a test licence, permission if the pilot counts as a clinical investigation (a question for counsel), an ethics committee and trial registration before the first patient. Data duties under India's data protection rules start on 13 May 2027 by the gazette's wording (one law firm says a day earlier), inside a pilot starting now [D2-04-F19, D2-04-F20].

**Budget:** about ₹4.35-5.40 lakh for 217 loop-arm patients over 3 months (OUR ARITHMETIC), mostly cuffs at ₹1,849-2,334 each [D2-02-F30], without doctor time, licence and ethics fees (not found) or team costs.

**Three results that would make the team stop** (OUR VIEW):

1. Doctors leave most proposals unruled for days; the loop stalls.
2. Most enrolled patients stop sending valid blocks within the first month; a US programme lost about 45% over its course [D2-01-F5].
3. Any serious harm linked to an approved step, such as symptomatic low pressure or a fall, that the safety branches did not catch.

### 5.9 The next 90 days

Five moves in order; costs only where the notes give one.

| Move | Owner | Cost | Done when |
|---|---|---|---|
| 1. Freeze the engine; replay it on open home readings from 757 Ghanaian patients [D2-03-F61] | Engineering | A cuff, about ₹2,600 (search summary only) [D1-06-F31] | 36 of 36 tests pass; replay logged |
| 2. Sign a supervising physician and one clinic; set the open low-pressure and lab limits | Clinical | No price | A named doctor signs the protocol file |
| 3. Put the three questions for a lawyer (Appendix E) to counsel; ask CDSCO (India's device regulator) for a class through its portal [D2-04-F11] | Business | Fees NOT FOUND [D2-04-F16] | Written answers on class, pilot permit and data duties |
| 4. Ten clinic conversations; test ₹99, ₹149 and ₹299 a month (ASSUMPTION); count cuff owners | Business | No price | Two signed letters, one naming a price |
| 5. File a 90-day pilot of about 300 patients with an ethics committee; register it before the first patient (search summary only) [D2-04-F45] | Clinical | Up to ₹7.8 lakh if every patient is lent a cuff (OUR ARITHMETIC: 300 x ₹2,600) | Submission accepted; registration filed |

OUR VIEW: moves 3 and 4 answer the two rows that the question tree in chapter 3.2 marks as missing: will anyone pay, and can it be defended.

Full detail: Appendix G (protocol file, tests, hour-by-hour plan, parts, hardware test, simulation, sample size, budget, draft thesis, hard questions).

OUR VIEW: tonight's win is a tested loop that a human approves, plus a simulation that honestly says the gain comes from contact. Chapter 6 turns it into a recommendation and names the weak spots before anyone else does.
