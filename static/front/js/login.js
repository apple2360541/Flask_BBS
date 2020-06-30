$(function () {
    $("#front-login").click(function (event) {
        event.preventDefault();
        var input_telephone = $("input[name=telephone]");
        var input_password = $("input[name=password]");
        var input_remember = $("input[name=remember]");
        base.post({
            "url": "/login/",
            "data": {
                "telephone": input_telephone.val(),
                "password": input_password.val(),
                "remember": input_remember.checked ? 1 : 0
            },
            "success": function (data) {
                if (data.code == 200) {
                    var back = $("#return-to-span").text();
                    if (back) {
                        window.location = back;
                    } else {
                        window.location = "/";
                    }
                } else {
                    zlalert.alertError(data.msg)
                }

            },
            "fail": function (error) {
                zlalert.alertError(error)
            }
        })
    })
});