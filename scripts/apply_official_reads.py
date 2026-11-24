#!/usr/bin/env python3
"""Apply official Michelin page reads to the starred-restaurant lines in data.js.

Source of values: data/michelin_official_pages_2026-11-24.json (address, cuisine,
price tier, website, phone, schedule URL). Hours are transcribed from the
schedule text recorded in that file. Only the entries listed in HOURS are
rewritten; every other line in data.js is left byte-for-byte unchanged.

Run from the repository root:  python3 scripts/apply_official_reads.py
"""
import json
import re
import sys

CHECKED = "2026-11-24"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def week(open_days, hours, closed="Closed"):
    """Build a Mon..Sun map: days in open_days get `hours`; others get `closed`."""
    return {d: (hours if d in open_days else closed) for d in DAYS}


TUE_SAT = ["Tue", "Wed", "Thu", "Fri", "Sat"]
TUE_THU = ["Tue", "Wed", "Thu"]
WED_SAT = ["Wed", "Thu", "Fri", "Sat"]

HOURS = {
    "Benu": {**week(["Wed", "Thu"], "5:00–8:00 pm"), "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm"},
    "Atelier Crenn": week(TUE_SAT, "4:45–8:45 pm"),
    "Californios": week(TUE_SAT, "5:00–10:00 pm"),
    "Quince": {**week(TUE_THU, "5:00–9:00 pm"),
               "Fri": "11:30 am–1:00 pm & 5:00–9:00 pm", "Sat": "11:30 am–1:00 pm & 5:00–9:00 pm"},
    "Enclos": week(WED_SAT, "5:30–8:00 pm"),
    "SingleThread": week(DAYS, "4:00–8:45 pm"),
    "The French Laundry": week(DAYS, "4:00–8:00 pm"),
    "Acquerello": week(TUE_SAT, "5:30–9:45 pm"),
    "Birdsong": {**week(TUE_THU, "5:30–8:00 pm"), "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm"},
    "Kiln": {**week(TUE_THU, "6:00–8:00 pm"), "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm"},
    "Lazy Bear": week(TUE_SAT, "5:00–11:00 pm"),
    "Saison": week(TUE_SAT, "5:00–9:30 pm"),
    "Commis": week(TUE_SAT, "5:00–9:30 pm"),
    "Sons & Daughters": None,  # chunk 0 of the official page did not include the schedule
}

# Couple (2 adults) figures carried from the earlier verified set (COORDINATION T11), restated
# as arithmetic on the official per-person prices. Tax and gratuity excluded. Not re-checked
# against the restaurant sites in this session.
COUPLE = {
    "Benu": {"base_for_2": 850, "per_person": 425, "fees": "22% service", "total_before_tax": 1037,
             "basis": "$425 pp × 2 = $850; + 22% service = $1,037", "source": "https://benusf.com/info"},
    "Acquerello": {"base_for_2": 590, "per_person": 295, "fees": "20% service + 4% surcharge", "total_before_tax": None,
                   "basis": "$295 pp × 2 = $590 before 20% service and 4% surcharge (surcharge base not stated, so no all-in total)",
                   "source": "https://acquerellosf.com/"},
    "Kiln": {"base_for_2": 630, "per_person": 315, "fees": "20% service", "total_before_tax": 756,
             "basis": "$315 pp × 2 = $630; + 20% service = $756", "source": "https://kilnsf.com/information"},
    "Commis": {"base_for_2": 558, "per_person": 279, "fees": "20% service", "total_before_tax": 670,
               "basis": "$279 pp × 2 = $558; + 20% service = $669.60, rounded $670", "source": "https://commisrestaurant.com/info"},
    "Birdsong": {"base_for_2": 700, "per_person": 350, "fees": "service not stated", "total_before_tax": None,
                 "basis": "Journey menu $350 pp × 2 = $700 food base (Discovery $290 pp = $580); service not stated on source",
                 "source": "https://birdsongsf.com/experience"},
}


def js(value):
    """Serialize a Python value as a JS literal (strings double-quoted, numbers bare, None as null)."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        return "{" + ",".join(f"{k}:{js(v)}" for k, v in value.items()) + "}"
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return '"' + text + '"'


def field(line, key):
    m = re.search(key + r':"([^"]*)"', line)
    return m.group(1) if m else None


def main():
    records = json.load(open("data/michelin_official_pages_2026-11-24.json", encoding="utf-8"))["records"]
    lines = open("data.js", encoding="utf-8").read().split("\n")
    out, done = [], set()
    for line in lines:
        m = re.match(r'^(\s*)\{name:"([^"]+)"', line)
        if not (m and m.group(2) in HOURS):
            out.append(line)
            continue
        name = m.group(2)
        rec = records[name]
        if name not in records:
            sys.exit("no official page read for " + name)
        stars = re.search(r"stars:(\d+)", line).group(1)
        entry = {
            "name": name,
            "city": field(line, "city"),
            "area": field(line, "area"),
            "type": "star",
            "stars": int(stars),
            "address": rec["address"],
            "cuisine": rec["cuisine"],
            "price": rec["price"],
            "website": rec["website"],
            "phone": rec["phone"],
            "source": rec["url"],
            "verified": "Official Michelin page read " + CHECKED,
        }
        if HOURS[name] is not None:
            entry["hours"] = HOURS[name]
        if name in COUPLE:
            entry["couple"] = COUPLE[name]
        if name in ("SingleThread", "The French Laundry"):
            entry["flag"] = "Michelin page shows identical daily hours; confirm on the restaurant site"
        if name == "Quince":
            entry["note"] = "Official page (read 24 Nov 2026) shows Tue–Sat dinner and Fri–Sat lunch; the earlier 5–8 PM Tuesday hours were replaced"
        out.append(m.group(1) + "{" + ",".join(f"{k}:{js(v)}" for k, v in entry.items()) + "},")
        done.add(name)
    missing = set(HOURS) - done
    if missing:
        sys.exit(f"entries not found in data.js: {sorted(missing)}")
    open("data.js", "w", encoding="utf-8").write("\n".join(out))
    print("updated", len(done), "entries")


if __name__ == "__main__":
    main()
