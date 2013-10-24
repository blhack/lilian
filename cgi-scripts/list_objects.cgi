#!/usr/bin/python

import cgi
import sys
import json

sys.path.append("/home/john/projects/lilian/")

import lilian

#what did they tell us for user and password

form = cgi.FieldStorage()
last = form.getvalue("last",0)
try:
	last = int(last)
except:
	last = 0

objects = lilian.list_objects(last,100)

print "Content-type:application/json"
print
response = {"objects":objects}

print (json.JSONEncoder().encode(response))
