import { Form } from './forms.js'

class Table extends Form {
    numRows = 0;
    isTable = true;
    constructor(title, colCount, formId, tableHeader, required, checkboxCols) {
        super(title, colCount, formId, required)
        this.tableHeader = tableHeader;
        this.buttons = [
            `delete-row-${this.formId}`,
            `submit-${this.formId}`
        ]
        this.checkboxCols = checkboxCols || Array(colCount).fill(false);
    }
    getSubmissionData(count) {
        //get all rows that got returned
        let form_data = {};
        form_data['formId'] = this.formId;
        for (let row = 0; row < count; row++) {
            for (let col = 0; col < this.colCount; col++) {
                let id = `${this.formId}-${row}-${col}`;
                let input = $(`#${id}`);
                let value = input.val();
                if (input.hasClass("form-check-input")) { //check if checkmark input
                    form_data[id] = (input.prop("checked")) ? 1 : 0; //non-system table
                }
                else if (value === "Others" && input.prop('tagName') === 'SELECT') //use the other field on others
                    form_data[id] = $(`#${this.formId}-${row}-other`).val();
                else
                    form_data[id] = value;
            }
        }
        return form_data;
    }
    parse(result, callback) {
        let data = JSON.parse(result);
        let elements = []
        for (const tuple of data['data']) {
            let row = $("<tr>", {});
            for (let i = 1; i < tuple.length; i++) {
                $("<td>", {}).html(`${tuple[i]}`).appendTo(row)
            }
            elements.push(row)
        }
        callback(elements)
    }
    getHTML() {
        const html =
            `<div class="card">
          <div class="card-body">
            <h5 class="card-title">${this.title}</h5>
            <form id="${this.formId}" method="POST">
              <div class="table-responsive">
                <table class="table table-bordered">` +
            this.tableHeader +
            `<tbody id="${this.formId}-body">
                  </tbody>
                  <tfoot id="${this.formId}-footer">
                  </tfoot>
                </table>
              </div>
              <button type=button class="btn btn-light border-dark ms-auto" id="add-row-${this.formId}"> Add row </button>
              <button type=button class="d-none btn btn-danger ms-auto" id="delete-row-${this.formId}"> Delete row </button>
              <button type=submit class="d-none btn btn-success ms-auto" id="submit-${this.formId}"> Submit </button>
            </form>
          </div>
        </div>`;
        return html;
    }
    resetRows() {
        if (this.numRows > 0)
            this.buttonToggle();
        this.numRows = 0;
    }
    addRow() {
        //adjust row count
        this.numRows++;
        if (this.numRows == 1)
            this.buttonToggle();
    }
    deleteRow() {
        if (this.numRows > 0) {
            this.numRows--;
            if (this.numRows == 0)
                this.buttonToggle();
            $(`#${this.formId}-body`).find("tr:last").remove();
        }
    }
    othersHandler(id, value, type) {
        if (type === "SELECT" && id.split('-').at(-1) === '0') {
            id = id.split('-').slice(0, -1).join("-") + "-other"
            if (value === "Others") {
                $(`#${id}`).removeClass('d-none')
                $(`#${id}`).prop('required', true)
            }
            else {
                $(`#${id}`).addClass('d-none')
                $(`#${id}`).prop('required', false)
            }
        }
    }
}

export class OptionTable extends Table {
    constructor(title, options, colCount, formId, tableHeader, required, checkboxCols) {
        super(title, colCount, formId, tableHeader, required, checkboxCols)
        this.options = options
    }
    addRow() {
        super.addRow()
        let rowIndex = this.numRows - 1;
        let option_html = '';
        $.each(this.options, function (_, option) {
            option_html += `<option value='${option}'>${option}</option>`;
        });
        let value_html = '';
        for (let col = 1; col < this.colCount; col++) {
            let required = (this.required[col]) ? "required" : "";
            if (this.checkboxCols[col])
                value_html += `<td style="text-align:center; padding-top:15px; padding-bottom: 1px"> <input class="form-check-input" style="transform: scale(2)" type="checkbox" value="1" id="${this.formId}-${rowIndex}-${col}"></td>`
            else
                value_html += `<td> <input type="text" class="form-control" placeholder="Value" id="${this.formId}-${rowIndex}-${col}" ${required}> </td>`;
        }
        const html = `
                <tr class="table-light">
                    <td>
                    <select class="form-select" id="${this.formId}-${rowIndex}-0" required>
                        <option value="" selected disabled hidden>Select</option>` +
            option_html +
            `
                    </select>
                    <input type="text" class="d-none form-control" placeholder="Value" id="${this.formId}-${rowIndex}-other">
                    </td>` +
            value_html +
            `
                </tr>
                `;
        $(`#${this.formId}-body`).append(html);
    }
}

