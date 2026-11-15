"""Market size for the home blood-pressure step loop, counted two ways at each level.

Usage:  python dtx_market_model.py [out.md]

Method (the same as the FloorSe mid-sem model): TAM, SAM and SOM are each counted top-down
and bottom-up, the LOWER figure is used, and the US$100 million-a-year test is stated even
when it fails. Every input carries its fact ID or the tag ASSUMPTION. Change an input here
and rerun; the document's table must match this script's output.
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CRORE = 1e7
LAKH = 1e5

# ---------------- inputs ----------------
I = {
    "price_month":        (149,        "ASSUMPTION", "Price per active patient a month (from the build plan, D2-01)"),
    "adults_htn":         (315e6,      "D1-03-F02, corrected by D3-02: a 2021 projection by the survey's investigators, not a count", "Adults with high blood pressure in India"),
    "treated_share_low":  (0.177,      "D1-03-F07 as checked by D3-02 (NFHS-5 2019-21, preprint)", "Share of them on medicines"),
    "treated_share_high": (0.307,      "D2-05-F30 as checked by D3-02 (a 2018 ceiling that assumes the public sector gives 30% of treatment)", "Share receiving blood-pressure drugs daily, ceiling from drug sales"),
    "public_on_treatment": (42.01e6,   "D1-03-F14 (search summary only)", "Hypertension patients on treatment in the public programme, March 2025"),
    "retail_bp_market":   (16371 * CRORE, "D2-05-F01", "Retail sales of blood-pressure medicines, year to December 2025, rupees"),
    "private_drug_year":  (3906,       "D2-05-F17 as checked by D3-02 (modelled price of one brand pill a day, 2019-20; the paper's range is about Rs 2,500 to Rs 5,100)", "What a private patient spends on these medicines a year, rupees"),
    "phone_share":        (0.50,       "ASSUMPTION, in line with smartphone access of 57.9% at ages 50-59 and 44.7% at 60-69 (D3-07-F11, quoted second-hand)", "Share of private patients reachable on a smartphone"),
    "organised_share":    (0.20,       "ASSUMPTION", "Share whose doctor or clinic could enrol them in a programme in the next 5 years"),
    "doctors":            (1388185,    "D2-05-F38 as checked by D3-02 (reply to Parliament, December 2025)", "Registered allopathic doctors"),
    "doctors_active":     (0.80,       "D2-05-F38 (the ministry's availability assumption, made for allopathic and AYUSH doctors together)", "Share of registered doctors in practice"),
    "doctors_private":    (0.70,       "ASSUMPTION; 66.3% of outpatient diabetes care is private (D3-07-F01)", "Share of practising doctors in private practice"),
    "doctors_treat_bp":   (0.40,       "ASSUMPTION", "Share of those who manage blood pressure as general or internal-medicine doctors"),
    "patients_per_doctor": (30,        "ASSUMPTION", "Patients a doctor enrols in the programme"),
    "public_price_month": (15,         "ASSUMPTION (public drug cost is about Rs 200 a patient a year, D2-05-F18)", "Price per patient a month a state might pay"),
    "usd_inr":            (94.25,      "D2-05 Digest item 10 (rate on 13 Nov 2026)", "Rupees per US dollar"),
    "som_share_y3":       (0.005,      "ASSUMPTION", "Top-down share of SAM in year 3"),
    "som_share_y5":       (0.03,       "ASSUMPTION", "Top-down share of SAM in year 5"),
}
# bottom-up SOM: (year, clinics live at year end, paying patients per clinic)  all ASSUMPTION
SOM_PLAN = [(1, 2, 0), (2, 15, 150), (3, 60, 200), (4, 180, 220), (5, 400, 250)]


def v(k):
    return I[k][0]


def ind(n):
    """Indian digit grouping: 1388185 -> 13,88,185."""
    s = str(int(round(n)))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


def crore(x):
    return "₹{:,.0f} crore".format(x / CRORE) if x >= 100 * CRORE else "₹{:,.1f} crore".format(x / CRORE)


def lakh(n):
    return "{:,.1f} lakh".format(n / LAKH)


def main():
    out = []
    p_year = v("price_month") * 12

    treated_low = v("adults_htn") * v("treated_share_low")
    treated_high = v("adults_htn") * v("treated_share_high")
    retail_patients = v("retail_bp_market") / v("private_drug_year")

    tam_bu = treated_low * p_year
    tam_td = retail_patients * p_year
    tam = min(tam_bu, tam_td)

    sam_bu_patients = retail_patients * v("phone_share") * v("organised_share")
    sam_bu = sam_bu_patients * p_year
    sam_td_doctors = v("doctors") * v("doctors_active") * v("doctors_private") * v("doctors_treat_bp")
    sam_td_patients = sam_td_doctors * v("patients_per_doctor")
    sam_td = sam_td_patients * p_year
    sam = min(sam_bu, sam_td)

    som_bu = {y: c * n * p_year for y, c, n in SOM_PLAN}
    som_td = {3: sam * v("som_share_y3"), 5: sam * v("som_share_y5")}

    usd100m = 100e6 * v("usd_inr")
    need_patients = usd100m / p_year

    out.append("# DT3 market model: home blood-pressure step loop (output of tools/dtx_market_model.py)\n")
    out.append("All figures are OUR ARITHMETIC from the inputs listed at the end. Rupees a year. Price: ₹{:,} a patient a month, ₹{:,} a year (ASSUMPTION).\n".format(v("price_month"), p_year))

    out.append("## Result\n")
    out.append("| Level | Top-down | Bottom-up | Used (the lower) |")
    out.append("|---|---|---|---|")
    out.append("| TAM: every Indian adult on blood-pressure medicines who could be served | {} ({} private retail patients) | {} ({} treated adults, low case) | **{}** |".format(
        crore(tam_td), lakh(retail_patients), crore(tam_bu), lakh(treated_low), crore(tam)))
    out.append("| SAM: private patients a doctor could enrol on a household smartphone | {} ({} patients through {} doctors) | {} ({} patients) | **{}** |".format(
        crore(sam_td), lakh(sam_td_patients), lakh(sam_td_doctors), crore(sam_bu), lakh(sam_bu_patients), crore(sam)))
    out.append("| SOM year 3 | {} ({:.1%} of SAM) | {} ({} clinics x {} patients) | **{}** |".format(
        crore(som_td[3]), v("som_share_y3"), crore(som_bu[3]), SOM_PLAN[2][1], SOM_PLAN[2][2], crore(min(som_td[3], som_bu[3]))))
    out.append("| SOM year 5 | {} ({:.0%} of SAM) | {} ({} clinics x {} patients) | **{}** |".format(
        crore(som_td[5]), v("som_share_y5"), crore(som_bu[5]), SOM_PLAN[4][1], SOM_PLAN[4][2], crore(min(som_td[5], som_bu[5]))))
    out.append("")

    out.append("## How each figure is counted\n")
    out.append("- **TAM top-down.** Retail blood-pressure medicine sales {} divided by a private patient's yearly medicine spend ₹{:,} = {} patients buying in the private market. Times ₹{:,} a year = {}. The spend figure is a modelled price for one brand pill a day; across the paper's range of about ₹2,500 to ₹5,100 the count runs from {} to {} patients.".format(
        crore(v("retail_bp_market")), v("private_drug_year"), lakh(retail_patients), p_year, crore(tam_td), lakh(v("retail_bp_market") / 5100), lakh(v("retail_bp_market") / 2500)))
    out.append("- **TAM bottom-up.** {:,.0f} million adults with high blood pressure x {:.1%} on medicines = {} (the ceiling from drug sales, {:.1%}, would give {}). Times ₹{:,} = {}.".format(
        v("adults_htn") / 1e6, v("treated_share_low"), lakh(treated_low), v("treated_share_high"), lakh(treated_high), p_year, crore(tam_bu)))
    out.append("- **SAM bottom-up.** {} private patients x {:.0%} reachable on a household smartphone x {:.0%} whose doctor could enrol them = {} patients. Times ₹{:,} = {}.".format(
        lakh(retail_patients), v("phone_share"), v("organised_share"), lakh(sam_bu_patients), p_year, crore(sam_bu)))
    out.append("- **SAM top-down.** {} registered doctors x {:.0%} in practice x {:.0%} private x {:.0%} managing blood pressure = {} doctors, x {} patients each = {} patients. Times ₹{:,} = {}.".format(
        ind(v("doctors")), v("doctors_active"), v("doctors_private"), v("doctors_treat_bp"), lakh(sam_td_doctors), v("patients_per_doctor"), lakh(sam_td_patients), p_year, crore(sam_td)))
    out.append("- **SOM bottom-up.** Clinics live and paying patients per clinic at each year end (the first year is an unpaid pilot):")
    out.append("")
    out.append("| Year | Clinics | Patients per clinic | Paying patients | Revenue a year |")
    out.append("|---|---|---|---|---|")
    for y, c, n in SOM_PLAN:
        out.append("| {} | {} | {} | {} | {} |".format(y, c, n, ind(c * n), crore(c * n * p_year) if c * n else "pilot, unpaid"))
    out.append("")

    out.append("## The US$100 million-a-year test\n")
    out.append("- US$100 million a year = {} at ₹{} to the dollar.".format(crore(usd100m), v("usd_inr")))
    out.append("- At ₹{:,} a patient a year that needs {} paying patients ({}).".format(p_year, lakh(need_patients), ind(need_patients)))
    out.append("- The serviceable market above holds {} patients. **The test fails on this model in India alone**: it needs {:.1f} times the SAM.".format(lakh(min(sam_bu_patients, sam_td_patients)), need_patients / min(sam_bu_patients, sam_td_patients)))
    out.append("- Where the rest would have to come from: more protocols on the same loop (diabetes, heart failure), a paid public tier, other countries that use the same family of protocols, or a higher price paid by an insurer, employer or medicine maker.")
    out.append("")

    out.append("## Price sensitivity\n")
    out.append("| Price a month | SAM used | SOM year 5 (bottom-up) | Patients needed for US$100 million |")
    out.append("|---|---|---|---|")
    for pm in (99, 149, 299):
        py = pm * 12
        out.append("| ₹{} | {} | {} | {} |".format(pm, crore(min(sam_bu_patients, sam_td_patients) * py), crore(SOM_PLAN[4][1] * SOM_PLAN[4][2] * py), lakh(usd100m / py)))
    out.append("")

    public_tier = v("public_on_treatment") * v("public_price_month") * 12
    out.append("## A public tier, shown apart\n")
    out.append("- {} patients on treatment in the public programme x ₹{} a month x 12 = {} a year. A state would pay this only for results, since the medicines themselves cost about ₹200 a patient a year.".format(
        lakh(v("public_on_treatment")), v("public_price_month"), crore(public_tier)))
    out.append("")

    out.append("## Inputs\n")
    out.append("| Input | Value | Source or tag |")
    out.append("|---|---|---|")
    for k, (val, src, label) in I.items():
        if isinstance(val, float) and val < 1:
            sval = "{:.1%}".format(val)
        elif val >= CRORE * 100:
            sval = crore(val)
        elif val >= 1e6:
            sval = "{:,.2f} million".format(val / 1e6)
        else:
            sval = ind(val)
        out.append("| {} | {} | {} |".format(label, sval, src))
    out.append("| Clinics and patients per clinic by year | see the table above | ASSUMPTION |")
    out.append("")
    out.append("What this model leaves out: patients treated in the public system (shown apart), diabetes and other conditions, device sales, and any country outside India. No measured split of public and private treatment was found (D2-05-F30), which is why the private count is derived from medicine sales.")

    text = "\n".join(out) + "\n"
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write(text)
    print(text)


if __name__ == "__main__":
    main()
