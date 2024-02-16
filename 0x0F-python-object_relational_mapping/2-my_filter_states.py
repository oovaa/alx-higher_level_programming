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
    to_search = sys.argv[4]

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            to_search))
    rows = cur.fetchall()
    for r in rows:
        print(r)

    # Close the connection
    cur.close()
    db.close()
