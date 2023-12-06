export class Form {
    constructor(title, colCount, formId, required) {
        this.title = title;
        this.colCount = colCount;
        this.formId = formId;
        this.buttons = [
            `delete-${this.formId}`,
            `submit-${this.formId}`
        ]
        this.required = required;
    }
    buttonToggle() {
        $.each(this.buttons, function (_, buttonId) {
            let button = $(`#${buttonId}`)
            if (button.hasClass(`d-none`))
                button.removeClass(`d-none`);
            else
                button.addClass(`d-none`);
        });
    }
    addCheckbox(col, title) {
        return `
        <div class="row mb-1">
          <div class="col col-11 col-md-9 col-xxl-7">
            <label class="form-check-label" for="${this.formId}-${col}">${title}</label>
          </div>
          <div class="col">
            <input class="form-check-input border border-dark" id="${this.formId}-${col}" style="height: 20px; width: 20px" type="checkbox" value="">
          </div>
        </div>
        `
    }
    addValue(col, title) {
        let required = (this.required[col]) ? "required" : "";
        return `
        <div class="row">
          <div class="col col-11 col-md-8 col-xxl-6">
            <label class="form-check-label" for="${this.formId}-${col}">${title}</label>
          </div>
          <div class="col">
            <input class="form-control" placeholder="Value" id="${this.formId}-${col}" type="text" ${required}>
          </div>
        </div>
        `
    }
    addMultiselectGrouped(col, title, titles) {
        let required = (this.required[col]) ? "required" : "";
        let html = `
        <div class="row">
        <div class="row"><p class="m-0"> ${title} </p></div>
        <div class="row align-items-center mb-2">`
        let keys = Object.keys(titles)
        let values = Object.values(titles)
        for (let i = 0; i < values.length; i++) {
            html += `
            <div class="col-auto">
                <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${i}" style="height: 20px; width: 20px" type="checkbox" value="${(isNaN(keys[i])) ? keys[i] : values[i]}">
                <label class="form-check-label" for="${this.formId}-${col}-${i}"> ${values[i]} </label>
            </div>`
            if (i < (values.length / 2) - 1) {

            }
        }
        html += `
        <div class="col-auto">
        <input class="form-control" name="${this.formId}-${col}" style="width: 100px" placeholder="Other" id="${this.formId}-${col}-${values.length}" type="text">
        </div>
        </div>
        </div>
    `
        return html
    }
    addMultiselectArranged(col, title, titles) {
        let html = `<div class="row"><div class="row"><p class="m-0"> ${title} </p></div>`
        let keys = Object.keys(titles)
        let values = Object.values(titles)
        if (values.length % 2 !== 0) {
            for (let i = 0; i < values.length / 2; i++) {
                let j = i + Math.ceil(values.length / 2)
                html += `
            <div class="row align-items-center mb-2">
                <div class="col-6">
                <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${i}" style="height: 20px; width: 20px" type="checkbox" value="${(isNaN(keys[i])) ? keys[i] : values[i]}">
                <label class="form-check-label" for="${this.formId}-${col}-${i}"> ${values[i]} </label>
                </div>`
                if (i < (values.length / 2) - 1) {
                    html += `<div class="col-6">
                <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${j}" style="height: 20px; width: 20px" type="checkbox" value="${(isNaN(keys[j])) ? keys[j] : values[j]}">
                <label class="form-check-label" for="${this.formId}-${col}-${j}"> ${values[j]} </label>
                </div>
            </div>`
                }
            }
            html += `
            <div class="col-auto">
            <input class="form-control" name="${this.formId}-${col}" placeholder="Other" id="${this.formId}-${col}-${values.length}" type="text">
            </div>
            </div>
            </div>
            `
        } else {
            for (let i = 0; i < values.length / 2; i++) {
                let j = i + Math.floor(values.length / 2)
                html += `
                <div class="row align-items-center mb-2">
                    <div class="col-6">
                        <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${i}" style="height: 20px; width: 20px" type="checkbox" value="${(isNaN(keys[i])) ? keys[i] : values[i]}">
                        <label class="form-check-label" for="${this.formId}-${col}-${i}"> ${values[i]} </label>
                    </div>
                    <div class="col-6">
                        <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${j}" style="height: 20px; width: 20px" type="checkbox" value="${(isNaN(keys[j])) ? keys[j] : values[j]}">
                        <label class="form-check-label" for="${this.formId}-${col}-${j}"> ${values[j]} </label>
                    </div>
                </div>`
            }
            html += `
            <div class="row">
                <div class="col-11">
                    <input class="form-control" name="${this.formId}-${col}" placeholder="Other" id="${this.formId}-${col}-${values.length}" type="text">
                </div>
            </div>
            </div>
            `
        }
        return html
    }
    addRadio(col, title, titles) {
        let required = (this.required[col]) ? "required" : "";
        let html = `
            <div class="row">
              <div class="col col-11 col-md-9 col-xxl-7">
                <p> ${title} </p>
              </div>
              <div class="col input-group">
            `
        let keys = Object.keys(titles)
        let values = Object.values(titles)
        for (let i = 0; i < values.length; i++) {
            html += `
                <div class="form-check me-3">
                      <input class="form-check-input border border-dark" name="${this.formId}-${col}" id="${this.formId}-${col}-${i}" style="height: 20px; width: 20px" type="radio" value="${(isNaN(keys[i])) ? keys[i] : values[i]}" ${required}>
                      <label class="form-check-label" for="${this.formId}-${col}-${i}"> ${values[i]} </label>
                    </div>
                `
        }
        html += `
                </div>
                </div>`
        return html
    }
    setBodyHTML(elements) {
        let id = this.formId;
        $(`#${id}-body`).empty()
        $(`#${id}-body`).append(elements);
    }
    getSubmissionData(hasOther) {
        let form_data = {}
        form_data["formId"] = this.formId;
        form_data["hasOther"] = hasOther;
        for (let col = 0; col < this.colCount; col++) {
            let row = $(`#${this.formId}`).children().eq(col)
            let id = `${this.formId}-${col}`;
            let rowId = `${this.formId}-0-${col}` //logic on server-side php requires a row number
            if (!row.hasClass('d-none')) {
                if ($(`#${id}`).length !== 1) { //must be a radio or a multi-checkbox 
                    if ($(`input[name='${id}']`).prop('type') === 'checkbox') {
                        //multi-checkbox
                        let inputs = []
                        console.log(`[name='${id}']`)
                        $(`input[name='${id}']:checked`).each(function () {
                            inputs.push($(this).val())
                        })
                        form_data[rowId] = inputs.join(',').trim()
                        let other = $(`input[type='text'][name='${id}']`).val()
                        if (other)
                            form_data[`${rowId}-other`] = other;
                    }
                    else
                        form_data[rowId] = $(`input[type='radio'][name='${id}']:checked`).val() //radio
                }
                else if ($(`#${id}`).prop("type") === 'checkbox')
                    form_data[rowId] = ($(`#${id}`).prop("checked")) ? 1 : 0;
                else
                    form_data[rowId] = $(`#${id}`).val();
            } else if ($(`#${id}`).prop("type") === 'checkbox') {
                form_data[rowId] = 0;
            }
        }
        console.log(form_data)
        return form_data;
    }
    parse(result, callback) {
        if (result && JSON.parse(result)['data'][0]) {
            callback(JSON.parse(result)['data'][0]);
        } else {
            $(`#${this.formId}`).find(`input`).prop('disabled', false)
            $(`#${this.formId}`).find(`input[type='checkbox'],input[type='radio']`).prop('checked', false)
            $(`#${this.formId}`).find(`input[type='text']`).val("")
            this.checkboxChecker();
            if ($(`#submit-${this.formId}`).hasClass('d-none')) 
                this.buttonToggle();
        }
    }
    checkboxChecker() {
        for (let i = 0; i < this.colCount; i++) {
            this.checkboxChecker(`${this.formId}-${i}`)
        }
    }
}

