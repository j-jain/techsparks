# R4-04 Funded - YC and a16z  (agent: Sonnet, date 2026-11-12)

Scope: YC (W25 onward) and a16z deals announced since Jan 2025. Where I opened the page, no tag; "(snippet)" = search-result text only. YC company pages usually do not state funding; where no amount was seen I say "amount not seen". Founder-reported traction is company-reported unless stated. 20 full entries (12 YC, 8 a16z). Round-4 dates: Fall 2026 and Winter 2027 RFS pages exist; I used the live YC RFS page I could open.

## YC Requests for Startups that match Indian problems

Source for the list below: https://www.ycombinator.com/rfs (opened 2026-11-12; page showed only the Winter 2027 list, 11 requests) and the Summer 2026 list as described at https://thenextweb.com/news/yc-summer-2026-rfs-hard-tech-pivot (opened; 11 of 15 requests described).
- **AI for City Hall** (permits, inspections, 311) — Winter 2027 RFS. Indian match: municipal building-plan approval already being automated by the state: BMC "CivitTwin" AI pre-scrutiny (https://www.freepressjournal.in/mumbai/bmc-launches-indias-first-ai-based-civittwin-system-for-faster-building-approvals, snippet, undated), DDA single-window AI CAD scrutiny (https://theprint.in/india/dda-rolls-out-ai-driven-single-window-system-to-streamline-building-approvals-in-delhi/2929206/, snippet). Buyer in India is the municipality, so the wedge is the architect-side pre-check (see Structured AI entry).
- **Plaid for Government Benefits** (verify income/tax/residency once, apply to many programs) — Winter 2027 RFS. Indian match: DigiLocker/DBT/Aadhaar-linked schemes; the India version is a consent layer for scheme eligibility. Not searched for numbers.
- **The $15-an-Hour Expert** (AI lets uncredentialed workers do finance/law/healthcare-billing work) — Winter 2027 RFS. Indian match: India's medical-billing and clinic back-office labour pool (see Lassie, Avelis).
- **Vertical Foundation Models** for manufacturing, energy, biology — Winter 2027 RFS. Indian match: MSME factory data; no search done.
- **AI for the Air-Gapped Economy** (offline on-prem AI for defence, banking, healthcare) — Winter 2027 RFS. Indian match: banks/NBFCs and public-sector firms with data-localisation rules; no search done.
- **Robots Made in America** (domestic robot supply chain: magnets, grippers) — Winter 2027 RFS. Indian mirror: rare-earth magnet scheme, see Westmag entry.
- **AI for low-pesticide agriculture** (real-time weed/pest ID, robotic spot treatment) — Summer 2026 RFS (Garry Tan). Indian match: smallholder spraying; no search done.
- **Semiconductor supply chain software** — Summer 2026 RFS; **AI Personalized Medicine** — Summer 2026 RFS; **SaaS Challengers** (AI-native ERP, industrial control, supply chain) — Summer 2026 RFS. No Indian check done.

---

## Adialante — mobile whole-body MRI trucks that bring prostate-cancer screening to clinics, paid per scan (YC S26)
- Backers and round: Y Combinator Spring 2026 batch; $500,000 YC investment per Marquette alumni story (snippet): https://today.marquette.edu/2026/04/igniting-change-in-cancer-screening-alumnus-dr-efrain-torres-entrepreneurial-journey-to-servant-leadership/ ; batch confirmed by TechCrunch 18 Jun 2026: https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/ . Seed round reported still open (snippet, healthcarediscovery.ai). Aggregator totals conflict ($500K vs $3.47M); treat amount as unsettled.
- Problem, customer, how it works: urology clinics cannot buy a multi-crore MRI. Adialante owns and operates compact scanners (claimed ~50% less hardware, ~80% lighter, no special infrastructure) and brings them in trailers; clinic pays a per-scan fee and recoups via insurance. AI role is thin: "continuously improve our AI software after every scan". The real moat is hardware physics, not ML. https://www.ycombinator.com/launches/QLh-adialante-we-re-going-to-screen-the-world-for-cancer
- Traction signals: 6 clinics signed up, $12.75M in letters of intent, $30k deposit, an assembled scanner, 2 patents (same launch page; founder-reported). No FDA clearance yet (snippet, healthcarediscovery.ai).
- Does India have this problem? Prostate cancer: 37,948 Indian men in 2022, about 3% of 14 lakh cancers, per a WHO-derived news report (snippet): https://telanganatoday.com/prostate-cancer-cases-rising-in-men-under-50-in-india . Lancet-commission-style range 33,000-42,000 new cases a year, doubling to ~71,000 by 2040 (snippet, same search). A hospital blog says ~85% found at stage 3-4 but I could not verify it against a registry; do not use without checking. No national organised screening programme (snippet).
- Indian equivalents: VoxelGrids (Bengaluru, Tata Trusts-linked) indigenous MRI, machine ~Rs 3.5 cr vs Rs 5-8.5 cr imported, exploring mobile units and pay-per-use (snippet; company claims): https://www.tata.com/newsroom/faster-cheaper-accessible-mri-scanner-tata-trusts ; Cent (full-body MRI, price not found); Time Medical low-field MRI (aneurysm screening); BPL Medical mobile AI mammography bus, Hyderabad (snippet): https://biovoicenews.com/world-cancer-day-bpl-medical-technologies-equips-indias-first-ai-integrated-mobile-cancer-screening-bus/ . Funding for each: not found.
- What differs in India: price (a clinic-level per-scan fee must be a few thousand rupees, not "hundreds of dollars"); buyer is a diagnostic chain or CSR/state programme, not insurer reimbursement; no PSA habit; regulator is CDSCO plus AERB-style rules for imaging; power and cooling for a trailer.
- India version sketch: do not build the MRI. Build the software layer: an AI triage that reads a PSA value plus age/family history plus a low-field or existing hospital MRI and scores who needs the scan, delivered through a pay-per-use dashboard for a diagnostic chain. Demo with public prostate MRI datasets (PI-CAI) and a mocked booking flow.
- Overnight-demo potential: 2/5. Hardware cannot be shown; the ML part is a public-dataset classifier only.
- Overlap: none.

## Automax.ai (and ValueMate) — LiDAR phone scans plus AI agents produce mortgage appraisals in minutes (YC F25; ValueMate X25)
- Backers and round: Y Combinator Fall 2025 (https://www.ycombinator.com/companies/automax-ai , via search; batch per snippet). Amount not seen. ValueMate (YC Spring/X25) does a similar phone LiDAR workflow: https://yespress.io/valuemate-yc-x25 (snippet).
- Problem, customer, how it works: US mortgage appraisals are slow. Automax is itself an appraisal firm: a certified inspector scans the property with an app, LiDAR plus computer vision extract 150+ attributes (dimensions, condition, finishes), AI agents pick and adjust comparables, a licensed appraiser signs. Under 10 minutes for AI draft, report in under 20 min end to end. https://www.ycombinator.com/launches/Oq3-automax-ai-powered-property-appraisals-in-minutes
- Traction signals: earlier tooling produced 3,000+ reports a month; taking orders in California and Colorado (same launch page, founder-reported). A competitor's forum post alleges per-appraisal pricing of $30 for the copilot; unverified (snippet).
- Does India have this problem? Banks and housing finance firms mostly use manual valuation: Valocity states this (snippet): https://www.valocityglobal.com/en-sg/2021/12/the-role-of-technology-in-the-indian-mortgage-valuation-ecosystem (2021, dated). Hard Indian number on valuation turnaround: NOT FOUND.
- Indian equivalents: Navanc (Bengaluru, $1M seed, AI property score for secured lending; 2024-25, snippet): https://housing.com/news/navanc-raises-1m-seed-funding-to-revolutionize-secured-lending-with-ai-powered-property-score/ ; AdvaRisk Instant Ownership Check (backed by ICICI Bank/NABARD, 14 states; snippet): https://www.business-standard.com/amp/finance/personal-finance/this-new-ai-tool-could-speed-up-your-home-loan-and-prevent-property-fraud-125051300337_1.html ; Valocity (valuer field-capture tool); Magicbricks PropWorth. None found using LiDAR in valuation.
- What differs in India: no comparable-sales database (registered value vs real price gap, unregistered cash component); title and legal opinion is a bigger part of risk than the appraisal; valuers are empanelled by each bank; carpet vs super-built-up area measurement is the daily dispute, which is exactly what LiDAR measures.
- India version sketch: phone-LiDAR (iPhone Pro) walk-through that outputs carpet area, room dimensions, floor-plan and a condition score from photos, formatted as a bank-valuer annexure. Sold to empanelled valuers at a per-report fee.
- Overnight-demo potential: 4/5. iPhone LiDAR/RoomPlan scan plus a vision-model condition score plus PDF report is feasible in hours.
- Overlap: none.

## Brumby (ex-GrazeMate) — autonomous drones that herd cattle between paddocks using reinforcement learning (YC W26)
- Backers and round: $1.2M pre-seed led by Y Combinator with Antler and NextGen Ventures, plus Meat & Livestock Australia (snippet): https://www.startupdaily.net/topic/funding/y-combinator-backs-queensland-teenagers-mustering-startup-in-1-2-million-raise/ ; announced January 2026 (snippet). YC now lists it as Brumby: https://www.ycombinator.com/companies/grazemate . Aggregators show $500K and $1M; $1.2M is the most consistent.
- Problem, customer, how it works: moving cattle by helicopter, bike or horse. Drone flies to the paddock, positions around the herd and applies "pressure" like a stockman; RL models learn herd response. Tags: computer vision and reinforcement learning. Hardware details not public. https://www.ycombinator.com/launches/PKm-grazemate-drones-that-herd-cattle
- Traction signals: page reports none; a TechCrunch piece called it an investor favourite (https://techcrunch.com/2026/03/28/from-moon-hotels-to-cattle-herding-8-startups-investors-chased-at-yc-demo-day/). An aggregator claims 9,650 test missions in Queensland (snippet, unverified).
- Does India have this problem? India has 535.78 million livestock, 192.49 million cattle and 109.85 million buffalo in the 20th Livestock Census 2019 (snippet): https://www.gstimes.in/20th-livestock-census-india-has-535-78-million-livestock . First pastoral livestock census counted pastoralists for the first time since 1919 (snippet): https://www.downtoearth.org.in/agriculture/pastoral-census-after-105-years-india-will-count-its-transhumant-livestock-communities .
- Indian equivalents: no herding-drone company found. Adjacent: eVerse.AI CowGPT smart collar for dairy cows, used by "thousands" of farmers (snippet): https://www.businesstoday.in/latest/trends/story/can-an-ai-collar-predict-when-a-cow-will-fall-sick-heres-how-cowgpt-works-539200-2026-06-25 ; Drufarm collar; Verdant Impact vet telemedicine. Funding not checked.
- What differs in India: herds are 5-50 animals, not 2,000; grazing is on commons, forest and roadsides, not fenced paddocks; the pain is health, theft and straying, not mustering labour. A 2026 drone+GIS study in Kachchh counted cattle from aerial imagery (snippet): https://www.arccjournals.com/journal/asian-journal-of-dairy-and-food-research/DRF-538 .
- India version sketch: drop herding; build drone or phone-photo cattle counting and body-condition scoring for pastoral census, insurance or fodder-bank planning. Count animals in aerial images with a detection model.
- Overnight-demo potential: 3/5. Counting from public aerial imagery is easy; a flying demo is not.
- Overlap: none direct (livestock, not produce).

## Complir — "Vanta for physical products": AI agents map each product to each market's rules and generate labels, warnings and technical files (YC S26)
- Backers and round: Y Combinator Spring 2026; no amount stated on the page. Copenhagen, team 13. https://www.ycombinator.com/companies/complir ; batch also in TechCrunch 18 Jun 2026 list (URL above).
- Problem, customer, how it works: retailers with thousands of SKUs need per-country rules, translations, labels, risk assessments, declarations. Complir maps products to requirements, structures messy product data and generates the outputs, updating when rules change.
- Traction signals: Flying Tiger Copenhagen (1,000+ stores) over a year; 100k+ products under management; ~45% month-on-month growth, all company-stated (YC page).
- Does India have this problem? 769 products are under BIS quality-control orders, called a regulatory roadblock, and GTRI says QCO testing costs hurt MSMEs (snippet): https://swarajyamag.com/amp/story/economy/500-scientists-769-products-how-indias-quality-push-risks-becoming-a-regulatory-roadblock ; https://www.deccanchronicle.com/amp/business/high-qco-testing-costs-detrimental-to-msmes-1950185 . Customs demands for EPR certificates at Chennai port hit small importers hardest (snippet): https://www.thecore.in/business/when-every-clearance-chennaiport-a-customs-inside-indias-broken-import-system-845839 .
- Indian equivalents: none found for AI product-compliance across BIS/Legal Metrology/EPR; only consultancies (EPR certification services, snippets). Search did not look for Indian startups by name, so "none found" means none surfaced.
- What differs in India: rules are regulator-by-regulator (BIS, Legal Metrology packaging declaration, EPR plastics/batteries/e-waste, FSSAI labels); buyer is an importer, MSME exporter or e-commerce seller, price sensitivity is high; rules arrive as scanned gazette PDFs and notifications, sometimes in Hindi.
- India version sketch: take a product description or photo and output which BIS/QCO, Legal Metrology and EPR obligations apply, and draft the mandatory pack declaration. Corpus = BIS QCO list and Legal Metrology packaged-commodity rules.
- Overnight-demo potential: 4/5. RAG over a few regulation PDFs plus label generation is a clean demo.
- Overlap: none.

## Hemut — AI voice agents that make check calls and book loads for trucking back offices (YC X25)
- Backers and round: Y Combinator Spring 2025 (X25); profile reports $1.8M seed in 2025 at ~$30M valuation (snippet, secondary): https://yespress.io/hemut-yc-x25 (page returned 403 on fetch).
- Problem, customer, how it works: dispatch teams spend the day on phone calls to drivers and brokers. Voice agents handle inbound/outbound calls (check calls, load booking). Other YC players in the same space: Lanesurf (S25), Peer (S26), HappyRobot (S23, older) (snippet): https://yespress.io/hemut-yc-x25 .
- Traction signals: not stated in what I could read.
- Does India have this problem? ~75% of truck operators run fewer than 5 trucks (Redseer, snippet): https://redseer.com/articles/unlocking-growth-in-indias-fragmented-trucking-sector/ ; 1-2 lakh brokers sit between small owners and loads (Deccan Herald citing NITI Aayog-related reporting, snippet): https://deccanherald.com/business/indian-truckers-caught-on-a-pot-holed-road-to-growth-aspirations-1218737.html . Sources disagree on the empty-running percentage; NOT FOUND as a single hard number.
- Indian equivalents: TrucksUp ($8.2M, AI freight matching, snippet): https://www.trysignalbase.com/news/funding/trucksup-solutions-raises-8-2m-funding ; Vahak, BlackBuck, Fr8 exist (not checked this round). Indian voice-AI platforms: Bolna $6.3M seed General Catalyst (https://yourstory.com/ai-story/voice-ai-startup-bolna-raises-63m-led-by-general-catalyst), Ringg AI $10M Series A Peak XV (https://yourstory.com/2026/08/voice-ai-startup-ringg-ai-raises-10m-series-a-peak-xv-partners), Gnani.ai $10M. None trucking-specific found.
- What differs in India: calls are in Hindi, Punjabi, Tamil, Haryanvi, over poor networks; the "customer" is a transport-agent (commission agent) or a mid-size fleet, not a US dispatcher; payment is cash and part-advance; compliance documents are e-way bill and LR, not US DOT.
- India version sketch: Hindi/Hinglish voice agent that calls a driver, asks for location and ETA, transcribes the reply and writes it to a trip sheet; Bolna/Whisper plus a ledger. 
- Overnight-demo potential: 4/5. A voice agent with a Hinglish transcript to structured trip update is demoable live.
- Overlap: voice notes turned into structured insight (the voice-to-insight area). Overlap: factory-floor voice-to-insight (technique, not sector).

## Structured AI — AI quality control of construction drawing sets against building codes (YC F25)
- Backers and round: Y Combinator Fall 2025; $4.2M seed reported by ENR on 9 Jun 2026 per YC page: https://www.ycombinator.com/companies/structured-ai . Investors not stated on the page.
- Problem, customer, how it works: design firms lose time to drawing errors and cross-trade clashes. Agents learn a firm's standards, apply building codes, review PDF drawings and Revit models, flag errors with location and fix. Claims a vision model trained on thousands of engineering symbols and a 100-page set checked against 2,000 pages of code in minutes (company claim).
- Traction signals: 11 people, NYC; no customers named.
- Does India have this problem? Mumbai, Delhi, Telangana, Gurugram are all rolling out AI/auto-DCR plan scrutiny, and rejections come back as revision loops (snippet): https://www.freepressjournal.in/mumbai/bmc-launches-indias-first-ai-based-civittwin-system-for-faster-building-approvals , https://thepatriot.in/?p=85335 . A guide says "a rejected building plan is almost never the end" (snippet): https://www.studiomatrx.org/guides/why-building-plans-get-rejected-india . No independent rejection-rate number found.
- Indian equivalents: government portals (autoDCR, BuildNow Telangana, BMC CivitTwin); Tagbin Brixx text-to-3D design (https://yourstory.com/2026/08/tagbin-brixx-ai-building-design-bim-platform, snippet). No funded private pre-check startup surfaced. Contineu ($1.2M seed, quality/compliance monitoring, snippet: https://indianstartupnews.com/funding/bengaluru-based-deeptech-startup-contineu-raises-12-million-in-a-seed-round-9311806 ) is on-site, not drawings.
- What differs in India: no single code; NBC 2016 and Model Bye-Laws are templates and local bye-laws rule; plans are 2D DWG/PDF, rarely Revit; approval is discretionary; buyer is a 1-5 person architecture practice paying very little.
- India version sketch: upload a DWG/PDF plan; extract plot area, setbacks, FAR/FSI and height with a vision+geometry parser, check against one city's bye-laws and return a pre-scrutiny report before the architect files.
- Overnight-demo potential: 3/5. Parsing messy plans is hard; one city's rules on clean sample plans is feasible.
- Overlap: none.

## Avelis Health — ML and voice agents audit medical claims for self-insured employers and health plans (YC S25)
- Backers and round: Y Combinator Summer 2025; amount not stated. NYC, team of 3. https://www.ycombinator.com/companies/avelis-health
- Problem, customer, how it works: ML models read every claim for patterns, voice agents fetch medical records, LLM agents check what was billed, integration blocks improper payments and recovers overpayments. Claims 3-7% savings on claims spend (company-stated, unverified).
- Traction signals: none named.
- Does India have this problem? BCG with Medi Assist estimates Rs 8,000-10,000 crore a year lost to fraud, waste and abuse in health insurance, concentrated in claims of Rs 50,000 to Rs 2.5 lakh (snippet): https://www.bcg.com/publications/2025/india-rebuilding-trust-combating-fraud-waste-and-abuse-in-indias-health-insurance-ecosystem . Ayushman Bharat rejected 3.56 lakh fraudulent claims worth Rs 643 crore (snippet, dated Mar 2025): https://www.angelone.in/news/market-updates/ayushman-bharat-fraud-crackdown-govt-rejects-rs-643-crore-worth-of-bogus-claims . IRDAI Insurance Fraud Monitoring Framework, effective 1 Apr 2026 (snippet).
- Indian equivalents: no AI claim-audit startup surfaced in this search (Medi Assist is the TPA and co-author of the BCG report). "None found"; Plum ($20M Peak XV Series B, corporate insurance and AI claims ops; snippet): https://cdn.dealstreetasia.com/stories/plum-series-b-round-477147 is adjacent.
- What differs in India: buyers are insurers, TPAs and the NHA (public scheme), not self-insured employers; scanned handwritten discharge summaries; ICD-10 coding is inconsistent; standard treatment rates are still being negotiated (snippet, Outlook Business). Fraud pattern = upcoding, unnecessary admissions, same-patient duplicates.
- India version sketch: take a synthetic set of PM-JAY-style claims plus scanned discharge summaries, flag duplicates, procedure-diagnosis mismatches and length-of-stay outliers with a rule+LLM stack, output an audit queue.
- Overnight-demo potential: 4/5. Anomaly scoring plus document-vs-claim check on synthetic data.
- Overlap: none.

## CentralComs — AI receptionist and follow-up agent for HVAC, plumbing and electrical companies (YC S26)
- Backers and round: Y Combinator Spring 2026; amount not stated. SF, team of 2. https://www.ycombinator.com/companies/centralcoms
- Problem, customer, how it works: home-services firms miss calls after hours. Agents answer, qualify, book into ServiceTitan/Housecall Pro/Jobber, chase estimates and send reminders.
- Traction signals: none named; co-founder's earlier facility-management platform was used by NVIDIA, Cushman & Wakefield, NASA JPL (page).
- Does India have this problem? Home services is ~Rs 5.1 lakh crore (FY2025) with 90.5% unorganised and online penetration under 1% (snippet, Redseer-based): https://india.entrepreneur.com/?p=96423 and https://www.share.market/buzz/ipo-corner/urban-company-ipo-2025-complete-investor-guide/ . Urban Company's professional count varies 40,000-55,000 by source (snippet).
- Indian equivalents: Urban Company (listed 2025); voice-AI platforms Bolna, Ringg, Gnani (URLs above). No Indian AI receptionist for plumbers/electricians found.
- What differs in India: technicians use WhatsApp and a notebook, not ServiceTitan; calls in local languages; the customer pays cash and negotiates the visit price; the "software" to integrate with is WhatsApp Business and Google Business Profile.
- India version sketch: WhatsApp+voice agent that takes a missed call, asks the problem in Hindi, quotes a visit range from a price table and books a slot on a Google Sheet for a 5-technician firm.
- Overnight-demo potential: 4/5.
- Overlap: none.

## Vela Energy — AI agents for procurement, permitting and engineering studies on large-load energy projects (YC W26, a16z Speedrun)
- Backers and round: $1.3M pre-seed led by a16z Speedrun (snippet from yespress write-up; secondary source): https://yespress.io/vela-yc-w26 (page returned 403 on fetch). Primary announcement not seen.
- Problem, customer, how it works: data-centre and large-load developers lose months on interconnection, permits and studies. Agents prepare and track the paperwork. Details beyond the snippet not seen.
- Traction signals: not seen.
- Does India have this problem? ~50 GW of clean energy stranded by transmission bottlenecks (IEEFA via Down To Earth): https://www.downtoearth.org.in/energy/50-gw-of-clean-energy-stranded-as-transmission-bottlenecks-stall-indias-green-shift-ieefa ; one-third of newly commissioned RE capacity faces curtailment (ICRA via pv-magazine, 8 Jul 2026): https://www.pv-magazine.com/2026/07/08/one-third-of-indias-new-renewable-energy-capacity-faces-curtailment-due-to-grid-constraints/ . Right-of-way, forest and wildlife approvals are the main delay (snippet); IEEFA recommends a single-window clearance system.
- Indian equivalents: none found for AI permitting; WorkOnGrid (Rs 22.5 cr / $2.4M, Transition VC, utility data; snippet): https://www.pulse.bot/ai/deals/workongrid-raises-24m-in-funding-round-led-by-transition-vc-19a23211-18fc-44b6-9466-5eb075dc7767 ; Probus Smart Things ($5M, smart grid comms; snippet).
- What differs in India: land parcels and RoW clearances across state governments (not utility interconnection queues); forest/wildlife clearances; buyer is a developer or transmission SPV; documents include revenue records in regional languages.
- India version sketch: a tracker that reads a transmission line route (KML), overlays forest, wetland, village and railway layers from open data and lists the clearances each stretch needs, with a draft application checklist.
- Overnight-demo potential: 3/5. Geo-overlay is easy; the permitting knowledge base is the work.
- Overlap: none.

## Stilta — AI agents that search and analyse patents and scientific literature for IP lawyers (YC W26 Demo Day)
- Backers and round: Y Combinator (W26 Demo Day, TechCrunch 28 Mar 2026): https://techcrunch.com/2026/03/28/from-moon-hotels-to-cattle-herding-8-startups-investors-chased-at-yc-demo-day/ ; amount not seen.
- Problem, customer, how it works: prior-art search for patent lawyers; agents search and analyse patents and papers. No further detail opened.
- Traction signals: none opened.
- Does India have this problem? Indian Patent Office examinations fell from 23,295 (2023) to 14,705 (2024); 2023 filings hit a record 90,300; practitioner quotes pendency of 24-30 months (snippet, law-firm commentary): https://ssrana.in/articles/backlog-bottleneck-and-the-fast-lane-what-the-latest-patent-office-data-says-about-processing-times-in-india/ .
- Indian equivalents: none found for AI patent search (not searched by name).
- What differs in India: applicants are universities, MSMEs and individuals using agents on small fees; Hindi/regional prior art is thin, so the search set is mostly English patents; the Indian IPO fast-track for startups.
- India version sketch: upload an invention disclosure; return nearest prior art from Google Patents/Lens open data with claim-by-claim overlap and a novelty note, aimed at university tech-transfer offices.
- Overnight-demo potential: 4/5 (embedding search over a public patent subset).
- Overlap: none.

## Tivara — AI agents that handle phone calls and scheduling for healthcare admin (YC-backed seed)
- Backers and round: $3.6M seed with Y Combinator among backers (snippet from Business Insider via AOL): https://www.aol.com/news/read-pitch-deck-y-combinator-140001189.html . Date not seen.
- Problem, customer, how it works: front-desk call volume in US practices; voice/chat agents answer and schedule. Detail beyond snippet not seen.
- Traction signals: not seen.
- Does India have this problem? Small-clinic receptionist work is mostly manual; numeric evidence not found. Vendor pages quote lost-revenue figures that are unverified (https://curastax.pages.dev/, snippet).
- Indian equivalents: Pype AI ($1.2M pre-seed, Kalaari, hospitals; snippet): https://entrackr.com/snippets/pype-ai-raises-12-mn-in-pre-seed-round-led-by-kalaari-capital-10783582 ; Mykare.ai ($3.2M total; snippet): https://inc42.com/buzz/mykare-closes-round-at-3-2-mn-to-enhance-ai-capabilities/ ; Voiceoc (Rs 3 cr); CuraStax from Rs 999/month, CallMissed 22 languages (vendor pages).
- What differs in India: price (Rs 1,000-5,000 a month, not hundreds of dollars); WhatsApp is the default channel; ABDM/ABHA IDs; many clinics use no EMR.
- India version sketch: WhatsApp appointment bot with voice-note intake in Indian languages, ABHA lookup mock and a reminder cron.
- Overnight-demo potential: 4/5. Crowded in India, so differentiation matters more than build.
- Overlap: voice notes to structured insight (technique).

## Rudus — AI quantity takeoff and estimating for concrete contractors (YC 2026 construction/real-estate cohort)
- Backers and round: Y Combinator 2026; amount not seen. Listed in MarketScale's cohort roundup: https://www.marketscale.com/industries/engineering-and-construction/y-combinators-2026-construction-and-proptech-cohort-targets-the-industrys-costliest-operational-bottlenecks.md . Batch label not given there.
- Problem, customer, how it works: reads plans to produce takeoffs; claims 70% less estimation time. Same cohort: FlowManual (bidding/purchasing), Foreman (estimate to invoice), Helonic (clash and RFI drafts from plan PDFs), Nerviom (approvals for data centre/factory/energy projects, one-person company).
- Traction signals: none stated.
- Does India have this problem? Indian takeoff/BOQ tools are funded: MeltPlan $10M seed (Bessemer, Feb 2026, Melt Takeoff extracts quantities from 2D/3D plans, snippet): https://india.entrepreneur.com/news-and-trends/meltplan-raises-usd-10-mn-seed-round-led-by-bessemer/503018 ; Attentive.ai ~$12M Series A (Noida office, US customers; snippet): https://theprint.in/ani-press-releases/attentive-ai-completes-12m-series-a-round-to-expand-ai-offerings-for-the-construction-industry/2460091 . Hard Indian number on estimation time: NOT FOUND.
- Indian equivalents: MeltPlan and Attentive.ai (above); Track3D ($4.3M seed), Inkers, SitePace, Flo Mobility (site robots, $2.5M) are adjacent on monitoring (snippets).
- What differs in India: BOQ follows CPWD/state schedule-of-rates; drawings often hand-marked; contractor buyers are small and cash-based; steel/cement rates change weekly.
- India version sketch: upload a floor plan, detect walls/slabs/columns, compute quantities and price against a state schedule of rates to give a BOQ draft.
- Overnight-demo potential: 3/5.
- Overlap: none.

---

## Unlimited Industries — design-and-build company using AI to evaluate hundreds of thousands of design configurations for power, manufacturing and mineral plants (a16z)
- Backers and round: $12M seed co-led by a16z and CIV; published 3 Dec 2025: https://www.startuphub.ai/news/a16z-backs-unlimited-industries-funding-to-build-ai-construction
- Problem, customer, how it works: owns design and build in one company to remove handoffs. AI platform evaluates design configurations for cost, safety and performance. Reported results: one project's pre-construction engineering went from ~6 months to a few weeks; one design cut projected capex by more than half (company-reported).
- Traction signals: no customers named.
- Does India have this problem? India plans ~Rs 4.91 lakh crore ($60B) on transmission in 2027-32; Mazagon Dock won a Rs 117.99 crore AI-substation order from MSETCL (snippet): https://powerpeakdigest.com/mazagon-dock-msetcl-ai-grid-order/ . No hard number on Indian EPC design time.
- Indian equivalents: no generative-design EPC startup found; adjacent grid-tech: Kimbal ($22M Series B, GEF Capital; snippet https://inc42.com/buzz/kimbal-bags-22-mn-to-scale-smart-grid-solutions-globally/), WorkOnGrid, Probus (above).
- What differs in India: EPC contractors, not a design-build startup, own the job; design is by in-house CAD teams; BoQ pricing is tendered and low-margin; land and RoW, not design, set the schedule.
- India version sketch: layout optimiser for a solar-plant or small substation that tries thousands of equipment placements against a terrain and cost model and returns the cheapest compliant one.
- Overnight-demo potential: 3/5.
- Overlap: none.

## XBuild — AI estimating platform for specialty contractors, starting with roofing (a16z participated)
- Backers and round: $19M Series A led by N47 with Rackhouse Ventures and a16z participating, 20 Jan 2026: https://fintech.global/2026/01/22/xbuild-raises-19m-to-scale-ai-estimating-platform/ (snippet via search; a16z did not lead). Some sources wrongly list a16z as lead.
- Problem, customer, how it works: contractors hand-estimate from plans and aerial data; XBuild produces estimates, expanding to concrete, HVAC, plumbing, glazing.
- Traction signals: 15,000+ projects, $250M+ in construction value processed (company-reported, snippet).
- Does India have this problem? See Rudus entry (MeltPlan, Attentive.ai already funded). Roofing-specific Indian number: NOT SEARCHED.
- Indian equivalents: MeltPlan, Attentive.ai (above).
- What differs in India: roofs are RCC slabs, tin sheds or tiled; satellite imagery for roof measurement is usable but roof pitch/material varies; contractors quote by square foot verbally.
- India version sketch: measure a roof or terrace from satellite/drone imagery and give a waterproofing or solar-install quantity quote.
- Overnight-demo potential: 4/5 (segment roofs from imagery, compute area, quote).
- Overlap: none.

## FurtherAI — AI workspace for insurance underwriting, claims and compliance (a16z)
- Backers and round: $25M Series A led by a16z, 7 Oct 2025, total funding $30M: https://www.startuphub.ai/news/furtherai-series-a-a16z-bets-25m-on-ai-for-insurance ; also https://a16z.com/announcement/investing-in-furtherai/ (from search listing).
- Problem, customer, how it works: carriers, MGAs and brokers process submissions and policy comparisons by hand; FurtherAI runs insurance-specific workflows integrated with carrier and broker systems. Clients named: Accelerant, MSI, Leavitt Group. Reported 15% better submission-to-quote ratio and proposals 10x faster (company-reported).
- Traction signals: as above; "billions in premiums".
- Does India have this problem? Bengaluru's Pibit.AI sells underwriting automation, mostly to US clients: $7M Series A, Stellaris, YC and Arali participating, Nov 2025 (snippet): https://india.entrepreneur.com/news-and-trends/pibitai-raises-7-mn-from-stellaris-venture-partners-and/499890 . Health-claims leakage number in the Avelis entry.
- Indian equivalents: Pibit.AI (above); BimaKavach (MSME commercial insurance, Beyond Capital, undisclosed, Jul 2026; snippet: https://pulse2.com/beyond-capital-ventures-invests-in-bimakavach-to-advance-ai-native-commercial-insurance-in-india/); Plum ($20M Peak XV Series B). FurtherAI also reported a $5M seed led by Nexus (snippet).
- What differs in India: PDFs, scanned proposal forms, emails and WhatsApp; Hindi names; broker-led distribution; IRDAI rules.
- India version sketch: extract fields from a messy commercial insurance proposal (fire, marine, motor fleet) and compare two quotes side by side.
- Overnight-demo potential: 4/5.
- Overlap: none.

## Lassie — AI to run doctors' offices, starting with dental insurance payment posting (a16z)
- Backers and round: $35M Series A led by a16z, post dated 26 Jun 2026: https://www.homebrew.co/blog-posts/lassie-raises-usd35-million-series-a-to-save-doctors-the-busy-work
- Problem, customer, how it works: small practices lose time to back-office work; first agent posts insurance payments. Technology detail not given.
- Traction signals: 700+ practices in 49 states; cofounders personally onboarded the first 100 offices.
- Does India have this problem? Overlaps with Tivara entry. Hard Indian number on clinic admin burden: NOT FOUND. Indian clinics' tooling is price-bound: CuraStax lists from Rs 999/month (vendor page, snippet).
- Indian equivalents: Pype AI, Mykare.ai, Voiceoc (see Tivara entry).
- What differs in India: most payments are cash or UPI, not insurer remittances; the admin pain is billing, stock and follow-ups; insurance (TPA) reconciliation matters in hospitals, not solo clinics.
- India version sketch: UPI+cash reconciliation, bill generation and recall messages for a dental clinic from a WhatsApp chat.
- Overnight-demo potential: 3/5.
- Overlap: none.

## Sphere — AI tax-rules engine that handles registration, calculation and filing across borders (a16z)
- Backers and round: $21M Series A led by a16z with YC and Felicis, 18 Nov 2025: https://techcrunch.com/2025/11/18/a16z-leads-21m-series-a-into-tax-compliance-platform-sphere
- Problem, customer, how it works: AI engine "TRAM" codifies tax rules per jurisdiction and decides taxability with citations; human reviewers approve before a non-AI tax engine applies tax. Connects to 100+ tax authorities; setup under 24 hours. Customers named: Lovable, Replit, ElevenLabs (global SaaS firms).
- Traction signals: no revenue figure.
- Does India have this problem? GST/TDS compliance is the Indian analogue. Number of GST taxpayers: NOT FOUND in my search (snippet only returned vendors).
- Indian equivalents: ClearTax; Mysa ($3.4M pre-Series A, Blume and Piper Serica, AP automation; snippet https://india.entrepreneur.com/?p=92984); GSTHero, IndiaFilings (older Rs 32 cr pre-Series A, 2022).
- What differs in India: one national GST rate schedule but frequent notifications, HSN/SAC code ambiguity, e-invoicing; buyer is an MSME paying a CA Rs 1,000-3,000 a month.
- India version sketch: a GST classifier that reads an invoice or product description, suggests HSN code and rate with the notification cited, and flags ITC mismatches.
- Overnight-demo potential: 4/5.
- Overlap: none.

## Eka Robotics — vision-based robot manipulation for factory floors (a16z, F-Prime)
- Backers and round: $150M Series A led by a16z and F-Prime (snippet only; page returned 403): https://aimagazine.com/news/what-is-eka-robotics-how-it-raised-us-150m-in-series-a . Date not seen.
- Problem, customer, how it works: factory-floor manipulation using a vision-based model. Detail not seen. Treat all facts as snippet.
- Traction signals: not seen.
- Does India have this problem? Indian robotics funding was $42.1M in H1 2026 per Tracxn (snippet): https://voice.lapaas.com/indian-robotics-startups-raise-42-1-million-in-h1-2026/ . Hard number on MSME automation: NOT FOUND.
- Indian equivalents: Mowito ($3M pre-seed, Version One Ventures, 7 Jul 2026, foundation models so robot arms learn from demonstration; snippet https://ecorpit.com/physical-ai-robot-arm-models-india-manufacturing-2026/), CynLr ($10M Series A, Jan 2025; https://www.robotics247.com/article/cynlr_indian_deep_tech_robotics_startup_raises_10m_series_a_funding), ANSCER Robotics ($5.4M Series A, IAN Alpha; https://yourstory.com/2026/05/anscer-robotics-series-a-funding-round-led-by-ian-alpha-fund), Integra Robotics ($1.12M).
- What differs in India: labour is cheap, so ROI needs sub-Rs 5 lakh arms and 18-month payback; parts are non-standard; buyers are auto-component and electronics MSMEs.
- India version sketch: pick-and-place on a Rs 30,000 desktop arm using a camera and an open VLA/imitation model; sell as retrofit for sorting.
- Overnight-demo potential: 3/5 if an arm is in the kit; 1/5 otherwise.
- Overlap: CCTV vision AI for factories (shared factory-vision theme, not the same product).

## Westmag — US-made motors and actuators ("muscle of physical AI") for defence, drones and robotics (a16z)
- Backers and round: seed led by a16z, 2 Jun 2026: https://a16z.com/announcement/investing-in-westmag/ . Amount not stated on the page.
- Problem, customer, how it works: customers depend on Chinese motors; Westmag runs a semi-automated line in South San Francisco, shipping qualified defence motors and robotics actuators. Technical detail minimal.
- Traction signals: shipping from the factory (page).
- Does India have this problem? India imported ~93% of its rare-earth magnets from China in FY24-25 (snippet): https://www.magzter.com/nl/stories/news/India-Today/THE-GROWTH-MAGNETS ; India approved a Rs 7,280 crore scheme in Nov 2025 for magnet production (snippet): https://www.kotakneo.com/investing-guide/articles/india-rare-earth-magnet-investment-china-monopoly/ ; imports fell 56% to 16,281 tonnes in Apr-Sep FY2026 (Mint, snippet): https://www.magzter.com/nl/stories/newspaper/Mint-Mumbai/MAGNET-IMPORTS-SLIDE-AS-AUTO-COS-EYE-SHIFT-AWAY-FROM-CHINA .
- Indian equivalents: no drone/robot motor startup found in search; Enerzolve (power electronics, snippet https://yourstory.com/2026/07/enerzolve-power-electronics-india-grid).
- What differs in India: policy subsidy (PLI-style) is the driver; demand from drone makers under the defence push; rare-earth supply is the blocker, not know-how.
- India version sketch: BLDC motor designer that, from a torque/RPM spec, selects a magnet-light topology (ferrite or reluctance) and outputs a winding design with a simulation.
- Overnight-demo potential: 2/5 (3D-printed winding jig and a test stand are possible, a real motor is not).
- Overlap: none.

## PrismaX — teleoperation data platform that pays remote operators to drive robots and produce training data (a16z CSX)
- Backers and round: $11M round led by a16z CSX, June 2025 (snippet): https://www.therobotreport.com/prismax-launches-with-11m-to-scale-virtual-datasets-for-robotics-foundation-models/ ; https://roboticsandautomationnews.com/2025/06/17/prismax-raises-11-million-as-it-emerges-from-development/92205 . Not a plain seed round.
- Problem, customer, how it works / traction: only the search snippet seen: teleoperation data portal for robotics foundation models.
- Does India have this problem? India version = cheap remote operators for data collection. India check: NOT SEARCHED.
- Indian equivalents: not searched.
- What differs in India: labour price is the edge; bandwidth and latency to a robot overseas.
- India version sketch: a small teleop rig (phone camera plus servo arm) producing labelled grasp demonstrations.
- Overnight-demo potential: 2/5.
- Overlap: none.

---

## Logged in one line
- Developer tools and agent infra (skipped): Arga Labs, Sazabi, Superset, Lightsprint, Tasklet, Ploy (YC S26) — https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/ ; Byteport (networking), Luel (training-data marketplace), Pax Historia (game), Hex Security — TechCrunch 28 Mar 2026 (URL above).
- Security: Silmaril (prompt-injection defence, S26).
- Defence/space: 9 Mothers (counter-drone robots), Dispatch (reusable return spacecraft), Beyond Reach Labs (unfolding solar arrays), GRU Space (lunar hotel), Salem Robotics (nuclear inspection, S26; runtimewire).
- Healthcare (not opened): Claim Health ($4.4M seed, Maverick; https://pulse2.com/claim-health-4-4-million-seed-funding/), Prana (W26), Plena Health (S26), LunaBill (F25), Locata (S25) — snippets from YC directory searches.
- Logistics (not opened): Lanesurf (S25), Peer (S26), Alchemize (customs, YC P2026), Fleetline; FleetWorks $17M AI dispatcher (YC status unconfirmed): https://techcrunch.com/2025/10/14/fleetworks-raises-17m-to-match-truckers-with-cargo-faster .
- Construction/proptech (YC 2026, from MarketScale): FlowManual, Foreman, Helonic, Nerviom, CentralComs (done above), Wayline, AquaShield, Travo, RealPact. Opusense AI (inspection documentation), InspectMind AI (W24, outside date window).
- a16z, others: Agave (construction API, a16z led seed, Jul 2026; snippet, page 404), Endra ($50M Series A led by a16z, Jun 2026; Swedish construction tech; fetch failed), Dream (AI architect of record, $17M seed, 29 Oct 2026; 403), Ciridae ($20M seed, Accel and a16z, 18 May 2026; product not described: https://runtimewire.com/article/ciridae-20m-seed-accel-a16z-physical-economy-ai), Adaptive (TechCrunch, $6.5M seed), Nexxa.ai ($9M seed, Construct Capital; a16z speedrun participated), Base Power ($200M Series B, Apr 2025, a16z: https://techcrunch.com/2025/04/09/a16z-backs-base-power-in-200m-round-for-home-backup-batteries), Heron Power, Chariot Defense, Ulysses.
- a16z, bio and non-industrial: Genesis Therapeutics ($200M Series B), Phylo (seed Feb 2026), Stipple Bio ($100M Series A Apr 2026); Horowitz Andreessen Academy ($42M school, 22 Sep 2026: https://runtimewire.com/article/gagan-biyani-horowitz-andreessen-academy-42m), Oboe ($16M Series A, a16z, Dec 2025), Straia (Speedrun pre-seed); Poseidon AI ($15M, a16z crypto), XDOF ($70M), Syncere ($11M a16z Speedrun, home robotics).

## NOT SEARCHED
- Indian equivalents by company name for Stilta, Westmag-type motors, Unlimited Industries (EPC design); India hard numbers for Automax (valuation turnaround), Rudus/XBuild (estimation time), Tivara/Lassie (clinic admin burden), Sphere (GST taxpayer count), Eka (MSME automation).
- India check for PrismaX (teleop labour).
- India checks for YC RFS items other than city-hall plan scrutiny and the magnet scheme.
- Primary a16z/Speedrun announcements for Vela Energy; funding amounts for most YC S26 and F25 entries (YC pages do not state them).
- Pages that returned 403/404/closed socket: yespress.io Hemut and Vela, aimagazine Eka, fourweekmba Dream, a16z Agave, pulse.bot Endra, ycombinator.com/companies Hemut.

Searches used: 41
