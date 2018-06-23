<?php
	require __DIR__."/_config.php";

	if(is_login()){
		redirect("./");

	}else if($do === "register"){
		if(!is_valid_username($username)){
			$msg = "invalid username";

		}else if(is_exists_username($username)){
			$msg = "already exists username";

		}else if(!is_valid_password($password)){
			$msg = "invalid password";

		}else if($password !== $confirm_password){
			$msg = "not equal password";

		}else if(!add_user($username, $password)){
			$msg = "failed to register";

		}else{
			redirect("./login.php");
		}
	}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>register - uglyweb</title>
	</head>
	<body>
		<h2>user register</h2>
		<form action="./register.php" method="post">
			<input type="hidden" name="do" value="register">
			<input type="text" name="username" placeholder="username" value="<?php echo htmlentities($username); ?>">
			<input type="password" name="password" placeholder="password" value="<?php echo htmlentities($password); ?>">
			<input type="password" name="confirm_password" placeholder="confirm password" value="<?php echo htmlentities($confirm_password); ?>">
			<button type="submit">register</button>
		</form>
		<p><?php echo htmlentities($msg); ?></p>
	</body>
</html>