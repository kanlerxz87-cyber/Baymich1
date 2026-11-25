(() => {
  const d = window.BAY_DATA;
  const $ = (selector) => document.querySelector(selector);
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[char]));
  const safeLink = (url, label, cls = "") => `<a${cls ? ` class="${escapeHtml(cls)}"` : ""} href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)}</a>`;

  const starRows = d.restaurants.filter((r) => r.type === "star");

  function starCount(r) { return Number(r.stars || 0); }

  function starLabel(r) {
    const s = starCount(r);
    const tier = r.price ? ` <span class="badge price-tier">${escapeHtml(r.price)}</span>` : '';
    return `<span class="badge badge-star"><span aria-hidden="true">${"★".repeat(s)}</span><span>${s} ${s === 1 ? "Star" : "Stars"}</span></span>${tier}<span class="micro-label">2026 MICHELIN Guide</span>`;
  }
  function distinctionLabel(r) {
    return r.type === "star"
      ? starLabel(r)
      : `<span class="badge badge-bib">BIB</span>${r.price ? ` <span class="badge price-tier">${escapeHtml(r.price)}</span>` : ''}<span class="micro-label">Bib Gourmand &middot; guide-listed, no star</span>`;
  }
  function hoursText(r) {
    if (!r.hours) {
      return `<span class="missing">Not verified</span><small>Hours not confirmed from an official source; check the Michelin profile for your date.</small>`;
    }
    const open = Object.entries(r.hours).filter(([, time]) => time !== "Closed").map(([day, time]) => `${day} ${escapeHtml(time)}`).join(" &middot; ");
    const closed = Object.entries(r.hours).filter(([, time]) => time === "Closed").map(([day]) => day).join(", ");
    const detail = Object.entries(r.hours).map(([day, time]) => `<li><b>${escapeHtml(day)}:</b> ${escapeHtml(time)}</li>`).join("");
    const srcNote = r.verified ? ` <span class="micro-label">Schedule per MICHELIN Guide profile read ${r.verified}</span>` : '';
    return `<details class="hours-details"><summary>${escapeHtml(open)}</summary><ul>${detail}</ul><small>Closed: ${escapeHtml(closed)}. Special-date exceptions not verified; confirm for your date.${srcNote}</small></details>`;
  }
  function priceText(r) {
    if (r.couple) {
      const c = r.couple;
      return `<span class="verified">Verified &middot; ${escapeHtml(c.basis)}</span><small>Source: ${safeLink(c.source, "official restaurant site", "small-link")}. Tax, beverages and optional pairings are extra unless the source states otherwise.</small>`;
    }
    return `<span class="missing">Not verified</span><small>Official two-adult total not confirmed; Michelin price bands are not converted into a dollar total.</small>`;
  }
  function socialText(r) {
    const s = r.social || {};
    const links = [];
    if (s.instagram) links.push(`<a href="${escapeHtml(s.instagram)}" target="_blank" rel=\"noopener noreferrer\" class=\"small-link\">Instagram &#8594;</a>`);
    if (s.facebook) links.push(`<a href="${escapeHtml(s.facebook)}" target="_blank" rel=\"noopener noreferrer\" class=\"small-link\">Facebook &#8594;</a>`);
    if (links.length) {
      const src = r.socialSource ? `<br><small class=\"src-note\">Source: ${escapeHtml(r.socialSource)}</small>` : '';
      return `${links.join(' &#8226; ')}${src}`;
    }
    return `<span class="missing">Not verified</span><small>No Instagram / TikTok / YouTube link confirmed from an official restaurant source.</small>`;
  }
  function restaurantRow(r) {
    const status = r.type === "star" ? `${starCount(r)} ${starCount(r) === 1 ? "Star" : "Stars"}` : "Bib Gourmand &middot; no star";
    return `<tr>
      <td data-label="Restaurant"><div class="restaurant-name">${safeLink(r.source, escapeHtml(r.name), "restaurant-link")}</div><small>${escapeHtml(r.city)}</small>${r.address ? `<br><small class="addr">${escapeHtml(r.address)}</small>` : ''}${r.cuisine ? `<br><small class="cuisine">${escapeHtml(r.cuisine)}</small>` : ''}${r.phone ? `<br><small>${escapeHtml(r.phone)}</small>` : ''}</td>
      <td data-label="MICHELIN standing">${distinctionLabel(r)}<span class="sr-only">${escapeHtml(status)}</span></td>
      <td data-label="Area cluster">${escapeHtml(r.area)}</td>
      <td data-label="Days, hours & exceptions">${hoursText(r)}</td>
      <td data-label="Total for 2 adults">${priceText(r)}</td>
      <td data-label="Official social">${socialText(r)}</td>
      <td data-label="Restaurant site">${r.website ? safeLink(r.website, "Official site &nbsp;&rarr;", "small-link") : `<span class="missing">Not verified</span>`}</td>
      <td data-label="Source">${safeLink(r.source, "MICHELIN &nbsp;&rarr;", "source-chip")}</td>
    </tr>`;
  }
  function renderRestaurants() {
    const q = $("#restaurant-search").value.trim().toLowerCase();
    const kind = $("#distinction-filter").value;
    const area = $("#area-filter").value;
    const filtered = d.restaurants.filter((r) => {
      const matchesQuery = !q || `${r.name} ${r.city} ${r.area}`.toLowerCase().includes(q);
      const matchesKind = kind === "all" || r.type === kind;
      const matchesArea = area === "all" || r.area === area;
      return matchesQuery && matchesKind && matchesArea;
    }).sort((a, b) => (a.type === b.type ? (starCount(b) || 0) - (starCount(a) || 0) || a.name.localeCompare(b.name) : a.type === "star" ? -1 : 1));
    $("#restaurant-result-count").textContent = `${filtered.length} of ${d.restaurants.length} entries`;
    const head = `<table class="data-table"><thead><tr><th scope="col">Restaurant</th><th scope="col">MICHELIN standing</th><th scope="col">Area cluster</th><th scope="col">Days, hours & exceptions</th><th scope="col">Total for 2 adults</th><th scope="col">Official social</th><th scope="col">Restaurant site</th><th scope="col">Source</th></tr></thead><tbody>${filtered.map(restaurantRow).join("")}</tbody></table>`;
    $("#restaurant-table").innerHTML = filtered.length ? head : `<div class="empty-state">No restaurants match those filters. Try another city or distinction.</div>`;
  }

  const areas = [...new Set(d.restaurants.map((r) => r.area))].sort();
  areas.forEach((area) => $("#area-filter").insertAdjacentHTML("beforeend", `<option value="${escapeHtml(area)}">${escapeHtml(area)}</option>`));
  $("#restaurant-search").addEventListener("input", renderRestaurants);
  $("#distinction-filter").addEventListener("change", renderRestaurants);
  $("#area-filter").addEventListener("change", renderRestaurants);
  renderRestaurants();

  $("#hero-star-count").textContent = starRows.length;
  $("#hero-sf-count").textContent = starRows.filter((r) => r.city === "San Francisco").length;

  const svg = `<svg class="cluster-svg" viewBox="0 0 100 100" role="presentation" aria-hidden="true">
    <defs><linearGradient id="bayFade" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#d9e9de"/><stop offset="1" stop-color="#eff5ef"/></linearGradient></defs>
    <rect width="100" height="100" rx="8" fill="#edf4ef"/>
    <path d="M42 0 C39 12 49 17 43 28 C38 40 48 47 43 61 C40 74 49 86 44 100 L61 100 C58 87 64 79 59 66 C55 52 65 42 59 29 C54 18 64 10 61 0Z" fill="url(#bayFade)" stroke="#d1dfd5" stroke-width=".5"/>
    <path d="M8 21 C27 12 38 15 48 28 M12 58 C28 50 38 46 48 46 M18 84 C29 75 38 72 48 70 M63 18 C76 20 84 30 91 38 M62 48 C74 51 82 62 89 71" fill="none" stroke="#cad9cf" stroke-width=".6" stroke-dasharray="1.5 1.4"/>
    ${d.clusters.map((c) => `<g class="map-node" data-area="${escapeHtml(c.name)}" tabindex="0" role="button" aria-label="Filter restaurants in ${escapeHtml(c.name)}; ${c.count} starred restaurants"><circle cx="${c.x}" cy="${c.y}" r="${Math.max(3.2, Math.min(6.3, 2.8 + c.count * .1))}" fill="#254c3c" opacity=".94"/><text x="${c.x}" y="${c.y + .75}" text-anchor="middle" fill="white" font-size="2.5" font-weight="700">${c.count}</text><text x="${c.x}" y="${c.y + Math.max(3.2, Math.min(6.3, 2.8 + c.count * .1)) + 3.4}" text-anchor="middle" fill="#17382b" font-size="2.7" font-weight="700">${escapeHtml(c.name)}</text></g>`).join("")}
    <text x="7" y="95" fill="#65756c" font-size="2.4">SCHEMATIC &middot; NOT TO SCALE</text>
  </svg>`;
  $("#cluster-map").innerHTML = svg;
  const clusterCard = (c) => `<button type="button" class="cluster-card" data-area="${escapeHtml(c.name)}"><span class="cluster-count">${c.count}</span><span><b>${escapeHtml(c.name)}</b><small>${escapeHtml(c.sub)}</small></span><span class="cluster-arrow" aria-hidden="true">&rarr;</span></button>`;
  $("#cluster-cards").innerHTML = d.clusters.map(clusterCard).join("");
  function filterByArea(area) {
    $("#area-filter").value = area;
    $("#distinction-filter").value = "star";
    renderRestaurants();
    location.hash = "restaurants";
  }
  document.querySelectorAll(".cluster-card, .map-node").forEach((el) => {
    el.addEventListener("click", () => filterByArea(el.dataset.area));
    if (el.classList.contains("map-node")) el.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); filterByArea(el.dataset.area); } });
  });

  $("#hotel-cards").innerHTML = d.hotels.map((h, index) => `<article class="hotel-card">
    <div class="hotel-topline"><span class="hotel-order">CANDIDATE ${String(index + 1).padStart(2, "0")}</span><span class="key-badge">${"&#9670;".repeat(h.keys)} <span>${h.keys} MICHELIN ${h.keys === 1 ? "KEY" : "KEYS"}</span></span></div>
    <h3>${safeLink(h.source, escapeHtml(h.name), "hotel-name")}</h3>
    <p class="hotel-loc">${escapeHtml(h.neighborhood)} &middot; ${escapeHtml(h.area)}</p>
    <div class="hotel-fields"><div><small>Stars in corresponding city cluster</small><b>${h.area === "San Francisco" ? "25 city-wide" : "Not assigned"}</b></div>${h.address ? `<div><small>Address</small><b>${escapeHtml(h.address)}</b></div>` : ''}${h.rooms ? `<div><small>Rooms</small><b>${escapeHtml(h.rooms)}</b></div>` : ''}<div><small>Restaurants within chosen radius</small><b class="missing">Not verified</b></div><div><small>Date-specific room rate</small><b class="missing">Not verified</b></div></div>
    <p class="hotel-caveat">Candidate order is for display only&mdash;not a recommendation rank. Open the source for current hotel details and booking dates.</p>
    ${safeLink(h.source, "Official hotel profile &nbsp;&rarr;", "button button-outline")}
  </article>`).join("");

  const flags = {
    meal: d.restaurants.filter((r) => !r.couple).length,
    social: d.restaurants.length,
    schedule: d.restaurants.filter((r) => !r.hours).length,
    hotelNearby: d.hotels.length,
    hotelRate: d.hotels.length
  };
  $("#flag-count").textContent = `${flags.meal + flags.social + flags.schedule + flags.hotelNearby + flags.hotelRate} unresolved field checks`;

  $("#menu-toggle").addEventListener("click", () => {
    const expanded = $("#menu-toggle").getAttribute("aria-expanded") === "true";
    $("#menu-toggle").setAttribute("aria-expanded", String(!expanded));
    $("#primary-nav").classList.toggle("nav-open", !expanded);
  });
  document.querySelectorAll(".primary-nav a").forEach((link) => link.addEventListener("click", () => {
    $("#primary-nav").classList.remove("nav-open");
    $("#menu-toggle").setAttribute("aria-expanded", "false");
  }));
  const radioInputs = [...document.querySelectorAll("input[type=radio]")];
  const status = $("#choice-status");
  function restoreChoices() {
    try {
      const saved = JSON.parse(localStorage.getItem("bayMichelinSuggestions") || "{}");
      Object.entries(saved).forEach(([key, value]) => { const input = document.querySelector(`input[name="${CSS.escape(key)}"][value="${CSS.escape(value)}"]`); if (input) input.checked = true; });
      status.textContent = Object.keys(saved).length ? `${Object.keys(saved).length} planning choice${Object.keys(saved).length === 1 ? "" : "s"} saved in this browser. No ranking or site data was changed.` : "No choices saved yet. Your selections stay in this browser only.";
    } catch { status.textContent = "Local planning choices are not available in this browser."; }
  }
  function saveChoices() {
    const selected = {};
    radioInputs.filter((el) => el.checked).forEach((el) => selected[el.name] = el.value);
    localStorage.setItem("bayMichelinSuggestions", JSON.stringify(selected));
    status.textContent = `${Object.keys(selected).length} planning choice${Object.keys(selected).length === 1 ? "" : "s"} saved in this browser. No ranking or site data was changed.`;
  }
  radioInputs.forEach((el) => el.addEventListener("change", saveChoices));
  $("#clear-choices").addEventListener("click", () => { localStorage.removeItem("bayMichelinSuggestions"); radioInputs.forEach((el) => el.checked = false); restoreChoices(); });
  restoreChoices();

  const navLinks = [...document.querySelectorAll(".primary-nav a")];
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) navLinks.forEach((link) => link.classList.toggle("active", link.dataset.nav === entry.target.id));
  }), {rootMargin: "-22% 0px -68% 0%"});
  document.querySelectorAll("main section[id]").forEach((section) => observer.observe(section));
})();
