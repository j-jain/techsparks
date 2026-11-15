"""Check that a restructured edition kept the facts of the original parts.

Usage:  python check_restructure.py <old_parts_dir> <new_parts_dir>

Reports
- fact IDs cited in the old parts but missing from the new parts, and IDs that are new
  (D4 IDs are a later research round and are counted, not flagged; files named *biology* and
  "### ... new research" sections are skipped by the numbers check)
- numbers in the new text that appear nowhere in the old text (to check by hand)
- old-style cross-references left in the new text ("part F2", "tab H", "Decision brief")
- pictures: each should be placed exactly once
- story repetition: how often the most-repeated old facts are cited in the story chapters
- word counts per new part
"""
import collections
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FULL = re.compile(r"D(\d)-(\d\d)-F0*(\d+)")
SHORT = re.compile(r"(D\d-\d\d)-F0*\d+((?:\s*(?:,|and|to)\s*F0*\d+)+)")
URL = re.compile(r"https?://\S+")
PIC = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
NUM = re.compile(r"(?<![\w.-])\d[\d,]*(?:\.\d+)?")
STALE = re.compile(r"\b[Pp]arts? [A-M](?:\d|\b)|\b[Tt]ab [A-M]\b|\bDecision brief\b|\bsee [A-M]\d\b|\b(?:B|C|D|E|F|G)\d{1,2}\b(?! *\.)")
STORY = ("10", "20", "30", "40", "50", "60")


def ids(text):
    out = collections.Counter()
    for m in FULL.finditer(text):
        out["D%s-%s-F%d" % (m.group(1), m.group(2), int(m.group(3)))] += 1
    for m in SHORT.finditer(text):
        for n in re.findall(r"F0*(\d+)", m.group(2)):
            out["%s-F%d" % (m.group(1), int(n))] += 1
    return out


def numbers(text):
    text = URL.sub(" ", text)
    text = PIC.sub(" ", text)
    text = FULL.sub(" ", text)
    text = re.sub(r"\bF0*\d+\b", " ", text)
    return set(m.group(0).rstrip(",.") for m in NUM.finditer(text))


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    old_dir, new_dir = Path(sys.argv[1]), Path(sys.argv[2])
    old_parts = {p.name: p.read_text(encoding="utf-8") for p in sorted(old_dir.glob("*.md"))}
    new_parts = {p.name: p.read_text(encoding="utf-8") for p in sorted(new_dir.glob("*.md"))}
    old_all, new_all = "\n".join(old_parts.values()), "\n".join(new_parts.values())
    problems = 0

    old_ids, new_ids = set(ids(old_all)), set(ids(new_all))
    print("== fact IDs: %d in old, %d in new" % (len(old_ids), len(new_ids)))
    new_round = sorted(i for i in new_ids - old_ids if i.startswith("D4-"))
    print("  new research (D4) IDs cited: %d" % len(new_round))
    missing, extra = sorted(old_ids - new_ids), sorted(i for i in new_ids - old_ids if not i.startswith("D4-"))
    for label, group in (("missing from new", missing), ("new, not in old", extra)):
        if group:
            problems += len(group)
            print("  %s (%d): %s" % (label, len(group), ", ".join(group)))

    print("== numbers in the new text that are not in the old text")
    old_nums = numbers(old_all)
    unknown = 0
    for name, text in new_parts.items():
        if "biology" in name:
            continue
        new_section = False
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("### "):
                new_section = "new research" in line.lower()
            if new_section or line.startswith("#") or "<!--" in line:
                continue
            for n in sorted(numbers(line) - old_nums):
                plain = n.replace(",", "")
                if plain.isdigit() and int(plain) <= 12:
                    continue
                if re.fullmatch(r"\d\.\d{1,2}", n) and re.search(r"[Cc]hapters? [\d.]*" + re.escape(n) + r"|" + re.escape(n) + r" and|and " + re.escape(n), line):
                    continue
                unknown += 1
                print("  %s:%d  %s   | %s" % (name, i, n, line.strip()[:110]))
    print("  total: %d" % unknown)
    problems += unknown

    print("== old-style cross-references")
    stale = 0
    for name, text in new_parts.items():
        if name.startswith(("70", "90")) or "biology" in name:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            clean = URL.sub(" ", FULL.sub(" ", line))
            clean = clean.replace("old part", "oldpart")
            for m in STALE.finditer(clean):
                if re.match(r"[A-I]\d", m.group(0)) and name.startswith("8"):
                    continue
                stale += 1
                print("  %s:%d  '%s'   | %s" % (name, i, m.group(0), line.strip()[:100]))
    print("  total: %d (appendix section numbers like B3 inside appendices are allowed; check the rest)" % stale)

    print("== pictures")
    used = collections.Counter(m.group(1) for m in PIC.finditer(new_all))
    root = new_dir.parent.parent
    for pic in sorted((root / "adaptive-care-pictures").glob("*.png")):
        key = "adaptive-care-pictures/" + pic.name
        if used[key] != 1:
            problems += 1
            print("  %s placed %d times" % (pic.name, used[key]))
    for key in used:
        if not (root / key).exists():
            problems += 1
            print("  missing file: " + key)

    print("== story repetition (old facts cited in 4+ old parts)")
    per_old = collections.Counter()
    for text in old_parts.values():
        for i in set(ids(text)):
            per_old[i] += 1
    story = collections.Counter()
    for name, text in new_parts.items():
        if name[:2] in STORY:
            story.update(ids(text))
    for i, n in sorted(per_old.items(), key=lambda kv: -kv[1]):
        if n >= 4:
            flag = "  <-- repeated in story" if story[i] > 2 else ""
            print("  %-12s old parts %2d  story citations %d%s" % (i, n, story[i], flag))

    print("== words per new part")
    total = 0
    for name, text in new_parts.items():
        w = len(re.findall(r"\S+", text))
        total += w
        print("  %-24s %6d" % (name, w))
    print("  %-24s %6d" % ("total", total))
    print("\nproblems flagged: %d" % problems)


if __name__ == "__main__":
    main()
