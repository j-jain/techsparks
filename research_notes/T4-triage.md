# T4 — Triage after Round 4 (coordinator, 12 Nov 2026)

Round 4 produced five notes: `R4-01` and `R4-02` (nine mentors and the institutions), `R4-03` (ten proptech problems), `R4-04` (20 startups backed by YC or a16z) and `R4-05` (20 backed by Sequoia or Peak XV). 163 of 200 searches were used. This file picks the 14 ideas that go to Round 5 and says who checks and who designs each.

## What Round 4 established

- **No public brief exists.** SPARK Night's challenge statements, judges and criteria are not published anywhere that could be opened. The mentors' own public statements from 2024–26 are almost nil. What they would want to see is therefore read from what their funds have paid for.
- **The five poster mentors, by what their record rewards:**
  - *Vibhore Sharma* (Capital 2B and Redstart Labs, both Info Edge vehicles; ex-CTO of Info Edge): sensing or robotics joined to ML, and proof that the technology works. Portfolio includes robot vision (CynLr), warehouse robots (Unbox), drones (Skylark), brain-MRI AI (BrainSight), geospatial AI (Attentive AI, Skyserve AI), TB genomics (Aarogya AI) and, through Capital 2B, voice AI (Ringg).
  - *Karthik Varada* (Beyond Next Ventures, India): deep science with a climate, health or resource outcome, moving from lab to market. Portfolio includes silicon-anode cells (Volt14), an airborne-pathogen device (Biomoneta), edge AI (Myelin Foundry) and dairy mastitis detection (Faunatech).
  - *Shilpy Kochhar* (Ashoka R&D Office; ten years at BIRAC): biotech and health devices and diagnostics, with a named grant route (BIG, up to Rs 50 lakh).
  - *Anuj Mehta* (Campus Fund): student founders. The fund's own data say applied AI is about four-fifths of student deep tech, and it backs hardware-heavy student teams (Digantara, EtherealX, Sarla Aviation).
  - *Aman Mankani* (PedalStart; the poster spells it "Makhani"): the firm's house view is cash, revenue, retention and the right customer. Who pays, and how soon.
- **Site-only mentors:** Arshia Mal (WTFund: Rs 20 lakh grants to under-25s; recent picks are health hardware plus AI), Aishwarya Malhi (Rebalance: women founders, about 40% deep tech), Vidushi Malhotra and Apoorv Bamba (Belong Education: employability, Tier 2–3 India).

## The shortlist (14)

IDs: M = read from the mentors' record, P = proptech, F = India version of a funded startup. Several ideas belong to two groups; the group shown is where the report will place it.

| ID | Idea | Comes from | Design | Claims |
|---|---|---|---|---|
| M1 | Phone-on-microscope AI slide reader for small labs, malaria blood smears first | Kochhar's BIRAC diagnostics record; WTFund backed a slide digitiser (Turocrates AI); Info Edge backed TB genomics (Aarogya AI). Not researched in Round 4 | D1 | C1 |
| M2 | Hinglish OPD scribe that prints the prescription for solo doctors | `R4-05` entry 4 (Freed, Sequoia). Capital 2B is in voice AI through Ringg | D1 | C1 |
| M3 | Solder and placement defect inspector for small electronics assemblers | `R4-05` entry 13 (SixSense, Peak XV Surge). Info Edge backed CynLr | D1 | C1 |
| M4 | Acoustic leak finder for city water pipes | `R4-05` entry 15 (Puralink, Peak XV Surge). Fits Varada's resources thesis | D1 | C1 |
| F2 | Health-insurance claim checker that cites the policy clause | `R4-05` entry 1 (Pace, Sequoia) and `R4-04` Avelis Health (YC) | D1 | C1 |
| F3 | Hindi voice agent that makes a small fleet's check calls | `R4-04` Hemut (YC) | D1 | C1 |
| F4 | Drawing-to-quote for small machine shops | `R4-05` entry 12 (Pre6, Peak XV Surge) | D1 | C1 |
| P1 | Finding untaxed and unauthorised construction from imagery | `R4-03` Problems 1 and 7 | D2 | C2 |
| P2 | Move-in and move-out condition report for rented flats | `R4-03` Problem 5 | D2 | C2 |
| P3 | Chain-of-title reader for sale deeds in Indian languages | `R4-03` Problem 6 | D2 | C2 |
| P4 | Phone scan of a new flat: true carpet area, snag list, valuer's annexure | `R4-03` Problem 4 and `R4-04` Automax.ai (YC) | D2 | C2 |
| P5 | Independent construction-progress check for lenders and buyer groups | `R4-03` Problem 3 | D2 | C2 |
| F7 | Building-plan pre-check against one city's bye-laws | `R4-04` Structured AI (YC) and the YC request "AI for City Hall" | D2 | C2 |
| F1 | Product-compliance checker for importers and small sellers (BIS, Legal Metrology, EPR) | `R4-04` Complir (YC) | D2 | C2 |

