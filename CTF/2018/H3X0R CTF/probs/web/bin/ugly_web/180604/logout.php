<?php
	require __DIR__."/_config.php";

	if(!is_login()){
		die("not logged in");

	}else{
		unset_login();
		redirect("./");

	}