# Create a Course

Courses organise the curriculum. Do not create one for every new subject.

## Create a course when

- several accepted lessons form a coherent thread, or the learner asks for a course on a topic;
- the grouping helps the learner navigate or see a progression;
- the topic is likely to keep growing.

A single unusual lesson can live in the closest sensible course until a real cluster emerges.

## Procedure

1. Review existing courses for a natural home first.
2. Choose a human-readable title and a **permanent** slug (lowercase letters, digits, hyphens), for example `jazz-harmony`. Lesson IDs are built from it, so do not rename it later.
3. Copy `templates/course.html` to `courses/<slug>/index.html` and replace every placeholder, including `data-progress-count="COURSE-SLUG"`.
4. Create `courses/<slug>/lessons/` and add the first lesson with `CREATE_LESSON.md` (numbering starts at `01`).
5. Describe the course in terms of concepts and goals, not a single source.
6. Choose a traversal style (ROADMAP, COURSE or PROJECT; see `docs/curriculum-design-research.md`) and say briefly on the course page how to move through it.
7. Add a course card to the root `index.html`: copy `templates/course-card.html` and set the `href`, lesson count, `data-progress-count` and `data-total`. The "Make it yours" callout can stay or be removed once the learner is settled.
8. Run `python3 tools/validate_site.py`.

Courses may evolve. Do not pretend the first taxonomy is permanent, but keep published slugs and lesson numbers stable.
