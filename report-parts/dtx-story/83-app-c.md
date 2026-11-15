## Appendix C. The technology in detail

This appendix holds the detail behind chapter 2.3 (and the system parts in chapter 4): for each stage of a therapy loop, the technology that exists in November 2026, its cost and testing, and what a student team can build by noon. The protocol file itself (doses, steps, intervals, thresholds) and tonight's parts list and costs are in Appendix G; here we explain the idea of a protocol as data and the science of a trustworthy home reading. OUR VIEW: the hard engineering is in trusting the home reading and in bounding the decision, not in the model that makes it.

### C1. The parts of a therapy loop

A loop that changes treatment has six stages. The picture of this system map is in chapter 4.

| Stage | Its job | Technology found | Our build tonight (OUR VIEW) |
|---|---|---|---|
| Sense | Get a number from the patient's home | Omron cuffs read with omblepy [D1-06-F07]; cuff-screen photo readers [D2-02-F4]; Bluetooth glucose profile [D1-06-F29] | Photo of any cuff, confirmed by the patient; typed entry as fallback |
| Check the reading | Check that it was taken properly | AHA and ESH home rules [D2-02-F10, D2-02-F11]; posture-error trials [D2-02-F16] | Kit-built motion clip plus a checklist |
| Decide | Turn valid readings into a proposed next step | Step protocols [D1-06-F14]; HL7 CQL [D2-03-F52]; OpenAPS bounds [D2-03-F46] | One YAML file per protocol, run by a pure `decide()` function |
| Confirm | A clinician accepts or rejects | CDS Hooks cards with an accept button [D2-03-F53] | Clinician queue: Approve, Edit, Reject |
| Act | Tell the patient, in their language | Telegram bot [D2-01-F9]; Indian speech APIs [D2-03-F58] | Telegram chat plus a web form |
| Learn | Improve choices from each patient's response | Personal drug-response trials [D2-03-F12]; adaptive message timing [D2-03-F10] | Roadmap only; nothing learns tonight |

### C2. Sensing at home in India

This section shows what a household or maker kit can measure tonight, how the number gets out, and what accuracy studies say. Night delivery to Sonipat was NOT FOUND.

| Signal | Device | Price (date) | How data gets out | Accuracy evidence |
|---|---|---|---|---|
| Blood pressure | Omron HEM-7156T (Bluetooth) | about ₹2,600 (search summary only; listings in Appendix E1) [D1-06-F31] | Omron's own protocol, not the standard service; read with omblepy [D1-06-F07, D2-02-F1] | Maker's table cites ISO and ESH grades (THEIR CLAIM) [D2-02-F29] |
| Blood pressure | Omron HEM-7120 | RRP ₹2,334 (undated); ₹1,849 online, 10 Jun 2026 (search summary only) [D2-02-F30] | Photo or typing | Passed ESH-IP 2010 (Medaval) [D2-02-F28] |
| Blood pressure | Dr Morepen BP-01 | NOT RESEARCHED | Photo or typing | "has not been clinically validated" (Medaval) [D2-02-F32] |
| Glucose | Accu-Chek Instant (Bluetooth) | ₹1,124-1,321 (undated, search summary only) [D1-06-F48] | Certified Bluetooth glucose meter; one paired device; third-party reading not confirmed [D1-06-F48] | NOT RESEARCHED |
| Pulse, oxygen | MAX30102 (kit) | In kit | I2C to ESP32 | No large independent validation (search summary only) [D1-06-F19] |
| Heart rhythm | AD8232 (kit) | In kit | Analog to ESP32 | No human validation found (search summary only) [D1-06-F47] |
| Arm position | MPU6050 (kit) | ₹144-275 (undated, search summary only) [D2-02-F31] | I2C to ESP32 | NOT RESEARCHED |
| Lung function | ESP32 Venturi spirometer, about £45 | Parts | Python, no repository | n = 30: FEV1 error 5.18%; peak flow error 18.01%, 51.80 L/min too low [D1-06-F24] |
| Movement, pulse, walking | Phone only: MediaPipe Pose (33 body points) [D1-06-F26]; camera pulse with pyVHR, GPL-3 [D1-06-F45]; 6-minute walk app | Free | Phone | Walk distance r = 0.83, n = 32 (search summary only) [D1-06-F52]; others NOT RESEARCHED |