export class NetworkForm extends Form {
    hasOther = [7];
    constructor(title, colCount, formId, required) {
        super(title, colCount, formId, required)
    }
    getHTML() {
        let html = `
            <div class="card">
                <div class="card-body">
                    <form id="${this.formId}" method="POST">`
        let col = 0;
        let titles = [
            "Does your agency have a Local Area Network (LAN?)",
            "Does your agency have an Intranet?",
            "If yes, does your agency have a Virtual Private Network (VPN)?",
            'Does your agency have a Wide Area Network (WAN)?',
            "Does your agency have a Private Automatic Branch Exchange (PABX or PBX)?",
        ];
        for (; col < 5; col++) {
            html += this.addCheckbox(col, titles[col])
        }
        titles = ["Private", "Hosted", "VoIP PBX or IP-PBX", "Hosted IP"]
        html += this.addRadio(col, "If yes, what is the PBX set up?", titles)
        col++
        html += this.addCheckbox(col, "Is your agency connected to the Internet?")
        col++
        titles = ['Dial-up', 'Leased line', 'WiFi', 'DSL', 'Mobile phone', 'ISDN', 'Satellite']
        html += this.addMultiselectGrouped(col, "What is/are your agency’s mode/s of access to the Internet? (Check all items that are applicable)", titles)
        col++;
        titles = [
            "Who is (are) your Internet Service Provider(s)?",
            "What is the combined internet bandwidth (voice and data)?",
            "How many employees have access to the Internet in the office?",
            "How many employees have their own official e-mail address?"
        ];
        for (; col < 12; col++) {
            html += this.addValue(col, titles[col - 8])
        }
        html += this.addCheckbox(col, "Does your agency have a web site?")
        html += this.addValue(col + 1, "If YES, what is the URL of your agency’s web site?")
        html += `
            <button type=submit class="btn btn-success ms-auto" id="submit-${this.formId}"> Submit </button>
            <button type=button class="d-none btn btn-danger ms-auto" id="delete-${this.formId}"> Delete </button>
          </form>
        </div>
        </div>`;
        return html;
    }
    setBodyHTML(data) {
        console.log(data)
        $(`#${this.formId}`).children('div').removeClass('d-none')
        $(`#${this.formId}`).find(`input`).prop('disabled', true)
        let counter = 0;
        let maxCol = 15;
        let offset = 1
        while (counter < maxCol) {
            let col = counter + offset;
            let id = `#${this.formId}-${counter}`
            if ($(id).prop('type') === "checkbox") {
                if (data[col] === '1')
                    $(id).prop('checked', true)
                else
                    $(id).prop('checked', false)
            } else if ($(id).prop('type') === "text") {
                $(id).val(data[col] || "NULL") 
            } else {//either a radio or a multiselect
                let strings = (data[col]) ? data[col].split(',') : [];
                for (const string of strings) {
                    $(`input[type='checkbox'][value='${string}']`).prop('checked', true)
                }
                
            }
            if (this.hasOther.includes(counter)) {
                $(`input[type='text'][name='${this.formId}-${counter}']`).val(data[col + 1] || "NULL")
                maxCol--;
                offset++
            }
            counter++;
        }
        this.buttonToggle();
    }
    checkboxChecker(id) {
        if (!id)
            super.checkboxChecker(id)
        else {
            let rows = $(`#${this.formId}`).children();
            let checks = {
                '1': [2],
                '4': [5],
                '6': [7, 8, 9, 10, 11],
                '12': [13]
            }
            let keys = Object.keys(checks)
            for (const key of keys) {
                if (id == `${this.formId}-${key}`) {
                    if ($(`#${this.formId}-${key}`).prop('checked')) {
                        for (const num of checks[key]) {
                            rows.eq(num).removeClass('d-none');
                            rows.eq(num).find("input:not([type='checkbox'],[placeholder='Other'])").prop("required", true);
                        }
                    } else {
                        for (const num of checks[key]) {
                            rows.eq(num).addClass('d-none');
                            rows.eq(num).find("input:not([type='checkbox'],[placeholder='Other'])").prop("required", false);
                        }
                    }
                }
            }
        }
    }
}

