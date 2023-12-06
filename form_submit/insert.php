<?php

require_once '../php_action/core.php';
class Table
{
    protected $formId;
    protected $tableId;
    protected $colCount;
    protected $columns;
    protected $rowCount;

    public function __construct($formId, $columns)
    {
        $this->formId = $formId;
        $this->tableId = str_replace("-", "_", $formId);

        $this->colCount = count($columns) - 1;
        $this->columns = $columns;
    }
    public function columns()
    {
        $columns = $this->columns;
        for ($i = 0; $i < count($columns); $i++) {
            if ($i != count($columns) - 1)
                $columns[$i] = '`' . $this->columns[$i] . "`, ";
            else
                $columns[$i] = '`' . $this->columns[$i] . "`";
        }
        return join("", $columns);
    }
    public function setRowCount()
    {
        $data = [];
        $count = 0;
        while (isset($_POST[$this->formId . "-{$count}-0"])) {
            $id = $this->formId . "-{$count}-0";
            $data[] = $id;
            $count++;
        }
        $this->rowCount = $count;
    }
    protected function baseValidate()
    {
        if (!isset($_SESSION['code'])) {
            $errors['code'] = "Office ID and form year not set.";
        } else if ($this->rowCount < 1) {
            $errors['count'] = "Rows not retrieved.";
        }
    }
    public function submitData($connect, $errors)
    {
        if (empty($errors)) {
            //query an insert
            $data = [];
            $code = $_SESSION['code'];
            $sql = "INSERT INTO `{$this->tableId}` ({$this->columns()}) VALUES ('{$code}', ";
            for ($row = 0; $row < $this->rowCount; $row++) {
                if ($row > 0)
                    $sql = $sql . ", ('{$code}', ";
                for ($col = 0; $col < $this->colCount; $col++) {
                    $val = $_POST[$this->formId . "-{$row}-{$col}"];
                    $data[$val] = $val;
                    if (empty($val) || !isset($val)) //check if set
                        if ($val == 0)
                            $attr = 0;
                        else
                            $attr = "NULL";
                    else {
                        //if set, check if numeric AND not a use code
                        if (is_numeric($val) && ($col !== $this->colCount - 1 && get_class($this) !== "SystemTable"))
                            $attr = (int) $val;
                        else
                            $attr = "'" . $val . "'";
                    }
                    if ($col == $this->colCount - 1)
                        $sql = $sql . "{$attr}";
                    else
                        $sql = $sql . "{$attr}, ";
                }
                $sql = $sql . ")";
            }
            //$data['sql'] = $sql;
            if ($connect->query($sql) === FALSE) {
                $errors['sql'] = "Failed to insert entries";
            }
        }
        if (empty($errors)) {
            $data['success'] = True;
        } else {
            $data['success'] = False;
            $data['errors'] = $errors;
        }
        $data['formId'] = $this->formId;
        $data['count'] = $this->rowCount;

        echo json_encode($data);
    }
}

class OSTable extends Table
{
    public function validate()
    {
        $errors = parent::baseValidate();
        if (!empty($errors))
            return $errors;

        for ($row = 0; $row < $this->rowCount; $row++) {
            if (
                ($_POST[$this->formId . "-{$row}-1"] == 0 && empty($_POST[$this->formId . "-{$row}-2"])) ||
                ($_POST[$this->formId . "-{$row}-1"] == 1 && !empty($_POST[$this->formId . "-{$row}-2"]))
            )
                $errors['values'] = "Please choose one option: either select lifetime license or input a year.";
            else if ($_POST[$this->formId . "-{$row}-1"] == 0) {
                if (!is_numeric($_POST[$this->formId . "-{$row}-2"])) {
                    $errors['values'] = "Expiry year must be numeric.";
                } else if ($_POST[$this->formId . "-{$row}-2"] < 1901 || $_POST[$this->formId . "-{$row}-2"] > 2155) {
                    $errors['values'] = "Expiry year must be a valid year (from 1901 to 2155)";
                }
            }
        }
        return $errors;
    }
}

