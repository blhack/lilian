#!/usr/bin/python

import cgi
import sys
import json

sys.path.append("/home/john/projects/lilian/")

import lilian

#what did they tell us for user and password

form = cgi.FieldStorage()
object_id = form.getvalue("object_id","")

object_info = lilian.get_object_info(object_id)

print "Content-type:application/json"
print
response = object_info

print (json.JSONEncoder().encode(response))
