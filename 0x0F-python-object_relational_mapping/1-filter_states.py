from sys import argv
import MySQLdb


def main():
    """
    runs as the main fuction
    """
    db = MySQLdb.connect(host=argv[2], passwd=argv[3], db=argv[4])
    sql = "SELECT name FROM states WHERE name = \"N*\" ORDER BY id ASC;"
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        print(x)


if __name__ == "__main__":
    main()
