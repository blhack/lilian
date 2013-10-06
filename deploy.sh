#!/bin/bash

mypath=/var/www/newslily

cp lilian.py $mypath/modules/
cp -rvp htdocs/* $mypath/htdocs/
cp -rvp cgi-scripts/* $mypath/cgi-bin/
cp -rvp js/* $mypath/htdocs/js/