### Why these, and what Round 5 must resolve

**M1 Slide reader.** The one idea added by the coordinator, because the bio mentor's whole career is biotech entrepreneurship and Round 4 produced no bio idea. The argument to test: as malaria falls, positives become rare, and a tired microscopist misses them; a model that screens fields and shows the suspicious ones is worth more in an elimination-stage country, not less. Public cell-image data exist (NIH malaria cells, BBBC041, Makerere thick-smear phone images). Resolve: is malaria the right first test, or is it TB sputum, cervical cytology or anaemia typing? Who buys (state malaria programme, private labs)? How do SigTuple, Morphle and Turocrates AI differ? What can be shown overnight with a teaching microscope, a phone and prepared slides?

**M2 OPD scribe.** Eka Care already has a scribe (3,000+ doctors per the notes). The open gap claimed is the noisy two-to-three-minute consult for a solo GP, output as a printed or WhatsApp prescription, in Hindi and one or two regional languages. Resolve: is that gap real or has Eka closed it? What word error rate do current models reach on code-mixed medical speech? Price a solo GP will pay.

**M3 Defect inspector.** Best overnight score in Round 4 (public PCB datasets, one camera). Indian rivals SwitchOn and Frinks are funded and sell to larger plants. Resolve: the small-assembler segment's size, what AOI machines cost them today, whether a Rs 20–30 thousand camera station is credible. Overlap: factory vision.

**M4 Leak finder.** Non-revenue water is cited at 40–50% without one authoritative source. Solinas (IIT Madras) and Fluid Robotics work inside pipes; SmartTerra works on data. The idea skips the robot: a contact microphone or accelerometer on a valve or hydrant and a classifier. Resolve: published accuracy of acoustic leak detection on plastic versus metal pipes, the effect of intermittent supply (pipes are empty much of the day), who pays.

**F2 Claim checker.** Strongest regulatory hook in the set: the notes say IRDAI now requires a rejection to cite the policy clause, and BCG with Medi Assist puts fraud, waste and abuse at Rs 8,000–10,000 crore a year. Two possible products: an auditor for the insurer or TPA (Avelis), or an explainer for the hospital billing desk or patient (Pace turned around). Resolve: pick one. Check thoroughly for Indian competitors, since "none found" in Round 4 came from one search.

**F3 Trucking voice agent.** About three-quarters of operators run fewer than five trucks. Indian voice platforms exist (Bolna, Ringg, Gnani) but none found for trucking. Resolve: who is the buyer (transport agent, mid-size fleet, a broker app), is the check call really the pain, and what is left once BlackBuck-style GPS tracking is counted. Overlap: voice notes into structured data.

**F4 Drawing-to-quote.** Pre6 sells to large suppliers (SKF, L&T Valves, Rane per its site). The gap claimed is the 10–50 person job shop quoting from a photographed drawing. Resolve: how accurately current vision models read dimensions and tolerances from 2D drawings, how job shops quote today, a defensible costing method.

**P1 Change detection.** Municipalities already commission this (Nagpur, Hyderabad, Delhi, Navi Mumbai, Bhubaneswar). Nagpur's pilot found 7,000 of 9,000 mapped properties differed from the register. Resolve: which open imagery is sharp enough (Sentinel-2 at 10 m is not; what is?), open building-footprint datasets for India, how vendors are paid, what one team can show overnight.

**P2 Condition report.** Rs 1.26 lakh crore of deposits in six metros (NoBroker report, secondary). Resolve: is this a product or a feature; the best first buyer (co-living and PG operators, property managers, NoBroker-type platforms); how reliably a model separates damage from wear.

