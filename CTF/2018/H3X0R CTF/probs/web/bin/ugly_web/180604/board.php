<?php
	require __DIR__."/_config.php";

	if(!is_login()){
		redirect("./login.php");

	}else if($do === "write_post"){
		if(!is_valid_contents($contents)){
			$msg = "invalid contents";

		}else if(!add_post($contents)){
			$msg = "failed to write";

		}else{
			$contents = "";

		}
	}

	$posts = get_posts();
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>board - uglyweb</title>
	</head>
	<body>
		<h2>board</h2>
		<table border="1">
			<colgroup>
				<col style="width: 150px;">
				<col style="width: 400px">
				<col style="width: 100px;">
			</colgroup>
			<thead>
				<tr>
					<th>time</th>
					<th>contents</th>
					<th>writter</th>
				</tr>
			</thead>
			<tbody>
<?php
	foreach($posts as $post){
?>
				<tr>
					<td><?php echo htmlentities($post['time']); ?></td>
					<td><?php echo htmlentities($post['contents']); ?></td>
					<td><?php echo htmlentities($post['writter']); ?></td>
				</tr>
<?php
	}
?>
			</tbody>
		</table>
		<br>
		<form action="./board.php" method="post">
			<input type="hidden" name="do" value="write_post">
			<input type="text" name="contents" placeholder="contents" value="<?php echo htmlentities($contents); ?>">
			<button type="submit">write</button>
		</form>
		<p><?php echo htmlentities($msg); ?></p>
	</body>
</html>