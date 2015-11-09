
# 1.- add the mysql-community repo
#   sudo rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
# 2.- install mysql
#   yum install mysql-community-server
# 3.- start service
#   service mysqld start
# 4.- first configuration mysql
#   mysql_secure_installation
# 5.- alternative to step 4
#     mysql -u root
#     mysql> . Use the below given commands to reset root’s password.
#     mysql> use mysql;
#     mysql> update user set password=PASSWORD("GIVE-NEW-ROOT-PASSWORD") where User='root';
#     mysql> flush privileges;
#     
#     mysql> SELECT User, Host, Password FROM mysql.user;
#     mysql> CREATE USER 'root'@'%' IDENTIFIED BY "PASSWORD";
#     mysql> GRANT ALL PRIVILEGES ON *.* TO "root"@"%" IDENTIFIED BY "PASSWORD" WITH GRANT OPTION;
#     mysql> FLUSH PRIVILEGES;
#     mysql> quit
# --- with mysqlworkbeanch you can create users and block acces for root
