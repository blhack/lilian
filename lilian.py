import MySQLdb
import cgi
import bcrypt
import time
import os
import sys
import warnings
import datetime

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
	today = datetime.datetime.today()
	log_file = open(logfile,"a")
	log_file.write("[%s/%s/%s - %s:%s:%s] %s \n" % (today.month,today.day,today.year,today.hour,today.minute,today.second,message))


def auth(user,password):
	c.execute("select password from users where user = %s", (user))
	results = c.fetchall()
	if len(results) == 0:
		log("Did not authenticate user %s.  I do not know who this is." % (user))
		return(0)
	hashed = results[0][0]
	if bcrypt.hashpw(password, hashed) == hashed:
		log("Authenticated %s" % (user))
		return(1)
	else:
		log("Did not authenticate %s.  Invalid password." % (user))
		return(0)
		

def register(user,password):
	hashed = bcrypt.hashpw(password, bcrypt.gensalt())
	try:
		c.execute("insert into users (user,password,registration_date) values(%s,%s,%s)", (user,hashed,now))
	except MySQLdb.IntegrityError:
		return("dupe")
	return(1)


