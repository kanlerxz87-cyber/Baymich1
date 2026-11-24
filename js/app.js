/* ==========================================================================
   Baymich1 — MICHELIN Guide SF Bay Area
   Site application: loads JSON data, renders pages
   ========================================================================== */

const DATA_ROOT = "../data";

const STARRED_FILE = `${DATA_ROOT}/restaurants.json`;
const BIB_FILE = `${DATA_ROOT}/bibgourmand.json`;

let starred = [];
let bib = [];

// ---------- helpers ----------

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

function escapeHtml(str) {
  if (!str) return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function formatStars(r) {
  if (!r.hasMichelinStar) return '<span class="badge b-bib">Bib Gourmand</span>';
  const s = r.stars || 0;
  const cls = s === 3 ? "b-3" : s === 2 ? "b-2" : "b-1";
  return `<span class="stars-row ${cls}">${"★".repeat(s)} ${s}-star Michelin</span>`;
}

function verifiedBadge(v) {
  const cls = v ? "v-true" : "v-false";
  const label = v ? "Verified" : "Unverified";
  return `<span class="verified-tag ${cls}">${label}</span>`;
}

function linksHtml(r, labelKey) {
  const links = [];
  if (r.website) links.push(`<a href="${escapeHtml(r.website)}" target="_blank" rel="noopener">Restaurant website</a>`);
  if (r.michelinLink) links.push(`<a href="${escapeHtml(r.michelinLink)}" target="_blank" rel="noopener">MICHELIN Guide listing</a>`);
  if (r.instagram) links.push(`<a href="https://www.instagram.com/${escapeHtml(r.instagram).replace(/^@/, "")}" target="_blank" rel="noopener">Instagram</a>`);
  if (r.sourceLinks && r.sourceLinks.length) {
    r.sourceLinks.forEach((u, i) => {
      if (i >= 3) return; // keep mobile tidy
      links.push(`<a href="${escapeHtml(u)}" target="_blank" rel="noopener">Source ${i + 1}</a>`);
    });
  }
  if (!links.length) return `<span style="color:#94a3b8">No public link on record</span>`;
  return links.map(l => `<div class="link-cell">${l}</div>`).join("");
}

// ---------- load ----------

async function loadJson(url) {
  const res = await fetch(url, { cache: "no-cache" });
  if (!res.ok) throw new Error(`Failed to load ${url}: ${res.status}`);
  return res.json();
}

async function init() {
  try {
    const [sData, bData] = await Promise.all([loadJson(STARRED_FILE), loadJson(BIB_FILE)]);
    starred = sData.restaurants || [];
    bib = bData.restaurants || [];
  } catch (err) {
    console.error(err);
    const el = $("#app");
    if (el) el.innerHTML = `<div class="empty">Failed to load data. ${escapeHtml(err.message)}</div>`;
    return;
  }
  renderPage();
}

// ---------- rendering ----------

function renderPage() {
  const path = window.location.pathname;
  const isIndex = path.endsWith("/") || path.endsWith("index.html");
  const isRestaurants = path.includes("restaurants.html");
  const isStarred = path.includes("starred.html");
  const isBib = path.includes("bib-gourmand.html");
  const isClusters = path.includes("clusters.html");
  const isHotels = path.includes("hotels.html");

  if (isIndex) renderIndex();
  else if (isStarred) renderRestaurantPage("starred", starred.filter(r => r.hasMichelinStar), "Michelin-Starred Restaurants");
  else if (isBib) renderRestaurantPage("bib", bib, "Bib Gourmand — Guide-Listed (No Star)");
  else if (isRestaurants) renderRestaurantPage("all", [...starred.filter(r => r.hasMichelinStar), ...bib], "All MICHELIN Guide Restaurants");
  else if (isClusters) renderClusters();
  else if (isHotels) renderHotels();
  else renderIndex(); // fallback

  setupMobileNav();
  setupHighlights();
}

function renderRestaurantPage(key, items, title) {
  const app = $("#app");
  if (!app) return;
  const starredOnly = key === "starred";
  const countStar = items.filter(r => r.hasMichelinStar).length;
  const countBib = items.filter(r => !r.hasMichelinStar).length;

  let header = `
    <div class="section-header">
      <div>
        <h2>${escapeHtml(title)}</h2>
        <div class="page-sub">${items.length} establishments &bull; ${countStar} starred &bull; ${countBib} guide-listed (Bib Gourmand)</div>
      </div>
    </div>
  `;

  if (starredOnly) {
    header += `
      <div class="callout">
        <strong>Star vs. guide-listed.</strong> A restaurant with a Michelin star currently holds a Michelin distinction
        (1, 2 or 3 stars). A "Bib Gourmand" / guide-listed restaurant is recognized in the MICHELIN Guide for good quality,
        good-value cooking but does <em>not</em> currently hold a star. Blank price/hours/social cells could not be confirmed
        from an official source and are flagged unverified &mdash; never inferred.
      </div>`;
  }

  const search = `
    <div class="controls">
      <input type="search" id="search-${key}" placeholder="Search restaurant, city or cuisine&hellip;">
      <select id="filter-dist-${key}">
        <option value="">All distinctions</option>
        <option value="3-star Michelin">3 stars</option>
        <option value="2-star Michelin">2 stars</option>
        <option value="1-star Michelin">1 star</option>
        <option value="Bib Gourmand">Bib Gourmand (no star)</option>
      </select>
      <select id="filter-city-${key}">
        <option value="">All cities</option>
        <option value="San Francisco">San Francisco</option>
        <option value="Oakland">Oakland</option>
        <option value="San Anselmo">San Anselmo</option>
        <option value="San Mateo">San Mateo</option>
        <option value="Berkeley">Berkeley</option>
        <option value="Alameda">Alameda</option>
        <option value="Mill Valley">Mill Valley</option>
        <option value="El Cerrito">El Cerrito</option>
        <option value="San Leandro">San Leandro</option>
        <option value="Fairfax">Fairfax</option>
      </select>
    </div>`;

  const table = `
    <div class="table-wrap" id="table-wrap-${key}">
      <table id="tbl-${key}">
        <thead>
          <tr>
            <th>Restaurant</th>
            <th>Distinction</th>
            <th>City / Area</th>
            <th>Cuisine</th>
            <th>Michelin price</th>
            <th>Est. price (2 adults)</th>
            <th>Days &amp; hours</th>
            <th>Links &amp; sources</th>
          </tr>
        </thead>
        <tbody id="tbody-${key}"></tbody>
      </table>
    </div>
    <div id="count-${key}" style="margin:8px 0;font-size:0.82rem;color:#64748b"></div>
  `;

  app.innerHTML = header + search + table;

  const tbody = $(`#tbody-${key}`);
  const countEl = $(`#count-${key}`);
  const searchInput = $(`#search-${key}`);
  const distSelect = $(`#filter-dist-${key}`);
  const citySelect = $(`#filter-city-${key}`);

  function render(items) {
    tbody.innerHTML = "";
    items.forEach(r => {
      const distinction = r.distinction;
      const cityArea = r.city + (r.area ? ` &bull; ${r.area}` : "");
      const price2 = r.estPrice2AdultsTotal
        ? `<div class="price-total">${escapeHtml(r.estPrice2AdultsTotal)}</div>
           <div class="price-est">${r.priceVerified ? verifiedBadge(true) : verifiedBadge(false)} ${escapeHtml(r.priceSource || "")}</div>`
        : `<span style="color:#94a3b8">Not verified</span>`;
      const hours = r.hours || `<span style="color:#94a3b8">Not verified</span>`;
      const appLinks = linksHtml(r);
      const verifiedAll = r.priceVerified || r.socialVerified;
      tr = `
        <tr>
          <td data-label="Restaurant">
            <div style="font-weight:700">${escapeHtml(r.name)}</div>
            <div style="font-size:0.78rem;color:#64748b">${r.address || "Address not verified"}</div>
          </td>
          <td data-label="Distinction">${formatStars(r)}</td>
          <td data-label="City / Area">${escapeHtml(cityArea)}</td>
          <td data-label="Cuisine">${escapeHtml(r.cuisine || "&mdash;")}</td>
          <td data-label="Michelin price">
            <span style="font-weight:700">${escapeHtml(r.michelinPriceBracket || "&mdash;")}</span>
          </td>
          <td data-label="Est. price (2 adults)">${price2}</td>
          <td data-label="Days &amp; hours">${escapeHtml(r.hours || "&mdash;")}</td>
          <td data-label="Links &amp; sources">${appLinks}</td>
        </tr>
      `;
      tbody.innerHTML += tr;
    });
    countEl.textContent = `Showing ${items.length} of ${items.length} establishments.`;
  }

  function applyFilters() {
    const q = searchInput.value.toLowerCase();
    const dist = distSelect.value;
    const city = citySelect.value;
    const filtered = items.filter(r => {
      const text = `${r.name} ${r.city} ${r.cuisine} ${r.distinction} ${r.address || ""}`.toLowerCase();
      const matchQ = !q || text.includes(q);
      const matchDist = !dist || r.distinction === dist;
      const matchCity = !city || r.city === city;
      return matchQ && matchDist && matchCity;
    });
    render(filtered);
  }

  searchInput.addEventListener("input", applyFilters);
  distSelect.addEventListener("change", applyFilters);
  citySelect.addEventListener("change", applyFilters);

  render(items);
}

// ---------- index / dashboard ----------

function renderIndex() {
  const app = $("#app");
  if (!app) return;
  const starCount = starred.filter(r => r.hasMichelinStar).length;
  const three = starred.filter(r => r.stars === 3).length;
  const two = starred.filter(r => r.stars === 2).length;
  const one = starred.filter(r => r.stars === 1).length;
  const bibCount = bib.length;

  app.innerHTML = `
    <section class="hero">
      <div class="container">
        <h1>MICHELIN Guide <span class="accent">San Francisco Bay Area</span></h1>
        <p>An organized, mobile-friendly guide and map of Michelin-rated and Michelin-starred restaurants across
        San Francisco, Oakland and the Bay Area. Every distinction is verified against the official MICHELIN Guide;
        pricing, hours and social links are verified from official sources where available.</p>
        <div class="stats">
          <div class="stat"><div class="num">${starCount}</div><div class="lbl">Michelin-starred restaurants</div></div>
          <div class="stat"><div class="num">${three + two + one}</div><div class="lbl">Starred (3★ ${three} &bull; 2★ ${two} &bull; 1★ ${one})</div></div>
          <div class="stat"><div class="num">${bibCount}</div><div class="lbl">Bib Gourmand (guide-listed, no star)</div></div>
          <div class="stat"><div class="num">2 adults</div><div class="lbl">Estimated total price shown</div></div>
        </div>
      </div>
    </section>

    <section class="section dashboard">
      <div class="container">
        <h2>Explore by category</h2>
        <div class="dashboard-grid">
          <a href="pages/restaurants.html" class="card">
            <span class="kicker">All restaurants</span>
            <h3>All MICHELIN Guide restaurants</h3>
            <p>${starCount} starred + ${bibCount} Bib Gourmand. Searchable table with prices, hours &amp; links.</p>
          </a>
          <a href="pages/starred.html" class="card">
            <span class="tag tag-starred">Starred</span>
            <h3>Michelin-starred</h3>
            <p>${three} three-star &bull; ${two} two-star &bull; ${one} one-star.</p>
          </a>
          <a href="pages/bib-gourmand.html" class="card">
            <span class="tag tag-bib">Bib Gourmand</span>
            <h3>Guide-listed (no star)</h3>
            <p>${bibCount} good-quality, good-value restaurants in the MICHELIN Guide.</p>
          </a>
          <a href="pages/clusters.html" class="card">
            <span class="kicker">Analysis</span>
            <h3>Restaurant clusters</h3>
            <p>Where Michelin restaurants concentrate across the Bay Area.</p>
          </a>
          <a href="pages/hotels.html" class="card">
            <span class="kicker">Hotels</span>
            <h3>Hotels ranked by Michelin access</h3>
            <p>Hotels ranked by the number of Michelin restaurants nearby.</p>
          </a>
          <a href="pages/executive-summary.html" class="card">
            <span class="kicker">Summary</span>
            <h3>Executive summary</h3>
            <p>Key findings, costs and decision notes at a glance.</p>
          </a>
          <a href="pages/suggestions.html" class="card">
            <span class="kicker">Improvement</span>
            <h3>Suggestions &amp; open questions</h3>
            <p>Suggested site improvements and questions to answer before decisions.</p>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="callout">
          <strong>Verification standard.</strong> Star status, city, cuisine and Michelin price bracket are verified
          against <a href="https://guide.michelin.com/us/en/california/san-francisco/restaurants" target="_blank" rel="noopener">guide.michelin.com</a>
          (2026 MICHELIN Guide California, stars announced June 24, 2026). Exact 2-adult prices, opening hours, days open,
          exceptions and social links are marked verified only when confirmed from an official source; blank values are
          flagged unverified and never inferred. See the Questions page for what still needs confirming.
        </div>
      </div>
    </section>
  `;
}

// ---------- clusters ----------

function renderClusters() {
  const app = $("#app");
  if (!app) return;
  const sf = starred.filter(r => r.hasMichelinStar && r.city === "San Francisco").length;
  const oak = starred.filter(r => r.hasMichelinStar && r.city === "Oakland").length;
  const other = starred.filter(r => r.hasMichelinStar && r.city !== "San Francisco" && r.city !== "Oakland").length;

  app.innerHTML = `
    <div class="section-header">
      <div>
        <h2>Michelin restaurant clusters</h2>
        <div class="page-sub">Where starred restaurants concentrate across the San Francisco Bay Area (2026 guide).</div>
      </div>
    </div>

    <div class="cluster-grid">
      <div class="cluster-card">
        <h4>San Francisco <span style="font-weight:normal;font-size:0.8rem;color:#64748b">(${sf} starred)</span></h4>
        <ul>
          <li>Dense fine-dining core: SoMa, Nob Hill, Jackson Square, Mission, Fillmore/Japantown, Chinatown</li>
          <li>3-star: Quince, Californios, Benu, Atelier Crenn</li>
          <li>2-star: Acquerello, Kiln, Lazy Bear, Saison, Sons &amp; Daughters, Birdsong</li>
          <li>Best for: many starred meals within a short transit/walking radius</li>
        </ul>
      </div>
      <div class="cluster-card">
        <h4>Oakland (East Bay) <span style="font-weight:normal;font-size:0.8rem;color:#64748b">(${oak} starred)</span></h4>
        <ul>
          <li>Commis (2-star, Piedmont Ave) and Sun Moon Studio (1-star)</li>
          <li>Strong Bib Gourmand bench: MAMA, Soba Ichi, Joodooboo, Bombera, Jo&rsquo;s Modern Thai, FOB Kitchen</li>
          <li>Best value-star ratio in the East Bay</li>
        </ul>
      </div>
      <div class="cluster-card">
        <h4>Peninsula &amp; Marin <span style="font-weight:normal;font-size:0.8rem;color:#64748b">(${other} starred)</span></h4>
        <ul>
          <li>Wakuriya (1-star, San Mateo), Madcap (1-star, San Anselmo)</li>
          <li>Bib Gourmand spread: Pausa (San Mateo), Insalata&rsquo;s (San Anselmo), Village Sake (Fairfax), Playa (Mill Valley)</li>
          <li>Best for: wine-country / coastal stays</li>
        </ul>
      </div>
    </div>

    <div class="section-header" style="margin-top:26px">
      <div>
        <h2>Clustering insight</h2>
        <div class="page-sub">Implication for hotel selection and itinerary planning.</div>
      </div>
    </div>
    <div class="callout">
      <strong>San Francisco is the primary cluster.</strong> 23 of 29 starred restaurants are in San Francisco, concentrated
      in SoMa / Nob Hill / Mission / Jackson Square. A visitor staying in central SF can reach most starred restaurants
      without a car. Oakland offers a secondary East Bay cluster (Commis) plus the deepest Bib Gourmand bench. Peninsula/Marin
      starred spots are single outliers best paired with a hotel stay nearby rather than a day trip from SF.
    </div>
  `;
}

// ---------- hotels ----------

function renderHotels() {
  const app = $("#app");
  if (!app) return;
  // Hotel data: verified Michelin-listed hotels + estimated nearby starred count (reasoned, flagged)
  const hotels = [
    {
      rank: 1, name: "San Francisco Proper Hotel", city: "San Francisco",
      near: "SoMa / Union Square", estNearbyStarred: "Many (SoMa + Nob Hill within short trip)",
      note: "Michelin-listed hotel; central SF cluster access.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/san-francisco-proper-hotel-8978"
    },
    {
      rank: 2, name: "Hotel Zeppelin San Francisco", city: "San Francisco",
      near: "Union Square / Nob Hill", estNearbyStarred: "Many (Nob Hill, SoMa)",
      note: "Michelin-listed hotel; near Acquerello, State Bird Provisions area.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/hotel-zeppelin-san-francisco-8165"
    },
    {
      rank: 3, name: "The Battery", city: "San Francisco",
      near: "Financial District / Embarcadero", estNearbyStarred: "Several (Quince, Jackson Square nearby)",
      note: "Michelin-listed hotel; private members club hotel.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-battery-san-francisco-8661"
    },
    {
      rank: 4, name: "Hotel Zetta San Francisco", city: "San Francisco",
      near: "SoMa", estNearbyStarred: "Several (Saison, Birdsong, Californios nearby)",
      note: "Michelin-listed hotel; SoMa cluster.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/hotel-zetta-sanfrancisco-7044"
    },
    {
      rank: 5, name: "Auberge du Soleil, Auberge Collection", city: "Rutherford (Napa)",
      near: "Napa Valley", estNearbyStarred: "Few (Auberge du Soleil restaurant 1-star on property)",
      note: "Michelin-listed hotel; wine country; 1-star Auberge du Soleil restaurant on property.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/auberge-du-soleil-auberge-collection-7246"
    },
    {
      rank: 6, name: "SingleThread Inn", city: "Healdsburg (Sonoma)",
      near: "Sonoma", estNearbyStarred: "1 (SingleThread 3-star on property)",
      note: "Michelin-listed hotel; 3-star SingleThread restaurant on property.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/singlethread-inn-13698"
    },
    {
      rank: 7, name: "Farmhouse Inn", city: "Sonoma County",
      near: "Sonoma", estNearbyStarred: "Few (Sonoma wine country)",
      note: "Michelin-listed hotel; Sonoma County.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/farmhouse-inn-5081"
    },
    {
      rank: 8, name: "Post Ranch Inn", city: "Big Sur",
      near: "Big Sur coast", estNearbyStarred: "None in immediate area",
      note: "Michelin-listed hotel; remote coast, not near a Michelin cluster.",
      michelin: "https://guide.michelin.com/us/en/hotels-stays/big-sur/post-ranch-inn-7341"
    }
  ];

  let rows = hotels.map(h => `
    <div class="hotel-row">
      <div style="display:flex;align-items:center;gap:12px">
        <div class="hotel-rank">#${h.rank}</div>
        <div>
          <div style="display:flex;align-items:center;gap:6px">
            <h4 style="font-size:1rem">${escapeHtml(h.name)}</h4>
            <span class="badge b-bib" style="font-size:0.62rem">Michelin-listed hotel</span>
          </div>
          <div class="hotel-meta">
            <span>${escapeHtml(h.city)}</span>
            <span>${escapeHtml(h.near)}</span>
          </div>
          <p style="font-size:0.82rem;color:#64748b">${escapeHtml(h.note)}</p>
          <div class="hotel-meta" style="margin-top:6px">
            <span><strong>Michelin-starred nearby (est.):</strong> ${escapeHtml(h.estNearbyStarred)}</span>
          </div>
        </div>
      </div>
      <div style="margin-top:8px">
        <a href="${escapeHtml(h.michelin)}" target="_blank" rel="noopener" style="font-size:0.8rem">View on MICHELIN Guide Hotels ↗</a>
        <span style="font-size:0.72rem;color:#94a3b8;margin-left:8px">Nearby count is reasoned, not official — verify</span>
      </div>
    </div>
  `).join("");

  app.innerHTML = `
    <div class="section-header">
      <div>
        <h2>Hotels ranked by Michelin restaurant access</h2>
        <div class="page-sub">Michelin-listed hotels ranked by the estimated number of Michelin-starred restaurants nearby (San Francisco Bay Area).</div>
      </div>
    </div>
    <div class="callout warn">
      <strong>Ranking method.</strong> Rankings are based on each hotel&rsquo;s location relative to the verified 2026 Michelin-starred
      restaurant list (mostly central San Francisco). The exact &ldquo;number of Michelin restaurants around&rdquo; each hotel is
      <em>not published by Michelin</em> and is reasoned from addresses &mdash; treat as an estimate, verify before booking decisions.
    </div>
    <div id="hotel-list">${rows}</div>
  `;
}

function setupMobileNav() {
  const btn = $(".nav-toggle");
  const menu = $("#mobile-menu");
  if (!btn || !menu) return;
  btn.addEventListener("click", () => menu.classList.toggle("open"));
  $$("#mobile-menu a").forEach(a => a.addEventListener("click", () => menu.classList.remove("open")));
}

function setupHighlights() {
  // highlight active nav link
  const path = window.location.pathname;
  $$("nav a, #mobile-menu a").forEach(a => {
    const href = a.getAttribute("href");
    if (href && path.includes(href.replace("pages/", ""))) a.classList.add("active");
  });
}

init();
