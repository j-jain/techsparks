# R2 — Brief for the Round 2 verification agents (Opus)

You verify, size and design. Round 1 found the problems; your job is to find out whether each one is real, unsolved, sellable and buildable overnight, with numbers that will survive a claims check. Read `R0-brief.md` first (event, exclusions, citation rule); this file adds what Round 2 needs.

## Budget and access
- Your allowance is **40 web searches for all three problems**. Spend them where Round 1 left the biggest gaps (listed in your task), roughly 13 each; it is fine to spend 20 on one if that is where the uncertainty is. End your notes with `Searches used: N`.
- reddit.com is blocked for WebSearch's domain filter and for WebFetch. Round 1 agents got Reddit engagement counts through mirrors; try these in order: `https://reddit.sentinel-team.org/posts/<postid>/snapshots/...` (search the mirror), `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&title=<words>&limit=25&sort=desc` (JSON; scores may be stale), redlib instances such as `https://axebps-redlib.hf.space/r/<sub>/comments/<id>/` and `https://lr.us.psf.lt/r/<sub>/comments/<id>/`. Quote upvotes and comment counts with the snapshot date.
- YouTube view counts: `https://returnyoutubedislikeapi.com/votes?videoId=<id>` returns JSON with `viewCount` and `likes`; Invidious instances expose `/api/v1/videos/<id>`. Use them for the two or three most-cited videos per problem; say "(view count via returnyoutubedislike API, <date>)".
- No Nimble tools. WebSearch standard mode unless a niche query returns nothing.

## Deliverables per problem (use these exact headings)

### (a) Proof dossier
Count how many *independent* public items you can now stand behind (different authors, dates). List the 6–10 best, each as `URL — date — engagement — one line on what it shows`. Add Reddit/YouTube engagement where Round 1 could not. Give the two or three strongest hard numbers with their primary source. State the final tier (A/B/C) and why.

### (b) Market size
Bottom-up arithmetic, shown line by line: affected units (sourced) × plausible price (sourced or clearly marked assumption) = TAM; a realistic serviceable slice; who pays today and how much. Give ₹ crore figures and name the buyer (consumer, RWA, firm, insurer, state, central). If a published market figure exists, quote it with source and say whether you believe it.

### (c) Competitive map
Indian and global products that attack this problem: name, what they do, funding (with source), status (alive / pivoted / dead) and why they have not closed the gap. Include government programmes. Be specific about what they do NOT do: that is the gap.

### (d) Solution approaches (2–3, distinct)
For each: the deep-tech core, what the mixed team (CS + hardware + bio) builds, the first customer, the unit economics guess, the moat. At least one approach should use the hardware or bio capability. Say which approach you would pick and why.

### (e) Regulatory and safety gates
What certification, law or data-access gate stands between the prototype and a sale (CDSCO, BIS, UIDAI, WPC, DGCA, state acts, DPDP). Which gates block the overnight demo (none should) versus the business.

### (f) Overnight wedge
What exactly the team can demo by noon on 14 Nov with building kits and off-the-shelf parts; what "initial testing result" is honestly reachable in ~14 hours (a number, not a claim); what the one-page Deep Tech Thesis would argue.

### (g) Verdict
One paragraph: is this real, unsolved, sellable, buildable? Score 1–5 on proof, market, feasibility, unsolved gap, deep-tech, risk. Then the three biggest unknowns that Round 3 should check.

## Rules
- Build on the Round 1 note for each problem (path given in your task); do not redo what it already sourced, extend it. Flag any Round 1 figure you now believe is wrong, with the better source.
- Every number carries a URL and a date. "(snippet)" if you could not open the page. "(my arithmetic)" for your own multiplication. "NOT FOUND" beats a guess.
- No marketing language. Short Hinglish quotes from real posts are welcome in quotation marks.
- Note file: one Markdown file for your three problems, `# R2-0N <set name> (agent: Opus, date 2026-11-03)`, one `## Problem: <name>` section per problem with the (a)–(g) headings, then `## NOT SEARCHED` and `Searches used: N`.
