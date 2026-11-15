# S0 story brief: rewrite the adaptive care document as one story plus one appendix (14 Nov 2026)

## Why this rewrite

`SPARK Night 2026 - adaptive care challenge.md` was written overnight by many agents, one "lens" per part (doctor's view, engineer's view, business view ...). The research is good but the reader cannot follow it:

- It opens with the answer (part A and the Decision brief) before the reader knows the problem.
- The same facts repeat in many parts. "About half do not come back" (D1-03-F10) is in 11 parts; the 1.0 against 6.1 mmHg result (D1-01-F05) in 6. One topic, such as "who else does this", is spread over F1, H, I and L.

The owner asked for: a story that flows. First the problem and the market issues, told simply. Then the research, condensed, in plain words. Then the analysis. Then the product we can build. Then the MVP. Then the recommendation (old L) and the method (old M). The story should be short enough to read in one sitting, but the first three chapters should carry a little more detail (about two extra pages each). After the story comes an appendix where all the heavy detail sits, each topic in one place.

**The owner's hard rule: do not change any information and do not make anything up. Fix the flow.**

## The source

- The only source is the old part files in `report-parts\dtx\` (00-head to 99-method). Read them in full for the parts you are given.
- Do not open the research notes for new facts. No web. No memory. No new number, name, date, quote, claim or judgement.
- Transition sentences ("So the question becomes who pays.") are allowed and wanted. They carry no facts.
- Style rules: read `research_notes\dtx\W0-writer-brief.md` sections "Facts" (rules 2 to 7), "Writing" and "Pictures". Where W0 says "use facts from the notes", this brief overrides it: use only what is in the old parts.

## Keep facts exact

1. Every number keeps its value, its unit and its fact ID in square brackets, written as in the source, for example `[D1-01-F05]`. Several: `[D1-01-F01, D1-01-F02]`. Always the full ID (no "F02 to F04" shorthand).
2. Every tag stays with its claim: OUR VIEW, OUR ARITHMETIC, OUR ESTIMATE, ASSUMPTION, EXAMPLE, THEIR CLAIM, OUR DESIGN, OUR SIMULATION, NOT RESEARCHED, NOT FOUND, TARGET. Every "(search summary only)" stays.
3. Trials keep who was compared with whom, how many, where, how long, and whether the result was null. In the story you may give the headline; the appendix keeps the full description.
4. Conflicting figures stay both, with their years.
5. Simplify the words, never the meaning. "Not significant" stays "not significant". "Says it holds" stays "says it holds" (not "holds").
6. If two parts word the same fact differently, use the wording from the part that the fact-home table names as its home.

## Said once

- `S1-fact-homes.md` (same folder) gives every one of the 587 cited fact IDs one home appendix (A to H), chosen by script from where the old document explains it most. IDs in that table are written without leading zeros (D1-01-F5 is D1-01-F05 in the text).
- **Appendix writers:** every ID whose home is one of your appendices must appear in your appendix, with its full detail. An ID from your source parts whose home is another appendix: leave it out, unless your text cannot make sense without it; then one short clause with the ID, no re-explaining.
- Overrides to the table: the protocol file (doses, steps, intervals, thresholds as a data file) and the parts list and costs of tonight's build live in **Appendix G**; Appendix C explains the idea of a protocol as data and the science of a trustworthy reading, and points to G for the file and the parts.
- **Story writers:** the story may cite any ID. A fact is stated once in the whole story (chapters 1 to 6). A later chapter may recall it in one short clause ("the half who do not return, chapter 1"), without repeating the detail.
- The story and the appendix are allowed to overlap in one way only: the story gives the headline, the appendix gives the full detail.

## The new document

Part files go in `report-parts\dtx-story\` (joined in file-name order). Each file starts with one `## ` heading exactly as below. Inside, use `### ` and `#### ` only. Story sub-sections are numbered (`### 1.1 ...`). Appendix sub-sections are numbered with the letter (`### B1. ...`).

