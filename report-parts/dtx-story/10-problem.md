## 1. The problem

This chapter tells the problem as a story, before any answer: what the fund asked for, who it is about, why their care breaks down between visits, what patients and doctors say, and why the market has not fixed it.

### 1.1 Who set the challenge and what it really asks

The challenge was set for SPARK Night (13-14 Nov 2026, Ashoka University) by Beyond Next Ventures, a fund that backs founders solving social issues with deep science and deep tech, and that works across Japan and India [D2-07-F8]. The event poster names as challenge mentor Karthik Varada, Senior Associate in the fund's India investment group, based in Bengaluru [D2-07-F1, D2-07-F2, D2-07-F3]. The fund's words:

> We need ways to manage chronic disease burden at scale despite limited access to resources, specialists and irregular clinical follow-ups. Patients need treatment methods that responds to their specific condition, and will remain adaptive to patient needs between appointments. How can digital therapeutics use rapid feedback from medical devices or biomarkers to continuously personalise care, thereby bringing measurable improvements in health outcomes to patients who cannot access frequent specialist support? The opportunity is to extend effective treatment into everyday life, beyond monitoring and reminders.

Read phrase by phrase, the challenge sets six requirements (our reading, with where the evidence is).

| The fund's words | What a product must do (OUR VIEW) | Evidence |
|---|---|---|
| "rapid feedback from medical devices or biomarkers" | Use a signal that moves within days of a treatment change and is cheap and correct to measure at home. | Chapter 2.3 |
| "continuously personalise care" | Recompute the treatment from this patient's readings: the protocol step (a protocol is a written step-by-step treatment plan), the response to the last step, whether the medicine was taken, and what is unsafe. | Chapter 2.3 |
| "adaptive to patient needs between appointments" | Change the treatment without waiting for the next visit. | Chapter 1.3 |
| "measurable improvements in health outcomes" | Move one endpoint (the result a trial is judged on) within 90 days, past an accepted threshold for "clinically meaningful". | Chapter 2.1 |
| "patients who cannot access frequent specialist support" | Move the routine decision to a general doctor, nurse or health worker under a written protocol. The specialist owns the protocol and sees the exceptions. | Chapter 1.3 |
| "beyond monitoring and reminders" | Reach adaptive depth 4: the therapy itself changes. | Below, and chapter 2.1 |

#### What "beyond monitoring and reminders" rules in and out

This document sorts every product on an "adaptive depth" scale from 0 to 4: how far the product changes treatment. The fund names levels 1 and 2 and asks to go beyond them. OUR VIEW: it is asking for level 4.

| Level | What it means | Examples in the notes |
|---|---|---|
| 0 | Uses no patient data | The Nerivio migraine wearable, switched on by the patient, rated 0-1 [D1-02-F12] |
| 1 | Shows data | Pocket ECGs in India (search summary only) [D1-04-F32]; Omron VitalSight abroad [D1-01-F39] |
| 2 | Sends reminders or generic content | India's government Simple app, with overdue lists and reminder messages [D3-05-F03]; the Medisafe reminder app abroad |
| 3 | Coaches from the person's own data | Sugar.fit, BeatO and Fitterfly in India [D1-04-F04, D1-04-F06, D1-04-F07]; CureApp HT in Japan |
| 4 | Changes the therapy: a dose, a protocol step, an exercise prescription | In India, only Sanofi's My Dose Coach was found, its Indian results unconfirmed [D1-04-F09]; abroad, d-Nav and insulin pumps [D1-05-F41] |

The line between 3 and 4 matters most: level 3 changes the advice (what to eat, how to exercise), level 4 changes the prescription (a new dose or protocol step). A clinician approving each change keeps a product at level 4. The test: after the software runs, the prescription is different. OUR VIEW: level 4 is the entry condition, however good the sensor.

#### The loop: sense, decide, confirm, act, learn

A product at level 4 runs a loop of five stages. Monitoring products stop after the first.

- **Sense.** A home device gives a number, valid only if it was taken correctly. Level 1 products stop here.
- **Decide.** Software applies a written protocol to this patient's readings and proposes the next step. Coaching apps decide advice, not doses (chapter 1.5).
- **Confirm.** A doctor, nurse or health worker approves each change; unsafe cases go to a specialist.
- **Act.** The patient gets the new dose, medicine or exercise level.
- **Learn.** The next readings show whether it worked, and the loop runs again.

![The difference between monitoring and a therapy loop](adaptive-care-pictures/00-the-loop.png)

