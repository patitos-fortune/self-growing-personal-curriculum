# How progress tracking works

The site stays static: no accounts, no server, no cookies, no analytics. Progress has two layers.

## 1. Browser storage (immediate, per device)

Each lesson has a **Mark as read** button. Clicking it stores a record in the browser's `localStorage`:

- **Key:** `sgpc-progress-v1:<site path>`, for example `sgpc-progress-v1:/my-curriculum/`. The path is included because every project site under `https://<user>.github.io/` shares one browser origin, so two curricula would otherwise overwrite each other.
- **Value:** the same format as `PROGRESS.json` (below).

It survives page navigation, reloads and browser restarts.

**Limitations:** it is specific to one browser on one device. It is not synced, and it is lost if you clear site data or browse privately. Some browsers limit storage for pages opened from `file://`.

## 2. `curriculum/PROGRESS.json` (durable, in Git)

```json
{
  "version": 1,
  "completed": [
    { "lesson": "example-learning-how-to-learn/01", "completed": "2026-09-26" }
  ]
}
```

- `lesson` is the stable lesson ID `<course-slug>/<NN>`, matching `courses/<course-slug>/lessons/<NN>.html`.
- `completed` is a date (`YYYY-MM-DD`).

When the site is served over HTTP(S), as on GitHub Pages or a local `python3 -m http.server`, `progress.js` fetches this file and shows those lessons as read on every device. Lessons recorded here cannot be unmarked from the browser. Change the file instead.

The validator checks that the file is well formed and that every ID refers to an existing lesson.

## Moving progress from the browser into Git

1. Open the **Progress** page on the site and click **Export progress (JSON)**. This downloads `learning-progress.json`, which uses the same format plus an `exported` timestamp.
2. Give the file to your AI assistant: *"Merge this into curriculum/PROGRESS.json following prompts/UPDATE_PROGRESS.md."*
3. Review the diff, commit and push. After the next deploy, those lessons show as read everywhere.

You can also just tell the assistant *"I finished lesson 3 of the jazz-harmony course"*, and it will add the record.

## Moving progress between devices without Git

Export on one device, then use **Import progress file** on the Progress page of the other. Imports merge by lesson ID, never delete anything, and keep the earliest completion date.

## What "read" means

Delivered, opened, completed and mastered are different things. The site records only what you explicitly mark. Nobody, AI assistants included, should treat "read" as "mastered".

## Room to grow

Because both layers use the same small JSON format, later additions do not need a backend. Examples: syncing through a gist or a file in cloud storage, or recording review dates for spaced repetition. Anything that needs credentials should stay out of the static site. Do not put GitHub tokens in page JavaScript.
