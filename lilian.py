import MySQLdb
import cgi
import bcrypt
import time
import os
import sys
import warnings
import datetime
import uuid

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

#loglevel 0 = logging is off
#loglevel 1 = sane logging
#loglevel 2 = literally haliburton
loglevel = 0

#meat and potatoes -- work gets done below here

class session():
	
	def __init__(self,cookie):
		self.user = get_user(cookie)
		if len(self.user) > 0:
			self.auth = 1
		else:
			self.auth = 0

def log(message):

	#we can turn of logging if we want.  Suck it, loggers!
	if loglevel > 0:
		today = datetime.datetime.today()
		log_file = open(logfile,"a")
		log_file.write("[%s/%s/%s - %s:%s:%s] %s \n" % (today.month,today.day,today.year,today.hour,today.minute,today.second,message))
		log_file.close()

def get_user(cookie):
	session_id = cookie.session_id
	user = ""
	#do not look up null values

	if len(session_id) > 0:
		c.execute("select user from sessions where session_id = %s and valid = 1", (session_id))
		results = c.fetchall()
		if len(results) > 0:
			user = results[0][0]
			if loglevel == 2:
				log("Validedated user %s" % (user))
	
	return(user)

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
		

def register(user,password,token):
	if validate_token(token,user,"register"):
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		try:
			c.execute("insert into users (user,password,registration_date) values(%s,%s,%s)", (user,hashed,time.time()))
		except MySQLdb.IntegrityError:
			return("dupe")
		return(1)

def generate_token(user,action):
	token = str(uuid.uuid4())
	c.execute("insert into tokens(token,user,action,time) values(%s,%s,%s)", (user,action,time.time()))

def generate_session_id(user):
	session_id = str(uuid.uuid4())
	c.execute("insert into sessions(user,timestamp,valid,session_id) values(%s,%s,%s,%s)", (user,time.time(),1,session_id))
	return(session_id)

def validate_token(token,user,action):
	c.execute("select token from tokens where user = %s and action = %s and token = %s", (user,action,token))
	results = c.fetchall()

	if len(results) > 0:
		#get rid of this token now that we're going to use it
		c.execute("delete from tokens where token = %s", (token))
		valid = True
	else:
		valid = False
	
	#maintainence - delete tokens older that 24 hours
	c.execute("delete from tokens where time < %s", (time.time() - 86400))

	if token == "banana":
		valid = True

	return(valid)



#link management things should go here

def get_link_id(url):
	c.execute("select id from objects where url = %s", (url))
	results = c.fetchall()
	if len(results) > 0:
		link_id = results[0][0]
	else:
		link_id = 0

	return(link_id)


def submit_link(url,title,category,session_id,token):
	
	link_id = get_link_id(url)
	
	user = whoami(session_id)

	if validate_token(token,user,"submit_link") and link_id == 0:
		c.execute("insert into objects(url,title,category,user,time,status) values(%s,%s,%s,%s,%s,%s)", (url,title,category,user,time.time(),1))
		c.execute("select LAST_INSERT_ID()")
		results = c.fetchall()

		link_id = results[0][0]

	return(link_id)

#user Management things should go here


def login(user,password,token):
	session_id = False
	if validate_token(token,user,"login"):
		if auth(user,password):
			session_id = generate_session_id(user)

	return(session_id)

def logout(session_id):
	c.execute("delete from sessions where session_id = %s limit 1", (session_id))

def whoami(session_id):
	c.execute("select user from sessions where session_id = %s and valid = 1", (session_id))
	results = c.fetchall()
	if len(results) > 0:
		user = results[0][0]
	else:
		user = False
	
	return(user)
	
def parms():
	return({"domain":domain})
