"""Build the SPARK Night source register (.xlsx) from the Round 2 and Round 3 notes.

One row per (finalist, URL) cited in a finalist's Round 2 section, with the source type
(by domain), the date found on the citing line, what the line says it supports, and the
Round 3 claims-check status where that URL was re-checked.
"""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
NOTES = ROOT / "research_notes"
OUT = ROOT / "SPARK Night 2026 - source register.xlsx"

# Finalist -> (R2 file, keywords that identify its "## Problem" heading)
FINALISTS = {
    "U4 Lift black-box": ("R2-03 Urban sensing.md", ["U4"]),
    "U1 Street-dog re-ID": ("R2-01 Bio and health.md", ["U1", "Stray dogs"]),
    "A1 Indoor/outdoor PM pair": ("R2-03 Urban sensing.md", ["A1"]),
    "F1 Digital-arrest call-guard": ("R2-05 AI and systems.md", ["F1"]),
    "H1 Counterfeit-medicine checker": ("R2-01 Bio and health.md", ["H1", "Counterfeit"]),
    "E1 Smart-meter witness": ("R2-02 Home energy.md", ["E1"]),
    "S2 GNSS integrity node": ("R2-04 Space defence and industrial safety.md", ["S2"]),
    "E3 EV charging-bay monitor": ("R2-02 Home energy.md", ["E3"]),
}
CLAIMS_FILES = ["R3-claims-01.md", "R3-claims-02.md", "R3-claims-03.md"]

URL_RE = re.compile(r"https?://[^\s<>()\[\]\"']+")
DATE_RES = [
    re.compile(r"\b\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]* \d{4}\b"),
    re.compile(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]* \d{4}\b"),
    re.compile(r"\b(?:FY|20)\d{2}(?:[-–]\d{2,4})?\b"),
]
STATUS_RE = re.compile(r"\b(CONFIRMED|CORRECTED|CONTESTED|NOT FOUND|LIVE|DEAD|CHANGED)\b")
SUBHEAD_RE = re.compile(r"^###\s*\(([a-g])\)")

TYPE_RULES = [
    ("reddit", ["reddit.com", "sentinel-team.org", "arctic-shift", "redlib", "psf.lt"]),
    ("youtube", ["youtube.com", "youtu.be", "returnyoutubedislike"]),
    ("government / parliament", ["gov.in", "nic.in", "pib.gov", "sansad", "cpcb", "morth", "mnre", "cdsco",
                                 "localcircles"]),
    ("court", ["livelaw", "indiankanoon", "verdictum", "barandbench", "scobserver", "scconline"]),
    ("academic", ["arxiv", "ncbi", "pmc", "nih.gov", "elifesciences", "plos", "biomedcentral", "sciencedirect",
                  "springer", "ieee", "researchsquare", "europepmc", "stanford", "utexas", "ceew.in",
                  "bfi.uchicago", "ispor", "pubmed", "nist.gov"]),
    ("vendor / company", ["robu.in", "zbotic", "robocraze", "electronicscomp", "amazon", "bolt.earth",
                          "airveda", "genrobotics", "kone", "otis", "thermofisher", "u-blox", "melexis",
                          "honeywell", "truecaller", "solarquarter", "mercom", "indiamart", "fruugo"]),
]


def clean_url(u: str) -> str:
    return u.rstrip(".,;:)]}>\"'").rstrip()


def source_type(u: str) -> str:
    host = (urlparse(u).netloc or "").lower()
    path = u.lower()
    for label, keys in TYPE_RULES:
        if any(k in host or k in path for k in keys):
            return label
    news = ["theprint", "thequint", "newslaundry", "indiaspend", "ndtv", "indiatimes", "hindustantimes", "thehindu",
            "indianexpress", "business-standard", "businesstoday", "economictimes", "livemint", "freepressjournal",
            "tribuneindia", "deccanherald", "deccanchronicle", "telanganatoday", "thenewsminute", "theweek",
            "outlookindia", "downtoearth", "inc42", "yourstory", "entrackr", "medicaldialogues", "careers360",
            "millenniumpost", "ianslive", "newsonair", "scroll", "wionews", "aljazeera", "bbc", "reuters",
            "techcrunch", "citizenmatters", "mongabay", "thewire", "siasat", "ptinews", "aajtak", "zeenews",
            "news18", "republicworld", "patrika", "bhaskar", "jagran", "amarujala", "navbharat", "gulfnews",
            "telecomtalk", "autocarpro", "autocarindia", "pv-magazine", "saurenergy", "newkerala", "etvbharat",
            "organiser", "lokmattimes", "babushahi", "insidegnss", "gpsworld", "elevatorworld", "mediananma",
            "medianama", "dtnext", "onmanorama", "kashmirlife", "newsarenaindia", "thehitavada", "openthemagazine",
            "governancenow", "opencity", "newsable", "asianetnews", "uniindia", "tndindia", "powerline"]
    if any(n in host for n in news):
        return "news"
    return "other"


