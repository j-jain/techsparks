## 3. Analysis: what it all means

Chapters 1 and 2 set out the problem and what the research found. This chapter puts them together. It states the thesis in a few paragraphs, tests it as a strategy partner and an investor would, and then weighs every option the team considered, so that the choice of what to build comes out of the evidence rather than before it.

### 3.1 The thesis

OUR VIEW throughout this section.

**What works is the treatment change.** The active ingredient is the treatment change, not the sensor and not the nudge. A product that stops at showing a reading sits with the trials whose results are mostly null (chapter 2.1). The authority to change the dose between visits, and someone acting on it, is what worked; electronics added little once a clinician was stepping the dose.

**India's gap sits in one place.** India's programme already has the protocol, free drugs, a record and an overdue list (chapter 2.2). It lacks a dose decision for the uncontrolled patient who does not go back to the doctor: India lacks decide, confirm and act between visits. The Indian null trial, mWellcare, shows where value cannot come from: a prompt at a visit that was happening anyway adds nothing. So the value must come from changing the dose between visits and reaching the half who never return (chapter 1.3).

**The hard engineering is narrow.** It is in trusting the home reading and in bounding the decision, not in the model that makes it (chapter 2.3). Language models can read and speak; a tested engine and a clinician decide.

**The business is the open question.** Lasting businesses are paid for an outcome a payer counts, or for hardware that delivers the dose (chapter 2.4). In India no payer was found for this, and on our own arithmetic the reachable market is small for a venture fund (chapter 2.5).

Put together, the opportunity is the routine treatment decision between visits that the fund asked for (chapter 1.1), made from a trustworthy home reading, approved by someone allowed to approve it, inside programmes India already runs, and paid for by someone other than the patient. The rest of this chapter tests that idea against strategy and against the other options.

### 3.2 Where to play and how to win

This section tests the idea the way a strategy partner and an early-stage deep-tech investor would. Chapter 2 found the deepest evidence and the largest pool in blood pressure, so the questions use blood pressure as the working case; section 3.3 checks that choice against six other options.

#### The question tree

The governing question is whether a medicine-adjusting loop that starts with blood pressure can become a business that improves outcomes for people far from a specialist. Six sub-questions follow, each graded on what the research supports.

| Sub-question | What the research supports | Grade |
|---|---|---|
| 1. Whether the loop works | Abroad, yes, in randomised trials (HyperLink, chapter 2.1; Lesotho, chapter 2.2). India's nearest trial, mWellcare, was null, and no Indian randomised trial of the home loop was found | Strong abroad; missing in India |
| 2. Whether the gap is real in India | Yes on size: about half of programme patients did not return (chapter 1.3). Less clear on cause: in Bathinda, feeling well and distance led (chapter 1.4) | Strong on size; partial on cause |
| 3. Whether it can be delivered safely and legally | Safety: no more falls, low pressure or kidney harm in rural China (chapter 2.1). Law: it is device software under India's July 2026 guidance, with class and pilot permit open; only a registered doctor may prescribe; no order lets a nurse change a dose (chapter 2.6) | Partial |
| 4. Whether anyone will pay | No Indian payer was found (chapter 1.5); our monthly price is an ASSUMPTION (chapter 2.5) | Missing |
| 5. Whether it can be defended | Not yet: the protocol is public, and the government's open-source Simple app, whose protocol model has no step ladder, could add one (chapter 1.5) | Missing |
| 6. Whether this team can start it | The prototype, yes: the protocols and open home readings exist (chapter 2.3). A pilot needs a supervising doctor, an ethics committee and prior registration (chapter 2.6); the team has none yet | Partial |

OUR VIEW: the medicine is settled; payment and defence are not.

#### Where to play

| Choice | Our choice (OUR VIEW) | Why |
|---|---|---|
| Disease | Blood pressure first, insulin second (section 3.3) | The largest pool (chapter 1.2). Insulin adds a low-sugar hazard, and the US clears its dose software as a regulated device (chapter 2.6) |
| Customer | Private clinics and chains first, on a protocol their doctors sign; states later, paid on results | Public medicines cost very little (chapter 1.5), so a state will not pay app prices. Caution: most of the Bhopal private doctors interviewed did not follow the state protocol (chapter 1.4) |
| Channel | Doctor-enrolled chat on a family phone; voice later | Clinician referral added 40 days of retention (chapter 2.1); phones are often shared and many older adults lack a smartphone (chapters 1.3, 2.5) |
| Geography | One state at a time; abroad later | State protocols differ at the second step (chapter 2.2) |

OUR VIEW: the first payer is an urban private clinic, not the rural patient the challenge names.

#### How to win

