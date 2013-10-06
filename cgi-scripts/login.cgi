#!/usr/bin/python

import Cookie
import os
import time
import cgi
import sys
import json

sys.path.append("/home/john/projects/lilian/")

import lilian

#what did they tell us for user and password

form = cgi.FieldStorage()
user = form.getvalue("user","")
password = form.getvalue("password","")
token = form.getvalue("token","")

session_id = lilian.login(user,password,token)
print "Content-type:application/json"
print
response = {"session_id":session_id}

print (json.JSONEncoder().encode(response))
