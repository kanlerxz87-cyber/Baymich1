#!/usr/bin/env python3
"""Apply official Michelin page reads (2026-11-25) to the 27 one-star entries in data.js.
Preserves existing social/socialSource fields. Hours normalized to data.js style (en-dash, am/pm).
"""
import json, re, sys

DATA_JS = "data.js"
JSON_PATH = "data/michelin_official_pages_2026-11-25.json"

with open(JSON_PATH) as f:
    records = json.load(f)["records"]

def norm_time(t):
    # "11:30 AM-2 PM" -> "11:30 am–2:00 pm"; "5 PM-9 PM" -> "5:00–9:00 pm"
    t = t.strip()
    parts = re.split(r"\s*&\s*", t)
    out = []
    for p in parts:
        m = re.match(r"^\s*(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?\s*-\s*(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\s*$", p, re.I)
        if not m:
            out.append(p)
            continue
        h1, m1, ap1, h2, m2, ap2 = m.groups()
        m1 = m1 or "00"; m2 = m2 or "00"
        ap1 = ap1 or ap2
        out.append(f"{int(h1)}:{m1} {ap1.lower()}–{int(h2)}:{m2} {ap2.lower()}")
    return " & ".join(out)

def hours_obj(schedule):
    # schedule: "Mon 5:30-9 PM; Tue closed; ..."
    days = []
    for chunk in schedule.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        day = chunk.split()[0]
        rest = chunk[len(day):].strip()
        if rest.lower() == "closed":
            days.append((day, "Closed"))
        else:
            days.append((day, norm_time(rest)))
    order = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    d = dict(days)
    return "hours:{" + ",".join(f'{k}:"{d[k]}"' for k in order) + "}"

with open(DATA_JS) as f:
    text = f.read()

# update checked date
text = text.replace('checked: "2026-11-24"', 'checked: "2026-11-25"', 1)

for name, rec in records.items():
    # find the line for this restaurant
    pat = re.compile(r'\{name:"' + re.escape(name) + r'".*?\},?\n')
    m = pat.search(text)
    if not m:
        print(f"NOT FOUND: {name}", file=sys.stderr)
        sys.exit(1)
    old = m.group(0)
    # extract existing social/socialSource/website if present
    soc = re.search(r'social:\{[^}]*\}', old)
    soc_src = re.search(r'socialSource:"[^"]*"', old)
    # build new entry
    fields = [f'name:"{name}"']
    city = re.search(r'city:"([^"]*)"', old).group(1)
    area = re.search(r'area:"([^"]*)"', old).group(1)
    fields.append(f'city:"{city}"')
    fields.append(f'area:"{area}"')
    fields.append('type:"star"')
    fields.append('stars:1')
    fields.append(f'address:"{rec["address"]}"')
    fields.append(f'cuisine:"{rec["cuisine"]}"')
    fields.append(f'price:"{rec["price"]}"')
    fields.append(f'website:"{rec["website"]}"')
    if rec["phone"] != "not on page":
        fields.append(f'phone:"{rec["phone"]}"')
    fields.append(f'source:"{rec["url"]}"')
    fields.append('verified:"Official Michelin page read 2026-11-25"')
    fields.append(hours_obj(rec["schedule"]))
    if soc:
        fields.append(soc.group(0))
    if soc_src:
        fields.append(soc_src.group(0))
    new = "{" + ",".join(fields) + "},\n"
    text = text.replace(old, new, 1)
    print(f"updated: {name}")

with open(DATA_JS, "w") as f:
    f.write(text)
print("done")
