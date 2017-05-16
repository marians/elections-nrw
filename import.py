# coding: utf-8

"""
Imports CSV files from the ./data foder
into an SQLite database
"""

import os
import sys
import csv
import sqlite3

# our data directory path
root = "./data"

# CSV delimiter
delimiter = ";"

# database file path
dbfile = "./elections.sqlite"


def read_csv(path):
    """
    Reads CSV file and returns data as lists of lists
    """
    rows = []
    with open(path, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for row in reader:
            rows.append(row)
    return rows


def process_rows(rowdata):
    """
    Reads raw data as list of lists and returns dict
    """
    headers = rowdata[0]

    # validate column assignment
    assert headers[0] == "Wahlkreisnr."
    assert headers[1] == "Wahlkreisname"
    assert headers[2] == "Wahlberechtigte insgesamt"
    assert headers[3] == "Wähler/-innen insgesamt" or headers[3] == "Wähler/-innen"
    assert headers[4] == "Ungültige Stimmen Erststimmen"
    assert headers[5] == "Ungültige Stimmen Zweitstimmen"
    assert headers[6] == "Gültige Stimmen Erststimmen"
    assert headers[7] == "Gültige Stimmen Zweitstimmen"

    district_results = []

    records = []
    for row in rowdata[1:]:
        district_number = int(row[0])
        if district_number == 0:
            continue

        record = {
            "district": {
                "number": district_number,
                "name": row[1].decode("utf-8"),
                "voters": int(row[2]),
            },
            "district_result": {
                "voted": int(row[3]),
                "first_votes_valid": int(row[6]),
                "second_votes_valid": int(row[7]),
                "first_votes_invalid": int(row[4]),
                "second_votes_invalid": int(row[5]),
            },
            "party_results": []
        }

        # parse party results
        i = 8  # first party result column index
        while i < len(headers):
            party1, suffix1 = headers[i].rsplit(None, 1)
            party2, suffix2 = headers[(i+1)].rsplit(None, 1)
            assert party1 == party2
            assert suffix1 == "Erststimmen"
            assert suffix2 == "Zweitstimmen"

            record["party_results"].append({
                "party": party1.decode("utf-8"),
                "first_votes": mint(row[i]),
                "second_votes": mint(row[(i+1)]),
            })
            i += 2

        records.append(record)
    return records


def mint(string):
    """
    Convert a numeric field into an int or None
    """
    if string == "-":
        return None
    if string == "":
        return None
    return int(string)


def dbimport(year, election_type, records):
    """
    Imports a list of records into databases
    """

    # add election
    election_id = "%s-%s" % (election_type, year)
    cursor.execute("INSERT INTO election VALUES (?, ?, ?)", (
        election_id, year, election_type,
    ))

    for r in records:

        # add district
        cursor.execute("INSERT INTO district VALUES (?, ?, ?, ?)", (
            election_id,
            r["district"]["number"],
            r["district"]["name"],
            r["district"]["voters"],
        ))

        # add district result
        cursor.execute("INSERT INTO district_result VALUES (?, ?, ?, ?, ?, ?, ?)", (
                election_id,
                r["district"]["number"],
                r["district_result"]["voted"],
                r["district_result"]["first_votes_valid"],
                r["district_result"]["second_votes_valid"],
                r["district_result"]["first_votes_invalid"],
                r["district_result"]["second_votes_invalid"],
        ))

        # add party results
        for pr in r["party_results"]:
            cursor.execute("INSERT INTO party_result VALUES (?, ?, ?, ?, ?)", (
                election_id,
                r["district"]["number"],
                pr["party"],
                pr["first_votes"],
                pr["second_votes"],
            ))

    conn.commit()


def create_tables():
    # elections table
    cursor.execute("DROP TABLE election")
    cursor.execute("DROP TABLE district")
    cursor.execute("DROP TABLE district_result")
    cursor.execute("DROP TABLE party_result")

    cursor.execute('''CREATE TABLE election
             (id text, year integer, type text)''')
    cursor.execute('''CREATE TABLE district
             (election_id text, district_number integer, name text, voter integer)''')
    cursor.execute('''CREATE TABLE district_result
             (election_id text, district_number integer, voted text,
             votes_primary_valid integer,
             votes_secondary_valid integer,
             votes_primary_invalid integer,
             votes_secondary_invalid integer)
             ''')
    cursor.execute('''CREATE TABLE party_result
             (election_id text, district_number integer, party text,
             votes_primary integer, votes_secondary integer)''')


if __name__ == "__main__":

    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    create_tables()
    conn.commit()

    for f in os.listdir(root):

        if not f.endswith(".csv"):
            continue

        # CSV file path
        path = os.path.join(root, f)

        # year from file name 'xxxxx_YYYY.csv'
        (election_type, year) = f.split(".")[0].split("_")
        year = int(year)

        # CSV file content
        rows = read_csv(path)

        print("Read %d rows for election type %s for year %d" % (len(rows), election_type, year))

        records = process_rows(rows)
        print("Processed %d datasets" % len(records))

        dbimport(year=year, election_type=election_type, records=records)

    conn.close()
