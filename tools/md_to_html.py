"""Convert the report Markdown to a styled HTML file that Word opens cleanly (then Word COM saves .docx/.pdf).

Uses the `markdown` package when present; otherwise a small built-in converter that covers what the
report uses: headings, paragraphs, bullet lists, pipe tables, horizontal rules, bold, italic, code, links.
"""
import html
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
text = src.read_text(encoding="utf-8")


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def fallback(md: str) -> str:
    out, para, table, in_list = [], [], [], False

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_table():
        nonlocal table
        if not table:
            return
        rows = [r for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
        cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
        if cells:
            out.append("<table>")
            out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr>")
            for r in cells[1:]:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</table>")
        table = []

    # Nested lists: a stack of (indent, tag). Each <li> stays open until its next sibling or
    # the end of its list, so a deeper list can sit inside it. Bullets (-, *) give <ul>,
    # "1." style markers give <ol>.
    stack = []

    def close_list(to_indent=-1):
        nonlocal in_list
        while stack and stack[-1][0] > to_indent:
            out.append(f"</li></{stack.pop()[1]}>")
        in_list = bool(stack)

    for line in md.splitlines():
        s = line.rstrip()
        if s.startswith("|"):
            flush_para(); close_list(); table.append(s); continue
        flush_table()
        if not s.strip():
            flush_para(); close_list(); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush_para(); close_list()
            lvl = len(m.group(1)); out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); continue
        if re.match(r"^-{3,}\s*$", s):
            flush_para(); close_list(); out.append("<hr/>"); continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", s)
        if m:
            flush_para()
            indent = len(m.group(1))
            tag = "ul" if m.group(2) in "-*" else "ol"
            close_list(indent)                      # leave any deeper lists
            if stack and stack[-1][0] == indent:
                if stack[-1][1] == tag:
                    out.append("</li>")             # next sibling
                else:
                    out.append(f"</li></{stack.pop()[1]}>")
            if not stack or stack[-1][0] < indent:
                out.append(f"<{tag}>"); stack.append((indent, tag))
            in_list = True
            out.append(f"<li>{inline(m.group(3))}"); continue
        if in_list and s.startswith("  "):
            out[-1] = out[-1] + " " + inline(s.strip()); continue
        close_list(); para.append(s.strip())
    flush_para(); flush_table(); close_list()
    return "\n".join(out)


try:
    import markdown  # type: ignore
    body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    engine = "markdown package"
except ImportError:
    body = fallback(text)
    engine = "built-in converter"

css = """
body { font-family: Georgia, 'Times New Roman', serif; font-size: 11pt; line-height: 1.35; }
h1 { font-family: Calibri, Arial, sans-serif; font-size: 20pt; color: #1f2a44; }
h2 { font-family: Calibri, Arial, sans-serif; font-size: 15pt; color: #1f2a44; margin-top: 18pt; }
h3 { font-family: Calibri, Arial, sans-serif; font-size: 12.5pt; color: #2b3a67; margin-top: 14pt; }
p { margin: 0 0 7pt 0; text-align: left; }
table { border-collapse: collapse; margin: 6pt 0 10pt 0; }
th, td { border: 1px solid #999999; padding: 3pt 5pt; vertical-align: top; font-family: Calibri, Arial, sans-serif; font-size: 9pt; }
th { background: #e8ebf2; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 9.5pt; }
hr { border: 0; border-top: 1px solid #bbbbbb; margin: 12pt 0; }
li { margin-bottom: 3pt; }
"""
_h1 = re.search(r"^#\s+(.+)$", text, flags=re.M)
title = html.escape(_h1.group(1).strip() if _h1 else src.stem, quote=False)
doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>{body}</body></html>"""
dst.write_text(doc, encoding="utf-8")
print(f"wrote {dst} ({len(doc)} chars) via {engine}")
