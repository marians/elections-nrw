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

## Rohdaten

Im Verzeichnis `data/` sind (leicht modifizierte) Kopien der Wahlergebnisse (Quelle: [MIK NRW](https://www.wahlergebnisse.nrw.de/)) enthalten.

Mit dem Script `data/get_data.sh` kann nachvollzogen werden, wie diese Dateien erstellt wurden. Durch erneutes Ausführen können evtl. Aktualisierungen der Daten heruntergeladen werden.
