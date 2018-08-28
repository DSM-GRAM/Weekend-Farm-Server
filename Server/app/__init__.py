from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger


def create_app(*config_obj):
    app_ = Flask(__name__)

    for config in config_obj:
        app_.config.from_object(config)

    JWTManager().init_app(app_)
    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)

    return app_
