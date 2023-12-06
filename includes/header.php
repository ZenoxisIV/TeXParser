<?php require_once 'php_action/core.php'; ?>

<!DOCTYPE html>
<html>

<head>
  <title>UPD ICT Database</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">
  <script
			  src="https://code.jquery.com/jquery-3.7.1.js"
			  integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4="
			  crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  <link href="./assets/css/custom.min.css" rel="stylesheet">
  <!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">-->
  <!--<link href="./assets/css/custom.min.css" rel="stylesheet">-->
</head>

<body>
  <!--navbar-->
  <div class="vh-100 vw-100">
    <nav class="navbar fixed-top navbar-dark bg-primary">
      <div class="container-fluid">
        <a href="#sidebar" data-bs-toggle="offcanvas">
          <button class="btn d-lg-none bg-primary btn-outline-light me-2">
            <i class="bi bi-list text-light"></i>
          </button>
        </a>
        <a class="navbar-brand" href="./home.php">
          <div class="d-none d-lg-block ms-2">
              <div class="row">
                <div class="col"><img style="width:50px" src="./assets/img/upd_logo.png" alt=""></div>
                <div class="col px-0">
                  <p class="my-0 fs-5 title">University of the Philippines Diliman</p>
                  <p class="my-0 fs-6">ICT Database System</p>
                </div>  
              </div>             
          </div>
        </a>
        <div class="dropdown ms-auto me-3">
          <a href="#" class="text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <strong>Admin</strong>
          </a>
          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
            <li><a class="dropdown-item" href="#">Settings</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" href="#logout_modal" data-bs-toggle="modal">Sign out</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- offcanvas, sidebar converts to offcanvas on smaller screens-->
    <div class="offcanvas offcanvas-start text-white bg-dark" tabindex="-1" id="sidebar">
      <ul class="nav nav-pills flex-column">
        <li class="nav-item align-end my-2 ms-auto me-2">
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="close"></button>
        </li>
      </ul>
      <hr>
    </div>

    <!-- logout modal -->
    <div class="modal fade" id="logout_modal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="logout-modal-title"> Are you sure? </h5>
            <button class="btn-close" data-bs-toggle="modal" aria-label="close"></button>
          </div>
          <div class="modal-footer">
            <a class="btn btn-danger" href="logout.php">Confirm</a>
            <button class="btn btn-light btn-outline-dark" data-bs-toggle="modal" data-bs-target="#logout_modal">Cancel</button>
          </div>
        </div>
      </div>
    </div>

    <!--sidebar + content-->
    <div class="h-100 d-flex flex-row" style="padding-top: 80px">
      <div class="d-lg-block d-none flex-shrink-0 p-3 text-light bg-dark" style="width: 300px; overflow: auto" id="nav-sidebar">
      </div>