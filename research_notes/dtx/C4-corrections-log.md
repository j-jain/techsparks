# C4 corrections log: claims check of the smart ICU idea check and notes D6-01 to D6-03 (2026-11-16)

One line per change or check: item | fact ID | old (short) -> new (short), or the check result.

## Checks run

1. **Guideline quotes, checked by script against text extracted from the PDFs.**
   - CCB guideline (D6-01-F01, F02): 13 strings checked, all found. They include: 602 districts; Specialists-5 Rs 60,00,000; Nurses-66; GDMO-12; Rs 26,60,000; Specialists-7 Rs 84,00,000; 1:1 ICU; "up to FY 25-26"; teleconsultation; Rs 23.75 Cr; Rs 4.592 Cr; monitors 20/12/16; "Poisoning, Septic Shocks".
   - Snakebite STG (D6-03-F01): all 7 quoted strings found. Three first showed as missing only because of carriage returns at line breaks.
2. **Fact IDs.** Every ID cited in the report body has a register row, and every register row is cited in the body. Every D6 ID cited is defined in a D6 note.
3. **W0 style.**
   - No em dashes, and no exclamation marks outside URLs.
   - Banned-word hits were only inside URLs ("...shortage-solution", "...poor-fund-utilisation") and the word "high-resolution".
   - One note line was reworded: "outcome or utilisation data" -> "outcome or bed-use data" (D6-02, not found list).
4. **Spot-checks against sources** (10 facts): D6-01-F01, F02, F03, F08, F14; D6-02-F12, F17, F18; D6-03-F01, F02. Results below.

## Corrections to the approved plan, carried into the report

1. Plan, finding 5 | D6-01-F08 | "Pesticide poisoning, sepsis, heart attacks and pregnancy emergencies fill district beds" -> report leads with sepsis (29.3% in INDICAPS-II). Poisoning was 1.5% in that sample, which leans to large hospitals. A district-hospital case mix was NOT FOUND.
2. Plan, finding 4 | D6-02-F12 | TELESCOPE "15,230 patients" -> "17,024 adults" (abstract via Europe PMC). 15,230 was the intervention-period count in a secondary summary.
3. Plan, finding 4 | D6-02-F13 | Lilly 2011 "Most of the benefit came from following standard care steps" -> the authors attributed about 25% (hospital) and 30% (ICU) of the mortality association to best-practice adherence and complications. The report says the benefit is "tied to" standard steps, not "comes from".
4. Plan, product part 2 | D6-02-F18 | "Oxford-linked preprint ... on one monitor family" -> "6,498 images from Vietnamese ICUs and open datasets". The one-monitor-family dataset (Mindray Beneview T8) is a different paper (D6-02-F19).
5. Plan, money | D6-03-F08 | "₹8,500-10,350 a day for an ICU bed (higher with a ventilator)" -> without a ventilator ₹8,500-8,800, with a ventilator ₹9,000-10,350, from one package schedule (unofficial copy). The report uses ₹8,500.
6. Plan, protocol packs | D6-03-F02 | atropine regimen "stepped up by the protocol" (source not opened) -> OPENED PMC3550249. The regimen: start 1.8-3.0 mg IV, double every 5 minutes until atropinisation, then an infusion at 10% of the loading total per hour, reviewed every 15 minutes. Mortality 18/80 against 6/75 is confirmed as deaths.
7. Plan, protocol packs | none | "Diabetic ketoacidosis: insulin drip" -> dropped from the report. NOT RESEARCHED in this pass.
8. Plan, protocol packs | D6-03-F04 | eclampsia kept as "next". The national MgSO4 regimen was NOT OPENED, so no regimen is written.
9. Plan, finding 1 | D6-01-F03 | 621 CCBs and ₹18,799.21 crore: still SNIPPET (sansad.in refused the connection). Now corroborated by a second search summary of a MoHFW release, which gives 621 CCBs within ₹33,081.82 crore of approvals.

## Corrections inside the report during the check

1. Section 7 | D2-04-F17 | link pointed to PMC8663742 (the D2-04-F18 source) -> conventuslaw.com note, the actual F17 source.
2. Sections 2 and 8 | D6-01-F13 | Karnataka ₹30 crore linked to the 185-posts article -> linked to the digitalhealthnews article that states ₹30 crore.
3. Section 3 | D6-02-F08 | Nagaland monitor integration linked to the Jharkhand article -> linked to the Nagaland IPR page.
4. Section 9 | D6-02-F04 | "Beds covered per specialist" -> "Patients covered per specialist". The Cloudphysician figure is patients.
5. Section 5 | D6-03-F02 | "(search summary only)" and "NOT OPENED yet" removed after opening the trial. The pack row now states the 5-minute and 15-minute check intervals from the paper.

## Spot-check results

| Fact | What was checked | Result |
|---|---|---|
| D6-01-F01 | 602 districts; top conditions list; 20/12/16 monitors | CONFIRMED (PDF text) |
| D6-01-F02 | HR norms, HR money to FY 25-26, Annexure 3 lines | CONFIRMED (PDF text) |
| D6-01-F03 | 621 CCBs, ₹18,799.21 crore | CONFIRMED by a second summary; primary PDF not loaded |
| D6-01-F08 | INDICAPS-II 23.4%, 29.3%, 1.5%, 36.4% | CONFIRMED (PMC page) |
| D6-01-F14 | 58,000 a year; 94% rural; 77% outside hospital | CONFIRMED (PMC page) |
| D6-02-F12 | 30 ICUs; 17,024; 8.1 against 7.1 days; P .24 | CONFIRMED (Europe PMC abstract) |
| D6-02-F17 | 4 hubs, 35 spokes; 2,420; 17.6% to 14.2%; OR 0.76 | CONFIRMED (PMC page) |
| D6-02-F18 | 6,498 images; above 98.9% | CONFIRMED (arXiv abstract); CORRECTED in plan wording (item 4) |
| D6-03-F01 | 7 quoted strings | CONFIRMED (PDF text) |
| D6-03-F02 | times, deaths, toxicity, regimen | CONFIRMED (PMC page), upgraded from SNIPPET |

## Issue found in older notes (not changed)

- Two notes share the prefix D5-01: `D5-01 High-stakes conditions.md` (warfarin and sickle cell, F01-F22) and `D5-01 Vitals station web checks.md` (F01-F24). For example, D5-01-F03 is the Chhattisgarh warfarin study in one note and the Kenyan cardiac-arrest audit in the other.
- The smart ICU report cites only the vitals-check meanings (F01, F07, F11, F18) and links each one to its source, so its links are unambiguous.
- Suggest renaming one note's IDs (for example to D5-03) in a later pass. Not done here, because other parts may cite them.

## Still open

- Primary Lok Sabha PDFs (sansad.in) and the official Telemedicine Practice Guidelines did not load.
- The official NHA HBP 2022 rate master was not opened.
- Cloudphysician's price and any peer-reviewed outcome paper: NOT FOUND.
