## Appendix I. Biology deep dive (new research, 14 Nov)

This appendix is the biology underneath the step loop, for the team's biology student, who will turn it into protocol rules: how each drug lowers pressure, who responds to which, how fast a step works, how much readings move on their own, why each safety check exists, which lab tests matter, and how to tell whether a medicine was taken. Chapter 2.7 tells it in short; chapter 4.9 lists the product features.

### I1. How to read this appendix

- **New research.** Five notes written early on 14 Nov 2026, after the rest of this document: who responds to what (D4-01), how fast a dose change works (D4-02), natural variation and how many readings (D4-03), why each safety check exists (D4-04), and biomarkers and adherence signals (D4-05). Their fact IDs start with D4.
- **Claims checks.** Three checks re-opened the sources by a second route (D4-06, D4-07, D4-08). A corrected fact carries the corrected value and "(corrected in the claims check)"; a confirmed fact whose use the check limited carries "(claims check)"; where a check found two values, both are given. Appendix J gives every verdict.
- **What was opened.** Mostly primary sources: US drug labels; NICE, KDIGO (the international kidney guideline group), UK Kidney Association (UKKA), WHO 2021, ESH 2023 and ISH 2020 texts; Indian state protocol sheets (Punjab, Madhya Pradesh, Telangana, Maharashtra) and Nigeria's sheet; India's 2025 essential diagnostics list; papers through Europe PMC. Many trials were read as abstracts only. Facts seen only in a search result are marked "(search summary only)", including every Indian test price. The Gujarat sheet was not reopened in this round.
- **India data are thin.** No Indian rotation trial of drug choice, no Indian drug-assay study of adherence, no Indian data on how much one person's home readings vary, and Indian seasonal data come from readings by nurses or investigators, not home cuffs. Each number below says where it was measured.
- **Not medical advice.** Medicines and doses appear only as written in a label, guideline, protocol sheet or trial. Every suggestion (I9, I10) is for the team and a supervising clinician to decide; the state protocol stays as written.

### I2. How the protocol's drugs lower pressure

The ladder uses three drug families, and each pulls a different lever.

| Drug | Lever | What happens in the body | Half-life |
|---|---|---|---|
| Amlodipine (calcium-channel blocker) | Muscle of the arterioles, the smallest arteries | It "inhibits the transmembrane influx of calcium ions" into vessel muscle more than heart muscle, so arterioles relax and resistance falls; slow binding gives "a gradual onset of effect"; no significant heart-rate change on daily dosing; GFR (glomerular filtration rate, how much blood the kidneys filter) rises [D4-01-F17] | 30-50 hours [D4-02-F01] |
| Telmisartan (ARB: angiotensin II receptor blocker) | The angiotensin hormone system | Blocks angiotensin II at the AT1 receptor, so blocks vessel tightening and aldosterone release; renin and angiotensin II rise but "do not overcome the effect"; 80 mg blocked the response to infused angiotensin II about 90% at peak and 40% at 24 hours [D4-01-F20] | About 24 hours, cleared in bile [D4-02-F05] |
| Losartan (ARB, Nigeria's sheet) | Same | About 14% is turned by liver enzymes (CYP2C9, CYP3A4) into a metabolite 10-40 times more potent; renin doubles to triples [D4-01-F25] | 2 hours; metabolite 6-9 [D4-01-F25] |
| Chlorthalidone (thiazide-like diuretic) | The kidney's handling of salt | More sodium and chloride lost in urine (distal convoluted tubule); lower plasma volume and cardiac output; "sodium and water depletion appear to provide a basis for its antihypertensive effect"; extra urine for up to 72 hours [D4-01-F23] | About 40-60 hours [D4-01-F23] |
| Hydrochlorothiazide (thiazide) | Same | Distal tubule; shrinking plasma volume raises renin, aldosterone and potassium loss; mechanism "not fully understood"; extra urine for 6-12 hours [D4-01-F24] | 5.6-14.8 hours [D4-02-F11] |

Three mechanisms matter later. Aldosterone drives the kidney's collecting duct to pass potassium, so an ARB tends to raise potassium [D4-04-F06, D4-04-F26], although telmisartan up to 80 mg did not change plasma aldosterone in healthy volunteers [D4-05-F18]. Angiotensin II keeps the efferent arteriole (the vessel leaving each glomerulus, the kidney's filter) tight and so holds up filtration; blocking it lowers filtration pressure and creatinine rises a little (I6) [D4-04-F52, D4-04-F26]. And a thiazide's effect changes over weeks: in 11 patients on hydrochlorothiazide 50 mg twice daily (a small 1978 Western study), the 48-hour fall came with lower cardiac output and plasma volume and a reflex rise in resistance; by 6-8 weeks resistance had fallen and cardiac output recovered while the volumes stayed down (claims check) [D4-02-F39].

The families add up because each provokes a reaction the next one blocks. A thiazide shrinks volume and raises renin and aldosterone; an ARB blocks exactly that, and adding telmisartan to hydrochlorothiazide gave an extra fall "similar in magnitude" to telmisartan alone [D4-01-F22]. Amlodipine's widening of the arterioles is thought to raise capillary pressure, so fluid leaks into the ankles [D4-04-F65]; adding an ARB or ACE inhibitor cut that swelling by 38%, for a reason the sources checked do not state [D4-04-F66]. Across 42 factorial trials (10,968 people) the effects of two families simply added (observed against expected 1.01) [D4-01-F09].

**For the loop (OUR VIEW).** Steps 3 and 5 add a new lever; steps 2 and 4 push the same lever harder. The mechanisms predict that the new levers do more, and I3 shows that they do.

### I3. Who responds to what

#### Two kinds of high pressure

The Cambridge rotation trial proposed that some people's pressure is driven mainly by renin and angiotensin, and others' by salt and volume [D4-01-F04]. Renin-angiotensin blockers work when pressure is renin-driven, diuretics when it is volume-driven (low renin), and calcium blockers across renin levels [D4-01-F06]. In 1,031 US men, hydrochlorothiazide worked in 82%, 78% and 14% at low, medium and high renin, captopril (an ACE inhibitor) in 51%, 83% and 100%, and diltiazem (a calcium blocker) in 83%, 82% and 83%; yet age and race predicted response better than renin did [D4-01-F06]. Salt suppresses renin: in 391 salt-sensitive US patients on alternating high and low salt, the calcium blocker isradipine lost less effect on high salt than enalapril (high-minus-low salt difference -3.6/-1.6 to -8.1/-5.3 against -9.0/-5.3 to -11.8/-7.0 mmHg) [D4-01-F13].

#### Rotation trials: how much better is each person's best drug

| Trial | Who, where, how long | Finding |
|---|---|---|
| PHYSIC [D4-01-F01, D4-01-F02, D4-01-F03] | Sweden, 280 randomised, 270 analysed, mean age 64. Lisinopril 20 mg, candesartan 16 mg, hydrochlorothiazide 25 mg and amlodipine 10 mg in random order, two repeated; each period a 1-week washout, 2 weeks of dose increase and at least 4 weeks at full dose; ambulatory (24-hour monitor) readings | Each person's best drug gave 4.4 mmHg lower systolic pressure than a fixed choice, 3.1 against lisinopril; both are model estimates (claims check). Real differences lay between a renin-angiotensin blocker and amlodipine or the thiazide; large differences within those pairs were excluded, which is not the same as none. Authors: about twice the gain of doubling a dose |
| Cambridge [D4-01-F04] | 56 young untreated UK patients, a month each on four families; 36 finished; 1999 | Control on one drug rose from 39% on the first drug to 73% on each person's best (p=0.0001); ACE-inhibitor and beta-blocker responses went together, as did calcium-blocker and diuretic responses |
| GENRES [D4-01-F32] | 208 Finnish men, four drugs for 4 weeks each with placebo gaps | The same split; amlodipine and thiazide responses grew with age, with higher placebo pressure and with less night-time dipping |

