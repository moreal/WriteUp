<?php
	require __DIR__."/_config.php";

	if(is_login()){
		redirect("./");

	}else if($do === "login"){
		if(!is_valid_username($username)){
			$msg = "invalid username";

		}else if(!is_exists_username($username)){
			$msg = "not exists username";

		}else if(!is_valid_password($password)){
			$msg = "invalid password";
		
		}else if(secure_hash($password) !== get_user_password($username)){
			$msg = "wrong password";

		}else{
			set_login($username, $password);
			redirect("./");
		}
	}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>login - uglyweb</title>
	</head>
	<body>
		<h2>user login</h2>
		<form action="./login.php" method="post">
			<input type="hidden" name="do" value="login">
			<input type="text" name="username" placeholder="username" value="<?php echo htmlentities($username); ?>">
			<input type="password" name="password" placeholder="password" value="<?php echo htmlentities($password); ?>">
			<button type="submit">login</button>
		</form>
		<p><?php echo htmlentities($msg); ?></p>
	</body>
</html>