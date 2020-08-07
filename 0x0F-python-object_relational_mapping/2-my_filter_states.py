#!/usr/bin/python3
"""list all states where name matches arg"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    state = argv[4]
    cur = conn.cursor()
    q = """ SELECT * FROM states ORDER BY states.id ASC """
    cur.execute(q)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state:
            print(row)
    cur.close()
    conn.close()
