# D7-02 a16z: companies solving the adaptive-care problems (agent: Opus 5.5, 2026-11-16)

Scope: companies backed by Andreessen Horowitz (any fund; nearly all here are a16z Bio + Health) that address the four threads: A (adaptive chronic care between visits), B (high-stakes dosing where specialists are rare), C (low-cost vitals and remote monitoring), D (smart ICU and hospital deterioration). Deals announced since Jan 2025 come first; older portfolio companies are kept only if still active and relevant. Every fact has an ID (D7-02-Fnn), a URL, and a tag: OPENED (I read the page) or SNIPPET (search summary only). Earlier IDs (D2-06, D3-03, D6-02, D1-xx) are reused and were not re-opened. Company numbers are THEIR CLAIM unless stated. a16z backing was confirmed from an a16z post, a company release, or two or more press reports; where only one aggregator said so, I say "not confirmed". About 45 searches and fetches were used. 14 companies are entered, plus a list of companies that turned out NOT to be a16z-backed. The a16z.com/portfolio page could not be filtered by Bio + Health via fetch (it showed only a partial list), so the portfolio was built from announcements and press.

## Digest

1. **No a16z company does remote dose management for warfarin/INR, hydroxyurea, epilepsy drugs, transplant drugs, oral chemo dosing or insulin titration.** The closest is Thyme Care (oncology symptom reports reviewed by nurses), which manages side effects rather than doses. D7-02-F21, Gaps.
2. **No a16z company sells a cheap vitals station, contactless bed sensor or tele-ICU.** In the hospital, a16z money goes to software: sepsis alerts (Bayesian), AI clinicians (Telepatia), and nurse documentation (Abridge, Ambience, Hippocratic). D7-02-F29, F31, F36, F39, F18.
3. **Bayesian Health** (a16z led, 2021) got FDA 510(k) clearance for the first continuous AI sepsis monitor (announced 12 May 2026). It watches every inpatient without waiting for a clinician to suspect sepsis, and clinicians decide what to do. Study claims: 82% sensitivity, 5.7 h earlier, 18% lower mortality when alerts were acted on in time. D7-02-F27, F29; D6-02-F16.
4. **Telepatia** ($33M Series A led by a16z, 17 Jun 2026) is the best emerging-market analogue. It sells AI documentation, decision support and "AI doctors, nurses, auditors" to Latin American hospital systems, trained on local protocols, and plans India later. Claims: 25+ hospital systems, 14M patients, protocol adherence 84% to 99%. D7-02-F31, F32.
5. **Counsel Health** (a16z led the seed, co-led the $25M Series A, Oct 2025) is an AI-first medical group: AI does first contact and check-ins, and physicians prescribe and order labs. **Oura agreed to buy it on 10 Nov 2026**, so ring data now flows to its doctors with permission (reported price $625M). D7-02-F01, F02, F04.
6. **Hippocratic AI** (a16z co-led the $50M seed in 2023 and joined the B and C rounds) now sells 30+ "orchestrators" that bundle voice agents for outcomes such as readmissions and chronic care. Claims: 250M interactions, 99.89% correct advice in 775,000 reviewed calls. It says its agents do not diagnose or prescribe. D7-02-F14, F16, F17.
7. **Hippocratic's Nurse Co-Pilot** (April 2026): a ward nurse starts an AI phone call from the EHR (admission, education, caregiver, medications). The note goes back to the EHR and red flags go to the nurse. Claim: 3+ hours saved per nurse per day. D7-02-F18.
8. **Abridge** ($300M Series E led by a16z, Jun 2025) moved into nursing: speech at the bedside drafts Epic flowsheet values for the nurse to confirm. Rural Reid Health reports 30-45 min less charting per shift and RN vacancy down from 18% to 8% since rollout (association, THEIR CLAIM). D7-02-F34, F36, F37.
9. **Omada** (a16z led the 2014 Series B; IPO Jun 2025) passed 1,025,000 members in Q1 2026 and is adding GLP-1 prescribing through Optum Rx. The call did not say that clinicians change doses from device data; AI summarises data for the care team. D7-02-F05, F07.
10. **Thyme Care** (a16z led the 2021 round and joined the Series E of $125M+ on 2 Sep 2026) says patients who completed its symptom-reporting program had 28% fewer ED visits or admissions (company-linked figure). D7-02-F19, F20, F21.
11. **Sprinter Health** (a16z joined the $55M Series B, May 2025) is the only a16z "care loop at home" company: cross-trained field workers (assistant, community health worker, phlebotomist) plus virtual NPs, with AI routing of up to 12 home visits a day. It is a close analogue to an ASHA-plus-teleconsult model. D7-02-F25.
12. **The a16z thesis is labour, not devices.** Big Ideas 2025: "specialist AI models serving as 'super staffing' platforms" paid from labour budgets; Feb 2026: healthcare can "leapfrog directly to AI-native models of care delivery". D7-02-F40, F41.

## Companies

### A. Adaptive chronic care between visits

