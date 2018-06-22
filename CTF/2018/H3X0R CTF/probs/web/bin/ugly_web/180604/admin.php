<?php
	require __DIR__."/_config.php";

	if(!is_login()){
		redirect("./login.php");

	}if(get_my_username() !== "admin"){
		$msg = "permission denied";

	}else if($do === "view_flag"){
		if(!is_valid_password($confirm_password)){
			$msg = "invalid password";
		
		}else if(secure_hash($confirm_password) !== get_my_password()){
			$msg = "wrong password";

		}else{
			$confirm_password = "";
			$msg = __FLAG__;

		}
	}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>admin - uglyweb</title>
	</head>
	<body>
		<h2>admin panel</h2>
		<form action="./admin.php" method="post">
			<input type="hidden" name="do" value="view_flag">
			<input type="password" name="confirm_password" placeholder="confirm password" value="<?php echo htmlentities($confirm_password); ?>">
			<button type="submit">view flag</button>
		</form>
		<p><?php echo htmlentities($msg); ?></p>
	</body>
</html>