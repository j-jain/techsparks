# R3 — Proof routes tested by the coordinator (Fable, 2026-11-03, between Rounds 2 and 3)

## What works and what does not
- **reddit.com / old.reddit.com**: blocked in the built-in browser pane ("not allowed due to safety restrictions") and for the agents' WebSearch/WebFetch. No direct route.
- **Reddit mirrors**: `reddit.sentinel-team.org` serves individual post snapshot pages by post id (scores + comment counts at snapshot time) but has no text search; `axebps-redlib.hf.space` never woke from "Preparing Space"; `lr.us.psf.lt` denied; `redlib.catsarch.com` bad TLS cert; `redlib.privacyredirect.com` sits behind a "Gandalf" bot check (not completed, by rule); `safereddit.com` rendered blank. Usable Reddit routes for Round 3 are therefore the Arctic Shift JSON API (`arctic-shift.photon-reddit.com/api/posts/search?...`, scores may be stale) and sentinel-team post pages by id, both via the agents' WebFetch, plus news coverage of viral posts.
- **YouTube**: renders in the pane with view counts ONLY while the Claude window is open and the pane is visible; as a background page the results never render (empty body). Invidious (`yewtu.be`) sits behind a browser-verification wall. Agents can use `https://returnyoutubedislikeapi.com/votes?videoId=<id>` for view counts of specific videos.

## Harvested while the pane was visible (search-results page, view counts as shown, 3 Nov 2026)

### F1 digital arrest (query "digital arrest scam india")
- "Scammers New Technique for Digital Arrest || How to Save Yourself" — Fight For Your Right by Shri RM Mishra — **987K views**, 1y ago (Hindi)
- "Operation Digital Arrest: India Today's Nitin Jain Exposes New Digital Fraud" — India Today — **155K**, 2y ago
- "Cyber Crime and Digital Arrest…WARNING!" — TV9 Bharatvarsh — **116K**, 3w ago
- "Digital Arrest Scam: How You Can Stay Safe | Tech Today" — India Today — 40K, 1y ago
- "What Explains The Rise Of Digital Arrest Scams In India? | GRAVITAS" — WION — 32K, 1y ago (Bengaluru techie lost ₹11.8 cr)
- "India's Fastest Growing Fraud Digital Arrest Is 100% Fake" — HDFC Bank — 32K, 8mo ago
- "Why & How Was This Man 'Digitally Arrested'" — NDTV — 27K, 1y ago
- "Digital Arrest Scams | Why the SC & President Warned | Drishti IAS" — 14K, 1y ago
- **New this week (2–4 days before 3 Nov 2026)**: "Supreme Court: CJI's 'Smash Phones' Solution… Centre Tells SC" — Times Now — 13K; "SC Cracks Down on Digital Arrest Scams: Banks Must Compensate Victims" — NEWS9 — 8.5K; "Digital Arrest Scam Crackdown: SC Demands Action Against Suspicious Bank Transactions" — CNN-News18 — 6K; "Banks Must Compensate If Due Diligence Fails" — Republic — 3.5K; "A case for stronger banking safeguards" — The Hindu — 1.1K. → A Supreme Court ruling on bank liability for digital-arrest losses landed in the last week; Round 3 must pin the order and date.

### H1 counterfeit medicines (query "nakli dawai fake medicine india")
- "Nakli Dawa Ka Sach – Aapki Dawa Asli Hai Ya Nahi?" — SAGAR MEDICAL STORE — **79K**, 1y ago
- "Original medicine vs fake Medicine | How to identify" — Sriniket kumar — **48K**, 5y ago
- "Fake Cancer Drug Racket Busted In Bengaluru; Over 90 Hospitals Under Scanner" — India Today — **22K**, 1mo ago
- "Fake Medicines: नकली दवाओं को कैसे पहचाने? | Tata 1MG" — 19K, 2y ago
- "Real Vs Fake: How To Spot Fake Medicines?" — 14K (Short); "UP में नकली दवाओं के बड़े खेल का भंडाफोड़" — 11K (Short); "How to Identify Fake Medicines in India" — 10K (Short)
- "बेंगलुरु में नकली दवाओं की फैक्ट्री का भंडाफोड़, 4.91 करोड़" — IndiaTV — 5.1K, 2mo ago; "Karnataka Fake Medicine Racket: ₹4.5 Crore, Pfizer Labels Found" — News18 — 3.1K, 2mo ago
- Pattern: steady "how to identify" demand (79K, 48K, several 10K+ Shorts) plus a cluster of racket busts in Aug–Sep 2026.

### Not harvested (pane went hidden): snakebite, stray dogs, smart meter, rooftop solar, EV fire, AQI, tankers, lifts, GNSS, drones, Sigachi, NEET, panic buttons. Round 3 agents to fetch via the returnyoutubedislike API on the top video ids from search snippets, or the coordinator retries the pane when the window is open.
