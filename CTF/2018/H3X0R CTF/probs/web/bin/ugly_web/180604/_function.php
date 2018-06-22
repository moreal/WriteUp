<?php
	function secure_hash($data){
		return hash("sha256", __HASH_SALT__.$data);
	}
	function redirect($url){
		header("Location: ".$url);
		die;
	}

	function is_login(){
		return isset($_SESSION['is_login']);
	}
	function set_login($username, $password){
		$_SESSION['is_login'] = true;
		$_SESSION['username'] = strtolower($username);
		$_SESSION['password'] = secure_hash($password);
		return;
	}
	function unset_login(){
		unset($_SESSION['is_login'], $_SESSION['username'], $_SESSION['password']);
		return;
	}

	function is_valid_username($username){
		return preg_match("/^[a-z0-9_-]{4,20}$/is", $username);
	}
	function is_exists_username($username){
		return is_file(__DIR__."/users/".strtolower($username).".txt");
	}
	function is_valid_password($password){
		return preg_match("/^.{8,100}$/is", $password);
	}
	function is_valid_contents($contents){
		return preg_match("/^.{1,100}$/is", $contents);
	}

	function get_my_username(){
		return isset($_SESSION['username']) ? $_SESSION['username'] : false;
	}
	function get_my_password(){
		return isset($_SESSION['password']) ? $_SESSION['password'] : false;
	}
	function get_user_password($username){
		return file_get_contents(__DIR__."/users/".strtolower($username).".txt");
	}
	function get_posts($username){
		$time = time();
		$time_div = intval($time / (60 * 60));
		$posts = [];
		foreach(scandir(__DIR__."/boards/".$time_div."/") as $filename){
			if($filename !== "." && $filename !== ".."){
				$posts[] = [
					'time' => date("y-m-d H:i:s", hexdec(substr($filename, 0, 8))),
					'contents' => file_get_contents(__DIR__."/boards/".$time_div."/".$filename),
					'writter' => substr($filename, 8, -4)
				];
			}			
		}
		usort($posts, function($a, $b){
			if($a['time'] < $b['time']){
				return -1;

			}else if($a['time'] > $b['time']){
				return 1;

			}else{
				return 0;

			}
		});
		return $posts;
	}

	function add_user($username, $password){
		if(!is_dir(__DIR__."/users/") && !mkdir(__DIR__."/users/")){
			return false;
		}
		return file_put_contents(__DIR__."/users/".strtolower($username).".txt", secure_hash($password));
	}
	function add_post($contents){
		$time = time();
		$time_div = intval($time / (60 * 60));
		if(!is_dir(__DIR__."/boards/") && !mkdir(__DIR__."/boards/") || !is_dir(__DIR__."/boards/".$time_div."/") && !mkdir(__DIR__."/boards/".$time_div."/")){
			return false;
		}
		return file_put_contents(__DIR__."/boards/".$time_div."/".sprintf("%08x", $time).get_my_username().".txt", $contents);
	}