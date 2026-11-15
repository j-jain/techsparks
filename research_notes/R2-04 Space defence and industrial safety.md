# R2-04 Space, defence and industrial safety (agent: Opus, date 2026-11-03)

> Access notes. Reddit stayed unreachable: arctic-shift returned HTTP 422, then "Too many requests" and "Timeout" on every retry; the two redlib instances were down (HF Space "Preparing", ECONNRESET); old.reddit.com JSON came back empty. So there are NO Reddit counts in this file. YouTube view counts were read from YouTube's own search-results page (ytInitialData, fetched with curl on 3 Nov 2026), not from the returnyoutubedislike API; video dates are approximate, derived from YouTube's "N months ago" label. "(fetched)" = I opened the page; "(snippet)" = search summary only; "(my arithmetic)" = my multiplication; "(my knowledge, unsourced)" = not checked this round. Everything below is civil, defensive and detection-only.

---

## Problem: S2 — GNSS jamming and spoofing near borders and airports, no national detection network

### (a) Proof dossier

Independent items I now stand behind: 12 (4 parliamentary replies on different dates, 2 international bodies, 6+ YouTube videos from different channels with 13k-330k views).

Best items:
- https://www.theweek.in/wire-updates/business/2025/03/20/del31-lsq-flights-gps-interference.html — 20 Mar 2025 — Lok Sabha written reply — ~465 GPS interference/spoofing incidents in the border region, Nov 2023-Feb 2025, mostly Amritsar and Jammu (Round 1, fetched).
- https://www.millenniumpost.in/big-stories/1951-issues-of-aircraft-gps-interference-reported-in-2-yrs-639406 — 12 Dec 2025 — Lok Sabha written reply, MoS Murlidhar Mohol — (fetched) "1,951" GPS interference issues Nov 2023-Nov 2025 after the DGCA circular of 24 Nov 2023; airports: Delhi, Mumbai, Kolkata, Amritsar, Hyderabad, Bangalore, Chennai; WMO examining cases.
- https://www.newkerala.com/news/a/airlines-report-623-incidents-gps-spoofing-delhi-airspace-456.htm — 12 Mar 2026 (IANS) — Lok Sabha written reply, Mohol — (fetched) 2,354 incidents Nov 2023-Dec 2025; 623 more reported by airlines in Delhi airspace in January-February (the lead says 2025, the body says "this year"; article is dated 2026, so I read it as Jan-Feb 2026, but the source is internally inconsistent); within 60 nm of Delhi.
- https://www.theweek.in/wire-updates/business/2025/12/01/del69-rsq-flights-gps-spoofing.html — 1 Dec 2025 — Rajya Sabha reply — Delhi RWY 10 spoofing during GPS-based approaches; AAI asked WMO to find the source (Round 1, snippet).
- https://insidegnss.com/?p=196673 — 8 Apr 2026 — Secure World Foundation, Global Counterspace Capabilities 2026 — (fetched) "more than 10 percent of flights in the Delhi region have reported spoofing incidents"; Indian EW units were used to interfere with GNSS during the May 2025 conflict (my inference: some border-area interference may be India's own, so a detection network must separate friendly from hostile sources).
- https://telanganatoday.com/rising-gps-interference-incidents-a-concern-global-airlines-grouping-iata — 14 Dec 2025 (PTI) — (fetched) IATA names India among new hotspots; global GPS-loss rate 31 per 1,000 flights (2022) to 56 (2024) to an estimated 59 (2025).
- https://www.youtube.com/watch?v=hk6l2UUp__M — ~Nov-Dec 2025 — StudyIQ IAS, 330,314 views — "GPS Spoofing: Fake Satellite Signals Cause Disruptions At Delhi Airport" (view count from YouTube search page, 3 Nov 2026).
- https://www.youtube.com/watch?v=74Esa3zc8cE — ~Nov-Dec 2025 — Flying Beast (airline-pilot YouTuber), 261,978 views — "GPS Spoofing Attack on Delhi Airport": the closest thing to a pilot's public voice I found.
- https://www.youtube.com/watch?v=ywC2R8z2CoE — ~Nov-Dec 2025 — World Affairs by Unacademy, 234,014 views — "GPS Spoofing Hits Kolkata! ...": spread beyond Delhi.
- https://www.youtube.com/watch?v=9Wf0M9HMUqg — ~Dec 2025 — Drishti IAS, 33,494 views; https://www.youtube.com/watch?v=J1cTkW9nHYs — India Today, 20,106 views; https://www.youtube.com/watch?v=gNSqVYit8W4 — Republic World, 17,943 views; https://www.youtube.com/watch?v=gJUUYg7bPng — DW Hindi, 14,373 views (Hindi explainer); https://www.youtube.com/watch?v=gWmUK_uVmlk — India Today Global, ~Jul 2026, 13,399 views — "India Uncovers Suspected Cross-Border GPS Spoofing Network Threatening Commercial Flights".
- June 2026 probe of a spoofing network with bases in at least three neighbouring countries (including Pakistan and Myanmar) — https://threatcluster.io/cluster/india-investigates-gps-spoofing-threat-linked-to-foreign-cyb-8eddb036 — (snippet only, aggregator; no official attribution found). Treat as unconfirmed.

Strongest hard numbers:
1. 2,354 GNSS interference incidents Nov 2023-Dec 2025, plus 623 in Delhi airspace in Jan-Feb 2026 (Lok Sabha, 12 Mar 2026, fetched).
2. 1,951 incidents Nov 2023-Nov 2025, 7 major airports (Lok Sabha, 11 Dec 2025, fetched). Implied: 2,354 − 1,951 = 403 in December 2025 alone, and 623 / 2 ≈ 312 a month in Delhi airspace in early 2026 (my arithmetic). Reporting jumped after the 10 Nov 2025 SOP, so part of the rise is reporting, not interference.
3. >10% of Delhi-region flights reported spoofing (SWF 2026, fetched).

