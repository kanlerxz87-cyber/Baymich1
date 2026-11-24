#!/usr/bin/env python3
"""Build the static GitHub Pages site from data/*.json.

Run:  python3 scripts/build_site.py
Outputs: index.html, pages/*.html, assets/style.css (repo root = GitHub Pages source).
Also runs a link check: every local href/src must point to an existing file.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = json.load(open(os.path.join(ROOT, "data", "michelin_bay_area_stars.json"), encoding="utf-8"))
AS_OF = DATA["as_of"]
E = html.escape


def badge(text, kind):
    return f'<span class="badge {kind}">{E(text)}</span>'


def status_badge(s):
    m = {"VERIFIED": ("Verified", "ok"), "PARTIAL": ("Partial", "warn"), "UNVERIFIED": ("Unverified", "bad")}
    t, k = m.get(s, (s, "bad"))
    return badge(t, k)


def src_links(keys):
    out = []
    for k in keys:
        s = DATA["sources"].get(k)
        if s:
            out.append(f'<a href="{E(s["url"])}" rel="noopener" target="_blank" title="{E(s["label"])}">[{E(k)}]</a>')
    return " ".join(out)


def layout(title, body, depth=0, active=""):
    prefix = "../" if depth else ""
    nav_items = [
        ("index", "Home", "index.html"),
        ("starred", "Michelin starred", "pages/michelin-starred.html"),
        ("summary", "Executive summary", "pages/executive-summary.html"),
        ("flags", "Flagged for review", "pages/flagged-for-review.html"),
        ("suggest", "Suggestions & questions", "pages/suggestions.html"),
        ("repo", "Repo review", "pages/repo-review.html"),
    ]
    nav = "".join(
        f'<a class="{"on" if key == active else ""}" href="{prefix}{href}">{E(label)}</a>'
        for key, label, href in nav_items
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · Bay Area Michelin Dashboard</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header class="top">
  <div class="brand"><a href="{prefix}index.html">Bay Area Michelin Dashboard</a></div>
  <nav class="nav">{nav}</nav>
</header>
<main class="wrap">
{body}
</main>
<footer class="foot">
  Data as of {E(AS_OF)} · Every value links to an official source or is marked <strong>Unverified</strong>. ·
  Source repo: <a href="https://github.com/kanlerxz87-cyber/Baymich1">github.com/kanlerxz87-cyber/Baymich1</a>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- starred page
def starred_page():
    rows = []
    s = DATA["starred"]
    order = {3: 0, 2: 1, 1: 2}
    s_sorted = sorted(s, key=lambda x: (order[x["stars"]], x["county"], x["name"]))
    for i, x in enumerate(s_sorted, 1):
        star_label = {3: "★★★ 3 stars", 2: "★★ 2 stars", 1: "★ 1 star"}[x["stars"]]
        new = badge("NEW 2026", "new") if x["new"] else ""
        tier = E(x["price_tier"]) if x["price_tier"] else '<span class="muted">not captured</span>'
        cuisine = E(x["cuisine"]) if x["cuisine"] else '<span class="muted">not captured</span>'
        loc = f'{E(x["city"])}<br><span class="muted">{E(x["county"])} Co.</span>'
        addr = E(x["address"]) if x["address"] else '<span class="muted">UNVERIFIED</span>'
        hours = E(x["hours"]) if x["hours"] and x["hours"] != "Not captured" else '<span class="muted">UNVERIFIED — not captured</span>'
        web = (f'<a href="{E(x["website"])}" target="_blank" rel="noopener">Official site</a>' if x["website"]
               else '<span class="muted">UNVERIFIED</span>')
        mich = f'<a href="{E(x["michelin"])}" target="_blank" rel="noopener">Michelin page</a>'
        flag = f' {badge(x["flag"], "bad")}' if x.get("flag") else ""
        rows.append(f"""
<tr>
  <td data-label="#">{i}</td>
  <td data-label="Restaurant"><strong>{E(x["name"])}</strong>{new}{flag}</td>
  <td data-label="Michelin status">{star_label}</td>
  <td data-label="City / county">{loc}</td>
  <td data-label="Cuisine">{cuisine}</td>
  <td data-label="Michelin price tier">{tier}</td>
  <td data-label="Est. cost, 2 adults (total)">{badge("UNVERIFIED", "bad")}</td>
  <td data-label="Days & hours (official)">{hours}<br>{status_badge(x["hours_status"])}</td>
  <td data-label="Address">{addr}</td>
  <td data-label="Website / phone">{web}{'<br><span class="muted">' + E(x["phone"]) + '</span>' if x["phone"] else ''}</td>
  <td data-label="Social (YT / TikTok / IG)">{badge("Not searched", "bad")}</td>
  <td data-label="Sources">{mich}<br>{src_links(x["sources"])}</td>