The business must be best at four things (OUR VIEW). None of them is the rules engine.

| Must be best at | Why it decides the result | "Better" is measured by |
|---|---|---|
| Trusting a home reading from any cuff | Posture alone moves a reading by several mmHg (chapter 2.3) | Share of patients completing a valid 3-day block each cycle; photo-reading error |
| A safe decision in seconds of doctor time | A primary-care consultation lasted about two minutes (chapter 1.3) | Median seconds per approval; share decided within 7 days |
| Keeping patients sending readings | WhatsApp reminders did not raise return visits (chapter 1.4) | Share sending blocks at 3 and 6 months; lapsed patients brought back |
| Proof a payer accepts | Pear had randomised trials yet won too few payers and prescribers, a trade-press review said (chapter 1.5) | Gain in the share under 140/90 at 90 days against comparison clinics |

**Where the money is today.** Medicines are the largest pool; devices are small and one-time; consultations have no checked figure; programmes are diabetes-only and loss-making (chapter 2.5). OUR VIEW: a loop can draw on what a clinic or hospital earns by keeping a patient, or on a medicine maker's patient-support budget (size NOT FOUND). The reachable market is under 5% of the pill pool (OUR ARITHMETIC: the SAM divided by retail blood-pressure medicine sales, chapter 2.5). A doctor paid per visit may see a home loop as lost visits, so the thing to sell is kept patients.

#### Five forces and three futures

Five forces decide who keeps the profit (readings are OUR VIEW).

| Force | Reading | The fact behind it |
|---|---|---|
| Rivalry | Low today | No private home-titration service was found in India (chapter 2.4) |
| New entrants | High | Simple is open source and its programme holds the patients; Lupin's Lyfe and Huma's platform announce Class C licences (THEIR CLAIM) [D1-04-F15, D1-04-F30]; any hospital software team can code a public sheet; the AI labs' health assistants read phone data but change no therapy (chapter 2.4) |
| Substitutes | High | The free public visit: most patients who keep attending are controlled on the first pill, on clinic readings (chapter 2.2) |
| Buyer power | High | No payer buys this today |
| Supplier power | Moderate | Omron already sells a plan-drafting tool for clinicians in the UK (chapter 2.4); the scarcest input is the approving doctor's time |

OUR VIEW: entry is easy and buyers are few.

The next three years turn on two things the team does not control: how strictly CDSCO applies its 2026 guidance, and whether anyone but the patient pays (OUR VIEW).

| Future | What it means | Early sign to watch |
|---|---|---|
| A. Light class, a payer appears | CDSCO confirms Class A or B for a doctor-approved proposal, licensed by the state [D2-04-F12] | A class reply through CDSCO's portal [D2-04-F11]; a first paid contract |
| B. Strict class, a payer appears | Read as "treatment", or as patient-facing without professional support, the tool moves to Class C, licensed centrally, and a pilot becomes a clinical investigation. Slower, but the licence then keeps others out | CDSCO's risk list puts dose-proposing software in Class C [D2-04-F11] |
| C. No payer, either class | The patient is the only buyer; the loop survives as a free feature of the public programme | Pilot clinics decline to pay after the free period; outpatient insurance stays negligible (chapter 1.5) |

OUR VIEW: the payer decides whether this is a company or a feature.

#### The risks that matter

Six risks could end the project. The stop lines are OUR VIEW, to be agreed before any pilot.

| Risk | Stop if |
|---|---|
| Doctors leave proposals unanswered, as mWellcare's prompts added nothing (chapter 2.1) | Most proposals outlast the 30-day cycle after two months |
| No cuff at home: few clinic attenders measure at home (chapter 1.4) | Under half complete a block even with a lent cuff |
| A wrong step from a bad reading; the Gujarat sheet has no low-pressure rule | Serious harm traced to an approved proposal: halt and review |
| A clinical investigation is required before any pilot (chapter 2.6) | Class C and no partner to sponsor it |
| Nobody pays | A positive pilot and no buyer above our monthly cost per patient (ASSUMPTION, chapter 2.5) |
| No gain over a well-run clinic | Under 5 mmHg and no gain in the share controlled |

#### The investor's lens

A deep-tech fund that reports impact and works across Japan and India would test four things; the readings are ours, not the mentor's (OUR VIEW).