Round 1 figure to discard: "over 800 flights delayed" (The Week, 6 Dec 2025). The 800+ number (Outlook Business amp story, Business Standard YouTube title) describes the 6-7 Nov 2025 Delhi disruption, which AAI attributed to a failure of the Automatic Message Switching System (AMSS) that processes flight plans; other outlets said 400+ (WION) or 100+ (The Week, 7 Nov 2025); the Civil Aviation Minister told Parliament spoofing did not affect flight movements because conventional aids were used — https://www.wionews.com/india-news/what-is-gps-spoofing-that-caused-disruption-of-over-400-flights-at-delhi-airport-1762534357521 and https://www.theweek.in/news/india/2025/11/07/why-delhi-airport-flights-are-delayed-unpacking-atc-snags-that-disrupted-100-flights.amp.html (both snippet). Do not use "800 flights" as a spoofing cost.

Final tier: A on public attention (5+ independent videos with 13k-330k views, plus parliamentary numbers). Caveat: the people who suffer (pilots, ATCs, airlines) speak through institutions, not posts; only Flying Beast is a practitioner voice. Reddit unmeasured.

### (b) Market size

Affected units (sourced):
- Operational airports: 164 as of Oct 2025 (AAI Chairman) — https://tourismbreakingnews.com/indias-operational-airports-count-reaches-164-34-more-to-be-added-by-2047-aai (snippet); 163 (IBEF, Feb 2026, snippet); 166 (undated Parliament reply, snippet).
- Airports officially named for spoofing/interference: 7 (Delhi, Mumbai, Kolkata, Amritsar, Hyderabad, Bengaluru, Chennai) plus Jammu from the border reply = 8.
- Ports, telecom/power/banking timing sites: NOT SEARCHED (no sourced count).

Price anchors:
- Low-cost receiver: u-blox F9P class costs "sub $400" per receiver (Stanford, arXiv 2509.13600v2, 17 Jul 2026, fetched PDF).
- Incumbent airport system: Enaire's DYLEMA at Madrid uses nine stations and costs "on the order of millions of euros" (same paper, fetched).

Bottom-up (my arithmetic, prices are my assumptions):
- Node: F9P + antenna + RTL-SDR + compute + enclosure ≈ ₹60-80k BOM; sell at ₹2.5 lakh + ₹60k/yr service.
- Airport network: 8 nodes = ₹20 lakh capex + ₹4.8 lakh/yr.
- TAM, low-cost model: 164 airports × ₹20 lakh = ₹32.8 cr capex + 164 × ₹4.8 lakh = ₹7.9 cr/yr.
- TAM, incumbent price: top 20 airports × €1M ≈ €20M ≈ ₹200 cr at an assumed ₹100/€ (rate NOT SEARCHED).
- Airline data feed (assumption): 6 airline groups × ₹25 lakh/yr = ₹1.5 cr/yr.
- SAM (first 2-3 years): the 8 named airports × ₹20 lakh = ₹1.6 cr + ₹38 lakh/yr. Tiny.

Who pays today: nobody for ground sensing that I could find. AAI forwards reports to DoT's Wireless Monitoring Organisation (fetched, NewKerala); DGCA's Nov 2023 circular allows the ANSP to set up a threat monitoring and analysis network (https://www.gpsworld.com/indias-dgca-clarifies-10-minute-gnss-interference-reporting-requirement/, snippet; page 403), but I found no sign one exists. Buyers: AAI (central PSU), private airport operators (DIAL etc.), later ports, telecom/power timing, defence. Published India market figure: NOT FOUND. Verdict on size: the domestic civil market is ₹35-200 cr, too thin alone; the venture case needs defence, timing infrastructure or export.

### (c) Competitive map

- Government: DGCA circular (24 Nov 2023) and 10-minute SOP (10 Nov 2025); AAI → WMO source-finding; ICAO GNSS Manual recommends continuous threat monitoring (NewKerala, fetched). DIAL working on a new ILS for RWY 10/28 to cut GPS reliance (snippet via search summary). Gap: reporting is pilot-memory based; no sensor records the RF.
- Accord Software & Systems (Bengaluru) — Navika-1100 GPS L1 + NavIC L5 module with 16-tone interference mitigation and spoofing detection — https://accord-soft.com/navika-1100.php (snippet; datasheet marked preliminary). Protects one receiver; not a monitoring network or map. Funding NOT SEARCHED.
- ISRO SAC NavIC signal-monitoring receiver with notch filtering/pulse blanking — https://www.unoosa.org/documents/pdf/icg/2022/ICG16/WG-B/ICG16_WG-B_18.pdf (snippet). Research/ISRO internal.
- IIT Jodhpur indigenous NavIC receiver project with anti-jam/anti-spoof — https://iitj.ac.in/Electrical-Engineering/en/Design-and-Development-of-NavIC-Receiver (snippet). HAL EoI for anti-jam GNSS for military aircraft — https://idrw.org/indias-shield-against-the-invisible-hals-call-for-next-gen-anti-jamming-gnss-systems/ (snippet). Defence receivers, not civil monitoring.
- "Elena Geo": NOT FOUND (search returned nothing).
- GPSPatron (Warsaw) — GP-Probe DIN L1 (single channel, cannot classify jamming vs spoofing) and GP-Probe TGE2 (classifies), GP-Cloud — https://support.gpspatron.com/support/solutions/folders/101000427657 (snippet). Price NOT FOUND. No Indian deployment found.
- Enaire DYLEMA (Madrid) — 9 stations, multi-beam AoA antennas, "millions of euros" (Stanford paper, fetched).
- Crowd maps: GPSJam — free, ADS-B NACp aggregated in 24 h hexes, does not say it separates spoofing from jamming, India coverage not addressed — https://gpsjam.org/faq (fetched). rfi.stanford.edu similar (Stanford paper). Gap: aircraft-only, daily, no ground truth.
- Septentrio AIM+, u-blox F9 built-in flags, Spirent, Safran: prices and Indian sales NOT SEARCHED.
- Startups in India doing civil GNSS-integrity networks: none found (not proof of absence).

### (d) Solution approaches

1. GNSS "weather station" network (pick). Deep-tech core: the Stanford method on a $400 receiver — a 2-D detector combining SBAS C/N0 (very stable for geostationary SBAS) with a calibrated received-power metric from u-blox's UBX-MON-SPAN FFT (500 kHz bins), auto-calibrated from ~30 min of clean data; cross-receiver voting to localise; plus an RTL-SDR L1 waterfall and a network-time check for clock jumps. Team: hardware (node, enclosure, power), CS (classifier, map, DGCA-format auto-report). First customer: a private airport operator (DIAL) or AAI CNS at Amritsar/Jammu. Unit economics: ₹60-80k BOM, ₹2.5 lakh price, ₹60k/yr service (assumptions). Moat: calibrated Indian dataset (GAGAN SBAS thresholds — India's SBAS is GAGAN, my knowledge, unsourced), event archive across sites, integration with the 10-minute SOP.
2. ADS-B integrity map for Indian airspace (software only). Own 1090 MHz RTL-SDR receivers (receive-only) plus public feeds; India-specific GPSJam with daily reports to airline safety teams. Cheapest, but cannot tell spoofing from jamming and goes blind where no aircraft fly.
3. Drone-side GNSS integrity plus visual-inertial fallback (licence to Indian drone makers). Detect spoofing from IMU/vision vs GNSS disagreement; fall back to visual odometry. Larger per-unit market but crowded and not India-specific.
Pick 1, with 2 as a free data layer to get attention. Bio capability has no role here.

