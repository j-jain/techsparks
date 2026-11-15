# R2-05 AI and Systems  (agent: Opus, date 2026-11-03)

Method notes (read first)
- Reddit counts come from the arctic-shift mirror API (`arctic-shift.photon-reddit.com/api/posts/search`, fetched 3 Nov 2026). Scores are as of the mirror's capture, which is often hours after posting, so they understate live totals. Posts the mirror captured at score 1 are marked "(stale)". Post links are given as reddit.com/r/<sub>/comments/<id>/.
- YouTube view counts come from YouTube's own search-results page sorted by views, parsed directly on 3 Nov 2026 (not the returnyoutubedislike API; Invidious search endpoints were down). The "age" is YouTube's relative label on 3 Nov 2026.
- "(fetched)" = I opened the page. "(snippet)" = from search-result text only. "(my arithmetic)" = my own multiplication. "(background)" = my own technical knowledge, not sourced this round; Round 3 should verify.
- Risk score scale: 5 = lowest risk.

---

## Problem: F1 "Digital arrest" and impersonation-call scams on the elderly (nothing protects the victim during the call)

### (a) Proof dossier
Independent public items I can now stand behind: 14 or more (6 Reddit threads by different posters on different dates, 6 or more organic YouTube videos from different channels, plus the Round 1 news cases). Best ones:
- https://www.reddit.com/r/india/comments/1m3rf36/ — 19 Jul 2025 — 543 upvotes, 24 comments (mirror) — "India's first digital arrest conviction: 9 sentenced to life by Bengal court".
- https://www.reddit.com/r/india/comments/1hphezu/ — 30 Dec 2024 — 434 upvotes, 70 comments (mirror) — first-person: "Wasted 40 mins of a digital arrest scammer"; shows how common the call is.
- https://www.reddit.com/r/india/comments/1hkht8d/ — 23 Dec 2024 — 346 upvotes, 80 comments (mirror) — Bengaluru techie loses Rs 11.8 crore.
- https://www.reddit.com/r/india/comments/1q5dawp/ — 6 Jan 2026 — 193 upvotes, 19 comments (mirror) — Hyderabad man, 81, loses Rs 7 crore, named in a fake drugs case.
- https://www.reddit.com/r/india/comments/1fyqjmu/ — 8 Oct 2024 — 150 upvotes, 20 comments (mirror) — journalist's own digital-arrest ordeal ("I thought it was a scam call until I didn't").
- https://www.reddit.com/r/india/comments/1hnxev2/ — 28 Dec 2024 — 17 upvotes, 23 comments (mirror) — first-person: "Truecaller premium probably saved me from digital arrest".
- https://www.youtube.com/watch?v=boV205aW4dM — ~2 years old — 32.9 million views (YouTube search page, 3 Nov 2026) — A2 Motivation (Arvind Arora) short, "Delhi में नया Scam! लड़की कैसे हो गई Digital Arrest".
- https://www.youtube.com/watch?v=hzNkrTEF7MQ — ~1 year — 9.78 million views — Santosh Patel DSP (a serving police officer), "डिजिटल अरेस्ट की धारा कौन सी है?".
- https://www.youtube.com/watch?v=AFOe88JU8uM — ~1 year — 3.99 million views — News 24, anchor Rimjhim Jethani on her own digital-arrest fraud ("मेरे साथ हुआ बड़ा Fraud").
- https://www.youtube.com/watch?v=gqCN7mAusDo — ~2 years — 2.34 million views — The Lallantop: scammer tries to "digitally arrest" its own journalist (a second Lallantop video, SlAPLyHM0Jo, has 2.06 million; an Aaj Tak journalist's story T9qeoB-D6nw has 2.17 million; Tamil comedy channel Parithabangal 8SvwL3a2tAE has 2.71 million).
- Paid awareness spots, NOT counted as organic proof but they show who already pays (see (b)): NPCI "UPI Chalega" डिजिटल अरेस्ट 6pS7c80RQqY 434 million views; RBI "Digital Arrest – Handcuff" RQ46CJBe3NQ 333 million and "Interrogation" siyTZ6DaFeQ 189 million; ICICI ZBS0e2azeug 31.5 million; IDBI cJZimhwAOy8 30.9 million; SBI qvqmRQby-wk 22.6 million and LdRe3U4vOro 22.2 million; HDFC "Vigil Aunty" L5u1GmBn5zk 20.1 million (all YouTube search page, 3 Nov 2026).

