"""Apply the 27 official Michelin one-star page reads (2026-11-25) to data.js.

Only the one-star rows (type:"star", stars:1) are rewritten. Each row keeps its
existing source, social and socialSource fields. Fields the official page did not
show (phone for Sun Moon Studio and Naides) are left out, not inferred.
Source of values: data/michelin_onestar_reads_2026-11-25.json.
"""
import json, re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
READS = ROOT / "data" / "michelin_onestar_reads_2026-11-25.json"
DATA = ROOT / "data.js"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
C = "Closed"

def hrs(**kw):
    # kw keys are day names; values are the verified Michelin text
    return {d: kw[d] for d in DAYS}

def same(v, days):
    return {d: v for d in days}

HOURS = {
    "Auro": hrs(Mon=C, Tue=C, Wed="5–9 PM", Thu="5–9 PM", Fri="5–9 PM", Sat="5–9 PM", Sun=C),
    "Cyrus": hrs(Mon=C, Tue=C, Wed=C, Thu="5–9 PM", Fri="5–9 PM", Sat="5–9 PM", Sun="5–9 PM"),
    "Troubadour": hrs(Mon=C, Tue=C, Wed=C, Thu="5:30–8:30 PM", Fri="5:30–8:30 PM", Sat="5:30–8:30 PM", Sun="5:30–8:30 PM"),
    "Auberge du Soleil": {d: "11:30 AM–2:15 PM; 5:30–9 PM" for d in DAYS},
    "Press": hrs(Mon="5–9 PM", Tue="5–9 PM", Wed="5–9 PM", Thu="5–9 PM", Fri="5–10 PM", Sat="5–10 PM", Sun="5–9 PM"),
    "Madcap": hrs(Mon=C, Tue="5:30–8:30 PM", Wed="5:30–8:30 PM", Thu="5:30–8:30 PM", Fri="5:30–9 PM", Sat="5:30–9 PM", Sun=C),
    "Sun Moon Studio": hrs(Mon=C, Tue=C, Wed=C, Thu="5–9 PM", Fri="5–9 PM", Sat="5–9 PM", Sun="5–8 PM"),
    "Selby's": same("5–9 PM", DAYS),
    "Protégé": hrs(Mon=C, Tue="5–9:15 PM", Wed="5–9:15 PM", Thu="5–9:15 PM", Fri="5–9:15 PM", Sat="5–9:15 PM", Sun=C),
    "Wakuriya": hrs(Mon=C, Tue=C, Wed="6:30–9:30 PM", Thu="6:30–9:30 PM", Fri="6:30–9:30 PM", Sat="6–9 PM", Sun="6–9 PM"),
    "The Village Pub": hrs(Mon="5–9 PM", Tue="5–9 PM", Wed="5–9 PM", Thu="5–9 PM", Fri="11:30 AM–2:30 PM; 5–9 PM", Sat="11 AM–2 PM; 5–9 PM", Sun="11 AM–2 PM; 5–9 PM"),
    "Plumed Horse": hrs(Mon=C, Tue="5–10 PM", Wed="5–10 PM", Thu="5–10 PM", Fri="5–10 PM", Sat="5–10 PM", Sun="5–10 PM"),
    "7 Adams": hrs(Mon="5:30–9 PM", Tue="5:30–9 PM", Wed="5:30–9 PM", Thu="5:30–9 PM", Fri="5–10 PM", Sat="5–10 PM", Sun="5–9 PM"),
    "Angler SF": hrs(Mon="5–9 PM", Tue="11:30 AM–2 PM; 5–9 PM", Wed="11:30 AM–2 PM; 5–9 PM", Thu="11:30 AM–2 PM; 5–9 PM", Fri="11:30 AM–2 PM; 5–9 PM", Sat="11:30 AM–2 PM; 5–9 PM", Sun="5–9 PM"),
    "Hilda and Jesse": hrs(Mon="5:30–9 PM", Tue=C, Wed=C, Thu="5:30–9 PM", Fri="5:30–9 PM", Sat="10 AM–2 PM", Sun="10 AM–2 PM"),
    "Kin Khao": hrs(Mon="11:30 AM–2 PM; 5:30–9 PM", Tue="11:30 AM–2 PM; 5:30–9 PM", Wed="11:30 AM–2 PM; 5:30–9 PM", Thu="11:30 AM–2 PM; 5:30–9 PM", Fri="11:30 AM–2 PM; 5:30–10 PM", Sat="11:30 AM–2 PM; 5:30–10 PM", Sun="11:30 AM–2 PM; 5:30–9 PM"),
    "Mister Jiu's": hrs(Mon=C, Tue="5–9 PM", Wed="5–9 PM", Thu="5–9 PM", Fri="5–9:30 PM", Sat="5–9:30 PM", Sun=C),
    "Naides": hrs(Mon=C, Tue=C, Wed=C, Thu="5:30–8:30 PM", Fri="5:30–8:30 PM", Sat="5:30–8:30 PM", Sun="5:30–8:30 PM"),
    "Nari": hrs(Mon="5:30–9 PM", Tue="5:30–9 PM", Wed="5:30–9 PM", Thu="5:30–9 PM", Fri="5:30–9:30 PM", Sat="5:30–9:30 PM", Sun="5:30–9 PM"),
    "Niku Steakhouse": hrs(Mon="5–9 PM", Tue="5–9 PM", Wed="5–9 PM", Thu="5–9 PM", Fri="5–10 PM", Sat="5–10 PM", Sun="5–9 PM"),
    "Nisei": hrs(Mon=C, Tue=C, Wed="5–9 PM", Thu="5–9 PM", Fri="5–9 PM", Sat="5–9 PM", Sun="5–9 PM"),
    "San Ho Won": hrs(Mon=C, Tue="5–10 PM", Wed="5–10 PM", Thu="5–10 PM", Fri="5–10 PM", Sat="4:30–10 PM", Sun="4:30–10 PM"),
    "Sorrel": hrs(Mon=C, Tue=C, Wed="5–9 PM", Thu="5–9 PM", Fri="5–9 PM", Sat="5–9 PM", Sun="5–9 PM"),
    "Ssal": hrs(Mon=C, Tue=C, Wed="5:30–8:30 PM", Thu="5:30–8:30 PM", Fri="5:30–8:30 PM", Sat="5:30–8:30 PM", Sun="5:30–8:30 PM"),
    "State Bird Provisions": hrs(Mon="5:30–10 PM", Tue="5:30–10 PM", Wed="5:30–10 PM", Thu="5:30–10 PM", Fri=C, Sat="5:30–10:30 PM", Sun="5:30–10 PM"),
    "The Progress": same("5:30–10 PM", DAYS),
    "Wolfsbane": hrs(Mon=C, Tue="5:30–10 PM", Wed="5:30–10 PM", Thu="5:30–10 PM", Fri="5:30–10 PM", Sat="5:30–10 PM", Sun=C),
}

