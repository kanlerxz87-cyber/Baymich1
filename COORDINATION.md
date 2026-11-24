# COORDINATION.md

Shared task board for the Baymich1 Michelin SF Bay Area guide project.
Branch: `arena/e4732d51-baymich1` (branched from main `3fa14d7`).

Session ID: `session-arena-e4732d51`

## How to use
- Claim a task by writing your session ID in the `owner` column and setting status to `in progress`.
- Commit and push the claim immediately.
- Never start a task another session has claimed.
- Keep scopes non-overlapping: each session works on its own branch/worktree named `session-<id>/<task>` and edits only files in its claimed scope.
- Make small, frequent commits; run `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding the other session's work, log what happened.
- When finished, record sources, verification performed, and irregularities here; mark `done`.
- Never mark anything verified without checking against an official source; link that source.
- A status of `needs review` means published on the Flagged for Review page and does not block anything.
- If a session crashes or its claim is >60 minutes old with no commits, any other session may take over and note the handoff in the log.

## Tasks

| # | Task | Scope (files) | Status | Owner | Sources / verification | Irregularities |
|---|------|---------------|--------|-------|------------------------|----------------|
| 1 | Create coordination board & claim tasks | COORDINATION.md | in progress | session-arena-e4732d51 | — | — |
| 2 | Research: official Michelin Guide SF Bay Area restaurant list (guide-listed vs starred, Bib Gourmand) | docs/data/restaurants.md | unclaimed | — | michelinguide.com | — |
| 3 | Research: Michelin star clusters in SF Bay Area | docs/analysis/clusters.md | unclaimed | — | michelinguide.com | — |
| 4 | Research: hotels ranked by Michelin restaurant proximity/count | docs/data/hotels.md | unclaimed | — | official hotel sites / michelinguide.com | — |
| 5 | Research: pricing (2 adults), hours, days open, exceptions, social links per restaurant | docs/data/restaurants.md | unclaimed | — | official restaurant sites | — |
| 6 | Build: GitHub Pages site structure (landing page + category subpages) | index.html, category pages, assets | unclaimed | — | — | — |
| 7 | Build: tables with all entries, sources, unverified flags | site pages | unclaimed | — | — | — |
| 8 | Build: executive summary | docs/executive-summary.md | unclaimed | — | — | — |
| 9 | Build: suggestions section (pre-implementation review) | docs/suggestions.md | unclaimed | — | — | — |
| 10 | Build: open questions / information needed / answers before decisions | docs/questions.md | unclaimed | — | — | — |
| 11 | Verification: line-by-line source check of every table row | all data files | unclaimed | — | official sources | — |
| 12 | Integration: merge branches, re-verify combined data, confirm no broken links, publish to GitHub Pages | all | unclaimed | — | — | — |

## Log

- 2026-11-24: session-arena-e4732d51 created COORDINATION.md and claimed task 1 (in progress).
