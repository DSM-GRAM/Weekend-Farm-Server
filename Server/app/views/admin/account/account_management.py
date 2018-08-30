from flask import Blueprint
from flask_restful import Api
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/')
class AccountManagement(BaseResource):
    @
