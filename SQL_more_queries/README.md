# SQL - More queries

## Tasks

### Se connecter à mysql
Dans votre terminal, ecrivez :
```
mysql -h localhost -u root -p
```
Si jamais il y a un soucis sur les privilèges, utilisé "sudo" devant :
```
sudo mysql -h localhost -u root -p
```

0. My privileges!<br>
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
```
-- script that lists all privileges of the MySQL users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
```
Use in your terminal this line
```
echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

1. Root user<br>
Write a script that creates the MySQL server user user_0d_1.
- user_0d_1 should have all privileges on your MySQL server
- The user_0d_1 password should be set to user_0d_1_pwd
- If the user user_0d_1 already exists, your script should not fail
```
-- script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
```
Use in your terminal this line
```
cat 1-create_user.sql | mysql -hlocalhost -uroot -p
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```