### (e) Regulatory and safety gates

- Possession: the Telecommunications (Radio Equipment Possession Authorisation) Rules, 2026 were notified 8 Jul 2026 under s.3(1)(c) of the Telecommunications Act 2023; authorisation is purpose-based (dealing, or "testing or demonstration"), fee ₹1,000; Rule 10 lists persons who need no authorisation (legacy licences, statutory exemptions, spectrum assignees, amateurs, telecom subscribers); non-radiating or ≤100 mW test equipment must not cause interference — https://www.khaitanco.com/sites/default/files/2026-07/ERGO_Radio_14072026.pdf (14 Jul 2026, fetched PDF). Round 1's "receive-only is unrestricted" is NOT CONFIRMED: I could not read whether GNSS modules or receive-only SDRs fall under a Rule 10 statutory exemption. GNSS receivers in every phone suggest consumer receivers are exempt in practice (my inference). For the demo: use a commercial GNSS module and an RTL-SDR (receive-only); avoid HackRF/Pluto (they can transmit).
- Transmitting: any jamming or spoofing source is "blocking equipment" needing Section 48 permission (same Khaitan note). The demo transmits nothing.
- TEXBAT data: free for research; do not redistribute; cite Humphreys et al. 2012 — https://radionavlab.ae.utexas.edu/texbat/ (fetched). Commercial use is not covered: business gate, not demo gate.
- Business gates: AAI/airport security clearance for equipment on airside; DGCA acceptance of sensor evidence; government procurement (GeM/tenders); defence buyers need security vetting.
- Demo blockers: none if receive-only.

### (f) Overnight wedge

Demo by noon:
- Live node: u-blox F9P (or any u-blox with UBX-NAV-SAT C/N0) on a rooftop + RTL-SDR at 1575.42 MHz; log C/N0, AGC, MON-SPAN, position and clock; dashboard map with a jam/spoof/blocked/OK state.
- Replay: run TEXBAT recordings (download beforehand; file sizes NOT checked) through a software receiver (e.g., GNSS-SDR) and apply the same detector; add synthetic noise digitally to recorded IQ to emulate jamming (software only, nothing radiated).
- Blockage test: cover the antenna with foil to show "blocked" is not mislabelled as jamming.
Honest results reachable in ~14 h: (1) false-alarm count over ~10 h of live nominal data; (2) detection latency on each TEXBAT spoofing scenario (8 datasets in TEXBAT 1.1); (3) separation of blockage vs synthetic jamming. Published benchmark to compare against: on Jammertest 2024 the F9P method flagged RFI with ≥99.5% accuracy, classified jamming at ~95-99% (two receivers fell to 50% and 87% under sweep/PRN jamming), but classified spoofing (meaconing) at only 53-67% with SBAS and near 0% with GPS signals (arXiv 2509.13600v2, Tables 3-4, fetched). Say this openly: cheap receivers detect interference well and spoofing poorly.
Thesis: India now logs ~300 GNSS interference reports a month around Delhi alone (my arithmetic from 623 in two months) and has no sensor that records the RF; a $400-class receiver detects >99% of interference events; a dense cheap network turns pilot reports into localised, time-stamped evidence for AAI/WMO at a fraction of a DYLEMA-class system.

### (g) Verdict

Real and growing (parliamentary counts rose from 465 to 2,354 in ~2 years, partly from better reporting), visibly unsolved on the ground-sensing side, and buildable overnight without transmitting. Sellability is the weak point: the civil domestic buyer is a handful of airports and one PSU, procurement is slow, and spoofing classification on cheap receivers is still poor. Scores (5 = best; for risk, 5 = lowest risk): proof 4, market 2, feasibility 4, unsolved gap 4, deep-tech 5, risk 2.
Round 3 unknowns: (1) whether AAI/DIAL/WMO already has or is tendering a ground monitoring system (RTI or tender search); (2) the Rule 10 exemption text of GSR 592(E) for GNSS modules and receive-only SDRs; (3) whether GAGAN SBAS C/N0 is as stable over India as WAAS/EGNOS were in the Stanford work, and how big the TEXBAT files are.

---

## Problem: S3 — Cheap passive drone detection for the Punjab border strip, jails and district police

### (a) Proof dossier

Independent items I stand behind: ~10 for border drone smuggling; only 3-4 anecdotal items for jail drone drops.

