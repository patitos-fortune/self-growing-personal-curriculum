# Agent Instructions

These instructions are for any AI coding assistant working in this repository (Claude Code, Codex, Copilot, Cursor, ChatGPT with repository access, and so on). `CLAUDE.md` only points here, so this file is the single source of truth.

## What this repository is

A **self-growing personal curriculum**: a small static website of lessons, plus the learner profile, progress record and workflows that let an AI assistant help grow it over time.

- The **learner** owns the repository and decides what gets learned. You scout, propose, write and maintain.
- The curriculum should grow in the direction of the learner's actual interests and goals, which can be anything: software, music theory, a language, woodworking, statistics, history.
- It stays **lightweight**: static HTML/CSS plus one small JavaScript file, no framework, no build step, no database, no accounts, no server. Do not add any of these unless the learner explicitly asks for it and understands the trade-off.

Your job is not only to generate pages. Help the learner discover, understand, connect and keep ideas worth learning.

## Repository map

| Path | Purpose | Who edits it |
|---|---|---|
| `curriculum/LEARNING_PROFILE.md` | Interests, goals, experience, preferences | You, only with information the learner stated |
| `curriculum/CANDIDATES.md` | Staging area: scouted ideas and their editorial outcome | You, during scouting |
| `curriculum/PROGRESS.json` | Durable record of completed lessons | You, only on explicit learner report/export |
| `index.html` | Library home: one course card per course | You, when courses change |
| `courses/<slug>/index.html` | Course index: one lesson card per lesson | You, when lessons change |
| `courses/<slug>/lessons/NN.html` | Lessons | You |
| `progress.html` | Progress page (export/import/reset) | Rarely |
| `assets/css/style.css` | The only stylesheet | Rarely; reuse existing classes |
| `assets/js/progress.js` | Browser-side progress tracking | Rarely |
| `templates/` | Starting points for new courses and lessons | Rarely |
| `prompts/` | Step-by-step workflows (below) | Rarely |
| `tools/validate_site.py` | Structural checks; run after every change | Rarely |
| `docs/` | Human documentation | When behaviour changes |

## Workflows

| Situation | Follow |
|---|---|
| New learner / first session | "First run" below |
| "What should I learn next?" / "Find me topics about X" | `prompts/SCOUT.md` |
| Learner picked a candidate / asked for a lesson | `prompts/CREATE_LESSON.md` |
| A cluster of lessons needs its own course | `prompts/CREATE_COURSE.md` |
| Learner reports completion or gives a progress export | `prompts/UPDATE_PROGRESS.md` |
| Periodic tidy-up or "is my curriculum coherent?" | `prompts/REVIEW_CURRICULUM.md` |

## First run

When `curriculum/LEARNING_PROFILE.md` still contains the placeholder text:

1. Read this file, `README.md` and `curriculum/LEARNING_PROFILE.md`.
2. Ask the learner, briefly, only what materially affects the curriculum: what they want to learn, why (goal or project), what they already know, and how they like to learn. A one-line answer is enough to start.
3. Record what they said in the learning profile. Do not invent expertise, goals or preferences.
4. Ask whether to keep or remove the example course (`courses/example-learning-how-to-learn/`). If they want it removed, see "Removing the example course".
5. Optionally, suggest a starting shape (ROADMAP, COURSE or PROJECT; see `docs/curriculum-design-research.md`) and whether to rename the site title.
6. Scout with `prompts/SCOUT.md` and present candidates. Do not write lessons until the learner chooses, unless they explicitly ask you to go ahead.

## Research ideas vs. accepted curriculum

Keep these stages separate. This is what stops the curriculum from bloating:

**source → candidate (CANDIDATES.md) → learner decision → lesson (courses/) → progress (PROGRESS.json)**

- A scouted idea is a **candidate**, recorded in `curriculum/CANDIDATES.md`. It is not curriculum.
- Only a candidate that the learner accepted (or a lesson they asked for directly) becomes a lesson under `courses/`.
- Every candidate gets one editorial outcome:
  - **ADD**: a distinct, useful concept that deserves a new lesson;
  - **MERGE**: strengthens an existing lesson (name it);
  - **REFERENCE**: worth keeping as a source, but adds no lesson;
  - **REPLACE**: a clearly better source or treatment for an existing lesson (preserve provenance);
  - **SKIP**: no action. "Nothing worth adding" is a valid result.
- Before proposing ADD, check `CANDIDATES.md` and existing lesson titles so you don't propose something already covered, merged or skipped.

