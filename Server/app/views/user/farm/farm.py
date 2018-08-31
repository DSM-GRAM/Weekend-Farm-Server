from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.user import UserModel
from app.models.apply import ApplyModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/farm'


@api.resource('')
class FarmInform(BaseResource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        유저 Farm 메인 화면
        """
        apply = ApplyModel.objects(user=UserModel.objects(id=get_jwt_identity()).first()).first()


        a = {
            'date': apply.period,
            'money':
        }
        pass