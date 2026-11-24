# SF Bay Area Michelin guide — requirements and verification plan

**Status: planning only; no directory or commercial facts verified yet.** This repository started with only a minimal README. There is currently no restaurant inventory, hotel data, map, pricing evidence, activity catalog, or site implementation. Consequently this document does not assert that any named business has a Michelin distinction, an available room, a price, opening hours, or social account.

## Decision objective

Help a traveler choose a Bay Area lodging base and a practical itinerary using a transparent inventory of Michelin Guide selections, current Michelin-star holders, official restaurant prices, operating schedules, activities, and linked social-video references. Keep the two Michelin statuses distinct: **currently starred** and **Guide-listed without a current star**. Do not treat an historical star, a Guide recommendation, a Bib Gourmand, or a Green Star as a current Michelin star.

## Required record fields

### Restaurant records

| Field | Requirement |
|---|---|
| Name and official restaurant URL | Link to the restaurant's own page; use Michelin's official listing separately for Michelin status. |
| Michelin status | Exact current category and star count only where the current official Michelin listing explicitly confirms it; otherwise blank and flagged. Capture verification date. |
| Address / coordinates | Official restaurant source; coordinates only when authoritative or directly geocoded from the official address, with method recorded. |
| Price for two adults | Total, currency, inclusions, taxes/service treatment, date, and source. Prefer an explicit official menu or booking price. When only menu items are listed, calculate a range only from cited, explicit item prices and label assumptions (e.g., two diners, selected courses); do not imply a full meal price. If no defensible official total exists, leave blank. |
| Days, hours, exceptions | Exact official schedule, timezone, holiday/seasonal caveats, and date checked. Blank if absent or ambiguous. |
| Social/video | Direct YouTube, TikTok, or Instagram URL, identified as an official account or third-party coverage; do not present third-party content as official. |
| Provenance | One or more direct source URLs per row and field-level notes for values not found. |

### Hotel records and ranking

Capture official property URL, address, verified pricing for a consistent date/party/room basis, taxes/fees treatment, availability timestamp, and source. Compute restaurant proximity/density from the verified restaurant dataset and publish the radius/metric, distance method, category weights (if any), and tie handling. Hotel ranking must not be a claim that a hotel is best overall: distinguish nearby count from route convenience, price, and traveler preferences. Do not rank hotels until coverage, dates, and weighting are disclosed; blank or flag unsupported values.

### Activity records

Use the same identity, official URL, hours/exceptions, official-source link, and social/video provenance rules. Identify activities as proposed itinerary options, not Michelin-rated restaurants.

## Required pages and presentation

- Mobile-first landing page with an executive summary, scope, last-checked date, coverage caveats, and links to category pages.
- Separate restaurant, hotel/clusters, activities, methodology, and **Flagged for Review** pages.
- Accessible responsive tables (or stacked cards on narrow screens), readable labels, currency and time-zone clarity, sortable/filterable data only if it works accessibly, and no dense unlabelled map-only content.
- Map with visible markers, category/status filters, list/map synchronization, accessible list alternative, and attribution for the map/data provider. Do not plot records lacking verified locations.
- Each published row must link to an official source for the business and to the official Michelin page for Michelin status where applicable. Social links are additional, never substitutes for primary evidence.

## Questions that must be answered before a responsible recommendation

| Question | What is currently known | Missing evidence / next step |
|---|---|---|
| What exactly counts as the Bay Area? | User specified the San Francisco Bay Area. | Select a documented county boundary or radius and list included counties/cities before measuring coverage. |
| Which Michelin distinctions qualify? | User wants starred and merely Guide-listed places separated. | Define whether Bib Gourmand, Green Star, and special awards are included as separate categories; verify current distinctions against Michelin's official guide. |
| What does “current” mean? | Current status is required. | Set refresh cadence and record the date each Michelin listing was checked. |
| What does restaurant cost for two mean? | User requests total for two adults, exact price or range. | Decide meal format, drinks, taxes, service, and date assumptions. Official menus may not provide a comparable total; keep blank rather than infer. |
| Which travel dates and hotel party/room are relevant? | None supplied. | Establish date window, nights, guests, room basis, and fee/tax convention; rates/availability are date-dependent. |
| How should a hotel be ranked? | User asks for amount of Michelin restaurants around hotels. | Agree on radius, distance metric, weighting of starred vs listed, and how price/transport/accessibility influence the ranking. Until then provide counts and a transparent methodology rather than a subjective “best.” |
| Which transport and accessibility needs matter? | None supplied. | Record driving/transit/walking preference, mobility needs, parking, and acceptable travel time. |
| What activities and social sources are acceptable? | User requests corresponding YouTube/TikTok/Instagram links where possible. | Use official channels when available; clearly identify third-party videos and omit unavailable/unverifiable links. |
| What does “verified” mean for hours and exceptions? | Official sources are required. | Record source URL and check date; confirm holiday/seasonal exceptions on the business's own site or leave the exception field blank/flagged. |
| Can the requested GitHub Pages site be published now? | The repo has no site or data yet. | Build and verify the site first. Confirm repository Pages settings / deployment permissions through GitHub after implementation; do not claim a live URL before successful deployment. |

## Verification and review workflow

1. Establish a dated scope and a source register. Prefer Michelin's own current guide for Michelin classifications; each business's official site for address, menu, hours, booking terms, and official social accounts; and a hotel's official site for property and rates.
2. Verify every row and every changing value against its cited page. Record the exact source and check date. Do not use search-result snippets as the only evidence. If an official source does not resolve a value, leave it empty and add the item to Flagged for Review.
3. Treat social/video links as discovery aids. Confirm the URL resolves and label creator/official-account status. Do not invent a link when none is found.
4. Keep prices comparable and fully labelled; never fabricate totals from uncited assumptions. Record whether price includes tax, service, beverages, and booking fees where the source says so.
5. Validate coordinates, duplicate names, closed/relocated venues, ambiguous Michelin status, stale schedules, missing official sources, and conflicting source values. Retain conflicts as review flags rather than silently choosing a value.
6. Before publication, test mobile layout, keyboard access, table-to-card readability, map/list alternatives, all links, and the static-site build. Recheck all current claims and document unresolved items.

## Initial irregularities / blockers

- No source data, code, data schema, package configuration, or Pages deployment configuration was present at initial inspection.
- No official source has yet been consulted in this task; all factual restaurant/hotel/activity tables must remain unpublished or explicitly empty until verified.
- Pricing and hotel rankings cannot be responsibly made comparable without travel dates and a stated total-cost basis. The site can still show verified source prices with their exact scope and flag missing comparability.
- The user's “no manual input” instruction is followed by proceeding with conservative defaults and documenting unresolved choices, not by inventing answers. Any defaults used later must be explicitly disclosed.
