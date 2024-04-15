#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
print "Content-Type: text/html"
print ""

x='''<form action= "action.py" method= "POST">'''
print x

print """
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
display: inline-block;
height: 43px;
width: 350px;
font-size: 1em;
font-size: 18px;
font-weight: bold ;
text-align: center ;
float: left;
//text-decoration: underline;
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
top: 268px;
left 220px;
margin:5px;
}

div.s
{
//border: 2px solid blue;
position: absolute;
top: 280px;
left: 240px;
margin: 250px;
}


</style>


<html>
<title>SYDOOP</title>


 <div class="jumbotron" style="background-color:#4e6982; padding-top: 30px;margin:0;">
    <h2 style="color:pink;text-align:center;font-size:25px "><strong> WELCOME TO SYDOOP</strong></h2>

      <div class="row">
       <div class="col-md-2"><img src="/media/img.gif"></div>
      </div>
     
       

   </div> 
<div class='m'>

<a class='mymenu' >Network Management</a>
</div> 
   
 
<br>

<div class='s'>
     <a style="padding-top: 8px; height:23px;" class='ss' href='action.py'>Click over here to Create your cluster..!</a>
</div>
<h2 style="color:#4e6982;text-align:center;font-size:25px;padding-top: 30px; "><strong> Node Management</strong></h2>
<div class='nn'>   
       <a style="margin-top: 10px" class='mm' >NAMENODE
       <a style="margin-top: 10px" class='mm' >DATANODE
       <a style="margin-top: 10px" class='mm' >DEVICE IP
       <a style="margin-top: 10px" class='mm' >DISK CAPACITY
       <a style="margin-top: 10px" class='mm' >TOTAL RAM
       <a style="margin-top: 10px" class='mm' >CPU PROCESSORS
</br></br></br>
</a>
</div>
</div>
</head>

</html>"""

print "</br></br></br>"

data=cgi.FieldStorage()
i_p=data['ip'].value
class scan():
	dic_sys={}
	#def scan_ip(self):
	#	os.system("sudo nmap -sn "+i_p+" | grep report > /var/www/cgi-bin/proj/nmap_report")
	def split_ip(self):
		os.system("rm -f /var/www/cgi-bin/proj/files/i_p")
		with open ('/var/www/cgi-bin/proj/files/nmap_report') as f:
			for each in f:
				x=each.split()[5]
        		        l=len(x)-1
        		        ip_s=x[1:l]
				scan.dic_sys['ip']=ip_s				
				f=open('/var/www/cgi-bin/proj/files/i_p','a')
				f.write(ip_s+'\n')
				f.close()
				
				
	def check_info(self):
		with open ('/var/www/cgi-bin/proj/files/i_p') as f:
			for each_ip in f:
				ip=each_ip[0:-1]	
				chk="sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+""
				check=os.system(chk)
				if check==0:
					os.system("sudo ssh "+ip+" hostname > /var/www/cgi-bin/proj/files/hosts")
					#with open ("hosts") as f:
					#	for each in f:
					#		scan.dic_sys['host']=each		
						
					
					os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@127.0.0.1 mkdir -p /data/"+ip)
					os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'mkdir /project'")

					os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'parted -l /dev/sda > /project/hdd.txt'")
					os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no "+ip+":/project/hdd.txt  /data/"+ip)
					dic={}
					with open('/data/'+ip+'/hdd.txt') as f:
						i=0
						for each in f:
							dic[i]=each
							i+=1
						mx=int(dic[1].split()[2][0:-2])
						mn=int(dic[i-3].split()[2][0:3])
						rem=mx-mn
					scan.dic_sys['hd']=rem

					os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'free -m | grep Mem > /project/ram.txt'")
					os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no root@"+ip+":/project/ram.txt         /data/"+ip)
					with open('/data/'+ip+'/ram.txt') as f:
						for each in f:
							ram=each.split()[1]
							if ram>1500 and ram<2000:
								r='2GB' 
							else:
								r='4GB'			
					scan.dic_sys['ram']=r
		

	
					os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'cat /proc/cpuinfo | grep processor | wc -l > /project/cpu.txt'")
					os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no root@"+ip+":/project/cpu.txt  /data/"+ip)
					with open('/data/'+ip+'/cpu.txt') as f:
						cpu=f.readline()
					scan.dic_sys['cpu']=cpu
					
					#print "<pre><table><tr><td><input type='radio' name='nn' value='+ip+'></td><td><input type='checkbox' name='dn' value="+ip+"></td><td><"+ip+"></td></tr></table></pre>"

           				print "<div style='margin:5px'><a class='my' style='height:20px'><input type='radio' name='nn' value="+ip+"></a><a class='my' ><input type='checkbox' name='dn' value="+ip+"></a><a class='my' >"+ip+"</a><a class='my' >"+str(scan.dic_sys['hd'])+"GB</a><a class='my' >"+scan.dic_sys['ram']+"</a><a class='my' >"+cpu+"</a></div>"





a=scan()
#a.scan_ip()
a.split_ip()
a.check_info()






print "</br></br><p style=color:#4e6982;font-size:22px;padding-top:35px;>Enter Hard Disk size:<input type='text' name='hd'></p>"



print "<input type='submit' value='create'>"
