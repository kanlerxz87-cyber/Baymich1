/* Renders every page from the JSON files in docs/data/.
   Values are shown exactly as stored. Empty values show as "Not verified". */
(function () {
  "use strict";

  var PAGES = [
    { id: "home", href: "index.html", label: "Home" },
    { id: "restaurants", href: "restaurants.html", label: "Restaurants" },
    { id: "hotels", href: "hotels.html", label: "Hotels" },
    { id: "activities", href: "activities.html", label: "Activities" },
    { id: "summary", href: "summary.html", label: "Summary" },
    { id: "questions", href: "questions.html", label: "Questions" },
    { id: "suggestions", href: "suggestions.html", label: "Suggestions" },
    { id: "flagged", href: "flagged.html", label: "Flagged" },
    { id: "sources", href: "sources.html", label: "Sources" }
  ];

  function esc(s) {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function cell(label, value, cls) {
    var v = value === undefined || value === null || value === "";
    return '<td data-label="' + esc(label) + '"' + (cls ? ' class="' + cls + '"' : "") + ">" +
      (v ? '<span class="blank">Not verified</span>' : (value.indexOf && value.indexOf("<") === 0 ? value : esc(value))) +
      "</td>";
  }
  function link(url, text) {
    if (!url) return "";
    return '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(text || url) + "</a>";
  }
  function starPill(status) {
    var s = status || "";
    var cls = "pill";
    if (/3 Stars/i.test(s)) cls += " star3";
    else if (/2 Stars/i.test(s)) cls += " star2";
    else if (/Listed/i.test(s)) cls += " listed";
    return '<span class="' + cls + '">' + esc(s) + "</span>";
  }
  function nav(active) {
    var html = '<header class="top"><div class="wrap"><a class="brand" href="index.html">Bay Area Michelin Dashboard</a><nav class="menu">';
    PAGES.forEach(function (p) {
      html += '<a href="' + p.href + '"' + (p.id === active ? ' class="active"' : "") + ">" + p.label + "</a>";
    });
    return html + "</nav></div></header>";
  }
  function footer() {
    return '<footer>Every value is taken from the official source linked on its row. Blank = not verified. Press reports are context only. Last updated 2026-11-24.</footer>';
  }
  function getJSON(path) {
    return fetch(path, { cache: "no-store" }).then(function (r) {
      if (!r.ok) throw new Error(path + " → " + r.status);
      return r.json();
    });
  }

  var render = {};

  render.restaurants = function (data) {
    var rows = data.restaurants.rows;
    var html = '<h1>Michelin restaurants — SF Bay Area</h1>' +
      '<p class="lead">' + rows.length + ' verified rows. Every row links to its official Michelin page. Two-adult totals and social links are blank until verified.</p>';
    html += '<div class="note"><strong>Michelin category counts</strong> (official listing, "San Francisco and surroundings", 145 total): ' +
      "3 Stars: 4 · 2 Stars: 7 · 1 Star: 18 · Bib Gourmand: 30 · Selected: 86. Only the rows below are verified individually.</div>";
    html += '<div class="table-wrap"><table><thead><tr>' +
      "<th>Restaurant</th><th>Michelin status</th><th>Cuisine</th><th>Address</th><th>Michelin price tier</th>" +
      "<th>Two-adult total</th><th>Days &amp; hours</th><th>Exceptions / notes</th><th>Social (YT/TikTok/IG)</th><th>Links</th><th>Verification</th>" +
      "</tr></thead><tbody>";
    rows.forEach(function (r) {
      html += "<tr>" +
        '<td class="title" data-label="Restaurant"><strong>' + esc(r.name) + "</strong></td>" +
        '<td data-label="Michelin status">' + starPill(r.michelin_status) + "</td>" +
        cell("Cuisine", r.cuisine) +
        cell("Address", r.address) +
        cell("Michelin price tier", r.michelin_price_tier) +
        cell("Two-adult total", r.two_adult_total) +
        cell("Days & hours", r.hours) +
        cell("Exceptions / notes", r.hours_exceptions) +
        cell("Social links", r.social_links) +
        '<td data-label="Links">' + link(r.michelin_url, "Michelin page") + (r.website ? "<br>" + link(r.website, "Website") : "") + (r.phone ? "<br>" + esc(r.phone) : "") + "</td>" +
        '<td data-label="Verification">' + esc(r.verification) + "</td>" +
        "</tr>";
    });
    html += "</tbody></table></div>";
    html += '<h2>Press-reported, not yet verified</h2><p class="small">These names appear in press reports only. They are NOT in the table above.</p><ul class="clean">';
    (data.restaurants.press_reported_not_verified || []).forEach(function (p) {
      html += "<li><strong>" + esc(p.name) + "</strong> — " + esc(p.note) + " " + link(p.press_source, "press source") + "</li>";
    });
    html += "</ul>";
    html += '<div class="note"><strong>Pricing:</strong> ' + esc(data.restaurants.meta.pricing_note) + "</div>";
    html += '<div class="note"><strong>Social links:</strong> ' + esc(data.restaurants.meta.social_note) + "</div>";
    return html;
  };

  render.home = function (data, rdata) {
    var rows = rdata.rows;
    var starred = rows.filter(function (r) { return /Stars/.test(r.michelin_status); }).length;
    var hoursFull = rows.filter(function (r) { return r.hours; }).length;
    var html = '<h1>Bay Area Michelin Dashboard</h1>' +
      '<p class="lead">Organized, source-linked view of Michelin restaurants in the San Francisco Bay Area. Verified values only.</p>' +
      '<div class="grid">' +
      '<div class="card"><div class="num">' + rows.length + '</div><div class="label">Verified restaurants</div></div>' +
      '<div class="card"><div class="num">' + starred + '</div><div class="label">With Michelin stars</div></div>' +
      '<div class="card"><div class="num">' + hoursFull + '</div><div class="label">Hours fully captured</div></div>' +
      '<div class="card"><div class="num">145</div><div class="label">Michelin listing (SF &amp; surroundings)</div></div>' +
      "</div>";
    html += "<h2>Pages</h2><div class=\"grid\">";
    [
      ["restaurants.html", "Restaurants", "Verified Michelin table with links and hours"],
      ["hotels.html", "Hotels", "Ranking method — not yet ranked"],
      ["activities.html", "Activities", "Not started"],
      ["summary.html", "Executive summary", "Key findings and clusters"],
      ["questions.html", "Questions", "What is answered and what is open"],
      ["suggestions.html", "Suggestions", "Options to choose before changes"],
      ["flagged.html", "Flagged for review", "Irregularities and unverified items"],
      ["sources.html", "Sources", "Official and press links"]
    ].forEach(function (c) {
      html += '<div class="card"><a class="cardlink" href="' + c[0] + '"><strong>' + c[1] + "</strong><div class=\"small\">" + c[2] + "</div></a></div>";
    });
    html += "</div>";
    html += '<h2>Status</h2><div class="note warn">Hotels, activities, two-adult prices and social links are <strong>not verified</strong>. They are left blank rather than estimated.</div>';
    return html;
  };

  render.summary = function (data) {
    var es = data.executive_summary;
    var html = "<h1>Executive summary</h1><p class=\"lead\">" + esc(es.headline) + "</p><ul class=\"clean\">";
    es.bullets.forEach(function (b) { html += "<li>" + esc(b) + "</li>"; });
    html += "</ul>";
    html += "<h2>Michelin tiers (official)</h2><div class=\"table-wrap\"><table><thead><tr><th>Tier</th><th>Meaning (official)</th><th>Count (SF &amp; surroundings)</th></tr></thead><tbody>" +
      "<tr><td>3 Stars</td><td>Exceptional cuisine</td><td>4</td></tr>" +
      "<tr><td>2 Stars</td><td>Excellent cooking</td><td>7</td></tr>" +
      "<tr><td>1 Star</td><td>High quality cooking</td><td>18</td></tr>" +
      "<tr><td>Bib Gourmand</td><td>Good quality, good value cooking</td><td>30</td></tr>" +
      "<tr><td>Selected</td><td>Good cooking</td><td>86</td></tr></tbody></table></div>" +
      '<p class="small">Source: ' + link("https://guide.michelin.com/us/en/california/san-francisco/restaurants", "Michelin SF listing") + "</p>";
    return html;
  };

  render.questions = function (data) {
    var q = data.questions;
    var html = "<h1>Questions</h1><p class=\"lead\">What is already answered, and what must be decided or found before a decision can be made.</p>";
    html += "<h2>Answered</h2>";
    q.answered.forEach(function (x) {
      html += '<div class="qa"><div class="q">' + esc(x.q) + '</div><div>' + esc(x.a) + '</div><div class="meta">Source: ' + link(x.source, "official page") + "</div></div>";
    });
    html += "<h2>Open</h2>";
    q.open.forEach(function (x) {
      html += '<div class="qa"><div class="q">' + esc(x.q) + '</div><div class="meta"><strong>Why it matters:</strong> ' + esc(x.why) + "</div><div class=\"meta\"><strong>How to find out:</strong> " + esc(x.how_to_find) + "</div></div>";
    });
    return html;
  };

  render.suggestions = function (data) {
    var html = "<h1>Suggestions</h1><p class=\"lead\">Options to review and choose before anything is changed. None has been implemented.</p>";
    data.suggestions.forEach(function (s) {
      html += '<div class="sugg"><div><strong>' + esc(s.id) + " · " + esc(s.title) + '</strong> <span class="pill pending">' + esc(s.status) + '</span></div><div class="small" style="margin-top:6px">' + esc(s.detail) + "</div></div>";
    });
    return html;
  };

  render.flagged = function (data) {
    var html = "<h1>Flagged for review</h1><p class=\"lead\">Irregularities and items that could not be verified. Nothing here is in the verified tables.</p>";
    html += '<div class="table-wrap"><table><thead><tr><th>Item</th><th>Issue</th><th>Action</th><th>Source</th></tr></thead><tbody>';
    data.flagged.forEach(function (f) {
      html += "<tr>" + '<td data-label="Item"><strong>' + esc(f.item) + "</strong></td>" +
        '<td data-label="Issue">' + esc(f.issue) + "</td>" +
        '<td data-label="Action">' + esc(f.action) + "</td>" +
        '<td data-label="Source">' + link(f.source, "link") + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  };

  render.sources = function (data) {
    var html = "<h1>Sources</h1><p class=\"lead\">Official Michelin pages are the verification base. Press links are context only.</p>";
    html += '<div class="table-wrap"><table><thead><tr><th>Source</th><th>Used for</th><th>Link</th></tr></thead><tbody>';
    data.sources.forEach(function (s) {
      html += "<tr>" + '<td data-label="Source">' + esc(s.label) + "</td>" +
        '<td data-label="Used for">' + esc(s.supports) + "</td>" +
        '<td data-label="Link">' + link(s.url, s.url) + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  };

  render.hotels = function (data) {
    var h = data.hotels;
    return "<h1>Hotels</h1><p class=\"lead\">Status: <strong>" + esc(h.status) + "</strong></p>" +
      '<div class="note">' + esc(h.method) + "</div>" +
      '<div class="note warn">No hotel rows are verified yet, so no ranking is shown. The ranking rule itself needs your decision (see Questions and Suggestion S5).</div>' +
      '<div class="table-wrap"><table><thead><tr><th>Rank</th><th>Hotel</th><th>Michelin restaurants nearby</th><th>Source</th></tr></thead><tbody><tr><td colspan="4" class="blank">No verified rows yet</td></tr></tbody></table></div>';
  };

  render.activities = function (data) {
    var a = data.activities;
    return "<h1>Activities</h1><p class=\"lead\">Status: <strong>" + esc(a.status) + "</strong></p>" +
      '<div class="note">' + esc(a.method) + "</div>" +
      '<div class="table-wrap"><table><thead><tr><th>Activity</th><th>Days &amp; hours</th><th>Exceptions</th><th>Social (YT/TikTok/IG)</th><th>Link</th></tr></thead><tbody><tr><td colspan="5" class="blank">No verified rows yet</td></tr></tbody></table></div>';
  };

  var page = document.body.getAttribute("data-page");
  var app = document.getElementById("app");
  var header = document.getElementById("site-header");
  if (header) header.innerHTML = nav(page);
  var footEl = document.getElementById("site-footer");
  if (footEl) footEl.innerHTML = footer();

  Promise.all([getJSON("data/restaurants.json"), getJSON("data/content.json")])
    .then(function (res) {
      var rdata = res[0], cdata = res[1];
      var merged = { restaurants: rdata, hotels: cdata.hotels, activities: cdata.activities,
        executive_summary: cdata.executive_summary, questions: cdata.questions,
        suggestions: cdata.suggestions, flagged: cdata.flagged, sources: cdata.sources };
      var fn = render[page];
      app.innerHTML = fn ? fn(merged, rdata) : "<p>Page not found.</p>";
    })
    .catch(function (e) {
      app.innerHTML = '<div class="note bad">Could not load data: ' + esc(e.message) + "</div>";
    });
})();