</tr>""")
    counts = {k: sum(1 for x in s if x["stars"] == k) for k in (3, 2, 1)}
    body = f"""
<section class="hero">
  <h1>Michelin-starred restaurants · SF Bay Area</h1>
  <p>Official 2026 Michelin star list for the 9-county Bay Area. <strong>{len(s)} starred</strong>:
     {counts[3]} three-star · {counts[2]} two-star · {counts[1]} one-star.
     Status shown is the star level from Michelin's 2026 California list (ceremony 24 Jun 2026).</p>
  <p class="legend">
    {badge("Verified", "ok")} value read from an official Michelin page ·
    {badge("Partial", "warn")} some days missing ·
    {badge("Unverified", "bad")} not confirmed from an official source — left blank on purpose.
  </p>
</section>

<section class="card">
  <h2>Table</h2>
  <p class="muted small">Scroll sideways on wide screens, or view on a phone (rows stack automatically). Prices: Michelin shows only a price tier (<code>$</code> to <code>$$$$</code>), not a dollar amount. Couple-cost values are not verified yet, so they are blank.</p>
  <div class="tablewrap">
  <table class="data">
    <thead><tr>
      <th>#</th><th>Restaurant</th><th>Michelin status</th><th>City / county</th><th>Cuisine</th>
      <th>Michelin price tier</th><th>Est. cost, 2 adults (total)</th><th>Days &amp; hours (official)</th>
      <th>Address</th><th>Website / phone</th><th>Social (YT / TikTok / IG)</th><th>Sources</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  </div>
</section>


"""
    return layout("Michelin starred", body, depth=1, active="starred")


# ----------------------------------------------------------- executive summary
def summary_page():
    body = f"""
<section class="hero">
  <h1>Executive summary</h1>
  <p class="muted">As of {E(AS_OF)} · Scope: 9-county SF Bay Area · Source of record: Michelin Guide official pages</p>
</section>

<section class="kpis">
  <div class="kpi"><div class="n">41</div><div class="l">Michelin-starred restaurants (Bay Area)</div></div>
  <div class="kpi"><div class="n">7</div><div class="l">Three-star</div></div>
  <div class="kpi"><div class="n">7</div><div class="l">Two-star</div></div>
  <div class="kpi"><div class="n">27</div><div class="l">One-star</div></div>
  <div class="kpi"><div class="n">6 / 41</div><div class="l">Full hours verified</div></div>
  <div class="kpi bad"><div class="n">0</div><div class="l">Dollar prices verified</div></div>
</section>

<section class="card">
  <h2>Key findings</h2>
  <ol class="list">
    <li><strong>San Francisco holds 25 of 41 starred restaurants (61%)</strong>, including 4 of 7 three-star places (Atelier Crenn, Benu, Californios, Quince). {src_links(["A"])}</li>
    <li><strong>Wine Country is the second cluster:</strong> Napa (4) and Sonoma (4) together hold 8 starred restaurants, including The French Laundry, Enclos and SingleThread at three stars. {src_links(["A", "B"])}</li>
    <li><strong>Peninsula, South Bay, East Bay, Marin:</strong> the 5 one-star places in San Mateo and Santa Clara counties, 2 in Oakland (Commis at two stars, Sun Moon Studio at one), and 1 in San Anselmo (Madcap). County labels are general geography, see F12. {src_links(["A"])}</li>
    <li><strong>2026 changes:</strong> Californios (SF) and Enclos (Sonoma) moved to three stars. New one-star entries include Naides and Wolfsbane (SF) and Troubadour (Healdsburg). {src_links(["A", "B"])}</li>
    <li><strong>Price (Michelin category, not a dollar amount):</strong> tiers were read for the 14 two- and three-star places (all $$$$). One-star tiers are not captured yet. The Michelin pages read so far show tiers, not dollar amounts, so couple costs are left unverified. {src_links(["C","D"])}</li>
    <li><strong>Hours:</strong> full hours were read for 7 restaurants and partial hours for 1 (Saison). The other 33 are unverified and flagged. {src_links(["D"])}</li>
  </ol>
