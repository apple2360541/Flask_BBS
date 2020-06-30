from app import create_app
from ext import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.cms import models as cms_model
from apps.fronts import models as font_model
CMSUser = cms_model.CMSUser
CMSRole = cms_model.CMSRole
FontUser=font_model.FontUser
CMSPermission = cms_model.CMSPermission
app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.option("-u", '--username', dest='username')
@manager.option("-p", '--password', dest='password')
@manager.option("-e", '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username, password, email)

    db.session.add(user)
    db.session.commit()
    print("创建成功%s" % username)


@manager.command
def create_role():
    # 1.创建角色
    visitor = CMSRole(name="访问者", desc="只能访问，不能修改删除")
    visitor.permissions = CMSPermission.VISTOR
    #
    # 2.运营人员
    operator = CMSRole(name="运营", desc="修改信息，管理帖子，评论，管理前后台用户")
    operator.permissions = CMSPermission.VISTOR | CMSPermission.COMMENTER | CMSPermission.POSTER | CMSPermission.FONTUSER
    # 3.管理员
    admin = CMSRole(name="管理员", desc="修改信息，管理帖子，评论，版块")
    admin.permissions = CMSPermission.VISTOR | CMSPermission.COMMENTER | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.BORDER | CMSPermission.FONTUSER

    # 4.开发者
    developer = CMSRole(name="开发者", desc="开发人员专用")
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])

    db.session.commit()


@manager.option("-e", "--email", dest="email")
@manager.option("-n", "--name", dest="name")
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print("添加成功")
        else:
            print("%s没有这个角色" % name)
    else:
        print("%s这个邮箱没有用户" % email)

@manager.option("-t","--phone",dest="phone")
@manager.option("-u","--username",dest="username")
@manager.option("-p","--password",dest="password")
@manager.option("-e","--email",dest="email")
def add_font_user(phone,username,password,email):
    user=FontUser()
    user.username=username
    user.phone=phone
    user.password=password
    user.email=email
    db.session.add(user)
    db.session.commit()
@manager.command
def test_permission():
    user = CMSUser.query.first()
    print(user)
    if user and user.is_developer(CMSPermission.VISTOR):
        print("有权限")
    else:
        print("没有权限")


if __name__ == '__main__':
    manager.run()
