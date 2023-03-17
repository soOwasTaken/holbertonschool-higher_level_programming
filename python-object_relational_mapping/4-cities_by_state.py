#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    # create a cursor object
    cursor = db.cursor()

    # execute the SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    # fetch all the matching rows
    rows = cursor.fetchall()

    # display the rows
    for row in rows:
        print(row)

    # close the cursor and database connection
    cursor.close()
    db.close()