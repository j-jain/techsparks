## 7. Method and limits

This chapter is the old part M. It says how the research was made, the rules it followed, the checks that were run and how far to trust it. The claim register that used to sit here is now Appendix J.

### This edition

- **What changed on 14 November.** The 13 November document was written by many agents, one view per part (the doctor's, the engineer's, the business view and so on), and opened with its answer. The same facts were repeated across parts. This edition re-orders the same parts into one story (chapters 1 to 6) followed by an appendix (A to H) that holds the full detail, each topic in one place, and Appendix J, the claim register.
- **What did not change.** The re-ordering added no research. No fact, number, tag or judgement from the 13 November parts was added or changed, with one exception found by the biology claims check: the GRAND study's percentages are shares of the 1,578 patients analysed, not the 1,920 enrolled, and this is corrected and marked where it appears. Repeated passages were removed and the wording was made plainer where that did not change the meaning.
- **What is new.** One research round was added on 14 November at the owner's request: a biology deep dive (Round 4, below). It is marked "new research" wherever it appears: chapter 2.7, chapter 4.9 and Appendix I.
- **How that was checked.** A script compared the new text with the 13 November parts: every fact ID cited in the old edition must be cited in the new one, no new ID may appear, and every number in the new text must also appear in the old text (the new biology sections are exempt, as they are new research). The result is in the table of checks below.

### How this was made