- **Hard to copy.** Not today. What could become hard to copy is a record of home readings with medicine changes, since no open dataset of that kind was found (chapter 2.3); but learning is about 15% of the build (OUR ESTIMATE), and nothing built tonight is hard to copy.
- **Prototype to licensed product.** A test licence, a clinical-investigation permit if required, then a manufacturing licence from the state (Class A or B) or the centre (Class C or D) [D2-04-F12]. The class is unknown, fees were NOT FOUND, and the team has no doctor or sponsor yet.
- **Proof that changes the valuation.** A controlled 90-day pilot with one clinic paying. Uncontrolled results are not enough: Closed Loop Medicine had only an uncontrolled trial, and its shareholders wound it up (chapter 2.4).
- **Where Japan fits.** As precedent and supplier, not customer. Japan's insurance pays for a lifestyle-only blood-pressure app (chapter 2.6), and Omron, the cuff maker, is based in Kyoto [D2-02-F34]; the notes show no Japanese partner, payer rule or regulator route.

The fund has backed digital therapy twice: CureApp, its first fund's first investment in 2015 by its chief executive's account [D3-06-F26], and India's Wellthy (chapter 2.4). Its partner says investors like to enter between an alpha prototype and a customer pilot (LinkedIn, read 13 Nov 2026). OUR VIEW: a prototype alone is not fundable; a signed pilot customer is the next proof.

#### Three questions a partner would press

1. **Dose product or follow-up product.** On clinic data, mostly follow-up: among programme patients who kept attending, later steps added 6-7 points of control to what the first pill achieved (OUR ARITHMETIC from chapter 2.2: 77 - 70; 82 - 76) [D1-06-F04]. Home data may show more, because many treated patients who look controlled in clinic are not controlled at home (chapter 1.4). Settled by: a pilot that counts patients brought back separately from doses changed.
2. **Who pays, and whether that buyer serves the patient the challenge names.** Nobody yet. Our assumed yearly price adds about 46% to one private-brand pill's yearly cost (OUR ARITHMETIC: 1,788 ÷ 3,906, chapter 2.5) [D2-05-F17]; the rural patient sits in the public tier, at the lower price assumed in chapter 2.5. Settled by: two clinics signing at a stated price, and one state naming the result it would pay for.
3. **What stops Simple, a hospital or a medicine maker from copying it.** Nothing today. Later: outcome data, a licence, clinic contracts. Settled by: whether logged step responses improve decisions, which takes months of patients.

OUR VIEW: no answer to question 2 within 90 days means a public-good tool, not a company.

### 3.3 The options weighed

The strategy questions used blood pressure as the working case. This section checks that choice. The team sorted every kind of feedback loop from chapter 2.1 and scored seven options, labelled A to G.

#### The option tree

1. **A drug dose or a protocol step.** A: blood pressure, from a home cuff. B: insulin dose in type 2 diabetes, from fasting sugar. G: heart-failure medicines, from weight, pressure, pulse and lab values. C: a breathing plan for asthma and COPD, from an inhaler sensor, peak flow (how hard a person can blow out) and air quality. F: warfarin, from a home INR test. E: weight-loss injection dose, from weight and side effects. Gout was not scored: the one trial found had nurses stepping the dose, with no device or software (chapter 2.1).
2. **Food and behaviour.** Not scored: meals guided by a glucose sensor are already sold in India with a doctor and a coach (chapter 1.5); a lifestyle-coaching app for blood pressure changes no medicine; and activity nudges faded in a 6-week trial of 44 US adults [D1-02-F31, D2-03-F02].
3. **Exercise as the dose.** D: rehabilitation at home, guided by camera and pulse sensor.
4. **Therapy delivered by the device.** Not scored: closed-loop insulin pumps need costly hardware; wearable migraine stimulation is triggered by the patient with no sensor loop; auto-adjusting breathing machines were NOT RESEARCHED.
5. **Biofeedback.** Not scored: guided slow breathing lost its effect without the maker's trials (chapter 2.1), and a pooled result for heart-rhythm feedback (18 studies, 1,352 people) showed no fall in stress [D1-02-F15].

OUR VIEW: as chapter 2.1 found, proof is strongest where the loop changes a drug dose or the device delivers the therapy, and the device route needs expensive hardware, so a student team, and a low-resource country, should start with group 1.

#### Two gates, six tests

Each option had to pass two gates. First, it changes the therapy itself from device or biomarker feedback. Second, it can be built honestly tonight: kit or phone parts, a clinician or health worker confirming every change, and a test on open data, a simulator or teammates. All seven pass the first gate. Heart failure and warfarin pass the second only as rule tests, because neither has a device or data tonight.

The options were then scored from 1 to 5 on six tests, weighted: proof 25, market 20, feasibility tonight 20, gap 15, deep-tech 10, low risk 10. The scores are OUR ESTIMATE: the coordinator's judgement from the first round of notes, not measurements.

