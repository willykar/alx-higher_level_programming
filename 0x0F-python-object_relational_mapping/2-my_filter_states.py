#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{sys.argv[4]}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
