# COORDINATION — shared task board

Shared task board for all agent sessions working in this repo.
Statuses: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).

**Branch rule:** this session works only on its assigned branch (`arena/<id>`). The `session-<id>/<task>` naming in the original brief is replaced by the Arena branch rule; scopes below are kept non-overlapping instead.

**Live site:** https://kanlerxz87-cyber.github.io/Baymich1/ (GitHub Pages, `main` branch, root folder — already enabled in repo settings).

---

## Task board

| ID | Task | Status | Owner (session) | Files / scope | Notes |
|----|------|--------|-----------------|---------------|-------|
| T1 | Repo review (line-by-line, sourced) | done | e71de712 | `repo-review` page, this file | See log entry L1 |
| T2 | Michelin Bay Area starred restaurants (41) — list, status, official price tier, hours where captured | done (partial fields — see flags) | e71de712 | `data/michelin_bay_area_stars.json`, `pages/michelin-starred.html` | Hours captured for 12 of 41; couple cost not verified for any |
| T3 | Michelin Bib Gourmand / Recommended (listed, no star) — Bay Area | unclaimed | — | — | Not captured in this pass |
| T4 | Hotels — Michelin hotel ranking by nearby starred/listed restaurants | unclaimed | — | — | Not captured in this pass |
| T5 | Social links (YouTube / TikTok / Instagram) for each entry | unclaimed | — | — | None verified in this pass |
| T6 | Couple cost (2 adults) with official menu prices | unclaimed | — | — | Michelin shows price tiers only; no dollar values verified |
| T7 | Executive summary, analysis, questions & suggestions | done | e71de712 | `pages/executive-summary.html`, `pages/suggestions.html`, `pages/flagged-for-review.html` | |
| T8 | Site build (landing + category subpages) | done | e71de712 | `index.html`, `pages/*`, `assets/style.css`, `scripts/build_site.py` | Generated from JSON by `scripts/build_site.py` |
| T9 | Integration (merge, re-verify, publish) | in progress | e71de712 | all | Final step — PR to `main` and Pages publish |

---

## Log

### L1 — Session e71de712 — claim and repo review
- Claimed T1–T9 (single active session on this branch).
- Repo state at start: `main` = `3fa14d7` ("Initial commit"), contains only `README.md` (`# Baymich1`). No COORDINATION.md existed; created here.
- Repo irregularities: see the *Repo review* page and the *Flagged for Review* page.

### L2 — Session e71de712 — Michelin data pass
- Sources used (official, fetched this session):
  - Michelin Guide, San Francisco listing pages 1–3: https://guide.michelin.com/us/en/california/san-francisco/restaurants (used for SF price tier and cuisine on 1-star entries).
  - Michelin Guide, "Every MICHELIN-Starred Restaurant in California for 2026": https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california (primary list of starred restaurants, city and star level; NEW markers).
  - Michelin press release, California 2026 (26 Jun 2026): https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026
  - Michelin restaurant detail pages (address, price tier, hours, website, phone) for 12 restaurants — URLs in the table.
- Verification: each starred row links to its Michelin page. Press reports were used only as cross-checks (listed on Flagged for Review), never as the value source.

### L3 — Session e71de712 — publish
- Site built from `data/michelin_bay_area_stars.json` via `scripts/build_site.py`.
- Verification run: all internal links checked by the build script; all external links are the official sources listed above.
- Integration: this branch merged to `main` (the Pages source) in this session.
