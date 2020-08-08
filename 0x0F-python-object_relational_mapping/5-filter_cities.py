#!/usr/bin/env python3
# Write a script that takes in the name of a state as an argument and
# lists all cities of that state, using the database hbtn_0e_4_usa

import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_Name = sys.argv[3]
    state_Name = sys.argv[4]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=db_Name
)
cur = db.cursor()
cur.execute("SELECT cities.name "
            "FROM cities INNER JOIN states "
            "ON states.id = cities.state_id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC;", (state_Name,))
rows = cur.fetchall()

print(", ".join([row[0] for row in rows]))

cur.close()
db.close()
