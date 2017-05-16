#!/bin/bash

# Landtag 2017
curl -s https://www.wahlergebnisse.nrw.de/landtagswahlen/2017/LW17_WK_insgesamt.txt \
  | tail -n +3 \
  > ltw_2017.csv

# Landtag 2012
curl -s https://www.wahlergebnisse.nrw.de/landtagswahlen/2012/txtdateien/a136lw1200.txt \
  | iconv -f iso-8859-1 -t utf-8 \
  > ltw_2012.csv

# Landtag 2010
curl -s https://www.wahlergebnisse.nrw.de/landtagswahlen/2010/aktuell/txtdateien/a136lw1000.txt \
  | iconv -f iso-8859-1 -t utf-8 \
  > ltw_2010.csv


# Ältere Wahlergebnisse liegen nicht getrennt nach Erst- und Zweitstimmen vor

# # Landtag 2005
# curl -s http://alt.wahlergebnisse.nrw.de/landtagswahlen/2005/lwahl/txtdateien/a135lw0500.txt \
#   | iconv -f iso-8859-1 -t utf-8 \
#   | tr -d "\r" \
#   > data/ltw_2005.csv
#
# # Landtag 2000
# curl -s http://alt.wahlergebnisse.nrw.de/landtagswahlen/2000/wahlkr/lw_gesamt1.txt \
#   | iconv -f iso-8859-1 -t utf-8 \
#   | tail -n +3 \
#   > data/ltw_2000.csv
