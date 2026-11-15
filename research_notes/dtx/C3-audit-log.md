# C3 audit log: final consistency and claims audit of all parts (2026-11-13, about 11:05 PM)

Scope: all 18 parts in `report-parts\dtx\`, read in full; claims checks D3-01, D3-02 and D3-03 applied to 10-challenge, 60-strategy and 80-build (not covered by C1 or C2); combined "never say" list applied to every part; cross-part consistency on the items in the audit brief; numbers without a source (check_report.py). 80-build.md was read last; it had not changed since 22:56:04 when read and edited (edits from 23:03).

One line per change: part | what | old (short) -> new (short).

## Combined "never say" list used
From D3-01: "self-monitoring plus dose changes cut BP by 6.1"; STRONG-HF 15.2% vs 23.3% as raw counts; "25% of Trivandrum heart-failure patients"; "COBRA-BPS health workers changed doses"; "both HF telemonitoring trials had no therapy change"; "adherence rose from 30% to 84%"; "3.3% of mental-health app users stay to day 30"; "the China result is the protocol alone"; "warfarin self-dosing beats self-testing" head to head; a Propeller shutdown date or "ResMed closed Propeller 31 Jan 2019"; "PHTI says digital diabetes tools fail" without scope.
From D3-02: "32.9% controlled" in one cascade; "1:778"; any BeatO revenue; a Twin Health 2026 round or US$1.4B; My Dose Coach 295/684; "only two Class C products in India".
From D3-03: "ADA 2026 says 2 units every 3 days"; "Teladoc wrote down Livongo by $13.4B"; "$1,195 a course" (Pear $6M and $130M kept with D1-02-F42, per ruling); "Cadence's AI resolves 55% of dose changes"; Cadence or Nourish valuations; "Simple has no step logic anywhere"; "omblepy is open-source licensed"; "the control rates are home readings"; "DPDP consent duties start 12 May 2027" without the caveat.

## 03-read-this-first.md
1. 03 | D1-01-F05 never say | "intensive support that included dose changes it moved 6.1" -> "intensive support (dose changes by doctors, pharmacists or patients, plus education or counselling) it moved 6.1"

## 05-decision-brief.md
1. 05 | citation form | "(D1-01-F09, F38)" -> "(D1-01-F09, D1-01-F38)"
2. 05 | citation form | "(D1-01-F32, F33)" -> "(D1-01-F32, D1-01-F33)"
3. 05 | D1-03-F10 consistency | "control rose from 26.3% to 59.8%" -> adds "with no comparison group"
4. 05 | D1-03-F09 (D3-02 wording) | "9.8% of diabetics and 35.4% of hypertensives are controlled" -> "control rates were 9.8% for diabetes and 35.4% for hypertension"
5. 05 | D1-03-F16 wording | "79.9% of posts vacant in four specialities" -> "79.9% of required posts in four specialities unfilled"
6. 05 | citation range (writer rule 2) | "(D1-04-F02 to F07)" -> six full IDs
7. 05 | D1-06-F14 (D3-03 corrected rules) | "referral rules for very high readings and pregnancy" -> adds lab values before raising telmisartan, abnormal-lab referral, childbearing age without effective contraception, adults over 30
8. 05 | D1-04-F15 THEIR CLAIM, citation form | "Lupin already holds ... (D1-02-F07, F54)" -> "Lupin says it already holds ... (D1-02-F07, D1-02-F54)"
9. 05 | reading-route ruling | "read the cuff (Bluetooth, or a phone photo of any cheap cuff's screen)" -> "a phone photo of any cuff's screen, with the person confirming the digits; typed entry as fallback; Bluetooth only if a suitable cuff is in hand"

## 10-challenge.md (first claims-check pass for this part)
1. 10 | D1-01-F05 never say | B2 row "intensive support that included dose changes: 6.1" -> "intensive support (dose changes by doctors, pharmacists or patients, plus education or counselling): 6.1"
2. 10 | D1-01-F05 never say | B6 rule 1 "intensive support that included dose changes, education or counselling, 6.1" -> same corrected wording plus "not dose changes alone"
3. 10 | D1-02-F05 never say (head to head) | "those who left the dose to the clinic did not (0.94)" -> adds "the two approaches were not compared head to head"
4. 10 | D1-06-F40 never say | "Simple app stores each protocol as a drug list with no step ladder" -> "the protocol model ... stores a drug list and follow-up days, and no step ladder was found in it"
(Already correct in this part, no edit: D1-03-F16 wording in B2 and B8; D1-01-F32/F33 "without a mandated dose protocol"; D1-01-F27 adjusted estimates and side effects; D1-02-F59 pillboxes or labels; D1-02-F41 Teva wording; D1-03-F09 denominator; Pear $6M and $130M with D1-02-F42; China drugs and incentives; mWellcare 40 centres, 3,698, 0.98 mmHg, not significant.)

## 20-burden.md
1. 20 | numbers without source | IHCI survey table rows "52.4% | 58.5% | +6.1" etc. -> IDs added (D1-01-F10, D1-03-F12, D1-01-F11); +6.1 and +3.9 tagged OUR ARITHMETIC; +6.7 cited D1-03-F12
2. 20 | numbers without source | C5 shortfall table rows -> [D1-03-F16] added to each share cell

## 30-doctor.md
1. 30 | number without source | "already produced a 13 mmHg fall." -> adds [D1-01-F46]
2. 30 | cross-part conflict (CureApp HT price) | "about 8,000 yen ... search summary only [D1-01-F57]" -> adds "the company's June 2026 release gives 7,010 yen for the app as an insured material (THEIR CLAIM) [D2-04-F43]"

## 55-money.md
1. 55 | untagged DT3 figures | TAM/SAM/SOM table rows -> "(OUR ARITHMETIC)" in the first cell
2. 55 | untagged DT3 figures | SOM year table revenue cells -> "(OUR ARITHMETIC)"
3. 55 | untagged DT3 figures | "52.7 lakh ... (52,71,253)" and "1.3 times the SAM" -> "(OUR ARITHMETIC)"
4. 55 | Indian number grouping (writer rule) | "785,417 / 392,708 / 340,136 / ₹9,425,000,000" -> "7,85,417 / 3,92,708 / 3,40,136 / ₹9,42,50,00,000"
5. 55 | untagged DT3 figures | price-sensitivity rows -> "(OUR ARITHMETIC)"
6. 55 | untagged figures | so-what "₹149" -> "(ASSUMPTION)"; "SAM ₹749 crore ... test fails" -> "(OUR ARITHMETIC)"

## 60-strategy.md (first claims-check pass for this part)
1. 60 | D1-03-F24 date | "A consultation lasts about 2 minutes (2013-2015)" -> "lasted"
2. 60 | untagged | "test ₹99, ₹149 and ₹299 a month (DT3)" -> "(ASSUMPTION, DT3)"
3. 60 | untagged | "misses US$100 million a year on our model (DT3)" -> "(OUR ARITHMETIC, DT3)"
4. 60 | D3-03 never say (control rates are home readings) | "70-76% were controlled on the first pill" -> adds "on clinic readings"
(Checked, no edit needed: Simple "protocol model has no step ladder" matches D3-03; telemedicine direct delivery; fund led Wellthy June 2023, CureApp first investment 2015; Pear "won too few payers and prescribers"; Cadence in FDA pilot, not cleared, no valuation; Closed Loop liquidation and single-arm trial; all DT3 figures match.)

## 70-funded.md
1. 70 | wrong fact ID | Biobeat row "Omron cuff about ₹2,600 (search summary only) [D1-06-F07]" -> [D1-06-F31] (F07 is omblepy; F31 is the price)

## 80-build.md (first claims-check pass for this part)
1. 80 | D1-04-F10 (D3-02 corrected, opened) | "arrived in March 2026 (search summary only)" -> "arrived on 20-21 March 2026"
2. 80 | D1-03-F10 consistency | Card 1 "control rose from 26.3% to 59.8%" -> adds "with no comparison group"
3. 80 | D1-06-F40 never say | Card 1 "The government's Simple app has no step logic" -> "The protocol model ... stores a drug list and follow-up days, and no step logic was found in it"
4. 80 | DT3 contradiction | TAM bottom-up "₹11,264 crore (630.0 lakh ...)" -> "₹9,969 crore (557.5 lakh ...)"
5. 80 | untagged DT3 figures | market table rows -> "(OUR ARITHMETIC)" in the first cell
6. 80 | D2-05-F17 (D3-02 corrected) | "₹3,906 a private patient spends on them a year (2019-20 prices)" -> adds "a modelled price for one brand pill a day"
7. 80 | untagged | "1.3 times the SAM." -> "(OUR ARITHMETIC)"
8. 80 | D1-03-F02, D2-05-F38 (D3-02 upgraded and corrected) | "rest on inputs seen only in search summaries" -> "rest on a 2021 projection ..., not a count [D1-03-F02], and on assumed shares of registered doctors [D2-05-F38]"
9. 80 | D1-06-F50 (D3-03 corrected) | "22 UK patients, 2,054 patient-days" -> adds "of which 1,099 have peak-flow readings"
10. 80 | untagged price | S.M.A.R.T statement "₹149 a patient a month [M]" -> "(ASSUMPTION)"
11. 80 | D1-03-F10 consistency | S.M.A.R.T "R" line -> adds "with no comparison group"
12. 80 | D1-06-F14 (D3-03 corrected rules) | feature table safety branches "very high reading, pregnancy, tests before telmisartan 80 mg, referral after the last step" -> adds childbearing age without contraception, abnormal lab referral, patients outside the population or with the sheet's other conditions sent to the doctor
13. 80 | contradiction with 55 (D3-07-F20) | Messages "WhatsApp's price in India is NOT RESEARCHED" -> "third-party copies of WhatsApp's India prices are in part F2 [D3-07-F20]"
14. 80 | D1-06-F40 never say | moat "Simple app has no step logic today" -> "No step logic was found in the protocol model of ... Simple app"
15. 80 | D2-04-F17 (D3-03 corrected) | "A law-firm note ... says only a registered doctor prescribes" -> "The telemedicine guidelines (clause 5.4) say only a registered doctor may counsel or prescribe, and the final prescription has to be delivered directly by that doctor"
16. 80 | reading-route ruling | open decision "Photo with a confirm step; Bluetooth; typed" -> "Photo with a confirm step (tonight's route); typed entry as fallback; Bluetooth only if a suitable cuff is in hand"
17. 80 | regulation consistency | "device class A, B or C" -> "likely device class A or B, depending on how hypertension is graded (C if read as treatment)"
18. 80 | untagged | pilot design "about 300 patients" -> "(OUR DESIGN)"
19. 80 | untagged | price options "₹99, ₹149 or ₹299" -> "(ASSUMPTION)"
20. 80 | untagged | so-what "test that fails in India alone" -> "(OUR ARITHMETIC)"
21. 80 | home-threshold consistency | open decision "135/85, the home line in European guidance" -> adds "(applying it to a clinic protocol is OUR DESIGN)"
(Checked, no edit needed: scores 4.35/3.35/3.35/3.10/3.05/2.90/2.70; China caveat; STRONG-HF adjusted and 1,078 patients in 14 countries [D1-01-F27]; TELE-HF/BEAT-HF "without a mandated dose protocol"; warfarin not head to head; ADA "2025"; data-law date with caveat; heart-failure sales ₹1,519 crore is in D2-05-F01; unit economics; ₹1 crore arithmetic.)

## 85-mvp.md
1. 85 | untagged | results table "(iv) ... 3 people x 10 cards" -> "(OUR DESIGN)"
2. 85 | untagged | simulation table rows -> "(OUR SIMULATION)" in the first cell
3. 85 | untagged | "With 20% drop-out" -> "(ASSUMPTION)"
4. 85 | untagged | "D2-01's earlier sketch was about 300 patients" -> "(OUR DESIGN)"
5. 85 | untagged | budget total "about ₹4.35-5.40 lakh" -> "(OUR ARITHMETIC)"
6. 85 | untagged | so-what "about 434 patients" -> "(OUR ARITHMETIC)"

## 95-recommendation.md
1. 95 | reading-route ruling | "Photo of any cuff's screen; Bluetooth cuff; typed" -> photo with the person confirming (tonight's route); typed fallback; Bluetooth only if a suitable cuff is in hand
2. 95 | home-threshold consistency | "135/85 at home for a protocol written for 140/90 in clinic [D2-01-F1]" -> adds [D1-06-F14] and "applying the clinic protocol to home readings is OUR DESIGN"
3. 95 | D1-04-F15 THEIR CLAIM | "an Indian Class C licence is already held" -> "Lupin says it already holds an Indian Class C licence"

## 99-method.md
1. 99 | stale reference | "the corrections log (`C1-` files)" -> "the corrections and audit logs (`C1-` to `C3-` files)"

## Counts
- 00-head.md: 0
- 03-read-this-first.md: 1
- 05-decision-brief.md: 9
- 10-challenge.md: 4
- 20-burden.md: 2
- 25-voice.md: 0
- 30-doctor.md: 2
- 35-scale.md: 0
- 40-engineer.md: 0
- 50-players.md: 0
- 55-money.md: 6
- 60-strategy.md: 4
- 70-funded.md: 1
- 80-build.md: 21
- 85-mvp.md: 6
- 90-mentor.md: 0
- 95-recommendation.md: 3
- 99-method.md: 1
- Total: 60

## Final check_report.py output (after edits)
- link_facts.py: no fact ID cited that is missing from the notes (587 cited, 803 indexed).
- Numbers without a source or tag: 10 lines, all acceptable: 3 table header rows (price sensitivity, channel guillotine, simulation); 1 test-case table row (T35, T36); 1 schedule row (05:30-07:00); 3 lines in the verbatim thesis quote; 1 "What we could not find" item in 20-burden ("Doctors per 1,000 people, rural against urban", a gap, no figure claimed); 1 line in 55-money defining the US$100 million test (the test's own definition, its arithmetic is tagged on the next lines).
- Marks: one exclamation mark inside the verbatim LinkedIn quote in 90-mentor ("Congratulations!!"); "unlock" and "empower" appear only in the generated claim register (fact text from D1-05-F47 "unlock codes" and D1-05-F50 "Empower Health", a programme name), not in any part.
- Missing pictures: reported only because the joined file sits in the scratchpad, away from `adaptive-care-pictures\`; picture lines untouched.
- Headings: every part opens with exactly one `## ` (00-head carries the document `# ` title); no `#####`; no em dashes; all tables have consistent column counts.

