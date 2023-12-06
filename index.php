<?php

require_once "php_action/db_connect.php";

session_start();

if (isset($_SESSION['userId'])) {
	header('location: home.php');
}

if ($_POST) {
	$username = $_POST['username'];
	$password = $_POST['password'];

	$sql = "SELECT * FROM users WHERE username = '$username'";
	$result = $connect->query($sql);

	if ($result->num_rows == 1) {
		// $hash = password_hash($password, PASSWORD_DEFAULT);
		// exists
		$value = $result->fetch_assoc();
		$hash = $value['password'];
		if (password_verify($password, $hash)) {
			$user_id = $value['user_id'];
			$_SESSION['userId'] = $user_id;
			header('location: home.php');
		} else {
			$error = "Incorrect username/password.";
		}
	} else {
		$error = "Username does not exist!";
	}
}

?>

<!DOCTYPE html>
<html>

<head>
	<title>Inventory Management System</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=deivce-width, initial-scale=1">
	<!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">-->
	<link href="./assets/css/custom.min.css" rel="stylesheet">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">
	<script type="text/javascript" src="assets/jquery/jquery.min.js"></script>
	<link rel="stylesheet" type="text/css" href="assets/jquery-ui/jquery-ui.min.css">
	<script type="text/javascript" src="assets/jquery-ui/jquery-ui.min.js"></script>
	<script type="text/javascript" src="assets/bootstrap/js/bootstrap.min.js"></script>
</head>

<body>

	<div class="d-flex vh-100 w-100 align-items-center justify-content-center bg-primary">
		<div class="row justify-content-center w-md-75 m-sm-100">
			<div class="col-5 rounded shadow-lg border p-5 bg-white">
				<div class="center"><img class="logo mb-3" src="./assets/img/upd_logo.png" alt=""></div>
				<h1 class="title center">University of the Philippines Diliman</h1>
				<h2 class="py-3 center">ICT Database System</h2>
				<form action="index.php" method="post" id="loginForm">
					<div class="mb-3">
						<label for="username1" class="form-label">Username</label>
						<div class="input-group">
							<span class="input-group-text">
								<i class="bi bi-person-fill"></i>
							</span>	
							<input type="username" class="form-control" id="username" name="username" required>
						</div>
					</div>
					<div class="mb-3">
						<label for="password1" class="form-label">Password</label>
						<div class="input-group">
							<span class="input-group-text">
								<i class="bi bi-key-fill"></i>
							</span>	
						<input type="password" class="form-control" id="password" name="password" required>
						</div>
					</div>
					<button type="submit" class="mb-3 btn btn-outline-success">Log in</button>
					<div>
						<div class="row">
							<div class="col d-flex"><a href="#">User Manual</a></div>
							<div class="col d-flex justify-content-end"><p>Need help?&nbsp;</p><a href="#">Contact us</a></div>
						</div>
					</div>
					<h5 class="text-danger">
						<?php if (isset($error)) {echo $error;} ?>
					</h5>
				</form>
			</div>
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
