"""Render every HTML file in a folder to a PNG with headless Chrome or Edge.

Usage:  python render_pictures.py <src_dir> <out_dir> [name-filter]

Each HTML file sets its own size with a meta tag in <head>:
    <meta name="shot" content="393x852@3">      width x height @ device scale
Default when the tag is missing: 1200x800@2.
Only the standard library is used.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CANDIDATES = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    raise SystemExit("No Chrome or Edge found; set CHROME to its path.")


def shot_size(html_text):
    m = re.search(r'<meta\s+name="shot"\s+content="(\d+)x(\d+)(?:@([\d.]+))?"', html_text)
    if not m:
        return 1200, 800, 2.0
    return int(m.group(1)), int(m.group(2)), float(m.group(3) or 2)


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    name_filter = sys.argv[3] if len(sys.argv) > 3 else ""
    out.mkdir(parents=True, exist_ok=True)
    browser = find_browser()
    files = sorted(p for p in src.glob("*.html") if name_filter in p.name)
    if not files:
        raise SystemExit("No HTML files matched in " + str(src))
    for f in files:
        w, h, s = shot_size(f.read_text(encoding="utf-8"))
        png = out / (f.stem + ".png")
        if png.exists():
            png.unlink()
        with tempfile.TemporaryDirectory() as profile:
            cmd = [
                browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--no-first-run", "--no-default-browser-check",
                "--user-data-dir=" + profile,
                "--window-size=%d,%d" % (w, h),
                "--force-device-scale-factor=%g" % s,
                "--virtual-time-budget=4000",
                "--screenshot=" + str(png),
                f.as_uri(),
            ]
            try:
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
            except subprocess.TimeoutExpired:
                print("TIMEOUT  " + f.name)
                continue
        if png.exists():
            print("ok       %-44s %dx%d@%g  %d KB" % (png.name, w, h, s, png.stat().st_size // 1024))
        else:
            print("FAILED   " + f.name)


if __name__ == "__main__":
    main()
