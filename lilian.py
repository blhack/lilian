import MySQLdb
import cgi
import bcrypt
import time
import os
import sys
import warnings

#see parms.py for parameters

from parms import *

#set up the database connection

db = MySQLdb.connect(user=db_user,passwd=db_pass,db=db_name)
c = db.cursor()


try:
	open(logfile,"a")
except IOError:
	warnings.warn("Cannot write to specified logfile.  See parms.py for log file location.  Logging to /tmp/lilian.log", UserWarning)
	logfile = "/tmp/lilian.log"
	

#global variables go here
now = time.time()


#meat and potatoes -- work gets done below here

def log(message):
	open(logfile,"a")


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
		

def register(user,password):
	hashed = bcrypt.hashpw(password, bcrypt.gensalt())
	try:
		c.execute("insert into users (user,password,registration_date) values(%s,%s,%s)", (user,hashed,now))
	except MySQLdb.IntegrityError:
		return("dupe")
		
	return(1)
