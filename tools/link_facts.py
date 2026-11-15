"""Turn fact IDs in the joined report into source links and build the claim register.

Usage:  python link_facts.py <notes_dir> <report.md>

What it does
1. Reads every research note in <notes_dir> (files named like "D1-01 ....md") and indexes each
   fact ID with the line that defines it, the URLs on that line and whether it was OPENED or SNIPPET.
2. Reads the claims-check notes (file names containing "Claims check") and indexes each verdict.
3. In the report: expands short forms ("D1-01-F09, F38", "D1-04-F02 to F07"), then turns every
   fact ID into a link to its first source URL.
4. Replaces the line <!-- REGISTER --> with a table of every fact cited: what the note records,
   the source, how it was read, and the claims-check verdict.
5. Prints what could not be linked, so it can be fixed by hand.
"""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FULL_ID = re.compile(r"D(\d)-(\d\d)-F0*(\d+)")
FULL_DEF = re.compile(r"^\s*(?:[-*]\s*|\|\s*)?\**D(\d)-(\d\d)-F0*(\d+)\b")
SHORT_DEF = re.compile(r"^\s*(?:[-*]\s*|\|\s*)\**F0*(\d+)\b")
URL = re.compile(r"https?://[^\s<>|)\]]+")
STATUS_WORDS = ("CONFIRMED", "CORRECTED", "CONTESTED", "NOT FOUND")


def canon(a, b, n):
    return "D%s-%s-F%d" % (a, b, int(n))


def clean_url(u):
    return u.rstrip(".,;:'\"")


PMID = re.compile(r"PMID:?\s*(\d{6,9})")
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s|,;)\]]+)")
SAME = re.compile(r"same (source|url|report|page|paper|study|note|article|pdf|document)", re.I)


def urls_on(line):
    urls = [clean_url(u) for u in URL.findall(line)]
    if not urls:
        m = PMID.search(line)
        if m:
            urls = ["https://pubmed.ncbi.nlm.nih.gov/%s/" % m.group(1)]
    if not urls:
        m = DOI.search(line)
        if m:
            urls = ["https://doi.org/" + m.group(1).rstrip(".")]
    return urls


def index_notes(notes_dir):
    facts, checks = {}, {}
    for f in sorted(notes_dir.glob("D*.md")):
        m = re.match(r"^(D\d-\d\d)\b", f.name)
        if not m:
            continue
        code = m.group(1)
        a, b = code[1], code[3:5]
        lines = f.read_text(encoding="utf-8").splitlines()
        if "claims check" in f.name.lower():
            for line in lines:
                if not line.lstrip().startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 3:
                    continue
                ids = [canon(*x) for x in FULL_ID.findall(cells[0])]
                if not ids:
                    continue
                for i in ids:
                    checks[i] = (cells[2], cells[3] if len(cells) > 3 else "", f.name)
            continue

        # which lines sit inside the Digest (never used as a definition unless nothing else exists)
        in_digest, digest = False, set()
        for n, line in enumerate(lines):
            if line.startswith("## "):
                in_digest = line.strip().lower().startswith("## digest")
            if in_digest:
                digest.add(n)

        def_line = {}                       # fid -> line number
        for n, line in enumerate(lines):    # pass 1: the ID opens the line
            md = FULL_DEF.match(line)
            fid = canon(*md.groups()) if md else None
            if not fid:
                ms = SHORT_DEF.match(line)
                if ms:
                    fid = canon(a, b, ms.group(1))
            if fid and fid not in def_line and (n not in digest):
                def_line[fid] = n
        seen = {}                           # pass 2: first mention outside the Digest, a line with a URL preferred
        for n, line in enumerate(lines):
            for x in FULL_ID.findall(line):
                fid = canon(*x)
                if fid[:5] != code or fid in def_line:
                    continue
                has_url = bool(urls_on(line))
                rank = (n in digest, not has_url, n)
                if fid not in seen or rank < seen[fid][0]:
                    seen[fid] = (rank, n)
        for fid, (_, n) in seen.items():
            def_line[fid] = n

        starts = set(def_line.values())
        last_urls, last_n = [], -99
        for fid, n in sorted(def_line.items(), key=lambda kv: kv[1]):
            line = lines[n]
            urls = urls_on(line)
            if not urls:                                    # look ahead a few lines, up to the next fact
                for k in range(n + 1, min(n + 4, len(lines))):
                    if k in starts:
                        break
                    urls = urls_on(lines[k])
                    if urls:
                        break
            inherited = False
            if not urls and last_urls and (
                SAME.search(line)
                or (n - last_n <= 4 and "NOT FOUND" not in line and "SNIPPET" not in line)
            ):
                urls, inherited = list(last_urls), True     # same source as the fact just above it
            if urls and not inherited:
                last_urls, last_n = urls, n
            elif urls:
                last_n = n
            status = "SNIPPET" if "SNIPPET" in line else ("OPENED" if "OPENED" in line else "")
            text = line.strip().lstrip("-*| ").strip()
            text = re.sub(r"^\**(?:D\d-\d\d-)?F0*\d+[a-z]?\**[\s.:|/]*", "", text)
            text = URL.sub("", text)
            text = re.sub(r"\s+", " ", text).strip(" .|:;,")
            facts[fid] = {"text": text, "urls": urls, "status": status, "note": f.name}
    return facts, checks


