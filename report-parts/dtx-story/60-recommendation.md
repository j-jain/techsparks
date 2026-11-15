## 6. Recommendation, risks and open questions

This chapter brings the story to its answer: what to do, how to say it, where the idea is weak, and what the team still must decide.

### 6.1 The recommendation

Build the home blood-pressure step loop tonight, and present it as the first protocol on a loop that can carry others. OUR VIEW, for three reasons.

1. **It is where the proof is strongest.** In the UK and US trials, pressure fell further than under usual care when a home reading led to a medicine change; in rural China, health workers stepping doses by protocol cut heart attacks, strokes and heart deaths, inside a programme that also gave cheaper medicines and paid for results; and an independent US review backed only the programmes that adjust medication (chapter 2.1).
2. **It is where India's gap is.** The government programme gets good control among patients who return, about half do not return, and only about one in five people with high blood pressure is controlled in its first nine districts (chapter 1). No Indian service was found that changes a dose from home readings, and no step logic was found in the government app's protocol model (chapter 1.5).
3. **It can be built and tested honestly by noon.** The state protocol is public, down to the doses and the 30-day interval (chapter 4.1), and the programme's own control-by-step figures give a base for a simulated cohort (chapter 5.4).

Make the engine load any protocol as data, so insulin becomes "same loop, new protocol" and heart failure is the expansion (chapter 4.8). Software builds the engine, the patient chat, the approval screen and the test harness. Hardware reads the cuff (chapter 4.3) and builds the clip, so a bad reading never triggers a dose change. Biology encodes the protocol and its safety branches, writes the test cases and owns the clinical story.

### 6.2 The pitch in one breath

OUR VIEW. "India's own blood-pressure protocol works when patients come back, and half do not. We bring the 30-day step home: a home reading that has been checked, the state's protocol run from a data file, a doctor's one-tap approval, and the change sent in the patient's language. Before any step-up we ask whether the medicine was taken. Every branch is tested, and the same loop is ready for the next protocol."

### 6.3 What you can say at noon, and what you cannot

| You can say | You cannot say |
|---|---|
| Every branch of two published protocols passes our tests. | The product is safe, validated or approved. |
| A simulation of ours, built on the programme's own figures, shows where the gain would come from. | The loop improves control. No patient has used it. |
| Readings from teammates flowed end to end, and this share passed the quality check. | These are clinical data. |
| A doctor approves every change; the software only drafts. | The software prescribes or treats. |
| It is a student prototype, not a medical device. | It complies with any rule. India's new guidance treats such software as a device (chapter 2.6). |

What we are not claiming: any benefit to patients, since tonight's results are code tests, our own simulation and teammates' readings; or that the loop is a cleared device, since India's guidance gives no exemption for tools only a clinician sees (chapter 2.6). The scores, the market model and the price are ours; no customer has been interviewed.

### 6.4 The three weak spots to own first

1. **Who pays.** Public treatment is cheap enough that a state will not pay app-scale prices, and outpatient insurance cover is tiny (chapter 1.5). Our price of ₹149 a patient a month is an ASSUMPTION, and at that price the US$100 million-a-year test fails in India alone (OUR ARITHMETIC, chapter 2.5). Companies that died abroad sold software without a payer (chapter 1.5).
2. **It will be regulated**, and a study on patients needs permission and ethics approval first [D2-04-F13, D2-04-F14]. The honest path is clinician-approved proposals at one partner clinic under ethics approval, then a licence.
3. **An Indian trial of clinic decision support found nothing.** In mWellcare, prompting nurses and doctors during visits added no significant gain over well-run usual care (chapter 2.1). The loop has to earn its value between visits, among the patients who do not return. If a pilot shows no gain in return rate or control, that result stops the project.

### 6.5 Why not the other options

OUR VIEW, from the scores and reasons in chapter 3.3.

| Option | Why it is not the first build |
|---|---|
| Insulin dose guidance | Good trials, but no open type 2 simulator for an honest test tonight [D1-06-F30], a real risk of low blood sugar, and a large medicine maker's dosing app already exists. Shown on paper as the second protocol. |
| Adaptive home rehabilitation | Easy to demo, but it matches in-person care without beating usual care, and Lupin says it already holds an Indian Class C licence for cardiac rehabilitation. |
| Heart-failure dose loop | Strong outcome proof and the largest unmet need far from a specialist [D1-01-F31, D1-01-F35], but it needs lab values, so no honest test tonight. The later protocol. |
| Breathing plan with a sensor | The dose change that works in asthma needs no sensor [D1-02-F37], and sensor inhalers failed commercially. |
| Warfarin self-dosing | The best proof of all, a small market, and no meter tonight. |
| Weight-loss injection companion | A hot market after generic semaglutide, no outcome evidence yet [D1-01-F41], and three Indian players already in. |
| Handgrip exercise dosed by a load-cell device | A drug-free arm, set aside late in the night: the one sham-controlled trial found no significant change [D3-08-F10], and the main device drew a US regulator's warning letter in 2019 [D3-08-F27]. A possible later arm (Appendix F). |

### 6.6 Pitching to the mentor

