<?php
    $latexFilePath = "ICT_Inventory.tex";
    $logFilePath = "compile_log.txt";
    $pdfFilePath = compileLatex($latexFilePath, $logFilePath);
    echo json_encode(['success' => true, 'filePath' => $pdfFilePath]);

    function compileLatex($filePath, $logFilePath) {
        try {
            // Run pdflatex command and capture output and errors
            $command = "pdflatex -interaction=nonstopmode $filePath";
            exec($command, $output, $returnCode);
    
            if ($returnCode == 0) {
                // Delete generated .aux and .out files
                $baseFileName = pathinfo($filePath, PATHINFO_FILENAME);
                $filesToDelete = ["$baseFileName.aux", "$baseFileName.out"];
    
                foreach ($filesToDelete as $file) {
                    if (file_exists($file)) {
                        unlink($file);
                    }
                }
            }
    
            return "$baseFileName.pdf";
        } catch (Exception $err) {
            echo "Error compiling LaTeX file: {$err->getMessage()}\n";
            return 0;
        }
    }
?>