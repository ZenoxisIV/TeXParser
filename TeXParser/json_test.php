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

//$tables = ['cd_year', 'cd_usage', 'servers', 'pc_os', 'ws_os', 'server_os', 'automation_software', 'admin_systems', 'si_systems'];
$tables = ['databases'];

foreach ($tables as $table) {
    $sql = "SELECT * FROM $table WHERE Code = '991901'";
    $result = $connect->query($sql);

    if ($result->num_rows > 0) {
        // Fetch column names
        $fields_info = $result->fetch_fields();
        $columns = array();
        foreach ($fields_info as $field) {
            $columns[] = $field->name;
        }

        // Initialize output array
        $output[$table]['columns'] = $columns;
        
        // Fetch row data
        while ($row = $result->fetch_assoc()) {
            $output[$table]['rows'][] = array_values($row);
        }
    }
}

$connect->close();
echo json_encode($output);


