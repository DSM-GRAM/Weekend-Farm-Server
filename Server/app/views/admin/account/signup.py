from flask import Blueprint, abort, request
from flask_restful import Api
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.views import BaseResource
from app.docs.admin.account.signup import ADMIN_SIGNUP_POST
from app.models.admin.account.account import AdminModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/signup')
class SignupAdmin(BaseResource):
    @swag_from(ADMIN_SIGNUP_POST)
    def post(self):
        """
        관리자 회원가입
        """
        admin_id = request.json['id']
        admin_pw = request.json['pw']
        admin_name = request.json['name']
        admin_phone_number = request.json['phone_number']

        if AdminModel.objects(id=admin_id).first():
            abort(409)

        admin_hashed_pw = generate_password_hash(admin_phone_number)

        AdminModel(
           id=admin_id,
           pw=admin_pw,
           name=admin_name,
           phone_number=admin_hashed_pw
        ).save()

        return '', 201
