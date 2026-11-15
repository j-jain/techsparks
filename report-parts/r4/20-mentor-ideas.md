## 3. Ideas read from the mentors' records

These four come from what the mentors' funds have already paid for. Each was designed in detail by one agent and its key facts were attacked by another. Two of the four shrank under that scrutiny; the cards say so.

### M3 · Solder and placement inspector for small electronics assemblers

*Buildable overnight 5/5 · Business 3/5 · AI/ML about 60% · Track: Frontier Hardware*

- **The problem.** India made electronics worth Rs 13.11 lakh crore in 2025–26 ([MeitY figures, 24 Jul 2026](https://www.bisinfotech.com/india-electronics-manufacturing-reaches-13-11-lakh-crore-milestone/)). Big plants check boards with automatic optical inspection machines that cost about Rs 50–60 lakh (trade listings, snippet). Small assemblers cannot buy one, so a person checks each board by eye under a lamp, and faults reach the customer.
- **Who pays.** The owner of a 20–200 person assembly unit. Today the cost is one to three inspectors plus rework and returns. A plausible price is Rs 30,000 for the station and Rs 1,500 a month. With about 4,000 such sites (assumption), that is roughly Rs 7 crore a year of recurring revenue: real, but small.
- **How it works.**
  1. A fixed jig, an overhead camera and a ring light photograph each board.
  2. The image is aligned to a photo of a known-good board.
  3. The board's pick-and-place file says where each part should be, so the software cuts out one small image per part.
  4. Each cut-out gets three checks: an anomaly score against good boards, a solder-fault detector, and a polarity check.
  5. The screen shows red boxes and a pass or fail.
- **The AI/ML core.**
  - Anomaly detection with PatchCore (Intel's open `anomalib` library). It trains only on photos of good boards, so a shop needs 20–50 good photos and no fault labels.
  - A YOLO detector fine-tuned on SolDef_AI, an open set of solder-fault images, to name the fault.
  - Round 1 pointed at the well-known PCB datasets. The design agent found those cover bare boards before assembly and cannot teach solder or placement faults.
  - What one top-down camera cannot see: joint height, joints hidden under chips, slightly lifted leads. It catches missing, wrong, shifted or reversed parts, solder bridges and gross solder faults.
- **Why India needs its own version.** Price is 100 times lower than a machine. Small Indian shops run many board types in small batches, which suits learning from good boards better than a day of rule-writing per board. The operator screen should be in Hindi with pictures.
- **Funded analogue.** SixSense, in Peak XV's Surge 11 cohort, sells no-code vision inspection to chip plants ([Inc42, 25 Sep 2025](https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11)). This idea keeps the method and changes the line, the price and the training.
- **Who has tried.** SwitchOn raised $8 million in July 2026 ([Entrepreneur India](https://india.entrepreneur.com/business-news/switchon-raises-78-crore-in-pre-series-b-round-led-by-ivycap-ventures)) and Frinks AI raised $5.4 million in May 2025 ([Tribune](https://www.tribuneindia.com/news/business/frinks-ai-a-manufacturing-ai-startup-by-iit-hyderabad-alumni-raises-5-4m-led-by-prime-ventures)). Both sell to larger plants. Nobody was found selling a station under Rs 50,000.
- **What you could show by noon.** Solder 20 cheap through-hole kits: 10 good, 10 with one planted fault each (bridge, missing resistor, reversed LED, reversed capacitor, cold joint). Train on 30 photos of good boards only. **The number:** faults caught on the 10 faulty boards and false alarms on the 10 good ones, each board photographed three times after being put back in the jig (60 images). Compare with simple pixel differencing, and with a teammate inspecting each board for 30 seconds.
- **Parts and cost.** A webcam or USB microscope camera (Rs 1,500–3,500), a ring light (Rs 400), kits (about Rs 2,000). About Rs 4,000–6,000 in all (estimates).
- **The hard question.** "One flat camera misses half of solder defects. Is this a toy?" It misses joint-shape and hidden-joint faults. It replaces the eye-and-lamp check, not the Rs 50 lakh machine, and the pitch should say exactly that.
- **Suits.** Vibhore Sharma (his one public quote is about manufacturing; his funds back CynLr and Unbox Robotics). Anuj Mehta (student-built hardware plus applied AI). Arshia Mal (WTFund backed a desktop pick-and-place machine).
- **Overlap with your own work.** Same technique as your factory CCTV idea, in a different sector.

### M1 · Phone-on-microscope slide reader for malaria

*Buildable overnight 3/5 · Business 2/5 · AI/ML about 75% · Track: Bio & Health*

- **The problem.** India runs about 18 crore malaria tests a year and finds about 2.6 lakh positives, roughly one in 700 ([national programme report, Dec 2024](https://ncvbdc.mohfw.gov.in/Doc/MMIS/2024/MMIS-Report-Country-Dec-2024.pdf); [ORF, 14 Oct 2025](https://www.orfonline.org/expert-speak/more-tests-fewer-cases-tracking-india-s-fight-against-malaria)). The count mixes microscope slides and rapid tests, and the split is not published. A technician who sees one positive in hundreds of slides will miss some. In August 2026 the Health Ministry also asked states to look into unusually high examination rates for duplicate entries ([ThePrint/PTI](https://theprint.in/india/india-sees-nearly-80-pc-decline-in-malaria-cases-deaths-between-2015-2025-health-ministry/3027841/)). So the programme has two needs: catch the rare positive, and prove a slide was really read.
- **The idea.** A phone clamped to the eyepiece of the lab's existing microscope. It photographs 10–20 fields, marks the objects that look like parasites, and shows them as thumbnails for the technician to confirm or reject. It keeps a dated photo record of every slide. The technician still makes the diagnosis.
- **Who pays.** The state malaria programme, through National Health Mission funds. Indian malaria alone is worth perhaps Rs 10–15 crore a year (the designer's estimate, on assumed slide counts). That is too small for a company, so it is a starting point. The same rig could read ordinary blood smears for small private labs, or serve African malaria programmes.
- **The AI/ML core.**
  - Stage one: a small object detector (YOLO11n) finds white cells and parasite candidates. Stage two: a small classifier (EfficientNet-B0) throws out look-alikes such as platelets and stain debris.
  - Data is free from the US National Library of Medicine: thick smears from 150 falciparum patients (1,819 phone photos, 84,961 marked parasites), 150 vivax patients and 50 uninfected patients ([dataset page](https://lhncbc.nlm.nih.gov/LHC-research/LHC-projects/image-processing/malaria-datasheet.html)).
  - Published result on phone photos: 82.7% sensitivity and 98.4% specificity per image patch on 30 held-out patients ([Yang et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077747/)). The slides were from Bangladesh. No India-validated figure exists.
  - Why a human must confirm: at one positive in 700, even a 2% false-alarm rate per slide gives about 14 false alarms for every true case.
  - It cannot tell the two species apart on thick smears, find very faint infections, or read a stain or microscope it has not seen.
- **Why malaria first.** TB smear reading is being replaced by molecular tests under national policy. Cervical-cancer slides have no open Indian supply. Anaemia typing is already done by analysers.
- **Who has tried.** SigTuple sells bench analysers for blood-cell counts, with no malaria claim ([BioSpectrum, 24 Feb 2026](https://www.biospectrumindia.com/news/100/27380/sigtuple-announces-launch-of-ai-enabled-digital-morphology-analyser.html)). Morphle sells slide scanners and raised $5 million in November 2025 ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/inflexor-ventures-leads-usd-5-mn-funding-in-healthtech/500036)). Turocrates AI, from WTFund's latest cohort, describes itself only as an "OS for precision diagnostics". None sells a phone-on-microscope malaria checker to a public programme.
- **What you could show by noon.** Train on the public images, splitting by patient so no patient is in both training and test. **The number:** sensitivity and specificity per patient on 30 infected and 20 uninfected held-out patients, with the uncertainty range stated (it will be wide). If the biology lab has a microscope with a 100x oil lens, add a second number: false alarms on your own phone photos of known-negative slides. That shows honestly how much accuracy drops on a new microscope.
- **Parts and cost.** Borrowed microscope and phone, a 3D-printed clamp, slides and stain. Under Rs 500.
- **The hard question.** "Your model learned from Bangladeshi slides. Why would it work in Bastar?" It will not without retraining. The plan starts with a 2,000-slide re-read study in one district.
- **Suits.** Shilpy Kochhar (a diagnostic with a BIRAC grant route). Arshia Mal (WTFund backed a pathology-slide device). Karthik Varada (a health outcome).

### M4 · Acoustic leak finder for water pipes (survives only in a smaller form)

*Buildable overnight 4/5 · Business 2/5 · AI/ML about 50% · Track: Frontier Hardware & Climate*

- **The problem.** Indian city water utilities lose an average of 38% of treated water before it is billed ([ORF citing NIUA, 24 Aug 2025](https://www.orfonline.org/expert-speak/the-cost-of-leakage-how-water-losses-fuel-unsustainable-choices)). Leaks are found by crews with listening rods, or by digging.
- **Funded analogue.** Puralink, a Sydney company in Peak XV's Surge programme, builds robots that travel inside pipes ([Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/puralink-dredges-up-2-3m-seed-round-for-autonomous-pipe-robot/)). In India, Solinas Integrity does similar work and raised $5.5 million in August 2026 ([Inc42](https://inc42.com/?p=567452)).
- **The idea.** Skip the robot. A "listening stick" (a piezo disc or accelerometer on a rod) is touched to a valve or hydrant for ten seconds. A phone records the sound, a model labels it leak, tap use, pump or traffic, and each point lands on a map.
- **The AI/ML core.** Convert each clip to a spectrogram, pass it through a pretrained audio model (YAMNet or PANNs) and train a small classifier on top. A free dataset exists: 280 thirty-second recordings from a 47-metre PVC test rig with four leak types (Aghashahi and others, *Data in Brief*, 2023). Published field accuracy is over 99% on metal pipes and about 89% on plastic (snippet).
- **Why the city-wide version fails in India.**
  - Supply is intermittent. Mumbai averaged 5.4 hours of water a day in 2024 (Praja Foundation, snippet). An empty pipe makes no leak noise.
  - During supply hours, household suction pumps on the main add noise. No published method handles that.
  - In plastic pipe the sound dies within metres, so a survey would need a listening point every 20–50 metres.
- **What survives.** A survey tool for metal trunk mains and for private networks: campuses, townships, industrial estates. These pay faster than municipalities too.
- **What you could show by noon.** Three to four metres of PVC pipe on a lab tap, with a 1.5 mm drilled hole and a screw plug. Record with the plug in and out, at four distances, with and without a small pump running. **The number:** leak-or-not accuracy on about 120 clips, split by recording session, shown against distance. Compare with a simple loudness threshold. Say plainly that this is a lab rig.
- **Parts and cost.** Pipe, fittings, a USB sound card, piezo discs, a small pump. About Rs 1,300.
- **The hard question.** "Your pipes are empty most of the day and noisy the rest. How does this work at all?" Only in the supply window, and only once the model has heard Indian pump noise, which nobody has recorded yet.
- **Suits.** Karthik Varada (a resource outcome in litres). Vibhore Sharma (a sensor feeding a model).

### M2 · Hinglish clinic scribe (did not survive; a smaller piece does)

*Buildable overnight 4/5 · Business 2/5 · AI/ML about 80% · Track: AI & Systems*

- **Where it started.** Freed, backed by Sequoia, writes the clinical note from a recording of the visit and serves over 17,000 clinicians ([Sequoia, 5 Mar 2025](https://sequoiacap.com/article/partnering-with-freed-an-ai-powered-clinicians-assistant)). The Indian case looked strong: one study of government speciality clinics in Patna found about two minutes per patient and over 200 patients a day ([IJCMPH](https://www.ijcmph.com/index.php/ijcmph/article/view/5276); one hospital, not a national figure).
- **Why it failed.** Eka Care already does it. EkaScribe writes prescriptions as well as notes, works in Hindi and many other languages, has a free tier, and costs about $20–25 a month (snippet). Eka is also building an offline version with NVIDIA ([Digital Health News](https://www.digitalhealthnews.com/eka-care-nvidia-partner-to-develop-offline-multilingual-ai-medical-scribe-for-india)). Round 1's claim that solo clinics were an open gap did not hold.
- **What survives.** The error that matters in a scribe is a wrong drug or dose on a printed prescription, and no vendor publishes that figure for mixed Hindi-English speech. A **drug-and-dose checker** would match what was heard against a list of Indian brand names and force the doctor to confirm anything uncertain. It could be sold as a component to scribe makers.
- **What you could show by noon.** Record 30 staged consultations using 60 real brand names, half with clinic noise playing. **The number:** the share of prescription lines where drug, strength, dose, frequency and duration are all correct, with and without the brand-name matcher. Eka has published a test set of medical speech (3,619 English and 320 Hindi clips) that can serve as a second check.
- **The hard question.** "Eka has a free tier. Why you?" On the full scribe, no reason. Only the measured drug-line accuracy is new.
- **Suits.** Shilpy Kochhar (health delivery). Vibhore Sharma (Capital 2B is an investor in the voice-AI company Ringg).