class HardwareTable extends Table
{
    public function validate()
    {
        $errors = parent::baseValidate();
        if (!empty($errors))
            return $errors;

        for ($row = 0; $row < $this->rowCount; $row++) {
            $atLeastOneValue = false;
            if (strlen($_POST[$this->formId . "-{$row}-0"]) > 100)
                $errors['types'] = "Type must be less than 100 characters.";
            for ($col = 1; $col < $this->colCount; $col++) {
                if (!empty($_POST[$this->formId . "-{$row}-{$col}"])) {
                    $value = $_POST[$this->formId . "-{$row}-{$col}"];
                    $atLeastOneValue = true;
                    if (!is_numeric($value)) {
                        $errors['values'] = "Values must be numeric.";
                    } else if ($value < 0 || $value > 999999) {
                        $errors['values'] = "Values must be positive (up to 6 digits).";
                    }
                }
            }
            if (!$atLeastOneValue)
                $errors['values'] = "Please fill at least one value per row";
        }

        return $errors;
    }
}

class SystemTable extends Table
{
    public function validate()
    {
        $errors = parent::baseValidate();
        $useCodes = range(1, 15);
        if (!empty($errors))
            return $errors;

        for ($row = 0; $row < $this->rowCount; $row++) {
            $baseId = $this->formId . "-{$row}-";
            if (strlen($_POST[$baseId . "0"]) > 30)
                $errors['name'] = "Name must be less than 30 characters.";

            if ($this->formId == "databases" && strlen($_POST[$baseId . "2"]) > 100)
                $errors['desc'] = "Description must be less than 100 characters.";
            else if (strlen($_POST[$baseId . "2"]) > 30)
                $errors['platform'] = "Platform must be less than 30 characters.";

            if ($this->formId == "databases" && strlen($_POST[$baseId . "3"]) > 30)
                $errors['software'] = "Software must be less than 30 characters.";

            if (!is_numeric($_POST[$baseId . "4"]))
                $errors['cost'] = "Maintenance cost must be a number.";
            else if ($_POST[$baseId . "4"] > 999999.99 || $_POST[$baseId . "4"] < 0)
                $errors['cost'] = "Maintenance cost either too large or too small.";

            if ($_POST[$baseId . "5"] == 15 && strlen($_POST[$baseId . "6"]) > 30)
                $errors['use'] = "Others should be 30 characters or less.";
            else {
                foreach (explode(',', $_POST[$baseId . "5"]) as $code) {
                    if (!in_array($code, $useCodes))
                        $errors['use'] = "Use codes must be comma-separated use codes.";
                    break;
                }
            }
        }
        return $errors;
    }
}

class Form extends Table
{
    public function validate()
    {
        return [];
    }
    public function setRowCount()
    {
        $this->rowCount = 1;
    }
    public function submitData($connect, $errors)
    {
        if (empty($errors)) {
            //query an insert
            $data = [];
            $code = $_SESSION['code'];
            $sql = "INSERT INTO `{$this->tableId}` ({$this->columns()}) VALUES ('{$code}', ";
            $colCount = (isset($_POST['hasOther'])) ? $this->colCount - count($_POST['hasOther']) : $this->colCount;
            for ($col = 0; $col < $colCount; $col++) {
                if (isset($_POST[$this->formId . "-0-{$col}"])) {
                    $val = $_POST[$this->formId . "-0-{$col}"];
                    $data[$val] = $val;
                    if (empty($val)) //check if empty
                        $attr = ($val == 0) ? 0 : "NULL";
                    else {
                        //if set, check if numeric
                        if (is_numeric($val))
                            $attr = (int) $val;
                        else
                            $attr = "'" . $val . "'";
                    }
                } else {
                    $attr = "NULL";
                }
                if ($col == $colCount - 1)
                    $sql = $sql . "{$attr}";
                else
                    $sql = $sql . "{$attr}, ";
                if (isset($_POST['hasOther']) && in_array($col, $_POST['hasOther'])) {
                    $val = (isset($_POST[$this->formId . "-0-{$col}-other"])) ? "'" . $_POST[$this->formId . "-0-{$col}-other"] . "'" : "";
                    $attr = (empty($val)) ? "NULL" : $val;
                    if ($col == $colCount - 1)
                        $sql = $sql . "{$attr}";
                    else
                        $sql = $sql . "{$attr}, ";
                }
            }
            $sql = $sql . ")";
            //$data['sql'] = $sql;
            if ($connect->query($sql) === FALSE) {
                $errors['sql'] = "Failed to insert entries";
            }
        }
        if (empty($errors)) {
            $data['success'] = True;
        } else {
            $data['success'] = False;
            $data['errors'] = $errors;
        }
        $data['formId'] = $this->formId;
        $data['count'] = $this->rowCount;

        echo json_encode($data);
    }
}

