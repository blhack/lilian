import MySQLdb
import cgi
import bcrypt

#mysql_parms is a one line csv that is $username,$password,$db for mysql

path_to_parms = 'db/parms.my'

mysql_parms = open(path_to_parms,"r").read().rstrip("\n").split(",")

mysql_username = mysql_parms[0]
mysql_password = mysql_parms[1]
mysql_db = mysql_parms[2]

db = MySQLdb.connect(user=mysql_username,passwd=mysql_password,db=mysql_db)
c = db.cursor()


def auth(user,password):
	c.execute("select password from users where user = %s", (user))
	results = c.fetchall()
	if len(results) == 0:
		return(0)
	hashed = results[0][0]
	if bcrypt.hashpw(password, hashed) == hashed:
		return(1)
	else:
		return(0)
		
