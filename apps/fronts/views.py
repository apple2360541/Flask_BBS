from flask import (Blueprint,
                   views,
                   request,
                   render_template, make_response, session)
from utils.captcha import Captcha
from io import BytesIO
from .code import send_code, generate_code
from utils import restful
from ext import redis
from requests import Request
from .forms import SignupForm, LoginForm
from .models import FontUser
from ext import db
from config import FRONT_USER_ID
front = Blueprint("front", __name__)


@front.route("/")
def index():
    return "front index "


class LoginView(views.MethodView):
    def get(self):
        return render_template("front/front_login.html")

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FontUser.query.filter_by(phone=telephone).first()
            if user and user.check_password(password):
                session[FRONT_USER_ID]=user.id
                if remember:
                    session.permanent=True
            else:
                return restful.params_error("手机号或密码错误")


        else:
            return restful.params_error(form.getError())


class ForgetView(views.MethodView):
    def get(self):
        render_to = request.referrer
        return render_template("front/front_login.html")

    def post(self):
        pass


@front.route("/captcha/")
def graph_captcha():
    # 获取验证码
    text, image = Captcha.gene_graph_captcha()
    # Bytes,自截留
    out = BytesIO()
    image.save(out, "png")
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = "image/png"
    redis.set(text.lower(), text.lower(), ex=60 * 5)
    return resp


class SignupView(views.MethodView):
    def get(self):
        render_to = request.referrer
        return render_template("front/front_signup.html")

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password.data
            user = FontUser(username=username, phone=telephone, password=password)
            db.session.add(user)
            db.session.commit()
            restful.success()
        else:
            restful.params_error(form.getError())


@front.route("/sms_captcha/", methods=["POST"])
def smf_captcha():
    phone = request.form.get("telephone")
    if not phone or len(phone) != 11:
        return restful.params_error("请输入正确手机号")
    code = generate_code()
    if send_code(phone, code):
        redis.hset(phone, "register", code)
        redis.expire(phone, 60 * 10)
        return restful.success("验证码发送成功")
    else:
        return restful.server_error("发送失败")


front.add_url_rule("/signup/", view_func=SignupView.as_view("signup"))
front.add_url_rule("/login/", view_func=LoginView.as_view("login"))
front.add_url_rule("/forget/", view_func=ForgetView.as_view("forget"))
