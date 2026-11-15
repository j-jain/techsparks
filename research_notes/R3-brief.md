# R3 — Brief for Round 3 agents (claims check and build feasibility)

Read `R0-brief.md` (event, exclusions, citation rule) and `T2-triage.md` (the eight finalists and why) first. Then the R2 file(s) named in your task. Everything you write carries a URL and a date; "(snippet)" if you could not open the page; "NOT FOUND" beats a guess.

Access notes: reddit.com is unreachable (use the Arctic Shift API `arctic-shift.photon-reddit.com/api/posts/search?...` sparingly, it rate-limits); YouTube view counts: fetch the watch page (`viewCount` in the page) or `returnyoutubedislikeapi.com/votes?videoId=<id>`. No Nimble tools. WebSearch standard mode.

## A. Claims-check agents (Sonnet) — 50 searches each

Purpose: nothing in the final report may rest on a number or link that does not hold. For each finalist assigned to you:

1. **Hard numbers.** Take every figure the R2 section uses in (a) proof dossier, (b) market size and (g) verdict (counts, ₹ figures, percentages, dates, survey sample sizes). Open the primary page (or the best available page) and mark each: `CONFIRMED` (value and date match) · `CORRECTED → <new value, source, date>` · `NOT FOUND` (page dead or figure absent) · `CONTESTED` (another credible source gives a different value; give both). Where R2 said "(snippet)", try to open the page now.
2. **Proof links.** For the 6–10 best proof items in (a): does the URL resolve, is the date right, is the engagement figure (upvotes / views / responses) plausible as of today? Mark `LIVE / DEAD / CHANGED`. Where R2 could not get Reddit counts, try once per finalist to get them.
3. **Round 3 unknowns.** Each R2 section ends with three unknowns. Answer the ones that web search can answer (ignore the ones that need a phone call or a bench test; say so). Spend up to a third of your budget here.
4. **Verdict on the evidence base.** One paragraph per finalist: does the Tier still hold, does the market arithmetic still hold, what single number should the report lead with, and what should it never claim.

Output file: `research_notes/R3-claims-0N.md`, one `## <ID> <name>` section per finalist, each with a table (Claim | R2 value | Status | Verified value / source / date), a "Proof links" table, an "Unknowns answered" list, and the verdict paragraph. End with `## NOT CHECKED` and `Searches used: N`.

## B. Build-feasibility agents (Opus) — 20 searches each

Purpose: turn each finalist's R2 section (f) "overnight wedge" into a plan a mixed CS + hardware + bio undergraduate team can execute between 6:00 PM on 13 Nov and 12:00 noon on 14 Nov 2026 at Ashoka University (Sonipat, Haryana). Building kits, food and quiet rooms are provided; assume the kits hold common maker parts (ESP32/Arduino boards, breadboards, jumper wires, basic sensors, relays, power supplies) but NOT specialist sensors, so anything specialist must be ordered by about 7 Nov to arrive in time. For each finalist:

1. **Bill of materials** with Indian sources and prices (robu.in, zbotic.in, electronicscomp.com, Amazon.in, thingbits.in, etc.; cite the listing URL and price; mark delivery-risk items), split into "bring / pre-order" and "expect in the kit". Total ₹.
2. **Hour-by-hour plan** 18:00 → 12:00 for a team of 4–6 (who does what: CS, hardware, bio), with the first demo-able milestone by ~02:00 and a cut-down fallback if a part fails.
3. **Test protocol** that yields the honest numbers R2 named in (f): exactly what to measure, how many trials, what to report (with a results-table template). Note any safety rule (no abused lithium cells, no transmitting, no live mains in the hall, no real gas).
4. **Demo script** (3 minutes) for the morning pitch, and the one-page **Deep Tech Thesis** outline: problem (with the two strongest numbers), why now, the deep-tech core, what was built, the measured result, the business (buyer, price, SAM), what ₹2 lakh over 3 months would prove, and the Singapore-immersion angle.
5. **Judge-proofing:** the three hardest questions a deeptech jury will ask (e.g. "Airveda already does this", "cheap receivers classify spoofing at 53–67%") and the honest answers.
6. **Pre-event checklist** (data to download, datasets, permissions such as a campus lift or a drone flight, accounts, calibration references).
7. **Feasibility verdict:** 1–5 on buildability overnight with reasons, and whether this is a "safe" pick (works for sure) or a "high-ceiling" pick (bigger story, more can go wrong).

Output file: `research_notes/R3-build-0N.md`, one `## <ID> <name>` section per finalist with headings 1–7. End with `## NOT CHECKED` and `Searches used: N`.
