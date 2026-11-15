# R4 — Brief for Round 4 agents (mentors, proptech, funded startups)

Date of this round: 12 November 2026. Read `R0-brief.md` first for the event, the proof tiers and the citation rule. This brief changes some of it. Where the two disagree, this brief wins.

## Why this round exists

The 3 Nov report found 8 checked problems for SPARK Night (13 Nov 6 PM to 14 Nov noon, Ashoka University). It never looked at three things, which this round covers:

1. **The mentors.** Who they are, what they fund, what they say in public, and so what they would want to see built.
2. **Proptech.** Indian property, housing and building problems with an AI, vision or sensing angle.
3. **What global investors just funded.** Deep-tech and AI startups backed since January 2025 by Y Combinator, a16z, Sequoia Capital and Peak XV, which could be applied in India or rebuilt as an Indian version.

The output is an **idea bank**, not a ranking. The coordinator writes the report; you gather cited facts.

## What changed from R0

- **No exclusions.** Farming, food, cold chain and every other field are open.
- **Flag overlaps instead of dropping them.** The team's lead already works on the areas below. When something you find sits close to one of them, add the line `Overlap: <area>`. Do **not** put these descriptions or any personal names of the team in a search query.
  - voice notes from factory-floor workers turned into insights and dashboards
  - weighing kitchen waste in hotels and canteens
  - fresh-produce freshness, shelf life, vision grading and lot tracking
  - CCTV vision AI for factories, food plants first
  - a fresh-produce supply business selling to hotels and restaurants, with a packhouse
- **Preference.** AI/ML first, applied to conventional problems (construction, property, factories, logistics, clinics, utilities, farming, government paperwork, shops). Hardware is allowed.
- **"Recent" means January 2025 onwards.** Prefer 2026.

## Access rules

- Load WebSearch and WebFetch with ToolSearch before your first search. WebSearch in `standard` mode; `extended` only for a niche query that came back empty.
- reddit.com is unreachable. Use the Arctic Shift API (`arctic-shift.photon-reddit.com/api/posts/search?...`) sparingly; it rate-limits.
- LinkedIn, Instagram and X posts usually cannot be opened. Use what the search snippet shows and mark it `(snippet)`. Never reconstruct a post you could not read.
- YouTube: view counts from the watch page (`viewCount`) or mark "(snippet)".
- No Nimble tools.
- **Search budget is strict.** Your allowance is in your task. End your notes with `Searches used: N`. If you run out, write `NOT SEARCHED: <what>`.

## Citation rule (unchanged, repeated because it matters)

Every fact carries a URL, the date of the item, and one line on what it shows. "(snippet)" if you could not open the page. `NOT FOUND` beats a guess. Never invent a quote: a quotation needs a page that contains those words.

## Identity rule for people

Several mentor names are common. Before you attribute anything to a person, confirm it is the same person: same firm, same city, same photo caption or bio line. Give at least two independent sources tying the person to the role. If only one exists, say `single source`. If two people share the name, say which one you rejected and why.

## Note schemas

### A. Mentor notes (`R4-01`, `R4-02`)

```
## <Name> — <current role, firm>
- Identity check: <2+ sources; any namesake rejected>
- Background: <career in 2–3 lines, with dates>
- Firm / fund: <thesis, stage, cheque size, fund size, sectors> — URLs
- Portfolio worth knowing: <company — what it does — year> (deep tech and AI first)
- What they have said, 2024–26: <date — where — the point, quoted or paraphrased — URL> (as many as you can verify)
- Says they want: <...>
- Says they dislike / red flags: <...>
- Questions they ask founders: <stated or evident from interviews>
- Link to Ashoka / SPARK Night: <...>
- INFERENCE (label it): what this person would want to see built overnight, and which problems they would want solved. Two to four lines, each tied to a fact above.
```

End with `## The institutions` covering whatever your task names, then `## NOT FOUND` and `Searches used: N`.

### B. Proptech note (`R4-03`)

Use the Round 1 problem schema from `R0-brief.md` (who suffers, how they cope, public proof with tier, hard number, who has tried, wedge, overnight feasibility, market pointer, risks). Add two lines to each problem:

- `AI/ML core:` what model, trained on what data, and where that data comes from in India.
- `Buyer:` who signs the cheque, and what they pay today for the workaround.

Eight to ten problems. Then `## Logged but weak`, `## NOT SEARCHED`, `Searches used: N`.

### C. Funded-startup notes (`R4-04`, `R4-05`)

```
## <Startup> — <one line: what it does>
- Backers and round: <investor(s), round, amount, date> — URL
- Problem, customer, and how the tech works: <ML core, any hardware>
- Traction signals: <customers, revenue, pilots, if public>
- Does India have this problem? <one hard number> — URL
- Indian equivalents: <name — funding — alive/dead> or "none found"
- What differs in India: <price point, data, language, connectivity, rules, buyer>
- India version sketch: <2–3 lines>
- Overnight-demo potential (1–5) and why
- Overlap: <area, if any>
```

Selection rule: prefer AI/ML applied to conventional industries (construction, property, manufacturing, logistics, healthcare delivery, energy and utilities, farming and food, government and compliance, education, insurance and lending operations, small retail). Skip developer tools, foundation-model labs, crypto, consumer social and pure chat wrappers; log those in one line at most. Aim for 18–22 full entries, then `## Logged in one line`, `## NOT SEARCHED`, `Searches used: N`.

## Style

Dense, factual, no filler, no marketing language. Do not rank and do not write a conclusion; the coordinator does that.
