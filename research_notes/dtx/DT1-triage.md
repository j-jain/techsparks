# DT1 triage: what to build tonight (coordinator, Fable, 2026-11-13 about 10 PM IST)

Written from the Round 1 notes D1-01 to D1-06. Fact IDs point into those notes. Numbers were opened at source by the research agents unless marked SNIPPET. The second-pass claims check has not run yet.

## 1. What Round 1 established

**Loops that change the medicine from home readings work.**
- TASMINH2: self-titration by a pre-agreed plan, systolic 5.4 mmHg lower at 12 months (D1-01-F01). TASMIN-SR: 9.2 mmHg lower (D1-01-F02). TASMINH4: GP titrating from home readings, 3.5 to 4.7 mmHg lower (D1-01-F03).
- HyperLink: pharmacists adjusting drugs from home telemonitoring, 57.2% controlled against 30.0%, systolic 10.7 mmHg lower at 6 months (D1-01-F04).
- China Rural Hypertension Control Project: village doctors starting and stepping drugs by protocol, 57.0% against 19.9% under 130/80 at 18 months; at 4 years cardiovascular events HR 0.75 (age 60+) and 0.64 (under 60), all-cause death HR 0.90 (60+), with no difference in falls, low pressure or kidney outcomes (D1-01-F09, F38).
- COBRA-BPS (Bangladesh, Pakistan, Sri Lanka): 5.2 mmHg lower, 53.2% against 43.7% controlled (D1-01-F37).
- Insulin: d-Nav HbA1c down 1.0 against 0.3 (D1-01-F13); TeleDiab-2 down 1.44 and 1.48 against 0.92 (D1-01-F14).
- Heart failure: STRONG-HF rapid up-titration, readmission or death 15.2% against 23.3%, RR 0.66 (D1-01-F27).
- Warfarin: home test plus self-dosing, clots RR 0.47, death RR 0.55 (D1-02-F05). Gout nurse titration, 95% against 30% at target (D1-02-F06). Patient-adjusted asthma steroid dosing, exacerbations RR 0.68 (D1-02-F37).

**Monitoring and reminders alone mostly do not.**
- Self-monitoring alone: 1.0 mmHg, no effect; with intensive support 6.1 mmHg (D1-01-F05).
- MedISAFE-BP reminder app: 0.5 mmHg, p=0.78 (D1-01-F06).
- Heart-failure telemonitoring without a therapy change: TELE-HF and BEAT-HF negative (D1-01-F32, F33).
- Warfarin home testing with a phone call to the clinic: death RR 0.94 (D1-02-F05).
- ASCENT tuberculosis pillboxes, n=23,483: no gain in outcomes (D1-02-F59). Inhaler reminders: adherence 30% to 84%, school absence unchanged (D1-02-F01).
- PHTI, Oct 2024: only medication-management programmes gave clinically meaningful falls; monitoring-only and behaviour-change programmes did not (D1-01-F39, D1-05-F1, F2). PHTI, Mar 2024: digital diabetes tools "do not deliver clinically meaningful benefits and result in a higher cost than usual care" (D1-01-F40).

**India's gap is the dose change and the return visit.**
- IHCI cohort: 51% returned; among returners control rose from 26.3% to 59.8% (D1-03-F10). District surveys: 14.5% controlled in 2018-19, 21.2% in 2023-24 (D1-01-F10, F11).
- Tamil Nadu: over 95% of diagnosed on treatment, 9.8% of diabetics and 35.4% of hypertensives controlled (D1-03-F09).
- Rural community health centres: 79.9% of specialist posts vacant (D1-03-F16). Consultation about 2 minutes (D1-03-F24).
- Scale: hypertension 35.5% and diabetes 11.4% of adults 20+ (D1-03-F01).

**Nobody in India was found running a dose-change loop from home readings.**
- Diabetes programmes sit at adaptive depth 3 (D1-04-F02, F04, F06, F07). Sanofi My Dose Coach is the one depth-4 product; India status unknown (D1-04-F09).
- Only two CDSCO Class C digital products found: Lupin Lyfe (cardiac rehab) and Huma (D1-04-F15, F30).
- The government's Simple app stores a drug list and follow-up days, with no step logic (D1-06-F40). Phable shut in Feb 2023 (D1-04-F23).

**Why earlier companies died.** Pear: assets about US$6M against US$130M liabilities, about US$1,195 a course, thin payer base (D1-02-F42, D1-05-F20). Akili: US$523,000 of prescription revenue in 2023 (D1-02-F44). Teva withdrew Digihaler in June 2024 (D1-02-F41). Retention: 3.3% at 30 days for mental-health apps; clinician referral adds 40 days (D1-02-F26, F27).

**What can be built tonight.**
- Blood pressure: exact Gujarat 5-step sheet with thresholds, 30-day re-checks, safety branches (D1-06-F14); Punjab and Maharashtra ladders with control by step for 159,292 patients (D1-06-F01 to F04); a second protocol from Nigeria (D1-06-F15); Omron HEM-7156T about ₹2,600, readable with omblepy (D1-06-F07, F31, prices SNIPPET).
- Insulin: ADA "2 units every 3 days" rule (D1-06-F16); ShanghaiT2DM open data (D1-06-F11); no open type 2 simulator (D1-06-F30).
- Asthma: AAMOS-00 open data, 2,054 patient-days (D1-06-F50); GINA 2025 rules (D1-06-F20 to F22); home-made peak flow is weak, error 18% (D1-06-F24).
- Rehabilitation: MediaPipe Pose (D1-06-F26); start rule resting heart rate plus 20-30 beats, effort 11-14 (D1-06-F36).

## 2. Gates

