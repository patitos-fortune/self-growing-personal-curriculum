#!/usr/bin/env python3
"""Validate the static self-growing curriculum across every course."""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
COURSES = ROOT / "courses"
errors=[]; warnings=[]
def err(x): errors.append(x)
def warn(x): warnings.append(x)
def external(x): return x.startswith(("http://","https://","mailto:","#","//"))
def html_files(): return sorted(ROOT.rglob("*.html"))
def validate_course(course):
    idx=course/"index.html"; lessons=course/"lessons"
    if not idx.exists(): err(f"{course.relative_to(ROOT)}: missing index.html"); return
    if not lessons.exists(): err(f"{course.relative_to(ROOT)}: missing lessons/"); return
    text=idx.read_text(encoding="utf-8")
    refs=sorted({int(x) for x in re.findall(r'lessons/(\d+)\.html',text)})
    files=sorted(int(f.stem) for f in lessons.glob("*.html") if f.stem.isdigit())
    if refs:
        expected=list(range(1,max(refs)+1))
        if refs != expected: err(f"{course.name}: course index numbering has gaps: {refs}")
        if files != expected: err(f"{course.name}: lesson files do not match 01..{max(refs):02d}: {files}")
    elif files: warn(f"{course.name}: lesson files exist but index references none")
    for f in lessons.glob("*.html"):
        t=f.read_text(encoding="utf-8")
        if "../index.html" not in t: err(f"{f.relative_to(ROOT)}: missing course-index link")
        if "../../../index.html" not in t: err(f"{f.relative_to(ROOT)}: missing library-home link")
        if "lesson-nav" not in t: err(f"{f.relative_to(ROOT)}: missing lesson-nav")
        if "<details>" not in t or "<summary>" not in t: warn(f"{f.relative_to(ROOT)}: no reveal-answer details block")
def main():
    if COURSES.exists():
        for c in sorted(x for x in COURSES.iterdir() if x.is_dir()): validate_course(c)
    for p in html_files():
        t=p.read_text(encoding="utf-8")
        if "localhost" in t or "127.0.0.1" in t: err(f"{p.relative_to(ROOT)}: localhost reference")
        for bad in [r"C:\\","/home/","/Users/","file://"]:
            if bad in t: err(f"{p.relative_to(ROOT)}: absolute filesystem path {bad}")
        for m in re.finditer(r'(?:href|src)="(/[^/"][^"]*)"',t):
            err(f"{p.relative_to(ROOT)}: absolute-root path {m.group(1)!r}; use relative paths")
        for ref in re.findall(r'(?:href|src)="([^"]+)"',t):
            if external(ref): continue
            part=ref.split("#")[0]
            if part and not (p.parent/part).resolve().exists():
                err(f"{p.relative_to(ROOT)}: broken reference {ref!r}")
    print(f"VALIDATION REPORT — {len(errors)} error(s), {len(warnings)} warning(s)")
    for x in warnings: print("WARNING:",x)
    for x in errors: print("ERROR:",x)
    print("RESULT:","FAIL" if errors else "PASS")
    return 1 if errors else 0
if __name__=="__main__": sys.exit(main())
