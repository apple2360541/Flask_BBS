from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from redis import Redis,StrictRedis
redis = StrictRedis("112.124.15.96", password="apple2882960", port=6379,decode_responses=True)
db=SQLAlchemy()
mail=Mail()