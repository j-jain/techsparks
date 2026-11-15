# R3-build-02 — Build feasibility: F1, H1, E3, S2  (agent: Opus, date 2026-11-03)

Method notes (read first)
- Prices: Robocraze prices come from the store's own product-search JSON (`robocraze.com/search/suggest.json`, then `/products/<handle>.js` for stock), zbotic prices from its WooCommerce store API, both fetched 3 Nov 2026. Both are listing prices including GST (zbotic figures equal base × 1.18, e.g. ₹2,899 × 1.18 = ₹3,420.82). "(snippet)" = price seen only in a search summary. "est., NOT VERIFIED" = my estimate, no listing opened. robu.in blocked catalogue queries (HTTP 403), so robu prices appear only where a search snippet showed them.
- Stock is as of 3 Nov 2026. Order deadline for everything: **Thu 5 Nov** (gives 8 days before 13 Nov; the brief's "by ~7 Nov" is the latest safe date). Delivery times to Sonipat were not checked (NOT CHECKED); domestic in-stock items usually take 3–6 days (assumption). Import-route sellers (Tanotis, cart2india: "ships in 10 working days") are marked HIGH delivery risk.
- "(background)" = my own technical knowledge, not sourced this round. "(my arithmetic)" = my calculation.

Cross-cutting rules for all four builds
1. Campus Wi-Fi is likely WPA2-Enterprise or a captive portal (assumption, NOT CHECKED); ESP32 boards handle these poorly. Bring a travel router or a dedicated phone hotspot.
2. Freeze model thresholds before the test block and write the config hash and time into the repo README ("pre-registration"). Judges trust numbers that could not be tuned on the test set.
3. Record a full backup demo video as soon as the 02:00 milestone works, and again at ~07:30.
4. Name a safety officer (the bio member suits this) who holds the stop authority, the extinguisher location and the test log.
5. Team template: C1 = ML/CS lead, C2 = embedded + web/dashboard, HW1 = sensors/circuits, HW2 = mechanical/3D-print/rig, B = bio/wet-lab. For a 4-person team, HW2's work goes to HW1 and C2.

---

## F1 Digital-arrest call-guard puck

### 1. Bill of materials

Architecture decision for the night: stage 1 on the puck (ESP32-S3: microphone capture, voice-activity gating, Hindi voice warning, LEDs; optional 4-word keyword spotter); stage 2 on a laptop on the same LAN (streaming Hindi/Hinglish ASR + cue classifier + fusion). Say on stage that the laptop stands in for a Pi 5 or the family's old Android phone and that no audio leaves the LAN. No part here is a delivery risk.

Pre-order (all in stock at Robocraze, 3 Nov 2026):

| Item | Qty | Listing | Unit ₹ | Line ₹ | Note |
|---|---|---|---|---|---|
| ESP32-S3 dev board, 8 MB flash / 8 MB PSRAM (7Semi DevKitC-1-N8R8) | 2 | https://robocraze.com/products/7semi-esp32-s3-dev-boardc-1-n8r8-wifi-bluetooth-dual-usb-c-rgb-led | 949 | 1,898 | Alt: SmartElex ESP32-S3 ₹825 https://robocraze.com/products/smartelex-esp32-s3-wifi-ble-development-kit |
| INMP441 I2S MEMS microphone | 3 | https://robocraze.com/products/inmp441-mems-high-precision-omnidirectional-microphone-module-i2s | 179 | 537 | 1 spare. Alt: zbotic ₹133.34 (in stock) https://zbotic.in/product/inmp441-mems-omnidirectional-microphone-module-high-precision-snr-low-power-i2c-interface-supports-esp32/ |
| MAX98357A I2S 3 W class-D amplifier | 2 | https://robocraze.com/products/smartelex-max98357a-i2s-audio-breakout-amplifier-for-raspberry-pi-and-microcontrollers | 195 | 390 | Other Indian listings are imports at ₹844–2,100 (Tanotis, cart2india, snippet); buy Robocraze |
| WS2812 16-LED ring (status light) | 2 | https://robocraze.com/products/ws2812-16-bit-rgb-led-round | 78 | 156 | |
| 1.3" I2C OLED 128×64 | 1 | https://robocraze.com/products/1-3in-oled-display | 339 | 339 | Optional |
| **Pre-order subtotal** | | | | **3,320** | |

Expect in the kit or bring:

| Item | Qty | ₹ | Note |
|---|---|---|---|
| Speaker 3 W, 4 Ω, 40–50 mm | 2 | ~200 (est., NOT VERIFIED) | Usually in maker kits |
| Breadboard, jumpers, 2 push buttons (mute, test), USB-C cables, 10,000 mAh power bank | — | 0 | Kit / own |
| 3D-printed puck enclosure (PLA, ~60 g) | 2 | ~100 (est.) | Print at the Ashoka makerspace before the event |
| Laptop, ≥16 GB RAM, NVIDIA GPU if possible | 1 | 0 | ASR server |
| Travel router or phone hotspot; 2–3 team phones for role-play calls | — | 0 | Own |

**Total ≈ ₹3,620** (₹3,320 verified + ~₹300 estimates). Per-puck BOM at single-unit retail ≈ ₹1,550 (ESP32-S3 949 + mic 179 + amp 195 + LED ring 78 + speaker ~100 + enclosure ~50; my arithmetic), inside R2's ₹1,500–2,500 assumption. A Raspberry Pi 5 is not needed overnight (Robocraze listed only Pi 5 accessories on 3 Nov, e.g. the 27 W PSU at ₹1,249; board price NOT CHECKED).

Software (free): faster-whisper (CTranslate2) multilingual small/medium; AI4Bharat IndicWhisper (Vistaar: Whisper fine-tuned on 10.7k hours across 12 Indian languages, lowest average WER per language on its benchmark; a Hindi checkpoint `whisper-medium-hi_alldata_multigpu` is listed, code/models via GitHub AI4Bharat/vistaar; Hugging Face repo and a faster-whisper/CTranslate2 conversion NOT confirmed — https://arxiv.org/abs/2305.15386 and https://admin.models.ai4bharat.org/models/, snippets); a multilingual sentence-embedding model (multilingual-e5-small or LaBSE, background) + scikit-learn; Telegram Bot API; optional Edge Impulse for on-device keywords. Espressif's own ESP-SR WakeNet/MultiNet target English and Mandarin; Hindi keywords need custom training on your own recordings (vendor blog, https://zbotic.in/esp32-voice-assistant-offline-keyword-detection-tutorial/, snippet, treat as unverified).

### 2. Hour-by-hour plan (18:00 Fri 13 Nov → 12:00 Sat 14 Nov)

Roles: C1 = ASR + classifier; C2 = ESP32 firmware, alert path, dashboard; HW1 = audio wiring, puck #1; HW2 = enclosure, puck #2, test rooms; B = script author, actor, blind test lead (no wet-lab work in this project, so B owns test integrity).

| Time | C1 | C2 | HW1 / HW2 | B |
|---|---|---|---|---|
| 18:00–19:00 | Start ASR server offline with pre-downloaded models; time one 5 s chunk on small and medium | Router up; flash the pre-tested I2S capture firmware | HW1 wires INMP441 + MAX98357A to ESP32-S3 #1, speaker test | Seal the 40 test scripts (written pre-event, never shown to C1/C2) |
| 19:00–20:30 | Streaming loop: VAD-gated 5 s chunks with 1 s overlap, `language="hi"`, Silero VAD filter on (background), keep Devanagari + Latin output; log latency per chunk | Puck → laptop audio over WebSocket/UDP (16 kHz, 16-bit mono = 256 kbit/s); half-duplex: mic stream paused while the puck speaks | HW2 wires puck #2; acoustic check: team phone on speaker 0.5–1.5 m from puck, 30 s recording, C1 checks the transcript | Rehearse the 4 dev-set scam variants with HW2 as the "officer" |
| 20:30–23:00 | Cue model: (a) lexicon of ~80 cue phrases in Devanagari and Roman (CBI/सीबीआई, ED, money laundering, arrest warrant, "kisi ko mat batana", "video on rakhiye", parcel, drugs, RBI verification, safe account, transfer); (b) embedding + logistic regression over 5 classes (authority, secrecy/isolation, threat, payment demand, benign) trained on the 600 pre-written turns; (c) fusion: risk score over a 3-min sliding window + call-duration term; alert when ≥3 of 4 cue classes, or authority + payment | Telegram bot message with cue timeline; Hindi warning WAV in ESP32 flash ("Police video call par arrest nahi karti. Phone kaatiye, 1930 par call kijiye"); LED states green/amber/red | Enclosure fit; mic port away from speaker; mute button | Record 10 dev calls (not test) for tuning |
| 23:00–01:45 | Tune thresholds on dev calls only; 01:45 FREEZE model and thresholds, write config hash in README | Streamlit dashboard: live transcript, cue timeline, risk score, alert time | Puck #2 finished; spare mic pre-wired | Set up test room 2; timing sheet |
| **02:00 milestone** | Full chain on a dev call: "officer" speaks on speakerphone → puck speaks the Hindi warning → Telegram alert arrives → dashboard shows the cue timeline. Record the backup video now. | | | |
| 02:00–03:00 | Stretch only if milestone met: IndicWhisper vs faster-whisper A/B on the 10 dev calls | Stretch: Edge Impulse 4-keyword model on ESP32-S3 (only if samples were recorded pre-event) | Sleep in shifts | Sleep |
| 03:00–06:30 | TEST block (code frozen; watch logs only) | Logs ground-truth timestamps | Actors | Runs the protocol in two rooms in parallel, 20 calls each (~100 min per room) |
| 06:30–08:00 | Metrics, confusion matrix, seconds-to-alert, error analysis | Demo mode, polish | Photos, tidy build | Thesis draft |
| 08:00–10:00 | All: one-page Deep Tech Thesis, 3 slides, three demo rehearsals, second backup video | | | |
| 10:00–12:00 | Pitch window / buffer | | | |

Cut-down fallbacks:
- I2S mic or ESP32 audio fails → a USB mic or phone on the laptop is the "ear"; the ESP32 keeps the speaker and LEDs. Say so on stage.
- ASR too slow or poor on Hinglish speakerphone audio → smaller model + lexicon-only cues (the keyword path alone triggers on any scripted call).
- Wi-Fi fails → stream audio over the ESP32-S3's native USB serial (256 kbit/s fits).
- Telegram unreachable → local siren/LED only, plus an SMS sent by hand from a tethered phone for the demo.

### 3. Test protocol (the numbers R2 named: recall, false positives, seconds-to-alert)

Pre-registered at 01:45: model version, thresholds, and the definition of an alert (first red state).

Test set (authored by B pre-event, sealed, never seen by C1/C2; at least half of each script's cue phrases must not appear in the training turns):
- 20 scam calls, 4 variants × 5: S1 CBI/ED money laundering ("aapke Aadhaar se account khula hai"); S2 courier parcel with drugs; S3 TRAI/telecom SIM disconnection handed to "police"; S4 RBI "verification / safe account" transfer. 2–4 min each, each containing ≥3 of the 4 cue classes.
- 20 benign calls: B1 genuine bank fraud-team call (blocks the card, never asks for a transfer) ×4; B2 courier delivery ×3; B3 doctor/hospital ×3; B4 relative urgently asking for money ×3 (hard negative); B5 police passport-verification call ×3 (hard negative: real authority, no payment); B6 a TV news segment about digital arrest playing in the room ×4 (hard negative; a news-style script read by an actor, not copied from a broadcast).
- Extra conditions, reported separately: 5 scam calls with the phone held to the ear (victim's side only audible); 3 scam calls with TV/fan noise.

Procedure: B shuffles the order. The "caller" sits in another room and calls a team phone placed on speaker 1 m from the puck; the "victim" replies naturally. B logs the call-connect time and the time of the first cue utterance; the system logs its alert time. Each call stops at 4 min or 30 s after an alert.

Report: recall (alerted scams / 20); false-positive count (alerted benign / 20) and precision; median and IQR of seconds-to-alert from call connect and from the first cue; per-cue-class hit rate; Wilson 95% intervals (e.g. 18/20 → 0.70–0.97, my arithmetic). Expect alerts roughly 60–120 s into a call because fusion waits for ≥3 cue classes (my estimate; measure it).

Results template:

| Condition | n | Alerted | Recall / FP | Median s-to-alert (call start) | Median s-to-alert (first cue) | Notes |
|---|---|---|---|---|---|---|
| Scam S1–S4, speaker | 20 | | | | | |
| Benign B1–B6, speaker | 20 | | | n/a | n/a | which hard negatives fired |
| Scam, phone at ear | 5 | | | | | |
| Scam, TV/fan noise | 3 | | | | | |

Confusion matrix (speaker condition): rows = truth (scam / benign), columns = predicted (alert / no alert).

State in the results that the test is staged, team-authored, same voices and quiet rooms, so the numbers are optimistic and prove the plumbing, not field performance.

Safety and ethics: no calls to outsiders, no recordings of real victims, no real officials' names in scripts, never call 1930 for testing; all actors consent; audio ring buffer and transcripts deleted after the event.

### 4. Demo script (3 min) and Deep Tech Thesis outline

Demo:
- 0:00–0:20 Hook: "In 2024 Indians reported 1,23,672 digital-arrest cases and lost ₹1,935 crore. The call lasts hours, and no app on a budget phone is allowed to hear it." Hold up the puck.
- 0:20–0:40 Why: Android removed call-audio capture for third-party apps (Android 10, Play policy May 2022); Google's detector runs on Pixel 9+ only; Truecaller's family alert is number-based.
- 0:40–1:50 Live: a teammate calls the "victim" phone on speaker as a "CBI officer". The dashboard lights authority → secrecy → threat → payment; the puck speaks the Hindi warning; the "son's" phone gets a Telegram alert ("Maa ko CBI call: 4 cues, 1 min 12 s").
- 1:50–2:30 Results table: recall x/20, false positives y/20, median seconds-to-alert; which hard negatives fired (police verification, TV news) and what failed.
- 2:30–3:00 Business and ask: bank senior/wealth desks; ₹3,999 device or bank-paid ₹99/month; SAM ₹159–297 crore/yr.
- If hall noise breaks the live run, play the backup video and keep talking.

Deep Tech Thesis (one page):
- Problem (two numbers): 1,23,672 digital-arrest cases and ₹1,935.51 crore lost in 2024 (Rajya Sabha reply via The Quint, 17 Apr 2025); digital arrest ≈ 8% of ₹19,812.96 crore cyber-fraud losses in 2025 ≈ ₹1,585 crore (I4C via IANS, 3 Jan 2026; my arithmetic). Supreme Court suo motu case (9 Feb 2026).
- Why now: the platform blind spot (third-party apps cannot hear calls); Google Scam Detection in India since 20 Nov 2025 but Pixel 9+ only, off by default (TechCrunch); Truecaller Family Protection (13 Mar 2026) is number-reputation only; DPDP Rules phase in to ~12 May 2027, which favours on-device processing.
- Deep-tech core: streaming Hinglish ASR plus script-level intent fusion (authority, isolation, threat, payment, accumulated over minutes) on an always-on acoustic edge device with a half-duplex warning loop; works with any phone, feature phones and WhatsApp video "custody".
- What we built: two pucks (ESP32-S3 + INMP441 + MAX98357A), LAN ASR + classifier, Telegram family alert, cue-timeline dashboard.
- Measured result: recall, false positives and median seconds-to-alert on 40 staged calls, with the caveat.
- Business: buyer = private bank senior/wealth desks, then general insurers and telcos; ₹3,999 device or ₹99/month bank-paid; SAM ₹159–297 crore/yr (R2, value-based at 10% of loss averted, assumption); puck BOM ≈ ₹1,550 at retail.
- What ₹2 lakh over 3 months proves: 30 pucks in consenting senior homes (~₹50k hardware) to measure false alarms per day of real household audio (TV, ordinary calls), which decides whether families keep it switched on; a consented 500-call Hinglish + two-regional-language script corpus; stage 2 moved onto a ~₹5k Android phone or a Pi; one bank letter of intent.
- Singapore angle: Singapore runs ScamShield (OGP; 820k+ downloads, an on-device classifier plus police blocklist, per R2 snippets) and faces government-official impersonation scams in English, Mandarin, Malay and Tamil; the immersion goal is to test script-level detection across those languages and meet the agencies running ScamShield (hypothesis; nobody contacted).

### 5. Judge-proofing

1. "Google and Samsung already do on-device scam detection; this becomes a free phone feature." → Today it is Pixel 9+ (under 1% of Indian phones, TechCrunch 20 Nov 2025) and Galaxy flagships, off by default, Phone-app calls only, no family loop. Seniors use budget Android and feature phones, and the "custody" runs for hours on WhatsApp/Skype video. The puck needs no OS access. If Google ships it to every Android phone, our wedge narrows to feature phones, video custody and the family alert; we say so.
2. "An always-listening microphone in a senior's home is a privacy problem. DPDP?" → Stage 1 only gates voice; stage 2 runs on the home LAN; no audio is stored beyond a ≤30 s ring buffer; transcripts are discarded after scoring; only cue labels leave the house; there is a physical mute; the consent notice follows the DPDP Rules being phased in to May 2027.
3. "Your 40 calls are staged by your own team, and scammers will change their words." → Agreed; the numbers prove the plumbing and are optimistic. The model scores the con's structure (authority + isolation + threat + payment over minutes), which a scammer cannot drop without dropping the con; the number that matters next is false alarms per day in real homes, which is what the grant buys.

### 6. Pre-event checklist

- Order all Robocraze parts by Thu 5 Nov; flash and test I2S capture and playback at home by 11 Nov.
- Write 300 scam + 300 benign training turns, paraphrased from published victim accounts (summarise, do not copy transcripts); B separately writes the 40 sealed test scripts.
- Download and test offline: faster-whisper small + medium (and large-v3-turbo if a GPU laptop is available, background), the IndicWhisper Hindi checkpoint from AI4Bharat/vistaar, multilingual-e5-small. Measure latency on the actual laptop.
- A team member creates a Telegram bot with BotFather on their own account and a test "family" group.
- Record the Hindi (and English) warning WAV at 16 kHz.
- Optional on-device keywords: record 50 samples × 4 keywords × 4 speakers; train in Edge Impulse (team member's own account); flash and test.
- Print two enclosures at the makerspace; pack a travel router/hotspot.
- One-paragraph consent note for actors; rules: no outside calls, no real officials' names.

### 7. Feasibility verdict

**Buildability 4/5. Safe pick.** Every part is cheap and in stock; most of the work is software the CS members already know; the keyword path guarantees a working demo. The story ceiling is high (₹1,935 crore problem, a Supreme Court case), but the measured result is soft because the calls are staged. Biggest risk on the night: Hinglish ASR on speakerphone audio in a noisy hall, which shows up as late or missed alerts, or false alarms on the TV-news and police-verification hard negatives.

---

## H1 Counterfeit-medicine checker (tablets only)

### 1. Bill of materials

Sensor decision: the AS7265x is a HIGH delivery risk (robotools lists it with no stock status; ibots shows "available on backorder"). The in-stock AS7343 (14 channels; the 7Semi listing says 350–1000 nm, on-board LED) is the primary sensor; the AS7341 is the second unit. Order the AS7265x only if the seller confirms dispatch by 7 Nov.

Pre-order:

| Item | Qty | Listing | Unit ₹ | Line ₹ | Stock 3 Nov | Delivery risk |
|---|---|---|---|---|---|---|
| AS7343 14-ch spectral sensor (7Semi) | 2 | https://robocraze.com/products/7semi-as7343-14-ch-spectral-sensor-module | 1,600 | 3,200 | In stock | Low |
| AS7341 11-ch spectral sensor (Waveshare) | 1 | https://zbotic.in/product/waveshare-as7341-spectral-color-sensor-visible-spectrum-sensor-multi-channels-high-precision-i2c-bus/ | 1,867.94 | 1,867.94 | In stock | Low. Alt: DFRobot Fermion AS7341 ₹1,090 at ibots (snippet) |
| 1.3" I2C OLED | 1 | https://robocraze.com/products/1-3in-oled-display | 339 | 339 | In stock | Low |
| **Pre-order subtotal** | | | | **5,406.94** | | |
| STRETCH: SparkFun Triad AS7265x (18 ch, 410–940 nm) | 1 | https://robotools.in/shop/sensor/light-color-sensor/sparkfun-triad-spectroscopy-sensor-as7265x/ (₹7,488, stock not stated); https://ibots.in/product/sparkfun-triad-spectroscopy-sensor-as7265x/ (₹8,330.80, backorder) | 7,488 | (7,488) | Unclear / backorder | **HIGH** — fallback is the AS7343 already ordered |

Consumables and kit (estimates, NOT VERIFIED unless a listing is given):

| Item | ₹ | Note |
|---|---|---|
| ESP32 dev board, breadboard, jumpers | 0 | Kit |
| OTC tablet library: 8 products, 2 strips each (ideally 2 batches) | 800–1,200 | Local chemist, keep bills |
| Ferric chloride powder (sold as PCB etchant), dropper bottles, distilled water, 10 glass vials, nitrile gloves, goggles | ~600 | Or borrow from the Ashoka bio/chem lab with permission |
| Acetone (nail-polish remover) for batch-code erasure samples | ~60 | |
| 37 °C bath: beaker on the kit hot plate or a USB mug warmer + DS18B20 probe (kit) | ~300 | |
| Black PLA chamber with fixed tablet seat, black flock/velvet, white reference (PTFE tape stack or matte paper stack) | ~200 | Print before the event |
| Clip-on phone macro lens | ~300 | Optional |

**Total ≈ ₹7,900** (₹5,407 verified + ~₹2,500 estimates); **≈ ₹15,400 with the AS7265x** (robotools price).

Library rule (no prescription drugs): ibuprofen is on India's Schedule H list (at least in higher strengths; https://en.wikipedia.org/wiki/Schedule_H and https://laafon.com/understanding-schedule-h-drugs-regulations-and-restrictions-in-india/, snippets), so drop it even though R0 named it. Paracetamol was in the June 2022 proposal to move 16 drugs to OTC/Schedule K (https://theprint.in/india/centre-plans-to-bring-16-common-drugs-for-cough-cold-pain-under-over-the-counter-category/986910/, snippet; finalisation not confirmed). Buy only strips without the Rx symbol or the Schedule H warning box. Suggested library: paracetamol 500 mg × 3 brands; antacid chewable × 2 brands; vitamin C chewable; calcium + D3; one multivitamin tablet. Report brands as Brand A/B/C so nothing reads as "brand X is fake".

"Fakes" are labelled surrogates ("SURROGATE – NOT MEDICINE"), destroyed after the event: (a) wrong-product lookalike (calcium or antacid presented as paracetamol); (b) no-API (a white dextrose/glucose tablet or chalk tablet of similar size); (c) brand swap (paracetamol brand B presented as brand A); (d) re-coated (genuine tablet with a thin food-colour or clear-varnish film); (e) 50%-API re-press: skipped (no tablet press); say so.

Physics to state honestly (background): a 350–1000 nm silicon sensor fingerprints the coating, dye, excipients and surface scattering. The molecular bands that identify an API are mostly beyond 1,000 nm, so the box can say "matches the genuine product or not", not "contains X mg of paracetamol". The bio colour test supplies the API-presence check for paracetamol (phenol + ferric chloride gives a blue-violet colour; background chemistry).

### 2. Hour-by-hour plan

Roles: HW1 = sensor and optics; HW2 = chamber, scanning operator; C1 = data pipeline + models; C2 = phone pack-forensics + UI; B = colour and disintegration tests, sample custody, blinding.

| Time | HW1 / HW2 | C1 | C2 | B |
|---|---|---|---|---|
| 18:00–19:00 | HW1 wires AS7343 #1/#2 (I2C, 3.3 V) to ESP32; firmware reads all channels at fixed gain and integration, LED-on minus LED-off (ambient rejection). HW2 fits the pre-printed chamber | Serial → CSV logger with metadata (sensor, product, strip, tablet, face, read #) | Phone capture flow (simple web page with camera) | Label sample bags; wet bench set up away from electronics; gloves and goggles |
| 19:00–20:00 | Calibration: dark, white and black references each session; one tablet re-seated 10× → per-channel CV; 10-min LED warm-up drift check | Live plots, CV calculation | Photo set of all 8 strips (front, back, batch code) | FeCl₃ solution made up (dilute, small volume) |
| 20:00 gate | If re-seat CV is above ~5% on most channels, fix the seat geometry before building the library | | | |
| 20:00–23:00 | LIBRARY: 8 products × 3 training tablets × 2 faces × 5 re-seats = 240 reads per sensor (~10 s each ≈ 45 min per sensor; two sensors in parallel) | Normalise (white-reference ratio, SNV); PCA view; closed-set classifiers (kNN, SVM, LDA); per-brand one-class model (robust Mahalanobis) for "matches claimed brand?" | Batch-code erasure set: acetone wipe on 3 strips; classifier (edge density / OCR presence + batch-format check) | FeCl₃ test on all 8 products; disintegration time at 37 °C in water, 3 tablets per product; turbidity read through a vial by the spare sensor |
| 23:00–02:00 | Handheld box: scan → verdict on OLED | Web app: "Claimed Brand A → MATCH 0.94 / NO MATCH (closest: calcium class)" | Phone check integrated | Colour-test result entry in the app |
| **02:00 milestone** | A live scan identifies a tablet and flags a surrogate; FeCl₃ shows paracetamol positive vs calcium negative; an erased batch code is flagged. Record the backup video. | | | |
| 02:00–05:00 | BLIND TEST: operator (HW2) does not know labels | Frozen model | Photo blind test | B codes and shuffles all test items and keeps the key |
| 05:00–07:00 | | Analysis, confusion matrices, failure gallery | Results slides | Colour/disintegration tables |
| 07:00–10:00 | All: thesis, demo rehearsal, second backup video | | | |
| 10:00–12:00 | Pitch window / buffer | | | |

Cut-down fallbacks:
- AS7343 dead or absent → AS7341; both dead → a TCS34725-class RGB sensor if the kit has one, or the phone camera under a fixed LED as a 3-channel colourimeter, and the colour test carries the content claim.
- I2C trouble on the ESP32 → an Arduino Uno/Nano from the kit.
- Ferric chloride not allowed in the hall → run the colour test in the lab before the event, bring the photos and sensor reads, demo only the dry scan live; disintegration in water stays.
- Chamber fails → black cardboard box with a fixed hole and taped seat.

### 3. Test protocol

Splits are by tablet, never by read (reads of one tablet never appear in both train and test).

Measures:
1. Repeatability: per-channel CV, one tablet re-seated 10×, per sensor.
2. Closed-set identification, 8 products: accuracy and confusion matrix on held-out tablets (2 unseen tablets per product, from a different strip where possible, × 2 faces × 3 reads = 96 reads).
3. Open-set verification against the claimed brand: impostor rejection rate (sensitivity) by surrogate type (a)–(d), 10 surrogates × 2 faces × 3 reads = 60 reads; genuine acceptance (specificity proxy) on the 96 held-out reads; threshold fixed on training data at 01:45.
4. Brand vs brand, same molecule (paracetamol A/B/C): pairwise accuracy. This answers R2's unknown 2.
5. Through-blister vs bare tablet: 4 products × 2 tablets × 3 reads = 24 reads through the clear blister side; report the accuracy drop.
6. Colour test: paracetamol present vs absent, 10 + 10 blind samples; sensitivity/specificity by eye and by sensor (absorbance-like ratio on the 550–600 nm channels vs a blank).
7. Disintegration: time to full disintegration at 37 °C in water, mean ± SD of 3 tablets per product.
8. Pack forensics: erased vs intact batch codes, 5 + 10 blind photos.
9. Seconds per scan; cost per scan.

Benchmark to quote alongside: PLoS NTD 2021 (12 portable devices): no-API or wrong-API sensitivity 91.5–100%; 50%/80%-API (substandard) sensitivity 5.6–50% for IR and Raman devices (R2, Europe PMC abstract of PMC8483346). We did not test a 50%-API tablet; say so.

Results templates:

| Test | n (reads / samples) | Metric | Result | Notes |
|---|---|---|---|---|
| Re-seat repeatability | 10 per sensor | median CV across channels | | |
| Closed-set ID (8 products) | 96 | accuracy | | confusion matrix attached |
| Impostor (a) lookalike | 18 | rejected % | | |
| Impostor (b) no-API | 12 | rejected % | | |
| Impostor (c) brand swap | 18 | rejected % | | |
| Impostor (d) re-coated | 12 | rejected % | | |
| Genuine accepted | 96 | accepted % | | |
| Paracetamol A vs B vs C | 36 | accuracy | | |
| Through blister | 24 | accuracy (vs bare) | | |
| FeCl₃ paracetamol test | 20 | sens / spec | | |
| Erased batch code | 15 | sens / spec | | |
| Time per scan | — | seconds | | |

| Product (anonymised) | Disintegration time, s (3 tablets) | FeCl₃ colour |
|---|---|---|
| Paracetamol A | | |
| … | | |

Safety: nothing is ingested; gloves and goggles for ferric chloride (corrosive, stains; small dilute volumes); liquid waste in a labelled bottle returned to the lab; tablets returned to the lab or a pharmacy take-back; no prescription drugs; surrogates labelled and destroyed; no claim that any real product is counterfeit; no medical claims anywhere.

### 4. Demo script (3 min) and Deep Tech Thesis outline

Demo:
- 0:00–0:25 Hook: Delhi, Aug 2026: 588 cancer vials (~₹9 crore), batch numbers wiped with acetone; fakes supplied to 90+ Bengaluru hospitals; regulators found 245 spurious samples in FY2024-25. "The QR code checks the label. Nobody checks what is inside."
- 0:25–1:30 Live: a judge picks a tablet from a tray (genuine or surrogate); 5-second scan; screen shows "Claimed Brand A: MATCH 0.96" or "NO MATCH, closest: calcium class". Then a phone photo of an acetone-wiped strip → "batch code erased". Then one drop of ferric chloride: violet = paracetamol present.
- 1:30–2:20 Blind-test numbers, the brand-vs-brand result (even if weak) and where it fails (white-on-white tablets, substandard dose not tested).
- 2:20–3:00 Business and ask: hospital pharmacy goods-receipt, oncology first; ₹15,000 + ₹1,000/month; SAM ≈ ₹60 crore/yr; the Indian brand-spectra library is the moat.

Deep Tech Thesis:
- Problem (two numbers): 245 spurious drug samples found by regulators in FY2024-25 (282 in FY2023-24; ThePrint, 17 Sep 2026) and the Delhi oncology racket, 588 vials worth ~₹9 crore with batch numbers removed by acetone (Medical Dialogues, 24 Aug 2026). Context: CDSCO's Sept 2026 alert listed 330 NSQ + 1 spurious; LocalCircles: 15% of 1,06,000 respondents say they were sold counterfeit medicine (self-reported).
- Why now: the QR mandate widens to vaccines and anti-cancer drugs from 1 Jul 2027 but QR codes "can be copied" (ThePrint, 25 Jun 2026); 14-channel spectral chips now cost ₹1,600 at Indian retail (Robocraze, 3 Nov 2026); published evidence that cheap devices catch no-API/wrong-API fakes at 91.5–100% sensitivity (PLoS NTD 2021).
- Deep-tech core: LED-differential, white-referenced multispectral reflectance fingerprint (350–1000 nm) with an open-set per-brand verification model and a growing Indian brand-spectra library; plus a colourimetric API-presence test and pack forensics.
- What we built and measured: handheld box + app; blind-test table.
- Business: buyers with liability, i.e. hospital pharmacies (after the Bengaluru 90-hospital case), oncology pharmacies, pharma brand-protection teams, state drug controllers, not retail chemists; ₹15,000 + ₹1,000/month per site; SAM ≈ ₹60 crore/yr (R2, 50,000 outlets × ₹12,000/yr, assumption).
- What ₹2 lakh over 3 months proves: a 3-month goods-receipt pilot with a licensed hospital pharmacy (they hold the stock and licences); a multi-batch library for ~200 SKUs, because batch-to-batch variation is the real false-alarm risk; a head-to-head against a micro-spectrometer (Hamamatsu C12880MA class, price NOT SEARCHED); a request to a state drug controller for Government-Analyst-confirmed spurious samples; a legal opinion on device status (triage, "hold and send to lab").
- Singapore angle: Singapore's Health Sciences Authority regulates and tests medicines in a regional pharma manufacturing and distribution hub; the immersion goal is cross-border library sharing for ASEAN fakes (hypothesis, background; nobody contacted).

### 5. Judge-proofing

1. "A ₹1,600 colour sensor is not spectroscopy; it cannot see the API." → Correct for 350–1000 nm silicon: it sees coating, dye, excipients and scattering. That is why we claim only "matches the genuine product or not" and add a chemical colour test for API presence. It will not catch substandard (under-dosed) stock; the PLoS NTD 2021 study found even IR/Raman devices caught 50–80%-API samples only 5.6–50% of the time.
2. "Fakers copy the look, and genuine batches vary, so you will false-alarm." → Copying the visible look is not the same as matching the coating and excipient reflectance into the near-infrared. Batch variation is the real risk: tonight's library is one batch per brand, so the pilot's first job is the multi-batch false-alarm rate. The output is "hold and send to the Government Analyst", never a verdict (under the Drugs and Cosmetics Act only a Government Analyst's report establishes "spurious").
3. "Who pays? Chemists profit from cheap fakes, and Thermo TruScan already exists." → Not chemists. Hospitals and oncology pharmacies carry the liability; brand owners and regulators have budgets. TruScan and trinamiX handhelds are lakh-priced, have no Indian brand library and are not sold to hospital stores; we are 10–50× cheaper and the library is the moat.

### 6. Pre-event checklist

- **Bench test by 10–11 Nov (R2 unknown 2):** AS7343 on two paracetamol brands + one calcium tablet. If brand-vs-brand does not separate, reframe the pitch to "wrong-product and no-API" before the night.
- Order AS7343 × 2 + AS7341 by Thu 5 Nov; AS7265x only if robotools/ibots confirm dispatch by 7 Nov.
- Buy the tablet library (no Rx or Schedule H marking; drop ibuprofen); 2 strips per product, two batches where possible; keep bills.
- Permission to use ferric chloride, and to do small wet work in the hall; if refused, run the colour test in the lab beforehand.
- Print the dark chamber and tablet seat; prepare white and black references; macro lens.
- Python environment (scikit-learn, pyserial, numpy, pandas) and the phone capture page tested.
- Decide the brand anonymisation key (Brand A/B/C) and keep it off the slides.

### 7. Feasibility verdict

**Buildability 4/5. Safe pick.** The build is simple (an I2C sensor, a printed chamber, a classifier); the in-stock AS7343 removes most delivery risk; a demo by 02:00 is near-certain. The ceiling is moderate: the honest claim is "wrong-product/no-API triage", not counterfeit detection in general. Biggest risk on the night: most OTC tablets are white, and a 350–1000 nm chip may not separate two white paracetamol brands, which would leave the headline result weak; the pre-event bench test tells you before you commit.

---

## E3 EV charging-bay safety monitor (low-voltage rig only)

### 1. Bill of materials

Safety envelope (non-negotiable): 12 V DC only, fed from **enclosed plug-in adapters** (no open-frame SMPS with exposed 230 V screw terminals in the hall); the dummy pack heater is capped at 80 °C by an independent hardware thermostat; isopropyl alcohol (IPA) ≤5 drops on a cotton bud, away from the heater, no flames; one 18650 charged within spec by a TP4056, inside a LiPo bag, attended at all times; no abuse of any lithium cell.

IR-array decision: the MLX90640 is out of stock at Robocraze (₹4,585 / ₹4,715), robu (₹6,500, restock 25–30 days, snippet from stg.robu.in) and zbotic's 110° version; zbotic's 55° version is in stock at ₹8,730.82. Fallbacks in stock: AMG8833 8×8 (₹3,420.82, zbotic) and MLX90614 single-point (₹709, Robocraze). An 8×8 array at 1 m with a 60° field of view resolves ~14 cm pixels (my arithmetic, background FOV), enough to see a 30 × 20 cm pack zone.

Pre-order:

| Item | Qty | Listing | Unit ₹ | Line ₹ | Stock 3 Nov / risk |
|---|---|---|---|---|---|
| MLX90640 32×24 IR array, 55° (Waveshare) | 1 | https://zbotic.in/product/waveshare-mlx90640-ir-array-thermal-imaging-camera-3224-pixels-55-fov/ | 8,730.82 | 8,730.82 | In stock; **MEDIUM** risk (only one in-stock seller found). Other prices: ThinkRobotics 110° ₹6,499.99 (snippet); Tanotis SparkFun 55° ₹8,530 import (snippet) |
| — fallback A: AMG8833 8×8 | (1) | https://zbotic.in/product/amg8833-ir-88-thermal-imager-array-temperature-sensor-module/ | 3,420.82 | — | In stock |
| — fallback B: MLX90614 single-point IR | (1) | https://robocraze.com/products/mlx90614esf-infrared-ir-temperature-sensor-module | 709 | — | In stock |
| BME688 gas/T/RH/P breakout, 2.54 mm pitch (7Semi Nano) | 1 | https://robocraze.com/products/7semi-bme688-environmental-sensor-nano-breakout | 1,359 | 1,359 | In stock. Cheaper ₹1,004 version has a 1.27 mm header (awkward on a breadboard). SGP30 alternative: M5Stack ₹1,344 out of stock |
| MQ-3 alcohol sensor (cross-check for IPA) | 1 | https://robocraze.com/products/mq-3-gas-sensor-module | 139 | 139 | In stock |
| 12 V 40 W ceramic cartridge heater | 3 | https://robocraze.com/products/12v-40w-ceramic-cartridge-heater | 99 | 297 | In stock (1 pack heater, 1 load, 1 spare) |
| 80 mm aluminium heatsink (dummy pack body; load sink) | 2 | https://robocraze.com/products/80mm-aluminium-cpu-heatsink | 271 | 542 | In stock |
| W1209 thermostat (independent hard cut-off at 80 °C) | 1 | https://robocraze.com/products/w1209-digital-temperature-controller-thermostat-module | 99 | 99 | In stock |
| 10k NTC thermistor | 6 | https://robocraze.com/products/10k-temperature-sensor-thermistor | 10 | 60 | In stock |
| INA219 V/I monitor (two straddle the terminal, one logs the 18650) | 3 | https://robocraze.com/products/ina219-i2c-voltage-current-power-monitor-sensor-breakout-board-7semi | 240 | 720 | In stock; set 3 different I2C addresses |
| ADS1115 16-bit ADC (backup for terminal voltage drop) | 1 | https://robocraze.com/products/16-bit-i2c-4-channel-ads1115-module | 145 | 145 | In stock |
| 5 V 30 A relay module (cut-off) | 2 | https://robocraze.com/products/5v-30a-1-channel-relay-module | 145 | 290 | In stock |
| 12 V mini siren | 1 | https://robocraze.com/products/12v-mini-square-siren | 199 | 199 | In stock |
| 12 V 5 A enclosed power adapter | 2 | https://robocraze.com/products/novel-12v-5amp-industrial-grade-smps-power-adapter | 584 | 1,168 | In stock (one for load circuit, one for pack heater) |
| TP4056 1 A charger with protection | 1 | https://robocraze.com/products/tp4056-lithium-battery-charging-board | 26 | 26 | In stock |
| 18650 holder | 1 | https://robocraze.com/products/18650-2-cell-holder | 29 | 29 | In stock |
| LiPo/Li-ion fire-resistant bag 215×45×165 mm | 1 | https://probots.co.in/215x45x165mm-lithium-polymer-battery-fire-and-water-resistant-lipo-li-ion-protection-bag.html | 569 | 569 | (snippet); robu has a large bag "in stock" (snippet, no price) |
| **Pre-order subtotal** | | | | **14,372.82** | |

Kit / bring / estimates:

| Item | ₹ | Note |
|---|---|---|
| Branded 18650 (Samsung/LG/Molicel) from a reputable seller | ~400 (est., NOT VERIFIED) | Do not use a ₹69–102 unbranded "2,500 mAh" cell (Robocraze lists these): likely relabelled; unknown history |
| ESP32 dev boards ×2, breadboards, jumpers, 14–16 AWG wire, screw-terminal blocks (the "loose terminal"), multimeter | 0 | Kit |
| Matte black paint or black electrical tape (emissivity, see below), IPA 99% 100 ml, cotton buds, kitchen probe thermometer, small desk fan | ~400 (est.) | |

**Total ≈ ₹15,170** (₹14,373 verified + ~₹800 estimates); **≈ ₹9,860 with the AMG8833** instead of the MLX90640.

Data (pre-download): NASA PCoE "5. Battery Data Set" zip, 209,708,670 bytes (~210 MB), https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip (HTTP 200, Last-Modified 18 Sep 2022, checked 3 Nov 2026; B0005/B0006/B0007/B0018 .mat files with charge, discharge and impedance runs). The data.nasa.gov listing itself says "This dataset has no data" and points to DASHlink (https://data.nasa.gov/dataset/li-ion-battery-aging-datasets, snippet; DASHlink did not respond on 3 Nov). CALCE battery data page is live with CS2, CX2, INR 18650-20R and A123 sets (https://calce.umd.edu/battery-data, fetched 3 Nov 2026).

Physics notes that decide the rig (background):
- **Emissivity:** bare aluminium has emissivity ~0.05–0.1, so an IR array reads it near ambient even when hot. Wrap the dummy pack and the terminal area in black electrical tape or matte black paint (~0.95). Real e2W packs are plastic-cased, so this is also the realistic case.
- **Loose contacts heat at normal current:** an MCB trips on overcurrent and an RCD on leakage; a loose joint overheats at rated current, so neither trips. Heat = I²R_contact. One 40 W heater as the "charger load" draws ~3.3 A at 12 V; a 0.1–0.3 Ω loose joint dissipates ~1.1–3.3 W at a small terminal (my arithmetic). A 350–750 W e2W charger draws ~1.5–3.3 A at 230 V (background on charger ratings), so the rig reproduces the plug's current level and therefore its contact heating; only the voltage differs.
- **Contact resistance is measured directly:** two INA219s either side of the terminal give ΔV; R = ΔV/I. The INA219 bus-voltage LSB is 4 mV, i.e. ~1.2 mΩ resolution at 3.3 A (my arithmetic, background datasheet LSB).

### 2. Hour-by-hour plan

Roles: HW1 = sensor head (IR array, BME688, MQ-3, thermistors); HW2 = rig (dummy pack + heater + W1209 interlock, load circuit with the screw terminal, relays, siren); C2 = ESP32 firmware, hash-chained signed log, Telegram, dashboard; C1 = fusion logic + SoH model; B = safety officer and test lead (IPA protocol, confounders, timing).

| Time | HW1 | HW2 | C1 | C2 | B |
|---|---|---|---|---|---|
| 18:00–18:45 | Safety brief and organiser sign-off: adapters only, heater ≤80 °C with W1209 cut, IPA ≤5 drops, 18650 attended in bag, extinguisher location | | | | Leads the brief; owns the stop authority |
| 18:45–21:00 | Sensor head on ESP32 #1: MLX90640 (or fallback), BME688, MQ-3 warm-up, 4 thermistors | Dummy pack: heatsink + cartridge heater + black tape + 2 thermistors + W1209 hard cut; load circuit: 12 V → screw terminal → heater-load on second heatsink, INA219s either side; relay in series; siren | SoH model on pre-downloaded NASA data: charge-curve features (CC duration, time to 4.2 V, CV current-decay constant, charge capacity), labels = discharge capacity, split by cell (train B0005/6/7 → test B0018, plus leave-one-cell-out); first MAE by 21:00 | Firmware: 2 Hz sensor frames to laptop (MQTT or HTTP); relay control; HMAC-SHA256 hash-chained event log (each record carries the previous record's hash; key in NVS) | IPA and confounder kit; test log sheets |
| 21:00–23:00 | Thermistor calibration vs kitchen probe (ice water, warm water) | Rig wiring check with multimeter; tight vs loose torque marks on the terminal | Fusion: three levels. Watch = any channel past baseline + 3σ; Warn = rate-of-rise above 2× the largest rise seen in normal cycles, or R_contact up >50% from baseline, or gas resistance down >X% (set from baseline); Cut = Warn on two modalities or pack >60 °C → relay open, siren | Dashboard (IR heat map, R_contact trend, gas, state); Telegram "guard room" alert; log verifier script | |
| 23:00–00:30 | Baselines (30 min normal operation) | First heater ramp; first loose-terminal run | Threshold setting on baseline only | Integration | Times everything |
| 00:30–02:00 | — | Heater ramps 1–3 and loose-terminal runs 1–5 in parallel (separate heatsinks) | Freeze thresholds at 01:45 (config hash in README) | | |
| **02:00 milestone** | Heater ramp → Warn → Cut: relay opens, siren, Telegram, signed log entry; a loose terminal flagged by its R_contact trend before it reaches 60 °C. Record the backup video. | | | | |
| 02:00–03:00 | | Ramps 4–5, terminal runs 6–10 | | | IPA runs (15) and confounders |
| 03:00–07:00 | | 4-hour normal-cycle run (false-alarm test) with scheduled confounders | 18650 charge log features (attended, in bag, 03:00–05:30) | | Logs every human interaction and confounder time; supervises the 18650 |
| 07:00–10:00 | All: analysis, thesis, rehearsal, second backup video | | | | |
| 10:00–12:00 | Pitch window / buffer | | | | |

Cut-down fallbacks:
- MLX90640 does not arrive → AMG8833; if neither, MLX90614 spot sensor aimed at the pack zone.
- BME688 fails → MQ-3 for the IPA test (state it is less selective).
- Organisers refuse the 18650 or IPA → drop them; SoH runs on datasets only; gas demo becomes a recorded clip from a pre-event test in a ventilated lab.
- Heater or relay rig fails → loose-terminal + thermistor demo with the siren driven by the ESP32.

### 3. Test protocol

| Test | What is varied | Trials | Measure and report |
|---|---|---|---|
| T1 Pack overheat (heater ramp ~2 °C/min from ambient, capped 80 °C) | — | 5 | Time from ramp start to Watch, Warn, Cut; pack temperature at each; IR-array lag vs contact thermistor; relay open time after the Cut decision |
| T2 Loose terminal | B sets tight or loose by coin flip, operator blind | 10 (≈5/5) | R_contact (mΩ), terminal ΔT after 10 min, time-to-flag; sensitivity/specificity; scatter of R_contact vs ΔT |
| T3 IPA vapour (5 drops on a bud) | distance 10 / 20 / 30 cm | 5 each = 15 | Detection rate, response time (s) to the gas threshold, recovery time; BME688 vs MQ-3 |
| T3b Confounders | hand sanitiser at 1 m, coffee, perfume dab (not aerosol), marker pen, food | 5 | Alarms triggered (false positives) |
| T4 False alarms | 4 h normal "charging" cycles (pack held at 40–45 °C, tight terminal), plus scheduled confounders (person walking past, hand near sensor, hot tea cup at 30 cm) | 1 × 4 h | Alarms per hour by level; confounder-caused alarms listed separately |
| T5 SoH estimation | held-out NASA cells | leave-one-cell-out | MAE in % SoH (and Ah); feature importance |
| T6 Live 18650 CC-CV curve | — | 1 charge | Curve and extracted features; no accuracy claim (no capacity label) |

Results templates:

| T1 ramp # | Start °C | Watch at (s, °C) | Warn at (s, °C) | Cut at (s, °C) | Relay open (ms) |
|---|---|---|---|---|---|
| 1–5 | | | | | |

| T2 run # | Truth (tight/loose) | R_contact (mΩ) | ΔT after 10 min (°C) | Flagged? | Time-to-flag (s) |
|---|---|---|---|---|---|
| 1–10 | | | | | |

| T3 distance | Runs | Detected | Median response (s) | Recovery (s) |
|---|---|---|---|---|
| 10 / 20 / 30 cm | 5 each | | | |

| T4 hour | Watch | Warn | Cut | Confounder-caused |
|---|---|---|---|---|
| 1–4 | | | | |

| T5 test cell | MAE % SoH | MAE Ah |
|---|---|---|
| B0005 / B0006 / B0007 / B0018 | | |

Say in the results that T1 and T3 are proxies (an aluminium block and IPA vapour), not thermal runaway or electrolyte venting, and that open-bay detection lead time for a real venting pack is unmeasured.

Safety rules: no mains wiring in the hall; adapters only; W1209 hard cut at 80 °C independent of the ESP32; never leave a heater or the 18650 unattended; 18650 only inside the bag, charge only (TP4056, 1 A default, background), abort if cell surface >45 °C or voltage outside 2.5–4.2 V on arrival; IPA away from the heater, no ignition sources; extinguisher identified before starting.

### 4. Demo script (3 min) and Deep Tech Thesis outline

Demo:
- 0:00–0:20 Hook: Noida, July 2026, a scooter catching fire while charging kills two; Karnataka logged 83 EV fires in four years, 65 blamed on "power leakage"; a Gurugram society removed 75 basement chargers.
- 0:20–1:40 Live: (a) loosen the "charger" terminal → R_contact climbs and the IR map shows a hot spot at the plug → "Warn: loose connection" while the wire is still only warm; (b) the pre-warmed dummy pack ramps → Cut: relay clicks, siren, Telegram to the "guard room", a new signed log line with its hash; (c) IPA bud near the sensor → gas channel spikes.
- 1:40–2:20 Results: latencies, 10 loose-terminal runs, false alarms per hour, SoH MAE; what this does not prove (real runaway).
- 2:20–3:00 Business and ask: societies that removed chargers; Haryana's fire-certification route; ₹6,000 per bay + ₹100/month; SAM ₹235 crore + ₹47 crore/yr; ₹2 lakh to measure real-cell detection lead time in a certified lab.

Deep Tech Thesis:
- Problem (two numbers): Karnataka recorded 83 EV fires from Jan 2020 to Nov 2024, rising from 3 to 36 a year, with 65 attributed to "power leakage" (Karnataka Legislative Council reply via convergenceindia.org, Dec 2024, snippet); India registered 14,01,861 electric two-wheelers in FY26 (Vahan via Business Standard, 1 Apr 2026). Plus Noida, July 2026: two dead.
- Why now: Haryana's amended building code (5 Jun 2026) requires 1 charger per 5 slots in group housing and lets existing complexes install with Fire Department + discom certification, with detailed fire rules being drafted; a Supreme Court PIL on society charging (Feb 2026); societies removing chargers.
- Deep-tech core: multi-modal bay sensing with sensor fusion: direct contact-resistance trending at the plug (I²R heating at normal current, invisible to MCBs and RCDs), thermal-array rate-of-rise over the pack zone, MOX VOC sensing as a venting proxy, autonomous cut-off, and a tamper-evident signed log a fire officer can accept; charging-curve state-of-health as the software layer.
- What we built and measured: the rig, the head, the log, the T1–T5 tables.
- Business: RWAs and societies (first: those that removed chargers), via the fire-certification trigger; ₹6,000 per bay + ₹100/month; SAM ₹235 crore one-time + ₹47 crore/yr (R2, assumptions).
- What ₹2 lakh over 3 months proves: (1) controlled abuse tests of real e2W cells/modules at a certified test lab (e.g. ICAT Manesar or ARAI; background, not contacted) to measure how early gas + IR see venting in an open bay, the #1 unknown; (2) a 10-bay pilot in a Gurugram/Noida society with a fire-department walkthrough; (3) a mains-side version with arc-fault current signatures, built under proper electrical certification.
- Singapore angle: Singapore made UL 2272 certification mandatory for e-scooters/PMDs after a run of PMD fires around 2019–20 (background, unsourced this round); its regulator-led approach is the template for India's pending rules; immersion goal: compare bay-safety requirements and meet the fire authority (hypothesis).

### 5. Judge-proofing

1. "You heated an aluminium block. Can you detect a real venting pack in an open bay in time?" → Not yet, and we say so: tonight proves the sensing, fusion and cut-off chain. Honeywell's Li-ion Tamer reports ~6.4 min warning, but in enclosed battery racks (vendor-reported); open-bay lead time is unmeasured, which is the first use of the grant. Our strongest claim tonight is the plug side, which is where Karnataka's tally puts most fires (65/83 "power leakage").
2. "Smart sockets (Bolt.Earth, ₹4,999) and MCB/RCDs already protect this." → An MCB trips on overcurrent and an RCD on leakage; a loose contact overheats at normal current, so neither trips. Bolt.Earth's sockets cut off on voltage faults but have no plug temperature, contact-resistance or gas sensing. We measure the contact resistance directly.
3. "RWAs pay nothing today and insurers do not care. Who buys?" → True today. The trigger is regulation: Haryana's code routes existing complexes through fire-department certification, and fire rules are being drafted; the pitch to societies like DLF Ultima is "restore the chargers you removed, under monitoring", with a log a fire officer can accept. If the rules never name monitoring, the business is weak, and we say that too.

### 6. Pre-event checklist

- Order everything by Thu 5 Nov; MLX90640 from zbotic (only in-stock seller found), with the AMG8833 as a cheap second order if budget allows.
- Written OK from the organisers for: low-voltage rig on enclosed adapters, a heater ≤80 °C with an independent cut, ≤5 drops of IPA, one 18650 charging attended in a LiPo bag; ask for an ABC or CO₂ extinguisher near the table. If refused, drop the 18650 and IPA.
- Download the NASA zip (210 MB) and CALCE CS2 data; convert .mat to Parquet; train the baseline SoH model before the event.
- Pre-build rig mechanics at the makerspace; black tape on the pack and terminal; drill or clamp the cartridge heater into the heatsink.
- Calibrate thermistors against a kitchen probe (ice water, warm water); set the three INA219 addresses.
- Buy a branded 18650; check voltage and wrapper on arrival.
- Telegram bot on a team member's own account.

### 7. Feasibility verdict

**Buildability 4/5. Safe pick.** The parts are cheap and almost all in stock, the physics is deterministic, and the demo needs no ML to work; it is the most predictable build of the four. The ceiling is capped because the overnight numbers come from proxies (a heated block, IPA vapour), not real thermal runaway. Biggest risk on the night: the venue refusing heaters, IPA or a lithium cell on safety grounds, which shrinks the demo to the loose-terminal test and dataset SoH; second, the MLX90640 not arriving (AMG8833 fallback).

---

## S2 GNSS integrity node (receive-only)

### 1. Bill of materials

Receiver decision: use two u-blox **MAX-M10S** boards (₹1,775 each, in stock) as the primary nodes. The u-blox M10 SPG 5.10 interface description (UBX-21035062 R02) includes **UBX-MON-SPAN** (a 256-bin spectrum per RF path plus the PGA gain, p.87), **UBX-MON-RF** (jammingState, agcCnt), **UBX-NAV-SAT** (per-satellite C/N0) and a **spoofDetState** field (fetched PDF, https://docs.sparkfun.com/SparkFun_u-blox_SAM-M10Q/assets/component_documentation/u-blox-M10-SPG-5.10_InterfaceDescription_UBX-21035062.pdf, 3 Nov 2026). So the cheap board carries every message the Stanford detector uses; it is L1-only, so no dual-frequency checks, and the Stanford accuracy figures (measured on F9P-class receivers) must be re-established, not quoted as ours. The ZED-F9P is an optional upgrade: the board is in stock but a multiband antenna is a HIGH delivery risk, and an F9P without one is pointless. The RTL-SDR is dropped from the must-have list: the RTL-SDR Blog V4 is end-of-life (R828D tuner stock exhausted; the V4L is the successor, search summary, snippet), the one Indian listing found is out of stock (electropi.in, ₹4,540 + GST, snippet), and MON-SPAN already gives a coarse spectrum.

Pre-order:

| Item | Qty | Listing | Unit ₹ | Line ₹ | Stock 3 Nov / risk |
|---|---|---|---|---|---|
| u-blox MAX-M10S breakout, SMA connector, UART/I2C (SmartElex) | 2 | https://robocraze.com/products/smartelex-u-blox-max-m10s-gnss-module-breakout | 1,775 | 3,550 | In stock; low. Alt: 7Semi MAX-M10S ₹1,976 https://robocraze.com/products/7semi-max-m10s-gnss-receiver-breakout-industrial-grade-positioning-module |
| Active L1 GPS antenna, 28 dB LNA, 3–5 V, SMA male, 3 m cable | 2 | https://www.electronicscomp.com/1575-mhz-gps-antenna-for-gps-and-gsm-module-with-3-meter-cable-good-quality | 447 (379 + 18% GST) | 894 | In stock (114 units); low. Check the breakout feeds antenna bias (VCC_RF): NOT VERIFIED from the listing |
| CP2102 USB-UART adapter | 2 | https://robocraze.com/products/cp2102-usb-2-0-to-ttl-uart-serial-converter-module | 135 | 270 | In stock (or kit) |
| **Primary subtotal** | | | | **4,714** | |

Optional upgrade (only if the antenna is confirmed in stock):

| Item | Listing | ₹ | Risk |
|---|---|---|---|
| ZED-F9P L1/L2 board, U.FL (SmartElex) | https://robocraze.com/products/smartelex-gps-rtk-board-ufl-zed-f9p-04b | 17,965 | In stock; low. 7Semi SMA version ₹20,489 https://robocraze.com/products/u-blox-zed-f9p-dual-band-gnss-rtk-sma-modem-7semi |
| Multiband L1/L2 magnetic-mount antenna (SparkFun, via Tanotis) | https://tanotis.com/products/sparkfun-gnss-multi-band-magnetic-mount-antenna-5m-sma | 9,135 incl. import duties (snippet) | **HIGH** (import, stock and lead time not shown); zbotic Holybro RTK antennas ₹2,731–10,999 all out of stock |
| SMA–U.FL pigtail 20 cm | https://robocraze.com/products/sma-to-u-fl-cable-20cm | 57 | Low |

Kit / own: 2 ESP32 boards (UART → Wi-Fi bridge so the rooftop node needs no laptop beside it), 2 × 10,000 mAh power banks, weatherproof box or zip bags and cable ties (~₹300 est.), aluminium foil and a steel pot (blockage tests), a laptop with Ubuntu 22.04/24.04 or WSL2 and ≥200 GB free (or an external SSD) for TEXBAT segments.

**Total ≈ ₹5,000** (₹4,714 verified + ~₹300 estimates); **≈ ₹32,200 with the F9P upgrade** (+₹27,157).

TEXBAT and GNSS-SDR facts (checked 3 Nov 2026 with curl, since WebFetch could not resolve the host):
- Raw files are huge: cleanStatic 45 GB, cleanDynamic 41 GB, ds1–ds4 43 GB each, ds5–ds6 39 GB, ds7–ds8 44 GB, plus a short **cleanStatic80.bin of 8,016,392,192 bytes (7.5 GiB)** (https://rnl-data.ae.utexas.edu/datastore/texbat/, directory listing). The server supports HTTP byte ranges (`Accept-Ranges: bytes`; ds1.bin = 46,170,898,432 bytes), so a time window can be downloaded without the whole file.
- Format: IQ rate 25 MHz, centre 1575.42 MHz (ds1.xml). cleanStatic80 = 80.2 s and ds7 = 468 s at 4 bytes per complex sample (16-bit I + 16-bit Q), i.e. **100 MB per second of recording** (my arithmetic from file sizes and the ds7 timeline). GNSS-SDR's matching input type is probably `ishort` (interleaved int16; background); confirm on cleanStatic80 before the event.
- **Processed observables already exist** for cleanStatic, ds2, ds3 and ds7 (UT's GRID receiver): channel.mat 3.3–3.4 MB (per-channel C/N0 in dB-Hz, Doppler, pseudorange, carrier phase, a "spoofing detected" error bit, transmitter ID), navsol.mat ~197 KB, txinfo.mat ~1.7 MB, in-band power at 2/4/8 MHz (~24 KB each), iq.mat ~83 MB, iqtaps.mat ~650 MB (https://rnl-data.ae.utexas.edu/datastore/texbat/processed/; column definitions in https://rnl-data.ae.utexas.edu/datastore/satNavCourse/logFileDocumentation/channeldef.txt). No processed set for ds1, ds4, ds5, ds6, ds8.
- ds7 ground truth (texbat_ds7_and_ds8.pdf in the same directory): clean 0–110 s; spoofer injected and carrier-aligned 110–130 s; 130–150 s observables "not significantly different" from clean; 150–468 s code-phase push at 1.2 m/s, reaching 381.6 m (1.273 µs clock offset) at 468 s. Onset times for ds1–ds6: NOT RE-READ; read them off the processed data or Humphreys et al. 2012.
- Licence: free for research, "refrain from distributing" (TEXBAT page). Over 130 users have downloaded it as of Feb 2025 (same page).
- GNSS-SDR install: `sudo apt install gnss-sdr` (Debian 9+/Ubuntu 16.04+), Docker image `carlesfernandez/docker-gnsssdr`, MacPorts `sudo port install gnss-sdr`; packaged versions lag the source (https://gnss-sdr.org/build-and-install/, fetched 3 Nov 2026). Install effort is low; processing 25 Msps files on a laptop is the slow part.
- Consequence for R2's wedge: "TEXBAT replay through GNSS-SDR" means 40+ GB per scenario. The realistic overnight route is (a) the detector on UT's processed observables for ds2, ds3, ds7 (~5 MB each), (b) GNSS-SDR on the 8 GB cleanStatic80 clip with jamming added digitally, and (c) raw ds scenarios only for byte ranges downloaded before the event.

Detector (the deep-tech core): 1 Hz features per node: SBAS C/N0 (India's SBAS is GAGAN; PRNs 127/128/132, background, verify via NAV-SAT svId), median and spread of GPS C/N0 across satellites, received-power proxy = MON-SPAN integrated in-band power corrected for PGA gain (the Stanford approach, arXiv 2509.13600v2), MON-RF agcCnt and jammingState, NAV-STATUS spoofDetState, position residual vs the node's surveyed static position, receiver-clock residual vs a linear fit of the clean period. States: OK / BLOCKED (C/N0 down, power flat or down) / JAM (power up, C/N0 down) / SPOOF-SUSPECT (position or clock residual beyond threshold, or a power step with uniform C/N0). Calibrate on 30–60 min of clean data. Two nodes 10–20 m apart vote: both flag = area event; one flags = local (e.g. foil). Expected ds7 catch by the clock check: push starts at 150 s at 1.2 m/s, so a 20 m threshold trips at ~167 s, ~57 s after injection (my arithmetic; depends on the clock-noise floor in the processed data).

### 2. Hour-by-hour plan

Roles: HW1 = node A and rooftop mounting; HW2 = node B and blockage tests; C1 = detector + TEXBAT + synthetic jamming; C2 = UBX logging, dashboard, alerts; B = timekeeper, interaction log, thesis (no bio role here). For 4 people, B's tasks go to HW2.

| Time | HW1 / HW2 | C1 | C2 | B |
|---|---|---|---|---|
| 18:00–19:00 | Mount nodes A and B with open sky, 10–20 m apart (permission arranged beforehand); power banks; ESP32 UART→Wi-Fi bridges | Load pre-downloaded TEXBAT processed .mat files (scipy.io); plot C/N0, power, navsol for cleanStatic and ds2 | Enable UBX messages on both M10s (NAV-SAT, NAV-PVT, NAV-STATUS, NAV-CLOCK, MON-RF, MON-SPAN at 1 Hz) with pyubx2; log to Parquet | Starts the interaction log (every time anyone touches a node) |
| 19:00–20:00 | Leave nodes untouched | Detector code | Live plots | |
| 20:00 | **Freeze thresholds** after ≥45 min of clean calibration; surveyed position = 45-min mean; write config hash; **start the 10-h nominal clock (20:00–06:00)** | | | |
| 20:00–23:00 | HW2: scheduled foil/pot blockages on node B (logged windows) | Detector on TEXBAT cleanStatic (false alarms), ds2, ds3 → latency table | Dashboard: two-node map, state badges, MON-SPAN waterfall, C/N0 sky plot; Telegram alerts | Logs blockage windows to the second |
| 23:00–02:00 | More blockage trials (full and partial cover) | Synthetic jamming: add CW, band-limited noise and chirp to cleanStatic80 IQ in numpy at 5 jam-to-noise levels → GNSS-SDR → C/N0 + in-band power → detector. If GNSS-SDR stalls, compute in-band power from IQ directly and mark C/N0 as unmeasured | Alert de-duplication; event export | |
| **02:00 milestone** | Dashboard shows both live nodes; foil on node B labelled BLOCKED (not JAM) while node A stays OK; TEXBAT ds2 labelled SPOOF-SUSPECT with a latency; Telegram alert fires. Record the backup video. | | | |
| 02:00–06:00 | Nodes untouched except scheduled trials; sleep in shifts | ds7 run; jamming sweep finished; optional raw ds2/ds7 window through GNSS-SDR if pre-downloaded | Results export | Keeps the log |
| 06:00 | **Stop the 10-h clock**; count unlabelled alarm events | | | |
| 06:00–10:00 | All: analysis, thesis, rehearsal, second backup video | | | |
| 10:00–12:00 | Pitch window / buffer | | | |

Cut-down fallbacks:
- No rooftop → window ledge or balcony with the widest sky view; recalibrate and report the lower C/N0.
- One receiver dead → single live node + TEXBAT (no cross-node vote).
- No receivers arrive → software-only demo on TEXBAT processed data and cleanStatic80 (say so).
- GNSS-SDR fails on raw data → processed observables only; synthetic jamming shown on power only.

### 3. Test protocol

| Test | Data | Trials | Measure and report |
|---|---|---|---|
| T1 False alarms, nominal | Live nodes A and B, 20:00–06:00 (~36,000 epochs per node at 1 Hz), minus logged test windows | 2 nodes × 10 h | Alarm events per hour by state (contiguous flagged epochs merged into one event); also false alarms on TEXBAT cleanStatic |
| T2 Spoofing detection latency | TEXBAT ds2, ds3, ds7 (processed); others only if raw windows were run | 1 run each | Onset (s), first alarm (s), latency (s), which feature fired, missed (Y/N) |
| T3 Blockage vs jamming separation | 10 live foil/pot blockages on node B (full and partial) + synthetic jamming (CW, noise, chirp × 5 levels = 15) | 25 | Confusion matrix OK / BLOCKED / JAM; label accuracy |
| T4 Local vs area | Node A during node B blockages | 10 | Node A stayed OK (yes/no) |

Results templates:

| T1 node | Hours | OK→BLOCKED events | OK→JAM events | OK→SPOOF events | Events/hour |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| TEXBAT cleanStatic | 0.13 | | | | |

| T2 scenario | Type (per TEXBAT) | Onset (s) | First alarm (s) | Latency (s) | Feature | Missed? |
|---|---|---|---|---|---|---|
| ds2 | overpowered time push | | | | | |
| ds3 | matched-power time push | | | | | |
| ds7 | matched-power, carrier-aligned time push | 110 | | | | |

| T3 truth \ predicted | OK | BLOCKED | JAM |
|---|---|---|---|
| Blockage (10) | | | |
| Synthetic jam (15) | | | |

Benchmark to quote: on Jammertest 2024 the F9P method flagged interference with ≥99.5% accuracy, classified jamming at ~95–99%, but classified spoofing at only 53–67% with SBAS and near 0% with GPS signals (arXiv 2509.13600v2, Tables 3–4, R2 fetched). Say openly that cheap receivers detect interference well and spoofing poorly, and that our M10 numbers are our own calibration, not the paper's.

Safety and legal: receive-only hardware only; nothing is radiated; no HackRF, Pluto or signal generators; all jamming is added in software to recorded IQ; TEXBAT is not redistributed (keep it off shared drives); rooftop work only with permission and a buddy, never alone at night.

### 4. Demo script (3 min) and Deep Tech Thesis outline

Demo:
- 0:00–0:20 Hook: "Pilots reported 2,354 GNSS interference incidents between Nov 2023 and Dec 2025, and 623 more in Delhi airspace in two months this year. Over 10% of Delhi-region flights have reported spoofing. No ground sensor in India records the RF."
- 0:20–1:30 Live: dashboard with two rooftop nodes. A teammate wraps node B's antenna in foil: BLOCKED, not JAM, and node A stays OK, so the system calls it a local event. Then replay TEXBAT ds2: state flips to SPOOF-SUSPECT at t = X s with the clock residual climbing; then a synthetic-jam clip: JAM, with the MON-SPAN waterfall lighting up.
- 1:30–2:20 Results: false alarms over 10 h, the latency table including ds7 (caught late or missed), blockage-vs-jam confusion matrix; the honest line about spoofing.
- 2:20–3:00 Business and ask: a ~₹5k M10 node (₹60–80k F9P class) sold at ₹2.5 lakh vs a DYLEMA-class system costing "millions of euros"; first buyer a private airport operator or AAI; then telecom/power timing and defence; ₹2 lakh for a six-node pilot.

Deep Tech Thesis:
- Problem (two numbers): 2,354 GNSS interference incidents Nov 2023–Dec 2025, plus 623 in Delhi airspace in Jan–Feb 2026 (Lok Sabha reply, IANS via NewKerala, 12 Mar 2026); more than 10% of Delhi-region flights reported spoofing (Secure World Foundation 2026 via Inside GNSS, 8 Apr 2026).
- Why now: DGCA's 10-minute reporting SOP (10 Nov 2025) turned pilot memory into a report stream with no RF evidence behind it; IATA names India a new hotspot; ₹1,775 receivers now expose spectrum (MON-SPAN) and AGC data; the Stanford low-cost detection method was published in 2025–26.
- Deep-tech core: a calibrated multi-feature integrity detector (SBAS C/N0 × received power × position/clock consistency of a surveyed static node) and multi-node voting that separates blockage, jamming and spoofing.
- What we built and measured: two live nodes, the dashboard, T1–T4.
- Business: AAI and private airport operators first; ₹2.5 lakh per node + ₹60k/yr service (R2 assumptions); SAM only ~₹1.6 crore + ₹38 lakh/yr for the 8 named airports, so the venture case rests on timing infrastructure (telecom, power, banking), defence and export.
- What ₹2 lakh over 3 months proves: a six-node M10 network (~₹30k hardware) around one airport perimeter or the campus, with permissions; three months of GAGAN-calibrated baselines; validation on public Jammertest data or by taking part; an RTI on AAI/WMO ground monitoring; one letter of intent.
- Singapore angle: Changi is a regional hub and GNSS interference over the surrounding seas is reported by aviation bodies (background, not verified this round); the immersion goal is to compare Delhi and Singapore interference signatures and meet the aviation regulator's navigation team (hypothesis).

### 5. Judge-proofing

1. "Cheap receivers classify spoofing at only 53–67% (SBAS) and near 0% (GPS); your node cannot catch spoofing." → Correct for a receiver that does not know where it is. A fixed node knows its surveyed position and has a stable clock model, so position and clock jumps are strong spoofing tells; our TEXBAT table shows which scenarios we catch and how late (ds7, carrier-aligned, is the hardest). The core value is interference and jamming evidence (≥99.5% detection in the same study), which is what most pilot reports describe.
2. "GPSJam and ADS-B maps already show this for free." → They are aircraft-derived, aggregated in 24-hour hexes, do not separate spoofing from jamming, go blind where no aircraft fly, and record no RF. A ground node gives time-stamped spectra and states that the Wireless Monitoring Organisation can use to find a source. Complementary, not competing.
3. "Who buys? Your SAM is ₹2 crore." → Agreed, domestic civil aviation alone is small and slow. The path is private airport operators, then GNSS-timing users (telecom, power-grid PMUs, banks), then defence and export. On legality: the kit is receive-only; whether GNSS modules fall under the Rule 10 exemption of the 2026 Radio Equipment Possession Authorisation Rules is NOT CONFIRMED (R2 unknown), so we would apply for authorisation for any field network.

### 6. Pre-event checklist

- Order 2 × MAX-M10S + 2 antennas + 2 CP2102 by Thu 5 Nov; F9P only if a multiband antenna is confirmed in stock.
- Download before the event on a fast connection: TEXBAT processed folders for cleanStatic, ds2, ds3, ds7 (channel, navsol, txinfo and power .mat files, ~25 MB in total; iq.mat optional, ~83 MB each); cleanStatic80.bin (8.0 GB); if bandwidth allows, byte-range windows of raw ds2 and ds7 around the onset (e.g. 90–200 s ≈ 11 GB each, using `curl -r`). Check the md5 files for any full download.
- Install GNSS-SDR (apt or Docker) and get a position fix from cleanStatic80 before the event. This is the go/no-go for the raw-IQ path.
- Script and test pyubx2 configuration of the M10 (CFG-VALSET message rates incl. MON-SPAN) at home; confirm the breakout powers the active antenna.
- Run a 24-hour home baseline on 11–12 Nov: sets thresholds, confirms GAGAN satellites are tracked, gives a second false-alarm dataset.
- Written permission from Ashoka facilities/security for rooftop or terrace access on the night of 13–14 Nov (or pick a window with open sky).
- Telegram bot on a team member's own account.
- A one-paragraph note for the organisers: receive-only, nothing transmitted, no jammers.

### 7. Feasibility verdict

**Buildability 3/5. High-ceiling pick.** The strongest deep-tech story of the four and cheap, in-stock receivers; the processed TEXBAT observables make the replay result near-certain. Live logging needs open sky and a 10-hour untouched run, the raw-IQ path through GNSS-SDR is slow, and the spoofing numbers may be poor (that is the published state of the art). The market is the weakest of the four. Biggest risk on the night: no open-sky mounting (permission or weather), which degrades C/N0 and inflates false alarms; second, GNSS-SDR not reaching a fix on the raw clip in time.

---

## NOT CHECKED

- Delivery times from Robocraze, zbotic, electronicscomp and Probots to Sonipat; whether robotools/ibots can actually ship the AS7265x by 7 Nov.
- Contents of the event kits (ESP32-S3, speakers, MQ sensors, power banks, hot plate, multimeters, 3D printers).
- Amazon.in prices and stock for any part (Amazon pages were not fetched); robu.in prices (catalogue API returned 403).
- Raspberry Pi 5 board price and stock in India.
- Whether the SmartElex MAX-M10S breakout supplies antenna bias (VCC_RF) for an active antenna.
- GAGAN PRN numbers and their visibility from Sonipat; TEXBAT ds1–ds6 onset times; the GNSS-SDR `item_type` for TEXBAT.
- IndicWhisper availability as a faster-whisper/CTranslate2 model; actual faster-whisper Hindi latency on the team's laptop; ESP-SR language support beyond a vendor blog.
- Real separation of white OTC tablets by AS7343/AS7341 (needs the bench test); Hamamatsu C12880MA price.
- Prices of ferric chloride, the tablet library, IPA, a branded 18650, speakers, enclosures (all estimates).
- The ibuprofen Schedule H strength threshold; the Schedule K status of paracetamol.
- Organiser rules on heaters, lithium cells, chemicals and wet work in the hall; rooftop access at Ashoka.
- Rule 10 exemption text of the 2026 Radio Equipment Possession Authorisation Rules (left to the claims agent).
- Singapore angles (ScamShield figures come from R2 snippets; HSA, UL 2272 for PMDs, regional GNSS interference are background only).
- The arXiv 2509.13600v2 benchmark figures were not re-opened this round (carried from R2, which fetched them).

Searches used: 20

