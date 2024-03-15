#!/usr/bin/python3
'''lists all states from the database'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    usr_input = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                states.id=cities.state_idWHERE states.name=%s""",
                (usr_input, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
