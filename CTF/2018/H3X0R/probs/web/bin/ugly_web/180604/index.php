<?php
	require __DIR__."/_config.php";
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>uglyweb</title>
	</head>
	<body>
		<h2>welcome to uglyweb</h2>
		<p><img src="https://i.imgur.com/fbrwDKu.gif"></p>
		<a href="./">home</a>
<?php
	if(is_login()){
		if(get_my_username() === "admin"){
?>
		<a href="./admin.php">admin</a>
<?php
		}
?>
		<a href="./board.php">board</a>
		<a href="./logout.php">logout</a>
<?php
	}else{
?>
		<a href="./login.php">login</a>
		<a href="./register.php">register</a>
<?php
	}
?>
	</body>
</html>