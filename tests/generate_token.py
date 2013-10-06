#!/usr/bin/python

import sys

sys.path.append("/home/john/projects/lilian/")

import lilian

#generate a token

token = lilian.generate_token("Ryan","login")
print token