**Bluetooth in practice.** The standard blood-pressure service is 0x1810 (search summary only) [D1-06-F09], but no India-sold cuff was confirmed to use it [D2-02-F3]. Two Omron Connect models are encrypted [D1-06-F07]. Web Bluetooth needs HTTPS and a user click and is marked experimental [D1-06-F46].

**Reading any cuff's screen from a photo.** A purpose-trained reader reached mean errors of 1.2/0.8 mmHg on 776 US images and 0.9/0.5 mmHg on 1,934 Guatemalan recordings, against 4.1/2.7 mmHg for human transcribers on the Guatemalan set [D2-02-F4]. But 82% of 7,205 images in another Guatemalan set were poor quality, errors sat in the last digit, and only Omron screens were tested [D2-02-F4]. The open tool ssocr reads one row of digits [D2-02-F7]; 0 and 8, 1 and 7 get confused (search summary only) [D2-02-F9]. No published test of a general vision-language model on these screens was found [D2-02-F8].

**Blood pressure without a cuff, as of 2026.** The FDA cleared the Aktiia G0 cuffless monitor on 2 Jul 2025 [D2-02-F23]. The ESH says there are "no generally accepted protocols" for validating such devices [D2-02-F25], and a 2025 review found "no compelling evidence" of added value from pulse-wave methods [D2-02-F26]. A cuff must agree within a mean of 5 mmHg, SD up to 8 (search summary only) [D2-02-F27]. OUR VIEW: cuffless error is about the size of a dose step, and a kit version cannot be validated by noon. Do not build it tonight. Cuffless sensing stays on the roadmap until a validation protocol exists (chapter 5).

### C3. Making a home reading trustworthy

A home reading can be several mmHg wrong for reasons unrelated to the cuff. This section gives the guidance, the size of each mistake, the home threshold, and the clip that catches what a sensor can see.

**The guidance.** AHA: at least 5 minutes of quiet seated rest, two readings at least 1 minute apart, morning before tablets and evening, 7 days or more (minimum 3) [D2-02-F10]. ESH: the same, "Seven-day monitoring (not fewer than 3 days)" [D2-02-F11, D2-01-F1]. Dropping day 1 is "a matter of debate" for the ESH [D2-02-F12]; the AHA notes some guidelines drop it [D2-02-F10]. The ESH warns monitors over 4 years old drift [D2-02-F13] and calls handwritten logs "often incomplete and inaccurate" [D2-02-F14].

**The size of each mistake** (systolic / diastolic, mmHg):

| Mistake | Effect | Source |
|---|---|---|
| Arm on lap instead of on a desk | +3.9 / +4.0 (randomised crossover, n = 133, Baltimore) | [D2-02-F16] |
| Arm hanging at the side | +6.5 / +4.4 (same trial) | [D2-02-F16] |
| Arm below heart level | +0.49 / +0.47 per cm; arm at desk height against heart height +6.1 / +5.7 (n = 128) | [D2-02-F17] |
| Back not supported | +5 to +15 / +6 (AHA); +6 to +10 systolic (older table) | [D2-02-F18, D2-02-F20] |
| Legs crossed | +5 to +8 / +3 to +5 | [D2-02-F18] |
| Regular cuff on an arm that needs a large one | +4.8 systolic (randomised crossover, n = 195) | [D2-02-F19] |
| Regular cuff on an arm that needs an extra-large one | +19.5 systolic | [D2-02-F19] |
| Talking | +10 / +10 (older table, no citations in it) | [D2-02-F20] |
| Cuff over clothing | +5 to +50 systolic (older table) | [D2-02-F20] |
| No rest instead of 5 minutes | No meaningful difference below 140 systolic; none to at least 4 mmHg above (secondary review) | [D2-02-F21] |

