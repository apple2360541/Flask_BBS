from ext import db
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash
import enum
from uuid import uuid4


def gen_uuid():
    return uuid4().hex


from datetime import datetime


class Gender(enum.Enum):
    UNKNOW = 0
    MALE = 1
    FEMALE = 2
    SECRET = 3


class Common():
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class FontUser(db.Model):
    __tablename__ = "font_user"
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    username = db.Column(db.String(11), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    realName = db.Column(db.String(50))
    avatar = db.Column(db.String(50))
    signature = db.Column(db.String(50))
    gender = db.Column(db.Enum(Gender), default=Gender.UNKNOW)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs.get("password")
            kwargs.pop("password")
        super(FontUser, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result


# 自关联一对一和一对多
class Category(db.Model):
    __tablename__ = "t_category"
    id = db.Column(db.String(32), primary_key=True, default=gen_uuid, comment="主键")
    name = db.Column(db.String(20), nullable=False, comment="名字")
    parent_id = db.Column(db.ForeignKey('t_category.id'), on_delete='CASCADE', onupdate='CASCADE', index=True)
    parent = db.relationship('Category', remote_side=[id])
    children = db.relationship('Category', remote_side=[parent_id])


class FontGoods(db.Model, Common):
    __tablename__ = 't_front_good'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.ForeignKey('t_category.id'))
    category = db.relationship('Category', backref=db.backref('goods'))