*Diagram: monitoring stops at the reading; a therapy loop sends the reading back as a changed treatment.*

OUR VIEW: the fund asks for a routine treatment decision between visits, from a home reading, by someone the patient can reach. The rest of this chapter shows who needs that decision and why it does not happen today.

### 1.2 Who it is about and how big it is

In India, chronic disease "at scale" means high blood pressure and diabetes first. The surveys disagree because they count different ages, use different blood-pressure rules or survey bases, and ran in different years, so each figure is given with its source and none is picked over the others.

| Condition | Figure | Year of data | Who was counted |
|---|---|---|---|
| High blood pressure | 35.5% | 2008-2020 | ICMR-INDIAB survey, adults 20+, blood pressure measured, 113,043 people in 31 states and union territories [D1-03-F01] |
| High blood pressure | 315 million people, a 2021 projection by the survey's investigators, not a count in the paper | Projected to 2021 | Same study [D1-03-F02] |
| High blood pressure | 22.6%; 24% of men, 21% of women (search summary only) | 2019-21 | NFHS-5 (National Family Health Survey), ages 15+ [D1-03-F03, D1-03-F04] |
| High blood pressure | 45.9% | 2017-19 | LASI (Longitudinal Ageing Study in India), adults 45+, 72,262 people [D1-03-F25] |
| Diabetes | 11.4%; prediabetes 15.3% | 2008-2020 | ICMR-INDIAB, adults 20+ [D1-03-F01] |
| Diabetes | 101 million; prediabetes 136 million, 2021 projections by the survey's investigators, not counts in the paper | Projected to 2021 | Same study [D1-03-F02] |
| Diabetes | 89.8 million (age-standardised 10.5%); 156.7 million projected for 2050 | 2024 | IDF Diabetes Atlas, adults 20-79 [D1-03-F28] |
| Heart failure | 1.3-4.6 million cases, or about 8-10 million (about 1% of the population; search summary only); no national survey | 2010; 2016 | Reviews built from local and disease-specific data [D3-07-F24, D3-07-F25] |

Other long-term conditions are large too. COPD (chronic lung disease) and asthma had 55.3 million and 37.9 million cases in 2016 (search summary only) [D1-03-F36]. The Global Burden of Disease study put India's stroke cases at 9.4 million in 2021, up from 4.4 million in 1990 (press report quoting the authors) [D3-07-F26]. Heart failure has no national count, but its registries show a treatment gap: in the National Heart Failure Registry (10,851 acute patients, 53 hospitals, 21 states), 47.5% of eligible patients received guideline drugs, and 1-year death was 22.1% [D1-01-F47, D1-01-F48].

OUR VIEW: on any count, blood pressure is the largest pool.

#### Knowing, treated, controlled

A care cascade follows people with a condition through four steps: has it, knows it, is treated, is controlled. India's government hypertension programme, the India Hypertension Control Initiative (IHCI), surveyed the same nine districts twice, with no comparison districts.

![Share of adults with high blood pressure who know, are treated and are controlled, 2018-19 and 2023-24](adaptive-care-pictures/22-india-cascade.png)

*Chart: in the first nine districts of India's hypertension programme, 21.2% of adults with high blood pressure were under control in 2023-24, up from 14.5% in 2018-19 [D1-01-F10, D1-01-F11].*

In the same surveys, awareness rose from 52.4% to 58.5% and treatment from 40.8% to 44.7%, among 7,047 and then 7,324 people with hypertension [D1-01-F10, D1-03-F12]. In two districts control was under 5% at the start [D1-01-F10]. Nationally, a preprint on the 2019-21 family health survey (1.69 million adults) counts 36.7% of all people with hypertension as aware, 17.7% as treated and 9.1% (about 1 in 11) as controlled [D1-03-F07]. Counted only among people aged 15-49 who are already on drugs, the same survey gives 73.7% controlled [D1-03-F06]; the ages and the denominators (the group a percentage is taken of) differ, so the two figures do not compare. For diabetes, 43% of cases, about 38.6 million, were undiagnosed in 2024 [D1-03-F28].

#### Treatment is not control

Getting people onto medicine is not enough. Tamil Nadu's doorstep programme, Makkalai Thedi Maruthuvam, was surveyed in 6,856 adults aged 30 and over across all 38 districts (paper abstract, 2025; a news report gives 6,809). Screening reached 79.4% for diabetes and 82.6% for hypertension, and over 95% of diagnosed people were on treatment. Yet control rates were 9.8% for diabetes and 35.4% for hypertension; the abstract does not say whether these are shares of everyone with the disease, of the diagnosed or of the treated [D1-03-F09].

