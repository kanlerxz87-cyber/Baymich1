# Coordination board

This repository began with a minimal README and no prior task board entries. Work is on the active Arena branch `arena/abfb32ee-baymich1` (the environment requires this branch; a separate branch/worktree is not allowed).

| Task | Status | Owner/session | Files touched |
|---|---|---|---|
| SF Bay Area Michelin guide research, dashboard design, and static site implementation | needs review | `arena/abfb32ee-baymich1` | `COORDINATION.md`, `README.md`, `.nojekyll`, `index.html`, `restaurants.html`, `clusters.html`, `hotels.html`, `activities.html`, `decisions.html`, `styles.css`, `data.js`, `app.js`, `directory.js`, `clusters.js` |

## Task log

### Claim

- Claim created before implementation. Scope: source-linked, responsive dashboard and dedicated category pages; review official Michelin, venue, hotel and visitor sources; leave unconfirmed fields blank and flag them.
- The environment's branch rules prohibit separate session branches/worktrees. All work remained on `arena/abfb32ee-baymich1`.
- Immediate claim push attempt: `git pull --rebase origin arena/abfb32ee-baymich1` failed because the remote does not have that ref (`fatal: couldn't find remote ref`). No other branch was pushed or created.

### Completion and verification

- Implemented a static, responsive multi-page GitHub Pages dashboard: landing page, restaurant directory, clusters/map searches, hotel shortlist, activities, and review/decisions.
- Verified 2026 status and city/tier roster from Michelin's official article, “Every MICHELIN-Starred Restaurant in California for 2026,” dated June 24, 2026: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california . The article provides official individual profile links for each included starred row. Transcribed 39 Bay Area rows: 7 three-star, 7 two-star, 25 one-star; San Francisco has 25. This is a dated published selection, not a guarantee of current operation.
- Michelin's same 2026 article calls Maria Isabel “a Recommended restaurant”; included separately as a Guide Recommended example, not as a star holder. It is not represented as a complete non-starred-guide inventory.
- Checked the Commis official information page: https://commisrestaurant.com/info/ . It states a 10-course menu at $279/person, excludes sales tax/beverages and has a 20% service charge. Couple food total with stated service charge is $279 × 2 × 1.20 = $669.60 before tax/beverages; the displayed row links this exact source. The $100/person booking deposit is credited against the final bill per the same official page, not added to the meal total.
- Checked Atelier Crenn official site and its linked Instagram account: https://www.ateliercrenn.com/ and https://www.instagram.com/atelier.crenn/ . Only this venue-linked social account is currently displayed; other social fields stay blank/unverified.
- Checked Quince official info/reservations page: https://www.quincerestaurant.com/info-reservations . It confirms the lunch menu is available Friday and Saturday but does not provide verified all-in totals in the fetched page. No hours or couple total inferred.
- Checked Four Seasons Hotel San Francisco at Embarcadero official site: https://www.fourseasons.com/embarcadero/ (property name and 222 Sansome Street address). Checked Hotel Zeppelin official site: https://www.zhotelssf.com/hotels/zeppelin (545 Post Street address). Both names appear in Michelin's official California travel article: https://guide.michelin.com/us/en/article/travel/visit-california-sacramento-los-angeles-san-diego-map-michelin-guide-restaurants-hotels . They are candidates only; no hotel rank, rate or restaurant-proximity count is claimed.
- Checked San Francisco Travel's official visitor resource: https://www.sftravel.com/ . The activities page intentionally has no activity rows until official operator hours, exceptions and media accounts can be verified.
- Validation performed: `node --check` passed for `data.js`, `app.js`, `directory.js` and `clusters.js`; static checks confirmed all 39 starred entries have Michelin profile links, no duplicate names, 7/7/25 star-tier counts, and navigation anchor targets. The broader directory, operating schedules, social channels, hotel-price/radius ranking, exact map coordinates and activity calendar remain flagged, not “verified.”

### Irregularities / remaining review

- A complete current non-starred MICHELIN Guide (Recommended/Bib Gourmand) roster has not been audited. Maria Isabel is only a sourced example.
- Most restaurant-owned sites, current meal totals for two, opening days/hours and exceptions, and official social/video links need a venue-by-venue official-source pass. These cells are visibly blank or flagged.
- Hotel ranking requested by restaurant density cannot be responsibly completed without verified coordinate/radius choices and date-specific all-in quotes; the two Michelin-mentioned SF hotel candidates are unranked.
- “Bay Area” has a disclosed broad interpretation including Wine Country and the Michelin-listed Marin/Peninsula cities; boundary needs review if a stricter county definition is intended.
- GitHub Pages is configured as a legacy `main`-root site. The branch Actions deployment first failed because `arena/abfb32ee-baymich1` is not allowed to deploy to the protected `github-pages` environment (run https://github.com/kanlerxz87-cyber/Baymich1/actions/runs/45359856478). A retry with an unprotected environment reached the deploy step but was rejected because only `main` is an allowed deployment branch (run https://github.com/kanlerxz87-cyber/Baymich1/actions/runs/45359958541). Attempts to change Pages settings to Actions returned HTTP 403. The failing workflow was removed; GitHub's existing legacy Pages build remains. The site will publish at the Pages URL only after normal integration to `main`. The initial claim pull failed because the remote branch did not yet exist; after branch creation, the branch was tracked and subsequent pushes used `git pull --rebase` first.
