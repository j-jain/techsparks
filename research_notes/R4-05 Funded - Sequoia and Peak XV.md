# R4-05 Funded - Sequoia and Peak XV  (agent: Sonnet, date 2026-11-12)

Notes on method. Funding facts below come from pages I opened (WebFetch) unless marked "(snippet)". Sequoia article pages show a bogus "Nov 11, 2026" metadata date; I used the date in the article body and say so where they conflict. Sequoia/Peak XV "India check" lines rely mostly on search-result snippets, so every India number is marked (snippet) unless I opened the page. Entries 1-10 are Sequoia Capital; entries 11-20 are Peak XV / Surge.

---

## 1. Pace — AI agents that do insurance back-office work (underwriting, claims, policy admin) from a client's own procedures
- Backers and round: Sequoia Capital led, $10M Series A, 27 Jan 2026 (Bryan Schreier, partner) — https://fortune.com/2026/01/27/exclusive-pace-raises-10-million-sequoia-enterprise-ai-collides-with-insurance/ ; Sequoia's own post, Series A led by Sequoia, amount not stated there — https://sequoiacap.com/article/partnering-with-pace-making-work-weightless
- Problem, customer, tech: Insurers and insurance BPOs spend on manual document-heavy work. Pace's agents read a company's SOPs, reason over long documents, work across back-office systems, and a human reviews a cited summary and confirms. Sequoia describes it as "end-to-end agent operating procedures, powered by reinforcement learning", with audit trail and guardrails. No hardware.
- Traction signals: Customers named by Fortune: Prudential, The Mutual Group, Newfront. Sequoia says "tens of thousands of tasks" a month. No revenue disclosed. Fortune cites insurance BPO at about $70B a year of spend (about $400B with wider financial services operations).
- Does India have this problem? 1,37,361 general+health insurance grievances in FY25, up 41% from 97,503; about 69% claim-related (snippet) — https://www.outlookmoney.com/amp/story/personal-finance/health-insurance-complaints-jump-41-per-cent-69-per-cent-involve-claims-failures-reveals-1-finance-study . IRDAI FY25: 3.26 crore health claims, 87% settled, 8% repudiated (snippet, same search; secondary press) — https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx
- Indian equivalents: Plum (corporate/employee health insurance, Rs 193 crore (~$20.6M) Series B led by Peak XV, date not in snippet, plans AI claims ops) — https://cdn.dealstreetasia.com/stories/plum-series-b-round-477147 (snippet). No Indian agent-for-insurer-back-office startup found in my one insurance search; NOT SEARCHED specifically for TPA (third-party administrator) automation.
- What differs in India: IRDAI now requires insurers to cite the specific policy clause in a rejection (snippet, outlookmoney link above), so a document-to-clause explainer has a regulatory hook. Buyers are TPAs and hospital billing desks as well as insurers; claim documents are scanned, handwritten, mixed English/Hindi. Pricing per claim in rupees, not per seat in dollars.
- India version sketch: Take 20-30 public sample discharge summaries and policy wordings, build an agent that extracts diagnosis, procedure and amounts and checks them against a policy clause list, output a cited approve/query/reject recommendation for a human. Demo = upload a claim PDF, get the clause-cited reasoning.
- Overnight-demo potential: 4. Document extraction plus clause retrieval is doable in a night; the missing piece is realistic claim documents (synthetic ones are fine for a demo).
- Overlap: none.

