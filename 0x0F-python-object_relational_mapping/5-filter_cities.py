#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument 
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    state_name = sys.argv[4]

    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = '{}'".format(state_name))
    full_table = cur.fetchall()

    print(', '.join(x[0] for x in full_table))