- **When.** The night of 13 November 2026, between about 9:40 PM and midnight, India time, while the buildathon was running.
- **Who did what.** A coordinator (Claude Fable) planned the run, scored the options, wrote the argument, the Decision brief, parts A, L and M of the 13 November edition (their content is now in chapters 6 and 7 and the opening pages), and ruled where notes disagreed. Research agents gathered and recorded facts: Claude Opus for the clinical evidence, the build plans, the AI methods and the law; Claude Sonnet for the burden, the players, the market, the funded startups, the public voice, the scaled-care cases, the fund and the claims checks. Writers turned notes into parts: Fable for the challenge decoded, the strategist's view and what we could build; Opus for the rest. Separate agents drew the pictures and applied corrections.
- **Three rounds.** Round 1 answered "what to build tonight" (six notes). Round 2 produced the build plans, the methods, the rules, the market inputs and the funded-abroad tab (six notes, plus the coordinator's reading of the mentor's LinkedIn profile in the signed-in browser). Round 3 checked claims, filled gaps and added public voice, scaled-care cases, the fund's record and one late lead (eight notes).
- **Round 4, 14 November (the biology deep dive).** Between about 12:30 AM and 1:30 AM, five research agents (Claude Opus) answered the questions the team's review of the document found missing: who responds to which drug, how fast a dose change works, how much blood pressure varies on its own, why each safety check exists, which lab values matter and how fast they move, and how to tell from the body whether a medicine was taken. They recorded 284 facts in notes `D4-01` to `D4-05`, mostly from primary papers, drug labels and guidelines read through Europe PMC, PubMed and DailyMed. Three claims checks (`D4-06` to `D4-08`) then re-opened 183 of them. A writer turned the notes into chapter 2.7, chapter 4.9 and Appendix I.
- **A second session.** A side session opened by a "btw" message ran a duplicate research pass for about 13 minutes and then stopped. Its web notes were not used. Its two LinkedIn notes (L1 and L2) were, and are cited as "LinkedIn, read 13 Nov 2026".
- **The notes.** Everything is in `research_notes\dtx\`: the brief every agent followed (`D0-brief.md`), the notes (`D1-` to `D3-`, and `D4-` for the biology round), the scoring (`DT1-triage.md`), the argument (`DT2-spine.md`), the market model's output (`DT3-market-model.md`), the corrections and audit logs (`C1-` to `C3-` files) and the LinkedIn notes.

### The rules the research followed

1. Every fact has an ID, a value, a year, a source link, the date of the source, and whether the page was opened or only seen in a search summary.
2. An agent's own memory was a lead, never a source. "Not found" was written instead of a guess.
3. Conflicting figures were both recorded.
4. Trials were recorded with their design, size, country, comparator and limits, and null results with the same care as positive ones.
5. Companies' statements about themselves are marked THEIR CLAIM.
6. Writers could use only facts in the notes and had to cite each by ID. A script then turned each ID into a link to its source and built the register in Appendix J.

### What "opened" means, and other limits

- **"Opened" is weaker than it sounds.** The tool that fetches a page returns an extract made by a model, not the raw page. "Opened" means the value appeared in that extract. For the facts that carry the argument, a second agent fetched the source again, usually by a different route, and compared.
- **Blocked sources.** Several publishers and official sites refused the fetch tool (among them the Lancet and PubMed web pages, some government PDFs, and most company press sites). Journal abstracts were read through Europe PMC and the US National Library of Medicine's service instead. Reddit could not be read at all. Agents could not read LinkedIn; only the coordinator and the side session could, in the signed-in browser.
- **Abstracts, not full papers.** Most trial facts come from abstracts. Details that live only in a paper's tables may be missing.
- **The search budget ran out in Round 3.** Three agents hit the shared limit early. Their notes say exactly what was left unsearched, and the parts built on them carry those gaps.
- **No interviews.** Nobody on the team has yet spoken to a patient, doctor, pharmacist or payer about this. Chapter 1.4 and Appendix A are public voice, not customer evidence. The persona and the buying committee in Appendix F are hypotheses.
- **Ours, not findings.** The option scores, the market model, the price, the unit costs, the simulation and every "OUR VIEW" paragraph are judgements or arithmetic from stated inputs.
- **Not advice.** Nothing here is medical or legal advice. Doses appear only as quoted from published protocols. The legal sections say what the texts say and list questions for a lawyer.
- **Speed.** The research was written up in one night. Parts were written by different agents, and although a consistency pass was run, small differences in wording between parts may remain. This edition removed the repetition between parts.

### The checks that were run

| Check | What it covered | Result |
|---|---|---|
| Claims check 1 | Clinical evidence (notes D1-01, D1-02) | 53 claims re-opened: 48 confirmed, 5 corrected in wording, none wrong |
| Claims check 2 | India burden, players, market (D1-03, D1-04, D2-05) | about 45 claims: 29 confirmed, 7 corrected, 5 contested, 3 not found. The search budget ran out before 9 search-summary facts could be upgraded |
| Claims check 3 | Players abroad, protocols, rules, funded startups (D1-05, D1-06, D2-04, D2-06, new facts in the build notes) | 85 claims: 63 confirmed, 13 corrected, 2 contested, 7 not found. Every protocol dose, step, interval and threshold matched the published sheets |
| Corrections | Three passes over the parts | 82, 69 and 60 edits, logged in `C1-corrections-log.md`, `C2-corrections-log.md` and `C3-audit-log.md` |
| Consistency audit | All parts read together | 19 contradictions between parts found and fixed |
| Sources | Every cited fact ID resolved against the notes by script | No cited fact is missing from the notes |
| Claims checks, Round 4 | The biology notes D4-01 to D4-05 (files D4-06 to D4-08) | 183 facts re-opened: 175 confirmed, 5 corrected, 1 contested, 2 not found. One correction reached back into the 13 November facts: the GRAND study's sample (D3-04-F09) |
| Fidelity of this edition | The 13 November parts against this edition, by script (`tools\check_restructure.py`) | All 587 cited fact IDs kept; no number added outside the new research and the GRAND correction; each picture placed once |
| Web searches | Research agents, three rounds | About 345 searches; most trial and protocol checks used direct fetches instead |
| Web searches, Round 4 | Five research agents and three checkers | 32 web searches; nearly everything else came from direct fetches of Europe PMC, PubMed, DailyMed, openFDA and guideline PDFs |
| Links | Every distinct source link in the 13 November edition requested once by script, 13 Nov 2026 about 11 PM | 494 links: 439 answered; 46 refused an automated request (LinkedIn and some news and journal sites; they open in a browser); 6 did not connect; 3 returned "not found" to the script (two US regulator pages, which often refuse scripts, and one news page) |

Most facts in the register below were read by one agent only and are marked "not re-checked". The checks were aimed at the facts that carry the argument, the market model and the protocol files.

### What was not found

Each appendix ends with its own list. The gaps that matter most for decisions:

- An Indian trial of home readings driving dose steps.
- A measured split of public and private treatment for high blood pressure.
- Current counts of specialists, and of private general doctors and clinics.
- Any Indian payer for remote monitoring or a digital therapeutic.
- A legal basis for a nurse or community health officer changing a dose.
- Prices paid to medicine-adjusting programmes in the United States.
- Uptake of the insured blood-pressure app in Japan.
- The buildathon's judging criteria.
- From the biology round: any rotation trial of drug choice in India or South Asia; any Indian study of drug assays for adherence or their price; any Indian data on how much home readings vary within a person, or on seasonal change in home cuff readings; the home-monitoring rules of the 2026 ISH guideline; how fast urine albumin and NT-proBNP fall after treatment (Appendix I lists the rest).
