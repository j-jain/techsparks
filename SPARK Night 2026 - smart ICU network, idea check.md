# Smart ICU network for district hospitals: idea check

16 Nov 2026.

**The idea as proposed:**
- Fit a room of 20-30 smart ICU beds into rural hospitals while they are being built.
- Each bed carries condition-specific sensors, cameras at several angles and a microphone.
- AI spots trouble, collects the evidence (for example before-and-after photos of yellowing skin) and suggests what to do.
- A central team of specialists reviews the case on a short call and approves. The nurse carries it out.
- When surgery is needed, the hospital calls the nearest surgeon.
- "Cloudphysician plus Cadence": the remote ICU of the first, with the treatment loop of the second.

How to read this note. Fact IDs link to their sources, and the register at the end lists each one. The research is in three notes: `research_notes\dtx\D6-01`, `D6-02` and `D6-03`. Tags mark what is not a sourced fact:

- OUR VIEW: a judgement.
- OUR ESTIMATE: a rough number.
- OUR ARITHMETIC: a sum we did, shown.
- ASSUMPTION: something to test.
- OUR DESIGN: a choice made for the product.
- EXAMPLE: mock-up data.
- TARGET: a pass bar for the pilot.
- THEIR CLAIM: what a company says about itself.
- NOT RESEARCHED or NOT FOUND: a gap.

## The answer

Build it, but do not sell "smart rooms". Sell a way to run the ICUs the government is already building in every district, safely, with the staff those ICUs will actually have. OUR VIEW. Six reasons:

