$(function () {
    $("#update_psd").click(function (event) {
        event.preventDefault();
        var oldPwd = $("input[name=old_psd]");
        var newPwd = $("input[name=new_psd]");
        var rePwd = $("input[name=re_psd]");
        var oldP = oldPwd.val();
        var newP = newPwd.val();
        var reP = rePwd.val();
        console.log(oldP);
        console.log(newP);
        console.log(reP);
        base.post({
            "url": "/cms/resetpwd/",
            "data": {
                "old_password": oldP,
                "new_password": newP,
                "re_password": reP,
            },
            "success": function (data) {
                console.log(data);
                if (data.code == 200) {
                    oldPwd.val("");
                    newPwd.val("");
                    rePwd.val("");

                    zlalert.alertSuccessToast("密码修改成功")
                } else {
                    zlalert.alertError(data.msg);
                    // alert(data.msg)
                }
            },
            "fail": function (error) {
                console.log(error);
                zlalert.alertError(error);
            }
        })
    });


});