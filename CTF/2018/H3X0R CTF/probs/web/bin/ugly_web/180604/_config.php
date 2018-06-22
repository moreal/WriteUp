<?php
	error_reporting(0);
	session_start();

	extract($_REQUEST);

	define("__FLAG__", "**secret**");
	define("__HASH_SALT__", "TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST");

	if(strlen(__HASH_SALT__) < 80){
		die("the hash salt is too short");
	}

	require __DIR__."/_function.php";