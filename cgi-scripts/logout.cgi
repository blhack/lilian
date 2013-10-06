#!/usr/bin/python

import cgi
import sys
import json
import Cookie
import os

cookie = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

sys.path.append("/home/john/projects/lilian/")

import lilian

#what did they tell us for user and password

if cookie.has_key("session_id"):
	session_id = cookie["session_id"].value
	lilian.logout(session_id)
	status = True
else:
	status = False

print "Content-type:application/json"
print
response = {"status":status}

print (json.JSONEncoder().encode(response))
