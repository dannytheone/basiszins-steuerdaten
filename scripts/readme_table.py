"""Schreibt die Basiszins-Tabelle aus data/basiszins.csv zwischen die Marker in README.md."""
import csv, re, pathlib

rows = list(csv.DictReader(open("data/basiszins.csv", encoding="utf-8")))
lines = ["| Jahr | Basiszins | BMF-Schreiben | Vorabpauschale |", "|---:|---:|---|---|"]
for r in rows:
    pct = r["basiszins_prozent"].replace(".", ",")
    lines.append(f"| {r['jahr']} | {pct} % | {r['bmf_schreiben']} | {r['vorabpauschale_faellt_an']} |")
p = pathlib.Path("README.md")
s = p.read_text(encoding="utf-8")
s = re.sub(r"(<!-- tabelle:start -->\n)(?:.*?\n)?(<!-- tabelle:ende -->)", lambda m: m.group(1) + "\n".join(lines) + "\n" + m.group(2), s, flags=re.S)
p.write_text(s, encoding="utf-8")
