#!/usr/bin/python2

print "content-type: text/html\r\n"

print """
<form action="save.py" method="POST">
<div style="text-align: center;">
	<div style="box-sizing: border-box; display: inline-block; width: auto; max-width: 480px; background-color: #FFFFFF; border: 2px solid #0361A8; border-radius: 5px; box-shadow: 0px 0px 8px #0361A8; margin: 50px auto auto;">
	<div style="background: #0361A8; border-radius: 5px 5px 0px 0px; padding: 15px;"><span style="font-family: verdana,arial; color: #D4D4D4; font-size: 1.00em; font-weight:bold;">Register yourself</span></div>
	<div style="background: ; padding: 15px">
	<style type="text/css" scoped>
	td { text-align:left; font-family: verdana,arial; color: #064073; font-size: 1.00em; }
	input { border: 1px solid #CCCCCC; border-radius: 5px; color: #666666; display: inline-block; font-size: 1.00em;  padding: 5px; width: 100%; }
	input[type="button"], input[type="reset"], input[type="submit"] { height: auto; width: auto; cursor: pointer; box-shadow: 2px 3px 5px #0361A8; float: right; margin-top: 10px; }
	table.center { margin-left:auto; margin-right:auto; }
	.error { font-family: verdana,arial; color: #D41313; font-size: 1px; }
	</style>
<form method="post" action="" name="aform" target="_top">
<input type="hidden" name="action" value="login">
<input type="hidden" name="hide" value="">

<table class='center'>
<tr><td>Name :</td><td><input type="text" name="name"></td></tr>
<tr><td>phone :</td><td><input type="text" name="phone"></td></tr>
<tr><td>Password :</td><td><input type="password" name="password"></td></tr>
<tr><td>Confirm Password :</td><td><input type="password" name="confirm_password"></td></tr>
<tr><td>Email-id :</td><td><input type ="text" name ="email"></td></tr>&nbsp;&nbsp;
<tr><td><input type="submit" value="submit"></td></tr>
<tr><td colspan=2>&nbsp;</td></tr>
<tr><td><a href="login_registration.py">previous </a></td><tr>

</table>
</form>
</d iv></div></div>

"""
