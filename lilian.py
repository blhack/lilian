import MySQLdb
import cgi
import bcrypt

#mysql_parms is a one line csv that is $username,$password for mysql

path_to_parms = 'db/parms.my'

mysql_parms = open(path_to_parms,"r").read().rstrip("\n").split(",")

mysql_username = mysql_parms[0]
mysql_password = mysql_parms[1]
mysql_db = mysql_parms[2]

db = MySQLdb.connect(user=mysql_username,passwd=mysql_password,db=mysql_db)
c = db.cursor()