| Option | Proof | Market | Tonight | Gap | Deep-tech | Low risk | Score |
|---|---|---|---|---|---|---|---|
| A. Home blood-pressure step loop | 5 | 4 | 5 | 4 | 3 | 4 | **4.35** |
| B. Insulin dose guidance, type 2 diabetes | 4 | 4 | 3 | 3 | 3 | 2 | 3.35 |
| D. Adaptive home rehabilitation (camera and pulse) | 3 | 3 | 5 | 2 | 3 | 4 | 3.35 |
| G. Heart-failure dose loop | 4 | 3 | 2 | 4 | 3 | 2 | 3.10 |
| C. Breathing plan with inhaler sensor and air quality | 2 | 3 | 4 | 3 | 4 | 3 | 3.05 |
| F. Warfarin self-dosing | 5 | 2 | 2 | 3 | 2 | 2 | 2.90 |
| E. Weight-loss injection dose companion | 2 | 4 | 3 | 2 | 2 | 3 | 2.70 |

![Weighted scores of the seven options](adaptive-care-pictures/24-option-scores.png)

*Chart: the seven options on the same six tests. OUR ESTIMATE.*

#### Why each scored as it did

OUR VIEW, one line each.

| Option | Reason |
|---|---|
| A. Blood pressure | The strongest proof, at scale and under non-physicians; the largest patient pool; the exact Indian protocol text; no Indian service found. Weak spots: who pays, and it can look like "just rules" |
| B. Insulin | Good trials and drug-maker interest, but tonight's test is thin: the open data covers only 3-14 days [D1-06-F11] and no open type 2 simulator exists (chapter 2.3). Low blood sugar is a real hazard, and Sanofi already has a dosing app, cleared in the US (chapter 2.6) |
| D. Rehabilitation | The easiest demo, but software rehabilitation matches in-person care without beating usual care (chapter 2.1), and Lupin says it already holds an Indian Class C licence for cardiac rehabilitation |
| G. Heart failure | Strong outcome proof and the best fit to "far from a specialist": in the German TIM-HF2 trial the benefit of remote management grew with distance to a cardiologist, 13% lower risk per doubling of distance [D1-01-F31]. But it needs lab values, so it cannot be tested honestly tonight |
| C. Breathing plan | The most hardware and the best open data [D1-06-F50], but the dose change that works needs no sensor, and sensor inhalers failed commercially (chapters 1.5, 2.1) |
| F. Warfarin | The best proof of all, a small market, no meter tonight |
| E. Weight-loss injections | A hot market since generic semaglutide arrived on 20-21 March 2026 [D1-04-F10], but no outcome evidence for digital dose support yet, with an independent US review due in 2027 [D1-01-F41], and three Indian players already in it (chapter 2.4) |

A second pass of the claims check re-opened 53 clinical facts at source: 48 were confirmed and 5 corrected in wording, and every number matched. The corrections that bear on these reasons are already in chapter 2.1: the pooled gain with intensive support is not for dose changes alone, the China programme also gave free or discounted drugs and paid incentives tied to control, the heart-failure rates are adjusted and came with more side effects, the null telemonitoring trials lacked a mandated dose protocol, and warfarin self-dosing and self-testing were not compared head to head. OUR VIEW: no score moves. Option A leads by a full point, and its proof should be stated as "a protocol inside a funded programme", never as "the protocol alone".

#### The three to weigh, and why blood pressure first

Three options were weighed closely. Insulin dose guidance has strong trials and drug-maker interest, but no honest test tonight and a real low-sugar hazard; it is best shown as a second protocol on the same engine, tested on paper. Home rehabilitation is the easiest demo but a different product with weaker proof. Heart failure fits the challenge's "far from a specialist" best and has strong outcome proof, but it needs lab values, so it is the later protocol for the same engine. The breathing plan, warfarin and weight-loss injections fall behind on proof, market or the night's constraints.

OUR VIEW: blood pressure comes first because only it has all four things at once: a complete published Indian protocol, a cheap and valid home signal, outcome proof at scale (including deaths and strokes avoided under non-physicians), and an honest test tonight. It also has the largest pool of patients (chapter 1.2) and no Indian service doing it (chapter 1.5). Insulin and heart failure are the same loop with a new protocol file; rehabilitation and the breathing plan are different products.

So the choice is the **home blood-pressure step loop**: a checked home reading leads to the next step of the state's published protocol, which a doctor approves before the change reaches the patient. Insulin is the second protocol for the same engine, and heart failure the later expansion.

Full detail: Appendix F (strategy and the options).

OUR VIEW: the concept passes on evidence and timing. It does not yet pass on customer proof or on defence, and the stop lines above should be agreed before any pilot. Chapter 4 shows the product end to end: what the patient and the doctor see, and the checks that keep a bad reading or a missed tablet from changing a dose.
