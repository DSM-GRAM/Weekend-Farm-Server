from flask import Blueprint, abort, request
from flask_restful import Api
from flasgger import swag_from
from werkzeug.security import generate_password_hash

from app.views import BaseResource
from app.docs.user.account.signup import USER_SIGNUP_POST
from app.models.admin.account.account import AdminModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/login')
class AccountManagement(BaseResource):
    @swag_from(USER_SIGNUP_POST)
    def post(self):
        """
        관리자 로그인
        """
        payload = request.json

        admin_id = payload['id']
        admin_pw = payload['pw']

        admin = AdminModel.objects(id=id).first()

        if admin is None:
            abort(406)

        return {
            'access_token': create_access_token(identity=admin_id),
            'refresh_token': create_refresh_token(identity=admin_id)
        }, 200 if check_password_hash(admin.pw, admin_pw) else abort(406)