**P3 Title reader.** Strongest proof, hardest build. Landeed is funded and has an AI unit. Resolve: where Landeed stops (which states, which document types), how good OCR is on old Telugu, Kannada, Marathi and Hindi deeds, who pays per search (banks and NBFCs through panel lawyers).

**P4 Flat scan.** Merges two things that use the same phone scan: the buyer's snag-and-area check at handover, and the bank valuer's measurement annexure (the Automax.ai model). Resolve: accuracy of phone LiDAR for floor area, which phones have it, whether RERA's carpet-area definition can be computed from a scan, which of the two buyers to lead with.

**P5 Progress check.** 1.56 lakh stalled units in the top seven cities (ICRA). Track3D, Contineu and HUVIAiR sell to developers; nobody found selling independent verification to lenders or buyers. Resolve: do lenders already buy this from project-monitoring consultants and at what price; what can be read from free or cheap satellite imagery versus a drone or a phone. Overlap: site vision.

**F7 Plan pre-check.** Cities are automating scrutiny on their side (BMC, DDA, Telangana). No architect-side pre-check startup found. Resolve: which city has machine-readable rules and sample plans, what autoDCR-style systems already give the architect for free, whether a 1–5 person practice pays.

**F1 Compliance checker.** 769 products under BIS quality-control orders; EPR and Legal Metrology add more. No Indian AI tool surfaced. Resolve: the first buyer (importer, Amazon or Flipkart seller, D2C brand), the price of a compliance consultant today, how to keep the rule base current, and Indian competitors by name.

### Not shortlisted, kept for the report's table

From `R4-04`: Automax.ai (folded into P4), Brumby (cattle counting for India), Adialante, CentralComs, Stilta, Rudus, Vela Energy, Tivara, Unlimited Industries, XBuild, FurtherAI, Lassie, Sphere, Eka Robotics, Westmag, PrismaX. From `R4-05`: Mecka, Bunkerhill, Avelios, Sunflower Labs, WithCoverage, Sandstone, Rillet, Form Energy, Luminai, Supanote, Ringg, Zoop, Rosella, August AI, Hoola. From `R4-03`: unsafe old buildings (liability; overnight score 2), sewage plants in societies, tanker water, site safety and concrete.

Reasons in brief: GST and accounting (Rillet, Sphere) and voice agents for clinics (Tivara, Ringg) are crowded in India; court-order explainer (Sandstone) has no clear payer; MRI, motors, batteries and chips cannot be shown by a student team; unsafe-building screening cannot be claimed honestly overnight.

## Assignments for Round 5

### Design agent D1 → `R5-design-01.md`
M1, M2, M3, M4, F2, F3, F4. Read the `R4-05` entries 1, 4, 12, 13, 15 and the `R4-04` entries Avelis Health and Hemut. M1 has no Round 4 note: source its two Indian numbers yourself and open the pages.

### Design agent D2 → `R5-design-02.md`
P1, P2, P3, P4, P5, F7, F1. Read `R4-03` Problems 1, 3, 4, 5, 6, 7 and the `R4-04` entries Automax.ai, Structured AI and Complir, plus the YC Requests for Startups section.

### Claims agent C1 → `R5-claims-01.md`

**Mentors and institutions** (sources in `R4-01`, `R4-02`):

