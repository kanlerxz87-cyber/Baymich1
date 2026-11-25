// Applies official MICHELIN restaurant-page reads (data/official_one_star_reads_2026-11-25.json)
// to data.js, and clears social handles that were not confirmed from an official restaurant site.
// Usage: node scripts/apply_one_star_reads_2026-11-25.js
const fs = require("fs");
const path = require("path");
const root = path.join(__dirname, "..");
const dataPath = path.join(root, "data.js");
const readsPath = path.join(root, "data", "official_one_star_reads_2026-11-25.json");
const candidatesPath = path.join(root, "data", "social_candidates_unverified_2026-11-25.json");

global.window = {};
require("vm").runInThisContext(fs.readFileSync(dataPath, "utf8"));
const bay = window.BAY_DATA;
const reads = JSON.parse(fs.readFileSync(readsPath, "utf8")).reads;
const nameMap = { "The Restaurant at Auberge du Soleil": "Auberge du Soleil" };
const DATE = "2026-11-25";
const DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

let applied = 0;
for (const rd of reads) {
  const key = nameMap[rd.name] || rd.name;
  const r = bay.restaurants.find((x) => x.name === key && x.type === "star");
  if (!r) throw new Error("No roster row for " + rd.name);
  r.address = rd.address;
  r.cuisine = rd.cuisine;
  r.price = rd.price;
  if (rd.website) r.website = rd.website;
  if (rd.phone) r.phone = rd.phone;
  r.source = rd.url;
  const hrs = rd.hours || {};
  if (Object.keys(hrs).length) {
    r.hours = {};
    for (const d of DAYS) r.hours[d] = hrs[d] ? hrs[d] : "Not verified";
  } else {
    delete r.hours;
  }
  if (rd.note) r.flag = rd.note;
  else delete r.flag;
  r.verified = "Official Michelin page read " + DATE;
  applied++;
}

// Social handles: keep none as verified. Save the previous candidates for review, unrendered.
const candidates = [];
for (const r of bay.restaurants) {
  if (r.social) {
    candidates.push({ name: r.name, candidate_handles: r.social, cited_basis: r.socialSource || "" });
    delete r.social;
    delete r.socialSource;
  }
}
fs.writeFileSync(candidatesPath, JSON.stringify({
  _note: "UNVERIFIED candidate social handles carried from earlier passes. Each cited a third-party aggregator (or, for Atelier Crenn, a sameAs claim that could not be reproduced on 2026-11-25 from the official homepage text). Not shown as links on the site. Confirm each from the restaurant's own website before use.",
  checked: DATE,
  candidates
}, null, 2) + "\n");

bay.checked = DATE;
const header = "/* Primary-source records. Current-star scope: 2026 MICHELIN Guide California roster (nine-county filter). Blank values are intentionally not inferred. Last edits: 2026-11-25 (official MICHELIN restaurant pages for 19 one-star rows; social handles cleared pending official confirmation). */\n";
const body = "window.BAY_DATA = " + JSON.stringify(bay, null, 2)
  .replace(/"([A-Za-z_][A-Za-z0-9_]*)":/g, "$1:") + ";\n";
fs.writeFileSync(dataPath, header + body);
console.log("applied", applied, "social cleared", candidates.length);
