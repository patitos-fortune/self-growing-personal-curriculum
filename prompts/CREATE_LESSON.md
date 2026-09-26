# Create a Lesson

Create a lesson only after the learner accepted a candidate or explicitly asked for the lesson.

## Before writing

1. Read `AGENTS.md` and `curriculum/LEARNING_PROFILE.md`.
2. Read the relevant course index and any lessons this one builds on or contrasts with.
3. Check that the concept is not already taught. If it mostly is, propose MERGE instead.
4. Inspect the real source(s) supporting any specific claims.
5. Decide which course it belongs to. If none fits and a real cluster is forming, follow `CREATE_COURSE.md`. If not, put it in the closest course.

## Lesson contract

A lesson keeps these separate:
- **Source:** what the real source says or does.
- **Concept:** the general idea.
- **Mechanism:** how the idea actually works.
- **Transfer:** where else it applies.

It is not an installation guide, a book summary or a repository walkthrough. It should be self-contained, readable on a phone, and doable in one focused sitting (usually 10–30 minutes).

## Structure

Copy `templates/lesson.html` and keep this sequence:

1. **What You're Learning:** the precise concept and its scope.
2. **Why This Matters:** motivation without hype.
3. **The Idea:** the mechanism.
4. **Walk Through an Example:** a genuinely worked example: a trace, a table, a calculation, an annotated passage, or an inline SVG diagram.
5. **Sources to Explore:** the real source(s), what each contains, and a link. Say whether you verified it.
6. **Try It:** a mental exercise that needs no setup.
7. **Reveal answer:** inside the native `<details>/<summary>`.
8. **Takeaways:** 3–5 durable points.

## Filling in the template

- File: `courses/<slug>/lessons/NN.html`, where `NN` is the next unused number in that course (`01`, `02`, ...).
- `<body data-lesson-id="<slug>/NN">`: must match the path exactly.
- Replace every uppercase placeholder (`LESSON TITLE`, `COURSE TITLE`, `CONTENT`, ...). The validator rejects leftovers.
- Level badge: `tier-1` Foundations, `tier-2` Intermediate, `tier-3` Deep dive. Remove it if the course does not use levels.
- External links: `target="_blank" rel="noopener"`.

## Wiring it into the site

1. **Course index** (`courses/<slug>/index.html`): copy an existing `<li>` lesson card and set `href="lessons/NN.html"`, `data-lesson-id`, title, duration and description. Title and duration must match the lesson header. Update the lesson count text.
2. **Navigation:** in the new lesson, "Previous" links to `NN-1` (or stays disabled for `01`) and "Next" stays disabled. In the previous lesson, change the disabled "Next" span into a link to the new lesson.
3. **Home page** (`index.html`): update the course card's lesson count and its `data-total` value.
4. **Candidates:** set the candidate's outcome to `ADD → <slug>/NN` in `curriculum/CANDIDATES.md`.

## Quality checks

- Can it be understood without opening the source?
- Is every source-specific claim grounded? Are unverified things labelled as such?
- Is the worked example actually worked, not decorative?
- Does the exercise test the central idea?
- Does it duplicate an existing lesson?

Finally run `python3 tools/validate_site.py` and fix everything until it reports `RESULT: PASS`.
