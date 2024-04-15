#!/usr/bin/python

import commands
import cgi
import cgitb
cgitb.enable()

print "Content-type: text/html\n"
print ""
print """
<style>
p.lw
{
color:fuchsia;
text-decoration: none;
text-align:left;
font-size: 15px;
}

p.w
{
color:fuchsia;
margin:20px;
font-weight: bold;
text-decoration:;
text-align:left;
font-size: 15px;
}

#l
{
color:fuchsia;
text-align:left;
font-size: 24px;
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

a.mm
{
//border: 0.5px solid blue;
font-family: arial; color: #4e6982;
display: inline-block;
height: 43px;
width: 250px;
font-size: 1em;
font-size: 16px;
font-weight: bold ;
text-align: center ;
float: left;
//text-decoration: underline;
-moz-box-shadow: 1px 1px 3px 1px #c4cde0 ;
}

a:hover.mymenu
{
text-decoration: none;

color: #4e6982;
background-color:#ebeef4;
width:1350px;
float: center;
}

p:hover.lw
{
border: 2px solid #ebeef4;
text-decoration: ;
background-color:#ebeef4;
color: #3b5998;
width:1250px;
}

p:hover.w
{
text-decoration: ;
font-weight: bold;
color: #c4cde0;
width:1250px;
}

div.m
{
//border: 2px solid blue;
position: absolute;
top: 135px;
left 220px;
}

div.n
{
//border: 2px solid blue;
position: absolute;
top: 250px;
left: 175px;
margin: 20px;
}

div.mr
{
//border: 2px solid blue;
position: absolute;
top: 250px;
left: 860px;
margin: 20px;
}

div.mrr
{
//border: 2px solid blue;
position: absolute;
top: 0px;
left: 680px;
width:500px;

}
div.o
{
//border: 2px solid blue;
position: absolute;
top: 70px;
left: 0px;
width:400px;
margin: 
}

div.oo
{
//border: 2px solid blue;
position: absolute;
top: 300px;
left: 110px;
margin: 
}



</style>




<div class='m'>
<a class='mymenu' href=>Upload and Run</a>
</div>

<div class='n'>
<a style="padding-top: 8px; height:23px;" class='mm'>Upload Data into HDFS</a>
</div>

<div class='mr'>
<a style="padding-top: 8px; height:23px;" class='mm'>Run MR queries</a>
</div>


<html>
<title>SYDOOP</title>


 <div class="jumbotron" style="background-color:#4e6982; padding-top: 30px;margin:0;">
    <h2 style="color:pink;text-align:center;font-size:25px;"><strong> WELCOME TO SYDOOP</strong></h2>

      <div class="row">
       <div class="col-md-2"><img src="/media/img.gif"></div>
      </div>
     
       

   </div> 
   
   
 
<br>




</p>
    </div> 
</div>    
</div>
  
 </div>           
</body>
</html>"""
	

print "</br></br></br></br></br>"
x='''<form action="processs.py" method="POST">	
	<div class='oo'></br><p style=color:#4e6982;font-size:22px;padding-top:0px;>Input Directory <input type='text' name='folder'></p></br></br>
	<div class='o'></br><p style=color:#4e6982;font-size:22px;>Output Directory <input type='text' name='folderr'></p>
	Browse File<input type='text' name='file'>
	

<div class='mrr'><form</br></br><p style=color:#4e6982;font-size:22px;padding-top:0px;>Select your Desire! <select name="choose">
		<option value="none">SELECT</option></br>
		<option value="wordcount">WordCount</option>
		</select>
                </br>
	
	</br>
	</form>'''

print x

print "<input type='submit' value='proceed!!'>"

