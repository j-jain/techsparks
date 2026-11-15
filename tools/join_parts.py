"""Join the part files in report-parts/dtx into the one adaptive-care document.

Usage:
    python join_parts.py [parts_dir] [out_file]

Parts are joined in file-name order with one blank line between them.
A line that reads exactly <!-- CONTENTS --> is replaced by a contents list
built from the level-2 headings (## ...) of all parts.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_PARTS = ROOT / "report-parts" / "dtx"
DEFAULT_OUT = ROOT / "SPARK Night 2026 - adaptive care challenge.md"


def slug(heading: str) -> str:
    """GitHub-style anchor for a heading."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parts_dir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PARTS
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    parts = sorted(parts_dir.glob("*.md"))
    if not parts:
        sys.exit(f"No part files found in {parts_dir}")

    texts = [p.read_text(encoding="utf-8").strip() for p in parts]
    doc = "\n\n".join(texts) + "\n"

    in_code = False
    headings = []
    for line in doc.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and line.startswith("## "):
            headings.append(line[3:].strip())
    contents = "\n".join(f"- [{h}](#{slug(h)})" for h in headings)
    doc = doc.replace("<!-- CONTENTS -->", contents)

    out.write_text(doc, encoding="utf-8", newline="\n")
    words = len(re.findall(r"\S+", doc))
    print(f"Joined {len(parts)} parts -> {out}")
    print(f"{words:,} words, {doc.count(chr(10)):,} lines, {len(headings)} sections")
    for p in parts:
        print("  ", p.name)


if __name__ == "__main__":
    main()
