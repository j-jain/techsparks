# R5-design-01  (agent: Opus, date 2026-11-12)

Method. Problem proof is reused from R4-04 and R4-05 with their URLs. New facts come from pages opened on 12 Nov 2026 unless marked "(snippet)". Lines marked ASSUMPTION are the agent's own working numbers, not sourced facts. Prices for local parts are estimates and are not checked.

---

## M1 Phone-on-microscope AI slide reader (malaria blood smears first)

### 1. The problem in one paragraph
India tests a very large number of blood samples for malaria and finds very few positives. In 2024 the programme ran **181.65 million tests and found 2,55,500 positives, a test positivity rate of 0.14%**. In 2016 it was 0.87%. Testing rose about 45% over the period while cases fell (ORF table built from NCVBDC data, 14 Oct 2025, https://www.orfonline.org/expert-speak/more-tests-fewer-cases-tracking-india-s-fight-against-malaria). NCVBDC's own table counts **12.24 crore blood slide examinations in 2017 (provisional)**, so microscopy, not only rapid tests, makes up most of that volume (https://ncvbdc.mohfw.gov.in/index4.php?lang=1&level=0&linkid=564&lid=3867, opened 12 Nov 2026). On 28 Aug 2026 the Health Ministry reported an 80% fall in cases and deaths from 2015 to 2025. It also asked states to look into unusually high blood-examination rates for duplicate tests and repeated entries (ThePrint/PTI, https://theprint.in/india/india-sees-nearly-80-pc-decline-in-malaria-cases-deaths-between-2015-2025-health-ministry/3027841/). Two pains follow. A microscopist now finds about one positive in every 700 slides, which is the condition under which people miss rare events. And the programme cannot easily prove that a slide was actually read. Elimination by 2030 rests on both.

### 2. How the system works
```
Giemsa/JSB-stained thick smear -> teaching or PHC microscope, 100x oil
   -> phone in a 3D-printed eyepiece clamp -> app captures 10-20 fields
   -> on-phone detector: WBCs + parasite candidates per field
   -> candidate classifier -> parasites per 200 WBC -> parasites/uL estimate
   -> screen: "Possible positive: 7 candidates" + thumbnail gallery
   -> technician taps confirm / reject on each thumbnail (about 10 s)
   -> record: slide ID, field photos, timestamp, AI count, human call
   -> syncs when online to a district QA dashboard
```
The technician still makes the diagnosis. The AI does two jobs. It puts the few suspicious objects in front of the reader, and it re-reads every slide the reader called negative, flagging disagreements for cross-check. It also leaves a photo record proving the slide was examined, which answers the ministry's duplicate-entry worry.

### 3. The AI/ML core
- **Model family.** A two-stage detector, the same shape as the published NLM pipeline. Stage 1 is a one-stage object detector (Ultralytics **YOLO11n or YOLOv8n**) on 640-px tiles, with two classes: WBC and parasite candidate. Stage 2 is a small patch classifier (**timm EfficientNet-B0 or MobileNetV3**, 64x64 crops) that removes false candidates such as platelets, stain debris and dust. Parasite density comes from counting against WBCs, as in WHO practice. Export to TFLite or ONNX for the phone. Detection is preferred over whole-image classification because a positive slide may hold only a handful of parasites in thousands of cells.
- **Data (all free, NLM, https://lhncbc.nlm.nih.gov/LHC-research/LHC-projects/image-processing/malaria-datasheet.html, opened 12 Nov 2026):**
  - Thick smears, *P. falciparum*: 150 patients, 1,819 phone images (3024x4032), **84,961 annotated parasites**, from Chittagong Medical College Hospital, Bangladesh.
  - Thick smears, *P. vivax*: 150 patients.
  - Thick smears, uninfected: 50 patients.
  - Thin smears: 193 patients, plus the single-cell crop set (`cell_images.zip`, also on TensorFlow Datasets and Kaggle).
  - The vivax set matters because India carries both species.
  - Indian data would come from slides re-read in a pilot with an ICMR-NIMR or state reference lab. None is public.
- **Published accuracy.** Yang et al., IEEE JBHI 2020 (PMC12077747, opened). Phone-captured thick smears, custom CNN plus a classical candidate screen. On 30 held-out patients at patch level: **sensitivity 82.73%, specificity 98.39%**, AUC 97.34%. Five-fold cross-validation gave 92.59% and 94.33%. The patient-level parasite count correlated with expert counts at R = 0.99. Inference took about 10 s per image on a Galaxy S6. A patient-level field study of the Malaria Screener app ran on 190 patients in Sudan (Malar J 2023, PubMed 36707822). Its sensitivity and specificity could not be retrieved (NOT CHECKED).
- **What it cannot do.**
  - Separate Pf from Pv reliably on thick smears. Species needs thin films.
  - Detect very low parasitaemia, where only one or two parasites appear across 100 fields.
  - Read a stain, microscope or phone it has not seen. Domain shift is the main technical risk, and India's JSB stain differs from the Giemsa in the dataset (JSB use NOT CHECKED).
  - Replace the legal diagnosis.
  - Specificity is the binding number. At 0.14% positivity, even a 2% false-flag rate per slide means about 14 false flags for every true positive. That is why the design has a human confirm thumbnails rather than letting the AI call slides.

### 4. Why India needs its own version
- **Price.** The capital item is the phone the technician already owns, plus a clamp under Rs 1,000. Slide scanners (Morphle) and analysers (SigTuple) are lab capital purchases.
- **Connectivity.** PHC labs need on-device inference and sync later.
- **Data.** The India product has to handle vivax, JSB stain and Indian microscopes, and none of these is in a public set.
- **Regulation.** Software that informs a diagnosis is a medical device under CDSCO's Medical Devices Rules 2017. A pilot run as "decision support, human confirms" inside a programme study is the realistic route (classification NOT CHECKED).
- **Buyer.** The state NHM vector-borne programme and NCVBDC, paid as QA per slide or per lab, and private chains that run public-private partnership labs. Not patients.

### 5. Who has tried, and the gap
- **SigTuple** (Bengaluru). Its AI100 with Shonit has US FDA 510(k) K221309, cleared Sep 2023, for WBC differential and RBC and platelet morphology. Malaria is only "flagged" and is not a cleared claim. It is a bench analyser sold to hospitals and chains (https://www.biospectrumindia.com/news/91/23658/sigtuples-ai100-with-shonit-receives-us-fda-510k-clearance.html; https://www.accessdata.fda.gov/cdrh_docs/reviews/K221309.pdf, search result).
- **Morphle.** Its site (opened) lists the MorphoLens 1/6/240/400 whole-slide scanners, HemoLens for peripheral smears, bone marrow and urine, and a robotic microtome. It shows no malaria product and gives a New York head-office address (https://www.morphlelabs.com).
- **Turocrates AI.** The site shows only the line "OS for precision diagnostics" (https://turocrates.ai, opened). The description as a microscope attachment comes only from the WTFund cohort note in T4 and is unverified.
- **The gap.** None sells a phone-on-existing-microscope, malaria-specific QA tool to a public programme.

### 6. The business
- Buyer: the state programme, through NHM budget lines. Today it pays for microscopists and cross-checking labs (cost NOT FOUND).
- Arithmetic:
  - Microscopy slides per year: 12.24 crore in 2017 (sourced). ASSUMPTION: about 10 crore today, after the shift to RDTs.
  - QA re-read at Rs 1.5 per slide: 10 crore x 1.5 = **Rs 15 crore a year**, the whole Indian malaria ceiling.
  - Per-lab licence instead. ASSUMPTION: about 15,000 malaria microscopy points (count NOT FOUND). 15,000 x Rs 6,000 a year = **Rs 9 crore a year**.
- Verdict on size: Indian malaria alone is too small to be a venture business. It is a beachhead.
- Expansion:
  - The same rig and pipeline for peripheral-smear morphology in small private labs. ASSUMPTION: about 1 lakh labs x Rs 500 a month = Rs 60 crore a year.
  - Export to African malaria programmes, through donor-funded procurement.
- First ten customers: Odisha, Chhattisgarh, Jharkhand, Mizoram, Tripura and Meghalaya programme officers. Their states are among the 33 high-burden districts, which held 64% of 2025 cases. Then two PPP lab chains, ICMR-NIMR (validation partner) and two NGOs running tribal health labs.

### 7. What a team could show by noon
- **Core, certain to work.**
  1. Train YOLO11n on tiled NLM thick-smear images, Pf plus uninfected, on a Colab T4. That is about 2 hours for 30 epochs (ASSUMPTION).
  2. Split by patient, never by image, so no patient appears in both training and test.
  3. Add the patch classifier.
  4. Ship a web or Android demo showing the thumbnail gallery and the count.
- **Microscope part.**
  1. Borrow a teaching microscope with a 100x oil objective from the biology lab.
  2. Photograph any prepared blood slides the lab holds.
  3. If no Plasmodium slides exist, the bio member makes and stains thin and thick films from a volunteer's own finger-prick (sterile lancet, consent). These are known negatives.
- **The one honest number.** Patient-level sensitivity and specificity on held-out patients: **30 Pf patients and 20 uninfected patients**, 40 images each. A patient counts as positive if confirmed candidates reach at least 1 per 200 WBC. Report each figure with a 95% interval; with 30 and 20 patients the intervals will be wide, and the pitch should say so. The baseline is the published patch-level 82.7% / 98.4%.
- **Second number, if microscope slides exist.** False candidates per 100 WBC on 20 fields of known-negative slides captured with the team's own phone. This is the domain-shift test the pitch should show.
- **Fallback.** If the microscope or slides fail, show only the held-out dataset result and a recorded capture video.

### 8. Parts and cost
- In a typical kit: none needed.
- Bring or buy locally:
  - Borrowed: teaching microscope with 100x oil objective, immersion oil, phone.
  - 3D-printed eyepiece clamp: about Rs 50 of filament.
  - Glass slides: about Rs 100.
  - Lancets and spirit swabs: about Rs 150.
  - Giemsa or Leishman stain from the bio lab.
  - Total cash: under Rs 500 (estimates).

### 9. Three hard questions
1. *"RDTs are cheaper and faster. Why read slides at all?"* Microscopy is still how species is confirmed, how parasite density is measured to follow treatment, and how QA is done. The national tables count crores of slides. But if a state is moving to RDT-only at village level, the market shrinks, and this answer must be checked state by state.
2. *"Your model is trained on Bangladeshi Giemsa images. Why would it work in Bastar?"* It will not work without adaptation. The noon demo measures the drop on our own captures. The business plan begins with a 2,000-slide re-read study in one district to fine-tune and validate.
3. *"Who pays, and how does it get bought?"* A state programme, through a pilot under NHM innovation funds, then procurement. That is slow (12 to 24 months), which is why the business case needs the private-lab morphology expansion.

### 10. Risks and what would kill it
- RDT-only policy at the periphery.
- Poor domain transfer across stains and microscopes.
- CDSCO device classification adding cost before revenue.
- Government payment delays.
- A bench-analyser maker (SigTuple) adding a cheap malaria mode.
- Kill test: if fine-tuning on 500 local slides cannot reach patient-level specificity of at least 95% at sensitivity of at least 90%, stop.

### 11. Verdict
Resolve answered: **malaria is the right first test.**
- TB smear microscopy is still large: 19.3 million smears in 2023, 79% of presumptive testing. But national policy targets 100% upfront NAAT, so that market is designed to shrink (IndiaSpend/The Hindu, snippet, https://www.indiaspend.com/health/2025-tb-elimination-goal-marred-by-low-govt-spending-erratic-drug-diagnostics-supply-945448).
- Cervical cytology has no open Indian slide supply and India screens mostly by VIA.
- Anaemia typing is already done by analysers.

Scores: **buildability 3/5** (the dataset half is a 5; the live-microscope half depends on what the bio lab has), **business 2/5** in India alone, **AI/ML share about 75%**. The CS vision member should lead, with the bio member owning slides, staining and the clinical protocol.

---

## M2 Hinglish OPD scribe that prints the prescription

### 1. The problem in one paragraph
Indian GPs see patients in a few minutes and write the prescription by hand while they talk. Irving et al. (BMJ Open, 8 Nov 2017) found that 18 countries holding about half the world's population get 5 minutes or less per primary-care visit, from 48 s in Bangladesh to 22.5 min in Sweden (search result, https://spiral.imperial.ac.uk/entities/publication/ce117921-e0d1-4b26-996a-72ab8d0430a4). India's own figure could not be opened (NOT CHECKED). The US analogue, Freed (Sequoia-led Series A, 5 Mar 2025), serves 17,000+ providers (https://sequoiacap.com/article/partnering-with-freed-an-ai-powered-clinicians-assistant). The Indian leader, Eka Care, has a scribe used by 3,000+ doctors (R4-05 entry 4, snippets).

### 2. How the system works
```
phone on desk (or Rs 800 lapel mic) records 2-3 min consult
 -> ASR (Hindi/English code-mixed, 16 kHz) -> transcript with speaker turns
 -> LLM extracts JSON: complaints, vitals, diagnosis, drugs[brand, strength, dose, freq, days], tests, advice, follow-up
 -> drug names snapped to an Indian brand dictionary; any low-confidence drug or dose is shown in red
 -> doctor taps to confirm (5-10 s) -> prescription PDF on the clinic letterhead
 -> thermal/laser print + WhatsApp to patient with advice in the patient's language
```

### 3. The AI/ML core
- **ASR.** Run three models tonight:
  - **Whisper large-v3-turbo** via faster-whisper. Open; handles code-switching reasonably on clean audio, but degrades on 8 kHz telephone audio (Gnani blog, vendor, snippet).
  - **AI4Bharat IndicConformer**. Open, NeMo.
  - **Sarvam Saaras v3**. API. Sarvam self-reports Saarika Hindi WER of 11.81% on its VISTAAR benchmark, which is not a code-mixed or medical test (https://docs.sarvam.ai/api/models/saarika, snippet).
- **The relevant benchmark.** Eka Care released the **Eka Medical ASR Evaluation Dataset**: 3,619 English and 320 Hindi test samples, MIT licence, gated on Hugging Face (`ekacare/eka-medical-asr-evaluation-dataset`). It is built around branded drug names. Its card gives English WER of **0.183 for AWS Transcribe against 0.109 for Eka's Parrotlet-a-en-5b** (search result summarising the HF card). The later Parrotlet-a-2.5-pro card shows Indian English 9.15 and Hindi 18.16 against Gemini 3.1 Pro at 12.09 and 19.08, but the metric is ambiguous and must be checked before citing. Older Hindi-English code-switched systems (MUCS 2021 baseline) sat above 35% WER (snippet).
  - **Implication:** expect about 10–20% WER on medical Hinglish. Whole-transcript WER is not the number that matters. The error that matters is a wrong drug or dose on a printed prescription.
- **Structuring.** An instruction-tuned LLM (Qwen2.5-7B-Instruct locally, or an API model) with JSON-schema constrained output. Drug normalisation by fuzzy and phonetic match (rapidfuzz plus Double Metaphone) against an Indian brand list, such as the Kaggle "A-Z medicine dataset of India" (existence and size NOT CHECKED).
- **What it cannot do.**
  - Separate three overlapping voices reliably when patient, attendant and doctor talk at once.
  - Know a drug the doctor only thinks of and never says aloud.
  - Guarantee dose correctness. That is why every prescription needs a doctor tap.
  - Clinical judgement of any kind.

### 4. Why India needs its own version
- Consults are 2–3 minutes, not 20. The output is a one-page prescription, not a US-style SOAP note filed to an EHR.
- Speech is code-mixed, and Indian brand names (Dolo, Pan-D, Augmentin 625) defeat general ASR.
- Clinics are noisy, shared rooms.
- Price must be low hundreds of rupees a month for a solo GP.
- Regulation:
  - DPDP Act consent for recording (rules' status NOT CHECKED).
  - NMC guidance on generic-name prescribing (status NOT CHECKED).
  - ABDM-compatible output is a plus, not a must.
- What is kept from Freed: ambient capture, a note in the doctor's own template, product-led growth. What changes: the output is a printed and WhatsApp prescription, plus the drug-safety confirmation step.

### 5. Who has tried, and the gap
**Eka Care has largely closed the gap the T4 claimed.** EkaScribe generates prescriptions as well as notes, works in Hindi, Tamil, Kannada, Gujarati and more (20+ languages per Capterra), and is ABDM-compliant. Sources (all search results): MedTechSpectrum https://medtechspectrum.com/news/16/24807/eka-cares-ai-powered-ekascribe-transforms-clinical-documentation-for-doctors-across-india.html ; Capterra https://www.capterra.in/software/1095338/EkaScribe . Reported price: $20–25 a month (YourStory, Nov 2025, https://yourstory.com/2025/11/healthtech-startup-eka-care-ai-standardise-medical-records-doctor-patient), or Rs 19,999 per user per year (SoftwareSuggest, Apr 2026, https://www.softwaresuggest.com/ekascribe). It has a free tier. Others: FosterHealth.ai, ZenMD and Docstribe (R4-05, snippets). The gaps left are narrow:
- noisy multi-speaker rooms;
- fully offline use in low-connectivity clinics. Eka has an NVIDIA offline project, so this gap may also close.
- an auditable drug-and-dose accuracy figure, which no vendor publishes for Hinglish.

### 6. The business
- Buyer: the solo or two-doctor clinic owner. Today: a pen and a printed pad, about Rs 0. Some pay a compounder.
- Arithmetic. ASSUMPTION: about 3 lakh solo private allopathic GPs and small specialists (NMC registration count NOT CHECKED).
  - At 10% paid adoption: 30,000 x Rs 400 a month x 12 = **Rs 14.4 crore ARR**.
  - Against a free Eka tier and a $20–25 Eka price, Rs 400 is the ceiling.
- First ten customers: GPs in Sonipat and Kundli, and Ashoka's own health-centre doctor for testing. They would come through a local IMA branch.
- Verdict on business: weak as a stand-alone company.

### 7. What a team could show by noon
- **Core, certain to work.**
  1. Record **30 staged consults**, 2–3 minutes each, written from 10 common OPD cases (fever, URTI, gastritis, hypertension follow-up) by the bio member. They use 60 real brand names.
  2. Record half quiet and half with OPD babble played from a speaker at about 65 dB (phone sound meter).
  3. Run the pipeline end to end and print the prescription.
- **The one honest number.** **Prescription line exact-match rate**: drug, strength, dose, frequency and duration all correct, over the roughly 90 prescribed drug lines.
  - Baseline: raw Whisper transcript plus the LLM, without the dictionary snap.
  - Also report drug-name keyword error on the 320 Hindi Eka samples if access is granted.
- **Fallback.** If live ASR is flaky, run batch processing on the recorded files.

### 8. Parts and cost
Software only. Optional: lapel mic (about Rs 500–800) and the event's printer.

### 9. Three hard questions
1. *"Eka already does this with prescriptions in Hindi, and has a free tier. Why you?"* Honestly, on the product as described, no reason. The only defensible wedge is a measured, published drug-line accuracy in noisy rooms, sold as a component (a drug-name verifier API) to scribe makers. Or a different user: a pharmacist reading handwritten prescriptions.
2. *"What happens when it prints the wrong drug?"* The doctor must confirm each red line. Liability stays with the prescriber. The product must log what the doctor confirmed.
3. *"Will a GP pay?"* Most will not pay more than a few hundred rupees a month. The price evidence is Eka's own $20–25 and free tier.

### 10. Risks and what would kill it
Eka or a pharma-funded free scribe already serves the segment. Doctors also resist anything that adds taps. Consent and recording rules under DPDP are a further risk. Kill test: if 20 GP interviews produce fewer than 5 who would pay Rs 300 a month after trying Eka, stop.

### 11. Verdict
**Does not survive as stated.** The smaller version that does survive is a **drug-and-dose verifier for Indian code-mixed speech**: a constrained-vocabulary matcher plus confirmation UI, benchmarked openly. It can be shown overnight as part of the scribe. Scores: **buildability 4/5, business 2/5, AI/ML share about 80%**. Led by the CS member who knows ASR; the bio member writes the case scripts.

---

## M3 Solder and placement defect inspector for small electronics assemblers

Overlap: CCTV/vision AI for factories (technique; sector is electronics, not food).

### 1. The problem in one paragraph
India's electronics assembly base is large and getting larger, but it is split. Big EMS plants buy automatic optical inspection (AOI). Small assemblers hand-solder and inspect by eye under a magnifier lamp. An ELCINA-linked deck counts **1,330–1,350 SMT lines and 700+ wave-soldering lines as of 2018** (search snippet, ELCINA/MAIT material; the PDF could not be parsed). A new AOI machine costs about **Rs 50 lakh**, and demo units cost a half to a third of that (ElectronicsB2B, undated, https://www.electronicsb2b.com/?p=2266, snippet). A Seamark 3D AOI is listed at **Rs 60 lakh** (IndiaMART Gurugram, https://m.indiamart.com/city/gurgaon/optical-inspection-system.html, snippet). A unit with one line and Rs 5–20 crore turnover cannot buy that, so escapes reach the customer as field returns.

### 2. How the system works
```
fixed jig + overhead camera (USB microscope cam or phone) + diffuse ring light
 -> board placed against corner stops -> capture
 -> register to the golden board (ORB features + homography)
 -> crop each component ROI using the KiCad/Altium pick-and-place (CPL) file
 -> per ROI: (a) anomaly score vs golden boards (PatchCore)
            (b) detector for solder classes (bridge, excess, insufficient, spike)
            (c) presence / polarity check (template match on the mark)
 -> screen: board image with red boxes and labels; PASS / FAIL; log to CSV per serial
```
The pick-and-place file is the key design choice. It tells the system where every part should be, so the model judges small crops, not a whole cluttered board.

### 3. The AI/ML core
- **Correction to the R4 sketch.** The well-known PCB datasets are **bare-board fabrication** sets, not assembly sets. DeepPCB has 1,500 image pairs; PKU-Market-PCB has 693 images. Their defects are open, short, mouse-bite and spur (sizes from memory, NOT CHECKED). They do not teach solder-joint or placement faults.
- **Assembly data.**
  - **SolDef_AI** (Fontana et al., *J. Manuf. Mater. Process.* 8(3):117, 2024). Open; classes good / excess solder / poor solder / spike. The authors benchmark Mask R-CNN. Mirrored on Roboflow Universe under CC BY 4.0 (https://universe.roboflow.com/defectdetection-e5sqy/soldef_ai-for-defect-detection, snippet; the paper page returned 403, so image count NOT CHECKED).
  - A 2024 arXiv YOLO variant with a hybrid-attention feature pyramid on a **3,154-image solder dataset** with two defect types (https://arxiv.org/pdf/2401.01214, snippet).
- **Model choice.**
  - Primary: **PatchCore anomaly detection** (Intel `anomalib`). It trains only on good boards, so a shop needs 20–50 photos of a good board and no defect labels. On MVTec AD it reports image-level AUROC of about 99% (Roth et al., arXiv 2106.08265; figure from memory, NOT CHECKED this round).
  - Secondary: **YOLO11n** fine-tuned on SolDef_AI, to name the solder fault.
  - Polarity: classical template matching.
- **What it cannot do.** From one top-down camera it cannot see:
  - fillet height or wetting angle (real AOI uses several angles and RGB tiered lighting);
  - hidden joints under BGAs or QFNs (needs X-ray);
  - lifted leads by a few microns;
  - electrical faults.
- **What it catches.** Missing, wrong, shifted or reversed parts, bridges, gross excess or insufficient solder, and tombstones. That is low-end 2D AOI scope.

### 4. Why India needs its own version
- **Price.** Rs 25–40 thousand of hardware against Rs 50–60 lakh for an AOI machine.
- **Mix.** Indian small shops run high-mix, low-volume work with a lot of through-hole and hand soldering. Golden-board anomaly detection fits that better than rule programming that takes an AOI engineer a day per board.
- **Language.** An operator UI in Hindi with pictures.
- **Buyer.** The owner, often the founder-engineer, or an OEM pushing quality down to its tier-2 assemblers.
- **Origin.** It copies SixSense (Peak XV Surge 11, 25 Sep 2025, https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11): no-code vision inspection. It changes the line (SMT/THT assembly, not wafer fabs), the price (100x lower) and the training (good boards only).

### 5. Who has tried, and the gap
- SwitchOn (Rs 78 crore pre-Series B, IvyCap, Jul 2026) and Frinks AI ($5.4M, Prime, 2025) sell AI inspection to larger plants (R4-05 entry 12).
- Koh Young, Saki and Omron sell 3D AOI through Indian distributors at lakhs of rupees.
- Cheap Chinese desktop AOIs exist (price NOT CHECKED).
- The gap is the sub-Rs 50,000, self-trained station for small units.

### 6. The business
- Buyer: owner of a 20–200-person EMS or electronics product firm in Noida, Manesar, Bhiwadi, Kundli, Pune or Chennai. Today: 1–3 inspectors at about Rs 15–20 thousand a month each, plus rework and returns (ASSUMPTION).
- Price: Rs 30,000 for the station plus Rs 1,500 a month for software and model updates.
- Arithmetic:
  - 1,350 SMT lines in 2018. ASSUMPTION: about 2,500 lines today, and 40% without AOI = 1,000 lines.
  - Plus manual THT/wave units. ASSUMPTION: about 3,000 more.
  - About 4,000 sites x (Rs 30,000 + Rs 18,000 a year) = **Rs 19 crore** in year-one value at full penetration. Recurring: 4,000 x Rs 18,000 = **Rs 7.2 crore a year**.
- Verdict on size: a real but small Indian market. Export to Southeast Asian SMEs and growth in Indian assembly lift it.
- First ten: small assemblers in HSIIDC Kundli and Rai (next to Ashoka), Noida Phase 2, Bhiwadi; ELCINA's Micro and Small Industries Forum members (https://elcina.com/emsif); college robotics-kit makers.

### 7. What a team could show by noon
- **Setup.**
  1. Use 10 identical boards from the kit (ESP32 or Arduino Nano boards) as golden references and test subjects.
  2. Add 20 cheap through-hole kits (LED blinker or 555 timer). The hardware member solders 10 good and 10 each with one seeded defect: bridge, missing resistor, reversed LED, reversed electrolytic, cold/insufficient joint (2 of each).
  3. Build the jig from cardboard or a 3D print, with a ring light.
- **The one honest number.** **Board-level detection rate on 20 seeded-defect boards and false-call rate on 20 good boards**, each board imaged 3 times after re-placement (120 images).
  - Trained only on 30 images of good boards.
  - Baseline: pixel-difference against the golden image after registration.
  - Second baseline: a team member inspecting each board for 30 s by eye, blind to which boards are seeded.
  - Report recall, false calls per board and seconds per board.
- **Fallback.** If PatchCore is unstable, show YOLO on the SolDef_AI test split with its mAP, and the registration plus missing-part check.

### 8. Parts and cost
- In a typical kit: dev boards, breadboard, LEDs, resistors, a soldering iron if the lab has one.
- Bring or buy locally (estimates):
  - USB digital microscope camera or a 1080p webcam: Rs 1,500–3,500.
  - LED ring light: Rs 400.
  - Through-hole kits: Rs 60–100 each x 20 = about Rs 2,000.
  - Jig: 3D printed.
  - Total: about Rs 4,000–6,000.

### 9. Three hard questions
1. *"A single 2D camera misses half of solder defects. Isn't this a toy?"* It misses fillet-shape and hidden-joint defects. It catches placement, polarity, bridges and gross solder, which make up most hand-assembly escapes (share NOT FOUND; to be measured at a pilot shop). Sell it as replacing the eye-and-lamp check, not the AOI.
2. *"How many false calls per board?"* That is the number the demo reports. In production a station is abandoned once false calls pass about 1 per board, so thresholds are tuned per product on the shop's own good boards.
3. *"Why won't SwitchOn or a Chinese AOI maker undercut you?"* They might. The defence is CPL-file onboarding in minutes, Hindi operator UI and the distribution channel through ELCINA and component distributors. That is a weak moat; the business is a tools business.

### 10. Risks and what would kill it
- Lighting and board-colour variation.
- Shops unwilling to share CAD/CPL files (the system must also work from a golden photo alone).
- Price pressure from cheap AOI.
- Kill test: false calls above 0.5 per good board at 90% defect recall in a two-week pilot.

### 11. Verdict
Resolve answered:
- A Rs 20–30 thousand station is credible for placement and gross solder faults only.
- The small-assembler segment is at most low thousands of sites in India.
- What they spend on inspection today is people, not machines.

Scores: **buildability 5/5, business 3/5, AI/ML share about 60%** (the rest is jig, lighting and CPL plumbing). The CS vision member leads; the hardware member owns boards, defects and lighting.

---

## M4 Acoustic leak finder for city water pipes

### 1. The problem in one paragraph
Indian utilities lose a large share of treated water before it is billed. The common figure of 40–50% non-revenue water has no single authoritative national source (MIT Solve, https://solve.mit.edu/solutions/83032; Zerodha, https://zerodha.com/z-connect/?p=381495, snippets). Supply is intermittent: Mumbai averaged **5.37 hours of water a day in 2024, and only 4% of city pockets got round-the-clock supply** (Praja Foundation via Indian Express, https://praja.org/media-room/4675, snippet). Bengaluru's BWSSB is deploying AI and robotics against leaks and theft (https://theprint.in/india/bwssb-to-deploy-ai-and-robotic-technologies-to-curb-water-theft-and-leakages/2947404/, snippet). Leak finding is still done by crews with listening rods, or by digging.

### 2. How the system works
```
field engineer + "listening stick": piezo contact disc / MEMS accelerometer on a rod
 -> touch valve, hydrant, meter or exposed pipe for 10 s DURING SUPPLY HOURS
 -> phone records (USB sound card), GPS-tags the point
 -> on-phone model: P(leak noise) + label (leak / consumption / pump / traffic)
 -> map of points coloured by score; repeat survey shows trend
 -> crew confirms the top-scoring stretch with a ground mic before digging
```
Fixed loggers (ESP32 plus accelerometer, battery, night upload) are phase 2. In intermittent systems a logger must wake on pressure, so it also needs a pressure sensor.

### 3. The AI/ML core
- **Model.** Log-mel spectrogram (0–2 kHz for plastic, 0–5 kHz for metal) into:
  - a small CNN, or
  - pretrained audio embeddings (**YAMNet**, or **PANNs CNN14** via `panns_inference`) plus logistic regression or gradient boosting.
  - Embeddings are preferred: data are tiny, and they generalise better across sensors.
- **Data.**
  - **Aghashahi, Sela & Banks, "Benchmarking dataset for leak detection and localization in water distribution systems", Data in Brief 48 (2023) 109148.**
    - Rig: 47 m of 152.4 mm PVC, looped and branched.
    - Sensors: 2 accelerometers, 2 hydrophones, 2 dynamic pressure sensors.
    - Leak types: four (longitudinal crack, circumferential crack, gasket, orifice) plus no-leak, under several flow and noise conditions.
    - **280 signals of 30 s**; hydrophone at 8 kHz; accelerometer and pressure in CSV.
    - Mendeley DOI 10.17632/tbrnp6vrnj.1 (search result).
  - Plus the team's own rig recordings.
- **Published accuracy, plastic against metal.**
  - MEMS-accelerometer study on real networks with ML: **over 99% accuracy on metal pipes, about 89% on non-metal** (Science of the Total Environment, doi 10.1016/j.scitotenv.2021.151110, snippet).
  - A related Hong Kong (PolyU) study: random forest **100% on metal against 94.93% on non-metal** (snippet).
  - IFIP Networking 2024: leak noise in plastic attenuates far faster than in metal, and hydrophones beat accelerometers (https://dl.ifip.org/db/conf/networking/networking2024/1571017417.pdf, snippet).
  - **Implication:** expect sensor-to-leak range of only metres to tens of metres on PVC/HDPE, against hundreds on cast iron.
- **What it cannot do.**
  - Hear a leak on a pipe that is not pressurised, which in India is 18+ hours a day.
  - Separate a leak from an upstream household suction pump or open tap without context.
  - Localise precisely with one sensor (correlation needs two synchronised sensors).
  - Generalise from a lab rig to buried, soil-loaded pipes without field data.

### 4. Why India needs its own version
- **Intermittent supply** breaks the global method, which is night-time listening at minimum flow. In India, listening must happen during supply, when consumption noise is highest. Household suction pumps on the main are a specific Indian noise source. The model needs a "pump" class and a survey protocol (listen early in the supply window, before tanks fill).
- **Pipes.** Mixed materials, increasingly PVC/HDPE, often unmapped.
- **Price.** Commercial correlators and noise loggers are imported and costly (price NOT FOUND).
- **Buyer.** Municipal water departments and PHEDs through tenders, with slow payment. Ward-level leak-repair tenders exist: Ahmedabad's Khokhara ward has a Rs 10 lakh leak detection and repair package specifying ultrasonic or electronic tools (TenderDekho, snippet, https://tenderdekho.com/tender-detail/ahmedabad-municipal-corporation-water-leakage-repair-tender-td-279794).
- **Origin.** It copies Puralink (Surge 12, 28 Sep 2026): pipe inspection. It changes the method: no in-pipe robot, external sensing only.

### 5. Who has tried, and the gap
- Solinas Integrity (IIT Madras; Endobot for 90 mm+ pipes; about $948K) and Fluid Robotics (Pune) go inside pipes.
- SmartTerra works on utility data (R4-05 entry 15).
- Global acoustic vendors (Ovarro, Gutermann) sell hydrophones and loggers.
- The gap: a cheap, phone-based survey tool tuned for intermittent supply and plastic pipe. Whether utilities would adopt it is unproven.

### 6. The business
- Buyers, in order of speed to pay:
  1. Private networks: universities, townships, industrial estates, airports, rail colonies.
  2. PPP water operators.
  3. Municipal corporations.
- Arithmetic (no per-km tender rate was found, so ASSUMPTIONS throughout):
  - Survey service at Rs 3,000 per km.
  - City networks: 100 cities x 1,000 km = 1 lakh km, surveyed twice a year = 2 lakh km x Rs 3,000 = **Rs 60 crore a year** if it became standard practice.
  - Private campus route: 1,000 sites x Rs 1.5 lakh a year = **Rs 15 crore**.
  - The tool-sale alternative (Rs 40,000 per kit to 5,000 ULB and contractor crews = Rs 20 crore one-off) is weaker.
- First ten: Ashoka's estate office, HSIIDC Rai and Kundli, two Gurugram townships, Sonipat municipal water works, BWSSB's innovation cell, Nagpur's operator.

### 7. What a team could show by noon
- **Rig.**
  1. 3–4 m of 1-inch PVC (or GI if available) connected to a lab tap.
  2. Drill a 1.5 mm "leak" hole with a screw plug.
  3. Mount a piezo disc with tape and clay on the pipe at 0.5, 1, 2 and 3 m from the hole.
  4. Feed a USB sound card on a laptop. Optionally an MPU6050 on an ESP32 as a second channel.
- **Recording plan.** Conditions: plug in or out x four distances x flow on (tap downstream open or closed) x distractor (a small pump, or a phone playing traffic noise).
- **The one honest number.** **Leak / no-leak accuracy on about 120 ten-second clips, split by recording session**, so no clip's neighbours sit in training.
  - Report accuracy against distance on our PVC rig.
  - Baseline: an RMS-energy threshold.
  - Also report transfer: train on Aghashahi, test on our rig.
  - State plainly that this is a lab rig, not a buried main.
- **Fallback.** Classifier on the Aghashahi data only, with a live sound demo.

### 8. Parts and cost
- In a typical kit: ESP32, MPU6050 or another accelerometer if present, piezo disc, jumper wires.
- Bring or buy locally (estimates):
  - PVC pipe and fittings: Rs 400.
  - Tap adapter and hose: Rs 200.
  - USB sound card: Rs 300.
  - Spare piezo discs: Rs 50.
  - Small 12 V pump: Rs 300.
  - Total: about Rs 1,300.

### 9. Three hard questions
1. *"Your pipes are empty most of the day and full of pump noise when they're not. How does this work at all?"* Only inside the supply window, and only with a pump/consumption class trained on Indian recordings we do not yet have. This is the unsolved part. A pilot must record in one ward before any accuracy claim.
2. *"Plastic pipes kill the signal in a few metres. How many access points per km do you need?"* On PVC, perhaps every 20–50 m (inferred from the attenuation literature, not measured). That makes a stick survey slow. On DI/CI trunk mains it is viable. Lead with metal trunk mains and campus networks.
3. *"Will a municipality pay a startup on time?"* Often not. That is why the first buyers are private campuses and PPP operators.

### 10. Risks and what would kill it
Field accuracy on plastic and intermittent networks may be poor. Procurement is slow, and the incumbent contractors would be paid to find fewer leaks. Kill test: in a two-week campus pilot, fewer than half of the high-score points prove to be real leaks on excavation.

### 11. Verdict
Resolve answered:
- Accuracy: metal about 99–100%; plastic about 89–95%, at short range, in published ML work.
- Intermittent supply forces listening during supply and adds pump noise. No published method handles that.
- Payers: private campuses and PPP operators before municipalities.

**Survives only in smaller form:** a phone "listening stick" survey assistant for metal mains and private campus networks, not a city-wide leak finder. Scores: **buildability 4/5, business 2/5, AI/ML share about 50%**. The hardware member leads (sensor coupling and the rig decide everything); the CS member builds the audio model.

---

## F2 Health-insurance claim checker that cites the policy clause

### 1. The problem in one paragraph
- **Grievances.** **1,37,361** general and health insurance grievances in FY25, up 41%, about 69% claim-related (OutlookMoney, snippet, https://www.outlookmoney.com/amp/story/personal-finance/health-insurance-complaints-jump-41-per-cent-69-per-cent-involve-claims-failures-reveals-1-finance-study).
- **Claims.** IRDAI FY25: **3.26 crore health claims, 8% repudiated**, about 26 lakh claims (snippet, https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx).
- **Fraud, waste and abuse.** BCG with Medi Assist puts it at Rs 8,000–10,000 crore a year (R4-04, snippet).
- **Turnaround rules.** IRDAI's Master Circular of 29 May 2024 requires cashless decisions within 1 hour and discharge authorisation within 3 hours (Business Today, https://www.businesstoday.in/personal-finance/insurance/story/health-insurance-irdai-sets-3-hour-time-limit-for-insurers-to-clear-cashless-claims-details-here-431354-2024-05-29, snippet).
- **Repudiation rules.** A claim may not be repudiated without the Claims Review Committee's approval (snippet). A rejection or deduction must cite the exact policy terms (Ditto, https://joinditto.in/articles/irdai-flags-lapses-in-health-insurance-claims/, snippet with garbled text; **circular wording NOT CHECKED**).
- **Consequence.** Hospital insurance desks now work against hard clocks, and every deduction arrives with a clause number someone must check.

### 2. How the system works (pick: the hospital TPA desk)
```
nursing-home TPA desk uploads: policy schedule + wording PDF, pre-auth form,
   discharge summary, itemised bill, investigation reports (scans or photos)
 -> OCR / VLM extraction -> claim JSON (diagnosis, procedure, ICD guess, LOS,
   room category and rent, line items)
 -> clause engine:
     (a) computable rules: room-rent cap and proportionate deduction, sub-limits,
         co-pay, waiting periods vs policy start date, IRDAI non-payable items list
     (b) text clauses: retrieval over this policy's wording, LLM judges, must quote the clause verbatim
 -> output BEFORE submission: "Likely deductions Rs 18,400: 3.2 room-rent (quote),
   consumables list item 41 (quote); missing: indoor case papers, implant sticker"
 -> after a query/deduction letter: map each insurer line to the clause and
   draft a reply or appeal with the policyholder's facts
```

### 3. The AI/ML core
- **Extraction.**
  - Open: **Qwen2.5-VL-7B** or Surya/PaddleOCR plus an LLM.
  - API: any frontier VLM.
  - Output is a strict JSON schema, with fields cross-checked by arithmetic (bill totals must add up).
- **Clause retrieval.** Hybrid BM25 plus a dense embedder (bge-m3, multilingual) over clause-chunked policy wordings.
- **Judging.** The LLM is constrained to return a clause ID and a verbatim quote. A string-match verifier rejects any quote not present in the wording, so the system cannot cite a clause that does not exist.
- **Deterministic parts.** Room-rent proportionate deduction, sub-limits, co-pay and waiting periods are coded as rules, not left to the LLM.
- **Data.**
  - Public policy wordings for the top retail products (insurer websites).
  - The IRDAI standard exclusions and non-payable items lists (to be pulled from the circulars; NOT CHECKED).
  - **Insurance Ombudsman awards**, published by the Council for Insurance Ombudsmen, as real rejected cases with the cited clause and the outcome (availability and format NOT CHECKED). These are the best Indian test set available tonight.
  - Synthetic claim packets for the demo.
- **Published accuracy.** NOT FOUND for Indian claims. No public benchmark exists. The team must measure its own.
- **What it cannot do.**
  - Judge medical necessity.
  - Read illegible handwriting reliably.
  - Know an insurer's internal guidelines or a hospital's negotiated tariff (PPN packages).
  - Predict an adjuster's discretion.
  - It explains and predicts; it does not decide.

### 4. Why India needs its own version
- **Rules.** India-specific: room-rent proportionate deductions, the IRDAI non-payable list, the 1-hour and 3-hour clocks, the Claims Review Committee, the Bima Bharosa / Ombudsman path.
- **Documents.** Scanned, handwritten and mixed English/Hindi.
- **Buyer.** A 20–100-bed nursing home whose receivables depend on TPA settlements. US self-insured employers, Avelis's buyer, have no Indian equivalent at scale.
- **What changes from the copied startups.**
  - Avelis Health (YC S25) audits claims for payers. That side is taken in India (§5).
  - From Pace (Sequoia, $10M Series A, 27 Jan 2026) we keep "agent reads the SOP and gives a cited summary for a human".
  - We point it at the provider side.

### 5. Who has tried, and the gap
**The payer side is crowded. Round 4's "none found" was wrong.**
- **Superclaims** (Hyderabad): 65 AI agents, about 1 lakh claims a month, 10+ insurers and TPAs. Acquired by ekincare, Jul 2026 (https://telanganatoday.com/hyderabad-startup-superclaims-uses-ai-to-speed-up-health-insurance-claims ; https://india.entrepreneur.com/business-news/ekincare-acquires-hyderabad-based-saas-firm-superclaims, snippets).
- **Medi Assist's MAtrix** AI platform, with Star Health, May 2025 (snippet).
- **Bajaj General's in-house "Niriksha"** agentic adjudicator (https://www.qorusglobal.com/innovations/30778-niriksha-health-claims-adjudication-using-agentic-ai, snippet).
- **Policybazaar for Business ClaimSetu** (snippet).
- **Vitraya.** Clients reportedly include Star Health, Niva Bupa and Care, but the only source is one student slide deck.
- **NHA's PM-JAY Auto-Adjudication Hackathon 2026** (https://www.devdiscourse.com/article/law-order/3906970-indiaai-mission-honours-winners-of-ab-pm-jay-auto-adjudication-hackathon-showcase-2026, snippet).
- **Patient side.** Insurance Samadhan (grievance service; claim rejection is 88% of its complaints, Business Today, Mar 2025, https://www.businesstoday.in/amp/personal-finance/insurance/story/88-of-consumer-complaints-are-due-to-insurance-claims-being-rejected-report-467731-2025-03-12, snippet) and Ditto advisory.
- **Gap.** A pre-submission checker for small hospitals' insurance desks (ClaimBuddy and IHX not checked).

### 6. The business
- Buyer: owner or administrator of a 20–100-bed nursing home. Today: 1–3 TPA-desk staff at Rs 15–25 thousand a month each, plus deductions written off.
- Price: Rs 4,000 a month, or Rs 40 per claim checked.
- Arithmetic:
  - 3.26 crore claims a year. ASSUMPTION: 40% pass through non-chain small and mid hospitals = 1.3 crore claims.
  - At Rs 40 per claim = **Rs 52 crore a year** ceiling.
  - Seat model, ASSUMPTION: 15,000 empanelled small hospitals x Rs 48,000 a year = **Rs 72 crore**.
  - Value check: if the checker recovers even Rs 2,000 of avoidable deduction on 1 claim in 20, that is Rs 100 per claim checked, 2.5x the price.
  - Patient-side appeal drafts as a free funnel; Rs 499 per drafted Ombudsman complaint.
- First ten: nursing homes in Sonipat, Panipat and Rohtak through the local IMA/AHPI chapter; two hospital billing consultants; one TPA-desk outsourcing firm.

### 7. What a team could show by noon
- **Core, certain to work.**
  1. Three public policy wordings, clause-chunked.
  2. Rule engine for room rent, co-pay, sub-limits, waiting periods and the non-payable list.
  3. **20 synthetic claim packets** written by the bio member from realistic cases (appendectomy, cataract, dengue, normal delivery, knee replacement), each with 0–3 seeded problems.
  4. Upload, then a cited deduction forecast and a missing-documents list.
- **The one honest number.** On the 20 packets (about 40 seeded issues): **issue recall and precision, plus the share of citations that are both verbatim and the correct clause**.
  - Baseline: the same LLM with the whole policy in the prompt, without retrieval, rules or the quote verifier.
  - If Ombudsman awards are accessible, add **top-3 clause-match accuracy on 30 real awards** against the clause the insurer actually cited.
- **Fallback.** Typed claim JSON instead of OCR'd scans.

### 8. Parts and cost
Software only.

### 9. Three hard questions
1. *"Insurers and TPAs already run AI adjudication. Won't the insurer's own model always win?"* The checker does not fight the adjudicator. It makes the hospital's file complete and predicts deductions before submission. Hospitals have no tool for this today, and payer-side AI makes provider-side preparation more valuable, not less.
2. *"Where do you get real claims without breaking privacy law?"* Synthetic data and Ombudsman awards for the build. Pilot data stays in the hospital under its consent, with on-premise or Indian-region processing. No training on patient data without a signed agreement.
3. *"What if you cite the wrong clause and the hospital relies on it?"* Every citation is a verified verbatim quote with a confidence score. Low-confidence items are marked "check". Liability terms say it is advisory.

### 10. Risks and what would kill it
- Insurer portals changing formats.
- Hospitals' unwillingness to pay for software.
- Policy wordings changing every year.
- IRDAI standardising so much that deductions vanish (unlikely soon).
- A TPA giving a similar tool free to hospitals to speed its own queue.
- Kill test: a 30-day pilot at 3 nursing homes shows no fall in queries or deductions.

### 11. Verdict
Resolve answered: **pick the hospital desk** (pre-submission plus reply drafting), not the insurer or TPA auditor, which is crowded. Scores: **buildability 4/5, business 3/5, AI/ML share about 75%**. The CS/LLM member leads; the bio member writes the claim packets and checks clinical plausibility.

---

## F3 Hindi voice agent that makes a small fleet's check calls

Overlap: voice notes turned into structured data (technique, not sector).

### 1. The problem in one paragraph
- **Fragmentation.** Indian trucking is split into many small owners: about **75% of operators run fewer than five trucks** (Redseer, snippet, https://redseer.com/articles/unlocking-growth-in-indias-fragmented-trucking-sector/). Between 1 and 2 lakh brokers sit between owners and loads (Deccan Herald, snippet).
- **Language.** One vendor case page says **more than 60% of truck operators and SME transporters are Hindi-first** (snippet, vendor material on Vahak, https://www.rapyder.com/?p=31991).
- **How trips are tracked.** A transporter or shipper with market-hired trucks learns where a load is, why it is late and whether it was delivered by phoning the driver, often many times per trip.
- **Why tracking does not settle it.** FASTag data through ULIP now gives toll-crossing events without a GPS device. It reflects only the last toll crossed, not live position or status. The Road Ministry also sought an audit of ULIP data access after complaints of vehicle data being resold (search result summarising fr8.in, superprocure.com and lorrycare.com; https://www.fr8.in/blog/unified-logistics-interface-platform-ulip-india/).

### 2. How the system works
```
trip sheet (Google Sheet / Excel): truck no., driver phone, origin, destination, LR no.
 -> scheduler: call driver at planned points (or when FASTag shows no crossing for N hours)
 -> voice agent (Hindi/Hinglish; Haryanvi/Punjabi accents) asks: kahan ho? kab tak pahunchoge?
    koi problem? unloading hua? POD photo WhatsApp kar do
 -> ASR -> LLM slot-filling: location text, ETA, status, issue type, POD flag
 -> place resolver: "Dharuhera ke paas dhaba" -> OSM gazetteer -> lat/long -> OSRM ETA check
 -> trip sheet updated; exceptions (breakdown, police, detention, no answer x2) -> WhatsApp alert to the munshi
 -> shipper gets one daily status message per load
```

### 3. The AI/ML core
- **Speech stack.**
  - ASR on 8 kHz phone audio: **AI4Bharat IndicConformer** or **Whisper large-v3-turbo**, or the Sarvam API. Whisper degrades at 8 kHz (Gnani blog, vendor, snippet), so test both.
  - TTS: **AI4Bharat Indic Parler-TTS** (open) or Sarvam Bulbul.
  - Orchestration: open-source frameworks (Pipecat, LiveKit Agents, or Bolna's open-source framework; licences NOT CHECKED), or Bolna's hosted stack.
- **Dialogue.** A small state machine with an LLM doing slot extraction and re-asks. A free-form agent is avoided: drivers are driving, so calls must stay under 40 s.
- **The interesting ML piece** is **spoken place-name resolution**.
  - Drivers name dhabas, toll plazas, villages and highway numbers.
  - Build a corridor gazetteer from OpenStreetMap (places, toll plazas, fuel stations along NH-48 and NH-44).
  - Fuzzy-match transliterated names with phonetic keys.
  - Choose among candidates using the last known toll crossing and the route.
- **Data.** No public Indian trucker-call corpus (NOT FOUND). Build tonight with 30+ role-played calls recorded over real mobile networks with highway noise.
- **Published accuracy.** NOT FOUND for this domain. Nearest is general Hindi ASR at about 12–20% WER (M2 sources); expect worse on 8 kHz noisy calls.
- **What it cannot do.**
  - Verify the driver is telling the truth. Location claims can be checked only against FASTag/GPS.
  - Handle drivers who do not answer while driving. Legally and safely they should not.
  - Negotiate rates.
  - Understand every dialect. Tamil and Telugu need their own models.

### 4. Why India needs its own version
- **Language.** Hindi and Hinglish, with Punjabi, Haryanvi and Rajasthani accents. Poor networks.
- **Price.** Per minute, Bolna's bundled STT+LLM+TTS starts at **$0.06 a minute, about Rs 5.5**, plus telephony and platform fees not listed (https://www.bolna.ai/pricing, opened 12 Nov 2026). A 40-second call costs about Rs 5–6 all-in (ASSUMPTION on telephony). At 6 calls per trip that is Rs 30–36 a trip, against freight of Rs 30,000–80,000 a trip (ASSUMPTION).
- **Buyer.** The transport contractor or fleet operator with 10–100 own and attached trucks, whose munshi or traffic staff make the calls. Or a shipper's logistics desk using market trucks. It is not the 1–4 truck owner, who drives or calls himself.
- **Regulation.** TRAI commercial-communication rules for automated calls (category for service calls NOT CHECKED). DPDP consent for recording drivers.
- **Kept from Hemut (YC X25):** outbound check calls and structured updates. **Changed:** Indian languages, FASTag-aware call timing, WhatsApp POD capture. Load booking is dropped, because Indian booking runs on broker relationships and apps (Vahak, BlackBuck).

### 5. Who has tried, and the gap
- Horizontal Indian voice-AI platforms market logistics use cases: driver coordination, ETA, delivery confirmation (https://www.ringg.ai/use-cases/logistics ; https://www.acefone.com/industries/logistics/ ; https://www.squadstack.ai/logistics-quickcommerce-mobility, vendor pages).
- Edesy sells a Hindi truck-driver hiring screener (https://edesy.in/ai-voice-agent/use-cases/recruitment/logistics/in/hindi).
- Bolna ($6.3M seed, General Catalyst) and Ringg ($10M, Peak XV) are platforms, not trucking products.
- Freight platforms (BlackBuck, Vahak, TrucksUp, Fr8) and visibility vendors (Intugine, Trucknetic, using FASTag/ULIP) own tracking.
- The gap is thin: a packaged trip-status agent for mid-size transporters. Any of the above could add it.

### 6. The business
- Buyer: owner of a 10–100 truck transport company or a shipper's dispatch desk. Today: 1–3 traffic staff at Rs 15–20 thousand a month each, doing calls among other work (ASSUMPTION).
- Price: Rs 15 per tracked trip, or Rs 3,000 a month for up to 300 trips.
- Arithmetic:
  - Fleets of 10+ trucks. ASSUMPTION: about 25,000 firms (count NOT FOUND) x 150 trips a month x Rs 15 x 12 = **Rs 67 crore a year** at full penetration.
  - At 5%: **Rs 3.4 crore ARR**.
  - Margin per trip: Rs 15 – about Rs 33 cost (6 calls) is negative. Fix it by calling only on exceptions (no FASTag crossing in 4 h; ETA passed): about 2 calls a trip = about Rs 11 cost. **The margin is thin, and price has to rise to about Rs 25 a trip.**
- First ten: transporters at Kundli, Sanjay Gandhi Transport Nagar (Delhi) and the Gurugram/Manesar auto-parts corridor; one Sonipat manufacturer's dispatch desk.

### 7. What a team could show by noon
- **Core, certain to work.**
  1. A live outbound call to a team member's phone over a real network, in Hindi.
  2. 3 questions; the Google Sheet row updates in front of the judges; a WhatsApp exception alert.
- **The one honest number.** **Slot accuracy over 30 role-played calls**: 5 callers, each playing 6 scripted scenarios (on time, delayed by traffic, breakdown, police check, unloaded with POD, vague location), with truck noise played near the phone.
  - Fields: location resolved within 20 km of truth, ETA within 1 h, status, issue type.
  - Baseline: raw ASR transcript with keyword rules.
  - Also report median call length and the share of calls finished without a re-ask.
- **Fallback.** If telephony set-up fails (Indian number provisioning and KYC can take days), use a browser WebRTC call with the same pipeline and phone-quality audio downsampled to 8 kHz.

### 8. Parts and cost
Software only. API credits: a $10 Bolna top-up or a free Sarvam tier covers the night.

### 9. Three hard questions
1. *"GPS, SIM tracking and FASTag already tell the transporter where the truck is. What is left?"* Status and reasons: why it is late, breakdown, detention at unloading, POD. Tracking cannot give those. Whether transporters pay for that is not proven by any public source we found.
2. *"Drivers will hang up on a robot. What is your answer rate?"* Unknown. A pilot must measure it. Mitigations: call from the transporter's known number, keep it under 40 s, and only call on exceptions.
3. *"Ringg or Bolna can ship a trucking template next month. Where is your moat?"* Weak. It lies in the corridor place-name resolver, FASTag-triggered call logic and distribution to transporters. This is a vertical-SaaS business with modest defensibility.

### 10. Risks and what would kill it
- Low answer rates.
- Driver distraction (safety and law).
- Telecom rules on automated calls.
- Platforms bundling the feature free.
- Thin unit economics.
- Kill test: in a 2-week pilot with one transporter, fewer than 60% of calls give a usable status, or the transporter will not pay Rs 25 a trip.

### 11. Verdict
Resolve answered:
- Buyer: the 10–100 truck transporter or a shipper desk, not the small owner.
- The check call is a pain, but public proof is weak.
- What is left after GPS/FASTag is status and reasons, not location.

Scores: **buildability 4/5, business 2/5, AI/ML share about 70%**. The CS member who has built LLM apps leads. The work is mostly integration; there is no hardware or bio role.

---

## F4 Drawing-to-quote for small machine shops

Overlap: loose, with factory operations (not food, not CCTV).

### 1. The problem in one paragraph
- **How quoting works.** A small machine shop gets enquiries as a PDF or a WhatsApp photo of a 2D drawing. The owner reads dimensions, tolerances, material and finish, estimates machine time in his head and replies with a price, often a day later. That costs orders and margin.
- **Rates.** Indicative Indian job-work rates: **CNC turning Rs 400–1,200 an hour, 3-axis VMC Rs 600–1,800, 5-axis Rs 1,800–5,000** (Trade4Asia, undated, https://www.trade4asia.com/suppliers/cnc-vmc-job-work, snippet). IndiaMART asking prices run as low as Rs 300–600 an hour.
- **Funded analogue.** Pre6 (Peak XV Surge 11, 25 Sep 2025) automates drawing reading, ballooning and costing for large suppliers (SKF, L&T Valves, Rane per its site) (R4-05 entry 12).
- **Size.** The number of Indian MSME machining units is NOT FOUND here (assigned to C1).

### 2. How the system works
```
photo/PDF of drawing -> deskew + dewarp (OpenCV) -> detect regions (views, dimensions,
   GD&T frames, title block, notes) -> read each region -> feature list JSON
   [Ø25 h7, L 80 ±0.1, M10x1.5 thread 15 deep, Ra 0.8, material EN8, qty 200]
 -> owner verifies on screen: each callout boxed on the image, tap to fix (60-90 s)
 -> process planner: stock size + allowance -> material kg x rate
    features -> operations (face, turn, drill, tap, mill pocket, grind if Ra<0.8 or IT6)
    each op time = volume removed / MRR(material, tool) + approach; setup / batch qty
    tolerance and finish multipliers; outsourced ops (heat-treat, plating) as fixed lines
 -> machine-hour rate (shop's own) x time + material + overhead + margin
 -> quote PDF + WhatsApp text (English/Hindi); saved for later calibration
```

### 3. The AI/ML core
- **Reading, and why not just ask a frontier model.** Khan et al. (arXiv 2411.03707, Nov 2024, opened) tested 400 expert-annotated drawings. A **fine-tuned Florence-2 (0.23B parameters) beat zero-shot GPT-4o and Claude-3.5-Sonnet by 52.4% relative F1 and cut hallucinations by 43%**. Zero-shot frontier VLMs therefore misread or invent dimensions. The same group's pipeline (arXiv 2505.01530, IEEM 2025, opened) uses **YOLOv11 oriented boxes over nine categories (GD&T, general tolerances, measures, materials, notes, radii, surface roughness, threads, title blocks), then a fine-tuned Donut parser into JSON**. It reports **GD&T precision 94.77%, F1 97.3%, hallucination 5.23%**, on an in-house dataset that is not public.
- **Tonight's choice.**
  - Run a frontier or open VLM (**Qwen2.5-VL-7B** locally, or an API model) **per cropped region**, not per whole sheet. Cropping is what the published pipeline shows works.
  - Detect regions with a YOLO11-OBB trained on 15–20 drawings annotated by hand in Roboflow or CVAT over the night (about 300 boxes), or simply ask the VLM for region boxes.
  - The human verification screen is mandatory, because about 5% hallucination is fatal on a price.
- **Data.**
  - Public: NIST's MBE PMI test-case drawings, which have known ground truth (availability NOT CHECKED), and textbook machine-drawing exercises.
  - Collected: photos of 5–10 real drawings from shops in HSIIDC Kundli/Rai, with permission.
- **Costing ML.** First a transparent rules model (MRR tables from machining handbooks). Then per-shop calibration: gradient boosting or ridge regression from rule-estimated time to the owner's past quoted price, using 30–50 historical quotes. This learns the shop's own multiplier for difficulty, customer and urgency.
- **What it cannot do.**
  - Infer a 3D shape from incomplete views.
  - Read badly photographed or hand-sketched drawings reliably.
  - Know the shop's fixture situation or machine availability.
  - Price market-driven factors.
  - The quote is a draft for the owner, never auto-sent.

### 4. Why India needs its own version
- **Customer.** A 10–50 person shop with 3–15 machines, not a tier-1 supplier with ERP and PPAP teams.
- **Input and output.** WhatsApp photos, not CAD models. Output in rupees, in the owner's words.
- **Price.** Rs 1,500–2,500 a month, not enterprise SaaS.
- **Language.** Hindi/Marathi UI for the owner. Drawings themselves are in English with ISO/IS conventions.
- **Kept from Pre6:** drawing reading, feature extraction, costing. **Changed:** the phone-photo input, rule-plus-calibration costing for one shop, and a WhatsApp quote. Ballooning, PPAP and DFM are dropped.

### 5. Who has tried, and the gap
- Pre6 (Indian, large suppliers).
- Global instant-quote platforms (Xometry, Protolabs, and India's own Zetwerk-style marketplaces) quote from 3D CAD for their own network, not for an independent shop.
- CAD-based costing tools (aPriori and others) are enterprise-priced (NOT CHECKED).
- The gap: a quoting assistant the shop owns, working from 2D photos. Whether Pre6 moves down-market is the main threat.

### 6. The business
- Buyer: the shop owner. Today: his own evening hours, or an estimator at Rs 25–40 thousand a month, and lost enquiries (ASSUMPTION).
- Price: Rs 2,000 a month.
- Arithmetic:
  - ASSUMPTION: about 60,000 small CNC job shops in India (NOT FOUND).
  - 5% adoption = 3,000 x Rs 24,000 = **Rs 7.2 crore ARR**.
  - 20% = **Rs 29 crore**.
  - Value check: if faster quotes win 2 more orders a month at Rs 20,000 revenue and 20% margin, that is Rs 8,000 a month against a Rs 2,000 price.
  - Upside: the same reading engine sold to buyers' sourcing teams, who receive quotes from many shops.
- First ten: shops in HSIIDC Kundli, Rai and Barhi (Sonipat), Faridabad and Ludhiana clusters. Then IMTMA or local industry-association members.

### 7. What a team could show by noon
- **Core, certain to work.**
  1. 10 drawings (5 turned shafts and bushes, 5 milled brackets and plates), photographed at an angle with a phone and also rasterised from PDF.
  2. Region crop, then VLM read, then the verification UI, then rule costing with an editable rate table, then a quote PDF and WhatsApp text.
- **The one honest number.** **Callout-level exact-match accuracy** (value plus tolerance plus unit all correct) over about 150 callouts on the 10 drawings, PDF raster against phone photo.
  - Baselines: (a) the whole-sheet zero-shot VLM; (b) PaddleOCR plus regex.
  - Also report the minutes a human needs to correct a sheet.
- **Second number, only if a local shop will talk by phone during the night or morning.** Our estimate against the shop's real quote for 3 parts, as percentage difference. Present it as an anecdote, not accuracy.
- **Fallback.** PDF-only input and hand-entered features feeding the costing engine.

### 8. Parts and cost
Software only. Printed drawings to photograph: about Rs 50.

### 9. Three hard questions
1. *"Owners quote by gut and relationships. Will they trust a machine price?"* They should not trust it blindly, and the product does not ask them to. It reads the drawing so they don't have to, shows the time breakdown, and learns their own multiplier from past quotes. Whether they adopt it is untested; 10 shop interviews come first.
2. *"5% hallucination on dimensions means a wrong price. How do you stop that?"* Every callout is boxed on the image for a one-tap check. Values are cross-checked: dimensions must chain to the overall length, and a tolerance class must match the IT table. Nothing goes out without confirmation.
3. *"Isn't costing the hard part, not reading?"* Yes. Rule-based machining time is accurate to perhaps ±30% across shops (ASSUMPTION, not measured). Per-shop calibration on past quotes is what tightens it, and that needs 30+ past quotes from each shop.

### 10. Risks and what would kill it
- Shops sharing customers' drawings may break NDAs, so it needs on-device or Indian-region processing.
- Low willingness to pay.
- Pre6 or a marketplace offering free quoting to capture shops.
- Kill test: 10 shop owners shown the demo; fewer than 3 send past quotes for calibration.

### 11. Verdict
Resolve answered:
- **Reading:** zero-shot VLMs are not good enough; cropped, region-wise reading plus human verification is, with published F1 of about 97% for a fine-tuned detector plus parser.
- **Quoting today:** by owner judgement from WhatsApp drawings.
- **Defensible costing:** feature-to-operation rules with MRR, plus per-shop regression calibration.

Scores: **buildability 4/5, business 3/5, AI/ML share about 60%**. The CS vision member leads; a mechanical- or hardware-minded member writes the costing rules.

---

## NOT CHECKED

- Malaria Screener patient-level field results (Malar J 2023, Sudan, 190 patients): page did not load.
- Share of India's 18.17 crore malaria tests done by microscopy versus RDT (2024). Use of JSB versus Giemsa stain in programme labs. Programme cross-checking rules for negative slides. Number of malaria microscopy points. CDSCO class for diagnostic-support software.
- SolDef_AI image count and benchmark figures (paper returned 403). DeepPCB and PKU-PCB sizes and PatchCore MVTec AUROC are from memory. Prices of Chinese desktop AOI. Current count of Indian SMT lines; the 1,330–1,350 figure is 2018 and a snippet.
- India's mean consult length from Irving et al. 2017 (full text 403). NMC generic-prescription rule status. DPDP Rules status. The Indian medicine-brand dataset on Kaggle. Licence of Eka Parrotlet weights.
- Per-km leak-survey rates in municipal tenders (search found none). Commercial noise-logger and correlator prices. A national figure for urban hours of supply.
- IRDAI Master Circular wording on citing the clause in a repudiation (only secondary sources). The IRDAI non-payable items list and standard exclusions. Format and availability of Insurance Ombudsman awards. ClaimBuddy, IHX and Vitraya, whose status rests on a single deck.
- TRAI category for automated service calls. Licences of Bolna's open-source framework and Pipecat. Count of fleets with 10+ trucks.
- Count of Indian CNC job shops. NIST MBE PMI drawings availability. aPriori pricing.
- Local part prices (estimates only).

Searches used: 25
