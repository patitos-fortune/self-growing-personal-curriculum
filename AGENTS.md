# Agent Instructions

This repository is a self-growing personal curriculum. Your job is not merely to generate pages. Your job is to help the learner discover, understand, connect, and preserve ideas worth learning.

## First-run workflow

When the learner is new:

1. Read this file and `README.md`.
2. Read `curriculum/LEARNING_PROFILE.md`.
3. Ask only for missing information that materially affects useful scouting. A short statement of interests is enough to begin.
4. Update the learning profile with explicit information the learner provides. Do not invent expertise, goals, projects, or preferences.
5. Read the existing course indexes and lesson titles.
6. Follow `prompts/SCOUT.md`.
7. Present candidate topics before creating lessons unless the learner explicitly asks you to create one.

## Core educational rule

Teach the **transferable concept**, not the source repository.

Keep these distinct:
1. what the source project actually does;
2. the general concept it demonstrates;
3. how the concept works;
4. why the concept matters;
5. where else it can apply.

The learner must not need to install, clone, or run the source project to understand the lesson.

## Curriculum continuity

Before creating a lesson, inspect the existing curriculum for:
- prerequisites;
- concepts already covered;
- useful contrasts;
- natural follow-on ideas;
- connections that genuinely improve understanding.

Reference earlier lessons when useful. Never manufacture a connection merely to make the curriculum look interconnected.

## Source discipline

For source-driven lessons, inspect the real repository and relevant documentation/code before making repository-specific claims. Separate observed facts from interpretation. If evidence is insufficient, say so or choose a better source.

A repository may produce:
- one strong lesson;
- several distinct lessons;
- a candidate for later;
- or no lesson at all.

"No worthwhile lesson here" is an acceptable result.

## Knowledge evolution

Treat scouting as a staging layer, not automatic publication:

**source → candidate concept → learner selection → lesson → curriculum**

Do not let an interesting source silently become canonical curriculum.

If a credible new source materially conflicts with an existing lesson, preserve the disagreement and provenance. Flag the lesson for review rather than silently rewriting the earlier claim. Prefer dated/source-attributed notes when the disagreement matters.

## Writing lessons

Follow `prompts/CREATE_LESSON.md` and `templates/lesson.html`.

Lessons should be self-contained, readable on a phone, concrete rather than abstract, and generally suitable for a focused sitting. Include a worked example, a mental exercise with a revealable answer, source attribution, and concise takeaways.

## Creating courses

Follow `prompts/CREATE_COURSE.md`. Courses are organizational containers, not rigid academic departments. Create a new course only when a coherent cluster has emerged.

## Review

Periodically follow `prompts/REVIEW_CURRICULUM.md` to detect duplication, missing bridges, stale profile assumptions, and emerging areas of interest.

## Reading progress

Reading progress has two layers:

- browser-local interaction in `assets/js/progress.js` for immediate static-site controls;
- durable, portable state in `curriculum/PROGRESS.json`.

Follow `prompts/UPDATE_PROGRESS.md` when the learner reports completion or provides an exported progress file. Never equate delivery, opening, completion, and mastery.

Every published lesson must have a stable ID in the form `course-slug/NN`. Do not change an ID after publication.

## Structural rules

- Keep the site static HTML/CSS unless the learner explicitly chooses a more complex architecture.
- Keep internal links relative so GitHub Pages project URLs work.
- Keep shared styling in `assets/css/style.css`.
- Lesson files live at `courses/<slug>/lessons/NN.html`.
- Lesson numbering is permanent within a course.
- Update course indexes and Previous/Next navigation when adding lessons.
- Run `python3 tools/validate_site.py` after structural changes.
- Do not silently rewrite existing lesson content merely to make a new lesson fit.

## Human agency

The learner is the curator. Suggestions should expand choice, not silently decide the curriculum. Preserve unusual or niche interests rather than normalizing everyone toward the same generic software syllabus.
