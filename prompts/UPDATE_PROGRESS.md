# Update Reading Progress

Use this when the learner reports completing lessons or gives you an exported browser progress file (`learning-progress.json`). Background: `docs/progress-tracking.md`.

## Meaning of completion

Keep these states distinct:

- **Delivered:** a lesson was suggested or sent.
- **Opened:** the learner visited it.
- **Completed/read:** the learner explicitly marked or reported it as read.
- **Mastered:** never infer this from completion.

Only explicit learner action marks a lesson completed.

## Canonical format

`curriculum/PROGRESS.json`:

```json
{
  "version": 1,
  "completed": [
    { "lesson": "course-slug/01", "completed": "YYYY-MM-DD" }
  ]
}
```

Lesson IDs are permanent and correspond to `courses/<course-slug>/lessons/NN.html`. Keep records sorted by lesson ID so diffs stay readable.

## Updating from conversation

When the learner says they completed a lesson:

1. Find the lesson ID from the course index. If the reference is ambiguous ("the one about scales"), confirm it.
2. Add a record if the lesson is not already completed.
3. Use the date the learner gave, otherwise today's date.
4. Keep existing records and dates unchanged. Never create duplicates.

## Merging a browser export

1. Check `"version": 1` and that `completed` is a list. Ignore the extra `exported` field.
2. For each record, check the ID has the form `slug/NN` and matches an existing lesson file.
3. Merge by lesson ID. If both have a date, keep the earliest unless the learner says otherwise.
4. Never delete repository records because the export lacks them.
5. Report malformed or unknown IDs to the learner. Do not invent lessons for them.

## Removing records

Only when the learner explicitly asks (for example, to re-read a lesson as new), or when a lesson is deleted at their request.

## After editing

Run `python3 tools/validate_site.py`. It fails on malformed records or IDs that do not match a lesson.

## Recommending what to read next

Use completion as context, not as proof of mastery. Prefer sensible continuity and the learner's current interests over simply picking the next number.
