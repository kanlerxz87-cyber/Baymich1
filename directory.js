const escapeText = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const select = document.getElementById('city-filter');
[...new Set(restaurants.map(r=>r.city))].sort().forEach(city=>{const o=document.createElement('option');o.value=city;o.textContent=city;select.append(o)});
const rows = document.getElementById('restaurant-rows');
rows.innerHTML = restaurants.map(r=>{
  const badge = r.stars ? `${r.stars} ${r.stars===1?'Michelin star':'Michelin stars'} · 2026` : 'Guide Recommended · 2026';
  const profile = `<a href="${r.url}" target="_blank" rel="noopener">Michelin profile ↗</a>`;
  const venue = r.officialUrl ? `<a href="${r.officialUrl}" target="_blank" rel="noopener">Official venue site ↗</a>` : '';
  const source = `<a href="${MICHELIN_2026}" target="_blank" rel="noopener">2026 Michelin selection ↗</a>`;
  const menu = r.priceText ? `<a href="${r.priceUrl}" target="_blank" rel="noopener">${escapeText(r.priceText)} ↗</a>` : '<span class="empty-field">— not verified</span>';
  const media = r.socials?.length ? r.socials.map(s=>`<a href="${s.url}" target="_blank" rel="noopener">${escapeText(s.label)} ↗</a>`).join('<br>') : '<span class="social-empty">Not verified</span>';
  return `<tr data-city="${escapeText(r.city)}" data-stars="${r.stars||'recommended'}" data-search="${escapeText((r.name+' '+r.city).toLowerCase())}"><td><span class="restaurant-name">${escapeText(r.name)}${r.newIn2026?' <span class="new-tag">NEW 2026</span>':''}</span><span class="star-badge ${r.stars?'':'recommended-badge'}">${badge}</span></td><td class="city-cell">${escapeText(r.city)}</td><td>${menu}</td><td class="empty-field">— not verified</td><td><div class="table-links">${profile}${venue}${source}</div></td><td>${media}</td><td class="status-cell">${escapeText(r.note||(r.priceText?'Menu total excludes tax and beverages; hours require verification.':'Couple total and hours require official-source review.'))}</td></tr>`;
}).join('');
const search = document.getElementById('restaurant-search'), stars = document.getElementById('star-filter'), count = document.getElementById('result-count');
function applyFilters(){let n=0;for(const row of rows.rows){const ok=row.dataset.search.includes(search.value.trim().toLowerCase())&&(stars.value==='all'||row.dataset.stars===stars.value)&&(select.value==='all'||row.dataset.city===select.value);row.hidden=!ok;if(ok)n++;}count.textContent=`${n} ${n===1?'entry':'entries'}`;}
[search,stars,select].forEach(el=>{el.addEventListener('input',applyFilters);el.addEventListener('change',applyFilters)});applyFilters();
