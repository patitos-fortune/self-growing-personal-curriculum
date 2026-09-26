# Scout for Learning Opportunities

Use this when the learner wants to discover what to learn next, or asks "what can I learn from this source?"

## Inputs

Read:
- `curriculum/LEARNING_PROFILE.md`;
- `curriculum/CANDIDATES.md` (what was already proposed, merged or skipped);
- existing course indexes and lesson titles;
- any topic, source, goal or constraint the learner gave you.

The learner may give you a **source** ("What can I learn from this repository / book chapter / paper?") or an **interest** ("Find good things for me to learn about harmony in jazz").

## Goal

Find **concepts worth understanding**, each backed by a credible source, not just popular links.

Good sources depend on the subject:
- software and systems: readable open-source code, official docs, design documents;
- sciences and maths: open textbooks, open courseware, review papers, reputable explainers;
- languages, arts and crafts: well-regarded references, style guides, annotated examples;
- anything: primary sources and recognised standards bodies over anonymous summaries.

## Process

1. Search for or inspect real candidate sources. Only cite sources you actually looked at.
2. Establish what each source actually says or does.
3. Identify the specific concept it demonstrates or explains well.
4. Compare with existing lessons and with `CANDIDATES.md`.
5. Classify the opportunity:
   - **Deepens** an existing thread;
   - **Connects** two or more existing ideas;
   - **Introduces** a worthwhile new direction;
   - **Duplicate / low value**;
   - **Interesting source, weak teaching material**.
6. Propose an editorial outcome for each (ADD / MERGE / REFERENCE / REPLACE / SKIP; see `AGENTS.md`).
7. Record every candidate in `curriculum/CANDIDATES.md` with outcome `PROPOSED` (or `SKIP`, with a reason).
8. Present the candidates to the learner. Do not write lessons until they choose, unless they explicitly asked you to.

## What to show the learner

For each strong candidate, three to seven per round:
- the concept, in plain words;
- the source and what it actually is;
- why it may matter to *this* learner (link to their stated interests or goals, without forcing it);
- how it relates to existing lessons;
- suggested depth (one lesson / a short series);
- how confident you are in the source.

Keep "interesting source" and "good learning opportunity" clearly separate.

## After the learner decides

- Update each candidate's outcome in `CANDIDATES.md` (`ADD → slug/NN`, `MERGE → slug/NN`, `SKIP`, and so on) and move it to "Decided".
- For accepted candidates, continue with `CREATE_LESSON.md`.
