#!/usr/bin/env python3
"""Inject Michelin-verified hours objects into data.js Bib Gourmand records (root dashboard)."""
import json
import re

HOURS = {
    "A16": {"Mon": "5:00–9:30 pm", "Tue": "5:00–9:30 pm", "Wed": "5:00–9:30 pm", "Thu": "5:00–9:30 pm", "Fri": "12:00–10:00 pm", "Sat": "12:00–10:00 pm", "Sun": "12:00–9:30 pm"},
    "Bansang": {"Mon": "Closed", "Tue": "Closed", "Wed": "5:30–8:30 pm", "Thu": "5:30–8:30 pm", "Fri": "5:30–9:00 pm", "Sat": "5:30–9:00 pm", "Sun": "5:30–8:30 pm"},
    "Dumpling Home": {"Mon": "11:30 am–2:15 pm · 5:00–8:15 pm", "Tue": "11:30 am–2:15 pm · 5:00–8:15 pm", "Wed": "11:30 am–2:15 pm · 5:00–8:15 pm", "Thu": "11:30 am–2:15 pm · 5:00–8:15 pm", "Fri": "11:30 am–2:15 pm · 5:00–8:45 pm", "Sat": "11:30 am–2:15 pm · 5:00–8:45 pm", "Sun": "11:30 am–2:15 pm · 5:00–8:15 pm"},
    "FOB Kitchen": {"Mon": "Closed", "Tue": "9:00 am–2:00 pm", "Wed": "11:00 am–9:00 pm", "Thu": "11:00 am–9:00 pm", "Fri": "11:00 am–9:00 pm", "Sat": "11:00 am–9:00 pm", "Sun": "11:00 am–9:00 pm"},
    "Soba Ichi": {"Mon": "5:00–9:00 pm", "Tue": "Closed", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:00 pm", "Sat": "5:00–9:00 pm", "Sun": "5:00–9:00 pm"},
    "MAMA Oakland": {"Mon": "5:00–9:00 pm", "Tue": "5:00–9:00 pm", "Wed": "5:00–9:00 pm", "Thu": "5:00–9:00 pm", "Fri": "5:00–9:30 pm", "Sat": "5:00–9:30 pm", "Sun": "5:00–9:00 pm"},
}

path = "data.js"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

out = []
injected = 0
for line in lines:
    m = re.search(r'\{name:"([^"]+)",city:"[^"]+",area:"[^"]+",type:"bib"', line)
    if m and m.group(1) in HOURS and "hours:" not in line:
        name = m.group(1)
        hours_js = "hours:" + json.dumps(HOURS[name], ensure_ascii=False)
        stripped = line.rstrip("\n")
        idx = stripped.rfind("}")
        if idx != -1:
            stripped = stripped[:idx].rstrip() + ", " + hours_js + stripped[idx:]
            line = stripped + "\n"
            injected += 1
    out.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(out)

print(f"Injected hours into {injected} data.js Bib records")
