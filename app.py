from flask import Flask
from apps.cms import cms
from apps.common import common
from apps.fronts import front
import config
from flask_wtf import CSRFProtect
from ext import db,mail


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(cms)
    app.register_blueprint(common)
    app.register_blueprint(front)
    db.init_app(app)
    mail.init_app(app)
    CSRFProtect(app)
    return app


if __name__ == '__main__':
    app = create_app()

    app.run()
