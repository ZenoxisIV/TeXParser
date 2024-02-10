<?php
    shell_exec('python ./TeXParser/main.py');
    $latexFilePath = "./ICT_Inventory.tex";
    $output = compileLatex($latexFilePath);

    echo json_encode(['isSuccess' => true, 'filePath' => $output]);

    function compileLatex($filePath) {
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
            return $err->getMessage();
        }
    }