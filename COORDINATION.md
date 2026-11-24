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
| T2 | Michelin Bay Area starred restaurants (41) — list, star level, NEW flag, Michelin link | done (partial fields) | e71de712 | `data/michelin_bay_area_stars.json`, `pages/michelin-starred.html` | Star levels verified (article). Address/website/tier/hours read for 14 (3★/2★); hours verified for 7; cuisine, couple cost not verified. See F6, F13, F14. |
| T3 | Michelin Bib Gourmand / Recommended (listed, no star) — Bay Area | unclaimed | — | — | Not captured in this pass |
| T4 | Hotels — Michelin hotel ranking by nearby starred/listed restaurants | unclaimed | — | — | Not captured in this pass |
| T5 | Social links (YouTube / TikTok / Instagram) for each entry | unclaimed | — | — | None verified in this pass |
| T6 | Couple cost (2 adults) with official menu prices | unclaimed | — | — | Michelin shows price tiers only; no dollar values verified |
| T7 | Executive summary, analysis, questions & suggestions | done | e71de712 | `pages/executive-summary.html`, `pages/suggestions.html`, `pages/flagged-for-review.html` | |
| T8 | Site build (landing + category subpages) | done | e71de712 | `index.html`, `pages/*`, `assets/style.css`, `scripts/build_site.py` | Generated from JSON by `scripts/build_site.py` |
| T9 | Integration (merge to main, Pages publish) | in progress | e71de712 | all | Final step — PR to `main` and Pages publish |

---

## Log

### L1 — Session e71de712 — claim and repo review
- Claimed T1–T9 (single active session on this branch).
- Repo state at start: `main` = `3fa14d7` ("Initial commit"), contains only `README.md` (`# Baymich1`). No COORDINATION.md existed; created here.
- Repo irregularities: see the *Repo review* page and the *Flagged for Review* page.

### L2 — Session e71de712 — Michelin data pass
- Sources (official, fetched this session):
  - Michelin article, "Every MICHELIN-Starred Restaurant in California for 2026" (24 Jun 2026): https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california — chunks 0–2 read; full Bay Area star lists (3★ 7, 2★ 7, 1★ 27) and NEW markers. Chunks 3–4 not read.
  - Michelin press release (26 Jun 2026): https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026
  - Michelin restaurant detail pages for 14 restaurants (3★ and 2★): address, price tier, hours, website. Phone read for Atelier Crenn only.
  - Michelin SF listing pages 1–3: https://guide.michelin.com/us/en/california/san-francisco/restaurants (counts only; no row-level values used).
- Verification: each starred row links to its Michelin page (from the article). Values not read from an official page are blank and flagged UNVERIFIED. Press reports were not used as value sources.
- Corrections made in this pass: removed phone numbers and ZIP codes that were not read from official pages; removed 1★ cuisine/price tiers that were not read; removed press-only lost-star names; corrected Commis hours.

### L3 — Session e71de712 — publish (integration, T9)
- Site built from `data/michelin_bay_area_stars.json` by `scripts/build_site.py`. The build checks that every local link resolves. External links are the official sources listed above, plus the Michelin article for each row.
- Pages publishes from `main` (root). Publishing requires merging this branch to `main` (PR).
- Open items: see Flagged for Review (F1–F14) and Suggestions & questions (Q1–Q7).
