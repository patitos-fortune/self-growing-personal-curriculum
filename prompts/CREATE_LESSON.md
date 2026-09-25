# Create a Lesson

Create a lesson only after a topic has been selected or explicitly requested.

## Before writing

1. Read `AGENTS.md`.
2. Read `curriculum/LEARNING_PROFILE.md`.
3. Inspect existing course indexes and relevant prior lessons.
4. Inspect the real source repository/documentation/code supporting repository-specific claims.
5. Decide whether this belongs in an existing course or whether a new course is justified.

## Lesson contract

A lesson must separate:
- **Source:** what the real project does.
- **Concept:** the general idea demonstrated.
- **Mechanism:** how the idea actually works.
- **Transfer:** where the idea can apply elsewhere.

Do not turn the lesson into installation instructions or a repository walkthrough.

## Required structure

Use `templates/lesson.html` and preserve this learning sequence:

1. **What You're Learning** — precise concept and scope.
2. **Why This Matters** — motivation without hype.
3. **The Idea** — explain the mechanism.
4. **Walk Through an Example** — concrete worked example, trace, table, or inline diagram.
5. **Source Project to Explore** — grounded connection to the real implementation.
6. **Try It** — a mental exercise requiring no setup.
7. **Reveal answer** — inside native `<details>/<summary>`.
8. **Takeaways** — 3–5 durable points.

## Connections

If an earlier lesson is a genuine prerequisite, contrast, or conceptual bridge, mention it naturally. Do not add cross-references merely because they exist.

## Quality checks

Before finishing:
- Can the lesson be understood without cloning the source?
- Are repository-specific claims grounded?
- Is the worked example genuinely worked, rather than decorative?
- Does the exercise test the central idea?
- Are source facts distinguished from general explanation?
- Does this duplicate an existing lesson?
- Are title, description, duration, and navigation consistent with the course index?

Update the course index and neighboring navigation, then run `python3 tools/validate_site.py`.
