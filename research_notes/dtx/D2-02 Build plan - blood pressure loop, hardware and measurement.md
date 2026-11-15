# D2-02 Build plan: blood-pressure step loop, hardware and measurement (agent: claude-opus-5-5, 2026-11-13)

## Digest
Twelve facts for tonight:
1. omblepy reads the Omron HEM-7156T from Windows with `pip install terminaltables bleak` and `python omblepy.py -p -d HEM-7156T`; HEM-7120/7124/7140T not supported; avoid CSR8510 dongles (D2-02-F1).
2. No India-sold cuff was confirmed to use the standard Bluetooth BP service (F3, NOT FOUND); Omron uses a custom protocol (D1-06-F07).
3. Automated reading of cuff-screen photos reached 0.9-1.2 mmHg systolic error on held-out sets, but 82% of field images in one Guatemalan set were poor quality; errors cluster in the last digit (F4).
4. No published test of a general vision-language model reading BP screens was found (F8).
5. AHA: 5 min seated rest, 2 readings 1 min apart, morning before tablets and evening, 7+ days (min 3) (F10). ESH: same, threshold 135/85; discarding day 1 "matter of debate" (F11, F12).
6. Arm hanging at the side: +6.5/+4.4 mmHg; arm on lap: +3.9/+4.0 (ARMS trial, n = 133) (F16).
7. Arm height effect is 0.49 mmHg per cm, smaller than hydrostatic theory (F17).
8. Wrong cuff size: +4.8 (large arm) and +19.5 (extra-large arm) with a regular cuff (F19).
9. Back unsupported +5 to +15; legs crossed +5 to +8 (AHA Table 4) (F18). Talking +10/+10, clothing +5 to +50 (older table) (F20).
10. Omron HEM-7120 passed ESH-IP 2010 (Medaval 2 stars); RRP ₹2,334; Dr Morepen BP-01 "has not been clinically validated" (F28, F30, F32).
11. Aktiia G0 cuffless monitor: FDA 510(k) K250415, 2 Jul 2025 (F23); ESH says no accepted cuffless validation protocol (F25).
12. HERB-DH1 (CureApp, Japan): home BP -4.3 mmHg, 24-h -2.4 mmHg, with lifestyle guidance, not drug changes (F38).

Three surprises:
- Rest may matter little below 140 systolic, up to at least 4 mmHg above it (F21).
- Human transcription error was 4.1/2.7 mmHg in one Guatemalan set, worse than the algorithm (F4).
- ESH adult text says only "standardized sitting posture"; the explicit back-arm-feet wording sits in its paediatric section (F13).

Against starting leads / triage: the triage assumed a phone photo can be read "automatically". Published readers are purpose-trained on Omron screens; a general vision model is untested, so the confirm step is required (F4, F8). Clinic thresholds in the Indian protocols (140/90) differ from the home threshold (135/85) (F11, F15); D2-01 must choose.


## Findings

### 1. Getting the number out of the cuff (ranked for tonight by time to working; OUR DESIGN)

Rank 1 for tonight: **(b) phone photo of the cuff screen, read by a vision model, confirmed by the patient**. It works with any cuff the team can find, including the non-Bluetooth cuffs most households own. Rank 2: **(a) Omron HEM-7156T through omblepy**, only if one is in hand by about 02:00. Rank 3, always built: **(c) typed entry**. All three write the same record into the engine: {sys, dia, pulse, time, source, quality_flag}. OUR DESIGN.

#### 1(a) Bluetooth cuff read without the maker's app

Facts:
- D2-02-F1. omblepy install and use, verbatim from README: Windows `pip install terminaltables bleak`; first pairing with the cuff blinking -P-: `python ./omblepy.py -p -d HEM-7322T`; later `python ./omblepy.py -d HEM-7322T`. Flags: `-p` writes pairing key, `-d` device library, `-m` skip scan by MAC, `-n` only new records, `-t` sync clock. Supports Windows 10/11, Mac (UUID instead of MAC), Debian 13, Raspberry Pi OS, NixOS; Debian 11/12 unreliable. ESP32 bridge on branch `esp32bridge`, called "semi finished". Needs Bluetooth 4.2+ (prefer 5.0); CSR8510 dongles fail on Windows; remove any existing OS pairing before retrying. HEM-7156T tested for pairing, readout, new-record counter and time sync. HEM-7381T reads user 1 only. HEM-7120, HEM-7124, HEM-7140T NOT listed. No CSV flag documented. https://raw.githubusercontent.com/userx14/omblepy/main/README.md OPENED 13 Nov 2026, undated. CITED. Confirms and extends D1-06-F07, F32.
- Reuse D1-06-F07: Omron uses a custom EEPROM-read protocol, not the standard Blood Pressure service; HEM-7188T and HEM-7196T are encrypted and unsupported.
- Reuse D1-06-F09: standard GATT Blood Pressure service 0x1810, measurement characteristic 0x2A35 (SNIPPET). D2-02-F2. Bluetooth SIG publishes Blood Pressure Service v1.1.1 with mandatory erratum 23224. https://www.bluetooth.com/specifications/specs/blood-pressure-service-1-1-1/ SNIPPET.
- D2-02-F3. A search snippet says Omron's US telehealth product page lists "Blood Pressure Service" with Device Information and Current Time services. The page now 301-redirects to digitalhealth.omronconnect.com, which returned HTTP 403 on 13 Nov 2026. SNIPPET. Some Omron telehealth models may expose the standard service; which models, and whether any is sold in India: NOT FOUND.
- India-sold cuffs confirmed to expose the standard 0x1810 service (readable by Web Bluetooth, bleak or an ESP32 without vendor code): NOT FOUND in one search. Beurer and A&D UA-651BLE standard-profile claims: memory only, NOT FOUND, not used.
- Reuse D1-06-F46: Web Bluetooth needs HTTPS or localhost and a user click; browser support list not verified.