def js_value(v):
    if isinstance(v, dict):
        inner = ",".join(f"{k}:{js_value(x)}" if re.fullmatch(r"[A-Za-z_]\w*", k) else f"{json.dumps(k, ensure_ascii=False)}:{js_value(x)}" for k, x in v.items())
        return "{" + inner + "}"
    if isinstance(v, bool) or v is None:
        return json.dumps(v)
    if isinstance(v, (int, float)):
        return str(v)
    return json.dumps(v, ensure_ascii=False)

def main():
    reads = json.loads(READS.read_text(encoding="utf-8"))["records"]
    assert set(reads) == set(HOURS), (set(reads) ^ set(HOURS))
    # Read the current restaurant rows with node so the existing field values are exact.
    node = subprocess.run(["node", "-e", "const fs=require('fs');global.window={};eval(fs.readFileSync('data.js','utf8'));process.stdout.write(JSON.stringify(window.BAY_DATA.restaurants))"],
                          cwd=ROOT, capture_output=True, text=True, check=True)
    existing = {r["name"]: r for r in json.loads(node.stdout) if r.get("type") == "star" and r.get("stars") == 1}
    assert set(existing) == set(reads), (set(existing) ^ set(reads))

    lines = DATA.read_text(encoding="utf-8").split("\n")
    changed = 0
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)\{name:"((?:[^"\\]|\\.)*)"', line)
        if not m or 'type:"star",stars:1' not in line:
            continue
        name = m.group(2)
        if name not in reads:
            continue
        rec = reads[name]
        old = existing[name]
        new = {
            "name": old["name"], "city": old["city"], "area": old["area"], "type": "star", "stars": 1,
            "address": rec["address"], "cuisine": rec["cuisine"], "price": rec["price"],
            "website": rec["website"],
        }
        if rec.get("phone") and not rec["phone"].startswith("not on"):
            new["phone"] = rec["phone"]
        new["source"] = old["source"]
        flag = rec.get("flag")
        note = "2026-11-25 (official Michelin page: address, cuisine, price, website, phone, weekly schedule)"
        if rec.get("phone", "").startswith("not on"):
            note += "; phone not shown on the official page, left blank"
        if flag:
            note += "; FLAG: " + flag
        new["verified"] = note
        new["hours"] = HOURS[name]
        for k in ("social", "socialSource", "website"):
            pass
        if "social" in old:
            new["social"] = old["social"]
        if "socialSource" in old:
            new["socialSource"] = old["socialSource"]
        # keep the existing website if the official page gave none
        lines[i] = m.group(1) + "{" + ",".join(f"{k}:{js_value(v)}" for k, v in new.items()) + "},"
        changed += 1
    assert changed == 27, changed
    DATA.write_text("\n".join(lines), encoding="utf-8")
    print("rewrote", changed, "one-star rows")

if __name__ == "__main__":
    main()
