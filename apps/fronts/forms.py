from ..cms import BaseForm
from wtforms import StringField
from wtforms.validators import Required, Length, Regexp, EqualTo, ValidationError
from ext import redis


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[3,6,7,8,9]\d{9}", message="请输入正确的手机号码")])
    code = StringField(validators=[Regexp(r"\w{4}", message="请输入四位数字验证码")])
    username = StringField(validators=[Regexp(r".{2,20}", message="请输入正确格式的用户名")])
    password = StringField(validators=[Regexp("r[0-9a-zA-Z_\.]{6,20}", message="请输入正确格式的密码")])
    re_password = StringField(validators=[EqualTo("password", message="密码不一致")])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}", message="请输入正确格式的图形验证码")])

    def validate_code(self, field):
        code = field.data
        telephone = self.telephone.data
        cache_code = redis.hget(telephone, "register")
        if not cache_code or cache_code.lower() != code.lower():
            raise ValidationError(message="短信验证码错误")

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph = redis.get(graph_captcha.lower())
        if not graph or graph_captcha.lower() != graph:
            raise ValidationError(message="图形验证码错误")


class LoginForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[3,6,7,8,9]\d{9}", message="请输入正确的手机号码")])
    password = StringField(validators=[Regexp("r[0-9a-zA-Z_\.]{6,20}", message="请输入正确格式的密码")])
    remember=StringField()
