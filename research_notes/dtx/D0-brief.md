# D0 brief: rules for every research agent (Beyond Next Ventures challenge, SPARK Night)

Read this whole file before you start. Where it disagrees with any other instruction file (including the deep-research skill's `researcher.md`), this file wins.

## 1. What this is for

A student team (computer science + hardware + biology, Ashoka University, India) is in an overnight deep-tech buildathon RIGHT NOW: 13 Nov 2026 6 PM to 14 Nov 2026 noon, India time. By noon they must show a clearly defined problem, a working prototype, first test results and a one-page "Deep Tech Thesis". Kits hold common maker parts (ESP32 or Arduino boards, breadboards, basic sensors). Anything specialist must be borrowed, bought locally tonight, or replaced by a phone.

The challenge, set by the venture fund Beyond Next Ventures (verbatim):

> We need ways to manage chronic disease burden at scale despite limited access to resources, specialists and irregular clinical follow-ups. Patients need treatment methods that responds to their specific condition, and will remain adaptive to patient needs between appointments. How can digital therapeutics use rapid feedback from medical devices or biomarkers to continuously personalise care, thereby bringing measurable improvements in health outcomes to patients who cannot access frequent specialist support? The opportunity is to extend effective treatment into everyday life, beyond monitoring and reminders.

A coordinator combines your note with others into one long document. You gather and record facts. You do not rank options and you do not write conclusions.

## 2. Scope defaults

- India first. Then global evidence. Japan matters because it is the fund's home.
- "Digital therapeutic" here means software (often with a device) that changes the treatment itself for one patient: the dose, the next step of a protocol, the exercise, the diet plan, the stimulation. Dashboards and reminders alone do not count, but record the evidence about them, because the challenge says "beyond monitoring and reminders".
- "Adaptive depth" scale, used for every product and programme: 0 = uses no patient data; 1 = shows data (monitoring); 2 = reminders and generic content; 3 = personalised coaching from the person's own data; 4 = changes the therapy itself by protocol or algorithm (dose, protocol step, exercise prescription), with or without a clinician signing off.
- State of play as of November 2026. The coordinator's own knowledge stops in mid-2026 and may be stale, so check for 2026 events.

## 3. Speed and saving

- Time box: about 20 minutes. Stop at your search allowance (it is in your task).
- FIRST create your note file with its title and an empty Digest. Then append findings after every 5 to 8 searches. An agent that stalls must leave its work on disk.
- Cover the highest-value questions first.
- Not searched: write `NOT SEARCHED: <what>`. Looked for and not found: write `NOT FOUND: <what>`. Never guess.
- Prefer direct fetches of known sources, which need no search:
  - PubMed: `https://pubmed.ncbi.nlm.nih.gov/?term=...` or `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term=...` then `esummary.fcgi?db=pubmed&retmode=json&id=...`
  - Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json`
  - ClinicalTrials.gov: `https://clinicaltrials.gov/api/v2/studies?query.term=...`
  - openFDA devices: `https://api.fda.gov/device/510k.json?search=...`
  - arXiv: `http://export.arxiv.org/api/query?search_query=...`
  - regulator pages, company pages, journal pages, GitHub.
- Blocked or limited: reddit.com (use the Arctic Shift API sparingly), LinkedIn, X and Instagram (search snippets only; never reconstruct a post you could not read).
- End the note with `Searches used: N`.

## 4. The fact rule (the most important rule)

- Every fact is one bullet or table row with: an ID (`<note code>-F<number>`, for example `D1-03-F12`), the value with its unit, the year the value refers to, the source URL, the date of the source item (or "undated"), and OPENED (you opened the page and saw the value) or SNIPPET (search snippet only).
- Open the primary source for every number that matters. A SNIPPET number is second class and must be labelled.
- Quotes: 25 words or fewer, verbatim, only from a page you opened.
- Your own memory is a lead, never a source. The leads in your task are also only leads: confirm each one or mark it NOT FOUND.
- Figures that conflict: record both, with dates and sources. Do not pick one.
- Tag each fact: CITED (published figure, source opened), THEIR CLAIM (a company says it about itself), OUR ARITHMETIC (you computed it; show the sum), SOURCE ESTIMATE (the source itself estimates or models), SNIPPET.
- Time-sensitive facts (prices, laws, funding, whether a company is alive) carry their date.

## 5. Schemas

**A study.** Name and year; design (randomised trial, cluster trial, cohort, review); size; country and setting; who was compared with whom; primary outcome; effect with its confidence interval or p value; length of follow-up; funder; main limits; URL. Record null and negative results as carefully as positive ones. Flag India and other low-resource evidence.

**A company, product or programme.** What it is in one line; country; what it measures (device or biomarker); what it changes in the therapy; adaptive depth 0-4; who is in the loop (doctor, nurse, coach, nobody); evidence (trial? peer-reviewed? own data only?); regulatory status; price to the patient or payer; funding (amount, date, lead investor, or participant only); traction (THEIR CLAIM, with date); status as of Nov 2026 (alive, acquired, pivoted, shut); URL.

**A person.** Two independent sources tying the person to the role. If a namesake exists, say which one you rejected and why.

## 6. Note layout

```
# <note code> <title> (agent: <model>, 2026-11-13)

## Digest
(400 words at most: the 12 facts that matter most for deciding what to build tonight, each with its fact ID; 3 surprises; anything that contradicts the starting leads in section 7.)

## Findings
(grouped under the key questions in your task)

## NOT FOUND / NOT SEARCHED

Searches used: N
```

## 7. Starting leads to break

The coordinator's unverified starting ideas. Look for evidence against them as hard as evidence for them.

1. Programmes that change the treatment from home readings (dose titration, protocol steps) improve outcomes; monitoring and reminders alone mostly do not.
2. In India the binding limit is the prescriber's time and the gap between visits, so the workable design keeps a doctor or health worker approving each change while software does the reading, the protocol logic and the drafting.
3. Candidate loops: (a) home blood-pressure readings driving a stepwise medicine protocol; (b) fasting-glucose readings driving insulin dose changes in type 2 diabetes; (c) an inhaler or breathing sensor plus air-quality data adapting an asthma or COPD plan; (d) phone-camera and pulse-sensor rehabilitation that adapts each session.
4. The durable advantage is outcome data, clinical validation and distribution, not the app.
5. The honest regulatory route is decision support with clinician sign-off first; autonomous dosing needs a licence later.

## 8. Style

Dense, factual, plain words, short sentences. No marketing language. No em dashes. Rupees with Indian grouping (₹1,200; ₹844 crore). Give US dollar figures as published.
