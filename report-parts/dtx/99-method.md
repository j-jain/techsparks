## M. Method, limits and the claim register

### How this was made

- **When.** The night of 13 November 2026, between about 9:40 PM and midnight, India time, while the buildathon was running.
- **Who did what.** A coordinator (Claude Fable) planned the run, scored the options, wrote the argument, the Decision brief, parts A, L and M, and ruled where notes disagreed. Research agents gathered and recorded facts: Claude Opus for the clinical evidence, the build plans, the AI methods and the law; Claude Sonnet for the burden, the players, the market, the funded startups, the public voice, the scaled-care cases, the fund and the claims checks. Writers turned notes into parts: Fable for the challenge decoded, the strategist's view and what we could build; Opus for the rest. Separate agents drew the pictures and applied corrections.
- **Three rounds.** Round 1 answered "what to build tonight" (six notes). Round 2 produced the build plans, the methods, the rules, the market inputs and the funded-abroad tab (six notes, plus the coordinator's reading of the mentor's LinkedIn profile in the signed-in browser). Round 3 checked claims, filled gaps and added public voice, scaled-care cases, the fund's record and one late lead (eight notes).
- **A second session.** A side session opened by a "btw" message ran a duplicate research pass for about 13 minutes and then stopped. Its web notes were not used. Its two LinkedIn notes (L1 and L2) were, and are cited as "LinkedIn, read 13 Nov 2026".
- **The notes.** Everything is in `research_notes\dtx\`: the brief every agent followed (`D0-brief.md`), the notes (`D1-` to `D3-`), the scoring (`DT1-triage.md`), the argument (`DT2-spine.md`), the market model's output (`DT3-market-model.md`), the corrections and audit logs (`C1-` to `C3-` files) and the LinkedIn notes.

### The rules the research followed

1. Every fact has an ID, a value, a year, a source link, the date of the source, and whether the page was opened or only seen in a search summary.
2. An agent's own memory was a lead, never a source. "Not found" was written instead of a guess.
3. Conflicting figures were both recorded.
4. Trials were recorded with their design, size, country, comparator and limits, and null results with the same care as positive ones.
5. Companies' statements about themselves are marked THEIR CLAIM.
6. Writers could use only facts in the notes and had to cite each by ID. A script then turned each ID into a link to its source and built the register below.

### What "opened" means, and other limits

- **"Opened" is weaker than it sounds.** The tool that fetches a page returns an extract made by a model, not the raw page. "Opened" means the value appeared in that extract. For the facts that carry the argument, a second agent fetched the source again, usually by a different route, and compared.
- **Blocked sources.** Several publishers and official sites refused the fetch tool (among them the Lancet and PubMed web pages, some government PDFs, and most company press sites). Journal abstracts were read through Europe PMC and the US National Library of Medicine's service instead. Reddit could not be read at all. Agents could not read LinkedIn; only the coordinator and the side session could, in the signed-in browser.
- **Abstracts, not full papers.** Most trial facts come from abstracts. Details that live only in a paper's tables may be missing.
- **The search budget ran out in Round 3.** Three agents hit the shared limit early. Their notes say exactly what was left unsearched, and the parts built on them carry those gaps.
- **No interviews.** Nobody on the team has yet spoken to a patient, doctor, pharmacist or payer about this. Part C2 is public voice, not customer evidence. The persona and the buying committee in part I are hypotheses.
- **Ours, not findings.** The option scores, the market model, the price, the unit costs, the simulation and every "OUR VIEW" paragraph are judgements or arithmetic from stated inputs.
- **Not advice.** Nothing here is medical or legal advice. Doses appear only as quoted from published protocols. The legal sections say what the texts say and list questions for a lawyer.
- **Speed.** This was written in one night. Parts were written by different agents, and although a consistency pass was run, some repetition and small differences in wording between parts remain.

### The checks that were run

| Check | What it covered | Result |
|---|---|---|
| Claims check 1 | Clinical evidence (notes D1-01, D1-02) | 53 claims re-opened: 48 confirmed, 5 corrected in wording, none wrong |
| Claims check 2 | India burden, players, market (D1-03, D1-04, D2-05) | about 45 claims: 29 confirmed, 7 corrected, 5 contested, 3 not found. The search budget ran out before 9 search-summary facts could be upgraded |
| Claims check 3 | Players abroad, protocols, rules, funded startups (D1-05, D1-06, D2-04, D2-06, new facts in the build notes) | 85 claims: 63 confirmed, 13 corrected, 2 contested, 7 not found. Every protocol dose, step, interval and threshold matched the published sheets |
| Corrections | Three passes over the parts | 82, 69 and 60 edits, logged in `C1-corrections-log.md`, `C2-corrections-log.md` and `C3-audit-log.md` |
| Consistency audit | All parts read together | 19 contradictions between parts found and fixed |
| Sources | Every cited fact ID resolved against the notes by script | No cited fact is missing from the notes |
| Web searches | Research agents, three rounds | About 345 searches; most trial and protocol checks used direct fetches instead |
| Links | Every distinct source link in this file requested once by script, 13 Nov 2026 about 11 PM | 494 links: 439 answered; 46 refused an automated request (LinkedIn and some news and journal sites; they open in a browser); 6 did not connect; 3 returned "not found" to the script (two US regulator pages, which often refuse scripts, and one news page) |

Most facts in the register below were read by one agent only and are marked "not re-checked". The checks were aimed at the facts that carry the argument, the market model and the protocol files.

### What was not found

Each part ends with its own list. The gaps that matter most for decisions:

- An Indian trial of home readings driving dose steps.
- A measured split of public and private treatment for high blood pressure.
- Current counts of specialists, and of private general doctors and clinics.
- Any Indian payer for remote monitoring or a digital therapeutic.
- A legal basis for a nurse or community health officer changing a dose.
- Prices paid to medicine-adjusting programmes in the United States.
- Uptake of the insured blood-pressure app in Japan.
- The buildathon's judging criteria.

### The claim register

Every fact cited in this document, in order of its ID. "Read as" says whether the research agent opened the page or saw only a search summary. "Claims check" gives the second agent's verdict where one was run; "not re-checked" means only one agent read the source.

<!-- REGISTER -->