### Counsel Health (US): AI-first medical group, now being bought by Oura
- **What it is:** virtual primary care where an AI handles first contact and follow-up, and staff physicians handle licensed tasks.
- **Solution, concretely:** the patient chats with the AI and shares symptoms, medicine questions and recent labs. The AI keeps one running record of chats, labs and medicine changes. It prompts check-ins when trends appear, sends refill reminders, and decides when to bring in a physician. Physicians diagnose, prescribe (no controlled drugs), order labs and refer; "the physician remains accountable for clinical decisions". Consumers can add a doctor to a chat for $29; it is also sold to employers, health plans and health systems. D7-02-F02 | https://www.counselhealth.com/blog/chronic-condition-management-with-medical-ai | 2026-04-09 | OPENED. The page does not mention home BP devices or titration rules.
- **Chronic expansion:** a 7 Apr 2026 release says hypertension, high cholesterol and obesity will be added during 2026. D7-02-F03 | https://www.businesswire.com/news/home/20260407161180/en/Counsel-Health-Expands-Clinical-Care-Launching-Chronic-Condition-Services | SNIPPET.
- **Oura deal:** definitive agreement 10 Nov 2026, expected to close near the end of 2026. Counsel physicians can see Oura ring data and past chats with the member's permission. More than half of Counsel users in Oura Labs shared their Oura data (THEIR CLAIM). In Oura's example, a physician told a member to delay a GLP-1 injection by one day after food poisoning. Price is not on Oura's page; $625M is reported elsewhere. D7-02-F04 | https://ouraring.com/blog/oura-to-acquire-counsel-health/ | 2026-11-10 | OPENED; price: https://www.mobihealthnews.com/news/oura-acquire-counsel-health-625m | SNIPPET.
- **a16z round:** a16z led the $11M seed and co-led the Series A with GV (a16z post, 16 Oct 2025); the Series A was $25M. D7-02-F01 | https://a16z.com/announcement/investing-in-counsel-health/ (confirmed in D2-06-F11 and D3-03, OPENED there); amount: https://hitconsultant.net/2025/10/16/counsel-health-raises-25m-to-launch-physician-supervised-ai-care-platform | SNIPPET.
- **Traction:** says it resolves "most member concerns without escalation"; no figures (THEIR CLAIM, F02).
- **Maps to:** A (depth 3: physician changes treatment after AI triage; no protocol-driven titration described).
- **India:** none found.
- **Borrow / do differently:** borrow "AI does the first touch, the doctor signs off" and log every accept, edit or reject. In a district setting the doctor is scarce, so the escalation target should be a protocol-trained nurse or medical officer, with a specialist only for rule breaks. A wearable feed (the Oura route) is a luxury; a shared BP cuff plus a phone call is the Indian equivalent.

### Omada Health (US, public since Jun 2025): virtual cardiometabolic care with connected devices
- **What it is:** coaching and clinical support for prediabetes, diabetes, hypertension, weight/GLP-1, cholesterol and MSK, using connected devices.
- **Solution, concretely:** connected glucose meters, BP cuffs and scales send readings to coaches and care teams. The AI layer (OmadaSpark: meal tracking, a nutrition tool tuned on 3M+ foods) also "summarizes member data and surfaces potential next actions for care team review". Omada began a GLP-1 prescribing offering in the Optum Rx PBM channel and is a program administrator in Lilly's Employer Connect; management expects prescribing revenue to build in 2027. The call does not say clinicians change doses from device data. Paid by employers, health plans and PBMs. D7-02-F07 | https://www.fool.com/earnings/call-transcripts/2026/05/08/omada-health-omda-q1-2026-earnings-transcript/ | 2026-05-08 | OPENED.
- **Other 2026 launches:** Omada for Cholesterol (Feb 2026); GLP-1 FlexCare cash-pay option for employers. D7-02-F08 | https://www.barchart.com/story/news/305114/omada-adds-cholesterol-care-to-its-integrated-platform-addressing-the-silent-driver-of-cardiovascular-risk ; https://www.fiercehealthcare.com/digital-health/omada-health-swings-profit-q4-offers-new-glp-1-cash-pay-option-employers | SNIPPET (both pages returned empty or 403).
- **a16z round:** a16z led the $23M Series B in April 2014, and a16z's Balaji Srinivasan joined the board. D7-02-F05 | https://businesswire.com/news/home/20140409005871/en/Omada-Health-Closes-23-Million-Series-Financing | SNIPPET. IPO on 6 Jun 2025 at $19 (Nasdaq: OMDA); one secondary source puts a16z at about 9.6% before the IPO (not verified against the S-1). D7-02-F06 | https://www.fiercehealthcare.com/digital-health/omada-health-files-go-public-digital-health-industry-waits-ipo-revival ; https://awesomecapital.blogspot.com/2025/05/andreessen-horowitz-backed-omada-health.html | SNIPPET. No new a16z round since 2025 (public company).
- **Traction (THEIR CLAIM, Q1 2026):** 1,025,000 members (+51% year on year), Q1 revenue $78M (+42%). GLP-1 Care Track: 1.8 times the weight loss of controls at 12 weeks; 0.8% average weight change a year after stopping GLP-1, versus 11-12% regain in trials. No BP or A1C figures on the call. F07.
- **Maps to:** A (depth 2 to 3; prescribing is new).
- **India:** none found. Indian app-plus-coach equivalents (depth 3) are in D2-06 (Sugar.fit, BeatO, Fitterfly; D1-04-F04, F06, F07).
- **Borrow / do differently:** borrow "AI drafts next actions, the care team approves" as the safe first step toward titration. Omada's payer is the US employer; an Indian rural programme has none, so cost per patient must fit a state NCD budget or a ₹-per-month patient fee.

### Knownwell (US): obesity medicine and primary care, virtual plus clinics
- **What it is:** metabolic primary care with obesity medicine, nutrition and behavioural health, in person (Atlanta, Boston, Chicago, Dallas) and virtually nationwide.
- **Solution, concretely:** clinicians prescribe GLP-1s "if considered appropriate", alongside nutrition and behavioural care. New money goes to AI and clinical decision support. Accepts commercial insurance, Medicare and Medicaid. D7-02-F09 | https://medcitynews.com/2025/10/knownwell-obesity-medicine/ | 2025-10-21 | OPENED. The page does not describe device feeds or dose rules.
- **a16z round:** $25M on 20 Oct 2025 led by CVS Health Ventures, with a16z Bio + Health, MassMutual Catalyst, Intermountain Ventures and Flare taking part; more than $50M raised in total (F09, OPENED). a16z led the $20M Series A in Dec 2023. D7-02-F10 | https://pulse2.com/knownwell-20-million-funding/ | SNIPPET.
- **Traction:** none given.
- **Maps to:** A (obesity/GLP-1; depth 3).
- **India:** none. Generic semaglutide launched in India 21-22 Mar 2026 (D1-04-F10, reused from D2-06).
- **Borrow / do differently:** "weight-inclusive" clinics with hybrid visits suit urban India. In rural settings the GLP-1 dose ladder (step up every 4 weeks if tolerated) is a natural protocol for a nurse-run loop, but drug cost, not clinician time, will limit it.

