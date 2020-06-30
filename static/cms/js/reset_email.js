$(function () {
    $("#send_mail").click(function (event) {
        event.preventDefault();
        var getBtn = $("input[name=email]");
        var email = getBtn.val();
        if (!email) {
            zlalert.alertInfoToast("请输入邮箱");
            return
        }
        base.get({
            "url": "cms/email/",
            "data": {"email": email},
            "success": function (data) {
                if (data.code = 200) {
                    zlalert.alertSuccessToast("验证码发送成功,请注意查收")

                } else {
                    zlalert.alertErrorToast(data.msg)
                }
            },
            "fail": function (error) {
                zlalert.alertNetworkError()
            }
        })
    });

});
$(function () {
    $("#update_email").click(function (event) {
        event.preventDefault();
        var getBtn = $("input[name=email]");
        var codeInput = $("input[name=code]");
        var email = getBtn.val();
        var code = codeInput.val();
        if (!email) {
            zlalert.alertInfoToast("请输入邮箱");
            return
        }
        if (!code) {
            zlalert.alertInfoToast("请输入验证码");
            return
        }
        base.post({
            "url": "/cms/resetemail/",
            "data": {"email": email, "code": code},
            "success": function (data) {
                console.log(data);
                if (data.code == 200) {
                    getBtn.val("");
                    codeInput.val("");
                    zlalert.alertSuccessToast("修改成功")

                } else {
                    zlalert.alertInfoToast(data.msg)
                }
            },
            "fail": function (error) {
                console.log(error);
                zlalert.alertNetworkError()
            }
        })
    })
});