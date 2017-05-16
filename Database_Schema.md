Achtung: Dies ist eine Skizze! Die Implementierung weicht hiervon ab und ist nicht vollständig.

## election_type

	ID   Typ
	---- -----------------------
	ltw  landtagswahl
	eup  europäisches parlament
	btw  bundestag


## election

	ID        Jahr   Typ
	--------- ------ ----
	ltw-2000  2000   ltw
	ltw-2005  2005   ltw
	ltw-2010  2010   ltw
	ltw-2012  2012   ltw


## party

	ID      Name
	------- -----------
	GRUEN   Bündnis 90/Die Grünen


## district

  Election  Number  Name      Voters
  --------- ------- --------- ---------
  ltw-2012  1       Aachen I      86552


## district_shape

  Election  Number  Shape
  --------- ------- -----
  ltw-2012  1       ...


## district_result

  Election  District Number  Voted    Votes primary valid  Votes primary invalid  Votes secondary valid  Votes secondary invalid
  --------- ---------------- ------- -------------------- ---------------------- ----------------------- -----------------------
  ltw-2012  1                  55999                55306                    693                  55431                      568


## party_result

  Election  District Number  Party    Votes primary  Votes secondary
  --------- ---------------- -------- -------------- ----------------
  ltw-2012  1                   GRUEN           7382            10794