### Function Health (US): twice-yearly lab panels plus an AI "medical intelligence" layer
- **What it is:** a consumer membership with 100+ lab tests twice a year, plus MRI/CT (through Ezra), read by an AI model.
- **Solution, concretely:** labs, imaging, wearables and records feed a "Medical Intelligence Lab" model that is meant to "reveal early patterns" and "translate complexity into simple, meaningful action". Clinicians order and review (per D2-06). It reports results but does not run treatment changes. Paid in cash by members ($365 a year after a price cut, D2-06-F43). D7-02-F11 | https://a16z.com/announcement/function-health-series-b/ | 2025-11-19 | OPENED.
- **a16z round:** a16z invested in the $298M Series B at $2.5B (Nov 2025); Redpoint led (D2-06-F42; correction in C2-corrections-log). The a16z post says "investing in", not "leading". F11. a16z led the earlier $53M Series A (D2-06-F42, SNIPPET).
- **Traction (THEIR CLAIM):** lab panel has reached "hundreds of thousands of people". F11.
- **Maps to:** A, input side only (labs as biomarkers); it does not titrate.
- **India:** none found; Indian lab chains sell similar panels (not researched here).
- **Borrow / do differently:** borrow the idea of one record that joins labs and devices. In India the useful version is a cheap point-of-care panel (HbA1c, creatinine, INR) that triggers a protocol step, not a $365 wellness panel.

### Hippocratic AI (US): voice AI agents for between-visit care, plus a ward-nurse co-pilot (also D)
- **What it is:** a company with a safety-focused healthcare LLM ("Polaris") that sells voice agents that phone patients, now bundled into outcome "orchestrators".
- **Solution, concretely:** a supervisor layer picks which narrow agent calls which patient, when and on which channel, using patient answers, health signals and urgency. Example agents: post-discharge sepsis monitoring, diabetic follow-ups, medication adherence counselling. It is sold as outcome bundles: AI Chronic Care and Star Ratings for payers; AI Readmission Prevention and Lost-to-Follow-Up for providers. D7-02-F16 | https://itdigest.com/healthtech/hippocratic-ai-launches-agentic-orchestrators-to-own-end-to-end-healthcare-outcomes/ | 2026-08-17 | OPENED. The product menu includes AI Pharmacy, AI InPatient, AI Rapid Response and Nurse Co-Pilot, and a case study on closing HEDIS blood-pressure gaps. No anticoagulation or INR agent is listed. D7-02-F17 | https://hippocraticai.com/specialties/cardiology/ | OPENED. Outside coverage says the agents do not diagnose or prescribe (F17 search, SNIPPET: https://www.eesel.ai/blog/hippocratic-ai).
- **Nurse Co-Pilot (D):** see the D section entry note below; facts D7-02-F18.
- **a16z rounds:** $50M seed co-led by General Catalyst and a16z, 16 May 2023. D7-02-F14 | https://www.statnews.com/2023/05/16/artificial-intelligence-health-care-llm-general-catalyst-a16z/ | SNIPPET. $141M Series B led by Kleiner Perkins, Jan 2025, with a16z among existing investors. D7-02-F15 | https://www.businesswire.com/news/home/20250109643850/en/Hippocratic-AI-Completes-141MM-Series-B-Financing-Round-Led-by-Kleiner-Perkins-Valuing-the-Company-at-1.64B | SNIPPET (403 on fetch). $126M Series C led by Avenir, 3 Nov 2025, $3.5B, a16z participating (D2-06-F20, confirmed in D3-03).
- **Traction (THEIR CLAIM, Aug 2026):** 250M+ patient interactions; 300 live use cases; 7,700 US-licensed clinicians reviewed 775,000 calls, with 99.89% correct advice and "zero instances of serious harm". F16.
- **Maps to:** A (between-visit follow-up, depth 2 to 3) and D (Nurse Co-Pilot).
- **India:** no Indian deployment or Hindi support found. Premji Invest (India) is an investor (D2-06-F20).
- **Borrow / do differently:** borrow the "orchestrator" pattern: one scheduler decides which scripted call goes to which patient after which reading. India needs it on cheap voice calls in local languages, to feature phones, with the escalation going to an ANM or medical officer rather than a US nurse call centre (2care.ai is the Indian WhatsApp analogue, D1-04-F36).

### Devoted Health (US): Medicare Advantage insurer with its own medical group (short entry)
- **What it is:** a health plan plus in-house clinicians (Devoted Medical) serving older adults.
- **Solution, concretely:** job postings describe a hypertension clinic whose staff send out BP monitors and check measurement technique, and a cardiovascular team combining "remote monitoring, medication management" and education. Paid by Medicare (capitation). D7-02-F13 | https://jobs.generalcatalyst.com/companies/devoted-health/jobs/87410884-cardiovascular-clinical-guide | SNIPPET (job ads, not product pages).
- **a16z round:** $366M Series F in two tranches ($48M Nov 2025, $317M Jan 2026) led by The Space Between with Centricus; a16z named among existing investors who took part. D7-02-F12 | https://www.devoted.com/resources/2026-growth | 2026-01-30 | OPENED.
- **Traction (THEIR CLAIM):** 466,000+ members in 29 states; 96% of Star-rated members in plans rated 4+ stars for controlling blood pressure. F12.
- **Maps to:** A (insurer-run BP and medicine management).
- **India:** none; India has no comparable capitated payer for older adults.
- **Borrow / do differently:** the lesson is that the payer funds the BP loop because it is paid on control rates. In India the nearest lever is a state NCD programme or PM-JAY paying per controlled patient, which does not exist yet.

### B. High-stakes drug dosing where specialists are rare

