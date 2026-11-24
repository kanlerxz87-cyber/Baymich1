#!/usr/bin/env python3
"""Inject Michelin-verified hours objects into data.js restaurant records (root dashboard).

Only the 29 SF-region starred restaurants verified from guide.michelin.com on 2026-11-24
are touched. Records without an official-source hours object are left unchanged.
"""
import json
import re

# name -> {Mon..Sun} from the official Michelin profile (2026-11-24)
HOURS = {
    "Quince": {"Mon": "Closed", "Tue": "5:00–9:00 pm", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "11:30 am–1:00 pm · 5:00–9:00 pm", "Sat": "11:30 am–1:00 pm · 5:00–9:00 pm", "Sun": "Closed"},
    "Californios": {"Mon": "Closed", "Tue": "5:00–10:00 pm", "Wed": "5:00–10:00 pm", "Thu": "5:00–10:00 pm", "Fri": "5:00–10:00 pm", "Sat": "5:00–10:00 pm", "Sun": "Closed"},
    "Benu": {"Mon": "Closed", "Tue": "Closed", "Wed": "5:00–8:00 pm", "Thu": "5:00–8:00 pm", "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm", "Sun": "Closed"},
    "Atelier Crenn": {"Mon": "Closed", "Tue": "4:45–8:45 pm", "Wed": "4:45–8:45 pm", "Thu": "4:45–8:45 pm", "Fri": "4:45–8:45 pm", "Sat": "4:45–8:45 pm", "Sun": "Closed"},
    "Acquerello": {"Mon": "Closed", "Tue": "5:30–9:45 pm", "Wed": "5:30–9:45 pm", "Thu": "5:30–9:45 pm", "Fri": "5:30–9:45 pm", "Sat": "5:30–9:45 pm", "Sun": "Closed"},
    "Kiln": {"Mon": "Closed", "Tue": "6:00–8:00 pm", "Wed": "6:00–8:00 pm", "Thu": "6:00–8:00 pm", "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm", "Sun": "Closed"},
    "Lazy Bear": {"Mon": "Closed", "Tue": "5:00–11:00 pm", "Wed": "5:00–11:00 pm", "Thu": "5:00–11:00 pm", "Fri": "5:00–11:00 pm", "Sat": "5:00–11:00 pm", "Sun": "Closed"},
    "Saison": {"Mon": "Closed", "Tue": "5:00–9:30 pm", "Wed": "5:00–9:30 pm", "Thu": "5:00–9:30 pm", "Fri": "5:00–9:30 pm", "Sat": "5:00–9:30 pm", "Sun": "Closed"},
    "Sons & Daughters": {"Mon": "Closed", "Tue": "5:30–8:30 pm", "Wed": "5:30–8:30 pm", "Thu": "5:30–8:30 pm", "Fri": "5:30–8:30 pm", "Sat": "5:30–8:30 pm", "Sun": "Closed"},
    "Birdsong": {"Mon": "Closed", "Tue": "5:30–8:00 pm", "Wed": "5:30–8:00 pm", "Thu": "5:30–8:00 pm", "Fri": "5:00–8:30 pm", "Sat": "5:00–8:30 pm", "Sun": "Closed"},
    "Commis": {"Mon": "Closed", "Tue": "5:00–9:30 pm", "Wed": "5:00–9:30 pm", "Thu": "5:00–9:30 pm", "Fri": "5:00–9:30 pm", "Sat": "5:00–9:30 pm", "Sun": "Closed"},
    "Niku Steakhouse": {"Mon": "5:00–9:00 pm", "Tue": "5:00–9:00 pm", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–10:00 pm", "Sat": "5:00–10:00 pm", "Sun": "5:00–9:00 pm"},
    "Wolfsbane": {"Mon": "Closed", "Tue": "5:30–10:00 pm", "Wed": "5:30–10:00 pm", "Thu": "5:30–10:00 pm", "Fri": "5:30–10:00 pm", "Sat": "5:30–10:00 pm", "Sun": "Closed"},
    "San Ho Won": {"Mon": "Closed", "Tue": "5:00–10:00 pm", "Wed": "5:00–10:00 pm", "Thu": "5:00–10:00 pm", "Fri": "5:00–10:00 pm", "Sat": "4:30–10:00 pm", "Sun": "4:30–10:00 pm"},
    "Ssal": {"Mon": "Closed", "Tue": "Closed", "Wed": "5:30–8:30 pm", "Thu": "5:30–8:30 pm", "Fri": "5:30–8:30 pm", "Sat": "5:30–8:30 pm", "Sun": "5:30–8:30 pm"},
    "State Bird Provisions": {"Mon": "5:30–10:00 pm", "Tue": "5:30–10:00 pm", "Wed": "5:30–10:00 pm", "Thu": "5:30–10:00 pm", "Fri": "Closed", "Sat": "5:30–10:30 pm", "Sun": "5:30–10:00 pm"},
    "Hilda and Jesse": {"Mon": "5:30–9:00 pm", "Tue": "Closed", "Wed": "Closed", "Thu": "5:30–9:00 pm", "Fri": "5:30–9:00 pm", "Sat": "10:00 am–2:00 pm", "Sun": "10:00 am–2:00 pm"},
    "Nisei": {"Mon": "Closed", "Tue": "Closed", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:00 pm", "Sat": "5:00–9:00 pm", "Sun": "5:00–9:00 pm"},
    "Naides": {"Mon": "Closed", "Tue": "Closed", "Wed": "Closed", "Thu": "5:30–8:30 pm", "Fri": "5:30–8:30 pm", "Sat": "5:30–8:30 pm", "Sun": "5:30–8:30 pm"},
    "Nari": {"Mon": "5:30–9:00 pm", "Tue": "5:30–9:00 pm", "Wed": "5:30–9:00 pm", "Thu": "5:30–9:00 pm", "Fri": "5:30–9:30 pm", "Sat": "5:30–9:30 pm", "Sun": "5:30–9:00 pm"},
    "Mister Jiu's": {"Mon": "Closed", "Tue": "5:00–9:00 pm", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:30 pm", "Sat": "5:00–9:30 pm", "Sun": "Closed"},
    "Angler SF": {"Mon": "5:00–9:00 pm", "Tue": "11:30 am–2:00 pm · 5:00–9:00 pm", "Wed": "11:30 am–2:00 pm · 5:00–9:00 pm", "Thu": "11:30 am–2:00 pm · 5:00–9:00 pm", "Fri": "11:30 am–2:00 pm · 5:00–9:00 pm", "Sat": "11:30 am–2:00 pm · 5:00–9:00 pm", "Sun": "5:00–9:00 pm"},
    "Kin Khao": {"Mon": "11:30 am–2:00 pm · 5:30–9:00 pm", "Tue": "11:30 am–2:00 pm · 5:30–9:00 pm", "Wed": "11:30 am–2:00 pm · 5:30–9:00 pm", "Thu": "11:30 am–2:00 pm · 5:30–9:00 pm", "Fri": "11:30 am–2:00 pm · 5:30–10:00 pm", "Sat": "11:30 am–2:00 pm · 5:30–10:00 pm", "Sun": "11:30 am–2:00 pm · 5:30–9:00 pm"},
    "7 Adams": {"Mon": "5:30–9:00 pm", "Tue": "5:30–9:00 pm", "Wed": "5:30–9:00 pm", "Thu": "5:30–9:00 pm", "Fri": "5:00–10:00 pm", "Sat": "5:00–10:00 pm", "Sun": "5:00–9:00 pm"},
    "Sorrel": {"Mon": "Closed", "Tue": "Closed", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:00 pm", "Sat": "5:00–9:00 pm", "Sun": "5:00–9:00 pm"},
    "The Progress": {"Mon": "5:30–10:00 pm", "Tue": "5:30–10:00 pm", "Wed": "5:30–10:00 pm", "Thu": "5:30–10:00 pm", "Fri": "5:30–10:00 pm", "Sat": "5:30–10:00 pm", "Sun": "5:30–10:00 pm"},
    "Sun Moon Studio": {"Mon": "Closed", "Tue": "Closed", "Wed": "Closed", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:00 pm", "Sat": "5:00–9:00 pm", "Sun": "5:00–8:00 pm"},
    "Madcap": {"Mon": "Closed", "Tue": "5:30–8:30 pm", "Wed": "5:30–8:30 pm", "Thu": "5:30–8:30 pm", "Fri": "5:30–9:00 pm", "Sat": "5:30–9:00 pm", "Sun": "Closed"},
    "Wakuriya": {"Mon": "Closed", "Tue": "Closed", "Wed": "6:30–9:30 pm", "Thu": "6:30–9:30 pm", "Fri": "6:30–9:30 pm", "Sat": "6:00–9:00 pm", "Sun": "6:00–9:00 pm"},
}

path = "data.js"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

out = []
injected = 0
for line in lines:
    m = re.search(r'\{name:"([^"]+)"', line)
    if m and m.group(1) in HOURS and "hours:" not in line:
        name = m.group(1)
        h = HOURS[name]
        hours_js = "hours:" + json.dumps(h, ensure_ascii=False).replace('"', '"')
        # insert before the final closing brace of this single-line record,
        # preserving anything that follows it (e.g. a trailing comma)
        stripped = line.rstrip("\n")
        idx = stripped.rfind("}")
        if idx != -1:
            stripped = stripped[:idx].rstrip() + ", " + hours_js + stripped[idx:]
            line = stripped + "\n"
            injected += 1
    out.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(out)

print(f"Injected hours into {injected} data.js records")
