#!/usr/bin/env python3
"""Rename or rebrand the site in one step.

The shipped default is "Self-Growing Personal Curriculum" by Patitos Fortune,
with a duck logo. Branding lives only in presentation markup, never in lesson
IDs, storage keys or course slugs, so it can be replaced safely.

Examples:
    python3 tools/rebrand.py --name "Ada's Library" --byline "by Ada Lovelace"
    python3 tools/rebrand.py --byline ""                  # remove the byline
    python3 tools/rebrand.py --logo ~/my-logo.svg         # replace the logo
    python3 tools/rebrand.py --name "My Notes" --dry-run  # preview only

What it changes in every page and template:
    <span class="brand-name">…</span>     site name (header, home title, footer)
    <span class="brand-byline">…</span>   byline ("by Patitos Fortune")
    the site name inside <title>…</title>
    assets/brand/logo.<ext> and references to it (with --logo)

Colours are CSS variables at the top of assets/css/style.css, and the README
is Markdown; edit those by hand (see docs/customizing.md).
"""
import argparse
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules", "_site"}


def pages():
    return [p for p in sorted(ROOT.rglob("*.html")) if not SKIP.intersection(p.relative_to(ROOT).parts)]


def current(cls):
    m = re.search(rf'<span class="{cls}">(.*?)</span>', (ROOT / "index.html").read_text(encoding="utf-8"), re.S)
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", help="new site name")
    ap.add_argument("--byline", help='new byline, e.g. "by Ada"; use "" to remove it')
    ap.add_argument("--logo", help="path to a new logo image (SVG recommended; PNG/WebP also work)")
    ap.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    a = ap.parse_args()
    if a.name is None and a.byline is None and a.logo is None:
        ap.error("nothing to do: pass --name, --byline and/or --logo")

    old_name = current("brand-name")
    if old_name is None:
        sys.exit("index.html has no <span class=\"brand-name\">; cannot detect the current name.")
    new_name = html.escape(a.name, quote=False) if a.name is not None else None
    new_byline = html.escape(a.byline, quote=False) if a.byline is not None else None

    old_logo = next(iter(sorted((ROOT / "assets/brand").glob("logo.*"))), None)
    new_logo_name = None
    if a.logo:
        src = Path(a.logo).expanduser()
        if not src.is_file():
            sys.exit(f"logo not found: {src}")
        new_logo_name = "logo" + src.suffix.lower()

    changed = []
    for p in pages():
        s = p.read_text(encoding="utf-8")
        t = s
        if new_name is not None:
            t = re.sub(r'(<span class="brand-name">).*?(</span>)', lambda m: m.group(1) + new_name + m.group(2), t, flags=re.S)
            t = re.sub(r"(<title>)(.*?)(</title>)", lambda m: m.group(1) + m.group(2).replace(old_name, new_name) + m.group(3), t, flags=re.S)
        if new_byline is not None:
            t = re.sub(r'(<span class="brand-byline">).*?(</span>)', lambda m: m.group(1) + new_byline + m.group(2), t, flags=re.S)
        if new_logo_name and old_logo is not None:
            t = t.replace("assets/brand/" + old_logo.name, "assets/brand/" + new_logo_name)
        if t != s:
            changed.append(p.relative_to(ROOT).as_posix())
            if not a.dry_run:
                p.write_text(t, encoding="utf-8")

    if new_logo_name:
        dest = ROOT / "assets/brand" / new_logo_name
        if not a.dry_run:
            if old_logo is not None and old_logo.name != new_logo_name:
                old_logo.unlink()
            shutil.copyfile(Path(a.logo).expanduser(), dest)
        changed.append(dest.relative_to(ROOT).as_posix())

    verb = "Would change" if a.dry_run else "Changed"
    print(f"{verb} {len(changed)} file(s):")
    for c in changed:
        print("  " + c)
    if not a.dry_run:
        print("Next: update README.md by hand if you like, then run python3 tools/validate_site.py")


if __name__ == "__main__":
    main()
