<?php

require_once '../php_action/core.php';
$errors = [];
$data = [];

$office_ID = $_POST['office_ID'];
$year = $_POST['year'];

if (!is_numeric($office_ID)) {
    $errors['office_ID'] = "Input should be a number";
} else if ($office_ID > 99 || $office_ID < 0) {
    $errors['office_ID'] = "Office ID must be between 0 and 99";
}

if (!is_numeric($year)) {
    $errors['year'] = "Input should be a number";
} else if ($year > 2155 || $year < 1901) {
    $errors['year'] = "Year must be from 1901 to 2155.";
}

if (empty($errors)) {
    //first, use a query to check if the office exists
    $sql = "SELECT * FROM `office_names` WHERE Office_ID = {$office_ID}";
    $result = $connect->query($sql);
    if ($result->num_rows > 0) {
        //then, use a query to check if the year exists.
        if ($office_ID < 10)
            $office_ID = '0' . $office_ID;
        $code = $office_ID . $year;
        $year = $year . "-01-01";
        $sql = "SELECT * FROM `office_codes` WHERE Code = {$code}";
        $result2 = $connect->query($sql);
        if ($result2->num_rows <= 0) {
            $sql = $connect->prepare("INSERT INTO `office_codes` (`Code`, `Office_ID`, `Year`) VALUES (?, ?, ?)");
            $sql->bind_param('sis', $code, $office_ID, $year);
            if ($sql->execute() === FALSE) {
                $errors['sql'] = "Failed to create year.";
            }
        }
    } else {
        $errors['office_ID'] = "Office ID does not exist.";
    }
}

if (empty($errors)) {
    $data['success'] = True;
    $_SESSION['code'] = $code;
} else {
    $data['success'] = False;
    $data['errors'] = $errors;
}

$connect->close();

echo json_encode($data);
