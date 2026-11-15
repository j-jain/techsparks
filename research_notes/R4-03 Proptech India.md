# R4-03 Proptech India  (agent: Sonnet, date 2026-11-12)

Method note: WebSearch returns summaries with a URL list, not page text. Items I opened with WebFetch are marked (opened). Everything else is from a search summary and is marked (snippet). Reddit and Arctic Shift were unreachable (HTTP 422), so Reddit proof below comes only through news articles that quote Reddit posts; no upvote counts were available. Proof tiers are therefore judged on news items and hard numbers, and social engagement is mostly NOT FOUND.

---

## Problem 1: Property-tax under-assessment, found by AI over drone / satellite / LiDAR imagery
- Track: AI & Systems (also Space Tech)
- Who suffers: municipal corporations whose largest income is property tax but whose registers are 9+ years stale; honest taxpayers who carry the load of evaders. Annual / recurring.
- How they cope today: manual door-to-door surveys by tax inspectors, self-assessment forms, occasional one-off drone or GIS surveys by outside agencies.
- Public proof (tier B+, news and official statements only; no social engagement found):
  - https://www.nagpurtoday.in/nmc-to-launch-ai-based-property-survey-after-nine-years-to-boost-tax-revenue/ — 29 Oct 2025 (opened) — Nagpur pilot in Laxmi Nagar zone: AI mapping produced 9,000 property entries; about 2,000 were new constructions and 7,000 had structural or usage changes not in civic records. Tax inspectors physically checked 380 random properties and found 12 wholly new buildings and 215 with major alterations. Arrears exceed Rs 900 crore.
  - https://propnewstime.com/getdetailsStories/MjU2NDg=/ghmc-identifies-over-one-lakh-property-tax-defaulters-begins-recovery-of-more-than-inr-100-crore — undated (snippet) — GHMC (Hyderabad) GIS survey Aug 2024 to Dec 2025 using drone and high-resolution imagery found over 1 lakh defaulters and estimated evasion above Rs 100 crore; an earlier 2018 satellite pilot in Moosapet circle found about 9,000 unassessed structures.
  - https://theprint.in/india/mcd-begins-drone-survey-to-improve-property-tax-assessment-in-delhi/3050283/ — 2 Jun 2026 per search summary (snippet) — MCD signed MoUs with four agencies for a pilot drone survey in two wards; MCD spends nothing on the pilot. No results published yet.
  - https://www.tribuneindia.com/news/himachal/drone-survey-shows-solan-residents-owe-mc-rs-6-5-crore-632043 — undated (snippet) — Solan drone survey assessed about Rs 6.5 crore; 10 per cent of properties still unassessed after a 10-month exercise.
  - https://www.freepressjournal.in/amp/mumbai/navi-mumbai-nmmc-expects-rise-in-property-tax-collection-post-lidar-survey-data — undated (snippet) — Navi Mumbai expects higher collection after a LiDAR survey; Pune and Chennai (GCC) also reported using satellite/GIS (https://www.deccanchronicle.com/amp/southern-states/tamil-nadu/tn-gcc-eyes-under-assessed-wrongly-assessed-properties-for-tax-revision-1978777, snippet).