def expand_short_forms(text):
    """D1-01-F09, F38 -> D1-01-F09, D1-01-F38 ; D1-04-F02 to F07 -> all seven IDs."""
    pat = re.compile(r"(D\d-\d\d-)F(\d+)((?:\s*(?:,|and)\s*F\d+\b|\s+to\s+F\d+\b)+)")

    def repl(m):
        prefix, first, tail = m.group(1), m.group(2), m.group(3)
        width = len(first)
        out = [prefix + "F" + first]
        prev = int(first)
        for kind, num in re.findall(r"(,|and|to)\s*F(\d+)", tail):
            n = int(num)
            if kind == "to" and 0 < n - prev <= 30:
                out.extend(prefix + "F" + str(k).zfill(width) for k in range(prev + 1, n + 1))
            else:
                out.append(prefix + "F" + num)
            prev = n
        return ", ".join(out)

    prev_text = None
    while prev_text != text:
        prev_text = text
        text = pat.sub(repl, text)
    return text


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    notes_dir, report = Path(sys.argv[1]), Path(sys.argv[2])
    facts, checks = index_notes(notes_dir)
    text = report.read_text(encoding="utf-8")
    text = expand_short_forms(text)

    # [D1-01-F02, D1-01-F04] -> (D1-01-F02, D1-01-F04), so links are not nested in brackets
    group = re.compile(r"\[\s*(D\d-\d\d-F\d+(?:\s*[,;]\s*D\d-\d\d-F\d+)*)\s*\](?!\()")
    text = group.sub(lambda m: "(" + m.group(1) + ")", text)

    cited, missing, nourl = [], [], []

    def link(m):
        if m.start() > 0 and text[m.start() - 1] == "[" and text[m.end():m.end() + 2] == "](":
            return m.group(0)
        fid = canon(*m.groups())
        if fid not in cited:
            cited.append(fid)
        fact = facts.get(fid)
        if not fact:
            if fid not in missing:
                missing.append(fid)
            return m.group(0)
        if not fact["urls"]:
            if fid not in nourl:
                nourl.append(fid)
            return m.group(0)
        return "[%s](%s)" % (m.group(0), fact["urls"][0])

    out_lines, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code or "<!-- REGISTER -->" in line:
            out_lines.append(line)
            continue
        out_lines.append(FULL_ID.sub(link, line))
    text = "\n".join(out_lines) + "\n"

    def cell(s, n):
        s = s.replace("|", "/").replace("\n", " ")
        return (s[: n - 1] + "…") if len(s) > n else s

    def sort_key(fid):
        a, b, n = FULL_ID.match(fid).groups()
        return (int(a), int(b), int(n))

    rows = ["| Fact | What the note records | Source | Read as | Claims check |", "|---|---|---|---|---|"]
    tally = {}
    for fid in sorted(cited, key=sort_key):
        fact = facts.get(fid)
        if not fact:
            rows.append("| %s | NOT IN NOTES | | | |" % fid)
            continue
        if fact["urls"]:
            src = ", ".join(
                "[%s](%s)" % (urlparse(u).netloc.replace("www.", "") if i == 0 else str(i + 1), u)
                for i, u in enumerate(fact["urls"][:3])
            )
        else:
            src = "see note"
        chk = checks.get(fid)
        if chk:
            word = next((w for w in STATUS_WORDS if w in chk[0].upper()), chk[0][:20])
            tally[word] = tally.get(word, 0) + 1
            chk_text = cell(chk[0] + ((" " + chk[1]) if word != "CONFIRMED" and chk[1] else ""), 170)
        else:
            tally["not re-checked"] = tally.get("not re-checked", 0) + 1
            chk_text = "not re-checked"
        rows.append("| %s | %s | %s | %s | %s |" % (fid, cell(fact["text"], 230), src, fact["status"] or "", chk_text))
    text = text.replace("<!-- REGISTER -->", "\n".join(rows))
    report.write_text(text, encoding="utf-8")

    print("facts indexed: %d   verdicts indexed: %d" % (len(facts), len(checks)))
    print("facts cited in report: %d" % len(cited))
    print("claims-check tally: " + ", ".join("%s %d" % kv for kv in sorted(tally.items())))
    if missing:
        print("CITED BUT NOT IN NOTES (%d): %s" % (len(missing), ", ".join(missing)))
    if nourl:
        print("no URL on the fact line (%d): %s" % (len(nourl), ", ".join(nourl)))


if __name__ == "__main__":
    main()
