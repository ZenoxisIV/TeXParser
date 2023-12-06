import { errorStatus, successStatus } from "./status.js"
import { ANNEXA5 } from "./annexa5.js"
import { refreshData } from "./form.js"


function changeCurrentCode() {
    $.get("form_submit/office_code-get.php", function (result) {
        if (result !== null && result !== "") {
            let office_ID = JSON.parse(result).slice(0, 2);
            let year = JSON.parse(result).slice(2, 6);
            $('#current-code').html(`Office: <span class='text-success'>${office_ID}</span>, Year: <span class='text-success'>${year}</span>`)
        }
    })
}

$(document).ready(function () {
    $("#form_data").submit(function (event) {
        let form_data = {
            office_ID: $("#office_ID").val(),
            year: $("#year").val(),
        };

        $.post("form_submit/office_code.php", form_data, function (data) {
            data = JSON.parse(data);
            if (!data.success) {
                errorStatus(Object.values(data['errors']));
            } else {
                successStatus([`Form data exists!`]);
                for (const section of ANNEXA5) {
                    for (const form of section['tables']) {
                        refreshData(form)
                    }
                }
                changeCurrentCode()
            }
        }).fail(function (data) {
            console.log("fail");
        });

        event.preventDefault();

    });
}); 