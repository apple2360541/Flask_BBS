# encoding:utf-8
import os
from datetime import datetime, timedelta

HOST = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'apple2882960'
DB_NAME = 'bbs'
# dialect+driver://username:password@host:port/database
DB_URI = 'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8'.format(USERNAME=USERNAME,
                                                                                             PASSWORD=PASSWORD,
                                                                                             HOST=HOST,
                                                                                             PORT=PORT, DB_NAME=DB_NAME)
DEBUG = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATES_AUTO_RELOAD = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = "s"
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
CMS_USER_ID = "user_id"
FRONT_USER_ID="front_userid"
JSON_AS_ASCII = False
# SEVER_NAME="androidjdk.com:5000"
# 邮箱配置
MAIL_SERVER = "smtp.126.com"
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False

MAIL_USERNAME = "apple9302@126.com"
MAIL_PASSWORD = "apple2882960"
MAIL_DEFAULT_SENDER = "apple9302@126.com"

