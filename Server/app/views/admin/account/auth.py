from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from flasgger import swag_from
from werkzeug.security import check_password_hash

from app.models.admin.account.account import AdminModel
from app.views import BaseResource
from app.docs.admin.account.auth import ADMIN_AUTH_POST


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/login')
class AccountManagement(BaseResource):
    @swag_from(ADMIN_AUTH_POST)
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
