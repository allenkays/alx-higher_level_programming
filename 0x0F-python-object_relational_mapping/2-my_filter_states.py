#!/usr/bin/python3
"""
This script displays all the values in a table states,
based on user input
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    # connect to MySQL server running on port 3306 on localhost
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3]
            )

    # cursor to execute sql queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states input by user.
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    # Display the query output
    for row in rows:
        print(row)

    # close database connection
    db.close()
