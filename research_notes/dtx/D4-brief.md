# D4 brief: the biology deep dive (Round 4, 14 Nov 2026, about 00:40 AM India time)

Read this whole file, then read `D0-brief.md` sections 3 to 6 and 8 in this folder. D0's fact rule, schemas, note layout and style apply in full. Where this file adds to D0, this file wins.

## Why this round

The team's document is built on trial abstracts and policy papers. It has little of the physiology underneath: why one patient responds to a drug and another does not, how fast a dose change works, how much blood pressure moves on its own, why each safety check exists, which lab values matter and how fast they move, and how to tell from the body (not from the patient's word) whether the medicine was taken. That layer is what would make the product hard to copy. The reader of your note is the team's biology student, who will turn it into protocol rules and product features.

## The product it serves

A home blood-pressure step loop for India. A patient sends home cuff readings. Software runs the state's published step protocol (Gujarat HEARTS sheet) from a data file and drafts a dose change; a doctor approves it with one tap. Before any step-up it asks whether the medicine was taken. The protocol: step 1 amlodipine 5 mg; step 2 amlodipine 10 mg ("after 30 days measure BP again, if still high"); step 3 add telmisartan 40 mg; step 4 telmisartan 80 mg (requires blood sugar, urea, creatinine, urine protein; abnormal means refer; if no specialist, withdraw telmisartan and add chlorthalidone); step 5 add chlorthalidone 12.5 mg (hydrochlorothiazide 25 mg if unavailable). Telmisartan and chlorthalidone are barred in pregnancy and in women of childbearing age without effective contraception. A Nigeria protocol uses losartan. The loop uses home readings: two readings 1 minute apart, morning and evening, on days 24 to 30 of each 30-day cycle; at least 3 valid days, aiming for 7; "still high" is a home mean of 135/85 or more; 180/110 or more triggers urgent review.

These are the drugs to centre on: **amlodipine, telmisartan, chlorthalidone, hydrochlorothiazide** (and losartan). Other classes (ACE inhibitors, beta-blockers, spironolactone) matter where they explain a mechanism or a signal.

## Source rules for this round

