//this file performs all event watching.

import './office_code.js';
import { errorStatus, successStatus } from './status.js';
import { ANNEXA5 } from './annexa5.js'

function getFormData(form, callback) {
    let formId = form.formId;
    let formdata = {
        "form": formId.replaceAll('-', '_')
    };

    $.post(`form_submit/get.php`, formdata, function (result) {
        if (!form.isTable) 
            form.parse(result, callback)
        else if (result !== null && result !== "") { //if data doesn't exist, then don't do anything else
            form.parse(result, callback)
        }
    }).fail(function () {
        errorStatus([`Failed to retrieve data for form ${formId}. Try refreshing.`]);
    });
}

export function refreshData(form) {
    let callback = function (elements) {
        form.setBodyHTML(elements)
    }
    getFormData(form, callback)
    if (form.isTable)
        form.resetRows();
}

function othersHandler(form) {
    let formId = form.formId
    $(`#${formId}`).on('change', function (event) {
        let type = $(event.target).prop('tagName')
        let value = $(event.target).val()
        let id = $(event.target).prop('id')
        form.othersHandler(id, value, type)
    });
}

for (const section of ANNEXA5) {
    for (const form of section['tables']) {
        let formId = form.formId;

        //on page start, refresh all data
        $(`#${section.sectionId}`).append(form.getHTML());
        refreshData(form)

        //perform event watching
        if (form.isTable) {
            //add row event
            $(`#add-row-${form.formId}`).click(function () {
                form.addRow()
            });
            //delete row event
            $(`#delete-row-${form.formId}`).click(function () {
                form.deleteRow()
            });
            //others event
            othersHandler(form);
        }
        else {
            $(`#${formId}`).on('change', function (event) {
                let id = $(event.target).prop('id')
                form.checkboxChecker(id); //then make the function run on change event
            })
            $(`#delete-${form.formId}`).click(function () {
                console.log(`clicked`)
                let form_data = {
                    "formId": formId.replaceAll('-', '_')
                }
                $.post(`form_submit/delete.php`, form_data, function (data) {
                    try {
                        console.log(data)
                        data = JSON.parse(data);
                        if (data['success']) {
                            //refresh table
                            successStatus(['Deletion successful!'])
                            refreshData(form);
                        } else {
                            errorStatus(Object.values(data['errors']));
                        }
                    } catch (SyntaxError) {
                        console.log(SyntaxError)
                        errorStatus(['Deletion error.']);
                    }
                }).fail(function (data) {
                    errorStatus(['Connection error. Submission failed.'])
                });
            })
        }

        //submit event
        $(`#${form.formId}`).submit(function (event) {
            event.preventDefault();
            let form_data;
            if (form.isTable) {
                //need to know how many objects got submitted
                let count = 0;
                while ($(`#${form.formId}-${count}-0`).val()) {
                    count++;
                }
                console.log(form.formId, count);
                if (count < 1) {
                    errorStatus(["Rows not retrieved."]);
                }
                else {
                    form_data = form.getSubmissionData(count);
                }
            } else {
                form_data = form.getSubmissionData(form.hasOther);
            }
            if (form_data) {
                $.post(`form_submit/insert.php`, form_data, function (data) {
                    try {
                        console.log(data)
                        data = JSON.parse(data);
                        if (data['success']) {
                            //refresh table
                            successStatus(['Submission successful!'])
                            refreshData(form);
                        } else {
                            errorStatus(Object.values(data['errors']));
                        }
                    } catch (SyntaxError) {
                        console.log(SyntaxError)
                        errorStatus(['Submission error. Please double check for any repeated types.']);
                    }
                }).fail(function (data) {
                    errorStatus(['Connection error. Submission failed.'])
                });
            }
        });
    }
}