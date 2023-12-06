<?php
require_once 'includes/header.php';
require_once "php_action/db_connect.php";
?>

<script src="includes/nav.js"></script>

<link rel="stylesheet" href="./assets/css/homestyles.css">
<script src="includes/home.js"></script>


<!--note: DON'T INCLUDE A BODY TAG IN THIS DOCUMENT.
    Opening body tag is found in header.php,
    closing tag is found in footer.php-->

<?php
$_SESSION['tableName'] = "List of Offices";
$_SESSION['tableHeadings'] = ["Code", "ID", "Name"];
$_SESSION['tableRows'] = [];
?>

<div class="flex-grow-1" style="overflow-y: auto; overflow-x: hidden">
    <div class="col-11 mt-3 mx-auto">
        <div class="card card-table shadow mb-3">
            <div class="card-header bg-primary text-white sticky-header">
                <?php
                echo $_SESSION['tableName'];
                ?>
            </div>
            <div class="card-body">

                <div class="row">
                    <div class="col col-3 col-xxl-2">
                        <input type="text" class="form-control" placeholder="Search by Name" id="searchInput">
                    </div>
                    <div class="col col-auto">
                        <button class="btn bg-primary text-white" onclick="search()">Search</button>
                    </div>
                    <div class="col col-auto">
                        <button class="btn btn-light border-dark" data-bs-toggle="modal" data-bs-target="#checkboxModal">Show Columns</button>
                    </div>

                    <div class="col col-auto dropdown">
                        <button class="btn btn-light border-dark dropdown-toggle" id="dropdownBtn" data-bs-toggle="dropdown">Sort By...</button>
                        <ul class="dropdown-menu">
                            <li> <a href="#" class="dropdown-item" onclick="sortByName()">Sort by Name</a> </li>
                            <li> <a href="#" class="dropdown-item" onclick="sortByID()">Sort by ID</a> </li>
                        </ul>
                    </div>
                    <div class="d-none col col-auto dropdown" id="sortDirectionContainer">
                        <button class="btn btn-light border-dark dropdown-toggle" data-bs-toggle="dropdown"><span id="sortDirectionText">Choose...</span></button>
                        <ul class="dropdown-menu" id="sortDirectionDropdown">
                            <li> <a href="#" class="dropdown-item" onclick="setSortDirection('Ascending')">Ascending</a> </li>
                            <li> <a href="#" class="dropdown-item" onclick="setSortDirection('Descending')">Descending</a> </li>
                        </ul>
                    </div>

                </div>

                <div class="overlay" id="overlay"></div>
                <div class="table-container">
                    <table class="table table-bordered table-hover mx-auto" id="formChecklistTable">
                        <thead>
                            <tr>
                                <th scope="col" colspan="50" style="text-align: center;">Form Completion Checklist</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php

                            $columnsToCheck = [
                                'archiving', 'automation_software', 'cd_usage', 'cd_year',
                                'data_center', 'ict_issues', 'ict_projects', 'pc_os', 'security', 'servers',
                                'server_os', 'si_systems', 'special_solutions', 'ws_os'
                            ];

                            $sql = "SELECT Code, c.Office_ID, Name
                        FROM office_names AS n
                        JOIN office_codes AS c 
                        ON c.Office_ID = n.Office_ID";

                            $result = $connect->query($sql);

                            if ($result->num_rows > 0) {
                                echo "<tr>";

                                foreach ($_SESSION['tableHeadings'] as $heading) {
                                    echo "<th>" . $heading . "</th>";
                                }

                                foreach ($columnsToCheck as $column) {
                                    echo "<th class='column-$column'>$column</th>";
                                    $_SESSION['tableHeadings'][] = $column;
                                }

                                echo "</tr>";

                                $rows = [];
                                while ($row = $result->fetch_assoc()) {
                                    $code = $row["Code"];
                                    $officeId = $row["Office_ID"];
                                    $name = $row["Name"];

                                    $rowData = "<tr>
                                            <td>$code</td>
                                            <td>$officeId</td>
                                            <td>$name</td>";

                                    $singleRow = [$code, $officeId, $name];

                                    foreach ($columnsToCheck as $table) {
                                        $codeExists = checkCodeExistsInTable($connect, $table, $code);
                                        $entryMark = $codeExists == "Yes" ? "<span class='check-mark'>&#10004;</span>" : "<span class='cross-mark'>&#10060;</span>";
                                        $rowData .= "<td style='text-align: center; vertical-align: middle;' class='column-$table'><span>$entryMark</span></td>";

                                        $singleRow[] = $codeExists;
                                    }

                                    $rowData .= "</tr>";
                                    $rows[] = $rowData;

                                    array_push($_SESSION['tableRows'], $singleRow);
                                }

                                echo implode("", $rows); // Output all rows

                                echo "</table>";
                            } else {
                                echo "No records found.";
                            }

                            $connect->close();

                            function checkCodeExistsInTable($connect, $tableName, $code)
                            {
                                $sql = "SELECT COUNT(*) as count FROM $tableName WHERE Code = '$code'";
                                $result = $connect->query($sql);
                                $count = $result->fetch_assoc()['count'];
                                return $count > 0 ? "Yes" : "No";
                            }
                            ?>
                        </tbody>
                    </table>
                </div>
                <a class="mt-3 w-auto btn btn-success shadow-sm justify-content-center" href="./php_action/downloadReport.php">Download Report</a>
            </div>
        </div>
    </div>

    <script>
        // Event listeners
        document.getElementById("searchInput").addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                search();
            }
        });
    </script>
</div>

</div> <!--this ending tag closes the grid div started in the header. don't remove it.-->

<!-- modal-->
<div class="modal" id="checkboxModal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Select columns to show:</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <?php
                foreach ($columnsToCheck as $column) {
                    echo '<div class="form-check checkbox-container">';
                    echo '<input class="form-check-input" type="checkbox" id="' . $column . '" name="' . $column . '" checked>';
                    echo '<label class="form-check-label" for="' . $column . '">' . $column . '</label>';
                    echo '</div>';
                }
                ?>
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary" onclick="allCheckboxes()">Select All</button>
                <button class="btn btn-danger" onclick="clearCheckboxes()">Clear</button>
                <button class="btn btn-success" data-bs-dismiss="modal" onclick="show()">Apply</button>
            </div>
        </div>
    </div>
</div>

<?php require_once 'includes/footer.php'; ?>