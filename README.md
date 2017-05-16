# elections-nrw

Importiert die Ergebnisse von Landtagswahlen in NRW in eine SQLlite-Datenbank und vereinfacht so die Auswertung mittels SQL.

## Script

Mit dem Importscript `import.py` werden die CSV-Dateien im Verzeichnis `data/` in die SQLlite-Datenbank `elections.sqlite` importiert.

Ausführung:

```nohighlight
python ./import.py
```

## Datenbank-Schema

TODO

## Beispiele

### Wahlberechtigte und Wähler

```sql
SELECT

d2010.district_number AS district_number,
d2010.name AS district_name,
d2010.voter AS voters_2010,
dr2010.voted AS voted_2010,
d2012.voter AS voters_2012,
dr2012.voted AS voted_2012,
d2017.voter AS voters_2017,
dr2017.voted AS voted_2017

FROM district d2010

LEFT JOIN district d2012 ON (d2010.district_number=d2012.district_number)
LEFT JOIN district d2017 ON (d2010.district_number=d2017.district_number)
LEFT JOIN district_result dr2010 ON (d2010.district_number=dr2010.district_number)
LEFT JOIN district_result dr2012 ON (d2010.district_number=dr2012.district_number)
LEFT JOIN district_result dr2017 ON (d2010.district_number=dr2017.district_number)

WHERE
d2010.election_id="ltw-2010"
AND d2012.election_id="ltw-2012"
AND d2017.election_id="ltw-2017"
AND dr2010.election_id="ltw-2010"
AND dr2012.election_id="ltw-2012"
AND dr2017.election_id="ltw-2017"
```

## Rohdaten

Im Verzeichnis `data/` sind (leicht modifizierte) Kopien der Wahlergebnisse (Quelle: [MIK NRW](https://www.wahlergebnisse.nrw.de/)) enthalten.

Mit dem Script `data/get_data.sh` kann nachvollzogen werden, wie diese Dateien erstellt wurden. Durch erneutes Ausführen können evtl. Aktualisierungen der Daten heruntergeladen werden.