- Hard number: 7,000 of 9,000 mapped properties in one Nagpur zone differed from the tax register — https://www.nagpurtoday.in/nmc-to-launch-ai-based-property-survey-after-nine-years-to-boost-tax-revenue/ , 29 Oct 2025 (opened). Pune's Rs 1,000 crore added revenue is a projection only (snippet via the Bridge Chronicle, https://www.thebridgechronicle.com/amp/story/pune/drone-survey-exposes-massive-property-tax-evasion-in-pune-agn97).
- Who has tried: ORSAC + Vassar Labs "BLUIS" on Planet SkySat imagery, Bhubaneswar (https://www.planet.com/pulse/?p=147285, snippet), alive, flagged changes go to officials; Nagpur vendor not named; Delhi pilot by four unnamed agencies at no cost to MCD. Funding NOT FOUND. Nobody found who owns the software across many cities.
- Deep-tech wedge (one line): building-footprint change detection plus floor-count and use classification from high-resolution imagery, joined to a tax register, giving inspectors a ranked list of parcels to visit.
- AI/ML core: segmentation / change detection on satellite or drone orthomosaics (building footprints, added floors, roof-use change) plus record linkage to the municipal register. Data: Cartosat / commercial tiles or drone surveys the municipality already commissions; the register from the municipality. Labels come from inspector verification (Nagpur's 380-property check is an example of a label set).
- Buyer: the municipal corporation (commissioner / revenue department); today it pays survey agencies (cost per property NOT FOUND) or does the work by hand. Delhi's pilot shows agencies will work at zero upfront cost, so pricing is likely a share of recovered tax (inference).
- Overnight feasibility: 3. A demo on open imagery (building footprints, change between two dates) is doable; the register join and the precision on real parcels are not.
- Rough market pointer: Nagpur arrears alone exceed Rs 900 crore (opened page); 4,000+ urban local bodies in India (count NOT SEARCHED).
- Risks / regulation: drone use needs DGCA permission; high-resolution imagery licensing; political sensitivity of reassessment; municipal procurement is slow.

## Problem 2: Old and unsafe buildings: mandatory structural audits ignored, collapses repeat
- Track: AI & Systems / Frontier Hardware
- Who suffers: residents of 30-60 year old buildings in Mumbai-Thane, Delhi and other cities; tenants in cess buildings; municipal engineers who cannot inspect everything. Monsoon peaks, every year.
- How they cope today: municipal "dangerous building" lists (C1 to C3), notices to owners to submit structural audit reports, empanelled structural auditors paid by owners (a rebound hammer and visual survey), evacuation orders in monsoon.
- Public proof (tier A on news volume and hard numbers; social engagement NOT FOUND):
  - https://www.tribuneindia.com/news/india/6-killed-as-4-storey-building-collapses-in-bhiwandi-6-7-feared-trapped-under-rubble/ and https://theprint.in/india/ten-killed-as-4-storey-building-declared-unsafe-in-2020-collapses-in-bhiwandi-town/3002209/ — 31 Jul 2026 (snippet) — Kohinoor Apartment, Bhiwandi: 10 dead; declared unsafe in 2020; audit notices issued 2020 and 2022; repairs under way without permission or an audit (preliminary finding: simultaneous repair of multiple columns). Mayor says 130-140 "most dangerous" buildings in Bhiwandi need evacuating (snippet). 2020 Jilani building collapse in Bhiwandi killed 38 (snippet).
  - https://theprint.in/india/bhiwandi-building-collapse-misclassification-let-residents-stay-in-dangerous-structure/3010123/ — 2026 (snippet) — misclassification let residents stay in a dangerous structure.
  - https://thepatriot.in/?p=77115 — 14 Oct 2025 (opened) — Delhi Fire Services data: 247 collapses in FY2024-25 and 384 in Apr-Sep 2025; like-for-like to 20 Apr, 27 collapses vs 12 a year earlier; 2022-23: 349 collapses, 43 deaths, 315 injuries. (The article's "55%" mixes a 6-month and a 12-month count; the like-for-like figure is 27 vs 12.) MCD had declared the Subzi Mandi building unsafe before it fell.
  - https://www.freepressjournal.in/mumbai/mumbai-bmc-seeks-structural-audit-from-4431-sobo-properties — undated (snippet) — BMC wrote to 4,431 owners/tenants in South Mumbai asking for structural audit reports; officials say most do not submit despite yearly notices.
  - https://www.freepressjournal.in/mumbai/navi-mumbai-news-nmmc-declares-501-buildings-dangerous-for-202526-orders-immediate-evacuation-of-51-structures — 2025-26 (snippet) — NMMC declared 501 buildings dangerous, 51 to be evacuated immediately. Also KDMC: 661 unsafe buildings, 143 extremely dangerous still occupied (https://www.freepressjournal.in/mumbai/kdmc-identifies-661-unsafe-buildings-after-bhiwandi-tragedy-143-extremely-dangerous-structures-still-occupied, snippet).
  - Bombay High Court has quashed C1 notices where classification ignored audit reports (snippet in search summary; case not opened).
- Hard number: nearly 7,874 deaths from collapse of structures 2020-2024, Uttar Pradesh 223 and Maharashtra 220 in 2024, attributed to NCRB ADSI — https://superkalam.com/current-affairs/08-09-2026/nearly-8-000-people-died-due-to-collapse-of-structures-in-5-years-pg9-c79eb6d6-d398-44bb-a9e3-3a5e98d72314 , 8 Sep 2026 (snippet; secondary source; NCRB original not opened).
- Who has tried: no Indian startup found for AI structural-health screening of old residential buildings (NOT FOUND; one search did not target it). CAG audit found poor oversight of dangerous buildings by Mumbai civic bodies (https://propnewstime.com/latestnewsstories/MTk4OTg=/cag-flags-poor-oversight-of-dangerous-buildings-by-mumbai-civic-authorities, snippet).
- Deep-tech wedge (one line): low-cost screening tool (phone/drone crack imagery plus vibration from a phone or MEMS sensor) that ranks a city's buildings by risk so engineers inspect the top 5 per cent first.
- AI/ML core: crack and spalling segmentation on facade images; modal-frequency shift from accelerometer data as a damage indicator. Data: no public labelled Indian facade dataset found (NOT FOUND); would have to be built from audit reports and drone passes.
- Buyer: municipal corporation (dangerous-building cell) or housing society committee (owners pay structural auditors today; fee NOT FOUND).
- Overnight feasibility: 2. Crack segmentation demo on open datasets is possible; claiming structural risk is not defensible overnight.
- Rough market pointer: not sized; counts above (501 NMMC, 661 KDMC, 4,431 BMC letters) show the list size per city.
- Risks / regulation: liability if a model says "safe"; structural certification is legally done by licensed engineers; must be framed as triage.

## Problem 3: Under-construction projects: buyers and lenders cannot see real progress against the stated schedule
- Track: AI & Systems / Space Tech
- Who suffers: homebuyers paying construction-linked instalments for projects that stall; lenders and funds (SWAMIH) financing completion; RERA authorities.
- How they cope today: builder-supplied progress photos and RERA quarterly updates (self-reported), site visits by the buyer or an architect, RERA complaints and years of litigation.
- Public proof (tier A on numbers, news only; social engagement NOT FOUND):
  - ICRA (Mar 2026, via search summary, snippet): about 1.56 lakh units stalled across the top seven cities at Dec 2025, nearly 90 per cent in pre-RERA launches — https://www.icra.in/Rating/DownloadResearchSummaryReport?id=6814 .
  - PropEquity (Aug 2024, snippet): about 5.08 lakh units across roughly 2,000 projects in 42 cities stalled — https://constructionworld.in/latest-construction-news/real-estate-news/nearly-2000-housing-projects-stalled-in-india/61017 . The two counts differ by definition and city set.
  - https://www.rprealtyplus.com/index.php/realty-spotlight/what-2025-revealed-about-indias-housing-governance-124136.html — Feb 2026 (snippet) — about 4.8 lakh units delayed over three years; extensions granted on weak grounds.
  - https://www.ghar.tv/blog/maharera-recovery-warrants-crisis-only-31-executed-despite-government-directives/artid3560 and https://rentu.in/news/10001366/maharera-dues-recovery-slows-down-despite-dedicated-officers — Jun 2026 (snippet) — of 1,342 MahaRERA recovery warrants, about 306 executed; Mumbai suburban 540 complaints, Rs 424.79 crore pending recovery, Rs 80.49 crore recovered.
  - SWAMIH Fund 2.0 allocated Rs 650 crore in Union Budget 2026-27 to finish stalled units (snippet, https://www.outlookbusiness.com/corporate/swamih-20-why-indias-booming-housing-market-still-needs-govt-support).
  - https://realtynmore.com/housing-projects-in-india-worth-rs-3-3-lakhs-crores-47-billion-pending-execution-propequity — undated (snippet) — Rs 3.3 lakh crore of housing projects pending execution (PropEquity).
- Hard number: about 1.56 lakh units stalled in top 7 cities, Dec 2025 (ICRA, link above, snippet).
- Who has tried: Track3D (Bay Area + Hyderabad; Rs-equivalent $4.3M seed Sep 2024 led by Endiya, $10M Series A Sep 2025 led by Ironspring; 360 camera/drone/laser) — https://yourstory.com/ai-story/ai-startup-track3d-series-a-funding-ironspring-zacua-ventures (snippet), alive; Contineu (Bengaluru, $1.2M seed led by SenseAI, Tier I developers in Mumbai, Bengaluru, Kolkata, Delhi-NCR) — https://yourstory.com/2025/09/contineu-ai-startup-construction-quality-checks-india (snippet), alive; HUVIAiR (Bengaluru, $3.2M Series A, Boeing earlier investor) — https://www.outlookbusiness.com/news/huviair-raises-3-2-million-in-series-a-funding-round-news-33265 (snippet), alive; Doxel (US, $56.5M, India team); DRA (Chennai developer) adopted an AI site platform Apr 2026 (https://therealtytoday.com/news/technology/ai-and-drones-are-making-construction-progress-more-visible-and-accountable, snippet). All sell to developers; none found selling independent verification to buyers or lenders.
- Deep-tech wedge (one line): independent progress verification (percent complete by floor and trade) from satellite or periodic phone/drone captures, compared with the RERA-declared schedule, sold to lenders and buyer groups.
- AI/ML core: photogrammetry plus per-floor structure/finish classification; for large sites, multi-date satellite change detection. Data: developer's RERA filings (public), drone/phone captures, a few paid site-visit labels.
- Buyer: lenders / SWAMIH-type funds and buyers' associations. Today they pay architects or project-monitoring consultants (rate NOT FOUND). Developers pay the platforms above.
- Overnight feasibility: 3. Floor-count and facade-completion detection from a drone clip of a model or a real site is a plausible demo.
- Rough market pointer: 1.56 lakh to 5 lakh stalled units (ICRA vs PropEquity).
- Risks / regulation: DGCA drone rules; access to private sites; developers resist independent audits; claim that "drone reports count under RERA" was unverified (snippet).
- Overlap: CCTV vision AI for factories (shared computer-vision stack only).

## Problem 4: Handover "snagging": hidden seepage, defects and carpet-area shortfall found only after possession
- Track: AI & Systems / Frontier Hardware
- Who suffers: new-flat buyers at possession, for whom bargaining power falls once they sign; resident societies with tower-wide seepage.
- How they cope today: DIY checklists (NoBroker and builder blogs), a paid snagging inspection costing "a few thousand rupees" (guide claim, snippet), RERA complaint within the 5-year defect liability window under Section 14(3).
- Public proof (tier B; regulator orders and guides, no social metrics found):
  - https://www.livelaw.in/amp/consumer-cases/maharera-grants-relief-to-society-and-homebuyer-directs-builder-to-rectify-structural-defects-that-emerged-after-possession-294361 — (from R1-10) MahaRERA orders repair of structural defects after possession.
  - https://squarefeatindia.com/builder-must-fix-leakage-in-flat-even-after-possession-maharera-orders-rectification-at-builders-cost/ — 4 May 2026 per search summary (snippet) — MahaRERA orders a builder to fix leakage after possession.
  - https://www.therealtytoday.com/news/krera-directs-developer-to-repair-seepage-in-bengaluru-flat-after-buyer-complaint — undated (snippet) — KRERA directs repair of seepage in a Bengaluru flat.
  - https://www.freepressjournal.in/mumbai/consumer-connect-maharera-mandates-refund-for-carpet-area-shortfall-within-3-variation-cap — Jun 2026 (snippet, headline only) — MahaRERA mandates refund for carpet-area shortfall within a 3 per cent variation cap; Punjab RERA on extra area charges, https://www.businesstoday.in/personal-finance/real-estate/story/paid-more-for-extra-area-punjab-rera-clarifies-when-builders-can-charge-more-534031-2026-05-29 (May 2026, snippet).
  - https://citizenmatters.in/?p=12924 — undated (snippet) — "Why you should pay attention to home inspection during property handover".
  - https://www.team-bhp.com/forum/shifting-gears/219249-did-you-ever-get-cheated-builder-while-buying-house-share-tips-advice-here.html — undated (snippet) — forum thread of buyers cheated by builders; reply counts NOT FOUND.
- Hard number: no count of handover-defect complaints found (NOT FOUND). Closest: seepage is "among the most commonly claimed" RERA defects (guide, snippet) and MahaRERA had received about 33,806 complaints with 6,224 pending by Mar 2026 (snippet, https://propnewstime.com/getdetailsStories/MjczMjQ=/maharera-faces-backlog-with-over-6-300-unresolved-complaints-as-of-december-2025), not split by cause.
- Who has tried: no dedicated Indian snagging startup with funding found in two searches (NOT FOUND). Contineu (see Problem 3) does QA/QC for developers during construction, not buyer-side.
- Deep-tech wedge (one line): a phone-plus-thermal-attachment inspection app: LiDAR room scan for carpet area vs agreement, thermal and moisture reading for seepage, tap-test audio for hollow tiles, auto-generated snag report in RERA format.
- AI/ML core: LiDAR plane fitting for area, thermal image anomaly detection for moisture, audio classifier for hollow vs solid tile. Data: self-collected; no public Indian dataset found.
- Buyer: the flat buyer (B2C), or developers and banks who want a record; buyer pays a snagging inspector a few thousand rupees today (guide claim, snippet).
- Overnight feasibility: 4. LiDAR area measurement and a tap-test classifier are demoable with a phone and a hammer.
- Rough market pointer: not sized. Flat handovers per year NOT SEARCHED.
- Risks / regulation: thermal cameras on phones are low-resolution; a false "no seepage" claim creates liability; B2C acquisition cost.

## Problem 5: Rental security-deposit disputes and move-out damage claims with no neutral condition record
- Track: AI & Systems
- Who suffers: tenants in Bengaluru, Mumbai, Delhi-NCR (deposits of 6 to 10 months' rent are quoted for Mumbai and Bengaluru); landlords who do face real damage.
- How they cope today: photos and video at move-in (advised in articles), legal notices, consumer forums; rental agreements on stamp paper.
- Public proof (tier A: five or more independent items plus a hard number; Reddit counts NOT FOUND because the sub was unreachable):
  - https://www.businesstoday.in/latest/trends/story/rs1-lakh-deposit-rs19604-returned-bengaluru-tenant-alleges-massive-deduction-by-landlord-542774-2026-07-14 — 14 Jul 2026 (opened) — r/bangalorerentals post, "hundreds of reactions": Rs 1 lakh deposit, Rs 80,396 deducted, Rs 19,604 returned, for repainting, polishing and plumbing the tenant calls renovation for the next tenant.
  - https://www.businesstoday.in/latest/trends/story/birthday-buddy-to-un-level-auditor-bengaluru-tenants-exit-shock-over-rs20k-cuts-523343-2026-03-31 — 31 Mar 2026 (snippet) — Bengaluru tenants shocked over Rs 20k cuts.
  - https://www.freepressjournal.in/viral/bengaluru-tenant-alleges-owner-cut-51000-security-deposit-to-repaint-flat-reddit-post-sparks-debate — undated (snippet) — Reddit post: Rs 51,000 cut to repaint.
  - https://www.businesstoday.in/personal-finance/real-estate/story/the-biggest-scam-in-bengaluru-investment-advisor-calls-out-citys-rental-deposit-trap-472022-2025-04-15 — 15 Apr 2025 (snippet) — an adviser calls the deposit "the biggest scam in Bengaluru".
  - https://newsable.asianetnews.com/karnataka-news/bengaluru-rent-horror-man-claims-rs-80000-vanished-from-rs-1-lakh-security-deposit-viral-post-sparks-debate-articleshow-b8xwke6 — undated (snippet) — Rs 80,000 vanished from a Rs 1 lakh deposit; also https://www.deccanherald.com/amp/story/india%2Fkarnataka%2Fbengaluru%2Fbengaluru-security-deposit-scam-landlord-vanishes-without-returning-deposit-to-tenant-3775530 (snippet).
  - https://therealtytoday.com/news/landlords-5-lakh-security-deposit-for-40000-flat-in-bengaluru-stirs-social-media-outrage-amid-rising-rental-prices — undated (snippet) — Rs 5 lakh deposit for a Rs 40,000 flat triggers outrage.
- Hard number: Rs 1,26,042 crore in security deposits held by owners across six metros (Mumbai Rs 41,156 crore, Bengaluru Rs 31,628 crore, Delhi-NCR Rs 24,054 crore), NoBroker Rent Report 2026 via secondary coverage — https://www.businesstoday.in/personal-finance/story/rs1-26-lakh-crore-in-rental-deposits-how-verified-data-could-transform-indias-housing-market-553799-2026-09-08 (8 Sep 2026, snippet) and https://www.outlookmoney.com/personal-finance/nearly-half-of-urban-indians-now-prefer-renting-long-term-report (snippet). Survey figures (RentOk write-up, snippet, https://wb.rentok.com/case-study/security-deposits-the-hidden-cost-of-renting/): 75 per cent of tenants gave up a liked property over the deposit; 44 per cent got full deposit back (tradebrains, https://tradebrains.in/money/?p=11587, snippet) and 11 per cent never recovered it. Both are platform surveys with unknown samples.
- Who has tried: NoBroker (unicorn since Nov 2021, $210M Series E; $5M from Google Mar 2023 at $1B post-money; targeting profit; https://inc42.com/features/nobrokers-future-is-beyond-home-listings-but-will-profits-follow/ , snippet), alive; RentOk (rental management platform, funding NOT FOUND); Model Tenancy Act caps residential deposits at two months where adopted, not in Karnataka (snippet). No product found that issues a time-stamped condition report.
- Deep-tech wedge (one line): guided move-in / move-out room capture (video walk-through) with a vision model that diffs the two and prices only genuine damage, producing a neutral report both sides sign.
- AI/ML core: image alignment and change detection between two walk-throughs; VLM to label damage vs wear and tear; cost estimator trained on repair quotes. Data: tenant captures; repair price lists from painters/plumbers (collectable).
- Buyer: rental platforms, PG/co-living operators and property managers (need dispute reduction), or landlords/tenants paying per report. Today tenants pay nothing and fight informally; landlords pay a painter.
- Overnight feasibility: 4. Two-video diff plus damage labels is demoable.
- Rough market pointer: Rs 1.26 lakh crore of deposits (above); a 1 per cent leakage is about Rs 1,260 crore (simple arithmetic, my calculation).
- Risks / regulation: privacy of tenants' rooms; the report has no legal standing unless parties agree; likely a feature for an existing platform, a thin business alone.

## Problem 6: Land and title: digitised records that do not match the ground, forged and double-registered deeds
- Track: AI & Systems
- Who suffers: farmers and plot buyers (Telangana's Dharani is the worst documented case), banks and NBFCs doing title search before a mortgage, buyers of plots in Hyderabad-style suburbs.
- How they cope today: a lawyer's title search (several days, per-case fee NOT FOUND), certified copies from the sub-registrar, encumbrance certificates, litigation.
- Public proof (tier A: five or more independent items and hard numbers; engagement is news-level):
  - https://deccanchronicle.com/southern-states/telangana/massive-discrepancies-identified-between-sethwar-and-dharani-land-records-1861663 — undated (snippet) — Sethwar registers show about 26.98 lakh acres under base survey numbers in certain districts; Dharani lists about 32.80 lakh acres, roughly 6 lakh acres more; traced to by-survey numbers for land that does not exist; data uploaded 2016 with no field verification.
  - https://thehansindia.com/telangana/dharani-proves-a-bane-for-25k-families-across-state-924248 — undated (snippet) — about 25,000 families affected statewide (headline figure).
  - https://telanganatoday.com/bhu-bharati-struggles-to-deliver-promised-justice-to-farmers — 20 Jun 2026 (snippet) — rejections outpace approvals under the new Bhu Bharati portal; "RSR mismatch" applications rejected despite sale deeds. Also https://www.siasat.com/?p=3230677 and https://telanganatoday.com/telangana-landowners-face-fresh-hurdles-on-bhu-bharati-portal (30 Oct 2026, snippet).
  - https://www.landconflictwatch.org/conflicts/digitisation-dispossession-and-discrepancies-inside-kerala-s-digital-land-resurvey — undated (snippet) — Kerala digital resurvey discrepancies.
  - https://www.geosquare.in/hyderabad-real-estate-scandal-rs-1526-crore-fraud-through-double-registration-39138-news.html — 2026 (snippet) — double registration of plots at Quthbullapur sub-registrar office, about Rs 15.26 crore; a Hyderabad chargesheet in Jan 2026 covered a Rs 3,000 crore pre-launch fraud with 2,500 victims (snippet, via the fake-listings search result).
  - Daksh figure that land and property cases are about two-thirds of pending civil suits is a survey estimate; NJDG keeps no separate land category (Rajya Sabha 2022 answer: https://rsdebate.nic.in/bitstream/123456789/726049/1/PQ_256_24032022_U2507_p390_p391.pdf , snippet; page not opened).
- Hard number: about 6 lakh acres more in Dharani than in the Sethwar register (link above, snippet).
- Who has tried: Landeed (Hyderabad/Bengaluru; YC-backed; $2.5M pre-seed 2022, $8.3M seed Jan 2023 led by Draper and Bayhouse, $5M "Series X" Jan 2025 led by 10x Founders Fund for an AI/ML unit "Landeed Labs"; title search via one national app; plans title insurance) — https://yourstory.com/2025/01/proptech-startup-landeed-series-x-funding-round-ai-powered-property-title-search-platform , https://inc42.com/buzz/landeed-bags-5-mn-to-boost-its-ai-ml-stacks (snippets), alive in Jan 2025, 2026 status NOT FOUND. IRDAI has pushed title insurance since 2016-2021 (https://www.personalfn.com/dwl/insurance/all-you-should-know-about-the-new-title-insurance-policy-introduced-by-the-irdai , snippet). Teal, Zapkey, Propstack, CRE Matrix, PropertyChek, SmartOwner: no funding or status found (one search, NOT FOUND).
- Deep-tech wedge (one line): document AI that reads scanned sale deeds, mutation entries and RoR extracts in Telugu, Kannada, Hindi and Marathi, builds the chain of title, and flags survey-number gaps, phantom by-survey numbers and duplicate registrations.
- AI/ML core: OCR + layout model on old scanned deeds; named-entity extraction (parties, survey numbers, extent); graph/entity matching across deeds and records; anomaly rules on areas (e.g. sum of by-survey extents greater than base extent). Data: encumbrance and registry copies per property (state registration portals), RoR portals; no public training set found.
- Buyer: banks and NBFCs (title search cost per mortgage), title insurers, large buyers. Today they pay panel lawyers (fee NOT FOUND).
- Overnight feasibility: 3. A deed-to-chain-of-title extractor on a handful of sample deeds is demoable; accuracy on real handwritten deeds is not.
- Rough market pointer: not sized; Landeed's $5M AI round shows investors fund it.
- Risks / regulation: data access varies by state portal; registration verifies execution, not ownership (snippet, https://webiis08.mondaq.com/india/real-estate/1727536/registration-is-not-ownership-why-a-sale-deed-is-only-the-beginning), so output is a risk report, not a title opinion.

## Problem 7: Illegal construction and encroachment seen from the sky
- Track: Space Tech & Defence / AI & Systems
- Who suffers: civic bodies, defence estates, slum rehabilitation authorities; residents of unauthorised colonies where bylaws are ignored (Delhi collapses, Problem 2).
- How they cope today: field inspectors, complaint apps, periodic survey contracts.
- Public proof (tier B; government announcements, results sparse):
  - https://pib.gov.in/PressReleasePage.aspx?PRID=1839200 — 2022 (snippet) — DGDE AI change-detection tool with BARC on Cartosat-3 imagery: of 1,133 unauthorised changes detected, action taken in 570.
  - https://www.freepressjournal.in/amp/mumbai/bmc-approves-ai-drone-satellite-tech-to-detect-illegal-constructions-and-encroachments-across-mumbai — undated (snippet) — BMC General Body approved AI, drone and satellite monitoring with a geo-tagged complaint app; also https://yourstory.com/ai-story/bmc-ai-drones-satellites-illegal-buildings-mumbai (snippet).
  - https://www.freepressjournal.in/amp/mumbai/mumbai-sra-floats-tender-for-high-resolution-satellite-imagery-to-strengthen-slum-monitoring-and-track-unauthorised-development — undated (snippet) — SRA tender for high-resolution imagery, integrated with its Netram platform.
  - https://www.millenniumpost.in/delhi/gda-to-use-ai-satellite-imagery-to-curb-illegal-construction-608651 — undated (snippet) — Ghaziabad Development Authority to compare imagery with approved maps across eight zones.
  - https://thepatriot.in/?p=77115 — 14 Oct 2025 (opened) — Delhi has 1,731 unauthorised colonies (DDA), and an MCD official blames them for repeat collapses.
- Hard number: 1,133 unauthorised changes detected, 570 actioned (DGDE, link above, snippet).
- Who has tried: Vassar Labs / ORSAC (Bhubaneswar BLUIS on Planet imagery, snippet above), DGDE with BARC (in-house), Planet Labs as imagery supplier. Funding for vendors NOT FOUND. Same technology stack as Problem 1.
- Deep-tech wedge (one line): same change-detection engine as Problem 1, sold to development authorities for enforcement rather than tax.
- AI/ML core: bi-temporal change detection on sub-metre imagery; compare detected footprints against approved layout polygons. Data: approved maps are scanned PDFs in most authorities (inference); imagery from Planet/Maxar or drones.
- Buyer: development authorities, defence estates, SRA, forest departments. Pay today: survey agencies and imagery tenders (amounts NOT FOUND).
- Overnight feasibility: 3 (same as Problem 1). Treat Problems 1 and 7 as one product with two buyers.
- Rough market pointer: not sized.
- Risks / regulation: demolition decisions are political and legal; false positives anger citizens; satellite imagery licensing.

## Problem 8: Housing-society sewage treatment plants that exist on paper but do not run
- Track: Frontier Hardware & Climate
- Who suffers: residents (untreated sewage into drains and groundwater), RWAs that face penalties and water cut-offs; rivers and lakes downstream.
- How they cope today: an operator contract, occasional pollution-board inspections, penalties.
- Public proof (tier B; enforcement counts, no social metrics):
  - https://www.freepressjournal.in/pune/pune-pimpri-chinchwad-civic-body-warns-99-societies-over-non-operational-stps — undated (snippet) — PCMC: 99 societies (over 100 flats each) kept STPs non-operational despite three notices; societies cite maintenance costs.
  - https://www.freepressjournal.in/amp/pune/pune-pcmc-cuts-water-to-24-societies-over-faulty-stps-in-pimpri-chinchwad — undated (snippet) — PCMC cut water to 24 societies.
  - https://www.geosquare.in/pune-and-pimpri-chinchwads-rivers-and-groundwater-threatened-by-defunct-stps-36510-news.html — undated (snippet) — 125 private STPs with a combined 23 MLD capacity are non-functional.
  - https://magazine.watertoday.org/news/national/kspcb-bwssb-joint-team-bengaluru-stp-monitoring-bengaluru-sewage-treatment-plant-inspection-kspcb-golden-jubilee-bengaluru-90-percent-bengaluru-stps-failing — undated (snippet) — KSPCB chairman said 90 per cent of Bengaluru's STPs are non-functional (single official statement, not audited).
  - https://citizenmatters.in/bengaluru-apartment-sewage-treatment-plants-stp-kspcb-approval-cfe-cfo-reforms/ — undated (snippet) — apartment STPs malfunction soon after approval; residents spend lakhs on fixes.
  - https://www.tribuneindia.com/news/archive/haryana/gmda-issues-notices-to-366-housing-societies-814509 — undated (snippet) — GMDA notices to 366 housing societies (Gurugram). A vendor blog says NGT upheld a Rs 68.25 lakh penalty for 182 days of STP non-compliance (https://susbio.in/what-happens-if-your-society-has-no-stp-penalties-2026/ , snippet, vendor claim, unverified).
- Hard number: 125 non-functional private STPs, 23 MLD, in Pune/PCMC (geosquare link above, snippet).
- Who has tried: service vendors (Susbio and similar; funding NOT FOUND). No IoT STP-compliance monitoring startup found (NOT FOUND, not specifically searched).
- Deep-tech wedge (one line): a low-cost sensor kit on the STP (outlet turbidity/COD proxy, flow, aerator current, tank level) with a regulator-grade log and alarm so the RWA can prove it complied and a municipality can see which plants are dead.
- AI/ML core: anomaly detection on aerator current and flow to detect "plant off" or bypass; soft-sensor regression for BOD/COD from turbidity, pH and conductivity. Data: lab samples from partner societies; none public.
- Buyer: RWA / builder-run societies (avoid penalties) and municipal / pollution boards (monitoring). Today RWAs pay an operator and pay penalties; amounts NOT FOUND.
- Overnight feasibility: 4. Current clamp plus turbidity sensor plus an alarm dashboard is buildable with hardware on hand.
- Rough market pointer: not sized; 99 + 125 + 366 figures give per-city plant counts only.
- Risks / regulation: disclosure risk for societies; sensors in wet environments foul quickly; spot-sample compliance is what regulators accept today.

## Problem 9: Housing-society water: tanker bills with no litres measured at the sump (from R2-03)
- Track: Frontier Hardware & Climate
- Who suffers: RWAs in Bengaluru and Gurugram that spend lakhs a month on tankers and cannot check what they receive.
- How they cope today: tanker contracts, RWA maintenance funds, per-flat meters sold by startups.
- Public proof (tier B; reused from R2-03, whose own verdict was thin public engagement):
  - https://www.tribuneindia.com/news/haryana/200-societies-along-dwarka-e-way-suffer-at-the-hands-of-tanker-mafia-634420 — 26 Jun 2024 — more than 200 societies on Dwarka Expressway hit by the tanker mafia; Rs 5,000 for a 5,000 L tanker; one RWA spent about Rs 10 lakh in three months (from R2-03).
  - https://opencity.in/bengaluru-water-tankers-survey-2025-situation-better-than-2024/ — 27 Oct 2025 — OpenCity + Bangalore Apartments Federation survey: just over 50 per cent better than 2024, 13.4 per cent worse; emergency buyers pay almost double (from R2-03).
  - https://the-ken.com/story/nobroker-wanted-to-eat-mygates-lunch-but-housing-societies-had-other-ideas/ — MyGate about 27,000 societies (snippet, from R2-03). YouTube: Jar App "Why does Bangalore have Tanker Mafia?" 20,805 views, 22 Mar 2025 (from R2-03).
- Hard number: about Rs 10 lakh in three months on tankers and pipeline repairs by one Dwarka Expressway RWA — Tribune, 26 Jun 2024 (from R2-03).
- Who has tried: WEGoT (Chennai; $2M seed Oct 2019, about $5M total; claimed 30,000+ homes Dec 2021; 2025 status NOT FOUND) and SmarterHomes / WaterOn (per-flat meters Rs 3,999-4,999) — https://yourstory.com/2019/10/funding-iot-based-water-crisis-management-startup-wegot-gofrugal/amp ; BWSSB Sanchari Cauvery GPS-tracked tankers (May 2025, https://www.theweek.in/news/india/2025/05/10/sanchari-cauvery-launched-to-curb-private-water-tanker-mafia-in-bengaluru.html) (all from R2-03). Gap noted by R2-03: nothing reconciles tanker bills against litres measured at the sump.
- Deep-tech wedge (one line): ultrasonic sump level plus tanker-arrival log to reconcile litres billed and received, with a "days of water left" forecast.
- AI/ML core: light. Time-series forecasting of consumption and drawdown; anomaly detection on level traces (short-fill). Data: own sensors. Honest note from R2-03: the wedge rests on an unproven claim that tankers short-fill.
- Buyer: the RWA, from maintenance funds (from R2-03).
- Overnight feasibility: 4. Level sensor plus dashboard.
- Rough market pointer: R2-03 used 25,000-30,000 app-managed societies as a national proxy.
- Risks / regulation: R2-03 scored deep-tech 2 and proof 3; included here for completeness since it is housing-society operations.

## Problem 10: Construction-site safety and concrete quality: deaths with poor data, quality checked by cubes after the pour
- Track: AI & Systems / Frontier Hardware
- Who suffers: construction workers (falls, electrocution, collapse), developers and contractors facing delays and rework, owners of buildings with weak concrete.
- How they cope today: manual site walks, safety officers on large sites only, cube tests at 7 and 28 days (after casting), state BOCW welfare boards recording deaths.
- Public proof (tier B; news and parliament data, no social engagement found):
  - https://rsdebate.nic.in/bitstream/123456789/759389/1/PQ_267_20032025_U2332_p407_p408.pdf — 20 Mar 2025 (snippet) — Rajya Sabha answer: updated data on construction-worker deaths and injuries is held by the state BOCW boards; no central figure.
  - https://www.deccanherald.com/india/karnataka/millions-of-workers-minimum-safety-in-construction-boom-3940155 — 2026 (snippet) — Karnataka board data: 223 construction-worker deaths between 2020-21 and 2025-26.
  - https://www.counterview.in/2026/04/gujarat-records-1746-construction.html — Apr 2026 (snippet) — Gujarat 2025: 130 deaths and 17 serious injuries reported; 88 per cent at private sites.
  - https://www.business-humanrights.org/ja/最新ニュース/india-british-safety-council-report-says-48000-die-yearly-due-to-occupational-accidents — undated (snippet) — British Safety Council study cited about 11,616 construction deaths per year and 25 per cent from falls (secondary estimate; a 2016 paper gave 11,614-22,080, https://pmc.ncbi.nlm.nih.gov/articles/PMC9306058 , snippet).
  - https://www.thequint.com/opinion/gurugram-collapse-when-citizens-pay-for-indias-shoddy-construction-practices — undated (snippet) — opinion: cubes are tested at 7 and 28 days after the concrete is cast; https://www.occrp.org/en/daily/1920-india-corruption-confirmed-in-deadly-building-collapse (snippet) — corruption confirmed in a deadly collapse. 2013 Thane and 2021 Mumbai Altaf Mansion inquiries looked at substandard cement (snippets).
- Hard number: national estimate of about 11,616 construction deaths per year (British Safety Council, secondary, snippet); the only primary Indian numbers are state-level (Karnataka 223 over six years).
- Who has tried: Contineu (Bengaluru, $1.2M seed, helmet 360 cameras for QA/QC and compliance; first aim quality, then safety and progress) — https://yourstory.com/2025/09/contineu-ai-startup-construction-quality-checks-india (snippet), alive; Track3D, HUVIAiR, Doxel (Problem 3); Powerplay (Bengaluru site-management app, Accel and Surge, $5.2M, date unverified, snippet); Flo Mobility (Inc42 https://inc42.com/?p=550251, snippet). NDT-based concrete testing startups in India: NOT FOUND.
- Deep-tech wedge (one line): PPE / fall-hazard detection from existing site cameras plus embedded wireless maturity sensors in the pour giving live strength estimates, so a pour can be signed off without waiting 28 days.
- AI/ML core: object detection for helmets, harnesses and edge exposure on site CCTV; maturity-method strength curve from embedded temperature sensors. Data: site CCTV (developer-owned); labelled PPE datasets exist globally, India-specific NOT FOUND.
- Buyer: large developers and EPC contractors (safety and quality heads); insurers. Pays today: safety officers' salaries and third-party labs (amounts NOT FOUND).
- Overnight feasibility: 4 for PPE detection on sample video; 2 for the concrete sensor.
- Rough market pointer: not sized.
- Risks / regulation: worker surveillance and privacy; informal sites rarely have cameras (88 per cent of Gujarat accidents at private sites, snippet).
- Overlap: CCTV vision AI for factories (same detection stack, different site).

---

## Already covered (do not research again; see R1-10 and R2-02/R2-03 reports)
- Lift-monitoring retrofit "lift black-box" for housing societies (R1-10 Problem 4; R2-03 U4): UP Lift and Escalator Act 2024 registration, KALA (PAPL/Ardelisys) competitor.
- Smart-meter bill explainer with leakage detection (R2-02).
- EV charging-bay monitor for apartment complexes (R2-02 E3): Haryana building code 5 Jun 2026; RWAs removing chargers.
- Indoor / outdoor air-quality pair (R2-03).
- Housing-society water and tanker reconciliation is also in R2-03; it is repeated as Problem 9 only to keep the proptech list complete.

## Logged but weak
- Fake rental listings and advance fraud: Mumbai cyber police alert 4 Nov 2025 (opened, https://www.freepressjournal.in/amp/mumbai/mumbai-news-cyber-police-issue-alert-on-online-rental-scam-citizens-warned-against-fake-property-listings, no loss count given); "deposit-zero" racket Rs 47 lakh, Kashimira (snippet); Bengaluru Telegram scam; Mumbai man lost Rs 2.8 lakh on a fake NoBroker listing (snippet, https://www.freepressjournal.in/amp/mumbai/mumbai-cyber-fraud-44-year-old-man-duped-of-28-lakh-in-nobroker-rental-scam-money-withdrawn-from-bhopal-petrol-pump-account). Marketplace and fraud-ops problem; the AI wedge (listing verification) belongs to platforms. Tier B.
- Commercial building HVAC waste: HVAC 40-60 per cent of commercial building energy and 10-25 per cent savings from BMS optimisation are consultant claims (https://aikosh.indiaai.gov.in/home/use-cases/details/a_retrofit_first_ai_strategy_delivers_efficiency_gains_in_buildings.html , snippet); NHance.ai case study claims 32 per cent HVAC waste cut and Rs 4.8 lakh a year in a Bengaluru office (vendor, https://www.casestudies.com/company/nhanceai/case-study/bengaluru-office-cuts-hvac-energy-waste-by-32-with-nhanceai , snippet); Curie Labs claims 25 per cent bill cuts (vendor). Tier C: only vendor claims, no public complaints.
- Valuation / circle rates / bank valuation fraud: mechanism explained (circle rate is a floor; duty on the higher value) but no public proof of AI valuation demand or of bank valuation fraud found (one search; NOT FOUND).
- Tenant and police verification: not searched (down-weighted by the brief).
- Square Yards ($35M round and IPO preparation; Rs 1,410 crore operating revenue as second-largest proptech behind Livspace) and HouseEazy ($7M Series A Aug 2024, Chiratae) are alive per https://entrackr.com/report/after-2024-revival-indian-proptech-raises-550-mn-in-2025-amid-full-stack-shift-and-ipo-wave-11069442 and https://www.outlookbusiness.com/corporate/proptech-startup-houseeazy-raises-usd-1-mn-from-investors-as-seed-funding (snippets). Indian proptech raised over $550M in 2025 (Entrackr, snippet). MACJ, Propstack, Zapkey, CRE Matrix, PropertyChek, SmartOwner, Aurum, WeHouse: status NOT FOUND.
- Housing-society maintenance-fund disputes, seepage between flats, common-area power: not searched.

## NOT SEARCHED
- NCRB ADSI original table for "collapse of structures" (only secondary summaries seen).
- Reddit and YouTube engagement for any problem (Reddit unreachable, YouTube not searched); LocalCircles proptech surveys (none surfaced in one targeted search).
- Per-case price of a lawyer's title search; price of a structural audit; price of a paid snagging inspection beyond "a few thousand rupees" (guide claim).
- Funding and status of Teal, Zapkey, Propstack, CRE Matrix, PropertyChek, SmartOwner, MACJ, Aurum, WeHouse, Powerplay (date), Landeed in 2026.
- Number of urban local bodies and their property-tax budgets; annual flat handovers; number of RWAs in India.
- Delhi MCD 2026 pilot results; BMC / GDA AI enforcement outcomes.
- Tenant verification, police verification and rental agreement stamp-duty problems.
- Construction material theft and labour attendance fraud.

Searches used: 32 (WebSearch). Also 4 WebFetch page opens succeeded; 4 Arctic Shift fetches failed with HTTP 422.
