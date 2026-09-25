# Scout for Learning Opportunities

Use this workflow when the learner wants to discover what to learn next, especially from GitHub or other inspectable open-source projects.

## Inputs

Read:
- `curriculum/LEARNING_PROFILE.md`;
- existing course indexes and lesson titles;
- any repository, topic, domain, or constraint supplied by the learner.

The learner may provide either a source ("What can I learn from this repository?") or an interest ("Find useful things for me to learn about procedural generation").

## Goal

Find **transferable concepts worth understanding**, not merely popular repositories.

## Process

1. Search or inspect real candidate projects.
2. Establish what each project actually does.
3. Identify the specific concept(s) it demonstrates well.
4. Compare each concept with the existing curriculum.
5. Classify the opportunity:
   - **Deepens** an existing thread;
   - **Connects** two or more existing ideas;
   - **Introduces** a worthwhile new direction;
   - **Duplicate / low value**;
   - **Interesting project, weak teaching source**.
6. Prefer projects with readable implementation or documentation, clear provenance, and enough evidence to ground a lesson.
7. Do not force relevance to the learner's projects.
8. Do not create lessons until the learner chooses candidates, unless explicitly asked to do so.

## Candidate output

For each strong candidate report:
- source repository;
- what it actually does;
- transferable concept;
- why the concept may matter to this learner;
- relationship to existing lessons, if any;
- suggested depth;
- confidence/evidence notes.

Keep the distinction between "interesting repository" and "good learning opportunity" explicit.

## Selection

Once the learner selects a candidate, continue with `CREATE_LESSON.md`.