OUR VIEW: two steps leak, diagnosis and control. The step from "treated" to "controlled" depends on the dose being raised and the medicine being taken.

#### The world and Japan

Low control is a world problem. About 1.4 billion people aged 30-79 have hypertension; 44% do not know it, 23% are controlled, and two-thirds live in low- and middle-income countries (2024) [D1-03-F32]. There are 830 million adults with diabetes, and 59% of those aged 30 and over are not on diabetes medicine (2022) [D1-03-F33]. Japan, the fund's home, has about 43 million people with hypertension, about 31 million (73%) of them poorly controlled (2010 base, cited for 2017; search summary only) [D1-03-F47], and 29.4% of its people were aged 65 or over in September 2025 (search summary only) [D1-03-F48]. OUR VIEW: "treated but not controlled" is the gap in Japan too, so the problem is not only Indian.

### 1.3 Why care breaks down between visits

India does not lack programmes. It already screens and treats at large scale through free public programmes. The breakdown comes after the first prescription, in the weeks between visits.

#### A large system that sees people once

| Programme | Scale (date) |
|---|---|
| National NCD (non-communicable disease) screening | 41.5 crore people screened for hypertension and 41.3 crore for diabetes (cumulative, Aug 2026) [D1-03-F20] |
| "75 by 25" (75 million on standard care by 2025) | 42.01 million hypertension patients put on standard care by the public programme as of 5 Mar 2025, and 25.27 million diabetes patients (search summary only; three outlets agree) [D1-03-F14] |
| Ayushman Arogya Mandirs (12 free services) | Over 1.86 lakh functional (Aug 2026) [D1-03-F19] |
| NCD clinics | 770 district clinics and 6,410 at community health centres (2026) [D1-03-F20] |
| eSanjeevani teleconsultation | Over 49 crore consultations by Aug 2026 [D1-03-F19] |
| Jan Aushadhi Kendras (generic medicine shops) | 18,646 (Feb 2026), priced 50-80% below branded medicines [D1-03-F20] |

#### The return visit that half never make

IHCI runs a fixed drug protocol. Its cohort registered 21,895 patients at 24 sites in Punjab, Madhya Pradesh, Maharashtra and Telangana (Jan 2018-Jun 2019) and followed them up in Jul-Sep 2019, with no comparison group. Only 11,274 (51%) came back. Among those who did, control rose from 26.3% to 59.8% [D1-03-F10]. A second cohort, 281,209 patients started in Punjab and Maharashtra in 2018-2021, found 36% with no visit in Jan-Mar 2022; the two cohorts differ in sites, years and the definition of loss [D3-05-F04]. Another count found about 27% of registered IHCI patients did not return in Jan-Mar 2021 (search summary only) [D1-03-F13].

The visit matters because the dose waits for it. A doctor dispenses the first medicine. Trained paramedical staff dispense the monthly refill only when pressure is controlled; uncontrolled patients are sent to a doctor for a dose change [D3-05-F08]. A patient who does not go back stays on the same dose. Some also stop taking it: pooled Indian non-adherence (adherence means taking the medicine as prescribed) to blood-pressure drugs is 48%, with a prediction interval of 9-90% (search summary only) [D1-03-F44].

#### Few specialists, two minutes

In March 2023, 79.9% of the required posts in four specialities (surgeon, physician, paediatrician, obstetrician-gynaecologist) at rural community health centres were unfilled [D1-03-F16], and the shortfall has stayed near 17,500 posts since 2014-15 [D1-03-F17]. The only specialist counts are from a 2017 parliamentary committee (search summary only): about 4,000 cardiologists, 1,200 nephrologists and 650 endocrinologists, against the committee's estimated needs of 88,000, 40,000 and 28,000 [D1-03-F18]. The government told Parliament it does not hold speciality-wise doctor data (news report of the reply, 13 Apr 2025) [D3-07-F22]. Where patients do see a doctor, the visit is short: Indian primary-care visits lasted about 2.3 minutes (2013, stopwatch, 412 visits) and 2 minutes (2015), against 10.2 minutes in Japan (2012) [D1-03-F24].

#### Cost

Families pay a large share of the bill. Out-of-pocket spending was 39.4% of total health expenditure in 2021-22 and 43.41% in 2022-23 (National Health Accounts released 27 May 2026, via a news report); in 2022-23 household spending rose by ₹26,375 crore while government spending fell by nearly ₹49,000 crore [D1-03-F23]. No figure was found for the household cost of a chronic-care visit, travel or lost wages, loss to follow-up outside IHCI, or how long a dose change is delayed.

