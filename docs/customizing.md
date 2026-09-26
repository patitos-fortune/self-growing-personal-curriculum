# Customizing the name and look

The template ships with a **Patitos Fortune** default theme: the duck logo, "by Patitos Fortune" byline and warm orange palette. You can use it as it is. Rebranding changes presentation only, never the curriculum engine. Lesson IDs, course slugs, the progress storage key and `PROGRESS.json` contain no brand name, so your lessons and progress are unaffected.

## The quick way

```bash
python3 tools/rebrand.py --name "My Learning Library" --byline "by Your Name"
python3 tools/rebrand.py --logo path/to/logo.svg      # optional
python3 tools/rebrand.py --byline ""                  # optional: no byline
python3 tools/validate_site.py
```

Add `--dry-run` to preview. Or ask your AI assistant: *"Rebrand the site as 'My Learning Library' by Your Name using tools/rebrand.py, and update the README header."*

## Where the branding lives

| What | Where | How to change |
|---|---|---|
| Site name | `<span class="brand-name">` in every page and template, and inside `<title>` | `tools/rebrand.py --name` |
| Byline ("by Patitos Fortune") | `<span class="brand-byline">` in every page and template | `tools/rebrand.py --byline` |
| Logo and favicon (duck) | `assets/brand/logo.svg`, referenced by every page | Replace the file, or `tools/rebrand.py --logo` |
| Colours and fonts | Variables at the top of `assets/css/style.css` (`--color-accent`, `--color-bg`, `--font-head`, ...) | Edit by hand, and keep text contrast at WCAG AA (4.5:1) |
| Home tagline | `.home-subtitle` in `index.html` | Edit by hand |
| README header | Logo, title and byline at the top of `README.md` | Edit by hand |
| Copyright | `LICENSE` | Add your own name for your changes, and keep the original notice as MIT requires |

## Keeping it fork-friendly

- Don't put the brand into course slugs, lesson IDs, file names or JavaScript. The engine stays neutral on purpose.
- Pages hold the brand in the same few elements everywhere. When you add pages by hand, copy the header and footer from `templates/` so the rebrand tool can find them.