1. The product changes the therapy itself from device or biomarker feedback.
2. It can be built honestly tonight: kit or phone parts, a clinician or health worker confirms every change, a test on open data, a simulator or teammates.

All seven options pass gate 1. Heart failure and warfarin pass gate 2 only as rule tests, since neither has a device or data tonight.

## 3. Scores (1-5; weights proof 25, market 20, feasibility 20, gap 15, deep-tech 10, low risk 10)

| Option | Proof | Market | Tonight | Gap | Deep-tech | Low risk | Score |
|---|---|---|---|---|---|---|---|
| A. Home blood-pressure step loop | 5 | 4 | 5 | 4 | 3 | 4 | 4.35 |
| B. Insulin dose guidance, type 2 diabetes | 4 | 4 | 3 | 3 | 3 | 2 | 3.35 |
| D. Adaptive home rehabilitation | 3 | 3 | 5 | 2 | 3 | 4 | 3.35 |
| G. Heart-failure dose loop | 4 | 3 | 2 | 4 | 3 | 2 | 3.10 |
| C. Breathing plan with inhaler sensor and air quality | 2 | 3 | 4 | 3 | 4 | 3 | 3.05 |
| F. Warfarin self-dosing | 5 | 2 | 2 | 3 | 2 | 2 | 2.90 |
| E. Weight-loss injection dose companion | 2 | 4 | 3 | 2 | 2 | 3 | 2.70 |

Reasons in one line each:
- **A.** Strongest proof including hard outcomes at scale by non-physicians; largest patient pool; exact Indian protocol text; no Indian service found. Weak spots: who pays, and it can look like "just rules".
- **B.** Good trials and pharma interest. Tonight's test is thin (no type 2 simulator; the open data covers 3-14 days) and low blood sugar is a real hazard. My Dose Coach exists.
- **D.** Easiest demo. Software rehab matches in-person care but does not beat usual care (D1-02-F07, F54); Lupin holds the licence.
- **G.** Strong outcome proof and the best fit to "far from a specialist" (TIM-HF2 benefit grew with distance to a cardiologist, D1-01-F31; only 25% of Trivandrum patients left hospital on all three drug classes, D1-01-F35). Needs lab values, so it cannot be tested honestly tonight. A later protocol for the same engine.
- **C.** Most hardware and the best open data, but the dose change that works needs no sensor, sensor systems showed no clear outcome gain (D1-02-F02), and smart inhalers failed commercially.
- **F.** Best proof of all, small market, no meter tonight.
- **E.** Hot market after generic semaglutide (21-22 Mar 2026, D1-04-F10), but no outcome evidence for digital dose support yet (PHTI reports in 2027, D1-01-F41) and Healthify, BeatO and Tracky are already there.

## 4. Decision

Recommended build: **A, the home blood-pressure step loop**, with an engine that loads any protocol as data, so the insulin rule (B) is shown as "same loop, new protocol" and heart failure (G) is the later expansion.

What makes A more than a rules engine:
1. **Trusting a home reading.** Readings count only if taken properly (rest, posture, arm position, repeat readings, morning and evening). A kit-built clip with a motion sensor checks arm position and stillness. A phone photo of any cheap cuff's screen is read automatically, so no Bluetooth cuff is needed.
2. **Titrate or support.** The protocol says to check the medicine was taken before stepping up (D1-06-F14). The loop asks that question first, using a simple adherence signal, and only then proposes a dose change. Adherence tech alone fails (D1-02-F59); here it is an input to the dose decision, not a reminder.
3. **A safety case.** Every branch of the protocol is tested, every proposal carries its reasons, unsafe cases are sent up, and a clinician approves each change.
4. **Learning later.** Each patient's response to each step becomes data for predicting who needs two drugs sooner.

Round 2 therefore puts both design agents on A (software, and hardware plus measurement). If the user picks another option, a design agent is added for it.

## 4a. Addendum after the last Round 1 note (D1-01 complete)

- **The Indian null result to answer.** mWellcare: cluster trial, 40 community health centres, 3,698 people with hypertension or diabetes; nurse-managed care with an Android decision-support app against enhanced usual care; systolic difference 0.98 mmHg (95% CI -4.64 to 2.67), HbA1c +0.11; both arms fell about 13 mmHg (D1-01-F46). Prompting a clinician during a visit added nothing over a well-run protocol programme.
- **What that means for A.** The loop must earn its value where mWellcare did not look: between visits, from home readings, and among the 49% who do not return (D1-03-F10). The trials that back A are the ones where the dose changed without a clinic visit (D1-01-F02, F04) or where non-physicians were given the authority to step doses (D1-01-F09, F38). The pilot endpoint should be control at 90 days among patients who would not have come back.
- **Two more cautions.** In TASMINH4 telemonitoring added nothing significant over paper self-monitoring once the GP titrated (D1-01-F03), so the electronics are not the active ingredient; the dose change is. The China result also included free or cheap drugs and incentives for village doctors (D1-01-F38 note, SNIPPET), so the protocol alone may do less.
- **Heart failure in India** (for the roadmap): 47.5% of eligible patients received guideline drugs in the national registry, 90-day mortality 14.2%, 1-year 22.1% (D1-01-F47, F48); after a heart attack with weak pumping, use of one drug class fell from 69% to 6% within a year (D1-01-F50).

## 5. Open questions passed to Round 2

- Who pays in India, and a rupee price per patient per month.
- The regulatory class of a dose-proposing tool with clinician sign-off, and what the telemedicine rules allow.
- Home-reading rules from the guidelines (how many readings, over how many days).
- Whether a phone photo of a cuff screen can be read reliably.
- Whether Beyond Next Ventures invested in Wellthy Therapeutics itself (D2-07).
