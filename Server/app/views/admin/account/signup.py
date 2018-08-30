from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.docs.admin.account.signup import SIGNUP_POST


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/signup')
class SignupAdmin(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        """
        관리자 회원가입
        """
        pass