## 2. Mecka — human-demonstration data and robot deployment for physical AI
- Backers and round: Sequoia Capital led, $60M Series B, 8 Oct 2026 (NVIDIA, M12, Microsoft's fund, Qualcomm Ventures, Samsung joined) — https://pulse2.com/mecka-raises-60-million-series-b-led-by-sequoia-capital/ ; Sequoia post (7 Oct 2026 per search listing) — https://sequoiacap.com/article/partnering-with-mecka
- Problem, customer, tech: Robot models need real-world demonstrations. Mecka builds its own multi-sensor capture hardware, runs capture fleets recording people doing tasks in homes and workplaces, uses vision/multimodal models to turn raw sensor data into structured datasets, and also deploys robots for enterprises that have no robotics team.
- Traction signals: Customers are frontier robotics labs and "Magnificent Seven" companies; over $100M run-rate in June 2026, about $300M projected by end 2026 (company claim in the release).
- Does India have this problem? Not the same problem: India is already a collection hub. Inc42 reports finished egocentric datasets sell for $15-50 per hour and demand could reach 200,000-300,000 hours; workers can earn about $2 an hour (snippet) — https://inc42.com/features/india-trains-the-worlds-robots-but-at-what-cost/ . MeitY is reported to be examining consent practices (snippet, Remio analysis) — https://www.remio.ai/post/india-humanoid-robot-training-pays-workers-now-while-automating-their-skills
- Indian equivalents: Human Archive — $8.2M raised, backers include Wing VC, NVP Capital, Y Combinator, 1,000+ headsets on Indian gig workers — https://pulse2.com/human-archive-8-2-million-raised-to-build-training-data-infrastructure-for-physical-ai/ (snippet); Objectways (data services) — Inc42 link above (snippet). Alive as of 2026 per those pages.
- What differs in India: labour is cheap, so the value is in data collection at scale, not in robots; consent, privacy and worker-pay disputes are live (Urban Company and Pronto reportedly declined partnerships, snippet). Tasks differ (Indian kitchens, kirana, small workshops), which is the data Western labs lack.
- India version sketch: Not a data-broker clone. A student version is a consent-first capture rig (head-mounted camera plus IMU on a microcontroller) and a labelling pipeline that segments an Indian kitchen or workshop task into steps; the sellable idea is task diversity and fair pay, not volume.
- Overnight-demo potential: 3. Capture rig plus automatic step segmentation is demoable; no one can show a trained robot in 18 hours.
- Overlap: loose, with factory-floor worker data capture (voice) and CCTV vision on factory floors.

## 3. Bunkerhill Health — AI agents that hospitals build themselves (Carebricks)
- Backers and round: Sequoia backed at seed and "doubling down" with a new round; amount and round type not disclosed; post dated 16 Jul 2026 in body (Alfred Lin) — https://sequoiacap.com/article/partnering-with-bunkerhill-health-ai-agents-that-improve-patient-outcomes
- Problem, customer, tech: Health systems have many clinical and admin tasks no vendor covers. Carebricks lets a hospital turn a use-case idea into an agent that runs in the background and surfaces missed findings (earlier product moved imaging models from research to bedside with FDA clearance).
- Traction signals: UTMB Health went from one agent in production to more than twenty and consolidated several vendors' point tools. Only customer named.
- Does India have this problem? Radiology/clinical backlog is real but I did NOT find a clean Indian radiologist-shortage number in my search. Indian health-AI activity is visible: CARPL.ai $10M Series A led by IFC, late Jul 2026 (snippet) — https://www.healthcareittoday.com/2026/07/27/carpl-ai-raises-10m-led-by-ifc-pearl-health-raises-110-million/
- Indian equivalents: CARPL.ai (marketplace of 300+ radiology AI apps from 100+ partners through one integration) — same link; 5C Network (reads 15,000+ scans a day for 2,000+ facilities, company claim) — https://www.5cnetwork.com/resources/best-radiology-ai-companies-india (snippet); Prodoc AI (seed, Dr A. Velumani Family Office; "intelligence layer" for hospitals; 100+ hospitals, company claim) — https://biospectrumindia.com/news/104/28575/prodoc-ai-secures-seed-funding-to-develop-intelligence-layer-for-indian-hospitals.html (snippet). Qure.ai: no 2025-26 funding found.
- What differs in India: hospitals are mostly small and paper-based (a 2025 commentary says small and medium hospitals still run on paper, snippet) — https://newsreel.asia/articles/india-healthcare-small-medium-hospitals-digitalisation ; ABDM integration, WhatsApp as the interface, rupee price points, and doctors who do not want a new dashboard.
- India version sketch: A no-code "agent builder" for one small nursing home: pick three use cases (discharge-summary draft, missed follow-up flag, lab-value alert), wire to a spreadsheet standing in for the HIS. The gap is the small-hospital layer under CARPL/Prodoc.
- Overnight-demo potential: 3. Agent plus a fake hospital dataset is easy; credibility needs real clinicians.
- Overlap: none.

## 4. Freed — AI scribe for clinicians in small practices
- Backers and round: Sequoia led Series A, amount not disclosed, 5 Mar 2025 per article body — https://sequoiacap.com/article/partnering-with-freed-an-ai-powered-clinicians-assistant
- Problem, customer, tech: Doctors lose hours to documentation. Freed transcribes the visit audio, drafts the note in the clinician's own phrasing and templates, and files it into the EHR; product-led growth.
- Traction signals: 17,000+ providers, small and medium independent practices, nearly 100 specialties.
- Does India have this problem? Indian doctors see far more patients per day; one commentary quotes an average of 30 patients versus 3 for a US doctor (weak source, personal blog) — https://gulzar05.blogspot.com/2026/03/some-thoughts-on-startup-innovation.html . Hard official number NOT FOUND in this search.
- Indian equivalents: Eka Care (total funding $19.5M, last round Series A July 2022; Parrotlet clinical speech model; NVIDIA partnership for an offline multilingual scribe; scribe used by 3,000+ doctors) — https://www.digitalhealthnews.com/eka-care-nvidia-partner-to-develop-offline-multilingual-ai-medical-scribe-for-india and https://yourstory.com/2025/11/healthtech-startup-eka-care-ai-standardise-medical-records-doctor-patient (snippets); FosterHealth.ai; ZenMD (launched May 2026, ZenScribe); Docstribe (ABGD Ventures) — all snippet, no amounts.
- What differs in India: code-mixed Hindi-English-regional speech in noisy OPDs with 2-3 minute consults; most notes are short prescriptions, not long US-style notes; no EHR to integrate with, so the output is a printed/WhatsApp prescription; price in the low hundreds of rupees a month.
- India version sketch: Gap left open is clinic-noise robustness and the "prescription pad" output for solo GPs, plus Tier-2 languages (Marathi, Tamil, Bengali). Demo: record a staged Hinglish consult on a phone, get prescription plus advice in the patient's language.
- Overnight-demo potential: 4. Whisper-class ASR plus an LLM structuring step is a night's work; the test is word error rate on Hinglish medical terms.
- Overlap: none.

## 5. Avelios — hospital information system built from scratch (Munich)
- Backers and round: Sequoia led Series A, amount not disclosed, 6 Feb 2025 per article body (previously only pre-seed) — https://sequoiacap.com/article/partnering-with-avelios-healthcare-for-the-modern-age
- Problem, customer, tech: Legacy HIS software; a major incumbent plans to sunset its product in 2027, forcing replacement at 1,000+ hospitals in Germany. Modular system: clinical documentation, administration/billing, patient portal, AI modules.
- Traction signals: has won several of Germany's largest public and private hospitals; no revenue given.
- Does India have this problem? Small hospitals digitising: the Centre launched C-DAC's cloud e-Sushrut HMIS for small clinics around 30 Jun 2026 (snippet) — https://medicaldialogues.in/news/health/hospital-diagnostics/centre-launches-cloud-based-hmis-for-small-healthcare-facilities-173885 . No count of small hospitals found.
- Indian equivalents: Prodoc AI (above); Surgy Health (SurgyOne AI HIS/EHR for 500-1,500-bed groups in India/Gulf) — https://www.digitalhealthnews.com/bengaluru-based-surgy-health-launches-ai-enabled-his-for-india-gcc-markets ; DocPlix (Rs 1.2 crore bridge, ABDM EHR) — https://cxodigitalpulse.com/?p=17963 ; Larkai Healthcare (AI+IoT devices for small-town hospitals) — https://yourstory.com/2025/11/larkai-healthcare-startup-ai-iot-hospital-care-to-indias-small-towns (all snippet).
- What differs in India: free government HMIS now exists, so a paid product needs a reason; the buyer is the owner-doctor, price sensitivity is extreme, billing is TPA/cash-heavy, ABDM compliance is the entry ticket.
- India version sketch: Gap left open is the 20-50 bed nursing home (Surgy targets large groups, e-Sushrut targets clinics). Tiny HIS: OPD, bed board, billing, TPA paperwork, with AI only for discharge summary and billing codes.
- Overnight-demo potential: 2. A whole HIS is too large; only the AI discharge-summary slice is demoable.
- Overlap: none.

## 6. Sunflower Labs — autonomous drone that patrols a site when a sensor trips
- Backers and round: Sequoia partnered; round type and amount not disclosed; post dated 4 Nov 2025 in body — https://sequoiacap.com/article/partnering-with-sunflower-labs-your-autonomous-eye-in-the-sky
- Problem, customer, tech: Security patrols at data centres, stadiums, warehouses, communities. Motion sensors on the ground trigger a drone from a base station within about 5 seconds; it flies to the spot, streams video, detects people, vehicles, water leaks, fires; integrates with existing security platforms; recent FAA approval for 99% of the US.
- Traction signals: Sequoia claims a 10x cost advantage over patrols; customers named: a Swiss railway, a Los Angeles community, a self-storage company. No numbers.
- Does India have this problem? NOT FOUND as a hard number in my one drone search; India has no comparable rule that allows autonomous beyond-visual-line flight yet (not searched; do not assume).
- Indian equivalents: SUIND (Rs 20.5 crore seed led by Transition VC, WASP surveillance platform in development; alive) — https://india.entrepreneur.com/business-news/suind-raises-inr-20-5-cr-in-seed-round-led-by-transition-vc (snippet); Marut Drones ($6.2M Series A from Lok Capital, Nov 2024, DGCA-certified Skyswift 56 surveillance drone) — https://dronelife.com/2024/11/06/marut-drones-secures-6-2-million-in-series-a-funding-amid-indias-push-for-domestic-drone-manufacturing/ (snippet); Vayudh ($10M, defence ISR) — https://inc42.com/buzz/dronetech-startup-vayudh-bags-10-mn-from-dharana-capital-others (snippet). No drone-in-a-box commercial site-patrol startup found.
- What differs in India: DGCA permissions per flight zone, security-guard labour is cheap (the 10x cost claim does not hold), buyers are solar plants, warehouses, mines, gated townships, and the use case is as much theft/animal intrusion as people.
- India version sketch: Skip the drone. The portable core is "trigger sensor -> camera -> classifier -> WhatsApp alert" for a solar plant or godown perimeter, which is a fixed pole-camera plus PIR/ultrasonic build; drone is phase 2.
- Overnight-demo potential: 4 for the sensor+camera+classifier alert; 1 for any drone.
- Overlap: loose, with CCTV vision AI (site rather than factory).

## 7. WithCoverage — AI-assisted commercial insurance broker for businesses
- Backers and round: Sequoia Capital and Khosla Ventures co-led, $42M Series B, 14 Jan 2026 — https://pulse2.com/withcoverage-42-million-series-b-closed-to-build-ai-powered-risk-management-team
- Problem, customer, tech: Businesses buy commercial insurance through slow, opaque brokers. WithCoverage shops policies across carriers, flags coverage gaps and handles switching paperwork with an "AI-enabled Risk Management Team" (AI plus specialists).
- Traction signals: 700+ businesses switched in about 18 months; customers named: GoPuff, Eight Sleep, Blank Street.
- Does India have this problem? India has 63 million+ MSMEs (about 30% of GDP) and fewer than 5% carry adequate commercial insurance (snippet; secondary source, also another source says about 1% insured, so the range is wide) — https://pulse2.com/beyond-capital-ventures-invests-in-bimakavach-to-advance-ai-native-commercial-insurance-in-india/
- Indian equivalents: BimaKavach (Indore, SME insurance; Beyond Capital Ventures investment July 2026, amount undisclosed) — same link; Covrzy (IRDAI broking licence; Rs 3.2 crore / $400K pre-seed led by Antler) — https://indianstartupnews.com/news/insurtech-startup-covrzy-receives-irdai-general-insurance-broking-license-6695924 ; Plum (see entry 1); Onsurity ($24M Series B led by IFC, older) — https://techcrunch.com/?p=2611402 (all snippet).
- What differs in India: the SME buyer buys a policy only when a bank, landlord or client demands it; premiums are tiny; distribution is through agents and bank loans; IRDAI broker licence required.
- India version sketch: Gap left open is the shop/small-factory fire-and-theft policy. Photo of the premises -> risk checklist (wiring, stock, exits) -> quote comparison. Demo = vision model reading a shop photo and listing coverage gaps.
- Overnight-demo potential: 3. The photo-to-risk-checklist part is easy; real quotes are not.
- Overlap: none.

## 8. Sandstone — AI for in-house legal teams
- Backers and round: Sequoia led, $10M, public launch week of 13 Jan 2026; round type not stated — https://news.bgov.com/legal-ops-and-tech/sequoia-leads-backing-of-ai-legal-technology-startup-sandstone (paywalled, truncated)
- Problem, customer, tech: Pulls data from HR, sales and other functions so in-house lawyers can track company goals and work more efficiently. Customers and traction not visible in the page I could read.
- Does India have this problem? 5 crore+ pending court cases (secondary, vendor-authored) — https://blogs.ecourtsindia.com/2026/04/16/top-legaltech-startups-in-india-2026-whos-building-the-future-of-law/ (snippet). In-house legal teams are not the Indian pain; courts are.
- Indian equivalents: Adalat AI (nonprofit, YC Fall 2026 batch, speech-to-text for court records; one source says 6,000+ judges in 11 states) — https://www.barandbench.com/news/law-policy/legal-tech-nonprofit-adalat-ai-joins-y-combinator and https://analyticsindiamag.com/ai-features/yc-backs-indias-legal-tech-nonprofit-adalat-ai-as-it-takes-courtroom-ai-global ; Jhana ($1.6M seed, Together Fund, 2024 or late 2023, sources differ) — https://entrackr.com/2024/09/ai-paralegal-startup-jhana-raises-1-6-mn-in-seed-round (all snippet).
- What differs in India: the real buyer is the court system and litigants; documents are scanned, multilingual, with vernacular judgments; budgets are government or philanthropic.
- India version sketch: Gap left open is the litigant and small-business owner, not lawyers: upload a notice or order in Hindi/regional language, get a plain-language summary, deadline and next-step list.
- Overnight-demo potential: 4. OCR plus summarisation plus deadline extraction on real court orders (public on eCourts) is demoable.
- Overlap: none.

## 9. Rillet — AI-native accounting system (general ledger / ERP)
- Backers and round: Sequoia led $25M Series A, announced 28 May 2025 (TechCrunch headline date) — https://techcrunch.com/2025/05/28/rillet-raises-25m-from-sequoia-to-automate-general-ledger-systems-using-ai ; $100M Series C at $1B valuation led by ICONIQ with Sequoia participating, Aug 2026 (600+ customers) — https://pulse2.com/rillet-raises-100-million-series-c-at-1-billion-valuation-as-ai-native-erp-tops-600-customers/ (snippet only for the Series C)
- Problem, customer, tech: Mid-market finance teams on legacy ledgers. AI agents do accruals, reconciliation and board reporting.
- Does India have this problem? Hard number NOT FOUND in my search. Indian vendor content says GST reconciliation (GSTR-2B) and TDS are what global tools miss (Tally's own guidance, snippet) — https://tallysolutions.com/ai-for-business/top-5-uses-of-ai-in-accounting-for-growing-businesses/
- Indian equivalents: Febi.ai (about Rs 16.8 crore / $2M pre-Series A, date unconfirmed) — https://thefinancestory.com/ai-powered-bookkeeping-tax-compliance-platform-febi-ai-raised-%e2%82%b916-8-crores ; Hisabkitab (Surat, undisclosed seed, July 2026, figures conflict) — https://app.dealroom.co/companies/hisabkitab ; Karbon Business AiAccountant (AI plus licensed CAs); Suvidha AI (GST reconciliation, Tally sync) — https://yourstory.com/companies/suvidha-ai (all snippet; no verified funding for most).
- What differs in India: the system of record is Tally, not a cloud ERP, and the user is a chartered accountant serving many small clients; GST portal data (GSTR-2B) is the ground truth to reconcile against; price is a few thousand rupees a year.
- India version sketch: Gap left open: a reconciliation agent that matches purchase bills (photos, PDFs, WhatsApp) to GSTR-2B and flags ITC mismatches, exporting back to Tally XML.
- Overnight-demo potential: 4. Invoice OCR plus fuzzy match against a sample GSTR-2B file is demoable with synthetic data.
- Overlap: none.

## 10. Form Energy — iron-air batteries for multi-day grid storage
- Backers and round: Sequoia invested $100M (upsized from a proposed $50M) in a round after Form closed a Series G; Sequoia post dated 1 Sep 2026 in body — https://sequoiacap.com/article/partnering-with-form-energy
- Problem, customer, tech: Lithium-ion stores grid energy for 4-6 hours; iron-air (iron plus air) aims to compete with gas peaker plants on cost for multi-day storage. Factory on a former steel mill site in West Virginia (400+ jobs) and a large hyperscale order. Not an AI company; included as deep tech with an energy-utility buyer.
- Does India have this problem? CEA target 60.63 GW of storage by 2029-30 (41.65 GW battery, 18.98 GW pumped hydro); commissioned about 10.3 GW as of June 2026; no statutory definition or funding mechanism yet for 8h+ storage, VGF framework proposed for FY2028 (snippets) — https://solarquarter.com/2026/05/20/new-jmk-research-ieefa-report-warns-indias-2030-renewable-energy-targets-depend-on-rapid-expansion-of-energy-storage/ and https://www.theweek.in/wire-updates/business/2026/10/30/india-s-500-gw-re-target-hinges-on-ldes-scale-up-fy28-viability-gap-funding-key-enabler-iesa-report.html
- Indian equivalents: none found for iron-air or zinc; India awarded LDES contracts for 1,344 MW pumped hydro and a utility-scale flow battery (NTPC at Khavda) — https://www.energy-storage.news/india-awards-long-duration-energy-storage-contracts-for-1344mw-pumped-hydro-utility-scale-flow-battery/ (snippet). Peak XV-backed Newtrace (electrolyzers, Rs 46.91 crore seed, date not confirmed) is adjacent — Entrackr via search result, no URL opened.
- What differs in India: pumped hydro dominates, tariffs are the constraint, buyer is a state discom or NTPC/SECI tender, not a hyperscaler.
- India version sketch: Not buildable overnight as chemistry. The software gap is dispatch forecasting: a model that tells a solar developer when 8h+ storage beats 4h on real Indian price and load data.
- Overnight-demo potential: 2 (chemistry) / 3 (dispatch model on public IEX price data).
- Overlap: none.

---

## 11. Luminai — AI platform for US health-system operations
- Backers and round: Peak XV investment post, 9 Apr 2026 (title: "Transforming Operations for a $5T Industry"); one aggregator reports a $38M Series B led by Peak XV but that page had placeholder text, so unconfirmed — https://peakxv.com/insight/investing-in-luminai-transforming-operations-for-a-5t-industry (opened title via search; page fetch failed) ; https://inforcapital.com/news/luminai-closes-38-million-series-b-funding-round-led-by-peak-xv-partners (snippet)
- Problem, customer, tech: Peak XV says it works with dozens of provider institutions on operations (the repetitive admin work between systems). No further technical detail confirmed.
- Does India have this problem? India check: NOT SEARCHED.
- Indian equivalents: NOT SEARCHED (see CloudPhysician in "Logged in one line" for an Indian Peak XV health-operations bet).
- What differs in India / India version sketch: NOT SEARCHED.
- Overnight-demo potential: 2 on current knowledge (needs hospital system access).
- Overlap: none.

## 12. Pre6 — AI for manufacturing engineering paperwork (drawing reading, ballooning, costing, DFM, PPAP)
- Backers and round: Peak XV Surge 11 cohort, 25 Sep 2025; seed, amount not found — https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11 ; Peak XV profile: https://www.peakxv.com/companies/pre6 (snippet)
- Problem, customer, tech: Auto and engineering suppliers spend days turning customer drawings into inspection balloons, cost sheets and PPAP files. Pre6 reads engineering drawings with vision/LLM models and generates these in minutes. Bengaluru company, founded 2024 by Amod Malviya and Rishi Kedia; site lists SKF, L&T Valves, Rane Group as customers (snippet) — https://pre6-webapp.pages.dev/
- Does India have this problem? Hard number NOT FOUND; it is an Indian company serving Indian suppliers, so the problem exists by construction.
- Indian equivalents: this is itself the Indian entry. Neighbours: SwitchOn (Rs 78 crore / $8M pre-Series B, IvyCap, July 2026; AI quality inspection) — https://yourstory.com/2026/07/manufacturing-tech-startup-switchon-pre-series-b-funding-ivycap-ventures ; Frinks AI ($5.4M pre-Series A, Prime Venture Partners, 2025) — https://www.tribuneindia.com/news/business/frinks-ai-a-manufacturing-ai-startup-by-iit-hyderabad-alumni-raises-5-4m-led-by-prime-ventures ; AugurAI (Rs 2 crore, optics-based inspection, Oct 2026) — https://www.theweek.in/wire-updates/business/2026/10/30/augurai-raises-2-crore-from-campus-angels-network-to-scale-ai-powered-precision-optics-solutions.html (snippets).
- What differs in India / gap left open: Pre6 sells to large tier-1 suppliers. The open gap is the small job-shop (10-50 employees) that quotes from a PDF or a photographed drawing on WhatsApp and costs by gut feel; price point of a few thousand rupees a month and Hindi/Marathi-speaking owners.
- India version sketch: Photo of a part drawing -> extracted dimensions and tolerances -> machining-time and cost estimate in rupees using a small rate table. Demo on 5 public drawings.
- Overnight-demo potential: 4. Drawing-to-fields extraction is a good vision/LLM exercise; costing rules can be hard-coded.
- Overlap: loose, with factory operations (not food, not CCTV).

## 13. SixSense — vision and predictive AI for semiconductor manufacturing yield
- Backers and round: Peak XV Surge 11 cohort, 25 Sep 2025; seed amount not found — https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11 . (Inc42 description: "predictive insights and a no-code deep learning and computer vision platform for semiconductor manufacturing yield". I did not find a standalone SixSense page; founder base not confirmed.)
- Problem, customer, tech: Fabs and assembly/test plants lose yield to defects found late; no-code CV models inspect wafer/die images and predict yield drift.
- Does India have this problem? India's chip assembly/test plants are only starting; no hard number gathered. NOT SEARCHED for fab capacity.
- Indian equivalents: SwitchOn, Frinks, AugurAI (see entry 12); Peak XV-led chip startups C2i Semiconductors ($15M, extended Series A to $16.7M) — https://entrackr.com/news/semiconductor-startup-c2i-semiconductors-raises-15-mn-led-by-peak-xv-11110040 and Agrani Labs ($8M seed, Jan 2026) — https://evertiq.com/news/2026-01-30-indian-ai-semiconductor-startup-agrani-labs-raises-8m (snippets).
- What differs in India: the near-term customers are OSAT lines, PCB and electronics assembly (SMT) lines, not wafer fabs; defect classes are solder, component placement.
- India version sketch: PCB-defect classifier for an SMT line: public PCB defect datasets, a webcam over a board, a pass/fail with bounding boxes.
- Overnight-demo potential: 5. Public datasets, one camera, visible result.
- Overlap: CCTV/vision AI for factories (close).

## 14. Supanote — admin automation for behavioural-health clinics (notes, therapy progress, scribe)
- Backers and round: Peak XV Surge 11 cohort, 25 Sep 2025; seed amount not found — https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11
- Problem, customer, tech: Therapists and psychiatric clinics spend time on session notes and progress tracking. AI scribe plus structured progress notes. No hardware.
- Does India have this problem? India has about 0.75 psychiatrists per 100,000 people, a quarter of WHO's benchmark of 3; treatment gap estimated 70-92%; Tele-MANAS took about 30 lakh calls by Dec 2025 (snippet) — https://www.theweek.in/news/health/2025/12/11/why-are-mental-health-services-still-out-of-reach-for-millions-in-india.amp.html and https://onmanorama.com/news/nation/what-india-wants-now-number-of-psychiatrists.html
- Indian equivalents: none found specifically for mental-health documentation; general scribes in entry 4 (snippets).
- What differs in India: the constraint is clinician time and distribution; counsellors, nurses and social workers are the thin workforce (same source); sessions occur in several languages with code-switching; teleconsults over phone calls.
- India version sketch: Tele-MANAS style call-handler assistant: transcribe a counselling call in Hindi/regional language, produce a risk flag, summary and follow-up reminder. Strong ethics constraints (consent, no diagnosis).
- Overnight-demo potential: 3. Transcribe-summarise is easy; safe risk flagging and test data are hard, and sensitive.
- Overlap: none.

## 15. Puralink — autonomous robots for underground pipe networks
- Backers and round: Peak XV Surge 12 cohort, announced 28-29 Sep 2026; funding not disclosed — https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/ and https://dealroom.co/news/157580-peak-xv-lifts-surge-seed-cap-to-5m-unveils-18-startup-cohort/
- Problem, customer, tech: Utilities need to inspect buried pipes. Puralink builds autonomous robots that travel inside the pipe network. Details beyond that not published in the pages I read.
- Does India have this problem? Non-revenue water is commonly cited at 40-50% (leaks, theft, unpaid) — no single authoritative national figure — https://solve.mit.edu/solutions/83032 and https://zerodha.com/z-connect/?p=381495 (snippets). BWSSB (Bengaluru) is deploying AI and robotics against leaks and theft — https://theprint.in/india/bwssb-to-deploy-ai-and-robotic-technologies-to-curb-water-theft-and-leakages/2947404/ (snippet).
- Indian equivalents: Solinas Integrity (IIT Madras, Chennai; Endobot crawler for 90 mm+ pipes; reported $948K funding; 100+ municipal projects claimed) — https://www.robotics.press/news/solinas-integrity-company-profile/ ; Fluid Robotics (Pune, founded 2016) — https://yourstory.com/socialstory/2019/04/startup-fluid-robotics-robots-water-management ; SmartTerra (BWSSB project, Titan grant) — all snippet.
- What differs in India: intermittent supply and small-diameter, unmapped, mixed-material pipes; customers are municipal corporations buying through tenders with slow payment; robots must survive silt and sewage.
- India version sketch: Skip the in-pipe robot. A leak-detection kit: acoustic or pressure sensors on a hydrant or valve plus a classifier that flags leak signatures; sold per kilometre to a ward engineer.
- Overnight-demo potential: 3. Accelerometer or microphone on a pipe with a toy leak is a quick hardware demo; robot is not.
- Overlap: none.

## 16. Ringg — enterprise voice AI agents (calls, WhatsApp, browser) — Indian company
- Backers and round: Peak XV Partners led, $10M extended Series A (Arkam Ventures, Capital 2B), 26 Aug 2026 — https://news.ventureintelligence.com/private-equity/enterprise-voice-ai-startup-ringg-raises-%2410-m-led-by-peak-xv
- Problem, customer, tech: Enterprises run repetitive outbound and inbound calls. Ringg's agents automate workflows over voice, WhatsApp and browser. About 20 million call attempts a month; customers in healthcare, fintech, banking, marketplaces.
- Does India have this problem? Analysts claim India handles over a billion voice calls a day across support, collections, recruitment, logistics (weak, unattributed in snippet) — https://analyticsindiamag.com/ai-trends/these-7-indian-voice-ai-startups-are-getting-loud/ ; Tracxn-cited figure, $160.58M across 37 rounds in Indian voice-first AI 2019-2026 (low-quality source) — https://claw-times.pages.dev/articles/india-voice-ai-startup-surge-160m-funded-gnani-ai-30m-daily-interactions/
- Indian equivalents / crowding: Bolna ($6.3M seed led by General Catalyst, Jan 2026, customers Varun Beverages, Spinny, Snabbit) — https://yourstory.com/ai-story/voice-ai-startup-bolna-raises-63m-led-by-general-catalyst ; Gnani.ai ($10M, Aavishkaar, Mar 2026) — https://www.newskart.com/gnani-ai-raises-10-million-aavishkaar-capital-march-2026/ ; Navana.ai (Rs 40 crore Series A, Ronnie Screwvala) — https://analyticsindiamag.com/ai-news/voice-ai-startup-navanaai-secures-40-crore-series-a-led-by-ronnie-screwvala ; Sarvam (thin data) (all snippet).
- Gap left open: this space is crowded at the enterprise end. Open gaps I can infer but did not verify: small businesses (clinics, schools, coaching centres, kirana wholesalers) that cannot afford enterprise platforms, and dialects below the top-8 languages. Mark as inference.
- India version sketch: Appointment-reminder and no-show-reduction caller for a clinic in Hindi plus one regional language, priced per call at paise.
- Overnight-demo potential: 4. Real-time voice demo with a phone call is impressive, but it is the most crowded space in this note.
- Overlap: none.

## 17. Zoop — AI live-commerce marketplace for offline retailers and wholesalers — Indian company
- Backers and round: Peak XV (announced at Impact AI PitchFest, India AI Impact Summit, 17 Feb 2026; article 21 Feb 2026); amount and lead not disclosed — https://india.entrepreneur.com/news-and-trends/five-ai-startups-secure-peak-xv-support-to-build/502888
- Problem, customer, tech: Offline retailers and wholesalers sell via live video; tools for voice-based cataloguing, live coaching, operational automation.
- Does India have this problem? Hard number (kirana count) NOT FOUND in my search; the search did not confirm the commonly quoted 1.3 crore stores.
- Indian equivalents: Apnaklub ($3.5M from Sequoia India's Surge) — https://entrepreneur.com/en-in/finance/b2b-fmcg-wholesale-platform-apnaklub-raises-35-mn-funding/379003 ; KiranaPro (claims 30,000 kiranas, 35 cities) — https://inc42.com/?p=502016 ; Kiko Live ($1.1-1.5M) — https://yourstory.com/2024/11/kiko-live-traditional-retailers-growing-ecommerce-market ; Fairdeal.Market ($15M, 20,000+ Delhi NCR retailers) — https://www.outlookbusiness.com/news/fairdealmarket-raises-15-mn-in-funding-round-led-by-bertelsmann-india-investments ; Jumbotail; 1K Kirana — all snippet. Crowded.
- Gap left open: the AI-cataloguing step. Voice or photo of a shelf to a priced catalogue in the shopkeeper's language is the reusable piece.
- India version sketch: Shelf photo -> product recognition and price list -> WhatsApp catalogue. Demo: 20 packaged products.
- Overnight-demo potential: 4 (shelf-photo SKU recogniser).
- Overlap: none.

## 18. Rosella — AI-native commercial insurance brokerage (US businesses)
- Backers and round: Peak XV and Intact Private Capital, about $2.4-2.5M pre-seed, early 2026; in Surge 12 — https://cdn.dealstreetasia.com/stories/peak-xv-partners-rosella-477893 (snippet, "$2.4m") ; https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/
- Problem, customer, tech: Brokers re-key a business's details into 100+ carrier portals. Rosella automates submissions across portals and uses AI to compare policies and flag coverage gaps (snippet).
- Does India have this problem? See entry 7 (63M MSMEs, under 5% adequately insured, snippet). India carrier submission is largely PDF/email, not portals.
- Indian equivalents: BimaKavach, Covrzy, Plum (entry 7).
- What differs in India: fewer portals, more agents; IRDAI-licensed broker needed.
- India version sketch: as entry 7, via a broker licence partner.
- Overnight-demo potential: 3.
- Overlap: none.

## 19. August AI — health assistant (WhatsApp/app) for symptoms, prescriptions, reports — Indian company
- Backers and round: Accel-led $3M seed (Oct 2025 per search page); Inc42 reports Peak XV in talks to put in about $4M (not confirmed as closed); listed in Surge 12 cohort 28 Sep 2026 — https://inc42.com/?p=568262 (snippet) ; https://dealroom.co/news/157580-peak-xv-lifts-surge-seed-cap-to-5m-unveils-18-startup-cohort/ . The "9M users in 160 countries" figure came from the TechCrunch/Dealroom-style summary of the cohort article; I could not corroborate it.
- Problem, customer, tech: Users upload text, audio or lab-report PDFs and get plain-language explanations; B2B deployment with hospital chains (snippet) — https://yourstory.com/2024/09/august-ai-helping-users-access-reliable-health-information
- Does India have this problem? Hard number NOT SEARCHED.
- Indian equivalents: Eka Care (entry 4); Hoola Health (paediatric platform, Surge 12; not searched).
- Gap left open: Beyond urban English users. Voice-first vernacular report explanation for older patients and medicine-schedule adherence; anything touching diagnosis has regulatory risk.
- India version sketch: Lab-report photo -> Hindi voice explanation with "see a doctor" thresholds; no diagnosis.
- Overnight-demo potential: 4.
- Overlap: none.

## 20. Hoola Health — single platform for children's and family care (consults, vaccines, diagnostics, therapy, dental)
- Backers and round: Peak XV Surge 12 cohort, 28 Sep 2026; funding not disclosed — https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/
- Problem, customer, tech: Family-care bundling; AI role unclear from the sources I read.
- India check: NOT SEARCHED. Included only because it is Surge-backed healthcare delivery; weak fit to AI/ML core.
- Overnight-demo potential: 2.
- Overlap: none.

---

## Surge cohorts 2025-26: deep-tech and AI companies

Surge 12 (announced 28-29 Sep 2026; 18 companies, $5M seed ceiling, Peak XV says $50M+ invested, companies raised $90M+ in seed) — source: https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/ (15 named, via fetch) and https://dealroom.co/news/157580-peak-xv-lifts-surge-seed-cap-to-5m-unveils-18-startup-cohort/ ; 3 stealth (education, applied AI, medical products)
- Alma — AI-native personal computing platform (AI/software)
- August AI — AI primary-care clinical intelligence (health; see entry 19)
- Hiloop — post-training platform to adapt open-weight models (AI infrastructure; skipped)
- Hoola Health — children's and family care (health; entry 20)
- Kello — AI talent discovery (HR; skipped), also in Feb 2026 Peak XV announcement
- Kindling — AI content for tech startups (marketing; skipped)
- Puralink — autonomous pipe robots (robotics; entry 15)
- Reinforce Labs — evaluation, red-teaming of enterprise AI (AI safety; skipped)
- Rosella — AI-native commercial insurance brokerage (entry 18; about $2.5M pre-seed)
- Ulook — RF-sensing satellites for spectrum intelligence (space; about $2.3M seed from growX Ventures and InfoEdge Ventures per TechCrunch table; not Peak XV-led)
- Non-fit: Ditto (AI dating, $9.2M seed), GameStock (fintech), Riffle (music), Tribe Money (fintech), Wingit (beauty commerce)

Surge 11 (announced 25 Sep 2025) — source: https://inc42.com/buzz/meet-the-startups-from-peak-xvs-surge-11 (page lists 20; headline said 23; 3 AI ventures in stealth per Entrepreneur)
- Pre6 — manufacturing AI (entry 12)
- SixSense — semiconductor yield vision (entry 13)
- Supanote — behavioural-health admin AI (entry 14)
- Nirmata — Kubernetes policy-as-code (developer tool; skipped)
- Qbeast, Tonbo.io — data infrastructure (developer tools; skipped)
- OnFinance, Finster AI, Ignosis, AIR Trading, Cybrilla, Vault Wealth — finance AI/infrastructure (skipped)
- Round1 AI (AI interviews), Just Words, Palo, Thanks — HR and marketing AI (skipped)
- Consumer: Aretto, NEAU, Neude Skin, Ten X You (no AI core)

Surge 10 (Oct 2024, 14 startups) is outside the January 2025 window; not listed. Source for existence: https://yourstory.com/2024/10/peak-xv-announced-surge-10-cohort

Other Peak XV India announcements in 2026 (not Surge cohorts): five AI startups at the India AI Impact Summit, 17 Feb 2026: Companion Labs, Kello, Memfold AI, Round1, Zoop (amounts undisclosed) — https://india.entrepreneur.com/news-and-trends/five-ai-startups-secure-peak-xv-support-to-build/502888 . Companion Labs: $2.5M seed led by Surge, vernacular character-based AI entertainment for Tier 2-4 cities (consumer; skipped) — https://entrackr.com/snippets/peak-xv-leads-25-mn-round-in-companion-labs-11157241

---

## Logged in one line

Skipped by selection rule (developer tools, model labs, crypto, social, chat wrappers, finance/consumer):
- Sequoia: Auctor ($20M Series A led, Apr 2026, enterprise software implementation, snippet) https://www.pulse.bot/ai/deals/auctor-raises-20m-series-a-led-by-sequoia-capital-41b9e563-35c3-481d-926e-ea6d38c8a2af/ ; Blacksmith ($66M Series C, unicorn, CI tooling, 21 Oct 2026) https://techcrunch.com/2026/10/21/blacksmith-hits-unicorn-valuation-after-sequoia-leads-series-c/ ; Ineffable Intelligence (David Silver lab, ~$1B seed, foundation lab) https://sequoiacap.com/article/partnering-with-ineffable-intelligence-a-superlearner-for-the-era-of-experience ; Etched (inference chips, $300M Series C, 23 Jul 2026) https://sequoiacap.com/article/partnering-with-etched-building-the-inference-machine ; Juicebox, Cymphony, Sail Research, Day AI, Reflection AI, Trajectory, Catalyst (trading agents), Edelbyte (data infra, seed 11 Nov 2026) — dev/model/finance tools, snippets only.
- Sequoia, deep tech but no Indian angle used: Waymo ($16B co-led, 2 Feb 2026) https://sequoiacap.com/article/partnering-with-waymo ; Harvey (co-led $200M at $11B, Mar 2026) https://harvey.ai/blog/harvey-raises-growth-round-at-dollar11-billion-valuation-co-led-by-gic-and-sequoia ; Anterior (prior-authorisation AI, Sequoia led 2023 seed, $40M round Feb 2026 where Sequoia was an existing investor, not lead) https://sequoiacap.com/article/partnering-with-anterior-the-co-pilot-for-health-care ; Neros (defence drones, May 2024 seed, outside window); Cobot (2023, outside window).
- Sequoia context: $10B "reindustrialization" commitment reported in 2026 (manufacturing, energy, defence; dates differ across sources) https://thenextweb.com/news/sequoia-capital-is-putting-10bn-behind-ai-and-reindustrialization ; Sequoia Scout (not Sequoia-led) in Structured AI (construction QA/QC, $4.2M seed) https://proptechconnect.com/structured-ai-raises-42m-to-bring-ai-powered-quality-assurance-to-construction-projects/ ; Magentic (industrial supply chain, $18M Series A led by Felicis, Sequoia participating) via the first search listing (snippet).
- Peak XV chips: Agrani Labs ($8M seed, AI GPU, Jan 2026) https://evertiq.com/news/2026-01-30-indian-ai-semiconductor-startup-agrani-labs-raises-8m ; C2i Semiconductors ($15M, power for AI data centres) https://entrackr.com/news/semiconductor-startup-c2i-semiconductors-raises-15-mn-led-by-peak-xv-11110040 — hardware design, not student-buildable.
- Peak XV manufacturing hardware (dates unconfirmed, Entrackr snippets): Ethereal Machines (precision components, $7.3M Series A led by Surge), Newtrace (electrolyzers, Rs 46.91 crore seed), Incore (semiconductor IP, Rs 24.6 crore seed).
- Peak XV, outside window: CloudPhysician (Bengaluru tele-ICU and AI "RADAR" co-pilot; $10.5M Series A led by Peak XV, 26 June 2024; 200+ hospitals, 23 states, 1 lakh+ patients) https://thebiostartups.com/news/3/934/ai-health-startup-cloudphysician-raises-10-5-m-funding-led-by-peak-xv-partners.html — dated before January 2025, but it is the most direct Indian example of AI applied to Tier-2 critical care and a useful India-gap reference; supporting stat: India has under 5,000 intensivists against 3 lakh+ ICU beds in one source, other sources differ (snippet) https://theprint.in/health/why-ventilators-remain-unused-or-locked-up-despite-patients-at-rural-hospitals-needing-them/661820
- Notable Indian deals from other funds seen in passing: SwitchOn ($8M, IvyCap, SIG Tattva, Trifecta, Jul 2026); Frinks AI ($5.4M, Prime, 2025); Bolna ($6.3M, General Catalyst, Jan 2026); Gnani.ai ($10M, Aavishkaar, Mar 2026); CARPL.ai ($10M, IFC, Jul 2026); Prodoc AI (seed, Velumani family office); BimaKavach (Beyond Capital Ventures, Jul 2026); Marut Drones ($6.2M, Lok Capital, Nov 2024); Ciridae ($20M seed, Accel + a16z, "AI into the physical economy") https://runtimewire.com/article/ciridae-20m-seed-accel-a16z-physical-economy-ai ; Mimic Robotics ($16M seed led by Elaia, Sequoia Scout only) https://www.aol.com/articles/sequoia-backed-mimic-robotics-secures-020110699.html — all from snippets, not chased.

## NOT SEARCHED
- Luminai, Hoola Health, SixSense: any India check (see entries 11, 13, 20).
- Peak XV or Surge companies in climate, agriculture, logistics or construction: my two broad queries returned none in 2025-26 (only Newtrace, Ethereal, Incore with unconfirmed dates).
- Sequoia-led 2025-26 rounds in construction, trucking and warehouse robotics: two queries found none led by Sequoia (Structured AI was Scout only). Sequoia's own "partnering" listings did not show construction.
- Hard Indian numbers for: accounting/GST (entry 9), autonomous site security (entry 6), small-hospital count (entry 5), radiologist shortage (entry 3), kirana count (entry 17), India doctor consultation length (entry 4).
- DGCA rules on autonomous drone flight; IRDAI broker-licence cost; MeitY consent guidance details.
- Surge 12 stealth companies' identities; Surge 11 3 stealth AI ventures.
- Sequoia Arc programme cohorts (not found in any search result).
- Peak XV's own surge.peakxv.com company pages (search returned links; I did not open them).

Searches used: 39
