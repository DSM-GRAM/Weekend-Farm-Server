from flask import Blueprint, abort, request
from flask_restful import Api
from werkzeug.security import generate_password_hash

from app.views import BaseResource
from app.models.user import UserModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'


@api.resource('/signup')
class SignupAdmin(BaseResource):
    def post(self):
        """
        유저 회원가입
        """
        user_id = request.json['id']
        user_pw = request.json['pw']
        user_name = request.json['name']
        user_phone_number = request.json['phoneNum']

        if UserModel.objects(id=user_id).first():
            abort(409)

        user_hashed_pw = generate_password_hash(user_pw)

        UserModel(
            id=user_id,
            pw=user_hashed_pw,
            name=user_name,
            phone_number=user_phone_number
        ).save()

        return '', 201
