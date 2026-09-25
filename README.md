# Self-Growing Personal Curriculum

A lightweight, AI-maintainable personal learning library that grows from the learner's interests.

The project is deliberately simple: static HTML + CSS, no database, no accounts, no framework, no build step, and no required AI provider. The repository itself stores the learning profile, curriculum, lesson format, and instructions that an AI coding assistant can follow.

## The idea

1. Start with a few interests.
2. Ask an AI coding assistant to read `AGENTS.md`.
3. The AI reads or creates `curriculum/LEARNING_PROFILE.md`.
4. It scouts real open-source projects for transferable ideas worth learning.
5. You choose what is interesting.
6. The AI creates lessons grounded in real implementations.
7. New lessons connect to prior lessons where that genuinely improves understanding.
8. Your curriculum gradually becomes specific to you.

The source repository is evidence and a concrete example, not homework. Learners should not have to clone or run every project used in a lesson.

## Quick start

Clone or create a repository from this project, then point your AI coding assistant at the repository and say:

> Read AGENTS.md. I want to use this as my personal learning library. My main interests are [YOUR INTERESTS]. Help me initialize my learning profile and scout for my first learning topics.

The AI should then follow the workflow in `prompts/SCOUT.md`. You remain the curator: scouting proposes candidates; it does not automatically turn everything into a lesson.

## Structure

```
.
├── AGENTS.md
├── README.md
├── index.html
├── assets/css/style.css
├── curriculum/
│   └── LEARNING_PROFILE.md
├── prompts/
│   ├── SCOUT.md
│   ├── CREATE_LESSON.md
│   ├── CREATE_COURSE.md
│   └── REVIEW_CURRICULUM.md
├── templates/
│   ├── lesson.html
│   └── course.html
├── courses/
└── tools/
    └── validate_site.py
```

## Design principles

- **Personal relevance over generic coverage.** The curriculum should follow the learner's curiosity.
- **Real sources, transferable ideas.** Repositories provide concrete implementations from which general concepts can be taught.
- **Do not force connections.** A repository can be interesting without belonging in the curriculum.
- **Continuity matters.** Check existing lessons for prerequisites, overlaps, contrasts, and useful conceptual bridges.
- **Understanding before installation.** A lesson must stand on its own.
- **Human curation stays in the loop.** The AI scouts and proposes; the learner decides what deserves attention.
- **Portable context.** Important learner context lives in this repository rather than depending on one AI provider's memory.
- **Static by default.** Keep the reading experience offline-friendly and dependency-free.

## Adding content manually

Each course lives at `courses/<course-slug>/`, with an `index.html` and a `lessons/` folder. Lesson numbering is per course and permanent. Copy the files in `templates/` when starting a new course or lesson.

Run `python3 tools/validate_site.py` before committing structural changes.

## Origin

This project was extracted from the architecture and learning workflow behind **Patitos Learning**, then generalized so the curriculum, learner profile, scouting loop, and AI instructions can travel together as an independent project.

## License

MIT. See `LICENSE`.