#### Phones and who is left out

Most Indians have a mobile connection, but the patient is not always the one who holds it.

| Measure | Figure | Year |
|---|---|---|
| Smartphone owners | Over 622 million (industry estimate) [D1-03-F41] | 2025 |
| Women 15-49 owning a phone | 63.6%; rural 57.4% (search summary only) [D1-03-F42] | 2023-24 |
| Women 15-49 owning the phone they use (another note) | 54%; rural 46.6% [D3-04-F23] | Not stated |
| Phone ownership, ages 15+ | Men 83.9%, women 56.2% (search summary only) [D1-03-F42] | 2025 |
| Rural older adults near Mysore (150 people) | 50% owned a phone, few a smartphone; digital literacy 11% [D3-04-F56] | Not stated |
| People who spoke English | About 10.6% [D3-04-F57] | 2011 |

About four in ten rural women do not own a phone (OUR ARITHMETIC: 100 - 57.4 = 42.6%). OUR VIEW: anything that reaches patients between visits must work on a shared phone, through a health worker, and by voice.

OUR VIEW: a two-minute visit has no time to read two weeks of home readings, and the visit itself is the step that about half the patients skip.

### 1.4 What patients and doctors say in public

The numbers show where care breaks. The voices show why. The team has done no interviews, so this section reports published interview studies and surveys (PUBLISHED STUDY), public app reviews (PUBLIC REVIEW) and posts (FORUM POST). None of it is customer evidence gathered by the team; reviews are self-selected, and the studies were read as abstracts only.

#### Why patients miss follow-up and stop medicines

Eight Indian interview studies (PUBLISHED STUDY) name the same causes: feeling well, cost, family duties, fear of long-term drugs and traditional medicine [D3-04-F01, D3-04-F02, D3-04-F03, D3-04-F04, D3-04-F05, D3-04-F12, D3-04-F13, D3-04-F14]. In coastal Karnataka, 32 patients lost to follow-up described "symptom-driven healthcare seeking", work duties, wage loss and rushed consultations, and suggested reminders and digital records [D3-04-F01]. In rural Tamil Nadu, stopping was structural, unintentional (work, travel, caregiving) or intentional, and family could both help and hinder [D3-04-F02]. In Ludhiana, "about 50% patients were adherent" among 40 people with diabetes [D3-04-F14]. In Chennai, caregivers enable access for older adults and devices are shared [D3-04-F05]. A FORUM POST by an adult child says the father's pressure stayed controlled on Ayurvedic treatment, then rose, and he went back to some medication [D3-04-F52].

One small survey puts numbers on it. In Bathinda (Punjab), 157 people who had missed visits for over 3 months were phoned (a small convenience sample): 24.8% had no sense of being ill, 22.2% named distance, 15.2% had no guidance or reminder and 8.2% had an acute illness [D3-05-F07].

OUR VIEW: feeling well recurs as a reason to stop, and a home reading is one thing that can contradict it.

#### Home monitors in Indian homes

Few patients use a home cuff, most taught themselves, and home readings show that many "controlled" patients are not.

- **Who has one.** Of 2,588 clinic-attending people with hypertension and caregivers in North India, 18.1% used a home monitor (urban 20.5%, rural 8.5%); 75.2% learned by themselves, and technique was excellent in 15.9% of patients and 5.9% of caregivers [D3-04-F06]. No household survey figure was found. Omron says household penetration is "below 5%" (2026 article) or "just 2%" (2024 article) (THEIR CLAIM) [D3-07-F14, D3-07-F15]; another report gives 6% (search summary only) [D2-05-F29]; a web claim of under 5% cites no source [D3-04-F22].
- **What doctors do with them.** About 88% of 832 Indian doctors recommend home monitoring but estimate that only 30.4% of patients measure, and about 30% give no instructions [D3-04-F07]. Only 15.1% knew the correct home thresholds [D3-04-F18].
- **What home readings reveal.** In the GRAND study (18 centres, 12 states; 1,920 treated patients who attend regularly were enrolled and 1,578 with valid clinic and home readings were analysed; 7 days of home readings), 77.7% of those analysed looked controlled by clinic pressure but only 55.9% by clinic plus home; 21.8% had masked uncontrolled pressure (high at home, normal in clinic) [D3-04-F09, D4-03-F40]. The 13 November edition attached these shares to the 1,920; the claims check of 14 November found they are shares of the 1,578.

