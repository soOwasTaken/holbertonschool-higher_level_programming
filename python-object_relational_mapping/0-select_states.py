#!/usr/bin/python3
"""script that list all states from database x"""
import sys
import MySQLdb

if __name__ == '__name__':
    db = MySQLdb(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    result = cursor.fetchall()
    for row in result:
        print(row)