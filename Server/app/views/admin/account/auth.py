from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.docs.admin.account.auth import AUTH_POST


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/login')
class AccountManagement(BaseResource):
    @swag_from(AUTH_POST)
    def post(self):
        pass


# @api.resource('/')
# class