A counterweight: across 7 placebo-controlled ACE-inhibitor trials (28,281 people, change at 3 months, clinic readings), only 3% of the apparent spread in individual systolic response was real [D4-03-F55]. OUR VIEW: PHYSIC repeated each drug, so it could see a modest real difference between families; one patient's single before-and-after change mostly shows noise.

#### Traits that predict response

| Trait | Evidence |
|---|---|
| Age | Amlodipine works better in older patients, "perhaps because of greater baseline systolic pressure" [D4-01-F18]; in an open US trial (1,084 patients, 16 weeks, no placebo) 91.5% of those 65 or over reached goal against 84.1% [D4-01-F39]; telmisartan's effect is "not influenced by patient age, gender, weight, or body mass index" [D4-01-F21] |
| Sex | Same trial: 91.4% of women against 83.0% of men [D4-01-F39]; amlodipine ankle swelling 14.6% in women against 5.6% in men, all doses pooled [D4-01-F19]; the benefit of each mmHg is the same in both sexes (51 trials, 358,636 people) [D4-01-F38] |
| Salt (India data) | North-east India, 374 volunteers: 47.6% of people with high pressure were salt-sensitive, and an extra-salt habit doubled the odds (OR 1.99) [D4-01-F47]. UK Bangladeshi kidney patients (56, 6 months): low-salt advice lowered 24-hour pressure 8/2 mmHg on top of drugs [D4-01-F48] |
| African ancestry | Calcium blockers and diuretics beat ACE inhibitors and beta-blockers (35 trials, 25,540 people) [D4-01-F11]; CREOLE (728 patients, six sub-Saharan countries, 6 months): pairs with amlodipine lowered 24-hour systolic pressure about 3 mmHg more than perindopril plus thiazide [D4-01-F12]; telmisartan is "noticeably less" effective in Black patients [D4-01-F21] |
| South Asian ancestry | 16 low-quality trials with 1,719 patients, mostly in India, median 8 weeks: "no significant difference" between families [D4-01-F11]. ASCOT (UK and Nordic, 132 South Asians): adding perindopril to amlodipine changed systolic pressure by -6.2 mmHg against -1.7 in white patients (interaction P=0.004) [D4-01-F07] |
| Body weight | No usable rule for the protocol drugs [D4-01-F41, D4-01-F42] |

Guidelines use little of this. NICE alone has an age and ancestry rule (an ACE inhibitor or ARB first for adults with type 2 diabetes, or under 55 and not of Black African or African-Caribbean origin; a calcium blocker first at 55 or over, or of Black African or African-Caribbean origin, without diabetes), and has no South Asian rule [D4-01-F15]; its committee found "No evidence for step 2 or step 3 treatment was identified that was relevant to determining the best sequence" [D4-01-F16]. WHO 2021 lets any of three families start (search summary only) [D4-01-F43]. India's IHCI starts amlodipine except in kidney disease, with procurement within budget a stated reason [D4-01-F46]; state documents say amlodipine needs no metabolic monitoring and can be given to women of childbearing age (search summary only) [D4-01-F46].

**Gene tests are not usable.** In GENRES's gene study (228 Finnish men) one signal reached genome-wide significance and did not replicate [D4-01-F33]; polygenic scores predicted nothing [D4-01-F34]; the best single variant (YEATS4) added 3.4/2.5 mmHg of thiazide response in 746 US patients and is untested in South Asians [D4-01-F35]. A 2025 review says clinical use "remains challenging", each common variant is worth about 1 mmHg, and gene-based dosing advice exists for metoprolol but not for amlodipine, telmisartan or the thiazides [D4-01-F36]; South Asian gene claims are hypotheses [D4-01-F37].

#### Raising a dose against adding a drug

Doubling a dose gave about one fifth (0.22) of the extra fall that adding a second family gave (42 factorial trials, 10,968 people) [D4-01-F09]. Across 484 placebo-controlled trials (104,176 people, mean 8.6 weeks), a standard-dose drug lowered systolic pressure 8.7 mmHg, each doubling added 1.5, and two drugs gave 14.9 [D4-01-F10]. Half the maximum ARB dose gives 80% of the maximum fall [D4-01-F52]; chlorthalidone 12.5-75 mg showed no dose dependence (low-quality evidence) [D4-01-F26]; thiazide and calcium-blocker side effects rise steeply with dose, while ARBs caused no excess symptoms [D4-01-F08]. In TRIUMPH (Sri Lanka, 700 patients, 6 months, open-label, against usual care), one low-dose pill of telmisartan 20 mg, amlodipine 2.5 mg and chlorthalidone 12.5 mg brought 70% to target against 55%, with dizziness or fainting in 5.2% against 2.8% [D4-01-F28].

#### What each Gujarat step adds

From the US telmisartan-amlodipine label (8-week trials, place not stated):

| Step | Extra systolic fall | Cost |
|---|---|---|
| 2. Amlodipine 5 to 10 mg | 5.3 mmHg (OUR ARITHMETIC: 18.2 - 12.9, placebo-subtracted, 1,461 patients) [D4-01-F49] | Ankle swelling from 3.0% to 10.8% [D4-01-F19] |
| 3. Add telmisartan 40 mg | 4.0 mmHg (OUR ARITHMETIC: 22.2 - 18.2) [D4-01-F49]; 3.7 beyond staying on amlodipine 10 mg, in 947 patients not controlled on it [D4-01-F50] | Kidney and potassium checks (I6) |
| 4. Telmisartan 40 to 80 mg | 1.7 mmHg (OUR ARITHMETIC: 23.9 - 22.2) [D4-01-F49]; 0.2 in the same 947 (OUR ARITHMETIC: 11.3 - 11.1, not formally tested) [D4-01-F50]; -1 to +4 from the telmisartan label's ranges (OUR ARITHMETIC, claims check) [D4-01-F21] | Four lab tests on the sheet |
| 5. Add chlorthalidone 12.5 mg | About 6.2 mmHg when hydrochlorothiazide 25 mg was added to amlodipine plus valsartan (another ARB) in 2,271 patients starting at 170/107, with no placebo arm [D4-01-F53] | Potassium, sodium, uric acid, sugar (I6) |

In 1,097 patients not controlled on amlodipine 5 mg, adding telmisartan 40 mg beat raising amlodipine to 10 mg by 2.4/1.4 mmHg, with swelling in 4.3% against 27.2% [D4-01-F51]. In India's programme, step 2 lifted clinic control from 70% to 75% in Punjab (amlodipine 10 mg) and from 76% to 81% in Maharashtra (add telmisartan 40 mg) [D4-01-F45]. These are levels at the latest visit after a median 12 months, among patients who returned, with 16.5% and 31.5% already under 140/90 at registration; they are not the effect of one 30-day step (claims check) [D4-02-F17].

**For the loop (OUR VIEW).** Adding or switching a family is where the millimetres are; step 4 buys almost nothing for four lab tests. No family stands out in South Asians, so the fixed order is defensible; age, sex and salt habit are the cheap traits to record; gene and renin tests are not ready.

### I4. How fast a dose change works

A step can be judged only once the new dose has had its full effect. Two clocks matter: the blood level, which is steady after 4-5 half-lives (about 94-97% of the steady state; OUR ARITHMETIC, as in the note) [D4-02-F01], and the body's response, which can lag behind it.

