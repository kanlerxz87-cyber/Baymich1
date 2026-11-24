#!/usr/bin/env python3
"""Apply Michelin-verified hours/days/address/website/cuisine to data/bibgourmand.json.

All values read from the official MICHELIN Guide restaurant profile pages
(guide.michelin.com) on 2026-11-24. Where Michelin does not publish hours on the
profile, hours/days are left blank (unverified) — never inferred.
"""
import json

# id -> verified fields from the official Michelin profile (2026-11-24)
verified = {
    "izakaya-rintaro": {
        "address": "82 14th St., San Francisco, CA 94103, USA",
        "website": "https://www.izakayarintaro.com/",
        "cuisine": "Japanese, Izakaya",
        "michelinPriceBracket": "$$",
    },
    "a16": {
        "address": "2355 Chestnut St., San Francisco, CA 94123, USA",
        "website": "https://www.a16pizza.com/",
        "cuisine": "Pizza, Italian",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu 5:00–9:30 PM; Fri–Sat 12:00–10:00 PM; Sun 12:00–9:30 PM",
        "daysOpen": "Monday–Sunday",
    },
    "z-y": {
        "address": "655 Jackson St., San Francisco, CA 94133, USA",
        "website": "https://www.zandyrestaurant.com/",
        "cuisine": "Chinese, Sichuan",
        "michelinPriceBracket": "$$",
        "hours": "Mon 11:30 AM–3:00 PM & 4:30–9:00 PM; Tue closed; Wed–Sun 11:30 AM–3:00 PM & 4:30–9:00 PM",
        "daysOpen": "Monday, Wednesday–Sunday (Tuesday closed)",
    },
    "good-good-culture-club": {
        "address": "3560 18th St., San Francisco, CA 94110, USA",
        "website": "https://goodgoodcultureclub.com/",
        "cuisine": "South East Asian, Californian",
        "michelinPriceBracket": "$$",
    },
    "kitchen-istanbul": {
        "address": "349 Clement St., San Francisco, CA 94118, USA",
        "website": "https://www.kitchenistanbulsf.com/",
        "cuisine": "Turkish, Californian",
        "michelinPriceBracket": "$$",
    },
    "okane": {
        "address": "669 Townsend St., San Francisco, CA 94103, USA",
        "website": "https://www.okanesf.com/",
        "cuisine": "Japanese, Izakaya",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu 11:30 AM–2:30 PM & 5:00–9:00 PM; Fri 11:30 AM–2:30 PM & 5:00–10:00 PM; Sat 5:00–10:00 PM; Sun 5:00–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "trestle": {
        "address": "531 Jackson St., San Francisco, CA 94133, USA",
        "website": "https://www.trestlesf.com/",
        "cuisine": "Contemporary, Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu & Sun 5:30–9:00 PM; Fri–Sat 5:30–10:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "bansang": {
        "address": "1560 Fillmore St., San Francisco, CA 94115, USA",
        "website": "https://bansangsf.com/",
        "cuisine": "Korean, Contemporary",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Tue closed; Wed–Thu & Sun 5:30–8:30 PM; Fri–Sat 5:30–9:00 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "dumpling-home": {
        "address": "298 Gough St., San Francisco, CA 94102, USA",
        "website": "https://www.dumplinghome.com/",
        "cuisine": "Chinese, Dumplings",
        "michelinPriceBracket": "$",
        "hours": "Mon–Thu & Sun 11:30 AM–2:15 PM & 5:00–8:15 PM; Fri–Sat 11:30 AM–2:15 PM & 5:00–8:45 PM",
        "daysOpen": "Monday–Sunday",
    },
    "anchor-oyster-bar": {
        "address": "579 Castro St., San Francisco, CA 94114, USA",
        "website": "https://www.anchoroysterbar.com/",
        "cuisine": "Seafood, Italian-American",
        "michelinPriceBracket": "$$",
        "hours": "Mon, Thu–Sun 2:00–8:00 PM; Tue–Wed closed",
        "daysOpen": "Monday, Thursday–Sunday",
    },
    "outerlands": {
        "address": "4001 Judah St., San Francisco, CA 94122, USA",
        "website": "https://outerlandssf.com/",
        "cuisine": "Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu 5:00–9:00 PM; Fri 5:00–9:30 PM; Sat 9:30 AM–2:00 PM & 4:30–9:30 PM; Sun 9:30 AM–2:00 PM & 4:30–9:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "mama-oakland": {
        "address": "388 Grand Ave., Oakland, CA 94610, USA",
        "website": "https://mama-oakland.com/",
        "cuisine": "Italian, Contemporary",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu & Sun 5:00–9:00 PM; Fri–Sat 5:00–9:30 PM",
        "daysOpen": "Monday–Sunday",
    },
    "soba-ichi": {
        "address": "2311A Magnolia St., Oakland, CA 94607, USA",
        "website": "https://sobaichioakland.com/",
        "cuisine": "Japanese",
        "michelinPriceBracket": "$$",
        "hours": "Mon, Wed–Sun 5:00–9:00 PM; Tue closed",
        "daysOpen": "Monday, Wednesday–Sunday",
    },
    "joodooboo": {
        "address": "4201 Market St., Oakland, CA 94608, USA",
        "website": "https://www.joodooboo.co/",
        "cuisine": "Korean, Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon closed; Tue–Sun 12:00–3:00 PM & 4:30–8:00 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "bombera": {
        "address": "3459 Champion St., Oakland, CA 94602, USA",
        "website": "https://www.bomberaoakland.com/",
        "cuisine": "Mexican, Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon, Wed–Sat 5:00–9:00 PM; Tue & Sun closed",
        "daysOpen": "Monday, Wednesday–Saturday",
    },
    "snail-bar": {
        "address": "4935 Shattuck Ave., Oakland, CA 94609, USA",
        "website": "https://snailbaroakland.com/",
        "cuisine": "Contemporary, Californian",
        "michelinPriceBracket": "$$$",
        "hours": "Mon, Fri–Sun 5:00–9:00 PM (Fri–Sat to 10:00 PM); Tue–Thu closed",
        "daysOpen": "Monday, Friday–Sunday",
    },
    "comal": {
        "address": "2020 Shattuck Ave., Berkeley, CA 94704, USA",
        "website": "https://www.comalberkeley.com/",
        "cuisine": "Mexican",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Wed & Sun 5:00–9:00 PM; Thu–Sat 5:00–10:00 PM",
        "daysOpen": "Monday–Sunday",
    },
    "ippuku": {
        "address": "2130 Center St., Berkeley, CA 94704, USA",
        "website": "https://ippukuberkeley.com/",
        "cuisine": "Japanese",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu & Sun 5:00–9:30 PM; Fri–Sat 5:00–10:30 PM",
        "daysOpen": "Monday–Sunday",
    },
    "spinning-bones": {
        "address": "1205 Park St., Alameda, CA 94501, USA",
        "website": "https://www.spinningbones.com/",
        "cuisine": "Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Tue closed; Wed–Thu & Sun 11:30 AM–8:00 PM; Fri–Sat 11:30 AM–9:00 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "great-china": {
        "address": "2190 Bancroft Way, Berkeley, CA 94704, USA",
        "website": "https://www.greatchinaberkeley.com/",
        "cuisine": "Chinese",
        "michelinPriceBracket": "$$",
        "hours": "Mon, Wed–Sun 5:00–8:30 PM; Tue closed",
        "daysOpen": "Monday, Wednesday–Sunday",
    },
    "playa": {
        "address": "41 Throckmorton Ave., Mill Valley, CA 94941, USA",
        "website": "https://www.playamv.com/",
        "cuisine": "Mexican, Contemporary",
        "michelinPriceBracket": "$$",
        "hours": "Mon closed; Tue 4:00–9:00 PM; Wed–Thu 11:30 AM–2:00 PM & 4:00–9:00 PM; Fri 11:30 AM–10:00 PM; Sat 11:00 AM–10:00 PM; Sun 11:00 AM–8:00 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "jos-modern-thai": {
        "address": "3725 MacArthur Blvd., Oakland, CA 94619, USA",
        "website": "https://www.josmodernthai.com/",
        "cuisine": "Thai, Californian",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Tue closed; Wed–Thu & Sun 12:00–2:30 PM & 5:00–9:00 PM; Fri–Sat 12:00–2:30 PM & 5:00–9:30 PM",
        "daysOpen": "Wednesday–Sunday",
    },
    "new-dumpling": {
        "address": "10064 San Pablo Ave., El Cerrito, CA 94530, USA",
        "website": "https://www.newdumplingfood.com/",
        "cuisine": "Chinese, Dumplings",
        "michelinPriceBracket": "$",
    },
    "fob-kitchen": {
        "address": "5179 Telegraph Ave., Oakland, CA 94609, USA",
        "website": "https://www.fobkitchen.com/",
        "cuisine": "Filipino, Contemporary",
        "michelinPriceBracket": "$$",
        "hours": "Mon closed; Tue 9:00 AM–2:00 PM; Wed–Sun 11:00 AM–9:00 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "tacos-oscar": {
        "address": "420 40th St., Oakland, CA 94609, USA",
        "website": "https://www.tacososcar.com/",
        "cuisine": "Mexican, Contemporary",
        "michelinPriceBracket": "$",
        "hours": "Mon & Thu 5:00–9:00 PM; Tue–Wed closed; Fri 5:00–9:30 PM; Sat–Sun 11:00 AM–2:00 PM & 5:00–9:30 PM (Sun dinner to 9:00 PM)",
        "daysOpen": "Monday, Thursday–Sunday",
    },
    "teni-east-kitchen": {
        "address": "4015 Broadway, Oakland, CA 94611, USA",
        "website": "https://www.tenieastkitchen.com/",
        "cuisine": "Burmese",
        "michelinPriceBracket": "$",
        "hours": "Mon closed; Tue–Thu 5:00–9:00 PM; Fri–Sat 5:00–9:30 PM; Sun 5:00–8:30 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "top-hatters-kitchen": {
        "address": "855 MacArthur Blvd., San Leandro, CA 94577, USA",
        "website": "https://tophatterskitchen.com/",
        "cuisine": "Contemporary, Vietnamese",
        "michelinPriceBracket": "$$",
        "hours": "Mon closed; Tue–Sun 11:45 AM–2:30 PM & 4:45–8:30 PM",
        "daysOpen": "Tuesday–Sunday",
    },
    "insalatas": {
        "address": "120 Sir Francis Drake Blvd., San Anselmo, CA 94960, USA",
        "website": "https://insalatas.com/",
        "cuisine": "Mediterranean Cuisine",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu 11:30 AM–2:30 PM & 5:00–8:30 PM; Fri–Sat 11:30 AM–2:30 PM & 5:00–9:00 PM; Sun 11:00 AM–2:30 PM & 5:00–8:30 PM",
        "daysOpen": "Monday–Sunday",
    },
    "pausa": {
        "address": "223 E. 4th Ave., San Mateo, CA 94401, USA",
        "website": "https://www.pausasanmateo.com/",
        "cuisine": "Italian, Regional Cuisine",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Thu 4:30–9:00 PM; Fri–Sat 4:00–9:30 PM; Sun 4:00–8:30 PM",
        "daysOpen": "Monday–Sunday",
    },
    "village-sake": {
        "address": "19 Bolinas Rd., Fairfax, CA 94930, USA",
        "website": "https://www.villagesake.com/",
        "cuisine": "Japanese",
        "michelinPriceBracket": "$$",
        "hours": "Mon–Tue closed; Wed–Thu & Sun 5:00–8:00 PM; Fri–Sat 5:00–8:30 PM",
        "daysOpen": "Wednesday–Sunday",
    },
}

path = "data/bibgourmand.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)

rs = data["restaurants"] if "restaurants" in data else data
applied = 0
for r in rs:
    rec = verified.get(r["id"])
    if not rec:
        print(f"  ! no verified record for id={r['id']} ({r.get('name')})")
        continue
    for k, v in rec.items():
        r[k] = v
    r["hoursVerified"] = bool(rec.get("hours"))
    r["hoursSource"] = r.get("michelinLink") or "https://guide.michelin.com"
    applied += 1

data.setdefault("meta", {})
data["meta"]["verificationPolicy"] = (
    "Distinction, city, cuisine, Michelin price bracket, address and website verified against each "
    "restaurant's official MICHELIN Guide profile (guide.michelin.com) on 2026-11-24. Hours/days are "
    "verified only where Michelin publishes them on the profile; where absent, hours stay blank and are "
    "flagged unverified. Exact dollar prices are not listed on Michelin profiles and are left blank unless "
    "confirmed from the restaurant's own official source."
)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

with_hours = sum(1 for r in rs if r.get("hours"))
print(f"Updated {applied} Bib Gourmand records; {with_hours} with verified hours; "
      f"{applied - with_hours} hours unverified (not published on Michelin profile)")
