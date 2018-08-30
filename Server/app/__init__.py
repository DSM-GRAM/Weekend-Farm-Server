from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from app.views import Router


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    JWTManager().init_app(app_)
    Router().init_app(app_)

    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)

    return app_