define("HARDWARE", [
    'cd-year',
    'cd-usage',
    'servers'
]);

define("OS", [
    'pc-os',
    'ws-os',
    'server-os',
    'automation-software',
]);

define("SYSTEM", [
    'admin-systems',
    'si-systems',
    'databases'
]);

define("FORMS", [
    'network',
]);

define("COLUMNS", [
    'cd-year' => array('Code', 'CD_Type', 'Owned_1y', 'Leased_1y', 'Owned_2y', 'Leased_2y', 'Owned_3y', 'Leased_3y', 'More'),
    'cd-usage' => array('Code', 'CD_Type', 'Employees', 'Training', 'Frontline', 'General', 'Projects'),
    'servers' => array('Code', 'Capacity', 'In-house', 'Co-located'),
    'pc-os' => array('Code', 'PC_OS_Name', 'Lifetime', 'Expiration'),
    'ws-os' => array('Code', 'WS_OS_Name', 'Lifetime', 'Expiration'),
    'server-os' => array('Code', 'Server_OS_Name', 'Lifetime', 'Expiration'),
    'automation-software' => array('Code', 'Software', 'Lifetime', 'Expiration'),
    'admin-systems' => array('Code', 'Admin_System', 'Own_Property', 'Platform', 'Environment', 'Maintenance_Cost', 'Use_Codes', 'Use_other'),
    'si-systems' => array('Code', 'SI_System', 'Own_Property', 'Platform', 'Environment', 'Maintenance_Cost', 'Use_Codes', 'Use_other'),
    'databases' => array('Code', 'DB_Name', 'Own_Property', 'Description', 'DB_Software', 'Maintenance_Cost', 'Use_Codes', 'Use_other'),
    'network' => array('Code', 'LAN', 'Intranet', 'VPN', 'WAN', 'PABX_PBX', 'PBX_Setup', 'Internet', 'MOA', 'MOA_Other', 'ISPs', 'Bandwidth', 'Employee_net', 'Employee_mail', 'Website', 'URL')
]);

$formId = $_POST['formId'];
if (in_array($formId, HARDWARE)) {
    $table = new HardwareTable($formId, COLUMNS[$formId]);
} else if (in_array($formId, OS)) {
    $table = new OSTable($formId, COLUMNS[$formId]);
} else if (in_array($formId, SYSTEM)) {
    $table = new SystemTable($formId, COLUMNS[$formId]);
} else if (in_array($formId, FORMS)) {
    $table = new Form($formId, COLUMNS[$formId]);
}
if (!isset($_SESSION['code'])) {
    $data = [];
    $data['errors'][] = "Office ID and form year not set.";
    echo json_encode($data);
}
else if (isset($table)) {
    $table->setRowCount();
    $table->submitData($connect, $table->validate());
    unset($table);
} else {
    $data = [];
    $data['errors'][] = "Table not found on server.";
    echo json_encode($data);
}
