# Bay Michelin — San Francisco Bay Area dining planner

A source-first, responsive static dashboard for the San Francisco Bay Area Michelin Guide. It presents the official Michelin California 2026 starred roster filtered to Bay Area locations, separates a clearly identified Guide Recommended example from star-holders, shows city clusters, and makes missing evidence explicit rather than filling it in.

## Open locally

Open `index.html` in a browser, or run a simple local server from the repository root:

```sh
python3 -m http.server 8000
```

## Current contents

- Landing / executive summary and dated research snapshot (`index.html`).
- Searchable and filterable restaurant directory (`restaurants.html`).
- City-cluster counts and Google Maps search links (`clusters.html`; not an address/coordinate map).
- Michelin-sourced, unranked San Francisco hotel candidates (`hotels.html`); no rates or hotel-level nearby counts are claimed.
- Activity discovery page with no unverified activity entries (`activities.html`).
- Open questions, flagged verification gaps, and a suggestion menu (`decisions.html`).

## Source and verification policy

The full star roster shown is transcribed from the [MICHELIN Guide's California 2026 star list](https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california), published June 24, 2026. Every restaurant row links to its official MICHELIN Guide profile and to the 2026 source article. Michelin status is a dated selection snapshot, not a claim about live operating status. The additional Maria Isabel row is labeled Recommended because the same Michelin article explicitly describes it as such.

Prices for two, current opening schedules and exceptions, venue-owned websites beyond the Michelin profile, official social/video accounts, hotel rates, hotel proximity counts, and a complete non-starred Guide roster are not yet verified. They are intentionally blank or called out in the page's flagged-review section. Do not treat a blank as zero or as a negative claim.

## GitHub Pages

A GitHub Actions Pages workflow is included at `.github/workflows/pages.yml`. It deploys the current Arena branch when its repository Pages source is configured to **GitHub Actions** and the repository permits Pages deployments. GitHub Pages account/repository settings are external to these static files.
