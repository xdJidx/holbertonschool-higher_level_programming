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