| Drug | Steady level | Time to (near) full effect | Label step interval |
|---|---|---|---|
| Amlodipine | 7-8 days [D4-02-F01] | Not stated; slow binding builds the effect over days [D4-02-F02, D4-02-F03] | "In general, wait 7 to 14 days between titration steps" [D4-02-F03] |
| Telmisartan | About 4-5 days (OUR ARITHMETIC: 24 hours x 4-5) [D4-02-F05] | US label: "Most of the antihypertensive effect is apparent within 2 weeks and maximal reduction is generally attained after 4 weeks" [D4-02-F06]; a European label: maximum at 4-8 weeks, to bear in mind "when considering raising the dose" [D4-02-F43] | 2-4 weeks (with hydrochlorothiazide) [D4-02-F07] |
| Losartan | Not given | "substantially present within one week", maximal at 3-6 weeks in some studies [D4-02-F13] | Not given |
| Chlorthalidone | About 7-12 days (OUR ARITHMETIC: 40-60 hours x 4-5; half-lives measured at 50-200 mg, claims check) [D4-02-F08] | Office readings: mostly by week 2 [D4-02-F41]; 24-hour readings in India: still growing at 12 weeks [D4-02-F44] | 2 weeks (15 mg product) [D4-02-F09] |
| Hydrochlorothiazide | About 1-3 days (OUR ARITHMETIC: 5.6-14.8 hours x 5) [D4-02-F11] | Near maximal at 4 weeks, with olmesartan [D4-02-F12] | Not given |

**Share of the full effect by day.** A review of 18 trials (4,168 patients starting a first drug, office readings; abstract only) found half the maximum systolic fall arrived in 0.91 weeks, with no difference between families, and in 1.2 weeks where the dose was being raised [D4-02-F36]. None of the trials raised the dose of a drug already being taken, so the 1.2-week figure is the closer match to a protocol step (claims check) [D4-02-F36]. The paper's curve shape could not be opened; it says only "asymptotic approach model" (the claims check could not find the equation) [D4-02-F37]. ASSUMING an exponential curve, the share is about 53% at 1 week, 78% at 2 and 95% at 4 (OUR ARITHMETIC: 1 - 0.5^(weeks / 0.91)); on a hyperbolic curve, about 69% at 2 weeks and 82% at 4 (OUR ARITHMETIC, by the claims check) [D4-02-F37]. ESH 2023 expects a two-drug combination's fall "within 1-2 weeks" and a single drug's more slowly [D4-02-F20].

**Thiazides lag on 24-hour readings.** Office readings show most of chlorthalidone's effect early: 15.7 mmHg by week 2 on 12.5 mg in a US crossover trial (30 completed the first period) [D4-02-F41]. In an Indian double-blind trial (54 patients, 12 weeks, abstract only; the first author and two co-authors are from the maker Ipca Laboratories), chlorthalidone 6.25 mg lowered ambulatory systolic pressure 6.74 mmHg at 4 weeks; two news reports give the 12-week fall as 12.11 or 11.1/7.8 mmHg, so week 4 held about 56-61% of it (OUR ARITHMETIC: 6.74 / 12.11 and 6.74 / 11.1; contested in the claims check) [D4-02-F44]. In the same trial hydrochlorothiazide 12.5 mg lowered office pressure but not 24-hour pressure: it "merely converted sustained hypertension into masked hypertension" [D4-02-F42].

**Guideline intervals.** Punjab's IHCI sheet says "After 30 days" at each step, with a footnote: "Dose of anti-hypertension medications can be titrated at 15 days frequency if required" [D4-02-F15]. Madhya Pradesh's says 30 days only [D4-02-F16]; Nigeria's, 1 month [D4-02-F33]. WHO 2021 suggests monthly follow-up until target (conditional, low-certainty evidence) and says the intervals "should be viewed as suggestions and may be modified" (claims check) [D4-02-F18]. ISH 2020: "Aim for BP control within 3 months" [D4-02-F19]. ESH 2023 allows monthly checks, notes that observational studies and "one small RCT" favour 2-weekly visits, says frequency "should not be subjected to rigid rules" [D4-02-F20], and warns against "a long titration period" with uncontrolled pressure [D4-02-F21]. NICE gives no interval [D4-02-F22].

| Faster stepping | Design | Result |
|---|---|---|
| Godwin 2010, Canada [D4-02-F24] | Cluster trial, 19 doctors, 156 patients: 2-weekly visits for 16 weeks against usual care; abstract only | Office systolic pressure fell 14.7 against 2.7 mmHg at 12 months; side effects not reported |
| Turchin 2010, US [D4-02-F25] | Cohort, 5,042 patients with diabetes | Visits every 2 weeks or less reached normal pressure in a median 0.7 against 1.9 months; observational |
| Ojji 2024, Nigeria [D4-02-F34] | Open-label trial, 300 adults, 6 months: a low-dose triple pill (telmisartan, amlodipine, indapamide) reviewed at 2 weeks and stepped up at clinic 135/85 or more, against the Nigeria protocol stepped monthly (corrected in the claims check) | Home control 62% against 28%; no stops for adverse events; but more eGFR falls of over 30% at month 1 (11% against 4%, equal by month 6) and more potassium under 3.5 at month 6 (34% against 18%). The arms differed in drugs, so speed is not isolated |
| Ishak 2024, US [D4-02-F31] | Pilot, 42 patients, pharmacist telehealth, no control group | "no instances of falls or hypotension" |

No trial randomised 2-week against 4-week steps and counted side effects. Once pressure is controlled, 6-monthly review equalled 3-monthly (609 patients, Ontario, 3 years) [D4-02-F27].

#### The 30-day step, drug by drug

OUR ARITHMETIC on an ASSUMED curve shape [D4-02-F36, D4-02-F37]: readings on days 24-30 see about 80-96% of the full effect (exponential with a half-time of 0.91 weeks gives 93-96%, with 1.2 weeks 86-92%, a hyperbolic curve 79-83%); a 14-day step read on days 8-14 would see about 48-78%.

| Step | Steady by day 24 | OUR VIEW |
|---|---|---|
| 2. Amlodipine 10 mg | Yes [D4-02-F01] | 30 days is sound; a 15-day step has support for this step alone (label, Punjab sheet, a 1987 trial in 30 patients titrated "at 2 weekly intervals") [D4-02-F03, D4-02-F15, D4-02-F35], as a clinician's option |
| 3 and 4. Telmisartan 40, then 80 mg | Yes [D4-02-F05] | Keep 30 days; the European label's 4-8 weeks argues against faster steps [D4-02-F43], and Ojji's fast ARB-plus-diuretic arm had early kidney and potassium changes [D4-02-F34] |
| 5. Chlorthalidone 12.5 mg | Yes [D4-02-F08] | Keep 30 days; the 24-hour effect may still be growing [D4-02-F44], so a mean just above the line may earn one more cycle |
| 5. Hydrochlorothiazide 25 mg | Yes [D4-02-F11] | Keep 30 days; it is short-acting, so a morning reading before the tablet sits at its lowest level: record the dose time [D4-02-F42] |

**For the loop (OUR VIEW).** The 30-day step and the day 24-30 window fit the biology on any curve shape. Faster stepping has mostly observational support, the one trial with side-effect numbers saw early kidney and potassium changes, and India's programme did not record side effects [D4-02-F34, D4-02-F17].

### I5. Natural variation and how many readings

A protocol step changes pressure by 2-6 mmHg (I3). This section measures how much pressure moves on its own, and how many readings it takes to see a step.

#### Why the number moves

