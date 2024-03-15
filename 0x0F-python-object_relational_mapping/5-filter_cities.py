#!/usr/bin/python3
'''lists all states from the database'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    usr_input = sys.argv[4]
    cur.execute("""SELECT cities.name FROM states INNER JOIN cities ON
                states.id=cities.state_id WHERE states.name = %s
                ORDER BY cities.id ASC""", (usr_input, ))
    data = cur.fetchall()
    print(", ".join([city[0] for city in data]))

    cur.close()
    db.close()
