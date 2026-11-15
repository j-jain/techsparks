# R5-design-02  (agent: Opus, date 2026-11-12)

Scope: design for P1, P2, P3, P4, P5, F7, F1 (assignment D2 in `T4-triage.md`). Problem facts reused from `R4-03 Proptech India.md` and `R4-04 Funded - YC and a16z.md` keep their original URLs and tags. New facts carry a URL and date; "(opened)" means I read the page or PDF, "(snippet)" means search-result text only. Market sizes marked "assumption" are my own inputs, shown so the reader can change them. Search budget: 30; used 26.

Three findings change the shortlist and should reach the report:
1. **Cartosat-3 sub-metre imagery is cheap and free to government.** NRSC/NSIL price list: Cartosat-3 PAN 0.28 m, 17 km x 17 km scene, Rs 3,860 (Geo Orthokit) or Rs 4,810 (ortho) for non-government users; free for government entities; urgent delivery +50%; 100% advance payment through an NSIL ordering account. https://ibm.gov.in/writereaddata/files/17210395936694fae952c70Commercial_Products_Ordering_Bhoonidhi_Thr_NSIL_Interface_FA.pdf (FAQ dated 26 Apr 2024, opened). That is about Rs 13–17 per sq km, so imagery cost does not limit P1 or P5. A student team cannot get it overnight, though: you need an ordering account and payment first.
2. **F7's core does not survive in Haryana.** HSVP's OBPAS already gives the architect a free scrutiny engine before submission. It parses the drawing, checks setbacks, FAR, coverage and height against the Haryana Building Code 2017, and marks each parameter pass or fail. https://obpas.hsvphry.org.in/docs/UserManual_AA.pdf (undated manual, opened). AutoDCR cities have a PreDCR add-in that does the same job.
3. **P3 overlaps Landeed almost completely.** Landeed already sells banks 30+-year chain-of-title reports signed by its own advocates, plus AI go/no-go screening. https://www.landeed.com/banks-and-nbfcs (undated, opened).

---

## P1 Finding untaxed and unauthorised construction from imagery (one engine, two buyers)

### 1. The problem in one paragraph
Property tax is a city's largest own revenue. Registers, though, go years without revision, and nobody records new floors, sheds and changes of use. In Nagpur's Laxmi Nagar pilot, AI mapping produced 9,000 property entries. About 2,000 were new constructions and 7,000 had changes not in the civic record. Inspectors checked 380 at random and found 12 wholly new buildings and 215 major alterations, so 59% of the checked parcels had changed. City arrears exceed Rs 900 crore. https://www.nagpurtoday.in/nmc-to-launch-ai-based-property-survey-after-nine-years-to-boost-tax-revenue/ (29 Oct 2025, opened). Enforcement faces the same gap. The Defence Estates tool on Cartosat-3 detected 1,133 unauthorised changes, and officials acted on 570. https://pib.gov.in/PressReleasePage.aspx?PRID=1839200 (2022, snippet). The same change detector serves two buyers: the tax wing, which wants a list ranked by rupees, and the enforcement wing or development authority, which wants a list of changes with no matching permission.

### 2. How the system works
```
Imagery date A + date B (Cartosat-3 0.28 m / drone ortho) ─┐
Open building footprints (Google Open Buildings v3) ────────┤→ co-register → footprint + change model
Tax register (property ID, address, plot, built-up, floors) ┤→ geocode / parcel join
Approved-plan list (for enforcement) ───────────────────────┘
        ↓
Per parcel: new structure? footprint grew by x m²? new rooftop structure? height change (shadow)?
        ↓
Tax gap estimate = Δ built-up m² × unit area value × rate   |  Enforcement: change with no permission on file
        ↓
Ranked inspector list → field app (photo + verdict) → verdicts become training labels
```
The inspector sees a map with numbered parcels, a before/after slider, and an estimated rupee gap or a "no permission found" tag. The inspector visits the top of the list first and records "confirmed / not a change / already assessed". Nagpur's 380-parcel check is exactly this kind of label set.

