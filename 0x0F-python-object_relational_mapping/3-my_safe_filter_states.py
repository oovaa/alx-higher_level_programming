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
    searched = sys.argv[4]
    print(searched)

    cur = db.cursor()

    # Use parameterized query
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (searched,))

    rows = cur.fetchall()
    for r in rows:
        print(r)
