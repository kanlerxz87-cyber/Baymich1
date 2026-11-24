# COORDINATION — shared task board

Statuses: `unclaimed` · `in progress` · `done` · `needs review` (published on the Review Flags page; does not block a completed site delivery).

**Branch rule:** work stays on its own Arena-managed branch; no branch switching or `session-*` branch creation beyond the Arena-assigned branch. Original repository was `main` at `3fa14d7` at the start of this work.

**Live site:** <https://kanlerxz87-cyber.github.io/Baymich1/> (GitHub Pages is enabled on `main`, root folder; built and public).

**Sessions represented:** `e71de712` (initial), `arena/fe2115f0-baymich1` (integration/dashboard), `session-arena-e4732d51` (branch `arena/e4732d51-baymich1`, this session). No earlier session-owned files were deleted in this merge.

## Combined task board

| ID | Task | Status | Owner session | Scope / files | Notes |
|---|------|--------|---------------|---------------|-------|
| T1 | Repository review (line-by-line, sourced) | done | `e71de712` | `pages/repo-review.html`, initial coordination log | Retained; linked from Sources page. |
| T2 | Current Michelin-starred roster, distinction, sources | done (detail fields flagged) | `e71de712` + integration | `data/michelin_bay_area_stars.json`, `data.js`, `restaurants.html`, `pages/michelin-starred.html` | Dated 2026 roster: 41 Bay Area-city entries (27 one-star, 7 two-star, 7 three-star; incl. Yountville). Prices/socials/most hours flagged. |
| T3 | Bib Gourmand / Guide-listed, not starred | needs review | integration | `data.js`, `restaurants.html`, `pages/suggestions.html` | Eight Bib Gourmand examples; not exhaustive. |
| T4 | Hotels selected/ranked by nearby restaurant density | needs review | integration | `data.js`, `hotels.html`, `pages/executive-summary.html` | Four MICHELIN-Key candidates; no unsupported proximity rank or room prices. Radius/travel mode/dates unresolved. |
| T5 | Verified social links (YouTube / TikTok / Instagram) | needs review | integration | `data.js`, `restaurants.html` | No account filled without official-source confirmation. |
| T6 | Restaurant total for two adults | needs review | integration | `data.js`, `restaurants.html` | No official all-in totals confirmed; left blank and flagged. |
| T7 | Executive summary, questions, decision support, suggestions | done | `e71de712` + integration | `index.html`, `decision-brief.html`, `suggestions.html`, `review.html`, existing `pages/*` | Executive brief, known/unknown Q&A, selectable proposals, flag page published. |
| T8 | Responsive Pages dashboard and category pages | done | `e71de712` + integration | `index.html`, `restaurants.html`, `clusters.html`, `hotels.html`, `decision-brief.html`, `suggestions.html`, `review.html`, `sources.html`, `styles.css`, `app.js`, `subpages.js` | Earlier session's pages/data/review retained; root dashboard is the entry point. |
| T9 | Final integration, reconcile sources, build/links, publish | done | integration | all shared outputs | PR #3 merged; Pages build succeeded; category pages verified. |
| T10 (this session) | Research: official Michelin Guide SF Bay Area list (starred vs Bib Gourmand) | done | `session-arena-e4732d51` | `data/restaurants.json`, `data/bibgourmand.json` | 29 SF-region starred (4×3★, 7×2★, 18×1★) + 30 Bib Gourmand, verified vs guide.michelin.com 2026 guide. |
| T11 (this session) | Research: 2-adult pricing, hours, days, exceptions, social links | done | `session-arena-e4732d51` | `data/restaurants.json`, `data/bibgourmand.json` | Pricing/hours verified from official restaurant sites where confirmable: Benu (benusf.com/info), Acquerello (acquerellosf.com), Kiln (kilnsf.com/information), Commis (commisrestaurant.com/info), Birdsong (birdsongsf.com/experience). Conflicting/stale sources flagged unverified and never inferred (Quince, Californios, Saison, Sons & Daughters, Lazy Bear, Atelier Crenn). Bib Gourmand details blank/unverified. Verified data published to GitHub Pages main. |
| T12 (this session) | Build: landing page + category subpages, tables, executive summary, suggestions, questions | done | `session-arena-e4732d51` | `index.html`, `pages/*.html`, `css/style.css`, `js/app.js` | Responsive client-side dashboard; blank/unverified flagged per policy. Preserved in this merge as complementary files alongside the root dashboard. Live site published at https://kanlerxz87-cyber.github.io/Baymich1/ |
| T13 (session `arena-6f1a05c4`) | Repo review refresh: count/data conflicts, inferred values, stale hours | in progress | `arena-6f1a05c4` (branch `arena/6f1a05c4-baymich1`) | `pages/repo-review.html`, `data/bay-area-starred.json`, `COORDINATION.md` | Claimed. |
| T14 (session `arena-6f1a05c4`) | Official Michelin roster reconciliation (SF region 29 starred) with links | done | `arena-6f1a05c4` | `data/bay-area-starred.json`, `data/bay-area-starred.md` | 29 starred (4×3★, 7×2★, 18×1★) matched to official SF-region header and per-row Michelin pages. Bay Area names outside the SF region not fully reconciled (open item). |
| T15 (session `arena-6f1a05c4`) | Hours, days open, exceptions, price bracket, address from official Michelin restaurant pages | needs review | `arena-6f1a05c4` | `data/bay-area-starred.json`, `data/bay-area-starred.md` | Hours, address, cuisine, Michelin price, website and phone captured for all 29 from official pages (Niku hours captured in a later page chunk). Holiday exceptions and 2-adult cost not captured; flagged unverified. |
| T16 | Social links (YouTube / TikTok / Instagram) | unclaimed | — | — | Next session to claim. |
| T17 | Hotel ranking by nearby starred-restaurant density | unclaimed | — | — | Needs radius/mode/date decision from user. |
| T18 | Site rebuild from verified data (index/nav/table data) | unclaimed | — | — | Shared outputs: final integration session only. |

