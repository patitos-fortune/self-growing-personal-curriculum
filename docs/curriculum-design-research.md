# Curriculum Design Research

This document records the design principles adopted after comparing several mature learning and curation repositories. These projects are references, not dependencies or templates to copy wholesale.

## Three starter curriculum archetypes

A new curriculum should begin with one of three simple traversal models. These are different ways to move through knowledge, not visual themes or difficulty levels.

### 1. ROADMAP — explore a knowledge graph

**Question it answers:** What should I learn, and what connects to what?

Inspired by:
- https://github.com/kamranahmedse/developer-roadmap

Represent a subject as concepts and meaningful prerequisite/adjacency relationships. The learner can see branches and choose where to go next. Prefer this when exploration and dependency awareness matter more than one canonical sequence.

Minimal conceptual model:

```text
topic
├── prerequisite
├── sibling concept
└── possible next concepts
```

Do not reproduce giant roadmaps by default. The transferable idea is the graph.

### 2. COURSE — follow an ordered progression

**Question it answers:** In what order should I learn this?

Inspired by:
- https://github.com/ossu/computer-science

Use an explicit sequence where earlier material prepares the learner for later material. Parallel branches are allowed when prerequisites permit them, but the curriculum supplies a recommended path.

Prefer this when concepts genuinely build on one another or when the learner wants less navigation overhead.

### 3. PROJECT — learn by building

**Question it answers:** What can I build that forces me to learn this?

Inspired by:
- https://github.com/practical-tutorials/project-based-learning

Organize learning around artifacts whose construction exposes concepts at the moment they become useful. A project path should still name the concepts being learned; building is the vehicle, not a substitute for understanding.

A useful project learning object can connect:

```text
concept → short explanation → exercise → artifact → reflection → next concept
```

## Choosing an archetype

Do not infer that one archetype is universally better.

Use **ROADMAP** when the learner wants to explore a broad field or understand dependencies.

Use **COURSE** when order and scaffolding are important.

Use **PROJECT** when the learner has a concrete thing they want to make and concepts can be introduced through that work.

A mature curriculum may mix them later. Keep the first-run choice simple.

## Compact learning-object schema

Reference:
- https://github.com/Chalarangelo/30-seconds-of-code

Short, independently useful learning objects benefit from stable metadata. The project does not need a database to use a consistent schema.

Recommended conceptual fields:

```text
stable_id
title
concept
difficulty
estimated_time
tags
prerequisites
explanation
worked_example
exercise
connections
sources
status
```

Not every field needs to be rendered to the learner. The important property is consistency so humans and AI tools can inspect, connect and maintain the curriculum.

## Static data and search architecture

Reference:
- https://github.com/EbookFoundation/free-programming-books
- https://github.com/EbookFoundation/free-programming-books-search

Keep canonical curriculum content in Git-friendly text/data. If richer browsing or search is added later, derive a static index such as JSON during generation/build rather than introducing a database merely for discovery.

Preferred direction:

```text
Markdown / structured curriculum data
                ↓
        generated static index
                ↓
        GitHub Pages / browser
                ↓
      local filtering and search
```

This preserves the project's core properties: inspectable source, portable state, static hosting, no account requirement and no server-side credentials.

Do not add a build system until the amount of content makes the derived index worthwhile.

## Editorial constitution: curate, do not accumulate

Reference:
- https://github.com/sindresorhus/awesome
- https://github.com/sindresorhus/awesome/blob/main/awesome.md

Self-growing must not mean monotonically growing.

Every scouted candidate should receive one explicit editorial outcome:

- **ADD** — sufficiently novel and useful to deserve a new lesson.
- **MERGE** — valuable material that strengthens an existing lesson without deserving a separate one.
- **REFERENCE** — preserve as a useful source/example, but do not add curriculum weight.
- **REPLACE** — a clearly better source or treatment supersedes an existing candidate; preserve provenance when replacing published material.
- **SKIP** — interesting is not enough; no curriculum action is required.

Before choosing ADD, check:
1. Is the transferable concept genuinely distinct?
2. Does an existing lesson already teach it adequately?
3. Does it fit the learner's interests, projects or useful foundations?
4. Is the source strong enough to ground the lesson?
5. Can the concept be taught without requiring the learner to adopt the source project?

The system should be comfortable becoming better without becoming larger.

## Relationship to the existing scouting workflow

The original flow remains:

```text
source
  ↓
candidate concept
  ↓
editorial decision
  ↓
lesson / merge / reference / skip
  ↓
curriculum
```

The three archetypes determine how accepted lessons are traversed. They do not weaken the human-curation gate.

## Design guardrails

- Do not force every learner into software-engineering examples.
- Do not turn ROADMAP into a giant intimidating graph on first run.
- Do not turn COURSE into a rigid degree imitation.
- Do not turn PROJECT into tutorial copying without conceptual explanation.
- Do not introduce a database merely to track static metadata.
- Do not let an AI publish every plausible candidate automatically.
- Preserve stable lesson IDs even if curriculum relationships evolve.
- Prefer small derived indexes and local browser state over server infrastructure until a real requirement justifies complexity.
