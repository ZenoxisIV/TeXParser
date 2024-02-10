<?php
require_once 'includes/header.php';
?>

<script type="text/javascript" src="includes/nav.js"></script>

<!--note: DON'T INCLUDE A BODY TAG IN THIS DOCUMENT.
    Opening body tag is found in header.php,
    closing tag is found in footer.php-->

<div class="flex-grow-1" style="overflow-y: auto; overflow-x: hidden;">

<button id="generatePdfButton">Generate PDF</button>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script>
    $(document).ready(function() {
        $('#generatePdfButton').on('click', function() {
            // Make an AJAX request to generate the PDF
            $.ajax({
                url: './convertTEXtoPDF.php',
                type: 'POST',
                dataType: 'json',
                success: function(response) {
                    // Open the generated PDF in a new tab
                    window.open(response.filePath, '_blank');
                },
                error: function() {
                    alert('A fatal error occurred in executing dependencies.');
                }
            });
        });
    });
</script>

</div>


</div> <!--this ending tag closes the flexbox div started in the header. don't remove it.-->

<?php require_once 'includes/footer.php'; ?>