- **Alerting reaction.** A doctor's arrival raised intra-arterial pressure within 1-4 minutes by a mean 26.7/14.9 mmHg in 48 people (Italy, 1983) [D4-03-F53]; 10-18 minutes of rest lowered an arrival reading by about 10 mmHg (65 people, Germany) [D4-03-F54].
- **Habituation.** Day 1 of home readings runs about 2.8/1.4 mmHg high and readings level off after day 3 (2,122 people, Finland, Greece, UK) [D4-03-F01]; in treated UK patients the day-1 excess faded after 6 months of self-monitoring [D4-03-F16].
- **Two readings.** The second averaged 2.3 mmHg lower than the first but was higher in 31.7% of pairs (175 Japanese kidney patients) [D4-03-F36]; first, second and averaged readings predicted heart events equally (Japan) [D4-03-F37].
- **Daily rhythm.** A normal "dipper" falls 10-20% at night [D4-03-F50]; 11.9% of 27,472 Indian primary-care patients had high pressure only at night [D4-03-F39]. Evening home readings ran 3.8 mmHg above morning ones in untreated and 0.9 mmHg in treated Finnish adults (OUR ARITHMETIC: 141.5 - 137.7; 137.1 - 136.2) [D4-03-F23].
- **Seasons.** Japanese home readings are 3-4 mmHg higher in winter (7,908 people) [D4-03-F28]. Indian figures are larger but are not home-cuff data: winter ran 9.01/5.61 mmHg above summer in 978 Punjab community members measured by nurses at home or work, with cold raising sympathetic drive [D4-03-F31], and 11.07/6.79 mmHg in 132 young women with normal pressure in a Delhi slum, measured at investigator visits [D4-03-F32].
- **Regression to the mean.** People picked for a high reading are partly picked for a random error that does not repeat: 286 Australians starting at a home mean of 156 fell to 143 within a year, in both trial arms [D4-03-F26], and the UK HOME BP usual-care group fell 9.8 mmHg (OUR ARITHMETIC: 151.6 - 141.8) [D4-03-F57].

#### How big the movement is

| Level | Systolic spread | Who |
|---|---|---|
| One reading within a week | SD 11.8 mmHg; a 95% band of about plus or minus 23 (OUR ARITHMETIC: 1.96 x 11.8) [D4-03-F10, D4-03-F62] | 225 treated UK patients, mean age about 67 |
| Two weekly means | SD of the difference 10.11 (1 day), 6.37 (3 days), 4.36 mmHg (7 days) [D4-03-F33] | 316 untreated US adults, mean home 115/77 |
| Error band of one mean | About plus or minus 8.8 mmHg for 3 days, 6.0 for 7 days (OUR ARITHMETIC: SD / 1.414 x 1.96) [D4-03-F34] | Same |
| 3-day against 7-day mean | 3.66 mmHg apart on average at month 1 [D4-03-F06] | 84 treated UK patients |
| A week's or a month's readings around each person's own trend | SD 4.7 and 5.1 mmHg, the model's leftover scatter (claims check) [D4-03-F11] | 232 and 582 treated UK patients |

The 3-day and 7-day figures come from untreated young adults; treated older patients vary more, so the loop's real bands are probably wider (claims check) [D4-03-F34].

#### How many readings, and how big a real change

A review of 37 studies found 3 days reach 72-91% of the best prediction of outcomes and 7 days 86-96%, and advises extending from 3 to 7 days only near a threshold [D4-03-F02]; with an upper and a lower cut-off, most people can be classed within 3 days [D4-03-F04]. ESH 2021 says 7 days, "not fewer than 3", and calls discarding day 1 "matter of debate" [D4-03-F07, D4-03-F17]. The smallest change beyond noise at 95% is about 12.5 mmHg between two 3-day means and 8.5 between two 7-day means (OUR ARITHMETIC: 1.96 x 6.37; 1.96 x 4.36) [D4-03-F34], and 13.0-14.1 between two months on unchanged drugs (OUR ARITHMETIC: 4.7-5.1 x 1.414 x 1.96) [D4-03-F61]. Reading noise as change misleads: on fixed drugs, a home mean of 130 had an 18% chance of reading 135 or more at 6 months, with only a 25% chance that such a rise was real [D4-03-F11]; among 1,709 PROGRESS trial patients, a clinic rise of over 10 mmHg gave 6 false alarms per true one [D4-03-F15].

#### White-coat and masked high pressure in India

White-coat means high in clinic but normal at home; masked means the reverse (home line 135/85, clinic 140/90) [D4-03-F42]. Untreated people (India Heart Study, 18,918 people, 1,237 doctors): 23.7% white-coat, 18.2% masked [D4-03-F21]. Primary care with 24-hour monitors (27,472 people): 12.0% and 19.3% [D4-03-F39]. Treated patients (GRAND, 1,578 analysed of 1,920 enrolled): 5.1% white-coat uncontrolled, 21.8% masked uncontrolled [D4-03-F40]. The labels are unstable: a masked label from home readings agreed with a repeat at kappa 0.26 (1 is perfect agreement) and a white-coat label at 0.18 (15 studies) [D4-03-F44]. Only 18.1% of 2,588 North Indian patients or carers used home monitoring, and technique was excellent in 15.9% of patients [D4-03-F58].

#### What self-titration trials required before a step

| Trial | Rule |
|---|---|
| TASMIN-SR, UK [D4-03-F13] | First week of each month, two morning readings 5 minutes apart, the second used; "Four or more above target readings in two consecutive weeks" required a change; each plan step came after "two consecutive months of raised readings" |
| TASMINH4, UK [D4-03-F18] | Twice morning and evening, first week of every month; weekly means; home targets under 135/85 (under 80 years), 145/85 (80 or over), 135/75 (diabetes) |
| HOME BP, UK, 622 patients [D4-03-F56] | Two morning readings for 7 days each month; a change only "When mean home blood pressure was above target for two consecutive months"; clinic systolic 3.4 mmHg lower than usual care |
| HOMEBP [D4-03-F14] | After 3 controlled months, measure every 8 weeks |
| Australia, 286 patients [D4-03-F38] | 3 or more of the last 10 readings at 135 or more best predicted uncontrolled 24-hour pressure |

Trials that used the clinic target of 140/90 for home readings controlled pressure worse [D4-03-F19]. ESH 2021 says dose self-adjustment is "to be avoided, if not under guidance by the physician in charge" [D4-03-F07]. No home-titration trial was found that used a formal statistical rule.

**For the loop (OUR VIEW).** A step's 2-6 mmHg is smaller than the noise between two monthly means, so the loop should judge where the mean sits against the line, not how far it moved. Seven days narrow the error band from about 9 to about 6 mmHg, and the UK trials waited for two months above target.

### I6. Why each safety check exists

#### The kidney after telmisartan

Blocking angiotensin II "causes selectively greater vasodilatation of the efferent arterioles of the glomeruli, resulting in a decline of the intraglomerular filtration pressure", so GFR falls and creatinine (a waste product the kidney clears) rises [D4-04-F26]; KDIGO treats a small early rise as expected [D4-05-F28]. The fall is bigger when both kidney arteries are narrowed, where ACE inhibitors are contraindicated "due to risk of azotemia" and ARB labels "anticipate an effect similar" [D4-04-F52, D4-04-F04], and in patients short of salt and water, whose pressure leans on angiotensin II [D4-04-F09].

| Source (scope) | Rule |
|---|---|
| Telmisartan label | Creatinine up 0.5 mg/dL or more in 0.4% against 0.3% on placebo; no threshold or recheck interval [D4-04-F05, D4-04-F04] |
| UKKA 2026 (every ACE inhibitor or ARB start) | Recheck "at 1-2 weeks after initiation of ACE-I or ARB and after every dose titration" (grade 1A, the strongest) [D4-04-F34] |
| NICE NG203 (adults with kidney disease) | Test 1-2 weeks after starting and after each dose rise; under a 25% eGFR fall or a 30% creatinine rise, no change; at 25% or 30% or more, look for dehydration or NSAID painkillers, then stop or cut the dose [D4-04-F23] |
| KDIGO 2021 and 2024 (kidney disease) | Check within 2-4 weeks, "depending on the current GFR and serum potassium"; the rise "will typically happen during the first 2 weeks" and should settle "within 2-4 weeks"; continue "unless serum creatinine rises by more than 30% within 4 weeks"; no trial has tested any cut-off [D4-04-F27, D4-05-F27, D4-05-F28] |
| Bakris and Weir 2000 (12 ACE-inhibitor trials, 1,102 people) | Rises "of up to 30% that stabilize within the first 2 months" went with long-term kidney protection; withdraw if the rise exceeds 30% within 2 months or potassium reaches 5.6 (claims check) [D4-04-F21] |
| IHCI Telangana and Maharashtra sheets | Baseline labs only; no recheck after telmisartan (claims check) [D4-04-F57] |

