## 4. The product we can build

Chapter 3 ended with a choice: the home blood-pressure step loop. This chapter shows that product end to end: what it does, what the patient and the doctor see, and the checks that stop a bad reading or a missed tablet from changing a dose. It ends with the same loop carrying other protocols.

### 4.1 What it does

OUR DESIGN. The loop is for adults on blood-pressure medicine who miss the 30-day review: the half who do not return (chapter 1.3). Once a month the patient takes a week of home readings with an upper-arm cuff and sends each one as a photo of the cuff's screen. The software checks the readings, asks whether the medicine was taken, and drafts the next step of the state's published protocol, with its reasons. A registered doctor approves, edits or rejects it in one tap, and the patient gets the change in their own language, in the doctor's name. Nothing that changes treatment reaches the patient before a clinician approves.

The protocol is Gujarat's published ladder: amlodipine 5 mg, then 10 mg, then add telmisartan 40 mg, then raise it to 80 mg, then add chlorthalidone 12.5 mg (hydrochlorothiazide 25 mg if chlorthalidone is not available), with a re-check after 30 days on each step. After the last step the sheet says: "Check if the patient has been taking medications regularly and correctly. If yes, refer to a specialist." It covers adults over 30. Its safety rules are in chapter 4.7, and every protocol rule in this chapter comes from that sheet [D1-06-F14].

### 4.2 The system map

A loop that changes treatment has six stages. Open parts already exist for each (Appendix C); the work is joining them with a safety rule at each handover (OUR VIEW).

| Stage | Its job | Our build tonight (OUR VIEW) |
|---|---|---|
| Sense | Get a number from the home | Photo of any cuff's screen, confirmed by the patient; typed entry as fallback |
| Check | Was the reading taken properly | Kit-built motion clip plus a phone checklist |
| Decide | Turn valid readings into a proposed step | One file per protocol, run by one `decide()` function |
| Confirm | A clinician accepts or rejects | Clinician queue: Approve, Edit, Reject |
| Act | Tell the patient, in their language | Telegram chat plus a web form |
| Learn | Improve choices from each response | Roadmap only; nothing learns tonight |

![System map of the step loop](adaptive-care-pictures/14-system-map.png)

*The six stages of the loop and the technology chosen for each tonight.*

The engine is one pure Python function, `decide()` (OUR DESIGN). It reads a protocol file written in YAML (a plain-text data format), the patient's state and the week's readings, and returns a proposal with its reasons. It never computes a dose: it can only pick a regimen written in the file. Each number in the file carries the sheet's own words; a value the source does not give is left blank, and the engine refuses that branch until a clinician fills it. No language model sits in the dose path (chapter 2.3 gives the reason); a model only reads the cuff photo and handles translation and speech.

### 4.3 The patient side

![Patient chat on the phone](adaptive-care-pictures/10-bp-patient-chat.png)

*Mock-up with example data.*

The patient uses a Telegram chat, or a web form if the chat fails, on a phone that may be a family member's (chapter 1.3). It prompts a measurement, takes a photo or typed reading, asks about tablets and delivers the change.

The home-reading rule (OUR DESIGN, from published guidance): on days 24 to 30 of each 30-day cycle the patient takes two readings 1 minute apart after 5 minutes of seated rest, morning before tablets and evening [D2-02-F10]. A session counts only if both readings pass the quality checks. The engine needs at least 3 valid days and aims for 7, as the European Society of Hypertension advises; the same society says a home mean of 135/85 corresponds to 140/90 in clinic [D2-01-F1]; the International Society of Hypertension [D2-01-F3] and the Indian Guidelines IV (search summary only) [D2-01-F4] use the same home line. So a mean at or above 135 systolic or 85 diastolic is "still high"; one session at or above 180 or 110 is "very high".

The Gujarat sheet is written for clinic readings at 140/90. **Applying a clinic protocol to home readings at 135/85 is OUR DESIGN.** The team says so aloud on the slide, and the threshold stays a value the clinician signs. No Indian home-against-clinic offset was searched.

The photo is read twice by a vision model, checked against plausible ranges and shown back for the person to confirm; memory screens are rejected. General vision models are untested on cuff screens (chapter 2.3) [D2-02-F8]. A photo cannot prove who measured or when; the clip's time-stamped record (chapter 4.5) narrows that gap without closing it. Typed entry is always built; Bluetooth only if an Omron HEM-7156T is in hand [D2-02-F1].

### 4.4 The doctor side

![Clinician queue of proposal cards](adaptive-care-pictures/11-bp-doctor-queue.png)

