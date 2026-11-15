# D2-01 Build plan: home blood-pressure step loop, software side (agent: claude-opus-5-5, 2026-11-13)

Scope: engine, protocol data, interfaces, tests, simulated cohort, story. Hardware and measurement science are in D2-02. Fact IDs from Round 1 notes are reused as given (D1-0x-Fn). New facts carry D2-01-Fn and are listed in the fact register at the end. Anything from our own reasoning is marked OUR DESIGN. OUR SIMULATION means a model we wrote, not data. ASSUMPTION marks every business or model input we chose.

## Digest

- Build: a protocol-agnostic step engine (YAML protocol files, one pure Python decision function), a Telegram patient bot with a plain web form as fallback, a one-tap clinician queue, and a test plus simulation page. Python, FastAPI, SQLite. No LLM in the dose path. OUR DESIGN.
- Protocol: the Gujarat HEARTS sheet (D1-06-F14) is written out in full as data, with the Nigeria losartan sheet (D1-06-F15) as a second file and the ADA basal-insulin rule (D1-06-F16) as a paper-only third file.
- The "titrate or support" check comes from the sheet itself: "Check for compliance at each visit before titration of dose or addition of drugs" (D1-06-F14).
- Home rules: ESH 2021 says "Seven-day monitoring (not fewer than 3 days)", with "Duplicate morning and evening measurements"; the home threshold is 135/85 against 140/90 in clinic (D2-01-F1, F3, F4). The Indian sheet is written for clinic readings, so mapping it to 135/85 at home is OUR DESIGN and must be said aloud.
- US programmes that change drugs remotely report big falls: Mass General Brigham -8.7/-3.8 mmHg at 6 months against -1.5/-0.7 (non-randomised), with about 45% dropping out or unreachable (D2-01-F5). Ochsner reports control rising from 57.1% to 76.1% and from 61.3% to 77.7% (D2-01-F6). PHTI rates only medication management as clinically meaningful (D1-05-F1, F2).
- OUR SIMULATION (Punjab step curve, 51% monthly return, 30-day refills): 12-month control is 39.0% with clinic-only follow-up. With the home loop it is 49.1%, 55.0% or 59.8% at 30%, 50% or 70% monthly engagement. Most of the gain comes from contact and refills, not from extra steps. Non-adherent step-ups fall from 47.6 to 25.3 per 100 patients. These figures depend on the assumptions and do not show an effect.
- Money: in the public sector, drugs cost "as low as Rs 200 per patient per year" (D2-01-F12), so a state will not pay app-scale prices. Our ASSUMPTION is ₹149 per patient per month sold to private clinics and hospital chains, with a ₹10 to ₹20 public tier later.
- Regulatory: CDSCO's draft software guidance (21 Oct 2025) classes clinical decision software by intended use (D2-01-F11, SNIPPET). A dose-proposing tool is likely a licensed device, not a wellness app.
- Not sourced: the 2025 AHA/ACC home schedule text, the exact Indian Guidelines IV home wording, the WhatsApp per-message price in India, and Cadence or Story Health outcome numbers.

## 1. The problem in one paragraph

India treats hypertension with a simple published ladder: amlodipine 5 mg, then 10 mg, then telmisartan, then a diuretic, each step 30 days apart (D1-06-F14). The ladder works when patients come back. In the IHCI cohort only 51% of 21,895 registered patients returned for follow-up, but among those who returned control rose from 26.3% to 59.8% (D1-03-F10). Across nine IHCI districts, community control was still 21.2% in 2023-24 (D1-01-F11). The step that fails is the return visit, where someone reads the pressure, checks the pills were taken and moves one rung up. A rural primary-care consultation lasts about 2 minutes (D1-03-F24), and 79.9% of specialist posts at rural community health centres are empty (D1-03-F16). Trials abroad show the fix: home readings that drive a dose change, not home readings alone. Self-monitoring alone gave -1.0 mmHg, and with systematic titration -6.1 mmHg (D1-01-F05). Village doctors titrating by protocol in China cut cardiovascular events (HR 0.75 at age 60+, 0.64 under 60) (D1-01-F38).

