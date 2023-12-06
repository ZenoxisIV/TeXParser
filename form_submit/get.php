<?php

require_once '../php_action/core.php';
if (isset($_SESSION['code']) && isset($_POST['form'])) {
    $sql = "SELECT * FROM `{$_POST['form']}` WHERE Code = '{$_SESSION['code']}'";
    $result = $connect->query($sql);

    $output = array('data' => array());

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $output['data'][] = array_values($row);
        }
    }

    $connect->close();
    echo json_encode($output);
} else
    echo null;
?>
