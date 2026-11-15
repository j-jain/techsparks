# R2-02 Home energy (agent: Opus, date 2026-11-03)

Method note. YouTube view, comment and like counts below were read from each video's YouTube watch page (fields `viewCount`, comment header, like count), fetched 3 Nov 2026; marked "(YT page, 3 Nov 2026)". Cross-check on one video: returnyoutubedislike API gave 7,324 views for wuNGyvLGdxE against 8,480 on the search page, so the API lags. Reddit counts come from the arctic-shift archive API (scores are captured near posting time and may be stale); marked "(arctic-shift, 3 Nov 2026)". "(snippet)" = search-result summary only. "(my arithmetic)" = my own calculation. Risk scores in (g): 5 = highest risk.

---

## Problem: E1 Smart / prepaid meter bill shock with no consumer-side way to verify the meter (with E6: outages with no ground truth)

### (a) Proof dossier

Independent items I can stand behind: 13 new this round (8 YouTube videos from 8 channels, 5 news/regulator items from different outlets and dates; Round 1's ThePrint, Aaj Tak, Tribune, Hitavada and Patrika items still stand and are not repeated here).

- https://www.youtube.com/watch?v=yt1T7Fl3vMg — 28 Jun 2026 — 28,60,983 views, 553 comments, 30,760 likes (YT page, 3 Nov 2026) — Umar Solar, "Kya Smart Meter Tez Bhagta Hai | Smart Meter Test": a home test of whether the smart meter runs fast. This is direct demand for consumer-side verification.
- https://www.youtube.com/watch?v=GqxEiMRWxxM — 28 Mar 2026 — 13,51,066 views, 1.9K comments, 8,532 likes (YT page, 3 Nov 2026) — Sanskriti PCS, "UP Smart Meter Controversy: Smart Meter Scam or System Failure? Ground Reality from Uttar Pradesh".
- https://www.youtube.com/watch?v=PcbCRTNbiMk — 3 May 2025 — 10,47,973 views, 637 comments (YT page, 3 Nov 2026) — Viral Khan Sir, "सरकार हर घर में Smart Meter क्यों लगवा रही है? | बिजली बिल ज्यादा क्यों आ रहा है?"
- https://www.youtube.com/watch?v=-jx2bCdpLlQ — 21 Jul 2025 — 9,30,480 views, 667 comments (YT page, 3 Nov 2026) — NewsHooks, "क्या है स्मार्ट मीटर का सच?" #uppcl.
- https://www.youtube.com/watch?v=MDXGm__TTIQ — 24 Apr 2026 — 6,92,783 views, 335 comments (YT page, 3 Nov 2026) — Zee Uttar Pradesh, new UP smart-meter rules, penalty for not restoring supply.
- https://www.youtube.com/watch?v=VBLgbnDBhKA — 8 Oct 2026 — 3,81,761 views, 280 comments (YT page, 3 Nov 2026) — SolarSquare, "Smart Meter लगते ही Electricity Bill 4X? - असली Reason क्या है?" A funded rooftop-solar company now uses smart-meter bill shock as a sales funnel.
- https://www.youtube.com/watch?v=mba0Ru6mh8s — 17 Aug 2025 — 1,64,608 views, 148 comments (YT page, 3 Nov 2026) — Bijli Forum, "Smart Meter Running Fast?"; a second Bijli Forum video on the same topic covers filing at a consumer forum.
- https://www.youtube.com/watch?v=AyoZvEATW5E — 30 Mar 2026 — 11,775 views, 32 comments (YT page, 3 Nov 2026) — Aleemtake, "बिल जमा होने के बाद भी लाइट नहीं चली" (power not restored after recharge).
- https://test.uniindia.com/uproar-in-maha-assembly-over-mandatory-smart-metre-rollout/west/news/3897763.html — 3 Jul 2026 — UNI wire — Maharashtra Assembly uproar; MoS Energy: smart meters mandatory, prepaid optional; 1.23 crore installed; 3.92 lakh billing complaints.
- https://newsable.asianetnews.com/gallery/india/uttar-pradesh-smart-meter-row-complaints-protests-and-govt-relief-explained-pvvtaxa — 21 Apr 2026 — Asianet Newsable, citing India Today — UP: 78 lakh+ smart meters, 70 lakh+ in prepaid mode; protests in Jalaun (meters thrown on roads, 70+ booked), Aligarh, Noida, Lucknow; replacement paused; 4-member expert committee (IIT Kanpur, ERDA Vadodara, UPPCL) to check accuracy.
- https://www.freepressjournal.in/amp/mumbai/thane-msedcl-steps-in-as-smart-meter-complaints-rise-check-meters-to-be-installed-for-accuracy-audits — 31 Jul 2026 — FPJ — Thane: 3 lakh+ smart meters of ~7.5 lakh consumers; consumers allege bills up with unchanged consumption; MSEDCL to fit old meters as check meters beside 20-25% of new smart meters and at complainants' premises, compare for 2-3 months. MSEDCL chief engineer: meters record identically (a stated position, not an audit).
- https://www.freepressjournal.in/uttar-pradesh/up-power-companies-resolve-99-of-2017-million-electricity-complaints-registered-in-july-2026 — 11 Aug 2026 — FPJ — UP 1912 helpline: about 20.17 lakh electricity complaints in July 2026 alone (all types; smart-meter share not given).
- https://solarquarter.com/2026/08/31/uperc-closes-smart-meter-overcharging-case-after-inr-32-74-crore-consumer-refund/ — 31 Aug 2026 — SolarQuarter — UPERC closed suo-motu case 27 Aug 2026 after Rs 32.74 crore credited to 92,231 accounts.
- Reddit (arctic-shift, 3 Nov 2026): smart-meter posts in r/india and r/legaladviceindia are small (e.g. r/legaladviceindia "BEST sent SMS notice for change to Smart Meter. Can we resist?", 22 Oct 2026, 1 point, 4 comments; "GEB installing smart meter without permission", 12 Jan 2025, 4 points, 6 comments; r/india "UP discom scraps Adani's Rs 5,400-crore smart meter bid", 6 Feb 2023, 79 points, 12 comments). The best Reddit item is r/nagpur "MSEDCL smart meter scam", 24 Jun 2026, 73 points, 45 comments. The conversation lives on Hindi YouTube and Hindi news, not Reddit. See the end-of-file Reddit block, which also has the r/gurgaon outage-mapping threads for E6.

Strongest hard numbers:
1. 7.24 crore smart meters installed (consumer + DT + feeder) as of 30 Jun 2026, 5.73 crore of them under RDSS; 19.79 crore consumer meters sanctioned; RDSS sunset 31 Mar 2028 — https://www.tndindia.com/indias-smart-meter-population-at-7-24-crore-parliament/amp/ (MoS Power written reply, page undated, "3 months ago").
2. Maharashtra: 3.92 lakh billing complaints on 1.23 crore smart meters (UNI, 3 Jul 2026, above). UNI says "roughly 4%"; 3.92/123 = 3.2% (my arithmetic).
3. UP 1912 helpline: 20.17 lakh complaints in one month (FPJ, 11 Aug 2026).

Final tier: **A**. More than 5 independent items with six- and seven-figure view counts and hundreds to ~2,000 comments, plus government numbers.

Round 1 figures I now believe are wrong or need restating:
- "UP refunding ~Rs 200 crore to 5 lakh+ consumers" (FPJ, 11 May 2026) was the announcement. The regulator-closed figure is Rs 32.74 crore to 92,231 accounts (UPERC, closed 27 Aug 2026, SolarQuarter above). More important: the refund is for **meter cost over-recovered on new connections** (Rs 6,016 charged vs Rs 2,800 approved), not for inaccurate metering. It is not evidence that the meters mis-record.
- "52.8 million smart meters" (ThePrint, Apr 2026) is superseded by 7.24 crore at 30 Jun 2026 (above).
- UP did not drop smart meters. It moved prepaid to postpaid (FPJ 11 May 2026; ~84 lakh consumers per The Goan, 30 May 2026: https://www.thegoan.net/the-goan-special/spotlight-ï»¿while-goa-resists-other-states-accelerate-meter-upgrade-drive/148961.html).
- No accuracy finding was found for the UP expert committee. MSEDCL and an Andaman CGRF check-meter case (https://vidyut.andamannicobar.gov.in/Doc/07-10-2023_18Complaint%20No.%20ANI-CGRF-276-23-24-08%20dated%2015.06.2023.pdf, 2023, snippet: "no discrepancy found") point the other way. The pain may be less "the meter is wrong" than "nobody can explain why my bill rose" (catch-up after slow old meters, estimated bills, prepaid deductions, new loads, earth leakage).

E6 (outages) proof added this round: Prayas ESMI ran ~400 voltage monitors in 23 states, at scale 2015-2018, data until 2023 (https://www.watchyourpower.org/faqs.php; https://energy.prayaspune.org/our-work/policy-regulatory-engagements/electricity-supply-monitoring-initiative, snippet). Delhi has per-hour outage compensation (Rs 50/h, then Rs 100/h; DERC SOP https://www.derc.gov.in/sites/default/files/4th-Amendment-SOP.pdf, undated, snippet). A 2018 critique names "no proper real-time monitoring of electricity supply" as a gap (https://www.shankariasparliament.com/current-affairs/addressing-the-shortcomings-in-compensating-policy, 24 Apr 2018). E6 stays Tier B on its own.

### (b) Market size

Bottom-up (dispute-driven buyers):
- Complaint rate: 3.92 lakh / 1.23 crore = 3.2% of smart-meter households lodge billing complaints (Maharashtra, UNI 3 Jul 2026; my arithmetic).
- National installed: 7.24 crore × 3.2% = 23.2 lakh complaining households (my arithmetic; overstated slightly because 7.24 crore includes DT and feeder meters).
- At full RDSS: 19.79 crore consumer meters × 3.2% = 63.3 lakh (my arithmetic).
- Price: Rs 2,500 per device (assumption). Comparators: SustLabs Ohm Assistant Rs 6,680 single-phase (Intelliware, undated: https://intelliware.in/product/electricity-monitor-sustlabs-ohm-assistant-1-phase/), Amazon range Rs 5,680-6,880 (price-history.in, older, snippet); generic Tuya Wi-Fi CT meters Rs 3,199-5,490 (Fruugo India listings, undated, snippet); DIY PZEM-004T + CT Rs 400-600 (https://zbotic.in/home-energy-monitor-with-esp32-and-pzem-004t-module/, snippet).
- **TAM (dispute-driven, installed base): 23.2 lakh × Rs 2,500 = Rs 580 crore one-time; at full RDSS Rs 1,583 crore cumulative to 2028** (my arithmetic).
- **SAM (UP + Maharashtra, where disputes are loudest): Maharashtra 3.92 lakh + UP 78 lakh × 3.2% = 2.5 lakh → 6.4 lakh households × Rs 2,500 = Rs 160 crore** (my arithmetic; UP rate assumed equal to Maharashtra's).
- Rental variant: one device covers four 3-month check periods a year (the statutory check-meter window); Rs 500 per rental to an RWA or consumer body = Rs 2,000/device/year (assumption).
- Ceiling framing: every smart-meter home buying a Rs 2,500 monitor = 7.24 crore × 2,500 = Rs 18,100 crore. I do not believe this; home energy monitors have stayed niche (SustLabs has raised only ~US$1.5 M, see (c)).
- Who pays today: the consumer pays nothing for a discom check meter (statutory, see (e)); a NABL lab test costs Rs 450 single-phase / Rs 550 three-phase (CSERC-empanelled lab, https://solarquarter.com/2026/03/17/cserc-empanels-nabl-accredited-lab-to-ensure-transparent-testing-of-defective-electricity-meters-in-chhattisgarh/, 17 Mar 2026), and the fee is forfeited if the meter is found correct (snippet). Buyers: consumers via RWAs; possibly discoms that need trust audits (MSEDCL is fitting check meters on 20-25% of new installs, FPJ 31 Jul 2026).
- No published market figure for consumer check meters found.

### (c) Competitive map

| Who | What | Funding / status | What it does NOT do |
|---|---|---|---|
| Discom check meter (all states) | Second licensee meter beside the disputed one for at least 3 months, within 5 days of complaint (2024 Rules) | Statutory; MSEDCL plan 31 Jul 2026; APDCL (R1) | Consumer does not control it; consumers distrust the discom testing itself (Hitavada, R1) |
| NABL meter labs | Bench test of a removed meter | Rs 450 (CSERC, Mar 2026) | One snapshot in a lab, not in-situ consumption; no explanation of the bill |
| Discom apps (UPPCL etc.) | Show consumption from the disputed meter | ThePrint (R1): 54,321 of 1,24,590 app users knew about real-time data | Same data source as the dispute |
| SustLabs Ohm Assistant (IIT Bombay incubated) | Single-point NILM home monitor | ~US$1.5 M total (Caplight, PitchBook; aggregators), last round an accelerator round Dec 2023 (Inc42/CB Insights, snippet: https://inc42.com/company/sustlabs/funding/); licensing its AI to Schneider/Legrand for meters (snippet). Alive | No evidence-grade log, no dispute workflow, no prepaid-deduction reconciliation; Rs 5.7-6.9k price |
| Generic Tuya / Smart Life CT meters | Wi-Fi kWh logging | Commodity, Rs 3,199-5,490 | No calibration certificate, cloud abroad, no tamper-evident record |
| Prayas ESMI (E6) | Plug-in voltage/outage monitors, public data | NGO; ~400 sites, at scale 2015-2018, data to 2023 | Never found a paying buyer; data used in regulator submissions only |
| SolarSquare | Rooftop solar; makes smart-meter bill-shock content | US$53 M Series C Jun 2026 (https://renewablewatch.in/2026/06/17/solarsquare-raises-53-million-in-series-c-funding-round/, snippet); plans "home energy management" (aggregator, snippet) | Not a meter; likely future entrant |
| Sense / Emporia | US home monitors | NOT FOUND in India (search returned no India pricing) | — |

Gap: no product gives a household a calibrated, tamper-evident, in-situ record that (1) matches the statutory 3-month check-meter window, (2) explains the bill by appliance, and (3) turns into a complaint pack. The hardware is a commodity. The gap is trust, calibration and workflow.

### (d) Solution approaches

1. **Witness check meter (hardware + crypto).** ESP32 + class-1-capable metering IC (ATM90E26 / ADE7953) + split-core CT + plug-in voltage reference, RTC and a secure element (ATECC608) signing a hash-chained minute log of kWh, V, I, PF and outages. Rented through RWAs for the 3-month check period; auto-builds a side-by-side "my witness vs your meter" complaint pack for the discom, then CGRF. First customer: Noida RWA federation (its head said "hundreds" queue at offices, ThePrint R1) or UP consumer council (UPRVUP, which challenged the MVVNL lab's IS 16444 accreditation, https://indianmasterminds.com/news/yogi-adityanath-smart-meter-overbilling-probe-up-196930/, snippet). Unit economics (assumptions): BOM Rs 1,500-1,800, rent Rs 500/quarter or sell Rs 2,500. Moat: calibration and trust brand plus a dataset of thousands of disputes. The hardware moat is weak.
2. **Bill explainer with leakage detection (hardware + ML).** Same device plus a core-balance (residual current) CT on phase + neutral to catch earth leakage, the cause a Nagpur expert blamed for inflated bills (Hitavada, R1), which is also a shock hazard. On-device NILM labels AC / geyser / EV / pump load so the user sees why the bill rose. Most disputes may end with "the meter is right, here is why", and that is still valuable to the consumer and to the discom.
3. **Discom trust audits (B2G).** Sell randomised independent loggers to discoms / SERCs to settle complaint clusters and publish results (MSEDCL already spends on check meters for 20-25% of installs). Long sales cycle; conflicts with discoms' own position that their meters are right.
4. (E6) **Colony outage ledger.** Cheap plug-in voltage nodes, mesh to an RWA dashboard, compensation-claim generator where SoP compensation exists (Delhi). ESMI's history says it had no buyer; keep it as a free feature of approach 1 or 2.

Pick: **2 built on 1**, a check meter whose first output is an explanation plus a leakage alarm, with the signed log as the dispute backstop. It uses the hardware team, gives the ML team a real task, and has value whether the meter is right or wrong.

### (e) Regulatory and safety gates

- Electricity (Rights of Consumers) Amendment Rules 2024 (notified ~22 Feb 2024): on a complaint that readings do not match consumption, the licensee must install an additional meter within 5 days for at least 3 months; meter testing within 30 days (https://powerline.net.in/2024/02/26/mop-notifies-electricity-rights-of-consumers-amendment-rules-2024/, snippet; https://www.legitquest.com/act/electricity-rights-of-consumers-amendment-rules-2024/F72A, snippet). A Ministry advisory reportedly also asks for check meters on up to 5% of smart meters (https://righttoinformation.wiki/practical-guides/electricity-bill-doubled-smart-meter-installation, secondary source, snippet). So the state already supplies a free check meter. The product must win on trust and explanation, not on existence.
- Admissibility: NOT SEARCHED in depth. My reading: a consumer device is not a revenue meter under the CEA metering regulations, so CGRF/Ombudsman will decide on the licensee's check meter or a NABL test. Consumer commissions use summary procedure and can weigh other evidence. A court filing of an electronic log would need a Bharatiya Sakshya Adhiniyam s.63 certificate (not verified). Realistic role of the log: trigger and steer the official test, not replace it.
- DPDP Act 2023: minute-level load data reveals occupancy and habits; consent, local storage and deletion needed.
- Electrical: the CT is non-invasive, but the voltage tap at the DB needs a licensed electrician; a plug-in voltage reference avoids opening the DB.
- WPC: ESP32 modules with existing ETA approval for 2.4 GHz (assumed, not checked).
- Blocks the demo: none (bench rig on an enclosed module). Blocks the business: trust and calibration (NABL calibration of the product line), plus the legal standing of logs.

### (f) Overnight wedge

- Build: ESP32 + enclosed PZEM-004T or ATM90E26 board with CT on one extension lead; DS3231 RTC; SHA-256 hash chain signed with a device key (ATECC608 if in the kit, otherwise a key in flash); small web dashboard; residual-current CT test with a deliberately unbalanced low-voltage loop; NILM model trained on the public iAWE Indian-homes dataset (IIIT-Delhi, https://iawe.github.io/; not re-verified this round).
- Tests reachable in ~14 h (numbers, not claims):
  1. kWh error % vs a commercial plug-in energy meter across 5 loads (kettle ~1.5 kW, iron, fan, LED bulb, laptop charger as a non-linear load), each over 20-30 min. Target ≤2%.
  2. Outage detection: 20 power-strip off/on cycles → detection rate and timestamp error (s).
  3. Tamper test: edit 1 of N stored records → verification failure rate (should be 100%).
  4. NILM: per-appliance F1 on held-out iAWE days for 4-5 appliances.
- Deep Tech Thesis line: smart meters moved the trust problem from the meter reader to an algorithm the consumer cannot see. A calibrated, signed Rs 2k witness that also explains the bill restores it, and turns 3.2% complaint rates into evidence either side can accept.

### (g) Verdict

Real: yes. Tier A, with million-view Hindi videos and 3.92 lakh complaints in one state. Unsolved: partly. The law already gives a free discom check meter, cheap Wi-Fi monitors exist, and the UP refund was about meter price, not accuracy. What is unsolved is trust and explanation. Sellable: thin as a device (SAM ~Rs 160 crore one-time); better as an RWA rental, a trust service, or a feature in a home-energy product (SolarSquare is circling). Buildable overnight: easily. Scores: proof 5, market 2, feasibility 5, unsolved gap 3, deep-tech 3, risk 3.

Three unknowns for Round 3:
1. Has any CGRF, Ombudsman or consumer commission order relied on consumer-side logged data? Find 3 orders on indiankanoon / CGRF sites.
2. Can a consumer device read an IS 16444 smart meter's optical/DLMS port at public-client level without discom keys, to auto-compare readings?
3. Willingness to pay: will a Noida/Ghaziabad RWA or UPRVUP pay Rs 500 per 3-month rental? Needs 3 calls. Also what the UP expert committee concluded on accuracy.

Reddit sweep (E1): see end-of-file block "Reddit sweep results".

---

## Problem: E2 Rooftop solar after installation: substandard installs, low output, net-meter limbo, subsidy waits (PM Surya Ghar)

### (a) Proof dossier

Independent items I can stand behind: 14 (8 YouTube channels + 2 new news/government items + 4 from Round 1; Round 1's Mongabay 28 Aug 2025, MNRE SOP 25 Jun 2026, Tribune Sirsa 7 Jan 2025 and Sentinel Assam 6 Jul 2026 still stand).

- https://www.youtube.com/watch?v=Eq7cBo-OPD8 — 22 Nov 2025 — 20,45,441 views, 6.2K comments, 33,188 likes (YT page, 3 Nov 2026) — Bijli Forum, "सोलर से बिजली बेचने के नाम पर बेवकूफ बनाया जा रहा है" (net-metering export economics; a consumer-advocacy channel).
- https://www.youtube.com/watch?v=YN3dnxFvwiw — 8 Dec 2025 — 8,89,800 views, 2K comments (YT page, 3 Nov 2026) — Tapan Gupta, an owner's series: "First Bill After Net Metering ... बिजली विभाग का धोखा"; his 9th-bill video, "सत्यानाश!! सोलर लगाने के बाद भी 2528 रुपए का बिल" (5 Aug 2026, 12,043 views, 161 comments), https://www.youtube.com/watch?v=3IPkfgfdMXY.
- https://www.youtube.com/watch?v=YjkzMaQIRRs — 1 May 2026 — 12,48,824 views, 314 comments (YT page, 3 Nov 2026) — Shanu Gyan, "पैसा बर्बाद? 3kW Solar System लगाया | ये 3 गलतियां…".
- https://www.youtube.com/watch?v=mMdId47m8dc — 11 Aug 2026 — 15,60,464 views, 347 comments (YT page, 3 Nov 2026) — Deepak chaudhary (an installer channel), "PM Surya Ghar: सोलर लगवाने से पहले ये 5 बड़े धोखे".
- https://www.youtube.com/watch?v=lOXK5cQTiAs — 31 May 2025 — 3,10,752 views, 415 comments (YT page, 3 Nov 2026) — Anand Master Ji, "Biggest Scam Alert! TATA Solar Ongrid 3.3kW | PM Muft Bijli Yojana".
- https://www.youtube.com/watch?v=ewlIx84_UM4 — 26 Oct 2025 — 75,265 views, 267 comments (YT page, 3 Nov 2026) — owner review, "3kW On Grid Solar का झटका! बिल कम नहीं, ज्यादा आया".
- https://www.youtube.com/watch?v=ijtw1jWY-mI — 10 May 2026 — 11,393 views, 38 comments (YT page, 3 Nov 2026) — Varanasi: cheap system, "Vendor ने लगा दिया घटिया सिस्टम".
- https://www.youtube.com/watch?v=lOxX4djbHg4 — 16 Oct 2026 — 10,779 views, 18 comments (YT page, 3 Nov 2026) — "Solar Panel सही से काम कर रहा है की नहीं कैसे चेक करें? Solar Performance Test" (demand for self-checking).
- https://solarquarter.com/2026/08/27/mnre-deactivates-66-pm-surya-ghar-vendors-over-rooftop-solar-application-backlog/ — 27 Aug 2026 — SolarQuarter (snippet) — MNRE deactivated 66 vendors over pending applications.
- https://www.downtoearth.org.in/energy/as-rooftop-solar-scales-up-india-confronts-a-generation-blind-spot — 24 Dec 2025 — Down To Earth — "the government has no comprehensive data on how much electricity these systems actually generate"; 23.2 GW rooftop installed (Nov 2025); consumers report "suboptimal daily generation".
- Caveat: several of the highest-view videos are from installers or explainers, not aggrieved owners. The loudest pain is net-metering bills and subsidy delays; generation shortfall is a quieter third.

Strongest hard numbers:
1. **Verified:** 25,02,217 rooftop systems installed of 63,26,125 applications as of 5 Mar 2026 (Rajya Sabha reply); 31,12,850 households benefited as of 6 Mar 2026 (Lok Sabha reply) — https://www.millenniumpost.in/amp/business/pm-surya-ghar-yojana-benefits-over-31-lakh-homes-naik-651369 (11 Mar 2026). Round 1 called the 25.02 lakh "households"; it is systems.
2. Latest: 50.06 lakh households, 14.8 GW commissioned (MNRE, 4 Aug 2026), record 5.06 lakh installs in July 2026 — https://solarquarter.com/2026/08/07/pm-surya-ghar-scheme-crosses-50-lakh-rooftop-solar-installations-adds-record-5-06-lakh-homes-in-july-2026/ (snippet); 40.07 lakh systems in a late-July Parliament statement (snippet via search summary). Target 1 crore households by FY 2026-27.
3. Shortfall, primary source: CEEW-BYPL field study, Nov 2023, 61 of 681 rooftop sites in BYPL Delhi (~9 MW). Average present CUF ~10-12% by circle vs 15-17% achievable with O&M; "35-60% more energy production from the existing systems" with regular maintenance; dust losses "reported to be 13.4%"; 80% of sites reported soiling issues; "28% of the panels found to be damaged"; average annual degradation 2%; ~70% of residential owners maintain systems themselves. 27 of 61 sites (44%) had CUF below 13% (my arithmetic from the sample table) — https://www.ceew.in/sites/default/files/CEEW-research-achieving-optimum-energy-generation-from-rooftop-solar-systems.pdf (PDF read 3 Nov 2026).
   - Round 1 / vendor figure to drop: "50% of home systems underperform by 30%" is SolarSquare's paraphrase (https://www.solarsquare.in/blog/does-your-solar-guarantee-power-production-and-savings, 1 Aug 2024). The CEEW sample is small, Delhi-only, pre-PM Surya Ghar and mixes residential with C&I. Cite the CEEW numbers above instead.

Final tier: **A**. More than 5 independent items with lakhs of views and thousands of comments, plus Parliament figures and a field study. But generation shortfall specifically (the wedge's target) is Tier B on public engagement; most anger is about bills, net metering and subsidy.

Reddit sweep (E2): see end-of-file block.

### (b) Market size

- Units: 40.07 lakh systems (late Jul 2026) → ~50 lakh by Aug on the household measure; 1 crore target by FY27 (sources above).
- Price: device Rs 2,500 + Rs 600/year service (assumption). Comparators: Tuya bidirectional Wi-Fi solar meters Rs 3,199-4,349 (Fruugo India listings, undated, snippet: https://www.fruugoindia.com/smart-wifi-energy-meter-with-buzzer-overload-alarm-solar-power-generation-consumption-monitoring-single-phase-2-ct/p-370625796-803071119); installer-grade monitoring Rs 25,000+ (IndiaMART listing, snippet); CEEW basic AMC package priced at Rs 1,025 + Rs 768 per kW (Nov 2023 PDF; reading of the formula ambiguous).
- **TAM: 40 lakh × Rs 2,500 = Rs 1,000 crore one-time + 40 lakh × Rs 600 = Rs 240 crore/year; at the 1 crore target, Rs 2,500 crore + Rs 600 crore/yr** (my arithmetic).
- **SAM (underperformers): 44% × 40 lakh = 17.6 lakh × Rs 2,500 = Rs 440 crore** (my arithmetic; the CEEW share from n=61 extrapolated, weak).
- Published figure: CEEW puts the basic-AMC market at ">700 crore" on a 9 GW base (Nov 2023 PDF). Plausible as a ceiling for O&M services, not for a monitoring device.
- Who pays today: the vendor (M2M monitoring is mandated on the vendor, see (c)); the household pays for AMC/cleaning if at all (70% self-maintain, CEEW); SolarSquare bundles a 5-year savings guarantee into its price. Buyer candidates: households (willingness to pay untested), state nodal agencies/discoms enforcing the MNRE SOP, installers who want to prove performance, O&M/cleaning crews.

### (c) Competitive map

| Who | What | Funding / status | What it does NOT do |
|---|---|---|---|
| MNRE M2M mandate (Dec 2025) | SIM-based remote monitoring required on all PM Surya Ghar systems; inverter data to national servers; OERC recognised M2M inverters as generation meters | Government; formal implementation dates not announced as of 24 Dec 2025 (DTE, above) | Legacy 23.2 GW not covered; data comes from the installer's inverter; no consumer-facing verdict |
| MNRE OM 17 Aug 2026 | Inverter-level data stored in India; daily cumulative generation by inverter serial to the National Portal; OEMs had 30 days to confirm or be barred | https://solarquarter.com/2026/08/21/mnre-mandates-domestic-data-storage-for-solar-inverters-under-pm-surya-ghar-scheme/ (snippet) | Compliance outcome not found; no irradiance-normalised check; the consumer is not the user |
| MNRE SOP (22 Jun 2026) + vendor deactivation | Complaint → show cause → 1-month deactivation within 30 days; 66 vendors deactivated for backlog (Aug 2026) | Government | The consumer must bring evidence; no measurement tool |
| Inverter OEM apps (Growatt, Solis, etc.) | Free generation view | Bundled | Not independent of the installer; most show kWh, not expected-vs-actual (not verified per brand) |
| SolarSquare | Installs + "GoodZero" 5-yr savings guarantee + per-panel monitoring code (own blog) | US$53 M Series C Jun 2026, valuation US$450-500 M, FY25 op revenue Rs 355 crore (aggregators, snippet); 50,000+ homes | Only its own customers |
| SmartHelio (Swiss/Indian) | IoT + AI diagnostics for solar plants | CHF 250k in 2020 (https://www.pv-magazine-india.com/2020/10/05/indian-led-startup-raises-swiss-funding-for-its-solar-diagnostic-tool); US$5 M round (venturelab, undated, snippet); ~US$6-7 M total (aggregators, conflicting) | Utility/C&I plants, not homes |
| Generic Tuya Wi-Fi solar meters | kWh in/out | Rs 3.2-4.3k | No expected-yield model, no diagnosis, no evidence pack |
| Prescinto, Wattmonk, Loom Solar, Tata Power app | — | NOT SEARCHED | — |

Gap: an installer-independent, irradiance-normalised "is my plant delivering?" verdict with diagnosis (soiling vs shading vs string fault vs grid-outage downtime) and an MNRE-SOP evidence pack. The gap is narrowing. Once the national portal holds daily generation for every new system, MNRE or a state could run expected-vs-actual centrally at no cost to the household. What stays open: legacy systems, distrust of installer-controlled data, physical diagnosis and remediation.

### (d) Solution approaches

1. **Independent solar health logger (hardware + ML).** AC CT on the inverter output, grid-presence/voltage sense (anti-islanding downtime during outages is a real cause of low output, per the Varanasi vendor in Mongabay, R1), ESP32. Expected yield from free satellite/forecast irradiance (Open-Meteo or NASA POWER) + pvlib with roof tilt/azimuth. Daily verdict + fault class + evidence pack (timestamps, geo-tagged photos) in MNRE SOP format. First customer: households in UP districts with vendor complaints, sold through a cleaning/O&M crew. Unit economics (assumptions): BOM Rs 1,200, sell Rs 2,500, Rs 50/month alerts.
2. **Vision inspection (hardware + CV).** Phone photo, plus an optional thermal module (FLIR Lepton class) on a pole or drone: soiling %, hot spots, cracked or shattered modules (CEEW: "28% of the panels found to be damaged"). Sold as a Rs 300-500 inspection by gig cleaning crews; the report is the SOP evidence.
3. **Portal analytics for state nodal agencies (data only).** If states get the M2M/National Portal feed, rank vendors by irradiance-normalised underperformance to target SOP enforcement (UPNEDA already blacklists vendors, R1). Buyer: state agency/discom. Depends on data access.

Pick: **1, with 2 as the upsell.** It is the only route that does not depend on government data access, and it uses the hardware team. Approach 3 is the scale route if the portal opens.

### (e) Regulatory and safety gates

- Not a billing meter: net-metering settlement uses discom bidirectional meters, and Odisha accepts M2M inverter data as the generation meter. An independent logger has evidentiary, not settlement, value.
- MNRE OM 17 Aug 2026 data localisation applies to inverter OEMs. A third-party logger storing data abroad would be out of step with the policy direction; host in India.
- Electrical work on the AC side needs a licensed electrician; avoid the DC side.
- DPDP: household generation and consumption data.
- Blocks the demo: none. Blocks the business: willingness to pay and data access, not certification.

### (f) Overnight wedge

- Daylight constraint: the event runs 6 pm to noon, so only ~5 hours of sun after a ~7 am sunrise (approximate, not checked). Build and calibrate overnight; collect data 7-11:30 am.
- Build: 20-50 W panel + resistive load or small MPPT + INA226 DC logger (an SCT-013 if a small grid-tie inverter is available), ESP32, BH1750/pyranometer-proxy for local reference, pvlib clear-sky + Open-Meteo hourly irradiance for Sonipat, dashboard + PDF evidence pack.
- Tests (numbers):
  1. Clean-panel expected vs measured energy error % over the morning.
  2. Induced faults: 25% cloth shading, talc "soiling" layer, one of two panels disconnected → detection rate and minutes-to-flag.
  3. Grid-outage vs panel-fault classification on a simulated load cut.
- Deep Tech Thesis line: India adds ~5 lakh rooftops a month and the only generation data belongs to the seller. CEEW measured 35-60% recoverable energy in Delhi systems. An installer-independent witness that normalises for sunlight turns "my bill didn't fall" into an actionable SOP complaint.

### (g) Verdict

Real: yes, but the loud public pain is bills, net metering and subsidy delays. Low generation is real (CEEW field data) but less voiced. Unsolved: shrinking. M2M monitoring and the 17 Aug 2026 data OM put daily generation on a national portal, SolarSquare guarantees savings for its customers, and Rs 3-4k Wi-Fi meters exist. Sellable: unproven willingness to pay against a free inverter app. Buildable overnight: yes, with a daylight squeeze. Scores: proof 4, market 3, feasibility 3, unsolved gap 2, deep-tech 3, risk 3.

Three unknowns for Round 3:
1. Will MNRE or states open National Portal generation data to consumers or third parties? If yes, the device is unnecessary and analytics become possible; if no, the reverse.
2. What is the real underperformance distribution of PM Surya Ghar systems? CEEW is n=61, Delhi, pre-scheme. Look for an RTI or discom study.
3. Will households or O&M crews pay Rs 2-3k when the inverter app is free? Is outage-driven anti-islanding downtime, not panels, the main cause of low output in UP?

---

## Problem: E3 EV two-wheeler charging fires and the apartment-charging impasse, plus unknowable battery health

### (a) Proof dossier

Independent items I can stand behind: 14 (YouTube from 9 channels + LiveLaw + Karnataka Council reply + 3 from Round 1; Round 1's ThePrint 1 Jun 2026, Business Today 26 May 2026 and FPJ 30 Mar 2026 still stand).

- https://www.youtube.com/watch?v=VqOrCc6KlwM — 15 Jul 2026 — 6,251 views (YT page, 3 Nov 2026) — CNBC-TV18, "Noida Fire: EV Battery Blast Kills 2, Traps Residents"; also https://www.youtube.com/watch?v=I1LYXr5Lqik — 16 Jul 2026 — 8,945 views, 15 comments — Indian Express Hindi, "चार्ज हो रही स्कूटी से लगी आग". **Resolves Round 1's conflict: two dead in the Noida Mamura fire** (also TV9 Bharatvarsh live stream, same date, title "2 की मौत").
- https://www.youtube.com/watch?v=UCfQHVumJS4 — 18 Mar 2026 — 63,626 views, 178 comments (YT page, 3 Nov 2026) — The Hindu, "Eight killed in Indore house fire after EV blast; Govt. orders probe"; https://www.youtube.com/watch?v=ZChfwW_rvsY — 18 Mar 2026 — 30,695 views — News Nation, "Indore EV Car Blast | LPG | Digital Lock". **Flag on Round 1: the Indore vehicle was an electric car, with LPG cylinders and a digital lock worsening the toll. It is an EV home-charging death, not a two-wheeler case.**
- https://www.youtube.com/watch?v=JGXVIo19VsE — 18 Mar 2026 — 4,305 views — News Nation, "Delhi Fire Kills At Least 7 Near Palam Metro Station | EV charging blast" (cause per title only; not verified).
- https://www.youtube.com/watch?v=OE__37LSF2c — 1 Nov 2026 — 1,36,288 views, 41 comments, 2,171 likes (YT page, 3 Nov 2026) — "United Electric Bike Fire Incident: Why this happened and how to prevent".
- https://www.youtube.com/watch?v=IoacUzWN1Ko — 2 May 2022 — 2,46,411 views (YT page, 3 Nov 2026) — BBC News Hindi, why e-scooters catch fire (the 2022 wave).
- https://www.youtube.com/watch?v=4WqNn0q4ZsY — 2 Aug 2026 — 22,112 views, 40 comments (YT page, 3 Nov 2026) — News Nation, "Can Housing Society Stop EV Charger Installation? | Supreme Court Case".
- https://www.youtube.com/watch?v=0TOtLgCXBP4 — 23 May 2026 — 13,813 views, 24 comments — Throttle EV India, "Chargers Removed from Society Basements!".
- https://www.youtube.com/watch?v=rXFa0gYibf8 — 27 Jul 2025 — 9,11,927 views, 1.2K comments (YT page, 3 Nov 2026) — My Motor Talks, "EV Scooter Problems Nobody Will Tell You" (battery and after-sales; not fire-specific).
- https://www.youtube.com/watch?v=B-3Xsz8Dpbw — 22 Aug 2026 — 91,852 views, 97 comments — "EV Scooter की Battery कितने साल चलेगी? Battery Replacement Cost का पूरा सच" (battery-health anxiety).
- https://www.livelaw.in/top-stories/after-housing-society-refuses-permission-for-ev-charger-installation-owner-moves-supreme-court-to-enforce-power-ministry-guidelines-524393 — 24 Feb 2026 — LiveLaw (snippet) — SC notice on the PIL by a Nirala Estate (Greater Noida) resident seeking enforcement of MoP 2024 society-charging guidelines; next hearing (22 May) deferred, no ruling (ThePrint, R1).
- Karnataka Legislative Council reply (Commerce & Industries Minister): 83 EV fires Jan 2020-Nov 2024 — 3 (2021), 9 (2022), 28 (2023), 36 (2024); 65 attributed to "power leakage", 13 to battery explosions, 5 accidental; most were e2Ws; Okinawa, Ola, Ather named most — https://convergenceindia.org/industry-news/mobility/karnataka-records-83-ev-fire-incidents-in-4-years-okinawa-and-ola-top-the-list-118861 (Dec 2024, snippet; fetch failed twice).

Strongest hard numbers:
1. Karnataka 83 EV fires, rising from 3 to 36 a year (2021-2024), 65 of 83 electrical "power leakage" (above, snippet).
2. e2W registrations FY26: 14,01,861 (+21.8% from 11,50,815 in FY25), Vahan via Business Standard — https://www.business-standard.com/industry/auto/ev-sales-surge-in-fy26-on-strong-q4-push-vahan-data-126040101172_1.html (1 Apr 2026, snippet); Jan-Sep 2026: 15.61 lakh (https://www.angelone.in/news/economy/electric-two-wheeler-sales-cross-15-lakh-in-nine-months-of-2026, snippet).
3. Noida Mamura: 2 dead, 100+ rescued (Jul 2026); Gurugram DLF Ultima: 75 basement chargers removed (ThePrint 1 Jun 2026, R1).
- National fire count: NOT FOUND. A secondary site cites eDAR at 9 EV fires in 2025 (https://www.91wheels.com/buyers-guide/are-electric-cars-safe, snippet). That is clearly an undercount, since Karnataka alone recorded 36 in 2024; eDAR is a road-accident database.

Final tier: **A (weakest of the three)**. More than 5 independent items and hard numbers, but engagement on fire-specific items is in the thousands to tens of thousands of views, not lakhs; the large-view videos are about battery cost and general EV problems. The apartment-charging impasse is better evidenced than fires.

Reddit sweep (E3): see end-of-file block.

### (b) Market size

- Vehicles: ≥25.5 lakh e2Ws sold in FY25 + FY26 alone (11.51 + 14.02 lakh; my arithmetic); on-road parc NOT FOUND (no Vahan cumulative figure surfaced).
- Societies: 1.96 lakh cooperative housing societies (https://insights.dataful.in/articles/how-indias-cooperatives-are-distributed-across-states-and-sectors, Aug 2026, snippet); Maharashtra alone 1,26,544 (snippet). This excludes RWAs/apartment associations registered under other laws (no national count found).
- Regulatory pull: Haryana's amended building code (5 Jun 2026) requires 1 charger per 5 parking slots in group housing, cooperative and RWA complexes (the headline frames it as new and renovated complexes), and lets owners in existing complexes install in allotted slots with Fire Department + discom certification — https://www.autocarindia.com/car-news/haryana-mandates-ev-chargers-in-new-and-renovated-residential-complexes-439920 (9 Jun 2026).
- Price: Rs 6,000 per bay monitor + Rs 100/bay/month (assumption; reference: Bolt.Earth smart sockets Rs 4,999-5,499 without thermal or gas sensing, see (c)). Bays per society: 10 (assumption; DLF Ultima alone had 75 chargers).
- **TAM: 1.96 lakh societies × 10 bays × Rs 6,000 = Rs 1,176 crore one-time** (my arithmetic).
- **SAM: 20% of societies (urban gated, basement/stilt parking in NCR, MMR, Pune, Bengaluru, Hyderabad; assumption) = 39,200 × 10 × Rs 6,000 = Rs 235 crore + monitoring 3.92 lakh bays × Rs 1,200/yr = Rs 47 crore/yr** (my arithmetic).
- Used-battery SoH certificate: no national standard (https://vahanbazaar.in/news/used-ev-battery-health-risk-2026, 2026, snippet); resale volume NOT FOUND, so not sized.
- Insurers as payers: weak. Business Standard (17 May 2022, pressreader snippet) said EV fire claims were "in single digits"; disputes turn on electrical-fault exclusions (https://www.outlookmoney.com/personal-finance/why-many-two-wheeler-fire-claims-get-rejected-and-how-to-avoid-it, snippet).
- Who pays today: RWAs pay nothing for monitoring; they refuse or remove chargers (ThePrint), or fine domestic-connection charging (Rs 25,000, R1). Owners pay Rs 5-5.5k for a smart socket.

### (c) Competitive map

| Who | What | Funding / status | What it does NOT do |
|---|---|---|---|
| Bolt.Earth Lite / Pro smart sockets | 3.3 kW socket; MCB, over/under-voltage, auto cut-off, app-authenticated sessions; LEVAC variant ARAI-certified | Rs 4,999 / Rs 5,499 (https://bolt.earth/blog/budget-ev-charging-setup-for-homes-and-apartments-under-%e2%82%b930000-options, snippet). Alive | No plug/cable temperature, arc/loose-contact, pack temperature or gas sensing; no fire-NOC log |
| Kazam, Charzer | Society charging | NOT SEARCHED (query returned only Bolt.Earth) | — |
| OEM BMS under AIS-156 Amd 3 (Phase 1 1 Dec 2022, Phase 2 31 Mar 2023) | Overcharge/over-temperature protection, multiple in-pack sensors, thermal-propagation test, "audio-visual warning ahead of a thermal event", IPX7; charger earth-leakage detection | Mandatory — https://www.meraev.com/blog/electric-scooter-battery-safety-norms-india-explained (27 Jul 2026) | "The rules cannot follow the scooter home": nothing on socket, wiring or charging location; warning goes to a rider who is asleep |
| MakerMax | M201 battery tester + pressure/temperature/gas sensors in battery zones, 3-level Wi-Fi alarm, for e2Ws | https://www.outlookbusiness.com/amp/story/news/makermax-develops-testing-devices-algorithms-to-tackle-battery-fires-news-189643 (1 Apr 2022, upd. Jul 2023); funding, customers, status not found → likely stalled | Not society-bay focused; no evidence of deployment |
| iRasus (Gurugram), Flowatt (Rs 2.2 crore pre-seed), The Energy Company (US$2 M) | Fleet battery analytics / predictive maintenance | https://www.saurenergy.com/ev-storage/deep-tech-analytics-platform-irasus-raises-seed-funding (snippet); https://www.autocarpro.in/news/flowatt-secures-₹22-crore-pre-seed-funding-led-by-pedalstart-129293 (snippet) | B2B fleets with BMS data access; not retrofit, not residential |
| Honeywell Li-ion Tamer | Off-gas detection for BESS | 6.4 min warning before thermal runaway in DNV-GL tests; stopping charge on alert avoided runaway; H2 seen only at runaway — https://www.honeywell.com/us/en/insights/articles/national-lab-testing-demonstrates-value-in-early-detection (vendor-reported) | Priced and validated for enclosed BESS racks, not an open parking bay |
| Battery health / used EVs | Ola transferable warranty, replacement below 70% SoH (MeraEV, snippet); Electric One + iPower "500 battery health centres" announced 2022 (https://emobilityplus.com/2022/05/13/electric-one-partners-with-ipower-batteries-to-establish-ev-battery-replacement-and-health-centers-in-india/amp/), status unknown | — | No independent SoH certificate for resale |
| Government | Haryana code (Jun 2026; Fire Dept to draft detailed EV-charging fire rules); BIS NBC draft (Oct 2025) restricting basement charging, final status unconfirmed (https://www.businesstoday.in/auto/story/buying-an-ev-check-basement-charging-rules-first-528040-2026-04-29); "NBCS 2026" requiring rate-of-rise heat sensors and compartmentation in EV charging areas, per a vendor blog only (https://elion.co.in/nbcs-2026-vs-nbc-2016-fire-safety/, 1 Jun 2026, snippet, unverified, advisory) | — | No device spec, no certification route for retrofit monitors |

Gap: no product watches a residential charging bay, covering the socket/plug/cable (the "power leakage" class that dominates Karnataka's tally) and the pack (temperature + gas), cuts power, and produces a log a fire officer or RWA can accept. MakerMax tried the pack-sensor idea in 2022 and left no trace.

### (d) Solution approaches

1. **Bay safety monitor (hardware + ML).** Smart socket with current/voltage signature analysis for arcing and loose contacts (high-frequency current features), a thermistor at the plug terminals, an overhead IR thermopile array (MLX90640) over the parked scooter's battery zone, VOC/CO/H2 gas sensors, relay cut-off, local siren + guard-room and app alert, and a signed event log for the fire NOC. First customer: a Gurugram or Noida society that removed basement chargers (DLF Ultima); pitch "restore chargers under monitoring". Unit economics (assumptions): BOM Rs 2,500-3,500, sell Rs 6,000 + Rs 100/month. Moat: near-miss dataset across bays, fire-department acceptance, and certification once Haryana's rules are written.
2. **Charging-curve health and anomaly (ML on approach 1's data).** The socket sees each session's input power vs time. Track energy per full charge (capacity proxy), CV-tail shape and post-charge standby draw to flag degradation or abnormal self-discharge (a grown-in internal short shows up as rising charge energy at constant use; the literature shows detection on charge-phase voltage timing — https://www.energy-proceedings.org/wp-content/uploads/icae2024/1728100405.pdf, 2024, snippet — and notes field shorts develop slowly, many cycles before runaway: https://ecs.confex.com/ecs/imlb2016/webprogram/Paper77331.html, 2016, withdrawn abstract, snippet). Output: a "battery health report" for resale.
3. **Electrolyte-vapour sensing (bio/chem + hardware, post-event).** The wet-lab members characterise low-cost MOX/chemiresistive sensor response to electrolyte solvent vapours (DMC/EMC) vs household confounders (perfume, petrol, cooking) in a fume hood, to build a selective venting signature. Not for the overnight hall.

Pick: **1, with 2 as its software layer.** The Karnataka cause split (65/83 electrical) says the socket/cable side may prevent more fires than gas sensing. Approach 1 covers both and is what an RWA or fire officer can understand.

### (e) Regulatory and safety gates

- Product side: socket-outlet and RCD standards (IS 1293 / IS 12640 family) and IS 17017 for EV charging equipment apply to a socket device (not verified which are compulsory under BIS CRS); WPC for radio.
- Building side: state fire department and discom certification for chargers in allotted bays (Haryana, Jun 2026); the BIS NBC basement draft (status unconfirmed). Whether a monitor substitutes for sprinklers or compartmentation is the commercial question, and no rule says so yet.
- Liability: product liability under the Consumer Protection Act 2019 if a monitored bay burns. Needs insurance, plus wording as "monitoring", not "fire prevention".
- AIS-156 is vehicle-side; no change needed.
- DPDP: minimal (bay-level, not personal).
- Blocks the demo: nothing, provided no real lithium cell is abused. Blocks the business: certification route and fire-department acceptance.

### (f) Overnight wedge

- Safety rule: no abuse of real lithium cells. All fault data comes from simulators or public datasets.
- Build: ESP32 + relay + 12-24 V low-voltage rig (no mains in the demo). Dummy "pack" = aluminium block + 50 W heater pad + thermistors; MLX90640 IR array overhead; BME688/SGP30 gas sensor; a deliberately loosened screw terminal on a 12 V, 10 A resistive load to reproduce contact heating; siren + app.
- Vapour stand-in: a few drops of isopropyl alcohol on a cotton bud held 10-30 cm from the sensor, in a ventilated area with no ignition source, as a proxy for solvent venting.
- Battery-health piece: log CC-CV curves from a single 18650 charged within spec by a TP4056 module (normal charging only, attended, in a fire-safe bag), plus train/test SoH estimation on public datasets (NASA PCoE / CALCE; not re-verified this round).
- Tests (numbers):
  1. Detection latency: heater ramp ~2 °C/min → seconds to alarm and to relay cut.
  2. Loose-contact detection: terminal temperature rise and time-to-flag.
  3. False alarms over several hours of normal "charging" cycles.
  4. IPA-vapour detection distance and response time.
  5. SoH MAE (%) on held-out dataset cells.
- Deep Tech Thesis line: India sold 14 lakh e2Ws in FY26 and RWAs are pulling chargers because nobody watches a bay at 3 am. A Rs 6k bay monitor that sees the plug, the pack and the air converts a fire-NOC "no" into a monitored "yes".

### (g) Verdict

Real: yes. Deaths in Noida (2W) and Indore (EV car), Karnataka's rising count, chargers removed and a Supreme Court PIL. Unsolved: yes. No bay-level monitor exists; smart sockets stop at voltage cut-off; MakerMax stalled. Sellable: plausible to societies once a fire department names monitoring as a condition. Haryana's pending rules are the swing factor, and insurers are not buyers yet. Buildable overnight: only as a simulation, so the "testing result" proves the plumbing, not real thermal-runaway detection. Scores: proof 4, market 3, feasibility 3, unsolved gap 4, deep-tech 4, risk 4.

Three unknowns for Round 3:
1. Can retrofit gas/IR sensing catch a 2W pack venting in an open bay in time? Li-ion Tamer data is for enclosed BESS. Look for any open-air or parking-garage test (UL, FM Global, BRE) with lead times.
2. Will Haryana's Fire and Emergency Services (or Maharashtra, or the NBC final) require detection or monitoring for basement or bay charging? That decides whether RWAs must buy.
3. What is the cause mix of residential charging fires? Karnataka says 65/83 "power leakage". Get the underlying Fire Services categories; if wiring and socket faults dominate, the cheaper smart-socket path wins.

---

## Reddit sweep results (arctic-shift)

Source: arctic-shift title search, 49 subreddit × keyword queries run 3 Nov 2026. 16 queries failed on the API's rate limit, which other agents were also hitting (r/noida, r/indiasocial, r/uttarpradesh, r/IndiaSpeaks, r/kanpur, r/indore "smart meter"; r/delhi, r/lucknow, r/gurgaon "solar"; r/ElectricVehiclesIndia "RWA", "charging", "basement"). r/ElectricVehiclesIndia "fire", "society" and "battery health" returned 0 posts, which looks like an index gap, not an absence. Scores are captured near posting time and usually understate final counts. Format: date, points, comments.

**Bottom line: Reddit engagement on all three is modest (tens of points, 10-75 comments).** The loud public channel for E1 and E2 is Hindi YouTube and Hindi news. Reddit adds texture, not tier.

E1 (smart meters):
- r/nagpur "MSEDCL smart meter scam" (id 1ue7ac7) — 24 Jun 2026 — 73 pts, 45 comments; same thread series "Part 3 - MSEDCL high bill smart meter scam update - Don't tolerate their ignorance" (1vfev6j) — 4 Aug 2026 — 32 pts, 7 comments (same author likely; count once).
- r/nagpur "Smart Meter" (1s9fqkh) — 1 Apr 2026 — 8 pts, 20 comments; "What is your opinion about smart meter?" (1deqfaa) — 13 Jun 2024 — 28 pts, 15 comments.
- r/mumbai "BEST sent SMS notice for change to Smart Meter. Can we resist?" (1x4xgur) — 13 Oct 2026 — 24 pts, 25 comments (cross-posted to r/legaladviceindia 22 Oct 2026).
- r/lucknow "Billing counter clerk of Lucknow's Rajajipuram Power House assaulted by smart meter company's staff…" (1set5u5) — 7 Apr 2026 — 34 pts, 3 comments; "UPPCL Smart Meter for Solar" (1v39mhf) — 22 Jul 2026 — 4 pts, 15 comments.
- r/india "Used 0 units of electricity. Still got a ₹1239 bill" (1sjjxnx) — 12 Apr 2026 — 0 pts, 11 comments.
- E6 outages: r/gurgaon residents crowd-map outages in threads: "Light's out in sector 40 since 8pm. Which other sectors are also facing power cut?" (1tknkye) — 22 May 2026 — 9 pts, 62 comments; "Power cut 🥵" (1uj051x) — 29 Jun 2026 — 61 comments; "Power Cut" (1vuucdw) — 21 Aug 2026 — 44 comments; "Power cut attendance. Sector 46" (1tohem8) — 26 May 2026 — 36 comments; "Where to check for power cut schedule in Gurgaon?" (1tkmjem) — 22 May 2026 — 10 comments. This is direct evidence that residents want a shared outage map and build one by hand in comments. r/india "Lighting a candle because of power cut…WFH from rural Bihar" (np6u58) — 31 May 2021 — 1,116 pts, 105 comments.

E2 (rooftop solar):
- r/pune "MSEDCL wants to add extra tarriffs on solar energy…How do we protest" (1isv0ij) — 19 Feb 2025 — 171 pts, 43 comments.
- r/bangalore "Bangalore homeowners with solar rooftops — is it actually worth it?" (1rqi1y9) — 11 Mar 2026 — 44 pts, 41 comments.
- r/bangalore "Installed Solar roof top recently. But how do I get the bill with all the details from BESCOM?" (1m1chek) — 16 Jul 2025 — 15 pts, 35 comments (net-meter bill opacity).
- r/bangalore "BESCOM Net-Metering Users — How are exported solar units settled?" (1pete89) — 5 Dec 2025 — 12 comments; r/hyderabad "New Solar connection export queries" (1xdba07) — 23 Oct 2026 — 15 comments; r/bangalore "No gruha jyoti for solar rooftop users?" (1i2hrr5) — 16 Jan 2025 — 11 comments.
- r/hyderabad "SolarSquare quoted me 3.35L for a 4.8kW system…Is this a rip-off?" (1uzamlk) — 17 Jul 2026 — 22 pts, 17 comments.
- r/pune "I want to start a solar cleaning service" (1rnveqq) — 8 Mar 2026 — 20 comments (O&M supply side).
- Reading: Reddit solar talk is pre-purchase ROI and net-meter billing opacity. I found no Reddit thread about measured generation shortfall, which supports the view in E2 (g) that shortfall is under-voiced.

E3 (EV charging / battery):
- r/bangalore "After RWA snub, EV owner hauls e-scooter to 5th floor kitchen for charging" (pko3iy) — 9 Sep 2021 — 275 pts, 74 comments. The impasse pushes charging indoors, the exact fire scenario.
- r/bangalore "RWA is neither installing a common EV charging point nor allowing me to install my personal charger" (1gqchro) — 13 Nov 2024 — 89 pts, 33 comments.
- r/india "Ola S1 pro electric scooter catches fire in Pune" (tosuiy) — 26 Mar 2022 — 88 pts, 23 comments.
- Battery-health unknowability, r/olaelectric: "Ola Electric nightmare: 40+ days waiting for RSA…dead battery, and a ₹65,000 repair" (1x85vmu) — 17 Oct 2026 — 18 comments; "Ola S1 Pro Gen1 battery suddenly dropping from 35–45% to 0%" (1rq28by) — 10 Mar 2026 — 21 comments; "3.5-year-old Ola S1 (41k kms) battery suddenly dropping from 80% to 1%. Ola quoting full replacement. Repair or Scrap?" (1v043r6) — 18 Jul 2026 — 14 comments; "Overnight battery drain on new Ola S1 X" (1uhnvb2) — 28 Jun 2026 — 26 comments.
- r/ElectricVehiclesIndia: NOT FOUND (index returned 0 or timed out).

---

## NOT SEARCHED
- E1: CGRF/Ombudsman orders citing consumer-side logs; CEA metering regulation clause on consumer-owned meters; DLMS optical-port access without discom keys; UP expert-committee findings; NCH electricity-sector share (search returned only 2018-19 data); Sense/Emporia India availability; Zenatix (commercial buildings, out of scope).
- E1/E6: NFMS public feeder data (one search, nothing found); current ESMI status beyond 2023.
- E2: Prescinto, Wattmonk, Loom Solar, Tata Power app features and prices; PM Surya Ghar subsidy-pending national figure; the late-July 40.07 lakh figure's primary page; Sonipat sunrise time.
- E3: Kazam and Charzer features; e2W on-road parc; national 2025-26 fire count (none exists that I found); IRDAI EV claim data; Battery Smart/Lohum status; Li-ion Tamer price.
- Reddit: see sweep block; LocalCircles surveys on any of the three (not searched this round).

Searches used: 39
