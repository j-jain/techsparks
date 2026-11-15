# D3 brief: rules for claims-check agents

Read `D0-brief.md` in this folder first (the challenge, the fact rule, style). This file adds the rules for checking.

## Your job

Try to break each claim. Re-open the source for every fact you are assigned and compare what the note says with what the source says: the number, the unit, the year, the population, the comparator, the direction, and who said it. Where the cited page cannot be opened, find the same fact at another primary source (for journal papers use Europe PMC or NCBI E-utilities; for regulators the regulator's own page; for companies the filing or the company's page).

## Order of work

1. Every fact ID cited in `DT1-triage.md` and in `..\..\report-parts\dtx\05-decision-brief.md` that comes from your assigned notes. These are already in front of the team, so they come first.
2. Every fact in the Digest of each assigned note.
3. Every fact tagged SNIPPET that a later section is likely to use: upgrade it (open a page that shows the value) or mark it NOT FOUND.
4. Then the rest, as far as your allowance goes.

## Status labels

- `CONFIRMED`: the source says what the note says. Give the page you opened and today's date.
- `CORRECTED -> <new value, source, date>`: the note is wrong or imprecise. Say exactly what changes (for example a different denominator, a different year, lead investor against participant).
- `CONTESTED`: two credible sources disagree. Give both.
- `NOT FOUND`: you could not find a page that shows it. The writers will then leave it out.

Extra checks:
- People and companies: is the role or the status still true in November 2026? Namesake risk?
- Funding rounds: did the named fund lead or only take part?
- Trials: is the number the primary outcome or a secondary or post-hoc one? Is the comparison against usual care or against something else? Was the trial randomised?
- Percentages: what is the denominator?
- Quotes: are the words on the page exactly as quoted?

## Output

Create your note first, then append in batches of about 10 checks.

```
# <note code> Claims check: <which notes> (agent: <model>, 2026-11-13)

## Verdict
(150 words at most: how many checked, how many of each status, the corrections that change a sentence the team is already using, and a "never say" list.)

## Checks
| Fact ID | Claim as noted | Status | Verified value, source, date opened |
|---|---|---|---|

## Could not check
(fact IDs and why)

Searches used: N
```

Do not add new research topics. Do not rank options. Plain words, no em dashes.
