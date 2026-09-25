# Create a Course

Courses organize an emerging curriculum. Do not create a new course for every new subject.

## Create a course when

- several lessons form a coherent conceptual thread;
- the grouping helps the learner navigate or understand progression;
- the topic is likely to continue growing.

A single unusual lesson can remain in the closest sensible course until a real cluster emerges.

## Procedure

1. Review existing courses for a natural home.
2. Choose a concise human-readable title and URL-safe slug.
3. Copy `templates/course.html` to `courses/<slug>/index.html`.
4. Create `courses/<slug>/lessons/`.
5. Describe the course around concepts and learning goals, not around a specific repository.
6. Add the course card to the root `index.html`.
7. Start lesson numbering at `01`.
8. Keep numbering permanent after publication.
9. Run `python3 tools/validate_site.py`.

Courses may evolve organically. Avoid pretending the initial taxonomy is permanent.