A 30% creatinine rise is about a 25% eGFR fall, so the two cut-offs differ in size (claims check) [D4-05-F28]. Rises below 30% are not fully harmless: among 122,363 UK starters (observational), death was 1.15 times as frequent after a 10-19% rise and 1.35 times after 20-29%, against under 10%, though the rise may mark sicker patients rather than cause harm [D4-04-F22]. In ONTARGET (25,620 patients, median 56 months) telmisartan 80 mg equalled ramipril, and combining an ARB with an ACE inhibitor raised kidney dysfunction with no extra benefit [D4-04-F55].

#### Potassium

Potassium sets the resting electrical charge of heart muscle cells; high potassium can cause "arrhythmias and cardiac arrest", moving fast "from peaked T waves to ventricular fibrillation or asystole", and the ECG may look normal, so only a blood test rules it out [D4-04-F35]. ARBs push potassium up by blunting aldosterone [D4-04-F26]; thiazides push it down, because more sodium reaching the collecting duct is swapped for potassium (textbook physiology, not in the label) [D4-05-F21]. Death is least common at 4.0 to under 5.0 mEq/L and rises on either side (911,698 US records, observational) [D4-04-F36]; thiazide 100 mg carried 3.6 times the odds of sudden cardiac arrest of 25 mg (US case-control study, 114 arrests) [D4-04-F37].

| Potassium (mmol/l) | Action |
|---|---|
| Above 5.0 before starting | Caution (UKKA); do not routinely start (NICE, kidney disease) [D4-04-F34, D4-04-F24] |
| 5.5-5.9 | Repeat "within 3 days, or as soon as feasible" if found unexpectedly; consider a lower dose [D4-04-F34] |
| 6.0-6.4 | Repeat within 1 day; stop the ACE inhibitor or ARB if the patient does not qualify for potassium binders (claims check) [D4-04-F34, D4-04-F24] |
| 6.5 or more | Admit at once [D4-04-F34] |

Telmisartan alone caused "no clinically significant changes" in potassium; the risk comes with kidney disease, heart failure, supplements, potassium-sparing diuretics and "potassium-containing salt substitutes" [D4-04-F06, D4-04-F07], which NICE says people on ACE inhibitors or ARBs should not use [D4-04-F28]. KDIGO prefers managing high potassium to stopping the drug [D4-05-F31]. On the other side, chlorthalidone caused more low potassium than hydrochlorothiazide (6.0% against 4.4%; 13,523 US veterans aged 65 or over, 2.4 years), with equal heart outcomes [D4-04-F33].

#### Pregnancy

In the second and third trimesters, renin-angiotensin drugs reduce the fetus's kidney function: less fetal urine, so the amniotic fluid drains (oligohydramnios), the lungs cannot grow, the squeezed fetus gets skull and limb deformities, and newborns can have no urine, low pressure or kidney failure, or die [D4-04-F02]. Timing matters because amniotic fluid grows from 10-20 ml at 10 weeks to about 800 ml at 24 weeks, with fetal urine a main source late in pregnancy [D4-04-F56]. Autopsies of 14 exposed fetuses or newborns found malformed kidney tubules, and the lesions may persist after the drug stops [D4-04-F54]. First-trimester evidence is ACE-inhibitor data, not ARB data, and the two studies measure different outcomes: any major malformation had a risk ratio of 2.71 against no blood-pressure drug in Tennessee (29,507 infants) [D4-04-F31]; in California (465,754 pairs), heart defects had an odds ratio of 1.14 against untreated hypertensive mothers, and any birth defect 0.97 on the like-for-like comparison (claims check) [D4-04-F32].

The telmisartan label (a generic made in India, revised March 2025; maker corrected in the claims check) says: "When pregnancy is detected, discontinue telmisartan as soon as possible" [D4-04-F01]; losartan's says the same [D4-04-F03]. Thiazides "can cause placental hypoperfusion", and chlorthalidone "should not be used as first-line therapy to treat hypertension in pregnancy", with no boxed warning [D4-04-F17]. Amlodipine's data "are not sufficient to inform a drug-associated risk" [D4-04-F14]. NICE says to stop an ACE inhibitor or ARB "preferably within 2 working days of notification of pregnancy" and offer labetalol, then nifedipine, then methyldopa [D4-04-F29, D4-04-F30].

#### Dizziness on standing in older people

Standing pools 25-30% of the blood in the legs and gut [D4-04-F47]. Pressure sensors in the carotid sinus and aortic arch (the baroreflex) signal the brainstem, which raises heart rate and tightens vessels; with age the reflex, fluid volume and vein tone weaken, and drugs add to it [D4-04-F46]. Orthostatic hypotension is a fall of 20 systolic or 10 diastolic after at least 1 minute standing, measured from lying (or seated if lying is impractical, repeating from lying if a seated test is negative despite symptoms) [D4-04-F38]. It affects 22.2% of community adults over 60 (24,967 people) [D4-04-F39] and 9.6% of 240 older people in Kerala, where a first-minute drop went with falls (odds 1.97) [D4-04-F40]; an ordinary cuff finds first-minute drops in 5.6% against 29.0% by continuous measurement [D4-04-F41]. It goes with falls (odds 1.73, 50 studies) [D4-04-F42]. Hip fractures were 43% more common in the 45 days after starting any blood-pressure drug (301,591 people, Ontario) [D4-04-F48], and in ALLHAT (23,964 people 65 or over) amlodipine brought more falls than chlorthalidone in the first year only (HR 2.24, needing confirmation) [D4-04-F49]. Lower targets slightly lowered orthostatic hypotension in 5 trials (18,466 people; odds 0.93), though the trials missed first-minute drops [D4-04-F44]. At home, a patient-led lying-to-standing test agreed with the clinician's at kappa 0.90 in 25 older patients in north-east England, though single readings differed by up to 17-20 mmHg [D4-04-F50].

#### Sodium, uric acid and sugar on thiazides

- **Sodium.** Thiazides block the salt transporter in the distal convoluted tubule, the segment that dilutes urine, so free water is passed poorly; drinking a lot and eating little make it worse [D4-04-F60]. In Denmark (age 40 or over), 3.83% of new bendroflumethiazide users and 3.51% of new hydrochlorothiazide-combination users had sodium under 130 mmol/l within 2 years, with hazard ratios of 3.56 and 4.25 in the first 30 days falling to 1.26 and 1.29 after a year; labels call it rare [D4-04-F58]. Each 10 years of age gave a hazard ratio of 2.14 and each 5 kg more weight odds of 0.77 (Hong Kong, 223 cases) [D4-04-F61]. In Lucknow, 27% of outpatients on diuretics for 6 months or more had low sodium; of 247 hospitalised low-sodium cases of any cause, 45% were admitted in April-June and 46.6% in October-March, and diuretic use was not significant in the multivariate analysis (corrected in the claims check) [D4-04-F62]. Season is at most a soft flag.
- **Uric acid.** Thiazides cut uric acid clearance and "may precipitate gout in susceptible patients" [D4-04-F16]; in 5,789 US adults over 9 years they raised gout risk (HR 1.44), and the link vanished after adjusting for uric acid [D4-04-F63].
- **Sugar.** Labels report dose-related glucose rises [D4-04-F15, D4-04-F19]; across 59 trials glucose rose as potassium fell (r = -0.54), perhaps because low potassium reduces insulin release [D4-04-F64].

#### Ankle swelling on amlodipine

Widening the arterioles is thought to raise capillary pressure, so fluid leaks into the ankles [D4-04-F65]. Swelling was 3.0% at 5 mg and 10.8% at 10 mg against 0.6% on placebo [D4-04-F11], 14.6% in women and 5.6% in men across doses [D4-04-F12], and 24% after 6 months across 106 calcium-blocker trials [D4-04-F65]. Adding an ARB or ACE inhibitor cut it by 38% [D4-04-F66]. In India, 23.9% of 800 amlodipine patients in a Mumbai hospital record study had swelling at some point [D4-04-F67], and an unpublished IHCI survey found about 12% on 10 mg [D4-02-F17].