</section>

<section class="card">
  <h2>Clusters (where starred restaurants sit)</h2>
  <div class="tablewrap"><table class="data">
    <thead><tr><th>Cluster</th><th>3★</th><th>2★</th><th>1★</th><th>Total</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td data-label="Cluster">San Francisco</td><td data-label="3★">4</td><td data-label="2★">6</td><td data-label="1★">15</td><td data-label="Total">25</td><td data-label="Notes">Neighborhood labels not captured. Entries: 4 three-star, 6 two-star, 15 one-star.</td></tr>
      <tr><td data-label="Cluster">Napa + Sonoma (Wine Country)</td><td data-label="3★">3</td><td data-label="2★">0</td><td data-label="1★">5</td><td data-label="Total">8</td><td data-label="Notes">Napa: Yountville (3★), Calistoga, Rutherford, Saint Helena (1★ each). Sonoma: Sonoma (3★ Enclos), Healdsburg (3★ SingleThread; 1★ Troubadour), Geyserville (1★ Cyrus).</td></tr>
      <tr><td data-label="Cluster">East Bay (Oakland / Alameda)</td><td data-label="3★">0</td><td data-label="2★">1</td><td data-label="1★">1</td><td data-label="Total">2</td><td data-label="Notes">Oakland: Commis (2★), Sun Moon Studio (1★).</td></tr>
      <tr><td data-label="Cluster">Peninsula + South Bay (San Mateo, Santa Clara)</td><td data-label="3★">0</td><td data-label="2★">0</td><td data-label="1★">5</td><td data-label="Total">5</td><td data-label="Notes">Atherton (Selby's), San Mateo (Wakuriya), Woodside (The Village Pub); Palo Alto (Protégé), Saratoga (Plumed Horse).</td></tr>
      <tr><td data-label="Cluster">Marin</td><td data-label="3★">0</td><td data-label="2★">0</td><td data-label="1★">1</td><td data-label="Total">1</td><td data-label="Notes">San Anselmo (Madcap).</td></tr>
    </tbody>
  </table></div>
  <p class="small muted">Counts from the official Michelin 2026 California article (city-level). Cluster grouping by county is general geography, not Michelin. {src_links(["A"])}</p>
</section>

<section class="card">
  <h2>Hotels (ranking)</h2>
  <p><strong>Not done in this pass.</strong> The ranking needs a defined search radius and the Michelin hotel data, which were not captured. No hotel data has been verified in this pass. {src_links(["A"])}</p>
</section>

<section class="card">
  <h2>What is still missing</h2>
  <ul class="list">
    <li>Bib Gourmand and Recommended (listed, no star) restaurants in the Bay Area — not captured.</li>
    <li>Dollar prices for two adults — no official value verified.</li>
    <li>YouTube / TikTok / Instagram links — none verified yet.</li>
    <li>Hotel ranking — not built.</li>
    <li>Activities — not started.</li>
  </ul>
  <p>See <a href="suggestions.html">Suggestions &amp; questions</a> for the decisions needed to finish these.</p>
</section>
"""
    return layout("Executive summary", body, depth=1, active="summary")


# --------------------------------------------------------------- flagged page
FLAGS = [
    ("F1", "Press cross-check not completed", "Official Michelin pages are the source of record. Press reports were not checked line by line against them in this pass, so no press conflict is claimed or resolved here.", ["A"], "needs review"),
    ("F2", "Michelin listing counts do not match the article", "The SF listing shows counts for 'San Francisco and surroundings' (3★ 4, 2★ 7, 1★ 18, Bib 30, Selected 86; 145 total). The article-based Bay Area count is 41 starred, a different geography. Not reconciled.", ["C", "A"], "needs review"),
    ("F3", "Hours incomplete", "See F14.", ["D"], "needs review"),
    ("F4", "No dollar prices verified", "Michelin shows price tiers only ($ to $$$$), not dollar amounts. The couple-cost column is blank for all 41 rows (UNVERIFIED).", ["C", "D"], "needs review"),
    ("F5", "Websites not opened", "Restaurant websites and phone numbers were taken from the Michelin detail pages. They were not separately opened to confirm they still work.", ["D"], "needs review"),
    ("F6", "1-star entries have little detail", "For the 27 one-star places, only city and star level are captured from the official article. Cuisine, price tier, address, hours and websites are blank (UNVERIFIED) until each Michelin detail page is read.", ["A"], "needs review"),
    ("F7", "Lost stars not included", "Press reports of 2026 star losses were seen in search snippets but not verified on Michelin pages. They are left out of the site.", [], "needs review"),
    ("F8", "No social links", "No YouTube, TikTok or Instagram links verified in this pass (task T5).", [], "needs review"),
    ("F9", "No Bib Gourmand / Recommended list", "Listed-but-no-star restaurants are not in the table yet (task T3).", ["C"], "needs review"),
    ("F10", "No hotel ranking", "Michelin hotel data and the search radius are not defined (task T4).", [], "needs review"),
    ("F11", "Brief's branch naming garbled", "The task brief shows the branch pattern with escaped characters. This session uses the assigned Arena branch rule instead.", [], "needs review"),
    ("F12", "County labels are general geography", "The article gives city only. County labels (e.g. Napa, Sonoma, San Mateo) are general geography, not Michelin data. Unverified.", [], "needs review"),
    ("F13", "Michelin detail pages read for 14 of 41", "Address, website, price tier and hours were read from detail pages for 14 restaurants (3★ and 2★). The 27 one-star pages were not opened. Phone numbers were read for Atelier Crenn only.", ["D"], "needs review"),
    ("F14", "Hours completeness", "Full hours verified for 7 of 41 (Benu, Californios, Quince, Acquerello, Kiln, Lazy Bear, Commis). Partial for Saison. 33 not captured.", ["D"], "needs review"),
]


def flags_page():
    rows = []
    for fid, title, text, srcs, st in FLAGS:
        rows.append(f"""<tr>
  <td data-label="ID">{badge(fid, "bad")}</td>
  <td data-label="Item"><strong>{E(title)}</strong></td>
  <td data-label="Detail">{E(text)}</td>
  <td data-label="Sources">{src_links(srcs) if srcs else '<span class="muted">none</span>'}</td>
  <td data-label="Status">{badge("Needs review", "warn")}</td>
</tr>""")
    body = f"""
<section class="hero">
  <h1>Flagged for review</h1>
  <p>Irregularities, unverified values and open tasks. Nothing here is hidden: each item says what is unknown and where to check.</p>
</section>
<section class="card">
  <div class="tablewrap"><table class="data">
    <thead><tr><th>ID</th><th>Item</th><th>Detail</th><th>Sources</th><th>Status</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table></div>
</section>
"""
    return layout("Flagged for review", body, depth=1, active="flags")


# --------------------------------------------------- suggestions & questions
QUESTIONS = [
    ("Q1", "Which 'Bay Area' definition should the site use?", "Answered in the site: 9 counties (Alameda, Contra Costa, Marin, Napa, San Francisco, San Mateo, Santa Clara, Solano, Sonoma). Needs your confirmation.", "Partly answered"),
    ("Q2", "What dollar figure counts as the couple cost?", "Michelin gives tiers only. Options: (a) official menu price from each restaurant site, (b) reservation-platform prices, (c) keep tiers only. None is verified yet.", "Open"),
    ("Q3", "What radius counts for hotel ranking?", "Walking (0.5 mi), short drive (5 mi) or county-wide? Also: count starred only, or starred plus Bib and Recommended?", "Open"),
    ("Q4", "Which social platforms count as a 'corresponding link'?", "Official brand account linked from the restaurant's own website, or any account found by search? The first option is easier to verify.", "Open"),
    ("Q5", "Visit window and party details", "Dates, time of day and budget per person would let the site show which places are open on your days.", "Open"),
    ("Q6", "Is Wine Country (Napa, Sonoma) in scope?", "Eight of 41 starred places are in Napa and Sonoma. They are included now as Bay Area counties. Confirm or remove.", "Partly answered"),
    ("Q7", "Should future data changes go through a PR to main?", "Pages publishes from main, so content goes live only after a merge. Please confirm this is how you want future changes handled.", "Open"),
]

SUGGESTIONS = [
    ("S1", "Add filters (county, star level, price tier, open-on-day)", "Lets a planner narrow 41 rows quickly on a phone.", "Medium effort. Needs a small script on the page (GitHub Pages can run it).", "Recommended: do first"),
    ("S2", "Add a 'last verified' date to every row", "Shows how old each value is. Important for hours and openings.", "Low effort. Needs a date field per row in the JSON.", "Recommended: do first"),
    ("S3", "Add an automated link checker (GitHub Actions)", "Catches broken Michelin and restaurant links after each change.", "Low to medium effort. Adds a workflow file. The sandbox cannot reach guide.michelin.com from bash, so checks must run on GitHub.", "Recommended"),
    ("S4", "Finish the Bib Gourmand / Recommended table (T3)", "Covers the 'listed but no star' group the brief asks for.", "Medium effort. Needs a full pass of the Michelin Bay Area listing.", "Recommended"),
    ("S5", "Build the hotel ranking (T4)", "Ranks hotels by nearby starred and listed restaurants.", "Needs Q3 answered first.", "Decide after Q3"),
    ("S6", "Add social links (T5) using rule Q4", "Covers the YouTube / TikTok / Instagram requirement.", "Medium to high effort, one search per restaurant.", "Decide after Q4"),
    ("S7", "Couple cost from official menu prices (T6)", "Gives a real estimate range instead of blanks.", "High effort. Each restaurant's menu must be checked. Leave blank where no official price exists.", "Decide after Q2"),
    ("S8", "Add a map view", "Shows clusters visually.", "Medium effort. Needs a map library, which adds a dependency.", "Optional"),
]


def suggest_page():
    q = "".join(f"""<tr>
  <td data-label="ID">{badge(a, "bad")}</td><td data-label="Question"><strong>{E(b)}</strong></td>
  <td data-label="Context">{E(c)}</td><td data-label="Status">{badge(d, "warn" if "Open" in d else "ok")}</td></tr>""" for a, b, c, d in QUESTIONS)
    s = "".join(f"""<tr>
  <td data-label="ID">{badge(a, "ok")}</td><td data-label="Suggestion"><strong>{E(b)}</strong></td>
  <td data-label="Why">{E(c)}</td><td data-label="Effort / needs">{E(d)}</td><td data-label="Advice">{E(e)}</td></tr>""" for a, b, c, d, e in SUGGESTIONS)
    body = f"""
<section class="hero">
  <h1>Suggestions &amp; questions</h1>
  <p>Nothing here changes the site. Review the suggestions, answer the questions, then choose a path. Reply in chat with the IDs you want (for example, "S1, S2, S3, Q1 yes").</p>
</section>

<section class="card">
  <h2>Questions that need answers before deciding</h2>
  <div class="tablewrap"><table class="data">
    <thead><tr><th>ID</th><th>Question</th><th>Context</th><th>Status</th></tr></thead>
    <tbody>{q}</tbody></table></div>
</section>

<section class="card">
  <h2>Suggestions (choose the path)</h2>
  <div class="tablewrap"><table class="data">
    <thead><tr><th>ID</th><th>Suggestion</th><th>Why</th><th>Effort / needs</th><th>Advice</th></tr></thead>
    <tbody>{s}</tbody></table></div>
  <p class="small muted">Recommended path: S1 + S2 + S3, then T3 (Bib / Recommended). This adds value without needing the open questions answered.</p>
</section>
"""
    return layout("Suggestions & questions", body, depth=1, active="suggest")


# --------------------------------------------------------------- repo review
REPO = [
    ("R1", "Repo state at start", "One branch (main), one commit ('Initial commit', 3fa14d7). The only file is README.md, which reads '# Baymich1'.", "https://github.com/kanlerxz87-cyber/Baymich1/blob/main/README.md"),
    ("R2", "No description or project purpose", "The README gives no description. The project goal (Michelin Bay Area) is not written in the repo. Owner should confirm.", "https://github.com/kanlerxz87-cyber/Baymich1"),
    ("R3", "No LICENSE", "GitHub API reports license: null. Who may reuse the content is not stated.", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository"),
    ("R4", "No .gitignore", "Generated files and local tooling could be committed by mistake.", "https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files"),
    ("R5", "GitHub Pages was enabled before any content", "Pages is set to build from main, root folder. Before this session the root held only README.md. This session adds index.html and the pages/ folder at the root.", "https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site"),
    ("R6", "COORDINATION.md was missing", "The brief required a shared task board. It did not exist, so it was created in this session.", "https://github.com/kanlerxz87-cyber/Baymich1/blob/main/COORDINATION.md"),
    ("R7", "Brief's branch naming", "The brief's session-branch naming was garbled. The Arena branch rule is used instead (see F11).", "https://github.com/kanlerxz87-cyber/Baymich1/branches"),
]


def repo_page():
    rows = "".join(f"""<tr>
  <td data-label="ID">{badge(a, "warn")}</td><td data-label="Finding"><strong>{E(b)}</strong></td>
  <td data-label="Detail">{E(c)}</td><td data-label="Link for manual review"><a href="{E(d)}" target="_blank" rel="noopener">Open</a></td></tr>""" for a, b, c, d in REPO)
    body = f"""
<section class="hero">
  <h1>Repo review</h1>
  <p>Checked line by line on {E(AS_OF)}. Each finding links to a source for manual review. Items are flagged, not changed.</p>
</section>
<section class="card">
  <div class="tablewrap"><table class="data">
    <thead><tr><th>ID</th><th>Finding</th><th>Detail</th><th>Link</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</section>
"""
    return layout("Repo review", body, depth=1, active="repo")


# -------------------------------------------------------------------- landing
def index_page():
    tiles = [
        ("Michelin starred", "41 Bay Area restaurants with official 2026 star levels, hours where captured, and sources.", "pages/michelin-starred.html", "Live", "ok"),
        ("Executive summary", "Key findings, clusters, what is still missing.", "pages/executive-summary.html", "Live", "ok"),
        ("Suggestions & questions", "Options to choose from, and the questions that need answers first.", "pages/suggestions.html", "Live", "ok"),
        ("Flagged for review", "Unverified values, conflicts, open tasks.", "pages/flagged-for-review.html", "Live", "ok"),
        ("Repo review", "Sourced review of the repo, with links for manual checks.", "pages/repo-review.html", "Live", "ok"),
        ("Bib Gourmand & Recommended", "Listed-but-no-star restaurants. Not captured yet.", "", "Pending", "warn"),
        ("Hotels (ranking)", "Ranked by nearby Michelin restaurants. Needs radius decision.", "", "Pending", "warn"),
        ("Activities", "Not started.", "", "Pending", "warn"),
        ("Social links", "YouTube / TikTok / Instagram. None verified yet.", "", "Pending", "warn"),
    ]
    cards = []
    for title, desc, href, st, kind in tiles:
        inner = f'<h3>{E(title)}</h3><p>{E(desc)}</p>{badge(st, kind)}'
        if href:
            cards.append(f'<a class="tile" href="{href}">{inner}</a>')
        else:
            cards.append(f'<div class="tile dim">{inner}</div>')
    body = f"""
<section class="hero">
  <h1>SF Bay Area Michelin dashboard</h1>
  <p>Michelin-starred restaurants, sources, open questions and review items. Every value links to an official source or is marked <strong>Unverified</strong>.</p>
</section>

<section class="kpis">
  <div class="kpi"><div class="n">41</div><div class="l">Starred (Bay Area, 2026)</div></div>
  <div class="kpi"><div class="n">41 / 41</div><div class="l">Rows with an official Michelin link</div></div>
  <div class="kpi bad"><div class="n">33</div><div class="l">Rows with hours not captured (of 41)</div></div>
  <div class="kpi bad"><div class="n">0</div><div class="l">Verified couple costs</div></div>
</section>

<section class="grid">
  {''.join(cards)}
</section>

<section class="card">
  <h2>Start here</h2>
  <ol class="list">
    <li><a href="pages/michelin-starred.html">Open the starred table</a> — one row per restaurant, stacks on phones.</li>
    <li><a href="pages/executive-summary.html">Read the executive summary</a> for the key numbers.</li>
    <li><a href="pages/suggestions.html">Choose a path</a> — nothing changes until you pick.</li>
  </ol>
</section>
"""
    return layout("Home", body, depth=0, active="index")


CSS = """
:root{--ink:#1d2433;--muted:#667085;--line:#e4e7ec;--bg:#f7f8fa;--card:#fff;--gold:#b48a1e;--ok:#067647;--okbg:#ecfdf3;--warn:#b54708;--warnbg:#fffaeb;--bad:#b42318;--badbg:#fef3f2;--new:#1849a9;--newbg:#eff8ff}
*{box-sizing:border-box}
body{margin:0;font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:#1849a9}
.top{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line);padding:10px 16px;display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center}
.brand a{font-weight:700;color:var(--ink);text-decoration:none}
.nav{display:flex;flex-wrap:wrap;gap:6px}
.nav a{font-size:14px;padding:6px 10px;border-radius:999px;text-decoration:none;color:var(--ink);background:#f2f4f7}
.nav a.on{background:var(--ink);color:#fff}
.wrap{max-width:1200px;margin:0 auto;padding:16px}
.hero{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;margin-bottom:14px}
.hero h1{margin:0 0 6px;font-size:clamp(22px,4vw,30px)}
.hero p{margin:6px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:14px}
.card h2{margin:0 0 8px;font-size:20px}
.list li{margin:6px 0}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px}
.kpi .n{font-size:26px;font-weight:700;color:var(--ink)}
.kpi .l{font-size:13px;color:var(--muted)}
.kpi.bad .n{color:var(--bad)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:14px}
.tile{display:block;background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px;text-decoration:none;color:var(--ink)}
.tile:hover{border-color:#98a2b3}
.tile h3{margin:0 0 4px;font-size:17px}
.tile p{margin:0 0 8px;color:var(--muted);font-size:14px}
.tile.dim{opacity:.7}
.badge{display:inline-block;font-size:12px;font-weight:600;padding:2px 8px;border-radius:999px;margin:2px 4px 2px 0;white-space:nowrap}
.badge.ok{background:var(--okbg);color:var(--ok)}
.badge.warn{background:var(--warnbg);color:var(--warn)}
.badge.bad{background:var(--badbg);color:var(--bad)}
.badge.new{background:var(--newbg);color:var(--new)}
.muted{color:var(--muted)}
.small{font-size:13px}
.legend{font-size:14px}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
table.data{width:100%;border-collapse:collapse;font-size:14px}
table.data th,table.data td{text-align:left;padding:8px;border-bottom:1px solid var(--line);vertical-align:top}
table.data th{background:#f9fafb;font-size:12px;text-transform:uppercase;letter-spacing:.02em;color:var(--muted);position:sticky;top:0}
table.data tr:hover td{background:#fcfcfd}
.foot{max-width:1200px;margin:20px auto;padding:0 16px 24px;color:var(--muted);font-size:13px}
code{background:#f2f4f7;padding:0 4px;border-radius:4px}
@media (max-width:720px){
  .wrap{padding:10px}
  table.data thead{display:none}
  table.data,table.data tbody,table.data tr,table.data td{display:block;width:100%}
  table.data tr{border:1px solid var(--line);border-radius:12px;margin-bottom:10px;padding:6px 10px;background:#fff}
  table.data td{border:0;padding:5px 0;display:flex;gap:10px;justify-content:space-between}
  table.data td::before{content:attr(data-label);font-size:11px;text-transform:uppercase;color:var(--muted);flex:0 0 40%;font-weight:600}
  table.data td[data-label="Restaurant"]{font-size:16px}
  table.data td[data-label="Restaurant"]::before{content:none}
}
"""


def check_links(files):
    bad = []
    for path in files:
        src = open(path, encoding="utf-8").read()
        base = os.path.dirname(path)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', src):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#", "tel:")):
                continue
            t = target.split("#")[0]
            if not t:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, t))):
                bad.append((os.path.relpath(path, ROOT), target))
    return bad


def main():
    os.makedirs(os.path.join(ROOT, "pages"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    outs = {
        os.path.join(ROOT, "index.html"): index_page(),
        os.path.join(ROOT, "pages", "michelin-starred.html"): starred_page(),
        os.path.join(ROOT, "pages", "executive-summary.html"): summary_page(),
        os.path.join(ROOT, "pages", "flagged-for-review.html"): flags_page(),
        os.path.join(ROOT, "pages", "suggestions.html"): suggest_page(),
        os.path.join(ROOT, "pages", "repo-review.html"): repo_page(),
    }
    for p, content in outs.items():
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
    with open(os.path.join(ROOT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(ROOT, ".nojekyll"), "w") as f:
        f.write("")
    bad = check_links(list(outs.keys()))
    if bad:
        print("BROKEN LOCAL LINKS:", bad)
        sys.exit(1)
    print(f"built {len(outs)} pages; local links OK")


if __name__ == "__main__":
    main()
