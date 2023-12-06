<?php
session_start();
include("../includes/tcpdf/tcpdf.php");

// Make TCPDF object
$pdf = new TCPDF('L', 'mm', 'LEGAL');

// Modify default stuff
$pdf->SetAutoPageBreak(true);
$pdf->setPrintHeader(false);
$pdf->setPrintFooter(false);

// Add new page
$pdf->AddPage();

$pdf->Image('../assets/img/upd_logo_tp.png', null, null, 40, 0, '', '', 'B', true, 300, 'C', false, false);
$pdf->Ln(5);

// Add the content
$numColumns = count($_SESSION['tableHeadings']);
$numRows = count($_SESSION['tableRows']);
$colWidth = 315 / ($numColumns - 2);

$pdf->setFont('Helvetica', 'B', 14);
$pdf->setFillColor(136, 136, 136);
$pdf->Cell(335, 10, $_SESSION['tableName'], 1, 1, "C", true, '', 1);

$pdf->setFont('Helvetica', '', 8);
$pdf->setFillColor(204, 204, 204);
foreach ($_SESSION['tableHeadings'] as $column){
    if ($column == 'Code' || $column == 'ID'){
        $pdf->Cell(10, 5, $column, 1, 0, 'C', true, '', 1);
    } else {
    $pdf->Cell($colWidth, 5, $column, 1, 0, 'C', true, '', 1);
    }
}
$pdf->Ln();

$pdf->setFont('Helvetica', '', 7);
$pdf->setFillColor(240, 240, 240);
for ($i = 0; $i < $numRows; $i++){
    for ($j = 0; $j < $numColumns; $j++){
        if ($j == 0 || $j == 1){
            $pdf->Cell(10, 5, $_SESSION['tableRows'][$i][$j], 1, 0, 'C', true, '', 1);
        } else {
        $pdf->Cell($colWidth, 5, $_SESSION['tableRows'][$i][$j], 1, 0, 'C', true, '', 1);
        }
    }
    $pdf->Ln();
}

// Output the content
$pdf->Output();
?>