- MN1. Vibhore Sharma is Partner at Capital 2B and also General Partner / Head of Deep Tech Investing at Redstart Labs; ex-CTO of Info Edge; co-founded Capital 2B in 2022 with Amit Behl; the fund is $75M, backed by Info Edge and Temasek, pre-seed to Series A. Which title is current in November 2026?
- MN2. Capital 2B portfolio includes Manastu Space, Botsync, Ahammune, Beatoven.ai, HyperNorm AI, and it took part in Ringg's $10M round of 26 Aug 2026. Redstart portfolio includes Unbox Robotics, BrainSight AI, Skylark Drones, ePlane, CynLr. Info Edge approved Rs 100 crore more for Redstart on 3 Nov 2025.
- MN3. Sharma said in 2022 that deep-tech goals are "binary" and the question is whether the technology works. Find the page and the exact words. Find any statement of his from 2024–26 (podcast, panel, interview).
- MN4. Karthik Varada is Senior Associate, Investment Group (India), Beyond Next Ventures; IIT Hyderabad; University of Tokyo PhD; joined Sep 2022. BNV's India 1 fund's first deal was Volt14 (14 May 2025, $1.87M led by Blume), second FinalLayer (Oct 2025). India portfolio includes Biomoneta, Myelin Foundry and Faunatech.
- MN5. The poster's "Aman Makhani, PedalStart" is Aman Mankani, on PedalStart's founding team in Gurugram. Confirm spelling, role and that he is the person on the poster. PedalStart's co-founders are Manas Pal and Aditya Darolia; Pal's 9 Jan 2026 SMEStreet piece contains "Raising money did not fix broken products, services, weak sales, or confused teams."
- MN6. Anuj Mehta's title at Campus Fund (Vice President or Investment Director). Fund III is $100M, announced 23 Jun 2025, first cheques Rs 1–8 crore. Portfolio includes Digantara, EtherealX, Sarla Aviation, Serendipity Space. The fund's 2025 report: deep tech about 17% of 7,300+ startups evaluated, about 79% of that applied AI. "Build In India" carve-out of up to $10M, 23 Sep 2026.
- MN7. Shilpy Kochhar is Director, Research & Development Office, Ashoka; previously Head of Business Development and Communications at BIRAC after 10+ years there; in 2019 she ran the Ignition Grant, regional centres and student entrepreneurship programmes.
- MN8. WTFund gives Rs 20 lakh, non-dilutive, to founders under 25. Its cohort profiled on 31 Jan 2026 included Astraeus Innovus (oral cancer screening), Turocrates AI (microscope attachment for pathology slides), Bloom Rehab, Placestation and Aeyi (CCTV incident alerts). Arshia Mal's role there.
- MN9. Aishwarya Malhi co-founded Rebalance in 2019; a 23 May 2026 interview gives 10 cohorts, 30+ startups, about 40% deep tech and about US$50M deployed, and the quote "Good investing is not gendered. Access is."
- MN10. Vidushi Malhotra and Apoorv Bamba are co-founders of Belong Education (12 Oct 2022 release on the InternIn acquisition).
- MN11. Info Edge had 18 deep-tech investments by April 2025, including Attentive AI, Skyserve AI, Aarogya AI, RaylOT, CynLr and BrainSight AI; by 31 Mar 2026 the count was 30 companies and Rs 455 crore; on 27 Mar 2026 the board approved up to Rs 250 crore for A88 Fund I.
- MN12. BIRAC's BIG grant is up to Rs 50 lakh over 18 months with calls around 1 January and 1 July. Is a call opening on 1 Jan 2027?

