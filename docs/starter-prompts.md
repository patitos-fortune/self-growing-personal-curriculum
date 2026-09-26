# Starter prompts

Copy these into any AI coding assistant that can read and edit files in your repository (Claude Code, Codex, GitHub Copilot, Cursor, ChatGPT with the repository connected, and so on). Replace the parts in brackets. Assistants that don't pick up `AGENTS.md` automatically need to be told to read it, which is why most prompts start that way.

## First session

> Read AGENTS.md and follow its first-run steps. I want to learn [X, Y and Z]. My goal is [why, or a project]. I already know [background]. I prefer [short lessons I can read on my phone / lots of worked examples / ...]. Help me set up my learning profile and suggest my first topics. Don't write lessons until I pick.

## Find more to learn

> Read AGENTS.md, then follow prompts/SCOUT.md. Suggest 5 candidate topics for [interest]. Record them in curriculum/CANDIDATES.md.

## Learn from a specific source

> Read AGENTS.md. What could I learn from [URL of a repository / article / book chapter / paper]? Follow prompts/SCOUT.md and tell me which concepts would make good lessons, and which would just be interesting trivia.

## Turn chosen candidates into lessons

> I choose candidates [1 and 3]. Follow prompts/CREATE_LESSON.md to write them, update the course index, navigation and home page, record the outcome in CANDIDATES.md, and run the validator.

## Start a new course

> Lessons about [topic] are piling up. Follow prompts/CREATE_COURSE.md and propose whether they deserve their own course. Don't renumber or move published lessons.

## Record progress

> I finished [course name] lessons [1–3] on [date]. Update curriculum/PROGRESS.json following prompts/UPDATE_PROGRESS.md.

> Here is my exported learning-progress.json: [attach or paste]. Merge it into curriculum/PROGRESS.json following prompts/UPDATE_PROGRESS.md.

## Keep it coherent

> Follow prompts/REVIEW_CURRICULUM.md. Report duplicates, missing bridges and stale sources, and suggest what I should read next based on my progress. Don't change anything yet.

## Housekeeping

> Remove the example course, following "Removing the example course" in AGENTS.md.

> Rename the site title from "Self-Growing Personal Curriculum" to "[My Library]" on every page and template.

> Help me publish this site with GitHub Pages following docs/publishing.md.

## Tips

- Ask the assistant to show you the candidates before writing anything. Curation is the point.
- Review the diff before you commit. The validator catches structural mistakes, not factual ones.
- If a lesson claims something surprising, ask: "Which source supports this sentence?"
