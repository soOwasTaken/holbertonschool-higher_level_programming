#!/usr/bin/python3
"""
lists all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    # create a cursor object
    cursor = db.cursor()

    # execute the SQL query
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    # fetch all the rows
    rows = cursor.fetchall()

    # display the rows as a comma-separated list
    print(", ".join(row[0] for row in rows))

    # close the cursor and database connection
    cursor.close()
    db.close()