Best items:
- https://www.millenniumpost.in/nation/bsf-seized-294-drones-in-punjab-in-2024-govt-tells-lok-sabha-602874 — 18 Mar 2025 — Lok Sabha — 294 drones seized on the Punjab border in 2024 (Round 1, fetched).
- https://www.tribuneindia.com/news/defence/bsf-integrating-new-technologies-to-strengthen-anti-infiltration-anti-smuggling-grid-in-punjab-jammu-sectors — 3 Dec 2025 — BSF Punjab Frontier — (fetched) 278 rogue drones recovered in 2025, 380 kg heroin, 200+ weapons; smuggling drones are small, ~500 g payload; "frequency-hopping drones make detection difficult"; drone forensics lab in Amritsar; anti-drone systems deployed "on a massive scale" with Punjab Police.
- https://www.newsonair.gov.in/bsf-seizes-272-drones-over-367-kg-heroin-along-punjab-border-in-2025 — 30 Nov 2025 — AIR — 272 drones Jan-30 Nov 2025 (snippet; fetch failed).
- https://www.theweek.in/news/defence/2025/11/18/bsfs-war-on-drones-255-pakistani-drones-neutralised-in-2025.html — 18 Nov 2025 — (fetched) 255 drones "neutralised" by BSF in 2025 (a different measure from "recovered").
- https://www.tribuneindia.com/news/punjab/punjab-to-buy-nine-anti-drone-systems — 10 May 2025 — (fetched) Punjab Cabinet approves 9 anti-drone systems for ₹51.41 cr along 532 km; vendor and capabilities not named. Three were unveiled in Tarn Taran in Aug 2025, three of nine van-mounted (https://www.theweek.in/wire-updates/national/2025/08/09/des46-pb-anti-drone-ld-system.html, snippet).
- https://onmanorama.com/news/kerala/2024/02/23/drones-kerala-police-anti-drone.html — 23 Feb 2024 — (fetched) Kerala Police to buy 20 anti-drone systems at ₹60 lakh each (RF analysers and sensors), funded from a ₹500 cr central allocation; uses: VIP meetings, high-security zones.
- https://www.theweek.in/news/india/2026/09/07/suspected-drone-sighting-near-amritsar-airport-triggers-security-alert-7-flights-diverted.amp.html — 7 Sep 2026 — (snippet) Amritsar airport closed 9:50-11:15 pm after suspected drones; 7 flights diverted to Delhi and Chandigarh.
- https://babushahi.com/full-news.php?id=215807 — 10 Jan 2026 — (fetched) Ferozepur Central Jail phone recoveries 70 (2019) → 437 (2022) → ~500 (2024) → 649+ (2025); phones "often thrown over high jail walls"; ₹126 cr Punjab upgrade for 13 sensitive jails buys AI CCTV and X-ray scanners, NO anti-drone. Same series: https://babushahi.com/full-news.php?id=212631 (26 Oct 2025, fetched) gives 535 to Oct 2025.
- Jail drone anecdotes: Patiala 500 m no-drone zone around jails (Round 1, snippet); drone found near security tower of Modern Jail Kapurthala, tobacco recovered, year unclear — https://www.tribuneindia.com/news/jalandhar/drone-falls-near-security-tower-of-modern-jail-kapurthala/ (snippet); drone over Kannur Central Jail, Kerala — https://www.devdiscourse.com/article/law-order/3766257-drone-mystery-security-alert-at-kannur-central-jail (snippet, date unknown).
- YouTube (views from YouTube search page, 3 Nov 2026): https://www.youtube.com/watch?v=SXB-_SPSMG8 Republic World, ~2021, 38,702 views (Pakistan drone drops 3.2 kg heroin, Ferozepur); https://www.youtube.com/watch?v=azIiUW5sq1g The Tribune, ~2022, 23,650; https://www.youtube.com/watch?v=1ueJRfKv6hA ANI, ~2023, 16,317; https://www.youtube.com/watch?v=D924oT3gIIk Republic, ~2022, 11,999; recent: https://www.youtube.com/watch?v=uDMbPue8IzM CNN-News18 "Punjab's Drone Smuggling Crisis", ~Aug 2026, 1,965; https://www.youtube.com/watch?v=A7rK3DGcZc0 The Tribune "30 Drone Runs in 90 Days...", ~Oct 2026, 1,095. A YouTube search for Indian jail drone drops returned only US videos.

Strongest hard numbers: 294 drones seized (Punjab, 2024, Lok Sabha); 278 recovered (Punjab, 2025, BSF via Tribune 3 Dec 2025); Punjab ₹51.41 cr for 9 systems = ₹5.71 cr each (my arithmetic).

