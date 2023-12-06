// Search function
function search() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toLowerCase();
    table = document.getElementById("formChecklistTable");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2]; // Search based from Name column
        if (td) {
            txtValue = td.textContent || td.innerText;
            tr[i].style.display = txtValue.toLowerCase().indexOf(filter) > -1 ? "table-row" : "none";
        }
    }
}

// Checkbox functions
function show() {
    var checkboxes = document.querySelectorAll('#checkboxModal input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        var columnClassName = 'column-' + checkbox.id;
        var columns = document.querySelectorAll('#formChecklistTable .' + columnClassName);
        columns.forEach(function (column) {
            column.style.display = checkbox.checked ? 'table-cell' : 'none';
        });
    });
}

function clearCheckboxes() {
    var checkboxes = document.querySelectorAll('.checkbox-container input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.checked = false;
    });
}

function allCheckboxes() {
    $('.checkbox-container input[type="checkbox"]').prop('checked', true)
}

// Sorting functions
function setSortDirection(direction) {
    document.getElementById("sortDirectionText").innerText = direction;
    applySorting(direction);
}

function applySorting(direction) {
    var currentSortingCriteria = document.getElementById("dropdownBtn").innerText;
    if (currentSortingCriteria === 'Sort by Name') {
        sortTable(2, direction);
    } else if (currentSortingCriteria === 'Sort by ID') {
        sortTable(1, direction);
    }
}

function sortByName() {
    showSortDirectionButton();
    document.getElementById("dropdownBtn").innerText = 'Sort by Name';
    var currentSortDirection = document.getElementById("sortDirectionText").innerText;
    if (currentSortDirection === "Ascending" || currentSortDirection === "Descending") {
        applySorting(currentSortDirection);
    } else {
        setSortDirection('Ascending');
        applySorting('Ascending');
    }
}

function sortByID() {
    showSortDirectionButton();
    document.getElementById("dropdownBtn").innerText = 'Sort by ID';
    var currentSortDirection = document.getElementById("sortDirectionText").innerText;
    if (currentSortDirection === "Ascending" || currentSortDirection === "Descending") {
        applySorting(currentSortDirection);
    } else {
        setSortDirection('Ascending');
        applySorting('Ascending');
    }
}

function showSortDirectionButton() {
    $("#sortDirectionContainer").removeClass('d-none')
}

function sortTable(columnIndex, sortDirection) {
    const tbl = document.getElementById("formChecklistTable").tBodies[0];
    var store = [];
    for (var i = 1, len = tbl.rows.length; i < len; i++) {
        var row = tbl.rows[i];
        var cellText = row.cells[columnIndex].textContent || row.cells[columnIndex].innerText;
        store.push([cellText, row]);
    }
    store.sort(function (x, y) {
        var a = x[0];
        var b = y[0];
        if (isNaN(a) || isNaN(b)) {
            return sortDirection === 'Ascending' ? a.localeCompare(b) : b.localeCompare(a);
        } else {
            return sortDirection === 'Ascending' ? parseInt(a) - parseInt(b) : parseInt(b) - parseInt(a);
        }
    });
    
    for (var i = 0, len = store.length; i < len; i++) {
        tbl.appendChild(store[i][1]);
    }
    
    store = null;
}