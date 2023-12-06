<?php
require_once 'includes/header.php';

?>

<script>
  for (const id of ['sidebar', 'nav-sidebar']) {
    //CHANGE THIS TO THE NAVIGATION PANE OF YOUR WEBPAGE.
    let html = `
    <ul class="nav nav-pills flex-column">
      <li class="nav-item">
        <a href="./home.php" class="nav-link text-white" aria-current="page">
          <i class="bi bi-house-door-fill me-4"></i> 
          Home
        </a>
      </li>
      <li class="nav-item">
        <a href="./form.php" class="nav-link text-white active" aria-current="page">
        <i class="bi bi-input-cursor-text me-4"></i>
          Form
        </a>
      </li>
      <hr>
    </ul>
    <ul class="nav nav-pills flex-column" ${(id == 'nav-sidebar') ? `id='nav-content'` : ''}>
    `
    const nav = {
      'hardware' : 'Hardware',
      'software' : 'Software',
      'networkSection' : 'Network',
      'securitySection' : 'Security, Disaster Recovery, & Back-up',
      'archivingSection' : 'Data Archiving',
      'specialSolutions' : 'Special Solutions and Other Services',
      'datacenter' : 'Data Center',
      'ict' : 'ICT Projects'
    }

    for (const key in nav) {
      html += 
      `<li>
        <a href="#${key}" class="nav-link text-white ps-4">
          ${nav[key]}
        </a>
      </li>`
    }
    html += `</ul>`
    document.getElementById(id).insertAdjacentHTML('beforeEnd', html);
  }
</script>


<!--note: DON'T INCLUDE A BODY TAG IN THIS DOCUMENT.
    Opening body tag is found in header.php,
    closing tag is found in footer.php-->

<div data-bs-spy="scroll" data-bs-target="#nav-content" class="flex-grow-1 position-relative" style="overflow-y: auto; overflow-x: hidden">
  <!--insert your site body code here.-->
  <div id="form" class="col-11 mt-3 mx-auto">
    <h3> Form data | Currently: <span id="current-code">
        <?php
        if (isset($_SESSION['code'])) {
          $code = $_SESSION['code'];
          $office = substr($code, 0, 2);
          $year = substr($code, 2, 6);
          echo "Office: <span class='text-success'> {$office}</span>, Year: <span class='text-success'> {$year}</span>";
        } else
          echo "<span class='text-danger'> Unset </span>";
        ?>
      </span>
    </h3>
    <form id="form_data" method="POST">
      <div class="row align-items-end">
        <div class="col col-lg-2 col-xxl-1 col-sm-auto">
          <label for="office_ID" class="form-label">Office ID</label>
          <input type="text" class="form-control" id="office_ID" name="office_ID" required>
        </div>
        <div class="col col-lg-3 col-xxl-2 col-sm-auto">
          <label for="Year" class="form-label">Year</label>
          <input type="text" class="form-control" id="year" name="year" required>
        </div>
        <div class="col col-sm-auto">
          <button type="submit" class="btn btn-success">Submit</button>
        </div>
      </div>
    </form>
    <hr>
    <div id="hardware">
      <h3> Hardware </h3>
    </div>
    <hr>
    <div id="software">
      <h3> Software </h3>
    </div>
    <hr>
    <div id="networkSection">
      <h3> Network </h3>
    </div>
    <hr>
    <div id="securitySection">
      <h3> Security, Disaster Recovery, & Back-up </h3>
    </div>
    <hr>
    <div id="archivingSection">
      <h3> Data Archiving </h3>
    </div>
    <hr>
    <div id="specialSolutions">
      <h3> Special Solutions and Other Services </h3>
    </div>
    <hr>
    <div id="datacenter">
      <h3> Data Center </h3>
    </div>
    <hr>
    <div id="ict">
      <h3> ICT Projects </h3>
    </div>
    <hr>
  </div>

</div> <!--this ending tag closes the flexbox div started in the header. don't remove it.-->

<!-- status modal-->
<div class="modal" tabindex="-1" id="status">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Error</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<script type="module" src="./form_submit/form.js">
</script>

<?php require_once 'includes/footer.php'; ?>