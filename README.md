# Bay Michelin — San Francisco Bay Area field guide

A source-first, responsive GitHub Pages guide for Michelin-starred restaurants, selected Bib Gourmand restaurants, hotel candidates, regional clusters, decision gaps and follow-up suggestions.

## Live site

The repository’s GitHub Pages publishing source is the `main` branch at the repository root. After the site update is merged and Pages finishes publishing, visit:

<https://kanlerxz87-cyber.github.io/Baymich1/>

## Scope and evidence

- Current starred entries use the official MICHELIN Guide California 2026 selection, revealed June 24, 2026. The roster is filtered to the named Bay Area cities displayed in the site: **40 restaurants**.
- Eight Bib Gourmand entries are samples, not the full non-starred Guide selection. Bib Gourmand is clearly separated from Michelin Stars.
- All restaurant entries link to an official MICHELIN Guide profile. Hotel candidates link to official MICHELIN hotel profiles.
- Missing price, social, operating-hour and distance fields are intentionally unfilled and flagged. Broad MICHELIN price symbols are not converted into a total for two adults.
- Hotel candidates are not ranked by nearby restaurant count because no distance radius or travel mode was supplied/verified. Michelin Key awards are kept distinct from restaurant stars.

See [COORDINATION.md](COORDINATION.md) for task ownership and verification status. See the site’s Sources page for primary-source links and limitations.

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
