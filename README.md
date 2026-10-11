# Basiszins und Steuerdaten für Kapitalerträge in Deutschland

Offene Daten zur Vorabpauschale und Besteuerung von Kapitalerträgen im Privatvermögen, als CSV und JSON, maschinenlesbar und unter **CC BY 4.0** frei nutzbar.

- **Basiszins** zur Berechnung der Vorabpauschale (§ 18 Abs. 4 InvStG) seit 2018, mit Datum des BMF-Schreibens
- **Steuerparameter:** Abgeltungsteuer, Solidaritätszuschlag, effektive Belastung mit Kirchensteuer (8 % und 9 %), Sparerpauschbetrag, Teilfreistellungssätze für Aktien-, Misch- und Immobilienfonds

Die Daten werden wöchentlich automatisch aus der offenen Schnittstelle von [Planafolio](https://planafolio.com/basiszins) aktualisiert.

## Basiszins

<!-- tabelle:start -->
| Jahr | Basiszins | BMF-Schreiben | Vorabpauschale |
|---:|---:|---|---|
| 2018 | 0,87 % | 2018-01-04 | ja |
| 2019 | 0,52 % | 2019-01-09 | ja |
| 2020 | 0,07 % | 2020-01-29 | ja |
| 2021 | -0,45 % | 2021-01-06 | nein |
| 2022 | -0,05 % | 2022-01-07 | nein |
| 2023 | 2,55 % | 2023-01-04 | ja |
| 2024 | 2,29 % | 2024-01-05 | ja |
| 2025 | 2,53 % | 2025-01-10 | ja |
| 2026 | 3,20 % | 2026-01-13 | ja |
<!-- tabelle:ende -->

Bei negativem Basiszins fällt keine Vorabpauschale an. Erklärung und Rechenweg: [planafolio.com/basiszins](https://planafolio.com/basiszins), selbst rechnen mit dem [Vorabpauschale-Rechner](https://planafolio.com/vorabpauschale-rechner).

## Dateien

| Datei | Inhalt |
|---|---|
| [`data/basiszins.csv`](data/basiszins.csv) · [`.json`](data/basiszins.json) | Basiszins je Jahr |
| [`data/kapitalertragsteuer.csv`](data/kapitalertragsteuer.csv) · [`.json`](data/kapitalertragsteuer.json) | Steuersätze, Freibeträge, Teilfreistellung mit Rechtsgrundlage und Gültigkeit |
| [`datapackage.json`](datapackage.json) | Beschreibung im [Frictionless-Data-Format](https://specs.frictionlessdata.io/data-package/) |

Anteile stehen als Dezimalzahl (`0.25` = 25 %). In `kapitalertragsteuer.csv` bedeutet die Variante `bavariaBw` Kirchensteuer 8 % (Bayern, Baden-Württemberg), `other` Kirchensteuer 9 %, `none` ohne Kirchensteuer.

### Direkt abrufen

```
https://planafolio.com/api/open-data/basiszins
https://planafolio.com/api/open-data/basiszins/csv
https://planafolio.com/api/open-data/kapitalertragsteuer
https://planafolio.com/api/open-data/kapitalertragsteuer/csv
```

Ohne Schlüssel, mit offenem CORS. Für JavaScript/TypeScript gibt es die Rechenlogik als npm-Paket [`investsteuer`](https://www.npmjs.com/package/investsteuer).

## Lizenz und Quellenangabe

[CC BY 4.0](LICENSE). Bitte als Quelle angeben:

> Planafolio ([planafolio.com/basiszins](https://planafolio.com/basiszins)), CC BY 4.0

Die Daten sind sorgfältig gegen die BMF-Schreiben und Gesetzestexte geprüft, aber keine Steuerberatung.

---

## English

Open data on Germany's *Basiszins* (base rate for the *Vorabpauschale*, the advance lump-sum tax on accumulating funds, § 18 InvStG) since 2018, plus capital gains tax parameters (flat tax, solidarity surcharge, church tax, saver's allowance, partial exemption rates). CSV and JSON, updated weekly from [planafolio.com](https://planafolio.com/basiszins), licensed CC BY 4.0. Please credit "Planafolio (planafolio.com/basiszins)".