### Thyme Care (US): oncology care navigation and symptom management for payers
- **What it is:** value-based cancer care support that coordinates patients, oncologists and health plans; it is now the anchor of a new "Thyme Companies" group.
- **Solution, concretely:** patients report treatment symptoms electronically (an ePRO programme); Thyme's clinical team reviews the reports in real time and steps in to avoid ED visits and admissions. A separate readmission-prevention programme targets complex patients. Paid by health plans and risk-bearing providers (total cost of care contracts). D7-02-F21 | https://hcttf.org/wp-content/uploads/2026/02/Advancing-Value-Based-Oncology-Through-247-Integrated-Virtual-Cancer-Care-1.pdf (PDF title: "24/7, Integrated Virtual Cancer Care"; text not extractable) | SNIPPET. No dose-management product was found; it manages side effects, not chemo doses.
- **a16z rounds:** a16z led the $22M round in Oct 2021 (with AlleyCorp and Frist Cressey). D7-02-F19 | https://www.businesswire.com/news/home/20211005005475/en/Andreessen-Horowitz-Leads-22M-in-Funding-for-Thyme-Care-to-Improve-Patient-Outcomes-Close-Gaps-in-Health-Disparities-and-Drive-Value-Based-Cancer-Care | SNIPPET. Series E of more than $125M, 2 Sep 2026, led by Morgan Health, valuation above $2B; a16z Bio + Health took part, as did Humana and CVS Health Ventures. D7-02-F20 | https://pulse2.com/thyme-care-raises-over-125-million-series-e-at-more-than-2-billion-valuation-and-launches-thyme-companies/ | OPENED.
- **Traction (THEIR CLAIM):** available to 10.5M+ people in all 50 states; manages $7B+ in oncology spend; "validated reductions of 5% to 10% in total cost of care"; profitable (F20). ePRO completers: 28% relative reduction in ED visits or admissions; readmissions 30% lower among complex patients (F21, SNIPPET).
- **Maps to:** B (oral chemo and cancer treatment safety), partly; it covers side effects and escalation, not dosing.
- **India:** none found.
- **Borrow / do differently:** borrow the weekly symptom check-in with fixed red-flag rules (fever on chemo, bleeding, vomiting) routed to a nurse the same day. For warfarin the same skeleton applies, but India must add a dose step from a home or clinic INR, which Thyme does not do.

### OpenEvidence (US): AI clinical evidence search for doctors (decision support, B and D)
- **What it is:** an AI search tool that helps physicians find and interpret medical evidence at the point of care.
- **Solution, concretely:** the clinician types a question and gets an evidence-cited answer. It is free to US clinicians and ad-funded (not checked here). A partnership with Anthropic is to bring clinical decision support to physicians in nearly 100 low- and middle-income countries; MSK's OncoKB is to be added. It also plans its own cancer drug pipeline. No dosing engine is described. D7-02-F23 | https://refreshmiami.com/news/openevidence-hits-15b-valuation-as-its-ambitions-move-far-beyond-medical-search/ | 2026-09-25 | OPENED.
- **a16z round:** $250M at a $15B valuation, Sep 2026; Business Insider (as reported) says hospital systems and a16z led (F23). Other outlets name a16z and Byers Capital as co-leads. D7-02-F24 | https://af.net/realtime/clinical-ai-startup-openevidence-secures-250m-led-by-andreessen-horowitz-at-15b-valuation/ | SNIPPET. Round name (Series D or E) differs between sources.
- **Traction:** usage figures not on the opened page.
- **Maps to:** B and D, as a reference tool for doctors without specialists. It is not a dosing tool.
- **India:** the LMIC partnership may cover India; India is not named (F23).
- **Borrow / do differently:** a medical officer in a district hospital can use such a tool to check a rare decision, but a warfarin or hydroxyurea dose needs a fixed, audited protocol, not a free-text answer. Use search as the backup, and the protocol as the decision.

### Milu Health (US): medication reviews by pharmacists plus a savings platform (short, B-adjacent)
- **What it is:** an employer-paid platform that reads health records to steer people to cheaper, better care; its pharmacists do medication reviews.
- **Solution, concretely:** pharmacists and nurses do comprehensive and targeted medication reviews (CMR/TMR) and reconciliation using clinical and claims data (job ads, one dated 4 Jun 2026). D7-02-F22 | https://jobs.a16z.com/jobs/milu-health/4fdccb23-5c72-48d8-ba69-b388c2e1245f--medication-review-pharmacist-chicago | SNIPPET.
- **a16z round:** $4.8M seed led by a16z Bio + Health, March 2024 (before the 2025 window). F22 | https://www.businesswire.com/news/home/20240311529401/en/milu-health-announces-4.8m-seed-round-led-by-a16z-bio-health-and-partners-with-employers-to-expand-employee-access-to-ai-driven-health-savings-platform | SNIPPET.
- **Maps to:** B, only adjacent (medicine review, not dose management).
- **India:** none.
- **Borrow / do differently:** the pharmacist review is the human layer India mostly lacks in primary care. A trained nurse or pharmacist reviewing a monthly drug list (for interactions with warfarin, for example) is a cheap safety add-on.

### C. Low-cost vitals and remote monitoring, with the care loop around it