The HEM-7120 standard cuff fits arms of 22-32 cm [D2-02-F30], so arm size must be measured.

**Home against clinic thresholds.** The ESH says a home mean of 135/85 corresponds to 140/90 in clinic [D2-01-F1]; the ISH [D2-01-F3] and the Indian Guidelines on Hypertension IV (search summary only) [D2-01-F4] use 135/85 at home. The Gujarat protocol is written for clinic readings at 140/90 [D1-06-F14]. Our engine (OUR DESIGN, from [D2-01-F1]) reads home sessions on days 24-30 of each 30-day cycle and calls a block "still high" at a home mean of 135 or 85; the full reading rule, with its minimum number of valid days, the day-1 rule and the urgent line, is in Appendix G. Using a clinic protocol on home readings is our choice and must be said on the slide.

Why it matters: SMARThealth India (stepped-wedge cluster trial, 18 clusters, rural Andhra Pradesh) found no blood-pressure effect, partly because "fluctuating BP values" made risk scores disagree, so only 37.2% of the cohort was exposed [D2-03-F17].

**The kit-built quality clip** (OUR DESIGN, from [D2-02-F10, D2-02-F16, D2-02-F17]; the picture is in chapter 4, the wiring and parts in Appendix G). An ESP32 with two MPU6050 motion sensors, on the cuff and the forearm. A helper seats the person correctly once and the clip stores that posture. It then:
- enforces 300 seconds of still rest, restarting on movement;
- checks the forearm is within 20 degrees of flat (a hanging arm fails) and the upper arm within 15 degrees of the stored posture;
- requires stillness through a 60-second measurement;
- enforces 60 seconds between readings.

A 15-degree change moves the cuff about 2.4 cm, about 1.2 mmHg (OUR ARITHMETIC: 15 x (0.866 - 0.707) = 2.4 cm; 2.4 x 0.49 = 1.2). The clip shows green or red and posts reasons, joined to the reading by time. It does not measure blood pressure. Legs crossed, clothing, cuff size, talking, bladder and smoking go into a 4-question phone checklist. Thresholds are OUR ESTIMATE. A weighted reading-quality score instead of pass or fail is roadmap work (chapter 5).

### C4. Algorithms that set a dose

Four families of dose algorithm are in use; each is bounded. The insulin and warfarin trials named here are described in full in Appendix B; this section is about how each algorithm limits what it can do.

**Closed-loop insulin, the model case.** In trials, Control-IQ raised time in the target glucose range by 11 points against a sensor-augmented pump in type 1 diabetes [D1-01-F24], and 2IQP cut HbA1c (a blood test showing average sugar over about three months) a further 0.6 points in insulin-treated type 2 diabetes [D1-01-F43]. The do-it-yourself system OpenAPS writes its safety rules down [D2-03-F46]:
- It acts only through temporary basal rates, so if it stops, the pump returns to the normal plan; the core version "cannot issue insulin boluses".
- The temporary rate is capped by the lowest of several limits, including "4x the current scheduled basal rate".
- Missing or conflicting data sends it back to the pre-set plan.

Its code (oref0, MIT) says it is "not a 'set and forget' system" [D1-06-F12]; dosing logic sits in `determine-basal.js` [D1-06-F53].

**Insulin titration rules.** ADA 2025: start basal insulin at 10 units a day or 0.1-0.2 units/kg, "increase 2 units every 3 days to reach FPG target without hypoglycemia", and if low sugar has no clear reason "lower dose by 10-20%" [D1-06-F16]. An upper limit of 0.5 units/kg/day is quoted (search summary only) [D1-06-F18]. India's ICMR workflow gives targets but no titration schedule [D1-06-F17]. In trials, d-Nav (device plus clinician) cut HbA1c 1.0% against 0.3% for the clinician alone [D1-01-F13], and TeleDiab-2 cut it 1.44% and 1.48% against 0.92% [D1-01-F14]. The FDA has cleared dose apps such as My Dose Coach (2017) and iSage Rx (2024) [D2-03-F47]. A reinforcement-learning model, RL-DITR, was tested only single-arm in 16 inpatients in China [D2-03-F11].

