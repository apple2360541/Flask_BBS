$(function () {
    $("#captcha-img").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var src = self.attr("src");
        var newsrc = xtparam.setParam(src, "xx", Math.random());
        self.attr("src", newsrc)
    })
});

$(function () {
    $("#send-code").click(function (event) {
        event.preventDefault();
        var telephone = $("input[name=telephone]");
        var salt = 'dqgeryeu5sdg56sdg486575es#$%';
        var phone = telephone.val();
        var myreg = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
        if (!myreg.test(phone)) {
            zlalert.alertInfoToast("请输入正确手机号");
            return
        }
        var self = $(this);
        var timestamp = (new Date).getTime();
        console.log(timestamp);
        var sign = md5(timestamp + telephone + salt);
        console.log(sign);

        base.post({
            "url": "/common/sms_captcha/",
            "data": {
                "telephone": telephone,
                "timestamp": timestamp,
                "sign": sign
            },
            "success": function (data) {
                console.log(data);
                if (data.code == 200) {
                    // telephone.val("");

                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;

                        if (timeCount <= 0) {
                            self.text("发送验证码");
                            self.removeAttr("disabled");
                            clearInterval(timer)
                        } else {
                            self.text(timeCount + "s");
                            self.attr("disabled", 'disabled');
                        }
                    }, 1000);

                    zlalert.alertSuccessToast("验证码发送成功")
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
    })
});
$(function () {
    $("#register").click(function (event) {
        event.preventDefault();

        var input_phone = $("input[name=telephone]");
        var input_code = $("input[name=code]");
        var input_username = $("input[name=username]");
        var input_password = $("input[name=password]");
        var input_re_password = $("input[name=re_password]");
        var graph_captcha = $("input[name=graph_captcha]");
        var telephone = input_phone.val();
        var code = input_code.val();
        var username = input_username.val();
        var password = input_password.val();
        var re_password = input_re_password.val();
        base.post({
            "url": "/signup/",
            "data": {
                "telephone": telephone,
                "code": code,
                "username": username,
                "password": password,
                "re_password": re_password,
                "graph_captcha": graph_captcha,
            },
            "success": function (data) {
                console.log(data);
                if (data.code == 200) {
                    // telephone.val("");
                    window.location="/";


                    // zlalert.alertSuccessToast("注册成功")
                } else {
                    zlalert.alertError(data.msg);
                    // alert(data.msg)
                }
            },
            "fail": function (error) {
                console.log(error);
                zlalert.alertError(error);
            }

        });

    })

});