def find_date(line: str) -> str:
    for rx in DATE_RES:
        m = rx.search(line)
        if m:
            return m.group(0)
    return ""


def split_problems(text: str):
    """Yield (heading, body) for each '## Problem' section."""
    parts = re.split(r"^(## Problem[^\n]*)$", text, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        yield parts[i], parts[i + 1]


def section_for(finalist: str, heading_keys, text: str):
    for heading, body in split_problems(text):
        if any(k.lower() in heading.lower() for k in heading_keys):
            return body
    return ""


def collect_status():
    """Map URL -> (status, finalist-ish context) from the Round 3 claims files."""
    status = {}
    for name in CLAIMS_FILES:
        p = NOTES / name
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            urls = [clean_url(u) for u in URL_RE.findall(line)]
            if not urls:
                continue
            m = STATUS_RE.search(line)
            if not m:
                continue
            for u in urls:
                status.setdefault(u, m.group(1))
    return status


def main():
    status = collect_status()
    rows = []
    seen = set()
    for finalist, (fname, keys) in FINALISTS.items():
        p = NOTES / fname
        if not p.exists():
            print("missing", p)
            continue
        body = section_for(finalist, keys, p.read_text(encoding="utf-8", errors="replace"))
        if not body:
            print("no section for", finalist)
            continue
        sub = ""
        for line in body.splitlines():
            m = SUBHEAD_RE.match(line.strip())
            if m:
                sub = {"a": "(a) proof", "b": "(b) market", "c": "(c) competitors", "d": "(d) solutions",
                       "e": "(e) gates", "f": "(f) overnight", "g": "(g) verdict"}[m.group(1)]
                continue
            urls = [clean_url(u) for u in URL_RE.findall(line)]
            if not urls:
                continue
            context = URL_RE.sub("", line).strip(" -—|*>")
            context = re.sub(r"\s+", " ", context)[:240]
            for u in urls:
                key = (finalist, u)
                if key in seen:
                    continue
                seen.add(key)
                st = status.get(u)
                if st is None:
                    # try a loose match on the path without query string
                    base = u.split("?")[0].rstrip("/")
                    st = next((v for k, v in status.items() if k.split("?")[0].rstrip("/") == base), None)
                rows.append([
                    finalist, u, source_type(u), find_date(line), sub, context,
                    st or "not individually re-checked in R3 (section re-read)",
                ])

    wb = Workbook()
    ws = wb.active
    ws.title = "Sources"
    header = ["Finalist", "URL", "Source type", "Date on citing line", "Section", "What it supports (citing line)",
              "Round 3 status"]
    ws.append(header)
    for r in rows:
        ws.append(r)
    widths = [30, 70, 20, 18, 14, 90, 36]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for c in ws[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="DDDDDD")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=True)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    ws2 = wb.create_sheet("Summary")
    ws2.append(["Finalist", "URLs cited", "Reddit", "YouTube", "Govt / parliament", "Court", "Academic", "News",
                "Vendor", "Other", "CONFIRMED", "CORRECTED", "CONTESTED", "NOT FOUND", "LIVE/DEAD/CHANGED"])
    for finalist in FINALISTS:
        fr = [r for r in rows if r[0] == finalist]
        t = lambda label: sum(1 for r in fr if r[2] == label)
        s = lambda label: sum(1 for r in fr if r[6] == label)
        ws2.append([finalist, len(fr), t("reddit"), t("youtube"), t("government / parliament"), t("court"),
                    t("academic"), t("news"), t("vendor / company"), t("other"), s("CONFIRMED"), s("CORRECTED"),
                    s("CONTESTED"), s("NOT FOUND"), s("LIVE") + s("DEAD") + s("CHANGED")])
    ws2.append(["Total", len(rows)])
    for c in ws2[1]:
        c.font = Font(bold=True)
    ws2.column_dimensions["A"].width = 32
    ws2.append([])
    ws2.append(["Built 3 Nov 2026 from research_notes R2-01..R2-05 (finalist sections) and R3-claims-01..03. "
                "Status is the Round 3 mark where the claims-checker opened that URL; other URLs sit in sections "
                "whose figures were re-read but not individually marked."])

    wb.save(OUT)
    print(f"wrote {OUT} with {len(rows)} rows; statuses found for {sum(1 for r in rows if r[6] in ('CONFIRMED','CORRECTED','CONTESTED','NOT FOUND','LIVE','DEAD','CHANGED'))}")


if __name__ == "__main__":
    main()