**Blood-pressure protocols.** Gujarat's published ladder, with 30-day reviews: amlodipine 5 mg, amlodipine 10 mg, add telmisartan 40 mg, telmisartan 80 mg (after blood sugar, urea, creatinine and urine protein; if any is abnormal, refer, or, with no specialist reachable, withdraw telmisartan and add chlorthalidone), add chlorthalidone 12.5 mg, then check adherence and refer. The sheet covers adults over 30, checks adherence at each visit, and bars telmisartan and chlorthalidone in pregnancy and in women of childbearing age not on effective contraception [D1-06-F14]. (How this sheet is written as a data file is in Appendix G.) Punjab and Maharashtra differ at step 2 [D1-06-F01, D1-06-F02]; across 159,292 patients who returned and stayed on protocol, control on clinic readings plateaued at 77% and 82% [D1-06-F04].

People do differ. PHYSIC (randomised, double-blind, repeated crossover, 280 people, Sweden, 1,468 treatment periods) found real between-person differences in drug response, worth about 4.4 mmHg if chosen per person [D2-03-F12]. A one-time "responder" label from a short run-in did not predict 12-month response in 608 Chinese patients [D2-03-F13].

**Warfarin tables.** The IWPC algorithm sets only the starting dose [D2-03-F48]. Feedback tables agree on no change at INR (a clotting test) 2.0-3.0 but differ outside it (search summary only) [D1-06-F37]. Self-management cut clots (RR 0.47) and deaths (RR 0.55) in pooled trials, compared indirectly with self-testing [D1-02-F05].

| Algorithm | Input | Output | How it is bounded |
|---|---|---|---|
| Closed-loop insulin | Continuous glucose sensor | Temporary basal rate | Rate caps, no boluses (oref0), revert on missing data [D2-03-F46] |
| Basal titration | Fasting glucose over 3 days | +2 units or -10-20% | Upper limit per kg; hypo branch; clinician sets cause [D1-06-F16, D1-06-F18] |
| BP ladder | 30-day review of readings | Next written regimen | Fixed steps, lab and pregnancy guards, referral at the end [D1-06-F14] |
| Warfarin table | INR | Weekly dose change in % | No-change band 2.0-3.0; hold at high INR [D1-06-F37] |

### C5. A protocol as data

A protocol written as data, not code, can be read by a clinician, tested branch by branch, and swapped without changing the engine. This section gives the prior art, what Indian decision-support trials found, the test-coverage lesson, and how our files fit.

**Prior art.**
- A 2002 review of 11 guideline languages found four basic parts: data collection, decision, patient state, intervention [D2-03-F54].
- WHO SMART Guidelines have no general hypertension kit; the blood-pressure kit is for pregnancy only, its machine-readable layers are "not yet available", and its licence is non-commercial [D2-03-F50, D2-03-F51].
- HL7 CQL is a standard logic language with an Apache-2.0 engine that is "not a complete implementation" and needs a Java 17 translator [D2-03-F52].
- CDS Hooks returns suggestion cards with an accept button (CC BY 4.0) [D2-03-F53].
- India's open Simple app stores a protocol as a drug list plus `follow_up_days`, with no step logic found (Appendix D2) [D1-06-F40].

**Indian decision-support trials.**