#### What 180/110 means

Without symptoms this is urgency; an emergency is very high pressure "associated with acute organ damage" [D4-04-F70]. In 59,836 Cleveland Clinic office visits at 180/110 or more, matched patients sent home (852) had no major heart events at 7 days against 0.5% of those sent to hospital (426), and referral brought more admissions without better outcomes; patients referred for symptoms were excluded [D4-04-F68]. Long-standing high pressure "shifts the lower and upper blood pressure limits of CBF autoregulation towards higher pressure" (CBF: cerebral blood flow), and lowering cuts brain flow only below the lower limit [D4-04-F72]. OUR VIEW: a fast fall is more likely to cross that raised limit, which argues against bringing pressure down fast at home. NICE sends a person at 180/120 to same-day care only with eye signs or "life-threatening symptoms such as new onset confusion, chest pain, signs of heart failure, or acute kidney injury" [D4-04-F71]. The sheets differ: Telangana refers "after starting treatment", Maharashtra starts treatment and refers immediately [D4-04-F57], and Nigeria sends the patient to emergency within 1 hour [D4-02-F33].

**For the loop (OUR VIEW).** Each check has a window: kidney and potassium tests 1-4 weeks after telmisartan starts or rises; sodium and potassium in the first month of a thiazide; a pregnancy question every cycle on a barred drug; a standing check in older patients in the weeks after each step; and a symptom question, not a faster dose, at a very high reading.

### I7. Biomarkers beyond the cuff

"Public" is India's 2025 essential diagnostics list; these tests are free under the National Health Mission's free diagnostics initiative (2015, revised 2019) [D4-05-F39]. Prices are search summaries from 14 Nov 2026.

| Marker | What it tells | Normal and action thresholds | How fast it changes | Public test site | Private price |
|---|---|---|---|---|---|
| Creatinine, eGFR | Kidney filtration; read against diet and muscle [D4-05-F26] | On an ARB, a rise under 30% is expected [D4-05-F28]; 30% or more, look for causes (NICE) [D4-04-F23]; an eGFR change over 20% exceeds normal variation in kidney disease [D4-05-F29] | Rises in the first 2 weeks of an ARB, settles by 2-4 [D4-04-F27] | PHC (primary health centre) [D4-05-F39]; point-of-care allowed where labs are far [D4-05-F30] | Not searched; one point-of-care analyser listed at ₹30,000 (search summary only) [D4-05-F50] |
| Potassium | Heart-rhythm risk | Caution above 5.0 before an ARB; 5.5-5.9 recheck within 3 days, 6.0-6.4 within 1 day, 6.5 or more admit [D4-04-F34]; death risk rises below 4.0 [D4-04-F36] | Recheck 1-2 weeks after an ARB starts or rises [D4-04-F34]; 0.35 mmol/l lower by week 4 of chlorthalidone 15 mg [D4-02-F10] | Sent from a PHC to a hub; on site at a CHC (community health centre) [D4-05-F39] | Not searched |
| Urine albumin-to-creatinine ratio (ACR) | Damage to the kidney's filter; predicts kidney and heart events [D4-05-F32] | Under 30 mg/g normal to mild, 30-300 moderate, over 300 severe [D4-05-F32]; a doubling exceeds lab variation; confirm a strip result with a lab ACR [D4-05-F33] | Not found | Dipstick at village level; ACR sent from a PHC [D4-05-F39] | ₹270-660 (search summary only) [D4-05-F40]; a phone-read home test is US-cleared, no India price [D4-05-F49] |
| NT-proBNP | Stretch of the heart wall (from a 2026 review) [D4-05-F34] | Heart failure ruled out under 125 pg/mL (not acute) or 300 (acute); acute rule-in at 450, 900 or 1,800 by age band [D4-05-F34] | Not found | District or sub-district hospital only [D4-05-F35] | ₹1,200-3,520 (search summary only; the claims check could not re-find it) [D4-05-F36] |
| HbA1c | Average sugar over about 2-3 months [D4-05-F37] | Goal under 7% for many adults; misleading in anaemia, kidney failure, pregnancy [D4-05-F37] | Months; test about 3-monthly after a change [D4-05-F37] | PHC sends the sample on [D4-05-F39] | ₹270-300 with home collection (search summary only) [D4-05-F38] |
| Uric acid | Raised by thiazides; gout [D4-04-F16, D4-04-F63] | Threshold not found | Up 0.66 mg/dL by week 4 of chlorthalidone 15 mg [D4-02-F10] | PHC [D4-05-F39] | Not searched |
| Sodium | Thiazide-linked low sodium | Under 130 mmol/l was the Danish study's outcome [D4-04-F58] | Risk highest in the first 30 days [D4-04-F58] | Sent from a PHC to a hub [D4-05-F39] | Not searched |
| Renin, aldosterone-to-renin ratio | Rises on an ARB: a sign it is taken [D4-05-F18, D4-05-F19] | A 48% fall in the ratio from baseline flagged adherence (one 40-patient study) [D4-05-F43] | Seen at 2 weeks [D4-05-F43] | Not routine in primary care [D4-05-F18] | Not found |

The Gujarat step-4 panel (sugar, urea, creatinine, urine protein) is mostly doable at a PHC; potassium and ACR need a sample sent on [D4-05-F39].

**For the loop (OUR VIEW).** Creatinine and potassium are the step-cycle tests, joined by sodium at the thiazide step; ACR and HbA1c are slow checks; NT-proBNP is for suspected heart failure only.

### I8. Signs the medicine was taken

#### How often apparent failure is non-adherence

| Study | Who | Not taking the drugs |
|---|---|---|
| Meta-analysis, 24 studies [D4-05-F01] | Uncontrolled on 3 or more families | 31.2% pooled (3.3-86.1%); assays found more than self-report or pharmacy data |
| UK and Czech clinics [D4-05-F03] | 1,348, urine or blood assay | 41.6% and 31.5%; each extra prescribed drug went with an 85% and 77% increase in non-adherence (the abstract does not say odds or risk; per drug, not per dose step, claims check) |
| Brazil 2026 [D4-05-F07] | 253 treated patients averaging 3.2 drugs | 32.4% adherent by urine assay against 90.1% by questionnaire; agreement nil (kappa 0.014); odds 1.57 per drug |
| UK primary care [D4-05-F12] | 191 people 65 or over, median 2 drugs | 4.7%; "widespread testing is not indicated" there |
| Global, 161 studies [D4-05-F13] | 27 million patients | 27-40%, higher in low- and middle-income countries |
| Belgium [D4-05-F44] | 201 referred as resistant | About 3 in 4 not truly resistant; only 23.4% on maximal doses |
| India [D4-05-F15] | No assay study found | Not known |

**Drug assays** (liquid chromatography with mass spectrometry, LC-MS/MS, which finds the drug in urine or blood) are the reference test. Telling non-adherent patients their result was followed by large falls in UK and Czech clinics, but with no control group [D4-05-F04]. Two randomised trials were null on pressure: RHYME (Netherlands, 100 patients, 12 months) raised adherence from 70.0% to 92.5% without a significant change in resistant hypertension [D4-05-F05]; OUTREACH (UK, 12 centres) randomised 130 non-adherent patients after 748 of 879 were excluded at the first visit (corrected in the claims check), and found -5.1 mmHg, not significant [D4-05-F11]. Patients may take their drugs because they know they are tested (the Hawthorne effect) [D4-05-F06], and long half-lives mean a dose the day before still shows [D4-05-F17]. UK experts advise ordering a test when systolic pressure fell less than 10 mmHg after a second drug [D4-05-F14]; this is a trigger for a confirmatory assay, not a sign of non-adherence, and at Gujarat step 3 the label trial's mean fall was 11.1 mmHg, only 3.7 of it beyond staying on amlodipine, so many adherent patients would be flagged (claims check) [D4-05-F14, D4-01-F50]. No Indian lab offering such a panel, and no price, was found.

