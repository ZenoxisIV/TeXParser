<?php

require_once '../php_action/core.php';
if (isset($_SESSION['code'])) {
    echo json_encode($_SESSION['code']);
} else
    echo null;
?>