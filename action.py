#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
print "Content-Type: text/html"
print ""
x='''<form action="mr.py" method="POST">
<!DOCTYPE html>
<html>
<head>
<style>
a.my
{
border: 1px groove #D4D4D4;

font-family: verdana,arial; color: #064073;
display: block;
width: 220px;
font-size: 17px;
font-weight: bold;
text-align: center ;
float: left;
text-decoration: none;
-moz-box-shadow: ;
}




a.mymenu
{
font-family: verdana,arial; color: #4e6982;
display: block;
height: 24px;
width: 1350px;
font-size: 1em;
background-color:white;
font-size: 21px;
font-weight: bold;
text-align: center ;
float: left;
text-decoration: none;
-moz-box-shadow: 1px 1px 2px 1px #4e6982;
}

a.ss
{
//border: 0.5px solid blue;
font-family: arial; color: #4e6982;
text-decoration:none;
display: inline-block;
height: 43px;
width: 350px;
font-size: 1em;
font-size: 18px;
font-weight: bold ;
text-align: center ;
float: left;
-moz-box-shadow: 1px 1px 1px 2px #c4cde0 ;
}

a.mm
{
border: 0.8px groove #4e6982;
font-family: arial; color: #4e6982;
display: inline-block;
padding-top:5px;
height: 25px;
width: 220px;
font-size: 1em;
font-size: 16px;
font-weight: bold ;
text-align: center ;
float: left;
//text-decoration: underline;
-moz-box-shadow:  1px 1px 3px  #4e6982 ;
}

a:hover.mymenu
{
text-decoration: none;

color: #4e6982;
background-color:#ebeef4;
width:1350px;
float: center;
}



a:hover.ss
{
text-decoration: none;
color: #4e6982;
background-color: #ebeef4;
font-size: 18px;
}

div.n
{
//border: 2px solid blue;
position: absolute;
top: 280px;
left 220px;
//margin: 20px;
}

div.nn
{
border: 3px bold #D4D4D4;
position: absolute;
top: 266px;
left 220px;
margin:5px;
}

div.s
{
//border: 2px solid blue;
position: absolute;
top: 140px;
left: 10px;
margin: 200px;
}

div.r
{
//border: 2px solid blue;
position: absolute;
top: 140px;
left: 600px;
margin: 200px;
}


</style>


<html>
<title>SYDOOP</title>


 <div class="jumbotron" style="background-color:#4e6982; padding-top: 30px;margin:0;">
    <h2 style="color:pink;text-align:center;font-size:25px; "><strong> WELCOME TO SYDOOP</strong></h2>

      <div class="row">
       <div class="col-md-2"><img src="/media/img.gif"></div>
      </div>
     
       

   </div> 
<div class='m'>

<a class='mymenu' href='login.py'>Cluster Report</a>

</div> 
   
 
<br>

<div class='s'>
     <a style="padding-top: 8px; height:23px;" class='ss' href='http://127.0.0.1:50070/dfshealth.jsp'>HADOOP NameNode Administration</a>
</div>

<div class='r'>
     <a style="padding-top: 8px; height:23px;" class='ss' href='http://127.0.0.1:50030/jobtracker.jsp'>HADOOP MapReduce Administration</a>
</div>

<h2 style="color:#4e6982;text-align:center;font-size:25px;padding-top: 30px; "><strong>YOUR HADOOP CLUSTER HAS BEEN SET UP...</strong></h2>
</div>
</head>

</html>'''

     
       




print x

form=cgi.FieldStorage()
nn=form['nn'].value
hd=form['hd'].value
key =form.keys()
dn=key[0]
value =form.getvalue(dn)
print ""
print "<tr><td></br></br></br></br></br></br></br></br></br></br><a href='modify.py'>Click</a> to add more Datanodes</td><tr>"
os.system("sudo ssh "+nn+" rm -f /var/www/cgi-bin/proj/files/task")
class write_ip():
	def write_nn(self):
		os.system("sudo ssh "+nn+" echo -e "+nn+" | cat > /var/www/cgi-bin/proj/files/job")
	def write_dn(self):		
		for dn in value:
			os.system("sudo ssh "+nn+" echo -e "+dn+" | cat >> /var/www/cgi-bin/proj/files/task")
		