## Core educational rules

- Teach the **transferable concept**, not the source. Keep separate: what the source says or does; the general idea; how it works; why it matters; where else it applies.
- The learner should not need to install, clone, buy or run anything to understand a lesson.
- Sources can be anything credible and inspectable: open-source code, official documentation, textbooks, open courseware, papers, standards, reputable articles or talks. Pick what fits the subject.
- Ground source-specific claims in the actual source. Separate observed facts from your interpretation. If you could not verify something, say so in the lesson or choose a better source. Never invent citations, quotes, statistics or URLs.
- Connect to earlier lessons only when the connection genuinely helps (a prerequisite, contrast or bridge).
- Respect niche interests. Do not steer everyone toward the same generic syllabus.

## How content is represented

- A course is a folder `courses/<slug>/` (lowercase, hyphens) with an `index.html` and a `lessons/` folder.
- A lesson is `courses/<slug>/lessons/NN.html`, numbered from `01` per course with no gaps.
- **Lesson ID** = `<slug>/<NN>`, for example `spanish-basics/03`. It appears as `data-lesson-id` on the lesson's `<body>` and on its card in the course index. Progress is keyed by it.
- **IDs and numbers are permanent once published.** Never renumber, rename a published course slug, or reuse a number for different content. Add new lessons at the end. If order matters, explain the recommended path on the course index instead of renumbering.
- The course index card and the lesson header must use the same title and duration (the validator checks this).
- All internal links are relative (`../index.html`, never `/index.html`) so the site works at `https://<user>.github.io/<repo>/` and when opened from disk.
- Use existing CSS classes from `assets/css/style.css`. No per-page `<style>` blocks, external fonts, CDNs, trackers or remote images. Draw diagrams as HTML tables or inline SVG.

## Adding a lesson (summary; details in `prompts/CREATE_LESSON.md`)

1. Copy `templates/lesson.html` to `courses/<slug>/lessons/NN.html` (next free number).
2. Replace every placeholder, including `data-lesson-id`.
3. Add its card to `courses/<slug>/index.html` (copy an existing card) and update that page's lesson count.
4. Set Previous/Next: the new lesson links back to the previous lesson, and the previous lesson's disabled "Next" becomes a link to the new one.
5. Update the lesson count on the course card in the root `index.html`.
6. Record the outcome in `curriculum/CANDIDATES.md` if the lesson came from a candidate.
7. Run `python3 tools/validate_site.py`.

## Preserving existing work

- Do not delete, rewrite or reorder existing lessons to make new ones fit. Propose the change and let the learner decide.
- If a credible new source contradicts an existing lesson, add a dated note to that lesson and cite both sources. Do not silently rewrite the earlier claim.
- Never remove records from `curriculum/PROGRESS.json` unless the learner explicitly asks, or the lesson itself is being deleted at their request.
- Never overwrite `LEARNING_PROFILE.md` wholesale. Edit the relevant lines.

## Progress tracking

- On the site, **Mark as read** saves to the reader's browser (`localStorage`). That is per browser and per device. See `docs/progress-tracking.md`.
- `curriculum/PROGRESS.json` is the durable, portable record in Git. The site reads it and shows those lessons as read on every device.
- Only explicit learner action counts as completion. Delivered, opened, completed and mastered are different things. Never infer mastery.
- To merge a browser export (`learning-progress.json`) into the repository, follow `prompts/UPDATE_PROGRESS.md`.
- If you delete a lesson at the learner's request, remove its records from `PROGRESS.json` too (the validator flags unknown IDs).

## Removing the example course

The template ships with `courses/example-learning-how-to-learn/` to show the format. When the learner no longer wants it:

1. Delete the `courses/example-learning-how-to-learn/` folder.
2. Remove its course card from `index.html`. Keep the "Make it yours" callout: it is the empty state.
3. Remove any `example-learning-how-to-learn/...` records from `curriculum/PROGRESS.json`.
4. Run the validator.

## Testing after changes

Always run:

```bash
python3 tools/validate_site.py
```

It must end with `RESULT: PASS`. Then, if you can, preview the site locally with `python3 -m http.server 8000` and open the pages you changed, including on a narrow (phone-width) window. On GitHub, the Pages workflow runs the same validator and refuses to deploy if it fails.

## Human agency

The learner is the curator. Offer choices rather than making silent decisions. Keep your changes small, explain what you changed, and let the learner review it before it is merged or published.
