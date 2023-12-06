for (const id of ['sidebar', 'nav-sidebar']) {
    //CHANGE THIS TO THE NAVIGATION PANE OF YOUR WEBPAGE.
    const html = `
    <ul class="nav nav-pills flex-column">
      <li class="nav-item">
        <a href="./home.php" class="nav-link active" aria-current="page">
          <i class="bi bi-house-door-fill me-4"></i> 
          Home
        </a>
      </li>
      <li class="nav-item">
        <a href="./form.php" class="nav-link text-white" aria-current="page">
        <i class="bi bi-input-cursor-text me-4"></i>
          Form
        </a>
      </li>
      <hr>
      <li>
        <a href="./template.php" class="nav-link text-white">
          <i class="bi bi-file-spreadsheet-fill me-4"></i> 
          Reports Viewing
        </a>
      </li>
      <li>
        <a href="./template.php" class="nav-link text-white">
          <i class="bi bi-laptop-fill me-4"></i> 
          Manage Equipment
        </a>
      </li>
      <li>
        <a href="./template.php" class="nav-link text-white">
          <i class="bi bi-file-earmark-code-fill me-4"></i> 
          Manage System Metadata
        </a>
      </li>
    </ul>
    `
    const sidebar = document.getElementById(id);
    sidebar.insertAdjacentHTML('beforeend', html);
  }