## Log

### L6 — Session `arena-6f1a05c4` — T14/T15 outputs
- Output: `data/bay-area-starred.json` and `data/bay-area-starred.md` (29 starred, SF region). Sources: official 2026 California article plus each official restaurant page at guide.michelin.com/us/en/california/...
- Not captured: 2-adult costs, social links, holiday exceptions (flagged unverified per row). Bay Area one- and two-star names outside the SF region are not yet reconciled.
- Cross-session requests (not edited here): `README.md`, `index.html`, `data.js` and `scripts/build_site.py` still show 41 starred; `data/restaurants.json` has stale rows. Requested for the final integration session (T18). Log only.
- T16–T18 added as unclaimed rows; not started.

### L5 — Session `arena-6f1a05c4` (branch `arena/6f1a05c4-baymich1`) — claim
- Claimed T13–T15 on the Arena-assigned branch only (no other branches created or switched). Scope: repo review refresh, official roster reconciliation, official hours/price/address pages for starred entries.
- Rows T16–T18 (social links, hotel ranking, site rebuild) will be claimed after T13–T15 are committed.


### L1 — Session `e71de712` — initial claim and repository review
- Claimed T1–T9 on its Arena branch. Starting repository was the initial commit and a minimal README; `COORDINATION.md` did not yet exist.
- Created `pages/repo-review.html`, based on the starting repository state, with source links for each finding.

### L2 — Session `e71de712` — initial restaurant data and dashboard
- Source: MICHELIN Guide, “Every MICHELIN-Starred Restaurant in California for 2026,” 24 Jun 2026: <https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california>.
- Created a 41-row Bay Area city/county dataset and cited official restaurant profile pages. Dataset clearly marks incomplete values.
- Existing outputs retained at `data/michelin_bay_area_stars.json`, `pages/*`, `assets/style.css`, `scripts/build_site.py`; no file from that session was removed.

