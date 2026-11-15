# S1-06 Funded startups and frontier-lab health AI (agent: claude-sonnet-5-5, 2026-11-13)

## Digest
(pending)

## Findings

### A. Y Combinator companies, batches 2023-2026 (source: yc-oss API, OPENED 13 Nov 2026)
Source for every row: https://yc-oss.github.io/api/industries/healthcare.json (also /industries/healthcare-it, healthcare-services, medical-devices, diagnostics, consumer-health-and-wellness, therapeutics, and /tags/digital-health, health-tech, telehealth). Company page = https://www.ycombinator.com/companies/<slug>. Status is as the API lists it on 13 Nov 2026. Descriptions are the company's own YC text (THEIR CLAIM). Of ~226 healthcare-industry companies in 2023-2026 batches, most are admin/RCM/scribe/drug-discovery; the chronic-care and wearable-data ones are below. No YC company in these files was a dedicated remote-BP, kidney, COPD-device or hypertension-titration company (NOT FOUND in the API files; the "Winter 2026" and later batches are as listed by the API, which I did not cross-check on ycombinator.com).

| Company | Batch | Status | One line (YC text) | Site | Adapt. depth (INFERENCE from text) |
|---|---|---|---|---|---|
| Empirical Health | S23 | Active | AI-native heart health: 100+ biomarker lab test, lifetime risk model, plan to lower it; team 4 | empirical.health | 3 |
| LifestyleRx | S23 | Active | Insurance-covered virtual care for Type 2 diabetes reversal; doctors guide lifestyle change; team 9 | lifestylerx.io | 2-3 |
| Kivo Health | W23 | Active | AI-powered virtual care for seniors with chronic disease, starting with lung care; says raised $10M Series A; works with Stanford, UCLA, Optum Health | kivohealth.com | 3 |
| Stellar Sleep | S23 | Active | Psychology-based care for chronic insomnia (CBT-I type) | stellarsleep.com | 2 |
| Elythea | S23 | Active | ML to predict obstetric complications (preeclampsia, PPH, preterm labor) | elythea.org | 1 |
| Aidy | W24 | Active | Mobile app for chronic conditions, starting with IBD; logs symptoms, diet, treatment; pattern finding; team 2 | aidyhq.com | 3 |
| Copper Health | W24 | Active | Remote therapeutic monitoring (RTM) platform for physical therapy, AI-powered | copperhealth.co | 2 |
| GloGlo | W24 | Active | "Curing and preventing type 1 diabetes" (tag file only; not a care-loop product) | NOT OPENED | n/a |
| Selera Medical | W24 | Inactive | Minimally invasive device to offload fluid in heart failure | seleramedical.com | n/a (device) |
| Mito Health | S24 | Active | $9/month membership; labs, scans, home kits, Rx at cost | mitohealth.com | 1 |
| Amby Health | W25 | Active | "Your wearable tells you what happened. Amby texts you what to do next, checks in, and adjusts" | tryamby.com | 3 |
| Galen AI | S25 | Acquired | Personal AI companion linking medical records (800+ institutions) and 20+ wearables incl. Dexcom | galenai.com | 1-3 |
| Lucis | S25 | Active | "Function Health for Europe": blood tests plus AI insight | lucis.life | 1 |
| Nori | F25 | Active | AI health coach; Apple Health, records, wearables to a daily plan | nori.ai | 3 |
| Prana | W26 | Active | AI primary-care doctor; watches records and wearables for "clinical drift"; "full-stack medical provider" | pranadoc.com | 3 |
| Clara | S26 | Active | AI primary care and longevity practice from Circle Medical founders; sees user's medical data | askclara.com | 3 |
| Juno | S26 | Active | AI health assistant for chronic illness; says 300,000+ patients since October launch (THEIR CLAIM) | junocompanion.com | 2-3 |
| Illume Labs | S26 | Active | 24/7 health and longevity companion fusing wearables, blood panels, genome; daily texts | illumelabs.ai | 3 |
| Helios Intelligence | F26 | Active | At-home test, 1,000+ biomarkers from a drop of blood; longitudinal model | heliosinc.ai | 1 |
| STASIS | F26 | Active | "The WHOOP for 16 billion eyes" (eye wearable; tag file only, not read) | get-stasis.com | 1 |
| Lumeria | S26 | Active | Phone-clip multispectral skin camera ("Oura Ring for Skin") | lumeria.com | 2-3 |
| RonanRx | S26 | Active | Personalised peptides and GLP-1s, "full stack pharmaceutical company" | ronanrx.com | 4? (compounded dosing; not read) |
| Sonia | W24 | Active | Voice AI mental-health support by MIT/ETH researchers | soniahealth.com | 2 |
| Allia Health, Sunflower (addiction telemedicine), Perspectives Health (behavioural programme admin), Understood Care (Medicare patient advocates), Haplotype Labs (genetic risk SaaS), Kaigo Health (AI outpatient care workforce, F25), Beacon Health (AI employees for primary care, W26), FutureClinic (F24 "personal doctors through chat") | various | Active | adjacent; not chronic-loop products | see API | 1-2 |

