#!/usr/bin/python3

"""
Takes an argument and displays all values in the states
matching the argument
"""
from sys import argv
import MySQLdb


def main():
    """
    runs as the main fuction
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    sql = ("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
           .format(argv[4]))
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        print(x)


if __name__ == "__main__":
    main()
