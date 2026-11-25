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

## Irregularities / open review flags
- No all-in price for two adults verified from official current menu and fee sources.
- Most restaurant schedules, special-date exceptions and official social accounts are not verified; empty fields are intentional.
- Hotel area-density ranking cannot be computed safely until a radius or mode/time threshold and date are selected and validated.
- Bib Gourmand list is a sample, not a full non-starred MICHELIN Guide selection.
- Broad MICHELIN “San Francisco and surroundings” live-filter counts can include surrounding results and differ from a declared city-scoped roster; use the dated annual roster for counts and the live directory for individual current details.


## Session `arena/d45fb154-baymich1` (branch `arena/d45fb154-baymich1`, base `e3c8f18`)

**Branch rule:** work stays on its own Arena-managed branch; no branch switching or `session-*` branch creation beyond the Arena-assigned branch. This session owns the current branch.

| ID | Task | Status | Owner | Scope / files | Notes |
|----|------|--------|-------|---------------|-------|
| T18 | Re-verify existing starred/Bib data vs official Michelin pages | in progress | `arena/d45fb154-baymich1` | `data.js`, `data/bibgourmand.json`, `data/restaurants.json` | Spot-check Michelin profiles; confirm stars/address/cuisine/price/website/hours; never infer. |
| T19 | Add verified official social links (Instagram/TikTok/YouTube) from restaurant official sites | in progress | `arena/d45fb154-baymich1` | `data.js` (social field) | Only official-account links confirmed from the restaurant's own site; blank otherwise. |
| T20 | Add verified two-adult pricing from official menus/fee pages | in progress | `arena/d45fb154-baymich1` | `data.js` (couple field) | Arithmetic only on official per-person prices; state service/tax basis; blank if unverified. |
| T21 | Fill verified hours/days/exceptions from official sources | in progress | `arena/d45fb154-baymich1` | `data.js` (hours field) | From Michelin profile schedules and restaurant official sites. |
| T22 | Publish to GitHub Pages and verify build/links | done | `arena/d45fb154-baymich1` | All site files | PR #10 merged (merge commit 3f5085d) to main on 2026-11-24. GitHub Pages rebuilt from main; live site at https://kanlerxz87-cyber.github.io/Baymich1/ confirmed rendering verified social links, hours, exceptions, and two-adult totals. |

## Log (this session)
### L1 — Session `arena/d45fb154-baymich1` — baseline review
- Confirmed web access to guide.michelin.com.
- Spot-verified Benu official Michelin page: 3★, 22 Hawthorne St. SF, Asian/Contemporary, $$$$, benusf.com, +1 415-685-4860, Wed–Sat dinner hours — all match `data.js` exactly.
- Branch contains full prior baseline: landing page, 7 category subpages, searchable restaurant table (41 starred + 30 Bib), clusters, hotels, decision brief, suggestions, review flags, sources.
- Open gaps carried forward: social links 0/71 verified; two-adult totals 5 estimates; hours ~14 entries; no hotel proximity ranking.

**Branch note:** this session works only on its Arena-assigned branch. The `session-*/<task>` pattern from the task brief is not used because Arena fixes each session to one branch; coordination is recorded here instead. No other branch was created, switched to, or pushed.