Round 1 correction: the jail angle is weaker than Round 1 implied. The only jail-level numbers (Ferozepur phones) point to wall throws and insiders (a DSP Security was arrested at Sangrur jail in May 2025 — https://newsarenaindia.com/states/drug-racket-busted-inside-sangrur-jail-several-held/44395, snippet), and Punjab's ₹126 cr jail upgrade buys no anti-drone kit.

Final tier: B. Border smuggling alone would reach A on news/government density, but its video engagement is mostly 2021-2023 and in the 10k-40k range; the civil wedge (jails, police stations) is Tier C.

### (b) Market size

Affected units:
- Prisons: 1,332 in India, 5,30,333 inmates, 31 Dec 2023 (NCRB PSI 2023) — https://theprint.in/india/drop-in-inmates-additions-but-indian-prisons-120-full-delhi-jails-most-overcrowded-at-200-ncrb-data/2754893 (1 Oct 2025, fetched). Punjab: 10 central jails (snippet); total Punjab jails NOT FOUND; 13 "sensitive" jails in the ₹126 cr upgrade (Babushahi, fetched).
- Police: 777 police districts and 16,587 police stations as of 1 Jan 2019 (BPR&D DoPO) — https://www.drishtiias.com/daily-updates/daily-news-analysis/data-on-police-organisations-bprd/print_manually (snippet; old).
- Airports: 164 operational (see S2).
- Punjab border: 532 km (Tribune, fetched).

Price anchors: Kerala ₹60 lakh/unit (fetched); Punjab handheld anti-drone guns ₹10 lakh each and static/vehicle ADS ₹10-12 cr each — https://www.securitytoday.in/anti-drone-systems-village-committees-2367-cctv-cameras-to-counter-pak-drones (snippet; fetch got HTTP 429); Indrajaal ₹10 cr urban-police order (unit count unknown).

Bottom-up (my arithmetic; ₹4 lakh per detection-only node is my assumption, 1/15 of Kerala's unit price):
- Jails: 1,332 × 2 nodes × ₹4 lakh = ₹106.6 cr.
- Police districts: 777 × 1 node × ₹4 lakh = ₹31.1 cr.
- Airports: 164 × 4 nodes × ₹4 lakh = ₹26.2 cr.
- TAM (civil, detection-only) ≈ ₹164 cr capex + ~15% AMC ≈ ₹25 cr/yr.
- SAM (Punjab first): 13 sensitive jails × 2 × ₹4 lakh = ₹1.04 cr; border tripwire mesh cueing the ₹5.7 cr ADS units, one node per 2 km: 532 / 2 = 266 nodes × ₹4 lakh = ₹10.6 cr. SAM ≈ ₹12 cr.
- Who pays today: states (Punjab, Kerala) from own budget and the central ₹500 cr security allocation; MHA/MoD for BSF and Army. Published India counter-drone market figure: NOT SEARCHED.

### (c) Competitive map

- Indrajaal (Hyderabad; spun out of Grene Robotics, founded 2023) — wide-area autonomous anti-drone; ₹48 cr pre-Series A (Sep 2025) co-led by India Accelerator and Finvolve — https://inc42.com/?p=530813 (fetched); ~₹155 cr "Ranger" patrol-vehicle orders (Aug 2026), incl. ~₹10 cr from an urban police force; 4 km envelope; GNSS spoofing, RF jamming and cyber-takeover kill chain — https://www.theweek.in/news/defence/2026/08/17/indian-army-orders-mobile-anti-drone-system-what-can-indrajaal-ranger-do.html (fetched). Buyer reported as Army (The Week) vs MHA (company NSE filing, snippet). Alive, well funded, sells crores-scale vehicles, not jail sensors.
- Zen Technologies — MoD anti-drone orders ₹37 cr (Oct 2025) and ₹289 cr upgrade (Oct 2025) (https://www.businesstoday.in/markets/stocks/story/zen-technologies-wins-rs-37-crore-order-from-defence-ministry-check-stock-reaction-deal-details-497715-2025-10-10, snippet). Defence, hard-kill.
- BEL — naval anti-drone system and Army IDDIS contracts (https://theprint.in/defence/navy-signs-contract-with-bel-to-procure-indias-first-indigenous-naval-anti-drone-system/725726, snippet). Defence.
- Paras Defence — MoD anti-drone order Nov 2025 (https://filingreader.com/news-wire/mumbai/2025-11-11/paras-defence-secures-significant-anti-drone-system-order-from-ministry-of, snippet).
- Gurutvaa, Big Bang Boom, Tonbo: NOT SEARCHED.
- Punjab's 9 ADS units: vendor NOT FOUND (a Substack guess of Kotai Electronics/BEL is unreliable).
- Dedrone (global; detects DJI OcuSync/Lightbridge) — https://blog.dedrone.com/en/dedrones-dronetracker-software-platform-detects-entire-dji-product-line-through-lightbridge-1-2-and-ocusync (snippet). Indian price NOT FOUND.
- DJI AeroScope end-of-life: NOT SEARCHED.
- Remote ID: no finalised Indian mandate found; the draft Civil Drone (Promotion and Regulation) Bill 2025 (Sep 2025) requires a DGCA UIN and "traceability" features to be notified later — https://www.medianama.com/2025/10/223-draft-civil-drone-promotion-and-regulation-bill-2025/ (snippet).
- Gap: every Indian vendor found sells ₹10 lakh-₹12 cr systems with jamming/kill; I found no sub-₹5 lakh detection-only node for jails or police stations (absence not proven). But the jail demand itself is unproven (see (a)).

### (d) Solution approaches

1. Passive RF identity node. Deep-tech core: decode DJI DroneID (OcuSync) with SDRs — an open-source prototype does this with two HackRF One radios (Bender, arXiv 2207.10795, Jul 2022, abstract fetched; a 0.75-mile Mavic 2 detection is reported in the paper per search snippet) — plus an ESP32 sniffing Wi-Fi DroneID beacons from Wi-Fi DJI models, plus 2.4/5.8 GHz energy detection. Gives serial, drone GPS and pilot location when DroneID is on. Weakness: smugglers' modified or frequency-hopping drones (Tribune 3 Dec 2025) may not broadcast ID.
2. Acoustic array node (pick for jails/police). 4-8 MEMS mics, edge classifier, TDOA bearing; catches RF-silent, pre-programmed drones. Published ranges: up to 300 m for most methods and 500 m for a YAMNet detector (https://www.preprints.org/manuscript/202401.0209, snippet); a multi-node study cited there reports 98.97% detection at 1.28% false alarms; delivery-event detection 96% at 8% false positives within 100 m (arXiv 2602.09991, snippet). Jail perimeters are a few hundred metres, which fits.
3. Fused border tripwire mesh (pick for Punjab): cheap RF+acoustic nodes every ~2 km on LoRa backhaul that cue Punjab's 9 expensive ADS units and BSF. Buyer: Punjab Police second line.
Pick: 2+1 fused in one node (acoustic for detection, RF for identity), sold first as a cueing sensor to Punjab Police, with jails and airports later. Bio capability has no role.

### (e) Regulatory and safety gates

- Possession of SDRs: same 2026 Possession Rules as S2 (fetched Khaitan note). HackRF can transmit, so it may need a "testing or demonstration" authorisation (₹1,000) unless a Rule 10 exemption applies: Round 3 check. RTL-SDR does not reach 2.4 GHz (my knowledge, unsourced), so the 2.4/5.8 GHz demo needs HackRF-class hardware in receive mode or an ESP32 (2.4 GHz is a de-licensed band, my knowledge, unsourced).
- No jamming, spoofing or takeover: those are blocking equipment needing Section 48 permission (Khaitan note) and are out of scope.
- Flying the test drone: Drone Rules 2021 and Digital Sky zones (green/yellow/red); a sub-250 g nano drone flown by the team in a green zone on campus with university permission (rule details my knowledge, unsourced; check Sonipat's zone on the Digital Sky map before the event).
- Privacy: DroneID includes the pilot's location, which is personal data under DPDP (my inference); log and retain carefully.
- Business gates: MHA/state procurement, BCAS/AAI approval for airport deployment, police tender norms. Demo blockers: none if receive-only and the drone flight is permitted.

### (f) Overnight wedge

Demo: one node (Raspberry Pi/ESP32 + 4-mic array + HackRF in receive-only or ESP32 Wi-Fi sniffer) + phone alert with bearing; team-owned nano drone flown in a permitted area; public DroneRF data (Qatar University, 227 segments, 3 drones, CC BY 4.0 — https://data.mendeley.com/datasets/f4c2b4n755/1, fetched) to pre-train the RF classifier.
Honest results reachable: detection probability at 50/100/200/300 m (≥10 passes each), false alarms per hour over 2-3 h of campus background noise (generators, traffic, birds), bearing error in degrees from TDOA, and whether DroneID decoded (yes/no) for the team's drone.
Thesis: Punjab loses ~280-300 drones' worth of contraband a year at the border alone; India's counter-drone market sells ₹10 lakh-₹12 cr kill systems, so the cheap layer — many passive ears that say "a drone is here, bearing 040°" — is missing, and it can cue the few expensive units Punjab already bought.

### (g) Verdict

The border problem is real and measured, but it is a BSF/defence problem with well-funded Indian vendors (Indrajaal, Zen, BEL); the civil entry point Round 1 proposed (jails) is weakly evidenced, since Punjab's own jail data points to wall throws and insiders, and its ₹126 cr jail upgrade buys no anti-drone kit. Buildable overnight as a detection node; sellable mainly as a cueing sensor to state police. Scores: proof 3, market 2, feasibility 3, unsolved gap 3, deep-tech 4, risk 2.
Round 3 unknowns: (1) the share of jail contraband that arrives by drone (Punjab Prisons RTI or official interview); (2) the share of seized border drones that broadcast DJI DroneID (the BSF Amritsar forensics lab would know); (3) whether any vendor already sells sub-₹5 lakh passive detection nodes in India, and MHA rules for police counter-drone procurement.

---

## Problem: M1+M5 — Dust/chemical blasts and electrical short-circuit fires in small and mid-size factories with paper-only inspection

### (a) Proof dossier

Independent items I stand behind: 12+ (expert panel, state action, NCRB, insurer data, and 10+ YouTube videos from different channels on 5 separate disasters).

Best items:
- https://telanganatoday.com/sigachi-blast-expert-panel-finds-multiple-violations-holds-management-responsible — 23 Nov 2025 — expert panel: 54 dead; MCC dust cloud ignited near a bag-sealing machine; no heat/smoke detection (Round 1, fetched). Death toll reconciles with 46 dead + 8 untraced in Aug 2025 (below).
- https://telanganatoday.com/telangana-government-forms-special-teams-to-inspect-high-risk-industries-after-sigachi-blast — 7 Aug 2025 — (fetched) 4,061 high-risk pharma/chemical/other units in Telangana; 5 special teams led by Deputy Chief Inspectors; 4-phase two-month drive; units must submit a "self-certification checklist" within a week; no sensor or detector requirement.
- One in five high-risk Telangana factories non-compliant (state survey, via search summary, snippet; outlet not confirmed).
- Gujarat Deesa (1 Apr 2025, 21-22 dead): police inspected earlier, filed a negative report (no fire NOC, no extinguishers), no follow-up; SIT formed; Gujarat High Court in Nov 2025 told the Director of Industrial Safety and Health to explain how the unit operated — https://www.livelaw.in/amp/high-court/gujarat-high-court/gujarat-high-court-fire-cracker-warehouse-tragedy-deesa-311109 and https://english.gujaratsamachar.com/news/gujarat/gujarat-high-court-slams-asst-govt-pleader-over-casual-approach-in-deesa-blast-pil (snippets). No new rule found.
- NCRB 2024: 742 factory/machine accidents, 660 deaths; 5,888 fire deaths with 17.2% from short circuits; 149 factory fires (Round 1, Dataful, fetched).
- YouTube (views from YouTube search page, 3 Nov 2026):
  - https://www.youtube.com/watch?v=RDtHOMgBCc4 — Prime9 News (Telugu), ~Jul 2025, 1,760,525 views — exclusive visuals from before the Sigachi incident; https://www.youtube.com/watch?v=fiQToplT5SE — Prime9, 117,427 views — pre-incident CCTV.
  - https://www.youtube.com/watch?v=mxM7s7XKMTE — India Today, ~Jul 2025, 18,047 views — "Safety Lapses Exposed"; https://www.youtube.com/watch?v=QGXkSF0hW3I — India Today, 12,382.
  - https://www.youtube.com/watch?v=xFAaLC5t1e0 — ABP News, ~May 2022, 714,124 views — Mundka fire, people breaking glass to jump; https://www.youtube.com/watch?v=QZwYoNYrpKs — Zee News, 83,554; https://www.youtube.com/watch?v=jOuFhElrT9I — NDTV, 45,710.
  - https://www.youtube.com/watch?v=U51Yzr7Yc5w — DW News, ~Dec 2019, 44,533 — Anaj Mandi; https://www.youtube.com/watch?v=k9w6zKex03Y — The Quint, 13,540; https://www.youtube.com/watch?v=koBEEL7ItyY — CNN-News18, 1,405 — "Short Circuit Caused Blaze, Factory Didn't Have Fire Clearance".
  - https://www.youtube.com/watch?v=Qco-vPdRnFE — Gujarat First, ~Apr 2025, 22,695 — Vadodara administration wakes up after Deesa; https://www.youtube.com/watch?v=qg95es7zV4o — Rajasthan Patrika, 18,340; https://www.youtube.com/watch?v=8Rfm9wAyipA — Aaj Tak, 13,394.
  - Recency: https://www.youtube.com/watch?v=vKRuBV-DFVQ — NDTV, ~1 Nov 2026, 6,471 views — 4 killed in a shoe-factory fire at Mangolpur, Delhi; https://www.youtube.com/watch?v=tp0ziJUhruk — India Today, ~Jul 2026, 3,545 — Tamil Nadu cardboard factory fire after short circuit.

Strongest hard numbers: NCRB 2024 660 factory-accident deaths; 17.2% of 5,888 fire deaths from short circuits; Sigachi 54 dead.

Final tier: A on public attention (Sigachi 1.76M, Mundka 714k, several 13k-84k videos across 5 events). Caveat: the engagement is about disasters, not owners asking for monitoring; willingness to pay is not evidenced (see (b)).

### (b) Market size

Affected units:
- Registered factories: 2,60,061 (ASI 2023-24, up from 2,53,334) — https://rbi.org.in/scripts/PublicationsView.aspx?id=23565 (RBI Table 116, snippet). Replaces Round 1's party-quoted Gujarat 31,500 as the base.
- Major Accident Hazard units: 2,393 (Nov 2024) — https://www.indianchemicalnews.com/general/dcpc-launches-first-training-programme-on-chemical-and-petrochemical-industrial-safety-24291 (snippet); 2,347 factories required to draw on-site emergency plans in 2023 (MoLE via https://dataful.in/datasets/23772/, snippet).
- Telangana high-risk units: 4,061 (fetched). National count of hazardous-process or dust-handling units: NOT FOUND.

Who pays today:
- Insurers: fire premium ₹24,240 cr in FY2024-25, down from ₹25,656 cr — https://www.gicouncil.in/yearbook/2024-25/?p=282 (snippet); fire/engineering tariffs de-notified from April 2024 (secondary summary of IRDAI annual report, snippet), which lets insurers price risk, so monitoring discounts are now possible in principle. Large corporates pay ₹5-250 cr fire premiums (https://business-standard.com/amp/finance/insurance/fire-engineering-insurance-premiums-likely-to-move-up-by-60-in-2025-124122900408_1.html, snippet). No Indian premium discount for IoT monitoring found.
- Factory owners: periodic thermography scans cost ₹15,000-75,000 per facility visit (Elion, vendor, snippet). Enforcement is weak (14 people jailed under the Factories Act in 3 years, Round 1).

Bottom-up (my arithmetic; ₹15,000 per node + ₹500/month monitoring is my assumption):
- TAM (all ASI factories, 3 panel/equipment nodes each): 2,60,061 × 3 × ₹15,000 = ₹1,170 cr hardware + 2,60,061 × 3 × ₹6,000 = ₹468 cr/yr. Upper bound; most small units will not buy.
- SAM (Telangana high-risk, 5 nodes each): 4,061 × 5 × ₹15,000 = ₹30.5 cr + ₹12.2 cr/yr. National MAH units at 10 nodes: 2,393 × 10 × ₹15,000 = ₹35.9 cr.
- Insurer channel ceiling: if insurers spent 1% of fire premium on risk engineering (assumption), ₹242 cr/yr; the industrial share of fire premium is NOT FOUND.
- Published India figure for industrial safety IoT: NOT FOUND.

### (c) Competitive map

- Detect Technologies (Chennai, IIT-M incubated, 2016) — AI safety/inspection for large plants (Vedanta, Tata Steel); $3.3M Series A 2018 (SAIF) — https://yourstory.com/2018/11/chennai-based-detect-technologies-raises-3-3-m-series-funding-led-saif-partners-global-expansion; $12M 2021 (Accel, Elevation) — https://entrackr.com/2021/06/detect-technologies-raises-12-mn-led-by-accel-and-elevation-capital; $28M Series B 2022 (Prosus) — https://prnewswire.com/il/news-releases/industrial-ai-enterprise-detect-technologies-raises-28mn-in-series-b-funding-led-by-prosus-ventures-804664457.html (all snippets). Alive; enterprise-priced, camera/AI, not ₹15k retrofit for MSMEs.
- ICICI Lombard Risk Management — patented an IoT system to avert fire hazards, to be offered to SME and corporate clients — https://www.icicilombard.com/docs/default-source/public-disclosures/2022-2023/q4/press-release/press-release---icici-lombard-risk-management-receives-a-patent-for-iot-enabled-system-to-avert-fire-hazards.pdf (2022-23, snippet; PDF 403). The most direct competitor AND the likeliest partner; current status unknown.
- Thermography/continuous thermal vendors: Elion (periodic scans), Hikvision thermal cameras, Omron K6PM panel IR sensor (designed for abnormal-mode monitoring, not fire detection), iFactory AI (US-priced $95k-240k per deployment; claims insurer premium credits of 40-75%, vendor, unverifiable — https://ifactoryapp.com/industries/cement-plant/thermal-camera-switchgear-inspection, fetched). A search summary attributed a Daman pharma case (42 panels, ₹18.4 lakh ≈ ₹44k/panel) to a vendor page I could not identify; unverified.
- Arc-fault devices: Indian standard IS 17121 for AFDDs exists; recommended for hospitals, schools, hotels, malls, not mandated — https://copperindia.org/closing-the-safety-gap-with-arc-fault-detection-devices-afdds (7 Dec 2021, fetched). AFDDs trip a circuit; they keep no audit trail.
- Government: Telangana special inspections + self-certification; Central OSH Rules pre-published 30 Dec 2025 (snippet); Gujarat SIT. None requires continuous sensing.
- Asimov and Indian thermal-panel makers: NOT SEARCHED.
- Gap: nothing found that gives a small factory a cheap, tamper-evident, continuous record of ignition precursors that an insurer, a buyer's auditor or an inspector can trust.

### (d) Solution approaches

1. Ignition-source monitor (pick). MLX90640 thermal array (32×24, ±1.5 °C, needs calibration — https://zbotic.in/thermal-imaging-camera-for-electronics-mlx90640-guide/, snippet; Melexis pitches the MLX90642 for busbar monitoring, https://www.melexis.com/en/product/mlx90642/far-infrared-thermal-sensor-array-high-snr, snippet) + CT clamp current + ESP32; flags a joint whose temperature rise exceeds what its load (I²R) explains; hash-chained log; WhatsApp alert. Targets the 17.2% short-circuit fire share and the hot surfaces that ignite dust (sealers, motors, dryer outlets). First customer: a pharma/chemical unit in Telangana's 4,061, through an insurer's risk-engineering team. Unit economics: ~₹6-9k BOM, ₹15k + ₹500/month (assumptions). Moat: load-normalised thermal model trained across many panels; insurer integration.
2. Combustible-dust housekeeping monitor. The honest physics: MCC's minimum explosible concentration is ~55-85 g/m³ (St 1, Kst 68-192 bar·m/s; secondary source, https://so09.tci-thaijo.org/index.php/PMR/article/download/3188/1923/13321, snippet), while cheap optical PM sensors read up to roughly 0.5-1 mg/m³ (my knowledge, unsourced) — four to five orders of magnitude lower. So a cheap node cannot measure "explosibility"; it can measure dust escape (PM spikes near sealers/packing) and settled-layer build-up on deposition plates, which feed secondary explosions. The bio/wet-lab members can calibrate the deposition plates gravimetrically (filters + microbalance). Sigachi's ignition was in the packing area during sealing (expert panel), so this is on point.
3. Compliance-evidence layer: sensor log + photo checklist that turns Telangana's self-certification into verifiable records for inspectors and for large customers auditing excipient suppliers. Software-heavy; depends on a regulator or buyer accepting it.
Pick 1 as the product, 2 as the dust module for powder handlers; sell through insurers or buyer audits, not to owners.

### (e) Regulatory and safety gates

- Business: fire detection products are typically certified to BIS standards (IS 2189 system code; detector standards) and anything installed in a dust/gas hazardous zone needs flameproof/intrinsic-safety certification (PESO/CCOE in India) — my knowledge, unsourced; NOT SEARCHED. Liability if an alarm fails; insurer acceptance; data-sharing consent with insurers (DPDP for worker data only if cameras are added).
- Demo: no ignition, no combustible-dust clouds. Use talc or chalk (non-combustible) for the dust demo and a low-voltage (12-24 V DC) loose-terminal rig for the thermal demo. No gate blocks the overnight demo.

### (f) Overnight wedge

Demo: a mock distribution board with one deliberately loose screw terminal carrying 5-10 A at 12-24 V DC; MLX90640 + CT node with load-normalised hotspot alarm and a hash-chained log viewer; WhatsApp alert. Side module: acrylic box with talc, PM sensor + deposition plate.
Honest results reachable: (1) time from fault onset to alarm at a +15 °C load-normalised threshold, over ~10 trials; (2) false alarms over ~2 h of normal load cycling (ambient swings included); (3) deposition-plate reading vs microbalance mass at ~5 talc loadings (R²). No claim of explosion prediction.
Thesis: India inspects ignition sources and dust on paper about once a year (Sigachi's inspection reports "did not reflect" violations); deaths come from conditions that build up over hours or days (a hot joint, a dust layer). A ₹15k node makes them continuous and tamper-evident, paid for by the party that carries the loss (insurer or buyer), not the owner who skipped the audit.

### (g) Verdict

The harm is real, heavily covered and measured by NCRB; the thermal/current part is buildable overnight and technically credible; the dust part is credible only as housekeeping and ignition-source monitoring, not as explosion sensing. The gap is real for MSMEs but the payer is unproven: no Indian insurer discount for monitoring was found, ICICI Lombard has its own IoT device, and enforcement is weak. Scores: proof 4, market 3, feasibility 4 (thermal) / 2 (dust explosibility), unsolved gap 3, deep-tech 3, risk 3.
Round 3 unknowns: (1) will an insurer (ICICI Lombard Risk Management, Tata AIG, New India) pilot or discount for sensor-verified risk, and what happened to ICICI's patented device; (2) national count of dust-handling/hazardous-process units and whether Telangana's self-certification could accept sensor logs; (3) whether an MLX90640 through a panel viewing window catches loose-lug faults reliably at 40-45 °C ambient in dusty Indian plants.

---

## NOT SEARCHED
- Reddit engagement for all three problems (mirrors failed; see access note).
- S2: Septentrio/u-blox/Spirent/Safran/GPSPatron prices; Indian ports and telecom/power/banking timing-site counts; NavIC 2026 operational count (Round 1 value not rechecked); public Jammertest dataset availability; TEXBAT file sizes; ₹/€ rate.
- S3: DJI AeroScope end-of-life; Gurutvaa, Big Bang Boom, Tonbo products and prices; Jammu drone counts for 2025; MHA counter-drone SOP; vendor of Punjab's 9 units; police station count after 2019; any published India counter-drone market size.
- M1: Asimov; Indian thermal-panel makers; post-Deesa Gujarat rule changes beyond the SIT/HC; BIS/PESO certification paths for detectors; pharma customers' supplier-audit response to Sigachi; industrial share of fire premium; Telangana total factory count.
- Exact Rule 10 exemption text of the Telecommunications (Radio Equipment Possession Authorisation) Rules, 2026 (G.S.R. 592(E), 8 Jul 2026).

Searches used: 40