| File | `## ` heading | Writer | Words | Built from (old parts) |
|---|---|---|---|---|
| 00-head.md | (title, what this is, how to read, layout, contents) | coordinator | 450 | 00, 03 |
| 10-problem.md | 1. The problem | Story writer 1 | 3,500 | 10, 20, 25, 50 (why companies died, the gap), 55 (who pays today, briefly), 90 (one paragraph on who set the challenge) |
| 20-research.md | 2. What the research found | Story writer 1 | 5,500 | 30, 35, 40, 50, 70, 55 |
| 30-analysis.md | 3. Analysis: what it all means | Story writer 1 | 3,000 | 60, 80 (option tree, scores, why blood pressure first), 05 |
| 40-product.md | 4. The product we can build | Story writer 2 | 1,800 | 80 (card 1, expansion), 85, 40 (system parts) |
| 50-mvp.md | 5. The MVP | Story writer 2 | 2,200 | 85, 40 (honest tonight against roadmap), 60 (G11 next 90 days) |
| 60-recommendation.md | 6. Recommendation, risks and open questions | Story writer 2 | 1,800 | 95, 03, 05, 90 (framing and questions) |
| 70-method.md | 7. Method and limits | coordinator | 900 | 99 |
| 81-app-a.md | Appendix A. The challenge, the burden and the voices in detail | Appendix writer 1 | as needed | 10, 20, 25 |
| 82-app-b.md | Appendix B. The clinical evidence in detail | Appendix writer 1 | as needed | 30, 35 (and 10's B4 to B6 where they hold evidence) |
| 83-app-c.md | Appendix C. The technology in detail | Appendix writer 2 | as needed | 40 |
| 84-app-d.md | Appendix D. Every player in detail | Appendix writer 2 | as needed | 50, 70 |
| 85-app-e.md | Appendix E. Money and rules in detail | Appendix writer 2 | as needed | 55 |
| 86-app-f.md | Appendix F. Strategy and the options in detail | Appendix writer 3 | as needed | 60, 80, 95 (the handgrip row), 05 (scores) |
| 87-app-g.md | Appendix G. The build pack in detail | Appendix writer 3 | as needed | 85 |
| 88-app-h.md | Appendix H. The mentor and the fund in detail | Appendix writer 3 | as needed | 90 |
| 89-app-i.md | Appendix I. The claim register | coordinator | generated | 99 register |

## The story (chapters 1 to 6)

The reader is a third-year student on the team, some with English as a second language, and later a fund mentor. They should be able to read chapters 1 to 6 alone and understand the problem, what was found, why, what to build and what to say. The answer comes at the end, not the start.

How every story chapter is written:
- Opens with two or three sentences: what this chapter shows and why it follows the last one.
- Each `###` sub-section in chapter 2 opens with an "In short" block quote: `> **In short.**` then 2 to 4 short bullets inside the quote.
- Plain words, short sentences. A technical term is explained once in brackets the first time it appears in the story.
- A table for any comparison of three or more things.
- Ends with "Full detail: Appendix X (sections X1 to X4)." and a short closing paragraph that leads into the next chapter. A judgement in it is marked OUR VIEW.

### Chapter 1. The problem (the story of the problem and the market issues)

1. Who set the challenge and what it really asks. The fund's words (quote them once, from 00-head), one or two sentences on who set it (the fund and the mentor, from 90). What each phrase demands, in plain words. What "beyond monitoring and reminders" rules in and out: the therapy itself has to change. The loop: sense, decide, confirm, act, learn. Picture `00-the-loop.png`.
2. Who it is about and how big it is. How many people in India have high blood pressure, diabetes, heart failure. The cascade: know, treated, controlled. Picture `22-india-cascade.png`. Treatment is not control. The world and Japan in a line or two.
3. Why care breaks down between visits. The specialist and time gap, cost, follow-up, about half not returning to the government programme, public programmes and their reach, phones and who is left out.
4. What patients and doctors say in public. Why patients miss follow-up and stop medicines, home monitors in Indian homes, what doctors and health workers say, what users say about existing programmes, reminders.
5. The market issues: why the market has not fixed this. What has been sold so far (apps that show readings or send reminders). Why companies died. Who pays today and why nobody pays for an app on its own. No Indian service was found that changes a dose from home readings (a search result, not proof of absence).
6. The problem in one paragraph: the scarce thing is the prescriber's decision, which waits for a clinic visit half the patients never make. Use the wording already in the old parts (for example 10's "So what for us" or 60).

### Chapter 2. What the research found (condensed, plain words)

1. What actually improves outcomes. The five rules the evidence gives, each with its headline trial. Pictures `20-what-lowers-pressure.png` and `21-share-controlled.png`. The map of feedback-driven therapies (what the loop changes). One table: condition, what works, how strong, the main caution (blood pressure, diabetes, heart failure, others). Prescription apps and adherence technology in two or three sentences. Safety in two or three sentences.
2. How care has been scaled without specialists. India's hypertension programme in practice, who may change a dose in India, Tamil Nadu, programmes abroad, what these programmes changed that software alone could not.
3. What the technology can and cannot do. Trusting a home reading, dose algorithms, a protocol as data, what language models may and may not do with doses, adaptive nudging and personal response models as later work, open data and simulators.
4. Who is already doing this. India (alive, shut or sold, not found), abroad, the closest relatives to our loop, prescribed apps in Germany, Japan and Korea, what funds abroad are backing, the gap. Merge old F1 and H here.
5. The money. What is spent today, who could pay in India, market size counted two ways (picture `23-market-size.png`), the US$100 million-a-year test, price sensitivity, unit economics, what comparable companies earn and are worth, the funding climate.
6. The rules. India's July 2026 guidance, telemedicine rules, who may change a dose, what tonight's prototype may and may not say, rules and payment abroad, in short.

