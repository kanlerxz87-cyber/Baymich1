# COORDINATION — shared task board

Repo: `kanlerxz87-cyber/Baymich1` · Working branch: `arena/7e371c2d-baymich1` (base `main` @ `3fa14d7`)

**Branch note:** The session rules ask for `session-<id>/<task>` branches. This session is fixed to its assigned branch `arena/7e371c2d-baymich1`, so all tasks are committed there. Other sessions should claim tasks here and use their own branch only if Arena assigns one.

Status values: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).

| Task | Status | Owner (session) | Files in scope | Notes |
|---|---|---|---|---|
| T1 Repo review & irregularities | needs review | 7e371c2d | `README.md`, `COORDINATION.md` | Repo has only README; see Flagged page |
| T2 Michelin Bay Area restaurants (official pages) | needs review | 7e371c2d | `docs/data/restaurants.json` | 10 rows verified from official pages; rest flagged |
| T3 Hotels ranked by nearby Michelin restaurants | unclaimed | — | `docs/data/hotels.json` | Not started; method on Hotels page |
| T4 Activities + YouTube/TikTok/Instagram links | unclaimed | — | `docs/data/activities.json` | Not started; no social links verified yet |
| T5 Site (GitHub Pages dashboard) | in progress | 7e371c2d | `docs/**` | Static site, reads JSON from `docs/data/` |
| T6 Integration, re-verification, publish | unclaimed | — | all shared outputs | Final integration session only |

## Log

### 2026-11-24 · session 7e371c2d
- **Claimed** T1, T2, T5 (and T3/T4 scoped, not started). Committed and pushed this claim first.
- **T1 (repo review):** Repo contains only `README.md` (`# Baymich1`) and an "Initial commit". No code, license, `.gitignore`, or CI. `COORDINATION.md` did not exist; created here.
- **T2 (restaurants):** Official source: `https://guide.michelin.com/us/en/california/san-francisco/restaurants` (145 entries for "San Francisco and surroundings": 4 three-star, 7 two-star, 18 one-star, 30 Bib Gourmand, 86 Selected).
  - Verified individually on official Michelin pages (star icons, address, cuisine, price tier, website, phone): Quince, Atelier Crenn, Benu, Californios, Lazy Bear, Saison, Acquerello, Birdsong, Commis (Oakland), Abacá (listed, no star).
  - Hours: captured for Quince, Benu, Californios, Lazy Bear, Saison (Tue–Thu only), Acquerello. Not captured: Atelier Crenn, Birdsong, Commis, Abacá, Saison Fri–Sun → left blank and flagged.
  - Irregularities: see Flagged page (Kiln slug resolves to London; Sons & Daughters page not found; press dates conflict; 1-star and other press-reported names not yet checked).
- **T5 (site):** Static site in `docs/`, built from the JSON files above.
- **Scope not done this session:** hotel ranking (T3), activities and social links (T4), pricing for two adults (no official per-couple price was verified; left blank).
