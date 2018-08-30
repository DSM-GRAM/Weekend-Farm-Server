from flask import Blueprint, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.docs.admin.account.signup import SIGNUP_POST
from app.models.admin.account.account import AdminModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/signup')
class SignupAdmin(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        id = request.json['id']
        pw = request.json['pw']
        name = request.json['name']
        phone_number = request.json['phone_number']

        if AdminModel.object(id=id).first():
            abort(406)

        AdminModel(
           id=id,
           pw=pw,
           name=name,
           phone_number=phone_number
       ).save()

        return '', 201
