"""Turn the Markdown report into one PDF with its pictures inside.

Usage (needs Python 3.11 here, which has markdown-it-py, and Chrome or Edge):
    python md_to_pdf.py <report.md> [out.pdf]

- Tables, block quotes, code blocks, links and pictures are kept.
- Each heading gets the same anchor the contents list uses, so the contents list is clickable.
- Pictures are found relative to the Markdown file.
- The page is A4 with page numbers at the foot.
"""
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BROWSERS = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page {
  size: A4;
  margin: 16mm 14mm 18mm 14mm;
  @bottom-center { content: counter(page) " / " counter(pages); font: 8pt "Segoe UI", Arial, sans-serif; color: #64748b; }
}
html { font-size: 10.4pt; }
body { font-family: "Segoe UI", "Nirmala UI", Arial, sans-serif; color: #111827; line-height: 1.42; margin: 0; }
h1 { font-size: 23pt; line-height: 1.15; margin: 0 0 10pt; }
h2 { font-size: 16.5pt; line-height: 1.2; margin: 0 0 9pt; padding-bottom: 3pt; border-bottom: 2pt solid #0f766e; page-break-before: always; }
h3 { font-size: 12.6pt; margin: 14pt 0 5pt; color: #0f3d3a; page-break-after: avoid; }
h4 { font-size: 11pt; margin: 11pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 6pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 6pt; padding-left: 16pt; }
li { margin: 0 0 2.5pt; }
a { color: #0b5cab; text-decoration: none; overflow-wrap: anywhere; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 8.3pt; line-height: 1.3; }
th, td { border: 0.6pt solid #cbd5e1; padding: 3pt 4pt; vertical-align: top; text-align: left; overflow-wrap: break-word; }
th { background: #f1f5f9; font-weight: 600; }
tr { page-break-inside: avoid; }
table.register { font-size: 6.9pt; table-layout: fixed; }
table.register th:nth-child(1), table.register td:nth-child(1) { width: 17mm; white-space: nowrap; overflow-wrap: normal; }
table.register th:nth-child(3), table.register td:nth-child(3) { width: 31mm; }
table.register th:nth-child(4), table.register td:nth-child(4) { width: 14mm; white-space: nowrap; overflow-wrap: normal; }
table.register th:nth-child(5), table.register td:nth-child(5) { width: 44mm; }
.phones { display: flex; gap: 9pt; justify-content: center; align-items: flex-start; margin: 8pt 0 10pt; page-break-inside: avoid; }
figure.phone { margin: 0; flex: 0 1 31%; }
figure.phone img { max-width: 100%; margin: 0; border: 0.6pt solid #e2e8f0; }
figcaption { font-size: 8pt; font-style: italic; color: #475569; text-align: center; margin-top: 3pt; }
blockquote { margin: 6pt 0 8pt; padding: 5pt 10pt; border-left: 3pt solid #5eead4; background: #f8fafc; }
blockquote p:last-child { margin-bottom: 0; }
code { font-family: Consolas, "Courier New", monospace; font-size: 8.6pt; background: #f1f5f9; padding: 0 2pt; overflow-wrap: anywhere; }
pre { background: #f8fafc; border: 0.6pt solid #e2e8f0; padding: 6pt 8pt; font-size: 7.8pt; line-height: 1.32; white-space: pre-wrap; overflow-wrap: anywhere; }
pre code { background: none; padding: 0; font-size: inherit; }
img { max-width: 100%; height: auto; display: block; margin: 8pt auto 3pt; page-break-inside: avoid; }
img.phone { max-width: 43%; border: 0.6pt solid #e2e8f0; }
hr { border: 0; border-top: 0.6pt solid #cbd5e1; margin: 10pt 0; }
"""


def slug(title):
    s = title.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s", "-", s)


def find_browser():
    for b in BROWSERS:
        if b and Path(b).exists():
            return b
    raise SystemExit("No Chrome or Edge found; set CHROME to its path.")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    md_path = Path(sys.argv[1]).resolve()
    pdf = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else md_path.with_suffix(".pdf")
    text = md_path.read_text(encoding="utf-8")

    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    body = md.render(text)

    def add_id(m):
        level, inner = m.group(1), m.group(2)
        plain = html.unescape(re.sub(r"<[^>]+>", "", inner))
        return '<h%s id="%s">%s</h%s>' % (level, slug(plain), inner, level)

    body = re.sub(r"<h([1-4])>(.*?)</h\1>", add_id, body, flags=re.S)

    base = md_path.parent.as_uri() + "/"

    def fix_img(m):
        src = m.group(1)
        cls = ' class="phone"' if re.search(r"/1[0-2]-bp-", "/" + src) else ""
        if not re.match(r"^[a-z]+:", src):
            src = base + src.replace(" ", "%20")
        return '<img%s src="%s"' % (cls, src)

    body = re.sub(r'<img src="([^"]+)"', fix_img, body)

    # phone mock-ups: picture plus its caption become a figure, and neighbours sit side by side
    def to_fig(m):
        return '<figure class="phone">%s<figcaption>%s</figcaption></figure>' % (m.group(1), m.group(2))

    body = re.sub(r'<p>(<img class="phone"[^>]*>)\s*<em>(.*?)</em></p>', to_fig, body, flags=re.S)
    body = re.sub(r'<p>(<img class="phone"[^>]*>)</p>\s*<p><em>(.*?)</em></p>', to_fig, body, flags=re.S)
    body = re.sub(
        r'((?:<figure class="phone">.*?</figure>\s*)+)',
        lambda m: '<div class="phones">%s</div>' % m.group(1),
        body,
        flags=re.S,
    )

    last = body.rfind("<table>")
    if last >= 0:
        body = body[:last] + '<table class="register">' + body[last + len("<table>"):]

    title = re.search(r"^# (.+)$", text, flags=re.M)
    doc = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head>'
        "<body>%s</body></html>" % (html.escape(title.group(1) if title else md_path.stem), CSS, body)
    )

    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "report.html"
        page.write_text(doc, encoding="utf-8")
        if pdf.exists():
            pdf.unlink()
        cmd = [
            find_browser(), "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
            "--user-data-dir=" + str(Path(tmp) / "profile"),
            "--no-pdf-header-footer", "--virtual-time-budget=30000",
            "--print-to-pdf=" + str(pdf), page.as_uri(),
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    if not pdf.exists():
        raise SystemExit("PDF was not written")
    print("wrote %s  (%.1f MB)" % (pdf.name, pdf.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
