
$(document).ready(function () {
    $.ajax({
        url: "https://localhost:44393/api/business",
        type: "GET",
        success: function (result) {

            result.forEach(function (array) {
                console.log(array);
            });
        }
    });
});