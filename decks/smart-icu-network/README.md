# StepICU pitch deck (smart ICU network)

Source files for the 11-slide pitch deck built from `SPARK Night 2026 - smart ICU network, idea check.md`. The deck itself is a Slides artifact on claude.ai (private to its owner); download it as PowerPoint or PDF from Share › Export.

Framework: YC seed deck order, with Kevin Hale's "legible, simple, obvious" design rules. Colours: white background, near-black text, one grey, one accent (YC orange `#F26522`).

| # | Slide | File |
|---|---|---|
| 1 | Title | `project/slides/cover.html` |
| 2 | Problem: 621 district ICUs, 1 in 6 specialists | `problem.html` |
| 3 | Solution: protocol loop, specialists see only exceptions | `loop.html` |
| 4 | One night: on-site doctor runs it, specialist joins once | `night.html` |
| 5 | Insight: watching vs acting on time | `insight.html` |
| 6 | Same bed kit, swap the protocol file | `packs.html` |
| 7 | Business model and cost per bed | `money.html` |
| 8 | Market: TAM, SAM, SOM | `market.html` |
| 9 | Competition | `compare.html` |
| 10 | The product: one bed in detail, screen mock-ups | `product.html` |
| 11 | The ask: one district ICU for a 3-month pilot | `ask.html` |

- `project/deck.json` holds the slide order; `project/deck.css` holds the shared styles.
- Each slide's speaker notes (the `<aside>` at the end of the file) carry the spoken script, every source with its fact ID, and tags such as ASSUMPTION, OUR ARITHMETIC and search summary only.
- Prices and costs on slides 7 and 8 are assumptions to test in the pilot, not facts.
