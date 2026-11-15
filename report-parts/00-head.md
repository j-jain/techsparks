# SPARK Night 2026 — problems worth attacking, and the proof behind them

*Research for the TechSparks Ashoka 2.0 overnight deeptech buildathon, 13–14 November 2026. Compiled 3 November 2026 from three rounds of research (62 problems found, 15 verified, 8 finalists claims-checked and build-planned). Working files: `research_notes\` beside this report; every URL in `SPARK Night 2026 - source register.xlsx`.*

## 1. Executive summary

Across ten fields and 62 proven problems, eight survived verification as real, loud in public, deep-tech-shaped, sellable, and buildable between 6 PM and noon. Three stand out, for different reasons:

**1. Lift black-box (Frontier Hardware) — the recommended pick.** Half of India's ~6 lakh society lifts sit outside manufacturer monitoring; 46 % of users were stuck in the last year (LocalCircles, Jul 2026); Pune inspected 9 % of its 61,521 lifts in five months. Two state Lift Acts now make resident associations responsible for a maintenance record that does not exist — Maharashtra's came into force on 1 November 2026, twelve days before the event. A ₹15 k read-only retrofit sells into a ₹2,400–4,800 cr-a-year maintenance pool with a buyer named by law; the overnight build (₹10 k of parts, a model shaft with injected faults) yields precision, recall and latency numbers by noon. The widest market and the clearest "why now" in the set.

**2. Street-dog re-ID (AI & Systems / Bio & Health) — the loudest proof and the cheapest build.** 37 lakh dog bites in 2024 (+70 % in two years), rabies deaths a hundred times the official count, a Supreme Court that has ordered compliance reports for 17 November — three days after SPARK Night — and cities paying ₹700–1,870 per sterilisation they cannot verify. Phone-photo re-identification plus mark–resight statistics turns "we sterilised X dogs" into "ward Y is at 64 % ± 8 %", with no catching, collars or chips. ₹500 of parts; the one honest unknown — re-ID accuracy on look-alike Indian street dogs — is exactly what the night can measure, and nobody has published it.

**3. Digital-arrest call-guard (AI & Systems) — the biggest story, and a payer created two weeks ago.** Seniors lost ₹4,005 cr to cyber fraud in 2025; no app on Android or iOS may hear a call; on 29 October 2026 the Supreme Court directed that RBI's rules must make banks compensate victims where due diligence failed, with directions due by 30 November. A ₹3,600 speakerphone puck that spots the Hinglish scam script on-device and alerts the family is the demo; the bank that must now pay for failures is the customer.

Close behind, and better for a particular team: the **indoor/outdoor PM pair** (the surest demo, 5/5, in the week Delhi's air is at its worst, but a seasonal consumer-hardware market in which Airveda already claims a purifier verdict); the **counterfeit-medicine checker** (the bio team's best sellable problem, aimed at hospital oncology goods-receipt with a 91–100 % published sensitivity for wrong-API fakes, provided a bench test before the event shows cheap spectral sensors can tell white tablets apart); the **smart-meter witness** (2.9 M people watched a home test of whether their meter runs fast; easiest build; but the law already gives a free check meter and the meters are not wrong, so the product is a bill explainer); the **GNSS integrity node** (the Space-track pick: ~300 interference reports a month around Delhi and no ground sensor anywhere, a $400-class receiver that flags 99 % of interference, and a civil market of eight airports); and the **EV charging-bay monitor** (the most unsolved — nobody watches a bay — but the weakest proof and a buyer waiting on Haryana's unwritten fire rules).

How to choose between them: a hardware-heavy team with a lift to instrument takes 1; a CS-heavy team takes 2; a team that wants the room on its feet takes 3; a team that cannot afford a failed demo takes the PM pair; a team with a bio member who wants to lead takes the medicine checker.

| Rank | Finalist | Track | Score | TAM / SAM (₹ cr) | Overnight BOM | Build | Why now |
|---|---|---|---|---|---|---|---|
| 1 | Lift black-box | Frontier Hardware | 4.15 | 900 + 180/yr · 184 | ≈ 10,000 | 4/5 high-ceiling | Maharashtra Lift Act in force 1 Nov 2026; UP Act registrations |
| 2 | Street-dog re-ID | AI & Systems | 3.95 | 77–125/yr · 20/yr | ≈ 500 | 4/5 safe | SC compliance reports due 17 Nov 2026 |
| 3 | Indoor/outdoor PM pair | Frontier Hardware & Climate | 3.90 | 1,050 + 210/yr · 36 | ≈ 8,000 | 5/5 safe | Delhi AQI season now |
| 4 | Digital-arrest call-guard | AI & Systems | 3.80 | 160–300/yr (SAM) | ≈ 3,620 | 4/5 safe | SC order 29 Oct 2026 on bank liability |
| 5 | Counterfeit-medicine checker | Bio & Health | 3.70 | 595/yr · 60/yr | ≈ 7,900 | 4/5 safe | Aug–Sep 2026 oncology rackets |
| 6 | Smart-meter witness | Frontier Hardware | 3.70 | 580 · 160 | ≈ 6,600 | 4/5 safe | 3.92 lakh complaints, Maharashtra Jul 2026 |
| 7 | GNSS integrity node | Space Tech & Defence | 3.50 | 33 + 8/yr · 2 | ≈ 5,000 | 3/5 high-ceiling | 623 Delhi reports Jan–Feb 2026 |
| 8 | EV charging-bay monitor | Frontier Hardware & Climate | 3.40 | 1,176 · 235 + 47/yr | ≈ 9,860 | 4/5 safe, capped | Haryana code Jun 2026; fire rules pending |

Everything in this report rests on public evidence that was re-opened and re-checked; where a Round 1 or Round 2 number did not survive, the correction is stated in the finalist's section. The thirteen near-misses (section 4) and the full longlist of 62 (Appendix A) are kept so the choice can be revisited.

