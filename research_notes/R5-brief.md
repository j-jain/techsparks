# R5 — Brief for Round 5 agents (claims check and solution design)

Date of this round: 12 November 2026. Read `R0-brief.md` (event, citation rule), then `R4-brief.md` (what changed: no exclusions, overlap flag, access rules), then `T4-triage.md` (the shortlist and which ideas are yours). Everything you write carries a URL and a date; "(snippet)" if you could not open the page; `NOT FOUND` beats a guess.

Access notes: reddit.com is unreachable (Arctic Shift API sparingly). LinkedIn, Instagram and X posts are snippet-only. No Nimble tools. WebSearch in standard mode. Load WebSearch and WebFetch with ToolSearch before your first search. End your notes with `Searches used: N`.

## A. Claims-check agents (Sonnet) — 40 searches each

Purpose: nothing in the final report may rest on a number, a role or a funding round that does not hold. You are given claims and their URLs. You are **not** given the coordinator's conclusions, and your job is to try to break each claim, not to confirm it.

For each item assigned to you in `T4-triage.md`:

1. **Open the source.** Open the cited page (or the best available page) and mark the claim:
   - `CONFIRMED` — value, date and attribution match.
   - `CORRECTED → <new value, source, date>`.
   - `CONTESTED` — another credible source gives a different value; give both.
   - `NOT FOUND` — page dead, or the figure or statement is not on it.
2. **People.** For each mentor claim: is this the right person (not a namesake), is the role current as of November 2026, and does the quoted or paraphrased statement appear on the page? A paraphrase that goes beyond the page is `CORRECTED`.
3. **Funding rounds.** Investor, round, amount and date, checked against a primary announcement or two press reports. Flag any round where the named fund only participated and did not lead, and any company that has since shut down, pivoted or been acquired.
4. **Indian numbers.** Each market or problem figure: source, year, and whether it measures what the claim says it measures.
5. **Indian equivalents.** Where the notes say "none found", spend one search trying to find one. Where they name one, check it is alive.
6. **Verdict paragraph** per idea: does the evidence base hold, what single number should the report lead with, and what should it never claim.

Output: `research_notes/R5-claims-0N.md`, one `## <ID> <name>` section per item, each with a table (Claim | Noted value | Status | Verified value / source / date) and the verdict paragraph. End with `## NOT CHECKED` and `Searches used: N`.

## B. Solution-design agents (Opus) — 20 searches each

Purpose: turn each shortlisted idea into a solution a sharp reader could start building. The reader is a third-year computer-science student who likes AI/ML, has a mixed team (software, hardware, bio) and attends SPARK Night (13 Nov 6 PM to 14 Nov noon, Ashoka University, Sonipat). Building kits with common maker parts are provided; specialist parts can no longer be ordered, so anything specialist must be something a student could borrow, buy locally the same day, or replace with a phone.

Use searches for what a design needs and the notes lack: public datasets, model benchmarks, part prices, a regulation's exact wording, a competitor's actual product. Do not re-research the problem proof; it is in the R4 notes.

For each idea assigned to you in `T4-triage.md`, write these headings:

1. **The problem in one paragraph**, with the two strongest Indian numbers from the notes (keep their URLs).
2. **How the system works.** Inputs, steps, outputs. What the user sees. A plain-text block diagram is welcome.
3. **The AI/ML core.** Which model family and why; what it is trained or prompted on; where Indian data comes from (a named public dataset, a government portal, data the team can collect in a night, synthetic data); the expected accuracy from published work, with the citation; what the model cannot do.
4. **Why India needs its own version.** Price point, language, connectivity, data, regulation, who the buyer is. If it copies a funded foreign startup, say exactly what is kept and what changes.
5. **Who has tried**, and the gap they leave.
6. **The business.** Buyer, what they pay today, price, a bottom-up market estimate with the arithmetic shown, the first ten customers.
7. **What a team could show by noon.** The overnight prototype, cut down to what is certain to work; the test that yields one honest measured number (what is measured, how many trials, against what baseline); the fallback if the main piece fails.
8. **Parts and cost**, if any hardware, split into "in a typical kit" and "bring or buy locally". Write "software only" where true.
9. **The hardest question a mentor will ask**, and the honest answer. Give three.
10. **Risks and what would kill it.**
11. **Verdict:** buildability overnight 1–5, strength as a business 1–5, share of the work that is AI/ML (rough per cent), and one line on who on a mixed team should lead it.

Depth matters more than polish: reason through the mechanism, name the actual model and dataset, show the arithmetic. If two approaches are plausible, pick one and say why. If the idea does not survive your own scrutiny, say so plainly and say what smaller version would.

Output: `research_notes/R5-design-0N.md`, one `## <ID> <name>` section per idea with headings 1–11. End with `## NOT CHECKED` and `Searches used: N`.
