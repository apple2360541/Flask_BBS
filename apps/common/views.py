from flask import Blueprint, request, views, render_template
from apps.fronts.code import generate_code, send_code
from utils import restful
from ext import redis
from .forms import SMSCaptachaForm

common = Blueprint("common", __name__, url_prefix='/common')


class CommonIndexView(views.MethodView):
    def get(self):
        return render_template("common/Index.html")

    def post(self):
        username = request.args.get("username")
        name = request.form.get("usernae")
        print(username)
        print(name)
        return restful.success("成功")


# @common.route("/")
# def index():
#     return "common index "
common.add_url_rule("/", view_func=CommonIndexView.as_view("index"))


@common.route("/sms_captcha/", methods=["POST"])
def smf_captcha():
    form = SMSCaptachaForm(request.form)
    if form.validate():
        phone = form.telephone.data
        code = generate_code()
        if send_code(phone, code):
            redis.hset(phone, "register", code)
            redis.expire(phone, 60 * 10)
            return restful.success("验证码发送成功")
        else:
            return restful.server_error("发送失败")
    else:
        return restful.params_error("参数错误")
