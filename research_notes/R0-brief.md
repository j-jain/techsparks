# R0 — Brief for every research agent (SPARK Night 2026)

Read this whole file before you search. It is the fixed contract for the research.

## The event

SPARK Night, launch of TechSparks Ashoka 2.0, Ashoka University (Sonipat, Haryana). 13 Nov 2026 6:00 PM to 14 Nov 12:00 noon. An overnight deeptech buildathon: by noon a team must show (1) a clearly defined problem, (2) a working prototype, (3) some initial testing results, (4) a one-page "Deep Tech Thesis" on what was built and why it matters. Tracks: Bio & Health; AI & Systems; Frontier Hardware & Climate; Space Tech & Defence; Open Track. Prizes: builder grants up to ₹2 lakh, a slot in an Innovators Immersion Programme in Singapore (2027), and an investor pitch at Builders Fest. Food, building kits and quiet rooms are provided.

The team is a mixed one: computer science (vision, ML, LLMs, embedded, web) PLUS people who can do hardware (sensors, microcontrollers, 3D printing, simple circuits) PLUS people with a bio/wet-lab background. So hardware and bio prototypes ARE on the table.

The grant is ₹2 lakh, but the user does NOT want to be limited by that: the goal is a problem that is real, heavily proven in public, and the seed of a viable Indian business.

## What we are looking for

Real problems that people and firms in India complain about in public, loudly and repeatedly, where a deep-tech wedge (vision, sensing, a device, a bio assay, satellite or GNSS data, embedded systems, ML) could be the start of a solution. Breadth across fields is the point: do not collapse your field into one obvious problem. Report what the public actually says, not what you expected to find.

## Hard exclusions (do not report these even if you find proof)

- Anything in agriculture, fresh produce, food supply chain, cold chain, packhouses, hydroponics, farm-gate grading, canteen/kitchen food waste, dairy, fisheries as food.
- The user's own existing ideas: factory-floor voice-to-insight (FloorSe), kitchen waste weighing (Tarazu), factory CCTV vision for food plants, produce grading and shelf-life (Lot Life / FreshFlow).
- Manufacturing as a field is still OPEN for other (non-food) problems.

## Pre-filters (a problem must pass all three)

1. It is an India problem with Indian public evidence (Indian subreddits, Hindi or English YouTube, Indian news, Indian government data). A global problem counts only with Indian proof.
2. It has at least one conceivable deep-tech wedge. Pure marketplace or app ideas may be logged in one line but are down-weighted.
3. It is not excluded above.

## Proof tiers

- Tier A: 5 or more independent public threads, videos or posts with real engagement (hundreds of upvotes, thousands of views, long comment threads, or a LocalCircles / consumer-helpline statistic), PLUS at least one hard number from news or government data.
- Tier B: 2 to 4 independent public items, or many items but no hard number.
- Tier C: anecdotal, one post, or only expert opinion. Tier C does not advance past Round 1; still log it in one line.

"Independent" means different authors on different dates, not one viral post and its reposts.

## Sources to use (and what they are good for)

- Reddit via `site:reddit.com`: r/india, r/indiasocial, r/IndiaSpeaks, r/delhi, r/bangalore, r/mumbai, r/pune, r/hyderabad, r/kolkata, r/Chennai, r/legaladviceindia, r/indianstartups, r/developersIndia, r/IndianAcademia, r/indianmedicine, r/IndianWomen, r/CarsIndia, r/indianbikes, r/indiadiscussion, r/ElectricVehiclesIndia, r/IndiaInvestments. Capture upvotes and comment counts from the search snippet or by fetching old.reddit.com.
- YouTube via `site:youtube.com` (search in English AND in Hindi / Hinglish): capture the title, channel, view count and date from the snippet. YouTube pages themselves fetch poorly; say "view count from search snippet" rather than inventing one.
- Quora via `site:quora.com`, X / Twitter and Instagram ONLY through news coverage of viral posts or search-result snippets. Instagram is not fetchable; say so, do not fake Instagram proof.
- LocalCircles surveys (localcircles.com) are gold: sample size and percentage, with date.
- National Consumer Helpline statistics, consumer-court orders (indiankanoon.org, consumerhelpline.gov.in), RTI replies reported in news.
- Google Play Store review rants for apps in the space (snippets).
- Government data: PIB, MoSPI, NCRB (road deaths, cybercrime), NFHS-5, CPCB (air), CGWB (groundwater), NITI Aayog, Lok Sabha / Rajya Sabha questions (sansad.in), Economic Survey, sector regulators.
- Who tried before: Inc42, YourStory, The Ken, Entrackr, ET Tech, Mint, Tracxn/Crunchbase snippets. Note funding and whether the company is alive, pivoted or dead.
- Use WebSearch (standard mode by default; extended only for a niche query that came back empty) and WebFetch. Load them with ToolSearch before your first search. Do not use Nimble tools; they are not authorised in this session.

## Search budget (strict)

All agents in a round share ONE pool of about 200 web searches. Your allowance is stated in your task. Spend it on your highest-value questions first: public proof before market numbers, market numbers before competitor history. If you run out, write the gap as `NOT SEARCHED: <what>` rather than guessing. End your notes with the line `Searches used: N`.

## Citation rule

Every fact carries a URL, the date of the item (or "undated"), and one line on what it shows (e.g. "r/delhi, 1.2k upvotes, 340 comments, Nov 2025: residents describing AQI 450 days with kids"). Never cite a figure without the page it came from. Prefer primary pages over roundups. If a number comes from a search snippet and you could not open the page, say "(snippet)".

## Note schema for Round 1 (one file per agent, Markdown)

```
# R1-NN <field>  (agent: Sonnet, date 2026-11-03)

## Problem 1: <short name>
- Track: <one of the five>
- Who suffers: <people / firms, where, how often>
- How they cope today: <workarounds, what they pay now>
- Public proof (tier A/B/C):
  - <URL> — <date> — <engagement> — <what it shows>
  - ... (3 or more)
- Hard number: <stat> — <source URL, date>
- Who has tried: <startup / product — funding — alive / dead / pivoted — why it stalled, if known>
- Deep-tech wedge (one line): <what a mixed team could build>
- Overnight feasibility (1-5) and why:
- Rough market pointer: <affected units x plausible price, or a quoted market figure with source>
- Risks / regulation (one line):

## Problem 2: ...
(4 to 6 problems)

## Logged but weak (Tier C or non-deep-tech), one line each
- ...

## NOT SEARCHED
- ...

Searches used: N
```

## Style

Dense, factual, no filler, no marketing language. Hinglish quotes from posts are welcome in quotation marks (short). Do not write a conclusion or ranking; the coordinator ranks.