Exact steps tonight (OUR DESIGN):
1. Laptop with Windows 10/11 and built-in Bluetooth 4.2+ (check Device Manager; avoid CSR8510 dongles, F1). `git clone https://github.com/userx14/omblepy`; `pip install terminaltables bleak`.
2. Take one reading on the HEM-7156T so memory is not empty. Hold the cuff's Bluetooth button until -P- blinks. Run `python omblepy.py -p -d HEM-7156T -t`. Afterwards `-n` for new records only.
3. Wrap it in a short Python script that parses the printed table and posts {sys, dia, pulse, device_time, source:"ble"} to the engine endpoint (D2-01 owns the endpoint).
4. Any other Bluetooth cuff: open nRF Connect on a phone and look for service 0x1810. If present, a 40-line bleak script that subscribes to indications on 0x2A35 reads it (decode flags byte then IEEE-11073 SFLOAT systolic, diastolic, MAP; layout from memory, check against the SIG spec). If absent, the cuff speaks a vendor protocol: stop and use the photo path.

Time to working: OUR ESTIMATE 30 to 60 min with cuff and a good adapter in hand; open-ended if pairing fails.
Failure modes: no HEM-7156T in Sonipat tonight (D1-06-F31 prices are online listings, not shop stock); adapter incompatibility (F1); encrypted Connect models (D1-06-F07); wrong cuff clock (use `-t`); multi-user memory; the Omron phone app and omblepy pairing may compete, so pair with omblepy only (OUR ESTIMATE, not tested).

#### 1(b) Phone photo of any cuff screen, read automatically

Facts:
- D2-02-F4. Katebi et al., PLOS Digital Health 2024, "Automated image transcription for perinatal blood pressure monitoring using mobile health technology", PMID 39356720. YOLOv5 screen localisation plus three-layer CNN, up to 3 digits per row. Mean absolute error on held-out sets: 1.2 / 0.8 mmHg (systolic / diastolic) Georgia IMPROVE (776 images, 48 participants, Omron BP710N); 0.9 / 0.5 mmHg Guatemala Set 2 (1,934 recordings, 570 women). Human transcription MAE: 4.1 / 2.7 mmHg on Guatemala Set 2; 0.5 / 0.3 on IMPROVE. Guatemala Set 1: of 7,205 annotated Omron M7 images, 5,944 (about 82%) were rated poor quality. Errors were "often in the last digit". Failure modes: dark homes, blur, reflections, cropping; other devices untested. Contour-based code (BPimageTranscribe) at https://doi.org/10.5281/zenodo.4383306; data not public. Funders NIH Fogarty, NICHD, Google.org. https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000588 OPENED. CITED. Low-resource setting (Guatemala) evidence.
- D2-02-F5. Same paper: Kulkarni et al. 2021 data with YOLO localisation reached MAE 1.04 / 0.91 mmHg. OPENED (as cited). A search snippet adds Kulkarni 2021: 8,192 Omron M7 images, CNN 91% classification accuracy, systolic MAE 3.19 mmHg on readable images. Frontiers page returned 404. SNIPPET for 91% and 3.19.
- D2-02-F6. Shenoy and Aalami, AMIA 2017 (arXiv 1807.04888): smartphone engine recognises seven-segment digits from glucose and BP monitors "with an accuracy of 98.2%" (digit level; dataset size not on the abstract page). https://arxiv.org/abs/1807.04888 OPENED. CITED.
- D2-02-F7. ssocr: GPL-3.0 or later; Linux, FreeBSD, macOS, Windows via Cygwin; reads one row of digits; no accuracy claim. https://github.com/auerswal/ssocr OPENED 13 Nov 2026. CITED. A BP screen has three rows plus icons, so ssocr needs per-row crops.
- D2-02-F8. Published evaluation of a general vision-language model reading BP monitor screen photos: NOT FOUND (one search). Related only: a 2026 AHA-meeting study found AI chatbots often recommend unvalidated home BP monitors (Gemini 86-91% correct, others about 63-83%). SNIPPET (HealthDay and remio.ai summaries, not opened).
- D2-02-F9. Seven-segment confusions 0 vs 8 and 1 vs 7 reported by Tanoto et al. SNIPPET.

Exact steps tonight (OUR DESIGN):
1. Phone web page (or Telegram bot, D1-06-F54) with camera capture and an overlay: "fill the box with the screen, no flash, tilt to remove glare".
2. Send the image to a vision-capable language model with a strict JSON reply: {"sys":int|null,"dia":int|null,"pulse":int|null,"memory_or_average_icon":bool,"error_code":str|null,"confidence":"high|low"}. Tell it to return null rather than guess.
3. Code checks: 60 <= sys <= 260; 30 <= dia <= 160; sys minus dia >= 10; 30 <= pulse <= 200; reject if a memory or average icon is shown. OUR DESIGN thresholds, not from a source.
4. Read twice (model twice, or model plus ssocr). If they disagree, or confidence is low, force the confirm step. Always show the three numbers back in large type: "Does your screen say this? Yes / Fix". Edits are stored as source:"photo_corrected" with the image kept.
5. Reading time = photo EXIF time (cheap screens rarely show the clock).
Time to working: OUR ESTIMATE 60 to 90 min.
Failure modes: glare and dark rooms (F4); last-digit errors (F4); 0/8 and 1/7 (F9); photo of a memory recall; an old photo or someone else's cuff (the photo proves a screen, not a person or a time); consent for sending health images to a cloud model (record consent on first use).

#### 1(c) Typed entry (fallback, always built)
Three numeric fields with the same checks. Any value that would trigger a step change must be typed twice or backed by a photo. Stored as source:"typed". The engine may require photo or Bluetooth source before proposing a dose increase. OUR DESIGN. Reason: ESH calls patient handwritten logs "often incomplete and inaccurate (misreporting)" (D2-02-F14).

### 2. What makes a home reading count

