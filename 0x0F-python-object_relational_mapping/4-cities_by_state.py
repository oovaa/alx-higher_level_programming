#!/usr/bin/python3
"""a script that takes in an argument and displays 
all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, (SELECT name FROM state WHERE s.id = ) FROM cities")
    full_table = cur.fetchall()

    [print(x) for x in full_table]
