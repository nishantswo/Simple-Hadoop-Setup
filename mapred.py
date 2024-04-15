#!/usr/bin/python
import os
import commands
import cgi
import cgitb
cgitb.enable()
print "Content-type: text/html"
print ""


data=cgi.FieldStorage()
files=data['files'].value
mapred=data['choose'].value


print inpt_file+"</br>"
print mapred+"</br>"

mr=mapred.split('/')
print mr[0]
print mr[1]



if inpt_file!='none':	
	os.system('''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nn+''' "hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /"''')


