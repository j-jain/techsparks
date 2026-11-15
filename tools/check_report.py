"""Checks on the joined report. Run after join_parts.py and link_facts.py.

Usage:  python check_report.py <report.md> [--links]

Reports
- banned words, em dashes, exclamation marks
- picture links that point to a missing file
- paragraphs and table rows that contain a number but no fact link and no tag
  (OUR ARITHMETIC, OUR ESTIMATE, OUR VIEW, ASSUMPTION, EXAMPLE, THEIR CLAIM, NOT RESEARCHED...)
- with --links: every distinct source URL is requested once and failures are listed
"""
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BANNED = [
    "synergy", "revolutionary", "game-changing", "ai-powered", "seamless", "leverage", "utilise", "utilize",
    "robust", "cutting-edge", "innovative", "streamline", "optimise", "optimize", "empower", "unlock",
    "world-class", "best-in-class", "next-gen", "ecosystem", "holistic", "delve", "landscape",
]
TAGS = ("OUR ARITHMETIC", "OUR ESTIMATE", "OUR VIEW", "ASSUMPTION", "EXAMPLE", "THEIR CLAIM", "NOT RESEARCHED",
        "NOT FOUND", "OUR DESIGN", "OUR SIMULATION", "Mock-up", "TARGET")
FACT_LINK = re.compile(r"\[D\d-\d\d-F\d+\]\(|D\d-\d\d-F\d+")
NUMBER = re.compile(r"(?<![A-Za-z#/-])\d[\d,.]*\s?(%|mmHg|crore|lakh|million|billion|patients|people|points)|[₹$£€]\s?\d")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    report = Path(sys.argv[1])
    text = report.read_text(encoding="utf-8")
    lines = text.splitlines()
    problems = 0

    print("== words and marks")
    for i, line in enumerate(lines, 1):
        if line.startswith(">") or "THEIR CLAIM" in line:
            continue
        low = re.sub(r"\]\([^)]*\)", "]", line.lower())
        low = re.sub(r"\"[^\"]*\"", "", low)
        for w in BANNED:
            if re.search(r"(?<![a-z-])" + re.escape(w) + r"(?![a-z])", low):
                print("  line %d: banned word '%s'" % (i, w))
                problems += 1
        if "—" in line:
            print("  line %d: em dash" % i)
            problems += 1
        if re.search(r"[a-z]!(\s|$)", line) and not line.lstrip().startswith("!["):
            print("  line %d: exclamation mark" % i)
            problems += 1

    print("== pictures")
    for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        p = report.parent / m.group(1)
        if not p.exists():
            print("  missing picture: " + m.group(1))
            problems += 1

    print("== numbers without a source or a tag")
    untagged, in_code, section = 0, False, ""
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        if line.startswith("#"):
            section = line.strip("# ").strip()
            continue
        if line.startswith("|---") or line.startswith("![") or not line.strip():
            continue
        if NUMBER.search(line) and not FACT_LINK.search(line) and not any(t in line for t in TAGS):
            untagged += 1
            if untagged <= 60:
                print("  line %d [%s]: %s" % (i, section[:28], line.strip()[:120]))
    print("  total lines with a number and no source or tag: %d" % untagged)

    if "--links" in sys.argv:
        print("== links")
        urls = sorted(set(u.rstrip(".,") for u in re.findall(r"\]\((https?://[^)\s]+)\)", text)))

        def probe(u):
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (link check)"}, method="GET")
                with urllib.request.urlopen(req, timeout=20) as r:
                    return u, r.status
            except Exception as e:  # noqa: BLE001
                code = getattr(e, "code", None)
                return u, code if code else type(e).__name__

        with ThreadPoolExecutor(max_workers=12) as ex:
            results = list(ex.map(probe, urls))
        bad = [(u, s) for u, s in results if s != 200]
        print("  %d distinct links, %d did not answer 200" % (len(urls), len(bad)))
        for u, s in bad:
            print("  %s  %s" % (s, u))

    print("== done: %d style problems" % problems)


if __name__ == "__main__":
    main()