| Trial | Design and setting | Compared | Result |
|---|---|---|---|
| CARRS [D2-03-F14] | Randomised, 1,146 with diabetes, urban clinics, India and Pakistan, 28 months | Coordinators plus decision-support records against usual care | Positive: composite goal 18.2% against 8.1% |
| mWellcare [D2-03-F15] | Cluster randomised, 40 health centres, 3,698 people, 12 months | Nurse-run app with decision support against enhanced usual care | Null: systolic -0.98 (95% CI -4.64 to 2.67) |
| mPower Heart [D2-03-F16] | Before-and-after, no control, Himachal Pradesh, 6,797 people | Phone tool drafts prescription, physician vets | Systolic -14.6 mmHg, uncontrolled |
| SMARThealth India [D2-03-F17] | Stepped-wedge cluster, 18 clusters, rural Andhra Pradesh | Health-worker tablet plus doctor decision support against usual care | Null on blood pressure |
| IMPACT Diabetes [D2-03-F18] | Cluster randomised, 8 centres, 418 people, 9 months | Health-worker decision support under physician supervision | Small positive: HbA1c fall of 0.5% or more, 21.8% against 10.3% |

**The test-coverage lesson.** When the US VA re-encoded its hypertension decision support (ATHENA-HTN), 26 decision points gave 3,120 possible outputs, and 100 test cases covered "only 1% of the possible output combinations" [D2-03-F55].

**How our files fit** (OUR DESIGN; the files, the decision steps and the test table are in Appendix G). One YAML file per protocol: Gujarat, Nigeria, and the ADA insulin rule as paper only [D1-06-F14, D1-06-F15, D1-06-F16]. Each number carries the exact source words; a missing value is `null` and the engine refuses that branch. A pure `decide()` function checks safety first, then enough readings, the 30-day interval, the threshold, adherence, the last step, and the lab and pregnancy guards, and only then proposes a step. It never computes a dose; it only picks a regimen written in the file. Thirty-six test cases cover every branch listed so far, run against two protocols; the age, childbearing-age, abnormal-lab and "outside the demo" branches found later on the sheets still need tests [D1-06-F14, D1-06-F15]. Insulin and heart-failure protocols in the same engine are roadmap work, and heart failure needs lab values (chapter 5).

### C6. Language models and medicine doses

Language models make dose errors even when told to follow a protocol.

| Study | Setup | Error |
|---|---|---|
| TacroDose AI [D2-03-F38] | GPT-4 prompted with a hospital tacrolimus protocol, 300 simulated cases | First version: 13.9% "sentinel errors"; with stronger constraints and output checks: 1.0%, and 13.3% of runs not reproducible (OUR ARITHMETIC: 100 - 86.7) |
| Anticoagulant hold times [D2-03-F39] | ChatGPT and Gemini, 25 cases | "potentially dangerous recommendations in 12-20% of scenarios" |
| Prescribing-error checker [D2-03-F40] | Randomised crossover, 91 error scenarios | Pharmacist plus model was best, 61% accuracy; 1.5 times better than the pharmacist alone at catching serious errors |
| Incident-report classification [D2-03-F41] | o4-mini, 200 Swedish reports | 96.0% agreement with pharmacists |

No completed randomised trial of a language-model coach with a blood-pressure or HbA1c outcome was found; two are registered [D2-03-F44], and an Indian trial protocol uses a frozen Mistral-7B with nurses after heart surgery [D2-03-F37].

**The design pattern** (OUR VIEW, following [D2-03-F38, D2-03-F40, D2-03-F46]):
1. The model handles language only: cuff photo to strict JSON, translation, speech.
2. A fixed, tested engine makes every decision, from the protocol file.
3. Code checks every output against the protocol: plausible ranges, two agreeing reads, a regimen that exists in the file.
4. A clinician approves every change.

**Indian-language tools.** Indian-language voice and offline speech models are roadmap work (chapter 5).

| Tool | What | Price or licence | Fact |
|---|---|---|---|
| Sarvam AI API | Speech-to-text, text-to-speech, translation | Speech-to-text ₹0.49 a minute (price page, 13 Nov 2026) or ₹1.5 a minute (another listing, search summary only); text-to-speech ₹2-3 per 1,000 characters; ₹100 free credits (THEIR CLAIM) | [D2-03-F58, D1-06-F35] |
| AI4Bharat IndicTrans2 | Translation, 22 languages plus English | MIT | [D2-03-F59] |
| AI4Bharat IndicConformer | Speech recognition, 22 languages | MIT; needs a NeMo fork | [D2-03-F60] |
| Bhashini (Government of India) | Voice in 22 languages, text in 36 (government claim) | Price NOT FOUND | [D2-03-F57] |

