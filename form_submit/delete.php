<?php

require_once '../php_action/core.php';

$reply = [];
$errors = [];

if (isset($_SESSION['code']) && isset($_POST['formId'])) {
    $sql = "DELETE FROM `" . $_POST['formId'] . "` WHERE `Code`='{$_SESSION["code"]}'";
    $reply['sql'] = $sql; 
    if ($connect->query($sql) === FALSE) {
        $errors['sql'] = "Failed to insert entries";
    }
} else
    $errors[] = "Error with deletion detection.";

if (empty($errors)) {
    $reply['success'] = true;
} else {
    $reply['success'] = false;
    $reply['errors'] = $errors;
}
echo json_encode($reply);
