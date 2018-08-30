from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.docs.admin.account.account_management import ADMIN_ADD_INFORM


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/manage')
class AccountManagement(BaseResource):
    @swag_from(ADMIN_ADD_INFORM)
    def post(self):
        pass
