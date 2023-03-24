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

    db = MySQLdb.connect(
            username=argv[1],
            passwd=argv[2],
            database=argv[3],
            state_name=[argv4],
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
            for row in rows:
                print(row)

    cursor.close()
    db.close()
