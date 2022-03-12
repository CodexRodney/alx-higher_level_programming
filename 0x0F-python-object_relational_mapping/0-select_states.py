#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def main():
    """
    The main fuction where everything runs from
    """
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    sql = ("SELECT * FROM states ORDER BY id")
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        print(x)


if __name__ == "__main__":
    main()
