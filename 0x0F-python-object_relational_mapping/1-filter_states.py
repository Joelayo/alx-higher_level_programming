#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv


    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