#### 2.1 Current guidance
- D2-02-F10. AHA scientific statement "Measurement of Blood Pressure in Humans" (Muntner et al., Hypertension 2019, PMID 30827125, PMC11409525), Table 9 "Guidance for Conducting HBPM": rest quietly seated at least 5 minutes, no talking or texting; two readings at least 1 minute apart; morning before antihypertensive medication and evening before bed; preferred 7 days or more (28+ readings), minimum 3 days (12 readings); consecutive days ideal; some guidelines exclude day 1, making the minimum 4 days and preferred 8 days. Table 5 preparation: 3-5 minute seated rest, no talking during rest or measurement, empty bladder, clothing removed from cuff site. https://pmc.ncbi.nlm.nih.gov/articles/PMC11409525/ OPENED. CITED.
- D2-02-F11. ESH Working Group position paper "Home blood pressure monitoring: methodology, clinical relevance and practical application" (Parati, Stergiou et al., J Hypertens 2021, PMC9904446), Box 15: "After a 5 min sitting rest and 1 min between measurements"; "Duplicate morning and evening measurements"; "Before drug intake if treated"; "Seven-day monitoring (not fewer than 3 days)"; measure "Before each office visit and whenever an unusual BP change is suspected"; "HBP threshold for hypertension diagnosis is at least 135/85 mmHg". OPENED. CITED.
- D2-02-F12. Same ESH paper on discarding day 1: a "matter of debate"; "no evidence of an improvement when measurements of the first day were discarded"; impact minimal with more days. OPENED. CITED. (Conflicts in emphasis with AHA F10, which notes some guidelines exclude day 1. Both recorded.)
- D2-02-F13. Same ESH paper, posture wording: the adult text says "standardized sitting posture"; the explicit "Back supported, arm resting at heart level, feet flat on floor" and "Avoid talking during and between measurements" appear in its paediatric section. Devices: "Only clinically validated upper arm-cuff devices recommended"; "monitors more than 4 years old more likely to be inaccurate"; readings kept as "a downloadable electronic log maintained in the monitor memory" or transmitted "for the physician's review". OPENED. CITED.
- D2-02-F14. Same ESH paper: handwritten logbooks "often incomplete and inaccurate (misreporting)"; lists "Limited reliability of BP values reported by patients". No percentage given. OPENED. CITED.
- D2-02-F15. India: Indian Guidelines on Hypertension-IV (2019) home mean threshold >135/85 mmHg (ABPM 24 h >130/80; office >140/90). SNIPPET (search summary; primary JAPI text not opened). A secondary source says Indian clinicians discard day 1 and average the rest: SNIPPET (omnicuris), not confirmed. Indian guideline text on number of days and readings: NOT FOUND.
- Implication for the engine (OUR DESIGN): a "home BP block" = morning and evening, 2 readings 1 min apart, after 5 min seated rest, morning before tablets, 7 days (minimum 3). The engine decides on the mean of valid readings in the block, ignoring day 1 as an option toggled by the doctor (because F10 and F12 differ). Note the IHCI and Gujarat thresholds (140/90, D1-06-F03, F14) are clinic thresholds; the home threshold is 135/85 (F11, F15). D2-01 must decide which the engine uses; flagged, not decided here.

#### 2.2 Published size of each common error

| Error | Effect (systolic / diastolic, mmHg) | Source | Status |
|---|---|---|---|
| Arm resting on lap vs supported on desk | +3.9 (95% CI 2.5-5.2) / +4.0 (3.1-5.0) | D2-02-F16 ARMS trial | OPENED |
| Arm unsupported, hanging at side vs desk | +6.5 (5.1-7.9) / +4.4 (3.4-5.4) | D2-02-F16 | OPENED |
| Arm height below heart, per cm | +0.49 per cm / +0.47 per cm (smaller than the 0.74 per cm hydrostatic prediction) | D2-02-F17 | OPENED (abstract) |
| Back not supported | +5 to +15 / +6 | D2-02-F18 AHA Table 4 | OPENED |
| Legs crossed | +5 to +8 / +3 to +5 | D2-02-F18 | OPENED |
| Supine vs seated | +3 to +10 / about +1 to +5 | D2-02-F18 | OPENED |
| Cuff too small / too large | Higher / lower (no value in AHA) | D2-02-F18 | OPENED |
| Regular cuff on arm needing large cuff | +4.8 systolic | D2-02-F19 Cuff(SZ) trial | OPENED (abstract summary) |
| Regular cuff on arm needing extra-large cuff | +19.5 systolic | D2-02-F19 | OPENED |
| Regular cuff on arm needing small cuff | -3.6 systolic | D2-02-F19 | OPENED |
| Talking or active listening | +10 / +10 | D2-02-F20 Handler 2009 Table 1 | OPENED |
| Cuff over clothing | +5 to +50 systolic | D2-02-F20 | OPENED |
| Distended bladder | +15 / +10 | D2-02-F20 | OPENED |
| Smoking within 30 min | +6 to +20 systolic | D2-02-F20 | OPENED |
| Back unsupported | +6 to +10 systolic | D2-02-F20 | OPENED (differs from AHA F18; both recorded) |
| Arm unsupported, sitting | +1 to +7 / +5 to +11 | D2-02-F20 | OPENED |
| No rest vs 5 min rest | No meaningful difference if SBP <140; from none to at least 4 mmHg if SBP >=140 | D2-02-F21 | OPENED (secondary review) |
| All sources pooled | Individual sources range -23.6 to +33 systolic, -14 to +23 diastolic; 328 studies, 29 sources | D2-02-F22 | OPENED (abstract) |