### C7. Sensor and language models from the frontier labs

The large labs have built models of wearable signals and health conversations; few can be used today. Their consumer health products (ChatGPT Health, Claude, Google's Gemini coach, Copilot Health) are described as products in Appendix D11.

| Who | What | Evidence | Usable by a team today | Seen only in search summaries |
|---|---|---|---|---|
| Google | LSM and SensorLM wearable models [D2-03-F25, D2-03-F26] | Up to 40 and 59.7 million hours of wearable data | No open weights found | |
| Google | PH-LLM; Personal Health Agent [D2-03-F31, D2-03-F30] | PH-LLM matched experts on fitness, not sleep; the agent splits data, expert and coach roles | Not released; the agent pattern is reusable | |
| Google | AMIE for disease management, Nature 2026 [D2-03-F29] | Randomised, blinded virtual exam against 21 GPs on 100 cases; non-inferior; simulated patients | No public model | |
| Google | MedGemma 1.5 4B [D2-03-F32, D2-03-F62] | Released 13 Jan 2026; adds lab-report extraction | Yes, gated; "not intended to directly inform clinical diagnosis" | |
| Apple | Wearable behaviour model [D2-03-F27] | 2.5 billion hours, 162,000 people, 57 tasks | No weights stated | |
| Apple | Paid AI health coach [D2-03-F45] | Pre-launch press reports only | No | Yes; launch NOT FOUND |
| OpenAI | HealthBench [D2-03-F33] | 5,000 conversations, rubrics by 262 physicians; o3 scored 60% | Yes, open source (licence not opened) | |
| OpenAI | ChatGPT Health, launched 7 Jan 2026 [D2-03-F36] | "not intended for diagnosis or treatment"; US records only | Consumer product | Yes; user numbers conflict (230 against 300 million) |
| Microsoft | MAI-DxO [D2-03-F34] | 80% on 304 NEJM cases against 20% for generalists; diagnosis, not dosing | NOT RESEARCHED | |
| Anthropic | Claude for Healthcare, 11 Jan 2026 [D2-03-F35] | Connectors (ICD-10, PubMed), FHIR skills; "We do not use users' health data to train models" (THEIR CLAIM) | Yes, via API | |
| Academic | PaPaGei pulse-wave model [D2-03-F28] | 57,000 hours; better on at least 14 of 20 tasks | Yes; code BSD-3, weights licence not stated | |

### C8. Adaptive nudging, bandits and reinforcement learning (later work)

Adaptive nudging learns when and what to send each person. A just-in-time adaptive intervention (JITAI) adapts "weekly, daily, or even many times a day"; a micro-randomised trial randomises each decision point [D2-03-F01]. Bandit timing of reminders, to help complete reading blocks, is roadmap work (chapter 5).

| Study | Design | Result |
|---|---|---|
| HeartSteps V1 [D2-03-F02] | Micro-randomised, 44 US adults, 6 weeks | Any suggestion +35 steps in 30 minutes (p = .06), fading over time; walking suggestions +59 (p = .02) |
| HeartSteps V2 [D2-03-F03]; Oralytics [D2-03-F08] | Learning algorithms deployed in US trials | Outcome results NOT FOUND |
| DIAMANTE [D2-03-F10] | Randomised, 3 arms, 168 people with diabetes and depression, US safety-net clinics, 6 months | Learned texts beat random texts: steps up 19% against 1.6% (random) and 3.9% (weekly message); HbA1c not in the abstract |
| Automated diabetes prevention app [D2-03-F42] | Randomised non-inferiority, 368 people, 2 US sites, 12 months | Matched human coaches: 31.7% against 31.9% |
| JITAI meta-analyses [D2-03-F04, D2-03-F06] | Mental health, 23 studies; sleep, 11 trials | Small effect (g = 0.15); adaptive not better than non-adaptive for sleep |

Two cautions. Standard estimators "can be inconsistent and fail to be replicable" on bandit-trial data [D2-03-F09]. A 2026 guideline for live learning systems uses pre-set fallbacks, which "safeguarded participants" in two case studies [D2-03-F07].

Open tools: MABWiser (Apache 2.0) [D1-06-F55]; Open Bandit Pipeline (Apache 2.0, off-policy estimators) [D2-03-F49]; HeartSteps V1 data (CC BY 4.0, 8,274 decisions) [D1-06-F44].

### C9. Personal response models and "digital twins" (later work)

A "digital twin" here is a model of one person that predicts their response to food or treatment. A model of each patient's response to the next step, built from real approved steps, is roadmap work (chapter 5). Twin Health as a company (funding, depth, Indian presence) is in Appendix D.

- **Twin Health, India, blood pressure** [D2-03-F19]: secondary analysis of an Indian randomised trial in 319 people with type 2 diabetes (233 twin, 86 standard care). Home readings guided blood-pressure drug changes. Systolic fell 7.6 against 3.2 mmHg at one year. Limits: secondary analysis, only 59 people on blood-pressure drugs, company-linked. The drug changes followed a protocol; the machine learning predicted diet response.
- **Method** [D2-03-F21]: predicts each person's post-meal glucose from a glucose sensor, food logs and other inputs and "dynamically adjusts dietary recommendations". No open code found.
- **Twin Health, US** [D2-03-F43]: randomised, 150 people, Cleveland Clinic, 12 months; HbA1c under 6.5% without glucose drugs other than metformin in 71% against 2.4%. Source is the institution's summary; funding not shown.
- **Twin Health, real world** [D2-03-F20]: 1,853 completers, HbA1c -1.8%, no control (THEIR CLAIM).
- **Glucose foundation models**: GluFormer (over 10 million readings, 10,812 adults) predicted later diabetes and cardiovascular death (arXiv only) [D2-03-F23]; CGM-LSM and GlucoFM report lower forecast error [D2-03-F24].
- **Blood pressure**: one agent-based model simulates six drugs on virtual patients; licence unconfirmed (search summary only) [D1-06-F43].

PHYSIC measured personal response over repeated periods [D2-03-F12]; a single run-in response did not predict the long-term one [D2-03-F13] (both in C4).

### C10. Open data, simulators and code

This table lists what a team can download tonight and the test each one makes possible.

| Name | What it is | Licence or access | Test it enables | Fact |
|---|---|---|---|---|
| IHCI control by step | Per-step control for 159,292 patients, Punjab and Maharashtra | CC BY 4.0 paper | Calibrate a simulated cohort to real step curves | [D1-06-F04] |
| R `bp` package | Home blood-pressure series incl. 757 Ghanaian patients and 1,283 children | GPL-3 | Replay the engine on real home readings | [D2-03-F61] |
| BPimageTranscribe | Contour-based cuff-photo reader | On Zenodo; data not public | Baseline for the photo reader | [D2-02-F4] |
| ShanghaiT2DM | 100 type 2 patients, glucose sensor plus insulin doses, 3-14 days | CC BY 4.0, no application | Replay fasting values through the 2-units rule | [D1-06-F11] |
| simglucose | Type 1 simulator, 30 virtual patients, Gym interface | MIT | Test an insulin rule; type 1 only | [D1-06-F10] |
| OpenAPS oref0 | Open closed-loop dosing code | MIT | Read real dose-bounding code | [D1-06-F12, D1-06-F53] |
| AAMOS-00 | 22 UK asthma patients, 2,054 patient-days, of which 1,099 have peak-flow readings; smart peak flow, inhaler, watch, air quality | CC BY 4.0 | Replay an asthma action-plan rule | [D1-06-F50] |
| HeartSteps V1 | 8,274 randomised nudge decisions | CC BY 4.0 | Offline bandit replay | [D1-06-F44] |
| BIDMC PPG | 53 ICU recordings, pulse and breathing | ODC Attribution | Test a heart-rate algorithm before using MAX30102 data | [D1-06-F33] |
| cql-execution | HL7 CQL engine | Apache-2.0 | Run protocol logic in a standard language | [D2-03-F52] |

No open type 2 diabetes simulator, blood-pressure titration simulator, or large home-blood-pressure dataset with medicine changes was found [D1-06-F30, D1-06-F42, D1-06-F43].

### C11. What we could not find

- A published test of a general vision-language model reading blood-pressure screens [D2-02-F8].
- Any cuff sold in India confirmed to use the standard Bluetooth blood-pressure service [D2-02-F3].
- An open type 2 diabetes simulator or a blood-pressure titration simulator [D1-06-F30, D1-06-F43].
- A large open dataset of home readings with medicine changes [D1-06-F42].
- A completed trial of a language-model coach with a blood-pressure or HbA1c outcome [D2-03-F44].
- A WHO computable kit for general hypertension [D2-03-F50].
- Open weights for Google and Apple sensor models, or Twin Health code [D2-03-F25, D2-03-F27, D2-03-F21].
- HeartSteps V2 and Oralytics outcome results [D2-03-F03, D2-03-F08].
- Bhashini prices and terms [D2-03-F57].
- Indian guideline text on how many home readings over how many days, and an Indian home-against-clinic offset [D2-02-F15].
- Independent validation of MAX30102, AD8232 and MPU6050 tilt [D1-06-F19, D1-06-F47].
- Night delivery to Sonipat.
- Any trial of adherence-gated titration (NOT SEARCHED).

### C12. So what for us

OUR VIEW.
- **The reading is the science.** Arm position alone adds 3.9-6.5 mmHg [D2-02-F16], and noisy readings broke an Indian trial [D2-03-F17]. The clip and reading rules are our deep-tech claim, not the rules engine. The engine refuses to step a dose on readings that fail the clip, so a posture mistake costs a repeat, not a wrong prescription.
- **Blood pressure is the signal to start with.** It is the one signal a household can measure tonight with a validated, cheap device. The photo path reaches any cuff, so we do not depend on Bluetooth, but every photo read must be shown back to the patient to confirm.
- **Join open parts, with a safety rule at each handover.** Every stage of the loop has open parts and none needs a new model tonight; the value is in joining them.
- **Bound every action.** Every working dose algorithm caps its actions and falls back to a standing plan when data is missing; a ladder is the simplest case. Copy OpenAPS [D2-03-F46]: choose only written regimens, hold the current step on missing data, never step on one reading.
- **Keep models on language.** A 1% dangerous-error rate under the best constraints [D2-03-F38] rules out a model choosing doses. The model reads photos and speaks Hindi; the engine decides. Sarvam is the fastest way to a Hindi voice message tonight; the MIT models are the path to running offline later. Of the frontier-lab models, only MedGemma, PaPaGei and HealthBench can be downloaded, none sets doses, and nothing from them enters our decision.
- **Act between visits, not during them.** Decision support used during clinic visits did not beat good usual care in two Indian trials [D2-03-F15, D2-03-F17]; our value is the change made without a visit.
- **Test on generated cases and replayed data, not only hand-written ones.** ATHENA's 1% coverage says so [D2-03-F55]. Our honest tests tonight are branch coverage, a replay of the `bp` Ghana data, and a labelled simulated cohort calibrated to the IHCI step curve.
- **The learning layer is earned, not claimed.** People do respond differently to drugs [D2-03-F12], which is the honest reason a later learning layer could add value, but no open twin exists for blood-pressure drugs. Each approved step in our loop gives one labelled example (readings before, readings 30 days after); that is the dataset a response model would need, and it does not exist in the open today [D1-06-F42]. Adaptive timing has one head-to-head win, on steps, not a clinical measure; in our loop it could help complete 7-day reading blocks, later, and a HeartSteps replay shows the method only.
