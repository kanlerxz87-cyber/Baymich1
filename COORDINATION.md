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
| T13 (session `9ac97f9f`, branch `arena/9ac97f9f-baymich1`) | Re-verify official SF-region starred roster line by line; reconcile 29 vs 41 scope; add on-list column | done | `9ac97f9f` | `data/official_sf_region_starred_2026-11-24.json` (new), `scripts/build_site.py`, `pages/michelin-starred.html`, `COORDINATION.md` | Official all-starred page: 29 of 29, all 29 names and star counts matched. 4 Peninsula/South Bay starred pages checked (not on that list). Site table now has an "On official SF-region list" column (29 Yes / 12 Not on list). |

## Log

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

### L5 — Session `9ac97f9f` (branch `arena/9ac97f9f-baymich1`) — official roster re-check
- Base: `main` @ `67a6016` (PR #6). Branch name follows the Arena assignment; the `session-*` naming above was not used.
- Sources read: <https://guide.michelin.com/us/en/california/san-francisco/restaurants/all-starred> (7 chunks, "San Francisco and surroundings: 1-29 of 29"); count cross-check <https://guide.michelin.com/us/en/california/san-francisco/restaurants> ("1-48 of 145"; 3★ 4, 2★ 7, 1★ 18, Bib 30, Selected 86).
- Restaurant pages checked for star icon: Protégé <https://guide.michelin.com/us/en/california/palo-alto/restaurant/protege>, Plumed Horse <https://guide.michelin.com/us/en/california/saratoga/restaurant/plumed-horse>, Selby's <https://guide.michelin.com/us/en/california/atherton/restaurant/selby-s>, The Village Pub <https://guide.michelin.com/us/en/california/woodside/restaurant/the-village-pub>. Each shows a single MICHELIN star icon; none is on the 29-entry SF-region list.
- Result: `data/restaurants.json` 29 names match the official list. `data/michelin_bay_area_stars.json` (41 rows, site table) mixes scopes; its own rules describe nine counties plus Napa/Sonoma, while the page header said "9-county Bay Area". Scope warning added to the Michelin starred page.
- Irregularity: the build script rewrites `index.html` and `pages/repo-review.html` (root dashboard from an earlier session is overwritten). Those two files were restored to the committed version in this session; the root landing page still needs an owner decision.

## Irregularities / open review flags
- No all-in price for two adults verified from official current menu and fee sources.
- Most restaurant schedules, special-date exceptions and official social accounts are not verified; empty fields are intentional.
- Hotel area-density ranking cannot be computed safely until a radius or mode/time threshold and date are selected and validated.
- Bib Gourmand list is a sample, not a full non-starred MICHELIN Guide selection.
- Broad MICHELIN “San Francisco and surroundings” live-filter counts can include surrounding results and differ from a declared city-scoped roster; use the dated annual roster for counts and the live directory for individual current details.
- **Scope conflict (new):** `data/michelin_bay_area_stars.json` (41, nine counties + Napa/Sonoma) vs `data/restaurants.json` and the official SF-region page (29). Not resolved: the 12 Napa/Sonoma/Peninsula rows not on the SF-region list remain unverified beyond the page-existence check; the 4 Peninsula ones show a star on their own official pages.
- **Generator overwrites root landing:** `scripts/build_site.py` writes `index.html`, which is also the root dashboard (`app.js`/`data.js`). Running the build changes that file; a decision is needed on which landing page is canonical.
- **Unverified Michelin rows:** Quince hours/price are from third-party sources in `restaurants.json` (flagged in the file); Atelier Crenn row in the 41-file uses the `/ca/` Michelin locale.