Fact details:
- D2-02-F16. Liu, Ishigami et al., ARMS crossover randomised trial, JAMA Intern Med 2024, PMID 39373998, DOI 10.1001/jamainternmed.2024.5213; n = 133 adults, Baltimore, Aug 2022 to Jun 2023; NIH extramural support. Values above are difference-in-differences vs desk. Europe PMC abstract OPENED. CITED.
- D2-02-F17. Adiyaman et al., Blood Press Monit 2006;11(6):309-313, PMID 17106314; n = 128, mostly treated hypertensive outpatients; simultaneous both-arm measurement, desk level vs heart level. "The effect of the height differences between the arm positions on the blood pressure readings was smaller than predicted". Europe PMC abstract OPENED. CITED.
- D2-02-F18. AHA 2019 statement Table 4 "Body Position and BP Measurement" (F10 source). OPENED. CITED. Arm below heart and arm held up by patient: direction only, no value.
- D2-02-F19. Ishigami et al., Cuff(SZ) randomised crossover trial, JAMA Intern Med 2023;183(10):1061-1068, PMID 37548984; n = 195 community adults. Authors: miscuffing gave "strikingly inaccurate BP measurements". Europe PMC record OPENED (abstract via summary). CITED. Relevance: Omron HEM-7120 standard cuff fits 22-32 cm; S cuff 17-22 cm is optional (D2-02-F30). Arm circumference must be measured with a tape for every person.
- D2-02-F20. Handler, Perm J 2009 (PMC2911816), Table 1 "Factors affecting accuracy of blood pressure measure"; table carries no citations itself; talking linked in text to Le Pailleur 1998, clothing to Reeves 1995. OPENED. CITED. Older and less rigorous than F16-F19.
- D2-02-F21. Tools for Practice #415 (CFPCLearn, about June 2026) summarising Brady et al., Hypertension 2021, randomised crossover, n = 113: no meaningful difference between no rest and 5 min rest when SBP <140; when SBP >=140, results from no effect to at least 4 mmHg; advice "Consider a five-minute rest before measurement" when SBP >=140. https://cfpclearn.ca/tfp415/ OPENED. CITED (secondary). Original paper not opened.
- D2-02-F22. Kallioinen et al., J Hypertens 2017;35(3):421-441, PMID 27977471, systematic review to June 2015: 328 studies, 29 sources of inaccuracy, 27 with significant directional effects. Abstract OPENED. Per-source values in the full text NOT OPENED (paywalled).

What the clip can and cannot see (OUR DESIGN, linking 2.2 to section 3): arm on lap or hanging (F16) and stillness are measurable with a motion sensor; rest time is measurable by a timer; back support is partly inferable from a trunk sensor; legs crossed, cuff over clothing, cuff size, talking, full bladder and smoking are NOT measurable by the clip and go into a 4-question checklist on the phone before each block.

### 3. The kit-built "reading-quality clip" (OUR DESIGN throughout unless a fact ID is given)

#### 3.1 Purpose
Mark each reading valid or not, with reasons, so the engine only titrates on readings taken properly. It does not measure blood pressure.

#### 3.2 Parts
- 1 x ESP32 dev board (kit).
- 2 x MPU6050 modules: A on the cuff (upper arm), B on the wrist strap (forearm). Same I2C bus: A with AD0 low (0x68), B with AD0 high (0x69). MPU6050 module about ₹145 to ₹275 at Indian retailers (D2-02-F31, SNIPPET).
- Optional 3rd sensor C on the sternum (trunk) for back support: needs a second I2C bus (ESP32 has two) because only two MPU6050 addresses exist.
- 1 x push button (start), 1 x RGB LED or three LEDs, 1 x buzzer if in kit.
- Power: USB power bank. Velcro or elastic, tape, 1 m of 4-core ribbon or jumper wires per remote sensor.

#### 3.3 Wiring
- MPU6050 A and B: VCC to 3V3, GND to GND, SDA to GPIO21, SCL to GPIO22 (shared bus), AD0 of B to 3V3. Keep wires under about 1 m; add 4.7 kOhm pull-ups if the module lacks them.
- Sensor C (optional): SDA GPIO18, SCL GPIO19 on Wire1.
- Button GPIO0 or GPIO4 to GND with internal pull-up. LED on GPIO2 (on-board) or RGB on GPIO25/26/27 through 220 Ohm. Buzzer GPIO15.

#### 3.4 Signal logic and thresholds
Sample all sensors at 50 Hz; low-pass accelerometer for tilt, gyro for motion.

1. Calibration (once per person, 2 min): helper seats the person correctly (back against chair, feet flat, forearm on table, cuff at mid-chest height, checked by eye or photo). Clip stores reference tilt of A and B. Reason: an angle sensor cannot know where the heart is; the reference posture supplies it.
2. Rest timer: person presses button. Clip requires 300 s of rest (F10, F11: 5 min). Rest counts only while "still" (below). If movement breaks stillness for more than 10 s, the timer restarts.
3. Stillness: gyro magnitude below 5 deg/s on A and B for at least 90% of each 10 s window. Thresholds are OUR ESTIMATE, to tune on teammates at 01:00.
4. Arm position:
   - Forearm B pitch within 20 deg of horizontal = forearm resting on a surface. Forearm near vertical = hanging at side (ARMS side position, +6.5 mmHg, F16) -> invalid.
   - Upper arm A tilt within 15 deg of the calibrated reference. Arithmetic (OUR ARITHMETIC): cuff centre about 15 cm from the shoulder; a 15 deg change from 30 deg to 45 deg moves it 15 x (cos30 - cos45) = 15 x (0.866 - 0.707) = 2.4 cm, which at 0.49 mmHg/cm (F17) is about 1.2 mmHg. Lap position lowers the elbow and changes A's tilt; expected to exceed 15 deg (OUR ESTIMATE, to test).
5. Trunk (optional C): tilt within 10 deg of calibration and low sway. Leaning forward off the chair back (back unsupported, +5 to +15, F18) shows as forward tilt.
6. Inflation window: the person presses the button again when they press the cuff's start button (or the clip detects cuff motor vibration on A; OUR ESTIMATE, untested). The measurement window lasts 60 s. Stillness and arm checks must hold through it.
7. Second reading: enforce at least 60 s between readings (F10, F11) with LED countdown.
8. Output per reading: valid = rest_ok AND still_ok AND forearm_ok AND upperarm_ok (AND trunk_ok if C fitted). LED green = valid, red = invalid with a reason code; buzzer on invalid.

