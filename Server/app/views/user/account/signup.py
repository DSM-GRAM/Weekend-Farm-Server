from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from flasgger import swag_from
from werkzeug.security import check_password_hash

from app.views import BaseResource
from app.docs.user.account.signup import USER_SIGNUP_POST
from app.models.user.account.account import UserModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


@api.resource('/signup')
class AccountManagement(BaseResource):
    @swag_from(USER_SIGNUP_POST)
    def post(self):
        """
        유저 회원가입
        """
        payload = request.json

        user_id = payload['id']
        user_pw = payload['pw']

        user = UserModel.objects(id=user_id).first()

        if user is None:
            abort(406)

        return {
            'access_token': create_access_token(identity=user_id),
            'refresh_token': create_refresh_token(identity=user_id)
        }, 200 if check_password_hash(user.pw, user_pw) else abort(406)
