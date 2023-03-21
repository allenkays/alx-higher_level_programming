#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states from hbtn_0e_0_usa database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # Display results in the same format as example
    for row in rows:
        print(row)

    # Close database connection
    db.close()