#### 3.5 Firmware outline (Arduino-ESP32)
```
setup(): Wire.begin(21,22); init MPU 0x68, 0x69 (+Wire1 for C); WiFi or BLE; load calibration from NVS
loop @50 Hz:
  read accel+gyro A,B(,C); tilt = atan2 on low-passed accel; gyroMag = |gyro|
  state machine: IDLE -> CALIBRATE -> REST(300 s, restart on motion) -> READY (green blink)
                 -> MEASURE(60 s after button) -> GAP(60 s) -> MEASURE -> DONE
  per state: accumulate still_fraction, max tilt deviation A/B/C
  on MEASURE end: build record {clip_id, session_id, t_start, t_end (from NTP), rest_s,
                  still_frac, forearm_dev, upperarm_dev, trunk_dev, valid, reasons[]}
                  POST JSON to engine /quality (WiFi) or notify over BLE to the phone page
```
Libraries: Adafruit_MPU6050 or a raw-register read (faster to debug). NTP time over WiFi is needed so clip windows and photo times line up.

#### 3.6 Pairing a quality flag with a reading
- Bluetooth path: omblepy gives the cuff's own timestamp (after `-t` clock sync, F1). Join to the clip window whose MEASURE interval contains the cuff time (tolerance plus or minus 90 s).
- Photo path: the phone page holds the session_id. The photo must be taken within 3 min after a MEASURE window ends; the record joins to that window. The clip window ID is shown on the phone so the person sees "Reading 2 of 2: posture OK".
- Typed path: joins the same way by entry time, but stays "typed".
- The engine counts a home BP block as usable only if, say, at least 75% of readings are valid and at least 3 days are covered (F10, F11). The 75% figure is OUR DESIGN, a placeholder for the doctor to set.

#### 3.7 What a pulse sensor (MAX30102) could add
- Cross-check: pulse from the finger sensor vs the pulse on the cuff screen within plus or minus 5 bpm. That ties the reading to the person wearing the clip at that minute (a binding check against a photo of an old or borrowed reading). OUR DESIGN.
- Rest marker: heart rate settling during the 5 min rest.
- Irregular rhythm: a crude irregularity flag (oscillometric cuffs are less reliable in arrhythmia; source NOT SEARCHED tonight).
- Limits: MAX30102 has no large independent clinical validation (D1-06-F19); finger PPG is motion-sensitive; another sensor and cable.
- Verdict for tonight (OUR DESIGN): optional stretch after 07:00, only the pulse cross-check. Not on the critical path.

### 4. Adherence signal as an input to the dose decision (OUR DESIGN unless a fact ID is given)

Why: the Gujarat protocol says "Check for compliance at each visit before titration of dose or addition of drugs" and, after step 5, check regular use before referral (D1-06-F14). Stepping up a dose that was not being taken is the error to prevent.

Options from kit parts:
| Sensor | Build | What it detects | Honest limits |
|---|---|---|---|
| Reed switch + magnet | Reed on box body, magnet on lid; ESP32 GPIO with pull-up, deep-sleep wake on change | Lid opened, time | Opening is not swallowing; open-and-close for other reasons; strips taken out for the week |
| Hall sensor (A3144 or ESP32 built-in hall) | Same as reed; ESP32 internal hall sensor is weak and removed in newer ESP-IDF (from memory, not verified) | Lid opened | As above |
| Light gate (LDR or IR pair in box) | LDR inside an opaque box; light when lid opens | Lid opened | Fails in the dark; same ingestion limit |
| Load cell + HX711 | Strip box on a 1 kg bar load cell | Weight drop | One tablet is about a tenth to a few tenths of a gram (OUR ESTIMATE); cheap cells drift and vibrate; detecting one tablet is unlikely without care; better at detecting a whole strip removed |
| Phone tap | "Taken" button on the morning BP page, before the reading | Self-report | Self-report overstates adherence (from memory, NOT SEARCHED) |

Recommendation for tonight (OUR DESIGN): reed switch on a pill box, 14-day window, expected openings = doses per day x days. If openings fall below 80% of expected (threshold OUR DESIGN, a placeholder for the doctor) the engine proposes "check adherence and support" instead of "step up", and asks the patient one question in the morning flow ("Did you take your BP tablet yesterday?"). Combine sensor and answer; disagreement goes to the doctor.

Evidence that boxes alone do not help: ASCENT tuberculosis pillboxes, n = 23,483, no outcome gain (D1-02-F59); inhaler reminders raised adherence 30% to 84% with school absence unchanged (D1-02-F01); MedISAFE-BP reminder app 0.5 mmHg, p = 0.78 (D1-01-F06).
How this use differs: the signal does not remind anyone. It changes which branch of the protocol fires (titrate vs support adherence), the branch the protocol already requires a human to check (D1-06-F14). Whether this improves outcomes is untested: no trial of adherence-gated titration was searched tonight (NOT SEARCHED).

### 5. Cuffless and phone-only blood pressure, as of 2026
- D2-02-F23. FDA 510(k) K250415, "G0 Blood Pressure Monitoring System (G0)", Aktiia SA, product code DXN, decision 2 Jul 2025, Substantially Equivalent. https://api.fda.gov/device/510k.json?search=applicant:aktiia OPENED. CITED. Search snippets add: first OTC cuffless clearance, trial of 140 patients vs double auscultation, CE Class IIa in Europe, US availability in 2026 (SNIPPET, MobiHealthNews and MassDevice, not opened). Whether it needs cuff calibration: NOT FOUND tonight.
- D2-02-F24. Other FDA-cleared cuffless devices per press reports: Biozen BP1000 fingertip, "calibration-free", 510(k) May 2026; Wellvii BP Go finger device, August 2026; Biobeat. All SNIPPET (press releases, not opened, not checked in openFDA).
- D2-02-F25. ESH recommendations for validating cuffless BP devices, J Hypertens 2023, PMID 37303198: says there are "no generally accepted protocols"; proposes six tests (static, device position, treatment, awake/asleep, exercise, recalibration) for intermittent cuffless devices. Europe PMC abstract OPENED. CITED.
- D2-02-F26. "Cuffless Blood Pressure Measurement: Where Do We Actually Stand?", Hypertension 2025, PMID 40231350: "no compelling evidence that pulse wave analysis and pulse arrival time can provide significant added value"; many accuracy claims used "inadequate testing procedures". Abstract OPENED. CITED. ESH nocturnal BP position paper 2025 (PMID 40509714): cuffless technologies "require further validation". OPENED (abstract).
- D2-02-F27. Cuff device standard ISO 81060-2: mean difference within plus or minus 5 mmHg with SD no more than 8 mmHg over paired readings, typically 85 subjects; a second per-subject criterion (SD limit about 6.95 mmHg at zero mean). SNIPPET (validation papers quoting the standard; ISO text not opened). ISO 81060-3 (cuffless): NOT OPENED.
- Indian (CDSCO) clearance of any cuffless BP device: NOT SEARCHED.
- Why not tonight (OUR DESIGN reasoning from F25, F26 and D1-06-F19): the treatment step changes by about 5-10 mmHg bands, the same size as cuffless error; no accepted validation protocol (F25); a dose-changing loop needs the most trusted input, which is a validated upper-arm cuff (F13); a MAX30102 build has no validation of its own. A cuffless claim would draw the hardest jury question and cannot be tested by noon.

