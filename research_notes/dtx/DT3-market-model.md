# DT3 market model: home blood-pressure step loop (output of tools/dtx_market_model.py)

All figures are OUR ARITHMETIC from the inputs listed at the end. Rupees a year. Price: ₹149 a patient a month, ₹1,788 a year (ASSUMPTION).

## Result

| Level | Top-down | Bottom-up | Used (the lower) |
|---|---|---|---|
| TAM: every Indian adult on blood-pressure medicines who could be served | ₹7,494 crore (419.1 lakh private retail patients) | ₹9,969 crore (557.5 lakh treated adults, low case) | **₹7,494 crore** |
| SAM: private patients a doctor could enrol on a household smartphone | ₹1,668 crore (93.3 lakh patients through 3.1 lakh doctors) | ₹749 crore (41.9 lakh patients) | **₹749 crore** |
| SOM year 3 | ₹3.7 crore (0.5% of SAM) | ₹2.1 crore (60 clinics x 200 patients) | **₹2.1 crore** |
| SOM year 5 | ₹22.5 crore (3% of SAM) | ₹17.9 crore (400 clinics x 250 patients) | **₹17.9 crore** |

## How each figure is counted

- **TAM top-down.** Retail blood-pressure medicine sales ₹16,371 crore divided by a private patient's yearly medicine spend ₹3,906 = 419.1 lakh patients buying in the private market. Times ₹1,788 a year = ₹7,494 crore. The spend figure is a modelled price for one brand pill a day; across the paper's range of about ₹2,500 to ₹5,100 the count runs from 321.0 lakh to 654.8 lakh patients.
- **TAM bottom-up.** 315 million adults with high blood pressure x 17.7% on medicines = 557.5 lakh (the ceiling from drug sales, 30.7%, would give 967.0 lakh). Times ₹1,788 = ₹9,969 crore.
- **SAM bottom-up.** 419.1 lakh private patients x 50% reachable on a household smartphone x 20% whose doctor could enrol them = 41.9 lakh patients. Times ₹1,788 = ₹749 crore.
- **SAM top-down.** 13,88,185 registered doctors x 80% in practice x 70% private x 40% managing blood pressure = 3.1 lakh doctors, x 30 patients each = 93.3 lakh patients. Times ₹1,788 = ₹1,668 crore.
- **SOM bottom-up.** Clinics live and paying patients per clinic at each year end (the first year is an unpaid pilot):

| Year | Clinics | Patients per clinic | Paying patients | Revenue a year |
|---|---|---|---|---|
| 1 | 2 | 0 | 0 | pilot, unpaid |
| 2 | 15 | 150 | 2,250 | ₹0.4 crore |
| 3 | 60 | 200 | 12,000 | ₹2.1 crore |
| 4 | 180 | 220 | 39,600 | ₹7.1 crore |
| 5 | 400 | 250 | 1,00,000 | ₹17.9 crore |

## The US$100 million-a-year test

- US$100 million a year = ₹942 crore at ₹94.25 to the dollar.
- At ₹1,788 a patient a year that needs 52.7 lakh paying patients (52,71,253).
- The serviceable market above holds 41.9 lakh patients. **The test fails on this model in India alone**: it needs 1.3 times the SAM.
- Where the rest would have to come from: more protocols on the same loop (diabetes, heart failure), a paid public tier, other countries that use the same family of protocols, or a higher price paid by an insurer, employer or medicine maker.

## Price sensitivity

| Price a month | SAM used | SOM year 5 (bottom-up) | Patients needed for US$100 million |
|---|---|---|---|
| ₹99 | ₹498 crore | ₹11.9 crore | 79.3 lakh |
| ₹149 | ₹749 crore | ₹17.9 crore | 52.7 lakh |
| ₹299 | ₹1,504 crore | ₹35.9 crore | 26.3 lakh |

## A public tier, shown apart

- 420.1 lakh patients on treatment in the public programme x ₹15 a month x 12 = ₹756 crore a year. A state would pay this only for results, since the medicines themselves cost about ₹200 a patient a year.

## Inputs

| Input | Value | Source or tag |
|---|---|---|
| Price per active patient a month (from the build plan, D2-01) | 149 | ASSUMPTION |
| Adults with high blood pressure in India | 315.00 million | D1-03-F02, corrected by D3-02: a 2021 projection by the survey's investigators, not a count |
| Share of them on medicines | 17.7% | D1-03-F07 as checked by D3-02 (NFHS-5 2019-21, preprint) |
| Share receiving blood-pressure drugs daily, ceiling from drug sales | 30.7% | D2-05-F30 as checked by D3-02 (a 2018 ceiling that assumes the public sector gives 30% of treatment) |
| Hypertension patients on treatment in the public programme, March 2025 | 42.01 million | D1-03-F14 (search summary only) |
| Retail sales of blood-pressure medicines, year to December 2025, rupees | ₹16,371 crore | D2-05-F01 |
| What a private patient spends on these medicines a year, rupees | 3,906 | D2-05-F17 as checked by D3-02 (modelled price of one brand pill a day, 2019-20; the paper's range is about Rs 2,500 to Rs 5,100) |
| Share of private patients reachable on a smartphone | 50.0% | ASSUMPTION, in line with smartphone access of 57.9% at ages 50-59 and 44.7% at 60-69 (D3-07-F11, quoted second-hand) |
| Share whose doctor or clinic could enrol them in a programme in the next 5 years | 20.0% | ASSUMPTION |
| Registered allopathic doctors | 1.39 million | D2-05-F38 as checked by D3-02 (reply to Parliament, December 2025) |
| Share of registered doctors in practice | 80.0% | D2-05-F38 (the ministry's availability assumption, made for allopathic and AYUSH doctors together) |
| Share of practising doctors in private practice | 70.0% | ASSUMPTION; 66.3% of outpatient diabetes care is private (D3-07-F01) |
| Share of those who manage blood pressure as general or internal-medicine doctors | 40.0% | ASSUMPTION |
| Patients a doctor enrols in the programme | 30 | ASSUMPTION |
| Price per patient a month a state might pay | 15 | ASSUMPTION (public drug cost is about Rs 200 a patient a year, D2-05-F18) |
| Rupees per US dollar | 94 | D2-05 Digest item 10 (rate on 13 Nov 2026) |
| Top-down share of SAM in year 3 | 0.5% | ASSUMPTION |
| Top-down share of SAM in year 5 | 3.0% | ASSUMPTION |
| Clinics and patients per clinic by year | see the table above | ASSUMPTION |

What this model leaves out: patients treated in the public system (shown apart), diabetes and other conditions, device sales, and any country outside India. No measured split of public and private treatment was found (D2-05-F30), which is why the private count is derived from medicine sales.