### B. Venture rounds (draft, appended as found; OPENED = page read, SNIPPET = search summary only)
| Company | Round, date, amount | Lead (others) | What it does | Depth | Traction (THEIR CLAIM) | Source / status |
|---|---|---|---|---|---|---|
| Function Health | Series B, 19 Nov 2025, $298M, $2.5B valuation (one outlet says $2.8B) | Redpoint Ventures; a16z reported as participant (a16z Bio+Health led the earlier $53M Series A) | Lab testing plus AI "medical intelligence" for 100+ biomarkers | 1-2 | not captured | SNIPPET https://www.fiercehealthcare.com/health-tech/function-health-lands-298m-series-b-rolls-out-medical-intelligence-ai-model-health-data ; https://www.cooley.com/news/coverage/2025/2025-11-19-function-health-secures-$298-million-series-b . a16z = participant only |
| Hippocratic AI | Series C, 3 Nov 2025, $126M at $3.5B; total $404M (company figure) | Avenir Growth (CapitalG, General Catalyst, Kleiner Perkins participating/existing; Series B Jan 2025 $141M at $1.64B) | Safety-focused generative AI agents that call patients (chronic care follow-up, discharge) | 2-3 | not captured | SNIPPET https://hippocraticai.com/?p=9108 ; https://siliconangle.com/2025/11/03/hippocratic-ais-valuation-soars-3-5b-raising-126m-new-funding/ . GC participated (existing) |
| Superpower | Series A, Apr 2025, $30M, >$300M post | Forerunner Ventures (Day One, Susa) | Consumer longevity: labs, plan, supplements, membership | 1-2 | 2026 items: Forbes AU Apr 2026 says >A$65M raised, $432M valuation; Function Health sued Superpower 26 Jan 2026 (per search summary) | SNIPPET https://www.smartcompany.com.au/startupsmart/aussie-founded-superpower-raises-47-million-help-live-longer/ . Lead "Series A 2026" was WRONG: round is 2025 |
| Marley Medical (lead) | Seed Oct 2021, ~$9M total over 2 rounds | CRV; Rock Health also listed | Hypertension management | 3? | none | SNIPPET https://app.dealroom.co/companies/marley_medical . NO 2024-2026 round found; a16z/GC lead NOT confirmed. Lead mostly wrong |
| Doctronic | Series A $20M (Sep 2025); Series B $40M, 24 Mar 2026 | Abstract and Lightspeed co-led (USV, Seven Stars, Mantis, Tusk) | Consumer AI doctor; says first AI to legally renew prescriptions in US (Utah pilot, per headline) | 4 (Rx renewal by AI) | "15x growth, 300,000+ weekly users in under a year" THEIR CLAIM | SNIPPET https://www.vcaonline.com/news/2026032402/doctronic-raises-40m-series-b-following-breakthrough-as-first-ai-to-legally-renew-prescriptions-in-the-u-s-/ ; https://www.businesswire.com/news/home/20260324814372/en |
| Counsel Health | Series A $25M, 16 Oct 2025 (seed $11M led by a16z 2024) | a16z and GV | Physician-supervised AI care platform | 2-3 | not captured | SNIPPET https://hitconsultant.net/2025/10/16/counsel-health-raises-25m-to-launch-physician-supervised-ai-care-platform |
| Fay | $25M seed + Series A, date not confirmed (2025?) | seed General Catalyst; Series A Forerunner | Dietitian network, insurance billing | 2 | n/a | SNIPPET (search summary); date NOT CONFIRMED |
| Nourish | $100M, 2026 (week of ~May 2026) | Menlo Ventures | Virtual nutrition-focused metabolic care | 2 | n/a | OPENED https://media.startuphealth.com/p/9amhealth-s-26m-series-b-expands-a-proven-cardiometabolic-model-startup-health-insights-week-of-may |
| 9amHealth | Series B $26M, week of 19 May 2026 | Define Ventures (SemperVirens, Catalio, NewHealth) | Virtual diabetes/cardiometabolic clinic, AI-enabled workflows, endocrinologists, clinical pharmacists | 3-4 | ">$50M projected savings across two Fortune 100 employers" THEIR CLAIM | OPENED same URL |
| Chamber | Series A $60M, 4 Feb 2026 | Frist Cressey Ventures (existing: General Catalyst, AlleyCorp; Optum Ventures) | Cardiology data platform flags high-risk patients and gaps in guideline-directed therapy | 3 (clinician decision support) | 500+ cardiologists, 7 states THEIR CLAIM | OPENED https://pulse2.com/chamber-60-million-series-a-raised-for-cardiology-value-based-care-platform |
| Vital Signals | >$15M, 20 May 2026 | XYZ Ventures (no others named) | Consumer BP technology; claims "breakthrough" (unspecified) | 1 | none given | OPENED https://pulse2.com/vital-signals-15-million-raised-to-transform-blood-pressure-management/ |
| Knownwell | Series B ~$25-26M, Oct 2025 | lead unclear; a16z, Flare, Flybridge, CVS Health Ventures listed | Obesity care, AI-enabled, Needham MA | 3 | n/a | SNIPPET https://startupintros.com/news/2025-10-01-knownwell-series-b . a16z participation only possible |
| Signos | $20M, May 2026 | no lead named (GV, Dexcom, BCBS Alabama) | CGM plus app for weight loss | 3 | n/a | SNIPPET https://finance.yahoo.com/sectors/healthcare/articles/signos-raises-20m-expands-dexcom-134415440.html |
| Junction (ex-Vital) | Series A $18M, 11 Mar 2025 | Creandum (YC, Point Nine, Amino, Inflect) | One API to 500+ wearables and labs | 1 (infrastructure) | 500k lab tests/yr, 2M devices THEIR CLAIM | SNIPPET https://techcrunch.com/2025/03/11/junction-an-api-to-link-health-wearables-with-labs-raises-18m ; no Series B found |
| Twin Health | Series E $53M 2025 (Maj Invest), valuation $950M; aggregators claim Series F ~$61.5M 29 Jun 2026 at ~$1.4B | undisclosed | Metabolic digital twin: CGM + wearable + AI, adjusts diet and medicines with clinicians | 4 | Aggregator: 84% T2D remission at 6 months in interim Garmin study, NOT peer reviewed | SNIPPET https://www.massdevice.com/twin-health-raises-53m-digital-twin-diabetes/ ; 2026 round UNCONFIRMED |
| Virta Health | 2026 round UNCONFIRMED (aggregator) | n/a | T2D reversal by diet plus medication deprescribing | 4 | n/a | SNIPPET https://www.caplight.com/company/virta-health |
| Oura | Series E, Oct 2025, >$900M at ~$11B | Fidelity (ICONIQ, Whale Rock, Atreides) | Smart ring | 1-2 | CEO projects ~$2B 2026 sales (profile) | SNIPPET https://www.fiercehealthcare.com/health-tech/oura-raises-900m-series-e-oura-ring-sales-catapult |
| Ultrahuman | 2026 funding NOT FOUND | | | | | |


## NOT FOUND / NOT SEARCHED

Searches used: 9 so far
