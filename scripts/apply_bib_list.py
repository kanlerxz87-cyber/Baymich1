#!/usr/bin/env python3
"""Replace the 8 sample Bib Gourmand lines in data.js with the full 30-entry list in
data/bibgourmand.json (official Michelin 'San Francisco and surroundings' Bib Gourmand filter).
Count (30) and the first three names were re-read on the official page on 2026-11-24;
the remaining names/cities/cuisines are carried from the earlier verification (COORDINATION T10)
and are flagged as such in each row. Area labels are derived from city names (geography, not a Michelin field).
"""
import json, re

AREA = {"San Francisco": "San Francisco", "Oakland": "East Bay", "Berkeley": "East Bay", "Alameda": "East Bay",
        "El Cerrito": "East Bay", "San Leandro": "East Bay", "Mill Valley": "Marin", "San Anselmo": "Marin",
        "Fairfax": "Marin", "San Mateo": "Peninsula & South Bay"}

def js(v):
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'

def main():
    rows = json.load(open("data/bibgourmand.json", encoding="utf-8"))["restaurants"]
    assert len(rows) == 30, len(rows)
    new = []
    for i, r in enumerate(rows):
        parts = [f'name:{js(r["name"])}', f'city:{js(r["city"])}', f'area:{js(AREA.get(r["city"], "Other"))}',
                 'type:"bib"', f'cuisine:{js(r["cuisine"])}', f'price:{js(r["michelinPriceBracket"])}',
                 f'source:{js(r["michelinLink"])}',
                 'verified:"Official Michelin Bib Gourmand list (count and first three names read 24 Nov 2026); other fields carried from T10"']
        new.append("    {" + ",".join(parts) + "}" + ("," if i < len(rows) - 1 else ""))
    src = open("data.js", encoding="utf-8").read().split("\n")
    out, inserted = [], False
    for line in src:
        if re.match(r'^\s*\{name:"[^"]+",city:"[^"]+",area:"[^"]+",type:"bib"', line):
            if not inserted:
                out.extend(new); inserted = True
            continue
        out.append(line)
    if not inserted:
        raise SystemExit("no bib lines found")
    # ensure the entry before the first bib line (the last star line) ends with a comma
    text = "\n".join(out)
    text = re.sub(r'\}\n(    \{name:"[^"]+",city:"[^"]+",area:"[^"]+",type:"bib")', r'},\n\1', text)
    open("data.js", "w", encoding="utf-8").write(text)
    print("bib entries written:", len(rows))

if __name__ == "__main__":
    main()