export class SecurityForm extends Form {
    hasOther = [1]
    getHTML() {
        let html = `
            <div class="card">
                <div class="card-body">
                    <form id="${this.formId}" method="POST">`
        html += this.addCheckbox(0, "Does your agency have a protection scheme for your ICT resources?")
        let titles = {
            'Policy': 'Security Policy / Guideline',
            'Back-up power': 'Back-up power unit (e.g. UPS, Generator)',
            'Encryption': 'Encryption',
            'Hardware firewall': 'Hardware firewall',
            'Software firewall': 'Software firewall',
            'Security service': 'Subscription to a security service (e.g. anti-virus software, intrusion alert)',
            'Security training': 'Regular ICT security training of employees',
            'Disaster Recovery Plan': 'Disaster Recovery Plan',
            'Digital signatures': 'Digital signatures',
            'Off-site back-up': 'Off-site back-up',
            'Physical restriction': 'Physically restricted access to critical ICT equipment',
            'Secure servers': 'Secure servers',
            'Non-local back-up media': 'Storage of back-up media in localities other than the operating environment'
        };
        html += this.addMultiselectArranged(1, "If YES, what is/are the measure/s being used by your office? (Check all applicable)", titles)
        html += `
                    <button type=submit class="btn btn-success ms-auto" id="submit-${this.formId}"> Submit </button>
                    </form>
                </div>
            </div>`
        return html
    }
    checkboxChecker(id) {
        if (!id)
            super.checkboxChecker(id)
        else {
            let rows = $(`#${this.formId}`).children();
            if (id == `${this.formId}-0`) {
                if ($(`#${this.formId}-0`).prop('checked')) {
                    rows.eq(1).removeClass('d-none');
                } else
                    rows.eq(1).addClass('d-none');
            }
        }
    }
}

