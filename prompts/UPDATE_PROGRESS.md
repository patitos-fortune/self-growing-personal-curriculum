# Update Reading Progress

Use this workflow when the learner reports completing lessons or provides an exported browser progress file.

## Meaning of completion

Keep these states distinct:

- **Delivered**: a lesson was sent or suggested.
- **Opened**: the learner visited it.
- **Completed/read**: the learner explicitly marked or reported it as read.
- **Mastered**: never infer this merely from completion.

Only explicit learner action should mark a lesson completed.

## Canonical repository state

Durable reading history lives in `curriculum/PROGRESS.json`.

Each completion record uses:

```json
{
  "lesson": "course-slug/01",
  "completed": "YYYY-MM-DD"
}
```

Lesson IDs are stable and correspond to `courses/<course-slug>/lessons/NN.html`.

## Updating from conversation

When the learner says they completed a lesson:

1. Confirm the lesson ID from the curriculum.
2. Add it if it is not already completed.
3. Preserve existing completion dates.
4. Do not remove other records.
5. Use the learner's stated completion date when supplied; otherwise use the current date.
6. Keep records deterministic and avoid duplicates.

## Merging browser exports

The static site may export browser-local progress.

When given an export:
1. Validate its version and lesson IDs.
2. Merge by lesson ID.
3. Never delete repository completions simply because the browser export lacks them.
4. If both contain dates, preserve the earliest credible completion date unless the learner instructs otherwise.
5. Report malformed or unknown lesson IDs instead of silently inventing lessons.

## Recommendations

When suggesting what to read next, use completion state as context, but do not assume completed means mastered. Prefer sensible continuity and the learner's current interests over mechanically selecting the next number.
