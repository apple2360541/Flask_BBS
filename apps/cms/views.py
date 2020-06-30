from flask import (Blueprint, render_template, views, request, session, redirect, url_for, g, jsonify)
from .forms import LoginForm, ResetPsdForm, ResetEmailForm
from .models import CMSUser, CMSPermission
from .decorators import login_required, permission_required
from config import CMS_USER_ID
from ext import db
from utils import restful
from ext import mail, redis
from flask_mail import Message
import string
import random

cms = Blueprint("cms", __name__, url_prefix="/cms")


@cms.route("/")
@login_required
def index():
    # user=g.cms_user
    return render_template('cms/cms_index.html')


@cms.route("/comments/")
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template("cms/cms_comments.html")


@cms.route("/posts/")
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    return render_template("cms/cms_posts.html")


@cms.route("/boarders/")
@login_required
@permission_required(CMSPermission.BORDER)
def boarders():
    return render_template("cms/cms_borders.html")


@cms.route("/fontusers/")
@login_required
@permission_required(CMSPermission.FONTUSER)
def fontusers():
    return render_template("cms/cms_fontuser_manage.html")


@cms.route("/backusers/")
@login_required
@permission_required(CMSPermission.CMSUSER)
def backusers():
    return render_template("cms/cms_backuser_manage.html")


@cms.route("/groups/")
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def groups():
    return render_template("cms/cms_group_manage.html")


@cms.route("/resetemail/cms/email/")
@login_required
def send_email():
    email = request.args.get("email")
    if email:
        source = list(string.ascii_letters)
        # source.extend(list(range(0, 10)))
        source.extend(map(lambda x: str(x), range(0, 10)))
        # source.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        code = "".join(random.sample(source, 6))
        print(code)

        # redis.expire(email, 10 * 60)
        message = Message(subject="Python论坛邮箱验证码", recipients=[email], body="您的验证码是%s,有效期10分钟!" % code)
        try:
            mail.send(message)
        except:
            return restful.server_error("服务器异常")
        redis.set(email, code, 60 * 10)
        return restful.success("发送成功")
    else:
        restful.params_error("请输入邮箱地址")


@cms.route("/logout/")
def logout():
    del session[CMS_USER_ID]
    return redirect(url_for("cms.login"))


@login_required
@cms.route("/profile/")
def profile():
    return render_template("cms/cms_profile.html")


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template("cms/cms_resetpwd.html")

    def post(self):
        form = ResetPsdForm(request.form)
        if form.validate():
            old = form.old_password.data
            password = form.new_password.data
            cms_user = g.cms_user
            if cms_user.check_password(old):
                cms_user.password = password
                db.session.commit()

                return restful.success(msg="修改成功")
            else:
                return restful.params_error(msg="密码错误")
        else:

            return restful.params_error(msg=form.getError())


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True

                return redirect(url_for('cms.index'))
            else:
                return self.get(message="邮箱或密码不正确")



        else:

            return self.get(message=form.getError())


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template("cms/cms_resetemail.html")

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            redis.delete(email)
            g.cms_user.email = email
            db.session.commit()
            print("删除%s" % email)
            return restful.success("修改成功")
        else:
            return restful.params_error(form.getError())


cms.add_url_rule("/login/", view_func=LoginView.as_view('login'))
cms.add_url_rule("/resetpwd/", view_func=ResetPwdView.as_view('resetpwd'))
cms.add_url_rule("/resetemail/", view_func=ResetEmailView.as_view('resetemail'))