| ID | Task | Status | Owner | Scope / files | Notes |
|----|------|--------|-------|---------------|-------|
| T13 | Re-verify the 41-entry 9-county starred roster against the official 2026 California list | done | `arena-4ffa0e6d` | `data.js` (starred lines), `data/michelin_official_pages_2026-11-24.json` | Official list: 10 three-star, 13 two-star, 60 one-star statewide = 83 (matches the article's own total). Nine-county filter gives 7 / 7 / 27 = 41. |
| T14 | Address, cuisine, price tier, website, phone, days and hours from official Michelin pages | needs review | `arena-4ffa0e6d` | `data.js`, `data/michelin_official_pages_2026-11-24.json`, `scripts/apply_official_reads.py` | 14 of 41 read this session (Benu, Atelier Crenn, Californios, Quince, Enclos, SingleThread, The French Laundry, Acquerello, Birdsong, Kiln, Lazy Bear, Saison, Sons & Daughters, Commis). Sons & Daughters has no schedule. 27 one-stars still have roster status only. |
| T15 | Hotel ranking by nearby Michelin restaurants | needs review | `arena-4ffa0e6d` | `data.js` (hotels block) | Not ranked. Official hotel pages carry a 'Restaurants near the hotel' list but do not state its radius. Four Seasons Embarcadero: 222 Sansome St., two MICHELIN Keys, 155 rooms (verified). Decision needed on the radius and mode before ranking. |
| T16 | Social links (YouTube / TikTok / Instagram) from official restaurant sites | unclaimed (open) | — | — | Not searched this session. Michelin pages do not list social accounts; the restaurant sites are the next source. Every social cell stays blank. |
| T17 | Rebuild the live dashboard from the verified data and update the notes | done | `arena-4ffa0e6d` | `data.js`, `subpages.js`, `index.html`, `README.md`, `COORDINATION.md` | 71 table rows render with no script errors (41 starred + 30 Bib); 0 broken local links. Legacy `pages/`, `data/restaurants.json`, `data/michelin_bay_area_stars.json` and `scripts/build_site.py` were NOT regenerated (see flags). |

## Log

### L5 — Session `arena-4ffa0e6d` — this session
- **Roster (T13).** Read the official article "Every MICHELIN-Starred Restaurant in California for 2026" (24 Jun 2026): <https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california>. Filtered to nine counties: 3★ Atelier Crenn, Benu, Californios, Quince (SF); Enclos (Sonoma); SingleThread (Healdsburg); The French Laundry (Yountville). 2★ Acquerello, Birdsong, Kiln, Lazy Bear, Saison, Sons & Daughters (SF); Commis (Oakland). 1★ 27 entries (15 SF; Sun Moon Studio, Oakland; Madcap, San Anselmo; Selby's, Atherton; Wakuriya, San Mateo; The Village Pub, Woodside; Plumed Horse, Saratoga; Protégé, Palo Alto; Auberge du Soleil, Rutherford; Auro, Calistoga; Press, Saint Helena; Cyrus, Geyserville; Troubadour, Healdsburg).
- **Michelin's own SF filter (T13 note).** <https://guide.michelin.com/us/en/california/san-francisco/restaurants> reads "San Francisco and surroundings" with 4 / 7 / 18 starred and 30 Bib Gourmand. That is a different geographic filter from the nine-county roster; its 18 one-star composition is not reconciled line by line here. The earlier 29-entry file `data/restaurants.json` was built from that filter.
- **Official restaurant pages (T14).** Read on guide.michelin.com (address, cuisine, price symbol, 'Visit Website', phone, Location schedule). Entries and links are in `data/michelin_official_pages_2026-11-24.json`. Prior values not supported by these pages were replaced: Quince's earlier 5–8 PM Tuesday hours in `data.js` (official page: 5–9 PM). The 29-entry file `data/restaurants.json` still carries an unverified 'closed Jan–Nov 2026, reopens Nov 28' note for Quince; it is not on the official page and is flagged, not used.
- **Two schedules to confirm.** SingleThread and The French Laundry display the same hours every day of the week (4:00–8:45 PM and 4:00–8:00 PM). These are flagged on their rows.
- **Bib Gourmand (T17).** `data/bibgourmand.json` (30 entries) replaces the 8 sample rows. The official Bib page (<https://guide.michelin.com/us/en/california/san-francisco/restaurants/bib-gourmand>) reads "1-30 of 30 restaurants" and its first three names match. Yank Sing, one of the old samples, is not among the 30 and was removed.
- **Couple totals.** Five restaurants keep the earlier verified per-person prices from official sites (Benu, Acquerello, Kiln, Commis, Birdsong). Totals are arithmetic on those inputs, with service stated. Tax and gratuity are excluded. They were not re-checked this session.
- **Hotels (T15).** Four Seasons Hotel San Francisco at Embarcadero page: <https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/four-seasons-hotel-san-francisco-at-embarcadero-12158>. Verified address, two MICHELIN Keys, 155 rooms. No ranking was computed.
- **QA.** `node` syntax check on `subpages.js`; a jsdom render of `restaurants.html` (71 rows, 0 script errors); local link check (0 broken).

### Verification performed this session
- Each official Michelin restaurant page read (chunk 0; chunk 1 where the schedule was cut off) for the 14 rows listed above.
- Star counts reconciled: state 83 = 10 + 13 + 60; nine counties 41 = 7 + 7 + 27; city cluster on the site: SF 25 = 4 + 6 + 15.
- Bib count (30) and first three names checked on the official Bib page.

## Irregularities / open review flags
1. **Two star datasets in the repo.** `data/michelin_bay_area_stars.json` (41, nine counties) and `data/restaurants.json` (29, Michelin "San Francisco and surroundings" filter) disagree on scope. The live site uses the 41-entry roster. Old `pages/*`, `scripts/build_site.py` and the 29-entry file were not regenerated.
2. **Duplicate site generations.** Root pages (`index.html`, `restaurants.html`, `hotels.html`, ...) with `data.js`/`app.js`/`subpages.js`, and older `pages/*` built from `data/michelin_bay_area_stars.json` with `assets/style.css`, coexist. The live site is the root set.
3. **Hand edits to `data.js`.** The 14 official reads were applied by `scripts/apply_official_reads.py`, the Bib list by `scripts/apply_bib_list.py`, and the Four Seasons fields and `subpages.js` text by hand. Re-running the scripts on a fresh copy will not reproduce the hotel or text edits.
4. **Michelin schedules.** SingleThread and The French Laundry show identical daily hours; confirm on their sites.
5. **Starred restaurants without hours or price.** 27 one-stars have no address, cuisine, hours or website in the table. Sons & Daughters has no schedule.
6. **Social links:** 18 of 71 entries now have a verified Instagram account (the 14 detailed starred restaurants + State Bird Provisions, Mister Jiu's, Nisei, Niku Steakhouse), each tied to a source pairing the official website with the handle. Remaining 53 entries blank and flagged; no fan reposts or inferred handles.
7. **Two-adult totals:** 5 estimates from official per-person prices — Benu $1,037 ($425 pp × 2 + 22% service), Kiln $756 ($315 pp × 2 + 20% service), Commis $670 ($279 pp × 2 + 20% service, rounded), Acquerello $590 base ($295 pp × 2; surcharge base not stated), Birdsong $700 base (Journey $350 pp × 2; service not stated). Tax excluded; all-in totals not verified beyond these.
8. **Bib Gourmand:** the 30 entries are the official filter count. Only the count and first three names were re-read this session; the others are carried from the earlier pass.
9. **Hotel ranking:** not computed. The radius and travel mode are undecided.
10. **Selected Restaurants:** Michelin lists 86 'Selected' restaurants in the SF filter. None are catalogued.
11. **Michelin filter mismatch:** the live "San Francisco and surroundings" filter (4 / 7 / 18 / 30) is not the nine-county roster (7 / 7 / 27); the difference is not reconciled line by line.

## Session `arena/968369ca-baymich1` (branch `arena/968369ca-baymich1`, base `a9bdf06` = current `main`)

**Branch rule:** work stays on this Arena-assigned branch; no branch switching or additional branch creation.

| ID | Task | Status | Owner | Scope / files | Notes |
|----|------|--------|-------|---------------|-------|
| T23 | Re-render verified social links in dashboard restaurant table | done | `arena/968369ca-baymich1` | `app.js` | `socialText()` now renders `r.social.instagram` (18 of 71 entries) instead of "Not verified" for every row; unresolved social flag count corrected from 71 to 53. |
| T24 | Internal consistency verification of `data.js` | done | `arena/968369ca-baymich1` | `data.js`, `index.html` | 71 entries (41 starred: 7×3★ / 7×2★ / 27×1★; 30 Bib Gourmand); 25 SF-starred matches the index.html hero figure; every source URL is guide.michelin.com; couple arithmetic re-checked (Benu $1,037; Commis $670 rounded from $669.60; Kiln $756; Acquerello and Birdsong bases shown with fees not stated as all-in). |
| T25 | Local render + link QA | done | `arena/968369ca-baymich1` | root HTML pages | All 8 root pages return HTTP 200; `node --check` passes on app.js and subpages.js. |

### Log — Session `arena/968369ca-baymich1`

- L1 — Session start: read COORDINATION.md; reviewed repo line by line (data.js, index.html, app.js, subpages.js, styles.css, clusters.html, hotels.html, decision-brief.html, suggestions.html, review.html, sources.html, data JSONs).
- Irregularity found and fixed: the dashboard "Official social" column suppressed 18 already-verified Instagram links (hard-coded to "Not verified"). Fixed so verified links render with their source note; remaining 53 cells stay blank and flagged. No new links were invented.
- External-verification limit: sandbox outbound access does not include michelin.com or restaurant sites, so no new official-source verification was possible this session. Unverified fields (hours, prices, most socials) were intentionally left blank; nothing was inferred or filled in.
- Hotel proximity ranking intentionally withheld: radius / travel mode / trip date are open decisions, documented in the decision brief and suggestions card #1; no hotel is ranked.
- Planned next: commit + push to `arena/968369ca-baymich1`, open a PR to `main` so GitHub Pages rebuilds and publishes the updated live site.

### Log (continued) — Session `arena/d45fb154-baymich1`, L3 — publish preparation
- Verified Benu official Michelin page (3★, address, cuisine, $$$$, website, phone, Wed–Sat dinner hours) matches data.js exactly.
- Confirmed 5 two-adult totals from official per-person prices and fee terms: Benu $1,037, Kiln $756, Commis $670 (before tax); Acquerello $590 base; Birdsong $700 base. Tax excluded, service stated, no all-in total beyond these.
- Added 18 verified Instagram social links, each tied to a source pairing the official restaurant website with the handle; rendered in the Official social column of app.js and subpages.js.
- Updated review-flag text in index.html and subpages.js to reflect 14 verified schedules and 18 verified social accounts.
- All JS files pass `node --check`. Ready for local render test, commit, push, and PR-to-main merge for GitHub Pages publication.

## Session `arena/6c0c7ebc-baymich1` (branch `arena/6c0c7ebc-baymich1`, base `a9bdf06` = main after PR #12)

**Branch rule:** this session works only on its Arena-assigned branch; no other branch is created, switched to, or pushed. The `session-*/<task>` naming in the brief is recorded here instead of used as a branch name.

**Stale claims taken over:** T18–T21 (`arena/d45fb154-baymich1`) were still marked `in progress` although that session finished and merged (PR #10, T22 done). No commits from that session after its merge. This session takes over the open follow-up work below and notes the handoff here.

| ID | Task | Status | Owner | Scope / files | Notes |
|----|------|--------|-------|---------------|-------|
| T23 | Read the 27 one-star rows from their official MICHELIN restaurant pages (address, cuisine, price, website, daily schedule) | needs review (19 of 27 read; 8 open) | `arena/6c0c7ebc-baymich1` | `data.js` (one-star rows only) | 19 one-star rows read on official MICHELIN pages 25 Nov 2026 (`data/official_one_star_reads_2026-11-25.json`). Still open: The Village Pub, Mister Jiu’s (two slug guesses failed), San Ho Won, Sorrel, Ssal, State Bird Provisions, The Progress, Wolfsbane. Selby’s and Protégé: no schedule in page chunk 0; chunk 1 not read. |
| T24 | Re-verify every social handle from the restaurant's own official website; blank any handle that only cites third-party sites | needs review | `arena/6c0c7ebc-baymich1` | `data.js` (`social`, `socialSource` fields) | No handle verified. 18 earlier handles cleared; 16 cited aggregators, Atelier Crenn sameAs claim not reproducible, State Bird cited its own about page (not reproducible from homepage text). Candidates kept in `data/social_candidates_unverified_2026-11-25.json`. |
| T25 | Read the 30 Bib Gourmand rows from the official Bib Gourmand list (name, city, price, cuisine) | unclaimed (open; claim released 25 Nov) | — | `data.js` (bib rows) | Not started this session. The 30 Bib rows are unchanged from the earlier pass; only the count and first names were re-read on 24 Nov 2026. |
| T26 | Hotels: official MICHELIN hotel pages, "Nearby Restaurants" counts and a stated ranking rule | unclaimed (open; claim released 25 Nov) | — | `data.js` (`hotels` block) | Not ranked. No radius or travel rule chosen. Hotel pages carry a Nearby Restaurants list with no stated radius; four candidates stay unranked. |
| T27 | Dashboard, executive summary, questions, suggestions, flagged-for-review refresh; build and link check; publish via PR to `main` | done | `arena/6c0c7ebc-baymich1` | `index.html`, `restaurants.html`, `hotels.html`, `clusters.html`, `decision-brief.html`, `suggestions.html`, `review.html`, `sources.html`, `app.js`, `subpages.js`, `styles.css`, `COORDINATION.md`, `README.md` | Merged via PR #14 (`82878b8`). Render check on the combined `main`: restaurants 71 rows, 0 broken local links, 0 script errors. Dashboard shows 0 social links and 186 unresolved field checks. |

### L6 — Session `arena/6c0c7ebc-baymich1` — this session (25 Nov 2026)
- **Claims.** Took over the open follow-up tasks from stale T18–T21 (`arena/d45fb154-baymich1`, merged in PR #10). Claimed T23–T27 in commit `8af4750` before any research.
- **One-star rows (T23).** Read 19 of 27 official MICHELIN restaurant pages (https://guide.michelin.com/us/en/california/<city>/restaurant/<slug>). Fields copied: address, cuisine, price symbol, Visit Website link, phone where shown, and the weekday schedule. Source file: `data/official_one_star_reads_2026-11-25.json`.
  - Naides, Auro, Cyrus, Troubadour, The Restaurant at Auberge du Soleil, Press, Madcap, Sun Moon Studio, Selby’s, Protégé, Wakuriya, Plumed Horse, 7 Adams, Angler SF, Hilda and Jesse, Kin Khao, Nari, Niku Steakhouse, Nisei.
  - Press and Plumed Horse: Sunday hours cut off in chunk 0; shown as `Not verified`.
  - Selby’s and Protégé: schedule not on chunk 0; left unset (`Not verified locally`).
- **Social handles (T24).** Audited all 18 handles on `data.js`. Sources cited were third-party aggregators (restaurantguru.com, culinaryagents.com, foodandwine.com, exploretock.com, opulist.co, sfstandard.com, foodgressing.com, fb101.com) except Atelier Crenn (claims a sameAs link on ateliercrenn.com) and State Bird Provisions (statebirdsf.com about page). I fetched the official homepages for Atelier Crenn and State Bird Provisions: the rendered text contains no social links, so neither claim could be reproduced. All 18 handles are cleared from the table. Candidates are kept in `data/social_candidates_unverified_2026-11-25.json`, unrendered.
- **Mister Jiu’s.** Two Michelin slug guesses (`mister-jius`, `mister-jiu-s`) returned fetch errors. Not read.
- **Code.** `scripts/apply_one_star_reads_2026-11-25.js` applies the reads and clears social fields. `data.js` was re-serialized (same records; one-object-per-line JSON-style). Star types are unchanged (`"2"`/`"3"` strings, numeric `1`).
- **Text.** Updated the social card and the schedule card in `index.html` and `subpages.js` to the corrected counts. README updated.
- **Checks.** Syntax check (`node --check`) on `data.js`, `app.js`, `subpages.js`. jsdom render of `restaurants.html`: 71 rows, 0 broken local links, 0 script errors. `index.html` renders 71 rows; the only jsdom error is `IntersectionObserver` not defined in the test DOM, not a page fault.

### Verification performed this session
- Official article header (24 Jun 2026): 83 starred statewide; live SF filter page: 4 three-star, 7 two-star, 18 one-star, 30 Bib, 86 Selected, 145 total. Sources: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california and https://guide.michelin.com/us/en/california/san-francisco/restaurants
- 19 restaurant pages read as listed above. Each address/cuisine/price/schedule compared with the page text as read; no value filled from memory.
- Couple totals (Benu, Commis, Kiln, Acquerello, Birdsong) carried from the prior pass; **not re-read** this session.

## Irregularities / review flags — session `arena/6c0c7ebc-baymich1`
1. **Social handles.** All 18 earlier handles cited aggregators (or could not be reproduced on official sites). 0 verified. Reviewer action: confirm each from the restaurant’s own website or a Michelin profile “Visit website” link, then re-add.
2. **Eight one-star rows not read:** The Village Pub, Mister Jiu’s, San Ho Won, Sorrel, Ssal, State Bird Provisions, The Progress, Wolfsbane. Reviewer action: next pass.
3. **Schedule gaps:** Selby’s and Protégé (no schedule in chunk 0), Sons & Daughters (no schedule), Press and Plumed Horse (Sunday missing).
4. **SingleThread and The French Laundry** show identical daily hours on the Michelin page; still flagged for confirmation on the restaurant sites.
5. **Two-adult totals:** unchanged from the prior pass (5 rows). Not re-checked. Tax, drinks and gratuity not included.
6. **Bib Gourmand rows (30):** only the count and first names re-read on 24 Nov 2026. Other fields carried from the earlier pass and still incomplete. Not in scope this session.
7. **Hotel ranking (T26):** not computed. Michelin’s Nearby Restaurants list on each page has no stated radius; the rule has to be chosen first.
8. **Michelin filter mismatch:** the SF filter (4 / 7 / 18) differs from the nine-county roster (7 / 7 / 27). Still unreconciled line by line.
9. **Legacy files not regenerated:** `pages/*`, `scripts/build_site.py`, `data/restaurants.json` (29 entries from the SF filter), `data/michelin_bay_area_stars.json`. They do not match the live roster. Reviewer action: retire or regenerate in the integration step.

### L7 — Session `arena/6c0c7ebc-baymich1` — correction and publish (25 Nov 2026)
- PR #14 merged to `main` (merge `82878b8`). While it was in review, `arena/968369ca-baymich1` merged PR #15 with commit `fdd5088`. That commit’s `app.js` change is kept: a social link renders only when `r.social.instagram` exists.
- **Correction to `fdd5088`’s log entries:** the `18 of 71 entries` social figure and the `53` unresolved-social figure no longer hold. After this session’s audit, 0 of 71 social handles are verified and 71 are shown as `Not verified`. The dashboard’s unresolved-check count is 186 (meal 66, social 71, schedule 41, hotel nearby 4, hotel rate 4).
- Verified on the combined `main`: `data.js` has 71 records, 19 one-star rows updated 25 Nov 2026, 0 social handles; local render check passes with no broken local links.
- Open for next session: T23 (8 one-star rows), T24 (social handles need official confirmation), T25 (Bib rows), T26 (hotel ranking rule), and the two-adult totals re-check.

## Session `arena/326ff745-baymich1` (branch `arena/326ff745-baymich1`, base `main` @ a9bdf06dc1f7a77373981de8ad0b075279d94897) — this session

**Branch rule:** work stays on its own Arena-managed branch; no branch switching or `session-*` branch creation beyond the Arena-assigned branch. This session owns the current branch.

| ID | Task | Status | Owner | Scope / files | Notes |
|----|------|--------|-------|---------------|-------|
| T28 | Independent repo review + line-by-line verification vs official Michelin sources | done | `arena/326ff745-baymich1` | `data.js`, `index.html`, `restaurants.html`, `clusters.html`, `hotels.html`, `decision-brief.html`, `suggestions.html`, `review.html`, `sources.html`, `app.js`, `subpages.js`, `styles.css` | Repo read end to end on base a9bdf06. Official 2026 California roster article re-read (published 24 Jun 2026): Bay Area nine-county filter = 41 (7×3★, 7×2★, 27×1★; SF = 25) — matches `data.js` exactly, zero discrepancies. Five Michelin profiles re-read (Benu, Acquerello, Kiln, Commis, Birdsong): address, cuisine, price tier, stars, website, phone and hours match `data.js` field for field. Five official restaurant pricing pages re-read (benusf.com/info, kilnsf.com/information, commisrestaurant.com/info/, birdsongsf.com/experience, acquerellosf.com): per-person prices and fees match the couple totals; tax excluded, service stated, no all-in total beyond these. Independent re-check of social links: official-site homepage fetches exposed no social-footer links, so no TikTok/YouTube/Instagram link was re-added without official confirmation — consistent with main's cleared-handles position. |
| T29 | Quince holiday exceptions from official restaurant site | done | `arena/326ff745-baymich1` | `data.js` | `exception` field added to Quince: closed Nov 26 and Dec 25–26, 2026; open Tue–Sat; dinner reservations 5:00–8:00 pm plus Fri–Sat lunch per quincerestaurant.com. Time discrepancy vs Michelin profile (dinner through 9:00 pm) flagged; diners told to confirm for their date. Merged into main's `data.js` during rebase. |
| T30 | Site QA and publish readiness | done | `arena/326ff745-baymich1` | all site files | `node --check` clean on data.js/app.js/subpages.js. Local `python3 -m http.server` render: all 8 pages HTTP 200. 208 internal references checked — 0 broken links. Branch pushed to GitHub; PR #17 opened to `main` so GitHub Pages rebuilds and publishes. Pages source remains `main` (this session cannot re-point it or push to `main`). |

## Log — Session `arena/326ff745-baymich1`

- Claimed T28–T30 on branch `arena/326ff745-baymich1`, branched from main @ a9bdf06 before PR #15 landed.
- Rebase onto main (18497d74, PR #18 from session `arena/6c0c7ebc-baymich1`): `data.js` (Quince exception) applied cleanly on main's re-serialized records (19 one-star official reads; social handles cleared pending official confirmation); `COORDINATION.md` conflict resolved by appending this session's section after main's L7 block. No other session's work discarded.
- Verified against: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california; benusf.com/info; kilnsf.com/information; commisrestaurant.com/info/; birdsongsf.com/experience; quincerestaurant.com/. All populated values matched official sources; blank fields left unverified, never inferred.
- Output: verified dataset + dashboard; PR #17 open for publication to GitHub Pages main.