### 3. The AI/ML core
- **Model family:** bi-temporal Siamese change detection. Use **BIT** or **ChangeFormer** from **Open-CD** (open-mmlab, https://arxiv.org/pdf/2407.15317), with checkpoints pretrained on **LEVIR-CD**: 637 image pairs, 1024 x 1024 px at 0.5 m, building change labels. Published F1 on LEVIR-CD: BIT 89.3, ChangeFormer 91.1 under one fixed protocol (https://arxiv.org/html/2402.06994v2, "A Change Detection Reality Check", 2024, snippet), and 90.7 / 91.1 in Open-CD's tables (snippet). That paper's point is that simple U-Net baselines come close to these models, so a team need not chase the newest architecture. Per-date footprints come from **Google Open Buildings v3**: 1.8 billion polygons, India included, CC-BY-4.0, with a confidence threshold per S2 cell for 90% precision. https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_Research_open-buildings_v3_polygons (snippet). **SAM / segment-geospatial** can refresh footprints on new tiles.
- **Free change signal for a first pass:** **Open Buildings 2.5D Temporal** gives annual rasters for 2016–2023 of building presence, fractional counts and height. The effective resolution is 4 m, from Sentinel-2. India is covered. Height MAE is 1.5 m, but Google evaluated it only in North America, Europe and Japan. Google also warns that detections "are not always stable" year to year and that tiny or touching buildings merge. https://sites.research.google/gr/open-buildings/temporal (undated, opened). Use it to find new buildings from 2016 to 2023. It cannot find new floors, and it stops at 2023.
- **Imagery: what is available and what it can see**

| Source | GSD | Cost | Revisit / dates | Sees | Cannot see |
|---|---|---|---|---|---|
| Sentinel-2 | 10 m | free | ~5 days | cleared plots, large new blocks (≥ ~30 x 30 m) | single houses, sheds, floors |
| Open Buildings Temporal | 4 m effective | free | annual, 2016–2023 | new building presence, coarse height (1.5 m MAE, not validated in India) | added floor reliably, anything after 2023 |
| Esri World Imagery Wayback / Google Earth Pro history | ~0.3–0.6 m in Indian cities | free to view; licence bars commercial use | irregular, often 1–2 dates a year | demo-grade before/after | use in a paid product |
| Cartosat-3 PAN (NRSC/NSIL) | 0.28 m (0.45 m pan-sharpened) | Rs 3,860–4,810 per 289 km² scene; free to government entities | archive plus planning requests (not priced; feasibility decided by NRSC) | new building, footprint extension of a few m², new tin shed or rooftop room, shadow-length height | interior use, a floor added to a building in a dense row where shadows fall on neighbours |
| Drone ortho + oblique (2–3 cm) | 2–3 cm | survey contract | on demand | added floor, terrace room, signboards (a hint of commercial use) | interior subdivision |

  Cartosat source: NRSC/NSIL FAQ above (26 Apr 2024, opened). A new floor is the hard case. From nadir, a 3 m floor shows only as longer shadows. At a sun elevation of 45°, a 3 m rise lengthens the shadow by 3 m, about 11 px at 0.28 m. That is measurable on a detached house facing open ground, and lost in a dense row of houses. Expect low recall on added floors from satellite. Floors and use need a drone or street-level photos.
- **Indian data:** LEVIR-CD comes from US cities, so expect a clear drop on Indian rooftops: water tanks, stair rooms, tarpaulins, construction material on roofs. Fine-tune on 200–500 labelled Indian tile pairs, which a team can label in about two days with a polygon tool. Inspector verdicts become a growing label set.
- **What the model cannot do:** decide legality, ownership or tax liability; see use changes from the air; separate a tarpaulin from a roof; avoid false changes from off-nadir lean on tall buildings, so co-register and ignore thin edge changes; join a parcel to a register entry with no geocode. That join is often the larger error source. Treat the output as a ranked visit list, never an assessment.

### 4. Why India needs its own version
The buyer is a municipal commissioner or a development authority, not a county assessor buying a US-style aerial subscription. Indian government entities get Cartosat-3 0.28 m imagery free (NRSC FAQ above), which no foreign vendor has built a product on. Registers are spreadsheets with free-text addresses in English, Hindi or Marathi, so the work is record linkage as much as vision. Payment is per property surveyed. Delhi MCD capped a drone plus door-to-door survey of about 30,000 industrial-area properties at Rs 3 crore, about Rs 1,000 per property. https://www.prithviestates.com/?p=139133 (15 Mar 2023, opened). MCD's 2026 ward pilot was at zero cost to MCD (R4-03, ThePrint, 2 Jun 2026, snippet). Drone surveys need DGCA zone checks. Draft-rule summaries say the yellow zone shrank from 45 km to 12 km around an airport perimeter, and nano drones (≤ 250 g) need no UIN outside restricted zones. https://www.drishtiias.com/daily-updates/daily-news-analysis/draft-drone-rules-2021 (Jul 2021, snippet; verify on the Digital Sky map).

### 5. Who has tried, and the gap
ORSAC with Vassar Labs runs BLUIS on Planet SkySat in Bhubaneswar (R4-03, snippet). DGDE built its tool in-house with BARC on Cartosat-3. GHMC, Pune, Navi Mumbai (LiDAR) and Solan ran one-off surveys through agencies (R4-03). Tenders price work "per property" (GeM listings for UP ULBs; Surat geo-tagging tender closed 5 Feb 2026, https://tenderdekho.com/tender-detail/surat-municipal-corporation-geo-tagging-property-tax-survey-tender-td-266688, snippet; a 2026 Tauru, Haryana property-survey tender, https://www.publicservicesmap.in/tenders/2026-tauru-property-survey--hry-2026-hry-515100-1, snippet). The gap: every city buys a one-off survey that is stale within two years. Nobody found sells a recurring change alert that reuses free government imagery across many cities.

### 6. The business
- Buyer and price today: about Rs 1,000 per property for drone plus door-to-door (MCD 2023). The product sells as a yearly change-alert subscription at **Rs 10–20 per property per year**, plus an optional recovery-linked fee.
- Bottom-up (assumptions labelled): the 100 largest ULBs × an average 3 lakh assessed properties = 3 crore properties (assumption). At Rs 15 per property per year that is **Rs 45 crore a year**. Enforcement buyers: 60 development authorities, cantonments and SRA-type bodies × Rs 30 lakh a year = **Rs 18 crore**. Ceiling about **Rs 60–65 crore a year**. A recovery share is larger per city: if alerts add 2% to a city collecting Rs 500 crore, that is Rs 10 crore, and a 5% share is Rs 50 lakh a year from one city. Cities rarely sign such contracts.
- Verdict on the business: a real but government-paced B2G company. It is also a natural module for an existing GIS survey firm.
- First ten customers: Nagpur (NMC, pilot already run), MCD (pilot wards), GHMC, PMC/PCMC, NMMC, Greater Chennai, GDA Ghaziabad (comparing imagery with approved maps), Mumbai SRA (imagery tender), DGDE / cantonment boards, and a Haryana ULB near the event (Sonipat or Tauru).

### 7. What a team could show by noon
- **Prototype (certain to work):** an area of interest covering the Ashoka campus plus Rai and Kundli, about 25 km². Export two Esri Wayback dates (for example 2019 and the latest) as 0.5 m tiles. Run a pretrained Open-CD BIT checkpoint, and overlay Open Buildings v3 footprints and the 2016→2023 Temporal presence change. Build a mock register of 150 parcels from footprint IDs with 30 deliberately stale entries (floors or built-up area understated). Show a ranked Leaflet map with a before/after slider and an "inspector" form.
- **The one number:** precision@50, the share of the top 50 flagged parcels that are real building changes. Two team members label all candidates blind on the newer image; report agreement as Cohen's kappa. Baseline: rank by Open Buildings Temporal presence change alone, and by random order. Recall comes from 100 randomly sampled parcels labelled the same way. Ground-truth five campus or Rai structures on foot with timestamped photos. Typical claim: "precision@50 = 0.xx vs 0.yy for the free baseline".
- **Fallback:** if the pretrained model fails on Indian roofs, difference the footprint masks (SAM on each date) and rank by area gained.

### 8. Parts and cost
Software only. Optional: a borrowed nano drone (≤ 250 g) for one oblique pass over a campus building to show floor counting, only if the Digital Sky map shows green and the campus permits it.

### 9. Three hard questions and honest answers
1. *"Cities already hire survey agencies. Why you?"* They hire one-off surveys at about Rs 1,000 per property, and the result goes stale. We sell the re-survey as a cheap recurring diff on imagery that is free to them. The honest weakness: the door-to-door step, the register join and the notice stay manual.
2. *"What precision on dense Indian housing?"* Unknown until fine-tuned. LEVIR-CD's ~90 F1 is for US suburbs. Nagpur's check found 59% of sampled parcels changed, so even a modest model beats random visits. Added floors from satellite will have low recall. Say so, and add drones for the top decile.
3. *"Who pays and when? MCD's pilot paid vendors nothing."* That is the real risk. Pilots are free, and paid scale means a tender. A recovery-share contract needs a commissioner willing to sign one. Expect 12–18 months to first revenue.

### 10. Risks and what would kill it
Reassessment is politically toxic before municipal elections. Registers may be unavailable or ungeocodable. Free viewers' imagery cannot be used commercially. Cartosat ordering is slow. Defamation risk if a false "unauthorised" flag leaks. A large GIS incumbent bundling the same feature into every survey tender would kill it.

### 11. Verdict
Buildability overnight **4**. Business **3**. AI/ML share **~60%** (change detection, footprint segmentation, register matching). Lead: the CS vision person, with whoever is comfortable with GIS (QGIS, Earth Engine).

---

## P2 Move-in and move-out condition report for rented flats

### 1. The problem in one paragraph
Tenants in Bengaluru and Mumbai routinely pay deposits of six to ten months' rent. At move-out, landlords deduct repainting and polishing that tenants call renovation for the next tenant. A widely shared Bengaluru case: Rs 1 lakh deposit, Rs 80,396 deducted, Rs 19,604 returned. https://www.businesstoday.in/latest/trends/story/rs1-lakh-deposit-rs19604-returned-bengaluru-tenant-alleges-massive-deduction-by-landlord-542774-2026-07-14 (14 Jul 2026, opened). Owners in six metros hold an estimated **Rs 1,26,042 crore** of security deposits (NoBroker Rent Report 2026 via Business Today, https://www.businesstoday.in/personal-finance/story/rs1-26-lakh-crore-in-rental-deposits-how-verified-data-could-transform-indias-housing-market-553799-2026-09-08, 8 Sep 2026, snippet). Neither side has a neutral record of the flat's condition on day one.

### 2. How the system works
```
Move-in: guided capture per room (fixed checklist: 4 walls, ceiling, floor, doors, windows, fixtures, appliances)
         → timestamped, hashed photos + short video → both parties confirm by OTP → PDF baseline
Move-out: app shows the move-in photo as a ghost overlay → tenant matches viewpoint → capture
         → align each pair → change regions → classify (damage / wear / not a change) → price from rate card
         → itemised deduction proposal with photo evidence and the policy clause → both accept or dispute
```
The tenant and landlord each see a two-page report. On it: a list of changes, each with before/after crops and a label ("new damage: hole in plaster, 4 cm"; "wear: paint fading, not chargeable after 2 years"; "not a change: lighting"), and a suggested amount with the rate used.

### 3. The AI/ML core
- **Alignment:** SuperPoint + **LightGlue** (open, https://github.com/cvg/LightGlue) feature matching and a homography per wall (walls are planar), with a fallback to LoFTR. The ghost overlay at capture time does most of the work; alignment fixes the rest.
- **Change regions:** the absolute difference after photometric normalisation, followed by morphology. A Siamese change net is optional; at this scale simple differencing on aligned planar images is enough and easier to debug.
- **Labelling the change:** an open VLM (**Qwen2.5-VL-7B-Instruct**) or a Gemini/Claude API. It gets the two crops and a fixed taxonomy: hole, crack, stain, burn, broken or missing fixture, scratch on floor, paint scuff; wear (fading, light scuffs, picture-nail holes where policy allows); not a change (shadow, reflection, moved furniture). For cracks, a YOLOv8-seg model trained on public crack sets (Crack500; SDNET2018, ~56,000 concrete images) helps. Those sets are concrete, not painted plaster, so treat them as a weak prior.
- **Published accuracy:** I found no benchmark for indoor damage-versus-wear classification (NOT FOUND). Any accuracy number must come from the team's own test.
- **Data tonight:** hostel rooms with staged, reversible changes. Removable "stains" (washable marker on tape), chalk "cracks", a stick-on "hole", a removed bulb or switch cover, a moved chair, curtains and lights changed as distractors.
- **What the model cannot do:** decide whether a mark is "normal wear". That is a contract and policy rule (age of paint, length of tenancy), so the system applies a written rule table on top of the vision label. It also cannot see inside walls (seepage behind paint), judge hidden plumbing, or stop a landlord who simply refuses to pay.

### 4. Why India needs its own version
Deposits are far larger than in the West: 6–10 months' rent versus about one month. The Model Tenancy Act's two-month cap applies only where a state has adopted it, and not in Karnataka (R4-03, snippet). Disputes go to WhatsApp, legal notices and consumer forums, not small-claims deposit schemes. So the report must be shareable on WhatsApp, available in Kannada, Hindi and Marathi, and work on a Rs 10,000 Android phone. The capture-and-checklist part already exists in India: RentOk sells digital move-in and move-out checklists with photo uploads and pitches them for dispute avoidance (https://wb.rentok.com/?p=4194, undated, snippet). For PG and co-living, consumer guides say agreements allow deductions only for dues and genuine damage beyond wear, and complain that branded operators deduct through apps with no breakup. https://righttoinformation.wiki/practical-guides/pg-coliving-security-deposit-not-returned-refund-guide (2026, snippet).

### 5. Who has tried, and the gap
NoBroker (unicorn; agreements, rent payments), RentOk (checklists), co-living operators' own move-out apps. In the UK, "inventory clerk" software is standard (not checked this round). The gap: nobody produces an automated, neutral **diff with a price**. The capture is a commodity; the comparison and the itemised, rule-based deduction are not.

### 6. The business
- Resolve, product or feature: **a feature.** The capture already exists in RentOk, and the natural owners are rental platforms and co-living operators who control both move-in and move-out.
- Bottom-up (assumptions labelled): Rs 1,26,042 crore ÷ an average deposit of Rs 1.5 lakh (assumption) ≈ 84 lakh tenancies in six metros. With a two-year average tenancy (assumption), that is ≈ 42 lakh move-outs a year. B2C at Rs 299 per move-in/move-out pair with 3% uptake = 1.26 lakh × 299 = **Rs 3.8 crore a year**: not a company. B2B API at Rs 75 per move-out across platforms and operators reaching 20% of move-outs = 8.4 lakh × 75 = **Rs 6.3 crore a year**: a decent feature licence.
- A company appears only if the report anchors a financial product: deposit-free renting or deposit insurance, where the report is the underwriter's claim evidence and the money is in the premium or float. That is a fintech, not a vision company.
- Best first buyer: **co-living and PG operators.** They run hundreds of move-outs a month, staff handle every dispute, and they control the app. Then managed-rental firms, then NoBroker-type platforms as a licence. First ten: five large co-living and PG chains in Bengaluru, Gurugram and Pune; two student-housing operators near campuses (including Sonipat's Education City); RentOk and one rental platform as API partners; one deposit-insurance product as a pilot partner.

### 7. What a team could show by noon
- **Prototype:** an Android web app (PWA) with a guided room checklist and ghost overlay, a Python backend running LightGlue alignment, differencing and VLM labelling, and a PDF report.
- **Test protocol:** 10 hostel rooms. Teammate A captures move-in. Teammate B, blind to the plan, stages 0–4 changes per room from an 8-type list (30 real changes in total) and 3 distractors per room (30 in total: lights, curtains, a moved chair). Teammate C captures move-out using the overlay. **Measured number:** detection recall on the 30 real changes, plus false alarms per room on the 30 distractors, with label accuracy (damage / wear / no change) on the detected ones. **Baseline:** the same VLM given the two unaligned photos with no differencing. Expect alignment plus differencing to cut false alarms sharply; that gap is the result.
- **Fallback:** if alignment fails on blank walls, ask for fixed-position shots (four corners of each room) and compare per shot.

### 8. Parts and cost
Software only, plus phones. Props: painter's tape, washable markers, chalk, sticky notes (under Rs 300).

### 9. Three hard questions and honest answers
1. *"Why would a landlord agree to a neutral report?"* Many will not. That is why the buyer is the operator or platform, which imposes the process. B2C landlord adoption will be low.
2. *"Does the report have legal standing?"* Only as evidence both parties signed. Electronic records need the usual certificate in court. Its real value is ending most disputes before they reach a notice.
3. *"Isn't this a feature for NoBroker or RentOk?"* Yes. Build it as a licensable module or as the evidence layer of a deposit product. Do not pitch it as a standalone company.

### 10. Risks and what would kill it
Privacy (photos of lived-in rooms; store on the operator's side, blur faces and documents). Platforms building it in-house in a sprint. Wear-versus-damage rules contested by both sides. Low-quality phone captures in dim rooms.

### 11. Verdict
Buildability overnight **4**. Business **2** standalone (3 as a module of a deposit product). AI/ML share **~55%**. Lead: the CS vision person; a web person builds the capture flow.

---

## P3 Chain-of-title reader for sale deeds in Indian languages

### 1. The problem in one paragraph
A sale deed is registered, but registration proves execution, not ownership (https://webiis08.mondaq.com/india/real-estate/1727536/registration-is-not-ownership-why-a-sale-deed-is-only-the-beginning, snippet). A buyer or lender must trace 13–30 years of deeds, mutations and encumbrances, mostly scanned and in the state language. Digitised land records also disagree with the base registers. Telangana's Dharani lists about **32.80 lakh acres** under base survey numbers in certain districts against **26.98 lakh** in the Sethwar registers, about 6 lakh acres of land that does not exist. https://deccanchronicle.com/southern-states/telangana/massive-discrepancies-identified-between-sethwar-and-dharani-land-records-1861663 (undated, snippet). Double registration is a live fraud: about Rs 15.26 crore at the Quthbullapur sub-registrar office. https://www.geosquare.in/hyderabad-real-estate-scandal-rs-1526-crore-fraud-through-double-registration-39138-news.html (2026, snippet).

### 2. How the system works
```
Inputs: scanned deeds (PDF/phone photos) + encumbrance certificate (EC) from the state portal + RoR / jamabandi / 7-12 extract
  → OCR (state language) → schema extraction per deed:
     {doc no, date, SRO, executants, claimants, survey/khasra no + sub-division, extent + unit, boundaries N/S/E/W,
      consideration, link (prior) document}
  → name matching across scripts (Telugu/Hindi ↔ English EC transliteration)
  → title graph: parcel nodes, deed edges seller→buyer with extent and date
  → rule checks → flags with evidence crops → "questions for the advocate" + chain diagram
```
Rule checks: (1) a missing link document, so the chain has a gap; (2) a seller selling before acquiring; (3) the sum of extents sold from a parcel exceeding the extent held (the Dharani-type phantom area); (4) two outgoing deeds from the same holder for overlapping extent (double sale); (5) boundaries that do not reconcile between successive deeds; (6) EC entries (mortgages, agreements) with no matching document in the file.

### 3. The AI/ML core
- **OCR is the bottleneck, and the numbers are now public.** Sarvam's Indic OCR Bench (20,267 block-level samples, documents from 1800 to the present, varying scan quality; vendor-run) gives word accuracy:

| Language | Sarvam Vision (API) | Gemini 3 Pro | Google Cloud Vision | Surya (open) | Gemma3-27B (open) |
|---|---|---|---|---|---|
| Telugu | 87.7 | 85.3 | 82.6 | 58.8 | 53.9 |
| Kannada | 89.9 | 87.4 | 85.5 | 68.1 | 46.0 |
| Marathi | 93.1 | 90.4 | 87.9 | 72.3 | 70.6 |
| Hindi | 95.9 | 95.1 | 90.9 | 81.9 | 85.6 |

  Source: https://www.sarvam.ai/blogs/Sarvam-vision (5 Feb 2026, opened). On the olmOCR-Bench "OldScan" category, Sarvam Vision scored 49.8, its weakest category (same page). Read plainly: open models are not good enough for Telugu or Kannada deeds. A hosted API reaches about 88–90% word accuracy on Telugu and Kannada and about 96% on Hindi. So 1 word in 8–10 is wrong on a southern deed, and a survey number or extent misread breaks the chain. Handwritten registers have no published Indian benchmark: do not claim them.
- **Extraction:** an LLM with a strict JSON schema (Claude or Gemini via API; Qwen2.5-7B-Instruct as the open option). Every extracted field gets a pointer to its bounding box so a lawyer can check it.
- **Error control by cross-checks, not model faith:** typed EC extracts (often in English) confirm document numbers and dates; extents must satisfy the arithmetic; and survey numbers must exist in the RoR.
- **Data:** no public labelled corpus of Indian deeds was found (R4-03, NOT FOUND). Tonight: build 20 synthetic deeds from a real published format, typed in Hindi (and five in Telugu if a team member reads it), with names and survey numbers invented. Print them, photograph them under poor light, and plant defects in three chains.
- **What the model cannot do:** give a title opinion; see unregistered GPA or agreement-to-sell transactions, court cases or family partitions not in the file; detect forged signatures or impersonation; read missing documents.

### 4. Why India needs its own version
Every state has its own portal, record names (pahani, jamabandi, 7/12, RoR-1B), units (acres-guntas, kanal-marla, sq yards, bigha) and language. Lenders pay a panel advocate for a search report plus title certificate, often charged to the borrower. Bandhan Bank's home-loan schedule caps "search report and TCC" at **Rs 5,000 per property** and valuation at Rs 5,000 + GST. https://bandhan.bank.in/sites/default/files/2026-07/Schedule-of-Charges-of-Home-Loan-and-LAP-03072026.pdf (3 Jul 2026, snippet). Bank guidance has fees paid through the bank, not directly by the borrower (SBI-era guideline, snippet in the same search). The buyer is the lender's legal department or its panel advocate, not the homebuyer.

### 5. Who has tried, and the gap (Resolve: where Landeed stops)
Landeed's bank page sells origination screening ("AI go/no-go"), approval diligence (RoR/EC, certified TSRs), 30+-year chain-of-title reports signed by advocates it employs "on our liability", EC and CERSAI monitoring and a portfolio dashboard. It shows HDFC Bank and Chola logos, relationship unconfirmed. https://www.landeed.com/banks-and-nbfcs (undated, opened). Directories put coverage at 20–24+ states and 120+ document types, with AI reports only in "select regions like Telangana" (https://www.toolmage.com/en/tool/landeed/, snippet). AdvaRisk (ICICI Bank / NABARD-backed, 14 states) sells an instant ownership check (R4-04, snippet). So the bank chain-of-title product is taken. The gaps left: (a) the thousands of independent panel advocates who still read deeds by hand and keep their own bank panels; (b) states and record types where Landeed's AI does not yet run, plausibly the Hindi belt's jamabandi and mutation (intkal) records; (c) plot buyers in peri-urban layouts before they pay a token amount.

### 6. The business
- **Resolve, who pays per search:** banks and NBFCs, through panel advocates, about Rs 3,000–5,000 per property (Bandhan cap above).
- Bottom-up (assumptions labelled): 30 lakh secured property loans a year, home loans plus LAP (assumption, NOT CHECKED) × Rs 4,000 = **Rs 1,200 crore a year** spent on title searches. Landeed's model takes the whole fee with advocates on payroll. An advocate tool takes a slice: Rs 300 per file × 10% of files = **Rs 9 crore a year**.
- Verdict: **as a standalone company against Landeed, it does not survive.** The smaller version that does: a **Hindi-first deed and jamabandi reader for panel advocates in Haryana and western UP**. It builds the chain, flags gaps and over-sales, and drafts the search-report annexure; the advocate signs. Hindi OCR is the strongest (~96%), Haryana records are online, and the event is in Sonipat. Sold per file or Rs 2,000 a month per practice. It could later be sold to, or partner with, Landeed or a lender.
- First ten customers: five panel advocates in Sonipat and Gurugram district courts; two small HFCs active in Haryana; one co-operative bank; one plotted-development broker; one title-insurance pilot.

### 7. What a team could show by noon
- **Prototype:** upload 6–8 deed images for one parcel → extracted table with evidence boxes → chain diagram (graphviz or d3) → flag list.
- **Test protocol:** 20 synthetic Hindi deeds forming 4 chains, three of them with planted defects (one gap, one over-sale of extent, one double sale), photographed at two qualities. **Measured number:** field-level exact-match accuracy on 8 key fields × 20 deeds = 160 fields, hand-keyed as truth, plus planted defects caught out of 3 with false flags counted. **Baseline:** open Surya OCR plus regex versus the API OCR plus LLM pipeline. This also reproduces the open-versus-API gap from the Sarvam table on the team's own data.
- **Fallback:** typed digital PDFs only (no photographs). The chain logic still demonstrates.

### 8. Parts and cost
Software only. API spend under Rs 1,000. A printer and phones.

### 9. Three hard questions and honest answers
1. *"Landeed has $15M+ and advocates on payroll. Why you?"* We would not fight them for bank contracts. The wedge is the independent advocate and the Hindi-belt record types, and an acquisition or partnership is the realistic exit.
2. *"What happens when OCR misreads a survey number?"* The chain fails visibly: the arithmetic and EC cross-checks flag it, and every field links to its image crop. Accuracy on a real southern deed is about 88–90% per word (Sarvam bench), so a human check is mandatory.
3. *"Liability if you miss a defect?"* The advocate signs and carries liability. The tool is a checklist and drafting aid. A US title-industry study found AI search on public records alone missed at least one meaningful matter in 40.8% of files (DataTrace, https://www.housingwire.com/articles/public-record-linked-ai-misses-key-title-issues-in-many-searches/, 2026, snippet; competitor-authored). So never sell it AI-only.

### 10. Risks and what would kill it
State portals adding captchas or blocking bulk access. Landeed moving downmarket with a free advocate tool. Personal data in deeds (DPDP Act obligations). Handwritten pre-1990 registers. Low willingness to pay among advocates.

### 11. Verdict
Buildability overnight **3** (4 on typed or synthetic deeds). Business **2** as stated (3 for the Haryana advocate tool). AI/ML share **~70%**. Lead: the CS/LLM person, with a Hindi reader on the team. A law student would help.

---

## P4 Phone scan of a new flat: true carpet area, snag list, valuer's annexure

### 1. The problem in one paragraph
At possession, buyers find seepage, hollow tiles and less carpet area than they paid for, and their leverage drops once they sign. MahaRERA has ordered refunds for carpet-area shortfall with a 3% variation cap (https://www.freepressjournal.in/mumbai/consumer-connect-maharera-mandates-refund-for-carpet-area-shortfall-within-3-variation-cap, Jun 2026, headline-only snippet; how the 3% band works is not confirmed). MahaRERA had received about 33,806 complaints, 6,224 pending (R4-03, snippet). Volume is large: housing completions in the top seven cities rose to about **5.19 lakh units in 2025**, and 2026 is projected at a record ~5.4 lakh. https://www.businesstoday.in/amp/personal-finance/real-estate/story/west-asia-conflict-puts-record-5-4-lakh-housing-deliveries-at-risk-in-2026-report-536279-2026-06-11 (11 Jun 2026, snippet, ANAROCK).

### 2. How the system works
```
iPhone Pro (LiDAR) → Apple RoomPlan scan per room → walls, openings, objects (CapturedRoom JSON / USDZ)
  → floor polygons per room; partition thickness = gap between adjacent room polygons
  → carpet area (RERA 2(k)) = Σ room floor areas + footprint of internal partitions − shafts; balconies and terraces listed separately
  → compare with the agreement's carpet area → shortfall % and rupee value (shortfall m² × agreed rate)
Snag module: photo per surface → crack / chip / tile-gap / paint detection + VLM description;
             tap-test audio per tile → hollow / solid; phone IMU → floor slope and wall plumb;
             optional thermal clip-on → damp-patch candidates
Output: PDF (a) buyer: plan, area table, snag list with locations, ready for the builder or RERA;
            (b) valuer: room dimensions, carpet area, condition grade, photos in the bank's annexure format
```

### 3. The AI/ML core
- **Geometry, not ML, carries the area.** RoomPlan (free iOS API, on-device) or the ARKit scene mesh with RANSAC plane fitting in **Open3D**. **Resolve: the RERA definition can be computed.** RERA s.2(k) carpet area is the net usable floor area, excluding external walls, service shafts, exclusive balcony or verandah and exclusive open terrace, but *including* internal partition walls (Act text, from memory; check the Act). A scan measures inner faces, so partitions must be added back: measure each partition's thickness (typically 100–230 mm) once, multiply by its length.
- **Accuracy (Resolve):** I found no peer-reviewed RoomPlan floor-area error figure. A TU Delft thesis on three offices against a terrestrial laser scanner reports "good overall accuracy" by Chamfer and Hausdorff distance, with errors in wall heights where the ceiling was not visible (https://3d.bk.tudelft.nl/ken/files/26_giorgos.pdf, snippet). Reviewers claim 1–3 cm on clean rooms (marketing-adjacent), and an Apple developer-forum user reports about 15 cm (https://developer.apple.com/forums/thread/712500, snippet). What matters: on a 3 m × 4 m room, a 1 cm error on each wall is ~0.6% of area, and 5 cm is ~2.9%, the size of the whole 3% tolerance. **So a LiDAR scan can settle a 3% dispute only if per-wall error stays near 1–2 cm.** The team must measure this (Section 7). The tool should report a confidence band and fall back to a laser distance meter for the decisive walls.
- **Phones with LiDAR:** iPhone 12 Pro / Pro Max through iPhone 17 Pro / Pro Max, and iPad Pro from 2020. Base iPhones and Android phones have none in current models. A few older Samsungs (S20+/Ultra, Note10+) had a ToF sensor, since dropped, and ARCore's Depth API is software depth with much larger error (from memory, not checked this round). **Fallback without LiDAR:** a Bluetooth or manual laser distance meter (±2 mm class) plus an in-app sketch, where the user taps a wall and enters or receives the reading. That is what PropCheck's engineers already do (below).
- **Snag models:** YOLOv8-seg fine-tuned on public crack data plus 100 self-labelled tile and paint photos; a VLM (Qwen2.5-VL or Gemini) to write the snag line ("hairline crack, 30 cm, above bedroom-2 window").
- **Tap test:** a small CNN or logistic regression on log-mel spectrograms (YAMNet/PANNs embeddings) separating hollow from solid tile. No published accuracy found for Indian floor tiles (NOT FOUND); measure it.
- **What it cannot do:** see seepage behind dry plaster (thermal shows only active damp with a temperature difference), test concrete strength or waterproofing, judge electrical safety beyond a socket tester, or give a legal area certificate.

### 4. Why India needs its own version (and what changes from Automax.ai)
Automax.ai keeps an inspector scanning with LiDAR, CV extracting 150+ attributes, AI choosing comparables and a licensed appraiser signing (R4-04, YC launch page). **Kept:** the phone scan → attributes → report pipeline, and the decision to be the service firm, not just software. **Changed:** India has no reliable comparables database (registered value versus real price; cash component), so drop AI valuation. The daily Indian fight is carpet versus super built-up area, which is a measurement problem. Banks cap valuation fees at about Rs 5,000 (Bandhan schedule above), so the valuer wants speed, not insight. iPhone Pro ownership is thin in India, so the scanner sits with an inspector or valuer, not the buyer. The incumbent is human: **PropCheck** claims 45,000+ inspections, 550+ projects and 500 pre-delivery inspections per city per month, with a thermal camera, laser meter, moisture meter and mallet. It "digitally measures" carpet area with a laser meter, runs its own snag platform SNAGR (also sold standalone) and gives builders 35% off retail. https://propcheck.in/b2b and https://propcheck.in/ (undated, opened). Earlier pricing: Nemmadi charged B2B Rs 2–5 per sq ft (https://yourstory.com/2019/07/nemmadi-home-inspection-startup-construction, Jul 2019, snippet).

### 5. Who has tried, and the gap
PropCheck, HousePedia (NCR), Nemmadi (Bengaluru), all human-led with software. On the lending side: Navanc (AI property score), AdvaRisk, Valocity. In the US: Automax.ai, ValueMate. The gap: an inspection that takes 4 hours with two engineers (Godrej guide, https://www.godrejvanantara.com/project-status/what-is-snagging-inspection-and-do-you-need-it.html, snippet) could take one technician 60–90 minutes, with area accuracy stated and an auto-generated report.

### 6. The business (Resolve: which buyer first)
- **Lead with the handover buyer, served through an inspection crew** (Automax's "be the firm" model). The carpet-area check turns into money: on a 700 sq ft flat at Rs 12,000 per sq ft, a 1% shortfall is Rs 84,000. A Rs 4,000–6,000 inspection is an easy sell at that moment. The valuer side is a second product: fees are capped and lenders care more about title than area.
- Bottom-up: 5.19 lakh completions (top 7, 2025) × 20% inspected (assumption) = 1.04 lakh × Rs 5,000 = **Rs 52 crore a year** of service revenue in the top seven cities alone. Pure software licensed to inspection firms: 1.04 lakh × Rs 300 = Rs 3 crore, so software alone is a feature for PropCheck. Valuer annexure: 30 lakh property loans (assumption) × 20% × Rs 150 = Rs 9 crore.
- First ten customers: buyers in three NCR projects nearing possession (via buyer WhatsApp groups and RWAs); two smaller inspection firms as software licensees; two empanelled valuer firms in Gurugram; one HFC's technical team; two developers wanting a pre-handover self-check (PropCheck's B2B segment).

### 7. What a team could show by noon
- **Prototype:** a Swift app (RoomPlan sample code) exporting CapturedRoom JSON → Python area and partition calculator → PDF. A web snag form with photo detection, a tap-test recorder, and an Android path with the laser-meter fallback.
- **Test protocol (the one number):** **mean absolute percentage error of room floor area**, RoomPlan versus a laser distance meter. 10 rooms (hostel rooms, a seminar room, offices, a common room with clutter) × 3 scans each by three different people = 30 scans. Truth: each wall measured twice with a laser meter at 10 cm above the floor; rectangles computed, irregular rooms triangulated. Report MAPE, the maximum error, and the share of scans within ±1% and ±3%. **Baseline:** one person with a 5 m tape (the DIY buyer's method) on the same rooms. If no iPhone Pro can be borrowed: test an ARCore measure app against the laser meter. That still yields an honest number, probably showing why LiDAR or a meter is needed.
- **Secondary (only if time):** tap test on 4 loose tiles over a gap versus 4 bedded tiles, 20 taps each, leave-one-tile-out accuracy.
- **Fallback:** the laser-meter workflow with app sketch and report generation (certain to work).

### 8. Parts and cost
- In a typical kit: none needed. A microcontroller is optional (no role).
- Bring or buy locally: an iPhone 12 Pro or later (borrow from a student); a laser distance meter (buy in a Sonipat hardware shop or by quick delivery; price not checked, budget Rs 1,500–4,000); a rubber mallet or screwdriver handle; 8 ceramic tiles + a sheet of plywood (~Rs 400); optional thermal clip-on (FLIR One / InfiRay class), borrow from an engineering lab.

### 9. Three hard questions and honest answers
1. *"Is phone LiDAR accurate enough to call a 3% shortfall?"* Only if per-wall error is ~1–2 cm, which is not published for RoomPlan. Our 30-scan test gives the number. Where the band straddles the threshold, the app asks for laser-meter readings on the decisive walls.
2. *"PropCheck has done 45,000 inspections. What do you add?"* Speed and a stated accuracy band, so one technician does in 90 minutes what two engineers do in four hours. Either license to them or undercut them in tier-2 cities. Honest: they could adopt RoomPlan themselves.
3. *"B2C acquisition at a one-time event is expensive."* Yes. Go through buyer associations of projects near possession (one RWA group brings dozens of flats) and through developers' pre-handover checks.

### 10. Risks and what would kill it
Liability for a missed defect or a wrong area; iPhone Pro dependence; developers refusing scanning before possession; incumbents adding LiDAR; RERA tolerances that make small shortfalls non-refundable (unverified 3% headline).

### 11. Verdict
Buildability overnight **5** (area test and report). Business **3** (as a tech-enabled inspection service; 2 as pure software). AI/ML share **~40%**: geometry dominates and the snag and tap models are smaller. Lead: an iOS-capable CS member, with a hardware member on the measurement protocol.

---

## P5 Independent construction-progress check for lenders and buyer groups

### 1. The problem in one paragraph
Homebuyers pay construction-linked instalments and lenders release tranches against progress the developer reports. When a project stalls, both find out late. ICRA counts about **1.56 lakh stalled units** in the top seven cities at Dec 2025 (https://www.icra.in/Rating/DownloadResearchSummaryReport?id=6814, Mar 2026, snippet). PropEquity counts about 5.08 lakh units in roughly 2,000 projects across 42 cities (R4-03, snippet). Lenders now have a rule to follow. The **RBI (Project Finance) Directions, 2025** (19 Jun 2025, effective 1 Oct 2025) require phased disbursement, "proportionate to the stage of completion", "certified by the Lenders' independent engineer or architect". https://www.azbpartners.com/bank/rbi-issues-directions-on-project-finance-for-all-regulated-entities/ (29 Jul 2025, opened). Whether that applies to every residential construction loan, or only to exposures under a common lender agreement, is not settled by the law-firm summary. AZB says it covers project-finance exposures where repayment comes from project cash flows; the CRE-RH treatment is NOT CHECKED.

### 2. How the system works
```
Per project: RERA registration (towers, floors, declared schedule, quarterly certificates)
Evidence stream, monthly:
  (a) satellite chip of the plot (Cartosat-3 0.28 m; one 289 km² scene covers many projects)
  (b) phone walk-round video from public roads / boundary on a fixed route (a buyer-group volunteer or a field agent)
  (c) drone pass where airspace and access allow
  → per tower: stage (excavation / foundation / superstructure n of N / masonry / facade / finishing / external works),
    slabs cast (count), crane present, facade netting
  → compare with the RERA-declared schedule and the developer's demand letter / disbursement request
  → report: % structure complete, months of slippage, "claimed slab 12, evidence shows 9", evidence crops with dates
```
The lender sees a portfolio watchlist: projects sorted by the gap between claimed and observed progress. A buyer group sees one project's monthly page.

### 3. The AI/ML core
- **Phone and drone (the main signal):** floor and slab counting on facade images. Fine-tune YOLOv8 to detect slab edges and floor bands on 300–500 labelled facade photos, and use a VLM (Qwen2.5-VL / Gemini) zero-shot as a second opinion and for stage labels. No published accuracy for floor counting on Indian under-construction towers was found (NOT FOUND). The team must measure it.
- **Satellite (portfolio screening, coarse):** stage classification on 0.28 m chips (ResNet/ViT fine-tuned on a few hundred labelled chips), crane detection, and height from shadow length: h = L × tan(sun elevation), with the elevation taken from scene metadata. Example: at a 50° sun, one 3 m floor adds ~2.5 m of shadow (~9 px at 0.28 m). Isolated towers on open plots, typical of NCR's periphery, can be measured to within about ±1 floor; dense cores and netted towers cannot. Open Buildings Temporal heights (1.5 m MAE, annual, ending 2023, not validated in India) are no use for monthly checks (https://sites.research.google/gr/open-buildings/temporal, opened). Sentinel-2 at 10 m shows only site clearing and footprints of large towers, never floors.
- **Imagery cost:** Cartosat-3 at Rs 3,860–4,810 per 17 km × 17 km scene (NRSC/NSIL FAQ, 26 Apr 2024, opened). Shared across 20+ projects in a scene, that is a few hundred rupees per project per month, if NRSC can deliver monthly over the area. Planning requests are unpriced and subject to feasibility (same FAQ).
- **What it cannot do:** see inside (MEP, finishes, quality, safety), detect a slab cast with weak concrete, see under netting or behind hoardings, or read whether money was diverted. It is evidence of physical progress only.

### 4. Why India needs its own version
The Indian buyer is unusual: thousands of retail homebuyers financing a project through instalments, plus NBFC and HFC construction lenders and SWAMIH (Rs 650 crore for SWAMIH 2.0 in Budget 2026–27, R4-03, snippet). RERA makes the developer's own architect, engineer and CA certify withdrawals from the 70% escrow account in proportion to completion (RERA s.4(2)(l)(D), from memory; check the text). India has a public, per-project declared schedule to test against, which most countries lack. But all of those certificates come from people the developer pays. Lenders already pay independent engineers (LIEs). ITCOT's list of LIE assignments at 31 Dec 2025 includes a residential and commercial project financed by Indian Bank (https://itcot.com/webroot/img/5.%20LIE%20Assignments%20%20with%20Project%20Cost-31.12.2025.pdf, snippet). LIE fees: NOT FOUND. Developers, not lenders, buy Track3D, Contineu and HUVIAiR.

### 5. Who has tried, and the gap (Resolve: do lenders already buy this?)
Yes, lenders buy progress certification, but from LIE and architect firms doing site visits, now required before each tranche under the RBI Directions. Track3D ($10M Series A), Contineu ($1.2M seed) and HUVIAiR ($3.2M Series A) sell site-capture platforms to developers (R4-03, snippets). The gap is neither the certificate nor the developer dashboard. It is **cheap, continuous, external evidence across a lender's whole book** between site visits, and an independent page for buyers of stalled projects, who have no access to the site.

### 6. The business
- Buyers: (1) LIE and architect firms, who use it to cut site-visit time and add dated evidence; (2) NBFC/HFC construction-finance risk teams, as a portfolio watchlist; (3) buyer associations of delayed projects; (4) RERA authorities checking quarterly declarations.
- Bottom-up (assumptions labelled): 5,000 actively financed under-construction projects nationally (assumption) × Rs 6,000 per project per month × 12 = **Rs 36 crore a year**. Buyer groups: 2,000 stalled projects (PropEquity) × 25% × Rs 50,000 a year = **Rs 2.5 crore**. Small. **Plainly: a feature for an LIE firm or a lender's risk platform, or the monitoring arm of a larger construction-finance data business.** Not a standalone venture at this size.
- First ten customers: two LIE or project-monitoring firms (ITCOT-type); three NBFC construction lenders active in NCR; SWAMIH's investment manager (SBICAP Ventures, from memory); two buyer associations of delayed Gurugram or Noida projects; Haryana RERA (HRERA) and one more RERA authority as a pilot.

### 7. What a team could show by noon
- **Prototype:** a phone-video upload → frame sampling → slab and floor counter (YOLO + VLM) → tower stage card → comparison with typed-in RERA data → monthly report PDF. Add a satellite tab showing an Esri Wayback time-lapse of 2–3 projects near Kundli and Sonipat (qualitative, labelled demo-only).
- **Test protocol (the one number):** **mean absolute error in floor count** on 20 buildings with known floor counts: Ashoka hostels and academic blocks (counts confirmed with facilities or by walking the stairs), plus visible under-construction towers near Rai and Kundli photographed from public roads, with truth counted by two people from close photos. Two views per building = 40 images. **Baseline:** zero-shot VLM count versus the fine-tuned YOLO slab detector versus a person counting from the same far photo. Report MAE and the share exactly right.
- **Fallback:** VLM-only counting with a human-in-the-loop confirm button. The comparison with RERA dates still demonstrates.

### 8. Parts and cost
Software only, plus phones. Optional borrowed nano drone, only where the Digital Sky map shows green and the site permits it. Not on private construction sites without written permission.

### 9. Three hard questions and honest answers
1. *"Lenders already pay an LIE. Why add you?"* The LIE visits a site periodically; we watch the whole book every month for a fraction of a visit's cost and tell the LIE where to go. Sell to the LIE, not around them.
2. *"Developers will block access."* Our evidence comes from public roads, satellite and buyers. That covers the structure (floors, facade), not interiors, and we say so.
3. *"Will a lender act on your report?"* Legally it is not a certificate. It is a trigger for a site visit or a covenant query, so the value is earlier warning. We need one lender to show a stalled project would have been flagged months earlier: a backtest on archived imagery of 10 known stalled projects is the first post-event study.

### 10. Risks and what would kill it
Small market; LIEs adopting phone apps themselves; Track3D-type firms adding a "lender view"; Cartosat delivery cadence; DGCA limits; defamation if a report on a named project is wrong.

### 11. Verdict
Buildability overnight **4**. Business **2–3** (feature unless it grows into construction-finance data). AI/ML share **~55%**. Lead: the CS vision person, with a hardware member on drone and phone capture.

---

## F7 Building-plan pre-check against one city's bye-laws

### 1. The problem in one paragraph
Small practices draw plans, submit them to the city's online system and get them back for revision. "A rejected building plan is almost never the end" (https://www.studiomatrx.org/guides/why-building-plans-get-rejected-india, snippet). Cities are automating scrutiny: BMC's AI "CivitTwin" pre-scrutiny, and DDA's single-window AI CAD scrutiny (R4-04, snippets). YC's Winter 2027 "AI for City Hall" request and Structured AI ($4.2M seed per ENR, 9 Jun 2026, via the YC page) show investors want code-checking (R4-04). No independent Indian rejection-rate figure was found (R4-04, NOT FOUND), so the proof is weak.

### 2. How the system works (and what already exists)
**Resolve: what the city gives the architect for free.** HSVP's OBPAS: the architect uploads drawings in the prescribed format. The system validates mandatory layers, and the architect "may also utilise the scrutiny engine before submitting to JE for official scrutiny". The engine "automatically parses drawing inputs and compares them with statutory limits as per the Haryana Building Code, 2017 … (setbacks, FAR, coverage, height, etc.)" and marks each parameter pass or fail. https://obpas.hsvphry.org.in/docs/UserManual_AA.pdf (opened). AutoDCR (SoftTech) cities have **PreDCR**, an AutoCAD add-in that creates the required layers in one click and "will highlight all the failed entities" (PreDCR manual on Scribd, https://www.scribd.com/document/426332462/PreDCR-HelpManual-AreaTable, snippet). **So a parameter pre-check already exists, free, wherever these systems run.** The pain that is left is the format. OBPAS: "All layers must be named and coloured as mentioned in the Annexure. Drawings made with different layer names and colours will not be scrutinised", and the same applies to text heights; the bounding rectangle and room labels (BEDROOM, KITCHEN, STILT PARKING …) are compulsory (same manual).

The surviving design, a **"layer fixer + feasibility" tool**:
```
Architect's own DWG/DXF (arbitrary layers)  → parse entities (ezdxf) → classify each entity/layer to the OBPAS schema
   (plot boundary, building footprint, floor plan per level, setback lines, room labels, parking, RWH) → rewrite layers,
   colours, text heights, close polylines, add the bounding rectangle → run a local HBC-2017 rule check (same parameters)
   → export a submission-ready DXF + a list of what the city engine will check
Separate front door: "What can I build on this plot?" — plot size, road width, zone → permissible coverage, FAR, height,
   setbacks under the code tables, before any drawing exists (for owners and small builders)
```

### 3. The AI/ML core
- **Entity-to-layer mapping:** a gradient-boosted classifier (LightGBM) on CAD entity features: layer name tokens, colour, entity type, closed or not, area, aspect ratio, containment, nearby text. An LLM maps free-text layer names ("WALL-NEW", "plot bdry") to schema classes. Training data: the team draws 10–15 plans in each style (their own layer names) tonight and labels by layer. That is weak supervision, but it is how firms actually draw.
- **Rule base:** Haryana Building Code 2017 and amendments. Third-party tables conflict on coverage and FAR (search summary of infralens.in and others, 2025–26, snippets), so rules must be keyed from the gazetted Chapter 6/7 tables by hand and versioned, not extracted by an LLM unchecked.
- **Raster plans (scanned or PDF):** floor-plan parsing models trained on CubiCasa5K (5,000 annotated plans, Finnish; https://arxiv.org/abs/1904.01920, not opened this round) transfer poorly to Indian hand or 2D CAD conventions. Out of scope for the night.
- **What it cannot do:** exercise discretion (approval is discretionary), check structural safety, fire NOC conditions beyond simple distances, or local zoning-plan exceptions; guarantee the city engine accepts the file.

### 4. Why India needs its own version
There is no single code. NBC 2016 and the Model Bye-Laws are templates and local bye-laws rule. Plans are 2D DWG, not Revit, so Structured AI's Revit and PDF clash checking does not transfer. Each city's portal defines its own layer grammar, and the state already does the scrutiny. **Kept from Structured AI:** a machine checking drawings against codes. **Changed:** the Indian value is meeting the portal's machine-readable format, and the buyer is a 1–5 person practice. India has about 1.05 lakh registered architects, ~85,000 with valid licences and ~65,000 practising (Construction World interview, https://www.constructionworld.in/latest-construction-news/real-estate-news/architecture-is-the-fastest-growing-profession/20805, undated, snippet).

### 5. Who has tried, and the gap
SoftTech (AutoDCR/PreDCR; Capterra lists a starting price of Rs 5,000, https://www.capterra.in/software/13186/autodcr, snippet); the state portals (OBPAS, BuildNow Telangana, BMC CivitTwin, DDA); Tagbin Brixx (text-to-3D design). No private architect-side tool surfaced (R4-04). The gap is small: layer conformance in cities without a PreDCR-like add-in, and plot feasibility for owners.

### 6. The business
- Bottom-up: 65,000 practising architects × 15% adoption × Rs 6,000 a year = **Rs 5.9 crore a year**. Owner-side feasibility as lead generation for architects: about Rs 1–2 crore.
- **Verdict: does not survive as a company.** It is a feature for SoftTech, the portal vendors, or a CAD plug-in seller. The YC thesis ("AI for City Hall") points to the *city* as buyer, and Indian cities already buy scrutiny from vendors. The more interesting version is selling **post-approval deviation checks** to cities: comparing the approved plan with what was built (P1/P5 imagery). That is a P1 extension, not F7.
- First ten customers (if built anyway): five small practices in Gurugram and Sonipat filing on OBPAS; two practices in a non-OBPAS Haryana ULB; one architecture college studio; one AutoDCR reseller; one plotted-colony developer.

### 7. What a team could show by noon
- **Prototype:** a DXF upload → layer-mapping → rewrite to the OBPAS schema → local rule check (setbacks, coverage, FAR, height) for residential plotted buildings → report.
- **Test protocol:** 12 residential plans drawn by three team members in their own layer styles, with 30 planted violations across them (short setbacks, excess coverage or FAR, height). **Measured numbers:** (a) the share of CAD entities mapped to the correct schema layer, against hand labels; (b) planted violations caught out of 30, with false flags counted. **Baseline:** a layer-name keyword-match mapper; and a teammate checking by calculator, timed.
- **Fallback:** the rule check only, on plans already drawn in OBPAS layers.

### 8. Parts and cost
Software only (ezdxf, LibreCAD or an AutoCAD student licence).

### 9. Three hard questions and honest answers
1. *"OBPAS and PreDCR already pre-check for free. Who pays you?"* Almost nobody, for the parameter check. Only the layer-fixing and feasibility pieces are new, and they are small.
2. *"Your rule tables disagree with the gazette?"* They will unless keyed and versioned by hand. Third-party tables already conflict.
3. *"Why not sell to the city?"* Cities buy from incumbents through tenders. A student team's realistic route is the deviation-check extension of P1.

### 10. Risks and what would kill it
The portal changes its layer spec; SoftTech or the portal adds auto-layering; the market is too small; liability for wrong feasibility advice.

### 11. Verdict
Buildability overnight **4**. Business **1–2**. AI/ML share **~35%**. Lead: a CS member with CAD familiarity. **Recommend dropping F7 from the idea bank, or folding its "approved plan versus built" angle into P1.**

---

## F1 Product-compliance checker for importers and small sellers (BIS QCOs, Legal Metrology, EPR)

### 1. The problem in one paragraph
A small importer or online seller must know whether a product needs BIS certification under a Quality Control Order, which declarations the Legal Metrology packaging rules require, and whether it must register for EPR (plastic packaging, e-waste, batteries). The rules move. About 700 QCOs were issued between 2016 and 2025, and by January 2026 the government had withdrawn 69 (ThePrint, https://theprint.in/economy/as-govt-starts-rolling-back-quality-control-orders-a-look-at-adverse-impact-they-had-mainly-on-msmes/2785033, Jan 2026, snippet). A January 2026 piece cites "more than 187 QCOs encompassing over 769 products" (https://swarajyamag.com/amp/story/news-brief/bis-withdraws-nine-outdated-standards-amid-indias-broader-quality-regulation-rethink, snippet). Another source says repeals cut products under mandatory QCOs to 736 (search summary, source unidentified, snippet). Customs demands for EPR certificates at Chennai port hit small importers hardest (R4-04, https://www.thecore.in/business/when-every-clearance-chennaiport-a-customs-inside-indias-broken-import-system-845839, snippet). One electronics product's CRS registration costs roughly **Rs 75,000–1.3 lakh** all-in: the BIS fee (~Rs 43,000–53,000 + GST quoted), lab testing (Rs 5,000–1.5 lakh) and a consultant (Rs 9,999–14,999). These are consultant pages, e.g. https://www.agileregulatory.com/blogs/bis-certification-cost-in-india-in-2026- and https://www.professionalutilities.com/bis-crs-registration (2026, snippets).

### 2. How the system works
```
Input: product listing (title, description, photos, spec sheet PDF), seller role (importer / manufacturer / brand owner), HS code if known
 → product understanding (VLM on photos + text) → candidate HS heading + product category
 → retrieval over a versioned rule base: BIS QCO list (IS no., scheme: CRS / ISI), Legal Metrology (Packaged Commodities) Rules 2011 + amendments,
   EPR (Plastic Waste Mgmt Rules, E-Waste Rules 2022, Battery Waste Mgmt Rules 2022), plus flags for WPC (wireless), BEE (star label), FSSAI (food)
 → obligations checklist, each with a citation (notification no., date, status: in force / deferred / withdrawn) and confidence
 → Legal Metrology label check: phone photo of the pack → OCR → required declarations present? → draft compliant label text
 → "ask a consultant" hand-off for anything below the confidence threshold
Rule-base upkeep: daily crawl of the BIS compulsory-certification list, the e-Gazette (search "Quality Control Order"), CPCB EPR portal notices,
   DoCA Legal Metrology notices → diff → human reviewer approves → new version; customers' SKUs re-scored and alerted
```

### 3. The AI/ML core
- **Retrieval-augmented classification:** the multilingual **bge-m3** embedding (open) over the rule corpus. Gazette PDFs are bilingual, Hindi and English. An LLM (Claude or Gemini API; **Qwen2.5-7B-Instruct** as the open fallback) does multi-label "which regimes apply". The output must quote the retrieved clause; no clause, no claim.
- **Label checker (the most certain piece):** OCR of the pack (Google Cloud Vision or Sarvam Vision; Hindi word accuracy ~91–96% on Sarvam's bench, https://www.sarvam.ai/blogs/Sarvam-vision, opened) → field extraction → rule check against Rule 6 declarations. Those are: manufacturer/packer/importer name and address, country of origin for imports, common or generic name, net quantity, month and year of manufacture, MRP inclusive of taxes, unit sale price (added by the 2021 amendment, in force from 1 Apr 2022), and consumer-care details (list from memory plus https://www.scconline.com/blog/post/2022/03/30/implementation-of-new-labelling-norms-extended-vide-legal-metrology-packaged-commodities-amendment-rules-2022/, 30 Mar 2022, snippet). Sources disagree on whether "month and year" for imports means manufacture or import (snippet), so the checker shows both and flags.
- **Published accuracy:** I found no benchmark for LLM classification of products to Indian regulations or HS codes (NOT FOUND).
- **Data:** none public. Tonight: 60 products (30 in QCO categories such as toys, helmets, pressure cookers, LED lamps, USB chargers and power banks; 30 outside), labelled by hand from the BIS list; and 20 real packaged goods from the campus store, photographed.
- **What it cannot do:** give a legal opinion; know unpublished clarifications, exemptions or customs practice at a given port; test the product; decide a borderline HS classification.

### 4. Why India needs its own version (and what changes from Complir)
Complir maps each SKU to each market's rules and generates labels and technical files for a 1,000-store European retailer (R4-04, YC page). **Kept:** product→requirement mapping, label generation and change alerts. **Changed:** in India each regulator publishes separately (BIS, DoCA Legal Metrology, CPCB/MoEFCC for EPR, DoT for WPC, BEE), by gazette PDF, sometimes in Hindi first. Rules are withdrawn as well as added (69 QCOs withdrawn), so status tracking matters more than in the EU. The buyer is an importer or online seller with tens to hundreds of SKUs, used to paying a consultant Rs 10–15k per filing, not enterprise SaaS. Indian consultancies give applicability advice free to win the filing (Agile Regulatory, ASC Group, Elitas, Professional Utilities, Corpseed, RegisterKaro; search 12 Nov 2026, snippets). **Resolve, Indian competitors:** only consultancies surfaced. No Indian AI tool for BIS, Legal Metrology or EPR was found in one search (C2 should try names).

### 5. Who has tried, and the gap
Consultancies, some calling themselves "technology-enabled", do the filings. Marketplaces enforce some category rules at listing (not checked). The gap: **a self-serve, always-current applicability and label check**. A seller can run it on every SKU before import or listing, with the consultant brought in only where filing is needed.

### 6. The business (Resolve: first buyer, price, upkeep)
- **First buyer: importer-sellers of consumer electronics, toys and small appliances** (Delhi's wholesale import trade, Amazon and Flipkart sellers). Their exposure is shipments held at customs and listings taken down, a cost far above the Rs 10–15k consultant fee. D2C brands come next (packaging and EPR); MSME exporters are a different rulebook.
- Bottom-up (assumptions labelled): 50,000 small importers and brands (assumption, NOT CHECKED) × 20 new SKUs a year = 10 lakh SKU checks × Rs 150 = **Rs 15 crore**. Plus monitoring at Rs 1,000 a month × 5,000 firms = **Rs 6 crore**. A pure checker is about a Rs 20 crore market: a feature, or lead generation for a filing business.
- **The company version** is a tech-enabled compliance firm: the AI does applicability, document assembly and labels, and staff file CRS, LMPC and EPR. It earns the Rs 10–15k per filing at a lower cost per file. 20,000 filings a year × Rs 12,000 = Rs 24 crore of revenue at scale. A services business with software margins at best.
- **Keeping the rule base current:** a daily crawler and diff with a named human reviewer (a law graduate, part-time). Every rule carries notification number, date and status, and SKUs are re-scored on change. This upkeep is the moat, and the main cost.
- First ten customers: five electronics/accessory importers in Delhi's import markets; two toy importers; one D2C personal-care brand (labels plus EPR); one compliance consultancy as a white-label partner; one Sonipat/Kundli manufacturer exporting to India's marketplaces.

### 7. What a team could show by noon
- **Prototype:** (a) a "paste a listing" applicability checker with citations; (b) a "photograph a pack" Legal Metrology label checker.
- **Test protocol:** **(main number) label-checker accuracy** on 20 real packs from the campus store × 8 required declarations = 160 field checks (present / absent / wrong), with truth by two people reading the pack, reported as precision and recall on "missing declaration". **(second) applicability** on 60 products: precision and recall of "QCO applies", against the hand label from the BIS list. **Baseline:** keyword match of product names against the BIS list; an LLM without retrieval.
- **Fallback:** the label checker alone. It is the most certain demo: real packs, a phone, OCR, rules.

### 8. Parts and cost
Software only. About Rs 500 of packaged goods from the campus store.

### 9. Three hard questions and honest answers
1. *"Consultants give applicability advice free. Why pay you?"* For the check alone, they won't pay much. They pay for speed across hundreds of SKUs and for alerts when a QCO lands or is withdrawn. The money is in filings, so the business is a tech-enabled consultancy or a consultancy's back office.
2. *"If your model says 'no BIS needed' and customs holds the shipment?"* Answers carry citations and a confidence score, and low confidence goes to a human. Liability is capped by terms. Do not sell guarantees.
3. *"How do you stay current?"* A crawler, diffs and a human reviewer, with versioned rules. The 69 withdrawals show the churn is real and costly to track by hand, which is the product's reason to exist.

### 10. Risks and what would kill it
Hallucinated obligations; a regime change (QCO rollback shrinking the problem); marketplaces building their own checks into seller onboarding; low willingness to pay; consultants underpricing.

### 11. Verdict
Buildability overnight **5** (label checker certain; applicability 4). Business **3** (as a tech-enabled compliance service; 2 as a pure tool). AI/ML share **~50%**. Lead: the CS/LLM person; a commerce or law student keys the rule base.

---

## NOT CHECKED
- Exact RoomPlan / iPhone LiDAR floor-area error from a peer-reviewed study (two searches found none); ARCore depth accuracy; LiDAR phone list is from memory (iPhone 12 Pro–17 Pro, iPad Pro 2020+).
- Whether the RBI Project Finance Directions' independent-engineer certification applies to all CRE-RH (residential) construction loans; LIE fee levels; RERA s.4(2)(l)(D) wording (from memory).
- MahaRERA's 3% carpet-area order (headline only): whether shortfalls under 3% are refundable.
- RERA s.2(k) carpet-area wording (from memory).
- Cartosat-3 archive density and planning cadence over NCR; whether the 2024 price list is current; Planet SkySat and Maxar prices for India.
- Microsoft Global ML Building Footprints coverage of India; Open Buildings v3 precision in Indian cities.
- Final Drone Rules 2021 zone distances (only draft summaries seen) and the Digital Sky classification for the Ashoka campus.
- Number of urban local bodies, property-tax collections, secured property loans per year, small importers in India (all used as labelled assumptions).
- Accuracy of LLM classification of products to Indian regulations or HS codes; tap-test hollow-tile accuracy; indoor damage-versus-wear benchmarks; floor counting from facade photos.
- Legal Metrology Rule 6 full current text (G.S.R. 226(E), 28 Mar 2022, not opened); LMPC importer registration fee.
- Landeed's exact state-by-state AI coverage and bank pricing; whether PreDCR is free in each AutoDCR city; Model Tenancy Act adopting states; UK and US inventory-report software.
- Whether Amazon and Flipkart enforce BIS QCOs at listing.

Searches used: 26

