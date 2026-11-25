# Bay Michelin — San Francisco Bay Area field guide

A source-first, responsive GitHub Pages guide for Michelin-starred restaurants, selected Bib Gourmand restaurants, hotel candidates, regional clusters, decision gaps and follow-up suggestions.

## Live site

The repository’s GitHub Pages publishing source is the `main` branch at the repository root. After the site update is merged and Pages finishes publishing, visit:

<https://kanlerxz87-cyber.github.io/Baymich1/>

## Scope and evidence

- **Starred (41):** the official MICHELIN Guide California 2026 list (revealed 24 June 2026), filtered to the nine Bay Area counties: 7 three-star, 7 two-star, 27 one-star. Source: <https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california>.
- **Verified in detail (33 of 41):** address, cuisine, price tier, website and phone read from each official MICHELIN restaurant page: 14 on 24 Nov 2026, and 19 one-star rows on 25 Nov 2026. 30 starred rows have a daily schedule. Selby’s and Protégé show no schedule in the page read; Sons & Daughters has none. Eight one-star rows (The Village Pub, Mister Jiu’s, San Ho Won, Sorrel, Ssal, State Bird Provisions, The Progress, Wolfsbane) are still unread. Michelin hours have no special-date exceptions, so none are assumed.
- **Bib Gourmand (30):** the official "San Francisco and surroundings" Bib Gourmand filter. Count and first three names re-read on 24 Nov 2026; the rest carried from the earlier pass. Michelin's 86 "Selected Restaurants" are not catalogued.
- **Couple totals:** five restaurants show arithmetic on official per-person prices, with service stated and tax excluded. All others are marked "Not verified".
- **Social links:** none verified. Eighteen handles from earlier passes cited aggregator sites and were cleared; they are kept only as unverified candidates in `data/social_candidates_unverified_2026-11-25.json`.
- **Hotels:** four candidates. No ranking is computed; the radius and travel mode are a pending decision.

Missing values are left blank and flagged, never inferred. See [COORDINATION.md](COORDINATION.md) for the task board, the verification log and the open-flags list, and the site's Sources and Flagged for review pages.

## Run locally

This is a static site; no build step or dependencies are required. Serve the repository root, for example:

```sh
python3 -m http.server 8080 --bind 0.0.0.0
```

## Files

- `index.html` — executive-summary landing dashboard
- `restaurants.html`, `clusters.html`, `hotels.html` — category subpages
- `decision-brief.html`, `suggestions.html`, `review.html`, `sources.html` — decision and audit subpages
- `styles.css` — responsive, accessible presentation
- `data.js` — source-linked restaurant, hotel and cluster records
- `app.js`, `subpages.js` — filters, category views and local-only suggestion choices
- `COORDINATION.md` — shared task board and verification log
