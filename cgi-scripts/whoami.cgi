#!/usr/bin/python

import cgi
import sys
import json

sys.path.append("/home/john/projects/lilian/")

import lilian

#what did they tell us for user and password

form = cgi.FieldStorage()
session_id = form.getvalue("session_id","")
session_id = cgi.escape(session_id)
user = lilian.whoami(session_id)

print "Content-type:application/json"
print
response = {"user":user}

print (json.JSONEncoder().encode(response))
