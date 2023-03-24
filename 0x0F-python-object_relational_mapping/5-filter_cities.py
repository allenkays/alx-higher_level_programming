#!/usr/bin/env python3
"""
This script takes in the name of a state and returns all cities in it
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    '''
    database connection
    '''
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    # connect to MySQL server on localhost
    db = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            database=db_name,
            host="localhost",
            port=3306
            )
    # create a cursor to execute MySQL queries on objects
    with db.cursor() as cursor:
        cursor.execute("""
                SELECT
                    cities.id, cities.name, states.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                WHERE
                    states.name = %s
                ORDER BY
                    cities.id ASC""", (state_name,))

        rows = cursor.fetchall()

        if rows is not None:
            print(", ".joim([row[1] for row in rows]))

    cursor.close()
    db.close()
