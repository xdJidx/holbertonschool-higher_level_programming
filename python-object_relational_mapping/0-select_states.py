#!/usr/bin/env python3
import MySQLdb
import sys


def list_states(username, password, database):
    try:
        # Connect to MySQL server running on localhost at standard port 3306
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=username, passwd=password,
                                     db=database)

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to retrieve
        # all distinct states sorted by id in ascending order
        cursor.execute("SELECT DISTINCT * FROM states ORDER BY id ASC;")

        # Fetch all rows from the result set
        states = cursor.fetchall()

        # Display the results as specified in the example
        for state in states:
            state_id, state_name = state
            print(state)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username>"
              + " <mysql_password> <database_name>")
        sys.exit(1)

    # Get the arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, database_name)