### 6. Low-cost cuffs sold in India on independent validation lists
| Cuff | Validation listing | Price (date) | Bluetooth |
|---|---|---|---|
| Omron HEM-7120 (HEM-7120-IN) | Medaval: passed ESH-IP 2010 in general population, 2 stars; STRIDE BP "Self-measurement for adults (Unavailable) (Preferred)" as shown on Medaval; study Zhang et al., Blood Press Monit 2021;26(6):435-440, PMID 34001755 (D2-02-F28, OPENED) | RRP ₹2,334 incl. taxes (Omron India page, undated, OPENED, D2-02-F30); ₹1,849 on 1mg and Smartprix (10 Jun 2026), ₹1,898 Flipkart (SNIPPET) | No (F30) |
| Omron HEM-7124 (HEM-7124-IN) | Medaval lists it in the HEM-7120 family by internal declaration (D2-02-F28); Omron's own table grade B (ESH-IP 2010) (F29) | NOT FOUND | No (not checked) |
| Omron HEM-7156T | Omron's own validation table: general population and pregnancy, grades C (ISO 81060-2:2009), G (ESH-IP 2010), I (Universal Standard) (D2-02-F29, THEIR CLAIM). Independent Medaval or STRIDE BP page: NOT OPENED | ₹2,593 to ₹2,892 (D1-06-F31, SNIPPET, mid-2026) | Yes, omblepy-readable (F1) |
| Rossmax CF175 | Passed International Protocol 2010 (PubMed) and on Medaval ESH list (2023) | NOT FOUND | NOT FOUND |
| Dr Morepen BPOne BP-01 | Medaval: "There appears to be no peer-reviewed clinical validation information available"; "This device has not been clinically validated." (D2-02-F32, OPENED, undated) | NOT SEARCHED | NOT SEARCHED |
| Dr Trust models | NOT FOUND on Medaval in one search | NOT SEARCHED | |

- D2-02-F28. Medaval Omron HEM-7120 page. https://medaval.ie/resources/EN/devices/Omron-HEM-7120.php OPENED, undated. CITED.
- D2-02-F29. Omron Healthcare India "Why choose OMRON" validation table (rows HEM-7120-IN, HEM-7124-IN grade B; HEM-7156, HEM-7156T, HEM-7361T grades C, G, I incl. pregnancy). HEM-7121J not listed. https://omronhealthcare-ap.com/in/Why-choose-omron OPENED, undated. THEIR CLAIM (manufacturer table citing studies).
- D2-02-F30. Omron HEM-7120 India page: RRP INR 2,334 incl. taxes; cuff HEM-CR24 22-32 cm; optional S cuff HEM-CS24 17-22 cm; no Bluetooth. https://www.omronhealthcare-ap.com/in/product/12-hem-7120 OPENED, undated. CITED.
- D2-02-F31. MPU6050 module retail: Robu ₹165 incl. GST, Zbotic ₹233 + GST, others ₹144 to ₹200. SNIPPET, undated.
- D2-02-F33. STRIDE BP lists 620 devices with filters for Home and Upper arm; the search parameter in the URL did not filter server-side, so model-level lookups for Omron failed by fetch. https://www.stridebp.org/bp-monitors OPENED 13 Nov 2026.
- Can the team buy one tonight in Sonipat? UNCERTAIN. Online listings exist (1mg, PharmEasy, Flipkart) but none was confirmed for night delivery to a Sonipat pincode; Blinkit listing NOT FOUND. A chemist near campus may stock HEM-7120 (OUR ESTIMATE; not checked). Ask teammates, staff and the campus health centre for any cuff first.

### 7. Bill of materials (prices as found; dates shown; SNIPPET unless marked OPENED)

| Item | Usually in a maker kit | Buy tonight if a shop is open | Fallback if not |
|---|---|---|---|
| Upper-arm cuff (the reference) | No | Omron HEM-7120, RRP ₹2,334 (OPENED, undated, F30); ₹1,849 online (10 Jun 2026) | Any cuff a teammate, staff member or health centre owns; photo path works with any make (section 1b) |
| Bluetooth cuff | No | Omron HEM-7156T, ₹2,593 to ₹2,892 (mid-2026, D1-06-F31) | Skip the BLE path; photo path only |
| Tape measure (arm circumference, cuff size check, F19) | Sometimes | Tailor's tape, about ₹50 (OUR ESTIMATE) | Paper strip marked against a ruler |
| ESP32 dev board | Yes | | Arduino Uno + HC-05 or USB serial to laptop |
| MPU6050 x 2 (x 3 with trunk) | Yes (task says common) | ₹144 to ₹275 each (undated, F31) | One MPU6050 on the forearm only (covers lap and side positions, F16) |
| Push button, LEDs, buzzer, resistors | Yes | | Phone page buttons replace the clip button |
| Jumper wires, breadboard, 4.7 kOhm | Yes | | |
| Velcro, elastic, tape | Often | Stationery shop, OUR ESTIMATE under ₹100 | Medical tape, rubber bands |
| Reed switch + magnet (adherence) | Sometimes | Not priced (NOT SEARCHED) | Light gate with LDR (kit) or phone "taken" tap |
| Pill box with lid | No | Any chemist, OUR ESTIMATE under ₹100 | Cardboard box with a flap |
| MAX30102 (optional) | Yes (task says common) | | Skip |
| Bluetooth 4.2+ laptop or dongle (for omblepy) | Laptops | Avoid CSR8510 dongles (F1) | Run omblepy on a Mac or a Raspberry Pi 4/5 (F1) |
| Power bank, USB cable | Personal | | Laptop USB |
| Phone with camera, laptop | Personal | | |
Cash outlay if buying one non-Bluetooth cuff and small parts: about ₹2,000 to ₹2,600 (OUR ARITHMETIC: ₹1,849 to ₹2,334 cuff + about ₹300 tape, velcro, box; MPU6050s from kit).

