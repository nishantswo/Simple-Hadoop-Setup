#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
print "Content-Type: text/html"


print """
<style>
p.lw
{
color:#3b8898;
text-decoration: none;
text-align:left;
font-size: 15px;
}

p.w
{
color:#3b8898;
margin:20px;
font-weight: bold;
text-decoration:;
text-align:left;
font-size: 15px;
}

#l
{
color:#4e6982;
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
border: 1px groove #D4D4D4;
text-decoration: ;
background-color:#ebeef4;
color: #4e6982;
width:1250px;
}

p:hover.w
{
text-decoration: ;
font-weight: bold;
color: black;
width:1250px;
}

div.m
{
//border: 2px solid blue;
position: absolute;
top: 135px;
left 220px;
}



</style>




<div class='m'>
<a  class='mymenu' href='login.py'>Start your DATA Journey with SYDOOP..</a>

</div>






<html>
<title>SYDOOP</title>


 <div class="jumbotron" style="background-color:#4e6982; padding-top: 30px;margin:0;">
    <h2 style="color:pink;text-align:center;font-size:25px; "><strong> WELCOME TO SYDOOP</strong></h2>

      <div class="row">
       <div class="col-md-2"><img src="smileys-doctor-066788.gif"/></div>
      </div>
     
       

   </div> 
   
   
 
<br>



<div class="row">
   <div class="col-md-12">
     <h3 style="margin-top: 30px" align="left" id="l">About SYDOOP</h3>
   </div>
<div class="row">   
   <div class="col-md-12">
       <p style="margin-top: 10px" class="lw"> SYDOOP provides High Performance Distributed Computing for analyzing BIG DATA using HADOOP Framework.
       <p style="margin-top: 10px" class="lw"> SYDOOP provides you the facility to analyze your highly sensitive structured or unstructured data-sets.
       <p style="margin-top: 10px" class="lw"> SYDOOP offers you the flexibility to setup your own customized cluster in different loacation.   
       <p style="margin-top: 10px" class="lw"> SYDOOP automates all the Core Components of the hadoop framework like:-
       <p style="margin-top: 10px" class="w"> - Scanning of Nodes 
       <p style="margin-top: 10px" class="w"> - Setup of HDFS Filesystem
       <p style="margin-top: 10px" class="w"> - Setup Hadoop Cluster
       <p style="margin-top: 10px" class="w"> - Map Reduce Programming
       <p style="margin-top: 10px" class="w"> - Automatic Initialization and Live Status of NameNode, DataNode, JobTracker and Tasktracker
</p>
    </div> 
</div>    
</div>
  
 </div>           
</body>
</html>"""
