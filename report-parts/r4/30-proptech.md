## 4. Proptech ideas

Round 1 found ten Indian property problems with public proof. Five went through design and fact-checking. One finding runs through all five: in Indian property, the AI part is usually a feature inside a service that people already pay for, and seldom a software company on its own. The cards say which is which.

### P1 · Finding untaxed and unauthorised construction from imagery

*Buildable overnight 4/5 · Business 3/5 · AI/ML about 60% · Track: AI & Systems or Space Tech*

- **The problem.** Property tax is a city's largest income of its own, but tax registers go years without revision. In one Nagpur zone, an AI survey flagged 7,000 of 9,000 properties as different from the register. Inspectors checked 380 at random and found 227 wrong: 12 new buildings and 215 major alterations. The city's arrears exceed Rs 900 crore ([Nagpur Today, 29 Oct 2025](https://www.nagpurtoday.in/nmc-to-launch-ai-based-property-survey-after-nine-years-to-boost-tax-revenue/)). Hyderabad's survey found over one lakh defaulters ([PropNewsTime](https://propnewstime.com/getdetailsStories/MjU2NDg=/ghmc-identifies-over-one-lakh-property-tax-defaulters-begins-recovery-of-more-than-inr-100-crore)), and Delhi began a drone survey of two wards in September 2026 ([ThePrint](https://theprint.in/india/mcd-begins-drone-survey-to-improve-property-tax-assessment-in-delhi/3050283/)).
- **The idea.** One change detector, two buyers. The tax wing wants a list of properties ranked by rupees owed. The enforcement wing wants a list of changes with no building permission on file.
- **Who pays.** The municipal corporation. In 2023 Delhi capped a drone and door-to-door survey of about 30,000 properties at Rs 3 crore, roughly Rs 1,000 a property ([Prithvi Estates, 15 Mar 2023](https://www.prithviestates.com/?p=139133)). Each such survey is stale within two years. The product is a yearly change alert at perhaps Rs 10–20 a property. With 100 large cities and 3 crore properties (assumptions), the ceiling is about Rs 60 crore a year.
- **How it works.**
  1. Take two images of the same area from different dates.
  2. Detect where building footprints appeared or grew.
  3. Match each change to a line in the tax register.
  4. Estimate the tax gap: extra built area times the city's rate.
  5. Give inspectors a ranked visit list. Their verdicts become training labels.
- **The AI/ML core.**
  - Change-detection models (BIT or ChangeFormer in the open Open-CD toolkit), pretrained on LEVIR-CD, a set of 637 image pairs. They score about 90% on that set, which is American suburbs; expect less on Indian rooftops until fine-tuned.
  - Google's Open Buildings gives free building outlines for India, and a yearly presence layer for 2016–2023 ([Open Buildings Temporal](https://sites.research.google/gr/open-buildings/temporal)).
  - Matching a change to a register entry with a free-text address is often the larger source of error.
- **What imagery can see.** This is the key design fact.
  - Free Sentinel-2 images (10 metres per pixel) cannot see a single house.
  - India's Cartosat-3 (0.28 metres) costs Rs 3,860–4,810 for a 17 by 17 km scene and is free to government bodies ([NRSC/NSIL price note, Apr 2024](https://ibm.gov.in/writereaddata/files/17210395936694fae952c70Commercial_Products_Ordering_Bhoonidhi_Thr_NSIL_Interface_FA.pdf)). It shows new buildings, sheds and extensions.
  - A new floor is nearly invisible from above. It shows only as a slightly longer shadow. Floors need a drone.
- **Who has tried.** Bhubaneswar runs a system built by Vassar Labs on commercial imagery (snippet). The Defence Estates office built its own with BARC and in 2022 reported 1,133 unauthorised changes detected ([DGDE](https://dgde.gov.in/dgde-develops-ai-based-software-to-detect-unauthorised-constructions-encroachments-on-defence-land), snippet). Other cities hire one-off survey agencies. Nobody was found selling a recurring alert across many cities.
- **What you could show by noon.** Cover the Ashoka campus, Rai and Kundli, about 25 square km, using two dates from a free historical-imagery viewer (fine for a demo; its licence bars commercial use). Build a mock register of 150 properties with 30 deliberately out of date. **The number:** of the top 50 properties the system flags, how many are real changes, judged by two teammates separately. Compare with the free Google yearly layer and with random order.
- **Parts and cost.** Software only.
- **The hard question.** "Who pays, and when?" City pilots are usually free and paid work needs a tender. Expect 12–18 months to first revenue.
- **Suits.** Vibhore Sharma (Info Edge has backed geospatial AI before). The weak point for a revenue-minded mentor is the slow public buyer.
- **Note.** The one surviving piece of the dropped plan-checking idea (section 4.6) belongs here: comparing an approved plan with what was actually built.

### P4 · Phone scan of a new flat: true carpet area and a snag list

*Buildable overnight 5/5 · Business 3/5 · AI/ML about 40% · Track: AI & Systems*

- **The problem.** Buyers find seepage, hollow tiles and less floor area than they paid for only after taking possession. MahaRERA alone had 6,366 complaints pending in December 2025, of all kinds ([PropNewsTime, citing the state Economic Survey](https://propnewstime.com/getdetailsStories/MjczMjQ=/maharera-faces-backlog-with-over-6-300-unresolved-complaints-as-of-december-2025)). About 5.2 lakh homes were completed in the top seven cities in 2025 (ANAROCK, snippet). The money is concrete: on a 700 sq ft flat at Rs 12,000 a sq ft, a 1% shortfall is Rs 84,000.
- **Funded analogue.** Automax.ai (Y Combinator, Fall 2025) sends an inspector to scan a house with a phone's depth sensor, drafts the valuation with AI, and has a licensed appraiser sign ([YC launch page](https://www.ycombinator.com/launches/Oq3-automax-ai-powered-property-appraisals-in-minutes)).
- **What changes for India.** India has no reliable database of comparable sale prices, so AI valuation is dropped. The daily Indian dispute is carpet area, which is a measurement problem. Like Automax, this works best as an inspection service that uses software, not as software alone.
- **How it works.**
  1. Scan each room with an iPhone Pro; Apple's free RoomPlan tool returns walls and openings.
  2. Compute carpet area as the RERA Act defines it (section 2(k)): usable floor area including internal partition walls, excluding outer walls, shafts, balconies and terraces.
  3. Compare with the sale agreement and state the shortfall in rupees.
  4. Add snags: cracks from photos, hollow tiles from the sound of a tap, floor slope from the phone's motion sensor.
  5. Produce a report the buyer can send to the builder or to RERA.
- **The AI/ML core.** Geometry carries the area; ML does the smaller jobs. A segmentation model finds cracks, an audio classifier separates hollow from solid tiles, and a vision-language model writes each snag line.
- **The accuracy question nobody has answered.** No published study gives RoomPlan's floor-area error. On a 3 by 4 metre room, a 5 cm error on each wall is about 3% of the area, which is the whole 3% variation that Maharashtra's model sale agreement allows before a refund is due (an advocate's reading in the [Free Press Journal, 29 Jun 2026](https://www.freepressjournal.in/mumbai/consumer-connect-maharera-mandates-refund-for-carpet-area-shortfall-within-3-variation-cap), not a ruling). So the scan settles a dispute only if each wall is right to 1–2 cm. Where it is not, the app must ask for a laser-meter reading.
- **Which phones.** Only iPhone 12 Pro and later Pro models, and iPad Pro, have the sensor. Without one, use a laser distance meter and an in-app sketch.
- **Who has tried.** PropCheck says it has done over 45,000 inspections, using laser meters and thermal scanning ([propcheck.in](https://propcheck.in/); another part of the same page says 10,000-plus). Nemmadi and HomeInspeKtor are similar. All are people-led.
- **Who pays.** The buyer, Rs 4,000–6,000 at handover. If 20% of completed homes were inspected (assumption), that is about Rs 52 crore a year of service revenue in the top seven cities. Software licensed to inspection firms would earn about Rs 3 crore.
- **What you could show by noon.** **The number:** average error in room floor area, phone scan against laser meter, over 10 rooms scanned three times each by different people. Compare with one person using a tape. This number does not exist in print, so measuring it is a real result.
- **Parts and cost.** A borrowed iPhone Pro, a laser distance meter (Rs 1,500–4,000, estimate), eight tiles and a sheet of plywood for the tap test.
- **The hard question.** "PropCheck has done 45,000 inspections. What do you add?" One technician in 90 minutes instead of two engineers in four hours, with a stated accuracy band. They could adopt the same tool.
- **Suits.** A revenue-minded mentor (a buyer who pays at a moment of need). Anuj Mehta.

### P2 · Move-in and move-out condition report for rented flats

*Buildable overnight 4/5 · Business 2/5 · AI/ML about 55% · Track: AI & Systems*

- **The problem.** Tenants in Bengaluru and Mumbai pay deposits of many months' rent and argue over deductions when they leave. One widely shared case: Rs 1 lakh paid, Rs 19,604 returned ([Business Today, 14 Jul 2026](https://www.businesstoday.in/latest/trends/story/rs1-lakh-deposit-rs19604-returned-bengaluru-tenant-alleges-massive-deduction-by-landlord-542774-2026-07-14)). An estimate attributed to NoBroker puts deposits held in six metros at Rs 1.26 lakh crore ([RentOk summary](https://rentok.com/blogs/case-study/security-deposits-the-hidden-cost-of-renting)); the method is not published, so treat it as a rough size. Neither side has a neutral record of the flat on day one.
- **Verdict up front: a feature.** RentOk already sells photo checklists for move-in and move-out. Abroad, several products produce AI condition reports (Property Inspect, Paraspot and others). What is new is the automatic comparison with a priced, itemised deduction.
- **How it works.**
  1. At move-in, the app guides a fixed set of photos per room. Both sides confirm.
  2. At move-out, the app shows the old photo as a faint overlay so the new one matches.
  3. Software aligns each pair and finds what changed.
  4. A model labels each change as damage, normal wear, or no real change (a shadow, a moved chair).
  5. A written rule table, not the model, decides what is chargeable, and a rate card prices it.
- **The AI/ML core.** Feature matching (LightGlue) aligns the pair; image differencing finds changes; a vision-language model labels them. No published accuracy exists for telling damage from wear indoors.
- **Who pays.** Co-living and PG operators, who handle hundreds of move-outs a month and control the app. A licence at Rs 75 a move-out might earn about Rs 6 crore a year (assumptions). It becomes a company only as the evidence layer of a deposit-free renting product.
- **What you could show by noon.** Ten hostel rooms. One teammate photographs them. A second stages 30 reversible changes (washable marks, a chalk crack, a missing switch cover) and 30 distractions (lights, curtains, a moved chair). A third re-photographs. **The number:** real changes caught, and false alarms per room. Compare with handing the model the two photos without alignment.
- **Parts and cost.** Phones, tape, chalk, washable markers. Under Rs 300.
- **The hard question.** "Why would a landlord agree to a neutral report?" Many will not. That is why the buyer is the operator, who can make it the process.

### P5 · Independent construction-progress check for lenders and buyers

*Buildable overnight 4/5 · Business 2–3/5 · AI/ML about 55% · Track: AI & Systems*

- **The problem.** About 1.56 lakh homes were stalled in the top seven cities at December 2025 (ICRA, March 2026, snippet). Buyers pay instalments and lenders release money against progress the developer reports.
- **What lenders already buy.** The Reserve Bank's Project Finance Directions, in force since 1 October 2025, require each loan instalment to be certified by the lender's independent engineer or architect ([AZB summary](https://www.azbpartners.com/bank/rbi-issues-directions-on-project-finance-for-all-regulated-entities/)). Whether this covers every housing construction loan was not confirmed. So the certificate is taken. What is missing is cheap, monthly, outside evidence between site visits.
- **The idea.** A phone video from the public road, plus satellite images, turned into a floor count and a stage for each tower. Compare with the schedule the developer filed with RERA. A lender sees which projects lag their claims.
- **The AI/ML core.** A detector counts floor slabs on photos of the building face, with a vision-language model as a second opinion. From satellite, tower height can be estimated from shadow length to within about one floor, and only for towers standing in the open. It cannot see interiors or quality.
- **Who has tried.** Track3D ($10 million, September 2025), Contineu ($1.2 million) and HUVIAiR sell site-capture tools to developers (snippets). Nobody was found selling outside evidence to lenders or buyers.
- **Who pays.** The engineering firms that certify for lenders, and lenders' risk teams. About Rs 36 crore a year on assumed project counts. A feature for those firms, not a company.
- **What you could show by noon.** **The number:** average error in floor count on 20 buildings whose floors you know (campus blocks, towers near Rai and Kundli photographed from the road), two views each. Compare the detector, a model with no training, and a person counting from the same photo.
- **The hard question.** "Lenders already pay an engineer. Why add you?" The engineer visits now and then; this watches every project every month and says where to go.
- **Overlap with your own work.** Same site-camera technique as your factory vision idea.

### P3 · Title reader for sale deeds (did not survive; a smaller piece does)

*Buildable overnight 3/5 · Business 2/5 · AI/ML about 70% · Track: AI & Systems*

- **The problem.** Land records disagree with each other. In the Telangana districts checked, the digital record showed 32.80 lakh acres where the older survey register showed 26.98 lakh, a gap of 5.8 lakh acres ([Deccan Chronicle, 17 Feb 2025](https://deccanchronicle.com/southern-states/telangana/massive-discrepancies-identified-between-sethwar-and-dharani-land-records-1861663)). A lender must trace decades of deeds before it lends.
- **Why the broad version failed.**
  - Landeed already sells banks 30-year chain-of-title reports signed by its own advocates, with AI screening ([Landeed](https://www.landeed.com/banks-and-nbfcs)).
  - Reading the documents is not good enough yet. On one vendor's benchmark, the best paid service reads about 88% of Telugu words correctly and open models 54–59%; Hindi reaches about 96% ([Sarvam, 5 Feb 2026](https://www.sarvam.ai/blogs/Sarvam-vision)). One word in eight wrong breaks a chain of survey numbers.
- **What survives.** A Hindi deed and land-record reader for the independent advocates who do title searches for banks in Haryana and western UP. It builds the chain, flags gaps, over-sales and double sales, and drafts the annexure; the advocate signs. Banks cap the fee for such a search at about Rs 5,000 a property (one bank's fee schedule, snippet).
- **What you could show by noon.** Twenty made-up Hindi deeds forming four chains, three with a planted defect, photographed in poor light. **The number:** fields read exactly right out of 160, and defects caught out of three.
- **The hard question.** "Landeed has the money and the advocates. Why you?" Do not fight for bank contracts. The opening is the independent advocate and Hindi-belt record types.

### 4.6 Tested and dropped: building-plan pre-check

Structured AI (Y Combinator, Fall 2025) checks construction drawings against building codes, and Y Combinator's current list asks for "AI for City Hall". The Indian version looked open in round 1. It is not. Haryana's online approval system already lets an architect run its scrutiny engine free before submitting ([HSVP manual](https://obpas.hsvphry.org.in/docs/UserManual_AA.pdf)). Mumbai launched its own AI pre-scrutiny in May 2026 ([Free Press Journal](https://www.freepressjournal.in/mumbai/bmc-launches-indias-first-ai-based-civittwin-system-for-faster-building-approvals)), and SoftTech and two others sell architect-side tools. The market left over is about Rs 6 crore a year. Dropped.

### 4.7 Other property problems found, not designed

| Problem | Strongest fact found | Why it was not taken further |
|---|---|---|
| Old, unsafe buildings | A Bhiwandi building declared unsafe in 2020 collapsed in July 2026, killing ten (snippet) | A model cannot honestly call a building safe or unsafe; liability |
| Society sewage plants that do not run | 125 private plants not working in Pune and Pimpri-Chinchwad (snippet) | A sensor kit, little AI; proof is enforcement counts only |
| Tanker water with no litres measured | One society spent about Rs 10 lakh in three months | Covered in the 3 Nov report, which judged the proof thin |
| Site safety and concrete quality | About 11,600 construction deaths a year (secondary estimate) | Helmet detection is crowded; overlaps your factory vision idea |

Full notes: `research_notes\R4-03 Proptech India.md`.
