# Audit T13 — star-dataset cross-check and irregularities

**Session:** `775cc15c` · **Branch:** `arena/775cc15c-baymich1` · **Date checked:** 2026-11-24
**Type:** read-only audit. No shared outputs (data files, `index.html`, `pages/*`, navigation) were changed. Those changes are reserved for the integration session.

## 1. Method

1. Compared the three repo datasets row by row on name, star level, and city:
   - `data/michelin_bay_area_stars.json` (`starred`, 41 entries)
   - `data/restaurants.json` (29 entries)
   - `data.js` (41 entries, `window.BAY_DATA`)
2. Fetched official MICHELIN Guide pages to confirm star level, address, price symbol, and hours for a sample of entries.
3. Logged each finding below with the page it came from.

## 2. Results

### 2a. Dataset consistency: passed

| Check | Result |
|---|---|
| Star level, roster (41) vs `restaurants.json` (29) | **0 mismatches** on the 29 shared entries |
| City, roster vs `restaurants.json` | **0 mismatches** |
| `data.js` names/stars vs roster | **0 mismatches** (41 rows) |
| Name variant | `Naides` (roster) = `Restaurant Naides` (restaurants.json). Same restaurant; the name should be normalised in the integration pass. |

Star counts by file: roster 27×1★, 7×2★, 7×3★ (41). `restaurants.json` 18×1★, 7×2★, 4×3★ (29). The 12-entry difference is the Napa, Sonoma, and Peninsula/Santa Clara entries (for example The French Laundry, Cyrus, Singlethread, Auberge du Soleil, Plumed Horse, Protégé), which the roster includes and the 29-entry file excludes.

### 2b. Official-source spot checks

| Restaurant | Repo value | Official MICHELIN page shows | Result | Source |
|---|---|---|---|---|
| Californios | 3★; hours `Tue–Sat 5:00pm–9:00pm` (`restaurants.json`); roster says `Tue–Sat 5–10 PM` marked VERIFIED | Address 355 11th St.; 3 Michelin star icons; Tue–Sat **5 PM–10 PM**; Sun & Mon closed; price symbol `$$$$`; website `californiossf.com`; phone +1 415-757-0994 | **Closing time conflict** (9pm in `restaurants.json`, 10pm on Michelin page). The roster's "VERIFIED" tag is supported by the Michelin page, not by the restaurant's own site, so the restaurant's own site still needs checking. | <https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios> |
| Restaurant Naides | 1★; address "Not confirmed"; hours null; website null | 708 Bush St., San Francisco, CA 94108; 1 star icon; Thu–Sun **5:30 PM–8:30 PM**; Mon–Wed closed; price `$$$$`; website `restaurantnaides.com`; Tock booking link | **Gap.** The official page has the address, hours, and website, but `restaurants.json` still has them blank. Suggest the integration session fill these from the official page. | <https://guide.michelin.com/us/en/california/san-francisco/restaurant/naides> |
| Official article (scope check) | Roster = 41 "Bay Area" entries | Article: "a total of 83 Starred restaurants" statewide for California 2026, and it names Californios as the first three-star Mexican restaurant in the world and Naides as a new one-star | Confirms the statewide total and that the roster is a filtered subset. The 41-entry roster is not the full statewide list. | <https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california> |

### 2c. Irregularities to flag for review

| # | Severity | Irregularity | Where | Action proposed |
|---|---|---|---|---|
| I-1 | **High** | **Derived price presented as a verified total.** Californios `estPrice2AdultsTotal` = "$650–$900 food only (2 adults)". This is 2 × the per-person range ($325–$450) and is not stated by any source. The policy is "never infer"; this value is inferred. | `data/restaurants.json` → californios | Blank it, or replace it with a sourced total. Keep the per-person range and its source, flagged unverified. |
| I-2 | **High** | **Hours conflict.** `restaurants.json` says closes 9pm; the official Michelin page says 10pm. | `data/restaurants.json` → californios; roster `hours` | Re-check on californiossf.com (not checked this session), then correct the value to the source it matches. |
| I-3 | Medium | **Roster label is ahead of its evidence.** The roster marks Californios hours "VERIFIED" from the Michelin page, but the same record's `restaurants.json` counterpart gives a different time. Two datasets disagree on a field marked verified. | both files | Keep one canonical value; mark source and date. |
| I-4 | Medium | **Blank fields with an official value available.** Naides address, hours, website are null/"Not confirmed" even though the official page provides them. | `data/restaurants.json` → naides | Integration session fills from the official page (Section 2b). |
| I-5 | Medium | **Scope is undefined in the files.** The roster says "9 counties" (Alameda, Contra Costa, Marin, Napa, San Francisco, San Mateo, Santa Clara, Solano, Sonoma). `restaurants.json` is labelled "SF region" and holds 29 entries. The README says "Bay Area". Three different definitions are in use. | README, `restaurants.json` meta, roster `scope` | Needs a decision (Section 3, Q1). |
| I-6 | Low | **Name variant.** "Naides" vs "Restaurant Naides". | both files | Normalise to the official page title "Restaurant Naides". |
| I-7 | Low | **Duplicate, overlapping dashboards.** Root `index.html`, `data.js`, `app.js`, `subpages.js`, `styles.css`, plus `pages/*.html`, `assets/style.css`, `css/style.css`, `js/app.js`, and `scripts/build_site.py`. The build script reads `michelin_bay_area_stars.json` but not `restaurants.json`. | repo root | Integration session should pick one data source and one build path. Not changed here. |
| I-8 | Low | **Not verified in this session.** The Californios own-site price and hours, Naides' own site, and the social links are not checked. Only the Michelin pages above were fetched. | — | Listed under open items. |

## 3. Questions that block decisions (need answers, not guesses)

1. **Q1 — What is "Bay Area"?** 9 counties (roster, 41 entries), SF city + Oakland + Peninsula only (the 29-entry file), or SF city only? The answer changes every count, cluster, and hotel ranking.
2. **Q2 — Which official value is canonical for hours and price when sources differ?** For example, Californios: the Michelin page (10pm) or the restaurant's own site (not yet checked)?
3. **Q3 — Which price basis is wanted for "2 adults"?** Food only, or with tasting pairings, service, and tax? Official sources publish per-person prices, not all-in totals. Totals must be computed only from a stated formula, which should be approved first.
4. **Q4 — Which travel mode and radius define "nearby" for hotel ranking?** Walking, driving, or transit, and what minutes/kilometres? Needed before the hotel ranking can be computed.
5. **Q5 — Which dates should the open-day and hours checks use?** Hours change by season and holidays.

## 4. Suggestions for discovering missing information (no changes made)

- For each row, check the official restaurant website and the Michelin detail page. Record both URLs and the date checked.
- Use the Michelin "Visit Website" link as the starting point for official social handles, then confirm the handle on the restaurant's own site before adding it.
- Add a `checkedOn` date column to each row so stale values are visible.
- Use one canonical data file. Generate all pages from it, then run a link check.

## 5. Open items (not done in this session)

- Verify the remaining 27 starred and 30 Bib Gourmand entries against official sources (T3, T5, T6 remain "needs review").
- Hotel ranking (T4): blocked on Q1 and Q4.
- Totals for two adults (T6): blocked on Q2 and Q3.
- Mobile/readability pass of the site: integration session.
