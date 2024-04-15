#!/usr/bin/python

print "content-type: text/html\r\n"

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
cell-spacing: 7px;
height: 43px;
width: 350px;
top: 150px;
font-size: 1em;
font-size: 16px;
font-weight: bold ;
text-align: center ;
float: left;
//text-decoration: underline;
-moz-box-shadow: 1px 1px 1px 2px #c4cde0 ;
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
margin: 20px;
top: 280px;
left 220px;
}

</style>




<div class='m'>
<a class='mymenu' >Login</a>

</div>

<div class='n'>
<a  class='mm'>Please provide your Authentication for accessing the services of SYDOOP</a>
</div>




<html>
<title>SYDOOP</title>


 <div class="jumbotron" style="background-color:#4e6982; padding-top: 30px;margin:0;">
    <h2 style="color:pink;text-align:center;font-size:25px;";font-size:25px><strong> WELCOME TO SYDOOP</strong></h2>

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
</html>
<form action='network.py' method='post'>


<div style="text-align: center;">
	<div style="box-sizing: border-box; display: inline-block; width: auto; max-width: 480px; background-color: #FFFFFF; border: 2px solid #4e6982; border-radius: 5px; box-shadow: 0px 0px 8px #4e6982; margin: 50px auto auto;">
	<div style="background: #4e6982; border-radius: 5px 5px 0px 0px; padding: 15px;"><span style="font-family: verdana,arial; color: pink; font-size: 1.00em; font-weight:bold;">Login Credentials</span></div>
	<div style="background: ; padding: 15px">
	<style type="text/css" scoped>
	td { text-align:left; font-family: verdana,arial; color: #4e6982; font-size: 1.00em; }
	input { border: 1px solid #CCCCCC; border-radius: 5px; color: #666666; display: inline-block; font-size: 1.00em;  padding: 5px; width: 100%; }
	input[type="button"], input[type="reset"], input[type="submit"] { height: auto; width: auto; cursor: pointer; box-shadow: 0px 0px 5px #0361A8; float: right; margin-top: 10px; }
	table.center { margin-left:auto; margin-right:auto; }
	.error { font-family: verdana,arial; color: #D41313; font-size: 1px; }
	</style>
	



<table class='center'>
<tr><td>Enter the Name:</td><td><input type="text" name="login"></td></tr>
<tr><td>Password:</td><td><input type="password" name="password"></td></tr>
<tr><td>&nbsp;</td><td><input type="submit" value="login"></td></tr>
<tr><td colspan=2>&nbsp;</td></tr>
<tr><td colspan=2>Not member yet? Click <a href="registration.py">here</a> to register.</td></tr>
</table>
</form>
"""

