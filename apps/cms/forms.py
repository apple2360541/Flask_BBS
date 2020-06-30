from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo, ValidationError
from ext import redis
from flask import g


class BaseForm(Form):
    def getError(self):
        return self.errors.popitem()[1][0]
    def validate(self):
        return super(BaseForm,self).validate()


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入邮箱"), InputRequired()])
    password = StringField(validators=[Length(6, 20, message="请输入6到16位密码")])
    remember = IntegerField()


class ResetPsdForm(BaseForm):
    old_password = StringField(validators=[Length(6, 20, message="请输入6到16位旧密码")])
    new_password = StringField(validators=[Length(6, 20, message="请输入6到16位新密码")])
    re_password = StringField(validators=[EqualTo("new_password", message="密码不一致")])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message="请输入邮箱")])
    code = StringField(validators=[Length(6, 6, message="请输入6位验证码")])

    def validate_code(self, field):
        code = field.data
        email = self.email.data
        print(email)
        redis_code = redis.get(email)
        print(code)
        print(redis_code)

        if not redis_code or redis_code.lower() != code.lower():
            raise ValidationError("验证码不正确")

    def validate_email(self, field):
        email = field.data
        current_email = g.cms_user.email
        print("验证邮箱")
        print(current_email)
        print(email)
        if email == current_email:
            raise ValidationError("邮箱不可修改为一样")