**Ideas** (sources in `R4-05` and `R4-04`; check each line's funding facts, Indian numbers and Indian competitors):

- M1. Find and verify three numbers, opening the pages: blood slides examined for malaria in India per year; India's reported malaria cases in the latest year; any published sensitivity and specificity for AI malaria microscopy on phone-captured images. Check SigTuple, Morphle and Turocrates AI are alive and what each sells.
- M2. Freed: Sequoia-led Series A, 5 Mar 2025, 17,000+ providers. Eka Care: total funding $19.5M, scribe used by 3,000+ doctors, NVIDIA partnership for an offline multilingual scribe. Find one hard Indian number on consult length or patients per doctor per day.
- M3. SixSense in Peak XV's Surge 11 (25 Sep 2025). SwitchOn Rs 78 crore pre-Series B (IvyCap, Jul 2026). Frinks AI $5.4M (Prime, 2025). Find one hard number on India's electronics assembly base.
- M4. Puralink in Surge 12 (28 Sep 2026). Solinas Integrity: funding and status. Find the best available source for India's non-revenue water percentage.
- F2. Pace: $10M Series A led by Sequoia, 27 Jan 2026. Avelis Health: YC S25. BCG and Medi Assist: Rs 8,000–10,000 crore a year in fraud, waste and abuse. FY25: 1,37,361 grievances, about 69% claim-related; 3.26 crore health claims, 8% repudiated. IRDAI requires the rejection to cite the policy clause: find the circular. Indian AI claim-audit competitors: search by name (for example IHX, Vitraya, Artivatic, ClaimBuddy, Qantev).
- F3. Hemut: YC X25, $1.8M seed. About 75% of Indian truck operators run fewer than five trucks (Redseer). Bolna $6.3M seed (General Catalyst, Jan 2026). Any Indian voice agent built for trucking.
- F4. Pre6 in Surge 11; founders Amod Malviya and Rishi Kedia; customers SKF, L&T Valves, Rane. Find one hard number on Indian machine shops or MSME engineering units.

### Claims agent C2 → `R5-claims-02.md`

**Ideas** (sources in `R4-03` and `R4-04`):

- P1. Nagpur pilot: 9,000 properties mapped, about 2,000 new and 7,000 changed; inspectors checked 380 and found 12 new buildings and 215 with major alterations; arrears above Rs 900 crore (29 Oct 2025). Hyderabad GIS survey: over 1 lakh defaulters, evasion above Rs 100 crore. Delhi MCD drone pilot (2 Jun 2026). Defence estates: 1,133 unauthorised changes detected, 570 acted on. Vassar Labs / ORSAC in Bhubaneswar. Info Edge backed Attentive AI and Skyserve AI.
- P2. Rs 1,26,042 crore of deposits across six metros (NoBroker Rent Report 2026). The 14 Jul 2026 Business Today case: Rs 1 lakh deposit, Rs 19,604 returned. Model Tenancy Act two-month cap and which states adopted it. Any Indian or foreign product that issues a move-in / move-out condition report.
- P3. Telangana: Dharani lists about 32.80 lakh acres against 26.98 lakh in Sethwar. Landeed: $8.3M seed (Jan 2023), $5M round (Jan 2025) for an AI unit; status in 2026. Land and property share of civil cases (Daksh).
- P4. MahaRERA refund for carpet-area shortfall within a 3% variation cap (Jun 2026). MahaRERA complaints: about 33,806 received, 6,224 pending by Mar 2026. Automax.ai: YC F25. Navanc $1M seed. Any Indian home-inspection or snagging company with funding.
- P5. ICRA: about 1.56 lakh stalled units in the top seven cities at Dec 2025. PropEquity: about 5.08 lakh units in roughly 2,000 projects in 42 cities. SWAMIH 2.0: Rs 650 crore in Budget 2026–27. Track3D $10M Series A (Sep 2025); Contineu $1.2M seed; HUVIAiR $3.2M Series A.
- F7. Structured AI: YC F25, $4.2M seed (ENR, 9 Jun 2026). BMC "CivitTwin" AI pre-scrutiny; DDA single-window AI scrutiny. The YC request "AI for City Hall" (Winter 2027). Any Indian architect-side plan-checking startup.
- F1. Complir: YC S26; Flying Tiger Copenhagen as customer. 769 products under BIS quality-control orders. Any Indian AI compliance startup for BIS, Legal Metrology or EPR, by name.

**The funded-startup table.** The report will list about 24 startups with backer, round, amount and date. For each line below, confirm from a primary announcement or two press reports; correct where the named fund only participated; flag shut-downs, pivots and acquisitions. Spend about one search per two lines and stop at your allowance.

- YC: Brumby / GrazeMate (W26, $1.2M pre-seed), Adialante (S26), CentralComs (S26), Stilta (W26), Hemut (X25), Avelis Health (S25).
- a16z: Unlimited Industries ($12M seed co-led, 3 Dec 2025), FurtherAI ($25M Series A led, 7 Oct 2025), Lassie ($35M Series A led, 26 Jun 2026), Sphere ($21M Series A led, 18 Nov 2025), Westmag (seed led, 2 Jun 2026), XBuild ($19M Series A, 20 Jan 2026, a16z participated, N47 led), Eka Robotics ($150M Series A, a16z and F-Prime).
- Sequoia: Mecka ($60M Series B led, 8 Oct 2026), WithCoverage ($42M Series B co-led with Khosla, 14 Jan 2026), Sandstone ($10M led, Jan 2026), Rillet ($25M Series A led, 28 May 2025), Sunflower Labs (Nov 2025), Form Energy ($100M, Sep 2026).
- Peak XV: Ringg ($10M extended Series A led, 26 Aug 2026, with Arkam and Capital 2B), Supanote (Surge 11), Zoop (Feb 2026), August AI (Surge 12).