### Chapter 3. Analysis: what it all means

1. The thesis, in a few paragraphs (from the parts' own wording).
2. Where to play and how to win: the question tree in brief, where to play, how to win, where the money is today, five forces and three futures in two small tables or a few lines each, the risks that matter, the investor's lens, the three questions a partner would press.
3. The options weighed: the option tree in brief, the seven options, the six weighted tests, picture `24-option-scores.png`, the three to weigh, and why blood pressure first.

### Chapter 4. The product we can build

The home blood-pressure step loop, end to end: what it does in one paragraph; the system map (picture `14-system-map.png`); the patient side (`10-bp-patient-chat.png`); the doctor side (`11-bp-doctor-queue.png`, `12-bp-doctor-detail.png`); trusting the reading (`13-reading-quality-clip.png`); the "was the medicine taken" check; safety built into the design; same loop, new protocol (`15-same-loop-new-protocol.png`) and the expansion order.

### Chapter 5. The MVP

The ladder: rung 1 tonight, rung 2 a two-week test with a doctor in the loop, rung 3 a 90-day pilot (and the next 90 days from G11). What is built tonight in brief (software, hardware, the protocol file, the tests, the cut lines). Honest tonight against roadmap. The four results the team can show honestly. The 3-minute demo script. The safety statement. Point to Appendix G for the full build pack and the draft Deep Tech Thesis.

### Chapter 6. Recommendation, risks and open questions (the old L)

The recommendation and its three reasons (recalling chapter 2 facts in one clause each, not re-explaining). The pitch in one breath. What you can say at noon and what you cannot (the table from 03). What we are not claiming. The three weak spots (merge 03 and 95). Why not the other options (the table from 95; the handgrip row's detail goes to Appendix F, keep one line here). Pitching to the mentor: how to frame it for him, five questions to expect, five worth asking (from 90). Open decisions. The next seven days. What this document does not cover.

## Pictures

Each picture is placed once, in the story, where the list above puts it: `![short description](adaptive-care-pictures/<file>.png)` with one italic caption line under it. Take the caption from the old part that used the picture, or from `adaptive-care-pictures\captions.md`. Mock-ups are captioned "Mock-up with example data." Appendices do not repeat pictures; they may say "(picture in chapter 4)".

## The appendix

How every appendix is written:
- Opens with one or two sentences: what it holds and which story chapter it supports.
- Keeps all the detail of its source parts: trial sizes, confidence intervals, full tables, full lists, every company row, limits, nulls, dates. This is where the depth lives.
- Removes repetition: within the appendix, and anything whose home is another appendix (see "Said once").
- Orders its sub-sections to follow the story chapter it supports, not the old part's order.
- Merges the old parts' many "So what for us" paragraphs into one "So what for us" at the end of the appendix (OUR VIEW), keeping each distinct judgement once.
- Keeps "What we could not find" as one section at the end of the appendix, merged and de-duplicated.
- Simplifies wording where it helps, without changing meaning.

## Cross-references

Every old reference ("part F2", "Part J", "see I", "B6", "the Decision brief") must point to the new place: a story chapter ("chapter 2.5") or an appendix section ("Appendix E3"). Use the section numbers you write. If you point into another writer's appendix, use the appendix letter only ("Appendix G").

## House style (the checker enforces it)

No em dashes. No exclamation marks. No rhetorical questions. No "Imagine". Banned words: synergy, revolutionary, game-changing, AI-powered, seamless, leverage, utilise, robust, cutting-edge, innovative, streamline, optimise, empower, unlock, world-class, best-in-class, next-gen, ecosystem, landscape, holistic, delve, and "solution" for the product. Rupees in Indian grouping (₹2,600; 3.3 lakh; ₹844 crore). Ranges with a plain hyphen. "a month", not "/mo". Never "compliant", "100%" or "zero risk" in a legal sense.

## When you finish

Reply with: the file(s) written and their word counts; any fact ID from your source parts that you could not place (with the reason); any place where you had to choose between two differing wordings of the same fact.