#### Which body signals work for which drug

| Drug | Signal | Shows intake |
|---|---|---|
| Amlodipine | No significant heart-rate change on daily dosing [D4-05-F16] | No |
| Telmisartan, losartan | No heart-rate change; renin rises (losartan: doubles to triples) [D4-05-F18, D4-05-F19] | Only by a lab test; one study (40 patients, 40 controls) found a 48% fall in the aldosterone-to-renin ratio flagged adherence with 90% sensitivity and 75% specificity [D4-05-F43] |
| Chlorthalidone, hydrochlorothiazide | Potassium falls and uric acid rises with dose, in step with the pressure effect [D4-05-F21, D4-05-F22] | Weakly |
| Beta-blockers (not in the protocol) | Heart rate falls; "Monitor heart rate" [D4-05-F41] | Yes, on a cuff's pulse reading |
| Any drug, by a wearable | No validated method found (search summary only) [D4-05-F45] | No |

#### Refill data, packaging and devices

In 597 Indian TB patients checked with urine tests on surprise home visits, the 99DOTS phone-call record had sensitivity 70% and negative predictive value 21% [D4-05-F23]. REMIND (US, 53,480 people, 12 months) found a pillbox, timer cap or toggle strip no better than nothing [D4-05-F24]. Blister and calendar packs raised pills taken by 11% and lowered diastolic but not systolic pressure (Cochrane, searches to 2010) [D4-05-F46]. Patient traits predicted poor refill collection only weakly (C statistic 0.606), so the refill record itself is the measure [D4-05-F47], though refills and self-report both undercount non-adherence against assays [D4-05-F48].

**For the loop (OUR VIEW).** Amlodipine and telmisartan leave no cheap body signal. The practical layers are refill dates, a photo or count of the strip, and potassium and uric acid at the thiazide step; assays belong at referral.

### I9. Features this suggests for the product

OUR VIEW and OUR DESIGN throughout. **Tonight**: a data field, question or test case that changes no dose decision, before the 05:00 engine freeze. **Next**: the two-week test or pilot, after a clinician signs it. **Later**: needs patient data. "Hard to copy" appears only where the notes support it.

