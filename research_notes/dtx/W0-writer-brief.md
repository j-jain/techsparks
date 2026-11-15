# W0 writer brief: rules for every writer of a document part

You turn research notes into one part of a long working document for a student team. You do no web research. Read `D0-brief.md`, `DT1-triage.md` and `DT2-spine.md` in this folder first; the spine holds the argument and you must not change its positions.

## The reader

Third-year university students (computer science, hardware, biology) in an overnight buildathon, and a venture-fund mentor who may skim it later. English is a second language for some. They want to know what is true, how sure we are, and what to do.

## Facts

1. **Use only facts that are in the notes.** No number, name, date, quote or claim from your own memory. If the notes do not have it, write `NOT RESEARCHED` or leave it out.
2. **Cite every fact by its ID in square brackets right after the sentence or clause**, for example `[D1-01-F02]`. Several IDs: `[D1-01-F02, D1-01-F04]`. Write the full ID each time (no ranges, no "F02-F04"). A script later turns each ID into a link to its source.
3. **Carry the status.** If a fact is SNIPPET in the notes, say "(search summary only)" in the text. If a claims-check note (files starting `D3-`) corrected a fact, use the corrected value and cite both IDs. If it marked a fact NOT FOUND, leave the fact out.
4. **Tags for numbers that are not published facts:** OUR ARITHMETIC (show the sum), OUR ESTIMATE, ASSUMPTION, THEIR CLAIM (a company about itself), EXAMPLE (mock-up data). A judgement of ours is marked OUR VIEW once at the start of the paragraph or table.
5. **Conflicting figures** are both given, with their years, and the reason they differ if the notes give one.
6. **Dates** on anything that changes: prices, laws, funding, whether a company is alive.
7. **Trials:** always say who was compared with whom, how many people, where, and how long. Say when a result was null. Say when a study was not randomised or was run by the company.

## Writing

- Plain words and short sentences. Explain each technical term once, in brackets, the first time: "HbA1c (a blood test showing average sugar over about three months)".
- Bullets and tables for anything with parallel items. A table for every comparison of three or more things.
- Each section opens with one or two sentences that say what the section shows. Each ends with a short "So what for us" paragraph marked OUR VIEW.
- Headings: your part starts with one `## ` heading exactly as given in your task. Inside it use `### ` and `#### ` only.
- No em dashes, no exclamation marks, no rhetorical questions, no "Imagine".
- Do not use these words: synergy, revolutionary, game-changing, AI-powered, seamless, leverage, utilise, robust, cutting-edge, innovative, streamline, optimise, empower, unlock, world-class, best-in-class, next-gen, ecosystem, "solution" for the product. Also avoid: landscape, journey (except "user journey"), holistic, delve.
- Numbers: Indian grouping and units for rupees (₹2,600; ₹844 crore; 21,895 patients; 3.3 lakh). Dollar figures as published. Ranges with a plain hyphen: ₹760-980, 37-42%. Write "a month", not "/mo".
- Legal statements: say what the text says and whose question it remains. Never write "compliant", "100%" or "zero risk".
- Medicines and doses only as quoted in the notes.
- Keep to your word budget within 10%.

## Pictures

Where your task names a picture, place it with `![short description](adaptive-care-pictures/<file>.png)` and one italic caption line under it. Mock-up screens are captioned "Mock-up with example data."

## Output

Write your part to the file path given in your task. Create the file first with the heading, then append section by section. When done, reply with: the word count, any place where the notes were too thin to write what was asked, and any fact you wanted but could not find in the notes.