Two strongest Indian numbers: **51% return rate, with control 26.3% to 59.8% among returners** (D1-03-F10, https://pmc.ncbi.nlm.nih.gov/articles/PMC8678731/), and **21.2% controlled in IHCI districts in 2023-24** (D1-01-F11, https://pubmed.ncbi.nlm.nih.gov/42827825/).

## 2. How the system works

### 2.1 The loop (OUR DESIGN)

```
 Patient at home                 Engine (server)                       Doctor (phone or laptop)
 ---------------                 ---------------                       ------------------------
 cuff reading  --photo/BLE/typed--> 1. quality gate (D2-02 flags)
 (2 AM + 2 PM, 7 days)              2. safety screen (very high, pregnancy, low)
                                    3. enough valid days?  -- no --> "please take 2 more days"
                                    4. 30 days since last change?  -- no --> "keep going"
                                    5. home mean (day 1 dropped) >= 135/85?
                                         no  --> "on target, same medicine" (no doctor needed)
                                         yes --> 6. ADHERENCE QUESTION (titrate or support)
                                                   missed doses --> SUPPORT proposal ----+
                                                   took all     --> 7. next protocol step |
                                                                       + guards (labs,     |
                                                                         pregnancy, last   |
                                                                         step -> refer)    |
                                    8. proposal card with reasons ----------------------->  approve / edit / reject (one tap)
 message in own language  <------- 9. on approve: render template in patient's language,
 ("from today: amlodipine 10 mg")      log, set next check in 30 days
```

### 2.2 Data flow

1. Reading enters by one of three routes: a Bluetooth cuff read through omblepy (D1-06-F07), a photo of any cuff's screen read automatically (D2-02 covers accuracy), or typed numbers as a fallback. Each reading is stored with its timestamp, its route and D2-02's quality flags: rest, posture, arm still, repeat reading.
2. Each 30-day cycle the engine asks for a 7-day measurement block in days 23 to 30 (OUR DESIGN, following ESH "7 days before each clinic visit", D2-01-F1).
3. At cycle end, or at once for a very high reading, the engine runs `decide()` (section 3b) on the patient state, the readings window and the protocol file.
4. The output is a **proposal**. It is never sent to the patient directly, except "keep going" and "please measure" prompts that change no treatment.
5. A clinician sees a queue of proposal cards, each with: patient, current step, 7-day mean and the readings, the adherence answer, the exact protocol line that applies, the proposed change, and the guards checked. One tap approves. Edit and reject need a reason.
6. On approval the patient gets the change from a pre-written template in their language, and the engine logs the step, the time to approve and the time to deliver.

### 2.3 Who approves what (OUR DESIGN)

| Event | Engine does | Human needed |
|---|---|---|
| Reading on target | Tells patient "same medicine, next check on <date>" | No (no treatment change) |
| Not enough readings | Asks for more | No |
| Uncontrolled + missed doses | Sends adherence support (why it matters, pill timing, refill place), proposes "no step-up" | Clinician sees it in queue as FYI and can override |
| Uncontrolled + adherent | Proposes the next protocol step | Clinician approves every step |
| Lab check required (before telmisartan 80) | Proposes "order blood sugar, urea, creatinine, urine protein" | Clinician approves the lab order |
| Pregnancy flag + step blocked | Proposes "refer, protocol bars telmisartan and chlorthalidone" | Clinician |
| Very high reading (>= 180/110) | Asks for a repeat reading after rest; if still high, urgent card + tells patient to contact clinic today | Clinician, urgent |
| Last step reached and still high | Adherence check, then proposes specialist referral | Clinician |

### 2.4 Titrate or support

The Gujarat sheet says "Check for compliance at each visit before titration of dose or addition of drugs" and, after step 5, "Check if the patient has been taking medications regularly and correctly. If yes, refer to a specialist." (D1-06-F14). The engine makes this an input to the decision.
- Signal tonight: two chat questions with buttons. "In the last 7 days, how many days did you miss your BP tablet? 0 / 1-2 / 3 or more" and "Do you have tablets left for the next 7 days? yes / no". Adherent = 0 missed days (OUR DESIGN; the sheet gives no cut-off, so the clinician can change it in the protocol file).
- Later signals: refill dates from the dispensing record, and a pill-photo count. These are NOT built tonight.
- Why this matters: a reminder app alone gave -0.5 mmHg (D1-01-F06), and pillboxes alone gave no outcome gain (D1-02-F59). Here adherence is not a reminder. It decides between two treatment actions: step up the dose, or keep the dose and fix intake. That avoids raising the dose for a patient who is not taking the first one. In India pooled non-adherence to BP drugs is about 48%, a figure that depends heavily on definition (D1-03-F44, SNIPPET).

### 2.5 What the patient sees (Telegram, English shown; Hindi and one more language as templates)

```
Bot: Good morning Asha. Please sit quietly for 5 minutes, then take 2 readings, 1 minute apart. Send a photo of the screen.
Bot: Thank you. 2 good readings saved (6 of 14 this week).
...
Bot: Your doctor reviewed your readings. Your average this week was 146/92, above the target.
     From tomorrow: Amlodipine 10 mg, one tablet each morning (in place of 5 mg).
     Next check: 7 days of readings from 6 Dec. If you feel dizzy or faint, call the clinic: <number>.
     [I understand]  [I have a question]
```
Every treatment message ends with "approved by Dr <name> on <date>". OUR DESIGN.

## 3. The engineering core

### 3a. A protocol as data

**Schema (OUR DESIGN).** One YAML file per protocol. The engine knows only these keys. Every number carries a `text` field holding the exact source words, or a `source` field naming a fact ID. A key with `null` means "not in the source": the engine refuses to run that branch until a clinician fills it in. The biology student owns these files.

```yaml
# schema v0.1 (OUR DESIGN)
id: str                     # unique id
name: str
kind: ladder | dose_titration
measure: bp | fpg           # what reading drives it
source: {url, doc, fact_id}
status: demo | paper_only
thresholds:                 # what counts as "still high"
  clinic_high: {sbp, dbp, rule: any|both, text}
  home_high:   {sbp, dbp, rule, source, note}
reading_window: {days_min, days_target, per_session, sessions_per_day, drop_first_day, source}
review_interval_days: int   # minimum days on a step before the next step
pre_titration_check: adherence | none
adherence_rule: {missed_days_max: int, set_by: clinician|protocol}
entry_rules: [ {when: {sbp_gte|sbp_range|dbp_gte|dbp_range}, action, text} ]   # new, untreated patients (clinic)
steps:
  - n: int
    regimen: [ {drug, dose_mg, freq} ]   # the FULL regimen on this step, not a diff
    text: str                            # exact sheet wording
    requires: [ {lab: str, max_age_days: int|null} ]   # guards before moving INTO this step
    substitutes: [ {drug, dose_mg, if: str, text} ]
after_last_step: {action: adherence_then_refer|refer, text}
contraindications:
  - when: pregnancy|...
    blocked_drugs: [str]
    action: block_step_and_refer
    text: str
safety:
  very_high: {sbp_gte, dbp_gte, rule, action, text}
  low:       {sbp_lt: null, action: urgent_review, note}   # null until a clinician sets it
messages: {lang: {template_id: str}}     # patient text per action, per language
```

**State machine (OUR DESIGN).** Per patient:

```
ENROLLED -> ON_STEP(n) -> [cycle end] -> one of
   HOLD (controlled)              -> ON_STEP(n)            (no approval)
   NEED_READINGS                  -> ON_STEP(n)            (no approval)
   SUPPORT (non-adherent)         -> ON_STEP(n)            (FYI to clinician)
   PROPOSE_STEP(n+1)  --approve-->  ON_STEP(n+1)
   PROPOSE_LABS       --approve-->  AWAIT_LABS --labs in--> re-run decide()
   PROPOSE_REFER      --approve-->  REFERRED (loop pauses)
   URGENT (very high, confirmed)  --clinician acts--> any state
   BLOCKED (pregnancy guard)      --> PROPOSE_REFER
 any PROPOSE_* --reject(reason)--> ON_STEP(n), next cycle
```

#### File 1: `protocols/in_gujarat_hearts.yaml` (from D1-06-F14, all quoted text exactly as the note quotes it)

```yaml
id: in_gujarat_hearts_2025
name: Gujarat hypertension protocol (WHO HEARTS, India)
kind: ladder
measure: bp
status: demo
source:
  url: https://resolvetosavelives.org/wp-content/uploads/2025/02/759_CVH_HEARTS-in-India_Fact-Sheet_0225_Rev-A_v10.pdf
  doc: "759_CVH_0225_Rev A (Feb 2025)"
  fact_id: D1-06-F14
  extraction_note: ">= symbols lost in PDF extraction; 'SBP 140' read as SBP >= 140 (D1-06-F14)"
thresholds:
  clinic_high: {sbp: 140, dbp: 90, rule: any, text: "High BP: SBP 140 or DBP 90 mmHg"}
  home_high:
    sbp: 135
    dbp: 85
    rule: any
    source: [D2-01-F1, D2-01-F3, D2-01-F4]
    note: "OUR DESIGN mapping. The sheet is written for clinic readings. ESH 2021 says home >=135/85 corresponds to office 140/90."
reading_window: {days_min: 3, days_target: 7, per_session: 2, sessions_per_day: 2, drop_first_day: true, source: D2-01-F1}
review_interval_days: 30
review_text: "After 30 days measure BP again."
dispense_text: "Dispense drugs for 30 days and give appointment after 4 weeks"
pre_titration_check: adherence
pre_titration_text: "Check for compliance at each visit before titration of dose or addition of drugs"
adherence_rule: {missed_days_max: 0, set_by: clinician}   # OUR DESIGN default; sheet gives no cut-off
entry_rules:   # untreated patients at a clinic visit; the home loop starts after step 1 is prescribed
  - when: {sbp_gte: 180, or_dbp_gte: 110}
    action: start_step_1_and_refer
    text: "If SBP 180 or DBP 110, refer patient to a specialist after starting treatment"
  - when: {sbp_range: [160, 179], or_dbp_range: [100, 109]}
    action: start_step_1_same_day
    text: "If SBP 160-179 or DBP 100-109, start treatment on the same day"
  - when: {sbp_range: [140, 159], or_dbp_range: [90, 99]}
    action: recheck_other_day_then_start
    text: "If SBP 140-159 or DBP 90-99, check on a different day and if still elevated, start treatment"
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
    requires:
      - {lab: blood_sugar, max_age_days: null}
      - {lab: urea, max_age_days: null}
      - {lab: creatinine, max_age_days: null}
      - {lab: urine_protein, max_age_days: null}
    requires_text: "** blood sugar, urea, creatinine, urine protein before raising telmisartan"   # as summarised in D1-06-F14
    requires_note: "max_age_days is not in the sheet; null until the clinician sets it"
  - n: 5
    regimen: [{drug: amlodipine, dose_mg: 10}, {drug: telmisartan, dose_mg: 80}, {drug: chlorthalidone, dose_mg: 12.5}]
    text: "Add Chlorthalidone 12.5mg***"
    substitutes:
      - {drug: hydrochlorothiazide, dose_mg: 25, if: chlorthalidone_unavailable,
         text: "Hydrochlorothiazide 25 mg can be used if Chlorthalidone 12.5 mg is not available"}
after_last_step:
  action: adherence_then_refer
  text: "Check if the patient has been taking medications regularly and correctly. If yes, refer to a specialist."
contraindications:
  - when: pregnancy
    blocked_drugs: [telmisartan, chlorthalidone]
    action: block_step_and_refer      # OUR DESIGN: the sheet does not say what to give instead
    text: "DO NOT give Telmisartan or Chlorthalidone."
safety:
  very_high:
    sbp_gte: 180
    dbp_gte: 110
    rule: any
    action: repeat_then_urgent_review   # OUR DESIGN for a HOME reading; the sheet's line is for clinic entry
    text: "If SBP 180 or DBP 110, refer patient to a specialist after starting treatment"
  low:
    sbp_lt: null
    action: urgent_review
    note: "Not in the sheet. Threshold must be set by the supervising clinician before any real use."
```

Note on step 3: the sheet says "Add Telmisartan 40mg" after step 2's amlodipine 10 mg, so the regimen keeps amlodipine 10 mg. Note on IHCI variants: Punjab follows this order, while Maharashtra adds telmisartan at step 2 (D1-06-F01, F02). A Maharashtra file is a 10-minute copy if wanted.

#### File 2: `protocols/ng_hearts_losartan.yaml` (from D1-06-F15)

```yaml
id: ng_hearts_losartan_2019
name: HEARTS-model hypertension protocol, losartan variant (Nigeria)
kind: ladder
measure: bp
status: demo
source:
  url: https://resolvetosavelives.org/wp-content/uploads/2023/05/nigeria-hypertension-protocol-04-1.pdf
  fact_id: D1-06-F15
  note: "PDF metadata title says Bangladesh, created 4 Dec 2019 (D1-06-F15)"
thresholds:
  clinic_high: {sbp: null, dbp: null, rule: any,
                note: "Target / 'still high' cut-off is not in the D1-06-F15 quote. Biology student: read it from the PDF tonight. Engine refuses to run until set."}
  home_high: {sbp: 135, dbp: 85, rule: any, source: [D2-01-F1], note: "OUR DESIGN mapping, same as file 1"}
reading_window: {days_min: 3, days_target: 7, per_session: 2, sessions_per_day: 2, drop_first_day: true, source: D2-01-F1}
review_interval_days: 30          # "After 1 month"
review_text: "After 1 month, measure BP again."
pre_titration_check: none         # not in the D1-06-F15 quote
entry_rules:
  - when: {sbp_gte: 180, or_dbp_gte: 110}
    action: start_step_3_and_refer_emergency
    text: ">=180/110 give step 3 drugs and refer to emergency \"within 1 hour\""   # as summarised in D1-06-F15
  - when: {sbp_gte: 160, or_dbp_gte: 100}
    action: start_step_2
    text: "Initial >=160/100 start at Step 2"                                  # as summarised in D1-06-F15
steps:
  - n: 1
    regimen: [{drug: amlodipine, dose_mg: 5}]
    text: "Start amlodipine 5 mg."
  - n: 2
    regimen: [{drug: amlodipine, dose_mg: 5}, {drug: losartan, dose_mg: 50}]
    text: "After 1 month, measure BP again. If still high, Treat with amlodipine 5 mg + losartan 50 mg."
  - n: 3
    regimen: [{drug: amlodipine, dose_mg: 10}, {drug: losartan, dose_mg: 100}]
    text: "amlodipine 10 mg + losartan 100 mg"              # as summarised in D1-06-F15
  - n: 4
    regimen: [{drug: amlodipine, dose_mg: 10}, {drug: losartan, dose_mg: 100}, {drug: hydrochlorothiazide, dose_mg: 25}]
    text: "+ HCTZ 25 mg"                                     # as summarised in D1-06-F15
after_last_step:
  action: refer
  text: "Refer for specialist hypertension management."
contraindications: []   # pregnancy rule not in the D1-06-F15 quote; check the PDF
safety:
  very_high: {sbp_gte: 180, dbp_gte: 110, rule: any, action: repeat_then_urgent_review,
              text: ">=180/110 ... refer to emergency \"within 1 hour\""}
  low: {sbp_lt: null, action: urgent_review}
```

Why this file matters: the same `decide()` runs it with no code change. The test suite runs every case against both files. Differences in behaviour come from data alone: a different entry step, a different step-2 drug, no adherence pre-check, and an emergency referral.

#### File 3: `protocols/ada_basal_insulin.yaml` (PAPER ONLY, from D1-06-F16; never run on a person)

```yaml
id: ada_2025_basal_insulin
name: ADA Standards of Care 2025, Figure 9.4, basal insulin titration (paper only)
kind: dose_titration
measure: fpg
status: paper_only
source:
  url: https://diabetesed.net/wp-content/uploads/2024/12/ADA-2025-Instensifying-Injectable-Therapy_v2.pdf
  fact_id: D1-06-F16
start:
  options:
    - {dose_units_per_day: 10, text: "Start 10 units a day"}
    - {dose_units_per_kg_per_day: [0.1, 0.2], text: "OR 0.1-0.2 units/kg a day"}
target:
  fpg_mg_dl: [80, 130]
  source: D1-06-F17
  text: "Pre-prandial capillary plasma glucose: 80-130 mg/dl"   # ICMR STW; ADA figure target value not quoted in D1-06-F16
titration:
  step_units: 2
  every_days: 3
  text: "increase 2 units every 3 days to reach FPG target without hypoglycemia"
  upper_limit_units_per_kg: 0.5
  upper_limit_source: "D1-06-F18 (SNIPPET, '2 x 3 rule' upper limit 0.5 units/kg/day)"
hypoglycaemia:
  action: clinician_determines_cause
  if_no_clear_cause: {reduce_pct: [10, 20]}
  text: "For hypoglycemia determine cause. If no clear reason lower dose by 10-20%"
  hypo_threshold_mg_dl: null   # not quoted in D1-06-F16; must come from the full ADA text
```

Use on the slide: "same engine, new file: the step becomes '+2 units', the interval becomes 3 days, the safety branch becomes hypoglycaemia". Tonight it is shown as YAML and unit tests only, with no patient-facing messages.

### 3b. The decision function (pseudocode, OUR DESIGN)

```python
def decide(protocol, patient, readings, now, adherence_answer=None) -> Proposal:
    # patient: step, last_change_at, pregnant, labs{name: date}, lang, status
    reasons = []

    # 0. paused states
    if patient.status in ("REFERRED", "AWAIT_LABS_PENDING"):
        return Proposal("NONE", reasons=["loop paused: " + patient.status])

    valid = [r for r in readings if r.quality_ok]           # D2-02 flags
    latest = latest_session_mean(valid)                     # mean of the 2 readings in the newest session

    # 1. safety first, on any single session
    vh = protocol.safety.very_high
    if latest and exceeds(latest, vh):
        if not latest.is_confirmed_repeat:
            return Proposal("ASK_REPEAT", reasons=[f"session {latest} >= {vh}"], msg="repeat_after_rest")
        return Proposal("URGENT_REVIEW", needs_approval=True, urgent=True,
                        reasons=[vh.text, f"confirmed {latest}"], msg="contact_clinic_today")
    low = protocol.safety.low
    if low.sbp_lt is not None and latest and latest.sbp < low.sbp_lt:
        return Proposal("URGENT_REVIEW", needs_approval=True, urgent=True, reasons=["low reading"])

    # 2. enough readings?
    w = protocol.reading_window
    window = readings_in_last_days(valid, w.days_target, now)
    days = distinct_days(window)
    if len(days) < w.days_min:
        return Proposal("NEED_READINGS", reasons=[f"{len(days)} valid days < {w.days_min}"], msg="please_measure")
    if w.drop_first_day and len(days) > w.days_min:          # OUR DESIGN: keep >= days_min after dropping
        window = [r for r in window if r.day != days[0]]
    mean = mean_bp(window)

    # 3. interval
    if (now - patient.last_change_at).days < protocol.review_interval_days:
        return Proposal("HOLD", reasons=[f"on step < {protocol.review_interval_days} days"], msg="keep_going")

    # 4. controlled?
    th = protocol.thresholds.home_high
    if th.sbp is None:
        raise ProtocolIncomplete("home threshold not set")
    if not exceeds(mean, th):
        return Proposal("HOLD", reasons=[f"home mean {mean} < {th.sbp}/{th.dbp}"], msg="on_target")
    reasons.append(f"home mean {mean} >= {th.sbp}/{th.dbp} over {len(days)} days")

    # 5. titrate or support
    if protocol.pre_titration_check == "adherence":
        if adherence_answer is None:
            return Proposal("ASK_ADHERENCE", msg="adherence_question")
        if adherence_answer.missed_days > protocol.adherence_rule.missed_days_max or not adherence_answer.has_stock:
            return Proposal("SUPPORT", needs_approval=False, fyi=True,
                            reasons=reasons + [protocol.pre_titration_text, f"missed {adherence_answer.missed_days} days"],
                            msg="adherence_support")

    # 6. last step?
    nxt = protocol.step(patient.step + 1)
    if nxt is None:
        return Proposal("REFER", needs_approval=True, reasons=reasons + [protocol.after_last_step.text], msg="referral")

    # 7. guards on the next step
    for c in protocol.contraindications:
        if patient.has(c.when) and set(nxt.drugs) & set(c.blocked_drugs):
            return Proposal("REFER", needs_approval=True, reasons=reasons + [c.text], blocked_step=nxt.n)
    missing = [q.lab for q in nxt.requires if not patient.has_lab(q.lab, q.max_age_days, now)]
    if missing:
        return Proposal("ORDER_LABS", needs_approval=True, labs=missing, reasons=reasons + [nxt.requires_text])

    # 8. propose the step
    regimen = apply_substitutes(nxt, patient.unavailable_drugs)
    return Proposal("STEP_UP", needs_approval=True, from_step=patient.step, to_step=nxt.n,
                    regimen=regimen, reasons=reasons + [nxt.text], msg="step_change")
```

Rules the code must keep (OUR DESIGN): `decide()` is pure: no I/O, no clock reads, no randomness. Every `Proposal` carries `reasons` that quote the protocol line. Nothing with `needs_approval=True` reaches the patient until a clinician has approved it. The function never computes a dose. It can only pick a regimen that is written in the file.

### 3c. Test cases (one per branch; run against file 1, and against file 2 where marked)

Readings are home session means. "7d" means 7 valid days of AM and PM duplicates. Step-change dates are set so the 30-day interval has passed unless stated.

| # | Patient state | Readings / input | Expected proposal | Branch |
|---|---|---|---|---|
| T1 | Step 1, 35 days on step | 7d mean 128/80 | HOLD, "on_target" | controlled |
| T2 | Step 1, 35 days | 7d mean 135/80 | ASK_ADHERENCE (135 counts as high: >=) | threshold edge, SBP |
| T3 | Step 1, 35 days | 7d mean 130/85 | ASK_ADHERENCE | threshold edge, DBP, rule any |
| T4 | Step 1, 35 days | 7d mean 134/84 | HOLD | just below |
| T5 | Step 1, 35 days | 2 valid days only | NEED_READINGS | too few days |
| T6 | Step 1, 20 days | 7d mean 150/95 | HOLD "keep_going" | 30-day interval |
| T7 | Step 1, 35 days | 7d 150/95, adherence: missed 3 days | SUPPORT (FYI), no step | titrate or support |
| T8 | Step 1, 35 days | 7d 150/95, missed 0, has stock | STEP_UP 1 to 2: amlodipine 10 mg | step 2 |
| T9 | Step 2 | 7d 148/92, adherent | STEP_UP 2 to 3: amlodipine 10 + telmisartan 40 | step 3 |
| T10 | Step 3, no labs on file | 7d 146/90, adherent | ORDER_LABS [blood_sugar, urea, creatinine, urine_protein] | lab guard |
| T11 | Step 3, all 4 labs on file | 7d 146/90, adherent | STEP_UP 3 to 4: telmisartan 80 | step 4 |
| T12 | Step 4 | 7d 144/90, adherent | STEP_UP 4 to 5: + chlorthalidone 12.5 | step 5 |
| T13 | Step 4, chlorthalidone unavailable | 7d 144/90, adherent | STEP_UP 4 to 5 with hydrochlorothiazide 25 mg | substitute |
| T14 | Step 5 | 7d 142/90, adherent | REFER, after_last_step text | last step |
| T15 | Step 5 | 7d 142/90, missed 2 days | SUPPORT | adherence before referral |
| T16 | Step 2, pregnant | 7d 150/95, adherent | REFER, blocked step 3, "DO NOT give Telmisartan or Chlorthalidone." | pregnancy |
| T17 | Step 1, pregnant | 7d 150/95, adherent | STEP_UP to amlodipine 10 (not blocked) | pregnancy, unblocked drug |
| T18 | Step 2 | single session 186/100, not repeated | ASK_REPEAT | very high, unconfirmed |
| T19 | Step 2 | repeat session 184/112 | URGENT_REVIEW | very high, confirmed |
| T20 | Step 2 | session 150/112 confirmed | URGENT_REVIEW (DBP alone) | very high, DBP |
| T21 | Step 2, 10 days on step | confirmed 182/100 | URGENT_REVIEW (safety beats interval) | order of checks |
| T22 | Any | readings with quality flag "arm moving" only | NEED_READINGS | quality gate |
| T23 | Status REFERRED | anything | NONE | paused |
| T24 | Step 1 | 4 days; day 1 mean 160/100, days 2-4 mean 130/80 | HOLD (day 1 dropped) | drop first day |
| T25 | Step 1 | 3 days; day 1 high, days 2-3 normal | uses all 3 days (cannot drop below days_min) | drop-first-day limit |
| T26 | Low threshold null | session 85/50 | no low branch fires; LOG warning "low threshold unset" | unset safety param |
| T27 | Entry: untreated, clinic 182/96 | - | start_step_1_and_refer | entry >=180 |
| T28 | Entry: clinic 165/95 | - | start_step_1_same_day | entry 160-179 |
| T29 | Entry: clinic 145/92 | - | recheck_other_day_then_start | entry 140-159 |
| T30 | File 2, step 1 | 7d 150/95 | STEP_UP to amlodipine 5 + losartan 50, with no adherence question | protocol-agnostic |
| T31 | File 2, step 4 | 7d 150/95 | REFER "Refer for specialist hypertension management." | file 2 last step |
| T32 | File 2, entry 165/102 | - | start_step_2 | file 2 entry |
| T33 | File 2, clinic threshold null | run clinic-mode check | raises ProtocolIncomplete | refuses incomplete data |
| T34 | Clinician rejects T8 with reason | - | state stays step 1; proposal logged rejected | approval path |
| T35 | File 3 (paper) | FPG 160 for 3 days, dose 10 U | proposal +2 U (12 U); never sent to a patient (status paper_only) | insulin rule |
| T36 | File 3 | hypo event, cause "none" | proposal reduce 10-20% (range shown, clinician picks) | insulin hypo |

Coverage target: every key in each YAML file is read by at least one test. Measure line and branch coverage of `decide()` with `pytest --cov --cov-branch`. The report is result (i) in section 7.

### 3d. Learning layer: what is real tonight and what comes later

Real tonight:
- Deterministic protocol engine, tests, audit log.
- One small piece of measurement ML from D2-02: reading the cuff screen from a photo (digit OCR), with a confidence score that sends doubtful readings back to the patient. Its accuracy belongs to D2-02.
- The simulated cohort (section 7), which is OUR SIMULATION and not learning.

Honest later (needs months of data from real patients):
1. **Predicting response to the next step.** Each approved step yields one labelled example: features before the step (home mean, variability, age, step, adherence answers, step history), and the outcome (home mean 30 days later, controlled yes or no). With a few thousand step-events, a gradient-boosted model or a hierarchical Bayesian model could estimate "chance this patient is controlled on step n+1". The use: flag patients unlikely to respond to amlodipine 10 mg, so the clinician can consider an earlier second drug. That choice belongs to the clinician and stays inside the protocol's options. The F04 curve already shows most gain comes at step 1 and later steps add only 2 to 5 points (D1-06-F04), so the model's value would come from spotting the 23% to 18% who never reach control on the ladder. No open home-BP-with-medication dataset exists to train it now (D1-06-F42).
2. **Choosing message timing and wording.** A contextual bandit picks the reminder hour and the framing that most often produce a complete 7-day block. MABWiser (Apache 2.0, D1-06-F55) can be replayed offline on HeartSteps V1 (CC BY, D1-06-F44) as a method demo, but HeartSteps is activity nudging in 37 US participants, not BP.
3. **Reading-quality scoring.** Combine motion, posture and time-of-day flags (D2-02) into a weight per reading rather than a yes/no gate.
4. **Risk of loss to follow-up.** Predict who will stop sending readings, so health workers call them first. This targets the 51% return gap directly.

What the team must not claim: that any model chooses doses, or that the prototype "learns". On the slide, the engine is rules and the learning comes later.

## 4. Home-reading logic

### 4.1 What the guidelines say

| Source | Schedule | Home threshold | Status |
|---|---|---|---|
| ESH 2021 position paper on home BP (Parati, Stergiou, Bilo et al., J Hypertens 39(9):1742-1767) | "Seven-day monitoring (not fewer than 3 days)"; "Duplicate morning and evening measurements"; "After a 5 min sitting rest and 1 min between measurements", before drug intake if treated; discarding day 1 "is matter of debate"; long-term: "7 days before each clinic visit" | >=135/85, which the paper says corresponds to office 140/90 | D2-01-F1, OPENED |
| ESH 2023 guideline | Secondary summaries and an Omron leaflet repeat 3 to 7 days, duplicate AM and PM, day 1 dropped | 135/85 | D2-01-F2, SNIPPET (guideline text not opened) |
| ISH 2020 (via AAFP summary, 15 Jun 2021) | Schedule not stated in the summary; a reproduced ISH table says the average "after excluding readings of the first day" counts (SNIPPET) | "hypertension is diagnosed if readings are consistently 135/85 mm Hg or greater" | D2-01-F3, OPENED (AAFP) |
| AHA | 2019 AHA statement as quoted by a consumer site: 2 readings AM and 2 PM, preferably 7 days, first day often excluded. The 2025 AHA/ACC guideline's own schedule was NOT FOUND. The 2025 guideline keeps 130/80 as its hypertension line | not opened | D2-01-F2b, SNIPPET |
| Indian Guidelines on Hypertension IV (2019; J Hum Hypertens 2020) | NOT FOUND | "the threshold for diagnosis by HBPM mean and daytime ABPM is >135/85 mm of Hg" (summary snippet); office ">140/90" | D2-01-F4, SNIPPET |
| Gujarat HEARTS sheet | Clinic only: "After 30 days measure BP again" | clinic "SBP 140 or DBP 90" | D1-06-F14 |

Key points for the team:
- Home thresholds are lower than clinic thresholds. 135/85 at home corresponds to 140/90 in clinic (D2-01-F1).
- The Indian protocol is written for clinic readings. Using it on home readings is OUR DESIGN, so say so on the slide.
- ESH warns against self-adjusting medication without physician guidance (D2-01-F1). Clinician approval of every step fits this.

### 4.2 The rule the engine uses (OUR DESIGN, from D2-01-F1)

1. **Block:** in each 30-day cycle, the patient measures on days 24 to 30: two readings 1 minute apart after 5 minutes seated rest, morning (before tablets) and evening.
2. **Valid reading:** passes D2-02's quality flags. A session counts if both readings are valid. Its value is the mean of the two.
3. **Enough:** at least 3 distinct days with at least one valid session, aiming for 7 (ESH "not fewer than 3 days").
4. **Day 1:** drop day 1 when 4 or more valid days remain afterwards. Otherwise keep it (ESH calls dropping it debated, with minimal impact over more days).
5. **Still high:** mean SBP >= 135 OR mean DBP >= 85 across the block.
6. **Very high:** any single session >= 180 or >= 110 (the sheet's referral threshold, D1-06-F14). This triggers a repeat after 5 minutes. If confirmed, it goes to URGENT_REVIEW immediately, without waiting for the block.
7. **Clinic reading override:** if a clinic reading is entered during the cycle, the proposal card shows both. The clinician decides. The engine does not merge them.

Open question for D2-02 and the biology student: the white-coat gap and the ESH 135/85 equivalence come from European data. No Indian home-vs-clinic offset was searched (NOT SEARCHED).

## 5. Why India needs its own version, and who has tried

### 5.1 US programmes that adjust medication remotely

| Programme | Who changes the drug | Result reported | Evidence quality | Fact |
|---|---|---|---|---|
| Mass General Brigham remote hypertension programme | Non-licensed navigators and pharmacists using standard algorithms; pharmacists prescribe under collaborative agreements; off-algorithm changes go to a supervising physician | 3,658 enrolled. Clinic SBP/DBP -8.7/-3.8 at 6 months and -9.7/-5.2 at 12 months, against -1.5/-0.7 and +0.2/-1.9 in an education-only group (P<.001). About 41% reached goal; about 45% dropped out, were unreachable or returned to primary care (OUR ARITHMETIC from page counts, which conflict slightly with the paper's Table 2) | Prospective QI cohort, non-randomised, JAMA Cardiol, 9 Nov 2022 | D2-01-F5 |
| Ochsner Digital Medicine | Pharmacists and a licensed clinician adjust drugs from Bluetooth cuff readings; health coaches support lifestyle | 5,057 Medicare patients, 2019-2023: control rose from 57.1% to 76.1% (Black patients) and from 61.3% to 77.7% (white patients) | Retrospective, propensity-matched, difference-in-differences, JGIM (news release 17 Nov 2025) | D2-01-F6 |
| Ochsner (own case study) | as above | 79% against 26% control vs propensity-matched usual care | THEIR CLAIM, SNIPPET (AMA page) | D2-01-F7 |
| HyperLink (Minneapolis) | Pharmacists adjust from home telemonitoring | 57.2% against 30.0% controlled; SBP -10.7 at 6 months | Cluster RCT | D1-01-F04 |
| PHTI category verdict (Cadence, Ochsner, Story Health) | Virtual care team including a prescriber | "Clinically meaningful and more rapid declines in SBP"; "evidence supports broader adoption"; monitoring-only and behaviour-change groups not meaningful | Independent assessment, Oct 2024 | D1-05-F1, F2; D1-01-F39 |

Cadence and Story Health outcome numbers: NOT SEARCHED.

What these programmes have in common is a paid pharmacist or navigator workforce plus US reimbursement. MGB shows the weak spot: about 45% dropout. An Indian version cannot assume a pharmacist per patient panel. The scarce resource is the doctor's 2 minutes (D1-03-F24).

### 5.2 Who has tried in India and the gap

- **Government IHCI and the Simple app:** stores a drug list and `follow_up_days`, flags overdue patients and sends reminders, but has no step logic (D1-06-F40; D1-04-F19). Adaptive depth 2. More than 2.5 million patients were enrolled by April 2022, and 47% of those under care were controlled in Q1 2021 (D2-01-F12).
- **mWellcare:** nurse decision-support prompts across 40 CHCs gave a null result for BP (D1-01-F46). Lesson: prompts that a busy clinician may ignore are not a loop. Our design differs because the engine drafts the exact change and the patient message, so the clinician only taps.
- **Private players:** Phable (shut Feb 2023), BeatO, Sugar.fit, Twin and others sit at adaptive depth 2 to 3. No private home-BP titration service was found (D1-04 Digest; D1-04-F14, F23).
- **Trials:** EASE-BP, an open-label RCT of BP self-monitoring in Indian primary care (CTRI/2023/02/049949), has a published protocol (Oct 2024) but its results were NOT FOUND (D2-01-F14, SNIPPET). SMARThealth India was a stepped-wedge cluster trial of health-worker decision support in rural Andhra Pradesh; its result was not opened (D2-01-F16, SNIPPET).

### 5.3 What changes for India (OUR DESIGN unless cited)

| Factor | US model | India version |
|---|---|---|
| Who titrates | Pharmacist or navigator under protocol | Medical officer or GP taps approve. Later, a state may delegate to community health officers, as China did with village doctors (D1-01-F09) |
| Protocol | Practice-specific algorithms | The state's own published HEARTS sheet, loaded as a file (Gujarat, Punjab, Maharashtra differ, D1-06-F01, F02) |
| Device | Bluetooth cuff supplied | Any cuff: photo of the screen, Bluetooth where available, typed fallback (D2-02) |
| Channel | App or portal | Chat (Telegram tonight, WhatsApp in product); voice and IVR later for patients without smartphones. Rural women's phone ownership is 57.4% (NFHS-6, D1-03-F42, SNIPPET) |
| Language | English or Spanish | Pre-translated templates per state language. No machine translation of dose text |
| Drug cost | Insurance | Public drugs at about ₹200 per patient per year (D2-01-F12). Private generic combinations cost about ₹47 to ₹83 per 10 tablets (D2-01-F15, SNIPPET) |
| Regulation | FDA non-device CDS route debated | CDSCO draft software guidance (21 Oct 2025) classes software by intended use (D2-01-F11, SNIPPET). Telemedicine Practice Guidelines 2020 allow "List B" add-on medicines only in follow-up consults after an in-person visit (D2-01-F10, SNIPPET) |

## 6. The business in brief

Who could pay (OUR DESIGN):
1. **Private hospital chains and multi-doctor clinics** that run NCD clinics. The loop keeps patients and refills inside their system and saves visit time. First buyer.
2. **Pharma patient-support programmes** for antihypertensive brands. There is a conflict risk if the payer sells the drug being stepped up, so keep the protocol state-published and locked.
3. **Employers and insurers' OPD or wellness plans**: longer sales cycle.
4. **State NCD programmes**: largest pool but lowest price, since drugs cost ₹200 per patient per year (D2-01-F12).

**Price and unit cost (all inputs labelled):**

| Line | Value | Basis |
|---|---|---|
| Price to clinic, private tier | ₹149 per active patient per month | ASSUMPTION. Below Sugar.fit's ₹29,990 / 12 = ₹2,499 per month (D1-04-F04, OUR ARITHMETIC) and close to a generic combination strip |
| Messages | Telegram: ₹0. WhatsApp per-message price in India: NOT SEARCHED | ASSUMPTION ₹15 per patient per month for WhatsApp templates, to be checked |
| Cloud and storage | ₹5 per patient per month | ASSUMPTION |
| Photo-reading compute | ₹2 per patient per month (about 30 photos, small on-device or server model) | ASSUMPTION |
| Doctor time | Proposals per 100 patients per month: 6.5 to 8.5 in OUR SIMULATION (section 7). At 30 seconds each, about 4 minutes per 100 patients per month | OUR SIMULATION + ASSUMPTION of 30 s |
| Health-worker follow-up for silent patients | ₹30 per patient per month (1 call of 5 min per month at ₹25,000 per month salary, about 9,600 call-minutes per month) | ASSUMPTION. OUR ARITHMETIC: ₹25,000 / 9,600 x 5 min = about ₹13, rounded up for overhead |
| Gross margin at ₹149 | ₹149 - (15 + 5 + 2 + 30) = ₹97, about 65% | OUR ARITHMETIC |
| Cuff | ₹2,600 one-time (HEM-7156T, D1-06-F31, SNIPPET), or the patient's own cuff | Patient or clinic pays |

**Bottom-up size (ASSUMPTION-heavy):**
- 42.01 million hypertension patients on treatment under 75 by 25 (D1-03-F14, SNIPPET). The private-sector share is not sourced. ASSUMPTION: 10 million are treated privately and 5% are reachable by a clinic chain programme in 5 years, giving 5,00,000 patients. 5,00,000 x ₹149 x 12 = ₹89.4 crore a year (OUR ARITHMETIC).
- First customer: one chain with 10,000 enrolled gives 10,000 x ₹149 x 12 = ₹1.79 crore a year (OUR ARITHMETIC).
- Public tier: ASSUMPTION ₹15 per patient per month at 10 lakh patients gives ₹18 crore a year. It is only viable if a state pays for outcomes: controlled patients, return rate.

What would move the price: proof of control gain against usual care in an Indian cluster, which PHTI-style buyers demand (D1-05-F21, panel view).

## 7. What the team shows by noon

### 7.1 Three-minute demo script (OUR DESIGN)

| Time | Who | What is on screen | Words (short) |
|---|---|---|---|
| 0:00-0:25 | Lead | One slide: 51% return; 26.3% to 59.8% among returners; 21.2% controlled | "India's protocol works when patients come back. Half don't. We bring the 30-day visit home." |
| 0:25-0:50 | Lead | Loop diagram (2.1) | "Reading in, protocol step out, doctor taps once, patient told in Hindi." |
| 0:50-1:30 | Patient teammate | Phone: Telegram bot. Live cuff reading by photo (or the D2-02 clip). Bot confirms "2 good readings saved" | "Real reading, quality-checked." |
| 1:30-1:50 | Engine owner | Seeded demo patient "Asha" (synthetic): 7 days at about 148/92 on amlodipine 5 mg. Bot asks the adherence question; tap "0 days missed" | "Before stepping up, the protocol says check compliance. We ask." |
| 1:50-2:15 | Doctor (mentor or teammate) | Laptop: clinician queue. Card shows mean, readings, protocol line "If still high: Increase to Amlodipine 10mg", guards passed. Tap Approve. Timer shows seconds | "One tap. Every change is approved." |
| 2:15-2:30 | Patient teammate | Phone receives Hindi message with the change and the doctor's name | "Change delivered in her language." |
| 2:30-2:50 | Bio student | Results page: 36 tests pass, branch coverage %, simulation chart | "Every branch of the sheet tested. Our simulation, not a trial." |
| 2:50-3:00 | Lead | Swap the protocol dropdown to Nigeria; re-run Asha: proposal becomes losartan 50 | "Same engine, any state's protocol." |

Backup if the network fails: the whole flow on the plain web page on localhost, with a screen recording made at 10:30.

### 7.2 "Initial test results" (honest)

**(i) Branch coverage on the protocol files.**
- Measured: number of test cases passing (target 36 of 36), line and branch coverage of `engine/decide.py` from `pytest --cov --cov-branch`, and "keys exercised" per YAML file (a small script logs which protocol keys `decide()` read during the test run).
- Claim allowed: "the code does what the sheet says in every branch we listed". Not allowed: "safe" or "clinically validated".

**(ii) Simulated cohort. OUR SIMULATION with stated assumptions. It is not a trial and shows no effect on patients.**

Design:
- Unit: one patient, monthly cycles, 12 months, n = 5,000 per arm, same random seed across arms.
- Ladder: Gujarat order (= Punjab order, D1-06-F01). Each patient has a hidden "responder step" R: the first step at which they would be controlled. From the Punjab cumulative control by step (70%, 75%, 77%, plateau 77%; D1-06-F04): P(R=1)=0.70, P(R=2)=0.05, P(R=3)=0.02, never within the ladder = 0.23 (OUR ARITHMETIC: differences of the cumulative figures). Sensitivity run with Maharashtra figures (76%, 81%, 82%): 0.76 / 0.05 / 0.01 / never 0.18. Caveat: F04 figures are clinic BP at 30-day reviews among patients who were followed. They already include real-world adherence, so adherence is not applied a second time to control.
- Non-adherence: 48% of patients flagged non-adherent (D1-03-F44, SNIPPET, definition-dependent). Used only to count step-ups given to non-adherent patients.
- Clinic-only arm: each month the patient attends with p = 0.51 (ASSUMPTION built from D1-03-F10's 51% return; F10 is "returned at least once", so per-visit attendance is likely lower and this favours the clinic arm). A visit refills 30 days of drugs ("Dispense drugs for 30 days", D1-06-F14). With no visit the drugs run out and the patient is not controlled that month (ASSUMPTION). At a visit, if uncontrolled, the doctor steps up without an adherence check (ASSUMPTION, reflecting 2-minute consults, D1-03-F24).
- Home-loop arm: each month the patient sends a valid 7-day block with probability e (engagement), at three levels, 0.3 / 0.5 / 0.7 (ASSUMPTION). If engaged, the loop runs `decide()`. A non-adherent patient gets SUPPORT (no step-up). An adherent uncontrolled patient gets a step-up approved by the clinician (ASSUMPTION: always approved). The refill happens if the patient collects drugs after the prompt, p = 0.9 (ASSUMPTION). If not engaged, the patient falls back to the clinic arm's 0.51 visit chance.
- Outputs: % controlled each month per arm; step-ups given to non-adherent patients per 100 patients over 12 months; proposals per 100 patients per month (doctor workload).

Pseudocode (the runnable version is about 40 lines of Python, written tonight at `sim/cohort.py`):

```python
for arm in [clinic, loop(e=.3), loop(e=.5), loop(e=.7)]:
  for patient in range(5000):
    R = draw(responder_dist); step = 1; nonadherent = rand() < .48
    for month in 1..12:
      engaged = arm.is_loop and rand() < arm.e
      contact = engaged or rand() < .51
      on_drug = contact and (not engaged or rand() < .9)
      if contact and step < R and step < 5:
          if engaged and nonadherent: support()           # no step-up
          else: proposals += 1; oversteps += nonadherent; step += 1
      controlled[month] += on_drug and step >= R
```

Indicative output from a first run by this agent (OUR SIMULATION, seed 1, n = 5,000; re-run tonight, do not quote as data):

| Arm | Controlled, month 6 | Controlled, month 12 | Step-ups to non-adherent patients per 100 (12 mo) | Proposals per 100 patients per month |
|---|---|---|---|---|
| Clinic only (Punjab curve) | 38.7% | 39.0% | 47.6 | 8.5 |
| Loop, engagement 30% | 47.8% | 49.1% | 44.6 | 8.1 |
| Loop, engagement 50% | 53.5% | 55.0% | 37.3 | 7.5 |
| Loop, engagement 70% | 58.9% | 59.8% | 25.3 | 6.5 |
| Clinic only (Maharashtra curve) | 41.0% | 41.4% | 37.7 | 6.8 |
| Loop 30 / 50 / 70% (Maharashtra) | 51.1 / 57.3 / 63.1% | 52.4 / 58.6 / 64.3% | 34.9 / 28.9 / 20.1 | 6.3 / 5.8 / 5.0 |

Sanity check: the clinic arm at 39% sits between district control of 21.2% (D1-01-F11) and 59.8% among IHCI returners (D1-03-F10). That is plausible, not a validation.

What the simulation honestly says: almost all of the modelled gain comes from contact and refills (the 51% return gap), not from smarter stepping, because the F04 curve plateaus after step 3. The adherence check mainly cuts needless step-ups. Both conclusions follow from the assumptions, which are stated. The chart is a line chart: month 0 to 12 on x, % controlled on y, four lines (clinic, loop 30/50/70), and a light band from 20 seeds per line. Below the chart, a bar pair shows "step-ups to non-adherent patients". Title: "OUR SIMULATION. Assumptions listed. Not a trial."

**(iii) Live run of real readings from teammates.**
- 4 to 6 teammates each take 2 sessions of 2 readings with D2-02's protocol and send them through the bot. They then appear in the queue and logs.
- Report: number of readings received, % passing the quality gate, time from photo to stored reading (median), and digit-read accuracy against the cuff screen if the photo route is used (D2-02 owns this number).
- Honest caveat: young, mostly normotensive teammates trigger HOLD, not step-ups. The step path is shown with the seeded synthetic patient. Teammates' readings are not clinical data.

**(iv) Time to approve.**
- The clinician screen logs `card_shown_at` and `decision_at`. Ask 3 people (a teammate, a mentor, and a doctor if one is present) to process 10 cards each: 7 step-ups, 1 lab order, 1 pregnancy block, 1 urgent. Report median and range of seconds per card and the number of wrong taps (for example, approving the pregnancy block as a step-up).
- Honest caveat: these are not clinicians on real patients. It measures the interface, not clinical judgement.

## 8. Stack and skeleton that minimise risk tonight

**Language and framework (OUR DESIGN):** Python 3.11, FastAPI, Jinja2 templates with HTMX (no JS build step), SQLite through `sqlmodel` or plain `sqlite3`, PyYAML plus `pydantic` to validate protocol files, `pytest` + `pytest-cov`. One process, run on one laptop, with `ngrok` or `cloudflared` only if a public URL is needed.

**Patient channel comparison:**

| Channel | Setup steps (from docs) | Time tonight | Risks | Verdict |
|---|---|---|---|---|
| Telegram bot | @BotFather `/newbot`, answer prompts, receive token; long polling works without a public URL; inline buttons supported (D1-06-F54; D2-01-F9) | Docs give no time. ESTIMATE 15 min to first message with `python-telegram-bot` | Few Indian patients use Telegram, but that does not matter for the demo | **Primary tonight** |
| WhatsApp Cloud API test number | Create Meta app with WhatsApp use case and a business portfolio; connect account; temporary token (it "expires quickly"); first message is the `hello_world` template; reply opens a 24-hour window for free-form; webhook needs a public HTTPS URL; permanent token needs a system user (D2-01-F8, OPENED; D1-06-F34) | Docs give no time. ESTIMATE 1 to 3 hours, with account-review and webhook risk | Token expiry mid-demo; test-recipient limit (about 5 numbers per secondary guides, SNIPPET); template rules | Product slide only. Try after 07:00 only if everything else is green |
| Plain web page (mobile form) | None beyond the FastAPI app | ESTIMATE 30 to 45 min | No push messages, so the patient must open the page | **Fallback, built anyway**; also the offline demo |

**Storage (OUR DESIGN):** SQLite file `loop.db`. Tables: `patient(id, name, lang, step, last_change_at, pregnant, status, protocol_id)`, `reading(id, patient_id, ts, sbp, dbp, pulse, route, quality_json)`, `adherence(id, patient_id, ts, missed_days, has_stock)`, `lab(id, patient_id, name, date, value)`, `proposal(id, patient_id, created_at, action, payload_json, reasons_json, status, decided_by, card_shown_at, decided_at)`, `message(id, patient_id, ts, template_id, lang, text)`. Synthetic patients only.

**Repository layout:**

```
bp-step-loop/
  README.md               # run commands, safety statement
  protocols/
    in_gujarat_hearts.yaml
    ng_hearts_losartan.yaml
    ada_basal_insulin.yaml          # paper_only
    schema.py                       # pydantic models; load() refuses null in required branches
  engine/
    decide.py                       # pure function, section 3b
    window.py                       # home-reading window rules, section 4.2
    proposals.py                    # Proposal dataclass, reasons
  app/
    main.py                         # FastAPI: /readings, /queue, /approve, /patient/<id>
    bot.py                          # Telegram long polling -> same API
    templates/  queue.html  patient_form.html  results.html
    messages/ en.yaml hi.yaml <third>.yaml
  ingest/
    photo_reader.py                 # from D2-02
    omron_ble.py                    # omblepy wrapper, from D2-02
  sim/
    cohort.py                       # section 7.2 (ii)
    plot.py                         # matplotlib PNG for results page
  tests/
    test_gujarat.py  test_nigeria.py  test_ada_paper.py  test_window.py
  seed/
    synthetic_patients.py           # "Asha", "Ravi", "Meena" with scripted 7-day readings
```

**The three screens:**
1. **Patient:** Telegram chat (and the same flow on `patient_form.html`). Measure prompt, photo or number entry, "saved n of 14", adherence buttons, change message, "I understand" button.
2. **Clinician queue:** list of cards sorted urgent first. Each card shows the patient, the step, a sparkline of 7 days, the mean, the adherence answer, the protocol line quoted, guards checked (ticks), the proposed regimen in bold, and [Approve] [Edit] [Reject]. A timer is logged.
3. **Results:** test count and coverage, the simulation chart with its assumptions box, live-run counts, approve-time table, and a protocol dropdown (Gujarat / Nigeria / ADA paper) that shows the YAML.

## 9. Hour-by-hour plan, 23:00 Thu 13 Nov to 12:00 Fri 14 Nov

Roles: **E** = engine (CS), **I** = interfaces (CS), **P** = protocol and tests (biology), **H** = hardware and measurement (D2-02's plan), **L** = lead, story and simulation (the 5th or 6th person, or E after 05:00).

| Time | E (engine) | I (interfaces) | P (protocol, tests) | H (hardware) | L (story, sim) | Checkpoint |
|---|---|---|---|---|---|---|
| 23:00-23:30 | Repo, schema.py, Proposal class | FastAPI skeleton, SQLite tables | Copy file 1 from this note; open the Nigeria PDF, fill its null threshold | Per D2-02 | Slide 1 problem, safety statement | Repo runs `pytest` (0 tests) |
| 23:30-01:00 | `decide()` steps 0-4 + window rules | Telegram bot echo, then saves readings | Write T1-T12 as pytest | | Write `sim/cohort.py` | **00:30: T1-T8 green** |
| 01:00-02:30 | `decide()` steps 5-8, guards, substitutes | Clinician queue page with Approve | T13-T29 | | Run sim, chart v1 | **02:00 FIRST END-TO-END: typed reading -> proposal -> approve -> message (English)** |
| 02:30-04:00 | Nigeria file runs; ProtocolIncomplete; audit log | Adherence buttons in bot; patient web form | T30-T36, coverage run | Hand over reading route (photo or BLE) | Seed synthetic patients; slide 2 loop | **03:30: 36 tests, coverage number** |
| 04:00-05:30 | Integrate D2-02 reading route + quality flags | Hindi + 3rd language templates (teammates write, P checks dose words) | Review every message template against the sheet words | Integration | Results page | **05:00 FREEZE ENGINE: no logic changes after this, only bug fixes with a test** |
| 05:30-07:00 | Approve timer, edit/reject reasons | Protocol dropdown on results page | Teammates' live readings session 1 | Live readings | Approve-time trial (3 people x 10 cards) | **06:30: all 4 results exist in some form** |
| 07:00-08:30 | Bug fixes only | Optional: WhatsApp test number (time-box 60 min, stop at 08:30) | Thesis draft review | | Deep Tech Thesis final | |
| 08:30-10:00 | Sim 20-seed bands | Polish queue card | Teammates' live readings session 2 | | Deck, 6 slides | **09:30 full dress rehearsal 1** |
| 10:00-10:30 | | Record backup video of full flow | | | | **10:30 backup recorded** |
| 10:30-11:30 | Fix only rehearsal bugs | | Mentor Q&A drill (section 10) | | Rehearsal 2 and 3 | |
| 11:30-12:00 | Laptop on charger, offline mode tested | | | | | Present |

**Cut lines (drop in this order if behind):**
1. WhatsApp: never on the critical path.
2. Third language. Keep English and Hindi.
3. 20-seed simulation bands. One run plus a stated assumption box is enough.
4. ADA file as tests. Show the YAML only.
5. Nigeria file as live dropdown. Keep its tests only.
6. Telegram. Use the web form for the patient side.
7. Photo or Bluetooth reading route. Use typed readings, and say D2-02's measurement work is shown separately.

Never cut: the adherence check, the clinician approval step, the pregnancy and very-high branches, the test table, the safety statement.

**Critical path:** schema, then `decide()`, then the T1-T29 tests, then the queue with Approve, then the change message. Everything else hangs off it. If the 02:00 end-to-end checkpoint is missed, apply cut lines 1 to 4 immediately.

## 10. The three hardest mentor questions (deep-tech fund, measurable impact, path to product)

**Q1. "This is a rules engine. Where is the deep tech, and what stops Simple or a hospital IT team from adding it in a month?"**
Honest answer: the dose logic should be rules, because a published protocol is the safest thing to automate and the evidence comes from protocol titration (D1-01-F09, F38; D1-05-F2). The hard parts are three:
- trusting a home reading from any cuff in Indian homes (D2-02);
- the decision of whether to step up or fix intake, made from that reading plus adherence;
- the outcome dataset: every approved step with its 30-day response, which no one in India holds (no open home-BP-with-medication dataset, D1-06-F42).
Simple could add step logic; its data model has none today (D1-06-F40). Our position is to be the measurement-plus-decision layer that plugs into Simple or a hospital EMR, not to compete with the registry. The learning layer (3d) comes after data, and we do not claim it tonight.

**Q2. "What measurable impact, and how soon can you prove it?"**
Honest answer: tonight we have only code correctness and a simulation. The measurable endpoint is the share of enrolled patients controlled at 6 months, plus the return rate. The baseline is IHCI's 51% return (D1-03-F10) and 21.2% district control (D1-01-F11). Abroad, comparable programmes report -8.7 mmHg at 6 months against education alone (D2-01-F5), and CRHCP cut cardiovascular events (D1-01-F38). The first proof would be a 6-month pragmatic pilot with one clinic chain or a district: about 300 patients, control and return rate against matched clinics. That pilot needs an ethics committee and CTRI registration. The MGB lesson is that about 45% dropped out or were unreachable (D2-01-F5), so engagement is the metric to watch from week 1.

**Q3. "Who pays, and what is the regulatory path? A tool that proposes doses sounds like a medical device."**
Honest answer: yes, it likely is. CDSCO's draft software guidance (21 Oct 2025) classes clinical decision software by intended use and the severity of the condition (D2-01-F11, SNIPPET). A drug-step proposal for hypertension is unlikely to be Class A. Path:
1. Clinician-approved decision support at one partner clinic, under ethics approval.
2. CDSCO test licence, then a manufacturing licence on the risk class CDSCO assigns.
3. Only later, delegated titration by community health officers under a state protocol, as CRHCP did with village doctors.
The telemedicine rules let a doctor add "List B" medicines in a follow-up after an in-person visit (D2-01-F10, SNIPPET). The first payer is a private clinic chain at about ₹149 per patient per month (ASSUMPTION). Public money comes only with outcome-linked pricing, because drugs cost about ₹200 per patient per year (D2-01-F12). Pear's failure is the warning: do not depend on a new reimbursement category (D1-05-F20, F21).

## 11. Risks, what would kill it, and the safety statement

| Risk | Why it matters | Mitigation tonight / later |
|---|---|---|
| Bad home readings drive a wrong step | Over-treatment, falls | Quality gate, 3-to-7-day mean, repeat for very high, clinician sees raw readings (D2-02) |
| Over-titration / low BP | Sheet has no low-BP rule | `low.sbp_lt` null blocks silent use; clinician sets it before any real patient. CRHCP saw no excess falls or hypotension (D1-01-F38), but that was with supervision |
| Clinicians do not respond to the queue | The loop stalls, as with mWellcare prompts (D1-01-F46) | One-tap cards; measure approve time; later, service-level targets in the contract |
| Engagement collapses | MGB about 45% dropped out or unreachable (D2-01-F5); app retention is poor (D1-02-F26) | Clinician-enrolled (referral adds days of retention, D1-02-F27), chat not app, health-worker call for silent patients |
| Regulatory class higher than expected | Delays revenue | Start as research use under ethics approval; plan for the CDSCO licence early |
| Payer will not pay | Pear's fate (D1-05-F20) | Sell to clinics on time saved and refills; outcome-linked price for states |
| Home vs clinic threshold mapping questioned | The Indian sheet is clinic-based | Say so; make the threshold a protocol parameter the clinician signs |
| Phone access | Rural women 57.4% own a phone (D1-03-F42, SNIPPET) | Family phone, health-worker entry, IVR later |
| Protocol divergence between states | Wrong ladder applied | One file per state, chosen at enrolment, shown on every card |

**What would kill it:** an Indian pilot showing no gain in return rate or control over usual care. A regulator ruling that each proposal is a teleconsultation needing a full consult record. Or no clinic willing to pay before outcome data exist.

**Safety statement (shown on the first slide and in the README, verbatim):**
> This is a student prototype built overnight. It is not medical advice and not a medical device. It does not diagnose or treat anyone. A clinician must approve every change of medicine; the software only drafts proposals from a published protocol. No patient data were used tonight. The readings shown are from teammates who volunteered and from synthetic patients; they are not clinical data. The simulation is our own model with stated assumptions, not a trial. Low-blood-pressure and lab-recency limits are deliberately left unset and must be set by a supervising clinician before any real use.

## 12. Draft one-page Deep Tech Thesis (at most 350 words)

**Home BP step loop: bringing India's 30-day hypertension visit home**

*Problem.* India has a simple, published hypertension ladder: amlodipine, then telmisartan, then a diuretic, one step every 30 days. It works for patients who return: in the IHCI cohort, control rose from 26.3% to 59.8% among returners. But only 51% returned, and district control is 21.2%. Consultations last about two minutes, and most rural specialist posts are empty.

*Insight.* Trials agree that home readings alone do little (-1.0 mmHg). Home readings that drive a medicine change work: pharmacist titration 57% against 30% controlled, and village-doctor protocol titration in China cut cardiovascular events by a quarter. India's missing piece is not the protocol. It is the moment when someone reads the pressure, checks the pills were taken, and moves one step.

*What we built.* A loop that takes a quality-checked home cuff reading (photo or Bluetooth) and runs the state's published protocol, stored as data. Before any step-up it asks whether the medicine was taken, because the protocol says compliance comes first. It drafts the next step with its reasons, a doctor approves in one tap, and the patient receives the change in their language. The same engine runs the Gujarat and Nigeria protocols with no code change, and an insulin rule on paper.

*Results by noon.* All protocol branches covered by tests. Real teammate readings flowing end to end. Seconds to approve a change. OUR SIMULATION, calibrated to IHCI step-by-step control rates and the 51% return rate, suggests most of the gain comes from restoring contact and refills, not from smarter dosing. It is a model, not evidence.

*Why it is deep tech.* The defensible parts are trustworthy home measurement on cheap cuffs, the titrate-or-support decision, and a dataset of step-by-step responses that does not exist in India. That dataset is what a future model would need to predict who needs a second drug early.

*Path.* Clinician-approved decision support at one clinic chain (about ₹149 per patient per month), an ethics-approved pilot measuring control and return rate, then a CDSCO licence and state programmes on outcome-linked pricing.

(Word count 347 including title, counted with `wc -w`.)

## 13. Verdict

- **Buildability tonight: 5 of 5.** It is pure software on a laptop with a clear critical path. Hardware risk sits with D2-02 and has a typed-reading fallback.
- **Business: 3 of 5.** There is a real need and strong foreign proof, but no Indian payer is proven, the public price ceiling is low (drugs about ₹200 per patient per year), and the tool is likely a regulated device.
- **AI/ML share: about 15%.** Photo digit-reading and quality scoring (D2-02 side) plus the simulation. The dose logic is deliberately rules. The learning layer is future work.
- **Who leads:** the CS engine owner leads the build. The biology student owns the protocol files, test table and safety statement, and should answer the clinical questions on stage.

## Fact register (new facts, D2-01)

- D2-01-F1 | ESH Working Group 2021 position paper on home BP (Parati, Stergiou, Bilo et al.), J Hypertens 2021;39(9):1742-1767, 26 Jul 2021. "Seven-day monitoring (not fewer than 3 days)"; "Duplicate morning and evening measurements"; "After a 5 min sitting rest and 1 min between measurements"; discarding day 1 "is matter of debate"; home >=135/85 corresponds to office 140/90; long-term "7 days before each clinic visit, at least over 1 week within 3 months"; daily monitoring discouraged; self-adjusting drugs without physician guidance to be avoided. | https://pmc.ncbi.nlm.nih.gov/articles/PMC9904446/ | OPENED (first 100,000 of 359,803 characters), CITED
- D2-01-F2 | ESH 2023 guideline home schedule (3-7 days, duplicate AM/PM, day 1 dropped, 135/85) per secondary summary and Omron leaflet; guideline text not opened. | https://m3india.in/contents/editor_pick/esh-2023-hypertension-guidelines ; https://omron-healthcare.com/storage/professional/leaflets/how-to-measure-bp-home.pdf | SNIPPET
- D2-01-F2b | AHA 2019 statement schedule (2 AM + 2 PM, preferably 7 days, first day often excluded) as reported by Black Health; 2025 AHA/ACC keeps 130/80; 2025 guideline's home schedule NOT FOUND. | https://www.blackhealth.org/articles/home-blood-pressure-monitoring-black-adults/ | SNIPPET
- D2-01-F3 | ISH 2020 via AAFP practice guideline summary, Am Fam Physician 2021;103(12):763-765, 15 Jun 2021: "When BP is measured at home, hypertension is diagnosed if readings are consistently 135/85 mm Hg or greater." Schedule not in summary. ISH original (ahajournals) returned 403. | https://www.aafp.org/pubs/afp/issues/2021/0615/p763.html | OPENED, CITED
- D2-01-F4 | Indian Guidelines on Hypertension IV (2019), Shah et al., J Hum Hypertens 2020: HBPM threshold ">135/85 mm of Hg"; office ">140/90"; exact home schedule NOT FOUND. | https://www.pubmed.gov/32427886/ | SNIPPET
- D2-01-F5 | Mass General Brigham remote hypertension and lipid programme, JAMA Cardiol, online 9 Nov 2022 (8[1]:12-21): prospective QI cohort, non-randomised, education-only comparison; hypertension n = 3,658; "Nonlicensed navigators and pharmacists, supported by cardiovascular clinicians" with standardised algorithms; SBP/DBP -8.7/-3.8 (6 mo), -9.7/-5.2 (12 mo) vs -1.5/-0.7 and +0.2/-1.9; 1,492 to maintenance; 276 dropped out, 1,064 unreachable, 302 returned to primary care (about 45%, OUR ARITHMETIC; Table 2 counts differ slightly). | https://pmc.ncbi.nlm.nih.gov/articles/PMC9647559/ | OPENED, CITED
- D2-01-F6 | Ochsner Digital Medicine, JGIM study via Ochsner news release 17 Nov 2025: retrospective, propensity-matched, difference-in-differences, 5,057 Medicare patients, Jan 2019-Oct 2023; control 57.1% to 76.1% (Black), 61.3% to 77.7% (white); licensed clinician manages medicines. | https://news.ochsner.org/news-releases/study-shows-ochsner-digital-medicine-improves-hypertension-control-reduces-care-gaps/ | OPENED, CITED (journal article itself not opened)
- D2-01-F7 | Ochsner case study: 79% vs 26% control vs propensity-matched usual care. | https://www.ama-assn.org/practice-management/digital-health/return-health-telehealth-case-study-hypertension-digital | SNIPPET, THEIR CLAIM
- D2-01-F8 | WhatsApp Cloud API get-started (Meta docs, undated, opened 13 Nov 2026): Meta app with WhatsApp use case and business portfolio; temporary token "expires quickly and is not suitable for development purposes"; first test is `hello_world` template; reply opens 24-hour window for non-template messages; webhook and system-user permanent token steps; no time estimate; recipient limit not stated on page. | https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/ | OPENED, CITED
- D2-01-F9 | Telegram bot tutorial (opened 13 Nov 2026): `/newbot` with @BotFather returns a token; examples use long polling; inline buttons supported; no time estimate. | https://core.telegram.org/bots/tutorial | OPENED, CITED
- D2-01-F10 | Telemedicine Practice Guidelines 2020 (India): List B medicines may be prescribed in follow-up consultations as add-ons to drugs prescribed in person for the same condition; follow-up = same clinician, same condition, within 6 months of an in-person visit (secondary commentary); hypertension drugs not named in results. | https://pmc.ncbi.nlm.nih.gov/articles/PMC8554922 ; https://www.mondaq.com/india/healthcare/921874/telemedicine-practice-guidelines | SNIPPET
- D2-01-F11 | CDSCO draft Guidance on Medical Device Software, 21 Oct 2025: SaMD classified by intended use and clinical impact under MDR 2017 classes A-D, IMDRF-aligned; finalisation NOT CONFIRMED. | https://india-briefing.com/news/cdsco-draft-guidance-medical-software-40691.html ; https://corporate.cyrilamarchandblogs.com/2026/01/medical-device-as-software-has-cdsco-guidance-changed-the-rules/ | SNIPPET
- D2-01-F12 | WHO India, 2 Jun 2022: public-sector treatment "could be as low as Rs 200 per patient per year"; "more than 2.5 million patients with hypertension have been enrolled" by April 2022 across 15,000+ facilities; "Nearly 47% of the registered patients under care had blood pressure under control" (Q1 2021). | https://www.who.int/india/news/detail/02-06-2022-india-hypertension-control-initiative--a-high-impact-and-low-cost-solution | OPENED, CITED
- D2-01-F13 | Sahoo et al., J Hum Hypertens 2023: protocol medication cost about US$2-4 per patient per year public; private US$33.88-58.44 (protocols 1-2) and US$51.57-68.83 (protocol 3). | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10471490/ | SNIPPET
- D2-01-F14 | EASE-BP, open-label RCT of BP self-monitoring in Indian primary care, CTRI/2023/02/049949, protocol Oct 2024 (part B: 332 known hypertensives, SBP and adherence at 3 months); results NOT FOUND. | https://researchportal.searo.who.int/index.php/hrp/search/downloadFinalReport/55/1387 | SNIPPET
- D2-01-F15 | Drug prices: Jan Aushadhi telmisartan 40 mg Rs 9.60 per 10 tablets (Punjab rate comparison, 2019); retail telmisartan 40 + amlodipine 5 combination ₹46.95 (PharmEasy offer) to ₹83.44 MRP (Truemeds) per 10 tablets, undated listings. | https://phsc.punjab.gov.in/sites/default/files/2019-08/1520181015336RateComparisonGenericandBrandedMedicines.pdf ; https://www.truemeds.in/medicine/telvisart-am-405-mg-tablet-10-tm-tacr1-100905 | SNIPPET
- D2-01-F16 | SMARThealth India stepped-wedge cluster RCT, 18 PHC clusters, rural Andhra Pradesh, primary outcome SBP <140; result not opened. | https://typeset.io/pdf/smarthealth-india-a-stepped-wedge-cluster-randomised-4ezusx8u52.pdf | SNIPPET

## NOT FOUND / NOT SEARCHED

- NOT FOUND: 2025 AHA/ACC home-BP schedule text; Indian Guidelines IV exact home schedule; ESH 2023 guideline text (only the 2021 ESH position paper opened); Nigeria sheet's control threshold and pregnancy rule (not in the D1-06-F15 quote; PDF not re-opened); EASE-BP results; current Jan Aushadhi combination price; WhatsApp test-recipient limit on Meta's page.
- NOT SEARCHED: WhatsApp per-message price in India; Cadence and Story Health outcome figures; Indian home-vs-clinic BP offset; IndicTrans2 or Bhashini for translation (templates written by hand instead); low-BP alert thresholds (deliberately left to the clinician).
- Simulation numbers in 7.2 come from a script this agent ran (n = 5,000, seed 1). They are OUR SIMULATION and must be re-run by the team.

Searches used: 11


