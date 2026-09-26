<p align="center"><img src="assets/brand/logo.svg" alt="Patitos Fortune duck" width="96"></p>

<h1 align="center">Self-Growing Personal Curriculum</h1>

<p align="center"><strong>A Patitos Fortune template</strong></p>

A template for a **personal learning library that you grow with an AI coding assistant**. You tell the assistant what you want to learn. It suggests topics backed by real sources, writes short self-contained lessons for the ones you pick, and keeps the curriculum coherent over time. The result is a small static website you can read on your phone and publish free on GitHub Pages.

- **Any subject:** programming, maths, music, languages, history, crafts.
- **You curate:** the assistant proposes, and nothing becomes a lesson until you accept it.
- **Plain files:** HTML, CSS, one small JavaScript file for progress, and Markdown instructions. No framework, build step, database, accounts or server.
- **Works with any capable AI assistant:** the rules live in [`AGENTS.md`](AGENTS.md), not in one provider's memory.
- **Tracks what you've read:** click **Mark as read**. Progress lives in your browser and, if you want, in a JSON file committed to the repository.

It includes a two-lesson example course so you can see the format before you start. It ships with the Patitos Fortune look (duck logo, warm palette), and you can keep it or rebrand in one command. See [Customizing](#customizing).

## Get started in 5 minutes

**1. Make your own copy.** Click **Use this template** (or **Fork**) on GitHub, or clone it:

```bash
git clone https://github.com/<you>/<your-copy>.git
cd <your-copy>
```

**2. Open it with your AI coding assistant** (Claude Code, Codex, GitHub Copilot, Cursor, ...) and say something like:

> Read AGENTS.md and follow its first-run steps. I want to learn **[X, Y and Z]**. My goal is **[why]**. I already know **[background]**. Help me set up my learning profile and suggest my first topics. Don't write lessons until I pick.

The assistant fills in `curriculum/LEARNING_PROFILE.md`, asks whether to keep the example course, and proposes candidate topics with sources.

**3. Pick what interests you.**

> I'll take candidates 1 and 3. Write the lessons.

It writes the lessons, links them into the site and runs the validator.

**4. Read it.** Open `index.html` in a browser, or preview it properly:

```bash
python3 -m http.server 8000   # then open http://localhost:8000/
```

**5. Publish it** (optional): in your GitHub repository go to **Settings → Pages → Source: GitHub Actions** and push to `main`. Your site appears at `https://<you>.github.io/<your-copy>/`. Details, including forks and private repositories, are in [docs/publishing.md](docs/publishing.md).

**6. Keep growing it.** Come back whenever you like:

> Read AGENTS.md. Suggest what I should learn next, based on my profile and what I've read.

More ready-to-use prompts: [docs/starter-prompts.md](docs/starter-prompts.md).

## How the curriculum grows

```text
your interests ─► scouting ─► candidates ─► you choose ─► lessons ─► progress
 (LEARNING_       (prompts/    (CANDIDATES   (ADD/MERGE/    (courses/)  (PROGRESS.json
  PROFILE.md)      SCOUT.md)    .md)          SKIP...)                   + browser)
```

- **Scouting** finds concepts worth learning, each tied to a credible source: open-source code, documentation, textbooks, papers or reputable articles, depending on the subject.
- **Candidates** are recorded in `curriculum/CANDIDATES.md` with an explicit outcome (ADD, MERGE, REFERENCE, REPLACE or SKIP). This keeps research ideas separate from accepted lessons and stops the assistant from proposing the same thing twice.
- **Lessons** follow a fixed shape: what you're learning, why it matters, the idea, a worked example, sources, a self-check exercise with a hidden answer, and takeaways. Each lesson makes sense without installing or opening its sources.
- **Existing work is preserved:** lesson numbers and IDs never change once published, and the assistant proposes changes to older lessons instead of silently rewriting them.

The full rules for assistants are in [`AGENTS.md`](AGENTS.md). Step-by-step workflows are in [`prompts/`](prompts/).

## Reading progress

Every lesson has a **Mark as read** button, and the **Progress** page lists what you've read.

| Where | What | Limits |
|---|---|---|
| Your browser (`localStorage`) | Updated instantly when you click | This browser and device only. Lost if site data is cleared |
| `curriculum/PROGRESS.json` | The durable record in Git. The published site shows these as read everywhere | Updated through a commit, usually by your assistant |

To make browser progress permanent, export it from the Progress page and ask your assistant to merge it. To move between devices without Git, export on one and import on the other. There are no accounts and no server, and nothing is sent anywhere. See [docs/progress-tracking.md](docs/progress-tracking.md).

## Repository layout

```text
.
├── AGENTS.md                  Rules and workflows for AI assistants (CLAUDE.md points here)
├── README.md
├── index.html                 Library home: one card per course
├── progress.html              Progress page: list, export, import, reset
├── assets/
│   ├── brand/logo.svg         Default logo and favicon (Patitos Fortune duck)
│   ├── css/style.css          The only stylesheet; brand colours at the top
│   └── js/progress.js         Mark-as-read and progress (the only script)
├── courses/
│   └── <course-slug>/
│       ├── index.html         Course index: one card per lesson
│       └── lessons/01.html…   Lessons; ID = <course-slug>/<NN>
├── curriculum/
│   ├── LEARNING_PROFILE.md    Your interests, goals, background, preferences
│   ├── CANDIDATES.md          Scouted ideas and decisions (not published lessons)
│   └── PROGRESS.json          Durable reading progress
├── prompts/                   SCOUT, CREATE_LESSON, CREATE_COURSE, UPDATE_PROGRESS, REVIEW_CURRICULUM
├── templates/                 lesson.html, course.html, course-card.html starting points
├── docs/                      Publishing, progress, customizing, starter prompts, design research
├── tools/validate_site.py     Structural checks (Python 3 standard library only)
├── tools/rebrand.py           Rename or rebrand the site in one step
└── .github/workflows/pages.yml  Validates every push/PR; deploys main to GitHub Pages
```

## Checking your changes

```bash
python3 tools/validate_site.py
```

It checks links, relative paths, lesson numbering and IDs, Previous/Next navigation, title and duration consistency between course indexes and lessons, leftover template placeholders, and `PROGRESS.json`. The GitHub workflow runs it on every push and pull request and will not deploy a failing site. It checks structure, not facts, so read what your assistant writes.

## Customizing

- **Name, byline, logo:** the default presentation is Patitos Fortune branded. Run `python3 tools/rebrand.py --name "My Library" --byline "by Me"` (and optionally `--logo`). Colours are variables at the top of `assets/css/style.css`. Branding never touches lesson IDs or progress. Full list of what to change: [docs/customizing.md](docs/customizing.md).
- **Curriculum shape:** ROADMAP (explore connected topics), COURSE (ordered path) or PROJECT (learn by building). See [docs/curriculum-design-research.md](docs/curriculum-design-research.md).
- **Adding lessons by hand:** copy `templates/lesson.html`, follow [prompts/CREATE_LESSON.md](prompts/CREATE_LESSON.md), and run the validator.

## Design principles

- **Personal relevance over generic coverage.** Follow the learner's curiosity, including niche interests.
- **Grounded in real sources.** Separate what a source says from interpretation, and never invent citations.
- **Curate, don't accumulate.** "Nothing worth adding" is a valid outcome.
- **Understanding before installation.** Every lesson stands on its own.
- **Portable and static.** Plain files you own, readable offline, hostable anywhere.

## FAQ

**Do I need to know how to code?** Not really. You need a GitHub account and an AI assistant that can edit files in a repository. The assistant does the HTML.

**Does it need an API key or a specific AI provider?** No. The site never calls an AI. You use whichever assistant you like to edit the repository.

**Is my learning profile public?** If your repository is public, yes, like every other file in it. Keep sensitive details out of it, or use a private repository (see [docs/publishing.md](docs/publishing.md) for how Pages behaves with private repositories).

**Can I use it without GitHub?** Yes. It's a folder of static files. Open `index.html` locally or upload it to any static host.

## License

MIT. See [LICENSE](LICENSE).
