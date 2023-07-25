# SQL - More queries

## Tasks

### Se connecter à mysql
Dans votre terminal, ecrivez :
```
mysql -h localhost -u root -p
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