The mentor's fund (chapter 1.1) led a 2023 round in Wellthy, an Indian digital-therapeutics company [D3-06-F01]. By its chief executive's account, its first investment, in 2015, was CureApp, the Japanese company whose blood-pressure app is covered by insurance there (THEIR CLAIM) [D3-06-F26]. That app coaches lifestyle and does not change medicines [D3-06-F19]. The home step loop is the piece neither had: the reading changes the medicine. Say that plainly, and be ready for the question the Wellthy story raises: who pays.

OUR VIEW: he modelled outcome-based contracts for his master's thesis, so expect him to ask what outcome changes, by how much, and who checks it. He has promoted an 8-minute, no-slides pitch format (Appendix H): practise the whole loop that way.

**How to frame it** (OUR VIEW):

1. **One outcome, measured one way:** the share under 140/90 at 90 days among patients who would not have returned, set against the fall a US review counts as meaningful (chapter 2.1), with each reading checked for posture and repeats.
2. **The easiest wedge.** His partner asks for the "easiest" wedge into a large market [D2-07-F14]. Blood pressure is it: the largest patient pool (chapter 1), a cheap cuff (chapter 5.9) and a step protocol already in government text (chapter 4.1). The same engine loads insulin next.
3. **Prototype to product.** Tonight a tested loop; next a 90-day pilot. The partner says investors like to enter between an alpha prototype and a beta customer pilot.
4. **A real Japan angle.** Name only Panasonic's health and wellness theme [D2-07-F9], the CII healthcare delegation and the Intralink event (Appendix H). Claim no Japanese partner.
5. **Say the null result first:** mWellcare (chapter 2.1). Our loop works between visits, where that trial did not look.

| Question to expect | Honest answer |
|---|---|
| What outcome changes, by how much? | Point to HyperLink, the US trial of pharmacists adjusting doses from home readings (chapter 2.1). We have no patient data of our own. |
| Is this just a rules engine? | The rules are what the trials show works, and nobody runs them at home. The hard parts are trusting a home reading, telling a missed dose from a needed step-up, and proving safety; adherence tools alone failed (chapter 2.1). |
| Who pays? | Not known yet. Firms selling an app alone died (chapter 1.5). |
| Is it safe and legal? | A clinician approves every change; unsafe cases go up. The regulatory class is still open. |
| Will patients stay? | A clinician's referral keeps people in remote programmes longer (chapter 2.1); many women own no phone (chapter 1.3), so it must work on a shared one. |

**Five questions worth asking him:**

1. Your fund led Wellthy's 2023 round and Wellthy now sits inside TruDoc: who ended up paying for that kind of chronic-disease programme, and what would you do differently?
2. What evidence would you want before a pilot: 90-day control, or something harder?
3. Does anyone in the Panasonic programme or the CII corridor work on home measurement?
4. How does the campus pre-incubation route work, and can an Ashoka team enter it?
5. Could Biomoneta or Anaut share how they handled device approval?

### 6.7 Open decisions for the team

| Decision | Options | What would settle it |
|---|---|---|
| First customer | A private clinic chain; a district programme; a non-profit that runs hypertension care | Three conversations next week (discussion guide in Appendix F) |
| Who approves a step | A doctor only; later a health officer under a written order | A lawyer's answer. No order letting a health officer change a dose was found [D3-05-F30], and the telemedicine guidelines want the registered doctor to deliver the prescription directly (chapter 2.6) |
| How the reading comes in | Photo confirmed by the person (tonight); typed entry; Bluetooth with a suitable cuff (chapter 4.3) | Tonight's test of the photo reader on teammates |
| The home line | 135/85 at home for a protocol written for 140/90 in clinic (OUR DESIGN, chapter 4.3) | A clinician's signature on the protocol file |
| Open or closed | Give the engine to the public programme's open-source app; keep it proprietary | Who the first customer is |
| Second protocol | Insulin; heart failure | Whether a diagnostics partner for lab values can be found |

### 6.8 The next seven days

1. Interview one general doctor, two patients on blood-pressure medicine with a family member, one pharmacist and one health worker, using the guide in Appendix F.
2. Ask one clinic whether its doctor would approve proposals for ten of their own patients for two weeks (rung 2, chapter 5.7), and what paperwork they would need.
3. Put the three questions for a lawyer (Appendix E) to a lawyer or a regulatory consultant.
4. Rerun the simulation with engagement figures from the two-week test in place of assumptions.
5. Write up tonight's four results with their limits, and send them to the mentor with one clear ask.

### 6.9 What this document does not cover

Chapter 7 and the claim register (Appendix J) list what was not found or re-checked. The largest gaps: customer interviews, a measured public-private split of treatment, current specialist counts, and any Indian trial of home readings driving dose steps.

Full detail: Appendix F (options, frameworks, the handgrip arm), Appendix H (mentor and fund) and Appendix E (rules, questions for a lawyer).

OUR VIEW: the medicine is settled; payment and defence are not. A prototype alone is not fundable; the next proof is a signed pilot clinic, a doctor who signs the protocol, and a class answer from the regulator. Chapter 7 explains how this document was made and how far to trust it.