### L3 — Session `arena/fe2115f0-baymich1` — integration/dashboard and reconciliation
- Preserved the earlier session's data, page files, site-generation script, and repository review. Rechecked the official 2026 MICHELIN roster; roster corrected to **41** (7 three-star), Wine Country **8**.
- Added The French Laundry (3-star, Yountville) confirmed via <https://guide.michelin.com/us/en/california/yountville/restaurant/the-french-laundry>.
- PR #3 merged to `main` at `87e24bc97ce484f8ef057d4d99caf36b7f140a6c` on 2026-11-24 at 08:56 UTC. GitHub Pages build completed `built` at 08:57:10 UTC. Live dashboard confirmed at <https://kanlerxz87-cyber.github.io/Baymich1/>.

### L4 — Session `session-arena-e4732d51` (branch `arena/e4732d51-baymich1`) — this session
- Branched from `main` at `3fa14d7`. Researched the official MICHELIN Guide San Francisco region pages (all-starred + Bib Gourmand, 2026 guide, announced 24 Jun 2026).
- Created `data/restaurants.json` (29 SF-region starred: 4×3★, 7×2★, 18×1★) and `data/bibgourmand.json` (30 Bib Gourmand). Distinction/city/cuisine/Michelin price bracket verified against guide.michelin.com.
- Verified pricing/hours from official restaurant sites where confirmable: Benu, Acquerello, Kiln, Commis, Birdsong. Conflicting/stale sources flagged unverified and never inferred (Quince, Californios, Saison, Sons & Daughters, Lazy Bear, Atelier Crenn).
- Built a responsive client-side dashboard: landing page + category subpages (all/starred/Bib Gourmand/clusters/hotels/executive-summary/suggestions/questions), searchable tables with per-entry sources and verified/unverified flags.
- Conflict note: merging into `main` produced add/add conflicts in `COORDINATION.md`, `index.html`, `pages/executive-summary.html`, `pages/suggestions.html`. Resolved by preserving the `main` (integration session) versions of the three HTML files and retaining this session's data files and complementary pages; no earlier session-owned files were deleted.
- PR #5 merged to `main` (merge commit `9ffa2ed`) on 2026-11-24. GitHub Pages build `built`; live site confirmed at <https://kanlerxz87-cyber.github.io/Baymich1/>.

### Verification performed by this session
- Fetched official MICHELIN Guide San Francisco region pages (all-starred + Bib Gourmand). Confirmed 29 starred (4×3★, 7×2★, 18×1★) and 30 Bib Gourmand.
- Verified distinction, city, cuisine and Michelin price bracket against guide.michelin.com for all 59 restaurants.
- Verified 2-adult pricing/hours from official restaurant sites where confirmable: Benu ($425 pp + 22% service, benusf.com/info), Acquerello ($295 pp seasonal tasting + 20% service + 4% surcharge, acquerellosf.com), Kiln ($315 pp + 20% service, kilnsf.com/information), Commis ($279 pp + 20% service, commisrestaurant.com/info), Birdsong (Journey $350 / Discovery $290 pp, birdsongsf.com/experience).
- Missing fields left blank and flagged unverified; never inferred.

## Irregularities / open review flags
- No all-in price for two adults verified from official current menu and fee sources.
- Most restaurant schedules, special-date exceptions and official social accounts are not verified; empty fields are intentional.
- Hotel area-density ranking cannot be computed safely until a radius or mode/time threshold and date are selected and validated.
- Bib Gourmand list is a sample, not a full non-starred MICHELIN Guide selection.
- Broad MICHELIN “San Francisco and surroundings” live-filter counts can include surrounding results and differ from a declared city-scoped roster; use the dated annual roster for counts and the live directory for individual current details.
