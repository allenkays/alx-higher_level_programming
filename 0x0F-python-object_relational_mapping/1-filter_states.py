#!/usr/bin/python3
"""
This script list all the states whose names start with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # connect to MySQL server running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )
    # create a cursor to execute mysql querries
    cur = db.cursor()

    # Execute SQL query to retrieve all states from hbtn_0e_0_usa
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY state.id ASC")

    # Fetch all entries from table states with name starting with N
    rows = cur.fetchall()

    # Display results in the same format as example
    for row in rows:
        print(row)

    # close db connection.
    db.close()
