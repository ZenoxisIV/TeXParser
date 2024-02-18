<?php
    shell_exec('python ./TeXParser/main.py');
    $latexFilePath = "./ICT_Inventory.tex";
    $pdfFilePath= compileLatex($latexFilePath);

    if (is_null($pdfFilePath)) {        
        echo json_encode(['isSuccess' => false, 'filePath' => null]);
        throw new Exception('LaTeX file failed to compile.');
    }
    
    echo json_encode(['isSuccess' => true, 'filePath' => $pdfFilePath]);
    return;

    function compileLatex($filePath) {
        // Run pdflatex command and capture output and errors
        $command = "pdflatex -interaction=nonstopmode $filePath";
        exec($command, $unused, $returnCode);

        $baseFileName = null;

        if ($returnCode == 0) {
            exec($command); // Execute pdflatex again to generate .aux dependencies (e.g., table of contents, list of figures, last page number, etc.)
            $baseFileName = pathinfo($filePath, PATHINFO_FILENAME);

            // Delete generated .aux and .out files
            $filesToDelete = ["$baseFileName.aux", "$baseFileName.out"];
    
            deleteResidualFiles($baseFileName, $filesToDelete);
        }

        if (is_null($baseFileName)) {
            return null;
        }

        return "$baseFileName.pdf";
    }

    function deleteResidualFiles($baseFileName, $filesToDelete) {
        foreach ($filesToDelete as $file) {
            if (file_exists($file)) {
                unlink($file);
            }
        }
    }