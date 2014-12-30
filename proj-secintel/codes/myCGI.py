import cgitb; cgitb.enable()
import cgi
import os

input_data  = cgi.FieldStorage()
if input_data:
    print "Content-Type: text/html\n"
    print "hello"
else:
    f = open('my.html', 'r'); s = f.read(); f.close()
    print "Content-Type: text/html\n"
    print s