- **Primary sources first:** physiology and pharmacology papers, pharmacokinetic studies, drug labels (DailyMed, FDA labels, EMA SmPCs, CDSCO where available), guideline documents (ESH 2023, ISH 2020, ACC/AHA 2017 or later, WHO 2021, NICE NG136, Indian guidelines), meta-analyses and named trials. Use Europe PMC (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&resultType=core` returns abstracts) and PubMed E-utilities (`efetch.fcgi?db=pubmed&id=...&rettype=abstract&retmode=text`) as in D0. The Lancet and PubMed web pages often refuse the fetch tool; go through Europe PMC instead.
- Record each fact with **the mechanism as well as the number** where the source gives it ("telmisartan blocks the AT1 receptor, so the efferent arteriole of the glomerulus relaxes and filtration pressure falls, so creatinine rises a little" is what the biology student needs).
- Flag **India and South Asian** data. Say so plainly when only Western data exist.
- Record **how fast** things happen in days or weeks wherever the source gives it.
- Record nulls and disagreements between guidelines.
- You are not writing advice. Doses appear only as quoted from a label, guideline or protocol.

## Notes, codes and allowances

| Code | File name | Questions | Searches |
|---|---|---|---|
| D4-01 | `D4-01 Who responds to what.md` | Response differences by drug class: age, salt sensitivity, ancestry (including South Asian and African), plasma renin, sex, body weight. Crossover or rotation trials of personalised drug choice (each patient tries several classes; how much better is the best one than the average). Guideline rules for the first drug by profile (NICE's age and ancestry rule; others). Pharmacogenomics: what is known, effect sizes, whether any is used in practice. Dose-response: how much extra lowering doubling a dose gives against adding a second class (half-dose combination evidence). How each protocol drug lowers pressure (mechanism). | 35 |
| D4-02 | `D4-02 How fast a dose change works.md` | For each protocol drug: half-life, time to steady state, time to near-full blood-pressure effect after starting or raising the dose (labels, pharmacokinetic studies, trials). Guideline intervals between titration steps (India IHCI/HEARTS, WHO 2021, ISH 2020, ESH 2023, ACC/AHA, NICE). Trials that titrated faster (for example every 2 weeks) and what they found on control and side effects. How much of the full effect is present at 1, 2 and 4 weeks. Does the response keep growing after 4 weeks for chlorthalidone or telmisartan. | 35 |
| D4-03 | `D4-03 Natural variation and how many readings.md` | How much home readings vary: reading to reading in one session, morning against evening, day to day (within-person standard deviation, in mmHg). Daily rhythm, night dipping, the morning surge. White-coat hypertension and masked hypertension: definitions and prevalence (India studies if any). Seasonal change (summer against winter, India if any). Regression to the mean. Studies on how many home readings or days give a reliable mean, and the error of a 3-day against a 7-day mean. Any published statistical rule for deciding "still high" or "changed" from noisy home readings (for example in self-titration trials such as TASMINH or in titration algorithms). The first-day effect and first-reading effect. | 35 |
| D4-04 | `D4-04 Why each safety check exists.md` | ARBs (telmisartan, losartan) and the kidney: why creatinine rises, how much rise is expected and accepted (guideline thresholds such as 30%), when to stop, bilateral renal artery stenosis, the labels' monitoring advice, when to recheck after starting. Pregnancy: why ARBs, ACE inhibitors and diuretics are barred (fetal kidney, oligohydramnios, timing by trimester; label boxed warnings), what is used instead. Potassium: high on ARBs, low on thiazides; the thresholds labels and guidelines use; why it matters for the heart. Dizziness on standing in older people (orthostatic hypotension): definition, prevalence by age (India if any), mechanism (baroreflex), falls, which drugs and doses raise it, how to test it at home. Thiazide-type effects: sodium (hyponatraemia, older women), uric acid and gout, blood sugar. Amlodipine ankle swelling: mechanism, dose dependence, how often. Very high readings: what 180/110 means physiologically. | 35 |
| D4-05 | `D4-05 Biomarkers and adherence signals.md` | Lab values beyond the cuff: creatinine and eGFR, potassium, urine albumin (albumin-to-creatinine ratio), BNP or NT-proBNP, HbA1c. For each: what it tells, the normal and action thresholds, how fast it changes after a treatment change (days, weeks, months), and whether a point-of-care or home test exists with its price in India (state the date). Non-adherence: how often apparent uncontrolled or resistant hypertension is non-adherence when measured by urine or blood drug assays (liquid chromatography with mass spectrometry), and the main studies. Which body signals reveal whether a drug was taken, drug by drug: heart rate for beta-blockers and some calcium blockers (and whether amlodipine changes heart rate), lab changes for diuretics (potassium, uric acid) and ARBs (renin), and any wearable or home signal. Pharmacy refill data, smart pill boxes and blister packs: evidence. Cost of drug assays in India if any. | 35 |

If a question cannot be answered in your allowance, write NOT SEARCHED. If you looked and found nothing, write NOT FOUND.

## Fact line format (must match exactly, a script parses it)

Each fact is one bullet that starts with its ID, then fields separated by ` | `:

```
- D4-02-F07 | Telmisartan time to full effect | Maximum blood-pressure lowering is generally reached 4 to 8 weeks after starting (label wording quoted: "..."). Mechanism: ... Year 2023. https://dailymed.nlm.nih.gov/... | source dated 2023-05 | OPENED | CITED
```

Number facts F01, F02 and so on, in order. Put the source URL on the same line as the ID. One fact per line.

## Note layout

Use D0 section 6, with the title `# D4-0N <title> (agent: <model>, 2026-11-14)`. In the Digest, give the 12 facts that matter most for the biology of the loop, then a section `## What this suggests for the product` (at most 8 bullets, each tied to fact IDs, each marked as a suggestion), then the Findings grouped by your questions, then NOT FOUND / NOT SEARCHED, then `Searches used: N`.

Create the note file first with its title and an empty Digest, then append after every 5 to 8 searches. Time box about 25 minutes.
