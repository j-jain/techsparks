# R3-build-01 — Build feasibility, set 1: U4, U1, A1, E1  (agent: Opus, date 2026-11-03)

Method and conventions
- Prices were read on 3 Nov 2026. electronicscomp.com prices come from its own search and product pages; the item pages I opened show prices **excluding 18% GST**. robu.in and zbotic.in block page fetches, so their prices come from search-result text and are marked "(snippet)". Some of those listings were 7–11 months old when the search engine indexed them. Amazon.in prices are also "(snippet)".
- Delivery-risk flag: **[R]** = I saw the item out of stock somewhere, the stock status is not shown, or the listing is old. Order every [R] item by **5 Nov** from two sellers, and test each part for DOA (dead on arrival) the day it arrives.
- Event clock: on 13 Nov sunset in Sonipat is 17:27, and on 14 Nov sunrise is 06:45 (https://www.sunrise-and-sunset.com/en/sun/india/sonipat/2026/november, read 3 Nov 2026). The build opens after dark. This matters most for U1.
- Roles: **E** = embedded CS, **M** = ML/vision CS, **W** = web/stats CS, **H** = hardware, **H2** = mechanics/3D printing (sixth member, if any), **B** = bio/wet-lab member. In a team of 4, W merges into M and H2 into H.
- Assumption to confirm with the organisers: parts may be bought and DOA-tested before the event but not assembled before 18:00 on 13 Nov. Pre-event *data* (dog photos, phone lift traces, a downloaded dataset) is allowed. Check the SPARK Night rules on both points.
- Problem numbers come from the Round 2 files (R2-01, R2-02, R2-03). The claims check (R3-claims-01/02) may correct them. Use its values in the final thesis.

---

## U4 Lift black-box retrofit

### 1. Bill of materials

**Bring / pre-order (two sensor boxes: one for the real lift in Plan A, one for the model shaft in Plan B)**

| # | Item | Qty | Source (listing) | Unit ₹ | Line ₹ | Risk |
|---|---|---|---|---|---|---|
| 1 | Espressif ESP32-S3-DevKitC-1-N8 (lift box: RAM for 1 kHz IMU buffers) | 1 | electronicscomp, listed on https://www.electronicscomp.com/index.php?route=product/search&search=ESP32-S3 | 1,101 | 1,101 | — |
| 2 | Waveshare BMP390 barometer. Bosch rates relative accuracy at ±0.03 hPa ≈ ±25 cm and absolute at ±0.50 hPa (https://bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp390, snippet) | 2 | https://www.electronicscomp.com/waveshare-bmp390high-precision-barometric-pressure-sensor-barometric-pressure-altitude-temperature-measuring | 1,045 | 2,090 | **[R]** stock not shown. The same board at Hubtronics costs ₹874.38 incl. GST and showed "0 in Stock" (https://hubtronics.in/environment-sensors/bmp390-barometric-pressure-sensor) |
| 3 | VL53L1X ToF sensor, 4 m range (door state across a real lift car) | 1 | Holybro https://www.electronicscomp.com/holybro-st-vl53l1x-lidar (Waveshare version ₹1,538) | 1,465 | 1,465 | **[R]** stock not shown |
| 4 | VL53L0X ToF sensor, 2 m range (levelling on the model) | 2 | https://www.electronicscomp.com/vl53l0-tof-based-lidar-laser-distance-sensor | 245 | 490 | — |
| 5 | MPU6050 6-axis IMU | 3 | https://www.electronicscomp.com/mpu6050-triple-axis-gyro-accelerometer-module | 122 | 366 | — (probably also in the kit) |
| 6 | PN532 NFC V3 kit (reader plus card/tag) for the technician tap | 1 | https://www.electronicscomp.com/pn532-nfc-rfid-read-write-module-v3-kit | 279 | 279 | — |
| 7 | DS3231 RTC | 2 | https://www.electronicscomp.com/ds3231-real-time-clock-module-3.3v-5v-precise-for-raspberry-pi | 139 | 278 | — |
| 8 | Micro SD card module | 2 | https://www.electronicscomp.com/micro-sd-card-module-india | 36 | 72 | — |
| 9 | MC-38 magnetic door contact | 3 | https://www.electronicscomp.com/mc-38-wired-door-window-sensor-magnetic-switch-home-alarm-system | 35 | 105 | — |
| 10 | Adafruit ATECC608 breakout (signs log heads; the key never leaves the chip) | 1 | https://robu.in/product/adafruit-atecc608-breakout-board-stemma-qt-qwiic/ (snippet, listing ~324 days old) | 729 | 729 | **[R]** |
| 11 | NEMA17 42HS40-1704 stepper, 7.2 kg·cm (winch) | 1 | https://www.electronicscomp.com/42hs40-1704-nema17-72-kg-cm-stepper-motor-round-type-shaft | 782 | 782 | — |
| 12 | A4988 stepper driver | 2 | https://www.electronicscomp.com/a4988-stepper-motor-driver-controller-board-red | 79 | 158 | — |
| 13 | Shaft frame: 2 × 1.5 m aluminium angle or wooden battens, guide strings or rods, spool, 2 bearings, braided fishing line, MDF base, packing foam | — | local hardware shop (assumption) | — | 800 | — |
| | **Subtotal** | | | | **8,715** | |

The electronicscomp lines (₹7,186) are ex-GST, so add ~₹1,290 GST. **Delivered total ≈ ₹10,000** (my arithmetic; shipping charges not checked).

**Expect in the kit:** ESP32 boards ×2 (model box and rig controller); a BMP280 as the fallback barometer; SG90 servos ×2 (door and free-fall latch); a 12 V 2 A adapter; breadboards and jumpers; USB cables; a multimeter; a 3D printer and PLA (makerspace).
**Bring:** 2 commercial USB power banks (no loose LiPo cells); 2 microSD cards; 2 Android phones with barometers and the phyphox app (its "Elevator" experiment measures speed and height from the pressure sensor, https://phyphox.org/experiment/elevator/); a tape measure and steel ruler; foam tape or Velcro; cable ties.
**Not needed for the demo:** a 4G Cat-1 modem. It is only in the product BOM, and electronicscomp had no A7670C listing.

### 2. Hour-by-hour plan

| Time | E (firmware) | M (ML) | W (web/stats) | H / H2 (hardware) | B (test officer) |
|---|---|---|---|---|---|
| 18:00–18:30 | All: roles, Plan A go/no-go (the written permission must already exist), safety brief | | | | |
| 18:30–20:00 | Drivers: IMU 1 kHz via FIFO, BMP390 at 50 Hz, ToF at 20 Hz, reed switch; SD logging; Wi-Fi/MQTT to a laptop | Record 20 real trips with phyphox on 2 phones in a campus lift; write trip segmentation on these traces | Dashboard skeleton (live trace, trip list, alarms); hash-chained log plus verifier | H: solder the lift box (S3 + BMP390 + MPU6050 + VL53L1X + RTC + SD + PN532 + ATECC608). H2: start the 3D print of the car (2–3 h); build the frame; mount the spool | Print the randomised fault schedules (dev and test, sealed), trip log sheets and the permission letter |
| 20:00–21:00 | Bench-test the lift box with H | Trip features: duration, peak \|a\|, peak jerk, vibration RMS in bands, barometric Δh, levelling | NFC tap → signed "visit" record | H + B with the facilities escort: mount the box in the campus lift (ceiling corner, foam tape, VL53L1X on the back wall aimed at the door, no contact with any control). Logging starts and runs to 09:30 | 30 scripted rides with known floor sequences and a stopwatch (ground truth for floor detection) |
| 21:00–23:00 | Rig controller: stepper profiles (3 speeds; landings at 0/50/100/150 cm); servo door; servo latch; a shared GPIO "fault" line to the sensor box for latency | Rules: door-open-while-moving, free-fall, jerk, levelling, entrapment | Alarm panel; fault-injection button | H2: finish the shaft, door, latch, foam stop and catch line | Check the rig against the safety list |
| 23:00–02:00 | All: model box on the shaft; first normal trips; tuning starts | | | | |
| **02:00 milestone** | Live dashboard on the model: trips counted, floor shown, "MOVING WITH DOOR OPEN" fires, free-fall fires, an NFC tap appears as a signed visit, and editing one stored record turns the verifier red | | | | |
| 02:00–04:00 | Dev dataset: 50 normal trips + 20 faults. B injects faults blind from the schedule. M tunes thresholds and an isolation forest on dev data only. W and H2 sleep. | | | | |
| 04:00–04:30 | Freeze thresholds; write the hash of the code and config into the log (the honesty anchor) | | | | |
| 04:30–06:30 | Test dataset: 50 normal trips + 20 faults on a fresh random schedule. E and M sleep. | | | | |
| 06:30–08:00 | — | Test-set metrics | Plots | H: tidy the rig for the demo | Results table |
| 08:00–09:30 | — | — | Hand-count 1 h of trips with B at the Plan A lift lobby (morning traffic) | Retrieve the lift box at 09:15 with the escort | Hand count |
| 09:30–10:30 | — | Plan A analysis: trips vs hand count; floors vs the 30 scripted rides; ride quality | | | |
| 10:30–12:00 | Thesis one-pager, 3-minute script, slides, two dry runs with the live rig | | | | |

**Fallbacks**
- BMP390 dead or not delivered: use the BMP280 from the kit. Its relative accuracy is about ±1 m (background, not verified), which still separates ~3 m floors in a real lift. On the model, take height from step counts plus ToF.
- VL53L1X fails: use the reed switch on the model door. On the real lift, report door state as "not measured".
- Stepper winch fails: hand-crank the spool. Faults are still injectable (door servo, hand-stopped jerk, latch drop). Run 40 normal trips + 20 faults instead of 100 + 40.
- Plan A refused: run Plan B, and use phyphox traces of 20–30 real trips as the real-lift dataset for trip and floor detection.

### 3. Test protocol

**Plan B rig.** A 1.5 m shaft with 4 landings 50 cm apart. Each landing is ≈ 6 Pa of pressure change (air ≈ 11.8 Pa per metre; my arithmetic), against the BMP390's typical ±3 Pa relative accuracy, so the barometer alone is marginal on the model. Model floor detection therefore fuses the barometer with the IMU. Barometric floor detection is validated properly only in Plan A or on the phone traces. Car ~300 g; speeds 5, 10 and 15 cm/s.
- Normal trips: 100 (random floor pairs, 3 speed profiles), 50 dev and 50 test.
- Faults: 40, 20 dev and 20 test:

| Code | Fault | Injection | n dev/test | Detection rule (thresholds set on dev) |
|---|---|---|---|---|
| F1 | Moving with door open | servo opens the door mid-trip | 5/5 | door ≠ closed AND \|v\| > v_min for > 100 ms |
| F2 | Abrupt stop / jerk | hard stepper stop from 15 cm/s | 5/5 | \|jerk\| > θ_j |
| F3 | Free-fall, 10 cm | servo releases the latch; the car drops on rails onto foam, held by a catch line | 5/5 | \|a\| < 0.3 g for > 40 ms. A 10 cm free fall lasts ≈ 143 ms (t = √(2h/g)) |
| F4 | Levelling offset | stop 10, 20 or 30 mm off the landing mark | 5/5 | \|ToF height − landing\| > 10 mm |
| F5 (optional) | Entrapment | stop between landings, door closed, 60 s | extra | not at a landing (±20 mm) AND door closed AND t > 60 s |

- Outputs, per fault type: precision; recall with a Wilson 95% CI; false alarms per 100 normal trips; detection latency (median and p95) = alarm timestamp − GPIO fault-edge timestamp, both on the sensor ESP32's clock; levelling MAE against steel-ruler readings; isolation-forest AUC (trained on normal dev trips only) on the test set.
- Honesty rule: thresholds are frozen at 04:00 and their hash is written into the log. Only test-set numbers are headline numbers.

**Plan A (real campus lift), ~12 h of logging**
- Trip count against a 1 h hand count (08:00–09:00).
- Arrival-floor accuracy on 30 scripted rides, and height error per floor (m).
- Per-trip ride quality, reported in the style of ISO 18738-1: maximum and A95 peak-to-peak vibration, acceleration and jerk. This is not a compliant measurement. The standard specifies its own instrument and processing chain, sets no acceptance levels, and has been replaced by ISO 8100-34 (https://www.iso.org/standard/54395.html and the AFNOR listing, snippets).
- Door-open count against the hand count, if the ToF sensor is mounted. Uptime and data loss %.

**Results templates**

Table U4-B (Plan B test set)
| Fault | n injected | TP | FN | FP (in 50 normal trips) | Precision | Recall (95% CI) | Latency median / p95 (ms) |
|---|---|---|---|---|---|---|---|
| F1 door open while moving | | | | | | | |
| F2 jerk | | | | | | | |
| F3 free-fall | | | | | | | |
| F4 levelling | | | | | | | |
| False alarms per 100 normal trips | | | | | | | |
| Levelling MAE (mm), n stops | | | | | | | |
| Anomaly AUC (test) | | | | | | | |

Table U4-A (Plan A real lift)
| Metric | Box | Ground truth | Error |
|---|---|---|---|
| Trips in 1 h | | hand count | |
| Arrival floor correct (30 rides) | | scripted log | % |
| Peak accel / jerk, median over trips | | — | — |
| Door-open events | | hand count | |
| Hours logged / data loss % | | — | |

**Safety.** Never enter the shaft, the car top or the machine room. Mount the box only inside the car, with the facilities escort. The box runs on a commercial power bank with no wiring into the lift. Test free-fall only on the model, with the foam stop and catch line, hands clear. Limit the stepper current. Nobody jumps in or misuses the real lift to "simulate" a fault. Everything in the hall is 12 V or USB; there is no live mains.

### 4. Demo script and Deep Tech Thesis

**3-minute demo**
- 0:00–0:25 — "46% of Indian lift users or their families were stuck at least once last year (LocalCircles, ~11k responses, Jul 2026). Pune had 61,521 lifts and inspected 5,694 of them in five months." One still from the 1.5 M-view Lucknow clip.
- 0:25–0:50 — The gap: OEM IoT covers only OEM-maintained lifts with compatible controllers. About half of society lifts are on third-party, society-staff or no AMC, and the state's evidence is paper certificates.
- 0:50–1:50 — Live on the model lift: a normal trip shows floor, jerk and levelling in mm. A judge presses "inject": the door opens mid-trip and a red alarm shows its latency. The latch drops and FREE-FALL fires. A technician taps an NFC card and a signed visit record appears. One record is edited on the SD card and the verifier turns red at that record.
- 1:50–2:30 — Numbers: Table U4-B headline (recall, false alarms per 100 trips, latency) and Plan A (trip-count error, floor accuracy, hours logged).
- 2:30–3:00 — Business: ₹12–15k one-time + ₹300/month per lift. Buyers are AOAs (made responsible by the UP Act 2024) and third-party AMC firms. SAM ₹184 cr. The ask.

**One-page thesis outline**
1. **Problem:** 46% stuck in the last year (LocalCircles, 31 Jul 2026). Pune inspected 9.3% of its 61,521 lifts in Jul–Nov 2025 (FPJ, 9 Dec 2025).
2. **Why now:** the UP Lift and Escalator Act 2024 registers societies and AMC agencies and requires annual maintenance certificates (12,600 registrations covering ~16,000 lifts by Feb 2026). Maharashtra's 2017 Act still has no notified rules (Bombay HC PIL, 2025). The Supreme Court (29 Jul 2026) upheld a ~₹3 cr award with 70% liability on Otis, so maintainer liability now carries a price.
3. **Deep-tech core:** a read-only, multi-sensor trip signature (IMU jerk and free-fall, barometric height and velocity, ToF levelling, door state); hard rules for lethal states such as "moving with door open"; an unsupervised per-lift anomaly score; a hardware-signed, hash-chained maintenance and trip log.
4. **What was built:** two boxes, a model shaft with fault injection, a dashboard, a verifier.
5. **Measured result:** headline lines from Tables U4-B and U4-A.
6. **Business:** buyers are RWAs/AOAs, third-party AMC firms and insurers. Price ₹12–15k + ₹300/month. SAM ₹184 cr + ₹37 cr/yr (R2-03). The AMC pool is ₹2,400–4,800 cr/yr.
7. **What ₹2 lakh over 3 months would prove** (budget is my assumption): 10 boxes with 4G in 10 Noida/Ghaziabad society lifts (~₹60k incl. data), one third-party AMC partner, a legal opinion on whether a sensor counts as an "alteration" under the UP Act (~₹30k), field costs (~₹40k), reserve (~₹70k). Targets: 3 months of trips per lift; ≥1 real anomaly class caught before a service call (door or levelling drift); 2 AOA letters of intent.
8. **Singapore angle** (background, not verified this round): Singapore regulates lift maintenance tightly and its town councils use remote lift monitoring. The immersion is a chance to benchmark against a market where retrofit monitoring already exists.

### 5. Judge-proofing

1. **"Otis ONE, KONE 24/7 and TKE MAX already monitor lifts."**
   - These systems cover the OEM's own maintained, compatible lifts. Otis India says Otis ONE is "not compatible with all elevator controllers", and KONE says maintenance "is best done by the manufacturer" (R2-03).
   - LocalCircles (Jul 2026): only 49% of AMCs are with the manufacturer; 30% are third-party, 11% society staff, and 10% call a technician when the lift breaks.
   - Our box never touches the controller, so it works on any brand. It is built for that other half.
2. **"KALA (PAPL + Ardelisys) launched an any-brand IoT retrofit in 2024."**
   - True. Its price and install count are unknown (R2 could not open the page). Do not claim to be first.
   - Our wedge is evidence rather than dashboards: a tamper-evident, signed log of trips and technician visits that RWAs, inspectors and insurers can rely on, plus the "moving with door open" rule.
   - If KALA owns the hardware channel, the log and analytics layer can be licensed to it.
3. **"Your model is a stepper on a string. A 10 cm drop onto foam is not a lift failure."**
   - Agreed. The model validates detection logic and latency only. The real-lift numbers are trip counts, floors and ride quality from Plan A.
   - Failure prediction needs months of fleet data, which is what the ₹2 lakh pilot buys. We do not claim prediction tonight.
4. **Bonus: "Does fitting a sensor count as an alteration under state Lift Acts, and will AMCs void their contracts?"**
   - Unknown (R2: NOT FOUND). The device is self-powered and adhesive-mounted, with no electrical connection to the lift. A legal opinion is step 1 of the pilot.

### 6. Pre-event checklist
- **By 5–7 Nov:** order items 1–13 (BMP390, VL53L1X and ATECC608 first), asking for delivery by 11 Nov. DOA-test each part on arrival.
- **By 10 Nov:** written permission from Ashoka facilities/estates AND the lift's AMC agency for a read-only, adhesive-mounted, battery-powered logger inside one car, from 20:00 on 13 Nov to 09:30 on 14 Nov. Name the lift, the escort and a contact, and keep a signed copy.
- Confirm the SPARK Night rules. If pre-printing parts is allowed, print the car and frame brackets beforehand.
- Record 20–30 phyphox traces (pressure plus accelerometer, exported) in two campus lifts.
- Set up a shared GitHub repo, a local Mosquitto MQTT broker on one laptop, and a Python environment (numpy, pandas, scikit-learn, cryptography). Pin the Arduino libraries (BMP3XX, VL53L1X, PN532, ArduinoECCX08).
- B prepares the randomised dev and test fault schedules in sealed envelopes and prints the result sheets.
- Take the thesis numbers from R2-03 U4, corrected by R3-claims-01.

### 7. Feasibility verdict
**Buildability: 4/5.**
- All parts are hobby-grade and listed by Indian sellers, with possible stock-outs for the BMP390 and VL53L1X.
- The firmware, rules and log are standard work.
- The real effort is mechanical: the 3D-printed car, winch and free-fall latch can take 4–5 h.
- Plan A depends on permission obtained before the event.

**Type: high-ceiling.** It has the strongest market and a buyer named in law, but more moving parts than the others.

**Biggest risk on the night:** the model shaft not running reliably by ~02:00, which starves the 100 + 40 trial dataset.

---

## U1 Street-dog re-ID (phone photos → individual ID → sterilisation coverage → bite map)

The rabies-diagnostic stretch is dropped, as R2 recommended.

### 1. Bill of materials

There is no specialist hardware, and nothing needs pre-ordering. Models and data:

| Item | Source | ₹ | Risk |
|---|---|---|---|
| DINOv2 ViT-B/14 backbone. "Code and model weights are released under the Apache License 2.0"; loads via `torch.hub.load('facebookresearch/dinov2','dinov2_vitb14')` | https://github.com/facebookresearch/dinov2 (read 3 Nov 2026) | 0 | — |
| MegaDescriptor-L-384: Swin-L, "pre-trained on animal re-identification datasets", 384×384 input, **CC BY-NC 4.0** (fine for the demo, not for a product) | https://huggingface.co/BVRA/MegaDescriptor-L-384 (read 3 Nov 2026) | 0 | licence blocks commercial use |
| PetFace data + pretrained ArcFace. 257,484 individuals across 13 families. Obtained via a Google Form; "for non-commercial research purpose only"; the README only shows cat weights, so dog weights are unconfirmed | https://dahlian00.github.io/PetFacePage/ ; https://github.com/mapooon/PetFace (read 3 Nov 2026) | 0 | **[R]** approval time |
| GPU: a team laptop GPU, or Kaggle/Colab free tiers (quotas: background, not verified) | — | 0 | quota or Wi-Fi |
| Dog detector: COCO "dog" class (torchvision Faster R-CNN, BSD licence; Ultralytics YOLO is AGPL-3.0, background, not verified) | — | 0 | — |

**Bring:** 3 phones with GPS on (ideally one with a 2–3× telephoto lens); 3 power banks; 2 head torches; 2 reflective vests; a printed A4 grey card (white balance); clipboards and record sheets. Consumables ≈ ₹500 (assumption).
**BOM total ≈ ₹500.** Nothing is needed from the kit.

Honest note: the hardware members have no real build task here. H leads the fieldwork (fixed routes, GPS, consistent side-on and face shots); B leads the field protocol and ear-notch ground truth.

### 2. Hour-by-hour plan

Constraint: the event opens after sunset (17:27), so the evening session is in the dark. The **gallery is built in daylight before the event**, the night session is a stress test, and the 06:45 morning session is the main cross-day test.

| Time | M (vision) | E (pipeline) | W (app + stats) | H (field lead) | B (field protocol + ground truth) |
|---|---|---|---|---|---|
| 18:00–18:30 | All: load the pre-event dataset; safety brief; fix the night route | | | | |
| 18:30–20:30 | Zero-shot baselines (DINOv2, MegaDescriptor) on the pre-event day-1 → day-2 split. First honest number by 20:30 | Detector → body and head crops; blur human faces; deduplicate | App skeleton: upload → top-5 matches with photos, distance, "last seen"; map | 19:00–21:00 night session N on a fixed lit route: every dog seen, 5–10 shots (side + face, flash and no-flash), GPS and time logged | With H on session N; on-the-spot notes (ear notch, sex, collar, marks) |
| 20:30–01:00 | Fine-tune an ArcFace head on the train-ID dogs (60% of IDs) with night-style augmentation; checkpoint by 00:30 | Eval scripts (bootstrap by dog), config hashing | Chapman mark-resight + Wilson CIs; bite-map page (Pune city series; ward level is mock) | Annotate the night queries against the gallery, independently of B | Annotate independently; compute Cohen's κ; resolve disputes |
| **02:00 milestone** | The app matches a night photo to the gallery (top-5, score, GPS re-rank). First night-set top-1/top-5, zero-shot vs fine-tuned | | | | |
| 02:00–06:00 | Open-set threshold on held-out IDs; ear-notch linear probe on DINOv2 features; freeze at 06:00 and write the config hash into the run log | Paired sleep shifts of 2 h | | | |
| 06:45–08:30 | — | — | Joins the field | Morning session S2 on the **same fixed route as pre-event session S1** (for mark-resight); photograph all dogs | With H |
| 08:30–09:30 | Run the frozen model on the morning set | — | — | Double annotation | Double annotation |
| 09:30–10:30 | Results tables | | Mark-resight: human-matched vs model-matched; coverage % ± CI | | Ear-notch table |
| 10:30–12:00 | Thesis, slides, rehearsal | | | | |

**Fallbacks**
- No GPU: zero-shot embeddings + kNN on CPU, with no training.
- Night photos unusable: report the night as the failure mode and make the morning set the headline.
- Too few dogs at the event: the headline becomes the pre-event day-1 vs day-2 cross-day test (already labelled), with the event sessions as extra.
- App breaks: demo from a notebook.

### 3. Test protocol

**Data design**
- **Gallery G (pre-event):** at least 2 daylight days (for example 9 and 11 Nov). All findable campus and campus-edge dogs, target 40–60, with ≥8 images per dog per day (side + face). Two annotators assign the ground-truth IDs, using marks, collar, ear notch and location.
- **ID split:** 60% of dogs are train IDs, used for fine-tuning only. The other 40% are held-out IDs that are never trained on; they stand in for a new ward.
- **Queries:** Q_N (night of 13 Nov) and Q_M (morning of 14 Nov). Every query is double-annotated, and disputed images are excluded with the count reported.

**Metrics** (always report n dogs and n images)
- Closed-set top-1 and top-5, per image and per dog (majority vote). Split train IDs vs held-out IDs, with vs without the GPS prior, night vs morning, zero-shot vs fine-tuned.
- Open-set: AUROC for known vs new dog, and precision at 90% recall of "known".
- Ear-notch classifier: accuracy, sensitivity and specificity on held-out dogs (tiny n, so show the confusion matrix).
- Cohen's κ between annotators. Ground truth is itself uncertain for look-alike tan dogs, so report it.
- 95% CIs by bootstrap over dogs (1,000 resamples). With 30 dogs, a 50% top-1 carries roughly ±18 points (normal approximation, my arithmetic). Say so on the slide.

**Mark-resight (campus)**
- Session S1 is a pre-event fixed-route walk (for example 12 Nov, 06:45–08:30). Session S2 is 14 Nov, same route and window.
- Chapman estimator: N̂ = (n1+1)(n2+1)/(m2+1) − 1, with a 95% CI. Compare N̂ with a roster of known campus dogs (from campus animal-care volunteers or security, if one exists).
- Compute it twice, with m2 matched by humans and by the model, to show how ID errors propagate into the population and coverage estimates.
- Sterilisation coverage = ear-notched / identified dogs, with a Wilson 95% CI.
- Assumptions to state on the slide: a closed population, and equal sighting probability (violated by shy dogs).

**Results templates**

Table U1-a (re-ID)
| Query set | IDs | n dogs | n images | Model | GPS prior | Top-1 (95% CI) | Top-5 | Open-set AUROC |
|---|---|---|---|---|---|---|---|---|
| Morning | held-out | | | fine-tuned | on/off | | | |
| Morning | train | | | fine-tuned | on/off | | | |
| Night | held-out / train | | | zero-shot / fine-tuned | on/off | | | |
| Pre-event D1→D2 | all | | | zero-shot | off | | | |

Table U1-b (population and coverage)
| Matching | n1 | n2 | m2 | N̂ (95% CI) | Roster count | Notched % (95% CI) |
|---|---|---|---|---|---|---|
| Human | | | | | | |
| Model | | | | | | |

Table U1-c (ear notch): n dogs | TP | FP | TN | FN | accuracy.

**Expectation.** PetFace's ArcFace gets top-1 **77.86%** on seen dogs from cooperative face photos (arXiv 2407.13555, via R2-01). That is a ceiling, not a target. Report whatever comes out.

**Safety**
- Fieldwork in pairs. Never touch, feed, chase or corner a dog. Avoid packs, mothers with pups and dogs that are eating.
- The night session stays on lit paths, with torches and vests, and campus security is told in advance.
- Any bite or scratch: wash for 15 min, then go straight to the campus health centre for PEP.
- No samples of any kind.
- Privacy: blur human faces before storage and never photograph into homes.

### 4. Demo script and Deep Tech Thesis

**3-minute demo**
- 0:00–0:25 — "37 lakh dog-bite cases in 2024. ICMR estimates 5,726 rabies deaths a year, against 54 reported. Cities pay ₹700–1,650 per sterilisation and cannot prove which dog was done."
- 0:25–0:55 — The Supreme Court orders of Aug–Nov 2025 demand compliance affidavits. Today's tools: chips that need a capture, collars that get lost, and self-reported app censuses (Ahmedabad claims 89%).
- 0:55–1:50 — Live: a judge picks a photo from this morning's set (or of a dog nearby). The app returns "#17, score 0.83, notched, last seen 14 h ago at X" with the gallery photo. A held-out dog is flagged "unknown". Toggle the GPS prior on and off.
- 1:50–2:30 — Results: top-1/top-5 for day vs night and for held-out IDs; campus N̂ ± CI against the roster; coverage % ± CI. Show how ID error widens the CI.
- 2:30–3:00 — Business and ask.

**One-page thesis outline**
1. **Problem:** 37,17,336 dog-bite cases in 2024 (Lok Sabha via IANS, 22 Jul 2025). ICMR/Lancet: 5,726 rabies deaths a year against 54 reported (~106×).
2. **Why now:** Supreme Court orders (11 Aug, 22 Aug and 7 Nov 2025) with state compliance affidavits; MCD's ₹20 cr microchipping budget; BMC's ₹23 cr over 3 years; Pune's ₹25 lakh census tender (Jul 2026).
3. **Deep-tech core:** metric-learning re-ID of free-ranging dogs from ordinary phone photos; a territory (GPS) prior that shrinks the gallery; open-set rejection; capture-recapture statistics that turn IDs into coverage with confidence intervals.
4. **What was built:** capture protocol, matcher app, coverage calculator, bite map.
5. **Measured result:** headline lines from Tables U1-a and U1-b.
6. **Business:** municipal veterinary departments already tender surveys at ₹19–30 lakh (Panvel, Pune, Ahmedabad). Price ₹15–20 lakh/yr per city. SAM ≈ ₹20 cr/yr (R2-01). The first paid feature is auditing ABC claims for duplicates.
7. **What ₹2 lakh over 3 months would prove:** two wards in Sonipat or Gurugram with an AWBI-recognised ABC NGO; monthly survey passes; ≥200 dogs; cross-month top-1; a duplicate-claim audit of one month of ABC claims; release of the first Indian free-ranging-dog re-ID benchmark.
8. **Singapore angle** (background, not verified): Singapore manages free-roaming dogs through a trap-neuter-release-manage programme. It faces the same verification problem at a smaller scale, and NUS/A*STAR vision groups are possible partners.

### 5. Judge-proofing

1. **"PetFace already does re-ID, and Petnow claims 98.97% with nose prints."**
   - Both work on cooperative pet photos (a close face or nose shot). PetFace's own ArcFace top-1 is 77.86% on seen dogs.
   - Street dogs do not pose.
   - No study of re-ID on Indian free-ranging dogs was found. R2 found none, and this round's search turned up only Flickr pet-dog datasets and a western-India mugger-crocodile UAV study (88.8% TPR; https://zenodo.org/record/6758870, snippet).
   - Our number is cross-day, in street conditions, with CIs.
2. **"Indian pariah dogs look alike, so this collapses at city scale."**
   - Partly true. That is why matching is limited per ward by the territory prior, there is an open-set "unknown" output, and low-confidence matches go to human review.
   - Coverage estimates only need correct re-sightings. We show how much ID error widens the CI, and we report held-out-ID accuracy for generalisation.
3. **"Microchips (MCD ₹20 cr) and BMC's AI pilot already exist."**
   - A chip proves identity only after a capture and a scan; it cannot audit a street from 5 m away.
   - The BMC pilot (an unnamed startup, sensors fitted after sterilisation) has no public results (R2).
   - We are an audit layer that sits on top of any ABC programme.
4. **Bonus: "This is polarised, and the courts keep changing their orders."**
   - It works under both the release and the shelter regimes. Neutral evidence is the one thing both sides can accept.

### 6. Pre-event checklist
- **5–7 Nov — 1-hour pilot (R2 unknown 1):** 15 dogs over two sessions, scored zero-shot with DINOv2 top-1. This is the go/no-go on the night session.
- **8–12 Nov:** collect the gallery on ≥2 daylight days, and walk session S1 on the fixed route. Tell campus security/admin. Ask any campus animal-care group for a roster, names and sterilisation status.
- Submit the PetFace Google Form now (research only; approval may never come).
- Cache DINOv2 and MegaDescriptor weights locally in case there is no internet.
- Check GPU accounts and laptop CUDA.
- Annotation tool: Label Studio or a spreadsheet.
- Bite data: the Pune city series (navbharatlive, 29 Jul 2026) and any Sonipat data. Otherwise label the bite map as mock.
- Confirm the event rules allow pre-collected data.

### 7. Feasibility verdict
**Buildability: 4/5.** There is no hardware to fail and the pipeline is standard. The risk is in the data: how many dogs, and photo quality after dark.

**Type: safe.** A working matcher and an honest number are near-certain. The story risk is a low top-1, which is still a publishable first measurement.

**Biggest risk on the night:** too few usable photos in the dark (the build opens after the 17:27 sunset), so the pre-event daylight gallery and the 06:45 morning session have to carry the result.

---

## A1 Indoor/outdoor PM pair: purifier-efficacy verdict

### 1. Bill of materials

**Bring / pre-order**

| # | Item | Qty | Source (listing) | Unit ₹ | Line ₹ | Risk |
|---|---|---|---|---|---|---|
| 1 | Plantower PMS5003 laser PM sensor (same model in both nodes, plus 1 spare) | 3 | robu https://robu.in/product/plantower-pm5003-gas-sensor-uart/ (₹2,299, shown in stock on an index ~229 days old; snippet) | 2,299 | 6,897 | **[R] high.** Hubtronics ₹1,499 + GST, 0 in stock (https://hubtronics.in/pms5003-pm2.5-sensor, read 3 Nov 2026). Robocraze ₹1,930, sold out (snippet). Amazon.in listings ₹3,999–5,619 (snippet; e.g. https://www.amazon.in/PMS5003-Precision-Quality-Particle-Concentration/dp/B0F9W3ZD9C) |
| 1-alt | Plantower PMS7003 (only if no PMS5003; both nodes must be the same model) | 3 | robu https://robu.in/product/plantower-pms7003-gas-sensor-uart/ ₹1,881 (snippet). zbotic ~₹1,415 incl. GST (category page, snippet). electronicscomp ₹2,149 ex-GST, out of stock (https://www.electronicscomp.com/pms7003-sensor-module-pm2.5-air-particle-dust-sensor) | 1,881 | (5,643) | **[R]** |
| 2 | GY-SHT31-D RH/temperature sensor | 3 | https://www.electronicscomp.com/unwelded-gy-sht31-d-digital-temperature-and-humidity-sensor | 263 | 789 | — |
| 3 | Micro SD card module (backup logs) | 2 | https://www.electronicscomp.com/micro-sd-card-module-india | 36 | 72 | — |
| 4 | Painter's tape, cardboard, zip bags, incense (only if permitted) | — | local (assumption) | — | 250 | — |
| 5 (optional) | Mi-compatible HEPA filter: a "new" filter if the borrowed purifier is a Mi, or for a fan + filter DIY unit | 1 | Amazon.in ₹1,799 (HEPA + carbon) / ₹2,469 (HEPA only) (snippet; https://www.amazon.in/Compatible-Purifier-Activated-Replacement-Allergens/dp/B0G4DKHDSJ) | 1,799 | 1,799 | optional |
| | **Core total (1–4)** | | | | **8,008** | |

- With the optional filter the total is ₹9,807. GST on the electronicscomp lines adds ~₹155 (my arithmetic).
- Using PMS7003 instead of PMS5003 brings the core total to ≈ ₹6,750.
- Other alternative: Nova SDS011 at ₹1,859 ex-GST, out of stock at electronicscomp (https://www.electronicscomp.com/nova-pm-sensor-sds011-high-precision-laser-pm2.5-air-quality-detection-sensor).

**Expect in the kit:** 2 ESP32 boards, USB cables, breadboards, jumpers.
**Borrow:** 1 purifier with its rated CADR on the label (ideally with an old filter fitted and a new one available); 1 table fan for mixing; a laser distance meter or tape; a flask of hot water.
**Bring:** 2 power banks; an extension cord.

Sensor note: log both Plantower output fields (CF=1 and ATM) and fix the headline field before the first run. NIOSH found that one manufacturer's correction factor changed CADR accuracy across four of the low-cost systems it tested (Barnes et al., *Aerosol Sci. Technol.* 60(8), 2026, https://stacks.cdc.gov/view/cdc/259938).

### 2. Hour-by-hour plan

Chamber: the quiet room. Measure L×W×H and note the leaks. The outdoor node sits at a window or balcony under a rain/dew cover.

| Time | E (firmware) | M (analysis) | W (dashboard + CPCB) | H (nodes + chamber) | B (test officer) |
|---|---|---|---|---|---|
| 18:00–18:30 | All: get the room and purifier; measure volume; locate the smoke detectors; ask the organisers about incense | | | | |
| 18:30–20:00 | PMS frames at 1 Hz (both fields), SHT31, NTP time, MQTT to a laptop, SD backup | Decay-fit code (log-linear with background term; residual bootstrap); κ-Köhler function | Dashboard (live I/O ratio, live decay plot, verdict card); CPCB Murthal fetch script | Build 2 nodes (ESP32 + PMS5003 + SHT31) in vented boxes | Run sheets; purifier label CADR and model; filter age |
| 20:00–21:00 | **Co-location 1:** both nodes side by side indoors, 60 min | | | | |
| 21:00 | The outdoor node goes outside and stays until 09:00 (~12 hourly points against CPCB) | | | | |
| 21:00–22:00 | **Natural decay N1:** load the room with outdoor air (window open 15 min; mid-Nov outdoor PM is usually high, check it live), or with incense if permitted. Close up; mixing fan on; purifier OFF; log 45 min | | | | |
| 22:00–00:30 | **Clean runs C1–C3:** reload 10–15 min, purifier ON at a fixed speed, then 30 min decay each | | | | |
| 00:30–01:30 | **Natural decay N2** | | | | |
| **02:00 milestone** | The dashboard shows clean-filter effective CADR (m³/h ± SE) and its % of rated, with a live I/O ratio | | | | |
| 01:30–04:00 | **Degraded runs D1–D3:** 50% of the filter face taped over, or an old filter from a hostel purifier; same speed | | | | |
| 04:00–05:00 | **Natural decay N3** (checks k_off stability). Paired sleep shifts. | | | | |
| 05:00–06:00 | **Humidity artefact:** one node in a closed box over hot water (RH ~50 → 95%), the other node outside the box as control; apply the correction | | | | |
| 06:00–09:00 | Indoor/outdoor ratio in purifier on/off hourly blocks; pull CPCB data (if it has updated) | | | | |
| 09:00–09:45 | **Co-location 2** (drift check) | | | | |
| 09:45–10:45 | Analysis and results tables | | | | |
| 10:45–12:00 | Thesis, slides, rehearsal | | | | |

**Fallbacks**
- One PM sensor dead: the single-node decay test still works, because a decay rate does not depend on sensor gain. Drop the I/O ratio and co-location.
- No purifier: build a table fan + HEPA filter unit (₹1,799). The result is then clean vs degraded only, not "% of rated".
- Outdoor PM too low to load the room: use incense outside the room with permission, or report low-C0 runs.
- CPCB data delayed: report that comparison as pending and lead with co-location.

### 3. Test protocol

**Definitions**
- k: OLS fit of ln(C(t) − C_bg) on t. The window runs from full mixing (t0 + 2 min) until C < 3·C_bg or 30 min have passed. C_bg is the infiltration floor, taken from the run tail.
- k_off: mean of N1–N3.
- **Effective CADR = V · (k_on − k_off)**, in m³/h.
- % of rated = effective CADR / CADR on the label.
- AHAM's rated CADR is measured differently, in a standard 28.5 m³ (1,008 ft³) room with the cleaner both running and not running (https://en.wikipedia.org/wiki/Clean_air_delivery_rate). Ours is an in-room effective value and must be called that.

**Trials:** co-location 2 × 60 min; natural decay 3; clean filter 3; degraded filter 3; humidity 1 (two RH steps); CPCB hourly ~10–12.

**Humidity correction.** Use the κ-Köhler hygroscopic-growth correction from Crilley et al. 2018 (https://amt.copernicus.org/articles/11/709/2018/):
- Their low-cost OPC read 250–400% high above ~85% RH. After correction it was within 33% of a TEOM-FDMS.
- Their fitted κ was 0.38–0.51.
- Caveat to state: kettle or hot-water steam makes liquid droplets, which is a different artefact from hygroscopic growth. The demo shows the artefact and the limit of the correction.

**Context for the method.**
- A Corsi-Rosenthal box study found a PMS5003 gave CADR from decay similar to an aerodynamic particle sizer (snippet via the CDC search result).
- NIOSH tested 7 low-cost systems on DIY cleaners: CADR MAPE ranged from 1.6% to 44.2%, and 3 of the 7 were at or below 10% (Barnes et al. 2026).
- Toronto's in-situ tests found one low-cost sensor type matched the reference and another under-read at high PM (https://hab.civmin.utoronto.ca/projects/in-situ-testing-of-portable-air-cleaners/).
- So the method is published. Our contribution is the product: a paired, falsifiable verdict.

**Results templates**

Table A1-a (co-location)
| Session | n min | Slope | Intercept (µg/m³) | R² | Mean bias (µg/m³) |
|---|---|---|---|---|---|
| Start 20:00 | | | | | |
| End 09:00 (drift) | | | | | |

Table A1-b (decay runs)
| Run | Condition | C0 (µg/m³) | k (h⁻¹) ± SE | R² | Eff. CADR (m³/h) | % of rated |
|---|---|---|---|---|---|---|
| N1–N3 | natural | | | | — | — |
| C1–C3 | clean | | | | | |
| D1–D3 | degraded | | | | | |
| **Summary** | clean mean ± SD / degraded mean ± SD / separation = (mean_C − mean_D)/pooled SD / Welch t (n = 3 vs 3: low power, say so) / run-to-run CV | | | | | |

Table A1-c (humidity): RH step | raw PM | corrected PM | control-node PM.

Table A1-d (vs CPCB, indicative only): n hours | slope | intercept | R² | MAE.
- Station: "Murthal, Sonipat – HSPCB", the one CAAQMS listed for Sonipat in a Lok Sabha annex dated 19 Nov 2024 (https://eparlib.sansad.in/bitstream/123456789/3002603/1/AU213_POuJGE.pdf, snippet).
- Distance from campus: not measured; check on a map.

**Headline sentence:** "Clean filter X m³/h (Y% of rated) vs degraded Z m³/h; separation S pooled SD; run-to-run CV Q%."

**Safety**
- No real gas.
- Incense only with the organisers' permission: in a metal tray, never unattended. Never cover or disable a smoke detector; ask facilities instead.
- B handles the hot water, in a flask.
- The purifier and fan are ordinary appliances on the hall's sockets, with no opened mains. The ESP32s run on USB.

### 4. Demo script and Deep Tech Thesis

**3-minute demo**
- 0:00–0:25 — "A Delhi AQI explainer has 6.8 M views; 44,000 people answered LocalCircles on bad air. Nobody trusts the number, and your purifier's 'filter remaining' is a timer: Dyson's is based on hours of use."
- 0:25–0:50 — The question no product answers: is my purifier delivering in my room, and is the filter spent?
- 0:50–1:50 — Live: two nodes on the table and the I/O dashboard. Overlay the recorded clean vs taped-filter decay curves, and show the verdict card ("Effective CADR … m³/h = …% of rated → replace filter") with the night's numbers. Micro-demo: hold the hot-water box over one node to show the RH artefact, then toggle the correction.
- 1:50–2:30 — Numbers: co-location agreement, clean vs degraded separation, CPCB (indicative).
- 2:30–3:00 — Business: ₹3,999–4,999 for the pair + ₹49/month. Delhi-NCR purifier owners first. SAM ₹36 cr. The moat is an effective-CADR dataset by model × filter age. The ask.

**One-page thesis outline**
1. **Problem:** LocalCircles 44,000+ responses (26 Oct 2025). Delhi has 38 CAAQMS: 22 of the 25 checked break siting rules, and only 34.5% of the city is within 2 km of one (IndiaSpend/Newslaundry, 1 Dec 2025).
2. **Why now:**
   - Peak season; Dhruv Rathee's explainer at 6.84 M views.
   - 0.6–1.2 M purifiers sold a year, with filter alerts that are timers.
   - No CSIR-NPL/BIS certification route exists for low-cost sensors, so position the node as an efficacy instrument, not a regulatory AQI monitor.
3. **Deep-tech core:**
   - Decay and indoor/outdoor ratios cancel each sensor's gain error, so a ₹2k sensor gives an absolute, checkable verdict.
   - κ-Köhler humidity correction.
   - Drift correction against the nearest CAAQMS.
   - A crowdsourced effective-CADR dataset.
4. **What was built:** two nodes, a test-mode protocol, a fitter and a dashboard.
5. **Measured result:** Tables A1-a and A1-b headlines.
6. **Business:** consumers first, RWAs and schools second, purifier brands as channel or certification buyers. SAM ₹36 cr + ₹7 cr/yr. The filter-replacement pool it steers is ₹216–432 cr/yr (R2-03).
7. **What ₹2 lakh over 3 months would prove:** 40 node pairs in 40 Delhi-NCR homes through the winter, giving effective CADR vs filter age for 5 popular models; a willingness-to-pay landing page at ₹3,999 with pre-orders; one purifier-review YouTuber partnership.
8. **Singapore angle** (background, not verified): Southeast Asian transboundary haze drives purifier buying in Singapore and its neighbours. The same verdict under tropical humidity is where the RH correction earns its keep.

### 5. Judge-proofing

1. **"Airveda already does this."**
   - Airveda sells individually calibrated single-point monitors. Its catalogue says "measure performance changes in your air purifier", as charts the user has to read (R2-03).
   - We give a falsifiable number from a protocol: effective CADR in m³/h, % of rated, a filter verdict, and an indoor/outdoor protection factor.
   - If Airveda adds this, the moat is the per-model × filter-age dataset.
   - Not checked: whether Airveda or Qubo already compute an efficacy number in-app.
2. **"₹2k sensors are useless in a Delhi winter."**
   - For absolute, regulatory-grade AQI, partly true, and we do not claim it.
   - A decay rate is a ratio, so gain error cancels.
   - Published DIY-cleaner work found some low-cost systems within 10% CADR error and others up to 44% (Barnes et al. 2026). We show our own co-location and run-to-run CV, and we correct for RH.
3. **"Your room is leaky and badly mixed. That is not an AHAM chamber."**
   - That is the point: AHAM measures in a 28.5 m³ chamber, and homes are not chambers.
   - Natural-decay runs subtract leakage and deposition, and a fan mixes the room.
   - We call the result "effective CADR in this room" and never present it as an AHAM rating.
4. **Bonus: "Will anyone pay ₹4k on top of a purifier?"**
   - Unknown. The landing page and pre-orders in the ₹2 lakh plan test exactly this.

### 6. Pre-event checklist
- **By 5 Nov:** order 3 PM sensors, split across two sellers (stock-outs seen at Hubtronics, Robocraze and electronicscomp), all the same model. On arrival, DOA-test them and co-locate for 30 min at home.
- Borrow a purifier with its CADR on the label, ideally with an old filter. Record the model and filter age.
- Book the quiet room (with an openable window). Get the organisers' written answer on incense and on the smoke detectors in that room. Measure the room beforehand.
- CPCB:
  - confirm the Murthal, Sonipat – HSPCB station on the CCR portal (15-min data, app.cpcbccr.com / airquality.cpcb.gov.in);
  - test the unofficial `cpcbccr` Python client (https://github.com/sakethramanujam/cpcbccr-python-client);
  - clean the data for zeros, negatives and 999s; a 2020 note said 15-min requests were capped at one week each (https://urbanemissions.info/?p=2408);
  - pre-download the last 2 weeks.
- Python: numpy, scipy, pandas. Pick a PMS library that exposes both CF=1 and ATM fields.
- Read Crilley 2018 and Barnes 2026 for the method line in the thesis.

### 7. Feasibility verdict
**Buildability: 5/5.** Two sensors and one curve fit, with no mechanics. Each run takes ~45 min, so all 9 decay runs fit comfortably overnight.

**Type: safe.**

**Biggest risk on the night:** a leaky, badly mixed room makes run-to-run noise as large as the clean-vs-degraded gap (n = 3 each), so the headline separation is not significant. The pre-event risk is PM-sensor stock.

---

## E1 Smart-meter witness meter

**Mains rule (from the brief): no live mains work in the hall.** Use only two things:
- **(a) A sealed, pre-wired "witness box."** It is assembled and tested by a qualified electrician before the event and never opened at the event. It plugs in series with a commercial plug-in reference meter and commercial appliances, on an RCCB-protected circuit, and only after the organisers approve it in writing.
- **(b) A 12 V low-voltage rig** for leakage and everything else.

### 1. Bill of materials

**Bring / pre-order**

| # | Item | Qty | Source (listing) | Unit ₹ | Line ₹ | Risk |
|---|---|---|---|---|---|---|
| 1 | PZEM-004T with split CT and case: 100 A, 80–260 V, Modbus-RTU over TTL. The manual gives 0.5% accuracy for V, I and P, and energy resolution is 1 Wh. The supplied CT is class 1.5 (manual mirror https://manualmachine.com/innovatorsguru/accommunicationmodulepzem004tv30/17924474-user-manual; https://espeasy.readthedocs.io/en/latest/Plugin/P102.html; how2electronics; all snippets) | 2 (1 spare) | https://www.electronicscomp.com/pzem-004t-with-split-ct-with-outcase-ac-meter ("Availability: 5", ex-GST, read 3 Nov 2026) | 862.80 | 1,725.60 | The listing does not say "v3.0 (Modbus)", so confirm with the seller. Alternative: "xcluma PZEM-004T v3.0 with case" on Amazon.in (https://www.amazon.in/xcluma-PZEM-004T-80-260V-voltage-communication/dp/B0823P417C; price not captured) |
| 2 | Witness-box enclosure set: surface electrical box, socket, 3-pin plug top, 1.5 mm² 3-core cable, glands. Electrician assembles it before the event | 1 | local electrical shop (assumption) | — | 500 | — |
| 3 | Reference plug-in energy meter, Blackt BT72PM (230 V, 3-pin; W/V/A/kWh) | 1 | https://www.amazon.in/Blackt-Electrotech-BT72PM3-Digital-Energy/dp/B0FGWHL8L2 (₹939–999, snippet) | 999 | 999 | accuracy and kWh resolution not stated |
| 4 | Adafruit ATECC608 breakout (ECDSA P-256 signing) | 1 | https://robu.in/product/adafruit-atecc608-breakout-board-stemma-qt-qwiic/ (snippet) | 729 | 729 | **[R]** old listing. Bare chips at robu cost ₹133–170 |
| 5 | ESP32-S3-DevKitC-1-N8. Its fallback signer is the RSA Digital Signature peripheral, whose key is protected by an eFuse HMAC key that software cannot read (https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/ds.html) | 1 | electronicscomp ESP32-S3 search page | 1,101 | 1,101 | — |
| 6 | DS3231 RTC | 1 | https://www.electronicscomp.com/ds3231-real-time-clock-module-3.3v-5v-precise-for-raspberry-pi | 139 | 139 | — |
| 7 | Micro SD card module | 1 | https://www.electronicscomp.com/micro-sd-card-module-india | 36 | 36 | — |
| 8 | ZMCT103C residual-current CT module (5 A : 5 mA) | 2 | https://zbotic.in/product/zmct103c-ac-current-sensor-module/ (₹109.74 incl. GST, snippet). Amazon DEPOKE ₹119 (https://www.amazon.in/ZMCT103C-10-Ampere-Current-Transformer/dp/B08XK3W745, snippet) | 110 | 220 | — |
| 9 | SCT-013-005 split-core CT, 5 A (current channel on the LV rig) | 1 | https://www.electronicscomp.com/sct-013-005-non-invasive-split-core-current-transformer-ac-current-sensor-5a | 387 | 387 | — |
| 10 | Power resistors (10 Ω 10 W ×4; 100, 220, 470 Ω and 1 kΩ at 2 W for the leak path); 12 V bulbs | — | local (assumption) | — | 150 | — |
| | **Total** | | | | **≈ 5,987** | |

The electronicscomp lines (₹3,389) are ex-GST, so add ~₹610. **Delivered ≈ ₹6,600** (my arithmetic).

**Expect in the kit:** a spare ESP32, an L298N H-bridge, a 12 V 2 A adapter, a multimeter (true-RMS if possible), breadboards, jumpers.
**Borrow:** an electric kettle (~1.5 kW), a clothes iron, a table fan, a plug-in LED lamp, a laptop charger.
**Bring:** a USB power bank (so the ESP32 survives the outage test), and an RCCB-protected extension if the hall sockets turn out not to be RCCB-protected.

### 2. Hour-by-hour plan

| Time | E (firmware) | W (crypto + dashboard) | M (NILM) | H (rigs) | B (test officer + safety marshal) |
|---|---|---|---|---|---|
| 18:00–18:30 | All: plan; safety briefing; organisers sign off the sealed box and appliance bench (designated table, RCCB, no water near electronics) | | | | |
| 18:30–20:30 | Read the PZEM at 1 Hz over Modbus (mandulaj PZEM-004T-v30 library, https://www.github.com/mandulaj/PZEM-004T-v30); minute aggregation; DS3231; SD; outage logic (Modbus timeout + voltage loss) | Record format; SHA-256 chain; ATECC608 signing (ArduinoECCX08 / cryptoauthlib); Python verifier; dashboard | Load iAWE (pre-converted with NILMTK's `convert_iawe`); resample to 1 min; train CO/FHMM baselines and a seq2point CNN | LV rig: 12 V DC → L298N switched at 50 Hz by the second ESP32 → 10 Ω loads. Pass both conductors through the ZMCT103C (N turns); add a leak resistor path that bypasses the CT; SCT-013-005 on one conductor | Run sheets; kettle/iron supervision |
| 20:30–02:00 | Energy/power test: each of the 5 loads twice (≈ 4.5 h with changeovers; protocol below). B runs it; E logs. | | | 21:00–01:00: leakage threshold sweep on the LV rig (H with W) | Never leaves the kettle or iron unattended |
| **02:00 milestone** | The dashboard shows the witness box's signed minute log with a green verifier, the first kettle/iron energy error %, and a leakage alarm on the LV rig. Editing one SD record turns the verifier red. | | | | |
| 02:00–04:00 | Outage test: 20 off/on cycles of the switch upstream of the box (random 5–60 s off), filmed with a phone stopwatch in frame. Paired sleep shift. | | | | |
| 04:00–05:30 | — | Tamper suite (scripted) + head-anchoring demo (hourly head hash sent to a phone/server) | NILM evaluation on held-out days | — | — |
| 05:30–08:00 | — | "Explain the bill" page: month kWh by appliance class + tariff slab | NILM tables | Tidy the rigs | Sleep shift |
| 08:00–10:00 | Analysis, tables, re-run any failed load | | | | |
| 10:00–12:00 | Thesis, slides, rehearsal | | | | |

**Fallbacks**
- PZEM dead: use the spare.
- **Organisers refuse even the sealed box:** there is no live kWh test in the hall. Show signed logs from the same 5-load test run on 11–12 Nov in a supervised campus lab, clearly labelled "pre-event" (check the rules first). The hash chain is what shows those logs were not edited afterwards. In the hall, run the LV rig, the tamper suite, an outage test simulated by cutting the H-bridge supply, and NILM.
- ATECC608 fails: use the ESP32-S3 DS peripheral, or a software key in flash (labelled weaker).
- NILM training too slow: report the NILMTK CO/FHMM baselines only.

### 3. Test protocol

**1. Energy and power accuracy** (witness vs reference). Chain: wall socket (RCCB) → BT72PM reference → witness box → load.
- **High loads, energy error %:** kettle (2 × 20 min, refilled, never boiled dry), iron (2 × 30 min, thermostat cycling), fan (2 × 30 min). Error = (E_wit − E_ref)/E_ref.
  - Record the reference display's kWh resolution first. Example: a 20-min kettle run is ≈ 0.5 kWh, so a 0.001 kWh display gives 0.2% quantisation and a 0.01 kWh display gives 2% (my arithmetic).
- **Low loads, power error %:** LED lamp and laptop charger (non-linear, low PF). Take 20 paired W readings each, photographing the reference display every 30 s next to the dashboard. Report PF. The kWh display is too coarse for these loads overnight.
- **Kettle cross-check:** true-RMS multimeter V × clamp I, if available. On a resistive load this shows which meter is off.
- Target (R2): ≤2%. Report the reference meter's unstated accuracy as the limit of the test.

**2. Outage detection.** 20 cycles → detection rate; start and end timestamp error (s) against the video; shortest outage detected.

**3. Tamper evidence.** Use a 1,000-record signed log. Run 20 trials of each attack:
- edit one value;
- delete one record;
- swap two records;
- insert a forged record;
- re-sign with a different key;
- truncate the tail.

Report detection %. Truncation is detected only when the chain head is anchored, so show the result both with and without hourly anchoring. That is the honest limit of a hash chain.

**4. Leakage (LV rig, scaled).**
- Inject imbalance currents of 0, 5, 10, 20, 30, 50 and 100 mA through leak resistors; looping the conductors N times through the core multiplies sensitivity. Run 10 trials per level.
- Report the detection probability curve, the level giving 95% detection, and false alarms per hour of balanced running (1 h).
- Scaling note: residual-current physics is the same at 230 V, but a product needs a proper core-balance CT and a lab test. The 30 mA figure is the usual RCCB trip level (background).

**5. NILM on iAWE.**
- Data: one New Delhi home, summer 2013, ~73 days; observed mains 180–260 V (https://iawe.github.io/, read 3 Nov 2026). NILMTK metadata lists a fridge, 2 ACs, a washing machine, a laptop, an iron, a TV, a water filter and kitchen outlets (https://github.com/nilmtk/nilmtk/tree/master/nilmtk/dataset_converters/iawe).
- Method: resample to 1 min to match the device log; split train/test by day (70/30).
- Report per-appliance on/off F1 and MAE (W) for 4–5 appliances, against the CO/FHMM baselines.

**Results templates**

Table E1-a (energy / power)
| Load | Type | Run | Duration | E_ref kWh or P_ref W | E_wit / P_wit | Error % | PF |
|---|---|---|---|---|---|---|---|
| Kettle | resistive | 1, 2 | 20 min | | | | |
| Iron | resistive, cycling | 1, 2 | 30 min | | | | |
| Fan | inductive | 1, 2 | 30 min | | | | |
| LED lamp | non-linear | 20 readings | — | | | | |
| Laptop charger | SMPS | 20 readings | — | | | | |

Table E1-b (outage): cycles | detected | missed | mean \|Δt_start\| (s) | mean \|Δt_end\| (s) | shortest detected.

Table E1-c (tamper): attack | trials | detected | % (with / without head anchoring).

Table E1-d (leakage): imbalance mA | trials | detected | P(detect). Plus false alarms per hour.

Table E1-e (NILM): appliance | F1 ours | F1 FHMM | F1 CO | MAE (W).

**Safety**
- No live mains work in the hall. The sealed box is never opened.
- Only commercial appliances, on an RCCB circuit.
- Kettle and iron sit on a heat-proof tile, are never unattended, and are unplugged after each run.
- The LV rig is ≤12 V from a commercial adapter.
- No loose lithium cells. No liquids on the electronics bench.
- B is safety marshal, with authority to stop any test.
- Lock the ATECC608 config only after all tests; locking is irreversible.

### 4. Demo script and Deep Tech Thesis

**3-minute demo**
- 0:00–0:25 — "7.24 crore smart meters were installed by 30 Jun 2026. Maharashtra logged 3.92 lakh billing complaints on 1.23 crore of them. A home 'smart meter test' video has 28.6 lakh views."
- 0:25–0:50 — What exists today: the discom's check meter (their meter checking their meter), a NABL lab test at ₹450 that is a one-time snapshot, and Wi-Fi plugs with no evidence value.
- 0:50–1:50 — Live:
  - the kettle runs through the reference meter and the witness box, and the dashboard's watts match;
  - the signed minute log scrolls;
  - flip the upstream switch and an outage is logged with timestamps;
  - add a leak resistor on the LV rig and "EARTH LEAKAGE" fires;
  - change one number in the SD file and the verifier turns red at that exact record.
- 1:50–2:30 — Numbers: energy error % per load, outage detection, tamper detection %, leakage threshold, NILM F1. The "bill explainer" page for a sample iAWE month.
- 2:30–3:00 — Business: ₹2,500 device, or ₹500 per quarter rented via RWAs and consumer councils. SAM ₹160 cr. The ask.

**One-page thesis outline**
1. **Problem:** 7.24 crore smart meters installed (MoS Power reply, as of 30 Jun 2026). 3.92 lakh billing complaints on 1.23 crore meters in Maharashtra = 3.2% (UNI, 3 Jul 2026).
2. **Why now:**
   - RDSS has 19.79 crore consumer meters sanctioned, with the scheme ending 31 Mar 2028.
   - UP moved prepaid meters to postpaid.
   - MSEDCL is fitting check meters on 20–25% of new installs (FPJ, 31 Jul 2026).
   - The 2024 Consumer Rules require a check meter within 5 days, for 3 months.
3. **Deep-tech core:**
   - metering IC + hardware-rooted, signed hash chain = tamper-evident, in-situ evidence;
   - residual-current leakage detection;
   - NILM bill explanation trained on Indian-home data.
4. **What was built:** sealed witness box, LV leakage rig, signed log and verifier, NILM explainer.
5. **Measured result:** Tables E1-a to E1-e headlines.
6. **Business:** RWA rental and consumer councils (UPRVUP), possibly discom trust audits. ₹2,500 per device. SAM ₹160 cr one-time (R2-02).
7. **What ₹2 lakh over 3 months would prove:**
   - 30 homes in Noida/Ghaziabad, logging alongside the discom check meters for the statutory 3-month window;
   - NABL calibration of 5 units;
   - a test of reading the IS 16444 meter's optical port (R2 unknown 2);
   - 3 RWA letters of intent.
8. **Singapore angle** (background, not verified): Singapore has rolled out smart meters nationally and runs an open electricity retail market, so consumer trust and bill explanation are exportable features.

### 5. Judge-proofing

1. **"The law already gives a free check meter within 5 days."**
   - Yes (2024 Rules). But it is the discom's meter checking the discom's meter, and consumers distrust it (R2-02).
   - Ours is held by the consumer, covers the same 3-month window, explains the bill, and turns the complaint into a structured pack.
   - It triggers and steers the official test; it does not replace it.
2. **"A PZEM is an ₹860 hobby module with a class-1.5 CT, and SustLabs and Tuya monitors already exist. Why call this a witness?"**
   - Show tonight's measured error (Table E1-a).
   - The hardware is a commodity. The product is calibration (NABL per unit in the pilot), signed tamper-evident logs, leakage detection and the explanation.
   - SustLabs (~US$1.5 M raised) does NILM but has no evidence-grade log or dispute workflow.
3. **"Most smart meters are accurate, and UP's ₹32.74 cr refund was for meter cost, not mis-metering."**
   - Agreed, and we say so first: never claim that the meters are wrong.
   - If the meter is right, the device shows why the bill rose (a new AC, earth leakage, catch-up after a slow old meter). If it is wrong, the log is evidence. The device has value either way.
4. **Bonus: "Is the log admissible?"**
   - It is not a revenue meter under the CEA metering regulations, so at a CGRF it is supporting evidence.
   - Court use would need a Bharatiya Sakshya Adhiniyam s.63 certificate (R2, not verified).

### 6. Pre-event checklist
- **By 7 Nov:** email the organisers: may a sealed, pre-wired, electrician-assembled metering box with commercial appliances run on an RCCB-protected bench? Get a written yes or no. If no, book a supervised campus lab for an 11–12 Nov run, and confirm the rules allow pre-event results.
- Order the PZEM ×2 (confirm v3.0/Modbus with the seller), the ATECC608 and the reference meter.
- The electrician assembles the witness box, tests continuity, insulation and earth, and seals it.
- iAWE: download the SharePoint folder linked from https://iawe.github.io/; convert it with NILMTK; confirm the sampling rate and terms; pre-train the baselines. The SharePoint link must be tested now.
- Bench-flash the PZEM library and the ATECC608 example (do not lock the chip yet).
- Borrow the five loads and check the kettle and iron are in good condition.
- Get the Haryana DHBVN/UHBVN domestic tariff slabs for the bill explainer.

### 7. Feasibility verdict
**Buildability: 4/5.** It would be 5 without the mains rule. The parts are commodity and in stock, and the libraries are mature. The only uncertain steps are provisioning the ATECC608 and the organisers' decision on the sealed mains box.

**Type: safe.** It will work. The story is smaller: the device market is thin, and the law already provides a check meter.

**Biggest risk on the night:** the organisers refuse the sealed mains box. That removes the live kWh-error number, which is the first result judges will ask for.

---

## NOT CHECKED
- **Seller stock and freshness:**
  - current stock at robu.in and zbotic.in (both block page fetches; their prices come from search snippets on listings indexed 7–11 months ago);
  - shipping times and charges for every seller;
  - whether the electronicscomp PZEM-004T split-CT listing is v3.0 (Modbus).
- **Unconfirmed part specs:**
  - PZEM-004T energy (kWh) accuracy class (only V/I/P at 0.5% and the CT at class 1.5 were seen);
  - the Blackt BT72PM's accuracy and kWh display resolution;
  - BMP280 relative accuracy (the ±0.12 hPa ≈ ±1 m used for the U4 fallback is background, not verified);
  - ICM-42688 availability (not listed at electronicscomp);
  - price of an A7670C 4G Cat-1 module (not listed at electronicscomp).
- **Models and data:**
  - iAWE sampling rate and licence, and whether its SharePoint link opens;
  - whether PetFace dog weights exist (the README shows cat weights only);
  - Kaggle/Colab GPU quotas;
  - the Ultralytics YOLO licence (AGPL-3.0 is background).
- **Standards:** the processing details and filters in ISO 18738-1 / ISO 8100-34 (paywalled).
- **Air-quality data:** the distance from Ashoka to the Murthal, Sonipat – HSPCB station, and the current CCR portal interface and request limits (the one-week cap on 15-min requests is from a 2020 note).
- **Singapore angles for all four finalists** (lift monitoring, the dog TNRM programme, haze, smart meters): background only, no search spent.
- **Event and campus:** SPARK Night rules on pre-built hardware, code and data; actual kit contents; the Ashoka facilities/AMC permission process for U4 Plan A; whether a campus animal-care roster exists for U1.
- **Already assigned elsewhere:** the R2 problem numbers reused in the thesis outlines are being verified by R3-claims-01/02. Airveda/Qubo in-app efficacy features and KALA traction were also not checked here.

Searches used: 16
