#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} <username> <password> <database>'.format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306
                )
    except Exception as e:
        print('Error connecting to MySQL server:', e)
        sys.exit(1)

    # Execute query
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cities ORDER BY id ASC')

    # Fetch results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
