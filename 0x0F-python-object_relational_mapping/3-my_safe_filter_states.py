#!/usr/bin/python3
"""
This script mitigates against sql injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to db with creds provided by user
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3]
            )

    # Create a cursor object to run SQL queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states from given databese
    cursor.execute("SELECT * FROM states \
            WHERE name=%s \
            ORDER BY states.id ASC", (argv[4], ))

    # Fetch all rows meeting criteria
    rows = cursor.fetchall()

    # Display fetched output
    for row in rows:
        print(row)

    # close connection to MySQL server
    db.close()