#### What doctors and health workers say

Doctors describe heavy workloads, and many private doctors do not follow the state protocol. In Kolar, Karnataka: "Doctors face very high workloads, especially in the public sector" [D3-04-F16]. Of 30 private doctors in Bhopal, 19 did not follow the state protocol, citing fear of losing patients if pressure did not come down at once, or of causing drug side effects, and a preference for fixed-dose combinations (two drugs in one tablet) [D3-04-F15]. Two programme people wrote on LinkedIn (paraphrased; read 13 Nov 2026): a national NCD consultant at UNICEF India (about Apr 2026) blamed blood-pressure machines left uncalibrated for months and mid-month drug stock-outs, and a doctor and WHO consultant (about Oct 2026) said counting visits is not enough, citing an Indian trial, mWellcare (chapter 2.1), as showing that a digital system does not guarantee results. No Indian doctor, nurse or health worker was found speaking about dose steps from home readings. OUR VIEW: a doctor's approval cannot be assumed.

#### What users say about existing programmes

The latest 100 Apple App Store India reviews of each of three diabetes programmes, BeatO, Sugar.fit and Fitterfly, were read on 13 Nov 2026. One-star reviews numbered 55, 76 and 9 (count from the research note's method section); Fitterfly's 5-star profile looks prompted (the note's inference). The complaints fall into a few themes (PUBLIC REVIEW).

| Theme | What reviewers describe |
|---|---|
| Unwanted calls | Repeated recorded calls and WhatsApp messages about classes and webinars never signed up for (Sugar.fit, Jul and Oct 2026) [D3-04-F27, D3-04-F28] |
| No reachable person | No doctor slot for days; no support line that answers (Sugar.fit, Sep and Oct 2026) [D3-04-F29, D3-04-F30] |
| Coaching runs dry | "by the third month, there is hardly anything new to discuss" (Sugar.fit, 26 Sep 2026) [D3-04-F33]; no follow-up after a month [D3-04-F34] |
| Device and data | A sensor whose data never synced; five readings in five minutes that differed by over 50 (BeatO, Sep and Mar 2026) [D3-04-F36, D3-04-F37] |
| Money and medicine | ₹18,990 paid for a 4-month programme with, the reviewer says, only one month's medicine delivered; a refund still pending after about 20 days (Sugar.fit, Oct 2026; BeatO, Jul 2026) [D3-04-F40, D3-04-F42] |
| Praise for a named coach | Credit to a personal coach; one reviewer reports HbA1c (a blood test of average sugar over about three months) down to 6.1 and medicine halved (Fitterfly, 2025 and 2024) [D3-04-F43, D3-04-F44] |

None of the 300 reviews mentions language or voice, and none describes a dose change from a home reading (count from the research note's method section).

#### Reminders and messages

Reminders alone did not bring people back. In a Punjab trial at two public hospitals, 388 patients with uncontrolled pressure got two myth-busting WhatsApp reminders before their visit, or none; attendance was 21.8% against 19.6%, a null result, and beliefs did not change [D3-04-F50]. A Delhi study of 110 patients (counselling, voice calls, SMS) reported control rising from 14.7% to 52.9%, but with no control group [D3-04-F51].

OUR VIEW: patients stop when they feel well, few use a cuff well, doctors are stretched and wary of the protocol, and a message works only if it reaches the person who holds the phone and leads to a decision.

### 1.5 The market issues: why the market has not fixed this

The gap is clear; this section explains why companies have not filled it. Three answers recur in the notes: what has been sold stops before the dose, the companies that sold apps on their own ran out of money, and nobody yet pays for the step that is missing.

#### What has been sold so far

India's private chronic-care programmes sell a glucose sensor or meter plus a doctor and a coach. None of their pages says glucose data changes a drug dose by algorithm, so on what is published they sit at adaptive depth 3 [D1-04-F02, D1-04-F04, D1-04-F06, D1-04-F07]. Their outcome figures are their own averages with no comparison group (THEIR CLAIM) [D1-04-F06, D1-04-F07]. The patient pays: Sugar.fit charges ₹29,990 for 12 months or ₹15,990 for 4 months (13 Nov 2026) [D1-04-F04], and HealthifyRx charged ₹48,000 for 3 months (May 2025) [D1-04-F26].

The government's tools stop at the same place. IHCI's Simple app keeps a registry, flags overdue patients and sends reminders [D1-04-F19]. The app's protocol model stores a drug list and follow-up days, and no step logic was found in it [D1-06-F40]. So the nurse records the reading, but the step-up decision still waits for a visit.

#### Why companies died

Abroad, several companies sold digital therapeutics (software that changes one patient's treatment) or sensors, some with good trials, and failed. India's best-funded chronic-care app did too.

| Company | What it sold | What happened |
|---|---|---|
| Pear Therapeutics (US) | Prescription apps for addiction and insomnia, with randomised trials [D1-02-F17] | Bankrupt April 2023; assets sold for just over $6M against $130M of liabilities [D1-05-F20, D1-02-F42]. A panel said it tried to change care and payment at once [D1-05-F21] |
| Akili (US) | A game for ADHD in children | $523,000 of prescription revenue in 2023, net loss $59.5M; sale agreed for about $34M in May 2024 [D1-02-F44] |
| Better Therapeutics (US) | A diabetes app: HbA1c 0.39 points lower than a control app (669 patients, 90 days) [D1-02-F21] | Expected no revenue in 2023 (revenue not reported), deficit $134.3M; weighed winding down in March 2024 [D1-02-F46] |
| Teva Digihaler | Sensor inhalers and app | US distribution and app support stopped 1 June 2024; the US notice gave no reason and a UK recall cited "commercial reasons" [D1-02-F41] |
| PhableCare (India) | Blood-pressure and glucose devices, consultations (depth 2) | Raised ₹187 crore in Apr 2022; stopped work in Feb 2023; staff fell from about 2,000 to 200, many unpaid. Former staff said there were no funds; the founders blamed staff misconduct [D1-04-F14, D1-04-F23] |

The common causes, as the notes give them:

- No one paid for the app alone [D1-05-F20, D1-02-F44, D1-05-F23].
- Too few prescribers, and trials that payers did not accept as outcome proof [D1-05-F21].
- Sensors with no therapy change [D1-02-F41, D1-02-F02].
- Valuations ahead of revenue, then no cash [D1-05-F55, D1-04-F23].
- Users leave fast: across 93 mental-health apps, the median app kept 3.3% of its users at day 30 [D1-02-F26].

#### Who pays today

In India, the patient pays for private programmes, as above, and the state pays for public care, where treatment "could be as low as Rs 200 per patient per year", a modelled drug cost that leaves out staff (WHO, 2022; SOURCE ESTIMATE) [D2-01-F12, D2-05-F18, D3-05-F09]. The notes found no Indian payer, public or private, that pays for remote blood-pressure monitoring or a digital therapeutic as a line item [D2-04-F47]. Insurance barely touches outpatient care: outpatient cover is below 0.1% of a US$37.7 billion outpatient market (industry-sponsored, search summary only) [D2-05-F10].

Abroad, the firms that reached scale are paid by someone other than the patient. Employers and insurers pay for clinician-led programmes: Hinge Health, paid "primarily" by employers, had revenue of $234.97M in the third quarter of 2026 [D1-05-F15, D1-05-F16]. Or the company sells a device that delivers the therapy: Insulet, a closed-loop insulin pump maker, had revenue of $842.0M in the same quarter [D1-05-F41].

#### No dose change found

No Indian service was found that turns home blood-pressure or glucose readings into a medicine change between visits [D1-04-F09, D1-04-F19]. This was one agent's limited search on 13 Nov 2026, a search result and not proof of absence; chapter 2.4 lists the searches and the nearest products abroad.

OUR VIEW: India's best-funded chronic-care app ran out of money within a year of its largest round. Money raised is not proof that anyone will pay. The doctor controls the prescription and the payer controls the money; a product that leaves either out has no user or no buyer.

### 1.6 The problem in one paragraph

OUR VIEW. Hundreds of millions of Indians have high blood pressure or diabetes, many are on medicine, and few are controlled. India already screens and enrols them at crore scale, and its programme has a protocol and free drugs. What it lacks between visits is the decision, the confirmation and the action. The scarce thing is the prescriber's decision, which waits for a visit that about half the patients do not make, and the visits that do happen were found to last about two minutes. The products sold so far show readings, send reminders or coach, and stop before the dose; companies that sold an app on its own, even with good trials, failed for lack of a payer.

Full detail: Appendix A (the challenge, the burden and the voices), with Appendix D for the companies and Appendix E for who pays.

The problem is now clear: a large, treatable population, a system that loses half of it between visits, and a market that watches and reminds but does not change the treatment. The next chapter asks what the research says actually works, and whether anyone has made it work without specialists.
