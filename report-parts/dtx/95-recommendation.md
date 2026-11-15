## L. Recommendation, risks and open questions

### The recommendation

Build the home blood-pressure step loop tonight, and present it as the first protocol on a loop that can carry others. OUR VIEW, for three reasons.

1. **It is where the proof is strongest.** When a home reading leads to a medicine change, pressure falls by 5 to 10 mmHg more than usual care in the UK and US trials [D1-01-F01, D1-01-F02, D1-01-F04]. When health workers were allowed to step doses by protocol in rural China, heart attacks, strokes and heart deaths fell over 4 years with no rise in falls or kidney harm, though that programme also gave free or cheaper medicines and paid for results [D1-01-F09, D1-01-F38]. An independent US review backed only the programmes that adjust medication [D1-01-F39].
2. **It is where India's gap is.** The government programme gets good control among patients who return, and about half do not return [D1-03-F10]. In its first nine districts 21.2% of people with high blood pressure are controlled [D1-01-F11]. No Indian service was found that changes a dose from home readings, and no step logic was found in the protocol model of the government's open-source app [D1-06-F40].
3. **It can be built and tested honestly by noon.** The state protocol is public, down to the doses and the 30-day interval [D1-06-F14]. The programme's own control-by-step figures give a base for a simulated cohort [D1-06-F04]. The build plans are in part J.

### The pitch in one breath

OUR VIEW. "India's own blood-pressure protocol works when patients come back, and half do not. We bring the 30-day step home: a home reading that has been checked, the state's protocol run from a data file, a doctor's one-tap approval, and the change sent in the patient's language. Before any step-up we ask whether the medicine was taken. Every branch is tested, and the same loop is ready for the next protocol."

### What we are not claiming

- **No benefit to patients has been shown.** Tonight's results are code tests, a simulation of our own, and readings from teammates.
- **It is not a medical device and not cleared by anyone.** India's July 2026 guidance treats software of this kind as a regulated device, with the class depending on how the condition is graded, and gives no exemption for tools that only a clinician sees [D2-04-F01, D2-04-F03, D2-04-F04, D2-04-F07]. A study on patients before a licence needs permission and ethics approval [D2-04-F13, D2-04-F14].
- **The scores, the market model and the price are ours.** No customer has been interviewed.

### The three weak spots, said plainly

1. **Who pays.** Public-sector medicines for blood pressure cost about ₹200 a patient a year [D2-01-F12], so a state will not pay app-scale prices. Outpatient insurance cover is tiny (search summary only) [D2-05-F10]. Our price of ₹149 a patient a month is an ASSUMPTION, and at that price the US$100 million-a-year test fails in India alone: it needs 52.7 lakh paying patients against 41.9 lakh in the serviceable market (OUR ARITHMETIC, part F2). The companies that died abroad sold software without a payer [D1-02-F42, D1-02-F44].
2. **It will be regulated.** See above. The honest path is clinician-approved proposals at one partner clinic under ethics approval, then a licence.
3. **An Indian trial of clinic decision support found nothing.** In mWellcare, prompting nurses and doctors during visits added 0.98 mmHg, not significant, over well-run usual care [D1-01-F46]. Our loop has to earn its value between visits and among the patients who do not return. If a pilot shows no gain in return rate or control, that is the result that stops the project.

### Why not the other options

OUR VIEW, from the scores in part I.

| Option | Why it is not the first build |
|---|---|
| Insulin dose guidance | Good trials [D1-01-F13, D1-01-F14], but no open type 2 simulator for an honest test tonight [D1-06-F30], a real risk of low blood sugar, and a dosing app from a large medicine maker already exists [D1-04-F09]. Shown tonight as the second protocol on paper. |
| Adaptive home rehabilitation | Easy to demo, but software rehabilitation matches in-person care without beating usual care [D1-02-F07, D1-02-F54], and Lupin says it already holds an Indian Class C licence for cardiac rehabilitation [D1-04-F15]. |
| Heart-failure dose loop | Strong outcome proof [D1-01-F27], and the largest unmet need far from a specialist [D1-01-F31, D1-01-F35]. It needs lab values, so it cannot be tested honestly tonight. The later protocol. |
| Breathing plan with a sensor | The dose change that works in asthma needs no sensor [D1-02-F37], and sensor inhalers failed commercially [D1-02-F41]. |
| Warfarin self-dosing | The best proof of all [D1-02-F05], a small market, and no meter tonight. |
| Weight-loss injection companion | A hot market after generic semaglutide [D1-04-F10], no outcome evidence yet [D1-01-F41], and three Indian players already in. |
| A drug-free arm: handgrip exercise dosed by a load-cell device | Checked late in the night and set aside. A 2023 analysis of 270 trials put isometric exercise at 8.24 mmHg lower systolic pressure [D3-08-F01], and handgrip alone at 5.38 mmHg across 31 studies [D3-08-F05]. But the one sham-controlled handgrip trial found no significant change [D3-08-F10], the effect on 24-hour pressure is not significant [D3-08-F07], and the main device sold for it received a US regulator's warning letter in 2019 [D3-08-F27]. A possible later arm once the evidence firms up; European guidance names isometric training as a complement to aerobic exercise [D3-08-F21]. |

### Open decisions for the team

| Decision | Options | What would settle it |
|---|---|---|
| First customer | A private clinic chain; a district programme; a non-profit that runs hypertension care | Three conversations next week (part I has the discussion guide) |
| Who approves a step | A doctor only; later a health officer under a written order | A lawyer's answer. No order letting a health officer change a dose was found [D3-05-F30], and the telemedicine guidelines require the registered doctor to deliver the prescription directly [D2-04-F17] |
| How the reading comes in | Photo of any cuff's screen, with the person confirming the digits (tonight's route); typed entry as fallback; Bluetooth only if a suitable cuff is in hand | Tonight's test of the photo reader on teammates |
| The home line | 135/85 at home for a protocol written for 140/90 in clinic [D2-01-F1, D1-06-F14]; applying the clinic protocol to home readings is OUR DESIGN | A clinician's signature on the protocol file |
| Open or closed | Give the engine to the public programme's open-source app; keep it proprietary | Who the first customer is |
| Second protocol | Insulin; heart failure | Whether a diagnostics partner for lab values can be found |

### The next seven days

1. Interview one general doctor, two patients on blood-pressure medicine with a family member, one pharmacist and one health worker, using the guide in part I.
2. Ask one clinic whether its doctor would approve proposals for ten of their own patients for two weeks (rung 2 in part J), and what paperwork they would need.
3. Put the three questions at the end of part F2 to a lawyer or a regulatory consultant.
4. Rerun the simulation with engagement figures from the two-week test in place of assumptions.
5. Write up tonight's four results with their limits, and send them to the mentor with one clear ask.

### What this document does not cover

Part M lists what was not found and what was not re-checked. The largest gaps are customer interviews, a measured split of public and private treatment, current specialist counts, and any Indian trial of home readings driving dose steps.
