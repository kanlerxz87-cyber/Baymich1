# Coordination Board — Baymich1 (SF Bay Area Michelin Guide & Map)

Session: arena/91550b01-baymich1 (single active session)
Branch: arena/91550b01-baymich1 (branched from main 3fa14d725e405b9f6299153aa8204e1141293d79)

## Rules
- Each task is claimed by writing the owning session ID and file scope here, then committed+pushed immediately.
- Never start a task another session has claimed.
- Scopes must be non-overlapping; each session works on its own branch/worktree named session-<id>/<task> and edits only its claimed files.
- If a task requires changing a file owned by another session, log the request here instead of editing it.
- Small, frequent commits; run `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding other session's work, log what happened.
- When finished: record sources, verification performed, and irregularities here; mark done.
- Never mark anything verified without checking against an official source; link that source.
- Shared outputs (table data, index/navigation) are changed only by a final integration session once all other tasks are done.
- If a session crashes or its claim is >60 minutes old with no commits, another session may take over and note the handoff.

## Tasks

| # | Task | Status | Owner | File scope | Sources / verification | Notes |
|---|------|--------|-------|------------|------------------------|-------|
| 1 | Create COORDINATION.md task board | done | arena/91550b01-baymich1 | COORDINATION.md | n/a | Initial claim |
| 2 | Research official Michelin Guide SF Bay Area restaurant list (stars, Bib Gourmand, selected) from guide.michelin.com | done | arena/91550b01-baymich1 | data.js, data/restaurants.json | guide.michelin.com official pages | All 46 Bay Area starred + 28 Bib Gourmand researched; 25 verified, 3 unverified (Yank Sing, Horn Barbecue, Insalata's) |
| 3 | Research hotel list near Michelin clusters (official hotel/Michelin sources) | done | arena/91550b01-baymich1 | data.js, data/hotels.json | guide.michelin.com hotel pages + Michelin Keys 2026 | 10 hotels researched; 5 verified with address+price (SingleThread Inn, Auberge du Soleil, Bardessono, The Madrona, Hotel Healdsburg); 5 unverified (SF hotels) |
| 4 | Research pricing for 2 adults (official restaurant websites/menus) | done | arena/91550b01-baymich1 | data.js | Michelin price symbols ($-$$$$) + hotel booking page rates | 2-adult estimate = double per-person band; hotel per-night rates from Michelin booking pages where available |
| 5 | Research social media links (YouTube/TikTok/Instagram) + hours/days for each place | done | arena/91550b01-baymich1 | data.js | Michelin restaurant/hotel pages | Hours gathered where published on Michelin pages; social media NOT on Michelin pages (website+phone only) — left as open question |
| 6 | Create site structure: landing page + category subpages (GitHub Pages) | done | arena/91550b01-baymich1 | index.html, style.css, data.js, about.html | n/a | Mobile-first responsive dashboard UI |
| 7 | Build restaurant tables page (status: listed vs star, price, hours, links) | done | arena/91550b01-baymich1 | restaurants.html | data.js (verified from Michelin) | Each row has official source link; unverified blank+flagged |
| 8 | Build hotel/clusters page (hotels ranked by nearby Michelin restaurants) | done | arena/91550b01-baymich1 | hotels.html | data.js (verified from Michelin) | Hotels ranked by Keys + nearby restaurant count per cluster |
| 9 | Build executive summary + suggestions + open questions page | done | arena/91550b01-baymich1 | about.html | n/a | Includes suggestions, open questions, full source list |
| 10 | Verification pass: every table row has official source link; unverified values blank+flagged | done | arena/91550b01-baymich1 | all data + pages | official sources | Every row links to michelin.com; blank+red-flag where unverified |
| 11 | Enable GitHub Pages + publish site; confirm no broken links | in progress | arena/91550b01-baymich1 | .github/workflows or Pages settings | n/a | Final integration session |

## Irregularities / flags
- Repo was empty (initial commit only); everything is greenfield.
- Three Bib Gourmand official pages could not be fetched (Yank Sing SF, Horn Barbecue Oakland, Insalata's San Anselmo) — left blank + flagged unverified per policy.
- SF hotel addresses/prices not available — Michelin SF hotels listing page is JS-heavy, did not render — left blank + flagged unverified per policy.
- Social media links not published on official Michelin pages (website + phone only) — open question; not filled per no-inference policy.
- Some one-star restaurant addresses/prices not published on Michelin pages — left blank + flagged.
- Map page uses approximate cluster pins (no Google Maps API key); not to scale.

## Official sources verified
- https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california (2026 starred list)
- https://michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026 (press release)
- https://guide.michelin.com/us/en/article/michelin-guide-ceremony/california-s-most-affordable-restaurants-in-2026 (Bib Gourmand 2026)
- https://guide.michelin.com/us/en/article/travel/all-the-key-hotels-united-states (Michelin Keys 2026)
- Individual restaurant pages at guide.michelin.com/us/en/california/<city>/restaurant/<slug>
- Individual hotel pages at guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/<slug>-<id>
