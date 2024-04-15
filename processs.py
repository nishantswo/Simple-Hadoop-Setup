#!/usr/bin/python
import os
import commands
import cgi
import cgitb
import time
cgitb.enable()
print "Content-type: text/html"
print ""

 
nn=commands.getoutput('cat /var/www/cgi-bin/proj/files/job')
print nn
data=cgi.FieldStorage()

folder=data['folder'].value
folderr=data['folderr'].value
files=data['file'].value
mapred=data['choose'].value





os.system('''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nn+''' "hadoop fs -mkdir /'''+folder+'''"''')
os.system('''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nn+''' "hadoop fs -copyFromLocal /'''+files+''' /'''+folder+'''/"''')

if mapred!='none':
	os.system('''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nn+''' "hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /'''+folder+'''/'''+files+''' /'''+folderr+'''"''')

print"</br></br><input type='submit' value='deploy a complete hadoop stack into your cluster'></form>"

























	
