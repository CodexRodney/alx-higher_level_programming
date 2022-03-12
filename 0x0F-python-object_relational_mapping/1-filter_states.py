#!/usr/bin/python3

"""
lists all states with a name satrting with N from a database
"""
from sys import argv
import MySQLdb


def main():
    """
    runs as the main fuction
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    sql = "SELECT * FROM states WHERE BINARY name LIKE 'N%'  ORDER BY id ASC"
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        print(x)


if __name__ == "__main__":
    main()