### 8. Test protocol for noon (runnable on teammates; OUR DESIGN)

Ethics and framing: volunteers are healthy teammates and other participants who agree verbally; no names stored, IDs only; anyone reading at or above 180/110 is told to see a doctor and is not "tested further". No clinical claim. This tests the pipeline and the clip, not cuff accuracy and not patient outcomes.

Sample size reachable: OUR ESTIMATE 6 to 10 people. One cuff, about 8 min per condition (5 min rest + 2 readings 1 min apart), 3 conditions per person = about 25 min per person. With one cuff, 8 people = about 3.3 h; a second cuff halves it.

Per person:
1. Measure arm circumference; record whether the cuff fits (22-32 cm for HEM-7120, F30). Exclude out-of-range arms from the posture comparison.
2. Calibrate the clip in correct posture.
3. Conditions in random order (coin flip): C = correct (back supported, feet flat, forearm on desk, cuff at heart level, silent, 5 min rest); W1 = arm hanging unsupported at the side; W2 = arm on lap. Optional W3 = talking, W4 = no rest. Each condition: 2 readings 1 min apart. Repeat C at the end if time allows (BP drifts down over a session; the C-W-C sandwich exposes drift).
4. Every reading: clip record, cuff screen photo (twice: once well lit, once deliberately at an angle or with glare), human transcription by a second person, BLE readout if the HEM-7156T is present.

What to report (results table template):
| Measure | n | Result | Comparison |
|---|---|---|---|
| Clip flags invalid when posture was wrong (W1, W2) | readings | x / y | (sensitivity, small n) |
| Clip passes valid when posture was correct (C) | readings | x / y | (specificity, small n) |
| Mean of (W1 - C) systolic, diastolic | people | mean, range | ARMS +6.5 / +4.4 (F16) |
| Mean of (W2 - C) systolic, diastolic | people | mean, range | ARMS +3.9 / +4.0 (F16) |
| Photo reader exact match per field (sys, dia, pulse), good photos | photos | % | Katebi MAE 0.9-1.2 sys (F4) |
| Same, bad photos | photos | % and how many sent to confirm | |
| Photo reader MAE vs human transcription | photos | mmHg | |
| BLE readout vs screen | readings | x / y exact | expected all exact |
| End-to-end: reading to engine proposal | runs | seconds | |

Honest reporting rules: give n and ranges, not p-values; say teammates are young and mostly normotensive, so posture effects may differ from patients'; do not claim the clip improves BP control; state that the sensitivity numbers come from deliberately exaggerated wrong postures; report every failed photo and every clip false alarm. Seed the engine with synthetic high readings for the step-change demo (D1-06 Q6(a)) and label them synthetic.

### 9. Hour-by-hour hardware plan, 23:00 13 Nov to 12:00 14 Nov (one or two hardware students; H1 = clip, H2 = cuff and photo path; OUR DESIGN)

| Time | H1 (clip) | H2 (cuff reading) | Checkpoint / cut line |
|---|---|---|---|
| 23:00-23:30 | Inventory kit: ESP32, MPU6050 count, buttons, LEDs | Find a cuff (teammates, staff, health centre); order HEM-7120 if a seller confirms night delivery | 23:30: is there a cuff? If none by 00:30, photo path is tested on a borrowed cuff in the morning only |
| 23:30-00:30 | ESP32 + MPU6050 A printing tilt and gyro over serial | Photo page: capture + vision-model call returning JSON | 00:30: one sensor streams; one photo parsed |
| 00:30-01:30 | Second MPU6050 (0x69); tilt for both; mount on cuff and wrist strap | Confirm screen + plausibility checks + post to engine endpoint (with D2-01) | 01:30: CUT LINE: if sensor B fails, continue with forearm sensor only |
| 01:30-02:30 | State machine: calibrate, 5 min rest, measure, gap; LEDs | If HEM-7156T present: omblepy pairing and readout (time box 60 min) | 02:30: FIRST DEMO: one reading flows photo -> engine; clip shows green/red. If omblepy not working by 02:30, drop BLE |
| 02:30-03:30 | Tune stillness and tilt thresholds on two teammates | Second read (model twice or ssocr) + disagreement rule | |
| 03:30-04:30 | WiFi + NTP + POST quality record; join with readings by time | Typed fallback; source labels | 04:30: quality flag visible next to each reading in the engine |
| 04:30-05:30 | Reed-switch pill box (wake on change, post event) | Adherence question in the morning flow | 05:30: CUT LINE: if pill box not done, use phone "taken" tap |
| 05:30-06:30 | Rest / sleep in shifts | Rest / sleep in shifts | |
| 06:30-09:30 | Run test protocol (section 8) | Photograph and transcribe every reading; BLE if present | 09:30: STOP TESTING whatever n is |
| 09:30-10:30 | Fill results table | Count photo reader matches | |
| 10:30-11:30 | Demo rehearsal: correct vs arm-at-side, clip turns red, engine refuses to titrate | Rehearse photo of a cheap cuff -> confirm -> engine | Optional MAX30102 pulse cross-check only if all above done by 07:00 |
| 11:30-12:00 | Freeze hardware, pack spares | Freeze | |