1. **A response model on each family's time course.** Store each step's expected extra fall (about 5, 4, 2 and 6 mmHg for steps 2 to 5) and time course in the protocol file, and show expected against measured on the doctor's card (tonight, display only) [D4-01-F49, D4-01-F50, D4-01-F53, D4-02-F36]. Around day 14 after a step, a home mean with almost no fall prompts the medicine question early, without an early step-up (next) [D4-02-F37]. Learn each patient's own response across repeated cycles (later); a single cycle is mostly noise [D4-03-F55]. Hard to copy: the national programme records no side effects or home readings by step [D4-02-F17], and each approved step adds one Indian example.
2. **Choosing the next drug from the profile.** Record age, sex and salt habit (tonight: three fields) [D4-01-F39, D4-01-F47, D4-01-F13]. For an adherent patient who fails a step, the card can raise the switch between a renin-angiotensin blocker and amlodipine or a thiazide, where differences between people lie (later, within what the sheet and clinician allow) [D4-01-F02, D4-01-F04]. No gene or renin tests [D4-01-F34, D4-01-F36]. South Asian trials show no family advantage [D4-01-F11]. Hard to copy: no Indian rotation trial exists, so the loop's data could test these predictors first.
3. **Adherence beyond self-report.** Add the refill date and a strip photo, and ask harder at steps 3 and 5, which add a drug (next) [D4-05-F47, D4-05-F46, D4-05-F03, D4-05-F07]. Read potassium and uric acid at the thiazide step as a weak intake sign (next) [D4-05-F22]; an aldosterone-to-renin baseline is the only ARB-specific sign found (later) [D4-05-F43]. Not: heart rate [D4-05-F16], in-loop assays [D4-05-F15], or the less-than-10 mmHg trigger as a label [D4-05-F14]. In older UK primary care only 4.7% were non-adherent [D4-05-F12], and clinicians fear patients feeling policed [D4-05-F09]. Hard to copy: no Indian assay study of adherence exists [D4-05-F15].
4. **A "still high" rule sized to the noise.** Treat 135/85 as the centre of a band: with 7 valid days a mean of about 141 or more is high beyond noise (OUR ARITHMETIC: 135 + 6.0) [D4-03-F34]; 135-140 earns a second cycle, as TASMIN-SR and HOME BP waited two months [D4-03-F13, D4-03-F56]; with 3-4 days and a mean within about 9 mmHg of 135, ask for more days [D4-03-F02, D4-03-F34]. Test cases tonight; live next, once a clinician signs the band. The bands probably understate older treated patients' noise [D4-03-F34], and ESH warns against slow titration [D4-02-F21]. Hard to copy: no Indian data on home-reading variation were found.
5. **A safety window after each step** (next, unless marked). Creatinine and potassium 1-2 weeks (UKKA) to 2-4 weeks (KDIGO) after telmisartan starts or rises, as percent change from a baseline taken before step 3, holding the next step until the result is in [D4-04-F34, D4-04-F27]; ask about potassium salt substitutes and painkillers first [D4-04-F07, D4-04-F23]. Sodium and potassium in the first month of chlorthalidone, older and thinner patients first [D4-04-F58, D4-04-F61]. A pregnancy question every cycle on a barred drug, with "pregnant" raising a stop-within-2-working-days card and a drafted switch (tonight as a question and test) [D4-04-F29, D4-04-F30]. For patients 60 or over, a lying (or seated) to standing pair and a falls question in the 45 days after each step [D4-04-F38, D4-04-F48, D4-04-F50]. An ankle-swelling question after step 2 [D4-04-F11, D4-04-F66]. At 180/110, a rested repeat and a symptom checklist set by the clinician (OUR DESIGN, starting from NICE's list): symptoms to same-day care, no symptoms to urgent review, never extra doses (tonight if time allows) [D4-04-F71, D4-04-F68, D4-04-F72]. Hard to copy: India's programme did not record side effects [D4-01-F45].

### I10. What this suggests changing in the current design

OUR VIEW: suggestions for the team and a clinician to decide. None changes the state protocol, and no other part of this document was edited to make them.

| Current design (where) | What the new research says | Suggested change | When |
|---|---|---|---|
| 30-day step (chapter 4.1) | Every drug is steady by day 24; about 80-96% of the effect is in by days 24-30 (OUR ARITHMETIC, assumed curve) [D4-02-F37]; Punjab allows 15 days [D4-02-F15] | Keep 30 days; 15 days only for amlodipine 5 to 10 mg, as a clinician's option | Later |
| At least 3 valid days, aim for 7 (chapter 4.3) | 3-day error band about plus or minus 8.8 mmHg against 6.0 for 7 days (OUR ARITHMETIC) [D4-03-F34] | With 3-4 days and a mean within about 9 mmHg of 135, ask for more days | Next |
| "Still high" at 135/85 (chapter 4.3) | The home-clinic gap is supported [D4-02-F22, D4-03-F19]; a 7-day mean still carries about 6 mmHg of noise [D4-03-F34] | Keep the line; add a band (about 141 with 7 days) and a second cycle for 135-140 | Next |
| Day 1 dropped if 4 or more valid days remain (Appendix G) | Fits the evidence; the day-1 effect fades after 6 months [D4-03-F01, D4-03-F16] | Keep; stop dropping day 1 after 6 months | Later |
| Two self-report buttons (chapter 4.6) | Self-report 90.1% against assay 32.4% in one clinic [D4-05-F07] | Add refill date and strip photo; ask harder at steps 3 and 5 | Next |
| Step 2, amlodipine 10 mg (chapter 4.1) | Adds 5.3 mmHg but more than triples ankle swelling [D4-01-F49, D4-01-F19]; adding telmisartan to 5 mg did better [D4-01-F51] | Ask about swelling; show the trial on the card; keep the Gujarat order | Next |
| Step 4, telmisartan 80 mg (chapter 4.7) | Adds 0.2-1.7 mmHg for four lab tests [D4-01-F49, D4-01-F50] | Flag it as low-yield; ask the clinician, and later the state, about going straight to step 5 | Next; later |
| Labs only before telmisartan 80 mg (chapter 4.7) | UKKA rechecks 1-2 weeks after every ARB start or rise; the IHCI sheets ask none [D4-04-F34, D4-04-F57] | Baseline before step 3; recheck after steps 3 and 4; hold the next step for the result | Next |
| No labs at step 5 (chapter 4.7) | Thiazide low sodium is front-loaded in 30 days [D4-04-F58] | Sodium and potassium in the first month | Next |
| Hydrochlorothiazide substitute (chapter 4.1) | Short-acting [D4-02-F42] | Record the dose time beside readings | Next |
| Pregnancy checked at the next step (chapter 4.7) | Stop an ARB within 2 working days [D4-04-F29] | Ask every cycle while a barred drug is taken | Tonight (question); next |
| Low-pressure rule unset (chapter 4.7) | 22.2% of over-60s; hip fractures rise in 45 days [D4-04-F39, D4-04-F48] | Standing check and falls question for patients 60 or over | Next |
| 180/110: repeat, then an urgent card (chapter 4.7) | Emergency means organ damage; do not lower fast [D4-04-F70, D4-04-F72] | Add a symptom checklist | Tonight or next |
| No season rule | Indian winter readings 9-11 mmHg higher, not home-cuff data [D4-03-F31, D4-03-F32] | A season note on the card | Later |
| Loop for patients who miss review (chapter 4.1) | 21.8% of treated patients high only at home [D4-03-F40] | Offer home cycles to the clinic-controlled | Later |
| Monthly cycles with no end (chapter 4.3) | Controlled patients: 6-monthly equalled 3-monthly; HOMEBP went 8-weekly [D4-02-F27, D4-03-F14] | A maintenance mode | Later |

### I11. Where the new research meets the old

Old numbers are repeated only where needed to show a difference; the old facts' own verdicts are in Appendix J.

| Topic | Old fact (where) | New fact | Same or different | Claims check |
|---|---|---|---|---|
| GRAND's size | Chapter 1.4 and Appendix A attach GRAND's percentages to 1,920 treated patients [D3-04-F09] | 1,920 were enrolled; 1,578 with valid clinic and home readings were analysed, and every percentage is of the 1,578 [D4-03-F40] | Same percentages, different count | The claims check D4-06 corrected D3-04-F09 and confirmed D4-03-F40; those chapters were not edited here |
| PHYSIC | Chapter 2.3, Appendix C [D2-03-F12] | Same size and gain; adds 270 analysed, which pairs differ, model estimates [D4-01-F01, D4-01-F02]; most apparent individual response is noise [D4-03-F55] | Same, with a counterweight | Confirmed |
| Amlodipine leg swelling | Chapter 2.1, Appendix B: a rate by arm in a self-titration trial [D1-01-F01] | Rates by dose: 3.0% at 5 mg, 10.8% at 10 mg [D4-01-F19]; 23.9% in Mumbai records [D4-04-F67] | Different measures, no conflict | D4-01-F19 confirmed |
| IHCI control by step | Chapter 2.2 [D3-05-F04, D1-06-F04] | Same figures [D4-01-F45]; adds median 12 months of treatment, 16.5% and 31.5% controlled at registration, 36% not returning and 8% off protocol (OUR ARITHMETIC: 44%, near chapter 2.2's "about 43%") [D4-02-F17] | Same, with caveats | Confirmed, with cautions |
| Who returns | Chapter 1.3: about half of a 21,895-patient cohort [D1-03-F10] | 36% of 281,209 starters did not return in Jan-Mar 2022 [D4-01-F45] | Different cohorts, no conflict | Confirmed |
| TASMINH4, HyperLink, TASMIN-SR | Chapter 2.1, Appendix B [D1-01-F03, D1-01-F04, D1-01-F02] | Same results; add schedules, the rule before a step and similar adverse events [D4-02-F28, D4-02-F29, D4-03-F13] | Same, with detail | Confirmed |
| Share not taking drugs | Chapter 5.4's simulation uses 48% (search summary only) [D1-03-F44] | 4.7% to 67.6% by setting (OUR ARITHMETIC: 100 - 32.4) [D4-05-F12, D4-05-F07] | 48% is inside a wide range | Confirmed |
| 99DOTS and adherence technology | Chapter 2.1 rule 3, Appendix B [D1-02-F58, D1-02-F59] | 99DOTS NPV 21% against urine tests [D4-05-F23]; REMIND, RHYME, OUTREACH null [D4-05-F24, D4-05-F05, D4-05-F11] | Agrees | Confirmed; OUTREACH count corrected |
| Safety of stepping | Chapter 2.1: no rise in falls at 4 years in China [D1-01-F38] | Hip fractures rise in the first 45 days [D4-04-F48]; Nigeria's fast arm had early kidney and potassium changes [D4-02-F34] | Different time windows | Confirmed; D4-02-F34 corrected |
| Home and clinic lines | Chapter 4.3 [D2-01-F1] | NICE: home 5 mmHg lower [D4-02-F22]; HOME BP used clinic minus 5/5 [D4-03-F56] | Agrees | Confirmed |
| Step curve | Chapter 5.4: the simulation's step curve is flat after step 3 | Step 4 adds 0.2-1.7 mmHg [D4-01-F49, D4-01-F50] | Agrees | Confirmed |
| Interval | Chapter 4.1: Gujarat's 30 days [D1-06-F14] | Punjab allows 15 days, Madhya Pradesh does not [D4-02-F15, D4-02-F16] | Different sheets | Confirmed |

### I12. What we could not find

- **Who responds:** an Indian or South Asian rotation trial; Indian evidence that age, sex, renin or salt changes response; Indian renin profiles; any gene test in routine use for the protocol drugs.
- **Timing:** weeks to maximum effect for amlodipine; a trial of 2-week against 4-week steps with side effects counted; the 18-trial model's curve; the Indian chlorthalidone trial's full paper; the Gujarat sheet in this round; Indian package inserts.
- **Variation:** Indian data on within-person home variation or on seasonal home readings; a formal statistical stepping rule in any trial; the 2026 ISH home-monitoring rules; an Indian home-clinic offset.
- **Safety:** numeric creatinine or potassium thresholds in the US labels; a recheck after telmisartan in the IHCI sheets; Indian studies of high potassium on telmisartan or of thiazide low-sodium risk factors.
- **Tests and adherence:** how fast ACR or NT-proBNP change after treatment; a uric acid threshold; private prices for creatinine, potassium and sodium tests; an India price for home ACR; an Indian drug-assay study, lab or price; a validated wearable intake signal.

### I13. So what for us

OUR VIEW.

- **The biology supports the loop's shape:** a fixed ladder, 30-day steps, a mean of several days of home readings, a medicine check before a step-up and a doctor's approval.
- **It shows where the design is thin:** kidney and potassium rechecks after telmisartan, sodium after the thiazide, pregnancy at every cycle, a standing check for older patients, and self-report as the only adherence check. Each is a protocol-file change for the biology student and a clinician, not a code rewrite.
- **The number for the pitch:** a step moves pressure by 2-6 mmHg, less than the noise between two monthly means. The loop's value is getting each patient to the next step at the right time and safely, as chapter 5's simulation also says, not clever per-patient dosing tonight.
- **What makes it hard to copy is the record:** approved steps with home readings before and after, labs, refills and side effects, for Indian patients; none of this was found published.
- **Say it plainly:** none of this has been tested on patients; it is a design informed mostly by Western physiology and a few Indian studies.
