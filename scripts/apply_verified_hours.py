#!/usr/bin/env python3
"""Apply Michelin-verified hours/address/website/cuisine/price-band to data/restaurants.json.

All values below were read from the official MICHELIN Guide restaurant profile pages
(guide.michelin.com) on 2026-11-24. Fields not present in an official source are left
untouched (blank/unverified) — never inferred.
"""
import json

MICH = "https://guide.michelin.com"

# id -> verified fields from the official Michelin profile (2026-11-24)
verified = {
    "quince": {
        "address": "470 Pacific Ave., San Francisco, CA 94133, USA",
        "website": "https://www.quincerestaurant.com/",
        "cuisine": "Contemporary, Californian",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Thu 5:00–9:00 PM; Fri–Sat 11:30 AM–1:00 PM & 5:00–9:00 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "californios": {
        "address": "355 11th St., San Francisco, CA 94103, USA",
        "website": "https://www.californiossf.com/",
        "cuisine": "Mexican, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:00–10:00 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "benu": {
        "address": "22 Hawthorne St., San Francisco, CA 94105, USA",
        "website": "https://www.benusf.com/",
        "cuisine": "Asian, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Tue closed; Wed–Thu 5:00–8:00 PM; Fri–Sat 5:00–8:30 PM; Sun closed",
        "daysOpen": "Wednesday–Saturday",
    },
    "atelier-crenn": {
        "address": "3127 Fillmore St., San Francisco, CA 94123, USA",
        "website": "https://www.ateliercrenn.com/",
        "cuisine": "Contemporary, French",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 4:45–8:45 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "acquerello": {
        "address": "1722 Sacramento St., San Francisco, CA 94109, USA",
        "website": "https://www.acquerellosf.com/",
        "cuisine": "Italian, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:30–9:45 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "kiln": {
        "address": "149 Fell St., San Francisco, CA 94102, USA",
        "website": "https://www.kilnsf.com/",
        "cuisine": "Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Thu 6:00–8:00 PM; Fri–Sat 5:00–8:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "lazy-bear": {
        "address": "3416 19th St., San Francisco, CA 94110, USA",
        "website": "https://www.lazybearsf.com/",
        "cuisine": "Contemporary, Modern Cuisine",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:00–11:00 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "saison": {
        "address": "178 Townsend St., San Francisco, CA 94107, USA",
        "website": "https://www.saisonsf.com/",
        "cuisine": "Californian, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:00–9:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "sons-daughters": {
        "address": "2875 18th St., San Francisco, CA 94110, USA",
        "website": "https://www.sonsanddaughterssf.com/",
        "cuisine": "Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:30–8:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "birdsong": {
        "address": "1085 Mission St., San Francisco, CA 94103, USA",
        "website": "https://www.birdsongsf.com/",
        "cuisine": "Contemporary, American",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Thu 5:30–8:00 PM; Fri–Sat 5:00–8:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "commis": {
        "address": "3859 Piedmont Ave., Oakland, CA 94611, USA",
        "website": "https://commisrestaurant.com/",
        "cuisine": "Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:00–9:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "niku-steakhouse": {
        "address": "61 Division St., San Francisco, CA 94103, USA",
        "website": "https://www.nikusteakhouse.com/",
        "cuisine": "Steakhouse",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Thu 5:00–9:00 PM; Fri–Sat 5:00–10:00 PM; Sun 5:00–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "wolfsbane": {
        "address": "2495 3rd St., San Francisco, CA 94107, USA",
        "website": "https://wolfsbanesf.com/",
        "cuisine": "Contemporary, Californian",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Sat 5:30–10:00 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "san-ho-won": {
        "address": "2170 Bryant St., San Francisco, CA 94110, USA",
        "website": "https://www.sanhowon.com/",
        "cuisine": "Korean, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Fri 5:00–10:00 PM; Sat–Sun 4:30–10:00 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "ssal": {
        "address": "2226 Polk St., San Francisco, CA 94109, USA",
        "website": "https://ssalsf.com/",
        "cuisine": "Korean, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Tue closed; Wed–Sun 5:30–8:30 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "state-bird-provisions": {
        "address": "1529 Fillmore St., San Francisco, CA 94115, USA",
        "website": "https://www.statebirdsf.com/",
        "cuisine": "Californian",
        "michelinPriceBracket": "$$$",
        "hours": "Mon–Thu 5:30–10:00 PM; Fri closed; Sat 5:30–10:30 PM; Sun 5:30–10:00 PM",
        "daysOpen": "Monday–Sunday (Friday closed)",
    },
    "hilda-and-jesse": {
        "address": "701 Union St., San Francisco, CA 94133, USA",
        "website": "https://www.hildaandjessesf.com/",
        "cuisine": "American, Contemporary",
        "michelinPriceBracket": "$$$",
        "hours": "Mon 5:30–9:00 PM; Tue–Wed closed; Thu–Fri 5:30–9:00 PM; Sat–Sun 10:00 AM–2:00 PM",
        "daysOpen": "Monday, Thursday–Sunday",
    },
    "nisei": {
        "address": "2316 Polk St., San Francisco, CA 94109, USA",
        "website": "https://www.restaurantnisei.com/",
        "cuisine": "Japanese, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Tue closed; Wed–Sun 5:00–9:00 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "naides": {
        "address": "708 Bush St., San Francisco, CA 94108, USA",
        "website": "https://www.restaurantnaides.com/",
        "cuisine": "Filipino, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Wed closed; Thu–Sun 5:30–8:30 PM",
        "daysOpen": "Thursday–Sunday",
    },
    "nari": {
        "address": "Hotel Kabuki - JDV by Hyatt, 1625 Post St., San Francisco, CA 94115, USA",
        "website": "https://www.narisf.com/",
        "cuisine": "Thai, Contemporary",
        "michelinPriceBracket": "$$$",
        "hours": "Mon–Thu 5:30–9:00 PM; Fri–Sat 5:30–9:30 PM; Sun 5:30–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "mister-jius": {
        "address": "28 Waverly Pl., San Francisco, CA 94108, USA",
        "website": "https://misterjius.com/",
        "cuisine": "Chinese, Contemporary",
        "michelinPriceBracket": "$$$",
        "hours": "Mon closed; Tue–Thu 5:00–9:00 PM; Fri–Sat 5:00–9:30 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "angler-sf": {
        "address": "132 The Embarcadero, San Francisco, CA 94105, USA",
        "website": "https://anglersf.com/",
        "cuisine": "Contemporary, Seafood",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon 5:00–9:00 PM; Tue–Sat 11:30 AM–2:00 PM & 5:00–9:00 PM; Sun 5:00–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "kin-khao": {
        "address": "Parc 55 San Francisco - a Hilton Hotel, 55 Cyril Magnin St., San Francisco, CA 94102, USA",
        "website": "https://www.kinkhao.com/",
        "cuisine": "Thai, Californian",
        "michelinPriceBracket": "$$$",
        "hours": "Mon–Thu 11:30 AM–2:00 PM & 5:30–9:00 PM; Fri–Sat 11:30 AM–2:00 PM & 5:30–10:00 PM; Sun 11:30 AM–2:00 PM & 5:30–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "7-adams": {
        "address": "1963 Sutter St., San Francisco, CA 94115, USA",
        "website": "https://www.7adamsrestaurant.com/",
        "cuisine": "Californian, Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Thu 5:30–9:00 PM; Fri–Sat 5:00–10:00 PM; Sun 5:00–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "sorrel": {
        "address": "3228 Sacramento St., San Francisco, CA 94115, USA",
        "website": "https://www.sorrelrestaurant.com/",
        "cuisine": "Contemporary, Italian",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Tue closed; Wed–Sun 5:00–9:00 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "the-progress": {
        "address": "1525 Fillmore St., San Francisco, CA 94115, USA",
        "website": "https://theprogress-sf.com/",
        "cuisine": "Californian",
        "michelinPriceBracket": "$$$",
        "hours": "Mon–Sun 5:30–10:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "sun-moon-studio": {
        "address": "1940 Union St., Ste. 21, Oakland, CA 94607, USA",
        "website": "https://www.sunmoonstudio.com/",
        "cuisine": "Californian",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Wed closed; Thu–Sat 5:00–9:00 PM; Sun 5:00–8:00 PM",
        "daysOpen": "Thursday–Sunday",
    },
    "madcap": {
        "address": "198 Sir Francis Drake Blvd., San Anselmo, CA 94960, USA",
        "website": "https://www.madcapmarin.com/",
        "cuisine": "Contemporary, Asian Contemporary",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon closed; Tue–Thu 5:30–8:30 PM; Fri–Sat 5:30–9:00 PM; Sun closed",
        "daysOpen": "Tuesday–Saturday",
    },
    "wakuriya": {
        "address": "115 De Anza Blvd., San Mateo, CA 94402, USA",
        "website": "https://www.wakuriya.com/",
        "cuisine": "Japanese, Californian",
        "michelinPriceBracket": "$$$$",
        "hours": "Mon–Tue closed; Wed–Fri 6:30–9:30 PM; Sat–Sun 6:00–9:00 PM",
        "daysOpen": "Wednesday–Sunday",
    },
}

path = "data/restaurants.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)

applied = 0
for r in data["restaurants"]:
    rec = verified.get(r["id"])
    if not rec:
        print(f"  ! no verified record for id={r['id']} ({r['name']})")
        continue
    for k, v in rec.items():
        r[k] = v
    r["hoursVerified"] = True
    r["hoursSource"] = r.get("michelinLink") or f"{MICH}/us/en/california/{r['city'].lower()}/restaurant"
    applied += 1

data["meta"]["verificationPolicy"] = (
    "Distinction, star level, city, cuisine, Michelin price bracket, address, website, "
    "opening hours and days open were verified against each restaurant's official MICHELIN "
    "Guide profile (guide.michelin.com) on 2026-11-24. Exact 2-adult pricing is only marked "
    "verified when confirmed from the restaurant's own official menu/fee page; blank or "
    "'sources vary' values are flagged unverified and never inferred. Exceptions and social "
    "links are left blank unless confirmed from an official source."
)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Updated {applied} restaurant records in {path}")
