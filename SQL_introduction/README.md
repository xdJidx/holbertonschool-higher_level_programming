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

7. First add<br>
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
- New row:<br>
    id = 89<br>
    name = Best School<br>
- The database name will be passed as an argument of the mysql command
```
-- script that lists all rows of the table first_table from the database hbtn_0c_0
SELECT * FROM first_table
```
use in your terminal this line
```
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

8. Count 89<br>
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
- The database name will be passed as an argument of the mysql command
```
-- script that displays the number of records with id = 89 in the table first_table
SELECT COUNT(*) FROM first_table WHERE id = 89
```
use in your terminal this line
```
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
```

9. Full creation
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

- second_table description:<br>
    id INT<br>
    name VARCHAR(256)<br>
    score INT<br>
- The database name will be passed as an argument to the mysql command
- If the table second_table already exists, your script should not fail
- You are not allowed to use the SELECT and SHOW statements
- Your script should create these records:<br>
    id = 1, name = “John”, score = 10<br>
    id = 2, name = “Alex”, score = 3 <br>
    id = 3, name = “Bob”, score = 14<br>
    id = 4, name = “George”, score = 8<br>
```
-- cript that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
```
use in your terminal this line
```
cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

10. List by best<br>
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the mysql command
```
-- script that lists all records of the table second_table
SELECT score, name FROM second_table ORDER BY score DESC;
```
use in your terminal this line
```
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

11. Select the best<br>
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the mysql command
```
-- script that lists all records with a score >= 10 in the table second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
```
use in your terminal this line
```
cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

12. Cheating is bad<br>
Write a script that updates the score of Bob to 10 in the table second_table.
- You are not allowed to use Bob’s id value, only the name field
- The database name will be passed as an argument of the mysql command
```
-- script that updates the score of Bob to 10 in the table second_table.
UPDATE second_table SET score = 10 WHERE name = 'Bob'
```
use in your terminal this line
```
cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

13. Score too low<br>
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- The database name will be passed as an argument of the mysql command
```
-- script that removes all records with a score <= 5 in the table second_table
DELETE FROM second_table WHERE score <= 5;
```
use in your terminal this line
```
cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

14. Average<br>
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
- The result column name should be average
- The database name will be passed as an argument of the mysql command
```
-- script that computes the score average of all records in the table second_table
SELECT AVG(score) AS average FROM second_table;
```
use in your terminal this line
```
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

15. Number by score<br>
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
- The result should display:<br>
    the score<br>
    the number of records for this score with the label number
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the mysql command
```
-- script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
```
use in your terminal this line
```
cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

16. Say my name<br>
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
- Don’t list rows without a name value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the mysql command
```
-- script that lists all records of the table second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
```
use in your terminal this line
```
cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
