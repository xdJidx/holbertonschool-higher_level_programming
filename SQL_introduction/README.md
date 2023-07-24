# SQL - Introduction

## Tasks

0. List databases<br>
Write a script that lists all databases of your MySQL server.
```
-- script that lists all databases of your MySQL server.
SHOW DATABASES
```
use in your terminal this line
```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

1. Create a database<br>
Creates the database hbtn_0c_0 in your MySQL server.
```
-- script that creates the database hbtn_0c_0 in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0c_0
```
use in your terminal this line
```
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

2. Delete a database<br>
Deletes the database hbtn_0c_0 in your MySQL server.
```
-- script that deletes the database hbtn_0c_0 in your MySQL server.
DROP DATABASE IF EXISTS hbtn_0c_0
```
use in your terminal this line
```
cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
```

3. List tables<br>
Lists all the tables of a database in your MySQL server.
```
-- script that lists all the tables of a database in your MySQL server.
SHOW TABLES
```
use in your terminal this line
```
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

4. First table<br>
Write a script that creates a table called first_table in the current database in your MySQL server.
- first_table description:
- id INT
- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table first_table already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements
```
-- script that creates a table called first_table
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256))
```
use in your terminal this line
```
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

5. Full description<br>
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
- The database name will be passed as an argument of the mysql command
- You are not allowed to use the DESCRIBE or EXPLAIN statements
```
-- script that prints the full description of the table first_table from the database hbtn_0c_0
SHOW CREATE TABLE first_table
```
use in your terminal this line
```
cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

6. List all in table<br>
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
- All fields should be printed
- The database name will be passed as an argument of the mysql command
```
-- script that lists all rows of the table first_table from the database hbtn_0c_0
SELECT * FROM first_table
```
use in your terminal this line
```
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
