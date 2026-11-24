const cityFilter = document.getElementById('city-filter');
const cityNames = [...new Set(restaurants.map(r => r.city))].sort((a,b) => a.localeCompare(b));
cityNames.forEach(city => {
  const option = document.createElement('option'); option.value = city; option.textContent = city; cityFilter.append(option);
});

const starText = r => r.stars ? `${r.stars} ${r.stars === 1 ? 'Michelin star' : 'Michelin stars'} · 2026` : 'Guide Recommended · 2026';
const rowMarkup = r => {
  const badgeClass = r.stars ? 'star-badge' : 'star-badge recommended-badge';
  const name = escapeHtml(r.name);
  const city = escapeHtml(r.city);
  const newTag = r.newIn2026 ? ' <span class="new-tag">NEW 2026</span>' : '';
  const totalCell = r.priceText ? `<a href="${r.priceUrl}" target="_blank" rel="noopener">${escapeHtml(r.priceText)} ↗</a>` : '<span class="empty-field">— not verified</span>';
  const venueLink = r.officialUrl ? `<a href="${r.officialUrl}" target="_blank" rel="noopener">Official venue site ↗</a>` : '';
  const socialLinks = r.socials?.length ? r.socials.map(s => `<a href="${s.url}" target="_blank" rel="noopener">${escapeHtml(s.label)} ↗</a>`).join('<br>') : '<span class="social-empty">Not verified</span>';
  const status = [r.priceText ? 'Menu total excludes tax/drinks.' : 'Couple total not confirmed.',r.note].filter(Boolean).join(' ');
  return `<tr data-city="${city}" data-stars="${r.stars || 'recommended'}" data-search="${escapeHtml((r.name+' '+r.city).toLowerCase())}">
    <td><span class="restaurant-name">${name}${newTag}</span><span class="${badgeClass}">${starText(r)}</span></td>
    <td class="city-cell">${city}</td>
    <td>${totalCell}</td>
    <td class="empty-field">— not verified</td>
    <td><div class="table-links"><a href="${r.url}" target="_blank" rel="noopener">Michelin profile ↗</a>${venueLink}<a href="${MICHELIN_2026}" target="_blank" rel="noopener">2026 selection ↗</a></div></td>
    <td>${socialLinks}</td>
    <td class="status-cell">${escapeHtml(status || 'Hours require official-source review.')}</td>
  </tr>`;
};
function escapeHtml(value){return String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
const tbody = document.getElementById('restaurant-rows');
tbody.innerHTML = restaurants.map(rowMarkup).join('');

document.getElementById('stat-restaurants').textContent = restaurants.filter(r => r.stars > 0).length;
document.getElementById('stat-three').textContent = restaurants.filter(r => r.stars === 3).length;
document.getElementById('stat-cities').textContent = new Set(restaurants.filter(r => r.stars > 0).map(r => r.city)).size;
const sfCount = restaurants.filter(r => r.stars > 0 && r.city === 'San Francisco').length;
document.getElementById('sf-summary').textContent = `${sfCount} restaurants with one to three Michelin stars in the 2026 selection, plus the separately labeled Recommended example. The city's roster is the largest cluster in this dataset.`;

const clusterGrid = document.getElementById('cluster-grid');
areaGroups.forEach(group => {
  const members = restaurants.filter(r => r.stars > 0 && group.cities.includes(r.city));
  const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(group.mapLabel)}`;
  const cityList = group.cities.join(', ');
  const card = document.createElement('article');
  card.className = 'cluster-card';
  card.innerHTML = `<div class="cluster-top"><h3>${escapeHtml(group.name)}</h3><span class="cluster-count">${members.length}<small>starred</small></span></div><div class="cluster-links"><button type="button" data-cluster-cities="${escapeHtml(group.cities.join('|'))}">Filter directory →</button><a href="${mapsUrl}" target="_blank" rel="noopener">Open map search ↗</a></div>`;
  clusterGrid.append(card);
});

const searchInput = document.getElementById('restaurant-search');
const starFilter = document.getElementById('star-filter');
const resultCount = document.getElementById('result-count');
function filterRows(){
  const query = searchInput.value.trim().toLowerCase();
  const selectedStars = starFilter.value;
  const selectedCity = cityFilter.value;
  let shown = 0;
  [...tbody.rows].forEach(row => {
    const searchMatch = row.dataset.search.includes(query);
    const starMatch = selectedStars === 'all' || row.dataset.stars === selectedStars;
    const cityMatch = selectedCity === 'all' || row.dataset.city === selectedCity;
    const visible = searchMatch && starMatch && cityMatch;
    row.hidden = !visible;
    if(visible) shown++;
  });
  resultCount.textContent = `${shown} entr${shown === 1 ? 'y' : 'ies'}`;
}
[searchInput,starFilter,cityFilter].forEach(el => el.addEventListener('input',filterRows));
[starFilter,cityFilter].forEach(el => el.addEventListener('change',filterRows));
clusterGrid.addEventListener('click', event => {
  const button = event.target.closest('button[data-cluster-cities]');
  if(!button) return;
  const cities = button.dataset.clusterCities.split('|');
  cityFilter.value = cities.length === 1 ? cities[0] : 'all';
  if(cities.length > 1) {
    searchInput.value = '';
    [...tbody.rows].forEach(row => { row.hidden = !(cities.includes(row.dataset.city) && (starFilter.value === 'all' || row.dataset.stars === starFilter.value)); });
    const shown = [...tbody.rows].filter(row => !row.hidden).length;
    resultCount.textContent = `${shown} entries · ${button.closest('.cluster-card').querySelector('h3').textContent}`;
  } else filterRows();
  document.getElementById('restaurants').scrollIntoView({behavior:'smooth'});
});
filterRows();

document.querySelectorAll('[data-filter-city]').forEach(link => link.addEventListener('click', event => {
  event.preventDefault(); cityFilter.value = link.dataset.filterCity; filterRows(); document.getElementById('restaurants').scrollIntoView({behavior:'smooth'});
}));
const menuToggle = document.getElementById('menu-toggle');
const nav = document.getElementById('primary-nav');
menuToggle.addEventListener('click', () => {const open = nav.classList.toggle('open'); menuToggle.setAttribute('aria-expanded', String(open));});
nav.addEventListener('click', event => {if(event.target.matches('a')){nav.classList.remove('open');menuToggle.setAttribute('aria-expanded','false');}});