### Sprinter Health (US): home visits by cross-trained field workers plus virtual clinicians
- **What it is:** a mobile medical practice that sends "Sprinters" into homes on behalf of health plans to close care gaps.
- **Solution, concretely:** Sprinters are cross-trained as medical assistants, community health workers and phlebotomists. They follow a test checklist for each patient (examples: lead screening, diabetic eye exam, annual assessment) and join a virtual nurse practitioner or specialist in a hybrid visit. The "Sprinter Platform" uses AI to plan schedules from traffic, weather, parking and patient needs; one Sprinter sees up to 12 people a day. Paid by health plans (quality-measure gap closure). D7-02-F25 | https://sprinterhealth.com/news/sprinter-health-raises-55-million-to-expand-access-to-preventive-care-and-close-critical-care-gaps-for-people-nationwide | 2025-05-15 | OPENED.
- **a16z rounds:** $55M Series B, 15 May 2025, led by General Catalyst; a16z Bio + Health took part, with GV, Accel and the UC Regents (F25, OPENED). Earlier: GV and a16z invested in Oct 2021 (D7-02-F26 | https://www.sprinterhealth.com/news/gv-andreessen-horowitz-invest-in-sprinter-health-to-scale-up-at-home-lab-testing-services | OPENED; amount and lead not on the page). One aggregator says a16z led a $33M Series A (https://seedtable.com/companies/sprinter-health/funding-rounds/series-b-2025-05 | SNIPPET).
- **Traction (THEIR CLAIM):** nearly 100,000 home visits; NPS above 90; 80% gap-closure rate across up to 20 quality measures; 18 states in May 2025 (a later headline says 25). F25.
- **Maps to:** C (the human care loop around home measurements). It is not a sensor company.
- **India:** none, but the model matches ASHA and ANM home visits plus teleconsultation.
- **Borrow / do differently:** borrow the cross-trained worker, the per-patient checklist and AI route planning. In India, add a shared multi-parameter kit (BP, SpO2, glucose, weight, INR strip) carried by the worker, and pay per controlled patient rather than per gap closed.

(No other a16z company in thread C was found. Older a16z seeds, Levels (CGM app, 2020) and Cardiogram (Apple Watch AF detection, 2016), are not "low-cost multi-sensor" and their current status was not checked. D7-02-F48.)

### D. Smart ICU and hospital deterioration for understaffed hospitals

### Hippocratic AI, Nurse Co-Pilot (the company entry is under A)
- **Solution, concretely:** a ward nurse picks a patient and a use case in the EHR and clicks deploy. The agent phones the patient (no app; 10-15 minute calls) for admission education, disease and discharge education, caregiver readiness, or a walk-through of each medicine. A structured note and full transcript go back to the EHR (Epic, MEDITECH, Oracle Cerner). "Smart Escalation" flags red flags, comprehension gaps and care needs for the nurse. Pilot partners: Cleveland Clinic, Cincinnati Children's, OhioHealth. Claims from time-motion studies on medical-surgical units: about 15/60/40/60 minutes saved per use case per shift; headline "3+ hours saved per nurse, per day" (THEIR CLAIM; the page does not reconcile the per-shift and per-day figures). It does not monitor vitals. D7-02-F18 | https://hippocraticai.com/nurse-co-pilot/ | OPENED; launch 16 Apr 2026: https://www.businesswire.com/news/home/20260416138680/en/ | SNIPPET.
- **Borrow / do differently:** discharge and medicine education on the phone is the cheapest nurse-hour saver for an Indian district ward. It must run in the local language and reach a family member's phone.

### Bayesian Health (US): continuous AI sepsis and deterioration alerts inside the EHR
- **What it is:** a Johns Hopkins spinout (founder Suchi Saria) whose TREWS platform watches every inpatient's record and flags sepsis early.
- **Solution, concretely:** the platform reasons over the full patient record and runs continuously on all hospitalised patients. It flags sepsis "before clinical suspicion" (other cleared tools need a clinician to suspect sepsis first). Alerts appear inside the existing EHR workflow and clinicians decide the response. Sold to hospitals. D7-02-F29 | https://www.biospace.com/press-releases/bayesian-health-receives-first-ever-fda-clearance-for-continuous-ai-sepsis-monitoring | 2026-05-12 | OPENED.
- **Regulatory:** FDA 510(k) clearance, described as the first for a continuous AI sepsis monitor, building on a Breakthrough Device designation (F29). One outlet says the clearance date was 30 Apr 2026 (SNIPPET). A CMS New Technology Add-on Payment was "expected" in the release. A later outlet says it was approved with payments from 1 Oct 2026. D7-02-F30 | https://www.unite.ai/?p=459992 | SNIPPET, not verified against CMS.
- **a16z round:** a16z led (Julie Yoo joined the board), announced 12 Jul 2021. D7-02-F27 | https://a16z.com/2021/07/12/investing-in-bayesian-health/ | OPENED (amount not on the page). $15M round with Health 2047, Lifeforce and Catalio. D7-02-F28 | https://medcitynews.com/2021/07/johns-hopkins-spinoff-looking-to-build-better-risk-prediction-tools-emerges-with-15m/ | SNIPPET. No 2025-2026 round found.
- **Evidence (study claims cited by the company):** 764,707 encounters at 5 hospitals; 82% sensitivity; about 1 in 3 alerts physician-confirmed; 5.7 h lead time; 89% provider adoption; 18% lower in-hospital mortality when clinicians acted on alerts in time (F29). The mortality gain appeared only when an alert was confirmed within 3 hours (D6-02-F16, Nat Med 2022).
- **Deployment:** Cleveland Clinic and University of Rochester Medicine named; no total count (F29).
- **Maps to:** D (AI early warning).
- **India:** none found. Cloudphysician (India) does remote ICU with cameras and AI notes but has no published sepsis-alert trial (D6-02-F01).
- **Borrow / do differently:** borrow "screen everyone, not just suspected cases" and the 3-hour confirm-and-act rule. Indian district hospitals often lack an EHR with timed vitals and labs, so the input must be a nurse-entered NEWS-style score or a monitor-reading camera, and the alert must go to someone who can start antibiotics (a medical officer or a tele-intensivist hub).

### Telepatia (Colombia, Latin America): AI clinicians for under-staffed hospital systems
- **What it is:** an AI-native clinical platform sold to hospital systems in Brazil, Colombia and Mexico (Chile and Argentina also named).
- **Solution, concretely:** consultation audio is transcribed in real time into the record. It flags drug interactions and gives recommendations from medical literature, clinical guidelines and each hospital's own protocols. It connects to local record systems (Hosvital in Colombia, per press; the doctor makes the final call). Its "AI healthcare workers" (AI doctors, nurses, auditors) are a growing set; one founder quote says the AI nurse is still coming. D7-02-F31 | https://a16z.com/announcement/investing-in-telepatia/ | 2026-06-17 | OPENED; D7-02-F33 | https://www.valoraanalitik.com/telepatia-ia-para-reducir-errores-medicos/ ; https://thenextweb.com/news/telepatia-ai-healthcare-latin-america-33m-a16z | SNIPPET.
- **a16z round:** $33M Series A led by a16z, 17 Jun 2026 (authors Daisy Wolf, Gabriel Vasquez, Eva Steinman). Angels: Shyam Sankar (Palantir), Simón Borrero (Rappi), David Vélez (Nubank). Seed Oct 2025 ($9M per Colombian press); about $42M total (F31, F33). D7-02-F32 | https://latamlist.com/telepatia-raises-33m-series-a-led-by-andreessen-horowitz/ | 2026-06-18 | OPENED.
- **Traction (THEIR CLAIM):** launched July 2025; 25+ hospital systems; 14M patients; physicians recover 1.7 h a day; 60,000 medical errors "prevented in real time"; protocol adherence 84% to 99%; Mater Dei (Brazil) physicians use it eight hours a day. a16z's case: Latin America has 43% fewer physicians and 65% fewer nurses per capita than the OECD average, and the top 100 institutions employ half its physicians (F31).
- **Maps to:** D (hospital protocol automation, AI clinician support), and B in part (drug-interaction checks).
- **India:** plans to deepen Latin America first, then expand to India, Africa and Southeast Asia; no date (F32, F33).
- **Borrow / do differently:** this is the closest a16z proof that a shortage-driven, protocol-trained hospital AI can sell in a middle-income market. Its "protocol adherence" metric is a direct template for an Indian district-hospital pitch. India differs: public district hospitals buy through state tenders, not a few big private systems, so the entry route is a state health mission or the private chains first.

### Abridge (US): ambient documentation, now for ward nurses
- **What it is:** AI that turns clinical conversations into notes, billing codes and, since 2026, nurse flowsheet entries.
- **Solution, concretely:** recorded conversations become documentation with ICD-10/HCC codes and next steps; 28 languages; 55 specialties. D7-02-F34 | https://abridge.com/blog/series-e | 2025-06-23 | OPENED. For nurses: the nurse talks through care at the bedside; the tool drafts Epic flowsheet entries that the nurse checks, with each value linked to the spoken moment ("Linked Sources"). It became generally available to nurses across its health-system clients in early May 2026. KLAS First Look score 94.3 (six early sites). Integrations with smart-room vendors hellocare.ai and Artisight were announced in June 2026. D7-02-F36 | https://hitconsultant.net/2026/04/02/klas-report-abridge-ambient-ai-nursing-flowsheets-ehr/ ; https://www.abridge.com/platform/nursing | SNIPPET.
- **a16z round:** $300M Series E led by a16z, with Khosla, 23-24 Jun 2025 (F34, OPENED); $5.3B valuation. D7-02-F35 | https://www.beckershospitalreview.com/healthcare-information-technology/innovation/abridge-closes-300m-in-series-e-funding-hits-5-3b-valuation/ | SNIPPET. A $316M Series E extension in Apr 2026 is reported by one source only (not confirmed).
- **Traction (THEIR CLAIM):** 150+ enterprise health systems; 50M+ conversations projected for 2025 (F34). Reid Health, a rural system in Indiana and Ohio: heavy users spend 30-45 fewer minutes per shift on documentation; RN vacancy fell from about 18% to 8% since rollout; extended to nursing assistants (CNAs) and technicians. D7-02-F37 | https://medcitynews.com/2026/06/documentation-abridge-nurse-tech-hospital/ | 2026-06-26 | OPENED. The vacancy fall is an association reported by the hospital, not a measured effect.
- **Maps to:** D (nurse time in understaffed wards). It does not detect deterioration.
- **India:** none found; which of the 28 languages are Indian was not checked.
- **Borrow / do differently:** borrow "speak the vitals, the AI fills the chart, the nurse confirms" as the way to get timed vitals into a record where none exists. That record is what an early-warning score needs. In India the chart is often paper, so the output may need to be a printed or WhatsApp summary as well as a digital record.

### Ambience Healthcare (US): ambient documentation and coding, now an inpatient nursing suite
- **What it is:** an AI platform for documentation, coding and clinical documentation integrity in health systems.
- **Solution, concretely (Nursing Suite, 23 Jun 2026):** "Nursing Summary" reads the multi-day record before a shift (hospital course, events, discharge barriers, handoff). "Chart Chat for Nursing" answers plain-language questions with citations. "Ambient Flowsheet Documentation" turns a nurse's spoken assessment into flowsheet values, each tied to the source phrase, and nothing is saved until the nurse confirms. No customers or time savings named. D7-02-F39 | https://hitconsultant.net/2026/06/23/ambience-healthcare-launches-inpatient-nursing-suite/ | OPENED.
- **a16z round:** $243M Series C, 29 Jul 2025, co-led by Oak HC/FT and a16z; $1.25B valuation; 40+ US health systems (Cleveland Clinic, UCSF and others). D7-02-F38 | https://siliconangle.com/2025/07/29/ai-native-clinical-documentation-startup-ambience-healthcare-raises-243m/ ; https://fiercehealthcare.com/health-tech/ambience-banks-243m-series-c-investors-continue-bet-big-ambient-ai | SNIPPET.
- **Maps to:** D (nurse workload and handover).
- **India:** none found.
- **Borrow / do differently:** the AI shift handover summary is the transferable piece. In a 1-nurse-to-many-beds Indian ward, a handover sheet listing "who is getting worse" is worth more than dictation.

## a16z's own stated themes (2025-2026)

- Big Ideas 2025, Julie Yoo, "Super Staffing for Healthcare": "the mother of all clinical staffing crises"; "specialist AI models serving as 'super staffing' platforms"; companies can tap "labor budgets vs. IT budgets". Vijay Pande: wearables and blood-biomarker AI to "monitor their health proactively". D7-02-F40 | https://a16z.com/big-ideas-in-tech-2025/ | OPENED (no date on the page).
- "AI in Healthcare: The Leapfrog Opportunity", 24 Feb 2026 (Julie Yoo, Oliver Wyman summit talk): healthcare's low legacy tech lets it "leapfrog directly to AI-native models of care delivery". No mention of India or emerging markets. D7-02-F41 | https://a16z.com/podcast/ai-in-healthcare-the-leapfrog-opportunity/ | OPENED.
- Already recorded: "Infinite Healthcare" (26 Feb 2026; D2-06-F49) and "The State of Longevity" (3 Nov 2026; "The opportunity is helping people act on them"; D2-06-F50). Neither discusses titration.
- Telepatia post (F31) is the only a16z post seen that argues from a middle-income clinician shortage.

## Gaps

1. **Thread B has no a16z company doing dosing.** No a16z company was found doing remote dose management for warfarin/INR, sickle-cell hydroxyurea, epilepsy drugs, transplant immunosuppressants, oral chemo dosing or insulin titration. Hippocratic AI's menu lists no anticoagulation agent (F17); Thyme Care manages symptoms, not doses (F21). Warfarin AI exists only as research: CURATE.AI (retrospective, 127 patients) and a GPT-4 study (doses within plus or minus 1 mg/week of physicians in 74% of 180 cases, modelled). D7-02-F50 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12079355/ ; https://www.hirudotherapysociety.org/en/research/retrospective-modeling-study-of-chatgpt-gpt-tezcan-2026 | SNIPPET. The user's lead pick (RHD warfarin) is open ground for a16z-style companies.
2. **Thread C has no a16z sensor or vitals-station company.** No a16z-backed cheap multi-sensor vitals station, contactless bed sensor or RPM hardware company was found since 2025. Older a16z seeds (Levels 2020, Cardiogram 2016) are consumer apps. D7-02-F48 | https://techcrunch.com/2020/11/17/levels-raises-12m-from-a16z-and-others-to-bring-its-biowearable-to-market ; https://a16z.com/2016/10/20/cardiogram | SNIPPET.
3. **Thread D has no a16z tele-ICU, camera or hub-and-spoke company.** No a16z-backed tele-ICU, camera bed or monitor-reading company, or hub-and-spoke critical care network, was found. a16z's hospital bets are EHR software (Bayesian, Abridge, Ambience, Hippocratic, Telepatia), which assumes a digital record that most Indian district hospitals lack.
4. **No a16z company in this list operates in India.** Telepatia names India as a later market (F32); OpenEvidence's LMIC partnership does not name India (F23).
5. **Checked and NOT a16z-backed** (useful because the brief listed some of them):
   - Story Health (heart-failure medicine titration through remote coaching; VITAL-HF trial): Series A $22.6M led by Northpond and B Capital; Define, General Catalyst and LRVHealth also invested. No a16z. D7-02-F42 | https://www.citybiz.co/article/223273/story-health-raises-22-6-million-in-series-a/ | SNIPPET.
   - Virta Health: Venrock, Obvious, Sequoia Global Equities and others; no a16z seen. D7-02-F43 | https://www.virtahealth.com/press/virta-health-raises-45-million-to-expand-treatment-for-type-2-diabetes-reversal | SNIPPET.
   - Biofourmis: General Atlantic led the $300M Series D (2022), with SoftBank, Sequoia and others; no a16z. One source says CopilotIQ bought it in Oct 2024 (unconfirmed). D7-02-F44 | https://globalventuring.com/corporate/biofourmis-takes-care-with-300m/ | SNIPPET.
   - Cityblock: only one aggregator lists a16z (a Series A); every other source names Thrive, Maverick, Redpoint, General Catalyst, Tiger, SoftBank. a16z backing not confirmed. D7-02-F45 | https://www.techstackipo.com/company/cityblock-health | SNIPPET.
   - Akido Labs (ScopeAI; medical assistants see patients, AI proposes, doctors approve): $60M Series B led by Oak HC/FT, May 2025; YC; no a16z. D7-02-F46 | https://siliconangle.com/2025/05/15/akido-lands-60m-grow-ai-platform-underserved-healthcare-settings | SNIPPET.
   - Doctronic (autonomous AI prescription renewals in Utah's sandbox, about 190 medicines): $40M Series B, Mar 2026, co-led by Abstract and Lightspeed; USV existing; no a16z. D7-02-F47 | https://pulse2.com/doctronic-40-million-raised-for-ai-based-prescription-renewal-and-autonomous-clinical-care-platform | SNIPPET.
   - Cadence: Spark Capital led; no a16z (D2-06-F1).
   - Not checked (no usable result): Qventus, Cleerly, Eleos.
6. **Adjacent a16z health deals not entered (administrative or cost, not care loops):** Prosper AI ($30M, Jun 2026), Truemed ($34M, Dec 2025), Lassie, Infinitus, Protege, General Medicine ($120M Series B led by a16z; date not seen; D7-02-F49 | https://aiweekly.co/alerts/pillpack-founders-general-medicine-raises-120m-series-b-led-by-a16z-with-eli | SNIPPET).
7. **Not resolved:**
   - Omada's a16z stake after the IPO (S-1 not opened).
   - Hippocratic AI's 2026 funding (unannounced amounts on one aggregator).
   - Thyme Care's ePRO study design.
   - Bayesian's NTAP status.
   - Counsel deal price on a primary source.

## Sources

OPENED:
- https://www.counselhealth.com/blog/chronic-condition-management-with-medical-ai (F02)
- https://ouraring.com/blog/oura-to-acquire-counsel-health/ (F04)
- https://www.fool.com/earnings/call-transcripts/2026/05/08/omada-health-omda-q1-2026-earnings-transcript/ (F07)
- https://medcitynews.com/2025/10/knownwell-obesity-medicine/ (F09)
- https://a16z.com/announcement/function-health-series-b/ (F11)
- https://www.devoted.com/resources/2026-growth (F12)
- https://itdigest.com/healthtech/hippocratic-ai-launches-agentic-orchestrators-to-own-end-to-end-healthcare-outcomes/ (F16)
- https://hippocraticai.com/specialties/cardiology/ (F17)
- https://hippocraticai.com/nurse-co-pilot/ (F18)
- https://pulse2.com/thyme-care-raises-over-125-million-series-e-at-more-than-2-billion-valuation-and-launches-thyme-companies/ (F20)
- https://refreshmiami.com/news/openevidence-hits-15b-valuation-as-its-ambitions-move-far-beyond-medical-search/ (F23)
- https://sprinterhealth.com/news/sprinter-health-raises-55-million-to-expand-access-to-preventive-care-and-close-critical-care-gaps-for-people-nationwide (F25)
- https://www.sprinterhealth.com/news/gv-andreessen-horowitz-invest-in-sprinter-health-to-scale-up-at-home-lab-testing-services (F26)
- https://a16z.com/2021/07/12/investing-in-bayesian-health/ (F27)
- https://www.biospace.com/press-releases/bayesian-health-receives-first-ever-fda-clearance-for-continuous-ai-sepsis-monitoring (F29)
- https://a16z.com/announcement/investing-in-telepatia/ (F31)
- https://latamlist.com/telepatia-raises-33m-series-a-led-by-andreessen-horowitz/ (F32)
- https://abridge.com/blog/series-e (F34)
- https://medcitynews.com/2026/06/documentation-abridge-nurse-tech-hospital/ (F37)
- https://hitconsultant.net/2026/06/23/ambience-healthcare-launches-inpatient-nursing-suite/ (F39)
- https://a16z.com/big-ideas-in-tech-2025/ (F40)
- https://a16z.com/podcast/ai-in-healthcare-the-leapfrog-opportunity/ (F41)

SNIPPET (search summary only):
- F01 amount: https://hitconsultant.net/2025/10/16/counsel-health-raises-25m-to-launch-physician-supervised-ai-care-platform
- F03: https://www.businesswire.com/news/home/20260407161180/en/Counsel-Health-Expands-Clinical-Care-Launching-Chronic-Condition-Services
- F04 price: https://www.mobihealthnews.com/news/oura-acquire-counsel-health-625m
- F05: https://businesswire.com/news/home/20140409005871/en/Omada-Health-Closes-23-Million-Series-Financing
- F06: https://awesomecapital.blogspot.com/2025/05/andreessen-horowitz-backed-omada-health.html
- F08: https://www.barchart.com/story/news/305114/omada-adds-cholesterol-care-to-its-integrated-platform-addressing-the-silent-driver-of-cardiovascular-risk
- F10: https://pulse2.com/knownwell-20-million-funding/
- F13: https://jobs.generalcatalyst.com/companies/devoted-health/jobs/87410884-cardiovascular-clinical-guide
- F14: https://www.statnews.com/2023/05/16/artificial-intelligence-health-care-llm-general-catalyst-a16z/
- F15: https://www.businesswire.com/news/home/20250109643850/en/Hippocratic-AI-Completes-141MM-Series-B-Financing-Round-Led-by-Kleiner-Perkins-Valuing-the-Company-at-1.64B
- F19: https://www.businesswire.com/news/home/20211005005475/en/Andreessen-Horowitz-Leads-22M-in-Funding-for-Thyme-Care-to-Improve-Patient-Outcomes-Close-Gaps-in-Health-Disparities-and-Drive-Value-Based-Cancer-Care
- F21: https://hcttf.org/wp-content/uploads/2026/02/Advancing-Value-Based-Oncology-Through-247-Integrated-Virtual-Cancer-Care-1.pdf
- F22: https://www.businesswire.com/news/home/20240311529401/en/milu-health-announces-4.8m-seed-round-led-by-a16z-bio-health-and-partners-with-employers-to-expand-employee-access-to-ai-driven-health-savings-platform
- F24: https://af.net/realtime/clinical-ai-startup-openevidence-secures-250m-led-by-andreessen-horowitz-at-15b-valuation/
- F28: https://medcitynews.com/2021/07/johns-hopkins-spinoff-looking-to-build-better-risk-prediction-tools-emerges-with-15m/
- F30: https://www.unite.ai/?p=459992
- F33: https://thenextweb.com/news/telepatia-ai-healthcare-latin-america-33m-a16z ; https://www.valoraanalitik.com/telepatia-ia-para-reducir-errores-medicos/
- F35: https://www.beckershospitalreview.com/healthcare-information-technology/innovation/abridge-closes-300m-in-series-e-funding-hits-5-3b-valuation/
- F36: https://hitconsultant.net/2026/04/02/klas-report-abridge-ambient-ai-nursing-flowsheets-ehr/
- F38: https://siliconangle.com/2025/07/29/ai-native-clinical-documentation-startup-ambience-healthcare-raises-243m/
- F42: https://www.citybiz.co/article/223273/story-health-raises-22-6-million-in-series-a/
- F43: https://www.virtahealth.com/press/virta-health-raises-45-million-to-expand-treatment-for-type-2-diabetes-reversal
- F44: https://globalventuring.com/corporate/biofourmis-takes-care-with-300m/
- F45: https://www.techstackipo.com/company/cityblock-health
- F46: https://siliconangle.com/2025/05/15/akido-lands-60m-grow-ai-platform-underserved-healthcare-settings
- F47: https://pulse2.com/doctronic-40-million-raised-for-ai-based-prescription-renewal-and-autonomous-clinical-care-platform
- F48: https://techcrunch.com/2020/11/17/levels-raises-12m-from-a16z-and-others-to-bring-its-biowearable-to-market ; https://a16z.com/2016/10/20/cardiogram
- F49: https://aiweekly.co/alerts/pillpack-founders-general-medicine-raises-120m-series-b-led-by-a16z-with-eli
- F50: https://pmc.ncbi.nlm.nih.gov/articles/PMC12079355/ ; https://www.hirudotherapysociety.org/en/research/retrospective-modeling-study-of-chatgpt-gpt-tezcan-2026

Reused, not re-opened: D2-06-F1, F11, F20, F42, F43, F49, F50; D3-03 (Counsel, Hippocratic checks); D6-02-F01, F16; D1-04-F04, F06, F07, F10, F36.