Critical path: cuff in hand -> photo read -> engine; then clip forearm sensor -> rest timer -> valid flag joined to the reading. Everything else is cut-able.

### 10. The Japan angle on devices
- D2-02-F34. Omron Healthcare (Kyoto): worldwide cumulative sales of its BP monitors passed 400 million units, announced 29 Sep 2025; first monitor in 1973; vision "Going for ZERO" (eradicating cerebro-cardiovascular events). The release claims "the world's most recommended blood pressure monitors by healthcare professionals" (Frost & Sullivan, Kantar surveys) and makes no market-share figure. https://healthcare.omron.com/press-releases/omron-healthcare-exceeds-400m-blood-pressure-monitors-sold OPENED. THEIR CLAIM.
- D2-02-F35. Omron India page: monitors "available in over 130 countries/regions"; cites a Fuji Keizai survey and global cumulative sales to Sep 2025 without a figure. OPENED (F29 page). THEIR CLAIM. Omron's share of the Indian home BP market: NOT FOUND.
- D2-02-F36. Omron acquired Luscii Healthtech (Netherlands), announced 5 Apr 2024 in Kyoto; seed investment in 2018; Luscii works with about 70% of Dutch hospitals, covers over 150 conditions including chronic hypertension; helps providers "monitor and guide patients remotely". No mention of medication titration. https://healthcare.omron.com/press-releases/omron-healthcare-acquires-luscii-healthtech OPENED. THEIR CLAIM. Adaptive depth from this page: 1-3 (monitoring with clinician guidance); titration not stated.
- D2-02-F37. Japan: Omron Healthcare, telemedEASE and PORT offer an online hypertension treatment support service. SNIPPET (omron.com page returned 403). Details NOT FOUND.
- D2-02-F38. CureApp HT, Japan: first standalone app approved as a medical device for hypertension; insurance launch 1 Sep 2022; renamed "CureApp Blood Pressure"; Teijin Pharma co-marketing from June 2024. SNIPPET. Pivotal trial HERB-DH1 (Kario et al., Eur Heart J 2021;42(40):4111-4122, PMID 34455443): open-label, 12 Japanese sites, n = 390 (199 vs 191); 24-h ambulatory SBP at 12 weeks -2.4 mmHg (95% CI -4.5 to -0.3); home BP -4.3 mmHg (-6.7 to -1.9). Europe PMC record OPENED. CITED. The app gives lifestyle guidance (adaptive depth 3), not drug titration. Which home cuffs were used in the trial: NOT FOUND. An Omron-CureApp partnership: NOT FOUND.
- D2-02-F39. Omron and UCSF launched a 2026 AFib trial using OMRON Connect readings in hypertension management. SNIPPET.
- A Japanese programme pairing a cuff maker's devices with drug titration by protocol: NOT FOUND.

### 11. Three hardest mentor questions on hardware and measurement (honest answers)

1. "Your clip measures angles, not heart level. How do you know the cuff is at heart level?"
   It does not know absolute height. It compares each reading with a supervised reference posture and catches the two common errors with published sizes: arm on lap (+3.9 systolic) and arm hanging at the side (+6.5) (F16). Our tolerance is about 1 mmHg of hydrostatic shift (section 3.4 arithmetic using F17). Back support is only partly sensed; legs crossed, clothing, cuff size and talking are checklist items, not sensed. Tonight's numbers show whether it separates deliberately wrong from correct posture on a few teammates, nothing more.
2. "Patients can photograph an old reading, and the vision model can misread. Why trust the number that changes someone's dose?"
   The published image readers reach about 1 mmHg mean error on good images, but 82% of field images in one low-resource dataset were poor quality and errors cluster in the last digit (F4); no published test of a general vision-language model on BP screens was found (F8). So every read is shown back for confirmation, two reads must agree, memory-recall screens are rejected, and a dose step-up needs a block of readings over at least 3 days (F10, F11), not one photo. The doctor approves every change. A photo cannot prove who took the reading or when; the clip time-join and the optional pulse cross-check narrow that gap but do not close it.
3. "Is a ₹2,000 cuff accurate enough to titrate on, and in Indian patients with large arms?"
   Use only cuffs on an independent validation list: the Omron HEM-7120 passed ESH-IP 2010 and is listed by Medaval (F28); a popular Indian brand model is listed as not validated (F32). Validation standards allow a mean difference within 5 mmHg, SD up to 8 (F27, SNIPPET). Cuff size matters more than brand: a regular cuff on an arm needing a large one reads 4.8 higher, on an extra-large arm 19.5 higher (F19); the HEM-7120 standard cuff fits 22-32 cm (F30), so the app must ask for arm circumference and refuse readings outside the cuff range. ESH warns monitors over 4 years old drift (F13); the app asks the cuff's age. Indian-population validation of these models: NOT FOUND.

## NOT FOUND / NOT SEARCHED
- NOT FOUND: India-sold cuffs exposing the standard 0x1810 service; which Omron telehealth models expose it; published evaluation of a vision-language model reading BP screens; Indian guideline text on home-reading days and counts (only the 135/85 threshold, SNIPPET); Aktiia calibration requirement; Omron India market share; Omron-CureApp partnership; HERB-DH1 cuff model; Japanese cuff-plus-titration programme; independent STRIDE BP or Medaval page for HEM-7156T; Dr Trust validation; HEM-7124 price; night delivery of a cuff to a Sonipat pincode; Kallioinen per-source values (paywalled); ESH 2021 practice guideline full text (paywalled; position paper used instead).
- NOT SEARCHED: CDSCO status of cuffless devices; ISO 81060-3 text; reed switch and HX711 prices; self-reported adherence bias; arrhythmia effect on oscillometric accuracy; MPU6050 tilt accuracy; any trial of adherence-gated titration; Kulkarni 2021 full text (404).

Searches used: 18