- **The timing is real, and bigger than one hospital.**
  - The government plans Critical Care Blocks for 602 districts ([D6-01-F01](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf)). A Dec 2025 Lok Sabha reply counts 621 approved, worth ₹18,799.21 crore (search summary only) ([D6-01-F03](https://eparlib.sansad.in/bitstream/123456789/3017761/1/AU2281_ePmCao.pdf)).
  - One analysis puts completion at 3% ([D6-01-F04](https://www.impriindia.com/insights/the-next-phase-of-indias-health-system/)).
  - Every block's design already lists a monitor with a central station for each ICU bed, and budgets money for "teleconsultation" ([D6-01-F01](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf), [D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf)).
  - Your "enter during construction" instinct fits a funded national programme.
- **The gap is people, not machines.**
  - The norms ask for specialists round the clock and one nurse per ICU bed. Central money for staff ended in FY 2025-26 ([D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf)).
  - India had 8,350 critical care specialists against a need of more than 50,000 (2016) ([D6-01-F09](https://www.onmanorama.com/business/news/hospitals-doctors-icu-who-indian-medical-association-village-remote-areas-india.html)).
  - Ventilators bought in Covid sat idle for lack of trained staff ([D6-01-F11](https://www.freepressjournal.in/bhopal/madhya-pradesh-40-ventilators-from-covid-era-lying-unused-or-scrapped), [D6-01-F12](https://www.pressreader.com/india/hindustan-times-bathinda/20210518/281809991789472)).
- **Cameras plus AI plus remote specialists already exist.**
  - Cloudphysician has camera vision, AI notes and voice-to-text, and claims 1,30,000+ patients across 280 hospitals ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930)).
  - 10BedICU runs 216 ICUs and 15 hubs on free open-source software ([D6-02-F05](https://www.10bedicu.org/), [D6-02-F07](https://github.com/ohcnetwork/care)).
  - Copying them is not a gap.
- **Watching does not help by itself; acting on time does.**
  - The largest trial of remote intensivist rounds (30 ICUs, 17,024 adults) found no shorter ICU stay and no difference in any other outcome ([D6-02-F12](https://pubmed.ncbi.nlm.nih.gov/39382244/)).
  - Where benefit appears, it is tied to standard steps done more reliably and to alerts acted on within hours ([D6-02-F13](https://pubmed.ncbi.nlm.nih.gov/21576622/), [D6-02-F16](https://pubmed.ncbi.nlm.nih.gov/35864252/)).
  - This is Cadence's real lesson too: only programmes that changed treatment moved blood pressure ([D1-05-F1](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf)).
- **Rural ICUs need protocol packs, not organ rooms.**
  - The block guideline names heart attack, stroke, COPD, ARDS, poisoning and septic shock as the top critical-care conditions ([D6-01-F01](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf)).
  - Snakebite and pesticide poisoning have written Indian or trial-tested step-by-step treatments ([D6-03-F01](https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf), [D6-03-F02](https://pmc.ncbi.nlm.nih.gov/articles/PMC3550249/)).
- **Nobody covers the whole path.** Cloudphysician stops at the ICU door, and Cadence works only at home in the US ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930), [D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care)). Ward, then ICU, then home is open. OUR VIEW

**Problem statement for the pitch (OUR VIEW):** "India is building ICUs in 621 districts but not the specialists to run them, so beds sit idle or patients die waiting to be moved. We make a district ICU run safely with the staff it has. Standard treatments run step by step from written protocols. A remote specialist approves only what needs a specialist. The patient is followed from the ward, through the ICU, to home."

Next step: build three parts and test them on open ICU data (section 9):
- a camera that reads any monitor
- the protocol engine with a snakebite and a sepsis file
- the specialist's one-tap card

Then a three-month pilot in one district ICU.

## 1. The problem, in numbers

This section shows what is being built, who is missing, and who the patients are.

| What | Number | Source |
|---|---|---|
| Critical Care Blocks approved | 621 blocks, ₹18,799.21 crore, FY 2021-22 to 2025-26 (search summary only) | [D6-01-F03](https://eparlib.sansad.in/bitstream/123456789/3017761/1/AU2281_ePmCao.pdf) |
| How many are finished | "only 3% completion" (IMPRI, Jul 2026); one unsourced page says "10 out of 394 units operational" | [D6-01-F04](https://www.impriindia.com/insights/the-next-phase-of-indias-health-system/), [D6-01-F05](https://c4scourses.in/national-affairs/pm-abhim-funds/) |
| Cost of a 50-bed block | ₹23.75 crore to build and equip; ₹4.592 crore a year to run | [D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) |
| Staff budgeted for a 50-bed block | 5 specialists (₹60 lakh a year), 12 duty doctors, 66 nurses | [D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) |
| Pay implied for a specialist | about ₹1 lakh a month (₹84 lakh / 7 specialists / 12 months, 100-bed block); "only indicative" | OUR ARITHMETIC from [D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) |
| Critical care specialists | 8,350 against a need of more than 50,000 (IMA, 2016) | [D6-01-F09](https://www.onmanorama.com/business/news/hospitals-doctors-icu-who-indian-medical-association-village-remote-areas-india.html) |
| ICU beds in public hospitals | 37,834, including 9,873 for children (Dec 2024; search summary only) | [D6-01-F07](https://eparlib.sansad.in/bitstream/123456789/2987466/1/AU4360_wkfa0t.pdf) |
| Deaths in Indian ICUs | 18.1% (2010-11) and 23.4% (2018-19); the two samples differ | [D6-01-F08](https://pmc.ncbi.nlm.nih.gov/articles/PMC8645819/) |
| Snakebite deaths | about 58,000 a year; 94% rural; 77% outside hospital | [D6-01-F14](https://pmc.ncbi.nlm.nih.gov/articles/PMC7340498/) |
| Pesticide suicides | 7,123 in Telangana and Andhra Pradesh in 2024, called one in four of India's total (search summary only) | [D6-01-F16](https://thesouthfirst.com/health/a-cheap-herbicide-was-behind-nearly-1-in-4-suicide-deaths-in-2024-it-is-still-on-sale/) |
| Idle machines | about 40% of Covid-era ventilators unused or scrapped in Madhya Pradesh medical colleges (2025); 191 unused in Himachal (2021) | [D6-01-F11](https://www.freepressjournal.in/bhopal/madhya-pradesh-40-ventilators-from-covid-era-lying-unused-or-scrapped), [D6-01-F12](https://www.pressreader.com/india/hindustan-times-bathinda/20210518/281809991789472) |

**Who the patients are.**
- In the national INDICAPS-II snapshot (132 ICUs, 4,669 adults), 29.3% had sepsis or septic shock during their stay. Poisoning was 1.5%, mostly pesticides ([D6-01-F08](https://pmc.ncbi.nlm.nih.gov/articles/PMC8645819/)).
- That sample leans to large hospitals: 36.4% of its ICUs were in hospitals with 500 or more beds ([D6-01-F08](https://pmc.ncbi.nlm.nih.gov/articles/PMC8645819/)).
- A case mix for district-hospital ICUs was NOT FOUND.
- Snakebite and pesticide poisoning are rural and seasonal: about 70% of snakebite deaths fall in eight states ([D6-01-F14](https://pmc.ncbi.nlm.nih.gov/articles/PMC7340498/)).
- At one sub-district hospital, 48.96% of snakebite patients arrived after at least 6 hours (search summary only) ([D6-01-F15](https://www.ijmedicine.com/index.php/ijam/article/view/2877)).

**Getting patients moved is a gap too.**
- At one North Indian referral centre, 30.1% of 1,013 referred newborns died, half of those deaths within 24 hours of arrival (search summary only) ([D6-01-F17](https://doaj.org/article/c40f039c5d2e43998643b54ed3cbd482)).
- A study of injured patients notes India has no guidelines for transferring them ([D6-01-F17](https://doaj.org/article/c40f039c5d2e43998643b54ed3cbd482)).
- No adult ICU transfer study was found.

**So what for us (OUR VIEW).** The buyer exists (the state, for each block), and the pain is concrete: a building with monitors and ventilators, and no one trained to run them at 2 am. Lead with sepsis, the largest group, and add snakebite and pesticide packs in the eight high-burden states.

## 2. Who is already there

This section shows that the ICU-monitoring half of the idea is already sold, and where each player stops.

| Who | What they do | Scale (as stated) | Who pays | Where it stops (OUR VIEW) |
|---|---|---|---|---|
| Cloudphysician, Bengaluru | 24/7 remote intensivists. RADAR tools: NETRA (camera vision), AIRA (AI notes), SWARA (voice-to-text), HERA (digitises paper) ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930)) | 1,30,000+ patients, 280 hospitals (THEIR CLAIM; another page says 480) ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930), [D6-02-F02](https://frontiertech.niti.gov.in/story/cloudphysicians-radar-system-delivers-24-7-critical-care-anywhere-in-india)) | Mostly private hospitals: "90%" in an older report (search summary only) ([D6-02-F04](https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution)) | No protocol-step product, ward or home follow-up, or price published |
| 10BedICU with CARE | Donates ICU equipment and open-source software; hubs at medical colleges ([D6-02-F05](https://www.10bedicu.org/), [D6-02-F06](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages)) | 216 units, 15 hubs, 10 states (THEIR CLAIM) ([D6-02-F05](https://www.10bedicu.org/)) | Donors pay the set-up; states pay to run it ([D6-02-F05](https://www.10bedicu.org/)) | No outcome data; relies on hub specialists' time |
| State hubs (Karnataka, Jharkhand, Nagaland, Meghalaya, J&K) | Medical-college specialists support district ICUs ([D6-02-F08](https://www.devdiscourse.com/article/health/3847411-revolutionizing-healthcare-jharkhands-strategic-tele-icu-network-expansion)) | Karnataka: ₹30 crore for tele-ICU across 183 facilities ([D6-01-F13](https://www.digitalhealthnews.com/karnataka-expands-e-health-network-with-paperless-hospitals-tele-icu-across-183-govt-facilities)) | State budgets | Specialist time at the hub; no step automation found |
| Dozee MillionICU | Contactless ward monitoring; step-down beds ([D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/)) | 6,000 beds in about 140 public hospitals planned (search summary only) ([D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/)) | Development finance, hospitals | Its own study found 19-42% specificity ([D5-01-F01](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full)), so many alarms; no ICU protocol layer |
| Cadence, US | Protocol-bound medicine changes at home, 24/7 team ([D5-01-F11](https://www.ynhhs.org/patient-care/digital-health/connected-care)) | 100,000+ patients; $100M Series C, Jun 2026 (THEIR CLAIM) ([D2-06-F1](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/), [D2-06-F2](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/)) | US health systems | Not in India, not in hospital |

Three facts about Cloudphysician matter for the pitch:

- One intensivist covers "60 to 80 patients" on its platform (2020 report, search summary only) ([D6-02-F04](https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution)). That is the number to beat.
- It claims "up to 40% decrease" in ICU deaths. NITI's page carries a disclaimer that it does not validate submissions ([D6-02-F02](https://frontiertech.niti.gov.in/story/cloudphysicians-radar-system-delivers-24-7-critical-care-anywhere-in-india)). No peer-reviewed Cloudphysician outcome paper was found.
- It raised $10.5 million in Jun 2024, led by Peak XV, and is eyeing "10% of the Indian critical care market" (THEIR CLAIM) ([D6-02-F03](https://inc42.com/?p=464235)).

10BedICU's field problems are a free list of design requirements ([D6-02-F06](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages)):

- slow government decisions and sites not ready
- internet and electricity not always available
- unclear tele-ICU rules
- rural hospitals often lacking an operating theatre, blood bank, dialysis or radiology

**So what for us (OUR VIEW).** Do not pitch "AI cameras in the ICU". Cloudphysician owns that sentence. Pitch the loop (section 3) and the government block as the buyer, where Cloudphysician is weakest.

## 3. The gap: what neither Cloudphysician nor Cadence does

This section shows the layers of the combined product and who already covers each.

| Layer | Cloudphysician | 10BedICU and state hubs | Cadence | This idea (OUR DESIGN) |
|---|---|---|---|---|
| Fitted in while the block is built | Fitted later | Equipment donated to existing hospitals | Not applicable | A tele-ready spec written into the build: network points, camera mounts, a local server, backup power |
| Remote specialist | Yes | Yes, from medical colleges | Not in hospital | Yes, but only for exceptions: hard stops and requests to leave the protocol |
| Treatment steps from written protocols, approved by a clinician | None published | None found | Yes, at home, for chronic disease ([D3-06-F31](https://www.cadence.care/post/cadences-hypertensionos-software-selected-for-fdas-tempo-to-advance-hypertension-care)) | Yes, for acute ICU protocols |
| Reads any monitor by camera | Not stated | Monitor integration at Nagaland spokes ([D6-02-F08](https://ipr.nagaland.gov.in/node/10455)) | Not applicable | Yes, so mixed-brand government monitors need no paid integration |
| Ward early warning before the ICU | No | No | No | Yes: the shared vitals station from the earlier idea check |
| Transfer to a higher centre | Claims fewer transfers | Not found | No | Finds a centre that can take the patient, warns it, sends the case, tracks the trip |
| Follow-up at home | No | No | Yes, in the US | Yes: the warfarin, heart-failure and BP loops already designed |

**So what for us (OUR VIEW).** The defensible core is the protocol engine with time-to-action logging. Cameras and the specialist network are needed, but anyone can buy them.

## 4. The product

Six parts, all OUR DESIGN.

1. **Tele-ready build spec.**
   - A two-page specification that state NHM engineers and architects add to the block's drawings: network points, camera mounts, a server room with backup power, and monitor ports.
   - Cost now is a line item. Cost later is a retrofit.
   - This keeps your "before construction" idea and makes it sellable.
2. **One standard bed kit.**
   - One camera per bed, pointed at the monitor and the bed area. It reads the monitor's screen, so any brand works.
   - A preprint reads heart rate, SpO2 and arterial BP from screens with above 98.9% accuracy, on 6,498 images from Vietnamese ICUs and open datasets ([D6-02-F18](https://arxiv.org/abs/2511.23355)).
   - Extra sensors are added only when a protocol needs them.
3. **Protocol packs on the existing engine.**
   - The D2-01 engine is a pure decision function. It only picks steps written in a YAML protocol file, quotes the source line for every step, refuses to run any rule left blank, and needs a clinician's approval before anything reaches the patient.
   - The ICU packs are new files on the same engine (section 5).
4. **The 90-second specialist card.**
   - It is only for exceptions: a hard stop named in the protocol file, targets still missed after the steps the file allows, or the duty doctor asking to leave the protocol. Routine steps are the on-site duty doctor's one tap on the bed tablet, so most steps never reach a specialist (section 7).
   - It shows the trend since admission, the frames that support the proposal, the proposed step with its protocol line, and the reason. Approve, change or call, in one tap.
   - The service is measured on specialist minutes per decision and patients per specialist, against Cloudphysician's 60-80 ([D6-02-F04](https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution)).
5. **Escalation and transfer.**
   - When the protocol hits a hard stop that the hospital cannot handle (no ventilator, no dialysis, surgery, cath lab), the system lists the nearest centres that can, warns the chosen one with the full case, and logs the time to departure and arrival.
   - The snakebite guideline already ties referral to "availability of ASV, ventilation facility, hemodialysis facility" ([D6-03-F01](https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf)).
6. **Before and after the ICU.**
   - Ward rounds with the shared vitals station catch patients before they crash.
   - After discharge, home loops follow them: warfarin for valve patients, heart failure and BP, already designed in the D2 and D5 notes.
   - In rural Chhattisgarh, 30% of warfarin patients travelled more than 150 km to the clinic ([D5-02-F04](https://nmji.in/letter-from-ganiyari-4/)). A loop that follows them home is part of the same service.

**One night in a district ICU (EXAMPLE, no real patient, no doses shown):**

1. 02:10. A 34-year-old farmer arrives after drinking pesticide. The duty doctor (a GDMO, not an intensivist) opens the organophosphate pack on the tablet.
2. The bed camera reads the monitor. The nurse taps in pupils and chest sounds from a checklist.
3. The engine proposes the first atropine step from the protocol file, with the check time and the targets the file names. This is a routine step, so it goes to the duty doctor, not the specialist. The duty doctor approves it on the tablet at 02:12; the log records 2 minutes from proposal to approval.
4. The nurse gives the dose and the countdown runs. At 02:17 the check finds the targets not met, so the engine proposes the next (doubled) step. The duty doctor approves, the nurse gives it, and the loop repeats until the targets are met. The engine then proposes the infusion from the file, and the duty doctor approves that too. No specialist has been called.
5. 03:40. Breathing slows: a hard stop written into the pack, so this is an exception. The remote specialist's phone shows the card: heart-rate and breathing trend, two monitor frames, the steps given so far, and the hard stop with its source line. The specialist joins by video and decides to transfer; the duty doctor confirms the order. The system lists the nearest hospital with a free ventilator and warns it.
6. 08:00. The case summary and the PMJAY claim papers are already written from the log; the duty doctor reviews and signs them.
7. Specialist time for the whole night: one call. This is what lets one specialist cover many beds (target above 80, section 9).

## 5. Protocol packs

This section shows the first packs and where each rule comes from. Each pack is a YAML file. Every number carries its source text; a blank rule stops the engine until the clinical lead fills it in, as in D2-01.

| Pack | Written source | Timed checks the engine runs | What it proposes (on-site doctor approves) | Hard stops to the specialist |
|---|---|---|---|---|
| Snakebite | MoHFW Standard Treatment Guidelines, 2016 ([D6-03-F01](https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf)) | 20-minute clotting test "every 1 h from admission for three hours and then 6 hourly for 24 hours"; recheck 6 hours after the loading dose; bleeding check 1 hour after the first 10 vials | Repeat antivenom on the guideline's criteria; neostigmine trial steps with the stop rules "after 3 doses" | Paralysis needing a ventilator; 30 vials given ("reconsider"); no ventilator or dialysis on site, so referral |
| Pesticide (organophosphate) poisoning | Bangladesh RCT, 156 patients: rapidly increasing doses plus infusion against bolus dosing ([D6-03-F02](https://pmc.ncbi.nlm.nih.gov/articles/PMC3550249/)) | Check every 5 minutes until signs of atropinisation, then review the infusion every 15 minutes, as in the trial | Next (doubled) atropine step, then an infusion set from the loading total; restart lower after toxicity | Breathing failure; signs of atropine toxicity |
| Sepsis | Surviving Sepsis hour-1 bundle (search summary only) ([D6-03-F03](https://sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients)) | Lactate, remeasured if above 2 mmol/L; mean BP against 65 mm Hg | Cultures, antibiotics, 30 mL/kg fluid for low BP or lactate of 4 or more; start a vasopressor if low BP persists | Low BP despite a vasopressor; breathing failure |
| Heart attack (STEMI) | Tamil Nadu hub-and-spoke programme ([D6-02-F17](https://pmc.ncbi.nlm.nih.gov/articles/PMC5814984/)) | ECG sent to the hub; time since symptoms began | Clot-busting drug at the spoke when far from a hub, then transfer for angiography | Shock; failed clot-busting |
| Eclampsia (next) | Indian skilled-birth-attendant guidance: magnesium sulphate before referral ([D6-03-F04](https://pmc.ncbi.nlm.nih.gov/articles/PMC6020005)) | NOT OPENED: the national regimen and its checks | Not written until the guideline is read | Not written |

The trial evidence for the poisoning pack: time to stable fell from a mean of 151.74 to 23.90 minutes. Deaths were 18 of 80 against 6 of 75 (22.5% against 8.0%). Atropine toxicity was 28.4% against 12.0%. One hospital, open-label ([D6-03-F02](https://pmc.ncbi.nlm.nih.gov/articles/PMC3550249/)).

**So what for us (OUR VIEW).** Snakebite is the best first file. It is a national government text, it is already a timed loop, and a missed 6-hour recheck is exactly the step a stretched night shift skips. Sepsis is the biggest group and the strongest pitch number (29.3%, [D6-01-F08](https://pmc.ncbi.nlm.nih.gov/articles/PMC8645819/)).

## 6. Cameras and microphones: what they are for

This section keeps the parts of the original sensor plan that have evidence and drops the rest.

| Use | Keep? | Why |
|---|---|---|
| Reading the monitor screen | Yes, core | Works in a preprint ([D6-02-F18](https://arxiv.org/abs/2511.23355)); lets any monitor feed the system |
| Video for remote rounds | Yes, on demand | Standard in tele-ICU ([D6-02-F06](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages)); not streamed all the time |
| Frames attached to a proposal (wound, bedsore, breathing effort, skin) | Yes | The specialist sees what the engine saw. OUR DESIGN |
| Jaundice from eye or skin photos | Trend aid only | Studies of 46, 66 and 130 patients ([D6-02-F20](https://pubmed.ncbi.nlm.nih.gov/36574965/)); yellowing is usually visible only above about 2-3 mg/dL (search summary only). The lab bilirubin decides |
| Safety events (fall, line pulled out, head of bed down) | Version 2 | Needs its own validation (NOT RESEARCHED) |
| Microphone for voice notes in local languages | Yes | Cuts charting at night; Cloudphysician already has voice-to-text ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930)) |
| Microphone for alarms left ringing | Yes | Counts unanswered alarms for the audit. OUR DESIGN |
| CCTV and microphones at several angles per bed | No | Cost, and the privacy fight below |

**Privacy.**
- Haryana ordered live CCTV of PMJAY patients in ICUs and HDUs, shared with the State Health Agency, to check claims. The IMA objected that ICU patients are filmed exposed and rarely can consent ([D6-03-F06](https://medicaldialogues.in/amp/news/health/hospital-diagnostics/haryana-mandates-live-cctv-surveillance-of-icus-for-ayushman-bharat-patients-162359)).
- In 2021 the Supreme Court declined to order CCTV in every ward, citing patient privacy (search summary only) ([D6-03-F07](https://medicaldialogues.in/news/health/hospital-diagnostics/hospitals-are-not-police-stations-cant-direct-for-cctv-cameras-in-every-ward-supreme-court-82981)).

Design rules (OUR DESIGN):
- The camera faces the monitor and bed area.
- Faces are blurred on the device.
- Only events and the frames attached to proposals are stored. No raw audio is kept.

This gives the state its audit trail (care was given, at this time) without a live feed of bodies.

## 7. Rules

This section lists what applies and what remains a question for a lawyer or CDSCO.

- **Software class.**
  - ICU conditions fit the CDSCO definition of "critical": life-threatening, time-critical, for trained users ([D2-04-F05](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf)).
  - Software that proposes the next step reads as "drive clinical management", which is Class C for critical conditions. Software that acts on another device reads as "treatment", which is Class D ([D2-04-F03](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf), [D2-04-F04](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf)).
  - Product rule: propose, never act. The software never drives a pump. CDSCO confirms the class on review. OUR READING
- **Who is the doctor.**
  - Under the 2020 Telemedicine Practice Guidelines, the doctor who asks for a teleconsultation "remains the treating RMP and shall be responsible for treatment" (search summary only) ([D6-03-F05](https://iadvl-files-latest.s3.ap-south-1.amazonaws.com/academy-publications/Academy-Publications-23.pdf)).
  - AI platforms may support a doctor but "cannot... prescribe" ([D2-04-F17](https://conventuslaw.com/report/india-note-on-telemedicine-practice-guidelines/)).
  - No Indian rule lets a nurse change a dose on a standing order ([D2-04-F18](https://pmc.ncbi.nlm.nih.gov/articles/PMC8663742)).
  - So every step is a doctor's order: the local GDMO's tap, or the specialist's tap that the GDMO confirms. OUR VIEW
  - Question for counsel: can the remote specialist's approval stand as the order when the GDMO is the treating doctor?
- **Data.**
  - Most DPDP Rules duties start about May 2027: 18 months after publication on 13 Nov 2025 (OUR ARITHMETIC from [D2-04-F19](https://dpdp1.pages.dev/rule/1)).
  - Who consents for an unconscious patient's video was NOT FOUND.
- **Clinical content.** Use national texts where they exist (snakebite, [D6-03-F01](https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf)). Use a named trial where they do not, and have a named clinical lead sign each file.

## 8. Money

This section shows who can pay and a price to test.

| Payer | Why they would pay | Source |
|---|---|---|
| State NHM, for its Critical Care Blocks | Central money for staff ended in FY 2025-26; each 50-bed block budgets ₹60 lakh a year for 5 specialists and ₹26.6 lakh for non-staff costs including "teleconsultation" | [D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) |
| The hospital, from PMJAY claims | Public hospitals keep PMJAY claim money in their own or their Rogi Kalyan Samiti account; CAG's indicative staff-incentive share is 15%, and Uttarakhand allows up to 25% (search summary only) | [D6-03-F09](https://cag.gov.in/uploads/download_audit_report/2023/09_Chapter-V-064d22bab412c53.02505839.pdf) |
| State tele-ICU budgets | Karnataka: ₹30 crore across 183 facilities | [D6-01-F13](https://www.digitalhealthnews.com/karnataka-expands-e-health-network-with-paperless-hospitals-tele-icu-across-183-govt-facilities) |
| Small private hospitals | Cloudphysician's base (an older report says 90% private; search summary only) | [D6-02-F04](https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution) |
| Donors and development finance | 10BedICU's donors pay set-up costs; Dozee used British International Investment | [D6-02-F05](https://www.10bedicu.org/), [D5-01-F07](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/) |

**Price to test (ASSUMPTION):** ₹15,000 per ICU or HDU bed a month, covering hardware, software and the remote specialist service.

- **Per block:** a 50-bed block with 16 monitored beds pays ₹28.8 lakh a year (OUR ARITHMETIC: 16 x ₹15,000 x 12). That is about half the ₹60 lakh budgeted for its five specialists ([D6-01-F02](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf)), which it struggles to fill.
- **Per patient-day:** at full occupancy that is about ₹500 a day (OUR ARITHMETIC: ₹15,000 / 30). Remote monitoring was priced at $10-30 a day in 2016 ([D6-01-F09](https://www.onmanorama.com/business/news/hospitals-doctors-icu-who-indian-medical-association-village-remote-areas-india.html)).
- **Against PMJAY:** one PMJAY schedule pays about ₹8,500 for an ICU day without a ventilator (search summary only; package-specific) ([D6-03-F08](https://www.scribd.com/document/670510137/HBP-2022-003)). The monthly fee for a bed equals about 1.8 such days (OUR ARITHMETIC: 15,000 / 8,500). A bed kept open and full pays for the service many times over. OUR VIEW
- **Risk:** governments pay late. In Aug 2025, half of Haryana's empanelled private hospitals paused PMJAY over unpaid dues ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html)).

## 9. MVP: build, bench test, pilot

**Build (OUR DESIGN)**

| Part | What | Reuse |
|---|---|---|
| Monitor reader | Phone or USB camera, then a detector and OCR, as in the preprint pipeline ([D6-02-F18](https://arxiv.org/abs/2511.23355)) | Open models |
| Vitals stream and ward score | Readings every minute; NEWS2 for ward patients | Shared vitals station design |
| Protocol engine | Two new YAML files: snakebite (from the STG text) and sepsis hour-1 | D2-01 `decide()` and its test pattern |
| Specialist card | Phone web page: trend, frames, proposal, source line, one-tap approve | New |
| Nurse task list | Countdown to each timed check; marks done or missed | New |
| Audit log | Every reading, proposal, approval, action and time | D2-01 log |
| Replay data | eICU-CRD Demo: open licence, over 2,500 ICU stays from 20 hospitals ([D6-02-F22](https://physionet.org/content/eicu-crd-demo/)) | Open dataset |

**Bench tests (TARGETS)**

- **Monitor reading:** photograph at least three monitor brands under ward light and dim light. TARGET: at least 98% of heart rate, SpO2 and BP values read correctly against the screen.
- **Protocol files:** every rule quoted from the STG has a unit test, and every key in each file is read by a test. TARGET: 100%.
- **Replay:** run the sepsis file over the demo dataset. Report how many stays trigger a proposal and how early.
- **Specialist card:** 3-5 doctors each review 20 mock cards. TARGET: median under 2 minutes per decision.

**Pilot: one district ICU (about 10 beds) or one small private ICU, three months, before and after (OUR DESIGN)**

| Measure | How | Pass bar |
|---|---|---|
| Time from alert to action | Log | Better than the first-month baseline (TARGET) |
| Timed checks done on time (for example the snakebite 6-hour recheck) | Log against the protocol file | Above 90% (TARGET) |
| Specialist minutes per decision | Log | Under 2 minutes median (TARGET) |
| Patients covered per specialist | Rota and log | Above 80, beating the 60-80 Cloudphysician figure (TARGET) |
| Transfers out, and time from decision to departure | Log | Reported, and faster than baseline (TARGET) |
| ICU deaths | Register | Reported only |
| Nurse and doctor view | Short survey | Most want to keep it (TARGET) |

One ICU cannot show an effect on deaths. TELESCOPE needed 30 ICUs and still found none for remote rounds ([D6-02-F12](https://pubmed.ncbi.nlm.nih.gov/39382244/)). An outcome study comes later, across many blocks. OUR VIEW

## 10. What would kill it

- **Cloudphysician adds protocol steps.** It has the hospitals, the data and the money ([D6-02-F01](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930), [D6-02-F03](https://inc42.com/?p=464235)). Answer (OUR VIEW): sell to government blocks first, where its base is thin. Build on open CARE rather than against it ([D6-02-F07](https://github.com/ohcnetwork/care)).
- **States do not staff even the nurses and duty doctors.** Then there is no one to carry out a step. Check staffing before signing any site.
- **The Class C licence takes longer and costs more than planned** (fees and timelines NOT FOUND in D2-04).
- **Late payment** ([D5-01-F18](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html)).
- **Internet and power** ([D6-02-F06](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages)). Answer: the engine and log run on a local server, with SMS as a fallback for the specialist. OUR DESIGN
- **Missing back-up services:** no theatre, blood bank or dialysis ([D6-02-F06](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages)). This makes the transfer layer part of the core, not an extra.

## 11. Open questions

- How many Critical Care Blocks are open and staffed today, by state; the Lok Sabha PDFs did not load ([D6-01-F03](https://eparlib.sansad.in/bitstream/123456789/3017761/1/AU2281_ePmCao.pdf)).
- The case mix of district-hospital ICUs (NOT FOUND).
- Cloudphysician's price, and any peer-reviewed outcome paper (NOT FOUND).
- 10BedICU's outcome data and cost per unit (NOT FOUND).
- Whether CARE already reads monitors by camera or runs protocol steps.
- The full atropine regimen text from the trial, and the national eclampsia regimen (NOT OPENED).
- The official NHA PMJAY rates for ICU and HDU days.
- The official text of the Telemedicine Practice Guidelines (blocked again on 16 Nov 2026).
- Consent for video of unconscious patients under DPDP (NOT FOUND).
- How the monitor reader performs across brands and in dim light (bench test).

## Sources

| Fact | What the note records | Source | Read as | Claims check |
|---|---|---|---|---|
| D1-05-F1 | PHTI review: only programmes with a team that adjusts medicine gave a clinically meaningful BP fall | [phti.org](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Executive-Summary.pdf) | OPENED | CONFIRMED (earlier check) |
| D2-04-F03 | CDSCO software matrix: critical x treatment = D, drive = C, inform = B | [cdsco.gov.in](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf) | OPENED | not re-checked |
| D2-04-F04 | "Treatment" includes acting by connecting to other devices; "drive" guides next interventions | [cdsco.gov.in](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf) | OPENED | not re-checked |
| D2-04-F05 | "Critical": life threatening, time critical, for trained users | [cdsco.gov.in](https://www.cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf) | OPENED | not re-checked |
| D2-04-F17 | Telemedicine Guidelines 2020: AI cannot prescribe, may support the RMP (law-firm note) | [conventuslaw.com](https://conventuslaw.com/report/india-note-on-telemedicine-practice-guidelines/) | OPENED (commentary) | not re-checked |
| D2-04-F18 | No Indian rule found letting a nurse or CHO change a dose on a standing order | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8663742) | OPENED | not re-checked |
| D2-04-F19 | DPDP Rules 2025: Rules 3 and 5-16 start 18 months after publication (13 Nov 2025) | [dpdp1.pages.dev](https://dpdp1.pages.dev/rule/1) | OPENED (mirror) | not re-checked |
| D2-06-F1 | Cadence $100M Series C, Jun 2026, led by Spark Capital | [pulse2.com](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/) | SNIPPET | CONFIRMED (earlier check) |
| D2-06-F2 | Cadence traction claims: 100,000+ patients, 55% of alerts closed without a human | [pulse2.com](https://pulse2.com/cadence-raises-100-million-series-c-to-automate-chronic-care/amp/) | SNIPPET | CONFIRMED as THEIR CLAIM (earlier check) |
| D3-06-F31 | Cadence HypertensionOS selected for FDA TEMPO pilot; not an approval | [cadence.care](https://www.cadence.care/post/cadences-hypertensionos-software-selected-for-fdas-tempo-to-advance-hypertension-care) | OPENED | not re-checked |
| D5-01-F01 | Dozee KGMU study: specificity 19-42%; maker-funded | [frontiersin.org](https://frontiersin.org/articles/10.3389/fmedt.2024.1436034/full) | OPENED | not re-checked |
| D5-01-F07 | Dozee MillionICU with BII: 6,000 beds, about 140 public hospitals | [bii.co.uk](https://www.bii.co.uk/en/news-insight/news/dozee-partners-with-british-international-investment-to-transform-public-healthcare-in-india/) | SNIPPET | not re-checked |
| D5-01-F11 | Cadence kit: cuff, scale, 24/7 team; Medicare pays | [ynhhs.org](https://www.ynhhs.org/patient-care/digital-health/connected-care) | SNIPPET | not re-checked |
| D5-01-F18 | Haryana: 650 of 1,300 private hospitals paused PMJAY over dues, Aug 2025 | [moneylife.in](https://www.moneylife.in/article/how-patientsand-private-hospitalsare-struggling-with-ayushman-bharat/78042.html) | SNIPPET | not re-checked |
| D5-02-F04 | JSS Ganiyari: 30% of warfarin patients from over 150 km | [nmji.in](https://nmji.in/letter-from-ganiyari-4/) | OPENED | not re-checked |
| D6-01-F01 | CCB guideline 2022: 602 districts; top conditions; bed mix; monitor with central station per ICU bed | [nhsrcindia.org](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) | OPENED | CONFIRMED (C4, PDF text) |
| D6-01-F02 | CCB guideline: HR norms, HR money ends FY 25-26, unit costs, Annexure 3 staff and teleconsultation lines | [nhsrcindia.org](https://nhsrcindia.org/sites/default/files/Guidelines%20on%20Critical%20Care%20Hospital%20Block-PM-ABHIM_2022%20-%2003-11-2022.pdf) | OPENED | CONFIRMED (C4, PDF text) |
| D6-01-F03 | Lok Sabha Dec 2025: 621 CCBs, ₹18,799.21 crore; 621 also in a MoHFW release summary | [eparlib.sansad.in](https://eparlib.sansad.in/bitstream/123456789/3017761/1/AU2281_ePmCao.pdf), [2](https://mohfw.gov.in/en/press-info/9121) | SNIPPET | CONFIRMED by a second summary (C4) |
| D6-01-F04 | IMPRI Jul 2026: CCBs "only 3% completion" | [impriindia.com](https://www.impriindia.com/insights/the-next-phase-of-indias-health-system/) | OPENED | CONFIRMED as stated; IMPRI names no source (C4) |
| D6-01-F05 | "10 out of 394 units operational", no source named | [c4scourses.in](https://c4scourses.in/national-affairs/pm-abhim-funds/) | OPENED | low weight |
| D6-01-F07 | 37,834 public ICU beds incl. 9,873 paediatric | [eparlib.sansad.in](https://eparlib.sansad.in/bitstream/123456789/2987466/1/AU4360_wkfa0t.pdf) | SNIPPET | not re-checked |
| D6-01-F08 | INDICAPS-II: 4,669 adults, 132 ICUs; mortality 23.4%; sepsis 29.3%; poisoning 1.5% | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8645819/) | OPENED | CONFIRMED (C4) |
| D6-01-F09 | IMA via Reuters 2016: 8,350 specialists vs need over 50,000; $10-30 a day eICU | [onmanorama.com](https://www.onmanorama.com/business/news/hospitals-doctors-icu-who-indian-medical-association-village-remote-areas-india.html) | OPENED | CONFIRMED, 2016 figures (C4) |
| D6-01-F11 | Madhya Pradesh: about 40% of Covid ventilators unused or scrapped | [freepressjournal.in](https://www.freepressjournal.in/bhopal/madhya-pradesh-40-ventilators-from-covid-era-lying-unused-or-scrapped) | OPENED | not re-checked |
| D6-01-F12 | Himachal: 191 PM CARES ventilators unused, lack of trained staff | [pressreader.com](https://www.pressreader.com/india/hindustan-times-bathinda/20210518/281809991789472) | SNIPPET | not re-checked |
| D6-01-F13 | Karnataka: 185 ICU specialist posts; ₹30 crore tele-ICU across 183 facilities | [medicaldialogues.in](https://medicaldialogues.in/news/health/hospital-diagnostics/karnataka-to-appoint-185-specialist-doctors-at-district-and-taluk-hospitals-154995), [2](https://www.digitalhealthnews.com/karnataka-expands-e-health-network-with-paperless-hospitals-tele-icu-across-183-govt-facilities) | OPENED | not re-checked |
| D6-01-F14 | Million Death Study: about 58,000 snakebite deaths a year; 94% rural; 77% outside hospital | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7340498/) | OPENED | CONFIRMED (C4) |
| D6-01-F15 | Akhnoor: 48.96% of snakebite patients arrived after 6 hours or more | [ijmedicine.com](https://www.ijmedicine.com/index.php/ijam/article/view/2877) | SNIPPET | not re-checked |
| D6-01-F16 | NCRB 2024: 7,123 pesticide suicides in Telangana and AP, one in four of the national total | [thesouthfirst.com](https://thesouthfirst.com/health/a-cheap-herbicide-was-behind-nearly-1-in-4-suicide-deaths-in-2024-it-is-still-on-sale/) | SNIPPET | not re-checked |
| D6-01-F17 | Referred newborns: 30.1% died; no Indian trauma transfer guidelines | [doaj.org](https://doaj.org/article/c40f039c5d2e43998643b54ed3cbd482) | SNIPPET | not re-checked |
| D6-02-F01 | Cloudphysician: RADAR tools; 1,30,000+ patients, 280 hospitals | [thebetterindia.com](https://thebetterindia.com/health-care/cloudphysician-founders-dhruv-joshi-dileep-raman-smart-icu-in-a-box-remote-critical-care-rural-india-10884930) | OPENED | CONFIRMED as THEIR CLAIM (C4) |
| D6-02-F02 | NITI page: 480 hospitals; "up to 40% decrease" in ICU deaths; NITI disclaimer | [frontiertech.niti.gov.in](https://frontiertech.niti.gov.in/story/cloudphysicians-radar-system-delivers-24-7-critical-care-anywhere-in-india) | OPENED | not re-checked |
| D6-02-F03 | Cloudphysician Series A $10.5M, Peak XV, Jun 2024 | [inc42.com](https://inc42.com/?p=464235) | OPENED | not re-checked |
| D6-02-F04 | One intensivist covers 60-80 patients (2020); 90% private (older report) | [yourstory.com](https://yourstory.com/socialstory/2020/08/tele-icu-monitoring-services-shortage-solution) | SNIPPET | not re-checked |
| D6-02-F05 | 10BedICU: 216 units, 15 hubs; states pay running costs | [10bedicu.org](https://www.10bedicu.org/) | OPENED | not re-checked |
| D6-02-F06 | 10BedICU field problems: internet, power, missing theatre, blood bank, dialysis | [thinkglobalhealth.org](https://www.thinkglobalhealth.org/article/10-bed-icu-brings-intensive-care-units-indias-rural-towns-and-villages) | OPENED | not re-checked |
| D6-02-F07 | CARE: MIT licence; video feed and vitals monitoring | [github.com](https://github.com/ohcnetwork/care) | OPENED | not re-checked |
| D6-02-F08 | State tele-ICU hubs: Jharkhand, Nagaland, Meghalaya, J&K | [devdiscourse.com](https://www.devdiscourse.com/article/health/3847411-revolutionizing-healthcare-jharkhands-strategic-tele-icu-network-expansion) | SNIPPET | not re-checked |
| D6-02-F12 | TELESCOPE, JAMA 2024: 30 ICUs, 17,024 adults; stay 8.1 vs 7.1 days, P .24 | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39382244/) | OPENED (abstract) | CONFIRMED (C4) |
| D6-02-F13 | Lilly, JAMA 2011: hospital mortality 13.6% to 11.8%; adherence rose | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/21576622/) | OPENED (abstract) | not re-checked |
| D6-02-F16 | TREWS, Nat Med 2022: alert confirmed within 3 h linked to lower mortality | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/35864252/) | OPENED (abstract) | not re-checked |
| D6-02-F17 | TN-STEMI: 4 hubs, 35 spokes, 2,420 patients; one-year mortality 17.6% to 14.2% | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5814984/) | OPENED | CONFIRMED (C4) |
| D6-02-F18 | Monitor-reading preprint: 6,498 images; above 98.9% for HR, SpO2, arterial BP | [arxiv.org](https://arxiv.org/abs/2511.23355) | OPENED | CONFIRMED; plan wording CORRECTED (C4) |
| D6-02-F20 | Eye-photo jaundice studies: 46, 66 and 130 patients | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/36574965/) | OPENED (abstracts) | not re-checked |
| D6-02-F22 | eICU-CRD Demo: open licence, over 2,500 stays, 20 hospitals | [physionet.org](https://physionet.org/content/eicu-crd-demo/) | OPENED | not re-checked |
| D6-03-F01 | MoHFW snakebite STG 2016: clotting-test timing, repeat-dose and referral rules | [clinicalestablishments.mohfw.gov.in](https://clinicalestablishments.mohfw.gov.in/sites/default/files/standard-treatment-guidelines/3941.pdf) | OPENED | CONFIRMED (C4, PDF text) |
| D6-03-F02 | Atropine RCT, Bangladesh: 151.74 vs 23.90 minutes; deaths 22.5% vs 8.0%; regimen doubles every 5 minutes, then infusion | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3550249/) | OPENED | CONFIRMED (C4) |
| D6-03-F03 | Sepsis hour-1 bundle elements | [sccm.org](https://sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients) | SNIPPET | not re-checked |
| D6-03-F04 | Indian guidance: magnesium sulphate before referral | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6020005) | SNIPPET | not re-checked |
| D6-03-F05 | Telemedicine Guidelines: requesting RMP remains the treating RMP | [iadvl-files-latest.s3.ap-south-1.amazonaws.com](https://iadvl-files-latest.s3.ap-south-1.amazonaws.com/academy-publications/Academy-Publications-23.pdf) | SNIPPET | not re-checked |
| D6-03-F06 | Haryana live ICU CCTV order for PMJAY patients; IMA objections | [medicaldialogues.in](https://medicaldialogues.in/amp/news/health/hospital-diagnostics/haryana-mandates-live-cctv-surveillance-of-icus-for-ayushman-bharat-patients-162359) | OPENED | not re-checked |
| D6-03-F07 | Supreme Court 2021 declined CCTV in every ward | [medicaldialogues.in](https://medicaldialogues.in/news/health/hospital-diagnostics/hospitals-are-not-police-stations-cant-direct-for-cctv-cameras-in-every-ward-supreme-court-82981) | SNIPPET | not re-checked |
| D6-03-F08 | PMJAY HBP 2022 schedule: ICU without ventilator ₹8,500-8,800 a day | [scribd.com](https://www.scribd.com/document/670510137/HBP-2022-003) | SNIPPET | not re-checked |
| D6-03-F09 | Public hospitals keep PMJAY claim revenue; staff incentive 15% (CAG) or up to 25% (Uttarakhand) | [cag.gov.in](https://cag.gov.in/uploads/download_audit_report/2023/09_Chapter-V-064d22bab412c53.02505839.pdf) | SNIPPET | not re-checked |

## How this note was made

Facts come from three research notes written on 16 Nov 2026:

- `research_notes\dtx\D6-01 Smart ICU - need, Critical Care Blocks and staffing.md`
- `D6-02 Smart ICU - players and evidence.md`
- `D6-03 Smart ICU - protocols, rules and money.md`

It also reuses facts from the D1, D2, D3 and D5 notes.

Two government PDFs were read in full by extracting their text: the Critical Care Block guideline (2022) and the snakebite treatment guideline (2016).

Trial abstracts were read through Europe PMC, because PubMed pages required cookies. Sansad (Lok Sabha) PDFs, PIB and the official Telemedicine Guidelines did not load, so those facts are marked as search summaries.

A claims check re-opened key sources after writing; see `research_notes\dtx\C4-corrections-log.md`.