Strongest hard numbers:
- 2024: 1,23,672 digital-arrest cases, Rs 1,935.51 crore lost (Rajya Sabha reply quoted by The Quint, 17 Apr 2025; carried from R1).
- 2025: Rs 19,812.96 crore lost to cyber-financial fraud, ~21.77 lakh complaints (I4C/NCRP, https://ianslive.in/indians-lose-over-rs-52976-crore-to-cyber-frauds-over-six-years-report--20260103154943, 3 Jan 2026). By amount: investment schemes 77%, digital arrest 8%, credit-card fraud 7%. By complaint count: investment 36%, digital arrest 6% (snippet, search summary of the same I4C coverage). 8% of Rs 19,813 crore = Rs 1,585 crore for digital arrest in 2025 (my arithmetic).
- Saved vs recovered: Rs 7,130 crore "saved" (held before it left the system) across 23.02 lakh complaints, cumulative since the 1930/CFCFRMS system launched in 2021, MoS reply to MP Nathwani in Rajya Sabha (https://deshgujarat.com/2025/12/03/over-rs-7130-crore-saved-in-23-02-lakh-cyber-fraud-complaints-govt-to-rs-mp-nathwani, 3 Dec 2025, snippet). Actual money returned to victims: NOT FOUND. MHA: ~Rs 7,000 crore lost to online scams in the first five months of 2025 (cited in TechCrunch, 20 Nov 2025, fetched).
- Supreme Court, 9 Feb 2026, suo motu digital-arrest case: called the siphoning of "over Rs 54,000 crore" by digital fraud "robbery or dacoity", told the Centre to frame an SOP with RBI and banks, and asked RBI/DoT to meet on a victim-compensation framework (https://theprint.in/india/sc-terms-siphoning-of-over-rs-54000-cr-by-digital-fraud-dacoity-asks-centre-to-frame-sop/2849955, 9 Feb 2026, snippet; Business Standard's lede says ~Rs 52,000 crore). CORRECTION: an r/india thread title (1r0s6o7) says "Rs 54,000 crore in digital arrest cases"; it is total digital fraud, likely the same pool as I4C's Rs 52,976 crore six-year total (my inference). Do not cite Rs 54,000 crore as digital-arrest loss.

Final tier: A. Five or more independent threads/videos with real engagement (three Reddit threads at 340-540 upvotes; four organic YouTube videos above 2 million views each) plus government numbers. Caveat: Reddit engagement is in the hundreds, not thousands; the biggest YouTube numbers are paid bank/RBI ads.

Round 1 figures: the 8% share is by amount (6% by count); R1's "Supreme Court observed over Rs 3,000 crore by Nov 2025" (kuvera.in snippet) is still unverified.

Q6, investment/trading-app scams (the 77%), in brief: real and larger, but it is not a phone-call moment. Victims are pulled into WhatsApp/Telegram "stock tip" groups and fake trading apps over weeks. Examples: Delhi, 78-year-old loses ~Rs 19 crore in a WhatsApp IPO group (https://www.courtkutchehry.com/pages/blog/delhi-whatsapp-ipo-scam-19-crore-cyber-fraud, Dec 2025, snippet); Mumbai businessman Rs 3.43 crore, fake app showed Rs 44 crore "profit" (https://www.freepressjournal.in/mumbai/mumbai-businessman-loses-343-crore-in-whatsapp-share-trading-scam-fake-apps-showed-44-crore-profit, snippet); Pune retired techie Rs 4.43 crore (https://gulfnews.com/world/asia/india/how-a-retired-techie-lost-rs44-3m-to-a-whatsapp-trading-scam-1.500568550, snippet); I4C/CyberDost advisory on fake WhatsApp tips (https://www.outlookmoney.com/news/i4c-warns-investors-against-fake-whatsapp-stock-tips-fake-trading-apps, snippet); "30,000 victims, Rs 1,500 crore in six months, Bengaluru 26%", attributed to an I4C report (https://www.newsx.com/business/how-telegram-and-whatsapp-is-helping-scammers-over-30000-victims-across-india-rs-1500-crore-losses-in-six-months-bengaluru-tops-the-list-99192/amp, undated, snippet). r/IndiaInvestments engagement was NOT CAPTURED: the mirror rate-limited every attempt on 3 Nov 2026. Judgement: do not widen this wedge. Investment fraud needs a text/app/payee classifier (WhatsApp groups, APKs, UPI payee risk), where PhonePe/Google Play Protect/DoT FRI already sit. The call-guard's family-alert channel could later carry an investment-group warning, but that is a second product.

### (b) Market size
Affected units:
- 60+ population: 13.8 crore in 2021, projected 19.38 crore in 2031 (NSO "Elderly in India 2021", via https://theprint.in/india/indias-elderly-population-to-rise-41-over-next-decade-to-touch-194-mn-in-2031-govt-report/710476/ and https://www.businesstoday.in/lifestyle/health/story/indias-elderly-population-grows-to-138-cr-in-2021-over-lower-death-rates-nso-study-304209-2021-08-15, Aug 2021, snippets). 2026 ≈ 13.8 + (19.38 − 13.8)/2 = 16.6 crore (my arithmetic, linear interpolation).
- Elderly smartphone ownership: NOT FOUND reliably (one undated paper says 60% of 104 million older adults own a smartphone, https://pmc.ncbi.nlm.nih.gov/articles/PMC8938771, snippet; weak).

TAM (consumer-equivalent ceiling): 16.6 crore seniors × Rs 300/yr (assumption: Rs 25/month bundled by a bank or telco) = Rs 4,980 crore/yr (my arithmetic). Treat as a ceiling: consumer willingness to pay is unproven, since Truecaller's family feature and Google's detector are free.

SAM (value-based, what a bank or insurer would rationally pay):
- Digital-arrest loss pool 2025 ≈ Rs 1,585 crore (above). Call-led pool if credit-card/OTP fraud (7%) is also call-initiated (assumption) = 15% × Rs 19,813 crore = Rs 2,972 crore (my arithmetic).
- At 10% of loss averted as the price (assumption): Rs 159-297 crore/yr (my arithmetic). That is the realistic revenue pool for a protection layer sold to banks, insurers or telcos.
- Hardware puck, consumer route: 50 lakh affluent senior-only or NRI-parent households (assumption, not sourced) × Rs 3,000 device = Rs 1,500 crore one-time (my arithmetic).

Who pays today:
- Banks, RBI and NPCI pay for awareness: paid YouTube spots with 20-434 million views each (list in (a)). That is the clearest sign a bank marketing or fraud budget exists for this.
- Google, Truecaller and Airtel give protection away free, as a feature that keeps users.
- The state pays for I4C and 1930.
- No published market size for call-scam protection in India was found.

Buyers in order: private banks (senior and wealth customers), general insurers selling cyber covers, telcos, phone makers. Families of NRI parents buying direct is a consumer side-door.

### (c) Competitive map
Q1, platform gate (this decides the product form):
- Android: microphone capture for call recording was removed in Android 10. Google Play banned use of the Accessibility API for remote call audio from 11 May 2022. Only the pre-installed default dialer (Google Phone, Mi Dialer) keeps native recording. Sources: https://www.engadget.com/google-is-banning-third-party-call-recording-apps-from-the-play-store-093201443.html (Apr 2022, snippet) and https://www.techradar.com/news/new-google-play-store-policy-cracks-down-on-call-recording-apps (snippet).
- Android permissions: the permission to read the downlink audio stream is system/privileged-only, and Android does not let a second app capture the mic during a VoIP call such as WhatsApp (background; verify in R3).
- iOS: no third-party access to call audio. iOS 18's native call recording announces itself to both parties (https://www.idropnews.com/how-to/your-iphone-can-record-phone-calls-in-ios-18-heres-how-it-will-work/221524, 2024, snippet).
- Consequence: a third-party app cannot listen to the call. The options are (i) an OEM/dialer feature (Google and Samsung are already doing this on premium phones), (ii) telco-side metadata (what Airtel does; telco reading call content would be interception territory under the Telecom Act, background), or (iii) an external acoustic device in the room. Digital-arrest "custody" runs for hours on WhatsApp/Skype video (R1), so a room device hears at least the victim's side and the scammer's side when on speaker.

Players:
| Product | What it does | Status / funding | What it does NOT do (the gap) |
|---|---|---|---|
| Google Scam Detection (Phone by Google) | On-device Gemini Nano listens to calls from unknown numbers and warns; Hindi and English in India; announced 20 Nov 2025; plus screen-share alerts with Navi, Paytm, GPay (pilot, Android 11+) | Alive. TechCrunch (fetched, 20 Nov 2025): Pixel 9+ only, Pixel <1% of Indian market, off by default, plays a beep | Not on the budget Android phones and feature phones seniors use; Phone-app calls only, not WhatsApp/Skype video custody (my inference from scope); no family alert; no regional languages beyond Hindi/English |
| Samsung (Galaxy S26, One UI 8.5+) | Google's detector adapted for Galaxy | Launched at Unpacked 2026 (https://www.techrepublic.com/article/news-google-gemini-scam-detection-android-samsung-expansion/, snippet); vivo/Xiaomi support seen only in teardowns (https://www.androidauthority.com/p-3699159/, snippet) | Flagships first; the same gaps as Google; shows the gap is closing from the top of the market |
| Truecaller Family Protection (India) | One family admin is alerted when a member is called by a flagged or suspicious number, and can remotely end the call; shared block lists | Launched in India 13 Mar 2026 (https://www.fonearena.com/blog/?p=477504, fetched); core free, paid family plan; Android and iOS | Number-reputation based, not call content; fresh SIMs and video-call custody slip through. Truecaller's AI voice-clone scanner is US-only Premium since May 2024; India "soon" (https://business-standard.com/amp/technology/apps/truecaller-introduces-ai-call-scanner-feature-on-android-app-how-it-works-124052901441_1.html, snippet) |
| Airtel Fraud Alert | Network-level, no app: warns when a bank OTP arrives during a call that matches scam patterns | Launched 11 Feb 2026, Haryana first, then nationwide "over the next two weeks" (https://telecomtalk.info/bharti-airtel-curb-otp-banking-fraud-calls/1004293/, fetched); Airtel claims 30,000 frauds/day stopped (https://theprint.in/india/airtel-ai-algorithm-to-protect-customers-from-scams/2856991, snippet, unverified); also Airtel spam filter since Sep 2024 (R1) | Keyed to the OTP-on-call moment; digital-arrest transfers are RTGS/branch transfers over days of video "custody"; Airtel subscribers only; does not hear content |
| DoT Financial Fraud Risk Indicator (FRI) | Rates mobile numbers Medium/High/Very High risk on the Digital Intelligence Platform; PhonePe auto-declines Very High | Live 21 May 2025 (https://www.business-standard.com/industry/news/dot-launches-financial-fraud-risk-indicator-to-aid-cybercrime-detection-125052101912_1.html, snippet); 34 banks/PSPs froze 10.02 lakh accounts (https://www.governancenow.com/news/regular-story/how-dots-fraud-risk-indicator-empowers-stakeholders, 6 Aug 2025, snippet) | Protects payment rails after the fact; no grievance path (MediaNama, snippet); does not help the victim during the call |
| JioBharat "Safety-First" phones | Rs 799 4G feature phone; guardian controls who can call, blocks unknown numbers, live location | Launched IMC, 9 Oct 2025 (https://www.businesstoday.in/technology/news/story/jio-launches-safety-first-jiobharat-phones-and-ai-classroom-course-at-india-mobile-congress-2025-497431-2025-10-09, snippet). Jio sold 135 million JioPhone units overall (https://telecomtalk.info/?p=985265, snippet, undated) | A whitelist blunt instrument; no content analysis. It does show Jio thinks guardian-controlled phones for elderly users can be sold |
| Singapore ScamShield (OGP, state) | Blocks calls/SMS using police blacklist plus an on-device classifier | Alive. 820k+ downloads (https://ncpc.org.sg/scamshield, snippet); call-blocking permission rose 23%→80% after onboarding fixes (https://reports.open.gov.sg/scamshield/updates, snippet); national effort blocked 117 million calls by May 2025 (https://archive.opengovasia.com/2025/05/16/singapore-unified-strategy-strengthens-public-protection-and-trust/, snippet) | List-based; no live speech understanding. A state-run app is the model India's Sanchar Saathi follows |
| Indian startups | Kavach (pre-launch waitlist for a "digital arrest" shield, no company named, https://kavach-protect.pages.dev/); Panoplia.io/AI Kavach (2023, no call screening, https://yourstory.com/2023/11/panopliaio-combats-cyber-fraud-india-ai-backed-solutions); Quick Heal AntiFraud.AI (reputation-based scam-call alerts); Drona Pay (bank transaction risk, https://yourstory.com/2025/08/real-time-fraud-detection-startup-drona-pay-safe-digital-banking); a solo founder on r/india "building an AI 'Bodyguard' for Indian parents" (https://www.reddit.com/r/india/comments/1r23e59/, 11 Feb 2026, score 1) | No funding found for any live in-call product (all snippets) | No one ships live Hinglish content detection on the devices seniors use |

Gap, stated precisely: live, content-level detection of the impersonation script, (1) on budget Android and feature phones, (2) during WhatsApp/Skype video "custody", (3) in Hinglish and regional languages, (4) with a family member in the loop in real time. Google/Samsung cover (3)-partly on flagships; Truecaller covers (4) by number reputation only.

### (d) Solution approaches
1. Call-guard puck (hardware + edge ML). Pick this one.
   - Core: ESP32-S3 or Raspberry Pi Zero 2 W with a MEMS mic and speaker, placed by the parent's phone or TV room. On-device Hinglish keyword spotting runs continuously ("CBI", "ED", "money laundering", "aapka parcel", "arrest warrant", "kisi ko mat batana", "video on rakhiye", "RBI verification account", "transfer for clearance"). A second stage gets on-device or LAN-local ASR (faster-whisper/IndicWhisper on a Pi 5 or the family's old phone) plus a small intent classifier scoring four cues: authority claim, secrecy/isolation, a threat, and a payment demand. It also uses duration: hours-long, unknown-caller, and "camera on".
   - Output: a loud Hindi voice prompt on the puck ("Police video call par arrest nahi karti. Phone kaatiye, 1930 par call kijiye") plus a WhatsApp/SMS alert to the child. No audio leaves the device.
   - Team: CS builds KWS, ASR and the classifier; hardware builds the puck, enclosure and GSM/Wi-Fi alert; the bio member is not needed.
   - First customer: a private bank's senior-citizen or wealth desk, or a senior-living operator; consumer route through NRI children.
   - Unit economics: BOM ~Rs 1,500-2,500 (assumption); sell at Rs 3,999 or bank-subsidised plus Rs 99/month.
   - Moat: a labelled Hinglish/regional scam-script corpus, and working without any phone or OS access, which Google and Truecaller cannot do.
2. Licensed scam-intent model (software). An Indic-language classifier for live transcripts licensed to dialer apps, telcos' IVR/voicemail, Truecaller-like apps, or banks' outbound call QA. Deep-tech core: streaming intent classification with low false positives on genuine police/bank calls. Risk: Google/Samsung are building it in-house.
3. Bank-side "senior session guard" (no audio). A bank SDK flags a senior's high-value transfer when it coincides with a long unknown-number call, screen share or a new payee, and adds a cooling-off delay plus a family co-sign. This is mostly rules plus anomaly detection: weaker deep-tech, but the most direct buyer.

Why pick 1: it is the only form that sidesteps the Android/iOS audio block and covers feature phones and video-call custody. It also uses the team's hardware skill and demos well. Approach 2 is the business extension; approach 3 is the bank integration once a bank pilots the puck.

### (e) Regulatory and safety gates
- Blocks the overnight demo: none (staged calls among the team, no real call data).
- Blocks the business:
  - DPDP Act 2023 and Rules, notified 14 Nov 2025, phased over ~18 months to ~12 May 2027 (https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf, PIB; https://www.azbpartners.com/?p=87799, snippets). Processing the user's and the caller's speech needs a consent notice and purpose limitation; on-device, no-retention design minimises exposure.
  - WPC Equipment Type Approval for the Wi-Fi/BLE radio and possibly BIS CRS for the adapter (background; check in R3).
  - Recording a call one is party to is generally not barred in India, but a device recording a third party's voice should not store audio (background).
  - A telco-side variant reading call content runs into lawful-interception rules (Telecom Act 2023, background); stay off-network.
- Safety: a false negative is worse than none if families over-trust it. Market it as an alarm, not a guarantee.

### (f) Overnight wedge
- Demo by noon: the puck (ESP32-S3 + I2S mic + speaker) runs a keyword spotter, streaming to a laptop or Pi running faster-whisper (Hindi/Hinglish) plus a classifier. A team member plays the "CBI officer" on speakerphone; the puck speaks a Hindi warning and a phone receives a WhatsApp/Telegram alert, with a dashboard showing the cue timeline.
- Training data: ~300 synthetic Hinglish scam turns written from published victim accounts (Quint, Lallantop, News 24 videos) and ~300 benign turns (bank KYC call, courier, doctor, relatives).
- Honest test result reachable in ~14 h: 40 role-played calls (20 scam scripts in four variants, 20 benign including a genuine-sounding bank fraud-team call). Report recall, false-positive count, and median seconds-to-alert, with a confusion matrix. Expect this to be optimistic because the test data is staged; say so.
- Deep Tech Thesis: the fraud runs on a time window (hours of "custody") and a platform blind spot (no app may hear calls). An acoustic, on-device, family-in-the-loop guard closes the window without OS access, on any phone, in Hinglish.

### (g) Verdict
- Real: yes; Rs 1,585-1,935 crore a year and a Supreme Court suo motu case.
- Unsolved: partly. Google/Samsung (flagships, Hindi/English) and Truecaller (family alert, number-based) narrowed the gap in the last 12 months. What remains is budget/feature phones, video-call custody, regional languages, and content-level family alerts.
- Sellable: unproven. Consumers get free tools; the realistic payer is a bank or insurer, and no bank has been asked.
- Buildable overnight: yes.

Scores: proof 5, market 3, feasibility 4, unsolved gap 3, deep-tech 4, risk 3.

Round 3 should check:
1. What share of digital-arrest victims are reached on WhatsApp/Skype video or feature phones versus normal calls (I4C modus-operandi split).
2. Whether a bank or insurer will pay per protected senior, especially after the Supreme Court's Feb 2026 push for an RBI compensation framework.
3. Google Scam Detection's roadmap to mid-range Android in India and to regional languages, which would erase the software gap.

---

## Problem: D1 Exam integrity: paper leaks and remote-access cheating in high-stakes exams

### (a) Proof dossier
Independent items now: 16 or more (Reddit threads from different posters, YouTube from different channels, national news). Best ones:
- https://www.reddit.com/r/india/comments/1vhub0a/ — 7 Aug 2026 — 754 upvotes, 51 comments (mirror) — "NTA's own experts leaked NEET-UG papers for cash, CBI chargesheet alleges".
- https://www.reddit.com/r/india/comments/1v5wygb/ — 25 Jul 2026 — 315 upvotes, 49 comments (mirror) — "47 NTA officials sacked in major NEET paper leak purge".
- https://www.reddit.com/r/india/comments/1v5edjq/ — 24 Jul 2026 — 503 upvotes, 88 comments (mirror) — protest thread on the education minister's resignation; a political movement ("CJP") ran the NEET agitation (also 1v6tyre, 704 upvotes, 26 Jul 2026).
- https://www.reddit.com/r/JEENEETards/comments/1vkfsmg/ — 10 Aug 2026 — 1,007 upvotes, 34 comments (mirror) — meme on leaks ("IS company ke pen bahut leak hote"). Shows saturation; not substantive.
- https://www.reddit.com/r/JEENEETards/comments/1vjh3zv/ — 9 Aug 2026 — score 1 (stale) — the sharpest user insight: "If the paper setters faciliated the leak, how come a CBT NEET is going to fix that issue?"
- https://www.youtube.com/watch?v=TlppYYh-Gwc — ~5 months — 9.16 million views (YouTube search page, 3 Nov 2026) — Dhruv Rathee, "India's BIGGEST Exam Fraud | How NEET was Leaked!". The same creator's 2024 NEET video BFU9eSKO_t4 has 15.4 million: the problem recurs.
- https://www.youtube.com/watch?v=bQlWBvvJMcU — ~5 months — 11.0 million views — Professor Of How, "How NEET Paper Leaked? (3D)".
- https://www.youtube.com/watch?v=K_GR6A9dp0w — ~3 months — 8.43 million views — Democratic Times, NEET leak parliament march and student protest.
- https://www.youtube.com/watch?v=-Z_iD88MEvA — ~5 months — 3.28 million views — TV9 Bharatvarsh, accused's house, Jaipur.
- https://www.youtube.com/watch?v=ykCvifYo7bY — ~5 months — 314k views — The Followup, "कंप्यूटर अपने आप हल कर रहा था सवाल! SSC GD परीक्षा में धांधली" (remote-access cheating); also Testbook pOUZY6ZN0zQ, 97k ("SSC GD 2026 Exam Scam, 13 लाख में हुई Deal").
- https://news.careers360.com/ssc-cgl-2025-dhanbad-server-manager-arrested-cheating-case-scam-gang-candidates-mouse-answers-vendor-chairman-supreme-court — 30 Sep 2025 — (fetched) Dhanbad centre server manager arrested; a candidate only moved the mouse "while the system auto-selected answers"; SSC: "Some cases of remote access attempts have also been detected"; CGL 2025 had 28 lakh registered, ~13.5 lakh appeared.

Strongest hard numbers:
- NEET-UG 2026 cancelled (exam 3 May, cancelled 12 May), ~22.79 lakh candidates. Re-exam 21 Jun 2026: 5,440 centres in 551 cities plus 14 abroad; 1,38,560 CCTV cameras; 51,311 jammers (ECIL 17,054, BEL 34,257); 48,448 biometric staff; ~1,500 bank branches as custodians; ~700 OMR collection centres (https://businesstoday.in/education/exams/story/jammers-1-38-lakh-cctv-cameras-ai-surveillance-ntas-security-plan-for-big-neet-re-exam-today-538271-2026-06-21, 21 Jun 2026, fetched).
- CBI chargesheet, 28 Jul 2026: 13 accused including three NTA subject experts (Botany, Chemistry, Physics). The Chemistry expert had translated the paper Marathi→English. Leaked PDFs/images circulated on Telegram/WhatsApp "several days before"; one deal of Rs 25 lakh; a candidate offered access for Rs 4 lakh (https://openthemagazine.com/india/cbi-cracks-neet-ug-2026-paper-leak-chargesheet-alleges-nta-experts-sold-questions-in-multi-state-exam-racket, updated 7 Aug 2026, fetched; ~20,000 pages, 360 witnesses, 422 documents per https://www.thestar.com.my/aseanplus/aseanplus-news/2026/07/29/neet-ug-paper-leak-indian-cbis-20000-page-charge-sheet-cites-360-witnesses-422-documents-against-13-accused, snippet). An early CBI finding: the leaked paper was handwritten, scanned and turned into PDFs (https://medicaldialogues.in/amp/state-news/delhi/how-did-neet-2026-leaked-paper-circulate-cbi-probe-finds-170604, snippet).
- NTA: 270+ exams and 6.6 crore candidate registrations since 2018, with 24 employees (https://thewire.in/education/conflicting-nta-expenditure-data-triggers-privilege-motion-in-parliament, 27 Jul 2026, fetched). Fee income ~Rs 1,117 crore in 2023-24 (https://www.freepressjournal.in/amp/education/centre-reveals-nta-has-39-permanent-posts-conducted-over-270-exams-since-2018-income-increases-to-1117-crore-in-five-years, snippet).
- Earlier: 89 leak cases in a decade (Newslaundry, 31 Jul 2024, R1).

Final tier: A. Several Reddit threads at 300-1,000 upvotes, multiple YouTube videos at 3-11 million views in 2026, a CBI chargesheet and parliamentary data.

Round 1 corrections:
- (1) R1's "NEET re-exam of 21 June 2026 would be CBT (unverified)": wrong. The re-exam was pen-and-paper OMR; CBT is promised from 2027 (https://www.freepressjournal.in/education/neet-ug-2026-re-exam-faqs-what-students-need-to-know-about-exam-date-admit-cards-and-cbt-mode and https://www.indiatvnews.com/education/news/from-neet-s-shift-to-computer-based-mode-to-15-minute-extra-in-re-exam-five-big-announcements-by-pradhan-2026-05-15-1041229, 15 May 2026, snippets).
- (2) R1's "leak origin upstream (printing press)": the chargesheet points at NTA's own subject experts/translator; the Nashik press link is a May media account not confirmed in chargesheet coverage.

### (b) Market size
Q2, budgets and contracts found (all show exam-tech contracts run to hundreds of crores, but the security slice is small):
- NTA: collected Rs 3,512.98 crore and spent Rs 3,064.77 crore on exam conduct, 2018-19 to 2023-24 (https://news.careers360.com/nta-national-testing-agency-exam-fees-income-3514-cr-rose-after-cuet-ug-neet-jee-main-449-crore-balance-parliament, 2024, snippet), ≈ Rs 510 crore/yr spent on average (my arithmetic). Income was Rs 504 crore in 2019-20 and Rs 1,117 crore in 2023-24. A July 2026 Rajya Sabha reply gives figures Rs 16-51 crore higher, which triggered a privilege motion (The Wire, fetched).
- SSC CBT: Eduquity replaced TCS from July 2025 (https://www.oliveboard.in/blog/what-the-ssc-vendor-change-and-pattern-shifts-mean/, snippet). The contract is reportedly ~Rs 273 crore against a higher ~Rs 450 crore bid. Reported per-candidate rates conflict: Rs 171 vs TCS Rs 311 (https://ccagentorg.github.io/cbse-osm-osint/know-your-examtech.html, unofficial OSINT site) and Rs 220 vs Rs 350 (https://the420.in/eduquity-ssc-exam-controversy-server-crash-protests/). All unverified; no SSC document found.
- CBSE on-screen marking 2026: Coempt won at an evaluated Rs 384.6 crore vs TCS Rs 951.3 crore; Rs 24.75-25.74 vs Rs 53-65 per answer booklet (https://www.businesstoday.in/india/story/cbse-osm-portal-row-coempt-won-against-tcs-by-2-marks-60-percent-lower-financial-bid-534378-2026-06-02, 2 Jun 2026, fetched).
- Tender values for NTA's own vendors (TCS iON for CBT, the print vendors): NOT FOUND.

Bottom-up, integrity-analytics layer:
- Candidate-sittings per year:
  - NTA: 6.6 crore registrations over ~8 years ≈ 0.8 crore/yr; take ~1 crore/yr for 2026 given income doubling (my arithmetic plus assumption).
  - SSC: ≥0.3 crore (CGL alone 28 lakh registered, 2025).
  - State recruitment: ≥0.28 crore/yr (1.4 crore applicants in leaked exams over 5 years, Indian Express via R1, snippet).
  - Total ≈ 1.6 crore/yr, a lower bound (my arithmetic).
- Price: Rs 15-30 per candidate-sitting (assumption: 5-10% of the reported Rs 171-311 SSC CBT rate).
- TAM ≈ 1.6 crore × Rs 15-30 = Rs 24-48 crore/yr (my arithmetic). Cross-check: 3-5% of NTA's ~Rs 1,100 crore income ≈ Rs 33-55 crore, consistent.
- Hardware trunk loggers: a NEET-scale pen-paper exam has 5,440 centres × ~3 sealed trunks (assumption) ≈ 16,300 loggers × Rs 4,000 (assumption) ≈ Rs 6.5 crore one-time per exam body (my arithmetic). Board exams multiply this, but their centre counts were not gathered.
- SAM (3 years): 2-4 buyers (a state board or PSC, a CBT vendor, a university) × Rs 1-3 crore/yr = Rs 2-12 crore/yr (assumption).

Buyers: NTA (central), SSC (central), state PSCs/SSBs/boards (state), and CBT vendors TCS iON and Eduquity (firms that carry the legal liability).

No published "exam security" market figure was found.

### (c) Competitive map
Q3, exam-security technology:
- Per-copy codes are already standard in Indian boards, so plain watermarking is NOT a gap:
  - West Bengal Madhyamik hides a serial number on every page; 14 candidates were barred after photos were traced (https://obeta.ttef.in/my-kolkata/news/code-hooks-madhyamik-errant-duo-students-barred-from-test-for-clicking-questions/cid/1997989, snippet).
  - Haryana BSEH: QR code plus a unique number at three places per page, used to trace leakers (https://www.tribuneindia.com/news/haryana/to-check-paper-leak-board-question-papers-to-now-have-qr-code-481413, snippet).
  - Odisha BSE: QR, watermark and serial (https://news.careers360.com/bse-odisha-use-watermarks-barcodes-in-class-10-examinations-2025-prevent-paper-leaks, snippet).
  - Andhra Pradesh and Telangana: centre/hall codes (https://telanganatoday.com/andhra-pradesh-ssc-board-prints-qr-codes-on-question-paper-to-prevent-leaks, https://telanganatoday.com/qr-codes-and-security-numbers-to-secure-telangana-ssc-questions-from-leakage, snippets).
  - NEET-UG 2024: a serial code on a half-burnt paper was matched to a Hazaribagh centre (https://deccanherald.com/india/bihar/neet-row-bihar-police-found-68-matching-questions-among-burnt-scraps-3078066, snippet).
  - NEET 2026 re-exam: GPS-tracked transport, "traceable watermark identifiers" and IAF transport, reported by coaching sites and news (https://www.pw.live/neet/exams/nta-security-measures-for-neet-re-exam-2026, https://www.tribuneindia.com/news/india/neet-ug-2026-re-exam-iaf-to-transport-question-papers-as-nta-rolls-out-unprecedented-security-measures, snippets; weak).
- Why visual codes failed in 2026: the leak came from subject experts/translator before printing, and the copy was handwritten then scanned. Visual codes do not exist at that stage and do not survive retyping. Content-level canaries do survive: each insider's working copy carries unique paraphrases, numeric values and option orders (the "canary trap", background). So do "honey items", a variant whose answer differs from the final paper, so anyone who memorised the leaked answers marks a variant-specific wrong answer. In Indian exam bodies this was NOT FOUND (no evidence either way).
- Response forensics:
  - Caveon (US) sells data forensics: similarity statistics for collusion, answer copying, test-content sharing, and "did better on hard items than easy ones" patterns (https://blog.caveon.com/statistics-detect-test-cheating, snippet).
  - Questionmark partnered with Caveon in Dec 2019 (https://www.businesswire.com/news/home/20191209005569/en/, snippet).
  - Critics say Caveon's methods are not published in peer-reviewed literature (https://www.staradvertiser.com/2010/12/28/news/digital-cheaters-find-adversary-in-technology/, Dec 2010, snippet).
  - Caveon/ETS prices: NOT FOUND. Indian use of such forensics for NEET/SSC: NOT FOUND (the 2024 NEET Supreme Court case relied on a result analysis; background, unverified).
- Remote-access detection in CBT centres: the vendor's job. SSC says flagged terminals shut automatically (R1 snippet), yet arrests keep coming:
  - Dhanbad, Sep 2025 (fetched above).
  - UP/Uttarakhand STF on SSC MTS, local-network proxy (https://theprint.in/india/up-uttarakhand-stf-bust-gang-helping-candidates-cheat-in-ssc-mts-recruitment-exam/2855231, snippet).
  - Greater Noida, a Class-12 pass-out using a proxy server (https://theprint.in/india/youtube-tutorials-proxy-server-how-a-class-12-passout-helped-rig-ssc-exams-in-greater-noida/2939565/, snippet).
  - Ranchi SSC GD 2026, six held (https://telanganatoday.com/ranchi-police-bust-high-tech-ssc-gd-exam-racket-six-held, snippet).
  - Bihar CHO exam via AnyDesk (https://morungexpress.com/tech-savvy-exam-mafia-used-anydesk-software-to-solve-cho-papers-in-bihar, snippet).
  - No vendor of an independent centre-network sensor found.
- Physical: jammers from PSUs ECIL and BEL; CCTV with AI anomaly flags (NTA's own, vendor unknown). Tamper-evident trunk loggers: "digital locks" appear only on one coaching blog (https://www.ocacademy.in/blogs/neet-re-examination-2026-update, snippet). No Indian vendor or price found.
- Online-proctoring firms (Mercer-Mettl, Eklavvya and others): NOT SEARCHED; Eklavvya is marketing "CBT readiness after the 2026 NTA overhaul" (https://www.eklavvya.com/blog/?p=24054, vendor blog).

Q1, government programmes and what happened after May 2026:
- Radhakrishnan committee (report 21 Oct 2024; 101 recommendations):
  - Main items: computer-assisted secure pen-and-paper testing (encrypted papers sent to centres and printed just before the exam), DIGI-EXAM biometric/AI verification, 1,000 secure government centres, less outsourcing, and NTA verticals for information security, vigilance and forensics (Outlook explainer, fetched).
  - Status:
    - Radhakrishnan told the Supreme Court in May 2026 that a majority were implemented or in progress (https://www.newkerala.com/news/a/majority-neet-reform-recommendations-already-implemented-former-isro-713.htm, snippet).
    - The parliamentary education committee (June 2026) asked for a time-bound roadmap and said irregularities are "still rampant" (https://news.careers360.com/nta-exam-reform-time-bound-implementation-roadmap-aishe-survey-cabe-digvijaya-singh-parliament-panel-higher-education-ministry, snippet).
    - The Supreme Court asked NTA to report the steps taken (https://www.etvbharat.com/en/bharat/neet-sc-directs-nta-to-inform-on-steps-taken-to-implement-recommendations-of-radhakrishnan-panel-enn26081902733, Aug 2026, snippet).
- Political fallout: Education Minister Dharmendra Pradhan resigned 25 Jul 2026. The Nilekani task force was announced 26 Jul 2026 (with S. Somanath, Tapan Deka, Amrit Lal Meena, Anita Karwal, V. Kamakoti) "to recommend the next phase of examination reforms and future-proof the NTA" (https://www.outlookindia.com/national/outlook-explains-from-radhakrishnan-to-nilekani-why-india-is-revisiting-neet-reforms, fetched). Its report: NOT FOUND.
- Public Examinations (Prevention of Unfair Means) Amendment Bill: introduced 27 Jul 2026, up to 10 years and Rs 10 crore (Outlook, fetched); passed by the Lok Sabha 29 Jul 2026 (r/JEENEETards 1v9u3l1, title only, score 1).
- 47 NTA officials sacked (r/india 1v5wygb title, 25 Jul 2026; not verified against a primary source).

### (d) Solution approaches
1. Leak attribution and beneficiary forensics (software). Pick this one.
   - (i) Per-insider content canaries generated at setting, translation and moderation: LLM-assisted paraphrase, numeric perturbation and option-order variants, with each variant checked by a subject expert.
   - (ii) A leak matcher: OCR of a leaked photo or handwritten PDF, then fuzzy and semantic matching against all variants, returning the source variant and so the insider.
   - (iii) Post-exam response forensics on OMR/CBT data: accuracy on leaked-subset items vs other items, honey-item hits, person-fit statistics, and answer-string similarity clusters by centre. This gives the exam body evidence for "cancel or not".
   - Team: CS does NLP, OCR and statistics; the bio member verifies Biology/Chemistry variants stay scientifically correct (this matters for NEET).
   - First customer: a state board or state PSC that already prints QR codes, adding attribution through its print vendor. Unit economics: Rs 15-30 per candidate-sitting (assumption).
   - Moat: honey-item design plus validated forensics thresholds; evidentiary acceptance in court.
2. CBT centre remote-access sensor (hardware + ML). A Raspberry Pi on a mirrored switch port fingerprints RDP/VNC/AnyDesk/proxy traffic and unknown hosts. A per-terminal agent scores mouse/keyboard dynamics (Dhanbad: the candidate "only moving the mouse" while answers were auto-selected; this is detectable as zero-keystroke, synthetic-cursor behaviour). Buyers: TCS iON and Eduquity, under service-provider liability. Rs 5-10k per centre plus a fee per sitting (assumption).
3. Tamper-evident trunk logger (hardware). ESP32 + reed switch + light sensor + IMU + secure element, BLE handshake with the authorised custodian's phone, and a signed open-event log; GPS optional. Sells to boards and NTA's custodian-bank chain. It is the easiest hardware to build but the weakest moat (commodity), and it does not address the 2026 failure mode (insider before printing).

Why pick 1: it targets how the 2026 leak actually happened and works for pen-and-paper now and CBT from 2027. Show 2 as a hardware add-on in the demo if time allows.

### (e) Regulatory and safety gates
- Q4: the Public Examinations Act 2024 and Rules (23 Jun 2024) define unfair means to include "unauthorized access or leakage of question paper" and tampering with computer networks. They make service providers liable (fine up to Rs 1 crore plus recovery of the proportionate exam cost) (https://visionias.in/current-affairs/news-today/2024-06-26/polity-and-governance/public-examination-prevention-of-unfair-means-rules-2024-notified, fetched).
- The 2026 amendment raises penalties to up to Rs 10 crore/10 years (Outlook, fetched); a vendor blog claims Rs 5 crore and 8-year debarment for providers (unverified).
- The Act creates no explicit procurement obligation for any technology that I could find; the Rules leave "norms or standards" to be notified. The demand is indirect: vendor liability plus political pressure.
- Procurement: GFR/GeM tenders with turnover and experience criteria (background; DPIIT-startup relaxations exist but verify). The candidate response data is personal data under DPDP and needs an MoU with the exam body.
- Blocks the overnight demo: none (synthetic papers and synthetic candidates). Blocks the business: access to real response data, a tender route, and evidentiary acceptance.

Q6, can a student team reach NTA/SSC within a year? Directly, probably not:
- NTA has 24 staff, is mid-restructuring under a task force, is politically radioactive (minister resigned, protests, arrests of protesters), and buys through large vendors.
- Realistic path in 12 months:
  - (a) one state board or university as a pilot;
  - (b) a subcontract or licence to a CBT/print vendor (TCS iON, Eduquity, Coempt) that now carries Rs 1-10 crore liability;
  - (c) a submission to the Nilekani task force, where V. Kamakoti (IIT Madras director) is a member, so an academic-pilot route is plausible but speculative.
- Incentive risk: insiders implicated in leaks may resist attribution tools.

### (f) Overnight wedge
- Demo by noon:
  - (1) A 90-question NEET-style Biology/Chemistry set built from public past papers, turned into 10 "insider" variants (paraphrase, numeric changes, option shuffles, two honey items per variant) and checked by the bio member.
  - (2) Leak attribution: a teammate hand-copies 15 questions from a random variant; phone photo, OCR, matcher, named source variant, with a confidence score.
  - (3) Beneficiary forensics: simulate 22,000 candidates with a 3-parameter IRT model, 1% given the leaked variant's answers; the detector flags them by leaked-subset accuracy gap plus honey-item hits.
  - (4) Optional: an ESP32 trunk logger or a Pi sniffer flagging an AnyDesk session on a LAN.
- Honest test result in ~14 h:
  - Top-1 attribution accuracy over ~20 handwritten leaks, and the minimum number of copied questions needed.
  - Precision and recall of beneficiary detection at a fixed false-positive rate (e.g. 1 per 10,000 honest candidates) on the synthetic cohort.
  - Both are synthetic; state that.
- Deep Tech Thesis: India's leaks are insider events upstream of printing, so visual per-copy codes and CBT cannot see them. Content canaries and honey items give attribution that survives handwriting, and response forensics gives the evidence needed to cancel narrowly instead of cancelling for 22 lakh people.

### (g) Verdict
- Real and very public: tier A, with a 2026 chargesheet showing insider leaks.
- Unsolved: partly. Visual per-copy codes, jammers, CCTV and biometrics are everywhere. Insider attribution and response forensics are not visible in India.
- Sellable: weakly. The market is small (~Rs 25-50 crore/yr TAM) and lumpy B2G, and the buyer is in political turmoil.
- Buildable overnight: yes, on synthetic data.

Scores: proof 5, market 2, feasibility 4, unsolved gap 3, deep-tech 4, risk 2.

Round 3 should check:
1. Whether NTA or any board already uses content variants or response forensics (the 2024 Supreme Court case analysis; RTI; ask a board).
2. The Nilekani task force's recommendations and timeline, and whether they open a forensics or "information security vertical" procurement.
3. Whether TCS iON, Eduquity or Coempt would license attribution/forensics or a centre sensor given amended-Act liability; get one conversation.

---

## Problem: U3 Women's commute safety: mandated panic buttons and VLTDs that do not work

### (a) Proof dossier
Independent items: 9 or more (state audits and news across five states, NCW and NGO surveys); social engagement is weak.
- https://www.deccanherald.com/india/karnataka/bengaluru/most-panic-button-alarms-turning-out-non-serious-3583605 — 13 Jun 2025 — (fetched via the page's article body)
  - "A vast majority of the 500-700 panic button alarms received every day in Bengaluru are non-genuine", triggered "mostly by students in school buses, curious cab passengers, and drivers testing the device".
  - "To date, only 17 alerts have been genuine. These mostly involve road rage incidents", plus a bus breakdown and an accident; 2-3 needed police.
  - 1,08,639 of ~6 lakh public service vehicles (≈18%) fitted; 500-600 fitted/day.
  - A 30-person, 24/7 command centre with 12 computers.
  - 12 government-approved device makers.
  - Cost: VLTD Rs 5,424 + Rs 325 per button + Rs 1,800/yr = Rs 8,199-11,124 per vehicle, against Rs 2,000-4,500 for market devices.
  - No compliance deadline; enforced at fitness renewal.
- https://www.indiatvnews.com/auto/maharashtra-orders-verification-of-non-functional-panic-button-systems-in-cabs-buses-taxis-2025-12-13-1021552 — 13 Dec 2025 — (fetched) Mumbai command centre received 6,30,255 alerts (period not stated); 1,40,599 vehicles fitted, 1,01,086 functional, so ~39,500 (28%) faulty (my arithmetic). Legislative Council deputy chair Neelam Gorhe ordered verification and said the impact "has not been as expected". Owner is called first and 112 only if there is no response. The device is mandatory for a fitness certificate.
- https://www.thenewsminute.com/karnataka/costly-but-useless-panic-buttons-on-bengaluru-cabs-and-buses-offer-little-safety — 21 Jul 2025 — (R1) pressing the BMTC button gave a beep only; owners report Rs 11,000-16,000 actual cost.
- https://telanganatoday.com/panic-buttons-in-delhi-buses-taxis-fail-to-serve-purpose-acb-audit-report — 1 Aug 2023 — (R1) Delhi ACB audit: 0 of 14 buses had working buttons; no alert ever reached 112 (not integrated). Delhi disputes the audit.
- https://www.freepressjournal.in/bhopal/bhopal-check-when-you-hop-in-cab-its-panic-button-may-be-dysfunctional — 5 Nov 2024 — (R1) ~53% of ~5,000 Bhopal vehicles dysfunctional.
- https://deccanherald.com/india/karnataka/mangaluru/panic-buttons-not-serving-their-purpose-4104095 — 2026 (date not shown) — (snippet) Mangaluru inspection: no KSRTC city bus had panic buttons. Also https://www.deccanherald.com/india/karnataka/bengaluru/panic-buttons-seldom-work-cab-drivers-in-bengaluru-flag-safety-lapses-3774566 (snippet): cab drivers say buttons seldom work.
- https://obeta.ttef.in/my-kolkata/news/panic-buttons-fail-to-evoke-fast-response-late-reaction-beats-the-purpose-say-vehicle-owners/cid/2012532 — undated — (snippet) Kolkata owners: no immediate police response.
- https://www.freepressjournal.in/amp/india/nari-2025-report-40-women-feel-unsafe-in-cities-only-one-in-3-report-harassment — 29 Aug 2025 — (fetched) NCW NARI 2025: 12,770 women, 31 cities. 40% feel "not so safe" or "unsafe"; public transport is 29% of harassment locations (neighbourhoods 38%); only 1 in 3 incidents reported; only 25% are confident authorities will act.
- Other surveys (snippets):
  - Greenpeace: 77% of women feel unsafe on Delhi buses at night (https://theprint.in/india/77-pc-women-feel-unsafe-on-delhi-buses-after-dark-greenpeace-report/2334499).
  - Jagori: 34% of Delhi domestic workers were sexually harassed while commuting and 61% did not report (https://www.thequint.com/jobs/delhi-domestic-workers-women-safety-toilets-public-infrastructure-transport-buses-jagori-data-latest-news).
  - Chennai AWARE: 50% of 1,400 respondents harassed on public transport (https://www.thenewsminute.com/amp/story/tamil-nadu/does-chennai-deserve-safe-women-tag-survey-public-transport-says-otherwise-65141, undated).
- YouTube engagement is weak. The top panic-button videos are compliance/vendor content (YouTube search page, 3 Nov 2026):
  - "2026 commercial Cars ke liye Panic Button ka Raj" (Sachin Car Review, aJTJZVXGck4) 11,216 views.
  - "VLTD/Panic Button Device for just ₹4500! With Parivahan Certificate" (C3VoMja_bPs) 11,168 views.
  - A Kannada cab owner's video (l-9xFDzHe1E) 7,339 views.
  - The public conversation is drivers complaining about cost, not passengers complaining about safety.
- Reddit (arctic-shift mirror, 3 Nov 2026):
  - r/india post titles containing "panic button" since Jan 2022: 1 post (https://www.reddit.com/r/india/comments/1nxyq26/, 4 Oct 2025, an app idea, score 1).
  - r/IndianWomen titles containing "cab" since Jan 2024: 0 posts.
  - The r/bangalore pull failed (rate limit).
  - No Reddit thread with real engagement on panic buttons was found, which matches the low YouTube numbers.
  - Cab-safety threads exist, but they are about ride-hail apps, not panic buttons. r/delhi titles containing "cab" since Jan 2025 include:
    - https://www.reddit.com/r/delhi/comments/1tjn9f4/ — 21 May 2026 — 196 upvotes, 47 comments — "My friend was sexually harassed in a Rapido cab, and Rapido's response was a sad emoji".
    - https://www.reddit.com/r/delhi/comments/1tkj0xa/ — 22 May 2026 — 44 upvotes, 11 comments — "Late-night cab from IGI: driver ignored the app route and tried to detour". This is the route-deviation case the confirmation node targets.
  - The complaint channel is the ride-hail app's SOS and support, not the state panic button.

Hard numbers: Bengaluru 500-700 alarms/day with 17 genuine to date (DH, Jun 2025); Mumbai 6,30,255 alerts and 28% of fitted devices faulty (India TV, Dec 2025); NCW NARI: 29% of harassment happens on public transport. NCRB transport-specific crime figures: NOT FOUND (NCRB does not split by commute; R1).

Final tier: B. The infrastructure failure is well documented in five states, but public social engagement is low, and the women's-safety concern behind it is proven by surveys rather than by the panic-button channel.

Key finding that changes the framing: the genuine alerts that do arrive are road rage, breakdowns and accidents, not women in distress (DH). So "triage" improves a channel that people in danger are not using; women use 112, ride-hail SOS and location-sharing instead.

Round 1 corrections:
- R1's "500-600 alerts a day, about 18 genuine" reads as ~18 per day. DH says 17 genuine in total to date, so the signal-to-noise ratio is far worse than R1 implied (one genuine alert per several thousand).
- R1's "4.11% of 6.04 lakh fitted in 2024" is out of date: ~40,000 by 31 Dec 2024 (ANI via https://www.tribuneindia.com/news/business/karnataka-govt-mandates-intelligent-transportation-system-ais-140-guidelines-on-public-vehicles-over-6-5-lakh-vehicles-to-be-fitted-with-panic-button, Jan 2025, snippet), then 1,08,639 (18%) by June 2025.
- R1's "Rs 1,405 crore Nirbhaya Fund, 32 cities" for VLTDs could not be verified in a primary source.

### (b) Market size
Affected units:
- Karnataka ~6-6.5 lakh public service vehicles (DH; ANI). Maharashtra 1.4 lakh fitted.
- National count of VLTD-mandated vehicles: NOT FOUND. The MoRTH VLT and Emergency Button Order 2018 mandates VLTDs for public service vehicles; fitness certificates are gated on fitment through VAHAN (https://www.casemine.com/act/in/5f5f11e29fca195c05cce7fe, snippet).
- Assumption: national ≈ 60-70 lakh public service vehicles (Karnataka × ~10, assuming Karnataka is ~10% of India's transport vehicles; unverified).

Existing mandated market (not ours):
- 65 lakh × Rs 5,424 = Rs 3,526 crore of hardware (one-time, my arithmetic) plus 65 lakh × Rs 1,800 = Rs 1,170 crore/yr in maintenance and connectivity (my arithmetic, at Karnataka's capped prices).
- A vendor guide puts AIS-140 devices at Rs 5,500-9,000 entry, Rs 10,000-18,000 with panic/I-O, Rs 14,000-25,000+ for school buses, and Rs 1,200-5,000/yr recurring (https://blog.fleetx.ai/blog-ais-140-gps-device-price-in-india-2026/, 9 Jun 2026, fetched; vendor blog).

Our layer:
- TAM:
  - (i) confirmation add-on: Rs 1,500 (assumption) × 65 lakh = Rs 975 crore one-time (my arithmetic);
  - (ii) command-centre triage software: 36 states/UTs × Rs 0.5-2 crore/yr (assumption) = Rs 18-72 crore/yr (my arithmetic).
- SAM:
  - Metro cabs, school buses and women-special buses ≈ 10% of the fleet = 6.5 lakh × Rs 1,500 = Rs 97.5 crore one-time plus Rs 300/yr = Rs 19.5 crore/yr (my arithmetic, assumptions).
  - Plus triage in ~5 states with live command centres (Karnataka, Maharashtra, Himachal Pradesh, Tamil Nadu, Nagaland) × Rs 1 crore ≈ Rs 5 crore/yr.
  - Total ≈ Rs 25 crore/yr recurring.

Who pays today:
- Vehicle owners pay for devices (Rs 8,199-11,124 in Karnataka; drivers report Rs 12-16k).
- States pay for command centres, partly from the Nirbhaya Fund:
  - Fund utilisation overall ~74% (Dec 2024 reply, https://theprint.in/india/74-of-nirbhaya-funds-allocated-amount-utilised-wcd-ministry/2402521, snippet).
  - MHA's ERSS line is ~Rs 364 crore released/utilised (https://rsdebate.nic.in/bitstream/123456789/753131/1/PQ_266_18122024_U2713_p481_p488.pdf, RS 18 Dec 2024, snippet).
  - 18 states had not used ERSS funds (https://gulfnews.com/world/asia/india/government-concerned-over-poor-utilisation-of-nirbhaya-fund-1.68229569, snippet, older).
  - MoRTH asked states in Jan 2020 to apply for Nirbhaya money for VLT monitoring centres linked to ERSS-112 (https://www.dtnext.in/tamilnadu/2020/01/17/for-women-safety-use-nirbhaya-fund-for-vehicle-tracking-system, snippet).
  - MoRTH VLTD disbursement and utilisation: NOT FOUND.

Buyers: state transport departments (state), VLTD makers (firms, OEM licence), cab aggregators and school-bus or corporate night-shift operators (firms).

No published market figure for VLTD/panic-button systems was found.

### (c) Competitive map
| Player | What it does | Status | Gap |
|---|---|---|---|
| AIS-140 VLTD makers | GPS + panic button + dual SIM to the state command centre | 12 approved makers in Karnataka (DH); Andaman empanelled 16 firms (https://andamansheekha.com/?p=92556, snippet). Names such as iTriangle/Roadcast NOT VERIFIED this round | Binary button; no context, no confirmation; 18-28% of fitted units faulty in audits |
| State command centres | Karnataka (Shanthinagar, 30 staff) and Maharashtra (Mumbai) call the owner, then 112. Himachal Pradesh built its centre with C-DAC, integrated with ERSS-112 (https://roadsafety.hp.gov.in/scheme-reports, snippet). Nagaland Nirbhaya VLTS centre May 2024 (https://www.morungexpress.com/nirbhaya-vlts-command-control-centre-launched-in-nagaland, snippet). Tamil Nadu tendered devices with command-centre integration (https://www.thenewsminute.com/amp/story/tamil-nadu/tn-transport-dept-seeks-bids-for-vehicle-tracking-device-installation, snippet; IRT tender 1902/VLTD/CP/IRT/2026, bids closed 15 Apr 2026, https://www.publicservicesmap.in/tenders/supply-installation-activation-and-integration-o--tn-2026-irt-673657-1, snippet) | Alive, state-run | Manual call-back; no ranking; Delhi not integrated with 112 (ACB) |
| Chennai MTC "AI-enabled" panic system | 4 panic buttons + 3 cameras + an AI mobile network video recorder per bus; pressing records video and alarms a cloud control centre linked to police; 500 buses in phase 1 of ~2,500, Nirbhaya Safe City | Launched May 2022 (https://www.freepressjournal.in/amp/india/chennai-cm-mk-stalin-launches-ai-enabled-panic-button-cctv-surveillance-in-500-buses, fetched) | Closest to "confirmation" (video on press), but the AI is for missing persons and criminal ID; no audio or distress classification described |
| Uber India | In-app audio recording (riders and drivers), SOS linked to the Maharashtra Police control room, women-rider preference, RideCheck | Launched Nov 2024 (https://www.deccanherald.com/business/companies/ubers-new-safety-feature-allows-riders-to-record-audio-choose-women-rider-preference-option-3294708, snippet) | Phone-based, Uber trips only; audio reviewed only after a safety report. Ola: SOS to its own team, no audio recording (https://techcrunch.com/?p=1931058, snippet, older) |
| Safetipin | Safety audits/scores of public spaces and apps since 2013 | Alive; revenue ~US$348k in FY22 (aggregator, https://www.thecompanycheck.com/company/b/safetipin/084cccaond0a149kv, snippet); 2025 World Summit Award | Not in-vehicle; no alert handling |
| Consumer wearables | Leaf "Safer" (apparently discontinued; R1); Shark Tank wearable (R1) | Poor survival record | Need the user to trigger; no confirmation |
| International | Noonlight (US) | NOT SEARCHED | — |

Q4, technical (audio/motion models):
- No published precision/recall for scream detection on a microcontroller was found.
- Nearest evidence:
  - YAMNet distilled into an 80,713-parameter DS-CNN, 110 KB INT8, running on an ESP32-S3 at 28 ms per inference vs 508 ms for full YAMNet (baby-cry target; screaming used as a hard negative; test set only 62 segments) (https://huggingface.co/chayuto/yamnet-cry-distill-int8, snippet).
  - A student TinyML "help/scream" detector on two Arduinos at ~90.5% accuracy (https://z4ziad.github.io/pdf/fall_24/saishubasai_LATE_111164_12109709_18848_Project__Elderly_Care-2.pdf, snippet).
  - A CNN on an STM32F746 at ~97% on labelled audio, not scream-specific (https://elib.vku.udn.vn/handle/123456789/2703, snippet).
  - MSc thesis comparing SVM/MLP/ResNet-34 for screams with precision/recall/F1 and noise robustness (https://norma.ncirl.ie/8779/, snippet).
  - arXiv 2411.03016 (Nov 2024) scream detection for construction sites: no numbers in the abstract (fetched).
- So on-device feasibility is shown; accuracy in a noisy Indian bus or cab is unknown.
- Public data: AudioSet has a "Screaming" class (background); Hindi distress-word data must be recorded.

Gap: (1) context-confirmed alerts (audio + motion + route) at the edge; (2) ranked triage for command centres. The deeper gap is that women in danger do not use the channel at all, and nobody has fixed that.

### (d) Solution approaches
1. Command-centre triage software. Pick this as the business.
   - A ranking model over the existing VLTD alert stream: vehicle class (school bus vs cab), time and place, repeat-press patterns (testing, children), speed or route anomaly from GPS, device-health flags, and owner call-back outcomes.
   - Output: a ranked queue plus auto-close of likely tests, which cuts operator load. Deep-tech core: weakly supervised learning on noisy logs and anomaly detection on GPS tracks.
   - First customer: Karnataka or Maharashtra transport department (they have the noisy stream).
   - Price: Rs 0.5-2 crore/yr per state (assumption). Moat: labelled alert-outcome data.
2. In-vehicle confirmation node. The hardware variant, best for the demo.
   - ESP32-S3 + I2S MEMS mic + IMU (+ GNSS, or taps the VLTD's NMEA). On-device detection of screams and Hindi/Kannada distress words, harsh braking or struggle motion, and geofence/route deviation. When the button is pressed it attaches a confidence score and a 10-second encrypted context packet; it can also escalate without a press when signals are strong (opt-in).
   - Sold as a licensed module or firmware to the 12 approved VLTD makers.
   - BOM ~Rs 800-1,200 (assumption); sell at ~Rs 1,500.
3. Passenger-side BLE pairing. A phone app detects the vehicle's VLTD beacon and gives a discreet trigger plus audio confirmation that reaches the same command centre. Crowded (Uber SOS, 112 India app) and needs installs.

Why: 1 needs no new hardware in a mandated fleet and has a clear B2G owner. Show 2 to use the hardware skill and to feed better features into 1. Be honest in the thesis that the false-alarm problem is mostly children and testing, which software can rank out.

### (e) Regulatory and safety gates
- AIS-140 type approval (ARAI/ICAT) and state empanelment: an add-on that changes the VLTD needs re-certification by the maker. Licensing to makers avoids becoming a device maker.
- MoRTH VLT Order 2018: centres must feed VAHAN and states.
- DPDP Act/Rules (notified 14 Nov 2025, phased to ~May 2027): in-cab audio from passengers needs notice and consent (signage), purpose limitation, no continuous recording, and retention limits. Design it as always-listening-never-storing, keeping a rolling buffer only on a press.
- WPC approval for any radio.
- Blocks the overnight demo: none.
- Blocks the business: re-certification, state procurement, and DPDP consent design for audio.

### (f) Overnight wedge
- Demo by noon:
  - An ESP32-S3 node (I2S mic + MPU6050 + optional GPS) running a TFLite-Micro classifier for scream, Hindi distress words ("bachao", "gaadi roko", "help") and harsh motion, and sending a confirmed alert over Wi-Fi/MQTT to a dashboard.
  - The dashboard replays a simulated day of 600 alerts with the Bengaluru base rate (a handful genuine) plus synthetic test and child presses, and shows the triage ranking.
- Training data: AudioSet/Freesound screams plus 30-60 min of team-recorded Hindi distress phrases, mixed with recorded traffic, horn and bus noise.
- Honest test result in ~14 h:
  - (1) Recall on ~50 staged screams/phrases played in a car or room, and false triggers per hour on 1-2 hours of recorded road and bus noise.
  - (2) On-device latency in ms.
  - (3) Precision@10 of the triage ranker on the simulated alert stream (synthetic; say so).
- Deep Tech Thesis: mandated panic buttons in India generate hundreds of alerts a day with almost no genuine signal and a dead loop to 112. Context sensing at the edge and learned triage at the centre turn a binary press into a ranked, confirmable event, without new mandates.

### (g) Verdict
- Real: as an infrastructure failure, yes. Audits and official counts from Karnataka, Maharashtra, Delhi and Bhopal agree.
- The women's-safety framing is not supported by the alert data (the genuine alerts are road rage and accidents), and public social engagement is low.
- Unsolved: yes; no triage or confirmation product was found.
- Sellable: to states via slow procurement, or to VLTD makers via licence; Rs 25 crore/yr realistic SAM.
- Buildable overnight: yes.

Scores: proof 3, market 3, feasibility 4, unsolved gap 4, deep-tech 4, risk 2.

Round 3 should check:
1. Alert logs from the Karnataka and Maharashtra command centres (RTI or interview): composition of false alerts, and whether any women-distress alert ever arrived.
2. The national VLTD fitment count (VAHAN/MoRTH) and how many states run live command centres.
3. Whether 2-3 of the 12 Karnataka-approved VLTD makers would license a confirmation module, and what AIS-140 re-certification costs.

---

## NOT SEARCHED
- F1:
  - I4C modus-operandi split for digital arrest (phone call vs WhatsApp/Skype video).
  - Actual amounts returned to victims (vs "saved"); bank appetite or pilots for senior-customer protection.
  - Truecaller India subscriber numbers and Premium price.
  - Elderly smartphone ownership from a primary survey (NSSO/NFHS).
  - A primary text of Android's CAPTURE_AUDIO_OUTPUT / concurrent-capture rules.
- D1:
  - NTA's TCS iON and print-vendor contract values.
  - Indian online-proctoring firms (Mercer-Mettl, Eklavvya) and their funding.
  - Caveon/ETS pricing.
  - Nilekani task force report status.
  - JEE Main and CUET candidate counts.
  - Whether any Indian exam body uses content variants or response forensics.
- U3:
  - National VLTD-mandated vehicle count.
  - VLTD maker names and market shares (iTriangle, Roadcast and others).
  - Alert-volume data from Telangana, Kerala and Delhi command centres.
  - Noonlight and other international triage products.
  - NCRB transport-specific figures beyond R1.
  - DPDP guidance specific to in-vehicle audio.
  - Corporate night-shift transport rules for women employees as a buyer.

Searches used: 40
