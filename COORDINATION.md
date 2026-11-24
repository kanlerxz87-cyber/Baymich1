# COORDINATION — shared task board

Statuses: `unclaimed` · `in progress` · `done` · `needs review` (published on the Review Flags page; does not block a completed site delivery).

**Branch rule:** this work stays on the Arena-managed branch `arena/fe2115f0-baymich1`; no branch switching or `session-*` branch creation. The current owner is the integration session identified by that branch. Original repository was `main` at `3fa14d7` at the start of this work.

**Live site:** <https://kanlerxz87-cyber.github.io/Baymich1/> (GitHub Pages is enabled on `main`, root folder; publication follows merge/build).

| ID | Task | Status | Owner session | Scope / files | Notes |
|---|---|---|---|---|---|
| T1 | Repository review (line-by-line, sourced) | done | `e71de712` | `pages/repo-review.html`, initial coordination log | Retained in this repository and linked from the Sources page. |
| T2 | Current Michelin-starred restaurant roster, distinction, sources | done (some detail fields flagged) | `e71de712` + integration session | `data/michelin_bay_area_stars.json`, `data.js`, `restaurants.html`, `pages/michelin-starred.html` | Current dated 2026 roster is 41 Bay Area-city entries: 27 one-star, 7 two-star, 7 three-star; includes Yountville. Prices/socials and most hours remain flagged. |
| T3 | Bib Gourmand / Guide-listed, not starred | needs review | integration session | `data.js`, `restaurants.html`, `pages/suggestions.html` | Eight Bib Gourmand examples; not an exhaustive non-starred Guide directory. |
| T4 | Hotels selected/ranked by nearby restaurant density | needs review | integration session | `data.js`, `hotels.html`, `pages/executive-summary.html` | Four MICHELIN-Key candidates shown, no unsupported proximity rank or room prices. Radius/travel mode and dates are unresolved. |
| T5 | Verified social links (YouTube / TikTok / Instagram) | needs review | integration session | `data.js`, `restaurants.html` | No account filled without confirmation from an official source. |
| T6 | Restaurant total for two adults | needs review | integration session | `data.js`, `restaurants.html` | No official all-in totals confirmed; left blank and flagged. |
| T7 | Executive summary, questions, decision support and suggestions | done | `e71de712` + integration session | `index.html`, `decision-brief.html`, `suggestions.html`, `review.html`, existing `pages/*` | Executive brief, known/unknown Q&A, selectable proposals and flag page are published. |
| T8 | Responsive Pages dashboard and category pages | done | `e71de712` + integration session | `index.html`, `restaurants.html`, `clusters.html`, `hotels.html`, `decision-brief.html`, `suggestions.html`, `review.html`, `sources.html`, `styles.css`, `app.js`, `subpages.js` | The earlier session's generated pages, data and repository review are retained; new source-first dashboard is the root entry point. |
| T9 | Final integration, reconcile sources, build/links and publish | in progress | integration session | all shared outputs; current branch only | Reconcile 41-star scope with earlier merged output; verify conflict resolution and publish via PR. |

## Log

### L1 — Session `e71de712` — initial claim and repository review
- Claimed T1–T9 on its Arena branch. Starting repository was the initial commit and a minimal README; `COORDINATION.md` did not yet exist.
- Created `pages/repo-review.html`, based on the starting repository state, with source links for each finding.

### L2 — Session `e71de712` — initial restaurant data and dashboard
- Source: MICHELIN Guide, “Every MICHELIN-Starred Restaurant in California for 2026,” 24 Jun 2026: <https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california>.
- Created a 41-row Bay Area city/county dataset and cited official restaurant profile pages. The dataset clearly marks incomplete values. It also created initial executive summary, suggested questions, flagged fields, and a generated Pages site.
- Existing outputs retained at `data/michelin_bay_area_stars.json`, `pages/*`, `assets/style.css`, and `scripts/build_site.py`; no file from that session was removed.

### L3 — Session `arena/fe2115f0-baymich1` — initial inspection and claim
- At this session's start the local checkout was clean at `3fa14d7`, with only `README.md` and no coordination file. The initial claim was pushed before site work. Branch-specific pull initially failed because the remote branch did not yet exist; `git pull --rebase origin main` succeeded and the current branch was pushed.

### L4 — Session `arena/fe2115f0-baymich1` — inter-session conflict and reconciliation
- While preparing PR #3 for publication, `gh pr merge 3 --merge` reported that a clean merge commit could not be created. Fetching `origin/main` showed that PR #2 from session `e71de712` had merged after this branch was created. This was an integration conflict, not a reason to overwrite the earlier session's work.
- Reconciliation: preserve the earlier session's data, page files, site-generation script, and repository review. The official 2026 MICHELIN roster was rechecked. Its named Bay Area cities include Yountville/The French Laundry, a three-star entry omitted from the first version of this branch's count. Added The French Laundry and corrected the roster from 40 (6 three-star) to **41** (7 three-star), with Wine Country from 7 to **8**. The French Laundry profile was separately fetched and confirms its current three-star designation and Yountville location: <https://guide.michelin.com/us/en/california/yountville/restaurant/the-french-laundry>.
- Pending: rebase/integrate from the now-updated `origin/main`, retain both sessions' work, then update the PR and finish publication.

### Verification performed by the integration session
- Fetched the MICHELIN 2026 roster article and its list chunks. Final city-scoped counts: 41 restaurants; tier counts 27 one-star, 7 two-star and 7 three-star. City-group totals: San Francisco 25, Wine Country 8, East Bay 2, Marin 1, Peninsula & South Bay 5. Totals reconcile (25 + 8 + 2 + 1 + 5 = 41).
- Fetched official Michelin profiles for The French Laundry, Californios, Benu, Acquerello; official schedules were transcribed only for those three restaurants. Quince schedule and the special-date exception came from its official site. Four candidate hotel Keys/neighborhoods were checked against official Michelin hotel profiles.
- Every restaurant record links to its official Michelin Guide profile; every hotel candidate links to its official Michelin hotel profile. Missing fields remain blank/flagged.
- JavaScript syntax checks (`node --check`), `git diff --check`, local HTTP 200 checks for static pages/assets, and record/source counts passed. No project build dependency exists; GitHub Pages is configured for static root content.

## Irregularities / open review flags
- No all-in price for two adults has been verified from official current menu and fee sources.
- Most restaurant schedules, special-date exceptions and official social accounts are not verified; empty fields are intentional.
- Hotel area density ranking cannot be computed safely until a radius or mode/time threshold and date are selected and validated.
- The Bib Gourmand list is an 8-entry sample, not a full non-starred MICHELIN Guide selection.
- Broad MICHELIN “San Francisco and surroundings” live-filter counts include surrounding results and differ from the declared city-scoped 2026 roster. Use the dated annual roster for the 41 count and the live directory only for checking individual current details.
- The separate initial repository review is a historical snapshot from the repository's first commit; it is retained for transparency and linked from the Sources page.
