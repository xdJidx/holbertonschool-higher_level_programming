#!/usr/bin/python3
"""
Write a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Exécuter la requête pour récupérer l'État en fonction du nom fourni
    cursor.execute("SELECT * FROM `states` WHERE name=%s ORDER BY id ASC", (state_name,))
    [print(state) for state in cursor.fetchall()]

    cursor.close()
    db.close()
