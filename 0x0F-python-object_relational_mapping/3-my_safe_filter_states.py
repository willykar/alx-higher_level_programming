#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    usr_input = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (usr_input, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