export class SystemTable extends Table {
    constructor(title, colCount, formId, tableHeader, required, checkboxCols, optionCol = {}) {
        super(title, colCount, formId, tableHeader, required, checkboxCols)
        this.optionCol = optionCol
    }
    getSubmissionData(count) {
        //get all rows that got returned
        let form_data = {};
        form_data['formId'] = this.formId;
        for (let row = 0; row < count; row++) {
            for (let col = 0; col < this.colCount; col++) {
                let id = `${this.formId}-${row}-${col}`;
                let input = $(`#${id}`);
                let value = input.val();
                if (input.hasClass("form-check-input")) { //check if checkmark input
                    form_data[id] = (input.prop("checked")) ? 'Y' : 'N';
                }
                else if (value === "Others" && input.prop('tagName') === 'SELECT') //use the other field on others
                    form_data[id] = $(`#${this.formId}-${row}-other`).val();
                else
                    form_data[id] = value;

                if (col === this.colCount - 1) { //checks for a code 15
                    form_data[id] = value.trim();
                    form_data[`${this.formId}-${row}-6`] = (value === "15") ? $(`#${this.formId}-${row}-other`).val() : "";
                }
            }
        }
        return form_data;
    }
    addRow() {
        super.addRow()
        let rowIndex = this.numRows - 1;
        let value_html = '';
        for (let col = 0; col < this.colCount; col++) {
            let required = (this.required[col]) ? "required" : "";
            if (this.optionCol[col]) {
                value_html += `<td> <select class="form-select" id="${this.formId}-${rowIndex}-${col}" ${required}> <option value="" selected disabled hidden>Select</option>`
                let option_html = ``;
                for (const option of this.optionCol[col]) {
                    option_html += `<option value='${option}'>${option}</option>`;
                }
                value_html += option_html + `</select>`;
            }
            else if (this.checkboxCols[col])
                value_html += `<td style="text-align:center; padding-top:15px; padding-bottom: 1px"> <input class="form-check-input" style="transform: scale(2)" type="checkbox" value="1" id="${this.formId}-${rowIndex}-${col}">`
            else
                value_html += `<td> <input type="text" class="form-control" placeholder="Value" id="${this.formId}-${rowIndex}-${col}" ${required}>`;

            if (col == this.colCount - 1)
                value_html += `<input type="text" class="d-none form-control" placeholder="Value" id="${this.formId}-${rowIndex}-other">`

            value_html += `</td>`;
        }
        const html = `
                <tr class="table-light">` +
            value_html +
            `</tr>`;
        $(`#${this.formId}-body`).append(html);
    }
    setBodyHTML(elements) {
        let id = this.formId;
        $(`#${id}-body`).empty()
        for (const element of elements) {
            if (element.children().last().html() === "null")  //check if last column null
                element.children().last().remove()
            else
                element.children().eq(-2).remove() //if not, delete the 2nd to last column
        }
        $(`#${id}-body`).append(elements);
    }
    othersHandler(id, value, type) {
        if (id.split('-').at(-1) === '5') {
            id = id.split('-').slice(0, -1).join("-") + "-other"
            if (value === '15') {
                $(`#${id}`).removeClass('d-none')
                $(`#${id}`).prop('required', true)
            }
            else {
                $(`#${id}`).addClass('d-none')
                $(`#${id}`).prop('required', false)
            }
        }
    }
}

export class SSTable extends Table {
    constructor(title, colCount, formId, tableHeader, required, checkboxCols, optionCol = {}, otherCol = {}) {
        super(title, colCount, formId, tableHeader, required, checkboxCols)
        this.optionCol = optionCol
        this.otherCol = otherCol
    }
    getSubmissionData(count) {
        //get all rows that got returned
        let form_data = {};
        form_data['formId'] = this.formId;
        for (let row = 0; row < count; row++) {
            for (let col = 0; col < this.colCount; col++) {
                let id = `${this.formId}-${row}-${col}`;
                let input = $(`#${id}`);
                let value = input.val();
                if (input.hasClass("form-check-input")) { //check if checkmark input
                    form_data[id] = (input.prop("checked")) ? 'Y' : 'N';
                }
                else if (value === "Others" && input.prop('tagName') === 'SELECT') //use the other field on others
                    form_data[id] = $(`#${this.formId}-${row}-other`).val();
                else
                    form_data[id] = value;

                if (col === this.colCount - 1) { //checks for a code 15
                    form_data[id] = value.trim();
                    form_data[`${this.formId}-${row}-6`] = (value === "15") ? $(`#${this.formId}-${row}-other`).val() : "";
                }
            }
        }
        return form_data;
    }
    addRow() {
        super.addRow()
        let rowIndex = this.numRows - 1;
        let value_html = '';
        for (let col = 0; col < this.colCount; col++) {
            let required = (this.required[col]) ? "required" : "";
            if (this.optionCol[col]) {
                value_html += `<td> <select class="form-select" id="${this.formId}-${rowIndex}-${col}" ${required}> <option value="" selected disabled hidden>Select</option>`
                let option_html = ``;
                for (const option of this.optionCol[col]) {
                    option_html += `<option value='${option}'>${option}</option>`;
                }
                value_html += option_html + `</select>`;
            }
            else if (this.checkboxCols[col])
                value_html += `<td style="text-align:center; padding-top:15px; padding-bottom: 1px"> <input class="form-check-input" style="transform: scale(2)" type="checkbox" value="1" id="${this.formId}-${rowIndex}-${col}">`
            else
                value_html += `<td> <input type="text" class="form-control" placeholder="Value" id="${this.formId}-${rowIndex}-${col}" ${required}>`;

            if (this.otherCol[col])
                value_html += `<input type="text" class="d-none form-control" placeholder="Value" id="${this.formId}-${rowIndex}-${col}-other">`

            value_html += `</td>`;
        }
        const html = `
                <tr class="table-light">` +
            value_html +
            `</tr>`;
        $(`#${this.formId}-body`).append(html);
    }
    setBodyHTML(elements) {
        let id = this.formId;
        $(`#${id}-body`).empty()
        for (const element of elements) {
            if (element.children().last().html() === "null")  //check if last column null
                element.children().last().remove()
            else
                element.children().eq(-2).remove() //if not, delete the 2nd to last column
        }
        $(`#${id}-body`).append(elements);
    }
    othersHandler(id, value, type) {
        let col = id.split('-').at(-1)
        if (this.otherCol[col]) {
            id += "-other"
            if (value === this.otherCol[col]) {
                $(`#${id}`).removeClass('d-none')
                $(`#${id}`).prop('required', true)
            }
            else {
                $(`#${id}`).addClass('d-none')
                $(`#${id}`).prop('required', false)
            }
        }
    }
}