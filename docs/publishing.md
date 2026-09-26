# Publishing with GitHub Pages

The site is plain static files at the repository root, so there is nothing to build. Any static host works. These steps cover GitHub Pages.

## Option A (recommended): the included workflow

`.github/workflows/pages.yml` runs `tools/validate_site.py` on every push and pull request. On pushes to `main` it then publishes the site. A broken link or a lesson-ID mistake therefore stops the deploy instead of going live.

One-time setup:

1. Push your copy of the repository to GitHub.
2. **Settings → Pages → Build and deployment → Source:** choose **GitHub Actions**.
3. If you **forked** the repository: open the **Actions** tab and click the button that enables workflows. GitHub disables them on forks by default.
4. Push a commit to `main`, or run the workflow manually from **Actions → Validate and publish site → Run workflow**.
5. When it finishes, the site is at `https://<your-username>.github.io/<repository-name>/`. The workflow run shows the exact URL.

If the deploy job fails with a message about Pages not being enabled, step 2 has not been done yet.

## Option B: deploy from a branch (no Actions)

**Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**. GitHub serves the files as they are. The empty `.nojekyll` file stops GitHub from running Jekyll over them. You lose the automatic validation, so run `python3 tools/validate_site.py` yourself before pushing.

## Private repositories

GitHub Pages for private repositories depends on your GitHub plan. A published Pages site is public even when the repository is private, unless your plan supports access control. Check before publishing anything personal. Your learning profile (`curriculum/LEARNING_PROFILE.md`) is not linked from the site, but files in the repository root are reachable by URL once published.

## Paths

All internal links are relative, so the same files work:

- at `https://<user>.github.io/<repo>/` (a project site),
- at a custom domain root,
- when you open `index.html` directly from disk.

Never introduce root-absolute links like `/assets/...`. The validator rejects them.

## Previewing locally

```bash
python3 -m http.server 8000
# open http://localhost:8000/
```

Opening `index.html` directly also works. The only difference is that the browser cannot read `curriculum/PROGRESS.json` from disk, so only progress stored in the browser is shown.

## Checking a pull request before merging

Pull requests run the validation job but never deploy. To see changes rendered before merging, check out the branch locally and preview it as above.