*Mock-up with example data.*

The doctor sees a queue of cards, urgent ones first, batched once a day. Each card shows the current step, a 7-day sparkline (a small chart of the week's readings), the mean, the answer to the medicine question, the protocol line it quotes, the safety checks ticked and the proposed regimen, with Approve, Edit and Reject. A timer logs each decision. Because the card carries everything needed, the decision is one tap (OUR DESIGN).

![One proposal card in detail](adaptive-care-pictures/12-bp-doctor-detail.png)

*Mock-up with example data.*

The approval and the patient message are the doctor's own act, sent in the doctor's name: OUR DESIGN, and a question for a lawyer, since the telemedicine guidelines want the registered doctor to deliver the prescription directly (chapter 2.6).

### 4.5 Trusting the reading

A home reading can be several mmHg wrong for reasons unrelated to the cuff, such as an arm hanging at the side (chapter 2.3). The loop answers with a small clip built from the maker kit (OUR DESIGN): an ESP32 board with two MPU6050 motion sensors, one on the cuff and one on the forearm. A helper seats the person correctly once, and the clip stores that posture. It then enforces 300 seconds of still rest, restarting on movement; checks that the forearm is within 20 degrees of flat (a hanging arm fails) and the upper arm within 15 degrees of the stored posture; and requires stillness through each 60-second measurement. It shows green or red, with reasons, time-stamped to join the reading. A 15-degree change moves the cuff about 2.4 cm, about 1.2 mmHg (OUR ARITHMETIC: 15 x (0.866 - 0.707) = 2.4 cm; 2.4 x 0.49 = 1.2) [D2-02-F17]. The thresholds are OUR ESTIMATE. What the clip cannot see (legs crossed, clothing, cuff size, talking, a full bladder, smoking) goes into a 4-question phone checklist.

![The reading-quality clip](adaptive-care-pictures/13-reading-quality-clip.png)

*The kit-built clip checks rest, stillness and arm position; it does not measure blood pressure.*

Cuff size matters too: a regular cuff on a large arm reads high [D2-02-F19]. So the app asks the arm size and refuses arms outside the cuff's range; the Omron HEM-7120 standard cuff fits 22-32 cm [D2-02-F30], and it passed an independent validation (ESH-IP 2010) [D2-02-F28].

OUR VIEW: the engine refuses to step a dose on readings that fail the clip, so a posture mistake costs a repeat, not a wrong prescription.

### 4.6 Was the medicine taken

Raising a dose that is not being taken is unsafe (chapter 2.1). So before any step-up the chat asks two questions, as buttons (OUR DESIGN):

- "In the last 7 days, how many days did you miss your BP tablet? 0 / 1-2 / 3 or more"
- "Do you have tablets left for the next 7 days? yes / no"

Adherent means 0 missed days. That cut-off is OUR DESIGN and the clinician can change it, because the sheet says "Check for compliance at each visit before titration of dose or addition of drugs" but gives no number. Any missed day, or no tablets left, sends support instead of a step-up, and a card goes to the clinician for information.

### 4.7 Safety built into the design

The engine runs its checks in a fixed order and proposes a step only at the end (OUR DESIGN, from the sheet):

1. A patient who is referred or waiting for lab results is left alone. A patient aged 30 or under, or with diabetes, a past heart attack or stroke, or kidney disease, is flagged "outside the demo, send to the doctor": the sheet has branches for these that tonight's engine does not handle.
2. Readings that failed the quality gate are dropped.
3. Safety first. A session at or above 180 or 110 brings a request to repeat after rest; if confirmed, an urgent card goes to the doctor and the patient is told to contact the clinic today, ahead of the 30-day wait. This home action is OUR DESIGN; the sheet's 180/110 line is for clinic entry. A low-pressure rule acts only once a clinician sets its threshold.
4. Fewer than 3 valid days: ask for more. Under 30 days on the step: "keep going". Home mean below 135/85: "same medicine", no doctor needed.
5. At or above the line: the medicine question (chapter 4.6).
6. The guards: referral after the last step; referral when pregnancy, or childbearing age without effective contraception, meets a barred drug (amlodipine steps may go ahead); a lab order before telmisartan 80 mg, and for an abnormal value, referral or, with no specialist reachable, withdrawing telmisartan and adding chlorthalidone.
7. Only then: propose the next step, quoting the sheet line.

Following the written safety rules of OpenAPS, a do-it-yourself insulin system (chapter 2.3) [D2-03-F46], the engine only chooses written regimens, holds the current step when data is missing and never steps on one reading.

OUR VIEW: four things are never dropped: valid home readings, the medicine-taken check, a protocol-true proposal with its reasons and safety branches, and a doctor's approval of every change. A dose worked out outside the protocol file, and a language model in the dose path, are ruled out for good.

### 4.8 Same loop, new protocol

OUR VIEW: each new protocol is a new market on the same engine, approval screen and safety method.

| In order | Home signal | Rule in the notes | Status |
|---|---|---|---|
| 1. High blood pressure | Cuff | Gujarat's ladder; a Nigerian ladder as a second file (chapter 5.2) | Being built tonight |
| 2. Insulin, then the tablet steps for diabetes | Sugar meter | The American Diabetes Association's step rule (chapter 2.3) | On paper only |
| 3. Heart failure | Weight, pressure, pulse, lab values | Step up to full doses soon after discharge (chapter 2.1) | Roadmap; needs a diagnostics partner |
| 4. Warfarin, then asthma | INR meter; inhaler use | Dosing tables differ between sources (search summary only) [D1-06-F37] | Roadmap |

![Same loop, new protocol](adaptive-care-pictures/15-same-loop-new-protocol.png)

*Diagram: the engine, the approval screen and the chat stay the same; only the home signal and the protocol file change.*

The picture says a "doctor or health worker" approves. That is the later aim: only a registered doctor may prescribe (chapter 4.4), and no Indian rule was found that lets a nurse or health officer change a dose (chapter 2.6). It remains a question for counsel.

### 4.9 What the biology adds (new research, roadmap)

OUR VIEW and OUR DESIGN. The biology in chapter 2.7 suggests five additions to the loop. None changes the state protocol; each is for the team and a supervising clinician to decide. "Tonight" means a data field, question or test case that changes no dose decision; "next" means the two-week test or the pilot (chapter 5); "later" needs patient data.

| Feature | What it does | When | Key facts |
|---|---|---|---|
| 1. Expected effect per step | The protocol file stores each step's expected extra fall and time course, and the card shows expected against measured; a day-14 mean with almost no fall prompts the medicine question early; a patient's own response is learned only across repeated cycles, since one cycle is mostly noise | Tonight (display); next (day-14 prompt); later (learning) | [D4-01-F49, D4-02-F36, D4-03-F55] |
| 2. Profile fields | Age, sex and salt habit recorded from day one; for an adherent patient who fails a step, the card raises the switch between a renin-angiotensin blocker and amlodipine or a thiazide; no gene or renin tests | Tonight (fields); later (switch question) | [D4-01-F02, D4-01-F47, D4-01-F36] |
| 3. Adherence beyond self-report | The refill date and a photo of the remaining strip; a firmer check at steps 3 and 5, which add a drug; potassium and uric acid at the thiazide step as a weak sign; drug assays only at referral | Next | [D4-05-F07, D4-05-F03, D4-05-F22, D4-05-F15] |
| 4. A "still high" rule sized to the noise | 135/85 as the centre of a band: about 141 or more with 7 days is clearly high (OUR ARITHMETIC: 135 + 6.0), 135-140 earns a second cycle, and 3-4 days near the line earn more days | Tonight (test cases); next (live, once a clinician signs the band) | [D4-03-F34, D4-03-F13, D4-02-F21] |
| 5. A safety window after each step | Creatinine and potassium 1-4 weeks after telmisartan starts or rises, holding the next step; sodium and potassium in the first month of the thiazide; a pregnancy question every cycle on a barred drug; a standing check and falls question for patients 60 or over; an ankle-swelling question after step 2; a symptom checklist at 180/110 | Tonight (pregnancy question and symptom checklist as tests); next (the rest) | [D4-04-F34, D4-04-F58, D4-04-F29, D4-04-F48, D4-04-F70] |

Two flags for the doctor's card follow from the step prices in chapter 2.7: step 4 adds little for its four lab tests, and step 2 more than triples ankle swelling. Whether to change either is a question for the clinician and, later, the state; the software keeps the Gujarat order.

OUR VIEW: what would make this hard to copy is the record the loop builds. No Indian data were found on response by step with home readings, on how much one person's home readings vary, or on adherence measured by drug assay, and India's programme does not record side effects [D4-02-F17, D4-05-F15]. Each approved step adds one example. The comparison with the current design, item by item, is in Appendix I.

Full detail: Appendix C (technology for each stage, reading quality, protocols as data), Appendix G (protocol file, decision steps, screens) and Appendix I (the biology).

Chapter 5 shows the smallest version of this product that can be built and tested honestly in one night, and the steps after it.
