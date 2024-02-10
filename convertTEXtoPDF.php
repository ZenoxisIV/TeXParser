<?php
    shell_exec('python ./TeXParser/main.py');
    $latexFilePath = "./ICT_Inventory.tex";
    $output = compileLatex($latexFilePath);

    echo json_encode(['isSuccess' => true, 'filePath' => $output]);

    function compileLatex($filePath) {
        // Run pdflatex command and capture output and errors
        $command = "pdflatex -interaction=nonstopmode $filePath";
        exec($command, $output, $returnCode);

        if ($returnCode == 0) {
            exec($command); // Execute pdflatex again to generate .aux dependencies (e.g., table of contents, list of figures, last page number, etc.)
            $baseFileName = pathinfo($filePath, PATHINFO_FILENAME);

            // Delete generated .aux and .out files
            $filesToDelete = ["$baseFileName.aux", "$baseFileName.out"];
    
            deleteResidualFiles($filePath, $baseFileName, $filesToDelete);
        }

        return "$baseFileName.pdf";
    }

    function deleteResidualFiles($filePath, $baseFileName, $filesToDelete) {
        foreach ($filesToDelete as $file) {
            if (file_exists($file)) {
                unlink($file);
            }
        }
    }