class install():
	def nn_install(self):
		os.system("sudo ssh "+nn+" yum install jdk hadoop -y &> /dev/null")
		os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+nn+''' "echo -e 'PATH=/usr/java/jdk1.7.0_51/bin:$PATH export PATH' | cat >> /root/.bashrc"''')		
	def dn_install(self):
		for dn in value:
			os.system("sudo ssh "+dn+" yum install jdk -y &> /dev/null")
			os.system("sudo ssh "+dn+" yum install hadoop -y &> /dev/null")
			os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+dn+''' "echo -e 'PATH=/usr/java/jdk1.7.0_51/bin:$PATH export PATH' | cat >> /root/.bashrc"''')
			
class config():
	def nn_config(self):
		os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+nn+''' "sed -i  '/<configuration>/a <property><name>fs.default.name</name><value>hdfs://'''+nn+''':9001</value></property>' /etc/hadoop/core-site.xml &> /dev/null"''')
		 

		os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+nn+''' "sed -i  '/<configuration>/a <property><name>mapred.job.tracker</name><value>'''+nn+''':9002</value></property>' /etc/hadoop/mapred-site.xml &> /dev/null"''')
		
	def dn_config(self):
		for dn in value:		
                        os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+dn+''' "sed -i  '/<configuration>/a <property><name>fs.default.name</name><value>hdfs://'''+nn+''':9001</value></property>' /etc/hadoop/core-site.xml &> /dev/null"''')
		
			os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+dn+''' "sed -i  '/<configuration>/a <property><name>dfs.data.dir</name><value>/datano</value></property>' /etc/hadoop/hdfs-site.xml &> /dev/null"''') 

			os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+dn+''' "sed -i  '/<configuration>/a <property><name>mapred.job.tracker</name><value>'''+nn+''':9002</value></property>' /etc/hadoop/mapred-site.xml &> /dev/null"''')

class partition():
	def part_dn(self):
		if hd!=0:
			print hd
			for dn in value:
				os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+nn+''' "echo -e '\np\nn\n\n+'''+hd+'''\nw' | fdisk -cu /dev/sda &> /dev/null"''')
				os.system("sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" 'partx -a /dev/sda &> /dev/null'")
				os.system("sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" 'fdisk -cul /dev/sda > /var/www/cgi-bin/proj/disk1'")
				with open ('/var/www/cgi-bin/proj/disk1') as f:
					dict={}
					i=0
					for each_disk in f:
						dict[i]=each_disk
	        				i+=1
					ab=dict[i-1].split()[0]
				os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+nn+" 'mkfs.ext4  "+ab+" &> /dev/null'")
				os.system("sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" 'mkdir /datano &> /dev/null'")
				os.system('''sshpass -p "redhat" ssh -o stricthostkeychecking=no root@'''+nn+''' "mount '''+ab+''' /datano &> /dev/null"''')
class daemon(write_ip,install,config,partition):
	def permission(self):
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/start-all.sh &> /dev/null")
  		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/start-dfs.sh &> /dev/null")
    		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/start-mapred.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/hadoop-daemons.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/slaves.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/stop-all.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/stop-mapred.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" chmod +x /usr/sbin/stop-dfs.sh &> /dev/null")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" cp /var/www/cgi-bin/proj/i_p /etc/hadoop/slaves")
	
	def format(self):
		#os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" 'hadoop namenode -format -Y &> /dev/null'")		
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" hadoop-daemon.sh start namenode")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" hadoop-daemon.sh start datanode")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" hadoop-daemon.sh start jobtracker")
		os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" hadoop-daemon.sh start tasktracker")	
		#os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+nn+" 'hadoop-daemon.sh start namenode'")
		#for dn in value:
		#	os.system("sudo sshpass -p 'redhat' ssh -o stricthostkeychecking=no root@"+dn+" 'hadoop-daemon.sh start datanode'")





a=daemon()
a.write_nn()
a.write_dn()
#a.dn_install()
#a.nn_config()
#a.dn_config()
#a.part_dn()
#a.format()
#a.permission()


print"</br></br><input type='submit' value='upload data'>"

