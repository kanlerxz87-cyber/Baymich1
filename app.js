(() => {
  const d = window.BAY_DATA;
  const $ = (selector) => document.querySelector(selector);
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char]));
  const safeLink = (url, label, cls = "") => `<a${cls ? ` class="${cls}"` : ""} href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${label}</a>`;
  const starRows = d.restaurants.filter((r) => r.type === "star");
  const bibRows = d.restaurants.filter((r) => r.type === "bib");

  function starLabel(r) {
    return `<span class="badge badge-star"><span aria-hidden="true">${"★".repeat(r.stars)}</span><span>${r.stars} ${r.stars === 1 ? "Star" : "Stars"}</span></span><span class="micro-label">2026 MICHELIN Guide</span>`;
  }
  function distinctionLabel(r) {
    return r.type === "star" ? starLabel(r) : `<span class="badge badge-bib">BIB</span><span class="micro-label">Bib Gourmand · not a star</span>`;
  }
  function hoursText(r) {
    if (!r.hours) return `<span class="missing">Not verified locally</span><small>Open official profile for current schedule.</small>`;
    const days = Object.entries(r.hours).filter(([, time]) => time !== "Closed").map(([day, time]) => `${day} ${time}`).join(" · ");
    const closed = Object.entries(r.hours).filter(([, time]) => time === "Closed").map(([day]) => day).join(", ");
    const detail = Object.entries(r.hours).map(([day, time]) => `<li><b>${day}:</b> ${escapeHtml(time)}</li>`).join("");
    return `<details class="hours-details"><summary>${escapeHtml(days)}</summary><ul>${detail}</ul><small>Closed: ${escapeHtml(closed)}. ${escapeHtml(r.exception || "Holiday/special-date exceptions not verified; check the source for your date.")}</small></details>`;
  }
  function restaurantRow(r) {
    const status = r.type === "star" ? `${r.stars} ${r.stars === 1 ? "Star" : "Stars"}` : "Bib Gourmand · no star";
    return `<tr>
      <td data-label="Restaurant"><div class="restaurant-name">${safeLink(r.source, escapeHtml(r.name), "restaurant-link")}</div><small>${escapeHtml(r.city)}</small></td>
      <td data-label="MICHELIN status">${distinctionLabel(r)}<span class="sr-only">${escapeHtml(status)}</span></td>
      <td data-label="Cluster">${escapeHtml(r.area)}</td>
      <td data-label="Days, hours & exceptions">${hoursText(r)}</td>
      <td data-label="Total for 2 adults"><span class="missing">Not verified</span><small>Official two-person total not confirmed.</small></td>
      <td data-label="Official social"><span class="missing">Not verified</span><small>No official social link confirmed.</small></td>
      <td data-label="Restaurant site">${r.website ? safeLink(r.website, "Official site ↗", "small-link") : `<span class="missing">Not verified</span>`}</td>
      <td data-label="Source">${safeLink(r.source, "MICHELIN ↗", "source-chip")}</td>
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
    }).sort((a, b) => (a.type === b.type ? (b.stars || 0) - (a.stars || 0) || a.name.localeCompare(b.name) : a.type === "star" ? -1 : 1));
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
    <text x="7" y="95" fill="#65756c" font-size="2.4">SCHEMATIC · NOT TO SCALE</text>
  </svg>`;
  $("#cluster-map").innerHTML = svg;
  const clusterCard = (c) => `<button type="button" class="cluster-card" data-area="${escapeHtml(c.name)}"><span class="cluster-count">${c.count}</span><span><b>${escapeHtml(c.name)}</b><small>${escapeHtml(c.sub)}</small></span><span class="cluster-arrow" aria-hidden="true">↗</span></button>`;
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
    <div class="hotel-topline"><span class="hotel-order">CANDIDATE ${String(index + 1).padStart(2,"0")}</span><span class="key-badge">${"◆".repeat(h.keys)} <span>${h.keys} MICHELIN ${h.keys === 1 ? "KEY" : "KEYS"}</span></span></div>
    <h3>${safeLink(h.source, escapeHtml(h.name), "hotel-name")}</h3>
    <p class="hotel-loc">${escapeHtml(h.neighborhood)} · ${escapeHtml(h.area)}</p>
    <p class="hotel-loc">${escapeHtml(h.address || "")}</p>
    <div class="hotel-fields"><div><small>MICHELIN Key status</small><b>${"◆".repeat(h.keys)} ${h.keys} Key${h.keys === 1 ? "" : "s"} (verified)</b></div><div><small>Example rate (2026-12-22 → 2026-12-23)</small><b class="${h.exampleRate && !h.exampleRate.startsWith("Not") ? "" : "missing"}">${h.exampleRate ? escapeHtml(h.exampleRate) : "Not verified"}</b></div><div><small>Guest score (of 20)</small><b class="${h.guestScore ? "" : "missing"}">${h.guestScore ? escapeHtml(h.guestScore) : "Not enough verified stays"}</b></div></div>
    <p class="hotel-caveat">Candidate order is for display only—not a recommendation rank. Key count and example rate verified from the official MICHELIN hotel profile on 2026-11-24; rate is date-specific and changes. Restaurant-count ranking within a chosen radius is not yet computed.</p>
    ${safeLink(h.source, "Official hotel profile ↗", "button button-outline")}
  </article>`).join("");

  const flags = {
    meal: d.restaurants.length,
    social: d.restaurants.filter((r) => !r.social).length,
    schedule: d.restaurants.filter((r) => !r.hours).length,
    dateExceptions: d.restaurants.filter((r) => r.hours && !r.exception).length,
    hotelNearby: d.hotels.length,
    hotelRate: d.hotels.filter((h) => !h.rateVerified).length
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
  }), {rootMargin:"-22% 0px -68% 0px"});
  document.querySelectorAll("main section[id]").forEach((section) => observer.observe(section));
})();
