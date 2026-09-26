#!/usr/bin/env python3
"""Validate the static curriculum site.

Run from anywhere:

    python3 tools/validate_site.py

Checks (errors fail the run, warnings do not):

* every internal href/src resolves; no localhost, filesystem or root-absolute
  paths (root-absolute paths break on GitHub Pages project URLs);
* every course has index.html + lessons/, lesson files are 01..NN with no gaps,
  and the course index links every lesson exactly once;
* every lesson declares data-lesson-id="<course-slug>/<NN>" matching its path,
  links to its course index and the library home, has a lesson-nav block with
  correct Previous/Next links, and no leftover template placeholders;
* lesson titles and durations match the course index cards;
* every course is linked from the root index.html;
* curriculum/PROGRESS.json is well formed and only references real lessons.

Only the Python standard library is used. templates/ is skipped because its
relative paths are written for their final location under courses/.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES = ROOT / "courses"
PROGRESS = ROOT / "curriculum" / "PROGRESS.json"
SKIP_DIRS = {".git", "templates", "node_modules", "_site"}
PLACEHOLDERS = ["LESSON TITLE", "COURSE TITLE", "COURSE-SLUG", "ONE-SENTENCE TAGLINE",
                ">CONTENT<", "TAKEAWAY<", "LESSON DESCRIPTION", "COURSE DESCRIPTION"]
LESSON_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*/\d{2,}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errors, warnings = [], []
def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)
def rel(p): return p.relative_to(ROOT).as_posix()
def external(ref): return ref.startswith(("http://", "https://", "mailto:", "#", "//", "data:"))
def text_of(fragment): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def site_html_files():
    for p in sorted(ROOT.rglob("*.html")):
        if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts):
            yield p


def check_paths(p, t):
    if "localhost" in t or "127.0.0.1" in t:
        err(f"{rel(p)}: localhost reference")
    for bad in ["C:\\", "/home/", "/Users/", "file://"]:
        if bad in t:
            err(f"{rel(p)}: absolute filesystem path {bad!r}")
    for m in re.finditer(r'(?:href|src)="(/[^/"][^"]*)"', t):
        err(f"{rel(p)}: root-absolute path {m.group(1)!r}; use a relative path")
    for ref in re.findall(r'(?:href|src)="([^"]+)"', t):
        if external(ref):
            continue
        part = ref.split("#")[0].split("?")[0]
        if part and not (p.parent / part).resolve().exists():
            err(f"{rel(p)}: broken reference {ref!r}")


def lesson_cards(index_text):
    """Return {number: (card_html, data_lesson_id)} for lesson cards in a course index."""
    cards = {}
    for m in re.finditer(r'<a\b([^>]*\bhref="lessons/(\d+)\.html"[^>]*)>(.*?)</a>', index_text, re.S):
        attrs, num, body = m.group(1), int(m.group(2)), m.group(3)
        if num in cards:
            err(f"course index links lessons/{m.group(2)}.html more than once")
        lid = re.search(r'data-lesson-id="([^"]+)"', attrs)
        cards[num] = (body, lid.group(1) if lid else None)
    return cards


def validate_course(course, lesson_ids):
    slug = course.name
    idx, lessons = course / "index.html", course / "lessons"
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        err(f"courses/{slug}: slug must be lowercase letters, digits and hyphens")
    if not idx.exists():
        err(f"courses/{slug}: missing index.html"); return
    if not lessons.is_dir():
        err(f"courses/{slug}: missing lessons/ folder"); return
    index_text = idx.read_text(encoding="utf-8")
    cards = lesson_cards(index_text)
    files = {}
    for f in lessons.glob("*.html"):
        if not re.fullmatch(r"\d{2,}", f.stem):
            err(f"{rel(f)}: lesson files must be named NN.html (01.html, 02.html, ...)"); continue
        files[int(f.stem)] = f
    nums = sorted(files)
    if nums and nums != list(range(1, len(nums) + 1)):
        err(f"courses/{slug}: lesson files are not a continuous 01..NN sequence: {nums}")
    if sorted(cards) != nums:
        err(f"courses/{slug}: course index links lessons {sorted(cards)} but files exist for {nums}")
    if f'data-progress-count="{slug}"' not in index_text and nums:
        warn(f"courses/{slug}/index.html: no data-progress-count=\"{slug}\" element (progress summary hidden)")
    last = max(nums) if nums else 0
    for n, f in sorted(files.items()):
        t = f.read_text(encoding="utf-8")
        name = rel(f)
        expected_id = f"{slug}/{f.stem}"
        m = re.search(r'<body[^>]*\bdata-lesson-id="([^"]+)"', t)
        if not m:
            err(f"{name}: <body> is missing data-lesson-id=\"{expected_id}\"")
        elif m.group(1) != expected_id:
            err(f"{name}: data-lesson-id is {m.group(1)!r}, expected {expected_id!r} (IDs follow the file path)")
        lesson_ids.add(expected_id)
        for needle, what in [('href="../index.html"', "course-index link"),
                             ('href="../../../index.html"', "library-home link"),
                             ('class="lesson-nav"', "lesson-nav block"),
                             ('../../../assets/js/progress.js', "progress.js script")]:
            if needle not in t:
                err(f"{name}: missing {what}")
        if "data-progress-toggle" not in t:
            warn(f"{name}: no Mark as read button")
        if "<details" not in t or "<summary" not in t:
            warn(f"{name}: no <details>/<summary> reveal-answer block")
        for ph in PLACEHOLDERS:
            if ph in t:
                err(f"{name}: leftover template placeholder {ph!r}")
        nav = re.search(r'<nav class="lesson-nav">(.*?)</nav>', t, re.S)
        if nav:
            links = re.findall(r'href="(\d+)\.html"', nav.group(1))
            want = [x for x in (n - 1, n + 1) if 1 <= x <= last]
            got = sorted({int(x) for x in links})
            if got != want:
                err(f"{name}: Previous/Next links point to {got}, expected {want}")
        # Title / duration consistency with the course index card.
        if n in cards:
            body, card_id = cards[n]
            if card_id != expected_id:
                err(f"courses/{slug}/index.html: card for lessons/{f.stem}.html needs data-lesson-id=\"{expected_id}\"")
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
            ct = re.search(r'class="lesson-title"[^>]*>(.*?)</', body, re.S)
            if h1 and ct and text_of(h1.group(1)) != text_of(ct.group(1)):
                err(f"{name}: title {text_of(h1.group(1))!r} differs from course index {text_of(ct.group(1))!r}")
            ld = re.search(r'class="duration-badge"[^>]*>(.*?)</', t, re.S)
            cd = re.search(r'class="lesson-duration"[^>]*>(.*?)</', body, re.S)
            if ld and cd and text_of(ld.group(1)) != text_of(cd.group(1)):
                err(f"{name}: duration {text_of(ld.group(1))!r} differs from course index {text_of(cd.group(1))!r}")


def validate_progress(lesson_ids):
    if not PROGRESS.exists():
        err("curriculum/PROGRESS.json is missing"); return
    try:
        data = json.loads(PROGRESS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"curriculum/PROGRESS.json is not valid JSON: {e}"); return
    if data.get("version") != 1:
        err("curriculum/PROGRESS.json: expected \"version\": 1")
    seen = set()
    for i, rec in enumerate(data.get("completed", [])):
        if not isinstance(rec, dict) or not isinstance(rec.get("lesson"), str):
            err(f"curriculum/PROGRESS.json: completed[{i}] must be an object with a \"lesson\" string"); continue
        lid = rec["lesson"]
        if not LESSON_ID.match(lid):
            err(f"curriculum/PROGRESS.json: malformed lesson ID {lid!r}")
        elif lid not in lesson_ids:
            err(f"curriculum/PROGRESS.json: {lid!r} does not match any lesson in courses/")
        if lid in seen:
            err(f"curriculum/PROGRESS.json: duplicate record for {lid!r}")
        seen.add(lid)
        if "completed" in rec and not (isinstance(rec["completed"], str) and DATE.match(rec["completed"])):
            err(f"curriculum/PROGRESS.json: {lid!r} completed date must be YYYY-MM-DD")


def main():
    lesson_ids = set()
    home = ROOT / "index.html"
    home_text = home.read_text(encoding="utf-8") if home.exists() else ""
    if not home_text:
        err("index.html (library home) is missing")
    if COURSES.exists():
        for c in sorted(x for x in COURSES.iterdir() if x.is_dir()):
            validate_course(c, lesson_ids)
            if f'courses/{c.name}/index.html' not in home_text:
                err(f"index.html does not link courses/{c.name}/index.html")
    for p in site_html_files():
        check_paths(p, p.read_text(encoding="utf-8"))
    validate_progress(lesson_ids)
    courses = len([c for c in COURSES.iterdir() if c.is_dir()]) if COURSES.exists() else 0
    print(f"Checked {courses} course(s), {len(lesson_ids)} lesson(s).")
    print(f"VALIDATION REPORT — {len(errors)} error(s), {len(warnings)} warning(s)")
    for x in warnings:
        print("WARNING:", x)
    for x in errors:
        print("ERROR:", x)
    print("RESULT:", "FAIL" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