export class ArchivingForm extends Form {
    hasOther = [3, 4]
    getHTML() {
        let col = 0;
        let html = `
            <div class="card">
                <div class="card-body">
                    <form id="${this.formId}" method="POST">`
        html += this.addCheckbox(col, "Does your agency have a data archiving system?")
        col++;
        let titles = {
            'Manual': 'Manual',
            'Electronic': 'Electronic',
            'Both': 'Both/Combined',
        }
        html += this.addRadio(col, "If yes, what type of data archiving system does your agency use?", titles)
        col++
        titles = ['Conventional', 'Cloud']
        html += this.addRadio(col, "If electronic data archiving is being utilized, what is the mode?", titles)
        col++
        titles = {
            'Optical disks': 'Optical disks (e.g. CD-Rom, DVD)',
            'Tape': 'Tape',
            'Microfiche': 'Microfiche',
            'Hard Disk': 'Hard Disk',
            'External Hard Drive': 'External Hard Drive',
            'Diskette': 'Diskette'
        };
        html += this.addMultiselectArranged(col, "If conventional mode, what is the medium of storage of the archived data?", titles)
        col++
        titles = {
            'Publications': 'Publications (Annual Report, Statistical Report, etc.)',
            'Audio-visual recordings': 'Audio-visual recordings',
            'Maps': 'Maps',
            'Public documents': 'Public documents (civil registration forms, passports, land titles, etc.)',
            'Letters': 'Letters, memorandum orders, communications, etc.',
            'Unprocessed': 'Unprocessed/Raw Data',
            'Photographs': 'Photographs',
        };
        html += this.addMultiselectArranged(col, "What information is archived by your agency electronically? (Check all items that are applicable)", titles)
        col++
        html += `
                    <button type=submit class="btn btn-success ms-auto" id="submit-${this.formId}"> Submit </button>
                    </form>
                </div>
            </div>`
        return html
    }
    checkboxChecker(id) {
        if (!id) {
            super.checkboxChecker(id)
        }
        else {
            let rows = $(`#${this.formId}`).children();
            if (id == `${this.formId}-0`) {
                if ($(`#${this.formId}-0`).prop('checked')) {
                    rows.eq(1).removeClass('d-none');
                } else
                    rows.eq(1).addClass('d-none');
            }

            if (id.includes(`${this.formId}-2`)) {
                if ($(`input[type='radio'][name='${this.formId}-2']:checked`).val() === "Conventional")
                    rows.eq(3).removeClass('d-none');
                else
                    rows.eq(3).addClass('d-none');
            }
        }
    }
}

export class DataCenterForm extends Form {
    hasOther = []
    getHTML() {
        let col = 0;
        let html = `
            <div class="card">
                <div class="card-body">
                    <form id="${this.formId}" method="POST">`
        html += this.addCheckbox(col, "Does your agency have a data center?")
        col++;
        html += this.addValue(col, "If yes, how many sites?")
        col++
        let titles = ['In-house', 'Outsourced']
        html += this.addRadio(col, "Please check applicable maintenance set-up:", titles)
        col++
        html += this.addCheckbox(col, "Does your agency have a back-up site?")
        col++
        html += `
                    <button type=submit class="btn btn-success ms-auto" id="submit-${this.formId}"> Submit </button>
                    </form>
                </div>
            </div>`
        return html
    }
    checkboxChecker(id) {
        if (!id) {
            super.checkboxChecker(id)
        }
        else {
            let rows = $(`#${this.formId}`).children();
            if (id == `${this.formId}-0`) {
                if ($(`#${this.formId}-0`).prop('checked')) {
                    rows.eq(1).removeClass('d-none');
                    rows.eq(2).removeClass('d-none');
                    rows.eq(3).removeClass('d-none');
                } else {
                    rows.eq(1).addClass('d-none');
                    rows.eq(2).addClass('d-none');
                    rows.eq(3).addClass('d-none');
                }
            }
        }
    }
}

export class ICTForm extends Form {
    hasOther = [0]
    getHTML() {
        let html = `
            <div class="card">
                <div class="card-body">
                    <form id="${this.formId}" method="POST">
                    <h5 class="card-title">${this.title}</h5>`
        let titles = {
            'Budget': "No budget or insufficient budget",
            'Opposition': "Opposition or reluctance of stakeholders",
            'Recruitment': "Difficulty in recruiting and/or retaining qualified ICT personnel",
            'Bandwidth': "Unavailability of required bandwidth to support system/s",
            'Delayed funding': "Problems in contract management for outsourced services",
            'Support': "Delay in the release of projects funds",
            'ICT skill': "Lack of support by management",
            'Usage': "Low level of ICT skills among employees",
            'Procurement': "Not used or seldom used by intended users and/or clients",
            'Contracts': "Problems in procurement",
        }
        html += this.addMultiselectArranged(0, "", titles)
        html += `
                    <button type=submit class="btn btn-success ms-auto my-2" id="submit-${this.formId}"> Submit </button>
                    </form>
                </div>
            </div>`
        return html
    }
    checkboxChecker() {
    }
}