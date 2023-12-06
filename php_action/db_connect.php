<?php

$localhost = "localhost";
$username = "root";
$password = "";
$dbname = "ict_database";

try {
	$connect = new mysqli($localhost, $username, $password, $dbname);
}
catch(mysqli_sql_exception){
	echo"Could not connect!";
}
?>