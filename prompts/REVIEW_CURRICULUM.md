# Review the Curriculum

Use this periodically, or when the learner asks what to learn next or whether the curriculum still makes sense.

## Read

The learning profile, `curriculum/CANDIDATES.md`, `curriculum/PROGRESS.json`, the course indexes, and lesson content where needed.

## Look for

- duplicated concepts across lessons or courses;
- lessons that should mention each other, and missing prerequisites or bridges;
- isolated lessons that now form a cluster worth its own course;
- courses whose scope has drifted;
- candidates left as `PROPOSED` for a long time (ask whether to decide or drop them);
- recurring choices that suggest an emerging interest the profile does not yet mention;
- profile statements that look stale (ask; do not rewrite on speculation);
- credible newer sources that contradict or supersede claims in existing lessons;
- broken or stale source links;
- lessons read long ago that might deserve a short recap or review exercise.

## Rules

- Do not renumber, rename or reorder published lessons for tidiness. IDs are permanent.
- When sources disagree, preserve both with dates and citations. Do not silently overwrite.
- Do not force every lesson into one dependency graph.
- **Report proposed changes first.** Apply them only when the learner agrees.

Afterwards, run `python3 tools/validate_site.py` if anything changed.

The goal is a coherent curriculum that still reflects the learner's own path through the subjects.