## Could not resolve
1. 00-head.md status line ("Stage 2 of 3 ... Still being written: the challenge decoded, public voice ...; two claims checks applied, a third is running") is out of date: every part now exists and all three checks are applied. The true stage is the coordinator's to state; left unchanged.
2. 85-mvp.md verbatim thesis quote still says "photo or Bluetooth", "most rural specialist posts are empty" and that China "cut cardiovascular events by a quarter" without the drugs-and-incentives caveat. It is a verbatim draft; the wording-fix line under it already lists the needed changes. Left as quoted.
3. 55-money.md says CDSCO's flowchart notes clinical-investigation permission "is not mandatory for Class A" [D2-04-F39]. D2-04-F39 was not re-checked by D3-03; other parts say a study on patients needs permission and ethics approval. Not contradictory in substance (Class A is the exception), left; worth a check by counsel.
4. Women's phone ownership differs between parts: 20-burden and 90-mentor give 63.6% of women 15-49 (rural 57.4%) [D1-03-F42], 25-voice gives 54% owning the phone they use (rural 46.6%) [D3-04-F23]. Different sources and definitions; neither part gives both figures. Not edited (adding the second figure to each part would be new text).
5. 05-decision-brief.md cites facts in round brackets, not square brackets as the writer brief asks; the linking script still matches bare IDs, so left.
6. 50-players.md "Insulet, Tandem, Beta Bionics" and similar abroad figures were not re-checked by any claims check beyond D3-03's rows; nothing on the never-say list was found there.
